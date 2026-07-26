# Amazon Gmail Purchase Reconciliation — 2026-07-20

## Scope and evidence

- Source: Dane's authorized Gmail account through the local `gmail-readonly` path. No write-capable Gmail scope was used.
- Window: `2026-01-19` through `2026-07-19` local-date coverage (`after:2026/01/18 before:2026/07/20`).
- Amazon evidence reviewed: order confirmations, shipment/delivery notices, and return/refund notices.
- Coverage result: `42` Amazon order-confirmation messages were found. The `23` confirmations through `2026-05-31` all had a primary order identifier already present in `references/amazon_order_history.csv` (`23/23`), so the prior `2026-06-01` reconciliation remains the historical baseline.
- New period: `19` confirmations from `2026-06-02` through `2026-07-19`.
- Full HTML extraction recovered `53` named line-item records representing `52` unique product classes from the new confirmations. Amazon's privacy-category emails initially suppressed four titles, but owner-provided Amazon order screenshots on `2026-07-20` resolved all four without exposing private order identifiers in the repo.

Privacy boundary: this repository artifact intentionally omits Amazon order numbers, message IDs, account/address data, and private order URLs. Product descriptions, dates, quantities, and prices are retained only where they are relevant to the build BOM.

## Cost basis

The canonical BOM continues to use item-subtotal pricing where item detail is available. Checkout/shipment totals are retained here only as reconciliation controls because they include tax and, in some cases, order-level adjustments.

- Reconciled newer gross checkout/shipment envelope: `$1,987.34`.
- Observed refund: `$21.44` for the returned BLCCLOY 8-set T-shape 10-series joint-plate kit.
- Reconciled newer net checkout/shipment envelope after that refund: `$1,965.90`.
- The `2026-06-05` Amazon hardware/fit-out checkout contained two suborders totaling `$1,017.34` gross. Extracted item subtotals total `$952.55` across `38` units / `25` product classes. Removing the returned `$19.99` item leaves `$932.56` of kept item subtotal; the `$21.44` tax-inclusive refund leaves `$995.90` net checkout cost.
- To avoid double-counting that order in the BOM, the kept `$932.56` item subtotal is split between monitor-arm row `99` (`$179.99`) and aggregate hardware/fit-out row `222` (`$752.57`). Row `222` also includes the later `$21.66` FORRCKY repeat purchase, bringing that row to `$774.23`; the July washer repeat is tracked in row `46` instead.

Subsequent BOM normalization on `2026-07-26` preserved these reconciliation totals but replaced the aggregate layout with component rows. The `$774.23` hardware subtotal is now carried by rows `222` and `295-316`; the July washer and flat-head screw classes are itemized in rows `243-249`. The historical dispositions in the table below describe how the source evidence was first reconciled, not the current row granularity.

## New-period reconciliation

| Local purchase date | Confirmed items | Price control | BOM disposition |
| --- | --- | ---: | --- |
| 2026-06-02 | #4 x 3/8 in Phillips pan-head screws, 100 pack | `$3.99` item / `$4.28` checkout | Added row `223` |
| 2026-06-03 | Thick 3/4 OD x 1/4 ID x 1/4 in rubber spacer washers, 25 pack | `$9.99` item / `$10.71` checkout | Corrected row `50` |
| 2026-06-05 | 38-unit Amazon 10-series/interior-fit-out order | `$952.55` item / `$1,017.34` checkout | Monitor moved to purchased row `99`; kept remainder in row `222`; returned kit excluded |
| 2026-06-08 | BILITOOLS 15-piece universal serpentine-belt/tensioner tool set | `$30.99` item / `$33.24` checkout | Added row `224` |
| 2026-06-09 | SVAAR 2 AWG copper butt connectors, 8 pieces, with 3:1 heat shrink | `$17.99` item / `$19.29` checkout | Added row `225` |
| 2026-06-12 | Gates K060885 Micro-V belt | `$26.59` item / `$28.52` checkout | Existing row `206` already correct on order-total basis |
| 2026-06-17 | SKALON 18 in heavy-duty zip ties, 120 pack | `$13.49` item / `$14.47` shipped total | Added as repeat stock to row `49` |
| 2026-06-24 | Ninja SP151, bamboo topper, parchment, and tape measure | `$186.19` checkout | Existing row `68` already reconciled |
| 2026-06-24 | Sarlai 15 x 15 sink + FORIOUS faucet/soap dispenser | `$224.25` checkout | Sink corrected to `$179.00` in row `208`; faucet row `207` already correct at `$47.99` |
| 2026-06-24 | Nelko P21 14 x 40 mm replacement label roll | `$7.59` item / `$8.14` checkout | Added as repeat supply to row `52` |
| 2026-06-26 | Duxtop cooktop + BougeRV fan + GlueTread sidewall kit | `$171.89` checkout | Existing rows `67`, `209`, and `210` already match item subtotals |
| 2026-07-05 | FORRCKY 20-set 10-series bracket repeat + 50-piece 1/4 in washer pack | `$27.65` item / `$29.65` checkout | Brackets added to row `222`; washers added to row `46` |
| 2026-07-07 | Drill-brush attachment set | `$12.99` item / `$13.93` checkout | Added with cleaning tools in row `227` |
| 2026-07-07 | 62 in truck/RV wash-brush kit | `$24.69` item / `$26.48` checkout | Added with cleaning tools in row `227` |
| 2026-07-12 | KUS 14.5 in sender + 1/4-20 x 2 and x 2-1/2 in flat-head screw packs | `$77.48` item / `$83.10` shipped total | KUS remains row `212`; screw packs added to row `46` |
| 2026-07-13 | POWERTEC long-handle J-roller + Bates paint/mud mixer | `$23.98` item / `$25.72` checkout | Added row `226` |
| 2026-07-16 | SharkBite PEX adapters + Banjo fill elbow + Green Leaf vent elbow | `$34.14` item / `$36.62` checkout | Rows `218-220`; Banjo and vent-elbow prices corrected |
| 2026-07-18 | 3M heavy-duty double-sided tape; Sanuke 10-piece 4 AWG x 3/8 in/M10 lug set; TKDMR 10-piece 2/0 AWG x 5/16 in lug set | `$41.91` item / `$44.95` checkout | Screenshot-resolved into rows `96`, `37`, and `328`; row `228` reduced to a zero-dollar reconciliation bridge |
| 2026-07-19 | Sixzoo car sun-visor vanity mirror | `$7.99` item / `$8.57` checkout/shipped total | Screenshot-resolved row `229` |

## Final June 5 hardware/fit-out inventory

The final checkout differed materially from the earlier 31-item `$747.94` pre-submit cart snapshot. Gmail confirms `38` units / `25` product classes at a `$952.55` item subtotal before tax. Kept inventory includes:

- FORRCKY 10-series hardware: two 10-set heavy-L kits and four 20-set 90-degree kits; a fifth 20-set kit was purchased on July 5.
- BLCCLOY 10-set L-corner and 10-set T-corner kits. The separate 8-set T-shape kit was returned and is not counted.
- Abeicy: two 100-count 1/4-20 roll-in T-nut packs and two 25-count inside-corner packs.
- 800 BNUOK 1/4-20 x 1/2 in low-profile socket screws.
- 12 internal L connectors, 10 four-hole joining plates, and 25 pieces of 3/16 x 1 x 12 in 6061 flat bar.
- Four 16 in piano hinges, four 100N gas struts, rubber/TPE edge trims, 50 ft birch edge banding, and a VESA laptop tray.
- ARES WING dual monitor arm, tracked separately in row `99` because it remains a parked-use item until a travel cradle/restraint is built.
- DMWD five-pack rocker switches, WEBANG 10-pack 20A receptacles, RVSPARK two-pack USB-C outlets, and a 100W USB-C/5AC desktop power grommet.
- 9/32 in drill-bit stock and a 1/4-20 tap/#7 drill set.

Safety note: purchased inventory is not automatic installation approval. The desktop AC grommet and non-GFCI receptacles remain stock until the permanent AC layout, enclosure, GFCI protection, cable strain relief, and listing/fit requirements are satisfied.

## BOM changes

- Updated existing rows during the Gmail pass: `46`, `49`, `50`, `52`, `99`, `208`, `212`, `219`, and `220`. Owner screenshots then resolved rows `35`, `37`, `96`, `228`, and `229`.
- Added rows: `222-229`.
- Exact corrected prices include the Sarlai sink (`$179.00`), Banjo fill elbow (`$13.33`), Green Leaf vent elbow (`$12.97`), monitor arm (`$179.99`), 3M tape (`$20.99`), repeated 4 AWG and 2/0 lug stock, the `$7.99` visor mirror, and other repeat hardware/supply buys.
- No private Amazon identifiers were copied into the BOM or this reconciliation report.
