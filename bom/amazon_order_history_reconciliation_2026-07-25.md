# Amazon web-extension order-history reconciliation — 2026-07-25

## Scope and source

- Source: owner-provided Amazon order-history CSV exported with a browser extension on `2026-07-25`.
- Parsed records: `121` line items / `131` units.
- Parsed item-subtotal basis: `$8,644.52` before tax, shipping, credits, and returns.
- A duplicate header row at the end of the file was ignored.
- Repository artifacts intentionally omit order IDs, private order-detail URLs, and private item URLs. ASINs are retained because they are public product identifiers useful for exact reconciliation.

## Coverage warning

Despite the filename saying YTD, this export is **not a complete 2026 YTD ledger**. It contains January, February, March, April, and July rows, but no May or June rows. The existing BOM and prior reconciliation records contain known May/June Amazon purchases, so their absence here is a scraper-coverage gap—not evidence of returns, cancellations, or non-purchase.

| Month | Line items | Units | Item subtotal |
|---|---:|---:|---:|
| 2026-01 | 21 | 22 | `$850.12` |
| 2026-02 | 62 | 69 | `$6,112.40` |
| 2026-03 | 9 | 10 | `$987.30` |
| 2026-04 | 12 | 13 | `$395.60` |
| 2026-07 | 17 | 17 | `$299.10` |
| **Captured total** | **121** | **131** | **`$8,644.52`** |

Use the extension export as the preferred exact-title/ASIN source, but verify that every Amazon order-history page/date range has loaded before treating a future export as complete. This pass therefore preserves prior Gmail/CSV/screenshot reconciliation rather than deleting anything absent from the web-extension file.

## New purchases since the prior 2026-07-20 reconciliation

All four newly exposed lines are build/truck relevant and are now represented in the canonical BOM. Their item subtotal is `$88.91`.

| Date | ASIN | Item | Subtotal | BOM action |
|---|---|---|---:|---|
| 2026-07-24 | `B0C8JMH91Q` | `2-3/8 in` / `60 mm` bi-metal hole saw | `$7.80` | Added row `239`; exact KUS `FLS-U` opening tool. Tank cut remains geometry- and port-map-gated. |
| 2026-07-25 | `B0C7QBNVG9` | EFIELD `1/2 in PEX-B x 3/8 in OD compression male` adapters, 2-pack | `$10.83` | Row `233`; one for each FORIOUS faucet hose. No PTFE tape at compression seats. |
| 2026-07-25 | `B0FDFM97HP` | YVSKM `1/2 in PEX-B x 1/2 in female swivel` adapters, 4-pack | `$11.99` | Row `319`; use one at accumulator outlet and retain three spares. Listing says no-lead, but markings, gasket fit, potable documentation, and pressure test remain acceptance gates. |
| 2026-07-25 | `B0GHRQ27J6` | Dr.Roc Super Duty spare-hoist extension/lug-wrench tool kit | `$58.29` | Added row `240`; verify the full assembled extension, spare-hoist drive, lug fit, and stowage on the 2021 F-350 before travel reliance. |

## Existing lines enriched by the web export

No new costs were added for these already-reconciled purchases. The BOM was enriched with exact ASIN/title data where the earlier Gmail or screenshot source had been generic, truncated, or identifier-free:

- TKDMR repeat `2/0 AWG x 5/16 in` lug stock — row `35`, ASIN `B08R6VFF6B`.
- Sanuke `4 AWG` lug stock — rows `37` and `242`, ASINs `B092ZM6XY3` and `B092ZN6TGP`.
- July 12 `1/4-20` flat-head hardware — rows `248-249`, ASINs `B0D6LWGC8X` and `B0D6LW16SD`.
- `2 in x 10 ft` double-sided foam mounting tape — row `96`, ASIN `B0FPQ29CX1`.
- KUS `14.5 in` water sender — row `212`, ASIN `B00Y831WYI`.
- SharkBite PEX adapters and Banjo/Green Leaf fill/vent elbows — rows `218-220`, exact ASINs and item subtotals recorded.
- Flooring roller, paint mixer, wash-brush kit, and visor mirror — rows `175`, `226`, `318`, and `229`, exact ASINs recorded.

The `2026-07-26` BOM normalization later split clear multi-item rows into component-level records while preserving this sanitized evidence. Personal consumables and unrelated travel/grooming items remain outside the Hiatus BOM. Exact-ASIN string presence is reconciliation metadata, not the completeness test.

## Hot-water and plumbing result

- Active hot water remains propane-only: Joolca HOTTAP V2 Essentials in the rear swingout package with parked-only BLUE cold-out / RED hot-return water connections.
- Electric storage/tankless candidates, dedicated electric-heater branch language, and an interior heater-cubby reservation were removed from active BOM/checklist/finish-planning scope.
- Generic water-QD and propane-QD placeholders were closed: exact CPC HFC35 NSF parts own the water interface, and the supplied HOTTAP QCC1 regulator/hose connects directly to the cylinder only while parked.
- The fixed camper water pack now explicitly uses the purchased EFIELD faucet adapters and one purchased YVSKM accumulator swivel. The YVSKM part is **purchased, not automatically approved**: verify markings, included gasket, thread/seat fit, and cold pressure before service; use the Apollo fallback if it fails.
- The purchased `60 mm` hole saw does not clear the tank cut. Freeze the port/sender map and prove flat unobstructed geometry first.

## Files updated

- `README.md`
- `bom/bom_estimated_items.csv`
- `bom/amazon_order_history_reconciliation_2026-07-25.md`
- `docs/core/SYSTEMS.md`
- `docs/core/TRACKING.md`
- `docs/implementation/INTERIOR_furniture_layout_and_galley.md`
- `docs/implementation/INTERIOR_finish_paneling_and_feature_choices.md`
- `docs/plans/LIVE_BUILD_CHECKLIST.md`
- `logs/LOG.md`
