# Electrical Fuse Schedule (Implementation - Lynx Topology)

As-of date: `2026-02-24`

Purpose: define each required fuse by circuit, protected conductor/device, holder/housing method, physical placement, and linked wire gauge assumptions for the approved Phase 1 Lynx architecture with a battery-backed 12V bus.

Related docs:
- Canonical electrical/system baseline: `docs/SYSTEMS.md`
- Implementation topology and conductor map: `docs/ELECTRICAL_overview_diagram.md`
- Battery and trunk recalculation record: `docs/ELECTRICAL_battery_fuse_wire_recalc_2026-02-18.md`
- Decisions/open items tracker: `docs/TRACKING.md`
- BOM source of truth: `bom/bom_estimated_items.csv`

## Sweep Findings (2026-02-12)
| Finding ID | Finding | Impact | Resolution status |
| --- | --- | --- | --- |
| `FS-001` | `BB1248120` was modeled in planning docs as `120A` on the `48V` output. | Alternator-recovery math was materially overstated. | Corrected in `bom/bom_estimated_items.csv` row `18` and `docs/SYSTEMS.md` (`~1500W`, about `26A` at `57.6V`). |
| `FS-002` | Fuse schedule listed fuse values but not a complete housing/holder definition for every fuse family. | Install path and procurement freeze were ambiguous. | Resolved below with explicit holder/housing method and location per fuse ID. |
| `FS-003` | Fuse schedule did not tie each fuse to a conductor gauge plan. | Hard to verify "fuse protects conductor" rule at install time. | Resolved below with gauge mapping and assumptions. |

## Design Basis
- Topology: `Victron Lynx Distributor M10` (`LYN060102010`) with `4` fused `48V` branches.
- Battery bank assumption: `3x 48V 100Ah` batteries in parallel (`3` separate battery-positive conductors leaving batteries).
- 12V distribution assumption: 12V fuse block used as the shared junction device (main `+` stud = source combine, integrated negative bus/main `-` = return), fed by Orion-Tr Smart `48/12-30` charger and a `12V 100Ah LiFePO4` buffer battery branch.
- Parallel-bank safety rule: use one Class T fuse per battery-positive conductor leaving the battery. A single shared “bank fuse” does not protect the individual battery leads and does not prevent cross-feed faults between parallel batteries.
- Branch devices on Lynx:
1. MultiPlus-II `48/3000`
2. SmartSolar `150/45`
3. Sterling `BB1248120` output
4. Orion-Tr `48/12-30` input
- 12V buffer battery protection and switching baseline: `F-11` (`100A` class) on battery positive within ~`7"` of source, then `SW-12V-BATT` manual disconnect for service isolation.
- Phase 1 complexity lock: no automatic low-voltage disconnect (`LVD`) layer in this revision.
- SmartShunt control/power lead note: retain the Victron-supplied fused positive sense/power lead assembly (small-current harness), and avoid substituting lower-voltage automotive fuse components on the `48V` system.
- Sterling rating basis used for this revision: `BB1248120` output ceiling about `1500W` (`~26A` at `57.6V`), with `150A` input fuse and `40A` output fuse guidance.
- Inverter inrush-control baseline: use a manual pre-charge lead across the `48V` main disconnect studs during first energization with `F-02` installed; detailed procedure is in `docs/OPERATIONS.md` and procurement is tracked in BOM row `19`.

## Manufacturer References Used
- Victron MultiPlus-II `120V` installation page (recommends `125A` DC fuse for `48/3000`; cable table includes `AWG 1` to `AWG 2/0` by length): `https://www.victronenergy.com/media/pg/MultiPlus-II_120V/en/installation.html`
- Victron SmartSolar MPPT `150/45` installation/spec pages (`50A-63A` battery fuse range, terminal limit `16 mm2`/`AWG 6`): `https://www.victronenergy.com/media/pg/Manual_SmartSolar_MPPT_150-35__150-45/en/installation.html` and `https://www.victronenergy.com/media/pg/Manual_SmartSolar_MPPT_150-35__150-45/en/technical-specifications.html`
- Victron Orion-Tr Smart isolated DC-DC charger product page, manual, and datasheet (`48V` models require external input fuse per manual; `48/12-30` output rating and terminal limits per datasheet): `https://www.victronenergy.com/dc-dc-converters/orion-tr-dc-dc-converters-isolated`
- Victron Lynx Distributor manual (MEGA fuse carrier format): `https://www.victronenergy.com/media/pg/Lynx_Distributor/en/installation.html`
- Victron Orion-Tr Smart isolated DC-DC installation page (external input fuse guidance): `https://www.victronenergy.com/media/pg/Orion-Tr_Smart_DC-DC_Charger_-_Isolated/en/installation.html`
- Victron fuse datasheet (for `48V` systems use `58V`-class fuses): `https://www.victronenergy.com/upload/documents/Datasheet-Fuses-EN.pdf`
- Sterling BB12V->48V charger references (model list includes `BB1248120`, fuse/cable guidance): `https://sterling-power.com/products/battery-to-battery-chargers-12v-to-48v`
- Sterling BB12V->48V charger installation manual PDF (fuse/cable guidance): `https://sterling-power.com/cdn/shop/files/bb1230_1240_1260_12120_122430_241230_241240_241260_241280_242430_124810_1248120_241280_242430_b2b_installation_manual.pdf?v=1739450989`
- Blue Sea Systems guidance (fuse close to source): `https://www.bluesea.com/resources/1437`
- Blue Sea Class T holder-family compatibility (`110A-200A` vs `225A-400A`): `https://www.bluesea.com/support/articles/Fuse_Blocks/1438/Selecting_Class_T_Fuses`

## Battery Branch Re-Baseline (2026-02-18)
- This schedule now uses a gated battery-branch baseline of `200A Class T` per battery (`F-01A/B/C`) as a provisional default.
- Re-baseline method and calculations are documented in `docs/ELECTRICAL_battery_fuse_wire_recalc_2026-02-18.md`.
- Final lock gate for `F-01A/B/C`: capture a true `51.2V` battery datasheet/manual with validated current and terminal limits before permanent fuse lock.
- Holder-family constraint: battery branch values below `225A` require the `110A-200A` Class T holder family. Do not pair `<225A` fuse targets with `225A-400A` holder-only hardware.
- If validated battery or terminal limits are lower than current provisional assumptions, move `F-01A/B/C` to `175A` and update BOM row `7` accordingly.

## Required Fuse Map (Start-to-Finish, With Housing)
| Fuse ID | Circuit (source -> load) | Protected wire/device | Fuse type and voltage class | Amperage | Holder or housing method | Physical location | Planned conductor gauge |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `F-01A` | Battery A `+` -> bank positive combine/disconnect input | Battery A positive cable leaving battery | Class T (`>=125VDC`) | `200A` provisional | Blue Sea Class T fuse block (covered stud mount, `110A-200A` family) | Battery compartment, within ~`7"` of Battery A positive post | `2/0 AWG` |
| `F-01B` | Battery B `+` -> bank positive combine/disconnect input | Battery B positive cable leaving battery | Class T (`>=125VDC`) | `200A` provisional | Blue Sea Class T fuse block (covered stud mount, `110A-200A` family) | Battery compartment, within ~`7"` of Battery B positive post | `2/0 AWG` |
| `F-01C` | Battery C `+` -> bank positive combine/disconnect input | Battery C positive cable leaving battery | Class T (`>=125VDC`) | `200A` provisional | Blue Sea Class T fuse block (covered stud mount, `110A-200A` family) | Battery compartment, within ~`7"` of Battery C positive post | `2/0 AWG` |
| `F-02` | Lynx Slot 1 -> MultiPlus `DC+` | Main inverter positive feeder | `MEGA`, `58V` or `80V` | `125A` | Integrated Lynx Distributor fuse slot | Lynx Distributor, Slot 1 | `2/0 AWG` planned (`AWG 1` minimum on short run) |
| `F-03` | Lynx Slot 2 -> SmartSolar `BAT+` | MPPT battery-side positive feeder | `MEGA`, `58V` or `80V` | `60A` | Integrated Lynx Distributor fuse slot | Lynx Distributor, Slot 2 | `6 AWG` |
| `F-04` | Lynx Slot 3 -> Sterling `BB1248120` output `+` | Sterling output feeder to house `48V` bus | `MEGA`, `58V` or `80V` | `40A` | Integrated Lynx Distributor fuse slot | Lynx Distributor, Slot 3 | `6 AWG` planned (`10 AWG` minimum per Sterling table) |
| `F-05` | Lynx Slot 4 -> `48V` auxiliary feeder (Orion branch) | Aux feeder from Lynx to Orion-branch fuse point | `MEGA`, `58V` or `80V` | `40A` | Integrated Lynx Distributor fuse slot | Lynx Distributor, Slot 4 | `6 AWG` |
| `F-06` | `48V` aux feeder -> Orion `48V` input `+` | Orion input lead (device protection) | Inline MIDI family rated `>=58VDC` | `30A` (`58V` MIDI, lock) | Littelfuse `04980921GXM5` sealed inline MIDI holder on backplate | Electrical cabinet, mounted at source end of Orion input lead | `6 AWG` planned (`8 AWG` minimum per Orion cable table) |
| `F-07` | Orion `12V` output `+` -> 12V fuse block main `+` stud | Main `12V` feeder from Orion into shared source-combine point | `MEGA`, `58V` or `80V` | `60A` | Victron MEGA fuse holder (external, non-Lynx) | Electrical cabinet, within ~`7"` of Orion `12V` output stud | `6 AWG` planned (`8 AWG` minimum per Orion cable table) |
| `F-08` | Starter battery `+` -> Sterling `BB1248120` input `+` | Vehicle-side charger input cable | MEGA/ANL equivalent rated `>=32VDC` | `150A` | Sealed engine-bay fuse holder with high-temp cover | Engine bay, within ~`7"` of starter battery positive post | `2/0 AWG` planned (`2 AWG` minimum per Sterling table) |
| `F-09A/B/C` | PV string `+` leads -> MPPT PV combiner | Each solar string positive conductor and reverse-current path | `gPV` string fuse (`>=150VDC`) | `15A` each (provisional) | `10x38` touch-safe PV fuse holders in weatherproof combiner enclosure | Roof-entry combiner near gland/pass-through | `10 AWG` PV wire |
| `F-10` | `12V` fuse block branch circuits -> each `12V` load | Individual `12V` branch conductors and load circuits | ATO/ATC blade fuses (`32V` class) | Per-circuit | Integrated sockets in generic marine `12V` fuse block | `12V` fuse block in electrical cabinet | Per branch (table below) |
| `F-11` | 12V buffer battery `+` -> 12V fuse block main `+` stud via `SW-12V-BATT` | Buffer battery source cable and downstream junction fault exposure | Inline MIDI/AMI/ANL family rated `>=32VDC` | `100A` class baseline | Sealed inline holder mounted close to battery positive | Within ~`7"` of 12V buffer battery positive post | `4 AWG` planned |
| `OEM-SHUNT` | Lynx positive tap -> SmartShunt positive sense/power lead | SmartShunt electronics lead | Victron OEM inline low-current fuse (factory harness) | OEM value (small-current harness fuse) | Integrated inline holder in supplied harness | Electrical cabinet near Lynx positive tap | OEM harness lead |

Notes:
- Victron Orion fuse table is keyed by side voltage (`input or output`). For `48/12-30`: `F-06` tracks the `48V` input side (project lock now `30A` `58V` MIDI based on available holder/fuse family), and `F-07` tracks the `12V` output side (`60A`).

## 12V Buffer Battery Switching Requirement
- `SW-12V-BATT` is a manual service disconnect in the 12V buffer battery positive path, installed downstream of `F-11`.
- Operational default:
1. `SW-12V-BATT` closed (`NORMAL`) for battery-backed shared-junction operation.
2. `SW-12V-BATT` open (`SERVICE`) for battery isolation or Orion-only validation mode.
- Service-path note: the Orion `12V` output remains connected to the fuse-block main `+` stud through `F-07` even when `SW-12V-BATT` is open.
- Maintenance-path note: when `SW-12V-BATT` is closed, Orion output can maintain/charge the buffer battery through the shared fuse-block main `+` stud path.
- Do not solder-splice high-current source conductors; use crimped lugs on rated studs/junction hardware.
- Keep always-on safety branch (`12V-05`) unswitched at branch level; isolation is handled at source path controls.

## 12V Branch Fuse + Gauge Assignments (Initial Build)
| Circuit | Planned load | Fuse | Planned wire gauge | Notes |
| --- | --- | --- | --- | --- |
| `12V-01` | Starlink DC power supply | `10A` | `14 AWG duplex` | Remote-work load path |
| `12V-02` | Fridge (`35-50qt`) | `15A` | `14 AWG duplex` | Current estimate pass flags this as a voltage-drop warning at `~12 ft`; hold `<=8 ft` or move to `12 AWG` |
| `12V-03` | Diesel heater electrical | `15A` | `14 AWG duplex` | Startup surge expected; estimate pass flags tight margin at `~8 ft` |
| `12V-04` | Water pump | `10A` | `14 AWG duplex` | Intermittent duty |
| `12V-05` | CO + propane detector | `3A` | `18/2` | Always-on safety load |
| `12V-06` | LED lights + dimmer (Hiatus pre-installed) | `5A` | `18/2` | Hiatus pre-installed branch; estimate pass flags voltage-drop warning at `~8 ft`; shorten run/load or upsize |
| `12V-07` | Cerbo GX power feed (assumed via `12V` panel) | `3A` | `18/2` | Assumption until final harness lock |
| `12V-08` | USB PD station branch (office zone) | `20A` | `12 AWG duplex` | Keep `<=5 ft` (estimate-pass assumption) or upsize |
| `12V-09` | USB PD station branch (galley zone) | `15A` | `14 AWG duplex` | Current estimate pass assumes `~8 ft` and `~8A` expected load; move to `12 AWG` if sustained current rises |
| `12V-10` | Maxxair fan (Hiatus pre-installed) | `10A` | `14 AWG duplex` | Hiatus pre-installed roof fan branch; verify installed harness and branch labeling at audit |

## F-11 Validation (2026-02-22)
- Scope validated: `C-19A` (12V buffer battery positive path), including `F-11`, `SW-12V-BATT`, and planned `4 AWG` conductor.
- Documented branch-fuse envelope from `12V-01` through `12V-10`: `106A` theoretical simultaneous maximum (`10+15+15+10+3+5+3+20+15+10`).
- Modeled practical load envelope from `bom/load_model_wh.csv` is materially lower (`~300W` average, about `25A @ 12V`), but branch-level surge/transient overlap remains possible.
- Conductor check for `4 AWG`, `2.5 ft` one-way (`5 ft` loop) using this doc resistance basis (`0.0002485 ohm/ft`):
1. `50A` -> `0.062V` drop (`0.52% @ 12V`)
2. `80A` -> `0.099V` drop (`0.83% @ 12V`)
3. `100A` -> `0.124V` drop (`1.04% @ 12V`)
- Validation result: keep `F-11` at `100A` class for the current architecture. This preserves margin above the modeled `50A` design basis and near/at the branch-fuse aggregate envelope while staying aligned with the `4 AWG` short-run drop target.
- Hard lock conditions for this `100A` choice:
1. Buffer-battery positive path remains `4 AWG` and approximately `2.5 ft` one-way as documented.
2. `SW-12V-BATT` continuous DC rating is `>=100A` at the installed system voltage class.
3. The selected `12V 100Ah` battery/BMS continuous discharge rating is `>=100A`.
- Down-select gate: if final battery/BMS continuous rating is below `100A`, reduce `F-11` to the nearest compliant class (typically `80A`) and synchronize spare stock row `105`.

## Length-Validation Sync (2026-02-18)
- `docs/ELECTRICAL_overview_diagram.md` now carries one-way estimated lengths and voltage-drop screening for `C-01` through `C-36`.
- Lynx Orion-feeder branch fuse (`F-05`) is locked to `40A MEGA` for BOM sync in this pass.
- USB branch baseline is synchronized across docs/BOM: office branch `12 AWG` (`C-34`), galley branch `14 AWG` (`C-35`).

## Holder Ecosystem Standard (Procurement Guidance)
| Fuse family | Preferred holder style | Why |
| --- | --- | --- |
| Class T (`F-01A/B/C`) | Covered stud-mounted marine block (`110A-200A` family for current baseline) | High interrupt capacity and robust battery-compartment mounting; holder family must match chosen Class T range |
| MEGA (`58V/80V`) in Lynx (`F-02` to `F-05`) | Lynx integrated holders only | Eliminates separate branch fuse block and keeps topology locked |
| Inline `48V` Orion input (`F-06`) | Littelfuse `04980921GXM5` sealed inline MIDI holder on interior backplate | Keeps source-end protection near branch takeoff with confirmed `58V` holder availability |
| Orion output (`F-07`) `60A MEGA` | Victron external MEGA holder at Orion output | Standardizes `60A` spare pool with MPPT fuse family |
| 12V buffer battery main (`F-11`) | Sealed MIDI/AMI/ANL holder near battery | Protects shared 12V source-junction path from battery fault current |
| 12V battery disconnect (`SW-12V-BATT`) | Sealed rotary DC switch near distribution cabinet access | Provides simple service isolation without adding LVD complexity |
| Engine-bay Sterling input (`F-08`) | Sealed MEGA/ANL holder, high-temp/engine-bay suitable | Environmental robustness and source-proximate protection |
| PV string fuses (`F-09`) | DIN-rail `10x38` gPV holders in weatherproof combiner | Proper PV-voltage insulation and serviceable string isolation |
| 12V branches (`F-10`) | Integrated blade sockets in marine fuse block | Fast field service and clear branch labeling |
| SmartShunt positive lead (factory harness) | Keep Victron-supplied inline fused lead assembly | Preserves vendor-qualified low-current protection path for shunt electronics |

## Spare Fuse Inventory
| Fuse type | Installed qty | Spare qty to carry | Notes |
| --- | --- | --- | --- |
| Class T `200A` (provisional installed) | `3` | `3` | One spare per installed battery fuse while `200A` baseline is active |
| Class T `175A` (alternate pending final battery datasheet lock) | `0` | `3` optional | Optional non-regret alternate set if budget allows; install only if final lock gate requires lower value |
| `MEGA 125A` (`58V/80V`) | `1` | `4` | MultiPlus branch; BOM lock is `x5` total |
| `MEGA 60A` (`58V/80V`) | `2` | `4` | Shared pool for MPPT (`F-03`) + Orion output (`F-07`); target `6` total |
| `MEGA 40A` (`58V/80V`) | `2` | `4` | Shared Sterling (`F-04`) + Orion feeder (`F-05`) family; BOM lock is `x6` total |
| Orion input fuse (`30A` MIDI, `58V`) | `1` | `3` | BOM row `133` lock is `x4` total (`1` installed + `3` spares) |
| 12V buffer battery main fuse (`100A` class) | `1` | `3` | Spare pack basis is BOM row `105` (BOJACK `100A` ANL `3`-count) |
| Sterling input fuse `150A` (`32V+`) | `1` | `1` | Vehicle-side charger input |
| PV string fuse `15A gPV` | `3` | `3` | One spare per string |
| SmartShunt OEM harness fuse | `1` | `1` | Keep OEM-equivalent spare if the fuse is field-replaceable on final harness |
| ATO/ATC branch fuses | variable | `2` each used value | Keep mixed kit onboard |

## BOM Row Mapping
| Fuse scope | BOM row(s) |
| --- | --- |
| Main battery Class T protection (`F-01A/F-01B/F-01C`) + Class T spares | `bom/bom_estimated_items.csv` row `7` |
| Lynx branch MEGA fuses (`F-02` to `F-05`) installed + spare set | `bom/bom_estimated_items.csv` row `10` |
| Orion/Sterling installed fuse-holder hardware (`F-06`, `F-07`, `F-08`) | `bom/bom_estimated_items.csv` row `11` |
| Orion input fuses (`F-06`) | `bom/bom_estimated_items.csv` row `133` |
| 12V buffer battery (`B12`) | `bom/bom_estimated_items.csv` row `21` |
| 12V buffer battery main fuse + holder (`F-11`) | `bom/bom_estimated_items.csv` row `125` |
| 12V battery disconnect (`SW-12V-BATT`) | `bom/bom_estimated_items.csv` row `124` |
| 12V branch panel and blade fuses (`F-10`) | `bom/bom_estimated_items.csv` row `16` |
| SmartShunt OEM fused lead (`OEM-SHUNT`) | `bom/bom_estimated_items.csv` row `23` (included with SmartShunt kit) |
| High-current spare fuse kit (non-Lynx spares, if retained) | `bom/bom_estimated_items.csv` row `105` |
| PV string fuses + holder (`F-09A/B/C`) and spares | `bom/bom_estimated_items.csv` row `106` |

Related non-fuse accessory for energization safety:
- Inverter pre-charge lead accessory (`100-150 ohm` resistor lead used across main disconnect studs): `bom/bom_estimated_items.csv` row `19`.

## Lynx MEGA Procurement Lock (BOM Sync)
- Updated row `10` fuse-family lock: `125A x5`, `60A x6` (shared `F-03` + `F-07` pool), `40A x6` (shared `F-04` + `F-05` pool).
- Updated row `10` estimate should be kept synchronized with the final `40A x6` cart quantity.

## Assumptions and Open Items
1. Wire sizing above assumes copper conductors, enclosed vehicle routing, and the one-way run-length estimate set in `docs/ELECTRICAL_overview_diagram.md` (`2026-02-18` pass).
2. `F-09A/B/C` remains provisional at `15A` pending final solar module datasheet max-series-fuse confirmation.
3. Final SKU lock is still required for inline holders used by `F-08` and `F-11`, plus the external Victron MEGA holder for `F-07` and `SW-12V-BATT`.
4. If Orion run lengths exceed the short/medium assumption, keep `F-06`/`F-07` and upsize conductors before energizing.
5. Do not use `32V` automotive MEGA fuses on `48V` house circuits; use `58V`/`80V` DC-rated fuses only.
6. Keep the SmartShunt fused lead as an OEM harness item unless an equivalent voltage-rated replacement is fully validated.
7. `SW-12V-BATT` is manual-only in Phase 1; no automatic LVD behavior is assumed in this schedule.
8. Battery listing data (`<=200A` current limit) is currently treated as provisional because the provided screenshot includes `14.6V/14.2V` values that are not a `51.2V` profile; final lock requires validated `51.2V` battery documentation.
9. If final battery current or terminal limits are lower than current assumptions, down-select `F-01A/B/C` to `175A` and keep fuse-to-conductor coordination synchronized with `docs/ELECTRICAL_overview_diagram.md` and `bom/bom_estimated_items.csv`.
10. Orion fuse selection is side-voltage based per Victron table (`input or output`), not just converter model number. Keep `F-06` and `F-07` aligned to `48V` input / `12V` output sides.
11. Final lock for `F-11` requires explicit 12V buffer battery/BMS continuous discharge-current confirmation; if `<100A`, down-select `F-11` and `SW-12V-BATT`/holder family accordingly.
