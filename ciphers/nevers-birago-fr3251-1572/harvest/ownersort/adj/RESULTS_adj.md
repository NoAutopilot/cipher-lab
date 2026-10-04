# BIR-ADJ results (4 Oct 2026, 07:12-07:2x UTC, account-3 worker)

Prereg `PREREG_adj.md` + `key.tsv` pushed at cf40cb6a before any image read. Builder `build_adj.py` (deterministic, seed 20261004),
scorer `score_adj.py`; answers in `answers/` (blind Sonnet passes p1/p2, 10 items per call; blind Opus reconcile on splits only).
Images: the sorter's own tile boxes on the line strips already on disk (same public Gallica regions); 0 network requests.
Subagent calls: 6 control + 22 target + 1 reconcile = 29.

## Known-answer control (30 tiles, all three readers agree; true pile vs nearest look-alike pile)
Pass 1 30/30, pass 2 30/30 (gate 24/30) -> instrument licensed. Caveat: at ceiling (rule 3) -- it shows the instrument separates
confident tiles from their nearest look-alike pile, not that it is calibrated on the harder disputed tiles.

## Targets (109 tiles; 108 testable, t014 untestable: owner pile has no other member)
| leaf | owner right | machines right | both plausible | neither | untestable |
|---|---|---|---|---|---|
| f.117r | 24 | 0 | 6 | 0 | 0 |
| f.144r | 25 | 0 | 1 | 0 | 1 |
| f.168 | 49 | 1 | 2 | 0 | 0 |
| all | 98 | 1 | 9 | 0 | 1 |
Grades: agreed (both passes, at least one high) 78, agreed-low 27, reconciled 3 (t001, t062, t071 -> owner right).
Bias checks (after scoring, not pre-registered): raw strip answers 1:91, 2:105, both:20 (owner strip shown first on 50/109) -- no
position bias; owner strips are not closer in context (same-leaf share 0.35 owner vs 0.39 machine; same-line 0.04 vs 0.02); owner right
holds where the machine strip is pure (all six tiles owner-kept in the machine pile): 58 of 62, vs 40 of 46 where it is not (after reconcile).
What the instrument cannot separate: it asks "which group does this tile look like". The owner built the piles by eye, so for owner-made
new piles (24 items) the owner strip is the owner's own visual cluster; agreement with it is partly by construction. For sheet piles
(84 items, all 84 owner right; the 9 both-plausible and 1 machines-right are all on new piles: 14 of 24 owner right there) the owner pile is the published reference pile, a sharper test.
Candidate corrections: `owner_right.tsv` (98 tiles), every one at M (one instrument; never S without a second).

## Re-decode gate with only the 98 owner-right moves (`ownersort.py --new-piles-unknown --only-sids adj/owner_right.tsv` -> `../v3_adj/`)
| leaf | changes (value / U) | (a) base | (b) adj | control p95 | rank in 201 | gate |
|---|---|---|---|---|---|---|
| f.117r | 19 (18 / 1) | -1.215 | -1.284 | -1.217 | 101 | FAIL |
| f.168 | 46 (40 / 6) | -1.149 | -1.565 | -1.258 | 201 | FAIL |
| f.144r | 25 (21 / 4) | -1.418 | -1.459 | -1.379 | 37 | FAIL |
| pooled | | -1.239 | -1.384 | -1.301 | | FAIL |
Every leaf fails, including f.144r, which passed (rank 5) with the full v2 sort. So the image check and the language gate disagree:
on the image the owner's grouping is right at about 98 of 108 disputed tiles; under the 1572 key sheet values those groupings make every
text worse. Read together: the owner's piles track shape better than the machine readers' labels did, but the key-sheet value attached
to the pile (by family) does not fit these positions -- the gap is between sign shape and key value (the key's sign inventory, or the
tile-to-position mapping), not the owner's eye. Not settled here; nothing applied.
