Status: 24V Candidate Variant (non-canonical; canonical remains 48V baseline)

# Electrical Trade Study: 24V vs 48V Core (12V Fallback Sensitivity)

As-of date: `2026-02-20`

Purpose: deliver a decision-grade comparison of `24V` vs `48V` for this project using locked project preferences, current BOM deltas, and same-day live pricing checks.

## Locked Decision Inputs
- AC scope: `AC kitchen` retained in Phase 1.
- Inverter requirement: `~2.5kW` mixed use.
- Priority: `simplicity + cost` first.
- Battery class: `~15kWh`.
- Future growth: no expected major high-AC expansion in next `12-18` months.
- Churn tolerance: high (architecture can be changed now).
- Distribution strategy: `24V-native first`; keep `24->12` only where truly required.
- Vendor preference: `Victron/Sterling preferred`.

## Core Electrical Math (Locked)
Assumptions: `P_ac = 2500W`, `inverter_efficiency = 0.92`, nominal voltages `25.6V` and `51.2V`.

- `I_dc = P_ac / (V_dc * inverter_efficiency)`
- `Ah_required = Wh_bank / V_nominal`

| Item | 24V core | 48V core |
| --- | ---: | ---: |
| Inverter DC current at 2.5kW | `2500 / (25.6*0.92) = 106.1A` | `2500 / (51.2*0.92) = 53.1A` |
| Bank Ah for 15.36kWh | `15360/25.6 = 600Ah` | `15360/51.2 = 300Ah` |
| Alternator house-side current at 1.5kW | `1500/25.6 = 58.6A` | `1500/51.2 = 29.3A` |
| MPPT 150/45 output ceiling | `45A*28.8V = 1296W` | `45A*57.6V = 2592W` |
| MPPT clipping at 900W array | `No` | `No` |

Interpretation: `48V` clearly wins current reduction margin; `24V` stays in practical current ranges for this load and inverter class.

## Residual 12V Converter Budget (24V Candidate)
24V candidate assumption is to migrate most loads to 24V-capable devices, leaving only residual legacy/safety loads on 12V.

Planning budget for residual 12V path:
- Continuous design: `<=10A` (`<=120W` at 12V).
- Surge allowance: `<=20A` short duration.
- Example residual-only loads: gas detector, any unavoidable 12V control module, low-power legacy accessories.

This removes the need for a large battery-backed 12V subsystem in the candidate path.

## Live Pricing Check (US, 2026-02-20)
Note: market prices change quickly; values below are snapshot references.

### Inverter/charger class (~3kVA)
| Architecture | Product | Price | Vendor | Link |
| --- | --- | ---: | --- | --- |
| 24V | Victron MultiPlus-II 24/3000-70-50 (PMP242305130) | `$1,230.00` | MAURIPRO | https://www.mauripro.com/products/vie-pmp242305130 |
| 48V | Victron MultiPlus-II 48/3000-35-50 (PMP482305102) | `$1,270.00` | MAURIPRO | https://www.mauripro.com/products/vie-pmp482305102 |

### Alternator charger class (Sterling Saturn)
| Architecture | Product | Price | Vendor | Link |
| --- | --- | ---: | --- | --- |
| 24V output | BB1224120 | `$969.00` | Sterling Power North America | https://sterling-power.us/products/bb1224120 |
| 48V output | BB1248120 | `$949.00` | Sterling Power North America | https://sterling-power.us/products/bb1248120 |

### 24->12 or 48->12 residual conversion path
| Architecture | Product | Price | Vendor | Link |
| --- | --- | ---: | --- | --- |
| 24V core | Orion-Tr Smart 24/12-30A (isolated) | `$243.95` | Bend Battery | https://bendbattery.com/products/orion-tr-smart-24-12-30a-360w-isolated-dc-dc-charger |
| 48V core | Orion-Tr Smart 48/12-30A (isolated) | `$243.95` | MAURIPRO | https://www.mauripro.com/products/vie-ori481238120 |

### Battery architecture examples (~5.12kWh modules)
| Architecture | Product | Unit Price | Qty for ~15.36kWh | Total | Vendor | Link |
| --- | --- | ---: | ---: | ---: | --- | --- |
| 24V | EG4 LifePower4 24V 200Ah (5.12kWh) | `$1,149.00` | `3` | `$3,447.00` | Inverters R Us | https://invertersrus.com/product/eg4-flp-24v/ |
| 48V | EG4 LL-S 48V 100Ah (5.12kWh) | `$1,299.00` | `3` | `$3,897.00` | Inverters R Us | https://invertersrus.com/product/eg4-ll-s-48v/ |

Live-price direction from this check: `24V` shows lower battery and inverter cost in this snapshot; alternator charger and small converter costs are near parity.

## Variant BOM Delta (Architecture-Sensitive Rows)
Mapped in `bom/variants/24v/bom_estimated_items_24V_candidate.csv` using `24V_CANDIDATE_STATUS` tags.

| Row | Current 48V baseline intent | 24V candidate action |
| ---: | --- | --- |
| `3` | 48V bank | `SWAP` -> 24V bank sized to ~15kWh |
| `5` | 48V disconnect | `SWAP` -> 24V disconnect |
| `6` | Lynx Distributor | `KEEP` |
| `7` | Class T main battery protection | `SWAP` ratings/recoordination |
| `10` | 58V/80V MEGA ecosystem | `SWAP` to 32V branch fuse ecosystem where valid |
| `11` | 48V-specific holder selections | `SWAP` for 24V path and residual 12V path |
| `12` | 48V MultiPlus-II | `SWAP` -> 24V MultiPlus-II |
| `18` | BB1248120 (to 48V) | `SWAP` -> BB1224120 (to 24V) |
| `20` | 48->12 30A primary feed | `SWAP` -> 24->12 residual-only converter strategy |
| `21` | 12V 100Ah buffer battery | `REMOVE` |
| `25` | MPPT 150/45 | `KEEP` |
| `26` | BBR remote | `KEEP` |
| `117` | battery combine busbars | `KEEP` (relabel/retune ratings) |
| `124-126` | n/a | `ADD` 24V migration and residual-12V items |

## Decision Summary
Primary recommendation from this candidate package: **`24V core` with `24V-native-first distribution` and a small residual `24->12` path only if required.**

Why:
- Meets the `~2.5kW` inverter requirement at manageable DC current.
- Reduces architecture complexity relative to the current `48V + large 12V-buffered subsystem` approach.
- Improves cost direction in this snapshot when compared on equivalent architecture targets.

Where 48V still wins:
- Better high-power current margin and better long-term scaling for larger future AC growth.

## Migration Implications If 24V Is Promoted
1. Rebase canonical docs from current 48V paths to this 24V candidate set.
2. Rebuild fuse schedule around 24V branch currents and voltage classes.
3. Rework low-voltage device list to maximize true 24V-native loads and minimize converter dependency.
4. Re-run cabinet physical layout for updated battery/inverter/charger dimensions and cable routing.

## Notes
- This document is a variant analysis artifact only.
- Canonical implementation remains on 48V until explicit promotion.
