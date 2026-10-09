# TXP-KP2 results: homophone-complete key_print truth for the Dinteville gloss items (9 Oct 2026, 17:14-17:2x UTC by date -u)

LANE TX-ENGINEER-2 round 3, PREREG `benchmark-tx/PREREG-txeng2-3.md` section R2 (binding). Read-free: no vision call, no
reader, no network. Truth variant written by the build scripts (`--variant kp2`, `benchmark-tx/truth_variant.py`
`kp2_inverse`), never by hand; truth files + BENCHMARK-TX rows committed in c2add5a97 BEFORE any score. Offline test
`tools/tests/test_truth_variant.py` (kp2 inverse incl. multi-valued signs; `--variant kp2 --check` on all three; the
keyprint/jackknife variants and the default builds still `--check` up to date). Raw tx_bench output: `scores.txt`.

## Rule as implemented (as declared in R2)
S(L) = every key_print sign with value L at share >= 0.3 of its n and n >= 2, counting the majority value and the `others`
column; a multi-valued sign belongs to every such L; label-map merged as in R (D -> 4, al -> a, zh -> m). Resulting S:
a {4, v}; c {#}; d {#, 3}; e {., 0, 1, o}; g {9}; h {T}; i {1, L, p}; l {4}; m {z}; n {f, r}; o {y}; q {a}; r {c, w};
s {sq}; t {m, v}; u {a, m}. Still outside: `+` (plus, n 1), `B`, `div`, `h`, `n` (n 1); `0` as s (4/18), `m` as t (2/10),
`sq` as x (2/9). Scored positions, alignment, neighbour-conflict rule and exclusion classes exactly as R.

## Scores (tools/tx_bench.py; paired vs passZ_pipeline)
| item | scored / positions | passZ err_true (95%) | passA (fixed/broken vs Z) | passB (fixed/broken vs Z, p) |
|---|---|---|---|---|
| dint-f89-gloss-kp | 223 / 573 | 0.390 (87) 0.329-0.456 | 0.421 (94), 2/1 | 0.444 (99), 1/7 p 0.070 |
| **dint-f89-gloss-kp2** | **249 / 573** | **0.124 (31) 0.089-0.171** | 0.157 (39: 31 wrong + 8 ins), 2/2 p 1.0 | 0.137 (34: 28 + 6 ins), 3/0 p 0.25 |
| dint-f98v-gloss-kp | 66 / 246 | 0.515 (34) 0.397-0.631 | 0.561 (37), 0/1 | 0.500 (33), 2/0 p 0.50 |
| **dint-f98v-gloss-kp2** | **76 / 246** | **0.303 (23) 0.211-0.413** | 0.382 (29), 0/4 p 0.125 | 0.289 (22), 2/0 p 0.50 |
| dint-f113-gloss-kp | 71 / 186 | 0.465 (33) 0.354-0.580 | 0.465 (33), 0/0 | 0.465 (33), 0/0 |
| **dint-f113-gloss-kp2** | **75 / 186** | **0.187 (14) 0.115-0.289** | 0.200 (15), 0/1 | 0.173 (13), 1/0 p 1.0 |
bir1591-f23r-gloss has no key_print (another key family): no kp2 is defined for it; it stays -jk (C-) and out of every pool.

Excluded classes (kp2): f89 align-uncertain 174, gloss-unread 110, unaligned 27, letter-no-keyprint-sign 10, multi-letter 3;
f98v unaligned 70, align-uncertain 64, multi-letter 15, letter-no-keyprint-sign 10, gloss-unread 11; f113 unaligned 53,
align-uncertain 39, multi-letter 13, letter-no-keyprint-sign 5, gloss-unread 1. (Align-uncertain rises vs kp because more
letters now have an S(L), so positions that were letter-no-keyprint-sign reach the neighbour rule.)

## Pool rule (fixed in R2 before scoring) -- decision
| item | scored >= 100 | GAPS4 rank 1/201 unseeded | passZ err_true <= 0.25 | decision |
|---|---|---|---|---|
| dint-f89-gloss-kp2 | 249 yes | rank 1 of 201, unseeded (0.525 vs shuffled max 0.105) | 0.124 yes | **enters the DEV pool** |
| dint-f98v-gloss-kp2 | 76 | -- | -- | out of every pool (R2) |
| dint-f113-gloss-kp2 | 75 | -- | -- | out of every pool (R2) |
| bir1591-f23r-gloss-jk | -- | -- | -- | out of every pool (R2) |
f89-kp (round 2) is superseded for pooling by f89-kp2 per R2; the lane names which f89 truth the pool carries.

## Residual (read-free, after the scores; changes no truth, no gate)
passZ's kp2 errors by what key_print says of passZ's own sign: f89 31 = not-in-kp 15 (primed 0'/m'/v'/w', X_* labels),
kp-other 9, key_print has L but below kp2 (n 1 or share < 0.3) 7 (all `+` read where the gloss has l: plus n 1); f98v 23 = 13 / 8 / 2; f113 14 =
5 / 8 / 1. The notation artifact R2 targeted (61 of 87 on f89-kp) is down to 7 of 31; the rest is reader labels key_print
never saw or a read key_print gives another value -- reads, decipherer slips or alignment slips, not separable read-free.

## Power (tools/tx_power.py, 1000 draws, seed 1; full table `power.md`)
| unit / pool | E | N | clean 30% @0.01 | @0.05 | clean 50% @0.01 | @0.05 | noisy0.1 30% @0.05 | worse/no-op/random3 |
|---|---|---|---|---|---|---|---|---|
| f89_kp2 (passZ) | 31 | 249 | 0.783 | 0.938 | 0.999 | 1.000 | 0.390 | 0.000 |
| f98v_kp2 | 23 | 76 | 0.416 | 0.748 | 0.948 | 0.995 | 0.314 | 0.000 |
| f113_kp2 | 14 | 75 | 0.042 | 0.229 | 0.404 | 0.774 | 0.077 | 0.000 |
| dev today (dev_tune + dint_B + f87_C + f36v) | 37 | 583 | 0.902 | 0.987 | 1.000 | 1.000 | 0.426 | 0.000 |
| **dev + f89_kp2** | **68** | **832** | **0.999** | **1.000** | **1.000** | **1.000** | 0.755 | 0.000 |
| dev + f89_kp (round 2, for comparison) | 124 | 806 | 1.000 | 1.000 | 1.000 | 1.000 | 0.982 | 0.000 |
Units: dev_tune = birago1572-no87 : txeng/units/labels_dev_tune.tsv; dint_B = dint-f128-print : passB + dint128_label_map;
f87_C = ceppo-f87-S : passC; f36v = ceppo-f36v-gloss : recon (E/N reproduce the PREREG-0 / TXP-REBUILD rows: 12/343, 11/85,
7/139, 7/16; dev today 37/583, 0.902 here vs 0.907 / 0.914 earlier, draw noise).

## Calls and cost
0 vision calls, 0 subagents, 0 network requests (git only). Dollar figure: the orchestrator's get_session reading.
