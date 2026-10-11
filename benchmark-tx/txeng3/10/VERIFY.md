# VERIFY TXE3-10 PAIR (written 15:3x UTC 11 Oct 2026, by date -u)

Verifier: a subagent of the account-3 parent (session_0198Cv8ypBfBVfRToKVWx33M). It is not the solver session
(session_012YZasnTbPTJsYnd1X14g5f) and did not run the experiment. Inputs: committed files only, from a sparse
worktree at origin/main f3b81786. No model reading pass, no image or vision read, no network beyond git. No sorter
page, L74 oracle answer or frozen confirm item was opened. The experiment's own files were not changed.

## Method
1. Scorer: `tools/tx_bench.py` is unchanged since 6896cf0e (10 Oct 00:43 UTC), which is before the experiment. The
   truth and flags files are unchanged since 7d3f841e (9 Oct). Every committed output was scored with
   `--bench BENCHMARK-TX.tsv --item birago1572-no87 --exclude-flagged`. The eval-only and dev-only files also used
   `--coverage-diagnostic` (the fixed manifest would count the other split's lines as deleted). `--paired` was
   against `benchmark-tx/txeng/units/labels_{eval_heldout,dev_tune}.tsv`, or against `outputs/birago1572-no87/labels.tsv`
   for the whole item, which also used `--ci`.
2. Instrument: `glyph_atlas_pair.patch` was applied to `tools/glyph_atlas.py` at 1b50c66c in a scratch copy and its
   offline test passed. The pool inputs were taken from git at 1b50c66c: atlas signs.tsv, bitmaps.npz,
   no87_box_token.tsv, secure_tokens.tsv, sorter/no87/owner_map.tsv and owner-sort-2026-10-04/settled_labels.tsv.
   The run arguments are not committed anywhere, so they were rebuilt from the patch's `--help` and the PREREG:
   `classify --pair T18 T98 --out <atlas> --pool-dev units/labels_dev_tune.tsv --truth birago1572-no87.truth.tsv
   --pool-secure secure_tokens.tsv --pool-owner settled_labels.tsv --owner-map owner_map.tsv --map no87_box_token.tsv
   --exclude-pool-page f178r --exclude-pool-page f178v --exclude-pool-page f179r`. That base was then combined with
   (a) `--apply-unit units/labels_eval_heldout.tsv --shuffle-lolo 20`, (b) the same plus `--seed 1..5`, with and without
   `--force-t 0`, (c) `--apply-unit units/labels_dev_tune.tsv --loo-lines`, and (d) `--pair T90 T53` for (a) and (c).
   **All 31 committed instrument files came out byte-identical.** These are the g1/g2/apply/touched reports, the real
   and 10 control eval outputs, the dev output and the T90/T53 dev output.
   The patch still applies to origin/main's glyph_atlas.py, with offsets.

## Re-derivation (reported vs re-derived)
| quantity | reported (RESULTS.md) | re-derived | note |
|---|---|---|---|
| G1 LOGO acc, T18/T98 | 0.984 vs shuffled max 0.609 (chance 0.609) | 0.984 vs 0.609 (0.609) | byte-identical report; p <= 1/21 |
| G2 dev, T18/T98 | fixed 1, broken 0, both-wrong 1 | fixed 1 (L06.18), broken 0, both-wrong 1 (L10.31, truth c) | L is right at **17** of 19 dev pair positions. The PREREG says 18 and "ONE error"; broken is 0 either way |
| dev err as measured | 12/343 -> 11/343 | 12/343 -> 11/343 | tx_bench paired: fixed 1 broken 0 |
| dev err flagged excluded | 7/338 -> 6/338 | 7/338 -> 6/338 | |
| eval L as measured / flagged excl. | 0.040 (15/376) / 0.027 (10/371) | 15/376 / 10/371 | L's top confusion is d<-T98 x6 |
| eval X30 as measured / flagged excl. | 0.027 (10/376) / 0.013 (5/371) | 10/376 / 5/371 | |
| eval pair positions (registered statistic) | fixed 5, broken 0, exact p 0.0625 | fixed 5, broken 0, p 0.0625 (both masks) | 2 x 0.5^5 = 0.0625 |
| eval tx_bench headline under --paired (line level) | (not reported for eval) | 4 lines improved, 0 worse, p 0.125 | not the registered statistic |
| per position | 9 boxed T98: 6 d, 3 s; flipped 5 d; kept 3 s; missed L13.20 (m -0.98) | same | 10th T98 = f179r L03.2 (2:1 box), status excluded:unaligned, never scored |
| ctrl 1-5 (registered C1) | 0 changed, = L | 0 changed, = L | threshold rule disabled every permuted model |
| ctrl 1f..5f fixed/broken | 2/2, 2/1, 1/1, 1/2, 2/2 | same | err 0.040/0.037/0.040/0.043/0.040; flagged 0.027/0.024/0.027/0.030/0.027, same |
| whole item | 34/803 -> 29/803; 23/792 -> 18/792; bootstrap -0.013..-0.001; line p 0.125 | same | the same 5 eval flips, not independent evidence |
| whole-item d<-T98 | 7 -> 2: "L13.20 eval, and the dev pool's 1 is fixed; the remaining one is the un-boxed 2:1 position or outside the 1:1 map" | 7 -> 2: L13.20 (eval) and **f178v L06.18 (dev)** | **Attribution wrong.** passX30_topo_full.tsv carries only the 5 eval flips, so the dev error is still there. The 2:1 position is not scored |
| C2 T90/T53 G1 | 0.978 vs max 0.681 (chance 0.736) PASS | same | the features do separate p/t pool tiles |
| C2 T90/T53 G2 | fixed 0, broken 2 FAIL | fixed 0, broken 2 (dev 12/343 -> 14/343; flagged 7/338 -> 9/338) | both breaks are on one line (f178v L11, pos 26 T90->T53 truth p; pos 28 T53->T90 truth t). The one dev error (L05.4) is truth-flagged alignment-doubtful |
| cost | -- | USD 10.77 (parent's get_session fill, 967feff2) vs cap 15 | under cap. Box 05:47-06:06 of 2 h |

## Pre-registration order
- ROOM claim 05:55. PREREG committed in b8780673 at 05:57:04 UTC (a room.py "update" commit). Real and control eval
  outputs, dev gates and the patch were committed in 1b50c66c at 06:03:35 ("unscored"). RESULTS, the PREREG addendum
  and the LEDGER row were committed in 00746d35 at 06:06:38. So the PREREG came before every committed output.
- That the outputs went in before tx_bench ran is the worker's statement; git cannot show when a scorer ran. The
  byte-identical re-run shows the committed outputs are exactly what the committed instrument gives on the registered
  pool. Nothing in it depends on eval truth: t = 0.0 comes from pool LOGO, lambda 1 was registered, and the tool refuses
  an apply unit that shares lines with --pool-dev.
- Declared deviations (addendum): C1f was added; the tool change stays as a patch; C2 was not applied to eval. The
  addendum text was committed only after the eval outputs. The C1f outputs it describes were already in the 06:03 commit.
- Undeclared deviations (none changes the verdict):
  (a) A 29th feature, "skeleton length / ink" (`sk.sum()/ink`), is not in the PREREG's feature list, which gives 28.
      RESULTS lists it without calling it a deviation.
  (b) The pool is T18 25 / T98 39, not the registered 26 / 39. RESULTS says "after de-duplication"; the addendum does
      not.
  (c) The PREREG miscounts the dev errors: 2 errors and 17 correct, not 1 and 18.

## Gate
Registered: 'Verdict "helps" iff net > 0 and p < 0.05 (6-0 or better at this N); otherwise "weak for this pair at this N".'
Dev gates G1 (0.984 > 0.609) and G2 (broken 0) PASS as registered. At eval, net +5 and exact two-sided sign p = 0.0625
give **"weak for this pair at this N"**, and the reported verdict follows. Only a perfect 6/6 with none broken could
pass, because the boxed eval positions hold exactly six d<-T98 errors. The PREREG said so ("6-0 or better").
For context only, not a re-gate: 6 of the 9 positions are truth d. So "flip every T98" would score 6 fixed / 3 broken,
net +3. The chance that 5 random flips among 6 d / 3 s all land on d is 6/126 = 0.048. Every way of reading this
evidence puts it at the 0.05 line.

## Control (rule 3)
- **C1 as registered** (shuffled labels through the full pipeline) **could not vary** on fixed/broken. The threshold rule
  disabled every permuted model, so each output equals L at the pair positions. That makes it a non-test. The worker
  caught this and declared it.
- **C1f** (declared addition: the same permuted models applied with `--force-t 0`) **can vary, and did**: 2-4 changed,
  1-2 fixed, 1-2 broken, net -1..+1 per seed, 8 fixed / 8 broken over 16 flips in all. The real model's own threshold
  was also t = 0.0, so the control matches it on threshold. Real +5 vs control max +1 over 5 seeds is consistent with a
  real cue. N is still 9 positions.
- C2 (p/t) is a generalisation test, not a control for the d/s claim. G1 passed; G2 failed on 2 positions of one dev
  line. It was never applied to eval.

## Split
Tune on dev, report on eval, as registered. Secure and owner tiles from f178r/f178v/f179r are excluded. Dev tiles come
from dev_tune lines only, and truth is read only for those lines. There was one eval look. No eval-derived parameter
exists in the instrument (see above).
One forward note: 2 of the 23 secure T18/T98 tiles in the pool are on f152r, which is benchmark item birago1572-f152r
(split eval, 73 scored). The RESULTS next step ("another known-answer leaf of the same hand") must add
`--exclude-pool-page f152r` if that leaf is used, or the re-test trains on its own test leaf.

## Claims told to the owner
| # | claim | verdict | evidence | corrected sentence |
|---|---|---|---|---|
| 1 | A small d/s classifier fixed 5 of the 6 remaining d-read-as-s errors and broke nothing. | **holds** (scope note) | Re-derived exactly: 5 fixed / 0 broken at the 9 boxed eval positions (6 d, 3 s), and 0 of 17 correct dev positions broken. On the held-out lines "broke nothing" rests on 3 correct s reads, plus 17 on dev. | "On the held-out lines of Birago no.87, a small d/s classifier fixed 5 of the 6 d-read-as-s errors and changed none of the 3 correct s reads (none of 17 correct reads broken on the tuning lines either)." |
| 2 | It missed its pre-set statistical bar by one sign (p 0.0625 vs 0.05), so it is logged as weak, not adopted. | **holds** | Registered rule "helps iff net > 0 and p < 0.05", and 5-0 gives p 0.0625, so the verdict is "weak for this pair at this N". Only a perfect 6/6 could pass. Logged in RESULTS.md and LEDGER.md. The patch is not landed, and there is no tool_shelf.tsv or TRANSCRIPTION.md row yet. | "It was one fix short of its pre-set bar (it needed all 6 of 6; p 0.0625 vs 0.05), so it is logged as weak and not adopted." |
| 3 | It only works for that one pair (did not transfer to p/t). | **overstated** | Only one other pair (p/t) was tried, and only on the tuning lines. Its features did separate p/t tiles in the pool test (0.978 vs shuffled max 0.681), but applied to no.87 it broke 2 correct reads, both on one line, and fixed none. It was never tried on the held-out lines, and no other pair was tried. "Works" for d/s is itself "weak", not adopted. | "Tried on one other look-alike pair (p/t), it broke 2 correct reads on the tuning lines and fixed none, so it was not used there; no other pair has been tried." |

## Rule issues and objections
1. RESULTS.md line 45-46 misattributes the second remaining whole-item d<-T98. It is the dev error f178v L06.18, which
   G2 fixed but `passX30_topo_full.tsv` does not carry. It is not the 2:1 position, which is excluded:unaligned and
   never scored.
2. Rule 7: the run arguments are not committed. The outputs reproduce only after the arguments are rebuilt (Method 2
   above). A `run.sh` beside the patch would close this.
3. Undeclared PREREG deviations (a)-(c) above: an extra feature, a pool count of 25 not 26, and a dev error miscount.
   They are minor and none changes a gate.
4. The registered C1 could not vary on its statistic. This was caught and declared; C1f is the usable control.
5. The gate could be passed only by a perfect score (6/6). The PREREG named this. The LEDGER lesson ("size the gate to the
   error count") is right. `tools/tx_power.py` exists for this and is not cited.
6. RESULTS' explanation of the p/t failure ("the loop-position cue ... has no analogue for p vs t") is an
   interpretation. The pool test separated p/t at 0.978. The failure is 2 positions on one dev line, which may be about
   those tiles or the box map there, not shown either way.
7. TRANSCRIPTION.md: RESULTS quotes the flagged-excluded figures beside the as-measured ones, never alone. The owner
   claims quote neither. No novelty wording. Cost 10.77 is under the USD 15 cap.
8. Forward: exclude f152r from the pool before any re-test on birago1572-f152r (see Split).

## Safe sentence for the owner
On the held-out lines of Birago no.87, a small d/s classifier corrected 5 of the 6 d-read-as-s errors and changed none
of the 3 correct s reads. That is one fix short of the bar set beforehand, which only a perfect 6 of 6 could meet
(p 0.0625 vs 0.05), so it is logged as weak, not adopted. On the one other pair tried (p/t), it broke 2 correct reads on
the tuning lines, so it was not used there.

## Second check (11 Oct 2026, written 16:28 UTC by date -u, by the account-3 parent from the second verifier's report; workflow wf_35ed2244-0e6)

A second, independent agent ruled on each objection and non-holds verdict above, re-running the commands itself. Where it disagrees with this file, this section governs.

### Rulings on the first verifier's objections

- **agree**: RESULTS.md:45-46 names the wrong position as the second remaining whole-item d<-T98. It is dev f178v L06.18; the 2:1 position f179r L03.2 is never scored.
  - Evidence: I diffed passX30_topo_full.tsv against labels.tsv and it changes only the 5 eval positions (L15.9, L19.6, L19.24, L21.1, L23.21). f178v_L06 pos 18 still reads T98, and its truth is T18|T63 = d, scored, unflagged. f179r_L03 pos 2 has empty truth and status excluded:unaligned, so it can never be a d<-T98. tx_bench (whole item, --exclude-flagged) prints top confusion d<-T98 x7 for L and x2 for X30_full. The two are L13.20 (eval) and L06.18 (dev). RESULTS' 'the dev pool's 1 is fixed' is true only of the separate G2 dev output (passX30_topo_dev_tune.tsv), not of the whole-item file.
- **partly**: Rule 7: no run script or command lines are committed in benchmark-tx/txeng3/10/; the arguments had to be rebuilt to get byte-identical outputs.
  - Evidence: The facts are right. git grep for '--exclude-pool-page' or '--pool-secure' on origin/main finds them only in VERIFY.md and the patch. RESULTS, the LEDGER row, the ROOM lines and the commit messages carry no command lines either. I rebuilt the args, applied the patch to glyph_atlas.py at 1b50c66c (its offline test prints ok) and got byte-identical output for 30 committed files I compared: the eval output, touched and report files; all 10 control outputs with their touched and report files; dev and p/t dev outputs with their touched and g2 files; g1 for both pairs. Three caveats. (1) Rule 7 as written governs claimed plaintext readings, so this is the reproducibility spirit, not a literal breach. (2) VERIFY.md's own recipe is slightly off. Recipe (a) (--apply-unit eval with --shuffle-lolo 20) reproduces g1_T18_T98.tsv, but not apply_T18_T98_eval.tsv, whose shuffled column is empty; that file needs a run without --shuffle-lolo. g1_T90_T53.tsv can be made with no eval apply at all, given a dummy --tsv. (3) The three --exclude-pool-page flags change nothing: both pools are identical without them (T18/T98 25/39, T90/T53 24/67). So byte-identity cannot show the worker passed them, but it does show no eval-leaf tile could enter.
- **agree**: Undeclared PREREG deviation: topo_feats appends sk.sum()/ink as a 29th feature; the PREREG lists 28.
  - Evidence: Patch lines 99-100 return the 16 grid values, then [n_h, cy, area, above, below, ep.sum(), jn.sum(), (ey<top).sum(), (ey>bot).sum(), sk.sum()/ink], then 3 geometry values: 29 in all, and the docstring says '(29)'. PREREG lines 38-41 enumerate 16+3+4+2+3 = 28. RESULTS names 'skeleton length / ink' and '(29 features)' but never calls it a deviation, and the addendum does not mention it. It does not change a gate (not tested by ablation).
- **agree**: Pool T18 is 25, not the registered 26, and the dev lines hold 2 errors / 17 correct reads, not 1 / 18; neither is declared in the addendum.
  - Evidence: Pool by source, from the patch's own pair_pool: dev 12/6, secure 5/18, owner 8/15, so 25/39. The missing owner T18 is box f144r_05_026, which is also a secure S T18 token, so it was de-duplicated with the same label and no conflict. RESULTS says 'after de-duplication' and the addendum is silent. Dev: of the 19 L pair positions, L06.18 is T98 with truth d, and L10.31 is T98 with truth c (T36|T50), scored and unflagged. So L is right at 17, and the PREREG's 'ONE error' and '18 correct' (lines 6, 25, 52) are wrong. The PREREG's own dev pool count (T98 6 = 8 - 2) already implied two non-s reads. G2's 'broken 0' holds either way.
- **agree**: The registered C1 control could not vary (the threshold rule disables every permuted model); C1f was added after the dev gates, and its addendum text was committed only with RESULTS at 06:06, after the 06:03 eval outputs, which already included the C1f outputs.
  - Evidence: The ctrl1-5 reports show enabled 0 (ctrl1 lolo_acc 0.391), and every ctrl1-5 output equals L under tx_bench (0 lines changed). The shuffled LOGO accuracies max out at 0.609, far below the 0.95 decided-accuracy rule, so in practice C1 could not flip anything. Commit times (committer): PREREG b8780673 at 05:57:04; ctrl1f-5f outputs in 1b50c66c at 06:03:35; PREREG addendum (+9 lines) in 00746d35 at 06:06:38. C1f can vary and did. tx_bench shows ctrl1f 2 fixed/2 broken, 2f 2/1, 3f 1/1, 4f 1/2, 5f 2/2, i.e. 8 fixed and 8 broken over 16 flips. The real model also ran at t 0.0, so the threshold matches. The timing is a disclosure point only: the C1f outputs predate RESULTS.
- **agree**: RESULTS.md:55-57's mechanism for the p/t failure ('the loop-position cue has no analogue for p vs t') is not supported; the p/t pool test passed at 0.978 and the failure is 2 positions on one dev line.
  - Evidence: g1_T90_T53.tsv shows LOGO 0.978 against a shuffled max of 0.681 and a majority-class chance of 0.736, so the same features do separate p/t pool tiles. No feature ablation was run, so nothing isolates the loop cue. The G2 breaks are only f178v L11 pos 26 (T90->T53, margin 0.965) and pos 28 (T53->T90, margin 0.216, a marginal call). The box map at L11 is 1:1 there with matching signs, so a box-map fault is not shown either. The mechanism is an untested interpretation.
- **agree**: Forward risk: 2 of the 23 secure T18/T98 pool tiles are on f152r, which is benchmark item birago1572-f152r (split eval); any re-test on that leaf must add --exclude-pool-page f152r.
  - Evidence: secure_tokens.tsv has f152r_03_011 and f152r_03_026, both T98 grade S (passage L02), and both are in the 23-tile secure pool (5 T18 + 18 T98). BENCHMARK-TX.tsv lists birago1572-f152r with lines f152r_L01-04, split eval, 73 scored, same hand. It does not touch the no.87 result, so it is correctly framed as a forward risk.
- **agree**: The gate was reachable only by a perfect 6/6; tools/tx_power.py, meant for sizing such a gate before registration, was not used.
  - Evidence: tx_power.py was added in b8d08264 (9 Oct 15:13 UTC), before the PREREG, and the PREREG does not cite it (TXE3-8's PREREG does). With 9 positions and 6 errors, only 6-0 gives p < 0.05: 6-0 is p 0.031 and 6-1 is p 0.125. I ran tx_power --errors 6 --n 9 --alpha 0.05 --draws 2000. A clean fixer that fixes 80% of errors passes in 0.325 of draws, and only a perfect fixer passes reliably. No rule requires the tool, and the PREREG named the 6-0 requirement in words. So this is a process note that changes no claim.

### Final verdict on each claim told to the owner (11 Oct ~07:05 UTC)

- **holds**: A small d/s classifier fixed 5 of the 6 remaining d-read-as-s errors and broke nothing.
  - Evidence: I re-ran it from the committed patch and the outputs were byte-identical. tx_bench, eval versus L: as measured 15/376 -> 10/376; flagged excluded 10/371 -> 5/371; position-level fixed 5, broken 0. The 9 boxed eval T98 reads are 6 truth d and 3 truth s. It flipped 5 d (L15.9, L19.6, L19.24, L21.1, L23.21), kept all 3 s, and missed L13.20 (margin -0.982). Nothing else changed. On the tuning lines, run leave-one-line-out, it broke 0 of 17 correct reads, fixed L06.18, and moved L10.31 from one wrong value to another (truth c). The '6' is the held-out count; the whole letter has 7, the 7th on the tuning lines.
  - Corrected: On the held-out lines of Birago no.87, a small d/s classifier fixed 5 of the 6 d-read-as-s errors and changed none of the 3 correct s reads (and broke none of 17 correct reads on the tuning lines).
- **holds**: It missed its pre-set statistical bar by one sign (p 0.0625 vs 0.05), so it is logged as weak, not adopted.
  - Evidence: Registered rule: 'helps iff net > 0 and p < 0.05'. 5-0 gives two-sided exact p 0.0625; 6-0 would give 0.031. The verdict 'weak for this pair at this N' is in RESULTS.md and in the LEDGER row (cost 10.77). The patch is not landed in tools/glyph_atlas.py. Only a perfect 6/6 could pass; at that size tx_power gives an 80%-effective clean fixer a 0.325 pass rate.
  - Corrected: It was one fix short of its pre-set bar (it needed all 6 of 6; p 0.0625 vs 0.05), so it is logged as weak and not adopted.
- **overstated**: It only works for that one pair (did not transfer to p/t).
  - Evidence: Only one other pair, p/t (T90/T53), was tried, and only on the tuning lines. Its pool test passed (0.978 vs shuffled max 0.681), so the features do carry p/t information. Applied to no.87's tuning lines, it broke 2 correct reads on one line (f178v L11 pos 26, margin 0.965; pos 28, margin 0.216) and fixed none, and dev error went 12/343 -> 14/343. It was never applied to the held-out lines, and no other pair was tried. 'Works' for d/s is itself 'weak, not adopted'.
  - Corrected: Tried on one other look-alike pair (p/t), it broke 2 correct reads on the tuning lines and fixed none, so it was not used there; no other pair has been tried.

### Sentence the parent may give the owner

On the held-out lines of Birago no.87, a small d/s classifier corrected 5 of the 6 d-read-as-s errors and changed none of the 3 correct s reads (and broke none of 17 correct reads on the tuning lines). That was one fix short of a bar set beforehand that only a perfect 6 of 6 could meet (p 0.0625 vs 0.05), so it is logged as weak, not adopted. On the one other pair tried (p/t), it broke 2 correct reads on the tuning lines and was not used there.
