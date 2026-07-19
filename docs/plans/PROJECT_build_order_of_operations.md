---
aliases:
  - Hiatus build order
tags:
  - hiatus/plan
  - hiatus/build-order
status: active
related:
  - "[[PROJECT]]"
  - "[[PROCUREMENT_purchase_list_2026-05-26]]"
  - "[[TNUTZ_80_20_HARDWARE_MODEL_2026-06-01]]"
  - "[[SYSTEMS]]"
---

# Build Order of Operations (Truck Bed Camper)

## Purpose
- Define a practical order of operations that still supports parallel workstreams.
- Prioritize measured, reversible post-install module work: validate real camper envelopes first, then build systems and furniture modules without burying service access.

## Planning assumptions (as-of 2026-07-19)
- Hiatus install readiness/travel planning is historical; the real camper shell is available for physical measurements and mockups.
- Major Galley/Bench/Electrical/Desk modules have been test-fit as one system, removed, and preserved for reinstall.
- The one-piece Lonseal was glued to the three-piece `3/4 in` plywood floor on the evening of `2026-07-15`. The floor is permanent, controlled module loading has begun, and routine removal of the three plywood pieces is no longer possible without cutting the vinyl at both seams.
- The electrical module is now hard-mounted through the finished floor to truck-bed hardpoints. MultiPlus/AC-panel remount, final Bench anti-rack tie-in, full-bank commissioning, and service/road-restraint checks remain open.
- Electrical architecture and BOM assumptions in `docs/core/SYSTEMS.md` remain the active baseline, with the first live `48V`/MultiPlus/Cerbo/shore checkpoint passed. Do not drill around connected/live electrical equipment and do not road-travel until final restraint/access gates pass.
- The active dependency order is MultiPlus/AC-panel remount -> shore inlet/AC-in -> open-access `3x 48V` bank matching/commissioning -> `12V`/Orion closeout -> tank/pump bench test -> tank/restraint/wet spine/Galley installation -> Bench tie-in and closure. The water-fill penetration still follows its physically proven inside endpoint.
- Interior/furniture assumptions in `docs/implementation/INTERIOR_furniture_layout_and_galley.md` remain the current baseline. Black-walnut finish surfaces stay template-gated; lighting remains deferred behind core flooring, furniture, plumbing, and electrical integration.
- Active post-install tracker: `docs/plans/LIVE_BUILD_CHECKLIST.md`. Update it whenever practical sequence, blockers, or completed physical work changes.

## Generic full-build sequence (reference only)

The current build has already completed the floor step out of this generic order. Use the dated current-phase sequence below when it conflicts with this reference.
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
- Use `docs/implementation/INTERIOR_furniture_layout_and_galley.md` as the current furniture/galley concept checkpoint; keep the generated diagrams conceptual until post-install measurements prove the envelopes.
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

## Date-window execution plan (install window history + current restart)
1. May 2 to May 4 (completed heavy truck prep)
- Bed/flooring removed from travel/build path; Washington trip should remain mostly empty-bed.
- Bed rail caps were removed; most clips broke; caps were reinstalled with a large Loctite polyurethane bead underneath.
- Small drill holes and minor bed openings were sealed with Gorilla Waterproof Patch & Seal Tape; selected corner air gaps received small polyurethane beads.
- Exact-notch Lonseal trowel was purchased; roller/rolling method still needs confirmation before glue-down.
- Do not reinstall final floor or glue Lonseal before post-install ordinary inspection.

2. May 5 to May 6 (Washington travel/staging)
- Use May 5-6 for travel, route/weather/lodging confirmation, cure inspection, packing, and appointment confirmation.
- Keep batteries/electrical cabinet parts home unless Hiatus explicitly requests them.
- Stage near Bellingham by the evening before the May 7 appointment; do not start work that can leave the truck half-disassembled.

3. May 7 (install day)
- Confirm tailgate handling, tonneau timing, bed rail/interface sealing, attachment method, and weather/dust expectations with Hiatus before work starts.
- Have Hiatus inspect/accept the re-bonded rail caps and any prior rail-hole areas that interact with the camper interface.
- Capture before/during/after photos and a full shell measurement set before leaving.
- Do not leave with undocumented attachment, clearance, or weather-critical issues.

4. May 8 to May 11 (local shakedown + service-map freeze)
- Stay local enough to return to Hiatus for early issues if practical; run low-speed/highway shakedown and reinspect attachment/seals/doors/windows/fan.
- Observe dust/water paths, rattles, condensation behavior, barn-door seal behavior, and any bed rail cap movement.
- Freeze service map from real shell dimensions before penetrations, final cable cuts, Lonseal glue-down, or permanent module skins.
- Place top-off orders based on real measurements and update logs/tracking.

5. Current electrical-to-wet-spine integration phase (updated `2026-07-19`)
- **Completed physical gate:** permanent floor is carrying controlled work; electrical module is hard-mounted and all three battery branch harnesses are cut, lugged, heat-shrunk, and landed at the battery-side busbars.
- **Next electrical session:** remount MultiPlus/AC enclosure, prove/cut/seal the shore inlet and `10/3` route, then charge Batteries 2 and 3 individually. After rest, parallel all three only at `<=0.1V` difference and complete polarity/protection/SmartShunt/current-sharing checks.
- **Parallel `12V` closeout:** locate/install final `F-06 20A/80V`, complete `F-11 -> SW-12V-BATT -> panel`, verify `F-07`, then prove factory pod lights, Maxxair fan, and the first two DC outlets.
- **After-return plumbing session:** with the remaining fittings in hand, assemble and fill/pressure/leak/function-test the tank, KUS sender, pump, strainer, accumulator, manifold, fill/vent, and drain in the driveway before permanent mounting.
- **Installed closeout:** hard-mount tank/restraint/wet spine and Galley; add the Bench/electrical anti-rack tie-in; keep panels removable until AC/DC and plumbing tests pass; then torque/witness-mark and run a local shakedown.
- Missing fittings, failed voltage matching, an unsafe shore route, or a leaking bench assembly pauses its dependent step rather than being worked around permanently.

## Deferred / purchase-later rows (keep out of current critical path unless triggered)
- Optional 12V expansion path: row `118`.

## Critical hold points (do not skip)
- Hold 1: No heavy module/furniture loading until `72 hr` after actual #650 completion and the post-cure floor/hardpoint inspection passes.
- Hold 2: No tank sender/fill/vent hole until the empty tank has a complete port map and has passed one bare in-truck dry fit against wheel well, extrusion, hose bends, service access, and restraint.
- Hold 3: No battery-bench bridge/lid or service-obscuring frame until the `3x 48V` bank is restrained, individually protected/connected as designed, covered, labeled, and removable with emergency fuse/disconnect access preserved.
- Hold 4: No shore inlet cut until the hard-mounted electrical module, AC-in enclosure endpoint, inside cable path, backing, bend radius, strain relief, and exterior location are proven together.
- Hold 5: No water-fill/vent exterior cut until the final tank orientation, fill port, highest-point vent port, continuous hose fall/vent rise, service access, and spill/overflow path are proven together.
- Hold 6: No final cabinetry/panel closeout until fridge/tank/electrical envelopes and service access pass installed functional tests.
- Hold 7: No road travel with the electrical/heavy modules until integrated anti-rack and restraint paths are complete, torqued, witness-marked, and inspected.
- Hold 8: No field deployment until the low-consequence shakedown defects and post-drive floor/fastener/moisture/leak inspection are closed.

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
- Keep `docs/implementation/INTERIOR_furniture_layout_and_galley.md`, `docs/implementation/INTERIOR_driver_side_workstation.md`, and `docs/core/SYSTEMS.md` synchronized when the shell measurements change furniture, plumbing, or roof-safe monitor assumptions.
