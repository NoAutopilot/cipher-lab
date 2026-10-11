# TXE3-10 PAIR results (account 3, Fable; 05:47-06:1x UTC 11 Oct 2026 by date -u)

PREREG `benchmark-tx/PREREG-txeng3-10.md` (committed b8780673 before any score; eval outputs committed 1b50c66c at
06:03 UTC before tx_bench ran). Instrument: a one-pair topology discriminator for T18 (d) / T98 (s), `glyph_atlas.py
classify --pair A B`, kept as `glyph_atlas_pair.patch` in this folder (two TXE3 siblings, TXE3-5 and TXE3-7, committed to
tools/glyph_atlas.py within the hour, so the brief's rule applies: patch in own folder, named in ROOM; the patch
carries the tool change and its offline test `tools/tests/test_glyph_atlas_pair.py`, applies cleanly to origin at
1b50c66c, test passes). Pure numpy + PIL; no reader, no vision call, no network; the apply step never reads a truth file.

## What was built
Features per 48x48 atlas tile: 4x4 ink grid; loop (hole) count, largest-hole centroid y, hole area; ink share above the
hole top and below the hole bottom; Zhang-Suen skeleton endpoints and junctions, endpoints above/below the loop,
skeleton length / ink; box geometry rh rw dy (29 features). L2 logistic regression (lambda 1, class-balanced, Newton).
Threshold t by leave-one-group-out (LOGO) on the pool: smallest t with decided accuracy >= 0.95 at coverage >= 50%.
Pool (never an eval-line tile): dev_tune truth tiles 12/6, S-grade secure tiles of other leaves 5/18, the owner's
4 Oct 2026 sort on f.117/f.144r/f.168 mapped to atlas boxes 9/15 -> T18 25, T98 39 after de-duplication (22 groups).

## Dev gates (both pre-registered; both PASS for T18/T98)
| gate | T18/T98 | T90/T53 (control C2) |
|---|---|---|
| G1 LOGO accuracy at t=0 vs 20 shuffled-label LOGO runs | 0.984 vs max 0.609 (chance 0.609) PASS | 0.978 vs max 0.681 (chance 0.736) PASS |
| G2 dev_tune, each line voted by a pool excluding that line (19 / 22 pair positions) | fixed 1 (f178v L06.18 T98->T18, truth d), broken 0, both-wrong 1 (L10.31 T98->T18, truth c) PASS | fixed 0, broken 2 (L11.26 T90->T53 truth p; L11.28 T53->T90 truth t) FAIL |
| dev accepted-token error (343 scored, `--exclude-flagged` 338) | 12/343 0.035 (0.020-0.060) -> 11/343 0.032 (0.018-0.057); flagged-excluded 7/338 0.021 -> 6/338 0.018 | not applied to eval (gate) |

## Eval look (one; `passX30_topo_eval_heldout.tsv` vs L = `txeng/units/labels_eval_heldout.tsv`, 376 scored / 371 flagged-excluded)
| output | pair positions considered | changed | fixed | broken | exact sign p | eval err as measured (Wilson 95%) | flagged excluded (95%) |
|---|---|---|---|---|---|---|---|
| L (base) | | | | | | 0.040 (15/376) 0.024-0.065 | 0.027 (10/371) 0.015-0.049 |
| **X30 real** | 9 (the 10th T98 has a 2:1 box, kept) | 5 | **5** | **0** | **0.0625** | **0.027 (10/376) 0.015-0.048** | **0.013 (5/371) 0.006-0.031** |
| ctrl 1-5 shuffled labels, pipeline as registered | 0 (threshold rule disables every permuted model) | 0 | 0 | 0 | 1.0 | = L | = L |
| ctrl 1f shuffled, `--force-t 0` (declared addition, see PREREG addendum) | 9 | 4 | 2 | 2 | 1.0 | 0.040 | 0.027 |
| ctrl 2f | 9 | 3 | 2 | 1 | 1.0 | 0.037 | 0.024 |
| ctrl 3f | 9 | 2 | 1 | 1 | 1.0 | 0.040 | 0.027 |
| ctrl 4f | 9 | 3 | 1 | 2 | 1.0 | 0.043 | 0.030 |
| ctrl 5f | 9 | 4 | 2 | 2 | 1.0 | 0.040 | 0.027 |

Per position (truth read only after the committed look): of the 9 boxed eval T98 reads, 6 are truth d and 3 truth s. The
real discriminator flipped exactly 5 of the 6 d (f178v L15.9, L19.6, L19.24, L21.1, L23.21; margins 0.92-0.99), kept all
3 s (margins -0.98 to -1.00), and missed one d (L13.20, margin -0.98, a confident miss). Pair-level wrong on the boxed eval
positions: 6/9 -> 1/9.

Whole item (L with the 5 eval flips, `passX30_topo_full.tsv`, 803 scored): as measured 0.042 (34/803, 0.030-0.059) -> 0.036
(29/803, 0.025-0.051); flagged excluded 0.029 (23/792, 0.019-0.043) -> 0.023 (18/792, 0.014-0.036); paired line bootstrap
95% of the error difference -0.013..-0.001 (excludes 0); line sign test p 0.125 (4 lines improved, 0 worsened).
d <- T98 on the whole item: 7 (reconciled) / 7 (L) -> 2 (L13.20 eval, and the dev pool's 1 is fixed; the remaining one is
the un-boxed 2:1 position or outside the 1:1 map).

## Verdict (by the registered gate)
"Weak for this pair at this N": the registered rule was net > 0 AND exact sign p < 0.05, and 5 fixed / 0 broken gives
p = 0.0625 (a sixth flip was needed on a pool with six errors). Beside the gate, every number moved the right way: no break
on dev or eval, every shuffled control at net <= +1 against the real +5, the paired bootstrap of the whole-item difference
excludes zero, and the one miss is a confident wrong margin, not a borderline. This is not a refutation and not a pass; it
is a dev-and-eval result in the right direction one position short of its own gate, the X2b shape with twice the moves.

Generalisation control C2 (T90/T53, p/t): FAIL at G2 -- the same features break two correct dev positions and fix none;
the loop-position cue that separates d from s has no analogue for p vs t, so the instrument is pair-specific, not a general
look-alike fixer. Not applied to eval.

## For the owner (three sentences)
The d/s pair that was the biggest single source of error on no.87 can be told apart by where the loop sits on the stem,
and a small classifier using that cue, trained on your 4 October sort plus the secure and dev tiles, corrected five of
the six remaining d-read-as-s errors on the held-out lines without breaking anything. It missed the pre-registered
statistical bar by one position (p 0.0625, where 0.05 was needed), so it is logged as weak, not adopted, even though
every control and every direction is right. It does not transfer to the p/t pair, so it is a fix for this one confusion,
not a general tool.

## Next step and cost
One more known-answer leaf of the same hand (another Birago 1572 letter with a clerk sheet or gloss, or the no.87 2:1
position re-cut to a 1:1 box) would add the handful of T18/T98 positions the gate needs; re-running this exact instrument
on it is about USD 2 (read-free: pool build + apply + tx_bench), and is a legitimate second application, not a re-tune.
If the parent adopts the patch into tools/glyph_atlas.py it lands as one option with its test (449-line patch, applies
cleanly at 1b50c66c). Also for the parent: TRANSCRIPTION.md "Today" column and the TXE table should carry the X30 rows
(this worker does not edit the shared standard).

## Rules kept
Tune on dev, report on eval; outputs committed before scoring (1b50c66c 06:03 UTC); truth read for dev lines by the pool
step only, and for eval only by tx_bench after the commit; no frozen confirm item touched; no oracle page touched; no
reader or network call; BENCHMARK-TX truth unchanged. Date error caught and corrected: the first PREREG draft and ROOM
claim carried an estimated "06:1x" before `date -u` read 05:55; both were corrected before the push.
Cost: parent reads get_session (no figure visible to the worker); wall clock 05:47-06:1x UTC of a 2 h box.
