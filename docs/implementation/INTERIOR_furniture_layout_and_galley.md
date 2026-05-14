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
---

# Interior Furniture Layout and Galley Design Concepts

As-of date: `2026-05-14`

Purpose: capture a serious furniture/layout direction for the Hiatus/F-350 camper before anything is built. This document owns the interior **layout concept**, bench/storage strategy, galley/wet-spine direction, high-density furniture ideas, and loose furniture construction intent. The driver-side monitor/workstation mechanism detail remains in `docs/implementation/INTERIOR_driver_side_workstation.md`.

Status: **draft implementation baseline for mockup and design development**. This is not a final cut list. Do not convert these concepts into exact extrusion cuts, drawer-slide lengths, panels, penetrations, or water/propane routing until the installed shell, roof sweep, tank, fridge, and electrical envelopes are physically measured. Current construction direction: prototype the `10-series` exoskeleton first, then add mechanically removable overlay panels over living-facing surfaces after the frame geometry is proven.

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

- `01` correctly shows the requested plan orientation and primary zones. Minor caveat: it shows a water fill/vent chase callout on both sides; the actual fill/vent chase should remain passenger/wet-side unless physical routing proves otherwise.
- `02` correctly captures the stow-low monitor, rising VESA/Ergotron-style work mode, roof-safe state, Iceco/fridge slide, venting concept, drag chain, toe-kick storage, and travel locks. Geometry remains conceptual.
- `05` is the preferred galley/wet-spine image. It avoids city-water wording, shows active cold water now, future hot stubs capped, fresh tank fill/vent/outlet/drain, graywater cassette, removable service cassette, and rear shower/winterization/fill-vent hatch.
- `04` is a creative feature montage; it is useful for concept direction, not construction geometry.

---

## 2) Design thesis

Build the camper as two serviceable side spines around a clear center aisle:

1. **Driver side = electrical / work / fridge spine.**
   - Heavy batteries and electrical low/front.
   - Full-time work desk mid-left.
   - Iceco fridge/cooler rear-left because the old top-right location does not physically fit.
   - Shallow storage only where it does not steal knee room or roof-down clearance.
2. **Passenger side = storage / galley / wet spine.**
   - Top-right soft storage bench instead of a hanging closet.
   - `36 gal` wheel-well tank low on passenger side.
   - Compact sink/induction/graywater/appliance bay above and around tank.
   - Pump/manifold/winterization/shower service gathered into a removable wet-spine service cassette.
3. **Front cross-camper = cabover landing and battery step.**
   - The battery bench is not just storage; it is the step/landing system into the cabover bed.
   - Top-right storage bench continues the landing so cabover access is less awkward.
4. **Rear threshold = utility handoff.**
   - Rear-left fridge top/slide becomes grocery/camp handoff space.
   - Passenger-rear service hatch handles shower, winterization, fill/vent inspection, and future hot tie-in.

Bottom line: use the van-build trick of making every cubic inch multi-role, but keep truck-camper constraints stricter: lower weight, lower center of gravity, fewer hidden systems, better travel locking, and pop-down roof clearance.

---

## 3) Recommended baseline: Office-first hybrid layout

This is the recommended direction because the mission is full-time off-grid professional work, not just weekend camping.

```text
CAB / BULKHEAD / CABOVER
┌──────────────────────────────┬──────────────────────────────┐
│ DRIVER FRONT                 │ PASSENGER FRONT              │
│ Electrical closet            │ Soft storage bench           │
│ 3x 48V batteries low         │ Clothes cubes / bedding      │
│ Power stair bench            │ Cabover landing continuation │
│ 48V bulkhead board           │ No hanging closet            │
│ 12V wall-side board          │                              │
├──────────────────────────────┼──────────────────────────────┤
│ DRIVER MID                   │ PASSENGER MID                │
│ 12V battery low              │ Galley wet spine             │
│ Diesel heater                │ 36 gal wheel-well tank       │
│ Fixed desk                   │ Sink + induction + storage   │
│ Monitor stow-low cassette    │ Pump/manifold service board  │
├──────────────────────────────┼──────────────────────────────┤
│ DRIVER REAR                  │ PASSENGER REAR               │
│ Iceco fridge/cooler          │ Rear wet service hatch       │
│ Locking slide                │ Shower QD / winterize        │
│ Vent tower + landing shelf   │ Fill/vent access             │
└──────────────────────────────┴──────────────────────────────┘
REAR BARN DOORS
```

Why this wins:

- Keeps the desk as a real work bay instead of a camp table.
- Keeps wet systems and electrical/office systems on opposite sides.
- Puts the densest masses low: `3x 48V` batteries, `12V` battery, water tank, fridge, canned goods, tools.
- Gives a straight center aisle from rear doors toward cabover.
- Lets the top-right “closet” become useful storage/landing instead of a hanging-clothes dead zone.
- Lets plumbing service concentrate near passenger/rear, where shower and winterization actually happen.

Tradeoffs:

- Rear-left fridge can crowd entry if slide/lid geometry is sloppy.
- Driver side storage must stay shallow to preserve work comfort.
- Passenger galley can become service-hostile if drawers/skins bury pump and tank fittings.
- AC appliance choices need strict load sequencing.

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

## 5) Front driver electrical / power stair bench

### Required functions

The top-left electrical/battery zone has to do four jobs at once:

1. House `3x 48V` batteries low and restrained.
2. Carry the L-shaped electrical closet/backer above them.
3. Provide a cushioned bench / lounge surface.
4. Serve as a real step and landing into the cabover bed.

### Recommended construction concept

- **Battery well:** low, vented/warmed as required, and sized so batteries can be extracted without dismantling the whole interior.
- **Lift-out center bridge:** because the `3x 48V` batteries spill toward center, make the center-spill portion a removable bridge panel, not a fixed carcass.
- **Split lids:** avoid one giant cushion/lid. Use separate access panels for:
  - battery handle/cable inspection;
  - disconnect/Class T/fuse visual inspection;
  - center bridge removal;
  - soft storage that is allowed to be buried under cushions.
- **Aisle-facing service slit:** a narrow vertical access door for emergency disconnect/fuse inspection without pulling cushions or unloading the cabover.
- **Hard edge protection:** every positive stud, Class T terminal, bus, and high-current cable path needs covered/booted dead-front treatment before the bench becomes daily furniture.
- **Thermal branch:** if diesel heat is used for battery compartment support, duct it as a small controllable warm-air branch with sensor verification; do not blast warm air directly at inverter/fuse hardware.

Non-obvious details:

- Add a tactile/visible **“48V isolated”** indicator flag near the aisle service slit.
- Use cushion seams that reveal service panel divisions instead of hiding them.
- Make the cabover step top a slightly different texture/color so it reads as a foot target in low light.
- Put a removable sacrificial scuff plate on the front edge of the power stair; this edge will get kicked constantly.
- Do not use the battery bay for random storage. Use adjacent bench voids for soft goods; keep battery air/service volume disciplined.

---

## 6) Top-right storage bench instead of hanging closet

Hanging clothes storage is poor in this camper because it consumes height, blocks window/shoulder space, and creates an awkward single-use volume. Use a bench/cube system instead.

Recommended roles:

- Cabover landing continuation.
- Soft clothes cubes.
- Bedding/towels.
- Camera/office bags.
- Seasonal layers.
- Shower towel and dry bag storage near the wet-side but not inside the wet bay.

Build direction:

- Low bench base with removable cushion.
- Top access for low-frequency soft goods.
- A vertical soft-cube wall only if it stays below roof-down and window-clearance constraints.
- Compression nets or fabric doors instead of heavy cabinet fronts.
- A few standardized cube sizes, not one-off irregular boxes.

Advanced detail: use a **soft-bin manifest** instead of built-in compartments. Example: one cube for work gear, one for socks/base layers, one for toiletries, one for bedding, one empty overflow. This lets the furniture stay simple while the packing system carries the organization.

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

## 8) Rear-left Iceco fridge/cooler module

The Iceco has moved to the bottom-left / rear-left because the old top-right location does not physically fit. Treat this as a utility block, not just an appliance bay.

Recommended roles:

- Locking fridge slide or lift-access bay.
- Rear-door grocery handoff surface.
- Coffee/tool landing shelf.
- Vent chimney / warm-air escape path.
- Shallow vertical storage above/around it.

Design requirements:

- Measure body envelope including handles, hinges, lid sweep, cord bend radius, and compressor vent sides.
- Confirm whether lid access requires a full slide, partial slide, or top clearance only.
- Use positive slide lock plus secondary strap/draw latch.
- Add hard stops so the fridge cannot overextend into the aisle/rear entry or pull its cord.
- Provide lower cool-air intake and upper warm-air exhaust path. If boxed, use a small thermostatic `12V` fan and washable dust screen.
- Keep the top of the fridge module useful but not clutter-prone: add shallow rails/lip and a travel-cleared landing pad.

Non-obvious feature: build a narrow **fridge chimney tower** that also stores vertical items: cutting mat, laptop sleeve, Starlink/router panel, paper towel, bottle, trash slot, or shower sandals. Keep it shallow so it does not become a shoulder obstacle.

---

## 9) Passenger-side galley and wet spine

### Core recommendation

Build a **cold-water-first wet spine** and reserve hot-water capability with capped stubs. Do not let water-heater uncertainty block the sink/tank/pump/faucet/drain build.

```text
Fresh tank
  -> tank outlet shutoff
  -> flexible shock/load loop
  -> strainer
  -> pump
  -> flex loop
  -> accumulator + pressure gauge
  -> cold manifold
      -> sink cold
      -> exterior shower cold QD
      -> optional drinking filter/spigot
      -> capped future heater feed

Future heater return / hot side
  -> capped hot stub at manifold
  -> faucet hot side
  -> exterior shower hot QD cap
```

### Wet spine cassette

Mount the service-intensive plumbing on one removable or swing-out board/tray:

- Tank shutoff.
- Flex shock/load hose loop.
- Strainer.
- Pump.
- Accumulator.
- Pressure gauge.
- Cold manifold.
- Winterization pickup.
- Blowout Schrader.
- Low-point drains.
- Leak tray/sensor.
- Quick-disconnect unions and pump electrical connector.

Service rule: one hatch or one lift-out bin should expose the whole pump/strainer/accumulator/manifold cluster. If you need to remove drawers, unload pantry, or pull the tank to change a pump strainer, the furniture is wrong.

### Gravity-fill vent hose sizing

Owner measurement on `2026-05-12`: the gravity-fill vent nipple measures about `10 mm` OD on the main land and about `11 mm` OD at the largest barb/ridge. Correct vent hose sizing is therefore based on hose **ID**, not hose OD:

- Preferred spec: `10 mm ID` food-grade/potable flexible tube.
- Common inch fallback: `3/8 in ID` food-grade/potable tube (`9.5 mm` ID), warmed if needed for installation over the `11 mm` barb.
- Do **not** use the previously ordered `1/2 in ID x 5/8 in OD` tube for this nipple; `1/2 in ID` is about `12.7 mm` and is oversized for an `11 mm` barb.
- If an inch-size hose must slide on without heat/stretch, `7/16 in ID` (`11.1 mm`) is the next size up, but treat it as a looser fit and use a proper clamp plus leak/vent-flow check.

Use a stainless clamp, avoid kinking the vent line, and re-check after the first fill/drive cycle.

### Tank-specific notes

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

### Countertop and appliance strategy

Use convertible surfaces:

- Small sink with flush cover.
- Removable induction cooktop stored vertically.
- Cutting board / sink cover slot.
- Collapsible dish tub instead of a deep domestic sink if vertical volume is tight.
- Low appliance bay that can remain flexible: microwave, future `2.5-4 gal` electric tank, dry food bins, or removable appliance crate.
- Graywater slide cassette under sink with waterless trap or removable drain approach.

Avoid:

- Deep fixed drawers that block tank fittings.
- Permanent microwave high on the wall.
- A large sink that consumes the only prep surface.
- Hidden graywater plumbing with a trap that cannot be winterized.

---

## 10) Hot water decision tree

Current best posture: **cold-first now, hot-ready later**.

### Option A: Cold-first + kettle/induction

Use for phase 1.

- Sink works immediately.
- Exterior rinse/shower can be cold-only.
- Dishwater can come from induction/kettle.
- Lowest risk and least plumbing delay.

### Option B: Outdoor propane shower module

Use if the priority is rear/outdoor showering.

- Keep appliance outside.
- Feed with cold QD from pump/manifold.
- Propane stays rear/exterior.
- Hot output either goes to exterior shower only or to a deliberate temporary hot return QD.
- No indoor combustion, no concealed propane joints, no casual cubby propane without proper standards.

### Option C: Small electric tanked heater later

Plausible, but treat it as a managed load and a winterization object.

Energy reference:

- `2.5 gal` at `60°F` rise: about `367 Wh`
- `4.0 gal` at `60°F` rise: about `587 Wh`

Power conflict examples:

- Induction high + microwave input can exceed `2.4 kW` inverter-continuous class.
- Microwave + common `1440 W` electric heater load can also exceed comfort margin.
- Induction high + a `1440 W` electric heater is not acceptable as a normal simultaneous load.

If electric tanked hot water is added:

- Put it low/mid, not high.
- Add drain pan and visible drain/relief path.
- Add bypass/winterization valves.
- Put it on a labeled manual switch or load-shed relay.
- Treat it as a thermal battery preheated from shore/drive/solar surplus, not an unlimited shower source.

---

## 11) Storage system by access frequency

Do not just add cabinets. Assign storage by access frequency and travel mass.

### Daily access

- Desk: laptop, headset, keyboard, cables, notepad, USB-C station.
- Rear-left: fridge, groceries, coffee, shoes, wet tray.
- Galley top: sink cover, induction, cutting board, dish kit.
- Rear service hatch: shower hose, fill hose, winterization adapter.

### Frequent but not constant

- Top-right soft cubes: clothes, towel, toiletries, bedding.
- Galley vertical slots: cookware, cutting board, collapsible dish rack.
- Fridge tower: paper towel, bottle, small trash, Starlink/router gear.

### Infrequent / heavy / dirty

- Under-bench non-electrical voids: tools, recovery soft gear, spare parts.
- Rear threshold: leveling blocks, hose gear, shower sandals, wet gear.
- Toe-kick false bottoms: flat items, cable chase, lightweight spares only.

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
- **15-series T-slot:** no longer a broad starter-stock default after the `36 gal` wheel-well tank downscope. Use only for measured heavy/dynamic modules that prove they need the stiffness: possibly the electrical cabinet frame, fridge slide/base, monitor mast/spine, or desk frame.
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

### Gate I1: roof-down and cabover-step sweep

- Tape full-size power stair bench height.
- Tape top-right bench/cube height.
- Tape monitor stow height and cable loop.
- Cycle or simulate roof-down envelope.
- Confirm cabover entry path with cushions installed.

Pass when: roof closes with margin and cabover entry does not require stepping on fragile service panels.

### Gate I2: rear-left fridge envelope

- Measure Iceco body, handles, hinge/lid sweep, cord exit, vent sides, and slide extension.
- Open rear doors and simulate entry while fridge is extended.
- Confirm no door/aisle conflict.

Pass when: fridge opens, ventilates, locks, and does not dominate the rear threshold.

### Gate I3: seated workday mockup

- Mock chair/stool, desk height/depth, knee width/depth, footrest, monitor distance, keyboard/mouse reach, and outlet/USB placement.
- Work at it for long enough to find actual ergonomic problems.

Pass when: the desk is plausible for a full workday, not just a five-minute laptop perch.

### Gate I4: wet-spine service test

- Mock tank, pump board, graywater cassette, fill/vent chase, and rear service hatch.
- Simulate cleaning pump strainer, winterizing, dumping graywater, and connecting shower hose.

Pass when: all service actions can be done without unloading the whole galley.

### Gate I5: load sequencing test

Before adding microwave or electric hot water, write and label a simple operating hierarchy:

1. Induction cooking.
2. Microwave.
3. Water-heater recovery.
4. Office loads.

Pass when: a user can tell which high-draw appliance is allowed from labels/switching, not memory.

---

## 14) Procurement posture

Buy/commit later, after mockup:

- Final extrusion cut lengths.
- Drawer slide lengths.
- Final panels/skins.
- Monitor arm/mast exact hardware if roof sweep is unknown.
- Microwave pocket final size.
- Electric tanked heater.
- Propane cubby/hot-water hardware.
- Permanent penetrations.

Reasonable low-regret prep:

- Cardboard/foam mockup materials.
- A small assortment of `10-series` T-slot/rail connector samples plus a few representative `15-series` samples for stiffness comparison only.
- Latches/draw-latch samples.
- Anti-rattle tape samples.
- Cable-chain sample sized to monitor/fridge wiring.
- Service-panel fastener samples.
- Soft cube/bin samples for the top-right bench.

Do not buy broad `15-series` because “camper furniture needs extrusion.” Buy it only where a measured module actually needs that stiffness. Exact-cut `10-series` should also wait until the taped/cardboard envelope proves the module; stock-length/sacrificial prototype pieces are lower risk than final cut lists.

---

## 15) Current open questions owned by this design

- Exact installed camper interior dimensions and roof-down sweep line.
- Final power stair bench height and lid segmentation.
- Battery extraction path with the center-spill bench bridge removed.
- Whether top-right vertical cube storage clears roof/window/shoulder geometry.
- Exact Iceco model, lid/vent/cord/slide envelope, and rear-entry collision.
- Final driver-side desk height/depth after real seated mockup.
- Monitor mechanism choice: rising VESA spine vs under-desk flip-up vs quick-release sleeve.
- Wheel-well tank fitting orientation, fill/vent bend radius, drain access, and restraint path.
- Pump board location: aisle-facing, rear-facing, or hybrid removable cassette.
- Graywater strategy: jug/cassette size, waterless trap, vent, dump path, overflow behavior.
- Hot-water scope: cold-only phase 1, outdoor propane shower only, sink hot water, or small electric tanked later.
- Shower deployment: rear barn doors, passenger access window, or both.
- Appliance bay identity: microwave, electric tank, bins, or swappable crate.

---

## 16) Recommendation summary

Recommended baseline:

- **Use the office-first hybrid.** The full-time workstation is the mission-critical feature.
- **Turn the top-left battery mass into a power stair bench.** Make it serviceable, removable in sections, and safe to step on.
- **Make top-right a soft storage / clothes cube bench, not a closet.** Low, light, flexible, and cabover-useful.
- **Keep the driver desk shallow but serious.** Preserve knee room; store vertically and in toe-kick voids only where it does not hurt ergonomics.
- **Move Iceco rear-left and make it a utility block.** Slide/vent/landing surface/storage tower.
- **Build the passenger galley as a wet spine, not a hidden plumbing nest.** Removable pump/manifold cassette, graywater cassette, service hatch.
- **Cold-first, hot-ready.** Add capped future hot stubs; do not commit to propane/electric hot water until service-map freeze.
- **Treat every moving panel like cargo.** Latches, hard stops, anti-rattle, and roof-safe checks are not optional.
