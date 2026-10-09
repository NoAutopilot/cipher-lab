# TXP-REBUILD results: gloss-item truths re-derived from a key independent of the reads (9 Oct 2026, 16:34-16:4x UTC by date -u)

LANE TX-ENGINEER-2 round 2, PREREG `benchmark-tx/PREREG-txeng2-2.md` section R (binding). Read-free: no vision call, no reader.
Truth variants written by the build scripts (`--variant keyprint|jackknife`, helper `benchmark-tx/truth_variant.py`), never by
hand; truth files + BENCHMARK-TX rows committed in a32c22f84 BEFORE any score. Offline test `tools/tests/test_truth_variant.py`
(incl. `--variant ... --check` on all four, rule 7); the four default builds still `--check` up to date.

## Rule as implemented (stated)
- S(L) from `f128/print_align/key_print.tsv`: agree/n >= 0.75 and n >= 3 -> `.` e, `3` d, `4` l, `9` g, `D` a, `L` i, `T` h,
  `a` q, `al` u, `c` r, `f` n, `m` u, `r` n, `sq` s, `w` r, `y` o, `z` m, `p` i; written in reader labels (dint128_label_map:
  D -> `4`, al -> `a`), so reader `4` is in S(a) and S(l), reader `a` in S(q) and S(u). Not qualifying: `0` e 11/18, `v` a 8/13,
  `1` e 3/7, `#` c 7/13, `plus` l n 1, `zh` t n 2, `B`, `div`, `h`, `n`, `o`. Primed labels (0', v') are their own sheet cells,
  never in S(L).
- "Alignment flagged uncertain" = one rule for all leaves: a same-line neighbour (+-1) with interlinear_align status
  `conflict:*` (f89's declared rule). The position's OWN status is not used: it compares the chunk with passZ's own sign's
  leaf majority, which would exclude passZ's misreads by construction (the round-0b flaw the PREREG names).
- Same alignment as each round-0b build (f89 unseeded; f98v and f113 seeded by key_print only); gloss wildcard = gloss-unread.
- Jackknife (bir1591): per line i, key from all other lines' wildcard-free non-empty chunks, majority one letter, n >= 2,
  agree >= 0.75, on-sheet; grade **C-**.

## Scores (tools/tx_bench.py; paired vs passZ_pipeline)
| item | scored / positions | passZ err_true (95%) | passA | passB (fixed/broken vs Z, p) |
|---|---|---|---|---|
| dint-f89-gloss (0b) | 240 / 573 | 0.042 (10) 0.023-0.075 | 0.079 (19) | 0.121 (29), 0/14 p 0.0001 |
| **dint-f89-gloss-kp** | **223 / 573** | **0.390 (87) 0.329-0.456** | 0.421 (94), 2/1 p 1.0 | 0.444 (99), 1/7 p 0.070 |
| dint-f98v-gloss (0b) | 53 / 246 | 0.000 (0) | 0.057 (3) | 0.019 (1) |
| **dint-f98v-gloss-kp** | **66 / 246** | **0.515 (34) 0.397-0.631** | 0.561 (37), 0/1 | 0.500 (33), 2/0 p 0.50 |
| dint-f113-gloss (0b) | 81 / 186 | 0.000 (0) | 0.012 (1) | 0.025 (2) |
| **dint-f113-gloss-kp** | **71 / 186** | **0.465 (33) 0.354-0.580** | 0.465 (33), 0/0 | 0.465 (33), 0/0 |
| bir1591-f23r-gloss (0b, eval) | 203 / 330 | 0.079 (16) | 0.084 (17) | 0.103 (21), 1/6 p 0.125 |
| **bir1591-f23r-gloss-jk** (C-, eval) | **191 / 330** | **0.241 (46) 0.186-0.306** | 0.246 (47), 0/1 | 0.246 (47), 2/3 p 1.0 |

Excluded classes: f89-kp align-uncertain 159, gloss-unread 110, letter-no-keyprint-sign 51, unaligned 27, multi-letter 3;
f98v-kp unaligned 70, align-uncertain 63, letter-no-keyprint-sign 21, multi-letter 15, gloss-unread 11; f113-kp unaligned 53,
align-uncertain 37, multi-letter 13, letter-no-keyprint-sign 11, gloss-unread 1; bir-jk unaligned 68, align-uncertain 49,
letter-no-jackknife-sign 19, multi-letter 3. bir1591 is split eval: scored here only as the PREREG R truth validation the
section names (baselines on a new truth), no instrument, no look spent. On f113-kp passA, passB and passZ read identically
on all 71 scored positions.

## Registered prediction: E > 0 holds; "about 10-20% of scored on f.89" FAILS (observed 39.0%)
Post-hoc diagnostic, declared after the scores (changes no truth, no gate; `txeng2/rebuild/diagnose.py`): passZ's -kp errors
split by what key_print says of passZ's own sign:
| item | passZ errors | kp-same-below-gate | not-in-kp (primed, X_, NEW) | kp-other |
|---|---|---|---|---|
| f89-kp | 87 | **61** | 14 | 12 |
| f98v-kp | 34 | 14 | 9 | 11 |
| f113-kp | 33 | 16 | 5 | 12 |
| bir-jk | 46 | leaf-same 32 (support only on line i) | -- | leaf-other 14 |
kp-same-below-gate = passZ's sign has key_print majority L but misses 0.75/n>=3 (top: e <- `0` x27, a <- `v` x15, e <- `1` x12,
l <- `+` x7 on f89): S(L) is incomplete, so a real homophone is charged as an error. On f89 70% of E is this artifact; the
kp-other share (12/223 = 5.4%, up to 11.7% with not-in-kp) is the part that can be a reader error, decipherer slip or
alignment slip. The same holds for the jackknife: 32/46 are signs whose only support is line i itself.

## Pooling gate (declared in R)
| item | scored >= 100 | GAPS4 rank 1/201 unseeded or kp-seeded | enters dev pool by the rule |
|---|---|---|---|
| dint-f89-gloss-kp | 223 yes | rank 1, unseeded | **yes** |
| dint-f98v-gloss-kp | 66 no | rank 1, kp-seeded | no |
| dint-f113-gloss-kp | 71 no | rank 1, kp-seeded | no |
| bir1591-f23r-gloss-jk | 191 (eval split, not a dev candidate) | rank 1, unseeded | -- (eval pool stays 34 per R) |

**Flag for the lane (rule 3, not acted on here):** f89-kp passes the declared gate, but about 61 of its 87 errors are truth-set
incompleteness, not reads. Pooled as is it (a) inflates dev E 37 -> 124 and the planted-fixer power, and (b) rewards an
instrument that rewrites reads of `0`/`v`/`1`/`+` toward the key_print-qualified homophone (`.`, `4`, ...) -- a fix by
notation, not by image. The lane decides; an amendment would need declaring before any instrument is scored on it (e.g.
S(L) at n >= 3 with agree >= 0.5, or the kp-same-below-gate positions excluded as a class).

## Power (tools/tx_power.py, 1000 draws, seed 1; full table `power.md`)
| unit / pool | E | N | clean 30% @0.01 | @0.05 | clean 50% @0.01 | @0.05 | worse/no-op/random3 |
|---|---|---|---|---|---|---|---|
| f89_kp (passZ) | 87 | 223 | 1.000 | 1.000 | 1.000 | 1.000 | <= 0.001 |
| f98v_kp | 34 | 66 | 0.847 | 0.954 | 1.000 | 1.000 | 0.000 |
| f113_kp | 33 | 71 | 0.796 | 0.958 | 1.000 | 1.000 | 0.000 |
| bir_jk (eval, C-) | 46 | 191 | 0.974 | 0.998 | 1.000 | 1.000 | 0.000 |
| dev today (dev_tune + dint_B + f87_C + f36v) | 37 | 583 | 0.907 | 0.986 | 0.999 | 1.000 | 0.000 |
| dev gated (+ f89_kp) | 124 | 806 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 |
| dev + all three -kp | 191 | 943 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 |
(dev today re-run here gives 0.907 against the PREREG-0 table's 0.914 at clean 30% @0.01; same units, tool draw noise.)

## Calls and cost
0 vision calls, 0 subagents, 0 network requests. Dollar figure: the orchestrator's get_session reading.
