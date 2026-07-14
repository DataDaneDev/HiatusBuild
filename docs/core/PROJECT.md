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
- As-of date: 2026-07-13
- Phase: flooring foundation — installed-hardpoint verification, Lonseal template/dry fit, adhesive install, and restrained module reinstall
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

## Current execution focus (flooring foundation)
- Use [PROJECT_build_order_of_operations](../plans/PROJECT_build_order_of_operations.md) for active sequence and [LIVE_BUILD_CHECKLIST](../plans/LIVE_BUILD_CHECKLIST.md) for shop actions. Earlier install-window plans are historical references unless explicitly refreshed.
- Major Galley/Bench/Electrical/Desk modules have been reinforced/test-fit well enough to preserve real feet, seams, access, and integrated geometry through one controlled teardown.
- Finish only the remaining Desk/storage corrections needed to trust tab locations, then isolate electrical/remove loose batteries and record hardpoint centers from physical modules. Do not drill bed metal around connected/live equipment.
- Truck-bed stainless rivnuts are installed across rib highs, valleys, and some rib-edge transitions. Finish sealing, hand-test/map the active inserts, and relocate or retire any angled location that cannot accept a square load path before the floor closes.
- The three-piece `3/4 in` plywood floor is height-locked and final. Do not add underlayment; instead correct real rocking, high joints, loose edges, or visibly moving seams before glue.
- Gorilla tape is a practical dust/splash barrier where it is adhering well to the bed liner. Keep threads and rivnut bearing surfaces clear; inspect known edges after the first dusty/wet drive and rework actual failures.
- Use registered bed rivnuts rather than plywood alone for modules needing positive retention. Keep the heavier battery/water/electrical assemblies visibly restrained and serviceable; solve observed movement with practical distributed tabs/tie-ins rather than speculative hardware redesign.
- Electrical system status remains live-proven at the system level, but final wiring/full battery/plumbing work stays downstream of floor cure and restrained module reinstall. Alternator first-charge, AC-out/GFCI, solar, hot water, propane, lighting, and audio remain separate later gates.
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

## Build sequencing baseline (as-of 2026-07-10)
- Build sequencing remains overlapping, but the floor is now a hard dependency because final electrical/plumbing routing and module installation should not precede another teardown.
- Use physical module feet/access and the current cutlist workbook, not stale CAD, to freeze the hardpoint map.
- Canonical sequence: transfer real module geometry -> finish bed sealing -> set/test/register stainless rivnuts -> settle EPS/existing `3/4 in` substrate -> full module refit -> Lonseal dry fit/install/cure -> restrained reinstall -> final electrical/plumbing routes -> shakedown.
- Detailed owner docs:
  - [PROJECT_build_order_of_operations](../plans/PROJECT_build_order_of_operations.md)
  - [FLOORING_subfloor_build_process](../implementation/FLOORING_subfloor_build_process.md)
  - [LIVE_BUILD_CHECKLIST](../plans/LIVE_BUILD_CHECKLIST.md)

## Immediate next decisions
- **Hardpoint installation:** finish sealing, set each stainless rivnut, confirm firm collapse/no spin, bolt-test the threads, and record the completed location map.
- **Substrate:** retain the locked `3/4 in` floor height; dry-fit the existing panels and resolve real rocking, high joints, loose edges, or moving seams.
- **Sealing:** use the planned second Gorilla roll where its bedliner adhesion addresses a known splash/dust path; inspect the result rather than building a formal test program.
- **Restraint:** use the registered rivnuts for positively retained modules and confirm the battery bench, electrical module, and water tank are not loose or dependent on plywood alone.
- **Perimeter:** decide flat-trim vs flash-cove before cutting Lonseal; vertical/coved surfaces are not a #650-only installation.
- **Payload:** capture door-sticker payload and staged scale weights. Treat total payload, rear axle load, rear tire load, and left/right balance as active constraints.

## Foundation-to-shakedown sequence
Purpose: turn the proven module geometry into a stable, dry, serviceable final foundation before travel use.

1. **Geometry capture / de-energize**
   - Finish required Desk/storage corrections; isolate electrical/remove loose batteries; photograph/label modules and transfer real foot/tab centers from two bed datums.
2. **Finish bed sealing and verify hardpoints**
   - Complete the practical tape/seal pass, hand-test/map the installed stainless rivnuts, and relocate or retire any angled location that cannot accept a square load path before it is covered.
3. **Substrate and hardpoint dry build**
   - Settle EPS/base plywood, correct only real rocking/high-joint problems, and refit modules with locator bolts plus verified service access.
4. **Lonseal dry fit / locator proof**
   - Preserve the hole-recovery map and refit modules with temporary locator bolts before adhesive work.
5. **Lonseal and cure**
   - Dry-fit/cut after the perimeter decision, install with the complete #650 process, and keep foot traffic/heavy modules off through the published cure windows.
6. **Restrained reinstall and shakedown**
   - Reinstall/protect/torque/witness-mark, finish post-floor electrical/plumbing routing, then run a low-consequence shakedown and inspect for moisture, insert spin, settlement, abrasion, movement, and fastener loss.

### Cabinetry approach (recommended)
- Treat 80/20 as the *structure* and simple panels as the *skins*.
- Prioritize serviceability over concealment: every fuse/disconnect should be reachable without uninstalling major devices.
- Build “functional first”: once the electrical module works and survives vibration, add frosted panels + LED backlighting as a Phase 2 overlay.
