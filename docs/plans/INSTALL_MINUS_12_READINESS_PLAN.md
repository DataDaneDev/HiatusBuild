# May 7 Install Readiness and Immediate Post-Install Plan

As-of date: `2026-04-27`

Purpose: one practical planning document for the remaining days before the Hiatus install, the May 7 install day, and the first post-install actions. This replaces the narrower install-minus-12 plan.

Install appointment:

- Date/time: Thursday, May 7, 2026 at `9:00 AM`
- Location: `3171 Mercer Ave, Suite 101, Bellingham, WA 98225`
- Starting point: Park City, Utah
- Work time off: May `7-11`

## Current owner-confirmed state

### Truck bed / flooring

- EPS is installed against the truck bed under the subfloor, but some foam still needs cleaner trimming.
- `3/4 in` sealed plywood subfloor is installed in three slices over the EPS/rib structure.
- Plywood top face remains unsealed so the Lonseal adhesive can bond correctly.
- Lonseal sheet flooring and adhesive are in hand.
- Immediate missing flooring tool: exact-notch sheet-vinyl adhesive trowel, BOM row `174`.
- Once Lonseal is glued down, subfloor removal becomes materially harder, especially if the sheet bridges all three plywood slices.

### Truck bed sealing / install interface

- Bed rail caps still need to be removed and sealed under/around as appropriate.
- Prior owner cut roughly `2 in x 3 in` square holes in the top of the bed rails for a previous camper install.
- Those holes are now dust/water intrusion risks because the barn-door camper upgrade makes the rear enclosure much tighter.
- Tailgate must remain removable for barn-door camper use; working plan is to keep it on for the drive to Bellingham, then remove at/near Hiatus if required.
- Tonneau cover should stay on as long as practical for weather protection, then be removed if it interferes with the install.

### Electrical / charging

- Most electrical components are physically laid out on the garage floor on uncut `1/2 in` plywood.
- No final wire cuts are made yet.
- Fuses still need to be physically matched to their devices/holders before energization.
- Shore power remains the highest-leverage near-term unblocker because it enables safe initial charging and bench testing of the `3x 48V 100Ah` battery bank.
- Mechman `48V` alternator kit and Balmar `APM-48` are received, but alternator install remains deferred until the battery bank, shore charging, and monitoring path are proven.

### Layout / cabinetry / plumbing

- Iceco fridge and water tank dry fit invalidated the prior CAD location: the cooler/fridge did not open where planned.
- Current working assumption: fridge/cooler likely moves to the front-left corner, which makes existing furniture CAD reference-only.
- Aluminum extrusion needs to be ordered soon, but exact cut lengths should not be ordered from stale CAD.
- A faucet is now a missing discrete purchase item.
- Hot water remains unresolved: electric tanked may be viable later, electric tankless is not realistic on the current inverter scale, and portable propane should be treated as outdoor-use-only unless a specific unit is listed for enclosed/RV use.

## Priority triage

### Must complete before install / departure

1. **Travel and logistics gate**: stage the truck near Bellingham by the evening of May 6; do not plan to drive from Park City the morning of the 9 AM install.
2. **Shore AC-in / initial-charge path**: SKU-lock or order enough AC-in hardware to safely power the MultiPlus charger.
3. **Electrical safety prep**: lay out the electrical closet, match fuses to devices, label circuits, and write the first-charge checklist before energizing anything.
4. **Truck bed weather/dust prep**: inspect/seal bed rail caps and old `2 in x 3 in` holes without interfering with Hiatus install surfaces.
5. **Flooring gate**: trim EPS and verify subfloor fit; do not glue Lonseal until all access/penetration/hardpoint questions are cleared or explicitly deferred.
6. **Install-day measurement kit**: have a phone/print checklist for dimensions, hardpoints, passthrough candidates, and module envelopes.

### Should complete before install

1. Place a low-regret extrusion + connector starter order for rough module frames.
2. Redo CAD as block envelopes for fridge/tank/electrical/galley, not final furniture.
3. Split faucet/cold-water plumbing from the final water-heater decision so sink/pump/tank work can progress.
4. Stage travel/install kits: sealant/weather kit, tailgate removal kit, labels, measurement tools, fuse/fastener spares.

### Defer

1. Mechman alternator installation and live engine charging.
2. Final solar panel/string procurement; preserve passthrough routing only.
3. Final drawer fronts, finished panels, cosmetic skins, and exact drawer-slide lengths.
4. Indoor propane water-heater path unless listed unit, venting, combustion air, and clearances are locked.
5. Permanent Lonseal glue-down if any floor penetrations, underfloor routing, or hardpoints are unresolved.

## Shore power / initial charge plan

### Locked architecture

Keep the split AC architecture:

```text
shore source -> cord/adapter -> TT-30 inlet -> hardwired EMS -> AC-in breaker/disconnect -> MultiPlus-II AC-in
MultiPlus-II AC-out-1 -> separate AC-out branch enclosure -> galley/office branch protection
```

Rules:

- Do not combine AC-in and AC-out protection in the same undifferentiated breaker box.
- AC-in breaker/disconnect is required before MultiPlus AC-in.
- AC-out branch breakers/receptacles are not required to charge batteries.
- Keep AC-in and AC-out neutrals isolated in their respective enclosures.
- Do not add a fixed downstream neutral-ground bond in branch wiring.

### Near-term deliverable: AC-in-only charging mode

For the immediate garage path, build and test only the safe minimum path required to charge batteries through the MultiPlus:

```text
shore source -> cord/adapter -> inlet -> EMS -> AC-in breaker/disconnect -> MultiPlus AC-in -> MultiPlus DC -> one 48V battery at a time
```

Must-buy / lock now:

- BOM `107`: shore inlet + weatherproof hatch
- BOM `108`: shore cord + adapter kit
- BOM `123`: hardwired EMS/surge protector
- BOM `13`: AC input breaker/disconnect
- BOM `109`: split DIN enclosures, at least AC-in enclosure needed immediately
- BOM `14`: AC DIN accessory kit: neutral/ground bars, end stops, blanks, labels
- BOM `114`: `10/3` shore + AC-in feed cable
- Confirm enough rows `43-45`, `38`, `41`, and relevant terminals/labels for strain relief, grommets, P-clamps, heat shrink, ferrules, and enclosure entries.

Can defer if only charging batteries:

- BOM `110`: AC-out branch breaker set
- BOM `15`, `111`, `112`: GFCI/downstream receptacles and boxes
- BOM `113`: AC branch cable

### Battery first-charge hold points

Before any live charge:

- MultiPlus LiFePO4 profile is explicitly configured; reconcile repo planning value `56.8V` against battery/manual value `58.4V` before first energization.
- Source current limit is set to actual source: `15A`, `20A`, or `30A`.
- One battery is connected at a time for initial charge/verification.
- Correct Class T and branch fuse values are installed and labeled.
- AC-out loads and alternator branch are disconnected/inactive.
- Pre-charge procedure exists before closing into MultiPlus capacitors.
- Voltage/SOC/temp/current are logged for each battery before paralleling.

## Electrical closet plan

Near-term sequence:

1. Keep the `1/2 in` plywood uncut until the two-board envelope is validated.
2. Paper-template Board A and Board B at `90°`.
3. Place real components or templates: batteries, Class T fuses, main disconnect, Lynx, shunt, MultiPlus, Orion, AC-in/out enclosures, Cerbo/monitoring, 12V fuse block.
4. Mark separate corridors for `48V`, `12V/control`, and `120VAC`; cross at `90°` only where unavoidable.
5. Verify wrench access, bend radius, fuse replacement, label visibility, and service loops.
6. Match every fuse/holder to its device before cutting cable.
7. Pilot drill only after the layout passes service-access checks.
8. Do not cut shell-dependent cable runs yet.

Gate E1 passes when:

- no blocked terminals;
- no buried fuses/disconnects;
- all high-current and AC service points are reachable;
- cable exits are plausible;
- first-charge checklist is written.

## Flooring and truck-bed sealing plan

### Recommended order

1. Remove or partially lift bed rail caps and inspect old camper holes.
2. Confirm with Hiatus that the old `2 in x 3 in` rail holes are not needed for the new camper interface.
3. Clean/degrease rail surfaces and rust-protect bare cut edges.
4. Close holes as dust/weather intrusion points using low-profile, serviceable cover patches where possible:
   - aluminum/ABS/HDPE or similar non-absorbent patch/backer;
   - butyl tape, automotive seam sealer, MS polymer, or polyurethane sealant;
   - avoid expanding foam, brittle household caulk, or proud patches that can interfere with camper fit.
5. Reinstall rail caps with targeted sealing/gasketing while preserving drainage paths.
6. Trim EPS so no foam is proud, buckled, or in structural clamp stacks.
7. Verify plywood panels sit flat and can still be removed intentionally.
8. Dry-fit Lonseal and confirm adhesive/trowel/roller/workspace conditions.
9. Glue Lonseal only after the glue-down gate passes.

### Lonseal glue-down gate

Do not glue until all are true:

- rail/hole sealing is complete or explicitly deferred;
- EPS trim and subfloor seating are verified;
- no floor-through penetrations, anchors, drains, heater routes, or hardpoints need to be added under the finish sheet;
- top plywood face is clean, dry, untreated, and adhesive-compatible;
- correct trowel and roller are on hand;
- cure window is dry and within adhesive requirements;
- reduced serviceability from a one-piece glued sheet is accepted.

## Extrusion / furniture / CAD plan

### Key decision

Treat current furniture CAD as stale/reference-only until the fridge and water tank envelopes are reworked from physical dry fit.

### Starter order strategy

Buy stock-length extrusion and universal hardware, not final cut-to-length furniture.

- Favor `15-series` for heavy/dynamic modules: fridge, water tank, electrical/workstation cabinet.
- Use `10-series` for lighter desk/accessory/panel-retainer work.
- If simplifying, buy `15-series` first and defer most `10-series` until layout is clearer.
- Keep stock sticks under the BOM row `89` shipping threshold (`under 92 in`) where useful.

Reasonable starter order, if budget/storage allow:

- `8x` 15-series sticks at roughly `92 in` (`~61 ft` total)
- `6x` 10-series sticks at roughly `92 in` (`~46 ft` total)
- `300-400` T-nuts and matching button-head bolts split by series
- generous corner brackets, gussets, flat plates, 90-flat brackets, end caps, anti-rattle tape, VHB, spacers/shims

Defer:

- exact drawer-slide lengths;
- drawer fronts;
- panel skins;
- final cosmetic trim;
- any extrusion cut list that depends on stale fridge/tank CAD.

### Layout sequence

1. Measure actual Iceco body, handles, hinge/lid sweep, compressor vent side, and cord exit.
2. Measure actual water tank body and fitting protrusions.
3. Tape/cardboard floor envelopes for front-left fridge/tank candidates.
4. Verify lid opening, slide extension if used, aisle/door clearance, ventilation, tie-downs, and service loops.
5. Re-CAD block envelopes first.
6. Count extrusion by axis only after envelopes pass.

## Plumbing / hot water / propane plan

### Near-term decision

Decouple cold-water galley build from final hot-water decision.

Proceed toward a cold-water baseline:

- tank;
- pump;
- strainer/silencing;
- faucet and sink;
- drain/graywater path;
- service shutoffs;
- capped future hot-water tie-in.

Hot water posture:

- Electric tankless is not compatible with the current inverter scale for shower-class heating.
- Small electric tanked heater may be viable later, but defer until AC branch/source-load behavior is stable.
- Portable propane tankless is the provisional May 7 path only as an outdoor-use appliance.
- Listed indoor/RV propane remains a later option only after unit, venting, combustion air, clearances, and penetrations are locked.

Immediate BOM/procurement gaps:

- add faucet as its own discrete item;
- split sink/drain/graywater package out of generic cabinetry if not already purchased;
- propane regulator/hose/shutoff/QD/leak-test supplies must match the selected appliance manual;
- gas-rated sealant/thread treatment must not be assumed from potable-water PTFE tape.

## Day-by-day schedule

### Mon Apr 27 — reset plan and logistics gate

- Replace the narrow May 7 plan with this integrated plan.
- Confirm install appointment, arrival expectations, and whether Hiatus can remove/store tailgate onsite.
- Confirm route/travel plan so the truck is in Bellingham by May 6 evening.
- Start the single working checklist across electrical, floor, bed sealing, layout, plumbing, and travel.

Gate L0: travel/staging plan is real, not assumed.

### Tue Apr 28 — shore power / initial charge lock

- Lock/order rows `107`, `108`, `123`, `13`, `109`, `14`, `114`.
- Confirm accessories for strain relief, ferrules, labels, neutral/ground bars, and enclosure entries.
- Draft first-charge checklist.
- Decide whether final AC receptacle count is still open, but do not let that block AC-in charging hardware.

Gate S1: AC-in charge path is ordered/SKU-locked and first-charge checklist exists.

### Wed Apr 29 — electrical closet layout + fuse matching

- Complete one real Board A/B layout iteration.
- Match fuse IDs/values/holders to devices.
- Label board zones and cable corridors.
- Keep alternator branch inactive and shell-dependent cuts deferred.

Gate E1: service access and fuse/device matching pass.

### Thu Apr 30 — subfloor / EPS / Lonseal prep

- Trim EPS.
- Verify three plywood slices sit flat and can be removed intentionally.
- Confirm hardpoint pockets have no compressible stack.
- Confirm Lonseal trowel/roller and adhesive conditions.
- Do not glue unless the glue-down gate passes.

Gate F1: subfloor fit and serviceability pass.

### Fri May 1 — truck interface / dust / weather

- Contact Hiatus about tailgate, tonneau, bed rail caps, rail holes, and install interface expectations.
- Stage bed rail sealing kit and weather kit.
- Decide whether to keep tonneau on until Bellingham based on forecast and cure state.

Gate W1: tailgate/tonneau/sealing plan is known.

### Sat May 2 — extrusion and rough modules

- Rework fridge/tank/electrical/galley block envelopes.
- Place starter stock extrusion and connector order.
- Do not buy final panels/drawer slides from unverified dimensions.

Gate X1: enough low-regret extrusion/connectors are ordered to build rough frames after measured install dimensions.

### Sun May 3 — plumbing / propane / faucet path

- Add faucet/sink/drain procurement decisions.
- Pick provisional fridge/tank/faucet/pump zones.
- Treat water heater as provisional outdoor propane or deferred; do not cut indoor propane/vent paths.
- Add install-day measurement prompts for plumbing and propane.

Gate P0: cold-water baseline can proceed without locking final water heater.

### Mon May 4 — final pre-install readiness check

- Verify what is delivered versus merely ordered.
- Pack tools, labels, sealants, fuses, measurement kit, tailgate kit, and weather kit.
- Save install-day measurement list on phone.
- Reconfirm appointment.

Gate R1: blockers are classified as install-blocking, post-install-blocking, or deferrable.

### Tue May 5 — travel / catch-up buffer

- Use as travel or recovery buffer.
- Only finish reversible tasks if still local.
- Do not start anything that can leave the truck half-disassembled.

Gate T1: truck and tools are committed to Bellingham staging.

### Wed May 6 — arrive and stage in Bellingham

- Be in/near Bellingham by evening.
- Check truck bed, tonneau/tailgate state, subfloor state, and install kit access.
- Reconfirm morning arrival instructions.

Gate A1: truck is ready for 9 AM install.

### Thu May 7 — install day

- Arrive early.
- Confirm tailgate handling, bed rail/interface sealing, dust intrusion points, attachment method, and any installer notes before work starts.
- Photograph before/during/after.
- Before leaving, inspect seals, gaps, clearance, door/window/fan operation, attachment points, and visible weather-critical issues.
- Capture measurements for interior width/length/height, door swing, hardpoints, shore/solar passthrough candidates, fridge/tank/cabinet envelopes, and maximum module height.

Gate I1: do not leave with undocumented attachment, clearance, or weather-critical issues.

### Fri May 8 — local shakedown

- Stay local enough to return to Hiatus if needed.
- Drive low-speed and highway loops.
- Reinspect attachment, seal compression, dust/water gaps, doors, windows, fan, tailgate/tonneau implications.
- Transfer measurements into layout notes.

Gate S2: shell is mechanically/weather acceptable after first drive cycle.

### Sat May 9 — service-map freeze

- Use real shell dimensions to freeze electrical closet footprint, battery/service access, shore inlet candidate, solar passthrough reserve, fridge/tank positions, and plumbing/propane routes.
- Dry-place modules or cardboard envelopes.
- Do not cut final penetrations unless the service map is conflict-free.

Gate M1: no penetrations until layout and service map have no major conflicts.

### Sun May 10 — reversible-first post-install work

- Reconfirm floor stack and Lonseal glue-down decision against real camper install state.
- Start only reversible rough-in prep: labels, cable chase planning, module cut planning, plumbing mock routing.
- Build punch list by risk.

Gate C0: no permanent closure, glue, skins, or hidden routing before rough-in/service access validation.

### Mon May 11 — return / buffer / top-off orders

- Use as return travel, installer follow-up, emergency parts, or second shakedown buffer.
- Place top-off orders based on real dimensions.
- Update logs and tracking from install-window evidence.

Gate H1: home build resumes with real dimensions, punch list, and no unresolved safety-critical install issue.

## Install-day measurement checklist

Capture before leaving Hiatus or immediately after:

- true interior width at floor, bed rail height, and upper wall line;
- usable length and cabover/door constraints;
- door swing and entry obstruction envelope;
- window/latch/hinge interference zones;
- camper attachment and tie-down/hardpoint locations;
- floor datum, threshold, slope, and any step changes;
- shore inlet candidate locations;
- solar passthrough candidate locations and roof travel constraints;
- propane/fuel/heater routing candidates;
- water tank, fridge, sink, and pump service envelopes;
- cabinetry anchor candidates;
- maximum safe module height below bed/cabover/roof movement envelope.

## Global hold points

- No alternator install until batteries, shore charge, and monitoring are proven.
- No permanent shell penetrations until service map is frozen.
- No Lonseal glue-down until floor/rail/penetration gate passes.
- No final cabinet skins/drawers before real dimensions are captured.
- No indoor propane water-heater path without listing, venting, combustion air, clearances, detector layout, and leak-test plan.
- No battery paralleling until each 48V battery has been individually charged/tested and voltage/SOC matching is documented.
