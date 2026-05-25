---
aliases:
  - Fuse schedule
tags:
  - hiatus/implementation
  - hiatus/electrical
status: active
related:
  - "[[ELECTRICAL_48V_ARCHITECTURE]]"
  - "[[ELECTRICAL_overview_diagram]]"
  - "[[OPERATIONS]]"
---

# Electrical Fuse Schedule (Implementation - Lynx Topology)

As-of date: `2026-05-22`

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
- Alternator path lock for this pass:
1. `F-04` is locked to `150A` MEGA (`58V/80V`) in Lynx Slot 3 at the house-bank/Lynx end of the alternator positive run.
2. Obsolete pre-Mechman charger/fuse paths are removed from active architecture and primary layout planning.
3. WS500 required fused leads are `F-12` regulator power and `F-13` positive voltage sense; current-sense high/low is an unfused twisted sense pair per current Wakespeed manual.
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
| `F-05` | Lynx Slot 4 -> Orion `48V` input branch | Retired/unused in the recommended standalone Orion input-fuse topology | `MEGA`, `58V` or `80V` | No final install value: `20A` Lynx-compatible MEGA has not been confirmed available; do not use `40A` as the Orion device fuse | Leave Lynx Slot 4 unused unless a true `20A` Lynx-compatible `>58.4VDC` fuse is sourced | Lynx Distributor, Slot 4 | N/A |
| `F-06` | Lynx `48V +` bus tap -> Orion `48V` input `+` | Orion `48V` input/device lead; standalone source-side fuse used because Lynx Slot 4 cannot currently provide a confirmed `20A` device fuse | Eaton Bussmann `PV-20A10F` 10x38 `gPV` fuse (`20A`, `1000VDC`, `50kAIC`) in Eaton Bussmann `CHPV1U`/`CHPV1IU` holder (`30A`, `1000VDC`) or direct equivalent | `20A` per Victron Orion `48V` external battery-protection recommendation | Touch-safe DIN/fuse holder mounted in the electrical cabinet near the source end of the Orion input branch; not a cheap 32V/58V automotive blade or Renogy ANL part | Electrical cabinet between Lynx `+` bus and Orion input | `6 AWG` planned; Victron table only requires `2.5-6mm²` depending run length, so `6 AWG` is conservative if the holder accepts it or pigtails transition cleanly |
| `F-07` | Orion `12V` output `+` -> 12V fuse block main `+` stud | Main `12V` feeder from Orion into shared source-combine point | `MEGA`, `58V` or `80V` | `60A` | Victron MEGA fuse holder (external, non-Lynx) | Electrical cabinet, within ~`7"` of Orion `12V` output stud | `6 AWG` planned (`8 AWG` minimum per Orion cable table) |
| `F-09A/B/C` | PV string `+` leads -> MPPT PV combiner | Each solar string positive conductor and reverse-current path | `gPV` string fuse (`>=150VDC`) | `15A` each (provisional) | `10x38` touch-safe PV fuse holders in weatherproof combiner enclosure | Roof-entry combiner near gland/pass-through | `10 AWG` PV wire |
| `F-10` | `12V` fuse block branch circuits -> each `12V` load | Individual `12V` branch conductors and load circuits | ATO/ATC blade fuses (`32V` class) | Per-circuit | Integrated sockets in marine `12V` fuse block | `12V` fuse block in electrical cabinet | Per branch |
| `F-11` | 12V buffer battery `+` -> 12V fuse block main `+` stud via `SW-12V-BATT` | Buffer battery source cable and downstream junction fault exposure | Inline MIDI/AMI/ANL family rated `>=32VDC` | `100A` class baseline | Sealed inline holder mounted close to battery positive | Within ~`7"` of 12V buffer battery positive post | `4 AWG` planned |
| `F-12` | WS500 regulator power lead | WS500 power feed lead | Inline fuse/holder rated for the actual source voltage; current Wakespeed manual recommends sealed ATC, but this build treats the lead as `48V`-referenced unless final harness docs prove otherwise | `10A` baseline (`15A` if required by extra-large alternator case) | Sealed inline holder per WS500 kit/manual, with verified voltage rating | Near source end of WS500 regulator power lead | Harness lead |
| `F-13` | WS500 positive voltage-sense lead | WS500 battery/charging voltage sense lead | Inline fuse/holder rated for actual `48V` bank maximum voltage unless WS500-supplied harness documentation proves otherwise | `3A` | Holder per WS500 manual/kit, voltage class verified before install | Near positive sense takeoff on charge side of the main alternator branch fuse / battery-bank connection | Harness lead |
| `F-15` | Ford Upfitter `#3` -> WS500 brown ignition/enable wire | Low-current regulator enable/control wire | Inline ATC/ATO (`32V` class acceptable; 12V control circuit) | `3A` | Sealed inline holder near the Ford upfitter blunt-cut source / splice handoff | Engine bay or control-wire handoff point before small-gauge run to WS500 | `16 AWG` TXL/GXL |
| `OEM-SHUNT` | Lynx positive tap -> SmartShunt `Vbatt+` terminal | SmartShunt electronics supply/sense lead | External Victron-supplied red cable with inline low-current fuse; not an internal SmartShunt fuse | OEM value | Inline holder in supplied red cable | Electrical cabinet near Lynx positive tap / SmartShunt | OEM harness lead |

## Retired Fuse IDs
Obsolete pre-Mechman charger/fuse paths are removed from the active schedule. Do not reserve board space or labels for them.

## Spare Fuse Inventory (Updated)
| Fuse type | Installed qty | Spare qty to carry | Notes |
| --- | --- | --- | --- |
| Class T `200A` (provisional installed) | `3` | `1` on hand | Owner confirmed `3` holders and `4` slow-blow Class T fuses total (`3` installed + `1` spare); add more only if the one-spare-per-installed policy is later desired |
| `MEGA 150A` (`58V/80V`) | `1` | `2` | Alternator branch (`F-04`) installed + spare set (row `170`) |
| `MEGA 125A` (`58V/80V`) | `1` | `4` | MultiPlus branch |
| `MEGA 60A` (`58V/80V`) | `2` | `4` | Shared pool for MPPT (`F-03`) + Orion output (`F-07`) |
| `MEGA 40A` (`58V/80V`) | `0` active | `3` | Legacy spare stock only; do not use as Orion device protection |
| Orion `48V` input protection | `1` total source-side fuse: standalone `F-06` with Eaton Bussmann `PV-20A10F` unless a true Lynx-compatible `20A` `>58.4VDC` MEGA option is later sourced | `2` of the final value | Do not stack `40A` Lynx + inline `30A`; purchased `30A` MIDI stock is obsolete for final `F-06` |
| 12V buffer battery main fuse (`100A` class) | `1` | `3` | Spare pack basis is BOM row `105` |
| WS500 regulator power fuse (`F-12`) | `1` active position | `2` | Carry `10A` and `15A` spares with holder/fuse voltage rating verified for the source voltage |
| WS500 positive voltage-sense fuse (`F-13`) | `1` active position | `2` | Carry `3A` spares with holder/fuse voltage rating verified for the `48V` bank maximum |
| WS500 ignition/enable fuse (`F-15`) | `1` active position | `2` | Carry spare `3A` mini/ATO fuse and one spare sealed holder; 12V control circuit |
| PV string fuse `15A gPV` | `3` | `3` | One spare per string |
| SmartShunt OEM harness fuse | `1` | `1` | Keep OEM-equivalent spare if field-replaceable |
| ATO/ATC branch fuses | variable | `2` each used value | Keep mixed kit onboard |

## BOM Row Mapping
| Fuse scope | BOM row(s) |
| --- | --- |
| Main battery Class T protection (`F-01A/F-01B/F-01C`) + Class T spares | `bom/bom_estimated_items.csv` row `7` |
| Lynx branch MEGA fuses (`F-02` to `F-05`) installed + spare set | `bom/bom_estimated_items.csv` rows `10` and `170` |
| Orion installed fuse-holder hardware (`F-06`, `F-07`) | `bom/bom_estimated_items.csv` row `11` |
| Orion input fuses (`F-05` preferred, `F-06` conditional only) | `bom/bom_estimated_items.csv` rows `10`, `11`, and `133` |
| WS500 low-current fuse/holder kit (`F-12`, `F-13`) | `bom/bom_estimated_items.csv` row `171` |
| WS500 Upfitter `#3` enable/control path (`F-15`) | `bom/bom_estimated_items.csv` row `176` |
| 12V buffer battery (`B12`) | `bom/bom_estimated_items.csv` row `21` |
| 12V buffer battery main fuse + holder (`F-11`) | `bom/bom_estimated_items.csv` row `125` |
| 12V battery disconnect (`SW-12V-BATT`) | `bom/bom_estimated_items.csv` row `124` |
| 12V branch panel and blade fuses (`F-10`) | `bom/bom_estimated_items.csv` row `16` |
| SmartShunt external OEM fused red lead (`OEM-SHUNT`) | `bom/bom_estimated_items.csv` row `23` (included with SmartShunt kit) |
| PV string fuses + holder (`F-09A/B/C`) and spares | `bom/bom_estimated_items.csv` row `106` |

## Assumptions and Open Items
1. Wire sizing above assumes copper conductors and enclosed vehicle routing.
2. `F-09A/B/C` and the old `3S3P` fuse count are modeling placeholders only; final PV fusing waits until solar modules/stringing are selected after shore and alternator charging are working.
3. Confirm Mechman kit content/polarity (`PH`/`NH`) and WS500 harness voltage ratings before final low-current fuse-holder purchase/install.
4. `SW-12V-BATT` remains manual-only in Phase 1; no automatic LVD behavior is assumed.
5. Final lock for `F-11` still requires explicit 12V buffer battery/BMS continuous discharge-current confirmation.
6. `F-15` exists to protect the smaller-gauge control wire between Ford `Upfitter #3` and the WS500 brown ignition/enable wire; the factory `25A` upfitter circuit protection is not the final wire-protection device for that branch.
7. Orion `F-05/F-06` reassessment: the desired final topology is one source-side Orion input fuse, not two adjacent fuses. Use Lynx Slot 4 alone if a correctly rated/value fuse can satisfy the Orion input-protection requirement. The existing `40A` Lynx stock is wire/branch protection for `6 AWG`, not final Orion device protection. Do not intentionally stack `40A` at Lynx plus `30A` inline as the final answer; use a correct-value source fuse or keep a correctly rated inline fuse only when Lynx cannot provide that value.
