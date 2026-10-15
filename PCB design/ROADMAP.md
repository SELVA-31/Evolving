# PCB design roadmap · 15 Oct – 30 Nov 2026 · EasyEDA Pro certification

> 🟩 **Active.** Exam target: **Mon 30 Nov 2026** · 4 h · online · EasyEDA Pro only. Taken **only after two consecutive mocks ≥ 90 / 100**; register **Mon 23 Nov** if Mock #1 ≥ 85 (see `EXAM.md` §4).
> The 12-week analog / BMS / CV roadmap (`../ROADMAP.md`) stays ⏸ paused until after the exam.

**Identity:** System integrator (ATE + IoT boards) → senior hardware / PCB design engineer.
**Level:** Intermediate (reads schematics, has built boards; now going professional-level in EasyEDA Pro).
**Time:** 💻 2 h/day at the PC · 📱 30–60 min/day away from the PC · two 4-h weekend PC blocks for mock exams (W6, W7).
**Links to the paused plan:** analog (dividers, ADC, NTC, shunt, LDO vs buck) and BMS (charger, protection, fuel gauge) live inside Project 2 and Project 3.

---

## 1. What the exam is, and what that means for the plan

| Fact (official page, checked 15 Oct 2026) | What it means for us |
|---|---|
| 1 practical task, 100 points, **randomly assigned**, no fixed question set | We cannot memorise answers. We train the *procedure* until any small board is routine. |
| **4 hours**, auto-submitted at the end | Speed matters. Every week has a timed drill; W6–W7 are full 4-h mocks. |
| Covers "the complete workflow, from schematic to production" | Deliverables we assume are graded: schematic, custom library parts, PCB, DRC, Gerber + drill, BOM, pick-and-place, 3D check. |
| Must be built in **EasyEDA Pro**; no import from other tools | Pro only, from day 1. Learn the Pro library model (device = symbol + footprint + 3D). |
| Graded manually by EasyEDA engineers, pass ≥ 70 | Engineers grade *decisions*: readability, correct part attributes, sane placement, clean DRC. Hence `REVIEW-CHECKLIST.md` (100-point self-rubric). |
| Results within 15 days; fail → wait 15 days before re-registering | **Your rule: sit it only at 90+ readiness** (two consecutive mocks ≥ 90 on our checklist). 30 Nov is the target, not a hard deadline. |
| Register anytime → approval → exam window of 15 days | Register **Mon 23 Nov** only if Mock #1 (Sat 21) ≥ 85; the window then covers 30 Nov and a fallback to ~7 Dec. Confirm the wording with EasyEDA in W1 (`EXAM.md` §3). |
| **Official sample task exists** (LCEDA domestic certificate, same company): given schematic PDF + BOM → reproduce exactly → layout to given outline, coordinates, rule numbers, pours, 100 % routed, DRC 0 | Mocks and weekly drills use this format (`EXAM.md` §2, §5). Exactness and speed are trained, not only design judgment. |

---

## 2. Approach (decided): three loops every week

| Loop | Share of PC time | How it works | Why |
|---|---|---|---|
| **A · Spec → design → review** | ~60 % | I give a requirement sheet (`projects/pX-…/BRIEF.md`). You design in Pro. You send the **review packet** (below). I review against `REVIEW-CHECKLIST.md`: component choice → schematic → placement → routing → outputs. You fix and resubmit. | The exam grades judgment under a spec. This is exactly that. |
| **B · Dissect an existing design** | ~20 % | One open-source project per week from OSHWLab (same board type as Loop A). Clone it into Pro, run DRC, grade it with the checklist, write "3 things they did better / 3 things I would change". | Professional conventions are learned fastest by reading professional work. Also LinkedIn material. |
| **C · Timed drills and mocks** | ~20 % | W1–W5: one timed drill per week (60–90 min, a slice of the flow). W6–W7: full 4-h mocks on a task you have never seen, self-graded. | Only the clock teaches the clock. |

**Review packet** (what you send me after each project / mock):
1. Schematic PDF (Schematic → Export → PDF).
2. PCB images: top, bottom, 3D preview (PNG).
3. DRC result screenshots (schematic DRC and PCB DRC).
4. BOM (CSV) and the pick-and-place file.
5. Your own `REVIEW-CHECKLIST.md` score and your 3 biggest doubts.
6. Optional: make the OSHWLab project public and send the link.

---

## 3. Daily structure

### 💻 PC block · 120 min

| Block | Time | What |
|---|---|---|
| Build | 90 | The day's Loop A / B / C task from `weekly-plans/week-XX.md` |
| Check | 20 | Run DRC, compare with the checklist, note what to fix tomorrow |
| Log | 10 | 5-line journal (`journal/YYYY-MM-DD.md`, template in `../journal/TEMPLATE.md`) + git commit |

### 📱 Off-PC block · 30–60 min

| Day | What (first 15 min is always the **Daily 8**) |
|---|---|
| Every day | **Daily 8** from `daily-qa/week-XX.md`, read in the GitHub app (tap "Answer"); Anki optional. **No pen and paper:** Q1–Q4 MCQ pick a letter · Q5–Q6 calc sized for mental math or the phone calculator, result typed in a notes app or said aloud · Q7 scenario as 3 typed bullets or a voice note · Q8 interview as a 60-s voice note. Running score in the notes app, reported on Sunday |
| Mon · Wed · Fri | + Interview **Set**: 20–30 min, 3 problems from the week's theme (at the end of that day's Daily 8 section) |
| Tue | + Read this week's **learning module** (part 1 of the post pack in `linkedin/posts/`), 20–30 min. Write 3 lines: *what I will apply tomorrow* |
| Thu | + Video, 20–30 min: EasyEDA Pro feature videos (official channel), Phil's Lab (hardware design), Robert Feranec (design reviews). 3 lines again |
| Sat | + Datasheet / reference-design reading for next week's project (30 min) |
| Sun | + LinkedIn post draft (publish Mon) + weekly check-in to Claude (template in §9) |

---

## 4. Week-by-week

| Week | Dates | Theme | Loop A (you design) | Loop B (you dissect) | Timed drill / mock | Pass check |
|---|---|---|---|---|---|---|
| **W1** | Thu 15 – Sun 18 Oct | Baseline in Pro | Redraw the TP4056 + DW01A + FS8205A charger module you own: schematic → PCB → Gerber | Same module: compare your layout with the real board in your hand | None (baseline score only) | Schematic + PCB with **0 DRC errors**; Gerber opened in a viewer; baseline checklist score written down |
| **W2** | Mon 19 – Sun 25 Oct | Schematic + library mastery | **P1 schematic**: ESP32-C3 IoT sensor node (`projects/p1-esp32-iot-node/BRIEF.md`) + 2 custom devices from datasheets (symbol + footprint + 3D) | An ESP32-C3 dev board on OSHWLab | 60 min, exam format: transcribe a 30-part schematic from a PDF + BOM with exact designators, DRC = 0 on default rules | P1 schematic review **≥ 25/30**; library **10/10**; footprint dimensions match the datasheet land pattern |
| **W3** | Mon 26 Oct – Sun 1 Nov | PCB fundamentals | **P1 PCB**: 2-layer, outline, rules + net classes, placement, routing, GND pour, DRC, silkscreen, 3D, **Gerber + BOM + CPL** | Same dev board: placement and antenna keep-out decisions | 90 min, exam format: lay out a given netlist to a constraint sheet (outline, origin, fixed coordinates, 10 mil / 24-12 mil rules, pours, silkscreen spec) | P1 full packet **≥ 75/100**; Gerber checked in a viewer |
| **W4** | Mon 2 – Sun 8 Nov | Power + battery (analog / BMS link) | **P2**: 1S Li-ion power & monitor board: charger + protection + fuel gauge + cell divider / NTC to ADC + load switch + 3.3 V buck | A BQ24xx- or TP4056-based charger board on OSHWLab | 90 min: buck-converter layout from a datasheet layout example | P2 **≥ 80/100**; justification table complete ("no component without a reason") |
| **W5** | Mon 9 – Sun 15 Nov | Mixed-signal, interfaces, DFM / DFT (ATE link) | **P3**: ATE interface board, **4-layer**: STM32 + USB (diff pair) + INA226 current sense + relay / MUX channels + pogo-pin test points + fiducials + **panel ×2** | An STM32 + USB board on OSHWLab | Split mock: 2 h + 2 h on Sat / Sun (schematic day, PCB day) | P3 **≥ 80/100**; panel fabrication file + test-point report exported |
| **W6** | Mon 16 – Sun 22 Nov | Mock exams | Weekdays: speed drills on your 3 weakest checklist rows; hotkey sheet | A complex OSHWLab board (≥ 80 parts): grade it in 60 min | **Sat 21: Mock #1, 4 h, unseen exam-format task** (schematic PDF + BOM + constraint sheet from Claude) | Mock #1 **≥ 85/100** with section F passed → **register Mon 23 Nov** |
| **W7** | Mon 23 – Sun 29 Nov | Final mock + rest | Mon 23: register. Fix Mock #1 findings; redo its weakest 90 min | — | **Sat 28: Mock #2, 4 h** · Sun 29: light review, nothing new | Mock #2 **≥ 90/100** → **Mon 30 Nov: exam**. Otherwise Mock #3 Sat 5 Dec and exam by ~7 Dec, or postpone |

Day-by-day plans: `weekly-plans/week-XX.md`, created one week ahead (W1 is ready).

---

## 5. Tool syllabus · EasyEDA Pro features by week

Follows the official Pro documentation table of contents (prodocs.easyeda.com). Tick each feature the first time you use it on a real board.

| Week | Schematic | Library | PCB | Outputs |
|---|---|---|---|---|
| W1 | Project / Board structure · Device vs symbol · Wire, Net Label, Net Flag · Annotate Designator · Schematic DRC · Convert / Update PCB · Hotkeys | Place from the LCSC library; read device attributes | Board Outline · Layer Manager · Design Rule (defaults) · Single Routing · Copper Region · Check DRC · 2D / 3D Preview | Gerber · BOM · Pick and Place · PDF |
| W2 | New Page · Net Port · Reuse Block / Hierarchy · Bus · No Connect · attributes (value, footprint, LCSC #, Basic / Extended) · Find Similar · BOM Preview and Price · Cross Probe | **New Device** · New Symbol (Pins Manager, Symbol Wizard, Datasheet Extract Wizard) · New Footprint (Footprint Wizard, Pad Manager, Rule Check, Check Dimension) · 3D Model (attach, offset) | — | BOM scoped to the schematic |
| W3 | Import Changes from Schematic ↔ Update PCB to Schematic | Device Association | PCB Setting (grid, units) · Canvas Origin · **Net Class Manager** · Design Rule (clearance, width, via, per class) · Placement Transfer · Routing Width / Corner · Via · Fill vs Copper Region · Prohibited Region (antenna keep-out) · Teardrop · Silkscreen text · Auto Designator Placement · Dimension · Stack Table / Drill Table · 3D Shell Preview | **Gerber + drill** → open in a Gerber viewer · BOM · Pick and Place · PCB Information |
| W4 | Design Rule in schematic · Circuit Calculator (divider, LED) | Custom footprint for the charger IC (thermal pad) | Copper Manager · Suture (stitching) vias · thermal-relief settings · Routing Width for power nets · Constraint Region · Measure Distance · Flip Board | 3D File (STEP) · Interactive BOM |
| W5 | Multi-sheet with Net Ports (MCU / power / channels) · Module Signal Indicator Diagram | Footprint for pogo pin / test point · fiducial device | 4-layer Layer Manager + stackup · **Differential Pair Manager + Routing** · Equal Length Tuning · Fanout Routing · Test Point · Pad Pair Group · **Panelize / Advanced Panelize** (rails, V-cut, mouse bites) · Remove Unused Pads · PCB Comparison | **Test Point Report** · IPC-D-356A · Panel Fabrication File · ODB++ |
| W6–W7 | Everything above, under the clock | Datasheet → device in ≤ 25 min | Everything above, under the clock | Full set in ≤ 20 min |

---

## 6. Design-knowledge syllabus (tool-independent) by week

| Week | Topics | Where to read / watch |
|---|---|---|
| W1 | Schematic conventions (flow left → right, power up, ground down, no 4-way junctions), designator rules, what fabs need (Gerber, drill, outline), fab capabilities (min trace / space / via) | JLCPCB capabilities page · Phil's Lab schematic tips · EasyEDA Pro Quick Start |
| W2 | Decoupling (100 nF per supply pin + bulk), pull-ups / pull-downs, reset and boot strapping, USB-C power-sink basics (CC 5.1 kΩ), LDO selection (dropout, Iq, Cout), ESD / TVS on connectors, choosing JLCPCB Basic parts | ESP32-C3 datasheet + Espressif hardware design guidelines · TI decoupling app note · Phil's Lab USB hardware design |
| W3 | Trace width vs current (IPC-2221 outer layer), via sizes and current, return paths on a 2-layer board, GND pour + stitching, antenna keep-out, crystal placement, thermal relief vs direct connect, silkscreen rules, DRC strategy | Saturn PCB Toolkit (free) · Robert Feranec 2-layer layout videos · Espressif PCB layout guidelines |
| W4 | Charger topologies (linear vs switching), Li-ion protection (OV / UV / OC / SC) and back-to-back MOSFETs, fuel gauge basics (OCV vs coulomb counting), cell divider + Thevenin loading into an ADC, NTC, shunt sensing (INA226), buck layout: hot loop, input cap first, feedback trace, thermal copper | TI buck layout app notes · BQ24074 / TPS62xx datasheets (layout examples) · Battery University (protection) · paused roadmap W2, W5, W6, W8 topics |
| W5 | 4-layer stackups (SIG-GND-PWR-SIG vs SIG-GND-GND-SIG), differential pairs (USB 90 Ω, length matching), ESD on USB, connectors for fixtures, relay / MOSFET switching, **DFT**: test points, fiducials, tooling holes, pogo-pin access, **DFM**: panel rails, V-cut vs mouse bites, CPL rotation, Basic vs Extended parts and assembly cost | Phil's Lab 4-layer stackup + USB routing · JLCPCB panelization + SMT assembly help · IPC-7351 land-pattern basics |
| W6–W7 | Review discipline: the 100-point checklist until automatic; typical grader findings (floating pins, missing decoupling, unlabeled nets, silkscreen on pads, unrouted nets, ignored DRC) | `REVIEW-CHECKLIST.md` · your own mock debriefs |

---

## 7. Projects (Loop A) and how they link to analog / BMS / ATE / IoT

| Project | Board | Links to |
|---|---|---|
| **P1** (W2–W3) | ESP32-C3 IoT sensor node: USB-C power, 3.3 V LDO, I²C temp / humidity sensor, 1 MOSFET output, LEDs, boot / reset, Qwiic-style I²C header. 2-layer, ≤ 50 × 50 mm | Your IoT boards: the blocks you integrate every week |
| **P2** (W4) | 1S Li-ion power & monitor: charger (BQ24074 or MCP73831), protection (DW01A + FS8205A), fuel gauge (MAX17048), cell divider + NTC to MCU ADC, load switch, 3.3 V buck. 2-layer | Analog + BMS: the paused roadmap's divider, Thevenin, NTC, protection MOSFETs, LDO vs buck, on one board |
| **P3** (W5) | ATE interface board, 4-layer: STM32 + USB, INA226 current sense, 8 relay / MUX channels, pogo-pin test points, fiducials, panel ×2 | Your ATE work: fixtures, test points, measurement chain, DFT / DFM |
| **Mocks** (W6–W7) | Unseen tasks from the `EXAM.md` task bank | Exam conditions |

Every project ends with a **justification table** ("no component without a reason"): part · why this part · key number (voltage, current, tolerance) · alternative considered.

---

## 8. Sources

| Type | Source | Use |
|---|---|---|
| Official | EasyEDA Pro docs: prodocs.easyeda.com (Quick Start, Schematic, PCB, Libraries, Panel) | Menu paths and feature behaviour; §5 follows its table of contents |
| Official | Exam page: oshwlab.com/activities/certificate · contact: selina@easyeda.com | Rules, registration |
| Official | JLCPCB capabilities + SMT assembly help pages | Min trace / space / via, Basic vs Extended parts, BOM / CPL format |
| Video | EasyEDA official YouTube channel (Pro feature videos) | 📱 Tue / Thu |
| Video | Phil's Lab · Robert Feranec (FEDEVEL) · Altium Academy (concept videos are tool-independent) | Design reasoning, reviews |
| Datasheets | Espressif ESP32-C3 datasheet + hardware design guidelines · TI BQ24074 · MAX17048 · TI INA226 · STM32 hardware getting-started app notes | Reference circuits and layout examples for P1–P3 |
| Tools | Saturn PCB Toolkit (trace width, via current) · Gerber viewer (JLCPCB online viewer or gerbv) · digital calipers | Numbers and verification |
| Reference designs | OSHWLab search: "ESP32-C3", "TP4056", "BQ24074", "STM32F103 USB", "test jig" | Loop B material |

---

## 9. Outputs and rhythm

| Output | When |
|---|---|
| Journal entry + git commit | Daily (💻 Log block) |
| Daily 8 (Anki) | Daily (📱) |
| Review packet to Claude | End of each project; after each mock |
| LinkedIn post | 1–2 per week, per `linkedin/LINKEDIN-PLAN.md` (draft Sun, publish Mon; second post Thu) |
| Weekly check-in | Sunday |

**Sunday check-in (paste to Claude):**

```
PCB week N check-in
- PC hours: __/14 · Off-PC days: __/7 · Streak: __
- Checklist score this week: __/100 (weakest rows: ...)
- Timed drill: task ..., finished in __ min, DRC errors at submit: __
- Daily 8: __/32 correct · hardest: ...
- Loop B: project link ... · 3 better / 3 change: ...
- Stuck on: ...
- Review packet: attached / link
```

Claude replies with: review of the packet, next `weekly-plans/week-XX.md`, next `daily-qa/week-XX.md` (Daily 8 + interview sets), LinkedIn angle check, English feedback.

---

## 10. After the exam

- If the gate is not met by Mock #3 (Sat 5 Dec), we postpone and re-plan: the exam registration is open-ended, so readiness decides the date.
- Result arrives within 15 days of the exam. LinkedIn post either way (pass: what the exam rewarded; fail: what the grader found, retake date).
- Decision point on **Tue 1 Dec**: resume the 12-week roadmap re-dated from 1 Dec, keeping PCB design as a weekly 4-h block (the S6 "3S–4S monitor schematic" becomes a full PCB).
