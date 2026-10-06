# PREREG-LA: look-alike re-read of the p.4 4/5 forms (written 6 Oct 2026 18:46 UTC by date -u, before any re-read)

Job R12A-D1411LA (LANE LANE-RUN12-account-1). The scoring pre-registration is PREREG-D1411P4.md (commit afc9de42d), re-used
unchanged: same frozen tables, same statistic, same controls, same PASS rule, same letter and gloss tests. Only the input
numbers change. This file pins how the corrected numbers are made, before the re-read is run.

Tiles: la/tiles.tsv (la/build_tiles.py): the 83 p.4 numbers where pass A, pass B or the committed token has a digit 4 or 5.
Re-read: one blind Sonnet subagent call, crops only (images/d1411p4_crops/*.jpg), prompt la/prompt.md: every 4/5 digit of a
tile shown as '#', the reader names its shape X (cross), R (r-form), O (other digit) or ?, with H/M confidence. No table,
gloss, decode or prior value of the masked digits is shown. Shapes map X -> 4, R -> 5, O -> the committed digit.
Rule (tools/lookalike_pass.py reconcile rule, applied per number): a firm re-read (every '#' answered X/R/O, none '?') that
equals pass A's or pass B's token settles the number at 2-of-3 with the re-read value; otherwise the number is UNSETTLED
and keeps its committed value. Grades do not change (every number stays M or ok as committed; a settled number whose value
changed becomes M). Residual = unsettled / tiles: a 2-of-3 agreement figure, not true error (LESSONS "Look-alike pass").
Output: la/numbers_la.tsv; scored by la/score_la.py (score_p4.py with only the input and output paths changed). The verdict is
read by the afc9de42d rule; the change against the committed score (T21r 0.581) is reported beside it, not as a gate.
