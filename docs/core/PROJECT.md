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
- **Washington/install mode is now the priority.** Keep the truck bed mostly empty; leave the `3x 48V` batteries, electrical cabinet parts, and loose build materials home unless Hiatus specifically needs them.
- **Truck bed dust/weather closeout:** bed rail caps have been re-bonded with Loctite polyurethane, small drill holes were sealed with Gorilla Patch & Seal tape, and visible corner air gaps received polyurethane beads. Next gate is cure/inspection and later ordinary post-drive inspection after camper install.
- **Flooring gate:** trim EPS and verify three-piece plywood fit/serviceability after the trip. Do not glue Lonseal until rail/bed-floor/corner sealing is cured and inspected, post-install floor penetrations are ruled out, and the roller/rolling method is confirmed. The exact trowel is now purchased.
- **Install-day data capture:** photograph attachment points, bed rail/cap interface, barn-door seals, clearances, hardpoints, passthrough candidates, and all dimensions before leaving Hiatus.
- **Extrusion/furniture:** watch design videos and collect ideas during/after the trip, but do not place exact-cut aluminum extrusion orders until real camper/fridge/tank/electrical block envelopes are measured. Targeted stock/hardware orders are acceptable after the post-install measurement pass.
- **Electrical:** shore-power / initial-charge remains the post-trip priority before any alternator work. Build the AC-in-only MultiPlus charge path first: `shore source -> cord/adapter -> TT-30 inlet -> hardwired EMS -> AC-in breaker/disconnect -> MultiPlus AC-in`. Order/SKU-lock BOM rows `107`, `108`, `123`, `13`, `109`, `14`, and `114` plus glands/grommets/labels/ferrules.
- Keep AC-in and AC-out protection in separate enclosures. Do not let final AC receptacle-count churn block the AC-in charge path.
- Before first charge, reconcile the MultiPlus LiFePO4 charge profile (`56.8V` planning basis vs `58.4V` battery/manual basis), set source current limits, and charge/test one `48V` battery at a time before paralleling.
- Defer Mechman alternator installation until batteries are present, shore charging/monitoring are proven, and alternator vendor/support gates are closed.

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
   - Tape/cardboard the fridge, purchased `36 gal` wheel-well tank, electrical cabinet, galley, and desk zones.
   - Decide which modules truly need `15-series`, which can use `10-series`, and which should mount with simpler brackets/plywood.
5. **Electrical bench path**
   - Layout Board A/B with real service access and cable corridors.
   - SKU-lock AC-in charging hardware, write first-charge checklist, then charge/test one battery at a time.

### Cabinetry approach (recommended)
- Treat 80/20 as the *structure* and simple panels as the *skins*.
- Prioritize serviceability over concealment: every fuse/disconnect should be reachable without uninstalling major devices.
- Build “functional first”: once the electrical module works and survives vibration, add frosted panels + LED backlighting as a Phase 2 overlay.
