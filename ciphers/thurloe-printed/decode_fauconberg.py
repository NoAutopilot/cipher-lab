#!/usr/bin/env python3
"""Align Birch's printed interlinear decipherment for the Fauconberg-to-Henry-Cromwell
pool (P16-P24, nine rows of the twenty-three-item Thurloe printed-cipher set) and
build one combined key from it.

LANE T's heading scan (24 Sept 2026, NOTES.md section 10) found that the heading
"Lord Fauconberg to H. Cromwell, lord deputy/lieutenant of Ireland" sits directly
above the windows thurloe-check.tsv/index.tsv had attributed to Capt. Stoakes (P16),
Mr. Downing (P17), Dr. Tho. Harrison (P18), Mr. S. Disbrowe (P20) and Consul Maynard
(P24), joining the four rows (P19, P21, P22, P23) the Monck-pool solver (ROOM.md
03:00 UTC 24 Sept 2026, NOTES.md section 8) had already reattributed. All nine share
one numeral cipher and Birch prints the contemporary decipherment beside the cipher
line (word-by-word or letter-by-letter), so this -- like the P11-13 Montagu letter,
NOTES.md section 9 -- is an alignment of a printed plaintext, not a cryptanalysis.

Uses tools/interlinear_align.py (built for Montagu) unchanged: for each letter it
extracts every (plain line, cipher line) pair over the FULL letter (heading to the
next document's heading -- wider than the narrow detector windows in index.tsv,
which cut some letters off mid-cipher) into fauconberg_<date>_<row>_pairs.tsv, then
aligns pairs by dynamic programming into a per-letter key. This script combines the
nine per-letter keys (by summed vote) into key_fauconberg.tsv and writes
reading_fauconberg_<row>.txt per letter.

Grading (rule 4): H only for the values Tomokiyo (sources/cryptiana/web/thurloe.htm,
section "Henry Cromwell (1658-1859)") states directly -- E=11/13 -- kept at meaning
"e" regardless of what a given letter's OCR-noisy alignment votes for. C where the
combined vote across the nine letters has a clear majority (top meaning holds more
than half of all votes and at least 2 of them). M on conflict (no majority, or a
single occurrence). The single-capital name codes Tomokiyo also gives (A = Henry
Cromwell, O = Lambert, V = Desbrowe, Z = Protector) are not enciphered -- Birch
prints them as literal capitals inside the cipher line -- so they are listed
separately, at H, with an occurrence count from a plain grep, not a vote.

No cryptanalysis and no anneal (per brief); no reading beyond what the print gives.
Rule 7: `python3 decode_fauconberg.py` writes the pairs/key/reading files;
`python3 decode_fauconberg.py --check` recomputes in memory and exits non-zero if
any committed file is stale.
"""
import argparse
import csv
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent.parent / "tools"))
import interlinear_align as ia  # noqa: E402

DJVU = HERE.parent.parent / "sources" / "ia-fulltext" / "collectionofstat07thur_djvu.txt"
DJVU_GZ_HINT = (
    "not found: %s -- restore it first with\n"
    "  zcat sources/ia-fulltext/thurloe-gz/collectionofstat07thur_djvu.txt.gz "
    "> sources/ia-fulltext/collectionofstat07thur_djvu.txt" % DJVU
)

# (row, date label for the filename, first djvu line of the heading, last djvu line
# of the letter -- the line before the next document's own heading). Ranges found by
# direct inspection of the djvu text this pass (24 Sept 2026), not reused from
# index.tsv/thurloe-check.tsv, whose windows are narrower detector windows, not the
# full letter.
LETTERS = [
    ("P16", "1658-04-20", 7179, 7251),
    ("P17", "1658", 32122, 32356),
    ("P18", "1658-09-14", 34074, 34114),
    ("P19", "1658-09-21", 35655, 35800),
    ("P20", "1658-10-12", 39860, 39962),
    ("P21", "1658-10", 41199, 41367),
    ("P22", "1658-10-26", 42243, 42324),
    ("P23", "1658-11-23", 49474, 49660),
    ("P24", "1659-02-25", 56496, 56615),
]

# Tomokiyo, thurloe.htm, "Henry Cromwell (1658-1659)": "a numerical cipher ...
# (E=11/13)". Kept at H regardless of a given letter's own noisier vote (P20/P21/P23
# are OCR-heavy; see NOTES.md section 10).
TOMOKIYO_H = {11: "e", 13: "e"}

# Tomokiyo's single-capital name codes, same section. Not enciphered -- Birch prints
# these capitals literally inside the cipher line -- so counted by a plain regex over
# the pairs files' cipher_raw column, not voted on by the aligner.
NAME_CODES = {
    "A": "Henry Cromwell",
    "O": "Lambert",
    "V": "Desbrowe",
    "Z": "Protector",
}


def pairs_path(row, date):
    return HERE / ("fauconberg_%s_%s_pairs.tsv" % (date, row))


def reading_path(row):
    return HERE / ("reading_fauconberg_%s.txt" % row)


def extract_pairs(lines, first, last):
    """Same rule as interlinear_align.cmd_pairs, taken from already-loaded lines so
    the 1.86 MB djvu file is read once for all nine letters, not nine times."""
    rows = []
    prev = None
    for n in range(first, last + 1):
        s = lines[n - 1].strip() if n - 1 < len(lines) else ""
        if not s:
            continue
        if ia.is_cipher_line(s):
            if prev is not None:
                rows.append((prev[0], prev[1], n, s))
            prev = None
        else:
            prev = (n, s)
    return rows


def render_pairs(rows):
    out = ["plain_line\tplain_raw\tcipher_line\tcipher_raw"]
    for r in rows:
        out.append("\t".join(str(x) for x in r))
    return "\n".join(out) + "\n"


def name_code_counts(cipher_raws):
    """Count literal-capital name-code tokens (rule 10: report only what is found;
    a bare 'A' or 'V' as an ordinary word is excluded by requiring a following
    period, as printed)."""
    counts = Counter()
    for raw in cipher_raws:
        for tok in raw.split():
            core = tok.strip(",;:")
            if re.fullmatch(r"[AOVZ]\.", core):
                counts[core[0]] += 1
    return counts


def compute_all():
    """-> (per_letter, combined_key_rows, name_code_rows, name_code_total)."""
    if not DJVU.exists():
        sys.exit(DJVU_GZ_HINT)
    lines = DJVU.read_text(encoding="utf-8", errors="ignore").split("\n")

    per_letter = {}
    combined_counts = defaultdict(Counter)  # value -> Counter(meaning -> votes)
    combined_shown = {}  # (value, folded) -> Counter(display spelling -> votes)
    name_counts_total = Counter()

    for row, date, first, last in LETTERS:
        pair_rows = extract_pairs(lines, first, last)
        pairs_text = render_pairs(pair_rows)
        pairs = [
            dict(zip(["plain_line", "plain_raw", "cipher_line", "cipher_raw"], r))
            for r in pair_rows
        ]
        prepared, results, counts, shown = ia.run_align(pairs)
        token_rows = ia.token_rows(prepared, results, counts, shown)
        grades = Counter(r[7].split(":")[0] for r in token_rows)
        name_counts = name_code_counts(p["cipher_raw"] for p in pairs)
        name_counts_total.update(name_counts)

        for v, cnt in counts.items():
            combined_counts[v].update(cnt)
        for k, cnt in shown.items():
            combined_shown.setdefault(k, Counter()).update(cnt)

        per_letter[row] = dict(
            date=date,
            first=first,
            last=last,
            pairs_text=pairs_text,
            n_pairs=len(pair_rows),
            token_rows=token_rows,
            grades=grades,
            name_counts=name_counts,
            counts=counts,
            shown=shown,
        )

    key_rows = []
    for v in sorted(combined_counts):
        cnt = combined_counts[v]
        total = sum(cnt.values())
        top, topn = ia.top_of(cnt)
        meaning = ia.display(combined_shown, v, top)
        if v in TOMOKIYO_H:
            key_rows.append([v, TOMOKIYO_H[v], total, "H", "Tomokiyo thurloe.htm, Henry Cromwell (1658-1859), E=11/13"])
        elif topn >= 2 and topn * 2 > total:
            key_rows.append([v, meaning, total, "C", "printed interlinear, %d/%d agreeing places across the pool" % (topn, total)])
        else:
            key_rows.append([v, meaning, total, "M", "printed interlinear, no majority (%d/%d for top reading)" % (topn, total)])

    name_rows = []
    for code in sorted(NAME_CODES):
        n = name_counts_total.get(code, 0)
        name_rows.append([code, NAME_CODES[code], n, "H", "Tomokiyo thurloe.htm, Henry Cromwell (1658-1859); literal capital, not enciphered"])

    return per_letter, key_rows, name_rows


def render_key(key_rows, name_rows):
    out = ["value\tmeaning\tvotes\tgrade\tsource"]
    for r in key_rows:
        out.append("\t".join(str(x) for x in r))
    out.append("# single-capital name codes (not enciphered numerals; occurrence count from a plain regex, not a vote)")
    for r in name_rows:
        out.append("\t".join(str(x) for x in r))
    return "\n".join(out) + "\n"


def render_reading(row, info):
    grades = info["grades"]
    total = sum(grades.values())
    header = [
        "# Reading of Thurloe letter %s (Lord Fauconberg to H. Cromwell, %s) from the" % (row, info["date"]),
        "# decipherment Birch prints beside the cipher (1742), aligned by",
        "# tools/interlinear_align.py; combined-pool values from key_fauconberg.tsv kept at H.",
        "# Regenerate: python3 decode_fauconberg.py",
        "# %d cipher/clear tokens, alignment status: %s" % (total, dict(grades)),
        "# Matched control: none run -- nothing cryptanalytic is claimed (CLAUDE.md rule 3",
        "# applies only to a cryptanalytic negative; this is an alignment of a printed plaintext).",
        "#",
        "# Columns: cipher_line  idx  raw  kind  value  repair  plain_chunk  status",
        "#" + "=" * 74,
    ]
    lines = ["\t".join(str(x) for x in r) for r in info["token_rows"]]
    return "\n".join(header + lines) + "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()

    per_letter, key_rows, name_rows = compute_all()

    stale = False
    outputs = {}
    for row, date, first, last in LETTERS:
        outputs[pairs_path(row, date)] = per_letter[row]["pairs_text"]
        outputs[reading_path(row)] = render_reading(row, per_letter[row])
    outputs[HERE / "key_fauconberg.tsv"] = render_key(key_rows, name_rows)

    for path, rendered in outputs.items():
        if a.check:
            if not path.exists() or path.read_text(encoding="utf-8") != rendered:
                print("STALE: %s" % path.name, file=sys.stderr)
                stale = True
        else:
            path.write_text(rendered, encoding="utf-8")

    report = []
    for row, date, first, last in LETTERS:
        g = per_letter[row]["grades"]
        report.append(
            "%s (%s, lines %d-%d): %d pairs, %d tokens, agrees=%d conflict=%d clear=%d"
            % (row, date, first, last, per_letter[row]["n_pairs"], sum(g.values()),
               g.get("agrees", 0) + g.get("single", 0) + g.get("single-segment", 0),
               g.get("conflict", 0), g.get("clear", 0))
        )
    print("\n".join(report))
    print("combined key: %d values, %d name codes" % (len(key_rows), len(name_rows)))

    if a.check and stale:
        sys.exit(1)


if __name__ == "__main__":
    main()
