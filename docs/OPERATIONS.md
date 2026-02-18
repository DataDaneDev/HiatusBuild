# Operations

## Build and deployment cadence
- Weekly planning update in `docs/PROJECT.md`
- Continuous progress notes in `logs/LOG.md`
- Weekly risk/decision review in `docs/TRACKING.md`
- Reconcile workbook-derived CSV exports before major purchases (`bom/`)

## Pre-departure checklist (starter)
- Battery SOC and charging paths verified
- Communications primary and fallback validated
- Critical spares onboard (fuses, terminals, core tools)
- Fuse inventory verified against `docs/ELECTRICAL_fuse_schedule.md` (installed + spare counts)
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
- Verify correct fuse values/voltage classes against `docs/ELECTRICAL_fuse_schedule.md`.
- Confirm terminal torque marks, busbar covers, and abrasion protection on all high-current runs.
- Confirm `48V` disconnect operation and expected de-energization behavior.
- Validate AC branch polarity and GFCI/RCD trip on each outlet branch before normal use.
- Confirm detector status (LP/CO/smoke powered, test function passes, expiration date in range).

### Bench-test (electrical module)
Bench-test intent: validate wiring correctness and basic device behavior (shunt, converter, inverter/charger) *before* install, using controlled energization and small loads.

- Battery parallel tie: measure each battery voltage before paralleling; bring packs to near-equal voltage/SOC first to avoid large equalization currents.
- Safe energization order (DC): keep `48V` disconnect open and remove Lynx branch fuses; connect negatives first (battery negatives to battery-side negative combine, then to SmartShunt battery side); wire positives to Class T blocks with Class T fuses removed.
- Bank bring-up: insert Class T fuses one-at-a-time (disconnect still open) and confirm expected bank voltage at the battery-side busbar.
- System bring-up: close `48V` disconnect to energize the Lynx bus; then insert Lynx branch fuses one-at-a-time, verifying each branch after insertion.
- MultiPlus inrush: expect some inrush when first connecting the inverter branch; use a pre-charge method if needed (pre-charge resistor/switch or a temporary pre-charge lead) and stop if you see abnormal arcing/heating.
- Functional checks: verify SmartShunt reads voltage correctly, Orion outputs stable `12V` under load, MultiPlus inverts correctly into a small known load, and MultiPlus charges correctly when AC-in is applied.
- Shutdown check: open `48V` disconnect and confirm the system de-energizes as expected; verify no unintended return paths bypass shunt measurement.

### Propane-specific checks
- Tank bracket tight, valve accessible, and hose routing clear of heat/chafe zones.
- No propane odor before opening cabin; if odor exists, keep system off and ventilate.
- Leak-check propane path after any fitting change and before travel segments with planned propane use.
- Keep cylinder valve closed during fueling, service, and long-term storage windows.
- Do not operate portable outdoor-only propane appliances inside enclosed cabin space.

### Incident response quick actions
- If electrical burning odor/smoke: drop load, open `48V` disconnect, remove shore input, assess with extinguisher ready.
- If propane alarm or gas odor: close tank valve, remove ignition sources, ventilate immediately, and do not restore gas flow until fault is found.
- Log each incident or near-miss in `logs/LOG.md` and add unresolved hazards to `docs/TRACKING.md`.

## Marketplace sourcing routine (from workbook)
- Daily 5-minute scan: 80/20 extrusion, RV water tank, sink/faucet, office chair, monitor arm, cooktop, fridge, diesel heater, camper parts.
- Save searches and enable notifications to capture liquidation listings quickly.
- Prioritize used-commercial office gear over consumer-tier furniture for daily work ergonomics.
- Use strict safety screening for electrical components, especially used batteries and charging hardware.
- Tool sourcing (Ryobi-first) and listing tracker:
  - `docs/OPERATIONS_workbook_marketplace_tools.md`
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
- `docs/OPERATIONS_workbook_marketplace_finds.md`
