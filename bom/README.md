# BOM data contract

The component-level BOM is split into two directly usable CSVs:

- `bom_estimated_items.csv` — active build scope: acquired items plus unresolved `Selected`, `Planned`, and `Deferred` lines.
- `bom_inactive_items.csv` — stable-ID archive for `Returned` and `Retired` lines that must not affect the active build total or buy-list review.

The two files share one schema and one global row-ID namespace. Moving a line between them never changes its `row` identifier. Their union is the complete historical row registry.

Only `bom_estimated_items.csv` is summed as the current build total. Costs in `bom_inactive_items.csv` are retained as historical estimate, purchase, sunk-stock, or return evidence; they are excluded from the active total rather than erased or silently zeroed.

## Columns

| Column | Rule |
|---|---|
| `row` | Stable numeric BOM identifier across both CSVs. Do not renumber or reuse existing IDs; append new IDs. Gaps are allowed. |
| `category` | One canonical category from the list below. |
| `component` | One component, SKU class, true retail kit, or explicit planning allowance. Use sentence case except for proper names and acronyms. |
| `cost` | Numeric line cost with two decimal places. Blank means unknown; `0.00` means intentionally no separately counted cost. Do not include `$` or thousands separators. |
| `cost_basis` | Describes what the cost represents; see the controlled vocabulary below. |
| `purchase_date` | Actual purchase/source date in `YYYY-MM-DD`. Leave blank for unpurchased `Selected`, `Planned`, or `Deferred` lines and for retired lines that were never acquired. Retired stock may retain its actual acquisition date. Target dates belong in planning docs, not this field. |
| `purchase_status` | Procurement/scope state from the controlled vocabulary below. Installation and commissioning gates belong in `notes` or the owning implementation document. |
| `notes` | Concise source, quantity, role, and remaining-gate context. Keep implementation procedures in the owning docs. Maximum 500 characters. |

## Controlled vocabularies

### Categories

- `Camper`
- `Electrical`
- `Hardware`
- `Tools`
- `Appliances`
- `Plumbing`
- `Interior`
- `Consumables`
- `Vehicle`
- `Vehicle Electronics`
- `Services`

### Purchase status

- `Purchased` — acquired or committed cost is part of the build record
- `Partially Purchased` — one component line still has acquired and unacquired quantity
- `Included` — supplied with another item or existing stock; no separate procurement action
- `Selected` — exact direction/item is locked but not acquired
- `Planned` — requirement exists but selection or purchase remains open
- `Deferred` — deliberately outside the current build phase
- `Returned` — purchased and then returned/refunded; store in `bom_inactive_items.csv`
- `Retired` — superseded, removed, reconciled, or no longer required; store in `bom_inactive_items.csv`

### Cost basis

- `item_subtotal` — receipt/order line subtotal excluding order-level tax/shipping
- `purchase_record` — acquired cost is supported, but finer item-vs-delivered allocation is unavailable or unnecessary
- `delivered_total` — shipping/tax-inclusive delivered amount
- `order_remainder` — separately stated shipping, packaging, tax, or other order-level remainder
- `residual_allocation` — arithmetic remainder after evidence-backed children are split from a mixed historical row; not a receipt-level child price
- `owner_estimate` — owner-provided allowance for an unpurchased line
- `planning_estimate` — planning estimate, not a purchase record
- `included` — zero separately counted cost because another line supplies the item
- `not_applicable` — zero cost on a retired/non-procurement line
- `unknown` — cost not established

## Granularity rules

1. Use one row per independently sourceable component or SKU class.
2. Keep identical quantities, packs, assortments, and true manufacturer kits together when they share one lifecycle and cost basis.
3. Split mixed categories, mixed purchase states, or independently replaceable items.
4. Split shipping/packaging into `Services` when the order evidence provides a separate amount.
5. Exclude order-level tax rather than allocating it arbitrarily when the rest of the BOM uses pre-tax item subtotals.
6. If directly evidenced child costs do not fully allocate a mixed legacy total, use `residual_allocation` for the remaining parent cost and explain the arithmetic in `notes`.
7. A broad planning allowance may stay grouped only while component-level selection and cost allocation are genuinely unknown; name it explicitly as an `allowance` or `package`.
8. Lifecycle words such as `DEPRECATED`, `OPTIONAL`, `RESOLVED`, and `NOT REQUIRED` do not belong in `component`; use `purchase_status` and `notes`.

## Style

- Use `12V`, `48V`, `DC-DC`, `AWG`, `PEX-B`, and `heat-shrink` consistently.
- Use dimensions such as `3/8 in`, not mixed quote marks or improvised abbreviations.
- Start notes with the evidence or decision, then give the item role and only the unresolved gate.
- Store only sanitized product facts and public product URLs. Raw order IDs, account-scoped links, addresses, payment data, and invoice exports stay out of the public repository.

Run `python3 scripts/validate-bom.py` after editing either CSV. The default validation checks both files together for schema compliance, lifecycle placement, globally unique IDs/components/ASINs, and separate active/inactive totals.
