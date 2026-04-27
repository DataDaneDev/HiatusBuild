---
aliases:
  - Solar configuration matrix
tags:
  - hiatus/study
  - hiatus/solar
status: historical
related:
  - "[[SYSTEMS]]"
  - "[[ELECTRICAL_48V_ARCHITECTURE]]"
---

# Solar Configuration Matrix (48V House Baseline)

As-of date: `2026-03-20`

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

### C) Model-level matrix (Renogy + BougeRV Yuma candidates)
> Added for direct panel comparison with dimensions and pricing so CAD fit can be screened quickly.
> Pricing is volatile; values below are snapshot inputs as of `2026-03-20` plus your provided quotes where noted.
> **Section C flag intent (for your current goal):** `GREEN` means a clean exact-`1000W` path exists on a single `Victron 150/45`; `YELLOW` means electrically compatible module family, but exact `1000W` is not clean on one controller.

| Model | Tech / mount style | Rated power | Dimensions (in) | Weight (lbs) | STC electrical (`Vmp` / `Voc`) | Efficiency | Price basis (USD each) | Normalized value (`$/W`, `W/sqft`, `W/lb`) | `150/45` 48V stringing fit | Flag | Verdict |
| --- | --- | ---: | --- | ---: | --- | ---: | --- | --- | --- | --- | --- |
| `Renogy RNG-100DB-H` | Mono flex | `100W` | `48.0 x 21.6 x 0.08` | `4.2` | `18.9V / 22.5V` | `21%` | `$115` (your quote), `$139.99` (Renogy listing reference) | `1.15-1.40`, `13.9`, `23.8` | `4S` and `5S` both viable on `150/45`; `5S2P` supports `1000W` target if roof fit works. | `GREEN` | Best `$ / W` in this set, but standard mono-flex durability remains the main risk unless mounted with airflow and low-strain support. |
| `BougeRV Yuma 100W Pre-Punched` (`ISE152`) | CIGS flex, drilled | `100W` | `43.1 x 27.1 x 0.06` | `3.24` | `24.0V / 30.5V` | `17%` | `$200` (your quote), `$219.99` (BougeRV listing reference) | `2.00-2.20`, `12.3`, `30.9` | Use `3S`/`4S` only. `5S` is not acceptable (`152.5V` STC before cold correction). | `YELLOW` | Strong durability-profile candidate vs conventional mono-flex; very light; exact `1000W` on one controller is awkward (`800W` or `1200W` are clean). |
| `BougeRV Yuma 100W Adhesive-Long` (`ISE137`, "100L") | CIGS flex, long strip | `100W` | `82.2 x 13.7 x 0.06` | `4.63` | `24.0V / 30.5V` | `17%` | `$249.99` (BougeRV listing reference) | `2.50`, `12.8`, `21.6` | Use `3S`/`4S` only. | `YELLOW` | Best fit-helper shape for narrow roof lanes/CAD packing, but exact `1000W` on one controller is awkward (`800W` or `1200W` are clean). |
| `BougeRV Yuma 200W Adhesive` (`ISE138`) | CIGS flex, long rectangle | `200W` | `82.2 x 26.0 x 0.06` | `8.44` | `24.0V / 30.4V` | `17%` | `$419.99` (BougeRV listing reference) | `2.10`, `13.5`, `23.7` | Use `3S`/`4S` only. | `YELLOW` | Good compromise if you want fewer modules/cable runs; exact `1000W` on one controller is not a clean string set (`800W` or `1200W` are clean). |
| `BougeRV Yuma 200W Pre-Punched` (`ISE154`) | CIGS flex, drilled | `200W` | `82.8 x 27.1 x 0.06` | `5.95` | `24.0V / 30.4V` | `17%` | `$409.99` (BougeRV listing reference) | `2.05`, `12.8`, `33.6` | Use `3S`/`4S` only. | `YELLOW` | High-priority CAD candidate for robust mechanical fastening and fewer panels; exact `1000W` on one controller is not a clean string set (`800W` or `1200W` are clean). |

Notes:
- BougeRV web pages can mix variant blocks in one view; lock each final part by `SKU` and downloaded manual before purchase.
- Local reference PDF for BougeRV in this repo is image-based; electrical/dimension values above were cross-checked from current BougeRV product pages/manual links.

### D) Full-array comparison (targeting `~1000W`)
> This is the array-level view you asked for: what each configuration looks like when scaled to a `~1000W` goal.
> `Victron 150/45` power limit is not the blocker at `~1000W`; string architecture and panel `Voc/Vmp` classes are the blocker.

| Configuration | Panels for ~1000W | Array watts | Est. total footprint (sqft, raw panel area) | Est. total weight (lbs) | Est. total cost (USD) | Normalized (`$/W`, `W/sqft`, `W/lb`) | Clean single-`150/45` wiring for this wattage? | Closest clean single-controller options |
| --- | ---: | ---: | ---: | ---: | ---: | --- | --- | --- |
| `Renogy RNG-100DB-H` | `10 x 100W` | `1000W` | `72.0` | `42.0` | `$1,150-$1,399.90` | `1.15-1.40`, `13.9`, `23.8` | `YES` (`5S2P`) | N/A (`1000W` is clean). |
| `Yuma 100W Pre-Punched (ISE152)` | `10 x 100W` | `1000W` | `81.1` | `32.4` | `$2,000-$2,199.90` | `2.00-2.20`, `12.3`, `30.9` | `NO` (no clean equal-string layout at exact `1000W` on one controller). | `800W` (`4S2P`) or `1200W` (`3S4P`). |
| `Yuma 100W Adhesive-Long (ISE137 / 100L)` | `10 x 100W` | `1000W` | `78.2` | `46.3` | `$2,499.90` | `2.50`, `12.8`, `21.6` | `NO` (same `Voc/Vmp` class as Yuma 100 pre-punched). | `800W` (`4S2P`) or `1200W` (`3S4P`). |
| `Yuma 200W Adhesive (ISE138)` | `5 x 200W` | `1000W` | `74.2` | `42.2` | `$2,099.95` | `2.10`, `13.5`, `23.7` | `NO` (cannot build a clean exact-`1000W` string set on one `150/45`). | `800W` (`4S1P`) or `1200W` (`3S2P`, `6` panels). |
| `Yuma 200W Pre-Punched (ISE154)` | `5 x 200W` | `1000W` | `77.9` | `29.8` | `$2,049.95` | `2.05`, `12.8`, `33.6` | `NO` (same `Voc/Vmp` class as other Yuma modules). | `800W` (`4S1P`) or `1200W` (`3S2P`, `6` panels). |

Practical implication:
- If `1000W` exact on a **single** `Victron 150/45` is mandatory, this shortlist strongly favors `Renogy 100W` (`5S2P`).
- If CIGS durability is mandatory, accept a clean CIGS step size of either `800W` or `1200W` (or add a second MPPT and redesign around compatible string voltages).

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
   - For `Renogy RNG-100DB-H` (`Voc 22.5V`), `4S` or `5S` strings are generally viable.
   - For `BougeRV Yuma` modules (`Voc ~30.4-30.5V`), design around `3S` or `4S`; avoid `5S`.

## Recommended Path (revision)
### Preferred near-term direction
- Keep a **flexible-first target of `~800–1000W`** under the `75 lb` cap, but split by chemistry class:
  - **Cost-first and exact-`1000W` path (single controller):** `Renogy 100W` class (`5S2P`).
  - **Durability-first CIGS path:** prioritize `Yuma 200W Pre-Punched` for CAD at a clean `800W` (`4S1P`) or `1200W` (`3S2P`).
  - **Fit-first CIGS path:** evaluate `Yuma 100L` in CAD where narrow roof channels are needed.

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

## Source References (for this update)
- Local datasheet: `references/100-Watt 12-Volt Flexible Monocrystalline Solar Panel RNG-100DB-H.pdf` (Renogy `RNG-100DB-H` electrical/mechanical specs).
- BougeRV model pages used for live variant pricing/specs on `2026-03-20`:
  - `https://www.bougerv.com/products/100w-flexible-solar-panel`
  - `https://www.bougerv.com/products/200-watt-cigs-flexible-solar-kit`
  - `https://www.bougerv.com/products/200-watt-cigs-flexible-solar-system-kit`
  - `https://www.bougerv.com/products/yuma-200w-cigs-flexible-solar-panel-square-with-holes`
