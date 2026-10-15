# PREREG-PIS-121 (15 Oct 2026, 13:0x UTC by date -u; pushed before any blind pass is read and before any decode)
Job: PIS-121, LANE DEFAULT-A1-1140-15 (account 1), brief .claude/briefs/runs/2026-10-15-acct1-default-1140-jobs.md "PIS-121".
Question: does Tomokiyo's 1585 table (key.tsv, 67 labels) decode the cipher of fr.16045 f.121 (canvas 252) into text that agrees
with the period clerk's left-margin gloss on the same page better than a permuted table does?

## Material
- Image: openapi.bnf.fr IIIF v3 btv1b9060906j f252 full/max (3922x5693, sha1 407648e7e17b46283e3cb9200ad6b0056b5adaad), scratch only.
- Cipher crops: `tools/iiif_lines.py --image <c252_max.jpg> --region 1100,880,2750,3900 --prefix c252 --max-width 1600 --overlap 100`
  (27 lines x 2 segments). Gloss crops: three margin blocks, `--region 400,360,900,960` (glA), `400,2420,900,880` (glB),
  `400,3760,900,1060` (glC), `--distance 70`.
- Passes: two blind Sonnet passes on the cipher crops (value-blind: tx/SIGNSHEET.png + tx/SIGNS.md only, PIS-T's PASS_BRIEF rules);
  one blind Sonnet pass on the gloss crops (clear French, no cipher context, no key, no page text given); one reconciliation call that
  settles the cipher disagreements from the crops and the sign sheet only (no values, no decode, no gloss). The gloss pass is not
  settled or corrected by the worker before scoring (V-BRANDT rule); clear words in the body are not removed from either side.

## Score (fixed now)
- Decode D: each cipher label -> its key.tsv value (word signs -> their word; nulls S54-S56 -> nothing; `b|c` -> a class matching b or c;
  `?`/unknown -> '#', which matches nothing). Lines concatenated in order; letters only.
- Gloss G: per block (A, B, C) the pass's text, lower-case, accents stripped, letters only; fold j->i, v->u, y->i, k->c on both sides.
- S_block = Smith-Waterman local alignment score of G_block against D: match +2, mismatch -1, gap -2. S = S_A + S_B + S_C.
- Primary: S on the reconciled draft. Secondary (reported, not gated): S on pass A and pass B separately; per-block S.

## Control and gate (fixed now)
- Null: the same S with the key.tsv value column permuted across the 67 labels (uniform random permutation, seeds 0-999: 1,000 draws;
  the brief asks >= 200). It can differ from the target by construction (it changes D).
- **PASS** if S_real > the null's 99th percentile (rank >= 991 of 1,000). **FAIL** otherwise.
- Power check (positive control, run before the target score): synthetic page = the three gloss blocks (as read by the gloss pass)
  enciphered with key.tsv (random homophone per letter; letters without a sign, e.g. c -> S04/S05, kept as the b|c signs; k/z/j folded),
  embedded in random-label filler up to the target's reconciled sign count, then each sign replaced by a random label with probability
  e = the target's measured err_2reader from reconcile_passes.py on the two cipher passes. Same S and same permuted null (200 draws per
  seed), 5 seeds. Power PASS if >= 4/5 seeds clear their own p99. If the power check FAILS, a target FAIL is logged NON-TEST (not a
  negative on the table); a target PASS stands as a PASS against the null either way.

## What a result licenses
- No table value changes in this job under any outcome (the score is page-level; no per-sign gate is registered). Every decoded token
  stays grade M. A PASS is logged as "the 1585 table agrees with the f.121 gloss beyond a permuted table (p < 0.01)" in NOTES/HYPOTHESES;
  a FAIL with power PASS as a control-backed miss at this transcription; a FAIL with power FAIL as NON-TEST.
