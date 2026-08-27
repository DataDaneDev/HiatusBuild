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

## Planning assumptions (as-of 2026-08-27)
- Hiatus install readiness/travel planning is historical; the real camper shell is available for physical measurements and mockups.
- The permanent floor and main electrical/Galley/Bench structure are installed. The rear driver-side storage module, bench lid, desk/monitor package, air-fryer home, graywater route, and final skins remain.
- Starlink Standard 4 X is working from its installed switched direct-DC route. The fridge and pump are wired and switched; the three separately fused DC charging outlets and four duplex AC devices are physically installed. This is physical progress, not blanket functional proof: labeling, terminal protection, AC/DC branch tests, road restraint, and final covers remain.
- All four Renogy `175W` panels have arrived; one-panel physical test-fit plus measured layout indicates the roof package fits, direct bonding waits on exact silicone/cure proof, and the PV retractile cord is ordered. Keep one `4S1P` string on the existing Victron `150/45`.
- The LF Bros heater and rear storage module are one dependency package. Do not install the module or drill the heater turret until the complete underside exhaust/intake/fuel route, truck fuel tank/vehicle-line clearances, and compliant exterior or sealed/vented fuel containment are proven.
- Black-walnut sink/counter/desk routing is planned for mid-September. Bring the actual sink and soap dispenser; prove support, drain, tank, service, and continuous-slope graywater geometry before cutting.
- Current dependency order is switch/service safety -> DC/AC branch closeout -> solar weather-window/cord proof -> heater/storage dry layout -> mid-September walnut/sink routing -> graywater mockup -> alternator `F-04`/sensor/WS500 commissioning -> storage/real-chair/desk mockup -> appliance/bench/monitor travel restraint -> final skins -> shakedown.
- Interior/furniture assumptions in `docs/implementation/INTERIOR_furniture_layout_and_galley.md` remain the current baseline. Preserve the roughly `24 in` desk until the real chair/aisle test; lighting and audio remain deferred behind core systems and restraint.
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

5. Current working-utility integration phase (updated `2026-08-27`)
- **Completed physical gates:** permanent floor and main structure; installed Starlink pass-through/retractile with working switched `12V` conversion; wired/switched fridge and pump; three separately fused DC charging outlets; four wired duplex AC devices; four solar panels received, with one-panel physical fit plus measured layout indicating package fit.
- **First task:** hard-mount the hanging switches on one labeled removable service face, with AC in a separate listed covered box and no loose tape as the terminal barrier. Then close out actual fuse/slot/polarity/load/drop and four-device AC/GFCI tests.
- **Solar task:** verify received labels/connectors and exact silicone/cure; clean the roof; prove one panel before all four. On cord receipt, verify ratings/OD/gland/tangents/force/full motion; preserve only two `4S1P` string-end leads into the two-conductor cord/disconnect/MPPT route and use structural exterior clamps.
- **Heater/storage task:** dry-fit heater, sealed turret, underbody exhaust/intake/fuel route, fuel containment, pump, and rear storage module together. Heat shield is supplemental; no drilling before the complete truck fuel tank/vehicle-line/undercoating/combustible survey passes.
- **Walnut/water task:** bring the real sink and soap dispenser to the mid-September appointment. Prove bowl/drain/faucet/soap/support/tank/service geometry and continuous slope; mock a vented, positively retained, normally closed removable graywater vessel around `2.5 gal` before locking the design.
- **Alternator task:** complete `F-04 200A/80V`, both temperature sensors, support/protection, and WS500 read/save/program before controlled first charge.
- **Closure task:** install rear storage only after heater/fuel geometry; mock real chair and `24 in` desk before trimming; add positive travel restraint for batteries, ICECO, air fryer, bench lid, monitor, and laptop; panel last.
- Failed electrical tests, unsafe heater geometry, leaking wet assembly, inadequate road restraint, or blocked service access pauses its dependent step rather than being worked around permanently.

## Deferred / purchase-later rows (keep out of current critical path unless triggered)
- No additional `48V->12V` converter is active; inactive row `118` is retired under the Orion plus `12V` buffer-battery architecture. Reopen only from measured sustained-load evidence.

## Critical hold points (do not skip)
- Hold 1 (closed/historical): the #650 cure/heavy-loading gate has passed and modules are installed. Protect Lonseal and investigate only actual loose/expanding areas, moisture/dust evidence, insert spin, or floor movement.
- Hold 2 (tank physically installed; water service still held): the KUS replacement under-ring/gasket/hardware are installed. Keep sender access open until fill/vent, sink/drain completion, and one dry pressure/dwell proof show no leakage or unexplained pump cycling.
- Hold 3: No battery-bench bridge/lid or service-obscuring frame until the `3x 48V` bank is restrained, individually protected/connected as designed, covered, labeled, and removable with emergency fuse/disconnect access preserved.
- Hold 4 (shell cut closed `2026-08-02`): No energization through the installed shore inlet until the remaining `L/N/PE` splice is enclosed/strain-relieved and dead checks prove the locked breaker path, polarity, PE continuity, AC-in/AC-out neutral isolation, and no unintended neutral-ground bond.
- Hold 5 (shell cuts closed `2026-08-02`): No water-service acceptance until the installed KUS rebuild, fill/vent hose geometry, sink termination, spill/overflow path, and final dry pressure/dwell inspection pass.
- Hold 6: No final cabinetry/panel closeout until fridge/tank/electrical envelopes and service access pass installed functional tests.
- Hold 7: Integrated electrical/Bench/Galley anti-rack structure is complete; no road travel until batteries, ICECO, air fryer, bench lid, monitor/laptop hardware, every other heavy/rigid cargo item, and the remaining terminal/cable protections have positive restraint, torque/witness marks where applicable, and inspection.
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
