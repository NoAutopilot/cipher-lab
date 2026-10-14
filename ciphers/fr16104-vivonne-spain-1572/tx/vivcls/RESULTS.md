# VIV-CLS results: a supervised sign classifier trained on f.102r + f.103r, one look at f.201r (14 Oct 2026, 00:36-01:0x UTC by date -u)

Worker VIV-CLS (Opus, account 4) for LANE VIV-KEYSTONE (account 4). PREREG `../../PREREG-VIVCLS.md` pushed f7bf5aecb (00:50 UTC)
and its Addendum A (the chosen setting) eecb5560c (00:54 UTC), both before any f.201r tile was classified for the gate or its truth
opened. Read-free (no model call); one request to openapi.bnf.fr (the c206 native region, HTTP 200). No image in git.

## Verdict: gate FAIL on (a) and (b). The registered control missed its "near chance" band by 0.010, so formally the real numbers
license nothing; the miss is in the direction that flatters the classifier (see Control), so it does not rescue the fail.

| measure (f.201r, vivonne1573-f201r-dev, covered scored positions) | as measured | flagged-excluded |
|---|---|---|
| covered scored positions (exactly one 1:1 tile, round-2 map vs passA) | 415 of 894 (0.464) | 217 |
| passA top-1 err on them | 0.154 | 0.023 |
| classifier top-1 err on them | **0.313** | 0.240 |
| fixed / broken (classifier vs passA) | 16 / 82 | 4 / 51 |
| lines improved / worsened (covered positions) | 1 / 20, p < 0.001 | 1 / 16, p 0.0003 |
| gate (a) | **FAIL** | |
| passA wrong among covered | 64 | 5 |
| truth in classifier top-3 among passA's wrong | **0.359 (23 / 64)** | 0.80 (4 / 5) |
| gate (b) >= 0.50 | **FAIL** | |
| classifier top-3 contains truth, all covered | 0.783 | 0.857 |

Official scorer (tools/tx_bench.py, hybrid = passA with the classifier's top-1 at covered tokens, `--paired passA --exclude-flagged`;
real/tx_bench_paired.txt): as measured err_true 0.253 vs passA 0.185 (unit-cost edits 165 -> 227), lines improved 2 / worsened 20 /
tied 3, p 0.0001; flagged-excluded 0.148 vs passA 17 edits -> 63, lines 1 / 16, p 0.0003.

Coverage (segmentation, reported apart from classification): round-2 map, scored positions with exactly one 1:1 tile:
f.102r 0.504 (622 / 1,234), f.103r 0.464 (496 / 1,068), f.201r 0.464 against passA's tokens and 0.447 against its own ref
skeleton. About half of every leaf's scored positions get no single pen-unit tile: the clerk joins signs (TXE3-6 found the same on
f.102r), so even a perfect tile classifier could touch at most about half of a page.

## Control (rule 3; only the labels move, so it can differ)
The same setting fitted on the 961 training labels permuted across tiles (numpy seed 20261014), step 5 rerun with its own round-2
map: covered 368; top-1 err **0.848** as measured (0.824 flagged-excluded) vs chance 1 - sum p_train p_test = **0.908**; the
registered band was >= chance - 0.05 = 0.858, missed by 0.010. Hybrid err_true 0.475 (lines 0 improved / 24 worsened). The likely
cause is the map, not the fit: the label-aware round-2 map against passA keeps a tile 1:1 more readily where its top-k agrees with
passA's sign, so the covered set leans toward positions where any label set agrees with the reader. That bias favours the
classifier in the real run too, which is why the miss does not turn the fail into a non-test.

## Training and CV (f.102r and f.103r only; train_report.json)
Labels: covered scored positions of the round-2 map against each training leaf's ref skeleton (ref_sign if in the truth set, else the
set's only member, else dropped): 538 (24 codes) and 423 (23 codes). Cross-leaf CV, 8 settings, mean top-1 error 0.354-0.391
(majority class 0.84); chosen hog+zone+topo / LDA / k 5 (0.354, top-3 miss 0.267). The f.201r top-1 error on covered positions (0.313)
sits inside the CV range: the fit transferred to a different letter of the same hand as CV said it would. It is simply about twice the
reader's error on the same positions.

## Descriptive (not gated)
Where the classifier's top-1 agrees with passA (290 covered positions) passA is wrong 29 times (0.10); where they disagree (125) passA
is wrong 35 times (0.28; classifier right 24, neither 19). Agreement with an image classifier is a weak confidence flag on a reader
token, nothing more. Commonest classifier errors (truth set <- top-1): P|s|z <- m 5, x <- m 4, P|s|z <- x 4, P|s|z <- p 4.

## Against the reader lattice
The readers' lattice holds the truth at 0.124 of their errors on f.103r (VIV-LAT); the classifier's top-3 holds it at 0.359 of
passA's errors on covered f.201r positions -- higher, but under the registered 0.50 and only on the 46% of positions a single tile
covers: 23 of passA's 165 errors on the page (0.14). Gate (b) failed; the top-3 is not fed to key_decode_lattice.py.

## Files
seg.py (tiles), run.py (train / predict / score), train_report.json, train/labels_r{1,2}_*.tsv, train/map_r2_*.tsv,
{real,permuted}/{train_labels,topk_f201r,map_r2_f201r,f201r_cls_hybrid,f201r_cls_top3,per_position}.tsv, predict.json (sha256 of the
outputs, checked by `score` before the truth was opened), score.json, tx_bench_paired.txt. Untracked and regenerable: atlas/ (tiles
and page PNGs), train/cv_*.tsv, train/topk_r1_*.tsv, */classify_all.tsv. Regenerate: the f.201r crops per images/manifest.json
"vivcls", then `python3 tx/vivcls/seg.py`, `run.py train`, `run.py predict --features hog+zone+topo --metric lda --knn 5 --tag real`
(and `--permute 20261014 --tag permuted`), `run.py score --tag real|permuted`.
