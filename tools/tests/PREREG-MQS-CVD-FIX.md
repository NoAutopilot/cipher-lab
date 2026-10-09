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

## Results (9 Oct 2026, 10:3x UTC by date -u)

1. Gate 1 PASS: after the edit `--audit tools/glyph_atlas.py tools/build_dashboard.py` -> glyph_atlas 2 colour literals,
   2 chromatic, 0 flags; build_dashboard 22 literals, 8 chromatic, 0 flags; exit 0 (before: 4 + 2 flags, exit 2).
2. Gate 2 PASS: control unchanged, false flags 2/31, rotated null recall 0/10, CONTROL PASS.
3. Gate 3 PASS: test_glyph_atlas ok, _jitter ok (stab small 0.00, big 1.00), _match ok, build_dashboard counts/depth/fame/
   sidequests ok, test_cvd_check PASS (before and after; opencv/skimage/sklearn had to be pip-installed first).
4. Null PASS, after one finding: the first re-broken copy (OVERLAY_BLUE back to (0, 160, 0)) read 0 flags, because the
   audit scans 3-int tuples only on lines naming cv2/col/fill/outline and the bare constant line was invisible to it -- the
   first 0-flag result was coming from the hex in the comment above the constants, not the code. The constant lines now
   carry "# BGR colour" so the audit reads them; re-run: fixed file 0 flags (reads #0072b2, #b35900 from code lines
   161/162), re-broken copy 1 flag (CVD-COLLAPSE #00a000 vs #b35900, deutan 4.4, exit 2), pre-fix files 4 + 2 flags.
5. Palette: overlay pair #B35900/#0072B2 on white PASS (deutan 53.9, tritan 51.2). Dashboard light #22306E vs #B4741A PASS;
   dark #9DB7F5 vs #D9A24A PASS on contrast except white text on #9DB7F5 (2.00; was 2.23 on #6ABF85), fixed by drawing
   k-ours/out-ready chip text in var(--surface) (#1C2127 on #9DB7F5 PASS). Blue #0072B2/#56B4E9 for --good was rejected:
   the audit flags it CVD-COLLAPSE against --accent teal (tritan 7.9 / 5.0). Navy #22306E vs teal #2E6F6A is not flagged
   by the audit but is under the 20 palette gate under deutan/tritan; both are "positive" states and every chip carries
   its text label, so meaning does not ride on that hue difference.
Non-colour cues: segment --debug signs solid orange boxes, marks dashed blue boxes, line peaks dashed blue lines (checked
on a synthetic page render); strips odd positions solid orange, even dashed blue, position number printed under each.
