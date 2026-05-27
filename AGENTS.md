# Repository Agent Instructions

This repo is Dane/Sunny's public Hiatus/F-350 camper build source of truth. Keep maintenance practical and conservative.

## Canonical maintenance rules

- Use this repo itself as the planning source of truth; do not import private notes, email, work material, or raw photos unless explicitly approved.
- Prefer updating existing owner docs over creating new notes. Avoid document sprawl.
- Current high-level state belongs in `README.md`, `00 Home.md`, `docs/README.md`, and `docs/core/PROJECT.md`.
- Subsystem baseline belongs in `docs/core/SYSTEMS.md`; final `48V` topology belongs in `docs/core/ELECTRICAL_48V_ARCHITECTURE.md`.
- Implementation details belong in `docs/implementation/`; active sequence/procurement aids belong in `docs/plans/`; dated evidence belongs in `logs/LOG.md`.
- Historical plans may remain for provenance, but mark them clearly historical/reference-only rather than deleting context.

## Current posture to preserve

- Camper shell is installed/in hand; May 7 install-readiness planning is historical.
- Immediate build focus is finishing the proven live `48V` electrical board as a hard-mounted, strain-relieved mobile module.
- First live electrical checkpoint passed on `2026-05-27`: `55.5V` confirmed through the system including MultiPlus, inverter mode works, SmartShunt/Orion/Cerbo are online, and a short limited-current shore-charge test passed.
- Sustained/unattended charging remains gated on MultiPlus lithium-profile programming (`MK3-USB + VEConfigure` or equivalent). `DVCC` remains disabled unless a documented BMS/GX control path is added.
- Interior/furniture geometry is still measured-envelope/prototype work: no final extrusion cuts, permanent skins, final shell penetrations, or Lonseal glue-down until service/access gates pass.

## Verification before commit

- Run `git diff --check`.
- Scan changed text for secrets/private data and accidental public exposure.
- Check markdown sanity for changed files: balanced code fences, no malformed headings, no broken local links introduced.
- If changed docs have tracked PDF exports in `docs/pdf_exports/`, regenerate the affected PDFs/assets with `scripts/export-doc-pdfs.mjs` before commit.
- Review `git diff --stat` and enough context to catch stale-date replacements, duplicated sections, or historical text accidentally reactivated as current guidance.
