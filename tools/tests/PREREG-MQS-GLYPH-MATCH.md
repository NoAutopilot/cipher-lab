# PREREG MQS-GLYPH-MATCH (LANE MQS-2, account 4) -- written 9 Oct 2026 07:22 UTC by date -u, pushed before any score

Option under test: `tools/glyph_atlas.py match --out ATLAS --page NAME=IMAGE ... [--exclude-page P ...] [--k 140]
[--shuffle-labels SEED]` -- an image-only glyph-shape match of candidate leaves against a sign atlas (research/
MARY-STUART-TALK-2026-10-09.tsv row M03, "second-wave sweep of the sender's and recipient's series for the same glyph
set"; Lasry, Biermann and Tomokiyo 2023, Cryptologia 47:2, p.108 n.38, p.190 n.345). Shapes only: no cluster names,
no labels.json, no codes, no values are read or rendered; the atlas side is the committed segmentation's bitmaps,
re-clustered unsupervised. Nothing value-bearing is rendered (ASKS 118). Hosts: none. Vision calls: none. No status,
key, reading or AUDIT.md change.

## Statistic
Atlas = `ciphers/nevers-birago-fr3251-1572/atlas` signs.tsv + bitmaps.npz, minus every `--exclude-page`. Features =
the `classify` features (HOG + log rh/rw), StandardScaler + PCA(40) fitted on the atlas signs only; queries are
transformed with that fit. k-means k=140 (the atlas README's own k), SEED fixed. Per cluster: centroid, and radius
r_c = the 0.90 quantile of its members' distances to the centroid (clusters under 3 members take the median radius).
**IR(leaf)** = share of the leaf's segmented signs (fresh `segment`, default parameters, the whole image) whose distance
to the nearest centroid is <= that cluster's r_c. Higher = more of the leaf's shapes sit inside the atlas's own
shape clusters. Margin = IR(held-out) - max IR(10 negatives).

## Known answer (leave-one-leaf-out, not circular)
Held-out positive: fr.3252 f.117r (`ciphers/birago-fr3252-1571-72/images/f117/src_..._f118_4380_1400_3150_1300.jpg`),
removed from the atlas (all 291 f117r rows) BEFORE scaler, PCA and k-means are fitted, then segmented fresh as a query.
Reproduction check first: the fresh segmentation of f117r must give 291 +- 5 signs (atlas count); else the
segmentation parameters drifted: stop, non-test.
Negatives: 10 non-sibling leaves on disk, one per folder, none Birago/Nevers/fr.3251/fr.3252/fr.3993 (fr.3993 is the
Nevers papers; excluded as a possible sibling hand), no debosnys:
1 fr3151-seure-1558 f.75 crop; 2 fr5761-election-1519 canvas104 f.50v; 3 spinelli-beinecke-c1515 p1_clean;
4 wvo-11106-bergh-1572 crop_p2_top; 5 dupuy452-carpi-1520 canvas23 f.20 cipher; 6 fr7129-villeroy-bongars-1604 f268r
canvas541; 7 fr16045-pisany-rome-1585 f562 crop; 8 sforza-pusterla-1447-f13 f15 crop; 9 fr2933-salviati-1525 canvas56
native; 10 armstrong-madison-1808 one shorthand line strip set is NOT used (line strips, not a leaf); instead
sforza-italien1584-1447 pusterla/images/src_f38_f41a.jpg.
(Exact paths in tools/tests/MQS-GLYPH-MATCH-results.tsv.)

## Gates (all three for PASS)
- G1: IR(f117r) ranks 1 of 11 under the real-label LOO atlas.
- G2: margin >= 0.05.
- G3 (shuffled-label null, 20 seeds): atlas cluster labels permuted across atlas signs (sizes kept), centroids and radii
  recomputed from the permuted labels, all 11 leaves re-scored; real margin > the 95th percentile of the 20 null
  margins. Why this null can fail differently: IR is computed from per-cluster centroids and radii, which are
  functions of the labels; permuting labels moves every centroid toward the global mean and widens every radius, so
  IR changes for every leaf and the target's margin can shrink, grow or hold. If it holds (G3 fails), the cluster
  structure adds nothing over a global "near the atlas cloud" test and the option ships `weak` with that sentence.
- Ceiling: no restarts exist to inflate (k-means seed fixed); expected IR(f117r) roughly 0.6-0.85, negatives 0.2-0.6
  (a guess, not a gate). If every leaf scores above 0.95 the statistic has no headroom: non-test.

## Secondary (descriptive, no gate; reported)
Leave-one-leaf-out for every Birago atlas leaf (f174v and f174vB held out together, they are one leaf), real labels
only, query = that leaf's own stored atlas rows (f184v/f185r images are not on disk): rank of each held-out leaf
among itself + the 10 negatives. Reported as "ranked 1 in n/17 folds".

## Outcomes
PASS -> shelf `controlled-only` (one known answer, one hand). Any gate missed -> shelf `weak` with both numbers, option
kept, nothing run on a target from it, not re-briefed (rule 3 third-attempt clause applies only to repeats).
