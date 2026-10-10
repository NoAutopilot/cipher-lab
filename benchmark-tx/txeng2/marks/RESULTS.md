# MARKS-DEV2 -- the ':' mark-class detector, read-free half, on vivonne1573-f102r-dev2 (TXE2-MARKS, 10 Oct 2026)

For LANE TX-ENGINEER-2 (account-4). PREREG: benchmark-tx/PREREG-txeng2-21.md section MARKS-DEV2 (push c29543f04). Run 03:00-03:1x UTC
10 Oct 2026 by date -u. Read-free: no reader call, no vision call, no crop or overlay viewed; the dev2 truth and passZ_dv1 were opened
only by score.py and never printed; nothing of f.103r touched.

**Verdict (as declared): FAIL read-free** -- recall 0.000 (0 of 84 ':' positions) at precision undefined (0 candidates); lift undefined
(no position lies near a candidate), so the null p95 / max are undefined too. The gate needs recall >= 0.70 at precision >= 0.50 AND lift
> null p95; neither half is met.

| step | number |
|---|---|
| lines / crops | 37 lines, 74 crops (c105_f102r_L01..L37_s{1,2}.jpg) |
| component boxes (OL1-BOXES recipe, ghost rule unchanged) | 1698 (127 of them glyph_atlas marks) |
| boxes with larger side under 0.35 x the line's median sign height | 30 of 1698 (max-side/median quantiles: 1% 0.32, 5% 0.39, 10% 0.49) |
| ':' candidates | 0, on 0 lines |
| ':' truth positions (ref_sign ':', by script) | 84 |
| recall / precision, +-1 (gating) and exact | 0.000 / undefined; 0.000 / undefined |
| unflagged positions / position errors / insertions (fixed scorer, no label map) | 679 / 43 / 41 -- reproduces the registered triple (norm_map gives 679 / 33 / 41; not used) |
| lift (84 errors near a candidate / 679 positions near a candidate) | undefined (0 / 0) |
| null, 200 within-line shuffles, seed 20261010 | p95 undefined, max undefined |
| box count vs position count (36 truth lines; L14 has no truth rows) | 1653 boxes vs 1848 positions on the 36 lines; boxes < positions on 32 lines, > on 4 |

Why nothing fires (read-free diagnosis, from box geometry only): under the OL1-BOXES recipe almost no component is small enough --
30 of 1698 boxes are under 0.35 x the median sign height, and none of those forms a stacked, x-overlapping, stroke-free pair.
`tools/glyph_atlas.py segment` (default mode) merges same-line x-overlapping components whose vertical gap is under 0.6 x the median
height (--merge-vgap) and drops components whose side is under 0.12 x it (--min-area), so the two dots of a ':' most likely come out
as one box (or none), which this two-component rule cannot see. The count gap (boxes under positions on 32 of 36 lines) is in the same
direction. This is an inference from the segmenter's documented parameters, not a check on any image. The PREREG fixed the recipe
("no ghost rule change"), so no segmenter parameter was changed and no second rule was run: a different instrument (for instance a
single-component ':' shape test on the merged box, or a segment run with --merge-vgap lowered) would need its own PREREG.

Doubt list: doubt.tsv has 0 rows (it lists only rule candidates; no truth-derived row is written to a sorter feed).

## Files, commits and hashes
- rule.py, score.py, run.sh committed BEFORE any run against the truth: 669154460.
  rule.py sha256 1b7919176831941e8bf06bacbcfadcebd83cfff9ad773aa8019c48cddeac309b;
  score.py sha256 844fe968a68e88b3276e5f68fa6963a5f895a31f67ea2430253e2b4bf43cb9a1.
- boxes.tsv, candidates.tsv, doubt.tsv committed BEFORE scoring: 4dcd1cfad.
  boxes.tsv 98b5ca62ffcad35a5185a2cd79c9a7474cdfeefe991e73381789bfce475a9726;
  candidates.tsv 523226c5d1d447ed47a94528639f5469b72808f0f1a62fcecadae4561f0e9ea2 (header only);
  doubt.tsv 5098e3e3c80bdcac7ad2eb80e05fc73b8a523cd1c384b06ca940d5bbcb2e68c2 (header only).
- result.json (score.py output; counts and rates only, truth and pass sha256 inside):
  c48ed85a490649b8d2bec9d942a2b38b40f446c1b165e9080a7b524b9213a3eb.
- Regenerate: `sh benchmark-tx/txeng2/marks/run.sh && python3 benchmark-tx/txeng2/marks/score.py` (needs opencv-python-headless).

Openings of eval truth: 0
dev openings: 1 (by script)
