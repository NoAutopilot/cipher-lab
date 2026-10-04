# PREREG: q/ls and S split test (NEAR3-C1SPLIT, 4 Oct 2026; written and pushed before any run)

Target clair1161-avis-flandre-1688, stream = ciphertext.tsv minus '/' and [PLAIN:...] (924 signs; asserted equal to the spec stream).
Neither ciphertext.tsv nor key.tsv is edited. Script `split/split.py`; occurrence assignment `split/assign.tsv`.

## Variants
- **merged**: the stream as transcribed (baseline).
- **qls**: the 9 c185R occurrences reconciled as `q` where pass B read `ls` (tx/c185R_rec/disagreements.tsv: 7 q|ls,
  1 S|ls, 1 p|ls) -> new symbol `qL`. Pass B is the pass that separates them. The other 20 q stay `q`.
- **S**: the 14 `S` of the c186R block, assigned by eye from the line crops (one contact-sheet look): 7 open 5-like ->
  new symbol `S5`, 7 looped g-like stay `S` (one of these, L07 2nd, is M). The 53 c185R `S` stay `S`: a second look
  (a snippet grid at estimated positions) showed both shapes on c185R too, but the estimated positions were not reliable
  enough to assign each occurrence; so this tests the split on the block only.
- **placebo-qls K=1..5**: sign w, o, e, 9, p (c185R counts 19, 19, 16, 16, 25; q has 18 in c185R): 9 random c185R occurrences
  (random.Random(K).sample) -> a new symbol. Same leaf, same number moved as the real split.
- **placebo-S K=1..5**: sign +, 7, 4, th, qb (block counts 18, 14, 12, 12, 14; S has 14 in the block): 7 random block
  occurrences -> a new symbol. Same leaf, same number moved.
The placebo is a control that can differ: adding one symbol gives the anneal one more free letter and can raise fit by
itself; a placebo split has that freedom without the shape evidence.

## Recipe (every run, serially)
homophonic_anneal.solve(stream, fr16 order-3 model from the spec's three judge corpora, restarts 32, iters 40000, seed 1,
uni_weight 1.0), blind (no fixed signs; READ2-C1161B's 6 held signs are not held here, so the merged baseline is rerun
under this exact recipe rather than taken from key.tsv).

## Statistics
1. gloss match: glossctl.stat (difflib matching blocks / 170 gloss letters) of the c186R block decode vs align/pairs_c186R_v0.tsv gloss.
2. c185R judge: tools/judge_plaintext.py language score on the 704-sign c185R decode (higher is better).

## Gate (per pair)
Placebo p80 over 5 values = the 4th smallest of the 5 (sorted ascending, index 3).
**PASS for a split** when BOTH: gloss match(split) > gloss match(merged) AND > placebo p80 gloss match; AND
c185R judge(split) > c185R judge(merged) AND > placebo p80 c185R judge. Anything else: FAIL -> recommend merged for the
pooled job. A tie counts as not beating. No reruns with other seeds or restarts in this job.
Caveat stated in advance: for qls all 9 moved occurrences are on c185R, so the gloss match can move only through key
interaction; for S all 7 are on the block, so the c185R judge can move only through key interaction.
