# PREREG TXE4-3 ATLAS-NCA (account 3, Fable 5.1 worker session_01MfBjefFUCgpwKvfagrojGC; written 12 Oct 2026 01:2x UTC by date -u, pushed BEFORE any read, map or score)

One of the TXE4 experiments (account-3 parent, brief `.claude/briefs/runs/2026-10-11-acct3-txe4-3.md`, commit 93b7bb32).
Work folder `benchmark-tx/txeng4/3/`. Read-free: no reader, no vision call, no network. Cap USD 15, box 01:20-03:20 UTC
(unit-start limit 02:56 UTC). TXE4-0 REPAIR landed (6f84c5af, units 1-4); its optional unit 5 did NOT land, so the
machine-label steps 1-3 below are run here.

## Hypothesis
A family atlas of the Birago 1572 signs can be NAMED with no known answer and no owner sort: a kNN whose only voters are
sibling-leaf tiles labelled by the two blind machine readers' agreement (A/B agree, same id, neither conf L), joined to
their atlas boxes by the label-aware aligner under TXE4-0's join gate, and whose distance is LEARNED (NCA) on those same
tiles, reads no.87's held-out lines (a) better than the same tiles under today's unlearned HOG+PCA40 distance (A1) and
(b) no worse than the known-answer-named atlas (A0, 0.162). The permuted-label null (A3) bounds chance.

## Nearest prior (register rows) and what differs from them
- PREREG-txeng3-7 (TXE3-7 PROPAGATE, 11 Oct 2026; rescored on the label-aware map a4ccb93d1): a kNN from 445 owner-sorted
  tiles (A2) read about the same as one from the machine start labels (A1): no.87 0.300 vs 0.314, f152r 0.315 vs 0.342,
  both far behind the cluster-name atlas A0a 0.115. Those start labels were attached one tile off on five strips, so
  "label quality was not the limit" is withdrawn. Differs here: the labels are the sibling readers' AGREEMENT on nine
  leaves (about 1,100 tokens, not 445), joined by box_token_align with a join_check verdict per leaf (never an index or
  width-only join), and the distance is learned; features are a dev-chosen set, not only HOG+PCA40.
- X15 (atlas features; register verdict non-test: "not run: superseded by X3's step 1, the chooser not coverage is the
  limit"). That was a judgement about the lattice. This job asks a different question with a different instrument: can
  the atlas be named with no known answer at all (a learned-metric kNN on reader-agreed tiles).
- PREREG-txeng3-10 (dev-FAIL) and X2 (dev-FAIL) / X2b (non-test): pair classifiers on topology (the 29-feature
  `topo_feats` of benchmark-tx/txeng3/10/glyph_atlas_pair.patch). Rescored: X2 2 fixed / 6 broken p 0.29; X2b 3 / 1;
  TXE3-10 6 / 0 p 0.031 (verifier pending). Differs here: the topology features are one of two feature sets inside a
  multi-class kNN with a learned metric, not a one-pair logistic discriminator.
- M15 / MQS-CLASSIFY-ROUNDS (9 Oct 2026): owner tiles layered on labels.json gained 0.000; labels.json's 309 tune-truth
  overrides out-voted them. Differs here: labels.json never votes in any gated arm (--only-train-labels).
No named row is `retired`.

## Fixed inputs (all on disk; nothing fetched)
- Atlas: ciphers/nevers-birago-fr3251-1572/atlas/{signs.tsv (4,209 boxes), bitmaps.npz, marks.tsv, clusters.tsv}.
  labels.json is read ONLY by arm A0 (reference) and labels_boxmapLA.json ONLY by A0' (beside, never gated).
- Sibling reads: harvest/{f139v,f144r,f162r,f174r,f174v,f174vB,f175v,f184r}/passC_agreement.tsv and
  harvest/f185r/passC_rest90_agreement.tsv (passage order = file order; harvest/ciphertext_<leaf>.tsv confirms it).
  f152r's passC_agreement.tsv is NOT training (f152r is an eval item, reported beside).
- no.87 reads for A4 only: benchmark-tx/outputs/birago1572-no87/passA.tsv and passB.tsv (their per-position agreement).
- A5 only: atlas/secure_tokens.tsv minus its f152r rows.
- Scorer only (opened by tools/tx_bench.py and atlas/score_no87.py --map <temp compat>, never by an arm): BENCHMARK-TX.tsv,
  benchmark-tx/birago1572-no87.truth.tsv (+ .flags.tsv), birago1572-f152r.truth.tsv.
- Never used (R4/R4a): atlas/no87_box_token.tsv, atlas/no87_box_token_labelaware.tsv as an arm input, txeng3/7/
  f152r_box_token.tsv, any sorter page/status/pile/seed, settled_labels, owner_map, key_pins, passX20*, labels.tsv.
- Unsupervised feature fit: the HOG+PCA40 scaler/PCA of glyph_atlas.py `feats` is fitted on all 4,209 atlas bitmaps with
  no label (today's behaviour, shared by A0, A1 and A2 alike). The LEARNED metric (LDA/NCA) is fitted on the voter
  tiles only; every eval page (f152r_, f178r_, f178v_, f179r_) is excluded from that fit and from the vote, and in A4
  the evaluated line's own tiles are excluded (leave-one-line-out).

## Machine labels (steps 1-3 of the brief; no owner, no known answer)
Line correspondence (new here, truth-free, geometric + count-based): the sibling passages are named by letter line
(L02, L04.1, V01, f184v_L01) and the atlas pages by segmenter row, which merges two cursive lines on some pages (f139v:
3 atlas rows for 5 passages; f185r: 3 rows for 8) and holds prose rows on others (f144r, f152r, f162r, f184r). For each
atlas page a monotone DP assigns the ordered passages to the ordered atlas rows: a row may take 0 passages (prose) or
k >= 1 consecutive passages; cost per assigned row = |boxes - tokens assigned|, per unassigned row 0. A row that takes
k >= 2 passages is split into k sub-rows by the optimal 1-D clustering of its boxes' y-centres (sorted y, k-1 cut
points minimising within-group variance), assigned top to bottom. The result is a scratch signs copy with renumbered
page-local lines (benchmark-tx/txeng4/3/maps/signs_lines.tsv, committed) and per-leaf reads named <page>_L<nn>
(maps/read_<page>.tsv). This correspondence is a construction, not a verified fact: every line is then gated by
join_check (step 3), and a line whose correspondence is wrong FAILs or is UNCHECKABLE there and contributes nothing.
1. Seed round: box_token_align --lam 0 per page (width only); keep 1:1 boxes at rows with status agree, idA == idB,
   neither conf L (the AGREED token at that box).
2. classify --only-train-labels --train-labels <step-1 tokens> --holdout f152r_ --holdout f178r_ --holdout f178v_
   --holdout f179r_ --topk 3 --page all (HOG+PCA40 kNN5, today's features; labels.json never votes). This is a
   bootstrap step: its top-3 only steers the second map round and its top-1 is the check label.
3. Re-map each page with --topk <step 2> --loo --check-labels <step-2 top-1> --check-bound. A token is kept only if it
   is 1:1 at the same position in both rounds AND its line passed. On FAIL: drop the failing lines, list them, re-check
   once; still FAIL -> the leaf contributes nothing. UNCHECKABLE -> nothing. The printed rows and verdicts are pasted
   into the PREREG addendum and RESULTS. These are the AGREED LABELS; counts per leaf and per code are reported before
   any fit. A4's no.87 tiles (passA/passB agreement, all 29 no.87 lines) are joined the same way (steered by the step-2
   top-3 for the no.87 boxes, check = its top-1, --check-bound) and the result pasted before any fit.
Classifier exclusion (R4a): classify excludes each box from its own vote, so the step-2 top-1 used as the check label on
a sibling box never came from that box's own label; the check is run leave-one-out (--loo) because the same top-3 steered
the map.

## Tool change (tools/glyph_atlas.py classify; shared-tools rule R7)
- `--features hog|hog+zone+topo`: hog = today's X (PCA40 of HOG + 2 log size terms). hog+zone+topo = X plus the 29
  features of `topo_feats` from txeng3/10/glyph_atlas_pair.patch (its 4x4 ink-zoning grid, 16; hole/skeleton topology,
  10; rh, rw, dy, 3), standardised on the voter tiles.
- `--metric none|lda|nca --metric-dim D`: scikit-learn LinearDiscriminantAnalysis / NeighborhoodComponentsAnalysis
  fitted on the voter tiles only (the --train-labels tiles that are not held out), then every box is transformed and the
  kNN runs in that space. Offline tests in tools/tests/test_glyph_atlas.py: the fit never sees a held-out page; a planted
  two-class toy separates under NCA. If `git log origin/main --since='1 hour ago' -- tools/glyph_atlas.py` shows another
  TXE4 session's commit, the change is kept as benchmark-tx/txeng4/3/glyph_atlas.patch with its test and applied to a
  scratch copy (named in ROOM).

## Arms (eval units never in any fit or vote; same AGREED LABELS in A1-A4)
- A0: labels.json atlas (known-answer-named reference, not a control). A0': labels_boxmapLA.json, beside only.
- A1: AGREED LABELS, today's HOG+PCA40 kNN5, metric none (the label-volume control: same tiles and labels as A2).
- A2 (PRIMARY): AGREED LABELS, the dev-chosen features + NCA + k.
- A3: A2 with the labels permuted across the voter tiles, seeds 1-20 (shuffled-label chance null).
- A4: A2 plus no.87's own A/B-agreed tiles, leave-one-line-out (the evaluated line's tiles out of fit and vote).
- A5: NCA (A2's setting) on secure_tokens.tsv minus its 48 f152r rows, beside only; its LCS join is first run through
  join_check (check labels = step-2 top-1, as a map keyed by the construction's line names); not PASS -> A5 dropped.

## Dev choice (frozen grid)
Features {hog, hog+zone+topo} x NCA dim {16, 32, 64} x k {3, 5, 9} = 18 settings, scored on dev_tune (f178v L01-L12)
err_true flagged-excluded; ties on as-measured, then the smaller dim. Each setting's output is a per-line box sequence of
top-1 codes (atlas page f178v row li = letter line Lli, boxes in x order; no box map needed). Frozen, committed and
pushed before the eval look. The metric-dim is capped by the feature count and by (classes - 1) for LDA; LDA is not in
the grid (NCA only, as the brief's grid says) and is reported only if a run fails to converge.

## Endpoint
tools/tx_bench.py --bench BENCHMARK-TX.tsv --item birago1572-no87 --exclude-flagged --coverage-diagnostic (--strict and
--paired beside) on eval_heldout (f178v L13-L23, f179r L01-L03) per arm: err_true as measured AND flagged-excluded,
Wilson 95%, S/D/I. Top-3 miss through atlas/score_no87.py --map <temp no87_map.py --compat copy, never committed>.
f152r (73 scored) beside, direction only. Reference beside: corrected-join atlas top-1 0.103, top-3 miss 0.078.
Degenerate optimum named: a box sequence that emits '_' or '_held' for every box scores every token wrong; an arm whose
top-1 is '_' on a box emits '_' (never the line read), so no arm can borrow the line read's accuracy.

## Gate (eval_heldout, as measured; flagged-excluded beside and must not reverse)
(i) A2 vs A1 paired: fixed > broken, exact binomial p < 0.05.
(ii) A2 err_true <= A0's 0.162.
(iii) every A3 seed >= A2 + 0.20.
All three: PASS. (i) and (iii) without (ii): "weak: reader labels do not yet reach the known-answer-named atlas".
Anything else: FAIL. A4 gated the same way, reported beside.

## Control and why it can vary
A3's permuted labels destroy label-tile correspondence while keeping the tiles, codes and counts; TXE3-7's permuted nulls
read 0.719-0.791 on no.87 after the rescore, so the null moves far from any real arm. A1 shares A2's tiles and labels
exactly, so A2 - A1 is the features and the metric alone. Before any truth is read, the number of eval boxes whose top-1
differs between A2 and A1, and between A2 and each A3 seed, is counted (can_vary.json); 0 on either = NON-TEST, not a
negative. Ceiling: A0 at 0.162 leaves headroom.

## Units, stop rule and declared reading
1. Maps with shift checks (25 min). 2. Tool build + tests (35 min). 3. Dev grid (20 min). 4. Eval look and scoring
(15 min). Running estimate = Fable floor (~9.5) + units; no unit starts past 02:56 UTC or past an estimated USD 12.
Declared reading: after unit 1 only: "AGREED LABELS built, N tokens on M leaves; no classifier result". After unit 2:
"tool landed, untested on this target". After unit 3: "dev choice frozen; no eval look, no verdict". After unit 4: the
gate word for word. A null is a result. Non-test if the can-vary count is 0 or if every leaf's join is UNCHECKABLE.

## Expected (written before anything runs)
A1 and A2 both well above A0 (0.162) -- TXE3-7's A1 read 0.314 with 445 tiles; more tiles and a learned metric may bring
A2 under 0.25 but reaching 0.162 without a known answer would be a surprise. Most likely verdict: weak or FAIL on (ii).

## Addendum 1 (01:3x UTC 12 Oct, after unit 1, before any fit): join verdicts pasted (R4a)

Correspondence: benchmark-tx/txeng4/3/labels/correspondence.txt. Step-1 tokens 936 on 11 pages; step-2 bootstrap kNN (885->936 voters, labels_empty.json). Round-2 join_check (--steered, check = step-2 top-1), per page:

```
f139v: verdict ('FAIL', 'PASS'), lines kept 1/5, agreed labels 0
join_check: FAIL n=87 share0=0.115 (null p95 0.071) share+-1=0.046 (bound 0.151) -> benchmark-tx/txeng4/3/labels/round2_f139v.tsv.joincheck.json
dropped ['f139v_L01', 'f139v_L02', 'f139v_L04']; recheck: PASS n=20 {'+-2': 1, '+1': 1, '-1': 1, '0': 8, 'none': 9}
join_check: PASS n=20 share0=0.400 (null p95 0.150) share+-1=0.100 (bound 0.203) -> benchmark-tx/txeng4/3/labels/round2_f139v_recheck.tsv.joincheck.json
f144r: verdict ('UNCHECKABLE', None), lines kept 0/5, agreed labels 0
join_check: UNCHECKABLE n=37 share0=0.000 (null p95 0.054) share+-1=0.135 (bound 0.136) -> benchmark-tx/txeng4/3/labels/round2_f144r.tsv.joincheck.json
f162r: verdict ('UNCHECKABLE', None), lines kept 0/2, agreed labels 0
join_check: UNCHECKABLE n=6 share0=0.333 (null p95 0.342) share+-1=0.167 (bound 0.333) -> benchmark-tx/txeng4/3/labels/round2_f162r.tsv.joincheck.json
f174r: verdict ('PASS', None), lines kept 3/4, agreed labels 41
join_check: PASS n=73 share0=0.589 (null p95 0.097) share+-1=0.027 (bound 0.110) -> benchmark-tx/txeng4/3/labels/round2_f174r.tsv.joincheck.json
f174v: verdict ('FAIL', 'PASS'), lines kept 6/11, agreed labels 61
join_check: FAIL n=208 share0=0.207 (null p95 0.044) share+-1=0.077 (bound 0.111) -> benchmark-tx/txeng4/3/labels/round2_f174v.tsv.joincheck.json
dropped ['f174v_L05', 'f174v_L06', 'f174v_L07']; recheck: PASS n=139 {'+-2': 11, '+1': 7, '-1': 5, '0': 43, 'none': 73}
join_check: PASS n=139 share0=0.309 (null p95 0.058) share+-1=0.086 (bound 0.123) -> benchmark-tx/txeng4/3/labels/round2_f174v_recheck.tsv.joincheck.json
f174vB: verdict ('FAIL', 'PASS'), lines kept 10/11, agreed labels 134
join_check: FAIL n=266 share0=0.568 (null p95 0.057) share+-1=0.056 (bound 0.099) -> benchmark-tx/txeng4/3/labels/round2_f174vB.tsv.joincheck.json
dropped ['f174vB_L01']; recheck: PASS n=247 {'+-2': 7, '+1': 5, '-1': 8, '0': 151, 'none': 76}
join_check: PASS n=247 share0=0.611 (null p95 0.057) share+-1=0.053 (bound 0.097) -> benchmark-tx/txeng4/3/labels/round2_f174vB_recheck.tsv.joincheck.json
f175r: verdict ('PASS', None), lines kept 1/1, agreed labels 13
join_check: PASS n=23 share0=0.565 (null p95 0.130) share+-1=0.043 (bound 0.176) -> benchmark-tx/txeng4/3/labels/round2_f175r.tsv.joincheck.json
f175v: verdict ('PASS', None), lines kept 2/3, agreed labels 21
join_check: PASS n=45 share0=0.756 (null p95 0.089) share+-1=0.044 (bound 0.138) -> benchmark-tx/txeng4/3/labels/round2_f175v.tsv.joincheck.json
f184r: verdict ('FAIL', 'PASS'), lines kept 5/8, agreed labels 49
join_check: FAIL n=135 share0=0.178 (null p95 0.059) share+-1=0.059 (bound 0.111) -> benchmark-tx/txeng4/3/labels/round2_f184r.tsv.joincheck.json
dropped ['f184r_L14', 'f184r_L15']; recheck: PASS n=112 {'+-2': 2, '+1': 3, '-1': 2, '0': 24, 'none': 81}
join_check: PASS n=112 share0=0.214 (null p95 0.063) share+-1=0.045 (bound 0.118) -> benchmark-tx/txeng4/3/labels/round2_f184r_recheck.tsv.joincheck.json
f184v: verdict ('PASS', None), lines kept 4/4, agreed labels 48
join_check: PASS n=90 share0=0.544 (null p95 0.067) share+-1=0.100 (bound 0.112) -> benchmark-tx/txeng4/3/labels/round2_f184v.tsv.joincheck.json
f185r: verdict ('FAIL', 'PASS'), lines kept 5/8, agreed labels 24
join_check: FAIL n=116 share0=0.336 (null p95 0.061) share+-1=0.034 (bound 0.131) -> benchmark-tx/txeng4/3/labels/round2_f185r.tsv.joincheck.json
dropped ['f185r_L07', 'f185r_L09']; recheck: PASS n=93 {'+-2': 3, '+1': 1, '-1': 2, '0': 39, 'none': 48}
join_check: PASS n=93 share0=0.419 (null p95 0.077) share+-1=0.032 (bound 0.130) -> benchmark-tx/txeng4/3/labels/round2_f185r_recheck.tsv.joincheck.json
```

AGREED LABELS 391: f174r 41, f174v 61, f174vB 134, f175r 13, f175v 21, f184r 49, f184v 48, f185r 24 (f139v 0 after its dropped lines and the two-round position rule; f144r, f162r UNCHECKABLE -> nothing). Far under the brief's ~1,100: the two-round same-position rule and the per-line gate drop most of the width-only seed round's tokens, as pre-registered. Codes with >= 5 tiles: 31 of 42.

A4 (no.87 passA/passB LCS agreement 743 of 844 passA tokens): no87_round2 FAIL (f178r_L03 B1) -> dropped -> recheck PASS n=751, 0/-1/+1 428/12/12; 662 agreed tiles on 28 lines.

Deviation noted: a first run (folder maps/, uncommitted) read gap tokens the reconciled reading drops and let the count DP merge a partial-cipher first line into the next; fixed before any classifier arm ran (read = merged tokens; a row takes two passages only when its y-spread shows two baselines). A built-in safety check denied the scratch cleanup rm; nothing was re-issued, the folder was renamed instead.

## Addendum 2 (01:5x UTC 12 Oct, after the eval look)
A5 join (secure_tokens minus f152r, unsteered check = step-2 top-1): PASS n=588, 0/-1/+1 443/5/6, share0 0.753 vs null p95 0.077
-> A5 scored beside. Frozen setting hog+zone+topo NCA dim 32 k 5 (38bdc6bd1, before the look). Gate verdict: FAIL -- (i) A2 vs A1
fixed 11 / broken 10, p 1.000; (ii) A2 0.242 > 0.162; (iii) met (min A3 0.846). A4 beside: all three met (0.144; 46/8; p < 0.0001),
with its label-volume control un-run (see RESULTS.md). Numbers and the three owner sentences in benchmark-tx/txeng4/3/RESULTS.md.
