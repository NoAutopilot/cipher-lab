# Owner sort of the Noailles c510-516 sign sorter, 4 Oct 2026 (quick pass)

Exported from https://claude.ai/artifact/3b1kUhxALuBLWhpAqPHPPo (private) after the owner said done (4 Oct 2026). The owner
did a deliberately quick pass (pile merges + the "Check these first" tiles), not a tile-by-tile sort. `db/` is the page's
database; `settled_labels.tsv`/`summary.json` from `tools/sign_sorter_apply.py --atlas-topk <build>/sorter/topk.tsv --db db`
(the topk.tsv is rebuilt by `sorter/build.sh`). 9,865 tiles: kept 7,990, merged 1,835 (18 pile merges, 120 -> 108 piles),
moved 36, bad-cut 4; new piles k006-b/-c, k072-b, k087-b/-c/-d. The owner's piles are a third reader, not ground truth.
