# Install-minus-12 Readiness Plan

As-of date: `2026-04-25`

Purpose: compress the remaining pre-Washington work into the few decisions that materially improve build readiness when the camper comes home.

## Current owner-confirmed state

- Mechman `48V` alternator kit appears fit-compatible.
- Mechman kit has been received.
- Balmar `APM-48` has been received.
- Dedicated `48V` alternator installation should wait until the `3x 48V 100Ah` battery bank is present and ready to charge.
- Shore power should be solved before alternator installation because shore charging is the practical first-charge path for the new battery bank.
- The post-Washington goal is to come home with the camper and be ready to start furniture/module build quickly.

## Priority order for the next 12 days

### 1. Shore-power / initial-charge path

This is the highest-leverage near-term decision.

Current locked architecture remains:

`TT-30 inlet -> hardwired EMS -> AC-in breaker/disconnect -> MultiPlus-II AC-in -> 48V battery charging`

Immediate deliverable:

- SKU-lock and order the shore/AC-in path enough to safely charge the 3-battery bank from shore before alternator commissioning.

Critical BOM rows:

- `107` shore power inlet + weatherproof hatch
- `108` shore cord + adapter kit
- `123` hardwired EMS/surge protector
- `13` AC input breaker/disconnect
- `109` AC-in enclosure hardware
- `114` shore + AC-in feed cable
- accessory items: strain reliefs, ferrules/terminals, labels, enclosure grounds/neutrals

Charging reference from `docs/core/SYSTEMS.md`:

- MultiPlus-II charger model basis: `48/3000/35-50`
- Charger planning limit: `35A`
- Approximate bulk power at `56.8V`: `1,988W`
- Ideal bulk recharge from `20%` to `100%`: about `6.18h`
- Ideal bulk recharge from `50%` to `100%`: about `3.86h`

Practical note: real full-charge time will be longer near the top because absorption tapers. For initial battery setup, prioritize safe charging settings, verification, and monitoring over speed.

### 2. Interior extrusion order

Goal: have enough extrusion and connector hardware on hand to begin furniture immediately after camper pickup without pretending exact dimensions are already known.

The order should support a first-pass modular furniture build, not every final accessory.

Minimum pre-order method:

1. Sketch the first two modules only:
   - electrical/workstation cabinet
   - galley/storage module
2. For each module, count frame members by axis:
   - vertical posts
   - front/back horizontal rails
   - left/right depth rails
   - intermediate support rails
3. Add all member lengths in inches.
4. Add `25%` waste/rework allowance.
5. Convert to stock sticks under the shipping threshold noted in BOM row `89` (`under 92 in`).
6. Bias the order toward standard reusable lengths and simple corner hardware.

Ordering posture:

- Buy enough `10-series`/`15-series` extrusion to build rough furniture frames and test ergonomics.
- Do not over-lock final panel dimensions, drawer fronts, or cosmetic skins until the camper is physically measured.
- Buy connector hardware generously: corner brackets, gussets, flat plates, T-nuts, button-head bolts, end caps, panel anti-rattle tape.
- Keep a reserve of short offcuts for brackets, test joints, and adapter plates.

Working assumptions from current docs/BOM:

- BOM row `89`: aluminum extrusion, `10s` and `15s`, full length under `92 in` to save shipping.
- Rows `90-94`: corner brackets, adapters, gussets, flat brackets, and 90-flat brackets.
- Rows `95-97`: spacers/shims, VHB, and foam tape/anti-rattle materials.
- Row `122`: drawer slides remain a dependent choice after module dimensions are known.

### 3. Freeze the first build modules, not the whole interior

Before leaving for Washington, the useful target is not a perfect CAD model. It is a buildable starting kit:

- confirmed shore-charge parts ordered or in hand
- extrusion + bracket hardware ordered
- rough module envelope sketches done
- battery/shore charge checklist drafted
- shell-dependent measurements list ready for pickup day

## Pickup-day measurement list

Capture these before driving home or immediately after:

- true interior width at floor, bed-rail height, and upper wall line
- usable length behind cabover/door constraints
- door swing and entry obstruction envelope
- window/latch/hinge interference zones
- tie-down/hardpoint locations
- floor datum and any slope/step changes
- shore inlet candidate locations
- solar passthrough candidate locations
- cabinetry anchor candidates
- maximum safe module height below bed/cabover/roof movement envelope

## Decision gates

### Gate S1: shore initial-charge readiness

Pass when:

- shore inlet/cord/EMS/breaker/enclosure/feed cable are SKU-locked
- MultiPlus initial charge settings checklist exists
- battery first-charge procedure is written before first energization

### Gate F1: furniture-start readiness

Pass when:

- extrusion order is placed
- enough connector hardware is ordered for rough frames
- first two module envelopes are sketched
- pickup-day measurement list is printed/available on phone

## What not to do yet

- Do not install the Mechman alternator path before the battery bank exists and shore charging/monitoring is ready.
- Do not permanently bond final flooring or close panels before shell-dependent routing is known.
- Do not buy final drawer fronts/cosmetic skins before real camper dimensions are captured.
- Do not let solar final strategy block shore power or furniture-start readiness.
