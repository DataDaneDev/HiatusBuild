---
aliases:
  - 48V electrical architecture
  - Hiatus 48V baseline
tags:
  - hiatus/core
  - hiatus/electrical
status: active
related:
  - "[[SYSTEMS]]"
  - "[[ELECTRICAL_overview_diagram]]"
  - "[[ELECTRICAL_fuse_schedule]]"
  - "[[TRACKING]]"
---

# 48V Electrical Architecture

## Document role
- This file owns the final `48V` electrical architecture for the active build baseline.
- Use it for house-bank structure, alternator-path direction, shutdown logic, and manual control-path intent.
- Keep full conductor schedules, fuse matrices, and layout-level implementation detail in `docs/implementation/`.
- Keep unresolved vendor gates, risk state, and follow-up closure items in `docs/core/TRACKING.md`.
- Keep broad project sequencing and day-to-day execution framing in `docs/core/PROJECT.md` or the active plan docs.

As-of date: `2026-05-28`

Purpose: hold the finalized, concise `48V` house and alternator architecture in one place so wiring, protection, shutdown behavior, and BOM references are easy to understand without re-reading the historical trade studies.

Related docs:
- [Electrical topology diagram](../implementation/ELECTRICAL_overview_diagram.md)
- [Electrical fuse schedule](../implementation/ELECTRICAL_fuse_schedule.md)
- [Systems](SYSTEMS.md)
- [Tracking](TRACKING.md)
- [Estimated BOM](../../bom/bom_estimated_items.csv)

## Final direction
- House architecture stays `48V` core with `3x 51.2V 100Ah` batteries in parallel.
- Alternator charging is the dedicated `48V` secondary alternator path; obsolete pre-Mechman charger hardware is removed from active planning.
- Protection baseline is `Mechman + WS500 + Balmar APM-48`.
- Manual alternator-charge enable/disable is through Ford `Upfitter Switch #3`.
- `Upfitter #3` is a low-current control signal only. It does not carry alternator output current.
- `WS500` white `Feature-In` is reserved for future fault-interlock work, not required in Phase 1.

## Current commissioning state (`2026-05-27`)
- `48V` bus has been live-tested: owner measured `55.5V` throughout the system, including at the MultiPlus.
- MultiPlus-II DC/inverter mode has been switched on with inverter light illuminated, slight normal hum, and no reported error lights.
- SmartShunt and Orion-Tr Smart are visible in VictronConnect.
- Cerbo GX access point/remote-console workflow is active; Cerbo power is a small inline fused feed from the `48V` system side and MultiPlus communication is via `VE.Bus` RJ45.
- Shore charging has been short-tested through the MultiPlus at household-outlet current limits. This proves basic AC-in/charger function, not final charge-profile correctness.
- Do not treat the charger as commissioned for unattended/sustained use until the MultiPlus LiFePO4 charge profile is programmed/verified against the Dumfume manual: `58.4V +/-0.2V` charge/absorption target, equalization off, conservative LiFePO4 float/storage behavior, and source-current limit matched to the actual shore circuit. `DVCC` remains disabled unless a documented BMS/GX control path is added.
- AC-out branch/GFCI commissioning and secondary-alternator commissioning are still separate future gates.

## Locked component set
| Function | Locked baseline | BOM row(s) |
| --- | --- | --- |
| House batteries | `3x` Dumfume `51.2V 100Ah` LiFePO4 | `3` |
| Main house disconnect | Victron `275A` battery switch | `5` |
| Main fused distribution | Victron Lynx Distributor `M10` | `6` |
| Battery branch protection | `F-01A/B/C` `200A` Class T; manual-backed battery limit is `200A` max continuous discharge per battery, with terminal/manufacturer fuse guidance still not separately specified; owner confirmed `3` holders and `4` slow-blow Class T fuses total | `7` |
| Inverter/charger | MultiPlus-II `48/3000/35-50` | `12` |
| 48V to 12V charger | Orion-Tr Smart `48/12-30`; fed from Lynx `48V+` bus tap through standalone `F-06` (`30A 58V` MIDI interim, `20A 80V` FKS/ATO final); Lynx Slot 4 remains open | `20`, `11`, `133`, `182` |
| Monitoring | Cerbo GX + SmartShunt `300A` | `22`, `23` |
| Alternator kit | Mechman `48V` secondary alternator kit with `WS500` | `168` |
| Load-dump clamp | Balmar `APM-48` | `169` |
| Alternator branch fuse | `F-04` `150A` MEGA (`58V/80V`) in Lynx Slot 3 | `170` |
| WS500 low-current fuse set | `F-12` regulator power + `F-13` positive voltage sense; current-sense pair is unfused per current manual | `171` |
| WS500 Upfitter #3 control kit | `F-15` + control wire + holder/terminals | `176` |

## Battery manual limits and charger-programming baseline
- Battery model basis: Dumfume `51.2V 100Ah` LiFePO4, `3x` in parallel (`1S3P`; manual allows up to `1S4P`).
- Per-battery charge voltage: `58.4V +/-0.2V`; charge-limit/over-charge protection voltage also listed as `58.4V`.
- Per-battery current references: recommended charge `20A`; max continuous charge `100A`; recommended discharge `50A`; max continuous discharge `200A`.
- Bank-level reference for current `3x` setup: recommended charge `60A`; max continuous charge `300A`; recommended discharge `150A`; max continuous discharge `600A`.
- Protection thresholds: over-discharge protection `36.8V`, recovery `43.2V`; discharge overcurrent protection `600A`; short-circuit protection `1800A`.
- Temperature thresholds: low-temp charge protection approx `41F-50F` with recovery at `50F`; high-temp protection listed as `157F`/`140F`.
- MultiPlus-II charger limit is `35A`, so full-output charging is below the bank's `60A` recommended-charge reference. For first household-outlet tests, keep AC input current at `10A`, then `12A` max on a normal `15A` source.

## 48V power path
```mermaid
flowchart LR
    BATA["Battery A"] --> F01A["F-01A 200A Class T"]
    BATB["Battery B"] --> F01B["F-01B 200A Class T"]
    BATC["Battery C"] --> F01C["F-01C 200A Class T"]

    F01A --> POSBUS["48V + battery-side bus"]
    F01B --> POSBUS
    F01C --> POSBUS
    POSBUS --> DISC["48V main disconnect"]
    DISC --> LYNX["Lynx Distributor"]

    BATA -. "2/0 AWG -" .-> NEGBUS["48V - battery-side bus"]
    BATB -. "2/0 AWG -" .-> NEGBUS
    BATC -. "2/0 AWG -" .-> NEGBUS
    NEGBUS --> SHUNT["SmartShunt 300A"]
    SHUNT --> LYNX

    ALT48["Secondary 48V alternator"] --> APM48["APM-48"]
    APM48 --> F04["F-04 150A MEGA"]
    F04 --> LYNX
    ALT48 -. "Dedicated 2/0 AWG return" .-> LYNX

    LYNX --> MULTI["MultiPlus-II 48/3000\nSlot 1 / F-02 125A"]
    LYNX --> MPPT["SmartSolar 150/45\nSlot 2 / F-03 60A"]
    LYNX --> SLOT4["Lynx Slot 4 / F-05\nopen spare"]
    LYNX --> F06["F-06 inline Orion input fuse\n30A 58V MIDI interim\n20A 80V FKS/ATO final"]
    F06 --> ORION["Orion 48/12-30"]
```

## Alternator control path
```mermaid
flowchart LR
    UP3["Ford Upfitter Switch #3\n(factory relay output)"] --> F15["F-15 3A inline fuse"]
    F15 --> BROWN["WS500 brown ignition/enable wire"]
    WHITE["WS500 white Feature-In"] -. "reserved for future automatic fault interlock" .- WS500["WS500 regulator"]
    BROWN --> WS500
    WS500 -. "field/stator/sense harness" .- ALT48["Secondary 48V alternator"]
```

### Control logic
- `Upfitter #3 ON`: `WS500` brown wire is energized, regulator is allowed to run, alternator charging can occur.
- `Upfitter #3 OFF`: `WS500` is disabled through the brown wire, regulator field output collapses, and alternator charging stops.
- Use `Upfitter #3` as the manual alternator-charge shutdown control.
- Do not use the main `48V` disconnect as the first alternator shutdown method while the engine is running and the secondary alternator is charging.

### Why `Upfitter #3`
- It is already a factory-switched, relay-driven `12V` control source.
- It keeps the WS500 control in the truck cab without adding a separate aftermarket switch.
- It is suitable for a low-current enable signal, but not for any high-current alternator or battery conductor.
- A local inline fuse is still required because the factory upfitter circuit fuse is much larger than the small-gauge WS500 control wire.

## Fusing and wire baseline
| ID | Function | Locked value | Wire basis |
| --- | --- | --- | --- |
| `F-01A/B/C` | Battery branch positive protection | `200A` Class T provisional | `2/0 AWG` |
| `F-04` | Alternator branch into Lynx Slot 3 | `150A` MEGA (`58V/80V`) | `2/0 AWG` |
| `F-05` | Lynx Slot 4 | Open/blank spare fused position; not used for Orion | N/A |
| `F-06` | Orion `48V` input from Lynx bus tap | `30A 58V` MIDI interim; `20A 80V` FKS/ATO final | `6 AWG` planned; keep source-side unfused tap short |
| `F-12` | WS500 regulator power lead | `10A` baseline (`15A` if required by alternator case); voltage rating must cover the connected alternator/system positive voltage | harness lead |
| `F-13` | WS500 positive voltage-sense lead | `3A`; fuse/holder voltage class must cover the `48V` bank maximum unless proven by WS500 harness documentation | harness lead |
| `CERBO-PWR` | Cerbo GX low-current power feed | `1A-3A` inline fuse/holder rated for the `48V` bank maximum; system/load side of main disconnect preferred for bench shutdown | `18 AWG` red/black duplex acceptable |
| WS500 current-sense pair | Purple/grey current-sense high/low to shunt/current-sense point | No separate fuse position in current Wakespeed manual; twist pair if extended and route away from noise | harness lead |
| `F-15` | Upfitter #3 to WS500 brown ignition wire | `3A` inline ATO/ATC on 12V control circuit | `16 AWG` TXL/GXL control wire |

### Major conductors
- Battery branch and main `48V` trunk wiring: `2/0 AWG`.
- Parallel battery-current sharing target is similar **total loop resistance** per battery path, not equal positive-only length. The current bench layout may use short/medium/long positive leads balanced by long/medium/short negative leads; do not add unnecessary cable coils solely to make positive leads identical.
- Secondary alternator positive path (`ALT B+ -> APM-48 -> F-04 -> Lynx`): `2/0 AWG`, `~20 ft` one-way planning basis.
- Secondary alternator dedicated negative return (`ALT B- -> Lynx -`): `2/0 AWG`, `~20 ft` one-way planning basis.
- Orion `48V` feeder and MPPT battery leads: `6 AWG`; Orion positive leaves the Lynx bus through standalone `F-06`, not Lynx Slot 4.
- Upfitter #3 control lead to WS500 brown wire: `16 AWG` TXL/GXL planning basis, `~6 ft` one-way assumed until measured.

## APM-48 wiring intent
- Mount the `APM-48` at the alternator end of the `48V` branch, as close to the alternator output as practical.
- Connect APM red to alternator `B+`.
- Connect APM black to alternator `B-`, or to the approved alternator ground/case point if the alternator is not isolated-ground.
- Do not stack the APM ring terminals under the main battery cable lugs unless the product instructions for the exact unit explicitly allow it.

## Normal operating sequence
1. Main `48V` disconnect closed.
2. `Upfitter #3` switched `ON`.
3. Engine running.
4. `WS500` enabled and regulating.
5. Alternator charges the house bank through `APM-48` and `F-04`.

## Fault and shutdown sequence
If a battery pack trips or an alternator fault is suspected:
1. Switch `Upfitter #3` `OFF` to disable the `WS500`.
2. Wait for alternator charge current to collapse.
3. Open the main `48V` disconnect only after alternator charging is no longer active, if full house shutdown is required.

Reason:
- The regulator should be shut down first.
- The `APM-48` is a protection layer, not the primary shutdown method.

## One-battery-trip behavior
- If one battery BMS disconnects but the other two remain online, the `48V` bus should stay up.
- The system does not immediately become a full-bank load dump event just because one battery disappears.
- The practical effect is that charge and discharge current redistribute to the remaining batteries.
- The real hazard is a cascade where the second and third battery also disconnect under active alternator charge.

## What is still not fully closed
- Final Mechman kit fitment/content confirmation for the exact truck.
- Final `WS500` harness polarity confirmation (`PH` vs `NH`).
- Official vendor confirmation that the documented Dumfume battery/BMS behavior is acceptable with the `WS500`.
- Exact alternator negative/case isolation behavior in the installed Mechman kit.
- Whether future automatic fault-interlock logic should be added on the WS500 `Feature-In` or through an external relay.

## Rule for future edits
- Update this file first for any `48V` architecture, alternator-control, or shutdown-strategy change.
- Keep the implementation files for wiring detail and fuse placement, not for high-level architecture decisions.
