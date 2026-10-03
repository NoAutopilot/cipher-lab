#!/usr/bin/env python3
"""Re-derive the readings in reading.md from ciphertext.txt and the vocabulary table in key.md.

The mssEC 15 entries are dictionary-coded plaintext (no route transposition is recorded), so a reading is the
entry with every code word replaced by its meaning in brackets; the operator's tail (the time word and the filler
after it) is set apart in braces. Each code-word token is graded with the grade of its table row (C, I or M);
words not in the table are left as written.

Usage:  python3 decode.py            # print the readings and the grade counts
        python3 decode.py --check    # exit 1 if the block in reading.md differs from what is derived now
        python3 decode.py --write    # rewrite the derived block inside reading.md
        python3 decode.py --at "18 Jun" WORD...   # the value and grade key.md gives each word on that date

key.md rows carry a "witness dates" column (print/key_dates.py computes it); a word is read by the row whose range
covers the entry's ledger date, and graded M outside every range or where two values cover the date (rule 4).

Exit status is non-zero when --check finds reading.md stale.
"""
import datetime as dt
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
START = "<!-- decode.py: derived block starts -->"
END = "<!-- decode.py: derived block ends -->"

MONTHS = {"jan": 1, "feb": 2, "mar": 3, "apr": 4, "may": 5, "jun": 6, "jul": 7, "aug": 8}


def parse_day(text):
    """Return a 1862 date from 'February 5th 1862', "Feb 7 '62", '05 Feb', or None."""
    m = re.search(r"^\s*(\d{1,2}) (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug)\b", text)
    if m:
        return dt.date(1862, MONTHS[m.group(2).lower()], int(m.group(1)))
    m = re.search(r"\b(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug)[a-z]*\.?\s*(\d{1,2})(?!\d)", text, re.I)
    if m:
        return dt.date(1862, MONTHS[m.group(1)[:3].lower()], int(m.group(2)))
    return None


def parse_range(cell):
    """'05 Feb-21 Feb 1862' or '06 Feb 1862' -> (first, last); 'undated' -> None."""
    days = [parse_day(part) for part in cell.split("-")]
    if not days or None in days:
        return None
    return days[0], days[-1]


def load_key(path=HERE / "key.md"):
    """Return {code word (lower): [(meaning, grade, witness range or None), ...]} from the table in key.md.

    A word may have several rows, one per value, each with the witness date range that print/key_dates.py computes
    (GAPS127, 3 Oct 2026): spring-summer 1862 tables reuse Feb words for other names.
    """
    table = {}
    in_table = False
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("| code word |"):
            in_table = True
            continue
        if in_table:
            if not line.startswith("|"):
                if table:
                    break
                continue
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) < 5 or set(cells[0]) <= {"-"}:
                continue
            word, meaning, grade, dates = cells[0], cells[1], cells[2], cells[3]
            table.setdefault(word.lower(), []).append((meaning, grade, parse_range(dates)))
    if not table:
        sys.exit("no vocabulary table found in key.md")
    return table


def pick(rows, day):
    """Return (meaning, grade) for an entry dated `day` (rule 4, dated values).

    The rows whose witness range covers the day decide; one meaning keeps its row's grade, two or more meanings are a
    true conflict (meanings joined by ' | ', grade M). No covering row: the nearest dated row by date, graded M (a
    value outside its supporting range); an undated row is used only when no dated row exists or covers, at its grade
    if it is the word's only row, else M.
    """
    if day is None:
        dated = []
    else:
        dated = [r for r in rows if r[2]]
    cover = [r for r in dated if r[2][0] <= day <= r[2][1]]
    meanings = list(dict.fromkeys(r[0] for r in cover))
    if len(meanings) == 1:
        return cover[0][0], cover[0][1]
    if len(meanings) > 1:
        return " | ".join(meanings), "M"
    if len(rows) == 1:
        r = rows[0]
        return r[0], (r[1] if (r[2] is None or day is None) else "M")
    undated = [r for r in rows if r[2] is None]
    if undated:
        return undated[0][0], "M"
    if not dated:
        return rows[0][0], "M"
    near = min(dated, key=lambda r: min(abs((r[2][0] - day).days), abs((r[2][1] - day).days)))
    return near[0], "M"


def load_ciphertext(path=HERE / "ciphertext.txt"):
    """Return a list of (header, lines) for every '### ' block in ciphertext.txt."""
    blocks = []
    header, lines = None, []
    for raw in path.read_text(encoding="utf-8").splitlines():
        if raw.startswith("### "):
            if header:
                blocks.append((header, lines))
            header, lines = raw[4:].strip(), []
        elif header is not None:
            if raw.startswith("#") or raw.startswith("<!--"):
                continue
            lines.append(raw.rstrip())
    if header:
        blocks.append((header, lines))
    if not blocks:
        sys.exit("no '### ' blocks found in ciphertext.txt")
    return blocks


def clean_token(tok):
    """Strip editorial marks: <del>..</del> is dropped by the caller, <ins>..</ins> kept, [?] kept as a flag."""
    return tok.strip(" .,;:'\"()")


def entry_text(lines):
    """Join the manuscript lines, dropping <del>...</del> spans and the <ins> tags."""
    text = " ".join(l for l in lines if l.strip())
    text = re.sub(r"<del>.*?</del>", " ", text)
    text = re.sub(r"</?ins>", "", text)
    return re.sub(r"\s+", " ", text).strip()


def lookup(core, key):
    """Return (stem, suffix, row) for a token: handles the doubtful flag [?] and a possessive s."""
    flag = ""
    if core.endswith("[?]"):
        core, flag = core[:-3], "[?]"
    low = core.lower()
    if low in key:
        return core, flag, key[low]
    if low.endswith("s") and low[:-1] in key:
        return core[:-1], "s" + flag, key[low[:-1]]
    return core, flag, None


def decode_entry(text, key, day=None):
    """Return (reading, counts) where counts is a dict of grades over code-word tokens.

    The operator's tail (time word and filler) begins at the first time word; a time word is a table row whose
    meaning mentions "time word". Everything before it is rendered, code words in brackets.
    """
    words = text.split(" ")
    out = []
    counts = {"C": 0, "I": 0, "M": 0}
    tail = []
    for w in words:
        if tail:
            tail.append(w)
            continue
        core = clean_token(w)
        stem, flag, row = lookup(core, key)
        if row is None:
            out.append(w)
            continue
        meaning, grade = pick(row, day)
        counts[grade[0]] = counts.get(grade[0], 0) + 1
        if "time word" in meaning:
            hour = meaning.split("(")[0].strip()
            tail.append("{time " + stem + (": " + hour if hour else ": hour unresolved") + "}")
            continue
        out.append(w.replace(core, "[" + meaning + "]" + flag if not flag.startswith("s") else "[" + meaning + "]'s" + flag[1:]))
    reading = " ".join(out)
    if tail:
        reading += "  " + tail[0] + ((" {tail: " + " ".join(tail[1:]) + "}") if len(tail) > 1 else "")
    return reading, counts


def derive(key, blocks):
    parts = []
    total = {"C": 0, "I": 0, "M": 0}
    for header, lines in blocks:
        text = entry_text(lines)
        reading, counts = decode_entry(text, key, parse_day(header.split("|")[3]))
        for k, v in counts.items():
            total[k] = total.get(k, 0) + v
        grade_line = ", ".join(f"{k} {v}" for k, v in sorted(counts.items()) if v)
        parts.append(f"**{header}**\n\n{reading}\n\nCode-word tokens: {grade_line or 'none'}.\n")
    parts.append("Totals over the ten entries: " + ", ".join(f"{k} {v}" for k, v in sorted(total.items())) + ".")
    return "\n".join(parts).rstrip() + "\n"


def main(argv):
    key = load_key()
    if "--at" in argv:
        i = argv.index("--at")
        day = parse_day(argv[i + 1])
        for w in argv[i + 2:]:
            rows = key.get(w.lower())
            print(f"{w}\t{day}\t" + ("not in key.md" if not rows else "\t".join(pick(rows, day))))
        return 0
    blocks = load_ciphertext()
    derived = derive(key, blocks)
    reading_path = HERE / "reading.md"
    if "--write" in argv:
        current = reading_path.read_text(encoding="utf-8") if reading_path.exists() else f"{START}\n{END}\n"
        if START not in current or END not in current:
            sys.exit("reading.md lacks the derived-block markers")
        head, rest = current.split(START, 1)
        _, foot = rest.split(END, 1)
        reading_path.write_text(head + START + "\n" + derived + END + foot, encoding="utf-8")
        print("reading.md updated")
        return 0
    if "--check" in argv:
        current = reading_path.read_text(encoding="utf-8")
        inside = current.split(START, 1)[1].split(END, 1)[0].strip("\n") + "\n"
        if inside != derived:
            sys.stderr.write("reading.md is stale: the derived block differs from decode.py output\n")
            return 1
        print("reading.md is current")
        return 0
    print(derived)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
