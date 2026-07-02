---
aliases:
  - Hiatus live build checklist
  - July 4 build sprint checklist
  - Camper build running checklist
tags:
  - hiatus/plan
  - hiatus/checklist
  - hiatus/july4-sprint
status: active
related:
  - "[[PROJECT_build_order_of_operations]]"
  - "[[INTERIOR_furniture_layout_and_galley]]"
  - "[[INTERIOR_driver_side_workstation]]"
  - "[[FLOORING_subfloor_build_process]]"
  - "[[ELECTRICAL_Mechman_WS500_APM48_install_guide]]"
  - "[[SYSTEMS]]"
  - "[[TRACKING]]"
---

# Live Build Checklist — July 4 Sprint + Running Build Tracker

As-of: `2026-07-02`

Owner: Sunny / Dane

Maintainer rule: **update this file whenever the practical build state, sequence, blocker list, or next physical step changes.** Keep it as the live punch list; do not let stale chat notes become the checklist of record.

## Purpose

This is the active running checklist for the post-install Hiatus/F-350 camper build, with a fast-but-realistic July 4 long-weekend push. It translates the canonical build sequence into shop actions, physical gates, and test checkpoints.

It does **not** replace the owner docs:

- Overall sequence: `docs/plans/PROJECT_build_order_of_operations.md`
- Interior/galley baseline: `docs/implementation/INTERIOR_furniture_layout_and_galley.md`
- Workstation/monitor detail: `docs/implementation/INTERIOR_driver_side_workstation.md`
- Flooring/Lonseal gate: `docs/implementation/FLOORING_subfloor_build_process.md`
- Alternator install/commissioning: `docs/implementation/ELECTRICAL_Mechman_WS500_APM48_install_guide.md`
- Decisions/risks/open questions: `docs/core/TRACKING.md`

## Current build posture

- Electrical module is live-proven at the bench/system level but still not road-ready as a freestanding structure.
- Immediate physical priority is integrated structure: **bench/battery/step first, desk/workstation second, galley/wet-spine third**.
- Lonseal glue-down is intentionally late. Do not glue until hardpoints, rough-in, floor penetrations, moisture paths, and service access are proven.
- Alternator charging remains a separate commissioning gate. Mechanical/staged wiring is OK only if the alternator cannot charge into an incomplete or unsafe path.
- Solar research/procurement is deferred until shore + alternator + roof/module constraints are better proven.

## July 4 sprint strategy

### Definition of a successful long weekend

A realistic win is **not** a finished camper. A realistic win is:

1. Bench/battery/step structure rigid enough to brace the electrical module.
2. Desk frame/top physically placed enough to prove work geometry and electrical service access.
3. Galley/fridge/wet-spine skeleton started enough to become the datum for cooler/fridge/plumbing fitment.
4. Remaining batteries charged and staged safely.
5. Electrical module moved from “works on bench” toward “mechanically restrained system,” with wiring/strain-relief/test gates defined.
6. No irreversible finish work done before the underlying gates pass.

### Time-boxed sprint timeline

| Window | Primary objective | Realistic output | Do not get sucked into |
| --- | --- | --- | --- |
| Thu night `2026-07-02` | Reset, inventory, mark cuts, stage batteries | clean shop list, charged/charging batteries, labeled cut piles | truck-bed Tetris, final cooler decision |
| Fri `2026-07-03` | Bench/battery/step module | structural frame dry-fit, battery extraction path, electrical tie-in points | panels/skins, perfect cosmetics |
| Sat `2026-07-04` | Desk/workstation + electrical module restraint | desk top/frame located, electrical module braced, service access checked | monitor mechanism rabbit hole before roof/desk geometry works |
| Sun `2026-07-05` | Galley/fridge/wet-spine skeleton | galley/cooler/fridge datum built, sink/faucet/appliance envelopes checked | permanent plumbing closeout, final countertops |
| Mon `2026-07-06` if available | Wire/strain-relief/test + punch-list | safe low-power tests, AC/GFCI if ready, updated blocker list | alternator first-charge unless every prerequisite is green |
| Week after | Alternator rough-in/commissioning, plumbing pressure test, floor gate | controlled subsystem tests | Lonseal glue-down before hardpoints/penetrations are proven |

## Status legend

- `[ ]` open
- `[~]` in progress / partially complete
- `[x]` complete
- `[HOLD]` blocked by a gate or prerequisite
- `[DEFER]` intentionally later

---

# Master checklist

## 0. Reset, inventory, and sprint control

- [ ] Photograph/current-state pass before moving major parts.
- [ ] Clear a safe walking/cutting path in the shop/truck bed.
- [ ] Put all extrusion/offcut stock in one visible staging area.
- [ ] Mark the known latest cutlist workbook as the current source: `docs/plans/assets/module-cutlists/2026-06-25_module-cutlist-and-assignments.xlsx`.
- [ ] Preserve the Bench one-off updates in the workbook; do not overwrite the local working copy blindly from `HEAD`.
- [ ] Make three physical piles: `Bench`, `Desk`, `Galley candidate`.
- [ ] Label every cut extrusion with module + length + workbook/source row if known.
- [ ] Separate hardware by class: T-nuts, angle brackets, corner cubes, panel fasteners, bolts/washers, latch hardware.
- [ ] Identify missing hardware that blocks final travel-tight assembly vs hardware that only blocks cosmetics.
- [ ] Stage fire extinguisher, first-aid, insulated tools, multimeter, crimper, heat shrink, labels, paint pen/witness marker.
- [ ] Start a paper/shop whiteboard punch list for anything discovered physically; sync durable items back here.

## 1. Battery charging and staging

Goal: all batteries charged, known, and safe before final wiring/tests.

- [ ] Confirm the currently charged battery count and SOC/voltage.
- [ ] Charge the other `3 of 4` batteries as applicable, including the `12V` battery.
- [ ] For each `48V` battery, record resting voltage and display SOC after charge/rest.
- [ ] For the `12V` battery, record resting voltage and display SOC after charge/rest.
- [ ] Confirm all batteries are above low-temperature charge cutoff before charging.
- [ ] Confirm no battery is in BMS protection state.
- [ ] Confirm battery terminals are covered while batteries are staged loose.
- [ ] Confirm each 48V battery has its intended Class T/fuse/disconnect path before being paralleled into service.
- [ ] Confirm battery extraction path from the bench: no rail, lid, panel, or cable blocks removal.
- [ ] Add temporary “charged / not charged / do not connect” labels if any battery is out of sync.

## 2. Bench / battery / step module

Goal: build the structure that braces the electrical module and controls battery mass.

- [ ] Reconfirm bench footprint inside truck against real shell/wheel-well/electrical-module position.
- [ ] Verify battery orientation, terminal reach, and removal direction.
- [ ] Confirm bench height target against cabover entry/step use and cushion stack.
- [ ] Cut/identify all bench extrusion members.
- [ ] Dry-fit the bench frame square on the floor.
- [ ] Add crossmembers/diagonal/panel planes that prevent racking.
- [ ] Confirm battery bay is separated from ordinary storage.
- [ ] Add a flat divider board above battery service volume.
- [ ] Decide lid style: hinged with stay vs removable retained panel; avoid loose projectile panels.
- [ ] Add battery restraints: strap bars, capture rails, hold-downs, or framed pockets.
- [ ] Confirm Class T / disconnect / Lynx / shunt / fuse access does not require dismantling the bench.
- [ ] Confirm emergency service slit/access door for disconnect/fuse inspection.
- [ ] Add edge protection/scuff plate where the bench doubles as a step.
- [ ] Mark fasteners for final witness marks after retorque, not during first loose mockup.
- [ ] Do not install final skins until electrical service and battery extraction pass.

## 3. Electrical module mechanical integration

Goal: turn the freestanding live-proven electrical module into a restrained mobile module.

- [ ] Place electrical module against the bench/desk structure in its intended installed position.
- [ ] Confirm MultiPlus depth and service clearance are still acceptable.
- [ ] Confirm Cerbo, SmartShunt, Orion, Lynx, fuses, disconnects, and AC enclosure remain reachable.
- [ ] Add bench/desk tie-in rails or brackets so the electrical module cannot wobble standalone.
- [ ] Add anti-rack planes: removable panels, diagonal braces, or shear skins where useful.
- [ ] Verify hardpoint locations for module restraint before any final floor holes.
- [ ] Add grommets/edge trim where cables pass through plywood or extrusion edges.
- [ ] Add J-clamps/P-clamps/strain relief for high-current, AC, DC, and data cables.
- [ ] Separate AC, DC high-current, low-voltage DC, data, and audio where practical.
- [ ] Cover/boot all exposed positive studs and high-current terminals.
- [ ] Add labels to fuses, disconnects, AC branches, 12V junction, and key service wires.
- [ ] Add a visible “48V isolated / live” indicator flag or label near the service access point.
- [ ] Confirm there is no path for loose storage to contact electrical hardware.
- [ ] Paint-pen witness marks after final torque/retorque, not before final position is set.
- [ ] [HOLD] Do not road-travel with the module freestanding or lightly attached.

## 4. Desk / workstation module

Goal: prove full-time work geometry before building clever monitor mechanisms or skins.

- [ ] Reconfirm driver-side desk footprint near wheel well; current target remains roughly `24 in x 48 in` until measured fit says otherwise.
- [ ] Mock chair/stool position and seated elbow height.
- [ ] Check knee/foot clearance around wheel well and electrical step projection.
- [ ] Place rough desktop or template at target height.
- [ ] Confirm entry/exit movement and hip/shoulder clearance.
- [ ] Confirm roof-down sweep envelope for desk, DC shelf, monitor stow block, and cable loops.
- [ ] Decide desktop material for MVP: plywood/laminated birch now; phenolic/Richlite later only if worth it.
- [ ] Build lower desk frame tied into the electrical/bench spine.
- [ ] Add shallow DC electronics shelf/box only if it does not block service access or entry movement.
- [ ] Reserve ventilated cubby space for laptop dock, router/Starlink power, USB-C PD, and monitor brick.
- [ ] Add temporary outlet/USB access position for seated testing.
- [ ] Keep front desk edge rounded or clipped enough to avoid hip strikes.
- [ ] Do a real seated test: keyboard, mouse, laptop, monitor placeholder, outlet reach.
- [ ] Do not build deep drawers into knee space.

## 5. Monitor / laptop stand / office gear retention

Goal: secure the office without turning it into roof-close or travel cargo risk.

- [ ] Decide MVP monitor approach for the weekend: temporary stow-safe mount vs final rising mechanism.
- [ ] Measure actual monitor + VESA arm + cable loop envelope.
- [ ] Build or mock a face-down/low stow cradle at or below roof-safe height.
- [ ] Add hard stops so monitor load does not sit on LCD surface.
- [ ] Add positive travel latch/pin for monitor carriage/angle/stow state.
- [ ] Add laptop stand/sleeve with ventilation and travel retention.
- [ ] Add cable chain or controlled service loop; no cable loop can stand proud into roof path.
- [ ] Add quick disconnect or service slack so monitor/laptop hardware can be removed.
- [ ] Create a visible roof/drive checklist near the door: monitor down, cable flat, shelf latched, panels closed.
- [ ] [HOLD] Do not finalize monitor mechanism until roof sweep and seated desk test pass.

## 6. Galley / fridge / cooler / wet-spine skeleton

Goal: build the galley datum so cooler/fridge/plumbing fitment stops being guesswork.

- [ ] Extract and label the galley candidate cuts from the current workbook/unassigned pool.
- [ ] Identify all non-Bench, non-Electrical pieces that may belong to galley/fridge/wet-spine.
- [ ] Mock passenger-side fridge/cooler position with real handles, hinge/lid swing, cord bend, and hand clearance.
- [ ] Confirm raised fridge/cooler height target, currently about `16 in` above floor/service zone.
- [ ] Confirm relationship to `36 gal` wheel-well tank envelope.
- [ ] Build the lofted fridge/cooler support skeleton as a service exoskeleton, not a sealed cabinet.
- [ ] Add positive fridge/cooler travel restraint and hard stops.
- [ ] Preserve lower cool-air intake and upper warm-air exhaust around fridge compressor vents.
- [ ] Confirm pump/accumulator/strainer/manifold service opening below/near fridge.
- [ ] Confirm wet bay cannot leak into battery/electrical bays; add partition/drip tray concept.
- [ ] Place Sarlai `15 in x 15 in` topmount sink template on galley counter area.
- [ ] Check faucet shank/nut/hose clearance under the counter.
- [ ] Check sink drain/graywater cassette path.
- [ ] Check Duxtop induction cooktop storage/use position and cord route.
- [ ] Check Ninja SP151 cubby: heat clearance, crumb access, plug path, travel restraint.
- [ ] Add removable service-panel edges into the skeleton while framing.
- [ ] [HOLD] Do not cut final countertop sink opening until skeleton and faucet/drain clearance are physically confirmed.

## 7. Plumbing rough-in and test

Goal: cold-water-first, hot-ready later, serviceable and leak-testable.

- [ ] Confirm fresh tank position, fill path, vent path, and outlet orientation.
- [ ] Confirm vent hose size for the gravity-fill vent nipple: preferred `10 mm ID`; `3/8 in ID` warmed/clamped fallback.
- [ ] Build wet-spine service board/tray layout: tank shutoff, flex loop, strainer, pump, accumulator, pressure gauge, manifold.
- [ ] Include winterization pickup, blowout Schrader, and low-point drains if practical in MVP.
- [ ] Add unions/quick disconnects so the pump/strainer can be serviced without dismantling furniture.
- [ ] Add pump electrical connector and strain relief.
- [ ] Add shallow removable leak tray/pan under pump/strainer/accumulator area.
- [ ] Add leak sensor or at least a visible inspection point.
- [ ] Run cold line to sink faucet cold side.
- [ ] Stub/cap future hot-water feed/return so hot-water uncertainty does not block sink use.
- [ ] Add exterior shower cold QD only if routing does not force premature penetrations.
- [ ] Build graywater cassette/drain path with winterizable/waterless trap strategy.
- [ ] Pressure/leak test plumbing before panel closure.
- [ ] Recheck all clamps/unions after first drive.
- [ ] [DEFER] Hot water decision and permanent heater install.

## 8. AC/DC electrical closeout and tests

Goal: make the already-live electrical system safe, labeled, restrained, and tested in the camper/module context.

- [ ] Confirm main `48V` disconnect operation and shutdown sequence label.
- [ ] Confirm MultiPlus `I/O/II` behavior and safe default state.
- [ ] Confirm SmartShunt/SOC behavior with final battery bank connection.
- [ ] Confirm Orion `48V -> 12V` feed and standalone `F-06` final cleanup if ready.
- [ ] Confirm 12V buffer battery connection path, switch, and fuse state.
- [ ] Confirm 12V junction loads and branch labeling.
- [ ] Confirm Cerbo power, VE.Bus/RJ45, Wi-Fi/console access, and source label `Shore power`.
- [ ] Confirm AC-in path: portable EMS, shore cord, L5-30 inlet, AC-in breaker, MultiPlus.
- [ ] Commission AC-out branches only when the AC enclosure, breakers, grounding/bonding behavior, and GFCI receptacles are physically ready.
- [ ] Test GFCI trip/reset on both intended AC branch areas: office and galley.
- [ ] Test DC USB/PD outlets under realistic laptop/phone/tablet load.
- [ ] Test fridge/cooler DC outlet/feed if installed.
- [ ] Test pump circuit with fuse, switch, connector, and dry-run protection awareness.
- [ ] Add spare fuses in labeled holder/location.
- [ ] Add covers/dead-fronts over touchable AC/high-current DC zones.
- [ ] Record final test results in `logs/LOG.md` once performed.

## 9. Alternator / WS500 / APM-48 workstream

Goal: rough-in safely first; commission only after all preconditions are green.

- [ ] Confirm current mechanical alternator state: bracket/idler/belt/noise status.
- [ ] Confirm alternator remains electrically inert until the full charging path is ready.
- [ ] Confirm Mechman terminal labels: `B+`, `B-`/case ground, field, stator/tach if present.
- [ ] Confirm Wakespeed harness type and field polarity assumptions before wiring.
- [ ] Mount APM-48 at alternator: red to `B+`, black to `B-` or clean case ground per alternator style.
- [ ] Route `2/0 AWG` positive and dedicated `2/0 AWG` negative together along protected frame/bed path.
- [ ] Add chafe protection, loom, rubber-lined clamps, strain relief, and grommet/pass-through protection.
- [ ] Land positive at Lynx Slot 3 / `F-04 150A MEGA` house-bank end.
- [ ] Land dedicated negative return to the Lynx/house negative return path; do not rely on sheet metal/chassis only.
- [ ] Mount WS500 near house electrical board/battery/shunt area for short sense wiring.
- [ ] Wire brown ignition/enable from Ford Upfitter `#3` through `F-15 3A`.
- [ ] Wire PH-VAN red/black locally as combined regulator power/voltage sense through correct small fuse/negative reference.
- [ ] Wire blue field lead through Mechman adapter.
- [ ] Dead-end/protect unused yellow stator/tach unless explicitly required.
- [ ] Protect unused yellow/green CAN connector unless compatible CAN/BMS integration is later added.
- [ ] Install alternator temperature sensor and battery temperature sensor if profile requires.
- [ ] Configure conservative WS500 profile before first enable.
- [ ] First run: Upfitter `#3 OFF`, start engine, verify no unexpected charging.
- [ ] First charge: enable only with meter/app ready and abort plan understood; Upfitter `#3 OFF` must stop current.
- [ ] Measure charge-path and return-path voltage drop under load; target `<0.1V` each per Mechman first-run guidance.
- [ ] Log resting voltage, charging voltage/current, alternator temp, battery temp, WS500 profile, warnings, and shutdown behavior.
- [ ] [HOLD] Do not first-charge from alternator this weekend unless batteries, fusing, APM, WS500 config, sensors, and shutdown behavior are all ready.

## 10. Flooring / Lonseal / hardpoints

Goal: finish floor only after hidden work and anchors are resolved.

- [ ] Inspect bed rail/corner/drain-hole sealing after normal use/cure.
- [ ] Confirm EPS is not proud, buckled, wet, or blocking hardpoint pockets.
- [ ] Confirm plywood slices sit flat and can still be removed intentionally.
- [ ] Mark every planned structural hardpoint before vinyl glue-down.
- [ ] Remove EPS locally at structural hardpoints so plywood bears directly on steel.
- [ ] Confirm no new floor-through penetrations, heater routes, drains, anchor holes, or under-floor service needs remain.
- [ ] Dry-fit Lonseal and confirm pattern/grain/edge trim strategy.
- [ ] Confirm top plywood face is clean, dry, untreated, and adhesive-compatible.
- [ ] Confirm exact trowel, roller/rolling method, masking, blades, gloves, cleanup supplies, and cure window.
- [ ] Glue Lonseal only after floor/rough-in/service-access gate passes.
- [ ] After cure, trim edges and protect while loading modules.
- [ ] Bolt modules through Lonseal only after hardpoint stack and clamp load are correct.
- [ ] Seal any drilled plywood holes before final installation.
- [ ] [HOLD] Do not glue Lonseal before module fit, hardpoint, rough-in, and service-access gates pass.

## 11. Panels, skins, latches, storage, and travel retention

Goal: add only the panels that make the system safer or stiffer before cosmetic closure.

- [ ] Identify panels that are structural/shear/anti-rack vs cosmetic covers.
- [ ] Prioritize panels that brace electrical module, bench, desk, and galley skeleton.
- [ ] Keep electrical/plumbing service panels quick-removable.
- [ ] Use mechanical fasteners, quarter-turns, latches, or captive hardware for panels that matter.
- [ ] Use magnets only for light service covers with locator tabs/lips/backup retention.
- [ ] Add anti-rattle tape/felt/neoprene on panel interfaces.
- [ ] Add latches for every drawer/bin/door/slide in both travel and use states where needed.
- [ ] Add soft storage in body-contact zones instead of hard protruding drawers.
- [ ] Add toe-kick/access storage only if it does not bury service wiring/disconnects.
- [ ] Add labels for service-panel contents.
- [ ] Run a “shake by hand” test before driving.

## 12. Safety, detection, and emergency access

Goal: no daily-use build without basic emergency controls.

- [ ] Install/access fire extinguisher from rear/entry area.
- [ ] Confirm smoke/CO detector placement and power/batteries.
- [ ] Confirm propane/fuel items are not stored loose in interior service cavities.
- [ ] Confirm diesel heater fuel path/service access if heater work is active.
- [ ] Confirm all high-current terminals are covered before furniture becomes daily-use space.
- [ ] Confirm emergency disconnect path can be reached without unloading cabover/bench.
- [ ] Add simple printed/taped shutdown order near electrical service point.
- [ ] Add roof-down/drive checklist near door.
- [ ] Confirm no sharp extrusion/plywood/cable edges in daily movement paths.
- [ ] Confirm no heavy loose tools, batteries, panels, monitor, or fridge can become projectiles.

## 13. Comms, lighting, and comfort systems

Goal: enough utility for a workday without derailing core structure.

- [ ] Stage Starlink/router/dock power location in ventilated tech cubby.
- [ ] Confirm cable route from office electronics to DC/AC power without knee snags.
- [ ] Add temporary task light if final lighting is deferred.
- [ ] Add red/amber night strip only if the wiring path is already clean and non-blocking.
- [ ] Confirm fan/window/vent access remains usable after modules are placed.
- [ ] Confirm heater location/service path remains preserved, even if commissioning is later.
- [ ] [DEFER] Final QuinLED/WLED lighting install unless core modules are stable.
- [ ] [DEFER] Camper audio package; do not spend July 4 sprint time on it.

## 14. Solar research and procurement

Goal: keep solar out of the critical path until roof/module constraints are real.

- [ ] Reopen solar only after shore charging, alternator path, and roof/service constraints are better proven.
- [ ] Confirm roof real estate and shadow/hinge/fan constraints.
- [ ] Confirm flexible vs rigid/stand-off approach, cable gland, combiner/fuse count, and service path.
- [ ] Confirm MPPT `150/45` fit for selected stringing.
- [ ] Confirm roof penetration method and sealant/backing strategy.
- [ ] [DEFER] Pull trigger on panels until layout and charging-priority gates are green.

## 15. Weight, payload, balance, and shakedown

Goal: avoid building a beautiful overloaded rattle box.

- [ ] Record door-sticker payload if not already captured.
- [ ] Weigh major staged modules if practical: batteries, electrical module, bench, desk, galley, tank, water, tools.
- [ ] Plan water as variable payload: `36 gal` full is about `300 lb` water alone, `320+ lb` installed with tank/brackets/hoses.
- [ ] Keep dense storage low and balanced; avoid stacking heavy pantry/tools high on passenger wall with full water.
- [ ] Verify module bolts/hardpoints after the first short drive.
- [ ] Listen for rattles; identify panel, extrusion, latch, cable, and appliance noise sources.
- [ ] Retorque and witness-mark structural fasteners after shakedown.
- [ ] Recheck plumbing for leaks after first fill/drive.
- [ ] Recheck electrical strain relief and cable rub after first drive.
- [ ] Create post-shakedown punch list and sync it back here.

---

# Second-pass additions — major workstreams easy to miss

These are the things most likely to be forgotten when the focus is only modules/electrical/plumbing.

## Measurement and datum control

- [ ] Establish a single floor datum and wall datum for all module measurements.
- [ ] Mark roof-down safe line physically inside the camper.
- [ ] Record final aisle width after module frames and panel/handle allowances, not just bare frames.
- [ ] Record door/barn-door swing and rear-entry clearance with modules in place.
- [ ] Keep a short “changed dimensions” log whenever physical cuts diverge from the workbook.

## Consumables and shop readiness

- [ ] Confirm blades/discs/drill bits/countersinks/taps are in usable condition.
- [ ] Confirm crimp lugs/heat shrink/label tape/loom/P-clamps are enough for the weekend.
- [ ] Confirm adhesives/sealants are in-date and compatible with temperature/cure window.
- [ ] Confirm enough temporary fasteners are available for mockup without stealing final hardware.
- [ ] Confirm vacuum/cleanup plan before Lonseal or electrical work.

## Service documentation while building

- [ ] Photograph final cable routes before panels cover them.
- [ ] Photograph plumbing joints before panels cover them.
- [ ] Label both ends of every non-obvious wire/hose.
- [ ] Keep a list of fuse values and spare locations in the camper.
- [ ] Update `logs/LOG.md` for real tests/measurements, not for every thought.

## Moisture and spill management

- [ ] Add spill lip or protective edge near desk power electronics.
- [ ] Keep AC/USB/power bricks out of sink/desk spill paths.
- [ ] Add wet/dry partition between pump tray and battery/electrical zones.
- [ ] Confirm graywater cassette can be removed without spilling into electrical/battery bays.
- [ ] Confirm fridge condensation/drips cannot run into battery/electrical zones.

## Human factors

- [ ] Sit in the camper with the actual chair/stool before committing desk height.
- [ ] Step into cabover repeatedly using the bench/step mockup before final lid/panel choices.
- [ ] Simulate a workday cable mess: laptop, monitor, keyboard, mouse, phone, tablet, Starlink/router.
- [ ] Simulate cooking/cleaning path: sink cover, induction, Ninja, trash, dish tub, graywater removal.
- [ ] Check where shoes, wet jacket, trash, toilet/portable sanitation, and laundry will actually go.

## First-use / overnight / workday readiness

These do not need to be perfect for the July 4 sprint, but they are real blockers for an actual usable camper.

- [ ] Confirm bedding/cushion mode: where cushions live during work mode vs sleep mode.
- [ ] Confirm cabover entry path with bench/step loaded and desk installed.
- [ ] Confirm toilet/portable sanitation storage and deployment path.
- [ ] Confirm trash location that does not block entry, desk knees, or wet-service access.
- [ ] Confirm shoes/wet jacket/mud landing zone near rear entry.
- [ ] Confirm food bin/pantry location with travel retention.
- [ ] Confirm water fill workflow: fill hose, cap, vent behavior, tank access, overflow/spill control.
- [ ] Confirm graywater removal workflow without spilling into electrical/battery zones.
- [ ] Confirm daily tools/spares location separate from battery bay and wet bay.
- [ ] Confirm doors/windows/fan can be operated after modules and bedding are in place.
- [ ] Confirm privacy/curtain/window-cover minimum viable setup if first overnight is near.
- [ ] Confirm workday setup/teardown checklist: desk, chair, monitor, Starlink/router, power, lighting, ventilation.

## Procurement blocker review

Run this before assuming a weekend task is blocked.

- [ ] Identify true blockers vs “would be nicer with perfect hardware.”
- [ ] Buy/locate only high-leverage missing items: clamps, lugs, heat shrink, labels, hardware, latch parts, sealant, blades.
- [ ] Do not let low-priority finish materials steal time from module structure, electrical safety, or plumbing serviceability.
- [ ] Keep a small `buy now / buy later / do not buy yet` list in or near this checklist.

## Acceptance tests before calling the sprint a win

- [ ] Bench/electrical module does not wobble badly by hand.
- [ ] Batteries can be removed without dismantling the camper.
- [ ] Main electrical service points are reachable.
- [ ] Desk can support a real seated session without knee/entry pain.
- [ ] Monitor/laptop gear has a safe travel state, even if temporary.
- [ ] Galley/fridge/cooler skeleton gives a real datum for fit decisions.
- [ ] Water fill, graywater, toilet/sanitation, bedding, and trash each have a plausible temporary home or an explicit blocker.
- [ ] No planned irreversible work was done before its gate.
- [ ] The next 10 blockers are written down in this file.

---

# Near-term priority queue

## If energy is low

1. Label parts and piles.
2. Charge batteries.
3. Identify galley candidate cuts.
4. Build only enough skeleton to create a datum.
5. Stop before making irreversible cuts when tired.

## If energy is high

1. Bench frame + battery extraction path.
2. Electrical module brace/tie-in.
3. Desk frame/top location.
4. Galley/fridge/wet-spine skeleton.
5. Strain relief, covers, labels, low-power tests.

## Do not spend the long weekend on unless everything above is ahead of schedule

- Final solar purchase.
- Cosmetic skins.
- Permanent monitor mechanism perfection.
- Final lighting design.
- Audio system.
- Hot-water upgrade.
- Decorative finish work.

## Hard holds

- [HOLD] No Lonseal glue-down until hidden floor, hardpoint, rough-in, and service-access gates pass.
- [HOLD] No road travel with freestanding/lightly restrained electrical module.
- [HOLD] No alternator first-charge until APM, fusing, WS500 config, sensors, bank readiness, and shutdown behavior are ready.
- [HOLD] No final countertop sink cutout until faucet/drain/rail clearance is physically proven.
- [HOLD] No final panels over electrical/plumbing until labels, strain relief, leak/functional tests, and service access pass.
