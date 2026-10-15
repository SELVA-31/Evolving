"""Build Anki import files from the PCB Daily 8 markdown files (same format as ../../daily-qa).

Usage:  python "PCB design/daily-qa/build_anki.py"
Output: PCB design/daily-qa/anki/<week>.csv   -> Anki desktop: File > Import, then sync to phone
        PCB design/daily-qa/anki/<week>.apkg  -> only if `pip install genanki`; open directly on phone
"""
import csv
import html
import re
from pathlib import Path

HERE = Path(__file__).parent
OUT = HERE / "anki"
DECK = "Evolving::PCB Daily 8"
DECK_ID = 2059400111
MODEL_ID = 1607392319

DAY_RE = re.compile(r"^## ((?:Mon|Tue|Wed|Thu|Fri|Sat|Sun) .+)$", re.M)
Q_RE = re.compile(
    r"\*\*Q(\d) · (\w+)\*\* — (.+?)\n\n<details><summary>Answer</summary>\n\n(.*?)\n\n</details>",
    re.S,
)


def to_html(text):
    text = html.escape(text.strip(), quote=False)
    text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"`(.+?)`", r"<code>\1</code>", text)
    return text.replace("\n", "<br>")


def parse(md_path):
    text = md_path.read_text(encoding="utf-8")
    heads = list(DAY_RE.finditer(text))
    cards = []
    for i, head in enumerate(heads):
        end = heads[i + 1].start() if i + 1 < len(heads) else len(text)
        day = head.group(1).strip()
        for q in Q_RE.finditer(text, head.end(), end):
            num, kind, question, answer = q.groups()
            front = f"<small>{html.escape(day)} · Q{num} · {kind}</small><br><br>{to_html(question)}"
            cards.append((front, to_html(answer), f"{md_path.stem} {kind.lower()}"))
    return cards


def write_csv(cards, path):
    with path.open("w", encoding="utf-8", newline="") as f:
        f.write("#separator:tab\n#html:true\n#notetype:Basic\n")
        f.write(f"#deck:{DECK}\n#tags column:3\n")
        csv.writer(f, delimiter="\t", quoting=csv.QUOTE_ALL, lineterminator="\n").writerows(cards)


def write_apkg(cards, path):
    try:
        import genanki
    except ImportError:
        return False
    model = genanki.Model(
        MODEL_ID,
        "Evolving Basic",
        fields=[{"name": "Front"}, {"name": "Back"}],
        templates=[{
            "name": "Card 1",
            "qfmt": "{{Front}}",
            "afmt": "{{FrontSide}}<hr id=answer>{{Back}}",
        }],
    )
    deck = genanki.Deck(DECK_ID, DECK)
    for front, back, tags in cards:
        deck.add_note(genanki.Note(
            model=model, fields=[front, back], tags=tags.split(), guid=genanki.guid_for(front)
        ))
    genanki.Package(deck).write_to_file(str(path))
    return True


def main():
    OUT.mkdir(exist_ok=True)
    for md in sorted(HERE.glob("week-*.md")):
        cards = parse(md)
        write_csv(cards, OUT / f"{md.stem}.csv")
        apkg = write_apkg(cards, OUT / f"{md.stem}.apkg")
        print(f"{md.name}: {len(cards)} cards -> {md.stem}.csv" + (" + .apkg" if apkg else ""))


if __name__ == "__main__":
    main()
