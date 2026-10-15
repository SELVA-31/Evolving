# PCB design · EasyEDA Pro certification · 15 Oct – 30 Nov 2026

> 🟩 **Active** (started 15 Oct 2026). Exam: **Mon 30 Nov 2026**. The main 12-week roadmap (`../ROADMAP.md`) is ⏸ paused until after the exam.

## Brief (confirmed 15 Oct 2026)

- **Current work:** System integrator; ATE (automated test equipment) and IoT boards with varied requirements.
- **Goal:** EasyEDA Certified Professional (one 4-h practical task, pass ≥ 70 / 100). Longer term: senior hardware design / PCB design engineer.
- **Key date:** exam target 30 Nov 2026 (fallback by ~7 Dec), taken only after two consecutive mocks ≥ 90 / 100 → register 23 Nov if Mock #1 ≥ 85.
- **Hours:** 💻 2 h/day at the PC · 📱 30–60 min/day off-PC (videos, MCQs, interview-style problems).
- **Learn:** professional-level schematic and PCB design in EasyEDA Pro; new techniques by teaching + the official Pro documentation as syllabus.
- **Level:** intermediate.
- **Tools:** EasyEDA Pro, calipers, Gerber viewer, the TP4056 charger modules already on the bench.
- **Link to analog / BMS:** Project 2 (1S Li-ion power & monitor board) and Project 3 (ATE interface with current sensing) reuse the paused roadmap's topics.
- **LinkedIn:** 1–2 posts/week in a working-engineer voice (incidents, decisions, numbers), rotating ATE / IoT / analog-BMS / process so the feed never repeats.
- **Resume the main roadmap after:** decision on Tue 1 Dec 2026.

## Approach

Three loops every week: **A** I give a requirement sheet → you design → review against the 100-point checklist · **B** dissect one open-source design per week · **C** timed drills, then full 4-h mocks in W6–W7. Details in `ROADMAP.md` §2.

## Files

| File / folder | What |
|---|---|
| **`START-HERE.md`** | **The plan on one page: the seven runs, why, outcome, a normal day, this week** |
| `ROADMAP.md` | Approach, daily structure, 7-week plan, tool + knowledge syllabus, sources, check-in template |
| `EXAM.md` | Exam facts (verified), timeline, 4-h time budget, submission checklist, mock task bank |
| `REVIEW-CHECKLIST.md` | 100-point self-grading rubric used on every project and mock |
| `projects/p1-esp32-iot-node/BRIEF.md` | Project 1 requirement sheet (W2–W3) |
| `weekly-plans/week-XX.md` | Day-by-day plan, 💻 / 📱 tagged |
| `daily-qa/week-XX.md` + `build_anki.py` | Daily 8 questions + interview sets → Anki deck "Evolving::PCB Daily 8" |
| `MASTER-CHECKLIST.md` | The 16-topic hardware design checklist mapped to weeks, projects, Pro features and post dates |
| `linkedin/LINKEDIN-PLAN.md` | Voice rules, rotation, checklist-driven post calendar, recall prompts |
| `linkedin/POST-PROMPT.md` + `linkedin/posts/` | The 2-part post prompt (learning module + post) and the generated post packs |
| `journal/` | Daily 5-line log (`../journal/TEMPLATE.md`), `hotkeys.md` |

## Progress

| Week | Dates | Theme | Pass check | Status |
|---|---|---|---|---|
| W1 | 15 – 18 Oct | Baseline: charger module, full flow | 0 DRC errors, Gerber viewed, baseline score | 🟨 |
| W2 | 19 – 25 Oct | Schematic + library (P1) | P1 schematic ≥ 25/30, library 10/10 | ⬜ |
| W3 | 26 Oct – 1 Nov | PCB fundamentals (P1) | P1 packet ≥ 75/100 | ⬜ |
| W4 | 2 – 8 Nov | Power + battery (P2) | P2 ≥ 80/100 | ⬜ |
| W5 | 9 – 15 Nov | Mixed-signal, DFM/DFT (P3, 4-layer, panel) | P3 ≥ 80/100 | ⬜ |
| W6 | 16 – 22 Nov | Mock #1 (exam format) | ≥ 85/100 in 4 h → register Mon 23 | ⬜ |
| W7 | 23 – 29 Nov | Register · Mock #2 · rest | ≥ 90/100 in 4 h | ⬜ |
| — | **30 Nov** (or ≤ 7 Dec after Mock #3) | **Exam**, only at two mocks ≥ 90 | official pass 70 · our target 90 | ⬜ |

⬜ not started · 🟨 in progress · ✅ pass check met
