---
aliases:
  - Camper audio system
  - Hiatus camper stereo
  - Camper subwoofer plan
tags:
  - hiatus/implementation
  - hiatus/audio
  - hiatus/electrical
  - hiatus/interior
status: draft
related:
  - "[[SYSTEMS]]"
  - "[[ELECTRICAL_overview_diagram]]"
  - "[[ELECTRICAL_fuse_schedule]]"
  - "[[INTERIOR_driver_side_workstation]]"
  - "[[INTERIOR_furniture_layout_and_galley]]"
---

# Camper Audio System

As-of date: `2026-06-01`

Purpose: define a compact, budget-conscious camper audio system with strong bass, good-enough cabin sound, simple tablet integration, and explicit `12V` wiring/fusing. This is the camper-only system; truck-cab driving subwoofers remain a separate truck audio project.

## Design target

Goals, in priority order:

1. Strong bass in the small camper volume.
2. Good, clear audio without audiophile cost or tuning complexity.
3. Compact packaging that fits the driver-side electrical/workstation module or adjacent dry bench volume.
4. Simple source control from the Samsung `S11 Ultra` tablet.
5. Serviceable wiring with source fusing and controlled DC returns to the camper `12V` distribution system.

Non-goals:

- Do not use camper speakers/subs as the truck-cab driving audio system.
- Do not tie random audio grounds to the shell, truck bed, or chassis just to imitate a car-audio install.
- Do not add a big standalone home-theater inverter load for audio; keep the camper audio DC-first.

## Selected system package

Default package is a simple `2.1` system: Kicker marine/powersports source unit powers a pair of full-range speakers directly, with RCA line-out and remote turn-on feeding a powered down-firing subwoofer.

| Function | Selected product | Link | Planning notes |
| --- | --- | --- | --- |
| Source / tablet interface / speaker amp | Kicker `46KMC2` marine media receiver | https://www.kicker.com/46KMC2 | Bluetooth from `S11 Ultra`, USB/aux backup, `25W x 4` at `4 ohm`, `15A` ATM fuse, `2.5V` RCA line-out, remote amp turn-on output. |
| Main speakers | Kicker `CSC67` 6.75 in coaxial speakers, `4 ohm` | https://www.kicker.com/CSC67-Coaxial-Speakers-4-Ohm | Use one pair on front left/right channels. Speaker spec: 6.75 in, `4 ohm` class, `3.3 ohm` DC resistance, 90 dB sensitivity, 40 Hz-20 kHz range, 2-1/16 in bottom-mount depth. |
| Powered subwoofer | Kicker `49PTRTP10` powered down-firing 10 in enclosure | https://www.kicker.com/PTRTP10 | Built-in amp, `400W RMS @ 14.4V`, 25-120 Hz response, 6 in H x 25-5/8 in W x 13-1/4 in D, remote bass knob included. Manual calls for `4 AWG` power/ground and external `40A` fuse. |
| Sub power kit basis | Kicker marine `47KMPK4` 4 AWG amp power kit | https://www.kicker.com/marine-amp-power-kits | Tinned OFC marine cable basis. Kit includes `4 AWG` red/yellow power/ground and marine fuse hardware; replace/fit fuse value to the PTRTP10-required `40A`, not the kit's larger generic fuse. |
| RCA signal cable | Kicker K-Series 2-channel RCA cable, length to measured route | https://www.kicker.com/2-channel-4-meter-rca-cable-k-series | Use measured length; route away from 4 AWG power and high-current DC conductors. |
| Speaker wire | Kicker marine speaker wire | https://www.kicker.com/marine-speaker-wire | Use `16 AWG` marine speaker wire for the two speaker runs; do not run speaker negatives to chassis/shell. |

Estimated purchase bucket: about `$950-$1,100` before tax/shipping depending on retailer and wiring kit pricing. This intentionally buys bass first and avoids a separate full-range amplifier/DSP for Phase 1.

## Impedance and audio topology

- KMC2 speaker outputs expect `4 ohm` stereo loads.
- Wire one `CSC67` speaker to KMC2 front-left and one `CSC67` speaker to KMC2 front-right.
- Do not parallel speakers on one KMC2 channel.
- Cap/secure unused rear-left/rear-right speaker outputs for future expansion.
- Feed the PTRTP10 with the KMC2 RCA line-out. If the single RCA pre-out feeds only the sub, set sub low-pass at the powered subwoofer.
- KMC2 remote amp turn-on output feeds the PTRTP10 remote input with `18 AWG` low-current wire.
- Tablet source path: `S11 Ultra -> Bluetooth -> KMC2 -> speakers + RCA line-out -> PTRTP10`.
- Backup source path: `S11 Ultra USB/aux or local USB media -> KMC2` if Bluetooth behavior is annoying.

## Placement and packaging

Recommended default:

- Mount the KMC2 in the driver-side electrical/workstation/DC-shelf face where it is reachable from the desk/entry but not in a knee-impact zone.
- Mount the PTRTP10 low in a dry driver-side toe-kick/step-box volume or under the dry side of the battery/bench module, near the `12V` junction. Keep it out of the passenger-side wet spine and any plumbing leak path.
- Keep the powered sub serviceable: removable cover/panel, remote bass knob accessible, fuse accessible, and enough ventilation around the built-in amp side.
- Place the two `CSC67` speakers high/mid on opposite sides or opposite front corners, angled into the living/work zone. Final speaker cuts wait until wall panel thickness, roof sweep, window shade path, and cabinet face geometry are measured.
- If flush-mounting is not practical, use shallow surface pods or a removable baffle panel rather than cutting shell/fabric/structural members.

Mounting gates before cutting holes:

1. Verify speaker back-side depth: `CSC67` bottom-mount depth is about `2-1/16 in`; add terminal clearance and wire strain relief.
2. Verify KMC2 round/gauge-style cutout and rear wiring depth against the DC-shelf panel.
3. Verify PTRTP10 footprint: about `6 in H x 25-5/8 in W x 13-1/4 in D`, plus cable bend radius and ventilation.
4. Run roof-down sweep and panel/service removal checks before final speaker or source-unit cutouts.
5. Add positive mechanical retention for the powered sub; do not rely on friction or mass.

## DC power and fusing

This audio system lives on the camper `12V` distribution side. It does not get a new `48V` branch.

### Source unit branch: `12V-12 / AUDIO-HU`

- Source: existing `12V` fuse block / shared `12V` junction.
- Fuse: `15A` branch fuse at the `12V` fuse block; preserve the KMC2 harness `15A ATM` fuse shown in the KMC2 manual.
- Positive conductor: `12 AWG duplex` if the one-way run is kept around `5 ft`; use `10 AWG` if the final route is closer to `8 ft` or longer.
- Negative conductor: return in the same duplex cable to the `12V` negative bus/main negative stud. Do not use shell/chassis return.
- KMC2 yellow/battery and red/switched leads: for camper use, feed through the fused branch and add a small local switch or switched feed if you want the head unit truly off without opening the house system. Avoid always-on parasitic draw if storage behavior becomes annoying.

### Powered subwoofer branch: `12V-AUDIO-SUB`

- Source: `12V` source-combine/main positive stud or a rated positive distribution point downstream of `SW-12V-BATT`.
- Fuse: external `40A` fuse within about `18 in` of the `12V` source takeoff, matching the PTRTP10 manual.
- Positive conductor: `4 AWG` tinned/OFC from source fuse to PTRTP10 positive input.
- Negative conductor: matching `4 AWG` return from PTRTP10 negative input to the `12V` negative bus/main negative stud. Keep the return short if the sub is mounted near the electrical/DC shelf; otherwise run the paired return rather than bonding locally to random metal.
- Remote turn-on: `18 AWG` from KMC2 remote output to PTRTP10 remote input.
- Signal: shielded 2-channel RCA from KMC2 line-out to PTRTP10 RCA input, routed separately from the 4 AWG power run where practical.

### 12V capacity note

The KMC2 branch is `15A` max and the PTRTP10 branch is `40A` max, so audio can theoretically demand about `55A` at `12V` during heavy bass peaks. The Orion-Tr Smart `48/12-30` is only a `30A` continuous charger/feed into the shared `12V` system. The `12V 100Ah` buffer battery can support transients and short loud sessions, but sustained loud use above Orion output will slowly discharge the `12V` buffer battery until the average audio load drops or the system recharges.

Operational rule: loud music is fine; do not treat the camper audio system as a continuous `55A` load while also maxing USB-C, Starlink, lights, fan, fridge, and heater without watching `12V` battery voltage/SOC.

## Wire routing

- Keep audio power and return conductors paired and secured with P-clamps or mechanical cable mounts.
- Keep the 4 AWG sub power run low, short, and protected in loom wherever it passes through storage or service compartments.
- Cross RCA/speaker signal wires over high-current DC at `90 degrees` when they must cross; avoid long parallel runs next to 4 AWG/2/0 DC conductors.
- Route speaker wire above cabinet service zones, with drip loops avoided near wet-spine plumbing.
- Label both ends of every audio conductor:
  - `AUDIO-HU + / -`
  - `AUDIO-SUB + / -`
  - `AUDIO-REM`
  - `AUDIO-RCA`
  - `SPK-L + / -`
  - `SPK-R + / -`
- Add strain relief at the KMC2, PTRTP10 quick-connect/power plug, and speaker terminals.

## Initial tuning

Start conservative:

1. KMC2 loudness off unless low-volume listening needs it.
2. PTRTP10 low-pass around `80 Hz`.
3. PTRTP10 phase switch: test `0` and `180`; keep whichever gives stronger/cleaner bass at the desk/bench listening position.
4. Bass boost: start at `0`; add only enough to fill the camper at low volume.
5. Gain: set with normal tablet/KMC2 volume near expected maximum clean listening level; do not use gain as a volume knob.
6. Use the remote bass knob as the everyday bass trim so nighttime/quiet-camp mode is easy.

## Future upgrade path

Only upgrade if the simple system disappoints:

- Add a compact 4-channel amp/DSP such as Kicker `KEY200.4` for the coaxial speakers if the KMC2 internal `25W x 4` amp is not clean/loud enough.
- If adding that amp, create a second fused amp branch and revisit total `12V` current budget; do not silently stack it onto the KMC2 branch.
- Add a second speaker pair only if wall/panel placement proves clean and the KMC2 channel count remains one `4 ohm` speaker per channel.

## Open validation items

- Final KMC2 mounting face and rear wiring depth in the driver-side DC shelf.
- Final PTRTP10 physical location that preserves dry separation, service access, ventilation, and short 4 AWG run.
- Final speaker baffle/pod method after wall panel thickness and roof-down sweep are known.
- Exact RCA/speaker-wire lengths after furniture mockup.
- Verify actual `12V` buffer battery voltage sag during a loud music test with Starlink/fridge/fan also running.
