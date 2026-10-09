# TXE2-SORT (LANE TX-ENGINEER-2 experiments X6 sorter value curve + X20 owner decisions on file; read-free; Opus 5.5; cap 5; box 60 min from claim, 80% at 48)

For LANE TX-ENGINEER-2 (account 4, session_01NmaB9fhuaMSMYexV4NaVsR). Written 9 Oct 2026 15:2x UTC by date -u. PREREG
`benchmark-tx/PREREG-txeng2-1.md` section X6/X20 (binding) and `benchmark-tx/PREREG-txeng2-0.md` (S4, blindness). First: `git
fetch origin && git checkout -B main origin/main`; `export CIPHERLAB_ACCOUNT=account-4`; `python3 tools/room.py --start`; ROOM.md
last 30 lines; claim with `python3 tools/room.py "TXE2-SORT worker (account 4, Opus)" "claim ..." --push`. Read TRANSCRIPTION.md
items 6-7, `tools/tx_doubt.py` (--help; its per-position signals on dev_tune/eval_heldout are in benchmark-tx/txeng/doubt/),
`tools/sign_sorter_apply.py --help`, `ciphers/nevers-birago-fr3251-1572/sorter/README.md`, `sorter/no87/README.md`,
`sorter/owner-sort-2026-10-04/README.md`, `atlas/README.md` (clusters.tsv, labels.json, no87_box_token.tsv). No vision call.

## X6 (S4 measurement, no gate)
`tools/tx_sorter_curve.py` (--help, offline test `tools/tests/test_tx_sorter_curve.py` on a toy leaf with two clusters, one
impure): inputs a BENCHMARK-TX item + a baseline output + the box<->position map + the atlas clusters (sid -> cluster) + an
ordering file; the oracle (the truth file) names the true value class for the tile shown; the decision sets every tile of
that atlas cluster ON THE LEAF to the shown tile's true sign (an impure cluster therefore breaks its minority -- count them);
after each decision re-score with tools/tx_bench position_errors. Orderings: (a) tx_doubt signal count descending (the sorter
feed), (b) cluster size descending, (c) random, 10 seeds (mean and band), (d) oracle-best (greedy by net errors removed, an
upper bound). Output `benchmark-tx/txeng2/sorter/curve_<item>_<unit>.tsv` (ordering, k, err_true, fixed, broken) and
`RESULTS.md`: decisions-to-2% per unit per ordering (or "not reached by k=200"), and the value of the first 10 / 20 decisions.
Units: no.87 whole, dev_tune, eval_heldout (read-free, no reader: these are not eval looks, say so), and any dev item with a
cluster map (dint has a sorter folder: use it if a tile<->position map exists, else per-tile with no propagation, stated).
## X20
Apply the owner's 4 Oct 2026 decisions (`sorter/owner-sort-2026-10-04/corrections.tsv`, `labels_as_published.tsv`; the README
says how they were published and what `sign_sorter_apply.py --atlas-labels` writes) on top of L for no.87 at cluster level,
exactly as the TRANSCRIPTION.md rule "owner sorts are reused family-wide" prescribes; write `benchmark-tx/outputs/
birago1572-no87/passX20_owner.tsv` (all no.87 lines). Score dev_tune ONLY: `tools/tx_bench.py ... --paired benchmark-tx/txeng/
units/labels_dev_tune.tsv --exclude-flagged` (fixed/broken/p, positions changed). Commit the whole-leaf file; the lane scores
eval_heldout itself (its one look). If the owner's decisions touch no no.87 cluster, say so with the counts: a null result.

Write `benchmark-tx/txeng2/sorter/RESULTS.md` (both parts, every number), SYSTEM.md + tool_shelf.tsv rows for the new tool
(system_map_check passes), commit by path, push; ROOM done line "for LANE TX-ENGINEER-2": decisions-to-2% per unit under (a)
and (d), X20 dev fixed/broken/p and positions changed, "cost: the orchestrator get_session reading".
Stop at 80% of cap or box with what exists committed. Never edit a truth file; never AskUserQuestion. + `.claude/briefs/
README.md` common tail.
