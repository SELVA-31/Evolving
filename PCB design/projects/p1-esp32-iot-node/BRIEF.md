# P1 · ESP32-C3 IoT sensor node · requirement sheet

Weeks: W2 (schematic + library) → W3 (PCB + outputs). Graded with `../../REVIEW-CHECKLIST.md`.
Read this like a customer spec. Where it says *you decide*, you decide and you write the reason in the justification table.

## 1. Purpose

Indoor temperature / humidity node, USB-powered, Wi-Fi to MQTT, with one switched 12 V load (fan or valve). The kind of node you integrate at work, designed by you this time.

## 2. Requirements

| # | Requirement | Notes |
|---|---|---|
| R1 | **Power in:** USB-C receptacle (16-pin, USB 2.0 only), 5 V, ≤ 1 A | CC1 and CC2 each pulled down with 5.1 kΩ (why?). ESD protection on D+ / D−. Reverse-polarity protection not required (why not?). |
| R2 | **3.3 V rail:** LDO, ≥ 600 mA continuous | ESP32-C3 Wi-Fi peaks ≈ 350 mA. *You decide* the LDO: justify dropout at 500 mA, Iq, Cin / Cout per its datasheet, package, Basic / Extended. Power LED with a current you justify (≤ 2 mA is enough for an indicator). |
| R3 | **MCU:** ESP32-C3 module (MINI-1 or WROOM-02) | Native USB (D− on GPIO18, D+ on GPIO19) for programming. EN with RC per Espressif guidelines; BOOT button on GPIO9; RESET button. Handle every strapping pin per the Espressif hardware design guidelines. Antenna at a board edge with the keep-out the module datasheet specifies. |
| R4 | **Sensor:** I²C temperature + humidity | *You decide*: SHT40 / AHT20 / BME280. Pull-ups: value and whether the module already has them. Place the sensor away from the LDO and MCU heat (how far? why?). |
| R5 | **Expansion:** Qwiic-style I²C header | JST-SH 1.0 mm 4-pin (3.3 V, GND, SDA, SCL) or 4-pin 2.54 mm header — *you decide*, justify. |
| R6 | **Output:** 1 low-side N-MOSFET switch, 12 V / 1 A external load | 12 V arrives on a 2-pin screw terminal; load on another 2-pin terminal. Gate resistor, gate pull-down, flyback diode footprint (fit or DNP?), status LED. MOSFET must be fully on at 3.3 V gate (which spec tells you?). |
| R7 | **UI:** 1 user LED on a GPIO, BOOT + RESET buttons | |
| R8 | **Testability (ATE habit):** test points on 5 V, 3.3 V, GND, SDA, SCL, TX, RX | Labelled on silkscreen. |
| R9 | **Mechanical:** ≤ 50 × 50 mm, 2-layer, 4 × M3 mounting holes (3.2 mm) with keep-out, USB-C on an edge, board name + version on silkscreen | JLCPCB 2-layer capabilities. |
| R10 | **BOM:** JLCPCB **Basic** parts wherever possible; every part has an LCSC number; DNP marked; ≤ 30 BOM lines | |

## 3. Deliverables

| Week | Deliverable |
|---|---|
| W2 | Block diagram (paper photo is fine) · multi-page schematic (power / MCU / IO) with Net Ports · 2 custom devices from datasheets (the USB-C receptacle and the sensor, or the module if the library part is weak) · schematic DRC = 0 · BOM with LCSC numbers · justification table |
| W3 | PCB: outline, rules + net classes, placement, routing, GND pour, DRC = 0, silkscreen, 3D · Gerber + drill opened in a viewer · BOM + pick-and-place · review packet |

## 4. Answer these before you draw (write them in `P1-notes.md`)

1. Current budget: module peak + sensor + LEDs + MOSFET gate → LDO rating and dissipation at 5 V in.
2. Why 5.1 kΩ on CC1 and CC2, and why both.
3. Which ESP32-C3 pins are strapping pins, and what state each must have at reset.
4. Where does the antenna go, and what must not be under or beside it.
5. Which ESD part for USB, and where it sits on the board (hint: between connector and MCU, near the connector).
6. Why Basic parts: what does an Extended part cost at assembly.
7. What the 100 nF caps are for, and where each one must sit on the PCB.

## 5. P1-specific review rows (added to the 100-point checklist)

| Check | Verify |
|---|---|
| Antenna keep-out region exists and is empty of copper and parts | Prohibited Region in PCB |
| EN has the RC and the reset button; BOOT on GPIO9 with pull-up | Schematic walk-through vs Espressif guidelines |
| USB D+ / D− routed as a pair, short, ESD part near the connector | PCB top view |
| LDO input cap and output cap at the pins; thermal copper under the LDO if the package needs it | PCB top view, 3D |
| MOSFET gate resistor + pull-down; flyback diode footprint present | Schematic |
| Sensor placed away from heat sources, with a thermal slot or isolation if you can justify it | PCB top view |

## 6. Justification table (template)

| Ref | Part | Why this part | Key number | Alternative considered |
|---|---|---|---|---|
| U1 | | | | |
| U2 | | | | |
| … | | | | |

## 7. Hints (not answers)

- Espressif publishes a reference schematic in the ESP32-C3 hardware design guidelines. Read it, do not copy it; every part you keep gets a reason.
- The module datasheet gives a recommended PCB layout with the antenna keep-out drawn. Use that drawing for R3.
- For the LDO decision, compare at least two candidates on: dropout at 500 mA, Iq, Cout requirement, thermal resistance, Basic / Extended.
