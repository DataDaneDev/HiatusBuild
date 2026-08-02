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

# Live Build Checklist — Electrical Commissioning + Wet-Spine Integration

As-of: `2026-07-31`

Owner: Sunny / Dane

Maintainer rule: **update this file whenever the practical build state, sequence, blocker list, or next physical step changes.** Keep it as the live punch list; do not let stale chat notes become the checklist of record.

## Purpose

This is the active running checklist for the post-install Hiatus/F-350 camper build. It preserves the July 4 sprint record but now translates hard-mounted electrical integration, bank/`12V` commissioning, exterior penetrations, wet-spine testing, and restrained module closeout into shop actions, physical gates, and test checkpoints.

It does **not** replace the owner docs:

- Overall sequence: `docs/plans/PROJECT_build_order_of_operations.md`
- Interior/galley baseline: `docs/implementation/INTERIOR_furniture_layout_and_galley.md`
- Workstation/monitor detail: `docs/implementation/INTERIOR_driver_side_workstation.md`
- Flooring/Lonseal gate: `docs/implementation/FLOORING_subfloor_build_process.md`
- Alternator install/commissioning: `docs/implementation/ELECTRICAL_Mechman_WS500_APM48_install_guide.md`
- Decisions/risks/open questions: `docs/core/TRACKING.md`

## Current build posture

- Owner-reported `2026-07-19`: the electrical module is hard-mounted through the permanent Lonseal/plywood floor to truck-bed hardpoints. Fit is clean and it is stable enough for continued stationary work; the Bench tie-in remains required for final anti-rack stiffness and road restraint.
- The MultiPlus and combined AC breaker enclosure were temporarily removed before lifting. Embedded pronged/spiked T-nuts remain in the electrical backer, making both devices straightforward to remount from the service face.
- All three `48V` batteries' positive/negative `2/0 AWG` branch leads are cut, lugged, heat-shrunk, and landed at the battery-side busbars. The batteries remain isolated until Batteries 2 and 3 are individually charged, rested, and within `0.1V` before paralleling.
- The `12V` battery branch is close to completion, and the Orion/fuse panel are already mounted/wired. Final Orion input cleanup is one verified `40A` MEGA (`58VDC` minimum under the locked `56.8V` charge ceiling; Victron `CIP138040020 40A/80V` is the replacement fallback) in Lynx Slot 4 feeding the existing `6 AWG` input pair directly; remove/bypass the separate inline input fuse and retire `F-06`. Slot 2 remains `F-03 60A/80V` for MPPT. Keep `F-07 60A/80V` on Orion `12V` output and `F-11 100A` ANL on the `12V` battery positive branch.
- The water bench topology has passed an open-end function test from the tank/pump/accumulator through both hot and cold runs to the rear endpoints, and the owner reports an additional in-truck leak/function pass. That is useful interim evidence, but final acceptance still follows the replacement KUS mount, BLUE/RED bulkheads, fill/vent closeout, and one dry-compartment pressure/dwell test because those operations change the circuit. The gravity-fill hatch penetration was installed successfully on `2026-07-28`; final fill-hose/vent routing remains open. The two BLUE/RED service-port holes still wait for the inbound `27 mm` cutter **and** the actual Joolca/HQMPC latch-flow fit, bulkhead backing/thickness, and installed route—not the cutter alone.
- The Galley remains intentionally free-floating so the tank can come back out for the replacement KUS backing ring and the rear service holes can be worked without obstruction. Stationary MultiPlus/AC-enclosure remount and battery charging may proceed after all errands are complete, but the truck is a no-drive worksite until the Galley/Bench/electrical anti-rack tie and road restraint are complete.
- With the MultiPlus and AC enclosure remounted in their final backer locations, the shore inlet may proceed once its complete inside/outside path, hidden structure, backer grommet/strain relief, bend radius, and sealing surfaces are proven; the Galley tie is a road-restraint gate, not a blocker to stationary shore-route proof.
- Final surface direction remains a three-piece Nick black-walnut commission after templates are locked. A temporary Galley plywood counter/template is acceptable before final walnut so sink/faucet geometry can be proven.
- Plumbing is active fitment work. The tank/pump/accumulator and hot/cold runs worked correctly outside the camper through the rear endpoints, but the first KUS/`FLS-U` installation still has one stripped/galled free-spinning screw and a major sender-gasket leak. The empty leaking tank remains acceptable as a dry-fit geometry block, but hold water service and final tank restraint until the failed hardware is removed, the `FLS-U` ring/main gasket/matched screws are replaced, and a dry-area leak test passes. Whole-Galley removal is accepted for uncommon tank service; preserve accessible frame seams and a documented disassembly path rather than adding quick disconnects.
- Alternator charging remains a separate commissioning gate. Rough-in/routing with fuses pulled can proceed after floor/module reinstall; first-charge waits for APM, fusing, WS500 config, sensors, bank readiness, and shutdown behavior.
- Solar remains a discovery/provisioning workstream, but the Standard 4 X is now in hand as of owner report `2026-07-31`. Bench-activate it and measure the actual terminal, cable, connector, router/power-supply, and candidate mount envelope before drafting the combined fan/Starlink/solar roof plan. Keep panel procurement and roof penetrations held until the actual mount, popup service loop, shadows, roof-weight cap, cable route, and final panel/string layout are proven. Hot water remains the propane-only Joolca HOTTAP V2 package.

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

### Systems-integration priority ladder — `2026-07-31`

1. **Clear the truck-position dependency once:** pump-drain the tank, isolate/cover batteries, and remove or positively strap the loose tank, Galley, and shop gear before the minimum low-speed on-property turn. Do this before remounting the heavy MultiPlus/AC equipment; no public-road travel in the current free-floating Galley state.
2. **Finish the stationary electrical core:** remount the MultiPlus and AC enclosure, verify covers/support/service clearance, then close the Orion input and `12V` buffer branches. Battery 1 may power the protected `48V` bus for controlled Orion/`12V` proof, with normal pre-charge and branch-isolation checks; do not parallel unmatched batteries.
3. **Charge and match the house bank in parallel with other shop work:** charge Batteries 2 and 3 individually, rest/record all three, and parallel only when maximum-to-minimum rested voltage is `<=0.1V`.
4. **Clear the hardware-dependent wet side:** rebuild and bench-prove the KUS mount when the replacement ring arrives; mock the real sink/faucet; prove Joolca/HQMPC latch/flow plus bulkhead backing before cutting BLUE/RED holes; then finish fill/vent and run the final dry-area pressure/dwell test.
5. **Close structure before optional roof work:** after KUS and rear-port access no longer require the Galley loose, tie Galley/Bench/electrical together for road restraint. Bench-test and measure Starlink, then draft the integrated roof layout; solar procurement and roof holes remain downstream.

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
- [ ] Bring the `3x 48V` house batteries to a compatible resting voltage/SOC before paralleling; stage the separate `12V` buffer battery independently.
- [x] Cut, lug, adhesive-heat-shrink, and land all three batteries' positive/negative `2/0 AWG` branch cables at the battery-side busbars while the bay is open.
- [ ] Charge Battery 2 individually through the proven MultiPlus shore-charge path, then allow it to rest and record voltage/SOC.
- [ ] Charge Battery 3 individually, then allow it to rest and record voltage/SOC.
- [ ] Confirm all three rested battery voltages are within `0.1V` before making the parallel connection; do not use the parallel bus to equalize a larger mismatch.
- [ ] For each `48V` battery, record resting voltage and display SOC after charge/rest.
- [ ] For the `12V` battery, record resting voltage and display SOC after charge/rest.
- [ ] Confirm all batteries are above low-temperature charge cutoff before charging.
- [ ] Confirm no battery is in BMS protection state.
- [ ] Confirm battery terminals are covered while batteries are staged loose.
- [ ] Confirm each 48V battery has its intended Class T/fuse/disconnect path before being paralleled into service.
- [ ] Confirm battery extraction path from the bench: no rail, lid, panel, or cable blocks removal.
- [ ] Add temporary “charged / not charged / do not connect” labels if any battery is out of sync.
- [ ] Use battery placeholders or no-battery clearance checks during Galley/Bench dry fit; do not let loose heavy batteries become shop obstacles.
- [~] Floor release, module hard-mounting, and branch-cable fabrication are complete; hold final battery energization/torque/cover closeout until extraction access, polarity, branch protection, and the `<=0.1V` match are verified with the Bench open.

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
- [~] Branch cables are fabricated/landed at the busbars; charge/match/connect/fuse/cover the `3x 48V` bank before adding any Bench bridge, lid support, or upper member that obstructs terminal, fuse, disconnect, cable-clamp, or extraction access.
- [ ] Add edge protection/scuff plate where the bench doubles as a step.
- [ ] Mark fasteners for final witness marks after retorque, not during first loose mockup.
- [ ] Do not install final skins until electrical service and battery extraction pass.

## 3. Electrical module mechanical integration

Goal: turn the freestanding live-proven electrical module into a restrained mobile module.

- [x] Release/protect the Lonseal enough for controlled electrical-module loading; retain the final floor-condition photo/inspection item in Section 10.
- [x] Hard-mount the electrical module through registered floor/truck-bed hardpoints before the battery Bench or remaining furniture closes side/fastener access.
- [x] Place the electrical module in its intended installed position; owner reports clean fit and good stationary stability.
- [~] MultiPlus fit was previously proven, but it is temporarily off the backer; confirm final depth, airflow, terminal, and removal clearance during remount.
- [x] Preserve easy front-side equipment remounting with embedded pronged/spiked T-nuts in the plywood backer; do not replace them with loose rear nuts.
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
- [ ] Keep the front/rear Galley utility corner serviceable for the sink drain/graywater path, faucet cold/hot trunks, the BLUE source valve, unvalved RED hot return, and removable panel access; no interior water-heater volume is reserved.
- [~] The separate BLUE/RED camper penetrations and direct QDs are installed. Continue to hold the rear-box HOTTAP/propane package until the purchased Quick-Release HOTTAP Bracket backing and HOTTAP V2 Mount Cover, cylinder restraint/venting, regulator service hatch, supplied-hose reach, and operating clearances are physically proven.
- [ ] Mock passenger-side fridge/cooler position with real handles, hinge/lid swing, cord bend, and hand clearance.
- [ ] Confirm raised fridge/cooler height target, currently about `16 in` above floor/service zone.
- [ ] Confirm relationship to `36 gal` wheel-well tank envelope.
- [ ] Build the lofted fridge/cooler support skeleton as a service exoskeleton, not a sealed cabinet.
- [ ] Tie Galley to Bench/electrical structure with removable plates/bolts reachable from the aisle/top/service openings after KUS service and rear-port work are complete; the Galley is intentionally free-floating through the current stationary work window and the truck must not travel in that state.
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

Goal: build and test the fixed cold-water pack plus the selected propane-only BLUE cold-out / RED hot-return interface; keep every joint serviceable and leak-testable.

- [x] Record owner-confirmed physical geometry: four molded ports on each end, two visibly large and two smaller per end, with no obvious/open top port.
- [ ] Photograph/inventory the eight end ports, identify exact threads/model markings, inspect for a membrane-covered top boss, and temporarily label candidate functions: gravity fill, highest-point vent, pump outlet, drain, sender, spare/plug.
- [ ] Measure internal sender clearance at the exact KUS location and confirm a flat top area over the deepest unobstructed section; do not rely on the nominal `16 in` exterior depth alone.
- [ ] Lay out the gravity-fill hose, vent hose, pump outlet, drain, KUS sender, restraint brackets, and compact pump/accumulator pack around the empty tank on the workbench.
- [~] In-truck wet-spine fitment has progressed far enough to install the gravity-fill hatch and confirm that KUS service is physically possible with the tank installed but materially easier with the Galley loose and tank removable. Before final tank restraint, finish verifying wheel-well fit, bracket/plusnut reach, extrusion/fridge overlap, fill/vent bends, pump-board access, leak path, and the accepted whole-Galley tank-removal sequence; do not road-travel in this state.
- [ ] Freeze the tank port map after dry fit. Current default is upper large end port for gravity fill, highest suitable upper small end port for unrestricted vent/overflow, low north port for pump suction, and no projecting valve at the low south footpath boss; require continuous downhill fill-hose routing and continuous vent rise without a trapped low loop.
- [x] Select the KUS sender backing method: KUS/Wema `FLS-U` stainless SAE five-hole C-ring under-ring with the main sender gasket and matched long `FLS-U` screws; do not rely on self-tapping screws or sealant alone. The separate KUS gasket-mounting kit includes short screws with bonded metal/rubber sealing washers, while the official `FLS-U` manual depicts the long under-ring screws without transplanted washers. Do not peel or transfer loose rubber pieces between the two screw sets.
- [ ] Inventory the KUS electrical handoff before tank closure: locate the Cerbo GX MK2 factory `Tank` terminal block, confirm enough `18-22 AWG` duplex from sender to Cerbo, and stage two sealed pigtail splices plus two Cerbo-end ferrules. Wire black signal and pink return to the same numbered Tank-input column; no external power, fuse, chassis ground, analog gauge, or GX Tank 140.
- [ ] Bench-check the sender across its two leads before mounting (`~240 ohm` float down/empty, `~30-33 ohm` float up/full). After wiring, enable `Tank 1` at `Settings -> Integrations -> Tank and Temperature Sensors`, then set `Fresh Water`, `36 US gal`, and the US `240-30 ohm` sender standard; refine the custom tank shape only after measured fills.
- [x] Purchase the exact `2-3/8 in` / `60 mm` KUS-sender hole saw (BOM row `239`, ordered `2026-07-24`); procurement does not clear the cut gate.
- [x] Acquire the water-penetration cutters (`27 mm / 1-1/16 in` carbide cutter for the BLUE/RED RAINPAL service ports, `1-1/2 in` for the selected large-boss membrane field-fit, and `3-1/4 in` for the IZTOR camper-wall hatch) plus supplemental `1/2 in` PEX-B `90` elbows and cinch clamps (`2026-07-26`). The tank-boss cutter must visibly clear the internal threads before use.
- [~] The `60 mm / 2-3/8 in` sender opening is cut and the first `FLS-U` installation was attempted. Owner report `2026-07-27`: backing out the long sender screws damaged at least one under-ring thread; one screw is seized/spins without moving or producing clamp load, and water pours through the main gasket when the tank is inverted. This is a failed seal, not acceptable top-side splash tolerance.
- [ ] Recover and rebuild the sender mount before tank installation: remove the other free screws; if the failed screw spins, apply gentle upward load while backing it out; if it remains seized, protect the polyethylene and sender, capture all swarf, tether the C-ring, and remove only the failed screw head so the sender can lift and the ring/shank can rotate out through the `60 mm` opening. Replace the damaged `FLS-U` ring, main gasket, and all matched long screws as a set; inspect the sender flange and tank sealing land for bend, gouge, crack, or distortion. Hand-start every screw, tighten incrementally in a star pattern with a hand driver, and stop if any screw binds before seating. Do not tap the damaged ring oversize, install a thread insert, use a power driver, or substitute RTV for clamp load.
- [x] Confirm and acquire the gravity-fill vent hose: purchased `10 mm ID` food-grade silicone tube and matching clamps; verify unrestricted rise and overflow during final fill test.
- [~] Gravity-fill camper-wall hatch penetration installed successfully on `2026-07-28`. Finish the `1.5 in` fill-hose connection and unrestricted `10 mm` vent rise only after the tank returns to final orientation, then leak/overflow-test the flange, hose, clamps, and vent behavior before panel closure.
- [ ] Hard-mount the compact plumbing pack: tank shutoff, suction flex, strainer, pump, discharge flex, RecPro double-FIP hose, accumulator, YVSKM female-swivel PEX-B outlet, then one ordinary tee branching to faucet cold while the straight leg continues to the rear BLUE service valve.
- [~] Owner reports the sink/faucet fittings are received. Inspect the EFIELD faucet adapters' gasket/seat/markings, stage both faucet adapters plus the installed YVSKM accumulator swivel, and retain the remaining swivels as spares; prove the sink interfaces on a temporary plywood counter before the final walnut exists.
- [~] First clean-water function pass completed: the `12V` pump, accumulator, tank, interior hot/cold PEX, and rear open ball-valve endpoints all operated correctly outside the camper, with no visible leaks observed at those joints. It did not prove the later-installed sender: the `2026-07-27` inverted test produced a major sender-gasket leak after the under-ring thread failure. Repeat the full test only after sender rework and fill/rear-port installation, with the compartment dry and paper indicators at every joint; verify sender seal, gravity fill/vent, pump cycling, accumulator behavior, pump-assisted tank emptying, and every fitting/seam.
- [ ] Keep the low south tank boss unopened or use only a low-profile plug at the entry footpath. Use pump discharge through the fully open BLUE service outlet for routine tank emptying, with removable upstream suction flex as the dead-pump gravity fallback. Separately drain/winterize the pump, strainer, accumulator, BLUE/RED trunks, supplied Joolca hoses, and HOTTAP; add regulated blowout access only if installed geometry proves gravity draining insufficient.
- [ ] Do not add a manifold rail, antifreeze pickup, quick-disconnect unions, or three-valve heater bypass by default; preserve a known cooler/panel/frame disassembly path instead.
- [ ] Add pump electrical connector and strain relief.
- [ ] Add shallow removable leak tray/pan under pump/strainer/accumulator area.
- [ ] Add leak sensor or at least a visible inspection point.
- [~] Hot/cold PEX reaches the sink zone and terminates at accessible ball valves/final `90` fittings. Before the final countertop exists, make a scrap-plywood counter template and mount the real sink/faucet long enough to prove bowl, clips, drain, shank/nut, pull-out-hose sweep, and adapter clearance. Terminate the faucet hoses with the received EFIELD `1/2 in PEX-B x 3/8 in OD compression male` adapters; use no PTFE tape at either compression seat.
- [x] Interior service topology now has the direct BLUE cold-out and RED hot-return bulkheads/QDs installed and working. The BLUE source retains its accessible ball valve; RED intentionally runs without a valve because the removable heater-return hose is its disconnect and the fixed leg terminates only at faucet hot. No electric-heater branch, manifold, or bypass remains.
- [x] Use the camper BLUE port plus supplied `4 m` Joolca hose and shower handle/head as the pump-fed cold moto sprayer; no separate cold-spray branch is required.
- [x] Keep the exterior shower removable: supplied `4 m` hose from HOTTAP outlet to handle/head in shower mode, or from camper BLUE directly to handle/head in cold-spray mode. No permanent hot splitter or additional camper branch.
- [ ] Build graywater cassette/drain path with winterizable/waterless trap strategy.
- [~] Owner reports an additional in-truck leak/function test, with no new leak reported. Treat it as interim evidence only: after the KUS rebuild, BLUE/RED bulkheads, fill/vent closeout, and sink terminations change the circuit, dry the compartment completely, pressurize to pump cutoff with every outlet closed, place dry paper indicators at each joint, verify no unexplained pump cycling, and repeat inspection after dwell and pressure cycles.
- [ ] Recheck all clamps/unions after first drive.
- [x] Finalize hot water as propane-only Joolca HOTTAP V2 directly mounted outside the rear box; electric storage/tankless branches are closed. Preserve the supplied `5 m` shower assembly (`4 m + 1 m` red sections). The direct camper-port prototype is now installed and working.
- [x] Purchase one HOTTAP V2 Essentials, one Quick-Release HOTTAP Bracket, and one HOTTAP V2 Mount Cover (`2026-07-26`); receipt, inspection, and physical fit remain open.
- [x] RAINPAL `SSBF020` bulkheads and HQMPC brass male QDs are installed; owner reports correct quick-disconnect operation. Projection is substantial but accepted because the owner-designed clicked-on travel caps latch and release correctly.
- [~] The `27 mm / 1-1/16 in` shank openings and enlarged rear-fiberglass access relief are complete. Confirm the final local aluminum load backing, exposed laminate/core edge seal, locknut witness marks, and no looseness after hose pull/cycle testing and the first drive.
- [ ] [HOLD] After the HQMPC/Joolca fit passes, mock one approximately `30 in` potable-rated `3/4 in F-GHT x M-GHT` cold leader with verified female QD sockets at both ends. Verify a relaxed service loop, BLUE labeling, flow/ignition, drainability, and cold-pressure integrity; do not cut the supplied red hose.

## 8. AC/DC electrical closeout and tests

Goal: make the already-live electrical system safe, labeled, restrained, and tested in the camper/module context.

- [ ] Confirm main `48V` disconnect operation and shutdown sequence label.
- [ ] Confirm MultiPlus `I/O/II` behavior and safe default state.
- [ ] Confirm SmartShunt/SOC behavior with final battery bank connection.
- [ ] Remount the MultiPlus and combined AC breaker enclosure into the embedded backer T-nuts; confirm torque/thread engagement, service clearance, cable support, and covers before energizing.
- [ ] Remount the MultiPlus/AC enclosure in its final backer location for stationary work, then mock the complete L5-30 inlet-to-AC-in-breaker `10/3` route from both sides. The Galley tie is not required for stationary endpoint proof, but do not cut until bend radius, hidden structure, sealing land, backer grommet/gland, and independent strain relief are all proven; do not drive until integrated anti-rack/road restraint is complete.
- [~] Orion is mounted/wired; simplify its `48V` input to Lynx Slot 4 with `1x` verified `40A` MEGA (`58VDC` minimum under the locked `56.8V` charge ceiling; Victron `CIP138040020 40A/80V` is the replacement fallback) feeding the existing `6 AWG` pair directly. Remove/bypass the separate inline input fuse holder, retire standalone `F-06`, torque Lynx and Orion terminals to current manufacturer values, tug-test, and strain-relieve the pair.
- [ ] Identify the physically X-marked/misrated Lynx fuse by slot before replacement: Slot 2 requires `F-03 60A/80V` for MPPT; Slot 4 / `F-05` requires `40A` MEGA body-marked at least `58VDC` for Orion. Remove/quarantine any `32V`-rated fuse from the energized `48V` system.
- [ ] Verify `F-07 60A/80V` MEGA remains in the separate Orion `12V` output holder and is not confused with Lynx Slot 4 input protection.
- [~] Complete/verify the `12V` buffer path: `4 AWG battery + -> F-11 100A ANL -> SW-12V-BATT -> panel main +`; `4 AWG battery - -> panel main -` directly.
- [ ] Replace the Orion always-on remote jumper with a maintained SPST dry-contact switch between `L-H`. Label the operating sequence: loads off -> Orion remote off/status confirmed -> `SW-12V-BATT` open; startup reverses the source order by closing `SW-12V-BATT` before enabling Orion.
- [ ] Resolve the voltage-instrument discrepancy before unattended charging: existing meter reported `18V` while VictronConnect reported about `13.5V`. Disable Orion, replace the meter battery or use a known-good second meter, verify at the battery posts, then compare battery-post/Orion-output/app readings after re-enabling. Any verified value above the configured `14.20V` absorption target is a stop condition.
- [ ] Confirm 12V junction loads and branch labeling.
- [ ] Confirm Cerbo power, VE.Bus/RJ45, Wi-Fi/console access, and source label `Shore power`.
- [ ] Confirm AC-in path: portable EMS, shore cord, L5-30 inlet, AC-in breaker, MultiPlus.
- [ ] Before sustained shore charging or AC-out use, bond the MultiPlus external `M6 PE` lug to a verified truck-chassis point with `10 AWG` green stranded copper (`4 mm²` manual minimum). Add a separate corrosion-compatible aluminum-shell bond to the same equipment-ground network; do not leave the MultiPlus PE open or use shell/80/20 as its only path.
- [ ] Keep AC and DC grounding roles separate: no jumper from MultiPlus case/PE to Lynx negative or the `12V` negative bus, and no fixed downstream neutral-ground bond. Leave the MultiPlus internal ground relay enabled for normal inverter/shore transfer behavior.
- [ ] After Mechman ground style is physically identified, verify whether its case-ground plus dedicated `2/0` negative establishes the house-negative/chassis reference and confirm no parallel chassis path bypasses the SmartShunt.
- [ ] Commission AC-out branches only when the AC enclosure, breakers, grounding/bonding behavior, and GFCI receptacles are physically ready.
- [ ] Test GFCI trip/reset on both intended AC branch areas: office and galley.
- [ ] Test DC USB/PD outlets under realistic laptop/phone/tablet load.
- [~] Owner confirms the camper lights operate from the live `12V` junction; still verify final branch/fuse label and dimmer behavior on `12V-06`.
- [~] Owner confirms the camper fan operates from the live `12V` junction; still verify the `12V-10` branch/fuse label and all installed speed/direction/control functions.
- [ ] Wire and prove the first two DC charging outlets only after their branch fuse values, polarity, and labels are confirmed.
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

Goal: release the permanent floor from cure, preserve the hardpoints, and protect the finish through utilities-first module reinstall.

- [x] Glue the one-piece Lonseal to the three-piece `3/4 in` plywood floor with #650 on the evening of `2026-07-15`.
- [x] Accept that the finish now bridges both plywood seams; floor removal requires cutting the vinyl and is not part of the active plan.
- [~] Hold lifted perimeter areas with bolted boards during cure.
- [ ] Back out/clean/reinstall each temporary clamp bolt one at a time with hand/low-speed control before adhesive-contaminated threads become permanent; stop if a rivnut spins or stainless threads bind.
- [ ] Owner accepts Saturday-morning module loading; protect the surface and stop only if an area is actually loose.
- [ ] After cure, remove boards and photograph the complete floor before loading it.
- [ ] Inspect every edge and hardpoint; classify stable cosmetic waviness vs raised/hollow/loose areas, and check board/washer imprinting.
- [ ] Do not cut/inject/heat/aggressively reroll during cure. After cure, accept stable cosmetic irregularity or define a localized repair before modules hide it.
- [ ] Protect Lonseal with clean hardboard/cardboard/blankets during every extrusion/module/battery move; never drag parts across it.
- [x] Hard-mount the electrical module first, using the registered rivnuts and verified support path. Initial hard mount is complete; integrated anti-rack/final road restraint remains a separate closeout gate.
- [ ] Install the tank/restraint and other heavy modules only after their support/service gates pass; no heavy module depends on plywood alone.
- [ ] Torque/witness-mark final module fasteners, then perform a low-consequence shakedown and inspect/retorque for insert spin, vinyl indentation, moisture, abrasion, leaks, or module shift.

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

- [~] Standard 4 X is in hand as of owner report `2026-07-31`. Bench-activate it on the supplied AC path, inventory/measure the real terminal/cable/connector/router/power-supply stack, and stage the indoor equipment in the ventilated tech cubby before locking direct-DC conversion or permanent roof-mount details.
- [ ] Confirm cable route from office electronics to DC/AC power without knee snags.
- [ ] Add temporary task light if final lighting is deferred.
- [ ] Add red/amber night strip only if the wiring path is already clean and non-blocking.
- [ ] Confirm fan/window/vent access remains usable after modules are placed.
- [ ] Freeze the LF Bros heater envelope before final battery-cable landing: body horizontal/upright, at least `4 in` clear at rear cabin-air intake, unrestricted front warm-air outlet, and every clamp/plug serviceable without battery removal.
- [ ] Reject the electrical-backer exhaust route. Dry-fit a sealed metal floor turret/plate directly beneath the heater, inspect both sides for bed ribs/crossmembers/vehicle lines/wiring, and let that physical part control the layered-floor cut. LF Bros' simple-flat-metal reference is `2x 30 mm` combustion holes plus four stud holes, not an automatic Hiatus cut pattern.
- [ ] Mock the entire outside combustion path before drilling: exhaust with slight continuous fall and broad sweeps, muffler entirely outside, separate combustion intake protected from spray, intake/exhaust ends facing different directions, and metal stand-offs/shielding from fuel, wiring, plastic, undercoating, and openings.
- [ ] Mount the supplied `10 L` tank upright outside the open battery/electrical bay or in sealed externally vented spill containment. Drill only `7-8 mm` through the center of its molded lower boss for the supplied pull-through nozzle—do not cut out the apparent `3/4-1 in` pad and do not put the pump in the tank.
- [ ] Mock fuel order `tank -> filter -> external pump -> heater`; rubber-mount the pump close to tank, within `2 m` of heater, outlet toward heater and about `45 degrees` upward. Preserve filter, pump, clamps, and bottom-tank fitting access.
- [ ] Route the harness branches before closing the battery bay: main heater plug, pump two-pin lead, T4S controller lead, and fused `12V +/-`. The remote is wireless/no-cut; mount T4S away from the hot outlet. Preserve 12V power through commanded cooldown and verify actual `C-22` length/startup voltage before retaining short-run `14 AWG / 15A` or upgrading to `12 AWG`.
- [ ] [DEFER] Final QuinLED/WLED lighting install unless core modules are stable.
- [ ] [DEFER] Camper audio package; do not spend July 4 sprint time on it.

## 14. Solar research and procurement

Goal: keep solar out of the critical path until roof/module constraints are real.

- [~] Reopen solar layout work now; keep final panel procurement/string lock downstream of the measured Starlink/fan/mount roof layout, MPPT validation, cable/service path, and charging-priority review.
- [~] Reopen the roof layout now that Standard 4 X is in hand: map the fan, side rails, measured Starlink/mount service envelope, shadows, cable exit, popup service loop, flexible-panel trays, drainage, and the `75 lb` roof-panel cap as one system.
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
- [ ] Before travel reliance, assemble the purchased Dr.Roc spare-hoist/lug-wrench kit, operate the actual F-350 spare hoist by hand, verify lug-socket fit and stowage, and test-raise the measured spare. Do not impact-drive the hoist or work beneath a suspended tire.
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

## Friday `2026-07-31` through Sunday `2026-08-02`

| Window | Primary objective | Realistic output | Do not get sucked into |
| --- | --- | --- | --- |
| Fri evening `2026-07-31` | Clear truck position, then establish protected `48V -> Orion -> 12V` power | Pump-drain tank; isolate/cover electrical; remove or strap loose tank/Galley/gear; make the minimum on-property truck turn; remount MultiPlus/AC enclosure only after the truck is parked; record `12V` battery voltage and prove Orion charging from isolated Battery 1 if needed | Public-road travel; moving after heavy equipment is remounted; paralleling unmatched batteries |
| Sat morning `2026-08-01` | Close out the stationary electrical core | Verify Orion `F-05 40A >=58VDC` in Lynx Slot 4, remove the extra inline input fuse, verify `F-07 60A/80V` output and `F-11 100A` buffer branch, then test lights, fan, pump, DC outlets, and fridge branch one at a time | Alternator first-charge; cosmetic wire perfection; final long shell-dependent cable cuts |
| Sat afternoon/evening `2026-08-01` | Charge/match batteries while clearing reversible wet-side work | Charge Battery 2 and Battery 3 individually as needed; rest/record all three; build the real sink/faucet plywood mockup; test Joolca/HQMPC latch/retention/flow; bench-test/measure Starlink; stage KUS tools and bulkhead backing | Hard-mounting Galley before KUS/rear-port access clears; solar shopping spiral |
| Sun `2026-08-02` | Integrate only the systems that passed | Parallel the `3x 48V` bank only at `<=0.1V`; rebuild/bench-prove KUS if the ring arrives; cut/install BLUE/RED only if cutter, Joolca/QD, backing, and route all pass; finish fill/vent and final dry leak test; then tie Galley/Bench/electrical for road restraint. Draft the measured fan + Starlink + solar roof layout only after those gates | Roof holes, final solar purchase, HOTTAP permanent cuts, or public-road travel before restraint gates pass |

### Sunday-night win condition

1. Truck is parked in the workable orientation; MultiPlus/AC enclosure is remounted, covered, and usable for controlled shore charging.
2. Orion demonstrably charges the `12V` buffer and the fan/lights/pump/DC/fridge branches are individually fused and function-tested.
3. Batteries 2 and 3 are charged/rested; the bank is paralleled only if the `<=0.1V` gate passes.
4. KUS, BLUE/RED ports, fill/vent, sink, and Galley are completed only where delivered hardware and physical tests clear them; otherwise the blocked interface is left removable and documented.
5. The truck either has complete integrated road restraint or remains explicitly immobilized; Starlink has passed a bench test and the roof work ends at a measured fan + Starlink + solar layout, not new holes.

**Build order:** drain/secure/turn truck -> stationary electrical remount -> Orion/`12V` proof -> individual battery charging/matching -> KUS/rear-port/sink completion as parts permit -> Galley/electrical road restraint -> Starlink/solar roof-layout decision -> Mechman dead rough-in only as stretch work.

## Do not prioritize next unless the gate above is already green

- Cosmetic floor repair before the `72 hr` cure and full inspection distinguish stable waviness from loose/raised areas.
- Further tank or service-port drilling based only on garage-floor convenience; finish the remaining installed-geometry, backing, hose/QD, and service-path checks first.
- Bench bridge/lid or service-obscuring furniture before the `3x 48V` bank is individually charged/rested, equalized within `0.1V`, electrically paralleled/commissioned, protected, covered, labeled, and removable.
- Remaining shore, BLUE/RED service, HOTTAP, or roof holes before their complete inside routes/endpoints and physical fit gates are proven.
- Alternator first-charge.
- Final solar purchase or roof penetration.
- Permanent Quick-Release HOTTAP Bracket mount, cylinder cradle/vents, generic restraint-bracket acceptance, or BLUE/RED service-plate cuts before their package mockup and structural/load-path gates pass.
- Cosmetic skins everywhere.
- Permanent monitor mechanism perfection.
- Final lighting design.
- Audio system.
- Decorative finish work.

## Hard holds

- [HOLD] Do not load over an actually loose floor area; otherwise protect the Lonseal and proceed Saturday morning.
- [HOLD] No public-road travel until the hard-mounted electrical module also has its integrated anti-rack/final road-restraint path complete, torqued, witness-marked, and inspected. One minimum low-speed on-property reposition is acceptable only before remounting the heavy MultiPlus/AC equipment and after the tank is drained, batteries are isolated/covered, and the loose tank, Galley, and shop gear are removed or positively strapped.
- [HOLD] The sender hole has been cut, but no final tank installation, closure, or water service proceeds until the seized screw and damaged `FLS-U` ring are removed, the sender is rebuilt with a new main gasket and matched hardware, the sealing land/flange pass inspection, and a static wetting/inverted bench test shows no leakage. The installed gravity-fill hatch still requires final tank orientation, fill/vent hose geometry, backing inspection, and overflow/leak testing before service.
- [HOLD] No final sink/faucet terminal cuts or rear service-port shell holes until the purchased EFIELD/YVSKM adapters are accepted; the actual Joolca hose passes the HQMPC latch/retention/flow test; and the real sink/faucet/drain, RAINPAL bulkheads, backer thickness, and minimum-fitting geometry are mocked at full scale.
- [HOLD] Do not install a projecting gravity-drain valve on the low south tank boss in the entry footpath. Leave it unopened or low-profile plugged; use BLUE as the pump-assisted emptying outlet and removable upstream suction flex as the failed-pump gravity fallback. Exterior shower/cold spray uses the removable Joolca `4 m` hose and handle/head rather than a camper manifold.
- [HOLD] No permanent Quick-Release HOTTAP Bracket mount, cylinder cradle, box vents, service-plate cut, regulator service hatch, or HOTTAP V2 Mount Cover closeout until the purchased Joolca core package and selected Flame King package pass physical box/operating-clearance mockup and manual/listing review.
- [HOLD] No battery-bench bridge/lid or obstructing upper structure until the `3x 48V` bank is individually charged/rested, equalized within `0.1V`, electrically paralleled/commissioned, protected, covered, labeled, and removable with emergency access preserved.
- [HOLD] No alternator first-charge until APM, fusing, WS500 config, sensors, bank readiness, and shutdown behavior are ready.
- [HOLD] No final countertop sink cutout until faucet/drain/rail clearance is physically proven.
- [HOLD] No premium black walnut final cuts until plywood templates, support tabs, service access, entry sweep, and finish sample are approved.
- [HOLD] No final panels over electrical/plumbing until labels, strain relief, leak/functional tests, and service access pass.
- [HOLD] No shore inlet cut until the hard-mounted electrical endpoint, inside AC-in path, backing, bend radius, service access, and strain relief are physically proven.
- [CLOSED `2026-07-28`] Gravity-fill hatch penetration installed successfully after in-truck fitment. Final hose hookup/service remains held until tank orientation, fill and highest-point vent ports, continuous hose fall/vent rise, service access, backing, and overflow/spill behavior are physically proven.
- [HOLD] No HOTTAP water-service or roof/solar exterior penetration until both exterior geometry and inside service/routing/strain-relief paths are physically proven; no propane line enters the camper in the selected exterior-heater/rear-box-cylinder package.
