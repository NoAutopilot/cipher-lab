# PREREG MQS-CVD-FIX (LANE MQS-3, account 4) -- written 9 Oct 2026, 10:1x UTC by date -u, pushed before any control runs

Fix, not a method: replace the red-vs-green overlay pairs that MQS-CVD-AUDIT (9e102d301) flagged in
`tools/glyph_atlas.py` (cv2 BGR tuples, lines ~230/234/930) and `tools/build_dashboard.py` (--good green vs
--warn/#b45309 amber) with the project's own CVD palette (cvd_check.py `sheets_light`/`dark`: Okabe-Ito blue
#0072B2 / #56B4E9 and orange #B35900 / #E69F00), plus a non-colour cue where two overlay kinds share a picture
(dashed vs solid outline, line vs rectangle, the position number printed under each strip box).

## Before (pasted from the audit at HEAD d03c0101d)

    tools/glyph_atlas.py: 5 colour literals, 5 chromatic, 4 flags  (2 CVD-COLLAPSE, 2 RED-GREEN: #00a000 l.234 vs #dc0000 l.930 / #ff0000 l.230)
    tools/build_dashboard.py: 23 colour literals, 8 chromatic, 2 flags  (2 RED-GREEN: #2f7d4f l.729 / #6abf85 l.733 vs #b45309 l.768)

## Known answer and gate

1. `python3 tools/cvd_check.py --audit tools/glyph_atlas.py tools/build_dashboard.py` after the edit: **0 CVD-COLLAPSE and
   0 RED-GREEN** on any line this job edits (expected: 0 flags in both files, exit 0).
2. Control unchanged (cvd_check.py is not edited): `python3 tools/tests/mqs_cvd_audit_control.py` still reads
   false flags 2/31, rotated null recall 0/10, CONTROL PASS (its numbers at HEAD before this job).
3. Existing tests unchanged and passing: test_glyph_atlas, test_glyph_atlas_jitter, test_glyph_atlas_match,
   test_build_dashboard_counts/depth/fame/sidequests, test_cvd_check (all passed before the edit, with
   opencv-python-headless, scikit-image, scikit-learn installed in this container).
4. Null (must fail differently): the same audit run on the pre-fix files (`git show HEAD~:<file>` to a scratch path)
   must still report the 4 + 2 flags, and a scratch copy of the fixed glyph_atlas.py with one tuple put back to
   (0, 160, 0) must flag again. Why the null can fail differently from the known answer: the audit's statistic is a
   per-pair colour distance computed from the literal values, and the edit changes exactly those values, so the
   unfixed and re-broken copies can (and are expected to) flag while the fixed file does not -- unlike a shuffled-order
   control, nothing about the statistic is invariant to the manipulation.
5. New palette check: `python3 tools/cvd_check.py --marks <new overlay colours> --bg #ffffff` (glyph_atlas overlays sit
   on a white/grey page) PASS or WARN, and the dashboard light and dark `--good` vs `--accent`/`--warn` pairs not
   flagged by the audit.

A miss on gate 1 or 2 is reported with both numbers; this is a fix, so no shelf grade unless a shelf row describes the colours.
