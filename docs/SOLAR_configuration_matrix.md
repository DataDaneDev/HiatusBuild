# Solar Configuration Matrix (48V House Baseline)

As-of date: `2026-02-24`

Purpose: quick-screen roof-fit panel sets against the current electrical baseline:
- House bank: `48V` nominal (`51.2V` LiFePO4 class)
- Controller baseline: `Victron SmartSolar MPPT 150/45`
- Panel construction scope in this table: `rigid panels` only.

Flag meaning:
- `GREEN`: viable candidate on current baseline (still verify final datasheet temp coefficients and local coldest design temp).
- `YELLOW`: borderline/conditional on current baseline (can work, but margin is tight in hot or cold extremes).
- `RED`: not recommended/incompatible on current baseline.

## Candidate Configurations
| Option | Wiring | String Voc (STC) | Total wattage | Total weight (lbs) | Flag (`150/45` baseline) | Notes |
| --- | --- | ---: | ---: | ---: | --- | --- |
| `2x 400W` (`Voc 37.10V`) | `2S1P` | `74.20V` | `800W` | `90.42` | `YELLOW` | `2S` voltage can be borderline in high heat on `48V` charging profiles. |
| `4x 200W` (`Voc 37.44V`) | `2S2P` | `74.88V` | `800W` | `93.60` | `YELLOW` | Same `2S` hot-weather margin caution as above. |
| `4x 200W` (`Voc 37.44V`) | `4S1P` | `149.76V` | `800W` | `93.60` | `RED` | Too close to `150V` controller ceiling at STC; cold correction can exceed limit. |
| `5x 200W` (`Voc 37.44V`, overhang) | `5S1P` | `187.20V` | `1000W` | `117.00` | `RED` | Exceeds `150V` MPPT class; requires higher PV-voltage MPPT. |
| `10x 100W` (`Voc 22.79V`) | `5S2P` | `113.95V` | `1000W` | `130.00` | `GREEN` | Strong voltage headroom for `48V` charging on `150/45`. |
| `8x 120W` (`Voc 33.69V`) | `4S2P` | `134.76V` | `960W` | `126.96` | `GREEN` | Climate-conditional fit: with datasheet `Voc temp coeff = -0.25%/C`, `4S` reaches ~`150V` near `-20.2C` (`-4.4F`). |
| `4x 175W` (`Voc 24.48V`) | `4S1P` | `97.92V` | `700W` | `84.80` | `GREEN` | Solid electrical fit, lower total array wattage. |
| `3x 320W` (`Voc 43.82V`) | `3S1P` | `131.46V` | `960W` | `98.70` | `GREEN` | Strong candidate; verify `Voc` at coldest expected temperature before lock. |

## Notes
- Main `150/45` hard limit is PV `Voc < 150V` under worst-case cold conditions. Do not size from STC alone.
- "Cold-corrected `Voc`" means panel/string `Voc` recalculated below `25C` because `Voc` rises as temperature drops.
- Quick formula: `Voc_cold = Voc_stc * (1 + |temp_coeff_Voc| * (25C - T_cold))`.
- For a `48V` bank, low-series strings can struggle in hot conditions when PV operating voltage sags near charge voltage.
- The `3x320W (3S1P)` option is a strong electrical candidate on paper; final decision should be locked only after checking the exact module `Voc` temperature coefficient against your coldest expected ambient.
- If you move to a `250V` MPPT class, some currently `RED` high-series options become viable, but cold-voltage checks are still required.
- Weight basis provided by owner (per-panel rigid weights): `320W=32.9 lbs`, `120W=15.87 lbs`, `100W=13 lbs`, `175W=21.2 lbs`, `200W=23.4 lbs`, `400W=45.21 lbs`.
- `8x120W` quick checkpoints with the provided `-0.25%/C` `Voc` coefficient: about `149.17V` at `0F` (`-17.8C`) and about `151.04V` at `-10F` (`-23.3C`).
