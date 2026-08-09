---
aliases:
  - Hiatus tracking
tags:
  - hiatus/core
  - hiatus/tracking
status: active
related:
  - "[[PROJECT]]"
  - "[[SYSTEMS]]"
  - "[[OPERATIONS]]"
  - "[[LOG]]"
---

# Tracking

## Document role
- This file owns decision status, risk status, assumptions, and open questions across the project.
- Update the owning canonical doc first when a design or process changes, then record the status change here.
- Do not use this file as the full architecture source or the full procedure source; point back to the owner docs for that detail.
- Use `logs/LOG.md` for dated execution evidence and measured outcomes; use this file for the durable interpretation of what remains open, risky, or decided.

## Assumptions and constraints
- Constraints: truck/camper/dates are fixed constants
- Assumptions to validate: autonomy target, climate profile, load profile, travel cadence impacts
- Electrical run-length policy: physical bench-layout measurements are the primary cut-length source; CAD values are reference-only.
- Working load baseline assumption from load model v5 (BOM + owner-supplied office loads + conservative preliminary/future camper-audio allowance):
- `core_workday`: `3,915 Wh/day`
- `winter_workday`: `4,829 Wh/day`
- `minimal_idle_day`: `624 Wh/day`

## Decision log
- ID: D-001
- Date: 2026-02-11
- Decision: Use workbook `WH` load model as baseline planning input until measured data is available.
- Context: Legacy workbook had a complete daily Wh model; canonical docs had placeholders.
- Options considered: Keep placeholder only or import model now.
- Decision drivers: Better architecture sizing and faster procurement decisions.
- Result: Baseline set to `3,790 Wh/day` and documented in `docs/core/SYSTEMS.md`.
- Follow-up: Superseded by D-004 BOM-derived model reset.

- ID: D-002
- Date: 2026-02-11
- Decision: Keep Phase 1 house system centered on 48V architecture.
- Context: Workbook BOM and notes consistently reference 48V battery, inverter, and charging path.
- Options considered: Full 12V architecture, mixed architecture, 48V core with DC step-down.
- Decision drivers: Efficiency, inverter support, and existing BOM momentum.
- Result: 48V remains default architecture pending final component lock.
- Follow-up: Superseded by D-028/D-029 alternator-migration baseline and WS500 commissioning validation gates.

- ID: D-003
- Date: 2026-02-11
- Decision: Maintain a single electrical capacity and charging reference in `docs/core/SYSTEMS.md`.
- Context: Build decisions depend on fast re-calculation of load, autonomy, and charge-source coverage as components change.
- Options considered: Keep analysis ad hoc in chat notes, create separate analysis docs, or keep one maintained canonical section.
- Decision drivers: Traceability, low overhead updates, and consistency with canonical-doc workflow.
- Result: Added maintained electrical model section with formulas, scenario table, and update workflow in `docs/core/SYSTEMS.md`.
- Follow-up: Recompute after any BOM power-component change or measured duty-cycle update.

- ID: D-004
- Date: 2026-02-11
- Decision: Retire workbook-derived `WH` load assumptions and rebuild the electrical model from BOM componentry only.
- Context: Previous model inputs were stale and no longer represented the current build configuration.
- Options considered: Patch old model values or perform a full model reset from BOM rows.
- Decision drivers: Data integrity, repeatability, and alignment with BOM-as-source-of-truth workflow.
- Result: `bom/load_model_wh.csv` replaced with BOM-derived model v2 scenarios and `docs/core/SYSTEMS.md` recalculated from those values.
- Follow-up: Superseded by D-007 owner-supplied office-load modeling policy.

- ID: D-005
- Date: 2026-02-11
- Decision: Correct battery interpretation to `2x 48V 100Ah` and treat `400Ah` as max 4-battery system capability (not installed capacity).
- Context: A temporary documentation update incorrectly modeled installed capacity as `2x 400Ah`.
- Options considered: Keep oversized model or correct to installed battery count and capacity.
- Decision drivers: Accuracy of autonomy and charging predictions.
- Result: BOM battery row and all capacity/autonomy calculations were corrected in `docs/core/SYSTEMS.md`.
- Follow-up: `2026-02-12` convention locked: keep `48V` as system label and use `51.2V` nominal for battery Wh accounting.

- ID: D-006
- Date: 2026-02-11
- Decision: Adjust winter fridge duty-cycle assumption downward and model `900W` flexible solar with explicit derate factors.
- Context: Prior `winter_workday` model set fridge duty higher than core profile without supporting evidence, and solar estimates used one generic efficiency factor.
- Options considered: Keep prior assumptions, tweak only fridge duty, or update both fridge and solar methodology.
- Decision drivers: Reduce avoidable model bias and align with expected flexible-panel real-world behavior.
- Result: `winter_workday` load updated to `3,003 Wh/day`, and `docs/core/SYSTEMS.md` now uses a flexible-array planning base of `68%` efficiency with `60%-75%` sensitivity.
- Follow-up: Validate fridge duty cycle and daily solar harvest against Cerbo/SmartShunt logs after shakedown.

- ID: D-007
- Date: 2026-02-11
- Decision: Keep owner-supplied work electronics out of BOM cost tracking while including them in canonical Wh load modeling.
- Context: Laptop, monitor, tablet, keyboard, and mouse are already owned and should not inflate procurement BOM totals, but excluding them materially understates real daily energy demand.
- Options considered: Add owner gear to BOM, keep excluding owner gear from the model, or model owner gear separately from BOM pricing.
- Decision drivers: Accurate autonomy/charging analysis without polluting procurement cost accounting.
- Result: Added owner-supplied office-load rows to `bom/load_model_wh.csv` model v3 and recalculated `docs/core/SYSTEMS.md` capacity/autonomy/charging tables.
- Follow-up: Replace planning assumptions with measured device-level energy data from real workdays.

- ID: D-008
- Date: 2026-02-11
- Decision: Historical/obsolete alternator-charger architecture freeze.
- Context: Prior BOM/docs left alternator charging open and recovery-time math ambiguous.
- Options considered: earlier DC-DC alternator-charging variants that are no longer part of active planning.
- Decision drivers: Historical charge-rate and control assumptions before the dedicated `48V` secondary alternator decision.
- Result: Superseded by D-028/D-030 and removed from active fuse/layout planning.
- Follow-up: Historical traceability only; do not use for procurement, fusing, or board layout.

- ID: D-009
- Date: 2026-02-11
- Decision: Add Mechman 370A alternator and Big 3 wiring as explicit purchase-later BOM items while keeping stock-alternator-first operation.
- Context: Historical/superseded. Extended-idle use cases were being evaluated before the dedicated `48V` secondary alternator path replaced the single-12V upgrade concept.
- Options considered: Keep no-upgrade path only, add alternator only, add alternator plus Big 3 wiring scope.
- Decision drivers: Planning transparency, safer high-current upgrade path, and clearer future procurement sequencing.
- Result: Added purchase-later lines in BOM (`row 103` Mechman 370A alternator, `row 104` Big 3 estimate), added Big 3 wire notes to existing cable rows, and updated systems documentation with the staged strategy.
- Follow-up: Superseded by D-028; single-12V alternator + Big 3 path is now deprecated in BOM rows `103`/`104`.

- ID: D-010
- Date: 2026-02-12
- Decision: Lock Phase 1 distribution topology to `Lynx one-module` using `Victron Lynx Distributor M10` (`LYN060102010`).
- Context: Previous documentation included mixed Lynx/discrete language and ambiguous implementation baselines.
- Options considered: Keep discrete fuse-block topology, lock Lynx one-module, lock Lynx two-module.
- Decision drivers: Standardized layout, reduced wiring ambiguity, and alignment with current `4` modeled `48V` branch count.
- Result: Updated BOM Lynx row (`row 6`) and converted core electrical documentation to Lynx-only implementation baseline.
- Follow-up: Confirm whether future expansion requires adding a second Lynx module.

- ID: D-011
- Date: 2026-02-12
- Decision: Adopt a documented fuse baseline with explicit fuse IDs, locations, and spare inventory tied to BOM rows.
- Context: Fuse plan previously existed as mixed assumptions, not a single implementation schedule.
- Options considered: Keep generic fuse notes, track fuse values in BOM only, or maintain a dedicated fuse schedule linked to BOM.
- Decision drivers: Safety traceability, procurement clarity, and easier install-time validation.
- Result: Added `docs/implementation/ELECTRICAL_fuse_schedule.md`, mapped fuse groups to BOM rows (`7`, `10`, `11`, `16`, `105`, `106`), and set baseline battery Class T quantity to `2x` for two battery-positive conductors. Historical aggregate mapping note: the `2026-07-26` component split expanded row `10` into rows `10`, `323`, and `324`, and row `11` into rows `11`, `325`, and `326`.
- Follow-up: Lock exact fuse-holder SKUs and finalize any holder ecosystem constraints before purchase.

- ID: D-012
- Date: 2026-02-12
- Decision: Historical correction of obsolete alternator-charger rating assumptions and promotion of the topology artifact to implementation-level scope.
- Context: Earlier planning overstated the output of an obsolete alternator-charger path, and the topology diagram still excluded holder/wire-gauge implementation detail.
- Options considered: Keep existing assumptions, patch only charge-rate math, or patch charge-rate math and complete the fuse-holder + conductor topology together.
- Decision drivers: Safety planning accuracy, implementation readiness, and removal of unresolved holder/gauge ambiguity.
- Result: Superseded by the dedicated `48V` secondary alternator architecture; current implementation docs now own active fuse and conductor detail.
- Follow-up: Historical traceability only; do not use for current alternator commissioning.

- ID: D-013
- Date: 2026-02-13
- Decision: Lock Phase 1 camper AC/USB distribution baseline to two AC-out-1 branches plus DC-fed USB-C PD branches.
- Context: Previous AC scope was concept-level and procurement rows were incomplete, creating uncertainty around receptacle count, USB strategy, and shore interface hardware.
- Options considered: Single AC branch only, multi-branch panel with AC USB receptacles, or two AC branches with DC-fed USB-C PD outlets.
- Decision drivers: Practical usability (galley + office), safety/protection clarity, and reduced inverter idle/conversion losses for device charging.
- Result: Locked baseline to `4` total `120V` receptacle locations (`2` galley, `2` office), AC-out-1 branch split (`20A` galley + `15A` office), and an initial DC-fed USB-C PD baseline. Added corresponding BOM scope in rows `107-118` and aligned AC hierarchy in `docs/implementation/ELECTRICAL_overview_diagram.md`.
- Follow-up: Superseded in part by D-022 (USB station packaging, branch sizing changes, and 12V buffer-battery integration details).

- ID: D-014
- Date: 2026-02-15
- Decision: Adopt an overlapping build-sequence baseline with module-first prep before camper install date.
- Context: Install date is fixed (`2026-05-07`) and major build quality risks come from sequence errors (closing walls before rough-in validation, delayed module prep, and routing rework).
- Options considered: Strict serial trade flow, ad hoc sequencing, or staged sequence with explicit hold points and parallel workstreams.
- Decision drivers: Maintain install-date readiness, reduce rework risk, and keep system serviceability.
- Result: Added `docs/plans/PROJECT_build_order_of_operations.md` and linked it from `docs/core/PROJECT.md` as the active sequencing baseline.
- Follow-up: Update date windows after first dry-fit rehearsal and add sequence-specific risks if schedule compression appears.

- ID: D-015
- Date: 2026-02-15
- Decision: Adopt a consolidated multi-system safety baseline in `docs/core/SYSTEMS.md` covering `48V`, `12V`, `120VAC`, and propane architecture controls.
- Context: Safety guidance existed across fuse/topology notes and placeholder sections, but there was no single integrated baseline for commissioning, emergency shutdown, and propane/CO risk controls.
- Options considered: Keep safety details distributed only in implementation docs, create a separate standalone safety doc, or expand the canonical systems safety section with cross-links.
- Decision drivers: High-consequence risk reduction, clearer pre-energization hold points, and faster install-time validation.
- Result: Expanded `docs/core/SYSTEMS.md` `## Safety` with architecture-specific hazards, required controls, commissioning checks, emergency shutdown order, and pre-close inspection gates.
- Follow-up: Lock propane appliance listing/venting path and convert safety hold points into dated test records in `logs/LOG.md` during commissioning.

- ID: D-016
- Date: 2026-02-15
- Decision: Add explicit scope for modular inside/outside mounting rails and hardwall-popup solar jumper passthrough wiring.
- Context: Build intent requires flexible exterior/interior gear mounting (shovel/Maxtrax and interior hooks/baskets), and hardwall popup construction makes concealed in-wall solar routing impractical.
- Options considered: Leave as informal notes only, add one generic placeholder line, or add explicit BOM + systems + sequencing entries.
- Decision drivers: Procurement visibility, serviceable routing, and reduced install-day rework.
- Result: Added BOM rows `119`, `120`, and `121`; updated `docs/core/SYSTEMS.md` (`## Solar`, `## Cabinetry and structure`) and `docs/plans/PROJECT_build_order_of_operations.md` (Batches `B`, `C`, and `E`) to include the new scope.
- Follow-up: Lock final rail profile/attachment ecosystem and finalize solar jumper connector/passthrough SKU choices before purchase freeze.

- ID: D-017
- Date: 2026-02-16
- Decision: Reopen the `12V` vs `24V` vs `48V` core architecture decision (superseding the “48V default” assumption from D-002 pending final scope lock).
- Context: The electrical baseline assumed an AC-capable kitchen (induction + microwave) and a `3kVA` inverter class. The updated direction may be propane cooking + DC-first office (AC-light).
- Options considered: Full `12V` core, `24V` core + `12V` distribution, keep `48V` core + `12V` distribution.
- Decision drivers: Reduce space/complexity for a truck-bed camper, keep fast charging (alternator + solar), preserve a large bank (`10–15 kWh`), and avoid unnecessary high-current wiring or conversion layers.
- Result: Updated `docs/studies/ELECTRICAL_12V_vs_48V_trade_study.md` to reflect Scope A vs Scope B decision logic and to enumerate BOM/topology deltas by voltage. Final architecture selection is pending explicit AC policy + inverter approach lock.
- Follow-up: Superseded by D-018 architecture lock.

- ID: D-018
- Date: 2026-02-16
- Decision: Lock architecture to `48V` core + `12V` distribution.
- Context: After reopening the voltage study under a possible AC-light/propane scope, the project direction is to keep the existing `48V` implementation path.
- Options considered: Full `12V` core, `24V` core + `12V` distribution, keep `48V` core + `12V` distribution.
- Decision drivers: Keep fast charging + large bank performance margin, retain lower main-path current, and avoid redesign churn across BOM/topology/fuse documentation.
- Result: Updated `docs/studies/ELECTRICAL_12V_vs_48V_trade_study.md` recommendation and bottom-line sections to reflect `48V` as the active architecture.
- Follow-up: If AC load mix changes materially, update `bom/load_model_wh.csv` scenarios and recalculate `docs/core/SYSTEMS.md` while staying on `48V`.

- ID: D-019
- Date: 2026-02-16
- Decision: Accelerate procurement to a `Batch A+` wave so bench-build work can start immediately after core component arrivals.
- Context: Core electrical items alone would not enable practical bench assembly without pulled-forward wiring, lugs, fuse hardware, and basic electrical build tools.
- Options considered: Keep original phased dates (`Batch A` core only then later cable/consumables), ad hoc manual pull-forward, or explicit `Batch A+` resequencing with synchronized docs.
- Decision drivers: Reduce idle wait time between deliveries, remove bench-build blockers early, and keep one coherent source of truth across BOM, sequencing, and logs.
- Result: Updated `bom/bom_estimated_items.csv` `est_purchase_date` values for rows `3`, `4`, `5`, `6`, `7`, `10`, `11`, `12`, `16`, `17`, `18`, `20`, `22`, `23`, `26`, `27`, `28` through `45`, `52`, `53`, and `60`; synchronized `docs/plans/PROJECT_build_order_of_operations.md` and `docs/core/PROJECT.md` to reflect the accelerated wave.
- Follow-up: Capture actual order date/vendor/ETA status for each `Batch A+` row and flag any substitutions before bench wiring starts.

- ID: D-020
- Date: 2026-02-16
- Decision: Restore BOM row `122` as a placeholder interior line item for drawer-slide procurement tracking.
- Context: Canonical docs referenced row `122` for drawer hardware, but the row was missing from `bom/bom_estimated_items.csv`, creating a cross-document reference gap.
- Options considered: Remove row-`122` references from docs, or reinsert row `122` in BOM with unresolved pricing.
- Decision drivers: Keep row-ID traceability stable and preserve documentation consistency until cabinetry SKU lock.
- Result: Added row `122` to `bom/bom_estimated_items.csv` (`Drawer slide kits (soft-close undermount)`) with blank price and `2026-04-14` planning date.
- Follow-up: Lock final drawer-slide SKU (length/load class/brand) and populate price before interior procurement wave.

- ID: D-021
- Date: 2026-02-17
- Decision: Increase the house battery bank to `3x 48V 100Ah` LiFePO4 in parallel (from `2x`).
- Context: Space and payload margin allow a 3rd battery, and added capacity reduces “power anxiety” and reduces per-battery charge/discharge current.
- Options considered: Keep `2x` (`~10.24 kWh`), move to `3x` (`~15.36 kWh`), or jump to `4x` (`~20.48 kWh`) with higher cost and diminishing charging recovery speed.
- Decision drivers: Autonomy margin with a `20%` reserve floor, bench-build readiness for `Batch A+`, and parallel-bank current sharing.
- Result: Updated topology docs to add `Battery C` + `F-01C` Class T protection and added a 3-battery bench cut list for `2/0` cabling/lugs.
- Follow-up: Verify battery terminal stud size before ordering lugs; ensure batteries are at the same SOC/voltage before first parallel tie.

- ID: D-022
- Date: 2026-02-18
- Decision: Refresh the 12V subsystem to a shared battery-backed fuse-block junction using Orion-Tr Smart `48/12-30`, a `12V 100Ah LiFePO4` buffer battery, and two USB PD station branches.
- Context: Prior docs/BOM still treated the 12V buffer battery as deferred and used a `4`-point USB module baseline with `10A` per-zone fusing.
- Options considered: keep Orion-only 12V panel feed, add manual backup-only battery path, or lock a shared bus with source fusing and manual battery isolation.
- Decision drivers: better transient support for office/galley USB charging, cleaner service isolation, and minimal added control complexity.
- Result: Updated BOM row `20` (Orion Smart, `$243`), activated row `21` (`12V 100Ah LiFePO4`, `$113`), updated row `115` (two USB PD stations, `$100`), and revised canonical electrical docs to add `F-11` (`100A` class) + `SW-12V-BATT` in the 12V path with the fuse block main `+`/integrated `-` used as the junction pair. Historical row-meaning note: the current BOM now separates the purchased station in row `115` from the conditional second station in row `331`.
- Superseded assumptions: D-013's `4`-point USB/`10A`-zone baseline and deferred buffer-battery assumption for row `21`.
- Follow-up: lock final SKU family for `F-11` holder and `SW-12V-BATT` switch, then confirm under-load behavior of office `20A` and galley `15A` USB branches before procurement freeze.

- ID: D-023
- Date: 2026-02-19
- Decision: Lock AC architecture to split DIN panels with `30A` AC-in hardware, hardwired EMS, and reserve-only `AC-out-2` for Phase 1.
- Context: AC docs/BOM had mixed language between a compact load-center baseline and a split DIN approach, and AC procurement rows were not explicit for EMS and DIN panel accessory hardware.
- Options considered: keep compact load-center baseline, split DIN `20A` AC-in baseline, or split DIN with `30A` AC-in plus source-limited current settings.
- Decision drivers: compactness, service clarity, lower-complexity branch layout, and complete purchasable-component traceability.
- Result: updated AC topology and procurement docs to one architecture (`TT-30 -> EMS -> AC-in DIN 30A breaker -> MultiPlus AC-in`, plus AC-out DIN branch panel), updated BOM row meanings for AC rows (`13`, `14`, `109`, `110`, `113`, `114`) and added hardwired EMS row `123`, and adopted a manual AC validation checklist as the acceptance gate. Historical row-meaning note: the current component-level BOM pairs row `13` with AC-out-main row `327` and row `110` with branch-2 row `330`.
- Follow-up: partially reopened by D-026 for final branch utilization/receptacle count lock; superseded for procurement by D-044, which replaces hardwired EMS/split enclosures with portable EMS plus one combined `6-way` AC DIN enclosure.

- ID: D-024
- Date: 2026-03-18
- Decision: Replace CAD-gated run-length validation with bench-layout-first measured cut lengths for electrical harness work.
- Context: CAD-derived route-length artifacts are not being produced in time for current build pacing.
- Options considered: wait for CAD completion, cut from assumptions only, or lock physical-layout-first measurement workflow.
- Decision drivers: schedule realism, cut-length accuracy from real hardware placement, and reduced late-stage rework.
- Result: Project planning baseline now treats CAD lengths as rough planning input only; measured physical routes are the cut-length source of truth.
- Follow-up: record measured run lengths in implementation docs before final cable closeout orders.

- ID: D-025
- Date: 2026-03-18
- Decision: Remove the full-bed EPDM/RPDB thermal-break layer from the floor stack and run `3/4 in` birch directly over EPS/ribs.
- Context: Floor work advanced physically and stack-up priorities shifted toward simpler, stiffer execution.
- Options considered: keep EPDM thermal break, substitute alternate rubber layer, or remove thermal-break layer above EPS.
- Decision drivers: execution simplicity, available materials, and immediate progress against schedule.
- Result: Flooring baseline changed to bedliner -> EPS between ribs -> `3/4 in` birch subfloor -> finish vinyl; EPDM order was canceled before shipment and refunded, so no EPDM stock is on hand.
- Follow-up: confirm acoustic/thermal tradeoff is acceptable after initial in-use evaluation.

- ID: D-026
- Date: 2026-03-18
- Decision: Reopen final AC utilization scope (branch/receptacle count) while keeping the then-current `30A` shore + split-DIN protection architecture baseline.
- Context: Historical/superseded by D-044. At this point Phase-1 AC layout was close to lock, but final receptacle quantity was still being evaluated (`3` vs `4` locations) against real-use needs.
- Options considered: freeze current `4`-location plan, reduce to `3` locations, or defer decision until late install.
- Decision drivers: practical outlet usability, wiring simplicity, and avoiding unnecessary hardware sprawl.
- Result: Superseded by D-044: active AC purchase lock is one `6-way` enclosure with two `20A` GFCI branches; row `111` is obsolete and pop-up outlet details are deferred until provided.
- Follow-up: Closed/historical; use D-044 and current AC implementation docs for active AC work.

- ID: D-027
- Date: 2026-03-18
- Decision: Pay installer upcharge for `12-circuit` Blue Sea fuse panel (vs installer `6-circuit`) while retaining purchased budget `12-circuit` panel for bench prototyping.
- Context: Installation-day branch capacity and bench-development flexibility both matter.
- Options considered: keep installer `6-circuit`, switch installer to `12-circuit`, or rely only on owner-supplied panel.
- Decision drivers: cleaner final install capacity and preserving a separate prototype bench panel.
- Result: `+$50` installer scope change accepted; no conflict with prior owner-purchased `12-circuit` panel use case.
- Follow-up: map final installer panel branch assignments to the canonical fuse schedule during commissioning docs pass.

- ID: D-028
- Date: 2026-03-19
- Decision: Replace obsolete alternator-charger planning with dedicated `48V` secondary alternator architecture.
- Context: Current alternator trade study carried a simple `A1` migration baseline (`Mechman + WS500 + APM-48`) and the project requested an exact procurement delta under that assumption.
- Options considered: keep the obsolete charger baseline active, stage old/new hardware in parallel, or commit planning/procurement to the Mechman/Wakespeed path.
- Decision drivers: faster alternator-to-house charging, simplified architecture direction, and explicit procurement execution planning.
- Result: Migration delta is assimilated into canonical docs (`SYSTEMS`, `TRACKING`, starter plan, fuse schedule, and BOM). BOM rows updated for obsolete/returned hardware and new migration purchases (`18`, `26`, `103`, `104`, `168-173`) and standalone conditionals (`172`, `173`) removed from scope.
- Follow-up: obsolete charger hardware is not part of active layout, fuse planning, or commissioning.

- ID: D-029
- Date: 2026-03-19
- Decision: Finalize alternator migration fuse and wire baseline now.
- Context: Migration execution required immediate closure of fuse sizing and cable strategy before cable cuts or new contingency buys.
- Options considered: keep fuse/wire pending, downsize to new smaller cable now, or lock reuse-first with measured validation.
- Decision drivers: avoid unnecessary new wire spend, keep installation momentum, and close alternator branch protection ambiguity.
- Result: locked `F-04` at `150A` (`58V/80V` MEGA), added explicit WS500 low-current fuses (`F-12` `10A/15A`, `F-13` `3A`) with voltage-rating verification, clarified that WS500 current-sense high/low is not a fuse position, and locked reuse of existing uncut `2/0` inventory for the `~20 ft` alternator run baseline. Updated `docs/implementation/ELECTRICAL_fuse_schedule.md` and BOM rows `170-173` accordingly.
- Follow-up: if measured route reality materially differs, re-run drop/ampacity screen before any gauge downsize. `D-059` superseded this decision's separate `F-12`/`F-13` low-current-fuse assumption, and `D-066` supersedes its `F-04 150A` value with `200A/80V`; the `2/0` conductor decision remains current.

- ID: D-030
- Date: 2026-03-20
- Decision: Use Ford `Upfitter Switch #3` as the manual `WS500` enable/disable control path.
- Context: The finalized `48V` alternator architecture needed one simple operator shutdown method that disables the regulator before the main `48V` disconnect is used.
- Options considered: separate aftermarket dash switch, direct always-hot ignition feed, Ford upfitter switch direct to WS500 brown wire, or a more complex relay/interlock-only first implementation.
- Decision drivers: simple cab control, low added hardware count, cleaner operator procedure, and alignment with the `WS500` ignition/enable concept.
- Result: locked manual control path to `Ford Upfitter #3 -> F-15 3A inline fuse -> WS500 brown ignition/enable wire`; `WS500` white `Feature-In` remains reserved for future automatic fault-interlock work. Updated canonical `48V` doc, implementation docs, operations guidance, and BOM row `176`.
- Follow-up: if commissioning shows need for automatic fault shutdown, add relay/interlock logic on top of this manual baseline rather than replacing it.

- ID: D-031
- Date: 2026-03-20
- Decision: Consolidate finalized `48V` architecture into one canonical file.
- Context: The `48V` story had spread across trade studies, implementation docs, BOM notes, and tracking entries, making it harder to read the actual final design quickly.
- Options considered: keep the study as the de facto architecture source, collapse implementation detail into SYSTEMS only, or create one concise canonical `48V` architecture doc and point the rest of the repo at it.
- Decision drivers: clarity, lower maintenance overhead, and easier install-time reference for wiring and shutdown behavior.
- Result: added `docs/core/ELECTRICAL_48V_ARCHITECTURE.md` as the canonical `48V` design file; supporting docs now reference it instead of treating the alternator trade study as the final design source.
- Follow-up: keep implementation detail in the wiring/fuse docs and reserve the alternator study for research history only.

- ID: D-032
- Date: 2026-04-27
- Decision: Replace the narrow install-minus-12 plan with an integrated Apr 27-May 11 install readiness and post-install plan.
- Context: Install is fixed for May 7 at 9:00 AM in Bellingham, with travel from Park City and May 6-11 off work. Current blockers span shore charging, electrical layout, floor/bed sealing, extrusion, plumbing, and logistics.
- Options considered: keep the shore/extrusion-only plan, create multiple new docs, or replace the existing plan with one integrated plan.
- Decision drivers: avoid document creep while making the install window executable.
- Result: `docs/plans/INSTALL_MINUS_12_READINESS_PLAN.md` now owns the integrated install-window plan.
- Follow-up: update logs and this tracking file after install-day measurements and shakedown evidence.

- ID: D-033
- Date: 2026-04-27
- Decision: Prioritize an AC-in-only MultiPlus shore-charge path before final AC-out receptacle closure.
- Context: Initial battery charging and bench testing are blocked by shore-power uncertainty, while AC-out branch/receptacle layout can wait.
- Options considered: wait for complete AC branch layout, buy a combined breaker box, or keep split AC-in/AC-out architecture and build AC-in first.
- Decision drivers: safety, reduced decision coupling, and faster path to first battery charge.
- Result: AC-in path rows `107`, `108`, `123`, `13`, `109`, `14`, and `114` are the immediate purchase/SKU-lock focus; AC-out branch rows can defer if not needed for initial charge.
- Follow-up: superseded for procurement by D-044; first energization/short shore-charge test has passed, but sustained charging still requires MultiPlus LiFePO4 profile verification.

- ID: D-034
- Date: 2026-04-27
- Decision: Treat Lonseal glue-down as gated finish work, not immediate routine flooring.
- Context: EPS and three-piece plywood subfloor are installed, and Lonseal/glue are in hand, but glued finish flooring reduces subfloor serviceability. Bed rail cap sealing, old rail holes, bed-floor drain holes, and small corner gaps remain open moisture-control items.
- Options considered: glue now, delay all flooring, or complete trim/seal/cure-inspection gates before glue-down.
- Decision drivers: preserve access until rail/bed-floor/corner sealing, hardpoint, and penetration questions are closed.
- Result: Lonseal glue-down waits until bed rail/bed-floor/corner sealing is complete and visually inspected after cure/normal use, EPS trim passes, hardpoint pockets are verified, and cure/tool readiness passes.
- Follow-up: update `logs/LOG.md` with gate evidence before glue-down.

- ID: D-035
- Date: 2026-04-27
- Decision: Treat current furniture CAD as reference-only and order only low-regret stock extrusion/hardware until fridge/tank envelopes are revalidated.
- Context: Iceco/water tank dry fit showed the cooler/fridge does not open in the planned location. D-040 temporarily set the working baseline as rear-left / bottom-left; D-043 later supersedes that with the passenger-side lofted fridge/wet-spine baseline.
- Options considered: order exact cut lengths from stale CAD, wait on all extrusion, or buy stock-length starter extrusion and connector hardware.
- Decision drivers: avoid waiting later while limiting waste from a known CAD mismatch.
- Result: superseded by D-038 for tank restraint: do not treat a `15-series`-biased starter order as acceptable solely for the water tank; final drawer slides, panels, skins, and exact cut lists remain deferred.
- Follow-up: measure real fridge/purchased wheel-well tank envelopes and update module CAD after camper install measurements.

- ID: D-036
- Date: 2026-04-27
- Decision: Decouple cold-water galley progress from final water-heater selection.
- Context: Faucet is missing, and water heater decision fatigue risks blocking pump/tank/sink progress.
- Options considered: electric tankless, small tanked electric, portable outdoor propane, listed indoor/RV propane, engine-coolant marine calorifier, or cold-water-first with future hot tie-in.
- Decision drivers: current inverter scale, safety, and schedule.
- Result: Build toward cold-water tank/pump/faucet/sink/drain baseline with capped future hot tie-in; treat portable propane as outdoor-only provisional and defer electric tanked/listed indoor propane/engine-coolant calorifier until service-map freeze. As of `2026-05-28`, the engine-coolant option remains physically plausible because the Hiatus is a topper over the retained F-350 bed, so coolant lines could route through bed/floor structure rather than the removable shell.
- Follow-up: discrete BOM rows for faucet/sink are now added and purchased (`207-208`); still lock drain/graywater and propane support classes plus graywater/winterization details.

- ID: D-037
- Date: 2026-04-27
- Decision: Rebalance the pre-install plan around normal `9-5` workdays and a heavier May 2-3 weekend.
- Context: PTO is May 6-11, but weekday evenings through May 5 still have normal `9-5` work before them. The prior day-by-day plan put too much physical work on worknights.
- Options considered: keep daily equal workload, push everything to the weekend, or reserve worknights for light tasks while using the weekend for truck-heavy work.
- Decision drivers: reduce burnout, avoid half-disassembled truck risk, and preserve realistic execution before travel.
- Result: weekday evenings are limited to calls, ordering, labeling, small inspections, and packing; bed rail sealing, EPS trim, electrical layout, extrusion decisions, and plumbing layout move mainly to May 2-3.
- Follow-up: use May 6 PTO as the Bellingham travel/staging day; keep it logistics-only rather than build catch-up.

- ID: D-038
- Date: 2026-05-01
- Decision: Supersede the broad `15-series` water-tank exoskeleton plan after purchasing a `36 gal` wheel-well water tank.
- Context: The earlier `15-series` extrusion need was driven by a tall/skinny vertical `36 gal` tank concept. The purchased wheel-well tank is lower, wider, bracketed, and intended to plusnut into bed walls, reducing overturning leverage and removing the main reason for a heavy extrusion cage.
- Options considered: buy the prior `8x 92 in` `15-series` starter order, cancel all extrusion thinking, or downscope to targeted extrusion only where a remaining module proves it needs structure.
- Decision drivers: lower center of gravity, lower off-road moment load, reduced cost/weight/complexity, and avoiding stockpiling bulky material before post-install envelopes are verified.
- Result: do not buy `15-series` for tank restraint unless physical dry fit proves the wheel-well tank still needs a separate frame; use targeted `15-series` only for electrical/fridge/desk modules that cannot mount directly or with simpler brackets.
- Follow-up: dry-fit the tank, verify bracket/plusnut and any secondary floor/tie-down load path, then update final extrusion count after install measurements.

- ID: D-039
- Date: 2026-05-04
- Decision: Treat the Washington trip as empty-bed install/shakedown mode, not a full electrical/interior-build deployment.
- Context: Bed rail caps have been removed/rebonded with polyurethane, small drill holes patched with Gorilla tape, corner air gaps sealed, trowel purchased, and the flooring/subfloor is out or not ready for final closeout. Owner expects not to bring batteries/electrical on the trip.
- Options considered: rush flooring/electrical before departure, bring batteries and build parts for remote work, or keep the truck mostly empty and use the trip for install, shakedown, and measurement.
- Decision drivers: avoid half-finished adhesive/flooring work, reduce travel weight/risk, preserve access for post-install ordinary inspection, and avoid exact cabinetry/extrusion decisions before real camper measurements.
- Result: keep batteries/electrical parts home, let sealing cure, travel empty-bed, capture measurements/photos at Hiatus, then resume EPS/plywood/Lonseal, extrusion, and electrical bench work after return.
- Follow-up: log post-install inspection observations and measured camper dimensions before final floor glue-down or exact extrusion orders.

- ID: D-040
- Date: 2026-05-04
- Decision: Use the office-first hybrid interior layout as the draft furniture baseline.
- Context: The top-left electrical closet and `3x 48V` batteries spill into the center, the top-right fridge location failed fit, the driver side must support full-time monitor-based work, and the passenger side must absorb the `36 gal` wheel-well tank plus galley plumbing in a compact space.
- Options considered: keep a simple truck-camper layout, prioritize a rear utility threshold, or adopt a van-style high-density interior adapted to truck-camper roof/weight/service constraints.
- Decision drivers: full-time work ergonomics, low/forward heavy-mass placement, center-aisle movement, cabover step function, roof-down clearance, and plumbing/electrical serviceability.
- Result: this May 4 draft baseline used top-left power stair battery bench, top-right soft-storage/cabover-landing bench, driver-side desk with stow-low monitor and rear-left Iceco utility block, passenger-side galley wet spine over the `36 gal` tank, rear shower/fill/vent service hatch, cold-water-first plumbing, and capped future hot-water stubs. D-043 supersedes the fridge/bench/wet-spine placement with the passenger-side lofted fridge/wet-spine/battery-bench layout. Owner doc: `docs/implementation/INTERIOR_furniture_layout_and_galley.md` with generated concept diagrams under `media/diagrams/interior-furniture-2026-05-04/`.
- Follow-up: validate with real installed-shell measurements, roof-down sweep map, tank/fridge dry fit, wet-spine service mockup, seated workday test, and load sequencing before exact extrusion cuts or permanent penetrations.

- ID: D-041
- Date: 2026-05-12
- Decision: Correct gravity-fill vent tube sizing to `10 mm ID` / common `3/8 in ID` food-grade tube, not `1/2 in ID x 5/8 in OD` tube.
- Context: Owner dry-fit showed the ordered `1/2 in ID x 5/8 in OD` food-grade tube is too large for the water inlet gravity-feed vent nipple.
- Options considered: keep `1/2 in ID`, use `7/16 in ID`, or size the hose to the measured nipple land/barb.
- Decision drivers: measured nipple dimensions (`10 mm` OD main land, `11 mm` OD largest barb/ridge), clamp reliability, and avoiding a loose vent-line seal.
- Result: documentation now specifies `10 mm ID` preferred, `3/8 in ID` common inch fallback, and `7/16 in ID` only as a looser clamp-required fallback.
- Follow-up: dry-fit the replacement hose, clamp it, verify no kink/flow restriction, and re-check after the first fill/drive cycle.

- ID: D-042
- Date: 2026-05-14
- Decision: Use overlay/removable panels over `10-series` 80/20 for finished living-facing furniture surfaces, while keeping service zones exposed or quick-removable.
- Context: Owner prefers clean/homey finished surfaces and noted overlay panels are likely easier than inset panels because the 80/20 exoskeleton can be built first, then panels can be added without disassembling the frame or forcing thin `1/4 in` slot-fit panels.
- Options considered: exposed industrial 80/20, inset panels captured in extrusion slots, or overlay panels mechanically fastened to the frame.
- Decision drivers: finished appearance, easier iterative prototyping, better panel thickness flexibility, better shear-skin potential, and serviceability if access panels remain removable.
- Result: baseline is mechanically fastened overlay panels on visible cabin faces; exposed 80/20 or quick-removable covers in electrical, plumbing, rear utility, and wet-spine areas. Magnetic service panels are a promising non-structural cover pattern when backed by steel brackets/plates, anti-rattle tape, and secondary/captive retention where panel loss matters.
- Follow-up: test magnet size/spacing, steel landing plates, routed magnet pockets, anti-rattle tape, and secondary latch/tether options on a sample service panel before using magnets for real travel panels.

- ID: D-043
- Date: 2026-05-14
- Decision: Supersede the rear-left/driver-side fridge concept with a passenger-side lofted fridge/wet-spine/battery-bench layout.
- Context: After working with the actual camper, paneling and systems interference made the electrical/plumbing/fridge enclosure a three-dimensional layout problem. Owner found a better fit by moving the Iceco/fridge back to the passenger side, raised about `16 in` on an extrusion exoskeleton, slightly overlapping the `36 gal` wheel-well tank, with pump/accumulator below it next to the tank and batteries in adjacent separated bench enclosures.
- Options considered: continue with driver-side/rear-left fridge utility block; wait for perfect CAD before buying/cutting extrusion; or prototype a targeted 80/20 exoskeleton to prove the real component geometry.
- Decision drivers: serviceability, physical fit in the installed camper, better wet-side clustering, less driver-side office interference, ability to mount/enclose components from multiple faces, and reduced risk from trying to validate this only on the garage floor.
- Result: active baseline is passenger-side lofted fridge/wet-spine exoskeleton, under-fridge pump/accumulator service bay, adjacent separated `30 in` battery bench with flat divider board and cushion/lid use, driver-side `46 in` electrical closet/DC shelf/workstation zone, diesel heater low on driver side, and investigation of an exterior truck-bed-wall diesel tank/fill/pump path.
- Follow-up: physically mock the lofted fridge/wet-spine/battery bench in the camper, classify each 80/20 member by structural/service/panel role, search for a narrow exterior diesel tank around `8 gal` / `3 in x 17 in`, and update final cut lists only after access/interference checks pass.

- ID: D-044
- Date: 2026-05-16
- Decision: Lock and purchase the Phase 1 AC system as portable-EMS, single-enclosure `30A` shore/inverter AC.
- Context: AC procurement was reopened to avoid overbuilding and to fit the limited cabinet space near the MultiPlus while still preserving normal RV/camper protection.
- Options considered: two separate AC-in/AC-out enclosures, one combined DIN enclosure without AC-out main, one combined DIN enclosure with `30A` AC-out main, or upsizing feeder/panel for `40A+` output.
- Decision drivers: compactness, clear `30A` system cap, standard `10/3` feeder use, service labeling, and avoiding a full `40A/50A/75A` output build.
- Result: purchased Progressive Industries EMS-PT30X portable `30A` EMS; Camco TT-30P-to-L5-30R shore cord plus 15A dogbone; Nilight L5-30 inlet; Mollom `6-way` DIN enclosure; ControlGear `30A` breakers qty `2` for AC-in and AC-out main; ControlGear `20A` breakers qty `2`; ELEGRP `20A` GFCI receptacles qty `2` with covers/plates, `10/3` and `12/3` triplex wire, bus bars, ferrule crimper kit, butyl tape, and Sikaflex-221. Row `111` downstream non-GFCI receptacles is obsolete; row `112` is no longer a design blocker because outlet box/cover details are handled as installation fitment around the two active GFCIs. A user-provided pop-up multipurpose outlet remains deferred/outside active baseline until details are supplied.
- Follow-up: single-enclosure neutral isolation/PE continuity/no fixed downstream neutral-ground bond still need formal dead-check record before AC-out commissioning. Short AC-in charging validation is now complete; AC-out branch/GFCI commissioning remains separate.

- ID: D-045
- Date: 2026-05-27
- Decision: Mark first `48V` DC / MultiPlus / Cerbo / limited shore-charge commissioning checkpoint as passed, while keeping sustained charging and AC-out/alternator commissioning gated.
- Context: Owner completed first live energization after pre-charge and measured `55.5V` throughout the `48V` system, including the MultiPlus. MultiPlus inverter mode came online with normal light/hum and no errors. SmartShunt and Orion appeared in VictronConnect. Cerbo GX AP/remote-console workflow came online. A short shore-charge test ran with household-source current limiting.
- Options considered: treat the system as fully commissioned, treat the live test as failed/incomplete, or record it as a successful staged checkpoint with remaining configuration gates.
- Decision drivers: avoid losing important live-test evidence while not overclaiming charger-profile, AC-out, GFCI, or alternator readiness.
- Result: first live `48V` and AC-in functional checkpoint is passed. AC Input 1 should be labeled `Shore power`; household outlet testing uses `10A` first-test / `12A` max-on-15A policy. Cerbo is documented as a small inline fused `48V` feed (`CERBO-PWR`) rather than a 12V fuse-panel branch. Parallel battery cable balancing is documented as similar total loop resistance, not equal positive-only length.
- Follow-up: MultiPlus LiFePO4 charge-settings verification was later closed by owner live behavior check (bulk -> quick absorption at/near `100%` on the first battery). Formally verify AC neutral/ground/GFCI behavior before AC-out use; keep alternator commissioning deferred.

- ID: D-046
- Date: 2026-06-01
- Decision: Keep a compact DC-first camper audio system as a preliminary/future camper subsystem concept, separate from the truck-cab driving subwoofer system.
- Context: Owner wants strong bass and good audio in the camper without audiophile cost or duplicative truck/camper audio wiring. The `S11 Ultra` tablet is already the shared dashboard/Victron/media device.
- Options considered: soundbar-only, truck/camper shared subwoofer hardware, powered-sub camper `2.1`, or full multi-amp audiophile system.
- Decision drivers: strong bass per dollar, compact packaging, low integration risk, simple tablet control, and keeping high-current audio wiring on the camper `12V` side without new `48V` branch complexity.
- Result: draft future package is Kicker `46KMC2` source/head unit + Kicker `CSC67` `4 ohm` speaker pair + Kicker `49PTRTP10` powered 10 in down-firing sub. BOM rows `189-193`, implementation doc `docs/implementation/CAMPER_audio_system.md`, electrical fuse/conductor integration, and the current load model (v5 supersedes the original v4 entry) preserve the concept for later, but audio is not near-term procurement.
- Follow-up: validate KMC2 mounting depth, PTRTP10 dry/ventilated low mounting location, speaker cutout/pod locations, final RCA/speaker-wire lengths, and actual `12V` buffer-battery behavior during loud audio plus normal 12V loads.

- ID: D-047
- Date: 2026-06-01
- Decision: Close the MultiPlus shore-charge programming/verification blocker for the current charger setup without requiring a second-battery charge cycle.
- Context: Owner redid the MultiPlus settings and confirmed the first battery entered bulk, then quickly transitioned to absorption because it was already at/near `100%`, which matched the planned behavior. Owner does not need or want to charge a second battery solely for documentation.
- Options considered: require a second battery charge before closing the gate, close the profile gate based on first-battery behavior while leaving physical/AC-out/alternator gates open, or keep all charging marked uncommissioned.
- Decision drivers: charger settings and behavior were validated, additional charging is unnecessary wear/time, and the remaining risks are physical install/strain relief plus separate AC-out/alternator commissioning rather than charger-profile programming.
- Result: MultiPlus profile verification is closed for current shore charging; no second-battery charge is required just to validate the profile.
- Follow-up: keep normal unattended-charge physical safety checks: source-current limit, no abnormal heat/smell/noise, protected wiring, covers, and strain relief.

- ID: D-048
- Date: 2026-06-05
- Decision: Preserve the desired interior lighting design as a deferred `12V` QuinLED/WLED system with hardwired momentary buttons, superseding the prior `24V`/MiBoxer worksheet.
- Context: Owner likes the integrated WLED direction but explicitly does not want to install or procure lighting yet because plumbing, Starlink, solar, alternator, and furniture are higher priority.
- Options considered: keep MiBoxer RF controllers/remotes, use a `24V` converter-backed lighting subsystem, or use a single WLED/ESP32 analog PWM lighting controller.
- Decision drivers: one integrated system, fewer remote batteries, documented hardware, local hardwired controls for daily use, and preserving future app/API/Home Assistant flexibility without making lighting a current rabbit hole.
- Result: `docs/plans/INTERIOR_LIGHTING_PLAN_2026-05-31.md` now owns the deferred desired design: `12V-11 -> QuinLED An-Penta-Deca -> upper CCT + lower RGBCCT`, with three hardwired button locations and WLED presets.
- Follow-up: do not buy lighting yet; preserve rough-in opportunities and later verify strip/channel width, branch fuse/conductor sizing, controller channel current, button locations, WLED presets, and power-loss behavior on the bench before install.

- ID: D-049
- Date: 2026-06-11
- Decision: Close the Mechman mechanical/staged-driving concern and rough in WS500 wiring with the regulator near the truck-bed house electrical area.
- Context: Owner found the alternator noise was the Mechman-supplied idler pulley not being seated properly; tightening/seating the idler cleared the noise. Mechman confirmed the truck can be driven with the `48V` alternator mechanically installed and unwired/electrically disabled.
- Options considered: keep the prior staged-driving support gate open, treat the alternator as fully commissioned, or close only the mechanical/drivability gate while keeping electrical commissioning gated.
- Decision drivers: owner/Mechman confirmation, clean separation between mechanical drivability and live charging, and Wakespeed's analog shunt-sense/noise guidance.
- Result: mechanical-only staged driving is acceptable in the disabled/unwired state after belt/idler/noise checks pass. The WS500 rough-in default is regulator near the truck-bed house bank/shunt area, with `2/0` B+/B- high-current pair plus separate labeled looms for WS500 alternator leg, alternator temp sensor, local battery/shunt sense, and cab/control wiring.
- Follow-up: record measured route lengths; keep PH/NH harness polarity, alternator field-voltage/derate, case-ground behavior, WS500 profile, APM, fusing, sense wiring, and first charging run as commissioning gates.

- ID: D-050
- Date: 2026-06-27
- Decision: Treat the trimmed/inset freestanding electrical module as shop-fit complete but not road-ready until it is tied into the bench/desk/galley structure.
- Context: Owner trimmed the electrical backer to inset into the `80/20` frame and adjusted component placement after real MultiPlus depth proved deeper than the earlier model. The module now stands on its own and is ready to connect to the bench, but it is still too wobbly to drive with before panels and bench/desk tie-in.
- Options considered: bolt the freestanding electrical module into the truck now; pause and wait for the pending 80/20 nut/hardware shipment; continue building the bench/desk/galley modules and integrate them before road use.
- Decision drivers: road vibration/projectile risk, module racking control, practical use of on-hand extrusion/angle/hardware, and the need to validate the bench/desk/galley as one physical system.
- Result: next build sequence is bench/battery/step structure first, desk desktop/workstation support next, then galley/wet-spine counter/appliance module around the purchased sink/faucet, induction cooktop, and Ninja SP151 cubby. Do not drive with the electrical module freestanding.
- Follow-up: `2026-07-19` physical status: the electrical module is now hard-mounted through the finished floor to truck-bed hardpoints and fits cleanly. Final Bench tie-in/panels or diagonals, anti-rattle retention, fastener witness marks, strain relief, and emergency electrical access remain required before road shakedown.
- Follow-up: `2026-08-02` physical status: the returned Bench extrusion now ties the hard-mounted electrical and Galley/cooler structures together and the owner reports the integrated assembly is extremely stiff. D-050's anti-rack tie gate is closed; remaining road restraint is the battery/cooler capture, terminal/cable protection, torque/witness marks, and inspection.

- ID: D-051
- Date: 2026-07-05
- Decision: Commission final high-touch interior wood surfaces from Nick in black walnut after templates/dimensions are locked.
- Context: Owner discussed final wood surfaces with Nick and wants the camper to use three related black walnut pieces rather than unrelated commodity tops: Galley counter, Desk top, and L-shaped Bench/lid top.
- Options considered: keep plywood/butcher-block-only finish path, source marketplace/tabletop material, or commission custom black walnut pieces.
- Decision drivers: intentional furniture-grade interior, matching Galley/Desk/Bench design language, and the opportunity to use a controlled live edge at the Galley entry end.
- Result: current surface baseline is a black walnut live-edge Galley countertop, likely `~4 ft x 19 in` pending exact confirmation, `1.5 in` preferred / `2 in` acceptable thickness, with the last `~15 in` curving inward if the slab allows; a dimensional black walnut computer desk top; and a dimensional black walnut L-shaped Bench/lid top supported on aluminum-extrusion tabs with gas struts if actual weight/geometry work. Finish default is satin polyurethane or equivalent durable clear film, with epoxy used selectively for void/check stabilization rather than full flood coat unless deliberately chosen.
- Follow-up: create plywood/templates and dimension packet for Nick; confirm final Galley length/width, sink/faucet/appliance clearances, support tabs, Desk depth/height, Bench hinge/strut/latch geometry, finish sample, price, and schedule before premium cuts.

- ID: D-052
- Date: 2026-07-10
- Decision: Promote the floor to the active foundation gate using the owner-confirmed practical build path.
- Context: Integrated modules are test-fit, so one controlled teardown can settle the bed, floor, and hardpoints before final system routing. Owner confirmed that the stainless rivnuts are now installed across rib highs, valleys, and some rib-edge transitions, Gorilla tape is adhering well to bed liner as a dust/splash barrier, and the floor cannot exceed the existing `3/4 in` height.
- Options considered: redesign the inserts/substrate around preferred manufacturer conditions; defer floor work; or retain the proven height and proceed with a flat/stable substrate plus registered stainless-rivnut hardpoints.
- Decision drivers: strict build height, practical sealing performance, serviceability, avoiding another teardown, and positive module retention without turning the work into a compliance exercise.
- Result: finish the remaining tape/seal pass, hand-test/map the installed stainless rivnuts, relocate or retire poor angled locations, use the on-hand `5/8 in` sleeves only as measured under-plywood valley/EPS spacers, settle the existing EPS and `3/4 in` plywood until flat/quiet, dry-fit Lonseal with hole recovery planned, then install/cure and reinstall modules on the registered hardpoints. Product documents remain relevant for adhesive handling and cure, not as a mandate to alter the height-locked floor.
- Follow-up: record the final rivnut map and sealing completion, verify the plywood panels do not rock or move at seams, choose the Lonseal perimeter treatment, and record first-drive inspection evidence in `logs/LOG.md`.

- ID: D-053
- Date: 2026-07-16
- Decision: Treat the glued Lonseal floor as permanent and sequence the next build around open access to electrical batteries and the water tank before furniture closure.
- Context: Owner glued the one-piece Lonseal to the three-piece `3/4 in` plywood floor on the evening of `2026-07-15`. The sheet now bridges both plywood seams, so removing the floor as three sections requires cutting the vinyl. Owner reports mild waviness/bumps, some lifted edges held with bolted boards, and #650 contamination in some hardpoint holes; temporary bolts were installed to preserve threads. The empty truck also makes tank and battery work materially easier before all modules return.
- Options considered: reinstall every furniture module immediately after cure; complete all tank fitting work on the garage floor before checking installed geometry; or use a utilities-first staged reinstall with the electrical/battery bay open and one required in-truck tank dry fit before drilling.
- Decision drivers: #650's `72 hr` heavy-furniture cure, avoiding permanent bolt/thread capture, preserving battery terminal/fuse/extraction access, preserving tank fitting/sender/service access, and proving shore/water-fill routes from their inside endpoints before exterior cuts.
- Result: floor removal is no longer an active branch. During cure, preserve hardpoint threads and map the tank on the workbench. After post-cure floor inspection, hard-mount the electrical module first, install/wire/fuse the `3x 48V` bank with the bench open, then add the bench structure. For water, inventory ports and mock fittings on the workbench, perform one bare-tank in-truck dry fit, freeze the port/restraint/service map, then drill/install/bench-test and hard-mount the tank/wet spine. Shore and water-fill/vent penetrations follow physically proven inside routes.
- Follow-up: `2026-07-19` status: controlled module loading and the electrical hard-mount gate have passed; retain the final floor-condition photo/inspection and bolt/rivnut evidence as open closeout. Record the final tank port map and fitting method, bench-test the complete wet spine, and keep final cabinetry removable until electrical/plumbing functional tests pass.

- ID: D-054
- Date: 2026-07-25
- Decision: Simplify the Hiatus hot-water/plumbing baseline to a fixed minimum-fitting parallel branch rather than a manifold and three-valve bypass module.
- Context: The previously recommended cold manifold, hot manifold, three-valve bypass, quick unions, winterization pickup, and removable wet-spine cassette consume too much space and introduce too many joints for a truck-bed camper. Owner accepts knowledgeable service that may require removing the cooler, panels, or part of the 80/20 structure and cutting/capping PEX when uncommon component replacement is required.
- Options considered: retain the full service manifold/bypass cassette; use a compact manifold with three-valve heater bypass; or hard-mount the existing pump/accumulator pack and branch the heater in parallel with ordinary tees and one or two isolation valves.
- Decision drivers: minimum leak points, vibration/overlanding robustness, actual under-cooler/bench space, cold-water continuity, and avoiding residential/RV service conventions that do not earn their space here.
- Result: default path is `tank shutoff -> flex -> strainer -> pump -> flex -> accumulator -> one cold tee`; the straight leg is the joint-minimized cold trunk and the branch feeds the storage heater through one cold-inlet valve. Heater hot feeds one insulated trunk; a hot-out valve is optional for clean removal. No cold/hot manifold, three-valve bypass, quick-disconnect plumbing, or permanent antifreeze pickup is required. Keep the heater in parallel so cold remains available. Default to normal heater temperature with local faucet/shower mixing; add a central TMV only if intentionally storing hotter water. Factory T&P relief/discharge and heater drain requirements remain.
- Follow-up: dry-fit the chosen heater and route, then count exact tees/valves/adapters from real component ports before ordering. Preserve short flex at the pump, support the PEX, pressure/leak-test in the driveway, and recheck after the first drive.
- Supersession: D-055 later the same day closed the interior/storage-heater branch. Retain D-054 only for the accepted minimum-fitting/serviceability posture; the active topology is the external HOTTAP BLUE cold-out / RED hot-return circuit.

- ID: D-055
- Date: 2026-07-25
- Decision: Finalize propane-only hot water with a deployed Joolca HOTTAP V2 and two-port rear water interface; close the alternate hot-water branches.
- Context: Owner made the fuel decision final and accepts camp setup. The rear swingout box is directly behind the galley, the camper has a viable service-plate location above the taillight, the existing SHURflo `4008`/SEAFLO accumulator matches Joolca's published source range, and the owner does not want the box rebuilt into isolated internal compartments. Owner subsequently locked the filled-cylinder location as the ventilated rear box, selected a `10 lb` aluminum Flame King cylinder, and required the box-to-camper water hookup to be the only routine water connection.
- Options considered: fixed RV direct-vent heater in the swingout box; generic portable Flame King/Camplux shower unit; Joolca HOTTAP V2 with parked-only cold-out/hot-return hoses; cylinder inside the box during operation; or permanent cylinder mount on the rear swingout. A late parallel review identified the FOGATTI `FS07B1S` as the strongest Amazon-available fixed RV appliance, but it requires a dedicated roughly `13 x 13 in` rough opening, manufacturer exterior door/flue, `12VDC`, installed LP plumbing, and appliance/cylinder separation; that is a different permanent box-conversion architecture and does not supersede the selected portable/deployed HOTTAP path.
- Decision drivers: one appliance for exterior shower and sink washing, no occupied interior heater volume, minimal permanent plumbing, documented camper-pump/faucet support, no duplicate `12V` heater power system, easy winter draining, and no connected LP/water hoses across the moving pivot.
- Result: select HOTTAP V2 Essentials and one Flame King `YSN10LB-ALM` aluminum `10 lb` QCC1 cylinder. The cylinder travels upright, valve closed, and LP-disconnected in a rigidly backed cradle inside the permanently low/high-vented rear box; a foot-ring capture and rated body strap carry travel loads while thin rubber pads/strap prevent chafe and rattle. The HOTTAP stays on an articulating-TV-arm/Joolca-bracket assembly based inside the box, with a separate travel latch, and swings fully outside before ignition. This is consistent with Joolca's own vehicle-mount and swing-out-TV-bracket guidance. The camper and box each receive a BLUE/RED two-port plate; two short, sleeved CPC jumpers make the parked water connection, while the heater-side hoses remain attached. A Joolca-compatible three-way hot splitter leaves both the shower hose and faucet-return branch connected. A fan is not the safety basis and does not authorize burning the heater inside the box.
- Follow-up: obtain/dry-fit the actual `9 x 9 x 19.25 in` cylinder in the reported `19.5 in` shelf opening; prove valve/regulator access, the `0.25 in` nominal vertical margin, cradle/backing, permanent low/high free vent area, and arm/hose service loops. Mock the deployed heater against `39 in` top, `23.6 in` rear, and `19.7 in` front/side clearances measured from the heater faces. The FORIOUS `3/8 in` faucet adapters and accumulator female-swivel PEX-B stock were purchased `2026-07-25`; verify the YVSKM swivel markings/gaskets and cold-pressure-test them. Source four exact NSF CPC HFC35 `86600` panel bodies, four `83100` inserts, four `HFC312L` dust plugs, two sanitary double-ended jumpers, and the Joolca hot splitter/second outlet hose. Gauge-test pump/accumulator behavior; pressure/leak/ignition-test shower and sink modes at intended elevation; drain-test before drilling the final camper or box plate openings.
- Supersession: `D-056` replaces the articulating-arm, box-side plate, CPC jumper, and permanent three-way-splitter details while retaining this decision's propane-only HOTTAP, vented/restrained cylinder, exterior operation, and BLUE/RED camper service roles.

- ID: D-056
- Date: 2026-07-26
- Decision: Direct-mount the HOTTAP outside the rear box and standardize the camper ports on the Joolca/Melnor QuickConnect hose profile.
- Context: Owner selected the HOTTAP V2, Joolca vehicle quick plate, and mounted cover specifically to keep the heater outside the propane compartment, protect it from road dust, and recover box storage. Research confirmed that Joolca's supplied `5 m` shower assembly splits into `1 m` and `4 m` red sections with female quick-connect sockets at both ends; the shower handle/head disconnects from the long section, and Joolca explicitly documents Melnor QuickConnect compatibility plus existing-faucet use.
- Options considered: retain the doubled CPC HFC35 camper/box plates; adapt CPC to Joolca with pigtails; use Joolca/Melnor-profile plugs directly on a custom BSP bulkhead; or use standard marine MGHT bulkheads plus Melnor faucet adapters. The doubled CPC system remained technically stronger on pressure/temperature certification but defeated the one-hose workflow and added a box plate, four permanent couplings, four jumper inserts, arm service loops, and a splitter.
- Decision drivers: direct click-on use of the supplied hoses, cold moto sprayer capability, no box-side water panel, no arm, minimal setup, robust panel support, replaceable commodity adapters, dust protection, and preservation of the existing two accessible camper service valves.
- Result: mount the HOTTAP directly to the exterior box side on Joolca's structurally backed vehicle quick plate and cover. Build one camper plate with two Sea-Dog `513120-1` 316-stainless straight-through washdown outlets (`1/2 in FIP x 3/4 in MGHT`), each fitted with a Melnor `2MQC` faucet adapter; label BLUE cold out and RED hot return. The Sea-Dog backs connect directly to existing `UP120A5` MNPT-to-PEX adapters behind the two existing full-port ball valves. Use the included `1 m` female/female hose for camper BLUE to heater inlet if reach passes without strain, and the `4 m` female/female hose from heater outlet either to the shower handle/head or camper RED. For a cold moto rinse, connect the `4 m` hose from camper BLUE directly to the shower handle/head. No CPC set, box plate, permanent hot splitter, or extra hose is required for one-outlet-at-a-time use.
- Follow-up: obtain one Melnor `65134AMZ` kit and the exact HOTTAP/hoses before drilling; bench-snap every mating combination and verify both included hose lengths. Mock two Sea-Dog outlets on a backed plate, confirm wall/core/backside clearance, label/cover geometry, and service-valve access. Pressure-test the real pump below Melnor's published `80 PSI` ceiling; verify hot-only faucet flow above the HOTTAP minimum; leak-test, drain-test, and test ignition/temperature rise at intended elevation while returnable. Use the supplied threaded Sea-Dog caps by removing the `2MQC` adapters for travel until measured TPU tethered caps or a small protective hatch are proven.
- Supersession: `D-057` replaces only this decision's Sea-Dog/Melnor camper-port stack and travel-cover routine. The direct exterior HOTTAP mount, supplied-hose reuse, one-outlet-at-a-time modes, and absence of a box-side plate/arm/splitter remain active.

- ID: D-057
- Date: 2026-07-26
- Decision: Use compact self-sealing Koolance QD3 camper ports with removable QD3-to-Joolca adapter keys; reject the Sea-Dog plus travel-exposed plastic faucet-adapter stack.
- Context: The owner rejected permanent Melnor `2MQC` faucet adapters as visually bulky, vulnerable to road damage, and operationally self-defeating because the Sea-Dog threaded cap required screwing each adapter on/off at every camp. The HOTTAP V2 Essentials, Quick-Release HOTTAP Bracket, and HOTTAP V2 Mount Cover were subsequently purchased `2026-07-26`; only receipt and physical integration remain open for those three items. The straight-through Sea-Dog and male `2MQC` also provide no automatic shutoff, making the interior BLUE ball valve part of every disconnect routine. The desired exterior remains two small discrete nubs with no hatch, box, or large service fixture.
- Options considered: cheaper Melnor `237-337` plastic kits; Morvat all-brass garden-hose couplings; a roughly `2.75 in` cutout / `3 in` deep all-metal RV spray-port fixture; permanent Sea-Dog/Melnor hardware with manual valves; and Koolance `QD3-FT10-P` no-spill female panel couplings. The Melnor kit preserves the verified Joolca profile but not the appearance, road robustness, or shutoff. Morvat and Melnor's newer brass `15409` profile are not officially verified against Joolca. The RV spray-port fixture violates the small-penetration/no-hatch constraint.
- Decision drivers: automatic shutoff on both disconnected halves, metal wetted construction, one small round panel penetration per port, no routine valve or threaded-adapter step, easy color labeling/capping, bidirectional hot/cold service, and retention of the existing Joolca hose workflow.
- Result: prototype two Koolance `QD3-FT10-P` female panel couplings (`M18 x 1.0` shank, `10 mm / 3/8 in ID` rear barb) as BLUE cold out and RED hot return. Keep the two accessible camper ball valves for service/winterization but not routine setup. Build two permanently assembled removable keys: `QD3-MTN14` male no-spill -> `1/4 in FNPT x 3/4 in MGHT` brass reducer -> proven Joolca-compatible male garden QuickConnect. Fit-test Melnor brass `15409` first for an all-metal key; if it does not snap into the real Joolca hose, use verified-profile `2MQC` only on the removable key, never as travel-exposed wall hardware.
- Follow-up: buy/prototype one complete port/key before duplicating. Bench-prove QD3 shutoff in both directions, actual Joolca hose fit, hot flow, drainability, adapter-key rigidity, and simple stretch-cap fit. Confirm the actual thin backed plate, nominal `M18` clearance hole, locknut/tool access, short reinforced-hose route, dissimilar-metal isolation, and approximately `33.1 mm / 1.30 in` exterior projection before any camper cut. Koolance specifies water/glycol wetted materials but not potable-water or exterior-road certification, so retain the wash-water boundary and cap/inspect the ports.
- Supersession: `D-058` demotes QD3 from lead design to premium fallback after the owner challenged its cost, non-potable positioning, unnecessary `1/4 in` adapter step, and second-ecosystem key complexity.

- ID: D-058
- Date: 2026-07-26
- Decision: Make a direct Joolca/Melnor-profile metal wall plug on a compact stainless bulkhead the lead camper-port prototype; retain QD3 only as the premium automatic-shutoff fallback.
- Context: The HOTTAP is purchased and its real hoses can now control the decision. The camper plumbing is `1/2 in PEX-B`, and valves plus `UP120A5` PEX/MNPT adapters are already in hand. The QD3 design solved exposed-flow shutoff but introduced a second coupling standard, two adapter keys, `1/4 in NPT` to `3/4 in GHT` reducers, rear hose-barb transitions, high delivered cost, and no potable-water listing. Research found no compact all-metal automatic-shutoff panel coupling that simultaneously offers direct Joolca-profile mating, direct `1/2 in PEX-B`, and NSF/ANSI 61 certification. CPC HFC35/APC and LinkTech food-service families are generally NSF/ANSI 169 rather than drinking-water-system listings. Joolca's own current manual says HOTTAP is not allowed to supply drinking or sanitary water, so the whole external/heated circuit remains recreational wash hardware regardless of coupling brand.
- Options considered: retain QD3; substitute CPC/LinkTech/Kent industrial couplings; use a large RV spray-port or hatch; use a plastic Melnor `4MQC` water-stop socket plus the supplied double-male hose coupler; or expose one robust metal Joolca-compatible male plug on a small GHT bulkhead and use an immediately accessible manual service valve.
- Decision drivers: fewest wetted joints, direct `PEX-B` transition, use of the supplied Joolca hose ends without a loose key, compact metal exterior hardware, low cost, physical testability at a local hardware store, and no large hatch/box.
- Result: lead prototype per port is `1/2 in PEX-B -> accessible valve -> shortest supported PEX-B -> purchased UP120A5 -> compact 304-stainless bulkhead (1/2 in FNPT rear / 3/4 in MGHT front) -> physically verified metal Joolca-compatible tap adapter`. RAINPAL `SSBF020` is the first bulkhead candidate (`27 mm / 1-1/16 in` opening, `36 mm` flange, maximum `6 mm` panel when the outer GHT is used). Melnor `15409` is the first metal plug candidate because Joolca explicitly documents Melnor QuickConnect compatibility; GARDENA `39004-G` / UPC `066283390047` is second. A direct `PEX-B x MNPT` combination valve such as NSF/ANSI 61-G Legend `T-805MNL` may replace the separate valve/short PEX/UP120 stack only if the physical depth mockup earns the additional purchase. The manual-valve routine is explicit: connect closed, open active port(s), close and relieve before disconnecting. QD3 remains fallback if the real-hose test cannot produce a clean metal direct-profile plug or if one-click automatic shutoff later proves worth the cost and key.
- Follow-up: when the HOTTAP arrives, take one hose and the included double-male hose coupler to the store. Test Melnor `15409` first, use plastic Melnor hardware as the documented-profile control, then test GARDENA `39004-G`, Orbit/Gilmour/Morvat, or other metal families only as separate profiles. Separately test the Joolca double-male coupler in a Melnor `4MQC` water-stop socket as the inexpensive automatic-shutoff fallback. Bench-pressure-test the chosen stack, verify cap fit and valve access, and prove the bulkhead's panel/backer thickness before any camper cut. Preserve the supplied `5 m` shower assembly (`4 m + 1 m` red sections); after fit testing, prototype a separate approximately `30 in`, `3/4 in F-GHT x M-GHT` cold leader with Melnor `9MQC` and `8MQC` female sockets. The `1 m` red section remains the no-purchase cold-feed trial only; do not cut it without a published Joolca retermination method.
- Supersession: `D-061` closes the direct-port prototype gate with the owner-confirmed installed RAINPAL/HQMPC hardware, one BLUE source valve, unvalved RED return, and clicked-on travel-cap routine.

- ID: D-059
- Date: 2026-07-27
- Decision: Treat the owner-confirmed WS500 `PH-VAN` harness as one combined regulator-power/positive-voltage-sense lead protected by one `15A` bank-voltage-rated fuse/holder; retire the former separate `3A F-13` purchase line.
- Context: The active BOM still carried separate regulator-power and positive-sense fuse rows even though the physical harness was confirmed as `PH-VAN`, and the owner requested a manual technical review after confirming the Mechman alternator, WS500, and APM-48 are purchased.
- Decision drivers: Match the installed harness and current Wakespeed VAN/internal-BMS diagram, avoid redundant fuse hardware, preserve the required high-voltage interruption rating, and distinguish conductor/control protection from the APM-48 parallel load-dump clamp.
- Result: Active row `171` now owns one `15A` `F-12/F-13-PHVAN` fuse/holder; row `320` is inactive. Row `170` remains planned for one `150A` high-voltage MEGA at Lynx Slot 3 and row `176` remains planned for the local `3A` Upfitter #3 enable circuit until physical inventory closes them.
- Follow-up: Verify the exact fuse/holder markings and fit before energizing. The purchased row `321` empty `80V` FKS housings are candidates only if the matching contacts and actual `PH-VAN` red-lead wire gauge are compatible; the purchased `20A` FKS fuse stock is not the required `15A` fuse.

- ID: D-060
- Date: 2026-07-31
- Decision: Make the MultiPlus external chassis/PE connection mandatory and keep AC protective earth, AC neutral bonding, and DC negative references as three separate design roles.
- Context: The MultiPlus had been live-tested during earlier bench work, but the final mobile-installation chassis lug, aluminum-shell bond, and interaction with the future case-grounded or isolated-ground Mechman path had remained vague. The current official Victron MultiPlus-II 120V manual identifies the exterior `M6` as the primary PE connection, requires at least `4 mm²` grounding conductor, requires the casing to be connected to the vehicle chassis when shore unplugging removes source earth, and documents the internal neutral-to-chassis ground relay.
- Decision drivers: manufacturer instructions, uninterrupted fault-current return with shore disconnected, correct GFCI operation in both inverter and shore modes, avoidance of an unreliable aluminum-shell-only path, and prevention of a DC return that bypasses the SmartShunt.
- Result: run `10 AWG` green stranded copper from MultiPlus `M6 PE` to a verified truck-chassis bond point; add a separate corrosion-compatible shell bond into the same equipment-ground network; do not add a MultiPlus case/PE-to-DC-negative jumper or fixed downstream neutral-ground bond; leave the internal MultiPlus ground relay enabled. Add BOM row `339` for measured bonding wire/lugs/hardware.
- Follow-up: measure the routes, inventory/buy row `339`, install and continuity-test both bonds, test both GFCIs in inverter and accepted-shore modes, physically confirm Mechman isolated-vs-case-ground behavior, and prove no chassis path bypasses the SmartShunt before alternator commissioning.

- ID: D-061
- Date: 2026-08-01
- Decision: Accept the installed direct RAINPAL/HQMPC BLUE/RED camper ports and use only one source valve on BLUE; RED remains an unvalved removable-hose return to faucet hot.
- Context: Owner installed both `27 mm / 1-1/16 in` RAINPAL bulkheads after relieving the rear fiberglass for locknut access. The HQMPC male QDs project farther than ideal but connect correctly, and the owner-designed clicked-on travel caps fit and operate correctly.
- Decision drivers: actual in-hand fit and operation, minimum joint count, direct Joolca hose workflow, easy RED depressurization at faucet hot, and avoidance of an unnecessary second valve/QD ecosystem.
- Result: retain the installed stack. BLUE closes before hose changes; RED depressurizes by shutting down the HOTTAP and opening faucet hot, then drains/blows toward the sink with regulated low-pressure air as needed. QD3, GARDENA, and Legend substitution paths are inactive fallbacks.
- Follow-up: verify local aluminum backing/load spread, seal exposed laminate/core edges, witness-mark locknuts, complete a dry pressure/dwell test after final sink/sender work, and inspect for looseness after pull/cycle testing and the first drive.

- ID: D-062
- Date: 2026-08-05
- Decision: Treat the physically routed USB-PD baseline as three independent `12 AWG / 15A` branches—one Desk and two Galley—and reopen a small field-fit number of downstream AC receptacles behind the two first-in-chain GFCIs.
- Context: Owner reports all three PD routes, pump, fridge, and KUS wiring are in place and both first GFCIs are wired on separate breakers; earlier planning documented only two PD stations and treated downstream receptacles as obsolete.
- Decision drivers: match the physical build, preserve branch independence, use the already-installed GFCI architecture correctly, and avoid inventing the third fuse-panel position from stale planning.
- Result: Electrical overview, AC implementation, README posture, live checklist, and log now reflect three PD branches and optional downstream devices from GFCI `LOAD` only. D-022's shared `12V` source architecture remains valid, but its two-PD-branch quantity is superseded.
- Follow-up: identify/label the actual third PD fuse-panel slot, measure the final run, prove polarity/load/voltage drop, and inventory/lock downstream AC device count before procurement or closeout.

- ID: D-063
- Date: 2026-08-05
- Decision: Use one rugged fixed-body RJ45 panel bulkhead for both roof and ground Starlink deployment, and carry the Standard 4 X in a four-fastener protective frame on movable extrusion crossbars.
- Context: Owner wants the roof cable to disconnect cleanly at the camper, wants an ordinary long Ethernet cord to support ground deployment, and is concerned that the current bare mobility mount leaves the terminal edges exposed to branches.
- Options considered: existing service opening with inline coupler, large multi-cable through-bulkhead gland, two-panel etherCON route, purpose-built consumer wall socket, bare corner mounts, full protective enclosure, and a protective edge frame.
- Decision drivers: rugged PoE Type 4 interface, weather protection when mated/capped, ordinary RJ45 fallback compatibility, minimum panel cuts/interfaces, four-screw serviceability, edge protection, kickstand retention, and clear tight-trail removal.
- Result: select the Neutrik `NE8FDX-P6-W` as the fixed panel interface; use a compatible rugged Neutrik cable-side termination on the removable retractile jumper after OD verification; use a TRIO Gen 3 Standard Speedmount as the protective/removable terminal frame. The initial crossbar-only/color posture is superseded by D-064. Keep the complete OEM cable as direct recovery. Solar remains a later electrically/mechanically separate route.
- Follow-up: verify camper wall stack/interior clearance, coil tangent OD/conductors, exact cable-side part compatibility, crossbar profile/spacing, roof travel, strain relief, and loaded Starlink performance before cutting the wall or premade coil.

- ID: D-064
- Date: 2026-08-06
- Decision: Preserve both removable magnetic and extrusion hard-mount paths for the TRIO-framed Starlink terminal.
- Context: Owner purchased the white Gen 3 Standard Speedmount and intentionally included both TRIO's rubber-coated magnet/VHB-disc package and the `75 mm` stainless through-bolting option.
- Options considered: magnet/disc package only, crossbar hard mount only, or buy both attachment packages before the roof/contact mockup.
- Decision drivers: removal speed, no immediate irreversible roof commitment, existing roof-track/extrusion fallback, and the small incremental cost of retaining both factory-supported attachment paths.
- Result: TRIO order placed for the white Speedmount with `75 mm` through-hardware at `$285`, magnets at `$40`, and VHB-backed discs at `$40`; `$365` total with free shipping. The `75 mm` hardware attaches frame to extrusion and does not replace separate roof-track-to-extrusion T-bolts.
- Follow-up: on receipt, prove terminal/frame fit, roof-disc full contact, removal ergonomics, supplied fastener diameter/stack, crossbar span/stock, and independent tether geometry before bonding discs or drilling extrusion.

- ID: D-065
- Date: 2026-08-08
- Decision: Put the separate Wakespeed `500A/50mV` alternator shunt in the dedicated `2/0` negative return near the house board, eliminating the two positive-shunt `5A` fuse positions; retain one `15A/80VDC` fuse on the PH-VAN red combined regulator-power/positive-sense lead.
- Context: Wakespeed allows either shunt polarity. Positive placement avoids any chassis-return bypass but makes both millivolt sense wires full-bank-positive conductors requiring individual protection. The owner rejected three expensive/slow special-fuse purchases and asked for a proportional design review.
- Decision drivers: The active architecture already prohibits MultiPlus PE/case-to-DC-negative and other parallel `48V` chassis returns; the Mechman dedicated negative cable is intended to be the single normal alternator return. Negative shunt placement therefore removes two fuse/holder assemblies without weakening the required protection on the actual `16 AWG` PH-VAN power lead.
- Result: `ALT B-/case -> long 2/0 -> Wakespeed shunt -> short 2/0 -> Lynx negative`; grey/current-sense-low on the alternator side, purple/current-sense-high on the Lynx side; configure `Shunt at Alternator`. Buy only one low-cost `15A/80VDC` Littelfuse `166.7000.5152` or verified equivalent for PH-VAN red. Littelfuse confirms the owned `178.6150.0001` housing accepts FKS fuses at `80VDC`; only contacts/wire fit remain open.
- Follow-up: With all sources isolated and the alternator negative return disconnected, verify Lynx negative has no stable low-resistance continuity to chassis. If a parallel bond exists, stop and remove it or reopen protected positive-shunt placement before charging. Verify positive charge-current sign against an independent clamp meter during first commissioning.

- ID: D-066
- Date: 2026-08-08
- Decision: Supersede D-065 with the Wakespeed shunt in the common battery-negative path after the Victron SmartShunt; use `F-04 200A/80V` and a Mersen Class-CC PH-VAN branch.
- Context: A whole-system re-review compared positive-shunt, dedicated alternator-negative-shunt, no-shunt, and common battery-negative-shunt layouts. Wakespeed's standalone PH-VAN/internal-BMS-no-communication example places the analog shunt in the battery path. The owned Littelfuse blocks are empty housings with proprietary contacts and are not worth completing.
- Decision drivers: preserve net battery-current feedback without CAN/DVCC, prevent chassis-return geometry from bypassing the measurement, remove both `5A` sense-fuse positions, keep the alternator dedicated negative direct to Lynx, and use obvious screw-terminal protection for PH-VAN red. Mechman's published `48V Elite` curve reaches about `145.7A`; `125%` is about `182A`, making `200A` the next standard MEGA value for the existing `2/0` cable.
- Result: `battery negative combine -> SmartShunt -> Wakespeed 500A/50mV shunt -> Lynx/system negative`; purple/high faces battery/SmartShunt, grey/low faces Lynx/system, configure `Shunt at Battery`. Alternator `B- -> dedicated 2/0 -> Lynx negative`. `F-04=200A/80V`. PH-VAN red uses Mersen `USCC1 + ATDR15` in a small separate DC DIN enclosure, fed from the `F-04` alternator/load-side stud.
- Follow-up: read and record the Mechman-supplied WS500 configuration before altering it; confirm shunt stud fit, output/nameplate, charge ceiling, field derate, current sign, temp sensors, APM state, and `<0.1V` charge/return drops during controlled commissioning.

- ID: D-067
- Date: 2026-08-09
- Decision: Preserve the SmartShunt-to-Lynx hard connection by putting the Wakespeed shunt on the battery side, and eliminate the separate DC fuse-panel/DIN-enclosure concept.
- Context: The owner confirmed the Victron SmartShunt is physically hard-attached to the Lynx and rejected a bulky DC fuse panel. Series-shunt order does not change the net battery current measured when every source and load remains on the Lynx/system side.
- Decision drivers: fit the real mechanical layout, preserve both shunts' full-current measurement, avoid any bypass, protect the PH-VAN red lead at 48V-bank fault potential, and minimize volume and part count.
- Result: `battery negative combine -> Wakespeed 500A/50mV shunt -> Victron SmartShunt -> Lynx/system negative`; purple/high faces battery negative and grey/low faces SmartShunt/Lynx. Configure `Shunt at Battery`. PH-VAN red uses one Eaton/Bussmann `HEB-AA` in-line holder with one Littelfuse `KLKD015.T` `15A/600VAC/DC` midget fuse next to `F-04`; no DC fuse panel, DIN rail, or enclosure.
- Supersedes: D-066 only where it placed the Wakespeed shunt after the SmartShunt or selected the `USCC1/ATDR15` DIN-enclosure package. D-066's `Shunt at Battery`, no-`5A`-sense-fuses, and no-bypass requirements remain active.
- Follow-up: verify Wakespeed-shunt stud fit and jumper length before cable fabrication; commission against a clamp meter and verify positive charging-current sign.

- ID: D-068
- Date: 2026-08-09
- Decision: Reject the earlier `800-1200W` Yuma CIGS posture as geometry-invalid and make a field-proven `66 in` shallow track-cassette width the gate for the `800W` high-output path.
- Context: The historical solar matrix screened electrical compatibility and panel weight but did not compare raw CIGS panel area against the newly supplied `134 x 62 in` roof, MaxxFan, and Starlink envelopes. Two external AI packages then produced only `400-500W` CIGS and tolerance-fragile `760-800W` Lensun layouts.
- Options considered: force `800W` Yuma CIGS with direct bond, accept `400-500W` CIGS, use premium high-efficiency direct-bond modules, build a full roof rack, or reclaim only the width needed with shallow Yakima-track cassettes.
- Decision drivers: `57.69 sqft` total modeled roof versus `59.37-61.53 sqft` of Yuma panels alone for `800W`; modeled `3.915 kWh` core workday; existing Victron `150/45`; low roof height/branch exposure; thermal performance; replacement access; and all-up `75 lb` moving-roof uncertainty.
- Result: Lead high-output candidate is `4x Lensun 130W + 4x Lensun 70W = 800W`, `4S2P`, on removable vented panel-specific cassettes only if field measurements prove `134 x 66 in` safe supported width. Premium direct-bond fallback is `4x Solbian SP138 = 552W`, `4S1P`, on the modeled `134 x 62 in` skin. Yuma CIGS is limited to `400W / 4S` on the purchased controller; the physical `500W` layout requires a `250V` MPPT and is not the preferred leverage point. The `760W` AI layouts are rejected because the current Lensun `120W` dimensions differ from the package.
- Follow-up: measure the real common-origin roof/rail/fan/Starlink grid; prove or reject `66 in` carrier width; get Hiatus's all-up interpretation of the `75 lb` limit; obtain written manufacturer mounting/ventilation/warranty approval; template exact current SKUs and junction boxes; then run final cold-`Voc`, hot-`Vmp`, fusing, conductor, disconnect, and moving-jumper calculations before procurement.

## Risk register
- ID: R-001
- Risk: Roof load from rigid/flexible solar + Starlink + fan may exceed comfortable strut margin.
- Impact (1-5): 4
- Likelihood (1-5): 3
- Mitigation: Confirm with Hiatus whether `75 lb` covers all moving-roof additions; weigh panel/cassette/crossmember/fastener/Starlink/cable hardware as one system and validate lift effort/strut margin before panel release.
- Trigger: Final solar panel selection.
- Owner: Sunny
- Status: Open

- ID: R-002
- Risk: Remaining service-map decisions (solar, shore, diesel, and the selected HOTTAP water-service interface) can still drive bad penetrations or inaccessible closeout geometry.
- Impact (1-5): 4
- Likelihood (1-5): 3
- Mitigation: Validate each complete inside/outside route before cutting. For Starlink, mock the selected Neutrik panel wall stack, interior cable/service access, retractile-jumper travel/strain relief, and four-fastener protective crossbar mount; preserve the OEM cable as the no-cut recovery path. For hot water, prove the rear-box cylinder restraint/vents, purchased Quick-Release HOTTAP Bracket backing and HOTTAP V2 Mount Cover, single BLUE/RED camper plate, supplied-hose reach, port protection, and operating clearances; no propane passthrough enters the camper.
- Trigger: Any final shell/floor/wall penetration or permanent service-map closeout.
- Owner: Sunny
- Status: Open

- ID: R-003
- Risk: Battery cold-charge protection may be incomplete without validated sensor/relay logic.
- Impact (1-5): 5
- Likelihood (1-5): 2
- Mitigation: Require BMS low-temp charge cutoff and test thermostat-controlled heater branch.
- Trigger: First low-temperature use scenario.
- Owner: Sunny
- Status: Open

- ID: R-004
- Risk: Simultaneous high-draw AC loads can exceed inverter continuous output and cause nuisance trips.
- Impact (1-5): 4
- Likelihood (1-5): 3
- Mitigation: Enforce load-sequencing SOP, keep the locked propane-only HOTTAP path off the AC system, and validate AC branch design in bench testing.
- Trigger: Final appliance mix and first full-load test.
- Owner: Sunny
- Status: Open

- ID: R-005
- Risk: Combined installed + owner-supplied office loads reduce no-charge autonomy to roughly `2.7-3.2` workdays in the conservative future-audio model (season-dependent) even with the 3-battery bank; actual near-term office-only use may be better.
- Impact (1-5): 4
- Likelihood (1-5): 3
- Mitigation: Enforce SOC reserve policy, lock charging strategy (solar + alternator + shore cadence), and validate real duty cycles in shakedown tests.
- Trigger: Consecutive low-sun days or high winter-duty cycle operations.
- Owner: Sunny
- Status: Open

- ID: R-006
- Risk: Dedicated `48V` secondary-alternator commissioning could still fail on electrical integration details (`PH`/`NH` harness polarity, field-voltage/derate, grounding/isolation behavior under charge, WS500 profile, and load-dump mitigation closure).
- Impact (1-5): 4
- Likelihood (1-5): 2
- Mitigation: Mechanical/idler/staged-driving concern is closed by owner/Mechman confirmation. Keep live charging gated until harness polarity/accessory set, regulator profile, APM, required fusing, the negative-shunt no-bypass continuity proof, dedicated return, shunt polarity/current sign, and first-run shutdown behavior are verified.
- Trigger: WS500 wiring closeout and first alternator charging commissioning.
- Owner: Sunny
- Status: Partially mitigated; mechanical/drivability gate closed, electrical commissioning gates open

- ID: R-007
- Risk: High-fault-current `48V` battery architecture can produce severe arc/thermal events during commissioning or service if isolation, torque, polarity, or fuse-voltage controls are missed.
- Impact (1-5): 5
- Likelihood (1-5): 2
- Mitigation: Enforce documented pre-energization checks (polarity, torque witness, correct fuse voltage class, bus insulation covers, disconnect/isolation verification) and require controlled service procedure. First energization passed without observed faults; post-live cleanup still needs labels/covers/torque-witness/service-access verification.
- Trigger: Any major rewiring event, cover/label closeout, and post-energization inspection.
- Owner: Sunny
- Status: Partially mitigated by first live `48V` test; inspection closeout pending

- ID: R-008
- Risk: Propane leak, box accumulation, or combustion byproduct exposure could occur if the selected rear-box cylinder/HOTTAP package has inadequate restraint/venting, hose protection, deployed clearance, leak testing, or detector coverage.
- Impact (1-5): 5
- Likelihood (1-5): 3
- Mitigation: Keep the HOTTAP on its structurally backed exterior vehicle mount and never burn it inside the box/camper; prove cylinder restraint and permanent low/high vents, mounted-cover/travel state, regulator/service-hatch sweep, operating clearances, parked-only water-hose state, LP/CO/smoke detection, and leak testing before first burn.
- Trigger: Rear-box package fabrication, any LP connection change, first HOTTAP burn, or recurring pre-trip inspection.
- Owner: Sunny
- Status: Open

- ID: R-009
- Risk: AC shock/fire risk from neutral-ground misconfiguration or incomplete GFCI/RCD protection on branch circuits.
- Impact (1-5): 5
- Likelihood (1-5): 2
- Mitigation: Preserve AC protection chain (`source/adapters -> portable EMS -> shore cord -> L5-30 inlet -> AC-in breaker -> MultiPlus -> 30A AC-out main -> 20A branch breakers -> GFCI receptacles`), validate outlet polarity and GFCI/RCD operation at commissioning, keep AC-in and AC-out neutrals isolated, and verify ground continuity/chassis bonding. Short AC-in shore-charge test passed; AC-out/GFCI validation remains open.
- Trigger: AC branch wiring completion and AC-out/GFCI live test.
- Owner: Sunny
- Status: Partially mitigated; AC-in function passed, AC-out/GFCI pending

- ID: R-010
- Risk: Roof-to-shell coiled solar jumper routing can chafe, snag, or leak at passthrough points if cable travel and strain relief are not validated through popup cycles.
- Impact (1-5): 4
- Likelihood (1-5): 3
- Mitigation: Use UV/weather-rated cable, abrasion sleeves, drip loop + strain relief, and repeat open/close travel-cycle checks before final sealing.
- Trigger: First full roof open/close cycle test with finalized cable length and routing.
- Owner: Sunny
- Status: Open

- ID: R-011
- Risk: AC scope churn (final receptacle count and branch utilization not fully closed) can delay SKU lock and cabinet fit validation.
- Impact (1-5): 4
- Likelihood (1-5): 3
- Mitigation: D-044 closed the purchase gate with one explicit branch/receptacle map: two active `20A` GFCI branches behind a `30A` AC-out main in one `6-way` DIN enclosure. Do not add a third active AC branch without revisiting feed/protection/enclosure scope.
- Trigger: Any attempt to add AC receptacles/branches beyond the purchased `2x` GFCI baseline.
- Owner: Sunny
- Status: Mitigated by D-044; monitor install fit

- ID: R-012
- Risk: Travel/logistics compression could put the truck too far from Bellingham for the May 7 `9:00 AM` install.
- Impact (1-5): 5
- Likelihood (1-5): 2
- Mitigation: Historical only. Owner confirmed the May 7 install happened; travel, tailgate, tonneau, and arrival-buffer logistics are no longer active build risks.
- Trigger: Historical May 2026 shell-install logistics.
- Owner: Sunny
- Status: Closed / historical (owner confirmed 2026-05-17)

- ID: R-013
- Risk: Remaining bed gaps, lifted tape, or poorly sealed hardpoint areas can admit dust or splash under the EPS/plywood.
- Impact (1-5): 5
- Likelihood (1-5): 3
- Mitigation: The bed cavity is now closed by the permanent floor. Do not reopen it speculatively; monitor known perimeter/hardpoint paths after the first dusty/wet drives and investigate only actual dust trails, dampness, odor, swelling, or floor movement that justifies destructive access.
- Trigger: Lifted tape, an obvious open path, unexplained dampness/dust trail, or first-drive evidence of ingress.
- Owner: Sunny
- Status: Accepted/monitoring after permanent floor closure; underfloor rework is evidence-triggered only

- ID: R-014
- Risk: The permanent Lonseal installation may retain cosmetic waviness/bumps, edge lift, adhesive-contaminated hardpoint holes, or hidden substrate conditions that are no longer cheaply serviceable.
- Impact (1-5): 5
- Likelihood (1-5): 3
- Mitigation: Keep heavy modules off for `72 hr` after actual adhesive completion; remove/clean/reinstall temporary clamp bolts carefully during cure; remove boards and photograph/inspect all edges, hardpoints, and raised/hollow areas after cure; accept stable cosmetic irregularity or define a localized repair before modules hide it. Protect the floor during every reinstall.
- Trigger: Binding/spinning hardpoint bolt, loose/expanding edge or hollow area, board/washer imprinting, moisture, substrate movement, or damage during module reinstall.
- Owner: Sunny
- Status: Realized/monitoring; glue-down completed `2026-07-15`, post-cure inspection pending

- ID: R-015
- Risk: Modules can rack, shift, or create service problems if rivnuts are poorly set, bolts are inaccessible, clamp load crosses unsupported EPS, or heavy assemblies are left visibly loose.
- Impact (1-5): 5
- Likelihood (1-5): 3
- Mitigation: Use the owner-selected stainless rivnuts, verify firm collapse/no spin and usable threads, keep clamp load off EPS, record the location map, preserve service access, and use practical tabs/tie-ins where a heavier module needs more than one point of retention.
- Trigger: Pickup-box drilling, insert procurement/installation, heavy-module reinstall, filling the water tank, installing batteries, or any road test.
- Owner: Sunny
- Status: Open / rivnut installation and restrained-reinstall gate

- ID: R-016
- Risk: Battery first-charge or paralleling error can create BMS trips, high-current faults, or mismatched parallel-bank behavior.
- Impact (1-5): 5
- Likelihood (1-5): 2
- Mitigation: MultiPlus LiFePO4 profile has been configured/owner-verified by first-battery behavior; keep source-current limit matched to the shore circuit, log voltage/SOC/temp during meaningful charge sessions, and verify parallel-bank behavior during future controlled charge/load use.
- Trigger: Sustained shore charging, any high-SOC charge session, and first logged parallel-bank current-sharing check.
- Owner: Sunny
- Status: Partially mitigated; charger-profile programming closed, parallel-bank behavior and physical install/strain-relief gates still open

- ID: R-017
- Risk: Workstation/monitor/electrical-shelf mechanisms can collide with the pop-down roof or become vibration projectiles if stow height, cable loops, shelves, panels, or latches are validated from assumptions instead of real shell measurements.
- Impact (1-5): 4
- Likelihood (1-5): 3
- Mitigation: Use the driver-side workstation implementation gates: roof-down sweep map, stowed monitor block test, DC shelf/box interference check, positive travel locks on monitor/leaf/drawers/panels, cable drag-chain/service-loop checks, and post-drive re-torque/witness-mark inspection.
- Trigger: Building the driver-side desk, monitor mount, electrical closet/DC shelf, diesel-heater service panels, or any storage above the marked roof-safe line.
- Owner: Sunny
- Status: Open

- ID: R-018
- Risk: Passenger-side lofted fridge/wet-spine plumbing can become inaccessible, freeze-prone, or hazardous to adjacent batteries if the `36 gal` tank fittings, pump, accumulator, graywater cassette, fill/vent lines, heater branches, or leak paths are trapped behind finished work without a known disassembly path.
- Impact (1-5): 5
- Likelihood (1-5): 3
- Mitigation: Owner confirms four molded ports on each end—two visibly large and two smaller—with no original obvious/open top port. The tank is now physically strapped into the hard-mounted Galley structure, but the `2026-07-27` first `FLS-U` assembly damaged at least one backing-ring thread, left one screw without clamp load, and poured water through the main gasket during an inverted test. Preserve top sender access and hold water service/first fill—not dry fabrication—until the seized screw and damaged C-ring are recovered without enlarging the opening, the ring/main gasket/matched long screws are replaced, the sealing land/sender flange are inspected, and the leak test passes. Continue to require continuous gravity-fill fall, unrestricted vent rise, compact minimum-fitting pump/accumulator pack, wet/dry separation, leak inspection, and a documented cooler/panel/80/20 removal sequence.
- Trigger: Building passenger-side lofted fridge skeleton, galley cabinetry, tank restraint, pump board, battery bench partition, graywater cassette, or rear shower/fill/vent hatch.
- Owner: Sunny
- Status: Open

## Open questions
- Recover the actual `2026-07-15` #650 completion time if possible; otherwise keep evening `2026-07-18` as an earliest-only heavy-furniture planning estimate.
- During cure, back out/clean/reinstall the temporary edge-board bolts one at a time and record any binding, galling, or spinning rivnut.
- After cure, photograph/classify the mild waviness/bumps and lifted edges: stable cosmetic condition vs localized loose/raised/hollow repair area.
- Build and prove positive restraint for the `3x 48V` batteries, separate `12V` battery, and ICECO cooler while the service bay remains open; preserve battery extraction and emergency fuse/disconnect access.
- Create the final `36 gal` tank port map from physical inspection: verify the reported four end ports per side (two large/two small), identify exact thread sizes and any membrane-covered top boss, then lock KUS sender location/backing, upper-end gravity fill/vent, low north pump outlet, low tank drain, spare/plug ports, and manufacturer-compatible fitting methods.
- Verify the newly tightened tank-strap plusnut screws achieved clean full thread engagement; witness-mark the hardware and recheck after the first loaded drive.
- Finish the installed shore inlet's enclosed `L/N/PE` splice/dead checks. Separately, locate/mock the selected Starlink `NE8FDX-P6-W` panel interface in fixed-body structure below the moving seam, verify rear service access and wall stack, measure the candidate coil OD and popup travel, and dry-fit the TRIO frame/four-fastener extrusion-crossbar geometry before cutting the wall or cable.
- Lock Nick black-walnut commission details: exact Galley counter length/width (`~4 ft x 19 in` target pending confirmation), `1.5 in` vs `2 in` thickness, last `~15 in` live-edge curve, Desk dimensions, L-shaped Bench/lid hinge/support/gas-strut geometry, finish sample, price, and delivery timing.
- Verify the now-integrated electrical/Bench/Galley structure's remaining road details: battery/cooler capture, terminal covers, fastener witness marks, anti-rattle interfaces, strain relief, and emergency disconnect/fuse access.
- Log parallel-bank current-sharing/voltage behavior under controlled charge/load; use similar total loop resistance per battery path rather than forcing equal positive-only leads.
- Finalize ICECO travel restraint using its foot-level tie points, a low-stretch strap to anchored extrusion, an aisle-side hard stop, and a soft camper-wall bumper without blocking vents, lid swing, power-cord bend, or pump access.
- Measure the driver-side desk/monitor/electrical-shelf roof-down sweep envelope, choose the primary monitor mechanism (`rising VESA spine` vs under-desk flip-up vs quick-release sleeve), and validate that the stowed face-down cradle supports bezel/back-shell/VESA structure rather than loading the LCD panel.
- Lock workstation travel restraints: monitor mast/carriage latch, monitor arm hard stop, desk leaf latch, storage-door/service-panel latch standard, and cable-chain/service-loop path below the roof-safe line.
- Confirm actual seated work envelope: chair/stool height, desk height/depth, monitor viewing distance, knee clearance, footrest need, and reachable AC/DC/USB-C station locations.
- Preserve KUS sender access and the documented Galley/tank disassembly path now that the `36 gal` tank and surrounding structure are hard-mounted. Gravity-fill vent nipple measurement is captured (`10 mm` OD main land, `11 mm` OD largest barb); replacement vent tube dry-fit remains open.
- Validate purchased galley fixtures/appliances in the integrated counter module: Sarlai sink cutout, FORIOUS faucet under-counter clearance, drain/graywater path, Duxtop induction use/stow location, and Ninja SP151 cubby heat/retention/plug access.
- Lock drain/graywater, pump service-valve, and winterization details as discrete procurement rows; sink/faucet are now purchased and logged in BOM rows `207-208`.
- Mock the purchased SHURflo/SEAFLO pack in the `6 in` cooler-to-battery gap with strainer access, vibration isolation, nonconductive splash separation, and a drained leak path away from battery terminals/cabling. Two purchased EFIELD `1/2 in PEX-B x 3/8 in OD compression male` adapters terminate the FORIOUS faucet hoses. Install one of the four purchased YVSKM `1/2 in PEX-B x 1/2 in female-swivel` adapters at the accumulator outlet and retain three spares; inspect receipt, markings, gasket/seat fit, and potable-use documentation before acceptance, then cold-pressure-test the assembly. Use the purchased RecPro `30 in` double-FIP braided hose on the pump side and verify the post-accumulator tee, BLUE/RED valve access, service-plate backer, and continuous PEX routes before cutting the rear wall.
- Propane hot-water direction and rear-box package are locked; physical fit-up remains open. Receive and fit the HOTTAP/bracket/cover, Flame King cylinder, CALPOSE gauge, bracket/strap pack, and Safoner propane-hose pass-through in the rear box. The AWW stone mat is outdoor shower gear. Prototype one complete direct-profile camper-water port with the real HOTTAP hose before buying the second or drilling; retain QD3 only as fallback.
- Exact autonomy target by season and reserve floor policy (20% SOC currently modeled)
- Inventory and photograph the remaining loose Mechman/WS500 kit contents—especially temperature sensors, harness branches, terminals, and any supplied fusing—before alternator commissioning; the alternator and WS500 purchase and `PH-VAN` harness identity are owner-confirmed.
- Confirm Wakespeed support status for the documented `Dumfume 51.2V 100Ah` battery manual (`58.4V` charge voltage, `20-50A` recommended charge current per battery, `1S4P` max expansion) before final commissioning of the `WS500`-controlled alternator path
- `PH-VAN` harness polarity is confirmed; confirm whether the Mechman `48V` alternator field is `12V` or true `48V` before applying/removing Wakespeed `48V` field-derate settings.
- Before alternator commissioning, recheck belt tracking, idler alignment, fastener torque/witness marks, noise, field isolation, and output isolation. Mechanically installed/belted but electrically disabled staged driving has been owner/Mechman-confirmed acceptable after those mechanical checks; this does not authorize partial charging.
- Confirm the exact Ford upfitter blunt-cut wire/color/location used for `Upfitter #3` at install time and record the measured control-wire run length for `C-41`
- Confirm the Dumfume manual's `20-50A` recommended charge current is intended to scale across the current `1S3P` bank for alternator-charging use, not just single-battery charging
- Confirm whether the Mechman `48V` secondary-alternator path can be safely supported with an internal-BMS, non-CAN battery bank, including any required load-dump / avalanche-diode / keeper-battery mitigation
- Confirm whether the Mechman `48V` alternator negative/case can remain electrically isolated from chassis in the intended install, or whether the house `48V` system should be treated as engine/chassis referenced
- User-confirmed assumption: losing automatic house-to-starting-battery support is acceptable
- Confirm only that the retained factory alternator continues to handle normal starter/vehicle charging independently if the Mechman `48V` path is adopted
- Confirm measured daily draw for owner-supplied laptop/monitor/tablet charging to replace planning assumptions
- Validate Orion `48/12-30` charger headroom with the current 12V branch plan (including USB stations, `12V-10` Maxxair fan, `12V-06` Hiatus factory LED+dimmer, and planned `12V-11` WLED/QuinLED ambient strips). Audio remains preliminary/future; if `12V-12` KMC2 and `12V-AUDIO-SUB` are later promoted, re-check sustained Orion headroom and buffer-battery behavior before buying.
- Later, if audio is promoted from preliminary: lock camper audio mounting and routing details from `docs/implementation/CAMPER_audio_system.md`: KMC2 face/depth, PTRTP10 dry low location/ventilation/service access, speaker cutout or pod method, RCA/speaker-wire lengths, and loud-test voltage behavior with normal 12V loads running.
- Confirm/document AC dead-checks before AC-out commissioning: AC-in/AC-out neutral isolation, continuous PE/equipment ground, no fixed downstream neutral-ground bond, and staged GFCI test during AC-out commissioning.
- Final passthrough locations for solar and fuel/heater paths, including whether an exterior truck-bed-wall diesel tank/fill/pump can route through a protected grommet/bulkhead to the heater. Shore inlet hardware is selected; final inlet/cable support details are an install-fit task using on-hand clamps/grommets/strain relief.
- Lock roof-to-shell solar jumper connector strategy and exact service-loop length for full popup travel
- Flexible solar model/stringing strategy under roof `75 lb` cap and deferred-procurement timing
- Lock interior/exterior mounting rail ecosystem (rail profile, nut/hardware standard, bracket interfaces) and final linear-foot allowances
- Secondary internet strategy and minimum acceptable fallback performance
- Battery compartment heating and control implementation details (sensor, relay, setpoints)
- Storage/security SOP for flight windows
- Measured fridge compressor duty cycle by ambient band (cold, mild, hot) to replace modeled assumptions
- Lock final fuse-holder SKU standard for Orion output, WS500 low-current fuses, `F-15` upfitter control fuse, and PV string fusing hardware
- Orion `48V` input protection is locked as: Lynx Slot 4 -> one verified `40A` MEGA (`58VDC` minimum under the locked `56.8V` charge ceiling; Victron `CIP138040020 40A/80V` is the replacement fallback) -> existing `6 AWG` pair -> Orion. Retire standalone `F-06` and do not install the purchased MIDI/FKS stock or proposed DIN holder. This is the deliberate lowest-rework feeder-protection choice; `6 AWG` is overkill but safely protected. Keep `6 AWG` and `F-07 60A/80V` on the 30A 12V output.
- BOJACK `150A` AMI/MIDI holder stock purpose resolved: it came from the obsolete Sterling `BB1248120` `12V` input-fuse plan. Keep as obsolete/spare `12V` hardware only; do not use as active `F-04` alternator protection, WS500 fuse hardware, Orion input protection, or any `48V` install part unless separately voltage/form-factor validated.
- Final SKU lock for `F-11` holder family and `SW-12V-BATT` switch model/location
- Confirm acceptable monitoring expectation that Orion is not a direct GX telemetry node in current architecture; current Orion visibility is VictronConnect/BLE
- Confirm final location/format for measured run-length recordkeeping in implementation docs before final cable closeout
- Prove the purchased Quick-Release HOTTAP Bracket/backing and HOTTAP V2 Mount Cover, `10 lb` aluminum cylinder cradle/strap/pad package, fixed low/high box vents, regulator/service-hatch sweep, and full operating clearances with a physical box mockup.
- Lock the two-port BLUE/RED geometry only after the actual Joolca hose fit test and one direct-profile prototype prove bulkhead panel/backer thickness, locknut/valve/backside clearance, metal plug compatibility, hot flow, drainability, road-cap fit, and the measured approximately `19 in` hose reach. Compare QD3 only if the direct profile fails or automatic shutoff earns its key/cost. No large hatch or service box is in scope.
- Define and document recurring leak-test cadence (post-service, pre-trip, and periodic maintenance interval)
- Lock final fire detection/suppression layout (LP detector location, CO/smoke detector locations, extinguisher count/placement)

## Reusable templates
### Daily log
- Date:
- Objective:
- Completed:
- Issues:
- Next actions:

### Test case
- ID:
- Linked requirement:
- Setup:
- Procedure:
- Expected:
- Actual:
- Pass/Fail:

## Source artifacts
- `docs/core/SYSTEMS.md`
- `docs/legacy/PROJECT_workbook_hiatus_consult.md`
- `docs/legacy/SYSTEMS_workbook_build_notes_obsolete.md`
- `docs/implementation/INTERIOR_driver_side_workstation.md`
- `docs/implementation/INTERIOR_furniture_layout_and_galley.md`
- `media/diagrams/interior-furniture-2026-05-04/`
- `docs/implementation/ELECTRICAL_overview_diagram.md`
- `docs/implementation/ELECTRICAL_fuse_schedule.md`
