# Temporary Electrical Red Flags

Purpose: hold unresolved electrical documentation issues so they can be closed one by one.
Status date: 2026-02-12

## RF-001 Non-BOM Work Loads Excluded From Canonical Model
- Severity: High
- Issue: Canonical model previously excluded owner-supplied work electronics even though they are daily operational loads.
- Why this matters: Autonomy and solar sufficiency were materially overstated.
- Current references:
- `bom/load_model_wh.csv` (`Owner-Supplied` rows)
- `docs/SYSTEMS.md`
- `docs/TRACKING.md`
- Clarification captured:
- Keep owner devices out of BOM cost tracking.
- Include owner devices in Wh modeling and all dependent electrical calculations.
- Baseline assumptions now modeled:
- Laptop (mid-high tier, Excel/programming): `70W` for `8h` core, `10h` winter.
- Monitor (27 inch, 1440p, likely AC path): `35W` for matching work hours.
- Tablet + keyboard/mouse charging allowance included.
- Resolution target:
- Add modeled rows in `bom/load_model_wh.csv`.
- Recalculate `docs/SYSTEMS.md`.
- Recalculate tracking baselines in `docs/TRACKING.md`.
- Status: Closed (`2026-02-11`) pending measured load validation

## RF-002 Alternator Charging Path Not Locked
- Severity: Medium
- Issue: Resolved. Alternator charging architecture is now frozen to Sterling `BB1248120` + `BBR`.
- Why this matters: Charge recovery math and procurement are now tied to one concrete hardware path.
- Current references:
- `bom/bom_estimated_items.csv` (rows `18` and `26`)
- `docs/SYSTEMS.md`
- `docs/TRACKING.md` (`D-008`)
- Resolution completed:
- Component choice frozen in BOM.
- Charge-rate assumptions and recovery-time math updated in `docs/SYSTEMS.md`.
- Status: Closed (`2026-02-11`)

## RF-003 Power Distribution Topology Ambiguity (Lynx vs Discrete)
- Severity: Medium
- Issue: Previously unresolved.
- Resolution completed (`2026-02-12`):
- Topology locked to `Lynx one-module` (`Victron Lynx Distributor M10`, `LYN060102010`) for Phase 1.
- SYSTEMS documentation converted to Lynx-only implementation baseline and DIY comparison content removed.
- Next workstream explicitly defined: full start-to-finish fuse schedule for this locked topology.
- Current references:
- `bom/bom_estimated_items.csv:6`
- `docs/SYSTEMS.md` (`RF-003 Distribution Topology Decision (Lynx Locked)`)
- `docs/ELECTRICAL_overview_diagram.md`
- Status: Closed (`2026-02-12`)

## RF-004 Battery Energy Convention Not Finalized (48V vs 51.2V)
- Severity: Medium
- Issue: Resolved.
- Why this matters: Capacity/autonomy/charge-time outputs shift when nominal voltage basis changes.
- Current references:
- `docs/SYSTEMS.md`
- `docs/TRACKING.md`
- Resolution completed (`2026-02-12`):
- Keep `48V` as architecture/system label.
- Use `51.2V` nominal for battery Wh accounting in model tables.
- Recalculate dependent capacity/autonomy values in `docs/SYSTEMS.md`.
- Status: Closed (`2026-02-12`)

## RF-005 Fridge Row Semantics Could Be Misread
- Severity: Low-Medium
- Issue: `power_w` for fridge rows is modeled average power while notes reference compressor duty-cycle math.
- Why this matters: Easy for future edits to double-apply duty or misread assumptions.
- Current references:
- `bom/load_model_wh.csv:5`
- `bom/load_model_wh.csv:18`
- `bom/load_model_wh.csv:31`
- Clarification needed:
- Preferred modeling convention: average-power inputs or nameplate-power + explicit duty columns.
- Resolution target:
- Standardize column usage and notes across all rows.
- Status: Open

## RF-006 Historical Decision Log Wording Is Potentially Confusing
- Severity: Low
- Issue: Historical entry still states baseline `3,790 Wh/day` was documented in SYSTEMS (even though superseded).
- Why this matters: Quick readers may anchor on retired values.
- Current references:
- `docs/TRACKING.md:18`
- `docs/TRACKING.md:19`
- Clarification needed:
- Whether to keep historical text verbatim or append an explicit superseded-value note format.
- Resolution target:
- Apply consistent "superseded" annotation style to historical decisions.
- Status: Open

## RF-007 Purchase-Later Alternator Upgrade Integration Not Fully Locked
- Severity: Medium
- Issue: Mechman 370A alternator and Big 3 are now tracked as purchase-later, but fitment, belt spec, and final Big 3 fuse/routing details are not yet locked.
- Why this matters: Wrong fitment or incomplete vehicle-side wiring prep can create installation delays or charging/grounding faults.
- Current references:
- `bom/bom_estimated_items.csv` (rows `103` and `104`)
- `docs/SYSTEMS.md` (alternator charging and safety baseline sections)
- `docs/TRACKING.md` (`D-009`, `R-006`)
- Clarification needed:
- Truck-specific alternator fitment confirmation and shorter-belt part number.
- Final Big 3 cable/fuse package and RVC-loop routing requirement for the truck.
- Resolution target:
- Lock alternator SKU + belt + Big 3 spec in BOM notes before purchase.
- Status: Open

## RF-008 Sterling BB1248120 Output Rating Assumption Was Incorrect In Planning Math
- Severity: High
- Issue: A prior planning revision treated `BB1248120` as `120A` on the `48V` output path.
- Why this matters: Charge-recovery timelines and alternator strategy decisions were materially overstated.
- Current references:
- `bom/bom_estimated_items.csv` row `18`
- `docs/SYSTEMS.md` (Alternator charging section)
- `docs/TRACKING.md` (`D-012`)
- Resolution completed (`2026-02-12`):
- Corrected charger basis to `~1500W` max output (`~26A` at `57.6V` nominal output setting).
- Recalculated alternator-recovery time assumptions in `docs/SYSTEMS.md`.
- Updated electrical topology and fuse docs to implementation-level detail with holder and conductor mapping.
- Status: Closed (`2026-02-12`)

## Suggested Resolution Order
1. RF-007 Purchase-later alternator integration
2. RF-005 Load model column semantics
3. RF-006 Historical wording cleanup
