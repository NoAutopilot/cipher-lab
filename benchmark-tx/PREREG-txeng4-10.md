# PREREG TXE4-10 RECOG-CUT: does a classifier-chosen cut find sign boundaries in joined Saint-Gouard shapes? (account 3, Fable 5.1 worker, session_01GaCy6B7SdgFRcqYHTeFDL1; written 12 Oct 2026 01:2x-01:3x UTC by date -u, committed BEFORE any label join, segment, classify or score of this experiment)

One of ten TXE4 experiments (account-3 parent session_0198Cv8ypBfBVfRToKVWx33M; brief .claude/briefs/runs/2026-10-11-acct3-txe4-10.md).
Work in benchmark-tx/txeng4/10/. Nothing below is loosened after a result is seen; amendments are appended, dated. Read-free: no
model call, no network, no owner evidence (R4), no frozen confirm item.

## Hypothesis (low prior, declared)

On Vivonne f.102r (vivonne1573-f102r-dev2, dev), a pen-unit box wider than 1.5 x the median sign height holds several joined
signs. TXE3-6 showed the segmenter's column-ink-minimum split reads no better than random cuts, and VERIFY-6 showed the
whole pen-vs-split gap is reproduced by shuffled labels (box count, not reading; the kNN reads 0.046 above chance). The
hypothesis tested here: choosing the cut set that makes the pieces look most like known signs (the summed kNN log-posterior
of the pieces, minus a per-piece cost) finds sign boundaries better than ink valleys or random cuts. Prior: low, because the
classifier is near chance; the rigour of the chance nulls is the point.

## Nearest prior rows in research/TX-REGISTER.tsv, and what differs from them

- **PREREG-txeng3-6** (TXE3-6 UNIT; benchmark-tx/txeng3/6/): same item, same 22 train / 13 test lines, same (a) pen, (b)
  ink-minimum split and (c) random-cut box sets (used here as committed), same scorer. Differs: (1) a new cut rule, (d)
  recognition split, with its own shuffled-label control (e); (2) labels come from six machine reads voted together, never
  from truth (TXE3-6 labelled train boxes from the truth file); (3) boxes are joined to read positions through
  tools/box_token_align.py in two rounds with the join gate (R4a), never by count alone; (4) the gate carries a
  200-permutation reading-gain null on every arm (VERIFY-6's null A) and a 1:1 boundary share from tx_bench --seg-boxes.
- **PREREG-txeng3-5** (TXE3-5 BOXES): the owner's re-cuts, 1 fixed / 2 broken through an atlas kNN; not re-scored here, no
  owner cut is an input (R4). Differs: here every cut is the machine's.
- **S2-NOTE** (txeng2, TX-ENGINEER-2): on f.103r 42 of 75 product-reader errors were segmentation. Differs: this job tests one
  cutting rule under a weak kNN, not the product reader.
- BOXCLIP (benchmark-tx/boxclip/, 12 Oct 2026, gate FAIL): an edge-ink check for clipped boxes; read, not used. Differs: that
  asked whether a box is too small; this asks where a wide box divides.

## Fixed inputs (sha256 prefixes recorded 12 Oct 2026 01:25 UTC; none is edited)

- Crops: ciphers/fr16104-vivonne-spain-1572/images/c105_f102r_L??_s{1,2}.jpg (74), manifest.json x0 per crop.
- Box sets as committed by TXE3-6 (benchmark-tx/txeng3/6/seg/*/boxes.tsv): pen d710991f9ffff38c, sign 4e441b71de9beeea, rand1
  e9b837b6c6a850a0, rand2 4ac04256379daa54, rand3 b9eb91854fada35a. Their gitignored signs.tsv/bitmaps.npz were regenerated
  with benchmark-tx/txeng3/6/seg.py before this file was written; every regenerated boxes.tsv is byte-identical (git status
  clean), so the box sets are TXE3-6's.
- Truth and bench: benchmark-tx/txeng3/6/truth_test.tsv 66dda3830cbef39d (the 13 test lines' rows of the committed dev2 truth),
  bench_test.tsv 5f3a2ac9b933cb82. Opened only by tools/tx_bench.py (R3).
- Six machine reads for the labels: benchmark-tx/outputs/vivonne1573-f102r-dev2/passA_sv bb14596472678803, passB_sv
  37936450e635c862, passA_tl 586463118b581e79, passB_tl babd58fc1e1dcf3c; benchmark-tx/outputs/vivonne1573-f102r-dev/passA_dv1
  4e5f7a1024c310ca, passB_dv1 0654504d5de3b8b0. NOT dev2/passA.tsv or passB.tsv (inputs of the truth's reference sequence).
- Key: ciphers/fr16104-vivonne-spain-1572/key.tsv 7e3e758f6c6751ff (code column only, the label alphabet).
- Lines: TEST f102r_L02, L04, L08, L10, L16, L18, L20, L24, L28, L30, L32, L34, L36 (13; L14 has no truth rows, TXE3-6
  amendment 1). TRAIN the other 22 truth lines of L01-L36. Test lines never enter the labels, the kNN or the lambda choice.
- Classifier features: today's tools/glyph_atlas.py feats() (HOG 9/8x8/2x2 of the 48x48 bitmap, PCA 40, unit scaling, log
  rh and rw at weight 3), fitted on the exemplar set only. TXE4-3's frozen A2 setting had not landed when this job started
  (no TXE4-3 ROOM line at 01:22 UTC), so today's features are used.

## Labels (machines only; no truth, no person)

1. Consensus per train line: tools/reconcile_passes.py --vote over the six reads (passA_sv first). A position is a *label
   position* when >= 5 of 6 passes read the emitted sign (vote_share >= 0.83). The vote's full plurality sequence is the
   line read for the join; only label positions give labels.
2. Join round 1: tools/box_token_align.py --lam 0 (width only, a seed) of TXE3-6's seg/sign train boxes (line coordinates
   from boxes.tsv x_line) to the consensus sequence. Boxes 1:1 at a label position get a provisional label.
3. Round-1 kNN (k 5) on those provisional labels; its top-3 over every train box, each box excluded from its own vote
   (leave-one-out), written as a classify --topk file.
4. Join round 2: box_token_align.py --topk <round-1 top-3> --loo (default lam 1.5, neutral 0.5). A box is labelled only where
   it is 1:1 at the SAME position in both rounds and that position is a label position.
5. Shift check before the final kNN is trained: box_token_align.py --check-labels <round-1 top-1> --check-bound (and
   tools/join_check.py --steered on the round-2 map, since the top-k steered it; the leave-one-out row is the one read).
   PASS -> labels stand. FAIL -> drop the failing lines, re-check once; a second FAIL -> nothing joined is scored, verdict
   'untested-by-this-tool'. UNCHECKABLE -> fall back to TXE3-6 labels.py's round-0 rule with reader consensus in place of
   truth: keep only train lines whose seg/sign box count equals the consensus count AND whose round-1 map is all 1:1,
   label 1:1 in order; the join is then unverified and the verdict cannot go beyond 'untested-by-this-tool'.
6. Final kNN: one RecKNN (glyph_atlas.py, k 5, Laplace alpha 0.5: p(c) = (votes_c + 0.5) / (5 + 0.5 x C), C the number of
   label codes) trained on the labelled train boxes' bitmaps and frozen (labels.tsv + its sha256 in SHA256SUMS.prescore).
   It classifies EVERY arm's test boxes (none of which is an exemplar), top-1 and top-3.

## Arms (13 test lines)

- (a) pen units, (b) ink-minimum split, (c) random cuts seeds 1-3: TXE3-6's seg/*/boxes.tsv as committed.
- (d) recognition split: tools/glyph_atlas.py segment --split-by-recognition LABELS.tsv --rec-atlas DIR [--rec-lambda L]
  (new option, offline test in tools/tests/test_glyph_atlas.py). A pen box wider than W = 1.5 x median height (TXE3-6's W)
  gets candidate cut columns = the local minima of its column-ink profile plus a grid every 0.25 x median height, each at
  least 0.35 x median height from the box edges and from each other; every cut set of 0-3 cuts (1-4 pieces) is enumerated
  and the set maximising  sum_i g_i - L x n  is kept, g_i = log p(top code | piece i) - log(1/C) >= 0 (the kNN log-posterior
  of the piece above uniform), n the number of pieces. This is the brief's "summed log-posterior minus L per piece" with
  L shifted by the constant log(1/C): the same family. Degenerate optima, named: L = 0 -> every wide box in 4 pieces;
  L > max g -> no box split (= pen units). A piece with no ink is dropped.
  Lambda is chosen on the TRAIN lines only by sum over lines |boxes - consensus count| (no truth), from the grid
  L in {0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2, 2.5, 3.0}; ties go to the larger L.
- (e) recognition split with permuted labels, seeds 1, 2, 3: the exemplar labels permuted among the exemplars, the same
  features, the same L; the cut-choosing kNN is the permuted one, but classification of (e)'s boxes uses the frozen real
  kNN like every arm. Before scoring, the number of test boxes in which each (e) seed differs in geometry from (d) is
  counted and written: that is the can-vary count (rule 3). If it is 0 for a seed, that seed is a non-control and is said so.

## Endpoint (per arm, both masks, Wilson 95%; --strict beside; SER with S/D/I beside)

- Top-1 err_true via tools/tx_bench.py --bench benchmark-tx/txeng3/6/bench_test.tsv, as measured AND --exclude-flagged.
- Reading gain over chance: mean err_true of 200 label permutations over the arm's own test boxes (labels permuted across
  its boxes, geometry fixed; VERIFY-6's null A; tx_bench.py --perm-null 200 --perm-seed 1, a new option) minus the arm's
  real err_true.
- Boundary share: tx_bench.py --seg-boxes BOXES.tsv (new option): per line |boxes - truth positions| and the 1:1 / 2:1 /
  1:2 / skip shares of a box_token_align.py map of the boxes to the truth's ref_sign sequence, steered by the frozen kNN's
  top-3 with --loo, its shift check (--check-labels = the kNN top-1, leave-one-out row) printed beside. Truth is opened only
  inside tx_bench (R3).
- Paired: tx_bench --paired per line, (d) vs (a) and (d) vs each (e) seed; line sign test p (exact).

## Gate (all three needed for PASS)

1. (d)'s reading gain exceeds (a)'s by >= 0.03 and exceeds (b)'s and every (c) seed's.
2. (d) beats every (e) seed on err_true as measured, paired line sign test p < 0.05: at 13 lines this needs at least 11 of 13
   non-tied lines in one direction (two-sided exact binomial: 11/13 p = 0.0225, 10/13 p = 0.0923); with ties, the same
   rule on the non-tied lines (n non-tied, the two-sided exact p < 0.05).
3. (d)'s 1:1 share (tx_bench --seg-boxes) >= (a)'s + 0.05.
Anything less: 'the machine cannot place sign boundaries in joined shapes on this hand with this classifier'. If the frozen
kNN is at chance (its top-1 reading gain on (a) under 0.03, or the shift check UNCHECKABLE), the verdict is
'untested-by-this-tool' instead, whatever the arm numbers say. A null is a result.

## Control and why it can vary

- (e): the cut columns are chosen from the labels, so permuting the labels changes which cut set wins; its boxes and scores
  can differ from (d), and the difference count is written before scoring. (e) and the 200-permutation null are the gate's
  shuffled-label chance nulls (R4a). (c) random cuts: the same count as (b), cuts moved (TXE3-6: 144-150 of 653 boxes differ).
- The label-permutation null on every arm removes box-count effects (VERIFY-6's lesson): a gain measured against each arm's
  own null cannot come from the number of boxes.
- Headroom: pen units read 0.772 against a chance level of 0.818 under TXE3-6's truth-labelled kNN (VERIFY-6). A kNN from
  machine consensus labels will be no stronger; this is declared, and gate 1's 0.03 margin is about two-thirds of that gap.

## Units, stop rule, and the declared reading per units done

Box 120 min from the claim (01:22 UTC; no unit starts after 02:58 UTC), cap USD 15 (parent reads get_session; running estimate
= Fable floor 9-10 + units; no unit starts past an estimate of USD 12).
- U1 labels: consensus, two-round join, shift check, frozen kNN (25 min, ~USD 1).
- U2 tools: glyph_atlas segment --split-by-recognition, RecKNN; tx_bench --seg-boxes and --perm-null; offline tests (40 min, ~USD 2).
- U3 arms: lambda on train, (d), (e) x 3, can-vary counts, classification of all 8 arm outputs, SHA256SUMS.prescore (20 min, ~USD 1).
- U4 scoring: tx_bench on all arms, both masks, paired, 200-permutation nulls, --seg-boxes; RESULTS.md (15 min, ~USD 1).
Readings: U1 only -> 'labels built, no arm run: no result'. U1+U2 -> 'tools landed, untested on the item'. U1-U3 -> 'arms built,
unscored: no result' (outputs stay committed with hashes for a later scorer). U1-U4 -> the gate above, word for word. If U1
ends UNCHECKABLE or double-FAIL, the arms are still built and scored but the verdict is capped at 'untested-by-this-tool'.
Eval looks: none (dev item only; R6 not triggered).
