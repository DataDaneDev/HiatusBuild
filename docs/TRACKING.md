# Tracking

## Assumptions and constraints
- Constraints: truck/camper/dates are fixed constants
- Assumptions to validate: autonomy target, climate profile, load profile, travel cadence impacts
- Working load baseline assumption from load model v3 (BOM + owner-supplied office loads):
- `core_workday`: `3,530 Wh/day`
- `winter_workday`: `4,202 Wh/day`
- `minimal_idle_day`: `624 Wh/day`

## Decision log
- ID: D-001
- Date: 2026-02-11
- Decision: Use workbook `WH` load model as baseline planning input until measured data is available.
- Context: Legacy workbook had a complete daily Wh model; canonical docs had placeholders.
- Options considered: Keep placeholder only or import model now.
- Decision drivers: Better architecture sizing and faster procurement decisions.
- Result: Baseline set to `3,790 Wh/day` and documented in `docs/SYSTEMS.md`.
- Follow-up: Superseded by D-004 BOM-derived model reset.

- ID: D-002
- Date: 2026-02-11
- Decision: Keep Phase 1 house system centered on 48V architecture.
- Context: Workbook BOM and notes consistently reference 48V battery, inverter, and charging path.
- Options considered: Full 12V architecture, mixed architecture, 48V core with DC step-down.
- Decision drivers: Efficiency, inverter support, and existing BOM momentum.
- Result: 48V remains default architecture pending final component lock.
- Follow-up: Validate alternator charging thermal behavior in bench test at selected BBR current limits.

- ID: D-003
- Date: 2026-02-11
- Decision: Maintain a single electrical capacity and charging reference in `docs/SYSTEMS.md`.
- Context: Build decisions depend on fast re-calculation of load, autonomy, and charge-source coverage as components change.
- Options considered: Keep analysis ad hoc in chat notes, create separate analysis docs, or keep one maintained canonical section.
- Decision drivers: Traceability, low overhead updates, and consistency with canonical-doc workflow.
- Result: Added maintained electrical model section with formulas, scenario table, and update workflow in `docs/SYSTEMS.md`.
- Follow-up: Recompute after any BOM power-component change or measured duty-cycle update.

- ID: D-004
- Date: 2026-02-11
- Decision: Retire workbook-derived `WH` load assumptions and rebuild the electrical model from BOM componentry only.
- Context: Previous model inputs were stale and no longer represented the current build configuration.
- Options considered: Patch old model values or perform a full model reset from BOM rows.
- Decision drivers: Data integrity, repeatability, and alignment with BOM-as-source-of-truth workflow.
- Result: `bom/load_model_wh.csv` replaced with BOM-derived model v2 scenarios and `docs/SYSTEMS.md` recalculated from those values.
- Follow-up: Superseded by D-007 owner-supplied office-load modeling policy.

- ID: D-005
- Date: 2026-02-11
- Decision: Correct battery interpretation to `2x 48V 100Ah` and treat `400Ah` as max 4-battery system capability (not installed capacity).
- Context: A temporary documentation update incorrectly modeled installed capacity as `2x 400Ah`.
- Options considered: Keep oversized model or correct to installed battery count and capacity.
- Decision drivers: Accuracy of autonomy and charging predictions.
- Result: BOM battery row and all capacity/autonomy calculations were corrected in `docs/SYSTEMS.md`.
- Follow-up: `2026-02-12` convention locked: keep `48V` as system label and use `51.2V` nominal for battery Wh accounting.

- ID: D-006
- Date: 2026-02-11
- Decision: Adjust winter fridge duty-cycle assumption downward and model `900W` flexible solar with explicit derate factors.
- Context: Prior `winter_workday` model set fridge duty higher than core profile without supporting evidence, and solar estimates used one generic efficiency factor.
- Options considered: Keep prior assumptions, tweak only fridge duty, or update both fridge and solar methodology.
- Decision drivers: Reduce avoidable model bias and align with expected flexible-panel real-world behavior.
- Result: `winter_workday` load updated to `3,003 Wh/day`, and `docs/SYSTEMS.md` now uses a flexible-array planning base of `68%` efficiency with `60%-75%` sensitivity.
- Follow-up: Validate fridge duty cycle and daily solar harvest against Cerbo/SmartShunt logs after shakedown.

- ID: D-007
- Date: 2026-02-11
- Decision: Keep owner-supplied work electronics out of BOM cost tracking while including them in canonical Wh load modeling.
- Context: Laptop, monitor, tablet, keyboard, and mouse are already owned and should not inflate procurement BOM totals, but excluding them materially understates real daily energy demand.
- Options considered: Add owner gear to BOM, keep excluding owner gear from the model, or model owner gear separately from BOM pricing.
- Decision drivers: Accurate autonomy/charging analysis without polluting procurement cost accounting.
- Result: Added owner-supplied office-load rows to `bom/load_model_wh.csv` model v3 and recalculated `docs/SYSTEMS.md` capacity/autonomy/charging tables.
- Follow-up: Replace planning assumptions with measured device-level energy data from real workdays.

- ID: D-008
- Date: 2026-02-11
- Decision: Freeze alternator charging architecture to Sterling `BB1248120` with `BBR` remote control.
- Context: Prior BOM/docs left alternator charging open between dual Orion and Sterling options, keeping recovery-time math ambiguous.
- Options considered: `2x Orion-Tr Smart 12/48`, Sterling `BB1248120` without remote control, Sterling `BB1248120` with `BBR` remote.
- Decision drivers: Significantly higher charge-rate ceiling, adjustable output limiting from the remote, and simplified single-unit charging architecture.
- Result: Updated BOM (`row 18` charger, `row 26` remote), recalculated alternator charging in `docs/SYSTEMS.md`, and replaced unresolved Orion references in canonical planning docs.
- Follow-up: Bench-test alternator and belt thermal behavior with staged BBR limits before locking continuous operating setpoint.

- ID: D-009
- Date: 2026-02-11
- Decision: Add Mechman 370A alternator and Big 3 wiring as explicit purchase-later BOM items while keeping stock-alternator-first operation.
- Context: Extended-idle use cases may benefit from higher idle-output headroom, but the Sterling remote can already reduce charger demand (`65%` target) to protect stock alternator operation.
- Options considered: Keep no-upgrade path only, add alternator only, add alternator plus Big 3 wiring scope.
- Decision drivers: Planning transparency, safer high-current upgrade path, and clearer future procurement sequencing.
- Result: Added purchase-later lines in BOM (`row 103` Mechman 370A alternator, `row 104` Big 3 estimate), added Big 3 wire notes to existing cable rows, and updated systems documentation with the staged strategy.
- Follow-up: Confirm exact fitment and belt length for the truck platform, then lock final Big 3 cable/fuse spec before purchase.

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
- Result: Added `docs/ELECTRICAL_fuse_schedule.md`, mapped fuse groups to BOM rows (`7`, `10`, `11`, `16`, `105`, `106`), and set baseline battery Class T quantity to `2x` for two battery-positive conductors.
- Follow-up: Lock exact fuse-holder SKUs and finalize any holder ecosystem constraints before purchase.

- ID: D-012
- Date: 2026-02-12
- Decision: Correct Sterling `BB1248120` electrical rating assumptions and promote the electrical topology artifact to implementation-level scope.
- Context: Existing planning text treated `BB1248120` as `120A` on the `48V` output, which overstated alternator charging recovery, and the topology diagram still excluded holder/wire-gauge implementation detail.
- Options considered: Keep existing assumptions, patch only charge-rate math, or patch charge-rate math and complete the fuse-holder + conductor topology together.
- Decision drivers: Safety planning accuracy, implementation readiness, and removal of unresolved holder/gauge ambiguity.
- Result: Updated `bom/bom_estimated_items.csv` row `18`, recalculated alternator charging section values in `docs/SYSTEMS.md`, and expanded `docs/ELECTRICAL_overview_diagram.md` + `docs/ELECTRICAL_fuse_schedule.md` to full implementation detail.
- Follow-up: Validate real-world Sterling output power/current with instrumented charge logs and finalize holder SKUs before purchase freeze.

- ID: D-013
- Date: 2026-02-13
- Decision: Lock Phase 1 camper AC/USB distribution baseline to two AC-out-1 branches plus DC-fed USB-C PD branches.
- Context: Previous AC scope was concept-level and procurement rows were incomplete, creating uncertainty around receptacle count, USB strategy, and shore interface hardware.
- Options considered: Single AC branch only, multi-branch panel with AC USB receptacles, or two AC branches with DC-fed USB-C PD outlets.
- Decision drivers: Practical usability (galley + office), safety/protection clarity, and reduced inverter idle/conversion losses for device charging.
- Result: Locked baseline to `4` total `120V` receptacle locations (`2` galley, `2` office), AC-out-1 branch split (`20A` galley + `15A` office), and `4` DC-fed USB-C PD points (`2` office + `2` galley) with `10A` per-zone fuse baseline. Added corresponding BOM scope in rows `107-118` and aligned AC hierarchy in `docs/ELECTRICAL_overview_diagram.md`.
- Follow-up: Lock final SKU selections for inlet, enclosure/breakers, receptacles, and USB-C PD modules, then validate Orion `48/12-30` headroom under simultaneous-use scenarios before purchase freeze.

- ID: D-014
- Date: 2026-02-15
- Decision: Adopt an overlapping build-sequence baseline with module-first prep before camper install date.
- Context: Install date is fixed (`2026-05-07`) and major build quality risks come from sequence errors (closing walls before rough-in validation, delayed module prep, and routing rework).
- Options considered: Strict serial trade flow, ad hoc sequencing, or staged sequence with explicit hold points and parallel workstreams.
- Decision drivers: Maintain install-date readiness, reduce rework risk, and keep system serviceability.
- Result: Added `docs/PROJECT_build_order_of_operations.md` and linked it from `docs/PROJECT.md` as the active sequencing baseline.
- Follow-up: Update date windows after first dry-fit rehearsal and add sequence-specific risks if schedule compression appears.

- ID: D-015
- Date: 2026-02-15
- Decision: Adopt a consolidated multi-system safety baseline in `docs/SYSTEMS.md` covering `48V`, `12V`, `120VAC`, and propane architecture controls.
- Context: Safety guidance existed across fuse/topology notes and placeholder sections, but there was no single integrated baseline for commissioning, emergency shutdown, and propane/CO risk controls.
- Options considered: Keep safety details distributed only in implementation docs, create a separate standalone safety doc, or expand the canonical systems safety section with cross-links.
- Decision drivers: High-consequence risk reduction, clearer pre-energization hold points, and faster install-time validation.
- Result: Expanded `docs/SYSTEMS.md` `## Safety` with architecture-specific hazards, required controls, commissioning checks, emergency shutdown order, and pre-close inspection gates.
- Follow-up: Lock propane appliance listing/venting path and convert safety hold points into dated test records in `logs/LOG.md` during commissioning.

- ID: D-016
- Date: 2026-02-15
- Decision: Add explicit scope for modular inside/outside mounting rails and hardwall-popup solar jumper passthrough wiring.
- Context: Build intent requires flexible exterior/interior gear mounting (shovel/Maxtrax and interior hooks/baskets), and hardwall popup construction makes concealed in-wall solar routing impractical.
- Options considered: Leave as informal notes only, add one generic placeholder line, or add explicit BOM + systems + sequencing entries.
- Decision drivers: Procurement visibility, serviceable routing, and reduced install-day rework.
- Result: Added BOM rows `119`, `120`, and `121`; updated `docs/SYSTEMS.md` (`## Solar`, `## Cabinetry and structure`) and `docs/PROJECT_build_order_of_operations.md` (Batches `B`, `C`, and `E`) to include the new scope.
- Follow-up: Lock final rail profile/attachment ecosystem and finalize solar jumper connector/passthrough SKU choices before purchase freeze.

## Risk register
- ID: R-001
- Risk: Roof load from rigid/flexible solar + Starlink + fan may exceed comfortable strut margin.
- Impact (1-5): 4
- Likelihood (1-5): 3
- Mitigation: Confirm load limits and strut options with Hiatus before panel strategy lock.
- Trigger: Final solar panel selection.
- Owner: Sunny
- Status: Open

- ID: R-002
- Risk: Passthrough routing (solar, shore, diesel/propane) unresolved before production lock.
- Impact (1-5): 4
- Likelihood (1-5): 3
- Mitigation: Consolidate routing questions and get written confirmation from builder.
- Trigger: Production freeze date.
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
- Mitigation: Enforce load-sequencing SOP, prioritize propane water heating path, and validate AC branch design in bench testing.
- Trigger: Final appliance mix and first full-load test.
- Owner: Sunny
- Status: Open

- ID: R-005
- Risk: Combined installed + owner-supplied office loads reduce no-charge autonomy to roughly `1.8-2.2` workdays in active work scenarios.
- Impact (1-5): 4
- Likelihood (1-5): 3
- Mitigation: Enforce SOC reserve policy, lock charging strategy (solar + alternator + shore cadence), and validate real duty cycles in shakedown tests.
- Trigger: Consecutive low-sun days or high winter-duty cycle operations.
- Owner: Sunny
- Status: Open

- ID: R-006
- Risk: Purchase-later high-output alternator integration could still require fitment confirmation, belt-length change, and RVC-aware Big 3 routing updates.
- Impact (1-5): 4
- Likelihood (1-5): 2
- Mitigation: Confirm truck-specific part fitment/SKU, lock belt part number during install plan, and validate Big 3 routing/fusing before energizing.
- Trigger: Alternator-upgrade procurement kickoff.
- Owner: Sunny
- Status: Open

- ID: R-007
- Risk: High-fault-current `48V` battery architecture can produce severe arc/thermal events during commissioning or service if isolation, torque, polarity, or fuse-voltage controls are missed.
- Impact (1-5): 5
- Likelihood (1-5): 2
- Mitigation: Enforce documented pre-energization checks (polarity, torque witness, correct fuse voltage class, bus insulation covers, disconnect/isolation verification) and require controlled service procedure.
- Trigger: First full-system energization and any major rewiring event.
- Owner: Sunny
- Status: Open

- ID: R-008
- Risk: Propane leak or combustion byproduct exposure (CO) could occur if rear-mount routing, passthrough sealing, detector placement, or appliance listing/venting assumptions are wrong.
- Impact (1-5): 5
- Likelihood (1-5): 3
- Mitigation: Keep outdoor-only propane appliances out of enclosed use, require leak/pressure checks after every gas-path change, lock detector layout, and confirm listed venting method before indoor hot-water decisions.
- Trigger: Propane passthrough fabrication and final water-heater selection.
- Owner: Sunny
- Status: Open

- ID: R-009
- Risk: AC shock/fire risk from neutral-ground misconfiguration or incomplete GFCI/RCD protection on branch circuits.
- Impact (1-5): 5
- Likelihood (1-5): 2
- Mitigation: Preserve AC protection chain (`shore breaker -> MultiPlus -> branch protection`), validate outlet polarity and GFCI/RCD operation at commissioning, and verify ground continuity/chassis bonding.
- Trigger: AC branch wiring completion and first shore/inverter live test.
- Owner: Sunny
- Status: Open

- ID: R-010
- Risk: Roof-to-shell coiled solar jumper routing can chafe, snag, or leak at passthrough points if cable travel and strain relief are not validated through popup cycles.
- Impact (1-5): 4
- Likelihood (1-5): 3
- Mitigation: Use UV/weather-rated cable, abrasion sleeves, drip loop + strain relief, and repeat open/close travel-cycle checks before final sealing.
- Trigger: First full roof open/close cycle test with finalized cable length and routing.
- Owner: Sunny
- Status: Open

## Open questions
- Exact autonomy target by season and reserve floor policy (20% SOC currently modeled)
- Lock initial BBR current-limit setpoint for the assumed `240A` factory alternator after first instrumented charge tests
- Confirm Mechman 370A (SKU `11532370`) fitment for the actual truck platform before purchase (VIN check)
- Confirm required shorter belt length and final belt part number if the Mechman alternator is installed
- Lock Big 3 spec package (additional cable length, inline fuse type/rating, lug count, and RVC ground-loop routing requirement)
- Confirm measured daily draw for owner-supplied laptop/monitor/tablet charging to replace planning assumptions
- Lock final SKU set for AC/USB hardware (`rows 13-15`, `107-118`) and verify physical fitment with cabinet layout
- Validate Orion `48/12-30` converter headroom with the new USB-C PD branch plan (`12V-08`, `12V-09`) and trigger row `118` only if sustained overload is observed
- Final passthrough locations for solar, shore power, and fuel/heater paths
- Lock roof-to-shell solar jumper connector strategy and exact service-loop length for full popup travel
- Rigid vs flexible solar strategy under roof weight constraints
- Lock interior/exterior mounting rail ecosystem (rail profile, nut/hardware standard, bracket interfaces) and final linear-foot allowances
- Secondary internet strategy and minimum acceptable fallback performance
- Battery compartment heating and control implementation details (sensor, relay, setpoints)
- Storage/security SOP for flight windows
- Measured fridge compressor duty cycle by ambient band (cold, mild, hot) to replace modeled assumptions
- Final fuse-holder SKU standard for Orion input/output, Sterling input, and PV string fusing hardware
- Validate the chosen `F-05 + F-06` split-protection Orion branch against final measured run lengths and voltage drop
- Confirm acceptable monitoring expectation that Orion is not a direct GX telemetry node in current architecture
- Confirm measured Sterling `BB1248120` output current/power at idle and driving RPM bands for charge-time planning
- Lock final propane water-heater path: outdoor-use-only portable workflow vs listed indoor/RV unit with compliant venting/clearance package
- Lock propane passthrough hardware standard and no-concealed-joints rule for final routing
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
- `docs/SYSTEMS.md`
- `docs/PROJECT_workbook_hiatus_consult.md`
- `docs/SYSTEMS_workbook_build_notes.md`
- `docs/SYSTEMS_workbook_electrical_notes.md`
- `docs/ELECTRICAL_overview_diagram.md`
- `docs/ELECTRICAL_fuse_schedule.md`
