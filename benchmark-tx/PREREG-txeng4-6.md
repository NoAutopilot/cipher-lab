# PREREG TXE4-6 TIEBREAK (account 3, Fable 5.1 worker, session_01H8mDJE4tM3AC15746vPvQh, 12 Oct 2026 01:2x UTC by date -u; pushed BEFORE any read or score)

One of ten TXE4 experiments the account-3 parent launched on 12 Oct 2026 (brief `.claude/briefs/runs/2026-10-11-acct3-txe4-6.md`,
commit 93b7bb321). Question: when two blind readers disagree on a sign, does a free check of that sign's own box against the
k nearest tiles the same two readers AGREED on elsewhere on the same page settle the split better than the paid third
(adjudicating) reader? Read-free: no reader call, no vision call, no image read by a model. Rules: the brief's common TXE4 rules
R1-R10 and R4a bind. Truth and flags are opened only by tools/tx_bench.py (and by `dev_sweep.py`, which imports
tx_bench.position_errors for the declared dev step on no.87 dev_tune only -- the TXE4-9 tx_calibrate precedent). Every output is
committed with its sha256 (benchmark-tx/txeng4/6/SHA256SUMS.prescore) before it is scored; nothing published, nobody contacted.

## Hypothesis
H1: at the rows where readers A and B disagree, picking the candidate whose agreed-tile neighbours lie nearer the row's own box
(a kNN over glyph_atlas classify's features, tiles = the same page's reader-agreed boxes, leave-one-line-out) fixes more scored
positions than it breaks against the committed adjudicated output, pooled over no.87 eval_heldout, f152r and gunther L01-L17,
by the gate below, and beats a permuted-label null.
H0 (a result): it does not; the page's agreed ink does not separate the look-alike pairs the readers split on at this N, or the
adjudicator is already at the oracle bound on the Birago items (TXE-K: 35/36 on dev).

## Nearest prior (register rows) and what differs from them
- `M19-fable` / `M19-opus` (TXE-K, tools/tx_adjudicate.py, benchmark-tx/txeng/adjud/RESULTS.md, dev-FAIL): a value-blind third
  READER re-posed the same split items; the committed Sonnet adjudication was right at 35 of 36 dev_tune items, so dev is at
  ceiling for adjudication. This job replaces the third reader with a read-free check against the page's own agreed tiles; the
  committed adjudication is the base it is paired against, and dev is used only to freeze the margin threshold (safety).
- `X2b` (tools/tx_pair_clf.py --train-domain dev_tune, PREREG-txeng2-3, non-test; rescored on the corrected tiles 3 fixed / 1
  broken) and TXE3-10 (benchmark-tx/txeng3/10/, 6 / 0, p 0.031, verifier pending): classifiers trained on no.87's OWN ink
  moved the right way. Those are per-pair logistic models applied at every position whose line-read sign is a pair member,
  trained on truth-labelled dev tiles. This job's model is a kNN with NO truth label in training (tiles labelled only by what
  both readers agreed), applied ONLY at A!=B rows, on three items including a second hand (gunther).
- TXE3-3 CROSSHAND (benchmark-tx/txeng3/3/RESULTS.md and VERIFY.md): on gunther the blind adjudicator was right at 3 of the 9
  one-reader error events; an oracle pick reads 8/214 as measured. That headroom (passC 14 -> oracle 8) is what this job tests
  for; the no.87 headroom is at most the 6 split-row errors of passC (TXE3-1: 19 A!=B tiles of 371 hold 6 of 15 errors).
- TXE4-0 REPAIR (benchmark-tx/txeng4/0/RESULTS.md): the join gate tools/join_check.py and the label-aware aligner this job's
  every box-to-token join runs through. Its unit 5 (sibling-only kNN top-3) did NOT land: see Deviation 1.
Retired instruments named in R4 (':' mark rule, transcribe-and-decode crossword, look-alike pass as accuracy, exemplar compare
layout, M24 feature-first, err_2reader as predictor) are not used; no retired register id is re-run here.

## Deviations from the brief's METHOD, declared now
1. Boxes for no.87 and f152r: the brief names a kNN on SIBLING reader-agreed tokens (two rounds, holdout f152r_ f178r_ f178v_
   f179r_) or TXE4-0 unit 5's files. Unit 5 did not land, and the sibling passages' (f184r L01.., f168 R02.., f175v V01..,
   f174vB L01..) keys to the atlas's own line numbers are not on disk; building them is a unit of its own that does not fit
   this box. So all THREE items use the brief's own gunther recipe: round 1 `box_token_align.py --lam 0` as a seed only, on the
   reconciled draft of the page; round 2 a kNN (`glyph_atlas.py classify --only-train-labels --topk 3`, the box itself never
   votes) trained on the round-1 1:1 tokens at agreed columns (A == B, lower confidence not L) of the SAME page, then
   `box_token_align.py --topk <that kNN> --loo --check-labels <its top-1> --check-bound` (steered, so the leave-one-out row
   is the check). Boxes kept = 1:1 at the same position in both rounds. No owner evidence (no sorter status, seed, settled
   label, owner map, labelaware map) enters any map. The old width-only maps are never read.
2. Features: glyph_atlas classify's (HOG + PCA(40) + log size), fitted on the item's own atlas bitmaps. TXE3-10's topology
   features are NOT in tools/glyph_atlas.py on main (grep 'topolog' = 0), so they are not used.
3. The tiebreak ships as `tools/tx_tiebreak.py` (new, with tools/tests/test_tx_tiebreak.py), not as a reconcile_passes.py option:
   reconcile_passes.py aligns passes and has no image or atlas input; bolting a feature-space kNN onto it would make the
   aligner import scikit. tx_tiebreak.py reads reconcile_passes.py's own outputs (ciphertext_draft.tsv, disagreements.tsv).
   `tx_bench.py --pair A B` is added as named (b).
4. f152r geometry: the atlas's f152r lines 2-5 are the letter's L01-L04 and the two prose x-bounds, exactly as
   benchmark-tx/txeng3/7/rescore/map_f152r_la.py (truth-free geometry, reused, not re-derived).
5. Gunther boxes: `glyph_atlas.py segment --page p2_Lnn=<crop>` on the 17 crops, one page per crop, then the two rounds above.

## Fixed inputs (frozen now)
- Atlas: ciphers/nevers-birago-fr3251-1572/atlas/{signs.tsv,bitmaps.npz} for the Birago items; a fresh segment of
  benchmark-tx/txpool/gunther8246-p2/crops/p2_L01..L17.jpg for gunther (benchmark-tx/txeng4/6/gun_atlas/).
- Passes: no.87 benchmark-tx/outputs/birago1572-no87/{passA,passB}.tsv, base passC.tsv; f152r {passA,passB}.tsv, base
  passZ_pipeline.tsv; gunther benchmark-tx/txeng3/3/{passA_gun/passA_gun.tsv,passB_gun/passB_gun.tsv}, base passC_gun.tsv.
  Splits from `tools/reconcile_passes.py A B --method nw` (the committed recipe).
- Reachable rows: A != B columns where both candidates are non-blank signs (a one-sided blank is an insertion/deletion
  question with no box to compare on the blank side; such rows keep the base). The reachable share is quoted per item.
- Agreed tiles: draft rows with why 'agree' and confidence not L, with a 1:1 box kept in both rounds; leave-one-LINE-out.
- Distance: for a split box x, d(c) = mean Euclidean distance in the classify feature space to the k = 5 (fewer if fewer exist,
  minimum 1) nearest agreed tiles of class c, c in {A's sign, B's sign}; margin m = (d_far - d_near) / d_near. Undecidable
  (no agreed tile of one candidate on another line): keep the base. The pick is the nearer class when m > t.
- Threshold rule (dev, no.87 dev_tune = f178v L01-L12, safety only): t = the smallest value in {0, 0.05, 0.10, ..., 1.0} at
  which decided accuracy on dev reachable rows (leave-one-line-out) >= 0.90 at coverage >= 30% of reachable rows. If none
  meets it, STOP before eval and report the dev numbers (a null is a result). Accuracy at t = 0 is reported against the
  committed adjudicator's 35/36 and against a coin (0.5).
- Output per item = base with the tiebreak's pick written at the base position aligned to each decided split column
  (draft-to-base alignment by tx_bench.align's DP on sign identity; a decided column whose base position is a gap keeps
  the base).

## Arms
- T (target): base + overrides at m > t (the frozen t).
- R (replacement, beside): base + overrides at every reachable row (t = 0), fixed and broken counts beside.
- (a) control: the page's agreed-tile labels permuted within the page, 20 seeds (seeds 1-20), same t; this changes which
  candidate is nearer, so overrides, fixed and broken vary. It is the gate's shuffled-label chance null (R4a).
- (b) control: a coin flip (seeds 1-20) between A and B at T's own override positions and count.
- (c) the committed adjudicated output is the base.

## Endpoint
PRIMARY: pooled fixed and broken of T against the base, position McNemar from `tools/tx_bench.py --exclude-flagged --paired
<base> --strict` (gunther also `--coverage-diagnostic --line-prefix p2`), both masks (as measured; flagged excluded beside,
never alone), with err_true and Wilson 95% from the counts, unit-cost edits and S/D/I beside, per item and pooled over
no.87 eval_heldout (376) + f152r (73) + gunther L01-L17 (214).

## Gate (the brief's, word for word)
- pooled fixed > broken against the committed adjudicated output, exact two-sided p < 0.05;
- AND the real net > the 95th percentile of control (a);
- AND as-measured err_true is not higher on any of the three items.
Beside: the replacement arm (t = 0) with its fixed and broken counts.

## Units, stop rule and declared reading
U1 boxes and maps with pasted shift checks (30 min); U2 tool and tests (35 min); U3 pair report (10 min); U4 dev (10 min);
U5 eval and scoring (15 min). Estimate USD 12 (floor 9-10 + units). A unit is not started past 96 minutes from the claim
(01:20 UTC -> 02:56) or past a running estimate of USD 12. Readings: U1 only -> 'maps built, tiebreak untested'; U1-U3 ->
'pair report only, tiebreak untested'; U1-U4 -> 'dev result only: t frozen or STOP'; U1-U5 -> the gate verdict. An item whose
join check FAILs after its failing lines are dropped, or is UNCHECKABLE, or (gunther) gives a 1:1 box to under 70% of its
split rows, is dropped from the pool and reported as a non-test for that item. Eval looks: one per item (LOOKS.tsv).
