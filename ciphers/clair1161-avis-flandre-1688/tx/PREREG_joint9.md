# PREREG-C1161-JOINT9: joint test of the nine C1161-LOLO proposals as ONE hypothesis (4 Oct 2026, account-3 worker)

Written and pushed before any score is computed by this job. Disk only. Brief `.claude/briefs/runs/2026-10-04-acct3-c1161-joint9.md`.
Script `two/joint9.py` (committed with this file, run only after the push). Output `two/joint9.tsv`.

Hypothesis: key.tsv with all nine values replaced at once (K s, iib d, l f, ls m, o m, rot h, spiralG n, to s, x f).
Instrument unchanged from C1161-GLOSS9 / RUN4-C1161GJ: G = glossctl statistic (c186R 220-sign block decode vs the 170
period-gloss letters), J = fr16 judge `NgramModel.score` on the full 3375-letter decode (relative only).
- real dG = G(key.tsv + nine) - G(key.tsv); real dJ = J(key.tsv + nine) - J(key.tsv).

Null: 50 random joint keys, seeds 1..50 (`random.Random(seed)`): key.tsv with the same nine signs each given a value drawn
independently from the folder's value-frequency distribution = the number of key.tsv rows carrying each plaintext value
(49 signs: e 8, s 5, i 5, r 4, n 4, l 3, u/t/q/h/c/a 2, y/x/p/o/m/g/f/d 1). Scored identically (dG_i, dJ_i vs key.tsv).
PASS iff real dG > null p95(dG) AND real dJ > null p95(dJ) AND real dG > 0 (p95 = 48th of 50 sorted ascending). Else FAIL.
One test; no re-tuning, re-seeding or re-definition after scores.

Rule-3 check (can the control differ?): the null reassigns the same nine signs, so every token of those signs in the
c186R block (14 tokens) and in the full decode changes letter under each null key; both G and J are functions of exactly
those letters, so the null distribution can sit above, at or below the real value on both statistics. Not orthogonal.

Disclosed before scoring: (1) C1161-GLOSS9 already reported, as information, the real joint values (G 0.612 -> 0.647,
dJ +0.0053), so the real side is not blind; only the null is new. (2) A random-value null is weaker than GLOSS9's
shuffled-anneal-key null: any value set chosen by an anneal on this text is expected to beat random letters on the judge.
A PASS therefore says the nine fit better than random values for those signs, not that each value is right; the
grade S it would license is per the brief. (3) spiralG has 0 glossed tokens, so the gloss half carries no evidence for it.
