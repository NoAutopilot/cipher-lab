# Noailles c510-516 sign sorter (N4-NXS, 4 Oct 2026, account 2 worker for LANE-NEAR4)

One sign-sorter page for fr.16142 canvases 510-516 (Noailles to the King, Pera, 6 July 1574), built from LANE-RUN2's
outputs: the RUN2-NXATL family atlas (`run2/nxatl/`, k=120 clusters) and the RUN2-NXTA / RUN2-NXTB reader splits
(`run2/nxta/focus.tsv`, `run2/nxtb/focus.tsv`, `run2/nxtb/c515/disagreements.tsv`).

**The page is not committed.** It is 13.9 MB (13,930 KB; 9,863 tiles, 120 piles, 120 atlas clusters, 86 "Check these
first" tiles); this folder is already 24 MB, so committing it would cross the 30 MB line. Rebuild it on the publishing side:

    bash ciphers/fr16142-noailles-constantinople-1571/sorter/build.sh WORKDIR     # from the repo root, ~2 min

It needs numpy scipy scikit-image scikit-learn pillow opencv-python-headless, and makes 7 Gallica requests (the native
canvases, via `run2/nxatl/regen.sh`). Publish `WORKDIR/sorter/noailles_c510-516_sorter.html` with capabilities `{"db": {}}`
(see tools/sign_sorter.py's docstring). Decisions come back through `tools/sign_sorter_apply.py --clusters
run2/nxatl/clusters.tsv --atlas-labels run2/nxatl/labels_clusterid.json`.

## What the build does

- `run2/nxatl/regen.sh WORKDIR --check` re-fetches and rebuilds the atlas (4 Oct 2026 04:2x UTC: tolerant check OK, Gallica
  re-encoded the canvases again; 9,902 tiles vs 9,904 committed).
- `build_inputs.py` keeps the regenerated tile geometry but takes every tile's cluster and k1-k3 from the **committed**
  `run2/nxatl/sequences.tsv`, so pile and cluster ids are the committed atlas's (a fresh k-means run renumbers them).
  9,863 tiles are on both sides; 39 regen-only and 41 committed-only tile ids are dropped (re-encode differences, c511/c513).
- Focus: each reader (line, column) is placed on an atlas tile by (a) the atlas line on the same canvas whose crop y-centre is
  nearest, then (b) the same fraction along the line. Line offsets come out constant (NXTA c510 L01 = atlas L06; NXTB c515 Ln =
  atlas Ln; c516a L01-03 = atlas L01-03; c516b L01 = atlas L06), except **NXTB c516b L04 and L05 both land on atlas L09**
  (the blot: the atlas has 17 c516 cipher lines, the readers 18). Placement is about +-2 tiles; the page's focus note says so.
  Kept: every NXTA example position, NXTB pairs split on 2+ columns, c515 pairs split on 3+.
- Size options added to `tools/sign_sorter.py` for this page (`--thumb 64 --tile-quality 55 --page-scale 0.45
  --page-quality 45`): at the defaults the same page is 92 MB. Tiles and context lines checked by eye at these settings.
- No `--rank`: every rank the tool offers needs a key lattice or a confusion table; neither exists for c510-516.

## Checks (4 Oct 2026)

- `tools/tests/test_sign_sorter.py` ALL PASS (2 new checks for the size options); `test_sign_sorter_apply.py` ALL PASS.
- `tools/sign_sorter/browser_tests/run_all.sh` (synthetic fixtures): all 9 ok, before and after the change.
- `test_qa.js` on a c510-only build (1,437 tiles), default and small settings: ALL PASS (after the helper fix: the test's
  `bracketVisible` now applies `DATA.pageScale`).
- `test_qa.js` on this full page: no page errors; two FAILs, both judged artefacts of page size, not page faults:
  (1) "Check these first" box 2,933 px on a phone against the test's allowance of 2,860 px for 86 tiles;
  (2) step 2 shows no pile cards after the test's 600 ms wait -- the likeness vectors for 9,863 tiles take 3.5 s in headless
  Chromium (timed), and the page shows "Sorting the piles by likeness..." until then. Load time 9.4 s.
