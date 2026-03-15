# Solar Configuration Matrix (48V House Baseline)

As-of date: `2026-03-15`

Purpose: re-screen roof solar configurations after updated mechanical constraint:
- House bank: `48V` nominal (`51.2V` LiFePO4 class)
- Controller baseline: `Victron SmartSolar MPPT 150/45`
- **Hard cap from Hiatus:** `75 lbs` total panel weight on roof
- Scope in this revision: `rigid` and `flexible` panel paths

Flag meaning:
- `GREEN`: viable candidate on current baseline and under `75 lbs` cap (still verify final datasheet values and cold-weather `Voc` correction).
- `YELLOW`: usable but conditional (thermal margin, durability, mounting, or lifecycle caveats).
- `RED`: fails current baseline due to weight and/or electrical incompatibility.

## Decision Snapshot (given 75 lb hard cap)
- The original higher-watt rigid plans are effectively eliminated by weight (`800–1000W` rigid sets were `~90–130 lbs`).
- Under current known rigid weights, realistic rigid options top out around `~480–700W` while staying `<75 lbs`.
- Flexible solar is now the practical path to keep higher roof coverage and stay under the cap, but must be designed around heat, mounting method, and shorter expected service life vs rigid.

## Updated Candidate Configurations

### A) Rigid options (re-screened for 75 lb cap)
| Option | Wiring | String Voc (STC) | Total wattage | Total weight (lbs) | Flag (`150/45` + 75 lb cap) | Notes |
| --- | --- | ---: | ---: | ---: | --- | --- |
| `3x 200W` (`Voc 37.44V`) | `3S1P` | `112.32V` | `600W` | `70.20` | `GREEN` | Best high-output rigid option currently under weight cap. |
| `5x 100W` (`Voc 22.79V`) | `5S1P` | `113.95V` | `500W` | `65.00` | `GREEN` | Good voltage margin; lower roof watts. |
| `4x 120W` (`Voc 33.69V`) | `4S1P` | `134.76V` | `480W` | `63.48` | `GREEN` | Electrically strong; verify cold `Voc` by climate. |
| `3x 175W` (`Voc 24.48V`) | `3S1P` | `73.44V` | `525W` | `63.60` | `YELLOW` | `3S` may run tighter voltage margin in very hot roof conditions. |
| `1x 400W` (`Voc 37.10V`) | `1S1P` | `37.10V` | `400W` | `45.21` | `RED` | `1S` is generally unsuitable for reliable `48V` charging with MPPT headroom. |
| `4x 175W` (`Voc 24.48V`) | `4S1P` | `97.92V` | `700W` | `84.80` | `RED` | Electrically solid, but fails `75 lb` hard cap. |

### B) Flexible options (practical path to fuller roof coverage)
> Flexible entries are based on common market classes (not a locked model selection yet). Final lock requires exact module datasheets.

| Option class | Typical per-panel stats (market range) | Example wiring | Array STC watts | Approx array weight | Flag (`150/45` + 75 lb cap) | Notes |
| --- | --- | --- | ---: | ---: | --- | --- |
| `8x 100W` ETFE mono-flex | `100W`, `Voc ~22–24V`, `~4.5–6.5 lbs` each | `4S2P` (`Voc ~88–96V`) | `800W` | `~36–52 lbs` | `GREEN` | Strong balance of watts vs weight. Ensure mounting allows heat shedding. |
| `10x 100W` ETFE mono-flex | `100W`, `Voc ~22–24V`, `~4.5–6.5 lbs` each | `5S2P` (`Voc ~110–120V`) | `1000W` | `~45–65 lbs` | `GREEN` | Highest practical roof wattage while remaining under cap for most products. |
| `4x 200W` ETFE mono-flex | `200W`, `Voc ~24–28V`, `~8–11 lbs` each | `4S1P` (`Voc ~96–112V`) | `800W` | `~32–44 lbs` | `GREEN` | Fewer penetrations/wires; confirm real panel dimensions and roof fit. |
| `6x 150W` CIGS-flex class | `150W`, `Voc ~20–26V`, `~5–8 lbs` each | `3S2P` or `4S2P*` | `900W` | `~30–48 lbs` | `YELLOW` | Excellent low weight and shade tolerance, but specific voltage varies widely by model; wiring must match selected datasheet. |
| `12x 100W` flex (dense fill) | `100W`, `Voc ~22–24V`, `~4.5–6.5 lbs` each | `6S2P` (`Voc ~132–144V`) | `1200W` | `~54–78 lbs` | `YELLOW` | Can exceed weight with heavier panels and may approach `150V` cold limit; climate check mandatory. |

`*` `4S2P` only if selected module `Voc` and cold correction stay safely below controller maximum.

## Flexible-Solar Specific Findings (important)
1. **Weight advantage is decisive now.**
   - Flexible arrays can deliver `~800–1000W` under `75 lbs`, whereas rigid options in this project context mostly cap out around `~500–600W`.

2. **Heat management is the #1 performance/lifetime lever.**
   - Fully bonded flexible modules run hotter than standoff rigid modules.
   - Hotter cell temps reduce instantaneous output and can accelerate adhesive/backsheet aging.
   - Prefer mounting details that allow at least partial airflow paths and avoid trapping water.

3. **Lifecycle expectation is usually shorter than rigid.**
   - Practical planning assumption: flexible modules often have shorter real-world service life than framed rigid modules (especially in high-heat mobile-roof duty).
   - Procurement should prioritize clear warranty language (power warranty + product warranty + exclusions for mobile/RV use and bonding method).

4. **Material stack matters.**
   - Prefer ETFE-front flexible modules over older PET-front constructions for abrasion/UV resistance.
   - Verify junction box potting quality, cable strain relief, and backsheet temperature rating.

5. **Electrical architecture still matters on 48V.**
   - Even with flex, avoid low-series strings that can lose MPPT headroom on very hot days.
   - For most `100W` flex classes, `4S` or `5S` strings are usually safer than `2S/3S` for `48V` charging margin.

## Recommended Path (revision)
### Preferred near-term direction
- Move to a **flexible-first design target of `~800–1000W`** under the `75 lb` cap.
- Baseline candidate to investigate first:
  - `10x 100W` ETFE-flex class, wired `5S2P` (if final dimensions fit your roof map and cold-corrected `Voc` remains compliant).

### Conservative fallback
- If lifecycle risk of flex is unacceptable, select **`3x 200W` rigid (`600W`)** as the best under-cap rigid configuration.

## Pre-Purchase Validation Checklist (must-do before lock)
1. Collect exact datasheets for 2–3 finalist flexible modules and verify:
   - `Voc`, `Vmp`, `Isc`, `Imp`, `Voc temp coefficient`, dimensions, weight, min bend radius.
2. Run cold correction with your worst-case ambient:
   - `Voc_cold = Voc_stc * (1 + |temp_coeff_Voc| * (25C - T_cold))`
   - Keep corrected string `Voc` below controller absolute max with safety margin.
3. Confirm hot-weather MPPT headroom:
   - Ensure expected hot `Vmp` still comfortably exceeds battery charging voltage.
4. Confirm mounting stack-up:
   - Adhesive system (e.g., VHB pattern + sealant), cable routing, drip paths, and serviceability.
5. Confirm warranty fit for vehicle roof use:
   - Explicitly check exclusions related to curvature, bonding method, and vibration/mobile duty.

## Legacy weight basis retained from prior study (rigid)
- `320W=32.9 lbs`, `120W=15.87 lbs`, `100W=13 lbs`, `175W=21.2 lbs`, `200W=23.4 lbs`, `400W=45.21 lbs`.
