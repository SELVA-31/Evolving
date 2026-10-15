# LinkedIn plan · 19 Oct – Dec 2026 · 1–2 posts per week

Goal: a profile that reads like a working hardware engineer's notebook (incidents, decisions, numbers), not a tutorial feed. Topics come from the 16-topic `../MASTER-CHECKLIST.md`; each post is made with the 2-part prompt in `POST-PROMPT.md` (learning module + post), then filled with your real work (ATE, IoT) or the current self-set project, said plainly.

## 1. Voice rules

1. First person, past tense, **one** incident or decision per post.
2. Open with the moment: a symptom, a number, or a decision. Never with "I am learning…" or "In this post…".
3. At least one specific number (mV, mm, W, °C, hours, count, cost).
4. One lesson, written as a rule you now follow.
5. 120–200 words. One image: schematic crop, DRC screenshot, 3D render, bench photo, before / after, a small table. No stock images.
6. End with a question to the reader. ≤ 5 functional hashtags.
7. **Confidentiality:** no customer names, no customer schematics or part numbers that identify a product. Redraw a simplified version. If it is a self-set project, say so.
8. **Honesty:** only incidents that happened and numbers you calculated or measured. Anything else stays in `[brackets]` until it is real, or is deleted.

## 2. Rotation (this is what stops the feed from repeating)

**Lanes:** ATE work · IoT work · analog / BMS · process & tooling · validation (bench).
**Formats:** war story (symptom → wrong first guess → root cause → rule) · decision / trade-off · before / after · numbers / rule of thumb · checklist from scars · opinion.

Rules: never the same lane twice in a row · never the same format twice within three posts · at most one "exam / learning" framing every two weeks.

## 3. Calendar (checklist-driven)

| Publish | Checklist topic | Lane | Format | This plan's material | Real-incident hook |
|---|---|---|---|---|---|
| Mon 19 Oct | 1.2 Power architecture: LDO vs buck / boost | analog / BMS | numbers | W1 TP4056 module: 1.3 W at 1 A, dropout at low line | A device that got warm while charging; a regulator that dropped out on a weak USB port |
| Thu 22 Oct | 1.1 Component selection: MCU + parameter matching | IoT | decision | P1: ESP32-C3 module and LDO choice | A part that arrived in the wrong package; a module swap that broke a pin map |
| Mon 26 Oct | 1.4 Circuit protections: ESD, TVS, reverse polarity | ATE | war story | P1 USB-C ESD; fixture inputs facing a faulty DUT | A fixture channel or field unit killed by wrong polarity or ESD |
| Thu 29 Oct | 1.3 BOM lifecycle: active / obsolete / long-lead | process | checklist | P1 BOM with LCSC numbers, Basic vs Extended | A fixture delayed by a long-lead part; a substitution that was not equivalent |
| Mon 2 Nov | 3.3 EMI / EMC: stitching vias, decoupling placement | IoT | before / after | P1 layout before and after review | A noise problem solved by layout, not firmware |
| Thu 5 Nov | 2.4 Constraint management: DRC rules, net classes | process | opinion | P1 rules set before routing; dissected OSHWLab boards | "DRC-clean is not design-clean" |
| Mon 9 Nov | 2.3 IoT & RF layout: antenna clearance | IoT | numbers | P1 antenna keep-out in mm | Wi-Fi range difference between two placements or enclosures |
| Thu 12 Nov | 3.2 DFM: panelization, fiducials, mask, thermal relief | ATE | war story | P2 pour settings; P3 panel ×2 | A tombstoned part; an assembly quote that surprised you |
| Mon 16 Nov | 2.1 Layer stackup: 4 / 6 layers | process | decision | P3 4-layer stackup choice | A 2-layer board that should have been 4 |
| Thu 19 Nov | 2.2 Impedance control: 90 Ω USB pairs | IoT | numbers | P3 USB trace width / spacing for the stackup | USB enumeration failures on a long cable or bad routing |
| Mon 23 Nov | 3.1 Advanced DFT: test pads for bed-of-nails | ATE | checklist | P3 pogo test points on a grid | A board that could not be tested without soldering wires |
| Thu 26 Nov | 3.4 Manufacturing files: Gerber, drill, ODB++ | process | war story | Mock exam export discipline (minute 170) | A missing outline layer or wrong drill file at the fab |
| Tue 1 Dec | 4.1 Power-rail sequencing on a scope | validation | before / after | P1 boards bring-up (if ordered in W3) | A brown-out at power-on |
| Dec | 4.2 Protocol analysis (SPI / I²C / UART) · 4.3 SMD rework | validation | war story · numbers | P1 / P2 bring-up | I²C that only worked with the probe attached; a QFN rework |
| Dec | Exam result | process | decision | Certificate or grader findings | — |

## 4. Shape example (illustrative — replace every fact with yours)

> Channel 6 on a test fixture read 38 mV higher than the other seven. Same relay, same shunt, same firmware.
>
> My first guess was a bad relay. Swapped it. Same offset.
>
> The shunt's return path shared 60 mm of trace with the relay coil current. 300 mA through a 0.2 mm trace is roughly 40 mV. The "measurement error" was Ohm's law.
>
> Rule I follow now: sense returns get their own trace to the reference point, and I calculate the drop before routing, not after the board comes back.
>
> What is the smallest layout mistake that cost you a board spin?

Shape: symptom with a number → wrong first guess → root cause with a number → one rule → question.

## 5. Weekly workflow

| When | What |
|---|---|
| Sun 📱 (30 min) | Send `Post: <next topic>` (or take the pack that comes with the check-in reply). Answer the recall prompt in 3 lines. Replace every `[bracket]` in the post with your real number or incident. Choose the image from this week's work. |
| Mon 📱 (5 min) | Publish. |
| Tue 📱 (20–30 min) | Read part 1 of the pack (learning module). 3 lines: what I will apply tomorrow. |
| Thu 📱 (20 min) | Second post, same process, only if the week produced a real story or number. One strong post beats two thin ones. |
| Daily 📱 (5 min) | Comment on 2–3 posts by hardware engineers. Your comment is a mini-post: one specific observation. |

## 6. Recall prompts (mine these for real incidents; answer them once, keep the list in `incidents.md`)

1. A board that passed bring-up but failed in the field.
2. A connector that was mirrored or had the wrong pitch.
3. A part shortage that forced a redesign.
4. A test that gave different results on two fixtures.
5. An I²C or UART bus that only worked with the scope probe attached.
6. A regulator that got too hot, and what you changed.
7. A silkscreen or label error that cost assembly time.
8. A ground-loop or noise problem solved by layout, not firmware.
9. A BOM substitution that was not equivalent.
10. A customer requirement that looked trivial and was not.
