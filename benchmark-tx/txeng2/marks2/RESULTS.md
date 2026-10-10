# MARKS-DEV2b -- the same ':' rule on raw components, read-free half, on vivonne1573-f102r-dev2 (TXE2-MARKS2, 10 Oct 2026)

For LANE TX-ENGINEER-2 (account-4). PREREG: benchmark-tx/PREREG-txeng2-21.md section MARKS-DEV2b (worked from push d326cc43f).
Run 03:42-03:44 UTC 10 Oct 2026 by date -u. Read-free: no reader call, no vision call, no crop or overlay viewed; the dev2 truth and
passZ_dv1 were opened only by score.py and never printed; nothing of f.103r touched.

**Verdict (as declared): FAIL read-free -- untested-by-this-tool (raw components).** Recall 0.000 (0 of 84 ':' positions) at
precision undefined (0 candidates); lift undefined (0 / 0), null p95 and max undefined. The candidate pool is empty a second time,
so this is the tool's limit, not a negative for the two-component rule on this hand (rule 3's third-attempt clause: the
two-component rule on `glyph_atlas.py segment` output is retired for this hand as "untested-by-this-tool"; a different
instrument needs its own PREREG).

## Candidate pool (reported first; pool.py imports rule.py's own functions, box geometry only)
| step | MARKS-DEV2 (default segment) | MARKS-DEV2b (--merge-vgap 0.0 --min-area 0.03) |
|---|---|---|
| component boxes kept (OL1-BOXES recipe, ghost rule unchanged) | 1698 | 1771 |
| boxes with larger side under 0.35 x the line's median sign height | 30 | 29 |
| small pairs stacked (gap 0..1.0 x smaller h) and x-overlapping >= 0.50, before the stroke test | 0 | 0 |
| ':' candidates (after the no-third-component test) | 0 | 0 |
| max-side / median quantiles 1% / 5% / 10% / 25% | 0.32 / 0.39 / 0.49 / -- | 0.31 / 0.41 / 0.53 / 0.88 |

Per line: pool.tsv (no line has a stacked small pair).

## Scoring (score.py byte-identical in logic to marks/score.py; output path only)
| step | number |
|---|---|
| ':' truth positions (ref_sign ':', by script) | 84 |
| recall / precision, +-1 (gating) and exact | 0.000 / undefined; 0.000 / undefined |
| unflagged positions / position errors / insertions (fixed scorer, no label map) | 679 / 43 / 41 (registered triple reproduced) |
| lift | undefined (0 / 0); null (200 within-line shuffles) p95 undefined, max undefined |
| box count vs position count (36 truth lines) | 1726 boxes vs 1848 positions; boxes < positions on 26 lines, > on 8, = on 2 |

## Why the pool is still empty (read-free, from the segmenter's source only; no image viewed)
The knob changed (no vertical merge; sides down to 0.03 x median kept by `--min-area`) adds 73 boxes but not small ones: the
small-box count falls 30 -> 29. `tools/glyph_atlas.py segment` (commit 872b2aa6c) has a second, hard-coded filter that no option
reaches: line 230 drops every merged component with h < 0.3 x median AND w < 0.6 x median ("specks, dots of i"), and line 215
sends small components above the line to marks.tsv by position. A dot of a ':' is under 0.3 x median in height by construction
of the rule (0.35 x median), so the segmenter discards it before rule.py sees it, at any --min-area. The two-component rule was
therefore never shown the components it looks for, a second time. This is an inference from code, not a check on any image.
A raw connected-component pass (cv2 on the binarised crop, no speck filter) or a single-component ':' shape test on merged
boxes would be a different instrument, each needing its own PREREG.

Doubt list: doubt.tsv has 0 rows.

## Diff against marks/ (the only changes)
- run.sh: the segment call gains `--merge-vgap 0.0 --min-area 0.03`; temp dir marks2_seg; calls marks2/rule.py; header comment.
- rule.py, score.py: one line each, `M = .../marks` -> `.../marks2` (output directory), so the prior run's committed files are
  not overwritten. Rule and scorer logic unchanged (`diff` shows only that line).
- pool.py (new): the pool report, read-free.

## Files, commits and hashes
- rule.py, score.py, run.sh committed BEFORE any run: 71099570f.
  rule.py 9a3db16590f372da6cc3347a4d993768850763c84f411ebca6e73b0abb38eea5;
  score.py bab6c8530a2240e2ee878ce2dac027fddca9032bac88238e06b6e6bf2d0aa8dd;
  run.sh 33373dac39ef62163eb8c99907a6c028cb7510254385043513c2fd0b77d3b973.
- boxes.tsv, candidates.tsv, doubt.tsv, pool.py, pool.tsv committed BEFORE scoring: 2105c2b8f.
  boxes.tsv 3045cf8098510c4060cb29d7a708e774a6ac68e1988fb6dc1e8b61af543af941;
  candidates.tsv 523226c5d1d447ed47a94528639f5469b72808f0f1a62fcecadae4561f0e9ea2 (header only);
  doubt.tsv 5098e3e3c80bdcac7ad2eb80e05fc73b8a523cd1c384b06ca940d5bbcb2e68c2 (header only);
  pool.py ac543975093b448bc18ca3d9b904a37af8d2786b4b00ca2a146e20a1d6fe7cca;
  pool.tsv efe16f90c8f723884183912e015f771b4fb6c8717ec881efc28b38124d2ed259.
- result.json (score.py output; counts and rates only, truth and pass sha256 inside):
  b82089b1653ba81171dd92ee4d97aac8673e761fd6be27942c7638201259c4ae.
- Regenerate: `sh benchmark-tx/txeng2/marks2/run.sh && python3 benchmark-tx/txeng2/marks2/pool.py ${TMPDIR:-/tmp}/marks2_seg && python3 benchmark-tx/txeng2/marks2/score.py`.

Openings of eval truth: 0
dev openings: 1 (by script)
