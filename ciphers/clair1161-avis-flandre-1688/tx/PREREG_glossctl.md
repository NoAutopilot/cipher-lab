# PREREG_glossctl -- READ2-C1161B (written 3 Oct 2026 23:59 UTC, before any control run)

Brief: `.claude/briefs/runs/2026-10-03-acct2-read2-c1161b.md`. Script: `glossctl/glossctl.py` (results append to
`glossctl/results.tsv`).

**Statistic.** In-order gloss letter match, as READ2-C1161: decode the c186R block (ciphertext.tsv lines c186R_*, '/'
dropped, 220 signs) with a key; gloss = letters a-z of `align/pairs_c186R_v0.tsv` row `gloss` ('?' dropped, 170
letters); value = sum of `difflib.SequenceMatcher(None, decode, gloss, autojunk=False)` matching-block sizes / 170.
READ2-C1161's script was not committed; it reported 0.593 over "172 gloss letters". Re-implemented here, the real
key.tsv gives **0.594** (101/170). The target value for this test is 0.594, fixed now.

**Control (a), LM-fluent output.** The same anneal recipe that made key.tsv (family_run.py homophonic, anneal seed 1,
restarts 32, noise=0.10, profile=target, the spec's three fr16 judge corpora, tokens space, N=924 K=49), run on the
token-ORDER-shuffled full ciphertext (family_run's own --shuffle-target shuffle; shuffle seeds 1, 2, 3, ... serially,
at least 5, as many as fit before 00:30 UTC 4 Oct); each resulting key applied to the UNshuffled block and scored
against the gloss. The shuffled stream has the same sign frequencies, so its anneal key is a French-fluent key with
no information about sign order.

**Control (b), generic French overlap.** The real key's block decode scored against 200 windows of 170 letters drawn
at random (seed 1) from the concatenated letters of the same three fr16 corpus files; report p95, mean, max.

**Pass** = 0.594 > max over (a) AND 0.594 > p95 of (b). Both required. No change to statistic, recipe, threshold or
seeds after the first control run.

**Step 2 (only if Pass).** Gloss-seeded key repair, as the brief: align block decode to gloss; a sign is fixed (grade C)
when its aligned gloss letter is the same in every aligned occurrence and it has >= 2 aligned occurrences (one
occurrence also allowed when the sign occurs only in the block); re-anneal the free signs with the fixed ones held;
score the c185R decode (fr16 judge language score and word cover) against the same repair seeded from the gloss with
its letters shuffled within the gloss (3 shuffles). The repair is reported better only if its c185R judge score beats
every shuffled-gloss repair.
