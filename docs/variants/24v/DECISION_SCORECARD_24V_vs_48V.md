Status: 24V Candidate Variant (non-canonical; canonical remains 48V baseline)

# Decision Scorecard: 24V vs 48V

As-of date: `2026-02-20`

Purpose: quantify the architecture decision using locked project priorities and reproducible calculations.

## Locked Weights
- Cost (`BOM delta + live pricing`): `35%`
- Electrical simplicity/serviceability: `30%`
- Performance margin (current/thermal/headroom): `20%`
- Implementation disruption: `10%`
- Future scaling headroom: `5%`

## Decision Rule
1. Recommend the higher weighted score.
2. If score gap is `<5` points (0-100 scale), select the lower-risk option and document tie-break rationale.

## Required Calculations
Assumptions:
- `P_ac = 2500W`
- `eta_inverter = 0.92`
- `Wh_bank_target = 15360Wh` (`~15.36kWh`)
- `V24 = 25.6V`, `V48 = 51.2V`
- `P_alt = 1500W`
- MPPT output cap formula: `P_mppt_max = I_mppt_max * V_charge`

### 1) Inverter DC Current
`I_dc = P_ac / (V_dc * eta)`

- `I_24 = 2500 / (25.6*0.92) = 106.1A`
- `I_48 = 2500 / (51.2*0.92) = 53.1A`

### 2) Battery Ah Requirement
`Ah_required = Wh_bank_target / V_nominal`

- `Ah_24 = 15360 / 25.6 = 600Ah`
- `Ah_48 = 15360 / 51.2 = 300Ah`

### 3) MPPT Clipping Check (`900W` array with `150/45`)
- 24V charge voltage assumption: `28.8V`
- 48V charge voltage assumption: `57.6V`

`P_mppt_24_max = 45 * 28.8 = 1296W` -> no clipping at `900W`

`P_mppt_48_max = 45 * 57.6 = 2592W` -> no clipping at `900W`

### 4) Alternator House-Side Current at 1.5kW
`I = P/V`

- `I_alt_24 = 1500/25.6 = 58.6A`
- `I_alt_48 = 1500/51.2 = 29.3A`

### 5) Residual 12V Converter Budget (24V candidate)
Candidate assumption: most loads migrate to 24V. Residual 12V-only budget retained for edge loads.

- Continuous budget: `<=120W` (`<=10A @ 12V`)
- Short surge budget: `<=240W` (`<=20A @ 12V`)

Implication: no large battery-backed 12V subsystem required in candidate baseline.

## Live Pricing Snapshot (US, 2026-02-20)

| Class | 24V path | 48V path |
| --- | --- | --- |
| Inverter/charger | MultiPlus-II 24/3000-70-50 `$1,230.00` (MAURIPRO) https://www.mauripro.com/products/vie-pmp242305130 | MultiPlus-II 48/3000-35-50 `$1,270.00` (MAURIPRO) https://www.mauripro.com/products/vie-pmp482305102 |
| Alternator charger | Sterling BB1224120 `$969.00` (Sterling NA) https://sterling-power.us/products/bb1224120 | Sterling BB1248120 `$949.00` (Sterling NA) https://sterling-power.us/products/bb1248120 |
| 24->12 / 48->12 conversion | Orion Smart 24/12-30 `$243.95` (Bend Battery) https://bendbattery.com/products/orion-tr-smart-24-12-30a-360w-isolated-dc-dc-charger | Orion Smart 48/12-30 `$243.95` (MAURIPRO) https://www.mauripro.com/products/vie-ori481238120 |
| ~15.36kWh battery example | EG4 24V 200Ah 5.12kWh x3 = `$3,447.00` (Inverters R Us) https://invertersrus.com/product/eg4-flp-24v/ | EG4 48V 100Ah 5.12kWh x3 = `$3,897.00` (Inverters R Us) https://invertersrus.com/product/eg4-ll-s-48v/ |

## Scoring Matrix (0-100 scale)

| Criterion | Weight | 24V Score | 48V Score | Rationale (condensed) |
| --- | ---: | ---: | ---: | --- |
| Total architecture cost | `35%` | `84` | `68` | Snapshot pricing favors 24V on inverter + battery class totals |
| Simplicity/serviceability | `30%` | `88` | `66` | 24V-native-first can eliminate large 12V buffer subsystem and 48V fuse-voltage burden |
| Performance margin | `20%` | `72` | `90` | 48V halves major currents and keeps strongest thermal/headroom margin |
| Implementation disruption | `10%` | `62` | `86` | 48V remains current canonical path; 24V requires substantial rewiring/doc swaps |
| Future scaling headroom | `5%` | `70` | `90` | 48V is stronger for later high-power AC expansion |

### Weighted Totals
- `24V total = 84*0.35 + 88*0.30 + 72*0.20 + 62*0.10 + 70*0.05 = 79.9`
- `48V total = 68*0.35 + 66*0.30 + 90*0.20 + 86*0.10 + 90*0.05 = 74.7`
- Score gap = `5.2` points -> tie-break rule not required.

## Recommendation
**Recommend promoting the `24V` candidate architecture** for this project context.

Why this decision is coherent with locked inputs:
- You prioritized `simplicity + cost` and accepted high churn now.
- Power level (`~2.5kW`) is within practical 24V current envelopes.
- No near-term major AC growth reduces need for 48V scaling premium.

## Risk Notes
- 24V still requires disciplined cable length and fuse coordination due ~100A-class inverter path current at peak mixed use.
- If future scope changes to sustained high-power AC loads (A/C, electric heat/water), re-run this scorecard; 48V may become preferred.

## Validation Scenarios (This Package)
1. Data integrity: variant CSV headers and column order match canonical schemas.
2. Arithmetic integrity: candidate load totals remain `3,530 / 4,202 / 624 Wh/day`; score math recomputes to `79.9 vs 74.7`.
3. Cross-document consistency: candidate assumptions are aligned across trade study, systems, fuse schedule, and topology docs.
4. Cost reproducibility: each live-price row includes vendor + link + model and snapshot date.
5. Decision reproducibility: weighted score can be recomputed directly from the criteria table and formulas above.
6. Safety sanity: candidate fuse schedule keeps source-near protection and explicitly revalidates final values against selected hardware manuals.
