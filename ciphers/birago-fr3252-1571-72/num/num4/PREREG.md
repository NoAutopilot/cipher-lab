# BIRAGO-NUM4 pre-registration (decoy-null joint-consistency crib test)

Written 3 Oct 2026 before any target scoring. Brief `.claude/briefs/runs/2026-10-03-acct3-birago-num4.md`. Instrument
`joint_crib.py` (this folder). The anneal (`phased_homophonic`) is retired for this hypothesis (BIRAGO-NUM3); this is a
different instrument. Dev runs (statistic choice) used synthetic text only, seeds 98 and 99 (`dev_*.txt`); the scored
power control uses seed 4001; the target uses seed 20261003 for its decoys.

**Stream.** `../pooled_tokens.txt` (BIRAGO-NUM phase.py cut, f.119 + f.100r jointly), read with `../crib/crib_drag.py
read_runs` (strays and the 76 delimiter are breaks; a crib never crosses one).

**Crib set (15, fixed now; spelling v->u, as BIRAGO-NUM2):** carmagnola, bellagarda, ualletta, sauoia, turino, saluzzo,
monsignore, maesta, neuers, birago, ceppo, centurione, maresciale, ugonotti, regina. ("re" and "duca" dropped as too short
to carry a placement; "bellegarda" dropped as a near-duplicate of bellagarda that would agree with it by construction.)

**Placement.** A crib laid on consecutive pair tokens of one run, admissible if no code stands for two letters.

**Joint consistency.** Two placements (two cribs, or one crib at two places) are jointly consistent when they do not
overlap in the stream and no code is given two letters across them.

**Statistic (primary, `--stat max`; chosen on dev seeds, see below):** the maximum, over jointly consistent placement
pairs, of the it16dip bigram PMI summed over every adjacent token pair in both letters whose two codes the pair's joint
key fixes, each crib's internal bigrams removed (a constant per crib). Secondary (reported, not gating): `--stat count
--K 4`, the number of jointly consistent pairs that give the same letter to >= 4 shared codes.

**Null.** 200 decoy crib sets: each crib replaced by a random it16dip word of the same length (natural Italian letter
frequencies), dragged over the same real stream. p = (#decoys >= real + 1) / 201. Pass: p <= 0.05.

**Power control (rule 3, gate).** Synthetic it16dip text, 476 pairs, one homophonic key of 40 cells (no 6/7 digits),
5% stray digits, re-phased by `phase.em` (the measured segmentation error comes with it, as in BIRAGO-NUM2), 3 cribs from
the set planted once each, the full 15-crib set tested against 200 decoy sets. Found = p <= 0.05. Gate: >= 15/20 trials.
If the gate fails, the target is still scored for the record but its result is logged "untested-by-this-tool", neither
a pass nor a negative. A target pass licenses candidate pair values at grade M only.
