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
- As-of date: 2026-07-16
- Phase: permanent-floor cure and utilities-first restrained reinstall
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

## Current execution focus (floor cure and systems integration)
- Use [PROJECT_build_order_of_operations](../plans/PROJECT_build_order_of_operations.md) for active sequence and [LIVE_BUILD_CHECKLIST](../plans/LIVE_BUILD_CHECKLIST.md) for shop actions. Earlier install-window plans are historical references unless explicitly refreshed.
- Owner reported that the one-piece Lonseal was glued to the three-piece `3/4 in` plywood floor on the evening of `2026-07-15`. The floor is now intentionally permanent: removing the three plywood sections would require cutting the vinyl along both plywood seams.
- Hold heavy modules through the published `72 hr` cure window measured from actual adhesive completion. Because the exact finish time was not recorded, use the evening of `2026-07-18` only as the earliest planning estimate, not an automatic release.
- Owner reports mild waviness/bumps and some edge lift. Edge boards are bolted down for cure pressure, and temporary bolts were run through adhesive-contaminated hardpoint holes to preserve thread paths. Back those bolts out/clean them carefully during cure, then make any floor-repair decision only after the boards come off and the full cure inspection is complete.
- Use the empty-truck cure window for non-loading work: tank port inventory, sender/fill/vent/outlet/drain planning, plumbing-board layout, wire/hose inventory, labels, and bench preparation.
- After cure, hard-mount the electrical module first. Install/wire/fuse the `3x 48V` bank while the battery bay is open, prove extraction and emergency access, then add the bench bridge/lid and remaining modules.
- Treat the water tank as a two-stage job: workbench measurement/mockup followed by one bare-tank in-truck dry fit before any new sender/fill/vent hole is cut. Lock tank restraint and wet-spine service access before the passenger-side frame closes around it.
- Shore and water-fill penetrations stay downstream of their installed inside endpoints. Prove the complete inside route, bend radius/fall, backing, service access, and strain relief before cutting the shell/bed-side interface.
- Use registered bed rivnuts rather than plywood alone for modules needing positive retention. Electrical, battery, and full-tank loads must remain visibly restrained and serviceable.
- Electrical system status remains live-proven at the system level, but AC-out/GFCI, final bank install, road restraint, and alternator first-charge remain separate gates. Solar, hot water, propane, lighting, and audio remain later workstreams.
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
- M6: electrical module first-live checkpoint complete; hard-mounting, procurement, charger programming, and strain-relief closeout underway
- M7: shakedown and punch-list closure

## Build sequencing baseline (as-of 2026-07-16)
- The floor-removal branch is closed. Build sequencing now protects the installed Lonseal, preserves open access to heavy systems, and delays furniture closure until electrical/plumbing endpoints are installed and tested.
- Canonical sequence: floor cure/bolt cleanup/post-cure inspection -> tank workbench port map -> hard-mount electrical module -> install and close out the `3x 48V` bank with the bench open -> bare-tank in-truck dry fit and port freeze -> tank/restraint/wet-spine install -> shore and water-fill penetrations -> final electrical/plumbing routes and tests -> remaining modules/panels -> shakedown.
- Detailed owner docs:
  - [PROJECT_build_order_of_operations](../plans/PROJECT_build_order_of_operations.md)
  - [FLOORING_subfloor_build_process](../implementation/FLOORING_subfloor_build_process.md)
  - [LIVE_BUILD_CHECKLIST](../plans/LIVE_BUILD_CHECKLIST.md)

## Immediate next decisions
- **Cure/thread preservation:** identify the actual adhesive completion time if possible; keep heavy modules off for `72 hr`; back temporary clamp bolts out one at a time with hand/low-speed control, clean them, and avoid spinning/galling a stainless insert.
- **Post-cure floor disposition:** remove edge boards after the heavy-furniture cure gate, inspect edge adhesion, hollow/raised areas, bolt-hole condition, and board/washer imprinting, then accept stable cosmetic waviness or define a localized repair without reopening the whole floor.
- **Tank port map:** inventory every molded tank fitting and physically assign fill, vent, pump outlet, drain, sender, and unused/service ports. Do not assume gravity fill must enter through an arbitrary top hole; choose a manufacturer-compatible high-side/top fitting that supports continuous downhill fill-hose routing and a separate highest-point vent.
- **Electrical/battery order:** electrical module first, `3x 48V` batteries and their fuse/disconnect/parallel wiring second, bench closure third. Prove extraction and emergency service before adding the upper bench structure.
- **Penetrations:** shore inlet waits for the hard-mounted electrical path; water-fill/vent opening waits for tank orientation, fitting method, continuous hose fall/vent rise, and service access.
- **Restraint:** use registered rivnuts for positively retained modules and confirm the battery bench, electrical module, and full water tank are not loose or dependent on plywood alone.
- **Payload:** capture door-sticker payload and staged scale weights. Treat total payload, rear axle load, rear tire load, and left/right balance as active constraints.

## Cure-to-shakedown sequence
Purpose: turn the permanent floor into a serviceable installed electrical/water/furniture system without rebuilding access twice.

1. **Cure and floor inspection**
   - Preserve/clean hardpoint threads, keep heavy modules off for `72 hr`, remove cure boards, and record the accepted floor condition before loading it.
2. **Tank workbench map plus bare dry fit**
   - Measure the empty tank and KUS sender, inventory molded ports, mock fill/vent/outlet/drain/service-board routing on the garage floor, then place the bare tank in the truck once to verify wheel-well, extrusion, hose, sender-service, and restraint clearances before cutting.
3. **Electrical module and open battery-bank install**
   - Protect the floor, hard-mount/brace the electrical module, install and individually fuse/connect the `3x 48V` bank with the bench open, then verify disconnect, Class T, Lynx/shunt, covers, cable support, polarity, extraction, and service access.
4. **Tank, restraint, and wet-spine install**
   - Add the approved sender/fittings, bench leak-test the tank before installation, hard-mount its restraint, and install the removable pump/strainer/accumulator/manifold board with wet/dry separation and low-point service access.
5. **Exterior penetrations and rough-in**
   - With inside endpoints physically installed, prove and then cut the shore inlet plus gravity-fill/vent openings; seal, support, route, and test AC-in, cold-water, fill/vent, drain/graywater, and capped future-hot paths.
6. **Remaining modules, closeout, and shakedown**
   - Add the bench bridge and remaining Galley/Desk/fridge modules, keeping panels removable until electrical/plumbing tests pass; then torque/witness-mark, drive locally, and inspect for floor damage, leaks, insert spin, abrasion, module movement, and fastener loss.

### Cabinetry approach (recommended)
- Treat 80/20 as the *structure* and simple panels as the *skins*.
- Prioritize serviceability over concealment: every fuse/disconnect should be reachable without uninstalling major devices.
- Build “functional first”: once the electrical module works and survives vibration, add frosted panels + LED backlighting as a Phase 2 overlay.
