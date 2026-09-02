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

## Planning assumptions (as-of 2026-09-02)
- Hiatus install readiness/travel planning is historical; the real camper shell is available for physical measurements and mockups.
- The permanent floor and main electrical/Galley/Bench structure are installed. The `3x 48V` bank has been paralleled for an extended period, and the batteries plus ICECO are restrained. The rear driver-side storage module, Bench lid, monitor/laptop package, air-fryer home, other storage, and final skins remain.
- Starlink Standard 4 X, fridge, pump, three DC charging outlets, and the owner-described `12V`/`48V` systems are in regular use. All four duplex outlet boxes and remaining `120V` work are enclosed and in regular use, and the owner confirms the MultiPlus is grounded to the truck chassis. Specific verification of the installed MultiPlus `M6 PE` bond, separate conductive-shell bond, GFCI/polarity/neutral behavior, labeling, terminal-cover, and cable-support checks remain.
- All four Renogy `175W` panels have arrived. The PV pass-through, two-pole disconnect, stationary wiring, and MPPT landing are complete; no panels are connected. Keep one `4S1P` string on the existing Victron `150/45`; direct bonding still waits on exact roof preparation/caulk/cure proof.
- The LF Bros heater and rear storage module are one dependency package. The EVIL ENERGY `10 gal` diesel tank/feed package, final remote-fill/vent/isolation package, and CaLeQi `60 mm / 2.37 in` stainless floor turret are purchased. Turret-cut prep is complete: Lonseal waste is removed, the turret seats in the shallow recess, and the existing `1/2 in` template is the jigsaw riser. The turret cut may proceed after nearby `12V` battery/extrusion removal, actual blade-downstroke control, and its own underbody survey. Separately, exterior former-spare-tire mounting with the drafted `1010` / gusseted `2 x 2 in` angle cradle remains held for verified crossmember/frame hardpoints, load paths, and axle/tire travel before cradle fabrication or truck drilling.
- Fresh-water plumbing, KUS, and the `35 gal` tank are complete and have substantial owner-reported use. Final surfaces are a `48 in` live-edge Bubinga Galley and `47 in` live-edge Bubinga Desk; sink installation follows the mid-September routing work. The separate graywater system remains.
- Alternator charging and PV charging remain disabled. Alternator closeout is the protected PH-VAN red lead plus Wakespeed read/save/programming and controlled first charge. Solar closeout is roof prep/caulk/bond, series wiring, roof-side support, and controlled commissioning.
- HOTTAP receipt remains pending; propane geometry is mocked. The FLEXISPOT Foldex chair is ordered. Existing-camper shakedown is owner-reported good; each new subsystem still needs its own post-install check.
- Current dependency order is installed MultiPlus-ground verification plus separate shell bond/GFCI proof -> heater/storage/tank package -> mid-September Bubinga/sink -> graywater -> PH-VAN/Wakespeed first charge -> solar bond/wire/commission -> HOTTAP on receipt -> Bench lid/air fryer/monitor/laptop/storage -> final skins and subsystem shakedowns.
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

5. Current remaining-systems phase (updated `2026-09-02`)
- **Completed baseline:** permanent floor/main structure; operational Starlink, `12V`, `48V`, enclosed four-device `120V`, fresh plumbing/KUS/tank; paralleled and restrained batteries; restrained ICECO; completed PV pass-through/disconnect/fixed wiring/MPPT landing; successful existing-camper shakedown.
- **Electrical safety task:** the MultiPlus-to-truck-chassis ground is owner-confirmed installed. Verify its `M6 PE` origin, conductor/hardware, and chassis endpoint; close/verify the separate shell bond, then prove PE continuity, neutral isolation, polarity, and both GFCI chains. Finish the labeled removable DC switch face, terminal covers, cable support, and labels where still open.
- **Solar task:** no panels are connected. Verify final panel placement and exact roof preparation/caulk/cure, then bond and series-wire `4S1P`, structurally support the roof-side/moving lead, and commission through the completed pass-through/disconnect/MPPT path.
- **Heater/storage task:** inventory and dry-fit the purchased `10 gal` diesel tank/feed plus final remote-fill/vent/isolation package with the heater, sealed turret, underbody exhaust/intake/fuel route, pump, and rear storage module. First identify verified former-spare-tire crossmember/frame attachment points for the drafted `1010` / gusseted-angle cradle. Heat shield is supplemental; no drilling before the vehicle-line/undercoating/combustible survey, axle/tire travel check, complete filler/vent route, and approximately `86 lb` full-tank restraint pass.
- **Bubinga/water task:** bring the real sink and soap dispenser to the mid-September work on the `48 in` Galley and `47 in` Desk pieces. Fresh water is complete; prove only the new sink support/drain geometry and continuous slope into the selected never-fueled LF Bros `10 L` gray tank.
- **Alternator task:** install the protected PH-VAN red lead, read/save/program the WS500, and complete the detailed preflight before controlled first charge.
- **Closure task:** install rear storage only after heater/fuel geometry; accept the ordered chair against the real Desk/aisle; build and restrain the air fryer, Bench lid, monitor/laptop, and storage; panel last. Mount/commission HOTTAP only after receipt and physical clearance proof.
- Failed electrical tests, unsafe heater geometry, leaking wet assembly, inadequate road restraint, or blocked service access pauses its dependent step rather than being worked around permanently.

## Deferred / purchase-later rows (keep out of current critical path unless triggered)
- No additional `48V->12V` converter is active; inactive row `118` is retired under the Orion plus `12V` buffer-battery architecture. Reopen only from measured sustained-load evidence.

## Critical hold points (do not skip)
- Hold 1 (closed/historical): the #650 cure/heavy-loading gate has passed and modules are installed. Protect Lonseal and investigate only actual loose/expanding areas, moisture/dust evidence, insert spin, or floor movement.
- Hold 2 (fresh water closed): KUS, tank, fill/vent, pump, accumulator, PEX, and rear service ports are in regular use. Leak-check only new/disturbed sink joints and spill-test the separate graywater system.
- Hold 3 (bank staging closed; access remains): the `3x 48V` bank and ICECO are restrained. Bench-lid/storage work may proceed only while preserving battery extraction, covers, branch protection, and emergency fuse/disconnect access.
- Hold 4 (AC enclosures and MultiPlus chassis ground installed; verification/shell bond open): all four outlet boxes and remaining `120V` work are enclosed and in regular use, and the MultiPlus is owner-confirmed grounded to truck chassis. Verify that installed bond, close/verify the separate shell bond, and complete PE continuity, neutral isolation, polarity, and GFCI proof.
- Hold 5 (sink/graywater only): no final sink cut until the actual fixture/support/drain clearances pass; do not reopen completed fresh-water service.
- Hold 6: No final cabinetry/panel closeout until fridge/tank/electrical envelopes and service access pass installed functional tests.
- Hold 7: Existing-camper shakedown is good. Each newly installed air fryer, Bench lid, monitor/laptop package, storage item, solar array, heater/fuel system, HOTTAP, counter/sink/graywater, and alternator path needs its own retention/inspection/commissioning gate before reliance.
- Hold 8: Final skins wait until the affected heater, drain, electrical, leak, and service-access tests are complete.

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
