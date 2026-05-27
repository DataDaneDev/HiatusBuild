---
aliases:
  - Hiatus vault home
tags:
  - hiatus/home
  - workspace/router
status: active
---

# Hiatus Build Home

Start here when opening the project in Obsidian.

## Active Now
- [Project](docs/core/PROJECT.md) - scope, milestones, fixed constraints, near-term priorities.
- [Build order of operations](docs/plans/PROJECT_build_order_of_operations.md) - post-install sequence from measured envelopes through rough-in, module build, and commissioning.
- [Interior furniture and galley](docs/implementation/INTERIOR_furniture_layout_and_galley.md) - current office-first passenger-side lofted fridge/wet-spine, separated battery bench, and 10-series/overlay-panel furniture direction.
- [Electrical bench layout and test guide](docs/implementation/ELECTRICAL_bench_layout_and_test_guide.md) - staged electrical commissioning, post-live cleanup, hard-mounting, and strain-relief discipline.
- [Tracking](docs/core/TRACKING.md) - decisions, risks, assumptions, open questions.
- [Project Log](logs/LOG.md) - dated work evidence, measurements, tests, and follow-ups.

## Canonical Baseline
- [Systems](docs/core/SYSTEMS.md) - subsystem baseline and cross-system model.
- [48V Electrical Architecture](docs/core/ELECTRICAL_48V_ARCHITECTURE.md) - locked house/alternator architecture, shutdown order, control path.
- [Operations](docs/core/OPERATIONS.md) - repeatable checklists, inspections, commissioning, field procedures.
- [Docs Map](docs/README.md) - ownership rules and maintenance sequence.

## Build Detail
- [Electrical topology diagram](docs/implementation/ELECTRICAL_overview_diagram.md)
- [Electrical fuse schedule](docs/implementation/ELECTRICAL_fuse_schedule.md)
- [Electrical bench layout and test guide](docs/implementation/ELECTRICAL_bench_layout_and_test_guide.md)
- [Electrical AC BOM](docs/implementation/ELECTRICAL_AC_BOM.md)
- [Flooring subfloor build process](docs/implementation/FLOORING_subfloor_build_process.md)

## Plans And History
- [May 7 install readiness plan](docs/plans/INSTALL_MINUS_12_READINESS_PLAN.md) - historical install-window and early shakedown reference.
- [Starter electrical and flooring plan](docs/plans/STARTER_PLAN_electrical_and_flooring_pre_camper.md) - historical pre-camper execution reference.
- [Studies](docs/studies/) - option analysis and historical reasoning.
- [Legacy extracts](docs/legacy/) - workbook history only, not current-state maintenance.
- [Temporary trackers](docs/temp/) - retire or absorb into canonical docs as items close.

## Structured Sources
- [Estimated BOM](bom/bom_estimated_items.csv)
- [Misc items](bom/bom_misc_items.csv)
- [Load model](bom/load_model_wh.csv)
- [References](references/)
- [Media](media/)
- [CAD](cad/)

## Update Rhythm
1. Update the structured source first when facts come from BOM rows, prices, load inputs, or measurements.
2. Update the owning canonical doc from [README](README.md) or [Docs Map](docs/README.md).
3. Add only the needed summary or pointer in dependent implementation and plan docs.
4. Update [Tracking](docs/core/TRACKING.md) for decision, risk, assumption, or open-question state.
5. Update [Project Log](logs/LOG.md) for dated evidence, tests, measurements, or physical work.
