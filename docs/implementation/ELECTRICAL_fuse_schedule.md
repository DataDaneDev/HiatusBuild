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

As-of date: `2026-08-12`

Purpose: define each required fuse by circuit, protected conductor/device, holder/housing method, physical placement, and linked wire-gauge assumptions for the approved Phase 1 Lynx architecture with a battery-backed 12V bus and dedicated 48V secondary alternator branch.

Related docs:
- Canonical electrical/system baseline: `docs/core/SYSTEMS.md`
- Implementation topology and conductor map: `docs/implementation/ELECTRICAL_overview_diagram.md`
- Decisions/open items tracker: `docs/core/TRACKING.md`
- BOM source of truth: `bom/bom_estimated_items.csv`

## Design Basis
- Topology: `Victron Lynx Distributor M10` (`LYN060102010`) with `4` active fused `48V` branches; Slot 4 feeds Orion input.
- Battery bank assumption: `3x 48V 100Ah` batteries in parallel (`3` separate battery-positive conductors leaving batteries).
- 12V distribution assumption: 12V fuse block used as the shared junction device (main `+` stud = source combine, integrated negative bus/main `-` = return), fed by Orion-Tr Smart `48/12-30` charger and a `12V 100Ah LiFePO4` buffer battery branch.
- Parallel-bank safety rule: use one Class T fuse per battery-positive conductor leaving the battery.
- Active branch devices on Lynx:
1. MultiPlus-II `48/3000`
2. SmartSolar `150/45`
3. Dedicated `48V` secondary alternator branch (Mechman/WS500 path)
4. Slot 4 / `F-05` — Orion-Tr `48/12-30` input through one `40A` MEGA body-marked at least `58VDC`; standalone `F-06` is retired.
- Current shop identification note: do not infer the purpose of the physically X-marked/misrated Lynx fuse from the X alone. Identify its slot. Slot 2 requires `F-03 60A/80V` MEGA for the MPPT; Slot 4 requires `F-05 40A` MEGA marked `>=58VDC` for Orion. No `32V`-rated fuse is acceptable on an energized `48V` branch.
- Alternator path lock for this pass:
1. `F-04` is locked to `200A/80V` MEGA in Lynx Slot 3 at the house-bank/Lynx end of the alternator positive run. Mechman's published `48V Elite` curve reaches about `145.7A`; the `125%` fuse basis is about `182A`, so `200A` is the next standard size and remains within the installed `2/0 AWG` conductor envelope.
2. Obsolete pre-Mechman charger/fuse paths are removed from active architecture and primary layout planning.
3. Confirmed `PH-VAN` harness uses one short red/black pair as combined regulator power and voltage sense. Treat former separate `F-12` regulator-power and `F-13` positive-sense functions as one `15A` fused red lead from the `F-04` alternator/load-side stud. Use one compact Eaton/Bussmann `HEB-AA` in-line holder with a Littelfuse `KLKD015.T` `600VAC/DC` fuse; no DC fuse panel or DIN enclosure. Put the Wakespeed shunt on the battery side of the hard-mounted SmartShunt; its purple/high and grey/low sense leads remain unfused.
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
- Use `F-04 200A/80V` in Lynx Slot 3. This preserves margin above the published `145.7A` curve while protecting the existing `2/0 AWG` run.
- Reuse existing uncut `2/0` inventory for alternator `+` and dedicated negative run.
- Inactive BOM row `173` preserves the removed contingency estimate; open a new active line only if field measurement proves an actual shortfall.

## Required Fuse Map (Start-to-Finish, With Housing)
| Fuse ID | Circuit (source -> load) | Protected wire/device | Fuse type and voltage class | Amperage | Holder or housing method | Physical location | Planned conductor gauge |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `F-01A` | Battery A `+` -> bank positive combine/disconnect input | Battery A positive cable leaving battery | Class T (`>=125VDC`) | `200A` provisional | Blue Sea Class T fuse block (covered stud mount, `110A-200A` family) | Battery compartment, within ~`7"` of Battery A positive post | `2/0 AWG` |
| `F-01B` | Battery B `+` -> bank positive combine/disconnect input | Battery B positive cable leaving battery | Class T (`>=125VDC`) | `200A` provisional | Blue Sea Class T fuse block (covered stud mount, `110A-200A` family) | Battery compartment, within ~`7"` of Battery B positive post | `2/0 AWG` |
| `F-01C` | Battery C `+` -> bank positive combine/disconnect input | Battery C positive cable leaving battery | Class T (`>=125VDC`) | `200A` provisional | Blue Sea Class T fuse block (covered stud mount, `110A-200A` family) | Battery compartment, within ~`7"` of Battery C positive post | `2/0 AWG` |
| `F-02` | Lynx Slot 1 -> MultiPlus `DC+` | Main inverter positive feeder | `MEGA`, `58V` or `80V` | `125A` | Integrated Lynx Distributor fuse slot | Lynx Distributor, Slot 1 | `2/0 AWG` planned (`AWG 1` minimum on short run) |
| `F-03` | Lynx Slot 2 -> SmartSolar `BAT+` | MPPT battery-side positive feeder | `MEGA`, `80V` Victron replacement stock | `60A` | Integrated Lynx Distributor fuse slot | Lynx Distributor, Slot 2 | `6 AWG` |
| `F-04` | Lynx Slot 3 -> `48V` alternator branch input (`ALT+`) | Alternator-to-house positive charge cable | `MEGA`, `80V` | `200A` | Integrated Lynx Distributor fuse slot | Lynx Distributor, Slot 3 | `2/0 AWG` (reuse lock) |
| `F-05` | Lynx Slot 4 -> Orion `48V` input `+` | Orion `48V` input feeder | MEGA `40A`, body-marked `>=58VDC`; Victron `CIP138040020 40A/80V` replacement fallback | `40A` deliberate feeder-protection value; above Victron's `20A` table recommendation but safely below installed `6 AWG` ampacity | Integrated Lynx Distributor fuse slot | Lynx Distributor, Slot 4 | Existing `6 AWG` direct to Orion; no second input fuse |
| `F-06` | Retired standalone Orion input fuse position | Not active | N/A | Not installed | No holder | N/A | Purchased `30A/58V` MIDI and FKS/ATO stock plus proposed DIN hardware remain unused; do not stack with `F-05` |
| `F-07` | Orion `12V` output `+` -> 12V fuse block main `+` stud | Main `12V` feeder from Orion into shared source-combine point | `MEGA`, `80V` Victron replacement stock | `60A` | Victron MEGA fuse holder (external, non-Lynx) | Electrical cabinet, within ~`7"` of Orion `12V` output stud | `6 AWG` planned (`8 AWG` minimum per Orion cable table) |
| `F-09` (not presently required) | Purchased Renogy `4S` string positive -> two-pole PV load-break -> MPPT PV input | Add only if the received-module/code review requires series OCP; one string has no peer-string backfeed | Listed `gPV`, voltage class above the received-label cold-string calculation; current nominal screen is `114.86V` at `-40C` | No fuse in the current one-string design; if required later, size from received `Isc`, module series-fuse rating, conductor ampacity, and applicable PV rules | Compatible inline holder/combiner only if required; do not procure the retired three-position fuse package | Roof-entry/service area | Final gauge after moving-route measurement; `10 AWG` PV cable remains the planning class |
| `F-10` | `12V` fuse block branch circuits -> each `12V` load | Individual `12V` branch conductors and load circuits | ATO/ATC blade fuses (`32V` class) | Per-circuit | Integrated sockets in marine `12V` fuse block | `12V` fuse block in electrical cabinet | Per branch |
| `AUDIO-HU` / `12V-12` | `12V` fuse block -> Kicker `46KMC2` media center/source unit | KMC2 source/head-unit branch conductor and device harness | ATO/ATC branch fuse (`32V` class) plus KMC2 harness `15A ATM` fuse | `15A` | Integrated `12V` fuse block branch plus OEM KMC2 harness fuse | Electrical cabinet to driver-side DC shelf/source face | `12 AWG duplex` if kept around `5 ft`; `10 AWG` if route grows toward `8 ft+` |
| `AUDIO-SUB` | 12V source/main `+` stud -> external fuse -> Kicker `49PTRTP10` powered sub `+` | Powered-sub positive branch and subwoofer input; manual-required external protection | Inline/MRBF/AFS/ANL-class fuse matched to selected `4 AWG` kit (`32V`+ DC class acceptable on 12V branch) | `40A` | Holder within about `18 in` of 12V source takeoff; if using Kicker `47KMPK4`, fit the PTRTP10-required `40A` fuse rather than the kit generic larger fuse | Near `12V` source/junction, downstream of `SW-12V-BATT` | `4 AWG` positive with matching `4 AWG` return to 12V negative bus/main stud |
| `F-11` | 12V buffer battery `+` -> 12V fuse block main `+` stud via `SW-12V-BATT` | Buffer battery source cable and downstream junction fault exposure | Inline MIDI/AMI/ANL family rated `>=32VDC` | `100A` class baseline | Sealed inline holder mounted close to battery positive | Within ~`7"` of 12V buffer battery positive post | `4 AWG` planned |
| `F-12/F-13-PHVAN` | `F-04` alternator/load-side stud -> WS500 `PH-VAN` red lead | Combined WS500 regulator power and positive voltage-sense lead | Littelfuse `KLKD015.T` fast-acting midget fuse, `600VAC/DC` | `15A` | Eaton/Bussmann `HEB-AA` water-resistant in-line holder, `600V` | In-line immediately beside `F-04`; short `14 AWG` pigtails with sealed step-down splice to the `16 AWG` harness; no panel, DIN rail, or enclosure | `14 AWG` pigtail / harness lead |
| `CERBO-PWR` | `48V` system positive -> Cerbo GX power `+` | Cerbo GX low-current electronics feed | Inline fuse/holder rated for `48V` bank maximum voltage | `1A-3A` | Small inline holder close to the positive takeoff | Electrical cabinet, preferably system/load side of main disconnect so Cerbo powers down with the house system during bench shutdown | `18 AWG` red/black duplex acceptable |
| `F-15` | Ford Upfitter `#3` -> WS500 brown ignition/enable wire | Low-current regulator enable/control wire | Inline ATC/ATO (`32V` class acceptable; 12V control circuit) | `3A` | Purchased Anyongora sealed 16 AWG holder stock near the Ford upfitter blunt-cut source / splice handoff; verify exact 3A fuse is present and received holder/wire markings before use | Engine bay or control-wire handoff point before small-gauge run to WS500 | `16 AWG` TXL/GXL |
| `OEM-SHUNT` | Battery-side positive or Lynx/system positive tap -> SmartShunt `Vbatt+` terminal | SmartShunt electronics supply/sense lead | External Victron-supplied red cable with inline low-current fuse; not an internal SmartShunt fuse | OEM value | Inline holder in supplied red cable | Prefer battery-side positive if SOC continuity is desired while the main disconnect is open; system side is acceptable if zero parasitic draw during disconnect-off storage matters more | OEM harness lead |

## Retired Fuse IDs
Obsolete pre-Mechman charger/fuse paths are removed from the active schedule. Do not reserve board space or labels for them.

## Spare Fuse Inventory (Updated)
| Fuse type | Installed qty | Spare qty to carry | Notes |
| --- | --- | --- | --- |
| Class T `200A` (provisional installed) | `3` | `1` on hand | Owner confirmed `3` holders and `4` slow-blow Class T fuses total (`3` installed + `1` spare); add more only if the one-spare-per-installed policy is later desired |
| `MEGA 200A/80V` | `1` | `1` minimum | Alternator branch (`F-04`); Amazon Victron stock is commonly sold as a five-pack, so install one and carry one while retaining the remainder as shop stock |
| `MEGA 125A` (`58V/80V`) | `1` | `4` | MultiPlus branch |
| `MEGA 60A` (`80V`) | `2` | `3` | Victron 5-pack row `188`: install MPPT (`F-03`) + Orion output (`F-07`), keep 3 spares. Earlier 6x low-cost 60A MEGA batch was owner-confirmed misadvertised/not actually 58V and is quarantined/trash, not 48V install stock. |
| `MEGA 40A`, `>=58VDC` | `1` active | `1-2` | Orion input in Lynx Slot 4 (`F-05`); existing body-marked `58VDC` stock is acceptable under the locked `56.8V` charge ceiling; use Victron `CIP138040020 40A/80V` as replacement fallback |
| Retired Orion standalone input-fuse stock | `0` active | Optional purchased stock only | `30A/58V` MIDI and FKS/ATO parts are not installed; no `USM1/ATM20` purchase required |
| 12V buffer battery main fuse (`100A` class) | `1` | `3` | Spare pack basis is BOM row `105` |
| WS500 `PH-VAN` combined regulator power / positive-sense fuse (`F-12/F-13-PHVAN`) | `1` required position | `1` optional later | One Littelfuse `KLKD015.T` `15A/600VAC/DC` midget fuse in an Eaton/Bussmann `HEB-AA` in-line holder is sufficient to commission; no panel or proprietary automotive contacts are needed |
| Cerbo GX power fuse (`CERBO-PWR`) | `1` active position | `1` | Carry a spare `1A-3A` fuse/holder rated for the `48V` bank maximum |
| WS500 ignition/enable fuse (`F-15`) | `1` active position | `2` | Four-holder/mixed-fuse package purchased in BOM row `176`; verify the assortment contains an exact `3A` ATO/ATC fuse before treating F-15 as install-ready, then carry two `3A` spares and one spare holder |
| PV string OCP (`F-09`) | `0` planned | `0` | Current candidate is one purchased Renogy `4S` string, so there is no peer-string backfeed. Reopen only if received labels, conductor/connector limits, or applicable PV rules require it. |
| SmartShunt OEM harness fuse | `1` | `1` | Keep OEM-equivalent spare if field-replaceable |
| ATO/ATC branch fuses | variable | `2` each used value | Keep mixed kit onboard |
| Camper audio KMC2 branch (`AUDIO-HU`) | `1` active `15A` branch plus KMC2 harness `15A ATM` | `2` spare `15A` blade/ATM fuses | Preserve both source-side conductor protection and the KMC2 harness fuse |
| Camper audio powered sub (`AUDIO-SUB`) | `1` active `40A` external fuse | `1-2` spare `40A` fuses matching the selected holder family | PTRTP10 manual calls for `40A` external fuse and `4 AWG` power/ground |

## BOM Row Mapping
| Fuse scope | BOM row(s) |
| --- | --- |
| Main battery Class T protection (`F-01A/F-01B/F-01C`) + Class T spares | `bom/bom_estimated_items.csv` row `7` |
| Lynx branch MEGA fuses (`F-02` to `F-05` installed) + spare set | `bom/bom_estimated_items.csv` rows `10`, `170`, `188`, and `323` |
| Orion installed fuse-holder hardware (`F-05` Lynx input, `F-07` external output) | `bom/bom_estimated_items.csv` rows `6` and `11` |
| Retired Orion standalone input-fuse stock (`F-06`) | Purchased stock: active BOM rows `133`, `182`, and `321`; inactive rows `326` and `230` preserve retired holder/bridge history. Row `321` empty FKS housings and row `133` `20A` fuses are not used anywhere in the final alternator/Orion topology. |
| WS500 regulator-power and voltage-sense protection (`F-12/F-13-PHVAN`) | Active BOM row `171`; inactive row `320` preserves the retired separate-`3A` concept |
| Cerbo GX power feed (`CERBO-PWR`) | `bom/bom_estimated_items.csv` row `22`; small inline fuse/holder may come from low-current install stock |
| WS500 Upfitter `#3` enable/control path (`F-15`) | `bom/bom_estimated_items.csv` row `176` |
| 12V buffer battery (`B12`) | `bom/bom_estimated_items.csv` row `21` |
| 12V buffer battery main fuse + holder (`F-11`) | `bom/bom_estimated_items.csv` row `125` |
| 12V battery disconnect (`SW-12V-BATT`) | `bom/bom_estimated_items.csv` row `124` |
| 12V branch panel and blade fuses (`F-10`) | `bom/bom_estimated_items.csv` row `16` |
| Camper audio source/head-unit branch (`AUDIO-HU` / `12V-12`) | `bom/bom_estimated_items.csv` rows `189`, `192`, and `193` |
| Camper audio powered-sub branch (`AUDIO-SUB`) | `bom/bom_estimated_items.csv` rows `191` and `192` |
| SmartShunt external OEM fused red lead (`OEM-SHUNT`) | `bom/bom_estimated_items.csv` row `23` (included with SmartShunt kit) |
| Final PV string OCP / combiner / disconnect allowance (`F-09`, if required) | `bom/bom_estimated_items.csv` row `106` |

## Assumptions and Open Items
1. Wire sizing above assumes copper conductors and enclosed vehicle routing.
2. Solar panels are purchased as `4x Renogy 175W flexible = 700W`; the current candidate is one `4S` string on the Victron `150/45`. Current official G2 planning data give `95.6V Voc` and `9.50A Isc` at STC; published-coefficient cold Voc is `114.86V` at `-40C`. With one string, no individual `F-09` is presently planned. Verify received labels, connector/conductor ratings, moving-route ampacity, hot restart/tracking, and final code basis before as-built release; do not purchase or install the retired `3x 15A gPV` package.
3. Do not complete the owned Littelfuse `178.6150.0001` empty housings. Use the Eaton/Bussmann `HEB-AA` + Littelfuse `KLKD015.T` in-line branch for the PH-VAN red lead. The Wakespeed shunt is on the battery side of the hard-mounted SmartShunt, uses no `5A` sense fuses, and must be configured `Shunt at Battery`.
4. `SW-12V-BATT` remains manual-only in Phase 1; no automatic LVD behavior is assumed.
5. Final lock for `F-11` still requires explicit 12V buffer battery/BMS continuous discharge-current confirmation.
6. `F-15` exists to protect the smaller-gauge control wire between Ford `Upfitter #3` and the WS500 brown ignition/enable wire; the factory `25A` upfitter circuit protection is not the final wire-protection device for that branch. The purchased row `176` holder pack does not clear this gate until an exact `3A` fuse and the received 16 AWG holder/wire markings are verified.
7. Orion `F-05/F-06` lock: the active topology uses `F-05`, one `40A` MEGA body-marked at least `58VDC` in Lynx Slot 4, feeding the existing `6 AWG` Orion input directly. `F-06` is retired. This deliberately prioritizes simple feeder protection over strict adherence to Victron's `20A` table recommendation; do not stack an inline fuse after the Lynx fuse.
8. Camper audio `12V` load: KMC2 source branch and PTRTP10 powered-sub branch are downstream 12V loads, not new 48V branches. The PTRTP10 `40A` branch can exceed Orion `30A` continuous output during heavy bass; rely on the 12V buffer battery for transients and validate sustained loud-use behavior before assuming all 12V loads can run at max simultaneously.
9. Orion holder correction: no standalone input holder is required. The purchased `178.6150.0001` housing-only parts and `30A/58V` MIDI stock remain unused; do not salvage or stack them into the final branch. Torque the Slot 4 MEGA hardware and Orion terminals to current manufacturer values, tug-test, and strain-relieve the existing `6 AWG` pair.
