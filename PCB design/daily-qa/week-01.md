# Daily 8 · Week 01 · Fri 16 – Mon 19 Oct 2026

**How to use:** 8 questions per day, ~15 min, on your phone in the GitHub app: read the question, decide, tap **Answer**. No pen and paper: Q1–Q4 MCQ → pick a letter in your head · Q5–Q6 calc → mental math or the phone calculator, type the result in your notes app · Q7 scenario → 3 typed bullets or a voice note · Q8 interview → a 60-second voice note, then compare with the model answer. Keep a running score in the notes app (e.g. "Fri 6/8") and report it on Sunday. Each day covers the topic you worked on the **day before**. On Mon / Wed / Fri the day ends with a **Set** of 3 interview problems (20–30 min, bullets only). Anki deck (`build_anki.py`) is optional.

---

## Fri 16 Oct · Topic of Thu 15 Oct: EasyEDA Pro tour, project structure, exam rules

**Q1 · MCQ** — In EasyEDA Pro, what is a "device"?
- A) A schematic symbol only
- B) A PCB footprint only
- C) A symbol + footprint + 3D model + attributes, bound together and placed from the library
- D) A saved PCB template

<details><summary>Answer</summary>

**C.** Pro places *devices*, not bare symbols. The device carries the footprint, 3D model and attributes (manufacturer PN, LCSC number). That is why a missing footprint shows up as a BOM / PCB problem, not a drawing problem.

</details>

**Q2 · MCQ** — Which statement about the EasyEDA certification exam is correct?
- A) It is a 2-hour multiple-choice test
- B) It is one random practical task, 4 hours, pass mark 70 / 100, EasyEDA Pro only
- C) You may import a KiCad design and finish it in Pro
- D) You can retake it the next day if you fail

<details><summary>Answer</summary>

**B.** One task, 100 points, randomly assigned, auto-submitted after 4 h, graded by EasyEDA engineers. No imports from other tools. Fail → wait 15 days before re-registering.

</details>

**Q3 · MCQ** — You changed the schematic after the PCB already exists. The correct way to carry the change over is:
- A) Delete the PCB and Convert to PCB again
- B) Design → Update PCB (or, in the PCB editor, Import Changes from Schematic)
- C) Export a netlist and re-import it
- D) Redraw the change manually in the PCB

<details><summary>Answer</summary>

**B.** Update / Import Changes keeps your placement and routing and applies only the differences. Re-converting would throw the layout away.

</details>

**Q4 · MCQ** — In a Pro project, two different boards that belong to the same product should be:
- A) Two separate projects, always
- B) Two "Board" items in one project, each with its own schematic and PCB
- C) Two layers of the same PCB
- D) Two panels

<details><summary>Answer</summary>

**B.** New → Board adds a board (schematic + PCB) to the current project. Shared library parts and documents stay together.

</details>

**Q5 · Calc** — Convert: 0.127 mm to mil · 10 mil to mm · 0.6 mm to mil.

<details><summary>Answer</summary>

1 mil = 0.0254 mm.
0.127 mm = **5 mil** · 10 mil = **0.254 mm** · 0.6 mm ≈ **23.6 mil**.
5 mil is the usual fab minimum for trace width and spacing on a standard 2-layer board.

</details>

**Q6 · Apply** — Exam time budget: you plan 20 min reading, 70 min schematic, 20 min library, 20 min checks and 20 min exports. How many minutes remain for placement and routing, and is that enough for a 30-part board?

<details><summary>Answer</summary>

240 − (20 + 70 + 20 + 20 + 20) = **90 min**. For 30 parts on 2 layers that is tight but workable if the rules and net classes are set before the first track. If you are not fully routed by minute 200, simplify (bigger board, fewer features) rather than skip DRC and exports.

</details>

**Q7 · Apply** — You open a project and the PCB shows thin straight lines between pads but no copper tracks. What are those lines, and what three things must be set before you start routing?

<details><summary>Answer</summary>

They are **ratlines**: unrouted connections from the netlist. Before routing: 1. board outline and canvas origin; 2. layer stackup; 3. design rules and net classes (clearance, trace widths, via sizes). Placement comes before routing too; the ratlines show you how good the placement is (short, uncrossed = good).

</details>

**Q8 · Interview** — "Walk me through your flow from a requirement to production files." Answer aloud in 60 s.

<details><summary>Answer</summary>

Model answer: "I start with a block diagram and a current budget, then choose parts I can actually buy, preferring the assembler's basic parts. I draw the schematic by block, resolve every pin, add decoupling and pull-ups from the datasheets, and run the schematic DRC. Missing parts get a library device from the datasheet land pattern. On the PCB I set the outline, stackup and rules first, place by block with connectors on the edges, route power first, pour ground, then run DRC and check the 3D view. I export Gerber, drill, BOM and pick-and-place, open the Gerber in a viewer, and only then call it done."

</details>

### Set · Fri 16 Oct · 3 interview problems (20–30 min, write the answers in the journal)

**S1** — A customer sends you a one-paragraph spec for a small IoT board. List the 6 questions you ask before drawing anything (power, interfaces, mechanical, environment, quantity, test).

**S2** — Explain to a software colleague why a schematic that "looks fine" can still fail: give 3 failure modes that a schematic DRC catches and 3 that it cannot.

**S3** — Your manager asks how long a 30-part, 2-layer board takes from spec to Gerber. Give a phase-by-phase estimate in hours and say which phase is the riskiest and why.

---

## Sat 17 Oct · Topic of Fri 16 Oct: schematic conventions, the TP4056 + DW01A + FS8205A charger

**Q1 · MCQ** — TP4056 charge current is set by R_PROG with I_BAT = (V_PROG / R_PROG) × 1200 and V_PROG = 1.0 V. With R_PROG = 1.2 kΩ the charge current is:
- A) 0.1 A
- B) 0.5 A
- C) 1.0 A
- D) 1.2 A

<details><summary>Answer</summary>

**C.** (1.0 V / 1200 Ω) × 1200 = 1.0 A. The common module ships with 1.2 kΩ → 1 A. For a small cell you raise R_PROG (e.g., 2 kΩ → ≈ 0.6 A).

</details>

**Q2 · MCQ** — A net flag (power flag) named VBUS on two different sheets:
- A) Is only a drawing symbol with no electrical meaning
- B) Connects those points to the same global net
- C) Adds a component to the BOM
- D) Sets the trace width in the PCB

<details><summary>Answer</summary>

**B.** Net flags and net labels with the same name are the same net. That is also why a typo (VBUS vs VBUS_) silently splits a power net; check the Net panel.

</details>

**Q3 · MCQ** — In the protection circuit, the FS8205A is:
- A) A single N-MOSFET
- B) A dual N-MOSFET in one package, used back-to-back in the battery negative path
- C) A dual P-MOSFET in the positive path
- D) A resettable fuse

<details><summary>Answer</summary>

**B.** Two N-MOSFETs with sources tied together, driven by the DW01A's OD (discharge) and OC (charge) outputs. Their body diodes point in opposite directions, so the IC can block discharge and charge independently.

</details>

**Q4 · MCQ** — Schematic DRC flags "pin not connected" on a pin you intentionally leave open. The professional fix is:
- A) Delete the pin from the symbol
- B) Place a No Connect flag on the pin
- C) Ignore the error
- D) Wire it to GND

<details><summary>Answer</summary>

**B.** No Connect documents the decision and clears the DRC. Wiring to GND is only right if the datasheet says so (some unused pins must be tied, others must float).

</details>

**Q5 · Calc** — Status LED on 5 V, red LED with V_F ≈ 2.0 V, target 2 mA. Resistor value and power? Which E24 value do you pick?

<details><summary>Answer</summary>

R = (5 − 2.0) / 0.002 = **1.5 kΩ** (E24 value exists). P = 3 V × 2 mA = **6 mW**: any 0603 (100 mW) is fine. 2 mA is plenty for a modern indicator LED; 20 mA is a habit from old LEDs.

</details>

**Q6 · Calc** — TP4056 at 5.0 V input charging a cell at 3.7 V with 1 A. Power dissipated in the IC? What does the IC do about it, and what are your two design options?

<details><summary>Answer</summary>

P = (5.0 − 3.7) × 1 = **1.3 W** in a SOP-8 with a thermal pad. The TP4056 has thermal regulation: it reduces the charge current when the die reaches about 120 °C, so charging just gets slower. Options: 1. lower the current (R_PROG = 2 kΩ → ≈ 0.6 A → ≈ 0.8 W); 2. more copper under the thermal pad with vias to the bottom layer. This is exactly why linear chargers stop making sense above ≈ 1 A.

</details>

**Q7 · Apply** — The 10 µF input capacitor of the TP4056 must end up next to the VCC pin on the PCB. How do you make that intent survive from schematic to layout?

<details><summary>Answer</summary>

Draw it beside the IC pin on the schematic (not in a "caps" corner), add a short note ("place at pin 4"), and in the PCB place the IC first and the cap second, before anything else in that block. Placement Transfer from the schematic helps keep blocks together.

</details>

**Q8 · Interview** — "What does a Li-ion protection IC protect against, and why are there two MOSFETs?" Answer aloud in 60 s.

<details><summary>Answer</summary>

Model answer: "It watches the cell voltage and the current through the MOSFETs. It opens the charge switch on over-voltage, about 4.3 V on the DW01A, opens the discharge switch on under-voltage, about 2.4 V, and on over-current or short circuit it trips fast using the voltage drop across the MOSFETs. Two MOSFETs are needed because a single MOSFET's body diode always conducts in one direction; two back-to-back let the IC block charging and discharging separately. Check the exact thresholds in the datasheet."

</details>

---

## Sun 18 Oct · Topic of Sat 17 Oct: first PCB in Pro, rules, pour, Gerber

**Q1 · MCQ** — The usual minimum trace width and spacing a standard 2-layer fab (e.g., JLCPCB) accepts is about:
- A) 0.05 mm
- B) 0.127 mm (5 mil)
- C) 0.5 mm
- D) 1.0 mm

<details><summary>Answer</summary>

**B.** 0.127 mm / 5 mil for trace and space on standard 2-layer service. Design with margin: 0.2 mm signals, wider for power. Always check the current capabilities page before setting rules.

</details>

**Q2 · MCQ** — To manufacture bare boards the fab needs:
- A) The BOM only
- B) Gerber files for every layer (copper, mask, silkscreen, outline) plus the drill file
- C) The schematic PDF
- D) The 3D STEP file

<details><summary>Answer</summary>

**B.** Gerber + drill describe the board; BOM and pick-and-place are for assembly. The outline layer is often forgotten; without it the fab does not know the board shape.

</details>

**Q3 · MCQ** — "Thermal relief" spokes between a pad and a copper pour exist to:
- A) Carry more current
- B) Limit heat sinking so the pad can be soldered properly
- C) Reduce EMI
- D) Make DRC pass

<details><summary>Answer</summary>

**B.** A pad tied directly into a large pour sucks heat away during soldering, causing cold joints or tombstoning. Use direct connection only where current or thermal performance matters (e.g., a regulator's thermal pad), and then plan the soldering process.

</details>

**Q4 · MCQ** — A silkscreen designator printed over a pad will:
- A) Cause nothing; ink is non-conductive
- B) Be clipped by the fab, so the text becomes unreadable, and may be flagged by DRC
- C) Short the pad
- D) Change the pad size

<details><summary>Answer</summary>

**B.** Fabs remove silkscreen from exposed copper. The text ends up cut or missing, which is exactly what a grader notices. Move designators off pads and vias, readable in one or two rotations.

</details>

**Q5 · Calc** — Using the IPC-2221 outer-layer rule for 1 oz copper and a 10 °C rise, roughly what trace width carries 1 A? What width do you use for the TP4056 1 A charge path, and why wider?

<details><summary>Answer</summary>

About **0.3 mm (≈ 12 mil)** for 1 A at 10 °C rise on an outer layer, 1 oz. Use **≥ 0.6 mm** for the charge path: margin for the IC's heat already in that copper, lower voltage drop (a few mV matter when the IC terminates charging by voltage), and because width is free on a small board. Check your number in the Saturn PCB Toolkit.

</details>

**Q6 · Calc** — Conservative rule: one 0.3 mm-hole via with standard plating carries about 1 A without a noticeable temperature rise. Your battery path moves 3 A between layers. How many vias, and where do you put them?

<details><summary>Answer</summary>

At least **3, better 4** vias in parallel (one more than the minimum, for margin and manufacturing variation). Put them right beside the pad they serve, in a row along the current direction, not in the pad itself.

</details>

**Q7 · Apply** — You open your Gerbers in a viewer: the copper and silkscreen look right but there is no board outline. What happens if you order like this, and how do you fix it?

<details><summary>Answer</summary>

The fab cannot know the board shape; the order gets held for a question or, worse, they guess. Fix: draw the Board Outline object (not just a silkscreen rectangle), make sure the outline layer is included in the fabrication export, and re-check in the viewer. Dimension objects are for humans; the outline layer is for the machine.

</details>

**Q8 · Interview** — "Describe your placement strategy for a small 2-layer board." Answer aloud in 60 s.

<details><summary>Answer</summary>

Model answer: "Connectors go on the edges where the mechanics need them. Then I place by functional block, following the schematic: the regulator and its caps together, the MCU with its decoupling caps touching the pins, the crystal or antenna where the datasheet says. Power paths are short and wide, sensitive analog stays away from switching parts. I check the ratlines: short and uncrossed means the placement is right. Then ground pour on both sides with stitching vias, and silkscreen that someone can read on the bench."

</details>

---

## Mon 19 Oct · Topic of Sun 18 Oct: the review checklist, first library device from a datasheet

**Q1 · MCQ** — Footprint pad sizes should come from:
- A) A guess from the part photo
- B) The datasheet's recommended land pattern (or the IPC-7351 pattern for that package)
- C) Another part that looks similar
- D) The smallest size that passes DRC

<details><summary>Answer</summary>

**B.** The land pattern is designed for solder-joint reliability and reflow behaviour. "Looks similar" is how a 0.5 mm pitch part lands on a 0.65 mm footprint.

</details>

**Q2 · MCQ** — A clear pin-1 mark on the footprint silkscreen matters because:
- A) The 3D model needs it
- B) Assembly and inspection use it for orientation; a polarized part placed backwards is a dead board
- C) DRC requires it
- D) The autorouter uses it

<details><summary>Answer</summary>

**B.** Pin 1 dot, cathode bar, "+" on electrolytics. Also check the pick-and-place rotation against the 3D view; the mark is what the assembler's operator compares against.

</details>

**Q3 · MCQ** — In EasyEDA Pro, the library object that binds a symbol, a footprint and a 3D model is the:
- A) Reuse block
- B) Device
- C) Net class
- D) Panel library

<details><summary>Answer</summary>

**B.** Device. A reuse block is a copied circuit fragment; a net class is a rule group; the panel library is for panel shapes.

</details>

**Q4 · MCQ** — The courtyard of a footprint is:
- A) The copper pad area
- B) The keep-out area around body + pads that other parts must not enter
- C) The silkscreen outline
- D) The solder-paste opening

<details><summary>Answer</summary>

**B.** It is what placement DRC uses to stop parts from colliding and to leave room for the pick-and-place nozzle and rework.

</details>

**Q5 · Calc** — A connector has 0.5 mm pitch and 0.3 mm-wide pads. What is the gap between adjacent pads? Can a 0.127 mm trace with 0.127 mm clearance pass between two pads?

<details><summary>Answer</summary>

Gap = 0.5 − 0.3 = **0.2 mm**. A trace between them needs 0.127 + 2 × 0.127 = **0.381 mm** > 0.2 mm → **no**. Route out from the pad ends, and use the inner layers or the other side for crossings. This is why fine-pitch connectors push boards to 4 layers.

</details>

**Q6 · Calc** — Your self-grade: A 24/30, B 8/10, C 28/40, D 12/15, E 3/5. Total? Pass level? Which section is weakest in percentage terms?

<details><summary>Answer</summary>

Total **75 / 100**: pass level (≥ 70) but not exam-ready (≥ 85). Percentages: A 80 %, B 80 %, **C 70 %**, D 80 %, E 60 %. E is lowest in percent but worth only 5 points; **C (PCB) is where the points are** → next week's drills target C3 placement and C4 routing.

</details>

**Q7 · Apply** — Your new footprint passes Rule Check, but in 3D preview the model floats 2 mm above the board and is rotated 90°. What is wrong and how do you fix it?

<details><summary>Answer</summary>

The 3D model's origin / offset and rotation do not match the footprint. Fix in the 3D model settings of the footprint (Z offset, rotation about Z), then re-check the preview. A wrong model does not break fabrication, but it hides real collisions and misleads the pick-and-place rotation check.

</details>

**Q8 · Interview** — "How do you make sure a new part you created will not cause a board respin?" Answer aloud in 60 s.

<details><summary>Answer</summary>

Model answer: "I take the land pattern from the datasheet, not from a lookalike. I check the symbol pin numbers against the footprint pad numbers one by one, because a swapped pair is the classic respin. I print the footprint 1:1 and put the real part on it, or compare against the 3D model. I run the footprint rule check and the dimension check, then review the first placement in 3D. If the part is critical and new to me, I order a cheap footprint test board or put it on a corner coupon before committing."

</details>
