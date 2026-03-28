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
| Project scope, milestones, constraints, sequencing status | `docs/core/PROJECT.md` |
| Final `48V` house/alternator architecture, shutdown path, and wiring intent | `docs/core/ELECTRICAL_48V_ARCHITECTURE.md` |
| Electrical/solar/plumbing/comms/system architecture | `docs/core/SYSTEMS.md` |
| Checklists, maintenance cadence, travel handoff process | `docs/core/OPERATIONS.md` |
| Decisions, risks, assumptions, open questions | `docs/core/TRACKING.md` |
| Day-by-day progress notes or test evidence | `logs/LOG.md` |
| Build procurement line items | `bom/bom_estimated_items.csv` |
| Non-build misc/camping shopping items | `bom/bom_misc_items.csv` |
| Electrical load modeling assumptions (Wh) | `bom/load_model_wh.csv` |
| Electrical implementation topology details | `docs/implementation/ELECTRICAL_overview_diagram.md` |
| Fuse IDs, values, holders, spare policy | `docs/implementation/ELECTRICAL_fuse_schedule.md` |
| Bench-build electrical layout and staged test checklist | `docs/implementation/ELECTRICAL_bench_layout_and_test_guide.md` |
| Pre-camper starter execution plan (electrical + flooring) | `docs/plans/STARTER_PLAN_electrical_and_flooring_pre_camper.md` |

## Canonical docs rule
- Update existing canonical files before creating new docs.
- If a topic seems to belong in more than one place, keep detail in one file and link to it from the others.
- When in doubt:
1. Put active decision/risk/question status in `docs/core/TRACKING.md`.
2. Put execution notes and evidence in `logs/LOG.md`.

## Workspace structure
- `docs/`: organized doc sets; see `docs/README.md` for the folder map.
- `bom/`: procurement CSVs and load model CSV.
- `cad/`: Fusion 360 files, exports, and drawing artifacts.
- `logs/`: running build/test log.
- `media/`: progress photos and inspiration imports.
- `references/`: external manuals, datasheets, and source PDFs.
- `scripts/`: utility automation (for example, PDF export).
- `Camper Build.xlsx`: legacy workbook source.

## Docs scope
- Canonical planning docs:
1. `docs/core/PROJECT.md`
2. `docs/core/ELECTRICAL_48V_ARCHITECTURE.md`
3. `docs/core/SYSTEMS.md`
4. `docs/core/OPERATIONS.md`
5. `docs/core/TRACKING.md`
- Supporting implementation artifacts:
1. `docs/implementation/ELECTRICAL_overview_diagram.md`
2. `docs/implementation/ELECTRICAL_fuse_schedule.md`
3. `docs/plans/PROJECT_build_order_of_operations.md`
4. `docs/implementation/ELECTRICAL_AC_BOM.md`
5. `docs/implementation/ELECTRICAL_bench_layout_and_test_guide.md`
- Workbook extracts kept for traceability (non-canonical):
1. `docs/legacy/PROJECT_workbook_hiatus_consult.md`
2. `docs/legacy/SYSTEMS_workbook_build_notes_obsolete.md`
- Temporary issue trackers still present for compatibility:
1. `docs/temp/TEMP_electrical_red_flags.md`
2. `docs/temp/TEMP_procurement_red_flags.md`

## Folder usage details
- `cad/`: place Fusion files in `cad/fusion360/`, exports in `cad/exports/`, annotated drawings in `cad/drawings/`.
- `media/`: use `media/progress/` and `media/inspiration/`; for each import, log context in `logs/LOG.md`.
- `references/`: use descriptive filenames and link them from `docs/core/SYSTEMS.md` or `docs/core/PROJECT.md`.

## Automation notes
- PDF exports are generated with `scripts/export-doc-pdfs.mjs`.
- Default export targets include:
1. `docs/implementation/ELECTRICAL_AC_BOM.md`
2. `docs/implementation/ELECTRICAL_fuse_schedule.md`
3. `docs/implementation/ELECTRICAL_overview_diagram.md`
4. `docs/implementation/ELECTRICAL_bench_layout_and_test_guide.md`
5. `docs/implementation/FLOORING_subfloor_build_process.md`
6. `docs/core/SYSTEMS.md`
7. `docs/core/PROJECT.md`
8. `docs/core/ELECTRICAL_48V_ARCHITECTURE.md`
