# Build Order of Operations (Truck Bed Camper)

## Purpose
- Define a practical order of operations that still supports parallel workstreams.
- Prioritize "build modules now, drop in later" for the fixed camper install date on May 7, 2026.

## Planning assumptions (as-of 2026-02-15)
- Fixed install date: May 7, 2026.
- Time remaining from baseline date: 81 days.
- This plan assumes a Hiatus truck bed camper install with major module prep done before delivery.
- Electrical architecture and BOM assumptions in `docs/SYSTEMS.md` remain the active baseline.

## Typical full-build sequence (once camper shell is physically in hand)
1. Layout freeze and service-map freeze
- Lock exact locations for: batteries, inverter/charger, Lynx, tank(s), pump, heater, shore inlet, solar entry, cable chases, and service access panels.
- Output: dimensioned layout + no-conflict service map.

2. Structural and weather-critical penetrations
- Roof/wall/floor penetrations and backing plates first (fan, cable gland, shore power inlet, heater combustion/exhaust/intake paths, drains/vents as needed).
- Output: all shell penetrations sealed and leak-checked.

3. Floor build (if included in shell phase)
- Floor insulation and subfloor/finished floor substrate after under-floor penetrations are known.
- Output: stable floor datum for cabinetry/module tie-down points.

4. Rough-in phase (electrical + plumbing + heating + comms)
- Pull trunk wiring, branch runs, fuse/disconnect mounting backers, plumbing supply/drain lines, and heater duct/fuel routing.
- Keep rough-in accessible and labeled.
- Output: rough-in complete with service loops and protection in place.

5. Pre-close test gate
- Electrical continuity/polarity checks, insulation resistance where relevant, initial low-power energization, plumbing pressure/leak checks.
- Output: signed pre-close checklist before insulation/wall closure.

6. Insulation and interior panel closure
- Wall/ceiling insulation and vapor/air-control details after rough-in passes test gate.
- Install wall/ceiling panels with removable access strategy at key service points.
- Output: closed envelope without burying unresolved systems.

7. Cabinetry/module installation
- Install bench/electrical cabinet, galley, tank mounts, and structural anchoring.
- Keep final wire and plumbing terminations deferred until modules are fixed in final position.
- Output: all major modules mounted and restrained.

8. Final terminations and system commissioning
- Finalize AC/DC terminations, fuse installation, bonding/ground checks, plumbing hookups, pump and heater commissioning, device configuration.
- Output: full functional test passed with documented settings.

9. Shakedown and punch-list closure
- Short local trip + full workday simulation, then resolve issues before long deployment.
- Output: punch list closed or triaged with risk ranking.

## Parallel-work mindset (how to avoid strict-trade bottlenecks)
- Stream A: module fabrication
- Build electrical bench module, cabinet carcasses, and plumbing assemblies off-vehicle.
- Stream B: design and routing
- Finalize all run lengths, penetrations, fuse IDs, labels, and mounting hole maps.
- Stream C: verification
- Bench-test subsystems early (charger paths, converter outputs, USB/AC branch behavior, pressure tests).
- Stream D: shell execution
- Once shell is available, execute penetrations -> rough-in -> close-up using prepared modules and harnesses.

## Date-window draft plan (baseline date: February 15, 2026)
1. February 16 to February 29
- Freeze interior layout and service map.
- Freeze penetration map and builder questions list.
- Place remaining long-lead orders.

2. March 1 to March 22
- Build and bench-test electrical module(s) and sub-panels.
- Build cabinet/module frames and mounting interfaces.
- Build labeled harness sets and branch bundles to planned lengths.

3. March 23 to April 12
- Complete plumbing subassemblies (tank/pump/manifold concepts).
- Build install templates/jigs for repeatable placement.
- Finalize commissioning checklists and label packs.

4. April 13 to May 3
- Re-verify BOM completeness against install sequence.
- Perform dry-fit rehearsal of module footprints and fastener plans.
- Prep install kits by stage (penetrations, rough-in, close-up, commissioning).

5. May 4 to May 6
- Final pre-install readiness gate:
- all hardware on hand,
- all modules bench-tested,
- all drawings/checklists printed/exported,
- known risks logged in `docs/TRACKING.md`.

6. May 7 (install day)
- Execute shell-dependent scope and drop in prebuilt modules where possible.
- Capture deviations from planned routing or dimensions immediately.

7. May 8 to May 24
- Complete rough-in/termination sequence if not finished on install day.
- Run commissioning tests and first shakedown cycle.

## Critical hold points (do not skip)
- Hold 1: No penetrations until layout + service map is frozen.
- Hold 2: No insulation/panel closure until rough-in test gate passes.
- Hold 3: No final cabinetry close-out until service access is verified.
- Hold 4: No field deployment until shakedown defects are triaged.

## Truck-bed-camper adaptations vs typical van guides
- Less bare-metal body prep than a cargo van, but shell penetrations/sealing quality is even more critical.
- Module-first fabrication is higher leverage because camper install date is fixed and shell access is delayed.
- Serviceability matters more than perfect concealment in the first build cycle.

## Source references used for sequencing research
- Engineers Who Van Life, "Step-by-Step Guide for Building a DIY Van Conversion":
- https://engineerswhovanlife.com/diy-van-build-guide/
- GearJunkie, "How To Convert a Van for Life on the Road":
- https://gearjunkie.com/motors/van-life/van-conversion
- The Van Conversion, "Van Conversion Step-by-Step Guide":
- https://thevanconversion.com/van-conversion-step-by-step-guide/
- The Vansmith, "How Long Does a Van Conversion Take?":
- https://www.thevansmith.com/post/how-long-does-a-van-conversion-take

## Next doc integration points
- Update `docs/TRACKING.md` with sequence-related open risks after first dry-fit rehearsal.
- If date windows change, update this file and `docs/PROJECT.md` together so milestone language stays aligned.
