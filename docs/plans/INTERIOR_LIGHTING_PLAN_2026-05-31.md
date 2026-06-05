---
aliases:
  - Interior lighting plan
  - Camper lighting plan
  - WLED lighting design
tags:
  - hiatus/plan
  - hiatus/lighting
  - hiatus/electrical
status: deferred-design
related:
  - "[[SYSTEMS]]"
  - "[[ELECTRICAL_overview_diagram]]"
  - "[[PROJECT_build_order_of_operations]]"
---

# Interior Lighting Plan — 12V WLED / QuinLED Design

_As of 2026-06-05 11:28 MDT. This overwrites the prior `24V`/MiBoxer worksheet. Lighting is **not a near-term install task**; preserve this desired design and defer procurement/install until after plumbing, Starlink, solar, alternator, and core furniture work are farther along._

## Current decision

Use a **single 12V WLED/ESP32 lighting system** built around a central analog PWM controller, not separate MiBoxer RF controller/remotes.

Default architecture:

```text
12V-11 lighting branch -> central QuinLED An-Penta-Deca -> analog PWM outputs -> LED strips
                                      |
                                      +-> hardwired momentary buttons / WLED app / future API control
```

Design intent:

- Keep lighting on the existing dedicated `12V-11` lighting branch.
- Avoid a separate `24V` lighting converter unless a later measured reason justifies reopening the voltage architecture.
- Avoid multiple proprietary RF remotes and remote batteries.
- Make daily control feel camper-native: hardwired buttons for common actions, WLED/app/API only for setup and advanced control.
- Keep the controller accessible for firmware/config/service; do not bury it behind fixed furniture.

## Deferred status / build sequence

Do not buy or install this lighting package now. Current priority remains:

1. Plumbing / wet-spine rough-in.
2. Starlink and solar mounting/routing.
3. Alternator charging path.
4. Furniture/extrusion structure and real service envelopes.
5. Lighting procurement and install after final channel locations, wire paths, and button positions are physically known.

Preserve rough-in opportunities while building furniture: small wire chases, removable panels, and low-voltage button paths are useful even before final LED SKU lock.

## Zone layout

Use **two lighting zones**, not four.

### Zone 1 — upper CCT white wash

Purpose:

- Main interior light.
- Warm evening light.
- Cleaner neutral/task white for work, cleaning, and setup.

Physical layout:

- Two upper runs, about `7 ft` per side.
- Mount high in the side/roof corner area near the upper build envelope.
- Use 45-degree aluminum channel with milky diffuser.
- Aim down/inward, not into eyes.
- Treat left and right runs as one logical upper zone unless later testing proves a real need for side-by-side independent control.

Electrical/control:

- Use CCT/tunable-white strip: common positive plus `WW` and `CW` PWM returns.
- Uses `2` PWM channels on the QuinLED controller.

Preferred product class:

- BTF-LIGHTING FCOB/COB CCT strip, `12V`, high density, CRI90+, about `10 mm` wide.
- Product-family anchor: <https://www.btf-lighting.com/collections/cct-fcob-5v-12v-24v/products/fcob-cct-640leds-10mm-ra90-dimmable-dc12v-dc24v>

### Zone 2 — lower multipurpose night / aisle / entry strip

Purpose:

- Low night path.
- Rear/entry glow.
- Red low-light mode.
- Amber/orange-ish door-open/bug-reduction mode.
- Low warm-white floor wash.

Physical layout:

- One lower indirect run, about `6 ft` total.
- Place low under a toe-kick, ledge, bench lip, or lower cabinet edge where the emitter is hidden.
- Throw light across the floor/aisle, not directly at the bed or work position.
- Do not split into separate under-desk and aisle systems unless a measured use case appears later.

Electrical/control:

- Use RGBCCT strip: common positive plus `R`, `G`, `B`, `WW`, `CW` PWM returns.
- Uses `5` PWM channels on the QuinLED controller.

Preferred product class:

- BTF-LIGHTING 5050 RGBCCT 5-in-1 strip, `12V`, common-positive analog strip.
- Product-family anchors:
  - <https://www.btf-lighting.com/collections/5050-rgbw-5in1-led-strip/products/5050-rgbcct-5-colors-in-1-6pin-112leds-led-strip-dimmable-tunable-color-temperature-3000k-6500k-1>
  - <https://www.btf-lighting.com/collections/5050-rgbw-5in1-led-strip/products/dc-12v-24v-5050-rgbcct-5in1-led-light-96leds>

Caveat: RGBCCT strips are often wider than simple white/CCT strips. Confirm channel inner width before buying channel or committing a slot/ledge detail.

## Controller baseline

Preferred controller:

- **QuinLED An-Penta-Deca** analog PWM controller.
- Product page: <https://quinled.info/quinled-an-penta-deca/>
- Buying page: <https://quinled.info/an-penta-deca-buying-page/>
- Terminal reference: <https://quinled.info/quinled-an-penta-deca-board-terminals/>

Why this controller:

- `15` analog PWM channels; current design needs `7` channels (`2` upper CCT + `5` lower RGBCCT), leaving `8` spare.
- `12V-48V` compatible, so it can run directly from the `12V-11` branch.
- WLED preinstalled; also compatible with ESPHome if the system later moves toward Home Assistant.
- Dedicated button inputs and documented terminals.
- Better documented and more integrated than separate MiBoxer RF controllers/remotes.

Channel allocation draft:

```text
L1  Upper WW
L2  Upper CW
L3  Lower R
L4  Lower G
L5  Lower B
L6  Lower WW
L7  Lower CW
L8-L15 spare / future cabinet / task / exterior-low-light expansion
```

Final channel order can change during bench setup if WLED configuration is easier another way; keep the documented as-built mapping updated after install.

## Load planning

Prior strip-length math put the expected full-light load around `58.5-67.3W`, which is about `4.88-5.61A @ 12V`. Use an `80W` / `~6.7A @ 12V` design allowance unless final strips prove lower.

Planning implications:

- The load is modest relative to the camper electrical system.
- Keep it on a fused `12V` lighting branch, but verify final `12V-11` fuse and conductor sizing against the selected strip wattage and actual run lengths.
- Keep the controller and any strip power injection points accessible.
- If future expansion adds exterior/task lighting to the spare channels, recalc the branch load before assuming the same fuse/conductor remains correct.

## Physical controls

Use hardwired momentary buttons for normal daily control.

QuinLED An-Penta-Deca button-terminal facts:

- `3` dedicated button pins.
- Inputs are pulled high through debounce circuitry.
- Short the input to `GND` to trigger.
- The button wiring is logic-level only; it does not carry LED power.

Wiring pattern:

```text
QuinLED button input -> normally-open momentary button -> QuinLED GND
```

Button placement baseline:

1. **Rear/entry button**
   - Single press: lower warm/amber entry light.
   - Long press: dim/ramp lower light.
   - Double press: all off.

2. **Desk/bench button**
   - Single press: upper work light.
   - Long press: dim/ramp upper light.
   - Double press: warm lounge scene.

3. **Bed button**
   - Single press: red night mode.
   - Long press: dim/ramp night mode.
   - Double press: all off.

Duplicate buttons for the same function can usually be wired in parallel to the same input. Use separate inputs only when the actions need to be different.

If more than three distinct control locations/actions become necessary, consider the generic GPIO, an I2C/GPIO expansion approach, or a small secondary ESP/Home Assistant button node. Do not overbuild this until the furniture and sleep/work positions are physically proven.

## Remote / app / automation control

WLED gives several non-MiBoxer control paths:

- **Primary setup/control:** WLED web UI or WLED app over local WiFi.
- **Future integration:** JSON API, HTTP API, MQTT, Home Assistant, or ESPHome if desired.
- **Optional backup remote:** ESP-NOW/WIZmote-style remote can work without line-of-sight, but still uses batteries; treat as optional convenience, not the primary interface.
- **Avoid as primary:** IR remote. It needs line-of-sight and adds another cheap handheld remote problem.

Relevant WLED references:

- Buttons/macros: <https://kno.wled.ge/features/macros/#buttons>
- JSON API: <https://kno.wled.ge/interfaces/json-api/>
- Infrared / ESP-NOW remotes: <https://kno.wled.ge/interfaces/infrared/>

## Preset design

Create WLED presets before finalizing button actions.

Baseline preset set:

1. `All Off`
2. `Entry Warm` — lower warm/amber low, upper off.
3. `Night Red` — lower red very low, upper off.
4. `Work Light` — upper neutral white medium/high, lower off or very low.
5. `Lounge Warm` — upper warm low/medium, lower warm very low.
6. `Clean / Max` — upper bright neutral/cool, lower warm/white as useful.
7. `Door Bug Mode` — lower amber/orange low, upper off or very low warm.

During bench setup, verify each preset after power loss and after WiFi reconnect. Daily-use buttons should call presets rather than requiring manual color fiddling.

## Wiring and install rules

- Use tinned marine wire where practical.
- Keep LED strip and controller pigtails strain-relieved.
- Use ferrules or appropriate terminals for controller screw terminals where needed.
- Keep WAGO/lever connectors only in dry, accessible, strain-relieved service areas.
- Mechanically retain LED aluminum channel; do not rely on LED tape adhesive alone.
- Keep diffuser/channel sections removable where they cover service screws or panels.
- For analog strips, verify common-positive wiring before applying power; many RGB/RGBCCT strips share `+V` and switch the negative/color channels.
- Bench-test full-length or representative strip sections before cutting final pieces.
- Label channel outputs and pigtails at the controller before final closure.

## Procurement hold points

Before buying lighting parts:

1. Confirm final upper channel path after furniture and roof-close sweep.
2. Confirm final lower strip path after bench/galley/toe-kick geometry is real.
3. Confirm channel inner width for the selected CCT and RGBCCT strips.
4. Confirm selected strips are `12V`, analog/common-positive, and within controller/channel current limits.
5. Confirm final `12V-11` fuse/conductor sizing against selected strip wattage and future spare-channel plans.
6. Decide whether a camper WiFi/router baseline exists by the time lighting is installed; WLED still supports local AP/config modes, but normal use is cleaner on a stable local network.
7. Bench-test controller, strip segments, button inputs, presets, power-loss memory, and app/API access before mounting anything permanently.

## Superseded prior concepts

The previous `24V` converter-backed worksheet and MiBoxer RF controller/remotes are superseded for the desired design.

Keep the old ideas only as fallback references:

- MiBoxer/RF remains acceptable if a fast/simple no-config install is needed later.
- A plain rotary PWM dimmer remains acceptable for a single warm-white lower strip if the whole WLED path is abandoned.
- The current desired path is **12V QuinLED/WLED + hardwired momentary buttons**.
