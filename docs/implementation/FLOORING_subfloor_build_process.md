---
aliases:
  - Flooring subfloor build process
tags:
  - hiatus/implementation
  - hiatus/flooring
status: active
related:
  - "[[INSTALL_MINUS_12_READINESS_PLAN]]"
  - "[[STARTER_PLAN_electrical_and_flooring_pre_camper]]"
  - "[[PROJECT_build_order_of_operations]]"
---

# Flooring Subfloor Build Process

## Scope
- Define the locked floor stack-up, hardpoint strategy, procurement state, and install workflow for the truck bed floor.
- Baseline date for this revision: April 27, 2026.

## Final Subfloor Structure (Bottom to Top)
1. Existing spray-in bedliner.
2. `5/8 in` SilveRboard Graphite EPS between ribs only. Current state: installed, with some trim cleanup still required.
3. `3/4 in` birch plywood directly over EPS + rib structure. Current state: installed in three slices; bottom/edges are sealed and the top bond face remains untreated for Lonseal adhesive.
4. Lonseal Lonwood Madera marine sheet vinyl, glue-down finish layer. Current state: sheet vinyl and adhesive are in hand; glue-down is gated because it reduces subfloor serviceability.

## Explicitly De-Scoped Layer
- Full-bed `EPDM/RPDB` thermal-break sheet above EPS and below plywood is no longer in the active floor stack-up.
- EPDM order was canceled before shipment and refunded; no EPDM material is on hand for this build.

## Hardpoint Rule (Structural Anchors)
- At structural hardpoints, remove EPS locally so plywood bears directly on steel.
- Use mechanical fasteners into rivnuts at these pockets.
- Do not place compressible insulation in bolt clamp stacks.

## Procurement Snapshot (Updated)
### Purchased / in hand (active flooring path)
- SilveRboard Graphite EPS kit (`$71.38`) - Home Depot.
- Loctite PL 300 foamboard adhesive (`$5.48`) - Home Depot.
- TotalBoat Halcyon Water-Based Marine Varnish, clear gloss, pint (`$22.99`) - Amazon.
- `3/4 in` birch plywood, `4x8`, qty `2` (`$88` each, `$176` total).
- Lonseal Lonwood Madera Topseal marine sheet vinyl.
- Lonseal adhesive.

### Canceled / refunded (not in hand)
- Rubber-Cal EPDM closed-cell sponge rubber, qty `2` (`$47.22`) - Home Depot order canceled before shipment; refunded.

### Related purchase (not floor stack, but same workstream)
- `1/2 in` plywood, `4x8`, qty `1` (`$68`) for electrical backer/closet module.

### Not Yet Purchased / confirm before glue-down
- Exact-notch sheet-vinyl adhesive trowel (`1/16 x 1/32 x 1/32 in U-notch`; BOM row `174`).
- Compact segmented roller or equivalent if not already in hand (`row 175`).
- Fresh utility blades, masking tape, gloves, rags/cleaner, and disposable adhesive cleanup supplies as needed.

### Totals
- Active flooring package purchased to date: `$275.85`.
- Active flooring package remaining expected spend: `$429.08`.
- Active flooring package estimated total: `$704.93`.

## Installation Sequence
### Phase 0 - Bed rail dust/weather closeout before finish floor
1. Remove or lift bed rail caps as needed and photograph all old camper-install holes.
2. Confirm with Hiatus that the old roughly `2 in x 3 in` top-rail holes are not needed for the new camper interface.
3. Clean/degrease rail surfaces and rust-protect bare cut edges.
4. Close holes as dust/weather intrusion points using low-profile, serviceable cover patches where possible: thin aluminum/ABS/HDPE or similar non-absorbent patch/backer bedded in butyl tape, automotive seam sealer, MS polymer, or polyurethane sealant.
5. Reinstall rail caps with targeted sealing/gasketing while preserving drainage paths and avoiding camper-fit interference.

### Phase 1 - Prep / current-state correction
1. Clean bed thoroughly.
2. Trim EPS so it is not proud, buckled, or interfering with plywood seating.
3. Re-check structural hardpoints: remove EPS locally anywhere plywood must bear directly on steel.
4. Confirm the three plywood slices sit flat and can still be removed intentionally.

### Phase 2 - Between-Rib Insulation (mostly complete)
1. EPS remains between ribs only.
2. Maintain light tack-only adhesion where used; avoid full-surface bonding.
3. Confirm EPS does not interfere with hardpoint clearance zones.

### Phase 3 - Subfloor (`3/4 in` birch, three-slice state)
1. Verify panel seam strategy and removal path before finish flooring.
2. Confirm sealed bottom/edges/holes and untreated clean top bond face.
3. If new anchor holes are drilled, seal the inside of all plywood holes before final install.
4. Reinstall plywood and bolt structural hardpoints only after hardpoint pockets are clear.

### Phase 4 - Lonseal glue-down gate
Do not proceed until:
- bed rail/hole sealing is complete or explicitly deferred;
- EPS trim and plywood seating pass;
- no floor-through penetrations, drains, heater routes, anchor holes, or hidden hardpoints need access under the finish sheet;
- top plywood face is clean, dry, untreated, and adhesive-compatible;
- correct trowel and roller are on hand;
- dry cure window is available.

### Phase 5 - Finish Flooring
1. Dry-fit Lonseal sheet and align grain/pattern.
2. Apply adhesive per Lonseal adhesive manufacturer specification using the exact required trowel.
3. Lay vinyl and roll thoroughly.
4. Trim edges and allow cure before loading furniture.

## Final Build Height
- EPS: `0.625 in`
- Plywood: `0.750 in`
- Vinyl: `0.080 in`
- Total: approximately `1.46 in`

Confirm final door and tank clearances against this stack-up before permanent installation.

## Engineering Notes
- Thermal performance: moderate floor thermal decoupling from EPS; less top-side thermal break than prior EPDM-inclusive concept.
- Structural behavior: stiffer walking surface and higher point-load robustness with `3/4 in` birch.
- Moisture durability: sealed bottom face, edges, and drilled holes remain required because wood is directly above rib cavities; the top face stays untreated to remain compatible with the Lonseal vehicle-install substrate requirement for untreated plywood.
- Acoustic behavior: no dedicated EPDM damping layer in active stack; expect more direct structure-borne vibration vs prior concept.
- Serviceability: finish vinyl remains the only permanent bond layer, but one-piece Lonseal glued over three plywood slices will make subfloor removal materially harder. Treat glue-down as an explicit gate, not casual finish work.
