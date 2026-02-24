# 48V Battery Fuse + Wire Recalculation (Battery and 48V Trunks)

As-of date: `2026-02-18`

Purpose: document the decision-complete recalculation used to re-baseline battery branch fusing and major 48V trunk conductor sizing for the current `3x 48V 100Ah` architecture.

Related docs:
- `docs/ELECTRICAL_fuse_schedule.md`
- `docs/ELECTRICAL_overview_diagram.md`
- `bom/bom_estimated_items.csv`

## Scope
- In scope: battery-side and major `48V` trunk circuits (`C-01` through `C-15`).
- Out of scope in this pass: detailed `12V` branch resizing, AC branch recalculation, and CAD-final cut lengths.

## Inputs (Locked For This Pass)
| Input | Value | Basis |
| --- | --- | --- |
| Battery count `N` | `3` | Current architecture |
| Battery nominal voltage | `51.2V` | Current BOM convention |
| Battery current limit | `<=200A` per battery (provisional) | Product listing text provided by owner |
| Battery-side conductors | `2/0 AWG` copper | Current build baseline |
| Lynx discharge-active branch limits | `F-02=125A`, `F-05=40A` | Current branch architecture |
| MPPT/charger branch limits | `F-03=60A`, `F-04=40A` | Current branch architecture |
| Sharing factor `K_share` | `1.5` | Conservative parallel-imbalance factor |
| Continuous margin `K_cont` | `1.25` | Conservative continuous-load margin |
| Voltage-drop target (48V trunks) | `<=2%` | Existing electrical design target |

## Governing Equations
```text
I_total_discharge = F-02 + F-05
I_batt_design = (I_total_discharge / N) * K_share
I_fuse_min = I_batt_design * K_cont
I_fuse_max = min(I_battery_limit, I_cable_limit_after_derating, I_terminal_limit)
Select Class T fuse within [I_fuse_min, I_fuse_max]
```

## Battery Branch Fuse Envelope Calculation
1. Discharge envelope:
- `I_total_discharge = 125A + 40A = 165A`

2. Per-battery design current with conservative sharing:
- `I_batt_design = (165A / 3) * 1.5 = 82.5A`

3. Continuous-adjusted minimum:
- `I_fuse_min = 82.5A * 1.25 = 103.1A`

4. Maximum allowed:
- `I_fuse_max = min(200A provisional battery limit, conductor limit, terminal/busbar limits)`
- For this pass, battery listing limit `200A` is the active cap.

5. Selection:
- Provisional installed selection: `200A Class T` per battery (`F-01A/B/C`).
- Alternate value to stage as contingency: `175A Class T` spare set.

## Why 200A Provisional (Current Baseline)
- It stays inside the current provisional `<=200A` battery limit.
- It materially improves coordination vs the prior `225A` value.
- It preserves availability of a lower step (`175A`) if final validated battery data requires down-selection.

## Final Lock Gate (Mandatory)
Do not treat `200A` as permanently locked until both items are captured from a true `51.2V` battery datasheet/manual:
1. Continuous and peak discharge-current limits.
2. Terminal/stud and manufacturer fuse guidance limits.

If either validated limit is below current assumptions, lock `F-01A/B/C` to `175A` and update docs/BOM together.

## Class T Holder Family Constraint
- `<225A` fuse targets require `110A-200A` Class T holder family compatibility.
- Do not buy `225A-400A` holder-only hardware if targeting `200A` or `175A` battery branch fuses.

## 48V Conductor Check (Scenario-Band, No CAD Lock)
Assumptions for quick voltage-drop screen:
- Copper resistance at 20C (approx):
1. `2/0 AWG`: `0.0000779 ohm/ft`
2. `6 AWG`: `0.0003951 ohm/ft`
- Two-conductor DC loop method:
`V_drop = I * (2 * L_one_way * R_per_ft)`

### A) `2/0 AWG` main trunk screen (`I=165A`)
| One-way length `L` | Loop resistance | Vdrop | % of `51.2V` |
| --- | --- | --- | --- |
| `3 ft` | `0.000467 ohm` | `0.077V` | `0.15%` |
| `6 ft` | `0.000935 ohm` | `0.154V` | `0.30%` |
| `10 ft` | `0.001558 ohm` | `0.257V` | `0.50%` |

Result: passes `<=2%` target with substantial margin.

### B) `6 AWG` branch screen (worst branch `I=60A`)
| One-way length `L` | Loop resistance | Vdrop | % of `51.2V` |
| --- | --- | --- | --- |
| `3 ft` | `0.002371 ohm` | `0.142V` | `0.28%` |
| `6 ft` | `0.004741 ohm` | `0.284V` | `0.55%` |
| `10 ft` | `0.007902 ohm` | `0.474V` | `0.93%` |

Result: passes `<=2%` target in short/medium/long scenario bands.

## Procurement Defaults From This Recalc
1. Battery branch fuses (`F-01A/B/C`):
- Buy now: `200A Class T x3` installed + `200A x3` spares.
- Optional hedge: `175A Class T x3` alternate spare set.

2. Class T holders:
- Buy `110A-200A` compatible family for the battery branch path.

3. `2/0` cable quantity:
- Procurement baseline changed from `30 ft` to `50 ft total` for scenario-band routing, service loops, and termination waste.

## Validation and Test Scenarios
1. Documentation validation:
- Confirm all battery branch Class T holder SKUs are compatible with the selected fuse range (`110A-200A` family).
- Confirm all `48V` fuse families remain voltage-appropriate for system voltage class.

2. Bench electrical validation:
- Steady discharge test: apply representative inverter-backed load and verify no abnormal cable/fuse heating.
- Charge-path test: verify battery-branch current sharing while charging sources are active.
- Parallel-sharing check: clamp each battery positive branch under representative load and verify no persistent branch overload.
- Post-thermal-cycle torque check: re-torque and witness-mark high-current terminations after thermal cycling.

## Acceptance Criteria
- Selected battery fuse value satisfies: `I_fuse_min <= selected_fuse <= I_fuse_max`.
- `C-01` through `C-15` satisfy voltage-drop target under chosen scenario band.
- `docs/ELECTRICAL_fuse_schedule.md`, `docs/ELECTRICAL_overview_diagram.md`, and `bom/bom_estimated_items.csv` all show the same battery-fuse baseline and holder-family assumptions.

## Key Assumptions / Limits
1. Battery current-limit input is provisional pending validated `51.2V` datasheet/manual.
2. The provided `14.6V/14.2V` screenshot is treated as non-authoritative for this `51.2V` pack.
3. No branch expansion beyond current architecture is assumed in this pass.
4. Final route-length lock still requires CAD/physical layout validation before cut-to-length harnesses are finalized.
