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

# Driver-Side Workstation, Monitor, Fridge, and Storage Mechanisms

As-of date: `2026-05-04`

Purpose: capture a buildable design direction for the driver/left-side workstation zone so the camper can support full-time work, preserve pop-down roof clearance, and gain storage without ruining ergonomics.

Status: **draft implementation baseline**. Do not convert this into exact extrusion cuts, drawer-slide lengths, panel skins, or final penetrations until post-install shell measurements, Iceco envelope checks, and roof-popdown sweep tests pass.

Related docs:
- `docs/core/SYSTEMS.md`
- `docs/core/TRACKING.md`
- `docs/implementation/INTERIOR_furniture_layout_and_galley.md`
- `docs/plans/INSTALL_MINUS_12_READINESS_PLAN.md`

Generated concept diagram:

- ![Driver workstation monitor mechanism](../../media/diagrams/interior-furniture-2026-05-04/02-driver-workstation-monitor-mechanism.png)

Diagram caveat: this image is a mechanism concept, not a fabrication drawing. The monitor stow/deploy geometry, roof-safe line, Iceco slide, cable chain, and latch positions must be validated with the real installed shell.

---

## 1) Design thesis

Use the driver wall as a **service spine**, not as a deep drawer wall.

Overall interior layout owner: [INTERIOR_furniture_layout_and_galley](INTERIOR_furniture_layout_and_galley.md). This workstation doc owns the driver-side mechanism details inside that office-first layout.

Recommended primary architecture:

1. **Fixed lower structure:** desk/fridge/electrical modules tie into a low, rigid driver-wall frame that stays below the roof-down envelope.
2. **Stow-low monitor cassette:** monitor stores face-down or low in a padded cradle at/near the desk surface, with no travel load carried by the adjustable arm.
3. **Deployable mast/hinge:** only after the roof is popped, a short 80/20 mast or hinged VESA carriage raises/rotates the monitor into working position.
4. **Shallow storage wall:** use shallow cubbies, vertical sleeves, mesh pockets, and toe-kick storage around the desk/Iceco zone rather than filling knee space with drawers.
5. **Positive travel locks:** every moving element gets a mechanical latch/pin; magnets/friction are secondary only.

Bottom line: the monitor can feel Ergotron-sturdy while working, but it must become a **latched cargo item** while driving or lowering the roof.

---

## 2) Working constraints to preserve

### Layout constraints

- Driver/left wall sequence currently includes:
  - top/front-left electrical closet + `3x 48V` batteries / bench step into cabover;
  - `12V` buffer battery / ground and service paths;
  - diesel heater zone;
  - middle-left computer desk;
  - bottom/rear-left Iceco fridge/cooler because the old top-right location will not fit/open.
- Current furniture CAD is reference-only after the Iceco/water-tank dry fit mismatch.
- `15-series` extrusion should be reserved for actual dynamic/heavy modules: electrical cabinet, fridge slide/base, or workstation/monitor spine. Use `10-series`/lighter rail for accessories, panels, cubbies, and trim.

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
   - Iceco/fridge tower;
   - door-side aisle edge.
4. Add a physical margin before finalizing any stowed hardware height.
5. Create a simple go/no-go template or marked batten for future checks.

Pass when: roof can close with the monitor stowed, cable loop controlled, and no hard contact or fabric pinch.

### Gate W2: Iceco envelope

Measure and record:

- body length/width/height including handles;
- hinge/lid sweep and required hand clearance;
- compressor vent side(s), intake/exhaust grille locations, and minimum open-air path;
- cord exit and bend radius;
- whether a slide is required for lid access;
- aisle/door interference at full slide extension.

Pass when: the fridge opens, ventilates, and locks in both travel and parked modes.

### Gate W3: seated work envelope

Mock with cardboard/plywood:

- chair/stool position;
- desk height/depth;
- knee width/depth;
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

## 7) Iceco fridge/cooler module and vertical storage

### Fridge tray

- Put the Iceco on a dedicated tray/slide with positive travel lock and secondary strap or draw latch.
- The slide/base is a valid `15-series` use case if the fridge mass, extension moment, or rough-road loads demand it.
- Add hard stops so the fridge cannot overextend into the aisle/door or yank the power cord.
- Maintain an accessible drain/cleaning path if the unit has one.

### Venting

- Do not skin the compressor side tightly.
- Prefer a lower cool-air intake and upper warm-air exhaust/chimney path around the fridge tower.
- If the compartment is boxed, add a small thermostatic `12V` fan and washable dust screen.
- Keep sound treatment out of the direct vent path and away from heater/fire-risk zones.

### Storage around the fridge

Use the otherwise dead vertical volume as shallow/tall storage:

- **Above-fridge shelf:** soft bins for food, office supplies, headset, cables, paper notebooks.
- **Narrow side tower:** vertical laptop/tablet sleeve, router/Starlink power cubby, file slot, bottle slot, small trash slot.
- **Fridge-front panel:** bungee grid or MOLLE-style panel for light items only.
- **Rear service strip:** removable panel for fridge power, vent fan, and any heater/fuel routing inspection.

Do not add deep drawers directly over/around the fridge if they block lid opening, vent flow, or service access.

---

## 8) Storage mechanisms that preserve ergonomics

### Shallow monitor-shield cubbies

When the monitor is stowed, it can act as a protective face/shield for shallow cubbies behind it:

- smoke-grey acrylic doors or sliding covers;
- elastic/mesh retainers inside each cubby;
- foam/rubber bumpers so contents cannot touch the LCD;
- labels for daily office kit: dock, mouse, keyboard, chargers, notebook, medication/EDC, glasses.

### Toe-kick false bottom

Use a raised lower rail/deck under the desk/fridge zone:

- storage for seldom-used cables, spare parts, tie-downs, tools, or flat items;
- cable chase for desk/fridge low-voltage runs;
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

### Fridge and work noise

- Isolate fridge tray with thin neoprene/rubber pads where mechanically appropriate.
- Add anti-rattle tape to T-slot/panel contact points.
- Use hex/sound panels or fabric-wrapped absorption on large reflective wall/desk surfaces, but do not block ventilation.
- Keep pump/fridge/fan wiring and mounts serviceable so noise problems can be fixed after shakedown.

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
- fridge slide: locking slide plus secondary strap/latch;
- desk fold leaf: latch open and latch closed;
- drawers/bins: positive marine/RV latch, not just soft-close slides;
- service panels: quarter-turn/captive fasteners;
- cable loops: clips or drag chain so nothing can stand up into the roof path.

Add a visible “drive/roof-down checklist” near the door:

1. Monitor down + pin engaged.
2. Cable chain flat / no proud loop.
3. Fridge slide locked + strap engaged.
4. Desk leaf latched.
5. Storage doors latched.
6. Heater/service panels closed.
7. No item above marked roof-safe line.

Optional upgrade: a simple microswitch/reed-switch indicator on the monitor stow latch that lights a small green LED when the monitor is in the roof-safe position. Treat it as an aid, not the only safeguard.

---

## 11) Service access rules

- No fuse, disconnect, shunt, heater service joint, fridge vent fan, or power-conversion module should require removing the entire desk to inspect.
- Use removable side panels around the desk/fridge tower.
- Use service loops and labeled quick disconnects for monitor/data/power leads.
- Keep AC and DC/data paths separated or physically partitioned; label mixed-adjacent service cavities clearly.
- Preserve a tool path for tightening T-slot bolts, VESA bolts, and slide hardware after vibration shakedown.
- Use witness marks on structural and monitor-arm fasteners after final adjustment.

---

## 12) Build sequence

1. **Mock envelopes first:** cardboard/tape the electrical closet, desk, monitor stow block, Iceco, fridge slide, and storage tower inside the installed camper.
2. **Pass roof sweep:** prove the stowed monitor and all cubbies stay below the roof-down envelope.
3. **Pass chair/desk test:** sit and work at the mockup for at least one real session before committing storage below/around knees.
4. **Build lower frame:** desk/fridge/electrical service spine first; keep skins/removable panels temporary.
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

- Drive mixed surfaces with monitor stowed and fridge loaded.
- Inspect latches, VESA fasteners, T-slot joints, slide locks, storage doors, and anti-rattle surfaces.
- Re-torque/witness-mark after the first drive cycle.

### Thermal/noise test

- Run fridge, laptop/dock, monitor, USB-C PD, Starlink/router, and heater/ventilation in realistic combinations.
- Check fridge exhaust temperature, tech cubby temperature, fan noise, and whether heat is trapped around power bricks.

---

## 14) Open design choices

- Exact monitor mechanism: rising mast vs under-desk flip-up vs quick-release sleeve.
- Exact desk length/depth/height after chair and roof-envelope measurement.
- Whether the Iceco needs a full slide or can remain fixed with a lid-clearance cutout.
- Whether the monitor uses AC brick, DC-native power, or USB-C display/power through a dock.
- Final storage split between shallow cubbies, soft pockets, toe-kick, and bench-step storage.
- Final hardware ecosystem for latches, slides, and T-slot standard.
