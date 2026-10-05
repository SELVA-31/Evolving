# Daily 5 · Week 01 · Mon 05 – Sun 11 Oct 2026

**How to use:** 5 questions per day, ~10 min, on your phone. Each day covers the topic you studied the **day before**. Answer **before** opening the answer. Q5 = 60-second voice note.

---

## Mon 05 Oct · Topic of Sun 04 Oct: lab notebook, Git, week 0 review

**Q1 · Recall** — What four sections should every project README have?

<details><summary>Answer</summary>

1. Problem: what and why.
2. Approach: method, schematic, code.
3. Results: numbers and plots.
4. How to reproduce: hardware, software, steps.
Optional: lessons learned.

</details>

**Q2 · Why** — Why does showing failures in your lab notebook help with recruiters?

<details><summary>Answer</summary>

It proves you can debug: how you noticed a problem, found the root cause and fixed it. That is the daily work of a hardware engineer. Polished results alone don't show how you think.

</details>

**Q3 · Calc** — Convert: 0.047 µF to nF · 2 200 000 Ω to MΩ · 0.0035 A to mA.

<details><summary>Answer</summary>

47 nF · 2.2 MΩ · 3.5 mA.

</details>

**Q4 · Apply** — What is the difference between `git add`, `git commit` and `git push`?

<details><summary>Answer</summary>

add: choose (stage) the changes to save.
commit: save a snapshot locally, with a message.
push: upload your commits to GitHub.

</details>

**Q5 · Explain** — Aloud, 60 s: what is a lab notebook, and why do you keep yours public?

<details><summary>Answer</summary>

Model answer: "A lab notebook records what I tried, what I expected, what happened and what I learned, with enough detail that someone else can reproduce it. Keeping it public on GitHub makes me write clearly, lets others give feedback, and shows recruiters how I think, not just what I built."

</details>

## Tue 06 Oct · Topic of Mon 05 Oct: Ohm's law, power, resistor specs

**Q1 · Recall** — Write three forms of the power equation for a resistor.

<details><summary>Answer</summary>

P = V × I = I² × R = V² / R.

</details>

**Q2 · Why** — Why can two 10 kΩ resistors behave differently in a precision circuit?

<details><summary>Answer</summary>

They can differ in tolerance (1% vs 0.1%: initial error), temperature coefficient (e.g., 100 vs 25 ppm/°C: drift with temperature) and power rating (self-heating shifts the value). Material matters too: metal and thin film are more stable than carbon film.

</details>

**Q3 · Calc** — A 50 mΩ shunt carries 3 A. What is the voltage across it, the power, and which power rating would you choose?

<details><summary>Answer</summary>

V = I × R = 3 × 0.05 = 0.15 V (150 mV).
P = I² × R = 9 × 0.05 = 0.45 W.
With a 2× margin → choose a 1 W resistor.

</details>

**Q4 · Apply** — Why do high-current packs (e.g., 100 A) use very small shunts (0.1–1 mΩ), even though the signal becomes tiny?

<details><summary>Answer</summary>

Loss grows with I²: at 100 A, 1 mΩ burns 10 W; 0.1 mΩ burns 1 W. A smaller shunt means less heat and wasted energy, but the signal is only 10–100 mV, so the amplifier or ADC must have very low offset and noise. The trade-off is power loss vs signal size.

</details>

**Q5 · Explain** — Aloud, 60 s: why does a resistor's power rating matter? Use a number.

<details><summary>Answer</summary>

Model answer: "A resistor turns electrical energy into heat. If the heat is more than its rating, it overheats, drifts in value and can burn. For example, a 100 Ω resistor across 12 V dissipates 1.44 W. A 0.25 W resistor there is running at almost six times its rating, so it will fail."

</details>

## Wed 07 Oct · Topic of Tue 06 Oct: NumPy, image as a matrix

**Q1 · Recall** — A colour image has shape (480, 640, 3) and dtype uint8. What does each number mean, and what is the value range?

<details><summary>Answer</summary>

480 rows (height), 640 columns (width), 3 channels (B, G, R in OpenCV). uint8 → each value is 0–255.

</details>

**Q2 · Why** — Why does `np.array([250], dtype=np.uint8) + 10` give 4 instead of 260?

<details><summary>Answer</summary>

uint8 can only hold 0–255, so it wraps around: 260 − 256 = 4. In images this turns bright pixels dark. Fix: convert to int16 or float32 before the math, then clip to 0–255 and convert back to uint8.

</details>

**Q3 · Calc** — How many bytes is one 1920 × 1080 RGB uint8 image? And uncompressed video at 30 fps, per second?

<details><summary>Answer</summary>

1920 × 1080 × 3 = 6 220 800 bytes ≈ 6.2 MB. × 30 ≈ 187 MB/s. This is why cameras compress video and why embedded vision needs careful memory planning.

</details>

**Q4 · Apply** — In industrial inspection, why do you often convert images to grayscale first?

<details><summary>Answer</summary>

One channel instead of three: 3× less data and faster processing. Many defects (scratches, cracks, missing parts) show up as brightness changes, so colour adds little. Keep colour only when the defect is a colour difference (wrong wire colour, discolouration).

</details>

**Q5 · Explain** — Aloud, 60 s: explain to a non-engineer how a computer "sees" an image.

<details><summary>Answer</summary>

Model answer: "A computer sees an image as a grid of numbers. Each small square, called a pixel, has a brightness from 0 for black to 255 for white. A colour image has three grids: red, green and blue. Computer vision is maths on these numbers, for example finding places where the numbers change suddenly, which are edges."

</details>

## Thu 08 Oct · Topic of Wed 07 Oct: KVL, KCL, voltage dividers

**Q1 · Recall** — State KVL and KCL in one sentence each.

<details><summary>Answer</summary>

KVL: the sum of voltages around any closed loop is zero (energy conservation).
KCL: the current entering a node equals the current leaving it (charge conservation).

</details>

**Q2 · Why** — Why does a divider's output voltage change when you connect a load?

<details><summary>Answer</summary>

The load is in parallel with the bottom resistor, so the bottom resistance drops and the ratio changes. The divider has an output resistance of R1 ∥ R2; the load must be much larger (rule of thumb: 10–100×) to keep the error small. Next week's Thevenin topic explains this exactly.

</details>

**Q3 · Calc** — R1 = 100 kΩ (top), R2 = 240 kΩ (bottom), input 4.2 V. Find Vout and the current drawn from the cell.

<details><summary>Answer</summary>

Vout = 4.2 × 240 / (100 + 240) = 4.2 × 0.706 = 2.965 V.
I = 4.2 V / 340 kΩ ≈ 12.4 µA.

</details>

**Q4 · Apply** — A 4S Li-ion pack (max 16.8 V) must be read by a 3.3 V ADC. Choose a ratio and a pair of E24 resistor values.

<details><summary>Answer</summary>

Target ≤ ~3.0 V at 16.8 V → ratio ≤ 0.179.
Example: R1 = 470 kΩ, R2 = 100 kΩ → ratio 100 / 570 = 0.175 → 16.8 V becomes 2.95 V.
Drain: 16.8 / 570 k ≈ 29.5 µA. Source impedance: 470 k ∥ 100 k ≈ 82.5 kΩ → add a capacitor at the ADC pin.

</details>

**Q5 · Explain** — Aloud, 60 s: why can't a BMS connect a 4.2 V cell directly to a 3.3 V microcontroller ADC pin?

<details><summary>Answer</summary>

Model answer: "The ADC pin only accepts voltages up to its supply, about 3.3 V. A full cell is 4.2 V, which is out of range: the reading saturates, and the pin's protection diodes conduct, which can damage the microcontroller or drain the cell. So we scale the voltage down with a divider and keep the maximum below 3.3 V with some headroom."

</details>

## Fri 09 Oct · Topic of Thu 08 Oct: grayscale from scratch

**Q1 · Recall** — What formula does OpenCV use to convert colour to grayscale?

<details><summary>Answer</summary>

Y = 0.299 R + 0.587 G + 0.114 B (ITU-R BT.601 weights).

</details>

**Q2 · Why** — Why does green get the biggest weight?

<details><summary>Answer</summary>

Human eyes are most sensitive to green light, so green contributes most to perceived brightness. Equal weights (a plain average) make blue areas look too bright.

</details>

**Q3 · Calc** — An OpenCV pixel is [B, G, R] = [200, 100, 50]. What is its gray value?

<details><summary>Answer</summary>

Y = 0.299 × 50 + 0.587 × 100 + 0.114 × 200 = 14.95 + 58.7 + 22.8 = 96.45 → 96.
Trap: OpenCV order is BGR, so R = 50, not 200. Mixing the order gives about 124, which is wrong.

</details>

**Q4 · Apply** — Your grayscale differs from `cv2.cvtColor` by 1 in some pixels. Is your code wrong?

<details><summary>Answer</summary>

Probably not. OpenCV uses fixed-point integer maths with its own rounding; your float version may round 96.5 differently. Rule: max difference ≤ 1 = rounding; bigger = a bug (often BGR/RGB mix-up or uint8 overflow). This is how you validate against a reference.

</details>

**Q5 · Explain** — Aloud, 60 s: what does "validate against a reference implementation" mean, and why do you do it?

<details><summary>Answer</summary>

Model answer: "I write my own version of an algorithm, then run a trusted version, like OpenCV, on the same input. I compare the outputs with a number, such as the maximum pixel difference. If they match, I know I understood the algorithm. If not, the difference shows me where my understanding or my code is wrong."

</details>

## Sat 10 Oct · Topic of Fri 09 Oct: Li-ion cell basics

**Q1 · Recall** — Give the typical voltage window of NMC and LFP cells (max, nominal, min).

<details><summary>Answer</summary>

NMC: 4.2 V max · 3.6–3.7 V nominal · 2.5–3.0 V min.
LFP: 3.65 V max · 3.2–3.3 V nominal · 2.0–2.5 V min.
Always check the specific cell's datasheet.

</details>

**Q2 · Why** — Why is SOC from voltage much harder for LFP than for NMC?

<details><summary>Answer</summary>

LFP's OCV curve is very flat in the middle (about 1–2 mV per 1% SOC), so small measurement errors become big SOC errors. NMC is steeper (about 6–7 mV per 1% SOC). LFP also has hysteresis: its OCV differs after charging vs after discharging.

</details>

**Q3 · Calc** — A 3000 mAh cell is discharged at 1.5 A. What is the C-rate, and roughly how long will it last?

<details><summary>Answer</summary>

C-rate = 1.5 A / 3 A = 0.5C. Time ≈ 3 Ah / 1.5 A = 2 h. Real capacity is a bit lower at higher currents and low temperatures.

</details>

**Q4 · Apply** — Why don't phones and EVs show SOC as simply "the measured voltage"?

<details><summary>Answer</summary>

Under load, terminal voltage = OCV − I × R (plus polarisation). The voltage drops when you accelerate and recovers when you stop, so a voltage-only SOC would jump around. Real BMSs combine coulomb counting (integrating current) with OCV corrections at rest, plus temperature and aging compensation.

</details>

**Q5 · Explain** — Aloud, 60 s: explain SOC with the 4-line template (definition, why it matters, core idea, example).

<details><summary>Answer</summary>

Model answer: "SOC tells how much charge is left in a battery, as a percentage, like a fuel gauge. It matters because the BMS uses it to prevent over-charge and over-discharge and to predict range. It is estimated from current, voltage and temperature, often by combining coulomb counting with the cell's OCV curve. For example, an EV uses SOC to show remaining range and to limit power when the battery is nearly empty."

</details>

## Sun 11 Oct · Topic of Sat 10 Oct: bench lab, cell voltage with the STM32 ADC

**Q1 · Recall** — For a 12-bit ADC with a 3.3 V reference, what is 1 LSB in mV? How do you convert a raw count to volts?

<details><summary>Answer</summary>

12 bits = 4096 codes → 1 LSB = 3.3 / 4096 ≈ 0.806 mV.
V = raw × Vref / 4095 (ST's reference manuals use 4095 as full scale). Be consistent and write down which one you use.

</details>

**Q2 · Why** — Your ADC reads 20 mV lower than the multimeter. List three possible error sources.

<details><summary>Answer</summary>

1. Reference error: VDDA is not exactly 3.3 V (regulator ±1–2%).
2. Divider ratio error: resistor tolerance; use measured values in the calculation.
3. High source impedance: the ADC's sampling capacitor doesn't fully charge; add a capacitor at the pin or increase the sampling time.
Others: ADC offset/gain error, noise (average more samples), the multimeter's own accuracy.

</details>

**Q3 · Calc** — Raw ADC = 3680 (12-bit, 3.3 V reference), divider ratio 0.706. What is the cell voltage?

<details><summary>Answer</summary>

V_adc = 3680 × 3.3 / 4095 ≈ 2.966 V.
V_cell = 2.966 / 0.706 ≈ 4.20 V.

</details>

**Q4 · Apply** — Why do many BMS products calibrate each channel, or use factory-trimmed ICs?

<details><summary>Answer</summary>

Resistor, reference and ADC gain/offset errors add up to more than the accuracy target (a few mV). Measuring a known precise voltage and storing a gain/offset correction per channel removes most of this cheaply, which is cheaper than using ultra-precise parts everywhere. The trade-off is hardware precision vs calibration time and software.

</details>

**Q5 · Explain** — Aloud, 60 s: describe yesterday's experiment in 4 sentences: goal, setup, result, lesson.

<details><summary>Answer</summary>

Template: "My goal was to measure a Li-ion cell's voltage with an STM32 ADC and compare it with a multimeter. I used a __ k / __ k divider and logged readings to Python over UART. The ADC read about __ mV [higher / lower] than the meter. The main cause was __, so next I will __."

</details>
