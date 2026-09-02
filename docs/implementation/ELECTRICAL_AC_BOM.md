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
  - "[[ELECTRICAL_overview_diagram]]"
---

# Electrical AC BOM (Phase 1)

As-of date: `2026-09-02`

Purpose: maintain the installed Phase 1 AC architecture baseline: portable `30A` EMS, `30A` shore inlet/locking cord with modular `25 ft` TT-30 extension, one `6-way` DIN enclosure, `30A` AC-in breaker, `30A` AC-out main breaker, and two active `20A` GFCI-protected AC-out branches. Owner report `2026-09-02`: all `120V` work is in enclosures, including four duplex devices/eight plug positions total; the system has seen regular use; and the MultiPlus is grounded to truck chassis. Physical enclosure count and chassis-ground installation are closed. Final safety acceptance still requires explicit `LINE/LOAD/PE` proof, downstream protection, GFCI trip/reset in inverter and accepted-shore modes, polarity/neutral-isolation checks, inspection/continuity proof of the installed MultiPlus bond, the separate shell bond, and representative-load verification.

Related docs:
- `docs/implementation/ELECTRICAL_overview_diagram.md`
- `docs/core/SYSTEMS.md`
- `docs/core/TRACKING.md`
- `bom/bom_estimated_items.csv`

## Historical provenance
- [INSTALL_MINUS_12_READINESS_PLAN](../plans/INSTALL_MINUS_12_READINESS_PLAN.md) preserves the May 7 install-window AC planning context; this file owns current Phase 1 AC procurement/implementation.

## Historical physical shore-inlet install gate (`2026-07-19`) — closed/superseded by as-built state

- The L5-30 inlet was then purchased but not yet cut into the camper/bed-side interface.
- The electrical module was hard-mounted. The MultiPlus and combined AC breaker enclosure had been removed for the lift and still required remounting at that time.
- From the remounted AC-in breaker endpoint, mock the full `10/3` path to the candidate exterior inlet with required bend radius, cable support, drip/water management, service loop, strain relief, and access to both sides of the cut.
- Any small cable opening through the plywood electrical backer requires a correctly sized grommet/bushing or gland plus independent cable support/strain relief; bare `10/3` must not bear on a raw plywood edge.
- Confirm the exterior cover swing, connector clearance, wall/backing thickness, hidden structure/no-drill zone, butyl bedding land, finish-seal geometry, and a path that does not share the wet-side chase.
- Cut only after the complete inside and outside route is proven. Do not let the easiest exterior location create an inaccessible cable entry or service-obscuring bend behind the electrical module.
## Locked AC Architecture

### AC-in chain (shore to inverter)
- `shore source/adapters -> portable 30A EMS -> optional 25 ft TT-30 extension -> 30A locking shore cord -> L5-30 shore inlet -> combined 6-way AC DIN enclosure -> 30A UL489 AC-in breaker/disconnect -> MultiPlus AC-in (L/N/PE)`
- AC-in conductors are `10 AWG` / `10/3` on the protected AC-in path (`30A` hardware basis).
- MultiPlus input current limit is set to actual source when adapters are used. Use `10A` for first household tests and `12A` maximum policy on a normal `15A` outlet; do not leave the limit at `50A` on adapter/household shore.
- Use the modular extension only when the extra reach is needed. Fully seat, elevate, and weather-protect the TT-30 midpoint connection, and uncoil both cords under load.

### AC-out chain (inverter-backed branch distribution)
- `MultiPlus AC-out-1 -> 10/3 feeder -> combined 6-way AC DIN enclosure -> 30A UL489 AC-out main breaker -> 20A Branch A + 20A Branch B -> GFCI receptacle per branch`
- The two first-in-chain receptacles are `20A` self-test GFCIs: Branch A = office/driver side, Branch B = Galley/passenger side. Owner report `2026-09-02`: each GFCI feeds one downstream duplex from its `LOAD` side, all four devices are enclosed, and AC has seen regular use. Formal electrical acceptance remains open only for the explicit safety/functional checks below.
- Do not reopen the box-count task. Confirm `12 AWG`, `LINE/LOAD/PE`, PE continuity, labels, GFCI trip/reset, whole-chain downstream protection, polarity/neutral isolation, and representative loads in inverter and accepted-shore modes.
- AC-out branch hardware is not required to perform the initial AC-in-only battery charging test, but it is now included in the purchased Phase 1 cart.

### Neutral and ground handling
- AC-in and AC-out neutral termination paths remain isolated.
- Separate AC-in neutral pass-through/termination and AC-out neutral bar are required inside the combined enclosure.
- Common equipment grounding/PE bus is acceptable; do not use it as a neutral.
- Continuous equipment ground path and chassis bond are required end-to-end. The installed MultiPlus-II `48/3000/35-50 120V` is a Class I device; its official manual identifies the external `M6` connection as the primary PE point, requires at least `4 mm²` grounding conductor, and explicitly requires the casing to be connected to the vehicle chassis in a mobile shore-power installation. Owner report `2026-09-02`: the MultiPlus is grounded to truck chassis. Verify at the next de-energized inspection that the installed bond originates at the external `M6 PE` lug, uses at least `4 mm²` / selected `10 AWG` green stranded copper with suitable terminations, and lands at a sound chassis point; do not use the aluminum Hiatus shell or 80/20 as the only protective-earth path.
- Bond the aluminum camper shell separately into the same chassis/equipment-ground network with a corrosion-compatible connection. Treat shell hardware/body contact as unproven until low-resistance continuity is measured; use compatible/tinned terminals and antioxidant/isolation practice appropriate to the aluminum interface.
- Do not jumper the MultiPlus case/PE lug to Lynx negative or the `12V` negative bus. The `48V` and `12V` DC return paths remain on their dedicated conductors/buses; Mechman case-ground behavior is a separate commissioning check that may establish the single deliberate house-negative-to-chassis reference through the alternator and its dedicated `2/0` return.
- Do not add an always-bonded downstream neutral-ground bond in branch receptacle wiring. Leave the MultiPlus internal ground relay enabled for the normal single-unit topology: it bonds AC-out neutral to chassis in inverter mode and opens that bond when shore AC is accepted.

### AC-out-2 policy
- `AC-out-2` is **reserve-only** in Phase 1.
- Keep labeled panel space and capped route only; no energized branch hardware is procured for this path in Phase 1.

## Required Purchasable Components (Phase 1)

### Immediate AC-in-only initial charge path

These rows unblock safe MultiPlus shore charging and should not wait on final receptacle count:

| Component class | Qty | Rating/listing requirement | BOM row(s) | Phase 1 status |
| --- | --- | --- | --- | --- |
| Shore inlet | `1` | `30A 125V` L5-30 shore inlet with exterior cover | `107` | Purchased |
| Shore cord, modular extension + household adapter | `1` locking cord + `1` extension + `1` dogbone | `30A` TT-30P-to-L5-30R cord, `25 ft` TT-30P-to-TT-30R extension, and `15A` household dogbone adapter | `108`, `340`, `281` | Purchased |
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
| Shore cord, modular extension + household adapter | `1` locking cord + `1` extension + `1` dogbone | `30A` TT-30P-to-L5-30R cord, `25 ft` TT-30P-to-TT-30R extension, and `15A` household dogbone adapter | `108`, `340`, `281` | Purchased |
| Portable EMS/surge protector | `1` | Portable `30A` EMS used source-side before the shore cord | `123` | Purchased |
| AC-in breaker/disconnect | `1` | DIN-mount `UL 489` `1-pole 30A 120VAC` | `13` | Purchased |
| AC-out main breaker | `1` | DIN-mount `UL 489` `1-pole 30A 120VAC`, ahead of branch breakers | `327` | Purchased |
| Combined DIN enclosure | `1` | `6-way` DIN enclosure with slot plan: `30A in`, `30A out`, `20A`, `20A`, `2x` blank/spare | `109` | Purchased |
| AC-out branch breaker set | `2` active | DIN-mount `UL 489` branch breakers: `20A` + `20A` | `110`, `330` | Purchased |
| DIN accessory kit | `1` kit | Neutral isolation hardware, PE/ground bus support, ferrules, labels/blanks as needed | `14`, `41` | Purchased / labels-blanks confirm on hand |
| MultiPlus/chassis and shell bonding materials | field-measured | Owner confirms MultiPlus-to-truck-chassis ground installed; verify `M6 PE`, conductor, termination, endpoint, and continuity. Separate shell bond jumper; M6/tinned lugs, protected chassis attachment, compatible aluminum-interface hardware/compound | `51`, `339` | Chassis ground installed; shell bond inventory/buy |
| GFCI receptacles | `2` | `20A` self-test GFCI receptacles, one per active branch | `15` | Purchased |
| Standard downstream receptacles | `2` installed / owner-reported | One downstream duplex from each first GFCI `LOAD`, same `12 AWG` branch, accessible listed box | inactive historical `111`; installed inventory source not yet reconciled | Inspect/test as-built |
| Outlet boxes + covers/faceplates + clamps | `4` installed device sets / owner-reported | Six `14 cu in` old-work boxes were purchased; prove each used device's listed box, compatible cover/plate and clamp, conductor fill, wall-stack fit, and service access | active row `112` plus inventory | Physical acceptance open |
| AC branch cable | `30 ft` purchased | `12/3` stranded triplex branch cable (`C-31/C-32`) | `113` | Purchased |
| Shore + AC-in/AC-out feeder cable | `20 ft` purchased | `10/3` stranded triplex for `C-28/C-29/C-30` (`30A` paths) | `114` | Purchased |
| Strain relief/cable glands | per enclosure entries | Use assorted on-hand entry hardware sized during physical layout | `44` | On-hand fitment stock |
| Grommets | per pass-through points | Abrasion protection at penetrations, selected hands-on during routing | `43` | On-hand / install fit |
| P-clamps and retention hardware | per route | Cable support and vibration control, selected hands-on during routing | `45` | On-hand / install fit |
| Loom/sleeving | per exposed runs | Harness abrasion protection | `42` | Required |
| Heat shrink (adhesive) | install consumable | Termination sealing and strain relief support | `38` | Required |
| Ferrules/terminals (AC-relevant) | install consumable | Sized to `10 AWG` and `12 AWG` terminations as required by device terminals | `41`, `116` | Required |
| AC-out-2 branch breaker/protection hardware | `0` in Phase 1 | Reserve-only route, no energized branch hardware in this phase | N/A | Reserve-only (not procured) |

## First-Live AC-In Test Result (`2026-05-27`)
- AC Input 1 should be labeled `Shore power` for this mobile/source-current-limited system.
- MultiPlus switch `II` is charger-only; switch `I` is inverter/charger normal mode; `O` is off.
- Short shore test passed with household-source current limiting: about `1294W` shore input and about `54.3V x 21.6A` (`~1173W`) battery charge in bulk.
- Current disconnect practice: connect RV/EMS/load side first, then energize shore; disconnect in reverse by de-energizing/unplugging shore source before disconnecting the RV side.
- This result does not close battery-charge-profile commissioning. Program/verify the MultiPlus lithium settings before sustained charging.

## Manual AC Validation Checklist

### 0) AC-in-only initial charger validation
- Confirm AC-in physical order: `shore source/adapters -> portable EMS -> optional TT-30 extension -> locking shore cord -> inlet -> AC-in breaker/disconnect -> MultiPlus AC-in`.
- Confirm AC-out breakers/loads are disconnected or not yet installed for the first battery-charge test.
- Confirm MultiPlus input current limit is set to actual source (`10A` first household test, `12A` max on normal `15A`, actual rating for `20A`/`30A`).
- Confirm AC Input 1 is labeled/configured as `Shore power`.
- Confirm battery charge profile is intentionally set for the selected LiFePO4 voltage basis before sustained charging.
- Confirm AC-in and AC-out neutral paths are not mixed.

Use this checklist as the continuing acceptance gate before sustained shore charging, AC-out branch energization, or any AC enclosure closeout.

### 1) Topology integrity
- Confirm one unique AC-in chain exists: `shore source/adapters -> portable EMS -> cord -> inlet -> AC-in breaker -> MultiPlus AC-in`.
- Confirm one unique AC-out-1 chain exists: `MultiPlus AC-out-1 -> 30A AC-out main -> 20A branch breakers -> GFCI receptacles`.
- Confirm `AC-out-2` is documented as reserve-only and not active in Phase 1 procurement.
- Confirm the two first-in-chain GFCIs remain the only branch-origin devices and each owner-reported downstream duplex is fed only from its corresponding GFCI `LOAD`; prove compatible listed boxes/covers/clamps, conductor fill/accessibility, and whole-chain testing.

### 2) Protection coordination
- Confirm AC-in breaker is `30A` and AC-in conductors are `10 AWG`.
- Confirm AC-out main breaker is `30A` and the MultiPlus-to-enclosure feeder is `10 AWG`.
- Confirm branch OCP values are `20A` and `20A` with `12 AWG` branch conductors.
- Confirm breaker listing basis is `UL 489` (or equivalent NRTL listing) for branch/feeder use.

### 3) Neutral/ground correctness
- Confirm AC-in and AC-out neutral paths are isolated.
- Confirm input and output neutral paths are separately landed/passed through inside the combined enclosure.
- Confirm the equipment grounding/PE path is common and continuous.
- Confirm the MultiPlus external `M6 PE` lug is bonded to a verified truck-chassis point with at least `4 mm²` / selected `10 AWG` green stranded copper; the aluminum shell/80/20 is not the sole return.
- Confirm the aluminum shell has its own corrosion-compatible bond to the chassis/equipment-ground network and verify low-resistance continuity after final assembly.
- Confirm no intentional jumper exists from MultiPlus case/PE to Lynx negative or the `12V` negative bus, and confirm no chassis path bypasses the SmartShunt after the Mechman ground style is physically identified.
- Confirm no fixed downstream neutral-ground bond is added in branch receptacle wiring.
- Confirm the MultiPlus internal ground relay remains enabled for this normal single-unit mobile topology; test both GFCI branches in inverter mode and on accepted shore power before routine use.

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
- Purchased SKU lock is recorded in `bom/bom_estimated_items.csv` for rows `13`, `327`, `14`, `15`, `41`, `107`, `108`, `109`, `110`, `112`, `330`, `113`, `114`, `123`, `179`, and `180`. Rows `13`/`327` are the AC-in/AC-out `30A` pair; rows `110`/`330` are the two `20A` branch breakers. Row `112` is the purchased old-work box six-pack, not evidence that six downstream devices are approved. Row `181` was same-order tire-deflator/off-road support hardware and is intentionally outside AC scope.
- Inactive BOM row `111` preserves the formerly closed downstream-receptacle concept. Row `112` supplied the six purchased old-work boxes. Owner report `2026-08-27` closes physical device count at two GFCIs plus two downstream duplexes; installed receptacle/cover/clamp inventory provenance and all box-fill/wall-stack/accessibility/testing gates remain open.
- Current utilization note (`2026-05-16`): AC protection chain and purchase scope are locked for a `30A` system with two active `20A` branches. Do not add a third active AC branch without revisiting the AC-out main/enclosure/feed plan.
