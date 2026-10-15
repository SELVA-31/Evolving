# Post pack · Mon 19 Oct 2026 · 1.2 Power architecture: LDO circuits and buck / boost regulators

Prompt: `../POST-PROMPT.md` · Lane: analog / BMS · Format: numbers · Material: W1 TP4056 module, P1 LDO decision

---

## Part 1 · The learning module

### Core concepts, practically

**A linear regulator (LDO) is a resistor that adjusts itself.** It drops Vin − Vout across a pass transistor and turns that drop into heat: P = (Vin − Vout) × Iout, plus Iq × Vin. Efficiency is roughly Vout / Vin: 5 V → 3.3 V is 66 %; 12 V → 3.3 V is 27 %. It is quiet, cheap, needs two capacitors, and is the right choice whenever that heat is small.

**A buck converter is a switch and a filter.** It chops Vin at 0.5–2 MHz and lets an inductor + capacitor average it down to Vout. Efficiency 85–95 % almost regardless of ratio. Costs: an inductor, more board area, switching noise, and a layout that must be done right. A **boost** does the opposite (Vout > Vin); its input current is Iout × Vout / (Vin × η), so a 3.7 V → 5 V, 1 A boost pulls about 1.5 A from the cell.

**The decision is arithmetic, not taste:**
1. Compute P_loss = (Vin_max − Vout) × Iout_max.
2. Estimate the junction temperature: Tj = Ta + P × θJA (θJA from the datasheet for your copper area).
3. If Tj ≤ ~105 °C at the hottest ambient you will see: LDO. Otherwise: lower the current, add copper, or switch to a buck.
4. Then check the **other end**: at Vin_min, is Vin_min ≥ Vout + Vdropout(Imax) + 0.2 V? If not, the LDO falls out of regulation long before the battery is empty or the USB port sags.

**Two-stage rails** are common in mixed-signal boards: a buck brings 12 V down to 3.6–5 V efficiently, then an LDO makes the clean 3.3 V for the ADC and radio. The LDO's noise rejection (PSRR) falls at high frequency, so the buck's switching frequency still needs an output filter or a ferrite.

### Industry values and rules of thumb

| Rule | Value |
|---|---|
| LDO efficiency | ≈ Vout / Vin |
| Buck efficiency | 85–95 % |
| Move from LDO to a switcher when | P_loss > ~0.5 W (SOT-23 / SOT-89), > ~1 W (SOT-223 or SOP-8 with ~1 cm² copper), or Vin / Vout > ~2 |
| θJA, small packages | SOT-23 ≈ 200 °C/W · SOT-223 ≈ 60–90 °C/W on minimal copper, ≈ 40–50 °C/W with ~6 cm² · SOP-8 with exposed pad ≈ 50–70 °C/W with vias to a bottom pour |
| Design limit | Tj ≤ 105 °C (abs max usually 125 °C) |
| Dropout margin | Vin_min ≥ Vout + Vdo(Imax) + 0.2–0.3 V |
| USB low line at the device | 4.4–4.75 V after cable drop: pick an LDO with Vdo ≤ 0.4 V at the load current for 5 V → 3.3 V |
| Li-ion cell to 3.3 V | Cell is 3.0–4.2 V: an LDO with Vdo ≥ 0.5 V loses the bottom 30 % of the charge; use a ≤ 0.2 V dropout LDO, a buck-boost, or run the MCU at 3.0 V |
| Quiescent current | 1–2 µA (MCP1700 class) vs 5 mA (AMS1117 class): 1000× difference in standby battery life |
| Buck inductor | Ripple current 20–40 % of Iout; Isat ≥ 1.3 × Ipeak; low DCR |
| Buck layout | Input ceramic within 2–3 mm of VIN / GND pins; hot loop (Cin → switch → diode or low-side FET → Cin) as small as possible; feedback divider at the FB pin, trace away from the inductor and switch node |
| Ceramic capacitors | X5R / X7R lose 30–70 % of capacitance at rated DC bias; a 10 µF 0603 at 5 V may be 4 µF. Use 0805 or two in parallel for Cout |
| Indicator LED | 1–2 mA is enough; do not spend 20 mA of a 500 mA budget on a light |

### Common mistakes

| Mistake | What happens | Fix |
|---|---|---|
| Choosing the LDO by current rating only | AMS1117 at 12 V in, 3.3 V, 0.5 A = 4.35 W: dies or throttles | Do the P_loss arithmetic first; use a buck above ~1 W |
| Ignoring dropout at low line | 3.3 V LDO with 1.1 V dropout on a 4.5 V USB port: output sags, MCU brown-outs at Wi-Fi peaks | Choose Vdo ≤ 0.4 V at Imax, or test at 4.4 V |
| Battery device with a 1 V-dropout LDO | Device "dies" at 3.9 V with 40 % charge left | Low-dropout LDO, buck-boost, or lower rail |
| Buck feedback trace routed under the inductor | Output jitters, regulator unstable, hard to debug | FB trace short, on the quiet side, away from SW node |
| Input capacitor far from the switcher | Large hot loop: ringing, EMI, failed radiated tests | Cin at the pins, GND return directly under the IC |
| Inductor picked by inductance only | Saturates at load peaks, output drops, inductor heats | Check Isat and DCR against Ipeak |
| Thermal pad not connected to copper | Datasheet θJA never achieved; part runs 30–50 °C hotter | Pour under the pad + 4–9 vias to the bottom pour |
| Old LDO with ceramic-only output cap | Oscillates (needs ESR), or the reverse with a modern part | Follow the stability section of the datasheet, not habit |
| Enable pin left floating | Random power-up, works on the bench, fails in the field | Tie EN to VIN or drive it |
| Two sources (USB + battery) without a power path | Backfeed into the charger or the USB port | Ideal diode, power-path IC, or at least a Schottky with its drop budgeted |

### How a testing / ATE background helps here

- **You already run low-line and high-line tests** on finished products. Run the same test on the schematic: evaluate the LDO at 4.4 V and 5.25 V, and at the load current the Wi-Fi burst actually draws, before buying parts.
- **Thermal soak is a standard station step.** Put a thermocouple pad or a spot for an IR reading on the regulator in your own layout, and record case temperature at full load during bring-up. θJA from the datasheet is a starting point; your number is the truth.
- **Test points on every rail and on the enable pin** cost nothing and turn the rail-sequencing check into a 2-minute scope capture instead of probing a 0402 capacitor.
- **Load steps:** fixtures switch loads on and off all day. Do the same to your rail: a 0 → 300 mA step shows the regulator's transient response and whether the output capacitor is big enough after DC-bias derating.

### Apply this week

- TP4056 module (W1): 5 V in, 3.7 V cell, 1 A → 1.3 W in an SOP-8. At ≈ 60 °C/W that is ≈ 78 °C above ambient, so the IC's thermal regulation (≈ 120 °C die) throttles the current. Compute the 0.6 A case (R_PROG = 2 kΩ → ≈ 0.8 W). If you have a thermometer, measure the module at both currents.
- P1 LDO (W2): compare two candidates on dropout at 500 mA, Iq, Cout requirement, θJA, Basic / Extended. Write the Tj at 5 V in and 45 °C ambient in the justification table.

---

## Part 2 · The LinkedIn post

Replace every `[bracket]` with your measured value or delete the line. Do not publish a bracket.

> A ₹60 Li-ion charger module taught me where linear regulators stop making sense.
>
> This week I redrew the TP4056 charger board from scratch in EasyEDA Pro, part by part, as a self-set exercise. The surprise was not the circuit. It was the arithmetic.
>
> 5 V in, 3.7 V cell, 1 A charge current: (5 − 3.7) × 1 = 1.3 W of heat in an SOP-8. At roughly 60 °C/W, that is a die near 100 °C on a 25 °C bench. The IC survives by throttling the current. The chip is protecting itself from the board.
>
> [Measured: my module reached __ °C at 1 A and __ °C at 0.5 A.]
>
> The same three lines now decide every power rail I design:
> • P = (Vin − Vout) × I, before choosing the package.
> • Under ~0.5 W in a small package: LDO. Above ~1 W: switcher, or more copper and less current.
> • Check dropout at the lowest input you will really see: a USB port at 4.4 V, a cell at 3.4 V.
>
> From test-fixture work I already run low-line and thermal checks on finished products. Doing the same calculation at the schematic stage is cheaper than finding it with a thermocouple.
>
> Which regulator surprised you with heat you had not calculated?
>
> #HardwareDesign #PCBDesign #PowerElectronics #IoT #EmbeddedSystems

**Visual ideas (pick one):**
1. A 3-row table image: AMS1117 at 12 V / 0.5 A (4.35 W) · TP4056 at 5 V / 1 A (1.3 W) · a buck at 12 V / 0.5 A (≈ 0.2 W loss), each with the estimated temperature rise.
2. A thermal or IR-thermometer photo of the module charging at 1 A next to the same module at 0.5 A, temperatures written on the image.
3. A crop of your redrawn schematic with "P = (Vin − Vout) × I = 1.3 W" annotated at the IC.

**Before publishing:** brackets gone · θJA checked against the TP4056 datasheet · ≤ 200 words · one image · the question stays at the end.
