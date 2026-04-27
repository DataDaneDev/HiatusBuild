---
aliases:
  - Hiatus systems baseline
tags:
  - hiatus/core
  - hiatus/systems
status: active
related:
  - "[[PROJECT]]"
  - "[[ELECTRICAL_48V_ARCHITECTURE]]"
  - "[[TRACKING]]"
---

# Systems Design

## Document role
- This file owns the active subsystem baseline and cross-system modeling context for the build.
- Use this file to describe what the current system is, how the major subsystems fit together, and which assumptions are still active.
- Keep the final `48V` house/alternator architecture, shutdown order, and control-path lock in `docs/core/ELECTRICAL_48V_ARCHITECTURE.md`.
- Keep exact conductor, fuse, layout, and install-level detail in `docs/implementation/`.
- Keep decision/risk/open-question state in `docs/core/TRACKING.md` rather than letting this file become the live issue tracker.

## Electrical and energy
### Goals
- Deliver workday reliability with reserve margin
- Keep wiring safe, labeled, and serviceable

### Electrical doc links
- Canonical `48V` architecture and alternator-control baseline: [ELECTRICAL_48V_ARCHITECTURE](ELECTRICAL_48V_ARCHITECTURE.md)
- Implementation topology (components, fuses, holders, gauges): [ELECTRICAL_overview_diagram](../implementation/ELECTRICAL_overview_diagram.md)
- Fuse IDs, locations, housing methods, spares, and BOM mapping: [ELECTRICAL_fuse_schedule](../implementation/ELECTRICAL_fuse_schedule.md)
- Voltage architecture trade study (`12V` vs `48V`): [ELECTRICAL_12V_vs_48V_trade_study](../studies/ELECTRICAL_12V_vs_48V_trade_study.md)
- Alternator architecture trade study history (research archive only; final decisions moved to the canonical `48V` architecture doc): [ELECTRICAL_48V_dual_alternator_trade_study](../studies/ELECTRICAL_48V_dual_alternator_trade_study.md)
- Solar option screening matrix (stringing + MPPT fit flags): [SOLAR_configuration_matrix](../studies/SOLAR_configuration_matrix.md)
- Electrical decisions, risks, and unresolved items: [TRACKING](TRACKING.md)

### Planning snapshot (as-of `2026-04-27`)
- Battery bank: `3x 48V 100Ah LiFePO4` from BOM row 3 (`15.36 kWh` nominal at `51.2V` battery nominal).
- House architecture: `48V` core with Orion-Tr Smart `48V->12V` charging/step-down feeding a shared battery-backed `12V` junction.
- Inverter/charger candidate: Victron MultiPlus-II `48/3000/35-50`.
- Charge sources in current BOM: solar MPPT, dedicated `48V` secondary alternator path (`Mechman + WS500 + APM-48` migration baseline), shore AC charger path.
- Monitoring and protection: Cerbo GX, SmartShunt, battery temp sensing, Class T primary fuse + branch fusing.
- AC protection chain remains locked (`shore source -> cord/adapter -> TT-30 inlet -> EMS -> AC-in breaker -> MultiPlus -> separate AC-out branch panel`), with AC-in-only initial charging prioritized ahead of final receptacle-count/utilization closure.

### Modeling rules (procurement-first plus full-load)
- Primary procurement source of truth is `bom/bom_estimated_items.csv`.
- Load model is maintained in `bom/load_model_wh.csv` (model v3) and includes BOM-sourced installed loads plus owner-supplied work electronics (kept out of BOM cost totals).
- Legacy workbook WH model assumptions are retired and not used.
- Voltage convention: use `48V` as architecture label, but use `51.2V` nominal for battery Wh accounting.
- Run-length convention: measured physical layout lengths are cut-length source-of-truth; CAD values are planning references only.

### Input reference (maintained)
| Input | Current value | Source |
| --- | --- | --- |
| Battery bank | `3x Dumfume 51.2V 100Ah` (`1S3P`; manual allows up to `1S4P`) | `bom/bom_estimated_items.csv` row 3 + `references/Dunfume_36V_48V_100Ah_Battery_-_User_Manual.pdf` |
| Inverter/charger | MultiPlus-II `48/3000/35-50` | `bom/bom_estimated_items.csv` row 12 |
| Alternator charging | Dedicated `48V` secondary alternator path (`Mechman + WS500 + APM-48`) with `Upfitter #3 -> WS500 brown ignition` manual control and Lynx Slot 3 alternator branch fuse lock | `bom/bom_estimated_items.csv` rows `168-171`, `176` + `docs/core/ELECTRICAL_48V_ARCHITECTURE.md` |
| Sterling legacy items | `BB1248120` + `BBR` retained physically only until Mechman confirmation, then returned | `bom/bom_estimated_items.csv` rows `18` and `26` |
| Legacy single-12V upgrade path | Mechman `370A` + Big 3 path is deprecated under the dual-`48V` migration baseline | `bom/bom_estimated_items.csv` rows `103` and `104` |
| DC-DC charger | Orion-Tr Smart `48/12 30A` (`360W`) | `bom/bom_estimated_items.csv` row 20 |
| 12V buffer battery | `12V 100Ah LiFePO4` on shared 12V junction (`F-11` + `SW-12V-BATT`) | `bom/bom_estimated_items.csv` rows 21, 124, and 125 |
| Solar array candidate | Flexible-first placeholder (`~800-1000W` class; prior `9x100W`/`3S3P` concept retained for modeling basis) | `bom/bom_estimated_items.csv` row 24 |
| Solar controller | SmartSolar `MPPT 150/45` | `bom/bom_estimated_items.csv` row 25 |
| Load profiles (BOM + owner-supplied office loads) | `core_workday`, `winter_workday`, `minimal_idle_day` | `bom/load_model_wh.csv` |
| Owner-supplied office assumptions | Laptop + 27 inch 1440p monitor + tablet/peripheral charging | `bom/load_model_wh.csv` rows marked `Owner-Supplied` |

### Modeled expected usage
Load totals below are from `bom/load_model_wh.csv` model v3 (BOM loads plus owner-supplied office loads).

| Scenario | Daily energy | 5-day workweek energy | 7-day week energy | Dominant contributors |
| --- | --- | --- | --- | --- |
| `core_workday` | `3,530 Wh` | `17,650 Wh` | `24,710 Wh` | Laptop, monitor, Starlink, cooking, inverter idle |
| `winter_workday` | `4,202 Wh` | `21,010 Wh` | `29,414 Wh` | Laptop, monitor, Starlink, diesel heater, cooking |
| `minimal_idle_day` | `624 Wh` | `3,120 Wh` | `4,368 Wh` | Fridge + always-on monitoring/detector loads |

### Capacity analysis (corrected battery bank)
| Metric | Formula | Result |
| --- | --- | --- |
| Nominal battery energy | `51.2V x 100Ah x 3` | `15,360 Wh` |
| Usable energy to 20% reserve floor | `15,360 x 0.8` | `12,288 Wh` |
| Core day depth of discharge | `3,530 / 15,360` | `22.98%` per day |
| Winter day depth of discharge | `4,202 / 15,360` | `27.36%` per day |

### Autonomy (no charging)
| Scenario | Days (`100% -> 20%`) |
| --- | --- |
| `core_workday` | `3.48` |
| `winter_workday` | `2.92` |
| `minimal_idle_day` | `19.69` |

### Charging potential
All values are planning-level and should be replaced with measured charge logs after shakedown tests.

#### Solar charging (`900W` flexible `3S3P` focus)
Base planning factor for your target roof setup is now `68%` end-to-end harvest efficiency, with sensitivity from `60%` (poor conditions) to `75%` (strong conditions).

| Derate component | Planning factor | Note |
| --- | --- | --- |
| Nameplate realization | `0.95` | Manufacturing variance and real-world rating spread |
| Thermal factor (flexible with air gap) | `0.90` | Better than bonded-flat flexible, still hotter than rigid stand-off |
| MPPT + wiring efficiency | `0.96` | Controller and cable losses |
| Flat-roof angle/azimuth factor | `0.88` | No seasonal tilt optimization |
| Soiling + mismatch + partial shading allowance | `0.93` | Dirt, string mismatch, and intermittent shade impacts |
| Combined planning factor | `~0.68` | Product of factors above |

| `900W` array efficiency | 2 PSH day | 4 PSH day | 5 PSH day | Net vs `core_workday` at 4 PSH | Net vs `winter_workday` at 4 PSH |
| --- | --- | --- | --- | --- | --- |
| `60%` | `1,080 Wh` | `2,160 Wh` | `2,700 Wh` | `-1,370 Wh/day` | `-2,042 Wh/day` |
| `68%` (planning base) | `1,224 Wh` | `2,448 Wh` | `3,060 Wh` | `-1,082 Wh/day` | `-1,754 Wh/day` |
| `75%` | `1,350 Wh` | `2,700 Wh` | `3,375 Wh` | `-830 Wh/day` | `-1,502 Wh/day` |

- Break-even PSH at `900W`:
- `core_workday` (base `68%`): `3,530 / (900 x 0.68) = 5.77` PSH/day.
- `winter_workday` (base `68%`): `4,202 / (900 x 0.68) = 6.87` PSH/day.
- Sensitivity band for `winter_workday`: `6.23` PSH/day (`75%`) to `7.78` PSH/day (`60%`).
- `MPPT 150/45` is not the bottleneck for the current array range.

#### Alternator charging (dedicated `48V` secondary alternator path)
- Active migration baseline: Mechman dual-alternator kit + WS500 regulator + APM-48 protection module.
- `Lynx Slot 3` alternator branch fuse (`F-04`) is now locked at `150A` (`58V/80V MEGA` class).
- WS500 low-current fuse set is now explicitly part of the design baseline (`10A` power lead baseline, `3A` sense, `5A` current-sense where required).
- Manual charge-enable/disable path is now locked to Ford `Upfitter Switch #3` feeding the WS500 brown ignition/enable wire through local inline fuse `F-15`.
- `WS500` white `Feature-In` is reserved for future automatic fault-interlock work and is not required in Phase 1.
- Cable decision lock for this pass: reuse existing uncut `2/0` inventory for the alternator charge path (`~20 ft` one-way assumed), with dedicated equal-size negative run.
- Sterling `BB1248120`/`BBR` remain physically on hand only as return-pending hardware until Mechman fitment/content confirmation closes.
- Open execution gate: contact Mechman first, then complete Sterling physical return workflow.

#### Shore charging (MultiPlus-II charger path)
- Charger limit from model string: `35A`.
- Existing planning math uses `56.8V` absorption target (`~1,988W`), while the battery manual/BOM basis references `58.4V` (`~2,044W` at `35A`). Reconcile and document the actual MultiPlus LiFePO4 charge profile before first energization.
- Initial garage workflow: use AC-in-only MultiPlus charging and connect/charge one `48V` battery at a time before paralleling the `1S3P` bank.
- Ideal bulk-only recharge times at `56.8V` planning basis:
- Replace one `core_workday`: `1.78h`.
- Replace one `winter_workday`: `2.11h`.
- Recharge full `3x` bank from `20%` to `100%`: `6.18h`.
- Recharge one `48V 100Ah` battery from `20%` to `100%`: about `2.06h` ideal bulk-only.
- Real-world times are longer due to absorption taper near full charge, lower input-current limits on `15A` household sources, and any configured charge-current derate.

### Operational implications and constraints
- Battery capacity now supports roughly `2.9-3.5` office-workdays without charging depending on season and reserve policy.
- With `900W` flexible solar at the base `68%` factor, `4` PSH leaves a material daily deficit for both `core_workday` and `winter_workday`.
- Shore charging can materially recover SOC in a single evening (`~6.18h` from `20%` to `100%` in bulk-ideal terms).
- Alternator recovery potential is expected to materially exceed the old Sterling `~1.5kW` ceiling once the dedicated `48V` alternator path is commissioned.
- Current execution risk is no longer charger-capacity-limited operation; it is migration/commissioning quality (fitment, regulation, protection, and measured thermal behavior).
- MultiPlus-II `48/3000` inverter continuous output (`~2,400W`) can be exceeded by simultaneous induction + microwave + other AC loads, so high-draw AC loads need sequencing.
- Orion-Tr Smart `48->12V 30A` charger (`360W`) is the continuous charging/feed ceiling into the shared 12V junction; buffer battery supports short transients but sustained overload still requires load budgeting.

### Safety baseline
- Positive path sequence: battery -> Class T fuse (near source) -> disconnect -> Lynx Distributor -> fused branch feeds
- Negative path sequence: battery -> SmartShunt -> Lynx Distributor negative bus -> all load returns on load side of shunt
- Dedicated alternator branch grounding rule set: run equal-or-larger dedicated negative cable from secondary alternator to house-bank return path and avoid sheet-metal return paths.
- If the truck uses an RVC ground-sensor loop, route the upgraded ground path through the loop per vehicle requirements.
- Battery thermal strategy: insulated battery box, ducted warm-air branch, thermostat/relay enable logic
- Wiring practices: grommets, loom, glands, abrasion protection, and bend-radius validation
- Reference links from workbook notes:
- `https://youtu.be/dSYKabw_rgs?t=651`
- `https://www.diodeled.com/45-channel.html`

### Electrical overview diagram (implementation)
- Full implementation-level topology diagram: `docs/implementation/ELECTRICAL_overview_diagram.md`
- Scope includes fuse IDs, fuse-holder/housing methods, branch wire-gauge selections, and documented sizing assumptions.

### RF-003 Distribution Topology Decision (Lynx Locked)
Decision date: `2026-02-12`

Approved architecture for Phase 1:
- `Victron Lynx Distributor M10` (`LYN060102010`) is the single distribution backbone.
- Current tracked unit price is `$192.47`.
- Current modeled `48V` fused branches (`4` total):
- MultiPlus-II `48/3000`
- SmartSolar `150/45`
- Dedicated `48V` alternator branch output (`F-04` locked `150A`)
- Orion-Tr Smart `48/12` (shared 12V junction feeder)
- `1x` Lynx Distributor covers current branch count with `0` spare fused outputs.
- If future branch expansion is needed, add a second Lynx module in that phase.

Implementation notes:
- `Lynx Distributor` includes the negative busbar, so a separate standalone negative bus is not required in the Lynx path.
- `Lynx Distributor` branch-fuse LEDs need a `Lynx Shunt VE.Can` or `Lynx Smart BMS`; with `SmartShunt`-only monitoring, LED fuse indication is not active.
- Main Class T protection baseline is `3x` (one per battery-positive conductor) and is tracked in the fuse schedule/BOM.

Reference links:
- Lynx Distributor manual/specs: `https://www.victronenergy.com/media/pg/Lynx_Distributor/en/introduction.html`
- Lynx Distributor retail example: `https://www.invertersrus.com/product/victron-lynx-distributor/`

### Fuse Determination Baseline (Lynx)
Objective: maintain a complete start-to-finish fuse schedule for the approved Lynx architecture.

Current detailed schedule (active reference):
- `docs/implementation/ELECTRICAL_fuse_schedule.md`

Scope covered:
1. Main battery protection (`Class T`) quantity, rating, and placement.
2. Lynx branch fuses for each `48V` branch (MultiPlus, MPPT, dedicated alternator branch, Orion input).
3. WS500 low-current fuse requirements and alternator-branch protection coordination.
4. Any additional protective devices required by manufacturer manuals for both charge-source and load paths.

Method:
1. Pull max current requirements and overcurrent guidance from each device manual.
2. Confirm planned wire gauge/length/insulation assumptions for each run.
3. Size each fuse to protect the conductor first while meeting equipment requirements.
4. Build final fuse matrix with part numbers, quantities, and BOM row mapping.

## Solar
- Current direction: flexible-first design path due roof `75 lb` hard panel-weight cap.
- Near-term project policy: keep solar final procurement/string lock deferred deeper into build while preserving routing/passthrough reservations now.
- Hardwall popup wiring baseline for planning: no hidden in-wall solar run; use exterior-rated coiled jumper cable(s) from roof solar exit to a lower-shell weatherproof passthrough.
- BOM scope for that routing method is tracked in `bom/bom_estimated_items.csv` row `121`.
- Open points: exact passthrough location, connector standard (`MC4` direct vs bulkhead adapter strategy), and final flexible module/string configuration before SKU lock.
- Energy takeaway from current modeled load: moving from sub-`600W` class toward `~800-1000W` flexible can materially reduce daily deficit, but modeled office-workday profiles still require charging strategy integration (solar + alternator + shore).

### Electrical reference maintenance workflow
- Update trigger conditions:
- Any change to battery, inverter/charger, DC-DC, or solar components in `bom/bom_estimated_items.csv`.
- Any measured field data that materially changes duty-cycle assumptions.
- Any change in appliance selection, owner-supplied office electronics, or expected duty cycle in `bom/load_model_wh.csv`.
- Update process:
1. Update component rows and assumptions in `bom/load_model_wh.csv`.
2. Recalculate scenario daily Wh totals in this file from that CSV.
3. Recalculate autonomy at the active reserve floor (`usable Wh / daily Wh`).
4. Recalculate charging tables with latest charge source ratings and assumptions.
5. Record what changed in `docs/core/TRACKING.md` (decision/risk/open questions) and `logs/LOG.md`.
6. Remove stale assumptions that are not backed by BOM rows or explicit owner-supplied load assumptions.
- Formula quick reference:
```text
battery_nominal_wh = battery_voltage_v * battery_capacity_ah * battery_quantity
daily_wh = sum(component_wh_per_day) + conversion_loss_wh
autonomy_days = usable_battery_wh / daily_wh
solar_daily_wh = array_watts * effective_psh * solar_efficiency_factor
solar_efficiency_factor = nameplate_realization * thermal_factor * mppt_wiring_factor * orientation_factor * soiling_shading_factor
alternator_daily_wh = dc_dc_output_watts * drive_hours
alternator_practical_w = (alternator_rated_a - vehicle_base_load_a) * alternator_voltage_v * conversion_efficiency
house_charge_current_a = alternator_practical_w / charge_voltage_v
shore_charge_power_w = charge_voltage * charger_current_a
bulk_charge_hours = energy_to_replace_wh / shore_charge_power_w
```
- Retired model note:
- `bom/load_model_wh.csv` v1 (workbook-derived chart) and v2 (BOM-only) are superseded by model v3 (BOM plus owner-supplied office loads).

## Communications
- Primary internet path: Starlink Standard (DC power conversion item tracked in BOM)
- Secondary/fallback path: TBD (cellular path and carrier diversity not frozen)
- Placement constraint: routing and passthrough location unresolved

## Plumbing (if included in phase 1)
- Near-term baseline: decouple cold-water galley build from final hot-water selection. Build around tank, pump, faucet/sink, drain/graywater path, service shutoffs, and a capped future hot-water tie-in.
- Water capacity candidates captured: `10 gal` compact concept and `~25 gal` tank option. A full `25 gal` tank weighs about `208 lb` before tank/hardware and needs real restraint/anchor planning.
- Pump candidate captured: Shurflo 3.0 GPM class.
- Faucet is now an explicit missing purchase class and should be tracked separately from generic cabinetry.
- Hot-water decision posture: electric tankless is out of scale for the current `48/3000` inverter; small tanked electric is plausible later but adds AC load-management complexity; portable propane tankless remains provisional outdoor-use only; listed indoor/RV propane is deferred until venting/combustion-air/clearance package is locked.
- Freeze and winterization strategy: TBD.

## Cabinetry and structure
- Aluminum extrusion strategy: 15-series biased for heavy/dynamic modules (fridge, tank, electrical cabinet) and 10-series for light desk/accessory/panel work; use stock-length starter ordering until real envelopes are measured.
- Current furniture CAD is reference-only after Iceco/water tank dry fit; fridge/cooler likely moves to the front-left corner, so re-CAD block envelopes before final cut lists.
- Modular mounting baseline now includes T-slot/strut rails both exterior (recovery/tool mounts like shovel/Maxtrax) and interior (baskets/hooks/tie-down points); BOM rows `119` and `120`.
- Drawer hardware baseline includes `4x` soft-close undermount slide kits for primary cabinetry drawers; BOM row `122`, but final lengths are deferred until fridge/tank/electrical module envelopes are verified.
- Desk concepts captured: Lagun-style fold-in options and pneumatic pedestal concepts
- Material ideas captured: phenolic/richlite top, sound treatment, panel anti-rattle tape
- Monitor travel strategy concept: stow-low assisted deployment with structural bracing

## HVAC and condensation
- Heating approach in notes: diesel heater with possible branch to battery compartment
- Ventilation: Maxxair fan included in current camper config
- Lighting split: Hiatus factory overhead LED+dimmer is a separate circuit from planned ambient/cabinet LED strips (Govee)
- Condensation controls and climate envelope limits: TBD

## Safety
- Purpose: define a practical, build-ready safety baseline for the current architecture (`48V 15.36kWh` house bank, `12V` distribution, `120VAC` shore/inverter path, and propane-supported heating/hot-water concepts).
- Priority order: prevent ignition and overcurrent faults, preserve safe shutdown paths, detect hazards early, and make isolation/service repeatable.
- Final install gate: before energizing or using propane in service, verify all items against manufacturer manuals and complete licensed inspection where required.

### System-wide controls
- Keep one-line diagrams, fuse IDs, and conductor IDs synchronized across:
- `docs/implementation/ELECTRICAL_overview_diagram.md`
- `docs/implementation/ELECTRICAL_fuse_schedule.md`
- `docs/core/TRACKING.md`
- Ensure all protection and isolation devices are physically accessible without disassembling fixed furniture.
- Keep gas components and AC/DC electrical components separated by design; no mixed service cavities without physical barriers and clear labeling.
- Label every branch and shutoff point so an operator can isolate faults quickly under stress.

### 48V battery system safety (primary)
- Main hazards: high fault current, sustained DC arc potential, short-circuit heating, incorrect polarity during service, and thermal stress events.
- Required architecture controls:
- Battery positive path stays: battery -> Class T fuse near source -> main disconnect -> Lynx fused branches.
- Battery negative path stays: battery -> SmartShunt -> Lynx negative bus (all returns on load side of shunt).
- Use only voltage-appropriate overcurrent devices on house DC branches (`58V`/`80V` class on `48V` paths); do not substitute `32V` automotive-only fuses on `48V` circuits.
- Keep all busbars/studs covered and insulated; use boot covers, strain relief, and abrasion protection on all near-bus runs.
- Manual alternator shutdown order stays: `Upfitter #3 OFF` first to disable the `WS500`, then open the main `48V` disconnect only after alternator charging is no longer active.
- Commissioning controls (first energization and after major rework):
1. Verify polarity and expected voltage at each segment before inserting branch fuses.
2. Confirm torque marks on all high-current terminals and re-check after initial thermal cycles.
3. Confirm the disconnect fully de-energizes downstream service zones as intended.
4. Validate no unintended parallel return paths bypassing shunt measurement.
- Service controls:
- Remove conductive jewelry, use insulated tools, and keep one-hand work practice on live-exposure checks.
- Never perform branch rewiring with battery disconnect closed unless the specific test requires energized state and a spotter is present.

### 12V distribution safety
- Main hazards: feeder overload from Orion output limits, hidden voltage drop causing heat at terminations, and unfused accessory additions.
- Required controls:
- Keep Orion output feeder fused at source (`F-07`) and avoid adding unfused taps between Orion and the shared 12V junction.
- Keep 12V buffer battery positive protected at source (`F-11`) and route service isolation through `SW-12V-BATT` downstream of `F-11`.
- Keep `SW-12V-BATT` in its normal closed position during operation; use open position only for service isolation/diagnostics.
- In normal closed operation, Orion supports both active 12V loads and buffer-battery maintenance through the shared junction path.
- In this baseline, the 12V fuse block is the shared junction device (`main +` stud combine point plus integrated negative bus return point).
- Do not solder-splice high-current 12V source conductors; use crimped lugs on rated stud terminals.
- Maintain branch-level fuse-to-conductor coordination per `docs/implementation/ELECTRICAL_fuse_schedule.md`.
- Keep always-on detector branch (`12V-05`) protected but never switch-controlled.
- Keep ambient/cabinet strip lighting on the dedicated DC branch (`12V-11`) so low-light use does not require inverter operation.
- If sustained `12V` demand exceeds Orion headroom, treat additional `48V->12V` charger capacity (`BOM row 118`) as a safety action, not a convenience upgrade.

### 120VAC shore/inverter safety
- Main hazards: shock from miswired neutral/ground, ground-fault exposure at outlets, and overcurrent heating from undersized branch protection.
- Required controls:
- Keep shore path order: shore source -> shore cord/adapter -> shore inlet (`TT-30`) -> hardwired EMS/surge protection -> AC-in DIN enclosure (`30A` UL489 breaker/disconnect) -> MultiPlus AC-in.
- Keep AC-out path order: MultiPlus AC-out-1 -> AC-out DIN enclosure (`20A` galley + `15A` office branch breakers) -> first-outlet GFCI strategy with downstream protected receptacles.
- Keep AC-in hardware on a `30A` / `10 AWG` basis, and set MultiPlus input current limit to the actual source (`15A`, `20A`, or `30A`) whenever adapters are used.
- Keep AC-out-2 as reserve-only in Phase 1 (labeled capped route; no energized branch hardware yet).
- Preserve continuous equipment grounding and chassis bond through all AC paths.
- Do not add a fixed downstream neutral-ground bond in branch wiring; neutral/ground behavior must follow MultiPlus transfer/bonding design.
- Commissioning checks:
1. AC-in-only charger validation with AC-out loads disconnected for first battery charge.
2. Receptacle polarity test on each outlet location.
3. GFCI/RCD trip test at each protected branch.
4. Verify AC-out-2 remains de-energized as a reserve-only capped route in Phase 1.

### Propane safety (rear-mounted tank plus passthrough and hot-water path)
- Main hazards: leak accumulation, ignition near electrical equipment, CO exposure, and using outdoor-only appliances in enclosed space.
- Rear-mount tank controls:
- Keep cylinder upright and externally mounted with impact-resistant bracketry and valve protection.
- Keep tank shutoff valve accessible from outside without tools.
- Protect hose/regulator routing from road debris, abrasion, and exhaust heat zones.
- Propane passthrough controls:
- Use sealed bulkhead/pass-through hardware with chafe protection at all penetrations.
- Avoid concealed unions/joints in inaccessible cavities; keep serviceable connections at inspection points.
- Perform leak tests after any connection change and before each trip phase where propane is used.
- Appliance selection rule (critical):
- Treat portable outdoor tankless heaters as outdoor-use-only unless a specific model is explicitly listed for indoor/RV enclosed installation with compliant venting.
- If an indoor propane water-heating path is pursued, lock to an RV/marine-listed indoor unit with approved venting/combustion-air method and documented install clearances before purchase.
- Detection and ventilation controls:
- Keep an LP detector low in cabin, CO detector in breathing zone, and smoke detector high in cabin.
- Test detector alarm functions on a recurring schedule and replace by manufacturer expiration date.

### Emergency shutdown baseline
1. Remove active high-draw loads (AC and gas appliances) if safe to do so.
2. Open the `48V` main disconnect and remove shore input.
3. Close propane cylinder valve at the tank.
4. Ventilate cabin area and confirm detectors are active.
5. Use fire extinguisher only if contained/incipient and exit path is clear; otherwise evacuate and call emergency services.
6. Do not re-energize or reopen gas supply until fault root cause is identified and corrected.

### Safety hold points before walls/panels are closed
- Complete and document high-current DC inspection (polarity, fuse value, terminal torque, insulation/boots).
- Complete AC verification (polarity, GFCI/RCD trip tests, branch labeling, ground continuity).
- Complete propane leak check and pressure-hold verification with all planned valves/fittings in final positions.
- Complete detector placement and functional alarm tests.
- Record evidence in `logs/LOG.md` and track unresolved items in `docs/core/TRACKING.md`.

## Source artifacts
- `docs/legacy/SYSTEMS_workbook_build_notes_obsolete.md`
- `bom/load_model_wh.csv`
