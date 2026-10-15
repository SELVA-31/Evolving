# Start here · the plan on one page

Read only this file to understand the plan. The other files are reference you open when a step points to them.

## The whole plan in one sentence

You run the **same loop seven times, faster each time**: task → schematic → library parts → PCB → production files → review → fix. The seventh run is the exam, and you only do it when two mocks in a row score 90 or more.

| Run | When | Board | Time allowed | Purpose |
|---|---|---|---|---|
| 1 | W1 · 15–18 Oct | TP4056 charger module you own | 4 days | See the full flow once, slowly; baseline score |
| 2 | W2–W3 · 19 Oct – 1 Nov | P1 ESP32-C3 IoT node | 2 weeks | Learn each stage properly (schematic + library, then PCB) |
| 3 | W4 · 2–8 Nov | P2 Li-ion power board | 1 week | Power and analog / BMS blocks |
| 4 | W5 · 9–15 Nov | P3 ATE interface, 4-layer · split mock Sat / Sun | 1 week | Hard features; first exam-format run in 2 h + 2 h |
| 5 | Sat 21 Nov | Mock #1, unseen task, exam format | **4 hours** | ≥ 85 → register on Mon 23 Nov |
| 6 | Sat 28 Nov | Mock #2 | **4 hours** | ≥ 90 → exam Mon 30 Nov |
| 7 | **Mon 30 Nov** (or by ~7 Dec after a Mock #3) | The real exam | **4 hours** | Pass is 70; your target is 90 |

Everything else (Daily 8, learning modules, dissecting open-source boards, LinkedIn) supports these seven runs. If time is short, the runs stay and the supports shrink.

## What the exam task looks like, and where the mocks come from

EasyEDA gives no practice exam, sample or rubric for the international certificate. Its Chinese parent LCEDA publishes an official **sample task** for the same kind of certificate: you get a **schematic PDF + BOM** and must reproduce the schematic exactly (same designators, device codes, net labels), then lay out the board to a **given outline, origin, fixed coordinates, rule numbers and silkscreen spec**, 100 % routed, DRC clean, GND pours both sides. Their advice: finish, keep DRC at zero, change only the rules asked, align everything, lock the fixed parts. Full translation in `EXAM.md` §2.

So **the mocks are mine, in that format**: I pick an open-source board you have never seen and send only its schematic PDF, BOM and a constraint sheet. You rebuild it in Pro in 4 hours. We both grade it with the same 100-point checklist plus the exam-format gates. From W2 every week has a 60–90 min drill of the same kind.

## Why this shape (efficiency)

- **Every PC hour produces a board artifact.** Learning content is pushed to the phone.
- **The exam skill is "finish an exact board in 4 hours".** You practise that in slices weekly and in full three times.
- **One rubric for everything** (`REVIEW-CHECKLIST.md`), so your sense of "good" calibrates fast, and "90" means the same thing every week.
- **Weekly feedback loop.** Sunday check-in → I grade your packet → next week's drills target your weakest rows.
- **Budget:** about 92 PC hours + three 4-h mock blocks + about 35 phone hours.

## Outcome

1. Six boards from spec or PDF to production files in EasyEDA Pro, on OSHWLab + GitHub.
2. The certificate, taken only when the mocks say 90+. Target Mon 30 Nov; latest fallback ~7 Dec; if still not ready, we postpone and say so.
3. A review habit: the checklist runs in your head.
4. About 180 interview-style Q&A done, phone only, and about 12 LinkedIn posts, one per checklist topic.

Honest limits: 2 h/day is tight for P3; if W5 overruns, P3 drops the panel. Phase 4 of the master checklist (bench) happens in December.

## A normal day

**💻 PC · 2 h**
1. Open `weekly-plans/week-XX.md`, today's row (2 min).
2. **Build 90 min**: the task in that row.
3. **Check 20 min**: run DRC, tick the checklist rows named, note tomorrow's first fix.
4. **Log 10 min**: 5 lines in `journal/YYYY-MM-DD.md` + `git commit`.

**📱 Phone · 30–60 min, no pen and paper needed**
1. **Daily 8**, 15 min, in the GitHub app: open `daily-qa/week-XX.md`, read, tap "Answer" to check. Anki is optional.
   - Q1–Q4 MCQ: pick a letter in your head.
   - Q5–Q6 calc: numbers are chosen so the phone calculator or mental math is enough; say the steps aloud or type the result in your notes app.
   - Q7 scenario: 3 bullets typed in the notes app, or a voice note.
   - Q8 interview: a 60-second voice note.
   - Keep a running score in the notes app; report it on Sunday.
2. Then one extra, by day: Mon / Wed / Fri → the 3-problem **Set** (type bullets, no derivations needed) · Tue → the week's learning module · Thu → one video · Sat → next week's datasheet · Sun → fill the LinkedIn post, send the check-in.

## Who does what

| You | Claude |
|---|---|
| Design the boards in EasyEDA Pro | Write requirement sheets, weekly plans, mock tasks and constraint sheets |
| Send the review packet (PDF, PNGs, DRC, BOM, your score) | Grade against the checklist, name the 3 weakest rows, set next week's drills |
| Do the Daily 8 and the Sets on the phone | Write them one week ahead, phone-answerable |
| Fill the brackets in the post with your real numbers, publish | Generate the post pack (learning module + post) |
| Email EasyEDA the 5 questions in W1; register on 23 Nov if Mock #1 ≥ 85; sit the exam at ≥ 90 | Keep the gate honest |

## This week (W1), concretely

| Day | PC | Phone |
|---|---|---|
| Thu 15 | Install Pro, create the project, hotkeys, 10-part warm-up twice, copy exam rules, send the 5 questions to EasyEDA | Read `EXAM.md` §2, one Pro intro video |
| Fri 16 | Draw the charger module schematic, DRC = 0, BOM | Daily 8 + Set |
| Sat 17 | Its PCB: rules, place, route, pour, DRC = 0, Gerber opened in a viewer | Daily 8 + datasheet reading |
| Sun 18 | Self-grade (baseline), compare with the real module, make one library part, read the P1 brief | Daily 8, fill the post brackets, check-in |
