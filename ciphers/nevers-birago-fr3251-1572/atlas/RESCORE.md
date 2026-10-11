# TX-ATLAS-B72 naming and scoring -- RESCORE (11 Oct 2026, 17:4x UTC by date -u)

**Measurement correction: box-to-position map fixed (off by one), not a new gate look.**

Job BOXMAP-RESCORE (others) for the account-3 parent (session_0198Cv8ypBfBVfRToKVWx33M). Script-only: no vision call, no
reader, no image viewed, no network beyond git. No truth file, BENCHMARK-TX.tsv row or frozen confirm item was edited.

## What was wrong

`name_clusters.py` and `score_no87.py` join atlas boxes to no.87 line-read tokens through `no87_box_token.tsv`, a DP over box
widths that never looks at a label. On 10 of its 26 lines (f178v L06, L07, L09, L11, L13, L17, L21; f179r L01, L02, L03) it puts a
stretch of boxes one token off (TXE3-9 second check; `README.md` "Label-aware box map"). The replacement is
`no87_box_token_labelaware.tsv` (`no87_map.py --label-aware`, `tools/box_token_align.py`, commit ed5d42162).

**Only the map changed.** `no87_map.py --compat OUT` (new, this job) writes the label-aware map in the old file's row convention
and columns, with the `truth` column filled exactly as `main()` fills it; it reads the clerk-sheet alignment, so it goes to a temp
directory and is never committed. On the 15 lines the fix did not touch it is identical to the old file row for row.
`score_no87.py --map FILE` and `name_clusters.py --map FILE --out DIR` are new; without them both write byte-identical files
(`score_no87.txt`, `labels.json`, `cluster_names.tsv`: checked). Everything re-runs with

    sh ciphers/nevers-birago-fr3251-1572/atlas/rescore_boxmapLA/rescore.sh     # -> rescore_boxmapLA/rescore.txt

`rescore_boxmapLA/variants.py` adds two sensitivity maps (never committed, temp only): **status-only** (the same width DP plus the
owner's sorter statuses, no label at all; it moves only L06) and **sorter-only** (statuses plus the sorter pile labels, no atlas
top-k: it moves the same 10 lines and agrees with the label-aware map on 690 of 697 shared 1:1 boxes). The sorter-only map is the
check that the label-aware map's atlas evidence is not what makes the atlas look better below.

## 1. Naming (`name_clusters.py`, 76 of 140 clusters named from verified tune tiles; 309 per-tile overrides)

| | old map | label-aware map |
|---|---|---|
| verified tune tiles (overrides) | 309 | 302 (299 in both; 10 dropped, 3 added) |
| overrides whose sign changed (tile verified at both maps, label = the token it sits on) | -- | **35 of the 299** |
| clusters named from clerk votes / model sheet read / unnamed | 76 / 64 / 0 | 74 / 63 / 3 |
| cluster codes that change | -- | 8 (2 `_`->T37, 14 T13->`_`, 37 T37->T10, 63 T83->T19, 84 T24->`_`, 89 T86->`_`, 94 T86->T49, 132 T37->T24) |

So 45 of the 309 known-answer overrides (14.6%) were the neighbouring token's sign or did not hold, all on f178v L06, L07, L09 and
L11. Note the brief's wording "the shifted tiles rarely verify" is not how it worked: verification is a property of the token (its
line-read sign decodes to the clerk letter there), so a shifted tile verifies whenever its token does and carries that token's sign
into its own cluster. The three clusters now unnamed (14, 84, 89) lost their only clerk vote; under the original procedure they would
go to an exemplar-sheet model read, which this job does not do (no model call), so they stay `_` here.

Outputs: `rescore_boxmapLA/named/labels.json`, `rescore_boxmapLA/named/cluster_names.tsv` (the committed `labels.json` is unchanged
and still cited by every consumer).

## 2. Held-out score (`score_no87.py`, 15 held-out lines: f178v L13-L23, f179r L01-L03)

| map | atlas names | signs scored | line reads err_true | atlas top-1 err_true | atlas top-3 miss | atlas = line read |
|---|---|---|---|---|---|---|
| old (= score_no87.txt) | committed | 376 | 0.056 | **0.322** | **0.261** | 0.609 |
| status-only (no labels) | committed | 375 | 0.056 | 0.320 | 0.259 | 0.611 |
| **label-aware** | committed | 370 | 0.059 | **0.103** | **0.078** | 0.816 |
| sorter-only (no atlas labels) | committed | 371 | 0.062 | 0.108 | 0.086 | 0.809 |
| label-aware | re-derived on the label-aware map | 370 | 0.059 | 0.089 | 0.086 | 0.830 |

The map-free scorer does not move: `tools/tx_bench.py --legacy` on `topk/no87_heldout_bench.tsv` (boxes in x order, aligned by edit
distance) gives 0.162 (61/376) with the committed names and 0.162 (61/376; wrong 43, deleted 16) with the re-derived names.

## Does the conclusion change?

**Yes, in part.**
- The label-blind scorer's headline, "atlas top-1 err_true 0.322 against 0.056 for the line reads; the truth is outside the top-3 on
  0.261", was mostly the map. With the right join the atlas top-1 is 0.103 against 0.059 on the same 370 signs, and its top-3 misses
  0.078, not a quarter. The sorter-only map gives the same picture (0.108 / 0.086), so this is not the atlas labels steering the map.
- **What stands:** the atlas is still worse than the line reads (0.103 vs 0.059 here; 0.162 vs 0.040 on tx_bench, map-free and
  unchanged), so "the atlas does not replace the line reads on this hand" holds.
- **What falls:** "its top-3 misses a quarter of signs, so as built it cannot be the lattice that lowers err_true" -- the top-3 holds
  the truth on about 92% of held-out signs, so the stated reason is gone (whether a lattice gains is a separate test: see
  `harvest/tx_decode/RESCORE.md`). NOTES.md "TX-ATLAS-B72" also says "Mapping shifts are a minor part (held-out kNN label matches the
  token's own label 225x, a neighbour's 77x)": the neighbour count was the map. The same count in the KM test falls from 75 to 3 with
  the label-aware map (`tools/tests/RESCORE.md`).
- Naming: 14.6% of the 309 overrides were wrong or did not hold, 8 cluster codes change; the map-free score of a re-run with the
  re-derived names is unchanged (0.162), so the naming error did not drive the headline, but every consumer of `labels.json` (classify
  everywhere, the sorter seeds, TXE3-10's pool) carries those 35 wrong override labels until `labels.json` itself is rebuilt. That is a
  decision for the lane (it changes a shared input), not done here.

Files: `rescore_boxmapLA/rescore.sh`, `rescore.txt`, `variants.py`, `named/`, `no87_heldout_LA.tsv` (held-out classify, no.87 pages,
re-derived names), `no87_heldout_LA_bench.tsv`; `no87_map.py --compat`, `score_no87.py --map`, `name_clusters.py --map --out`.
