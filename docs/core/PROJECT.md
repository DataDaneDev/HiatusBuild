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
- As-of date: 2026-06-27
- Phase: post-install module integration buildout: electrical tower, bench/desk structure, and galley/wet-spine skeleton
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
- Use [INTERIOR_furniture_layout_and_galley](../implementation/INTERIOR_furniture_layout_and_galley.md) as the current owner for the office-first passenger-side lofted fridge/wet-spine concept, separated battery bench, galley counter/appliance bay, and `10-series` 80/20 overlay-panel direction.
- Use [ELECTRICAL_48V_ARCHITECTURE](ELECTRICAL_48V_ARCHITECTURE.md) as the canonical `48V` design reference while integrating the electrical module with the bench/desk structure and preserving alternator-control/service paths.
- Current physical state: the electrical backer has been trimmed to inset cleanly into the `80/20` frame; component locations were adjusted for real MultiPlus depth without changing the core electrical architecture; the electrical module is now freestanding and ready to tie into the bench/desk structure.
- Travel rule: do **not** drive with the freestanding electrical module by itself. It is intentionally not treated as road-ready until it is tied into the bench/desk/galley structure, hard-mounted to truck/camper hardpoints as applicable, and has panels/diagonal restraint/anti-rattle retention installed.
- Active work now shifts from isolated electrical-module fabrication to integrated `80/20` module buildout: bench first, desk desktop/workstation support, then galley/wet-spine counter with sink/faucet, induction position, and Ninja SP151 air-fryer cubby. Camper audio remains preliminary/future-roadmap, not near-term procurement.
- Electrical status remains live-proven at the system level: the `48V` bus, SmartShunt, Orion, Cerbo, MultiPlus inverter mode, and a short limited-current shore-charge test have all been proven without observed errors; remaining closeout is mechanical restraint, covers/panels, strain relief, labels, and access checks.
- Defer irreversible work (final shell penetrations, shell-dependent final cable cuts, permanent skins, and finish-floor glue-down) until physical module fit, service-map, access, and post-drive/shakedown checks pass.

## Scope
- In scope: electrical, charging, solar, communications, interior structure/cabinetry, operations process, maintenance tracking
- Out of scope for phase 1: non-critical aesthetic upgrades and major unrelated truck mechanical projects

## Requirements baseline (draft)
- Workday autonomy target: conservative modeled profiles (BOM loads + owner-supplied office loads + preliminary future-audio allowance) indicate `3,794 Wh/day` (`core_workday`) and `4,587 Wh/day` (`winter_workday`); actual near-term office-only use may be lower. Battery reserve floor policy is `20%` minimum SOC
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
- M6: electrical module first-live checkpoint complete; hard-mounting, procurement, charger programming, and strain-relief closeout underway
- M7: shakedown and punch-list closure

## Build sequencing baseline (as-of 2026-06-27)
- Build sequencing is tracked as an overlapping phase plan (not strict serial trades).
- May 7 install readiness is historical context; current sequencing focus is integrated module buildout: tie the trimmed/inset electrical module into the bench/desk structure, then build the galley/wet-spine counter/appliance module around the purchased sink/faucet, induction cooktop, and Ninja SP151 cubby.
- CAD and AI-generated diagrams are planning references only; real camper measurements, physical mockups, and the current module workbook own final dimensions.
- Detailed stage-by-stage order of operations, dependencies, and draft date windows:
- [PROJECT_build_order_of_operations](../plans/PROJECT_build_order_of_operations.md)

## Immediate next decisions
- **Electrical module integration:** keep the electrical tower out of driving service until it is tied into the bench/desk frame, panel/diagonal restraint is added, and the final truck/camper hardpoint plan is proven. The current freestanding state is a shop-fit milestone, not a road-ready state.
- **Bench first:** build the battery/bench/step structure that physically braces the electrical module and preserves battery extraction, disconnect/fuse access, and cushion/step loads.
- **Desk next:** fit the desktop/workstation support against the electrical/bench structure before final galley skins so seated geometry, roof-down sweep, DC/AC access, and entry movement stay honest.
- **Galley third:** build the passenger-side galley/wet-spine counter around the purchased Sarlai topmount sink, FORIOUS faucet, Duxtop induction cooktop, and Ninja SP151 air-fryer/toaster-oven cubby; validate cutout, faucet hose/nut clearance, drain/graywater path, and appliance heat/retention before final panels.
- **Extrusion/furniture:** continue using available `10-series`/`2010` stock, regular angle, and on-hand Chinese connector hardware as prototype/build stock; reserve the pending nut/hardware shipment for final tightening and serviceable seams. Avoid exact-final skins until all modules fit together in the truck.
- **Panel strategy:** use overlay/removable panels on living-facing surfaces, keep service zones exposed or quick-removable, and use magnets only for light service covers with locator/backup retention where panel loss matters.
- **Electrical:** current live-commissioning checkpoint is complete; the new mechanical priority is tie-in, anti-rack restraint, covers, labels, service loops, and post-drive retorque/witness-mark checks. AC-out/GFCI and alternator commissioning remain later separate gates.
- **Flooring gate:** do not glue Lonseal or permanently close the floor until EPS/subfloor fit, moisture path, hardpoint, and penetration/service-access checks pass in the installed camper.
- **Payload gate:** capture door-sticker payload and staged scale weights. Treat total payload, rear axle load, rear tire load, and left/right balance as active constraints.

## Post-install build restart sequence
Purpose: turn the installed camper shell and shop-built modules into a restrained, serviceable MVP structure before travel use.

1. **Electrical module tie-in / no-drive gate**
   - The trimmed/inset electrical backer and freestanding `80/20` electrical module are a successful shop-fit milestone.
   - Do not drive with the freestanding module loose or only lightly bolted; brace it into the bench/desk structure and verify anti-rack panels/diagonals, hardpoints, strain relief, and fastener witness marks first.
2. **Bench/step structure**
   - Build the bench/battery/step structure that braces the electrical module and keeps battery extraction, disconnects, fuses, and service panels reachable.
   - Validate lid/cushion/step loads and cabover entry before skins.
3. **Desk/workstation support**
   - Fit the desktop and driver-side workstation support to the electrical/bench structure.
   - Validate seated work geometry, roof-down sweep, entry clearance, DC/AC/USB access, monitor stow/latch path, and cable loops before permanent panels.
4. **Galley/wet-spine counter module**
   - Build the galley counter/wet-spine skeleton around the purchased sink/faucet, Duxtop induction cooktop, and Ninja SP151 appliance bay.
   - Validate sink cutout, faucet under-counter clearance, drain/graywater cassette, pump/strainer/manifold service, leak tray, induction stow/use position, air-fryer heat clearance, and travel restraint.
5. **Truck fit and shakedown**
   - Fit the integrated modules in the truck as a system, then add panels/covers/latches only after service access still works.
   - Do a local low-consequence drive/shakedown for rattles, movement, fastener loosening, leaks, high-draw load sequencing, and emergency electrical access before longer travel.

### Cabinetry approach (recommended)
- Treat 80/20 as the *structure* and simple panels as the *skins*.
- Prioritize serviceability over concealment: every fuse/disconnect should be reachable without uninstalling major devices.
- Build “functional first”: once the electrical module works and survives vibration, add frosted panels + LED backlighting as a Phase 2 overlay.
