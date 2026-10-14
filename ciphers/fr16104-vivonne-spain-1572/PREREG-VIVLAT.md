# PREREG-VIVLAT -- key-constrained lattice decode with a confusion matrix learnt on this hand (VIV-LAT)

Written 14 Oct 2026 00:0x UTC (date -u), before any score of the method was computed. Worker VIV-LAT for LANE VIV-KEYSTONE
(account 4); brief `.claude/briefs/runs/2026-10-13-acct4-keystone-viv-jobs.md`. Measurement only: nothing here edits key.tsv,
reading_piece63.tsv, status.json or any committed reading.

## Instrument and fixed settings
- `tools/key_decode_lattice.py` (shelf grade weak). Language model `--lang fr16` (tools/judge_plaintext.py corpus). Default beam,
  default unk_cost. Key: `key.tsv` columns code/meaning copied to `tx/vivlat/key_sv.tsv` as sign/value (all 32 rows, M rows
  included, no exceptions file -- decode.json absent).
- Passes: the independent blind passes only, columns renamed line->passage, sign->sign_id (alt, conf kept):
  f.102r dev2: `benchmark-tx/outputs/vivonne1573-f102r-dev/passA_dv1.tsv`, `passB_dv1.tsv`, `passZ_dv1.tsv`;
  f.103r confirm2: `benchmark-tx/outputs/vivonne1573-f103r-confirm2/passA_S2.tsv`, `passB_S2.tsv`, `passZ_S2b.tsv`.
- Lattice: `from-passes A B` (two readers, the tool's design; pass A is the skeleton, no --ref, so no committed reconciliation
  enters), `--confusion-matrix M --matrix-only`, default spread 0.3. Z is not a lattice reader (the tool takes two); Z IS used,
  with A and B, to learn the confusion matrix (pooled, not per-pass: `learn-confusion A B Z --key key_sv.tsv`, default
  smoothing 0.5).
- Output scored = the decode's `chosen` sign per position written as a pass (line, pos, sign). Baseline ("top-1 decode of the
  same passes") = the argmax sign per position of the PLAIN two-reader lattice (`from-passes A B`, no matrix, no --confusion),
  written the same way. Scorer `tools/tx_bench.py --item <item> --exclude-flagged --paired <top1.tsv> <lattice.tsv>`.
- lam grid {1, 2, 4, 8}.

## Step 1, dev (vivonne1573-f102r-dev2)
- Folds: odd line ids (L01, L03, ...) and even line ids. For fold k, M_k = learn-confusion on the OTHER fold's lines (A, B, Z vs
  dev2 truth). The whole page is decoded with M_k (lattice from A, B); only fold k's lines are kept. The two held halves are
  joined into one page file per lam and scored once, pooled.
- Dev rule: chosen lam = the lam with the largest (lines improved - lines worsened) in tx_bench's flagged-excluded paired
  line count vs the plain top-1; tie -> larger sign-level (fixed - broken) flagged-excluded; tie -> smaller lam.
- Dev stop rule: if the chosen lam's pooled flagged-excluded paired line result is not improved > worsened, dev FAILs and the
  confirm item is NOT looked at (it stays unspent for a later design).
- Dev controls recorded beside (not gating): the same pipeline with each M_k replaced by `--shuffle-offdiag 1` (off-diagonal
  cells permuted per true row) at the chosen lam; and truth-in-lattice share on the held folds.

## Step 2, confirm, ONE look (vivonne1573-f103r-confirm2)
- lam fixed from step 1; M = learn-confusion on ALL f.102r dev2 lines (A, B, Z). Lattice from passA_S2, passB_S2 with M.
  `decode --shuffles 100 --seed 1` (>= 50 value-shuffled keys).
- Gate, all three required: (a) flagged-excluded paired lines improved > worsened with tx_bench's line sign test p < 0.05, vs
  the plain top-1 of passA_S2+passB_S2; (b) as-measured err_true of the lattice decode <= the plain top-1's as-measured
  err_true; (c) the real key ranks 1 of 101 on the lattice decode's mean 4-gram score (tool's built-in control); the top-1
  decode's rank/z reported beside.
- Reported whatever the verdict: every tx_bench line, the shuffled-key ranks/z, and truth-in-lattice share = of the plain
  top-1's wrong scored positions (sign not in the truth set; matched by tx_bench alignment of the top-1 file to the truth
  skeleton, then the lattice row of the same skeleton position), the share whose truth set meets the lattice's candidate set.
  If under 50%, it is reported as the ceiling (as TX-DECODE's 27/97).

## Step 3, ink 63 (ff.190r-194r) -- only if the step-2 gate passes
Same recipe (lam fixed, M from all of f.102r dev2) on tx/f19x passA/passB, skeleton matched to the committed token skeleton as
viv63_clean.py builds it; outputs only under tx/viv63_lat/; every changed position graded S; longest clean run (AUDIT 2's
measure), judge score, five longest stretches. If the gate fails, step 3 is skipped; the failure is logged "untested-by-this-tool
at this error" only if truth-in-lattice < 50% explains it, else FAIL.

## Stop rule
Cap 6 usage dollars, box 00:00-01:30 UTC 14 Oct 2026 (80% at 01:12); no unit is started that would cross 80% of either.
Runner: `tx/vivlat/run_vivlat.py` (commands above, deterministic).
