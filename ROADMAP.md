# Roadmap · 01 Oct – 27 Dec 2026

**Identity:** System integrator (hardware + software) → application-specific hardware engineer.
**Time:** 3 h/day, every day. Weekday backlog → cleared on Sunday with extra hours.
**Tracks:** Hardware (analog → BMS) ~12 h/week · Computer vision ~6 h/week · Docs + English ~3 h/week.

---

## 1. Rules

1. **No component without a reason.** Every part on a schematic gets a line in a justification table.
2. **Predict → Measure → Explain the gap.** Write your prediction before every simulation, build or run.
3. **Every sprint ends with a measured pass check**, not just notes.
4. **Validate against a reference:** hand calc vs LTspice vs bench; your code vs OpenCV; your design vs a TI/ADI reference design.
5. **Minimum day rule:** on a bad day, do 30 min + Daily 5. The streak stays alive; the missing hours move to Sunday.
6. **Laptop-free days:** max 2 per week. Do the 📱 blocks; move that day's 💻 / 🔧 block to the weekend.

---

## 2. Daily structure (3 h)

📱 phone · 💻 laptop · 🔧 bench

| Block | Time | What |
|---|---|---|
| 📱 Learn | 60 min | 1–2 sources; notes in your own words |
| 💻 / 🔧 Do | 75 min | Hand calc → simulate → code / build |
| 📱 Check (💻 on sim / code days) | 30 min | Problems, compare with reference, pass-check progress |
| 📱 Log | 15 min | 5-line journal entry (`journal/TEMPLATE.md`) + git commit |
| 📱 **Daily 5** | ~10 min, phone, anytime | 5 questions on yesterday's topic (`daily-qa/`) |

## 3. Weekly rhythm

| Day | Focus |
|---|---|
| Mon | Analog concept: theory + hand calculations |
| Tue | CV concept + code |
| Wed | Analog → BMS application: LTspice / Python |
| Thu | CV practice |
| Fri | BMS concept + Python model |
| Sat | Bench lab: build + measure (STM32) |
| Sun | **Catch-up first** → docs → LinkedIn draft → English → weekly check-in with Claude |

---

## 4. Week-by-week plan

| Week | Dates | Sprint | Hardware track (analog → BMS) | CV track |
|---|---|---|---|---|
| W0 | Thu 01 – Sun 04 Oct | Setup | Units, V/I/R, multimeter, cell safety, STM32 → UART → Python | Python basics |
| W1 | 05 – 11 Oct | S1 | Ohm's law, power, resistor specs; KVL/KCL, dividers; Li-ion basics, OCV–SOC | NumPy, image as a matrix, grayscale from scratch |
| W2 | 12 – 18 Oct | S1 | Thevenin, loading, source impedance; ADC basics (LSB, reference); error budget; cell datasheet, internal resistance | Histograms, thresholding (Otsu), HSV |
| W3 | 19 – 25 Oct | S2 | Capacitors (types, ESR, DC bias), RC charge/discharge; inductor basics; cell relaxation | 1D → 2D convolution, kernels, blur, padding |
| W4 | 26 Oct – 01 Nov | S2 | Impedance, low-pass filters, Bode plots, anti-aliasing; fit cell model R0 + R1‖C1 | Gradients, Sobel, noise; conv2d from scratch |
| W5 | 02 – 08 Nov | S3 | Diodes (Schottky, Zener, TVS), reverse polarity; BJT basics; BMS faults (OV/UV/OC/SC/OT), fuses | Canny step by step; morphology |
| W6 | 09 – 15 Nov | S3 | MOSFETs (Vgs(th), Rds(on), gate drive, SOA, body diode); back-to-back switches; DW01A + FS8205A teardown | Contours, pixel → mm, camera exposure / focus / lighting |
| W7 | 16 – 22 Nov | S4 | Op-amp rules, inverting / non-inverting / buffer, single supply, rail-to-rail (LM358 vs MCP6002); NTC sensing | Alignment, image subtraction, template matching; DeepPCB |
| W8 | 23 – 29 Nov | S4 | Difference amp, offset / bias / CMRR / GBW; shunt current sensing, INA226; coulomb counting | PCB defect pipeline; precision / recall |
| W9 | 30 Nov – 06 Dec | S5 | ADC deep dive (noise, ENOB, averaging); references (TL431, LM4040); SOC by OCV + coulomb counting on CALCE data | ML basics: loss, gradient descent (NumPy), train / val / test |
| W10 | 07 – 13 Dec | S5 | LDO vs buck, efficiency, quiescent current; passive balancing; SOC fusion (EKF = stretch) | CNN in PyTorch on NEU-CLS; confusion matrix |
| W11 | 14 – 20 Dec | S6 | BQ76920 datasheet + reference design walkthrough; requirements + block diagram for your 3S–4S monitor | Webcam → detect → UART → STM32 reject signal |
| W12 | 21 – 27 Dec | S6 | EasyEDA schematic + justification table + design review | Latency + accuracy test; demo video; write-up |

Day-by-day plans: `weekly-plans/week-XX.md` (created one week ahead).

---

## 5. Sprint pass checks

| Sprint | Dates | Hardware pass check | CV pass check |
|---|---|---|---|
| S1 | 05 – 18 Oct | STM32 cell reading within **±10 mV** of the multimeter; every error source explained in mV | NumPy-only grayscale / histogram / threshold match OpenCV (**max diff ≤ 1**) |
| S2 | 19 Oct – 01 Nov | R0, R1, C1 fitted from a real pulse test; model vs measured plot | conv2d from scratch matches `cv2.filter2D` |
| S3 | 02 – 15 Nov | Every part of a DW01A + FS8205A module explained; measured Rds(on) vs datasheet | Object size in mm vs ruler, target error **≤ 3%** |
| S4 | 16 – 29 Nov | Coulomb-counted capacity vs full discharge, target error **≤ 3%** | Precision and recall on DeepPCB test images |
| S5 | 30 Nov – 13 Dec | SOC RMSE per method (OCV, coulomb counting, fusion) on CALCE data | Confusion matrix on NEU-CLS + 3 failures explained |
| S6 | 14 – 27 Dec | 3S–4S monitor schematic; every part in the justification table; review vs BQ76920 reference | End-to-end demo: latency (ms) + accuracy measured |

---

## 6. Core sources

| Track | Source | Why it fits |
|---|---|---|
| Analog | All About Circuits textbook, Vol. I–III (free, web) | Starts from zero, DC → AC → semiconductors in order; readable on phone |
| Analog | *Practical Electronics for Inventors* (Scherz & Monk) | Theory tied to real parts; bridges concept → component choice |
| Analog | *The Art of Electronics*, 3rd ed. (Horowitz & Hill) | Industry "why" behind design choices; use from S3 for depth |
| Analog + BMS | TI / Analog Devices datasheets and app notes | Real design decisions with numbers; how industry writes |
| BMS | Battery University (free, web) | Practical cell behaviour: charging, aging, safety |
| BMS | Gregory Plett: *Algorithms for Battery Management Systems* (Coursera) + *Battery Management Systems* Vol. I–II | Standard path for cell models, SOC, EKF (S2, S5) |
| CV | Shree Nayar: *First Principles of Computer Vision* (YouTube) | Physics and math under each algorithm, not just code |
| CV | OpenCV-Python tutorials | The reference you validate against |
| CV | Szeliski: *Computer Vision: Algorithms and Applications*, 2nd ed. (free PDF) | Depth when you need it |
| ML | *Dive into Deep Learning* (d2l.ai, free) | S5 CNN basics with runnable PyTorch code |

---

## 7. Outputs

| Output | Frequency |
|---|---|
| Journal entry + git commit | Daily |
| Daily 5 (Anki / GitHub app) | Daily |
| LinkedIn post (draft Sun, publish Mon) | Weekly |
| Sprint README with results + justification table | Every 2 weeks |

## 8. Sunday check-in (paste this to Claude)

```
Week N check-in
- Hours: __/21 · Streak: __ days
- Pass-check numbers: ...
- Daily 5: __/35 correct · hardest question: ...
- Stuck on: ...
- Links / files: ...
```

Claude replies with: review of results, next week's day-by-day plan, next week's 35 questions, English feedback.
