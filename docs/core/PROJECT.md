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
- As-of date: 2026-05-27
- Phase: post-install interior buildout and measured systems-layout validation
- Install milestone: May 7, 2026 Hiatus install is now historical context; the real camper shell is available for physical mockups and measurements
- Mission: build a reliable off-grid camper workspace suitable for full-time professional use

## Fixed constraints
- Truck platform is fixed: 2021 F-350 Regular Cab Long Bed
- Existing truck modifications are fixed: 2.5" lift, 37" tires, 4.88 regear
- Camper platform is fixed: installed/in-hand Hiatus shell on the F-350 long bed

## Objectives

- Support standard workdays without power anxiety
- Maintain reliable internet for meetings and high-value workflow tasks
- Provide ergonomic, repeatable workstation setup
- Keep system serviceable and safe in multi-climate travel use

## Current execution focus (post-install interior buildout)
- Use [PROJECT_build_order_of_operations](../plans/PROJECT_build_order_of_operations.md) as the active phase sequence. Use [INSTALL_MINUS_12_READINESS_PLAN](../plans/INSTALL_MINUS_12_READINESS_PLAN.md) and [STARTER_PLAN_electrical_and_flooring_pre_camper](../plans/STARTER_PLAN_electrical_and_flooring_pre_camper.md) as historical install-window/pre-camper references unless they are explicitly refreshed.
- Use [INTERIOR_furniture_layout_and_galley](../implementation/INTERIOR_furniture_layout_and_galley.md) as the current owner for the office-first passenger-side lofted fridge/wet-spine concept, separated battery bench, and `10-series` 80/20 overlay-panel direction.
- Use [ELECTRICAL_48V_ARCHITECTURE](ELECTRICAL_48V_ARCHITECTURE.md) as the canonical `48V` design reference while mechanically laying out the electrical module and alternator-control path.
- Active work now includes measured camper block envelopes, electrical module live-commissioning cleanup, fuse/device access checks, 80/20 prototype stock/hardware planning, floor/subfloor gates, and payload/weight tracking.
- Electrical status has moved past dead-layout only: the `48V` bus, SmartShunt, Orion, Cerbo, MultiPlus inverter mode, and a short limited-current shore-charge test have all been proven without observed errors.
- Defer irreversible work (final shell penetrations, shell-dependent final cable cuts, final extrusion vendor cuts, permanent skins, and finish-floor glue-down) until physical measurement, service-map, access, and post-energization checks pass.

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
- Several passthrough decisions (solar and diesel/propane routing) are still pending and tracked in `docs/core/TRACKING.md`; shore hardware is selected, with inlet/cable-support details handled during physical install.

## Milestone plan (draft)
- M0: requirements baseline frozen
- M1: system architecture selected (electrical + comms + thermal)
- M2: BOM v1 complete and procurement started
- M3: camper installed / physical shell available for real measurements
- M4: subsystem bench validation complete
- M5: measured interior block envelopes and service map complete
- M6: electrical module dead-mechanical layout and first-charge plan ready
- M7: shakedown and punch-list closure

## Build sequencing baseline (as-of 2026-05-27)
- Build sequencing is tracked as an overlapping phase plan (not strict serial trades).
- May 7 install readiness is historical context; current sequencing focus is measured interior envelopes, post-energization electrical cleanup/programming, targeted prototype extrusion/hardware ordering, and staged AC-out/alternator validation.
- CAD and AI-generated diagrams are planning references only; real camper measurements and physical mockups own final dimensions.
- Detailed stage-by-stage order of operations, dependencies, and draft date windows:
- [PROJECT_build_order_of_operations](../plans/PROJECT_build_order_of_operations.md)

## Immediate next decisions
- **Measured envelopes:** physically tape/cardboard the passenger-side lofted fridge/wet-spine skeleton, pump/accumulator board, water tank overlap, separated battery bench, driver-side electrical box/step box, `24 in x 48 in` wheel-well desk, DC shelf, diesel heater zone, and workstation before final cut lists.
- **Extrusion/furniture:** order/use 80/20 as controlled prototype stock/hardware, not a final vendor-cut enclosure. Default toward `10-series` unless real point loads or restraint needs prove otherwise.
- **Panel strategy:** use overlay/removable panels on living-facing surfaces, keep service zones exposed or quick-removable, and use magnets only for light service covers with locator/backup retention where panel loss matters.
- **Electrical:** current live-commissioning checkpoint is complete: owner confirmed `55.5V` throughout the `48V` system including at the MultiPlus, MultiPlus inverter mode came on with normal light/hum and no errors, SmartShunt and Orion are visible in VictronConnect, Cerbo GX access point/remote-console workflow is active, and a short shore-charge test ran at limited household-outlet current.
- Purchased Phase 1 AC baseline remains `shore source/adapters -> portable EMS -> shore cord -> L5-30 inlet -> single 6-way AC DIN enclosure -> 30A AC-in breaker/disconnect -> MultiPlus AC-in`, with `30A` AC-out main plus two `20A` GFCI branches for later AC-out validation. SKU lock is recorded in BOM rows `13`, `14`, `15`, `41`, `107`, `108`, `109`, `110`, `113`, `114`, `123`, `179`, and `180`; cable glands/clamps/grommets are on-hand fitment stock.
- AC-in and AC-out may share the purchased single `6-way` enclosure only if neutral paths remain isolated, PE/equipment grounding is continuous, no fixed downstream neutral-ground bond is added, and labeling/barriers/strain relief are verified during install. AC-out branch validation is still pending.
- Before sustained charging, program/verify the MultiPlus LiFePO4 charge profile via `MK3-USB + VEConfigure` or equivalent: absorption/float per Dumfume manual, equalization off, lithium temperature-compensation behavior confirmed, charger current conservative, and `DVCC` left disabled unless a documented BMS/GX control path is later added.
- Defer Mechman alternator installation until shore charging/monitoring are fully programmed/proven and alternator vendor/support gates are closed.
- **Flooring gate:** do not glue Lonseal or permanently close the floor until EPS/subfloor fit, moisture path, hardpoint, and penetration/service-access checks pass in the installed camper.
- **Payload gate:** capture door-sticker payload and staged scale weights. Treat total payload, rear axle load, rear tire load, and left/right balance as active constraints.

## Post-install build restart sequence
Purpose: turn the installed camper shell into measured block envelopes before buying hard-to-return interior structure.

1. **Shakedown / inspect**
   - Stay local enough to address early Hiatus issues if practical.
   - Check barn doors, cap seals, bed rail caps, windows/fan, dust paths, rattles, and water paths.
2. **Measure / map**
   - Capture interior dimensions, hardpoints, bed rail interface, floor clearances, door swing, window/fan locations, and candidate pass-through zones.
   - Mark no-drill/no-load zones and likely service chases.
3. **Floor closeout**
   - Visually inspect sealed bed paths after cure and normal travel/shakedown; look for lifted tape, cracked beads, dust trails, or dampness.
   - Trim EPS flat in ribs, verify plywood flushness, and keep hardpoint pockets non-compressible.
   - Glue Lonseal only after the gate passes.
4. **Block envelopes before extrusion**
   - Tape/cardboard the passenger-side lofted fridge/wet-spine skeleton, purchased `36 gal` wheel-well tank, under-fridge pump/accumulator board, separated battery bench, driver-side electrical closet/DC shelf, diesel heater base zone, and desk.
   - Use the interior furniture/galley concept doc as the layout checkpoint, then verify against real roof-down sweep, cabover/bench cushion use, fridge lid/vent/cord envelope, tank overlap/fitting orientation, pump service access, battery extraction, and wet/dry separation.
   - Default to `10-series` 80/20, plywood, panels, brackets, and light rail unless measured heavy/dynamic modules prove they need larger extrusion.
5. **Electrical bench path**
   - Continue from the completed first live checkpoint: verify torque/witness marks, covers, labeling, SmartShunt/Cerbo power-source behavior, and shutdown/de-energization behavior.
   - Program the MultiPlus battery charge profile before sustained charging, then repeat shore-charge validation with logged voltage/current/SOC/temperature.
   - Keep AC-out branch/GFCI validation and alternator commissioning as separate later gates.

### Cabinetry approach (recommended)
- Treat 80/20 as the *structure* and simple panels as the *skins*.
- Prioritize serviceability over concealment: every fuse/disconnect should be reachable without uninstalling major devices.
- Build “functional first”: once the electrical module works and survives vibration, add frosted panels + LED backlighting as a Phase 2 overlay.
