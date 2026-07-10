---
aliases:
  - Flooring and subfloor build process
tags:
  - hiatus/implementation
  - hiatus/flooring
  - hiatus/interior
status: active
related:
  - "[[PROJECT]]"
  - "[[TRACKING]]"
  - "[[PROJECT_build_order_of_operations]]"
  - "[[LIVE_BUILD_CHECKLIST]]"
---

# Flooring and Subfloor Build Process

**As of:** `2026-07-10`
**Role:** canonical owner for the truck-bed floor stack, moisture-path closeout, substrate preparation, hardpoints, Lonseal installation, and post-install verification.

## Current state

- Truck: `2021 Ford F-350 Regular Cab Long Bed` with an **aluminum pickup box/bed**, not a steel box.
- Camper shell is installed; major interior modules have been test-fit as an integrated layout.
- Existing floor materials:
  - factory/protective bed coating
  - `5/8 in` EPS strips in bed-rib valleys only
  - three removable `3/4 in` birch plywood sections, bottom faces/edges sealed and top bond faces untreated
  - one-piece Lonwood Madera Topseal sheet and `0.5 gal` Lonseal #650 adhesive in hand but unglued
- Bed sealing is partially complete. One wide Gorilla Waterproof Patch & Seal Tape roll has been used on discrete drill holes/small spots; a second matching roll is planned. Tape is **not** an approved seam-repair method.
- Floor closeout is now the next foundation gate before final module routing, full battery installation, and plumbing closeout.

## Stop-work holds

Do **not** drill final pickup-box holes, set the on-hand steel rivet nuts, or glue Lonseal until all five holds are closed:

1. **Aluminum compatibility:** final insert, bolt, washer, coating, and isolator stack complies with Ford aluminum-body guidance.
2. **Restraint class:** each attachment is classified as ordinary cabinetry/floor retention or heavy-system restraint. Thin box sheet is not assumed to be a crash-rated load path for the battery bench, `36 gal` water tank, or electrical module.
3. **Substrate:** Lonseal technical guidance is reconciled with the current single-layer `3/4 in` three-piece plywood floor.
4. **Moisture path:** obsolete holes are closed, intentional drains/weep paths are identified, and controlled ingress testing passes.
5. **Service map:** all required floor penetrations, module tabs, bolt access, and hole-recovery datums are frozen.

## Major corrections from the previous plan

### 1. The pickup box is aluminum

Ford's aluminum-body guidance controls the bed hardpoint design:

- do not use stainless fasteners against the aluminum body
- do not use standard plated-steel rivet nuts in the aluminum box
- use approved aluminum rivet nuts/Plusnuts or another Ford-compatible isolated attachment method
- use approved coated fasteners, aluminum washers where applicable, and non-conductive isolation between dissimilar-metal accessories and the body
- restore corrosion protection at drilled/cut edges
- do not use RTV silicone at aluminum-body attachment points
- never use an attachment point as an electrical ground

The purchased AOKLIT steel inserts in BOM row `127` and the stainless hardware in row `46` remain usable elsewhere, but they are **rejected for direct pickup-box hardpoints**.

Candidate only, not yet locked: Böllhoff aluminum `1/4-20` PLUSNUT `A25P280`, published grip range `0.020-0.280 in` and hole range `0.347-0.352 in`. Final selection still requires an actual box-sheet/grip measurement, backside clearance check, correct installation tool, and a matched-gauge coupon test.

### 2. The three-piece `3/4 in` substrate needs an explicit compliance decision

The current Lonseal Vehicle Installation Guide delegates substrate preparation to Lonseal's Interior Flooring Manual. The published Interior Flooring Manual calls for a minimum two-layer plywood system totaling `7/8 in`, with the top layer at least `1/4 in` APA underlayment grade.

Current floor: one `3/4 in` layer split into three pieces. It is common vehicle-build practice, but it is below the published interior-manual build-up and the moving joints can telegraph through or stress a one-piece adhered vinyl surface.

Close this gate by one of these two paths:

- **Preferred:** add a staggered `1/4 in` APA underlayment layer over the existing `3/4 in` base, mechanically tie it to the base without penetrating the truck bed, and mock the resulting `0.250 in` floor-height increase against doors, modules, electrical access, and furniture tabs before purchase/cut.
- **Exception path:** obtain written Lonseal technical acceptance for the exact single-layer `3/4 in` birch, three-panel, rib-supported mobile substrate and document the seam/joint preparation they require.

Do not bury this decision under adhesive. The current nominal valley-bottom stack is about `1.455 in`; a `1/4 in` underlayment would make it about `1.705 in`.

### 3. Module hardpoints must not be the only floor retention

Furniture bolts are not a complete substitute for a stable substrate. The subfloor must stay flat and registered if a module is removed for service. Establish independent floor retention/joint control before Lonseal so the adhesive and vinyl are not asked to bind three moving panels together.

### 4. Heavy systems need a stronger load-path review

Aluminum rivet nuts in thin box sheet may be acceptable anti-shift points for ordinary cabinetry after testing. They are not automatically adequate as the sole dynamic restraint for:

- the battery bench and its batteries
- the electrical module
- the `36 gal` water tank, which contains about `300 lb` of water when full
- any module whose failure could create a projectile or expose live high-current equipment

For those systems, verify distributed attachment geometry and a reinforced second load path using known pickup-box structure or OEM reinforced tie-down structure where practical. Do not count an untested catalog insert rating as a crash rating for the assembled module.

## Locked stack concept

| Layer | Material | Locked rule |
| --- | --- | --- |
| Finish | Lonwood Madera Topseal, Oregano, one piece | Uncut/glue-free until all closure gates pass |
| Adhesive | Lonseal #650 two-part epoxy | Horizontal surfaces only; full spread |
| Optional top underlayment | `1/4 in` APA underlayment grade | Preferred pending `0.250 in` clearance mockup or Lonseal written exception |
| Base subfloor | Three `3/4 in` birch plywood sections | Bottom/edges sealed; top bond face untreated; joints flat and independently controlled |
| Insulation | `5/8 in` EPS in valleys only | Filler/insulation, never a clamp-load member |
| Support | Aluminum bed-rib highs | Plywood bearing surface; verify each hardpoint's actual geometry |
| Vehicle | Coated aluminum pickup box | Preserve corrosion protection and intentional drainage |

No full-floor EPDM, foam sheet, or soft gasket belongs under the plywood. Soft material under the entire subfloor creates rocking and weakens fastener preload.

## Bed opening and sealing policy

Classify every opening before touching it.

| Opening type | Action |
| --- | --- |
| Abandoned drilled hole in smooth, sound metal | Small-hole tape patch may be acceptable after prep; use at least `1 in` coverage beyond every edge and hard-roll it |
| Larger or irregular obsolete hole | Use a fitted mechanical patch/plug plus Ford-compatible seam sealer and edge corrosion protection |
| Body seam, rail seam, or recurring gap | Do not bridge with Gorilla tape; use an appropriate automotive seam-repair method after identifying why the gap exists |
| Factory drain, weep path, body interface, or unknown opening | Do not seal by default; identify its function first and preserve a deliberate low-point drainage strategy |
| New hardpoint hole | Deburr, remove chips, restore aluminum corrosion protection, set the approved insert, and seal the finished pass-through without putting soft sealant in the structural clamp path |

### Gorilla tape limits

Gorilla's current directions say the surface must be clean and smooth and explicitly say **not for use on seams**. Therefore:

- use the existing/second roll only for discrete hole patches and compatible smooth-area spot repairs
- do not use it to blanket factory seams, unknown drains, bed-rail joints, or structural gaps
- inspect every existing patch for a hard-rolled perimeter, lifted corners, trapped grit, edge interference, and evidence of water tracking
- if an existing patch crosses a seam or an intentional drain, remove/rework it before the floor closes

### Moisture-path acceptance test

A visual check alone is insufficient before trapping the bed under EPS/plywood.

1. Vacuum and dry the bare bed.
2. Place dry paper towels or blotter strips inside at repaired holes, front corners, bed-rail interfaces, and low points.
3. Perform a bright-light check from below/inside where access permits.
4. Apply low-flow water to one exterior zone at a time. Do not use a pressure washer and do not flood electrical/camper interfaces.
5. Wait, inspect blotters and underside/cavity paths, and photograph any ingress.
6. Correct defects and repeat until dry.
7. After the first dusty/wet road shakedown, inspect reachable edges and mapped low points again.

If factory drains are intentionally retained, keep EPS/adhesive from blocking them and document their location. If any factory drain is intentionally closed because it is a proven upward-spray path, document the replacement inspection/drainage path; do not create a blind sealed cavity that can trap condensation or a future leak.

## Hardpoint design

### Load classes

- **F — floor retention:** keeps plywood/underlayment flat and registered independent of furniture.
- **C — ordinary cabinetry:** prevents light/medium furniture shift and racking after insert testing.
- **H — heavy-system restraint:** battery bench, electrical module, full water tank, or other high-consequence mass; requires explicit load-path review and redundant/distributed restraint.

Mark each hardpoint `F`, `C`, or `H` on the drawing and in photos.

### Required stack behavior

- Do not structurally screw furniture only to plywood.
- Do not clamp through EPS or another soft layer.
- Where bolt preload would otherwise crush plywood/vinyl or span a bed valley, use a rigid **aluminum compression sleeve** sized from the insert flange/bed support to the module foot. Cut it to the measured final stack; do not guess from nominal dimensions.
- Keep sealant in the annular weather seal around the pass-through, not under the sleeve's structural bearing faces.
- Keep final bolt heads accessible without removing charged batteries or dismantling fixed service equipment.
- Use a drill stop and verify below/behind every final hole for crossmembers, frame interfaces, wiring, fuel components, brake lines, sensors, and insert collapse clearance.

### Registration without drilling around live equipment

Do not drill the aluminum bed with connected/live electrical modules in place.

1. Finish module geometry enough to trust each foot/tab.
2. Isolate/de-energize the electrical system and remove loose batteries.
3. Photograph and label every module seam, shim, connector, service opening, and foot.
4. With modules positioned, transfer-punch/mark centers into tape or plywood; do not generate metal chips around live equipment.
5. Record each center from two fixed truck-bed datums and preserve a full-size template where practical.
6. Remove modules as assemblies.
7. Refit the plywood to its final datum, verify the underside/no-drill zone, then drill the aluminum bed with depth control.
8. Deburr, vacuum chips immediately, treat bare aluminum, and set/test inserts.
9. Use temporary locator bolts to prove the complete hole map before finish-floor glue-down.

If modules have already been removed before complete registration, reinstall only enough structure to transfer the real foot geometry. Do not create final holes from stale CAD or a single tape measurement.

## Execution sequence

### Gate A — freeze the physical map

- [ ] Finish remaining Desk/storage geometry corrections.
- [ ] Isolate electrical; remove loose batteries and energized sources from the drilling area.
- [ ] Photograph/label modules, shims, seams, connectors, service panels, and fastener groups.
- [ ] Trace module footprints and classify all candidate anchors `F`, `C`, or `H`.
- [ ] Record hardpoint centers from two fixed bed datums and make templates.
- [ ] Define all remaining floor penetrations and reserved future routes.

### Gate B — expose, clean, classify, and test the bed

- [ ] Remove modules and floor layers in a controlled order.
- [ ] Vacuum and degrease; remove loose adhesive, grit, and sharp debris.
- [ ] Map every hole, seam, drain, weep path, and existing patch before adding tape/sealant.
- [ ] Rework tape crossing seams/drains and mechanically repair larger holes.
- [ ] Let sealants cure per product instructions.
- [ ] Pass the controlled moisture-path test.

### Gate C — insulation, substrate, and aluminum-compatible hardpoints

- [ ] Inspect EPS for water, damage, proud/high points, and blocked drains; trim only where it rocks the plywood or blocks a deliberate path.
- [ ] Dry-fit all three base panels and eliminate rocking, high seams, unsupported edges, and grit.
- [ ] Close the Lonseal substrate gate: preferred `1/4 in` APA underlayment or written exception.
- [ ] Mock any extra floor height against module feet, doors, thresholds, service access, and roof-down geometry.
- [ ] Select aluminum inserts and coated fasteners from measured grip and Ford-compatible materials.
- [ ] Prove drill size, installation tool, collapse, spin resistance, and service removal on a matched-gauge aluminum coupon.
- [ ] Verify each truck hole's underside/no-drill zone and backside collapse clearance.
- [ ] Drill with a stop; deburr, vacuum, coat, set, and test each insert.
- [ ] Add independent floor retention/joint control.
- [ ] Cut/fit rigid aluminum compression sleeves at hardpoints that require them.
- [ ] Refit modules with temporary bolts and prove every hardpoint/access path.
- [ ] Remove modules again and confirm the floor remains stable by itself.

### Gate D — Lonseal dry fit and installation

- [ ] Decide flat perimeter vs intentional flash-cove before cutting. #650 is for horizontal surfaces; vertical/coved areas require Lonseal #400 contact adhesive or written manufacturer direction.
- [ ] Dry-fit the one-piece sheet, preserve pattern direction, and make the hole-recovery plan.
- [ ] Confirm substrate is permanently dry, smooth, flat, structurally sound, dust-free, and untreated on the bond face.
- [ ] Fill/sand approved joints and fastener depressions exactly as required by the accepted substrate path; vacuum again.
- [ ] Acclimate flooring, adhesive, and substrate at `65-85°F` for at least `48 h` before, during, and after installation.
- [ ] Stage two people, the `1/16 x 1/32 x 1/32 in` U-notch trowel, roller, low-speed mixer, blades, masking, gloves, eye protection, ventilation, ethyl-alcohol cleanup cloths, and waste plan.
- [ ] Mix the **entire** #650 A/B unit below `375 RPM`; do not partial-mix. Pot life is about `30 min` at `73°F`.
- [ ] Pour immediately, full-spread, and place the floor within the published `15 min` open/working windows without trapping air.
- [ ] Roll both directions. Manufacturer baseline is a `100 lb` three-section roller; the Vehicle Guide permits a properly used high-pressure hand roller where a full roller is impractical.
- [ ] Roll again `2-3 h` later.
- [ ] No foot traffic for `24 h`; no heavy furniture/traffic until the full `72 h` cure completes.

### Gate E — reinstall and prove

- [ ] Recover hardpoints with locator bolts/templates; do not blind-drill through finished vinyl.
- [ ] Seal all cut plywood/underlayment hole edges.
- [ ] Install compression sleeves and annular pass-through seals without contaminating bearing faces.
- [ ] Protect Lonseal during module installation.
- [ ] Reinstall modules and torque to the validated fastener/insert procedure.
- [ ] Witness-mark structural fasteners.
- [ ] Verify module racking, battery extraction, disconnect/fuse access, plumbing service access, and emergency egress.
- [ ] Perform a low-consequence local shakedown with heavy tanks/batteries staged only after their restraint gates pass.
- [ ] Reinspect and retorque as specified after the first drive; look for spinning inserts, vinyl indentation, sleeve settlement, moisture, abrasion, and shifted modules.

## Quality rejection criteria

Reject or rework if any condition exists:

- steel or stainless insert/fastener stack directly attached to the aluminum pickup box without an approved Ford-compatible design
- hardpoint over an unverified under-bed obstruction or without insert collapse clearance
- bolt preload carried by EPS, rubber, vinyl, or an unsupported plywood span
- furniture hardpoints are the only thing controlling three floor panels
- heavy module/tank/battery restraint relies only on untested thin-sheet inserts
- Gorilla tape bridging a body seam, intentional drain, or unknown gap
- lifted tape edges, trapped debris, damp blotter, or unexplained wet path
- proud EPS, rocking plywood, high joint, loose edge, or visible grit under the substrate
- unresolved single-layer substrate exception
- sealed/treated top plywood bond face without written adhesive approval
- unreserved penetration or inaccessible final bolt
- adhesive install outside `65-85°F`, partial A/B mix, missed working window, trapped air, inadequate rolling, or early heavy loading

## BOM synchronization

BOM owner: `bom/bom_estimated_items.csv`.

Key rows:

- `147`: `3/4 in` birch base plywood — purchased
- `148`: TotalBoat Halcyon edge/bottom sealer — purchased
- `149`: Lonwood Madera Topseal sheet — purchased/in hand, unglued
- `150`: Lonseal #650 `0.5 gal` — purchased/in hand, unmixed
- `174`: exact-notch trowel — purchased
- `175`: compact roller method — still must be physically confirmed
- `177`: polyurethane sealant — purchased/partially used
- `178`: Gorilla Waterproof Patch & Seal Tape — two-roll scope; one used/one planned; discrete holes only
- `214`: aluminum pickup-box rivet nuts/Plusnuts — required, exact SKU/quantity pending measured grip
- `215`: rigid aluminum floor-hardpoint compression sleeves — required where stack geometry needs them; exact cut lengths pending
- `216`: conditional `1/4 in` APA underlayment — hold until clearance mockup or Lonseal written exception

Do not maintain a second hand-calculated flooring total here; the BOM CSV owns quantity, price, and purchase status.

## Source hierarchy

1. Ford SVE Bulletin `Q-222R1`, *Attaching Accessories to Aluminum Panels and Structure* (repo copy: `references/Ford_Q-222R1_Attaching_Accessories_to_Aluminum_Panels_and_Structure.pdf`).
2. Ford General Body Builder Layout Book, aluminum body section (current public edition checked during the `2026-07-10` audit).
3. Lonseal Vehicle Installation Guide (repo copy: `references/lonseal flooring installation guide.pdf`).
4. Lonseal #650 Technical Data Sheet: <https://lonseal.com/wp-content/uploads/2024/11/TDS_650_110524.pdf>.
5. Lonseal Interior Flooring Manual: <https://lonseal.com/wp-content/uploads/2026/07/Interior_Flooring_Manual_070226.pdf>.
6. Gorilla Waterproof Patch & Seal Tape directions: <https://gorillatough.com/product/gorilla-waterproofing-tape-black/>.
7. Böllhoff RIVNUT/PLUSNUT catalog (repo copy: `references/Bollhoff_RIVNUT_PLUSNUT_catalog_US.pdf`) and the selected insert manufacturer's installation data.

If a product label/SDS or newer manufacturer document conflicts with this file, stop and use the current manufacturer requirement.
