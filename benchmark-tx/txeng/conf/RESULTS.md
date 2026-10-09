# TXE-E: a confusion matrix learnt on dev re-weights the key-constrained lattice (LANE TX-ENGINEER idea M5, 9 Oct 2026)

Brief `.claude/briefs/runs/2026-10-09-account4-txe-e.md`; PREREG `benchmark-tx/PREREG-txeng-2.md` (gate fixed > broken,
p < 0.01, Amendment). Worker TXE-E (account 4, Opus), 07:19-07:26 UTC by date -u. Read-free: **0 vision calls, 0 reader
calls, 0 network requests**; every number from passes already on disk.

**Verdict: FAIL.** Dev gate not met: vs L_dev_tune fixed 3, broken 7, p = 0.34 (lam 4); vs the plain lam-4 lattice fixed 0,
broken 0 (the decodes are identical on all 343 scored signs). No eval look taken (eval_heldout untouched, 0 of 1 used).

## What was built (tools/key_decode_lattice.py; test tools/tests/test_key_decode_lattice.py, 11 pass)
- `from-passes ... --confusion-matrix M.tsv [--spread S] [--matrix-only]`: each read sign r adds candidate t with weight
  S x w(reader) x p(r|t) / sum_t p(r|t) for every t with p(r|t) > 0 (flat-prior Bayes flip), on top of the fixed rule; S 0.3.
- `learn-confusion PASS.tsv ... --truth T --lines L... --out M.tsv [--key] [--line-prefix] [--per-pass] [--shuffle-offdiag SEED]`:
  P(read | true) from `tx_bench.align` (imported), scored positions only, a truth `|`-set splits a miss equally over its
  members, add-0.5 smoothing over the key's 51 signs; the learnt lines are written in the file's `#` header.
  `--shuffle-offdiag` is the rule-3 control matrix (off-diagonal cells permuted within each true row, row mass kept).

## Protocol (as briefed)
Harness `benchmark-tx/txeng/conf/run_conf.py dev` (regenerates everything; ~11 s). Inputs as TX-DECODE
(`harvest/tx_decode/run.sh`): blind passes A/B of f178v (L01-10 + L11-23 files), skeleton = committed passC restricted to the
page (its signs are not candidates), `confusion_1572.tsv`, printed key `key_1572_sheet.tsv`, LM **it16dip** (TX-DECODE's
corpus choice; the brief's "`--lang it`" conflicts with "reuse its corpus choice" -- I kept TX-DECODE's), beam 64.
Leave-one-line-out: for each dev line h, M learnt on the other 11 (pooled A+B, ~627 aligned reads, ~48 misses), the lattice
of h rebuilt with `--confusion-matrix`, the other 11 lines left on the plain lattice (so no neighbour lattice carries h's
truth), the 12-line unit decoded, line h kept. Matrices `dev_loo/M_conf_minus_*.tsv`; decodes committed (336a84fc) before
`tx_bench` ran.

## Learnt matrix (all 12 dev lines; diagnostic, `learn-confusion` top off-diagonal)
| truth <- read | p(read \| true) | excess over row floor |
|---|---|---|
| T18 <- T98 | 0.111 | 0.100 |
| T63 <- T98 | 0.109 | 0.098 |
| T29 <- T88 | 0.085 | 0.068 |
| T66 <- T76 | 0.084 | 0.067 |
| T95 <- T50 | 0.055 | 0.040 |
| T57 <- T50 | 0.054 | 0.040 |
| T92 <- T50 | 0.052 | 0.039 |
| T88 <- T42 | 0.057 | 0.038 |

The class-1 pairs are there (d T18/T63 <- s T98; e T66 <- n T76). But the flat-prior posterior for read T98 is T98 0.246,
T18 0.086, T63 0.084: add-0.5 over 51 cells spreads ~0.5 of each column over 48 zero-count signs. At S 0.3 that gives T18 about
0.026 of one reader's weight, which normalises to below the lattice's 0.02 floor once both readers and the 1572 spread are
summed. **Mechanism of the FAIL:** the smoothing dilutes the flip below the floor, so the learnt pairs rarely enter the lattice.

## Dev scores (tx_bench, `--paired`)
```
passM_conf_dev_tune.tsv (lam 4)        err_true 0.055 (19/343) 0.036-0.085 | wrong 17 deleted 1 inserted 1
paired passM_conf_dev_tune.tsv vs labels_dev_tune.tsv: 343 common; base wrong 14, output wrong 18; fixed 3, broken 7; p = 0.3438
paired passM_conf_dev_tune.tsv vs passL_lattice_dev_tune_lam4.tsv: 343 common; base wrong 18, output wrong 18; fixed 0, broken 0; p = 1.0000
passM_conf_dev_tune_lam1.tsv (lam 1)   err_true 0.085 (29/343) 0.059-0.119
paired passM_conf_dev_tune_lam1.tsv vs labels_dev_tune.tsv: base wrong 14, output wrong 28; fixed 3, broken 17; p = 0.0026 (worse)
paired passM_conf_dev_tune_lam1.tsv vs passL_lattice_dev_tune_lam1.tsv: base wrong 29, output wrong 28; fixed 2, broken 1; p = 1.0000
baseline passL_lattice_dev_tune_lam4.tsv vs labels_dev_tune.tsv: fixed 3, broken 7, p = 0.3438 (err_true 0.055)
baseline passL_lattice_dev_tune_lam1.tsv vs labels_dev_tune.tsv: fixed 3, broken 18, p = 0.0015 (err_true 0.087)
```
Truth in lattice (dev_tune, 343 scored): plain 331/343 (0.965), top-1 wrong 17 with the truth in the lattice at 5 of them;
with the matrix 331/343, 5 of 17: **unchanged** (the TX-DECODE 27/97 figure, recomputed on these lines, is 5/17 before and after).
Candidates per position 2.31 -> 2.22.

## Controls (rule 3)
- (a) value-shuffled M (`--shuffle-offdiag 1`, same LOO): fixed 3, broken 7, p = 0.34 vs L (lam 4); lam 1 fixed 3, broken 17.
  Identical to the real matrix. It does not pass the gate, as required, but the real M does not differ from it either: the
  control shows the matrix had no effect, not a gain that the shuffle removes.
- (b) shuffled-key, lam 4, 200 value-shuffled keys, f178v + f179r (26 lines), M learnt on all dev lines:
  matrix lattice rank 1, z 4.26 (shuffles mean -1.434, max -1.128); plain lattice rank 1, z 4.21. The real key still ranks first.

## Taxonomy (`tools/tx_taxonomy.py`, `taxonomy_dev.md` / `.tsv`, passes L, Lat4, M)
M repeats all 18 of Lat4's errors with the same wrong sign (18/18), so nothing moved because of the matrix. Every move vs L
comes from the lattice decode itself. Fixed 3: L06.18 d T98->T18 (class 1 d/s), L11.5 e T76->T66 (class 1 n/e), L11.29 e
T60->T86. Broken 7: s X_CE->T50 x3 (L04.4, L05.25, L08.10), d T18->T98 (L10.3, class 1 reversed), u T49->X_NEW (L02.9),
carmagnola T11->X_NEW (L03.24), l T95->deleted (L11.4).

## Post-hoc diagnostic (NOT a gate, not eligible for eval; `diag_posthoc.py`, output uncommitted scratch)
The same LOO with smoothing 0.01 and S 1.0, chosen after the FAIL to test the mechanism above: truth in lattice 334/343, with the
truth present at 8 of 17 top-1 errors (was 5). Decode vs plain lam-4 lattice: fixed 5, broken 1, p = 0.22. Vs L: fixed 3,
broken 3, p = 1.0, err_true 0.041 = L's. Lighter smoothing does put the learnt pairs into the lattice, but at this N the decode
only matches L. It does not beat it.

## Follow-up (one line, not done)
Any re-run with lighter smoothing, a non-flat prior or `--matrix-only` is a fresh dev attempt (a 2nd at this instrument).
Its dev headroom is bounded by the 9 to 12 dev errors whose truth is not in any reader's confusion, so the next step is a new
candidate source (atlas top-k / TXE-A), not another setting of this knob.
