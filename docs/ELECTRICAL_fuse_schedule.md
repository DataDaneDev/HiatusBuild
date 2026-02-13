# Electrical Fuse Schedule (Implementation - Lynx Topology)

As-of date: `2026-02-12`

Purpose: define each required fuse by circuit, protected conductor/device, holder/housing method, physical placement, and linked wire gauge assumptions for the approved Phase 1 Lynx architecture.

Related docs:
- Canonical electrical/system baseline: `docs/SYSTEMS.md`
- Implementation topology and conductor map: `docs/ELECTRICAL_overview_diagram.md`
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
- Battery bank assumption: `2x 48V 100Ah` batteries in parallel (`2` separate battery-positive conductors leaving batteries).
- Branch devices on Lynx:
1. MultiPlus-II `48/3000`
2. SmartSolar `150/45`
3. Sterling `BB1248120` output
4. Orion-Tr `48/12-30` input
- SmartShunt control/power lead note: retain the Victron-supplied fused positive sense/power lead assembly (small-current harness), and avoid substituting lower-voltage automotive fuse components on the `48V` system.
- Sterling rating basis used for this revision: `BB1248120` output ceiling about `1500W` (`~26A` at `57.6V`), with `150A` input fuse and `40A` output fuse guidance.

## Manufacturer References Used
- Victron MultiPlus-II `120V` installation page (recommends `125A` DC fuse for `48/3000`; cable table includes `AWG 1` to `AWG 2/0` by length): `https://www.victronenergy.com/media/pg/MultiPlus-II_120V/en/installation.html`
- Victron SmartSolar MPPT `150/45` installation/spec pages (`50A-63A` battery fuse range, terminal limit `16 mm2`/`AWG 6`): `https://www.victronenergy.com/media/pg/Manual_SmartSolar_MPPT_150-35__150-45/en/installation.html` and `https://www.victronenergy.com/media/pg/Manual_SmartSolar_MPPT_150-35__150-45/en/technical-specifications.html`
- Victron Orion-Tr Smart (isolated) installation page (`48V` side fuse `20A`; `12V` side fuse `60A`; cable table): `https://www.victronenergy.com/media/pg/Orion-Tr_Smart_DC-DC_Charger_(isolated)/en/installation.html`
- Victron Lynx Distributor manual (MEGA fuse carrier format): `https://www.victronenergy.com/media/pg/Lynx_Distributor/en/installation.html`
- Victron fuse datasheet (for `48V` systems use `58V`-class fuses): `https://www.victronenergy.com/upload/documents/Datasheet-Fuses-EN.pdf`
- Sterling BB12V->48V charger references (model list includes `BB1248120`, fuse/cable guidance): `https://sterling-power.com/products/battery-to-battery-chargers-12v-to-48v`
- Blue Sea Systems guidance (fuse close to source): `https://www.bluesea.com/resources/1437`

## Required Fuse Map (Start-to-Finish, With Housing)
| Fuse ID | Circuit (source -> load) | Protected wire/device | Fuse type and voltage class | Amperage | Holder or housing method | Physical location | Planned conductor gauge |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `F-01A` | Battery A `+` -> bank positive combine/disconnect input | Battery A positive cable leaving battery | Class T (`>=125VDC`) | `225A` | Blue Sea Class T fuse block (covered stud mount) | Battery compartment, within ~`7"` of Battery A positive post | `2/0 AWG` |
| `F-01B` | Battery B `+` -> bank positive combine/disconnect input | Battery B positive cable leaving battery | Class T (`>=125VDC`) | `225A` | Blue Sea Class T fuse block (covered stud mount) | Battery compartment, within ~`7"` of Battery B positive post | `2/0 AWG` |
| `F-02` | Lynx Slot 1 -> MultiPlus `DC+` | Main inverter positive feeder | `MEGA`, `58V` or `80V` | `125A` | Integrated Lynx Distributor fuse slot | Lynx Distributor, Slot 1 | `2/0 AWG` planned (`AWG 1` minimum on short run) |
| `F-03` | Lynx Slot 2 -> SmartSolar `BAT+` | MPPT battery-side positive feeder | `MEGA`, `58V` or `80V` | `60A` | Integrated Lynx Distributor fuse slot | Lynx Distributor, Slot 2 | `6 AWG` |
| `F-04` | Lynx Slot 3 -> Sterling `BB1248120` output `+` | Sterling output feeder to house `48V` bus | `MEGA`, `58V` or `80V` | `40A` | Integrated Lynx Distributor fuse slot | Lynx Distributor, Slot 3 | `6 AWG` planned (`10 AWG` minimum per Sterling table) |
| `F-05` | Lynx Slot 4 -> `48V` auxiliary feeder (Orion branch) | Aux feeder from Lynx to Orion-branch fuse point | `MEGA`, `58V` or `80V` | `40A` | Integrated Lynx Distributor fuse slot | Lynx Distributor, Slot 4 | `6 AWG` |
| `F-06` | `48V` aux feeder -> Orion `48V` input `+` | Orion input lead (device protection) | Inline MIDI/AMI/ANL family rated `>=58VDC` | `20A` target (`23A` if using Victron MIDI family) | Sealed inline fuse holder mounted on backplate | Electrical cabinet, mounted at source end of Orion input lead | `6 AWG` planned (`8 AWG` minimum per Orion cable table) |
| `F-07` | Orion `12V` output `+` -> `12V` fuse panel feed | Main `12V` feeder from Orion | Inline MIDI/AMI/ANL family rated `>=32VDC` | `60A` | Sealed inline fuse holder mounted on backplate | Electrical cabinet, within ~`7"` of Orion `12V` output stud | `6 AWG` planned (`8 AWG` minimum per Orion cable table) |
| `F-08` | Starter battery `+` -> Sterling `BB1248120` input `+` | Vehicle-side charger input cable | MEGA/ANL equivalent rated `>=32VDC` | `150A` | Sealed engine-bay fuse holder with high-temp cover | Engine bay, within ~`7"` of starter battery positive post | `2/0 AWG` planned (`2 AWG` minimum per Sterling table) |
| `F-09A/B/C` | PV string `+` leads -> MPPT PV combiner | Each solar string positive conductor and reverse-current path | `gPV` string fuse (`>=150VDC`) | `15A` each (provisional) | `10x38` touch-safe PV fuse holders in weatherproof combiner enclosure | Roof-entry combiner near gland/pass-through | `10 AWG` PV wire |
| `F-10` | `12V` fuse panel branch circuits -> each `12V` load | Individual `12V` branch conductors and load circuits | ATO/ATC blade fuses (`32V` class) | Per-circuit | Integrated sockets in Blue Sea `5026/5032` style fuse block | `12V` fuse panel in electrical cabinet | Per branch (table below) |
| `OEM-SHUNT` | Lynx positive tap -> SmartShunt positive sense/power lead | SmartShunt electronics lead | Victron OEM inline low-current fuse (factory harness) | OEM value (small-current harness fuse) | Integrated inline holder in supplied harness | Electrical cabinet near Lynx positive tap | OEM harness lead |

## 12V Branch Fuse + Gauge Assignments (Initial Build)
| Circuit | Planned load | Fuse | Planned wire gauge | Notes |
| --- | --- | --- | --- | --- |
| `12V-01` | Starlink DC power supply | `10A` | `14 AWG duplex` | Remote-work load path |
| `12V-02` | Fridge (`35-50qt`) | `15A` | `14 AWG duplex` | Move to `12 AWG` if one-way run exceeds ~`15 ft` |
| `12V-03` | Diesel heater electrical | `15A` | `14 AWG duplex` | Startup surge expected |
| `12V-04` | Water pump | `10A` | `14 AWG duplex` | Intermittent duty |
| `12V-05` | CO + propane detector | `3A` | `18/2` | Always-on safety load |
| `12V-06` | LED strips | `5A` | `18/2` | Lighting branch |
| `12V-07` | Cerbo GX power feed (assumed via `12V` panel) | `3A` | `18/2` | Assumption until final harness lock |
| `12V-08` | Spare branch 1 | `15A` placeholder | `14 AWG duplex` | Reserve |
| `12V-09` | Spare branch 2 | `15A` placeholder | `14 AWG duplex` | Reserve |

## Holder Ecosystem Standard (Procurement Guidance)
| Fuse family | Preferred holder style | Why |
| --- | --- | --- |
| Class T | Covered stud-mounted marine block | High interrupt capacity and robust battery-compartment mounting |
| MEGA (`58V/80V`) in Lynx | Lynx integrated holders only | Eliminates separate branch fuse block and keeps topology locked |
| Inline `48V` Orion input (`F-06`) | Sealed MIDI/AMI-compatible holder on interior backplate | Keeps source-end protection near branch takeoff |
| Inline `12V` Orion output (`F-07`) | Sealed MIDI/AMI-compatible holder at Orion output | Protects full panel feeder length |
| Engine-bay Sterling input (`F-08`) | Sealed MEGA/ANL holder, high-temp/engine-bay suitable | Environmental robustness and source-proximate protection |
| PV string fuses (`F-09`) | DIN-rail `10x38` gPV holders in weatherproof combiner | Proper PV-voltage insulation and serviceable string isolation |
| 12V branches (`F-10`) | Integrated blade sockets in marine fuse block | Fast field service and clear branch labeling |
| SmartShunt positive lead (factory harness) | Keep Victron-supplied inline fused lead assembly | Preserves vendor-qualified low-current protection path for shunt electronics |

## Spare Fuse Inventory
| Fuse type | Installed qty | Spare qty to carry | Notes |
| --- | --- | --- | --- |
| Class T `225A` | `2` | `2` | One spare per installed battery fuse |
| `MEGA 125A` (`58V/80V`) | `1` | `2` | MultiPlus branch |
| `MEGA 60A` (`58V/80V`) | `1` | `2` | MPPT branch |
| `MEGA 40A` (`58V/80V`) | `2` | `3` | Sterling + Orion feeder branches |
| Orion input fuse (`20A` target / `23A` MIDI) | `1` | `2` | Match installed holder family |
| Orion output fuse `60A` (`32V+`) | `1` | `2` | Main `12V` feeder protection |
| Sterling input fuse `150A` (`32V+`) | `1` | `1` | Vehicle-side charger input |
| PV string fuse `15A gPV` | `3` | `3` | One spare per string |
| SmartShunt OEM harness fuse | `1` | `1` | Keep OEM-equivalent spare if the fuse is field-replaceable on final harness |
| ATO/ATC branch fuses | variable | `2` each used value | Keep mixed kit onboard |

## BOM Row Mapping
| Fuse scope | BOM row(s) |
| --- | --- |
| Main battery Class T protection (`F-01A/F-01B`) + Class T spares | `bom/bom_estimated_items.csv` row `7` |
| Lynx branch MEGA fuses installed (`F-02` to `F-05`) | `bom/bom_estimated_items.csv` row `10` |
| Inline Orion/Sterling installed fuse hardware (`F-06`, `F-07`, `F-08`) | `bom/bom_estimated_items.csv` row `11` |
| 12V branch panel and blade fuses (`F-10`) | `bom/bom_estimated_items.csv` row `16` |
| SmartShunt OEM fused lead (`OEM-SHUNT`) | `bom/bom_estimated_items.csv` row `23` (included with SmartShunt kit) |
| High-current spare fuse kit (MEGA/MIDI/150A) | `bom/bom_estimated_items.csv` row `105` |
| PV string fuses + holder (`F-09A/B/C`) and spares | `bom/bom_estimated_items.csv` row `106` |

## Assumptions and Open Items
1. Wire sizing above assumes copper conductors, enclosed vehicle routing, and one-way run lengths generally `<=10 ft` for branch circuits unless noted.
2. `F-09A/B/C` remains provisional at `15A` pending final solar module datasheet max-series-fuse confirmation.
3. Final SKU lock is still required for inline holders used by `F-06`, `F-07`, and `F-08`.
4. If Orion run lengths exceed the short/medium assumption, keep `F-06`/`F-07` and upsize conductors before energizing.
5. Do not use `32V` automotive MEGA fuses on `48V` house circuits; use `58V`/`80V` DC-rated fuses only.
6. Keep the SmartShunt fused lead as an OEM harness item unless an equivalent voltage-rated replacement is fully validated.
