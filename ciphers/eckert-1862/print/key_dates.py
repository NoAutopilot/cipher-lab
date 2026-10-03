#!/usr/bin/env python3
"""Fill or check the "witness dates" column of key.md: the first and last ledger date of the telegrams that support
each row (GAPS127, 3 Oct 2026).

Witnesses per row, all from disk:
  (a) the ten transcribed entries (ciphertext.txt) whose text uses the code word, dated by their header;
  (b) ledger pages cited in the row's evidence as "p.[n]" (pointer = 4955 + n; page [9] = 4964, ciphertext T1),
      except "on p.[n]", which key.md uses for a page where the word stands with a different meaning;
  (c) ledger pointers cited after "ledger" in the evidence ("ledger 5095, 5079", "5060-5092": the endpoints);
  (d) "OR 7 p.N" pages, mapped to ledger pointers through print/or_matches.tsv (vol. 7 rows only);
  (e) print/align*/align_pairs.tsv occurrences of the word whose printed meaning agrees with the row's meaning;
  (f) for time words, the day-month dates written in the evidence ("ledger: 7 Feb 7.15 PM, 15 Feb 8 PM").
A row whose evidence says "dated split" or "true conflict" is a later value of a word that also has a Feb row
(GAPS127): it takes witnesses from (c) and (e) only, since the ten Feb entries, the Feb ledger pages and the OR 7
pages it mentions are witnesses of the other value.
A pointer is dated from print/or_matches.tsv's ledger head (the entry's own date as written); an undated pointer
takes the range between the nearest dated pointers on either side (the ledger is kept in date order, 1 Feb to
21 July 1862), so its witness widens the row's range rather than narrowing it.

Usage:  python3 print/key_dates.py            # print word, meaning, computed range, witness count
        python3 print/key_dates.py --write    # write the computed range into key.md's "witness dates" column
        python3 print/key_dates.py --check    # exit 1 if any key.md row's column differs from the computed range
"""
import csv
import datetime as dt
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
TARGET = HERE.parent
MONTHS = {"jan": 1, "feb": 2, "mar": 3, "mch": 3, "apr": 4, "may": 5, "jun": 6, "jul": 7, "aug": 8}
DATE_RE = re.compile(r"\b(Jan|Feb|Mar|Mch|Apr|May|Jun|Jul|Aug)[a-z]*\.?\s*(\d{1,2})", re.I)
FIRST, LAST = dt.date(1862, 2, 1), dt.date(1862, 7, 21)


def parse_date(text):
    m = DATE_RE.search(text or "")
    if not m:
        return None
    return dt.date(1862, MONTHS[m.group(1)[:3].lower()], int(m.group(2)))


def pointer_dates():
    """Return {pointer: (earliest, latest)} for every pointer 4955-5126."""
    dated = {}
    or7 = {}
    with open(HERE / "or_matches.tsv", encoding="utf-8") as f:
        for row in csv.DictReader(f, delimiter="\t"):
            p = int(row["pointer"])
            d = parse_date(row["ledger_head"])
            if d:
                dated[p] = d
            if row["volume"] == "warofrebellionco0007vari" and row["or_page"].isdigit():
                or7.setdefault(int(row["or_page"]), set()).add(p)
    for header, _ in load_entries():
        p = int(header.split("|")[2])
        dated.setdefault(p, parse_date(header.split("|")[3]))
    out = {}
    keys = sorted(dated)
    for p in range(4955, 5127):
        if p in dated:
            out[p] = (dated[p], dated[p])
            continue
        before = [dated[k] for k in keys if k < p]
        after = [dated[k] for k in keys if k > p]
        out[p] = (max(before) if before else FIRST, min(after) if after else LAST)
    return out, or7


def load_entries():
    sys.path.insert(0, str(TARGET))
    import decode
    return decode.load_ciphertext()


def norm(s):
    return re.sub(r"[^a-z]", "", s.lower())


def meaning_agrees(printed, meaning):
    m = norm(re.sub(r"\(.*?\)", "", meaning).replace("the ", ""))
    p = norm(printed.replace("the ", ""))
    p = p.replace("frederieksburg", "fredericksburg").replace("kiver", "river").replace("tranportation", "transportation")
    return bool(m) and (m in p or p in m)


def key_rows(path=TARGET / "key.md"):
    """Yield (line index, cells) for the vocabulary table rows."""
    lines = path.read_text(encoding="utf-8").splitlines()
    in_table = False
    for i, line in enumerate(lines):
        if line.startswith("| code word |"):
            in_table = True
            continue
        if in_table:
            if not line.startswith("|"):
                break
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if set(cells[0]) <= {"-"}:
                continue
            yield i, cells


def witnesses(word, meaning, evidence, pdates, or7, entries, pairs):
    w = word.lower()
    found = []  # (earliest, latest, label)
    alt = "dated split" in evidence or "true conflict" in evidence
    for header, lines in ([] if alt else entries):
        text = " ".join(lines).lower()
        text = re.sub(r"<del>.*?</del>", " ", text)
        toks = {t.strip(" .,;:'\"()[]?") for t in text.split()}
        if w in toks or w + "s" in toks:
            d = parse_date(header.split("|")[3])
            found.append((d, d, header.split("|")[0].strip("# ").strip()))
    if "time word" not in meaning:
        for n in ([] if alt else re.findall(r"(?<!on p\.)\[(\d+)\]", evidence)):
            p = 4955 + int(n)
            if p in pdates:
                found.append((*pdates[p], f"p.[{n}]"))
        for seg in re.findall(r"ledger ([\d ,\-]+)", evidence):
          for a, b in re.findall(r"\b(49[5-9]\d|50\d\d|51[0-2]\d)(?:-(\d{4}))?\b", seg):
            for p in filter(None, (a, b)):
                if int(p) in pdates:
                    found.append((*pdates[int(p)], p))
        for seg in ([] if alt else re.findall(r"OR 7 p\.([\d ,\-]+)", evidence)):
            for page in re.findall(r"\d+", seg):
                for p in or7.get(int(page), ()):
                    found.append((*pdates[p], f"OR7 p.{page}={p}"))
        for p, lw, printed in pairs:
            if lw.lower().rstrip("s") in (w, w.rstrip("s")) and meaning_agrees(printed, meaning):
                found.append((*pdates[p], f"{p}"))
    else:
        for m in re.finditer(r"(\d{1,2}) Feb", evidence):
            d = dt.date(1862, 2, int(m.group(1)))
            found.append((d, d, m.group(0)))
    return found


def compute():
    pdates, or7 = pointer_dates()
    entries = load_entries()
    pairs = []
    for f in sorted(HERE.glob("align*/align_pairs.tsv")):
        with open(f, encoding="utf-8") as fh:
            for row in csv.DictReader(fh, delimiter="\t"):
                pairs.append((int(row["pointer"]), row["ledger_word"], row["printed"]))
    result = {}
    for i, cells in key_rows():
        word, meaning, evidence = cells[0], cells[1], cells[-1]
        found = witnesses(word, meaning, evidence, pdates, or7, entries, pairs)
        if found:
            lo = min(f[0] for f in found)
            hi = max(f[1] for f in found)
            rng = f"{lo:%d %b}-{hi:%d %b} 1862" if lo != hi else f"{lo:%d %b} 1862"
        else:
            rng = "undated"
        result[i] = (cells, rng, len({f[2] for f in found}))
    return result


def main(argv):
    result = compute()
    path = TARGET / "key.md"
    lines = path.read_text(encoding="utf-8").splitlines()
    stale = 0
    for i, (cells, rng, n) in result.items():
        if len(cells) < 5:
            sys.exit(f"key.md row '{cells[0]}' has no witness-dates column")
        if cells[3] != rng:
            stale += 1
            if "--write" in argv:
                cells[3] = rng
                lines[i] = "| " + " | ".join(cells) + " |"
        if not argv:
            print(f"{cells[0]}\t{cells[1]}\t{cells[2]}\t{rng}\t{n} witnesses")
    if "--write" in argv:
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        print(f"key.md: {stale} witness-date cells written")
        return 0
    if "--check" in argv:
        if stale:
            sys.stderr.write(f"key.md: {stale} witness-date cells differ from print/key_dates.py\n")
            return 1
        print("key.md witness dates are current")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
