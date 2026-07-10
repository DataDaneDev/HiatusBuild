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

# Live Build Checklist — Flooring Foundation + Running Build Tracker

As-of: `2026-07-10`

Owner: Sunny / Dane

Maintainer rule: **update this file whenever the practical build state, sequence, blocker list, or next physical step changes.** Keep it as the live punch list; do not let stale chat notes become the checklist of record.

## Purpose

This is the active running checklist for the post-install Hiatus/F-350 camper build. It preserves the July 4 sprint record but now translates the flooring-foundation and restrained-reinstall sequence into shop actions, physical gates, and test checkpoints.

It does **not** replace the owner docs:

- Overall sequence: `docs/plans/PROJECT_build_order_of_operations.md`
- Interior/galley baseline: `docs/implementation/INTERIOR_furniture_layout_and_galley.md`
- Workstation/monitor detail: `docs/implementation/INTERIOR_driver_side_workstation.md`
- Flooring/Lonseal gate: `docs/implementation/FLOORING_subfloor_build_process.md`
- Alternator install/commissioning: `docs/implementation/ELECTRICAL_Mechman_WS500_APM48_install_guide.md`
- Decisions/risks/open questions: `docs/core/TRACKING.md`

## Current build posture

- Owner-reported `2026-07-06`: Desk/storage and Galley modules were reinforced and test-installed; the Galley rear stretch was rebuilt as one continuous `2010` member and the integrated layout was verified well enough to enter the floor teardown/reinstall gate.
- `2026-07-10` engineering correction: the `2021 F-350` pickup box is aluminum. The on-hand steel rivet nuts (BOM row `127`) and stainless hardware (row `46`) are rejected for direct pickup-box hardpoints under Ford SVE `Q-222R1`; use a measured-grip aluminum rivet-nut/Plusnut system and Ford-compatible coated/isolation stack instead.
- Do not drill the bed around connected/live electrical equipment. Finish the remaining Desk/storage geometry, isolate the system/remove loose batteries, transfer/record the real module-foot centers, then remove the modules before final bed drilling and chip cleanup.
- The existing three-piece single-layer `3/4 in` plywood is below Lonseal's published minimum two-layer `7/8 in` wood substrate. Hold glue-down until either a staggered `1/4 in` APA underlayment passes a `0.250 in` clearance mockup or Lonseal provides a written exception for the exact vehicle substrate.
- One wide Gorilla Waterproof Patch & Seal Tape roll has been used on discrete drill holes/small spots and a second matching roll is planned. Gorilla says the tape is not for seams; do not blanket body seams, unknown gaps, or intentional drains. Classify openings and pass a controlled low-flow ingress test before closing the floor.
- Floor/module restraint is now three separate problems: independent subfloor retention, ordinary cabinetry hardpoints, and reinforced/redundant heavy-system restraint for the battery bench, electrical module, and full water tank. Do not assume thin pickup-box-sheet inserts are crash-rated.
- EPS remains in bed-rib valleys only. Trim proud/wet/damaged EPS that rocks plywood or blocks a deliberate drain, but never carry bolt preload through EPS. Use measured rigid aluminum compression sleeves where a hardpoint spans soft material or would crush the finish/substrate stack.
- Final surface direction remains a three-piece Nick black-walnut commission after templates are locked. A temporary Galley plywood counter/template is acceptable before final walnut so sink/faucet geometry can be proven.
- Plumbing remains discovery/mockup until electrical and counter geometry make it testable, but floor completion may be the prerequisite that makes final routing worth doing.
- Alternator charging remains a separate commissioning gate. Rough-in/routing with fuses pulled can proceed after floor/module reinstall; first-charge waits for APM, fusing, WS500 config, sensors, bank readiness, and shutdown behavior.
- Solar, hot water, and propane remain discovery/provisioning workstreams until shore, water/fill routing, roof real estate, and exterior mount/pass-through constraints are better proven.

## Historical July 4 sprint strategy

### Definition of a successful long weekend

A realistic win is **not** a finished camper. A realistic win is:

As of `2026-07-04`, the Galley/cooler/Bench/electrical tie-in has moved from target to current state. The remaining weekend win is Desk/workstation geometry plus floor/hardpoint/service gates.

1. Galley/fridge/wet-spine skeleton tied into the Bench/cooler area enough to stop tipping and become the datum for cooler/fridge/plumbing fitment.
2. Galley front corner roughed as an entrance-safe service corner, with removable, accessible fasteners.
3. Battery bay/extraction path physically proven with batteries still out or isolated.
4. Floor hardpoint and Lonseal escape path preserved before final battery wiring.
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

### Foundation-gate priority ladder — `2026-07-10`

Now that the module fit is proven, close the foundation gates in this order:

1. **Freeze geometry without drilling metal:** finish Desk/storage corrections, isolate electrical/remove loose batteries, photograph/label all modules, transfer-punch/trace real feet/tabs into tape or plywood, classify anchors `F` floor / `C` cabinetry / `H` heavy, and record centers from two fixed bed datums.
2. **Remove once and expose the bed:** remove modules as labeled assemblies, then lift the floor layers in order. Vacuum, map every hole/seam/drain/patch, and verify no-drill/backside-clearance zones.
3. **Close sealing and drainage:** use tape only on discrete compatible holes, rework seam/drain crossings, repair larger openings mechanically, cure, then pass a controlled low-flow ingress test. Preserve a documented low-point drainage/inspection strategy.
4. **Close substrate/material gates:** settle/trim EPS and plywood; mock the optional `1/4 in` underlayment height; obtain Lonseal acceptance or add the underlayment; select aluminum inserts/coated fasteners from measured grip; test the insert stack on matched aluminum.
5. **Drill/set/register:** drill the de-energized, empty work area with depth control; deburr/vacuum/coating-protect; set/test aluminum inserts; add independent floor retention; fit rigid compression sleeves; prove every location with temporary locator bolts and a full module refit.
6. **Glue only after complete dry run:** decide flat perimeter vs flash-cove, dry-fit the one-piece Lonseal, stage #650 tools/temperature/two-person workflow, then glue/roll/reroll and allow the full `72 h` cure.
7. **Reinstall + prove restraint:** protect the finish, reinstall on proven stacks, torque/witness-mark, verify battery/service access and heavy-system redundant load paths, then perform a low-consequence shakedown and reinspection.
8. **Electrical/plumbing after floor:** final-route alternator/shore/full-bank electrical and testable plumbing only after the floor no longer needs another major teardown. Keep solar/hot-water/propane as parallel discovery, not penetration drivers.

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
- [ ] Mark the known latest cutlist workbook as the current source: `docs/plans/assets/module-cutlists/2026-07-04_module-cutlist-and-assignments.xlsx`.
- [ ] Preserve the Bench one-off updates in the workbook; do not overwrite the local working copy blindly from `HEAD`.
- [x] Keep module piles separate: `Bench`, `Galley`, `Electrical`, and the remaining `Desk` pool.
- [x] Mark the `23` workbook-assigned Galley pieces with `G` on the floor before cutting.
- [ ] Mark the `24` workbook-assigned Desk pieces with `D` on the floor before final desk cuts.
- [ ] Label every cut extrusion with module + length + workbook/source row if known.
- [ ] Separate hardware by class: T-nuts, angle brackets, corner cubes, panel fasteners, bolts/washers, latch hardware.
- [ ] Identify missing hardware that blocks final travel-tight assembly vs hardware that only blocks cosmetics.
- [ ] Stage fire extinguisher, first-aid, insulated tools, multimeter, crimper, heat shrink, labels, paint pen/witness marker.
- [ ] Start a paper/shop whiteboard punch list for anything discovered physically; sync durable items back here.

## 1. Battery charging and staging

Goal: keep batteries safe and isolated until physical access, floor hardpoints, and service path are proven enough for final in-truck wiring.

- [ ] Confirm the currently charged battery count and SOC/voltage.
- [ ] [DEFER] Charge the other `3 of 4` batteries, including the `12V` battery, after the battery install path is comfortable in the truck.
- [ ] For each `48V` battery, record resting voltage and display SOC after charge/rest.
- [ ] For the `12V` battery, record resting voltage and display SOC after charge/rest.
- [ ] Confirm all batteries are above low-temperature charge cutoff before charging.
- [ ] Confirm no battery is in BMS protection state.
- [ ] Confirm battery terminals are covered while batteries are staged loose.
- [ ] Confirm each 48V battery has its intended Class T/fuse/disconnect path before being paralleled into service.
- [ ] Confirm battery extraction path from the bench: no rail, lid, panel, or cable blocks removal.
- [ ] Add temporary “charged / not charged / do not connect” labels if any battery is out of sync.
- [ ] Use battery placeholders or no-battery clearance checks during Galley/Bench dry fit; do not let loose heavy batteries become shop obstacles.
- [ ] [HOLD] Do not final-route, final-cut, or final-torque battery cabling until floor hardpoints/Lonseal strategy and battery extraction access are proven.

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
- [ ] Confirm no final floor bolt or hardpoint will be hidden under an installed battery or inaccessible galley/bench member.
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

- [x] Use the Desk assignments now written in the current workbook: `24` total pieces tagged `Desk` in `piece_assignment` / `garage_final_cutlist`, with a dedicated `desk_shop_list` tab.
- [x] Desk/storage module reinforced and mostly test-installed in the truck as of owner report `2026-07-06`.
- [~] Apply owner-identified Desk/storage corrections from the first test install before locking top/panel geometry.
- [ ] Mark these `D` on the floor before final desk cuts if any uncut pieces remain: `1-3`, `5-1`, `6-1`, `7-2`, `7-3`, `8-2`, `8-4`, `9-1`, `9-3`, `10-1`, `10-2`, `10-4`, `12-2`, `12-3`, `15-4`, `16-3`, `17-1`, `17-2`, `18-2`, `18-3`, `19-1`, `20-1`, `20-2`, `21-1`.
- [~] Reconfirm driver-side desk footprint near wheel well; current target remains roughly `24 in x 48 in` until measured fit says otherwise.
- [ ] Mock chair/stool position and seated elbow height.
- [ ] Check knee/foot clearance around wheel well and electrical step projection.
- [~] Place rough desktop or template at target height.
- [ ] Confirm entry/exit movement and hip/shoulder clearance.
- [ ] Confirm roof-down sweep envelope for desk, DC shelf, monitor stow block, and cable loops.
- [ ] Record any changed Desk/storage dimensions from the `2026-07-06` test install in the changed-dimensions log before updating Nick/template packets.
- [ ] Decide desktop material for MVP: plywood/laminated birch template now; final commissioned black walnut after seated fit, roof sweep, and entry clearance are proven.
- [~] Build lower desk frame tied into the electrical/bench spine.
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

- [x] Use the Galley assignments now written in the current workbook: `23` total pieces tagged `Galley` in `piece_assignment` / `garage_final_cutlist`.
- [x] Galley extrusion frame cut and built as an exoskeleton.
- [x] Mark these `G` on the floor before cutting: `1-1`, `2-1`, `2-2`, `5-2`, `6-2`, `11-1`, `12-1`, `12-4`, `13-1`, `16-4`, `17-4`, `17-5`, `19-3`, `19-4`, `19-5`, `19-6`, `20-4`, `20-5`, `21-2`, `21-3`, `21-4`, `21-5`, `21-6`.
- [x] Preserve the existing Bench reservations from shared source-row pools; Galley uses the remaining unassigned `R18`/`R19`/`R21` pieces plus the owner-confirmed `17.5 in` row.
- [x] Tie the Galley frame into the Bench/cooler area so the current one-leg/tippy state becomes a restrained rectangle before adding skins or heavy fixtures.
- [x] Reinforce Galley rear/back stretch as one continuous `2010` member; owner reports the Galley is now very sturdy as of `2026-07-06`.
- [x] Modify/add cooler-bench tie-in rails or plates as needed; keep the seam removable and accessible without removing batteries.
- [ ] Decide the entrance-side Galley front corner shape with a physical sweep test: default `45° chamfer` if square clips entry and round is too fussy for the current 10-series frame.
- [ ] Keep the front/rear Galley utility corner as a serviceable wet corner candidate: drain path, spray nozzle/QD, future hot-water stub, and removable panel access.
- [ ] Do not commit to permanent propane hot water in the Galley corner until the exact listed appliance, vent/cutout, combustion air, clearances, LP routing, detectors, and winterization access are proven.
- [ ] Mock passenger-side fridge/cooler position with real handles, hinge/lid swing, cord bend, and hand clearance.
- [ ] Confirm raised fridge/cooler height target, currently about `16 in` above floor/service zone.
- [ ] Confirm relationship to `36 gal` wheel-well tank envelope.
- [ ] Build the lofted fridge/cooler support skeleton as a service exoskeleton, not a sealed cabinet.
- [x] Tie Galley to Bench/electrical structure with removable plates/bolts reachable from the aisle/top/service openings; avoid hidden fasteners that require removing batteries.
- [ ] Add positive fridge/cooler travel restraint and hard stops.
- [ ] Preserve lower cool-air intake and upper warm-air exhaust around fridge compressor vents.
- [ ] Confirm pump/accumulator/strainer/manifold service opening below/near fridge.
- [ ] Confirm wet bay cannot leak into battery/electrical bays; add partition/drip tray concept.
- [ ] Place Sarlai `15 in x 15 in` topmount sink template on galley counter area.
- [ ] Confirm final Nick Galley counter dimension sheet: likely `~4 ft x 19 in`, `1.5 in` preferred thickness / `2 in` acceptable, with the last `~15 in` inward-curving live-edge target if the slab allows.
- [ ] Confirm black walnut counter support-tab/fastener locations before Nick cuts/drills; do not rely on cosmetic skins to carry the slab.
- [ ] Choose finish sample for black walnut Galley: satin polyurethane/default durable film finish; epoxy only for local void/check stabilization unless intentionally choosing a plastic-gloss flood coat.
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
- [ ] Rough-plan a pump-fed cold spray nozzle/QD near the Galley utility corner; gravity-only spray is acceptable as a fallback drain/rinse concept but should not drive the layout.
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

Goal: use the verified module fit to do the one major teardown intentionally, finish the floor foundation, and reinstall modules onto known hardpoints before final electrical/plumbing routing.

- [~] Flooring is the active foundation gate now that major modules are test-fit.
- [ ] [HOLD] Reject BOM row `127` steel inserts and row `46` stainless hardware for direct attachment to the aluminum pickup box.
- [ ] [HOLD] Measure actual pickup-box sheet/grip and select a Ford-compatible aluminum rivet-nut/Plusnut plus coated-bolt/aluminum-washer/isolation stack.
- [ ] [HOLD] Resolve the Lonseal substrate discrepancy: mock `1/4 in` APA underlayment clearance or obtain written acceptance of the current single-layer `3/4 in` three-panel substrate.
- [ ] Finish Desk/storage geometry enough to trust final feet/tabs.
- [ ] Isolate/de-energize electrical and remove loose batteries before marking/drilling work.
- [ ] Photograph and label every module connection, seam, shim, bracket, service opening, and fastener group.
- [ ] Trace footprints and transfer actual foot/tab centers; classify anchors `F`, `C`, or `H` and record centers from two fixed bed datums.
- [ ] Identify heavy-system second/reinforced load paths for battery bench, electrical module, and full water tank; do not assume thin-sheet inserts are crash-rated.
- [ ] Remove modules as assemblies where practical.
- [ ] Lift floor layers, vacuum, and map every hole, seam, factory drain/weep path, existing patch, corrosion area, and underside obstruction.
- [ ] Inspect existing Gorilla tape; remove/rework any patch crossing a seam, drain, or unknown opening. Use the second roll only on discrete compatible holes.
- [ ] Cure repairs and pass the controlled low-flow/blotter ingress test before re-covering the bed.
- [ ] Confirm EPS is dry, not proud/buckled/crushed, and not blocking a deliberate drain; never carry clamp load through EPS.
- [ ] Dry-fit/settle the three plywood panels and resolve rocking, high joints, unsupported edges, and independent floor retention.
- [ ] Mock the additional `0.250 in` substrate option against module feet, doors/threshold, service panels, and roof-down geometry.
- [ ] Prove final insert drill/collapse/spin/service behavior on matched-gauge aluminum before drilling the truck.
- [ ] Verify under/behind every hole, use a drill stop, deburr/vacuum immediately, restore aluminum corrosion protection, then set/test inserts.
- [ ] Cut rigid aluminum compression sleeves to the measured finished stack where preload would cross soft material or crush the floor.
- [ ] Refit modules with temporary locator bolts; prove bolt access, hardpoint alignment, battery extraction, service access, and independent floor stability.
- [ ] Confirm no new floor-through penetration remains or reserve/grommet/edge-protect it before Lonseal.
- [ ] Decide flat perimeter vs flash-cove; #650 is horizontal-only and vertical/coved surfaces require #400 or written Lonseal direction.
- [ ] Dry-fit Lonseal and confirm pattern/grain, perimeter, and hole-recovery strategy.
- [ ] Confirm the accepted top bond face is clean, dry, smooth, flat, untreated, and adhesive-compatible.
- [ ] Stage the exact trowel, full-pressure roller method, low-speed mixer, two people, PPE/ventilation, masking, blades, and ethyl-alcohol cleanup cloths.
- [ ] Hold `65-85°F` for at least `48 h` before/during/after; mix the complete #650 unit, place within the working window, roll both directions, and reroll after `2-3 h`.
- [ ] No foot traffic for `24 h`; no modules/heavy traffic until the full `72 h` cure.
- [ ] Seal cut substrate edges/pass-through annuli without putting soft sealant in structural bearing faces.
- [ ] Protect Lonseal during module reinstall, torque to the validated insert procedure, witness-mark, then repeat rack/battery/service checks.
- [ ] Perform a low-consequence shakedown and inspect/retorque for insert spin, sleeve settlement, vinyl indentation, moisture, abrasion, or module shift.

## 11. Panels, skins, latches, storage, and travel retention

Goal: add only the panels/features that make the system safer, stiffer, more serviceable, or visually intentional before cosmetic closure. Detailed feature choices live in `docs/implementation/INTERIOR_finish_paneling_and_feature_choices.md`.

- [ ] Map every Galley/Bench/desk face as `finished wood`, `service removable`, `smoked/translucent feature`, or `open/exposed 80/20`.
- [ ] Identify panels that are structural/shear/anti-rack vs cosmetic covers.
- [ ] Prioritize panels that brace electrical module, bench, desk, and galley skeleton.
- [ ] Use `1/2 in` plywood for most living-facing vertical/removable faces; use `3/4 in` for tops, bench lids, cooler-bearing surfaces, step/load surfaces, and large horizontal spans.
- [ ] Mock Galley, desk, and L-shaped Bench/lid tops in `3/4 in` plywood before Nick cuts premium black walnut.
- [ ] Prepare Nick's dimension packet: Galley live-edge counter/template, Desk top template, L-shaped Bench/lid template, support tabs, hinge line, latch points, and any cutout/no-drill zones.
- [ ] Make at least two finish samples on scrap: clear satin and one warmer/stained option.
- [ ] Make black walnut/offcut finish samples: satin polyurethane as default; epoxy only as a selective fill/stabilizer sample unless intentionally choosing full flood coat.
- [ ] Size Bench/lid gas struts only after actual walnut lid weight, hinge line, opening angle, and mount points are known.
- [ ] Add positive closed-state latch, anti-rattle bumpers, and a mechanical open stop/backup support for the Bench/lid; gas struts are not travel retention by themselves.
- [ ] Prototype one `1/2 in` overlay panel using the intended fasteners/spacers/anti-rattle tape; keep hardware visually quiet against the silver extrusion rather than making it a feature.
- [ ] Source/test one smoked acrylic/polycarbonate sample before committing the `45°` front cupboard feature panel.
- [ ] Mock the `45°` Galley front cupboard in cardboard and confirm door swing/reach/cooler/bench interference before cutting plastic or finished wood.
- [ ] Keep electrical/plumbing service panels quick-removable.
- [ ] Use mechanical fasteners, quarter-turns, latches, or captive hardware for panels that matter.
- [ ] Use magnets only for light service covers with locator tabs/lips/backup retention.
- [ ] Add anti-rattle tape/felt/neoprene on panel interfaces.
- [ ] Add latches for every drawer/bin/door/slide in both travel and use states where needed.
- [ ] Prefer lift-out bins, elastic/shock-cord cubbies, and a few low positive-latched drawers over a full drawer wall until dimensions are stable.
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

1. Write the Desk/storage correction list on tape or paper and photograph the current module state.
2. Mark changed dimensions, module footprints, seams, shims, brackets, floor-tab/hardpoint candidates, roof/entry/interference notes, and battery extraction path before moving parts again.
3. Label the next service-panel zones: electrical, wet spine, battery, bench lid, desk cubby.
4. Sort the next `buy now / buy later / do not buy yet` items: Plusnuts/rivnuts and setting tooling, Lonseal adhesive/tools/protection, hardpoint/floor-tab hardware, panel fasteners/latches, P-clamps/loom/labels, plumbing fittings, shore-port hardware.
5. Stop before drilling final holes or gluing flooring when tired.

## If energy is high

1. Finish Desk/storage corrections enough to trust module geometry, then photograph/label/trace everything before teardown.
2. Run the pre-teardown hardpoint day: choose floor tabs, mark centers, confirm drill/Plusnut access, install/test/register Plusnuts where practical, and build the Lonseal hole-recovery map.
3. If the hardpoint gate is green, remove modules once, clean/level the bed and plywood, dry-fit/pre-punch Lonseal, glue/cure/protect, then reinstall and hard-mount modules.
4. After floor/module reinstall, final-route electrical: alternator conductors/harness, shore power, full `4x` battery install, covers, labels, strain relief, and controlled tests.
5. After floor + electrical + temporary Galley counter template, final-route plumbing when it can actually be leak/function tested.

## Do not prioritize next unless the gate above is already green

- Gluing Lonseal if hardpoints, service access, future pass-through reservations, adhesive/tool/cure conditions, or plywood leveling are still fuzzy.
- Full battery-bank install before the floor no longer needs teardown.
- Alternator first-charge.
- Final solar purchase or roof penetration.
- Permanent propane/hot-water appliance mount.
- Cosmetic skins everywhere.
- Permanent monitor mechanism perfection.
- Final lighting design.
- Audio system.
- Decorative finish work.

## Hard holds

- [HOLD] No Lonseal glue-down unless module fit is verified, hardpoints are determined with modules still installed, Plusnut/rivnut holes are drilled/tested/registered, service access is preserved, future pass-through/floor-through needs are reserved or explicitly not needed, plywood is level/prepped, and adhesive/tool/cure conditions are ready.
- [HOLD] No road travel with freestanding/lightly restrained electrical module.
- [HOLD] No full `4x` battery install until the floor/module-reinstall gate is closed enough that the bank will not need to come back out for flooring.
- [HOLD] No alternator first-charge until APM, fusing, WS500 config, sensors, bank readiness, and shutdown behavior are ready.
- [HOLD] No final countertop sink cutout until faucet/drain/rail clearance is physically proven.
- [HOLD] No premium black walnut final cuts until plywood templates, support tabs, service access, entry sweep, and finish sample are approved.
- [HOLD] No final panels over electrical/plumbing until labels, strain relief, leak/functional tests, and service access pass.
- [HOLD] No shore, water-fill, propane, or roof/solar exterior penetrations until both the exterior location and inside service/routing/strain-relief path are physically proven.
