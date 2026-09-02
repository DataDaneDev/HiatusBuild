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
- Canonical roof-solar architecture, geometry, electrical proof, and release gates: [SOLAR_configuration_matrix](../studies/SOLAR_configuration_matrix.md)
- Electrical decisions, risks, and unresolved items: [TRACKING](TRACKING.md)

### Planning snapshot (base model as-of `2026-09-02`)
- Battery bank: `3x 48V 100Ah LiFePO4` from BOM row 3 (`15.36 kWh` nominal at `51.2V` battery nominal).
- House architecture: `48V` core with Orion-Tr Smart `48V->12V` charging/step-down feeding a shared battery-backed `12V` junction.
- Inverter/charger: Victron MultiPlus-II `48/3000/35-50`, DC/inverter mode live-tested with no observed errors.
- Charge sources in current BOM: solar MPPT, dedicated `48V` secondary alternator path (`Mechman + WS500 + APM-48` migration baseline), shore AC charger path.
- Monitoring and protection: Cerbo GX, SmartShunt, battery temp sensing, Class T primary fuse + branch fusing.
- AC protection chain is purchased/locked for Phase 1 (`shore source/adapters -> portable EMS -> shore cord -> L5-30 inlet -> single 6-way AC DIN enclosure -> 30A AC-in breaker -> MultiPlus -> 30A AC-out main -> two 20A GFCI branches`). All four duplex receptacle boxes and the remaining `120V` work are enclosed and in regular owner-reported use; the owner confirms the MultiPlus is grounded to the truck chassis. Physical enclosure and chassis-ground installation are closed; retain explicit verification of the installed MultiPlus `M6 PE` bond, separate shell bond, `LINE/LOAD`, downstream GFCI trip, PE continuity, polarity, neutral isolation, and labels.
- Starlink Standard 4 X, fridge, pump, one driver-side `100W` charging outlet, two passenger-side `65W` charging outlets, and the installed `12V`/`48V` systems are in regular owner-reported use. Finish the labeled removable service face and any terminal/cable closeout still physically open.
- All four Renogy `175W` panels have arrived. The PV pass-through, two-pole disconnect, stationary wiring, and MPPT landing are complete; no panels are connected. Keep the `4S1P`/Victron `150/45` architecture. Direct bonding remains roof-preparation/caulk/cure gated, followed by series wiring, roof-side support, and controlled commissioning.
- The LF Bros diesel heater, fuel storage/line, and rear driver-side storage module are the main coupled installation gate. The mid-September counter milestone uses `48 in` Galley and `47 in` Desk live-edge Bubinga pieces; bring the actual sink and soap dispenser and prove the full drain/support envelope before cutting.

### Physical integration snapshot (`2026-09-02`)
- The permanent floor, electrical/Galley/Bench structure, water tank, and primary utility routes are installed. The batteries and ICECO are positively restrained. Remaining mobile retention is the not-yet-installed air fryer, Bench lid, monitor/laptop assembly, and other storage/cargo.
- Driver-rear shore inlet, AC feed, enclosures, and all four outlet boxes are installed and in regular use. The owner confirms the MultiPlus is grounded to the truck chassis. Remaining AC safety closeout is verification that this installed ground is the specified external `M6 PE` bond with a sound conductor/endpoint, installation or verification of the separate conductive-shell bond, and explicit PE/neutral/polarity/GFCI proof.
- Three `48V` battery branch harnesses are complete and the `1S3P` bank has been paralleled and in regular use for an extended period. The earlier isolated-charge/matching gate is historical.
- `12V` buffer branch remains `4 AWG`: `battery + -> F-11 100A ANL -> SW-12V-BATT -> fuse-panel main +`; `battery - -> fuse-panel main -`. Orion output uses `6 AWG` to the same junction through `F-07 60A/80V` on output positive. Because both sources meet at the fuse-panel main stud, `SW-12V-BATT` isolates only the buffer battery; it does **not** de-energize the fuse panel while the Orion remains enabled.
- Starlink, fridge, pump, and all three DC charging outlets are in regular owner-reported use. Confirm exact physical fuse slots/values, labels, terminal insulation, and any missing loaded-drop evidence during the next closeout pass rather than reopening functional status.
- Fresh-water plumbing, the replacement KUS sender, and the `35 gal` tank are owner-confirmed complete and extensively used. Only the future sink joints and separate graywater system remain wet-system work.
- Orion input protection is one verified `40A` MEGA (`58VDC` minimum under the locked `56.8V` charge ceiling; Victron `CIP138040020 40A/80V` is the replacement fallback) in Lynx Slot 4 feeding the existing `6 AWG` pair directly. No separate inline or DIN input fuse holder is used. Keep `6 AWG` and `F-07 60A/80V` on the Orion 30A `12V` output.

### Commissioning snapshot (`2026-08-02`)
- Owner confirmed `55.5V` at the `48V` bus and at the MultiPlus after pre-charge/energization.
- MultiPlus switch `I` brought inverter mode online; inverter light illuminated, slight hum was observed, and no error lights were reported.
- SmartShunt and Orion-Tr Smart are visible in VictronConnect. SmartShunt red fused `Vbatt+` lead should remain battery-side if SOC continuity while the main disconnect is open is desired; the parasitic draw is negligible for normal short storage windows.
- Cerbo GX is powered from the `48V` system through a small inline fused feed and uses `VE.Bus`/RJ45 to the MultiPlus; its Wi-Fi access point/remote-console workflow is active.
- AC input source type should be labeled `Shore power`, not generic `Grid`, for the mobile source-current-limited workflow.
- Household-outlet shore test used a reduced MultiPlus input-current limit (`10A` first test / `12A` maximum policy on a `15A` circuit). Observed values were about `1294W` shore input and about `54.3V x 21.6A` (`~1173W`) battery charge in bulk.
- MultiPlus battery charge profile has been owner-verified by supervised one-battery live behavior: settings were redone, the charger entered bulk, then quickly transitioned to absorption because the battery was already at/near `100%`, as planned. Current target remains absorption/charge voltage `56.8V`, float `54.0V`, short absorption dwell, equalization off, charger current within the connected-battery limit, and source-current limit set for the actual shore outlet. The Dumfume manual's `58.4V` value is documented, but because the same value is also listed as charge-limit/over-charge protection voltage, it is not the active routine target. Leave `DVCC` disabled unless a documented BMS/GX control path is added. No separate second-battery charge test is required just to close the charger-programming gate; AC-out/GFCI and alternator commissioning remain separate gates.
- Historical Battery 2/3 staging checkpoint (`2026-08-02/03`) is superseded by the owner-confirmed long-term parallel-bank operation reported `2026-09-02`; do not present isolated Battery 3 charging as current work.
- Owner-reported `12V` checkpoint (`2026-09-02`): the Orion/buffer system and installed `12V` loads have seen regular use. The prior implausible handheld-meter discrepancy is not an active behavior; retain the normal rule that any independently confirmed bus voltage above the configured `14.20V` absorption target is a stop condition.
- Normal shutdown/de-energize for the current bench system: MultiPlus `O`, turn off active `12V` loads, disable the Orion through VictronConnect or its remote on/off, de-energize/unplug shore, wait briefly, then open `SW-12V-BATT` and the main `48V` disconnect as required for the service scope. For startup, close `SW-12V-BATT` before enabling the Orion. Residual voltage on the Lynx/load side with disconnect open is expected from device capacitance but must be treated as live until metered near zero.

### Modeling rules (procurement-first plus full-load)
- Primary active-procurement source of truth is `bom/bom_estimated_items.csv`; returned/retired stable-ID history is in `bom/bom_inactive_items.csv` and is excluded from the active total.
- Load model is maintained in `bom/load_model_wh.csv` (model v5) and includes BOM-sourced installed loads, owner-supplied work electronics (kept out of BOM cost totals), and a conservative preliminary/future camper-audio listening profile. Audio is not near-term procurement.
- Legacy workbook WH model assumptions are retired and not used.
- Voltage convention: use `48V` as architecture label, but use `51.2V` nominal for battery Wh accounting.
- Run-length convention: measured physical layout lengths are cut-length source-of-truth; CAD values are planning references only.

### Input reference (maintained)
| Input | Current value | Source |
| --- | --- | --- |
| Battery bank | `3x Dumfume 51.2V 100Ah` (`1S3P`; manual allows up to `1S4P`). Per battery: charge voltage `58.4V +/-0.2V`; recommended charge current `20A`; max continuous charge `100A`; recommended discharge `50A`; max continuous discharge `200A`; over-discharge protect/recover `36.8V`/`43.2V`; discharge overcurrent `600A`; short-circuit `1800A`; low-temp charge protection approx `41F-50F`, recovery at `50F`; high-temp protection `157F`/`140F`. | `bom/bom_estimated_items.csv` row 3 + `references/Dunfume_36V_48V_100Ah_Battery_-_User_Manual.pdf` |
| Inverter/charger | MultiPlus-II `48/3000/35-50` | `bom/bom_estimated_items.csv` row 12 |
| Alternator charging | Dedicated `48V` secondary alternator path (`Mechman + WS500 + APM-48`) with `Upfitter #3 -> WS500 brown ignition` manual control and Lynx Slot 3 alternator branch fuse lock | `bom/bom_estimated_items.csv` rows `168-171`, `176`, `320` + `docs/core/ELECTRICAL_48V_ARCHITECTURE.md` |
| Obsolete pre-Mechman alternator charger/remote | Returned/obsolete; not part of primary layout, fuse planning, or commissioning | `bom/bom_inactive_items.csv` rows `18` and `26` |
| Legacy single-12V upgrade path | Mechman `370A` + Big 3 path is deprecated under the dual-`48V` migration baseline | `bom/bom_inactive_items.csv` rows `103` and `104` |
| DC-DC charger | Orion-Tr Smart `48/12 30A` (`360W`); `48V` input is protected by `F-05 40A` MEGA (`>=58VDC`) in Lynx Slot 4 with no second inline fuse, and `12V` output is separately protected by `F-07 60A/80V` | `bom/bom_estimated_items.csv` row 20 |
| 12V buffer battery | `12V 100Ah LiFePO4` on shared 12V junction (`F-11` + `SW-12V-BATT`) | `bom/bom_estimated_items.csv` rows 21, 124, and 125 |
| Solar array posture | Purchased `4x Renogy 175W flexible monocrystalline panels = 700W` on `2026-08-12`. The current official `RNG-175DB-H-G2` datasheet is the planning basis until the received labels confirm the exact SKU. A new packing screen fits two panels inside the measured `138 x 63 in` skin and one direct-mount panel across each side track, using real roof lands and a small local track-step spacer only if the actual panel needs it; this is not installation release. Direct roof attachment is locked; structural silicone is the active method subject to exact roof/backsheet preparation, coupon evidence, and full cure before travel. Carrier/cassette/rack fabrication is excluded unless the owner reopens it. The fixed-side pass-through/disconnect/stationary-wiring/MPPT path is installed; roof-side panel interconnect, support, and commissioning remain open. | `bom/bom_estimated_items.csv` row 24 + `docs/studies/SOLAR_configuration_matrix.md` |
| Solar controller | Retain the purchased SmartSolar `MPPT 150/45` for a candidate single `4S` Renogy string: `78.0V Vmp`, `95.6V Voc`, `8.98A Imp`, and `9.50A Isc`. Published-coefficient cold Voc is `114.86V` at `-40C`, well below the controller maximum. Hot-start margin is narrow: the datasheet lacks a direct Vmp coefficient and a published-coefficient estimate reaches about `61.87V` at `70C`, essentially the `56.8V + 5V` startup threshold before route drop. Received-label proof and hot-roof restart/tracking commissioning remain hard gates. | `bom/bom_estimated_items.csv` row 25 |
| Load profiles (BOM + owner-supplied office loads) | `core_workday`, `winter_workday`, `minimal_idle_day` | `bom/load_model_wh.csv` |
| Owner-supplied office assumptions | Laptop + 27 inch 1440p monitor + tablet/peripheral charging | `bom/load_model_wh.csv` rows marked `Owner-Supplied` |

### Modeled expected usage
Load totals below are from `bom/load_model_wh.csv` model v5 (BOM loads plus the purchased Ninja SP151 cooking appliance, owner-supplied office loads, and a conservative preliminary/future camper-audio profile).

| Scenario | Daily energy | 5-day workweek energy | 7-day week energy | Dominant contributors |
| --- | --- | --- | --- | --- |
| `core_workday` | `3,915 Wh` | `19,575 Wh` | `27,405 Wh` | Laptop, monitor, Starlink, cooking, inverter idle, conservative future-audio allowance |
| `winter_workday` | `4,829 Wh` | `24,145 Wh` | `33,803 Wh` | Laptop, monitor, Starlink, diesel heater, cooking, conservative future-audio allowance |
| `minimal_idle_day` | `624 Wh` | `3,120 Wh` | `4,368 Wh` | Fridge + always-on monitoring/detector loads |

### Capacity analysis (corrected battery bank)
| Metric | Formula | Result |
| --- | --- | --- |
| Nominal battery energy | `51.2V x 100Ah x 3` | `15,360 Wh` |
| Usable energy to 20% reserve floor | `15,360 x 0.8` | `12,288 Wh` |
| Core day depth of discharge | `3,915 / 15,360` | `25.49%` per day |
| Winter day depth of discharge | `4,829 / 15,360` | `31.44%` per day |

### Autonomy (no charging)
| Scenario | Days (`100% -> 20%`) |
| --- | --- |
| `core_workday` | `3.14` |
| `winter_workday` | `2.54` |
| `minimal_idle_day` | `19.69` |

### Charging potential
All values are planning-level and should be replaced with measured charge logs after shakedown tests.

#### Solar charging (`700W` purchased array)

- The owner purchased `4x Renogy 175W flexible panels = 700W` on `2026-08-12`. The candidate electrical posture is one `4S` string on the purchased SmartSolar `150/45`; exact received labels and hot-roof behavior control final acceptance. Direct roof attachment is the mounting baseline because the larger Renogy footprint supersedes the Arch Pro layout; industrial removable fastener vs structural silicone remains the material decision. Do not reintroduce a carrier/cassette/rack unless the owner explicitly reopens it.

Use the existing `68%` end-to-end planning factor until measured harvest exists. It may be optimistic if hot panels are directly bonded or if the `4S` string operates near the controller's hot-voltage threshold.

| `700W` at `68%` | 2 PSH day | 4 PSH day | 5 PSH day | Net vs `core_workday` at 4 PSH | Net vs `winter_workday` at 4 PSH |
| --- | ---: | ---: | ---: | ---: | ---: |
| Purchased Renogy array | `952 Wh` | `1,904 Wh` | `2,380 Wh` | `-2,011 Wh/day` | `-2,925 Wh/day` |

- Break-even is `8.22 PSH/day` for `core_workday` and `10.14 PSH/day` for `winter_workday`; roof solar is supplemental charging, not guaranteed workday autonomy.
- Current roof-fit, mounting, electrical proof, and release gates: `docs/studies/SOLAR_configuration_matrix.md`.

#### Alternator charging (dedicated `48V` secondary alternator path)
- Active migration baseline: Mechman dual-alternator kit + WS500 regulator + APM-48 protection module.
- `Lynx Slot 3` alternator branch fuse (`F-04`) is locked at `200A/80V MEGA` at the house-bank/Lynx end of the alternator positive run. Mechman's published `48V Elite` curve reaches about `145.7A`; `125%` is about `182A`, making `200A` the next standard fuse size while remaining within the installed `2/0 AWG` conductor envelope. Mechman guidance requires the fuse within `12 in` of the battery-bank connection; if final layout places the Lynx farther away, add a bank-end fuse holder rather than leaving the branch unfused at the bank end.
- The owner-confirmed `PH-VAN` harness combines regulator power and positive voltage sense on one short red lead. Land it on the alternator/load side of `F-04` and protect it immediately with one compact in-line high-interrupt DC fuse assembly: Eaton/Bussmann `HEB-AA` (`600V`) holder plus Littelfuse `KLKD015.T` (`15A`, fast acting, `600VAC/DC`) midget fuse. Use short `14 AWG` pigtails and a sealed `14-to-16 AWG` splice to the harness. This is one in-line holder in the loom; no DC fuse panel, DIN rail, or enclosure is added.
- Put the separate Wakespeed `500A/50mV` shunt on the battery side of the hard-mounted Victron SmartShunt in the same common battery-negative path: `battery negative combine -> Wakespeed shunt -> SmartShunt -> Lynx/system negative`. Purple/current-sense-high faces battery negative; grey/current-sense-low faces the SmartShunt/Lynx system side. Configure `Shunt at Battery`. This preserves the SmartShunt-to-Lynx hard connection while keeping every battery current path through both shunts.
- Manual charge-enable/disable path is locked to Ford `Upfitter Switch #3` feeding the WS500 brown ignition/enable wire through local inline fuse `F-15` (`3A`, 12V control circuit).
- `WS500` white `Feature-In` is reserved for future automatic fault-interlock work and is not required in Phase 1.
- Mechanical-only staged driving with the Mechman alternator installed but unwired/electrically disabled is owner/Mechman-confirmed acceptable after the idler/belt/noise check passes; this does not commission alternator charging.
- WS500 rough-in default is regulator near the truck-bed house electrical area so analog shunt/battery-sense wiring stays short; run the alternator-leg wiring forward in separate labeled looms from the `2/0` charge pair.
- Cable decision lock for this pass: reuse existing uncut `2/0` inventory for the alternator charge path (`~20 ft` one-way assumed), with dedicated equal-size negative run.
- Obsolete pre-Mechman alternator-charger hardware is returned/removed from active planning and should not appear in primary fuse/layout decisions.

#### Shore charging (MultiPlus-II charger path)
- Charger limit from model string: `35A`; Dumfume manual lists charge voltage as `58.4V +/-0.2V` but also lists charge-limit/over-charge protection at `58.4V`, so current commissioning uses a lower routine target: `56.8V` absorption/charge with `54.0V` float. For the `3x` bank, manual-backed current references are `60A` recommended charge total and `300A` max continuous charge total, so the MultiPlus `35A` maximum is within battery-bank limits.
- Current first-live result: AC-in shore charging was proven at household-outlet limits with MultiPlus input limit reduced (`10A` first test; `12A` policy ceiling on a `15A` circuit). Reported Cerbo values were about `1294W` from shore and about `54.3V x 21.6A` into the battery bank in bulk.
- Supervised charge-profile verification: fixed LiFePO4 settings were redone and live behavior matched the plan on the first battery; charging entered bulk, then quickly transitioned to absorption because the battery was already at/near `100%`. Earlier settled snapshot showed `56.8V` on the MultiPlus/SmartShunt with `0A` charge current, battery display about `55.8V`, SmartShunt SOC set to `100%`, and shore input current limit `12A` on the household-source test.
- Current charger profile: `56.8V` absorption/charge target, `54.0V` float, `52.8V` storage if available, equalization off, lithium temperature compensation behavior disabled/confirmed, minimum absorption time (`1h` in the observed `1-8h` field), repeated absorption `0.25h`, and charger current at or below the MultiPlus `35A` limit; if charging one isolated battery, cap current at `20A`.
- `DVCC` remains disabled in the current architecture because there is no documented BMS-to-GX control path.
- AC input current policy: label AC Input 1 as `Shore power`; use `10A` for first tests and `12A` maximum on a normal `15A` household circuit; use the actual pedestal/source rating for `20A`/`30A` sources.
- Ideal bulk-only recharge times at the current `56.8V` commissioning target and `35A` charger limit remain reference-only until measured charge logs replace them:
- Replace one `core_workday`: `1.97h`.
- Replace one `winter_workday`: `2.43h`.
- Recharge full `3x` bank from `20%` to `100%`: `6.18h`.
- Recharge one isolated `48V 100Ah` battery from `20%` to `100%`: about `3.61h` at the single-battery `20A` current cap.
- Real-world times are longer due to absorption taper near full charge, reduced household input-current limits, and any configured charge-current derate.

### Operational implications and constraints
- Battery capacity now supports roughly `2.5-3.1` office-workdays without charging in the conservative future-audio model, depending on season and reserve policy; actual near-term office-only use may be better.
- At the purchased `700W` case and base `68%` factor, `4` PSH still leaves `2,011Wh/day` and `2,925Wh/day` deficits for the modeled core and winter workdays. Roof solar is a charge-source reducer, not guaranteed workday autonomy.
- Shore charging can materially recover SOC in a single evening (`~6.18h` from `20%` to `100%` in bulk-ideal terms).
- Alternator recovery potential is expected to materially exceed the obsolete pre-Mechman charger path once the dedicated `48V` alternator path is commissioned.
- Current execution risk is no longer charger-capacity-limited operation; it is migration/commissioning quality (fitment, regulation, protection, and measured thermal behavior).
- MultiPlus-II `48/3000` inverter continuous output (`~2,400W`) can be exceeded by simultaneous induction + Ninja SP151 air fryer/toaster oven + other AC loads, so high-draw AC loads need sequencing.
- Orion-Tr Smart `48->12V 30A` charger (`360W`) is the continuous charging/feed ceiling into the shared 12V junction; buffer battery supports short transients, including audio bass peaks, but sustained overload still requires load budgeting.

### Safety baseline
- Positive path sequence: battery -> Class T fuse (near source) -> disconnect -> Lynx Distributor -> fused branch feeds
- Negative path sequence: battery -> Wakespeed `500A/50mV` shunt -> SmartShunt -> Lynx Distributor negative bus -> all load/charge returns on the system side of both shunts; do not separate the SmartShunt from the Lynx
- Dedicated alternator branch grounding rule set: run equal-or-larger dedicated negative cable from secondary alternator to house-bank return path and avoid sheet-metal return paths.
- MultiPlus mobile-installation protective earth is mandatory: external `M6 PE` lug -> `10 AWG` green stranded copper (`4 mm²` Victron minimum) -> verified truck-chassis bond point. Bond the aluminum Hiatus shell separately into the same equipment-ground network; do not use shell/80/20 as the only PE conductor.
- Keep AC PE, AC neutral, and DC negatives distinct. Do not jumper MultiPlus case/PE to Lynx or `12V` negative and do not add a fixed downstream neutral-ground bond; leave the MultiPlus internal ground relay enabled. Confirm Mechman case-ground behavior and verify no chassis path bypasses the SmartShunt before alternator commissioning.
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
- Current tracked unit price is `$211.65` (BOM row `6`).
- Current Lynx fused outputs in use (`4` total):
- Slot 1: MultiPlus-II `48/3000` (`F-02 125A`)
- Slot 2: SmartSolar `150/45` (`F-03 60A`)
- Slot 3: Dedicated `48V` alternator branch output (`F-04 200A/80V`)
- Slot 4 (`F-05`) feeds Orion-Tr Smart `48/12` through one `40A` MEGA body-marked at least `58VDC`; standalone `F-06` is retired.
- `1x` Lynx Distributor covers the current four active branch outputs with no spare fused slot.
- If another fused `48V` branch is added later, add a second Lynx module or a separately engineered branch in that phase.

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
2. Lynx branch fuses for active outputs: MultiPlus, MPPT, dedicated alternator branch, and Orion input (`F-05 40A`, `>=58VDC`, in Slot 4); no standalone Orion input fuse.
3. WS500 low-current fuse requirements and alternator-branch protection coordination.
4. Any additional protective devices required by manufacturer manuals for both charge-source and load paths.

Method:
1. Pull max current requirements and overcurrent guidance from each device manual.
2. Confirm planned wire gauge/length/insulation assumptions for each run.
3. Size each fuse to protect the conductor first while meeting equipment requirements.
4. Build final fuse matrix with part numbers, quantities, and BOM row mapping.

## Solar
- Received array: `4x Renogy 175W flexible monocrystalline = 700W`, one `4S1P` string on the purchased Victron `150/45`. The MPPT battery-output branch is `F-03 60A/80V MEGA` in Lynx Slot 2; the single series string currently has no separate `F-09` PV-string fuse.
- Owner test-fit `2026-08-27`: one-panel physical fit plus measured layout indicates the four-panel package can coexist with Starlink and MaxxAir while using nearly the complete roof. Actual labels/connector geometry and full `1:1` all-panel placement still control final coordinates and service access.
- Mounting is direct-to-roof with the exact structural-silicone stack allowed by the controlling received-panel instructions. Wash/decontaminate the roof, verify substrate/backsheet compatibility, coupon-test adhesion/removal/heat, and prove drainage/cure. On one panel, complete static inspection, heat/water/roof-cycle proof, and a temporary independent track-anchored safety restraint suitable for the test. Then use a private/closed-course low-speed test with inspection stops; only after that passes, run a deliberate progressive road-acceptance test with staged speed/stop inspections. Routine highway travel and the remaining panel bonds wait until the one-panel sequence passes.
- PV fixed-side work is complete: pass-through, two-pole disconnect, stationary `12 AWG` two-conductor run, and MPPT landing. Preserve the three panel-to-panel series mates and route only the two free `4S1P` string ends into that completed two-pole path. `12 AWG` is the conductor size; this is not a `12V` circuit.
- No panels are connected. During roof-side wiring, verify/support the moving/exposed lead through the full `28 in` roof stroke and cab/bed articulation so the pass-through, gland, adhesive guides, and terminals carry no spring, motion, or highway load.
- Energy takeaway: `700W` remains supplemental. Keep the dedicated `48V` alternator and shore path for predictable recovery; keep the `150/45` unless measured cool start and hot-roof restart/tracking fail.

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
- `bom/load_model_wh.csv` v1 (workbook-derived chart), v2 (BOM-only), v3 (BOM plus owner-supplied office loads), and v4 (added preliminary/future camper audio) are superseded by model v5, which adds the purchased Ninja SP151 appliance load while retaining the audio allowance.

## Camper audio
- Camper audio implementation owner: [CAMPER_audio_system](../implementation/CAMPER_audio_system.md). Status: preliminary/future-roadmap, not near-term procurement. Draft package is a DC-first `2.1` camper-only system: Samsung `S11 Ultra` tablet -> Kicker `46KMC2` marine media receiver -> Kicker `CSC67` `4 ohm` speaker pair plus Kicker `49PTRTP10` powered down-firing 10 in subwoofer.
- Active BOM rows `189-193` track deferred/preliminary source unit, speaker pair, powered sub, 4 AWG sub power/fuse kit, RCA/speaker wiring, mounts, and install consumables. Inactive BOM row `101` preserves the deprecated sound-system placeholder.
- Electrical posture: KMC2 uses a `15A` source/head-unit branch from the `12V` fuse panel; PTRTP10 uses a separate `40A` source fuse near the `12V` source takeoff with `4 AWG` positive and matching `4 AWG` return to the `12V` negative bus/main stud. Audio returns should not use shell/chassis as the normal current path.
- 12V headroom note: the selected audio system can theoretically peak around `55A` at `12V` (`15A` source unit + `40A` powered sub branch), above the Orion `30A` continuous 12V feed. The `12V` buffer battery supports peaks and short loud sessions, but sustained high-volume use should be watched on the `12V` battery voltage/SOC while other 12V loads are running.
- Physical placement default: KMC2 in the driver-side electrical/workstation/DC-shelf face; powered sub low in a dry driver-side toe-kick/step-box or dry bench volume near the `12V` junction; speaker cutouts/pods wait for wall panel thickness, roof-down sweep, and furniture-service checks.

## Communications
- Primary internet path: purchased Starlink Standard 4 X plus OEM mobility mount (`$405` owner-reported aggregate hardware total), with the purchased third-party DC converter and factory AC/inverter fallback. Current service is `$55/month`; exact plan name is not recorded, and the owner intends to move to an unlimited plan later.
- Secondary/fallback path: TBD (cellular path and carrier diversity not frozen)
- Moving-roof baseline: Starlink uses one rugged shielded fixed-body RJ45 panel bulkhead and removable retractile roof jumper, with a long outdoor shielded ground-deployment alternative and complete OEM cable retained for direct recovery. Owner report `2026-08-27`: the installed pass-through/coil works and the Standard 4 X operates from its switched dedicated `12V` conversion branch through a `20A` blade fuse. Final labels, weather/retention inspection, roof-motion inspection, and travel inspection remain; remove/stow the exposed roof equipment for tight brush. Full topology and acceptance detail live in [STARLINK_SOLAR_MOVING_UMBILICAL](../plans/STARLINK_SOLAR_MOVING_UMBILICAL.md).
- An exposed side-mounted energy chain is no longer the default: without a measured recess or trough its return bend projects or bunches outward when the roof closes, it does not make the midspan branch-proof, and it is harder to remove. A sleeve/service loop without a take-up mechanism is likewise only a hanging cable. Reopen either architecture only if physical measurements reveal a real inboard guide volume.
- `Sheltered` is not an assumed location. Use that term only if an existing rigid feature projects outward farther than the jumper and the jumper remains inside its contact shadow through the full roof stroke. No `front guard` or pouch is part of the current camper baseline.
- Starlink lead path is the purchased third-party Standard 4/4X Type-4-to-RJ45 pigtail pair, purchased shielded retractile Ethernet prototype, and purchased Neutrik `NE8FDX-P6-W` plus `NE8MXR1-B-TOP-D` panel/termination package. Both Neutrik cable assemblies are complete, and every green-coil conductor passed the owner's DMM continuity check; repeat that check on the short jumper. Neutrik publishes shielded Cat6A, PoE Type 4 Class 8 / `100W`, `>1000` mating cycles, and IP65 when correctly mated/capped. Shield-shell continuity, heat/dropout, spray/retention, final panel location/cut, and full-roof-stroke strain relief remain open. Preserve the complete factory Starlink cable as an unmodified direct recovery spare; the purchased Furnique coupler and 1 ft shielded jumper support optional panel-fed ground mode.
- Roof-mount lead is the purchased TRIO Gen 3 Standard Speedmount around the dish. Preserve both purchased attachment paths: removal-first magnets with VHB-backed roof discs after full-contact/cure proof, and the `75 mm` through-hardware for an extrusion hard-mount fallback. The full framed dish remains removable and keeps the factory kickstand usable. Edge protection is not branch-proof; remove/stow or ground-deploy it for tight brush.
- An ordinary RJ45 ground cable is physically compatible with the panel for dry-weather deployment; wet service needs a compatible sealed cable-side carrier or purpose-built weather-sealed ground lead. The upper terminal interface keeps the Type-4 adapter's weatherproof gland. Scanstrut through-cable gland paths are withdrawn from the finished Starlink quick-disconnect design.
- Solar lead path uses the installed continuous retractile cord/pass-through in the camper-to-cab gap, with no exterior quick disconnect and no manual roof-motion step. The fixed-camper compression gland is installed just above the Starlink entry behind the cab. Keep the helix outside and retain independent structural support so the gland, adhesive guides, and terminals carry no spring/highway load. After the inside clamp, exactly two accessible sealed splices transition to stationary `12/2`; the two-pole load-break, stationary wiring, and MPPT landing are complete. During roof-side panel wiring, preserve `4S1P`, route only the two free string ends through this path, and prove full roof stroke, cab/bed articulation, spray, force, heat/current, and post-install condition before routine PV use. No four-to-one branch/combiner is used.

## Plumbing (if included in phase 1)
- Current baseline: fresh-water tank, gravity fill/vent, KUS, pump, accumulator, PEX, and BLUE/RED camper service interfaces are complete and in extensive owner use. Remaining work is the sink/faucet/soap-dispenser connection after the Bubinga counter work, the separate graywater system, and HOTTAP installation after receipt.
- Interior layout and wet-spine draft owner: [INTERIOR_furniture_layout_and_galley](../implementation/INTERIOR_furniture_layout_and_galley.md). Current direction is a passenger-side lofted fridge/wet-spine exoskeleton: Iceco/fridge raised about `16 in`, pump/accumulator relocated into the owner-measured `6 in` gap between the cooler support and house batteries, rear fill/vent and one BLUE/RED hot-water service plate, graywater cassette, and no interior water-heater volume. The wet pack requires a nonconductive splash divider and drained leak path toward the bed floor, not reliance on the battery cases as water protection.
- Water capacity: purchased `35 gal` Sprinter/Transit wheel-well tank. Full water mass is about `292 lb` before tank/brackets/plumbing; plan around roughly `312+ lb` installed when full. The owner-provided order record corrected the prior `36 gal` assumption on `2026-09-01`.
- Historical pre-cut tank-port note (`2026-07-16`): four molded ports were observed on each end and the top opening was then unresolved. That discovery state is superseded by the owner-confirmed installed/operational fill, vent, KUS, and plumbing baseline; retain it only as provenance for future service.
- Tank restraint posture (`2026-08-02` owner report): the wheel-well tank is hard-mounted with two metal straps tightened into the truck-bed-wall plusnut locations and supported within the hard-mounted Galley structure. The wheel-well form factor lowers center of gravity and overturning moment. Confirm clean full thread engagement at the plusnuts, witness-mark the strap hardware, and recheck after the first loaded drive; any visibly cross-threaded or partially engaged location is a pre-drive rework item.
- Plumbing function evidence: the SHURflo `4008-101-A65` pump, SEAFLO accumulator, tank, interior PEX, fill/vent, rear service ports, and KUS have seen extensive installed use as of `2026-09-02`. Preserve approximately `37 PSI` accumulator precharge with the water side fully depressurized; leak-check new or disturbed sink joints rather than reopening the completed fresh-water baseline.
- Purchased galley fixture baseline: FORIOUS black pull-out faucet with soap dispenser plus Sarlai black `15 in x 15 in` topmount sink with approx. `11 in x 13 in` interior basin (BOM rows `207-208`). The FORIOUS manual and product diagram confirm separate `3/8 in` hot/cold supply-hose connections. The exact EFIELD two-pack of `1/2 in PEX-B barb x 3/8 in OD compression male` adapters (ASIN `B0C7QBNVG9`) was purchased `2026-07-25`; seat each faucet hose nut directly on the male compression seat with no PTFE tape.
- Current sink-layout implication (`2026-09-02`): take the actual Sarlai sink and FORIOUS soap dispenser to the planned mid-September routing work for the `48 in` live-edge Bubinga Galley piece. The sink is topmount, so its flange can live on the counter while the bowl passes through a local frame opening, but final cuts wait on the actual cutout, bowl, drain body, faucet/soap shanks/nuts/hoses, support rails, tank clearance, service access, and proof of continuous drain slope.
- Graywater vessel is now the LF Bros kit's supplied `10 L / 2.64 US gal` plastic tank, provided it remains never-fueled. Treat it as a positively retained, vented removable cassette with a normally closed outlet; preserve the top cap as cleanout/service access. The sink interface is still mockup-gated: inventory the actual basket/tailpiece first, then target a compact waterless trap and a continuously falling `3/4-1 in` smooth-wall drain hose into a top inlet. Do not use the existing `1/2 in` clear hose as the sink drain; reserve it for the short dump/discharge leg. Capture remains the default, with controlled discharge only where allowed.
- Interior plumbing state (`2026-09-02` owner report): gravity-fill hatch, fill/vent, direct BLUE cold-out, RED hot-return, pump/accumulator/PEX, and KUS/Cerbo tank monitoring are complete and in regular use. The BLUE source retains its accessible ball valve; RED remains intentionally unvalved because it is the removable heater return to sink hot. Keep access for the new sink joints and graywater path only.
- Sender-mount resolution (`2026-08-03`, operationally superseded `2026-09-02`): the failed first KUS/`FLS-U` hardware was replaced with a new `FLS-U` ring, main gasket, and matched long screws. The sender and tank have since seen extensive use. Preserve top access and inspect only after disturbance or evidence of seepage; do not retain a first-fill pressure/dwell gate as current work.
- Hot-water decision posture (`2026-09-02`, owner-confirmed selection; delivery pending): propane only. The purchased HOTTAP has not arrived; propane geometry is mocked. The purchased core package is one outdoor-use Joolca HOTTAP V2 Essentials, one Quick-Release HOTTAP Bracket, and one HOTTAP V2 Mount Cover. Mount it directly to a structurally backed exterior side face of the rear box with the purchased bracket and cover; it remains outside the cylinder compartment and no articulating arm or box-side water plate is used. The direct RAINPAL/HQMPC camper-port prototype passed physical installation and quick-disconnect operation; its projection is accepted with the owner-designed clicked-on travel caps. The installed stack uses one compact `304 stainless` bulkhead per port (`1/2 in FNPT` rear, `3/4 in MGHT` front) with a directly threaded metal male tap adapter that physically proved compatible with the Joolca female socket. Melnor `15409` is unavailable and remains only the visual/profile reference despite Joolca's documented Melnor QuickConnect compatibility. The acquired HQMPC two-set ASIN `B07FHXLKH5` supplied the two installed female-GHT/male-QD adapters and passed owner-reported connection operation. The RAINPAL bulkheads are installed, and the owner-designed clicked-on travel caps operate correctly. GARDENA `39004-G` is now only a fallback. Only BLUE stays behind an accessible source valve; RED is an unvalved removable-hose return to faucet hot. The QD3 key, `1/4 in` reducer, rear `3/8 in` hose-barb transition, and second QD ecosystem are rejected from the installed path. HOTTAP Essentials supplies one `5 m` shower assembly split into `4 m` and `1 m` red female/female sections; preserve both for their intended hot-side duties and prefer a separate roughly `30 in` BLUE-to-heater leader with Melnor `9MQC`/`8MQC` female sockets after fit testing. The `1 m` red section remains a valid no-purchase cold-feed trial, not the preferred final hose. Joolca states that HOTTAP is recreational wash hardware, not a drinking/sanitary-water appliance. Source/fitting details and the complete inline count live in [INTERIOR_furniture_layout_and_galley](../implementation/INTERIOR_furniture_layout_and_galley.md#propane-hot-water-routing-baseline-2026-08-01-installed-camper-ports).
- Rear propane package: the `2026-07-26` purchase includes the Flame King `YSN10LB-ALM` cylinder, CALPOSE gauge, and bracket/strap pack. The Safoner hatch provides a neat propane-hose pass-through through the rear box. The AWW stone mat is for the outdoor shower.
- HOTTAP mounting/operation: Joolca explicitly permits vehicle mounting. Through-bolt the purchased Quick-Release HOTTAP Bracket—previously documented as the vehicle quick plate—to proven structural backing on the exterior box side; do not ask the aluminum skin alone to carry road vibration. Keep the purchased HOTTAP V2 Mount Cover on for travel/dust protection and remove/open it as Joolca requires before operation. Disconnect LP and water for travel. Before first ignition, prove the actual exterior location against Joolca's published operating clearances and confirm that exhaust/heat do not impinge on the camper, box door, cylinder compartment vents, stored gear, or cover. Never burn the HOTTAP inside the cylinder box, even with its large door open.
- Freeze and winterization strategy (`2026-08-01` owner-confirmed port routine): after every freezing-weather use, close LP and the BLUE source valve, shut down the HOTTAP, open the sink hot side to relieve pressure, disconnect and gravity-drain both Joolca hoses, and follow the HOTTAP manual's drain/storage procedure. With the heater hose removed and faucet hot side open, use only regulated low-pressure air through the RED quick-disconnect to clear the short hot-return line toward the sink; the removable hose is the RED-side disconnect, so no separate RED valve is required. Arrange the short PEX-to-bulkhead terminations without trapped low points, clean the male exterior plugs, and install the clicked-on travel caps. Use the pump and fully open BLUE outlet for normal tank emptying; the low south boss stays unopened or receives only a low-profile plug because an exposed valve would occupy the entry footpath. A removable upstream suction-flex connection remains the dead-pump gravity fallback. Emptying the tank does not winterize the strainer, pump, accumulator, fixture cartridges, QDs, or low loops.
- Gravity-fill vent hose correction: owner-measured vent nipple is about `10 mm` OD on the main land and `11 mm` OD at the largest barb/ridge. Specify `10 mm ID` food-grade/potable tube, or `3/8 in ID` as the common inch fallback; the previously ordered `1/2 in ID x 5/8 in OD` tube is oversized.
- Current water-integration order: preserve the proven fresh-water/KUS system, complete the sink after the Bubinga routing work, leak-check the new joints, then build and spill-test the separate graywater path.
- Tank-level electrical baseline: purchased KUS SSS/SSL `14.5 in`, US `240-33 ohm`, two-wire sender connects directly to one native Cerbo GX MK2 Tank-input column. On the front-panel legend, Tank columns are `1-4` left to right, upper row `DATA`, lower row `GND`: connect KUS black/signal to upper `DATA` and KUS pink/return—the owner's red extension—to lower `GND`. Use `1.0 mm²` ferrules with `>=10 mm` pins for the `18 AWG` extensions, or `10-11 mm` untinned exposed stranded copper if only short ferrules are available. No separate 12V feed, fuse, analog gauge, VE.Direct cable, or GX Tank 140 is required.
- Current plumbing route (`2026-08-01` installed-port baseline): draw from a low north-end port through the existing tank shutoff, full-flow 90 only if the real turn requires it, flex, strainer, pump, discharge flex, and accumulator. Mount the purchased SHURflo/SEAFLO pack in the measured `6 in` cooler-to-battery gap on a thin vibration-isolated plate supported by extrusion; preserve strainer-bowl removal and point fittings/leak paths away from the batteries behind a nonconductive splash divider. The SEAFLO `SFAT-075-125-01` accumulator has two `1/2 in MNPT` pass-through ports; its supplied white swivels are flexible-hose barbs, not PEX-B. Use the purchased RecPro double-FIP hose on the pump side and one accepted YVSKM female-swivel PEX-B adapter on the outlet. After the accumulator, one `1/2 in` PEX tee branches to faucet cold while the straight leg continues to an accessible BLUE service valve and compact direct-profile wall port. The installed BLUE path reuses the purchased `UP120A5` after the valve and threads it directly into a `1/2 in FNPT` / `3/4 in MGHT` stainless bulkhead; the physically proven HQMPC female-GHT/male-QD adapter occupies the exterior GHT. The separate RED path uses the same compact bulkhead/QD hardware but omits the BLUE source valve; it is an unpressurized return when the heater hose is disconnected and runs directly to faucet hot. Do not replace the now-working stack with the previously considered Legend combination valve without a demonstrated service or depth benefit. Connect the BLUE hose with its valve closed, open BLUE only for use, then close BLUE and relieve pressure before disconnecting; RED has no separate valve. Prefer a separate approximately `30 in` cold leader from BLUE to the heater and retain the supplied `4 m + 1 m` red shower assembly; use the `1 m` red section only as the no-purchase cold-feed trial. No QD3 key/reducer/barb stack, box-side plate, CPC jumper set, arm service loops, permanent splitter, electric heater branch, manifold, bypass, or concealed heater cubby remains in the lead prototype.
- Exterior-cut dependency update (`2026-09-02`): the driver-rear shore inlet, passenger-rear water pass-throughs, water fill/vent, KUS, PV pass-through, PV disconnect, stationary PV run, and MPPT landing are complete. Remaining cuts are the staged heater turret and final sink/graywater geometry—not convenience-driven shell penetrations.

## Cabinetry and structure
- Interior furniture/layout draft owner: [INTERIOR_furniture_layout_and_galley](../implementation/INTERIOR_furniture_layout_and_galley.md). Recommended planning direction is the office-first hybrid: passenger-side lofted Iceco/fridge on an extrusion exoskeleton, pump/accumulator below the fridge next to the `35 gal` wheel-well tank, adjacent separated battery bench, driver-side electrical closet/workstation/DC shelf, diesel heater low in the driver-side utility zone, and clear center aisle/cabover movement.
- Driver-side workstation implementation draft: [INTERIOR_driver_side_workstation](../implementation/INTERIOR_driver_side_workstation.md). It captures the current best direction for a driver-side service-spine desk, stow-low monitor cassette/rising VESA spine, electrical-closet/DC-shelf interface, shallow storage, travel locks, cable management, heat/noise control, and roof-close acceptance tests.
- Aluminum extrusion strategy: the broad `15-series` starter order is superseded. Default to `10-series` prototype stock/hardware for furniture where practical; reserve larger extrusion for measured heavy/dynamic freestanding modules that prove they need the stiffness, such as the lofted fridge skeleton, electrical closet frame, monitor mast/spine, or battery bench structure if dry-fit proves the load path needs it.
- Current physical state (`2026-09-02` owner report): the main electrical/Galley/Bench structure is hard-mounted; batteries and ICECO are restrained; the rear driver-side storage module, Bench lid, desk/monitor hardware, air-fryer home, other storage, and final skins remain. Coordinate the rear module with the diesel tank/pump/fuel route before installing either. The FLEXISPOT Foldex chair is ordered. Final surfaces are `48 in` Galley and `47 in` Desk live-edge Bubinga pieces; preserve the real chair/knee/aisle fit gate before final mounting.
- Travel restraint baseline: battery and ICECO capture are closed. The air fryer needs shelf lips/hard stops plus a positive strap/latch; store the basket/rack/pan so they cannot chatter or become projectiles. The monitor/laptop arms need a padded hard-stop cradle contacting safe structure/bezel/VESA areas, with restraint that unloads the arms and does not press on an LCD. Size Bench gas struts from measured lid mass/center of gravity and hinge/bracket geometry; use symmetric geometry plus a separate positive closed latch and mechanical open stop.
- Panel strategy: living-facing furniture surfaces should use mechanically removable overlay panels over the frame; service zones stay exposed or quick-removable. Magnetic service covers are acceptable only for light non-structural panels and need locator/anti-shear features plus backup retention where loss would matter.
- Current furniture CAD and May 4 generated diagrams are reference-only after installed-shell layout changes; re-CAD block envelopes around the passenger-side lofted fridge/wet-spine, tank overlap, battery bench, driver-side electrical closet, and desk before final cut lists.
- Modular mounting baseline now includes T-slot/strut rails both exterior (recovery/tool mounts like shovel/Maxtrax) and interior (baskets/hooks/tie-down points); BOM rows `119` and `120`.
- Drawer hardware baseline includes `4x` soft-close undermount slide kits for primary cabinetry drawers; BOM row `122`, but final lengths are deferred until fridge/tank/electrical module envelopes are verified.
- Desk concepts captured: fixed full-time work surface with possible auxiliary fold leaf; Lagun-style or pneumatic concepts should remain secondary unless the measured work envelope proves they are stable enough.
- Material ideas captured: phenolic/richlite top, sound treatment, panel anti-rattle tape, frosted/angled LED strips, smoke-grey acrylic shallow cubby covers.
- Monitor travel strategy concept: stow-low/face-down assisted deployment with structural bracing, hard stops, positive travel locks, cable drag chain, and a visible roof-safe state before pop-down.

## HVAC and condensation
- Purchased heater baseline: LF Bros `5 kW / 12V / 10 L Split Pro`, with external metering pump/filter, exhaust/muffler, combustion intake, T4S hardwired controller, wireless remote, harness, mounting hardware, and the supplied plastic tank now reassigned to graywater. The purchased diesel reservoir/feed package is the EVIL ENERGY `10 gal` aluminum tank in BOM row `65`; its final remote `2 in` filler, `5/16 in` vent, and isolation purchases are BOM rows `364-366`. The floor interface is the purchased CaLeQi stainless `60 mm / 2.37 in` turret in BOM row `362`, nominally `200 x 180 mm` with a `125 mm` circular skirt. Detailed fit/cut owner: [INTERIOR_driver_side_workstation](../implementation/INTERIOR_driver_side_workstation.md#diesel-heater-integration-gate).
- Heater install posture (`2026-08-30` owner report): the heater location is above/adjacent to the truck fuel-tank envelope and the contemplated exhaust route is nearby. The `60 mm` skirt is not inherently too long: over the permanent `3/4 in` plywood plus Lonseal and truck-bed metal it should project roughly `1.5 in` below a rib-high bed plane, and still about `0.9-1.1 in` below the underside across a plausible `1.25-1.5 in` total corrugated-floor depth. That projection is useful for clearing the combustible floor and reaching the connection cavity, but the exact location remains physical-clearance gated. Do not release that layout from heat shield alone. Preserve at least `10 cm / 4 in` at the rear cabin-air inlet and an unrestricted warm-air outlet; dry-fit the LF Bros studs and supplied gasket to the delivered turret; measure the actual skirt and weld before cutting; and physically survey the full underside for the truck fuel tank, fuel/EVAP/brake lines, wiring, undercoating, structural members, plastics, skirt projection, pipe sweeps, and service reach. The turret top plate sits on the finished-floor plane with the skirt downward through one measured opening; do not stack the original flat mounting plate. Keep every combustion/exhaust/fuel connection outside the occupied envelope and serviceable after the rear driver-side storage module is installed.
- Turret-cut prep (`2026-09-02` owner report): the Lonseal waste circle is scored/peeled, a thin sacrificial top plywood layer came away with it, and the physical turret sits correctly in the resulting shallow recess. Use the existing rigid `1/2 in` template as the jigsaw riser, but set the wood blade from its actual maximum downstroke so roughly `1/8-3/16 in` of plywood remains over the bed; shim or shorten the blade if needed. Remove the adjacent `12V` battery and isolate its terminals, loosen obstructing extrusion so the tool stays flat, cut plywood first, remove the disk/EPS and reinspect, then cut the aluminum separately with the short metal blade.
- Outside routing baseline: exhaust and muffler stay completely outside, fall slightly for condensate, use broad sweeps rather than a hard `90-degree` turn, and remain separated/shielded from vehicle fuel systems, wiring, plastic, undercoating, body openings, and the combustion intake. Heat shield is supplemental to real clearance, noncombustible standoffs/guards, and a route that cannot contact or heat the truck fuel tank. Intake and exhaust must not terminate in the same direction or where exhaust can be recirculated.
- Purchased fuel-feed topology (`2026-08-30`): use one lower tank outlet as `-10AN male -> -10AN female / 1/8 NPT male adapter -> 1/8 NPT stainless shutoff -> 1/8 FNPT / 3/16 in barb -> short cut section of the supplied thick black LF Bros connector hose -> original 5 mm OD / 2 mm ID rigid line -> filter -> external metering pump -> heater`. The rubber section is a short transition sleeve, not the long fuel run. Use diesel-rated sealant only on tapered NPT joints per product instructions; AN joints seal at the flare seat, so inspect those seats and put no tape/sealant on AN threads. Mount the pump in rubber isolation, outlet toward the heater and upward about `45 degrees`, within `2 m`; keep line and service joints protected from heat, abrasion, and road debris.
- Purchased fill/vent topology (`2026-09-02`): replace the stock 12-bolt cap plate with Speedway `91676553`, then route its `2 in` neck through the purchased fuel-rated straight/45-degree hose sections and beaded aluminum straight/90-degree joiners to the Boltigen angled bed-wall deck fill. Preserve continuous fall into the tank, independently support the long route, and keep hose away from heat, abrasion, tire/axle travel, and frame pinch points. Leave the unused lower outlet capped; cap one upper port with the freed lower cap and use the other as `-10AN female / 5/16 in barb -> KINTLE 5/16 in hose -> remote rollover valve`. The earlier separate valve/hose from row `65` are superseded install stock. Mount the final valve upright above normal fuel level and terminate it outside under the bed, away from ignition and body openings. Verify the delivered cap/port count and leak/vent-test a small outdoor fill before service.
- Fuel-storage posture (`2026-09-02` owner concept): exterior mounting in the former spare-tire area is selected. The drafted cradle uses `1010` plus on-hand gusseted `2 x 2 in` aluminum angle, with vertical `1010` members using through-bolting and threaded ends plus regular T-nut `90s` as redundant joints; purchased `1/8 x 1 in` neoprene isolates the aluminum tank. Treat through-bolted/threaded-end structure as the primary retention and T-nut corners as secondary bracing. Before cradle fabrication or truck attachment drilling, identify sound attachment points on the spare-tire crossmember/frame area, prove load paths and hardware access without drilling blind into boxed structure or vehicle lines, retain positive vertical/lateral capture if a T-nut loosens, and verify clearance at full axle/tire travel. The approximately `86 lb` full tank, filler, vent, shutoff, filter/pump, and rear module must pass one coupled dry fit before cradle drilling or fueling; this does not independently hold the separately cleared heater-turret cut.
- Diesel level monitoring: the tank listing states a passive `3-90 ohm` sender. Bench-meter both endpoints and confirm empty/full direction on receipt, then wire its two leads to one unused native Cerbo GX MK2 `Tank` `DATA/GND` pair with no external `12V`; configure `Diesel`, `10 US gal`, and a custom approximately `3 ohm empty / 90 ohm full` range only after the meter check.
- Electrical/control baseline: the harness branches to heater, pump, T4S controller, and `12V +/-`; the pump is ECU-controlled and the wireless remote needs no wire or cut. Feed from fused `12V C-22`, never `48V`, and preserve power throughout controller-commanded cooldown. Measure the final route before accepting the planned short-run `14 AWG / 15A` branch; use `12 AWG` if length or startup-voltage testing demands it.
- Ventilation: Maxxair fan included in current camper config
- Lighting split: Hiatus factory overhead LED+dimmer remains separate from the planned ambient/cabinet LED subsystem. Desired future interior-lighting design is `12V` QuinLED/WLED analog PWM control on the dedicated lighting branch, with upper CCT white wash, lower RGBCCT night/entry strip, and hardwired momentary buttons; install/procurement is deferred.
- Condensation controls and climate envelope limits: TBD

## Safety
- Purpose: define a practical, build-ready safety baseline for the current architecture (`48V 15.36kWh` house bank, `12V` distribution, `120VAC` shore/inverter path, diesel cabin heat, and the selected exterior propane HOTTAP hot-water package).
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
- Battery positive path stays: battery -> Class T fuse near source -> main disconnect -> Lynx bus; all active load/charge branches are protected by their Lynx fused outputs, including Orion input `F-05` in Slot 4.
- Battery negative path stays: battery -> SmartShunt -> Lynx negative bus (all returns on load side of shunt).
- Use only voltage-appropriate overcurrent devices on house DC branches (`58V`/`80V` class on `48V` paths); do not substitute `32V` automotive-only fuses on `48V` circuits.
- Route the Orion input directly from Lynx Slot 4 through the existing `6 AWG` pair after `F-05` (`40A` MEGA, body-marked at least `58VDC`); standalone `F-06` is retired and no second input holder is installed.
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
- Do not open `SW-12V-BATT` as the normal way to stop charging. First turn off the fan/lights or other active loads, disable the Orion, confirm it reports off/not charging, and only then open the battery switch. Opening the battery switch while the Orion is enabled removes the battery but can leave the shared fuse-panel bus and loads powered from the Orion.
- Replace the Orion's always-on L-H jumper with a maintained SPST dry-contact switch between the remote `L` and `H` pins for routine local control; the official Victron sequence connects the destination battery before enabling the remote. Startup order is `SW-12V-BATT` closed first, Orion remote on second.
- In this baseline, the 12V fuse block is the shared junction device (`main +` stud combine point plus integrated negative bus return point).
- Do not solder-splice high-current 12V source conductors; use crimped lugs on rated stud terminals.
- Maintain branch-level fuse-to-conductor coordination per `docs/implementation/ELECTRICAL_fuse_schedule.md`.
- Keep always-on detector branch (`12V-05`) protected but never switch-controlled.
- Keep ambient/cabinet strip lighting on the dedicated DC branch (`12V-11`) so low-light use does not require inverter operation. Desired future path is `12V` QuinLED/WLED analog PWM control, not the superseded `24V` converter/MiBoxer worksheet; verify final fuse/conductor sizing once selected strip wattage and expansion channels are known.
- No additional `48V->12V` converter is planned: the Orion plus `12V` buffer battery is the active architecture. If measured sustained `12V` demand later exceeds Orion headroom, engineer a new expansion line then rather than carrying inactive BOM row `118` as current procurement.

### 120VAC shore/inverter safety
- Main hazards: shock from miswired neutral/ground, ground-fault exposure at outlets, and overcurrent heating from undersized branch protection.
- Required controls:
- Keep shore path order: shore source/adapters -> portable EMS/surge protection -> shore cord -> shore inlet (`L5-30`) -> combined AC DIN enclosure (`30A` UL489 AC-in breaker/disconnect) -> MultiPlus AC-in.
- Keep AC-out path order: MultiPlus AC-out-1 -> `10/3` feeder -> combined AC DIN enclosure (`30A` AC-out main + `20A`/`20A` branch breakers) -> first GFCI -> one `LOAD`-protected downstream duplex on each branch. Current device count is four duplex receptacles total: two driver-side and two passenger-side.
- Keep AC-in hardware on a `30A` / `10 AWG` basis, but set the MultiPlus input limit to the source-specific permitted draw whenever adapters are used: `10A` for first household tests and `12A` maximum policy on a normal `15A` outlet; use the accepted source rating/policy for `20A` or `30A` service.
- Keep AC-out-2 as reserve-only in Phase 1 (labeled capped route; no energized branch hardware yet).
- Preserve continuous equipment grounding and chassis bond through all AC paths.
- Do not add a fixed downstream neutral-ground bond in branch wiring; neutral/ground behavior must follow MultiPlus transfer/bonding design.
- Commissioning checks:
1. AC-in-only charger validation with AC-out loads disconnected for first battery charge.
2. Inspect and document all four listed device boxes, covers, clamps, conductor fill, and accessibility.
3. Prove first-device `LINE/LOAD`, downstream protection, receptacle polarity, and continuous PE at all eight plug positions.
4. Trip/reset each GFCI and confirm its downstream duplex loses/restores power under inverter and shore modes.
5. Verify AC-out-2 remains de-energized as a reserve-only capped route in Phase 1.

### Propane safety (rear-box cylinder plus exterior Joolca HOTTAP V2)
- Main hazards: LP leakage or accumulation in the rear box, ignition near electrical equipment, CO exposure, road damage, and operating an outdoor-only appliance inside an enclosed box or living space.
- Cylinder/box controls:
- Keep the purchased Flame King `YSN10LB-ALM` upright and secured in the ventilated rear box with the valve accessible.
- Use the Safoner hatch as the propane-hose pass-through through the rear box.
- The rear-box LP path is `cylinder -> CALPOSE gauge -> supplied QCC1 regulator/hose -> HOTTAP`.
- HOTTAP operating/travel controls:
- Mount the purchased Quick-Release HOTTAP Bracket directly to proven structural backing on the exterior box side, use the purchased HOTTAP V2 Mount Cover for travel/dust protection, and prove the manual clearances in the installed operating position.
- Never fire the HOTTAP inside the propane box, camper, or any other enclosed space. Operate it only on its exterior mount with the cover clear and exhaust/combustion zone unobstructed.
- Connect the BLUE cold-out and RED hot-return hoses only while parked; disconnect, drain, cap, and stow them before travel. Preserve full freeze drainage of the heater, supplied hoses, exterior stubs, and service trunks.
- Leak-test every disturbed LP connection before operation and define recurring post-service/pre-trip test cadence. Do not use a flame for leak checking.
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
