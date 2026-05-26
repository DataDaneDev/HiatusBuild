# Procurement Purchase List — 2026-05-26

Purpose: refined short-term buy list for the active HiatusBuild reminder items: Cerbo/Victron wiring, gravity-fill vent hose, diesel heater tank, and 80/20/TNutz starter stock.

Scope note: this is a purchase aid, not a final cut list. Do not order final extrusion cuts, drawer slides, panel skins, or cosmetic trim from this document alone.

## Priority order

1. Victron/Cerbo communication cables.
2. Gravity-fill vent hose and clamps.
3. TNutz starter stock and 80/20 hardware.
4. Diesel heater tank later, after physical re-measurement.

## Amazon / general purchase list

### Victron / Cerbo wiring

- **SmartShunt to Cerbo VE.Direct cable**
  - Buy: Victron VE.Direct cable, `1.8 m / 5.9 ft`.
  - Link: <https://www.amazon.com/Victron-VE-Direct-Cable-1-8m/dp/B01CPWVTS2>
  - Reason: safer routing margin than a too-short cable for SmartShunt placement.

- **MPPT to Cerbo VE.Direct cable**
  - Buy: Victron VE.Direct cable, `0.3 m / 0.98 ft`, if the MPPT and Cerbo are mounted close enough.
  - Link: <https://www.amazon.com/Victron-VE-Direct-Cable-0-3m/dp/B01F9ESER2>
  - Fallback: buy a longer Victron VE.Direct cable if the final board layout needs routing slack.

- **Optional short VE.Bus/Ethernet patch cable**
  - Buy: `1 ft` Cat6/RJ45 patch cable.
  - Link/search: <https://www.amazon.com/s?k=1+foot+cat6+patch+cable>
  - Use: Cerbo VE.Bus to MultiPlus if not crimping a custom RJ45 cable.

Existing/on-hand reminder: Cerbo power input cable with inline fuse and `2x` VE.Can RJ45 terminators are already accounted for; no CAN bus is currently planned.

### Gravity-fill vent hose

Known interface: gravity-fill vent nipple measured around `10 mm OD` on the main land and about `11 mm OD` at the largest barb/ridge.

- **Preferred hose**
  - Buy: `10 mm ID` food-grade/potable flexible tube.
  - Link/search: <https://www.amazon.com/s?k=10mm+ID+food+grade+silicone+tubing>

- **Common fallback**
  - Buy: `3/8 in ID` food-grade/potable tube; warm the hose if needed to install over the ~`11 mm` barb/ridge.
  - Link/search: <https://www.amazon.com/s?k=3%2F8+ID+food+grade+vinyl+tubing>
  - Stiffer/less kink-prone search: <https://www.amazon.com/s?k=3%2F8+ID+food+grade+braided+PVC+tubing>

- **Clamps**
  - Buy: small stainless hose clamps sized to the installed hose OD, not just the barb OD.
  - Likely search range: `10–16 mm`, but verify against the actual tube OD selected.
  - Link/search: <https://www.amazon.com/s?k=stainless+hose+clamps+10-16mm>

- **Avoid**
  - Do not use the previous `1/2 in ID x 5/8 in OD` tube for this vent nipple; it is too large.
  - `7/16 in ID` is last-resort only and should be clamped and vent/leak checked.

### Diesel heater fuel tank

Posture: not a blocker. Re-measure before buying. Carry-extra-fuel is acceptable until the final tank/service envelope is validated.

- **Possible slim candidate if actual clearance is at least ~3.5 in**
  - Candidate: `10 L / 2.64 gal` stainless parking-heater fuel tank for Webasto/Eberspacher-style heaters.
  - Link: <https://www.amazon.com/Parking-Stainless-Eberspacher-Replacement-Distance/dp/B0G4RP11X8>
  - Planning caveat: prior search suggested no clean off-the-shelf `5–10 gal` tank fits a true ~`17 in x 3 in` opening; the `3 in` depth is the blocker.

- **Decision rule**
  - If measured usable depth is under ~`3.5 in`, skip this class of off-the-shelf tank.
  - If `5–10 gal` is mandatory, expect custom slim tank or alternate mounting.
  - If lower capacity is acceptable, a `10 L` slim tank can remain a candidate.

## TNutz / 80/20 starter-stock list

Ordering posture: stock/prototype material only. Choose **no machining** for the starter extrusion sticks unless a specific module envelope has passed physical mockup.

### Core extrusion

- **15-series main stock**
  - Product: EX-1515L — `1.5 in x 1.5 in` Light Smooth T-Slotted Aluminum Extrusion.
  - Link: <https://www.tnutz.com/product/ex-1515l/>
  - Quantity: `8`
  - Length: `92 in`
  - Fractional length: `0.000 in`
  - Machining: `No machining`
  - Gross length: `61.3 ft`

- **10-series lighter/module stock**
  - Product: EX-1010 — `1 in x 1 in` Smooth T-Slotted Aluminum Extrusion.
  - Link: <https://www.tnutz.com/product/ex-1010/>
  - Quantity: `6`
  - Length: `92 in`
  - Fractional length: `0.000 in`
  - Machining: `No machining`
  - Gross length: `46.0 ft`

- **Starter-stock total**
  - Gross extrusion: `107.3 ft`.
  - Rough extrusion-only price basis observed from TNutz product pages: about `$480` before hardware, shipping, and tax.

### 15-series hardware

- **Corner gussets**
  - Product: CB-015-A — 15 Series 2 Hole Inside Corner Gusset.
  - Link: <https://www.tnutz.com/product/cb-015-a/>
  - Quantity: `12–16`
  - Hardware option: include `5/16-18 x 5/8 in` button-head screws plus compatible T-nuts.

- **Extra economy T-nuts**
  - Product: ET-015 — 15 Series `5/16-18` Economy T-Nut.
  - Link: <https://www.tnutz.com/product/et-015/>
  - Quantity: `50`

- **Drop-in T-nuts for after-assembly changes**
  - Product: DB-015 — 15 / 40 Series Drop-In T-Nut with spring ball.
  - Link: <https://www.tnutz.com/product/db-015/>
  - Quantity: `20`

- **End caps**
  - Product: EC-015 — 15 Series black plastic end cap.
  - Link: <https://www.tnutz.com/product/ec-015/>
  - Quantity: `16–24`

- **Cable-tie drops**
  - Product: AC-015-A — 15 Series 1/4-turn drop-in cable tie.
  - Link: <https://www.tnutz.com/product/ac-015-a/>
  - Quantity: `10`

### 10-series hardware

- **Corner gussets**
  - Product: CB-010-A — 10 Series 2 Hole Inside Corner Gusset.
  - Link: <https://www.tnutz.com/product/cb-010-a/>
  - Quantity: `16–24`
  - Hardware option: include `1/4-20 x 1/2 in` button-head screws plus compatible T-nuts.

- **Extra economy T-nuts**
  - Product: ET-010 — 10 Series `1/4-20` Economy T-Nut.
  - Link: <https://www.tnutz.com/product/et-010-1-4-20/>
  - Quantity: `75`

- **Drop-in T-nuts for after-assembly changes**
  - Product: DB-010 — Drop-In T-Nut with spring ball.
  - Link: <https://www.tnutz.com/product/db-010/>
  - Quantity: `20`

- **End caps**
  - Product: EC-010 — 10 Series black plastic end cap.
  - Link: <https://www.tnutz.com/product/ec-010/>
  - Quantity: `16–24`

- **Cable-tie drops**
  - Product: AC-010-A — 10 Series 1/4-turn drop-in cable tie.
  - Link: <https://www.tnutz.com/product/ac-010-a/>
  - Quantity: `10`

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
- Drawer slides.
- Panel skins.
- Cosmetic trim.
- Large diesel tank.
- Custom/fancy bracket packs beyond starter hardware.

## Validation gates before next procurement round

- Confirm final electrical-board component positions before buying additional exact-length data/communication cables.
- Dry-fit vent hose and clamp; verify no leak and no vent restriction.
- Physically re-measure diesel tank envelope before ordering tank hardware.
- Use the TNutz order for mockup/prototype framing; lock exact cuts only after the real module envelopes and service access pass.
