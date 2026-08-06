# Starlink + solar moving-roof umbilical

Status: **one-panel Starlink architecture selected; mount/cable package remains measurement- and bench-test-gated; solar deferred**
Last current-source check: `2026-08-06 04:34 MDT`

## Decision

Complete Starlink as its own pathway now. Install one dedicated rugged shielded RJ45 bulkhead in the fixed camper body near the Desk/router service zone, then bridge the pop-up movement with one removable shielded retractile Ethernet/PoE jumper. The same bulkhead must accept either the normal roof jumper or a long ground-deployment cable.

Solar is not part of this penetration or purchase. When the panel model, stringing, cold `Voc`, `Isc`, conductor size, and roof layout are real, add a separate PV-rated route and two-pole load-break disconnect. It may eventually sit beside the Starlink route, but it does not share conductors, connectors, or a guessed oversize gland.

This supersedes the prior no-new-hole/existing-service-route baseline, twin-coil-now, chain-first, guided-loose-loop, and shared-entry recommendations. The existing truck-bed service route and complete factory cable remain recovery paths, not the normal finished installation.

## Why the other two moving-section concepts lost

### Side-mounted energy chain — rejected as the default

A chain does not make the cable branch-proof. On an exposed vertical camper wall, the return bend still needs somewhere to collect when the roof closes. Without a measured recess or enclosed guide trough, the chain will project outward or bunch into a side lump. Keeping it against the wall would require another trough, retractor, or stow mechanism, increasing bulk and making trail removal harder.

An energy chain remains a contingency only if later geometry reveals a real inboard trough; there is no reason to buy one for the current exterior-wall concept.

### Loose cable/service loop in sleeve — rejected

Without an added spring reel, elastic take-up, or guided carriage, it is simply a slack cable hanging from two anchors. The sleeve supplies abrasion resistance but does not store slack. Adding the missing take-up hardware recreates a less predictable cable-carrier system.

### Meaning of `sheltered`

A route is sheltered only if an existing rigid camper feature projects outward farther than the cable and the cable stays inside that feature's contact shadow through the full roof stroke. No such location has been physically confirmed. The earlier `front guard` wording referred to an imagined fabricated pouch/deflector, not an existing Hiatus component, and is withdrawn.

No exterior always-connected cable is branch-proof. Normal-road mode keeps the coils attached; tight-trail mode powers/isolate the circuits, removes the coils, and caps the fixed ends.

## Selected Starlink physical layout

```text
MOVING ROOF / REMOVABLE MOUNT
  Standard 4 X terminal in TRIO protective edge frame
    -> upper STARGEAR Type-4/RJ45 adapter
    -> removable 3 m stretched shielded retractile jumper
    -> NE8MXR1-B-TOP-D locking/weather-sealed cable connector

FIXED CAMPER BODY
  NE8FDX-P6-W shielded RJ45 panel bulkhead with captive cap
    -> fixed interior shielded pure-copper Cat6A patch cable
    -> lower STARGEAR Type-4/RJ45 adapter
    -> Gen 3 router
    -> 12V-to-57V converter primary / factory AC supply + inverter fallback
```

Put the panel bulkhead in rigid fixed-body structure below the folding/moving seam and near enough to the Desk/router that the interior patch cable remains serviceable. Put the upper structural anchor directly above it on moving-roof structure/rail. Add a P-clamp behind the upper adapter joint and strain relief at the panel so neither electrical connector carries spring tension. The exact panel location, wall stack, anchor spacing, interior cable length, free extension, tangent lengths, and down-state coil projection still require a physical mockup.

The selected moving jumper must provide more free extension than measured roof travel plus endpoint routing and strain-relief reserve. The current upper-bound estimate is `36 in` lift + `8 in` fixed-body rise + `12 in` roof routing = `56 in` before drip-loop, tangent, and strain-relief reserve. A `6 ft` maximum-stretch coil is therefore too close to full extension; use the `3 m / 9.8 ft` stretched candidate and mock it through the complete roof stroke.

## Starlink cable, panel, and deployment topology

### Cable and panel topology

- Establish a working baseline with the complete factory Starlink cable, then remove and retain that cable as the unmodified direct recovery spare.
- Use one third-party Type-4-to-RJ45 adapter at the Standard 4 X terminal and one at the Gen 3 router dish-port end. A plain RJ45 plug does **not** plug directly into the router's proprietary dish port.
- From the router adapter, run a field-measured shielded pure-copper Cat6A patch cable to the rear of one [Neutrik `NE8FDX-P6-W`](https://www.neutrik.com/en/product/ne8fdx-p6-w) shielded feedthrough panel connector. Neutrik publishes Cat6A/10 Gbit/s, PoE Type 4 Class 8 / `100W`, `>1000` mating cycles, and IP65 both when correctly mated and when its captive cap is closed.
- Fit the lower end of the selected retractile jumper with [Neutrik `NE8MXR1-B-TOP-D`](https://www.neutrik.com/en/product/ne8mxr1-b-top-d), the retractable TOP carrier that includes the matched Cat6A RJ45 plug and wire manager. It accepts `5.5-8.0 mm` cable OD and AWG `24/7-27/7` stranded conductors, so the listed `26 AWG` coil is conductor-compatible only if its measured jacket OD is also inside that range. It intermates with `NE8FDX-P6-W`; Neutrik's published incompatibility is with `NE8FDY-C6` / `NE8FDY-C6-B`, not the selected panel connector. The panel accepts an ordinary RJ45 plug for dry-weather ground deployment, but a plain RJ45 connection is not the weather-sealed/locked normal-road interface.
- Join the jumper's upper end to the terminal adapter using the adapter's threaded weatherproof RJ45 gland.
- Put structural P-clamps/anchors behind the upper exterior joint and beside the panel; do not let the Starlink socket, RJ45 contacts, or panel connector carry coil tension.
- Keep the Gen 3 router and selected `10-36V` input / `57V 4.5A` output converter in an accessible ventilated Desk/service cubby. Feed the converter from a dedicated fused `12V` branch; retain the factory AC supply at a fixed GFCI-protected receptacle as the inverter fallback. Do not power Starlink through the plug-in desktop pop-up module.

### Roof / ground mode

- **Roof mode:** protective-framed dish stays on the extrusion crossbars; retractile jumper stays connected at the dish and locks into the panel connector. Disconnect/cap at the panel before removing the dish or entering tight brush.
- **Ground mode:** remove the dish plus protective frame from the two crossbars, retain the usable factory kickstand, unplug the roof jumper from the terminal adapter, and connect a field-length outdoor shielded pure-copper Cat6A cord from the panel to the terminal adapter. An ordinary RJ45 cord is electrically/physically compatible with the panel for dry conditions; add a second compatible rugged carrier or use a purpose-built weather-sealed ground lead for rain/snow.
- Preserve the complete OEM Starlink cable for direct router-to-terminal recovery if any adapter, bulkhead, reterminated plug, or retractile jumper fails.

## Roof mount and branch-protection direction

Current lead: [TRIO Gen 3 Standard Speedmount](https://www.trioflatmount.com/products/gen3speedmount), black, current listed price `$275`. It is explicitly compatible with Standard 4, wraps/protects all four dish edges, is `1.85 in` high, is sold for permanent/temporary highway use, and leaves the factory kickstand usable.

Mount the complete TRIO-framed dish across two movable black `10-series 1020` (`1 x 2 in`) extrusion crossbars carried by the existing longitudinal roof tracks, with the `2 in` dimension vertical. For Yakima-style tracks, the dimensional lead is one set of eight Yakima `8810074` Anchor Plate A inserts (`3/4 x 7/8 in`, centered M6 thread), inserted from a track end rather than through the approximately `1/2 in` top slot. Use two small 10-series 90-degree brackets at each crossbar end: eight `M6 x 20 mm` fasteners down into the Yakima plates and eight `1/4-20` fasteners into roll-in 10-series T-nuts in the extrusion. Physically prove one plate in the actual track before ordering/cutting the crossbars.

Use the TRIO four corner mounting points with stainless `1/4-20` button-head screws into captured roll-in T-nuts in the crossbar top slots. This makes the full dish/frame assembly removable with one power-driver bit and four screws; do not design a separate loose plate unless the real hole/crossbar spacing proves it necessary. Use reusable wedge-lock hardware or equivalent vibration control, witness marks, and one independent secondary retention tether; do not rely on hand-tight thumb knobs for highway retention.

The protective frame improves side/edge survival but does not make the terminal branch-proof. For tight, brushy routes, disconnect at the panel, remove the four screws, and stow/ground-deploy the dish. A thick limb contacting the face or using the frame as a lever is still a no-go for roof carriage.

### Current-source shortlist

| Item | Current link / observed price | Posture |
| --- | --- | --- |
| `2x` STARGEAR Standard 4/4X/Gen 3 Type-4-to-RJ45 adapters | [Amazon `B0D9NB1SQC`](https://www.amazon.com/dp/B0D9NB1SQC) — `$58.99`, in stock/Prime at check | **Lead adapter pair.** Third-party/non-OEM; seller claims 24 AWG copper pigtails, full shielding and IP67 RJ45 coupling. Bench-test before vehicle install. |
| ZBLZGP 3 m stretched Cat6A retractile cable | [Amazon `B0H286KLWZ`](https://www.amazon.com/dp/B0H286KLWZ) — `$35.00`, two in stock/Prime at check | **Budget prototype only.** PUR, dual shield, pure-copper claim, but 26 AWG and no established review history. STARGEAR recommends 23 AWG or larger for third-party PoE runs, so this is not accepted until a loaded Starlink heat/dropout test passes. |
| L-com `TRD815SZ-CH-1-6F` industrial coil | [L-com product page](https://www.l-com.com/category-5e-ethernet-coil-cord-rj45-rj45-180d-tangents-f-utp-foil-shielded-26awg-high-flex-industrial-zero-halogen-tpu-teal-1-to-6f) | Higher-confidence industrial construction and useful `1-6 ft` geometry, but current retail price/stock could not be verified without vendor challenge and prior pricing was poor. Do not buy unless the Amazon prototype fails or a distributor price is acceptable. |
| Fixed-body RJ45 bulkhead | [Neutrik `NE8FDX-P6-W`](https://www.neutrik.com/en/product/ne8fdx-p6-w) / [Markertek](https://www.markertek.com/product/ne8fdx-p6-w/neutrik-ne8fdx-p6-w-d-shape-cat6a-panel-connector-shielded-feedthrough-rubber-sealing-ip65-when-mated-nickel) — `$23.79` at check | **Selected panel connector.** Shielded Cat6A feedthrough, PoE Type 4 Class 8 / `100W`, `>1000` cycles, rugged latch, captive cap, and IP65 correctly mated/capped. Rear panel plug is ordinary RJ45. Published rear-side body depth is about `29.5 mm`; allow additional cable bend/service space. |
| Roof-jumper cable connector | [Neutrik `NE8MXR1-B-TOP-D`](https://www.neutrik.com/en/product/ne8mxr1-b-top-d) / [Mouser](https://www.mouser.com/ProductDetail/Neutrik/NE8MXR1-B-TOP-D) — `$8.93`, `110` listed in stock at check | **Selected after coil OD verification.** Retractable TOP carrier includes the Cat6A plug and wire manager; accepts `5.5-8.0 mm` OD and AWG `24/7-27/7` stranded. Prefer this over bare `NE8MX-B-TOP`; do not use indoor `NE8MX-B-1` for the exterior connection. |
| Protective removable dish frame | [TRIO Gen 3 Standard Speedmount](https://www.trioflatmount.com/products/gen3speedmount) — `$275` at check | **Mount lead.** Standard 4 compatible; protects all four edges; kickstand remains usable. Through-bolt four corners to two extrusion crossbars with reusable stainless fasteners/captured T-nuts. |
| Gen 3 router DC converter | [Amazon `B0DLZWHPKJ`](https://www.amazon.com/dp/B0DLZWHPKJ) — `$38.99` at check | **Selected budget primary with factory-AC fallback.** Seller claims `10-36V` input and `57V 4.5A` output. Treat rating as seller-supplied, mount on a ventilated/noncombustible surface, and reject for heat, reboot, or voltage-instability behavior during loaded testing. |
| Lower exterior inline RJ45 joint | [trueCABLE Cat6A shielded waterproof coupler](https://www.truecable.com/products/cat6a-waterproof-couplers-shielded) / [Amazon `B0949S87V7`](https://www.amazon.com/dp/B0949S87V7) | **Fallback only.** No longer needed if the one-panel Neutrik interface and compatible cable carrier are accepted. |
| One-cable fixed-body entry | [Seaview retro-fit cable gland, Amazon `B077PQ4FGG`](https://www.amazon.com/dp/B077PQ4FGG) | **Withdrawn from the normal path.** The selected interface is a panel connector, not a through-cable gland. |
| Prior shared-entry candidate | [Scanstrut `DS-H-MULTI-BLK`, Amazon `B0CSTC4D3C`](https://www.amazon.com/dp/B0CSTC4D3C) — `$53.34` at prior check | **Withdrawn.** It is a horizontal cable-entry/deck-seal product, not the desired straight panel quick-disconnect. |
| Straight sidewall candidate | [Scanstrut `TBH-4`](https://www.scanstrut.com/marine/cable-seal/bulkhead/tbh-4) | **Withdrawn from this route.** It is a cable seal, not a detachable panel connector, and its larger multi-cable cut is not justified by deferred solar. |

Immediate bench/fit package is the STARGEAR adapter pair, ZBLZGP 3 m coil, `NE8FDX-P6-W`, `NE8MXR1-B-TOP-D` after the coil OD check, and a field-measured fixed Cat6A run. The `26 AWG` coil is accepted only after retermination inspection and the loaded heat/dropout test. The TRIO frame and four-fastener crossbar geometry can be dry-fit independently. Do not cut the camper wall or coil until the connector mockup, wall stack, panel interior clearance, and crossbar spacing are physically proven.

## Why the one-panel Neutrik path now wins

The prior rejection applied to a two-panel layout, which added unnecessary chassis connectors and RJ45 interfaces. The selected layout uses only one fixed-body `NE8FDX-P6-W`: it provides the solid panel quick-disconnect Dane asked for, is explicitly rated for `100W` 802.3bt Type 4, protects the normal roof connection when correctly mated, caps cleanly when disconnected, and still accepts an ordinary RJ45 ground-deployment cord. The upper dish end continues to use the Type-4 adapter's own weatherproof gland, so a second panel connector adds no value.

- [Neutrik `NE8FDX-P6-W`](https://www.neutrik.com/en/product/ne8fdx-p6-w) is female RJ45 on the rear, so the panel part itself needs no punch-down/crimp tool. The published rear panel cut uses one `>=24 mm` center opening plus four `>=3.2 mm` M3 clearance holes on `19.0 +/- 0.1 mm` horizontal by `24.0 +/- 0.1 mm` vertical centers; it is not the common two-screw D-series cutout.
- `NE8MX-B-TOP` is the correct outdoor choice over `NE8MX-B-1`, but it is only a carrier and does not include an RJ45 plug. The final buy-list preference is the newer `NE8MXR1-B-TOP-D`, which adds the matched Cat6A plug/wire manager and a retractable shell while keeping IP65 in the correctly mated TOP connection.
- [Neutrik `NE8MX6-T`](https://www.neutrik.com/en/product/ne8mx6-t) is the Cat6A/PoE++ self-termination alternative, but its published `7-9.5 mm` cable-OD range must match the selected coil.
- [Neutrik `NE8MX-B`](https://www.neutrik.com/en/product/ne8mx-b) accepts a preassembled RJ45 cable without retermination, but it is not the exterior `TOP` weather-sealed solution.

**Release gate:** measure the actual coil tangent OD and inspect its shield/conductors before choosing the cable-side part. Do not drill the D-size panel opening or cut the premade coil merely because the chassis connector itself is selected.

## Full Starlink buy list — planning lock, not purchase record

### Buy-now bench/mount package

| Qty | Item | Current source / allowance | Notes |
| ---: | --- | --- | --- |
| 1 | TRIO Gen 3 Standard Speedmount, black | [TRIO](https://www.trioflatmount.com/products/gen3speedmount) — `$275` | Standard 4/4X frame; preserve kickstand. |
| 1 pair | STARGEAR Type-4/RJ45 adapters | [Amazon `B0D9NB1SQC`](https://www.amazon.com/dp/B0D9NB1SQC) — `$58.99` | One at terminal, one at Router 3 dish port. |
| 1 | ZBLZGP 3 m / 9.8 ft stretched retractile Cat6A cable | [Amazon `B0H286KLWZ`](https://www.amazon.com/dp/B0H286KLWZ) — `$35.00` | Budget prototype; `26 AWG` pure-copper/PUR/dual-shield seller claims. Measure OD before cutting. |
| 1 | Neutrik `NE8FDX-P6-W` panel feedthrough | [Markertek](https://www.markertek.com/product/ne8fdx-p6-w/neutrik-ne8fdx-p6-w-d-shape-cat6a-panel-connector-shielded-feedthrough-rubber-sealing-ip65-when-mated-nickel) — `$23.79` | Fixed-body female/female feedthrough with captive cap. |
| 1, optional 2nd spare | Neutrik `NE8MXR1-B-TOP-D` | [Mouser](https://www.mouser.com/ProductDetail/Neutrik/NE8MXR1-B-TOP-D) — `$8.93` each | Includes Cat6A plug/wire manager. One installed; a second is cheap insurance for a first-time termination. |
| 1 | VCELINK Cat7/6A shielded RJ45 crimper | [Amazon `B08LPMXM3Q`](https://www.amazon.com/dp/B08LPMXM3Q) — `$17.99` | Budget tool with standard/non-pass-through and shield-clip capability. It is not on Neutrik's approved-tool list; inspect contact depth and shield crimp, continuity-test, and have an AV/network shop reterminate if it does not make a clean full crimp. |
| 1 | Basic RJ45 continuity tester | [Amazon `B01M63EMBQ`](https://www.amazon.com/dp/B01M63EMBQ) — `$9.99` | Verify pins `1-8` in T568B order. This budget tester is not a Cat6A certifier; separately meter shield-shell continuity. |
| 1 | EAZUSE Gen 3 `12V` converter | [Amazon `B0DLZWHPKJ`](https://www.amazon.com/dp/B0DLZWHPKJ) — `$38.99` | `10-36V` input / `57V 4.5A` seller claim. Factory Starlink AC supply remains the inverter fallback. |
| 1 | Interior shielded Cat6A pure-copper patch cable | Cable Matters S/FTP `26 AWG`, field-measured length; allow `$10-15` | Ordinary shielded RJ45 male at both ends: rear of panel to RJ45 side of the lower STARGEAR adapter. It does not plug straight into the router dish port. |

### Roof-track/extrusion package — order only after one anchor plate fits

| Qty | Item | Specification / allowance |
| ---: | --- | --- |
| 1 set / 8 plates | Yakima `8810074` Anchor Plate A | `3/4 x 7/8 in`, centered M6 thread; current retail allowance about `$20`. Insert from track end. |
| 2 | Black 10-series `1020` extrusion crossbars | TNUTZ `EX-1020-BLACK` or equivalent; cut after track-center and TRIO-hole mockup. Use `2 in` axis vertical. |
| 8 | 10-series compact 90-degree corner brackets | Two per crossbar end; one leg to Yakima plate, one to extrusion side slot. |
| 8 | `M6 x 20 mm` stainless fasteners + M6 wedge-lock washers | Yakima plate to bracket. Confirm length against actual bracket/track stack. |
| 12 | `1/4-20` stainless button-head fasteners + 10-series roll-in T-nuts | Eight bracket-to-extrusion fasteners plus four TRIO-to-crossbar fasteners; final lengths after dry fit. |
| 12 | `1/4 in` wedge-lock washer pairs | Reusable vibration resistance; use witness marks after final torque. |
| 1 | Independent coated-stainless safety tether | Separate from the four TRIO mounting bolts and anchored to real roof structure/track hardware. |
| 1 lot | Tef-Gel or equivalent anti-galling/corrosion compound | Stainless-to-aluminum and stainless track hardware; do not combine anti-seize and threadlocker on the same threads. |

### Fixed-body panel and DC branch package

| Qty | Item | Specification |
| ---: | --- | --- |
| 4 | M3 stainless panel screws, washers, and prevailing-torque nuts | Length after measuring shell stack; use all four `3.2 mm` clearance holes to preserve gasket compression. |
| 2 | Structural strain-relief clamps | One beside the panel and one behind the upper Type-4/RJ45 joint; sized only after measuring actual cable/adapter OD. |
| 1 run | Dedicated red/yellow marine duplex DC cable | `12 AWG` only when converter is within roughly `6 ft` one-way of the fuse panel; use `10 AWG` for the more likely longer Desk run. Measure first. |
| 1 | `20A` ATO/ATC branch fuse | Dedicated Starlink converter slot in the existing Blue Sea panel; label both ends. If nuisance trips occur, diagnose load/voltage/heat rather than increasing the fuse above wire/device limits. |
| 2 | Correct wire-size ring terminals + 2 butt splices or lever-free permanent splices | Tinned copper, adhesive-lined heat-shrink, sized to fuse-panel studs and converter pigtails. No cigarette-lighter socket in the permanent path. |
| optional | Small 12V ball-bearing ventilation fan and finger guard | Add only if service-cubby temperatures or converter heat-soak testing justify it. Never bury the converter in insulation. |

Current observed-price required core package is about `$469` before the measured interior cable, crossbars, roof hardware, DC cable/fuse/terminations, shipping, and tax (`$478` with the optional spare Neutrik termination). Allow roughly `$620-650` for the complete installed package. Nothing in this section is marked purchased until owner confirmation or a purchase record is reconciled.

## Solar moving jumper — intentionally deferred

Do not buy, route, or pre-drill for the solar jumper yet. It remains sizing-gated because the panel model, string arrangement, cold `Voc`, array `Isc`, total moving length, and exact roof travel are not locked. Future PV stays electrically and mechanically separate from Starlink even if its anchors later share the same general area.

Required cable properties:

- two copper current-carrying conductors sized from final array current and total route voltage drop;
- jacket/conductor system explicitly rated above the final cold-array voltage;
- wet/outdoor, UV, oil, abrasion, and repeated-flex suitability;
- relaxed length and full-extension data for the actual finished coil;
- independent strain relief at both ends.

### Current candidate posture

| Item | Link / price posture | Decision |
| --- | --- | --- |
| igus `CF9-UL-60-04`, 10 AWG 4C straight chainflex | [Nassau National Cable](https://nassaunationalcable.com/products/igus-cf9-ul-60-04-10-awg-4c-stranded-bare-copper-unshielded-tpe-1000v-chainflex-cf9-ul-control-cable) — `$9.32/ft`, `15-day ARO`, shipping calculated at check | **Remove from the lead BOM.** It is affordable relative to Alpha EcoFlex, but it is straight four-conductor chain cable, not a retractile coil. It only solves flex life if a carrier/controlled loop is retained. |
| `RCC102SEO-1`, 10/2 SEOW 600 V retractile cord | [Wire & Cable Your Way](https://www.wireandcableyourway.com/retractable-cord-10-2-seow-600v) | Correct product class; current page requires a quote instead of presenting a checkout price. Hold until measured relaxed/extended requirements are known. |
| Generic Amazon 10 AWG PUR spring-cable listing | Current 2-conductor/2 m selection was about `$398` with long delivery during this check | **Reject as not reasonably priced.** |
| Trailer power coils with two 10 AWG conductors | Common on Amazon | **Reject for now.** Their low-voltage vehicle-cord rating does not establish suitability for the possible `150 V` PV circuit, and unused conductors add unnecessary bulk. |

No trustworthy, reasonably priced, checkout-ready Amazon 10 AWG two-conductor PV-capable retractile cable was found in this pass. Do not substitute a cheap low-voltage trailer coil or assume 10 AWG is final before the array is locked.

For frequent trail removal, use one connector family across the roof harness and removable coil. MC4/MC4-compatible connectors are acceptable only as matched-brand, de-energized service disconnects; do not mix brands or unplug under PV load. Exact connectors wait for the panel harness brand and array current.

## Compact PV disconnect

A rotary battery switch like the existing 12 V/48 V switches is not automatically suitable for a higher-voltage PV string. A rotary candidate must show a credible DC-PV load-break rating on the device, not merely `AC` ratings in an Amazon title.

Selection gates:

- voltage rating exceeds final cold-array `Voc`;
- current rating fits the final array/string configuration;
- two-pole switching opens both PV conductors;
- DC arc-interruption/load-break standard is visible on the device/datasheet;
- enclosure and glands fit the installed conductor OD and location;
- required string overcurrent protection remains separate unless the chosen device explicitly provides it.

| Candidate | Current link / observed price | Posture |
| --- | --- | --- |
| DIHOOL 30 A, 2-pole, 12-400 V AC/DC breaker in IP65 three-way DIN enclosure | [Amazon `B0B5QXYCTS`](https://www.amazon.com/dp/B0B5QXYCTS) — `$19.99`, in stock at check | **Practical compact budget candidate after array sizing.** Seller claims non-polarized thermal-magnetic interruption, glands, and `48-400 VDC`; current page does not establish a third-party PV certification. Inspect body markings before acceptance. |
| Generic Amazon 32 A rotary PV isolators | Approximately `$36-50` in current search | **Do not select by title alone.** Accept only if the actual unit/datasheet shows `IEC 60947-3`, `DC-PV2`, the necessary voltage/current topology, and a credible manufacturer. |
| IMO `SI32-PEL64R-2` enclosed rotary PV isolator | [US Solar Supplier](https://ussolarsupplier.com/products/imo-enclosed-dc-switch-ip66-32a-600vdc) — `$87.15`, listed available with `2026-08-11` to `2026-08-18` expected ship window at `2026-08-03` check; [FactoryMation technical listing](https://www.factorymation.com/SI32-PEL64R-2) | **Lead rotary service disconnect.** One-string, two-pole, lockable OFF, `32A`, `600VDC` UL508 listing / `DC-PV2` and IEC 60947-3 supplier claims, IP66/NEMA-class enclosure. Mount on the fixed body before the MPPT and open both PV conductors. Do not order until final cold `Voc`, array/string `Isc`, conductor OD/glands, and stringing prove fit; this is a service load-break, not string OCP. |

## Measurements needed before purchase lock

Record all dimensions in both roof-down and roof-up states:

1. actual vertical movement between the proposed fixed and moving anchors;
2. lower and upper tangent length from connector to strain-relief clamp;
3. desired retracted coil-body length and maximum allowed outward projection;
4. available connector/gland hole diameter and interior service access;
5. an existing rigid feature that actually projects farther outward than the coils, if any;
6. solar panel model/count, stringing, cold `Voc`, array/string `Isc`, and total one-way cable route;
7. actual OD of any purchased prototype cable before ordering Neutrik carriers or cable glands.

## Acceptance tests

### Starlink bench test

1. Establish a baseline with the complete factory cable.
2. Install the adapter pair and candidate coil on the bench.
3. Run the terminal at normal full service long enough to heat-soak the cable and connectors; verify no dropouts, speed instability, brownouts/reboots, connector heating, or visible arcing/carbonization.
4. Repeat with the coil relaxed and extended.
5. Preserve the complete factory cable as the recovery spare.

### Physical mockup

1. Use rope/cheap spring cable between proposed anchored points.
2. Cycle roof down, intermediate, and fully raised; the roof must never pull on a connector.
3. Confirm the down-state coil stays close to the body and does not fall below or outside the chosen profile.
4. Cycle repeatedly and inspect for coils winding together, slap, rub, pinch, and snag.
5. Prove trail removal and cap/stow workflow before drilling final holes.

### Trail-mode sequence

- Starlink: power down -> disconnect/remove coil -> cap fixed/moving RJ45 ends -> secure adapter pigtails.
- Solar: open the PV-rated disconnect -> verify current is stopped -> disconnect/remove the solar coil -> cap both ends.
