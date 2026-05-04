---
aliases:
  - Hiatus project baseline
tags:
  - hiatus/core
  - hiatus/project
status: active
related:
  - "[[SYSTEMS]]"
  - "[[ELECTRICAL_48V_ARCHITECTURE]]"
  - "[[TRACKING]]"
---

# Project

## Document role
- This file owns project scope, fixed constraints, milestone framing, sequencing posture, and near-term priority calls.
- Keep detailed subsystem design in `docs/core/SYSTEMS.md` and final `48V` electrical architecture in `docs/core/ELECTRICAL_48V_ARCHITECTURE.md`.
- Keep decision/risk/open-question state in `docs/core/TRACKING.md`, not as a second decision log here.
- Keep exact topology, fuse, conductor, and bench procedure detail in `docs/implementation/`.

## Snapshot
- As-of date: April 27, 2026
- Install milestone: May 7, 2026, `9:00 AM`, at `3171 Mercer Ave, Suite 101, Bellingham, WA 98225`
- Travel constraint: truck starts in Park City, Utah and should be staged near Bellingham by the evening of May 6
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
- Use [INSTALL_MINUS_12_READINESS_PLAN](../plans/INSTALL_MINUS_12_READINESS_PLAN.md) as the active Apr 27-May 11 install-window plan. Use [STARTER_PLAN_electrical_and_flooring_pre_camper](../plans/STARTER_PLAN_electrical_and_flooring_pre_camper.md) only for detailed pre-camper electrical/flooring execution references.
- Use [ELECTRICAL_48V_ARCHITECTURE](ELECTRICAL_48V_ARCHITECTURE.md) as the canonical `48V` design reference while laying out the electrical module and alternator-control path.
- Active work now includes shore AC-in ordering, electrical closet layout/fuse matching, bed-rail dust/weather sealing, EPS trim/subfloor verification, and low-regret extrusion ordering.
- Defer shell-dependent irreversible work (final penetrations, shell-run final cut lengths, permanent finish-floor bonding) until the real camper is installed and service-map checks pass.

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
- [PROJECT_build_order_of_operations](../plans/PROJECT_build_order_of_operations.md)

## Immediate next decisions
- **Priority 1: shore-power / initial-charge readiness.** Build the AC-in-only MultiPlus charge path first: `shore source -> cord/adapter -> TT-30 inlet -> hardwired EMS -> AC-in breaker/disconnect -> MultiPlus AC-in`. Order/SKU-lock BOM rows `107`, `108`, `123`, `13`, `109`, `14`, and `114` plus glands/grommets/labels/ferrules.
- Keep AC-in and AC-out protection in separate enclosures. Do not let final AC receptacle-count churn block the AC-in charge path.
- Before first charge, reconcile the MultiPlus LiFePO4 charge profile (`56.8V` planning basis vs `58.4V` battery/manual basis), set source current limits, and charge/test one `48V` battery at a time before paralleling.
- Complete electrical closet Board A/B layout on the `1/2 in` plywood with real service access, bend radius, fuse-holder matching, and labels before wire cutting.
- **Truck bed dust/weather closeout:** remove/inspect bed rail caps, confirm old `2 in x 3 in` rail holes are not needed by Hiatus, and seal them with low-profile serviceable patches/flexible sealant without trapping water. Also seal and leak-check bed-floor drain holes, unused floor penetrations, and small corner gaps that could admit water under the subfloor.
- **Flooring gate:** trim EPS and verify three-piece plywood fit/serviceability. Do not glue Lonseal until rail/bed-floor/corner sealing is complete and leak-checked, and hardpoint/floor penetration/routing questions are cleared.
- Keep tailgate on for the Bellingham drive unless Hiatus says otherwise; confirm removal/storage plan before departure. Keep tonneau on as long as practical for weather protection.
- Treat current furniture CAD as reference-only because the Iceco/water tank dry fit invalidated the fridge location. Re-CAD block envelopes first, likely with fridge/cooler in the front-left corner.
- Order a low-regret starter extrusion/hardware package from stock lengths under `92 in`; defer drawer slides, final panels, and exact cut lengths until real shell/fridge/tank envelopes are measured.
- Add faucet/sink/drain procurement as discrete plumbing work. Decouple cold-water plumbing from final hot-water choice; treat portable propane tankless as outdoor-use-only and defer electric tanked or listed indoor/RV propane decisions until service-map freeze.
- Defer Mechman alternator installation until batteries are present, shore charging/monitoring are proven, and alternator vendor/support gates are closed.

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
