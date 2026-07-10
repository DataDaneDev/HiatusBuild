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

## Planning assumptions (as-of 2026-07-10)
- Hiatus install readiness/travel planning is historical; the real camper shell is available for physical measurements and mockups.
- Major Galley/Bench/Electrical/Desk modules have been test-fit as one system. The active critical path has shifted from module fabrication to a deliberate floor teardown, aluminum-compatible hardpoint, substrate, and reinstall gate.
- The `2021 F-350` pickup box is aluminum. Direct box attachments must follow Ford SVE `Q-222R1`; on-hand steel rivet nuts and stainless fasteners are not valid bed hardpoints.
- Electrical architecture and BOM assumptions in `docs/core/SYSTEMS.md` remain the active baseline, with the first live `48V`/MultiPlus/Cerbo/shore checkpoint passed. Do not drill around connected/live electrical equipment and do not road-travel until final restraint/access gates pass.
- The current three-piece single-layer `3/4 in` plywood is below Lonseal's published two-layer `7/8 in` wood-substrate minimum. Glue-down waits for a `1/4 in` underlayment clearance mockup or written Lonseal acceptance of the exact vehicle substrate.
- Interior/furniture assumptions in `docs/implementation/INTERIOR_furniture_layout_and_galley.md` remain the current baseline. Black-walnut finish surfaces stay template-gated; lighting remains deferred behind core flooring, furniture, plumbing, and electrical integration.
- Active post-install tracker: `docs/plans/LIVE_BUILD_CHECKLIST.md`. Update it whenever practical sequence, blockers, or completed physical work changes.

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

5. Current flooring-foundation phase (updated `2026-07-10`)
- Major modules are test-fit well enough to preserve their real geometry. Finish only the remaining Desk/storage corrections required to trust final feet/tabs, then record centers from physical modules before teardown.
- Do not final-drill the bed around connected/live electrical equipment. Isolate/remove loose batteries, transfer real tab centers, remove modules, then drill/set/test in a clean de-energized work area.
- Classify every floor attachment: independent subfloor retention, ordinary cabinetry, or heavy-system restraint. Battery bench/electrical/full-tank restraint needs distributed/redundant load paths; do not assume thin aluminum pickup-box sheet inserts are crash-rated.
- Clean/map the exposed bed; distinguish abandoned holes from seams and factory drains/weep paths. Gorilla tape is for compatible discrete hole patches only, not seams. Pass a controlled low-flow ingress test before floor closure.
- Correct hardpoint materials for the aluminum pickup box before drilling: measured-grip aluminum rivet nuts/Plusnuts, Ford-compatible coated bolts/aluminum washers/isolators, restored edge corrosion protection, and no stainless or standard steel rivet nuts in direct box attachment.
- Resolve the Lonseal substrate gate before glue. Preferred path is a staggered `1/4 in` APA underlayment over the three `3/4 in` base panels if the `0.250 in` height increase passes physical clearance; otherwise obtain written Lonseal acceptance of the exact single-layer vehicle substrate.
- After hardpoints, independent floor retention, substrate, drainage, and full module refit pass, dry-fit/install Lonseal with the published #650 temperature/mix/working/rolling/cure process. Reinstall modules only after the full `72 h` cure.
- Continue using physical module envelopes to control later furniture/panel decisions; keep final walnut, wiring, plumbing, and cosmetic closeout downstream of the floor foundation gate.

## Deferred / purchase-later rows (keep out of current critical path unless triggered)
- Optional 12V expansion path: row `118`.

## Critical hold points (do not skip)
- Hold 1: No final penetrations until the layout/service map and the underside/no-drill check are frozen from physical modules.
- Hold 2: No pickup-box hardpoint drilling until the aluminum-compatible insert/fastener/isolation/coating stack and matched-gauge installation test pass.
- Hold 3: No Lonseal glue-down until moisture/drainage, independent floor retention, substrate compliance, hardpoint registration, and #650 workflow gates pass.
- Hold 4: No final cabinetry/panel closeout until fridge/tank/electrical envelopes and service access remain valid after the final floor stack.
- Hold 5: No road travel with the electrical/heavy modules until integrated anti-rack and redundant restraint paths are complete, torqued, witness-marked, and inspected.
- Hold 6: No field deployment until the low-consequence shakedown defects and post-drive fastener/moisture inspection are closed.

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
