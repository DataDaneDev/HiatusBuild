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

## Current execution focus (working utilities into solar/heater/interior integration)
- Use [PROJECT_build_order_of_operations](../plans/PROJECT_build_order_of_operations.md) for active sequence and [LIVE_BUILD_CHECKLIST](../plans/LIVE_BUILD_CHECKLIST.md) for shop actions. Earlier install-window plans are historical references unless explicitly refreshed.
- The permanent Lonseal floor, electrical/Galley/Bench structure, water tank, and primary utility routes are installed. Remaining road restraint is specific: positive capture for the `3x 48V` batteries, separate `12V` battery, ICECO, appliances, bench lid, monitor/laptop assembly, plus terminal/cable protection.
- Starlink Standard 4 X works from its switched dedicated `12V` conversion branch through a `20A` blade fuse, including the fixed-body pass-through and retractile jumper. The fridge and pump are wired and switched. Three independent charging branches are installed: one driver-side `100W` DC outlet and two passenger-side `65W` DC outlets, each separately fused.
- Four duplex `120V` receptacles are wired: two devices/four plug positions on each side. Device count is closed, but branch acceptance remains open for listed boxes/covers/clamps, `LINE/LOAD`, downstream GFCI protection, polarity, PE continuity, labels, and trip/reset in inverter and shore modes.
- The immediate safety correction is one narrow removable switch/service face. Individually insulate and label every DC switch terminal; mount any `120V` device in a listed covered box physically separated from DC terminals. Loose electrical tape is not a finished live-terminal barrier.
- All four Renogy `175W` panels have arrived; one-panel physical test-fit plus measured layout indicates compatibility with Starlink and MaxxAir while using nearly the whole roof. Keep the one-string `4S1P` topology on the Victron `150/45`; direct-roof bonding waits on exact silicone/substrate preparation and coupon/cure proof. The PV retractile cord is ordered and still needs received-property, gland, structural-clamp, spring-force, and full-motion proof.
- The LF Bros diesel heater is the main unresolved systems install. The EVIL ENERGY `10 gal` tank/feed/vent package is purchased; dry-lay it with the heater, sealed floor turret, complete underbody exhaust/intake/fuel route, and rear driver-side storage module. Heat shield is supplemental; proximity to the truck fuel tank, fuel/EVAP/brake lines, wiring, undercoating, combustibles, full-tank restraint, and exterior or liquid-tight externally vented containment remain hard release gates.
- A mid-September black-walnut counter/desk routing appointment is planned. The LF Bros `10 L / 2.64 gal` plastic tank is selected as the never-fueled removable graywater cassette. Bring the actual sink and soap dispenser; prove bowl, actual tailpiece/waterless trap, faucet/soap hardware, support rails, `3/4-1 in` continuously falling drain, top tank inlet/vent, retention/removal, and low dump valve before final cuts. Reserve the on-hand `1/2 in` clear hose for the dump leg, not the sink drain.
- Alternator architecture is unchanged. Main remaining work is `F-04 200A/80V`, both WS500 temperature sensors, configuration read/save/program via the purchased USB-A-to-B cable, and controlled first charge.
- Preserve the roughly `24 in` desk until the rear module, real chair, knees, and aisle are mocked. Monitor/laptop arms need padded hard stops and positive restraint without LCD pressure; gas struts need actual lid-force geometry plus a closed latch/open stop; the air fryer needs hard stops and a strap/latch rather than tape alone. Final skins wait until heater, drain, electrical, and service-access tests pass.

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
- M6: electrical/Bench/Galley/tank hard-mount and `12V` checkpoints complete; battery matching/restraint, shore splice, wet-side acceptance, and Galley wiring closeout underway
- M7: shakedown and punch-list closure

## Build sequencing baseline (as-of 2026-08-30)
- The permanent floor and main structure are installed. Keep heater/fuel, sink/drain, switch/service, battery, and hidden-route access open until each subsystem is tested and positively restrained.
- Canonical sequence: temporary labeled switch/service face -> DC/AC closeout tests -> weather-window solar attachment and moving-cord proof -> purchased diesel-tank/heater/storage dry layout and underbody survey -> mid-September sink/soap/walnut routing -> `10 L` graywater mockup/completion -> WS500/fuse/sensor alternator commissioning -> rear storage/desk/real-chair fit -> bench/appliance/monitor travel restraint -> final skins -> shakedown.
- Detailed owner docs:
  - [PROJECT_build_order_of_operations](../plans/PROJECT_build_order_of_operations.md)
  - [FLOORING_subfloor_build_process](../implementation/FLOORING_subfloor_build_process.md)
  - [LIVE_BUILD_CHECKLIST](../plans/LIVE_BUILD_CHECKLIST.md)

## Immediate next decisions
- **Switch/service face:** cut and mount the narrow removable face now. Keep `120V` in a listed covered box with cable clamps and PE continuity, physically separate AC from DC, individually insulate every switch terminal, and label the fuse/slot/load before normal powered work.
- **Solar release:** verify received panel labels/connectors and exact silicone/substrate/cure instructions; wash/decontaminate the roof; coupon-test the stack; attach and shakedown one panel before repeating. Preserve `4S1P`; only the two free string ends enter the two-conductor transition/disconnect/MPPT route.
- **PV moving route:** when the ordered cord arrives, verify exact conductors, OD, voltage/wet/UV/cold rating, tangents, spring force, and the full `28 in` roof stroke. Use structural redundant exterior clamps/guarding; adhesive cable mounts may guide but may not carry spring or highway load.
- **Diesel heater/storage:** inventory the purchased tank/feed/vent package and dry-fit it with the heater/storage before drilling. Release only after mapping the turret and complete underside route around the truck fuel tank and all fuel/EVAP/brake lines, wiring, undercoating, and combustibles, plus approximately `86 lb` full-tank restraint and external vent/containment. Keep exhaust/muffler outside.
- **Counter/drain:** bring the actual sink and soap dispenser to the mid-September routing appointment. Prove drain-body/support/tank clearances and continuous slope into the selected never-fueled LF Bros `10 L` tank; use the existing `1/2 in` clear hose only for the normally closed dump leg.
- **Alternator:** fit `F-04`, both temperature sensors, and final support/protection; read and save the current WS500 profile before changing it; then program and run the controlled first-charge guide.
- **Interior fit/restraint:** preserve the `24 in` desk pending actual chair/aisle mockup. Give the air fryer hard stops plus strap/latch, give the monitor/laptop assembly a padded arm-unloading cradle without LCD pressure, and size bench gas struts from measured lid geometry with a separate latch and open stop.
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
   - Route the actual sink/soap hardware at the mid-September walnut appointment only after support/tank/service clearances pass. Prove the actual tailpiece/waterless trap and continuous `3/4-1 in` fall into the vented, retained, normally closed LF Bros `10 L` gray tank before cutting.
5. **Alternator and remaining road restraint**
   - Complete `F-04`, sensors, protection, WS500 profile backup/programming, and controlled first charge. Finish battery/ICECO/appliance/bench-lid/monitor restraint, terminal covers, and abrasion protection.
6. **Measured interior closure and shakedown**
   - Mock the real chair, rear module, `24 in` desk, and aisle before trimming. Then complete positive latches/cradles, final skins, torque/witness marks, local drive, and post-drive inspection for leaks, abrasion, movement, heat, and fastener loss.

### Cabinetry approach (recommended)
- Treat 80/20 as the *structure* and simple panels as the *skins*.
- Prioritize serviceability over concealment: every fuse/disconnect should be reachable without uninstalling major devices.
- Build “functional first”: once the electrical module works and survives vibration, add frosted panels + LED backlighting as a Phase 2 overlay.
