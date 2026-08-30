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

As-of: `2026-08-30`

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

- Owner-reported overnight `2026-08-02/03`: the electrical module, Galley/cooler support, water tank, and reinstalled Bench extrusion are hard-mounted. The integrated structure is very stiff. Before public-road release, positively restrain the `3x 48V` batteries, separate `12V` battery, ICECO, air fryer, bench lid, monitor/laptop hardware, and every other heavy/rigid cargo item; also finish terminal covers and cable support.
- The driver-rear shore inlet and exterior-to-module cable route are installed. One accessible, enclosed, conductor/gauge-rated three-wire `L/N/PE` splice into the AC-input side remains before dead checks and controlled first use; preserve strain relief, PE continuity, AC-in/AC-out neutral isolation, and the `10A` first-test / `12A` maximum policy on a normal household `15A` source.
- All three `48V` batteries' positive/negative `2/0 AWG` branch leads are cut, lugged, heat-shrunk, and landed at the battery-side busbars. Battery 1 completed the corrected `20A`-cap cycle; Battery 2 resumed and reached absorption on `2026-08-03`; Battery 3 remains pending. Keep them isolated through individual charge/rest recording and make the permanent parallel connection only when maximum-to-minimum rested terminal voltage is `<=0.1V`.
- Owner report `2026-08-02`: the Orion charges the `12V` buffer battery and the camper `12V` system is operating correctly. The final topology remains one verified `F-05 40A >=58VDC` input fuse in Lynx Slot 4, `F-07 60A/80V` on Orion output, and `F-11 100A` on the buffer-battery branch; `SW-12V-BATT` isolates only the buffer battery while Orion is disabled.
- Owner report `2026-08-03`: all three passenger-rear water penetrations are physically installed and the replacement KUS `FLS-U` under-ring, main gasket, and matched hardware are installed and look correctly seated. The two-wire sender cable is run to the Cerbo area but not yet terminated. For the installed US-range KUS sender, use one numbered Cerbo Tank column: KUS black/signal to upper `DATA`, KUS pink/return to lower `GND`; the owner's red extension mapped to pink therefore lands on `GND`, despite the counterintuitive red color. Final water-system acceptance still waits for Cerbo setup/full-system leak proof, final fill/vent hookup, sink termination, and one dry-compartment pressure/dwell inspection after every disturbed joint is closed.
- Owner report `2026-08-27`: Starlink Standard 4 X is operational from the installed fixed-body pass-through/retractile jumper and switched `12V` conversion branch through a `20A` blade fuse. The fridge and pump are wired and switched. Three independent charging branches are installed: one driver-side `100W` outlet and two passenger-side `65W` outlets, each separately fused. Four duplex `120V` devices are wired—one GFCI origin plus one downstream device on each of the driver and passenger branches, for four plug positions per side. These are physical/build-progress facts; only Starlink is explicitly reported function-tested. Final labels, DC polarity/load/drop, AC boxes/clamps/covers, `LINE/LOAD`, PE, polarity, and GFCI trip/reset remain open.
- Owner purchase `2026-08-28`: E-Moto Rack Complete Dual E-Moto Carrier System for truck/e-moto transport. Receipt and inspection are pending. Before carrying the Talaria, prove `2 in` receiver fit, Warp 9 peg interface, anti-rattle/fastener setup, RangeMax swingout and rear-clearance geometry, and progressive loaded road acceptance.
- The Galley/cooler support, Bench tie, electrical module, and tank are no longer free-floating. The tank is retained by two metal straps into truck-bed-wall plusnut locations. Keep sender access and the known disassembly path. The truck remains a no-drive worksite until batteries, ICECO, air fryer, bench lid, monitor/laptop hardware, and all other heavy/rigid cargo have positive restraint and exposed-terminal/cable protection is complete.
- The shore shell cut/installation gate is closed. Hold energization only until the remaining AC-in splice is enclosed and strain-relieved, `L/N/PE` and breaker routing match the locked topology, PE continuity and no unintended neutral-ground bond are meter-proven, and the source-side EMS/current-limit setup is ready.
- Final surface direction remains a three-piece black-walnut commission with a mid-September routing appointment. Bring the actual sink and soap dispenser; do not route the walnut until the bowl, drain body, faucet/soap shanks and hoses, support rails, tank clearance, service path, and drain slope are physically proven.
- Plumbing is active closeout work. Prior pre-final owner reports recorded clean-water function through the pump/accumulator/rear endpoints; the current `2026-08-27` update confirms only that the pump branch is wired and switched. Hold routine water service until the installed branch load test, rebuilt sender, final fill/vent/sink joints, and dry-area pressure/dwell inspection pass.
- Alternator charging remains a separate commissioning gate. The main owner-reported remaining package is `F-04 200A/80V`, both temperature sensors, final protection/support, and WS500 profile read/save/program through the purchased USB-A-to-B cable before controlled first charge.
- Immediate safety task: replace the hanging/tape-covered switch bundle with one narrow removable plywood/ABS service face. Individually insulate and label every DC switch contact; mount the `120V` receptacle in a listed covered box with conductor restraint and PE continuity, physically separated from DC terminals.
- Adhesive cable raceway/zip-tie bases are accepted as routing aids, not structural road-load support. Use T-slot anchors/P-clamps or equivalent structural redundant restraint at exits, direction changes, connectors, service loops, and on the exterior PV run so adhesive alone never carries spring, wind, or branch load.
- Starlink's installed route and direct-DC conversion work. Retain the complete OEM cable for recovery and remove/stow the roof equipment for tight brush. Perform final label, connector-cap/retention, spray, roof-motion, loaded-heat, and post-drive inspection before calling the route travel-accepted.
- All four Renogy `175W` panels have arrived. One-panel physical test-fit plus measured layout indicates coexistence with Starlink/MaxxAir and near-total roof use. Keep one `4S1P` string on the Victron `150/45`; direct bonding waits on exact silicone/substrate preparation, coupon/cure proof, and one-panel shakedown. The PV retractile cord is ordered; verify its exact conductors, OD/gland fit, ratings, tangents, spring force, and full `28 in` roof stroke on receipt.
- The LF Bros heater is the main unresolved systems install. The EVIL ENERGY `10 gal` diesel tank/feed/vent package and CaLeQi `60 mm / 2.37 in` stainless turret are purchased, and the LF Bros `10 L` plastic tank is reassigned to graywater. The turret depth is acceptable only after a physical underside check: dry-fit the LF Bros studs/gasket to the delivered plate, measure the actual `125 mm` skirt and weld, place it skirt-down on the finished-floor plane, and verify that its projected depth plus intake/exhaust pipe sweeps clear the truck tank, fuel/EVAP/brake lines, wiring, crossmembers, undercoating, and road exposure before making the single round penetration. Do not stack the original flat plate. Heat-shield sheet is secondary edge protection, not the primary turret wall or CO/weather seal.

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

### Next-shop-day integration ladder — `2026-08-27`

1. **Make the switch/service face safe first:** de-energize correctly, cut one narrow removable plywood/ABS face, hard-mount and label every DC switch, individually insulate terminals, and put the `120V` device in its own listed covered box with clamps/PE and physical AC/DC separation.
2. **Close the working branches:** audit actual fuse slots/values; load-test Starlink, fridge, pump, and all three DC charging outlets; then inspect all four AC boxes/devices and prove GFCI origin `LINE/LOAD`, downstream protection, polarity, continuous PE, and trip/reset under inverter and shore power.
3. **Use the next dry weather for solar prep:** inspect received labels/connectors, wash/decontaminate the roof, prove the exact structural-silicone stack and cure on a coupon, finalize all-panel templates/cord routing, then attach and shakedown one panel before repeating.
4. **Verify the PV cord before drilling:** on receipt confirm conductors, OD/gland, `>=150VDC` wet/UV/cold/coiled rating, tangent geometry, spring force, and full roof/cab articulation. Preserve `4S1P`; only two free string ends enter the two-pole transition/cord/disconnect/MPPT path. Use structural clamps/guarding; adhesive guides are secondary.
5. **Dry-lay heater and storage as one package:** map the sealed turret and complete underside exhaust/intake/fuel path around the truck fuel tank, vehicle lines, wiring, undercoating, and combustibles. Keep exhaust/muffler outside and fuel exterior or in sealed externally vented containment. Do not install the rear storage module first.
6. **Prepare the mid-September walnut appointment:** take the real sink and soap dispenser. Prove drain body, faucet/soap hardware, support, tank, service clearances, and continuous slope; mock a vented, positively retained, normally closed removable vessel around `2.5 gal` before locking graywater.
7. **Finish alternator and road restraint before skins:** fit `F-04`, both temperature sensors, final support/protection, back up the WS500 profile before programming, and run controlled first charge. Then finish battery/ICECO/air-fryer/bench-lid/monitor restraint, mock the actual chair/`24 in` desk/aisle, and close panels last.

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

- [~] Current individual-charge state: Battery 1 completed the corrected `20A`-cap cycle through `56.8V` absorption and `54.0V` float without a BMS trip; Battery 2 resumed and reached absorption on `2026-08-03`; Battery 3 remains pending. SmartShunt SOC is stale across physical battery swaps and should not be used as the per-battery charge gate.
- [ ] Bring the `3x 48V` house batteries to a compatible resting voltage/SOC before paralleling; stage the separate `12V` buffer battery independently.
- [x] Cut, lug, adhesive-heat-shrink, and land all three batteries' positive/negative `2/0 AWG` branch cables at the battery-side busbars while the bay is open.
- [x] Charge Battery 1 individually through the proven MultiPlus shore-charge path; it reached about `56.76V` / `0A` in absorption and then `54.06V` float without an observed BMS protection event. Allow it to rest and record terminal voltage.
- [~] Charge Battery 2 individually through the proven MultiPlus shore-charge path, then allow it to rest and record terminal voltage; owner reports it resumed from the prior upper-`54V` bulk state and reached absorption on `2026-08-03`.
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
- [~] Add battery restraints: build a low extrusion perimeter with dividers/hard stops so each case is captured fore/aft and side-to-side, then use individual low-stretch straps over the cases to anchored extrusion/T-slot points. Tie the restraint frame into the hard-mounted Bench/electrical extrusion or through-bolted structural plywood with backing; do not rely on wood screws into plywood alone, and do not route straps across terminals, displays, or sharp case edges.
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
- [x] Add bench/desk tie-in rails or brackets so the electrical module cannot wobble standalone; owner reports the removed Bench extrusion is reinstalled between the electrical and Galley/cooler modules and the integrated structure is extremely stiff.
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
- [~] The electrical/Bench/Galley structure is no longer freestanding; hold road travel only until the heavy batteries/cooler are positively restrained and high-current terminals/cables are covered and supported.

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
- [ ] Record any changed Desk/storage dimensions from the `2026-07-06` test install in the changed-dimensions log before updating the fabricator/template packets.
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
- [ ] Build or mock a padded stow cradle at or below roof-safe height; contact safe bezel/back/VESA structure, not the LCD face.
- [ ] Add hard stops so the monitor arm is unloaded in travel and no ratchet/bungee pressure is applied through the screen.
- [ ] Add positive travel latch/pin/strap for monitor and laptop carriage/angle/stow state; elastic restraint is secondary.
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
- [x] Mock passenger-side fridge/cooler position with real handles, hinge/lid swing, cord bend, and hand clearance; the real cooler now sits on the hard-mounted extrusion support.
- [ ] Confirm raised fridge/cooler height target, currently about `16 in` above floor/service zone.
- [ ] Confirm relationship to `36 gal` wheel-well tank envelope.
- [x] Build the lofted fridge/cooler support skeleton as a service exoskeleton, not a sealed cabinet.
- [x] Tie Galley to Bench/electrical structure with removable plates/bolts reachable from the aisle/top/service openings; owner reports the integrated frame and returned Bench extrusion are hard-mounted and very stiff.
- [~] Add positive fridge/cooler travel restraint and hard stops. Use the cooler's foot-level tie points with a low-stretch cam strap to the support extrusion rather than over-tightening a ratchet strap across the case; add one aisle-side hard stop and a closed-cell/EPDM bumper at the camper-wall contact area.
- [ ] Preserve lower cool-air intake and upper warm-air exhaust around fridge compressor vents.
- [ ] Confirm pump/accumulator/strainer/manifold service opening below/near fridge.
- [ ] Confirm wet bay cannot leak into battery/electrical bays; add partition/drip tray concept.
- [~] Place the actual Sarlai `15 in x 15 in` topmount sink and soap dispenser on the final counter template for the mid-September routing appointment.
- [ ] Confirm final walnut Galley dimension/template, support tabs, sink/soap cutouts, and no-drill zones before travel.
- [ ] Confirm black-walnut counter support-tab/fastener locations before routing; do not rely on cosmetic skins to carry the slab.
- [ ] Check actual faucet/soap shank/nut/hose, sink bowl, drain body, rail, tank, and service clearances.
- [~] Graywater vessel selected: repurpose the never-fueled LF Bros `10 L / 2.64 gal` plastic tank as a vented, positively retained removable cassette with cleanout access and a normally closed outlet. Prove its location, full removal path, and continuous drain slope with the real sink/drain stack.
- [ ] Check Duxtop induction cooktop storage/use position and cord route.
- [ ] Build the Ninja SP151 travel cubby with shelf lip/hard stops plus a positive strap/latch; pressure-sensitive tape alone is not accepted. Restrain basket/rack/pan against chatter and remove any conspicuous soft separator before heating.
- [ ] Add removable service-panel edges into the skeleton while framing.
- [ ] [HOLD] Do not cut final countertop sink opening until skeleton and faucet/drain clearance are physically confirmed.

## 7. Plumbing rough-in and test

Goal: build and test the fixed cold-water pack plus the selected propane-only BLUE cold-out / RED hot-return interface; keep every joint serviceable and leak-testable.

- [x] Record owner-confirmed physical geometry: four molded ports on each end, two visibly large and two smaller per end, with no obvious/open top port.
- [ ] Photograph/inventory the eight end ports, identify exact threads/model markings, inspect for a membrane-covered top boss, and temporarily label candidate functions: gravity fill, highest-point vent, pump outlet, drain, sender, spare/plug.
- [ ] Measure internal sender clearance at the exact KUS location and confirm a flat top area over the deepest unobstructed section; do not rely on the nominal `16 in` exterior depth alone.
- [ ] Lay out the gravity-fill hose, vent hose, pump outlet, drain, KUS sender, restraint brackets, and compact pump/accumulator pack around the empty tank on the workbench.
- [~] In-truck wet-spine fitment has progressed through final tank placement and physical restraint: owner reports two metal straps are tightened into the truck-bed-wall plusnut locations and the surrounding Galley/Bench structure is hard-mounted. Preserve sender-opening access, pump-board access, fill/vent bends, leak path, and the accepted whole-Galley tank-removal sequence. Any plusnut screw that did not achieve clean full thread engagement is a rework item before first drive; otherwise witness-mark and recheck the strap hardware after the first loaded drive.
- [ ] Freeze the tank port map after dry fit. Current default is upper large end port for gravity fill, highest suitable upper small end port for unrestricted vent/overflow, low north port for pump suction, and no projecting valve at the low south footpath boss; require continuous downhill fill-hose routing and continuous vent rise without a trapped low loop.
- [x] Select the KUS sender backing method: KUS/Wema `FLS-U` stainless SAE five-hole C-ring under-ring with the main sender gasket and matched long `FLS-U` screws; do not rely on self-tapping screws or sealant alone. The separate KUS gasket-mounting kit includes short screws with bonded metal/rubber sealing washers, while the official `FLS-U` manual depicts the long under-ring screws without transplanted washers. Do not peel or transfer loose rubber pieces between the two screw sets.
- [ ] Inventory the KUS electrical handoff before tank closure: locate the Cerbo GX MK2 factory `Tank` terminal block, confirm enough `18-22 AWG` duplex from sender to Cerbo, and stage two sealed pigtail splices plus two Cerbo-end ferrules. Wire black signal and pink return to the same numbered Tank-input column; no external power, fuse, chassis ground, analog gauge, or GX Tank 140.
- [ ] Bench-check the sender across its two leads before mounting (`~240 ohm` float down/empty, `~30-33 ohm` float up/full). After wiring, enable `Tank 1` at `Settings -> Integrations -> Tank and Temperature Sensors`, then set `Fresh Water`, `36 US gal`, and the US `240-30 ohm` sender standard; refine the custom tank shape only after measured fills.
- [x] Purchase the exact `2-3/8 in` / `60 mm` KUS-sender hole saw (BOM row `239`, ordered `2026-07-24`); procurement does not clear the cut gate.
- [x] Acquire the water-penetration cutters (`27 mm / 1-1/16 in` carbide cutter for the BLUE/RED RAINPAL service ports, `1-1/2 in` for the selected large-boss membrane field-fit, and `3-1/4 in` for the IZTOR camper-wall hatch) plus supplemental `1/2 in` PEX-B `90` elbows and cinch clamps (`2026-07-26`). The tank-boss cutter must visibly clear the internal threads before use.
- [x] The `60 mm / 2-3/8 in` sender opening was cut and the first `FLS-U` installation failed after an under-ring thread stripped/galled; the damaged hardware was recovered without enlarging the opening.
- [x] Owner report `2026-08-03`: replacement `FLS-U` ring, main gasket, and matched long screws are installed and look correctly seated. Keep the sender exposed through the next leak proof; visual fit does not replace the dry pressure/dwell acceptance test.
- [x] Confirm and acquire the gravity-fill vent hose: purchased `10 mm ID` food-grade silicone tube and matching clamps; verify unrestricted rise and overflow during final fill test.
- [~] Gravity-fill camper-wall hatch penetration installed successfully on `2026-07-28`. Finish the `1.5 in` fill-hose connection and unrestricted `10 mm` vent rise only after the tank returns to final orientation, then leak/overflow-test the flange, hose, clamps, and vent behavior before panel closure.
- [ ] Hard-mount the compact plumbing pack: tank shutoff, suction flex, strainer, pump, discharge flex, RecPro double-FIP hose, accumulator, YVSKM female-swivel PEX-B outlet, then one ordinary tee branching to faucet cold while the straight leg continues to the rear BLUE service valve.
- [~] Owner reports the sink/faucet fittings are received. Inspect the EFIELD faucet adapters' gasket/seat/markings, stage both faucet adapters plus the installed YVSKM accumulator swivel, and retain the remaining swivels as spares; prove the sink interfaces on a temporary plywood counter before the final walnut exists.
- [x] Prior pre-final clean-water function pass: pump, accumulator, tank, interior PEX, and rear open ball-valve endpoints operated outside the final installed closeout with no visible leaks at those joints. Preserve this as dated subsystem evidence, not current installed pump-branch acceptance; repeat loaded electrical and dry-compartment pressure/dwell tests after final terminations/joints.
- [ ] Keep the low south tank boss unopened or use only a low-profile plug at the entry footpath. Use pump discharge through the fully open BLUE service outlet for routine tank emptying, with removable upstream suction flex as the dead-pump gravity fallback. Separately drain/winterize the pump, strainer, accumulator, BLUE/RED trunks, supplied Joolca hoses, and HOTTAP; add regulated blowout access only if installed geometry proves gravity draining insufficient.
- [ ] Do not add a manifold rail, antifreeze pickup, quick-disconnect unions, or three-valve heater bypass by default; preserve a known cooler/panel/frame disassembly path instead.
- [ ] Add pump electrical connector and strain relief.
- [ ] Add shallow removable leak tray/pan under pump/strainer/accumulator area.
- [ ] Add leak sensor or at least a visible inspection point.
- [~] Hot/cold PEX reaches the sink zone and terminates at accessible ball valves/final `90` fittings. Before the final countertop exists, make a scrap-plywood counter template and mount the real sink/faucet long enough to prove bowl, clips, drain, shank/nut, pull-out-hose sweep, and adapter clearance. Terminate the faucet hoses with the received EFIELD `1/2 in PEX-B x 3/8 in OD compression male` adapters; use no PTFE tape at either compression seat.
- [x] Interior service topology now has the direct BLUE cold-out and RED hot-return bulkheads/QDs installed and working. The BLUE source retains its accessible ball valve; RED intentionally runs without a valve because the removable heater-return hose is its disconnect and the fixed leg terminates only at faucet hot. No electric-heater branch, manifold, or bypass remains.
- [x] Use the camper BLUE port plus supplied `4 m` Joolca hose and shower handle/head as the pump-fed cold moto sprayer; no separate cold-spray branch is required.
- [x] Keep the exterior shower removable: supplied `4 m` hose from HOTTAP outlet to handle/head in shower mode, or from camper BLUE directly to handle/head in cold-spray mode. No permanent hot splitter or additional camper branch.
- [~] Build the graywater path around the selected never-fueled LF Bros `10 L` tank: inventory the actual basket/tailpiece, then mock a compact waterless trap and continuously falling `3/4-1 in` smooth-wall sink-drain hose into a top inlet. Keep the existing `1/2 in` clear hose for the dump leg only. Preferred low-outlet candidate is Banjo `TF050` gasketed `1/2 FNPT` bulkhead (`1-5/8 in` cutout) -> `HB050` `1/2 MNPT x 1/2 in` barb -> short clear hose -> accessible full-flow `LVHB050V` `1/2 in` barbed valve; do not buy/drill until the tank has enough flat gasket land/internal access and the hose is physically confirmed `1/2 in ID`. Keep the valve normally closed and the discharge end capped in travel; discharge only where allowed.
- [~] A prior additional in-truck leak/function test was reported with no new leak observed; it is not part of the new `2026-08-27` branch-functional evidence. After fill/vent closeout and sink terminations, dry the compartment, complete the installed pump electrical load/voltage-drop test, pressurize to cutoff with every outlet closed, place dry paper indicators at each joint including the sender, verify no unexplained cycling, and repeat after dwell/cycles.
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
- [~] Owner reports `C-31` Desk/office and `C-32` Galley AC branches each have one GFCI origin plus one downstream duplex, for four duplex devices/eight plug positions total. Before routine use, verify breaker values, `12 AWG` continuity, all listed boxes/covers/clamps/fill, first-device `LINE/LOAD`, downstream protection label, polarity, continuous PE, and trip/reset in inverter and shore modes.
- [~] Owner reports `C-20` Starlink works on its switched `20A` branch; `C-21` ICECO/fridge and `C-23` SHURflo are wired/switched; and the three charging branches are installed (`1x` driver `100W`, `2x` passenger `65W`, each separately fused). Audit and label actual source slots/fuses, polarity, switch state, loaded voltage drop, terminal insulation, and endpoint restraint.
- [~] Owner reports `C-48` KUS-to-Cerbo is wired. Verify both ends, confirm black/signal -> upper `DATA` and pink/red-extension -> lower `GND` in one Tank column, then configure/test the `240-33 ohm` fresh-water reading before closeout.
- [x] Downstream AC device count is closed at one additional duplex per branch. Continue each from the first GFCI's `LOAD`, label `GFCI Protected`, preserve continuous PE, and retest the whole chain. More receptacles do not add branch capacity; sequence induction/toaster and other high-draw Galley loads.
- [ ] Mount the circular plug-in Desk outlet/USB/PD module only after underside depth, cord bend, clamp, heat, spill, and service access are proven. Plug it into a fixed GFCI-protected receptacle; do not hardwire it or use it as the Starlink power path.
- [ ] If access will close, provision `C-22` LF Bros heater with `12 AWG` duplex / `15A` while preserving controller-commanded cooldown power, and `C-24` listed CO alarm with `18 AWG` duplex / `3A` on an always-on branch.
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
- [~] Owner reports all three DC charging outlets are wired and separately fused. Load-test the driver `100W` and both passenger `65W` endpoints with realistic devices; verify labels, polarity, branch fuse, conductor support, heat, and voltage drop.
- [~] Owner reports the switched fridge/cooler feed is wired. Verify switch-off behavior, polarity, loaded voltage drop, terminal insulation, and positive cooler restraint.
- [~] Owner reports the switched pump branch is wired. Verify fuse, connector, supported service loop, switch behavior, prime/cycle, leak inspection, and dry-run awareness.
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
- [ ] Land positive at Lynx Slot 3 / `F-04 200A/80V MEGA` house-bank end.
- [ ] Land dedicated negative return to the Lynx/house negative return path; do not rely on sheet metal/chassis only.
- [ ] Insert Wakespeed `500A/50mV` shunt on the battery side of the hard-mounted SmartShunt in the common battery-negative path: `battery -> Wakespeed shunt -> SmartShunt -> Lynx`; purple/high battery side, grey/low SmartShunt/Lynx side; confirm all returns remain on the system side.
- [ ] Mount WS500 near house electrical board/battery/shunt area for short sense wiring.
- [ ] Wire brown ignition/enable from Ford Upfitter `#3` through `F-15 3A`. Row `176` holder/mixed-fuse stock is purchased; confirm an exact `3A` fuse plus received 16 AWG holder/wire markings and splice fit before installation.
- [ ] Wire PH-VAN red from the `F-04` alternator/load-side stud through the Eaton/Bussmann `HEB-AA` + Littelfuse `KLKD015.T` `15A/600VAC/DC` in-line branch; secure it in the loom with no DC fuse panel or DIN enclosure; wire PH-VAN black to Lynx/system negative.
- [ ] Wire blue field lead through Mechman adapter.
- [ ] Dead-end/protect unused yellow stator/tach unless explicitly required.
- [ ] Protect unused yellow/green CAN connector unless compatible CAN/BMS integration is later added.
- [ ] Install alternator temperature sensor and battery temperature sensor if profile requires.
- [ ] Use the purchased 6 ft USB-A-to-B cable to read and record the Mechman-supplied WS500 profile before changing anything; first verify the cable carries data, then confirm `500A/50mV`, `Shunt at Battery`, charge ceiling, field derate, and conservative first-run current/field limit.
- [ ] First run: Upfitter `#3 OFF`, start engine, verify no unexpected charging.
- [ ] First charge: enable only with meter/app ready and abort plan understood; Upfitter `#3 OFF` must stop current.
- [ ] Measure charge-path and return-path voltage drop under load; target `<0.1V` each per Mechman first-run guidance.
- [ ] Log resting voltage, charging voltage/current, alternator temp, battery temp, WS500 profile, warnings, and shutdown behavior.
- [ ] [HOLD] Do not first-charge from alternator this weekend unless batteries, fusing, APM, WS500 config, sensors, and shutdown behavior are all ready.

## 10. Flooring / Lonseal / hardpoints

Goal: preserve the installed permanent floor and registered hardpoints while finishing/removing modules.

- [x] Glue the one-piece Lonseal to the three-piece `3/4 in` plywood floor with #650 on the evening of `2026-07-15`.
- [x] Accept that the finish bridges both plywood seams and that heavy modules are now installed; the earlier cure/loading hold is historical, not an active weekend gate.
- [ ] Monitor known edges/hardpoints after wet/dusty drives and module work. Investigate only actual loose/expanding areas, moisture/dust trails, swelling, insert spin, or floor movement; do not reopen the floor speculatively.
- [ ] Protect Lonseal with clean hardboard/cardboard/blankets during every extrusion/module/battery move; never drag parts across it.
- [x] Hard-mount the electrical module first, using the registered rivnuts and verified support path. Initial hard mount is complete; integrated anti-rack/final road restraint remains a separate closeout gate.
- [x] Install and restrain the `36 gal` tank within the hard-mounted Galley structure. Keep sender/fittings accessible and prove water acceptance separately.
- [ ] Torque/witness-mark final module fasteners, then perform a low-consequence shakedown and inspect/retorque for insert spin, vinyl indentation, moisture, abrasion, leaks, or module shift.

## 11. Panels, skins, latches, storage, and travel retention

Goal: add only the panels/features that make the system safer, stiffer, more serviceable, or visually intentional before cosmetic closure. Detailed feature choices live in `docs/implementation/INTERIOR_finish_paneling_and_feature_choices.md`.

- [ ] Map every Galley/Bench/desk face as `finished wood`, `service removable`, `smoked/translucent feature`, or `open/exposed 80/20`.
- [ ] Identify panels that are structural/shear/anti-rack vs cosmetic covers.
- [ ] Prioritize panels that brace electrical module, bench, desk, and galley skeleton.
- [ ] Use `1/2 in` plywood for most living-facing vertical/removable faces; use `3/4 in` for tops, bench lids, cooler-bearing surfaces, step/load surfaces, and large horizontal spans.
- [~] Prepare measured templates/dimension packets for the mid-September walnut routing; bring the real sink and soap dispenser. Do not allow routing/cutouts until support, drain, tank, service, hinge, and no-drill geometry pass.
- [ ] Prepare the fabricator's dimension packet: Galley live-edge counter/template, Desk top template, L-shaped Bench/lid template, support tabs, hinge line, latch points, and any cutout/no-drill zones.
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

- [~] Standard 4 X is operating from the installed fixed-body pass-through/retractile jumper and switched `12V` converter branch through a `20A` blade fuse. Finish label, cap/retention, spray, loaded heat/dropout/reboot, full roof-motion, and post-drive inspection before travel acceptance; retain the OEM cable for direct recovery.
- [ ] Confirm cable route from office electronics to DC/AC power without knee snags.
- [ ] Add temporary task light if final lighting is deferred.
- [ ] Add red/amber night strip only if the wiring path is already clean and non-blocking.
- [ ] Confirm fan/window/vent access remains usable after modules are placed.
- [ ] Dry-fit the LF Bros heater and rear driver-side storage module together before installing either. Preserve at least `4 in` at the rear cabin-air intake, unrestricted front warm-air outlet, and every clamp/plug service point.
- [ ] Survey the complete underside before drilling: actual turret footprint, bed ribs/crossmembers, truck fuel tank, fuel/EVAP/brake lines, wiring, undercoating, plastics, and service access. Use a sealed metal turret/plate; the heat shield is supplemental and does not release a route next to the truck tank.
- [ ] Mock the entire outside combustion path before drilling: exhaust/muffler fully outside with slight fall and broad sweeps, intake protected from spray, ends facing different directions, and real clearance plus noncombustible standoffs/guards from vehicle fuel systems, wiring, undercoating, plastics, and openings.
- [x] Purchase the EVIL ENERGY `10 gal` aluminum diesel tank/feed/vent package (`2026-08-30`, BOM row `65`). The LF Bros `10 L` plastic tank is no longer fuel storage and must remain never-fueled for graywater use.
- [ ] Inventory the delivered diesel tank before fit-up: verify filler cap/gasket and whether the cap is sealed or vented, both lower `-10AN` outlets/caps, both upper `-10AN` ports, sender leads/resistance, all purchased adapters/valve/hose, and no shipping damage. The remote rollover valve must be the only atmospheric vent path unless the cap vent has equivalent rollover shutoff. Do not buy duplicate caps unless delivered inventory disproves the listing imagery.
- [ ] Mock one lower feed as `-10AN -> 1/8 NPT adapter -> shutoff -> 3/16 in barb -> short LF Bros black rubber connector -> original 5 mm OD / 2 mm ID rigid line -> filter -> external pump -> heater`. Leave the other lower outlet capped; rubber-mount the pump near the tank with its outlet toward the heater and about `45 degrees` upward.
- [ ] Use diesel-rated thread sealant only on tapered NPT joints per its instructions. AN connections seal at the flare seat: inspect those seats and put no tape/sealant on AN threads. Leak-check a small outdoor test fill before service.
- [ ] Mock one upper port capped with the freed lower cap and the other as `-10AN -> 5/16 in barb -> NBR hose -> upright remote rollover vent outside`. Exterior tank mounting is preferred; any interior location requires liquid-tight externally vented containment, roughly `86 lb` full-load restraint, protected fill/shutoff/line routing, and isolation from living/electrical/general storage.
- [ ] Bench-meter the passive sender, then use one unused Cerbo Tank `DATA/GND` pair with no `12V` feed. Configure `Diesel`, `10 US gal`, and custom approximately `3 ohm empty / 90 ohm full` only after the real endpoints/direction are confirmed.
- [ ] Route the harness before closing the zone: heater, pump, T4S, fused `12V +/-`. Preserve commanded cooldown power and verify actual `C-22` length/startup voltage before retaining `14 AWG / 15A` or upgrading to `12 AWG`.
- [ ] [DEFER] Final QuinLED/WLED lighting install unless core modules are stable.
- [ ] [DEFER] Camper audio package; do not spend July 4 sprint time on it.

## 14. Solar research and procurement

Goal: fit and commission the purchased `700W` Renogy array without turning it into an unsafe secondary roof.

- [x] Record purchase: `4x Renogy 175W flexible monocrystalline = 700W`, purchased `2026-08-12`; BOM uses the `$616.90` discounted net item subtotal and excludes `$44.73` estimated tax.
- [~] Electrical planning screen: current official G2 data give `4S = 78.0V Vmp / 95.6V Voc / 9.50A Isc`; published-coefficient cold Voc is `114.86V` at `-40C`. The maximum-voltage screen passes, but estimated hot-start margin becomes negligible around `70C` before route drop; exact received labels and hot restart/tracking remain required.
- [~] Planning geometry: measured `138 x 63 in` fiberglass, centered MaxxAir, and `0.625 in` track step remain active. Current solver evidence finds no all-inside packing within the screened constraints; the candidate has two inside-skin panels and one direct-mount panel crossing each side track, using the real roof lands. Add a small local spacer/taper only if the actual panel mockup shows a sharp crease.
- [~] Received/geometry: all four panels are on hand; one-panel physical test-fit plus measured layout indicates compatibility with Starlink and MaxxAir while using nearly the full roof. Photograph/record all four labels, exact SKU, dimensions/weight, junction boxes/leads/connectors/polarity/grommets, and the controlling installation manual; then place full `1:1` templates and cycle fan/Starlink service.
- [ ] Wash/decontaminate the roof and verify the exact structural-silicone product, substrate/backsheet preparation, cure window, drainage, and representative coupon. On one panel, pass static/heat/water/roof-cycle proof with temporary independent track-anchored test restraint; then private low-speed testing with inspection stops; then a deliberate staged-speed road-acceptance test. Routine highway use and remaining panel bonds wait until that sequence passes.
- [ ] Lock the `4S1P` series mates/extensions, two free string-end leads, compact two-pole transition, ordered retractile cord, structural clamps/guard, fixed compression gland above the Starlink entry, two-pole load-break, short fixed `12 AWG` two-conductor run, labels, and MPPT entry. No combiner or `F-09` string fuse is presently planned for the one string.
- [~] PV retractile cord is owner-reported ordered. On receipt verify exact conductor count/gauge, OD/gland fit, `>=150VDC`, wet/UV/cold/coiled ampacity, tangents, spring force, and full `28 in` roof stroke plus cab/bed articulation before drilling. Adhesive zip-tie bases may guide only; structural redundant supports carry motion/wind/branch loads.
- [ ] Measure route drop and complete cool-start plus stationary hot-roof restart/tracking commissioning near the configured battery-charge target.
- [ ] **Installation release:** do not attach the remaining panels or begin routine highway travel until received-label, actual-weight, final-route, exact cure, one-panel static/heat/water/roof-cycle proof, temporary independent test restraint, private low-speed test, controlled staged-speed road acceptance, full-motion, and hot-operation gates pass.

Canonical decision and coordinates: `docs/studies/SOLAR_configuration_matrix.md`.

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

- [ ] Install/mock the rear storage module, real chair, knees, and roughly `24 in` desk together before trimming cabinetry or top. Try the folding/stowed-chair option first; shrink toward `20 in` only if measured seated and entry/aisle tests still fail.
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
- [ ] Receive and install the ordered removable bug screens. Owner-confirmed `2026-08-05` inside fixed-opening measurements are rear `55.5 in W x 44.25 in H` and passenger-side `57.5 in W x 19.75 in H`. Rear order is a Yotache custom `60 in W x 46 in H` black thickened screen with middle magnetic opening, giving `2.25 in` nominal side overlap and `1.75 in` top overlap with the bottom flush. Passenger order is a Risareyi black thickened screen, actual `24 in x 64 in`, installed rotated `90 degrees` as `64 in W x 24 in H` so its magnetic seam runs horizontally; centered over the opening it gives `3.25 in` nominal side overlap and about `2.125 in` top/bottom overlap.
- [ ] Dry-fit and cycle the passenger hatch before applying permanent adhesive. The paired fixed strut/bracket obstructions project about `1.5 in`; routing the rotated `64 in` screen around that contour nominally leaves about `1.75 in` of attachment allowance per side. Use hook-and-loop only on fixed bracket backs/frame surfaces, clear the moving strut rods and gasket/compression path, and add adhesive-backed loop to the screen's reinforced former-bottom hem only if rotation exposes an unbacked perimeter edge. Do not cut or sew the purchased screen unless the no-modification fit test fails and the owner explicitly changes direction.
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

## Current order — `2026-08-30`

1. **Switch/service safety:** build the narrow removable face; separately box AC; insulate and label every DC switch terminal.
2. **Branch closeout:** audit/test Starlink, fridge, pump, three DC charging outlets, and both two-device AC/GFCI chains.
3. **Solar weather window:** verify received labels/connectors and exact silicone/cure; prep roof; prove one panel before all four; verify the ordered cord and full-motion route before the new gland hole.
4. **Heater/storage package:** dry-fit heater, sealed turret, underside exhaust/intake/fuel path, fuel containment, pump, and rear module before drilling or installing cabinetry.
5. **Mid-September walnut:** bring real sink and soap dispenser; prove support/drain/tank/service geometry; then mock the continuously falling `3/4-1 in` drain, top inlet/vent, retention/removal, and low dump valve around the selected never-fueled LF Bros `10 L / 2.64 gal` cassette.
6. **Alternator:** fit `F-04`, both temperature sensors, support/protection, save/program WS500 profile, and run controlled first charge.
7. **Measured furniture and travel restraint:** preserve the `24 in` desk until the real chair/aisle mockup; positively restrain batteries, ICECO, air fryer, bench lid, monitor, and laptop; panel only after functional/service gates pass.

## Do not prioritize next unless the gate above is already green

- Cosmetic skins or final panel closure before heater, drain, electrical, leak, and access-dependent tests.
- Cutting the desk/storage by estimate before the real chair/aisle mockup.
- Attaching all solar panels before exact adhesive/cure and one-panel shakedown proof.
- Diesel-heater drilling based on heat shield alone or before the complete underside vehicle-line/fuel-tank survey.
- Alternator first charge before `F-04`, APM, WS500 profile, sensors, bank readiness, and shutdown behavior.
- Air-fryer tape-only retention or ratcheting/bungeeing directly against an LCD.
- Final lighting or audio ahead of safety/commissioning/road-restraint work.

## Hard holds

- [MONITOR] Permanent floor is in service. Protect Lonseal and investigate only actual loose/expanding areas, moisture/dust evidence, insert spin, or floor movement; do not retain the historical cure-weekend hold as current guidance.
- [HOLD] No public-road travel until batteries, ICECO, air fryer, monitor/laptop hardware, bench lid, and other heavy/rigid cargo have positive restraint; remaining terminal/cable protection is complete; critical fasteners are torqued/witness-marked; and a first-drive inspection plan is ready.
- [HOLD] The KUS replacement ring/gasket/hardware are installed. Keep sender access open and withhold final water closeout until fill/vent, sink terminations, and one dry pressure/dwell proof show no sender/fitting leakage or unexplained pump cycling.
- [HOLD] Rear BLUE/RED penetrations are installed and working. Hold final sink/walnut cuts until the real sink, soap dispenser, drain body, faucet hoses, support rails, tank clearance, and continuous-slope graywater path are mocked; hold final rear water/heater closeout until backing, hose pull/cycle, Joolca clearance, and leak/flow tests pass.
- [HOLD] Do not install a projecting gravity-drain valve on the low south tank boss in the entry footpath. Leave it unopened or low-profile plugged; use BLUE as the pump-assisted emptying outlet and removable upstream suction flex as the failed-pump gravity fallback. Exterior shower/cold spray uses the removable Joolca `4 m` hose and handle/head rather than a camper manifold.
- [HOLD] No permanent Quick-Release HOTTAP Bracket mount, cylinder cradle, box vents, service-plate cut, regulator service hatch, or HOTTAP V2 Mount Cover closeout until the purchased Joolca core package and selected Flame King package pass physical box/operating-clearance mockup and manual/listing review.
- [HOLD] No battery-bench bridge/lid or obstructing upper structure until the `3x 48V` bank is individually charged/rested, equalized within `0.1V`, electrically paralleled/commissioned, protected, covered, labeled, and removable with emergency access preserved.
- [HOLD] No alternator first-charge until APM, fusing, WS500 config, sensors, bank readiness, and shutdown behavior are ready.
- [HOLD] No final countertop sink cutout until faucet/drain/rail clearance is physically proven.
- [HOLD] No premium black walnut final cuts until plywood templates, support tabs, service access, entry sweep, and finish sample are approved.
- [HOLD] No final panels over electrical/plumbing until labels, strain relief, leak/functional tests, and service access pass.
- [CLOSED CUT / HOLD ENERGIZATION `2026-08-02`] Driver-rear shore inlet and cable route are installed. Do not energize through the new permanent path until the remaining accessible AC-in `L/N/PE` splice is enclosed with listed conductor/gauge-rated hardware, both cable sides are strain-relieved, topology and PE continuity pass dead checks, AC-in/AC-out neutrals remain isolated, and the first source is EMS-protected with the MultiPlus limited to `10A`.
- [CLOSED `2026-07-28`] Gravity-fill hatch penetration installed successfully after in-truck fitment. Final hose hookup/service remains held until tank orientation, fill and highest-point vent ports, continuous hose fall/vent rise, service access, backing, and overflow/spill behavior are physically proven.
- [HOLD] Starlink penetration is installed and working. No PV gland hole or all-panel bond/travel acceptance until exact cord/gland/inside-route geometry, structural strain relief, received-panel labels/connectors, exact silicone/cure, one-panel shakedown, full roof/cab motion, and hot-operation tests pass. No propane line enters the camper in the selected exterior-heater package.
