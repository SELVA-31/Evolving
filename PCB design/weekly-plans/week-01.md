# Week 1 · Thu 15 – Sun 18 Oct 2026 · Baseline in EasyEDA Pro

**Goal:** Run the complete workflow once, on a board you can hold in your hand (TP4056 + DW01A + FS8205A charger module), and write down a baseline score.
**Daily 8:** 📱 `daily-qa/week-01.md` (starts Fri 16; open in the GitHub app and tap "Answer"; no pen and paper needed; Anki deck optional)
**Where:** 💻 PC · 📱 phone

---

## Thu 15 Oct · Setup + Pro tour

| Block | Task |
|---|---|
| 💻 Build (90) | 1. Install the EasyEDA Pro desktop client (or open pro.easyeda.com), sign in, create your personal workspace. 2. New Project → "W1 TP4056 module" (Pro creates Board1 with a schematic and a PCB). 3. Read the Pro docs: Introduction → UI Introduction, Design Flow, Hotkeys. Fill `journal/hotkeys.md` from Settings → Hotkeys. 4. Warm-up: search the library for a 0603 resistor, 0603 capacitor, LED, TP4056, DW01A, FS8205A and a USB-C 16-pin receptacle; prefer parts marked JLCPCB **Basic**. Place, wire, add net labels, Convert to PCB, look at the ratlines. 5. Delete the PCB and do step 4 again, faster. |
| 💻 Check (20) | Open the exam page (oshwlab.com/activities/certificate). Copy the current rules into today's journal. Email the 5 questions in `EXAM.md` §3 to selina@easyeda.com. Read the official sample task in `EXAM.md` §2 once. |
| 💻 Log (10) | `journal/2026-10-15.md` + git commit. |
| 📱 (30–60) | Read `EXAM.md` and `REVIEW-CHECKLIST.md` on the phone. Watch one EasyEDA Pro introduction video (official channel), 20 min. No Daily 8 today. |

## Fri 16 Oct · Loop B, part 1: the charger module schematic

| Block | Task |
|---|---|
| 💻 Build (90) | Datasheets: TP4056 (typical application + R_PROG table), DW01A (typical application), FS8205A (pinout). Draw the complete module schematic: USB input, TP4056 with R_PROG, CHRG / STDBY LEDs, input and output caps, DW01A with its 100 Ω + 100 nF filter, FS8205A in the battery negative path, pads B+ / B− / OUT+ / OUT−. Net labels: VBUS, BAT+, BAT−, OUT−, GND. Power flags. Annotate. Attributes: value, footprint, LCSC number on every part. |
| 💻 Check (20) | Schematic DRC → 0 errors. Export → BOM → open the CSV: no empty LCSC cells. |
| 💻 Log (10) | Journal + commit. |
| 📱 (30–60) | Daily 8 (Fri) + the Fri **Set** (3 interview problems on the TP4056 circuit). |

## Sat 17 Oct · Loop B, part 2: PCB + fabrication files

| Block | Task |
|---|---|
| 💻 Build (90, take 120 if you can) | 1. Measure the real module with calipers; board outline the same size, 2-layer. 2. Layer Manager; Design Rule from JLCPCB 2-layer capabilities (min trace / space 0.127 mm; use 0.2 mm for signals, ≥ 0.6 mm for the 1 A charge path; via 0.6 / 0.3 mm). 3. Net class PWR (VBUS, BAT+, BAT−, OUT−) width 0.6 mm. 4. Place like the real module. 5. Route. 6. GND Copper Region on both sides, stitching vias. 7. Silkscreen: designators, "+ / −" at the pads, board name "W1-TP4056 v0.1". |
| 💻 Check (20) | PCB DRC = 0 errors, unrouted = 0. 3D preview. Export Gerber + drill → open in the JLCPCB Gerber viewer. Export BOM + pick-and-place. |
| 💻 Log (10) | Journal + commit. |
| 📱 (30–60) | Daily 8 (Sat) + reading: TP4056 thermal-regulation section; Espressif ESP32-C3 hardware design guidelines, chapters on power supply and strapping pins (prep for P1). |

## Sun 18 Oct · Baseline score, first library part, LinkedIn #1

| Block | Task |
|---|---|
| 💻 Build (90) | 1. Self-grade the module with `REVIEW-CHECKLIST.md` → baseline score into the journal. 2. Compare with the real module: list 5 placement / routing differences; for each, which is better and why. 3. Library warm-up: create the USB-C 16-pin receptacle you will use in P1 as a **device**: symbol via Pins Manager; footprint from the datasheet land pattern via Footprint Wizard; run footprint Rule Check and Check Dimension; attach the 3D model if the LCSC part has one. 4. Read `projects/p1-esp32-iot-node/BRIEF.md`; draw the block diagram on paper; start `P1-notes.md` with the 7 questions. |
| 💻 Check (20) | Footprint pad sizes: datasheet numbers and your numbers side by side in the journal. |
| 💻 Log (10) | Journal + commit. |
| 📱 (30–60) | Daily 8 (Sun) · LinkedIn post #1: fill the brackets in `linkedin/posts/2026-10-19-power-architecture.md` with your module's numbers, pick the visual · 5 phrases to `../english/phrase-bank.md` · Sunday check-in to Claude (template in `ROADMAP.md` §9) with the baseline score and the review packet. |

---

**Week 1 pass check:** schematic + PCB with 0 DRC errors · Gerber opened in a viewer · baseline score written · one device created from a datasheet · post #1 drafted.
