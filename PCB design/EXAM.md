# EasyEDA Certified Professional Exam · facts, official sample task, 90+ gate, 4-hour plan

## 1. Facts (official international page, checked 15 Oct 2026)

| Item | Official wording / fact |
|---|---|
| Format | "The exam includes 1 practical task worth 100 points." Task is randomly assigned; no fixed question set. |
| Duration | "After clicking 'Start Exam', the system will automatically submit your answers after 4 hours." |
| Pass mark | "A score of ≥70 is required to pass the exam." |
| Tool | "Designs must be created exclusively using EasyEDA Pro." No imports from other software. |
| Grading | The EasyEDA engineering team reviews and grades submissions. No public rubric. |
| Scope | "The complete workflow" from schematic to production. |
| Process | Register → wait for review → exam, to be completed within 15 days → grading → e-certificate. |
| Results | Within 15 days. |
| Retake | Fail → wait 15 days before re-registering. Pass → cannot register again. |
| Cost | Free ("limited-time FREE" in a promo post). |
| Contact | selina@easyeda.com |

Sources: oshwlab.com/activities/certificate · pro.easyeda.com

## 2. The official sample task (LCEDA junior PCB certification, same company, same tool)

EasyEDA publishes no sample for the international exam. Its Chinese parent (嘉立创EDA / LCEDA) publishes a **sample practical task with analysis** for its domestic PCB certification (wiki.lceda.cn → pcb-cert → junior → 考试样题分析). Same company, same editor, same kind of graders. We treat it as the best available model of what a task looks like. Translated:

**Project**
- Create the project in the exam workspace, named exactly as instructed ("GD32 core board + your number"); schematic named "…_SCH", PCB named "…_PCB".

**Schematic**
- You are given a **schematic PDF and a BOM**. Place the parts using the **exact designators and device codes** in the BOM. Wiring and layout must match the given schematic with no major deviation. Use the **given net labels and net ports; do not change them**. Schematic DRC: no errors, no warnings, **default rules**.

**PCB**
- Rectangular outline **60 × 75 mm**, corner radius **3 mm**, **origin at the bottom-left** corner.
- Mounting holes at **(5, 5) (5, 70) (55, 70) (55, 5) mm**. Connectors at given coordinates and rotations, e.g. J1 (5, 37.5) 270°, J2 (55, 37.5) 270°, P1 (30, 70) 0°.
- All parts on the **top layer**, parallel or perpendicular, no overlaps, even density, everything inside the outline.
- Rules: min trace **10 mil**; via **24 mil outer / 12 mil drill**; silkscreen default font, **6 mil line, 45 mil height**, top layer, tidy.
- 2 routing layers; **GND copper pour top and bottom**; **100 % routed**; DRC pass with no unconnected nets.
- Save before the deadline; nothing can be saved after it.

**Their own analysis notes**
- Do not forget the names of the project, schematic and PCB.
- Keep the schematic layout like the reference (MCU centre, crystal bottom-left); A4 sheet.
- **Finishing matters more than perfection. A design with DRC errors is almost certain to score poorly.**
- Use the alignment tools; lock the mounting holes and connectors after placing them at the given coordinates.
- Widen power traces; capacitors close to their pins.
- Mind the silkscreen for headers, buttons and the debug interface.
- Change **only** the rules the task requires; keep every other rule at default.

**What this tells us**
1. The task is likely **reproduce + lay out to constraints**, not invent-from-spec. Speed and exactness of transcription matter as much as design judgment.
2. Graders look for: exact naming, exact coordinates, only the required rules changed, neat orthogonal placement, wide power, caps at pins, tidy silkscreen, 100 % routed, 0 DRC.
3. The international page adds "to production", so exports (Gerber, BOM, pick-and-place) may also be asked. We train both.
4. Domestic rules differ (240 min with 20 theory + 80 practical, pass 75, no retake); the international one is 4 h, practical only, pass 70. Do not confuse them.

## 3. Questions to send to selina@easyeda.com in W1 (you send; keep the reply in the journal)

1. Is the international task in the same format as the LCEDA junior sample (given schematic PDF + BOM, then layout to given outline, coordinates and rules)?
2. What do graders evaluate, and are production files (Gerber, BOM, pick-and-place) required?
3. If the 15-day window after approval passes without starting the exam, does it count as a fail, and when can I re-register?
4. Will the exam still be free in November–December 2026?
5. Is a 2-layer design sufficient, or can the task require 4 layers?

## 4. The 90+ gate (your rule) and the timeline

You sit the exam **only when two consecutive mocks score ≥ 90 / 100** on `REVIEW-CHECKLIST.md`, with section F (exam-format compliance) fully passed and ≥ 20 min to spare. Our rubric is a proxy for theirs, so the margin is deliberate: 90 on ours is meant to land well above 70 on theirs.

| Date | Action | Gate |
|---|---|---|
| W1, by Sun 18 Oct | Read the exam page; send the 5 questions above | — |
| Every week W2–W5 | One exam-format drill (transcription or constraint layout), timed | Weekly score in the check-in |
| Sat 14 / Sun 15 Nov (W5) | Split mock: 2 h schematic + 2 h PCB | ≥ 80 |
| **Sat 21 Nov** | Mock #1, 4 h, unseen task | ≥ 85 → register |
| **Mon 23 Nov** | Register (window then covers 30 Nov and runs to ~7 Dec) | only if Mock #1 ≥ 85 |
| **Sat 28 Nov** | Mock #2, 4 h | ≥ 90 → exam Mon 30 Nov |
| Sat 5 Dec (if needed) | Mock #3, 4 h | ≥ 90 → exam by ~7 Dec |
| Still < 90 | Postpone. Let the window lapse only after EasyEDA has answered question 3; otherwise sit it anyway at ≥ 85 | — |

30 Nov is the **target**, not a hard deadline. Readiness decides.

## 5. Where the mocks come from

EasyEDA provides **no** practice exam, sample task or rubric for the international certification. The mocks are ours, built in the official format above:

- I pick an open-source project you have never opened (OSHWLab or GitHub, 30–60 parts) and send you **only** its schematic PDF, its BOM, and a **constraint sheet** (outline size and corner radius, origin, fixed coordinates and rotations, rule numbers, silkscreen spec, required exports).
- You reproduce it in EasyEDA Pro inside 4 hours, save, and send the review packet.
- You self-grade with the 100-point checklist plus section F; I grade it too and we compare. Your weakest rows become next week's drills.
- Drills (W2–W5) are slices of the same thing: 60 min transcription of a 30-part schematic with 0 DRC; 90 min layout to a constraint sheet.

## 6. The 4-hour time budget (exam-format task)

| Clock | Phase | Done when |
|---|---|---|
| 0:00–0:10 | Read the task twice. Create project, schematic and PCB with the **exact names**. Note every number (outline, coordinates, rules, font) on paper or in a text note | Names right, numbers listed |
| 0:10–1:20 | Transcribe the schematic from the PDF + BOM: exact designators and device codes, given net labels and ports, same sheet layout. Schematic DRC with default rules | 0 errors, 0 warnings |
| 1:20–1:30 | Update to PCB. Outline with exact size, corner radius, origin. Place mounting holes and connectors at the given coordinates and rotations; **lock them** | Fixed parts locked |
| 1:30–1:45 | Change **only** the required rules (trace 10 mil, via 24 / 12 mil, silkscreen 6 / 45 mil, or whatever the task says) | Rule dialog matches the task |
| 1:45–2:45 | Placement: all top layer, by block, orthogonal, aligned with the alignment tools, caps at pins, even density | Ratlines short and uncrossed |
| 2:45–3:20 | Routing: power first and wider, then signals; 100 % routed | 0 unrouted |
| 3:20–3:35 | GND pours top and bottom; silkscreen tidy, designators off pads, header and button labels | DRC = 0 |
| 3:35–3:50 | Exports if required (Gerber + drill, BOM, pick-and-place); 3D glance | Files exist |
| 3:50–4:00 | Save. Re-read the task against the design. Save again | Submitted with time to spare |

If the task is instead "design from a spec", use the design budget in `ROADMAP.md` §2 loop A and keep the same last 40 minutes.

Rule: when a phase overruns by 15 min, drop polish, never DRC, completeness or the exact constraints.

## 7. Submission checklist (mocks and the real exam)

- [ ] Project, schematic and PCB named exactly as instructed
- [ ] Every BOM designator and device code present; no extra parts
- [ ] Given net labels and ports unchanged
- [ ] Schematic DRC = 0 errors, 0 warnings, default rules
- [ ] Outline size, corner radius and origin exact
- [ ] Fixed parts at the given coordinates and rotations, locked
- [ ] Only the required rules changed
- [ ] All parts on the top layer, inside the outline, orthogonal, aligned
- [ ] 100 % routed; PCB DRC = 0
- [ ] GND pour top and bottom
- [ ] Silkscreen font as specified, designators readable, off pads
- [ ] Exports if required; project saved twice

## 8. Mock task sources and the design-from-spec bank

Exam-format mocks: an open-source project chosen by Claude per mock (not listed here, so it stays unseen).

Design-from-spec bank (used for drills and in case the real task is a spec):

| # | Task (2-layer unless stated) |
|---|---|
| 1 | USB-powered RS-485 ↔ Wi-Fi gateway: ESP32-C3 module, RS-485 transceiver, screw terminals, 3.3 V LDO, LEDs |
| 2 | 4-channel 4–20 mA input module: STM32G0, shunt + op-amp per channel, RS-485 out, 24 V → 3.3 V buck |
| 3 | 1S Li-ion BLE sensor tag: ESP32-C3, charger, fuel gauge, I²C sensor |
| 4 | 8-channel relay driver: I²C expander, transistor drivers, flyback diodes, 12 V → 5 V buck |
| 5 | STM32F103 USB development board: SWD header, LED + button, LDO, USB-C |
| 6 | 12 V RGB LED-strip driver: 3 MOSFET channels, MCU PWM, 5 V buck |
| 7 | Thermocouple reader: MAX31855, STM32, OLED header, USB-C power |
| 8 | Pogo-pin test fixture interface: 10 test points to a 2 × 10 header, fiducials, panel ×2 |

## 9. Day-before and exam-day checklist

- Pro desktop client updated; login works; library search works.
- Backup internet (phone hotspot) and power.
- Printed: hotkey sheet, `REVIEW-CHECKLIST.md`, the time budget above.
- Calipers, paper, pen, calculator.
- The day before: nothing new. Reread the checklist, sleep.

## 10. Risks

| Risk | Mitigation |
|---|---|
| Exam stops being free | Question 4 in W1; decide then |
| Window lapses because readiness is late | Question 3 in W1; register only after Mock #1 ≥ 85 |
| Task format differs from the LCEDA sample | Weekly drills cover both formats; question 1 in W1 |
| Internet drop mid-exam | Desktop client + hotspot; save often |
| Running out of time | Time budget + drop-polish rule; three timed mocks before the real one |
