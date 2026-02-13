# Electrical Topology Diagram (Implementation v4)

As-of date: `2026-02-13`

Purpose: provide a complete, install-level electrical topology for the current build scope, including all major electrical components, fuse IDs, fuse housings, and planned wire gauges.

Related docs:
- Canonical electrical/system baseline: `docs/SYSTEMS.md`
- Detailed fuse matrix: `docs/ELECTRICAL_fuse_schedule.md`
- Decisions and unresolved items: `docs/TRACKING.md`
- Procurement source of truth: `bom/bom_estimated_items.csv`

## Sweep Outcomes Included In This Revision
- Corrected Sterling `BB1248120` modeling basis to `~1500W` max output (`~26A` at `57.6V`), replacing prior `120A @ 48V` planning assumption.
- Added explicit fuse-holder/housing definitions for every fuse family (`Class T`, Lynx `MEGA`, inline `MIDI/ANL/AMI`, PV `gPV`, and `ATO/ATC`).
- Added conductor schedule across `48V`, `12V`, PV, and AC segments with explicit assumptions.

## Complete Power Topology (48V Core + Charge Sources)
```mermaid
flowchart LR
    subgraph VEHICLE_12V["Vehicle 12V Charging Path"]
        ALT["Factory alternator\n(240A assumed)"]
        START["Starter battery 12V"]
        F08["F-08 150A\nsealed engine-bay holder"]
        B2B["Sterling BB1248120\n12V->48V (~1.5kW max)"]
        BBR["Sterling BBR remote\ncurrent-limit control"]
        ALT --> START
        START -- "2/0 AWG" --> F08 --> B2B
        BBR -. "control harness" .- B2B
    end

    subgraph PV_PATH["Solar Path (900W, 3S3P)"]
        PVA["PV String A\n3x100W"]
        PVB["PV String B\n3x100W"]
        PVC["PV String C\n3x100W"]
        F09A["F-09A 15A gPV"]
        F09B["F-09B 15A gPV"]
        F09C["F-09C 15A gPV"]
        COMB["PV combiner enclosure\n3x 10x38 fuse holders"]
        MPPT["Victron SmartSolar\nMPPT 150/45"]
        PVA -- "10 AWG PV" --> F09A --> COMB
        PVB -- "10 AWG PV" --> F09B --> COMB
        PVC -- "10 AWG PV" --> F09C --> COMB
        COMB -- "10 AWG PV +/-" --> MPPT
    end

    subgraph HOUSE_48V["House 48V Core"]
        BATA["Battery A\n48V 100Ah"]
        BATB["Battery B\n48V 100Ah"]
        F01A["F-01A 225A Class T\nBlue Sea block"]
        F01B["F-01B 225A Class T\nBlue Sea block"]
        DISC["48V disconnect\nVictron 275A"]
        SHUNT["SmartShunt 500A\nmain negative path"]
        LYNX["Victron Lynx Distributor M10\n+ bus / - bus / 4 MEGA slots"]
        MULTI["MultiPlus-II\n48/3000/35-50"]
        ORION["Orion-Tr 48/12-30\nIsolated"]
        F06["F-06 20A (or 23A)\ninline >=58V holder"]
    end

    BATA -- "2/0 AWG +" --> F01A --> DISC
    BATB -- "2/0 AWG +" --> F01B --> DISC
    DISC -- "2/0 AWG +" --> LYNX

    BATA -- "2/0 AWG -" --> SHUNT
    BATB -- "2/0 AWG -" --> SHUNT
    SHUNT -- "2/0 AWG -" --> LYNX
    LYNX -. "SmartShunt fused + sense/power lead\n(factory harness)" .- SHUNT

    LYNX -- "Slot 1: F-02 125A MEGA\n2/0 AWG +" --> MULTI
    MULTI -- "2/0 AWG -" --> LYNX

    MPPT -- "BAT+ via Slot 2: F-03 60A MEGA\n6 AWG" --> LYNX
    MPPT -- "BAT- 6 AWG" --> LYNX

    B2B -- "OUT+ via Slot 3: F-04 40A MEGA\n6 AWG" --> LYNX
    B2B -- "OUT- 6 AWG" --> LYNX

    LYNX -- "Slot 4: F-05 40A MEGA\n6 AWG" --> F06 --> ORION
    ORION -- "48V input - (6 AWG)" --> LYNX
```

## 12V Distribution Topology (From Orion)
```mermaid
flowchart LR
    ORION["Orion-Tr 48/12-30\nIsolated converter"]
    F07["F-07 60A\ninline holder near Orion"]
    PANEL["12V fuse panel\nBlue Sea 5026/5032 style"]
    N12["12V negative busbar"]

    STAR["12V-01 Starlink PSU\n10A / 14 AWG"]
    FRIDGE["12V-02 Fridge\n15A / 14 AWG"]
    HEATER["12V-03 Diesel heater\n15A / 14 AWG"]
    PUMP["12V-04 Water pump\n10A / 14 AWG"]
    DET["12V-05 CO+Propane detector\n3A / 18/2"]
    LED["12V-06 LED strips\n5A / 18/2"]
    CERBO_PWR["12V-07 Cerbo GX feed\n3A / 18/2 (assumed)"]
    SP1["12V-08 Spare\n15A / 14 AWG"]
    SP2["12V-09 Spare\n15A / 14 AWG"]

    ORION -- "12V + (6 AWG)" --> F07 --> PANEL
    ORION -- "12V - (6 AWG)" --> N12

    PANEL --> STAR
    PANEL --> FRIDGE
    PANEL --> HEATER
    PANEL --> PUMP
    PANEL --> DET
    PANEL --> LED
    PANEL --> CERBO_PWR
    PANEL --> SP1
    PANEL --> SP2

    STAR --> N12
    FRIDGE --> N12
    HEATER --> N12
    PUMP --> N12
    DET --> N12
    LED --> N12
    CERBO_PWR --> N12
```

## AC Path Topology (Shore + Inverter Output, Full Hierarchy)
```mermaid
flowchart LR
    subgraph SHORE_SRC["Shore Source Path"]
        INLET["Shore inlet (120VAC)"]
        CORD["Shore cord + adapters\n(service-limited by pedestal/source)"]
        EMS["Optional EMS/surge protection"]
        ACINBRK["AC input breaker/disconnect\n20A target (or sized to source)"]
        INLET --> CORD --> EMS --> ACINBRK
    end

    subgraph MULTI_AC["MultiPlus-II AC Conversion + Transfer"]
        ACIN["AC-in terminals (L/N/PE)"]
        XFER["Internal transfer relay + charger stage\n(shore present = pass-through + charging)"]
        OUT1["AC-out-1 (inverter-backed output)"]
        OUT2["AC-out-2 (shore-only optional output)"]
        ACIN --> XFER --> OUT1
        XFER --> OUT2
    end

    subgraph AC_DIST["AC Distribution and Protection"]
        OUT1PROT["UL943-class RCD/GFCI + branch breaker(s)\nfor AC-out-1"]
        BR_A["Branch A: galley outlets"]
        BR_B["Branch B: office outlets"]
        OUT2PROT["AC-out-2 breaker + RCD/GFCI\n(shore-only future loads, optional)"]
        OUT1PROT --> BR_A
        OUT1PROT --> BR_B
    end

    subgraph AC_LOADS["Planned AC Loads"]
        IND["Induction cooktop"]
        MW["Microwave"]
        MON["External monitor + office chargers"]
        GENOUT["General 120V receptacles\n4 total locations (2 galley, 2 office)"]
        SHORE_ONLY["Future shore-only load (optional)\nA/C or electric water heat"]
    end

    subgraph USB_PD["USB/USB-C PD Strategy"]
        PD_DC["Locked: 12V branch -> DC USB-C PD modules\n4 total points (2 office, 2 galley)"]
        PD_AC["Alternative: USB receptacles on AC branch"]
    end

    ACINBRK --> ACIN
    OUT1 --> OUT1PROT
    OUT2 --> OUT2PROT

    BR_A --> IND
    BR_A --> MW
    BR_A --> MON
    BR_B --> GENOUT
    OUT2PROT --> SHORE_ONLY

    BR_A -. "if AC USB outlets selected" .-> PD_AC
```

### AC Operating Behavior (Expected)
- Shore present: MultiPlus transfer relay closes, AC-in is passed to AC-out paths, and charger stage charges the `48V` bank.
- Shore absent: MultiPlus transfers to inverter mode and powers `AC-out-1` from battery; `AC-out-2` drops by design.
- Input current limit should be set to the actual shore source (`15A`, `20A`, or `30A` adapter-limited) to avoid pedestal/source breaker trips.

### AC Safety/Protection Chain (What Must Exist)
- Upstream AC input protection/disconnect before MultiPlus AC-in.
- AC-out branch protection including UL943-class residual-current protection and overcurrent protection sized to branch wiring and expected load.
- Continuous equipment grounding path from shore inlet through MultiPlus and branch circuits, plus chassis bond in mobile install context.
- Neutral/ground handling must follow MultiPlus relay behavior; do not add an always-bonded downstream neutral-ground bond in branch receptacle wiring.

### AC Reference Basis (Manufacturer Guidance)
- Victron MultiPlus-II `120V` installation guidance (`AC-in` breaker sizing, UL943-class residual-current protection on outputs, and AC-out-2 shore-only behavior): `https://www.victronenergy.com/media/pg/MultiPlus-II_120V/en/installation.html`
- Victron MultiPlus-II datasheet (`48/3000/35-50` baseline model reference): `https://www.victronenergy.com/upload/documents/Datasheet-MultiPlus-II-inverter-charger-120V-EN.pdf`

### AC/USB Baseline Locked For BOM
- Shore interface: `30A` RV-style inlet baseline with adapter kit for `15A`/`20A` hookups.
- AC input protection: dedicated AC input breaker/disconnect upstream of MultiPlus AC-in.
- AC-out-1 distribution: two protected branches (`20A` galley, `15A` office) with GFCI-at-first-outlet strategy.
- Receptacle plan: `4` total `120V` receptacle locations (`2` galley, `2` office).
- USB charging plan: `4` DC-fed USB-C PD points on `12V` branches (`2` office, `2` galley) with `10A` per-zone branch fuse baseline.
- AC-out-2 remains optional and not in Phase 1 procurement baseline.

## Monitoring and Control Topology
```mermaid
flowchart LR
    CERBO["Cerbo GX"]
    MULTI["MultiPlus-II"]
    MPPT["SmartSolar MPPT"]
    SHUNT["SmartShunt 500A"]
    ORION["Orion-Tr 48/12"]
    BTEMP["Battery temp sensor"]
    SHUNT_PWR["SmartShunt fused + lead\n(factory harness)"]

    CERBO -. "VE.Bus" .- MULTI
    CERBO -. "VE.Direct" .- MPPT
    CERBO -. "VE.Direct" .- SHUNT
    ORION -. "VictronConnect/BLE\n(no direct GX link in this baseline)" .- CERBO
    BTEMP -. "temp input" .- MULTI
    SHUNT_PWR -. "power/sense harness" .- SHUNT
```

## Fuse Housing Map (Where Each Fuse Is Physically Housed)
| Fuse ID | Fuse value | Housing method | Location |
| --- | --- | --- | --- |
| `F-01A` | `225A Class T` | Blue Sea Class T fuse block | Battery compartment near Battery A `+` |
| `F-01B` | `225A Class T` | Blue Sea Class T fuse block | Battery compartment near Battery B `+` |
| `F-02` | `125A MEGA` | Lynx integrated slot holder | Lynx Slot 1 |
| `F-03` | `60A MEGA` | Lynx integrated slot holder | Lynx Slot 2 |
| `F-04` | `40A MEGA` | Lynx integrated slot holder | Lynx Slot 3 |
| `F-05` | `40A MEGA` | Lynx integrated slot holder | Lynx Slot 4 |
| `F-06` | `20A` target / `23A` MIDI fallback | Inline sealed holder (`>=58VDC`) | Electrical cabinet near Orion branch source |
| `F-07` | `60A` | Inline sealed holder (`>=32VDC`) | Electrical cabinet at Orion `12V +` source end |
| `F-08` | `150A` | Sealed engine-bay MEGA/ANL holder | Engine bay near starter battery `+` |
| `F-09A/B/C` | `15A gPV` each | `10x38` touch-safe fuse holders in PV combiner | Roof-entry combiner enclosure |
| `F-10` | Per branch (`ATO/ATC`) | Integrated blade sockets in 12V panel | Electrical cabinet |
| `OEM-SHUNT` | Factory low-current inline fuse (SmartShunt harness) | Integrated inline holder in Victron harness lead | Electrical cabinet near Lynx positive tap |

## Conductor Schedule (Start-to-Finish)
| Segment ID | Circuit segment | Nominal voltage | Current basis | Overcurrent protection | Planned wire gauge |
| --- | --- | --- | --- | --- | --- |
| `C-01` | Battery A `+` -> `F-01A` | `48V` | Battery branch, fuse-limited | `F-01A` `225A` | `2/0 AWG` |
| `C-02` | Battery B `+` -> `F-01B` | `48V` | Battery branch, fuse-limited | `F-01B` `225A` | `2/0 AWG` |
| `C-03` | Class T outputs -> disconnect input | `48V` | Combined trunk current | `F-01A/B` | `2/0 AWG` each branch |
| `C-04` | Disconnect output -> Lynx `+` bus | `48V` | Aggregate branch current (`<=265A` theoretical from Lynx slots) | Upstream Class T fuses | `2/0 AWG` |
| `C-05` | Battery negatives -> SmartShunt battery side | `48V` | Aggregate return current | N/A (main negative path) | `2/0 AWG` each branch |
| `C-06` | SmartShunt load side -> Lynx `-` bus | `48V` | Aggregate return current | N/A | `2/0 AWG` |
| `C-06A` | Lynx positive tap -> SmartShunt positive sense/power lead | `48V` | Shunt electronics supply (very low current) | Factory inline fuse in OEM harness | OEM harness lead |
| `C-07` | Lynx Slot 1 (`F-02`) -> MultiPlus `DC+` | `48V` | Inverter branch, fuse-limited | `F-02` `125A` | `2/0 AWG` (manual minimum `AWG 1` on short runs) |
| `C-08` | MultiPlus `DC-` -> Lynx `-` bus | `48V` | Inverter return current | `F-02` protects paired positive | `2/0 AWG` |
| `C-09` | MPPT `BAT+` -> Lynx Slot 2 (`F-03`) | `48V` | Controller output (`45A` max) | `F-03` `60A` | `6 AWG` |
| `C-10` | MPPT `BAT-` -> Lynx `-` bus | `48V` | Controller return current | `F-03` protects paired positive | `6 AWG` |
| `C-11` | Sterling output `+` -> Lynx Slot 3 (`F-04`) | `48V` | Charger output (`~26A` nominal max) | `F-04` `40A` | `6 AWG` planned (`10 AWG` minimum per Sterling table) |
| `C-12` | Sterling output `-` -> Lynx `-` bus | `48V` | Charger return current | `F-04` protects paired positive | `6 AWG` |
| `C-13` | Lynx Slot 4 (`F-05`) -> `F-06` holder | `48V` | Orion branch feeder, fuse-limited | `F-05` `40A` | `6 AWG` |
| `C-14` | `F-06` -> Orion `48V +` input | `48V` | Orion input, fuse-limited | `F-06` `20A`/`23A` | `6 AWG` planned (`8 AWG` minimum per Orion table) |
| `C-15` | Orion `48V -` input -> Lynx `-` bus | `48V` | Orion input return current | `F-06` protects paired positive | `6 AWG` |
| `C-16` | Starter battery `+` -> `F-08` -> Sterling input `+` | `12V` | Charger input path, fuse-limited | `F-08` `150A` | `2/0 AWG` planned (`2 AWG` minimum per Sterling table) |
| `C-17` | Vehicle return/chassis -> Sterling input `-` | `12V` | Charger input return | `F-08` protects paired positive | `2/0 AWG` planned |
| `C-18` | Orion `12V +` -> `F-07` -> 12V panel `+` bus | `12V` | Converter output path (`30A` continuous, `60A` fuse) | `F-07` `60A` | `6 AWG` planned (`8 AWG` minimum per Orion table) |
| `C-19` | Orion `12V -` -> 12V negative busbar | `12V` | Converter output return | `F-07` protects paired positive | `6 AWG` |
| `C-20` | 12V panel -> Starlink PSU | `12V` | Branch load | `F-10` `10A` | `14 AWG duplex` |
| `C-21` | 12V panel -> Fridge | `12V` | Branch load | `F-10` `15A` | `14 AWG duplex` |
| `C-22` | 12V panel -> Diesel heater | `12V` | Branch load | `F-10` `15A` | `14 AWG duplex` |
| `C-23` | 12V panel -> Water pump | `12V` | Branch load | `F-10` `10A` | `14 AWG duplex` |
| `C-24` | 12V panel -> CO + propane detector | `12V` | Branch load | `F-10` `3A` | `18/2` |
| `C-25` | 12V panel -> LED strips | `12V` | Branch load | `F-10` `5A` | `18/2` |
| `C-26` | 12V panel -> Cerbo GX power feed | `12V` | Branch load (`~3W`) | `F-10` `3A` (assumed) | `18/2` |
| `C-27` | PV strings -> `F-09` combiner -> MPPT PV input | PV string voltage (`3S`) | String current + combiner output current | `F-09A/B/C` `15A` each | `10 AWG` PV wire |
| `C-28` | Shore inlet -> shore cord/adapter -> AC input breaker/disconnect | `120VAC` | Source-limited shore current | Source-size-matched AC breaker/disconnect (`20A` target baseline) | `10/3` shore feed to inlet/breaker area |
| `C-29` | AC input breaker/disconnect -> MultiPlus AC-in | `120VAC` | MultiPlus AC input current | Upstream AC breaker/disconnect (`C-28`) | `12 AWG` stranded AC conductors |
| `C-30` | MultiPlus AC-out-1 -> branch RCD/GFCI + breaker assembly | `120VAC` | Inverter-backed branch distribution current | UL943-class RCD/GFCI + branch breakers (`20A` galley, `15A` office) | `12 AWG` stranded AC conductors |
| `C-31` | Branch A -> galley receptacle locations (`2`) | `120VAC` | Branch load (induction, microwave, galley outlets) | `C-30` branch protection stack | `12 AWG` stranded AC conductors |
| `C-32` | Branch B -> office receptacle locations (`2`) | `120VAC` | Branch load (monitor and office outlet use) | `C-30` branch protection stack | `12 AWG` stranded AC conductors |
| `C-33` | MultiPlus AC-out-2 (optional) -> shore-only future load branch | `120VAC` | Shore-only branch current | Dedicated breaker + UL943-class RCD/GFCI for AC-out-2 | `12 AWG` stranded AC conductors |
| `C-34` | 12V panel -> USB-C PD branch (office zone, `2` outlets) | `12V` | Device charging branch current (zone budget target `~100-120W`) | `F-10` branch fuse (`10A` baseline) | `14 AWG duplex` baseline |
| `C-35` | 12V panel -> USB-C PD branch (galley zone, `2` outlets) | `12V` | Device charging branch current (zone budget target `~100-120W`) | `F-10` branch fuse (`10A` baseline) | `14 AWG duplex` baseline |

## Additional Components Included In Topology Scope
- `48V` disconnect (`275A`)
- Pre-charge resistor (commissioning/soft-charge aid before connecting large DC loads)
- 12V negative busbar
- Shore AC inlet + cord/adapter interface hardware
- AC input breaker/disconnect hardware (compact load-center baseline; DIN-only if swapped at SKU lock)
- AC branch RCD/GFCI + breaker hardware
- Receptacle boxes + `120V` outlets (`4` planned locations: `2` galley, `2` office)
- Optional AC-out-2 branch protection path for future shore-only loads
- USB-C PD branch hardware (`4` DC-fed points, `2` office + `2` galley)
- Battery temperature sensor wiring to inverter/monitoring path
- SmartShunt fused positive sense/power lead (factory harness)

## Assumptions (Explicit)
1. Cable sizing assumes stranded copper conductors, enclosed vehicle routing, and typical one-way run lengths of `<=10 ft` unless otherwise stated.
2. Voltage-drop design intent used here: `<=2%` on major `48V` power runs and `<=3%` on `12V` branch circuits.
3. `F-09` PV string fuse value (`15A`) remains provisional until final module datasheet max-series-fuse rating is confirmed.
4. Cerbo GX feed is assumed from the `12V` panel (`12V-07`) for branch-level serviceability.
5. Orion branch remains split-protection (`F-05` upstream feeder + `F-06` device-level input fuse).
6. Big 3 alternator-upgrade path is purchase-later; this diagram captures the current stock-alternator-first architecture.

## Completion Status
- DC/PV topology is complete for current BOM scope and load model scope.
- AC hierarchy is now complete at architecture level, including transfer behavior, branch strategy, and protection chain.
- Remaining work is SKU-level part lock and run-length field validation for the now-locked AC/USB architecture.
