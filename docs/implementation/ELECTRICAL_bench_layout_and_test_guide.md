# Electrical Bench Layout + Test Guide (Garage Use)

As-of date: `2026-03-27`

Purpose: provide a practical, print-friendly game plan for building and validating the electrical closet module on the ground before final install.

Related docs:
- `docs/core/ELECTRICAL_48V_ARCHITECTURE.md`
- `docs/implementation/ELECTRICAL_overview_diagram.md`
- `docs/implementation/ELECTRICAL_fuse_schedule.md`
- `docs/plans/STARTER_PLAN_electrical_and_flooring_pre_camper.md`

---

## 1) Build intent lock (this guide assumes)

- Architecture remains `48V core + 12V distribution + shore/inverter AC`.
- Alternator path baseline is the dedicated `48V` secondary alternator path (`Mechman + WS500 + APM-48`).
- Electrical closet is a two-plane vertical corner build:
  - **Board A**: against bed wall (high-current `48V` hardware).
  - **Board B**: against bulkhead (controls, `12V`, AC support hardware).
- Closet sits above battery zone.
- Structural mounting intent is through-bolts with washers and lock nuts (no wood screws for permanent component mounting).

---

## 2) Recommended sequence (ground build -> test fit -> hard mount)

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

- Keep equal-length parallel battery cables as locked in architecture docs.
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

Pass when:
- No polarity/continuity mistakes and all terminations documented.

### T1: Low-risk controls and comms
- Validate control circuits and monitoring links first (`WS500` control path, comms, panel labeling).
- Confirm `Upfitter #3` control path is treated as low-current signal only.

Pass when:
- Control/monitoring paths behave as expected with no unexplained faults.

### T2: 48V core energization (no alternator)
- Bring up house `48V` path first.
- Verify expected voltage at key nodes and no abnormal heat/smell/noise.
- Confirm disconnect behavior and basic inverter/charger DC-side response.

Pass when:
- Stable voltage and normal behavior at all checkpoints.

### T3: 12V distribution validation
- Validate Orion-fed `12V` junction behavior and branch fusing.
- Test representative `12V` loads one at a time, then combined.

Pass when:
- `12V` rail remains stable under expected test loads.

### T4: AC path validation
- Validate AC-in and AC-out paths in staged order with small known loads first.
- Confirm branch protection behavior and outlet polarity/GFCI behavior.

Pass when:
- AC paths behave correctly in shore and inverter modes.

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
- Do not lock roof/solar final terminations.
- Do not permanently close access panels before all staged tests pass.
- Do not use main `48V` disconnect as first alternator shutdown method while charging is active; use `Upfitter #3` (`WS500` disable path) first.
