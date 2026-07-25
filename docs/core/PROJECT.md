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
- As-of date: 2026-07-19
- Phase: hard-mounted electrical integration, bank/shore/12V commissioning, then wet-spine installation
- Install milestone: May 7, 2026 Hiatus install is historical context; the real camper shell and integrated module fit now control physical decisions
- Mission: build a reliable off-grid camper workspace suitable for full-time professional use

## Fixed constraints
- Truck platform is fixed: 2021 F-350 Regular Cab Long Bed with an aluminum pickup box/body attachment environment
- Existing truck modifications are fixed: 2.5" lift, 37" tires, 4.88 regear
- Camper platform is fixed: installed/in-hand Hiatus shell on the F-350 long bed

## Objectives

- Support standard workdays without power anxiety
- Maintain reliable internet for meetings and high-value workflow tasks
- Provide ergonomic, repeatable workstation setup
- Keep system serviceable and safe in multi-climate travel use

## Current execution focus (electrical closeout into wet-spine integration)
- Use [PROJECT_build_order_of_operations](../plans/PROJECT_build_order_of_operations.md) for active sequence and [LIVE_BUILD_CHECKLIST](../plans/LIVE_BUILD_CHECKLIST.md) for shop actions. Earlier install-window plans are historical references unless explicitly refreshed.
- The one-piece Lonseal remains the permanent finish over the three-piece `3/4 in` plywood floor. Controlled module loading has begun, and the electrical module is now hard-mounted through the floor to registered truck-bed hardpoints.
- The module fits cleanly and is stable enough for continued stationary work. Final road restraint still requires the planned tie-in to the Bench/adjacent framing so the electrical frame cannot rack.
- The MultiPlus and combined AC breaker enclosure were removed before lifting to reduce module weight. Their mounting pattern is preserved by embedded pronged/spiked T-nuts in the plywood backer, so both can be remounted from the service face without loose rear nuts.
- All three `48V` batteries' `2/0 AWG` positive/negative branch cables are cut, lugged, heat-shrunk, and landed at the battery-side busbars. Keep the batteries isolated until Batteries 2 and 3 are charged individually, allowed to rest, and confirmed within `0.1V` before the three-way parallel connection.
- Immediate electrical sequence is MultiPlus/AC-enclosure remount -> complete/protect the `10/3` shore-inlet route -> individually charge/equalize the batteries -> parallel and commission the `15.36 kWh` bank -> complete the `12V` buffer branch and Orion fuse cleanup -> prove factory lights, Maxxair fan, and selected DC outlets.
- Treat the water tank as a two-stage job: workbench measurement/mockup followed by one bare-tank in-truck dry fit before any new sender/fill/vent hole is cut. Lock tank restraint and wet-spine service access before the passenger-side frame closes around it.
- Shore and water-fill penetrations stay downstream of their installed inside endpoints. Prove the complete inside route, bend radius/fall, backing, service access, and strain relief before cutting the shell/bed-side interface.
- Use registered bed rivnuts rather than plywood alone for modules needing positive retention. Electrical, battery, and full-tank loads must remain visibly restrained and serviceable.
- Electrical system status remains live-proven at the system level, but permanent shore AC-in, AC-out/GFCI, full-bank commissioning, road restraint, and alternator first-charge remain separate gates. Factory pod lighting, Maxxair fan, and initial DC outlets move into the immediate `12V` proof pass; solar, permanent hot water, propane closeout, and audio remain later workstreams.
- Black-walnut Galley/Desk/Bench finish surfaces remain template-gated after final floor height and module geometry are proven.

## Scope
- In scope: electrical, charging, solar, communications, interior structure/cabinetry, operations process, maintenance tracking
- Out of scope for phase 1: non-critical aesthetic upgrades and major unrelated truck mechanical projects

## Requirements baseline (draft)
- Workday autonomy target: load model v5 profiles indicate `3,915 Wh/day` (`core_workday`), `4,829 Wh/day` (`winter_workday`), and `624 Wh/day` (`minimal_idle_day`), including conservative future-audio allowance; actual near-term office-only use may be lower. Battery reserve floor policy is `20%` minimum SOC
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
- M6: electrical module first-live checkpoint and truck-bed hard-mount complete; shore inlet, bank/`12V` commissioning, Bench tie-in, and strain-relief closeout underway
- M7: shakedown and punch-list closure

## Build sequencing baseline (as-of 2026-07-19)
- The floor-removal branch is closed and the electrical-module hard-mount gate has passed. Build sequencing now keeps the battery bay and backer service face open while the heavy electrical equipment, shore route, battery bank, and `12V` junction are closed out.
- Canonical sequence: remount MultiPlus/AC enclosure -> prove and install shore inlet/AC-in path -> equalize and parallel the `3x 48V` bank -> finish Orion/`12V` branch and prove lights/fan/DC outlets -> bench/driveway assemble and test tank/pump/wet spine -> hard-mount tank/plumbing/Galley -> add Bench tie-in and remaining modules/panels -> shakedown.
- Detailed owner docs:
  - [PROJECT_build_order_of_operations](../plans/PROJECT_build_order_of_operations.md)
  - [FLOORING_subfloor_build_process](../implementation/FLOORING_subfloor_build_process.md)
  - [LIVE_BUILD_CHECKLIST](../plans/LIVE_BUILD_CHECKLIST.md)

## Immediate next decisions
- **Electrical backer remount:** reinstall the MultiPlus and AC breaker enclosure into the embedded T-nuts, then confirm backer thread engagement, service clearance, cable support, and anti-rack tie-in geometry before energizing.
- **Orion/fuse identity:** use one final standalone `F-06 20A/80V` FKS/ATO fuse/holder on the Orion `48V` input positive lead. The purchased `166.7000.5202` fuse is correct, but purchased `178.6150.0001` is housing-only; use complete looped-wire holder `178.6152.2501` and proper `6 AWG -> 14-16 AWG` reducer splices, or another fully validated complete `20A/80VDC` holder assembly. Identify the physically X-marked Lynx fuse by slot rather than assuming it belongs to Orion: Slot 2 requires `F-03 60A/80V` for the MPPT; Slot 4 remains empty. Retain `F-07 60A/80V` MEGA only on Orion `12V` output and `F-11 100A` ANL only on the `12V` battery positive branch.
- **Tank port map:** owner confirms four molded ports on each end—two visibly large and two smaller—with no obvious/open top port. Measure/identify the threads and inspect for a membrane-covered top boss. Current default is upper large end port for gravity fill, highest suitable upper small end port for unrestricted vent/overflow, low north-end suction to the pump, and a separate low tank drain; freeze the assignment only after installed-orientation dry fit.
- **Electrical/battery order:** remount AC equipment and install shore AC-in first; charge Batteries 2 and 3 individually; record rested voltages; parallel only at `<=0.1V` difference; then verify polarity, branch protection, SmartShunt, disconnect, and current sharing before Bench closure.
- **Penetrations:** the hard-mounted electrical endpoint now exists, so the shore inlet may proceed after the exact inside/outside route, hidden-structure clearance, backer grommet/strain relief, and sealing surfaces are proven together. Water-fill/vent still waits for tank orientation, fitting method, continuous hose fall/vent rise, and service access.
- **Restraint:** use registered rivnuts for positively retained modules and confirm the battery bench, electrical module, and full water tank are not loose or dependent on plywood alone.
- **Payload:** capture door-sticker payload and staged scale weights. Treat total payload, rear axle load, rear tire load, and left/right balance as active constraints.

## Electrical-to-shakedown sequence
Purpose: finish the hard-mounted utilities and close furniture around tested systems without rebuilding access twice.

1. **Electrical backer and shore AC-in**
   - Remount the MultiPlus and combined AC breaker enclosure into the embedded T-nuts; prove the complete inside/outside shore path, then cut, bed, seal, grommet, strain-relieve, and test the L5-30/`10/3` AC-in route.
2. **Open-access battery-bank commissioning**
   - Charge Batteries 2 and 3 individually, rest and record all three voltages, parallel only within `0.1V`, then verify branch protection, polarity, disconnect, Lynx/shunt, cable support, covers, extraction, and current sharing with the Bench open.
3. **`12V` commissioning**
   - Install final Orion `F-06`, complete the `12V` buffer branch, verify `F-07`/`F-11`, then prove factory lights, Maxxair fan, pump branch, and selected DC charging outlets.
4. **Tank, restraint, and wet-spine test/install**
   - Add the approved sender/fittings, bench/driveway fill-pressure-leak-function test the tank/pump assembly, then hard-mount its restraint and removable pump/strainer/accumulator/manifold board with wet/dry separation and low-point service access.
5. **Remaining penetrations, modules, and shakedown**
   - Prove/cut the gravity-fill/vent opening only from installed geometry; add Galley/Bench/Desk/fridge modules and the electrical anti-rack tie-in, keep panels removable until tests pass, then torque/witness-mark, drive locally, and inspect for floor damage, leaks, insert spin, abrasion, module movement, and fastener loss.

### Cabinetry approach (recommended)
- Treat 80/20 as the *structure* and simple panels as the *skins*.
- Prioritize serviceability over concealment: every fuse/disconnect should be reachable without uninstalling major devices.
- Build “functional first”: once the electrical module works and survives vibration, add frosted panels + LED backlighting as a Phase 2 overlay.
