# PREREG-DEC4450-INIT (account 4, LANE DEFAULT-A4-2135, 13 Oct 2026, written 22:4x UTC by date -u, before any f.4 initial is scored)

Question: is fr.2988 f.4r-6r (Nicolas Raince's clear French, "De Romme le xv^e iour de decembre 1526") the plain text
of fr.2988 f.2r-v (Hieronimo Ranzo's initial-letter + number code, Bourdeau `ranzo_c006/007`, 824 groups)?
Prior: expected negative (FT4, 3 Oct 2026: Raince's French-side voice; Ranzo's code encodes Italian; and Tomokiyo's
`francis.htm` places Raince's own Dec 1526 cipher letters in fr.2984 under a different, reconstructed cipher).

## Step 0 (done before this file, disk + 5 openapi.bnf.fr overviews at 600 px)
- f.2r-v groups: 824 (Bourdeau views 6-7, header lines excluded; 2 of them `?`).
- f.4r-6r words, estimated: about 106 text lines (line cutter on the 600 px overviews: 24 / 24 / ~23 / 24 / 11 by eye
  and `tools/iiif_lines.py`), x about 12 words per line (12 lines of f.4r and 12 of f.5r counted at 2x zoom: 12.4 and
  11.7) = about 1,270 words (range 1,110-1,430).
- Ratio 824 / 1,270 = 0.65 (range 0.58-0.74): inside the brief's 0.6-1.6 band at the point estimate, so step 0 does
  not rule out a 1-group-per-word pairing and the test runs.

## Data to be produced (after this file is pushed)
- `f2f4/initials.tsv`: the word initials of two segments of f.4-6, read from line crops (higher-resolution regions
  fetched from openapi.bnf.fr), two blind Sonnet passes, one reconciliation:
  - `open`: the first 5 text lines of f.4r (from "Vous verres monsigneur ...").
  - `close`: the last 5 text lines of f.6r ending with the word before the dateline "De Romme ..." (dateline excluded:
    datelines often stay outside the cipher).
  Abbreviations count as one word (e.g. "Sa S^te" two words, "lesd" one); an initial is the first letter as written,
  u/v and i/j folded (v->u, j->i) on both sides.
- `f2f4/measured_error.json`: `initial_error` = share of aligned word positions where pass A and pass B give a
  different initial (word-count mismatches count as errors), floor 0.05.

## Statistic, null, control, gate (code: `f2f4/score_f2f4.py`, committed with this file)
- S = SW(open, first 150 f.2 group letters) + SW(close, last 150 f.2 group letters); Smith-Waterman local alignment
  of letter strings, lower-cased, u/v and i/j folded, match +2, mismatch -1, gap -2. The f.2 letter of a group is its
  leading Latin letter (Bourdeau's L and Q read as l and q).
- Null (shuffled pairing): the f.2 letter sequence permuted 2,000 times (composition kept), same S;
  p = (1 + #null >= S) / 2,001. This null can differ from the target: S depends on order, the permutation destroys it.
- Positive control: 100 synthetic f.2-length streams = the same open/close initials with substitution at the measured
  `initial_error` and 10% word insertion/deletion, placed at the start and end of a French initial stream drawn from
  `tools/data/fr16`; power = share of replicates reaching p < 0.01 (200 nulls each).
- Gate: control power >= 0.90 required, else "CONTROL BELOW GATE (non-test)". With the control passed: PASS if
  p < 0.01, FAIL otherwise.
- Scope of a FAIL: it excludes f.4-6 being a *word-for-word* French plain text of f.2 under a literal initial-letter
  code; it does not test a translation (Italian code, French double), a paraphrase, or a code whose letter is not the
  plain word's initial. Reported as a matched-control negative for that hypothesis only.
- Seed 4450. Diagnostic only (not gating): best SW of each segment against all of f.2.
