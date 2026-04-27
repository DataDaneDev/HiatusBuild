# Starter Plan: Electrical + Flooring (Pre-Camper)

As-of date: `2026-04-27`

Purpose: give a phone-friendly, practical plan you can execute immediately **without the camper shell in hand**, using current field progress and updated decisions.

Related references:
- `docs/core/ELECTRICAL_48V_ARCHITECTURE.md`
- `docs/implementation/ELECTRICAL_overview_diagram.md`
- `docs/implementation/ELECTRICAL_fuse_schedule.md`
- `docs/implementation/ELECTRICAL_bench_layout_and_test_guide.md`
- `docs/studies/ELECTRICAL_48V_dual_alternator_trade_study.md`
- `docs/implementation/FLOORING_subfloor_build_process.md`
- `bom/bom_estimated_items.csv`

---

## 1) Current status lock (what to assume right now)

### Have now (working assumptions)
- Truck in hand: `2021 F-350 long bed`.
- Most core electrical components are already purchased.
- Electrical architecture remains `48V core + 12V distribution`.
- Garmin Tread 2 navigation is hardwired and mounted in-cab.
- Flooring workstream is active: EPS is installed and needs final trim cleanup; the `3/4 in` birch subfloor is installed in three slices with the top left untreated for Lonseal adhesive.
- Flooring materials now in hand include Lonseal sheet vinyl and adhesive; remaining immediate tool need is the exact-notch trowel (`row 174`) and roller confirmation (`row 175`).
- `1x` `1/2 in` plywood sheet remains the electrical backer/closet material, currently uncut with components laid out on/near it.
- Tooling readiness increased (major Bauer/Harbor Freight purchase completed).

### Not finalized / not in hand yet
- Camper shell not yet installed.
- Solar panels and final PV wiring/fusing path are not yet locked for final procurement.
- Alternator architecture direction is dedicated `48V` secondary alternator (`Mechman + WS500 + APM-48`); Mechman kit and APM-48 are received, but install remains deferred until batteries/shore charging/monitoring are proven.
- Final AC branch/receptacle count is secondary; the AC-in-only shore charge path must be SKU-locked first.
- Bed rail caps and old roughly `2 in x 3 in` rail holes need dust/weather sealing before the camper interface is finalized.

### Practical rule
- **Continue reversible and truck-only prep now** (bench layout, fuse/device matching, labels, rail-cap inspection/sealing, EPS trim, subfloor verification).
- **Do not do irreversible shell-dependent work yet** (final shell penetrations, final shell-run cable cuts, permanent finish-floor glue-down, final module skins).

---

## 2) Fast-start checklist (phone view)

Use this as your “open phone and go” sequence.

## Week 1 goal
- Lock electrical closet envelope and measured component layout on real backer material.
- Finalize floor panel seam map and hardpoint pocket map using installed EPS baseline.

## Week 2 goal
- Bench-build closet boards (pilot holes, test fit, staged full-size drilling).
- Start measured wire-route planning from physical layout (not CAD-derived cuts).

## Week 3 goal
- Build labeled install kits, AC decision pack, and shell-day execution checklists.

---

## 3) Electrical: pre-camper build plan (vertical closet on two plywood planes)

Garage execution note:
- Use `docs/implementation/ELECTRICAL_bench_layout_and_test_guide.md` as the step-by-step bench-build and staged-test checklist.

## 3.1 Lock the board concept before drilling
Target build concept (as you described): two plywood panels at `90°` in a vertical closet.

- **Board A (high-current / 48V power plane)**
  - Batteries, Class-T branch protection, main disconnect, Lynx, shunt, inverter/charger feed path.
- **Board B (controls / 12V / AC support plane)**
  - Orion, 12V fuse block + battery branch interface, monitoring/comms, AC input/output panel hardware locations.

Design rule:
- Keep heat-generating and high-current components spaced for airflow/service loops.
- Keep fuse and disconnect components reachable without removing major gear.

## 3.2 Construction-paper templating workflow (do this first)
1. Measure the available temporary workspace envelope for your closet mockup.
2. For each major component, make a paper cutout with:
   - exact footprint
   - mounting-hole locations
   - cable-entry sides
   - required bend radius zones
3. Tape cutouts onto paper representing Board A and Board B.
4. Check wrench access to terminals, fuse replacement access, and service loops.
5. Mark no-go zones for door swing, cabinet face frame, and future removable panels.
6. Take photos of each iteration and number them (`Layout A1`, `A2`, `B1`, etc.).

Exit criteria:
- One “build candidate” layout with no blocked terminals and no impossible cable bends.

## 3.3 Cardboard prototype (optional checkpoint)
- If any layout is still uncertain, use cardboard/foam board to mock the two-board `90°` corner before committing hole patterns.
- Transfer hole centers from templates.
- Dry-place actual components (or weight/size placeholders).
- Verify terminal access and service loops before full drilling.

Exit criteria:
- Confirmed "human serviceable" geometry.

## 3.4 Plywood execution (current phase)
- Transfer validated layout to plywood.
- Drill pilot holes first.
- Mount a subset (critical components) and confirm fit before drilling all holes full-size.
- Seal plywood faces/edges after hole layout is validated.

## 3.5 Wiring/harness preparation you can do now
You can pre-build a lot now without the camper:
- Print/label all fuse IDs from `docs/implementation/ELECTRICAL_fuse_schedule.md`.
- Build a wire label kit by circuit ID (`C-01`, etc.) and by endpoint.
- Pre-stage lugs/heatshrink by gauge bins (`2/0`, `2 AWG`, `4 AWG`, etc.).
- Build a termination checklist per branch (crimp, tug test, heatshrink, torque mark, continuity).

Do not finalize these yet:
- Final shell route-length cuts.
- Roof/solar run terminations.

## 3.6 Alternator path execution baseline (now locked)
- Build around the dedicated `48V` secondary alternator path (`A1` baseline) and retire Sterling-path layout dependencies.
- Keep Lynx Slot 3 reserved for the alternator branch (`F-04` now re-baselined in the fuse schedule).
- Reserve mounting space for WS500 harness fusing and APM-48 placement/service access.
- Reserve a small protected control-wire path from Ford `Upfitter #3` to the WS500 brown ignition/enable lead (`F-15` local inline fuse at the upfitter-to-WS500 handoff).
- Use existing uncut `2/0` stock for the alternator `+` and dedicated negative run until measured field routing proves otherwise.
- Do not initiate physical Sterling return shipment until Mechman fitment and kit-content details are confirmed.

---

## 4) Flooring + truck-bed sealing: active pre-camper execution plan

The flooring workstream is now beyond templating: EPS is installed, three plywood slices are installed, Lonseal and adhesive are in hand, and the next risk is crossing the glue-down point too early.

## 4.1 Bed rail dust/weather closeout
Before finish-floor glue-down if practical:
1. Remove or lift bed rail caps as needed.
2. Photograph and measure the old roughly `2 in x 3 in` camper-install holes.
3. Confirm with Hiatus that those holes are not needed for the new install.
4. Rust-protect bare cut edges.
5. Seal as dust/weather openings using low-profile serviceable patches and flexible automotive/weather-rated sealant or butyl.
6. Reinstall caps without trapping water or creating proud interference under the camper.

## 4.2 Hardpoint planning rule (critical)
Use hardpoint pocket zones from `docs/implementation/FLOORING_subfloor_build_process.md`:
- At structural anchor points, EPS is removed locally so plywood bears directly on steel.
- Keep these zones clearly marked to prevent accidental compressible stackups.

## 4.3 Current subfloor correction
Complete now:
- Trim EPS cleaner where needed.
- Confirm all three plywood slices sit flat.
- Confirm panel seam/removal strategy remains possible.
- Confirm the top face is clean, dry, untreated, and adhesive-compatible.

## 4.4 Lonseal glue-down gate
Do not glue until:
- rail/hole sealing is complete or deliberately deferred;
- no floor penetrations, hidden anchors, drains, heater routes, or hardpoints need under-floor access;
- exact trowel and roller are available;
- cure window is dry and within adhesive requirements;
- reduced serviceability from gluing over three plywood slices is accepted.

---

## 5) Day-of-work playbooks (short form)

## Electrical workday playbook (`2-4` hours)
1. Pick one board (`A` or `B`) only.
2. Complete one iteration of component paper layout.
3. Validate service access with your actual tools/hands.
4. Capture photos and update a one-line log entry.
5. Stop after one cleanly documented iteration.

## Flooring workday playbook (`2-4` hours)
1. Capture one geometry zone (front bulkhead, one side, one wheel well).
2. Transfer to template paper and verify symmetry assumptions.
3. Update hardpoint overlay.
4. Add one template revision tag and photo.

This keeps progress steady without waiting on missing materials.

---

## 6) Build gates (what must be true before moving on)

## Gate E1: Electrical layout freeze (before full board drilling)
- Paper + cardboard mockup approved.
- Terminal access verified for all high-current points.
- Fuse/service access verified.
- Future alternator-path reserve space confirmed.

## Gate F1: Floor layout freeze (before final drilling/sealing)
- Bed perimeter + wheel wells + hardpoint overlays verified in truck.
- Panel seam strategy verified for install/removal.
- Anchor-hole strategy marked.

## Gate E2/F2: Pre-install readiness (before camper arrival)
- Electrical boards at least dry-mounted and labeled.
- Floor panel patterns finalized and ready for cut/fit.
- Outstanding unknowns list reduced to shell-dependent items only.

---

## 7) Open items to keep visible on your phone

- Solar panel model/stringing not yet locked.
- Final PV fusing/wire lengths not yet locked.
- Alternator path is re-baselined to dedicated `48V` secondary alternator; Mechman alternator has been purchased, and Sterling return is pending received-kit/fitment/support confirmation.
- AC-in-only shore charge path SKU lock is the priority; final AC outlet/branch count remains secondary.
- Final closet envelope dimensions may shift after camper is physically in hand.
- Bed rail cap sealing, old rail-hole closure, tailgate removal/storage, and tonneau/weather timing need Hiatus confirmation.
- Fridge/water-tank dry fit invalidated current CAD location; front-left fridge/cooler envelope is now the working redesign candidate.
- Faucet is missing as a discrete plumbing purchase; hot-water decision should not block cold-water sink/pump/tank progress.

---

## 8) Suggested notes format (quick log template)

Use this in `logs/LOG.md` after each work session:

- **Date:**
- **Focus:** Electrical Board A / Board B / Flooring templates
- **What changed:**
- **What was verified:**
- **Blockers:**
- **Next action (single step):**

