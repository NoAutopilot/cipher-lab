# RUN2-NXATL -- family atlas for c510-516 (+ c262 known answer)

LANE-RUN2 wave 1, account 1 worker, 4 Oct 2026 (box from 02:46 UTC). Brief: `.claude/briefs/runs/2026-10-04-acct1-run2-wave1.md`.
This is TRANSCRIPTION.md's atlas step (segment -> over-split cluster -> top-3 classify) for the 7 July 1574 letter to the King
(fr.16142 canvases 510-516, Gallica `btv1b9060927q`). Nothing here decodes, aligns to Dupuy 521 or applies key.tsv to
c510-516 (that is wave 2, RUN2-NXALN, kept blind).

## What was done

1. **Images.** Native canvases f510-f516 fetched once (7 requests, 2 s apart, all HTTP 200, ~4.5 MB each; kept in scratchpad,
   re-fetched by `regen.sh`). c262 uses the committed NX-RECUT crops (`images/c262rc_L*_s*.jpg`), no request.
2. **Line bands.** `tools/iiif_lines.py --follow-slope 300 --slope-margin 15 --max-width 2400 --overlap 100` per canvas, with
   `--centres` taken from the row-ink profile of the left 600 px of each text block (`cen.py`; the full-width autocorrelation
   missed lines on these sloping pages, e.g. c512 jumped 254->575). Output pasted in `iiif_lines_out.txt`; regions and centres
   in `regen.sh` / `line_centres.json`. Overlays of all 7 canvases checked in one sheet: one text row per band.
   `git status` after every run: clean (crops written to scratchpad only).
3. **Clear text located** (`clear_lines.json`):
   - c510: L01-L04 clear (date, "Du S^r de Noailles au Roy", "Sire. La derniere depesche...", "a Sa Ma^te ..."); L05 is mixed:
     clear "Jours au paravant La reception d'icelle que" then cipher -- the first 22 tiles of L05 (through the last wide cursive
     tile) are dropped; **cipher starts at c510 L05, tile 23**.
   - c516 does NOT open with a clear lead-in: L01-L03 are cipher, **L04-L05 are clear** ("Sire quelque jours ... / Apres l'avoir
     entendu ce qu'il plaist a V. Ma^te me mander"), L06-L19 cipher (L09-L10 under the ink blot: L10 only 16 tiles, x < 1838),
     **L20-L23 clear** (closing and subscription, "... de Pera ... le vj^e de Juillet 1574"). L19 may end in a short clear tail
     (the overlay suggests "... sera ..."); its tiles are all kept and flagged here for wave 2 (grade M).
   - The c510 lead-in boundary and the c516 clear lines rest on one look at the overlay sheet plus a per-line count of wide
     cursive tiles (rw > 2.2), not on a reader's transcription.
4. **Segmentation** (`tools/glyph_atlas.py segment`, default mode, one page per line strip), then per strip (`filt2.py`): keep the
   segmented line nearest the strip centre; drop the right-hand overlap of _s1 and left-hand overlap of _s2 (50 px each side);
   drop tiles centred more than 0.9 sign heights off the line (neighbour-line and gloss intrusions) and specks (h and w under 0.5).
   Sizes are in units of the **leaf's** median sign height (`renorm.py`), because the per-strip estimate collapsed to 6-34 px on
   strips with blots or little ink (c510 L01-L03, c512 L01, c515 L10-11 s2, c516 L10 s2).
5. **Cluster** k=120 (deliberate over-split; c262's reconciliation uses 41 labels), marks k=24; **classify** every tile against all
   others with `--topk 3` (labels = the cluster ids themselves, `labels_clusterid.json`), so k1-k3 are cluster ids, not names.
   kNN top-1 = own cluster for 9,369 / 10,307 tiles (90.9%). Cluster sizes 20-217 (median 78).

## Segmentation check on c262 (step 3 of the brief)

Tiles per line vs NX-RECUT's reconciled count (`witness/c262rc_recon.tsv`):

| line | L01 | L02 | L03 | L04 | L05 | L06 | L07 | L08 | L09 | L10 | all |
|---|---|---|---|---|---|---|---|---|---|---|---|
| reconciled signs | 36 | 40 | 25 | 41 | 44 | 40 | 42 | 39 | 38 | 39 | 384 |
| tiles | 41 | 45 | 21 | 44 | 43 | 43 | 42 | 41 | 41 | 42 | 403 |
| ratio | 1.14 | 1.12 | 0.84 | 1.07 | 0.98 | 1.07 | 1.00 | 1.05 | 1.08 | 1.08 | **1.05** |

All 10 lines within the 25% acceptance (RUN1-SEG's); range 0.84-1.14. **Caveat, stated plainly:** the intrusion filter (0.9
sign heights) and the speck rule were chosen on this same block (before them: 453 tiles, 1.18, three lines over 25%), so this is an
in-sample check, not a held-out one. It shows the hand segments into roughly one tile per sign; it does not show which tiles are
split signs and which are merged pairs (27 surplus tiles and 8 unmatched labels in the alignment below).

## Sign counts (the first count of c510-516)

| leaf | cipher lines | tiles | est. signs (tiles / 1.05) |
|---|---|---|---|
| c510 | 37 | 1,437 | 1,369 |
| c511 | 39 | 1,534 | 1,462 |
| c512 | 41 | 1,626 | 1,549 |
| c513 | 40 | 1,625 | 1,548 |
| c514 | 39 | 1,533 | 1,461 |
| c515 | 40 | 1,538 | 1,465 |
| c516 | 17 | 611 | 582 |
| **c510-516** | **253** | **9,904** | **~9,440** |

FT-D's estimate was 9,750; the tile count is 9,904 and the c262-ratio estimate ~9,440. Short lines worth a glance in wave 2:
c512 L21 (19 tiles), c515 L11 (19), c516 L09-L10 (blot).

## Provisional names from c262 (grade M)

`c262_align.py`: hard-EM Needleman-Wunsch between each c262 line's tile clusters and the reconciled labels (gap 2, score
log P(label|cluster)/P(label)); 4 iterations, 376 tiles matched, 27 surplus tiles, 8 unmatched labels. 74 of the 120 clusters
occur on c262 and get a majority label (`cluster_provisional_names.tsv`, with support and purity); 46 clusters never occur on c262.
Only 17 clusters have support >= 3 and purity >= 0.6 (about 1,300 tiles of the whole set).

Descriptive control (not a gate; nothing is licensed by it): weighted purity of the cluster->label table, real 0.593, against the
same EM run with the cluster ids permuted among the c262 tiles (counts kept), 20 seeds: 0.311-0.356 (max 0.356). The clusters
carry the reconciler's distinctions well above chance, but a purity of 0.59 also says many clusters mix labels (k038, the
second-largest on c262, is 0.18 pure). These names rest on one reconciler's rulings (NX-RECUT) and an unchecked alignment;
they are provisional, grade M, and are not in `sequences.tsv`.

## Files (all in `run2/nxatl/`)

- `sequences.tsv` -- every tile in reading order: leaf, line, pos, tile id, x along the line, k-means cluster, marks above,
  k1-k3 cluster ids with distance and vote share.
- `sign_counts.tsv`; `clear_lines.json`; `line_centres.json`; `iiif_lines_out.txt` (the crop command's output).
- `clusters.tsv` (every tile and mark -> cluster), `atlas.tsv` (count, leaves, 12 exemplar ids and marks seen per cluster),
  `labels_clusterid.json`.
- `sheets/atlas_k000-019.jpg` ... `atlas_k100-119.jpg`: exemplar sheets, 20 clusters per image, 12 exemplars each, cut from the
  native strips (JPEG q40, 800 KB total). Sorter-ready: `tools/sign_sorter.py --atlas-topk <classify_all.tsv> --clusters
  clusters.tsv --atlas labels_clusterid.json --pages <WORK>/atlf/pages.json` after `regen.sh` (the page images live in the work dir,
  not the repo). Not published by this worker.
- `c262_align.py` -> `c262_tile_alignment.tsv`, `cluster_provisional_names.tsv`.
- `source_manifest.json`: sha1, size and URL of the 7 canvases the committed outputs were built from. Gallica served different
  bytes for c513 and c514 on a second fetch 14 minutes later (re-encoded; the sha1s of both fetches are recorded), so a refetch is not
  byte-stable: `regen.sh` runs the exact `--check` when the canvases match the manifest and a `--tolerant` check (per-leaf tile
  counts within 1%) when they do not. Refetch test: c513 1,625 -> 1,621 tiles, every other leaf identical; tolerant check OK.
- Exact check passed: `bash regen.sh <work dir holding the manifest canvases> --check` -> "check OK" (4 Oct 2026, 03:0x UTC).
- `regen.sh WORKDIR [--check]` re-fetches, re-cuts, re-segments, re-clusters and rewrites (or checks) `sequences.tsv` and
  `sign_counts.tsv`; helpers `cen.py`, `renorm.py`, `filt2.py`, `build.py`, `make_sequences.py`.

## Not done / where it was not found

- No reader named any c510-516 sign; no decode, no Dupuy alignment, no key.tsv (by design, wave 2 blind).
- No tile-level eye check of the segmentation on c510-516 (only the band overlays); merged/split tiles are unknown beyond c262's
  count ratio.
- The c262 alignment is not checked by eye.

Requests: gallica.bnf.fr 14 (7 native canvases + 7 again by the `regen.sh` end-to-end test in a fresh directory), all 200.
Subagent calls 0. Opus looks: 2 (a 7-canvas contact sheet and the 7-canvas overlay sheet; the brief allowed 1 -- one over).
