#!/usr/bin/env python3
"""GOLD-D1 (25 Sept 2026): base + mark recount for the 160-id GOLD-4C inventory (glyphs/inventory.tsv,
ciphertext_draft.tsv). Composite ids -- a base sign with a stroke, dash or dot stacked above or below it,
named by their parts (O-TILDE, OX-TILDE, O-DASH2, II-DASH, CC-DASH, ARCH-DASH, C-BAR-X, II-O, ...) -- fold to
(base, mark class); every other id folds to (itself, "none"): the fifteen "pure cluster" shapes GOLD-4C kept
as-is (X, PCT, Y-CURL, VENUS, CROSS-T, BAR-SOLID, BAR-THIN, CIRC-O, NOTE, AMP, TRIDENT, VEE, DASH-H, DASH-V,
V-DOT), the twenty PICT-* pictograms, the -LETTER/digit forms, and the GOLD-4A resplit ligatures NOTES.md
describes as one merged shape rather than a base carrying a separate stacked mark (O-SLASH, DAGGER-O,
DBL-SLASH, CHEVRON2, HOOK-L, LOOP-STEM, GEAR-DOT, CRESCENT, DELTA, WAVE-V) and every other -SLASH/-LOOP/-CURL
ligature id. PCT-SLASH folds to base PCT per inventory.tsv's own family column (a font-variant of one shape,
not a stacked mark); BAR-THIN and BAR-SOLID keep their own, separate bases (not folded into BLOB) per the brief.

This is a MECHANICAL, name-based table built from GOLD-4C's own composite naming -- box_labels.tsv and
inventory.tsv were not re-read from the page images for this job (GOLD-D1 does no image work, no decoding).
A handful of calls at the margin (three-hyphen-part names, single-occurrence tails, and whether an "-O" or
"-DOT" suffix is a stacked mark or part of a ligature already merged upstream) are this session's own reasoned
judgement calls, not a re-derivation from the crops; the composite set this table settles on -- 46 ids covering
233 boxes -- differs from GOLD-4C's own descriptive count ("36 composite ids ... cover 267 boxes", HYPOTHESES.md)
for exactly that reason, most of it the ligature ids (O-SLASH 27, DAGGER-O 18) that end in a mark-like suffix
but that NOTES.md's GOLD-4C section describes in prose as a single merged shape.

Run from ciphers/debosnys-1883:  python3 scripts/base_mark_recount.py [--check]
Writes glyphs/base_mark.tsv (sign, base, mark, count) and ciphertext_draft_base.tsv (ciphertext_draft.tsv's rows
with a base/mark split, sign replaced by base). --check regenerates both to memory and exits non-zero if either
committed file is stale (rule 7).
"""
import csv, sys, os, io, argparse
from collections import Counter

NOISE = ("_", "MULTI")

# Composite ids: base sign + stacked mark, named by their parts (GOLD-4C, 25 Sept 2026, NOTES.md/HYPOTHESES.md).
# Every id not listed here (or in BASE_OVERRIDE) maps to (itself, "none") by base_mark()'s fallback.
COMPOSITE = {
    # tilde (a stroke waved over the base)
    "O-TILDE": ("O", "TILDE"), "OX-TILDE": ("OX", "TILDE"), "XX-TILDE": ("XX", "TILDE"),
    "OO-TILDE": ("OO", "TILDE"), "IOI-TILDE": ("IOI", "TILDE"), "DOTS-TILDE": ("DOTS", "TILDE"),
    "II-TILDE": ("II", "TILDE"),
    # dash / dash2 (double dash) / dashbelow / dash-dots
    "CC-DASH": ("CC", "DASH"), "II-DASH": ("II", "DASH"), "ARCH-DASH": ("ARCH", "DASH"),
    "X-DASH": ("X", "DASH"), "U-DASH": ("U", "DASH"), "A-DASH": ("A", "DASH"),
    "NINE-DASH": ("NINE", "DASH"), "QQ-DASH": ("QQ", "DASH"), "LAMBDA-DASH": ("LAMBDA", "DASH"),
    "OO-DASH": ("OO", "DASH"), "TILDE-DASH": ("TILDE", "DASH"), "DOTS-DASH": ("DOTS", "DASH"),
    "O-DASH2": ("O", "DASH2"), "O-DASHBELOW": ("O", "DASHBELOW"), "O-DASH-DOTS": ("O", "DASH-DOTS"),
    # bar / bar-x / bar-cc / bar-o (a horizontal stroke, plain or itself carrying a small shape)
    "C-BAR-X": ("C", "BAR-X"), "X-BAR-CC": ("X", "BAR-CC"), "O-BAR-CC": ("O", "BAR-CC"),
    "O-BAR-O": ("O", "BAR-O"), "X-BAR": ("X", "BAR"), "E-BAR": ("E", "BAR"), "THETA-BAR": ("THETA", "BAR"),
    "NINE-BAR": ("NINE", "BAR"),
    # o (a small loop/o stacked on the base -- distinct from O as a base in the tilde/dash/bar rows above)
    "II-O": ("II", "O"), "CC-O": ("CC", "O"), "QQ-O": ("QQ", "O"), "ARCH-O": ("ARCH", "O"),
    "X-O": ("X", "O"), "OMEGA-O": ("OMEGA", "O"), "O-II": ("O", "II"),
    # dot / dots / dot-stem
    "C-DOT": ("C", "DOT"), "CC-DOT": ("CC", "DOT"), "X-DOT": ("X", "DOT"), "O-DOT-STEM": ("O", "DOT-STEM"),
    "ARCH-DOTS": ("ARCH", "DOTS"), "O-DOTS": ("O", "DOTS"), "J-DOTS": ("J", "DOTS"),
    # bracket / plus
    "O-BRACKET": ("O", "BRACKET"), "O-PLUS": ("O", "PLUS"),
}

# PCT-SLASH folds to base PCT per inventory.tsv's own family column (a font-variant of one shape, not a mark).
BASE_OVERRIDE = {"PCT-SLASH": ("PCT", "none")}


def base_mark(sign):
    if sign in COMPOSITE:
        return COMPOSITE[sign]
    if sign in BASE_OVERRIDE:
        return BASE_OVERRIDE[sign]
    return (sign, "none")


def ic(seq):
    n = len(seq)
    if n < 2:
        return 0.0
    c = Counter(seq)
    return sum(v * (v - 1) for v in c.values()) / (n * (n - 1))


def read_draft(path="ciphertext_draft.tsv"):
    return list(csv.DictReader(open(path, encoding="utf-8"), delimiter="\t"))


def build_base_mark_tsv(rows):
    counts = Counter(r["sign"] for r in rows if r["sign"] not in NOISE)
    out = io.StringIO()
    out.write("sign\tbase\tmark\tcount\n")
    for sign, cnt in sorted(counts.items(), key=lambda kv: (-kv[1], kv[0])):
        base, mark = base_mark(sign)
        out.write(f"{sign}\t{base}\t{mark}\t{cnt}\n")
    return out.getvalue()


def build_draft_base_tsv(rows):
    out = io.StringIO()
    out.write("line\tposition\tsign\tfamily\tconfidence\tnote\tmark\n")
    for r in rows:
        sign = r["sign"]
        base, mark = (sign, "none") if sign in NOISE else base_mark(sign)
        out.write(f"{r['line']}\t{r['position']}\t{base}\t{r['family']}\t{r['confidence']}\t{r['note']}\t{mark}\n")
    return out.getvalue()


def cryptogram_of(line):
    return line.split("_L")[0]


def report(rows):
    signed = [r for r in rows if r["sign"] not in NOISE]
    marks = [base_mark(r["sign"])[1] for r in signed]
    bases_all = [base_mark(r["sign"])[0] for r in signed]
    mark_counts = Counter(marks)
    n_mark_classes = len([m for m in mark_counts if m != "none"])
    lines = [
        f"K_base = {len(set(bases_all))} (from K=160 sign ids, N={len(signed)}); "
        f"mark classes = {n_mark_classes} (plus 'none' for unmarked/standalone signs)",
        "mark class counts: " + ", ".join(f"{m}={c}" for m, c in sorted(mark_counts.items(), key=lambda kv: -kv[1])),
        "",
        f"{'group':<24}{'N':>6}{'K_base':>8}{'IC_base':>10}{'K_160':>8}{'IC_160':>10}",
    ]
    groups = {"c1": ["c1"], "c2 (2a+2b)": ["c2a", "c2b"], "c3": ["c3"], "c4 (4a+4b)": ["c4a", "c4b"],
              "combined": ["c1", "c2a", "c2b", "c3", "c4a", "c4b"]}
    for gname, pages in groups.items():
        gr = [r for r in signed if cryptogram_of(r["line"]) in pages]
        seq160 = [r["sign"] for r in gr]
        seqbase = [base_mark(r["sign"])[0] for r in gr]
        n = len(seq160)
        lines.append(f"{gname:<24}{n:>6}{len(set(seqbase)):>8}{ic(seqbase):>10.4f}{len(set(seq160)):>8}{ic(seq160):>10.4f}")
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    rows = read_draft()
    files = {
        "glyphs/base_mark.tsv": build_base_mark_tsv(rows),
        "ciphertext_draft_base.tsv": build_draft_base_tsv(rows),
    }
    stale = [p for p, t in files.items() if not os.path.exists(p) or open(p, encoding="utf-8").read() != t]
    if a.check:
        print("stale: " + ", ".join(stale) if stale else "ok: committed base_mark files match ciphertext_draft.tsv")
        sys.exit(1 if stale else 0)
    for p, t in files.items():
        open(p, "w", encoding="utf-8").write(t)
    print(report(rows))


if __name__ == "__main__":
    main()
