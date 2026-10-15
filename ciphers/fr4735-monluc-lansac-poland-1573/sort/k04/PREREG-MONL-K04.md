# PREREG-MONL-K04: value-blind K04|K12 sort of the c268 L16-L20 K04-facing-n tokens and L11:14 (15 Oct 2026, account 1, for LANE DEFAULT-A1-0740-15)

Written and pushed before any tile is cut or any sort is run. Method and rules as sort/vb/PREREG-MONL-VB.md and PREREG-MONL-ADH.md part 2
(which follow sort/PREREG-MONL-SORT.md), with the scope narrowed for the budget (brief: sort = 2 units, one blind call per sort, <= 12
windows per call).

**Tiles (12, the same in both sorts; B lists them in reverse order).**
- 8 leads, chosen by the alignment (K04 facing clear n, align_c268.tsv as committed in c8eadcdd5): c268 L11:14, L16:11, L16:16, L17:20,
  L18:18, L20:8, L20:27, L20:37. The selection uses the clear text; the sort itself is value-blind (no value, reading, clear text, current
  label, machine label or decode shown; context ids of the 3 signs before and after, as in every earlier sort).
- 2 K04 controls: c172 L03:26 and L04:13 (PREREG-MONL-SORT's gloss-backed c172 K04 controls, the first two of the four).
- 2 K12 references in the same band: c268 L19:6 and L20:32 (current K12; L20:32 faces n as a confirm). These test whether the sort can
  see a K12 at this resolution at all, which the earlier controls did not (MONL-VB: "does not show they can find a split where one exists").
- Cells offered for every tile: K04 or K12 only.

**Rules.**
- Relabel K04 -> K12 only where both sorts give K12 and neither is conf L.
- Relabel nothing if either K04 control is moved to K12 by both sorts.
- Relabel nothing if both K12 references are moved to K04 by both sorts (the sort cannot see K12 here; result logged as non-discriminating).
- A relabel set is kept only if align_c268.py's L01-L20 shuffled-clear control (200 draws, seed 140) stays 0/200 at or above the real share.
- Relabels go in score_c268.py as tag `monl-k04`, conf M; then `score_c268.py`, `align_c268.py`, `decode_key.py .` and all `--check`s.
- Budget stop: if sort A alone would reach 80% of the cap, nothing is relabelled.
