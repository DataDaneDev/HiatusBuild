---
aliases:
  - Electrical AC BOM
tags:
  - hiatus/implementation
  - hiatus/electrical
status: active
related:
  - "[[SYSTEMS]]"
  - "[[ELECTRICAL_48V_ARCHITECTURE]]"
  - "[[INSTALL_MINUS_12_READINESS_PLAN]]"
---

# Electrical AC BOM (Phase 1)

As-of date: `2026-04-27`

Purpose: maintain the compact split-panel AC architecture baseline and procurement scope for Phase 1, with immediate emphasis on an AC-in-only MultiPlus shore-charge path for initial `48V` battery charging and later AC-out branch distribution.

Related docs:
- `docs/implementation/ELECTRICAL_overview_diagram.md`
- `docs/core/SYSTEMS.md`
- `docs/core/TRACKING.md`
- `bom/bom_estimated_items.csv`

## Locked AC Architecture

### AC-in chain (shore to inverter)
- `shore source -> shore cord/adapter -> TT-30 inlet -> hardwired EMS -> AC-in DIN enclosure -> 30A UL489 breaker/disconnect -> MultiPlus AC-in (L/N/PE)`
- AC-in conductors are `10 AWG` on the protected AC-in path (`30A` hardware basis).
- MultiPlus input current limit is set to actual source (`15A`, `20A`, or `30A`) when adapters are used.

### AC-out chain (inverter-backed branch distribution)
- `MultiPlus AC-out-1 -> AC-out DIN enclosure -> 20A branch + 15A branch -> first GFCI receptacle per branch -> downstream standard receptacle`
- Receptacle plan is pending final physical layout lock at `3-4` locations total (working baseline remains `4`: `2` galley, `2` office).
- AC-out branch hardware is not required to perform the initial AC-in-only battery charging test.

### Neutral and ground handling
- AC-in and AC-out neutral termination paths remain isolated.
- Dedicated neutral bar is used in each AC enclosure.
- Dedicated ground bar is used in each AC enclosure.
- Continuous equipment ground path and chassis bond are required end-to-end.
- Do not add an always-bonded downstream neutral-ground bond in branch receptacle wiring.

### AC-out-2 policy
- `AC-out-2` is **reserve-only** in Phase 1.
- Keep labeled panel space and capped route only; no energized branch hardware is procured for this path in Phase 1.

## Required Purchasable Components (Phase 1)

### Immediate AC-in-only initial charge path

These rows unblock safe MultiPlus shore charging and should not wait on final receptacle count:

| Component class | Qty | Rating/listing requirement | BOM row(s) | Phase 1 status |
| --- | --- | --- | --- | --- |
| TT-30 shore inlet + weatherproof hatch | `1` | RV `30A` shore interface, weatherproof exterior hardware | `107` | Required now |
| Shore cord + adapters (`TT-30` to `15A/20A`) | `1` kit | `30A` shore cord plus adapter set for mixed-source hookups | `108` | Required now |
| Hardwired EMS/surge protector | `1` | Hardwired `120VAC` EMS in shore path with open-neutral/polarity/voltage fault protection | `123` | Required now |
| AC-in breaker/disconnect | `1` | DIN-mount `UL 489` (or ETL/NRTL equivalent) `1-pole 30A 120VAC` | `13` | Required now |
| AC-in DIN enclosure and accessory hardware | `1` enclosure + accessories | DIN enclosure, rail, cover, neutral/ground bars, end stops, blanks, labels | `109`, `14` | Required now |
| Shore + AC-in feed cable | `11 ft` baseline | `10/3` stranded cable for `C-28/C-29` (`30A` path) | `114` | Required now |
| Strain relief/grommets/clamps/labels/ferrules | per entries | Sized for selected cable/enclosure terminals | `38`, `41`, `43`, `44`, `45` | Confirm on hand |

### Full AC-out distribution / final Phase 1 branch hardware

| Component class | Qty | Rating/listing requirement | BOM row(s) | Phase 1 status |
| --- | --- | --- | --- | --- |
| TT-30 shore inlet + weatherproof hatch | `1` | RV `30A` shore interface, weatherproof exterior hardware | `107` | Required |
| Shore cord + adapters (`TT-30` to `15A/20A`) | `1` kit | `30A` shore cord plus adapter set for mixed-source hookups | `108` | Required |
| Hardwired EMS/surge protector | `1` | Hardwired `120VAC` EMS in shore path with open-neutral/polarity/voltage fault protection | `123` | Required |
| AC-in breaker/disconnect | `1` | DIN-mount `UL 489` (or ETL/NRTL equivalent) `1-pole 30A 120VAC` | `13` | Required |
| Split DIN enclosure set (`AC-in` + `AC-out`) | `2` enclosures | Compact DIN enclosures with rail and cover hardware | `109` | Required |
| AC-out branch breaker set | `2` active + `1` spare position plan | DIN-mount `UL 489` (or ETL/NRTL equivalent): `20A` + `15A` | `110` | Required |
| DIN accessory kit | `1` kit | Input/output neutral bars, input/output ground bars, hot feed distribution block, DIN end-stops, blank fillers, labels | `14` | Required |
| GFCI receptacles (first outlet each branch) | `2` | `120VAC` GFCI receptacles for first outlet on each branch | `15` | Required |
| Standard downstream receptacles | `1-2` duplex | `120VAC` duplex receptacles for GFCI load-side downstream points | `111` | Required (final count pending) |
| Outlet boxes + covers/faceplates + clamps | `3-4` sets | Boxes and covers sized for branch cable method | `112` | Required (final count pending) |
| AC branch cable | `35 ft` baseline | `12 AWG` stranded AC branch cable (`C-30/C-31/C-32`) | `113` | Required |
| Shore + AC-in feed cable | `11 ft` baseline | `10/3` stranded cable for `C-28/C-29` (`30A` path) | `114` | Required |
| Strain relief/cable glands | per enclosure entries | Entry hardware sized to `10/3` and branch cable ODs | `44` | Required |
| Grommets | per pass-through points | Abrasion protection at penetrations | `43` | Required |
| P-clamps and retention hardware | per route | Cable support and vibration control | `45` | Required |
| Loom/sleeving | per exposed runs | Harness abrasion protection | `42` | Required |
| Heat shrink (adhesive) | install consumable | Termination sealing and strain relief support | `38` | Required |
| Ferrules/terminals (AC-relevant) | install consumable | Sized to `10 AWG` and `12 AWG` terminations as required by device terminals | `41`, `116` | Required |
| AC-out-2 branch breaker/protection hardware | `0` in Phase 1 | Reserve-only route, no energized branch hardware in this phase | N/A | Reserve-only (not procured) |

## Manual AC Validation Checklist

### 0) AC-in-only initial charger validation
- Confirm AC-in physical order: `shore source -> cord/adapter -> inlet -> EMS -> AC-in breaker/disconnect -> MultiPlus AC-in`.
- Confirm AC-out breakers/loads are disconnected or not yet installed for the first battery-charge test.
- Confirm MultiPlus input current limit is set to actual source (`15A`, `20A`, or `30A`).
- Confirm battery charge profile is intentionally set for the selected LiFePO4 voltage basis before energization.
- Confirm AC-in and AC-out neutral paths are not mixed.

Use this checklist as the acceptance gate before procurement freeze and before first live AC commissioning.

### 1) Topology integrity
- Confirm one unique AC-in chain exists: `shore source -> cord/adapter -> inlet -> EMS -> AC-in breaker -> MultiPlus AC-in`.
- Confirm one unique AC-out-1 chain exists: `MultiPlus AC-out-1 -> branch breakers -> receptacle chains`.
- Confirm `AC-out-2` is documented as reserve-only and not active in Phase 1 procurement.
- Confirm final receptacle count is explicitly locked (`3` or `4`) before AC-out branch cart freeze; this is not allowed to block AC-in initial-charge procurement.

### 2) Protection coordination
- Confirm AC-in breaker is `30A` and AC-in conductors are `10 AWG`.
- Confirm branch OCP values are `20A` (galley) and `15A` (office) with `12 AWG` branch conductors.
- Confirm breaker listing basis is `UL 489` (or equivalent NRTL listing) for branch/feeder use.

### 3) Neutral/ground correctness
- Confirm AC-in and AC-out neutral paths are isolated.
- Confirm input and output each have dedicated neutral and ground bars.
- Confirm continuous equipment grounding and chassis bond are documented.
- Confirm no fixed downstream neutral-ground bond is added in branch receptacle wiring.

### 4) Procurement completeness
- Confirm every required AC component class has a BOM row mapping.
- Confirm no AC-critical component exists only as implied text.
- Confirm AC-out-2 hardware remains excluded from Phase 1 carts.

### 5) Documentation parity
- Confirm AC assumptions match across:
  - `docs/implementation/ELECTRICAL_AC_BOM.md`
  - `docs/implementation/ELECTRICAL_overview_diagram.md`
  - `docs/core/SYSTEMS.md`
  - `docs/core/TRACKING.md`
  - `bom/bom_estimated_items.csv`

### 6) Operating scenarios
- AC-in-only initial charge: no AC-out loads connected, MultiPlus charger behavior documented.
- Shore present (`30A` source): pass-through + charging behavior documented.
- Shore present via `15A/20A` adapter: current-limit setting policy documented.
- Shore absent: inverter-backed `AC-out-1` behavior documented.
- GFCI trip/reset behavior per branch is called out for commissioning test.

## Procurement Notes
- DIN rail is a mounting method; breaker listing and rating remain the controlling requirement.
- Lowest-cost listed policy is acceptable only if each selected device has verifiable NRTL listing (`UL` or `ETL`) for intended use.
- Final SKU lock should be recorded in `bom/bom_estimated_items.csv` for rows `13`, `14`, `15`, `107`, `108`, `109`, `110`, `111`, `112`, `113`, `114`, and `123`.
- Reopened utilization note (`2026-03-18`): branch protection chain is locked; final receptacle-count/utilization map still requires final closure.
