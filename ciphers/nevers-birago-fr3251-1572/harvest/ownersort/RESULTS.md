# BIR-OWNERSORT results (4 Oct 2026, 06:53-07:1x UTC, account-3 worker)

Prereg `PREREG.md` pushed at 3f1fc54d before any score. Script `ownersort.py` (run from the repo root; deterministic, seeds in the file;
about 1 min on 4 CPUs). Disk only: 0 requests, 0 vision calls, 0 subagents.

One post-prereg fix, made after the first run's numbers were printed: step 3 counted `kept` tiles as owner picks where the base value
differs from the start pile's key value; the prereg says kept = no change. Fixed to `moved` only and re-run. The first run is kept as
`score_run1_keptbug.json` (it also FAILs every leaf: f.117r b -1.441, f.168 -1.574, f.144r -1.450). Nothing else changed.

## Step 1: three readers (`three_reader.tsv`, `agreement_by_sign.tsv`)
480 of 488 tiles carry an owner family (8 aside / bad-cut). Reader A = blind passA, B = blind passB at the tile's position.

| leaf | tiles | A=B | A=owner | B=owner | all three | owner moved |
|---|---|---|---|---|---|---|
| f.117r | 273 | 206 | 210 | 199 | 176 | 71 |
| f.144r | 88 | 68 | 47 | 47 | 41 | 57 |
| f.168 | 119 | 106 | 60 | 58 | 54 | 75 |
| all | 480 | 380 (0.79) | 317 (0.66) | 304 (0.63) | 271 (0.56) | 203 |

Of the 157 moved tiles where A and B agree, the owner's family equals that agreed read at 48; at 109 the owner overrode two blind
machine readers who agreed. 63 moves stay in the same family (a split only); 96 go to a new pile.
The 7 f.168 T24/T83 focus tiles (NEVBIR-LOOKALIKE): the owner chose T83 at none (T24 x2 kept, T24-c, T85 x2, T60-c, T90).

## Step 2: the 52 -> 105 split test (`power.tsv`, `splits.tsv`)
Power control first (synthetic merges of two real sheet piles with different values, the Z part split back out, 50 per size, the
same random re-split control): passes 2/50 at k=1, 5/50 at k=2, 5/50 at k=3, 9/50 at k=5 -- power 0.04-0.18, i.e. at the test's own
false-positive rate. The LM-gain test cannot tell a real homophone split from an over-split at these pile sizes (largest new pile 11 tiles).
Verdicts (57 new piles): 36 untestable at this N (sheet families; owner-only distinctions, flagged; tiles take the family's key value
at M at most), 21 owner-only (off-sheet families X_NEW/X_S/X_K, or no tiles left in the parent: T52-b, T52-c, T89-b). 0 SUPPORTED,
0 merges supported. No split is a recorded data-backed merge or distinction.
Mixed new piles (members from several start piles): T60-c 11 (T65 x6, T51, T60, T85, T24, T36), X_NEW-l 9 (T19 x4, T92 x2, X_NEW,
T58, T96), T66-b 6 (X_S x3, T66 x2, X_NEW), T60-b 5. These cross the key's value boundaries; the owner is grouping by a shape cue
the key does not use.

## Step 3: re-decode gate (`changes.tsv`, `score.json`; BIR-OWNER rule, seed 20261004)
| leaf | owner changes (value / U) | S / M | (a) base | (b) owner | (c) control p95 | (b) rank in 201 | gate |
|---|---|---|---|---|---|---|---|
| f.117r (fr) | 42 / 3 | 4 / 38 | -1.215 | -1.365 | -1.315 | 58 | FAIL |
| f.168 (it16dip) | 49 / 4 | 1 / 48 | -1.149 | -1.628 | -1.253 | 201 | FAIL |
| f.144r (it16dip) | 35 / 3 | 2 / 33 | -1.418 | -1.450 | -1.403 | 21 | FAIL |
| pooled | | | -1.239 | -1.445 | -1.321 | | FAIL |

Every leaf fails: the owner's complete sort makes each text worse than the base, and on f.168 worse than all 200 random look-alike
change sets (BIR-OWNER's partial save: rank 199). Nothing applied; the settled inventory for decoding is the base inventory unchanged.
Judge on the (b) texts, for the record:

    f144r b  FAIL language: score=-1.45,  null_p99=-1.596, real_p05=-0.975, real_median=-0.829, mode=both, N=92
    f168  b  FAIL language: score=-1.628, null_p99=-1.67,  real_p05=-0.942, real_median=-0.82,  mode=both, N=118
    f117  b  FAIL language: score=-1.365, null_p99=-1.793, real_p05=-0.891, real_median=-0.789, mode=both, N=276

## Step 4: recut list (`recut.tsv`)
8 tiles, no value guessed: bad-cut f117 L01.21, f144r L05.13, f168 V02.7; aside f117 L03.27, L05.27, L06.23, f144r L03.8, f168 V01.1,
each with its `tools/iiif_lines.py` recut command (f.117r ark btv1b9060232m canvas 118; f.144r/f.168 ark btv1b9060248g canvases 146, 171-172).

## Re-score, orchestrator, 4 Oct 2026 (owner challenged the verdict)
Scoring flaw in v1: a pile the owner started with "None of these: new sign" is named by the page after the tile's *old* pile
(T60-c, X_NEW-l, ...), and `fam()` scored it as that old pile's letter. 37 of 136 changes came from such piles; 9 of them
(T60-c: 6 T65 tiles, 1 T60) were filled mostly from other piles. `ownersort.py --new-piles-unknown` scores those piles '?'
(an owner-only new sign) and writes `v2/`. Result: **f.144r PASS** (b -1.376 > base -1.418 and > control p95 -1.441,
rank 5/201); f.117 FAIL (rank 69/201, indistinguishable from random change sets); f.168 FAIL (rank 201/201).
Caveats on what the remaining FAILs can say: every base text already FAILs the judge (about -1.2 vs real_p05 -0.9), so
the gate compares two unreadable texts; and f.168 is the leaf where the 1572 key was never licensed (rank 13-36/201),
so "worse under this key" there is weak evidence against the sort. Tile-to-position mapping checked: the published start
pile equals the base sign at the mapped position for 251/277 (f.117), 87/90 (f.144r), 113/121 (f.168) tiles.
v1's "nothing applied" stands until a per-tile adjudication (value-blind image check of the 109 tiles where the owner
overrode two agreeing machine readers) says who is right tile by tile.
