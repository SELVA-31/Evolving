# S1 · DC circuits and cell voltage sensing · 05 – 18 Oct

**Goal:** Measure a Li-ion cell's voltage with an STM32 ADC and explain every error source.
**Pass check:** STM32 reading within **±10 mV** of the multimeter, with an error budget in mV.

Folders: `sim/` (LTspice) · `firmware/` (STM32) · `python/` · `data/` · `images/`

## Experiments

| # | Date | Experiment | Predicted | Measured | Notes |
|---|---|---|---|---|---|
| 1 | 03 Oct | Resistor tolerance check (10 resistors) | | | |
| 2 | 07 Oct | Divider: hand calc vs LTspice | | | |
| 3 | 10 Oct | Cell voltage: STM32 ADC vs multimeter | | | |

## Error budget (fill in W2)

| Source | Size (mV) | How I found it | Fix |
|---|---|---|---|
| | | | |

## Design justification: divider

| Ref | Function | Value and calculation | Why this part | What fails if wrong |
|---|---|---|---|---|
| R1, R2 | | | | |
| C1 | | | | |

## Lessons

-
