# Electrical Trade Study: Sterling `BB1248120` vs Mechman `48V` Secondary Alternator

Status: pass `2` research draft (local-reference assimilation)  
Status date: `2026-03-19`

Historical-use note: this file is now a research archive. Final architecture decisions, wiring intent, and shutdown behavior live in `docs/core/ELECTRICAL_48V_ARCHITECTURE.md`.

Purpose: determine whether replacing the current Sterling `12V -> 48V` DC-DC alternator-charging path with a Mechman/Wakespeed `48V` secondary alternator architecture is actually a better fit for this project, or whether it creates more integration risk than it removes.

This pass explicitly assimilates newly added local references for Mechman `48V` installation and WS500 setup/operation documents.

Maintenance note (`2026-03-19`): canonical project docs now carry D-028/D-029 migration decisions, so active architecture is the dedicated `48V` secondary alternator path (`Mechman + WS500 + APM-48`) with Sterling hardware return-pending (contact Mechman first, then execute physical return). Sections comparing Sterling as the active baseline are retained as decision-history context.

## Bottom line
- The Mechman `48V` secondary-alternator concept is **real and technically plausible** for the `2021` `F-350` `7.3L` platform. Mechman publishes a `2020+` `7.3L` Godzilla dual-alternator bracket kit that retains the factory alternator and adds a second T-mount alternator.
- It is **not** a drop-in substitute for the current Sterling path. For this build, it becomes a different charging architecture with different controls, failure modes, and validation work.
- The biggest issue for your exact setup is **battery behavior**, not bracket fitment. Your bank is now confirmed to be **internal-BMS, non-CAN**. Wakespeed's own guidance treats that as a materially higher-risk integration case than a CAN-managed lithium bank.
- The newly documented Dumfume battery specs materially improve one part of the picture: the manual allows up to `1S4P`, sets a `58.4V` charge target, and recommends `20-50A` charge current per battery. On a `3x 100Ah` bank, the Mechman current curve looks much more compatible on raw charge-current magnitude than it did when the battery data was unknown.
- The new Mechman `INSTR-48V-GEN` document adds concrete installation criteria that are now hard requirements in this study: target about `2%` alternator-to-bank voltage drop, fuse the positive cable within `12 in` of bank connection, run a dedicated equal-or-larger ground cable, and validate startup at `2500 RPM` with `<0.1V` drop on both charge and ground paths.
- The new WS500 quick-start/manual docs confirm this is not just "alternator + regulator": harness polarity (`WS500-PH` vs `WS500-NH`), fused sense/power leads (`10-15A`, `3A`, and `5A` cases), default `500A/50mV` shunt assumptions, and charge-profile/capacity configuration are all explicit integration gates.
- User-confirmed assumption for this study: losing automatic house-to-starting-battery support is acceptable.
- A `370A` `12V` alternator upgrade alone is still the weakest value path. It adds vehicle-side headroom, but the Sterling charger remains capped at about `1.5 kW`, so house charging does not scale with alternator size the way many people assume.
- Current recommendation for execution: keep the dedicated `48V` secondary-alternator path as the active baseline, close the validation gates in this document, then execute Sterling return in the locked sequence (contact Mechman first, then return shipment).

## Current project baseline

| Item | Current project state | Why it matters |
| --- | --- | --- |
| House bank | `3x Dumfume 51.2V 100Ah` LiFePO4 in parallel (`15.36 kWh` nominal) | Exact battery is now documented; this improves charge-profile and parallel-bank analysis materially |
| Alternator charging | Dedicated `48V` secondary alternator path (`Mechman + WS500 + APM-48`) is the active baseline; Sterling `BB1248120` + `BBR` are return-pending | Active architecture now targets higher `48V` alternator charge potential with explicit validation gates |
| Sterling output ceiling | About `1,500 W` max, about `26A` at `57.6V` | Legacy comparison reference only (former active architecture) |
| Truck alternator basis | Current docs assume factory `240A` | Relevant for input-side thermal margin, not for raising house-side power above Sterling's limit |
| Purchase-later option | Mechman `370A` `12V` alternator | Helps margin/headroom, but not the `48V` house-side ceiling |

### Practical implication
- Sterling now functions as legacy comparison hardware only and is no longer the planning baseline.
- Dedicated `48V` secondary alternator path remains the only active architecture in this project that can materially exceed the old `~1.5 kW` alternator-to-house ceiling.

## What the Dumfume manual now clarifies

Manual/source basis for this section:
- `references/Dunfume_36V_48V_100Ah_Battery_-_User_Manual.pdf`
- User-supplied product/manual data in this research pass

| Battery parameter | Dumfume manual / supplied data | Immediate implication |
| --- | --- | --- |
| Nominal voltage | `51.2V` | Matches current project energy modeling basis |
| Capacity | `100Ah` per battery | Current bank is `3x` batteries in parallel |
| Charge voltage | `58.4V` | Any WS500 profile should be checked against this, not a generic `58.8V` assumption |
| Recommended charge current | `20-50A` per battery | Useful benchmark for whether Mechman output is a good fit |
| Max continuous charge current | `200A` per battery | Raw current ceiling is not the primary bottleneck here |
| Max expansion | Up to `1S4P` | Current `1S3P` bank is inside the manual's stated parallel-expansion limit |
| Charge temperature | `32°F - 149°F` (`0°C - 65°C`) | No-charge-below-freezing rule still matters for alternator charging logic |
| BMS | Internal `200A` BMS, non-CAN | Current-support and disconnect behavior are still the hard part |

### New battery-side conclusions
- The current battery bank is no longer a generic unknown. It is a defined `1S3P` bank using batteries whose manual allows up to `1S4P`.
- Inference from the manual's per-battery current guidance:
  - recommended aggregate bank charge current is likely about `60-150A` if current shares normally across `3` parallel batteries
  - absolute aggregate continuous charge capability is likely much higher than that, but "recommended" is the better planning number for alternator charging
- Inference from the provided Mechman curve against the documented `3x` battery bank:
  - `44.5A` total charge current is about `14.8A` per battery
  - `90.7A` total charge current is about `30.2A` per battery
  - `111.7A` total charge current is about `37.2A` per battery
  - `145.7A` total charge current is about `48.6A` per battery
- That means the Mechman current curve shown so far sits **inside or very near** the Dumfume manual's recommended per-battery charge-current range when divided across the current `3`-battery bank.
- The current Sterling path remains very gentle by comparison: about `26A` total is only about `8.7A` per battery.
- The unresolved battery risk is now less about "can the bank absorb this current?" and more about:
  - exact `WS500` programming
  - BMS disconnect behavior under charge
  - supported/non-supported battery status with Wakespeed
  - load-dump mitigation if the internal BMS opens

## What Ford and Mechman currently support

### Ford-side context
- The local `2021 Super Duty Pick-Up Order Guide` shows the `7.3L` gas pickup line had a factory `397 Amp Alternator (67B)` option when `Dual Battery (86M)` was ordered.
- That confirms Ford already supported a higher-output charging configuration on the `7.3L` gas pickup platform.
- It does **not** prove that Ford offered a factory dual-alternator setup on your pickup. In the order guide evidence reviewed here, the `7.3L` gas pickup language points to a higher-output alternator option, not a factory second alternator.

### Mechman dual-bracket support
- Mechman currently lists a `48-Volt Dual Bracket Kit for 2020+ Ford 7.3L Gas Godzilla platform (LiFePO4)` at `SKU GZDB-20-1AC-775048V-LFP`.
- The kit description and instruction sheet indicate it retains the factory alternator and adds a second alternator using a cast bracket, idler pulley, mounting hardware, and an `88.06 in` belt.
- The bracket instruction sheet specifically references `2020+` `7.3L` Godzilla fitment and a second T-mount alternator position.

### What this means
- On fitment alone, the dual-alternator concept is credible.
- The remaining questions are not "does a bracket exist?" but "does this work cleanly with your batteries, controls, grounding plan, and validation schedule?"

## What the `48V` alternator package actually includes

From the Mechman `B820648V-LFP` regulator/programming sheet reviewed in this pass:

- `WS500` regulator
- `2x` Wakespeed thermistors
- `500A/50mV` Wakespeed shunt
- `27 ft` Wakespeed positive harness
- `46 mm` `6-groove` pulley

### Important detail
- Mechman literature reviewed here is not perfectly self-consistent on battery programming.
- One part of the `B820648V-LFP` sheet says a generic AGM profile is the default unless otherwise specified.
- The same sheet then gives setup instructions for:
  - `Brand: Generic`
  - `Model: 48V`
  - `Battery Ah: 100`
  - `Total Batteries: 1`
  - `Charge Profile: CPE#8 LiFePO4`

### Why that matters for your build
- Your bank is not `1x 48V 100Ah`. It is `3x 48V 100Ah` in parallel.
- The out-of-box generic regulator setup shown in Mechman's literature is still not obviously matched to your actual bank.
- Your documented battery charge target is `58.4V`, so a generic `58.8V` profile should not be accepted without checking the manual and vendor guidance first.
- This means you should treat "pre-programmed for LiFePO4" as a starting point, not proof of compatibility.

## New findings from newly added reference files (`2026-03-19`)

### Mechman `INSTR-48V-GEN_3-28-2025` (local PDF) adds non-optional install constraints
- Local-reference housekeeping note: `Mechman 48v Alt Install Guide INSTR-48V-GEN_3-28-2025.pdf` and `Mechman General 48v install INSTR-48V-GEN_3-28-2025.pdf` are byte-identical copies of the same file.
- Cable-design target in the guide is about `2%` voltage drop from alternator to battery bank.
- Guide includes a cable-sizing reference table:
  - up to `100A` and `5 ft` one-way: `6 AWG`
  - up to `150A` and `10 ft` one-way: `4 AWG`
  - up to `200A` and `15 ft` one-way: `2 AWG`
  - up to `250A` and `20 ft` one-way: `1/0 AWG`
- Positive charge cable should be fused within `12 in` of battery-bank connection.
- Ground cable should be equal to or larger than the positive cable and should run directly from alternator to battery bank (not sheet metal/factory ground path).
- First-start checks are now explicit:
  - charge `48V` batteries fully before first startup
  - raise engine speed to around `2500 RPM`
  - verify bank voltage rises by at least `1V` over resting value
  - verify both charge-path and ground-path voltage drop are each `<0.1V` under load
- Warranty/support language in this file is strict:
  - programming support is limited to battery models Wakespeed officially supports
  - user programming changes beyond provided Mechman setup can void warranty coverage

### Mechman `INSTR-GZDB-20` bracket guide clarifies mechanical scope
- The bracket kit contains bracket/hardware, idler pulley, and `88.06 in` belt.
- Installation sequence explicitly uses two OEM-compatible alternators:
  - one saddle-mount position
  - one T-mount position
- Alternators are shown as not included in the bracket instructions themselves, so final kit scope still needs purchase-level confirmation.

### WS500 quick-start and product manual add specific integration requirements

#### Wiring/fusing assumptions that must be carried into design
- Harness polarity must match alternator type: `WS500-PH` (P-type) vs `WS500-NH` (N-type).
- WS500 alternator-positive power lead is called out for fusing (`10A`, or `15A` for extra-large-case alternators).
- Battery positive-sense lead is called out for `3A` fuse protection.
- Current-sense leads can require `5A` fuse protection when shunt is in the positive cable.
- WS500 default current-shunt assumption is `500A/50mV`.
- Manual wiring note indicates power and positive-sense leads should be connected on the alternator side of any disconnect switch/fuse that could isolate alternator from battery.
- Diagram note indicates a battery service disconnect must remain ON while engine is running.

#### Configuration implications for this bank (`3x 51.2V 100Ah = 300Ah`)
- DIP-switch capacity band for this bank maps to `250Ah-500Ah` range.
- Quick-start profile matrix shows `Custom #2` as LiFePO4-oriented; this still must be validated against the Dumfume `58.4V` target.
- DIP `#8` small-alternator mode limits field to about `75%`; this can be used as a staged commissioning/de-risk step.
- Function-in behavior changes by chemistry; manual indicates LiFePO4 configuration can force float via function input.
- WS500 profile table appears to set tighter LiFePO4 charge-temperature windows than the battery manual (`0°C` minimum and about `40°C` maximum in the table), so final programmed limits should be confirmed explicitly.

#### Fault visibility and system behavior now better defined
- WS500 advisory/error table includes battery over-voltage (`13`), alternator over-temp (`21`), alternator RPM above expected (`22`), and missing required sensor (`42`) conditions.
- Additional CAN-linked fault/advisory codes include bus-disconnect messaging (`51`/`52`), which is relevant if CAN/BMS integration is later added.
- Practical implication for this project: commissioning must include explicit interpretation of WS500 code behavior, not just steady-state voltage/current checks.

#### Important caution on profile tables
- The product-manual preset profile table is presented in voltage values that appear `12V`-scaled.
- For this `48V` project, do not infer final absolute setpoints from preset names alone; confirm actual WS500 programmed voltage targets against the battery manual's `58.4V` requirement.

## Why the dual-`48V` idea is attractive

### Architectural upside
- It preserves a dedicated factory alternator for truck/starter-battery duties.
- It avoids pulling `100A+` on the truck's `12V` side just to make `~1.5 kW` at the `48V` house bank.
- Wakespeed's own public guidance says a **secondary alternator is often the better automotive solution** because the factory alternator is commonly integrated with the vehicle's engine computer.

### Charging upside
- The Mechman `48V` output curve you provided is in alternator shaft RPM, not engine RPM.
- Even so, it shows the basic magnitude change clearly:

| Mechman curve point | Approx. `48V` output | Approx. power at `57.6V` |
| --- | --- | --- |
| `3,900` shaft RPM | `44.5A` | `2.56 kW` |
| `5,000` shaft RPM | `90.7A` | `5.22 kW` |
| `6,000` shaft RPM | `111.7A` | `6.43 kW` |
| `8,000` shaft RPM | `129.8A` | `7.48 kW` |
| `14,500` shaft RPM | `145.7A` | `8.39 kW` |

### Comparison to current Sterling path
- Sterling ceiling: about `26A` at `57.6V` (`~1.5 kW`)
- Mechman curve at `5,000` shaft RPM: `90.7A` (`~3.5x` the Sterling current ceiling)
- Mechman curve at `6,000` shaft RPM: `111.7A` (`~4.3x` the Sterling current ceiling)

### The catch
- Those Mechman numbers are at **alternator shaft speed**, not confirmed engine idle speed.
- Until pulley ratio and actual installed idle output are verified, you should not assume those gains appear at hot idle.

## The real problem for your setup: internal-BMS, non-CAN batteries

This is the key issue that makes the Mechman/Wakespeed path materially riskier than the Sterling path.

### What Wakespeed says
- Wakespeed's public FAQ says they cannot guarantee support for every battery with an internal BMS and that batteries not on their approved/supported list are not guaranteed to work correctly.
- Wakespeed also states that a battery with internal BMS and automatic disconnect behavior can require an alternator protection device and specifically mentions **avalanche diodes** as one mitigation path.
- Wakespeed's Cerbo/DVCC guidance says `DVCC` does **not** remove the need for direct `WS500`/battery communication and fault handling.
- Wakespeed's public guidance also says smart shunts that use digital communication, including examples like Victron SmartShunt-class devices, will not work as the regulator shunt input; the regulator expects an analog shunt signal.

### Why that matters here
- Your current bank is internal-BMS and **no CANbus**.
- The bank is now identified as Dumfume `51.2V 100Ah`, and current magnitude itself looks workable on a `3`-battery parallel bank.
- If a battery or bank BMS disconnects during charge because of over-voltage, low temperature, or internal fault logic, the alternator/regulator path has to survive that event safely.
- A Sterling DC-DC charger is far more naturally buffered/limited in that scenario than a direct `48V` alternator architecture.
- With the Mechman/Wakespeed path, safe operation depends much more heavily on:
  - supported battery behavior
  - correct regulator programming
  - shunt and temperature-sensor installation
  - load-dump protection strategy

### Warranty/support consequence
- Mechman's `48V` installation literature says they will provide regulator-programming support only for battery models officially supported by Wakespeed.
- The same literature says unsupported battery-programming modifications can void warranty support.
- The battery family is now documented, but in this research pass I did **not** find any public official Wakespeed reference to Dumfume on `wakespeed.com`.
- That is not proof of non-support. It means official vendor confirmation is still required before treating this as a supported battery/regulator combination.

## Isolation and grounding: do not assume full electrical isolation yet

Your stated goal is to keep the house charging system fully isolated from the starter/vehicle electrical system.

### What is clearly true
- A secondary alternator architecture is much more isolated from the truck's `12V` charging path than the current Sterling system.
- Mechman's `48V` installation literature says to run a **dedicated ground cable directly from the alternator to the battery bank** and not to rely on factory ground paths.

### What is still unresolved
- The Mechman `B820648V-LFP` document references a terminal block, ground modification, ground tag, negative tag, and positive tag.
- That documentation strongly suggests the grounding scheme needs to be treated carefully.
- It does **not** conclusively prove from the reviewed material alone whether the finished `48V` negative can remain fully floating from chassis in your install.

Inference from the reviewed Mechman documents:
- You should **not** design around the assumption of a fully floating/galvanically isolated `48V` alternator system until Mechman explicitly confirms how the alternator case, negative output, and engine/chassis relationship behave in this exact kit.

## Starter-battery maintenance changes if Sterling is removed

This is a practical system-behavior difference, not just a feature preference.

### Sterling path
- Sterling currently markets both:
  - a reverse-charging `12V/24V -> 48V` product page
  - a unidirectional / no-reverse-charge `12V/24V -> 48V` product page
- Your repo and purchase records say `BB1248120`, but the exact shipped label/manual behavior should be checked before assuming starter-battery backfeed behavior.

### Mechman `48V` secondary-alternator path
- No reviewed Mechman/Wakespeed material suggests automatic starter-battery maintenance is built in.
- If you replace Sterling completely, you should assume starter-battery trickle/maintenance is simply absent unless you later choose to add it back.

### Current project stance
- Loss of automatic house-to-starting-battery support is acceptable for this project.

### Optional replacement paths only if you later want that feature back
- Keep a dedicated small `48V -> 12V` charger for the starter battery
- Keep a service/maintenance charging strategy separate from the main alternator-charging architecture
- Accept no automatic house-to-starting-battery backfeed

## Why the `370A` single-`12V` upgrade is still weak on ROI

### What it does help
- More alternator headroom
- Better margin against vehicle loads plus Sterling demand
- Potentially better thermal behavior at low-speed/high-demand operation than a stock unit

### What it does not change
- The Sterling charger is still capped near `1.5 kW`
- The house bank still only sees about `26A` at `57.6V`

### Result
- A `370A` `12V` alternator upgrade is rational if your main concern is protecting the truck-side system while keeping Sterling.
- It is **not** the right upgrade if your real goal is materially faster `48V` house charging.

## Comparison matrix

| Option | House charge ceiling | Integration complexity | Battery/BMS risk | Starter-battery support | Schedule risk | Current position (`2026-03-19`) |
| --- | --- | --- | --- | --- | --- | --- |
| Keep Sterling as-is | `~1.0-1.5 kW` depending `BBR` setting | Low | Low-Medium | Possible, but no longer required | Low | Legacy fallback only (return-pending hardware) |
| Add `370A` `12V` alternator and keep Sterling | Still `~1.0-1.5 kW` | Medium | Low-Medium | Same as Sterling path | Medium | Deprecated path (BOM rows `103`/`104`) |
| Move to Mechman `48V` secondary alternator | Potentially `>2.5 kW` and much higher at usable shaft speed | High | High for non-CAN/internal-BMS bank | Not inherent, but acceptable | High | Active planning baseline with validation gates still required |

## Decision for this pass

### Recommended position now
- Keep dedicated `48V` secondary alternator architecture as the active baseline for Phase `1`.
- Keep Sterling charger/remote in return-pending status and execute return only after Mechman fitment/content confirmation.
- Treat the validation checklist below as mandatory pre-commissioning gates for the active Mechman path.
- Use the simple `A1` implementation as the default project direction unless testing proves extra control layers are required.

### Why
- Fitment looks credible.
- Performance upside is real.
- Battery/regulator/support risk remains the main commissioning constraint, so execution must stay gated by the validation items below.

## Simplified architecture baseline (project direction)

The project preference is to keep the `48V` alternator path simple unless commissioning data proves more layers are necessary.

### Simple A1 power path
- Main charge path:
  - `48V alternator B+` -> source-side high-AIC fuse/protection -> `48V` bus/Lynx feed -> battery-bank protection -> house bank
- Clamp protection path:
  - Balmar `APM-48` installed as a parallel protection device at/near alternator output, per manufacturer guidance
- Regulation and sensing path:
  - `WS500` connected for field/stator, alternator/battery voltage sense, shunt input, and temperature inputs per manual
- Grounding path:
  - dedicated alternator-to-bank negative cable, equal or larger than positive, no sheet-metal return path

### What "simple" intentionally excludes at first pass
- No advanced automated contactor/interlock logic as day-one default.
- No CAN/DVCC dependency as a prerequisite for basic alternator charging.
- No added architecture complexity unless fault testing or thermal behavior proves it is needed.

## Required validation before commissioning the Mechman path

### Battery support
- Exact battery family is now documented as Dumfume `51.2V 100Ah`; keep the manual in the repo as the local source of truth.
- Confirm with Wakespeed whether this battery is inside or outside their supported-programming path.
- Confirm whether the manual's recommended `20-50A` charge current is intended to scale across the current `1S3P` bank for alternator charging.
- Confirm whether `58.4V` should be treated as the hard alternator charge ceiling and whether any float stage should be reduced or disabled.

### Regulator and protection
- Confirm whether your battery chemistry/BMS behavior requires avalanche-diode protection, a battery-protection device, keeper battery strategy, or another specific mitigation.
- Confirm exact `WS500` accessory set still needed for your final architecture, especially if Cerbo integration is desired.
- Confirm whether the existing Victron `SmartShunt` stays only as a monitoring device while the WS500 uses its own included analog shunt.
- Confirm alternator field polarity and harness selection (`WS500-PH` vs `WS500-NH`) for the exact alternator in your kit.
- Confirm final fusing plan for WS500 harness leads (`10-15A` power lead, `3A` positive-sense lead, `5A` current-sense leads when applicable).
- Confirm whether battery and alternator temperature sensors are configured as required vs optional, and what fault behavior (`Code 42`) is expected if a required sensor is missing.
- Confirm final WS500 charge-profile choice and verify actual programmed voltage setpoints against Dumfume `58.4V` requirement.

### Grounding/isolation
- Confirm with Mechman whether the second alternator output negative is isolated from case/chassis or should be treated as case/engine referenced.
- Confirm the exact required negative/ground routing for a clean `48V` house-bank install.

### Output at realistic operating speeds
- Ask Mechman for expected `48V` output at:
  - hot idle
  - fast idle
  - typical highway engine RPM
- Do not accept shaft-speed curve alone as your idle-output answer.

### Operational behavior
- Starter-battery auto-maintenance is not required for this project.
- If desired later, add a separate maintenance path as a convenience feature rather than as a swap blocker.

### Commissioning criteria (now grounded in the added manuals)
- Use fully charged house batteries before first engine-run validation.
- Validate at around `2500 RPM` and record:
  - bank-voltage rise versus resting voltage (target at least `+1V` during active charging)
  - charge-path voltage drop (target `<0.1V`)
  - ground-path voltage drop (target `<0.1V`)
- Capture WS500 LED/error behavior during startup, ramp, acceptance, and any fault tests so post-install tuning is evidence-based.

### WS500 operator control and monitoring (vs Sterling remote)
- `WS500` does not provide a Sterling-style dedicated remote panel experience out of the box.
- Practical control/monitoring methods available:
  - DIP-switch setup (battery profile, battery-size band, small/large alternator mode)
  - Wakespeed smartphone/PC configuration workflow (for deeper setup/tuning)
  - onboard LED state/error indications for live status and faults
  - optional CAN integration if you later decide to add that layer
- Practical down-tune options:
  - small-alternator mode (about `75%` field limit)
  - charge profile and voltage/temperature parameter tuning to match battery limits


## Protection strategy deep-dive: dedicated modules vs AGM buffer

### Design target for this build
- Survive an internal-BMS disconnect event without damaging alternator/regulator/electronics.
- Keep charging performance gains that make the dual-`48V` alternator worth doing.
- Stay in a realistic budget band for a non-commercial build.

### Option A: protection-module architecture (recommended)

This approach treats the alternator system like a controlled power plant and layers explicit protection components.

#### Core protection stack
1. **External regulator with fast field control** (`WS500`, already implied by Mechman kits).
2. **High-power over-voltage/load-dump clamp** on the `48V` bus (e.g., Balmar `APM-48` class, sized for alternator energy).
3. **Primary over-current protection** near the source and battery (`Class-T` or equivalent high-AIC DC fusing, correctly rated for `58.4V+`).
4. **Dedicated positive/negative cable routing** with measured voltage-drop compliance.
5. **Temperature, voltage, and shunt feedback** wired exactly as required by the regulator.

#### Optional hardening layers (add only if testing indicates need)
1. **Regulator/battery disconnect interlock** so field current is collapsed immediately if battery contactor/BMS opens.
2. **Main charge-path contactor logic** for controlled fault isolation.
3. **Precharge path** where downstream DC capacitance or switching behavior makes it necessary.

#### Research variants inside Option A
- **A1: "minimum viable simple" module stack (default first implementation)**
  - Keep Mechman + WS500 accessory baseline.
  - Add one properly sized load-dump clamp module and correct fuse architecture.
  - Example: Balmar `APM-48` (`48V` specific) is a plausible clamp candidate at about `$141` sale / `$158` typical retail.
  - Practical incremental cost above kit wiring/fusing is still usually about `$250-$700` once you include the clamp plus mounting, short heavy leads, and the rest of source/battery protection details around it.
- **A2: "controlled disconnect hardening" stack (optional)**
  - A1 plus explicit battery contactor logic, precharge, and hard fault state behavior.
  - Add a dedicated enable chain (ignition/run + regulator healthy + battery ready).
  - Typical incremental cost: about `$700-$1,800`.
- **A3: "belt-and-suspenders" stack**
  - A2 plus redundant over-voltage path, transient logging, and higher-end sealed contactor architecture.
  - Typical incremental cost: `$1,800-$3,500+`.

#### Strengths
- Directly addresses the real hazard (load dump from abrupt battery disconnect).
- Preserves high charge-rate potential of the secondary alternator.
- Scales with future battery changes better than chemistry-specific buffering tricks.
- Allows a staged rollout: run simple A1 first, then add A2/A3 only if evidence justifies it.

#### Weaknesses
- Requires careful electrical design and commissioning discipline even in A1.
- Can grow into more parts/wiring if escalation to A2/A3 is required.

### Option B: AGM battery as a buffer

This approach adds lead-acid mass as a "shock absorber" between alternator/regulator behavior and lithium-bank transients.

#### Ways people try this
- **B1: full-time AGM on the `48V` bus** (typically `4x 12V AGM` in series).
- **B2: partial-buffer hybrid** where AGM is present mainly for transient events while lithium remains the primary bank.
- **B3: AGM intermediate bank + DC-DC to lithium** (architecturally similar to reintroducing a conversion stage).

#### Practical issues for this project
- A true `48V` AGM buffer usually means **four matched AGMs in series**, with balancing/maintenance concerns and substantial weight/volume.
- AGM does **not** remove the need for proper over-voltage/load-dump protection; it only softens some transients.
- If buffering is made robust enough to be dependable, cost/complexity can approach or exceed a correct module-based design while sacrificing efficiency.
- Reintroducing a DC-DC stage to make AGM buffering predictable also reintroduces conversion losses and charging bottlenecks the dual-alternator concept was meant to avoid.

#### Cost/weight reality
- Hardware can look cheaper on day one (`$600-$1,600` battery-side depending AGM size/quality), but lifecycle cost is usually worse due to AGM aging, replacement, mounting, and payload penalty.

### Baseline and conditional components

For a safe `48V` secondary-alternator build, plan on these baseline elements:
- Alternator output breaker/fuse strategy with verified DC interrupt rating for system voltage.
- Proper busbars/distribution blocks rated for fault current and temperature environment.
- Cable sizing/termination and strain relief verified for continuous current and engine-bay thermal conditions.
- Grounding topology that matches confirmed alternator negative/case behavior.
- Thermal sensing at alternator and battery, and analog shunt feedback compatible with WS500 requirements.
- Commissioning tests: no-load overspeed behavior, simulated disconnect behavior, hot-idle thermal run, and fault-state recovery.

Add these only when architecture/testing indicates need:
- Main battery disconnect contactor with emergency/manual service isolation.
- Precharge resistor/contactor path where inverter input capacitance requires it.

### Best reasonably priced path

For this project's risk profile (internal-BMS, non-CAN `48V` bank), the best value is:
- **Option A1 first**, not AGM buffering.
- Target a protection budget band around **`$250-$700` incremental** above base alternator/regulator kit and normal cabling/fusing.
- Escalate to A2 only if commissioning/fault testing shows a clear need.
- Use AGM only if you have a separate requirement that truly benefits from lead-acid characteristics (for example, extreme cold cranking support in a different subsystem), not as the primary alternator load-dump strategy.

### Concise verdict
- If you proceed with dual-`48V` alternator charging, start with **simple A1 module-first architecture** (field control + load-dump clamp + correct fusing/wiring).
- Add contactor/interlock/precharge layers only if your real test data shows they are needed.
- An **AGM buffer is a secondary aid at best**, and for this build it is usually heavier, less efficient, and not safer-per-dollar than a properly engineered protection-module stack.

### What you would still need (gap check vs currently purchased Sterling architecture)

If you move to a Mechman/WS500 `48V` secondary alternator path, these are the major adds/changes likely required beyond the currently purchased Sterling-centric parts list.

#### Likely no-longer-used Sterling-specific items
- Sterling `BB1248120` charger and `BBR` remote path hardware.
- Sterling-side fuse branches in the current implementation model (`F-04` output branch and `F-08` engine-bay input branch) would be removed or repurposed.
- Any Sterling-specific spare-fuse planning should be replaced with secondary-alternator-specific protection spares.

#### New protection/power-path components you likely still need
1. **Alternator-output primary protection**
   - A source-proximate high-interrupt DC fuse strategy rated for the final `48V` charging bus and expected fault current.
   - This is not the same protection profile as the old Sterling feeder fuse because available fault energy is much higher with a direct alternator path.
2. **Load-dump/over-voltage clamp device**
   - Dedicated transient suppression module/device sized for alternator disconnect events.
   - Treat this as required when charging internal-BMS lithium that can open under fault/temperature limits.
3. **Main charge-path contactor + control logic (conditional)**
   - Add if testing demonstrates unsafe behavior or unacceptable fault recovery without it.
4. **Precharge path (conditional)**
   - Add if connecting to significant downstream DC capacitance or if switching transients indicate need.
5. **WS500 integration accessories/IO planning**
   - Confirm exact accessory completion: analog shunt placement, battery/alternator temperature probes, harness lengths, and any I/O used for fault interlock.
6. **Engine-bay and chassis routing hardware**
   - Heat-rated loom, abrasion protection, standoffs/clamps, and strain relief suitable for continuous vibration/thermal cycling.
7. **Commissioning instrumentation and tests**
   - Test plan and measurement points for hot-idle output, fast-idle thermal behavior, and simulated battery-disconnect fault response.

#### Notes on Balmar `APM-48` (and why this does not collapse A1 to `$141`)
- `APM-48` is the correct voltage class to evaluate for this architecture, unlike `24V` modules.
- At roughly `$141-$158`, it materially lowers entry cost for the clamp component itself.
- It should still be treated as one layer of protection, not the entire protection strategy:
  - field control and WS500 behavior still matter
  - source/battery over-current protection still matters
  - wiring/placement quality still matters
  - commissioning tests under real fault-like events still matter
- Practical takeaway: `APM-48` can make A1 cheaper, but it does **not** make A1 equivalent to "buy one part and done."

#### Practical procurement implication
- The "Sterling fuse going away" is only a small part of the delta.
- The bigger procurement shift is adding a **proper high-energy protection chain** (primary source fuse strategy, dump clamp, and commissioning instrumentation first), then adding contactor/interlock/precharge only if needed and updating spare policy around whichever components are actually installed.

## Questions to send vendors

### To Mechman
1. Will `GZDB-20-1AC-775048V-LFP` fit a `2021 Ford F-350` pickup with the `7.3L` gas engine on my exact VIN/configuration?
2. What output should I expect from this kit at hot idle, fast idle, and normal driving RPM on the `7.3L` Godzilla?
3. Is the alternator negative isolated from the case, or should the `48V` system be treated as engine/chassis referenced?
4. Does this `48V` alternator include or require avalanche-diode/load-dump protection for internal-BMS lithium banks that can self-disconnect?
5. Can you pre-program the `WS500` for `3x Dumfume 51.2V 100Ah` parallel batteries with internal BMS and no CAN, using a `58.4V` charge target, and does that remain inside warranty support?
6. Exactly which Wakespeed accessories are included in the kit, and which Cerbo-integration pieces are extra?
7. Which WS500 harness polarity is correct for this exact alternator (`PH` or `NH`)?

### To Wakespeed
1. Is the Dumfume `51.2V 100Ah` battery on your supported list?
2. If not, what mitigation is mandatory for safe charging with an internal-BMS, non-CAN `48V` lithium bank?
3. Does DVCC/Cerbo provide any meaningful substitute for missing battery-CAN lockout in this case, or is it monitoring-only?
4. What is the recommended fault-handling strategy if the battery BMS disconnects under charge?
5. For a `48V` bank, what exact voltage setpoints does the selected LiFePO4 profile use, and does your preset/custom profile align with a `58.4V` ceiling?
6. For a `300Ah` bank, do you agree with the `250-500Ah` DIP capacity selection as the correct starting point?
7. For a non-CAN install, what is your recommended operator monitoring/control workflow that most closely replaces a simple "remote panel" experience?

### To the battery manufacturer
1. Is the recommended `20-50A` charge-current range intended per battery, and does it scale linearly in `1S3P` / `1S4P` parallel banks?
2. For alternator charging, should `58.4V` be treated as the hard charge ceiling, and should float be disabled or reduced?
3. Does the BMS open on over-voltage, under-temperature, over-current, or cell imbalance while charging?
4. Are three batteries in parallel approved for alternator charging specifically, and is the charge-current limit additive across the bank?

## What would change my recommendation
- Wakespeed explicitly supports the documented Dumfume battery or gives a safe approved configuration for it
- Mechman confirms safe mitigation for internal-BMS/non-CAN behavior
- Mechman confirms the grounding/isolation behavior you want
- Mechman provides realistic idle/fast-idle output numbers that materially outperform the current Sterling path in the RPM range you actually care about
- The retained factory alternator fully preserves normal starter/vehicle charging independence after the swap

## Migration Procurement Delta (Sterling -> 48V alternator)
- Delta is now assimilated into canonical docs (`SYSTEMS`, `TRACKING`, starter plan, fuse schedule, and BOM).
- Canonical migration lock for this pass:
  - `BB1248120` + `BBR` are return-pending (contact Mechman first, then execute physical return)
  - `A1` simple architecture remains the implementation baseline
  - Lynx remains the central `48V` distribution/fuse point
  - `F-04` alternator branch fuse is now locked at `150A` (`58V/80V` MEGA)
  - standalone BOM conditionals rows `172` and `173` are removed from scope

## Sources used in this pass
- [Project BOM baseline](../../bom/bom_estimated_items.csv)
- [Current systems baseline](../core/SYSTEMS.md)
- [Current project decision/risk log](../core/TRACKING.md)
- [Dumfume battery manual added to project](../../references/Dunfume_36V_48V_100Ah_Battery_-_User_Manual.pdf)
- [2021 Super Duty Pick-Up Order Guide](../../references/2021%20Super%20Duty%20Pick-Up%20Order%20Guide.pdf)
- [Mechman 48V general alternator install guide (`INSTR-48V-GEN_3-28-2025`)](../../references/Mechman%2048v%20Alt%20Install%20Guide%20INSTR-48V-GEN_3-28-2025.pdf)
- [Mechman dual alternator bracket guide (`INSTR-GZDB-20`)](../../references/Mechman%20dual%20alternator%20bracket%20INSTR-GZDB-20.pdf)
- [WS500 quick start guide (`09-30-2022 v3`)](../../references/WS500-Quick-Start-Guide-09-30-2022-V3.pdf)
- [WS500 product manual (`09-30-2022 v2`)](../../references/WS500-Product-Manual-09-30-2022-V2.pdf)
- User-provided product listing details for Balmar `APM-48` (`48V` alternator protection module, price snapshot about `$141.30` sale / `$157.99` list)
- [Mechman 48-Volt Dual Bracket Kit for 2020+ Ford 7.3L Gas Godzilla platform (LiFePO4) - Externally Regulated](https://mechman.com/48-volt-dual-bracket-kit-for-2020-ford-7-3l-gas-godzilla-platform-lifepo4-externally-regulated/)
- [Mechman 48-Volt Elite, Externally Regulated (`B820648V-LFP`)](https://mechman.com/content/instructional-pdfs/B820648V-LFP.pdf)
- [Mechman 370A alternator for Ford `5.0L` Coyote and Ford `7.3L` Godzilla (`11532370`)](https://mechman.com/370-amp-alternator-for-ford-5-0l-coyote-and-ford-7-3l-godzilla/)
- [Wakespeed Learn: performance, Cerbo/DVCC, smart shunts, battery support FAQ](https://www.wakespeed.com/learn)
- [Sterling reverse-charging `12V/24V -> 48V` product page](https://sterling-power.com/products/12v-to-48v-1500w-battery-to-battery-charger-w-reverse-charging-feature)
- [Sterling unidirectional / no-reverse-charge `12V/24V -> 48V` product page](https://sterling-power.com/products/12v-24v-to-48v-battery-to-battery-charger-uni-directional-charging-does-not-reverse-charge)
