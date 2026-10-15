# PREREG-MONL-CTL: addendum to sort/k04/PREREG-MONL-K04.md -- in-band K04-facing-d control sort (15 Oct 2026, account 1, for LANE DEFAULT-A1-0740-15)

Written and pushed before any tile is cut or any sort is run. Method, prompt wording, cells (K04|K12), context ids and tile format exactly as
PREREG-MONL-K04 (sort/k04/build_k04.py, prompts.py), one blind call per sort, B lists the tiles in reverse order, value-blind (no value,
reading, clear text, current label, machine label or decode shown).

**Why.** MONL-K04 relabelled c268 L16:11, L20:27, L20:37 K04 -> K12 (both sorts K12, conf M/M), but every c268d tile it sorted was either a
K04-facing-n lead or a K12 reference; no in-band K04 that faces clear d was sorted, and its c172 K04 controls were not found by either sort.
Its own revert rule (NOTES.md "Remaining gaps (MONL-K04)", verbatim): "an in-band control sort of the L16-L20 K04 tokens that face d
(L17:16, L19:2, L20:23, L20:33) mixed with the 4 unsettled leads (L11:14, L17:20, L20:8, L16:16), one call per sort; if the d-facing K04s
also go K12, revert the 3 MONL-K04 relabels".

**Tiles (10, the same in both sorts).**
- 4 in-band controls, K04 facing clear d (align_c268.tsv as committed, kind confirm): c268 L17:16, L19:2, L20:23, L20:33 (band c268d).
- 4 unsettled leads, K04 facing clear n: c268 L11:14 (band c268c), L16:16, L17:20, L20:8 (band c268d).
- 2 in-band K12 references (as MONL-K04): c268 L19:6, L20:32 (band c268d).
- No c172 tiles (both sorts failed to find them in MONL-K04; not repeated).

**Rules (operationalising MONL-K04's sentence).**
- A tile "goes K12" when both sorts label it K12 and neither answer is conf L (the same bar MONL-K04 used to relabel).
- **Revert:** if 2 or more of the 4 d-facing controls go K12, the 3 MONL-K04 relabels (L16:11, L20:27, L20:37) are reverted to K04 (tag
  `monl-k04` removed from score_c268.py's applied set; the sort answers kept on file), and no lead from this sort is relabelled.
- **Keep:** if 0 or 1 controls go K12, the 3 MONL-K04 relabels stand (conf M), and a lead here is relabelled K04 -> K12 only where both sorts
  give K12 and neither is conf L (tag `monl-ctl`, conf M).
- **Non-discriminating:** if both K12 references go K04 by both sorts, nothing is relabelled and nothing reverted; logged as such.
- Exactly 1 of 4 controls going K12 is logged as a warning beside the keep.
- Any relabel or revert is kept only if align_c268.py's L01-L20 shuffled-clear control (200 draws, seed 140) stays 0/200 at or above the
  real share; then score_c268.py, align_c268.py, decode_key.py . and all --checks.
- Budget: 2 Sonnet calls at most; if sort A alone would reach 80% of the cap (2.4), nothing is applied.
