# Week 1 · 05 – 11 Oct 2026 · Sprint 1 (part 1)

**Hardware goal:** Understand DC basics well enough to design a cell-voltage divider and read it with an STM32.
**CV goal:** Treat images as NumPy arrays; build grayscale from scratch and validate it against OpenCV.
**Daily 5:** 📱 `daily-qa/week-01.md`
**Where:** 📱 phone · 💻 laptop · 🔧 bench

---

## Mon 05 Oct · Analog concept: Ohm's law, power, resistor specs

| Block | Task |
|---|---|
| 📱 Learn (60) | Ohm's law; power P = VI = I²R = V²/R. Resistor specs: tolerance, power rating, tempco (ppm/°C), E-series (E12, E24, E96), types (carbon film, metal film, thin/thick film, shunt). |
| 📱 Do (75) | Solve the 10 problems in `hardware-track/s1-dc-circuits-and-cell-sensing/problems/2026-10-05-ohms-law-power.md` by hand. Read one metal-film resistor datasheet (e.g., Yageo MFR series) and extract 5 specs. |
| 📱 Check (30) | Power-rating check for 3 cases (with 2× margin). |
| 📱 Log (15) | Journal + commit. |

## Tue 06 Oct · CV concept: NumPy + image as a matrix

| Block | Task |
|---|---|
| 📱 Learn (60) | NumPy: shape, dtype, indexing, slicing, broadcasting, vectorisation. Image = H × W × C array of `uint8`. OpenCV loads **BGR**, not RGB. |
| 💻 Do (75) | Load an image with `cv2.imread`; print shape and dtype; crop by slicing; split channels; show with matplotlib (convert BGR → RGB); brighten with `int16` + `np.clip`; demonstrate `uint8` overflow. |
| 💻 Check (30) | Create a 100 × 100 black image with a white square in the centre using only NumPy. |
| 📱 Log (15) | Journal + commit. |

## Wed 07 Oct · Analog → BMS: KVL, KCL, dividers, first LTspice sim

| Block | Task |
|---|---|
| 📱 Learn (60) | KVL, KCL, series/parallel, divider formula, loading effect (preview). |
| 💻 Do (75) | Hand-design a divider for 1 cell (4.2 V → ≤ 3.0 V) and for a 4S pack (16.8 V → ≤ 3.0 V). Simulate both in LTspice (`.op` and `.dc` sweep over the cell range). |
| 💻 Check (30) | Hand calc = LTspice? Then add a 100 kΩ load on the output and measure the error; this is next week's Thevenin topic. |
| 📱 Log (15) | Journal + commit LTspice files to `hardware-track/s1-.../sim/`. |

## Thu 08 Oct · CV practice: grayscale from scratch

| Block | Task |
|---|---|
| 💻 Do (150) | Implement `gray = 0.299 R + 0.587 G + 0.114 B` with NumPy (mind BGR order). Compare with `cv2.cvtColor`: max absolute difference and number of differing pixels. Try equal weights (1/3 each) and compare visually. Save plots. |
| 💻 Check (15) | Sub-pass: max diff ≤ 1. If not, find why. |
| 📱 Log (15) | Journal + commit to `cv-track/s1-images-as-arrays/`. |

## Fri 09 Oct · BMS concept: Li-ion cell basics + Python

| Block | Task |
|---|---|
| 📱 Learn (60) | Cell structure (graphite anode, NMC / LFP cathode, separator, electrolyte). Voltage windows, capacity (Ah), energy (Wh), C-rate. OCV vs terminal voltage. SOC and SOH. Source: Battery University. |
| 📱 + 💻 Do (75) | 1. 📱 Read an 18650 datasheet (e.g., Samsung INR18650-35E or LG MJ1): extract nominal V, max V, cut-off, capacity, max continuous discharge, charge method, temperature range. 2. 💻 Python: plot the OCV–SOC tables below; compute slope (mV per 1% SOC) in the 20–80% range; use `np.interp` to convert voltage → SOC. |
| 📱 Check (30) | If your voltage measurement has ±25 mV error, how big is the SOC error at 50% for NMC? For LFP? |
| 📱 Log (15) | Journal + commit. |

Approximate OCV tables, **for practice only** (you'll replace them with real data in Sprint 5):

| SOC % | 0 | 10 | 20 | 30 | 40 | 50 | 60 | 70 | 80 | 90 | 100 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| NMC (V) | 3.00 | 3.45 | 3.55 | 3.61 | 3.65 | 3.70 | 3.78 | 3.86 | 3.95 | 4.06 | 4.18 |
| LFP (V) | 2.95 | 3.20 | 3.24 | 3.26 | 3.28 | 3.29 | 3.30 | 3.32 | 3.33 | 3.35 | 3.40 |

## Sat 10 Oct · Bench lab: cell voltage measurement chain

**Where:** 🔧 bench + 💻 laptop for every step.

**Safety:** cell in a holder with an inline fuse; or use the bench supply at 4.2 V with a 50 mA current limit.

| Step | Task |
|---|---|
| 1. Predict | Measure your two resistors with the DMM. Calculate the expected ADC count **before** powering. Write it down. |
| 2. Build | Divider on breadboard → STM32 ADC pin, 100 nF from ADC pin to GND. |
| 3. Firmware | Read ADC, average 64 samples, print raw count over UART at ~10 Hz. |
| 4. Python | Log to CSV with `pyserial`; convert to cell voltage; plot. |
| 5. Compare | Cell voltage from ADC vs DMM: error in mV. |
| 6. Break it | (a) Remove the 100 nF cap → what changes? (b) Use nominal instead of measured resistor values → how much error? |
| 7. Record | Table: predicted vs measured; list of error sources with rough size in mV. |

## Sun 11 Oct · Catch-up, docs, review

| Block | Task |
|---|---|
| 💻 Catch-up | Pending tasks first. |
| 💻 Docs | Fill week 1 results in both S1 sprint READMEs (tables are ready). |
| 📱 LinkedIn | Draft post #2: *"Two resistors, seven decisions: measuring a Li-ion cell with an STM32."* |
| 📱 English | Add 5 phrases to `english/phrase-bank.md`; reread `english/feedback-log.md`. |
| 📱 Check-in | Send the Sunday check-in to Claude with: ADC error (mV), grayscale max diff, Daily 5 score. |
