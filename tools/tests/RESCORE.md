# tools/tests consumers of the no.87 box map -- RESCORE (11 Oct 2026, 18:0x UTC by date -u)

**Measurement correction: box-to-position map fixed (off by one), not a new gate look.**

Job BOXMAP-RESCORE (others) for the account-3 parent (session_0198Cv8ypBfBVfRToKVWx33M). Script-only: no vision call, no reader, no
image viewed (the oddness audit and the classifier compute on page pixels by script, as originally), no network beyond git. No truth
file, BENCHMARK-TX.tsv row, frozen confirm item or owner page touched.

Four results here joined no.87 tiles to positions through `ciphers/nevers-birago-fr3251-1572/atlas/no87_box_token.tsv`, which is one
token off on 10 of 26 lines (`ciphers/nevers-birago-fr3251-1572/atlas/RESCORE.md`). **Only the map changed**: each script gained a
`--map` option (default unchanged; checked byte-identical or number-identical with the old map), fed the label-aware map
(`no87_box_token_labelaware.tsv`) or, where the consumer reads the old file's `truth` column, `atlas/no87_map.py --compat OUT` (temp
only: it carries the clerk alignment). Everything re-runs with `sh tools/tests/rescore_boxmapLA/rescore.sh`.

## 1. MQS-SHEETS G3, the KM box-map test (`km_birago_map.py`)

`km_birago_map.py` imports `tools/decipher_sheet.py`, which needs Python >= 3.12, and this container's 3.12 has no numpy/opencv;
`rescore_boxmapLA/km_rescore.py` is the same statistic without that import, and with the old map it reproduces the committed line
exactly. `km_birago_map.py` also gained `--map`.

| map | held-out 1:1 tokens | classify top-1 = own label | **neighbour's label** | null mean / p95 / max | gate (>= 0.55, > p95) |
|---|---|---|---|---|---|
| old (PREREG-MQS-SHEETS result) | 381 | 231 (0.606) | **75** | 0.066 / 0.085 / 0.094 | PASS |
| label-aware | 373 | 304 (**0.815**) | **3** | 0.069 / 0.097 / 0.099 | PASS |
| sorter-only sensitivity (no atlas labels; `atlas/rescore_boxmapLA/variants.py`) | 375 | 302 (0.805) | 4 | 0.064 / 0.087 / 0.109 | PASS |

**The gate verdict is the same, the reading is not.** The PREREG note says "a map wrong by one position fails and a map right passes
... no sign of a systematic mis-mapping". A map wrong by one position on 10 of 26 lines passed: the gate (0.55 and above a within-line
permutation null) cannot see a partial shift. The diagnostic was the neighbour count printed beside it, 75 of 381 then, 3 of 373 now.
A KM pass should not be cited as evidence that a box map is right; the neighbour count should carry a bound.

**R-K1** (`test_decipher_sheet.py`) is a regression test that the reading sheet cuts each tile at the box the map assigns; it passes
with any map and its conclusion (the code path) does not depend on which map. It was not run here (Python 3.12 without numpy). Note
that `tools/decipher_sheet.py`'s default Birago box map is still the old file, so a no.87 reading sheet built today would cut wrong
tiles on 10 lines; Birago sheets are refused while ASKS 118 is open (MQS-SHEET-REFUSAL), so none was shown. Pointing the default at the
label-aware map is a one-line tool change for the lane, not made here.

## 2. MQS-CLASSIFY-ROUNDS (`mqs_classify_rounds_run.py`)

The runner gained `--map`, `--labels`, `--out`, and `--legacy` on its tx_bench call: tx_bench's default scorer changed on 10 Oct and
its regexes no longer matched (the runner crashed as committed); with `--legacy` and the old map it reproduces
`MQS-CLASSIFY-ROUNDS-results.tsv` row for row. The map enters through arm C's training set (verified 1:1 tiles of half A, f178v
L13-L18: L13 and L17 are shifted) and M2 (`score_no87.py`).

| run | arm C round0 -> round1 (M1) | gain | fixed / broken | null gain p95 | M2 | arm T gain |
|---|---|---|---|---|---|---|
| committed (old map) | 0.204 -> 0.194 | 0.010 | 2 / 0, p 0.50 | 0.000 | 0.322 | 0.000 (null p95 0.000) |
| label-aware map (153 training tiles) | 0.204 -> 0.194 | 0.010 | 2 / 0, p 0.50 | 0.005 | **0.103 -> 0.100** | 0.000 |
| + atlas names re-derived on that map | 0.199 -> 0.190 | 0.009 | 2 / 0, p 0.50 | 0.005 | 0.089 -> 0.086 | 0.000 |

**Conclusion unchanged:** Gate C FAILs (gain under 0.02, p 0.50), Gate T FAILs; the option stays `weak` on the same numbers. M2's 0.322
was the map (see the atlas RESCORE); M1 does not use the map.

## 3. MQS-SORTER B: the owner's 4 Oct no.87 sort scored against BENCHMARK-TX (`mqs_sorter_score_owner.py`)

Registered rule unchanged (family piles take the printed value; owner-made piles read unknown). "Old map, today" differs from the
committed figure by one position because TX-TRUTH-VERIFY changed the truth after the 9 Oct run, not because of the map.

| | committed (9 Oct) | old map, today | **label-aware map** |
|---|---|---|---|
| scored positions | 200 | 200 | 198 |
| owner err_true (registered) | 0.260 (0.204-0.325) | 0.260 | **0.121 (0.083-0.174)** |
| committed reads, same positions | 0.020 | 0.015 | 0.010 |
| fixed / broken | 0 / 48 | 0 / 49 | **0 / 22** |
| moved: owner wrong / n | | 7 / 19 | 6 / 19 |
| kept: owner wrong / n | | 45 / 181 | **18 / 179** |
| diagnostic, owner-made piles left out | 0.176 (31/176) | 0.176 | **0.006 (1/175) = committed reads 0.006 (1/175)** |

With the right join, the owner's tiles in family piles are wrong at 1 of 175 positions, the same as the committed line reads; 23 of the
24 remaining "owner wrong" positions are tiles in his own new piles (T24-b, T89-b, X_NEW-l, T60-d ...), which the registered rule reads
as unknown. **The conclusion changes**: the shelf line "err_true 0.260 vs committed reads 0.020, fixed 0 broken 48" was mostly the map;
what is left is the scoring rule for owner-made piles, not the owner's eye. (Same finding as TXE3-9's kept tiles and BIR87-ALIGN's
disagreements: `benchmark-tx/txeng3/9/RESCORE.md`, `ciphers/nevers-birago-fr3251-1572/harvest/bir87align/RESCORE.md`.)

## 4. MQS-SORTER A: `sign_sorter.py --oddness-audit` on the no.87 known answer (`oddness_no87_inputs.py`)

The "clean" known-answer tiles are 1:1 tiles whose line-read sign decodes to the clerk letter at their token; with the old map, a
shifted tile whose token verifies entered its neighbour's pile as clean, so the piles already held unplanted misfits that competed with
the planted ones. `oddness_no87_inputs.py --map` is new. `rescore_boxmapLA/oddness_audit.tsv`:

| order | plants | before: mean recall@10%, seeds above p95, seeds passing | **after** |
|---|---|---|---|
| mean (page order) | random | 0.498, 20/20, **1/20** | **0.787, 20/20, 20/20** |
| mean | look-alike | 0.282, 16/20, 0/20 | 0.505, 20/20, 3/20 |
| medoid | random | 0.497, 20/20, 1/20 | 0.766, 20/20, 20/20 |
| medoid | look-alike | 0.260, 14/20, 0/20 | 0.485, 20/20, 1/20 |
| knn3 | random | 0.494, 20/20, 2/20 | 0.800, 20/20, 20/20 |
| knn3 | look-alike | 0.271, 14/20, 0/20 | 0.514, 20/20, 4/20 |

Clean tiles 635 -> 624 (622 -> 615 in 35 -> 37 piles of >= 3).

**The registered gate result reverses** (PREREG-MQS-SORTER A: random plants recall >= 0.6 and above the shuffled p95 in >= 18 of 20
seeds): FAILED 1/20 -> **met 20/20** for the page order and both variants. Look-alike plants (the real error kind) rise from 0.28 to
0.51, above the shuffled p95 in every seed, still under 0.6. As with every rescore here, this is the same instrument re-measured after a
fix made for another reason; whether `sign_sorter.py`'s shelf grade moves from `weak` is for the verifier and the lane.
