# Bill of Materials

Centralized BOM summary for AI and human review. Source workbook is `Camper Build.xlsx` (Price Sheet).

## Current BOM snapshot (2026-02-12)
- Estimated total from `bom/bom_estimated_items.csv`: `$47,575.89`
- Workbook formula baseline (`Price Sheet!D108`, range `D2:D103`): `$45,396.64`
- Budget-path total (`Price Sheet!G106`, range `G2:G105`): `$35,636.00`
- Estimated line items exported: `104`
- Budget options exported: `24`
- Misc items exported: `15`

## AI-friendly exports
- `bom/bom_estimated_items.csv`: normalized estimated BOM rows from workbook plus project-maintained extensions (for post-import decisions)
- `bom/bom_budget_options.csv`: normalized budget options from `G2:G105`
- `bom/bom_misc_items.csv`: miscellaneous items from columns `I:J`
- `bom/load_model_wh.csv`: daily energy/load model (BOM-sourced loads + explicit owner-supplied operational loads)
- `bom/bom_summary.json`: formulas, totals, and export counts

## Estimated subtotal by category
- Camper Platform: `$33,488.64`
- Interior: `$4,560.00`
- Power System: `$6,512.25`
- Appliances: `$1,968.00`
- Hardware: `$912.00`
- Tools: `$80.00`
- Misc: `$55.00`

## Notes
- Workbook rows marked "skip for now" are retained in exports if they are in the formula ranges.
- Truck purchase/registration rows below the estimated formula range were excluded from the normalized estimated export.
- Alternator charging BOM is now locked to Sterling `BB1248120` with `BBR` remote control.
- Added purchase-later rows for Mechman 370A alternator and Big 3 wiring upgrade estimate.
- Distribution architecture is locked to `Victron Lynx Distributor M10` (`LYN060102010`).
- Fuse BOM now includes explicit installed + spare inventory for Class T, Lynx branch MEGA, inline Orion/Sterling protection, and PV string fusing.
- Workbook-derived WH chart is retired; maintain electrical load assumptions in `bom/load_model_wh.csv` using BOM rows plus clearly marked owner-supplied loads when they affect operations.
- Keep future pricing updates in CSV first, then sync critical deltas here.
- `bom/bom_estimated_items.csv` includes `price_flag`:
- `user_filled` = existing owner/workbook-entered price
- `ai_set` = AI-added or AI-updated price estimate
- `blank` = no price entered yet

## Procurement notes template
- Item:
- Vendor:
- Qty:
- Lead time:
- Status:
- Notes:
