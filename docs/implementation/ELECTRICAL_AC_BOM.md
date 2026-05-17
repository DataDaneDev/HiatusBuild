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

As-of date: `2026-05-16`

Purpose: maintain the purchased Phase 1 AC architecture baseline: portable `30A` EMS, `30A` shore inlet/cord, one `6-way` DIN enclosure, `30A` AC-in breaker, `30A` AC-out main breaker, and two active `20A` GFCI-protected AC-out branches. Final physical outlet locations and enclosure access remain measurement-gated in the installed camper.

Related docs:
- `docs/implementation/ELECTRICAL_overview_diagram.md`
- `docs/core/SYSTEMS.md`
- `docs/core/TRACKING.md`
- `bom/bom_estimated_items.csv`

## Locked AC Architecture

### AC-in chain (shore to inverter)
- `shore source/adapters -> portable 30A EMS -> 30A shore cord -> L5-30 shore inlet -> combined 6-way AC DIN enclosure -> 30A UL489 AC-in breaker/disconnect -> MultiPlus AC-in (L/N/PE)`
- AC-in conductors are `10 AWG` / `10/3` on the protected AC-in path (`30A` hardware basis).
- MultiPlus input current limit is set to actual source (`15A`, `20A`, or `30A`) when adapters are used.

### AC-out chain (inverter-backed branch distribution)
- `MultiPlus AC-out-1 -> 10/3 feeder -> combined 6-way AC DIN enclosure -> 30A UL489 AC-out main breaker -> 20A branch 1 + 20A branch 2 -> GFCI receptacle per branch`
- Current purchased receptacle plan is `2` active GFCI receptacles total. Prior downstream non-GFCI receptacle locations are obsolete unless a later layout revision reopens them.
- AC-out branch hardware is not required to perform the initial AC-in-only battery charging test, but it is now included in the purchased Phase 1 cart.

### Neutral and ground handling
- AC-in and AC-out neutral termination paths remain isolated.
- Separate AC-in neutral pass-through/termination and AC-out neutral bar are required inside the combined enclosure.
- Common equipment grounding/PE bus is acceptable; do not use it as a neutral.
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
| Shore inlet | `1` | `30A 125V` L5-30 shore inlet with exterior cover | `107` | Purchased |
| Shore cord + household adapter | `1` cord + `1` dogbone | `30A` TT-30P-to-L5-30R cord plus `15A` household dogbone adapter | `108` | Purchased |
| Portable EMS/surge protector | `1` | Portable `30A` EMS with open-neutral/polarity/voltage protection | `123` | Purchased |
| AC-in breaker/disconnect | `1 of 2` | DIN-mount `UL 489` `1-pole 30A 120VAC` | `13` | Purchased |
| Combined AC DIN enclosure and bus hardware | `1` enclosure + accessories | `6-way` DIN enclosure; physically isolate AC-in and AC-out neutrals | `109`, `14` | Purchased |
| Shore + AC-in feed cable | as routed | `10/3` stranded tinned-copper cable for `C-28/C-29` (`30A` path) | `114` | Purchased |
| Shore-inlet seal/bedding consumables | per install | Butyl bedding + compatible exterior polyurethane perimeter/finish seal | `179`, `180` | Purchased |
| Strain relief/grommets/clamps/labels/ferrules | per entries | Sized for selected cable/enclosure terminals | `38`, `41`, `43`, `44`, `45` | Cable glands on hand; ferrule kit purchased |

### Full AC-out distribution / final Phase 1 branch hardware

| Component class | Qty | Rating/listing requirement | BOM row(s) | Phase 1 status |
| --- | --- | --- | --- | --- |
| Shore inlet | `1` | `30A 125V` L5-30 shore inlet with exterior cover | `107` | Purchased |
| Shore cord + household adapter | `1` cord + `1` dogbone | `30A` TT-30P-to-L5-30R cord plus `15A` household dogbone adapter | `108` | Purchased |
| Portable EMS/surge protector | `1` | Portable `30A` EMS used source-side before the shore cord | `123` | Purchased |
| AC-in breaker/disconnect | `1` | DIN-mount `UL 489` `1-pole 30A 120VAC` | `13` | Purchased |
| AC-out main breaker | `1` | DIN-mount `UL 489` `1-pole 30A 120VAC`, ahead of branch breakers | `13` | Purchased |
| Combined DIN enclosure | `1` | `6-way` DIN enclosure with slot plan: `30A in`, `30A out`, `20A`, `20A`, `2x` blank/spare | `109` | Purchased |
| AC-out branch breaker set | `2` active | DIN-mount `UL 489` branch breakers: `20A` + `20A` | `110` | Purchased |
| DIN accessory kit | `1` kit | Neutral isolation hardware, PE/ground bus support, ferrules, labels/blanks as needed | `14`, `41` | Purchased / labels-blanks confirm on hand |
| GFCI receptacles | `2` | `20A` self-test GFCI receptacles, one per active branch | `15` | Purchased |
| Standard downstream receptacles | `0` in current scope | Prior downstream non-GFCI receptacle plan is obsolete | `111` | Obsolete |
| Outlet boxes + covers/faceplates + clamps | `2` sets | Two active GFCI receptacles have covers/plates; final boxes/clamps are install-fit details using on-hand hardware as needed | `112` | Install-fit detail / not a first-charge blocker |
| AC branch cable | `30 ft` purchased | `12/3` stranded triplex branch cable (`C-31/C-32`) | `113` | Purchased |
| Shore + AC-in/AC-out feeder cable | `20 ft` purchased | `10/3` stranded triplex for `C-28/C-29/C-30` (`30A` paths) | `114` | Purchased |
| Strain relief/cable glands | per enclosure entries | Use assorted on-hand entry hardware sized during physical layout | `44` | On-hand fitment stock |
| Grommets | per pass-through points | Abrasion protection at penetrations, selected hands-on during routing | `43` | On-hand / install fit |
| P-clamps and retention hardware | per route | Cable support and vibration control, selected hands-on during routing | `45` | On-hand / install fit |
| Loom/sleeving | per exposed runs | Harness abrasion protection | `42` | Required |
| Heat shrink (adhesive) | install consumable | Termination sealing and strain relief support | `38` | Required |
| Ferrules/terminals (AC-relevant) | install consumable | Sized to `10 AWG` and `12 AWG` terminations as required by device terminals | `41`, `116` | Required |
| AC-out-2 branch breaker/protection hardware | `0` in Phase 1 | Reserve-only route, no energized branch hardware in this phase | N/A | Reserve-only (not procured) |

## Manual AC Validation Checklist

### 0) AC-in-only initial charger validation
- Confirm AC-in physical order: `shore source/adapters -> portable EMS -> shore cord -> inlet -> AC-in breaker/disconnect -> MultiPlus AC-in`.
- Confirm AC-out breakers/loads are disconnected or not yet installed for the first battery-charge test.
- Confirm MultiPlus input current limit is set to actual source (`15A`, `20A`, or `30A`).
- Confirm battery charge profile is intentionally set for the selected LiFePO4 voltage basis before energization.
- Confirm AC-in and AC-out neutral paths are not mixed.

Use this checklist as the acceptance gate before procurement freeze and before first live AC commissioning.

### 1) Topology integrity
- Confirm one unique AC-in chain exists: `shore source/adapters -> portable EMS -> cord -> inlet -> AC-in breaker -> MultiPlus AC-in`.
- Confirm one unique AC-out-1 chain exists: `MultiPlus AC-out-1 -> 30A AC-out main -> 20A branch breakers -> GFCI receptacles`.
- Confirm `AC-out-2` is documented as reserve-only and not active in Phase 1 procurement.
- Confirm current receptacle count is locked to `2` active GFCI receptacles unless a later layout revision reopens downstream receptacles.

### 2) Protection coordination
- Confirm AC-in breaker is `30A` and AC-in conductors are `10 AWG`.
- Confirm AC-out main breaker is `30A` and the MultiPlus-to-enclosure feeder is `10 AWG`.
- Confirm branch OCP values are `20A` and `20A` with `12 AWG` branch conductors.
- Confirm breaker listing basis is `UL 489` (or equivalent NRTL listing) for branch/feeder use.

### 3) Neutral/ground correctness
- Confirm AC-in and AC-out neutral paths are isolated.
- Confirm input and output neutral paths are separately landed/passed through inside the combined enclosure.
- Confirm the equipment grounding/PE path is common and continuous.
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
- Purchased SKU lock is recorded in `bom/bom_estimated_items.csv` for rows `13`, `14`, `15`, `41`, `107`, `108`, `109`, `110`, `113`, `114`, `123`, `179`, and `180`. Row `181` was same-order tire-deflator/off-road support hardware and is intentionally outside AC scope.
- Row `111` is obsolete under the current `2x` GFCI-receptacle plan. Row `112` is only an install-fit box/cover/clamp detail around the two active GFCIs, not an AC design blocker.
- Current utilization note (`2026-05-16`): AC protection chain and purchase scope are locked for a `30A` system with two active `20A` branches. Do not add a third active AC branch without revisiting the AC-out main/enclosure/feed plan.
