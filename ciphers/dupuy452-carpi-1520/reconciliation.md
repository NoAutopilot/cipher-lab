# Reconciliation: Raince to Madame, Dupuy 452 ff.28r-29v (23 Sept 2026)

Reconciliation worker, 23 Sept 2026, 23:18-00:05 UTC. Inputs: the 160 line crops f28r/f28v/f29r/f29v
(images/crops/), passA.tsv and passB.tsv (two blind passes), and two new gutter strips (below). Output:
`ciphertext.txt` (the reconciled sign sequence), `inventory.tsv`, `glyphs/contact_sheet.jpg`,
`glyphs/overrides.tsv` (every sign settled by eye) and the scripts in `glyphs/`. The earlier
reconciliation.md (f.20, Carpi) is now `reconciliation_f20_carpi.md`, and the earlier ciphertext.txt
(f.20) is now `ciphertext_f20_carpi.txt`. Both are unchanged. No decoding, no key, no solver.

## Gate

| | value |
|---|---|
| final tokens | **5,725** (f28r 1,426, f28v 1,987, f29r 1,950, f29v 362) |
| vs pass A (4,797) | **+19.3 %** |
| vs pass B (5,905 parsed sign tokens, of which 513 are overlap double-reads) | -3.0 % |
| sign types | **50** (plus 2 tokens typed `?`) |
| uncertain tokens (`?` suffix) | 365 (6.4 %) |
| CLEAN (passes' count within 5 % and < 40 types) | **NO** |

The count gate fails because pass A is short, not because the sequence is unstable. Pass A read the
bands f28r L01-L21 and f28v L02-L13 as "merged 2-line bands" and recorded only the left crop
segment's signs (13-15 per line of about 53). 1,796 segmented signs lie where no pass A crop reading
reaches. Pass B, which read both segments, lands within 3 % of the final count once its overlap
double-reads are removed.

The type gate fails because the page carries about 22 rare signs (1-33 occurrences each) besides
28 common ones. See "What would make it clean".

## Method

1. **Segmentation** (`glyphs/segment.py`). Each page column is rebuilt at native resolution from the
   crops (boxes in the crops manifest). Then: divide out the paper background; threshold at 0.62 of
   the local paper; remove vertical rules at least 121 px tall (the page edge and gutter line);
   take connected components; drop specks, slivers and detached ρ-tails. Each component goes to a
   text line by fitting a straight line y(x) per text line (3 iterations), because the lines slope
   up to about 40 px across a column. Components overlapping in x are merged when one is small or
   they are stacked vertically.

   The cipher span is in `glyphs/cipher_span.json`: f28r line 12 from x=6480 (the sign after
   "escript /") to line 37; f28v lines 1-36; f29r lines 1-36; f29v lines 1-7 up to x=3520 ("... K",
   before "(."). This agrees with both passes' own statements of where the block starts and ends.
2. **Clustering** (`glyphs/cluster.py`). HOG features plus size and placement, k-means with a
   deliberate over-split (72 clusters). The clusters were labelled by eye from montages
   (`cluster_labels_run1.json`), and rare shapes were labelled per sign (`manual_labels_run1/2.json`).
   Their cores became 2,758 prototypes (`prototypes.npz`, built by `make_prototypes.py`).
3. **Classification** (`glyphs/classify.py`). k=5 nearest prototypes on L2-normalised HOG plus a
   blurred 24x24 bitmap, with a light size term. Whitened PCA was dropped: it put z on I and 7 on T
   (4 % against 51 % on the hard cases; prototype 4-fold CV 98 % either way).
   - Topology settles o/θ (holes: 1 vs 2) and Λ/Δ (0 vs 1 hole).
   - "Fragment" can win only for marks under 24 px or at most 16 px high.
   - Touching pairs are split by a classifier-scored vertical cut, or by a ρ-tail rule; 10 splits
     were accepted automatically.
4. **Alignment** (`glyphs/reconcile.py`). Each crop file x line_no of each pass is aligned to the
   segmented signs of that physical line inside that crop's x-window. So the 700 px overlap
   between the _s1 and _s2 crops of a band is absorbed: a sign in the overlap can collect a reading
   from each crop.
   - The alignment is global on the pass side and free-ended on the page side.
   - Scores are log P(code | type), re-estimated over 4 rounds from a legend-based seed.
   - Pass A composite tokens ([TO], [ov], [zv] ...) were expanded into their parts, as the reader
     suggested.
5. **Settlement.** Disputed signs were looked at on the page crop (montages with context) and
   recorded in `glyphs/overrides.tsv`: 127 rows (117 retypes, 10 two-sign splits). Everything
   else takes the clustered type. A token is marked `?` by the rule in `glyphs/build.py`.
6. **Rule 7.** `python3 glyphs/build.py --check` rebuilds everything from the crops (about 35 s) and
   exits 1 if `ciphertext.txt` or `inventory.tsv` is stale. It passed at commit.

## Agreement

| measure | count | rate |
|---|---|---|
| segmented signs read by pass A / by pass B | 3,790 / 5,306 | 66 % / 93 % of 5,725 |
| pass A reading consistent with the final type | 3,109 / 3,790 | **82.0 %** |
| pass B reading consistent with the final type | 4,957 / 5,306 | **93.4 %** |
| signs read by both passes | 3,678 | |
| both passes' codes map to the same type (each code's majority type) | 2,547 / 3,678 | **69.2 %** |
| both passes consistent with the final type | 2,961 / 3,678 | **80.5 %** |

"Consistent" means the final type takes at least a tenth of that pass code's aligned readings
(`confusion_A.tsv`, `confusion_B.tsv`). The strict A-B figure is depressed mainly by the codes each
reader used for two or more types (class 3 below).

## Classes of disagreement, and how each was settled

1. **Coverage gaps in the crops (neither pass could see them): 70 signs.**
   - f28v's text runs past the crop column's right edge (crops stop at x=4300; ink reaches about
     4390). f29v's cipher lines run past 4150 (ink to about 4260).
   - Settled by fetching the two gutter strips once from Gallica IIIF (2 requests, 23 Sept 2026,
     descriptive UA, both 200). They are `images/gutter/f35_x4200_y400_w300_h4900.jpg` and
     `f36_x4050_y500_w350_h1200.jpg`, registered to the crops at offset (0,0) (mean abs. difference
     1.6 grey levels).
   - These 70 signs rest on the clustering alone.
2. **Pass A's unread right halves: 1,796 signs with no pass A reading** (f28r L07-L21 and f28v
   L02-L13, _s2 content). Settled by pass B plus clustering.

   A further 184 signs are uncovered by both passes' alignments outside the gutter. These are whole
   right halves of a few f28r lines (13, 16) and f28v lines, where the band's line numbering and the
   segmented lines did not pair up. They rest on the clustering; they are not marked uncertain
   unless the classifier is unsure.
3. **Codes spanning two or more types (systematic under-splitting by a reader).** Settled by the
   clusters: each pair was checked in shape montages and in page context, and the split is visible
   in `glyphs/contact_sheet.jpg`.
   - A `[phi]` = psi 353 + arr 235
   - A `[lam]` = l 311 + lam 172
   - A `[rho]` = rho 134 + q 126
   - A `[dag]` = db + dbar
   - A `[box]` = box + X 38
   - B `C01` = arr 136 + q 91 + rho 83 (f28r/f28v only)
   - B `ρ` = rho 115 + q 100 (f29r/f29v)
   - B `A` = arr + A
   - B `C06` = arr + psi + ankh
   - B `C11` = db + dbar
   - B `C14` = w + pi
   - B `3` = three + yogh

   Neither pass separated q (ball on a plain stem) from ρ (loop with a long tail curling left under
   the previous sign), yet the shapes are distinct on every exemplar. That is the most consequential
   split for the next worker, and it is a judgement from the image, not from either pass.
4. **Reader drift.** Pass B used `C01`/`C06` for the arrow sign on f28r-f28v and `A` on f29r-f29v,
   and `C01` then `ρ` for q/ρ. Settled as in class 3; the drift is why B's code table cannot be used
   as a key.
5. **Pass tokens aligned to no segmented sign.** Pass A 626, pass B 86. Mostly reading noise or
   double reads. At 15 places both passes read an extra sign at the same spot. Each was checked in
   context: most were signs my segmentation had put on the neighbouring line (fixed by the slope fit)
   or had lost against the gutter shadow (fixed by rule removal). The rest are ordinary misalignment.
6. **Signs covered by a pass but skipped by it.** A 139, B 198. After the fixes, the 22 that both
   passes skipped were checked. They are real signs at crop edges (both readers skip a sign cut by
   the crop boundary), not segmentation noise; detached ρ-tails were removed from this set.
7. **Merged or split signs.** 10 automatic splits and 10 by-eye splits in overrides.tsv (v+ρ, I+arrow,
   z+arrow, X+f). Some wide ρ boxes still carry a touching neighbour (ρ's tail joins the sign before
   it). Where the passes and the type disagree, they are marked `?`.
8. **Individual type conflicts.** 127 settled by eye (overrides.tsv; the "was" column gives the
   classifier's type). The rest are marked `?` (365).
   - The most frequent uncertain types are ankh 53, q 33, l 32, arr 30, sq 26, lamL 18, psi 12.
   - ankh/q and lamL/lam are the pairs where the passes never distinguish and the classifier is least
     sure.

## Remaining uncertain positions

- Every `?`-suffixed token in ciphertext.txt (365).
- The 2 tokens typed `?`.
- The 70 gutter signs and 184 unaligned signs, which rest on one source (the clustering).
- Allograph questions left open for the solver. These are shape distinctions that are real on the
  page but may not be distinct cipher signs: lamL/lam, dbar/db, ankh/q, pi/w, yogh/three, zslash/z,
  x/X, dash_o/o, oplus/th, K/R, H (includes a broken-stem form).

## What would make it clean

- **Count.** A third pass on exactly the part pass A did not read: the _s2 crops of f28r L07-L21 and
  f28v L02-L13, about 1,800 signs. Alternatively, accept pass B plus clustering as the second
  witness there. Re-cut crops for f28v (x 4300-4400) and f29v (x 4150-4260) so a human pass covers
  the gutter signs.
- **Types.** No further pass will bring 50 types under 40: 22 types occur 1-33 times and are distinct
  on the page. The count drops under 40 only if the solver finds, by frequency and context, that the
  allograph pairs above are one sign (11 merges give 39). That is a cryptanalytic judgement, deferred
  to the next worker. A third pass cannot settle it.

## Requests

- gallica.bnf.fr: 2 (IIIF region fetches, 1.5 s apart, both 200).
- No other host. No subagents used.
