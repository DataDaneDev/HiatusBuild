---
aliases:
  - Driver-side workstation implementation
  - Left wall workstation mechanisms
  - Monitor stow-low mechanism
tags:
  - hiatus/implementation
  - hiatus/interior
  - hiatus/workstation
status: draft
related:
  - "[[SYSTEMS]]"
  - "[[TRACKING]]"
  - "[[INTERIOR_finish_paneling_and_feature_choices]]"
---

# Driver-Side Workstation, Monitor, Electrical Shelf, and Storage Mechanisms

As-of date: `2026-09-02`

Purpose: capture a buildable design direction for the driver/left-side workstation and electrical-closet interface so the camper can support full-time work, preserve pop-down roof clearance, keep DC electronics/laptop plugs accessible, and gain storage without ruining ergonomics.

Status: **active measured-mockup baseline**, refreshed `2026-09-02`. The final Desk surface is a `47 in` live-edge Bubinga piece; the FLEXISPOT Foldex chair is ordered but not yet physically accepted in the camper. Preserve the approximately `24 in` desk depth until the real rear storage module and chair are in place. Do not trim the Bubinga or mount the monitor/laptop hardware until seated ergonomics, aisle/entry, heater/service, and roof-down envelopes pass. Adjustable arms are work-position devices only; each monitor/laptop platform needs a padded hard-stop cradle and positive mechanical travel latch/strap that does not load the screen, arm joints, or Desk edge.

Related docs:
- `docs/core/SYSTEMS.md`
- `docs/core/TRACKING.md`
- `docs/implementation/INTERIOR_furniture_layout_and_galley.md`
- `docs/implementation/INTERIOR_finish_paneling_and_feature_choices.md`
- `docs/plans/PROJECT_build_order_of_operations.md`

Generated concept diagram:

- ![Driver workstation monitor mechanism](../../media/diagrams/interior-furniture-2026-05-04/02-driver-workstation-monitor-mechanism.png)

Diagram caveat: this image is a mechanism concept, not a fabrication drawing. The monitor stow/deploy geometry, roof-safe line, cable chain, and latch positions must be validated with the real installed shell. The Iceco/fridge portion of the `2026-05-04` diagram is superseded by the passenger-side lofted fridge/wet-spine baseline.

---

## 1) Design thesis

Use the driver wall as a **work/electrical service spine**, not as a deep drawer wall or fridge tower.

Overall interior layout owner: [INTERIOR_furniture_layout_and_galley](INTERIOR_furniture_layout_and_galley.md). This workstation doc owns the driver-side mechanism details inside that office-first layout. The Iceco/fridge is now passenger-side and is no longer part of this driver-side module.

Recommended primary architecture:

1. **Fixed lower desk/utility structure:** desk, diesel-heater base zone, and electrical-closet service paths tie into a low, rigid driver-wall frame below the roof-down envelope.
2. **Stow-low monitor cassette:** monitor stores face-down or low in a padded cradle at/near the desk surface, with no travel load carried by the adjustable arm.
3. **Deployable mast/hinge:** only after the roof is popped, a short 80/20 mast or hinged VESA carriage raises/rotates the monitor into working position.
4. **Electrical closet / DC shelf interface:** the vertical electrical panel/closet can extend up to the `46 in` interior build height, with a shallow shelf/box projecting toward the desk/entry for DC electronics, laptop plugs, chargers, and office power.
5. **Shallow storage wall:** use shallow cubbies, vertical sleeves, mesh pockets, and toe-kick storage around the desk/electrical shelf rather than filling knee space with drawers.
6. **Positive travel locks:** every moving element gets a mechanical latch/pin; magnets/friction are secondary only.

Bottom line: the monitor can feel Ergotron-sturdy while working, but it must become a **latched cargo item** while driving or lowering the roof. The driver side should now stay focused on work ergonomics, electrical service access, and heater serviceability.

---

## 2) Working constraints to preserve

### Layout constraints

- Driver/left wall sequence currently includes:
  - vertical electrical closet/panel up to the `46 in` maximum interior build height;
  - cardboard-mocked electrical box plus a step box projecting from/integrating with it;
  - projecting DC electronics / laptop-plug shelf or box toward the computer desk and camper entry doors;
  - low diesel heater zone with service access;
  - `24 in x 48 in` desk remains the preserved starting envelope around the wheel-well area, integrated with the electrical step box. Mock the installed rear storage module plus actual chair first; try folding/stowed-chair handling before trimming. A `20 in` depth is a fallback only after measured aisle/entry and seated-work tests show the `24 in` version fails.
  - stow-low monitor mechanism and shallow storage only where they do not steal knee room, entry clearance, or service access.
- The Iceco/fridge is now passenger-side in the lofted wet-spine module; do not size the driver-side desk around a fridge tower.
- Current furniture CAD and `2026-05-04` generated diagrams are reference-only after the installed-shell layout change.
- `15-series` extrusion should be reserved for actual dynamic/heavy modules: electrical cabinet frame, monitor spine, or desk frame if measured loads demand it. Use `10-series`/lighter rail for accessories, panels, cubbies, and trim.

### Roof clearance constraints

- Nothing fixed to the roof or roof-lift structure for the workstation.
- The stowed monitor, mast, desk accessories, and cubby contents must sit below the measured roof-down sweep envelope with margin.
- The monitor must have a visible “roof safe” state: stow pin engaged, mast down, screen cradle latched, no cable loop standing proud.

### Ergonomic constraints

- The desk must remain a full-time work surface, not only a camping table.
- Do not occupy the knee/foot envelope with storage unless it is shallow and set back.
- A `27 in` 16:9 monitor has an approximate active-panel size of `23.5 in W x 13.2 in H`; target viewing distance should remain roughly `27-40 in` where the shell width allows.
- Desk height should be set from the actual chair/stool and seated elbow height. Treat `28-30 in` as only a starting range, not a fixed design value.

---

## 3) Pre-build measurement gates

Complete these before final cutting or ordering exact-length extrusion.

### Gate W1: roof-down sweep map

1. With the shell installed, mark a fixed floor datum and driver-wall datum.
2. Tape/cardboard a full-size block for the stowed monitor + mast + arm + cable chain.
3. Cycle the roof open/closed slowly and record the lowest moving-roof envelope at:
   - electrical closet / cabover step;
   - desk top;
   - monitor stow cradle;
   - electrical closet / DC shelf projection;
   - door-side aisle edge.
4. Add a physical margin before finalizing any stowed hardware height.
5. Create a simple go/no-go template or marked batten for future checks.

Pass when: roof can close with the monitor stowed, cable loop controlled, and no hard contact or fabric pinch.

### Gate W2: electrical closet / DC shelf / heater envelope

Measure and record:

- electrical closet height/depth/width up to the `46 in` maximum build height;
- service reach to fuses, disconnects, shunt/Lynx/12V hardware, labels, and cover fasteners;
- electrical step-box and DC shelf/box projection toward the desk/entry doors, including hip/shoulder/door interference and finished-panel/handle allowance;
- laptop plug/USB-C/AC/DC station reach from seated position;
- diesel heater body, duct, intake/exhaust/fuel-line, and service-panel access;
- cable bend radius, service loops, and AC/DC/data separation.

Pass when: electrical service, office power access, heater service, desk ergonomics, and entry/aisle movement all work without hidden service points, sharp hip/knee conflicts, or roof-down conflicts.

### Gate W3: seated work envelope

Mock with cardboard/plywood:

- chair/stool position;
- desk height/depth, including the current `24 in x 48 in` wheel-well desk target;
- knee width/depth around the wheel-well notch and electrical step-box projection;
- footrest/toe-kick clearance;
- monitor eye line and viewing distance;
- mouse/keyboard reach;
- laptop/dock location;
- outlet/USB access without cables crossing the knees.

Pass when: the desk feels usable for a real workday, not just a short laptop session.

---

## 4) Recommended monitor mechanism: stow-low rising VESA spine

### Concept

Build a short structural monitor spine at the driver wall/desk rear corner. During travel and roof lowering, the monitor rests face-down or low in a padded cradle. During work mode, the spine raises or pivots into the roof-up headspace and an Ergotron-like arm provides fine adjustment.

### Mechanical stack

- **Base frame:** `15-series` T-slot or similarly stiff structure tied into the desk/fridge lower frame and a wall-side vertical member. Avoid a desk-clamp-only mount.
- **Rising member:** nested T-slot, linear rail, or locking slide pair. It only needs enough stroke to lift the VESA pivot/arm from stow height into working height after the roof is up.
- **Assist:** gas strut or counterbalance spring is preferred for simplicity. A `12V` linear actuator is optional only if it has limit switches, manual override, and no ability to jam during roof-close prep.
- **VESA carriage:** heavy plate across two vertical points, not a single thin bracket. The adjustable monitor arm bolts to this carriage for fine positioning.
- **Cradle:** face-down tray at/near desk level with raised perimeter bumpers or VESA/back-shell supports so the LCD surface itself is not loaded.
- **Travel lock:** captive spring pin or over-center latch locks both the carriage and the monitor angle. The adjustable arm is unloaded by hard stops/padded supports.

### Deploy sequence

1. Roof up and fabric clear.
2. Release the monitor travel latch.
3. Raise the mast/carriage until the mechanical stop engages.
4. Rotate/swing monitor from face-down cradle to vertical working position.
5. Set arm tension and final monitor distance/height.
6. Confirm cable chain is in its free path.

### Stow sequence

1. Return monitor to the marked “stow angle.”
2. Fold or rotate into the cradle; confirm no pressure on the LCD panel.
3. Collapse/lower the mast until the roof-safe hard stop engages.
4. Engage the captive travel pin/latch.
5. Confirm the cable chain/service loop lies below the roof-down sweep line.
6. Lower roof only after the visible roof-safe marker is green/engaged.

### Cable management

- Use a small drag chain or hinged cable guide from the fixed desk frame to the moving VESA carriage.
- Keep display/data/USB-C/low-voltage DC in the moving chain. Do not run loose AC cord loops through the moving mechanism.
- Provide strain relief at both fixed and moving ends.
- Add a quick-disconnect service point near the VESA plate so the monitor can be removed without disassembling the desk.
- Label both ends of HDMI/DisplayPort/USB-C/power leads.

### Why this is preferred

- Keeps roof-down height low.
- Lets the monitor become solidly braced in work mode.
- Protects the arm from travel vibration loads.
- Preserves desk surface use when deployed.
- Creates a vertical “shield” for shallow storage cubbies when stowed.

---

## 5) Backup monitor mechanisms

### Option B: under-desk flip-up monitor garage

Use if the rising spine conflicts with windows, heater ducts, or roof sweep.

- Monitor lives in a shallow cassette below the rear half of the desk.
- A torque hinge/gas strut flips it up into working position.
- Pros: very roof-safe, simple stow state, protected screen.
- Cons: consumes knee depth and may force a shallower tech drawer.

Only use if the under-desk envelope still leaves full-time knee comfort.

### Option C: wall-pocket quick-release monitor

Use if travel robustness matters more than one-motion deployment.

- Monitor has VESA quick-release.
- Travel mode: monitor drops into a padded vertical sleeve along the driver wall or behind the desk-side storage face.
- Work mode: monitor clips onto a rigid arm/mast.
- Pros: most robust for rough travel and roof closing.
- Cons: less elegant daily setup; cables need quick-disconnect discipline.

### Option D: removable monitor-as-lid/storage shield

- Monitor rests face-down in a raised-lip “lid” over shallow cubbies.
- The VESA plate doubles as the lid hinge/prop connection.
- Use only if the panel can be supported on bezel/back-shell structure, never on the LCD surface.

---

## 6) Desk module design

### Desk top

- Final material direction: the selected `47 in` live-edge Bubinga Desk, visually paired with the `48 in` Bubinga Galley.
- Prototype/MVP material: `3/4 in` plywood or laminated birch remains valid for fit testing and can act as the pattern for support, cable, and mechanism locations before the Bubinga is drilled or trimmed.
- Shape: slightly radiused front edge; clipped or rounded aisle-side corner to avoid hip strikes.
- Depth: favor enough forearm support for typing/mousing; avoid going so deep that entry/aisle movement suffers.
- Mounting: T-slot underframe or cleats tied into the driver-wall service spine; avoid relying on a single Lagun-style point for the primary full-time desk unless used only as a fold-out auxiliary leaf.
- Finish: satin polyurethane or equivalent durable clear film finish; seal top, underside, edges, cable/grommet holes, mounting holes, and any end grain. Epoxy should be limited to void/check stabilization unless a deliberate plastic-gloss surface is chosen.

### Ergonomic layout

- Keep a clear knee bay under the primary typing/mousing zone.
- Use shallow storage on the wall side and above/behind the monitor, not in the knee zone.
- Add a toe/foot rail or footrest if the chosen chair/stool height requires it.
- Keep the primary outlet/USB-C station reachable with one hand while seated.
- Keep the laptop dock either:
  - vertical in a cooled wall-side sleeve; or
  - on a shallow shelf above the desk surface, not on the main mousing area.

### Desk expansion without permanent bulk

- Add a small aisle-side fold leaf only for temporary paperwork/food, with a positive latch in both open and closed states.
- Avoid making the fold leaf the monitor support path.
- Consider a slide-out “mouse wing” if the fixed top must remain narrow.

### Surface details

- Add a front cable slot/grommet only where it does not spill drinks into electrical cavities.
- Use a removable desk mat or thin cork/neoprene liner for sound and vibration, not a permanently glued soft layer that traps dirt/water.
- Add a warm-white task LED under the monitor/storage lip and a dim red/amber night strip under the desk edge.

---

## 7) Electrical closet / DC shelf / shallow storage module

The driver side no longer owns the Iceco/fridge. Use the freed driver-side volume for a disciplined electrical/workstation interface, not random deep storage.

### Electrical closet and DC shelf

- Electrical closet/panel can extend vertically up to the `46 in` maximum interior build height, subject to roof/window/entry clearance.
- A shallow shelf/box may project toward the computer desk/camper entry for DC electronics, laptop plugs, chargers, USB-C/PD, router/Starlink power, the camper audio source face (`Kicker 46KMC2` if selected), and labeled office/audio circuits.
- Keep AC, DC, audio signal, and data paths separated or physically partitioned; label any mixed-adjacent service cavity clearly.
- Keep power bricks, receptacles, and audio source wiring out of spill paths from the desk front edge.
- Ventilate power electronics; do not trap laptop docks, USB-C PD supplies, Starlink DC conversion hardware, or audio electronics in sealed acrylic boxes without airflow.

### Diesel-heater base zone

- Purchased heater baseline is the LF Bros `5 kW / 12V / 10 L Split Pro` kit with T4S hardwired LCD controller and wireless remote, now supplied from the separately purchased EVIL ENERGY `10 gal` aluminum tank/feed/vent package. The LF Bros plastic tank is reassigned to graywater and must remain never-fueled. The heater body is approximately `14.6 L x 3.5 W x 5.9 H in`; preserve the real connectors, clamps, service loops, and insulation/guarding beyond that bare envelope.
- Install the heater **horizontal and upright**, low in the driver-side utility zone. The large cabin-air ends stay inside: rear/cold-air inlet with at least `10 cm / 4 in` of open intake space, and front/warm-air outlet with a smooth unrestricted duct path. Do not rotate the heater onto its side merely to make the underside combustion ports face an electrical backer.
- The underside carries the combustion-air inlet, exhaust outlet, small fuel inlet, and four mounting studs. Those combustion connections should pass through a sealed metal floor plate/turret directly below the heater. Do **not** route the hot exhaust through plywood, the electrical backer, or an interior electrical cavity and then turn it downward.
- LF Bros' flat-metal demonstration uses the supplied pattern/plate, two `30 mm` holes for combustion exhaust/intake, and the four stud holes. Hiatus has a layered plywood/insulated/corrugated-bed floor, so the controlling cut is the actual sealed metal turret/plate selected for this floor stack; dry-fit that part and inspect beneath the truck before copying the simple two-hole demonstration.
- Turret-cut prep (`2026-09-02` owner report): the Lonseal circle is scored and peeled, with a thin top plywood layer removed inside the waste circle; that shallow recess accepts the physical turret cleanly. The unused routed `1/2 in` plywood template fits as a rigid jigsaw shoe riser. Before the plywood cut, remove the nearby `12V` battery and isolate its terminals, and loosen/remove only enough adjacent extrusion to keep the jigsaw shoe/template flat and unobstructed.
- Plywood/bed cut sequence: verify the wood blade at **maximum downward stroke** through the real `1/2 in` riser leaves about `1/8-3/16 in` of plywood over the aluminum; do not rely on nominal blade length alone. Add rigid shim or shorten the disposable blade if needed. Drill the starter hole inside the waste, use a clean wood scroll blade with orbital action off, and break the remaining thin plywood skin inward/upward. Remove the disk and EPS, inspect the exposed bed and underside again, then cut the aluminum separately with a short `18-24 TPI` bi-metal/nonferrous blade, orbital action off, before deburring, vacuuming chips, coating the edge, and completing the two seal boundaries.
- Outside only: connect the supplied corrugated exhaust and muffler with metal clamps/P-clamps, keep a continuous slight fall for condensate, and use broad sweeps rather than a hard `90-degree` elbow at the heater. Keep the muffler and entire exhaust path outside, separated and shielded from fuel line, pump, undercoating, wiring, plastic, openings, and the combustion intake. Aim the final outlet away from the intake and occupied openings.
- Route the combustion intake separately outside, protected from wheel spray and road debris. Its end must not point in the same direction or sit where it can ingest the heater exhaust.
- Purchased fuel feed is `tank lower -10AN outlet -> -10AN female / 1/8 NPT male adapter -> 1/8 NPT stainless shutoff -> 1/8 FNPT / 3/16 in barb -> short LF Bros thick black rubber connector -> original 5 mm OD / 2 mm ID rigid line -> filter -> external metering pump -> heater`. The thick black hose is cut into short transition sleeves; it is not the long fuel run. Leave the other lower outlet capped. Use diesel-rated sealant only on tapered NPT joints per its instructions; AN joints seal on the flare seat, so inspect those seats and put no tape/sealant on AN threads.
- Purchased vent is `upper -10AN port -> -10AN female / 5/16 in barb -> NBR hose -> upright remote rollover valve outside`; cap the other upper port with the cap freed from the connected lower outlet after delivered-hardware verification. Verify whether the filler cap is sealed or vented: the remote valve must be the only atmospheric vent path unless any cap vent has equivalent rollover shutoff. Mount the pump in its rubber clamp close to the tank, within `2 m` of the heater, with the **outlet toward the heater and angled upward about 45 degrees**. Keep the tank, fill, vent, filter, and pump outside the open battery/electrical/living bay or in liquid-tight externally vented containment; only a protected small fuel line should enter the heater zone.
- Tank fit is not released by purchase. Prove positive restraint for approximately `86 lb` full mass, filler/shutoff access, upright external vent, liquid containment, and complete storage-module/service geometry. Bench-meter the listed `3-90 ohm` sender before wiring it to an unused Cerbo Tank `DATA/GND` pair.
- The main harness branches to heater, pump, T4S controller, and `12V +/-`. The pump is controlled by the heater ECU; it gets no separate switch. Mount the T4S inside at a representative cabin-temperature location away from the hot-air outlet; the handheld remote is wireless and requires no wire or truck cut.
- Feed the heater from the fused `12V` system, never the `48V` house bank. Preserve uninterrupted power through the controller-commanded cooldown; do not use a battery/master switch as the normal shutdown. Existing `C-22` is a `15A` branch with `14 AWG` duplex and an assumed short run; measure the actual route and use `12 AWG` if the run is not very short or startup voltage-drop testing is marginal.
- Freeze the heater/turret, underbody exhaust/intake/muffler, tank/filter/pump, fuel-line pass-through, controller plug, and power-harness service loops before final battery cable landing. Preserve access to every clamp and connector without removing the batteries.

### Shallow storage around the desk

Use otherwise dead vertical/shallow volume without hurting ergonomics:

- **Above/behind desk shelf:** laptop dock, router/Starlink power, chargers, headset, cables, paper notebooks.
- **Narrow side cubbies:** vertical laptop/tablet sleeve, file slot, bottle slot, small trash slot.
- **Desk-front/side panel:** light bungee grid or mesh pocket only where it cannot snag knees or entry movement.
- **Service strip:** removable panel for office power, data leads, monitor cables, and heater/electrical inspection.

Do not add deep drawers directly over/around the desk if they block leg movement, service access, ventilation, or roof-safe monitor stowage.

---

## 8) Storage mechanisms that preserve ergonomics

### Shallow monitor-shield cubbies

When the monitor is stowed, it can act as a protective face/shield for shallow cubbies behind it:

- smoke-grey acrylic doors or sliding covers;
- elastic/mesh retainers inside each cubby;
- foam/rubber bumpers so contents cannot touch the LCD;
- labels for daily office kit: dock, mouse, keyboard, chargers, notebook, medication/EDC, glasses.

### Toe-kick false bottom

Use a raised lower rail/deck under the desk/electrical shelf zone:

- storage for seldom-used cables, spare parts, tie-downs, tools, or flat items;
- cable chase for desk/monitor/DC-electronics low-voltage runs;
- removable panels with finger holes or quarter-turn fasteners;
- recessed toe space at the desk bay so feet do not hit a vertical cabinet face.

Keep high-current battery conductors and service disconnects accessible and protected; do not turn the electrical closet into hidden miscellaneous storage.

### Bench step / electrical closet storage

- The cabover step/bench can gain storage, but battery service comes first.
- Use hinged/removable tops with mechanical stays, not loose lift-off panels that become projectiles.
- Keep battery terminals, Class T fuses, disconnects, shunt, and Lynx/service points reachable without unloading the whole camper.
- If heated/vented storage is added near the diesel heater, isolate it from battery/electrical service spaces and use temperature-controlled airflow.

### Soft storage where bodies move

At shoulder/hip/knee zones, prefer soft pockets, mesh, elastic, or rounded shallow bins over hard protruding drawers. A daily workstation should not punish entry/exit or chair movement.

---

## 9) Heat, noise, and electronics protection

### Diesel heater zone

- Keep combustion/fuel/exhaust routing separate from desk electronics and storage cavities.
- Preserve access to the heater body, pump, filter, fuel line, exhaust/intake clamps, and serviceable joints.
- If using a warm-air branch toward batteries or desk comfort, include a damper or removable duct section and avoid direct hot air on the monitor/laptop.

### Work noise and vibration

- Add anti-rattle tape to T-slot/panel contact points.
- Use hex/sound panels or fabric-wrapped absorption on large reflective wall/desk surfaces, but do not block ventilation.
- Keep monitor, fan, electronics, heater-adjacent panels, and service wiring accessible so noise problems can be fixed after shakedown.

### Electronics heat

- Give the laptop dock, monitor power brick, USB-C PD station, router, and Starlink DC conversion hardware a ventilated tech cubby.
- Avoid sealed acrylic boxes for power electronics unless forced ventilation is added.
- Keep AC receptacles and power bricks away from spill paths at the desk front edge.

---

## 10) Travel locks and safety interlocks

Every moving workstation element needs a primary mechanical restraint:

- monitor carriage/mast: captive pin or locking slide stop;
- monitor face-down cradle: over-center latch or compression latch;
- monitor arm: strapped or clamped into a padded, positively retained hard-stop cradle; the strap is a secondary restraint and must not load the LCD face, arm joints, or desk edge;
- desk fold leaf: latch open and latch closed;
- drawers/bins: positive marine/RV latch, not just soft-close slides;
- service panels: quarter-turn/captive fasteners;
- cable loops: clips or drag chain so nothing can stand up into the roof path.

Add a visible “drive/roof-down checklist” near the door:

1. Monitor down + pin engaged.
2. Cable chain flat / no proud loop.
3. Desk leaf latched.
4. Storage doors latched.
5. Electrical/heater service panels closed.
6. No item above marked roof-safe line.

Optional upgrade: a simple microswitch/reed-switch indicator on the monitor stow latch that lights a small green LED when the monitor is in the roof-safe position. Treat it as an aid, not the only safeguard.

---

## 11) Service access rules

- No fuse, disconnect, shunt, heater service joint, DC power-conversion module, or office power distribution point should require removing the entire desk to inspect.
- Use removable side panels around the desk/electrical shelf/heater-service zone.
- Use service loops and labeled quick disconnects for monitor/data/power leads.
- Keep AC and DC/data paths separated or physically partitioned; label mixed-adjacent service cavities clearly.
- Preserve a tool path for tightening T-slot bolts, VESA bolts, and slide hardware after vibration shakedown.
- Use witness marks on structural and monitor-arm fasteners after final adjustment.

---

## 12) Build sequence

1. **Mock envelopes first:** cardboard/tape the electrical closet, electrical step box, DC shelf/box, `24 in x 48 in` wheel-well desk, monitor stow block, diesel-heater service zone, and storage tower inside the installed camper.
2. **Pass roof sweep:** prove the stowed monitor, DC shelf, and all cubbies stay below the roof-down envelope.
3. **Pass chair/desk test:** sit and work at the mockup for at least one real session before committing storage below/around knees.
4. **Build lower frame:** desk/electrical/heater service spine first; keep skins/removable panels temporary.
5. **Build monitor mechanism on bench:** prove stow/deploy/latch/cable path outside the camper.
6. **Install monitor mechanism:** attach to structural spine, not just desktop; add hard stops and travel latch.
7. **Add storage skins:** shallow cubbies, acrylic/mesh retainers, toe-kick panels, and LED strips after mechanisms pass.
8. **Shakedown:** drive, re-torque, look for screen movement, latch chatter, fridge slide noise, cable rub, hot spots, and workday ergonomic pain points.

---

## 13) Acceptance tests

### Roof-close test

- Monitor fully stowed and latched.
- Cable chain/service loops below roof-safe line.
- Roof cycled open/closed slowly without contact.
- Test repeated after loading the storage cubbies.

### Workday test

- Complete a multi-hour laptop + monitor session.
- Confirm monitor height/distance, keyboard/mouse comfort, leg clearance, outlet access, fan/fridge noise, and lighting.
- Note any pressure points or awkward cable crossings.

### Travel test

- Drive mixed surfaces with monitor stowed and driver-side service panels loaded/latched.
- Inspect latches, VESA fasteners, T-slot joints, service-panel fasteners, storage doors, and anti-rattle surfaces.
- Re-torque/witness-mark after the first drive cycle.

### Thermal/noise test

- Run laptop/dock, monitor, USB-C PD, Starlink/router, DC shelf electronics, and heater/ventilation in realistic combinations.
- Check tech cubby temperature, heater-adjacent panel temperature, fan noise, and whether heat is trapped around power bricks.

---

## 14) Open design choices

- Exact monitor mechanism: rising mast vs under-desk flip-up vs quick-release sleeve.
- Exact installed support/depth/height and any trim/no-drill zones after chair and roof-envelope measurement against the selected `47 in` Bubinga Desk piece.
- Whether the monitor uses AC brick, DC-native power, or USB-C display/power through a dock.
- Final storage split between shallow cubbies, soft pockets, toe-kick, and bench-step storage.
- Final hardware ecosystem for latches, slides, and T-slot standard.
- Final desk finish sample: satin walnut film finish by default; epoxy only for local fills unless intentionally selected.
