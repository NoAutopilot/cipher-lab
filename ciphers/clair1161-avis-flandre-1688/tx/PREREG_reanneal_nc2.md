# PREREG-C1161RA addendum NC2: the same joint re-anneal, objective normalised by sum N_c^2

SCORE-NC2 (account-3 worker), 4 Oct 2026, written and pushed before any nc2 anneal or score.
Brief: `.claude/briefs/runs/2026-10-04-acct3-score-nc2.md`. Source: Lasry, Biermann and Tomokiyo 2023 (Cryptologia 47:2),
App. A p. 195, S = sum_g N_g log F_g / sum_c N_c^2; research/MARY-STUART-METHOD-2026-10-04.md row 16.

**Everything in tx/PREREG_reanneal.md stands unchanged** -- stream, held signs (6 C + 13 agreed S), the 29 free signs,
stage 1 (fr17 4-grams, uni_w 1.0, 32 restarts, 40000 iters), stage 2 coordinate ascent on J, W by the same held-out
formula, seeds 1-10, consensus >= 7/10, planted control a/p/d at e, recovery rule (consensus true AND dJ > shuffled-value
null p95), gate >= 2 of 3, per-sign decision rules -- **with one change:** `--norm nc2`. Every n-gram term (stage 1's
anneal score and stage 2's L4 inside J, and so the W calibration, which re-runs by the same formula) is computed by the
shared `tools/homophonic_anneal.ngram_term(norm="nc2")`: (sum of 4-gram log-probs shifted by the model's floor so each
term is >= 0) x n^2 q0 / sum_c N_c^2. Outputs in `two/ra_nc2/`; `two/ra/` (the C1161RA run) is not touched.

**Why this is a new instrument, not a fourth turn of the same knob (rule 3 third-attempt clause).** C1161RA changed
nothing about the objective; its failure was the objective's own optimum: the word-cover stage "drove all free signs to
i", a degenerate key that the per-character log-likelihood + cover score does not penalise. nc2 changes the objective
itself, in the one direction that failure names -- a key piling signs on one letter raises sum N_c^2 and loses score in
proportion -- so the test can fail differently from C1161RA (the planted signs' consensus and dJ both change), and it
is the instrument the Mary Stuart solvers used on 150,000 symbols. One attempt; if it fails it is logged and not tuned.

**Headroom (rule 3).** The control's blind baseline on file is C1161RA's own run of this exact planted control at
norm=none: **0/3 recovered** (two/ra/ctl_gate.txt; consensus i or none on a/p/d) -- far from ceiling, so a pass here
would be a gain of the objective, not of restarts.

**Gate.** Planted control >= 2 of 3 recovered under nc2, else NON-TEST: stop, log it, target not run, no tuning of W,
seeds or recipe. **Target arm** (10 seeds) only on GATE PASS; report per free sign the consensus value and seed
agreement (two/ra_nc2/tgt_signs.tsv). **No `--apply`:** nothing enters key.tsv in this job; any sign that clears is a
proposal graded M, written to NOTES.md/HYPOTHESES.md with a ROOM line.
