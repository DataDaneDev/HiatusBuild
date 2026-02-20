Status: 24V Candidate Variant (non-canonical; canonical remains 48V baseline)

# Electrical Fuse Schedule (24V Candidate)

As-of date: `2026-02-20`

Purpose: candidate fuse/protection baseline for a `24V` core architecture. This is a decision package artifact and is not yet canonical.

Related candidate docs:
- `docs/variants/24v/ELECTRICAL_24V_vs_48V_trade_study.md`
- `docs/variants/24v/ELECTRICAL_overview_diagram_24V_candidate.md`
- `bom/variants/24v/bom_estimated_items_24V_candidate.csv`

## Candidate Fuse Matrix
| Fuse ID | Protected path | Candidate class | Initial candidate value | Notes |
| --- | --- | --- | --- | --- |
| `F-01A/B/C` | Battery positive branch per battery | Class T | `175A-200A` (final by battery datasheet) | One per battery branch near source |
| `F-02` | Inverter feed (24V MultiPlus class) | MEGA/Class T upstream branch | `150A` candidate start | Final value by selected inverter manual/cable sizing |
| `F-03` | MPPT to 24V bus | MEGA | `60A` candidate | `150/45` class branch |
| `F-04` | Sterling BB1224120 output branch | MEGA | `70A` candidate | Final by charger output spec and cable limits |
| `F-05` | Residual 24->12 converter feed | MEGA/MIDI | `20A-40A` candidate | Depends on final converter size |
| `F-08` | Vehicle-side Sterling input | ANL/MEGA | `150A` candidate | 12V-side input protection near source |
| `F-10` | Residual 12V branch panel circuits | ATO/ATC | per branch | Safety/legacy loads only in candidate baseline |

## Voltage-Class Guidance (Candidate)
- 24V house paths: generally compatible with `32V` fuse ecosystem when branch voltage remains below rating.
- 12V vehicle/starter-battery paths: `32V` class remains normal.
- If any path exceeds `32V` fuse rating envelope by hardware selection, up-rate fuse voltage class accordingly.

## Candidate Protection Philosophy
1. Protect conductor first, then equipment.
2. Keep source protection physically close to source terminals.
3. Keep high-current 24V trunk lengths short.
4. Re-validate every final fuse value against actual selected hardware manuals before promotion.

## Validation Required Before Promotion
1. Battery datasheet verification for branch fuse upper limits.
2. Final inverter model confirmation and branch current envelope check.
3. Final Sterling charger model current envelope check for 24V output branch.
4. Residual 12V converter sizing lock and corresponding `F-05`/`F-10` updates.
