# BOXCLIP: would a script that flags clipped sorter boxes help? (12 Oct 2026)

Files: `PREREG-BOXCLIP.md` (method, labels, controls and gate, committed before any score), `run_boxclip.py` (the one scoring run; `--check`
re-derives `scores.tsv`, `--sensitivity` appends the labelled sensitivity table), `scores.tsv` (one row per labelled box), `RESULTS.md`
(verdict, every gate line, per sorter, sensitivity, post-hoc diagnostics), `diagnostics.py` (run after the verdict, changes nothing).
The tool is `tools/box_clip_check.py` (offline test `tools/tests/test_box_clip_check.py`). Live-page flags were not produced (gate FAIL).

## NOTES (for the owner, plain words)

I tested whether a script could look at the page picture and flag the boxes that hold only part of a sign (ink touching the box carries on outside it), using
your own work as the answer key: the 43 boxes you re-cut with "Fix the cut" (21 Modena, 22 Matignon f.110) against the 21 boxes you looked at and left
alone (10 Modena, 11 Matignon). It failed, on every line I set beforehand. It flagged 18 of your 43 re-cuts (42%) but also 8 of your 21 left-alone boxes
(38%); the dull rule "flag every box smaller than its page's median" does slightly better (balanced score 0.55 against 0.52, and 0.50 would be a coin
toss: the script's p-value against random flagging is about 0.5), and where it did flag, its proposed bigger box fits your re-cut no better than the old box
did. On Modena it flags nearly everything (26 of 31), because the g/q signs sit in running text; on Matignon it flags nothing (0 of 33), because the rule
that keeps one sign's ink from being counted as the next tile's also throws away the ink you were adding under the neighbouring tile. So as built it would
have saved you nothing, and I did not run it over the unfinished pages. One thing I saw only after the verdict, so it is a lead and not a result: with the
neighbour rule switched off, the same check flags 11 of your 22 Matignon re-cuts and none of the 11 you left. It would need a fresh test, registered first, on
boxes you have not yet touched (your next batch of re-cuts is the natural set) before it counts as help.
