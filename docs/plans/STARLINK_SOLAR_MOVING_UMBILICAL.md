# Starlink + solar moving-roof umbilical

Status: **Starlink fixed-body pass-through/retractile and switched `12V` conversion operational; final weather/travel closeout open. Four solar panels received; one-panel physical fit plus measured layout indicates package fit. Direct bond waits on silicone/cure proof; PV retractile ordered and pending received-property/full-motion proof.**
Last current-source check: `2026-08-27`

## Decision

Complete Starlink as its own pathway. Owner report `2026-08-27`: the dedicated rugged shielded RJ45 bulkhead is installed in the fixed camper body, the removable shielded retractile Ethernet/PoE jumper works, and Standard 4 X operates from the switched dedicated `12V` conversion branch through a `20A` blade fuse. The complete OEM cable remains the direct recovery spare. Remaining closeout is labeling, cap/retention/spray inspection, loaded heat/dropout/reboot observation, full roof-motion inspection, and post-drive inspection.

The Standard 4 X hardware kit and OEM mobility mount are purchased at an owner-reported `$405` aggregate total. Current service is `$55/month`; the exact plan name was not supplied, and the owner intends to move to an unlimited plan later. Recurring service stays in `bom/bom_misc_items.csv`, not the one-time build total.

Solar remains separate from the Starlink penetration. All four purchased Renogy `175W` panels have arrived; one-panel physical test-fit plus measured layout indicates that the four-panel package fits with Starlink and MaxxAir while using nearly the whole roof. The electrical path remains one `4S1P` string on the Victron `150/45`. Direct roof bonding waits on the exact structural-silicone product, substrate/backsheet preparation, coupon/cure proof, drainage, and one-panel shakedown. The owner reports the PV retractile cord is ordered; exact SKU/vendor/rating evidence is not recorded here yet, so received conductor count/gauge, OD/gland fit, `>=150VDC`, wet/UV/cold/coiled ampacity, tangents, force, and full `28 in` roof/cab articulation remain gates.

The selected PV path is one continuous retractile cord in the front camper-to-cab gap, with its fixed-camper compression gland just above the installed Starlink entry behind the cab. The owner accepts residual branch/snatch exposure. Keep the helix external, pass only a stationary lower tail through the gland, and use structural redundant exterior/interior clamps so adhesive guides, the gland, and terminals carry no spring, wind, or branch load. Preserve three panel-to-panel series mates and only two free string-end leads into the compact two-pole transition, continuous `12 AWG` two-conductor cord, fixed load-break, and MPPT. `12 AWG` is conductor size, not circuit voltage. There is no exterior PV quick disconnect or manual roof-motion release step.

This supersedes the prior no-new-hole/existing-service-route baseline, removable-PV-coil, chain-first, guided-loose-loop, and shared-entry recommendations. The existing truck-bed service route and complete factory Starlink cable remain recovery paths, not the normal finished installation.

## Why the other two moving-section concepts lost

### Side-mounted energy chain — rejected as the default

A chain does not make the cable branch-proof. On an exposed vertical camper wall, the return bend still needs somewhere to collect when the roof closes. Without a measured recess or enclosed guide trough, the chain will project outward or bunch into a side lump. Keeping it against the wall would require another trough, retractor, or stow mechanism, increasing bulk and making trail removal harder.

An energy chain remains a contingency only if later geometry reveals a real inboard trough; there is no reason to buy one for the current exterior-wall concept.

### Loose cable/service loop in sleeve — rejected

Without an added spring reel, elastic take-up, or guided carriage, it is simply a slack cable hanging from two anchors. The sleeve supplies abrasion resistance but does not store slack. Adding the missing take-up hardware recreates a less predictable cable-carrier system.

### Meaning of `sheltered`

A route is sheltered only if an existing rigid camper feature projects outward farther than the cable and the cable stays inside that feature's contact shadow through the full roof stroke. No such location has been physically confirmed. The earlier `front guard` wording referred to an imagined fabricated pouch/deflector, not an existing Hiatus component, and is withdrawn.

No exterior cable is branch-proof. The front camper-to-cab gap is the lead PV protection envelope because it avoids the exposed camper sides, but it is not accepted as `sheltered` until a roof-down cab/bed articulation and road-vibration mockup proves positive clearance. Starlink remains removable for tight-trail mode; the continuous PV cord remains installed and requires no normal roof-motion intervention.

## Selected Starlink physical layout

```text
MOVING ROOF / REMOVABLE MOUNT
  Standard 4 X terminal in TRIO protective edge frame
    -> upper AUDEETO Gen 3 weather/retention pigtail
    -> removable 3 m stretched shielded retractile jumper
    -> NE8MXR1-B-TOP-D locking/weather-sealed cable connector

FIXED CAMPER BODY
  NE8FDX-P6-W shielded RJ45 panel bulkhead with captive cap
    -> fixed interior shielded pure-copper Cat6A patch cable
    -> lower AUDEETO Gen 3 weather/retention pigtail
    -> Gen 3 router
    -> 12V-to-57V converter primary / factory AC supply + inverter fallback
```

Put the panel bulkhead in rigid fixed-body structure below the folding/moving seam and near the Desk/router service zone. The installed bulkhead/retractile route and direct-DC conversion are owner-reported operational. Keep structural strain relief behind the upper adapter joint and at the panel so no electrical connector carries spring tension. Final acceptance still requires label, shield-shell continuity record, cap/retention/spray inspection, loaded heat/dropout/reboot observation, full roof-motion inspection, and post-drive inspection. Remove/stow or ground-deploy the dish for tight brush; the protective frame and ability to disconnect do not make the roof equipment branch-proof.

## Starlink cable, panel, and deployment topology

### Cable and panel topology

- Establish a working baseline with the complete factory Starlink cable, then remove and retain that cable as the unmodified direct recovery spare.
- Use the two-pack of passive AUDEETO Gen 3 weather/retention pigtails: one at the Standard 4 X terminal and one at Router 3. These are not protocol or voltage converters; each provides a Starlink-port-compatible shielded male plug, short pigtail, and gland-sealed standard RJ45 female joint. The router-side pigtail keeps the service joint and cable strain off the router port; direct indoor RJ45 fit remains a bench-test simplification, not a planning assumption.
- From the router pigtail, run a field-measured shielded pure-copper Cat6A patch cable to the rear of one [Neutrik `NE8FDX-P6-W`](https://www.neutrik.com/en/product/ne8fdx-p6-w) shielded feedthrough panel connector. Neutrik publishes Cat6A/10 Gbit/s, PoE Type 4 Class 8 / `100W`, `>1000` mating cycles, and IP65 both when correctly mated and when its captive cap is closed.
- Fit the lower end of the selected retractile jumper with [Neutrik `NE8MXR1-B-TOP-D`](https://www.neutrik.com/en/product/ne8mxr1-b-top-d), the retractable TOP carrier that includes the matched Cat6A RJ45 plug and wire manager. It accepts `5.5-8.0 mm` cable OD and AWG `24/7-27/7` stranded conductors, so the listed `26 AWG` coil is conductor-compatible only if its measured jacket OD is also inside that range. It intermates with `NE8FDX-P6-W`; Neutrik's published incompatibility is with `NE8FDY-C6` / `NE8FDY-C6-B`, not the selected panel connector. The panel accepts an ordinary RJ45 plug for dry-weather ground deployment, but a plain RJ45 connection is not the weather-sealed/locked normal-road interface.
- Join the jumper's upper end to the terminal adapter using the adapter's threaded weatherproof RJ45 gland.
- Do not confuse a male device pigtail with the female/female factory-cable coupler. A third AUDEETO pigtail cannot directly accept the factory cable because both ends are male. If panel-fed factory-cable deployment is wanted, use one Furnique-style Gen 3/Cat6-Cat7 inline coupler on the camper end of the factory cable plus a short shielded RJ45-to-Neutrik TOP jumper to the panel. The coupler is electrically passive; “plug and play” means it joins two male-ended cables without cutting either one.
- Put structural P-clamps/anchors behind the upper exterior joint and beside the panel; do not let the Starlink socket, RJ45 contacts, or panel connector carry coil tension.
- Keep the Gen 3 router and selected `10-36V` input / `57V 4.5A` output converter in an accessible ventilated Desk/service cubby. Feed the converter from a dedicated fused `12V` branch; retain the factory AC supply at a fixed GFCI-protected receptacle as the inverter fallback. Do not power Starlink through the plug-in desktop pop-up module.

### Roof / ground mode

- **Roof mode:** protective-framed dish stays on the selected magnetic/VHB-disc or crossbar attachment package; retractile jumper stays connected at the dish and locks into the panel connector. Power down, disconnect/cap at the panel and upper pigtail, release the independent tether, then remove the complete dish/frame for tight brush.
- **Ground recovery mode — preferred:** remove the dish/frame, remove the upper pigtail from the terminal, and run the complete OEM Starlink cable directly from terminal to router through the existing service route. This bypasses every third-party data interface and needs no additional coupler.
- **Ground mode through the panel — optional convenience:** plug the factory cable into the terminal, connect its camper end to one Gen 3/Cat6-Cat7 female/female inline coupler, then use a short shielded male-ended jumper to the Neutrik panel. Fit a second `NE8MXR1-B-TOP-D` on the panel end if this mode must remain sealed in weather. Carrying this small adapter jumper is cleaner than buying a third device pigtail.
- Preserve the complete OEM cable for direct router-to-terminal recovery if any adapter, bulkhead, reterminated plug, or retractile jumper fails.

## Roof mount and branch-protection direction

Current lead: [TRIO Gen 3 Standard Speedmount](https://www.trioflatmount.com/products/gen3speedmount), **white**, purchased `2026-08-06` for `$285` including the `75 mm` stainless through-bolting hardware option. It is explicitly compatible with Standard 4, wraps/protects all four dish edges, is `1.85 in` high, is sold for permanent/temporary highway use, and leaves the factory kickstand usable.

Purchased removal-first attachment package is TRIO's own `$80` set of four rubber-coated magnets plus VHB-backed steel mounting discs. TRIO explicitly lists this semi-permanent combination for fiberglass roofs. It claims `60 lb` nominal holding force per magnet and high-speed mount testing, while also making final securement the user's responsibility. Accept it only if the actual gelcoat is sound, smooth, nonporous, flat at all four feet, and does not let the frame rock. Install at TRIO's stated `70-100 F` ideal temperature, use its surface prep, allow about `72 hours` full cure before highway/weather load, perform a low-speed test/reinspection, and add an independent coated-stainless tether to an existing Yakima-track hardpoint. The tether remains mandatory for brush and adhesive/gelcoat failure even though the mount is vendor-supported. The purchased `75 mm` stainless frame hardware preserves the hard-mount-to-extrusion option.

Mechanical fallback/current mockup is now a stock-driven `1010`/angle-aluminum package, not two full-height `1020` crossbars. Likely geometry is short/leftover `1010` running directly over and parallel to the Yakima tracks, with two continuous transverse members made from suitably stiff angle or other continuous stock; direct track-to-track crossmembers may omit the longitudinal extrusion if future modularity is not worth the extra joints. Do not use a long flat bar laid flat as the only wide-span crossmember unless a physical bending/twist test proves it; angle with a vertical leg is materially stiffer. Keep the main transverse members continuous and confine patchwork/splices to low-moment adapter or longitudinal sections.

The selected `M6 x 35 mm`, `20 x 20 x 4 mm` square-head track bolts are a plausible length for a **bare `25.4 mm`-high 1010 through-stack**: a nominal `1.6 mm` washer plus `6 mm` M6 nut leaves about `2 mm` / two threads of projection. They become marginal if angle, spacers, thick washers, or an additional plate share that same bolt. `M6 x 40 mm` would provide more tolerance, but an exact Yakima-compatible square-head variant is not readily sourced; `M6 x 65 mm` is unnecessarily long for the revised one-inch stack and remains relevant only to a roughly two-inch through-stack. Dry-fit before drilling and avoid crushing unsupported extrusion walls with a crush sleeve, internal spacer, or a load path through supported profile webs.

Preferred known-fit alternative is eight genuine Yakima [`8810074` Anchor Plate A](https://yakima.com/products/anchor-plate-a) threaded plates plus separately selected `M6 x 1.0` bolts. Yakima lists eight plates per kit; published third-party measurements are `3/4 x 7/8 in`, and the companion LandingPad hardware bag uses `M6 x 20 mm` bolts. The finite track floor makes bolt depth an acceptance item: with the intended bracket/member clamped in place, select or trim each bolt so its tip ends flush with or slightly shy of the plate underside while retaining nearly full plate-thread engagement. Use standard `M6` length steps and one or two measured hardened shim washers under the head for fine correction, or cut/chamfer a longer bolt; do not solve a large mismatch with a loose washer tower and never let a bottomed bolt imitate clamp torque. A representative plate/stack should be assembled outside the track first, then installed with marker or soft-clay evidence proving the tip does not contact the track floor. Prefer the known steel plates over hand-tapped thin aluminum; if custom plates are unavoidable, copy the proven plate envelope in adequate stainless and verify thread engagement, track clearance, edge distance, and pullout resistance.

The protective frame improves side/edge survival but does not make the terminal branch-proof. For tight, brushy routes, disconnect the cable and tether and stow/ground-deploy the dish. A thick limb contacting the face or using the frame as a lever is still a no-go for roof carriage.

## Solar geometry audit and purchased-array posture

The measured roof baseline is now `138 x 63 in` inside the Yakima tracks, not the older `134 x 62 in` model. The MaxxAir is laterally centered: current conservative keepout is `X=29...63`, `Y=23...40`; exact rear roof-flange and open-lid dimensions remain release measurements. The track top is `0.625 in` above fiberglass.

The current product/topology posture is:

- `4x Renogy 175W flexible monocrystalline = 700W`, purchased `2026-08-12` and owner-reported received by `2026-08-27`;
- one `4S1P` string to the purchased SmartSolar `150/45`, pending exact label record and hot commissioning;
- one-panel physical test-fit plus measured layout indicates that the complete roof package can coexist with Starlink and MaxxAir while using nearly the whole roof; full `1:1` templates still control exact coordinates, track transitions, leads, and service access;
- direct roof attachment using the exact controlling structural-silicone product/preparation/cure; no carrier/cassette/rack unless the owner reopens it;
- Starlink/TRIO remains removable for tight brush and needs independent positive retention per its owner doc.

Using Renogy's current official G2 data pending received-label confirmation, `4S` is `78.0V Vmp`, `95.6V Voc`, `8.98A Imp`, and `9.50A Isc`. The published `-0.31%/C` Voc coefficient gives `114.86V` nominal cold Voc at `-40C`, comfortably under Victron's limits. Hot start is the concern: an indirect published-coefficient estimate reaches about `61.87V` at `70C`, essentially the current `56.8V + 5V` startup threshold before route drop. One string has no peer-string backfeed, so no individual string fuse is presently planned; received labels, conductors/connectors, disconnect rating, route drop, and applicable PV rules remain the as-built gate.

Direct bonding waits on roof wash/decontamination, exact substrate/backsheet preparation, representative coupon, drainage, cure, and a staged one-panel acceptance: static/heat/water/roof-cycle proof; temporary independent track-anchored test restraint; private/closed-course low-speed test with stops; then deliberate progressive road testing with staged inspections. Routine highway use and remaining panel bonds wait until that sequence passes. Adhesive zip-tie mounts can guide conductors but cannot be the sole exterior restraint. Do not infer that panel receipt or good physical fit approves the adhesive stack, moving cord, or controller under worst-case hot conditions.

Canonical geometry, weight budget, electrical math, candidate coordinates, mounting constraints, and release checklist: [`SOLAR_configuration_matrix.md`](../studies/SOLAR_configuration_matrix.md).

### Current-source anchors

- [Renogy support page — 175W flexible panel](https://www.renogy.com/pages/175-watt-monocrystalline-solar-flexible-panels-rng-175db-h-html)
- [Renogy official RNG-175DB-H-G2 datasheet](https://cdn.shopify.com/s/files/1/0631/0137/0483/files/RNG-175DB-H-G2_20Datasheet.pdf?v=1752029087)
- [Victron SmartSolar `150/45` datasheet](https://www.victronenergy.com/upload/documents/Datasheet-SmartSolar-charge-controller-MPPT-150-35-%26-150-45-EN.pdf)
- [MAXXFAN Deluxe installation manual](https://library.maxxair.com/wp-content/uploads/2023/03/11e90001k_maxxfan-deluxe-install-11-2017.pdf)
- [TRIO VHB-backed magnet pads](https://www.trioflatmount.com/products/vhb-backed-magnet-mount-pads)

### Current-source shortlist

| Item | Current link / observed price | Posture |
| --- | --- | --- |
| `2x` AUDEETO 2 ft Gen 3/RJ45 weather-retention pigtails | [Amazon `B0DL358L3G`](https://www.amazon.com/dp/B0DL358L3G) — `$19.99` | **Purchased 2026-08-06; acceptance testing pending.** Two-pack provides one passive pigtail at the terminal and one at Router 3; seller claims `26 AWG`, shielding, `1000 Mbps`, and IP67 when correctly gland-mated/capped. Limited review history means continuity/shield/heat/retention testing remains mandatory. |
| Furnique Gen 3 / Cat6-Cat7 inline factory-cable coupler | [Amazon `B0GQZ5SNWR`](https://www.amazon.com/dp/B0GQZ5SNWR) — `$12.99` | **Purchased 2026-08-06 for optional panel-ground mode; acceptance testing pending.** Female/female passive coupler accepts the camper end of the unmodified factory cable and the purchased `1 ft` shielded jumper to the panel. It cannot plug into the terminal/router by itself; its IP68 claim is seller-supplied and must be spray/retention tested. |
| ZBLZGP 3 m stretched Cat6A retractile cable | [Amazon `B0H286KLWZ`](https://www.amazon.com/dp/B0H286KLWZ) — `$35.00` | **Terminated; conductor continuity passed 2026-08-12.** The green coil was an extremely tight fit in the Neutrik plug and required lubricant/insertion force. DMM continuity passed on every conductor at both finished ends. Shield-shell continuity, full-stroke strain relief, loaded Starlink heat/dropout/reboot, and spray/retention tests remain open. |
| L-com `TRD815SZ-CH-1-6F` industrial coil | [L-com product page](https://www.l-com.com/category-5e-ethernet-coil-cord-rj45-rj45-180d-tangents-f-utp-foil-shielded-26awg-high-flex-industrial-zero-halogen-tpu-teal-1-to-6f) | Higher-confidence industrial construction and useful `1-6 ft` geometry, but current retail price/stock could not be verified without vendor challenge and prior pricing was poor. Do not buy unless the Amazon prototype fails or a distributor price is acceptable. |
| Fixed-body RJ45 bulkhead | [Neutrik `NE8FDX-P6-W`](https://www.neutrik.com/en/product/ne8fdx-p6-w) / [Mouser](https://www.mouser.com/ProductDetail/Neutrik/NE8FDX-P6-W) | **Installed and owner-reported working by 2026-08-27.** Shielded Cat6A feedthrough, PoE Type 4 Class 8 / `100W`, `>1000` cycles, rugged latch, captive cap, and IP65 correctly mated/capped. Final backing/fastener, cap/retention/spray, rear bend/strain-relief, roof-motion, and post-drive inspection remain. |
| Roof-jumper cable connector | [Neutrik `NE8MXR1-B-TOP-D`](https://www.neutrik.com/en/product/ne8mxr1-b-top-d) / [Mouser](https://www.mouser.com/ProductDetail/Neutrik/NE8MXR1-B-TOP-D) | **Two received and both cable assemblies completed by 2026-08-12.** `$8.93` each / `$17.86` extended. One terminates the roof coil; the second terminates the short optional factory-cable panel jumper. The green-coil conductors passed DMM continuity; repeat the conductor check on the short jumper, then complete shield and loaded system/physical tests. |
| Protective removable dish frame and fiberglass attachment | [TRIO Gen 3 Standard Speedmount](https://www.trioflatmount.com/products/gen3speedmount) | **Purchased 2026-08-06; pending fulfillment.** White Speedmount with `75 mm` stainless through-bolting hardware, `$285`; four rubber-coated magnets, `$40`; VHB-backed magnet mounting discs, `$40`; `$365` total with free shipping. Require full flat magnet/disc contact, proper prep, about 72 h cure, low-speed reinspection, and an independent Yakima-track tether. Purchased through-hardware preserves the extrusion hard-mount option. |
| Gen 3 router DC converter | [Amazon `B0DLZWHPKJ`](https://www.amazon.com/dp/B0DLZWHPKJ) — `$38.99` | **Installed and owner-reported operational by 2026-08-27** on a switched dedicated `12V` branch with `20A` blade fuse; factory AC remains fallback. Final label, mounting/ventilation, loaded heat/reboot, input-drop, and post-drive checks remain. |
| Lower exterior inline RJ45 joint | [trueCABLE Cat6A shielded waterproof coupler](https://www.truecable.com/products/cat6a-waterproof-couplers-shielded) / [Amazon `B0949S87V7`](https://www.amazon.com/dp/B0949S87V7) | **Fallback only.** No longer needed if the one-panel Neutrik interface and compatible cable carrier are accepted. |
| One-cable fixed-body entry | [Seaview retro-fit cable gland, Amazon `B077PQ4FGG`](https://www.amazon.com/dp/B077PQ4FGG) | **Withdrawn from the normal path.** The selected interface is a panel connector, not a through-cable gland. |
| Prior shared-entry candidate | [Scanstrut `DS-H-MULTI-BLK`, Amazon `B0CSTC4D3C`](https://www.amazon.com/dp/B0CSTC4D3C) — `$53.34` at prior check | **Withdrawn.** It is a horizontal cable-entry/deck-seal product, not the desired straight panel quick-disconnect. |
| Straight sidewall candidate | [Scanstrut `TBH-4`](https://www.scanstrut.com/marine/cable-seal/bulkhead/tbh-4) | **Withdrawn from this route.** It is a cable seal, not a detachable panel connector, and its larger multi-cable cut is not justified by deferred solar. |

Orders placed `2026-08-06`: Mouser one `NE8FDX-P6-W` plus two `NE8MXR1-B-TOP-D`, `$46.31` item subtotal / `$54.80` checkout total; TRIO white Speedmount, `75 mm` through-hardware, magnets, and VHB-backed discs, `$365` with free shipping; Amazon pigtail pair, Furnique coupler, ZBLZGP coil, 10 ft and 1 ft Cable Matters patch cables, EAZUSE converter, and VCELINK crimper, `$141.44` combined item subtotal. By `2026-08-27`, the fixed-body pass-through, retractile roof jumper, and switched `12V` converter branch are owner-reported operational. Remaining acceptance is label/backing/strain-relief inspection, shield-shell record, cap/retention/spray, loaded converter/cable heat and reboot stability, full roof-motion inspection, roof-mount retention, and post-drive inspection.

## Why the one-panel Neutrik path now wins

The prior rejection applied to a two-panel layout, which added unnecessary chassis connectors and RJ45 interfaces. The selected layout uses only one fixed-body `NE8FDX-P6-W`: it provides the solid panel quick-disconnect Dane asked for, is explicitly rated for `100W` 802.3bt Type 4, protects the normal roof connection when correctly mated, caps cleanly when disconnected, and still accepts an ordinary RJ45 ground-deployment cord. The upper dish end continues to use the AUDEETO pigtail's weatherproof RJ45 gland, so a second panel connector adds no value.

- [Neutrik `NE8FDX-P6-W`](https://www.neutrik.com/en/product/ne8fdx-p6-w) is female RJ45 on the rear, so the panel part itself needs no punch-down/crimp tool. The published rear panel cut uses one `>=24 mm` center opening plus four `>=3.2 mm` M3 clearance holes on `19.0 +/- 0.1 mm` horizontal by `24.0 +/- 0.1 mm` vertical centers; it is not the common two-screw D-series cutout.
- `NE8MX-B-TOP` is the correct outdoor choice over `NE8MX-B-1`, but it is only a carrier and does not include an RJ45 plug. The final buy-list preference is the newer `NE8MXR1-B-TOP-D`, which adds the matched Cat6A plug/wire manager and a retractable shell while keeping IP65 in the correctly mated TOP connection.
- [Neutrik `NE8MX6-T`](https://www.neutrik.com/en/product/ne8mx6-t) is the Cat6A/PoE++ self-termination alternative, but its published `7-9.5 mm` cable-OD range must match the selected coil.
- [Neutrik `NE8MX-B`](https://www.neutrik.com/en/product/ne8mx-b) accepts a preassembled RJ45 cable without retermination, but it is not the exterior `TOP` weather-sealed solution.

**Current penetration state:** the Starlink bulkhead is installed and the route works. Inspect all four fasteners/gasket compression, sealed laminate/core edge, exterior cap/latch access, rear connector/bend and strain relief, interior service access, drip behavior, and the complete roof stroke; then repeat after spray/load and first drive. Keep this cutout geometry as as-built reference rather than treating the prior hold as still active.

## Full Starlink procurement and acceptance list

### Buy-now bench/mount package

| Qty | Item | Current source / allowance | Notes |
| ---: | --- | --- | --- |
| 1 | TRIO Gen 3 Standard Speedmount, white, with `75 mm` stainless through-bolting hardware | **Purchased from TRIO 2026-08-06; pending** — `$285` | Standard 4/4X frame; preserve kickstand. Through-hardware supports optional frame-to-extrusion mounting. |
| 1 pair | AUDEETO 2 ft Gen 3/RJ45 weather-retention pigtails | **Purchased from Amazon 2026-08-06** — `$19.99`, ASIN `B0DL358L3G` | One passive pigtail at terminal, one at Router 3. Budget prototype replacing the `$58.99` STARGEAR pair; bench-test before install. |
| optional 1 | Furnique Gen 3/Cat6-Cat7 female/female inline coupler | **Purchased from Amazon 2026-08-06** — `$12.99`, ASIN `B0GQZ5SNWR` | Factory cable -> purchased 1 ft shielded jumper -> Neutrik panel ground mode. Direct OEM cable recovery remains the lowest-interface fallback. |
| 1 | ZBLZGP 3 m / 9.8 ft stretched retractile Cat6A cable | **Purchased from Amazon 2026-08-06** — `$35.00`, ASIN `B0H286KLWZ` | Budget prototype; `26 AWG` pure-copper/PUR/dual-shield seller claims. Measure OD before cutting. |
| 1 | Neutrik `NE8FDX-P6-W` panel feedthrough | **Installed and owner-reported working by 2026-08-27** — purchased from Mouser 2026-08-06 at `$28.45` | Fixed-body female/female feedthrough with captive cap. Final backing/fastener, gasket, core-edge seal, rear bend/strain relief, spray/load, roof-motion, and post-drive checks remain. |
| 2 | Neutrik `NE8MXR1-B-TOP-D` | **Received and both cable assemblies completed** — purchased from Mouser 2026-08-06 at `$8.93` each / `$17.86` extended | One on roof coil and one on the short factory-cable panel jumper; all green-coil conductors passed owner DMM continuity on `2026-08-12`, while the short jumper still needs the same check. |
| 1 | VCELINK Cat7/6A shielded RJ45 crimper | **Purchased from Amazon 2026-08-06** — `$17.99`, ASIN `B08LPMXM3Q` | Budget tool with standard/non-pass-through and shield-clip capability. It is not on Neutrik's approved-tool list; inspect contact depth and shield crimp, continuity-test, and have an AV/network shop reterminate if it does not make a clean full crimp. |
| 1 | Basic RJ45 continuity tester | **No longer required after owner established a workable DMM method 2026-08-12.** | Green-coil conductors passed; repeat the DMM check on the short jumper. A budget tester would not certify Cat6A or replace shield-shell and loaded Starlink tests. |
| 1 | EAZUSE Gen 3 `12V` converter | **Installed and owner-reported working by 2026-08-27** — purchased from Amazon 2026-08-06 at `$38.99`, ASIN `B0DLZWHPKJ` | Switched dedicated `12V` branch with `20A` blade fuse; factory Starlink AC supply remains fallback. Verify label, ventilation/noncombustible mount, loaded input drop/heat/reboot behavior, and post-drive security. |
| 2 | Interior shielded Cat6A pure-copper patch cables | **Purchased from Amazon 2026-08-06** — Cable Matters 10 ft `$9.49` (`B00HEM5MZU`) plus 1 ft `$6.99` (`B0CVR26LWZ`) | Use the field-fit 10 ft run behind the panel; reserve the 1 ft lead for the purchased factory-cable coupler/panel jumper or bench work. Verify shield continuity, length, bend radius, and strain relief. |

### Removal-first fiberglass attachment package — purchased; installation remains roof-contact-gated

| Qty | Item | Specification / allowance |
| ---: | --- | --- |
| 1 set | TRIO rubber-coated magnets plus VHB-backed steel mounting discs | **Purchased 2026-08-06** — `$40` magnets plus `$40` discs. TRIO states four `60 lb` nominal magnets; verify received VHB/disc construction and instructions. |
| 1 | Independent coated-stainless safety tether | Anchor to real Yakima-track hardware, not another adhesive point. Release only after cable disconnection. |
| 1 | Surface/contact acceptance pass | Roof must be sound, smooth, nonporous, flat at all four feet, and free of rocking. Prep per TRIO, install at its stated `70-100 F` ideal range, cure about `72 h`, then low-speed test and re-inspect before highway use. |

### Roof-track/member package — `1010`/angle-aluminum mechanical candidate

| Qty | Item | Specification / allowance |
| ---: | --- | --- |
| 8 | Selected stainless square-head track T-bolts **or** Yakima `8810074` Anchor Plate A set | Current candidate is `M6 x 35 mm` with `20 x 20 x 4 mm` head. It is plausible for bare `1010`; end-feed and prove head/corner clearance. Prefer Anchor Plate A plus field-selected `M6 x 1.0` bolts when known Yakima fit and easy length changes matter more than bottom-up through-bolting. |
| 2 | Continuous transverse crossmembers | Prefer continuous angle aluminum with a vertical leg or another stiff section. Flat bar laid flat is an adapter/foot, not the default long-span beam. Direct track-to-track mounting is the simplest/lower-joint path; longitudinal `1010` over the tracks preserves modularity. |
| as needed | Leftover `1010` longitudinal rails/adapters | Patchwork is acceptable only with a clear load path. Keep main crossmembers continuous, stagger/brace any joints, and do not make several small brackets carry aerodynamic uplift in series. |
| 8 | M6 washers plus prevailing-torque nuts, or M6 bolts for threaded anchor plates | For bare `1010`, `35 mm` track studs leave about `2 mm` after a nominal washer/nut stack. Recalculate if another member is stacked at the same hole. Use bearing spread/crush control and corrosion isolation; no track-side L-bracket is inherently required. |
| 1 set | TRIO `75 mm` stainless through-bolting hardware | **Purchased with the Speedmount.** Use for frame-to-extrusion attachment only after confirming supplied diameter, four-corner hole stack, washers/nuts, and crossbar geometry. This does not replace the separate square-head track T-bolts that attach extrusion to the roof rails. |
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

Current documented purchased/ordered Starlink hardware is `$957.75` on the BOM basis: `$405` for the Standard 4 X kit plus OEM mobility mount, `$365` for the TRIO frame and magnet/disc package, `$46.31` Mouser item subtotal, and `$141.44` of Amazon interface/DC/tool components. The Mouser checkout total also carried `$8.49` of unallocated shipping/tax that is excluded from component rows. The separate `$9.99` tester has been retired. The working route still needs the final label/backing/strain-relief, shield, spray/retention, loaded heat/reboot, roof-mount/full-motion, and post-drive checks.

## Solar moving path — continuous front-gap retractile

### Selected architecture

```text
MOVING ROOF
  4x Renogy 175W in one 4S string
    -> three direct panel-to-panel series links
    -> only two free string-end leads (PV+ and PV-)
    -> compact two-polarity roof transition box
    -> upper structural jacket clamp
    -> factory straight upper tangent
    -> vertical retractile helix in camper-to-cab gap

FIXED CAMPER SHELL
  factory straight lower tangent
    -> lower structural jacket clamp
    -> broad supported bend + drip loop
    -> exterior clamp
    -> IP68 compression gland through fixed camper shell
    -> interior clamp
    -> accessible two-splice transition to stationary 12/2
    -> stationary interior 12/2 run
    -> two-pole PV load-break
    -> Victron SmartSolar 150/45
```

The concept is **continuous across the shell**. Only a smooth, full-round, stationary factory straight tail passes through the gland. The helix, first/last coil throat, splice, stripped jacket, or any sliding section must never enter or work inside the gland. The gland seals; independent clamps on real camper structure carry spring force and road load. Nothing attaches to or mechanically bridges into the truck cab.

Orient the coil vertically with its axis parallel to roof travel. Prefer axial/drop tangents at both ends. Keep the complete helix outside in a smooth, drained open channel or guard attached only to camper structure; do not put the coil in a tight tube. The lower tail forms a drip loop before approaching the gland straight and normal to the wall. A roof-side matched solar-connector service connection may remain, but only as a matched-brand, de-energized service connector—not a normal roof-motion step or a load-break.

The owner's internal-splice concept is valid and preferred over buying a retractile with a long stationary interior tail. After the cord is independently clamped inside the shell, make exactly two polarity-marked splices to fixed `12/2` in an accessible protected location. [Pacer `12/2` duplex boat cable](https://www.pacergroup.net/duplex-cable-12-awg/) is a relevant stationary-run class because the manufacturer specifies fine-stranded tinned copper and `600V`; the actual purchased cable still needs its exact wet/temperature markings checked. [3M `MH10BCX`](https://www.3mcanada.ca/3M/en_CA/p/d/v000076893/) is a relevant `12-10 AWG`, adhesive-lined, water/salt-sealed butt-splice class with a published `600V` building-wire rating. Release any butt splice only after confirming it accepts the retractile's exact extra-fine stranding, using the specified ratcheting crimper, completing a pull test, and supporting both cables so the splice carries no mechanical load. Keep this transition accessible rather than burying it in the wall.

### Cable release specification

- Preferred moving conductor: `12 AWG x 2`, finely stranded copper, with `12/3` acceptable only if the third conductor is individually capped at both ends and no green/green-yellow conductor is used for PV current.
- Require written continuous suitability for at least `150VDC`, `>=14.8A` at worst parked/retracted coiling and ambient, repeated flexing, wet/outdoor/UV/ozone/oil/abrasion service, and the selected cold-temperature floor.
- Require a dimensioned drawing: cable/coil OD tolerance, retracted body, safe working extension, upper/lower tangent direction and length, transition throats, bend radius, and force-versus-extension curve.
- Treat **overall clamp-center span**, **active helix length**, and **straight tangent lengths** as separate dimensions. Current owner geometry is approximately `24 in` overall roof-down plus `28 in` pop-up travel, or about `52 in` roof-up before any small route-angle effect. Direct measurements at all roof positions still control.
- The earlier `3-7 ft` span and `8.5-9 ft` cord target were overstated. For an idealized `5:1` active helix inside a `24 in` down / `52 in` up envelope, the prior `80%` working-extension screen needs only about `9.3 in` of natural helix, `14.7 in` of combined tangents, and `61.3 in` rated overall reach. A literal `60 in` maximum is close but leaves only `8 in` above the estimated roof-up span; prefer roughly `60-66 in` rated overall, or up to `72 in` if the natural roof-down length still fits near `24 in` and spring force remains low. Do not buy a `2-10 ft` cord by inertia: excess **retracted** length creates slack; extra maximum reach on a correctly self-retracting short coil does not.
- The interior `12/2` splice shortens only the stationary retractile tail. It does not reduce the moving clamp-center range the helix must accommodate.
- `12 AWG` is electrically sufficient unless final route/derating disproves it. At `9.5A`, `78V`, and a conservative `20 ft` one-way route, screened drop is about `0.733V / 0.94%`; `10 AWG` would reduce this to `0.460V / 0.59%` but typically adds moving mass, coil bulk, and spring load.

### Pre-order market screen (reference)

The owner reports that a PV retractile cord is now ordered, but the exact product identity and purchase evidence are not yet recorded in this public plan. Keep this table as comparison history. On receipt, identify the actual cord and test it against the release specification rather than assuming the earlier lead was the item ordered.

| Candidate | Verified posture | Decision |
| --- | --- | --- |
| [Coil Cable Specialist `1203PM06-5T`](https://www.coilcablespecialist.com/products/12-awg-3-conductor-ul62-retractable-cord-1203pm06), `12/3`, `600V`, `25A`, black FR polyurethane | Exact `1 ft -> 5 ft / Tangent` variant was available at `$63.25` on `2026-08-25`; `0.525 +/-0.010 in` cable OD and `1.760 +/-0.250 in` coil OD. The vendor's direction diagram shows tangent leads parallel to the coil axis, matching a vertical upper/lower anchor layout. The page has no drawing and does not define whether lengths include the straight leads. | **Primary stock near-fit, on written-data hold.** Its class is much closer than `2-10 ft`, but require a dimensioned overall/tangent drawing, `>=150VDC`, wet/UV/cold/coiled-ampacity, working-extension, cycle, and force confirmation before purchase release. Use black/white for PV and individually cap green at both ends. Its `13.08-13.59 mm` tolerance band requires the M25 `53112035` path, not the `7-13 mm` M20 gland. |
| [Coil Cable Specialist `1203PU06-5T`](https://www.coilcablespecialist.com/products/12-awg-3-conductor-ul-retractable-black-cord-1203pu06), `12/3`, `600V`, `25A`, black FR polyurethane | Exact `1 ft -> 5 ft / Tangent` variant was available at `$61.25` on `2026-08-25`; `0.400 +/-0.010 in` cable OD and `1.500 +/-0.250 in` coil OD. Length/tangent semantics remain unpublished. | **Smaller stock sample/fallback.** Prefer only if its exact wet/UV/cold construction and DC/force data are confirmed; its `~10.2 mm` straight jacket fits the M20 gland class more comfortably than the `1203PM06`. |
| [TPC Wire `60241` Trex-Onics High-Flex Ultra-Coil](https://www.tpcwire.com/products/wire-cable/control-cables-instrumentation/trex-onics-high-flex-ultra-coil-retractiles) | Manufacturer data: security-yellow `12/4`, tinned `168x34` stranding, `600V`, `30A`, `-40C`, sunlight/oil resistant, continuous-cycle polyurethane/TPE; `0.417 in` cable OD and `1.8 in` coil OD. Its `1 ft -> 5 ft` **active helix** has two additional `12 in` leads, making it `3-7 ft` overall. | **Durability/length-semantics reference only.** Its natural `3 ft` overall assembly is now too long for the estimated `2 ft` roof-down span unless the manufacturer approves shorter tails; stock yellow `12/4` is also needlessly bulky electrically. |
| [Nassau `123SOOW1TO5`](https://nassaunationalcable.com/products/12-3-soow-ul-csa-retractable-coil-cord-1ft-retracted-5ft-extended), black `12/3 SOOW` | `$85.22` and in stock at check; `600V`, `25/20A`, `-40C` to `90C`, sunlight/oil/moisture/abrasion resistant; `0.63 in` cable OD and `2.31 in` coil OD. Tangents and total endpoint length are unpublished. | **Documented budget stock fallback, but bulky.** Require a drawing, DC statement, force/cycle data, and proof that the `1-5 ft` length excludes adequate tangents. |
| [Nassau `102SOOW1TO5`](https://nassaunationalcable.com/products/10-2-soow-ul-csa-retractable-coil-cord-1ft-retracted-5ft-extended), `10/2 SOOW` | `$110.50` and in stock at check; exact two conductors, `600V`, `30A`, `-50C` to `105C`, `0.617 in` cable OD. Tangent length, coil OD, force, and total endpoint length are unpublished. | **Exact conductor-count fallback, not preferred.** Its larger/stiffer 10 AWG package buys negligible electrical benefit and forces a larger gland. |
| [Philatron custom coil form](https://philatron.com/contact/custom-coiled-cable-form.php) | RFQ supports exact working/retracted length, maximum coil diameter, axial leads and lengths, `12 AWG x 2`, tinned copper, outdoor and temperature requirements, plus soft-memory/low-pull-force selection. Public MOQ, price, and lead time are not stated. | **Best exact-fit RFQ path.** Request black `12/2`, about `24 in` maximum overall relaxed and `60-66 in` approved working reach, low spring force, explicit `>=150VDC`, wet/UV/-40C/continuous-cycle approval, and a signed drawing/force curve. |
| [Autac custom retractile](https://autacusa.com/build-your-cord/) | Configurator supports conductor count/material, `24 in` or custom retracted length, `5x` calculated extension, coil OD, and independent axial/radial A/B tangents. `12 AWG` must be entered as `Other`; price, MOQ, manufacturing lead time, and exact environmental/DC approval are not public. | **Second exact-fit RFQ path.** Use the same `24 in` overall relaxed / `60-66 in` working specification and require the vendor to distinguish active helix from total assembly. |
| Amazon Iron Forge `12/3` (`B0D1DR28HH`) | `$38.99` at the `2026-08-25` check and unusually close `2.5 ft` unstretched / `5 ft` fully stretched geometry, but the finished assembly is only `125V`, `15A`, has a molded plug, and has no DC rating. | **Reject.** Only about `10V` above the current `114.86V` cold-Voc screen and no defensible DC/PV evidence. |
| Trailer/liftgate coils and generic Amazon spring cords | Usually `12/24V` use or omit voltage, wet/UV, geometry, and dynamic-duty evidence. | **Reject.** Gauge alone does not qualify a cord for this PV source circuit. |

The purchase decision has been made outside the recorded evidence in this plan. Before using the ordered cord, identify its exact part/drawing and prove that total relaxed length fits the roof-down gap, approved working reach clears roof-up with reserve, and the DC/environmental/ampacity/force requirements pass. If it fails, return to the short `1-5 ft` stock class or Philatron/Autac exact-fit RFQ rather than accepting a long or poorly rated coil.

### Four-panel junction and roof transition

There is no electrical `4-to-1` junction in the selected `4S1P` topology. Make three one-to-one series connections between adjacent panels; the two unmatched ends are the entire array output. A four-input solar branch connector is parallel hardware: it would turn the array into `4P`, leaving only about `19.5V Vmp` while raising array current toward `38A`, which is unsuitable for charging the `48V` bank through the `150/45`.

The useful compact hardware is instead a **two-polarity transition box**:

```text
P1 --series-- P2 --series-- P3 --series-- P4
free PV- end ---------------------------------\
                                                  compact transition box -> one jacketed retractile
free PV+ end ---------------------------------/
```

- Use direct received-panel connectors for the three series links wherever they reach. Add only exact manufacturer-approved male-to-female extensions where the physical layout requires them; do not cross-mate lookalike solar-connector brands.
- Preserve the panel leads. After inspecting the received connector manufacturer/markings, one matching extension cable can be cut into complementary male and female pigtails for the two string ends if its length and polarity work.
- [Bud `PN-1322`](https://www.budind.com/product/nema-ip-rated-boxes/pn-series-nema-box/ip65-nema-4x-box-pn-1322/) is a current compact box screen: UV-stabilized polycarbonate, UL 508, NEMA 4/4X, IP65/IP66, about `4.53 x 2.56 x 2.17 in` outside. It gets two OD-matched small glands for the separate PV pigtails and one gland for the intact retractile jacket. Verify entry spacing, bend radius, and actual splice volume before drilling it.
- Inside the box, make exactly two polarity-separated, strain-free transitions. Lead method is a manufacturer-approved crimp splice compatible with both the PV pigtail and the retractile's extra-fine stranding; two secured [WAGO `221-2401`](https://www.wago.com/us/wire-splicing-connectors/inline-splicing-connector-with-lever/p/221-2401) `20A/600V` inline connectors are the accessible fallback when the exact conductors are within their approval range. The box—not a bare connector—provides weather protection.
- Independently clamp all three cables. Neither glands nor splices carry roof-motion load. No combiner, rooftop string-fuse box, or four-way branch is presently needed for one series string.

### Pre-order fixed-shell gland screen (reference)

The owner plans a compact compression-gland penetration above the installed Starlink entry and has described the expected class as PG9. Do not lock PG9, M20, or M25 from that expectation: the exact ordered cord identity/OD is not yet recorded, and the received straight tail plus wall stack control gland size. The candidates below remain pre-order reference only.

- **Lead for a compact `~10-11 mm` retractile tail:** [LAPP SKINTOP `MS-M-XL` M20, `53112025`](https://www.lapp.com/en_US/us/skintop-ms-m-xl/skintop-msr-m-xl/p/53112025), plus M20 brass locknut `52103020`. Manufacturer data specify `7-13 mm` cable range, `12 mm` long connection thread, nickel-plated brass, included body O-ring, IP68 at `10 bar`, IP69, NEMA Types `1/4X/6/12`, fixed `-40C` to `100C`, and documented strain relief. It fits the `0.400-0.417 in` CCS/TPC cord class with useful tolerance. Electrically isolate and bed the brass hardware where it meets the aluminum shell/backer.
- **If the laminated wall stack defeats the LAPP thread:** PFLITSCH blueglobe `bg 820ms` provides a `15 mm` long M20 thread and `9-14 mm` furnished sealing range; procurement and exact approval evidence are less straightforward in the US, so obtain the exact SKU/datasheet before cutting.
- **Nonmetal fallback:** black Heyco-Tite `M4340` includes a nylon locknut and panel sealing ring, has a `10.4 mm` M20 thread and `4.3-11.4 mm` IP68 range, and avoids metal/backer galvanic concerns. Confirm the received cord remains below `11.4 mm` and obtain Heyco's exact UL cable range if that listing is a release gate.
- **If a bulky `~0.62-0.63 in / 15.7-16.0 mm` SOOW cord wins:** none of those M20 choices fits. Move to LAPP `MS-M-XL` M25 `53112035`, `9-17 mm`, rather than squeezing an undersized seal.

Measure the finished cord OD at several clock positions and the entire wall/backer/seal/locknut stack. Preserve straight approach and wrench access. Clamp outside and inside so the cable is stationary at the gland, witness-mark both faces after torque, then hose-test, roof-cycle, and reinspect for slip or water tracks.

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

## Measurements needed before cord/penetration release

Record all dimensions in roof-down, quarter, half, three-quarter, and roof-up states:

1. routed centerline distance between proposed moving-roof and fixed-shell clamp centers at every position—not only vertical roof stroke;
2. lateral/fore-aft offset and angular change at both endpoints through the stroke;
3. continuous front-gap height, width, and depth for the coil/guard, plus the roof-down retracted-storage envelope;
4. cab-to-camper swept clearance with roof down during a controlled articulation check; static level-shop clearance is insufficient;
5. lower and upper factory tangent lengths needed from the undisturbed coil throats through both structural clamps, drip loop, gland, internal clamp, and terminations;
6. gland wall thickness, flat sealing land, hole/access envelope, straight approach, rear bend clearance, and received cord OD tolerance;
7. complete one-way PV route. Current Renogy `4S` planning values are `114.86V` nominal-coefficient cold Voc and `9.50A` STC Isc pending received labels.

## Acceptance tests

### Starlink bench test

1. Establish a baseline with the complete factory cable.
2. Install the adapter pair and candidate coil on the bench.
3. Run the terminal at normal full service long enough to heat-soak the cable and connectors; verify no dropouts, speed instability, brownouts/reboots, connector heating, or visible arcing/carbonization.
4. Repeat with the coil relaxed and extended.
5. Preserve the complete factory cable as the recovery spare.

### Physical mockup and moving-cord acceptance

1. Use a full-size surrogate matching the candidate retracted length, coil OD, tangents, and approximate spring force between proposed structural clamp centers.
2. Cycle roof down through every intermediate state to fully raised at least `20` times before drilling; prove no cab contact, turn inversion, pinch, hard stop, or tail movement at the gland.
3. Bench-measure pull at down, `25%`, `50%`, `75%`, and full-up equivalents. Provisional acceptance is `<=5 lbf` incremental full-up pull and `<=10%` of measured lift-assist margin unless Hiatus approves more.
4. Confirm the down-state helix retracts naturally into the drained guard without being axially crushed, falling below the guide, or slapping the cab/camper.
5. Proof the real endpoint clamps at twice maximum measured operating force for one minute with no jacket slip, bracket motion, gland displacement, or terminal load.
6. After final de-energized install, complete at least `100` roof cycles; inspect the throats, jacket, clamps, guide, gland, and witness marks before energization.
7. Spray-test the drip loop/gland and complete a progressive roof-down road/articulation shakedown with witness material before normal travel.

### Trail-mode sequence

- Starlink: power down -> disconnect/remove coil -> cap fixed/moving RJ45 ends -> secure adapter pigtails.
- Solar: no normal trail or roof-motion disconnect step. The continuous front-gap cord stays installed. Open the fixed two-pole PV load-break only for electrical service; matched roof-side service connectors are unplugged only de-energized.
