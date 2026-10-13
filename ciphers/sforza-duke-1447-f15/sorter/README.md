# SFZ-SORT sorter inputs (13 Oct 2026, account 4, LANE DEFAULT-A4-2135)
Blind sign sorter for the Duke's two glossed slips of January 1447, BnF italien 1584 f.5 (Gallica canvas 9) and f.8 (canvas 11);
the alphabet-settling step named by SFZ-DUKE (8 Oct 2026) after the second blind machine reader was retired for this hand. Built, not published.
`sh ciphers/sforza-duke-1447-f15/sorter/build.sh OUTDIR` runs `cut.py` (no network: the two native regions on disk under
../sforza-italien1584-1447/duke/images/, stacked; line traces from row-ink peaks at three x positions, quadratic; tiles are ink groups
from tools/sorter_recut.py with a 2 px margin, over-split on purpose), then tools/sign_sorter.py in default blind mode (no key, no value,
no reader label; starting piles are 40 machine shape clusters `shape-NN`; `--seed-shape`) and its preflight. 2,325 tiles, 31 lines
(f.5 L01-L15, f.8 L01-L16), 40 focus tiles (two per frequent shape cluster). Reader A's committed token counts (duke/ciphertext_f5.tsv,
f8.tsv, 1,761 tokens) were used only to choose the split threshold (1.25 x median width), never put on the page.
Not committed: the page, its data JSON, pages/, debug/, region.jpg (build.sh regenerates them).
The page asks: one pile per distinct sign (duke_labels.md's table lists 35 shapes, for scale only), re-cut joined signs, BAD-CUT for specks.
Check after the sort (not on the page): the dateline run (f.8 L15-16, f.5 L14-15), read twice identically by SFZ-DUKE, must come out
sign-for-sign the same under the owner's piles. Then `tools/sign_sorter_apply.py` -> settled labels -> g1_duke.py / g1_duke_anchored.py
unchanged (Remaining gaps in ../NOTES.md).
