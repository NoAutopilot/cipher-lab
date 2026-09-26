#!/usr/bin/env python3
"""Build specs/la-garde-1577.json from the reconciled v2 transcriptions (WC-LAGARDE, 26 Sept 2026).

Pools both letters' cipher passages (WVO 6179 pp.2-3, WVO 6467 p2's two runs) into one ciphertext for
tools/family_run.py, one line per manuscript-line run, each token written code^marks exactly as
ciphers/fr2933-salviati-1525/build_spec.py does it: a bare numeral is "N^", an overlined numeral is "N^ol",
a numeral carrying the loop-crossbar flourish is "N^lp", and a free-standing flourish with no attached digit
(10 in 6179, 1 in 6467 -- WC-LAGARDE's settling pass left these as their own rows, not merged onto a
neighbour, rule 2) becomes its own base code "MARK^", the same choice ciphers/la-garde-1577/solve_l2.py's
--mark-signs mode already makes for these rows.

Only the 239 rows carrying a non-empty `line` field are pooled -- the primary reconciled reading (matches
WC-LAGARDE's own "239 rows total (unchanged)" count in NOTES.md). Excluded: 6 trailing witness-only
insertion rows in ciphertext_6179_v2.tsv (empty `line` field, tokens a minority pass saw that the primary
reconciled sequence did not adopt -- L4's "not counted in the totals" already established this convention).

row_pattern is one S per pooled sign token, tiled as one manuscript-line run of S's followed by a single
plain-box gap ("_"), matching the family_run.py default that params["lengths"] (message lengths) would build
with no explicit pattern at all -- it is written out explicitly only so the run/gap structure is visible in
the spec file, per this target's own worker brief. This is coarser than fr2933-salviati-1525's row_pattern
(which tracks every real plain Italian word-box, since that transcription recorded them): this transcription
recorded only the cipher tokens, not the interleaving plain French words, so there is no finer honest pattern
to write.

  python3 ciphers/la-garde-1577/build_spec.py            writes specs/la-garde-1577.json
  python3 ciphers/la-garde-1577/build_spec.py --check    exits 1 if the committed spec's ciphertext differs
"""
import csv, json, os, sys
from collections import Counter

D = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(D))
OUT = os.path.join(ROOT, "specs", "la-garde-1577.json")
FILES = ("ciphertext_6179_v2.tsv", "ciphertext_6467_v2.tsv")


def to_sign(group):
    if group == "[mark]":
        return "MARK^"
    if group.endswith("~"):
        return group[:-1] + "^lp"
    if group.endswith("^"):
        return group[:-1] + "^ol"
    return group + "^"


def rows():
    for fn in FILES:
        for x in csv.DictReader(open(os.path.join(D, fn), encoding="utf-8"), delimiter="\t"):
            if x["line"]:
                yield fn, x


def build():
    runs, cur, prev = [], [], None
    for fn, x in rows():
        key = (fn, x["line"])
        if key != prev and cur:
            runs.append(cur); cur = []
        prev = key
        cur.append(to_sign(x["group"]))
    if cur:
        runs.append(cur)
    pattern = "".join("S" * len(r) + "_" for r in runs)
    return runs, pattern


def main():
    runs, pattern = build()
    toks = [t for r in runs for t in r]
    codes = Counter(t.split("^")[0] for t in toks)
    marks = Counter(t.split("^")[1] for t in toks)
    spec = {
        "slug": "la-garde-1577",
        "name": "La Garde, superintendent of Schoonhoven, to Willem van Oranje, 28 Nov 1577 (WVO 6179), pooled with "
                "Marnix van St. Aldegonde to Willem van Oranje, 2 Nov 1577 (WVO 6467) -- same dot-separated 1-24 "
                "numeral cipher family, two of its signs carrying an overline or a loop-crossbar flourish mark",
        "language_candidates": ["fr"],
        "ciphertext_source": "resources.huygens.knaw.nl/wvo/app/brief?nr=6179 and nr=6467; reconciled two/three-witness "
                              "transcription (ciphertext_6179_v2.tsv, ciphertext_6467_v2.tsv; NOTES.md sections L1-L4 and "
                              "WC-LAGARDE), all 9 previously-unresolved cells settled by WC-LAGARDE (26 Sept 2026) from "
                              "the images already on disk; measured pass-to-pass disagreement 20.1% (rows carrying a "
                              "witness alt), M-grade rate 21.8% (NOTES 'WC-LAGARDE' counts)",
        "ciphertext_date": "transcription 24-26 Sept 2026 (L1-L4, WC-LAGARDE); spec built 26 Sept 2026 by build_spec.py "
                            "(WC-LAGARDE2)",
        "alphabet": f"{len(codes)} base codes (numerals 1-24 plus '07' and '29', two recurring flourishes not fitting "
                     "that range at this transcription's current reading, and 'MARK' for a free-standing flourish "
                     "with no attached digit) each optionally carrying one mark: 'ol' a plain overline, 'lp' the "
                     f"loop-crossbar flourish; {len(set(toks))} code+mark types over {len(toks)} pooled sign tokens "
                     f"(marks: {marks['']} bare, {marks['ol']} overline, {marks['lp']} loop-crossbar)",
        "ciphertext": [" ".join(r) for r in runs],
        "row_pattern": pattern,
        "constraints": [
            "239 pooled tokens, two letters (WVO 6179 and 6467)",
            "6467 margin note 'Justifier le faict du grand' beside run 1 is an unconfirmed gloss, not a crib -- it "
            "matches the letter's own main-text clause 'justifier le faict de Gand' one word off, per two "
            "independent print editions (NOTES 'Y1: the 6467 margin'); solve_l2.py's crib test (up to 6 nulls, both "
            "spellings) already finds no consistent many-to-one sign-to-letter map",
            "value range capped at 24 with heavy reuse (10 appears roughly once per 10 tokens; 25 distinct base "
            "digit values over 228 numeral tokens in the original L1 count) -- read by L1 as more consistent with "
            "numbers-for-letters than a word nomenclator, before the syllabary/wordcode hypothesis was tried",
            "monoalphabetic/homophonic substitution (both mark-stripped and marks-as-distinct-signs) and periodic "
            "Vigenere/Beaufort (periods 1-14) are both control-backed negatives at every injected-error level from "
            "8% up through the transcription's own measured 20-26% disagreement range (NOTES 'L4', 'WC-LAGARDE'); "
            "not yet tried via tools/family_run.py: syllabary, wordcode (this spec)"
        ],
        "cheap_tests_in_order": [
            "syllabary: base code = numeral (letter), an overline or loop-crossbar mark = the following vowel "
            "(tools/families/syllabary.py) -- the materially different family the sign system's own two marks "
            "suggest, over the already-tried monoalphabetic/homophonic and periodic designs (owner's stuck-rule "
            "try, README common tail 18:53)",
            "wordcode: numeral runs read as a letter-or-word nomenclator inside sign runs (tools/families/wordcode.py) "
            "-- marked numerals as whole-word/name codes rather than syllable vowels"
        ],
        "cheap_test_done": [],
        "judge": {
            "language": "fr",
            "corpora": ["tools/data/fr16/lettresdecatheri01cathuoft_djvu.txt.gz",
                        "tools/data/fr16/lettresdecatheri02cathuoft_djvu.txt.gz"],
            "letters_min": 200,
            "letters_max": 380,
            "control_samples": 60
        },
        "written": "26 Sept 2026, LANE WC worker WC-LAGARDE2 (Sonnet), .claude/briefs/runs/2026-09-26-lane-wc-lagarde2.md"
    }
    if "--check" in sys.argv:
        old = json.load(open(OUT, encoding="utf-8"))
        if old.get("ciphertext") != spec["ciphertext"] or old.get("row_pattern") != spec["row_pattern"]:
            print("STALE: committed spec ciphertext differs from the v2 transcriptions"); return 1
        print(f"ok: {len(toks)} tokens, {len(set(toks))} types, {len(runs)} runs, pattern {len(pattern)} boxes"); return 0
    if os.path.exists(OUT):  # keep cheap_test_done rows already recorded
        old = json.load(open(OUT, encoding="utf-8"))
        spec["cheap_test_done"] = old.get("cheap_test_done", [])
    json.dump(spec, open(OUT, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    print(f"wrote {OUT}: {len(toks)} tokens, {len(set(toks))} types, {len(runs)} runs, pattern {len(pattern)} boxes "
          f"({pattern.count('_')} plain)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
