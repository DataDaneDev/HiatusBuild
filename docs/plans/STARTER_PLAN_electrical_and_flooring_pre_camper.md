# Starter Plan: Electrical + Flooring (Pre-Camper)

As-of date: `2026-03-19`

Purpose: give a phone-friendly, practical plan you can execute immediately **without the camper shell in hand**, using current field progress and updated decisions.

Related references:
- `docs/implementation/ELECTRICAL_overview_diagram.md`
- `docs/implementation/ELECTRICAL_fuse_schedule.md`
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
- Flooring workstream is active: EPS between ribs is already cut/installed.
- Flooring materials now in hand include `2x` `3/4 in` birch sheets (subfloor) and `1x` `1/2 in` sheet (electrical backer/closet use).
- Tooling readiness increased (major Bauer/Harbor Freight purchase completed).

### Not finalized / not in hand yet
- Camper shell not yet installed.
- Solar panels and final PV wiring/fusing path are not yet locked for final procurement.
- Alternator architecture direction is now dedicated `48V` secondary alternator (`Mechman + WS500 + APM-48`) with Sterling return pending vendor confirmation.
- Final AC branch/receptacle count and final shore-hardware SKU lock remain open.
- Finish vinyl and adhesive are not yet purchased.

### Practical rule
- **Continue reversible and truck-only irreversible work now** (bench layout, board drilling, floor panel fit/seal, labeling, harness prep).
- **Do not do irreversible shell-dependent work yet** (final shell penetrations, final shell-run cable cuts, permanent finish-floor glue-down).

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
- Use existing uncut `2/0` stock for the alternator `+` and dedicated negative run until measured field routing proves otherwise.
- Do not initiate physical Sterling return shipment until Mechman fitment and kit-content details are confirmed.

---

## 4) Flooring: active pre-camper execution plan

The flooring workstream is now in active execution (EPS installed and subfloor plywood purchased).

## 4.1 Template package to create now
Create these full-size templates for the truck bed:
1. Bed perimeter outline.
2. Wheel-well profile captures.
3. Rib valley map (depth and width by rib segment).
4. Structural hardpoint map (where compressible layers must be removed).
5. Proposed plywood seam map.
6. Proposed insulation-piece numbering map.

Mark every template with:
- orientation arrow (`FRONT`, `TAILGATE`, `DRIVER`, `PASSENGER`)
- date/version (example: `FLOOR-TEMPLATE-v1`)

## 4.2 Hardpoint planning rule (critical)
Use hardpoint pocket zones from `docs/implementation/FLOORING_subfloor_build_process.md`:
- At structural anchor points, EPS is removed locally so plywood bears directly on steel.
- Keep these zones clearly marked to prevent accidental compressible stackups.

## 4.3 Plywood cut planning and fit checks (now)
With plywood now purchased, complete:
- Panel seam direction for easiest install/removal.
- Test-fit each panel for insertion/rotation clearance.
- A service pull path so a panel can be removed later if needed.

## 4.4 Active execution sequence
Execution order:
1. Transfer template lines to plywood and rough-cut oversized.
2. Test-fit and trim in small increments.
3. Pre-drill anchor holes to hardpoint map.
4. Remove and seal all faces/edges.
5. Refit and confirm hole alignment before finish flooring stage.

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
- Alternator path is re-baselined to dedicated `48V` secondary alternator; Sterling return is pending Mechman confirmation.
- Final AC outlet/branch count lock still pending (two branches retained as working baseline).
- Final closet envelope dimensions may shift after camper is physically in hand.

---

## 8) Suggested notes format (quick log template)

Use this in `logs/LOG.md` after each work session:

- **Date:**
- **Focus:** Electrical Board A / Board B / Flooring templates
- **What changed:**
- **What was verified:**
- **Blockers:**
- **Next action (single step):**

