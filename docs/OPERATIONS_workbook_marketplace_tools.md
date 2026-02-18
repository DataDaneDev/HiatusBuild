# Marketplace Tools (Ryobi-First)

Status date: 2026-02-17

Purpose: buy used tools efficiently (Facebook Marketplace), minimize battery-ecosystem regret, and track “which version to buy” questions in one place.

Related artifacts:
- Tracker CSV (source of truth for listings): `bom/tools_marketplace_tracker.csv`
- General marketplace routine (non-tools): `docs/OPERATIONS_workbook_marketplace_finds.md`

## Strategy (minimize regret)
- Pick one cordless battery ecosystem first; default: `Ryobi ONE+ 18V`.
- Favor corded for high-duty stationary tools (miter saw, larger router, shop vac/dust extraction).
- Prefer tool-only used listings; buy batteries/chargers more selectively than tools.
- When in doubt: buy the “good enough” tool to start building, then upgrade once you’ve proven the workflow needs it.

## Ryobi ecosystem cheat sheet (what “versions” usually means)
- Platform:
  - `ONE+ 18V` (cordless, broad tool selection).
  - `Corded` (often best value for stationary/high-draw tools).
  - `40V` (mostly outdoor lawn tools; usually not needed for this build).
- Motor:
  - `Brushed`: cheaper, heavier battery draw, more wear over time.
  - `Brushless`: more power per size, better efficiency, generally worth it for “core” tools.
- Line:
  - `ONE+` (standard).
  - `ONE+ HP` (typically brushless + better electronics; often benefits from higher-output “HP” batteries but usually works with standard packs).
- Batteries (rule-of-thumb):
  - Start: `2x 4Ah` packs + `1x 2Ah` compact pack + any reliable charger.
  - Heavy-use tools (sander/multi-tool/circular saw): prefer `4Ah+`.
  - If a listing includes batteries: treat them as “bonus” unless you can confirm health.

## Recommended minimums (what to target used)
| Tool | “Good enough” version | Worth upgrading to | Battery note |
| --- | --- | --- | --- |
| Drill/driver | Brushed drill/driver | Brushless compact (or hammer drill if needed) | `2Ah` ok; `4Ah` nicer |
| Impact driver | Brushed impact | Brushless w/ speed modes | `2Ah` ok; `4Ah` nicer |
| Oscillating multi-tool | Any variable-speed | Lower-vibration brushless + tool-free clamp | `4Ah+` preferred |
| Random orbital sander | Any 5" ROS | Variable speed + better dust collection | `4Ah+` preferred |
| Router | Corded trim router | Larger corded plunge router for joinery | Cordless routers drain packs fast |
| Miter saw | Corded 10" | Sliding compound + good stand | Corded recommended for duty cycle |

## Used-buy checklist (Facebook Marketplace)
### For tools
- Run it for `30–60s` (ideally under light load) and listen for grinding/squealing, burning smell, or surging RPM.
- Check the business end:
  - Drill: chuck wobble, clutch works, both speeds work.
  - Impact: collet retention, mode selector works, no abnormal hammering noise.
  - Multi-tool: head doesn’t wobble, speed dial works, clamp holds blades.
  - Sander: pad is flat, not melted/warped; minimal vibration.
  - Miter saw: fence straight, bevel/miter detents lock, guard returns freely.
  - Router: collet tight, no obvious runout, speed control works.
- Confirm included parts you’d otherwise have to re-buy (fences, dust ports, edge guides, bases, wrenches, cases).

### For batteries/chargers
- Avoid packs that are cracked, swollen, or have melted terminals.
- Ask for date code/age and confirm it takes a full charge and runs a tool without immediate drop-out.
- Charger should start/finish a charge normally (no flashing error patterns).

## Tool-by-tool “version” guide (Ryobi-first)
Use this to decide what to write in the tracker under “must-have features” and “red flags”.

### Drill/driver
- Decide: standard drill vs hammer drill (only needed if you’ll drill masonry/brick often).
- Prefer: brushless, `1/2"` chuck, 2-speed, comfortable grip, compact head.
- Watch for: chuck wobble, slipping clutch, dead speed selector.

### Impact driver
- Prefer: brushless, 2–3 speed/mode control, good LED placement.
- Watch for: collet not retaining bits, intermittent trigger.

### Oscillating multi-tool (cutting multitool)
- Prefer: tool-free blade change, variable speed, lower vibration, good dust port (if present).
- Watch for: accessory clamp wear (blade slips), head wobble.

### Miter saw
- Corded is usually the best used value.
- Decide: non-sliding vs sliding; blade size (`10"` is typically plenty and lighter than `12"`).
- Watch for: bent fence, sloppy rails (sliders), rough bearings, broken guard, missing detent stops.
- Hidden costs: blade, stand, and dust collection.

### Router
- Decide:
  - Trim router (small edge profiles, light dados).
  - Plunge/2+ HP router (joinery, heavier cuts).
- Prefer: variable speed, soft start, solid base, common collet sizes (`1/4"` at minimum; `1/2"` for larger routers).
- Watch for: runout, sticky plunge posts, damaged collet/nut.

### Sanders (plural)
- Start with: 5" random orbital sander + a detail sander if you’ll do corners.
- Prefer: good dust collection (bag or vac port), variable speed.
- Watch for: warped pad, excessive vibration, stripped hook-and-loop.

## How to use the tracker CSV
- One row per listing (even if you pass) so you build pricing intuition over time.
- Treat “target price” as a decision gate: if it’s above target, only buy if it includes meaningful extras (batteries, stand, premium blade, etc.).
- Record “reason passed” aggressively; it prevents repeat mistakes.

## Don’t forget the “hidden” must-buys
- Consumables: bits, blades, sanding discs, router bits, driver bits.
- Accuracy: speed square, combination square, tape, straightedge, clamps.
- Dust/PPE: shop vac (corded), hearing protection, eye protection, respirator.
