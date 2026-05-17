# HiatusBuild Pre-Install Full Repo Audit — Archived Work Log

> **Archive note — 2026-05-17 03:17 MDT:** This file preserves the live audit ledger written on 2026-05-16. The findings below were subsequently triaged with Dane, resolved where appropriate in the canonical repo, verified, and pushed in commit `37febd2` (`Resolve preinstall audit triage items`). The individual finding entries intentionally remain in their original audit wording/status so the historical reasoning chain is preserved.

## 1) Header

- **Audit scope:** Full live-written pre-install audit of `/home/sunny/HiatusBuild`: markdown docs, BOM CSVs, diagram/media README docs, and git state. Scope includes canonical baseline map, deep electrical audit, cross-domain layout/plumbing/flooring/install sequencing audit, stale phrase/contradiction searches, and standardization review.
- **Started:** 2026-05-16 11:45:30 MDT (America/Denver)
- **Latest resumed pass:** 2026-05-16 18:49:00 MDT (America/Denver)
- **Archived:** 2026-05-17 03:17 MDT (America/Denver)
- **Repository:** `/home/sunny/HiatusBuild`
- **Branch:** `main`
- **Commit at start:** `b25f86efd9c8a76af3ea11a77aed51ab596557b5`
- **Resolution commit:** `37febd2` (`Resolve preinstall audit triage items`)
- **Pre-edit git state:** clean; `git pull --ff-only` returned `Already up to date.`
- **Original artifact policy:** The live audit pass intended this file as the only artifact and made no canonical edits, commits, or pushes during that pass. It is now archived after the follow-up triage/edit pass resolved the accepted findings in canonical docs/BOMs/PDF exports.
- **Public repo boundary:** Do not record secrets, credentials, private/company material, raw photos, or unredacted sensitive values.
- **Electrical safety note:** Electrical conclusions in this audit are planning recommendations only until verified against actual device manuals, labels, applicable code/listing requirements, and physical measurements.

## 2) Running cursor/checkpoint

- **Current pass status:** completed for 2026-05-16 18:49 MDT continuation pass; new findings F-016 through F-018 were appended and F-015 was refined in the live artifact only.
- **Last reviewed file/section/search query:** DC architecture/BMS/busbar/disconnect batch: `docs/core/ELECTRICAL_48V_ARCHITECTURE.md` locked component set and power path, plus `BMS|CAN|parallel|Class T|disconnect|SmartShunt|busbar|pre-charge` search. Stopped after refining F-015 because the active 48V architecture core doc also maps Class T battery branch protection to row `105`.
- **Review queue remaining:**
  - Deep electrical continuation: continue DC architecture/BMS assumptions, charge-source enable order, and charge-profile/fuse/wire item alignment.
  - Optional future pass: exhaustive classification of all 319+ stale phrase hits if Dane wants a cleanup sprint rather than this audit ledger.
- **Next planned step:** Continue in `ELECTRICAL_48V_ARCHITECTURE.md` around one-battery-trip behavior, vendor gates, and `TRACKING.md` risk/open-question parity.

## 3) Executive status

**Original live-audit executive status, preserved for archive context.** Eighteen issues found so far. Highest current safety/readiness concerns are F-010, F-013, and F-014: the core project doc contradicts the purchased single AC enclosure baseline, the active bench guide lacks explicit AC neutral/ground pre-energization gates, and WS500 low-current fuse documentation appears to treat a `48V` battery-sense lead as generic ATC/ATO without an explicit `>=58VDC` voltage-class/listing gate. Highest direct build-blocker concern remains F-006: BOM wire inventory/description appears inconsistent with active topology rollups, including a possible `2/0` red shortfall before waste. This pass also added F-016 through F-018: the AC BOM purchased-SKU lock accidentally includes unrelated tire-deflator row `181`, AC strain-relief/cable-entry readiness is mapped to generic/blank hardware rows without an explicit fit gate, and the active PV topology still presents `900W 3S3P` as if it were the selected implementation even though final solar module/string lock is deferred. Other concerns: `SYSTEMS.md` date drift, stale logistics/tracking, stale AC open questions, obsolete BOM row `111` in the install plan, inconsistent per-battery design-current values, stale active interior storage wording, temp/study stale AC status, ambiguous core shore-passthrough status, Class T spare mapping, and tracked root `.tmp_test` artifacts.

## 4) Findings ledger

### F-001 — active tracking layer still carries pre-May-7 shell-install logistics as open

- **Timestamp:** 2026-05-16 11:58 MDT
- **Subsystem:** project tracking / install sequencing / standardization
- **Severity:** standardization
- **Evidence/citation:**
  - `docs/core/PROJECT.md` lines 22-25: snapshot says `As-of date: 2026-05-14`, `Phase: post-install interior buildout and measured systems-layout validation`, and `May 7, 2026 Hiatus install is now historical context; the real camper shell is available for physical mockups and measurements`.
  - `docs/core/TRACKING.md` lines 593-597 still lists active open questions: `Confirm Tuesday/Wednesday Washington travel/staging details, route/weather, and arrival buffer before the May 7 9:00 AM install`, `Confirm with Hiatus whether tailgate can be removed onsite...`, `Confirm tonneau cover removal timing...`, and `Verify the re-bonded bed rail caps ... do not interfere with the Hiatus attachment/seal interface`.
  - `docs/core/TRACKING.md` lines 530-537 also keeps R-012 open: `Travel/logistics compression could put the truck too far from Bellingham for the May 7 9:00 AM install`.
- **Why it matters before install:** If this audit is used as a pre-interior-install readiness tool, stale shell-install logistics can obscure current gates: post-install inspection evidence, floor closeout, measured envelopes, and electrical first-charge. Keeping completed trip logistics open also weakens trust in the risk/open-question register as the install checklist source.
- **Recommended change:** In a later approved edit pass, mark R-012 and the May 7 travel/tailgate/tonneau/Hiatus-interface questions as closed/historical if install evidence confirms completion; replace them with any still-current post-install inspection gates, such as tailgate storage outcome, rail-cap/seal inspection result, or camper attachment observations.
- **Proposed update target(s):** `docs/core/TRACKING.md` risk register R-012 and open questions section; optionally `logs/LOG.md` if the install/travel outcome evidence is missing from dated logs.
- **Verification needed:** Confirm from `logs/LOG.md` or Dane-provided facts whether May 7 install occurred as expected, whether tailgate/tonneau handling is resolved, and whether any bed-rail interference/seal follow-up remains current.
- **Status:** proposed

### F-002 — AC open questions still reference superseded split-DIN/receptacle-count scope after D-044 purchase lock

- **Timestamp:** 2026-05-16 12:04 MDT
- **Subsystem:** electrical AC / tracking / procurement alignment
- **Severity:** medium
- **Evidence/citation:**
  - `docs/core/TRACKING.md` lines 421-428 records D-044: Phase 1 AC was locked/purchased as portable EMS plus one combined `6-way` DIN enclosure with `30A` AC-in, `30A` AC-out main, `2x 20A` GFCI branches; row `111` is obsolete and row `112` remains confirm-on-hand for boxes/covers.
  - `logs/LOG.md` lines 24-31 repeats the May 16 AC purchase lock and states the remaining AC issues are outlet boxes/covers, delivered wire jacket markings/listing, and DIN neutral isolation.
  - `docs/core/TRACKING.md` lines 618-619 still lists `Final AC receptacle count and distribution target (3 vs 4 locations; target 6 vs 8 practical plug points)` and `Verify physical fitment and service-access clearances for the split-DIN AC hardware set (rows 13, 15, 107, 108, 109, 110, 111, 112, 113, 114, 123) during cabinet mockup`.
- **Why it matters before install:** The active open-question list can send the builder back into a superseded AC design branch: split enclosures, obsolete downstream non-GFCI row `111`, and broad receptacle-count churn. That directly conflicts with the intended install gate of compact single-enclosure AC-in-first charging and could cause unnecessary cabinet holes, enclosure buys, or branch wiring changes.
- **Recommended change:** Replace the stale open questions with D-044-specific checks: confirm outlet box/covers row `112`, inspect delivered wire jacket/listings, dry-fit the single `6-way` DIN enclosure, confirm neutral isolation/bus arrangement, label AC-in vs AC-out inside the shared enclosure, and perform AC-in-only MultiPlus validation before AC-out branches.
- **Proposed update target(s):** `docs/core/TRACKING.md` open questions; optionally R-011 wording if it still implies broad branch-count uncertainty rather than monitoring against added third branch; `docs/implementation/ELECTRICAL_AC_BOM.md` and bench guide should be checked later for consistency.
- **Verification needed:** Confirm BOM row `111` is obsolete, row `112` status is still planned/confirm-on-hand, and no implementation doc still instructs split DIN enclosures as the active build path.
- **Status:** proposed

### F-003 — historical install plan's current AC-in section still lists obsolete BOM row `111` as deferrable hardware

- **Timestamp:** 2026-05-16 12:11 MDT
- **Subsystem:** electrical AC / BOM-row traceability / historical-plan caveat
- **Severity:** low
- **Evidence/citation:**
  - `docs/plans/INSTALL_MINUS_12_READINESS_PLAN.md` lines 109-149 presents a current `Shore power / initial charge plan` with the purchased single-enclosure AC architecture and rows locked on 2026-05-16.
  - Same file lines 151-155 says `Can still defer during first live charge... BOM 15, 111, 112: GFCI/downstream receptacles and boxes`.
  - `docs/core/TRACKING.md` D-044 lines 421-428 and `logs/LOG.md` lines 24-31 say row `111` downstream non-GFCI receptacles is obsolete, while row `112` remains planned/confirm-on-hand.
- **Why it matters before install:** Even in a reference plan, the AC-in-first section reads current and action-oriented. Listing obsolete row `111` as merely deferrable can accidentally reintroduce downstream non-GFCI receptacles or confuse the remaining purchase check, when the actual unresolved item is outlet boxes/covers plus delivered-hardware inspection.
- **Recommended change:** In a later approved edit pass, change the deferrable line to omit row `111` or explicitly state `row 111 obsolete; row 112 boxes/covers confirm-on-hand`; keep GFCI row `15` only as purchased-but-not-needed for AC-in-only first charge.
- **Proposed update target(s):** `docs/plans/INSTALL_MINUS_12_READINESS_PLAN.md` `Shore power / initial charge plan`, `Can still defer` list; optionally cross-check `docs/implementation/ELECTRICAL_AC_BOM.md` for the same row status.
- **Verification needed:** Confirm current BOM row statuses for `15`, `111`, and `112` before editing.
- **Status:** proposed

### F-004 — electrical topology worksheet has inconsistent per-battery design-current values (`82.5A` vs `77.5A`)

- **Timestamp:** 2026-05-16 12:21 MDT
- **Subsystem:** electrical DC / battery fuse-wire calculation
- **Severity:** medium
- **Evidence/citation:**
  - `docs/implementation/ELECTRICAL_overview_diagram.md` lines 46-55 states the current envelope is `I_total = F-02 + F-05 = 125A + 40A = 165A`, then calculates `I_batt_design = (165A / 3) * 1.5 = 82.5A` and `I_fuse_min = 103.1A`.
  - Same file lines 391-398, in the voltage-drop worksheet, lists `C-01`, `C-02`, `C-02C`, and `C-03` current basis as `77.5A` per battery/branch.
- **Why it matters before install:** This is the active implementation topology used for conductor, fuse, and cut-list validation. A stale current basis in the worksheet weakens confidence in the calculation chain immediately before battery paralleling and high-current cable fabrication. The selected `2/0` / `200A Class T` posture may still be conservative, but the doc should not carry two different design currents for the same battery branches.
- **Recommended change:** Recalculate the worksheet rows from the active formula and make the current basis consistent. If `82.5A` is the active design value, update the affected worksheet rows and voltage-drop values; if a different current envelope is intended, update the calculation block and explain the basis.
- **Proposed update target(s):** `docs/implementation/ELECTRICAL_overview_diagram.md` `Battery Fuse/Wire Recalculation Basis` and `Wiring Validation Worksheet`; cross-check `docs/studies/ELECTRICAL_battery_fuse_wire_recalc_2026-02-18.md` for the origin of `77.5A`.
- **Verification needed:** Re-run voltage-drop/current-basis math after confirming active fuse set and whether solar/alternator/Orion concurrent charging is included in the battery branch sizing envelope. Electrical safety remains planning-only until verified against actual manuals, labels, code/listing requirements, and physical measurements.
- **Status:** proposed

### F-005 — active interior storage section still uses superseded `top-right soft cubes` language

- **Timestamp:** 2026-05-16 12:29 MDT
- **Subsystem:** interior layout / stale phrase / storage zoning
- **Severity:** low
- **Evidence/citation:**
  - `docs/implementation/INTERIOR_furniture_layout_and_galley.md` lines 217-219 says `The old top-right soft-storage idea is superseded` and the passenger side now carries the lofted fridge/wet-spine/water-tank cluster plus adjacent separated battery bench.
  - Same active implementation file line 452, under `Frequent but not constant` storage, still says `Top-right soft cubes: clothes, towel, toiletries, bedding`.
  - Stale-phrase search query `rear-left|rear left|driver-side fridge|top-right|top left|top-left|15-series|split-DIN|3 vs 4|row 111|Sterling|BB1248120` found this hit during the interior/stale-phrase pass.
- **Why it matters before install:** The active layout is space-constrained around the passenger-side lofted fridge, wet-spine, tank, pump, and battery bench. A lingering `top-right soft cubes` storage instruction can make future mockups allocate soft storage into a zone now owned by systems access, ventilation, wet/dry separation, and service panels.
- **Recommended change:** Replace the active storage bullet with current terminology, e.g. `soft storage in verified light/upper zones only after fridge/wet-spine and roof-sweep clearances pass`, or move the old `top-right` phrasing into a historical caveat.
- **Proposed update target(s):** `docs/implementation/INTERIOR_furniture_layout_and_galley.md` section `## 11) Storage system by access frequency`; optionally `media/diagrams/interior-furniture-2026-05-04/README.md` if it still describes the top-right soft-storage concept without an explicit caveat.
- **Verification needed:** After editing, re-run stale phrase search for `top-right`, `top right`, and `rear-left` and classify remaining hits as historical-ok or media-reference-ok.
- **Status:** proposed

### F-006 — BOM wire inventory/description does not match active electrical topology rollups

- **Timestamp:** 2026-05-16 12:38 MDT
- **Subsystem:** electrical DC / BOM alignment / wire procurement
- **Severity:** high
- **Evidence/citation:**
  - `docs/implementation/ELECTRICAL_overview_diagram.md` lines 439-453 roll up active no-padding wire needs as `2/0 AWG red = 42.5 ft`, `2/0 AWG black = 35.0 ft`, `14 AWG duplex = 52 ft`, and `18/2 = 26.5 ft`.
  - `bom/bom_estimated_items.csv` row `28` line 28 says the purchased TEMCo `2/0` set gives `35 ft red + 35 ft black total` and `covers the active 2/0 baseline requirement ... with spare margin`. Against the topology rollup, red appears short by `7.5 ft` before waste/termination margin unless there is additional unrecorded red `2/0` stock.
  - `bom/bom_estimated_items.csv` row `32` line 32 says `14 AWG duplex baseline (no padding): 44 ft total` for `C-20/C-21/C-22/C-23/C-35`, omitting `C-36` that the topology rollup includes.
  - `bom/bom_estimated_items.csv` row `33` line 33 says `18/2 baseline usage (no padding): 18.5 ft total` for `C-24/C-25/C-26`, omitting `C-37` that the topology rollup includes.
- **Why it matters before install:** Wire stock is a direct build blocker. A false `covers baseline with spare margin` note can lead to cutting cables before realizing the red `2/0` run budget is short, especially with the dedicated alternator path included. The smaller-wire rollup mismatch can also hide missing Maxxair/ambient-lighting branch allowances during rough-in.
- **Recommended change:** Reconcile BOM rows `28`, `32`, and `33` against the active topology rollup. Explicitly separate purchased/on-hand stock from required no-padding baseline and planned checkout overage. If additional unrecorded `2/0` red exists, record it; if not, flag a top-off buy before final cable cuts.
- **Proposed update target(s):** `bom/bom_estimated_items.csv` rows `28`, `32`, `33`; `docs/implementation/ELECTRICAL_overview_diagram.md` wire rollup if the active circuit list changes; `docs/core/TRACKING.md` if this becomes a procurement risk.
- **Verification needed:** Physically inventory actual red/black `2/0`, `14 AWG duplex`, and `18/2` stock; confirm whether `C-36`/`C-37` are owner-installed or Hiatus preinstalled/optional before counting them in the purchase baseline; re-run wire rollup after measured route lengths replace assumptions.
- **Status:** proposed

### F-007 — temporary procurement red flags still carry pre-D-044 AC procurement blockers as open

- **Timestamp:** 2026-05-16 12:46 MDT
- **Subsystem:** procurement tracking / temp-doc boundary / AC standardization
- **Severity:** standardization
- **Evidence/citation:**
  - `docs/temp/TEMP_procurement_red_flags.md` lines 32-66 keeps PRF-003 open, including `Final receptacle-count closure (3 vs 4 locations)` and old resolution progress of `20A galley + 15A office` and `4 total 120V receptacle locations`.
  - Same file lines 82-97 keeps PRF-005 open, saying shore/AC component SKU lock and physical fitment validation are still pending across rows `13`, `14`, `15`, `107-114`.
  - Current AC purchase lock is recorded in `docs/core/TRACKING.md` D-044 lines 421-428, `docs/implementation/ELECTRICAL_AC_BOM.md` lines 26-47 and 141-146, and `bom/bom_estimated_items.csv` rows `13-15`, `107-114`, `123`, `179-180`.
- **Why it matters before install:** `docs/temp/` is non-canonical, but stale open red flags can still mislead a review into thinking AC SKU lock and receptacle count are unresolved, contradicting the active purchased two-GFCI/single-enclosure baseline. That undermines the repo's own rule that temp files must not silently override core/implementation owners.
- **Recommended change:** In a later approved cleanup pass, mark PRF-003/PRF-005 as closed or superseded by D-044, and point any remaining real gaps to the current owner docs: outlet boxes/covers row `112`, delivered wire jacket/listing check, enclosure fit/neutral isolation, and AC-in-only first-charge validation.
- **Proposed update target(s):** `docs/temp/TEMP_procurement_red_flags.md` PRF-003 and PRF-005; optionally `docs/README.md` temp-file rule if cleanup is deferred.
- **Verification needed:** Confirm no current docs still depend on TEMP procurement red flags for active AC work; verify row `112` and delivered hardware inspection remain the only AC procurement/fit gaps.
- **Status:** proposed

### F-008 — historical high-level health review has stale action-oriented AC focus without a post-D-044 caveat

- **Timestamp:** 2026-05-16 12:54 MDT
- **Subsystem:** studies boundary / reader routing / AC status
- **Severity:** low
- **Evidence/citation:**
  - `docs/studies/PROJECT_high_level_health_review_2026-03-15.md` front matter line 7 marks the file `status: historical`, but the body remains action-oriented: lines 43-47 say `AC scope is partially reopened`, `shore-power chain still needs final component/SKU lock`, and outlet count is pending (`3-4` receptacle locations).
  - Same file lines 66-68 says `Finalize AC scope in one pass: exact shore chain, branch count, and receptacle count with SKU-level lock`.
  - Current baseline evidence later supersedes this: `docs/core/TRACKING.md` D-044 lines 421-428 and `logs/LOG.md` lines 24-31 record the May 16 AC purchase lock and row `111` obsolescence.
- **Why it matters before install:** The file is marked historical, so preserving its content is acceptable. The risk is that it is a high-level health review with `Suggested near-term focus` phrasing and no top caveat pointing readers to D-044/current AC implementation. A quick reader could treat March AC churn as still current and reopen already-purchased shore/branch decisions.
- **Recommended change:** Add a short maintenance caveat near the top: this March health review is historical; AC procurement/scope sections were superseded by D-044 and current AC owner docs; keep only as a snapshot of March risk posture.
- **Proposed update target(s):** `docs/studies/PROJECT_high_level_health_review_2026-03-15.md` top status block or immediately under title; optionally add to stale-phrase ledger as historical-needs-caveat.
- **Verification needed:** Confirm D-044 remains the final active AC purchase lock before adding caveat.
- **Status:** proposed

### F-009 — active project scope still says shore-power passthrough decision is pending after AC shore hardware lock

- **Timestamp:** 2026-05-16 13:00 MDT
- **Subsystem:** core project posture / shore power / passthrough routing
- **Severity:** medium
- **Evidence/citation:**
  - `docs/core/PROJECT.md` lines 63-66 says Phase 1 includes core plumbing/electrical, then states `Several passthrough decisions (solar, shore power, diesel/propane routing) are still pending and tracked in docs/core/TRACKING.md`.
  - Current AC evidence says shore-interface hardware is no longer generically pending: `logs/LOG.md` lines 25-31 records purchased portable `30A` EMS, `TT-30P` to `L5-30R` shore cord, `L5-30` inlet, single `6-way` DIN enclosure, `30A` AC-in breaker, and first-charge validation path; `docs/core/TRACKING.md` D-044 lines 421-428 records the same lock.
  - Remaining AC issues are narrower: `logs/LOG.md` line 30 lists outlet boxes/covers row `112`, delivered `10/3` jacket/listing, and DIN neutral isolation before drilling/wiring.
- **Why it matters before install:** `PROJECT.md` is an active high-level routing doc. Saying `shore power` passthrough is still pending can reopen topology/interface selection instead of focusing on the real install gates: selected inlet location, physical cut/strain relief, enclosure fit, neutral isolation, and AC-in-only first charge. Solar and diesel/propane routing may still be genuinely pending, so the mixed list blurs closed vs open scope.
- **Recommended change:** Replace the broad phrase with a split status: shore interface/hardware selected/purchased, but physical inlet placement/cut/strain relief and AC verification remain gated; solar and diesel/propane passthrough routes remain pending if still true.
- **Proposed update target(s):** `docs/core/PROJECT.md` `Scope clarifications from workbook`; optionally `docs/core/TRACKING.md` open questions if it still groups shore with unresolved passthrough decisions.
- **Verification needed:** Confirm final `L5-30` inlet placement has not been cut/locked yet; verify no current plan has already selected a physical wall passthrough location.
- **Status:** proposed

### F-010 — active project doc contradicts purchased AC baseline by saying AC-in and AC-out protection stay in separate enclosures

- **Timestamp:** 2026-05-16 13:06 MDT
- **Subsystem:** electrical AC / safety / core project posture
- **Severity:** high
- **Evidence/citation:**
  - `docs/core/PROJECT.md` line 89 describes the purchased Phase 1 AC baseline as `single 6-way AC DIN enclosure -> 30A AC-in breaker/disconnect -> MultiPlus AC-in`, with `30A` AC-out main plus two `20A` GFCI branches.
  - Immediately after, `docs/core/PROJECT.md` line 90 says: `Keep AC-in and AC-out protection in separate enclosures. Do not let final AC receptacle-count churn block the AC-in charge path.`
  - Current implementation docs use the single-enclosure design, not separate enclosures: `docs/implementation/ELECTRICAL_AC_BOM.md` lines 18 and 75-82, `docs/implementation/ELECTRICAL_overview_diagram.md` lines 267-281 and 500-504, and `logs/LOG.md` lines 25-31.
- **Why it matters before install:** This is an active safety/topology contradiction in a core doc. A builder following `PROJECT.md` could either buy/build split AC enclosures contrary to purchased hardware or ignore the line and miss the real safety rule: AC-in and AC-out may share one physical enclosure only if neutral paths are isolated, PE/ground is handled correctly, labeling is clear, and physical barriers/strain relief/listings are validated. Incorrect neutral mixing or enclosure layout can create shock/GFCI/transfer-relay hazards.
- **Recommended change:** Replace the separate-enclosures sentence with the current rule: AC-in and AC-out protection may share the purchased `6-way` enclosure only with isolated neutral paths, common PE/ground handled per manual/listing, clear labels/barriers as applicable, and no fixed downstream neutral-ground bond; AC-in-only charge path remains the first live validation.
- **Proposed update target(s):** `docs/core/PROJECT.md` immediate electrical priority bullets; cross-check `docs/core/TRACKING.md` open questions and `docs/plans/INSTALL_MINUS_12_READINESS_PLAN.md` for any remaining split/separate enclosure language.
- **Verification needed:** Inspect the delivered DIN enclosure/bus hardware and MultiPlus manual before wiring; verify neutral isolation physically with continuity checks before energizing.
- **Status:** proposed

### F-011 — tracked root-level `.tmp_test` export artifacts violate repo boundary/standardization expectations

- **Timestamp:** 2026-05-16 13:13 MDT
- **Subsystem:** repo hygiene / generated artifacts / standardization
- **Severity:** standardization
- **Evidence/citation:**
  - Media/reference inventory found tracked root files `.tmp_test.mmd` and `.tmp_test.pdf` (`git ls-files .tmp_test.pdf .tmp_test.mmd` returns both files).
  - Expected generated PDF/Mermaid assets otherwise live under `docs/pdf_exports/` and `docs/pdf_exports/assets/...`; media README docs and routing docs do not present root-level `.tmp_test.*` as canonical build artifacts.
- **Why it matters before install:** Root-level temp artifacts create reader-routing noise and can be mistaken for a current diagram/export test, especially in a public repo. They also weaken the repo's standard of keeping generated/reference artifacts in named folders with README context.
- **Recommended change:** In a later approved cleanup pass, inspect the files for any unique content. If they are only export smoke-test leftovers, remove them from the tracked repo; if they contain useful export diagnostics, move/rename them under an appropriate generated-assets folder with context.
- **Proposed update target(s):** `.tmp_test.mmd`, `.tmp_test.pdf`; possibly `.gitignore` if future export smoke tests should not be tracked.
- **Verification needed:** Before deletion, compare `.tmp_test.*` against current `docs/pdf_exports/assets/*` outputs and confirm no unique/current diagram content is lost.
- **Status:** proposed

### F-012 — `SYSTEMS.md` snapshot date predates embedded May 16 AC purchase-lock state

- **Timestamp:** 2026-05-16 14:37 MDT
- **Subsystem:** core systems baseline / electrical AC / standardization
- **Severity:** standardization
- **Evidence/citation:**
  - `docs/core/SYSTEMS.md` line 37 labels the electrical planning snapshot `as-of 2026-05-14`.
  - Same snapshot line 43 says the AC protection chain is `now purchased/locked for Phase 1` and describes the May 16 single-enclosure AC baseline: portable EMS/shore cord/`L5-30` inlet, single `6-way` DIN enclosure, `30A` AC-in, `30A` AC-out main, and two `20A` GFCI branches.
  - Dated lock evidence is later than the snapshot date: `logs/LOG.md` lines 24-31 and `docs/implementation/ELECTRICAL_AC_BOM.md` lines 16-18 record the AC purchase lock on/as-of `2026-05-16`.
- **Why it matters before install:** `SYSTEMS.md` is an active core baseline and reader-routing target. A stale as-of label attached to newer purchased-hardware state makes it harder to tell whether the charge-profile warning, shore topology, and AC safety gates are current or partially backfilled. In a pre-install build window, date drift can cause reviewers to distrust the snapshot or miss that D-044/D-045-era AC state already superseded May 14 assumptions.
- **Recommended change:** In a later approved edit pass, either update the planning snapshot as-of date to `2026-05-16` after checking the whole section for May 16 parity, or split the AC purchase-lock sentence into a dated May 16 update note while keeping the rest of the May 14 modeling snapshot intact. Do not merely change the date if charge-profile, alternator, solar, or load-model values still reflect older assumptions.
- **Proposed update target(s):** `docs/core/SYSTEMS.md` `### Planning snapshot` and AC/shore charging bullets; optionally `docs/README.md` if the core baseline/date convention needs a one-line maintenance rule.
- **Verification needed:** Cross-check `SYSTEMS.md` against `docs/core/TRACKING.md` D-044, `docs/implementation/ELECTRICAL_AC_BOM.md`, `bom/load_model_wh.csv`, and `bom/bom_estimated_items.csv` before changing the date.
- **Status:** proposed

### F-013 — bench first-charge/AC validation ladder lacks explicit neutral-ground/GFCI pre-energization gates

- **Timestamp:** 2026-05-16 14:39 MDT
- **Subsystem:** electrical AC / bench commissioning / safety gate
- **Severity:** high
- **Evidence/citation:**
  - `docs/implementation/ELECTRICAL_bench_layout_and_test_guide.md` lines 162-169 defines the `T2.5` shore/MultiPlus initial charge validation steps, but only calls out AC-in path order, AC-out loads disconnected, battery/profile/current-limit, pre-charge, alternator inactive, and logging.
  - Same file lines 181-186 defines `T4` AC path validation as staged known-load testing plus branch protection/outlet polarity/GFCI behavior, but does not require a dead-meter verification of isolated AC-in/AC-out neutrals, no fixed downstream neutral-ground bond, continuous PE/equipment grounding, or chassis-bond intent before energization.
  - The current AC owner doc does require these checks: `docs/implementation/ELECTRICAL_AC_BOM.md` lines 38-43 and 114-119 state isolated AC-in/AC-out neutrals, common PE bus not used as neutral, continuous equipment ground/chassis bond, and no always-bonded downstream N-G bond.
- **Why it matters before install:** The bench guide is the print/use commissioning ladder. If the operator follows it literally during the first AC-in-only charge or later AC-out test, the neutral/ground safety checks could be treated as background design knowledge rather than a stop/go pre-energization gate. In a shared single DIN enclosure, a missed neutral mix or unintended downstream N-G bond is a direct shock/GFCI/transfer-relay hazard.
- **Recommended change:** Add explicit AC dead checks to T0 and/or T2.5 before shore energization: continuity/megger-as-appropriate verification that AC-in and AC-out neutrals are isolated; PE/equipment ground is continuous through inlet, enclosure, MultiPlus, and receptacles; no fixed downstream N-G bond exists; GFCI devices are installed/tested only at the staged AC-out step; and any chassis bond follows the MultiPlus manual/listing plan. Cross-link the bench guide to `ELECTRICAL_AC_BOM.md` neutral/ground checklist.
- **Proposed update target(s):** `docs/implementation/ELECTRICAL_bench_layout_and_test_guide.md` sections `T0`, `T2.5`, and `T4`; optionally `docs/core/OPERATIONS.md` pre-energization checklist if it is missing the same AC dead checks.
- **Verification needed:** Confirm actual MultiPlus-II `120V` manual neutral-transfer/bonding requirements, delivered enclosure bus layout, and GFCI receptacle wiring before writing final procedural language.
- **Status:** proposed

### F-014 — WS500 `48V` battery-sense fuse path is mapped to generic ATC/ATO hardware without a voltage-class gate

- **Timestamp:** 2026-05-16 14:41 MDT
- **Subsystem:** electrical DC / alternator regulator sensing / fuse voltage class
- **Severity:** high
- **Evidence/citation:**
  - `docs/implementation/ELECTRICAL_fuse_schedule.md` line 79 lists `F-13` as the `WS500 battery positive sense lead`, fuse type `Inline ATC/ATO`, `3A`, with no voltage-class requirement.
  - `docs/implementation/ELECTRICAL_overview_diagram.md` line 380 defines `C-39` as `WS500 battery positive-sense lead -> WS500`, nominal voltage `48V` sense lead, protected by `F-13 3A`.
  - `bom/bom_estimated_items.csv` row `171` line 170 describes a `Sealed ATC/inline fuse holder set + fuse assortment` for WS500 wiring, including `battery positive sense (3A)`, but does not distinguish `12V`-origin regulator power from the `48V` battery-sense circuit or require a `58V/80V`-class holder/fuse.
- **Why it matters before install:** Standard automotive ATC/ATO fuse holders and blade fuses are often `32V` class. That is acceptable for `12V` control wiring, but potentially under-rated on a `51.2V` nominal / `58.4V` charge-voltage LiFePO4 bank sense lead unless the specific Wakespeed harness/holder/fuse is rated for the actual circuit voltage. Low current does not eliminate DC arc/interrupt rating requirements.
- **Recommended change:** Split WS500 low-current fuse requirements by actual circuit voltage. Keep `F-12`/`F-15` as `12V`-origin control/power paths if confirmed, but mark `F-13` battery-positive sense as requiring a fuse/holder rated for the `48V` bank maximum voltage, or explicitly cite a Wakespeed-provided harness/holder rating that covers the circuit. Update BOM row `171` so it does not imply generic ATC hardware is sufficient for all WS500 fuses.
- **Proposed update target(s):** `docs/implementation/ELECTRICAL_fuse_schedule.md` `Required Fuse Map` and `BOM Row Mapping`; `bom/bom_estimated_items.csv` row `171`; optionally `docs/implementation/ELECTRICAL_overview_diagram.md` C-39 note and `docs/core/ELECTRICAL_48V_ARCHITECTURE.md` vendor-gate list.
- **Verification needed:** Check WS500 manual/kit harness specifications for battery-sense lead fuse and holder voltage ratings, and confirm whether `F-14` current-sense protection is on a `48V`-referenced lead or isolated low-voltage signal before procurement/wiring.
- **Status:** proposed

### F-015 — Class T spare-fuse tracking points to row `105`, but row `105` is a `100A 32V` ANL spare set for F-11

- **Timestamp:** 2026-05-16 14:43 MDT
- **Subsystem:** electrical DC / fuse spare inventory / BOM alignment
- **Severity:** medium
- **Evidence/citation:**
  - `bom/bom_estimated_items.csv` row `7` line 7 says the Class T purchase includes `JLLN-200 200A spare fuse x1` and that `Additional Class T spare top-off (x2) is tracked in row 105`.
  - `bom/bom_estimated_items.csv` row `105` line 104 is not Class T; it is `BOJACK 100A 32VDC ANL blade fuse pack (3-count) reserved as F-11 spare set x3`.
  - `docs/implementation/ELECTRICAL_fuse_schedule.md` lines 89-98 expects Class T `200A` installed qty `3`, spare qty `3`, while the BOM evidence only accounts for one Class T spare in row `7` unless another row exists.
  - `docs/core/ELECTRICAL_48V_ARCHITECTURE.md` line 50 repeats the same bad Class T mapping by listing `F-01A/B/C` battery branch protection BOM rows as `7`, `105`.
- **Why it matters before install:** This is not a primary energization blocker, but it is a misleading procurement/readiness signal for the most critical battery-source fuses. A reviewer could believe the `3x` Class T spare policy is satisfied when the referenced row is actually a `12V` buffer-battery ANL spare pack with insufficient voltage class for the `48V` Class T battery protection role.
- **Recommended change:** Correct row `7` to remove the row `105` Class T top-off reference unless a real Class T spare purchase row exists; add or update a proper Class T spare row for the missing `x2` JLLN-200 spares if the one-spare-per-installed-fuse policy remains active. Keep row `105` scoped only to `F-11` 12V buffer battery spares.
- **Proposed update target(s):** `bom/bom_estimated_items.csv` rows `7` and `105`; `docs/core/ELECTRICAL_48V_ARCHITECTURE.md` locked component set; `docs/implementation/ELECTRICAL_fuse_schedule.md` `Spare Fuse Inventory` and `BOM Row Mapping` if the spare policy changes.
- **Verification needed:** Physically inventory actual Class T spare count and exact fuse type/voltage rating; confirm whether one-spare-per-installed battery fuse is still required for pre-install travel or can be relaxed.
- **Status:** proposed

### F-016 — AC BOM purchased-SKU lock includes unrelated tire-deflator row `181`

- **Timestamp:** 2026-05-16 18:49 MDT
- **Subsystem:** electrical AC / BOM row traceability / standardization
- **Severity:** low
- **Evidence/citation:**
  - `docs/implementation/ELECTRICAL_AC_BOM.md` line 144 says the purchased AC SKU lock is recorded in BOM rows `13`, `14`, `15`, `41`, `107`, `108`, `109`, `110`, `113`, `114`, `123`, `179`, `180`, and `181`.
  - `bom/bom_estimated_items.csv` row `181` line 180 is `Rhino USA rapid tire deflators with gauge`, explicitly described as a vehicle/off-road support item `unrelated to AC system but included in the same purchase wave`.
  - The actual AC-related purchase rows in the same batch are rows `107-114`, `123`, `179`, and `180`, with row `112` still planned/confirm-on-hand for outlet boxes/covers.
- **Why it matters before install:** This is not a wiring safety defect by itself, but it weakens row-level traceability in the active AC owner doc. A later AC procurement check could chase row `181` as if it were an AC component or miss that row `112` is still the real physical outlet-box gap.
- **Recommended change:** Remove row `181` from the AC purchased-SKU lock list and, if helpful, add a parenthetical that row `181` was only same-order vehicle support hardware and is intentionally excluded from AC scope. Keep row `112` visible as planned/confirm-on-hand rather than purchased.
- **Proposed update target(s):** `docs/implementation/ELECTRICAL_AC_BOM.md` `Procurement Notes`; optionally `bom/bom_estimated_items.csv` only if row `181` description needs clearer non-AC wording.
- **Verification needed:** Confirm there is no AC accessory hidden in the tire-deflator purchase line and that row `112` remains the only unresolved GFCI box/cover procurement row.
- **Status:** proposed

### F-017 — AC strain-relief/cable-entry readiness is mapped to generic blank hardware rows without a cable-OD/enclosure-fit gate

- **Timestamp:** 2026-05-16 18:51 MDT
- **Subsystem:** electrical AC / shore inlet and enclosure penetrations / procurement readiness
- **Severity:** medium
- **Evidence/citation:**
  - `docs/implementation/ELECTRICAL_AC_BOM.md` lines 80-88 lists outlet boxes/covers row `112`, `10/3`/branch-cable strain relief row `44`, grommets row `43`, P-clamps row `45`, and related loom/heat-shrink/ferrule rows as required AC install hardware.
  - `bom/bom_estimated_items.csv` row `43` line 43 is `Rubber Grommets` with a blank description and `planned` status; row `44` line 44 is `Strain relief/cable glands` with a blank description and `Purchased` status; row `45` line 45 is `P-clamps` with a blank description and `Purchased` status.
  - `docs/plans/INSTALL_MINUS_12_READINESS_PLAN.md` line 149 separately says to confirm enough rows `43-45`, `38`, `41`, and terminals/labels for strain relief, grommets, P-clamps, heat shrink, ferrules, and enclosure entries.
  - `logs/LOG.md` line 30 only calls out delivered `10/3` jacket markings/listing and DIN neutral isolation, not a stop/go check that the cable glands/clamps physically fit the delivered `10/3`, `12/3`, inlet, enclosure knockouts, and outlet boxes.
- **Why it matters before install:** AC cable entries are a safety and durability item, not a generic consumable. A purchased-but-blank strain-relief row can falsely imply readiness even if the glands are the wrong trade size, wrong cable OD range, not suitable for the enclosure/inlet wall thickness, or not listed/appropriate for the AC cable jacket and environment. Bad strain relief can leave conductors carrying vibration load or expose abrasion at the shore inlet/enclosure.
- **Recommended change:** Add an explicit AC cable-entry fit gate: measure delivered `10/3` and `12/3` cable ODs; verify selected glands/clamps/grommets fit the DIN enclosure/inlet/outlet box knockouts and wall thickness; record gland size/range and listing/environment basis in the BOM or AC BOM; keep row `44` purchased only as generic stock until exact fit is confirmed. Tie row `112` box selection to compatible clamps/covers.
- **Proposed update target(s):** `docs/implementation/ELECTRICAL_AC_BOM.md` required components and manual validation checklist; `bom/bom_estimated_items.csv` rows `43-45` and `112`; optionally `docs/plans/INSTALL_MINUS_12_READINESS_PLAN.md` AC first-charge accessory checklist.
- **Verification needed:** Physical parts check after delivery: cable OD, gland/clamp markings/range, enclosure knockouts/wall thickness, inlet box entry path, GFCI box volume/cover compatibility, and cable support interval/routing.
- **Status:** proposed

### F-018 — active PV topology still presents `900W 3S3P` as implementation despite deferred final solar module/string lock

- **Timestamp:** 2026-05-16 18:52 MDT
- **Subsystem:** solar / MPPT configuration / electrical topology standardization
- **Severity:** medium
- **Evidence/citation:**
  - `docs/implementation/ELECTRICAL_overview_diagram.md` lines 73-85 draws `Solar Path (900W, 3S3P)` with three `3x100W` strings, three `F-09` `15A gPV` fuses, and a `10 AWG` combiner-to-`SmartSolar MPPT 150/45` trunk.
  - `bom/bom_estimated_items.csv` row `24` line 24 says the final panel model/string is not locked yet and the prior `9x100W` concept is retained as a planning placeholder only; row `106` line 105 defers PV string fuse set/holder purchase until panel/string lock.
  - `docs/core/SYSTEMS.md` lines 63-64 calls solar a flexible-first placeholder / prior `9x100W` concept retained for modeling basis and lists the controller as SmartSolar `MPPT 150/45`.
  - `docs/studies/SOLAR_configuration_matrix.md` lines 75-89 shows that finalist flexible options may be `5S2P`, `4S2P`, `4S1P`, or `3S2P`, not necessarily `3S3P`; lines 123-130 require final datasheets, cold `Voc`, and hot `Vmp` checks before lock.
  - `docs/implementation/ELECTRICAL_fuse_schedule.md` lines 75 and 123 correctly mark `F-09A/B/C` as provisional pending final module datasheet max-series-fuse confirmation, but that caveat is not equally visible in the active overview PV diagram.
- **Why it matters before install:** Solar is late-build, so this is not an immediate shore-first blocker. The risk is that an active implementation diagram can drive roof gland/combiner/fuse procurement and cable routing around a three-string `3S3P` layout even though the current flexible-first shortlist could need a different string count, fuse count, combiner size, cold-voltage margin, and MPPT configuration. Premature roof penetrations or combiner buys are hard to reverse.
- **Recommended change:** Mark the overview PV path as `placeholder/modeling-only` until module/string lock, or replace the detailed `3S3P` drawing with a generic `final string set -> gPV combiner as required -> MPPT 150/45` placeholder. Keep row `106` and `F-09` fuse count explicitly deferred until final datasheets confirm string count, max-series-fuse rating, cold `Voc`, hot `Vmp`, and whether one controller remains valid.
- **Proposed update target(s):** `docs/implementation/ELECTRICAL_overview_diagram.md` PV path diagram and assumptions; `docs/implementation/ELECTRICAL_fuse_schedule.md` `F-09` caveat if needed; `bom/bom_estimated_items.csv` rows `24`, `31`, and `106` if the placeholder language is not clear enough.
- **Verification needed:** Final panel datasheets, roof fit/CAD, worst-case cold `Voc`, hot-weather `Vmp` headroom above charge voltage, controller current/power clipping policy, string fuse requirements, combiner/gland count, and roof weight under Hiatus `75 lb` cap.
- **Status:** proposed

## 5) Stale phrase / contradiction ledger

### Q-001 — broad stale/superseded phrase sweep

- **Query:** `rear-left|rear left|driver-side fridge|top-right|top left|top-left|15-series|split-DIN|3 vs 4|row 111|Sterling|BB1248120`
- **Scope:** repo markdown (`*.md`)
- **Representative hits/classification:**
  - `docs/core/TRACKING.md` lines 618-619: `3 vs 4` / `split-DIN` / `row 111` open AC questions — **active-fix**, captured as F-002.
  - `docs/plans/INSTALL_MINUS_12_READINESS_PLAN.md` lines 151-155: row `111` listed as deferrable — **active-fix**, captured as F-003.
  - `docs/implementation/INTERIOR_furniture_layout_and_galley.md` line 452: `Top-right soft cubes` — **active-fix**, captured as F-005.
  - `docs/implementation/INTERIOR_furniture_layout_and_galley.md` lines 55-61 and `docs/implementation/INTERIOR_driver_side_workstation.md` lines 30-35: generated diagram caveats mentioning rear-left/Iceco/top-right — **historical-ok/media-reference-ok** because they explicitly say the old geometry is superseded.
  - `docs/core/TRACKING.md` D-008/D-009/D-012/D-028/D-043 and `logs/LOG.md` historical entries mentioning Sterling, top-left/top-right, rear-left, or `15-series` — **historical-ok** where superseded follow-up language is explicit.
  - `docs/core/SYSTEMS.md` lines 58-60 and 119-127: Sterling return-pending and dedicated `48V` path — **harmless/current gate** because Sterling is described as physical return-pending hardware, not active architecture.
- **Next action:** After approved edits, rerun narrower searches for `split-DIN`, `3 vs 4`, `row 111`, `top-right`, `rear-left`, and `driver-side fridge` and ensure remaining hits are historical/media caveats only.

## 6) Patch plan queue

1. **Tracking cleanup after evidence check:** update `docs/core/TRACKING.md` to close or historical-mark completed May 7 logistics items, preserving any unresolved post-install inspection/sealing gates.
2. **AC tracking cleanup:** replace stale split-DIN / 3-vs-4 receptacle open questions with D-044 single-enclosure inspection and AC-in-only validation gates; verify row `111` obsolete and row `112` status.
3. **Historical install-plan AC row cleanup:** in `docs/plans/INSTALL_MINUS_12_READINESS_PLAN.md`, revise the deferrable AC-out hardware note so row `111` is marked obsolete rather than deferred.

4. **Electrical calculation reconciliation:** in `docs/implementation/ELECTRICAL_overview_diagram.md`, reconcile `82.5A` vs `77.5A` per-battery current basis and update dependent voltage-drop worksheet values after math verification.
5. **Interior stale storage phrase cleanup:** in `docs/implementation/INTERIOR_furniture_layout_and_galley.md`, replace active `top-right soft cubes` storage wording with current light/upper-zone storage language or mark it historical.
6. **Wire/BOM reconciliation:** inventory actual wire stock, then reconcile `bom/bom_estimated_items.csv` rows `28`, `32`, and `33` against `ELECTRICAL_overview_diagram.md` wire rollups before final cable cuts.
7. **Temp/study AC status cleanup:** mark `docs/temp/TEMP_procurement_red_flags.md` PRF-003/PRF-005 and `docs/studies/PROJECT_high_level_health_review_2026-03-15.md` AC-focus sections as closed/superseded by D-044, or add top caveats pointing to current owner docs.
8. **Core shore-passthrough status split:** in `docs/core/PROJECT.md`, distinguish selected/purchased shore interface hardware from still-open physical inlet placement/cut/strain-relief gates and from genuinely pending solar/diesel/propane passthrough routing.
9. **AC enclosure contradiction fix:** in `docs/core/PROJECT.md`, replace the `separate enclosures` instruction with the current single-enclosure safety rule: isolated neutral paths, correct PE/ground, no fixed downstream N-G bond, labels/barriers/strain relief, and AC-in-only first charge.
10. **Repo artifact cleanup:** inspect `.tmp_test.mmd` and `.tmp_test.pdf`; remove or relocate with context if they are export-test leftovers.
11. **Core systems snapshot dating:** reconcile `docs/core/SYSTEMS.md` planning snapshot date with embedded May 16 AC purchase-lock state; update date only after checking the whole snapshot for parity, or split the AC lock into a dated note.
12. **Bench AC safety gates:** add neutral isolation, no downstream N-G bond, PE continuity, chassis-bond/manual verification, and staged GFCI test gates to `ELECTRICAL_bench_layout_and_test_guide.md` before first live shore/AC validation.
13. **WS500 fuse voltage-class split:** split row `171`/F-12/F-13/F-14 requirements by actual circuit voltage; require a `48V`-appropriate fuse/holder for the battery-sense lead unless Wakespeed harness ratings prove otherwise.
14. **Class T spare mapping cleanup:** correct BOM row `7`'s row `105` Class T spare reference and remove row `105` from `ELECTRICAL_48V_ARCHITECTURE.md` Class T mapping; keep row `105` as `F-11` 12V ANL spare stock or create/update a real Class T spare row.
15. **AC purchased-SKU row list cleanup:** remove unrelated row `181` from `ELECTRICAL_AC_BOM.md` purchased-SKU lock language and keep row `112` visible as the actual unresolved outlet-box/cover gap.
16. **AC cable-entry fit gate:** add explicit cable-OD/gland/knockout/box-volume verification for `10/3`, `12/3`, inlet/enclosure entries, and GFCI boxes; record exact row `43-45`/`112` hardware specs or keep them as generic stock until fit is verified.
17. **PV placeholder demotion:** mark active `900W 3S3P` PV topology as modeling-only or replace it with a final-string placeholder until panel datasheets/string count/controller checks are locked.

Later proposed updates will be grouped by dependency order and left un-applied unless Dane approves a follow-up editing pass.

## 7) Final verification/gaps

- **Verification performed through latest pass:**
  - Concurrency guard checked at 2026-05-16 18:48 MDT: audit artifact mtime was 2026-05-16 14:46 MDT, older than 10 minutes; editing proceeded.
  - `git status --short` before this pass showed only the live audit artifact as untracked/changed.
  - This continuation pass read the live artifact/cursor first, then reviewed wire rows `28`, `29`, `32`, `33`; AC rows `107-114`, `123`, `179-181`; AC accessory rows `43-45` and `112`; `ELECTRICAL_AC_BOM.md`; `ELECTRICAL_overview_diagram.md`; `PROJECT.md`; `ELECTRICAL_bench_layout_and_test_guide.md`; solar/MPPT docs; `SYSTEMS.md`; `ELECTRICAL_fuse_schedule.md`; and `ELECTRICAL_48V_ARCHITECTURE.md`.
  - Findings F-016 through F-018 were appended immediately after discovery, and F-015 was refined when the same Class T/row `105` mapping problem was found in the active 48V architecture doc.
  - No canonical docs, BOMs, diagrams, media, or raw photos were edited; only this live audit artifact was modified.
  - No commit or push was made.
  - Final checks for this pass: `git status --short` showed only `?? docs/studies/PREINSTALL_FULL_REPO_AUDIT_LIVE_2026-05-16.md`; `git diff --no-index --check /dev/null docs/studies/PREINSTALL_FULL_REPO_AUDIT_LIVE_2026-05-16.md` reported no whitespace errors; audit sanity script reported `358` lines, `0` code fences, balanced fences, no quadruple-blank runs, and `0` accidental leading `+-` diff-marker lines; token-pattern scan found `0` matches for common private-key/GitHub/OpenAI/AWS/Slack token patterns.
- **Gaps remaining / continuation notes:**
  - Wire rows `28`, `29`, `32`, and `33` were rechecked against the active rollup during the 18:49 MDT pass; no new issue beyond existing F-006 was needed, and row `29` matched the rollup.
  - Continue in `ELECTRICAL_48V_ARCHITECTURE.md` around one-battery-trip behavior, vendor gates, and `TRACKING.md` risk/open-question parity.
  - Later continuation should also review battery/BMS assumptions, charge-source enable order, charge-profile closure, and any remaining DC diagram safety-language gaps.
  - The broad stale phrase query returned `319` matches and was classified at representative-hit level; a future cleanup sprint should rerun narrower searches after approved source edits.
  - This audit did not open raw images/PDFs beyond file inventory and README/context review; no raw media was added or modified.
  - Findings are proposed only; no canonical source docs, BOMs, diagrams, or media were edited.
