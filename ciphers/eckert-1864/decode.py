#!/usr/bin/env python3
"""Re-derive the readings in reading.md from ciphertext.txt and the tables in key.md (Cipher No. 1, mssEC 41).

An mssEC 19 entry is dictionary-coded plaintext written in the order the sender gave it (no route transposition
is recorded in the ledger): a blind word (the column indicator of the route pages), a time word, the month and
the day in numeral words, the text with names, places, ranks, punctuation and many common words replaced by the
book's arbitraries, the word for "signature", the coded signature, and filler. The reading replaces every code
word by its meaning in brackets and grades each code-word token with the grade of its table row (H = read from
mssEC 41, C = known plaintext, I = inferred from another entry, M = uncertain). Numeral words are combined the
English way (twenty + six = 26; two + thousand + five + hundred = 2500). A code word carrying "ed", "ing" or "s"
is read as the stem plus the ending (the book's own rule, foot of page 24). Words not in any table are left as
written: they are the sender's plain words (including the phonetic spellings "tooth", "toby", "canby").

Usage:  python3 decode.py            # print the readings and the grade counts
        python3 decode.py --check    # exit 1 if the block in reading.md differs from what is derived now
        python3 decode.py --write    # rewrite the derived block inside reading.md
"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
START = "<!-- decode.py: derived block starts -->"
END = "<!-- decode.py: derived block ends -->"

PUNCT = {"period": ".", "comma": ",", "semicolon": ";", "semi colon": ";", "colon": ":", "interrogation": "?",
         "interogation": "?", "paragraph": "(paragraph)", "quotation": '"', "exclamation": "!", "dash": "-",
         "parenthesis": "( )", "hyphen": "-"}
MONTHS = {"jany": "Jan", "jan": "Jan", "feby": "Feb", "feb": "Feb", "mch": "Mar", "march": "Mar", "mar": "Mar",
          "april": "Apr", "apl": "Apr", "apr": "Apr", "may": "May", "june": "June", "july": "July", "aug": "Aug",
          "sept": "Sept", "sep": "Sept", "oct": "Oct", "nov": "Nov", "novr": "Nov", "dec": "Dec", "decr": "Dec"}


def load_key(path=HERE / "key.md"):
    """Return {code word (lower): (meaning, grade, kind)} from every '| code word |' table in key.md.

    kind is one of: word, numeral, time, blind, line, punct, sig, month-free. It is taken from a parenthesised
    tag at the end of the meaning ("(numeral)", "(time word)", "(blind word ...)", "(line indicator ...)") or
    from the meaning itself for punctuation and "Signature"."""
    table = {}
    in_table = False
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("| code word |"):
            in_table = True
            continue
        if not in_table:
            continue
        if not line.startswith("|"):
            in_table = False
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 3 or set(cells[0]) <= {"-"}:
            continue
        word, meaning, grade = cells[0], cells[1], cells[2]
        low = meaning.lower()
        kind = "word"
        if low.endswith("(numeral)"):
            kind = "numeral"
        elif "(time word)" in low:
            kind = "time"
        elif low.startswith("blind word"):
            kind = "blind"
        elif low.startswith("line indicator"):
            kind = "line"
        elif low in PUNCT:
            kind = "punct"
        elif low in ("signature", "signed"):
            kind = "sig"
        for w in word.split("/"):
            table[w.strip().lower()] = (meaning, grade[0], kind)
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
            if raw.startswith("#") or raw.startswith("<!--") or raw.startswith("note:"):
                continue
            lines.append(raw.rstrip())  # "plain:" lines are kept and read by entry_text
    if header:
        blocks.append((header, lines))
    if not blocks:
        sys.exit("no '### ' blocks found in ciphertext.txt")
    return blocks


def entry_text(lines):
    """Join the manuscript lines after the header line, dropping <del>..</del>, the <ins> tags and the '=' joins.

    A line "plain: word word" (the orchestrator's note that these tokens are the sender's plain English although
    they are printed in the book, e.g. "person" in "one additional person") is not text: its words are marked
    with a trailing backslash so that lookup() leaves them alone."""
    plain = set()
    body = []
    for l in lines[1:]:
        if l.startswith("plain:"):
            plain.update(w.lower() for w in l[6:].split())
        elif l.strip():
            body.append(l)
    text = " ".join(body)
    text = re.sub(r"<del>.*?</del>", " ", text)
    text = re.sub(r"</?ins>", "", text)
    text = re.sub(r"\s+=\s+", "", text)  # "Lock = wood" -> "Lockwood"
    text = re.sub(r"\s+-\s+", "", text)  # "dis - missed" -> "dismissed"
    text = re.sub(r"\s+", " ", text).strip()
    if plain:
        text = " ".join(w + "\\" if w.strip(" .,;:'\"()").lower() in plain else w for w in text.split(" "))
    return text


def lookup(core, key):
    """Return (stem, ending, row) for a token, allowing the doubtful flag [?] and the endings s, es, ed, d, ing."""
    flag = ""
    if core.endswith("\\"):
        return core[:-1], "", None
    if core.endswith("[?]"):
        core, flag = core[:-3], "[?]"
    low = core.lower()
    if low in key:
        return core, flag, key[low]
    for end in ("s", "es", "ed", "d", "ing", "ers", "er"):
        if low.endswith(end) and low[: -len(end)] in key:
            return core[: -len(end)], end + flag, key[low[: -len(end)]]
    if low.endswith("ing") and low[:-3] + "e" in key:
        return core[:-3] + "e", "ing" + flag, key[low[:-3] + "e"]
    return core, flag, None


def number(values):
    """Combine numeral values the English way: [20, 6] -> 26; [2, 1000, 5, 100] -> 2500."""
    total, cur = 0, 0
    for v in values:
        if v in (100, 1000):
            cur = (cur or 1) * v
            if v == 1000:
                total, cur = total + cur, 0
        else:
            cur += v
    return total + cur


def decode_entry(text, key):
    """Return (reading, counts). The tail (signature marker onwards) is set apart in braces."""
    words = text.split(" ")
    out = []
    counts = {"H": 0, "C": 0, "I": 0, "M": 0}
    i = 0
    signed = False
    tail = []
    while i < len(words):
        w = words[i]
        core = w.strip(" .,;:'\"()")
        stem, flag, row = lookup(core, key)
        if row is not None and row[2] in ("blind", "line"):
            # route indicators are never used inside an untransposed entry, and the printed words collide with
            # plain English ("must", "wait", "week", "June", "Army"): left as written, not graded
            row = None
        if row is None:
            w = w.replace("\\", "")
            if core.lower() in MONTHS and i + 1 < len(words):
                # month followed by numeral words: read the date
                j, vals = i + 1, []
                while j < len(words):
                    s2, f2, r2 = lookup(words[j].strip(" .,;:'\"()"), key)
                    if r2 and r2[2] == "numeral":
                        vals.append(int(r2[0].split()[0]))
                        counts[r2[1]] += 1
                        j += 1
                    else:
                        break
                if vals:
                    out.append(f"{{date: {MONTHS[core.lower()]} {number(vals)}}}")
                    i = j
                    continue
            (tail if signed else out).append(w)
            i += 1
            continue
        meaning, grade, kind = row
        counts[grade] = counts.get(grade, 0) + 1
        if kind == "numeral":
            j, vals = i, []
            while j < len(words):
                s2, f2, r2 = lookup(words[j].strip(" .,;:'\"()"), key)
                if r2 and r2[2] == "numeral":
                    vals.append(int(r2[0].split()[0]))
                    if j > i:
                        counts[r2[1]] += 1
                    j += 1
                else:
                    break
            rendered = "[" + str(number(vals)) + "]" + flag
            i = j
        elif kind == "time":
            rendered = "{time: " + meaning.split("(")[0].strip() + "}" + flag
            i += 1
        elif kind == "punct":
            rendered = "[" + PUNCT[meaning.lower()] + "]" + flag
            i += 1
        elif kind == "sig":
            signed = True
            rendered = "[signed]"
            i += 1
        else:
            end = flag.replace("[?]", "")
            q = "[?]" if flag.endswith("[?]") else ""
            rendered = "[" + meaning + "]" + ("'" + end if end == "s" and meaning[:1].isupper() else end) + q
            i += 1
        (tail if signed else out).append(rendered)
    reading = " ".join(out)
    if tail:
        reading += "  {tail: " + " ".join(tail) + "}"
    return reading, counts


def derive(key, blocks):
    parts = []
    total = {"H": 0, "C": 0, "I": 0, "M": 0}
    for header, lines in blocks:
        text = entry_text(lines)
        reading, counts = decode_entry(text, key)
        for k, v in counts.items():
            total[k] = total.get(k, 0) + v
        grade_line = ", ".join(f"{k} {v}" for k, v in counts.items() if v)
        parts.append(f"**{header}**\n\n{reading}\n\nCode-word tokens: {grade_line or 'none'}.\n")
    parts.append(f"Totals over the {len(blocks)} entries: " + ", ".join(f"{k} {v}" for k, v in total.items()) + ".")
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
