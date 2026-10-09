# PREREG-BRANDT-GATE (9 Oct 2026, written 02:2x UTC by date -u, before any score below is computed and before 0049 is fetched)

Target: Friedrich von Brandt to Hedwig Sophie, HStAM 4 f Staaten D Dänemark 131. Job BRANDT-GATE, LANE FAMILY-A2e (account 2).
PREREG-BRANDT-TX's CONSISTENT gate FAILed and is NOT re-run here (rule 3, third-attempt clause). Two different tests are registered.

## Test 1: token agrees count on 0020 (registered form of BRANDT-TX's exploratory statistic)

Inputs frozen: `pairs_0020.tsv` (10 pairs, 220 groups, unchanged since BRANDT-TX commit), tools/interlinear_align.py at origin/main.
Statistic: exactly as `explore_agrees.py` computes it -- `ia.run_align(pairs, floor=150, clear_consumes=True, prior=None,
code_prefix=None, null_cost=-3.0, wildcard=None, max_chunk=8, seg_bonus=1.0, len_prior=0.0)`, then the number of `ia.token_rows`
rows whose last field is 'agrees' (a token whose aligned chunk equals its value's top meaning, value seen >= 2 times).
Control: the same run with the gloss spans (`plain_raw`) dealt to the wrong segments by a uniform random derangement of the 10
pairs; n = 2000 derangements, fresh seed 20261009 (BRANDT-TX used 1672 with n 200; that run is not reused).
Can the control differ from the target? Yes: a gloss span over the wrong cipher run gives chunks that disagree across a value's
occurrences, lowering agrees; nothing in the statistic is invariant under re-dealing the spans.
Gate: PASS if real agrees > the maximum of the 2000 control draws AND empirical p = (1 + #{control >= real}) / 2001 < 0.01.
FAIL otherwise. Script: `gate_agrees.py` (written after this file is pushed; identical computation, only seed and n differ).

## Test 2: 0049 held-out letter test (0049 has not been transcribed by this project; it is read only after this file is pushed)

Key: from `key_0020.tsv` (BRANDT-TX primary run, built with no prior and with 0049 held out), the `meaning` (top chunk) of every
value whose meaning is a single letter: 58 values (167/170/262, word meanings, excluded). M-grade table, frozen as committed.
0049 data: the inserted slip's groups (and the left-page foot, if glossed) with the one letter written over each group, two blind
Sonnet passes on iiif_lines crops, reconciled with tools/reconcile_passes.py, splits settled from the image, written to
`ciphertext_0049.tsv` BEFORE the score script reads key_0020. Normalisation of gloss letters: lowercase, umlauts folded
(ä->a, ö->o, ü->u), j->i, v->u, y->i; the key's letters get the same folding. A group scores only if its gloss is one letter
after folding and its value is among the 58 keyed values (the "scorable" set).
Statistic: number of scorable groups whose key_0020 letter equals the gloss letter (token count).
Control: the 58 value->letter assignments of key_0020 permuted uniformly at random (letter multiset kept), n = 2000, seed
20261009; same scorable set. Can it differ? Yes: permuting assignments changes which letter each 0049 group is predicted to
carry; only the letter frequencies are held fixed, which is the chance baseline the test must beat.
Gate: PASS if real > the 99th percentile of the 2000 control draws (strictly greater). FAIL otherwise.
Not-a-test if fewer than 10 scorable groups.
Sensitivity (reported, does not change the gate): the same score with the 8 slip groups that HDK-131 already wrote into NOTES.md at
00:17 UTC (42 73 144 35 94 67 56 120 = c h w a n g e r, read by eye from a crop) excluded, since they were in the repository before
key_0020 was built (key_0020 was built automatically with no prior, so no leakage is expected; this checks it).

## What PASS/FAIL license
- Test 1 PASS: the period marginal gloss on 0020 is a letter-level decipherment of these groups (the alignment is not reading
  noise). Alone it does not grade tokens C.
- Test 2 PASS: key_0020's single-letter values that 0049's gloss confirms are grade C (known plaintext from the period gloss,
  two letters); values that agree on 0020 but are absent or disagree on 0049 stay M.
- C grades only if BOTH pass (test 1 licenses the 0020 alignment, test 2 confirms the values out of sample). Either FAIL: every
  token stays M; a FAIL is logged in HYPOTHESES.md with both numbers, and is not a design negative (the alignment tool, not the
  cipher, is what is tested).
