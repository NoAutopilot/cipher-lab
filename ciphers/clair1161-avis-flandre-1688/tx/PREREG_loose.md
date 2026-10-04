# PREREG_loose -- NEAR3-C1LOOSE (written 4 Oct 2026 01:2x UTC, before any run)

Brief: `.claude/briefs/runs/2026-10-04-ytbiz-near3-wave1.md`, job NEAR3-C1LOOSE. Script: `glossctl/loose.py` (rows append to
`glossctl/loose.tsv`; keys `glossctl/loose_real_key.tsv`, `glossctl/loose_shufN_key.tsv`). Runs serially, one anneal at a time.

**Alignment (unchanged from READ2-C1161B step 2, `glossctl/repair.py` `align`).** Global edit-distance alignment of the
220-sign c186R block (ciphertext.tsv lines c186R_*, '/' dropped) to the 170 gloss letters of `align/pairs_c186R_v0.tsv`;
cost 0 when the key's letter for the sign equals the gloss letter, 1 for a mismatch or a gap. The key used for the cost is
the **unrepaired READ2-C1161 key** (the key the strict run aligned with), reconstructed from today's key.tsv by restoring
the "was 'x'" value of the 10 re-annealed signs; check: it must give block-vs-gloss 0.594, or the run stops.

**Loose rule.** A sign is fixed (grade C for the real gloss) to its majority aligned gloss letter when it has **>= 3 aligned
occurrences** and the majority letter holds **>= 60%** of them (count(majority) / count(aligned) >= 0.60). No single-
occurrence clause. Signs below the rule stay free.

**Re-anneal (unchanged).** Full 924-sign spec stream (tokens space), `homophonic_anneal.solve`, fr16 order-3 model from the
spec's judge corpora, seed 1, restarts 32, iters 40000, uni_weight 1.0, fixed signs held. Decode c185R (first 704 signs) and
score with `tools/judge_plaintext.py specs/clair1161-avis-flandre-1688.json --file <c185R decode> --json`.

**Control.** The identical procedure (same alignment, same key for the cost, same rule, same anneal) with the gloss letters
shuffled within the gloss, `random.Random(S).shuffle`, **S = 1..10** (seeds 1-3 are the same shuffles READ2-C1161B used).

**Pre-registered outcome.** PASS when the real-gloss loose repair's c185R judge language score is **greater than the
maximum of the 10 shuffled-gloss loose repairs' c185R scores AND greater than -1.128** (the strict-rule real repair).
Otherwise FAIL. Block-vs-real-gloss match is reported for every run but is not the gate (fit to the gloss by construction).
No change to rule, alignment, recipe, seeds or threshold after the first run. key.tsv and the reading are not replaced in
this job whatever the outcome.
