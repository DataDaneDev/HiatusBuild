# Project

## Document role
- This file owns project scope, fixed constraints, milestone framing, sequencing posture, and near-term priority calls.
- Keep detailed subsystem design in `docs/core/SYSTEMS.md` and final `48V` electrical architecture in `docs/core/ELECTRICAL_48V_ARCHITECTURE.md`.
- Keep decision/risk/open-question state in `docs/core/TRACKING.md`, not as a second decision log here.
- Keep exact topology, fuse, conductor, and bench procedure detail in `docs/implementation/`.

## Snapshot
- As-of date: March 20, 2026
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

## Current pre-camper execution focus (electrical + flooring)
- Use `docs/plans/STARTER_PLAN_electrical_and_flooring_pre_camper.md` as the active day-to-day checklist while the camper shell is not yet in hand.
- Use `docs/core/ELECTRICAL_48V_ARCHITECTURE.md` as the canonical `48V` design reference while laying out the electrical module and alternator-control path.
- Active work now includes both reversible and truck-only irreversible tasks (EPS install, subfloor prep, bench board drilling/layout).
- Defer shell-dependent irreversible work (final penetrations, shell-run final cut lengths, permanent finish-floor bonding).

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
- Several passthrough decisions (solar, shore power, diesel/propane routing) are still pending and tracked in `docs/core/TRACKING.md`.

## Milestone plan (draft)
- M0: requirements baseline frozen
- M1: system architecture selected (electrical + comms + thermal)
- M2: BOM v1 complete and procurement started
- M3: physical fit checks and measured wiring route plan complete (CAD optional/reference-only)
- M4: subsystem bench validation complete
- M5: install-readiness checklist complete
- M6: install date (May 7, 2026)
- M7: shakedown and punch-list closure

## Build sequencing baseline (as-of 2026-03-18)
- Build sequencing is tracked as an overlapping phase plan (not strict serial trades).
- Target install date remains fixed at May 7, 2026 (`50` days from this baseline date).
- Accelerated procurement (`Batch A+`) is now historical context; current sequencing focus is AC closure, measured harness planning, and module completion.
- Detailed stage-by-stage order of operations, dependencies, and draft date windows:
- `docs/plans/PROJECT_build_order_of_operations.md`

## Immediate next decisions
- Finalize AC scope and hardware lock: shore-power chain plus final branch/receptacle count (`2` branches with final location count pending).
- Complete AC SKU-level lock and fitment validation for rows `13`, `107`, `108`, `109`, `110`, `111`, `112`, and `123`.
- Execute bench-build electrical closet layout and document measured run lengths; CAD lengths are reference-only for material planning.
- Keep the manual alternator shutdown path simple: Ford `Upfitter #3` will be the `WS500` enable/disable control in the finalized `48V` design.
- Validate shared 12V junction behavior (`Orion + buffer battery`) including `F-11` and `SW-12V-BATT` under office/galley USB station loads.
- Reserve solar passthrough/routing space now, but defer final flexible-panel procurement and string lock deeper into the build sequence.
- Confirm passthrough locations (solar, shore, fuel/heater routing) with Hiatus before production lock.
- Confirm received Mechman dual-48V kit fitment/content details, then execute Sterling return workflow (`rows 18/26`) and continue with the locked alternator migration fuse/wire baseline.
- Lock interior/exterior T-slot or strut mounting ecosystem and bracket/accessory interface standard.

## Unblock sprint (next 72 hours)
Purpose: convert planning certainty into a buildable, orderable physical layout (especially the electrical cabinet), without CAD-ing every bend radius.

### Outcome targets (definition of done)
By end of the sprint, you can point to a single electrical module footprint and say it is real:
1. Electrical cabinet envelope is locked (W x H x D), plus required service-access clearance.
2. All major electrical components fit on a 1:1 backer board mockup with cable exits accounted for.
3. A cabinet strategy is selected that matches build skills (Phase 1 = simple, serviceable; Phase 2 = pretty skins/lighting).
4. A purchase gate is cleared: you either place remaining critical-path orders confidently or you have a specific list of what must change first.

### Day-by-day plan
#### Day 1 (today)
1. Pick the cabinet zone and commit to a *bounding box* (not final cabinetry): "electrical lives here".
2. Write 10 "non-negotiables" for the electrical cabinet:
   - example set: short high-current runs, no buried fuses, strain relief at every entry, AC and DC separation, ventilation path, battery restraint, drip-loop mindset.
3. Decide the Phase 1 aesthetics rule:
   - Recommended: **no sliding doors** in Phase 1 (hinged or fully removable panels only). Plan for frosted polycarbonate + LEDs later by reserving space and a wire path.

#### Day 2
1. Do a 1:1 physical layout of the electrical stack:
   - On a scrap plywood/foam board backer, place full-size paper/cardboard templates for batteries, MultiPlus, Lynx, shunt, DC-DC, breakers, cable glands.
   - Add "keep-out" zones for cable bend room and service tool access.
2. Choose entry/exit points and routing corridors (don’t over-precision this):
   - define: "48V trunk exits left", "12V exits down/toe-kick chase", "AC exits up/right", etc.
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
