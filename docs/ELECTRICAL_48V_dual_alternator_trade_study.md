# Electrical Trade Study: Sterling `BB1248120` vs Mechman `48V` Secondary Alternator

Status: pass `1` research draft  
Status date: `2026-03-15`

Purpose: determine whether replacing the current Sterling `12V -> 48V` DC-DC alternator-charging path with a Mechman/Wakespeed `48V` secondary alternator architecture is actually a better fit for this project, or whether it creates more integration risk than it removes.

## Bottom line
- The Mechman `48V` secondary-alternator concept is **real and technically plausible** for the `2021` `F-350` `7.3L` platform. Mechman publishes a `2020+` `7.3L` Godzilla dual-alternator bracket kit that retains the factory alternator and adds a second T-mount alternator.
- It is **not** a drop-in substitute for the current Sterling path. For this build, it becomes a different charging architecture with different controls, failure modes, and validation work.
- The biggest issue for your exact setup is **battery behavior**, not bracket fitment. Your bank is now confirmed to be **internal-BMS, non-CAN**. Wakespeed's own guidance treats that as a materially higher-risk integration case than a CAN-managed lithium bank.
- The newly documented Dumfume battery specs materially improve one part of the picture: the manual allows up to `1S4P`, sets a `58.4V` charge target, and recommends `20-50A` charge current per battery. On a `3x 100Ah` bank, the Mechman current curve looks much more compatible on raw charge-current magnitude than it did when the battery data was unknown.
- A `370A` `12V` alternator upgrade alone is still the weakest value path. It adds vehicle-side headroom, but the Sterling charger remains capped at about `1.5 kW`, so house charging does not scale with alternator size the way many people assume.
- Current recommendation for this pass: **do not return the Sterling hardware yet**. The dual-`48V` path should stay in research/validation until battery support, load-dump mitigation, grounding/isolation, and starter-battery-maintenance strategy are explicitly closed.

## Current project baseline

| Item | Current project state | Why it matters |
| --- | --- | --- |
| House bank | `3x Dumfume 51.2V 100Ah` LiFePO4 in parallel (`15.36 kWh` nominal) | Exact battery is now documented; this improves charge-profile and parallel-bank analysis materially |
| Alternator charging | Sterling `BB1248120` + `BBR` remote | Already purchased; charger output is the current bottleneck |
| Sterling output ceiling | About `1,500 W` max, about `26A` at `57.6V` | This is the real cap on house charging with the current architecture |
| Truck alternator basis | Current docs assume factory `240A` | Relevant for input-side thermal margin, not for raising house-side power above Sterling's limit |
| Purchase-later option | Mechman `370A` `12V` alternator | Helps margin/headroom, but not the `48V` house-side ceiling |

### Practical implication
- Keeping the current Sterling path means all vehicle-side upgrades are still filtered through a charger capped near `1.5 kW`.
- Moving to a dedicated `48V` secondary alternator is the first option that could materially exceed the current alternator-to-house charge power.

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
- If you replace Sterling completely, you should assume starter-battery trickle/maintenance becomes a **separate design problem** unless proven otherwise.

### Likely replacement paths if you want that feature back
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

| Option | House charge ceiling | Integration complexity | Battery/BMS risk | Starter-battery support | Schedule risk | Current recommendation |
| --- | --- | --- | --- | --- | --- | --- |
| Keep Sterling as-is | `~1.0-1.5 kW` depending `BBR` setting | Low | Low-Medium | Possible, but verify exact SKU behavior | Low | Best short-term path |
| Add `370A` `12V` alternator and keep Sterling | Still `~1.0-1.5 kW` | Medium | Low-Medium | Same as Sterling path | Medium | Only if truck-side headroom is the problem |
| Move to Mechman `48V` secondary alternator | Potentially `>2.5 kW` and much higher at usable shaft speed | High | High for non-CAN/internal-BMS bank | Not inherent | High | Promising, but not yet de-risked enough to replace Sterling |

## Decision for this pass

### Recommended position now
- Keep the current Sterling architecture as the active baseline for Phase `1`.
- Do **not** return the Sterling charger/remote until the questions below are closed.
- Treat the Mechman `48V` path as a serious future upgrade candidate, not as an already-proven replacement.

### Why
- Fitment looks credible.
- Performance upside is real.
- But your battery/regulator/support risk is still too open for a confident swap decision.

## Required validation before considering the Mechman swap

### Battery support
- Exact battery family is now documented as Dumfume `51.2V 100Ah`; keep the manual in the repo as the local source of truth.
- Confirm with Wakespeed whether this battery is inside or outside their supported-programming path.
- Confirm whether the manual's recommended `20-50A` charge current is intended to scale across the current `1S3P` bank for alternator charging.
- Confirm whether `58.4V` should be treated as the hard alternator charge ceiling and whether any float stage should be reduced or disabled.

### Regulator and protection
- Confirm whether your battery chemistry/BMS behavior requires avalanche-diode protection, a battery-protection device, keeper battery strategy, or another specific mitigation.
- Confirm exact `WS500` accessory set still needed for your final architecture, especially if Cerbo integration is desired.
- Confirm whether the existing Victron `SmartShunt` stays only as a monitoring device while the WS500 uses its own included analog shunt.

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
- Define how the starter battery will be maintained if Sterling is removed.
- Decide whether losing automatic house-to-starting-battery support is acceptable.

## Questions to send vendors

### To Mechman
1. Will `GZDB-20-1AC-775048V-LFP` fit a `2021 Ford F-350` pickup with the `7.3L` gas engine on my exact VIN/configuration?
2. What output should I expect from this kit at hot idle, fast idle, and normal driving RPM on the `7.3L` Godzilla?
3. Is the alternator negative isolated from the case, or should the `48V` system be treated as engine/chassis referenced?
4. Does this `48V` alternator include or require avalanche-diode/load-dump protection for internal-BMS lithium banks that can self-disconnect?
5. Can you pre-program the `WS500` for `3x Dumfume 51.2V 100Ah` parallel batteries with internal BMS and no CAN, using a `58.4V` charge target, and does that remain inside warranty support?
6. Exactly which Wakespeed accessories are included in the kit, and which Cerbo-integration pieces are extra?

### To Wakespeed
1. Is the Dumfume `51.2V 100Ah` battery on your supported list?
2. If not, what mitigation is mandatory for safe charging with an internal-BMS, non-CAN `48V` lithium bank?
3. Does DVCC/Cerbo provide any meaningful substitute for missing battery-CAN lockout in this case, or is it monitoring-only?
4. What is the recommended fault-handling strategy if the battery BMS disconnects under charge?

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
- A clean starter-battery-maintenance plan exists after Sterling removal

## Sources used in this pass
- [Project BOM baseline](../bom/bom_estimated_items.csv)
- [Current systems baseline](./SYSTEMS.md)
- [Current project decision/risk log](./TRACKING.md)
- [Dumfume battery manual added to project](../references/Dunfume_36V_48V_100Ah_Battery_-_User_Manual.pdf)
- [2021 Super Duty Pick-Up Order Guide](../references/2021%20Super%20Duty%20Pick-Up%20Order%20Guide.pdf)
- [Mechman 48-Volt Dual Bracket Kit for 2020+ Ford 7.3L Gas Godzilla platform (LiFePO4) - Externally Regulated](https://mechman.com/48-volt-dual-bracket-kit-for-2020-ford-7-3l-gas-godzilla-platform-lifepo4-externally-regulated/)
- [Mechman 48-Volt Elite, Externally Regulated (`B820648V-LFP`)](https://mechman.com/content/instructional-pdfs/B820648V-LFP.pdf)
- [Mechman 370A alternator for Ford `5.0L` Coyote and Ford `7.3L` Godzilla (`11532370`)](https://mechman.com/370-amp-alternator-for-ford-5-0l-coyote-and-ford-7-3l-godzilla/)
- [Wakespeed Learn: performance, Cerbo/DVCC, smart shunts, battery support FAQ](https://www.wakespeed.com/learn)
- [Sterling reverse-charging `12V/24V -> 48V` product page](https://sterling-power.com/products/12v-to-48v-1500w-battery-to-battery-charger-w-reverse-charging-feature)
- [Sterling unidirectional / no-reverse-charge `12V/24V -> 48V` product page](https://sterling-power.com/products/12v-24v-to-48v-battery-to-battery-charger-uni-directional-charging-does-not-reverse-charge)
