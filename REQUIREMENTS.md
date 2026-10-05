# Requirements · Practical sessions

Buy in phases. "Needed from" = the week you first use it.

⚠️ **Li-ion safety:** fuse in series with every cell · current-limited supply · never short terminals · never charge unattended · non-flammable surface · open only low-voltage battery devices, never mains-powered ones.

---

## A. Bench instruments

| Item | Spec to look for | Needed from | Why |
|---|---|---|---|
| Digital multimeter | ≥ 6000 counts, mV + µA ranges, continuity, fused current inputs | W0 | Your reference for every measurement |
| Bench power supply | 0–30 V, 0–3 A or more, adjustable current limit | W0 | Safe testing; can stand in for a cell |
| Soldering iron | Temperature-controlled + solder, flux, wick | W0 | Headers, modules, wires |
| Breadboards ×2, jumper wires, crocodile-clip leads | — | W0 | Prototyping |
| Thermometer | DMM thermocouple or IR thermometer | S3 (W5) | MOSFET and cell temperature |
| Second multimeter | Any basic one | S4 (W8) | Voltage and current at the same time in the discharge test |
| Oscilloscope *(recommended)* | 2 ch, ≥ 20 MHz; budget: handheld / USB scope | S3 (W6) | Gate / switching waveforms, noise. The STM32 ADC can replace it for slow signals |
| Electronic load *(optional, very useful)* | Constant current, cut-off voltage, mAh reading (e.g., DL24-type) | S4 (W8) | Ground-truth capacity for coulomb counting |
| USB logic analyzer *(optional)* | 8 ch, 24 MHz + PulseView | S4 (W8) | Debug UART / I²C (INA226, BQ76920) |
| USB power meter *(optional)* | V, A, mAh | — | Charging current into cells |

## B. Battery + safety

| Item | Qty | Needed from | Note |
|---|---|---|---|
| 18650 Li-ion cells, NMC, genuine brand (Samsung, LG, Molicel, Murata) | 4 | W1 | Avoid fake "9900 mAh" cells; 4 cells allow a 3S/4S test pack later |
| LFP cell (26650 or 32650 LiFePO₄) *(optional)* | 1 | S2 | Compare the flat LFP OCV curve with NMC |
| 18650 holders: 1-cell with wires ×4, 4-cell ×1 | — | W1 | Never solder directly onto cells |
| Inline fuse holders + fuses (1 A, 3 A, 5 A) | 3 + spares | W1 | Mandatory in series with any cell |
| TP4056 charger module **with** protection (DW01A + FS8205A) | 3 | W1 | Charger now; teardown object in S3 |
| Cheap 3S or 4S BMS protection board | 1 | S3 | Reverse-engineering study |
| Ceramic tile / metal tray + LiPo safe bag | 1 | W1 | Where cells are charged and tested |

## C. Components

### Passives

| Item | Needed from |
|---|---|
| Resistor kit: metal film, 1%, E24, 10 Ω – 1 MΩ | W0 |
| Trimmer potentiometers 10 kΩ | W1 |
| Precision resistors 0.1% (2–4 values for your divider; recalculate the ratio with values you can buy) | W2 |
| Ceramic capacitor kit 10 pF – 1 µF (include C0G/NP0 **and** X7R) | S2 |
| Electrolytic capacitor kit 1 – 1000 µF | S2 |
| Inductors: 10 µH, 100 µH, 1 mH | S2 |
| Power resistors: 4.7 Ω 10 W, 2.2 Ω 25 W aluminium-clad + heatsink | S2 (pulse test) |
| Shunt resistors: 10 mΩ, 50 mΩ, 100 mΩ, 1%, 1–3 W | S4 |
| NTC thermistors 10 kΩ (B ≈ 3435 or 3950) | S4 |

### Semiconductors

| Item | Needed from |
|---|---|
| LEDs, assorted | W0 |
| Diodes: 1N4148, 1N4007, 1N5819 (Schottky) | S3 |
| Zener diodes: 3.3 V, 5.1 V | S3 |
| TVS diodes (P6KE / SMBJ series; standoff voltage above your pack max) | S3 |
| BJTs: BC547 (NPN) + BC557 (PNP), or 2N2222 + 2N2907 | S3 |
| N-MOSFET with Rds(on) specified at Vgs ≤ 2.5 V (e.g., AO3400A) | S3 |
| P-MOSFET (e.g., AO3401A) | S3 |
| SOT-23 and SOIC → DIP adapter boards | S3 |

### ICs and modules

| Item | Needed from | Lesson |
|---|---|---|
| Op-amps: LM358 **and** MCP6002 | S4 | Classic vs rail-to-rail: compare them on the bench |
| INA226 module (I²C) | S4 | Integrated current / voltage monitor |
| DS18B20 temperature sensor | S4 | Reference to validate your NTC circuit |
| TL431 + LM4040 (2.5 V or 4.096 V) | S5 | Voltage references for the ADC |
| AMS1117-3.3 **and** MCP1700-3.3 | S5 | Same job, ~1000× different quiescent current |
| Buck module (MP1584 or LM2596) | S5 | LDO vs buck efficiency |
| BQ76920 EVM / breakout *(optional)* | S6 | S6 is design-only unless you order a PCB |

## D. Microcontroller boards

| Item | Needed from | Note |
|---|---|---|
| STM32 board | W0 | See note below |
| ESP32 dev board | S6 *(optional telemetry)* | Wi-Fi/BLE. Its ADC is non-linear: don't use it for precision measurement |
| ST-LINK V2 + USB-UART adapter (CP2102 / CH340) | W0 | Only if you have a Blue Pill |

**STM32 note:** Nucleo boards (e.g., F401RE, G431RB, L476RG) include the ST-LINK programmer, a USB virtual COM port, and a factory **VREFINT calibration** value. The Blue Pill (STM32F103) needs a separate ST-LINK and USB-UART and has **no** factory VREFINT calibration value: calibrate against your multimeter or use an external reference. Both work; Nucleo is easier for measurement work.

## E. Computer vision hardware

| Item | Needed from |
|---|---|
| Webcam (laptop camera is fine to start; USB webcam with manual focus / exposure is better) | W1 |
| Controllable lighting: desk lamp, LED strip or ring light | S3 |
| Phone / webcam stand or tripod (fixed camera position) | S3 |
| Printed checkerboard + ruler (calibration targets) | S3 |
| Old PCBs, coins, washers (objects to measure and inspect) | S3 |
| ESP32-CAM (OV2640) *(optional)* | S6 |

## F. Software (all free)

| Tool | Needed from |
|---|---|
| Python 3.13 (installed) + `pip install numpy matplotlib pandas scipy opencv-python pyserial jupyter` | W0 |
| VS Code + Python and Jupyter extensions | W0 |
| Git (installed) + GitHub account | W0 |
| LTspice | W1 |
| EasyEDA (Std or Pro) | W1 |
| STM32CubeIDE (+ STM32CubeProgrammer) | W0 |
| Arduino IDE 2 (for ESP32) | S6 |
| Anki desktop (to import question decks) | W0 |
| PyTorch (CPU): `pip install torch torchvision` | S5 |
| PulseView (only with a logic analyzer) | S4 |

## G. Datasets (download when needed)

| Dataset | Needed from |
|---|---|
| DeepPCB (PCB defects, template + test pairs) | W7 |
| CALCE battery data (University of Maryland) | W9 |
| NEU surface defect database (NEU-CLS) | W10 |

## H. Phone

| App | Use |
|---|---|
| AnkiDroid (Android, free) / AnkiMobile (iPhone, paid) or AnkiWeb in browser (free) | Daily 5 questions, works offline |
| GitHub mobile app | Read plans and Q&A files |
| Falstad circuit simulator (falstad.com/circuit, in browser) | Play with circuits anywhere |
| Voice recorder | Q5 "explain aloud" answers |
| PDF reader | Datasheets and app notes offline |
