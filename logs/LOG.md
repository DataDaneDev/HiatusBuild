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
