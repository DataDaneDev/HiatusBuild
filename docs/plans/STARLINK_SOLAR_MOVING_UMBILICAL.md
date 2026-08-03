# Starlink + solar moving-roof umbilical

Status: **measurement-gated; removable twin-coil architecture is the current lead**  
Last current-source check: `2026-08-03 10:03 MDT`

## Decision

Use two electrically separate retractile jumpers mounted side by side between the fixed camper body and moving roof:

1. shielded Ethernet/PoE jumper for Starlink Standard 4 X;
2. correctly sized PV-rated jumper for solar.

The jumpers may share a mounting area and visual route but do not share conductors or a hybrid connector. The cable's own spring coil stores slack. Install independent strain-relief anchors so spring force is carried by the structure rather than the electrical connectors.

This supersedes the prior chain-first and guided-loose-loop recommendations.

## Why the other two moving-section concepts lost

### Side-mounted energy chain — rejected as the default

A chain does not make the cable branch-proof. On an exposed vertical camper wall, the return bend still needs somewhere to collect when the roof closes. Without a measured recess or enclosed guide trough, the chain will project outward or bunch into a side lump. Keeping it against the wall would require another trough, retractor, or stow mechanism, increasing bulk and making trail removal harder.

An energy chain remains a contingency only if later geometry reveals a real inboard trough; there is no reason to buy one for the current exterior-wall concept.

### Loose cable/service loop in sleeve — rejected

Without an added spring reel, elastic take-up, or guided carriage, it is simply a slack cable hanging from two anchors. The sleeve supplies abrasion resistance but does not store slack. Adding the missing take-up hardware recreates a less predictable cable-carrier system.

### Meaning of `sheltered`

A route is sheltered only if an existing rigid camper feature projects outward farther than the cable and the cable stays inside that feature's contact shadow through the full roof stroke. No such location has been physically confirmed. The earlier `front guard` wording referred to an imagined fabricated pouch/deflector, not an existing Hiatus component, and is withdrawn.

No exterior always-connected cable is branch-proof. Normal-road mode keeps the coils attached; tight-trail mode powers/isolate the circuits, removes the coils, and caps the fixed ends.

## Lead physical layout

```text
MOVING ROOF / ROOF HARNESS
  Starlink terminal -- short Type-4/RJ45 adapter pigtail -- weatherproof RJ45 joint
                                                        |
                                                  shielded coil
                                                        |
  PV roof harness ------------------------------- PV-rated coil
                                                        |
FIXED CAMPER BODY
  Starlink lower adapter/body entry -> router/power supply
  PV disconnect -> fixed PV cable -> MPPT 150/45
```

Mount the upper and lower strain-relief anchors vertically aligned. Keep the two coils separated enough that they cannot wind into one another. The exact side/front location, anchor spacing, free extension, tangent lengths, and down-state coil length wait for measurements.

The selected moving jumper must provide more free extension than measured roof travel plus endpoint routing and strain-relief reserve. Do not use `36 in` as the purchase length merely because `36 in` is the current lift assumption.

## Starlink: practical no-Ethernet-tool path

### Topology

- Remove and retain the factory Starlink cable as the unmodified recovery spare.
- Use one third-party Type-4-to-RJ45 adapter at the Standard 4 X terminal and one at the Gen 3 router/power end.
- Connect the two adapters with a removable shielded retractile Ethernet cable.
- Use the adapters' threaded IP67-style RJ45 glands for the exterior joints.
- Put structural P-clamps/anchors behind both joints; do not let the connectors carry coil tension.

### Current-source shortlist

| Item | Current link / observed price | Posture |
| --- | --- | --- |
| `2x` STARGEAR Standard 4/4X/Gen 3 Type-4-to-RJ45 adapters | [Amazon `B0D9NB1SQC`](https://www.amazon.com/dp/B0D9NB1SQC) — `$58.99`, in stock/Prime at check | **Lead adapter pair.** Third-party/non-OEM; seller claims 24 AWG copper pigtails, full shielding and IP67 RJ45 coupling. Bench-test before vehicle install. |
| ZBLZGP 3 m stretched Cat6A retractile cable | [Amazon `B0H286KLWZ`](https://www.amazon.com/dp/B0H286KLWZ) — `$35.00`, two in stock/Prime at check | **Budget prototype only.** PUR, dual shield, pure-copper claim, but 26 AWG and no established review history. STARGEAR recommends 23 AWG or larger for third-party PoE runs, so this is not accepted until a loaded Starlink heat/dropout test passes. |
| L-com `TRD815SZ-CH-1-6F` industrial coil | [L-com product page](https://www.l-com.com/category-5e-ethernet-coil-cord-rj45-rj45-180d-tangents-f-utp-foil-shielded-26awg-high-flex-industrial-zero-halogen-tpu-teal-1-to-6f) | Higher-confidence industrial construction and useful `1-6 ft` geometry, but current retail price/stock could not be verified without vendor challenge and prior pricing was poor. Do not buy unless the Amazon prototype fails or a distributor price is acceptable. |
| One-cable fixed-body entry | [Seaview retro-fit cable gland, Amazon `B077PQ4FGG`](https://www.amazon.com/dp/B077PQ4FGG) — `$29.00`, in stock/Prime at check | **Value entry** if only the stationary Starlink pigtail crosses here. Split/retrofit design accepts existing connectors. |
| Shared multi-cable fixed-body entry | [Scanstrut `DS-H-MULTI-BLK`, Amazon `B0CSTC4D3C`](https://www.amazon.com/dp/B0CSTC4D3C) — `$53.34`, in stock at check | **Lead shared entry** only if Starlink and the fixed PV conductors actually enter through one horizontal location. Not a moving-cable manager or quick disconnect. |

Observed base hardware total is `$122.99` with the Seaview entry or `$147.33` with the Scanstrut entry, before clamps, caps, sealant, and any short interior patch lead.

## Neutrik etherCON path

The Neutrik hardware is rugged and attractive, but it does not remove the need to adapt Starlink's Type-4 ports to RJ45.

- [Neutrik `NE8FDX-P6-W`](https://www.neutrik.com/en/product/ne8fdx-p6-w) is a sealed Cat6A feedthrough chassis connector. It is female RJ45 on the rear, so the panel part itself needs no punch-down or crimp tool. Current Amazon listing: [Amazon `B01H6Z3KPI`](https://www.amazon.com/dp/B01H6Z3KPI), `$29.83` at check.
- `NE8MC-B-TOP` is not the current manufacturer part number; Neutrik's current TOP cable-carrier family uses `NE8MX...` names.
- [Neutrik `NE8MX-B-TOP`](https://www.neutrik.com/en/product/ne8mx-b-top) fits approximately `5-8 mm` cable but is for non-preassembled cable. Installing it on a premade coil requires cutting an RJ45 end off and reterminating it with a compatible shielded stranded-conductor plug and Ethernet crimper.
- [Neutrik `NE8MX6-T`](https://www.neutrik.com/en/product/ne8mx6-t) is the Cat6A/PoE++ self-termination connector and does not use a conventional modular-plug crimper, but its published `7-9.5 mm` cable-OD range must match the selected coil. Current Amazon listing: [Amazon `B07B1F4Y9X`](https://www.amazon.com/dp/B07B1F4Y9X), `$17.65` plus `$9.95` delivery at check—reasonable only if combined shipping or another seller improves the delivered cost.
- [Neutrik `NE8MX-B`](https://www.neutrik.com/en/product/ne8mx-b) accepts a preassembled RJ45 cable without retermination, but it is not the exterior `TOP` weather-sealed solution.

**Recommendation:** do not buy Neutrik parts until the chosen coil's actual outside diameter and termination construction are known. A full two-panel Neutrik route adds two chassis connectors, two cable connectors, two panel holes, and four extra RJ45 interfaces. It protects the ends, not the cable midspan. Use it only if the physical panel/latch quality is worth that complexity after the simple adapter-and-threaded-gland prototype succeeds.

## Solar moving jumper

The solar jumper remains sizing-gated because the panel model, string arrangement, cold `Voc`, array `Isc`, total moving length, and exact roof travel are not locked.

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
| IMO `SI32-PEL64R-2` class enclosed rotary PV isolator | Distributor sourcing pending | Preferred rotary product class if a current US seller and sane delivered price can be confirmed. |

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
