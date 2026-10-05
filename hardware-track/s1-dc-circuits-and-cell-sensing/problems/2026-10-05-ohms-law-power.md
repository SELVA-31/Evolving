# Problems · Mon 05 Oct · Ohm's law, power, resistor specs

Solve by hand first. Then open the answer. Write wrong ones in your journal.

**1.** A 3.3 V GPIO drives an LED (forward voltage 2.0 V) at 5 mA. Find R and the nearest E24 value.

<details><summary>Answer</summary>

R = (3.3 − 2.0) / 0.005 = 260 Ω → nearest E24 = 270 Ω (current ≈ 4.8 mA).

</details>

**2.** 12 V is across a 4.7 kΩ resistor. Find the current and the power.

<details><summary>Answer</summary>

I = 12 / 4700 = 2.55 mA. P = 12² / 4700 = 30.6 mW.

</details>

**3.** A 100 Ω resistor is rated 0.25 W. What are the maximum voltage and current?

<details><summary>Answer</summary>

V = √(P × R) = √25 = 5 V. I = 5 / 100 = 50 mA.

</details>

**4.** You discharge a 4.2 V cell through 4.7 Ω. Find current, power, and a safe power rating.

<details><summary>Answer</summary>

I = 4.2 / 4.7 = 0.89 A. P = 4.2² / 4.7 = 3.75 W. With 2× margin → 10 W resistor.

</details>

**5.** A 10 mΩ shunt carries 5 A. Find the voltage across it, the power, and a rating.

<details><summary>Answer</summary>

V = 5 × 0.01 = 50 mV. P = 5² × 0.01 = 0.25 W. Choose ≥ 0.5 W (1 W is common).

</details>

**6.** What is the allowed range of a 100 kΩ resistor at 1%? At 0.1%?

<details><summary>Answer</summary>

1%: 99 – 101 kΩ. 0.1%: 99.9 – 100.1 kΩ.

</details>

**7.** A 10 kΩ resistor has a tempco of 100 ppm/°C. It heats from 25 °C to 75 °C. How much does R change? Repeat for 25 ppm/°C.

<details><summary>Answer</summary>

ΔR = 10 000 × 100 × 10⁻⁶ × 50 = 50 Ω (0.5%). At 25 ppm/°C: 12.5 Ω (0.125%).

</details>

**8.** A cable has 50 mΩ total resistance and carries 10 A from a 12 V pack. Find the voltage drop and the power lost.

<details><summary>Answer</summary>

V = 10 × 0.05 = 0.5 V (4.2% of 12 V). P = 10² × 0.05 = 5 W of heat in the cable.

</details>

**9.** A load draws 2 W for 30 minutes. How much energy is that in joules and in Wh?

<details><summary>Answer</summary>

E = 2 W × 1800 s = 3600 J = 1 Wh.

</details>

**10.** You calculate that you need 3.4 kΩ. What is the nearest value in E24 and in E96, and the % error of the E24 choice?

<details><summary>Answer</summary>

E24: 3.3 kΩ → error = (3.3 − 3.4) / 3.4 = −2.9%. E96: 3.40 kΩ (exact). Lesson: the E-series you buy from limits how exact your design can be.

</details>
