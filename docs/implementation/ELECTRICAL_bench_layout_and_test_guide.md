---
aliases:
  - Electrical bench layout guide
tags:
  - hiatus/implementation
  - hiatus/electrical
status: active
related:
  - "[[ELECTRICAL_48V_ARCHITECTURE]]"
  - "[[ELECTRICAL_fuse_schedule]]"
  - "[[OPERATIONS]]"
---

# Electrical Bench Layout + Test Guide

As-of date: `2026-07-19`

Purpose: provide a practical, print-friendly game plan for building, hard-mounting, post-live cleanup, and staged validation of the electrical module before mobile install or permanent enclosure/panel closeout.

Related docs:
- `docs/core/ELECTRICAL_48V_ARCHITECTURE.md`
- `docs/implementation/ELECTRICAL_overview_diagram.md`
- `docs/implementation/ELECTRICAL_fuse_schedule.md`
- `docs/plans/PROJECT_build_order_of_operations.md`

---

## 1) Build intent lock (this guide assumes)

- Architecture remains `48V core + 12V distribution + shore/inverter AC`.
- Alternator path baseline is the dedicated `48V` secondary alternator path (`Mechman + WS500 + APM-48`).
- Electrical closet is a two-plane vertical corner build:
  - **Board A**: against bed wall (high-current `48V` hardware).
  - **Board B**: against bulkhead (controls, `12V`, AC support hardware).
- Closet sits above battery zone.
- Structural mounting intent is through-bolts with washers and lock nuts (no wood screws for permanent component mounting).
- The installed camper shell owns final outer dimensions and service-access geometry; garage/floor layouts are templates only until the two-plane mockup passes in-camper insertion, removal, cable-bend, fuse-access, and panel-access checks.

---

## 2) Recommended sequence (ground build -> test fit -> hard mount)

Current owner status (`2026-07-19`): the electrical module has passed the first-live checkpoint and is now hard-mounted through the finished floor to truck-bed hardpoints. The MultiPlus and combined AC breaker enclosure were removed for the lift and will remount into embedded pronged T-nuts. All three battery branch harnesses are cut, lugged, heat-shrunk, and landed at the battery-side busbars, but the batteries remain isolated pending individual charge/rest/voltage matching.

Immediate priority:
1. Remount the MultiPlus and AC breaker enclosure; prove/protect the full L5-30/`10/3` shore-inlet path before cutting and energizing it.
2. Charge Batteries 2 and 3 individually, rest/record all three voltages, and parallel only when maximum-to-minimum difference is `<=0.1V`.
3. Locate/install final Orion `F-06 20A/80V`; identify any X-marked Lynx fuse by slot (`F-03 60A/80V` in Slot 2, Slot 4 empty), then complete the `12V` battery branch and prove factory loads.
4. Preserve the current working topology; do not add alternator or AC-out branch complexity until these cleanup checks pass.
5. Add/verify labels, covers, torque witness marks, J-clamp strain relief, cable protection, and service access around the energized layout.
6. Keep AC-out branch/GFCI validation and Mechman/WS500 alternator commissioning as separate later gates.

### Phase L1: Build the two backer boards on the ground
1. Rip the `1/2"` sheet into Board A + Board B to your target envelope.
2. Mark orientation on both boards: `TOP`, `BOTTOM`, `FRONT`, `REAR`, `BED WALL`, `BULKHEAD`.
3. Place boards at `90` degrees on temporary braces/clamps to represent closet geometry.

Exit criteria:
- Two boards stand in correct orientation and are easy to reposition.

### Phase L2: Paper layout before drilling
1. Make 1:1 paper templates for each major component.
2. On each template, mark:
   - footprint
   - hole centers
   - cable entry/exit sides
   - keep-out for bend radius + tool access
3. Tape templates to boards and pencil trace candidate positions.
4. Reserve explicit channels:
   - high-current `48V` trunk path
   - low-current control/comms path
   - AC route path separated from DC path

Exit criteria:
- No blocked fuse access, no blocked terminals, and no impossible cable bends.

### Phase L3: Truck-bed dry fit (before full drilling)
1. Move bare boards (or cardboard stand-ins with same outer dimensions) into truck bed.
2. Validate insertion, rotation, and removal path.
3. Validate service access around door swing/panels.
4. Adjust board size or corner angle now if needed.

Exit criteria:
- Boards can be inserted and removed without forcing or trimming installed components.

### Phase L4: Pilot drill + subset mount
1. Pilot drill only (`1/8"` class) for critical components first.
2. Mount a subset first (example: disconnect, Lynx, shunt, Orion, one AC enclosure).
3. Re-check wrench access, cable swing, and service pull paths.
4. Only after pass, drill final hole sizes and mount remainder.

Exit criteria:
- Critical devices fit and are serviceable with real tools/hands.

### Phase L5: Final mounting + board prep
1. Through-bolt permanent component mounts.
2. Add backing washers/plates where loads are concentrated.
3. Seal plywood faces/edges after hole pattern is validated.
4. Label each component position and cable corridor directly on board.

Exit criteria:
- Boards are mechanically complete and labeled for wiring.

---

## 3) Suggested zoning by board

### Board A (bed-wall plane, high-current focus)
- Place heavier/high-current gear lower when possible for stability and short battery paths.
- Keep these grouped for short `48V` runs:
  - main disconnect
  - Lynx
  - shunt
  - major `48V` feeds/returns
- Keep alternator branch landing (`F-04` path) accessible and clearly labeled.
- Keep Class-T and major fuse service points reachable without removing adjacent equipment.

### Board B (bulkhead plane, controls + distribution)
- Place `12V` panel, Orion, monitoring/comms, and AC panel hardware here.
- Keep AC hardware grouped and physically separated from DC/control paths.
- Keep control and comms routing high/clean, away from high-current cable bundles.

---

## 4) Wiring layout rules (before you crimp anything)

- Keep parallel battery paths balanced by similar total loop resistance. Equal positive-only leads are not required if short/medium/long positives are offset by long/medium/short negatives.
- Before paralleling, charge/rest/measure each battery separately and require maximum-to-minimum terminal-voltage difference `<=0.1V`; do not use the final parallel bus to equalize a larger mismatch.
- Keep `48V` high-current paths short and direct.
- Keep AC and DC routing physically separated; cross at `90` degrees only when unavoidable.
- Use abrasion protection at every edge pass-through.
- Leave service loops at removable devices (do not strain to exact length).
- Do not cut final shell-dependent runs yet; only bench-module harnesses at this stage.

---

## 5) Bench test ladder (staged energization)

Use a stop/go ladder; do not skip steps.

### T0: Dead checks
- Verify polarity labels and continuity on every cable.
- Verify torque marks applied to all completed terminations.
- Verify fuse IDs/ratings match `docs/implementation/ELECTRICAL_fuse_schedule.md`.
- Before any AC energization, meter the AC system dead: AC-in and AC-out neutrals are isolated, PE/equipment ground is continuous through inlet/enclosure/MultiPlus/receptacle paths, and no fixed downstream neutral-ground bond exists.

Pass when:
- No polarity/continuity mistakes and all terminations documented.

### T1: Low-risk controls and comms
- Validate control circuits and monitoring links first (`WS500` control path, comms, panel labeling).
- Confirm `Upfitter #3` control path is treated as low-current signal only.

Pass when:
- Control/monitoring paths behave as expected with no unexplained faults.

### T2: 48V core energization (no alternator)
- Bring up house `48V` path first.
- Use pre-charge before closing the main disconnect into MultiPlus/inverter capacitance.
- Verify expected voltage at key nodes and no abnormal heat/smell/noise.
- Confirm disconnect behavior and basic inverter/charger DC-side response.

Current result (`2026-05-27`):
- Owner measured `55.5V` throughout the system, including at the MultiPlus.
- MultiPlus switch `I` brought inverter mode online; inverter light illuminated, slight hum was observed, and no error lights were reported.
- SmartShunt and Orion-Tr Smart were visible in VictronConnect.

Pass when:
- Stable voltage and normal behavior at all checkpoints, with labels/covers/torque marks verified after the first live session.

### T2.5: Shore / MultiPlus initial charge validation
- Build the AC-in-only path first: shore source/adapters -> portable EMS -> shore cord -> inlet -> AC-in breaker/disconnect -> MultiPlus AC-in.
- Keep AC-out branch breakers/loads disconnected for the first charge test.
- Confirm the T0 AC dead-checks are complete before shore energization.
- Set AC Input 1 label/type to `Shore power` and set the MultiPlus input current limit to the actual source. Use `10A` for first household tests and `12A` maximum policy on a normal `15A` outlet.
- Leave `DVCC` disabled unless a documented BMS/GX control path is added.
- Before sustained charging, program/verify MultiPlus LiFePO4 charge profile from the Dumfume manual (`MK3-USB + VEConfigure` or equivalent): absorption/float, charge current, equalization off, and lithium temperature-compensation behavior.
- Use the pre-charge procedure before closing the `48V` disconnect into MultiPlus capacitance.
- Leave alternator branch inactive and `F-04` out during shore-charge validation.
- Log starting/resting voltage, charge current, temperature, SOC/monitor readings, abnormal heat/noise/smell, input-current limit, and stop conditions.

Current result (`2026-06-01`):
- Short AC-in test passed at limited household-outlet draw: about `1294W` shore input and about `54.3V x 21.6A` (`~1173W`) battery charging in bulk.
- Charge-profile verification is now treated as passed for the current shore-charger setup: owner redid settings and confirmed first-battery behavior entered bulk, then quickly transitioned to absorption because the battery was already at/near `100%`, as planned. No second-battery charge is required just to validate the profile.

Pass when:
- Shore charging repeats normally with programmed battery settings, no unexplained BMS trips, abnormal heat, polarity issues, or AC faults, and logged values match expected limits.

### T3: 12V distribution validation
- Validate Orion-fed `12V` junction behavior and branch fusing.
- Test representative `12V` loads one at a time, then combined.

Pass when:
- `12V` rail remains stable under expected test loads.

### T4: AC path validation
- Validate AC-in and AC-out paths in staged order with small known loads first.
- Reconfirm neutral isolation, PE continuity, no downstream neutral-ground bond, and correct outlet polarity before applying known loads.
- Confirm branch protection behavior and test each GFCI receptacle in its installed branch context.

Pass when:
- AC paths behave correctly in shore and inverter modes, with GFCI behavior verified and no neutral/ground faults found.

### T5: Alternator path readiness (pre-engine integration)
- Confirm alternator branch hardware is present/labeled/serviceable.
- Confirm WS500 enable/disable control path labeling and fuse placement (`F-15`).
- Defer live engine alternator validation until full install context and safety controls are ready.

Pass when:
- Alternator branch is install-ready with shutdown path understood and labeled.

Stop conditions (halt and fix before continuing):
- Any reversed polarity, unexpected voltage, heating at terminals, damaged insulation, nuisance fuse trips, or unclear shutdown behavior.

---

## 6) Garage workday card (print/use)

Use one card per session:

- **Date:**
- **Board focus:** `A` / `B` / Both
- **Phase:** `L1` / `L2` / `L3` / `L4` / `L5` / `T0-T5`
- **What changed:**
- **What passed:**
- **What failed or needs rework:**
- **Next single action:**

---

## 7) Hold points (do not cross yet)

- Do not finalize shell-dependent cable cuts.
- Do not leave shore charging unattended while wiring is loose, unprotected, being rerouted, or missing required strain relief/covers; the MultiPlus profile itself is programmed/owner-verified.
- Do not treat the short AC-in charge test as AC-out branch commissioning; GFCI/outlet validation remains separate.
- Do not lock roof/solar final terminations.
- Do not permanently close access panels before all staged tests pass.
- Do not use main `48V` disconnect as first alternator shutdown method while charging is active; use `Upfitter #3` (`WS500` disable path) first.
