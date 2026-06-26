## 2026-06-25 — Current module cut-list workbook filed

- Added the owner-built current best module assignment / garage cut-list workbook at `docs/plans/assets/module-cutlists/2026-06-25_module-cutlist-and-assignments.xlsx`.
- Naming convention going forward: use date-led generic cut-list filenames instead of temporary trigger words like faucet when the artifact is the current overall module/cut-list source.
- Workbook contents were not edited during filing.

## 2026-06-24 — EX-1010 profile interpretation corrected

- Owner confirmed the delivered `23x EX-1010` sticks are regular 4-slot pieces, not tri-slot / one-flat-side `1010-S` extrusion.
- Updated the TNUTZ hardware model note, BOM wording, and current cutlist-derived outputs to remove the stray `1010-S` assumption and normalize those pieces back to regular `1010`.

## 2026-06-24 — Galley sink and faucet purchased

- Owner purchased a FORIOUS black pull-out kitchen faucet with soap dispenser for `$47.99` and a Sarlai black drop-in/workstation sink for `$161.10`; raw order metadata was not copied into the repo.
- Sink dimensions logged: `15 in x 15 in` exterior topmount footprint with approx. `11 in x 13 in` interior basin.
- Added BOM rows `207-208`; generic cabinetry row `87` no longer carries sink/faucet as a catch-all. Current layout note: because the chosen sink is topmount, verify actual cutout, faucet under-counter clearance, drain/graywater path, and any local sink-zone rail/connector drop before final cuts.

## 2026-06-24 — Ninja SP151 microwave-replacement appliance order logged

- Owner ordered an Amazon appliance/tooling support bundle with grand total `$186.19`: Ninja SP151 8-in-1 flip-up air fryer/toaster oven (`1800W`) `$149.95`, GWYXC bamboo cutting-board/topper `$20.99`, GDMINLO 60 in flexible soft tape measure `$3.69`, Amazon Basics 15 in parchment paper `$5.47`, and `$6.09` tax/order remainder.
- BOM row `68` replaced the old compact-microwave placeholder with the purchased Ninja SP151 order group; item/order details were sanitized and no private order metadata was recorded.
- Load model updated to model the Ninja SP151 at `1800W` for short sequenced cooking cycles: `core_workday` now `3,915 Wh/day`, `winter_workday` now `4,829 Wh/day`, and `minimal_idle_day` remains `624 Wh/day`.

## 2026-06-12 — Gates 88.5 in Mechman belt test/spare ordered

- Owner ordered a Gates `K060885` Micro-V serpentine belt, 6-rib, approx. `88.46-88.5 in`, `$28.52`, arriving `2026-06-13`.
- BOM row `206` added as the longer Mechman dual-alternator accessory-belt test/spare; install validation remains pending against tensioner range, belt seating, and no squeal/walk.

## 2026-06-11 — Mechman staged-driving gate closed and WS500 rough-in clarified

- Owner confirmed the alternator noise was the Mechman-supplied idler pulley not being seated properly; after tightening/seating it, the noise went away.
- Mechman confirmed the truck can be driven with the `48V` alternator mechanically installed and unwired/electrically disabled.
- Updated the Mechman/WS500/APM-48 install guide to remove the stale staged-driving support gate and add an alternator-to-bed rough-in bundle map for high-current, WS500 alternator-leg, battery/shunt, temperature-sensor, and cab/control wiring.

## 2026-06-08 — 7.3L single-generator belt routing image saved

- Added the owner-confirmed `7.3L` single-generator belt-routing image to `media/references/mechman-ws500-apm48-install-guide/`.
- Updated the Mechman/WS500/APM-48 install guide with the routing orientation note: image label `A` is closest to the engine, and label `B` is furthest from the engine.

## 2026-06-07 — Mechman/WS500/APM-48 install guide added

- Added `docs/implementation/ELECTRICAL_Mechman_WS500_APM48_install_guide.md` as the detailed shop reference for the Mechman `48V` secondary alternator, Wakespeed `WS500`, Balmar `APM-48`, Ford Upfitter `#3` enable path, staged-install/drivability gates, first-run checks, and fault/shutdown handling.
- Reviewed current official Mechman, Wakespeed, and Balmar online/manual sources alongside local repo PDFs; retained unresolved gates at that time for exact alternator field/ground behavior, WS500 harness polarity, and final profile values. The staged-driving support-confirmation gate was later closed on `2026-06-11` after owner/Mechman confirmation.
- Corrected the active architecture/topology diagrams to show the APM-48 as a parallel surge/load-dump clamp at the alternator `B+`/`B-` or case point, not a series charge-current device.
- Updated repo navigation (`README.md`, `00 Home.md`, `docs/README.md`) and electrical cross-links so the install guide is discoverable from the canonical electrical docs.

## 2026-06-05 — Interior lighting design overwritten with deferred WLED plan

- Replaced the prior `24V`/MiBoxer interior lighting worksheet with a deferred desired `12V` QuinLED/WLED design on `12V-11`.
- Desired design: one QuinLED An-Penta-Deca analog PWM controller, upper CCT white-wash zone, lower RGBCCT night/entry zone, WLED presets, and hardwired momentary buttons for rear/entry, desk/bench, and bed control.
- Updated BOM row `98` and the load-model lighting labels from the old Govee placeholder to the deferred WLED/QuinLED package while preserving the current average-use Wh assumptions until final strip wattage is selected.
- Procurement/install status: intentionally deferred until after plumbing, Starlink, solar, alternator, and core furniture work; preserve rough-in opportunities but do not buy lighting hardware yet.

## 2026-06-03 — 80/20 panel spacer washers purchased

- Owner purchased a `25` pack of black rubber bushing spacer flat washers for 80/20 panel mounting: `3/4 in OD x 1/4 in ID x 1/4 in` thickness, `$10` total / `$0.40` each.
- Planning use: `1/4 in` standoffs/anti-rattle spacers behind `1/2 in` plywood inset/front panels on `10-series` 80/20, producing an effective `3/4 in` panel stack and a cleaner `1/4 in` visual reveal. Not for countertops, shelf load paths, or structural retention by itself.
- BOM row `50` updated from generic planned rubber washers to purchased 80/20 panel spacer washers.

## 2026-06-01 — Amazon order-history BOM reconciliation

- Reconciled `references/amazon_order_history.csv` against `bom/bom_estimated_items.csv` using quantity-extended item subtotals from the export; duplicate embedded CSV header row was ignored.
- Amazon CSV arithmetic: `138` item rows, `$9,266.68` quantity-extended item subtotal, `$9,057.08` mapped into the Hiatus/F-350 BOM, and `$209.60` excluded as non-build/personal/motorcycle/unrelated maintenance/cosmetic.
- Added sanitized audit trail at `bom/amazon_order_history_reconciliation_2026-06-01.md`; raw private order fields were not copied into the report.

## 2026-06-01 — MultiPlus profile verification blocker closed and board finish gate clarified

- Owner clarified that MultiPlus settings were redone and the first battery behaved as planned during shore charging: bulk began, then quickly transitioned to absorption because the battery was already at/near `100%`. No second-battery charge is required just to validate the charger profile.
- Remaining electrical board work is physical closeout: Cerbo is the only major item not hard-mounted; decide any route/sand/seal/paint step before J-clamp strain relief makes teardown more annoying.
- Documentation impact: removed stale "charger profile not verified" blockers while keeping AC-out/GFCI, alternator commissioning, Cerbo mounting, covers, labels, strain relief, and abrasion-control as open gates.

## 2026-06-01 — Mouser Orion F-06 final cleanup stock purchased

- Owner purchased Mouser Orion `F-06` final cleanup stock: `3x` Littelfuse `166.7000.5202` / Mouser `576-166.7000.5202` FKS/ATO fuses (`20A`, `80VDC`) and `3x` Littelfuse `178.6150.0001` / Mouser `576-178.6150.0001` holders (`80VDC` listing owner-confirmed).
- Cost basis: fuses `$7.88` each / `$23.64` extended; holders `$1.51` each / `$4.53` extended; order total `$38.79`, with `$10.62` shipping/tax/remainder over the `$28.17` parts subtotal.
- Allocation: install `1x` fuse/holder for final Orion `48V` input `F-06`; retain `2x` spare fuse/holder sets. Existing `30A 58V` MIDI remains acceptable interim protection on the short `6 AWG` Orion input run until swapped.

## 2026-06-01 — Camper audio system selected and integrated

- Added a camper-only DC-first audio plan, separate from any future truck-cab driving subwoofer system.
- Selected draft package: Kicker `46KMC2` source unit, Kicker `CSC67` `4 ohm` speaker pair, and Kicker `49PTRTP10` powered down-firing 10 in subwoofer with `4 AWG`/`40A` sub branch.
- Added BOM rows `189-193`, deprecated the old row `101` sound-system placeholder, added implementation owner doc `docs/implementation/CAMPER_audio_system.md`, and synchronized electrical overview/fuse schedule, systems, interior placement notes, and tracking.
- Updated `bom/load_model_wh.csv` to model moderate camper-audio use: `core_workday` now `3,794 Wh/day`, `winter_workday` now `4,587 Wh/day`, and `minimal_idle_day` remains `624 Wh/day`.

## 2026-06-01 — Docs/plans closeout and route-map cleanup

- Consolidated TNUTZ/80-20 ownership: detailed WIP cart/visual aids now live in `docs/plans/TNUTZ_80_20_HARDWARE_MODEL_2026-06-01.md`; procurement list is the short summary; `HIATUS_work_plan_2026-05-29.md` is historical/reference only.
- Marked camper audio as preliminary/future-roadmap and changed audio BOM rows `189-193` to deferred/preliminary rather than near-term planned purchases.
- Downgraded the `24V` lighting worksheet to draft/unlikely and kept active lighting architecture on the existing `12V-11` branch until deliberately reopened.
- Corrected AC branch intent: Branch A = office/driver side; Branch B = galley/passenger side.
- Reconfirmed Orion input protection path: standalone `F-06`, current/interim `30A 58V` MIDI, and final cleanup stock now purchased per the Mouser entry above.
- Refreshed route maps/frontmatter and clarified historical install/starter plans so stale plan snippets do not read as current instructions.

## 2026-05-30 — Shore-charge profile settled at 56.8V absorption

- Owner confirmed active MultiPlus charge settings were programmed and shore charging entered bulk, then absorption as expected.
- Settled snapshot: MultiPlus `56.8V`, SmartShunt `56.8V`, charge current `0A` while in absorption, battery display about `55.8V`, and shore input current limit `12A` for the household-source test.
- Owner set SmartShunt SOC to `100%` at this settled full/near-full state. Current go-forward profile remains fixed LiFePO4 with absorption/charge `56.8V`, float `54.0V`, storage `52.8V` if shown, absorption `1h` because the UI allows `1-8h`, repeated absorption `0.25h`, equalization off, temperature compensation off, and `35A` charger current for the full `3x` bank.
- Note on instruments: prior cheap DMM readings were inconsistent/high versus MultiPlus/SmartShunt/battery-display behavior and should not be used as the top-end tuning authority until cross-checked.

## 2026-05-30 — Victron 60A/80V MEGA fuse replacement purchase

- Owner purchased Victron `60A/80V` MEGA fuse 5-pack for MPPT/Orion-output stock: Amazon ASIN `B0F9PKDGWD`, listing/part text `CIP138060020`, observed price `$46.75`.
- Earlier low-cost `60A` MEGA batch (`6x`, two 3-packs at `$4.99` each / `$9.98` total) was owner-confirmed as misadvertised/not actually `58V`; mark as trash/quarantined and do not use on `48V` paths.
- Allocation: install `1x` at MPPT battery-side Lynx Slot 2 / `F-03`; install `1x` at Orion `12V` output / `F-07` if that holder needs a `60A` MEGA; retain `3x` spares. Do not use for MultiPlus `F-02` (`125A`), alternator `F-04` (`150A`), or Orion `48V` input `F-06` (MIDI/FKS/ATO path).

## 2026-05-30 — MultiPlus charge target lowered after top-end BMS trip theory
- Revised active MultiPlus-II commissioning profile for the Dumfume `3x 51.2V 100Ah` bank after live symptoms pointed toward top-end BMS charge protection.
- Key decision: use `56.8V` absorption/charge, `54.0V` float, `52.8V` storage if shown, `0.5h` max absorption, equalization off, temperature compensation off, and `35A` charger current only when all three batteries are paralleled. If testing one battery alone, cap charger current at `20A`.
- Rationale: the Dumfume manual lists `58.4V +/-0.2V` as a charge value but also lists `58.4V` as charge-limit/over-charge protection, leaving no practical voltage margin; the current target keeps the charger below the BMS protection ceiling rather than using the BMS as normal charge termination.
- Live follow-up: owner reported battery screen `53.3V` and `100%` while a cheap DMM showed `55.2V`; treat the battery display/SOC as low-confidence and use the highest credible terminal/bus reading for charger-safety decisions until cross-checked against SmartShunt/MultiPlus readings. VEConfigure UI noted absorption time range `1-8h` and repeated absorption time editable to `0.25h`; set charge curve `Fixed`, minimum absorption time, and repeated absorption `0.25h` for this commissioning profile.

## 2026-05-28 — MultiPlus default screenshot rollback values captured
- Added `docs/core/OPERATIONS.md` rollback reference for the visible MultiPlus-II factory/default values from owner screenshots, plus the active Hiatus programming target for the Dumfume `3x 51.2V 100Ah` bank.
- Key default values preserved for manual reconstruction include charger `57.60V` absorption, `55.20V` float, `8h` max absorption, inverter low-shutdown `37.2V`, `120V` output, PowerAssist `On`, and conditional AC input control `Off`.

## 2026-05-28 — Dumfume battery manual limits and MultiPlus programming baseline captured
- Owner provided live battery-manual values while programming the MultiPlus via MK3: `51.2V 100Ah`, recommended charge voltage `58.4V +/-0.2V`, charge-limit/over-charge protection voltage `58.4V`, recommended charge current `20A`, max continuous charge current `100A`, recommended discharge current `50A`, max continuous discharge current `200A`, over-discharge protection/recovery `36.8V`/`43.2V`, discharge overcurrent protection `600A`, short-circuit protection `1800A`, low-temp charge protection approx `41F-50F` with recovery at `50F`, and high-temp protection `157F`/`140F`.
- Current `3x` bank reference: `60A` recommended charge total and `300A` max continuous charge total; the MultiPlus-II `48/3000/35-50` `35A` charger limit is within that envelope.
- Updated BOM row `3`, `docs/core/SYSTEMS.md`, and `docs/core/ELECTRICAL_48V_ARCHITECTURE.md` so sustained shore charging can be programmed against manual-backed values instead of generic LiFePO4 assumptions.

## 2026-05-27 — Amazon comms/programming and prototype hardware purchase logged
- Owner purchased the immediate Amazon procurement wave; private order/payment/address details were intentionally not copied into public docs. Order subtotal basis for build tracking: `$171.17` before tax (`$183.57` total with estimated tax).
- Build-relevant electrical items purchased: Victron `MK3-USB-C` interface (`$59.44`), VE.Direct cable `5.90 ft` (`$16.31`), VE.Direct cable `2.95 ft` (`$16.13`), and one `3 ft` manufactured RJ45/Ethernet patch cable (`$5.99`).
- Plumbing/interior/support items purchased: `10 mm ID x 13 mm OD` food-grade silicone vent hose/clamp kit (`$10.99`), one Acegoo `118W` 12V USB-C/USB-A PD outlet (`$22.99`), countersunk cup magnets (`$12.34`), magnetic accessory mount (`$9.99`), and steel weld tabs/brackets (`$16.99`).
- BOM/procurement impact: rows `115`, `183`, `184`, `185`, and `186` updated; row `187` added for gravity-fill vent hose/clamps. MultiPlus sustained shore charging remains gated on programming/verification, not merely owning the MK3.

## 2026-05-27 — Repo freshness maintenance after first-live checkpoint
- Refreshed stale top-level and active-plan posture after the first live `48V`/MultiPlus/Cerbo/shore checkpoint.
- Updated procurement guidance to prioritize `MK3-USB`, Victron comms cables, board mounting/strain-relief hardware, Orion final `F-06` cleanup, and WS500 low-current fuse-holder validation.
- Downscoped the old broad `15-series` TNutz starter-stock posture: buy prototype stock only after real module envelopes and service access are proven.
- Marked old temp red-flag files as archived/reference surfaces rather than live trackers, and replaced stale generated `AGENTS.md` skill boilerplate with repo-specific maintenance guidance.

## 2026-05-27 — First 48V/MultiPlus/Cerbo/shore live checkpoint completed
- Owner confirmed `55.5V` throughout the `48V` system, including at the MultiPlus after pre-charge/energization.
- MultiPlus switch `I` brought inverter mode online: inverter light illuminated, slight hum observed, and no error lights reported.
- SmartShunt and Orion-Tr Smart both appeared in VictronConnect. Cerbo GX Wi-Fi access point/remote-console workflow came online; Cerbo power/comms path is `48V` small fused feed plus `VE.Bus` RJ45 to MultiPlus.
- AC Input 1 should be treated/labeled as `Shore power`; household-source test used reduced input-current limit (`10A` first test / `12A` max policy on `15A` outlet).
- Short shore-charge test showed about `1294W` shore input and about `54.3V x 21.6A` (`~1173W`) battery charge in bulk. Treat this as a functional test only until MultiPlus LiFePO4 charge settings are programmed/verified against the Dumfume manual.
- Shutdown practice captured: MultiPlus `O`, disable Orion if needed, de-energize/unplug shore, wait briefly, then open main `48V` disconnect. Residual voltage on Lynx/load side with disconnect open is expected capacitor bleed-down unless it remains stable/current-capable.
- Documentation updated: project/system snapshot, `48V` architecture, topology/fuse schedule, bench guide, AC BOM/checklist, operations quick cards, tracking risks/open questions, and this log.

## 2026-05-25 — Lynx Slot 4 left open; Orion input stays on F-06
- Locked active topology to leave Lynx Slot 4/`F-05` open/blank. Orion `48V` input now uses a Lynx `48V+` bus tap into standalone `F-06`, not an oversized Lynx MEGA fuse.
- Updated active electrical docs/BOM to show `F-06` as the single Orion input fuse: existing `30A 58V` MIDI for build/bench/interim use, planned `20A 80V` FKS/ATO cleanup later.
- Rebased battery-discharge sizing envelope from old `F-02 + F-05 = 165A` to `F-02 + F-06 = 155A` interim / `145A` final, while keeping the existing `2/0` and `200A Class T` posture conservative.

## 2026-05-24 — BOJACK 150A MIDI holder purpose resolved
- BOM/git history shows the BOJACK `150A` AMI/MIDI holder pack was originally purchased for the old Sterling `BB1248120` `12V` input-fuse path.
- Current status: obsolete/spare `12V` hardware only. It is not active Mechman/WS500 alternator protection, not Orion input protection, and not approved for any `48V` role without separate voltage/form-factor validation.
- Updated `bom/bom_estimated_items.csv` row `11` and `docs/core/TRACKING.md` so the part does not get mistaken for board-mounted active fuse hardware.

## 2026-05-24 — Orion input fuse interim/final decision locked
- Owner confirmed Mouser `576-178.6150.0001` holder listing says `80V`; final cleanup buy is Mouser `576-166.7000.5202` (`20A 80V` Littelfuse FKS/ATO fuse) plus Mouser `576-178.6150.0001` (`80V` Littelfuse ATO/FKS holder).
- Current build/interim install will run the existing `30A 58V` MIDI on the short `6 AWG` Orion `48V` input branch. This is acceptable wire protection and does not block bench/build progress.
- Final cleanup target remains `20A` because it matches the Victron Orion manual value; purchase is deferred until the next Mouser order.

## 2026-05-24 — Orion input fuse replacement downscoped
- Corrected the overbuilt `1000VDC` Orion `F-06` recommendation. Practical final target is now a low-cost `20A`, `80VDC` FKS/ATO blade-fuse path, led by Littelfuse `166.7000.5202`, with an ATO/FKS holder that visibly carries an `80VDC` rating.
- Existing `30A 58V` MIDI stock is no longer labeled obsolete: it is acceptable bench/contingency wire protection for the short `6 AWG` Orion input run, but `20A` remains the preferred final value because it matches the Victron Orion manual.
- Superseded by owner confirmation above: Mouser `576-178.6150.0001` listing says `80V`, so the prior holder-rating hold is closed.

## 2026-05-24 — Orion input fuse replacement found (superseded later same day)
- Superseded by the downscoped practical `20A 80V` FKS/ATO path above. Original note: replaced the unresolved Orion `48V` input protection guidance with a concrete buyable class: Eaton Bussmann `PV-20A10F` 10x38 `gPV` fuse (`20A`, `1000VDC`, `50kAIC`) in Eaton Bussmann `CHPV1U`/`CHPV1IU` holder (`30A`, `1000VDC`).
- Historical original note, superseded above: this pass had incorrectly labeled existing `30A 58V MIDI` stock obsolete for final `F-06`; later correction keeps it as current/interim use and row `182` as final 20A 80V cleanup purchase.
- Wire validation remains: planned `6 AWG` Orion `48V` input and `12V` output conductors are conservative for the assumed short electrical-cabinet run.

## 2026-05-24 — Orion input fuse topology reassessment
- Reassessed the Orion `48V` input from scratch after owner noted the separate input fuse may be redundant beside the Lynx fuse.
- Updated active guidance: final topology should use one correctly rated source-side Orion input fuse, preferably Lynx Slot 4 alone if a Lynx-compatible fuse exists at the Orion-required value. Keep separate inline `F-06` only if Lynx cannot be populated with the correct value/rating.
- Follow-up correction: the existing `40A` Lynx stock is not final Orion device protection, and `40A` at Lynx plus `30A` inline should not be treated as the final answer.

## 2026-05-24 — Electrical fuse inventory loose ends
- Captured two active electrical loose ends from owner inventory review:
  - Orion `48V` input protection still targets `20A` per Victron guidance, but purchased `30A 58V MIDI` stock is not the default install value and owner has not found an obvious `48V+` `20A` practical replacement.
  - BOJACK/`150A` hardware purpose is unresolved; it is not assumed to be the active `F-04` alternator fuse, not a WS500 low-current fuse, and not approved for a `48V` role without voltage/form-factor validation.
- Updated `docs/core/TRACKING.md` and `bom/bom_estimated_items.csv` so these do not get lost during fuse-holder/SKU cleanup.

## 2026-05-17 — Pre-install audit triage and cleanup
- Owner triaged `docs/studies/PREINSTALL_FULL_REPO_AUDIT_LIVE_2026-05-16.md` findings F-001 through F-018.
- Closed May 7 travel/tailgate/tonneau logistics as historical; install happened and those items are not active blockers.
- AC baseline confirmed: one purchased `6-way` AC enclosure, two active GFCI outlets/covers, row `111` obsolete, pop-up multipurpose outlet deferred until details are provided, and cable-gland/strain-relief hardware treated as on-hand install-fit stock rather than a design blocker.
- Rechecked battery-branch math: `(125A + 40A) / 3 * 1.5 = 82.5A`; worksheet stale `77.5A` values were updated while PASS voltage-drop result remains materially unchanged.
- Owner confirmed storage placement is too hands-on for prescriptive docs, excess `2/0` cable is on hand for alternator use, a good roll of `14 AWG` duplex marine wire is on hand, and Class T inventory is `3` holders plus `4` slow-blow fuses total.
- Real follow-ups retained: AC dead-checks before energization, WS500 `48V` battery-sense fuse/holder voltage-class validation, final measured run lengths, and solar design deferred until shore and alternator charging are proven.

---
aliases:
  - Hiatus project log
tags:
  - hiatus/log
status: active
related:
  - "[[PROJECT]]"
  - "[[TRACKING]]"
---

# Project Log

Single running log for build progress and test evidence.

## Entry template
- Date:
- Work completed:
- Measurements/data:
- Tests run:
- Issues:
- Next actions:

## 2026-05-16
- AC purchase lock completed after owner purchased the Amazon AC cart. Active Phase 1 AC baseline is now portable `30A` EMS, Camco `TT-30P` to `L5-30R` shore cord, `L5-30` inlet, one combined `6-way` DIN enclosure, `30A` AC-in breaker, `30A` AC-out main breaker, two `20A` AC-out branch breakers, two `20A` GFCI receptacles, `10/3` feeder cable, and `12/3` branch cable.
- BOM updated: rows `13`, `14`, `15`, `41`, `107`, `108`, `109`, `110`, `113`, `114`, and `123` now record the purchased SKUs/prices/status; row `111` is marked obsolete; row `112` remains planned/confirm-on-hand for outlet boxes/covers; new rows `179-181` capture Sikaflex-221, butyl tape, and tire deflators.
- Docs updated: `docs/implementation/ELECTRICAL_AC_BOM.md`, `docs/implementation/ELECTRICAL_overview_diagram.md`, `docs/implementation/ELECTRICAL_bench_layout_and_test_guide.md`, `docs/core/SYSTEMS.md`, `docs/core/PROJECT.md`, `docs/core/TRACKING.md`, and `docs/plans/INSTALL_MINUS_12_READINESS_PLAN.md`.
- PDF exports regenerated for `ELECTRICAL_AC_BOM`, `ELECTRICAL_overview_diagram`, `SYSTEMS`, and `PROJECT`.
- Tests run: CSV parse of `bom/bom_estimated_items.csv`; targeted AC row verification; stale AC-language search excluding historical decision text and regenerated PDF assets; targeted PDF export/mermaid render.
- Issues: outlet boxes/covers are not confirmed in the purchase cart and remain row `112` planned/confirm-on-hand; verify delivered `10/3` jacket markings/listing and physical DIN neutral isolation before drilling/wiring.
- Next actions: receive/inspect parts, update row statuses to `Received`, label the single enclosure layout, and perform AC-in-only MultiPlus charge validation before AC-out branch energization.

## 2026-05-15
- Physical layout photo/mockup received: blue-tape floor envelopes show current installed-camper module layout; cardboard represents the driver-side electrical box and integrated step box; the battery bench area is taped near the bulkhead/front wall; the desk is around the wheel well at about `24 in x 48 in` and integrates with the electrical step box.
- Fridge clarification: fridge remains at the same raised height but should slide deeper into the passenger-side corner.
- Documentation update: added the photo-derived mockup facts as text only; the photo itself was not committed/published.
- Additional photos received: top-down/rear-entry views confirm the Iceco/fridge is being mocked on the passenger-side wheel-well water tank at raised height, pump/accumulator are staged low in the wet-side footprint, the driver-side cardboard electrical/step/desk mass is being checked with a tape measure, and the center aisle remains plausible but margin-sensitive.
- Issues: convert this into a measured block-envelope sketch before exact extrusion lengths; prior photo-read red flags are treated as resolved/non-issues except for keeping a standard wet-tray note in the plumbing plan.
- Next actions: measure datum-to-tape lines, battery extraction path, desk/wheel-well notch, step-box projection, fridge slide/lid/vent sweep, and pump-service opening.

## 2026-05-14
- Owner layout update: the Iceco/fridge is back on the passenger side, raised about `16 in` on an extrusion exoskeleton and slightly overlapping the `36 gal` wheel-well water tank envelope.
- Plumbing update: pump and accumulator move below the fridge in that exoskeleton, next to the water tank, as a separated service bay rather than hidden galley plumbing.
- Battery/bench update: batteries sit adjacent to the pump area in separated enclosures inside an approximately `30 in` tall bench, with a flat divider board above the batteries separating battery space from bench storage; a lid opens the bench and Hiatus bed cushions can cover it when the bed is stowed.
- Driver-side update: electrical panel/closet moves/extends on the driver side up to the `46 in` maximum interior build height, with a shelf/box extending toward the computer desk/camper entry for DC electronics and laptop plugs; diesel heater stays low in this driver-side utility zone.
- Diesel update: investigate an exterior truck-bed-wall diesel tank, ideally around `8 gal` and roughly `3 in x 17 in` envelope if available, with exterior fill/spill exposure, exterior pump, and protected fuel-line pass-through to the heater.
- Docs updated: active layout, systems, tracking, build-order, workstation, and diagram caveats now supersede the rear-left/driver-side fridge references.
- Next actions: physically mock the passenger-side fridge/wet-spine skeleton and battery bench before exact cut lengths; search for an external narrow diesel tank; keep wet/dry and electrical/fuel separation explicit in the service map.

## 2026-05-12
- Owner measurement correction: the water inlet gravity-fill vent nipple measures about `10 mm` OD on the main land and about `11 mm` OD at the largest barb/ridge.
- Planning/procurement impact: the previously ordered `1/2 in ID x 5/8 in OD` food-grade tube is oversized for this nipple. Correct replacement target is `10 mm ID` food-grade/potable tube, with `3/8 in ID` as the common inch fallback and `7/16 in ID` only as a looser clamp-required fallback.
- Docs updated: `docs/implementation/INTERIOR_furniture_layout_and_galley.md`, `docs/core/SYSTEMS.md`, `docs/core/TRACKING.md`, and `bom/bom_estimated_items.csv`.
- Next action: dry-fit replacement vent hose with clamp, check for kinks/vent restriction, then re-check after first fill/drive cycle.

## 2026-05-11
- Owner update: general interior layout is physically blocked in. Gravity fill passthrough, `36 gal` wheel-well water tank, cooler/fridge, likely butcher-block desk, pump/accumulator, PEX routing, `3x 48V` batteries, `1x 12V` battery, diesel heater, and diesel tank all appear to fit the expected zones.
- Owner update: subfloor is done; sheet vinyl/Lonseal will remain unglued for now to avoid damage and preserve rough-in/floor-access flexibility.
- Planning impact: broad `15-series` extrusion is further downscoped because the water tank bolts/restraints should use the truck-bed/camper structure directly if dry-fit validates the load path. Default extrusion posture is now `10-series`/light rail/plywood/direct mount unless a measured heavy/dynamic module proves `15-series` is needed.
- Electrical status: components are laid out on plywood but not connected, drilled, or energized. Next electrical action is labeled mechanical layout/backer-board templating, not final wiring.
- Diesel status: larger diesel tank is a want, not a blocker; carry-extra-fuel remains acceptable until the final tank/service envelope is validated.
- Next actions: finish electrical backer-board template pass, validate `10-series` prototype/module needs from taped block envelopes, keep vinyl glue-down gated, and bench-build/pressure-test wet-spine plumbing as a removable service cassette before final cabinetry.

## 2026-05-04
- Designed the driver/left-side workstation mechanism package for full-time work use while preserving pop-down roof clearance.
- Added `docs/implementation/INTERIOR_driver_side_workstation.md` as the draft implementation owner for the service-spine desk, stow-low/rising VESA monitor mechanism, Iceco/fridge tower storage, toe-kick false bottom, shallow cubbies, travel locks, cable drag-chain/service loops, heat/noise/venting, and acceptance tests.
- Updated `docs/core/SYSTEMS.md`, `docs/core/TRACKING.md`, and `docs/README.md` so the new workstation implementation is discoverable and tracked without treating stale CAD as final.
- Measurements/data: no new physical camper measurements; calculated reference envelope for a `27 in` 16:9 monitor as about `23.5 in W x 13.2 in H` and used `27-40 in` as a practical viewing-distance target range.
- Tests run: documentation cross-link and markdown consistency pass; no physical roof-cycle or travel test performed yet.
- Issues: final monitor mechanism, desk dimensions, Iceco slide need, latch hardware, and roof-safe line remain measurement-gated after camper install.
- Next actions: perform roof-down sweep map, Iceco lid/vent/cord envelope, seated work mockup, then bench-test the selected monitor mechanism before exact extrusion cuts.

- Added the office-first interior furniture and galley concept baseline.
- Added `docs/implementation/INTERIOR_furniture_layout_and_galley.md` as the draft owner for the top-left power stair battery bench, top-right soft storage/cabover landing bench, driver-side desk/rear-left Iceco utility block, passenger-side galley wet spine over the `36 gal` tank, rear service hatch, cold-first plumbing, and future hot-water readiness.
- Added generated concept diagrams under `media/diagrams/interior-furniture-2026-05-04/` and linked the preferred diagrams from the implementation docs.
- Updated `docs/core/PROJECT.md`, `docs/core/SYSTEMS.md`, `docs/core/TRACKING.md`, `docs/plans/PROJECT_build_order_of_operations.md`, `docs/plans/INSTALL_MINUS_12_READINESS_PLAN.md`, `docs/plans/STARTER_PLAN_electrical_and_flooring_pre_camper.md`, and `docs/README.md` so the furniture/galley concept is discoverable without treating generated art or stale fridge CAD as fabrication geometry.
- Measurements/data: no new physical camper measurements; preserved planning references that `36 gal` water is about `300 lb` before tank/brackets/plumbing and should be treated as `320+ lb` installed when full.
- Tests run: generated diagram review, documentation cross-link review, and git diff review; no physical roof-cycle, tank dry-fit, plumbing pressure test, or seated workday mockup performed yet.
- Issues: generated diagrams are concept aids only; galley/fill/vent/drain routing, hot-water choice, fridge envelope, monitor kinematics, and roof-safe line remain measurement-gated.
- Next actions: measure the installed camper, dry-fit the tank/fridge/electrical/desk blocks, validate the wet-spine service cassette, then lock only the extrusion and slide lengths proven by the mockup.

## 2026-05-01
- Owner correction: this is the Washington trip, not a washing trip. Bed will be emptied before departure; existing removable flooring will be removed before departure and does not need to be brought along.
- Tailgate removal is optional for access/drying, with wiring/camera protection if removed.
- Updated weekend order-of-operations and flooring implementation notes to keep flooring out of the wet/adhesive rail-seal work zone and wait for sealant cure/tack timing before reinstalling or handling surfaces.
- Owner update: purchased a `36 gal` wheel-well water tank instead of the prior tall/skinny vertical tank concept.
- Planning impact: the broad `15-series` extrusion exoskeleton/starter order is no longer justified by tank restraint alone; downscope extrusion to targeted module needs after physical dry fit, while verifying tank bracket/plusnut and any secondary restraint load path.

## 2026-04-25
- Status correction from owner: Mechman `48V` alternator has been purchased.
- Interpretation: dedicated `48V` secondary-alternator architecture remains the active baseline; remaining alternator blockers should be narrowed to received-kit fitment/content, support details, harness polarity, isolation/grounding behavior, load-dump mitigation, and commissioning validation rather than pre-purchase architecture selection.
- Updated `docs/core/PROJECT.md`, `docs/core/TRACKING.md`, and `docs/plans/STARTER_PLAN_electrical_and_flooring_pre_camper.md` to reflect purchase status while preserving Sterling return as gated on received-kit/fitment/support confirmation.
- Follow-up owner status: Mechman kit appears fit-compatible and has been received; Balmar `APM-48` has been received.
- Sequencing correction: defer alternator installation until the `3x 48V` battery bank exists and shore charging/monitoring is ready.
- Near-term priority: solve shore power because it is the intended initial charge path for the three house batteries.
- Added `docs/plans/INSTALL_MINUS_12_READINESS_PLAN.md` to focus the 12-day pre-Washington window on shore-charge readiness and extrusion/furniture-start procurement.

## 2026-03-20
- Consolidated the finalized `48V` architecture into one canonical file:
- Added `docs/core/ELECTRICAL_48V_ARCHITECTURE.md` to hold the locked house-bank, alternator, shutdown, and control-path decisions.
- Locked the manual alternator-control baseline:
- Ford `Upfitter Switch #3 -> F-15 3A inline fuse -> WS500 brown ignition/enable wire`
- `WS500` white `Feature-In` left reserved for future automatic interlock work.
- Updated implementation docs to carry the same control path and fuse:
- `docs/implementation/ELECTRICAL_overview_diagram.md`
- `docs/implementation/ELECTRICAL_fuse_schedule.md`
- Updated repo entry points and canonical references:
- `README.md`
- `docs/README.md`
- `docs/core/SYSTEMS.md`
- `docs/core/PROJECT.md`
- `docs/plans/STARTER_PLAN_electrical_and_flooring_pre_camper.md`
- Updated operations/tracking to reflect the new shutdown order and consolidation:
- `docs/core/OPERATIONS.md`
- `docs/core/TRACKING.md`
- Updated temporary/history docs so they no longer present the old Sterling path as current:
- `docs/temp/TEMP_electrical_red_flags.md`
- `docs/studies/ELECTRICAL_48V_dual_alternator_trade_study.md`
- Updated BOM for the finalized alternator-control baseline:
- corrected active cable-note references in rows `28` and `29`
- clarified row `168` kit assumptions
- clarified row `171` scope
- added row `176` for the `WS500` Upfitter `#3` enable wiring kit
- Regenerated the updated PDF exports:
- `docs/pdf_exports/ELECTRICAL_48V_ARCHITECTURE.pdf`
- `docs/pdf_exports/ELECTRICAL_overview_diagram.pdf`
- `docs/pdf_exports/ELECTRICAL_fuse_schedule.pdf`
- `docs/pdf_exports/SYSTEMS.pdf`
- `docs/pdf_exports/PROJECT.pdf`
- Measurements/data: no physical measurements added in this pass; `C-41` control-wire length remains an install-time measured value.
- Tests run: documentation consistency pass across core docs, implementation docs, and BOM row mapping.
- Issues: vendor confirmation gates remain open for exact Mechman kit content, `PH/NH` harness polarity, supported Dumfume battery behavior, and alternator isolation details.
- Next actions: confirm vendor gates, measure and record the final `C-41` upfitter-to-WS500 control-wire run, and close measured-length updates in the implementation docs during install layout.

## 2026-03-18
- Ran a full project-maintenance documentation pass and synchronized health/planning/tracking/procurement docs with current field progress.
- Captured completed vehicle electronics integration:
- Garmin Tread 2 hardwired and mounted (`$50` Garmin motorcycle mount/hardwire kit + `$20` RAM arm + `$75` BuiltRight dash mount; Garmin unit already owned).
- Captured flooring execution progress and stack revision:
- EPS cut and installed between truck bed ribs.
- Removed EPDM/RPDB thermal-break layer from active stack.
- Locked active floor path to bedliner -> EPS between ribs -> `3/4 in` birch subfloor -> marine sheet vinyl.
- Captured new material purchases:
- `2x` `4x8` `3/4 in` birch plywood (`$88` each, `$176` total).
- `1x` `4x8` `1/2 in` plywood (`$68`) for electrical backer/closet module.
- Captured major Harbor Freight tooling purchase and related additions (total noted from provided line items: `$1,622`):
- Tool cart, Apex/Badlands winch, Bauer 6-tool combo, orbital sander, router, jigsaw, jigsaw blades, extra `20V 5Ah` battery, router bit kit, sanding discs, kneeling pad, super glue pack, step bits, epoxy, `2-yr` HF membership, Ryobi `10 in` sliding miter saw, and lifetime table.
- Captured installer scope change:
- Added `$50` upcharge for installer-provided `12-circuit` Blue Sea fuse panel (instead of `6-circuit`), while retaining owner-purchased budget `12-circuit` panel for bench/prototype use.
- Captured electrical workflow change:
- Retired CAD-gated run-length expectation and moved to bench-layout-first measured cut-length process.
- Captured planning posture updates:
- AC protection chain baseline retained, but final branch utilization/receptacle count is reopened for closure.
- Solar procurement/final sizing intentionally deferred deeper in build; flexible path remains active direction under `75 lb` cap.
- Measurements/data: no new electrical performance testing in this pass (documentation and procurement-state synchronization only).
- Tests run: consistency pass across updated docs and BOM row checks for updated/new rows.
- Issues: AC scope finalization and measured run-length record location still open.
- Next actions: close AC count/SKU lock, complete measured run-length capture from bench layout, then execute cable closeout procurement.

## 2026-03-15
- Researched a possible alternator-charging architecture change from the current Sterling `BB1248120` path to a Mechman/Wakespeed `48V` secondary-alternator system for the `2021` `F-350` `7.3L`.
- Added the battery manual and exact battery data for the current house bank:
- `references/Dunfume_36V_48V_100Ah_Battery_-_User_Manual.pdf`
- Updated the battery row in `bom/bom_estimated_items.csv` to identify the Dumfume `51.2V 100Ah` battery and capture manual-backed charge/parallel specs.
- Added a new supporting study:
- `docs/studies/ELECTRICAL_48V_dual_alternator_trade_study.md`
- Added a cross-link from `docs/core/SYSTEMS.md` so the new study is discoverable from the canonical electrical doc map.
- Added new open questions in `docs/core/TRACKING.md` focused on:
- Wakespeed support status for the internal-BMS, non-CAN battery bank
- required load-dump / avalanche-diode mitigation for a direct `48V` alternator path
- whether the Mechman `48V` system can remain electrically isolated from chassis as desired
- whether the retained factory alternator continues to handle starter/vehicle charging independently if Sterling hardware is removed
- Key findings from this research pass:
- Mechman publishes a real `2020+` `7.3L` Godzilla dual-alternator bracket path that retains the factory alternator and adds a second alternator.
- The `48V` Mechman/Wakespeed architecture has real performance upside over the current Sterling `~1.5 kW` ceiling.
- The Dumfume manual materially improved battery-side clarity: `58.4V` charge voltage, `20-50A` recommended charge current per battery, and `1S4P` max expansion mean the current `1S3P` bank looks current-compatible with the Mechman output curve on paper.
- The main remaining uncertainty is not raw charge-current acceptance; it is battery support and protection strategy with an internal-BMS, non-CAN `48V` bank.
- User confirmed that losing automatic house-to-starting-battery support is acceptable, so that feature is no longer a decision blocker in the alternator trade study.
- Current recommendation remains to keep Sterling as the active baseline and not return that hardware until the Mechman/Wakespeed battery-support and protection questions are explicitly closed.
- Measurements/data: source review only; no bench or vehicle tests performed.
- Tests run: document/source verification only.
- Issues: official Wakespeed support status for the documented Dumfume battery is still unresolved.
- Next actions: send the updated targeted vendor questions captured in the trade study to Mechman, Wakespeed, and the battery manufacturer.

## 2026-02-16
- Updated procurement sequencing to an accelerated `Batch A+` phase so the electrical bench build can start without waiting for later cable/consumable waves.
- Updated `bom/bom_estimated_items.csv` purchase windows:
- `2026-02-16`: rows `3`, `12`, `18`, `20`, `22`, `23`
- `2026-02-17`: rows `4`, `5`, `6`, `7`, `10`, `11`, `16`, `17`, `26`, `27`
- `2026-02-18`: rows `52`, `53`, `60`
- `2026-02-19`: rows `28`, `29`, `30`, `31`, `32`, `33`
- `2026-02-20`: rows `34`, `35`, `36`, `37`, `38`, `39`, `40`, `41`
- `2026-02-21`: rows `42`, `43`, `44`, `45`
- Restored missing BOM row `122` as a placeholder interior procurement line item for drawer-slide kits so canonical row references remain coherent.
- Synchronized planning/governance docs:
- `docs/plans/PROJECT_build_order_of_operations.md` updated from `Batch A` to `Batch A+` and adjusted downstream batch scope.
- `docs/core/PROJECT.md` sequencing baseline updated to `2026-02-16` with active `Batch A+` note.
- `docs/core/TRACKING.md` updated with decisions `D-019` and `D-020`.
- Measurements/data: none captured (documentation/procurement-plan update only).
- Tests run: row-level verification of targeted BOM date updates (`37` checks, `0` mismatches).
- Issues: initial BOM write attempt was blocked by a temporary file lock; write succeeded after lock release.
- Next actions: convert planned purchase dates to actual ordered status with vendor + ETA per row and identify any SKU substitutions before harness fabrication.

## 2026-02-15
- Performed integrated safety deep-dive for the current architecture with focus on the `48V 10.24kWh` system plus `12V`, `120VAC`, and propane paths.
- Expanded `docs/core/SYSTEMS.md` `## Safety` from placeholder bullets to a build-ready baseline covering:
- system-wide controls and isolation/access principles
- `48V` high-fault-current hazard controls and commissioning checks
- `12V` distribution protections and Orion headroom safety trigger
- `120VAC` protection-chain and commissioning test requirements
- propane rear-mount/passthrough controls and indoor water-heater selection rule
- emergency shutdown order and pre-close safety hold points
- Updated governance in `docs/core/TRACKING.md`:
- Added decision `D-015` (consolidated safety baseline adoption)
- Added risks `R-007` (`48V` arc/thermal fault exposure), `R-008` (propane/CO exposure), and `R-009` (AC neutral-ground/GFCI protection risk)
- Added open questions to lock propane heater listing/venting path, passthrough hardware rules, leak-test cadence, and detector/extinguisher layout.
- Added operations-ready checklist content in `docs/core/OPERATIONS.md`:
- pre-energization checks
- propane-specific checks
- incident-response quick actions
- Measurements/data: none captured in this documentation pass.
- Tests run: none (documentation update only).
- Issues: final propane appliance path and venting method remain unresolved and now explicitly tracked.
- Next actions: convert safety hold points to dated commissioning test records during wiring and gas-system validation.

## 2026-02-13
- Ran PRF-003 research sweep focused on AC distribution right-sizing for the current truck-camper architecture.
- Reviewed current project AC assumptions in:
- `bom/bom_estimated_items.csv` (rows `13`, `14`, `15`, `67`, `68`)
- `bom/load_model_wh.csv` (owner-supplied office AC-path assumptions)
- `docs/implementation/ELECTRICAL_overview_diagram.md` (shore + inverter AC topology)
- Quantified modeled AC-related energy share at roughly `27.9%` (`core_workday`) to `30.7%` (`winter_workday`) for current assumptions.
- Updated `docs/temp/TEMP_procurement_red_flags.md` PRF-003 to:
- Separate "AC safety requirements" from "panel size/mounting method" assumptions.
- Add confirmed Phase 1 AC load list and right-sized architecture options.
- Document that DIN rail is optional pending final enclosure choice.
- Keep PRF-003 open until AC topology lock and SKU lock are complete.
- Expanded `docs/implementation/ELECTRICAL_overview_diagram.md` AC section from high-level path to full hierarchy:
- Shore-source path, MultiPlus transfer/charger behavior, AC-out branch strategy, optional AC-out-2 handling, and USB-C PD strategy.
- Added AC operating-behavior notes, protection-chain requirements, procurement gap checklist, and detailed AC conductor-segment entries (`C-28` through `C-35`).
- Added new tracking open questions in `docs/core/TRACKING.md` for shore-interface lock (`15A` vs `30A`) and USB charging path lock (DC USB-C PD vs AC USB receptacles).
- Locked Phase 1 AC/USB baseline for procurement:
- AC-out-1 split into two branches (`20A` galley + `15A` office) with `4` total `120V` receptacle locations (`2` galley, `2` office).
- USB charging baseline locked to `4` DC-fed USB-C PD points (`2` office + `2` galley) on dedicated `12V` branches.
- Updated `bom/bom_estimated_items.csv`:
- Refined rows `13`, `14`, `15`, and `17`.
- Added rows `107-118` for shore interface, AC enclosure/protection, receptacle hardware, AC wire scope, USB-C PD hardware, and optional 12V-converter expansion path.
- Set USB-C PD zone design intent to two `10A` fused `12V` branches (office + galley) to keep demand aligned with current Orion headroom assumptions.
- Updated `docs/implementation/ELECTRICAL_overview_diagram.md` and `docs/implementation/ELECTRICAL_fuse_schedule.md` to map AC branches and USB-C PD branch circuits to the locked baseline.
- Added decision `D-013` in `docs/core/TRACKING.md` and replaced prior AC architecture open questions with a SKU-lock follow-up item.

## 2026-02-12
- Built RF-003 decision support for power-distribution topology in `docs/core/SYSTEMS.md`:
- Compared `DIY discrete` vs `Lynx one-module` vs `Lynx two-module`.
- Listed required component groupings for each topology.
- Added planning-level cost deltas using current BOM rows plus explicit Lynx price assumptions.
- Added clear decision rule for whether `1` Lynx is sufficient or when `2` is justified.
- Updated `docs/temp/TEMP_electrical_red_flags.md` RF-003 references and status to `Open (decision-ready)`.
- Added high-level electrical architecture draft in `docs/implementation/ELECTRICAL_overview_diagram.md` using a topology-only Mermaid diagram.
- Linked the new diagram from `docs/core/SYSTEMS.md` and indexed it in `docs/README.md`.
- Kept this revision intentionally free of fuse/disconnect/wire-gauge details pending final topology lock.
- Performed full electrical-system sweep for fuse/holder/gauge consistency:
- Corrected Sterling `BB1248120` spec basis from `120A @ 48V` assumption to `~1500W` max output (`~26A` at `57.6V`) in `bom/bom_estimated_items.csv` and `docs/core/SYSTEMS.md`.
- Recalculated alternator charging replacement-time assumptions in `docs/core/SYSTEMS.md`.
- Replaced `docs/implementation/ELECTRICAL_overview_diagram.md` with implementation-level topology including all major components, fuse holders, and conductor schedule.
- Reworked `docs/implementation/ELECTRICAL_fuse_schedule.md` to include full fuse housing methods, branch gauge tie-ins, and sweep findings.
- Added decision `D-012` in `docs/core/TRACKING.md` and closed new red flag `RF-008` in `docs/temp/TEMP_electrical_red_flags.md`.

## 2026-02-11
- Workspace structure simplified and consolidated for lower documentation overhead.
- Canonical docs reduced to four core files in `docs/`.
- Imported and dissected `Camper Build.xlsx` into AI-friendly artifacts.
- Added normalized BOM exports:
- `bom/bom_estimated_items.csv`
- `bom/bom_misc_items.csv`
- `bom/load_model_wh.csv`
- `bom/bom_summary.json`
- Added CAD-friendly layout exports:
- `cad/drawings/layout_1_annotations.csv`
- `cad/drawings/layout_1_fills.csv`
- `cad/drawings/layout_2_annotations.csv`
- `cad/drawings/layout_2_fills.csv`
- Extracted workbook-embedded media:
- `media/inspiration/workbook_import/` (non-layout images)
- `cad/drawings/workbook_import/` (layout-sheet images)
- `media/inspiration/workbook_import/manifest.json` maps source sheet to extracted files.
- Updated canonical docs (`docs/core/PROJECT.md`, `docs/core/SYSTEMS.md`, `docs/core/OPERATIONS.md`, `docs/core/TRACKING.md`) and `bom/BOM.md` with workbook-derived content.
- Added maintained electrical capacity and charging reference to `docs/core/SYSTEMS.md` with:
- Scenario-based usage models aligned to remote-office goals.
- Battery autonomy math (`100%->0%` and `100%->20%` reserve floor).
- Solar, alternator, and shore charging potential tables.
- Formula block and update workflow for future recalculation.
- Updated `docs/core/TRACKING.md` with:
- Decision D-003 (canonical maintained electrical model).
- Risk R-004 (inverter overload risk from simultaneous high-draw AC loads).
- Performed full electrical model reset from BOM source of truth:
- Temporary battery interpretation was set to `2x 51.2V 400Ah LiFePO4` (later corrected same day).
- Replaced `bom/load_model_wh.csv` with BOM-derived model v2 (`core_workday`, `winter_workday`, `minimal_idle_day`).
- Recalculated `docs/core/SYSTEMS.md` capacity, autonomy, and charging potential from BOM-derived values.
- Added tracking updates:
- Decision D-004 (retire workbook WH model, BOM-only model).
- Risk R-005 (later revised after battery capacity correction).
- Corrected battery capacity interpretation after follow-up clarification:
- Installed bank is `2x 48V 100Ah` (not `2x 400Ah`).
- `400Ah` is treated as max 4-battery system capability, not installed capacity.
- Updated `bom/bom_estimated_items.csv` battery row and recalculated `docs/core/SYSTEMS.md` capacity/autonomy/shore-recharge numbers.
- Updated `docs/core/TRACKING.md` with Decision D-005 and revised Risk R-005 to reflect reduced no-charge autonomy.
- Reviewed electrical model for winter-fridge and solar-assumption accuracy:
- Updated `bom/load_model_wh.csv` winter fridge from `55%` to `40%` duty-cycle assumption.
- Recalculated winter conversion-loss row and total from `3,181 Wh/day` to `3,003 Wh/day`.
- Updated `docs/core/SYSTEMS.md` with:
- revised winter DoD/autonomy/charging replacement times,
- a dedicated `20%` minimum SOC reserve-floor framing for autonomy,
- and a `900W` flexible `3S3P` solar derate model (base `68%`, sensitivity `60%-75%`).
- Updated `docs/core/TRACKING.md` with Decision D-006 and follow-up validation action for measured fridge/solar logs.
- Resolved RF-001 policy mismatch for owner-supplied office electronics:
- Kept owner devices out of BOM procurement cost tracking.
- Added explicit owner-supplied load rows (laptop, 27 inch 1440p monitor, tablet/peripherals) to `bom/load_model_wh.csv` model v3.
- Recalculated `docs/core/SYSTEMS.md` load totals, autonomy, and charging replacement times against model v3.
- Updated `docs/core/TRACKING.md` with Decision D-007 and refreshed load/risk/open-question entries.
- Marked `docs/temp/TEMP_electrical_red_flags.md` RF-001 as closed pending measured validation.
- Swapped alternator charging architecture to Sterling:
- Updated `bom/bom_estimated_items.csv` row `18` to Sterling `BB1248120` (`$807`) and added row `26` for Sterling `BBR` remote (`$108`).
- Updated BOM rollups in `bom/BOM.md` and `bom/bom_summary.json` (current estimated total now `$45,879.64`; Power System subtotal `$5,041.00`).
- Reworked alternator charging math in `docs/core/SYSTEMS.md` for Sterling nameplate, `65%` remote-limited output, and a practical `240A` alternator planning cap.
- Added decision D-008 in `docs/core/TRACKING.md` and closed RF-002 in `docs/temp/TEMP_electrical_red_flags.md`.
- Added purchase-later vehicle charging upgrade path:
- Added JS high-output alternator (`$548`) and Big 3 wiring estimate (`$225`) to `bom/bom_estimated_items.csv`.
- Added Big 3 note to existing 2/0 cable row to indicate gauge compatibility and expected extra length when upgrade is activated.
- Updated BOM rollups (`bom/BOM.md`, `bom/bom_summary.json`) to total `$46,652.64` with `102` estimated line items.
- Updated planning docs (`docs/core/SYSTEMS.md`, `docs/core/PROJECT.md`, `docs/core/TRACKING.md`, `docs/temp/TEMP_electrical_red_flags.md`) with staged stock-alternator-first strategy and purchase-later fitment/spec lock actions.
- Swapped purchase-later alternator candidate from JS to Mechman 370A (SKU `11532370`) at `$599`.
- Re-synced BOM rollups after price/model swap (current CSV total `$46,703.64`; Power System subtotal `$5,640.00`; `102` estimated line items).
