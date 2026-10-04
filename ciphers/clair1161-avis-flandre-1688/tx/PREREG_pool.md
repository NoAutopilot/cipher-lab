# PREREG_pool -- NEAR3-C1POOL (4 Oct 2026, written 02:12 UTC, pushed before any statistic is computed)

Brief: `.claude/briefs/runs/2026-10-04-ytbiz-near3-wave3.md`, job NEAR3-C1POOL. Script `pool/pool.py`.

## Material
`pool/new_leaves.tsv` (`pool.py build`): c186L 246, c187L 718, c187R 744, c188L 759 = **2467 cipher signs** (as transcribed;
'ss' written as two 's' rows, the c185R/c186R convention; leaf-local `NEW1` renamed `NEW_c186L_1` / `NEW_c187L_1` since the two
reports describe different shapes; every NEW* label kept as its own sign). Pooled stream for (b): ciphertext.tsv's 924 + 2467
= 3391 signs. Only statistic seen so far: none. Timing run (shuffled pooled stream, seed 99, not an arm): 113 s for one anneal at
restarts 32 -> under 2 min, so **restarts stay 32 in every arm**.

No marginal gloss is reported on any of the four new leaves (c186L none; c187L clear words in-line only; c187R the clear date
"Juil 23" and in-line words; c188L one clear word): `tools/interlinear_align.py` stays [retired] for this block.

## (a) held-out test of the CURRENT key.tsv (built on c185R + c186R only)
Decode each new leaf with key.tsv; unkeyed signs (NEW*) -> '?' (dropped by the judge's fold) in every arm alike.
Statistics: fr16 language score of `tools/judge_plaintext.py`'s model (same spec, same corpora) AND its word cover.
Controls: (i) key.tsv on each leaf's ORDER-shuffled signs (shuffled within leaf), 20 seeds; (ii) the 20 shuffled-ciphertext anneal
keys `glossctl/key_shuf1..20.tsv` on the UNshuffled leaves.
**PASS** (pooled, all four leaves) when the real score > max(ii score) and > p95(i score) [p95 = 19th of 20], AND the real cover >
max(ii cover) and > p95(i cover). Reported the same way for the pooled set without c188L (err_2reader 0.181) and per leaf; the
gate uses the all-four figure only. The full judge line on each real decode is pasted beside it.

## (b) pooled re-anneal (gated)
Recipe: `homophonic_anneal.solve(stream, fr16 order-3 model, restarts 32, iters 40000, seed, uni_weight 1.0)`, with the 6 C signs
of READ2-C1161B held fixed (a=u, d=n, e=p, ee=y, p=c, sd=g) and nothing else (the 10 strict-repair moves are free, per C1LOOSE);
q/ls and the S shapes merged (C1SPLIT). Real arm: seeds 1-5 on the 3391-sign pooled stream, keep the best anneal score.
Control: the pooled stream ORDER-shuffled (shuffle seeds 1-5), each annealed with seeds 1 and 2 (same fixed 6), best anneal score
per shuffle; statistic per shuffle = that key's gloss match on the (unshuffled) c186R block.
Statistic: block-vs-gloss match (`glossctl.stat`, 220-sign c186R block vs the 170 gloss letters) of the best real key.
**PASS** when (1) the real gloss match > max over the 5 shuffle bests, AND (2) the judge language score of the pooled key's decode
is at least the current key's. The brief names -1.136; stated exactly, -1.136 is the current key's score on the **924-sign
c185R + c186R** decode (NOTES.md READ2-C1161B), while its **c185R-only** (704) score is -1.128. Both like-for-like comparisons
must hold: pooled key on c185R+c186R >= -1.136 AND on c185R >= -1.128.
Order: real seeds 1-5, then shuffles 1-5 x seeds 1-2 (15 anneals, ~2 min each). Stop before an anneal that would cross 80% of the
box (03:03 UTC; box 02:07-03:17), reporting what ran; an incomplete control arm is a non-test, not a PASS.
If PASS: adopt the pooled key into key.tsv (C for the 6, S for annealed, M handled by decode_key from token conf). If FAIL: keep
key.tsv, regenerate the reading for the merged ciphertext under the old key.
