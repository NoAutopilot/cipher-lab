#!/usr/bin/env python3
"""Re-derive the readings in reading.md from ciphertext.txt and the vocabulary table in key.md.

The mssEC 15 entries are dictionary-coded plaintext (no route transposition is recorded), so a reading is the
entry with every code word replaced by its meaning in brackets; the operator's tail (the time word and the filler
after it) is set apart in braces. Each code-word token is graded with the grade of its table row (C, I or M);
words not in the table are left as written.

Usage:  python3 decode.py            # print the readings and the grade counts
        python3 decode.py --check    # exit 1 if the block in reading.md differs from what is derived now
        python3 decode.py --write    # rewrite the derived block inside reading.md

Exit status is non-zero when --check finds reading.md stale.
"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
START = "<!-- decode.py: derived block starts -->"
END = "<!-- decode.py: derived block ends -->"

def load_key(path=HERE / "key.md"):
    """Return {code word (lower): (meaning, grade)} from the markdown table in key.md."""
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
            if len(cells) < 4 or set(cells[0]) <= {"-"}:
                continue
            word, meaning, grade = cells[0], cells[1], cells[2]
            table[word.lower()] = (meaning, grade)
    if not table:
        sys.exit("no vocabulary table found in key.md")
    return table


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


def decode_entry(text, key):
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
        meaning, grade = row
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
        reading, counts = decode_entry(text, key)
        for k, v in counts.items():
            total[k] = total.get(k, 0) + v
        grade_line = ", ".join(f"{k} {v}" for k, v in sorted(counts.items()) if v)
        parts.append(f"**{header}**\n\n{reading}\n\nCode-word tokens: {grade_line or 'none'}.\n")
    parts.append("Totals over the ten entries: " + ", ".join(f"{k} {v}" for k, v in sorted(total.items())) + ".")
    return "\n".join(parts).rstrip() + "\n"


def main(argv):
    key = load_key()
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
