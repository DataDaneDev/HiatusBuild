# Electrical Trade Study: 12V vs 24V vs 48V Core

As-of date: `2026-02-17`

Purpose: re-evaluate the house electrical voltage architecture (`12V`, `24V`, or `48V` core) for a DIY truck bed camper remote-office build, and make explicit *exactly* what changes in BOM, wiring, and protection when switching.

Related inputs:
- `docs/SYSTEMS.md`
- `docs/ELECTRICAL_overview_diagram.md`
- `docs/ELECTRICAL_fuse_schedule.md`
- `bom/bom_estimated_items.csv`
- `bom/load_model_wh.csv`

## What Triggered This Revisit
The prior decision assumed an AC-capable kitchen (`induction` + `microwave`) and a `3kVA` inverter class. If those AC loads are removed (propane cooking, no microwave) and the office is DC-first, the “48V is mandatory” argument weakens, and the architecture decision should be re-scored.

## Decision Questions (In Order)
1. Do we still want “AC kitchen” capability (induction/microwave), or are we committing to propane cooking and an AC-light build?
2. What inverter strategy is actually required: always-on inverter/charger (`MultiPlus` class), or a small inverter used occasionally?
3. Given the above, what core bus voltage best fits the goals: simplicity, serviceability, fast charging (alternator + solar), and a large bank (`10–15 kWh`)?

## Two Scopes (This Is The Fork)
### Scope A — AC-Capable Kitchen (Prior Baseline)
- Keep: induction cooking and microwave.
- Implies: `2–3 kW`+ inverter class makes sense, often on for long windows.
- Result: high DC power paths are “normal,” favoring higher voltage cores (`24V`/`48V`).

### Scope B — DC-First Office + Propane Cooking (New Candidate)
- Remove: induction cooktop and microwave.
- Prefer: DC-native office power (USB‑C PD from `12V`, monitor moved to DC if possible), inverter off most of the day.
- Result: inverter becomes “occasional AC convenience” rather than a core always-on subsystem.

Planning-level impact using the current load model v3 as a starting point:
- Current modeled totals: `core_workday = 3,530 Wh/day`, `winter_workday = 4,202 Wh/day` (`bom/load_model_wh.csv`).
- If you remove induction + microwave + “always-on” inverter idle overhead, daily energy drops to roughly:
  - `core_workday`: ~`2,750 Wh/day` (down ~`780 Wh/day`)
  - `winter_workday`: ~`3,170 Wh/day` (down ~`1,030 Wh/day`)
These are derived deltas from the existing rows; they should be locked by editing `bom/load_model_wh.csv` once you commit to the propane/no-microwave scope.

## Current Build Snapshot (What The Repo Is Currently Designed Around)
- Battery bank: `3x 48V 100Ah` LiFePO4 (`15.36 kWh` nominal).
- Inverter/charger: Victron MultiPlus-II `48/3000/35-50`.
- Solar: `900W` array with MPPT `150/45`.
- Alternator charging: Sterling `BB1248120` (`~1500W` max output, ~`26A` at ~`57V` battery voltage).
- 12V loads via Orion `48/12-30` plus branch fuse panel.

## First Principles: Voltage Does Not Change Energy Need
- Daily energy demand is in `Wh`, not in system voltage.
- Changing from `48V` to `12V` does not reduce required daily energy.
- What voltage changes is current (`A`) required to move that energy.

## Scaling Math (This Is The Core Tradeoff)
Using `I = P / V` and `Ah = Wh / V` (nominals: `12.8V`, `25.6V`, `51.2V`):

| Item | 12V nominal (`12.8V`) | 24V nominal (`25.6V`) | 48V nominal (`51.2V`) |
| --- | ---: | ---: | ---: |
| Equivalent bank size for `10.24 kWh` | `800 Ah` | `400 Ah` | `200 Ah` |
| Equivalent bank size for `15.36 kWh` | `1200 Ah` | `600 Ah` | `300 Ah` |
| Current for `900W` solar output | `70.3A` | `35.2A` | `17.6A` |
| Current for `1500W` alternator charging | `117.2A` | `58.6A` | `29.3A` |
| Current for `1000W` inverter output (ideal) | `78.1A` | `39.1A` | `19.5A` |
| Current for `2000W` inverter output (ideal) | `156.3A` | `78.1A` | `39.1A` |
| Current for `3000W` inverter output (ideal) | `234.4A` | `117.2A` | `58.6A` |

Practical inverter note: with `90–93%` efficiency, DC input current is ~`8–11%` higher than the “ideal” numbers above.

### Important Nuance: The Truck/Alternator Side Is Still 12V
Even with a `12V->48V` charger, the alternator/starter-battery side is still a `~100A+` circuit at `~1.5kW` charge power. Higher house voltage mainly reduces current on the *house-side* wiring (and makes long runs from charger/MPPT to the bank easier).

## What This Means In Real Hardware Terms
- Under Scope A (AC kitchen + `3kVA` inverter), a `12V` core pushes normal-use circuits into the `~200–300A` class.
- Under Scope B (AC-light + `~1kW` inverter used occasionally), a `12V` core is usually in the `~50–150A` class for charging and typical loads.
- Lower current generally means: smaller conductors, less voltage drop stress, less `I^2R` heat, and easier protection coordination.

## Quantified Efficiency Reality
Main objection to `48V` is usually conversion loss to feed `12V` loads. For this build, that penalty is real but modest.

Approximate Orion conversion overhead (assuming `93%` efficiency) for currently modeled 12V-native loads:
- `core_workday`: about `122 Wh/day` (about `1.73%` of daily total)
- `winter_workday`: about `135 Wh/day` (about `1.60%` of daily total)
- `minimal_idle_day`: about `45 Wh/day` (about `3.58%` of daily total)

Interpretation:
- Moving to full `12V` would recover some converter loss.
- But that gain is not large enough, by itself, to justify a full architecture change; the real driver would be “Scope B” simplification (smaller/less-used inverter and deleting the step-down layer).

## Exactly What Changes Between 12V / 24V / 48V (Core + Distribution)
Assumption: you still want a `12V` distribution layer for RV-native loads (fridge, diesel heater, pumps, detectors, USB‑C PD, etc.).

| System area | 12V core (full 12V) | 24V core + 12V distribution | 48V core + 12V distribution (current) |
| --- | --- | --- | --- |
| **Battery bank for `10–15 kWh`** | Large `Ah` bank (`~800–1200Ah`); typically multiple batteries in parallel or a big DIY pack | Mid `Ah` bank (`~400–600Ah`); fewer parallels than 12V | Lower `Ah` bank (`~200–300Ah`); fewest parallels |
| **Inverter strategy** | Small `12V` inverter is feasible if Scope B; `3kVA` at 12V is high-current and wiring-heavy | `24V` inverter/charger options are common and “mid-current” | `48V` shines for `3kVA` class and higher |
| **Solar MPPT sizing (900W)** | Needs higher *output current* controller (e.g., `70–100A` class); `150/45` will clip | `150/45` class is generally fine; output current moderate | `150/45` class is fine; lowest output current |
| **Alternator charging (1.5kW class)** | House-side current ~`110A`; long runs become heavy copper | House-side current ~`55–60A`; easier cabling | House-side current ~`25–30A`; easiest cabling |
| **12V distribution** | Direct (no step-down converter) | Requires `24->12` DC-DC converter(s) | Requires `48->12` DC-DC converter(s) |
| **Fuse voltage class (common gotcha)** | `32V` ecosystem everywhere | `32V` ecosystem everywhere (8S LiFePO4 peaks < `32V`) | Must enforce `58V/80V` rated fuses on 48V paths |
| **Wiring bulk/routeability** | Heaviest on charge + inverter feeders | Moderate | Lightest |
| **Debug/service ecosystem** | Most RV/van parts are natively 12V | Less common but still widely supported | Less common RV-native, more “power-systems” style |

### What Stays The Same (Regardless Of Core Voltage)
- The load model (Wh/day) and autonomy targets do not change; only current and component sizing change.
- The `12V` branch fuse panel, labeling approach, and most RV-native loads remain `12V` (fridge/heater/pumps/detectors/USB‑C PD).
- Monitoring concepts remain the same (shunt + GX + temp sensing); the shunt still goes in the main negative path.
- AC safety requirements (GFCI/RCD, correct neutral/ground behavior, strain relief, etc.) do not change.

## Solar Stringing + Shading Note (Because It Came Up)
- Battery voltage sets the *minimum PV voltage* the MPPT needs to stay in regulation. A `48V` bank requires higher PV operating voltage than `12V`/`24V`.
- In partial shade, PV voltage can sag. Lower-voltage banks can therefore stay charging in “worse PV voltage” conditions *if* your stringing is close to the minimum for a `48V` bank.
- The biggest shade lever is usually array topology (more parallel strings, bypass diode behavior, and MPPT configuration) rather than the battery voltage alone.

## Existing BOM/Topology Impacts If We Switch (From The Current 48V Baseline)
Switching is not just “change battery voltage”; it cascades through charge sources, protection, and wiring.

1. Battery architecture (`bom row 3`)
- Current: `3x 48V 100Ah`.
- Full `12V` equivalent: roughly `800Ah` class bank (for same `10.24kWh` energy) or `~1200Ah` for `15.36kWh`.
- `24V` equivalent: `~400Ah` (`10.24kWh`) to `~600Ah` (`15.36kWh`).

2. Inverter/charger (`bom row 12`)
- `12V`: replace with `12V` inverter/charger (or shift to “small inverter + standalone shore charger” if Scope B).
- `24V`: replace with `24V` inverter/charger.
- DC-side feeder/protection scales directly with the current table above.

3. Solar controller (`bom row 25`)
- Current MPPT `150/45` is correctly sized for the current `48V` plan.
- At `12V`, `150/45` output caps at ~`648W` (`45A * 14.4V`), so it will clip a `900W` array. Full `12V` requires a higher-output controller class.
- At `24V`, `150/45` output caps at ~`1296W` (`45A * 28.8V`), so it will *not* clip a `900W` array.

4. Alternator charging (`bom rows 18, 26`)
- `12V`: replace `12V->48V` charger with a `12V->12V` current-limited charger/isolator strategy; house-side currents become ~`100A+` for `~1.5kW`.
- `24V`: replace with a `12V->24V` charger; house-side current becomes ~`55–60A` for `~1.5kW`.

5. 12V distribution layer (`bom row 20`)
- `12V`: remove the Orion `48/12-30` entirely (12V loads feed directly).
- `24V`: replace with a `24/12` converter (still needed).
- `48V`: keep as-is (or expand redundancy if desired).

6. DC bus / disconnect / fuse hardware (`bom rows 5, 6, 7, 10, 11, 105`)
- Your disconnect current rating and fuse strategy must match the new peak currents (inverter + charging).
- `12V/24V` can live in a `32V` fuse ecosystem; `48V` requires enforced `58V/80V` DC-rated fuses on 48V paths.
- You can still use a Lynx/busbar approach at any voltage, but fuse values and conductor gauges will change.

7. Documentation/test re-baseline
- `docs/SYSTEMS.md`, `docs/ELECTRICAL_overview_diagram.md`, and fuse schedule would need broad rewrite and re-validation after the architecture is chosen.

### BOM Swap Matrix (Concrete “What Changes” By Row)
This is intentionally “class of part,” not a final SKU lock.

| BOM row | Current (48V baseline) | If 12V core | If 24V core |
| ---: | --- | --- | --- |
| `3` | `3x 48V 100Ah` batteries | Replace with `~10–15 kWh` 12V bank (`~800–1200Ah` total) | Replace with `~10–15 kWh` 24V bank (`~400–600Ah` total) |
| `12` | MultiPlus-II `48/3000` | Replace with smaller `12V` inverter/charger *or* “small inverter + standalone charger” | Replace with `24V` inverter/charger sized to real AC needs |
| `18` + `26` | Sterling `BB1248120` + `BBR` (12/24 -> 48) | Replace with `12V -> 12V` current-limited alternator charging strategy (`~100A` class for `~1.5kW`) | Replace with `12V -> 24V` alternator charger (`~60A` class for `~1.5kW`) |
| `20` | Orion `48/12-30` | Remove (12V loads feed directly) | Replace with a `24/12` converter sized to 12V loads |
| `25` | MPPT `150/45` | Replace with higher output-current MPPT (because `45A` clips `900W` at 12V) | Keep `150/45` (no clipping at 900W) |
| `10` + `105` | 48V-rated MEGA/MIDI spares | Swap to 32V-rated fuses sized for new currents | Swap to 32V-rated fuses sized for new currents |

## Legitimate Advantages Of Full 12V
- More common RV/van ecosystem and easier field part availability.
- Native 12V loads can be fed directly without a dedicated step-down converter.
- Lower nominal voltage can feel more familiar for troubleshooting.

## Legitimate Advantages Of Keeping 48V Core
- Much lower current in all major power paths for this power level.
- Cleaner handling of `3kVA` inverter class and high short-duration AC loads.
- Better scaling if future inverter/charging power increases.
- Current project docs/BOM are already coherently designed around this architecture.

## 24V As A Compromise (Often The Sweet Spot)
- `24V` cuts current roughly in half relative to `12V`, while avoiding most of the “48V-only fuse-rating discipline” burden.
- For a `10–15 kWh` bank with `~1–2 kW` fast charging goals, `24V` often lands in an easy-to-wire current range without forcing 48V parts.
- Downside: it still requires a `24->12` conversion layer if you keep 12V RV loads.

## Recommendation (Current Project Decision)
Selected architecture: **keep `48V` core + `12V` distribution**.

Why this is still coherent with your goals:
- You still want a large bank (`10–15 kWh`) and fast charging from alternator + solar.
- `48V` keeps main current lower in the highest-power paths (inverter, MPPT battery side, alternator charger output side).
- The current BOM, fuse strategy, and topology are already aligned to this architecture, minimizing redesign churn.

## Next Steps (Given 48V Lock)
1. Keep `48V` core components as the baseline in `bom/bom_estimated_items.csv` (rows `3`, `12`, `18`, `20`, `25` and fuse rows tied to them).
2. If induction/microwave are dropped, update `bom/load_model_wh.csv` to a new Scope B profile while keeping the `48V` architecture.
3. Recompute `docs/SYSTEMS.md` autonomy and charging tables from that revised load model.
4. Keep `docs/ELECTRICAL_overview_diagram.md` and `docs/ELECTRICAL_fuse_schedule.md` on the current `48V` implementation path.

## How To Choose (Rules Of Thumb)
Use these as “quick filters” before you get lost in product selection.

### 12V core tends to be best when
- AC loads are modest (`<=1–2 kW` continuous) and the inverter is not always-on (Scope B).
- Most loads are `12V` native and you want to delete the `24/48 -> 12V` converter layer.
- You accept that “fast charging” becomes `~70–120A` class wiring on the house side.

### 24V core tends to be best when
- You want comfortable headroom for a `2–3 kW` inverter class without `250A+` class DC runs.
- You still want a large bank (`10–15 kWh`) and fast charging, but want to stay in `~50–120A` class house-side currents.
- You accept keeping a `24->12` converter layer for RV-native loads.

### 48V core tends to be best when
- You want `3 kW`+ inverter class, long runs, and/or future scaling, and you want to keep main DC currents low.
- You can enforce the `58V/80V` fuse-rating discipline and accept the converter layer.

## Risk-Control Actions If Staying On 48V
1. Protect against single-point failure of the `48V->12V` converter path.
   - Carry a spare Orion or design a fast swap path.

2. Keep cable runs short on highest-current circuits.
   - Preserve low voltage-drop targets and thermal margin.

3. Validate real-world energy and charging logs early.
   - Replace modeled assumptions with measured data after shakedown.

4. Enforce AC load sequencing.
   - Prevent simultaneous high-draw AC events from exceeding inverter continuous limits.

## Risk-Control Actions If Switching To Full 12V
1. Treat the bank as a high-current system even if loads are “low.”
   - Use per-battery fusing (or per-string) and equal-length cables/busbar layout so parallel batteries share current.

2. Keep high-current runs short.
   - Put MPPT(s), DC-DC charger(s), inverter, and main disconnect/fusing physically close to the bank; design around voltage-drop rather than “ampacity only.”

3. Choose charge hardware with realistic thermal derating.
   - A `~100A` class alternator-charging plan and a `~70A` class solar-output plan are normal for `900W` into `12V`; size wiring, fusing, and ventilation accordingly.

## Bottom Line
- Architecture for this project is now locked back to **`48V` core + `12V` distribution**.
- `12V` and `24V` alternatives remain documented here as reference options, but they are not the active implementation path.
