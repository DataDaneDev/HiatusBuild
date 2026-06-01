---
aliases:
  - Hiatus May 29 work plan
  - TNUTZ rough cutlist worksheet
tags:
  - hiatus/plan
  - hiatus/history
  - hiatus/8020
status: reference
related:
  - "[[PROJECT_build_order_of_operations]]"
  - "[[PROCUREMENT_purchase_list_2026-05-26]]"
  - "[[TNUTZ_80_20_HARDWARE_MODEL_2026-06-01]]"
---

# Historical Hiatus Work Plan — 2026-05-29 Tonight + Tomorrow

_As of Friday 2026-05-29, 21:04 MDT. Assumption at the time: tomorrow is one hard 8-hour build block._

Freshness note `2026-06-01`: this is a **historical/reference worksheet**, not the active build order. The rough TNUTZ cutlist is preserved for review, but active TNUTZ shopping-cart consolidation lives in [TNUTZ_80_20_HARDWARE_MODEL_2026-06-01](TNUTZ_80_20_HARDWARE_MODEL_2026-06-01.md), with procurement summary in [PROCUREMENT_purchase_list_2026-05-26](PROCUREMENT_purchase_list_2026-05-26.md).

## Mission

Get momentum back without creating rework: order the extrusion tonight, fix the charging/programming issue first tomorrow, then hard-mount and truck-fit the board.

## Historical tonight plan — not current instruction

### 1. Place the extrusion order

- Finalize the cart and submit it tonight.
- Buy only extrusion/hardware tied to proven structure.
- Avoid broad `15-series` overbuy unless a specific heavy freestanding module truly needs it.
- Keep uncertain final-cut geometry out of the order if it depends on tomorrow’s truck fit.
- Current owner intent as of `2026-06-01 00:26 MDT`: order `17` full-length TNUTZ `94 in` sticks of `10-series` extrusion, not vendor pre-cut pieces, because the transcript-derived list was not heavily validated and needs excess for changed dimensions, bad cuts, and likely missing/adjusted crossmembers.

#### Rough 10-series extrusion cutlist to review before ordering/cutting

Source: transcript-derived May 2026 measurement video plus quick `94 in` stock optimization. This is a **review worksheet**, not final geometry. Validate placements and re-measure spans before cutting; assume some flubbing in the original transcription/mapping.

Aggregated cuts:

- `19 in` — qty `2` (`1` front ambiguous `17-19 in`; `1` driver-side undetermined short member)
- `20 in` — qty `2`
- `21 in` — qty `4`
- `23 in` — qty `3`
- `24 in` — qty `4`
- `30 in` — qty `2` (tentative driver-side desk/diesel-heater-box verticals)
- `31 in` — qty `4`
- `36 in` — qty `7`
- `47 in` — qty `3`
- `48 in` — qty `3`
- `64 in` — qty `3`
- `65 in` — qty `2`

Placement map to review:

- Electrical/front cabinet: `36 in x2`, `23 in x3`, `47 in x3`, `19 in x1` ambiguous `17-19 in`.
- Cooler/front skeleton: `24 in x2`, `20 in x2`; interpreted as ground-level plus upper-cabinet-level members.
- Cooler/rear skeleton: `31 in x4`.
- Rear long stringers: `65 in x2`; probably one low and one upper.
- Side / under-desk / long tie-ins: `48 in x2`, `64 in x3`.
- Galley verticals: `36 in x5`.
- Water tank area: `48 in x1`, `21 in x4`.
- Driver side / diesel heater / desk area: `24 in x2`, `30 in x2` tentative, `19 in x1` undetermined.

Stock optimization note:

- Raw cut length: `1,370 in` / `114.2 ft`.
- `15 x 94 in` works only if saw kerf is ignored; exact-fit pairs like `64+30` and `47+47` become impossible once kerf is included.
- With realistic kerf (`1/16-1/8 in` per cut), optimized minimum is `16 x 94 in` sticks.
- Current order target: `17 x 94 in` sticks to add one extra full stick for validation drift and shop mistakes.

Review gates before cutting:

- Confirm whether each measured span is outside envelope, centerline/visual estimate, or clear span between uprights.
- Deduct `10-series` profile width where pieces fit between uprights instead of running full outside dimension.
- Confirm whether `65 in` should really be `64 in`.
- Re-check the `17-19 in` front corner and both `30 in` driver-side verticals.
- Confirm the `24 in + 20 in` cooler-front interpretation is not double-counted.
- Do the actual cutting plan with the measured blade kerf and mark every stick before making first cuts.

### 2. Prep tomorrow’s bench

- Clear the board/work area.
- Put required tools, fasteners, labels, meter, laptop/MK3/Victron gear in one place.
- Set the electrical system to a safe resting state before bed.

### 3. Do not do tonight

- Do not charge the other two batteries.
- Do not keep cycling the battery into BMS trip/protect.
- Do not start a late-night hard-mounting rabbit hole.

## Historical tomorrow plan — 8-hour crunch worksheet

### Hour 0–1 — Fix charge/programming issue first

Goal: stop the apparent overcharge/BMS trip before more physical build work.

- Open current MultiPlus/charger settings.
- Preserve current/default settings somewhere before changing them.
- Set conservative LiFePO4 commissioning targets unless the battery manual says otherwise:
  - Absorb/bulk: about `56.8–57.2V` measured at battery terminals.
  - Absorption time: `15–30 min`.
  - Float: about `54.0V`.
  - Equalization: off.
  - Temperature compensation: off unless manual explicitly requires it.
  - Charge current: conservative; about `20A` per 100Ah battery is a safe troubleshooting default.
- Verify with DMM at battery terminals, not only app/display voltage.
- Stop immediately if it returns to red/protect/0A near the top end.

Exit gate: charger behavior is sane enough for supervised testing, or electrical charging stays disabled and the day proceeds as non-energized mechanical work.

### Hour 1–2 — Board layout final check

- Put every component on the board in its intended final position.
- Confirm cable bends, fuse access, disconnect access, service reach, and cover clearance.
- Mark final hole locations.
- Label anything that would be annoying after mounting.

Exit gate: no blocked terminals, no inaccessible fuses, no cable path that requires uninstalling major gear later.

### Hour 2–4 — Hard-mount the board

- Drill/mount components in priority order:
  1. Main heavy components / load-bearing pieces.
  2. Bus/fuse/disconnect components.
  3. Small control/monitoring gear.
  4. Cable-management anchors.
- Keep service loops and strain relief.
- Do not final-trim cables unless the truck fit confirms geometry.

Exit gate: board can be lifted/moved as a real assembly without loose critical parts.

### Hour 4–5 — Bench sanity check

- Tug-check mounts and cable restraints.
- Confirm no exposed copper, rubbing, pinched conductors, or loose hardware.
- Confirm disconnects/fuses are reachable.
- If energizing: do only a short supervised low-risk check.

Exit gate: safe enough to physically test fit in the truck.

### Hour 5–7 — Truck test fit

- Move board into the truck carefully.
- Check:
  - Fit envelope.
  - Door/cover/seat/bed interference.
  - Cable entrance/exit paths.
  - Service access once installed.
  - Mounting points and vibration support.
  - Whether extrusion/cabinet assumptions still hold.
- Mark conflicts directly with tape/notes/photos.

Exit gate: know whether the board geometry works as-is, needs minor relocation, or needs a redesign before final install.

### Hour 7–8 — Lock next actions

- Write the short punch list:
  - Must-fix before install.
  - Nice-to-fix later.
  - Parts/hardware missing.
  - Extrusion/order corrections if the truck fit changed anything.
- Clean up tools enough that the next session starts fast.
- If charging settings were changed and verified, record the final values.

## Priority rules

1. Extrusion order tonight is non-negotiable.
2. Programming/overcharge fix happens before more charging.
3. Hard-mount only after service access and cable paths are checked.
4. Truck test fit beats CAD assumptions.
5. The other two batteries are not urgent right now.

## Definition of a good finish

By end of tomorrow:

- Extrusion order is placed.
- Charger settings are safer or charging is intentionally disabled pending diagnosis.
- Electrical board is hard-mounted enough to handle as an assembly.
- Board has been test-fit in the truck.
- A short punch list exists for the next build block.
