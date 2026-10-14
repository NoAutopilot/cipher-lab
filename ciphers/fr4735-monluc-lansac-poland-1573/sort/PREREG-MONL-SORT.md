# PREREG MONL-SORT (14 Oct 2026, 19:15 UTC by date -u; account 1, for LANE DEFAULT-A1-1840-14)

Pushed before either blind sort is read. Tiles: every K12, K14, K34 token of c268 L01-L05 (33) and c172 L02-L04 (12), plus the 4 c172
K04 tokens as in-set controls (49 tiles; sort/build_tiles.py). Windows: tools/lookalike_pass.py windows (commands in NOTES "## MONL-SORT").
Two blind Sonnet sorts (sort_prompt_A.md, sort_prompt_B.md: same tiles, page order reversed), no key value, reading or current label shown.

Relabel rule (fixed now): a token is relabelled from its current cell to the other cell of its pair only if BOTH sorts give that other
cell and neither sort marks it conf L. Every other token keeps its label. No key.tsv edit. A disagreement, SPLIT, X_NEW or L is logged, not applied.
Control read: the 4 c172 K04 tokens should sort K04 in both sorts; the 3 c172 K14 tokens the f.86 gloss confirms as p (L02:48, L02:54,
L03:40) should sort K14. If both sorts put 2 or more of these 7 controls on the other cell, nothing is relabelled (sorter not discriminating).
Reported after: decode_key.py --check exit, c268 grades, and align_c268.py confirm count against 136/169 (MONL-ALIGN).
