#!/usr/bin/env python3
"""Validate the canonical Hiatus BOM CSV using Python's standard library."""
from __future__ import annotations

import argparse
import csv
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime
from decimal import Decimal, InvalidOperation
from pathlib import Path

EXPECTED_HEADERS = [
    "row", "category", "component", "cost", "cost_basis",
    "purchase_date", "purchase_status", "notes",
]
CATEGORIES = {
    "Camper", "Electrical", "Hardware", "Tools", "Appliances", "Plumbing",
    "Interior", "Consumables", "Vehicle", "Vehicle Electronics", "Services",
}
STATUSES = {
    "Purchased", "Partially Purchased", "Included", "Selected", "Planned",
    "Deferred", "Returned", "Retired",
}
COST_BASES = {
    "item_subtotal", "purchase_record", "delivered_total", "order_remainder", "owner_estimate",
    "planning_estimate", "included", "not_applicable", "unknown",
}
ACTUAL_DATE_STATUSES = {"Purchased", "Partially Purchased", "Included", "Returned"}
STATUS_PREFIX = re.compile(r"^(?:DEPRECATED|OPTIONAL|OBSOLETE|RESOLVED|NOT REQUIRED|REMOVE|TEMP)\b", re.I)
ASIN = re.compile(r"\bB0[A-Z0-9]{8}\b")
PRIVATE_PATTERNS = {
    "Amazon account-order URL": re.compile(r"amazon\.[^\s,]+/(?:gp/your-account/order-details|your-orders/order-details)", re.I),
    "raw order identifier": re.compile(r"\border\s*(?:id|number)\s*[:#]\s*[A-Z0-9-]{8,}", re.I),
    "secret/token assignment": re.compile(r"(?i)(?:api[_-]?key|access[_-]?token|secret[_-]?key)\s*[:=]\s*[A-Za-z0-9_-]{12,}"),
}


def normalized_component(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", value.lower()).strip()


def validate(path: Path) -> int:
    errors: list[str] = []
    with path.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != EXPECTED_HEADERS:
            errors.append(f"headers {reader.fieldnames!r} != {EXPECTED_HEADERS!r}")
        rows = list(reader)

    ids: set[int] = set()
    components: defaultdict[str, list[str]] = defaultdict(list)
    asins: defaultdict[str, list[str]] = defaultdict(list)
    total = Decimal("0")

    for line_no, row in enumerate(rows, start=2):
        row_id = row.get("row", "")
        prefix = f"line {line_no} / row {row_id or '?'}"
        if row.keys() != dict.fromkeys(EXPECTED_HEADERS).keys():
            errors.append(f"{prefix}: malformed row width")
            continue

        if not re.fullmatch(r"[1-9][0-9]*", row_id):
            errors.append(f"{prefix}: row must be a positive integer without leading zeros")
        else:
            numeric_id = int(row_id)
            if numeric_id in ids:
                errors.append(f"{prefix}: duplicate row ID")
            ids.add(numeric_id)

        for key, value in row.items():
            if value != value.strip():
                errors.append(f"{prefix}: outer whitespace in {key}")

        category = row.get("category", "")
        status = row.get("purchase_status", "")
        basis = row.get("cost_basis", "")
        component = row.get("component", "")
        notes = row.get("notes", "")
        cost = row.get("cost", "")
        purchase_date = row.get("purchase_date", "")

        if category not in CATEGORIES:
            errors.append(f"{prefix}: invalid category {category!r}")
        if status not in STATUSES:
            errors.append(f"{prefix}: invalid purchase_status {status!r}")
        if basis not in COST_BASES:
            errors.append(f"{prefix}: invalid cost_basis {basis!r}")
        if not component:
            errors.append(f"{prefix}: blank component")
        elif STATUS_PREFIX.search(component):
            errors.append(f"{prefix}: lifecycle prefix belongs in status/notes, not component")
        if not notes:
            errors.append(f"{prefix}: blank notes")
        elif len(notes) < 40:
            errors.append(f"{prefix}: notes are too terse to identify source/role ({len(notes)} characters)")
        elif len(notes) > 500:
            errors.append(f"{prefix}: notes exceed 500 characters ({len(notes)})")
        elif notes[-1] not in ".!?":
            errors.append(f"{prefix}: notes must end with terminal punctuation")
        if status in {"Planned", "Selected", "Deferred"} and re.match(
            r"^(?:Not required|Removed from|Superseded|Deprecated|Obsolete|No longer needed)\b",
            notes,
            re.I,
        ):
            errors.append(f"{prefix}: retired semantics conflict with active planning status")

        normalized = normalized_component(component)
        if normalized:
            components[normalized].append(row_id)
        for asin in ASIN.findall(notes):
            asins[asin].append(row_id)
        for label, pattern in PRIVATE_PATTERNS.items():
            if pattern.search(notes):
                errors.append(f"{prefix}: contains {label}")

        if cost:
            if not re.fullmatch(r"[0-9]+\.[0-9]{2}", cost):
                errors.append(f"{prefix}: cost must use two decimal places")
            try:
                parsed = Decimal(cost)
                if parsed < 0:
                    errors.append(f"{prefix}: cost cannot be negative")
                total += parsed
            except InvalidOperation:
                errors.append(f"{prefix}: invalid numeric cost")
        elif basis != "unknown":
            errors.append(f"{prefix}: blank cost requires cost_basis unknown")

        if cost == "0.00":
            expected = "included" if status == "Included" else "not_applicable"
            if basis != expected:
                errors.append(f"{prefix}: zero cost requires cost_basis {expected}")
        if basis == "owner_estimate" and status not in {"Selected", "Planned", "Deferred", "Retired"}:
            errors.append(f"{prefix}: owner_estimate is not valid for status {status}")

        if purchase_date:
            try:
                datetime.strptime(purchase_date, "%Y-%m-%d")
            except ValueError:
                errors.append(f"{prefix}: purchase_date is not YYYY-MM-DD")
            if status not in ACTUAL_DATE_STATUSES:
                errors.append(f"{prefix}: unpurchased/retired row cannot carry purchase_date")

    for normalized, row_ids in components.items():
        if len(row_ids) > 1:
            errors.append(f"duplicate normalized component {normalized!r}: rows {', '.join(row_ids)}")
    for asin, row_ids in asins.items():
        if len(set(row_ids)) > 1:
            errors.append(f"ASIN {asin} appears in multiple rows: {', '.join(row_ids)}")

    if errors:
        print(f"BOM VALIDATION FAILED: {len(errors)} issue(s)", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    category_counts = Counter(row["category"] for row in rows)
    status_counts = Counter(row["purchase_status"] for row in rows)
    print(
        f"BOM VALIDATION PASSED: rows={len(rows)} unique_ids={len(ids)} "
        f"categories={len(category_counts)} statuses={len(status_counts)} total=${total:,.2f}"
    )
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", nargs="?", default="bom/bom_estimated_items.csv")
    args = parser.parse_args()
    return validate(Path(args.path))


if __name__ == "__main__":
    raise SystemExit(main())
