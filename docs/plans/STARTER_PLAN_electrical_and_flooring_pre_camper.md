# Starter Plan: Electrical + Flooring (Pre-Camper)

As-of date: `2026-03-15`

Purpose: give a phone-friendly, practical plan you can start immediately **without the camper shell in hand**, based on your current inventory and open decisions.

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
- You can start by templating and bench-layout work now.

### Not finalized / not in hand yet
- Camper shell not yet installed.
- Solar panels and final PV wiring/fusing path not yet purchased/locked.
- Alternator charging path decision still in progress (`Sterling` retained for now while dual-alternator path is validated).
- Flooring plywood and final finish vinyl are not yet purchased.

### Practical rule
- **Do all reversible work now** (templates, layout boards, labeling, harness planning, drill guides, mock mounting).
- **Do not do irreversible shell-dependent work yet** (final penetrations, final cable cut lengths for shell runs, permanent flooring glue-down).

---

## 2) Fast-start checklist (phone view)

Use this as your “open phone and go” sequence.

## Week 1 goal
- Build full-size electrical closet templates on construction paper.
- Build a 2-panel mockup (`90°` plywood corner concept) out of cardboard/foam board first.
- Produce a first-pass floor template set for bed geometry and hardpoints.

## Week 2 goal
- Transfer electrical mockup to real plywood once purchased.
- Pre-drill and test-fit electrical hardware spacing.
- Pre-plan floor panel seams/cuts and hardpoint pockets.

## Week 3 goal
- Build labeled install kits and checklists so install day is mostly execution.

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

## 3.3 Convert to a cardboard prototype before plywood
- Use cheap cardboard or foam board to mock the two-board `90°` corner.
- Transfer hole centers from the paper templates.
- Dry-place actual components (or weight/size placeholders).
- Verify you can physically terminate the largest lugs and close the imagined cabinet envelope.

Exit criteria:
- Confirmed “human serviceable” geometry.

## 3.4 When plywood arrives: first irreversible step
- Transfer the validated template to plywood.
- Drill pilot holes only first.
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

## 3.6 Alternator path while still undecided
Until the alternator strategy is fully locked:
- Keep Sterling-based path as current working baseline.
- Reserve physical board/cable space for either:
  - staying Sterling-only, or
  - future dual-alternator controller/harness integration.
- Avoid permanently consuming all service space around the starter-battery charge-input branch.

---

## 4) Flooring: pre-camper start plan (template-first, no plywood yet)

You can get meaningful work done now with your construction paper templates.

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
Before plywood arrives, pre-decide hardpoint pocket zones from `docs/implementation/FLOORING_subfloor_build_process.md`:
- At structural anchor points, EPS/EPDM are removed locally so plywood bears directly on steel.
- Keep these zones clearly marked in templates to prevent accidental compressible stackups.

## 4.3 Plywood cut planning before purchase
Even without purchasing plywood yet, you can:
- Choose panel seam direction for easiest install/removal.
- Confirm each panel can be inserted/rotated into place without binding.
- Mark a “service pull path” if a panel might need removal later.

## 4.4 Once plywood is purchased
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

## Gate E1: Electrical layout freeze (before full plywood drilling)
- Paper + cardboard mockup approved.
- Terminal access verified for all high-current points.
- Fuse/service access verified.
- Future alternator-path reserve space confirmed.

## Gate F1: Floor template freeze (before plywood purchase/cutting)
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
- Alternator strategy still in validation; Sterling retained as baseline for now.
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

