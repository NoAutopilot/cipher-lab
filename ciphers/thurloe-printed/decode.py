#!/usr/bin/env python3
"""Mechanically apply Tomokiyo's PARTIAL reconstructed keys (thurloe.htm) to the
Thurloe letters whose cipher system he has identified from OTHER correspondence
(Blake, Montagu, Downing), and, where the 1742 print itself sets a contemporary
decipherment above the cipher (P11-13, P15 for Montagu's system; P9, P10 for
Blake's), align that printed decipherment to the groups with
tools/interlinear_align.py and fold newly-confirmed values into an extended key.
Nothing here is cryptanalysis: every C/H value comes from Tomokiyo's page or from
Birch's own printed decipherment, never guessed or repaired beyond one-candidate
OCR-doubtful repairs already used for P11-13.

Reproducible per CLAUDE.md rule 7: regenerates reading_<letter>.txt (and, for the
aligned letters, key_*_extended.tsv / align_*.tsv) from ciphertext.txt / *_pairs.tsv
and the relevant key_*.tsv. --check recomputes in memory and exits non-zero if a
committed output file is stale.

Grading (mechanical-only letter: P14):
  H  the CLEANED token (after thurloe_extract.py's own l/i->1, o->0 normalisation)
     parses as a bare integer that is a key in the relevant key_*.tsv.
  M  thurloe_extract.py itself marked the token doubtful (trailing '?' in CLEANED --
     not a clean 1-4 digit run even after normalisation).
  U  a clean integer that is simply not one of the few values the key covers.

Grading (aligned letters: P9, P10, P11-13, P15 -- see extended_from_pairs()):
  H  value in the system's Tomokiyo key -- meaning from the key source.
  C  meaning from the printed decipherment, the group aligned to the same chunk
     at two or more places across the letter(s) run together (control on P11-13,
     the first of these: 100% of such tokens correct).
  I  OCR-doubtful token repaired: exactly one digit-confusion candidate is a value
     whose meaning matches the chunk aligned here (control: 100%).
  M  printed chunk aligned but not confirmed (one occurrence, control 80%) or in
     conflict with the same group elsewhere.
  U  not read: doubtful token with no single repair, or no chunk aligned.
  -  not a cipher group (parenthesised numeral or word printed in clear).
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

# (letter id, [row ciphertext.txt files in reading order], key file, reading-output file)
# P9, P11, P12, P13, P15 are handled by extended_from_pairs() instead (the print
# carries a decipherment for them); P10 likewise (extended_from_pairs, Blake system).
LETTERS = [
    ("P14", ["P14/ciphertext.txt"], "key_montagu_extended.tsv", "reading_P14.txt"),
    # P17 removed 24 Sept 2026 (LANE T): it is Fauconberg to H. Cromwell, not Downing;
    # its reading is reading_fauconberg_P17.txt from decode_fauconberg.py. key_downing.tsv
    # (Tomokiyo's Downing values) is kept as a source transcription but no row uses it.
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


def render(letter_id, grades, out_lines, key_note_lines):
    total = sum(grades.values())
    header = list(key_note_lines) + [
        "# Grades: H=%d M=%d U=%d (of %d cipher tokens total)" % (grades["H"], grades["M"], grades["U"], total),
        "#",
        "# Columns: djvu-line-tag  CLEANED-token  grade  decoded-value-or-token",
        "#" + "=" * 74,
    ]
    return "\n".join(header + out_lines) + "\n"


def tsv(header, rows):
    return "\n".join("\t".join(str(x) for x in r) for r in [header] + rows) + "\n"


def load_pairs_file(name):
    with open(HERE / name, encoding="utf-8") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def build_key_rows(tomo, counts, shown, label):
    """Value -> (meaning, grade, n, agree, others, source) from one run_align's
    counts/shown, backfilled with Tomokiyo's own values not seen in the pairs."""
    key_rows = []
    for v in sorted(counts):
        cnt = counts[v]
        top, topn = ia.top_of(cnt)
        rest = sorted(cnt.items(), key=lambda kv: (-kv[1], kv[0]))[1:]
        meaning = ia.display(shown, v, top)
        if v in tomo:
            grade = "H"
            src = "Tomokiyo thurloe.htm; print agrees" if ia.fold(tomo[v].lower()) == top else "Tomokiyo thurloe.htm; print differs"
            meaning = tomo[v]
        elif topn >= 2:
            grade, src = "C", "printed interlinear, %d agreeing places (%s)" % (topn, label)
        else:
            grade, src = "M", "printed interlinear, one place (%s)" % label
        others = ",".join("%s:%d" % (ia.display(shown, v, m), c) for m, c in rest)
        key_rows.append([v, meaning, grade, sum(cnt.values()), topn, others, src])
    for v in sorted(set(tomo) - set(counts)):
        key_rows.append([v, tomo[v], "H", 0, 0, "", "Tomokiyo thurloe.htm; not in these letters"])
    key_rows.sort(key=lambda r: r[0])
    return key_rows


def grade_pairs_tokens(pairs, align, tomo, counts, shown):
    """Grade every cipher_raw token of one pairs list against a shared `align`
    lookup {(cipher_line, idx): token_row} built by ia.token_rows over possibly
    several letters' pairs run together."""
    grades = Counter()
    out = []
    for p in pairs:
        raw = p["cipher_raw"].split()
        for k, tok in enumerate(raw):
            r = align.get((p["cipher_line"], str(k)))
            if r is None:
                g, reading, note = "U", "", "token not in joint alignment"
            else:
                _, _, _, kind, value, repair, chunk, status = r
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
            out.append("%s\t%s\t%s\t%s\t%s" % (p["cipher_line"], tok, g, reading, note))
    return grades, out


def render_extended(letter_label, source_note, grades, out_lines):
    total = sum(grades.values())
    ncipher = total - grades["-"]
    header = [
        "# Reading of Thurloe letter %s from the decipherment printed above the cipher" % letter_label,
        "# in the 1742 edition (%s)," % source_note,
        "# aligned by tools/interlinear_align.py; Tomokiyo's key values kept at H. Regenerate:",
        "# python3 decode.py",
        "# Grades over the %d cipher tokens: %d not cipher groups (-); of %d cipher groups"
        % (total, grades["-"], ncipher),
        "# H=%d C=%d I=%d M=%d U=%d" % (grades["H"], grades["C"], grades["I"], grades["M"], grades["U"]),
        "#",
        "# Columns: djvu-line-tag  raw-token  grade  reading  alignment-status",
        "#" + "=" * 74,
    ]
    return "\n".join(header + out_lines) + "\n"


def extended_p11_13():
    """P11-13 (Montagu, 20 Apr-29 May 1656): unchanged from the 24 Sept 2026 solver
    pass. -> ({filename: text}, grades, key_rows) so callers can merge key_rows with
    other Montagu-system letters without disturbing this letter's own computation."""
    PAIRS = "montagu_1656-05-29_pairs.tsv"
    tomo = load_key(HERE / "key_montagu.tsv")
    pairs = load_pairs_file(PAIRS)
    prepared, results, counts, shown = ia.run_align(pairs)
    rows = ia.token_rows(prepared, results, counts, shown)
    align = {(r[0], str(r[1])): r for r in rows}

    key_rows = build_key_rows(tomo, counts, shown, "P11-13")

    out_lines = []
    grades = Counter()
    for rel in ["P11/ciphertext.txt", "P12/ciphertext.txt", "P13/ciphertext.txt"]:
        idx = Counter()
        for tag, tok in cleaned_tokens(HERE / rel):
            line = tag.lstrip("L")
            k = idx[tag]
            idx[tag] += 1
            r = align.get((line, str(k)))
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
            out_lines.append("%s\t%s\t%s\t%s\t%s" % (tag, tok, g, reading, note))

    total = sum(grades.values())
    ncipher = total - grades["-"]
    reading_header = [
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
    reading_text = "\n".join(reading_header + out_lines) + "\n"
    files = {
        "key_montagu_extended.tsv": tsv(["value", "meaning", "grade", "n_in_letter", "n_agree", "other_alignments", "source"], key_rows),
        "align_montagu.tsv": tsv(["cipher_line", "idx", "raw", "kind", "value", "repair", "plain_chunk", "status"], rows),
        "reading_P11-13.txt": reading_text,
    }
    return files, grades, key_rows


def extended_p15():
    """P15 (Mountagu to Thurloe, 16 Sept 1656, aboard the Naseby, bay of Wyers/
    river of Lisbon): same Montagu system, its own printed decipherment, aligned
    independently from `P15_pairs.tsv` (18 pairs, djvu 35673-35760, wider than the
    original narrow ciphertext.txt window -- LANE T worker B, 24 Sept 2026)."""
    tomo = load_key(HERE / "key_montagu.tsv")
    pairs = load_pairs_file("P15_pairs.tsv")
    prepared, results, counts, shown = ia.run_align(pairs)
    rows = ia.token_rows(prepared, results, counts, shown)
    align = {(r[0], str(r[1])): r for r in rows}
    key_rows = build_key_rows(tomo, counts, shown, "P15")
    grades, out_lines = grade_pairs_tokens(pairs, align, tomo, counts, shown)
    reading_text = render_extended(
        "P15 (Gen. Mountagu to Thurloe, 16 Sept 1656, aboard the Naseby)",
        "IA collectionofstat05thur, printed p.~411 (running head), djvu 35673-35760",
        grades, out_lines,
    )
    return key_rows, {"align_P15.tsv": tsv(["cipher_line", "idx", "raw", "kind", "value", "repair", "plain_chunk", "status"], rows),
                       "reading_P15.txt": reading_text}, grades


def extended_blake():
    """P9 (Blake to the Protector, 4 July 1655, p.611-613) and P10 (Blake to the
    Protector, 6 July 1655, p.620): both carry a printed letter-by-letter
    decipherment, heavily fragmented by OCR into short mini-lines; only the
    cleanly-recoverable fragments are in P9_pairs.tsv/P10_pairs.tsv (LANE T worker
    B, 24 Sept 2026). Run together in one alignment so shared homophones (e, t, r,
    n, o, u -- already in Tomokiyo's key_blake.tsv from a different letter) get
    pooled votes rather than each letter's noise standing alone."""
    tomo = load_key(HERE / "key_blake.tsv")
    p9 = load_pairs_file("P9_pairs.tsv")
    p10 = load_pairs_file("P10_pairs.tsv")
    prepared, results, counts, shown = ia.run_align(p9 + p10)
    rows = ia.token_rows(prepared, results, counts, shown)
    align = {(r[0], str(r[1])): r for r in rows}
    key_rows = build_key_rows(tomo, counts, shown, "P9+P10")

    out = {}
    all_grades = Counter()
    for label, pairs, fname, note in [
        ("P9", p9, "reading_P9.txt", "IA collectionofstat03thur pp.611-613 (4 July 1655), djvu 51500-51610"),
        ("P10", p10, "reading_P10.txt", "IA collectionofstat03thur p.620 (6 July 1655), djvu 52290-52320"),
    ]:
        grades, out_lines = grade_pairs_tokens(pairs, align, tomo, counts, shown)
        out[fname] = render_extended("%s (Gen. Blake to the Protector)" % label, note, grades, out_lines)
        for k, v in grades.items():
            all_grades[k] += v
    out["align_blake.tsv"] = tsv(["cipher_line", "idx", "raw", "kind", "value", "repair", "plain_chunk", "status"], rows)
    return key_rows, out, all_grades


def merge_key_rows(base_rows, extra_rows):
    """base_rows wins on shared values (its own letter's computation is kept
    undisturbed); extra_rows only contributes values base_rows doesn't have."""
    have = {r[0] for r in base_rows}
    merged = list(base_rows) + [r for r in extra_rows if r[0] not in have]
    merged.sort(key=lambda r: r[0])
    return merged


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()

    stale = False
    outputs = {}  # filename -> text, checked/written together at the end

    # Montagu system: P11-13 (unchanged computation) + P15 (new), merged key.
    p11_13_files, p11_13_grades, p11_13_key_rows = extended_p11_13()
    p15_key_rows, p15_files, p15_grades = extended_p15()
    merged_montagu_rows = merge_key_rows(p11_13_key_rows, p15_key_rows)
    merged_montagu_text = tsv(
        ["value", "meaning", "grade", "n_in_letter", "n_agree", "other_alignments", "source"],
        merged_montagu_rows,
    )
    outputs.update(p11_13_files)
    outputs["key_montagu_extended.tsv"] = merged_montagu_text  # overrides p11_13_files' own copy
    outputs.update(p15_files)
    # H or C grade only: an M-graded (single, unconfirmed) value from one letter's
    # own alignment must not be mechanically stamped "H" (read from a key source)
    # when applied to a different letter that has no decipherment of its own.
    montagu_key_dict = {r[0]: r[1] for r in merged_montagu_rows if r[2] in ("H", "C")}

    # Blake system: P9 + P10, jointly aligned.
    blake_key_rows, blake_files, blake_grades = extended_blake()
    outputs["key_blake_extended.tsv"] = tsv(
        ["value", "meaning", "grade", "n_in_letter", "n_agree", "other_alignments", "source"],
        blake_key_rows,
    )
    outputs.update(blake_files)

    # Mechanical-only letters (P14: no printed decipherment found; P17: not this
    # worker's row, key/behaviour unchanged).
    report = []
    for letter_id, files, keyfile, outfile in LETTERS:
        if letter_id == "P14":
            key = montagu_key_dict
            key_note_lines = [
                "# Mechanical reading of Thurloe letter %s against the extended Montagu-system" % letter_id,
                "# key (Tomokiyo thurloe.htm plus this project's P11-13/P15 print-confirmed H/C",
                "# values; M-graded single-occurrence guesses excluded), applied unchanged.",
                "# Regenerate: python3 decode.py",
            ]
        else:
            key = load_key(HERE / keyfile)
            key_note_lines = [
                "# Mechanical reading of Thurloe letter %s against Tomokiyo's partial key" % letter_id,
                "# (thurloe.htm), applied unchanged. Regenerate: python3 decode.py",
            ]
        grades, out_lines = decode_letter(letter_id, files, key)
        outputs[outfile] = render(letter_id, grades, out_lines, key_note_lines)
        total = sum(grades.values())
        report.append((letter_id, grades["H"], grades["M"], grades["U"], total))

    for name, text in outputs.items():
        p = HERE / name
        if a.check:
            if not p.exists() or p.read_text(encoding="utf-8") != text:
                print("STALE: %s" % name, file=sys.stderr)
                stale = True
        else:
            p.write_text(text, encoding="utf-8")

    print("P11-13: H=%d C=%d I=%d M=%d U=%d not-cipher=%d" % (p11_13_grades["H"], p11_13_grades["C"], p11_13_grades["I"], p11_13_grades["M"], p11_13_grades["U"], p11_13_grades["-"]))
    print("P15:    H=%d C=%d I=%d M=%d U=%d not-cipher=%d" % (p15_grades["H"], p15_grades["C"], p15_grades["I"], p15_grades["M"], p15_grades["U"], p15_grades["-"]))
    print("P9+P10: H=%d C=%d I=%d M=%d U=%d not-cipher=%d" % (blake_grades["H"], blake_grades["C"], blake_grades["I"], blake_grades["M"], blake_grades["U"], blake_grades["-"]))

    print("letter\tH\tM\tU\ttotal")
    for letter_id, h, m, u, total in report:
        print("%s\t%d\t%d\t%d\t%d" % (letter_id, h, m, u, total))

    if a.check and stale:
        sys.exit(1)


if __name__ == "__main__":
    main()
