---
aliases:
  - Interior furniture layout and galley plan
  - Hiatus camper furniture concepts
  - Office-first hybrid layout
  - Galley wet spine
  - Power stair bench
tags:
  - hiatus/implementation
  - hiatus/interior
  - hiatus/furniture
  - hiatus/galley
  - hiatus/plumbing
status: draft
related:
  - "[[SYSTEMS]]"
  - "[[TRACKING]]"
  - "[[INTERIOR_driver_side_workstation]]"
  - "[[INTERIOR_finish_paneling_and_feature_choices]]"
---

# Interior Furniture Layout and Galley Design Concepts

As-of date: `2026-07-25`

Purpose: capture the active furniture/layout direction for the Hiatus/F-350 camper before final cuts. This document owns the interior **layout concept**, driver-side electrical-module/bench/desk integration, passenger-side lofted fridge/wet-spine exoskeleton, separated battery bench, galley/plumbing service strategy, high-density furniture ideas, and loose furniture construction intent. The driver-side monitor/workstation mechanism detail remains in `docs/implementation/INTERIOR_driver_side_workstation.md`; the finish/paneling/storage feature-design detail now lives in `docs/implementation/INTERIOR_finish_paneling_and_feature_choices.md`.

Status: **draft implementation baseline for hard-mounted electrical and wet-spine integration**, refreshed `2026-07-26`. The electrical module is now hard-mounted through the permanent Lonseal floor; the MultiPlus/AC enclosure remount, shore inlet, battery-bank matching/commissioning, `12V` closeout, and Bench anti-rack tie-in remain open. Keep the Bench service volume accessible while those gates close. In parallel, map and bench/driveway test the `36 gal` tank, KUS sender, fill, vent, pump outlet, drain, purchased faucet/accumulator adapters, and wet-spine hardware, with one bare in-truck dry fit before drilling or final fitting lock. Hot water is locked to the propane-only rear-box Joolca HOTTAP V2 package; the heater, Quick-Release HOTTAP Bracket, and HOTTAP V2 Mount Cover were purchased `2026-07-26`, while receipt and physical integration remain open. Keep final skins, exact drawer slides, BLUE/RED service-plate cuts, and premium walnut cuts gated on installed route/service validation.

Orientation convention throughout:

```text
TOP    = cab / bulkhead / cabover
BOTTOM = rear barn doors
LEFT   = driver side
RIGHT  = passenger side
```

---

## 1) Generated diagram set

The following images were generated on `2026-05-04` for this design pass and stored in the repo.

Primary use images:

- ![Office-first top-down layout](../../media/diagrams/interior-furniture-2026-05-04/01-office-first-top-down-layout.png)
- ![Driver workstation monitor mechanism](../../media/diagrams/interior-furniture-2026-05-04/02-driver-workstation-monitor-mechanism.png)
- ![Corrected galley wet spine](../../media/diagrams/interior-furniture-2026-05-04/05-galley-wet-spine-corrected.png)
- ![Furniture feature montage](../../media/diagrams/interior-furniture-2026-05-04/04-furniture-feature-montage.png)

Iteration archive:

- `media/diagrams/interior-furniture-2026-05-04/03-galley-wet-spine-original.png` is retained as a first-pass generation. It was superseded by `05-galley-wet-spine-corrected.png` because the first version had ambiguous front/rear labeling and used “city water” language that could confuse the intended fresh-tank-fill design.

Image verification notes:

- These `2026-05-04` images are retained as concept/iteration artifacts, not current fabrication geometry.
- `01` still shows useful plan orientation and early office-first reasoning, but its rear-left Iceco/top-right storage layout is superseded by the active passenger-side lofted fridge/wet-spine baseline.
- `02` still captures the stow-low monitor, rising VESA/Ergotron-style work mode, roof-safe state, drag chain, toe-kick storage, and travel locks. Its Iceco/fridge tower portion is superseded.
- `05` remains useful for cold-first/future-hot plumbing logic, but the pump/accumulator pack now belongs in the owner-measured `6 in` gap below the lofted passenger-side cooler support and adjacent to—but physically splash-separated from—the house batteries, not as a generic hidden galley cassette.
- `04` is a creative feature montage; it is useful for concept direction, not construction geometry.

---

## 2) Design thesis

Build the camper as a serviceable, separated wet/dry systems cluster around a clear center aisle:

1. **Passenger side = lofted fridge / wet spine / water-tank module.**
   - Iceco/fridge returns to the passenger side, raised about `16 in` on an extrusion exoskeleton.
   - The fridge slightly overlaps the `36 gal` wheel-well water tank envelope, so the frame must be mocked in 3D before exact cuts.
   - Pump and accumulator sit in the measured `6 in` gap below the cooler support toward the batteries, on a thin vibration-isolated service plate with strainer-bowl access, a nonconductive splash divider, and a drained leak path away from battery terminals/cabling.
   - Sink/graywater/fill/vent/winterization remain cold-first and hot-ready.
2. **Battery bench = separated energy mass adjacent to wet spine, not mixed plumbing storage.**
   - Batteries sit in separated enclosures inside an approximately `30 in` tall bench.
   - A flat board above the batteries separates bench storage/cushion use from battery service volume below.
   - The lid opens for battery/service access, and Hiatus bed cushions can cover the bench when the bed is not in use.
3. **Driver side = electrical closet / workstation / diesel heater zone.**
   - Electrical panel/closet extends up to the `46 in` maximum interior build height.
   - A shelf/box can project toward the computer desk/camper entry doors for DC electronics, laptop plugs, and office power access.
   - Diesel heater stays low in the driver-side utility zone, physically separated from battery and wet-service cavities.
4. **Exterior diesel preference = keep fuel outside the cabin.**
   - Investigate a narrow truck-bed-wall diesel tank, ideally around `8 gal` and roughly `3 in x 17 in` if a product exists.
   - Preferred fill/spill/pump exposure is outside, with only a protected fuel line passing through a grommet or sealed bulkhead to the heater.

Bottom line: the new layout is better because the fridge, tank, pump, batteries, electrical closet, and heater now form a real serviceable 3D systems package instead of a flat garage-floor mockup. The tradeoff is that rough 80/20 skeleton work becomes part of layout validation, not just final cabinetry.

### Physical mockup update — 2026-05-15

Owner-provided installed-camper photo/mockup confirms these current physical envelopes:

- Blue tape on the floor marks the current module footprints; use it as layout evidence, not final cut geometry.
- The taped battery bench area sits near the bulkhead/front wall and currently holds the `3x 51.2V 100Ah` batteries as a mass/extraction check.
- Cardboard represents the driver-side electrical box plus the step box projecting from/integrating with it.
- The desk is around the wheel-well area, planned at about `24 in x 48 in`, and integrates with the electrical step box.
- The fridge remains at the same raised height but should slide deeper into the passenger-side corner.
- Additional rear-entry/top-down photos show the Iceco/fridge physically mocked on top of the passenger-side wheel-well water tank, with the pump/accumulator staged low nearby in the wet-side footprint.
- The rear-entry view confirms a clear center aisle is still plausible with the fridge/tank stack on passenger side and the cardboard electrical/step/desk mass on driver side, but finished skins and handles could easily steal this margin.
- The side/top photo with the tape measure shows the driver-side cardboard electrical/step-box projection being checked against aisle/desk space; treat the visible roughly `18 in` tape span as a photo scale cue only, not a canonical measurement.

Practical implication: the next design artifact should be a measured block-envelope sketch from this taped mockup: datum, battery extraction path, step-box projection, desk/wheel-well notch, fridge slide/vent/lid sweep, pump-service access, and final aisle width after panel/handle allowances. Do not treat the photos as sufficient for exact extrusion lengths.

### Electrical module integration update — 2026-07-19

Owner-provided build update confirms the electrical module has moved from freestanding mockup into hard-mounted physical integration:

- The electrical backer was trimmed to inset cleanly into the `80/20` electrical frame.
- Component positions were adjusted for actual MultiPlus depth; the change is a packaging/mechanical fit correction, not a change to the active `48V` electrical architecture.
- The module is hard-mounted through the permanent finished floor to registered truck-bed hardpoints. Fit is clean and current stationary stiffness is acceptable; it will stiffen further when tied into the Bench, and that tie-in remains required before road use.
- The MultiPlus and combined AC breaker enclosure were removed before the lift to reduce module weight. Embedded pronged/spiked T-nuts in the plywood backer preserve easy front-side remounting and avoid loose through-bolt nuts behind the board.
- All three batteries' branch cable sets are cut, lugged, heat-shrunk, and landed at the battery-side busbars while the bay remains open. Batteries stay isolated until individual charge/rest/voltage matching is complete.
- Near-term module strategy is electrical closeout first: remount heavy AC equipment, install/prove shore AC-in, commission the matched `3x 48V` bank and `12V` junction, then bench-test and install the tank/wet spine before closing the Bench/Galley around either service zone.
- Available extra material includes two extra sticks, one `2010` extra-thick two-slot/two-bar stick, and regular angle stock; use these as fit/brace/prototype material before waiting on perfect final hardware.
- Pending dedicated `80/20` nuts/hardware should not block mock-fit, but final travel configuration should use the correct fastener standard, witness marks, and anti-rattle/retention hardware.

Travel rule: **the floor hard-mount alone is not the final road-restraint gate**. Drive only after the electrical module is tied into the Bench/adjacent structure or otherwise given verified anti-rack bracing, with panels/diagonals/latches installed enough to control racking and cargo/projectile risk.

### Black walnut surface commission update — 2026-07-05

Owner is leaning toward commissioning three final black walnut pieces from Nick after the current module geometry is locked:

1. **Passenger-side Galley countertop**
   - Target: black walnut live-edge slab, likely `~4 ft x 19 in` based on owner phrasing; confirm exact dimension sheet before cutting.
   - Thickness: `1.5 in` preferred; `2 in` acceptable if the best slab requires it.
   - Entry end: last `~15 in` should use a live edge that curves inward if Nick can source a suitable slab, so the camper entrance feels intentional and less snag-prone.
   - The live edge must remain functional: cleaned/eased/sealed, no loose bark, no dirt/water trap, and no hip/shoulder snag with the one-barn-door entry path.
2. **Driver-side computer desk top**
   - Target: dimensional black walnut rather than generic phenolic/Richlite as the final surface, while keeping plywood templates for fit validation first.
   - Finish and edge language should match the Galley: satin, softened wrist/front edge, quiet hardware, and sealed underside/holes.
3. **L-shaped Bench/lid top**
   - Target: dimensional black walnut L-shaped lid/top over the storage cubby.
   - Support: tabs/lands on the aluminum extrusion, with hinge line and support surfaces proven by template.
   - Lift assist: gas struts are desired if actual lid weight and geometry support it; add closed-state latch, anti-rattle bumpers, and mechanical open/overtravel control.

Finish posture for all three: satin polyurethane or equivalent durable clear film finish by default; epoxy only as a selective void/crack stabilizer unless the plasticky flood-coat look is deliberately chosen. Seal all faces, undersides, holes, live edges, and sink/cutout edges.

---

## 3) Recommended baseline: Office-first hybrid layout

This remains the recommended direction because the mission is full-time off-grid professional work, but the active layout now moves the fridge/wet-spine mass back to the passenger side.

```text
CAB / BULKHEAD / CABOVER
┌──────────────────────────────┬──────────────────────────────┐
│ DRIVER FRONT                 │ PASSENGER FRONT              │
│ Electrical closet / panel    │ Lofted Iceco/fridge skeleton │
│ Up to 46 in build height     │ ~16 in raised over service   │
│ DC electronics shelf/box     │ Slight tank overlap          │
│ Laptop plugs / office power  │ 36 gal wheel-well tank       │
├──────────────────────────────┼──────────────────────────────┤
│ DRIVER MID                   │ PASSENGER MID                │
│ Fixed computer desk          │ Pump + accumulator below     │
│ Monitor stow-low cassette    │ Strainer / manifold service  │
│ Electrical/service access    │ Battery bench adjacent       │
│ Diesel heater low            │ Separated enclosures         │
├──────────────────────────────┼──────────────────────────────┤
│ DRIVER REAR / ENTRY          │ PASSENGER REAR               │
│ Entry-side desk/DC access    │ Wet service / fill / shower  │
│ Heater service path          │ Graywater / winterization    │
│ Clear aisle preserved        │ Cushion-covered bench top    │
└──────────────────────────────┴──────────────────────────────┘
REAR BARN DOORS
```

Why this wins:

- Puts the fridge directly with the wet side and water tank instead of forcing a driver-side fridge tower.
- Uses the under-fridge volume for pump/accumulator/service hardware, which is exactly the kind of awkward space that should become mechanical volume.
- Keeps batteries in their own bench/enclosures with a real divider between electrical service and ordinary bench storage.
- Keeps the driver side focused on work ergonomics, electrical access, DC electronics, and the diesel heater.
- Preserves the clear center aisle while letting the 80/20 skeleton solve real 3D interference rather than pretending this can be fully drafted on the garage floor.

Tradeoffs:

- Passenger side becomes a dense systems stack; service hatches and removable panels are mandatory, not aesthetic options.
- The lofted fridge skeleton must be mocked with real component envelopes before exact cuts because it overlaps the tank and sits above plumbing.
- Wet/dry separation between pump plumbing and the adjacent battery bench needs hard partitions, drip paths, and service discipline.
- Driver-side electrical closet height and projecting DC shelf must be checked against entry movement, desk ergonomics, and roof-down clearance.

---

## 4) Alternate concept: Rear utility threshold layout

Use this only if outdoor shower/cooking and rear-door utility become more important than a permanently ready desk.

```text
CAB / BULKHEAD / CABOVER
┌──────────────────────────────┬──────────────────────────────┐
│ Wide power lounge / stair    │ Soft bench / clothes cubes   │
│ Batteries + electrical       │ Lightweight pantry / bedding │
├──────────────────────────────┼──────────────────────────────┤
│ Convertible desk             │ Shorter wet wall             │
│ Bench/desk shared seating    │ Tank + sink + removable cook │
├──────────────────────────────┼──────────────────────────────┤
│ Iceco outdoor/aisle slide    │ Wet threshold / shower QD    │
│ Shoe tray / utility landing  │ Fill / winterize / hose bay  │
└──────────────────────────────┴──────────────────────────────┘
REAR BARN DOORS
```

Use cases where this may be better:

- Outdoor cooking and showering are dominant.
- The rear threshold becomes the mudroom/wet zone.
- Desk can be setup/tear-down rather than always ready.
- Passenger/rear plumbing serviceability beats indoor counter length.

Why it is not the default:

- It risks making the desk side feel temporary.
- It clusters too many active things at the rear: fridge slide, shower hose, shoes, entry, bridge counter, and galley.
- It is more rear-heavy unless dense pantry/tank mass stays forward.
- It creates more moving panels, latches, and rattle points.

Best hybrid: keep the **office-first interior spine** but borrow the **rear wet-service hatch and wet threshold discipline** from this concept.

---

## 5) Driver-side electrical closet and battery-adjacent bench

### Required functions

The driver-side electrical/desk zone and adjacent battery bench have to solve these jobs together without mixing incompatible service cavities:

1. House the `3x 48V` batteries in separated, restrained enclosures inside an approximately `30 in` tall bench.
2. Keep a flat divider board above the batteries so ordinary bench storage/cushion use cannot intrude into battery service volume.
3. Carry the driver-side electrical closet/panel up to the `46 in` maximum interior build height.
4. Provide a projecting shelf/box toward the computer desk/camper entry for DC electronics, laptop plugs, chargers, and office power access.
5. Preserve a cushioned bench/lid surface that can be covered by Hiatus bed cushions when the bed is not in use.

### Recommended construction concept
- **Electrical module tie-in:** treat the hard-mounted electrical tower as a braced part of the bench/desk system, not an independent road-travel object. The bench/step frame should add lateral restraint and anti-rack support while preserving service access to disconnects, fuses, Cerbo, Orion, AC enclosure, and cable clamps.
- **Battery well:** low, restrained, partitioned from wet-service volume, and sized so batteries can be extracted without dismantling the whole interior.
- **Flat divider board:** separates battery bay below from bench storage/cushion use above; treat this as a protective service boundary, not just a shelf.
- **Lift/hinged lid:** lid must open for battery/storage access and include mechanical stays, gas struts, or controlled support sized to the actual lid weight; loose lift-off panels become projectiles. If the final L-shaped top is black walnut, verify hinge line, support tabs, strut geometry, closed latch, and service reach before cutting the finished lid.
- **Electrical closet:** use a vertical backer/closet face for serviceable fuses, disconnects, Lynx/Shunt/12V hardware, and labels, with dead-front protection where daily furniture users can touch it.
- **DC shelf/box:** acceptable toward the desk/entry if it remains shallow, ventilated, spill-protected, and does not block entry movement.
- **Service slit/access door:** keep emergency disconnect/fuse inspection reachable without pulling cushions or unloading the cabover.
- **Hard edge protection:** every positive stud, Class T terminal, bus, and high-current cable path needs covered/booted dead-front treatment before the bench becomes daily furniture.

Non-obvious details:

- Add a tactile/visible **“48V isolated”** indicator flag near the aisle service slit.
- Use cushion seams that reveal service panel divisions instead of hiding them.
- Put a removable sacrificial scuff plate on any step/bench edge that will be kicked constantly.
- Do not use the battery bay for random storage. Use only the separated bench storage volume above/adjacent to the protected battery bay.

---

## 6) Passenger-side lofted fridge, wet-spine skeleton, and battery bench

The old top-right soft-storage idea is superseded. The passenger side now carries the lofted fridge/wet-spine/water-tank cluster plus the adjacent separated battery bench.

Recommended roles:

- Lofted Iceco/fridge about `16 in` above the floor/tank service zone.
- `10-series` or targeted 80/20 exoskeleton to support the fridge and define service-panel edges.
- Under-fridge pump/accumulator/strainer/manifold bay next to the `36 gal` wheel-well tank.
- Battery bench adjacent to the plumbing bay, with hard separation between wet service and battery/electrical cavities.
- Cushion-compatible bench top/lid when the Hiatus bed cushions are not deployed as the bed.

Build direction:

- Mock the fridge, tank, pump, accumulator, battery boxes, bench lid, electrical step box, and `24 in x 48 in` wheel-well desk as one 3D package before buying exact-cut extrusion.
- Preserve a known cooler/panel/frame removal path to the pump strainer, accumulator, tank shutoff, and pump electrical connector; uncommon service does not require one-opening or quick-disconnect access.
- Use drip trays, leak sensor, and physical partitions so a plumbing leak cannot run into the battery enclosure.
- Use overlay/removable panels for finished faces only after the skeleton passes access and interference checks.
- Do not place the powered audio subwoofer or audio wiring in the wet-service bay. If camper audio uses the planned powered sub, keep it in a dry low bench/toe-kick/electrical-side volume and preserve service access/ventilation.
- Keep the fridge vent path open: lower cool-air intake, upper warm-air exhaust, and no tight skin around compressor vents.

Advanced detail: treat this as a **systems exoskeleton**, not cabinetry. Every extrusion member should have a job: structural support, service-panel edge, pump-board mount, fridge restraint, battery-bench boundary, or anti-rattle locator.

---

## 7) Driver-side workstation and monitor

Detailed implementation owner: `docs/implementation/INTERIOR_driver_side_workstation.md`.

Use the following summary as the layout-level baseline:

- Fixed full-time desk, not a wobbly camping table.
- Stow-low / face-down monitor cassette at desk height.
- Rising VESA spine or hinged carriage that deploys only after the roof is popped.
- Ergotron-style arm is for ergonomic adjustment, not for travel load.
- Monitor stores against hard stops and padded supports; no load on LCD surface.
- Positive latch/pin for monitor mast, monitor angle, fridge slide, desk leaf, and any doors.
- Cable drag chain or controlled service loop; no proud cable loop above roof-safe line.
- Shallow wall storage around desk; keep knee/foot space sacred.
- Toe-kick false bottom can carry flat gear, cable chase, and low-voltage/service loops if protected from dirt and kicks.

Layout-level storage around the desk:

- Laptop vertical sleeve.
- Dock/router/Starlink power cubby with ventilation.
- Headset hook or cubby.
- Paper/notebook slot.
- Keyboard flat slot.
- Small trash slot.
- Cable/adapters bin.
- Red/amber night strip under desk edge and warm task LED above work surface.

Hard rule: the desk side can gain storage, but not by sacrificing seated work geometry. A camper office that is miserable for `8` hours will fail the build mission.

---

## 8) Passenger-side lofted Iceco/fridge module

The Iceco/fridge has moved back to the passenger side. Current baseline: raise it about `16 in` on an extrusion exoskeleton so pump/accumulator hardware can live below it next to the wheel-well water tank. Treat this as a service module, not just an appliance bay.

Recommended roles:

- Fridge support tray or fixed lofted shelf with positive travel restraint.
- Under-fridge plumbing bay for the existing pump, accumulator, strainer, shutoff, short flex sections, and only the tees/valves actually required by the final fixture route.
- Vent chimney / warm-air escape path that does not heat the battery bench, tank bay, or desk electronics.
- Shallow landing surface or rail only where it does not interfere with lid opening, venting, or service access.
- Structural/service boundary between wet hardware and adjacent battery enclosures.

Design requirements:

- Measure body envelope including handles, hinges, lid sweep, cord bend radius, compressor vent sides, and required hand clearance at the raised height.
- Confirm whether lid access works fixed in place or needs a partial/full slide at the lofted height.
- Use positive travel lock plus secondary strap/draw latch if any slide is used.
- Add hard stops so the fridge cannot overextend into the aisle/rear entry or pull its cord.
- Provide lower cool-air intake and upper warm-air exhaust path. If boxed, use a small thermostatic `12V` fan and washable dust screen.
- Keep a known access path to the pump, strainer, accumulator, and heater connections. Removing the cooler, a panel, or a documented portion of the 80/20 frame is acceptable; the plumbing does not need quick-disconnect modularity or one-tool daily access.

Non-obvious feature: make the fridge skeleton do double duty as the hard mounting and wet/dry boundary for the compact plumbing pack. Use the existing 80/20 to support lines, protect them from cargo, define a shallow leak-tray edge, and keep vibration loads off fittings.

---

## 9) Passenger-side galley and wet spine

### Core recommendation

Build a **propane-only, parked-connection hot-water system** around the existing cold-water pack, two compact direct-profile camper ports, and a HOTTAP mounted directly to the exterior side of the rear swingout box. The purchased Quick-Release HOTTAP Bracket and HOTTAP V2 Mount Cover keep the heater outside the propane compartment, protected from road dust, and out of the box's storage volume. The port layer should use the real Joolca hose directly rather than add a second QD ecosystem unless physical testing proves that necessary. No articulating arm, box-side water plate, heater cubby, permanent three-way splitter, Sea-Dog washdown body, large service hatch, or travel-exposed plastic faucet adapter remains.

Current north/middle/south routing concept (`2026-07-26`; FORIOUS faucet interfaces confirmed at `3/8 in`; exact faucet and accumulator adapters purchased; camper service-plate fit remains field-gated):

```text
MIDDLE: fresh tank
  -> north-end low outlet + tank shutoff
  -> short reinforced potable-water flex / shock loop
  -> NORTH: strainer -> pump -> flex -> accumulator
  -> one 1/2 in PEX cold tee
      -> branch: faucet cold
      -> straight: rear BLUE service valve -> shortest supported PEX-B
                   -> UP120A5 -> compact stainless bulkhead
                   -> verified all-metal Joolca-compatible male tap adapter
                      (BLUE cold out)

Separate RED path:
faucet hot <- insulated 1/2 in PEX <- RED service valve
           <- shortest supported PEX-B <- UP120A5
           <- compact stainless bulkhead
           <- verified all-metal Joolca-compatible male tap adapter
              (RED hot return)

Parked hose modes using the supplied Joolca female/female hoses:
HOT SHOWER:
  camper BLUE male plug -> supplied 1 m hose -> HOTTAP inlet
  HOTTAP outlet -> supplied 4 m hose -> shower handle/head

SINK HOT:
  camper BLUE male plug -> supplied 1 m hose -> HOTTAP inlet
  HOTTAP outlet -> supplied 4 m hose -> camper RED male plug -> faucet hot

COLD MOTO SPRAYER:
  camper BLUE male plug -> supplied 4 m hose -> shower handle/head
  HOTTAP and LP remain disconnected

Separate unpressurized paths
  -> high end-port gravity fill + high end-port vent
  -> low tank drain for emptying the fresh tank
  -> sink gray drain/graywater cassette
```

Opening the faucet hot side in sink mode creates flow through the pump, BLUE port/hose, heater, RED hose/port, and faucet; the HOTTAP ignites once flow exceeds approximately `0.6 GPM`. One-outlet-at-a-time operation deliberately swaps the supplied `4 m` hose between the shower handle/head and camper RED rather than permanently adding a splitter and another hose. A direct male garden-profile plug is straight-through, so each immediately accessible BLUE/RED ball valve is an intentional camp control: connect with the valve closed, open only the active path, then close and relieve pressure before disconnecting. That one valve action is the cost of eliminating the QD3 body, adapter key, reducer, rear hose barb, and second QD standard.

The Joolca shower is modular at both connections: the shower head quick-connects to the handle, and the handle/head assembly quick-connects to the long hose. For camper RED service, disconnect the entire handle/head assembly from the `4 m` hose, leaving the hose's female socket free to snap onto the RED male plug. Do not assume the bare shower head replaces the handle; preserve the handle's control/connection role.

Do not use rigid PEX between the tank, strainer, and vibrating pump. Start the fixed `1/2 in` PEX distribution after the pump outlet flex section. Keep the fresh-tank drain, sink gray drain, and pressurized cold-out service port as distinct functions; a gravity tank drain is not a useful pressure wash outlet.

### Compact fixed plumbing pack

Hard-mount the existing plumbing compactly in the under-cooler/adjacent bench structure:

- Tank shutoff.
- Short reinforced suction flex.
- Strainer.
- Pump.
- Short discharge flex.
- Accumulator.
- One ordinary `1/2 in` PEX tee: faucet cold branch plus continued cold-out trunk.
- One accessible full-port `1/2 in` PEX ball valve immediately inside each rear service port, used for camp connection/disconnection as well as service/winterization.
- Two existing `UP120A5` `1/2 in PEX x 1/2 in MNPT` adapters, each threaded directly into the rear `1/2 in FNPT` of a compact bulkhead after the shortest supported PEX-B run from its valve. This removes the QD3-era `3/8 in` barb, short reinforced hose, and clamps.
- Two compact `1/2 in FNPT` rear / `3/4 in MGHT` front panel bulkheads. RAINPAL `SSBF020` is the lead physical candidate: seller-listed lead-free `304 stainless`, `27 mm / 1-1/16 in` panel opening, `36 mm` exterior flange, and maximum `6 mm` panel thickness when the exterior GHT must remain usable.
- Two directly mounted all-metal male tap adapters that physically latch and seal in the actual Joolca female hose socket. First candidate is GARDENA `39004-G` / UPC `066283390047`, a North-American-thread metal Original-GARDENA-System tap adapter. Melnor plastic `2MQC` is the known-profile control, not the installed target; Melnor brass `15409`, Morvat, and any locally stocked metal plug remain bench-test candidates rather than assumed fits.
- Optional joint-reduction comparison only: one NSF/ANSI `61-G` Legend `T-805MNL` / `101-580NL` `1/2 in F1807 PEX x 1/2 in MNPT` combination ball valve per port can replace the separate purchased valve, short PEX segment, and `UP120A5`. Do not buy it until the in-hand purchased stack is mocked for depth and access.
- One insulated, joint-minimized `1/2 in` PEX hot-return trunk from the RED service valve to faucet hot.

The compact bulkheads mount through one thin, structurally backed aluminum service plate or two locally reinforced thin-panel holes; they do not automatically span the full camper sandwich wall. For the RAINPAL candidate, physically verify its `27 mm` opening, `36 mm` flange, rear nut/tool access, gasket stack, and maximum usable panel thickness before cutting. Use a simple measured stretch cap over each metal male plug for road dust; no large hatch, box, or service-door cover is allowed.

Do not add a camper-side cold/hot manifold, three-valve bypass, permanent antifreeze pickup, exterior selector, box-side plate, CPC adapters, Sea-Dog body, adapter key, or permanent hot splitter. QD3 remains a premium fallback only if the actual-hose test cannot produce a clean durable direct-profile male plug or if automatic shutoff later proves worth the cost and cross-ecosystem key. Faucet cold remains available with the external heater disconnected.

Stock wet-tray footnote: any pump/accumulator/strainer area below the lofted fridge should have a shallow removable wet tray or pan with small upturned edges, a visible inspection/leak-sensor point, and a path to lift/wipe/dry it through the documented disassembly sequence. Treat it as early warning and cleanup management, not as primary containment; plumbing joints still need proper fittings, clamps, support, strain relief, and post-drive leak checks.

Service rule: preserve a known disassembly path and enough tool access to inspect/tighten the pump-side joints. It is acceptable to remove the cooler, panels, or part of the 80/20 structure for uncommon service; avoid only buried joints that require destroying finished work or removing the water tank.

### Gravity-fill vent hose sizing

Owner measurement on `2026-05-12`: the gravity-fill vent nipple measures about `10 mm` OD on the main land and about `11 mm` OD at the largest barb/ridge. Correct vent hose sizing is therefore based on hose **ID**, not hose OD:

- Preferred spec: `10 mm ID` food-grade/potable flexible tube.
- Common inch fallback: `3/8 in ID` food-grade/potable tube (`9.5 mm` ID), warmed if needed for installation over the `11 mm` barb.
- Do **not** use the previously ordered `1/2 in ID x 5/8 in OD` tube for this nipple; `1/2 in ID` is about `12.7 mm` and is oversized for an `11 mm` barb.
- If an inch-size hose must slide on without heat/stretch, `7/16 in ID` (`11.1 mm`) is the next size up, but treat it as a looser fit and use a proper clamp plus leak/vent-flow check.

Use a stainless clamp, avoid kinking the vent line, and re-check after the first fill/drive cycle.

### Tank-specific notes

Owner-confirmed physical port geometry (`2026-07-16`): the tank has four molded ports on each end, with two visibly large and two smaller ports per end, and no obvious/open top port. Exact model and thread sizes remain unconfirmed. The pattern resembles common wheel-well tanks advertised with `1.5 in` and `1/2 in` female NPT end ports, but that resemblance is not sufficient to order fittings. Inspect for a membrane-covered top boss, model/logo markings, and supplied plugs; verify each selected thread physically before procurement.

Provisional role map, subject to the installed-orientation dry fit:

- Upper large end port nearest the exterior hatch: gravity fill.
- Upper small end port that remains highest in normal fill orientation: unrestricted vent/overflow to the hatch vent nipple.
- Low port nearest the north pump bay: tank suction through a shutoff and short reinforced flex run.
- Low south/service-side port: gravity tank drain, with the valve and hose weight supported by the structure rather than cantilevered from the polyethylene boss.
- KUS sender: new mechanically backed/gasketed top opening over the deepest unobstructed tank section unless physical inspection reveals a suitable top boss.
- Unused ports: leave their membranes intact where applicable or reinstall manufacturer-compatible plugs with potable-water/plastic-compatible thread sealant.

Water mass planning values:

- `10 gal`: about `83.5 lb`
- `20 gal`: about `166.9 lb`
- `36 gal`: about `300.4 lb`
- Installed full tank, brackets, hoses, and hardware: plan around `320+ lb`

Implications:

- Treat fill level as a load-management choice, not background detail.
- Add a fill-level load label near the fill hatch.
- Verify bracket/plusnut locations and decide whether a secondary floor/tie-down path is needed.
- Keep dense pantry/tools away from the high passenger wall if the water tank is full; use lighter/bulkier storage above the tank.

### Tank workbench-to-install sequence (`2026-07-16`)

1. **Inventory before cutting:** photograph every molded opening and cap, measure threads/neck IDs/ODs, and label only temporary candidate functions (`fill`, `vent`, `pump outlet`, `drain`, `sender`, `spare`). Do not infer function from port size alone.
2. **Workbench mockup:** place the empty tank in its installed orientation on blocks; lay out the KUS sender, gravity-fill hose, vent hose, pump-outlet flex loop, drain, restraint brackets, and compact fixed pump/accumulator pack. Verify sender length against internal depth at the actual proposed location.
3. **Mandatory bare-tank truck dry fit:** after the floor cure gate, protect the Lonseal and place only the empty tank in the truck. Check wheel-well contact, extrusion/fridge envelope, plusnut/bracket reach, sender-removal clearance, fill/vent bend radius, continuous hose fall/rise, plumbing-pack access, low drain, and where a leak would travel.
4. **Freeze the port map:** with the reported end-port-only geometry, default the gravity fill to an upper large end port and the vent to the highest suitable upper small end port. Neither needs a literal top-surface penetration if both communicate with the tank airspace and the fill hose falls continuously from the exterior hatch while the unrestricted vent rises continuously to its nipple. Verify whether a membrane-covered top boss exists before cutting a separate KUS sender opening.
5. **Choose fitting methods:** use tank-manufacturer-approved molded, spin-weld, or properly backed bulkhead/under-ring methods appropriate to the polyethylene wall and access. The KUS sender method is now selected: purchased KUS/Wema `FLS-U` stainless SAE five-hole C-ring under-ring plus the supplied sender gasket and M5 screws; do not treat sealant or self-tapping screws alone as structure.
6. **Cut and test on the bench:** the exact `2-3/8 in` / `60 mm` bi-metal hole saw (Amazon ASIN `B0C8JMH91Q`) was purchased `2026-07-24`, but the cut still waits for a frozen sender/port map and proven flat unobstructed geometry. For the selected `FLS-U` method, follow the official manual's single-opening requirement rather than the smaller sender-alone guidance. Preassemble the sender, gasket, screws, and C-ring as shown; tilt/rotate the ring through the one opening and tighten the five screws into it—do **not** drill five separate pilot holes through the tank top. Capture/remove all chips, deburr without thinning the sealing land, install without distorting the wall, then fill and leak-test the tank/fittings before the extrusion locks access.
7. **Install wet-side first:** hard-mount the tank restraint and compact pump/accumulator pack before passenger-side furniture closure. Support the flex/PEX transitions, protect the wet/dry boundary, and preserve the documented cooler/panel/frame removal path; do not add fittings solely to make the assembly quick-removable.
8. **Cut the exterior fill/vent last:** physically prove the installed tank endpoints, hose fall/vent rise, backing, service access, and spill/overflow path from both sides before cutting the camper/bed-side interface.

### Propane hot-water routing baseline (`2026-07-26` owner-corrected final direction)

The final appliance architecture is propane-only and uses the existing pump/accumulator plus the two female/female hoses supplied with HOTTAP Essentials. The camper-port hardware remains pre-drill: lead prototype is a direct metal Joolca/GARDENA-profile plug on a compact stainless GHT bulkhead behind an accessible valve, with QD3 retained only as premium fallback. Preserve the tank's assigned functions: upper south ports for gravity fill and unrestricted vent, low north `1/2 in` port for pump pickup, and low south `1/2 in` port as a dedicated gravity tank drain.

```text
low north tank pickup
  -> tank shutoff -> reinforced suction flex -> strainer
  -> SHURflo 4008 pump -> discharge flex -> SEAFLO accumulator
  -> 1/2 in PEX tee
       -> branch: 1/2 in PEX -> faucet-cold adapter -> faucet cold
       -> straight: 1/2 in PEX -> BLUE full-port service valve
                    -> shortest supported PEX-B -> UP120A5 MNPT/PEX adapter
                    -> compact 1/2 in FNPT / 3/4 in MGHT stainless bulkhead
                    -> verified all-metal Joolca-compatible male tap adapter

HOTTAP mounted directly outside the box on Quick-Release HOTTAP Bracket
camper BLUE male plug -> supplied 1 m female/female hose -> HOTTAP blue inlet

Shower mode:
HOTTAP red outlet -> supplied 4 m female/female hose -> shower handle/head

Sink-hot mode:
HOTTAP red outlet -> supplied 4 m female/female hose
  -> camper RED male plug -> compact stainless bulkhead
  -> UP120A5 -> shortest supported PEX-B -> RED full-port service valve
  -> insulated 1/2 in PEX
  -> faucet-hot adapter -> faucet hot

Cold-sprayer mode:
camper BLUE male plug -> supplied 4 m female/female hose -> shower handle/head
HOTTAP and LP disconnected
```

The fixed camper and heater-package fitting stack is therefore:

1. One `1/2 in` PEX tee.
2. Two purchased EFIELD faucet adapters: `1/2 in PEX-B barb x 3/8 in OD compression male`, two-pack ASIN `B0C7QBNVG9`, purchased `2026-07-25`. The FORIOUS manual identifies both factory hot/cold supply hoses as `3/8 in`; screw each hose nut directly onto the adapter's male compression seat after removing any loose tube-compression nut/ferrule supplied with the adapter. Do not use PTFE tape on this compression connection.
3. Two existing full-port `1/2 in` PEX ball valves, one immediately accessible behind each rear service port. These are routine connect/disconnect controls as well as service/winterization isolation.
4. Two existing SharkBite `UP120A5` `1/2 in PEX x 1/2 in MNPT` adapters, each threaded directly into the rear of its bulkhead after the shortest supported PEX-B segment from the valve.
5. Two compact panel bulkheads with `1/2 in FNPT` rear and `3/4 in MGHT` front. Lead candidate RAINPAL `SSBF020` is seller-listed lead-free `304 stainless` and uses a `27 mm / 1-1/16 in` hole, `36 mm` exterior flange, and at most `6 mm` panel when the outside GHT is occupied.
6. Two all-metal North-American-thread male tap adapters physically proven against the real Joolca hose. Test GARDENA `39004-G` / UPC `066283390047` first. Use plastic Melnor `2MQC` only as the known-profile control; do not assume Melnor brass `15409` or Morvat fit from appearance.
7. Optional only after a depth mockup: NSF/ANSI `61-G` Legend `T-805MNL` / `101-580NL` `1/2 in F1807 PEX x 1/2 in MNPT` combination valve can replace each separate valve, short PEX segment, and `UP120A5`. The existing purchased parts remain the zero-new-purchase prototype.
8. The HOTTAP Essentials supplied hose assembly: one `1 m` and one `4 m` red hose, each with female QuickConnect sockets at both ends. Use the `1 m` hose as the first cold-feed trial. Do not cut it before mounted routing proves whether the approximately `20.4 in` nominal surplus is actually objectionable; if shortening is earned, target roughly `25-29 in` total hose length for the measured `19 in` span and inspect the factory hose-end construction first.
9. One thin, backed aluminum camper two-port plate or two locally reinforced thin-panel holes with BLUE/RED labels, compatible sealing, protected wall-core passage, and two simple measured stretch caps. No hatch or service box.
10. Twelve `1/2 in` PEX cinch clamps downstream of the accumulator: one at the accepted YVSKM accumulator adapter, three at the tee, one at each faucet adapter, two at each service valve, and one at each `UP120A5` transition. The YVSKM four-pack (ASIN `B0FDFM97HP`) was purchased `2026-07-25`; use one and retain three spares. Inspect markings and supplied gaskets, verify fit, and cold-pressure-test; Apollo `APXFB1212S` / `CPXFB1212S` remains the fallback. The purchased RecPro `30 in` double-FIP braided hose handles the pump-side accumulator connection.
11. Compatible thread sealant on the two `UP120A5` MNPT-to-bulkhead FNPT joints only; use proper flat washers on GHT seats. Do not apply thread sealant to compression seats, Joolca/GARDENA/Melnor QuickConnect O-rings, GHT washer seats, or Joolca gasketed/BSP connections unless that fitting's instructions require it.

The direct male tap adapters and compact GHT bulkheads are straight-through; the accessible BLUE/RED valves therefore stop flow before disconnection. The RAINPAL candidate is seller-claimed lead-free `304 stainless`, but neither it nor the GARDENA metal adapter carries a verified whole-assembly NSF/ANSI 61 listing in this review. That does not make the HOTTAP path potable: Joolca's current manual explicitly says the recreational appliance is not allowed to supply drinking or sanitary water. Treat the BLUE external service hose and complete heated side as recreational wash hardware, keep drinking water on the untouched interior cold faucet branch, cap/inspect the exterior plugs, and prove the assembled system physically before drilling.

One mode is configured at a time: cold sprayer, hot shower, or sink hot. Routine water setup is still simple: valve closed, hose click, valve open. Shutdown is close LP, close the active BLUE/RED valve(s), relieve at the faucet/shower, unplug/drain the hoses, drain the HOTTAP when freezing conditions require it, clean/cap the camper plugs, disconnect LP for travel, and secure the mounted cover. QD3 remains the fallback if the owner later decides eliminating that valve action is worth the cost and removable key.

Keep three rear functions distinct:

1. The low south tank port remains a gravity fresh-tank drain with its own supported valve and capped/hose-ready outlet.
2. The BLUE service port is pressurized cold water out to the deployed heater.
3. The RED service port accepts heated water back from the deployed heater and feeds only the faucet hot side.

Do not cross-connect the gravity drain into the pressure/hot circuit. The exterior shower is the removable `4 m` hose plus Joolca handle/head, not an additional permanent camper branch.

The purchased appliance is the **Joolca HOTTAP V2 Essentials**. The purchase plan previously carried an owner-supplied `35,000 BTU` figure, but Joolca's current US product page on `2026-07-26` states `27,000 BTU` and up to `6 L/min / 1.6 GPM`; verify the received data label before locking the burner rating or reusing the older number in thermal calculations. The current manual lists a `1.2 m / 4 ft` LPG hose plus separate `1 m / 3 ft` and `4 m / 13 ft` water hoses. Joolca's support documentation permits a camper-trailer pump source, Melnor QuickConnect fittings, vehicle mounting, and connection to an existing kitchen faucet. The purchased SHURflo `4008` is nominally `3.0 GPM` / `55 PSI`. Joolca says HOTTAP continues to operate at high elevation but loses efficiency/output as air thins; it publishes no hard numeric altitude ceiling, so prove ignition and useful temperature rise at intended Colorado elevation while the heater remains returnable.

The HOTTAP remains directly mounted to the exterior side of the bumper box. Through-bolt the purchased Quick-Release HOTTAP Bracket—previously documented as Joolca's vehicle quick plate—to structural backing; do not rely on aluminum skin alone for road vibration. Use the purchased HOTTAP V2 Mount Cover for dust/travel protection and remove/open it as required before operation. The external location recovers box storage and physically separates the burner from the cylinder compartment. LP and water stay disconnected for travel.

Before ignition, clear/remove the mounted cover and verify that the installed exterior position still satisfies Joolca's current manual clearances. Measure from the heater faces/exhaust to the nearest box wall/door, camper surface, vent opening, stored object, or open cover; marketing photos do not waive the manual. Do not operate the HOTTAP inside the open-front box. A fan does not change the appliance's outdoor-use classification.

Use the purchased Flame King `YSN10LB-ALM` DOT/TC aluminum cylinder with OPD QCC1/Type-1 valve upright. Flame King lists `10 lb` / `2.5 gal` propane capacity, `9.6 lb` empty weight, and `9 x 9 x 19.25 in` dimensions; nominal filled mass is about `19.6 lb`. The owner-selected location is inside the exterior rear swingout box. Treat it as a removable cylinder cargo package rather than permanent installed LP plumbing: travel valve closed and regulator/hose disconnected, then connect the supplied four-foot Joolca regulator/hose only when parked with the box open and heater deployed.

The reported shelf opening is `19.5 in`, leaving `0.25 in` nominal clearance over the listed cylinder. Dry-fit the purchased cylinder, bracket/strap pack, Safoner hatch, and AWW stone mat together in the rear box. Keep the cylinder upright and secure, use camper-appropriate mounting hardware, preserve valve/regulator access, and keep the low/high vents clear.

The HOTTAP manual states that the recreational appliance is not allowed to supply drinking or sanitary water, while Joolca support separately documents connection to an existing kitchen faucet. Resolve that conservatively: use the heated side as recreational sink/shower wash water only, never as drinking water or as a purification step. The cold branch bypasses the heater and remains the drinking-water path.

Purchase posture: the `2026-07-26` propane setup includes one HOTTAP V2 Essentials, one Quick-Release HOTTAP Bracket, one HOTTAP V2 Mount Cover, one Flame King `YSN10LB-ALM`, one CALPOSE gauge, one Safoner hatch, one AWW stone mat, and one bracket/strap two-pack. Receive and dry-fit the complete package together, then leak-test the assembled LP connections. The HOTTAP Nomad kit is not needed because it duplicates the purchased SHURflo system. Buy no QD3 key or two-port set now. When the HOTTAP arrives, test the real hose against the direct-profile camper-water port candidates. The measured camper-to-heater span is about `19 in`; use the supplied `1 m` hose as the cold-feed trial before buying or cutting anything.

The grey AWW foldable `23.6 x 15.5 in` stone mat is part of the propane setup, not shower gear. Confirm its exact placement during the rear-box dry fit.

For sink graywater, start with a removable under-sink vessel before adding an under-truck tank. Mock `2.5 gal` (`~20.9 lb` water) and `5 gal` (`~41.7 lb` water) sizes with the actual sink drain. The baseline should include a compact waterless trap, vented container connection, positive travel retention, removable spill tray/leak-sensor point, and a lift path that works when full. An under-truck gray tank remains a post-shakedown option because it adds a bed penetration, external vent/dump hardware, road-debris protection, freeze exposure, and legal-dump discipline; its dump valve should not be treated as a normally open drain.

### Countertop and appliance strategy
Use convertible surfaces:

- Small sink with flush cover.
- Purchased galley fixture baseline: Sarlai drop-in/workstation sink, black topmount, `15 in x 15 in` exterior with approx. `11 in x 13 in` interior basin, plus FORIOUS black pull-out faucet with soap dispenser.
- Current fit assumption: an `18-19 in` countertop with about `14 in` clear extrusion opening is probably workable because the chosen sink is topmount, but the actual sink cutout, faucet shank/nut/hose bends, drain/graywater path, and any local rail/connector drop still need field validation before final cuts.
- Final Galley surface direction: commission a black walnut live-edge slab after the plywood template is proven; current owner target is likely `~4 ft x 19 in`, `1.5 in` preferred thickness / `2 in` acceptable, with the last `~15 in` of the entry end curving inward if the slab allows.
- Treat the final walnut counter as protected furniture, not a raw cutting board: satin polyurethane or equivalent durable finish, all faces/cutouts/live edges sealed, and epoxy limited to void/check stabilization unless the full flood-coat look is intentionally selected.
- Removable Duxtop `8100MC/BT-180G3` induction cooktop stored vertically or in a retained slot when not in use; cooking position must keep pan handle, cord, GFCI outlet, and countertop heat clearance clear of the sink/faucet.
- Dedicated low cubby for the Ninja SP151 air-fryer/toaster oven with positive travel restraint, heat clearance, crumb-cleanout access, and a plug/service path that does not cross the wet bay.
- Cutting board / sink cover slot.
- Collapsible dish tub instead of a deep domestic sink if vertical volume is tight.
- Low appliance bay can remain flexible around the Ninja SP151 for dry food bins or a removable appliance crate only if they do not compromise heat clearance, graywater access, or wet/dry separation. No interior water-heater cubby is reserved.
- Graywater slide cassette under sink with waterless trap or removable drain approach.

Avoid:

- Deep fixed drawers that block tank fittings.
- Permanent microwave high on the wall.
- A large sink that consumes the only prep surface.
- Hidden graywater plumbing with a trap that cannot be winterized.

---

## 10) Propane hot-water operating modes

The decision is final: hot water is supplied only by the camp-deployed propane system.

### Sink mode

1. Remove/open the HOTTAP V2 Mount Cover and verify the exterior heater and exhaust zone are clear.
2. Confirm both camper service valves are closed. Snap the supplied `1 m` hose from camper BLUE directly to the HOTTAP inlet.
3. Disconnect the shower handle/head assembly from the `4 m` hose, connect that hose from the HOTTAP outlet directly to camper RED, then open the BLUE and RED service valves.
4. Connect the supplied regulator/hose from the upright, restrained `10 lb` cylinder through the protected service hatch to the exterior heater; route it clear of sharp edges/exhaust and leak-check the disturbed LP connection.
5. Open the propane cylinder.
6. Open the faucet hot side fully until air clears and the heater ignites; set temperature at the HOTTAP and minimize cold mixing so heater flow stays above the proven minimum flow.

### Shower mode

With BLUE and RED valves closed, snap the `1 m` hose from camper BLUE directly to the HOTTAP inlet and connect the `4 m` hose from HOTTAP outlet to the shower handle/head. Open BLUE; leave RED closed. Connect/leak-check LP, open LP, then use the shower control. Sink hot is not simultaneously connected in the minimal configuration.

### Cold moto-sprayer mode

Keep LP disconnected. With BLUE closed, snap the `4 m` hose from camper BLUE directly to the shower handle/head, then open BLUE and use the shower control as a pressurized cold sprayer. Leave RED closed. Clean the hose ends before later connecting to RED/hot service.

### Shutdown and freeze protection

1. Close the propane cylinder, then disconnect the regulator/hose before travel.
2. Close the active BLUE/RED camper service valve(s), then open the active faucet/shower control to relieve trapped pressure.
3. Disconnect and gravity-drain both supplied hoses; expect only residual water after the valves are closed and pressure is relieved.
4. Clean the exposed camper male plugs and install their measured stretch caps; clean the Joolca hose sockets before storage.
5. In freezing conditions, follow the HOTTAP manual's drain/storage procedure after every use and confirm the short PEX-to-bulkhead transitions drain without trapped low points.
6. Leave both camper service valves closed for travel and in the documented winterized state when applicable.
7. Confirm the exterior heater is dry, LP/water-disconnected, and protected by its HOTTAP V2 Mount Cover; confirm the upright cylinder is valve-closed and fully restrained.

---

## 11) Storage system by access frequency

Storage locations are owner-fit decisions to make in the actual camper, not prescriptive layout geometry in this doc. Keep only the travel-retention rules below when adding bins, drawers, shelves, or soft goods.

Travel-retention standards:

- Soft bins need compression nets or doors.
- Drawers need real travel latches.
- Slides need positive lock plus secondary retention.
- No open shelf should be trusted on washboard roads.
- Magnets are secondary, not primary.

---

## 12) Materials and mechanisms

Recommended material logic:

- **10-series / light rail / L-track / strut:** default for interior module framing, accessory rails, panels, baskets, hooks, removable dividers, wet-spine retainers, and soft-storage retention when the load is not clearly structural/dynamic.
- **15-series T-slot:** no longer a broad starter-stock default after the `36 gal` wheel-well tank downscope. Use only for measured heavy/dynamic modules that prove they need the stiffness: possibly the lofted fridge support, electrical closet frame, battery bench structure, monitor mast/spine, or desk frame.
- **Plywood:** main carcasses, L-shaped electrical backer, lids, service panels.
- **Phenolic/Richlite/laminated birch:** desk and galley top candidates if budget/weight tolerates it.
- **HDPE/ABS/aluminum panels:** wet-service access panels, shower hatch backing, removable scuff/kick plates.
- **Frosted acrylic/smoke-grey covers:** shallow cubby covers where visibility + retention matters.
- **Anti-rattle tape/felt/neoprene:** panel interfaces, drawers, lid perimeters.
- **Cable drag chain:** monitor mast, slide-out powered surfaces, fridge slide power if required.

Panel mounting direction:

- **Baseline finished look:** use overlay panels on living-facing/front/aisle surfaces so the finished camper reads as clean cabinetry rather than an exposed industrial frame.
- **Prototype logic:** overlay panels can be easier than inset panels because the `10-series` frame can be built and adjusted first; panels can then be scribed, trimmed, and bolted on without disassembling the extrusion to slide them into slots.
- **Strength logic:** mechanically fastened overlay panels can act as shear skins and reduce racking better than thin inset panels. Use bolts into T-nuts, threaded inserts, or accessible panel fasteners as the primary retention.
- **Panel thickness:** do not force `1/4 in` inset skins just because the extrusion slot invites it. Use thickness by function: thin for cosmetic/low-load covers, thicker plywood/composite where the panel is part of stiffness, service protection, or a step/load surface.
- **Service zones:** keep 80/20 visible or use quick-removable panels in electrical, plumbing, rear utility, and wet-spine areas. Do not hide fuses, disconnects, pump/strainer, valves, winterization points, or frequent fasteners behind permanent skins.
- **Visible face screws are acceptable:** do not over-engineer every panel just to hide screw heads. Countersunk face screws are valid on non-premium faces, especially if covered by carpet, fabric, laminate, removable trim strip, wood plugs, or a deliberate black/finish-washer hardware language. Stain alone will not hide screw heads; use plugs/filler only on panels that do not need frequent removal.
- **Magnetic panels:** acceptable as a promising option for light, non-structural service covers. Preferred pattern is routed/counterbored magnets in the back of the panel landing on steel brackets/plates attached to the 80/20, with felt/neoprene tape for anti-rattle.
- **Magnet limits:** magnets are strongest in pull and weaker in shear. Do not make them the primary retention for heavy panels, step faces, drawer/counter structure, or anything that could become cargo on rough roads. Use a captive tether, hidden screw, quarter-turn, latch, or positive stop where panel loss would matter.
- **Anti-shift locating features:** combine magnets with a small lip, cleat, dowel/locator pin, shoulder screw, rubber bumper, 3D-printed nub, or bracket tab that drops into/against an 80/20 slot. Let the locator carry shear/slide loads and let the magnets pull the panel tight.
- **Adhesive/tape:** use foam tape/VHB/felt mainly for anti-rattle, bedding, or light bonding after surface prep. Do not rely on adhesive alone for structural or service-critical panels.

Mechanism rules:

- Every moving piece gets an open-state and closed-state latch if both states matter.
- Use hard stops for slides/arms, not cable tension.
- Use witness marks/paint pen on structural fasteners after final assembly.
- Build service panels so they can be removed with common tools, not hidden behind permanent trim.

---

## 13) Mockup and validation gates

### Gate I0: electrical module road-restraint tie-in

- Tie the freestanding electrical module into the bench/desk structure or verified hardpoints before any road travel.
- Add anti-rack restraint: panels, diagonals, angle, gussets, or equivalent bracing enough that the tower cannot sway independently.
- Confirm service access remains reachable after tie-in: main disconnect, Class T/fuse areas, Lynx, Orion, Cerbo, AC enclosure, cable clamps, and labels.
- Add final fastener standardization, torque/witness marks, anti-rattle interfaces, and strain-relief checks.

Pass when: the electrical module behaves as part of the interior structure, not a loose freestanding rack, and emergency electrical access still works.

### Gate I1: roof-down, bench, and cabover-step sweep

- Tape full-size battery bench height, lid swing, cushion stack, and divider-board elevation.
- Tape passenger-side lofted fridge height, wet-spine service opening, and battery-bench partition.
- Tape monitor stow height, DC shelf projection, and cable loop.
- Cycle or simulate roof-down envelope.
- Confirm cabover entry path with cushions installed.

Pass when: roof closes with margin, bench/cushion use is plausible, and cabover entry does not require stepping on fragile service panels.

### Gate I2: passenger-side lofted fridge / wet-spine envelope

- Measure Iceco body, handles, hinge/lid sweep, cord exit, vent sides, and service clearance at the raised `~16 in` height.
- Mock the water tank overlap, under-fridge pump/accumulator board, battery bench wall, vent path, and any slide extension if used.
- Confirm the fridge opens, ventilates, locks, and still allows pump/strainer/accumulator service without removing major furniture.

Pass when: the fridge, tank, plumbing service bay, battery separation, vent path, and aisle/entry clearance all work together.

### Gate I3: seated workday mockup

- Mock chair/stool, desk height/depth, knee width/depth, footrest, monitor distance, keyboard/mouse reach, and outlet/USB placement.
- Work at it for long enough to find actual ergonomic problems.

Pass when: the desk is plausible for a full workday, not just a five-minute laptop perch.

### Gate I4: wet-spine service test

- Mock tank, under-fridge pump board, accumulator, graywater cassette, fill/vent chase, leak tray, battery separation wall, and rear/aisle service hatch.
- Simulate cleaning pump strainer, winterizing, dumping graywater, and connecting shower hose.

Pass when: all service actions can be done without unloading the whole galley.

### Gate I5: load sequencing test

Before using the Ninja SP151 air fryer/toaster oven or induction cooktop, write and label a simple operating hierarchy:

1. Induction cooking.
2. Ninja SP151 air fryer/toaster oven.
3. Office loads.

Hot water is propane-only and is not an AC load-sequencing branch.

Pass when: a user can tell which high-draw appliance is allowed from labels/switching, not memory.

---

## 14) Procurement posture

Buy/commit later, after mockup:

- Final extrusion cut lengths.
- Drawer slide lengths.
- Final panels/skins.
- Monitor arm/mast exact hardware if roof sweep is unknown.
- Appliance bay final pocket/restraint for the Ninja SP151.
- Rear-box Quick-Release HOTTAP Bracket/backing and HOTTAP V2 Mount Cover, Flame King cylinder restraint/vent package, single camper BLUE/RED service plate, supplied-hose reach, and port/road protection until the complete physical mockup passes.
- Permanent penetrations.

Reasonable low-regret prep:

- Cardboard/foam mockup materials.
- A small assortment of `10-series` T-slot/rail connector samples plus a few representative `15-series` samples for stiffness comparison only.
- Latches/draw-latch samples.
- Anti-rattle tape samples.
- Cable-chain/sample loom sized to monitor, desk/DC shelf, and fridge wiring where motion/service loops are needed.
- Service-panel fastener samples.
- Cushion/lid hardware, service-panel latch, and divider-board samples for the separated battery bench.

Do not buy broad `15-series` because “camper furniture needs extrusion.” Buy it only where a measured module actually needs that stiffness. Exact-cut `10-series` should also wait until the taped/cardboard envelope proves the module; stock-length/sacrificial prototype pieces are lower risk than final cut lists.

---

## 15) Current open questions owned by this design

- Exact installed camper interior dimensions and roof-down sweep line.
- Final electrical step-box and battery-bench height/lid segmentation.
- Battery extraction path with the step/bench bridge removed.
- Whether any fridge-adjacent or desk-adjacent vertical storage clears roof/window/shoulder geometry.
- Exact Iceco model, raised passenger-side lid/vent/cord/slide envelope, deeper-corner slide position, tank overlap, and service-panel clearance.
- Final driver-side desk height/depth after real seated mockup.
- Monitor mechanism choice: rising VESA spine vs under-desk flip-up vs quick-release sleeve.
- Wheel-well tank fitting orientation, fill/vent bend radius, drain access, and restraint path.
- Pump board location below the lofted fridge: aisle-facing, rear-facing, swing-out, or hybrid removable cassette.
- Graywater strategy: jug/cassette size, waterless trap, vent, dump path, overflow behavior.
- Rear-box HOTTAP package geometry: Quick-Release HOTTAP Bracket backing/clearances, HOTTAP V2 Mount Cover travel state, cylinder cradle/vents, single BLUE/RED camper plate, supplied `1 m`/`4 m` hose reach, port protection, regulator service hatch, and complete freeze drainage.
- Shower deployment: rear barn doors, passenger access window, or both.
- Appliance bay identity: Ninja SP151 restraint/storage, bins, or swappable crate; no interior water-heater volume is reserved.

---

## 16) Recommendation summary

Recommended baseline:

- **Use the office-first hybrid.** The full-time workstation is the mission-critical feature.
- **Turn the driver-side electrical/step-box and adjacent battery bench into a serviceable step/bench system.** Make it removable in sections, safe to step on where intended, and clear about which volume is electrical service versus ordinary storage.
- **Build the passenger side as a lofted fridge/wet-spine exoskeleton.** Raise the Iceco/fridge about `16 in`, put pump/accumulator below it, and prove the tank overlap/service access physically.
- **Make the battery bench separated and cushion-compatible.** Batteries low in their own enclosures, flat divider board above, lid access, storage/cushion use kept out of battery volume.
- **Keep the driver desk shallow but serious.** Preserve knee room; use the driver-side electrical closet/DC shelf for office power without blocking entry or roof closure.
- **Build plumbing as a service bay, not a hidden nest.** Under-fridge minimum-fitting pump/strainer/accumulator/tee access, graywater cassette, service hatch, leak tray, and wet/dry separation are mandatory.
- **Propane-only hot water.** Build the two-port BLUE cold-out / RED hot-return service interface; no alternate heater branch is reserved.
- **Treat every moving panel like cargo.** Latches, hard stops, anti-rattle, and roof-safe checks are not optional.
