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

## Planning assumptions (as-of 2026-06-27)
- Hiatus install readiness/travel planning is historical; the real camper shell is available for physical measurements and mockups.
- This plan assumes a post-install interior buildout with reversible/module-first work until service maps, penetrations, and access gates pass.
- Electrical architecture and BOM assumptions in `docs/core/SYSTEMS.md` remain the active baseline, with the first live `48V`/MultiPlus/Cerbo/shore checkpoint passed and the electrical backer now trimmed/inset into its `80/20` frame.
- Current electrical-module state: component placement has been adjusted for real MultiPlus depth, the module is freestanding and ready to tie into the bench/desk structure, but it is not road-ready as a standalone module because it still needs bench/desk/galley tie-in, panels/anti-rack restraint, hardpoint verification, and final fastener/strain-relief closeout.
- Interior/furniture assumptions in `docs/implementation/INTERIOR_furniture_layout_and_galley.md` remain the current draft baseline. The active sequence is now integrated module buildout: bench first, desk desktop/workstation support next, then galley/wet-spine counter/appliance module with the purchased sink/faucet, induction cooktop, and Ninja SP151 cubby. TNUTZ cart consolidation lives in `docs/plans/TNUTZ_80_20_HARDWARE_MODEL_2026-06-01.md`; procurement summary lives in `docs/plans/PROCUREMENT_purchase_list_2026-05-26.md`; lighting remains deferred behind core furniture/plumbing/electrical integration.

- Active post-install sprint/punch-list tracker: `docs/plans/LIVE_BUILD_CHECKLIST.md`. Update it whenever the practical next steps, blockers, or completed build work changes.

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

5. Current module-integration phase (updated `2026-06-27`)
- Owner status: the electrical backer has been trimmed so it insets cleanly into the `80/20` electrical frame. Minor component shifts were made after real MultiPlus depth proved deeper than earlier assumptions; these are mechanical packaging changes, not an electrical architecture change.
- The electrical module is now freestanding and ready to tie into the bench/desk structure. Treat the freestanding state as a shop-fit milestone only; do not drive with it loose or lightly anchored because it is still too wobbly without bench/desk/galley tie-in, panels/anti-rack restraint, and final hardpoint verification.
- Immediate build sequence: build the bench/battery/step structure first so it braces the electrical module and preserves battery/service access; fit the desk desktop/workstation support next; then build the galley/wet-spine counter/appliance module.
- Galley scope now has real purchased fixtures/appliances to package: Sarlai topmount sink, FORIOUS faucet, Duxtop induction cooktop, and Ninja SP151 air-fryer/toaster-oven cubby. Validate sink cutout/faucet clearance/drain path and appliance heat/retention before permanent panels.
- Continue using available `10-series`/`2010` stock, regular angle, and on-hand connector hardware as build/prototype stock; use the pending 80/20 nut/hardware shipment for final seams, serviceable fasteners, and hardware standardization rather than letting missing hardware stall module fitting.
- Sheet-vinyl/Lonseal remains intentionally unglued to avoid damage and preserve access while rough-in/interior buildout decisions are still open. Sheet-vinyl installation is a late finish-floor step after interior buildout/service-access gates, not a near-term blocker.
- Hold glue-down until the floor/rough-in gate passes: no pending floor penetrations, hardpoint pockets verified, EPS/subfloor sitting flush, and adhesive/roller method confirmed.
- Build the 80/20/furniture list from physical module envelopes first: classify each member as structural, panel support, service-access edge, or locator/anti-rattle, then use the consolidated TNUTZ WIP cart/visual aids before final vendor-cut lengths.

## Deferred / purchase-later rows (keep out of current critical path unless triggered)
- Optional 12V expansion path: row `118`.

## Critical hold points (do not skip)
- Hold 1: No penetrations until layout + service map is frozen from real installed camper measurements.
- Hold 2: No Lonseal glue-down, insulation, or panel closure until floor/rough-in/service-access gates pass.
- Hold 3: No final cabinetry close-out, drawer-slide lengths, or cosmetic skins until fridge/tank/electrical envelopes are verified.
- Hold 4: No road travel with the freestanding electrical module until it is tied into the bench/desk/galley structure, anti-rack restraint/panels are installed, hardpoints are verified, and fasteners are witness-marked.
- Hold 5: No field deployment until shakedown defects are triaged.

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
