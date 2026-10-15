# Master checklist · 16 topics → weeks, projects, EasyEDA Pro features, posts

Source: the "PCB Hardware Design Master Checklist" (4 phases) shared on 15 Oct 2026.
Each topic is **learned in a week, practised on a project, and becomes one post pack** (learning module + LinkedIn post) made with `linkedin/POST-PROMPT.md`. Phase 2 names Altium / Cadence; the EasyEDA Pro equivalents are listed.

## Phase 1 · Schematic capture & system architecture

| # | Topic | Learn | Practise on | EasyEDA Pro feature / bench | Post | Pack |
|---|---|---|---|---|---|---|
| 1.1 | Component selection: MCU (ESP32 / STM32), matching voltage, footprint, availability | W2 | P1: module, LDO, sensor choice; justification table | Library search with Basic / Extended filter · BOM Preview and Price · Alternative Devices panel | Thu 22 Oct | ⬜ |
| 1.2 | Power architecture: LDO circuits, buck / boost regulators | W1–W2 (linear: TP4056, P1 LDO) · W4 (buck in P2) | W1 module thermal calc · P1 LDO · P2 buck | Circuit Calculator · Copper Manager (thermal copper) · Suture Vias under thermal pads | Mon 19 Oct | ✅ `linkedin/posts/2026-10-19-power-architecture.md` |
| 1.3 | BOM lifecycle: active, obsolete, long-lead parts | W2 | P1 BOM: LCSC numbers, alternates column, Basic vs Extended | BOM export · Order Parts · Alternative Devices | Thu 29 Oct | ⬜ |
| 1.4 | Circuit protections: ESD, TVS, reverse polarity | W2 (P1 USB) · W4 (P2 power path) | P1 USB-C ESD array · P2 reverse / backfeed protection | — | Mon 26 Oct | ⬜ |

## Phase 2 · PCB layout & high-speed routing

| # | Topic | Learn | Practise on | EasyEDA Pro feature / bench | Post | Pack |
|---|---|---|---|---|---|---|
| 2.1 | Layer stackup: 4 / 6 layers, ground and power planes | W5 | P3 (4-layer) | Layer Manager · Stack Table | Mon 16 Nov | ⬜ |
| 2.2 | Impedance control: 50 Ω single-ended, 90 / 100 Ω differential (USB) | W5 | P3 USB D+ / D− | Differential Pair Manager + Routing · Equal Length Tuning · JLCPCB impedance calculator for the stackup | Thu 19 Nov | ⬜ |
| 2.3 | IoT & RF layout: antenna clearance zones, matching networks | W3 | P1 ESP32-C3 antenna keep-out | Prohibited Region · module datasheet layout drawing | Mon 9 Nov | ⬜ |
| 2.4 | Constraint management: DRC clearance and spacing rules | W3 | P1 rules **before** routing | Design Rule · Net Class Manager · Check DRC (Custom) | Thu 5 Nov | ⬜ |

## Phase 3 · DFx & manufacturing

| # | Topic | Learn | Practise on | EasyEDA Pro feature / bench | Post | Pack |
|---|---|---|---|---|---|---|
| 3.1 | Advanced DFT: test pad sizing and grid alignment for bed-of-nails | W5 | P3 pogo test points on a 2.54 mm grid, ≥ 1.0 mm pads | Test Point · Test Point Report · IPC-D-356A export | Mon 23 Nov | ⬜ |
| 3.2 | DFM: panelization, fiducials, solder-mask clearance, thermal reliefs | W4 (thermal relief, P2) · W5 (panel, P3) | P2 pour settings · P3 panel ×2 with rails + fiducials | Panelize / Advanced Panelize · copper thermal-relief settings · PCB Setting (mask expansion) · JLCPCB SMT Selection Tool | Thu 12 Nov | ⬜ |
| 3.3 | EMI / EMC: via stitching, decoupling placement, shielding | W3 | P1 layout, before / after review | Suture Vias · Copper Region · placement of 100 nF at pins | Mon 2 Nov | ⬜ |
| 3.4 | Manufacturing files: Gerber, NC drill, ODB++ | W1, then every project and mock | Every export, opened in a viewer | Export: Gerber (RS-274X) + drill · ODB++ · Pick and Place · PCB Information. Check in W3 whether the Gerber export carries X2 attributes | Thu 26 Nov | ⬜ |

## Phase 4 · Validation & lab bring-up (bench; after the exam)

| # | Topic | Learn | Practise on | Bench | Post | Pack |
|---|---|---|---|---|---|---|
| 4.1 | Power-rail sequencing: step-up and power-on states on a scope | Dec | P1 boards | Oscilloscope · test points from P1 requirement R8 | Tue 1 Dec | ⬜ |
| 4.2 | Protocol analysis: SPI / I²C / UART with a logic analyzer | Dec | P1 sensor bus, P3 INA226 | USB logic analyzer + PulseView | Dec | ⬜ |
| 4.3 | SMD rework: 0603 / 0402 passives, QFN | Dec | P1 / P2 assembly fixes | Iron, hot air, flux, tweezers | Dec | ⬜ |

**Recommended:** order 5 pcs of P1 from JLCPCB at the end of W3 (~1 Nov). Boards arrive mid-Nov; Phase 4 becomes real bring-up in December, not theory. Do not bring up boards in W6–W7; those weeks belong to the mocks.

## How a topic becomes a post pack

1. Sunday 📱: send `Post: <topic number and name>` (or it comes with the Sunday check-in reply).
2. Claude answers with the 2-part response from `linkedin/POST-PROMPT.md` and saves it to `linkedin/posts/YYYY-MM-DD-<topic>.md`.
3. Tue 📱: read part 1 (learning module) as the week's reading. Sun → Mon: replace every `[bracket]` in part 2 with your real number or incident, pick the visual, publish.
