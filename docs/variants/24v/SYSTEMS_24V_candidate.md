Status: 24V Candidate Variant (non-canonical; canonical remains 48V baseline)

# Systems Design (24V Candidate)

As-of date: `2026-02-20`

Purpose: provide a complete candidate systems baseline for a potential `24V` architecture promotion while canonical docs remain `48V`.

## Candidate Snapshot
- House core: `24V`.
- Target bank class: `~15kWh`.
- Inverter class: `~2.5kW` mixed-use requirement (3kVA class hardware acceptable).
- AC scope: AC kitchen retained.
- Distribution strategy: `24V-native first`; residual `12V` only where unavoidable.
- 12V strategy: no large dedicated 12V buffer battery in candidate baseline.

## Candidate Electrical Links
- Trade study and recommendation: `docs/variants/24v/ELECTRICAL_24V_vs_48V_trade_study.md`
- Candidate topology: `docs/variants/24v/ELECTRICAL_overview_diagram_24V_candidate.md`
- Candidate fuse schedule: `docs/variants/24v/ELECTRICAL_fuse_schedule_24V_candidate.md`
- Decision scorecard: `docs/variants/24v/DECISION_SCORECARD_24V_vs_48V.md`
- Candidate BOM: `bom/variants/24v/bom_estimated_items_24V_candidate.csv`
- Candidate load model: `bom/variants/24v/load_model_wh_24V_candidate.csv`

## Load Model Policy (Candidate)
- Baseline daily Wh remains unchanged from canonical model v3 for decision comparability.
- Any future duty-cycle or device-power changes must be made in the candidate CSV and recomputed in the scorecard.
- Converter-loss line remains conservative; it can be reduced only after actual appliance migration is locked.

## Candidate Capacity/Current Summary
Nominal basis: `24V = 25.6V`, `48V = 51.2V`.

| Metric | 24V candidate | 48V baseline reference |
| --- | ---: | ---: |
| Ah for 15.36kWh | `600Ah` | `300Ah` |
| 2.5kW inverter DC input current (`eta=0.92`) | `106.1A` | `53.1A` |
| 1.5kW alternator charge current (house side) | `58.6A` | `29.3A` |

## Candidate Operational Intent
1. Keep high-current 24V paths short and physically grouped.
2. Move practical loads to 24V-native appliance/device paths where possible.
3. Keep residual 12V limited to low-power legacy/safety loads.
4. Size residual 24->12 conversion for measured need, not for a full secondary subsystem.

## Promotion Gate
This candidate can be promoted to canonical only after:
1. Final scorecard sign-off in `docs/variants/24v/DECISION_SCORECARD_24V_vs_48V.md`.
2. Final 24V appliance compatibility review complete.
3. Fuse and wire schedule validation pass complete.
4. Cabinet fit/layout recheck against selected 24V hardware dimensions.
