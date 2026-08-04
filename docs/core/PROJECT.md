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
- As-of date: 2026-07-26
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
- The one-piece Lonseal remains the permanent finish over the three-piece `3/4 in` plywood floor. The electrical module, Galley/cooler support, water tank, and the returned Bench extrusion bridge are owner-reported hard-mounted; the integrated structure is extremely stiff.
- Remaining road restraint is specific rather than architectural: positively capture and strap the `3x 48V` batteries and separate `12V` battery, restrain the ICECO at its foot-level tie points with a lateral hard stop, and finish terminal/cable protection.
- All three `48V` batteries' `2/0 AWG` positive/negative branch cables are complete and landed. Battery 1 completed the corrected isolated charge cycle, Battery 2 remained in normal upper-`54V` bulk at the overnight `2026-08-02/03` checkpoint, and Battery 3 remains pending. Rest/record all three and parallel only at `<=0.1V` maximum-to-minimum spread.
- The Orion charges the `12V` buffer battery and the camper `12V` system operates correctly. The driver-rear shore inlet/cable route is installed; the enclosed `L/N/PE` splice and dead checks remain open before permanent-path use.
- The `36 gal` wheel-well tank is hard-mounted with two metal straps into truck-bed-wall plusnuts, and all three passenger-rear pass-throughs are installed. The KUS under-ring/gasket/hardware repair, fill/vent, sink/faucet termination, and dry pressure/dwell test remain the water-service gates.
- Immediate interior sequence is battery/cooler restraint -> plywood Galley counter and sink/faucet -> Galley/Desk wire pulls while access is open -> Desk/storage reinstall -> KUS/water acceptance as parts arrive.
- Starlink routing should first exploit the existing front truck-bed opening, with one protected moving section on the sheltered front face of the popup. Do not slide cable through a roof gland; prototype a fixed-end service loop or full-eight-conductor shielded industrial Ethernet coil through full roof cycles before locking holes or exposed connectors.
- Electrical system status remains live-proven at the system level, but permanent shore AC-in, AC-out/GFCI, full-bank commissioning, final road restraint, and alternator first-charge remain separate gates. Hot water remains the propane-only HOTTAP V2 rear-box package; solar and audio remain later workstreams.
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
- Solar and diesel-heater routing decisions remain pending and tracked in `docs/core/TRACKING.md`; shore hardware is selected, with inlet/cable-support details handled during physical install. The HOTTAP LP path stays within the cylinder box/outdoor heater package—no propane passthrough into the camper. The separate direct BLUE/RED camper water ports are installed; rear-box heater/cylinder integration and operating-clearance proof remain open.

## Milestone plan (draft)
- M0: requirements baseline frozen
- M1: system architecture selected (electrical + comms + thermal)
- M2: BOM v1 complete and procurement started
- M3: camper installed / physical shell available for real measurements
- M4: subsystem bench validation complete
- M5: measured interior block envelopes and service map complete
- M6: electrical/Bench/Galley/tank hard-mount and `12V` checkpoints complete; battery matching/restraint, shore splice, wet-side acceptance, and Galley wiring closeout underway
- M7: shakedown and punch-list closure

## Build sequencing baseline (as-of 2026-08-03)
- The permanent floor and integrated electrical/Bench/Galley/tank hard-mount gates have passed. Keep the battery bay, Galley counter underside, KUS opening, and hidden Desk/storage wire routes open while the remaining restraint, charging, plumbing, and wiring gates close.
- Canonical sequence: insulate/temporarily mount the live ICECO switch -> terminate/configure KUS -> wire/test pump -> pull every access-dependent Galley/Desk AC/DC/control branch -> build individual battery/cooler restraint -> finish Battery 3 charge/rest and match -> parallel and commission the `3x 48V` bank -> finish KUS/fill/vent/sink water acceptance -> reinstall Desk/storage -> mid-September `2026` final-walnut installation -> shore/AC-out and alternator closeout -> shakedown. Full temporary tops are dropped.
- Detailed owner docs:
  - [PROJECT_build_order_of_operations](../plans/PROJECT_build_order_of_operations.md)
  - [FLOORING_subfloor_build_process](../implementation/FLOORING_subfloor_build_process.md)
  - [LIVE_BUILD_CHECKLIST](../plans/LIVE_BUILD_CHECKLIST.md)

## Immediate next decisions
- **Battery/cooler restraint:** build low battery perimeter/divider capture tied into anchored extrusion or through-bolted structural plywood with backing, then strap each battery individually without crossing terminals/displays. Use the ICECO foot-level tie points with a low-stretch cam strap plus an aisle-side hard stop and soft wall bumper.
- **Immediate electrical endpoints:** individually insulate and temporarily hard-mount the ICECO switch, terminate/configure KUS, wire/test the `14 AWG / 10A` pump branch, then pull every access-dependent Galley/Desk AC/DC/control route while the modules remain open.
- **Battery order:** finish Battery 2's cycle and Battery 3 individually; record all three rested voltages; parallel only at `<=0.1V` spread; then verify polarity, branch protection, SmartShunt synchronization, disconnect, current sharing, covers, and cable support.
- **Galley/Desk order:** skip full temporary tops. Preserve and record the sink/faucet/support/no-drill geometry for the mid-September `2026` final-walnut target; reinstall Desk/storage only after hidden routes are pulled.
- **KUS/water service:** replacement under-ring/main gasket/matched hardware are installed. Keep top sender access open through Cerbo setup and the final fill/pressure/dwell leak proof.
- **Starlink transition:** ground deployment through the existing truck-bed service route is accepted for the first trip. Bench-test the Type-4/RJ45 adapter and retractile coil, measure popup travel/wall thickness/connector OD, and do not cut a sidewall hole until the fixed-entry part is proven. `DS-H-MULTI-BLK` is withdrawn for the proposed wall geometry; `TBH-4` is only a measurement-gated candidate.
- **Payload:** capture door-sticker payload and staged scale weights. Treat total payload, rear axle load, rear tire load, and left/right balance as active constraints.

## Electrical-to-shakedown sequence
Purpose: finish the hard-mounted utilities and close furniture around tested systems without rebuilding access twice.

1. **Open-access 12V/sender endpoints**
   - Protect and mount the ICECO switch, finish the KUS-to-Cerbo pair, and wire/prove the SHURflo branch before moving the Desk/storage modules back in.
2. **Hidden rough-in**
   - Pull Galley and Desk DC/AC/control/data routes while access is open. Use a temporary switch/service plate where needed; final decorative paneling follows tested wiring rather than leading it.
3. **Battery-bank commissioning and restraint**
   - Finish Battery 2's cycle and Battery 3 individually, rest and record all three voltages, add hard perimeter/divider capture plus individual cam straps, parallel only within `0.1V`, then verify branch protection, polarity, disconnect, Lynx/shunt, covers, extraction, and current sharing.
4. **Wet-side acceptance**
   - Configure/sanity-check the installed KUS sender, finish fill/vent and sink plumbing, then run the dry pressure/dwell test with the service openings still accessible.
5. **Communications and AC closeout**
   - Use ground-deployed Starlink as the first-trip fallback while the retractile route is bench/geometry tested; finish the shore `L/N/PE` splice/dead checks and AC-out/GFCI acceptance without burying either service path.
6. **Module closure, final tops, and shakedown**
   - Reinstall the Desk/storage modules after hidden wiring, prepare the final templates for the mid-September `2026` walnut target, finish panels/retainers and terminal protection, torque/witness-mark, drive locally, and inspect for floor damage, leaks, insert spin, abrasion, module movement, and fastener loss.

### Cabinetry approach (recommended)
- Treat 80/20 as the *structure* and simple panels as the *skins*.
- Prioritize serviceability over concealment: every fuse/disconnect should be reachable without uninstalling major devices.
- Build “functional first”: once the electrical module works and survives vibration, add frosted panels + LED backlighting as a Phase 2 overlay.
