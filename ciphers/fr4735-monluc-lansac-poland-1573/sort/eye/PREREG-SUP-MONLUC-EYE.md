# PREREG SUP-MONLUC-EYE (20 Oct 2026, 03:3x UTC by date -u; account 2, Opus)

Question: are the 7 split/low-conf K04|K12 tiles of MONL-SORT2 (L06:23, L08:10, L08:19, L09:27, L10:33, L22:14, L24:12) K04 or K12 by shape?
Material: MONL-SORT2's own family-A tiles regenerated from regen_monll11.sh / regen_monll21.sh (c268d tiles not regenerated, so L16:16, L18:18
are out), windows by tools/lookalike_pass.py windows, cropped +-260 px around the window tick, 1.5x, shuffled under ids T00-T17
(Random(2026)); id->line map written to a file this reader does not open until every call is recorded.
Reader: this worker, one look per sheet (3 sheets), each tile called K04 (dot/mark at the top-left of the 9 bowl, 'd' family) or
K12 (plain 9), or X, with H/M/L, no value, facing letter or clear text consulted.
In-band controls (in the 18): K04 controls L14:14, L23:16, L25:17 (d-facing, H/H in MONL-SORT2) and K12 refs L12:8, L14:13.
Gate: relabels are allowed only if every control is called K04 and no K12 ref is called K04 (0 errors on 5); otherwise no relabel.
Decision: a lead tile called K12 at H or M is relabelled K04 -> K12 (tag sup-monluc-eye, conf M); K04 at H/M is kept K04 and its split
closed as "K04 by shape"; X or L stays split. key.tsv is never edited.

## Decision
(added after the run, 20 Oct 2026; the gate and decision rule above were pushed before it)
Belief: the split K04|K12 tiles can be settled by shape at 3x
Would change it: any in-band control not called K04, or a K12 ref called K04
Observed: controls: L14:14 K04 (right), L23:16 and L25:17 X (no sign at the window tick); refs L12:8, L14:13 K12 (right); leads L06:23 K12 M, L08:10 K12 M, L08:19 K12 L, L09:27 K12 M, L10:33 K04 L, L22:14 X, L24:12 X
Decision: change -- gate not met (2 of 3 controls not seen), no relabel; next: re-cut the tiles by position from levelled crops and sort with in-band controls
Lesson: tools/lookalike_pass.py windows ticks missed the sign on 6 of 7 c268e (L21-L25) tiles; check a known tile before trusting a window sort there
