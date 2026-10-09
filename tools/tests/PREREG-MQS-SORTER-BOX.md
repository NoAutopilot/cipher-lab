# PREREG-MQS-SORTER-BOX (written 9 Oct 2026 by MQS-SORTER-BOX, before the control below was run)

Feature: the sign sorter's "Fix the cut" editor gains two saves besides "Save cut": **"Add as a missed sign"** (the box as
edited is saved as an added box, db collection `added`; the tile's own cut is unchanged) and **"Split: keep this part, add the
rest"** (the edited box becomes the tile's recut, and the part of the box the edit started from that lies beyond the edited
box's right edge -- or left edge, whichever remainder is wider -- is saved as an added box of kind `split`). `sign_sorter_apply.py`
writes the `added` docs to `added.tsv`; `sorter_apply_recuts.py --added added.tsv` crops each added box into the tiles folder
and appends it to signs.tsv (line copied from the tile it was made from; no label: it is sorted on the next page build).

## Known answer (synthetic, offline: `tools/tests/mqs_sorter_box_control.py`)

Per seed (20 seeds, 1..20): one synthetic line image, 24 ink glyphs (random strokes) at known boxes with 6-14 px gaps = truth.
Machine boxing damaged on purpose: 2 truth boxes dropped (missed signs), 2 adjacent pairs merged into one box each (merged boxes);
the rest exact. Simulated person (the page's own save rules, replicated in the script, with uniform +-3 px jitter on every
edge they place): a missed sign -> an `added` doc at its truth box; a merged box -> a recut of the merged tile to the left
truth box, then the split remainder computed by the page's rule from the merged box.

Statistic: **coverage** = share of the 24 truth signs matched by exactly one final signs.tsv box at IoU >= 0.5 (one-to-one),
after `sign_sorter_apply.py` and `sorter_apply_recuts.py --added` have run on the simulated db.

Nulls (each can differ from the known answer on coverage, because coverage depends on where final boxes sit and on how many
there are, which both nulls change):
- **off**: the same db with no `added` docs (the page before this job: recut only). Expected 20/24 = 0.833 at most
  (the two missed signs stay uncovered and each merged pair keeps at most its left half).
- **misplaced**: the same number of added boxes and the same recuts, but each added box placed at a uniformly random x on the
  line (same size). Expected near the off value.

Gate (fixed now): mean coverage >= 0.95 over 20 seeds AND coverage above both nulls' per-seed values in 20/20 seeds.
Ceiling check: the off null is at most 0.833, so there is headroom.

What this does NOT measure (stated before the run): a person's own placement accuracy, or whether a person finds missed
signs at all. The simulated person is perfect up to +-3 px; this is a plumbing control (page rule -> db -> apply -> crop ->
signs.tsv). Shelf grade for the person-facing feature is therefore at most `weak` whatever the number, and `untested` for
recall of missed signs by a person. A person-run known answer exists for later: Birago no.87 has 8 boxes aligned `1:2` to
BENCHMARK-TX truth (one box, two clerk letters; `ciphers/nevers-birago-fr3251-1572/atlas/no87_box_token.tsv`), i.e. real merged
boxes; and 26 `2:1` (one sign cut as two boxes). Named, not run here.

## Result (appended after the run, 9 Oct 2026; the text above is unchanged since a49219a1)

`python3 tools/tests/mqs_sorter_box_control.py` -> `RESULTS-MQS-SORTER-BOX.tsv`: coverage known 0.998 (min 0.958, seed 10: one
split-off rest, which spans the inter-sign gap by the page's rule, fell under IoU 0.5), off null 0.833 (every seed), misplaced null
0.837 (0.833-0.875); above both nulls 20/20; gate PASS. Apply exit 0 on every seed, 24 final boxes. One detail of the simulation
not spelled out above: on a split the person drags only the right edge, so the kept part's left edge stays the merged box's own
when the jitter would put it within 3 px of it. Shelf grade `weak` as pre-registered (no person measured).
