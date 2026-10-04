# PREREG: multi-seed consensus instrument 2 for the 28 M key signs (RUN3-C1161MS, 4 Oct 2026)

Written about 09:15 UTC 4 Oct 2026 by RUN3-C1161MS (account 1 worker, LANE-RUN3), pushed before any new anneal runs.
Script: `two/consensus.py` (written after this file). Stream, corpus and anneal recipe are those of `tx/PREREG_two_instr.md`
(N4-C1): the four non-training leaves c186L, c187L, c187R, c188L as merged (N 2465, K 54), `homophonic_anneal.solve`, fr16 order 3,
restarts 32, iters 40000, uni_w 1.0, nothing held. Instrument 1 = `key.tsv` at this commit (values unchanged since N4-C1).

## Instrument
- **Consensus instrument 2 (real)** = anneals with seeds 1..10 on the real four-leaf stream. For each sign, the majority letter
  over the 10 keys and its count n. The sign has a **consensus letter** only if n >= 6 (a strict majority of 10); otherwise
  "no consensus".
- **Control** = the identical consensus procedure (seeds 1..10, n >= 6) on the four-leaf stream order-shuffled with
  `random.Random(k).shuffle`, k = 1..5 (the same five shuffles as N4-C1). Five control consensus keys, 50 anneals.
- Seeds 1-3 and shuffles k s1 are re-run fresh into `two/cons/` (not reused); the solver is seeded, so seed 1 must reproduce
  `two/key_real_s1.tsv` exactly -- reported as a determinism check.

## Statistic and gate
- **A_cons** = share of cipher-token occurrences in the full six-leaf stream (C signs a, d, e, ee, p, sd excluded; signs key.tsv
  lacks excluded) whose consensus letter equals key.tsv's letter. A sign with no consensus letter, or absent from the four leaves,
  counts as **disagreement** (it stays in the denominator), so a consensus cannot score by abstaining.
- **Gate: PASS** if A_cons(real) > max A_cons over the 5 shuffled controls. FAIL: no grade changes; reported as the result.
- **Why the shuffled-order control can differ on this statistic (rule 3 orthogonality).** A_cons is a function of the letters the
  anneals assign, and those letters are driven by the n-gram (order) model: shuffling the order keeps every sign's frequency but
  destroys every bigram/trigram context, so a control consensus can agree with key.tsv only as far as frequency rank alone
  explains, and its seeds can also fail to agree with each other (fewer n >= 6 signs). The manipulation (order) is not orthogonal
  to the statistic (order-driven letter assignments), unlike a coverage count. N4-C1's single-seed control already varied
  0.033-0.351 on the sibling statistic, so this control is shown able to move.

## Per-sign regrade rule (applied only if the gate PASSes)
Only the 28 currently M-graded signs are candidates. A sign goes **M -> S** iff all hold:
1. it has a real consensus letter (n >= 6 of 10) and that letter equals key.tsv's value;
2. in at most 1 of the 5 shuffled-control consensus keys does the same sign also get key.tsv's letter with n >= 6
   (per-sign frequency-only guard: an agreement the shuffled order reproduces is not evidence of order information).
Otherwise the sign stays M; its source cell records the consensus letter and n. **No key value is changed in this pass**: where the
real consensus (n >= 6) gives a different letter from key.tsv, the sign stays M and the alternative is logged as a next step (a value
change needs its own test, e.g. the c186R gloss match and the judge, plus a rule-7 re-derivation). The 15 S and 6 C signs are not
regraded; their consensus is reported for information only (a consensus that contradicts an S sign is reported, not acted on).

## Reported
Per sign (all keyed non-C signs): key.tsv value and grade, real consensus letter and n, count of shuffled controls agreeing with
key.tsv at n >= 6, decision. A_cons real and the 5 controls; A_cons type-weighted (not gated). Then `tools/decode_key.py` and
`--check`; if any grade changed, a note that a rule-7 re-derivation is owed.
