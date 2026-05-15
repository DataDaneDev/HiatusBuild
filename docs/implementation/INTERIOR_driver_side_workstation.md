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
---

# Driver-Side Workstation, Monitor, Electrical Shelf, and Storage Mechanisms

As-of date: `2026-05-14`

Purpose: capture a buildable design direction for the driver/left-side workstation and electrical-closet interface so the camper can support full-time work, preserve pop-down roof clearance, keep DC electronics/laptop plugs accessible, and gain storage without ruining ergonomics.

Status: **draft implementation baseline**, updated after the passenger-side fridge/wet-spine change. Do not convert this into exact extrusion cuts, drawer-slide lengths, panel skins, or final penetrations until post-install shell measurements, driver-side electrical closet/DC shelf checks, diesel-heater service checks, and roof-popdown sweep tests pass.

Related docs:
- `docs/core/SYSTEMS.md`
- `docs/core/TRACKING.md`
- `docs/implementation/INTERIOR_furniture_layout_and_galley.md`
- `docs/plans/INSTALL_MINUS_12_READINESS_PLAN.md`

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
  - `24 in x 48 in` desk around the wheel-well area, integrated with the electrical step box;
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
- DC shelf/box projection toward the desk/entry doors, including hip/shoulder/door interference;
- laptop plug/USB-C/AC/DC station reach from seated position;
- diesel heater body, duct, intake/exhaust/fuel-line, and service-panel access;
- cable bend radius, service loops, and AC/DC/data separation.

Pass when: electrical service, office power access, heater service, desk ergonomics, and entry movement all work without hidden service points or roof-down conflicts.

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

- Material direction: phenolic, Richlite, or laminated Baltic/birch ply with sealed edges.
- Shape: slightly radiused front edge; clipped or rounded aisle-side corner to avoid hip strikes.
- Depth: favor enough forearm support for typing/mousing; avoid going so deep that entry/aisle movement suffers.
- Mounting: T-slot underframe or cleats tied into the driver-wall service spine; avoid relying on a single Lagun-style point for the primary full-time desk unless used only as a fold-out auxiliary leaf.

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
- A shallow shelf/box may project toward the computer desk/camper entry for DC electronics, laptop plugs, chargers, USB-C/PD, router/Starlink power, and labeled office circuits.
- Keep AC, DC, and data paths separated or physically partitioned; label any mixed-adjacent service cavity clearly.
- Keep power bricks and receptacles out of spill paths from the desk front edge.
- Ventilate power electronics; do not trap laptop docks, USB-C PD supplies, or Starlink DC conversion hardware in sealed acrylic boxes without airflow.

### Diesel-heater base zone

- Keep the diesel heater low in the driver-side utility zone.
- Preserve access to heater body, duct clamps, intake/exhaust, fuel-line pass-through, filter/pump interface if inside, and serviceable joints.
- Preferred fuel direction is exterior tank/fill/pump with only a protected line passing through a grommet/bulkhead to the heater.
- Keep heater hot surfaces, ducts, and combustion/fuel paths separated from desk electronics and storage cavities.

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
- monitor arm: strapped or clamped against a padded hard stop;
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
- Exact desk length/depth/height after chair and roof-envelope measurement.
- Whether the monitor uses AC brick, DC-native power, or USB-C display/power through a dock.
- Final storage split between shallow cubbies, soft pockets, toe-kick, and bench-step storage.
- Final hardware ecosystem for latches, slides, and T-slot standard.
