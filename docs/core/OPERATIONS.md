---
aliases:
  - Hiatus operations
tags:
  - hiatus/core
  - hiatus/operations
status: active
related:
  - "[[PROJECT]]"
  - "[[SYSTEMS]]"
  - "[[TRACKING]]"
  - "[[LOG]]"
---

# Operations

## Document role
- This file owns repeatable operating procedures, inspections, commissioning checks, and field-use checklists.
- Keep architecture rationale and hardware-baseline decisions in the core design docs, not here.
- Keep exact install topology and device-specific build detail in `docs/implementation/`.
- Keep dated work results, measurements, incidents, and test evidence in `logs/LOG.md`.
- Keep decision/risk/open-question state in `docs/core/TRACKING.md`.

## Build and deployment cadence
- Weekly planning update in `docs/core/PROJECT.md`
- Continuous progress notes in `logs/LOG.md`
- Weekly risk/decision review in `docs/core/TRACKING.md`
- Reconcile workbook-derived CSV exports before major purchases (`bom/`)

## Pre-departure checklist (starter)
- Battery SOC and charging paths verified
- Communications primary and fallback validated
- Critical spares onboard (fuses, terminals, core tools)
- Fuse inventory verified against [ELECTRICAL_fuse_schedule](../implementation/ELECTRICAL_fuse_schedule.md) (installed + spare counts)
- Workstation and data gear secured for travel

## Arrival/setup checklist (starter)
- Level/stabilize rig
- Check solar exposure and charging state
- Validate call-quality on primary and fallback links
- Confirm ventilation and thermal baseline

## Maintenance framework (starter)
- Electrical inspection interval: TBD
- Fastener and structure inspection interval: TBD
- Solar cleaning/inspection interval: TBD
- Cable chafe and connector condition checks: TBD

## Safety-critical checks (build + field)
### Pre-energization (after wiring changes)
- Verify correct fuse values/voltage classes against [ELECTRICAL_fuse_schedule](../implementation/ELECTRICAL_fuse_schedule.md).
- Confirm terminal torque marks, busbar covers, and abrasion protection on all high-current runs.
- Confirm `48V` disconnect operation and expected de-energization behavior.
- Confirm `F-11` (`12V` buffer battery main fuse) is installed at source and matches planned amp class.
- Confirm `SW-12V-BATT` switching behavior and labeling (closed = NORMAL operation, open = SERVICE battery isolation).
- Confirm 12V fuse-block main `+`/`-` stud terminations are tight, protected, and not over-stacked beyond hardware guidance.
- Confirm no solder-spliced high-current source joins are present in the 12V source-combine path.
- Confirm Ford `Upfitter #3` is labeled as the manual `WS500` alternator-charge enable/disable control.
- Validate AC branch polarity and GFCI/RCD trip on each outlet branch before normal use.
- Confirm detector status (LP/CO/smoke powered, test function passes, expiration date in range).

### Bench-test (electrical module)
Bench-test intent: validate wiring correctness and basic device behavior (shunt, Orion charger path, inverter/charger) *before* install, using controlled energization and small loads.

- Battery parallel tie: measure each battery voltage before paralleling; bring packs to near-equal voltage/SOC first to avoid large equalization currents.
- Safe energization order (DC): keep `48V` disconnect open and remove Lynx branch fuses; connect negatives first (battery negatives to battery-side negative combine, then to SmartShunt battery side); wire positives to Class T blocks with Class T fuses removed.
- Bank bring-up: insert Class T fuses one-at-a-time (disconnect still open) and confirm expected bank voltage at the battery-side busbar.
- System bring-up: close `48V` disconnect to energize the Lynx bus; then insert Lynx branch fuses one-at-a-time, verifying each branch after insertion.
- MultiPlus inrush: expect capacitor inrush when first energizing the inverter branch; use the pre-charge lead method below and stop if you see abnormal arcing/heating.
- Pre-charge lead baseline (current topology):
1. Preconditions: `F-02` installed, `48V` main disconnect `OFF`, and large `48V` loads/chargers disabled.
2. Lead construction: insulated alligator-clip lead with `100-150 ohm` wirewound resistor (high-power aluminum-shell style; target `>=50W` body). Add a small inline pre-charge fuse (`1-2A`, DC-rated) on the battery-side lead when available.
3. Connection points: bypass the `48V` main disconnect by clipping across its two main studs only (battery-side stud to load/Lynx-side stud).
4. Clip order: connect load-side stud first, then battery-side stud.
5. Wait for pre-charge: hold for several seconds and confirm low differential across disconnect studs (target `<1-2V` when meter is available).
6. Close disconnect: turn main disconnect `ON` while pre-charge lead remains attached.
7. Remove pre-charge lead: remove battery-side clip first, then load-side clip.
8. Do not use bare wire "touch" methods for pre-charge bypass.
- Functional checks: verify SmartShunt reads voltage correctly, Orion outputs stable `12V` under load, MultiPlus inverts correctly into a small known load, and MultiPlus charges correctly when AC-in is applied.
- Alternator-control check (when the secondary alternator path is installed): confirm `Upfitter #3 ON` enables the WS500 brown ignition/enable wire and `Upfitter #3 OFF` disables regulator output before using the main `48V` disconnect as a service step.
- 12V mode checks:
1. Orion-only mode (service validation): open `SW-12V-BATT`, keep Orion active, and verify 12V panel remains stable under expected baseline load.
2. Battery-backed mode (normal operation): close `SW-12V-BATT` and verify shared-junction stability under office + galley USB station loads.
3. Service isolation mode: open `SW-12V-BATT` and verify 12V battery branch is fully isolated while Orion path remains testable.
- Shutdown check: open `48V` disconnect and confirm the system de-energizes as expected; verify no unintended return paths bypass shunt measurement.
- Alternator-fault shutdown rule: if a battery pack trips or alternator charging fault is suspected while the engine is running, switch `Upfitter #3 OFF` first, wait for alternator charge current to collapse, then open the main `48V` disconnect only if full house shutdown is still required.

### Propane-specific checks
- Tank bracket tight, valve accessible, and hose routing clear of heat/chafe zones.
- No propane odor before opening cabin; if odor exists, keep system off and ventilate.
- Leak-check propane path after any fitting change and before travel segments with planned propane use.
- Keep cylinder valve closed during fueling, service, and long-term storage windows.
- Do not operate portable outdoor-only propane appliances inside enclosed cabin space.

### Incident response quick actions
- If electrical burning odor/smoke: drop load, open `48V` disconnect, remove shore input, assess with extinguisher ready.
- If alternator charging fault or battery-trip event occurs while driving/testing: switch `Upfitter #3 OFF` first to disable the `WS500`, then isolate the house system only after charging output has collapsed.
- If propane alarm or gas odor: close tank valve, remove ignition sources, ventilate immediately, and do not restore gas flow until fault is found.
- Log each incident or near-miss in `logs/LOG.md` and add unresolved hazards to `docs/core/TRACKING.md`.

## Marketplace sourcing routine (from workbook)
- Daily 5-minute scan: 80/20 extrusion, RV water tank, sink/faucet, office chair, monitor arm, cooktop, fridge, diesel heater, camper parts.
- Save searches and enable notifications to capture liquidation listings quickly.
- Prioritize used-commercial office gear over consumer-tier furniture for daily work ergonomics.
- Use strict safety screening for electrical components, especially used batteries and charging hardware.
- Tool sourcing (Ryobi-first) and listing tracker:
  - `bom/tools_marketplace_tracker.csv`

## Used-parts target pricing anchors
- 80/20 extrusion: target `$2-$4/ft` (vs higher retail).
- Plywood and hardwood: target `$40-$60/sheet` for usable cabinet-grade material.
- Office chair: target `$200-$400` for premium used models.
- Monitor arm: target `$50-$120` with adequate load rating.
- Water tank: target `$30-$100` with food-safe/NSF confirmation.
- Solar panels: target around `$0.30-$0.50/W` where condition is verified.

## Flight/travel handoff
- Secure shutdown checklist before leaving vehicle
- Storage/security procedure while away
- Carry-on vs checked equipment standard

## Source artifacts
- No standalone workbook extract is currently retained for this section.
