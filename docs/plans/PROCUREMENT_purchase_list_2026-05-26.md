# Procurement Purchase List — refreshed 2026-05-27

Purpose: short-term buy list for finishing the live-tested electrical board as a hard-mounted, strain-relieved mobile module, plus only the supporting interior/prototype items that should not block that work.

Scope note: this is a purchase aid, not a final cut list. Do not order final extrusion cuts, drawer slides, panel skins, or cosmetic trim from this document alone.

## Priority order

1. MultiPlus programming path and Victron/Cerbo communication cables.
2. Electrical-board hard-mount, protection, labeling, strain-relief, and abrasion-control hardware.
3. Mouser fuse cleanup parts for Orion final `F-06` and WS500 low-current circuits.
4. Gravity-fill vent hose and clamps.
5. Prototype-only 80/20/TNutz stock after electrical-board positions are mechanically proven.
6. Diesel heater tank later, after physical re-measurement.

## Amazon / Victron purchase list

### MultiPlus programming + Victron/Cerbo wiring

- **MK3-USB interface**
  - Buy: Victron `MK3-USB` interface.
  - Use: program/verify MultiPlus LiFePO4 charger settings with VEConfigure before sustained or unattended shore charging.
  - Status: priority purchase; this is the main blocker to treating shore charging as fully commissioned.

- **SmartShunt to Cerbo VE.Direct cable**
  - Buy: Victron VE.Direct cable, `1.8 m / 5.9 ft`.
  - Link: <https://www.amazon.com/Victron-VE-Direct-Cable-1-8m/dp/B01CPWVTS2>
  - Reason: safer routing margin than a too-short cable for SmartShunt placement.

- **MPPT to Cerbo VE.Direct cable**
  - Buy: Victron VE.Direct cable, `0.3 m / 0.98 ft`, only if the final MPPT/Cerbo positions are close.
  - Link: <https://www.amazon.com/Victron-VE-Direct-Cable-0-3m/dp/B01F9ESER2>
  - Fallback: buy a longer Victron VE.Direct cable if final board routing needs slack.

- **Short VE.Bus/RJ45 patch cables**
  - Buy: straight-through Cat6/RJ45 patch cables in `1 ft` and `3 ft` lengths.
  - Link/search: <https://www.amazon.com/s?k=1+foot+cat6+patch+cable>
  - Link/search: <https://www.amazon.com/s?k=3+foot+cat6+patch+cable>
  - Use: Cerbo VE.Bus to MultiPlus and spare short service routing option. Do **not** use the Cerbo LAN port for VE.Bus.

Existing/on-hand reminder: Cerbo power input cable with inline fuse and `2x` VE.Can RJ45 terminators are already accounted for; no CAN bus is currently planned.

### Electrical-board mobile-module cleanup

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
  - Buy: `10 mm ID` food-grade/potable flexible tube.
  - Link/search: <https://www.amazon.com/s?k=10mm+ID+food+grade+silicone+tubing>

- **Common fallback**
  - Buy: `3/8 in ID` food-grade/potable tube; warm the hose if needed to install over the ~`11 mm` barb/ridge.
  - Link/search: <https://www.amazon.com/s?k=3%2F8+ID+food+grade+vinyl+tubing>
  - Stiffer/less kink-prone search: <https://www.amazon.com/s?k=3%2F8+ID+food+grade+braided+PVC+tubing>

- **Clamps**
  - Buy: small stainless hose clamps sized to the installed hose OD, not just the barb OD.
  - Likely search range: `10-16 mm`, but verify against the actual tube OD selected.
  - Link/search: <https://www.amazon.com/s?k=stainless+hose+clamps+10-16mm>

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

- **Orion final `F-06` input fuse cleanup**
  - Buy: Mouser `576-166.7000.5202` Littelfuse FKS/ATO fuse, `20A`, `80VDC`.
  - Buy: Mouser `576-178.6150.0001` Littelfuse ATO/FKS holder, `80VDC` listing owner-confirmed.
  - Priority: cleanup item, not a build blocker; existing `30A 58V` MIDI is acceptable interim protection on the short `6 AWG` Orion input branch.

- **WS500 low-current fuse/holder pieces**
  - Buy only after confirming the harness/manual voltage-rating need: `F-12` regulator power lead baseline `10A` and `F-13` positive voltage-sense lead `3A`.
  - Requirement: holder/fuse voltage rating must cover the actual `48V` bank/alternator maximum unless the supplied harness documentation proves otherwise.

## TNutz / 80/20 posture

Ordering posture: prototype material only. Do **not** buy the old broad `8x 92 in` `15-series` package as a default starter order. Choose **no machining** for any prototype sticks unless a specific measured module envelope has passed physical mockup.

### Better current approach

- Buy or use small `10-series` prototype stock/hardware first for furniture/service-panel mockups.
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
- Solar panels, PV combiner, and PV string fuses until shore/alternator charging are more proven and the roof passthrough/service-loop strategy is reopened.
- Custom/fancy bracket packs beyond prototype hardware.

## Validation gates before next procurement round

- Confirm final electrical-board component positions before buying additional exact-length data/communication cables.
- Program/verify MultiPlus charger settings with MK3/VEConfigure before relying on sustained shore charging.
- Mount the electrical board hardware and verify service access, cable bends, fuse access, covers, labels, and strain relief.
- Dry-fit vent hose and clamp; verify no leak and no vent restriction.
- Physically re-measure diesel tank envelope before ordering tank hardware.
- Use any TNutz order for mockup/prototype framing; lock exact cuts only after the real module envelopes and service access pass.
