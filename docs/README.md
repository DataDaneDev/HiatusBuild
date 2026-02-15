# Docs Overview

Use these files as canonical sources to keep context centralized and AI-friendly:

- `docs/PROJECT.md`: scope, requirements, milestones, constraints
- `docs/SYSTEMS.md`: electrical, solar, plumbing, comms, structure, cabinetry, HVAC, safety
- `docs/OPERATIONS.md`: checklists, maintenance, travel/flight procedures
- `docs/TRACKING.md`: decisions, risks, assumptions, templates, open questions

Rule: update one of these first before creating any new doc file.

BOM source of truth:
- `bom/bom_estimated_items.csv` is the only maintained build BOM file (line-item level; no in-file total row).
- `bom/bom_misc_items.csv` is maintained separately for non-build camping/lifestyle items (not part of the build BOM rollup).

Supplementary workbook extracts (non-canonical, for traceability):
- `docs/PROJECT_workbook_hiatus_consult.md`
- `docs/SYSTEMS_workbook_build_notes.md`
- `docs/SYSTEMS_workbook_electrical_notes.md`
- `docs/OPERATIONS_workbook_marketplace_finds.md`

Supplementary working artifacts:
- `docs/ELECTRICAL_overview_diagram.md` (implementation-level topology with components, fuse/holder map, and conductor schedule assumptions)
- `docs/ELECTRICAL_fuse_schedule.md` (fuse IDs, housing/holder methods, gauge tie-ins, spare inventory, and BOM row mapping)
- `docs/PROJECT_build_order_of_operations.md` (staged build order with parallel workstreams, hold points, and date-window planning)
- `docs/TEMP_electrical_red_flags.md` (temporary electrical issue tracker and resolution queue)
- `docs/TEMP_procurement_red_flags.md` (temporary procurement-readiness issue tracker and resolution queue)
