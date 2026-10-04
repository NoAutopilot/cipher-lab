# LL-RECUT (account 3 worker) -- 4 Oct 2026 16:3x UTC (account-3 orchestrator; owner: "I can do these, but they need to be efficient")
Target: ciphers/fr16106-vivonne-longlee-1579/sorter (the Longlee f.101v sorter, published at https://claude.ai/artifact/CJoBEX8sy858LwSG868prC,
no owner moves yet). Problem (owner, on the page): many tiles straddle two signs or cut one in half -- as on Pisany f.75 (f75_L08_02 covered the looped l
AND the b beside it -- because build_inputs.py fitted ink-profile blobs to the readers' column COUNT (README "Tiles ... approximate").
Also the lines slope ~160 px across the region, so the context strip under the big view shows the line ABOVE and the brackets fall
off-screen. Today's tighten_tiles.py only trimmed vertically; it cannot fix horizontal cuts. Read the sorter README, build_inputs.py,
tighten_tiles.py, TRANSCRIPTION.md, and tools/glyph_atlas.py's docstring (segment, --cursive) first.
Goal: a page the owner can sort quickly, where ONE TILE = ONE SIGN.
1. Deskew: one horizontal strip per cipher line (rotate/shear along the line trace build_inputs.py already computes), so each sorter
   page is one straight line. The context strip and "lines above and below" then show the right line.
2. Segment each deskewed strip into signs by their own ink (tools/glyph_atlas.py segment, --cursive if the hand joins; check the debug
   overlay on 3 lines, at most 2 Sonnet vision calls to check it). Split touching signs at ink minima; prefer over-splitting a little
   (the owner merges fast) over two-sign tiles. Report tiles per line vs the readers' column counts (fit.tsv 46-55).
3. Starting piles, value-blind: map each new tile to the reconciled readers' label at that position (by x order along the line,
   tools/reconcile_passes.py draft) where the alignment is clear; where it is not, put it in the pile of its nearest shape cluster
   (glyph_atlas atlas/classify) and in the focus box. Aim: most tiles already right so the owner mostly confirms. Focus box <= 40,
   ranked by how much the answer matters (frequent shapes first).
4. Rebuild with build.sh (same pile naming, no values on the page), run tools/sign_sorter/browser_tests/run_all.sh with the built page
   (all ok), and commit inputs/scripts + README update; HTML stays in scratch for the orchestrator to publish. Keep the old signs.tsv
   for the record. Page under ~4 MB.
5. In the final paragraph: tiles/line before and after, a 20-tile spot check from the debug overlay (one sign per tile: how many of 20).
Disk only (images on disk), no network. Model Opus 5.5. Cap USD 6, box 60 min (stop before a step that would cross 80% of either).
ROOM claim/done via tools/room.py. Do not change any reading, key or other target.
ADDENDUM (orchestrator): the same fix was just done on Pisany -- read ciphers/fr16045-pisany-rome-1585/sorter/recut.py, small_pile.py
and build.sh and REUSE them (generalise into a shared tool option if the code is target-specific; Usage 8), do not rewrite from scratch.
Include the SMALL pile (tiny tiles) and a focus of 30 with one-line captions and a short --focus-note, as the Pisany build does
(test_qa's phone focus-height check). Spot check: make a 40-tile montage and count single-sign / speck / double tiles honestly.
Longlee's lines may not slope like Pisany's; deskew only if needed. Cap USD 6.
