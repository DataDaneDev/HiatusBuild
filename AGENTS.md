# Repository Agent Instructions

This repo is Dane/Sunny's public Hiatus/F-350 camper build source of truth. Keep maintenance practical and conservative.

## Canonical maintenance rules

- Use this repo itself as the planning source of truth; do not import private notes, email, work material, or raw photos unless explicitly approved.
- Prefer updating existing owner docs over creating new notes. Avoid document sprawl.
- Current high-level state belongs in `README.md`, `00 Home.md`, `docs/README.md`, and `docs/core/PROJECT.md`.
- Subsystem baseline belongs in `docs/core/SYSTEMS.md`; final `48V` topology belongs in `docs/core/ELECTRICAL_48V_ARCHITECTURE.md`.
- Implementation details belong in `docs/implementation/`; active sequence/procurement aids belong in `docs/plans/`; dated evidence belongs in `logs/LOG.md`.
- `docs/plans/LIVE_BUILD_CHECKLIST.md` is the live running build checklist. Whenever the practical build state, sequence, blockers, completed physical work, or next shop action changes, update that checklist in the same maintenance pass instead of leaving the change only in chat.
- Historical plans may remain for provenance, but mark them clearly historical/reference-only rather than deleting context.

## Current posture to preserve

- Camper shell is installed/in hand; May 7 install-readiness planning is historical.
- Immediate build focus is the labeled removable switch/service face and branch closeout, followed by weather-window solar proof, coupled diesel-heater/storage layout, sink/drain/walnut geometry, alternator commissioning, travel restraint, and final skins.
- First live electrical checkpoint passed on `2026-05-27`: `55.5V` confirmed through the system including MultiPlus, inverter mode works, SmartShunt/Orion/Cerbo are online, and a short limited-current shore-charge test passed.
- MultiPlus lithium-profile programming has been owner-verified with MK3/VEConfigure-equivalent settings and a supervised one-battery shore-charge behavior check: bulk began, then quickly transitioned to absorption at/near 100% as planned. `DVCC` remains disabled unless a documented BMS/GX control path is added; AC-out/GFCI and alternator commissioning remain separate gates.
- The permanent floor and main electrical/Galley/Bench structure are installed. Starlink direct DC and its pass-through/retractile work; fridge/pump are wired/switched; DC charging and AC device branches are physically installed but retain acceptance tests. Interior cuts/skins remain measured-envelope work; no final closure or new penetration before its service, safety, motion, leak, or restraint gate passes.

## Verification before commit

- Run `git diff --check`.
- Run `python3 scripts/validate-bom.py` whenever `bom/bom_estimated_items.csv` or `bom/bom_inactive_items.csv` changes; row IDs are globally stable across both files.
- Scan changed text for secrets/private data and accidental public exposure.
- This repo is public: do not commit invoices, raw account-order pages, order IDs, account-scoped URLs, addresses, or payment data. Sanitized purchase facts such as item, date, quantity, price, and ASIN are allowed when useful to the build.
- Check markdown sanity for changed files: balanced code fences, no malformed headings, no broken local links introduced.
- If changed docs have tracked PDF exports in `docs/pdf_exports/`, regenerate the affected PDFs/assets with `scripts/export-doc-pdfs.mjs` before commit.
- Review `git diff --stat` and enough context to catch stale-date replacements, duplicated sections, or historical text accidentally reactivated as current guidance.
