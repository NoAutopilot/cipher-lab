# TXD-HOLDOUT results (3 Oct 2026, account-1 worker for LANE-A1)

Pre-registration `PREREG.md` pushed at 0b9a9955 before any score. Script `holdout.py` (from ciphers/: `python3
nevers-birago-fr3251-1572/harvest/tx_decode/holdout/holdout.py c|a|b|ad`), outputs `c.json`, `a.json`, `b.json`,
`a_shuffled_target.json`. Disk only: 0 requests, 0 vision calls. Tool `tools/key_decode_lattice.py` unchanged.

## (c) Held-out lam tune (no.87 lines f178v_L12-L23, f178r, f179r; 521 aligned signs; f178v_L01-L11 not used)
| lam | 1 | 2 | 3 | **4** | 6 | 8 |
|---|---|---|---|---|---|---|
| wrong / 521 | 54 | 39 | 38 | **36** | 37 | 37 |
| err | 0.1036 | 0.0749 | 0.0729 | **0.0691** | 0.0710 | 0.0710 |
| err with U | 0.1670 | 0.1286 | 0.1267 | **0.1228** | 0.1248 | 0.1248 |
Chosen lam = 4 (same as TX-DECODE's), so no re-run. Margin: one sign over lam 6/8, two over lam 3 (top-1 is 38 wrong,
0.0729). The selection is genuine but thin. NB these held-out lines are the same ones TX-DECODE used to *check* lam 4
after picking it on f178v_L01-L11; here they choose it, as the brief asks, and agree.

## (a) Wrong-key gate at lam 4 (printed key vs 200 partition-preserving relabelings W1 + 18 letter rotations W2)
| letter | printed score | W1 rank / z (max) | W2 rank / z (max) | wrong keys >= printed | clerk variant (reference) | gate (a) |
|---|---|---|---|---|---|---|
| f.144r (no.73, 90) | -0.945 | 1/201, 4.64 (-1.217) | 1/19, 4.02 (-1.151) | 0 of 218 | -0.972 | PASS |
| f.168 (no.85, 122) | -1.019 | 1/201, 6.78 (-1.447) | 1/19, 5.03 (-1.364) | 0 of 218 | -1.019 | PASS |
| f.117r (no.77, 279) | -1.081 | 1/201, 6.92 (-1.438) | 1/19, 6.88 (-1.603) | 0 of 218 | -1.103 | PASS |

**Post-hoc diagnostic (NOT pre-registered, added after a-c were scored): can gate (a) fail?** Same 218 wrong keys on
position-shuffled lattices (seeds 100-104):
| letter | printed rank among 219 / z, seeds 100-104 | shuffled targets where gate (a) still PASSes |
|---|---|---|
| f.144r | 2/2.57, 5/2.04, 2/2.87, 1/2.84, 3/2.35 | 1 of 5 |
| f.168 | 1/3.64, 2/2.80, 1/3.24, 1/3.02, 1/3.22 | 4 of 5 |
| f.117r | 1/4.00, 1/3.52, 2/3.09, 1/4.65, 1/4.12 | 4 of 5 |
Gate (a) PASSes on 9 of 15 shuffled targets, so on its own it mostly measures how well the key's letter frequencies
fit the sign frequencies, not text: a rank-1 PASS against these wrong keys licenses little (rule 3, a control that passes
by construction on the null). What does separate is the z margin: real order 4.64 / 6.78 / 6.92 against a shuffled-target
max 2.87 / 3.64 / 4.65 (W1+W2 pooled). The discriminating control remains TX-DECODE's value-shuffle ranking, under which
the real key never ranked 1 on a shuffled target (best 4/201).

## (b) lam sweep (rank / z among 200 value-shuffled keys, seed 1)
| letter | lam 1 | 2 | 3 | 4 | 6 | 8 | label (rule stated in PREREG) |
|---|---|---|---|---|---|---|---|
| f.144r | 2 / 2.16 | 1 / 2.61 | 1 / 2.88 | 1 / 3.10 | 2 / 2.43 | 12 / 1.68 | tuned-only (rank 1 at lam 2-4 only) |
| f.168 | 1 / 2.55 | 1 / 2.33 | 1 / 2.58 | 1 / 2.77 | 1 / 2.56 | 5 / 2.08 | robust |
| f.117r | 1 / 3.28 | 1 / 3.48 | 1 / 3.28 | 1 / 3.66 | 1 / 3.31 | 1 / 3.44 | robust |

## (d) Judge
No re-run text (c chose lam 4). TX-DECODE's figures stand, side by side with its shuffled-target lattice decode (seed 100):
f.144r PASS -0.945 (real_p05 -0.979; shuffled -1.213); f.168 FAIL -1.019 (real_p05 -0.958; shuffled -1.301); f.117r FAIL
-1.081 (real_p05 -0.903; shuffled -1.382). The f.144r PASS is on a text 12 of whose 90 signs the language model chose.

## Verdict (pre-registered rule: gate (a) PASS at lam 4 AND (c) selects lam 4)
- **f.144r: lam-4 rank 1 survives held-out control** -- by the stated rule; but its rank 1 holds only at lam 2-4 (rank 2 at
  lam 1 and 6), the gate (a) PASS is weak evidence by the post-hoc diagnostic, and (c) chose lam 4 by one sign. The weakest.
- **f.168: lam-4 rank 1 survives held-out control** -- rank 1 at lam 1-6 (robust), z 2.33-2.77, modest.
- **f.117r: lam-4 rank 1 survives held-out control** -- rank 1 at every lam tried (1-8), z 3.28-3.66; the strongest.
No reading committed; nothing graded above S; no novelty classed.
