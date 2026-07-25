---
aliases:
  - Hiatus docs map
tags:
  - hiatus/docs-map
  - workspace/router
status: active
---

# Docs Map

Use this folder map when deciding where a document belongs. Current repo posture is **permanent-floor cure plus utilities-first restrained module reinstall** (`2026-07-16`): keep active truth in the owner docs below, and treat pre-install/readiness plans as historical references unless explicitly refreshed.

## Obsidian navigation
- Start with [00 Home](../00%20Home.md) for daily navigation.
- Use this file for ownership boundaries and maintenance order.
- The strongest Obsidian links should point to owner docs, not duplicate their content.

## Document ownership rules
- Keep one owner for each topic and let other files point back to it.
- Core docs define the active baseline.
- Implementation docs define exact build detail in support of the active baseline.
- Plans define sequence and short-horizon execution, not final architecture truth.
- Studies preserve analysis and reasoning history, but once a direction is locked the core docs become authoritative.
- Temp and legacy files are support layers only and must not become the de facto current state.

## Core relationship map
| File | Owns | Defers to |
| --- | --- | --- |
| [PROJECT](core/PROJECT.md) | Scope, milestones, sequencing posture, near-term priorities | [SYSTEMS](core/SYSTEMS.md) for subsystem baselines, [ELECTRICAL_48V_ARCHITECTURE](core/ELECTRICAL_48V_ARCHITECTURE.md) for final `48V` design, [TRACKING](core/TRACKING.md) for live decision/risk/open-question state |
| [ELECTRICAL_48V_ARCHITECTURE](core/ELECTRICAL_48V_ARCHITECTURE.md) | Final `48V` house/alternator architecture, shutdown logic, control-path intent | Implementation docs for exact conductor/fuse/layout detail, [ELECTRICAL_Mechman_WS500_APM48_install_guide](implementation/ELECTRICAL_Mechman_WS500_APM48_install_guide.md) for install/commissioning procedure, [TRACKING](core/TRACKING.md) for unresolved gates |
| [SYSTEMS](core/SYSTEMS.md) | Cross-system baseline, subsystem design snapshot, modeling context | [ELECTRICAL_48V_ARCHITECTURE](core/ELECTRICAL_48V_ARCHITECTURE.md) for locked `48V` architecture, implementation docs for install-level detail, [TRACKING](core/TRACKING.md) for state changes |
| [OPERATIONS](core/OPERATIONS.md) | Checklists, inspections, commissioning and field procedures | Core design docs for architecture rationale, [LOG](../logs/LOG.md) for dated results |
| [TRACKING](core/TRACKING.md) | Decisions, risks, assumptions, open questions | Owner docs for full current design or procedure detail |

## Core
- [PROJECT](core/PROJECT.md): project scope, milestones, sequencing, and near-term priorities.
- [ELECTRICAL_48V_ARCHITECTURE](core/ELECTRICAL_48V_ARCHITECTURE.md): canonical `48V` house/alternator design, wiring intent, shutdown order, and final decisions.
- [SYSTEMS](core/SYSTEMS.md): current system architecture baseline across major subsystems.
- [OPERATIONS](core/OPERATIONS.md): checklists, maintenance, inspections, and handoff procedures.
- [TRACKING](core/TRACKING.md): decisions, risks, assumptions, and open questions.

## Implementation
- [implementation](implementation/): build-ready reference docs that support the active baseline.
- [INTERIOR_furniture_layout_and_galley](implementation/INTERIOR_furniture_layout_and_galley.md): current draft office-first interior layout, passenger-side lofted fridge/wet-spine exoskeleton, separated battery bench, 10-series 80/20/overlay-panel direction, service-panel rules, and generated concept caveats.
- [INTERIOR_finish_paneling_and_feature_choices](implementation/INTERIOR_finish_paneling_and_feature_choices.md): draft Galley/desk finish and feature-design choices — wood tops, paneling, smoked acrylic/polycarbonate accents, storage mix, 45-degree Galley cupboard, latches, anti-rattle, and validation gates.
- [INTERIOR_driver_side_workstation](implementation/INTERIOR_driver_side_workstation.md): draft driver-side desk, stow-low monitor, electrical-closet/DC-shelf interface, diesel-heater base zone, and storage mechanism design.
- [CAMPER_audio_system](implementation/CAMPER_audio_system.md): preliminary/future camper-only `12V` audio package, source/sub/speaker selection, fusing, wire sizing, routing, and tuning notes; not near-term procurement.
- [ELECTRICAL_overview_diagram](implementation/ELECTRICAL_overview_diagram.md): implementation topology, conductor IDs, branch maps, diagrams, and active electrical assumptions.
- [ELECTRICAL_fuse_schedule](implementation/ELECTRICAL_fuse_schedule.md): fuse IDs, amperages, holder/fuse families, Orion Lynx Slot 4 `F-05`, spare policy, and BOM row mapping.
- [ELECTRICAL_Mechman_WS500_APM48_install_guide](implementation/ELECTRICAL_Mechman_WS500_APM48_install_guide.md): detailed shop guide for Mechman `48V` alternator, WS500, APM-48, staged-install/drivability gates, first-run tests, and shutdown/fault handling.
- [ELECTRICAL_AC_BOM](implementation/ELECTRICAL_AC_BOM.md): purchased Phase 1 AC hardware and Branch A/B outlet intent.
- [ELECTRICAL_bench_layout_and_test_guide](implementation/ELECTRICAL_bench_layout_and_test_guide.md): staged electrical commissioning, first-live results, hard-mounting/access checks, and post-live wiring/strain-relief validation.
- [FLOORING_subfloor_build_process](implementation/FLOORING_subfloor_build_process.md): permanent floor as-built state, cure/post-cure checks, hardpoint recovery, and finish-floor serviceability.
- Rule: implementation docs may expand the core baseline, but they should not silently redefine it.

## Plans
- [plans](plans/): active execution plans, procurement aids, WIP carts, and historical references.
- [LIVE_BUILD_CHECKLIST](plans/LIVE_BUILD_CHECKLIST.md): live running build checklist and cure/integration-gate tracker; update whenever practical build state, blockers, or next shop actions change.
- [PROJECT_build_order_of_operations](plans/PROJECT_build_order_of_operations.md): active floor-cure, tank/electrical dependency, penetration, and restrained-reinstall sequence.
- [PROCUREMENT_purchase_list_2026-05-26](plans/PROCUREMENT_purchase_list_2026-05-26.md): dated procurement snapshot; `bom/bom_estimated_items.csv` owns current item/status truth.
- [TNUTZ_80_20_HARDWARE_MODEL_2026-06-01](plans/TNUTZ_80_20_HARDWARE_MODEL_2026-06-01.md): consolidated WIP TNUTZ `10-series` cart, hardware model, visual-aid owner, and pointer to dated module cut-list workbooks under `plans/assets/module-cutlists/`.
- [INTERIOR_LIGHTING_PLAN_2026-05-31](plans/INTERIOR_LIGHTING_PLAN_2026-05-31.md): deferred desired `12V` QuinLED/WLED interior lighting design with hardwired buttons; supersedes the prior `24V`/MiBoxer worksheet and is not near-term procurement.
- [HIATUS_work_plan_2026-05-29](plans/HIATUS_work_plan_2026-05-29.md): historical one-night work plan and rough cutlist worksheet; not current sequencing.
- [INSTALL_MINUS_12_READINESS_PLAN](plans/INSTALL_MINUS_12_READINESS_PLAN.md) and [STARTER_PLAN_electrical_and_flooring_pre_camper](plans/STARTER_PLAN_electrical_and_flooring_pre_camper.md): historical install-window/pre-camper references unless updated at the top with a newer as-of date.
- Rule: plans may sequence work and call out current focus, but they should point back to canonical design docs for the actual baseline.

## Studies
- [studies](studies/): topic-specific evaluations, option screens, and deep dives.
- Rule: once a decision is locked, studies become supporting history rather than current truth.

## Temp
- [temp](temp/): archived temporary issue trackers retained for compatibility/provenance only.
- Rule: do not use `temp/` as live routing; absorb still-relevant items into canonical owners before acting on them.

## Legacy
- [legacy](legacy/): workbook extracts retained for traceability only.
- Rule: legacy docs are evidence and history, not update targets for current-state maintenance.

## Maintenance sequence
1. Update the structured source if the change begins in BOM rows, prices, model inputs, or measured data.
2. Update the owning core document.
3. Update dependent implementation/plan docs only where behavior, layout, or operator guidance changes.
4. Update [TRACKING](core/TRACKING.md) for decision/risk/open-question status changes.
5. Update [LOG](../logs/LOG.md) for dated evidence and completed work.
