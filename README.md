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

## Document relationship rules
- One topic should have one owning file. Related files may summarize or point to it, but should not compete with it.
- `docs/core/` owns the current project truth.
- `docs/implementation/` owns exact build detail that supports the active core baseline.
- `docs/plans/` owns execution sequence and short-horizon action framing, not architecture truth.
- `docs/studies/` owns option analysis and historical reasoning, not the active baseline once a decision is locked.
- `docs/temp/` and `docs/legacy/` are non-canonical support layers and must not silently override core docs.
- Structured inputs own structured facts:
  - `bom/bom_estimated_items.csv` owns current line items and purchase status.
  - `bom/load_model_wh.csv` owns load-model inputs and scenario math.
- `docs/core/TRACKING.md` owns decision, risk, assumption, and open-question status.
- `logs/LOG.md` owns dated work evidence, measured outcomes, and test history.

## Canonical docs rule
- Update existing canonical files before creating new docs.
- If a topic seems to belong in more than one place, keep detail in one file and link to it from the others.
- When in doubt:
1. Put active decision/risk/question status in `docs/core/TRACKING.md`.
2. Put execution notes and evidence in `logs/LOG.md`.

## Maintenance order
Use this order whenever the same change touches multiple files:

1. Update the structured source first if the change affects line items, component selections, prices, load assumptions, or measured model inputs.
2. Update the owning canonical doc from the first-stop map.
3. Update dependent docs only where the reader needs a summary, pointer, or changed downstream instruction.
4. Update `docs/core/TRACKING.md` if the change affects decision state, risk state, assumptions, or open questions.
5. Update `logs/LOG.md` if physical work was performed, measurements were taken, or a test/verification step occurred.
6. Regenerate PDF exports only after the source markdown files are current.

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

## Relationship quick guide
- `docs/core/PROJECT.md`: scope, milestones, sequencing posture, and near-term priorities.
- `docs/core/ELECTRICAL_48V_ARCHITECTURE.md`: final `48V` electrical architecture and shutdown/control logic.
- `docs/core/SYSTEMS.md`: active subsystem baselines and cross-system modeling context.
- `docs/core/OPERATIONS.md`: checklists, commissioning/inspection routines, and repeatable operating procedures.
- `docs/core/TRACKING.md`: what changed in decision status, what is risky, and what is still unresolved.
- `docs/implementation/*`: exact layouts, schedules, and install/test detail that must agree with the active core baseline.
- `docs/plans/*`: time-ordered execution guidance for the current phase.
- `docs/studies/*`: analysis history and option screening that inform, but do not replace, the active baseline.

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
