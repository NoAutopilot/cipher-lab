# PREREG MONL-VB (15 Oct 2026, 02:3x UTC by date -u; account 1, for LANE DEFAULT-A1-0206-15)

Pushed before any blind sort is run. Tiles (sort/vb/build_vb.py): every K04, K12, K14, K34 token of c268 L06-L10 (35; pairs K04|K12,
K14|K17, K34|K53; L06-L10 has no K17 or K53 token), c268 L04:6 and L04:8 (pair K12|K22, MONL-EYE's lead), and the 7 controls of
PREREG-MONL-SORT (c172 K04 at L03:26, L03:52, L04:13, L04:19; c172 K14 gloss-confirmed p at L02:48, L02:54, L03:40). 44 tiles.
L01-L05 K12/K14/K34 tokens are not re-sorted (MONL-SORT). Windows: tools/lookalike_pass.py windows, --per 12 (commands in NOTES "## MONL-VB").
Two blind Sonnet sorts, A and B, 4 calls each (one montage of <= 12 windows per call; call 4 = the L04:6/8 and control montages):
same windows, tile rows reversed in B; no key value, reading, clear text or current label shown; context signs by cell id only.

Relabel rule (same as PREREG-MONL-SORT): a token is relabelled to the other cell of its pair only if BOTH sorts give that other cell and
neither marks it conf L. Every other token keeps its label. No key.tsv edit. Disagreement, SPLIT, X_NEW or L is logged, not applied.
Control gate: if both sorts put 2 or more of the 7 controls on the other cell, nothing is relabelled.
Reported after: decode_key.py --check, align_c268.py --check, the L01-L10 and L06-L10 confirm counts against 255/333 and 111/164
(MONL-C268B), the shuffled-clear control (200 draws, seed 140) and the f.139 control. A relabel set is kept only if the shuffled-clear
max stays below the real share and 0/200 draws reach it; otherwise the relabels are reported and reverted.
