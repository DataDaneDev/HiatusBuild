# Hiatus Truck Bed Camper Project

This is the single workspace map and update guide for the Hiatus/F-350 camper build. The repo is now in the **hard-mounted electrical / utilities commissioning** phase: use it to keep the permanent floor, battery-bank closeout, `12V` commissioning, shore inlet, tank/wet-spine work, payload, and 80/20/panel decisions aligned without creating parallel notes.

## Open in Obsidian
- Start at [00 Home](00%20Home.md) for the shortest navigation path.
- Use this README for maintenance rules and [Docs Map](docs/README.md) for document ownership.
- The shared `.obsidian` settings group the graph by folder role and keep personal workspace state local.

## Fixed project constants
- Truck: 2021 Ford F-350 Regular Cab Long Bed with aluminum pickup box
- Truck mods: 2.5 inch lift, 37 inch tires, 4.88 differential regear
- Camper status: Hiatus shell is in hand/installed; May 7, 2026 install readiness is now historical context
- Primary use: Financial Analyst remote work (typical 9-5, Monday-Friday) with occasional subsidiary flights

## Current project posture — 2026-08-03
- Current focus: protect and temporarily mount the live ICECO switch, terminate/configure the KUS sender, wire the `14 AWG / 10A` SHURflo branch, and pull every access-dependent office/Galley AC/DC/control branch before finish panels. Finish Battery 3 charging/rested-voltage matching and parallel the `3x 48V` bank only at `<=0.1V` spread. Positive per-battery/cooler road restraint remains required before travel; one strap over the whole bank is not the final restraint.
- Flooring/module state: the permanent Lonseal/plywood floor, electrical module, Galley/cooler support, water tank, and the reinstalled Bench extrusion between the electrical and Galley modules are owner-reported hard-mounted. The integrated extrusion structure is now very stiff; the remaining mobile-structure gate is concentrated on positive restraint of the `3x 48V` batteries, the separate `12V` battery, the ICECO cooler, and final cable/terminal protection rather than another broad module rebuild.
- Battery state: all three `2/0 AWG` branch harnesses are complete and landed but the batteries remain isolated. Battery 1 completed the corrected `20A`-cap cycle through `56.8V` absorption and `54.0V` float; Battery 2 resumed and reached absorption on `2026-08-03`; Battery 3 remains pending. Rest and record each before paralleling.
- `12V` state: the Orion charges the buffer battery and the camper `12V` system is operating correctly. The ICECO appliance lead is switched and landed on `12V-02` with a `15A` fuse; exposed positive switch tabs still need individual insulation and temporary hard mounting. Final source topology remains `battery + -> F-11 100A ANL -> SW-12V-BATT -> panel main +` and `battery - -> panel main -`, with Orion input from Lynx Slot 4 through one verified `F-05 40A` MEGA rated at least `58VDC` and Orion output through `F-07 60A/80V`.
- Water state: all three passenger-rear pass-throughs are installed and the `36 gal` wheel-well tank is hard-mounted with two metal straps into the truck-bed-wall plusnut locations. The replacement KUS `FLS-U` under-ring/gasket/matched hardware is installed and visually seated; its two-wire lead is routed to the Cerbo but not terminated. Final Cerbo setup/full-system leak proof, fill/vent, sink/faucet termination, and the dry pressure/dwell acceptance test remain open.
- Counter/first-trip state: the three-piece black-walnut installation has a mid-September `2026` target. Full temporary tops are dropped; only a rough removable Galley sheet remains optional. Ground-deployed Starlink through the existing service route is the accepted first-trip fallback while the moving-coil wall entry remains measurement-gated.
- Electrical commissioning state: first-live `48V`, inverter, limited AC-in charging, corrected single-battery charger behavior, Orion, and camper `12V` checkpoints have passed. A single Progressive Industries EMS dropout self-recovered through its normal reconnect countdown and retained no previous-error code; monitor for recurrence rather than treating it as a present fault. The permanent shore-splice/dead-check closeout, full parallel bank, AC-out/GFCI, final road restraint, and alternator commissioning remain separate gates.
- Payload posture: legal payload still depends on the door sticker/scale tickets; water, batteries, bumpers, spare, 80/20, panels, tools, and tech remain active weight risks.

## First-stop update map
Use this table first whenever you are deciding where to put information.

| If you are updating... | Update here first |
| --- | --- |
| Project scope, milestones, constraints, sequencing status | [PROJECT](docs/core/PROJECT.md) |
| Final `48V` house/alternator architecture, shutdown path, and wiring intent | [ELECTRICAL_48V_ARCHITECTURE](docs/core/ELECTRICAL_48V_ARCHITECTURE.md) |
| Electrical/solar/plumbing/comms/system architecture | [SYSTEMS](docs/core/SYSTEMS.md) |
| Checklists, maintenance cadence, travel handoff process | [OPERATIONS](docs/core/OPERATIONS.md) |
| Decisions, risks, assumptions, open questions | [TRACKING](docs/core/TRACKING.md) |
| Day-by-day progress notes or test evidence | [LOG](logs/LOG.md) |
| Active build procurement line items | [bom_estimated_items.csv](bom/bom_estimated_items.csv) |
| Returned/retired BOM history | [bom_inactive_items.csv](bom/bom_inactive_items.csv) |
| BOM schema, controlled vocabularies, and editing rules | [BOM data contract](bom/README.md) |
| Non-build misc/camping shopping items | [bom_misc_items.csv](bom/bom_misc_items.csv) |
| Electrical load modeling assumptions (Wh) | [load_model_wh.csv](bom/load_model_wh.csv) |
| Electrical implementation topology details | [ELECTRICAL_overview_diagram](docs/implementation/ELECTRICAL_overview_diagram.md) |
| Fuse IDs, values, holders, spare policy | [ELECTRICAL_fuse_schedule](docs/implementation/ELECTRICAL_fuse_schedule.md) |
| Mechman `48V` alternator / WS500 / APM-48 install and first-run guide | [ELECTRICAL_Mechman_WS500_APM48_install_guide](docs/implementation/ELECTRICAL_Mechman_WS500_APM48_install_guide.md) |
| Bench-build electrical layout and staged test checklist | [ELECTRICAL_bench_layout_and_test_guide](docs/implementation/ELECTRICAL_bench_layout_and_test_guide.md) |
| AC implementation and branch intent | [ELECTRICAL_AC_BOM](docs/implementation/ELECTRICAL_AC_BOM.md) |
| Interior furniture/galley/workstation layout | [INTERIOR_furniture_layout_and_galley](docs/implementation/INTERIOR_furniture_layout_and_galley.md), [INTERIOR_driver_side_workstation](docs/implementation/INTERIOR_driver_side_workstation.md) |
| Flooring / sheet-vinyl finish gate | [FLOORING_subfloor_build_process](docs/implementation/FLOORING_subfloor_build_process.md) |
| Active post-install order of operations | [PROJECT_build_order_of_operations](docs/plans/PROJECT_build_order_of_operations.md), [LIVE_BUILD_CHECKLIST](docs/plans/LIVE_BUILD_CHECKLIST.md) |
| Starlink/solar moving-roof jumper architecture and current-source shortlist | [STARLINK_SOLAR_MOVING_UMBILICAL](docs/plans/STARLINK_SOLAR_MOVING_UMBILICAL.md) |
| Active procurement / WIP shopping carts / module cut-list artifacts | [PROCUREMENT_purchase_list](docs/plans/PROCUREMENT_purchase_list_2026-05-26.md), [TNUTZ_80_20_HARDWARE_MODEL](docs/plans/TNUTZ_80_20_HARDWARE_MODEL_2026-06-01.md), [INTERIOR_LIGHTING_PLAN](docs/plans/INTERIOR_LIGHTING_PLAN_2026-05-31.md) |
| Future/preliminary audio package | [CAMPER_audio_system](docs/implementation/CAMPER_audio_system.md) |
| Historical install-window / pre-camper references | [INSTALL_MINUS_12_READINESS_PLAN](docs/plans/INSTALL_MINUS_12_READINESS_PLAN.md), [STARTER_PLAN_electrical_and_flooring_pre_camper](docs/plans/STARTER_PLAN_electrical_and_flooring_pre_camper.md) |

## Document relationship rules
- One topic should have one owning file. Related files may summarize or point to it, but should not compete with it.
- `docs/core/` owns the current project truth.
- `docs/implementation/` owns exact build detail that supports the active core baseline.
- `docs/plans/` owns execution sequence and short-horizon action framing, not architecture truth.
- `docs/studies/` owns option analysis and historical reasoning, not the active baseline once a decision is locked.
- `docs/temp/` and `docs/legacy/` are non-canonical support layers and must not silently override core docs.
- Structured inputs own structured facts:
  - [bom_estimated_items.csv](bom/bom_estimated_items.csv) owns active line items and purchase status.
  - [bom_inactive_items.csv](bom/bom_inactive_items.csv) preserves stable-ID returned/retired history outside the active total.
  - [BOM data contract](bom/README.md) owns the CSV schema and normalization rules.
  - [load_model_wh.csv](bom/load_model_wh.csv) owns load-model inputs and scenario math.
- [TRACKING](docs/core/TRACKING.md) owns decision, risk, assumption, and open-question status.
- [LOG](logs/LOG.md) owns dated work evidence, measured outcomes, and test history.

## Canonical docs rule
- Update existing canonical files before creating new docs.
- If a topic seems to belong in more than one place, keep detail in one file and link to it from the others.
- When in doubt:
1. Put active decision/risk/question status in [TRACKING](docs/core/TRACKING.md).
2. Put execution notes and evidence in [LOG](logs/LOG.md).

## Maintenance order
Use this order whenever the same change touches multiple files:

1. Update the structured source first if the change affects line items, component selections, prices, load assumptions, or measured model inputs.
2. Update the owning canonical doc from the first-stop map.
3. Update dependent docs only where the reader needs a summary, pointer, or changed downstream instruction.
4. Update `docs/core/TRACKING.md` if the change affects decision state, risk state, assumptions, or open questions.
5. Update `logs/LOG.md` if physical work was performed, measurements were taken, or a test/verification step occurred.
6. Regenerate PDF exports only after the source markdown files are current.

## Workspace structure
- `docs/`: organized doc sets; see [Docs Map](docs/README.md) for the folder map.
- `docs/plans/assets/module-cutlists/`: dated current and historical module cut-list / assignment workbook artifacts.
- `bom/`: procurement CSVs and load model CSV.
- `cad/`: Fusion 360 files, exports, and drawing artifacts.
- `logs/`: running build/test log.
- `media/`: progress photos and inspiration imports.
- `references/`: external manuals, datasheets, and source PDFs.
- `scripts/`: utility automation (for example, PDF export).
- `Camper Build.xlsx`: legacy workbook source.

## Docs scope
- Canonical planning docs:
1. [PROJECT](docs/core/PROJECT.md)
2. [ELECTRICAL_48V_ARCHITECTURE](docs/core/ELECTRICAL_48V_ARCHITECTURE.md)
3. [SYSTEMS](docs/core/SYSTEMS.md)
4. [OPERATIONS](docs/core/OPERATIONS.md)
5. [TRACKING](docs/core/TRACKING.md)
- Supporting implementation artifacts:
1. [ELECTRICAL_overview_diagram](docs/implementation/ELECTRICAL_overview_diagram.md)
2. [ELECTRICAL_fuse_schedule](docs/implementation/ELECTRICAL_fuse_schedule.md)
3. [ELECTRICAL_Mechman_WS500_APM48_install_guide](docs/implementation/ELECTRICAL_Mechman_WS500_APM48_install_guide.md)
4. [ELECTRICAL_AC_BOM](docs/implementation/ELECTRICAL_AC_BOM.md)
5. [ELECTRICAL_bench_layout_and_test_guide](docs/implementation/ELECTRICAL_bench_layout_and_test_guide.md)
6. [FLOORING_subfloor_build_process](docs/implementation/FLOORING_subfloor_build_process.md)
7. [INTERIOR_furniture_layout_and_galley](docs/implementation/INTERIOR_furniture_layout_and_galley.md)
8. [INTERIOR_driver_side_workstation](docs/implementation/INTERIOR_driver_side_workstation.md)
9. [CAMPER_audio_system](docs/implementation/CAMPER_audio_system.md) - preliminary/future
- Workbook extracts kept for traceability (non-canonical):
1. [PROJECT_workbook_hiatus_consult](docs/legacy/PROJECT_workbook_hiatus_consult.md)
2. [SYSTEMS_workbook_build_notes_obsolete](docs/legacy/SYSTEMS_workbook_build_notes_obsolete.md)
- Archived issue trackers retained for compatibility, not live routing:
1. [TEMP_electrical_red_flags](docs/temp/TEMP_electrical_red_flags.md)
2. [TEMP_procurement_red_flags](docs/temp/TEMP_procurement_red_flags.md)

## Relationship quick guide
- [PROJECT](docs/core/PROJECT.md): scope, milestones, sequencing posture, and near-term priorities.
- [ELECTRICAL_48V_ARCHITECTURE](docs/core/ELECTRICAL_48V_ARCHITECTURE.md): final `48V` electrical architecture and shutdown/control logic.
- [SYSTEMS](docs/core/SYSTEMS.md): active subsystem baselines and cross-system modeling context.
- [OPERATIONS](docs/core/OPERATIONS.md): checklists, commissioning/inspection routines, and repeatable operating procedures.
- [TRACKING](docs/core/TRACKING.md): what changed in decision status, what is risky, and what is still unresolved.
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
1. [ELECTRICAL_AC_BOM](docs/implementation/ELECTRICAL_AC_BOM.md)
2. [ELECTRICAL_fuse_schedule](docs/implementation/ELECTRICAL_fuse_schedule.md)
3. [ELECTRICAL_overview_diagram](docs/implementation/ELECTRICAL_overview_diagram.md)
4. [ELECTRICAL_bench_layout_and_test_guide](docs/implementation/ELECTRICAL_bench_layout_and_test_guide.md)
5. [FLOORING_subfloor_build_process](docs/implementation/FLOORING_subfloor_build_process.md)
6. [SYSTEMS](docs/core/SYSTEMS.md)
7. [PROJECT](docs/core/PROJECT.md)
8. [ELECTRICAL_48V_ARCHITECTURE](docs/core/ELECTRICAL_48V_ARCHITECTURE.md)
9. [INSTALL_MINUS_12_READINESS_PLAN](docs/plans/INSTALL_MINUS_12_READINESS_PLAN.md)
