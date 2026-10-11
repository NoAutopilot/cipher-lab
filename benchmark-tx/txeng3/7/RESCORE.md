# TXE3-7 PROPAGATE -- RESCORE (BOXMAP-RESCORE job 7; 11 Oct 2026, 17:1x UTC by date -u)

**Measurement correction: box-to-position map fixed (off by one), not a new gate look.** The X_NEW-l -> T19 variant in
section 5 is post hoc, reported separately, and is not a gate result.

Job 7 for the account-3 parent (session_0198Cv8ypBfBVfRToKVWx33M). No vision call, no reader, no image, no network beyond
git (0 requests to any other host). No truth file, BENCHMARK-TX.tsv row, owner page or frozen confirm item was opened for
editing. The outputs were pushed (d032372cd) before anything was scored.

## 1. Did TXE3-7 use the old map? (the question asked)

| part of TXE3-7 | joins through `atlas/no87_box_token.tsv`? | truth-free check (`rescore/diagnostics.py`, `diagnostics.txt`) |
|---|---|---|
| `sorter/no87/owner_map.tsv` (owner strip tile -> atlas box, the join behind the TRAINING labels) | **No.** The owner's tiles are on f.117r, f.144r and f.168r/v, not no.87. `build_inputs.py` moves each strip tile's centre back into the atlas page image and takes the box that contains it (427 of the 438 registered joins). For the other 11 it takes the nearest box centre within 0.6 x tile height. There is no sequential DP, so one stray box cannot push the tiles after it. | The owner's final label is in its box's atlas top-3 at offset 0 / -1 / +1 / -2 / +2 for 277 / 28 / 31 / 30 / 33 tiles. No strip line has -1 or +1 beating 0. **The join is sound.** |
| the A1 control's labels (`old_sign`, the 3 Oct start piles) | No, but **the same kind of defect.** On 3 Oct the start labels were attached to strip tiles by index. That sorter's README already warned "f117 L09: 29 vs 30; f168 R03: 18 vs 19 ... the tile index may be one off". | The start label is in the box's top-3 at +1 rather than 0 on f117_L09 (13 vs 5), f144r_L06 (13 vs 2) and f168_V01 (6 vs 0), and at -1 on f168_R03 and f168_V02. Of the **121** boxes where the owner's label differs from the machine's, **62** equal the start label of the next or previous tile on the strip: f117_L09 17 of 18, f144r_L06 13 of 15, f168_V02 8 of 13, f168_R03 6 of 10, f168_V01 5 of 8. |
| the no.87 target join in `run_arms.py` (kNN code -> line-read position) | **Yes.** All 714 `op == 1:1` rows, every arm. | The registered arms' own kNN top-1 equals the line read at 0 / -1 / +1 / -2 / +2 for A1 339 / 57 / 51 / 16 / 17 of 714 on the old map. Six lines have -1 or +1 beating 0: f178v L09, L11, L13, L17, f179r L02, L03 (A2 adds L21). On the corrected map the counts are 413 / 11 / 16 / 22 / 15 of 700, and no line is shifted. |
| the f152r target join (`map_f152r.py` -> `f152r_box_token.tsv`) | No: its own file. It does run the same width-only DP. | No line shifts as a whole. At the end of L04, box f152r_05_025 (atlas top-1 `_`) takes token 21, and boxes 05_026-028 land one token late (their labels equal the read at -1). That is 3 to 4 tokens of 90. |

The classifier side never touches either map. With `--only-train-labels`, the kNN votes come from the 438 owner-map boxes
alone, so the defect reaches TXE3-7 only through the target-side join.

## 2. What was re-run (same everything else)

- **Classify outputs.** I re-ran all 69 registered classify calls (A0a, A1, A2, A3 seeds 1-20 x f152r, f178v, f179r) at
  ed5d42162. All 69 are **byte-identical** to `runs/`, so the committed runs are reused.
- **Scorer.** I re-scored the registered outputs (`out/`) with today's `tools/tx_bench.py`. Every figure in `results.json`
  reproduces (`results_la.json` "scorer_drift").
- **The only change is the join.** no.87 now uses `atlas/no87_box_token_labelaware.tsv`, with `op == '1:1'` rows only, as
  registered. That is 700 boxes, against 714 before. The 3 `unsure` rows and the boxes that are now 2:1, 1:2 or bad-cut keep
  the line read in every arm, so they cancel in the paired counts. f178r still has no map.
  - f152r keeps its registered map for the registered row.
  - A label-aware twin (`rescore/map_f152r_la.py`) is applied as a sensitivity row. It uses the same tool and defaults
    (lam 1.5, neutral 0.5, own-label leave-one-out) and the same x bounds and per-line W. Its labels are `runs/A0a_f152r.tsv`
    (f152r excluded, overrides removed). At lam 0 it reproduces the registered f152r map, all 90 of 90 rows, and this is
    asserted on every run. The twin moves 05_026-028 back one token and merges 05_024+025 and 05_008+009 into 2:1 pairs, so 87
    tokens are mapped 1:1.
- **Can-vary, counted before scoring (`rescore/can_vary_la.json`).** A1 and A2 top-1 differ on **122 of 700** no.87 boxes
  (registered: 125 of 714) and on 19 of 87 f152r boxes on the twin map. A2 differs from the nulls on 628-686. The test is still
  real. The map change alters the atlas output at 147 (A1) and 143 (A2) no.87 tokens.

Commands (repo root):

    python3 benchmark-tx/txeng3/7/rescore/map_f152r_la.py [--check]   # f152r twin map; asserts lam 0 = registered map
    python3 benchmark-tx/txeng3/7/rescore/run_arms_la.py              # outputs, post-hoc labels/runs, can_vary_la.json (no truth)
    python3 benchmark-tx/txeng3/7/rescore/score_la.py                 # the only truth-reading step -> results_la.{json,tsv}
    python3 benchmark-tx/txeng3/7/rescore/diagnostics.py              # section 1 (truth-free)

## 3. Results, registered arms (`tools/tx_bench.py --exclude-flagged --paired`, as `score.py`; Wilson 95% as `score.py` computes it)

| target | output | before (registered map) | **after (corrected map)** |
|---|---|---|---|
| no.87 | line read of record (passC) | 0.051 (41/803) | same |
| no.87 | A0a cluster-name atlas (not gated) | 0.138 (111/803); vs A1 189 / 36 | 0.115 (92/803); vs A1 185 / 34 -- partly circular, see section 6 |
| no.87 | **A1 machine labels, atlas** | 0.343 (275/803) 0.310-0.376; fe 0.336 (266/792) | **0.314 (252/803) 0.283-0.347; fe 0.307 (243/792)** |
| no.87 | **A2 owner labels, atlas** | 0.329 (264/803) 0.297-0.362; fe 0.322 (255/792) | **0.300 (241/803) 0.269-0.333; fe 0.293 (232/792)** |
| no.87 | **A2 vs A1, paired** | 41 / 33, p 0.416; lines 13 / 7, p 0.26 | **41 / 33, p 0.416; lines 13 / 7, p 0.26** (fe 40 / 32, p 0.41) |
| no.87 | gain A1 - A2 | +0.014 | +0.014 |
| no.87 | A3 null (20 seeds) err / null-gain p95 | 0.726-0.793 / -0.391 | 0.719-0.791 / -0.407 |
| no.87 | A1 override vs line read | 0.066 (53/803), 0 fixed / 11 broken, p 0.001 | **0.051 (41/803), 0 / 0** (2 substitutions, both on excluded positions) |
| no.87 | A2 override vs line read | 0.080 (64/803), 0 / 22, p < 0.001 | **0.056 (45/803), 0 / 4, p 0.125** (7 substitutions: 4 on scored signs, all wrong; 3 on excluded positions) |
| f152r | registered map: A1 / A2 atlas, paired | 0.384 (28/73) / 0.356 (26/73); 4 / 3, p 1.0 | unchanged (this map is not the old no.87 file) |
| f152r | twin map (sensitivity): A1 / A2 atlas, paired | -- | 0.342 (25/73) / 0.315 (23/73); 4 / 3, p 1.0; gain +0.027; null p95 -0.438 |
| f152r | override, both maps | 0.069 (5/73), 0 / 0 | 0.069 (5/73), 0 / 0 |
| pooled P+S | A2 vs A1 | 45 / 36, p 0.37 | 45 / 36, p 0.37 (either f152r map) |

**Registered gate** (A2 <= A1 - 0.02 AND fixed > broken at p < 0.05 AND gain > null p95):
- no.87 on the corrected map: **FAIL** (gain +0.014, 41 / 33, p 0.42), as before.
- f152r on the registered map: **FAIL** (+0.027, 4 / 3, p 1.0), as before.
- f152r on the twin map: **FAIL** (+0.027, 4 / 3, p 1.0).

The identical 41 / 33 is a coincidence, checked position by position. Two fixed positions left the set (f178v L07.26, f179r
L02.15) and two entered it (f179r L01.23, L01.30). One broken position left (f179r L02.17) and one entered (f178v L11.20). Both
arms drop by the same 23 errors, so their difference is unchanged. 39 of the 41 fixed and 32 of the 33 broken positions are the
same under both maps: where one label set is right and the other wrong, the old map mostly had the box on the right token.

## 4. Conclusions, before -> after

| # | conclusion as registered (RESULTS.md) | after the map fix | changes? |
|---|---|---|---|
| 1 | Gate: the owner's labels do not transfer (no.87 41 / 33, f152r 4 / 3, both FAIL) | no.87 41 / 33, f152r 4 / 3, both FAIL | **No** |
| 2 | Both label sets beat a permuted null by about 0.4; "labelled tiles of the hand" carry the information | yes: mean null gain -0.44 on no.87, -0.48 / -0.51 on the f152r maps | No |
| 3 | The atlas route reads 0.33-0.38, five to seven times the line reads | 0.30-0.31 on no.87 (0.31-0.34 on the f152r twin), about five to six times the line reads | No (level about 0.03 lower) |
| 4 | Override "only breaks": A1 0 / 11, A2 0 / 22, "0 fixed / 33 broken pooled"; "every unanimous disagreement is wrong" | A1 0 / 0 (2 substitutions), A2 0 / 4 (7 substitutions, p 0.125). It still never fixes a sign. | **Yes, in size.** Of the 22 distinct broken positions, 18 were a placement artifact: a unanimous vote landed on the neighbouring token. It is still not an accuracy step: 0 fixes in either arm (9 substitutions in all). |
| 5 | Confusions: under the owner's labels a<-T60 8 -> 15 and o<-X_NEW 0 -> 12 | a<-T60 8 -> 15, o<-X_NEW 5 -> 13 | No in direction. The registered "0" was a top-5 cut-off: A1 already had 5 on the old map (`tx_bench --top 60`). |
| 6 | (second check) A2-vs-A1 override difference 0 / 11, p 0.001, is a unanimity artifact | A2 override 0 / 4 vs A1 0 / 0 | The ruling stands; the gap shrinks from 11 to 4 |

## 5. POST HOC, reported separately: the second check's X_NEW-l -> T19 ruling (owner_review_2026-10-04.tsv q2)

`rescore/labels/owner_xnewl_t19.tsv` is `labels/owner.tsv` with the owner's X_NEW-l boxes coded T19 instead of X_NEW. Seven
boxes change: f117r_03_008, f117r_05_024, f117r_07_015, f144r_04_030, f144r_05_009, f168r_03_003, f168r_03_015. The kNN uses
the same settings (`rescore/runs/A2x_*.tsv`), and A2x is paired against A1 on the same map.

| target | A2x (X_NEW-l = T19) | registered maps (reproduces the second check) | **corrected maps** |
|---|---|---|---|
| no.87 | err_true; vs A1 | 0.310 (249/803); A1 0.343; **45 / 23, p 0.010**; lines 15 / 6, p 0.078 | **0.281 (226/803) 0.251-0.314; A1 0.314; 45 / 22, p 0.0067; lines 15 / 6, p 0.078**; fe 44 / 21, p 0.006 |
| no.87 | gain; gate shape | +0.032 > null p95 -0.391: shape PASS | +0.032 > null p95 -0.407: shape PASS |
| no.87 | vs A2 (only the 7 boxes differ) | 14 / 0 | 15 / 0, p 0.0001 |
| no.87 | override vs line read | 0 / 28 | 0 / 4 |
| f152r | vs A1 | 0.342 (25/73); 4 / 2, p 0.69 | twin map 0.301 (22/73); 4 / 2, p 0.69 |
| pooled P+S | vs A1 | -- | 49 / 24, p 0.005 |

**Reading:** the second check's figure reproduces exactly, and the map fix does not weaken it (45 / 22 against 45 / 23). It
is still post hoc on an eval item, so it is not a PASS. It shows the registered null turns on one mis-specified 7-tile pile.

**New caveat, from section 1, that cuts the other way.** About half of what TXE3-7 counted as "the owner's decisions" (62 of
the 121 boxes where A1 and A2 differ) are consistent with repairing machine start labels that were attached one tile off on
five strips. So A2 - A1, and A2x - A1, measure his visual decisions plus the repair of a misjoined control. A gain over a
correctly attached machine control would be smaller than 45 / 22, by an amount not measured here.

## 6. Limits

- **The corrected map is label-steered.** Its labels are the atlas top-3 with no.87 held out, the sorter seed, and the
  owner's no.87 moves and statuses. All arms are placed identically, so the paired A2-vs-A1 comparison is fair. Its fixed and
  broken counts did not move.
- **A0a is partly circular.** A0a's absolute figures improve partly because the map placed boxes where the same family of
  cluster-name labels agrees with the line read, so A0a stays reported, not gated. The f152r twin's A0a figure (0.151) is
  fully circular, because the twin was steered by A0a's own labels: ignore it.
- **The steering labels are not strictly truth-blind at their source.** The BOXMAP-LA soundness check notes that 76 of the
  140 cluster names behind the allheld top-3 were set from clerk-verified no.87 tune tiles (joined through the old map). It
  found the per-tile override path changes no position: the allheld top-3 plus statuses alone give the same 700 positions.
  The cluster-name residue is not bounded here. It reaches the A2-vs-A1 comparison only through which box sits on which
  token, which is the same for both arms.
- **Fewer tokens are mapped.** no.87 maps 14 fewer tokens than before (700 vs 714). They keep the line read in every arm.
- **Not re-run.** The start-label shift (section 1) is reported, not corrected: correcting it changes the A1 control's
  definition, which is a new registered test, not this rescore.

## 7. Owner sentence (replaces the second check's, figures updated)

The pre-registered test, re-scored after a box-position fix, still found no measurable gain when a shape classifier carried
your 4 Oct Birago corrections to other letters (no.87: 41 signs fixed, 33 broken). With your own 4 Oct ruling that X_NEW-l
is the same sign as T19 applied after the fact, your labels came out ahead on no.87 (45 fixed, 22 broken). But about half of
the label changes the test credited to you repaired machine labels that had been attached one tile off on five strips, so the
question stays open until a corrected, pre-registered re-run. f.152r, the one letter you never sorted, is too small to show
anything but a large effect. Letting this classifier overwrite a line read fixed nothing. Most of the harm reported earlier
was the same position error: the real figure is 4 signs broken with your labels and 0 with the machine's. So do not let it
overwrite readings.

## Next step and cost

The corrected pre-registered re-run, as the second check proposed, with one addition. It would use:
1. the owner's q2 merge;
2. a machine control whose start labels are re-attached to the right tiles, or the five shifted strips dropped from both arms;
3. a null that keeps shape (the owner's number of changes placed on random boxes);
4. the corrected no.87 map and the f152r twin.

That is about USD 3, 30 min, Sonnet, disk only: the classify calls take 6 s each.
