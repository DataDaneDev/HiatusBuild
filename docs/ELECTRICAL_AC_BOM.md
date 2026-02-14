# Electrical AC BOM (Phase 1)

As-of date: `2026-02-13`

Purpose: lock the compact AC parts list for the current truck-camper topology using:
- `2x` small DIN enclosures (`input` and `output`)
- `1x` dedicated shore input breaker
- `2x` AC-out branch breakers

Related docs:
- `docs/ELECTRICAL_overview_diagram.md`
- `bom/bom_estimated_items.csv`

## Locked Topology

### Input enclosure (shore to inverter)
- Path: `shore inlet -> AC input breaker -> MultiPlus AC-in (L)`
- Neutral path: `shore N -> insulated neutral terminal/splice -> MultiPlus AC-in (N)`
- Ground path: `shore PE -> ground bar/stud -> MultiPlus PE + chassis bond`

### Output enclosure (inverter to outlets)
- Path: `MultiPlus AC-out-1 (L) -> hot feed splitter -> 2x branch breakers`
- Branch A (`driver`): breaker output to first GFCI/outlet chain
- Branch B (`passenger`): breaker output to first GFCI/outlet chain
- Neutral path: `AC-out-1 N -> output neutral bar -> both branch neutrals`
- Ground path: `AC-out-1 PE -> output ground bar -> both branch grounds`

## Buy List (AC-Specific)

1. `2x` DIN enclosures, `2-way` each, with included rail and cable-entry hardware.
2. `3x` DIN-mount breakers, `UL 489`, `1-pole`, `120VAC`:
- `1x 20A` for shore input protection
- `1x 20A` for driver-side branch
- `1x 15A` for passenger-side branch
3. `1x` hot distribution block (`1-in / 2-out`) for output enclosure feed split.
4. `2x` insulated neutral bars or terminal blocks:
- `1x` for input enclosure
- `1x` for output enclosure
5. `2x` ground bars (or equivalent grounded termination points):
- `1x` for input enclosure
- `1x` for output enclosure
6. Cable glands / strain reliefs sized for planned AC cable runs (`10/3` shore feed, `12 AWG` branch).
7. Terminal consumables:
- ferrules/ring terminals sized to actual wire and terminal type
- adhesive heat shrink
8. Enclosure completion hardware:
- DIN end-stops
- blank fillers
- circuit labels

## Receptacle Plan (Current)
- `4` total receptacle locations (`2` galley/driver zone, `2` office/passenger zone)
- Preferred protection strategy:
- `2x` GFCI receptacles at first outlet in each branch
- downstream standard receptacles on GFCI load side where applicable

## Critical Wiring Constraints
1. Do not share a common hot bus between `AC-in` and `AC-out` circuits.
2. Keep `AC-in` neutral and `AC-out` neutral termination paths isolated.
3. Land only conductors allowed by each breaker terminal listing (no unlisted double-lugging).
4. Maintain continuous equipment ground path and chassis bond.

## Procurement Notes
- Enclosure listings alone do not qualify breaker protection suitability.
- Breakers should be confirmed as `UL 489` listed for branch/feeder protection use.
- Final SKU lock should be recorded back into `bom/bom_estimated_items.csv` rows:
- `13`, `109`, `110`, `111`, `112`, `113`, `114`, `115`, `116`.
