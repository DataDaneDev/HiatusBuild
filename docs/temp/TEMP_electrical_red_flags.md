# Temporary Electrical Red Flags

Purpose: hold unresolved electrical documentation issues so they can be closed one by one.
Status date: 2026-03-20

## RF-001 Non-BOM Work Loads Excluded From Canonical Model
- Severity: High
- Issue: Canonical model previously excluded owner-supplied work electronics even though they are daily operational loads.
- Why this matters: Autonomy and solar sufficiency were materially overstated.
- Current references:
- `bom/load_model_wh.csv` (`Owner-Supplied` rows)
- `docs/core/SYSTEMS.md`
- `docs/core/TRACKING.md`
- Clarification captured:
- Keep owner devices out of BOM cost tracking.
- Include owner devices in Wh modeling and all dependent electrical calculations.
- Baseline assumptions now modeled:
- Laptop (mid-high tier, Excel/programming): `70W` for `8h` core, `10h` winter.
- Monitor (27 inch, 1440p, likely AC path): `35W` for matching work hours.
- Tablet + keyboard/mouse charging allowance included.
- Resolution target:
- Add modeled rows in `bom/load_model_wh.csv`.
- Recalculate `docs/core/SYSTEMS.md`.
- Recalculate tracking baselines in `docs/core/TRACKING.md`.
- Status: Closed (`2026-02-11`) pending measured load validation

## RF-002 Alternator Charging Path Not Locked
- Severity: Medium
- Issue: Resolved. Alternator charging architecture is now frozen to the dedicated `48V` secondary alternator path (`Mechman + WS500 + APM-48`) with Ford `Upfitter #3` as the manual WS500 enable/disable control.
- Why this matters: Charge recovery math, shutdown order, wiring, and procurement are now tied to one concrete hardware path.
- Current references:
- `docs/core/ELECTRICAL_48V_ARCHITECTURE.md`
- `bom/bom_estimated_items.csv` (rows `168-171`, `176`)
- `docs/core/SYSTEMS.md`
- `docs/core/TRACKING.md` (`D-028`, `D-029`, `D-030`, `D-031`)
- Resolution completed:
- Component choice frozen in BOM.
- Manual control path frozen to `Upfitter #3 -> F-15 -> WS500 brown ignition`.
- Canonical `48V` design file added and linked from core docs.
- Status: Closed (`2026-03-20`)

## RF-003 Power Distribution Topology Ambiguity (Lynx vs Discrete)
- Severity: Medium
- Issue: Previously unresolved.
- Resolution completed (`2026-02-12`):
- Topology locked to `Lynx one-module` (`Victron Lynx Distributor M10`, `LYN060102010`) for Phase 1.
- SYSTEMS documentation converted to Lynx-only implementation baseline and DIY comparison content removed.
- Next workstream explicitly defined: full start-to-finish fuse schedule for this locked topology.
- Current references:
- `bom/bom_estimated_items.csv:6`
- `docs/core/SYSTEMS.md` (`RF-003 Distribution Topology Decision (Lynx Locked)`)
- `docs/implementation/ELECTRICAL_overview_diagram.md`
- Status: Closed (`2026-02-12`)

## RF-004 Battery Energy Convention Not Finalized (48V vs 51.2V)
- Severity: Medium
- Issue: Resolved.
- Why this matters: Capacity/autonomy/charge-time outputs shift when nominal voltage basis changes.
- Current references:
- `docs/core/SYSTEMS.md`
- `docs/core/TRACKING.md`
- Resolution completed (`2026-02-12`):
- Keep `48V` as architecture/system label.
- Use `51.2V` nominal for battery Wh accounting in model tables.
- Recalculate dependent capacity/autonomy values in `docs/core/SYSTEMS.md`.
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
- `docs/core/TRACKING.md:18`
- `docs/core/TRACKING.md:19`
- Clarification needed:
- Whether to keep historical text verbatim or append an explicit superseded-value note format.
- Resolution target:
- Apply consistent "superseded" annotation style to historical decisions.
- Status: Open

## RF-007 Dedicated `48V` Secondary Alternator Integration Still Needs Vendor Closure
- Severity: Medium
- Issue: The project has moved off the old single-12V upgrade path, but the dedicated `48V` secondary alternator still has vendor-confirmation gates open.
- Why this matters: Wrong kit content, incorrect harness polarity, or unsupported battery/BMS behavior can create commissioning risk and possible charging faults.
- Current references:
- `docs/core/ELECTRICAL_48V_ARCHITECTURE.md`
- `bom/bom_estimated_items.csv` (rows `168-171`, `176`)
- `docs/core/SYSTEMS.md`
- `docs/core/TRACKING.md` (`R-006`)
- Clarification needed:
- Truck-specific Mechman fitment/content confirmation and harness polarity (`PH`/`NH`).
- Official Wakespeed support status for the documented Dumfume battery/BMS behavior.
- Confirmed alternator negative/case isolation behavior and any mandatory extra mitigation.
- Resolution target:
- Close the remaining Mechman/Wakespeed vendor gates before commissioning.
- Status: Open

## RF-008 Sterling BB1248120 Output Rating Assumption Was Incorrect In Planning Math
- Severity: High
- Issue: A prior planning revision treated `BB1248120` as `120A` on the `48V` output path.
- Why this matters: Charge-recovery timelines and alternator strategy decisions were materially overstated.
- Current references:
- `bom/bom_estimated_items.csv` row `18`
- `docs/core/SYSTEMS.md` (Alternator charging section)
- `docs/core/TRACKING.md` (`D-012`)
- Resolution completed (`2026-02-12`):
- Corrected charger basis to `~1500W` max output (`~26A` at `57.6V` nominal output setting).
- Recalculated alternator-recovery time assumptions in `docs/core/SYSTEMS.md`.
- Updated electrical topology and fuse docs to implementation-level detail with holder and conductor mapping.
- Status: Closed (`2026-02-12`)

## RF-009 Run-Length Governance Shift (CAD Gate Retired) Needs Canonical Capture
- Severity: Medium
- Issue: Run-length validation method changed from CAD-gated assumptions to bench-layout-first measured lengths, but implementation docs still need one explicit canonical location for measured values.
- Why this matters: Without one measured-length source of truth, cable/fuse closeout can drift across docs and cut lists.
- Current references:
- `docs/core/TRACKING.md` (`D-024`)
- `docs/implementation/ELECTRICAL_fuse_schedule.md`
- `docs/implementation/ELECTRICAL_overview_diagram.md`
- Clarification needed:
- Where measured one-way run lengths will be maintained as the canonical dataset during build.
- Resolution target:
- Define canonical measured-length location and keep it in sync before final cable closeout procurement.
- Status: Open

## Suggested Resolution Order
1. RF-009 Run-length governance capture
2. RF-007 Purchase-later alternator integration
3. RF-005 Load model column semantics
4. RF-006 Historical wording cleanup
