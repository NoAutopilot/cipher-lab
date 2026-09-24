#!/usr/bin/env python3
"""Reading of Thurloe letter P8 from its own printed interlinear decipherment.

LANE T worker D (24 Sept 2026): P8 was extracted under the heading "Lord chief
baron Steele to secretary Thurloe" (djvu line 45193, printed p.289 per the MS
marginal note), but that letter ends at line 45222, signed "William Steele.";
the heading directly above P8's cipher (djvu 45229, printed page 541 per the
running head at 45227) is "General Blake to the protector.", signed "Rob.
Blake." and dated "George, June 12, 1655." (djvu 45228-45307). "key_steele.tsv"
and this script's name are kept for continuity with the brief that assigned
them; the letter is Blake's, not Steele's -- see NOTES.md section 13. This is
Blake's 12 June 1655 letter to the Protector, p.541, that Tomokiyo's thurloe.htm
"General Blake (1655)" section names as "almost entirely in cipher" (distinct
from the 4 July 1655 letter at p.611 already handled as P9 in decode.py).

Birch sets the contemporary decipherment letter-by-letter above/below each
cipher line of this letter (25 pairs, djvu 45229-45309), the same technique as
the Fauconberg-Henry Cromwell letters (NOTES.md section 8) and the Montagu
journal-letter (section 9, decode.py). tools/interlinear_align.py aligns the
groups to the printed letters; Tomokiyo's key_blake.tsv (from OTHER Blake/Hague
correspondence, not this letter) values are kept at grade H where they occur
here, and every value the print itself establishes (agreeing at two or more
places in this letter) is grade C -- known plaintext from the print, not a
cryptanalytic result. No cryptanalysis is performed: no guess, repair or
extension is made to any value the alignment does not itself support.

Reproducible per CLAUDE.md rule 7: python3 decode_steele.py regenerates
key_steele.tsv and reading_P8.txt from P8_pairs.tsv + key_blake.tsv;
--check recomputes in memory and exits non-zero if either is stale.
"""
import argparse
import csv
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent.parent / "tools"))
import interlinear_align as ia  # noqa: E402

PAIRS = HERE / "P8_pairs.tsv"
BLAKE_KEY = HERE / "key_blake.tsv"
OUT_KEY = HERE / "key_steele.tsv"
OUT_READING = HERE / "reading_P8.txt"


def load_blake_key():
    key = {}
    with open(BLAKE_KEY, encoding="utf-8") as f:
        for row in csv.DictReader(f, delimiter="\t"):
            key[int(row["value"])] = row["meaning"]
    return key


def tsv(header, rows):
    return "\n".join("\t".join(str(x) for x in r) for r in [header] + rows) + "\n"


def build():
    tomo = load_blake_key()
    with open(PAIRS, encoding="utf-8") as f:
        pairs = list(csv.DictReader(f, delimiter="\t"))
    prepared, results, counts, shown = ia.run_align(pairs)
    rows = ia.token_rows(prepared, results, counts, shown)
    align = {(r[0], r[1]): r for r in rows}

    key_rows = []
    for v in sorted(counts):
        cnt = counts[v]
        top, topn = ia.top_of(cnt)
        rest = sorted(cnt.items(), key=lambda kv: (-kv[1], kv[0]))[1:]
        meaning = ia.display(shown, v, top)
        if v in tomo:
            agrees = ia.fold(tomo[v].lower()) == top
            grade, src = ("H", "Tomokiyo thurloe.htm key_blake.tsv; print agrees" if agrees
                          else "Tomokiyo thurloe.htm key_blake.tsv; print differs")
            meaning = tomo[v]
        elif topn >= 2:
            grade, src = "C", "printed interlinear, %d agreeing places" % topn
        else:
            grade, src = "M", "printed interlinear, one place only"
        others = ",".join("%s:%d" % (ia.display(shown, v, m), c) for m, c in rest)
        key_rows.append([v, meaning, grade, sum(cnt.values()), topn, others, src])
    for v in sorted(set(tomo) - set(counts)):
        key_rows.append([v, tomo[v], "H", 0, 0, "", "Tomokiyo thurloe.htm key_blake.tsv; not in this letter's aligned pairs"])
    key_rows.sort(key=lambda r: r[0])

    grades = Counter()
    out = []
    for p, raw, toks, letters, starts, ends in prepared:
        line = p["cipher_line"]
        for k, tokraw in enumerate(raw):
            r = align.get((line, k))
            if r is None:
                g, reading, note = "U", "", "not aligned"
            else:
                _, _, rawtok, kind, value, repair, chunk, status = r
                note = status
                if kind == "clear":
                    g, reading = "-", ""
                elif kind == "doubtful":
                    if repair:
                        g, reading, note = "I", ia.display(shown, int(repair), ia.top_of(counts[int(repair)])[0]), "repaired to %s" % repair
                    else:
                        g, reading = "U", chunk
                elif int(value) in tomo:
                    g, reading = "H", tomo[int(value)]
                    if chunk and ia.fold(chunk) != ia.fold(tomo[int(value)].lower()):
                        note = "print aligned %r here" % chunk
                elif status == "agrees":
                    g, reading = "C", ia.display(shown, int(value), ia.fold(chunk))
                elif status == "null-or-unaligned":
                    g, reading = "U", ""
                else:
                    g, reading = "M", chunk
            grades[g] += 1
            out.append("L%s\t%s\t%s\t%s\t%s" % (line, tokraw, g, reading, note))

    total = sum(grades.values())
    ncipher = total - grades["-"]
    header = [
        "# Reading of Thurloe letter P8 (General Blake to the protector, aboard the George,",
        "# 12 June 1655, printed p.541 -- Tomokiyo's 'almost entirely in cipher' Blake letter,",
        "# NOT Lord chief baron Steele's letter that precedes it in the OCR text) from the",
        "# decipherment printed above the cipher in the 1742 edition, aligned by",
        "# tools/interlinear_align.py against P8_pairs.tsv. Tomokiyo's key_blake.tsv values",
        "# (reconstructed from OTHER Blake/Hague letters) kept at H. Regenerate: python3 decode_steele.py",
        "# Grades over %d tokens: %d not cipher groups (-); of %d cipher groups H=%d C=%d I=%d M=%d U=%d"
        % (total, grades["-"], ncipher, grades["H"], grades["C"], grades["I"], grades["M"], grades["U"]),
        "# No matched control run (no S grades; every meaning comes from the print or Tomokiyo).",
        "#",
        "# Columns: djvu-line  raw-token  grade  reading  alignment-status",
        "#" + "=" * 74,
    ]
    reading_text = "\n".join(header + out) + "\n"
    key_text = tsv(["value", "meaning", "grade", "n_in_letter", "n_agree", "other_alignments", "source"], key_rows)
    return key_text, reading_text, grades


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()

    key_text, reading_text, grades = build()
    stale = False
    for path, text in ((OUT_KEY, key_text), (OUT_READING, reading_text)):
        if a.check:
            if not path.exists() or path.read_text(encoding="utf-8") != text:
                print("STALE: %s" % path.name, file=sys.stderr)
                stale = True
        else:
            path.write_text(text, encoding="utf-8")
    total = sum(grades.values())
    print("P8: tokens=%d H=%d C=%d I=%d M=%d U=%d not-cipher=%d"
          % (total, grades["H"], grades["C"], grades["I"], grades["M"], grades["U"], grades["-"]))
    if a.check and stale:
        sys.exit(1)


if __name__ == "__main__":
    main()
