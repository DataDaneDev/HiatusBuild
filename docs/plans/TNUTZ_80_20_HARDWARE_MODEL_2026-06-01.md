---
aliases:
  - TNUTZ 80/20 hardware model
  - TNUTZ shopping cart worksheet
tags:
  - hiatus/plan
  - hiatus/8020
  - hiatus/procurement
status: draft
related:
  - "[[PROCUREMENT_purchase_list_2026-05-26]]"
  - "[[PROJECT_build_order_of_operations]]"
  - "[[INTERIOR_furniture_layout_and_galley]]"
---

# TNUTZ 10-Series Hardware Model — Hiatus Interior Buildout

_As of `2026-06-25`. Status: WIP TNUTZ shopping-cart / visual-aid worksheet with current dated cut-list workbook artifact. Consolidated order owner, not final fabrication geometry._

Freshness note `2026-06-01`: this file is the detailed owner for the current TNUTZ/80-20 order consolidation. The owner still needs to review the visual aids and WIP cart before submitting any order. Use [PROCUREMENT_purchase_list_2026-05-26](PROCUREMENT_purchase_list_2026-05-26.md) only as the short procurement summary.

Current cut-list artifact `2026-07-04`: the current best module assignment / garage cut-list workbook is [`assets/module-cutlists/2026-07-04_module-cutlist-and-assignments.xlsx`](assets/module-cutlists/2026-07-04_module-cutlist-and-assignments.xlsx). Date-led filenames in this folder are the convention going forward; rename the file when a material module-assignment revision changes the current shop artifact.

## Combined cart review — `2026-06-05`

Source: owner-provided Amazon cart text plus TNUTZ cart text. This is a pre-submit review worksheet, not proof of purchase.

### Immediate cart verdict

- **TNUTZ order should stay the one-shot order** because the visible cart total is high relative to item subtotal: line-item subtotal is about `$995.64`; cart total is `$1,292.38`; implied shipping/tax/fees are about `$296.74` / `29.8%` over item subtotal.
- **Do not split TNUTZ.** Add TNUTZ-only or shipping-sensitive items now if they are likely needed.
- **Extrusion pricing is acceptable:** `EX-1010` is `$24.94` per `94 in` stick / about `$3.18/ft`; `EX-1020` is `$39.98` per `94 in` stick / about `$5.10/ft`.
- **Amazon is acceptable for easy-return commodity hardware**, but keep the frame standard as `1/4-20`. Generic kits may include metric screws/T-nuts; treat those as incidental unless deliberately isolated.
- **Screw-head correction after owner clarification:** the Amazon `1/4-20 x 1/2 in flat-head` screws are not countersunk flat-heads; they are effectively low-profile pan/button-style socket screws. They are acceptable if the Allen socket engagement is good and the head bears cleanly on the brackets/plates. Button/pan/flanged-button heads remain safer bulk defaults if socket strip-out or small bearing area appears during test assembly.
- **Current cart has 23 sticks of `EX-1010` plus 1 stick of `EX-1020`.** If the target was strictly `23` total sticks, reduce `EX-1010` to `22`. If shipping is the constraint, keeping `23 + 1` is defensible.
- **Owner field check later confirmed the delivered `EX-1010` sticks are regular 4-slot pieces.** The cart/order does not show any explicit tri-slot/one-flat-side extrusion, so current planning should not assume any `1010-S` pieces.

### Parsed Amazon cart

Amazon subtotal shown by cart: `$747.94` for `31` items. Individual item prices were not included in the pasted text, so item-level price checking needs cart screenshots/links if exact SKU comparisons are required.

| Class | Parsed quantity | Review |
| --- | ---: | --- |
| BLCCLOY T-shape joint plate kit with `M5` hardware | `8 sets` | **Questionable.** Likely metric hardware. Keep only if the plate geometry works with 10-series and holes can accept or be drilled for `1/4-20` clearance. |
| BLCCLOY T-corner 90° kit with `M6` hardware | `10 sets` | **Probably usable as brackets only.** M6 holes usually clear `1/4 in` better than M5, but use `1/4-20` T-nuts/screws for the build standard. |
| BLCCLOY L-corner 90° kit with `M6` hardware | `10 sets` | **Probably usable as brackets only.** Same metric-hardware caveat. |
| Sutton Concepts 4-hole joining plate, 10 pack | `10 plates` | **Keep.** Useful reference/comparison plates; not enough alone for module seams. |
| Abeicy `1/4-20` roll-in spring T-nuts, 100 pack | `200 nuts` | **Keep/increase later if needed.** Good post-assembly accessory/panel nuts. Combined cart has about `800` single T-nuts before generic-kit hardware. |
| ARES WING dual heavy gas monitor arm | `1 arm` | **Conditional keep.** OK for parked ergonomics only if the AW3423DWF gets a padded travel dock/cradle that unloads the arm during driving. |
| Ergounion VESA laptop tray | `1 tray` | **Conditional keep.** Good parked accessory. Do not let a laptop ride there offroad. |
| FORRCKY 20-set 10-series 90° corner brackets | `80 sets` | **Keep.** This is the main cheap-corner quantity. Use with `1/4-20` hardware if holes fit. |
| FORRCKY 1010 heavy-duty corner bracket / gusset kit | `10 sets` | **Keep if listing is now true 1010/10-series.** This is the Amazon heavy-gusset substitute for expensive TNUTZ `CB-010-K`; verify hole spacing and use the `1/4-20` hardware standard where possible. |
| Abeicy 2-hole inside corner brackets, 25 pack | `50 brackets` | **Keep.** Good light/medium inside corners. |
| 16 in stainless piano hinges, 4 pack | `4 hinges` / `64 in total` | **Change if bench lid wants continuous hinge.** Four short hinges act like separate hinges, not a true continuous hinge. Buy a real `48–72 in` continuous hinge for the large bench lid if geometry allows. |
| Black TPE edge trim | `16.4 ft` | **Keep.** Useful anti-rattle/edge protection. |
| Birch veneer edge banding | `50 ft` | **Keep/defer.** Finish item; not critical to frame day. |
| Ravinte 16 in folding shelf brackets | `2 brackets` | **Keep for table/bench-extension experiments.** Add positive latch/support if it becomes a sleeper/road-load component. |
| DMWD 30A 12V / 20A 120VAC rocker switches | `5 switches` | **Use only for low-current auxiliary/service control unless exact circuit/listing is verified.** Do not use for 48V battery circuits or permanent AC branch shortcuts. |
| BNUOK `1/4-20 x 1/2 in` low-profile socket screws, 100 pack | `800 screws` | **Keep if test fit is good.** Owner clarified these are not countersunk flat-heads; they are low-profile pan/button-like screws. Button/pan heads only matter if these strip easily or do not bear cleanly on generic brackets. |
| 6061 flat bar `3/16 x 1 x 12 in` packs | `25 bars` / `25 ft` | **Keep.** Good DIY plates/VESA tabs. Yields about `141` two-inch plates or `72` four-inch plates with `1/8 in` kerf if dedicated entirely to plates. |
| 1010 internal L-shape inside connectors | `12 sets` | **Keep as sample/light hidden connectors.** Do not make hidden-only connectors the main load path. |

### Parsed TNUTZ cart

| Item | Qty | Unit | Extended | Review |
| --- | ---: | ---: | ---: | --- |
| `EX-1010` 1 x 1 smooth T-slot, `94 in` | `23` | `$24.94` | `$573.62` | **Keep.** Treat the purchased/delivered sticks as regular 4-slot `EX-1010`; no tri-slot / one-flat-side `1010-S` substitution is assumed. |
| `ET-010-1/4-20` economy T-nut | `600` | `$0.16` | `$96.00` | **Keep.** Good low-cost bulk. Add more roll-in/drop-in later if closed-frame changes require it. |
| `CB-010-K` 4-hole inside corner gusset | `8` | `$4.80` | `$38.40` | **Low for load corners.** If this is truly the only TNUTZ order, increase to at least `24`; `36` is better. Add cost from current qty: `+16 = $76.80`, `+28 = $134.40`. |
| `CBS-010-B` 3-hole slotted inside corner bracket | `20` | `$3.60` | `$72.00` | **Keep.** Useful adjustable/heavier corner class. |
| `1 x 1 x 1/8` 6063 angle stock, `94 in` | `2` | `$8.96` | `$17.92` | **Keep.** Very cheap custom tabs/stops/LED/panel brackets. |
| Liquidation 1/4 in aluminum angle gusset profile, 6 in | `7` | `$2.95` | `$20.65` | **Keep if geometry is useful.** Treat as custom gusset stock. |
| `HC-010-B` hidden 45° corner connector | `4` | `$1.75` | `$7.00` | **Keep as samples.** Not critical. |
| `ETD-010` double economy T-nut | `8` | `$0.49` | `$3.92` | **Keep.** Small useful sample. |
| 1/4-20 special tap for 10-series | `1` | `$10.00` | `$10.00` | **Keep.** Needed for tapped-end options. |
| `JIG-010-A` access-hole drill jig for 1020 + #7 bit | `1` | `$36.85` | `$36.85` | **Keep if using end fasteners/access holes.** Add spare #7 bits separately; one bit can break/dull. |
| `EF-010-1/4-20` blank end fastener assembly | `25` | `$0.95` | `$23.75` | **Keep.** Good clean end-fastener stock; not the primary vibration/load strategy. |
| `COVER-010-GRY` t-slot cover, 78 in | `4` | `$1.40` | `$5.60` | **Keep.** |
| `COVER-010-BLK` t-slot cover, 78 in | `6` | `$1.40` | `$8.40` | **Keep.** Combined covers total `65 ft`. |
| `AC-010-B` nylon cable tie mount with hardware | `25` | `$0.75` | `$18.75` | **Keep.** Useful cable control. |
| `BUM-010-TS` rubber tread strip | `12 ft` | `$1.15` | `$13.80` | **Keep.** Useful anti-rattle/contact/tread strip. |
| `GAS-010-A` economy panel gasket | `30 ft` | `$0.30` | `$9.00` | **Keep.** Cheap and useful for removable panels. |
| `EX-1020` 1 x 2 smooth T-slot, `94 in` | `1` | `$39.98` | `$39.98` | **Keep.** Good monitor spine / high-rigidity local member. |

### Combined hardware posture

- Single T-nuts directly counted: `600` TNUTZ economy + `200` Amazon roll-in = `800`, plus `8` double T-nuts and unknown metric kit hardware. For a no-stall build, target is closer to `1,000` usable `1/4-20` T-slot nuts. **Amazon can cover the last `200` quickly**, so this is not a TNUTZ blocker.
- Cheap corner bracket count is high enough for mockup and light/medium frame work: `80` FORRCKY 10-series sets + `50` Abeicy inside brackets + `20` BLCCLOY M6 bracket sets + `20` TNUTZ slotted/stock gusset classes + samples. **The weak point is not bracket count; it is heavy/load gusset count and screw/head compatibility.**
- DIY plate capacity from `25 ft` of `3/16 x 1 in` 6061 flat bar is strong. Keep flat bar and fabricate straight/L plates instead of buying every TNUTZ joining plate.
- The current carts are good for a flexible prototype/build-floor order, but they need a few corrections before submission.

### Recommended pre-submit changes

1. **No tri-slot substitution to carry forward.** Treat the purchased `EX-1010` sticks as regular 4-slot pieces unless a future order explicitly adds a one-flat-side profile.
2. **Heavy/load gussets:** TNUTZ `CB-010-K` is structurally nice but expensive at `$4.80` each. Owner intends to use the corrected Amazon 1010 heavy-gusset kit as the main substitute; buy TNUTZ `CB-010-K` only where exact fit/quality matters most.
3. **Amazon/TNUTZ: add or verify these shop consumables:** `9/32 in` clearance bits, spare `#7` tap bits, tap handle, cutting fluid, deburring/countersink tool, blue threadlocker, paint pen/witness marker, flat washers/fender washers.
4. **Bench lid: buy one real long continuous hinge** if the bench-top hinge line is long and straight. The four `16 in` hinges can be butted together and may work, but are not as clean as a single continuous hinge because each segment has separate pin alignment, gaps, and screw-pattern interruptions.
5. **Travel hardware missing:** add over-center draw latches / positive latches, rubber bumpers, webbing straps, and strap anchors for monitor/bench/service panels. Magnets are good for light hatches, but road-load items still need positive retention.
6. **Monitor mount:** the dual gas arm is acceptable only with a padded travel cradle/dock and arm restraint. Use the `EX-1020` mast and/or flat-bar VESA/backing plates to keep the arm mount from being just a desk-skin load.

### Buy / hold summary

- **Buy from TNUTZ now:** extrusion, `1020`, tap/jig/end-fastener tooling, gasket/tread/covers, cable mounts, angle stock, bulk TNUTZ T-nuts, and only the TNUTZ heavy gussets needed for exact-fit/high-confidence load corners.
- **Buy from Amazon now after edits:** 10-series cheap corner brackets, corrected 1010 heavy-gusset kit, roll-in `1/4-20` T-nuts, low-profile socket screws after test-fit, flat bar, edge trim, hinge/latch/propping hardware, monitor arm if paired with a travel cradle.
- **Hold until later:** drawer slides, final cabinet pulls, final cosmetic skins, exact sliding-door track, large drawer hardware order, gas struts for bench lid.

## Purpose

Calculate a robust TNUTZ/80-20 hardware order for the current Hiatus interior buildout using the actual intended module layout:

- Bulkhead/front = low bench / battery-bench structure.
- Driver bulkhead = electrical tower/closet up toward the `46 in` build-height envelope.
- Driver side = electrical tower merges into fixed computer desk, then driver-side tailgate storage.
- Passenger front = raised fridge stand, roughly `16 in` tall / a bit over one foot.
- Passenger side after fridge = `36 in` tall galley/wet run all the way to the tailgate.
- Modules must be disconnectable for disassembly/service.
- Weight-bearing surfaces should use stronger gussets and positive mechanical fastening.
- Order source: TNUTZ.
- Owner inventory: many `1/4-20` and `5/16` bolts already on hand; many plusnuts for truck/camper attachment.

This model intentionally overbuilds structural connection hardware versus a minimal sim-rig style frame. It is designed for vibration, serviceability, module removal, and real camper abuse.

## Hard assumptions

1. Primary extrusion remains `10-series` / `1 in` profile, currently `EX-1010` style full-length stock, with a local `EX-1020` monitor/high-rigidity allowance.
2. Current WIP extrusion stock target is about `23 x 94 in` `EX-1010` sticks plus `1 x 94 in` `EX-1020` stick unless the owner reduces `EX-1010` to keep the total stick count at `23`. Do not vendor pre-cut; submit full-length stock only after the visual aids and module assumptions are reviewed.
3. Structural T-slot hardware should be `1/4-20`; use `5/16` only for truck/camper plusnut anchoring where the plusnut/hole pattern calls for it.
4. No hidden-only joints for critical furniture. Hidden connectors can be nice visually, but this build needs visible/serviceable gussets and plates for inspection and retightening.
5. Module seams use external joining plates so the bench/tower/desk/fridge/galley can be separated later without destroying the frame.
6. Panels are overlay/removable after the skeleton is proven; panels can add shear later, but the extrusion frame should stand on its own for mockup.

## Layout model

Visual artifacts:

- SVG: [`assets/t-nutz-hardware-2026-06-01/topdown-module-hardware-model.svg`](assets/t-nutz-hardware-2026-06-01/topdown-module-hardware-model.svg)
- PNG: [`assets/t-nutz-hardware-2026-06-01/topdown-module-hardware-model.png`](assets/t-nutz-hardware-2026-06-01/topdown-module-hardware-model.png)
- Current dated workbook: [`assets/module-cutlists/2026-07-04_module-cutlist-and-assignments.xlsx`](assets/module-cutlists/2026-07-04_module-cutlist-and-assignments.xlsx)

These are functional connector models, not dimensional fabrication geometry.

```text
TOP = cab / bulkhead / cabover
BOTTOM = tailgate / rear entry
LEFT = driver side
RIGHT = passenger side

CAB / BULKHEAD
┌───────────────────────────────┬───────────────────────────────┐
│ M2 DRIVER ELECTRICAL TOWER    │ M1 BULKHEAD / BATTERY BENCH   │
│ 46 in-ish service spine       │ low bench / restrained mass    │
│ ties down to bench + wall     │ disconnectable service lids    │
├───────────────────────────────┼───────────────────────────────┤
│ M3 DRIVER COMPUTER DESK       │ M5 PASSENGER FRIDGE STAND     │
│ 24 x 48-ish work surface      │ ~16 in raised load frame       │
│ tied to electrical tower      │ pump/service volume below      │
├───────────────────────────────┼───────────────────────────────┤
│ M4 DRIVER TAILGATE STORAGE    │ M6 PASSENGER 36 in GALLEY     │
│ rear utility/storage bay      │ wet/counter run to tailgate    │
│ removable cargo restraint     │ removable service panels       │
└───────────────────────────────┴───────────────────────────────┘
TAILGATE / REAR ENTRY
```

## Connector classes used in the model

### H — heavy/load-bearing corner

Use where a human, fridge, countertop, monitor spine, or heavy electrical board can load the structure.

- TNUTZ: `CB-010-K` — 10 Series 4 Hole Inside Corner Gusset.
- Hardware per connector: `4` structural T-nuts + `4` screws.
- Use at:
  - bench top/seat/lid support;
  - fridge stand top frame;
  - galley counter top frame;
  - desk top frame;
  - monitor/electrical tower base and top bracing;
  - any corner that will rack while driving.

### S — standard corner

Use for lower rails, internal dividers, light panel-support rails, and non-seat/non-counter corners.

- TNUTZ: `CB-010-A` — 10 Series 2 Hole Inside Corner Gusset.
- Hardware per connector: `2` structural T-nuts + `2` screws.

### D — disconnect / straight module tie

Use to tie two modules together while keeping them separable later.

- TNUTZ: `JP-010-D` — 10 Series 4 Hole Joining Plate.
- Hardware per connector: `4` structural T-nuts + `4` screws.
- Use across vertical seams such as bench-to-tower, tower-to-desk, desk-to-tailgate storage, fridge-to-galley, and galley-to-rear tie points.

### L — 90-degree plate / flat anti-rack tie

Use where a face frame needs flat-plane anti-rack reinforcement or a removable L-shaped module seam.

- TNUTZ: `JP-010-G` — 10 Series 4 Hole 90° Joining Plate.
- Hardware per connector: `4` structural T-nuts + `4` screws.

### F — truck/camper anchoring foot

Use where extrusion frame attaches to bed floor, bulkhead, bed wall, or camper hardpoints.

- TNUTZ: `FM-010-A` or `FM-010-B` — 10 Series Floor Mount Base Angle.
- Hardware per connector: `2` structural T-nuts + `2` screws into extrusion, plus owner-supplied plusnut bolt/washer into truck/camper.
- Use `5/16` bolts only where the plusnut/hardpoint accepts them cleanly. Do not force `5/16` into 10-series slots.

### P — removable panel/access mount

Use after the frame geometry is proven for overlay panels, light service covers, and removable inspection panels.

- TNUTZ options: `AC-010-E` 10 Series Nylon 1/4-Turn Panel Mount Block, `PR-010-A` panel retainer, or `QTB-010-*` quarter-turn/drop-in studs where appropriate.
- Hardware per panel point: `1` light/panel T-nut + `1` screw/stud.
- Do not use magnets as primary retention for anything heavy or safety-critical.

## Module-by-module connector model

```text
Legend: H = heavy 4-hole gusset, S = standard 2-hole gusset,
        D = straight joining plate, L = 90° joining plate,
        F = floor/wall anchor foot, P = removable panel mount point.
```

- `M1` bulkhead / battery bench:
  - `H x12`: top bench perimeter, lid/seat support, battery restraint bracing.
  - `S x8`: lower frame, internal battery partitions, non-load-bearing support rails.
  - `D x6`: disconnect ties to driver electrical tower and passenger-side structures.
  - `F x6`: bed floor/bulkhead anchoring points.
  - `P x8`: battery/service lid and removable access panel points.

- `M2` driver bulkhead electrical tower:
  - `H x8`: vertical service frame, heavy electrical-board support, top/bottom anti-rack nodes.
  - `S x6`: shelf/secondary rail connections.
  - `D x4`: removable ties to bench and desk module.
  - `L x4`: anti-rack face ties / tower-to-sidewall alignment.
  - `F x6`: floor/bulkhead/sidewall anchoring points.
  - `P x6`: electrical inspection/dead-front/removable cover points.

- `M3` driver computer desk:
  - `H x10`: desk top perimeter, front corners, wall-side support, monitor-spine base allowance.
  - `S x6`: lower rails and non-critical crossmembers.
  - `D x4`: disconnect ties to electrical tower and rear storage.
  - `L x4`: anti-rack plates under/behind work surface.
  - `F x4`: floor/wall anchoring points.
  - `P x6`: removable modesty/service/cable panels.

- `M4` driver tailgate storage:
  - `H x4`: top/cargo-restraint frame corners.
  - `S x8`: lower/light storage frame.
  - `D x4`: disconnect ties to desk/driver-side rear structure.
  - `F x4`: floor/sidewall anchoring points.
  - `P x6`: storage/service panel points.

- `M5` passenger fridge stand:
  - `H x12`: top fridge support frame, lateral restraint, anti-rack bracing.
  - `S x8`: lower frame and under-fridge service-bay rails.
  - `D x4`: disconnect ties to galley and adjacent bench/wet-spine structure.
  - `L x4`: top-plane and side-plane anti-rack plates.
  - `F x4`: floor/tank-side anchoring points.
  - `P x4`: pump/accumulator access panel points.

- `M6` passenger 36 in galley run:
  - `H x14`: counter-height top frame, bay stations, rear/entry counter edge.
  - `S x10`: lower rails, panel edges, plumbing service rails.
  - `D x6`: disconnect ties to fridge stand and rear/tailgate module seam.
  - `L x4`: flat-plane anti-rack plates along long galley run.
  - `F x6`: floor/sidewall anchoring points.
  - `P x12`: plumbing/winterization/fill/graywater service panel points.

## Base hardware count from the model

These are the exact counts produced by the connector model before order-margin rounding.

| Item | Base count |
| --- | ---: |
| `CB-010-K` 10 Series 4 Hole Inside Corner Gusset | 60 |
| `CB-010-A` 10 Series 2 Hole Inside Corner Gusset | 46 |
| `JP-010-D` 10 Series 4 Hole Joining Plate | 28 |
| `JP-010-G` 10 Series 4 Hole 90° Joining Plate | 16 |
| `FM-010-A` or `FM-010-B` 10 Series Floor Mount Base Angle | 30 |
| `AC-010-E` / `PR-010-A` panel mount/retainer points | 42 |
| `ST-010` 1/4-20 Standard T-nuts, structural | 568 |
| `ET-010` / `DT-010` / `DB-010` 1/4-20 light or panel T-nuts | 42 |
| `1/4-20 x 1/2 in` button/flanged screws for structural brackets | 568 |
| 1/4-20 panel screw / quarter-turn stud | 42 |
| Owner plusnut anchor bolts/washers to truck/camper | 30 |

## Recommended TNUTZ order quantities

Order quantities are rounded up because this is a vibration-prone camper build, because exact spans are still being validated, and because a few extra connectors prevent a stalled build day.

### Structural frame hardware

- `CB-010-K` 10 Series 4 Hole Inside Corner Gusset — **qty 72**
  - Use for seat/bench/fridge/desk/galley/electrical tower load corners.

- `CB-010-A` 10 Series 2 Hole Inside Corner Gusset — **qty 56**
  - Use for lower rails, dividers, light support rails.

- `JP-010-D` 10 Series 4 Hole Joining Plate — **qty 36**
  - Main removable straight module-seam hardware.

- `JP-010-G` 10 Series 4 Hole 90° Joining Plate — **qty 24**
  - Flat L/anti-rack plates and removable 90-degree seams.

- `FM-010-A` or `FM-010-B` 10 Series Floor Mount Base Angle — **qty 36**
  - Use for truck/camper/floor/bulkhead anchor points.
  - Pick `FM-010-B` where the 2 in leg gives better plusnut spacing or a better load path; use `FM-010-A` where space is tight.

### T-nuts and screws

- `ST-010` 1/4-20 Standard T-nut — **qty 650**
  - Structural default. Use these for gussets, joining plates, floor mounts, and anything carrying real load.
  - If a lot of your existing hardware requires post-assembly insertion, substitute some of this count with `DB-010` spring-ball or `DT-010` drop-in T-nuts, but do not rely only on economy nuts for the structural frame.

- `ET-010` 1/4-20 Economy T-nut or `DB-010` / `DT-010` drop-in light T-nut — **qty 100**
  - For removable panels, light cubbies, cable clamps, labels, accessory brackets, and future changes.

- `1/4-20 x 1/2 in` button-head or flanged button-head screws — **qty 650 if your current bolt stock is not the right head/length**
  - TNUTZ carries `1/4-20 x 1/2″ Flanged Button Head Screw` and black/stainless button-head versions.
  - If you already have enough low-profile `1/4-20 x 1/2` screws, do not rebuy all of these.
  - Avoid long bolts bottoming in the slot or protruding into service cavities.

- `1/4-20` panel screws / quarter-turn studs — **qty 100**
  - Only needed if using quarter-turn/removable panel hardware now.

### Removable panel/service hardware

- `AC-010-E` 10 Series Nylon 1/4-Turn Panel Mount Block or `PR-010-A` 10 Series Panel Retainer — **qty 60 total panel points**
  - Use for electrical inspection covers, plumbing/wet-spine covers, light cosmetic panels, and storage panel retention.
  - For frequent-service panels, favor quarter-turn/pullable hardware over screws buried under cushions.

### Truck/camper anchoring consumables

- Owner-supplied plusnuts: **reserve at least 36 anchor locations**.
- `5/16` bolts/washers: use only for plusnut/frame-to-truck hardpoint attachments if that is the plusnut size.
- Add large OD washers or backing plates where sheet/bed structure needs load spread.
- Use isolation/bedding where aluminum meets painted steel: neoprene/EPDM/paint protection, not squishy structure.

## Do not buy / avoid for this order

- Broad `15-series` main stock package — still not the default.
- Hidden-only connectors for major load paths.
- Final drawer-slide lengths.
- Permanent cosmetic skins.
- Magnetic-only panels for anything heavy, structural, or safety-critical.
- Vendor pre-cut final lengths until the review worksheet is physically validated.

## Design rules for assembly

1. Build each module as its own subassembly first.
2. Use `D`/`L` joining plates only at module seams so the modules can disconnect later.
3. Use `H` gussets on every top frame or load-bearing surface.
4. Use `F` floor/wall anchors only after the module position is proven with the actual shell/roof/door/aisle sweep.
5. Do not close panels until service actions pass with real hands/tools:
   - battery extraction;
   - electrical disconnect/fuse access;
   - pump strainer cleaning;
   - accumulator service;
   - winterization/blowout/low-point drain;
   - fridge removal/vent access;
   - desk cable service;
   - diesel heater access.
6. Use witness marks on structural fasteners after final torque.
7. Re-torque after first rough drive/shakedown.

## Practical build sequence

1. **Cut/prototype extrusion stock only after placement review.** Keep the `23 x 94 in` `EX-1010` order full-length unless reducing one stick for a strict total-stick target; keep the `EX-1020` monitor/high-rigidity stick full-length until the mast geometry is proven.
2. **Assemble M1 bulkhead bench first** because it is the mass and datum base.
3. **Stand M2 electrical tower on M1**, check roof/down/entry sweep, then add temporary D/L seam plates.
4. **Build M3 driver desk off M2**, verify seated workday and monitor-safe geometry.
5. **Build M5 fridge stand independently**, validate fridge height, ventilation, lid/slide/removal, pump access below.
6. **Build M6 galley as a long service rail**, not a closed cabinet; keep wet panels removable.
7. **Add M4 rear storage last** so it does not steal tailgate/entry/service clearance.
8. Anchor to truck/camper only after the full aisle/roof/service map passes.

## Final validation before placing/submitting the TNUTZ hardware order

- Confirm whether you want black anodized visible brackets or plain zinc/aluminum where hidden.
- Confirm whether your current `1/4-20` bolt stock includes enough low-profile `1/2 in` button/flanged screws. If yes, reduce screw purchase.
- Confirm plusnut size for final frame-to-truck anchors before buying any additional anchor bolts.
- Confirm if any module truly needs `15-series`; current model says no, except possibly a future monitor mast/spine if the tested 10-series spine is too flexible.
- Re-check the rough cutlist placements before cutting: `17-19 in` corner, `30 in` driver verticals, `65 in` vs `64 in`, and `24+20 in` cooler/front interpretation.
- Reconcile the current cart against the `2026-06-05` combined cart review before checkout: owner later confirmed the purchased `EX-1010` stock stayed regular 4-slot with no tri-slot substitution; `CB-010-K` increase and Amazon screw/head-style correction remain the relevant follow-ups.
