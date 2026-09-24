#!/usr/bin/env python3
"""Mechanically apply Tomokiyo's PARTIAL reconstructed keys (thurloe.htm) to the
5 Thurloe letters whose cipher system he has identified from OTHER correspondence
(Blake, Montagu x2, Protector-to-Blake-and-Montagu, Downing). Tomokiyo's page does
not print a full nomenclator for any of these systems -- only a handful of letter
homophones (E) plus a short list of higher-value code words per system, reconstructed
by him from letters this project has not re-verified beyond the crib checks already
logged in NOTES.md. This script applies exactly those published values, nothing more:
it does not guess, repair, or extend the key.

Reproducible per CLAUDE.md rule 7: regenerates reading_<letter>.txt from the
ciphertext.txt file(s) and the relevant key_*.tsv. --check recomputes in memory and
exits non-zero if a committed reading file is stale.

Grading:
  H  the CLEANED token (after thurloe_extract.py's own l/i->1, o->0 normalisation)
     parses as a bare integer that is a key in the relevant key_*.tsv.
  M  thurloe_extract.py itself marked the token doubtful (trailing '?' in CLEANED --
     not a clean 1-4 digit run even after normalisation).
  U  a clean integer that is simply not one of the few values the key covers (the
     overwhelming majority, since each system has ~600 real code elements and the
     published key gives only a dozen or so).
"""
import argparse
import csv
import re
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent.parent / "tools"))
import interlinear_align as ia  # noqa: E402

# P11-13 extended reading (24 Sept 2026): the 1742 print sets a decipherment above
# every cipher line of this letter; tools/interlinear_align.py aligns it to the
# groups from montagu_1656-05-29_pairs.tsv (all 89 pairs of the letter, verbatim
# OCR). Grades for the extended reading:
#   H  value in key_montagu.tsv (Tomokiyo) -- meaning from the key source
#   C  meaning from the printed decipherment, the group aligned to the same chunk
#      at two or more places in the letter (control: 100% of such tokens correct)
#   I  OCR-doubtful token repaired: exactly one digit-confusion candidate is a value
#      whose meaning matches the chunk aligned here (control: 100%)
#   M  printed chunk aligned but not confirmed (one occurrence, control 80%) or in
#      conflict with the same group elsewhere in the letter
#   U  not read: doubtful token with no single repair, or no chunk aligned
#   -  not a cipher group (parenthesised numeral or word printed in clear)
PAIRS = "montagu_1656-05-29_pairs.tsv"
EXT_KEY = "key_montagu_extended.tsv"
EXT_ALIGN = "align_montagu.tsv"
EXT_READING = "reading_P11-13.txt"

# (letter id, [row ciphertext.txt files in reading order], key file, reading-output file)
LETTERS = [
    ("P9", ["P9/ciphertext.txt"], "key_blake.tsv", "reading_P9.txt"),
    ("P14", ["P14/ciphertext.txt"], "key_montagu.tsv", "reading_P14.txt"),
    ("P15", ["P15/ciphertext.txt"], "key_montagu.tsv", "reading_P15.txt"),
    ("P17", ["P17/ciphertext.txt"], "key_downing.tsv", "reading_P17.txt"),
]

CLEANED_LINE_RE = re.compile(r"CLEANED: (.*)$")


def load_key(path):
    key = {}
    with open(path, encoding="utf-8") as f:
        for row in csv.DictReader(f, delimiter="\t"):
            key[int(row["value"])] = row["meaning"]
    return key


def cleaned_tokens(ciphertext_path):
    """Yield (lineno_tag, raw_cleaned_token) for every CLEANED line's tokens."""
    out = []
    for line in ciphertext_path.read_text(encoding="utf-8").split("\n"):
        m = CLEANED_LINE_RE.search(line)
        if not m:
            continue
        tag = line.split("\t", 1)[0]
        for tok in m.group(1).split():
            out.append((tag, tok))
    return out


def classify(token, key):
    """Return (kind, note) for one CLEANED token."""
    doubtful = token.endswith("?")
    core = token.rstrip("?").rstrip(".,;:")
    if doubtful:
        return "M", core
    if core.isdigit():
        n = int(core)
        if n in key:
            return "H", key[n]
        return "U", str(n)
    # punctuation-only or a stray non-numeral survivor (e.g. "qu'0n?" already
    # caught by doubtful above); anything else falls through as unread
    return "U", core


def decode_letter(letter_id, files, key):
    grades = Counter()
    out_lines = []
    for rel in files:
        for tag, tok in cleaned_tokens(HERE / rel):
            kind, note = classify(tok, key)
            grades[kind] += 1
            out_lines.append("%s\t%s\t%s\t%s" % (tag, tok, kind, note))
    return grades, out_lines


def render(letter_id, grades, out_lines):
    total = sum(grades.values())
    header = [
        "# Mechanical reading of Thurloe letter %s against Tomokiyo's partial key" % letter_id,
        "# (thurloe.htm), applied unchanged. Regenerate: python3 decode.py",
        "# Grades: H=%d M=%d U=%d (of %d cipher tokens total)" % (grades["H"], grades["M"], grades["U"], total),
        "#",
        "# Columns: djvu-line-tag  CLEANED-token  grade  decoded-value-or-token",
        "#" + "=" * 74,
    ]
    return "\n".join(header + out_lines) + "\n"


def tsv(header, rows):
    return "\n".join("\t".join(str(x) for x in r) for r in [header] + rows) + "\n"


def extended_p11_13():
    """-> {filename: rendered text} for the aligned key, alignment and reading."""
    tomo = load_key(HERE / "key_montagu.tsv")
    with open(HERE / PAIRS, encoding="utf-8") as f:
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
            grade, src = "H", "Tomokiyo thurloe.htm; print agrees" if ia.fold(tomo[v].lower()) == top else "Tomokiyo thurloe.htm; print differs"
            meaning = tomo[v]
        elif topn >= 2:
            grade, src = "C", "printed interlinear, %d agreeing places" % topn
        else:
            grade, src = "M", "printed interlinear, one place"
        others = ",".join("%s:%d" % (ia.display(shown, v, m), c) for m, c in rest)
        key_rows.append([v, meaning, grade, sum(cnt.values()), topn, others, src])
    for v in sorted(set(tomo) - set(counts)):
        key_rows.append([v, tomo[v], "H", 0, 0, "", "Tomokiyo thurloe.htm; not in this letter"])
    key_rows.sort(key=lambda r: r[0])

    grades = Counter()
    out = []
    for rel in ["P11/ciphertext.txt", "P12/ciphertext.txt", "P13/ciphertext.txt"]:
        idx = Counter()
        for tag, tok in cleaned_tokens(HERE / rel):
            line = tag.lstrip("L")
            k = idx[tag]
            idx[tag] += 1
            r = align.get((line, k))
            if r is None:
                g, reading, note = "U", "", "line not in pairs file"
            else:
                _, _, raw, kind, value, repair, chunk, status = r
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
            out.append("%s\t%s\t%s\t%s\t%s" % (tag, tok, g, reading, note))
    total = sum(grades.values())
    ncipher = total - grades["-"]
    header = [
        "# Reading of Thurloe letter P11-13 (Montagu to Thurloe, journal-letter begun 20 April 1656,",
        "# endorsed 29 May 1656) from the decipherment printed above the cipher in the 1742 edition,",
        "# aligned by tools/interlinear_align.py; Tomokiyo's key values kept at H. Regenerate:",
        "# python3 decode.py",
        "# Grades over the %d CLEANED tokens: %d not cipher groups (-); of %d cipher groups"
        % (total, grades["-"], ncipher),
        "# H=%d C=%d I=%d M=%d U=%d" % (grades["H"], grades["C"], grades["I"], grades["M"], grades["U"]),
        "# Matched control: control_interlinear.py / control_result.tsv",
        "#",
        "# Columns: djvu-line-tag  CLEANED-token  grade  reading  alignment-status",
        "#" + "=" * 74,
    ]
    return {
        EXT_KEY: tsv(["value", "meaning", "grade", "n_in_letter", "n_agree", "other_alignments", "source"], key_rows),
        EXT_ALIGN: tsv(["cipher_line", "idx", "raw", "kind", "value", "repair", "plain_chunk", "status"], rows),
        EXT_READING: "\n".join(header + out) + "\n",
    }, grades


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()

    stale = False
    report = []
    for letter_id, files, keyfile, outfile in LETTERS:
        key = load_key(HERE / keyfile)
        grades, out_lines = decode_letter(letter_id, files, key)
        rendered = render(letter_id, grades, out_lines)
        out_path = HERE / outfile
        if a.check:
            if not out_path.exists() or out_path.read_text(encoding="utf-8") != rendered:
                print("STALE: %s" % outfile, file=sys.stderr)
                stale = True
        else:
            out_path.write_text(rendered, encoding="utf-8")
        total = sum(grades.values())
        report.append((letter_id, grades["H"], grades["M"], grades["U"], total))

    ext, eg = extended_p11_13()
    for name, text in ext.items():
        p = HERE / name
        if a.check:
            if not p.exists() or p.read_text(encoding="utf-8") != text:
                print("STALE: %s" % name, file=sys.stderr)
                stale = True
        else:
            p.write_text(text, encoding="utf-8")
    print("P11-13 extended: H=%d C=%d I=%d M=%d U=%d not-cipher=%d" % (eg["H"], eg["C"], eg["I"], eg["M"], eg["U"], eg["-"]))

    print("letter\tH\tM\tU\ttotal")
    for letter_id, h, m, u, total in report:
        print("%s\t%d\t%d\t%d\t%d" % (letter_id, h, m, u, total))

    if a.check and stale:
        sys.exit(1)


if __name__ == "__main__":
    main()
