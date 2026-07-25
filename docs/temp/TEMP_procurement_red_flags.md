---
aliases:
  - Procurement red flags
tags:
  - hiatus/temp
  - hiatus/procurement
status: archived-reference
related:
  - "[[TRACKING]]"
---

# Temporary Procurement Red Flags

Purpose: archived procurement issue sweep. Do not use this file as the live buy list; current procurement action belongs in `docs/plans/PROCUREMENT_purchase_list_2026-05-26.md`, `bom/bom_estimated_items.csv`, and `docs/core/TRACKING.md`. Remaining open PRF items below are retained as watchlist/provenance only.
Status date: 2026-05-27

## PRF-001 BOM Source Of Truth Is Split Across Multiple Files
- Severity: High
- Issue: `bom/BOM.md` and `bom/bom_summary.json` can drift from `bom/bom_estimated_items.csv`.
- Why this matters: procurement decisions can drift from current line-item data if multiple files are treated as authoritative.
- Current references:
- `bom/BOM.md`
- `bom/bom_summary.json`
- `bom/bom_estimated_items.csv`
- Resolution:
- Confirmed CSV-only BOM workflow.
- Kept `bom/bom_estimated_items.csv` as line-item level only (no in-file total row).
- Retired redundant rollup artifacts (`bom/BOM.md`, `bom/bom_summary.json`).
- Kept `bom/bom_misc_items.csv` as a separate non-build misc/lifestyle list.
- Status: Closed (2026-02-13)

## PRF-003 Electrical Cabinet BOM Has Unlocked Core Line Items
- Severity: Medium
- Issue: Historical/superseded. D-044 closed the AC purchase lock to one `6-way` enclosure, two active `20A` GFCI branches, and AC-in-first validation.
- Why this matters: unresolved SKU-level lock can still delay procurement, even after architecture-level decisions are complete.
- Current references:
- `bom/bom_estimated_items.csv` row `13` (`AC input breaker/disconnect`)
- `bom/bom_estimated_items.csv` row `14` (`DEPRECATED (AC): DIN rail mount`)
- `bom/bom_estimated_items.csv` row `17` (`DEPRECATED (12V): separate negative busbar`)
- `bom/bom_estimated_items.csv` row `19` (`Pre-charge Resistor`)
- Clarification needed:
- Final SKU choices for active AC/DC rows (breaker enclosure family, branch breaker models, receptacle family, USB-C PD module family).
- Final receptacle-count closure (`3` vs `4` locations) on the retained two-branch AC baseline.
- Final pre-charge resistor strategy/SKU for row `19`.
- Confirmed AC load list for Phase 1:
- `Appliances`: induction cooktop (`bom` row `67`), Ninja SP151 air fryer/toaster oven (`bom` row `68`)
- `Office`: monitor/charger branch via inverter (`bom/load_model_wh.csv` owner-supplied rows)
- `Infrastructure`: shore AC charger path via MultiPlus (`bom` row `12`)
- Modeled AC-related daily energy (planning):
- `core_workday`: `986 Wh/day` (~`27.9%` of `3,530 Wh/day`)
- `winter_workday`: `1,290 Wh/day` (~`30.7%` of `4,202 Wh/day`)
- Largest AC contributors are induction + Ninja SP151 + monitor path, with inverter-idle overhead when AC path is active.
- Research notes (2026-02-13):
- Victron MultiPlus-II installation guidance still requires AC overcurrent/disconnect on AC input and UL943-class residual-current protection plus overcurrent protection on AC output branches.
- Input breaker can be downsized to shore service rating; a `20A` shore input does not require a large panel.
- DIN rail is a mounting method, not a requirement in the referenced inverter guidance.
- External references used:
- `https://www.victronenergy.com/media/pg/MultiPlus-II_120V/en/installation.html` (`4.4` AC cabling section)
- `https://www.victronenergy.com/upload/documents/Datasheet-MultiPlus-II-inverter-charger-EN.pdf` (model ratings for `48/3000/35-50`)
- Resolution progress:
- Locked Phase 1 to two AC-out-1 branches (`20A` galley + `15A` office) and `4` total `120V` receptacle locations (`2` galley, `2` office).
- Locked USB charging baseline to DC-fed USB-C PD modules on `12V` branch circuits (`2` office + `2` galley points).
- Populated related BOM rows for shore interface, AC enclosure/protection, receptacle hardware, AC cable, USB-C PD branch hardware, and optional converter-expansion path (`rows 107-118`).
- Resolution target:
- Historical reference only; current AC work is owned by `docs/implementation/ELECTRICAL_AC_BOM.md`, `docs/core/TRACKING.md` D-044, and the bench validation checklist.
- Status: Closed / superseded by D-044 (`2026-05-17` owner-confirmed cleanup)

## PRF-004 Fuse And Holder SKU Lock Is Incomplete For Active Architecture
- Severity: High
- Issue: fuse families and ratings are documented, but holder SKU standard is not fully frozen.
- Why this matters: voltage-class or fitment mismatch at the holder level can create safety and rework risk.
- Current references:
- `docs/implementation/ELECTRICAL_fuse_schedule.md` (assumptions/open items)
- `docs/core/TRACKING.md` (open question on final fuse-holder SKU standard)
- `bom/bom_estimated_items.csv` rows `11`, `105`, `106`
- Clarification needed:
- Final SKUs for inline holders covering `F-11`, plus the external Victron MEGA holder for `F-07` and PV combiner hardware standard. Orion input no longer requires standalone `F-06`: use one `40A` MEGA body-marked at least `58VDC` in Lynx Slot 4 feeding the existing `6 AWG` pair directly; Victron `CIP138040020 40A/80V` is replacement fallback only.
- Resolution target:
- Freeze remaining holder SKU ecosystem and update BOM notes to reflect exact installed hardware.
- Status: Partially open (`F-06` closed; remaining holder standards still pending)

## PRF-005 Shore AC Feed Path Is Under-Specified In Procurement Data
- Severity: Medium
- Issue: Historical/superseded. Shore/AC SKU lock is complete for Phase 1; remaining box/clamp/grommet details are hands-on install fitment, not procurement blockers.
- Why this matters: wrong enclosure/inlet/interface choices can still create rework risk at install time.
- Current references:
- `docs/implementation/ELECTRICAL_overview_diagram.md` (full AC hierarchy, AC segment table `C-28` through `C-34`)
- `bom/bom_estimated_items.csv` rows `13`, `14`, `15`, `107-114`
- Clarification needed:
- Exact SKU/model lock for:
- Shore inlet and adapter ecosystem (`30A` inlet baseline with `15A/20A` adapters).
- AC enclosure and breaker family compatibility.
- GFCI + downstream receptacle family and box style.
- AC cable type and final cut lengths after layout confirmation.
- Resolution target:
- Historical reference only; do not use this temp note to reopen AC procurement/receptacle-count churn.
- Status: Closed / superseded by D-044 (`2026-05-17` owner-confirmed cleanup)

## PRF-006 CAD-Dependent Electrical Assumptions Are Not Yet Validated
- Severity: Medium
- Issue: original CAD-gated run-length workflow is no longer the active method; measured bench-layout lengths now need to be captured cleanly as the source of truth.
- Why this matters: final wire gauge, fuse choice margin, and cut-length ordering can be wrong if route lengths shift.
- Current references:
- `docs/implementation/ELECTRICAL_fuse_schedule.md` (run-length assumptions and Orion branch note)
- `docs/implementation/ELECTRICAL_overview_diagram.md` (conductor schedule assumptions)
- `docs/core/TRACKING.md` (`D-024`)
- Clarification needed:
- Measured one-way run lengths for major cabinet circuits from physical board layout.
- Canonical storage location for measured run-length records.
- Resolution target:
- Validate major run lengths from bench layout before freezing cable/fuse purchases and cut-to-length material orders.
- Status: Open

## PRF-007 Project Next-Steps Section Is Stale Relative To Completed Electrical Work
- Severity: Low
- Issue: `docs/core/PROJECT.md` still lists fuse-schedule creation as an immediate next decision despite completion.
- Why this matters: planning doc drift can waste review cycles and hide true remaining blockers.
- Current references:
- `docs/core/PROJECT.md` (`Immediate next decisions`)
- `docs/implementation/ELECTRICAL_fuse_schedule.md`
- Clarification needed:
- Preferred cadence for updating high-level “next decisions” after major subsystem closure.
- Resolution target:
- Replace completed items with current procurement blockers and validation tasks.
- Status: Closed (`2026-03-18`) after project-doc maintenance pass

## Suggested Resolution Order
1. PRF-004 fuse-holder SKU lock
2. PRF-006 measured run-length record lock
3. Keep PRF-003 and PRF-005 as historical/superseded AC procurement notes only
