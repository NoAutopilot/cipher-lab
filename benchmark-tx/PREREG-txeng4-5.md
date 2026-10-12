# PREREG TXE4-5 PAIR-BANK (account 3, Fable 5.1 worker, session_01HsQVPQ5RDUZTo6HUB2dYwm, 12 Oct 2026 01:2x UTC by date -u; pushed BEFORE any tool change, read or score)

Brief: `.claude/briefs/runs/2026-10-11-acct3-txe4-5.md` (93b7bb32). Claim: ROOM.md 01:18 UTC (pushed 649f4d484). Box: 120 min
from the claim, 01:18-03:18 UTC; unit-start limit 02:54 (96 min); running-estimate limit USD 12 of the USD 15 cap. (The ROOM claim
line's "01:25-03:25 / 03:01" was typed before the push; the clock-read figures here govern.) Prerequisite TXE4-0 REPAIR landed at
6f84c5af (tools/join_check.py, box_token_align.py --check-bound). Read-free: no reader, no vision call, no network beyond git.

## Hypothesis
Look-alike sign separators for ten confusable Birago 1572 pairs can be trained from MACHINE-AGREED tiles only (the two blind passes
agree on the sign; no owner sort, no dev truth, no secure/S-grade list) and, applied read-free at a line read's pair positions on
lines the model never saw, fix more pair errors than they break. Secondary (beside, not a gate): the d/s (T18/T98) separator does
not need the owner's 24 sorted tiles -- the machine-pool model matches TXE3-10's owner-pool model on dev_tune and on f152r.

## Nearest prior (register rows) and what differs from them
- TXE3-10 PAIR (`benchmark-tx/PREREG-txeng3-10.md`, RESULTS/VERIFY/RESCORE in benchmark-tx/txeng3/10/): one pair T18/T98, topology
  features, pool = dev truth tiles + S-grade secure tiles + the owner's 4 Oct sort; 6 fixed / 0 broken, p 0.031 on the corrected
  map (verifier ruling pending). Differs here: ten pairs; NO owner, dev-truth or secure tiles in any treatment pool (machine A/B
  agreement only); the join is tools/box_token_align.py with a machine kNN, checked by tools/join_check.py; a feature bank
  (topology + 4x4 zoning + HOG) with L1-logistic selection per pair; f152r as a never-pooled test leaf.
- X2 / TXE2-PAIR and X2b / TXE2-PAIR2 (`tools/tx_pair_clf.py`, benchmark-tx/txeng2/pair*/): pixels+HOG on secure tiles (2/6, p 0.29
  rescored) and on own-ink dev labels (3/1). Differs here: machine-agreed labels from twelve leaves, not secure or dev; topology
  in the bank; per-pair gates with a shuffled-label null inside the gate; eval on held-out lines and on another leaf.
- TXE-C (tx_pair_reread), TXE-H (tx_pair_hints), LOOKALIKE-TOOL: reader-based or retired; not re-run (R4).
Rule-3 note (brief): fourth attempt at pair classifiers on no.87; the third-attempt clause does not fire because X2 -> X2b ->
TXE3-10 moved together toward the gate; this is TXE3-10's own named next step (new pairs, new positions) with the human labels
removed, not a re-run of tx_pair_clf.py.

## Fixed inputs (frozen now)
- Atlas: `ciphers/nevers-birago-fr3251-1572/atlas/{signs.tsv,bitmaps.npz}` (4209 tiles, 18 pages).
- Machine agreement: `ciphers/nevers-birago-fr3251-1572/harvest/<leaf>/passC_agreement.tsv` for f139v, f144r, f162r, f168
  (R->f168r, V->f168v), f174r, f174v, f174vB, f175v, f184r (sibling pool leaves) and f178r, f178v, f179r (no.87's own A/B
  agreement). f152r's agreement file exists but f152r tiles NEVER enter any pool or kNN training set. The seed read per sibling
  line is pass A's own sequence as recorded in the agreement file (posA, idA); a tile is "agreed" only at status == agree.
  f162r's sub-line passages (L01.1 ...) are skipped if they do not resolve to one atlas line.
- Bases corrected: Pass A = `benchmark-tx/txeng/units/passA_eval_heldout.tsv` + `benchmark-tx/outputs/birago1572-f152r/passA.tsv`;
  L = `benchmark-tx/txeng/units/labels_eval_heldout.tsv` + `benchmark-tx/outputs/birago1572-f152r/passZ_pipeline.tsv`.
  Dev gate G2 on `benchmark-tx/txeng/units/labels_dev_tune.tsv` (and passA_dev_tune.tsv beside).
- Join recipe (R4a), every map: round 1 `tools/box_token_align.py --lam 0` (width-only seed, never stands alone); a kNN (cosine,
  k 7, on 16x16 downsampled ink + rh rw dy) trained ONLY on sibling-leaf tiles labelled by the round-1 join at agreed positions
  (pages f152r, f178r, f178v, f179r excluded from training), predicting top-3 for every atlas tile, leave-one-out for its own
  training tiles -> `--topk`; round 2 `box_token_align.py --topk KNN --loo --check-labels KNN-top1 --check-bound` (the labels
  steered the map, so the leave-one-out row is the check). Lines FAIL -> dropped and the check re-run once; UNCHECKABLE -> the
  join is unverified and the non-test rule applies. Pool tiles are those whose position is identical in rounds 1 and 2, on lines
  that PASS, op 1:1. The no.87 and f152r maps use the same recipe with `--read` the base being corrected and the same
  sibling-only kNN. Never: atlas/no87_box_token.tsv, no87_box_token_labelaware.tsv, txeng3/7/f152r_box_token.tsv, box_pos.tsv,
  --status, --tile-labels, labels.json, secure_tokens, owner files, settled_labels, passX20*, key_pins.
- Pairs (ten, from the brief): T18/T98, T90/T53, T76/T86, T76/T45, T76/T66, T50/T92, T24/T29, T60/T86, T95/T51, T64/T38.
- Features: topology (TXE3-10's 29: 16-cell ink grid, hole count/centroid/area, ink above/below the hole, skeleton endpoints and
  junctions and their place against the hole, skeleton length/ink, rh rw dy) + 4x4 zoning of the 32x32 ink box + HOG
  (glyph_atlas.py's own `_hog`). Selection per pair: L1 logistic (proximal gradient, lambda_1 fixed 0.05 on standardised
  features, class-balanced) keeps the non-zero features (at least 4: if fewer, the 4 largest |w|); the L2 PairLogit (lambda 1)
  is then fit on the kept features. Threshold t: TXE3-10's LOGO rule (smallest t in 0..0.9 with decided accuracy >= 0.95 at
  coverage >= 50%; none -> pair disabled). Groups for LOGO: sibling tiles by page; no.87 tiles by line.
- Pool rule at application: the pool never holds a tile from the line being corrected (no.87 own-ink tiles come only from other
  lines; for dev G2 each dev line is voted by a model whose pool excludes that line; for eval each eval line likewise). f152r
  tiles never in a pool. Pair counts per source are written read-free before any training (addendum A1).
- Read-free position counts (from the base files only, no truth): no.87 eval_heldout pass A / L: T98 10/10, T18 0/0; T90 9/9,
  T53 19/19; T76 10/9, T86 12/12; T45 38/38; T66 0/1; T50 1/1, T92 17/17; T24 3/3, T29 2/2; T60 27/27; T95 1/1, T51 0/0; T64 4/3,
  T38 1/1. f152r pass A / Z: T18 1/0, T98 2/3; T90 5/5, T53 1/1; T76 2/2, T86 5/6; T45 3/3; T66 0/0; T50 1/1, T92 1/1; T24 0/0,
  T29 0/0; T60 7/6; T95 2/2, T51 0/0; T64 2/2, T38 0/0. T24/T29 and T95/T51 and T64/T38 have 0-5 positions in the gate pool: they
  can pass dev gates but add at most a few flips; T76/T66 has 1.

## Arms
- Treatment, per pair: the machine-pool separator (above), applied at the base's A/B positions with a 1:1 box, flip iff m > t.
- Base: Pass A and L as listed, unchanged.
- Beside only (unit 5, optional): TXE3-10's owner-pool T18/T98 model rebuilt from the committed patch with `--pool-owner`,
  `--pool-dev`, `--pool-secure` and `--map` = this job's machine map for no.87 (never atlas/no87_box_token.tsv), on dev_tune
  (--loo-lines) and on f152r (`--exclude-pool-page f152r`), against the machine-pool T18/T98 model on the same two files.

## Endpoint
tools/tx_bench.py `--exclude-flagged --paired BASE --strict`, item birago1572-no87 (eval_heldout lines, --coverage-diagnostic) and
item birago1572-f152r: fixed / broken / net at the pair positions the model considered (touched rows), pooled over no.87
eval_heldout (new pairs only) + f152r (all passing pairs); exact two-sided sign test p; err_true as measured AND flagged-excluded
with Wilson 95% for base and output; unit-cost edits with S/D/I beside. T18/T98 and T90/T53 no.87 eval positions are REPORTED
(TXE3-10 and its rescore already looked at them) but EXCLUDED from the gate; those two pairs enter the gate only on f152r.

## Gate (the brief's, word for word)
- On the pass-A base: pooled fixed > broken, exact two-sided p < 0.05, with broken <= 1.
- On the L base: net >= 0.
- For each passing pair: the forced-threshold shuffled control has net <= +1 (the pair's shuffled-label chance null, R4a), and
  the label-reversed model breaks.
Dev gates before any eval application (brief METHOD 1): G1 leave-one-group-out accuracy above all 20 shuffled-label LOGO runs;
G2 dev_tune leave-one-line-out with broken = 0 (dev truth read only by tx_bench for G2). Only pairs passing both go to eval.
Power (tools/tx_power.py, --n 20, alpha 0.05): the exact sign test needs 6 fixed / 0 broken (p 0.031) or 8 / 1 (p 0.039) at
the least; 5/0 is p 0.0625. At E=6 pooled errors a 0.5-effective clean fixer passes in 0.018 of draws, at E=10 in 0.369; the
pooled new-pair positions number about 140 on no.87 eval plus about 30 on f152r, so the gate is reachable only if the bases
carry roughly 8 or more pair errors there and the separators catch most of them. A miss is "did not move at this N", not a
refutation, unless the controls show the separators are at chance (G1 fail).

## Control and why it can vary
- Per pair, 5 shuffled-label models (pool labels permuted, seeds 1-5) applied with `--force-t 0`: TXE3-10's ctrl-f shape, which
  flipped 2-4 positions there, so fixed/broken are free to differ from the real model's.
- Per pair, a label-reversed model (A and B swapped in the pool) applied with the real threshold rule: must break (it flips
  correct reads toward the wrong member); if it flips nothing, the pair's real model is "disabled by symmetry" and not counted
  as passing.
- Per pair, G1's 20 shuffled-label LOGO runs (the gate's own null).
- Every join carries join_check's within-page permuted-label null (B2/B3); an UNCHECKABLE join is a non-test for the tiles on it.

## Units, order, cost and stop rule
Running estimate = Fable floor 9.5 (TXE3-10 10.77 shape) + units. U1 land the patch + options (--pairs, --pool-agreed,
--feature-bank, map gated by join_check.require) with tests, 35 min, +0.5. U2 kNN, maps with pasted shift checks, pool counts
(addendum A1), 25 min, +0.5. U3 G1/G2 for ten pairs + controls, 30 min, +0.5. U4 eval outputs committed with SHA256SUMS.prescore
and LOOKS.tsv rows, then one score each, 15 min, +0.5 (running 11.5). U5 (optional, beside) owner-pool comparison, 10 min, +0.5
(running 12.0; started only if elapsed < 96 min). A unit is not started past 02:54 UTC or past a running estimate of USD 12.
Declared reading per units done: U1 only -> "tool landed, non-test (no pools)"; U2 -> "non-test: pool counts and join verdicts
only"; U3 -> "dev result per pair, no eval look"; U4 -> the registered verdict on the gate above; U5 -> adds the beside sentence.

## What is NOT done
No frozen confirm item; no truth or flags edit; no owner evidence in any arm; no retired instrument; no publishing; no second
eval look; no re-tuning after the eval outputs are committed; no edit to tools/glyph_atlas.py if another TXE4 session committed
to it within the hour (then benchmark-tx/txeng4/5/glyph_atlas_pairbank.patch, named in ROOM).
