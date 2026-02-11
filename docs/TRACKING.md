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
- Follow-up: Add exact battery SKU datasheet to `references/` and confirm nominal voltage convention (`48V` label vs `51.2V` LiFePO4 nominal).

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

## Open questions
- Exact autonomy target by season and reserve floor policy (20% SOC currently modeled)
- Lock initial BBR current-limit setpoint for the assumed `240A` factory alternator after first instrumented charge tests
- Confirm Mechman 370A (SKU `11532370`) fitment for the actual truck platform before purchase (VIN check)
- Confirm required shorter belt length and final belt part number if the Mechman alternator is installed
- Lock Big 3 spec package (additional cable length, inline fuse type/rating, lug count, and RVC ground-loop routing requirement)
- Confirm measured daily draw for owner-supplied laptop/monitor/tablet charging to replace planning assumptions
- Confirm battery datasheet nominal voltage convention (`48V` marketed vs `51.2V` nominal) for final energy accounting standard
- Final passthrough locations for solar, shore power, and fuel/heater paths
- Rigid vs flexible solar strategy under roof weight constraints
- Secondary internet strategy and minimum acceptable fallback performance
- Battery compartment heating and control implementation details (sensor, relay, setpoints)
- Storage/security SOP for flight windows
- Measured fridge compressor duty cycle by ambient band (cold, mild, hot) to replace modeled assumptions

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
- `docs/PROJECT_workbook_hiatus_consult.md`
- `docs/SYSTEMS_workbook_build_notes.md`
