Status: 24V Candidate Variant (non-canonical; canonical remains 48V baseline)

# Electrical Topology Diagram (24V Candidate)

As-of date: `2026-02-20`

Purpose: implementation candidate topology for a `24V` core architecture with `24V-native-first` distribution and residual `12V` support only where needed.

Related candidate docs:
- `docs/variants/24v/ELECTRICAL_24V_vs_48V_trade_study.md`
- `docs/variants/24v/ELECTRICAL_fuse_schedule_24V_candidate.md`
- `docs/variants/24v/SYSTEMS_24V_candidate.md`
- `bom/variants/24v/bom_estimated_items_24V_candidate.csv`

## Candidate Core Topology
```mermaid
flowchart LR
    ALT[Factory alternator 12V side] --> B2B[Sterling BB1224120 12V -> 24V]

    PV[900W array 3S3P] --> MPPT[SmartSolar MPPT 150/45]

    BATA[24V Battery A] --> CTA[F-01A Class T]
    BATB[24V Battery B] --> CTB[F-01B Class T]
    BATC[24V Battery C] --> CTC[F-01C Class T]

    CTA --> POSBUS[24V + combine bus]
    CTB --> POSBUS
    CTC --> POSBUS

    POSBUS --> DISC[24V disconnect]
    DISC --> LYNX[Lynx Distributor]

    BATA --> NEGBUS[24V - combine bus]
    BATB --> NEGBUS
    BATC --> NEGBUS
    NEGBUS --> SHUNT[SmartShunt]
    SHUNT --> LYNX

    LYNX -->|F-02| INV[MultiPlus-II 24V class]
    MPPT -->|F-03| LYNX
    B2B -->|F-04| LYNX

    LYNX -->|F-05 residual path| ORION[Orion 24/12 converter]
    ORION --> PANEL12[Small residual 12V fuse panel]

    LYNX --> PANEL24[Primary 24V branch panel]
    PANEL24 --> FRIDGE[24V fridge]
    PANEL24 --> HEATER[24V heater path]
    PANEL24 --> USBPD[24V USB-C PD path]
    PANEL24 --> STARLINK[24V Starlink power path]
```

## Candidate Notes
- High-current architecture remains centralized via Lynx/busbar + shunt.
- Residual 12V path is intentionally constrained to low-power legacy/safety loads.
- No dedicated large 12V buffer battery in this candidate baseline.
- MPPT `150/45` remains valid for `900W` at 24V (no clipping at `~28.8V` output target).
