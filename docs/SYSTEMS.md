# Systems Design

## Electrical and energy
### Goals
- Deliver workday reliability with reserve margin
- Keep wiring safe, labeled, and serviceable

### Electrical doc links
- Implementation topology (components, fuses, holders, gauges): `docs/ELECTRICAL_overview_diagram.md`
- Fuse IDs, locations, housing methods, spares, and BOM mapping: `docs/ELECTRICAL_fuse_schedule.md`
- Voltage architecture trade study (`12V` vs `48V`): `docs/ELECTRICAL_12V_vs_48V_trade_study.md`
- Electrical decisions, risks, and unresolved items: `docs/TRACKING.md`

### Planning snapshot (as-of `2026-02-18`)
- Battery bank: `3x 48V 100Ah LiFePO4` from BOM row 3 (`15.36 kWh` nominal at `51.2V` battery nominal).
- House architecture: `48V` core with Orion-Tr Smart `48V->12V` charging/step-down feeding a shared battery-backed `12V` junction.
- Inverter/charger candidate: Victron MultiPlus-II `48/3000/35-50`.
- Charge sources in current BOM: solar MPPT, Sterling alternator B2B path (factory alternator now, high-output alternator as purchase-later option), shore AC charger path.
- Monitoring and protection: Cerbo GX, SmartShunt, battery temp sensing, Class T primary fuse + branch fusing.

### Modeling rules (procurement-first plus full-load)
- Primary procurement source of truth is `bom/bom_estimated_items.csv`.
- Load model is maintained in `bom/load_model_wh.csv` (model v3) and includes BOM-sourced installed loads plus owner-supplied work electronics (kept out of BOM cost totals).
- Legacy workbook WH model assumptions are retired and not used.
- Voltage convention: use `48V` as architecture label, but use `51.2V` nominal for battery Wh accounting.

### Input reference (maintained)
| Input | Current value | Source |
| --- | --- | --- |
| Battery bank | `3x 48V 100Ah` | `bom/bom_estimated_items.csv` row 3 |
| Inverter/charger | MultiPlus-II `48/3000/35-50` | `bom/bom_estimated_items.csv` row 12 |
| Alternator charging | Sterling `BB1248120` (`12V/24V -> 48V`, `~1500W` max, `~26A` at `57.6V`) + `BBR` remote | `bom/bom_estimated_items.csv` rows 18 and 26 |
| Vehicle alternator assumption (current) | Factory `240A` (user-reported) with `65%` BBR limit option for extended idle sessions | `docs/TRACKING.md` |
| Purchase-later alternator path | Mechman 370A alternator + Big 3 wiring estimate | `bom/bom_estimated_items.csv` rows 103 and 104 |
| DC-DC charger | Orion-Tr Smart `48/12 30A` (`360W`) | `bom/bom_estimated_items.csv` row 20 |
| 12V buffer battery | `12V 100Ah LiFePO4` on shared 12V junction (`F-11` + `SW-12V-BATT`) | `bom/bom_estimated_items.csv` row 21 |
| Solar array candidate | `900W` flexible (`9x100W`, 3S3P) | `bom/bom_estimated_items.csv` row 24 |
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

#### Alternator charging (Sterling `BB1248120` + `BBR`)
- Charger output ceiling for `BB1248120`: about `1,500W` max (`~26A` at `57.6V`, `~26.4A` at `56.8V`).
- Remote-limited output case requested: `65%` cap (`~975W`, `~17.2A` at `56.8V`).
- Practical `240A` factory-alternator planning cap (assume `70A` non-house vehicle load, `14.2V` alternator voltage, `90%` conversion efficiency): `~2,173W` available on vehicle side, but `BB1248120` output cap (`~1,500W`) is the limiting factor.
- Extended-idle stock-alternator strategy: use the BBR remote current limit (`~65%` baseline) unless temperature/voltage logs support a higher continuous setting.
- Purchase-later vehicle-side path: Mechman 370A alternator (`$599`) plus Big 3 wiring upgrade estimate (`$225`) are tracked in BOM for added idle-current headroom.
- Installation notes captured from provided reference: direct-fit/OEM plug claim, possible `1/2` to `1` inch shorter belt with smaller pulley, and required Big 3 wiring addition.
- Drive time to replace one modeled day:
- `core_workday`: `3.62h` at remote `65%` output setting, `2.35h` at charger max output.
- `winter_workday`: `4.31h` at remote `65%` output setting, `2.80h` at charger max output.
- Implementation note: remote `%` output setting is not the same as alternator-safe current; final setting should be locked from belt/alternator temperature plus voltage-drop logs.

#### Shore charging (MultiPlus-II charger path)
- Charger limit from model string: `35A`.
- At `56.8V` absorption target, charger power is about `1,988W`.
- Ideal bulk-only recharge times:
- Replace one `core_workday`: `1.78h`.
- Replace one `winter_workday`: `2.11h`.
- Recharge from `20%` to `100%`: `6.18h`.
- Real-world times are longer due to absorption taper near full charge.

### Operational implications and constraints
- Battery capacity now supports roughly `2.9-3.5` office-workdays without charging depending on season and reserve policy.
- With `900W` flexible solar at the base `68%` factor, `4` PSH leaves a material daily deficit for both `core_workday` and `winter_workday`.
- Shore charging can materially recover SOC in a single evening (`~6.18h` from `20%` to `100%` in bulk-ideal terms).
- Alternator recovery potential is meaningful, but the current Sterling charger path is capped near `1.5kW`, so recovery is slower than earlier `120A@48V` planning assumptions.
- If the Mechman alternator path is purchased later, complete Big 3 wiring and re-baseline safe continuous BBR limits before extended idling use.
- MultiPlus-II `48/3000` inverter continuous output (`~2,400W`) can be exceeded by simultaneous induction + microwave + other AC loads, so high-draw AC loads need sequencing.
- Orion-Tr Smart `48->12V 30A` charger (`360W`) is the continuous charging/feed ceiling into the shared 12V junction; buffer battery supports short transients but sustained overload still requires load budgeting.

### Safety baseline
- Positive path sequence: battery -> Class T fuse (near source) -> disconnect -> Lynx Distributor -> fused branch feeds
- Negative path sequence: battery -> SmartShunt -> Lynx Distributor negative bus -> all load returns on load side of shunt
- Big 3 rule set (vehicle side): keep factory wiring in place, add Big 3 as parallel/augmentation, fuse the alternator-to-battery positive run inline, and prep grounds to bare metal.
- If the truck uses an RVC ground-sensor loop, route the upgraded ground path through the loop per vehicle requirements.
- Battery thermal strategy: insulated battery box, ducted warm-air branch, thermostat/relay enable logic
- Wiring practices: grommets, loom, glands, abrasion protection, and bend-radius validation
- Reference links from workbook notes:
- `https://youtu.be/dSYKabw_rgs?t=651`
- `https://www.diodeled.com/45-channel.html`

### Electrical overview diagram (implementation)
- Full implementation-level topology diagram: `docs/ELECTRICAL_overview_diagram.md`
- Scope includes fuse IDs, fuse-holder/housing methods, branch wire-gauge selections, and documented sizing assumptions.

### RF-003 Distribution Topology Decision (Lynx Locked)
Decision date: `2026-02-12`

Approved architecture for Phase 1:
- `Victron Lynx Distributor M10` (`LYN060102010`) is the single distribution backbone.
- Current tracked unit price is `$192.47`.
- Current modeled `48V` fused branches (`4` total):
- MultiPlus-II `48/3000`
- SmartSolar `150/45`
- Sterling `BB1248120` output
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
- `docs/ELECTRICAL_fuse_schedule.md`

Scope covered:
1. Main battery protection (`Class T`) quantity, rating, and placement.
2. Lynx branch fuses for each `48V` branch (MultiPlus, MPPT, Sterling output, Orion input).
3. Vehicle-side alternator/Big-3 inline fuse requirements when that path is activated.
4. Any additional protective devices required by manufacturer manuals for both charge-source and load paths.

Method:
1. Pull max current requirements and overcurrent guidance from each device manual.
2. Confirm planned wire gauge/length/insulation assumptions for each run.
3. Size each fuse to protect the conductor first while meeting equipment requirements.
4. Build final fuse matrix with part numbers, quantities, and BOM row mapping.

## Solar
- Current target options captured: flexible array around `900W` (`9x100W`) or rigid array around `600-800W`.
- Constraint to validate: added roof load from solar plus Starlink plus fan/struts.
- Hardwall popup wiring baseline for planning: no hidden in-wall solar run; use exterior-rated coiled jumper cable(s) from roof solar exit to a lower-shell weatherproof passthrough.
- BOM scope for that routing method is tracked in `bom/bom_estimated_items.csv` row `121`.
- Open points: exact passthrough location and connector standard (`MC4` direct vs bulkhead adapter strategy) before SKU lock.
- Energy takeaway from the current modeled load: moving from `600W` to `900W` improves expected harvest by about `720-900 Wh/day` at `4` PSH, depending on realized system efficiency, but still does not close the office-workday deficit by itself.

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
5. Record what changed in `docs/TRACKING.md` (decision/risk/open questions) and `logs/LOG.md`.
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
- Water capacity candidates captured: `10 gal` compact concept and `~25 gal` tank option
- Pump candidate captured: Shurflo 3.0 GPM class
- Water heating candidate captured: portable propane tankless model
- Freeze and winterization strategy: TBD

## Cabinetry and structure
- Aluminum extrusion strategy: 10-series and 15-series mix, with service chase/toe-kick concept for wiring
- Modular mounting baseline now includes T-slot/strut rails both exterior (recovery/tool mounts like shovel/Maxtrax) and interior (baskets/hooks/tie-down points); BOM rows `119` and `120`.
- Drawer hardware baseline includes `4x` soft-close undermount slide kits for primary cabinetry drawers; BOM row `122`.
- Desk concepts captured: Lagun-style fold-in options and pneumatic pedestal concepts
- Material ideas captured: phenolic/richlite top, sound treatment, panel anti-rattle tape
- Monitor travel strategy concept: stow-low assisted deployment with structural bracing

## HVAC and condensation
- Heating approach in notes: diesel heater with possible branch to battery compartment
- Ventilation: Maxxair fan included in current camper config
- Condensation controls and climate envelope limits: TBD

## Safety
- Purpose: define a practical, build-ready safety baseline for the current architecture (`48V 15.36kWh` house bank, `12V` distribution, `120VAC` shore/inverter path, and propane-supported heating/hot-water concepts).
- Priority order: prevent ignition and overcurrent faults, preserve safe shutdown paths, detect hazards early, and make isolation/service repeatable.
- Final install gate: before energizing or using propane in service, verify all items against manufacturer manuals and complete licensed inspection where required.

### System-wide controls
- Keep one-line diagrams, fuse IDs, and conductor IDs synchronized across:
- `docs/ELECTRICAL_overview_diagram.md`
- `docs/ELECTRICAL_fuse_schedule.md`
- `docs/TRACKING.md`
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
- Maintain branch-level fuse-to-conductor coordination per `docs/ELECTRICAL_fuse_schedule.md`.
- Keep always-on detector branch (`12V-05`) protected but never switch-controlled.
- If sustained `12V` demand exceeds Orion headroom, treat additional `48V->12V` charger capacity (`BOM row 118`) as a safety action, not a convenience upgrade.

### 120VAC shore/inverter safety
- Main hazards: shock from miswired neutral/ground, ground-fault exposure at outlets, and overcurrent heating from undersized branch protection.
- Required controls:
- Keep shore path order: shore inlet (`TT-30`) -> hardwired EMS/surge protection -> AC-in DIN enclosure (`30A` UL489 breaker/disconnect) -> MultiPlus AC-in.
- Keep AC-out path order: MultiPlus AC-out-1 -> AC-out DIN enclosure (`20A` galley + `15A` office branch breakers) -> first-outlet GFCI strategy with downstream protected receptacles.
- Keep AC-in hardware on a `30A` / `10 AWG` basis, and set MultiPlus input current limit to the actual source (`15A`, `20A`, or `30A`) whenever adapters are used.
- Keep AC-out-2 as reserve-only in Phase 1 (labeled capped route; no energized branch hardware yet).
- Preserve continuous equipment grounding and chassis bond through all AC paths.
- Do not add a fixed downstream neutral-ground bond in branch wiring; neutral/ground behavior must follow MultiPlus transfer/bonding design.
- Commissioning checks:
1. Receptacle polarity test on each outlet location.
2. GFCI/RCD trip test at each protected branch.
3. Verify AC-out-2 remains de-energized as a reserve-only capped route in Phase 1.

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
- Record evidence in `logs/LOG.md` and track unresolved items in `docs/TRACKING.md`.

## Source artifacts
- `docs/SYSTEMS_workbook_build_notes.md`
- `docs/SYSTEMS_workbook_electrical_notes.md`
- `bom/load_model_wh.csv`
