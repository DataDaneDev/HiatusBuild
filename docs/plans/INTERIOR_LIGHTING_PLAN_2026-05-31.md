# Interior Lighting Plan — Amazon-First Rev B

_As of 2026-05-31 11:37 MDT. Planning draft based on current working lengths: upper strips about 7 ft per side; lower/aisle strip about 6 ft total._

## Decision summary

Use **two lighting zones**, not four:

1. **Upper white wash** — the main style lighting. Two upper corner runs, about 7 ft each side, mounted at the ~47 in upper corners and aimed down/inward through 45° diffuser channel. Use high-density **CCT tunable white COB/FCOB** so the camper can run warm/cozy or cleaner task-white.
2. **Lower utility/night strip** — one 6 ft strip, placed low enough to work as aisle/kick light and rear-entry glow. Choose either:
   - **Recommended flexible version:** RGBCCT strip, so the same lower strip can be warm white, amber-ish, or red.
   - **Simpler version:** fixed 3000K warm white on a rotary dimmer. Add a small red light later only if needed.

This eliminates the redundant under-desk + aisle/kick split. The lower strip should be installed once, low and indirect, where it can serve both night path and entry lighting.

## Why 24V still makes sense here

The previous Rev A was overbuilt, but the **24V decision still holds** because the Amazon LED-strip ecosystem is good and a cheap buck converter is enough. Do **not** use a Victron Orion-Tr just for these lights.

With Dane's corrected lengths:

```text
Upper CCT: 14 ft total using BTF 48W/16.4ft strip
  = ~41.0W = ~1.71A @ 24V

Lower 6 ft RGBCCT/warm strip
  = ~17.6W to ~26.3W depending strip/controller assumption
  = ~0.73A to ~1.10A @ 24V

Total likely max
  = ~58.5W to ~67.3W
  = ~2.44A to ~2.80A @ 24V
  = only ~1.2A to ~1.4A from the 48V bus before converter losses
```

A cheap **48V nominal to 24V 10A / 240W buck converter** has plenty of headroom. Fuse it correctly and keep it accessible.

## Recommended build — balanced and flexible

### Zone 1 — upper CCT white wash

**Use:** normal style light, warm evening light, cleaner useful white when desired.

**Buy:**

- **BTF-LIGHTING FCOB COB CCT 24V LED Strip, 3000K–6000K, IP65, CRI 90+, 16.4 ft, 640 LEDs/m**
  - Amazon: https://www.amazon.com/BTF-LIGHTING-Flexible-3000K-6000K-Decoration-Controller/dp/B0C8D4JNJK
  - Notes: one 16.4 ft roll should cover two 7 ft upper runs if cut and wired as two parallel outputs from the same controller.
  - Why this over the old 12V listing: same general product class, but lower current and cleaner for split left/right camper runs.

**Controller:**

- **LGIDTECH / MiBoxer FUT035S CCT dual-white LED strip controller, 12–24V**
  - Amazon: https://www.amazon.com/LGIDTECH-FUT035S-Miboxer-Controller-12-24V/dp/B0B1WDKTGL
  - Purpose: CCT controller for + / WW / CW strip wiring.

**Remote:**

- **LGIDTECH FUT007 / MiLight CCT 4-zone remote**
  - Amazon: https://www.amazon.com/LGIDTECH-Mi-Light-Controller-Temperature-Changeable/dp/B075JDLHCY
  - Buy two if front + rear control matters: one mounted near bed/front, one mounted near rear/barn doors.
  - Note: confirm both remotes can pair to the same controller during bench test. MiBoxer/MiLight ecosystem generally supports multi-remote pairing, but verify before burying anything.

**Optional nicer remote:**

- **MiBoxer FUT006 rotating-wheel CCT remote**
  - Amazon: https://www.amazon.com/FUT006-Rotating-Brightness-Temperature-Adjustable/dp/B0DNRCHC6N
  - Better interface, more expensive. Buy only if the cheap FUT007 feels annoying.

**Mounting channel:**

- **Muzata V-shape / 45° LED aluminum channel with milky diffuser, 10 pack, 3.3 ft**
  - Amazon: https://www.amazon.com/Aluminum-Muzata-Channels-Diffusers-Mounting/dp/B01MS89UER
  - Silver 1 m sections; enough for upper and lower if cuts are planned well.

Alternative black/longer channel:

- **Muzata V-shape black 6.6 ft channel, 10 pack**
  - Amazon: https://www.amazon.com/Muzata-Channel-Diffuser-Aluminum-Extrusion/dp/B083JC6M14
  - Cleaner if black hardware aesthetic matters, but much more expensive/overkill for this small install.

### Zone 2 — lower multipurpose night / aisle / red strip

**Recommended flexible version:** one RGBCCT strip. It can be:

- warm white for aisle glow;
- amber/orange-ish near the rear doors for bug reduction;
- red for night vision / low-disturbance ingress;
- dim decorative color if desired.

**Buy:**

- **BTF-LIGHTING FCOB COB RGBCCT 24V LED Strip, RGB + tunable white 3000K–6000K, 16.4 ft, 960 LEDs/m, 12 mm width**
  - Amazon: https://www.amazon.com/BTF-LIGHTING-Temperature-3000K-6000K-Decoration-Controller/dp/B0C49QSTJ7
  - Notes: use only about 6 ft. This is not the best “true white” source, but it is good enough for a low indirect utility/night strip and avoids a separate red circuit.
  - Caveat: 12 mm wide, so verify channel width. Many small channels only fit 10 mm strips.

**Controller + remote kit:**

- **MiBoxer FUT043A+ 3-in-1 RGB/RGBW/RGB+CCT LED controller kit with 2.4GHz remote, 12–24V**
  - Amazon: https://www.amazon.com/DC12-24V-Wireless-Remote-Control-Controller/dp/B08CRCQ75W
  - Purpose: runs the RGBCCT lower strip with white/CCT/red/color modes.

**Second remote if front + rear control matters:**

- **MiBoxer FUT088 RGB+CCT remote**
  - Amazon: https://www.amazon.com/Miboxer-FUT088-Remote-Battery-Included/dp/B0DPNHPB2G
  - Buy one extra if the lower strip needs both bed/front and rear control.

**Mounting channel for RGBCCT lower strip:**

Because the RGBCCT strip is 12 mm wide, do not assume every small V-channel fits. Use one of these approaches:

- Use a **wider 12 mm+ compatible channel** after confirming dimensions on the selected Amazon listing.
- Or mount the RGBCCT strip in a protected flat/recessed channel under a lip where the LEDs are not directly visible.
- If using the Muzata V-channel above, verify actual inner width before committing to the 12 mm lower strip.

## Simpler lower-light alternative — rotary dimmer version

If the lower RGBCCT controller feels like controller creep, use fixed warm white and a knob.

**Buy:**

- **BTF-LIGHTING FCOB COB LED Strip Warm White 3000K, 24V, 16.4 ft, CRI 90+, 8 mm width**
  - Amazon: https://www.amazon.com/BTF-LIGHTING-Flexible-Dimmable-Deformable-Decoration/dp/B089NLLTCT
  - Use about 6 ft low and indirect.

**Rotary dimmer:**

- **SUPERNIGHT DC12V–24V 30A PWM rotary LED dimmer with aluminum housing**
  - Amazon: https://www.amazon.com/SUPERNIGHT-DC12V-24V-Controller-Brightness-Aluminum/dp/B07HN1BJWK
  - Cheap, simple, plenty of current capacity for a 6 ft warm-white lower strip.

**Smaller waterproof automotive/marine-ish dimmer:**

- **Oznium mini LED dimmer knob, 12–24V, waterproof, 2.4A @ 24V**
  - Amazon: https://www.amazon.com/Oznium-Dimmer-Rotary-Control-Switch/dp/B085TK13SH
  - More expensive but physically better for a vehicle install. Current is still enough for a 6 ft warm-white strip, but not for a large full-length zone.

**Rotary-dimmer limitation:**

A plain rotary PWM dimmer is effectively a **one-location control**. You can put it at the rear or at the bed/front, but not both without adding relay/momentary/RF complexity. Do not put two PWM dimmers in series or tie two dimmer outputs together.

Default if choosing rotary: put the lower-light rotary near the **rear/barn doors**, because entry/night use matters most there. The upper CCT zone can still have front/rear RF remotes.

## 48V to 24V power

**Buy:**

- **DC 36V/48V to 24V 10A 240W converter, 30–60V input, waterproof buck module**
  - Amazon: https://www.amazon.com/Voltage-Regulator-Converter-Waterproof-Transformer/dp/B089LRQM9Z
  - Verified Amazon product bullets: input range 30–60V, output 24V 10A/240W, over-current/over-load/short/over-temp protections, waterproof potted aluminum shell.

**Why this instead of Orion-Tr:**

- The lighting load is likely under 70W max.
- The converter is not charging batteries or feeding critical electronics.
- A cheap potted converter is acceptable if fused, accessible, strain-relieved, and treated as replaceable.

**Caveats:**

- Hiatus 48V LiFePO4 charging can approach the high 50V range; do not buy a converter with an input max below 60V.
- Keep the converter accessible; do not bury it permanently.
- Fuse the 48V input and 24V output or use a small fused distribution point.

## Fuse / wiring / connection components

**Inline fuse holder — cheap/small install:**

- **Blue Sea Systems 5065 waterproof in-line ATO/ATC fuse holder**
  - Amazon: https://www.amazon.com/Blue-Sea-Systems-Waterproof-Holder/dp/B004ZIUA62
  - Use for the converter input or a simple protected branch if the main fuse block is not already handling it.

Budget multi-pack:

- **DaierTek 12 AWG waterproof ATO/ATC inline fuse holders, 10 pack**
  - Amazon: https://www.amazon.com/DaierTek-Inline-Holder-Waterproof-Automotive/dp/B09CYRQ46S

**Wire:**

- **Ancor Marine Grade Duplex Cable, 16/2 AWG, 100 ft**
  - Amazon: https://www.amazon.com/Ancor-Marine-Grade-Duplex-Cables/dp/B000NV0BNM
  - Use for most lighting branches.

Budget tinned duplex option:

- **16 AWG duplex marine-grade tinned copper wire, 50 ft**
  - Amazon: https://www.amazon.com/Marine-Duplex-Battery-Automotive-Outdoors/dp/B0BWMNB6JP

**Accessible splices / distribution:**

- **WAGO 221 lever nut assortment**
  - Amazon: https://www.amazon.com/Compact-Splicing-Connector-Assortment-221-2401/dp/B0CJ5QF4Z2
  - Use only in dry, accessible enclosures/behind removable panels. Add strain relief; do not leave WAGOs loose in a hidden vibrating cavity.

## Physical layout recommendation

### Upper strips

- Install one ~7 ft run per side.
- Mount high in the upper side/corner transition at about 47 in.
- Use 45° channel with diffuser.
- Aim down/inward, not directly at eyes.
- Wire left and right upper strips in parallel from the same CCT controller output.
- Leave controller accessible in an electrical/service area.

### Lower strip

Best default placement: **low kick/aisle lip**, not under both desk and galley separately.

- One ~6 ft lower run is enough.
- Put it under a toe-kick/ledge/lower cabinet lip where the LED emitter is hidden.
- It should throw across the floor/aisle, not directly across your eyes while lying in bed.
- If using RGBCCT, make default presets/scenes:
  - warm white low = normal night path;
  - red low = night/bug/entry;
  - amber/orange low = door-open bug mode.

## Buying recommendation

### Recommended cart — flexible but still sane

- 1× BTF 24V CCT 16.4 ft upper strip: https://www.amazon.com/BTF-LIGHTING-Flexible-3000K-6000K-Decoration-Controller/dp/B0C8D4JNJK
- 1× MiBoxer/LGIDTECH FUT035S CCT controller: https://www.amazon.com/LGIDTECH-FUT035S-Miboxer-Controller-12-24V/dp/B0B1WDKTGL
- 2× FUT007 CCT remotes: https://www.amazon.com/LGIDTECH-Mi-Light-Controller-Temperature-Changeable/dp/B075JDLHCY
- 1× BTF 24V RGBCCT 16.4 ft lower strip: https://www.amazon.com/BTF-LIGHTING-Temperature-3000K-6000K-Decoration-Controller/dp/B0C49QSTJ7
- 1× MiBoxer FUT043A+ RGB/RGBW/RGBCCT controller kit: https://www.amazon.com/DC12-24V-Wireless-Remote-Control-Controller/dp/B08CRCQ75W
- Optional 1× extra FUT088 RGB+CCT remote: https://www.amazon.com/Miboxer-FUT088-Remote-Battery-Included/dp/B0DPNHPB2G
- 1× 48V-to-24V 10A converter: https://www.amazon.com/Voltage-Regulator-Converter-Waterproof-Transformer/dp/B089LRQM9Z
- 1× Muzata V-channel pack: https://www.amazon.com/Aluminum-Muzata-Channels-Diffusers-Mounting/dp/B01MS89UER
- 1× Blue Sea inline fuse holder: https://www.amazon.com/Blue-Sea-Systems-Waterproof-Holder/dp/B004ZIUA62
- 1× 16/2 tinned duplex wire: https://www.amazon.com/Ancor-Marine-Grade-Duplex-Cables/dp/B000NV0BNM
- 1× WAGO 221 assortment: https://www.amazon.com/Compact-Splicing-Connector-Assortment-221-2401/dp/B0CJ5QF4Z2

### Simpler cart — fewer controllers

- Upper CCT items from above.
- Replace lower RGBCCT/controller/remotes with:
  - 1× BTF 24V 3000K warm-white FCOB strip: https://www.amazon.com/BTF-LIGHTING-Flexible-Dimmable-Deformable-Decoration/dp/B089NLLTCT
  - 1× SUPERNIGHT rotary PWM dimmer: https://www.amazon.com/SUPERNIGHT-DC12V-24V-Controller-Brightness-Aluminum/dp/B07HN1BJWK
- Accept that lower light has only one physical dimmer location and no red unless added later.

## Bench-test checklist before install

1. Power the 48V-to-24V converter from a fused 48V source or bench supply.
2. Confirm 24V output with meter before connecting controllers.
3. Connect upper CCT strip/controller/remotes on bench.
4. Confirm CCT direction is logical; if warm/cool are reversed, swap WW/CW outputs.
5. Pair both upper remotes before mounting.
6. Connect lower RGBCCT strip/controller; confirm red, warm white, dimming, and off state.
7. Confirm controller memory behavior after power loss.
8. Only after bench success: cut strips to final lengths, solder/strain-relieve pigtails, install channels, then mount diffusers.

## Procurement hold points

- Confirm whether lower strip will be **RGBCCT flexible** or **fixed warm-white rotary**.
- Confirm channel inner width for the 12 mm RGBCCT strip before buying/mounting the lower channel.
- Confirm controller/remote pairing behavior on the bench before burying any wiring.
- Do not rely on LED tape adhesive alone; fasten the aluminum channel mechanically where practical.
