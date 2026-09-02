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
- As-of date: 2026-08-30
- Phase: working utility closeout plus solar/heater/interior integration
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

## Current execution focus (working camper into solar/heater/interior completion)
- Use [PROJECT_build_order_of_operations](../plans/PROJECT_build_order_of_operations.md) for active sequence and [LIVE_BUILD_CHECKLIST](../plans/LIVE_BUILD_CHECKLIST.md) for shop actions. Earlier install-window plans are historical references unless explicitly refreshed.
- The permanent Lonseal floor and main electrical/Galley/Bench structure are installed. The `3x 48V` bank has been paralleled and in regular use for an extended period; the batteries and ICECO are positively restrained. Remaining interior retention is the not-yet-installed air fryer, bench lid, monitor/laptop package, and other storage/cargo.
- Starlink Standard 4 X, the fridge, pump, three separately fused DC charging outlets, and the installed `12V`/`48V` system are in regular owner-reported use.
- All four duplex `120V` receptacles and the associated `120V` work are enclosed and in regular owner-reported use. Physical box/enclosure completion is closed; retain explicit checks for GFCI `LINE/LOAD` and downstream trip behavior, polarity, PE continuity, labels, and the separate MultiPlus/chassis/shell bonding task.
- The immediate safety correction is one narrow removable switch/service face. Individually insulate and label every DC switch terminal; mount any `120V` device in a listed covered box physically separated from DC terminals. Loose electrical tape is not a finished live-terminal barrier.
- All four Renogy `175W` panels have arrived. The solar pass-through, two-pole disconnect, fixed wiring, and MPPT connection are complete; no panels are connected yet. Remaining work is exact-material roof preparation/caulk-bonding, panel series wiring, roof-side cable support, and controlled PV commissioning on the existing `4S1P`/Victron `150/45` architecture.
- The LF Bros diesel heater is the main unresolved systems install. The EVIL ENERGY `10 gal` tank/feed/vent package is purchased; dry-lay it with the heater, sealed floor turret, complete underbody exhaust/intake/fuel route, and rear driver-side storage module. Heat shield is supplemental; proximity to the truck fuel tank, fuel/EVAP/brake lines, wiring, undercoating, combustibles, full-tank restraint, and exterior or liquid-tight externally vented containment remain hard release gates.
- Fresh-water plumbing, the KUS sender, and the `35 gal` tank are complete and have seen substantial owner-reported use. Remaining wet work is the sink after the mid-September counter work and the separate graywater system.
- Final wood direction is two live-edge Bubinga pieces: `48 in` Galley and `47 in` Desk. The earlier three-piece black-walnut concept is superseded; the Bench lid remains a separate unfinished item.
- Alternator charging is still disconnected. Owner-reported remaining install work is the protected PH-VAN red lead and Wakespeed read/save/programming, followed by the controlled first-charge verification.
- The FLEXISPOT Foldex chair is ordered. The HOTTAP has not arrived; propane geometry is mocked but final HOTTAP mounting, hose/clearance proof, leak test, and first burn wait on receipt.
- The existing camper has completed a successful owner-reported shakedown. Newly installed solar, heater/fuel, HOTTAP, and interior restraints still require their own post-install checks.

## Scope
- In scope: electrical, charging, solar, communications, interior structure/cabinetry, operations process, maintenance tracking
- Out of scope for phase 1: non-critical aesthetic upgrades and major unrelated truck mechanical projects

## Requirements baseline (draft)
- Workday autonomy target: load model v5 profiles indicate `3,915 Wh/day` (`core_workday`), `4,829 Wh/day` (`winter_workday`), and `624 Wh/day` (`minimal_idle_day`), including conservative future-audio allowance; actual near-term office-only use may be lower. Battery reserve floor policy is `20%` minimum SOC
- Connectivity reliability target: Starlink is the primary path and its installed direct-DC/pass-through/retractile route works; complete weather/travel acceptance and preserve the OEM-cable/ground-deployment recovery path.
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
- Solar and physical diesel-heater routing decisions remain pending and tracked in `docs/core/TRACKING.md`; the diesel tank/feed/vent hardware is purchased but not installation-released. Shore hardware is selected, with inlet/cable-support details handled during physical install. The HOTTAP LP path stays within the cylinder box/outdoor heater package—no propane passthrough into the camper. The separate direct BLUE/RED camper water ports are installed; rear-box heater/cylinder integration and operating-clearance proof remain open.

## Milestone plan (draft)
- M0: requirements baseline frozen
- M1: system architecture selected (electrical + comms + thermal)
- M2: BOM v1 complete and procurement started
- M3: camper installed / physical shell available for real measurements
- M4: subsystem bench validation complete
- M5: measured interior block envelopes and service map complete
- M6: electrical/Bench/Galley/tank hard-mount, battery parallel/restraint, fresh plumbing/KUS, enclosed AC devices, and working `12V`/`48V` utility systems complete
- M7: solar, heater/fuel, sink/graywater, alternator, HOTTAP, and interior-storage completion; existing camper shakedown passed, with subsystem-specific shakedowns still required

## Build sequencing baseline (as-of 2026-09-02)
- The permanent floor, main structure, battery bank/restraint, fresh-water system, enclosed AC devices, and primary utility systems are in service. Keep heater/fuel, sink/graywater, solar, alternator, HOTTAP, switch/service, and hidden-route access open until each new subsystem is finished and tested.
- Canonical sequence: heater turret and diesel-tank/storage integration -> mid-September Bubinga/sink geometry -> graywater -> protected PH-VAN red plus Wakespeed programming/first alternator charge -> solar caulk/bond/wire/commission -> HOTTAP receipt/mount/commission -> bench lid/air fryer/monitor/laptop/storage -> final skins and subsystem-specific shakedowns.
- Detailed owner docs:
  - [PROJECT_build_order_of_operations](../plans/PROJECT_build_order_of_operations.md)
  - [FLOORING_subfloor_build_process](../implementation/FLOORING_subfloor_build_process.md)
  - [LIVE_BUILD_CHECKLIST](../plans/LIVE_BUILD_CHECKLIST.md)

## Immediate next decisions
- **Electrical safety closeout:** finish the labeled removable DC switch/service face. The `120V` enclosures and four outlet boxes are complete and operational; verify GFCI downstream trip behavior, polarity, PE continuity, and the MultiPlus/chassis/shell bonds rather than reopening the box-count task.
- **Solar release:** the pass-through, disconnect, stationary wiring, and MPPT landing are complete. Verify exact caulk/adhesive preparation and cure, then bond, series-wire, structurally support, and commission the panels in `4S1P`; only the two free string ends enter the completed two-conductor transition/disconnect/MPPT route.
- **Diesel heater/storage:** inventory the purchased tank/feed/vent package and dry-fit it with the heater/storage before drilling. Release only after mapping the turret and complete underside route around the truck fuel tank and all fuel/EVAP/brake lines, wiring, undercoating, and combustibles, plus approximately `86 lb` full-tank restraint and external vent/containment. Keep exhaust/muffler outside.
- **Counter/drain:** fit the actual sink and soap dispenser to the `48 in` Bubinga Galley surface at the mid-September appointment. Fresh plumbing and KUS are operational; finish only the sink termination and separate graywater system.
- **Alternator:** complete the protected PH-VAN red lead, read/save/program the WS500, then run the controlled first-charge guide.
- **Interior fit/restraint:** accept the ordered chair against the `47 in` Bubinga Desk and aisle. Build the bench lid, air-fryer home, monitor/laptop travel cradle, and remaining storage.
- **Payload:** capture door-sticker payload and staged scale weights. Treat total payload, rear axle load, rear tire load, and left/right balance as active constraints.

## Electrical-to-shakedown sequence
Purpose: close tested utilities and finish the interior without rebuilding access twice.

1. **Safe temporary service face and branch closeout**
   - Hard-mount/label the DC switches; keep the AC device in its own listed covered box. Verify every DC fuse/slot, polarity, load, and drop; verify both AC chains' boxes/clamps, `LINE/LOAD`, PE, polarity, and GFCI trip/reset under inverter and shore power.
2. **Solar weather-window work**
   - Verify the panel labels, connectors, direct-bond product, roof preparation, coupon, and cure. Prove one panel before repeating. On cord receipt, prove the two-end `4S1P` path, structural clamps/guard, gland, disconnect, full stroke, articulation, and MPPT entry before travel.
3. **Heater/storage integration**
   - Inventory/dry-lay the purchased `10 gal` tank/feed/vent package with the heater, sealed turret, underbody exhaust/intake/fuel route, containment, and rear storage. Drill only after the underside vehicle-line/heat/combustible survey and full-tank restraint pass; complete functional/CO/leak checks before skins.
4. **Countertop, sink, and graywater**
   - Route the actual sink/soap hardware at the mid-September Bubinga appointment only after support/tank/service clearances pass. Prove the actual tailpiece/waterless trap and continuous `3/4-1 in` fall into the vented, retained, normally closed LF Bros `10 L` gray tank before cutting.
5. **Alternator and remaining road restraint**
   - Wire the protected PH-VAN red lead, read/save/program the WS500, complete the preflight, and run controlled first charge. Batteries and ICECO are already restrained; finish air-fryer/Bench-lid/monitor/laptop/general-storage retention, terminal covers, and abrasion protection.
6. **Measured interior closure and shakedown**
   - Mock the real chair, rear module, `24 in` desk, and aisle before trimming. Then complete positive latches/cradles, final skins, torque/witness marks, local drive, and post-drive inspection for leaks, abrasion, movement, heat, and fastener loss.

### Cabinetry approach (recommended)
- Treat 80/20 as the *structure* and simple panels as the *skins*.
- Prioritize serviceability over concealment: every fuse/disconnect should be reachable without uninstalling major devices.
- Build “functional first”: once the electrical module works and survives vibration, add frosted panels + LED backlighting as a Phase 2 overlay.
