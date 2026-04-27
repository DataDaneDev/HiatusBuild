---
aliases:
  - Hiatus docs map
tags:
  - hiatus/docs-map
  - workspace/router
status: active
---

# Docs Map

Use this folder map when deciding where a document belongs.

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
| [ELECTRICAL_48V_ARCHITECTURE](core/ELECTRICAL_48V_ARCHITECTURE.md) | Final `48V` house/alternator architecture, shutdown logic, control-path intent | Implementation docs for exact conductor/fuse/layout detail, [TRACKING](core/TRACKING.md) for unresolved gates |
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
- Rule: implementation docs may expand the core baseline, but they should not silently redefine it.

## Plans
- [plans](plans/): active execution plans and order-of-operations docs.
- Rule: plans may sequence work and call out current focus, but they should point back to canonical design docs for the actual baseline.

## Studies
- [studies](studies/): topic-specific evaluations, option screens, and deep dives.
- Rule: once a decision is locked, studies become supporting history rather than current truth.

## Temp
- [temp](temp/): temporary issue trackers that can be retired once absorbed into canonical docs.
- Rule: any still-open item in `temp/` should either point to its canonical owner or be absorbed and retired.

## Legacy
- [legacy](legacy/): workbook extracts retained for traceability only.
- Rule: legacy docs are evidence and history, not update targets for current-state maintenance.

## Maintenance sequence
1. Update the structured source if the change begins in BOM rows, prices, model inputs, or measured data.
2. Update the owning core document.
3. Update dependent implementation/plan docs only where behavior, layout, or operator guidance changes.
4. Update [TRACKING](core/TRACKING.md) for decision/risk/open-question status changes.
5. Update [LOG](../logs/LOG.md) for dated evidence and completed work.
