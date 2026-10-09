# PREREG-MANT0181 (MANT-0181, 9 Oct 2026, LANE FAMILY-A2l account 2; pushed in its own commit BEFORE any decode or score on 0181/0182)

Leaf: HStA Dresden 10026 Loc. 694/08, files 0181 (film label 0182; right page, stamp 138, "A Mr le B. de Manteuffel a Dresden le 6 juillet
1712" -- Flemming's letter TO Manteuffel, the reverse direction of the reports key.tsv was built from) and 0182 (film label 0183; left page, the
letter's continuation and end, "il ne faut pas tarder"). Fetched once each (frames.tsv URLs, HTTP 200). Two blind Sonnet passes (A crop order,
B reversed) are running/read as transcription only; no decode under key.tsv and no gate number has been computed when this file is pushed.
Key: key.tsv at origin/main as of this commit, unchanged by this job.

Stream: one letter = the 0181 runs then the 0182 runs, reading order. Gate (a): n/a (no interlinear letters over any code group at sheet or crop
scale; if a pass reports one, it is listed, not scored -- N < 5).
Gate (b) (design = PREREG-MANT-0177 unchanged except the seed and the added control (ii)): fr18 4-gram (tools/judge_plaintext.py LANG_CORPORA
fr18); name-abbreviation rule as PREREG-MANT-0177; block rule L <= 52 scored whole, else consecutive 52-letter blocks, tail reported only;
power at the scored length from the same positive-control streams (694/09 0085 r9+r10; 0136 unglossed), 200 permuted (seed 7) per window, pass
if real > 190th of 200; a TEST only if power >= 0.80, else "too-short" (no S grade).
 (i) key-permuted control: letter values permuted among key.tsv's letter-valued codes, 1000 permuted keys, seed 181 (+k per block); p95.
 (ii) SHUFFLED-TARGET control (CLAUDE.md rule 3, ARM-C1): the scored tokens' order permuted (100 orders, seed 1810+k), each decoded under the
      REAL key and scored on the same letters. Two outcomes are read from it:
      - VOID test: if more than 5 of the 100 shuffled-target decodes score above the (i) p95, the judge is VOID as a gate for this design at this
        N ("judge cannot decide"): no S grade from (b), grades by key alone (H where key.tsv is H, else M).
      - Order test: block PASS requires real > (i) p95 AND real > the shuffled-target 95th of 100 (i.e. > 95 of the 100 shuffled orders).
 Block verdict PASS / FAIL as above; leaf PASS (every block), MIXED (some), FAIL (none), VOID (VOID test), too-short (power).
Grades (rule 4): H only where key.tsv's row grade is H; S only for an unglossed letter token high/medium conf in a PASS block of a TEST that is not
VOID; name/word codes (value of 4+ letters) M; name-abbreviation M; low conf M; not in key U. Script f0181_08/grade_0181.py.
Decode: tools/decode_key.py f0181_08 --check. Phrases from the decode go to tools/print_check.py (G3) before any "not located" sentence.
Fixed before any score; any deviation is disclosed in NOTES.md as a deviation.
