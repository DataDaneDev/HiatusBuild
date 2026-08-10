---
aliases:
  - Active procurement purchase list
  - Hiatus procurement list
tags:
  - hiatus/plan
  - hiatus/procurement
status: active
related:
  - "[[PROJECT_build_order_of_operations]]"
  - "[[TNUTZ_80_20_HARDWARE_MODEL_2026-06-01]]"
  - "[[ELECTRICAL_fuse_schedule]]"
---

# Active Procurement Purchase List — refreshed 2026-06-01

Freshness note `2026-06-01`: filename date is historical; this is the current short-horizon procurement surface. Use it for shopping-cart posture, not final cut/fabrication geometry.

Purpose: short-term buy list for finishing the live-tested electrical board as a hard-mounted, strain-relieved mobile module, plus only the supporting interior/prototype items that should not block that work.

Scope note: this is a purchase aid, not a final cut list. Do not order final extrusion cuts, drawer slides, panel skins, or cosmetic trim from this document alone.

## Private procurement evidence

When the owner requests reconciliation, Atlas can use a private, read-only Gmail connection to locate Amazon order confirmations, invoices/receipts, shipment notices, returns, and refunds relevant to this build. Mailbox access is task-driven rather than continuous monitoring. Only sanitized build facts may enter this public repo: item, quantity, price, useful order-total components, purchase date, and fulfillment/refund status. Omit the email address, raw message or attachment, order number, delivery address, payment details, and unrelated personal purchases; reconcile extracted facts against the BOM before treating them as project state.

## Priority order

1. MultiPlus programming/verification is no longer the procurement blocker: settings were redone and first-battery shore-charge behavior matched plan. Keep normal physical safety gates before unattended charging.
2. Finish electrical-board hard-mount, protection, labeling, strain-relief, and abrasion-control hardware after checking what is now on hand.
3. Orion input cleanup is reduced to one Lynx-compatible fuse: obtain a verified `40A` MEGA (`58VDC` minimum under the locked `56.8V` charge ceiling; Victron `CIP138040020 40A/80V` is the replacement fallback) for Slot 4 if verified stock is not already on hand. No standalone `F-06`, DIN holder, or additional inline fuse hardware is required.
4. WIP TNUTZ shopping cart for `10-series` prototype stock/hardware after reviewing the visual aids and current module assumptions; do not treat it as final-cut geometry.
5. Diesel heater tank later, after physical re-measurement.

## Amazon / Victron purchase list

### MultiPlus programming + Victron/Cerbo wiring

- **MK3-USB-C interface**
  - Purchased: Victron `MK3-USB-C` interface on `2026-05-27` (`$59.44`).
  - Use: service/programming interface for MultiPlus LiFePO4 charger settings.
  - Status: hardware purchased and settings owner-verified by first-battery behavior; retain as service/rollback tool.

- **SmartShunt to Cerbo VE.Direct cable**
  - Purchased: Victron VE.Direct cable, `5.90 ft` on `2026-05-27` (`$16.31`).
  - Use: SmartShunt-to-Cerbo monitoring link.

- **MPPT to Cerbo VE.Direct cable**
  - Purchased: Victron VE.Direct cable, `2.95 ft` on `2026-05-27` (`$16.13`).
  - Use: MPPT-to-Cerbo link if routing works; otherwise keep as service/spare and buy a longer VE.Direct cable only if the final board layout needs more slack.

- **Short VE.Bus/RJ45 patch cable**
  - Purchased: one manufactured RJ45/Ethernet patch cable, `3 ft`, on `2026-05-27` (`$5.99`).
  - Use: Cerbo VE.Bus to MultiPlus or MK3 service path. Do **not** use the Cerbo LAN port for VE.Bus.
  - Optional: buy a second short spare/service cable later only if the single `3 ft` cable is inconvenient during MK3 programming.

Existing/on-hand reminder: Cerbo power input cable with inline fuse and `2x` VE.Can RJ45 terminators are already accounted for; no CAN bus is currently planned.

### Electrical-board mobile-module cleanup

2026-05-27 Amazon order added prototype mounting/accessory hardware: countersunk neodymium cup magnets, magnetic accessory mount, and steel weld tabs/brackets. Still verify the boring board-cleanup consumables below from on-hand stock before buying duplicates.

- **Rubber grommet assortment**
  - Buy if current stock is thin: mixed firewall/pass-through grommets sized for AC/DC cable entry points.
  - Use: abrasion protection anywhere cable crosses metal/plastic/plywood edges.

- **Split loom / abrasion sleeve**
  - Buy: `3/8 in`, `1/2 in`, and `3/4 in` split loom or equivalent braided sleeve.
  - Use: service loops, near-bus protection, and exposed routing during mobile board handling.

- **Cable clamps and adhesive/screw-down mounts**
  - Buy: P-clamps, screw-down cable clamps, adhesive zip-tie mounts, and quality zip ties.
  - Use: convert the proven live layout from bench-wired to vibration-resistant mobile module.

- **Small stainless screw/washer/spacer kit**
  - Buy: mixed M4/M5/M6 or #8/#10 stainless hardware, washers, nylon spacers/standoffs.
  - Use: mount Orion, fuse holders, DC panel, AC enclosure, Cerbo, reserved MPPT/WS500 locations, and service covers without improvised fasteners.

- **Wire labels / heat-shrink label tape**
  - Buy: heat-shrink labels or compatible label-tape cartridges.
  - Use: cable IDs, fuse IDs, disconnect/service labels, and shore-current warning labels.

### Gravity-fill vent hose

Known interface: gravity-fill vent nipple measured around `10 mm OD` on the main land and about `11 mm OD` at the largest barb/ridge.

- **Preferred hose**
  - Purchased: `10 mm ID x 13 mm OD`, `10 ft` food-grade silicone tube with stainless worm-gear clamps on `2026-05-27` (`$10.99`).

- **Common fallback**
  - Buy: `3/8 in ID` food-grade/potable tube; warm the hose if needed to install over the ~`11 mm` barb/ridge.
  - Link/search: <https://www.amazon.com/s?k=3%2F8+ID+food+grade+vinyl+tubing>
  - Stiffer/less kink-prone search: <https://www.amazon.com/s?k=3%2F8+ID+food+grade+braided+PVC+tubing>

- **Clamps**
  - Purchased with hose kit; verify clamp range against installed `13 mm OD` tube.
  - If included clamps do not tighten cleanly, replace with small stainless clamps sized to the installed hose OD.

- **Avoid**
  - Do not use the previous `1/2 in ID x 5/8 in OD` tube for this vent nipple; it is too large.
  - `7/16 in ID` is last-resort only and should be clamped and vent/leak checked.

### Diesel heater fuel tank

Posture: not a blocker. Re-measure before buying. Carry-extra-fuel is acceptable until the final tank/service envelope is validated.

- **Possible slim candidate if actual clearance is at least ~3.5 in**
  - Candidate: `10 L / 2.64 gal` stainless parking-heater fuel tank for Webasto/Eberspacher-style heaters.
  - Link: <https://www.amazon.com/Parking-Stainless-Eberspacher-Replacement-Distance/dp/B0G4RP11X8>
  - Planning caveat: prior search suggested no clean off-the-shelf `5-10 gal` tank fits a true ~`17 in x 3 in` opening; the `3 in` depth is the blocker.

- **Decision rule**
  - If measured usable depth is under ~`3.5 in`, skip this class of off-the-shelf tank.
  - If `5-10 gal` is mandatory, expect custom slim tank or alternate mounting.
  - If lower capacity is acceptable, a `10 L` slim tank can remain a candidate.

## Mouser / electrical cleanup list

- **Orion input-fuse cleanup history and final Slot 4 lock**
  - Purchased `2026-06-01` Mouser order, total `$38.79`.
  - Fuse stock: `3x` Mouser `576-166.7000.5202` / Littelfuse `166.7000.5202` FKS/ATO fuse, `20A`, `80VDC`, `$7.88` each / `$23.64` extended.
  - Housing stock: `3x` Mouser `576-178.6150.0001` / Littelfuse `178.6150.0001`, `$1.51` each / `$4.53` extended. Correction: these are empty housings with no contacts or leads, not install-ready holders. They are unused/dead-end stock; do not buy proprietary contacts or build either the Orion or WS500 branch around them.
  - Final install: one verified `40A` MEGA (`58VDC` minimum under the locked `56.8V` charge ceiling; Victron `CIP138040020 40A/80V` is the replacement fallback) in Lynx Slot 4 feeding the existing `6 AWG` Orion input pair directly. Retire standalone `F-06`; no DIN rail, pigtails, reducers, butt splices, or additional input holder.
  - Treat the purchased `20A` FKS fuses, empty FKS housings, and `30A/58V` MIDI stock as unused/dead-end inventory. Do not repurpose them for the final WS500 branch.

- **WS500 alternator purchase package — ordered `2026-08-09`; receipt/marking checks pending**
  - `F-04`: Victron `CIP138200020`, `200A/80V` MEGA, five-pack purchased at `$46.75` item subtotal. Install one in Lynx Slot 3 after confirming body markings and fit; retain spare stock.
  - `PH-VAN` red: Eaton/Bussmann `HEB-AA` water-resistant in-line holder (Amazon ASIN `B000LDA1WI`, `$16.83`) + Littelfuse `KLKD015.T` `15A/600VAC/DC` fast-acting midget fuse (Amazon ASIN `B013DDUSOS`, `$7.29`) purchased at `$24.12` combined item subtotal. Use short `14 AWG` pigtails and a sealed `14-to-16 AWG` splice. The source pigtail uses an M8 ring terminal on the same F-04 external/cable-side stud as the `2/0` alternator lug. Verify those small termination parts in on-hand stock before installation. This remains one in-line loom component; do not add a DC fuse panel, DIN rail, or enclosure.
  - Common negative: place the Wakespeed `500A/50mV` shunt on the battery side of the hard-mounted Victron SmartShunt: `battery negative combine -> Wakespeed shunt -> SmartShunt -> Lynx`. Purple/high faces battery negative and grey/low faces SmartShunt/Lynx. No `5A` sense fuses.
  - Routing: one `50 ft` roll of `3/4 in` split nylon loom, one `20-pack` of `1 in` cushioned P-clamps, and one correctly fitting red alternator-B+ boot set.

## TNutz / 80/20 posture

Detailed hardware model and WIP cart owner: [TNUTZ_80_20_HARDWARE_MODEL_2026-06-01](TNUTZ_80_20_HARDWARE_MODEL_2026-06-01.md). Use that worksheet for the consolidated `10-series` connector/T-nut/floor-mount cart and visual aids. The owner still needs to review the visuals before treating the cart as ready to submit. This section remains the shorter procurement posture summary.

Ordering posture: WIP shopping cart / prototype material only. Do **not** buy the old broad `8x 92 in` `15-series` package as a default starter order. Choose **no machining** for any prototype sticks unless a specific measured module envelope has passed physical mockup.

### Better current approach

- Current owner intent: consolidate around `17 x 94 in` full-length TNUTZ `10-series` sticks plus the hardware model quantities, pending visual-aid review and physical validation.
- Keep a few representative `15-series` pieces only for stiffness comparison or a proven heavy/dynamic module.
- Treat the electrical board/module as the first mechanical proof: mount real components, prove access, then decide what frame/skin support is actually needed.

### Candidate prototype stock, if needed now

- **10-series lighter/module stock**
  - Product: EX-1010 — `1 in x 1 in` Smooth T-Slotted Aluminum Extrusion.
  - Link: <https://www.tnutz.com/product/ex-1010/>
  - Quantity: small prototype batch, e.g. `4-6` sticks at stock length or shorter shipping-friendly lengths.
  - Machining: `No machining`.

- **10-series hardware**
  - Corner gussets: CB-010-A, quantity `16-24`.
  - Economy T-nuts: ET-010, quantity `50-75`.
  - Drop-in T-nuts: DB-010, quantity `20`.
  - End caps: EC-010, quantity `16-24`.
  - Cable-tie drops: AC-010-A, quantity `10`.

- **15-series sample/support only**
  - Product: EX-1515L or equivalent.
  - Quantity: small sample/prototype allowance only if the electrical/fridge/desk block shows a real stiffness need.
  - Do not order broad `15-series` main stock for the water tank; that old tank-exoskeleton assumption is superseded.

## Amazon / local add-ons for 80/20 assembly

- **3M VHB tape**
  - Search: <https://www.amazon.com/s?k=3M+VHB+5952+tape>
  - Use: clean panel bonding where suitable; not a structural substitute unless the joint is designed for tape.

- **Closed-cell neoprene or foam anti-rattle tape**
  - Search: <https://www.amazon.com/s?k=closed+cell+neoprene+foam+tape>
  - Use: bedding, anti-rattle, and paint/abrasion isolation.

- **Plastic shims**
  - Search: <https://www.amazon.com/s?k=plastic+shims+assorted>
  - Use: module alignment and non-absorptive spacing.

## Do not buy yet

- Final-cut extrusion lengths.
- Broad/default `15-series` stock package.
- Drawer slides.
- Panel skins.
- Cosmetic trim.
- Large diesel tank.
- `6x BougeRV Arch Pro 100W` panels and dedicated cassette hardware until the roof/fan/Starlink survey, `1:1` templates, cassette design, preliminary `<=75 lb` budget, and any required insurer/Hiatus acceptance pass. After receipt, bonding/travel remain blocked by label/polarity verification, built-cassette load proof, actual all-up weight, bond coupon, final PV route hardware, and hot-roof commissioning. The selected `3S2P` topology does not presently call for individual string fuses.
- Custom/fancy bracket packs beyond prototype hardware.

## 2026-05-27 Amazon purchase captured

Purchased/order subtotal: `$171.17` before tax (`$183.57` total with estimated tax). Public docs intentionally omit order number, address, and payment details.

Build-relevant items captured in BOM/log:

- Victron `MK3-USB-C` interface — `$59.44`.
- Victron VE.Direct cable, `5.90 ft` — `$16.31`.
- Victron VE.Direct cable, `2.95 ft` — `$16.13`.
- RJ45/Ethernet patch cable, `3 ft` — `$5.99`.
- Food-grade silicone vent hose/clamp kit, `10 mm ID x 13 mm OD`, `10 ft` — `$10.99`.
- Acegoo `118W` 12V USB-C/USB-A PD outlet, qty `1` — `$22.99`.
- Prototype mounting/accessory hardware: cup magnets (`$12.34`), magnetic accessory mount (`$9.99`), steel weld tabs/brackets (`$16.99`).

## Validation gates before next procurement round

- Program/verify MultiPlus charger settings with the purchased MK3 before relying on sustained shore charging.
- Mount the electrical board hardware and verify service access, cable bends, fuse access, covers, labels, and strain relief.
- Dry-fit vent hose and clamp; verify no leak and no vent restriction.
- Physically re-measure diesel tank envelope before ordering tank hardware.
- Use any TNutz order for mockup/prototype framing; lock exact cuts only after the real module envelopes and service access pass.
