# PREREG txeng3-10 (TXE3-10 PAIR, account 3; Fable; written 05:5x UTC 11 Oct 2026 by date -u, before any score)

Target: the d look-alike pair T18 (d) / T98 (s) on held-out Birago no.87. Reconciled output (passC) and L
(reconciled + NO87-LABELS, `benchmark-tx/outputs/birago1572-no87/labels.tsv`) both read T98 at 10 eval_heldout
positions and T18 at 0; ERRORMAP-2026-10-09 counts 6 eval d <- T98 errors in that pool (a published count, not a
position). On dev_tune L reads the pair at 19 positions (T18 11, T98 8) with ONE error (one T98 read whose truth is d).

Nearest priors (read before this was written): X2 / TXE2-PAIR (`tools/tx_pair_clf.py`: zones + raw 32x32 + HOG,
logistic regression, trained on S-grade secure tiles of other leaves; dev 1 fixed / 11 broken) and X2b / TXE2-PAIR2
(same features, trained leave-one-line-out on no.87's own dev_tune tiles; dev 3 fixed / 0 broken, p 0.25, "the gate
is not reachable at this N ... what would settle it is more labelled tiles, not a looser threshold"). Also
lookalike_pass (retired for this pair), TX-SHEET (d<-T98 7 -> 2 but s<-T50 up), the mark rule and the crossword
(retired). What is different here (rule 3's third-attempt clause): (1) the features are topological, not pixel
or gradient -- loop (hole) presence and its vertical position in the box, stroke endpoints from a skeleton and where
they sit relative to the loop, ink mass above and below the loop, a 4x4 ink grid, and the box geometry (rh, rw, dy);
on the dev-only sheet T18 is a loop ON TOP of a stem and T98 a loop in the MIDDLE of a stem that passes through it,
and the pool's geometry already splits (rh 1.35+-0.10 vs 1.85+-0.25, dy 0.32+-0.09 vs -0.03+-0.17); (2) the training
pool unions every non-eval labelled source instead of one: dev_tune truth tiles, the family's S-grade secure tiles,
and the owner's 4 Oct 2026 sort on f.117/f.144r/f.168 mapped to atlas boxes (X2 used secure only, X2b dev only);
(3) one pair, applied only at L's T18/T98 positions. If this fails its gates it is logged weak for the pair and the
next attempt needs new material (another known-answer leaf of this hand), not a fourth feature set.

## Hypothesis
A loop-position / stem-endpoint discriminator trained on the pooled non-eval tiles separates T18 from T98 better than
chance (LOGO accuracy above every shuffled-label run), does not break the 18 correct dev positions, and on eval fixes
more of L's T98 reads than it breaks.

## Training pool (fixed; never an eval-line tile, never no.87 truth outside dev_tune lines)
- dev_tune positions with a 1:1 box in `atlas/no87_box_token.tsv` whose L sign is T18 or T98, labelled by which member
  the truth homophone set contains (both or neither -> excluded): T18 12 (11 + the one T98-read d), T98 6.
- `atlas/secure_tokens.tsv` grade S, page not in {f178r, f178v, f179r}: T18 5, T98 18.
- `sorter/owner-sort-2026-10-04/settled_labels.tsv` new_sign in the pair, mapped by `sorter/no87/owner_map.tsv`
  (box non-empty, dup 0, dist_px <= 10): T18 9, T98 15 (f.117, f.144r, f.168 only; the owner's no.87 sort covers
  other families, so no no.87 tile enters through the owner route).
Pool: T18 26, T98 39. Groups for leave-one-group-out (LOGO): dev tiles by line, other tiles by page.

## Instrument (built as `tools/glyph_atlas.py classify --pair A B`, pure numpy + PIL; offline test in tools/tests)
Features per tile (48x48 atlas bitmap, ink high; cropped to the ink box, resized 32x32): 4x4 ink grid (16); holes:
count, largest-hole centroid y (0 top .. 1 bottom of the box), hole area share; skeleton (Zhang-Suen): endpoints,
junctions, endpoints above the hole top and below the hole bottom; ink share above the hole top and below the hole
bottom; box geometry rh, rw, dy from signs.tsv. Standardised. Model: L2 logistic regression (lambda 1, class-balanced,
Newton steps), class 1 = B of --pair A B. Margin at an applied position: m = p(partner of L) - p(L).
Threshold t: LOGO over the pool gives every pool tile a held-out p; for t in {0, 0.1, ..., 0.9} the decided tiles are
|2p-1| > t; t = the smallest value whose decided-tile accuracy >= 0.95 with coverage >= 50% of the pool; none -> the
pair is disabled (no flips). Apply: flip L's sign to the partner iff m > t; a position with no 1:1 box keeps L.
No neighbour-sign feature (kept out: N is too small to add a second feature family).

## Dev gate (both, else "weak for this pair", and NO eval look)
G1 LOGO accuracy at t = 0 of the real labels exceeds the maximum of 20 shuffled-label LOGO accuracies (labels permuted
   within the pool, seeds 1..20; permutation p <= 1/21).
G2 Applied to the 19 dev_tune pair positions, each under the model whose pool EXCLUDES that position's own line
   (the dev tile's own truth never trains the model that votes on it): broken = 0 of the 18 correct positions; the one
   error is reported fixed or kept (one position cannot carry a gate).

## Eval look (one, only after G1 and G2; outputs committed BEFORE tx_bench runs)
Output `benchmark-tx/outputs/birago1572-no87/passX30_topo_eval_heldout.tsv` = L_eval_heldout with the flips; the
eval position whose box op is 2:1 keeps L. Endpoint: paired vs `benchmark-tx/txeng/units/labels_eval_heldout.tsv`,
fixed / broken / net at the 10 pair positions, two-sided sign test p; err_true as measured AND flagged-excluded with
Wilson 95% for L and the output (tx_bench, `--exclude-flagged`, item birago1572-no87, eval_heldout lines). Verdict
"helps" iff net > 0 and p < 0.05 (6-0 or better at this N); otherwise "weak for this pair at this N". The pair's
reach is at most the 6 counted errors of 803 signs, inside L's own Wilson interval, so the paired count is the
endpoint and the whole-item err_true is reported beside it, never as the gate.

## Controls (rule 3; each can differ from the target on the statistic)
C1 Shuffled labels: the identical pipeline (pool, features, LOGO threshold, apply) with labels permuted within the
   pool, seeds 1-5, applied to the same eval positions; fixed / broken per seed. Must not pass the "helps" rule.
   It can vary: a permuted model flips different tiles, so its fixed/broken counts are free to differ.
C2 Generalisation: pair T90 (p) / T53 (t), the next-largest confusion (t <- T90 x3 reconciled), same pool rules
   (dev T53 13 incl. one T90-read t, T90 9; secure T53 43, T90 8; owner T53 12, T90 9), same gates G1/G2 on dev
   (dev has 22 pair positions, 1 error); if G1 and G2 pass, applied to eval's 27 1:1 T90/T53 positions, fixed /
   broken reported. Expected mostly "does not break" (ERRORMAP lists no eval t<-T90 among the top rows).

## Stop rule
Cap USD 15 and 2 h (box 05:47-07:47 UTC, 80% line 07:23); one eval look; no re-tuning after it; no second feature
set. Dev gate fail -> weak, no eval look, RESULTS.md says so. Never touches BENCHMARK-TX truth, the frozen confirm
items, or the oracle pages.

## Addendum (06:0x UTC 11 Oct 2026, written after the dev gates and before any eval score; see RESULTS.md)
1. The registered shuffled-label control (C1) is disabled by the pipeline's own threshold rule for every seed (no permuted
   model reaches 0.95 decided accuracy), so it flips nothing and cannot vary on fixed/broken. To give rule 3 a control that
   can differ from the target on that statistic, a declared secondary control was added: the same permuted models applied
   at argmax (`--force-t 0`), seeds 1-5, outputs `passX30_topo_ctrl{1..5}f_eval_heldout.tsv`. Both forms are reported.
2. The tool change is kept as `benchmark-tx/txeng3/10/glyph_atlas_pair.patch` (with its offline test), not landed in
   tools/glyph_atlas.py: TXE3-5 (f3e32015) and TXE3-7 (5552b57e) committed to the same file within the hour (brief rule).
3. C2 (T90/T53) failed G2 on dev (0 fixed, 2 broken) and was therefore not applied to eval, as registered.
