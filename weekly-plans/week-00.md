# Week 0 · Thu 01 – Sun 04 Oct 2026 · Setup

**Goal:** Tools installed, bench ready, first data flowing from STM32 to Python, habits running.
**Daily 5:** 📱 `daily-qa/week-00.md`
**Where:** 📱 phone · 💻 laptop · 🔧 bench

---

## Thu 01 Oct · Setup + electrical basics

| Block | Task |
|---|---|
| 📱 Learn (60) | Charge, voltage, current, resistance, their units. How a multimeter measures V, I and R. Source: All About Circuits Vol. I, first chapters. |
| 💻 Do (75) | Install everything in `REQUIREMENTS.md` section F (CubeIDE is a large download: start it first). Create a GitHub account/repo for this folder. |
| 📱 Check (30) | Daily 5: baseline check (answer honestly; it's your starting point). |
| 📱 Log (15) | First journal entry: `journal/2026-10-01.md` from `journal/TEMPLATE.md`. |

## Fri 02 Oct · Math toolkit + Python basics

| Block | Task |
|---|---|
| 📱 Learn (60) | SI prefixes (p, n, µ, m, k, M), scientific notation, rearranging equations, percent error, slope of a graph. |
| 💻 Do (75) | Python: variables, lists, loops, functions, f-strings. Write `adc_to_volts(raw, vref=3.3, bits=12)` and `percent_error(measured, true)`. Plot a straight line with matplotlib. Save in `cv-track/s1-images-as-arrays/python/basics.py`. |
| 📱 Check (30) | 10 unit-conversion problems; verify with Python. |
| 📱 Log (15) | Journal + commit. |

## Sat 03 Oct · Bench day 0

| Block | Task |
|---|---|
| 📱 Learn (45) | Multimeter modes and safety (never measure current in parallel). Breadboard internal connections. Resistor colour code. Li-ion safety rules (top of `REQUIREMENTS.md`). |
| 🔧 Do (105) | 1. Measure 10 resistors: colour code vs measured vs tolerance → table. 2. Continuity test on breadboard rows. 3. Measure a cell (or bench supply) voltage. 4. STM32: blink an LED, then send `hello` over UART and read it in Python with `pyserial`. |
| 💻 Check (15) | Are all resistors within tolerance? Compute % error in Python. |
| 📱 Log (15) | Journal + photo of your setup. |

## Sun 04 Oct · Habits + documentation

| Block | Task |
|---|---|
| Catch-up | Finish anything pending from Thu–Sat first. |
| Do | 1. Anki: import `daily-qa/anki/week-00.csv` + `week-01.csv`, set **New cards/day = 5**, sync to phone. 2. Update `README.md` progress. 3. Start `english/phrase-bank.md`. 4. Draft LinkedIn post #1: *"Starting a 12-week public engineering lab notebook: why analog, BMS and computer vision together."* |
| Review | What took longer than planned? Adjust next week. |
| Check-in | Send the Sunday check-in (ROADMAP §8) to Claude. |
