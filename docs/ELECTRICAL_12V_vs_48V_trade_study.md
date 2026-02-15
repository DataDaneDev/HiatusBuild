# Electrical Trade Study: Full 12V vs Current 48V Core

As-of date: `2026-02-15`

Purpose: deeply evaluate whether this build should switch from the current `48V core + 48V->12V distribution` architecture to a full `12V` architecture.

Related inputs:
- `docs/SYSTEMS.md`
- `docs/ELECTRICAL_overview_diagram.md`
- `docs/ELECTRICAL_fuse_schedule.md`
- `bom/bom_estimated_items.csv`
- `bom/load_model_wh.csv`

## Decision Question
- Should this build remain on the current `48V` architecture or switch to full `12V` before implementation freeze?

## Executive Answer
- Keep the current `48V` core architecture for this specific build scope.
- Do not switch to full `12V` at the current size (`10.24 kWh`, `3 kVA` inverter class, `900W` solar, alternator charging path).
- A full `12V` design is technically possible, but it increases high-current design stress, wiring/fusing complexity, and rework risk while delivering limited practical benefit for this configuration.

## Current Build Scope Snapshot (What We Are Actually Designing)
- Battery bank: `2x 48V 100Ah` LiFePO4 (`10.24 kWh` nominal).
- Inverter/charger: Victron MultiPlus-II `48/3000/35-50`.
- Solar: `900W` array with MPPT `150/45`.
- Alternator charging: Sterling `BB1248120` (`~1500W` max output, ~`26A` at ~`57V` battery voltage).
- 12V loads are already planned via Orion `48/12-30` plus branch fuse panel.
- Modeled daily use from canonical load model:
- `core_workday`: `3530 Wh/day`
- `winter_workday`: `4202 Wh/day`

## First Principles: Voltage Does Not Change Energy Need
- Daily energy demand is in `Wh`, not in system voltage.
- Changing from `48V` to `12V` does not reduce required daily energy.
- What voltage changes is current (`A`) required to move that energy.

## Scaling Math (This Is The Core Tradeoff)
Using `I = P / V` and `Ah = Wh / V`:

| Item | 12V nominal (`12.8V`) | 24V nominal (`25.6V`) | 48V nominal (`51.2V`) |
| --- | ---: | ---: | ---: |
| Equivalent bank size for `10.24 kWh` | `800 Ah` | `400 Ah` | `200 Ah` |
| Current for `900W` solar output | `70.3A` | `35.2A` | `17.6A` |
| Current for `1500W` alternator charging | `117.2A` | `58.6A` | `29.3A` |
| Current for `2400W` inverter output (ideal) | `187.5A` | `93.8A` | `46.9A` |
| Current for `3000W` inverter output (ideal) | `234.4A` | `117.2A` | `58.6A` |

Practical inverter example at `2400W` AC and `92%` efficiency:
- `12V`: about `204A` DC input.
- `24V`: about `102A` DC input.
- `48V`: about `51A` DC input.

## What This Means In Real Hardware Terms
- A full `12V` version of this design pushes major circuits into the `~200-300A` class during normal high-AC use.
- At `48V`, those same functions are usually in the `~25-60A` class.
- Lower current generally means:
- smaller/cleaner conductor requirements
- less voltage drop sensitivity
- less resistive heating (`I^2R`)
- easier branch protection coordination

## Quantified Efficiency Reality
Main objection to `48V` is usually conversion loss to feed `12V` loads. For this build, that penalty is real but modest.

Approximate Orion conversion overhead (assuming `93%` efficiency) for currently modeled 12V-native loads:
- `core_workday`: about `122 Wh/day` (about `1.73%` of daily total)
- `winter_workday`: about `135 Wh/day` (about `1.60%` of daily total)
- `minimal_idle_day`: about `45 Wh/day` (about `3.58%` of daily total)

Interpretation:
- Moving to full `12V` would recover some converter loss.
- But that gain is not large enough, by itself, to justify a full architecture change at this system size.

## Existing BOM/Topology Impacts If We Switch To Full 12V
Switching now is not just "change battery voltage"; it forces a cascade redesign:

1. Battery architecture (`bom row 3`)
- Current: `2x 48V 100Ah`.
- Full `12V` equivalent: roughly `800Ah` class bank (for same `10.24kWh` energy).
- Usually means many more parallel amp-hours and more current-sharing sensitivity.

2. Inverter/charger (`bom row 12`)
- Must replace with `12V` inverter/charger equivalent.
- DC-side feeder and protection would move into much higher current range.

3. Solar controller (`bom row 25`)
- Current MPPT `150/45` is correctly sized for the current `48V` plan.
- At `12V`, `150/45` output caps at ~`648W` (`45A * 14.4V`), so it will clip a `900W` array.
- Full `12V` path therefore requires a higher-output controller class.

4. Alternator charging (`bom rows 18, 26`)
- Must replace `12V->48V` charging path with a `12V` house charging design.
- House-side charging currents become much higher for the same charge power.

5. Distribution/protection updates (`docs/ELECTRICAL_fuse_schedule.md`)
- Main DC fuse and feeder strategy would need full recalculation.
- High-current cable, fuse, and disconnect sizing changes materially.

6. Documentation/test re-baseline
- `docs/SYSTEMS.md`, `docs/ELECTRICAL_overview_diagram.md`, and fuse schedule would need broad rewrite and re-validation.

## Legitimate Advantages Of Full 12V
- More common RV/van ecosystem and easier field part availability.
- Native 12V loads can be fed directly without a dedicated step-down converter.
- Lower nominal voltage can feel more familiar for troubleshooting.

## Legitimate Advantages Of Keeping 48V Core
- Much lower current in all major power paths for this power level.
- Cleaner handling of `3kVA` inverter class and high short-duration AC loads.
- Better scaling if future inverter/charging power increases.
- Current project docs/BOM are already coherently designed around this architecture.

## 24V As A Compromise
- `24V` is a technically reasonable middle point.
- It cuts current roughly in half relative to `12V`, but still doubles current versus `48V`.
- At this project stage, switching to `24V` still triggers broad redesign without removing enough complexity to beat staying on `48V`.

## Recommendation For This Build
- Keep `48V` core as the primary architecture.
- Keep `12V` distribution for native RV loads through converter(s).
- Treat `12V` as a distribution layer, not the core energy backbone.

## Conditions That Would Justify Reopening A Full 12V Decision
Re-open only if scope changes materially to most of the following:
- Battery target drops to around `<=5 kWh`.
- Inverter class drops to around `<=2000W`.
- AC cooking/microwave use is reduced or removed.
- Alternator charging expectations drop to lower daily recovery targets.
- Simplicity/common-parts priority outweighs charging/recovery performance.

## Risk-Control Actions If Staying On 48V
1. Protect against single-point failure of the `48V->12V` converter path.
- Carry a spare Orion or design a fast swap path.

2. Keep cable runs short on highest-current circuits.
- Preserve low voltage-drop targets and thermal margin.

3. Validate real-world energy and charging logs early.
- Replace modeled assumptions with measured data after shakedown.

4. Enforce AC load sequencing.
- Prevent simultaneous high-draw AC events from exceeding inverter continuous limits.

## Bottom Line
- A full `12V` architecture is possible, but for this exact system size and load profile it is not the better engineering choice.
- For this project, `48V core + 12V distribution` is the more robust and scalable design with lower high-current stress and lower redesign risk.
