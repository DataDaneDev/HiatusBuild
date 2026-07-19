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
  - "[[ELECTRICAL_Mechman_WS500_APM48_install_guide]]"
  - "[[OPERATIONS]]"
  - "[[CAMPER_audio_system]]"
---

# Electrical Fuse Schedule (Implementation - Lynx Topology)

As-of date: `2026-07-19`

Purpose: define each required fuse by circuit, protected conductor/device, holder/housing method, physical placement, and linked wire-gauge assumptions for the approved Phase 1 Lynx architecture with a battery-backed 12V bus and dedicated 48V secondary alternator branch.

Related docs:
- Canonical electrical/system baseline: `docs/core/SYSTEMS.md`
- Implementation topology and conductor map: `docs/implementation/ELECTRICAL_overview_diagram.md`
- Decisions/open items tracker: `docs/core/TRACKING.md`
- BOM source of truth: `bom/bom_estimated_items.csv`

## Design Basis
- Topology: `Victron Lynx Distributor M10` (`LYN060102010`) with `3` active fused `48V` branches and Lynx Slot 4 open/spare.
- Battery bank assumption: `3x 48V 100Ah` batteries in parallel (`3` separate battery-positive conductors leaving batteries).
- 12V distribution assumption: 12V fuse block used as the shared junction device (main `+` stud = source combine, integrated negative bus/main `-` = return), fed by Orion-Tr Smart `48/12-30` charger and a `12V 100Ah LiFePO4` buffer battery branch.
- Parallel-bank safety rule: use one Class T fuse per battery-positive conductor leaving the battery.
- Active branch devices on Lynx:
1. MultiPlus-II `48/3000`
2. SmartSolar `150/45`
3. Dedicated `48V` secondary alternator branch (Mechman/WS500 path)
4. Slot 4 / `F-05` open spare — Orion-Tr `48/12-30` input is **not** a Lynx fused branch; it uses standalone source-side `F-06` from a Lynx `48V+` bus tap.
- Current shop identification note: do not infer the purpose of the physically X-marked/misrated Lynx fuse from the X alone. Identify its slot. Slot 2 requires `F-03 60A/80V` MEGA for the MPPT; Slot 4 remains empty. No `32V`-rated fuse is acceptable on an energized `48V` branch.
- Alternator path lock for this pass:
1. `F-04` is locked to `150A` MEGA (`58V/80V`) in Lynx Slot 3 at the house-bank/Lynx end of the alternator positive run.
2. Obsolete pre-Mechman charger/fuse paths are removed from active architecture and primary layout planning.
3. Confirmed `PH-VAN` harness uses one short red/black pair as combined regulator power and voltage sense at the house/main bus. Treat former separate `F-12` regulator-power and `F-13` positive-sense functions as one fused `PH-VAN` red lead for this install; current Wakespeed VAN diagram shows `15A` at that lead. Current-sense high/low remains an unfused twisted sense pair per Wakespeed manual.
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
| `F-03` | Lynx Slot 2 -> SmartSolar `BAT+` | MPPT battery-side positive feeder | `MEGA`, `80V` Victron replacement stock | `60A` | Integrated Lynx Distributor fuse slot | Lynx Distributor, Slot 2 | `6 AWG` |
| `F-04` | Lynx Slot 3 -> `48V` alternator branch input (`ALT+`) | Alternator-to-house positive charge cable | `MEGA`, `58V` or `80V` | `150A` | Integrated Lynx Distributor fuse slot | Lynx Distributor, Slot 3 | `2/0 AWG` (reuse lock) |
| `F-05` | Lynx Slot 4 | Open spare fused position; no Orion connection in active topology | N/A | Not installed | Leave blank/open for now; legacy `40A` MEGA stock remains spare-only and is not Orion protection | Lynx Distributor, Slot 4 | N/A |
| `F-06` | Lynx `48V +` bus tap -> inline fuse -> Orion `48V` input `+` | Orion `48V` input/device lead; this is the one source-side Orion input fuse | **Interim/current:** existing `30A 58V` MIDI on the short `6 AWG` Orion input run. **Final cleanup stock purchased 2026-06-01:** `3x` Mouser `576-166.7000.5202` / Littelfuse `166.7000.5202` FKS/ATO blade fuses (`20A`, `80VDC`) plus `3x` Mouser `576-178.6150.0001` / Littelfuse `178.6150.0001` ATO/FKS holders (`80VDC` per owner-confirmed listing). | Interim `30A`; final `20A` per Victron Orion `48V` external battery-protection recommendation | Interim MIDI holder now acceptable for build/bench use; final FKS/ATO stock purchased in BOM row `182`. Keep the unfused source-side tap from Lynx to `F-06` physically short and protected. | Electrical cabinet between Lynx `+` bus tap and Orion input | `6 AWG` planned; pigtail/transition acceptable if the final blade holder does not directly accept `6 AWG` |
| `F-07` | Orion `12V` output `+` -> 12V fuse block main `+` stud | Main `12V` feeder from Orion into shared source-combine point | `MEGA`, `80V` Victron replacement stock | `60A` | Victron MEGA fuse holder (external, non-Lynx) | Electrical cabinet, within ~`7"` of Orion `12V` output stud | `6 AWG` planned (`8 AWG` minimum per Orion cable table) |
| `F-09A/B/C` | PV string `+` leads -> MPPT PV combiner | Each solar string positive conductor and reverse-current path | `gPV` string fuse (`>=150VDC`) | `15A` each (provisional) | `10x38` touch-safe PV fuse holders in weatherproof combiner enclosure | Roof-entry combiner near gland/pass-through | `10 AWG` PV wire |
| `F-10` | `12V` fuse block branch circuits -> each `12V` load | Individual `12V` branch conductors and load circuits | ATO/ATC blade fuses (`32V` class) | Per-circuit | Integrated sockets in marine `12V` fuse block | `12V` fuse block in electrical cabinet | Per branch |
| `AUDIO-HU` / `12V-12` | `12V` fuse block -> Kicker `46KMC2` media center/source unit | KMC2 source/head-unit branch conductor and device harness | ATO/ATC branch fuse (`32V` class) plus KMC2 harness `15A ATM` fuse | `15A` | Integrated `12V` fuse block branch plus OEM KMC2 harness fuse | Electrical cabinet to driver-side DC shelf/source face | `12 AWG duplex` if kept around `5 ft`; `10 AWG` if route grows toward `8 ft+` |
| `AUDIO-SUB` | 12V source/main `+` stud -> external fuse -> Kicker `49PTRTP10` powered sub `+` | Powered-sub positive branch and subwoofer input; manual-required external protection | Inline/MRBF/AFS/ANL-class fuse matched to selected `4 AWG` kit (`32V`+ DC class acceptable on 12V branch) | `40A` | Holder within about `18 in` of 12V source takeoff; if using Kicker `47KMPK4`, fit the PTRTP10-required `40A` fuse rather than the kit generic larger fuse | Near `12V` source/junction, downstream of `SW-12V-BATT` | `4 AWG` positive with matching `4 AWG` return to 12V negative bus/main stud |
| `F-11` | 12V buffer battery `+` -> 12V fuse block main `+` stud via `SW-12V-BATT` | Buffer battery source cable and downstream junction fault exposure | Inline MIDI/AMI/ANL family rated `>=32VDC` | `100A` class baseline | Sealed inline holder mounted close to battery positive | Within ~`7"` of 12V buffer battery positive post | `4 AWG` planned |
| `F-12/F-13-PHVAN` | `PH-VAN` WS500 red lead at house/main positive bus | Combined WS500 regulator power and positive voltage-sense lead | Inline fuse/holder rated for actual `48V` bank maximum; current Wakespeed VAN/internal-BMS diagram shows this fused at `15A` | `15A` unless Wakespeed/Mechman profile guidance overrides | Sealed inline holder close to the house/main positive bus takeoff feeding the short `PH-VAN` red lead | Electrical panel near WS500/main bus; do not extend the short VAN red/black pair | Harness lead |
| `CERBO-PWR` | `48V` system positive -> Cerbo GX power `+` | Cerbo GX low-current electronics feed | Inline fuse/holder rated for `48V` bank maximum voltage | `1A-3A` | Small inline holder close to the positive takeoff | Electrical cabinet, preferably system/load side of main disconnect so Cerbo powers down with the house system during bench shutdown | `18 AWG` red/black duplex acceptable |
| `F-15` | Ford Upfitter `#3` -> WS500 brown ignition/enable wire | Low-current regulator enable/control wire | Inline ATC/ATO (`32V` class acceptable; 12V control circuit) | `3A` | Sealed inline holder near the Ford upfitter blunt-cut source / splice handoff | Engine bay or control-wire handoff point before small-gauge run to WS500 | `16 AWG` TXL/GXL |
| `OEM-SHUNT` | Battery-side positive or Lynx/system positive tap -> SmartShunt `Vbatt+` terminal | SmartShunt electronics supply/sense lead | External Victron-supplied red cable with inline low-current fuse; not an internal SmartShunt fuse | OEM value | Inline holder in supplied red cable | Prefer battery-side positive if SOC continuity is desired while the main disconnect is open; system side is acceptable if zero parasitic draw during disconnect-off storage matters more | OEM harness lead |

## Retired Fuse IDs
Obsolete pre-Mechman charger/fuse paths are removed from the active schedule. Do not reserve board space or labels for them.

## Spare Fuse Inventory (Updated)
| Fuse type | Installed qty | Spare qty to carry | Notes |
| --- | --- | --- | --- |
| Class T `200A` (provisional installed) | `3` | `1` on hand | Owner confirmed `3` holders and `4` slow-blow Class T fuses total (`3` installed + `1` spare); add more only if the one-spare-per-installed policy is later desired |
| `MEGA 150A` (`58V/80V`) | `1` | `2` | Alternator branch (`F-04`) installed + spare set (row `170`) |
| `MEGA 125A` (`58V/80V`) | `1` | `4` | MultiPlus branch |
| `MEGA 60A` (`80V`) | `2` | `3` | Victron 5-pack row `188`: install MPPT (`F-03`) + Orion output (`F-07`), keep 3 spares. Earlier 6x low-cost 60A MEGA batch was owner-confirmed misadvertised/not actually 58V and is quarantined/trash, not 48V install stock. |
| `MEGA 40A` (`58V/80V`) | `0` active | `3` | Legacy spare stock only; do not use as Orion device protection |
| Orion `48V` input protection | Interim installed/available: existing `30A 58V` MIDI. Final cleanup stock purchased: `3x` Mouser `576-166.7000.5202` `20A 80VDC` FKS/ATO fuses + `3x` `576-178.6150.0001` `80VDC` holders | Install `1x` final fuse/holder and carry `2` spare final `20A` FKS/ATO fuses + holders | Interim `30A` protects the short `6 AWG` run; final `20A` matches the Orion manual and is the preferred cleanup hardware |
| 12V buffer battery main fuse (`100A` class) | `1` | `3` | Spare pack basis is BOM row `105` |
| WS500 `PH-VAN` combined regulator power / positive-sense fuse (`F-12/F-13-PHVAN`) | `1` active position | `2` | Carry `15A` spares with holder/fuse voltage rating verified for the `48V` bank maximum |
| Cerbo GX power fuse (`CERBO-PWR`) | `1` active position | `1` | Carry a spare `1A-3A` fuse/holder rated for the `48V` bank maximum |
| WS500 ignition/enable fuse (`F-15`) | `1` active position | `2` | Carry spare `3A` mini/ATO fuse and one spare sealed holder; 12V control circuit |
| PV string fuse `15A gPV` | `3` | `3` | One spare per string |
| SmartShunt OEM harness fuse | `1` | `1` | Keep OEM-equivalent spare if field-replaceable |
| ATO/ATC branch fuses | variable | `2` each used value | Keep mixed kit onboard |
| Camper audio KMC2 branch (`AUDIO-HU`) | `1` active `15A` branch plus KMC2 harness `15A ATM` | `2` spare `15A` blade/ATM fuses | Preserve both source-side conductor protection and the KMC2 harness fuse |
| Camper audio powered sub (`AUDIO-SUB`) | `1` active `40A` external fuse | `1-2` spare `40A` fuses matching the selected holder family | PTRTP10 manual calls for `40A` external fuse and `4 AWG` power/ground |

## BOM Row Mapping
| Fuse scope | BOM row(s) |
| --- | --- |
| Main battery Class T protection (`F-01A/F-01B/F-01C`) + Class T spares | `bom/bom_estimated_items.csv` row `7` |
| Lynx branch MEGA fuses (`F-02` to `F-04` installed; Slot 4/`F-05` open) + spare set | `bom/bom_estimated_items.csv` rows `10`, `170`, and `188` |
| Orion installed fuse-holder hardware (`F-06`, `F-07`) | `bom/bom_estimated_items.csv` row `11` |
| Orion input fuses (`F-06` active; `F-05` not used in active topology) | `bom/bom_estimated_items.csv` rows `11`, `133`, and `182` |
| WS500 low-current fuse/holder kit (`F-12/F-13-PHVAN`) | `bom/bom_estimated_items.csv` row `171` |
| Cerbo GX power feed (`CERBO-PWR`) | `bom/bom_estimated_items.csv` row `22`; small inline fuse/holder may come from low-current install stock |
| WS500 Upfitter `#3` enable/control path (`F-15`) | `bom/bom_estimated_items.csv` row `176` |
| 12V buffer battery (`B12`) | `bom/bom_estimated_items.csv` row `21` |
| 12V buffer battery main fuse + holder (`F-11`) | `bom/bom_estimated_items.csv` row `125` |
| 12V battery disconnect (`SW-12V-BATT`) | `bom/bom_estimated_items.csv` row `124` |
| 12V branch panel and blade fuses (`F-10`) | `bom/bom_estimated_items.csv` row `16` |
| Camper audio source/head-unit branch (`AUDIO-HU` / `12V-12`) | `bom/bom_estimated_items.csv` rows `189`, `192`, and `193` |
| Camper audio powered-sub branch (`AUDIO-SUB`) | `bom/bom_estimated_items.csv` rows `191` and `192` |
| SmartShunt external OEM fused red lead (`OEM-SHUNT`) | `bom/bom_estimated_items.csv` row `23` (included with SmartShunt kit) |
| PV string fuses + holder (`F-09A/B/C`) and spares | `bom/bom_estimated_items.csv` row `106` |

## Assumptions and Open Items
1. Wire sizing above assumes copper conductors and enclosed vehicle routing.
2. `F-09A/B/C` and the old `3S3P` fuse count are modeling placeholders only; final PV fusing waits until solar modules/stringing are selected after shore and alternator charging are working.
3. Confirm WS500 `PH-VAN` harness fuse-holder voltage rating before final install; current build default is one `15A` fused red lead at the house/main positive bus for combined regulator power and positive voltage sense.
4. `SW-12V-BATT` remains manual-only in Phase 1; no automatic LVD behavior is assumed.
5. Final lock for `F-11` still requires explicit 12V buffer battery/BMS continuous discharge-current confirmation.
6. `F-15` exists to protect the smaller-gauge control wire between Ford `Upfitter #3` and the WS500 brown ignition/enable wire; the factory `25A` upfitter circuit protection is not the final wire-protection device for that branch.
7. Orion `F-05/F-06` lock: the active topology uses `F-06` as the single source-side Orion input fuse from a Lynx `48V+` bus tap. Lynx Slot 4/`F-05` stays open/blank because practical `20A` Lynx/MEGA protection is not available; the existing `40A` Lynx stock is spare-only and must not be installed as Orion device protection. Do not stack a Lynx MEGA fuse plus `F-06` inline fuse for the Orion branch unless the topology is deliberately reopened.
8. Camper audio `12V` load: KMC2 source branch and PTRTP10 powered-sub branch are downstream 12V loads, not new 48V branches. The PTRTP10 `40A` branch can exceed Orion `30A` continuous output during heavy bass; rely on the 12V buffer battery for transients and validate sustained loud-use behavior before assuming all 12V loads can run at max simultaneously.
