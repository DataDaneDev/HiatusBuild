# Amazon one-month order-history reconciliation — through 2026-08-09

## Scope and source

- Source: owner-provided Amazon order-history CSV supplied `2026-08-10`, described as a one-month export.
- Parsed records: `19` line items / `19` units.
- Item-subtotal basis: `$425.22` before tax, shipping, credits, and returns.
- Captured order dates run only from `2026-08-05` through `2026-08-09`; this narrow result is not evidence that the rest of the month had no orders.
- The duplicate trailing header row was ignored.
- The sanitized tracked derivative in `references/amazon_order_history.csv` omits order IDs and private order-detail URLs. Public ASINs and public `/dp/ASIN` links are retained for exact matching.

All `19` lines map to Hiatus/F-350 work or on-hand build stock. No line was excluded as personal/unrelated. The exact installed allocation of the adjustable vents and adhesive heat-shield sheet is not documented, so the BOM records them as purchased stock without inventing a final location.

## Reconciliation result

| Date | ASIN | Item subtotal | BOM action |
|---|---|---:|---|
| 2026-08-09 | `B000LDA1WI` | `$16.83` | Existing row `171`; Eaton/Bussmann `HEB-AA` holder already captured exactly. |
| 2026-08-09 | `B013DDUSOS` | `$7.29` | Existing row `171`; Littelfuse `KLKD015.T` fuse already captured exactly. |
| 2026-08-09 | `B0FXBBXRFW` | `$46.75` | Existing row `170`; added exact ASIN to the already-priced Victron `200A/80V` five-pack. |
| 2026-08-08 | `B0GLGM9X8B` | `$21.99` | Added row `355`; three-piece washable camper rug set, final placement/retention field-fit. |
| 2026-08-08 | `B0D7LYHCMT` | `$2.99` | Updated row `354` from a `$7.50` planned USB cable to the exact purchased 6 ft USB-A-to-B cable. Verify data capability before reading the WS500 profile. |
| 2026-08-08 | `B0C6R22VBZ` | `$9.99` | Added row `356`; adjustable stainless ventilation hardware. Final cabinet/tech-cubby placement remains unassigned and cut-gated. |
| 2026-08-08 | `B0DYNTRH3D` | `$8.99` | Added row `357`; adhesive aluminum heat-shield stock. Final allocation and substrate/temperature suitability remain unverified. |
| 2026-08-08 | `B0F6NPV287` | `$7.99` | Updated row `176` from the `$20.97` Eaton plan to purchased Anyongora four-holder/mixed-fuse stock. Kept `Partially Purchased` because exact `3A` fuse availability and received markings still must be verified for WS500 `F-15`. |
| 2026-08-07 | `B0FND7L11X` | `$14.99` | Restored row `112` from inactive history to the active BOM: six `14 cu in` old-work boxes. Final downstream receptacle count, covers, clamps, conductor fill, wall fit, and accessibility remain open. |
| 2026-08-06 | `B0DLZWHPKJ` | `$38.99` | Updated row `27` from planned to purchased; Starlink DC converter remains heat/reboot/voltage-stability acceptance-gated. |
| 2026-08-06 | `B0GQZ5SNWR` | `$12.99` | Added row `358`; purchased optional Furnique factory-cable inline coupler for panel-fed ground deployment. |
| 2026-08-06 | `B00HEM5MZU` | `$9.49` | Consolidated in row `347`; purchased 10 ft shielded Cat6A fixed/interior run. |
| 2026-08-06 | `B0D3DK2K5F` | `$12.99` | Added row `359`; ten-pack of 1010 two-hole inside-corner brackets. Structural use remains fit/load-path gated. |
| 2026-08-06 | `B0DL358L3G` | `$19.99` | Updated row `344` from planned to purchased; Starlink pigtail pair remains continuity/shield/heat/retention gated. |
| 2026-08-06 | `B08LPMXM3Q` | `$17.99` | Split row `349` to the exact purchased VCELINK crimper. The unpurchased basic tester moved to planned row `360` at `$9.99`, preserving the prior combined allowance. |
| 2026-08-06 | `B0CVR26LWZ` | `$6.99` | Consolidated in row `347`; purchased 1 ft shielded Cat6A panel/coupler jumper or bench lead. |
| 2026-08-06 | `B0H286KLWZ` | `$35.00` | Updated row `345` from planned to purchased; retractile cable remains OD, termination, full-stroke, and loaded Starlink test gated. |
| 2026-08-05 | `B07YXZHZPH` | `$105.99` | Corrected row `341` from the earlier `$113.67` order-total basis to exact item subtotal. |
| 2026-08-05 | `B0DSKNT1K4` | `$26.99` | Corrected row `342` from the earlier `$28.95` order-total basis to exact item subtotal. |

## Cost result

- Amazon export item subtotal: `$425.22`.
- Net active-BOM change attributable to the Amazon reconciliation: `+$56.29`.
- The delta is lower than the export subtotal because many Starlink, screen, fuse, and WS500 items already existed as exact purchases or planning estimates.
- Active row `112` now carries the exact `$14.99` box purchase; its retired `$20.00` planning line was removed from inactive history.

## Additional owner-supplied evidence

### Starlink hardware and service

- Updated row `79` to the owner-reported `$405` aggregate purchase total for the Starlink Standard 4 X kit plus OEM mobility mount. The component split, tax, and shipping were not supplied, so the amount remains an aggregate `purchase_record` rather than an invented item subtotal.
- The OEM mobility mount is separate from the TRIO protective frame and attachment packages in rows `343` and `348`.
- Updated `bom/bom_misc_items.csv` from the stale `$165/month` entry to the current `$55/month` Starlink subscription. The exact service-plan name was not supplied; owner intends to move to an unlimited plan later. Recurring service is excluded from the one-time active build total.

### Mouser passthrough order

- The `2026-08-06` Mouser passthrough package was already represented exactly in row `346`: `1x NE8FDX-P6-W` at `$28.45` and `2x NE8MXR1-B-TOP-D` at `$8.93` each / `$17.86` extended; `$46.31` item subtotal.
- The previously reported `$54.80` checkout total leaves `$8.49` of unallocated shipping/tax outside component rows. No duplicate cost was added.

## Canonical total impact

- Active BOM before this pass: `$59,850.32`.
- Amazon reconciliation delta: `+$56.29`.
- Newly supplied Starlink kit/mobility-mount cost: `+$405.00`.
- Total active-BOM delta: `+$461.29`.
- Active BOM after this pass: `$60,311.61`.
- Inactive BOM after restoring row `112`: `$4,095.95`.

## Remaining acceptance/procurement gates

- Starlink follow-up as of `2026-08-12`: both Neutrik cable assemblies are complete, and every green-coil conductor passed owner DMM continuity. Repeat the conductor check on the short jumper; then verify shield continuity, converter heat/voltage behavior, loaded dropouts/reboots, full roof stroke and strain relief, final panel wall stack/cut, magnet/disc contact, tether, and direct-OEM recovery.
- RJ45 testing update: the VCELINK crimper is purchased. Basic continuity tester row `360` was retired after the owner's DMM method succeeded; a budget continuity tester would not certify Cat6A or replace the remaining shield and loaded-system tests.
- WS500 `F-15`: inspect the purchased mixed fuse pack for an exact `3A` ATO/ATC fuse and verify holder/wire markings and splice fit.
- WS500 USB: verify the purchased USB-A-to-B cable carries data before relying on it for profile capture.
- AC boxes: do not infer six downstream receptacles from a six-pack purchase. Inventory receptacles/covers/clamps and prove box fill, listing/markings, wall fit, accessibility, grounding, GFCI `LOAD` routing, and whole-chain trip/reset.
- Adjustable vents and heat shield: final install locations remain owner/field-fit decisions; no panel cut or adhesive install is authorized by procurement alone.

## Files updated

- `bom/bom_estimated_items.csv`
- `bom/bom_inactive_items.csv`
- `bom/bom_misc_items.csv`
- `bom/amazon_order_history_reconciliation_2026-08-10.md`
- `references/amazon_order_history.csv`
- `README.md`
- `docs/core/PROJECT.md`
- `docs/core/SYSTEMS.md`
- `docs/core/TRACKING.md`
- `docs/implementation/ELECTRICAL_AC_BOM.md`
- `docs/implementation/ELECTRICAL_fuse_schedule.md`
- `docs/implementation/ELECTRICAL_overview_diagram.md`
- `docs/plans/INSTALL_MINUS_12_READINESS_PLAN.md`
- `docs/plans/LIVE_BUILD_CHECKLIST.md`
- `docs/plans/STARLINK_SOLAR_MOVING_UMBILICAL.md`
- `docs/pdf_exports/{PROJECT,SYSTEMS,ELECTRICAL_AC_BOM,ELECTRICAL_fuse_schedule,ELECTRICAL_overview_diagram}.pdf`
- `docs/pdf_exports/assets/ELECTRICAL_overview_diagram/diagram-01.pdf` through `diagram-04.pdf`
- `logs/LOG.md`
