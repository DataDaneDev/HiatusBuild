## 2026-08-08 — Whole-system WS500 review moved shunt to common battery negative

- Superseded the earlier dedicated alternator-negative-shunt plan after comparing all four credible layouts. Final standalone/no-CAN default now follows Wakespeed's PH-VAN/internal-BMS example: `battery negative combine -> Victron SmartShunt -> Wakespeed 500A/50mV shunt -> Lynx/system negative`, with purple/high toward battery and grey/low toward Lynx; configure `Shunt at Battery`.
- The alternator negative `2/0` now runs directly to Lynx/system negative. This preserves the dedicated return while removing the chassis-bypass dependency that affected an alternator-branch shunt. No purple/grey `5A` fuses are used.
- Replaced the incomplete Littelfuse housing path with a screw-terminal Mersen `USCC1` Class-CC holder and one `ATDR15 15A/300VDC` time-delay fuse in a separate small DC DIN enclosure. Feed PH-VAN red from the `F-04` alternator/load-side stud through short `14 AWG` pigtails and a sealed step-down splice.
- Re-baselined `F-04` from `150A` to `200A/80V`: Mechman's published curve reaches about `145.7A`, and the `125%` basis is about `182A`; `200A` is the next standard size and remains inside the installed `2/0 AWG` cable envelope.

## 2026-08-08 — Wakespeed fuse plan simplified with negative alternator shunt

- Owner rejected the expensive/slow three-small-fuse outcome and requested a proportional re-check. The positive-side Wakespeed shunt would legitimately require separate protection on both full-bank-positive purple/grey sense wires, but positive placement is not mandatory.
- Final build default is the Wakespeed `500A/50mV` shunt in the dedicated `2/0` alternator negative return near the house board: grey/low on the alternator side, purple/high on the Lynx side, `Shunt at Alternator`, and no `5A` sense fuses. This is gated by a de-energized test proving no second Lynx-negative-to-chassis path bypasses the shunt.
- The PH-VAN short red lead still requires its own `15A` protection because it is a `16 AWG` regulator-power/voltage-sense conductor tapped from the `48V` bus. Procurement is narrowed to one `15A/80VDC` Littelfuse `166.7000.5152` or verified equivalent. Littelfuse confirms the owned `178.6150.0001` housing accepts FKS fuses at `80VDC`; only correct contacts/wire fit remain open, and no duplicate commissioning spare is required.

## 2026-08-06 — Starlink package buy list locked; physical-fit and bench gates remain

- Owner selected the TRIO Gen 3 Standard Speedmount, one fixed `NE8FDX-P6-W` panel feedthrough, a matching outdoor Neutrik cable connector, and a budget Amazon `12V` converter with the factory AC supply/inverter retained as fallback.
- Owner-confirmed Mouser order placed `2026-08-06`, pending fulfillment: `1x NE8FDX-P6-W` at `$28.45` and `2x NE8MXR1-B-TOP-D` at `$8.93` / `$17.86` extended. BOM records the `$46.31` item subtotal; the owner-reported `$54.80` checkout total leaves an unitemized `$8.49` shipping/tax difference that is not allocated to component rows.
- Owner-confirmed TRIO order placed `2026-08-06`, pending fulfillment: white Gen 3 Standard Speedmount with `75 mm` stainless through-bolting hardware at `$285`, four rubber-coated magnets at `$40`, and VHB-backed magnet mounting discs at `$40`; `$365` total with free shipping. The `75 mm` set is frame-to-extrusion hardware and does not replace separate roof-track-to-extrusion T-bolts.
- Replaced the `$58.99` STARGEAR adapter-pair lead with the `$19.99` Prime-only (`$25.99` regular) AUDEETO two-pack: one passive Gen 3 weather/retention pigtail at the terminal and one at Router 3. These are connector/retention adapters, not voltage or protocol converters, and remain continuity/shield/heat/retention bench-test gated because the listing has limited history and claims `26 AWG` pigtails.
- Clarified factory-cable modes: direct OEM terminal-to-router through the existing service route remains the fewest-interface recovery path. Optional use through the Neutrik panel needs one `$12.99` female/female Gen 3/Cat6-Cat7 coupler plus a short shielded RJ45-to-Neutrik TOP jumper. A third male device pigtail does not directly mate to the male factory-cable end.
- Final cable-side preference is `NE8MXR1-B-TOP-D`, not indoor `NE8MX-B-1`: it includes the matched Cat6A plug/wire manager, accepts `5.5-8.0 mm` cable OD and AWG `24/7-27/7` stranded conductors, retracts for ordinary RJ45 access, and forms the IP65 normal-road connection when correctly mated to the selected TOP-compatible panel connector. Bare `NE8MX-B-TOP` would work but requires a separately selected compatible RJ45 plug.
- Selected budget moving-jumper prototype is the 3 m / 9.8 ft stretched ZBLZGP 26 AWG shielded PUR coil. A 6 ft maximum-stretch coil was rejected because the current geometry already totals about 56 in before drip-loop, tangent, and strain-relief reserve. Measure the prototype's actual OD before cutting, then continuity/shield/load/heat/dropout test before wall installation.
- Owner clarified the hard-mount mockup will be mostly leftover `1010` directly over the Yakima tracks, with continuous angle-aluminum or other stiff transverse members; a direct track-to-track member may omit longitudinal extrusion. That supersedes the prior `2 in`-vertical `1020` assumption: `M6 x 35 mm` is plausible for a bare `25.4 mm` `1010` through-stack and leaves about `2 mm` beyond a nominal washer/M6-nut stack, while `65 mm` is unnecessarily long. End-feed/stack test the `20 x 20 x 4 mm` square head before drilling. Yakima `8810074` Anchor Plate A plus field-selected `M6 x 1.0` bolts is the known-fit alternative. Keep main crossmembers continuous; flat bar laid flat is not the preferred wide-span beam.
- Owner now leans toward Yakima Anchor Plate A plus field-sized `M6 x 1.0` bolts for either extrusion or angle/flat feet. Because bolt tips can bottom on the finite track floor, prove one representative installed stack and select/trim bolts to finish flush or slightly shy of the plate underside with nearly full thread engagement; one or two measured shim washers are acceptable, but a large washer tower or false torque from a bottomed bolt is not.
- Reopened solar mounting around a no-full-rack baseline. Ranked paths are vendor-approved adhesive-backed CIGS directly on confirmed-compatible fiberglass/gelcoat, or removable low-profile panel cassettes on the existing Yakima tracks with a real `1/2-3/4 in` open airflow path. A honeycomb carrier bonded directly to the roof adds stiffness/thermal separation but not ventilation. Ordinary mono-flex direct-bond and a tall solar-only `1010`/large-angle rack are not lead paths. Branch scraping requires inboard panel placement, protected cable/junction exits, and rounded sacrificial track-line rub rails/front deflection; “walkable” does not mean branch-abrasion-proof.
- Router power lead is the Amazon EAZUSE `10-36V` to `57V 4.5A` converter on a dedicated fused branch. Use a `20A` branch fuse; use `12 AWG` only for about `6 ft` or less one-way and `10 AWG` for the more likely longer Desk route. Mount ventilated/noncombustible and reject for heat, reboot, or voltage instability.
- Updated the planning buy list/BOM to about `$454` required core before interior cable/roof attachment/DC branch and about `$579` with the purchased magnetic attachment and normal allowances before shipping/tax. Because the second Neutrik termination is already purchased, the remaining optional factory-cable-through-panel kit is about `$21` for the inline coupler and short shielded cable. Panel cut, coil termination, roof attachment, and loaded connector testing remain gated.

## 2026-08-05 — DC/AC branch progress; one-panel Starlink architecture selected

- Owner reports the pump, ICECO/fridge feed, and KUS sender circuit are wired; three separate `12 AWG / 15A` USB-PD branches are routed (`1x` Desk, `2x` Galley); and the Desk and Galley GFCIs are wired on separate breakers. Final fuse/slot labels, DC polarity/load tests, KUS configuration, AC LINE/LOAD/PE proof, and GFCI trip/reset remain open.
- Owner plans a few downstream receptacles. They remain field-count gated and must continue from the first GFCI's `LOAD` terminals with the same `12 AWG` branch conductors, accessible listed boxes, proper restraint, and whole-chain trip testing. The circular Desk outlet/USB/PD module stays a removable plug-in device on a fixed GFCI-protected receptacle; Starlink does not plug through that module.
- Selected the finished Starlink interface direction: one Neutrik `NE8FDX-P6-W` shielded Cat6A / PoE Type 4 panel bulkhead on the fixed body, one removable retractile roof jumper with a compatible rugged cable-side connector, and a long outdoor shielded Cat6A ground-deployment alternative. The complete OEM cable remains the direct recovery path.
- Initial mount lead was the TRIO Gen 3 Standard Speedmount across two movable extrusion crossbars. The `2026-08-06` purchase superseded the initial color/attachment lock with a white frame plus both magnet/disc and `75 mm` extrusion-through-bolt packages. It protects the terminal edges and preserves kickstand use, but the full framed dish is removed for tight brush because no roof mount is branch-proof.
- Solar is deliberately deferred. Do not drill a shared/oversize Starlink/PV gland or buy a PV coil/disconnect until the actual panels, stringing, cold `Voc`, `Isc`, conductor size, and roof route are known; future PV remains separate from Starlink.

## 2026-08-05 — Rear and passenger-hatch bug screens ordered

- Ordered one Yotache custom rear-entry magnetic screen in finished `60 in W x 46 in H`, black thickened mesh with middle magnetic opening. Owner-provided single-item order total is `$113.67`; item/tax split was not supplied. Expected arrival is `2026-08-24` through `2026-09-01`.
- Ordered one Risareyi black thickened reinforced-polyester magnetic screen in actual `24 in x 64 in` at an owner-provided single-item order total of `$28.95`; item/tax split was not supplied. Install it rotated `90 degrees` as `64 in W x 24 in H`, turning the center seam into a horizontal hatch opening. Expected arrival is `2026-08-27`.
- Combined recorded purchase total is `$142.62`. Rear nominal overlap is `2.25 in` per side and `1.75 in` at top with the bottom flush. The rotated passenger screen provides `3.25 in` nominal side overlap; after the estimated `1.5 in` bracket contour, about `1.75 in` per side remains for fixed hook-and-loop attachment. Receipt, adhesive compatibility, full hatch travel, gasket clearance, and installed fit remain acceptance gates.

## 2026-08-05 — Initial rear and passenger-side bug-screen geometry study (superseded)

- Owner-confirmed inside fixed-opening measurements are rear barn-door entry `55.5 in W x 44.25 in H` and passenger-side lift hatch `57.5 in W x 19.75 in H`. The initial target envelopes were rear `59.5 in W x 46.25 in H` and side `61.5 in W x 21.75 in H`, giving `2 in` overlap on both vertical sides and the top with the bottom flush.
- This initial two-custom-screen direction was superseded later on `2026-08-05` by the purchase record above: rear Yotache custom `60 in W x 46 in H`, plus a premade Risareyi `24 in x 64 in` screen rotated to `64 in W x 24 in H` for a horizontal passenger-hatch opening and additional strut-bracket contour allowance.

## 2026-08-03 — KUS routed, ICECO branch live, September walnut install scheduled

- Owner reports the KUS sender is installed and its two-wire lead is routed to the Cerbo area. Final mapping is one numbered Cerbo Tank column: sender black/signal to upper `DATA`, sender pink/return to lower `GND`. The owner's red extension maps to pink and therefore lands on `GND`. Use `1.0 mm²` ferrules with `>=10 mm` pins on the `18 AWG` extensions, or `10-11 mm` of untinned bare stranded copper if only short ferrules are available.
- The ICECO appliance lead is now switched and landed on the fuse panel with a `15A` fuse; the appliance pigtail is `16 AWG`. The switch's exposed positive terminals require individual insulation and temporary hard mounting before normal powered work, followed by polarity/switch/voltage-drop proof. Adhesive cable raceway along extrusion is accepted as abrasion/routing assistance but needs mechanical T-slot/P-clamp support at load points and intervals.
- The three black-walnut top pieces now have a mid-September `2026` final-install target. Full temporary tops are dropped; only a rough removable Galley sheet remains optional if needed for sink geometry or interim protection.
- Next shop sequence is ICECO contact protection -> KUS termination/configuration -> `14 AWG / 10A` switched SHURflo branch -> access-dependent AC/DC/control pulls -> individual battery and cooler road restraint. One ratchet strap over the three `48V` cases is rejected in favor of hard per-case capture plus individual low-stretch cam straps anchored to the hard-mounted extrusion/frame.
- The prior Scanstrut `DS-H-MULTI-BLK` recommendation is withdrawn for the proposed vertical sidewall geometry. A straight Scanstrut `TBH-4` through-bulkhead seal is a measurement-gated candidate, not a quick disconnect or current buy. Ground-deployed Starlink through the existing service route is the accepted first-trip fallback. The current rotary PV service-disconnect lead is IMO `SI32-PEL64R-2`; solar cable/connector/disconnect release still waits for final array cold `Voc`, `Isc`, stringing, and route dimensions.

## 2026-08-03 — KUS rebuild installed; pre-countertop wiring rough-in starts

- Owner reports the replacement KUS `FLS-U` under-ring, main gasket, and matched long hardware are installed and look correctly seated. This closes the failed-hardware replacement step, not the sender/full-system leak proof; keep the sender visible through the next fill/pressure/dwell test before countertop closure.
- Battery 2 resumed the prior charge and reached absorption. During the low-current absorption period the Progressive Industries portable EMS briefly stopped passing AC, displayed the tail of its automatic reconnect countdown, clicked back on, and the MultiPlus returned to absorption. The EMS now shows `E0` and retained no `PE#` previous error; treat this as a one-off incoming-power/local-connection interruption unless it recurs, and do not bypass the EMS.
- Before the Galley countertop, rough in two `120VAC` outlet branches (`12/3`, `20A` breaker each), the ICECO branch (`12 AWG duplex`, `15A`), SHURflo pump (`14 AWG duplex`, `10A`), both PD stations (`12 AWG duplex`, `15A` each), and KUS-to-Cerbo sender pair (`18-22 AWG` duplex, no external fuse). Useful access-now provisions are the LF Bros heater (`12 AWG`, `15A`, preserve controller cooldown power) and listed CO alarm (`18 AWG`, `3A`, always-on).
- Any pulled-but-unconnected branch remains de-energized: AC conductors individually capped inside a listed outlet box with the branch breaker off; DC conductors individually capped/labeled with the source fuse removed. Preserve service loops, abrasion protection, strain relief, and labels at both ends.

## 2026-08-03 — Integrated structure hard-mounted; restraint and Starlink route narrowed

- Overnight report covering the `2026-08-02` work: the electrical module, Galley/cooler support, water tank, and the returned Bench extrusion between the electrical and Galley modules are hard-mounted. Owner reports the integrated structure is extremely stiff. The tank is retained by two metal straps into the truck-bed-wall plusnut locations; KUS replacement hardware, fill/vent, sink termination, and dry wet-side acceptance remain open.
- Battery 1 remains complete at the corrected `20A`-cap / `56.8V` absorption / `54.0V` float profile. Battery 2 did not reach absorption/float before shutdown but was still progressing normally in upper-`54V` bulk; Battery 3 remains pending. Permanent parallel remains gated on all three rested terminal voltages being within `0.1V`.
- Remaining mobile restraint is now specific rather than a broad structural rebuild: frame low extrusion perimeter/divider capture around the `3x 48V` batteries and separate `12V` battery, use individual over-case straps to anchored extrusion/T-slot points, and add ICECO foot-level restraint plus a lateral hard stop/soft wall bumper. Do not use plywood wood screws as the only dynamic load path or over-tighten a ratchet strap across the cooler case.
- Next interior sequence is plywood Galley counter in final clamped position -> prove/cut/install sink and faucet -> pull Galley DC/AC/data wiring while access is open -> reinstall/build Desk and storage only after their hidden wire routes are in. Keep top-side KUS access and the tank/whole-Galley disassembly path available.
- Owner review rejected the exposed side energy-chain and guided loose-loop defaults: the chain return bend would project/bunch when the roof closes unless another trough/retractor were added, while a sleeved service loop has no mechanism to store slack. Current lead is two side-by-side removable retractile jumpers—shielded Ethernet/PoE for Standard 4 X and separately rated PV—with structural strain relief independent of the connectors. Preserve the complete OEM Starlink cable as an unmodified recovery spare; bench-test any Type-4/RJ45 adapter and coil under load. Remove igus `CF9-UL-60-04` from the lead moving-section list because it is straight four-conductor chain cable, not a retractile coil. Tight-trail mode powers down Starlink and opens a correctly rated two-pole PV load-break before both jumpers are removed and fixed ends capped. Exact geometry, solar cable, connector, and disconnect remain measurement/array gated; the cleaned current-source list is in `docs/plans/STARLINK_SOLAR_MOVING_UMBILICAL.md`.

## 2026-08-02 — Shore/water penetrations installed; Sunday camping-readiness sequence

- Owner reports the driver-rear shore inlet and cable route are installed. One accessible three-wire `L/N/PE` splice into the AC-input side remains before dead checks and controlled first use. First permanent-path test remains source-side EMS protected with the MultiPlus limited to `10A` on a normal household `15A` source; preserve PE continuity, AC-in/AC-out neutral isolation, enclosure, and strain relief.
- All three passenger-rear water pass-throughs are now physically installed: gravity fill, BLUE cold-out, and RED hot-return. This closes the exterior penetration work but not final water acceptance; KUS sender repair, fill/vent hose closeout, sink termination, and a final dry-compartment pressure/dwell inspection remain.
- Owner reports the Orion charges the `12V` buffer battery and the camper `12V` branch is operating correctly. The three `48V` batteries remain on individual charge/rest/record duty, followed by permanent parallel only if maximum-to-minimum rested terminal voltage is `<=0.1V`.
- MK3/VictronConnect inspection confirmed the MultiPlus charger profile still held the locked `56.8V` absorption / `54.0V` float targets. The isolated-battery charge-current cap was corrected from the full-bank `35A` value to `20A`; the source-side limit remains `10A` first test / `12A` household maximum.
- Battery 1 completed a clean supervised cycle at the corrected profile: about `56.76V` with `0A` in absorption, followed by about `54.06V` in float, with no observed BMS protection event. Battery 2 then began charging normally at about `53.75V` and `19A` with the source limit set to `12A`. SmartShunt SOC carried Battery 1's `100%` state across the physical swap and is not valid for Battery 2 until the next full-state synchronization.
- SmartShunt history preserved evidence from the earlier May test: `58.96V` maximum and `6` high-voltage alarms. Owner review of the event timestamps found alarms spaced roughly `10 minutes` apart with approximately `5-10 minute` clear/recovery intervals. This pattern is consistent with repeated internal-BMS overvoltage disconnect/recovery/recharge cycling, but the SmartShunt history alone does not prove the battery-side fault state without BMS logs.
- Sunday critical path is shore splice/dead checks/supervised proof -> sequential Battery 1/2/3 charging -> temporary removable Galley/Desk plywood templates plus real anti-rack/road restraint -> bug-screen measurement/materials -> measured roof-track/Starlink/service-loop design. The existing longitudinal roof tracks already provide outer rails; start with movable extrusion crossbars after identifying the track hardware rather than duplicating a full perimeter rack. No roof penetration or solar-specific support is released before Hiatus confirms the roof zone and an always-connected protected popup service loop survives repeated raise/lower cycles.

## 2026-08-01 — BLUE/RED ports operational; Orion isolation control clarified

- Owner reports both RAINPAL/HQMPC direct camper water pass-throughs are installed and working. The fittings project substantially, but the owner-designed clicked-on quick-disconnect travel caps fit and operate correctly. The BLUE cold source has an accessible ball valve; RED intentionally has no valve because the removable HOTTAP return hose is its disconnect and the fixed leg terminates only at faucet hot. The rear fiberglass was relieved for locknut access after the original `27 mm / 1-1/16 in` shank cuts; final backing/edge-seal/witness-mark and post-drive looseness checks remain.
- Owner reports the Orion is charging the `12V` buffer battery while the camper fan and lights operate from the shared fuse-panel junction. Existing multimeter reported an implausible `18V` while VictronConnect reported about `13.5V`; independent voltage verification is required before unattended charging.
- Clarified the installed isolation behavior: `SW-12V-BATT` opens only the buffer-battery positive branch and does not de-energize the shared fuse panel while Orion remains enabled. Normal sequence is loads off -> Orion disabled/status confirmed -> battery switch open; startup closes the battery switch before enabling Orion. Victron's approved remote method is a maintained dry-contact switch between the Orion `L-H` pins in place of the always-on jumper.

## 2026-08-01 — Modular 30A shore extension purchased

- Owner confirmed purchase of one Nilight `25 ft` `30A 125V` RV extension cord, `TT-30P` to `TT-30R`, `10/3` pure-copper STW, with a UL/ETL listing claim, for `$55.64` item subtotal; public product identifier is ASIN `B0DLKVHPTZ`.
- New BOM row `340` records the purchase. It extends the existing `25 ft` Camco TT-30P-to-L5-30R locking cord to `50 ft` only when needed; normal shore topology keeps the portable EMS source-side and requires the TT-30 midpoint to be fully seated, elevated/weather-protected, and the cords uncoiled under load.

## 2026-07-31 — Weekend integration sprint reset

- Owner reports the Standard 4 X kit is now in hand and an additional in-truck water leak/function pass has been completed without a new leak report. Final water acceptance still follows the replacement KUS mount, BLUE/RED bulkheads, fill/vent closeout, sink terminations, and one dry-compartment pressure/dwell test because those operations change the circuit.
- Immediate Friday dependency is pump-draining the tank and making one minimum low-speed on-property truck reposition before the MultiPlus/AC enclosure is remounted. The loose tank, Galley, batteries, and shop gear must be removed or positively restrained for that move; public-road travel remains held until integrated Galley/Bench/electrical road restraint is complete.
- Weekend critical path is stationary MultiPlus/AC remount -> protected Battery 1 / Orion / `12V` proof -> individual Battery 2/3 charge and `<=0.1V` rested matching -> KUS/rear-port/sink completion as delivered parts permit -> Galley/electrical road restraint. Starlink gets a bench test and measured fan/Starlink/solar roof-layout pass only; solar procurement, roof holes, and alternator first-charge remain held.
- Closed the previously vague MultiPlus grounding posture against the current official MultiPlus-II 120V manual: the external `M6 PE` lug is not optional in the mobile install and gets at least `4 mm²`, selected as `10 AWG` green stranded copper, to a verified truck-chassis bond point. The aluminum Hiatus shell gets a separate corrosion-compatible bond into the same equipment-ground network; it is not the sole PE path. No MultiPlus-case-to-DC-negative jumper or fixed downstream neutral-ground bond is added; the internal MultiPlus ground relay handles inverter/shore neutral bonding. Mechman isolated-vs-case-ground behavior remains a physical commissioning check because a case-grounded alternator may become the deliberate house-negative/chassis reference through its dedicated `2/0` return, and no parallel path may bypass the SmartShunt.

## 2026-07-28 — Water bench function pass and in-camper fitment gate

- Owner reports the tank, `12V` pump, accumulator, interior hot/cold PEX, and rear endpoints all operated correctly in the outside-camper bench setup. The received sink/faucet fittings can now be proved on a temporary plywood counter rather than waiting for the final black-walnut surface.
- The KUS sender remains the isolated water-system failure: the first `FLS-U` ring has a free-spinning/seized screw and the sender gasket leaks heavily. The empty leaking tank may be used as a geometry block, but water service and final restraint remain on hold until the failed screw head/ring are recovered without enlarging the `60 mm` opening, the replacement ring/main gasket/matched screws are installed, and a dry-area leak test passes.
- Near-term sequence is sender recovery -> temporary empty tank/plumbing-pack/Galley dry fit -> freeze and, only if physically proven, drill fill/vent and hot/cold penetrations -> temporary sink/faucet mockup -> structural Galley/electrical tie-in. The shore route may be mocked in parallel, but its exterior penetration waits until the MultiPlus/AC enclosure can sit in its final supported position and the complete inside/outside cable path is proven.
- Later owner update: the gravity-fill hatch penetration installed successfully. The BLUE/RED service holes still wait for the `27 mm` cutter plus the actual Joolca/HQMPC latch-flow fit, backed bulkhead geometry, and installed route; the Galley remains intentionally removable for KUS repair and rear-port access.
- Owner elected to pivot into stationary electrical work after completing errands: remount MultiPlus/AC, charge/rest Batteries 2 and 3 individually, prove Orion charging the `12V` buffer and then fan/lights/pump/fridge branches, and keep the truck immobilized until the Galley/Bench/electrical anti-rack tie is complete. Mechman/APM/WS500 rough-in is a stretch lane; alternator first-charge remains held.
- Owner confirmed purchase of Starlink Standard 4 X on `2026-07-28`; actual paid amount was not supplied, so BOM row `79` moved to `Purchased` with unknown cost rather than treating the prior `$349` planning estimate as purchase evidence. The inbound kit reopens a measured fan/Starlink/solar roof-layout pass, but no panel buy or roof penetration is cleared before the actual mount and cable/service geometry are proven.

## 2026-07-27 — KUS sender under-ring thread failure and leak-test hold

- Owner reports the new `60 mm / 2-3/8 in` sender opening is cut and the KUS SSS/SSL sender was assembled with the main gasket and `FLS-U` C-ring. While backing the long sender screws out to revisit screw-head sealing hardware, at least one stainless under-ring thread stripped or galled; one screw is now seized or free-spinning without axial movement or clamp load.
- An inverted water test pours through the sender gasket. The tank is on hold for installation/use; top-side location and atmospheric operation do not make a gross slosh leak acceptable.
- Owner purchased a second identical `FLS-U` under-ring on `2026-07-27` at the same owner-reported `$28.81` delivered amount. BOM row `221` now carries `2x` units / `$57.62` total; the second unit supplies the replacement ring and matched long screws. A fresh main gasket remains an inventory/buy-if-not-included check.
- Official KUS hardware evidence distinguishes the two screw sets: the separate gasket-mounting kit includes short screws with bonded metal/rubber sealing washers, while the `FLS-U` kit/manual uses its longer under-ring screws and does not depict transplanted loose rubber pieces. Repair default is to recover/remove the failed screw, rotate the damaged C-ring out through the existing opening, replace the ring/main gasket/all matched long screws, inspect the tank sealing land and sender flange, then hand-tighten in a star pattern and repeat the static wetting/inverted test. No oversize tap, thread insert, power-driver tightening, or RTV clamp substitute is accepted.

## 2026-07-27 — Owner BOM review and WS500 PH-VAN fuse correction

- Owner review moved active BOM rows `56`, `88`, `95`, `97`, `112`, `118`, `211`, `236`, `285`, `320`, and `331` to the inactive file as `Retired`; stable IDs and historical estimates remain intact. Camper audio rows `189-193`, the larger diesel tank row `65`, WLED/QuinLED row `98`, and chair row `100` remain active but `Deferred`. The Morimoto headlight package row `211` is inactive; the separate Diode Dynamics bumper-pod row `213` remains active pending an explicit owner decision.
- Owner confirmed the Mechman alternator, WS500 regulator, and APM-48 are already purchased. Technical review against the current Wakespeed manual and the owner-confirmed `PH-VAN` harness closes the former separate-sense-fuse ambiguity: one short red lead combines regulator power and positive voltage sense and uses one `15A` bank-voltage-rated fuse/holder in active row `171`; former separate `3A` row `320` is retired.
- Alternator commissioning still requires three unresolved protection/control checks: inventory or buy one `150A` MEGA fuse body-marked for the `48V` bank voltage class (`F-04`, row `170`), inventory or buy the one `15A` `PH-VAN` red-lead fuse/holder (`F-12/F-13-PHVAN`, row `171`), and verify the local `3A` Upfitter #3 enable fuse/wire/terminals (`F-15`, row `176`). The APM-48 is a parallel load-dump clamp and does not replace any of these conductor/control fuses.
- No additional `48V->12V` converter, second USB-C station, AC outlet-box/faceplate purchase, temporary plumbing pressure gauge, second sealing-tape roll, wall/cabinet insulation, thermal-break shim, anti-rattle foam, or Domino joiner remains in active procurement. Starlink remains required; current target stays non-actuated Standard / Standard 4 X class, with the direct-DC supply held model-dependent. The HOTTAP cold-feed leader remains active only until delivered-hose reach/fit proves whether a separate short leader is actually needed.
- Post-review control totals are `290` active rows / `$59,071.18` and `40` inactive rows / `$4,115.95`; the preserved combined evidence remains `330` rows / `$63,187.13`. Active unpurchased status is now `20` Planned rows totaling `$5,782.01` in known estimates plus `14` Deferred rows totaling `$2,461.00`; each status also contains one unknown-cost line.

## 2026-07-27 — Active/inactive BOM split for manual procurement review

- Split the stable-ID BOM into active `bom/bom_estimated_items.csv` and historical `bom/bom_inactive_items.csv`. All `25` existing `Retired` rows and `4` existing `Returned` rows moved to the inactive file without renumbering or changing their recorded evidence.
- The active BOM now contains `301` rows totaling `$60,902.18`; the inactive archive contains `29` rows with `$2,284.95` of preserved historical estimates, returned purchases, and retired stock. The combined evidence control remains `330` rows / `$63,187.13`, but inactive amounts are excluded from the active build total.
- No unresolved active line changed status in this pass. Manual owner review remains open for `30` `Planned` rows totaling `$7,753.01` plus `15` `Deferred` rows totaling `$2,321.00`; blank unknown costs remain outside those numeric subtotals.

## 2026-07-27 — Water and rear-service hardware order recap

- The follow-up Amazon CSV supplies exact purchase evidence for the `2026-07-26` water hardware: `$38.93` for the RAINPAL bulkhead two-pack, HQMPC brass QD two-set, and GHT cap four-pack; `$24.18` for the `27 mm / 1-1/16 in`, `1-1/2 in`, and `3-1/4 in` cutters; and `$10.48` for the PEX-B elbow and cinch-clamp packs. These eight lines total `$73.59`; their ASINs and item subtotals now replace the prior estimate/unknown values in BOM rows `231`, `336`, and `337`.
- The two BLUE/RED service ports each use the purchased `27 mm / 1-1/16 in` carbide cutter and require backed openings. The `1-1/2 in` cutter is for the selected gravity-fill tank-boss membrane field-fit, while the `3-1/4 in` cutter is for the camper-wall IZTOR gravity-fill hatch. Verify the membrane cutter clears the internal boss threads before drilling. The remaining procurement/stock checks are fill-hose clamps if not included with the purchased hose, compatible NPT sealant, local backing/support hardware, propane leak-detection solution, and the listed detection/extinguisher safety layer before first propane burn. The supplied `1 m` Joolca hose can commission the cold feed; a dedicated approximately `30 in` leader remains a post-fit convenience purchase.

## 2026-07-26 — Available brass panel-plug prototype selected

- Melnor `15409` was unavailable. The available HQMPC solid-brass two-set, ASIN `B07FHXLKH5`, supplies two female `3/4 in GHT` to male-QD adapters with visual geometry extremely close to the Melnor reference, plus two unused female-QD/male-GHT couplers. Exact Joolca latch dimensions are not documented, so this is a returnable fit/pressure/pull test rather than assumed compatibility; no camper hole is cleared by the listing alone.
- The unused female-QD couplers may be repurposed as clicked-on travel protectors by threading lightweight female-GHT caps onto their male-GHT tails. This is acceptable for dust/impact protection behind the closed interior ball valves, but it projects farther and weighs more than a final measured flexible nipple cap and is not the winterization pressure boundary.

## 2026-07-26 — Interior water system first pressure/function pass

- Owner reports the tank, SHURflo pump, SEAFLO accumulator, and most interior PEX are assembled and functional. The sink remains uninstalled; hot/cold runs currently end at accessible ball valves and final `90` fittings, while the rear bulkheads and several pass-through-area PEX fittings remain open.
- The first pump/accumulator/ball-valve test found no visible leaks, including a soap-solution inspection, but intentional discharge from the open ball valves soaked the area. Treat this as a successful function pass rather than final leak proof; repeat with the compartment dry, paper indicators at joints, all outlets closed, and no unexplained pump cycling.
- Reconfirmed the rear service topology after the prior connector churn: one separate gravity-fill hatch plus only two pressurized service ports—BLUE cold out and RED hot return. The installed manual ball valves make automatic panel shutoff unnecessary, and the exterior/heated path may remain recreational wash hardware. The lead panel stack remains `PEX-B -> installed valve -> UP120A5 -> RAINPAL SSBF020 -> permanently threaded male QD`; the later same-day HQMPC entry supersedes unavailable Melnor `15409` as the physical test part. Routine setup uses click connections only, not garden-thread assembly.

## 2026-07-26 — Rear-box propane setup purchased

- Owner confirmed a five-item purchase: Safoner black aluminum `3.5 in` RV cable pass-through hatch (`$26.99`), CALPOSE QCC1 propane pressure gauge (`$10.99`), AWW grey `23.6 x 15.5 in` foldable stone bath mat (`$29.99`), generic orange cylinder wall-bracket/`59 in` strap two-pack (`$17.99`), and Flame King `YSN10LB-ALM` `10 lb` aluminum cylinder (`$185.86`). Same-day live item listings reconcile exactly to the owner-provided `$271.82` subtotal; no separate tax or shipping amount was provided.
- BOM rows `332-334` capture the new hatch, bath mat, and bracket pack; rows `70-71` now reflect the purchased cylinder and gauge. The former `$80.00` restraint/vent allowance is split between purchased row `334` (`$17.99`) and a `$62.01` remaining planning allowance in row `256`, preventing duplicate bracket cost. The purchase reconciliation adds `$67.97`; the concurrently reconciled direct camper-port prototype removes `$65.84`, so the combined canonical BOM moves only `$2.13`, from `$63,122.34` to `$63,124.47`.
- Owner clarified the exact roles: the Safoner hatch is a neat propane-hose pass-through through the rear box, and the AWW mat is for outdoor showers. The earlier shore-power interpretation was incorrect.

## 2026-07-26 — HOTTAP camper-port design simplified before hardware purchase

- Owner correctly challenged the QD3 concept's delivered cost, non-potable positioning, `1/4 in NPT` to `3/4 in GHT` reducer, rear hose-barb transition, and removable-key complexity. No QD3 hardware had been purchased or camper hole cut, so the port layer was reopened without disturbing the purchased HOTTAP/bracket/cover or the direct exterior-mount decision.
- The interim lead prototype used the real Joolca hose directly: accessible valve and `1/2 in PEX-B` transition -> compact `304 stainless` `1/2 in FNPT` / `3/4 in MGHT` bulkhead -> physically verified metal male tap adapter. The direct design eliminates the QD3 male key, `1/4 in` reducer, rear `3/8 in` hose barb, short reinforced hose, and clamps; the completed connector evidence below establishes the final test order.
- The incoming HOTTAP controls the buy gate. Bring one female-ended hose and the included double-male coupler to the store; use Melnor plastic QuickConnect as a profile control, test stocked metal male plugs, and test the Melnor `4MQC` water-stop socket as the inexpensive self-sealing alternative. The supplied `1 m` red section is a no-purchase cold-feed trial only; the completed hose evidence below establishes the preferred final leader. Joolca's current manual explicitly classifies HOTTAP as recreational wash hardware, not drinking/sanitary-water supply, so the interior cold faucet remains the potable path.

### Completed connector and hose evidence reconciliation

- Joolca explicitly documents Melnor QuickConnect compatibility. Melnor `15409` therefore moves ahead of GARDENA `39004-G` as the first metal wall-plug test; the RAINPAL `SSBF020` bulkhead remains the first compact panel candidate, with QD3 only as premium fallback.
- HOTTAP Essentials supplies one `5 m` shower assembly split into `4 m` and `1 m` red female/female sections; the short piece is a shower extension, not a documented cold hose. Preserve the factory assembly and prefer a separate approximately `30 in` cold leader using a rated `F-GHT x M-GHT` hose with Melnor `9MQC` and `8MQC` female sockets after the delivered fit test. The `1 m` red section remains the no-purchase trial, and no factory hose is cut without manufacturer retermination guidance.

## 2026-07-26 — HOTTAP V2 core package purchased

- Owner confirmed purchase of one HOTTAP V2 Essentials (`$399.00`), one HOTTAP V2 Mount Cover (`$95.00`), and one Quick-Release HOTTAP Bracket (`$95.00`). Item subtotal was `$589.00`, shipping was free, estimated tax was `$44.49`, and checkout total was `$633.49`.
- BOM rows `72`, `255`, and `69` now carry the three item subtotals as purchased on `2026-07-26`; included hose/battery rows `232` and `237` are activated pending receipt verification. Consistent with the BOM contract, order-level tax remains excluded rather than being allocated across item rows.
- Procurement is closed for the HOTTAP core package, but installation is not cleared: inspect the shipment, verify bracket/cover compatibility, prove structural backing and road-load behavior, and validate manual operating clearances before drilling or first ignition.

## 2026-07-26 — Late parallel-audit findings reconciled after canonical BOM cleanup

- Reconciled three read-only audit lanes against the already-normalized BOM rather than blindly applying every suggested split. Identical packs and true kits remain grouped when procurement identity and lifecycle are shared; battery-bank members, the GFCI two-pack, cable inventory, tool kits, and other true packages were not over-split.
- Split genuinely divergent inventory and lifecycle lines into rows `323-331`: `125A`/candidate `40A`/quarantined `60A` MEGA stock, active versus retired fuse holders, AC-in/AC-out and branch-1/branch-2 breakers, February versus July lug packs, pump-side versus spare short hoses, and purchased versus conditional USB-C PD stations.
- Corrected the former fuse-holder batch by `$0.01` to its three direct source amounts. The canonical control is now `324` rows / `$63,110.57`; added `residual_allocation` for the evidence-limited `$40.65` remainder in the former mixed MEGA-fuse batch.
- Corrected deferred lifecycle state for PV cable, inset-panel foam, drawer slides, and future HOTTAP-included parts; recorded the mechanically installed but electrically disabled Mechman state.
- Repaired active-doc drift: Lynx tracked price and four-slot count, Orion Slot 4 `F-05` topology, retired standalone `F-06`, electrical-module restraint language, battery-bank commissioning gates, AC breaker row references, and fuse-inventory references.
- Completed a repository-wide row-reference pass for every split parent. Canonical/current documents now point to child rows where the original aggregate meaning changed; historical plans, decision records, and reconciliation tables retain their dated facts, with explicit current-row mapping notes where an unannotated old reference would be misleading.

## 2026-07-26 — HOTTAP camper ports corrected to compact no-spill QD3

- Owner rejected the Sea-Dog `513120-1` plus permanent Melnor `2MQC` wall stack: the plastic adapter was visually bulky/vulnerable, the Sea-Dog and male garden plug were straight-through, and using the Sea-Dog cap required screwing the adapter on/off every camp. A large protective hatch or RV spray-port fixture is explicitly out of scope.
- Replaced only the camper-port layer with two Koolance `QD3-FT10-P` female no-spill panel couplings and removable adapter keys. QD3 automatically obstructs both disconnected halves, leaving the existing BLUE/RED ball valves for service/winterization instead of routine setup. The exterior remains two small capped nubs; the direct-mount HOTTAP, supplied `1 m`/`4 m` hose modes, and no-arm/no-box-plate/no-splitter decisions remain unchanged.
- Prototype one key before duplicating: `QD3-MTN14` -> `1/4 in FNPT x 3/4 in MGHT` reducer -> Melnor brass `15409` fit-test adapter. If `15409` does not mate with the actual Joolca female socket, use verified-profile `2MQC` only on the removable key. No camper cut occurs before port projection, backed-panel/locknut access, hose fit, shutoff, hot flow, drainability, and simple stretch-cap fit are proven.

## 2026-07-26 — BOM normalized to component-level records

- Audited all `236` legacy BOM rows in separate formatting, lifecycle, duplication, and row-granularity passes. Replaced `77` free-form status strings with `8` controlled values; standardized categories, component wording, ISO purchase dates, and two-decimal costs; and moved lifecycle prefixes out of component names.
- Split `24` mixed rows into `80` appended component/service records with exact child prices where source evidence existed. The June/July Amazon fit-out order, TNUTZ order, plumbing package, hardware assortments, vehicle electronics, and tooling are now independently filterable. True retail kits and unallocated planning packages remain grouped and are named accordingly.
- Consolidated duplicate CA-glue and flooring-roller records. Removed `$6.09` of order-level tax and a stale `$46.97` duplicate roller estimate, changing the all-row cost control from `$63,163.64` to `$63,110.58` without dropping any supported component cost.
- Replaced ambiguous legacy fields with the canonical eight-column contract: `row`, `category`, `component`, `cost`, `cost_basis`, `purchase_date`, `purchase_status`, and `notes`. Added `bom/README.md` plus `scripts/validate-bom.py` to enforce the contract and public-data boundary.

## 2026-07-26 — HOTTAP direct exterior mount and universal hose ports locked

- Owner selected the Joolca HOTTAP V2, vehicle quick plate, and mounted cover. The heater now stays directly mounted on a structurally backed exterior face of the rear box, protected from dust in travel and outside the propane-cylinder compartment in operation. The articulating arm and box-side water plate are removed from active scope, recovering interior box storage.
- Verified the Joolca connection topology from official setup/support and current spare-part imagery: both supplied red hoses (`1 m` and `4 m`) have female quick-connect sockets at both ends; the shower handle/head disconnects from the long hose; and Joolca explicitly documents Melnor QuickConnect compatibility and existing-faucet connection. One hose can therefore serve the shower, camper hot return, or cold moto sprayer, one mode at a time.
- Replaced the doubled CPC HFC35 interface with one camper BLUE/RED plate based on two Sea-Dog `513120-1` 316-stainless straight-through washdown outlets (`1/2 in FIP x 3/4 in MGHT`) and two Melnor `2MQC` faucet adapters. The existing `UP120A5` PEX/MNPT adapters and two camper ball valves remain useful. The included `1 m` hose is the default BLUE-to-heater feed if reach passes; the included `4 m` hose connects heater-to-shower or heater-to-RED hot return. Bench compatibility, pressure, flow, hot wash, dust-cap/hatch, drain, and elevation tests remain pre-drill gates.

## 2026-07-25 — Post-reconciliation audit and source cleanup

- Closed the delayed read-only audit findings against the pushed Amazon reconciliation. Active `PROJECT`, `SYSTEMS`, `TRACKING`, interior-layout, and live-checklist guidance now treats propane-only Joolca HOTTAP V2 as selected; remaining work is physical rear-box cylinder/vent, arm/travel-latch, BLUE/RED service-plate, hose, road-protection, deployed-clearance, leak-test, and freeze-drain validation rather than heater selection.
- Converted remaining faucet/accumulator language from sourcing to receipt/inspection/test gates for the purchased EFIELD two-pack and YVSKM four-pack. Split KUS hole-saw procurement from the still-open tank-cut gate and added the Dr.Roc spare-hoist/lug-wrench fit-and-function test before travel reliance.
- Sanitized the tracked Amazon reference to `127` retained build/truck lines totaling `$9,067.07`: removed account-scoped order fields, normalized item links to public ASIN URLs, and omitted `11` personal/motorcycle/unrelated maintenance/cosmetic lines totaling `$199.61`. The owner explicitly retained the TFNUO magnetic gun mount as an F-350/travel accessory in BOM row `241`.
- Added a narrow public-repo rule: invoices, raw account-order pages, order IDs, account-scoped URLs, addresses, and payment data stay out; sanitized purchase facts remain allowed. Refreshed the active `2026-07-25` posture and regenerated `PROJECT.pdf` and `SYSTEMS.pdf` from their owning source docs.

## 2026-07-25 — Amazon web-extension order history reconciled

- Reconciled the owner-provided browser-extension Amazon order-history CSV: `121` line items / `131` units / `$8,644.52` captured item subtotal. The export has no May or June rows despite known purchases in those months, so it is an incomplete YTD capture; prior Gmail/CSV/screenshot records remain authoritative for missing periods. Private order IDs and URLs were excluded from the repo.
- Added four newly exposed July 24-25 purchases totaling `$88.91`: exact `2-3/8 in` / `60 mm` KUS sender hole saw (`$7.80`), EFIELD faucet-adapter two-pack (`$10.83`), YVSKM accumulator-swivel four-pack (`$11.99`), and Dr.Roc F-350 spare-hoist/lug-wrench extension kit (`$58.29`). BOM rows `233`, `239`, and `240` own those costs/inventory.
- Enriched earlier reconciled BOM rows with exact ASIN/title data for repeat 2/0 and 4 AWG lugs, July 12 flat-head hardware, 3M foam mounting tape, KUS sender, tank PEX/fill/vent fittings, flooring tools, RV wash brush, and visor mirror without duplicating costs.
- Updated plumbing owners for the purchased faucet and accumulator adapters. The YVSKM listing says no-lead, but markings, gasket/seat fit, potable documentation, and cold-pressure testing remain acceptance gates; Apollo remains fallback. The purchased hole saw does not clear the tank cut before the sender/port map and flat unobstructed geometry are proven.
- Closed active electric hot-water remnants: BOM/checklist/finish planning now reserve no electric appliance, dedicated branch, or interior heater cubby. Propane-only Joolca HOTTAP with exact CPC HFC35 NSF BLUE/RED water interface remains the selected path; generic water-QD and propane-QD placeholders are retired.
- Reconciliation detail: `bom/amazon_order_history_reconciliation_2026-07-25.md`.

## 2026-07-25 — Propane-only hot water finalized with rear-box package

- Owner closed alternate hot-water branches and selected propane as final. Selected appliance basis is Joolca HOTTAP V2 Essentials: outdoor recreational unit, about `37,500 BTU/hr`, `0.6-1.5 GPM`, recommended `40-60 PSI` / `1.6-3.17 GPM`, and explicitly supported by Joolca for camper-pump input and an existing kitchen faucet. The purchased SHURflo `4008`/SEAFLO pack matches on published values, subject to actual pressure/flow test.
- Permanent water topology is `accumulator -> one 1/2 in PEX tee`; branch to faucet cold, straight to BLUE valve/QD; RED QD/valve through insulated `1/2 in` PEX to faucet hot. The camper and box each receive a guarded BLUE/RED two-port plate. At camp, two short sleeved CPC jumpers connect the plates while the box-side heater hoses remain attached. A Joolca-compatible three-way hot splitter keeps both the shower hose and faucet-return branch connected, so no heater-side water fittings are swapped during routine setup.
- The doubled interface uses four straight-through CPC HFC35 NSF `86600` panel bodies, four `83100` hose inserts, four `HFC312L` dust plugs, two existing PEX ball valves, two existing `UP120A5` adapters, two `1/2 in FNPT x 1/2 in` barbs, reinforced hose, clamps, and faucet adapters. The HFC35 set is rated to `125 PSI` and `280°F`, replacing the earlier marginal `60 PSI` HFC12 concept.
- FORIOUS documentation confirms the purchased faucet's hot and cold hose connections are both `3/8 in`; use two lead-free `1/2 in PEX-B barb x 3/8 in OD compression male` adapters and no PTFE tape at the compression seats. The SEAFLO accumulator has two `1/2 in MNPT` ports, but its included white swivel fittings are flexible-hose barbs—not PEX-B fittings. Use the purchased RecPro `30 in` double-FIP hose on the pump side and one lead-free `1/2 in PEX-B barb x 1/2 in female-swivel` adapter on the accumulator outlet.
- Owner locked a Flame King `YSN10LB-ALM` `10 lb` aluminum QCC1 cylinder inside the ventilated bumper box. It is `9 x 9 x 19.25 in`, `9.6 lb` empty, and about `19.6 lb` filled; the reported `19.5 in` shelf leaves only `0.25 in` nominal height margin. The travel package uses rigid foot-ring capture and a rated body strap as primary restraint, with thin EPDM pads/rubber strap only for chafe and rattle, plus fixed low/high vents and clear valve/regulator access. LP remains disconnected in travel.
- Joolca publishes vehicle-mount guidance and an official swing-out-TV-bracket example. The HOTTAP therefore stays on a structurally backed articulating arm based inside the box, with an independent travel cradle/latch, and swings fully beyond the opening before ignition. Prove Joolca's `39 in` top, `23.6 in` rear, and `19.7 in` front/side clearances from the deployed heater faces. Do not burn it inside the open-front box; a fan is not a substitute for the outdoor-use/clearance requirements.

## 2026-07-25 — Rear-swingout propane hot-water alternative reopened

- Owner reopened a camp-deployed propane option using the existing rear bumper swingout box, with an exterior shower as the primary use and hot water returned to the interior faucet if the appliance/listing permits it.
- Hydraulically, a two-line parked-only umbilical works: post-accumulator cold branch to a color-keyed cold-out bulkhead, exterior heater, then either an outdoor shower or a separate hot-return bulkhead feeding the faucet hot trunk. A hot-faucet request starts the SHURflo pump and can trigger an on-demand heater above its minimum flow. `20 ft` of `1/2 in ID` return hose holds about `0.20 gal`, requiring roughly `12 sec` to purge at `1 GPM`.
- The current Flame King YSNAZ132 and official Camplux AY132 manual do not support the sink concept: both limit the portable class to temporary non-potable point-of-use use and prohibit permanent plumbing/multiple-outlet distribution. The defensible sink-plus-shower class is an RV-listed direct-vent unit: RecPro RP-1057 `42,000 BTU` activates around `0.67 GPM`; Girard GSWH-2 is `12V`, `42,000 BTU`, `12.5 x 12.5 x 15.5 in`, and requires about `0.80 GPM`.
- The bumper box cannot simply remain open around an operating burner. Either remove/hang a portable shower unit fully outside, or create a fixed, separately ventilated/direct-vent RV-heater bay with unobstructed exterior intake/exhaust and a physically separate upright/bottom-vented/impact-protected LP-cylinder locker. Connect water/12V only while parked; no pressurized water or LP hose crosses the moving swingout pivot in travel. Propane remains an analyzed alternative, not a selected purchase.

## 2026-07-25 — Ariston ARI POU-06 promoted as current side-port fit lead

- Checked Amazon `B0924JBLT2` against the official ARI POU manual rather than listing photos alone. Model is `ARI POU-06 120V 1500W`; manual confirms `13.8 in` jacket diameter, `15.8 in` shell height, `16.175 in` floor-to-top-water-connections, top and side `3/4 in NPT` hot/cold connections, side T&P location, and side drain.
- The heater must remain upright, but all active water plumbing can use the side ports. Under the owner's hard `17 in` vertical cap, the documented total leaves `0.825 in` theoretical margin with no top elbows. Top anode/electrical service will require extracting the heater, which matches the accepted uncommon-service posture.
- Promoted Ariston above the A.O. Smith lowboy as the current six-gallon lead because its complete side-port geometry is documented. If the earlier `27 x 15 in` horizontal envelope still applies, orient the opposing port sides along the `27 in` axis; the `13.8 in` shell leaves `13.2 in` total for side hardware but only `1.2 in` total on the narrow axis. The manual's minimum pan-diameter guidance is `15.8 in`, so a true `15 in` cross-section requires a wider pan pocket or an explicit custom-tray deviation. The initial purchase gate was a `13.8 in` diameter x `16.175 in` high cardboard mockup plus side-fitting/T&P/drain sweep, shallow tray/restraint thickness, hardwire entry, and extraction path; the owner result below closes the nominal-body portion but not the real lower-skirt/underside gate. Amazon price observed at `$283.87`; no order placed.

- Owner cardboard modeling passed the nominal body gate: a `13.8 in` cylinder fits very precisely through the actual `14 in` extrusion-base opening, leaving `0.1 in` nominal radial clearance. Raising the heater above the extrusion is not viable because clearance below the cooler falls to about `16 in`. Available product photos show a continuous black bottom skirt with no visible feet/nubs and no obvious projection beyond the jacket, but do not expose or dimension the underside; final purchase/install gate is the real empty unit's maximum bottom-skirt/underside OD.
- Pump/accumulator route moved into the owner-measured `6 in` gap between the cooler support and house batteries. The purchased SHURflo 4008 and SEAFLO accumulator are about `4.3 in` and `4.5 in` high on paper, leaving `1.7 in` and `1.5 in` before plate/hoses/service sweep. Preserve a thin vibration-isolated mounting plate, removable strainer bowl, nonconductive splash divider, and drained leak path away from battery terminals/cabling.
- Drain roles remain separate: the heater drain valve is for intentional draining/winterization; the T&P discharge is a required unvalved safety outlet; a shallow catch tray catches unintended tank/fitting/pump leaks. The practical camper tray can be thin sheet beneath the whole bay with its curb outside the `14 in` pass-through and its own gravity drain through the bed, rather than a tub wall inside the opening; this is an explicit deviation from the manual's residential `15.8 in` pan-diameter guidance.

## 2026-07-25 — Hot-water plumbing simplified to minimum-fitting parallel branch

- Owner rejected the previously proposed cold/hot manifolds, removable cassette, quick unions, permanent antifreeze pickup, and three-valve heater bypass as overengineered for the real truck-bed-camper space and accepted uncommon service by removing the cooler/panels/part of the 80/20 structure or cutting/capping PEX.
- New baseline keeps the existing `tank shutoff -> flex -> strainer -> SHURflo pump -> flex -> accumulator` pack, then uses one ordinary tee: straight to the cold trunk and branch through one cold-inlet isolation valve to the future storage heater. Heater hot runs in one insulated trunk; a hot-out isolation valve is optional. No bypass jumper or manifold rail is required for cold-water continuity because the heater is a parallel branch.
- Default hot-water control is normal heater temperature with local faucet/shower mixing. A central thermostatic valve is added only if the selected heater intentionally stores hotter water to stretch capacity. The heater's factory T&P relief/discharge and drain path remain required.

## 2026-07-24 — ThermoMate ES400B fit correction

- Corrected the exact Amazon `B0CCJ3PS9J` ThermoMate ES400B installed envelope from the previously conflated short-body ES400 dimensions to the live listing's `24.3H x 12.6W x 12.4D in`, including valve. It is a tall/narrow four-gallon option, not the short-cubby value fallback.
- Short four-gallon fallback order is now Camplux ME40B (`14.5H x 14.5W x 12.9D`) first on value, then Bosch ES4 (`13.75H x 13.75W x 13.5D`) only when its smaller shell makes the fit. A.O. Smith E6-6C15SV official shell height is corrected to `15.25 in`.

## 2026-07-24 — Orion input simplified to Lynx Slot 4

- Stopped refactoring the Orion input around Victron's conservative `20A` table value. Final practical architecture uses one `40A` MEGA fuse body-marked at least `58VDC` in Lynx Slot 4 feeding the existing `6 AWG` Orion input pair directly. Existing verified `58VDC` stock is acceptable under the locked `56.8V` charge ceiling; Victron `CIP138040020 40A/80V` is replacement fallback only. The `40A` fuse protects the feeder; `6 AWG` is electrically overkill but already installed and needs no replacement.
- Remove/bypass the separate Orion input inline fuse holder rather than stacking two fuses. The purchased `30A/58V` MIDI, FKS/ATO parts, and proposed `USM1/ATM20` DIN assembly remain unused/superseded. No additional Orion input fuse holder is required.
- This is an explicit practical deviation from Victron's `20A` external-protection table, chosen because `40A` remains safely below the installed `6 AWG` conductor ampacity and eliminates repeated connection/holder rebuilds. Orion `12V` output remains separately protected by `F-07 60A/80V` MEGA.

## 2026-07-24 — Orion 48V input conductor right-sized

- Corrected the prior fixation on preserving `6 AWG` at the Orion `48V` input. Victron's current table calls for `4 mm²` minimum at `1-2 m` on a `48V` connection; for the documented `~2.5 ft / 0.76 m` cabinet run, `10 AWG` (`5.26 mm²`) is the clean US-size default.
- Superseded by the final Lynx Slot 4 decision above. The existing `6 AWG` input pair is safe but electrically unnecessary; leave it in place as the lowest-rework path. If the pair is ever replaced for unrelated reasons, flexible fine-strand `10 AWG` is adequate for the documented short run.
- Keep `6 AWG` on the Orion `12V` output: that side carries `30A` continuous and Victron's table calls for `10 mm²` at `1 m`, making `6 AWG` a reasonable common-size choice. The final later decision above uses one `40A` Lynx input fuse rated at least `58VDC` and retains `60A/80V` on 12V output.

## 2026-07-24 — Orion F-06 direct-termination correction (superseded later same day)

- Revalidated the Orion-Tr Smart `48/12-30` against Victron's current manual: external battery protection remains `20A` on the `48V` side and `60A` on the `12V` side. This pass initially preserved installed `6 AWG` on both sides; the later right-sizing note above makes `10 AWG` the default if the 48V input pair is recut while retaining `6 AWG` on the 12V output.
- Corrected a procurement mistake: purchased Littelfuse `166.7000.5202` FKS/ATO fuses are electrically rated `20A/80VDC`, but purchased `178.6150.0001` parts are empty housings and their contacts cannot directly terminate the installed `6 AWG`.
- Rejected the proposed pigtail/reducer-splice workaround as needless connection stacking. Final low-rework architecture is one panel-mounted Mersen `USM1` touch-safe `10x38 mm` fuse holder (`30A`, `1000VDC`, pressure-plate terminals accepting `#14-6 AWG`) with one Mersen `ATM20` fuse (`20A`, `600VAC/DC`) on a short `35 mm` DIN-rail segment. Existing `6 AWG` lands directly in the holder; no pigtails, reducers, butt splices, or extra lugs.
- Lynx Slot 4 / legacy `40A` MEGA remains open/spare and is not in the Orion branch. Orion uses exactly one source-side F-06 input fuse. Do not energize an installed inline fuse/holder whose marked DC rating is below the bank maximum; the documented bank recommendation reaches `58.6V`.

## 2026-07-20 — Six-month Amazon Gmail reconciliation completed

- Ran an authorized Gmail read-only review for `2026-01-19` through `2026-07-19`: `42` Amazon order-confirmation messages found. All `23` confirmations through May 31 matched primary order identifiers already present in the canonical Amazon history CSV; `19` newer confirmations were reconciled against the BOM.
- Extracted `53` named line-item records representing `52` unique product classes from the newer confirmation HTML. Amazon initially suppressed four exact titles, but owner-provided order screenshots resolved them as 3M double-sided tape, repeat Sanuke 4 AWG/M10 and TKDMR 2/0 AWG/M8 lug sets, and a Sixzoo visor mirror. Row `228` is now a zero-dollar bridge to rows `35`, `37`, and `96`; row `229` now owns the mirror.
- Reconciled the final June 5 Amazon hardware/fit-out order as `38` units / `25` product classes, `$952.55` item subtotal and `$1,017.34` gross checkout across two suborders. The returned BLCCLOY 8-set T-shape kit is excluded from inventory; its `$21.44` refund leaves `$995.90` net checkout cost.
- Updated canonical BOM rows `35`, `37`, `46`, `49`, `50`, `52`, `96`, `99`, `208`, `212`, `219`, `220`, `228`, and `229`; added rows `222-229`. Major corrections include the purchased ARES WING monitor arm, repeat 10-series hardware/washer/lug stock, 3M mounting tape, Sarlai sink price, Banjo/Green Leaf plumbing-fitting prices, belt-service tool, 2 AWG splice kit, flooring tools, truck/RV cleaning tools, and the visor mirror.
- Added `bom/amazon_gmail_reconciliation_2026-07-20.md` and refreshed the TNUTZ hardware owner with the final purchase/return state. Private order identifiers, Gmail message IDs, addresses, and private order URLs were intentionally excluded from repository artifacts.

## 2026-07-19 — Electrical module hard-mounted; battery harnesses complete

### Owner-reported physical progress
- Electrical module is hard-mounted through the permanent Lonseal/plywood floor to truck-bed hardpoints. It fits cleanly and is stable enough for continued stationary installation; the planned Bench tie-in should materially increase stiffness and remains required before road travel.
- MultiPlus and combined AC breaker enclosure were removed before lifting to reduce module weight. The earlier embedded pronged/spiked T-nut choice proved successful: both heavy components can be remounted directly from the front without reaching loose nuts behind the electrical backer.
- All three `48V` batteries' positive and negative `2/0 AWG` branch cables were cut, lugged, adhesive-heat-shrunk, and landed at the battery-side busbars.
- Batteries are not yet paralleled. Battery 2 and Battery 3 still need individual charging through the MultiPlus; after rest, all three must be within `0.1V` before final parallel connection and `15.36 kWh` bank commissioning.
- The `12V` buffer-battery branch is close to completion. Locked routing remains `4 AWG battery + -> F-11 100A ANL -> SW-12V-BATT -> fuse-panel main +` and `4 AWG battery - -> fuse-panel main -` directly.

### Immediate electrical clarification
- Orion input uses exactly one standalone `F-06` on the `48V` positive lead: final Mersen `USM1` DIN-rail holder with `ATM20 20A/600VDC` midget fuse. Use `10 AWG` input conductors if recutting; existing clean `6 AWG` may remain as a no-rework choice. Purchased FKS/ATO fuse/housing stock in row `182` is a dead-end for this branch and is not part of the final install.
- Identify the physically X-marked/misrated Lynx fuse by slot rather than assuming it is for Orion: Slot 2 requires `F-03 60A/80V` MEGA for the MPPT; Slot 4 / `F-05` stays open. No `32V`-rated fuse remains on an energized `48V` branch.
- Orion `12V` output retains separate `F-07 60A/80V` MEGA protection before the `12V` panel main positive stud; the `12V` buffer battery retains separate `F-11 100A` ANL protection near its positive post.

### Next execution path
- Remount MultiPlus and AC enclosure; prove/cut/seal the L5-30 shore inlet and protected `10/3` path into the AC-in breaker.
- Charge/rest/match Batteries 2 and 3, parallel all three only at `<=0.1V`, then run final polarity/protection/SmartShunt/current-sharing checks.
- Finish Orion `F-06` and the `12V` battery branch, then commission the six factory pod lights, Maxxair fan, and first two DC charging outlets.
- After the owner's four-day vacation and expected fitting arrivals, assemble and bench/driveway test the tank, KUS sender, fill/vent/drain, pump, strainer, accumulator, and manifold before hard-mounting plumbing and Galley components.

## 2026-07-17 — Affordable north-cubby electric hot water comparison

- Owner rejected the expensive marine/hydronic path and standard exterior-vented RV propane packaging as too costly/complex for the actual Hiatus need, then identified a candidate north cubby with an unordered internal envelope of `27 x 15 x 16 in`.
- Current comparison result is conditional on which cubby dimension is vertical because the electric mini-tanks require upright installation: EcoSmart ECO MINI 6 (`~$215`, `20.83H x 13.86W x 14.19D`, `1440W`) is the best value if `27 in` is vertical; A.O. Smith E6-6C15SV lowboy (`~$319`, `15.25H x 14.25 in dia`, `1500W`, side/top connections) is the best six-gallon fit if `16 in` is vertical; Bosch ES4 (`4 gal`, `13.75 x 13.75 x 13.5 in`) is the fallback if only `15 in` is vertical.
- A six-gallon tank at `140°F`, tempered with `50°F` inlet to `105°F`, yields about `9.8 gal` ideal mixed output and uses about `1.32 kWh` for a full `50->140°F` heat cycle. Cheap electric tankless is rejected: `120V / 3.5kW` exceeds the existing branch/inverter continuous class yet adds only about `24°F` at `1.0 GPM`, and adequate `240V` units require a new shore/inverter architecture.
- Plumbing mockup moved the heater to the north service zone: split after pump/accumulator into a joint-free cold trunk south and a heater isolation/bypass; send one insulated hot trunk south to the middle sink and rear shower mixer. Heater selection remains on hold until cubby `height x width x depth`, front opening, service extraction, restraint, wet/electrical separation, T&P discharge, drain pan, tempering, and expansion path are physically proven.

## 2026-07-16 — Permanent Lonseal floor installed; systems-integration sequence reset

### Owner-reported physical state
- On the evening of `2026-07-15`, the one-piece Lonwood Madera Topseal sheet was glued to the three-piece `3/4 in` plywood subfloor with Lonseal #650.
- The sheet now bridges both plywood seams. The floor is intentionally permanent; removing the plywood as three sections would require cutting the vinyl along the seams.
- Owner reports mild waviness/bumps and some edge lift. Boards were placed over the perimeter and bolted down for cure pressure.
- #650 entered some hardpoint holes. Temporary bolts were driven into the installed stainless rivnuts to preserve the thread paths; those bolts need controlled removal/cleaning during cure so they do not become permanent.

### Cure and inspection gate
- #650 basis remains no foot traffic for `24 hr` and no heavy furniture/modules for `72 hr` after actual adhesive completion.
- Exact completion time was not captured; evening `2026-07-18` is only the earliest planning estimate for heavy-module reinstall.
- After cure: remove edge boards, photograph the full floor, inspect edges/hardpoints/raised or hollow areas, and distinguish stable cosmetic waviness from any localized loose-area repair.

### Next-sequence decision
- Do not reinstall every module at once.
- Hard-mount the electrical module first, then install/wire/fuse the `3x 48V` bank with the bench open; add the battery-bench bridge/lid only after extraction and emergency service access pass.
- Map the `36 gal` tank ports, KUS sender, gravity fill, highest-point vent, outlet, drain, restraint, and wet-spine components on the workbench. Perform one bare-tank in-truck dry fit before drilling; then add fittings, bench leak-test, and hard-mount tank/wet spine.
- Cut the shore inlet only after the installed electrical endpoint and inside AC-in route are proven. Cut the water-fill/vent opening only after the installed tank orientation, fill/vent geometry, hose fall/rise, backing, and service path are proven.

### Tank-port and plumbing-route clarification
- Owner confirms the `36 gal` tank presents four molded ports on each end, with two visibly large and two smaller ports per end, and no obvious/open top port. Exact model/thread sizes remain unconfirmed; inspect for a membrane-covered top boss before making a separate KUS sender opening.
- Provisional role map is upper large end port for gravity fill, highest suitable upper small end port for unrestricted vent/overflow, low north-end outlet toward the north pump bay, and a separate low tank drain. Final assignment remains dry-fit and measurement gated.
- Current route concept is tank/sink in the middle, pump/strainer/accumulator/manifold to the north, and heater/drain/service interfaces to the south. Fixed `1/2 in` PEX starts after pump flex; cold branches feed the middle sink and south heater/washdown, while a future hot return runs from south to the sink with an optional short south shower branch.
- Keep three outlets distinct: gravity fresh-tank drain, sink gray drain, and pump-pressurized ambient-water washdown. The sink pull-out can support a temporary out-window shower, but a south shower branch avoids carrying heated water north to the sink only to route it south/outside again.

### Tank-plumbing procurement and sender backing
- Owner purchased the final immediate tank transition hardware: SharkBite `UP120A5` five-pack of `1/2 in MNPT x 1/2 in PEX` straight adapters, Banjo `HB150-90` `1-1/2 in MNPT x 1-1/2 in barb` gravity-fill elbow, and Green Leaf `EL1238` `1/2 in MPT x 3/8 in barb` vent elbow. Later physical inspection corrected the accumulator assumption: its two supplied female-swivel fittings terminate in flexible-hose barbs, not PEX-B crimp barbs. Use the purchased RecPro double-FIP braided hose on the pump side and obtain one lead-free `1/2 in PEX-B barb x 1/2 in female-swivel` adapter for the accumulator outlet.
- Owner purchased the KUS/Wema `FLS-U` stainless SAE five-hole C-ring under-ring from eBay item `406787629362`: `$17.55` unit price and `$28.81` owner-reported delivered total.
- Sender cut guidance is corrected to the selected backing method: the official FLS-U manual requires one `60 mm` tank opening, which maps to a `2-3/8 in` hole saw. The earlier sender-alone `36-42 mm`/`1-1/2 in` opening guidance does **not** leave room to rotate the C-ring through the tank wall. Wait for the ring, preassemble the sender/gasket/screws/C-ring as shown, rotate the ring through that one opening, and tighten the screws into the under-ring; do not drill five separate pilot holes through the tank top. Bench leak-test afterward.

## 2026-07-13 — Lonseal template and rough-cut method locked

- Owner reported the one-piece Lonseal is ready for driveway layout and needs wheel-well plus four corner-pillar cuts.
- Active method: work in shade on a clean sacrificial surface; verify the `72 x 96 in` sheet covers the assembled floor; use the three fitted plywood panels as the primary face-down master; add registered local paper patches only where the plywood does not capture a pillar/wheel-well detail; rough-cut `1/2-1 in` large; then dry-fit and trim incrementally in the truck.
- Preserve front/rear/driver/passenger orientation and hardpoint centers, do not assume side-to-side symmetry, and do not cut rivnut holes until the sheet is in its final registered position.

## 2026-07-12 — Rivnuts installed; sleeve routing corrected by bed geometry

- Owner confirmed all planned stainless truck-bed rivnuts are installed. Locations span rib highs, valleys, and some rib-edge transitions.
- The on-hand sleeves are approximately `0.585 in OD x 7/16 in ID x 5/8 in long`. They are `1/8 in` shorter than the `3/4 in` plywood, so they are not universal through-plywood compression limiters.
- Active routing: no under-plywood sleeve on supported rib highs; use a sleeve beneath the plywood only at a valley/EPS location whose measured gap fits; relocate or retire angled rib-edge locations that cannot accept square bearing. A true through-plywood limiter, if later needed, must be custom-length for `3/4 in plywood + measured gap`.
- Added BOM row `217` for the purchased 50-pack and updated the live checklist, flooring procedure, project/system snapshots, build order, and tracking decision to the installed state.

## 2026-07-10 — Flooring plan corrected to owner-confirmed practical path

- Owner confirmed the live physical state: truck-bed hardpoint holes are drilled and primed; stainless rivnuts are on hand but **not yet installed**; one Gorilla tape roll is in use and a second is planned for the remaining sealing pass; final floor height cannot exceed the existing `3/4 in` plywood stack.
- Replaced the over-rigid prior guidance. The active path is: finish practical sealing, set/bolt-test/map the stainless rivnuts, settle EPS and the three `3/4 in` plywood panels until flat/quiet, dry-fit/install Lonseal with the registered hole-recovery plan, then reinstall modules and inspect after the first local drive.
- Removed the aluminum-insert substitution, rigid compression-sleeve, and `1/4 in` underlayment BOM candidates (`214-216`). Retained the useful checks: no clamp load through EPS, no blind recovery of covered hardpoints, flat/stable plywood before vinyl, and correct #650 adhesive handling/cure.
- Prior same-day entry below remains historical evidence of the audit pass but is superseded where it conflicts with this owner-confirmed decision.

## 2026-07-10 — Flooring foundation engineering correction and canonical cleanup

- Initial research pass: the floor/sealing/hardpoint plan was audited against platform and manufacturer references. Its prescriptive aluminum-hardware, seam-tape, compression-sleeve, and underlayment conclusions are superseded by the owner-confirmed practical plan above; reference PDFs are retained only as background research.
- The canonical flooring procedure, `PROJECT`, `SYSTEMS`, `TRACKING`, build order, live checklist, indexes, and BOM were updated again to reflect the owner-confirmed `3/4 in` height lock, practical bedliner-tape use, drilled/primed holes, and pending stainless-rivnut installation.
- Reconciled the active load-model pointer from stale v4 values to model v5 (`3,915 / 4,829 / 624 Wh/day`) in current core baselines; historical dated log entries remain unchanged.

## 2026-07-09 — Fresh-water tank level sender purchased

- Owner purchased the KUS USA SSS/SSL 14.5 in reed-switch diesel/fuel-water level sender for `$60.00`, Standard American Output `240-30Ω`, with mounting gasket and screws.
- Added BOM row `212` as the selected fresh-water tank level sender for the `36 gal` wheel-well tank. Current install assumption is Cerbo GX resistive tank input using US `240-30Ω`/`240-33Ω` setup; verify internal depth and flat top-port location before drilling.

## 2026-07-06 — Hardpoint method corrected before flooring teardown

- Owner clarified that hardpoint determination itself is likely at least a full day and should happen before modules are removed, while current module geometry is still live and fit-verified.
- Updated flooring/checklist guidance: active path is to locate floor tabs and hardpoints with modules installed, drill/register/test Plusnuts/rivnuts from inside the truck bed before Lonseal, preserve hole locations through vinyl with datum measurements/photos/marked tape/pre-punched dry-fit holes or temporary locator bolts, then remove modules for bed cleanup/floor work.
- Corrected EPS assumptions: EPS lives between bed-rib valleys only and does not need blanket removal. Trim proud/high EPS that rocks plywood; prefer hardpoints on rib/high supported areas, and if a hardpoint must pass through a valley/EPS zone, treat EPS as filler/pass-through only rather than a structural clamp-load member.
- Captured retention direction: do not structurally screw furniture into plywood; primary furniture retention should bolt through the Lonseal/plywood clearance-hole stack into Plusnuts/rivnuts seated in truck-bed metal. Use separate plywood-only anchors only where needed to flatten/control plywood seams or edges.

## 2026-07-06 — Flooring elevated to next gated sprint candidate

- Owner challenged the prior sequencing because all major modules are now in-truck, connected, and fitment-verified; any final electrical or plumbing done before flooring would likely be removed again when the modules come out for Lonseal and hard mounting.
- Updated the live checklist with a non-yes-man posture: flooring is now the likely next major sprint, but only as a gate. Before glue, module geometry must be documented, hardpoints mapped, service access preserved, future floor/pass-through needs reserved or explicitly ruled out, plywood leveled/prepped, and adhesive/tool/cure readiness confirmed.
- Revised follow-on order after a successful floor sprint: reinstall/hard-mount modules, then final-route alternator/shore/full battery electrical, then final-route plumbing once electrical and a temporary Galley counter/sink template make leak/function testing real.

## 2026-07-06 — Major module test-fit state updated

- Owner reported the Desk/storage module has been reinforced and mostly test-installed, with a few corrections identified before locking top/panel geometry.
- Owner also reported major Galley reinforcement, including redoing a rear/back stretch as one continuous `2010` member; Galley now feels very sturdy.
- All major modules are now test-fit/installed and generally look good, moving the build from rough skeleton assembly into correction, service-access, rough-in, panel, and commissioning gates.
- Updated the live checklist priority ladder: finish Desk/storage corrections first; then map/prototype functional service/anti-rack panels; then keep plumbing in discovery/mockup until electrical and countertop geometry make it testable; then shore/electrical closeout and controlled low-power testing. Alternator first-charge, full battery-bank install, Lonseal, final solar, permanent hot-water/propane, and exterior penetrations remain held until their prerequisites are physically proven.

## 2026-07-05 — Black walnut surface commission direction captured

- Owner discussed final interior wood surfaces with Nick and is leaning toward three commissioned black walnut pieces: a live-edge Galley countertop, a dimensional-lumber computer desk top, and a dimensional-lumber L-shaped Bench/lid top.
- Captured current Galley target as likely `~4 ft x 19 in` pending exact confirmation, `1.5 in` preferred thickness / `2 in` acceptable if the right slab requires it, with the last `~15 in` of the entry end using an inward-curving live edge if Nick can source a suitable slab.
- Updated finish posture: satin polyurethane or comparable durable clear film finish is the default for cooking/desk use after full cure; epoxy is best limited to void/check stabilization unless a deliberately plasticky full flood-coat look is chosen. All faces, undersides, holes, cutouts, end grain, and live edges need sealing.
- Added Bench/lid gas-strut gate: size struts only after the walnut lid weight, hinge line, opening angle, and mount points are known; use closed-state latch, anti-rattle bumpers, and mechanical open/overtravel control.

## 2026-07-04 — Desk cutlist assignments completed

- Owner reported the Galley/cooler/Bench/electrical tie-ins are complete enough that the interior now behaves as one large in-truck module; active build focus shifted to the Desk/workstation module.
- Renamed the active cutlist workbook to `docs/plans/assets/module-cutlists/2026-07-04_module-cutlist-and-assignments.xlsx` and tagged the remaining `24` unassigned pieces as `Desk`; `garage_final_cutlist` mirrors that module tag, and a dedicated `desk_shop_list` tab lists the Desk pieces and grouped source-row/length pools.
- Updated the live checklist with the Desk marking list, the completed Galley/Bench/electrical tie-in state, and the remaining hardpoint/service-access gates before flooring, final cabling, or road travel.

## 2026-07-03 — Interior wood quantity, species, and silver-extrusion correction captured

- Added rough board-foot estimate for PC desk, Galley counter, and rounded entry cap: finished `3/4 in` equivalent is roughly `10.8-12.6 BF`; rough `4/4` net basis is roughly `14.4-17.1 BF`; practical rough-lumber buy target is `20-24 BF` with waste/selection allowance.
- Corrected finish/design language: actual extrusion is silver, not black; hardware should stay consistent, reachable, and visually quiet rather than becoming a decorative feature across the camper.
- Added wood-species/scent posture: cedar/juniper is best as removable scent accents, cubby liners, shoe/closet panels, or vented strips; main wet/work tops should prioritize harder woods such as maple/birch butcher block, white oak/ash, acacia/rubberwood, walnut, or cherry depending on budget and sourcing.

## 2026-07-03 — Galley entry-cap cost-control posture added

- Marketplace wood rounds with roughly `15 in` radius / `30 in` diameter are likely to be priced as furniture/art pieces, not scrap.
- Updated the finish/features doc to avoid buying a full round for the Galley entry cap; preferred approach is a small hardwood/tabletop/butcher-block/stair-tread/cabinet-shop offcut shaped from a template, or a smooth hardwood radius that repeats the chosen wood tone.

## 2026-07-03 — Galley `45°` smoked-front / rounded wood-cap concept captured

- Added the tailgate/entry-end Galley signature feature concept: a `45°` smoked acrylic/polycarbonate cupboard face under a rounded hardwood/live-edge-inspired cap that blends into the main countertop.
- Build posture: acrylic/polycarbonate remains a non-structural door/panel; the wood cap must be carried by `80/20`/wood cleats, use positive travel retention, and be mocked with the one-barn-door entry path before final plastic or finished wood cuts.
- Marketplace posture: look for dry, stable hardwood/live-edge character as a small cap/nosing offcut, not a raw bark slab that catches water, dirt, clothing, or fingers.

## 2026-07-03 — Interior finish, paneling, storage, and feature choices synthesized

- Added `docs/implementation/INTERIOR_finish_paneling_and_feature_choices.md` as the draft owner for Galley/desk finish and creative-useful feature decisions: wood tops, plywood thickness posture, butcher-block/live-edge sourcing, smoked acrylic/polycarbonate accent panels, lift-out bins vs drawers vs elastic cubbies, `45°` Galley front cupboard, latches, anti-rattle, and validation gates.
- Updated the live checklist to convert those feature ideas into next shop actions: face mapping, `1/2 in` overlay-panel prototype, `3/4 in` top mockups, finish samples, smoked-panel sample, and cardboard `45°` cupboard mockup before final skins/countertops.
- Kept the governing gates unchanged: stabilize/tie Galley to Bench/cooler before finish work; keep service panels removable; defer final hot-water appliance geometry, Lonseal glue-down, and battery-trapped work until access is proven.

## 2026-07-03 — Galley extrusion frame cut and built

- Owner reported the Galley `10-series` extrusion frame is fully cut and built as an exoskeleton.
- Current physical state: frame is still tippy/unstable because it has only limited rear/one-leg support until tied into the Bench/cooler area; next structural gate is a removable Galley-to-Bench tie-in that does not bury battery or floor-bolt access.
- Active front-corner decision: protect camper entry clearance first. Default working direction is a physical sweep-tested `45°` chamfer rather than a square corner that clips entry or a fussy rounded corner.
- Galley utility-corner planning remains open: rear/service corner is a candidate for drain path, pump-fed cold spray nozzle/QD, capped future hot-water stubs, and a possible future listed/vented propane hot-water footprint. Do not commit permanent propane hot water until appliance listing, vent/cutout, clearances, LP routing, detectors, and winterization access are proven.

## 2026-06-27 — Electrical module shop-fit complete; integrated module build order updated

- Owner reported the electrical backer was trimmed to inset cleanly into the `80/20` electrical frame, with minor component shifts made after the real MultiPlus depth proved deeper than the earlier model. No core electrical architecture change was implied.
- Electrical module is now freestanding and ready to tie into the bench/desk structure, but it should not be driven loose/standalone because it remains too wobbly without bench/desk/galley tie-in, panels/anti-rack restraint, and final hardpoint verification.
- Updated active docs to shift near-term sequence from isolated electrical-module fabrication to integrated module buildout: bench/battery/step structure first, desk desktop/workstation support next, then galley/wet-spine counter/appliance module.
- Galley packaging now explicitly includes the purchased Sarlai sink, FORIOUS faucet, Duxtop induction cooktop, and Ninja SP151 air-fryer/toaster-oven cubby, with cutout/faucet/drain/heat/retention validation gates before final panels.

## 2026-06-26 — Portable cooktop, fan/light, and tire repair kit purchased

- Owner purchased three Amazon/retail items totaling `$160.28` in provided item prices: Duxtop `8100MC/BT-180G3` 1800W portable induction cooktop (`$60.34`), BougeRV 20000mAh rechargeable portable fan/light (`$49.99`), and GlueTread full-size 4x4 sidewall tire repair kit (`$49.95`).
- BOM row `67` now replaces the generic induction placeholder with the purchased Duxtop unit; rows `209-210` add the portable fan/light and sidewall tire repair kit. The load model still treats induction as a `1200W` average cooking cycle with `1800W` max available, sequenced against the Ninja SP151 and other high-draw AC loads.

## 2026-06-25 — Current module cut-list workbook filed

- Added the owner-built current best module assignment / garage cut-list workbook under a date-led filename. This artifact was later renamed to `docs/plans/assets/module-cutlists/2026-07-04_module-cutlist-and-assignments.xlsx` when the Desk assignment pass materially changed the current shop workbook.
- Naming convention going forward: use date-led generic cut-list filenames instead of temporary trigger words like faucet when the artifact is the current overall module/cut-list source.
- Follow-up cleanup normalized the assignment keywords in `piece_assignment`: module values now use `Electrical` / `Bench`, `Against` was renamed to `assign_orientation`, `garage_final_cutlist.module_info` mirrors assigned rows, and an `assignment_legend` tab records the controlled vocabulary and current E-cut caution.

## 2026-06-24 — EX-1010 profile interpretation corrected

- Owner confirmed the delivered `23x EX-1010` sticks are regular 4-slot pieces, not tri-slot / one-flat-side `1010-S` extrusion.
- Updated the TNUTZ hardware model note, BOM wording, and current cutlist-derived outputs to remove the stray `1010-S` assumption and normalize those pieces back to regular `1010`.

## 2026-06-24 — Galley sink and faucet purchased

- Owner purchased a FORIOUS black pull-out kitchen faucet with soap dispenser for `$47.99` and a Sarlai black drop-in/workstation sink for `$161.10`; raw order metadata was not copied into the repo.
- Sink dimensions logged: `15 in x 15 in` exterior topmount footprint with approx. `11 in x 13 in` interior basin.
- Added BOM rows `207-208`; generic cabinetry row `87` no longer carries sink/faucet as a catch-all. Current layout note: because the chosen sink is topmount, verify actual cutout, faucet under-counter clearance, drain/graywater path, and any local sink-zone rail/connector drop before final cuts.

## 2026-06-24 — Ninja SP151 microwave-replacement appliance order logged

- Owner ordered an Amazon appliance/tooling support bundle with grand total `$186.19`: Ninja SP151 8-in-1 flip-up air fryer/toaster oven (`1800W`) `$149.95`, GWYXC bamboo cutting-board/topper `$20.99`, GDMINLO 60 in flexible soft tape measure `$3.69`, Amazon Basics 15 in parchment paper `$5.47`, and `$6.09` tax/order remainder.
- BOM row `68` replaced the old compact-microwave placeholder with the purchased Ninja SP151 order group; item/order details were sanitized and no private order metadata was recorded.
- Load model updated to model the Ninja SP151 at `1800W` for short sequenced cooking cycles: `core_workday` now `3,915 Wh/day`, `winter_workday` now `4,829 Wh/day`, and `minimal_idle_day` remains `624 Wh/day`.

## 2026-06-12 — Gates 88.5 in Mechman belt test/spare ordered

- Owner ordered a Gates `K060885` Micro-V serpentine belt, 6-rib, approx. `88.46-88.5 in`, `$28.52`, arriving `2026-06-13`.
- BOM row `206` added as the longer Mechman dual-alternator accessory-belt test/spare; install validation remains pending against tensioner range, belt seating, and no squeal/walk.

## 2026-06-11 — Mechman staged-driving gate closed and WS500 rough-in clarified

- Owner confirmed the alternator noise was the Mechman-supplied idler pulley not being seated properly; after tightening/seating it, the noise went away.
- Mechman confirmed the truck can be driven with the `48V` alternator mechanically installed and unwired/electrically disabled.
- Updated the Mechman/WS500/APM-48 install guide to remove the stale staged-driving support gate and add an alternator-to-bed rough-in bundle map for high-current, WS500 alternator-leg, battery/shunt, temperature-sensor, and cab/control wiring.

## 2026-06-08 — 7.3L single-generator belt routing image saved

- Added the owner-confirmed `7.3L` single-generator belt-routing image to `media/references/mechman-ws500-apm48-install-guide/`.
- Updated the Mechman/WS500/APM-48 install guide with the routing orientation note: image label `A` is closest to the engine, and label `B` is furthest from the engine.

## 2026-06-07 — Mechman/WS500/APM-48 install guide added

- Added `docs/implementation/ELECTRICAL_Mechman_WS500_APM48_install_guide.md` as the detailed shop reference for the Mechman `48V` secondary alternator, Wakespeed `WS500`, Balmar `APM-48`, Ford Upfitter `#3` enable path, staged-install/drivability gates, first-run checks, and fault/shutdown handling.
- Reviewed current official Mechman, Wakespeed, and Balmar online/manual sources alongside local repo PDFs; retained unresolved gates at that time for exact alternator field/ground behavior, WS500 harness polarity, and final profile values. The staged-driving support-confirmation gate was later closed on `2026-06-11` after owner/Mechman confirmation.
- Corrected the active architecture/topology diagrams to show the APM-48 as a parallel surge/load-dump clamp at the alternator `B+`/`B-` or case point, not a series charge-current device.
- Updated repo navigation (`README.md`, `00 Home.md`, `docs/README.md`) and electrical cross-links so the install guide is discoverable from the canonical electrical docs.

## 2026-06-05 — Interior lighting design overwritten with deferred WLED plan

- Replaced the prior `24V`/MiBoxer interior lighting worksheet with a deferred desired `12V` QuinLED/WLED design on `12V-11`.
- Desired design: one QuinLED An-Penta-Deca analog PWM controller, upper CCT white-wash zone, lower RGBCCT night/entry zone, WLED presets, and hardwired momentary buttons for rear/entry, desk/bench, and bed control.
- Updated BOM row `98` and the load-model lighting labels from the old Govee placeholder to the deferred WLED/QuinLED package while preserving the current average-use Wh assumptions until final strip wattage is selected.
- Procurement/install status: intentionally deferred until after plumbing, Starlink, solar, alternator, and core furniture work; preserve rough-in opportunities but do not buy lighting hardware yet.

## 2026-06-03 — 80/20 panel spacer washers purchased

- Owner purchased a `25` pack of black rubber bushing spacer flat washers for 80/20 panel mounting: `3/4 in OD x 1/4 in ID x 1/4 in` thickness, `$10` total / `$0.40` each.
- Planning use: `1/4 in` standoffs/anti-rattle spacers behind `1/2 in` plywood inset/front panels on `10-series` 80/20, producing an effective `3/4 in` panel stack and a cleaner `1/4 in` visual reveal. Not for countertops, shelf load paths, or structural retention by itself.
- BOM row `50` updated from generic planned rubber washers to purchased 80/20 panel spacer washers.

## 2026-06-01 — Amazon order-history BOM reconciliation

- Reconciled `references/amazon_order_history.csv` against `bom/bom_estimated_items.csv` using quantity-extended item subtotals from the export; duplicate embedded CSV header row was ignored.
- Amazon CSV arithmetic: `138` item rows, `$9,266.68` quantity-extended item subtotal, `$9,067.07` mapped into the Hiatus/F-350 BOM, and `$199.61` excluded as personal/motorcycle/unrelated maintenance/cosmetic.
- Added sanitized audit trail at `bom/amazon_order_history_reconciliation_2026-06-01.md`; raw private order fields were not copied into the report.

## 2026-06-01 — MultiPlus profile verification blocker closed and board finish gate clarified

- Owner clarified that MultiPlus settings were redone and the first battery behaved as planned during shore charging: bulk began, then quickly transitioned to absorption because the battery was already at/near `100%`. No second-battery charge is required just to validate the charger profile.
- Remaining electrical board work is physical closeout: Cerbo is the only major item not hard-mounted; decide any route/sand/seal/paint step before J-clamp strain relief makes teardown more annoying.
- Documentation impact: removed stale "charger profile not verified" blockers while keeping AC-out/GFCI, alternator commissioning, Cerbo mounting, covers, labels, strain relief, and abrasion-control as open gates.

## 2026-06-01 — Mouser Orion F-06 final cleanup stock purchased

- Owner purchased Mouser Orion `F-06` final cleanup stock: `3x` Littelfuse `166.7000.5202` / Mouser `576-166.7000.5202` FKS/ATO fuses (`20A`, `80VDC`) and `3x` Littelfuse `178.6150.0001` / Mouser `576-178.6150.0001` holders (`80VDC` listing owner-confirmed).
- Cost basis: fuses `$7.88` each / `$23.64` extended; holders `$1.51` each / `$4.53` extended; order total `$38.79`, with `$10.62` shipping/tax/remainder over the `$28.17` parts subtotal.
- Historical allocation was later invalidated: `178.6150.0001` is housing-only and the FKS contact system cannot directly terminate the installed `6 AWG`. The FKS/ATO stock is not final Orion hardware; see the `2026-07-24` direct-termination correction at the top of this log.

## 2026-06-01 — Camper audio system selected and integrated

- Added a camper-only DC-first audio plan, separate from any future truck-cab driving subwoofer system.
- Selected draft package: Kicker `46KMC2` source unit, Kicker `CSC67` `4 ohm` speaker pair, and Kicker `49PTRTP10` powered down-firing 10 in subwoofer with `4 AWG`/`40A` sub branch.
- Added BOM rows `189-193`, deprecated the old row `101` sound-system placeholder, added implementation owner doc `docs/implementation/CAMPER_audio_system.md`, and synchronized electrical overview/fuse schedule, systems, interior placement notes, and tracking.
- Updated `bom/load_model_wh.csv` to model moderate camper-audio use: `core_workday` now `3,794 Wh/day`, `winter_workday` now `4,587 Wh/day`, and `minimal_idle_day` remains `624 Wh/day`.

## 2026-06-01 — Docs/plans closeout and route-map cleanup

- Consolidated TNUTZ/80-20 ownership: detailed WIP cart/visual aids now live in `docs/plans/TNUTZ_80_20_HARDWARE_MODEL_2026-06-01.md`; procurement list is the short summary; `HIATUS_work_plan_2026-05-29.md` is historical/reference only.
- Marked camper audio as preliminary/future-roadmap and changed audio BOM rows `189-193` to deferred/preliminary rather than near-term planned purchases.
- Downgraded the `24V` lighting worksheet to draft/unlikely and kept active lighting architecture on the existing `12V-11` branch until deliberately reopened.
- Corrected AC branch intent: Branch A = office/driver side; Branch B = galley/passenger side.
- Reconfirmed Orion input protection path: standalone `F-06`, current/interim `30A 58V` MIDI, and final cleanup stock now purchased per the Mouser entry above.
- Refreshed route maps/frontmatter and clarified historical install/starter plans so stale plan snippets do not read as current instructions.

## 2026-05-30 — Shore-charge profile settled at 56.8V absorption

- Owner confirmed active MultiPlus charge settings were programmed and shore charging entered bulk, then absorption as expected.
- Settled snapshot: MultiPlus `56.8V`, SmartShunt `56.8V`, charge current `0A` while in absorption, battery display about `55.8V`, and shore input current limit `12A` for the household-source test.
- Owner set SmartShunt SOC to `100%` at this settled full/near-full state. Current go-forward profile remains fixed LiFePO4 with absorption/charge `56.8V`, float `54.0V`, storage `52.8V` if shown, absorption `1h` because the UI allows `1-8h`, repeated absorption `0.25h`, equalization off, temperature compensation off, and `35A` charger current for the full `3x` bank.
- Note on instruments: prior cheap DMM readings were inconsistent/high versus MultiPlus/SmartShunt/battery-display behavior and should not be used as the top-end tuning authority until cross-checked.

## 2026-05-30 — Victron 60A/80V MEGA fuse replacement purchase

- Owner purchased Victron `60A/80V` MEGA fuse 5-pack for MPPT/Orion-output stock: Amazon ASIN `B0F9PKDGWD`, listing/part text `CIP138060020`, observed price `$46.75`.
- Earlier low-cost `60A` MEGA batch (`6x`, two 3-packs at `$4.99` each / `$9.98` total) was owner-confirmed as misadvertised/not actually `58V`; mark as trash/quarantined and do not use on `48V` paths.
- Allocation: install `1x` at MPPT battery-side Lynx Slot 2 / `F-03`; install `1x` at Orion `12V` output / `F-07` if that holder needs a `60A` MEGA; retain `3x` spares. Do not use for MultiPlus `F-02` (`125A`), alternator `F-04` (`150A`), or Orion `48V` input `F-06` (final `USM1/ATM20` path).

## 2026-05-30 — MultiPlus charge target lowered after top-end BMS trip theory
- Revised active MultiPlus-II commissioning profile for the Dumfume `3x 51.2V 100Ah` bank after live symptoms pointed toward top-end BMS charge protection.
- Key decision: use `56.8V` absorption/charge, `54.0V` float, `52.8V` storage if shown, `0.5h` max absorption, equalization off, temperature compensation off, and `35A` charger current only when all three batteries are paralleled. If testing one battery alone, cap charger current at `20A`.
- Rationale: the Dumfume manual lists `58.4V +/-0.2V` as a charge value but also lists `58.4V` as charge-limit/over-charge protection, leaving no practical voltage margin; the current target keeps the charger below the BMS protection ceiling rather than using the BMS as normal charge termination.
- Live follow-up: owner reported battery screen `53.3V` and `100%` while a cheap DMM showed `55.2V`; treat the battery display/SOC as low-confidence and use the highest credible terminal/bus reading for charger-safety decisions until cross-checked against SmartShunt/MultiPlus readings. VEConfigure UI noted absorption time range `1-8h` and repeated absorption time editable to `0.25h`; set charge curve `Fixed`, minimum absorption time, and repeated absorption `0.25h` for this commissioning profile.

## 2026-05-28 — MultiPlus default screenshot rollback values captured
- Added `docs/core/OPERATIONS.md` rollback reference for the visible MultiPlus-II factory/default values from owner screenshots, plus the active Hiatus programming target for the Dumfume `3x 51.2V 100Ah` bank.
- Key default values preserved for manual reconstruction include charger `57.60V` absorption, `55.20V` float, `8h` max absorption, inverter low-shutdown `37.2V`, `120V` output, PowerAssist `On`, and conditional AC input control `Off`.

## 2026-05-28 — Dumfume battery manual limits and MultiPlus programming baseline captured
- Owner provided live battery-manual values while programming the MultiPlus via MK3: `51.2V 100Ah`, recommended charge voltage `58.4V +/-0.2V`, charge-limit/over-charge protection voltage `58.4V`, recommended charge current `20A`, max continuous charge current `100A`, recommended discharge current `50A`, max continuous discharge current `200A`, over-discharge protection/recovery `36.8V`/`43.2V`, discharge overcurrent protection `600A`, short-circuit protection `1800A`, low-temp charge protection approx `41F-50F` with recovery at `50F`, and high-temp protection `157F`/`140F`.
- Current `3x` bank reference: `60A` recommended charge total and `300A` max continuous charge total; the MultiPlus-II `48/3000/35-50` `35A` charger limit is within that envelope.
- Updated BOM row `3`, `docs/core/SYSTEMS.md`, and `docs/core/ELECTRICAL_48V_ARCHITECTURE.md` so sustained shore charging can be programmed against manual-backed values instead of generic LiFePO4 assumptions.

## 2026-05-27 — Amazon comms/programming and prototype hardware purchase logged
- Owner purchased the immediate Amazon procurement wave; private order/payment/address details were intentionally not copied into public docs. Order subtotal basis for build tracking: `$171.17` before tax (`$183.57` total with estimated tax).
- Build-relevant electrical items purchased: Victron `MK3-USB-C` interface (`$59.44`), VE.Direct cable `5.90 ft` (`$16.31`), VE.Direct cable `2.95 ft` (`$16.13`), and one `3 ft` manufactured RJ45/Ethernet patch cable (`$5.99`).
- Plumbing/interior/support items purchased: `10 mm ID x 13 mm OD` food-grade silicone vent hose/clamp kit (`$10.99`), one Acegoo `118W` 12V USB-C/USB-A PD outlet (`$22.99`), countersunk cup magnets (`$12.34`), magnetic accessory mount (`$9.99`), and steel weld tabs/brackets (`$16.99`).
- BOM/procurement impact: rows `115`, `183`, `184`, `185`, and `186` updated; row `187` added for gravity-fill vent hose/clamps. MultiPlus sustained shore charging remains gated on programming/verification, not merely owning the MK3.

## 2026-05-27 — Repo freshness maintenance after first-live checkpoint
- Refreshed stale top-level and active-plan posture after the first live `48V`/MultiPlus/Cerbo/shore checkpoint.
- Updated procurement guidance to prioritize `MK3-USB`, Victron comms cables, board mounting/strain-relief hardware, Orion final `F-06` cleanup, and WS500 low-current fuse-holder validation.
- Downscoped the old broad `15-series` TNutz starter-stock posture: buy prototype stock only after real module envelopes and service access are proven.
- Marked old temp red-flag files as archived/reference surfaces rather than live trackers, and replaced stale generated `AGENTS.md` skill boilerplate with repo-specific maintenance guidance.

## 2026-05-27 — First 48V/MultiPlus/Cerbo/shore live checkpoint completed
- Owner confirmed `55.5V` throughout the `48V` system, including at the MultiPlus after pre-charge/energization.
- MultiPlus switch `I` brought inverter mode online: inverter light illuminated, slight hum observed, and no error lights reported.
- SmartShunt and Orion-Tr Smart both appeared in VictronConnect. Cerbo GX Wi-Fi access point/remote-console workflow came online; Cerbo power/comms path is `48V` small fused feed plus `VE.Bus` RJ45 to MultiPlus.
- AC Input 1 should be treated/labeled as `Shore power`; household-source test used reduced input-current limit (`10A` first test / `12A` max policy on `15A` outlet).
- Short shore-charge test showed about `1294W` shore input and about `54.3V x 21.6A` (`~1173W`) battery charge in bulk. Treat this as a functional test only until MultiPlus LiFePO4 charge settings are programmed/verified against the Dumfume manual.
- Shutdown practice captured: MultiPlus `O`, disable Orion if needed, de-energize/unplug shore, wait briefly, then open main `48V` disconnect. Residual voltage on Lynx/load side with disconnect open is expected capacitor bleed-down unless it remains stable/current-capable.
- Documentation updated: project/system snapshot, `48V` architecture, topology/fuse schedule, bench guide, AC BOM/checklist, operations quick cards, tracking risks/open questions, and this log.

## 2026-05-25 — Lynx Slot 4 left open; Orion input stays on F-06
- Locked active topology to leave Lynx Slot 4/`F-05` open/blank. Orion `48V` input now uses a Lynx `48V+` bus tap into standalone `F-06`, not an oversized Lynx MEGA fuse.
- Historical hardware path later superseded: `F-06` remains the single Orion input fuse, but the final direct-termination assembly is `USM1/ATM20`; neither the `30A/58V` MIDI nor purchased FKS/ATO housing stock is final hardware.
- Rebased battery-discharge sizing envelope from old `F-02 + F-05 = 165A` to `F-02 + F-06 = 155A` interim / `145A` final, while keeping the existing `2/0` and `200A Class T` posture conservative.

## 2026-05-24 — BOJACK 150A MIDI holder purpose resolved
- BOM/git history shows the BOJACK `150A` AMI/MIDI holder pack was originally purchased for the old Sterling `BB1248120` `12V` input-fuse path.
- Current status: obsolete/spare `12V` hardware only. It is not active Mechman/WS500 alternator protection, not Orion input protection, and not approved for any `48V` role without separate voltage/form-factor validation.
- Updated `bom/bom_estimated_items.csv` row `11` and `docs/core/TRACKING.md` so the part does not get mistaken for board-mounted active fuse hardware.

## 2026-05-24 — Orion input fuse interim/final decision locked
- Owner confirmed Mouser `576-178.6150.0001` holder listing says `80V`; final cleanup buy is Mouser `576-166.7000.5202` (`20A 80V` Littelfuse FKS/ATO fuse) plus Mouser `576-178.6150.0001` (`80V` Littelfuse ATO/FKS holder).
- Superseded by the `2026-07-24` direct-termination correction: do not treat the `30A/58V` MIDI as final or energize it above its marked rating.
- Final value remains `20A` because it matches the Victron Orion manual; final holder/fuse pair is Mersen `USM1/ATM20`.

## 2026-05-24 — Orion input fuse replacement downscoped
- Superseded by the `2026-07-24` direct-termination correction. The FKS/ATO idea failed on mechanical termination: its contacts do not accept the installed `6 AWG`, and the purchased holder item is only an empty housing.
- The final architecture uses the higher-rated Mersen `USM1/ATM20` family not because the system needs `600-1000V`, but because it provides the correct `20A` fuse value, adequate DC interrupt rating, touch-safe panel mounting, and direct pressure-plate termination of `6 AWG` without splice stacking.
- Existing `30A/58V` MIDI stock is not final Orion hardware and must not be energized beyond its marked rating.

## 2026-05-24 — Orion input fuse replacement found (superseded later same day)
- Historical first DIN-fuse concept was directionally sound but used a PV-specific fuse and a holder whose terminal fit was not locked to the installed `6 AWG`. Final direct-termination selection is Mersen `USM1` with non-PV `ATM20 20A/600VDC` fast-acting midget fuse.
- Existing `30A/58V` MIDI and row `182` FKS/ATO stock are retained only as purchased dead-end inventory, not active/final F-06 hardware.
- Wire validation remains: planned `6 AWG` Orion `48V` input and `12V` output conductors are conservative for the assumed short electrical-cabinet run.

## 2026-05-24 — Orion input fuse topology reassessment
- Reassessed the Orion `48V` input from scratch after owner noted the separate input fuse may be redundant beside the Lynx fuse.
- Updated active guidance: final topology should use one correctly rated source-side Orion input fuse, preferably Lynx Slot 4 alone if a Lynx-compatible fuse exists at the Orion-required value. Keep separate inline `F-06` only if Lynx cannot be populated with the correct value/rating.
- Follow-up correction: the existing `40A` Lynx stock is not final Orion device protection, and `40A` at Lynx plus `30A` inline should not be treated as the final answer.

## 2026-05-24 — Electrical fuse inventory loose ends
- Captured two active electrical loose ends from owner inventory review:
  - Orion `48V` input protection still targets `20A` per Victron guidance, but purchased `30A 58V MIDI` stock is not the default install value and owner has not found an obvious `48V+` `20A` practical replacement.
  - BOJACK/`150A` hardware purpose is unresolved; it is not assumed to be the active `F-04` alternator fuse, not a WS500 low-current fuse, and not approved for a `48V` role without voltage/form-factor validation.
- Updated `docs/core/TRACKING.md` and `bom/bom_estimated_items.csv` so these do not get lost during fuse-holder/SKU cleanup.

## 2026-05-17 — Pre-install audit triage and cleanup
- Owner triaged `docs/studies/PREINSTALL_FULL_REPO_AUDIT_LIVE_2026-05-16.md` findings F-001 through F-018.
- Closed May 7 travel/tailgate/tonneau logistics as historical; install happened and those items are not active blockers.
- AC baseline confirmed: one purchased `6-way` AC enclosure, two active GFCI outlets/covers, row `111` obsolete, pop-up multipurpose outlet deferred until details are provided, and cable-gland/strain-relief hardware treated as on-hand install-fit stock rather than a design blocker.
- Rechecked battery-branch math: `(125A + 40A) / 3 * 1.5 = 82.5A`; worksheet stale `77.5A` values were updated while PASS voltage-drop result remains materially unchanged.
- Owner confirmed storage placement is too hands-on for prescriptive docs, excess `2/0` cable is on hand for alternator use, a good roll of `14 AWG` duplex marine wire is on hand, and Class T inventory is `3` holders plus `4` slow-blow fuses total.
- Real follow-ups retained: AC dead-checks before energization, WS500 `48V` battery-sense fuse/holder voltage-class validation, final measured run lengths, and solar design deferred until shore and alternator charging are proven.

---
aliases:
  - Hiatus project log
tags:
  - hiatus/log
status: active
related:
  - "[[PROJECT]]"
  - "[[TRACKING]]"
---

# Project Log

Single running log for build progress and test evidence.

## Entry template
- Date:
- Work completed:
- Measurements/data:
- Tests run:
- Issues:
- Next actions:

## 2026-05-16
- AC purchase lock completed after owner purchased the Amazon AC cart. Active Phase 1 AC baseline is now portable `30A` EMS, Camco `TT-30P` to `L5-30R` shore cord, `L5-30` inlet, one combined `6-way` DIN enclosure, `30A` AC-in breaker, `30A` AC-out main breaker, two `20A` AC-out branch breakers, two `20A` GFCI receptacles, `10/3` feeder cable, and `12/3` branch cable.
- BOM updated: rows `13`, `14`, `15`, `41`, `107`, `108`, `109`, `110`, `113`, `114`, and `123` now record the purchased SKUs/prices/status; row `111` is marked obsolete; row `112` remains planned/confirm-on-hand for outlet boxes/covers; new rows `179-181` capture Sikaflex-221, butyl tape, and tire deflators.
- Docs updated: `docs/implementation/ELECTRICAL_AC_BOM.md`, `docs/implementation/ELECTRICAL_overview_diagram.md`, `docs/implementation/ELECTRICAL_bench_layout_and_test_guide.md`, `docs/core/SYSTEMS.md`, `docs/core/PROJECT.md`, `docs/core/TRACKING.md`, and `docs/plans/INSTALL_MINUS_12_READINESS_PLAN.md`.
- PDF exports regenerated for `ELECTRICAL_AC_BOM`, `ELECTRICAL_overview_diagram`, `SYSTEMS`, and `PROJECT`.
- Tests run: CSV parse of `bom/bom_estimated_items.csv`; targeted AC row verification; stale AC-language search excluding historical decision text and regenerated PDF assets; targeted PDF export/mermaid render.
- Issues: outlet boxes/covers are not confirmed in the purchase cart and remain row `112` planned/confirm-on-hand; verify delivered `10/3` jacket markings/listing and physical DIN neutral isolation before drilling/wiring.
- Next actions: receive/inspect parts, update row statuses to `Received`, label the single enclosure layout, and perform AC-in-only MultiPlus charge validation before AC-out branch energization.

## 2026-05-15
- Physical layout photo/mockup received: blue-tape floor envelopes show current installed-camper module layout; cardboard represents the driver-side electrical box and integrated step box; the battery bench area is taped near the bulkhead/front wall; the desk is around the wheel well at about `24 in x 48 in` and integrates with the electrical step box.
- Fridge clarification: fridge remains at the same raised height but should slide deeper into the passenger-side corner.
- Documentation update: added the photo-derived mockup facts as text only; the photo itself was not committed/published.
- Additional photos received: top-down/rear-entry views confirm the Iceco/fridge is being mocked on the passenger-side wheel-well water tank at raised height, pump/accumulator are staged low in the wet-side footprint, the driver-side cardboard electrical/step/desk mass is being checked with a tape measure, and the center aisle remains plausible but margin-sensitive.
- Issues: convert this into a measured block-envelope sketch before exact extrusion lengths; prior photo-read red flags are treated as resolved/non-issues except for keeping a standard wet-tray note in the plumbing plan.
- Next actions: measure datum-to-tape lines, battery extraction path, desk/wheel-well notch, step-box projection, fridge slide/lid/vent sweep, and pump-service opening.

## 2026-05-14
- Owner layout update: the Iceco/fridge is back on the passenger side, raised about `16 in` on an extrusion exoskeleton and slightly overlapping the `36 gal` wheel-well water tank envelope.
- Plumbing update: pump and accumulator move below the fridge in that exoskeleton, next to the water tank, as a separated service bay rather than hidden galley plumbing.
- Battery/bench update: batteries sit adjacent to the pump area in separated enclosures inside an approximately `30 in` tall bench, with a flat divider board above the batteries separating battery space from bench storage; a lid opens the bench and Hiatus bed cushions can cover it when the bed is stowed.
- Driver-side update: electrical panel/closet moves/extends on the driver side up to the `46 in` maximum interior build height, with a shelf/box extending toward the computer desk/camper entry for DC electronics and laptop plugs; diesel heater stays low in this driver-side utility zone.
- Diesel update: investigate an exterior truck-bed-wall diesel tank, ideally around `8 gal` and roughly `3 in x 17 in` envelope if available, with exterior fill/spill exposure, exterior pump, and protected fuel-line pass-through to the heater.
- Docs updated: active layout, systems, tracking, build-order, workstation, and diagram caveats now supersede the rear-left/driver-side fridge references.
- Next actions: physically mock the passenger-side fridge/wet-spine skeleton and battery bench before exact cut lengths; search for an external narrow diesel tank; keep wet/dry and electrical/fuel separation explicit in the service map.

## 2026-05-12
- Owner measurement correction: the water inlet gravity-fill vent nipple measures about `10 mm` OD on the main land and about `11 mm` OD at the largest barb/ridge.
- Planning/procurement impact: the previously ordered `1/2 in ID x 5/8 in OD` food-grade tube is oversized for this nipple. Correct replacement target is `10 mm ID` food-grade/potable tube, with `3/8 in ID` as the common inch fallback and `7/16 in ID` only as a looser clamp-required fallback.
- Docs updated: `docs/implementation/INTERIOR_furniture_layout_and_galley.md`, `docs/core/SYSTEMS.md`, `docs/core/TRACKING.md`, and `bom/bom_estimated_items.csv`.
- Next action: dry-fit replacement vent hose with clamp, check for kinks/vent restriction, then re-check after first fill/drive cycle.

## 2026-05-11
- Owner update: general interior layout is physically blocked in. Gravity fill passthrough, `36 gal` wheel-well water tank, cooler/fridge, likely butcher-block desk, pump/accumulator, PEX routing, `3x 48V` batteries, `1x 12V` battery, diesel heater, and diesel tank all appear to fit the expected zones.
- Owner update: subfloor is done; sheet vinyl/Lonseal will remain unglued for now to avoid damage and preserve rough-in/floor-access flexibility.
- Planning impact: broad `15-series` extrusion is further downscoped because the water tank bolts/restraints should use the truck-bed/camper structure directly if dry-fit validates the load path. Default extrusion posture is now `10-series`/light rail/plywood/direct mount unless a measured heavy/dynamic module proves `15-series` is needed.
- Electrical status: components are laid out on plywood but not connected, drilled, or energized. Next electrical action is labeled mechanical layout/backer-board templating, not final wiring.
- Diesel status: larger diesel tank is a want, not a blocker; carry-extra-fuel remains acceptable until the final tank/service envelope is validated.
- Next actions: finish electrical backer-board template pass, validate `10-series` prototype/module needs from taped block envelopes, keep vinyl glue-down gated, and bench-build/pressure-test wet-spine plumbing as a removable service cassette before final cabinetry.

## 2026-05-04
- Designed the driver/left-side workstation mechanism package for full-time work use while preserving pop-down roof clearance.
- Added `docs/implementation/INTERIOR_driver_side_workstation.md` as the draft implementation owner for the service-spine desk, stow-low/rising VESA monitor mechanism, Iceco/fridge tower storage, toe-kick false bottom, shallow cubbies, travel locks, cable drag-chain/service loops, heat/noise/venting, and acceptance tests.
- Updated `docs/core/SYSTEMS.md`, `docs/core/TRACKING.md`, and `docs/README.md` so the new workstation implementation is discoverable and tracked without treating stale CAD as final.
- Measurements/data: no new physical camper measurements; calculated reference envelope for a `27 in` 16:9 monitor as about `23.5 in W x 13.2 in H` and used `27-40 in` as a practical viewing-distance target range.
- Tests run: documentation cross-link and markdown consistency pass; no physical roof-cycle or travel test performed yet.
- Issues: final monitor mechanism, desk dimensions, Iceco slide need, latch hardware, and roof-safe line remain measurement-gated after camper install.
- Next actions: perform roof-down sweep map, Iceco lid/vent/cord envelope, seated work mockup, then bench-test the selected monitor mechanism before exact extrusion cuts.

- Added the office-first interior furniture and galley concept baseline.
- Added `docs/implementation/INTERIOR_furniture_layout_and_galley.md` as the draft owner for the top-left power stair battery bench, top-right soft storage/cabover landing bench, driver-side desk/rear-left Iceco utility block, passenger-side galley wet spine over the `36 gal` tank, rear service hatch, cold-first plumbing, and future hot-water readiness.
- Added generated concept diagrams under `media/diagrams/interior-furniture-2026-05-04/` and linked the preferred diagrams from the implementation docs.
- Updated `docs/core/PROJECT.md`, `docs/core/SYSTEMS.md`, `docs/core/TRACKING.md`, `docs/plans/PROJECT_build_order_of_operations.md`, `docs/plans/INSTALL_MINUS_12_READINESS_PLAN.md`, `docs/plans/STARTER_PLAN_electrical_and_flooring_pre_camper.md`, and `docs/README.md` so the furniture/galley concept is discoverable without treating generated art or stale fridge CAD as fabrication geometry.
- Measurements/data: no new physical camper measurements; preserved planning references that `36 gal` water is about `300 lb` before tank/brackets/plumbing and should be treated as `320+ lb` installed when full.
- Tests run: generated diagram review, documentation cross-link review, and git diff review; no physical roof-cycle, tank dry-fit, plumbing pressure test, or seated workday mockup performed yet.
- Issues: generated diagrams are concept aids only; galley/fill/vent/drain routing, hot-water choice, fridge envelope, monitor kinematics, and roof-safe line remain measurement-gated.
- Next actions: measure the installed camper, dry-fit the tank/fridge/electrical/desk blocks, validate the wet-spine service cassette, then lock only the extrusion and slide lengths proven by the mockup.

## 2026-05-01
- Owner correction: this is the Washington trip, not a washing trip. Bed will be emptied before departure; existing removable flooring will be removed before departure and does not need to be brought along.
- Tailgate removal is optional for access/drying, with wiring/camera protection if removed.
- Updated weekend order-of-operations and flooring implementation notes to keep flooring out of the wet/adhesive rail-seal work zone and wait for sealant cure/tack timing before reinstalling or handling surfaces.
- Owner update: purchased a `36 gal` wheel-well water tank instead of the prior tall/skinny vertical tank concept.
- Planning impact: the broad `15-series` extrusion exoskeleton/starter order is no longer justified by tank restraint alone; downscope extrusion to targeted module needs after physical dry fit, while verifying tank bracket/plusnut and any secondary restraint load path.

## 2026-04-25
- Status correction from owner: Mechman `48V` alternator has been purchased.
- Interpretation: dedicated `48V` secondary-alternator architecture remains the active baseline; remaining alternator blockers should be narrowed to received-kit fitment/content, support details, harness polarity, isolation/grounding behavior, load-dump mitigation, and commissioning validation rather than pre-purchase architecture selection.
- Updated `docs/core/PROJECT.md`, `docs/core/TRACKING.md`, and `docs/plans/STARTER_PLAN_electrical_and_flooring_pre_camper.md` to reflect purchase status while preserving Sterling return as gated on received-kit/fitment/support confirmation.
- Follow-up owner status: Mechman kit appears fit-compatible and has been received; Balmar `APM-48` has been received.
- Sequencing correction: defer alternator installation until the `3x 48V` battery bank exists and shore charging/monitoring is ready.
- Near-term priority: solve shore power because it is the intended initial charge path for the three house batteries.
- Added `docs/plans/INSTALL_MINUS_12_READINESS_PLAN.md` to focus the 12-day pre-Washington window on shore-charge readiness and extrusion/furniture-start procurement.

## 2026-03-20
- Consolidated the finalized `48V` architecture into one canonical file:
- Added `docs/core/ELECTRICAL_48V_ARCHITECTURE.md` to hold the locked house-bank, alternator, shutdown, and control-path decisions.
- Locked the manual alternator-control baseline:
- Ford `Upfitter Switch #3 -> F-15 3A inline fuse -> WS500 brown ignition/enable wire`
- `WS500` white `Feature-In` left reserved for future automatic interlock work.
- Updated implementation docs to carry the same control path and fuse:
- `docs/implementation/ELECTRICAL_overview_diagram.md`
- `docs/implementation/ELECTRICAL_fuse_schedule.md`
- Updated repo entry points and canonical references:
- `README.md`
- `docs/README.md`
- `docs/core/SYSTEMS.md`
- `docs/core/PROJECT.md`
- `docs/plans/STARTER_PLAN_electrical_and_flooring_pre_camper.md`
- Updated operations/tracking to reflect the new shutdown order and consolidation:
- `docs/core/OPERATIONS.md`
- `docs/core/TRACKING.md`
- Updated temporary/history docs so they no longer present the old Sterling path as current:
- `docs/temp/TEMP_electrical_red_flags.md`
- `docs/studies/ELECTRICAL_48V_dual_alternator_trade_study.md`
- Updated BOM for the finalized alternator-control baseline:
- corrected active cable-note references in rows `28` and `29`
- clarified row `168` kit assumptions
- clarified row `171` scope
- added row `176` for the `WS500` Upfitter `#3` enable wiring kit
- Regenerated the updated PDF exports:
- `docs/pdf_exports/ELECTRICAL_48V_ARCHITECTURE.pdf`
- `docs/pdf_exports/ELECTRICAL_overview_diagram.pdf`
- `docs/pdf_exports/ELECTRICAL_fuse_schedule.pdf`
- `docs/pdf_exports/SYSTEMS.pdf`
- `docs/pdf_exports/PROJECT.pdf`
- Measurements/data: no physical measurements added in this pass; `C-41` control-wire length remains an install-time measured value.
- Tests run: documentation consistency pass across core docs, implementation docs, and BOM row mapping.
- Issues: vendor confirmation gates remain open for exact Mechman kit content, `PH/NH` harness polarity, supported Dumfume battery behavior, and alternator isolation details.
- Next actions: confirm vendor gates, measure and record the final `C-41` upfitter-to-WS500 control-wire run, and close measured-length updates in the implementation docs during install layout.

## 2026-03-18
- Ran a full project-maintenance documentation pass and synchronized health/planning/tracking/procurement docs with current field progress.
- Captured completed vehicle electronics integration:
- Garmin Tread 2 hardwired and mounted (`$50` Garmin motorcycle mount/hardwire kit + `$20` RAM arm + `$75` BuiltRight dash mount; Garmin unit already owned).
- Captured flooring execution progress and stack revision:
- EPS cut and installed between truck bed ribs.
- Removed EPDM/RPDB thermal-break layer from active stack.
- Locked active floor path to bedliner -> EPS between ribs -> `3/4 in` birch subfloor -> marine sheet vinyl.
- Captured new material purchases:
- `2x` `4x8` `3/4 in` birch plywood (`$88` each, `$176` total).
- `1x` `4x8` `1/2 in` plywood (`$68`) for electrical backer/closet module.
- Captured major Harbor Freight tooling purchase and related additions (total noted from provided line items: `$1,622`):
- Tool cart, Apex/Badlands winch, Bauer 6-tool combo, orbital sander, router, jigsaw, jigsaw blades, extra `20V 5Ah` battery, router bit kit, sanding discs, kneeling pad, super glue pack, step bits, epoxy, `2-yr` HF membership, Ryobi `10 in` sliding miter saw, and lifetime table.
- Captured installer scope change:
- Added `$50` upcharge for installer-provided `12-circuit` Blue Sea fuse panel (instead of `6-circuit`), while retaining owner-purchased budget `12-circuit` panel for bench/prototype use.
- Captured electrical workflow change:
- Retired CAD-gated run-length expectation and moved to bench-layout-first measured cut-length process.
- Captured planning posture updates:
- AC protection chain baseline retained, but final branch utilization/receptacle count is reopened for closure.
- Solar procurement/final sizing intentionally deferred deeper in build; flexible path remains active direction under `75 lb` cap.
- Measurements/data: no new electrical performance testing in this pass (documentation and procurement-state synchronization only).
- Tests run: consistency pass across updated docs and BOM row checks for updated/new rows.
- Issues: AC scope finalization and measured run-length record location still open.
- Next actions: close AC count/SKU lock, complete measured run-length capture from bench layout, then execute cable closeout procurement.

## 2026-03-15
- Researched a possible alternator-charging architecture change from the current Sterling `BB1248120` path to a Mechman/Wakespeed `48V` secondary-alternator system for the `2021` `F-350` `7.3L`.
- Added the battery manual and exact battery data for the current house bank:
- `references/Dunfume_36V_48V_100Ah_Battery_-_User_Manual.pdf`
- Updated the battery row in `bom/bom_estimated_items.csv` to identify the Dumfume `51.2V 100Ah` battery and capture manual-backed charge/parallel specs.
- Added a new supporting study:
- `docs/studies/ELECTRICAL_48V_dual_alternator_trade_study.md`
- Added a cross-link from `docs/core/SYSTEMS.md` so the new study is discoverable from the canonical electrical doc map.
- Added new open questions in `docs/core/TRACKING.md` focused on:
- Wakespeed support status for the internal-BMS, non-CAN battery bank
- required load-dump / avalanche-diode mitigation for a direct `48V` alternator path
- whether the Mechman `48V` system can remain electrically isolated from chassis as desired
- whether the retained factory alternator continues to handle starter/vehicle charging independently if Sterling hardware is removed
- Key findings from this research pass:
- Mechman publishes a real `2020+` `7.3L` Godzilla dual-alternator bracket path that retains the factory alternator and adds a second alternator.
- The `48V` Mechman/Wakespeed architecture has real performance upside over the current Sterling `~1.5 kW` ceiling.
- The Dumfume manual materially improved battery-side clarity: `58.4V` charge voltage, `20-50A` recommended charge current per battery, and `1S4P` max expansion mean the current `1S3P` bank looks current-compatible with the Mechman output curve on paper.
- The main remaining uncertainty is not raw charge-current acceptance; it is battery support and protection strategy with an internal-BMS, non-CAN `48V` bank.
- User confirmed that losing automatic house-to-starting-battery support is acceptable, so that feature is no longer a decision blocker in the alternator trade study.
- Current recommendation remains to keep Sterling as the active baseline and not return that hardware until the Mechman/Wakespeed battery-support and protection questions are explicitly closed.
- Measurements/data: source review only; no bench or vehicle tests performed.
- Tests run: document/source verification only.
- Issues: official Wakespeed support status for the documented Dumfume battery is still unresolved.
- Next actions: send the updated targeted vendor questions captured in the trade study to Mechman, Wakespeed, and the battery manufacturer.

## 2026-02-16
- Updated procurement sequencing to an accelerated `Batch A+` phase so the electrical bench build can start without waiting for later cable/consumable waves.
- Updated `bom/bom_estimated_items.csv` purchase windows:
- `2026-02-16`: rows `3`, `12`, `18`, `20`, `22`, `23`
- `2026-02-17`: rows `4`, `5`, `6`, `7`, `10`, `11`, `16`, `17`, `26`, `27`
- `2026-02-18`: rows `52`, `53`, `60`
- `2026-02-19`: rows `28`, `29`, `30`, `31`, `32`, `33`
- `2026-02-20`: rows `34`, `35`, `36`, `37`, `38`, `39`, `40`, `41`
- `2026-02-21`: rows `42`, `43`, `44`, `45`
- Restored missing BOM row `122` as a placeholder interior procurement line item for drawer-slide kits so canonical row references remain coherent.
- Synchronized planning/governance docs:
- `docs/plans/PROJECT_build_order_of_operations.md` updated from `Batch A` to `Batch A+` and adjusted downstream batch scope.
- `docs/core/PROJECT.md` sequencing baseline updated to `2026-02-16` with active `Batch A+` note.
- `docs/core/TRACKING.md` updated with decisions `D-019` and `D-020`.
- Measurements/data: none captured (documentation/procurement-plan update only).
- Tests run: row-level verification of targeted BOM date updates (`37` checks, `0` mismatches).
- Issues: initial BOM write attempt was blocked by a temporary file lock; write succeeded after lock release.
- Next actions: convert planned purchase dates to actual ordered status with vendor + ETA per row and identify any SKU substitutions before harness fabrication.

## 2026-02-15
- Performed integrated safety deep-dive for the current architecture with focus on the `48V 10.24kWh` system plus `12V`, `120VAC`, and propane paths.
- Expanded `docs/core/SYSTEMS.md` `## Safety` from placeholder bullets to a build-ready baseline covering:
- system-wide controls and isolation/access principles
- `48V` high-fault-current hazard controls and commissioning checks
- `12V` distribution protections and Orion headroom safety trigger
- `120VAC` protection-chain and commissioning test requirements
- propane rear-mount/passthrough controls and indoor water-heater selection rule
- emergency shutdown order and pre-close safety hold points
- Updated governance in `docs/core/TRACKING.md`:
- Added decision `D-015` (consolidated safety baseline adoption)
- Added risks `R-007` (`48V` arc/thermal fault exposure), `R-008` (propane/CO exposure), and `R-009` (AC neutral-ground/GFCI protection risk)
- Added open questions to lock propane heater listing/venting path, passthrough hardware rules, leak-test cadence, and detector/extinguisher layout.
- Added operations-ready checklist content in `docs/core/OPERATIONS.md`:
- pre-energization checks
- propane-specific checks
- incident-response quick actions
- Measurements/data: none captured in this documentation pass.
- Tests run: none (documentation update only).
- Issues: final propane appliance path and venting method remain unresolved and now explicitly tracked.
- Next actions: convert safety hold points to dated commissioning test records during wiring and gas-system validation.

## 2026-02-13
- Ran PRF-003 research sweep focused on AC distribution right-sizing for the current truck-camper architecture.
- Reviewed current project AC assumptions in:
- `bom/bom_estimated_items.csv` (rows `13`, `14`, `15`, `67`, `68`)
- `bom/load_model_wh.csv` (owner-supplied office AC-path assumptions)
- `docs/implementation/ELECTRICAL_overview_diagram.md` (shore + inverter AC topology)
- Quantified modeled AC-related energy share at roughly `27.9%` (`core_workday`) to `30.7%` (`winter_workday`) for current assumptions.
- Updated `docs/temp/TEMP_procurement_red_flags.md` PRF-003 to:
- Separate "AC safety requirements" from "panel size/mounting method" assumptions.
- Add confirmed Phase 1 AC load list and right-sized architecture options.
- Document that DIN rail is optional pending final enclosure choice.
- Keep PRF-003 open until AC topology lock and SKU lock are complete.
- Expanded `docs/implementation/ELECTRICAL_overview_diagram.md` AC section from high-level path to full hierarchy:
- Shore-source path, MultiPlus transfer/charger behavior, AC-out branch strategy, optional AC-out-2 handling, and USB-C PD strategy.
- Added AC operating-behavior notes, protection-chain requirements, procurement gap checklist, and detailed AC conductor-segment entries (`C-28` through `C-35`).
- Added new tracking open questions in `docs/core/TRACKING.md` for shore-interface lock (`15A` vs `30A`) and USB charging path lock (DC USB-C PD vs AC USB receptacles).
- Locked Phase 1 AC/USB baseline for procurement:
- AC-out-1 split into two branches (`20A` galley + `15A` office) with `4` total `120V` receptacle locations (`2` galley, `2` office).
- USB charging baseline locked to `4` DC-fed USB-C PD points (`2` office + `2` galley) on dedicated `12V` branches.
- Updated `bom/bom_estimated_items.csv`:
- Refined rows `13`, `14`, `15`, and `17`.
- Added rows `107-118` for shore interface, AC enclosure/protection, receptacle hardware, AC wire scope, USB-C PD hardware, and optional 12V-converter expansion path.
- Set USB-C PD zone design intent to two `10A` fused `12V` branches (office + galley) to keep demand aligned with current Orion headroom assumptions.
- Updated `docs/implementation/ELECTRICAL_overview_diagram.md` and `docs/implementation/ELECTRICAL_fuse_schedule.md` to map AC branches and USB-C PD branch circuits to the locked baseline.
- Added decision `D-013` in `docs/core/TRACKING.md` and replaced prior AC architecture open questions with a SKU-lock follow-up item.

## 2026-02-12
- Built RF-003 decision support for power-distribution topology in `docs/core/SYSTEMS.md`:
- Compared `DIY discrete` vs `Lynx one-module` vs `Lynx two-module`.
- Listed required component groupings for each topology.
- Added planning-level cost deltas using current BOM rows plus explicit Lynx price assumptions.
- Added clear decision rule for whether `1` Lynx is sufficient or when `2` is justified.
- Updated `docs/temp/TEMP_electrical_red_flags.md` RF-003 references and status to `Open (decision-ready)`.
- Added high-level electrical architecture draft in `docs/implementation/ELECTRICAL_overview_diagram.md` using a topology-only Mermaid diagram.
- Linked the new diagram from `docs/core/SYSTEMS.md` and indexed it in `docs/README.md`.
- Kept this revision intentionally free of fuse/disconnect/wire-gauge details pending final topology lock.
- Performed full electrical-system sweep for fuse/holder/gauge consistency:
- Corrected Sterling `BB1248120` spec basis from `120A @ 48V` assumption to `~1500W` max output (`~26A` at `57.6V`) in `bom/bom_estimated_items.csv` and `docs/core/SYSTEMS.md`.
- Recalculated alternator charging replacement-time assumptions in `docs/core/SYSTEMS.md`.
- Replaced `docs/implementation/ELECTRICAL_overview_diagram.md` with implementation-level topology including all major components, fuse holders, and conductor schedule.
- Reworked `docs/implementation/ELECTRICAL_fuse_schedule.md` to include full fuse housing methods, branch gauge tie-ins, and sweep findings.
- Added decision `D-012` in `docs/core/TRACKING.md` and closed new red flag `RF-008` in `docs/temp/TEMP_electrical_red_flags.md`.

## 2026-02-11
- Workspace structure simplified and consolidated for lower documentation overhead.
- Canonical docs reduced to four core files in `docs/`.
- Imported and dissected `Camper Build.xlsx` into AI-friendly artifacts.
- Added normalized BOM exports:
- `bom/bom_estimated_items.csv`
- `bom/bom_misc_items.csv`
- `bom/load_model_wh.csv`
- `bom/bom_summary.json`
- Added CAD-friendly layout exports:
- `cad/drawings/layout_1_annotations.csv`
- `cad/drawings/layout_1_fills.csv`
- `cad/drawings/layout_2_annotations.csv`
- `cad/drawings/layout_2_fills.csv`
- Extracted workbook-embedded media:
- `media/inspiration/workbook_import/` (non-layout images)
- `cad/drawings/workbook_import/` (layout-sheet images)
- `media/inspiration/workbook_import/manifest.json` maps source sheet to extracted files.
- Updated canonical docs (`docs/core/PROJECT.md`, `docs/core/SYSTEMS.md`, `docs/core/OPERATIONS.md`, `docs/core/TRACKING.md`) and `bom/BOM.md` with workbook-derived content.
- Added maintained electrical capacity and charging reference to `docs/core/SYSTEMS.md` with:
- Scenario-based usage models aligned to remote-office goals.
- Battery autonomy math (`100%->0%` and `100%->20%` reserve floor).
- Solar, alternator, and shore charging potential tables.
- Formula block and update workflow for future recalculation.
- Updated `docs/core/TRACKING.md` with:
- Decision D-003 (canonical maintained electrical model).
- Risk R-004 (inverter overload risk from simultaneous high-draw AC loads).
- Performed full electrical model reset from BOM source of truth:
- Temporary battery interpretation was set to `2x 51.2V 400Ah LiFePO4` (later corrected same day).
- Replaced `bom/load_model_wh.csv` with BOM-derived model v2 (`core_workday`, `winter_workday`, `minimal_idle_day`).
- Recalculated `docs/core/SYSTEMS.md` capacity, autonomy, and charging potential from BOM-derived values.
- Added tracking updates:
- Decision D-004 (retire workbook WH model, BOM-only model).
- Risk R-005 (later revised after battery capacity correction).
- Corrected battery capacity interpretation after follow-up clarification:
- Installed bank is `2x 48V 100Ah` (not `2x 400Ah`).
- `400Ah` is treated as max 4-battery system capability, not installed capacity.
- Updated `bom/bom_estimated_items.csv` battery row and recalculated `docs/core/SYSTEMS.md` capacity/autonomy/shore-recharge numbers.
- Updated `docs/core/TRACKING.md` with Decision D-005 and revised Risk R-005 to reflect reduced no-charge autonomy.
- Reviewed electrical model for winter-fridge and solar-assumption accuracy:
- Updated `bom/load_model_wh.csv` winter fridge from `55%` to `40%` duty-cycle assumption.
- Recalculated winter conversion-loss row and total from `3,181 Wh/day` to `3,003 Wh/day`.
- Updated `docs/core/SYSTEMS.md` with:
- revised winter DoD/autonomy/charging replacement times,
- a dedicated `20%` minimum SOC reserve-floor framing for autonomy,
- and a `900W` flexible `3S3P` solar derate model (base `68%`, sensitivity `60%-75%`).
- Updated `docs/core/TRACKING.md` with Decision D-006 and follow-up validation action for measured fridge/solar logs.
- Resolved RF-001 policy mismatch for owner-supplied office electronics:
- Kept owner devices out of BOM procurement cost tracking.
- Added explicit owner-supplied load rows (laptop, 27 inch 1440p monitor, tablet/peripherals) to `bom/load_model_wh.csv` model v3.
- Recalculated `docs/core/SYSTEMS.md` load totals, autonomy, and charging replacement times against model v3.
- Updated `docs/core/TRACKING.md` with Decision D-007 and refreshed load/risk/open-question entries.
- Marked `docs/temp/TEMP_electrical_red_flags.md` RF-001 as closed pending measured validation.
- Swapped alternator charging architecture to Sterling:
- Updated `bom/bom_estimated_items.csv` row `18` to Sterling `BB1248120` (`$807`) and added row `26` for Sterling `BBR` remote (`$108`).
- Updated BOM rollups in `bom/BOM.md` and `bom/bom_summary.json` (current estimated total now `$45,879.64`; Power System subtotal `$5,041.00`).
- Reworked alternator charging math in `docs/core/SYSTEMS.md` for Sterling nameplate, `65%` remote-limited output, and a practical `240A` alternator planning cap.
- Added decision D-008 in `docs/core/TRACKING.md` and closed RF-002 in `docs/temp/TEMP_electrical_red_flags.md`.
- Added purchase-later vehicle charging upgrade path:
- Added JS high-output alternator (`$548`) and Big 3 wiring estimate (`$225`) to `bom/bom_estimated_items.csv`.
- Added Big 3 note to existing 2/0 cable row to indicate gauge compatibility and expected extra length when upgrade is activated.
- Updated BOM rollups (`bom/BOM.md`, `bom/bom_summary.json`) to total `$46,652.64` with `102` estimated line items.
- Updated planning docs (`docs/core/SYSTEMS.md`, `docs/core/PROJECT.md`, `docs/core/TRACKING.md`, `docs/temp/TEMP_electrical_red_flags.md`) with staged stock-alternator-first strategy and purchase-later fitment/spec lock actions.
- Swapped purchase-later alternator candidate from JS to Mechman 370A (SKU `11532370`) at `$599`.
- Re-synced BOM rollups after price/model swap (current CSV total `$46,703.64`; Power System subtotal `$5,640.00`; `102` estimated line items).
