# TXD-HOLDOUT pre-registration (3 Oct 2026, ~09:33 UTC, account-1 worker for LANE-A1)

Written and pushed before any score below is computed. Brief: `.claude/briefs/runs/2026-10-03-acct1-txd-holdout.md`.
Tool: `tools/key_decode_lattice.py` (tool_shelf grade: weak), unchanged. Lattices: the committed TX-DECODE top-k files
(`../f144r_topk.tsv`, `../f168_topk.tsv`, `../f117_topk.tsv`, `../no87_topk.tsv`), not rebuilt. Languages as TX-DECODE
(f144r, f168, no.87: it16dip; f117: fr). Beam 64. Score = `NgramModel.score` of the decoded text (the tool's own control
statistic). Script: `holdout.py` (this folder), seeds fixed below.

## (a) Wrong-key control at lam 4
The other office keys on disk (`birago-fr3252-1571-72/keys/`: Ceppo f.36 clerk, fr.3995 no.32/71/73/74) are written in
different sign inventories (S-signs, two-figure codes); no mapping from them to the 1572 T-sign ids exists, so they cannot
be applied to a T-sign lattice. What transfers is the design (homophone partition + value set), so the wrong keys are:
- **W1, partition-preserving relabelings (200, seed 11):** the 1572 key's homophone partition kept exactly (signs sharing a
  value still share one); the distinct single-letter values permuted by a random bijection among themselves, the distinct
  word values permuted among themselves; nulls kept. Identity draws are redrawn.
- **W2, value rotations (all non-zero shifts):** single-letter values cyclically shifted by k over the sorted list of the
  key's own distinct letters; word values unchanged.
- **Reference (not a wrong key):** `../../key_1572_clerkvar.tsv`, reported beside, not part of the gate.
**Gate (a), per letter:** the printed key's lattice score must be strictly higher than every W1 and W2 key's. Any wrong
key scoring >= the printed key voids the lam-4 rank-1 result as evidence for that letter. Rank and z vs W1 also reported.

## (b) lam sweep
lam in {1, 2, 3, 4, 6, 8}; per letter rank/z of the printed key among 200 value-shuffled keys (tool's own `control`, seed
1, as TX-DECODE). **Stated in advance:** "robust" = rank 1 at lam 3, 4 and 6 and at >= 4 of the 6 values; "tuned-only" =
rank 1 at lam 4 but at <= 2 of the other 5 values; anything else "mixed". Reported per letter; this is descriptive and
does not by itself decide the verdict.

## (c) Held-out lam tune
Decode the whole no.87 lattice at each lam in {1, 2, 3, 4, 6, 8}; score err_true (wrong / aligned, U counted separately)
against `../truth87.tsv` ONLY on lines f178v_L12-L23, f178r_*, f179r_* (none of f178v_L01-L11, the lines lam 4 was picked
on). Chosen lam = minimum err; ties broken by lower err_with_U, then by the lam nearest 1. If chosen lam != 4, the three
letters are re-run at the chosen lam (200 shuffles, seed 1, plus gate (a) at that lam) and the judge run on each re-run text.

## (d) Judge
On any re-run text: `tools/judge_plaintext.py` with the same corpus as TX-DECODE (it16dip / fr), real_p05 beside the score,
and beside it the score of the same-lam lattice decode of one position-shuffled target (seed 100, as shuffled_target.py).

## Verdict per letter
"lam-4 rank 1 survives held-out control" iff gate (a) passes at lam 4 AND (c) selects lam 4, or (c) selects another lam
at which the letter is still rank 1/201 and gate (a) still passes. Otherwise "does not". No reading committed either way;
no token graded above S.
