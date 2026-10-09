# PREREG-BRANDT-UP (9 Oct 2026, written 02:5x UTC by date -u, before any score below is computed)

Target: Friedrich von Brandt to Hedwig Sophie, HStAM 4 f Staaten D Dänemark 131. Job BRANDT-UP, LANE FAMILY-A2e (account 2).
Material: image 0020 right-page head block (3 numeral lines above "Es ist hier eine troupe", with a left-margin gloss) and image 0021
left-page top (inline groups with interlinear glosses). Two blind Sonnet passes per block were written to disk before this file; the worker
saw the crops by eye while cutting them. Nothing is scored before this file is committed.

## Known-answer test (letters of the period gloss against values_gate.tsv's C values)

Frozen key: `values_gate.tsv` rows with grade C (16 values, single letters), as committed by BRANDT-GATE. No value is added or changed.
Data: `ciphertext_0020u.tsv` (head block) and `ciphertext_0021.tsv` (0021 top), reconciled from the two passes with
tools/reconcile_passes.py, splits settled from the image, gloss text per block (0020u: the margin note, in order; 0021: the gloss over
each group or run). Written before the score script runs.
Normalisation of gloss text: lowercase; ä->ae, ö->oe, ü->ue (make_pairs.py convention); letters a-z only; unread [?] letters dropped.
Per block: cipher string = the block's groups in order, clear words and separators removed; each group with a C value becomes its letter,
every other group a wildcard that matches no letter but may be skipped. Statistic: the longest common subsequence (LCS) between the
C-letter sequence (wildcards removed) and the gloss letter string of that block, summed over the two blocks = matched C tokens.
Control: the same statistic after a uniform random permutation of the letters among the 16 C values (value->letter re-assignment),
n = 2000, seed 20261009. Can the control differ from the target? Yes: re-assigned letters change the C-letter sequence and so its LCS
with the fixed gloss; nothing in the statistic is invariant under the permutation (rule 3).
Gate: PASS if real > control p99 AND empirical p = (1 + #{control >= real}) / 2001 < 0.01. FAIL otherwise.
Power note: the blocks are short (about 40 + 8 groups); if fewer than 10 C-value tokens fall in them the test is reported as
"non-test at this N" whatever its numbers.

## What each outcome licenses
- PASS: glossed tokens whose C value is LCS-matched to the gloss letter (and, on 0021, sits under a gloss containing that letter) grade C.
  Unglossed tokens decoded by a C value: none expected (both blocks glossed); any that occur grade S.
- FAIL or non-test: no change to values_gate.tsv; glossed tokens stay M except where the gloss is read letter-for-letter over the group.
- Word-level codes (e.g. multi-letter glosses over one group) are recorded with their gloss as M (one or two leaves), never C here.
Script: `score_up.py` (committed with this file; it reads only the files named above).
