# Hiatus Truck Bed Camper Project

This is the single workspace map and update guide for the project.

## Fixed project constants
- Truck: 2021 Ford F-350 Regular Cab Long Bed
- Truck mods: 2.5 inch lift, 37 inch tires, 4.88 differential regear
- Camper milestone: ready for install on May 7, 2026
- Primary use: Financial Analyst remote work (typical 9-5, Monday-Friday) with occasional subsidiary flights

## First-stop update map
Use this table first whenever you are deciding where to put information.

| If you are updating... | Update here first |
| --- | --- |
| Project scope, milestones, constraints, sequencing status | `docs/PROJECT.md` |
| Electrical/solar/plumbing/comms/system architecture | `docs/SYSTEMS.md` |
| Checklists, maintenance cadence, travel handoff process | `docs/OPERATIONS.md` |
| Decisions, risks, assumptions, open questions | `docs/TRACKING.md` |
| Day-by-day progress notes or test evidence | `logs/LOG.md` |
| Build procurement line items | `bom/bom_estimated_items.csv` |
| Non-build misc/camping shopping items | `bom/bom_misc_items.csv` |
| Electrical load modeling assumptions (Wh) | `bom/load_model_wh.csv` |
| Electrical implementation topology details | `docs/ELECTRICAL_overview_diagram.md` |
| Fuse IDs, values, holders, spare policy | `docs/ELECTRICAL_fuse_schedule.md` |

## Canonical docs rule
- Update existing canonical files before creating new docs.
- If a topic seems to belong in more than one place, keep detail in one file and link to it from the others.
- When in doubt:
1. Put active decision/risk/question status in `docs/TRACKING.md`.
2. Put execution notes and evidence in `logs/LOG.md`.

## Workspace structure
- `docs/`: project planning and technical design docs.
- `bom/`: procurement CSVs and load model CSV.
- `cad/`: Fusion 360 files, exports, and drawing artifacts.
- `logs/`: running build/test log.
- `media/`: progress photos and inspiration imports.
- `references/`: external manuals, datasheets, and source PDFs.
- `scripts/`: utility automation (for example, PDF export).
- `Camper Build.xlsx`: legacy workbook source.

## Docs scope
- Canonical planning docs:
1. `docs/PROJECT.md`
2. `docs/SYSTEMS.md`
3. `docs/OPERATIONS.md`
4. `docs/TRACKING.md`
- Supporting implementation artifacts:
1. `docs/ELECTRICAL_overview_diagram.md`
2. `docs/ELECTRICAL_fuse_schedule.md`
3. `docs/PROJECT_build_order_of_operations.md`
4. `docs/ELECTRICAL_AC_BOM.md`
- Workbook extracts kept for traceability (non-canonical):
1. `docs/PROJECT_workbook_hiatus_consult.md`
2. `docs/SYSTEMS_workbook_build_notes.md`
3. `docs/SYSTEMS_workbook_electrical_notes.md`
4. `docs/OPERATIONS_workbook_marketplace_finds.md`
- Temporary issue trackers still present for compatibility:
1. `docs/TEMP_electrical_red_flags.md`
2. `docs/TEMP_procurement_red_flags.md`

## Folder usage details
- `cad/`: place Fusion files in `cad/fusion360/`, exports in `cad/exports/`, annotated drawings in `cad/drawings/`.
- `media/`: use `media/progress/` and `media/inspiration/`; for each import, log context in `logs/LOG.md`.
- `references/`: use descriptive filenames and link them from `docs/SYSTEMS.md` or `docs/PROJECT.md`.

## Automation notes
- PDF exports are generated with `scripts/export-doc-pdfs.mjs`.
- Default export targets include:
1. `docs/ELECTRICAL_AC_BOM.md`
2. `docs/ELECTRICAL_fuse_schedule.md`
3. `docs/ELECTRICAL_overview_diagram.md`
4. `docs/SYSTEMS.md`
5. `docs/PROJECT.md`
