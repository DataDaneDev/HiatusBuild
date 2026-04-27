# Build Order of Operations (Truck Bed Camper)

## Purpose
- Define a practical order of operations that still supports parallel workstreams.
- Prioritize "build modules now, drop in later" for the fixed camper install date on May 7, 2026.

## Planning assumptions (as-of 2026-04-27)
- Fixed install appointment: May 7, 2026 at `9:00 AM` in Bellingham, Washington.
- Travel constraint: truck starts in Park City, Utah; stage near Bellingham by the evening of May 6.
- This plan assumes a Hiatus truck bed camper install with only reversible/module-first prep before delivery.
- Electrical architecture and BOM assumptions in `docs/core/SYSTEMS.md` remain the active baseline.

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
- Flooring stack-up, hardpoint method, and procurement status are tracked in `docs/implementation/FLOORING_subfloor_build_process.md`.

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
- Finalize measured physical run lengths, penetrations, fuse IDs, labels, and mounting hole maps (bench layout first, CAD lengths as reference-only).
- Stream C: verification
- Bench-test subsystems early (charger paths, converter outputs, USB/AC branch behavior, pressure tests).
- Stream D: shell execution
- Once shell is available, execute penetrations -> rough-in -> close-up using prepared modules and harnesses.

## Date-window execution plan (baseline date: April 27, 2026)
1. April 27 to April 28 (plan reset + shore AC-in lock)
- Use `docs/plans/INSTALL_MINUS_12_READINESS_PLAN.md` as the integrated Apr 27-May 11 plan.
- Confirm travel and install logistics for a May 7 `9:00 AM` Bellingham appointment.
- SKU-lock/order AC-in initial-charge hardware first: rows `107`, `108`, `123`, `13`, `109`, `14`, and `114`; do not let final AC-out receptacle count block this path.

2. April 29 to May 1 (electrical closet + floor/truck interface gates)
- Validate electrical Board A/B layout on physical plywood, including service access, fuse-holder matching, labels, and cable corridors.
- Trim EPS, verify three-piece plywood fit, preserve hardpoint pockets, and keep Lonseal glue-down gated.
- Remove/inspect bed rail caps, confirm old `2 in x 3 in` rail holes are not needed by Hiatus, and seal dust/weather intrusion points with low-profile flexible/serviceable methods.

3. May 2 to May 3 (layout/extrusion/plumbing decisions)
- Treat current furniture CAD as reference-only after the Iceco/water tank dry-fit conflict; rework block envelopes first.
- Place a stock-length starter extrusion/hardware order for rough frames, not final cut lengths or drawers.
- Add faucet/sink/drain procurement to the cold-water baseline; keep water-heater choice decoupled and propane outdoor-only unless listed otherwise.

4. May 4 to May 6 (final pre-install readiness + travel/staging)
- Confirm delivered vs ordered critical-path items.
- Pack measurement, tailgate, seal/weather, electrical labeling, fuse, and fastener kits.
- Stage the truck near Bellingham by the evening of May 6. Do not start work that can leave the truck half-disassembled.

5. May 7 (install day)
- Confirm tailgate handling, bed rail/interface sealing, attachment method, and weather/dust expectations with Hiatus before work starts.
- Capture before/during/after photos and a full shell measurement set before leaving.
- Do not leave with undocumented attachment, clearance, or weather-critical issues.

6. May 8 to May 11 (local shakedown + service-map freeze)
- Stay local enough to return to Hiatus for early issues; run low-speed/highway shakedown and reinspect attachment/seals/doors/windows/fan.
- Freeze service map from real shell dimensions before penetrations, final cable cuts, Lonseal glue-down, or permanent module skins.
- Place top-off orders based on real measurements and update logs/tracking.

## Deferred / purchase-later rows (keep out of current critical path unless triggered)
- Optional 12V expansion path: row `118`.

## Critical hold points (do not skip)
- Hold 1: No penetrations until layout + service map is frozen from real installed camper measurements.
- Hold 2: No Lonseal glue-down, insulation, or panel closure until floor/rough-in/service-access gates pass.
- Hold 3: No final cabinetry close-out, drawer-slide lengths, or cosmetic skins until fridge/tank/electrical envelopes are verified.
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
- Update `docs/core/TRACKING.md` with sequence-related open risks after first dry-fit rehearsal.
- If date windows change, update this file and `docs/core/PROJECT.md` together so milestone language stays aligned.
- Keep `docs/implementation/FLOORING_subfloor_build_process.md` and `bom/bom_estimated_items.csv` in sync when flooring purchases or stack-up assumptions change.
