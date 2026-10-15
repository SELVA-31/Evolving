# Review checklist · 100 points · used for every project, dissection and mock

Score honestly. **≥ 85** exam-ready · **70–84** pass-level, fix the weakest rows · **< 70** not yet.
The exam has no public rubric; this one mirrors "schematic to production" the way a reviewing engineer reads a board.

## A · Schematic · 30

| # | Check | Pts | How to verify in EasyEDA Pro |
|---|---|---|---|
| A1 | Readability: signal flow left → right, power rails at the top, GND at the bottom, no 4-way junctions, no wires through symbols, page titles | 5 | Zoom to fit. Can a stranger find power, MCU and connectors in 10 s? |
| A2 | Correctness: every pin wired or marked No Connect; a decoupling cap on every supply pin (+ bulk per IC); pull-ups / pull-downs (I²C, enable, boot / strapping); reset circuit per datasheet; polarity of diodes, caps, connectors; connector pins labelled | 10 | Left **Net** panel: no single-pin nets except intended. Walk each IC's "typical application" in its datasheet |
| A3 | Structure: multi-page by block when > ~25 parts; Net Ports between pages; power nets as Net Flags; designators consistent after Annotate | 5 | Design → Annotate Designator; Left **Page** panel |
| A4 | Attributes + DRC: value, footprint, manufacturer PN, LCSC #, Basic / Extended known, DNP marked; schematic DRC = 0 errors, warnings justified in a note | 10 | Export → BOM Preview: no empty cells. Design → Check DRC |

## B · Library · 10

| # | Check | Pts | How to verify |
|---|---|---|---|
| B1 | Symbol: pin numbers / names / types from the datasheet; pin 1 or polarity visible; pins on grid; inputs left, outputs right, power top, GND bottom | 4 | Pins Manager vs datasheet pin table, pin by pin |
| B2 | Footprint: pad sizes from the datasheet land pattern (or IPC-7351); pin-1 mark; silkscreen outline not on pads; courtyard; origin at centre; footprint **Rule Check** + **Check Dimension** pass; 1:1 print against the real part when you have it | 4 | Write datasheet numbers and your numbers side by side |
| B3 | Device binds symbol + footprint + 3D; the 3D model sits on the board correctly | 2 | 3D preview |

## C · PCB · 40

| # | Check | Pts | How to verify |
|---|---|---|---|
| C1 | Setup: board outline with Dimension objects, canvas origin set; layer stackup set; mounting holes with keep-out; fiducials if assembled; board name + version on silkscreen | 5 | Layer Manager, Stack Table |
| C2 | Rules before routing: net classes (PWR, SIG, USB …) with width / clearance; clearance ≥ fab minimum + margin; via sizes; special regions (antenna keep-out, slots) | 5 | Net Class Manager, Design Rule |
| C3 | Placement: blocks mirror the schematic; connectors on edges facing out; decoupling caps at the pin, bulk nearby; crystal / antenna per datasheet; converter hot loop tight; analog away from switching / digital; hot parts spaced; polarized parts oriented consistently; designators readable in at most two rotations | 10 | 2D top view with ratlines before routing: are they short and uncrossed? |
| C4 | Routing: 0 unrouted; power width per current (IPC-2221) with margin; short return paths; GND pour both sides + stitching vias; no acute angles; nothing under crystal or antenna; differential pairs routed as pairs, length-matched; no orphan copper; thermal relief for hand-soldered pads, direct connect where current matters; vias not in SMD pads | 12 | Bottom **Check DRC** panel: unrouted count; Copper Manager: orphans removed |
| C5 | DRC + silkscreen: PCB DRC = 0 errors, warnings justified; silkscreen not on pads or vias; polarity marks (+, cathode bar, pin-1 dot); connector pin labels; test-point labels; 3D preview inspected for collisions and orientation | 8 | Design → Check DRC; View → 3D Preview |

## D · Fabrication outputs · 15

| # | Check | Pts | How to verify |
|---|---|---|---|
| D1 | Gerber + drill generated with all layers, opened in a viewer; outline present; drills present | 5 | JLCPCB Gerber viewer or gerbv |
| D2 | BOM: LCSC # on every line, quantities right, DNP excluded, Basic vs Extended considered | 5 | Open the CSV |
| D3 | Pick-and-place exported; rotations sane in the 3D / assembly preview; Interactive BOM (optional) | 5 | JLCPCB order preview or 3D view |

## E · Documentation · 5

| # | Check | Pts |
|---|---|---|
| E1 | Block diagram; key calculations (LED resistor, divider, regulator dropout / current, trace width); justification table (part · why · key number · alternative) | 5 |

---

## F · Exam-format compliance · pass / fail gates (no points; any FAIL means the mock does not count towards the 90+ gate)

Taken from the official LCEDA sample task (`EXAM.md` §2). Apply to every exam-format drill and mock.

| # | Gate | Pass / Fail |
|---|---|---|
| F1 | Project, schematic and PCB named exactly as the task says | |
| F2 | Every BOM designator and device code present, none extra; given net labels and ports unchanged | |
| F3 | Schematic DRC: 0 errors **and** 0 warnings on default rules | |
| F4 | Outline size, corner radius and origin exact | |
| F5 | Fixed parts (holes, connectors) at the given coordinates and rotations, locked | |
| F6 | Only the rules the task requires were changed; all others default | |
| F7 | All parts on the required layer, inside the outline, orthogonal, aligned | |
| F8 | 100 % routed, PCB DRC = 0, pours on the required layers | |
| F9 | Silkscreen font / size as specified; designators readable, off pads | |
| F10 | Saved (and exported, if required) with ≥ 20 min to spare | |

## Score sheet (copy into the journal)

```
Project: ____  Date: ____  Time used: ____
A1 _/5  A2 _/10  A3 _/5  A4 _/10   → A _/30
B1 _/4  B2 _/4   B3 _/2             → B _/10
C1 _/5  C2 _/5   C3 _/10 C4 _/12 C5 _/8 → C _/40
D1 _/5  D2 _/5   D3 _/5             → D _/15
E1 _/5                              → E _/5
Total _/100   Weakest 3 rows: ____
Section F (exam format): F1–F10 all PASS?  yes / no   Time spare: ____ min
Counts towards the 90+ gate: yes / no
```

## Review packet (send with the score sheet)

1. Schematic PDF · 2. PCB top / bottom / 3D PNG · 3. DRC screenshots · 4. BOM CSV + pick-and-place · 5. Your 3 biggest doubts · 6. (optional) public OSHWLab link
