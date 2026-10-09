# TXE-I: contrast sweep before cutting (LANE TX-ENGINEER, idea O6 = owner's item 6; account 4, Opus 5.5; cap 7, box 100 min)

Read `.claude/briefs/runs/2026-10-09-account4-txe-COMMON.md` first, then `benchmark-tx/PREREG-txeng-2.md` (units, blindness,
Amendment: gate p < 0.01), research/TX-TAXONOMY-2026-10-09.md and research/TX-IDEAS-2026-10-09.md row O6 and the Results log
(TXE-A, C, E have failed on dev: a reader shown exemplars swaps right reads for look-alikes; a thin-only selection is too small;
a smoothed confusion flip never clears the lattice floor -- read them so you do not repeat their shapes). Why this job exists:
the owner asked (lane brief Amendment 1, item 6) that an uncertain sign be rendered at five contrast levels so a reader or a
script can watch which strokes persist and which appear, cut and label from the stable strokes, and log the sweep as the
evidence for the cut. The taxonomy's class 3 (thin strokes: half of the mapped errors at a 29% base) and the band-cut
descenders (class 2b) are the mechanisms: a faint tail that appears only at high contrast is the feature that separates
d T18 from s T98, and a stroke that vanishes at low contrast is the one the reader should not weigh.

## Build `tools/tx_contrast_sweep.py` (subcommands sweep, stable, sheet, resolve; --help; test tools/tests/test_tx_contrast_sweep.py)
Inputs (disk only): `ciphers/nevers-birago-fr3251-1572/atlas/signs.tsv` boxes, the page images (harvest `src_*.jpg`; origins
as in `tools/tx_taxonomy.py` load_geometry), the line read L (`benchmark-tx/outputs/birago1572-no87/labels.tsv`), the
box<->position map made label-blind (sequence alignment by order and x, as `tools/tx_compare.py map` does: import or call it,
never atlas/no87_box_token.tsv's truth column).
1. `sweep --page f178v --boxes ... --levels 5`: per box (grown 50%), five renderings at contrast levels from a weak stretch
   (5th-95th percentile) to a hard one (binarised at the page's Otsu threshold minus 2 steps), written as one strip per sign,
   with a manifest (level parameters).
2. `stable`: per box, the connected components of ink at each level; a stroke is STABLE when its component persists (IoU >=
   0.5 with a component at the next level) across >= 4 of 5 levels, APPEARING when it exists only at the two hardest levels,
   VANISHING when it exists only at the two softest. Writes per box: n_stable, n_appearing, n_vanishing, the stable-ink box
   (the union of stable components) and a flag `uncertain` when n_appearing + n_vanishing >= 1. Print per page the share of
   boxes flagged and the share whose stable-ink box differs from the atlas box by > 10% in height or width.
3. Read-free dev gate (opens truth; commit the per-box table first): on dev_tune, do the flagged boxes hold L's wrong
   positions? Precision/recall of `uncertain` against `tx_bench.position_errors` on labels_dev_tune.tsv (L's 14 wrong of
   343), and against pass A's 24. Registered gate for the read: the flag holds >= 50% of L's wrong positions at <= 20% of
   positions flagged. Report the same table on eval_heldout read-free (no reader; not an eval look -- say so).
4. If the gate in 3 is met: `sheet` writes, for the flagged dev positions only, rows of the five-level strip (soft to hard,
   left to right) with one neighbour of context at the middle level, at most 16 rows a sheet; ONE Opus 5.5 reader call per
   sheet with `harvest/sign_sheet_blind_1572.png` and the task "for each numbered row the five tiles are the same sign at
   rising contrast; weigh only strokes present in at least four tiles; give the sheet cell T## that matches, or X_NEW / ?;
   row, sign_id, conf, strokes used". Raw reads committed; `resolve` -> `benchmark-tx/outputs/birago1572-no87/
   passQ_sweep_dev_tune.tsv` (flagged positions take the sweep read, others keep L). Score `tools/tx_bench.py ... --paired
   benchmark-tx/txeng/units/labels_dev_tune.tsv`, gate fixed > broken p < 0.01; met -> eval_heldout once (the eval look);
   not met -> FAIL, no eval. If the gate in 3 is NOT met: no read; the flag table is the result (a negative with numbers).

## Report
`benchmark-tx/txeng/sweep/RESULTS.md`: per-page flag shares, the flag-vs-wrong table on dev and eval (read-free), the read's
lines if taken, `tools/tx_taxonomy.py` on passQ vs L (after commit), reader task text, calls. Shelf and SYSTEM rows (grade
from the result); one Results-log row in research/TX-IDEAS-2026-10-09.md (id O6; rebase before editing). Offline test: a
synthetic page with a sign whose faint tail appears only at the hard levels and a speck that vanishes: `stable` flags both
as uncertain with the right counts, and a solid sign is unflagged. Vision calls: at most 2 dev + 2 eval x about 1.5; cap 7;
stop before a call that crosses 80% of cap or box. Report in a short paragraph (first line: flag recall/precision and, if
read, fixed/broken/p) and stop.
