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

# Live Build Checklist — Remaining Systems + Interior Completion

As-of: `2026-09-02`

Owner: Sunny / Dane

Maintainer rule: **update this file whenever the practical build state, sequence, blocker list, or next physical step changes.** Keep it as the live punch list; do not let stale chat notes become the checklist of record.

## Purpose

This is the active running checklist for the working post-install Hiatus/F-350 camper. It preserves the July 4 sprint record, but the current queue now centers on solar, heater/fuel, alternator enable/programming, sink/graywater, HOTTAP receipt, and interior completion.

It does **not** replace the owner docs:

- Overall sequence: `docs/plans/PROJECT_build_order_of_operations.md`
- Interior/galley baseline: `docs/implementation/INTERIOR_furniture_layout_and_galley.md`
- Workstation/monitor detail: `docs/implementation/INTERIOR_driver_side_workstation.md`
- Flooring/Lonseal gate: `docs/implementation/FLOORING_subfloor_build_process.md`
- Alternator install/commissioning: `docs/implementation/ELECTRICAL_Mechman_WS500_APM48_install_guide.md`
- Decisions/risks/open questions: `docs/core/TRACKING.md`

## Current build posture

- Owner report `2026-09-02`: the `3x 48V` bank has been paralleled for an extended period, and the `12V`, `48V`, and `120V` systems have all seen regular use.
- All `120V` work is in enclosures, including all four duplex outlet boxes, and the owner confirms the MultiPlus is grounded to truck chassis. Do not reopen the physical box-count or chassis-ground installation tasks; retain verification of the installed MultiPlus `M6 PE` bond, the separate conductive-shell bond, GFCI `LINE/LOAD`/downstream trip, polarity, PE continuity, and neutral isolation.
- The batteries and ICECO are positively restrained. Remaining interior/cargo work is the not-yet-installed air fryer, Bench lid, monitor/laptop travel state, and other storage.
- Fresh-water plumbing, the KUS sender, and the `35 gal` tank are complete and have been used extensively. Remaining wet work is the sink after the mid-September counter work and the separate graywater system; leak-check the new sink joints when installed.
- Final surfaces are two live-edge Bubinga pieces: `48 in` Galley and `47 in` Desk. The earlier three-piece black-walnut concept is superseded. The FLEXISPOT Foldex chair is ordered and awaits installed fit/aisle acceptance.
- Solar fixed-side work is complete through the pass-through, two-pole disconnect, stationary wiring, and MPPT landing. No panels are connected. Remaining work is roof preparation/caulk-bonding, series wiring, exterior support, and controlled commissioning of the `4S1P` array.
- Alternator charging remains disabled. The owner reports the remaining install/configuration work as the protected PH-VAN red lead and Wakespeed read/save/programming before controlled first charge.
- The LF Bros heater, sealed floor turret, EVIL ENERGY `10 gal` tank/cradle/fill/vent, combustion route, fuel route, and rear driver-side storage module remain one coupled installation package.
- The HOTTAP has not arrived. Propane geometry is mocked; final appliance/bracket/cylinder integration, manual-clearance proof, leak test, and first burn wait on receipt.
- The existing camper has completed a successful owner-reported shakedown. Solar, heater/fuel, HOTTAP, alternator charging, and newly added interior retention still need their own post-install checks.
- The hanging DC switch bundle still needs a labeled removable service face if that finish-state work has not already been completed. Individually insulate all contacts and keep it physically separate from the now-enclosed AC work.
- Starlink's installed route and direct-DC conversion are operational. Retain the OEM cable for recovery and remove/stow exposed roof equipment for tight brush.

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

### Historical next-shop-day integration ladder — `2026-08-27`; superseded `2026-09-02`

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

Goal: maintain the now-operational parallel bank and preserve safe service access.

- [x] Owner report `2026-09-02`: all three `48V` batteries have been paralleled and in regular service for an extended period. The earlier Battery 2/3 isolated-charge staging sequence is historical, not an active build gate.
- [x] All three batteries' positive/negative `2/0 AWG` branch cables are fabricated and landed.
- [x] Batteries are positively restrained.
- [ ] Confirm/record final extraction access, terminal covers, polarity, branch protection, torque/witness marks, and SmartShunt bank-capacity configuration during the next de-energized service window.

## 2. Bench / battery / step module

Goal: finish the Bench lid/step without degrading battery service access.

- [x] Bench/electrical/Galley structure is hard-mounted, integrated, and owner-reported very stiff.
- [x] Batteries are positively restrained in the Bench area.
- [ ] Build and positively latch the Bench lid; add edge/scuff protection where it serves as a step.
- [ ] Confirm the lid/upper structure preserves battery extraction plus Class T/disconnect/Lynx/shunt/fuse access.
- [ ] Add final torque/witness marks and use only removable skins around electrical service points.

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
- [~] Reconfirm driver-side desk depth near the wheel well; the final top is a `47 in` live-edge Bubinga piece, with roughly `24 in` depth retained until installed fit says otherwise.
- [~] FLEXISPOT Foldex ordered; on receipt, fully lower/fold it and mock seated elbow height plus the five-star base against the Desk, wheel well, and aisle.
- [ ] Check knee/foot clearance around wheel well and electrical step projection.
- [~] Place rough desktop or template at target height.
- [ ] Confirm entry/exit movement and hip/shoulder clearance.
- [ ] Confirm roof-down sweep envelope for desk, DC shelf, monitor stow block, and cable loops.
- [ ] Record any changed Desk/storage dimensions from the `2026-07-06` test install in the changed-dimensions log before updating the fabricator/template packets.
- [x] Desktop material/length selected: `47 in` live-edge Bubinga. Preserve the seated-fit, support, roof-sweep, finish, and entry-clearance gates before final mounting.
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
- [ ] Confirm relationship to `35 gal` wheel-well tank envelope.
- [x] Build the lofted fridge/cooler support skeleton as a service exoskeleton, not a sealed cabinet.
- [x] Tie Galley to Bench/electrical structure with removable plates/bolts reachable from the aisle/top/service openings; owner reports the integrated frame and returned Bench extrusion are hard-mounted and very stiff.
- [x] ICECO/fridge travel restraint is owner-confirmed complete.
- [ ] Preserve lower cool-air intake and upper warm-air exhaust around fridge compressor vents.
- [ ] Confirm pump/accumulator/strainer/manifold service opening below/near fridge.
- [ ] Confirm wet bay cannot leak into battery/electrical bays; add partition/drip tray concept.
- [~] Place the actual Sarlai `15 in x 15 in` topmount sink and soap dispenser on the `48 in` live-edge Bubinga Galley template for the mid-September routing appointment.
- [ ] Confirm the `48 in` Bubinga Galley template, support tabs, sink/soap cutouts, and no-drill zones before routing.
- [ ] Confirm counter support-tab/fastener locations before routing; do not rely on cosmetic skins to carry the slab.
- [ ] Check actual faucet/soap shank/nut/hose, sink bowl, drain body, rail, tank, and service clearances.
- [~] Graywater vessel selected: repurpose the never-fueled LF Bros `10 L / 2.64 gal` plastic tank as a vented, positively retained removable cassette with cleanout access and a normally closed outlet. Prove its location, full removal path, and continuous drain slope with the real sink/drain stack.
- [ ] Check Duxtop induction cooktop storage/use position and cord route.
- [ ] Air fryer is not installed: build the Ninja SP151 travel cubby with shelf lip/hard stops plus a positive strap/latch; restrain basket/rack/pan against chatter.
- [ ] Add removable service-panel edges into the skeleton while framing.
- [ ] [HOLD] Do not cut final countertop sink opening until skeleton and faucet/drain clearance are physically confirmed.

## 7. Plumbing rough-in and test

Goal: preserve the completed/operational fresh-water system, then add the sink and graywater without disturbing proven work.

- [x] Owner report `2026-09-02`: fresh plumbing, the KUS sender, and the `35 gal` tank are complete and have been used extensively. The older discovery, sender-wiring, and general pressure/dwell items below are historical rather than active water-service holds.
- [ ] After the Bubinga counter work, install the sink/faucet/soap-dispenser terminations and leak-check only the new or disturbed joints.
- [ ] Build, vent, retain, and spill-test the separate graywater system.

- [x] Record owner-confirmed physical geometry: four molded ports on each end, two visibly large and two smaller per end, with no obvious/open top port.
- [x] Historical tank-port discovery, KUS clearance, fill/vent, pump, and accumulator layout work is complete in the installed system.
- [~] In-truck wet-spine fitment has progressed through final tank placement and physical restraint: owner reports two metal straps are tightened into the truck-bed-wall plusnut locations and the surrounding Galley/Bench structure is hard-mounted. Preserve sender-opening access, pump-board access, fill/vent bends, leak path, and the accepted whole-Galley tank-removal sequence. Any plusnut screw that did not achieve clean full thread engagement is a rework item before first drive; otherwise witness-mark and recheck the strap hardware after the first loaded drive.
- [x] Installed tank port map, fill, vent, pump suction, and low-profile footpath posture are operational.
- [x] Select the KUS sender backing method: KUS/Wema `FLS-U` stainless SAE five-hole C-ring under-ring with the main sender gasket and matched long `FLS-U` screws; do not rely on self-tapping screws or sealant alone. The separate KUS gasket-mounting kit includes short screws with bonded metal/rubber sealing washers, while the official `FLS-U` manual depicts the long under-ring screws without transplanted washers. Do not peel or transfer loose rubber pieces between the two screw sets.
- [x] KUS/Cerbo wiring, setup, and real-use behavior are owner-confirmed complete.
- [x] Purchase the exact `2-3/8 in` / `60 mm` KUS-sender hole saw (BOM row `239`, ordered `2026-07-24`); procurement does not clear the cut gate.
- [x] Acquire the water-penetration cutters (`27 mm / 1-1/16 in` carbide cutter for the BLUE/RED RAINPAL service ports, `1-1/2 in` for the selected large-boss membrane field-fit, and `3-1/4 in` for the IZTOR camper-wall hatch) plus supplemental `1/2 in` PEX-B `90` elbows and cinch clamps (`2026-07-26`). The tank-boss cutter must visibly clear the internal threads before use.
- [x] The `60 mm / 2-3/8 in` sender opening was cut and the first `FLS-U` installation failed after an under-ring thread stripped/galled; the damaged hardware was recovered without enlarging the opening.
- [x] Owner report `2026-08-03`: replacement `FLS-U` ring, main gasket, and matched long screws are installed and look correctly seated. Keep the sender exposed through the next leak proof; visual fit does not replace the dry pressure/dwell acceptance test.
- [x] Confirm and acquire the gravity-fill vent hose: purchased `10 mm ID` food-grade silicone tube and matching clamps; verify unrestricted rise and overflow during final fill test.
- [x] Gravity fill/vent and compact plumbing pack are installed and in regular use.
- [~] Owner reports the sink/faucet fittings are received. Inspect the EFIELD faucet adapters' gasket/seat/markings, stage both faucet adapters plus the installed YVSKM accumulator swivel, and retain the remaining swivels as spares; prove the sink interfaces against a temporary template before routing the final Bubinga Galley piece.
- [x] Fresh-water tank, pump, accumulator, interior PEX, rear service ports, and KUS have passed sustained owner use. Repeat leak checks only after sink installation or other disturbed joints.
- [ ] Keep the low south tank boss unopened or use only a low-profile plug at the entry footpath. Use pump discharge through the fully open BLUE service outlet for routine tank emptying, with removable upstream suction flex as the dead-pump gravity fallback. Separately drain/winterize the pump, strainer, accumulator, BLUE/RED trunks, supplied Joolca hoses, and HOTTAP; add regulated blowout access only if installed geometry proves gravity draining insufficient.
- [x] No manifold rail, antifreeze pickup, quick-disconnect unions, or three-valve heater bypass is needed in the completed fresh-water baseline; preserve the known service/disassembly path.
- [x] Pump electrical connection and normal operation are owner-confirmed complete.
- [~] A removable leak tray/sensor remains an optional refinement, not a plumbing-completion gate.
- [~] Hot/cold PEX reaches the sink zone and terminates at accessible ball valves/final `90` fittings. Before the final countertop exists, make a scrap-plywood counter template and mount the real sink/faucet long enough to prove bowl, clips, drain, shank/nut, pull-out-hose sweep, and adapter clearance. Terminate the faucet hoses with the received EFIELD `1/2 in PEX-B x 3/8 in OD compression male` adapters; use no PTFE tape at either compression seat.
- [x] Interior service topology now has the direct BLUE cold-out and RED hot-return bulkheads/QDs installed and working. The BLUE source retains its accessible ball valve; RED intentionally runs without a valve because the removable heater-return hose is its disconnect and the fixed leg terminates only at faucet hot. No electric-heater branch, manifold, or bypass remains.
- [x] Use the camper BLUE port plus supplied `4 m` Joolca hose and shower handle/head as the pump-fed cold moto sprayer; no separate cold-spray branch is required.
- [x] Keep the exterior shower removable: supplied `4 m` hose from HOTTAP outlet to handle/head in shower mode, or from camper BLUE directly to handle/head in cold-spray mode. No permanent hot splitter or additional camper branch.
- [~] Build the graywater path around the selected never-fueled LF Bros `10 L` tank: inventory the actual basket/tailpiece, then mock a compact waterless trap and continuously falling `3/4-1 in` smooth-wall sink-drain hose into a top inlet. Keep the existing `1/2 in` clear hose for the dump leg only. Preferred low-outlet candidate is Banjo `TF050` gasketed `1/2 FNPT` bulkhead (`1-5/8 in` cutout) -> `HB050` `1/2 MNPT x 1/2 in` barb -> short clear hose -> accessible full-flow `LVHB050V` `1/2 in` barbed valve; do not buy/drill until the tank has enough flat gasket land/internal access and the hose is physically confirmed `1/2 in ID`. Keep the valve normally closed and the discharge end capped in travel; discharge only where allowed.
- [x] Owner reports extensive installed water use and a good camper shakedown with no new water defect reported. Inspect the new sink/graywater work after installation rather than reopening the completed fresh-water system.
- [x] Finalize hot water as propane-only Joolca HOTTAP V2 directly mounted outside the rear box; electric storage/tankless branches are closed. Preserve the supplied `5 m` shower assembly (`4 m + 1 m` red sections). The direct camper-port prototype is now installed and working.
- [x] Purchase one HOTTAP V2 Essentials, one Quick-Release HOTTAP Bracket, and one HOTTAP V2 Mount Cover (`2026-07-26`); receipt, inspection, and physical fit remain open.
- [x] RAINPAL `SSBF020` bulkheads and HQMPC brass male QDs are installed; owner reports correct quick-disconnect operation. Projection is substantial but accepted because the owner-designed clicked-on travel caps latch and release correctly.
- [~] The `27 mm / 1-1/16 in` shank openings and enlarged rear-fiberglass access relief are complete. Confirm the final local aluminum load backing, exposed laminate/core edge seal, locknut witness marks, and no looseness after hose pull/cycle testing and the first drive.
- [ ] [HOLD] After the HQMPC/Joolca fit passes, mock one approximately `30 in` potable-rated `3/4 in F-GHT x M-GHT` cold leader with verified female QD sockets at both ends. Verify a relaxed service loop, BLUE labeling, flow/ignition, drainability, and cold-pressure integrity; do not cut the supplied red hose.

## 8. AC/DC electrical closeout and tests

Goal: make the already-live electrical system safe, labeled, restrained, and tested in the camper/module context.

- [x] Owner report `2026-09-02`: `12V`, `48V`, and `120V` have seen regular use; all four outlet boxes and the remaining `120V` work are enclosed; the `3x 48V` bank is paralleled; batteries and ICECO are restrained.
- [ ] Keep the specific installed-MultiPlus-ground verification, separate shell-bond, GFCI/polarity, labeling, terminal-cover, and cable-support checks below; do not re-open completed physical enclosure, chassis-ground installation, or battery-staging work.

- [ ] Confirm main `48V` disconnect operation and shutdown sequence label.
- [ ] Confirm MultiPlus `I/O/II` behavior and safe default state.
- [ ] Confirm SmartShunt/SOC behavior with final battery bank connection.
- [x] MultiPlus and the AC breaker/device enclosures are installed; the four outlet boxes are enclosed and in regular use.
- [~] Orion is mounted/wired; simplify its `48V` input to Lynx Slot 4 with `1x` verified `40A` MEGA (`58VDC` minimum under the locked `56.8V` charge ceiling; Victron `CIP138040020 40A/80V` is the replacement fallback) feeding the existing `6 AWG` pair directly. Remove/bypass the separate inline input fuse holder, retire standalone `F-06`, torque Lynx and Orion terminals to current manufacturer values, tug-test, and strain-relieve the pair.
- [ ] Identify the physically X-marked/misrated Lynx fuse by slot before replacement: Slot 2 requires `F-03 60A/80V` for MPPT; Slot 4 / `F-05` requires `40A` MEGA body-marked at least `58VDC` for Orion. Remove/quarantine any `32V`-rated fuse from the energized `48V` system.
- [ ] Verify `F-07 60A/80V` MEGA remains in the separate Orion `12V` output holder and is not confused with Lynx Slot 4 input protection.
- [~] Complete/verify the `12V` buffer path: `4 AWG battery + -> F-11 100A ANL -> SW-12V-BATT -> panel main +`; `4 AWG battery - -> panel main -` directly.
- [ ] Replace the Orion always-on remote jumper with a maintained SPST dry-contact switch between `L-H`. Label the operating sequence: loads off -> Orion remote off/status confirmed -> `SW-12V-BATT` open; startup reverses the source order by closing `SW-12V-BATT` before enabling Orion.
- [x] The old handheld-meter discrepancy is not an active behavior; the Orion/`12V` system has seen regular owner use. Any newly verified value above the configured `14.20V` absorption target remains a stop condition.
- [ ] Confirm 12V junction loads and branch labeling.
- [~] `C-31` Desk/office and `C-32` Galley AC branches are enclosed and in regular use. Retain explicit breaker, first-device `LINE/LOAD`, downstream-protection label, polarity, continuous-PE, and GFCI trip/reset proof in inverter and accepted-shore modes.
- [~] Starlink, ICECO/fridge, pump, and the three DC charging branches have seen regular owner use. Remaining closeout is labels, terminal insulation, conductor support, and any load/drop check not already physically recorded.
- [x] KUS-to-Cerbo setup and tank use are owner-confirmed complete.
- [x] Downstream AC device count is closed at one additional duplex per branch. Continue each from the first GFCI's `LOAD`, label `GFCI Protected`, preserve continuous PE, and retest the whole chain. More receptacles do not add branch capacity; sequence induction/toaster and other high-draw Galley loads.
- [ ] Mount the circular plug-in Desk outlet/USB/PD module only after underside depth, cord bend, clamp, heat, spill, and service access are proven. Plug it into a fixed GFCI-protected receptacle; do not hardwire it or use it as the Starlink power path.
- [ ] If access will close, provision `C-22` LF Bros heater with `12 AWG` duplex / `15A` while preserving controller-commanded cooldown power, and `C-24` listed CO alarm with `18 AWG` duplex / `3A` on an always-on branch.
- [ ] Confirm Cerbo power, VE.Bus/RJ45, Wi-Fi/console access, and source label `Shore power`.
- [x] AC-in path and enclosed `120V` distribution are owner-confirmed operational.
- [x] Owner report `2026-09-02`: the MultiPlus is grounded to the truck chassis; physical installation of that ground is closed.
- [ ] At the next de-energized inspection, verify the installed ground originates at the MultiPlus external `M6 PE` lug, uses at least `4 mm²` / selected `10 AWG` green stranded copper with suitable terminations, and lands at a sound truck-chassis point. Record the endpoint and continuity result rather than rebuilding a confirmed connection blindly.
- [ ] Add or verify a separate corrosion-compatible aluminum-shell bond to the same equipment-ground network; do not use shell/80/20 as the MultiPlus's only PE path.
- [ ] Keep AC and DC grounding roles separate: no jumper from MultiPlus case/PE to Lynx negative or the `12V` negative bus, and no fixed downstream neutral-ground bond. Leave the MultiPlus internal ground relay enabled for normal inverter/shore transfer behavior.
- [ ] After Mechman ground style is physically identified, verify whether its case-ground plus dedicated `2/0` negative establishes the house-negative/chassis reference and confirm no parallel chassis path bypasses the SmartShunt.
- [~] AC-out branches are in routine use. Close the remaining installed-ground verification, shell bonding, polarity, neutral-isolation, and GFCI acceptance checks without reopening enclosure or chassis-ground construction.
- [ ] Test GFCI trip/reset on both intended AC branch areas: office and galley.
- [ ] Test DC USB/PD outlets under realistic laptop/phone/tablet load.
- [~] Owner confirms the camper lights operate from the live `12V` junction; still verify final branch/fuse label and dimmer behavior on `12V-06`.
- [~] Owner confirms the camper fan operates from the live `12V` junction; still verify the `12V-10` branch/fuse label and all installed speed/direction/control functions.
- [~] Owner reports all three DC charging outlets are wired and separately fused. Load-test the driver `100W` and both passenger `65W` endpoints with realistic devices; verify labels, polarity, branch fuse, conductor support, heat, and voltage drop.
- [x] Switched fridge/cooler feed and positive ICECO restraint are owner-confirmed operational.
- [x] Switched pump branch and installed fresh-water system are owner-confirmed operational.
- [ ] Add spare fuses in labeled holder/location.
- [~] AC enclosures/dead-fronts are complete; confirm any remaining touchable high-current DC terminals are covered.
- [ ] Record PE/chassis/shell, GFCI/polarity, solar, alternator, heater, and HOTTAP results in `logs/LOG.md` as each closes.

## 9. Alternator / WS500 / APM-48 workstream

Goal: rough-in safely first; commission only after all preconditions are green.

- [~] Owner report `2026-09-02`: the alternator remains disabled/not yet connected as a charging source, and the only owner-identified remaining physical/configuration items are the protected PH-VAN red lead and Wakespeed read/save/programming. Treat the detailed owner guide as the final preflight rather than reopening already-completed hardware by stale checkbox.
- [ ] Wire PH-VAN red from the `F-04` alternator/load-side stud through the Eaton/Bussmann `HEB-AA` + Littelfuse `KLKD015.T` `15A/600VAC/DC` in-line branch; secure it in the loom beside `F-04`.
- [ ] Read and save the Mechman-supplied WS500 profile before changing anything; then program/verify shunt location and ratio, charge ceiling, field derate/current limit, temperature inputs, and Upfitter `#3` shutdown behavior.
- [ ] Run the controlled first-charge procedure with meter/app ready; confirm Upfitter `#3 OFF` stops charge current, record voltage/current/temperatures/warnings, and measure charge/return-path voltage drop under load.
- [ ] [HOLD] Keep alternator charging disabled until PH-VAN red, saved/programmed WS500 configuration, and the final preflight in `ELECTRICAL_Mechman_WS500_APM48_install_guide.md` are green.

## 10. Flooring / Lonseal / hardpoints

Goal: preserve the installed permanent floor and registered hardpoints while finishing/removing modules.

- [x] Glue the one-piece Lonseal to the three-piece `3/4 in` plywood floor with #650 on the evening of `2026-07-15`.
- [x] Accept that the finish bridges both plywood seams and that heavy modules are now installed; the earlier cure/loading hold is historical, not an active weekend gate.
- [ ] Monitor known edges/hardpoints after wet/dusty drives and module work. Investigate only actual loose/expanding areas, moisture/dust trails, swelling, insert spin, or floor movement; do not reopen the floor speculatively.
- [ ] Protect Lonseal with clean hardboard/cardboard/blankets during every extrusion/module/battery move; never drag parts across it.
- [x] Hard-mount the electrical module first, using the registered rivnuts and verified support path. Initial hard mount is complete; integrated anti-rack/final road restraint remains a separate closeout gate.
- [x] Install and restrain the `35 gal` tank within the hard-mounted Galley structure. Keep sender/fittings accessible and prove water acceptance separately.
- [ ] Torque/witness-mark final module fasteners, then perform a low-consequence shakedown and inspect/retorque for insert spin, vinyl indentation, moisture, abrasion, leaks, or module shift.

## 11. Panels, skins, latches, storage, and travel retention

Goal: add only the panels/features that make the system safer, stiffer, more serviceable, or visually intentional before cosmetic closure. Detailed feature choices live in `docs/implementation/INTERIOR_finish_paneling_and_feature_choices.md`.

- [ ] Map every Galley/Bench/desk face as `finished wood`, `service removable`, `smoked/translucent feature`, or `open/exposed 80/20`.
- [ ] Identify panels that are structural/shear/anti-rack vs cosmetic covers.
- [ ] Prioritize panels that brace electrical module, bench, desk, and galley skeleton.
- [ ] Use `1/2 in` plywood for most living-facing vertical/removable faces; use `3/4 in` for tops, bench lids, cooler-bearing surfaces, step/load surfaces, and large horizontal spans.
- [~] Prepare measured templates/dimension packets for the mid-September Bubinga routing; bring the real sink and soap dispenser. Do not allow routing/cutouts until support, drain, tank, service, and no-drill geometry pass.
- [ ] Prepare the fabricator's dimension packet for the `48 in` Galley and `47 in` Desk live-edge Bubinga pieces. The Bench lid is separate unfinished work, not part of the earlier three-piece commission.
- [ ] Make at least two finish samples on scrap: clear satin and one warmer/stained option.
- [ ] Make Bubinga/offcut finish samples: satin polyurethane as default; epoxy only as a selective fill/stabilizer sample unless intentionally choosing full flood coat.
- [ ] Size Bench/lid gas struts only after the actual lid material, weight, hinge line, opening angle, and mount points are known.
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
- [x] Prepare the turret opening (`2026-09-02`): score/peel the Lonseal waste circle, accept the thin sacrificial top plywood layer that came with it, test-seat the turret in the shallow recess, and confirm the existing rigid `1/2 in` template works as the jigsaw shoe riser.
- [~] Turret opening work has advanced to the final sealing stage (`2026-09-06` owner context). Before applying sealant, confirm the nearby `12V` battery was removed/isolated during cutting, plywood and aluminum were cut separately without vehicle-line damage, all chips/EPS debris are removed, the aluminum edge is deburred/coated, and the physical turret still sits flat without forcing.
- [ ] Before final seating, dry-mock the underside pipe access. Seal the turret flange to the Lonseal plane with a hidden, mechanically compressed continuous Permatex Ultra Copper high-temperature RTV gasket inside the fastener line and around the fastener holes; separately seal the skirt to aluminum `360 degrees` through every rib peak/valley. Allow `24 h` full cure before heat. If any lower gap exceeds about `1/4 in`, add a thin noncombustible metal collar/backer rather than bridging it with RTV/foam/wood/EPS.
- [ ] Mock the entire outside combustion path before final turret sealing: use the full corrugated exhaust pipe from heater to one stub of the supplied LF Bros muffler and leave the other muffler stub as the terminal outlet—do not cut the pipe in half solely to add a tail. Hard-mount the muffler outside by its bracket, point any drain down, preserve slight fall and broad sweeps, protect the intake from spray, face intake and exhaust away from each other, and prove real clearance plus noncombustible standoffs/guards from vehicle fuel systems, wiring, undercoating, plastics, and openings.
- [x] Purchase the EVIL ENERGY `10 gal` aluminum diesel tank/feed/vent package (`2026-08-30`, BOM row `65`) plus the remote `2 in` fill and neoprene-isolation hardware (`2026-09-02`, BOM rows `364` and `366`). Row `365` is a duplicate KINTLE vent kit/adapter order pending cancel/return. The LF Bros `10 L` plastic tank is no longer fuel storage and must remain never-fueled for graywater use.
- [ ] Inventory the delivered diesel package before fit-up: verify tank cap/gasket, both lower `-10AN` outlets/caps, both upper `-10AN` ports, sender leads/resistance, Speedway flange/gasket/bolts, every hose/joiner/clamp, the original EVIL `5/16 in` vent adapter/hose/valve, neoprene, and no shipping damage. Confirm cancellation/return of the duplicate row `365` package. The installed remote rollover valve must be the only atmospheric vent path unless another opening has equivalent rollover shutoff.
- [ ] Identify and document sound attachment points in the former spare-tire crossmember/frame area before cutting the cradle or drilling. Verify metal thickness/section, backside or threaded access, vehicle-line clearance, bolt stack, corrosion treatment, service removal, and full axle/tire travel.
- [ ] Dry-fit the owner-drafted cradle using `1010` plus gusseted `2 x 2 in` aluminum angle and neoprene isolation. Use the through-bolted/threaded-end verticals as primary retention, T-nut `90s` as secondary bracing, and preserve positive vertical/lateral capture if a T-nut loosens; prove the approximately `86 lb` full-load path before fueling.
- [~] Fuel-feed layout (`2026-09-06` owner report): the straight-through filter is mounted vertically and the external pump is laid out with its outlet toward the heater and about `45 degrees` upward; the small fuel line is ready to run but not complete. Finish `-10AN -> 1/8 NPT adapter -> shutoff -> 3/16 in barb -> short LF Bros black rubber connector -> original 5 mm OD / 2 mm ID rigid line -> filter -> external pump -> heater`, leaving the other lower outlet capped and keeping the pump rubber-isolated.
- [ ] Use diesel-rated thread sealant only on tapered NPT joints per its instructions. AN connections seal at the flare seat: inspect those seats and put no tape/sealant on AN threads. Leak-check a small outdoor test fill before service.
- [~] Remote fill field-fit (`2026-09-06` owner report): the tank package is largely assembled and the gravity-fill pass-through is near completion. Current path remains angled bed-wall fill -> lateral 45-degree hose dogleg -> owner-described stainless coupler -> straight hose -> 90-degree joiner -> Speedway `91676553`. The 45-degree hose has a slight kink; the tank-facing bead/barb end of the 90 was cut off to clear the Speedway flange. A roughly `4 in` hose sleeve with intended `2 in` engagement each side is planned, not verified. Keep continuous fall, independent support, and road/heat/axle clearance.
- [ ] Finish the bed-wall fill attachment using its supplied gasket and through-bolts, with `M4` only if the actual holes/countersinks suit it; add washers and locking nuts without distorting the sheet. Both sides of this wall are open air, so extra flange bedding is not required merely for a cabin/weather boundary. This does not replace fuel-tight hose connections.
- [ ] Before fuel: inspect the 45-degree hose's actual internal opening and remove any sharp crease/collapse by changing alignment or using a suitable molded fuel-fill bend; do not rely on a clamp around an unsupported bend as a kink repair. Deburr/clean the trimmed 90, verify actual straight insertion and fully metal-supported clamp lands, and resolve retention after bead removal (prefer restoring a bead or using an appropriate retained filler joint). Keep clearance between metal ends rather than forcing a hard butt; the hose sleeve's nominal length alone does not prove engagement or retention. Exact kink severity/stub geometry remain unverified.
- [x] Vent line physically completed (`2026-09-05` owner report); final valve/termination inspection and flow/rollover-path acceptance remain separate checks.
- [ ] Verify the completed vent uses one upright remote rollover valve outside, the unused upper port is capped, and no unprotected cap vent bypasses that valve. Do not install two check valves in series. After the fill-joint checks and feed shutoff/capped-outlet checks, perform a small outdoor diesel fill and inspect fill/feed/vent joints before priming or topping up.
- [~] Owner reordered the direct EVIL ENERGY `10AN -> 1/8 NPT` fitting (`2026-09-05`); receipt and exact flare/NPT fit remain pending. Immediate sequence is full underside exhaust/intake dry mock -> two-boundary turret seal/cure -> final fuel-line routing and fused heater wiring -> small outdoor diesel leak test -> prime -> supervised first burn with working CO detection and controller-commanded cooldown.
- [ ] Bench-meter the passive sender, then use one unused Cerbo Tank `DATA/GND` pair with no `12V` feed. Configure `Diesel`, `10 US gal`, and custom approximately `3 ohm empty / 90 ohm full` only after the real endpoints/direction are confirmed.
- [ ] Route the harness before closing the zone: heater, pump, T4S, fused `12V +/-`. Preserve commanded cooldown power and verify actual `C-22` length/startup voltage before retaining `14 AWG / 15A` or upgrading to `12 AWG`.
- [ ] [DEFER] Final QuinLED/WLED lighting install unless core modules are stable.
- [ ] [DEFER] Camper audio package; do not spend July 4 sprint time on it.

## 14. Solar research and procurement

Goal: fit and commission the purchased `700W` Renogy array without turning it into an unsafe secondary roof.

- [x] Record purchase: `4x Renogy 175W flexible monocrystalline = 700W`, purchased `2026-08-12`; BOM uses the `$616.90` discounted net item subtotal and excludes `$44.73` estimated tax.
- [~] Electrical planning screen: current official G2 data give `4S = 78.0V Vmp / 95.6V Voc / 9.50A Isc`; published-coefficient cold Voc is `114.86V` at `-40C`. The maximum-voltage screen passes, but estimated hot-start margin becomes negligible around `70C` before route drop; exact received labels and hot restart/tracking remain required.
- [~] Planning geometry: measured `138 x 63 in` fiberglass, centered MaxxAir, and `0.625 in` track step remain active. Current solver evidence finds no all-inside packing within the screened constraints; the candidate has two inside-skin panels and one direct-mount panel crossing each side track, using the real roof lands. Add a small local spacer/taper only if the actual panel mockup shows a sharp crease.
- [~] Received/geometry: all four panels are on hand; one-panel physical test-fit plus measured layout indicates compatibility with Starlink and MaxxAir while using nearly the full roof. Photograph/record labels/connectors/polarity if not already captured, then place final panels and cycle fan/Starlink service before caulk.
- [ ] Wash/decontaminate the roof and verify the exact structural-silicone product, substrate/backsheet preparation, cure window, drainage, and representative coupon. On one panel, pass static/heat/water/roof-cycle proof with temporary independent track-anchored test restraint; then private low-speed testing with inspection stops; then a deliberate staged-speed road-acceptance test. Routine highway use and remaining panel bonds wait until that sequence passes.
- [x] Fixed-side PV route is complete: pass-through, two-pole disconnect, stationary conductors, and MPPT landing. Preserve one `4S1P` string; only the two free string ends enter the existing two-conductor transition. No combiner or `F-09` string fuse is presently planned for the one string.
- [ ] During panel wiring, verify/support the exposed roof-side/moving cord through full roof travel so the gland and terminals carry no spring, motion, or wind load.
- [ ] Measure route drop and complete cool-start plus stationary hot-roof restart/tracking commissioning near the configured battery-charge target.
- [ ] **Installation release:** do not attach the remaining panels or begin routine highway travel until received-label, actual-weight, final-route, exact cure, one-panel static/heat/water/roof-cycle proof, temporary independent test restraint, private low-speed test, controlled staged-speed road acceptance, full-motion, and hot-operation gates pass.

Canonical decision and coordinates: `docs/studies/SOLAR_configuration_matrix.md`.

## 15. Weight, payload, balance, and shakedown

Goal: avoid building a beautiful overloaded rattle box.

- [x] Owner report `2026-09-02`: the existing camper shakedown is good. Keep the checks below for new solar, heater/fuel, HOTTAP, alternator, counter/sink/graywater, and interior-retention work rather than treating the current camper as untested.

- [ ] Record door-sticker payload if not already captured.
- [ ] Weigh major staged modules if practical: batteries, electrical module, bench, desk, galley, tank, water, tools.
- [ ] Plan water as variable payload: `35 gal` full is about `292 lb` water alone, `312+ lb` installed with tank/brackets/hoses.
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

- [~] FLEXISPOT Foldex is ordered; after receipt, mock the real chair, knees, `47 in` Bubinga Desk, rear storage, and aisle together before final mounting. Fully lower/fold the chair and test entry/aisle plus travel restraint.
- [ ] Step into cabover repeatedly using the bench/step mockup before final lid/panel choices.
- [ ] Simulate a workday cable mess: laptop, monitor, keyboard, mouse, phone, tablet, Starlink/router.
- [ ] Simulate cooking/cleaning path: sink cover, induction, Ninja, trash, dish tub, graywater removal.
- [ ] Check where shoes, wet jacket, trash, toilet/portable sanitation, and laundry will actually go.

## First-use / overnight / workday readiness

The owner reports the base camper shakedown is good. Treat these as usability refinements or gates for newly added equipment, not as a reason to reopen completed systems.

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

## Reference acceptance tests for new interior additions

- [x] Bench/electrical/Galley structure, batteries, and ICECO are restrained and have completed the owner-reported base shakedown.
- [ ] Preserve battery removability, terminal covers, and emergency fuse/disconnect access as the Bench lid and storage are added.
- [ ] Desk can support a real seated session without knee/entry pain.
- [ ] Monitor/laptop gear has a safe travel state, even if temporary.
- [x] Fresh-water fill, tank, KUS, pump, accumulator, PEX, and rear service ports are operational.
- [ ] Graywater, toilet/sanitation, bedding, trash, air fryer, monitor/laptop, and other storage each need a plausible retained home or explicit deferral.
- [ ] No planned irreversible work was done before its gate.
- [ ] The next 10 blockers are written down in this file.

---

# Near-term priority queue

## Current order — `2026-09-02`

1. **Protective-earth closeout:** verify the owner-confirmed installed MultiPlus-to-truck-chassis ground, install/verify the separate shell bond, then prove PE continuity, neutral isolation, polarity, and both GFCI chains.
2. **Heater/fuel/storage package:** finish the staged jigsaw/turret cut, then dry-fit and install the underside combustion route, diesel cradle/fill/vent/feed, pump, and rear module as one package.
3. **Bubinga/sink/graywater:** route the `48 in` Galley and `47 in` Desk pieces, install/leak-check the sink, and complete the separate vented/retained graywater system.
4. **Alternator:** wire the protected PH-VAN red lead, read/save/program the WS500, and run controlled first charge.
5. **Solar:** complete roof prep/caulk-bonding, `4S1P` panel wiring and roof-side support, then commission the already-complete pass-through/disconnect/MPPT path.
6. **Interior/HOTTAP:** receive/fit the chair; build the Bench lid, air-fryer home, monitor/laptop travel state, and storage; mount/commission HOTTAP after it arrives.

## Do not prioritize next unless the gate above is already green

- Cosmetic skins or final panel closure before heater, sink/graywater, electrical, and access-dependent tests.
- Cutting the desk/storage by estimate before the real chair/aisle mockup.
- Attaching all solar panels before exact adhesive/cure and one-panel shakedown proof.
- Diesel-heater drilling based on heat shield alone or before the complete underside vehicle-line/fuel-tank survey.
- Alternator first charge before protected PH-VAN red, saved/programmed WS500 profile, final preflight, and shutdown behavior.
- Air-fryer tape-only retention or ratcheting/bungeeing directly against an LCD.
- Final lighting or audio ahead of safety/commissioning/road-restraint work.

## Hard holds

- [MONITOR] Permanent floor is in service. Protect Lonseal and investigate only actual loose/expanding areas, moisture/dust evidence, insert spin, or floor movement; do not retain the historical cure-weekend hold as current guidance.
- [CLOSED BASE SHAKEDOWN / MONITOR NEW WORK] Batteries and ICECO are restrained and the existing camper shakedown is good. Positively restrain the air fryer, Bench lid, monitor/laptop hardware, and new storage before those items travel; inspect each newly installed subsystem after its first drive.
- [CLOSED FRESH WATER / HOLD NEW JOINTS] KUS, tank, fill/vent, pump, accumulator, PEX, and rear service ports are in regular use. Leak-check the sink joints when installed and spill-test the separate graywater system.
- [HOLD] Rear BLUE/RED penetrations are installed and working. Hold final sink/Bubinga cuts until the real sink, soap dispenser, drain body, faucet hoses, support rails, tank clearance, and continuous-slope graywater path are mocked; hold HOTTAP closeout until actual appliance clearance and leak/flow tests pass.
- [HOLD] Do not install a projecting gravity-drain valve on the low south tank boss in the entry footpath. Leave it unopened or low-profile plugged; use BLUE as the pump-assisted emptying outlet and removable upstream suction flex as the failed-pump gravity fallback. Exterior shower/cold spray uses the removable Joolca `4 m` hose and handle/head rather than a camper manifold.
- [HOLD] No permanent Quick-Release HOTTAP Bracket mount, cylinder cradle, box vents, service-plate cut, regulator service hatch, or HOTTAP V2 Mount Cover closeout until the purchased Joolca core package and selected Flame King package pass physical box/operating-clearance mockup and manual/listing review.
- [CLOSED BANK STAGING / HOLD ACCESS] The `3x 48V` bank is paralleled and restrained. The Bench lid may proceed only while preserving battery extraction, covers, branch protection, and emergency fuse/disconnect access.
- [HOLD] No alternator first-charge until protected PH-VAN red, saved/programmed WS500 configuration, final guide preflight, and shutdown behavior are ready.
- [HOLD] No final countertop sink cutout until faucet/drain/rail clearance is physically proven.
- [HOLD] No final Bubinga cuts until plywood templates, support tabs, service access, entry sweep, and finish sample are approved.
- [HOLD] No final panels over electrical/plumbing until labels, strain relief, leak/functional tests, and service access pass.
- [CLOSED AC ENCLOSURES + MULTIPLUS CHASSIS GROUND / HOLD VERIFICATION + SHELL BOND] Shore and all four outlet boxes are enclosed and in regular use, and the MultiPlus is owner-confirmed grounded to truck chassis. Verify that installed bond, close/verify the separate shell bond, and complete PE continuity, neutral isolation, polarity, and GFCI trip/reset proof.
- [CLOSED FRESH-WATER SERVICE] Gravity fill, highest-point vent, KUS, tank, pump, and rear service ports are in regular use; only sink and graywater integration remain.
- [CLOSED PV PENETRATION / HOLD PANELS] PV pass-through, disconnect, stationary conductors, and MPPT landing are complete. No all-panel bond/travel acceptance until roof preparation, exact caulk/cure, roof-side support, full roof/cab motion, and hot-operation tests pass.
