# Project

## Snapshot
- As-of date: February 11, 2026
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

## Build sequencing baseline (as-of 2026-02-15)
- Build sequencing is now tracked as an overlapping phase plan (not strict serial trades).
- Target install date remains fixed at May 7, 2026 (`81` days from this baseline date).
- Detailed stage-by-stage order of operations, dependencies, and draft date windows:
- `docs/PROJECT_build_order_of_operations.md`

## Immediate next decisions
- Build a full fuse schedule for the locked Lynx architecture (main protection, all branch fuses, vehicle-side protection where applicable)
- Freeze autonomy policy using modeled profiles (BOM + owner-supplied office loads) with a `20%` minimum SOC reserve floor
- Confirm passthrough locations (solar, shore, fuel/heater routing) with Hiatus before production lock
- Validate Sterling `BB1248120` + `BBR` current-limit operating envelope on the factory `240A` alternator; keep Mechman 370A alternator + Big 3 as purchase-later path pending fitment confirmation and install timing
- Choose final solar panel type (flex vs rigid)
