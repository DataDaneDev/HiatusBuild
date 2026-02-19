# Project

## Snapshot
- As-of date: February 19, 2026
- Install milestone: May 7, 2026
- Mission: build a reliable off-grid camper workspace suitable for full-time professional use

## Fixed constraints
- Truck platform is fixed: 2021 F-350 Regular Cab Long Bed
- Existing truck modifications are fixed: 2.5" lift, 37" tires, 4.88 regear
- Camper delivery/install readiness date is fixed: May 7, 2026

## Objectives
- Support standard workdays without power anxiety
- Maintain reliable internet for meetings and high-value workflow tasks
- Provide ergonomic, repeatable workstation setup
- Keep system serviceable and safe in multi-climate travel use

## Scope
- In scope: electrical, charging, solar, communications, interior structure/cabinetry, operations process, maintenance tracking
- Out of scope for phase 1: non-critical aesthetic upgrades and major unrelated truck mechanical projects

## Requirements baseline (draft)
- Workday autonomy target: modeled profiles (BOM loads + owner-supplied office loads) indicate `3,530 Wh/day` (`core_workday`) and `4,202 Wh/day` (`winter_workday`); battery reserve floor policy is `20%` minimum SOC
- Connectivity reliability target: Starlink is planned primary path; fallback strategy still TBD
- Thermal comfort and electronics protection limits: TBD
- System safety requirements: fusing, disconnects, wire protection, labeling, service access

## Workbook intake (from `Camper Build.xlsx`, imported 2026-02-11)
- Current camper config notes indicate Hiatus base model with vertical lower frame, double back doors, additional windows, Maxxair fan, and overhead LEDs.
- Consult note indicates "Into production 3rd week of February" and that delivery timeline adherence was reported as strong.
- Cabover reference captured: approximately `41 in`.
- Truck config in workbook matches fixed constants: 2021 F-350, 8 ft bed.

## Scope clarifications from workbook
- In scope for Phase 1 includes office-first electrical architecture, Starlink support, cabinetry/workstation, and core plumbing.
- Truck mechanical upgrades listed as "skip for now" remain out of scope for Phase 1.
- Several passthrough decisions (solar, shore power, diesel/propane routing) are still pending and tracked in `docs/TRACKING.md`.

## Milestone plan (draft)
- M0: requirements baseline frozen
- M1: system architecture selected (electrical + comms + thermal)
- M2: BOM v1 complete and procurement started
- M3: CAD fit checks and wiring route plan complete
- M4: subsystem bench validation complete
- M5: install-readiness checklist complete
- M6: install date (May 7, 2026)
- M7: shakedown and punch-list closure

## Build sequencing baseline (as-of 2026-02-16)
- Build sequencing is now tracked as an overlapping phase plan (not strict serial trades).
- Target install date remains fixed at May 7, 2026 (`80` days from this baseline date).
- Accelerated procurement phase (`Batch A+`) is active in `bom/bom_estimated_items.csv` with core electrical plus bench-build wiring/consumables pulled into February 16 to February 21.
- Detailed stage-by-stage order of operations, dependencies, and draft date windows:
- `docs/PROJECT_build_order_of_operations.md`

## Immediate next decisions
- Execute `Batch A+` purchase wave and capture vendor/ETA status for rows `3`, `4`, `5`, `6`, `7`, `10`, `11`, `12`, `16`, `17`, `18`, `20`, `21`, `22`, `23`, `26`, `27`, `28` through `45`, `52`, `53`, `60`, `117`
- Validate the full fuse schedule against final holder/SKU selections and cart contents for the locked Lynx architecture
- Validate shared 12V junction behavior (`Orion + buffer battery`) including `F-11` and `SW-12V-BATT` service isolation behavior under office/galley USB station loads
- Freeze autonomy policy using modeled profiles (BOM + owner-supplied office loads) with a `20%` minimum SOC reserve floor
- Confirm passthrough locations (solar, shore, fuel/heater routing) with Hiatus before production lock
- Lock hardwall-popup solar jumper approach details (connector family, passthrough hardware SKU, and service-loop length for roof travel)
- Validate Sterling `BB1248120` + `BBR` current-limit operating envelope on the factory `240A` alternator; keep Mechman 370A alternator + Big 3 as purchase-later path pending fitment confirmation and install timing
- Choose final solar panel type (flex vs rigid)
- Lock interior/exterior T-slot or strut mounting ecosystem and bracket/accessory interface standard

## Unblock sprint (next 72 hours)
Purpose: convert “planning certainty” into a buildable, orderable physical layout (especially the electrical cabinet), without CAD’ing every bend radius.

### Outcome targets (definition of done)
By end of the sprint, you can point to a single “electrical module footprint” and say it is real:
1. Electrical cabinet envelope is locked (W x H x D), plus required service-access clearance.
2. All major electrical components fit on a 1:1 backer board mockup with cable exits accounted for.
3. A cabinet strategy is selected that matches build skills (Phase 1 = simple, serviceable; Phase 2 = pretty skins/lighting).
4. A purchase gate is cleared: you either place `Batch A+` orders confidently or you have a specific list of what must change first.

### Day-by-day plan
#### Day 1 (today)
1. Pick the cabinet zone and commit to a *bounding box* (not final cabinetry): “electrical lives here”.
2. Write 10 “non-negotiables” for the electrical cabinet:
   - example set: short high-current runs, no buried fuses, strain relief at every entry, AC and DC separation, ventilation path, battery restraint, drip-loop mindset.
3. Decide the Phase 1 aesthetics rule:
   - Recommended: **no sliding doors** in Phase 1 (hinged or fully removable panels only). Plan for frosted polycarbonate + LEDs later by reserving space and a wire path.

#### Day 2
1. Do a 1:1 physical layout of the electrical stack:
   - On a scrap plywood/foam board backer, place full-size paper/cardboard templates for batteries, MultiPlus, Lynx, shunt, DC-DC, breakers, cable glands.
   - Add “keep-out” zones for cable bend room and service tool access.
2. Choose entry/exit points and routing corridors (don’t over-precision this):
   - define: “48V trunk exits left”, “12V exits down/toe-kick chase”, “AC exits up/right”, etc.
3. If anything doesn’t fit cleanly, resize the cabinet envelope now (this is cheaper than re-buying).

#### Day 3
1. Build a tiny prototype of your intended cabinetry method:
   - a short 80/20 frame segment + one panel/door attachment method (hinge OR magnets OR quarter-turn fasteners).
   - goal: confirm you can build something rigid, square, and non-rattly without woodworking-level joinery.
2. Update carts using a simple gate:
   - Buy now: items that are layout-insensitive and/or needed for bench-testing (core protection, bus covers, terminals/lugs, wire management, disconnects, mounting backer materials).
   - Buy after footprint lock: the expensive “hard-to-return” items whose exact mounting orientation/clearance matters most.

### Cabinetry approach (recommended)
- Treat 80/20 as the *structure* and simple panels as the *skins*.
- Prioritize serviceability over concealment: every fuse/disconnect should be reachable without uninstalling major devices.
- Build “functional first”: once the electrical module works and survives vibration, add frosted panels + LED backlighting as a Phase 2 overlay.
