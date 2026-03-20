# Electrical Fuse Schedule (Implementation - Lynx Topology)

As-of date: `2026-03-20`

Purpose: define each required fuse by circuit, protected conductor/device, holder/housing method, physical placement, and linked wire-gauge assumptions for the approved Phase 1 Lynx architecture with a battery-backed 12V bus and dedicated 48V secondary alternator branch.

Related docs:
- Canonical electrical/system baseline: `docs/core/SYSTEMS.md`
- Implementation topology and conductor map: `docs/implementation/ELECTRICAL_overview_diagram.md`
- Decisions/open items tracker: `docs/core/TRACKING.md`
- BOM source of truth: `bom/bom_estimated_items.csv`

## Design Basis
- Topology: `Victron Lynx Distributor M10` (`LYN060102010`) with `4` fused `48V` branches.
- Battery bank assumption: `3x 48V 100Ah` batteries in parallel (`3` separate battery-positive conductors leaving batteries).
- 12V distribution assumption: 12V fuse block used as the shared junction device (main `+` stud = source combine, integrated negative bus/main `-` = return), fed by Orion-Tr Smart `48/12-30` charger and a `12V 100Ah LiFePO4` buffer battery branch.
- Parallel-bank safety rule: use one Class T fuse per battery-positive conductor leaving the battery.
- Branch devices on Lynx:
1. MultiPlus-II `48/3000`
2. SmartSolar `150/45`
3. Dedicated `48V` secondary alternator branch (Mechman/WS500 path)
4. Orion-Tr `48/12-30` input
- Alternator migration lock for this pass:
1. `F-04` is re-baselined to `150A` MEGA (`58V/80V`) in Lynx Slot 3.
2. Legacy Sterling engine-bay input fuse path (`F-08`) is retired from active architecture.
3. WS500 support fuses are included as explicit install items (`F-12/F-13/F-14`).
4. Ford `Upfitter Switch #3` is locked as the manual `WS500` enable source through `F-15`.

## Alternator Branch Fuse + Wire Finalization (`2026-03-19`)
Assumptions for this pass:
1. One-way alternator run length: `20 ft`.
2. Dedicated positive and dedicated negative runs (loop length `40 ft`).
3. Charging target voltage basis: `58.4V`.
4. Voltage-drop planning target: about `<=2%` under expected charging current.

Resistance and drop screen (`V_drop = I * (2 * L * R_per_ft)`):

| Gauge | `150A` drop | `%` @ `58.4V` | `200A` drop | `%` @ `58.4V` | Decision note |
| --- | ---:| ---:| ---:| ---:| --- |
| `4 AWG` | `1.49V` | `2.55%` | `1.99V` | `3.40%` | Reject for this run length/current class |
| `2 AWG` | `0.94V` | `1.61%` | `1.25V` | `2.14%` | Acceptable for `~150A` class |
| `1/0 AWG` | `0.59V` | `1.01%` | `0.79V` | `1.35%` | Strong margin |
| `2/0 AWG` | `0.47V` | `0.80%` | `0.62V` | `1.07%` | Best margin; inventory already on hand |

Lock for this build pass:
- Keep the planned alternator branch fuse at `150A` (`F-04`, Lynx Slot 3).
- Reuse existing uncut `2/0` inventory for alternator `+` and dedicated negative run.
- Row `173` contingency purchase is removed from scope unless field measurement proves an actual shortfall.

## Required Fuse Map (Start-to-Finish, With Housing)
| Fuse ID | Circuit (source -> load) | Protected wire/device | Fuse type and voltage class | Amperage | Holder or housing method | Physical location | Planned conductor gauge |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `F-01A` | Battery A `+` -> bank positive combine/disconnect input | Battery A positive cable leaving battery | Class T (`>=125VDC`) | `200A` provisional | Blue Sea Class T fuse block (covered stud mount, `110A-200A` family) | Battery compartment, within ~`7"` of Battery A positive post | `2/0 AWG` |
| `F-01B` | Battery B `+` -> bank positive combine/disconnect input | Battery B positive cable leaving battery | Class T (`>=125VDC`) | `200A` provisional | Blue Sea Class T fuse block (covered stud mount, `110A-200A` family) | Battery compartment, within ~`7"` of Battery B positive post | `2/0 AWG` |
| `F-01C` | Battery C `+` -> bank positive combine/disconnect input | Battery C positive cable leaving battery | Class T (`>=125VDC`) | `200A` provisional | Blue Sea Class T fuse block (covered stud mount, `110A-200A` family) | Battery compartment, within ~`7"` of Battery C positive post | `2/0 AWG` |
| `F-02` | Lynx Slot 1 -> MultiPlus `DC+` | Main inverter positive feeder | `MEGA`, `58V` or `80V` | `125A` | Integrated Lynx Distributor fuse slot | Lynx Distributor, Slot 1 | `2/0 AWG` planned (`AWG 1` minimum on short run) |
| `F-03` | Lynx Slot 2 -> SmartSolar `BAT+` | MPPT battery-side positive feeder | `MEGA`, `58V` or `80V` | `60A` | Integrated Lynx Distributor fuse slot | Lynx Distributor, Slot 2 | `6 AWG` |
| `F-04` | Lynx Slot 3 -> `48V` alternator branch input (`ALT+`) | Alternator-to-house positive charge cable | `MEGA`, `58V` or `80V` | `150A` | Integrated Lynx Distributor fuse slot | Lynx Distributor, Slot 3 | `2/0 AWG` (reuse lock) |
| `F-05` | Lynx Slot 4 -> `48V` auxiliary feeder (Orion branch) | Aux feeder from Lynx to Orion-branch fuse point | `MEGA`, `58V` or `80V` | `40A` | Integrated Lynx Distributor fuse slot | Lynx Distributor, Slot 4 | `6 AWG` |
| `F-06` | `48V` aux feeder -> Orion `48V` input `+` | Orion input lead (device protection) | Inline MIDI family rated `>=58VDC` | `30A` (`58V` MIDI, lock) | Littelfuse `04980921GXM5` sealed inline MIDI holder on backplate | Electrical cabinet, mounted at source end of Orion input lead | `6 AWG` planned (`8 AWG` minimum per Orion cable table) |
| `F-07` | Orion `12V` output `+` -> 12V fuse block main `+` stud | Main `12V` feeder from Orion into shared source-combine point | `MEGA`, `58V` or `80V` | `60A` | Victron MEGA fuse holder (external, non-Lynx) | Electrical cabinet, within ~`7"` of Orion `12V` output stud | `6 AWG` planned (`8 AWG` minimum per Orion cable table) |
| `F-09A/B/C` | PV string `+` leads -> MPPT PV combiner | Each solar string positive conductor and reverse-current path | `gPV` string fuse (`>=150VDC`) | `15A` each (provisional) | `10x38` touch-safe PV fuse holders in weatherproof combiner enclosure | Roof-entry combiner near gland/pass-through | `10 AWG` PV wire |
| `F-10` | `12V` fuse block branch circuits -> each `12V` load | Individual `12V` branch conductors and load circuits | ATO/ATC blade fuses (`32V` class) | Per-circuit | Integrated sockets in marine `12V` fuse block | `12V` fuse block in electrical cabinet | Per branch |
| `F-11` | 12V buffer battery `+` -> 12V fuse block main `+` stud via `SW-12V-BATT` | Buffer battery source cable and downstream junction fault exposure | Inline MIDI/AMI/ANL family rated `>=32VDC` | `100A` class baseline | Sealed inline holder mounted close to battery positive | Within ~`7"` of 12V buffer battery positive post | `4 AWG` planned |
| `F-12` | WS500 regulator power lead | WS500 power feed lead | Inline ATC/ATO (`32V` class acceptable on 12V-origin lead) | `10A` baseline (`15A` allowed if required by alternator case) | Sealed inline holder (WS500 kit) | Near source end of WS500 power lead | Harness lead |
| `F-13` | WS500 battery positive sense lead | WS500 battery sense lead | Inline ATC/ATO | `3A` | Sealed inline holder (WS500 kit) | Near battery-positive sense takeoff | Harness lead |
| `F-14` | WS500 current-sense lead protection (when required by selected shunt layout) | WS500 current-sense wiring | Inline ATC/ATO | `5A` | Sealed inline holder (WS500 kit) | Near shunt/sense tap per WS500 guidance | Harness lead |
| `F-15` | Ford Upfitter `#3` -> WS500 brown ignition/enable wire | Low-current regulator enable/control wire | Inline ATC/ATO (`32V` class, local wire protection) | `3A` | Sealed inline holder near the Ford upfitter blunt-cut source / splice handoff | Engine bay or control-wire handoff point before small-gauge run to WS500 | `16 AWG` TXL/GXL |
| `OEM-SHUNT` | Lynx positive tap -> SmartShunt positive sense/power lead | SmartShunt electronics lead | Victron OEM inline low-current fuse (factory harness) | OEM value | Integrated inline holder in supplied harness | Electrical cabinet near Lynx positive tap | OEM harness lead |

## Retired Fuse IDs (Migration Cleanup)
| Retired ID | Previous path | Current status |
| --- | --- | --- |
| `F-08` | Starter battery `+` -> Sterling `BB1248120` input `+` (`150A` engine-bay fuse) | Retired with Sterling alternator-charge path. Hardware can remain as surplus/12V stock only. |

## Spare Fuse Inventory (Updated)
| Fuse type | Installed qty | Spare qty to carry | Notes |
| --- | --- | --- | --- |
| Class T `200A` (provisional installed) | `3` | `3` | One spare per installed battery fuse while `200A` baseline is active |
| `MEGA 150A` (`58V/80V`) | `1` | `2` | Alternator branch (`F-04`) installed + spare set (row `170`) |
| `MEGA 125A` (`58V/80V`) | `1` | `4` | MultiPlus branch |
| `MEGA 60A` (`58V/80V`) | `2` | `4` | Shared pool for MPPT (`F-03`) + Orion output (`F-07`) |
| `MEGA 40A` (`58V/80V`) | `1` | `3` | Orion feeder (`F-05`) plus spare set |
| Orion input fuse (`30A` MIDI, `58V`) | `1` | `3` | BOM row `133` lock is `x4` total (`1` installed + `3` spares) |
| 12V buffer battery main fuse (`100A` class) | `1` | `3` | Spare pack basis is BOM row `105` |
| WS500 low-current fuses | `3` active positions | `2` each used value | Carry `10A`, `15A`, `5A`, and `3A` spares |
| WS500 ignition/enable fuse (`F-15`) | `1` active position | `2` | Carry spare `3A` mini/ATO fuse and one spare sealed holder if using a potted inline kit |
| PV string fuse `15A gPV` | `3` | `3` | One spare per string |
| SmartShunt OEM harness fuse | `1` | `1` | Keep OEM-equivalent spare if field-replaceable |
| ATO/ATC branch fuses | variable | `2` each used value | Keep mixed kit onboard |

## BOM Row Mapping
| Fuse scope | BOM row(s) |
| --- | --- |
| Main battery Class T protection (`F-01A/F-01B/F-01C`) + Class T spares | `bom/bom_estimated_items.csv` row `7` |
| Lynx branch MEGA fuses (`F-02` to `F-05`) installed + spare set | `bom/bom_estimated_items.csv` rows `10` and `170` |
| Orion installed fuse-holder hardware (`F-06`, `F-07`) | `bom/bom_estimated_items.csv` row `11` |
| Orion input fuses (`F-06`) | `bom/bom_estimated_items.csv` row `133` |
| WS500 low-current fuse/holder kit (`F-12`, `F-13`, `F-14`) | `bom/bom_estimated_items.csv` row `171` |
| WS500 Upfitter `#3` enable/control path (`F-15`) | `bom/bom_estimated_items.csv` row `176` |
| 12V buffer battery (`B12`) | `bom/bom_estimated_items.csv` row `21` |
| 12V buffer battery main fuse + holder (`F-11`) | `bom/bom_estimated_items.csv` row `125` |
| 12V battery disconnect (`SW-12V-BATT`) | `bom/bom_estimated_items.csv` row `124` |
| 12V branch panel and blade fuses (`F-10`) | `bom/bom_estimated_items.csv` row `16` |
| SmartShunt OEM fused lead (`OEM-SHUNT`) | `bom/bom_estimated_items.csv` row `23` (included with SmartShunt kit) |
| PV string fuses + holder (`F-09A/B/C`) and spares | `bom/bom_estimated_items.csv` row `106` |

## Assumptions and Open Items
1. Wire sizing above assumes copper conductors and enclosed vehicle routing.
2. `F-09A/B/C` remains provisional at `15A` pending final solar module datasheet max-series-fuse confirmation.
3. Confirm Mechman kit content/polarity (`PH`/`NH`) before physically returning Sterling hardware.
4. `SW-12V-BATT` remains manual-only in Phase 1; no automatic LVD behavior is assumed.
5. Final lock for `F-11` still requires explicit 12V buffer battery/BMS continuous discharge-current confirmation.
6. `F-15` exists to protect the smaller-gauge control wire between Ford `Upfitter #3` and the WS500 brown ignition/enable wire; the factory `25A` upfitter circuit protection is not the final wire-protection device for that branch.
