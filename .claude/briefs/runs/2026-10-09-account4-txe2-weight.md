# TXE2-WEIGHT (LANE TX-ENGINEER-2 experiments X5 learned reader weighting + X19 deletion detector; read-free; Opus 5.5; cap 6; box 60 min from claim, 80% at 48)

For LANE TX-ENGINEER-2 (account 4, session_01NmaB9fhuaMSMYexV4NaVsR). Written 9 Oct 2026 15:5x UTC by date -u. PREREG
`benchmark-tx/PREREG-txeng2-1.md` section X5/X19 (binding) and `benchmark-tx/PREREG-txeng2-0.md`. First: `git fetch origin &&
git checkout -B main origin/main`; `export CIPHERLAB_ACCOUNT=account-4`; `python3 tools/room.py --start`; ROOM.md last 30 lines;
claim with `python3 tools/room.py "TXE2-WEIGHT worker (account 4, Opus)" "claim ..." --push`. Read `tools/tx_taxonomy.py` (how it
aligns every pass to the truth positions: reuse that), `tools/tx_bench.py` (position_errors, paired), `benchmark-tx/txeng2/
ERRORMAP-2026-10-09.md` (which passes cover which lines), `tools/reconcile_passes.py --vote` (TX-VIEWS' plain vote, the control),
`research/TX-TAXONOMY-2026-10-09.md` section 1 "Reader-specific bias". No vision call, no reader.

## X5 (primary)
1. `tools/tx_weighted_vote.py` (`--help`; test `tools/tests/test_tx_weighted_vote.py`: a toy with three readers, one biased,
   leave-one-line-out weights fix the biased reader's error and uniform weights do not). Subcommands: `learn` (weights from the
   dev_tune lines, leave-one-line-out, add-0.5 smoothing over the key's sign inventory `ciphers/nevers-birago-fr3251-1572/
   harvest/key_1572_sheet.tsv` + X_CE), `vote` (writes line pos sign for a unit), `control` (uniform; permuted-truth seeds 1-5).
   The truth is read only inside `learn` for the training lines and by tx_bench at the score; the tool never writes a truth.
2. Run on dev_tune with readers A, B, E, F, K2, V_s0, V_s1 (`benchmark-tx/outputs/birago1572-no87/`), leave-one-line-out; commit
   `passX5_weighted_dev_tune.tsv`, the uniform-vote output and the 5 permuted outputs; THEN score each with
   `python3 tools/tx_bench.py OUT --bench BENCHMARK-TX.tsv --item birago1572-no87 --paired benchmark-tx/txeng/units/labels_dev_tune.tsv
   --exclude-flagged`. Report fixed/broken/p for real, uniform and each permuted control; which positions moved and why (reader
   bias down-weighted or not); the all-same-wrong positions' fate.
3. If the dev gate (fixed > broken, p < 0.05, and every permuted control fails) is met: learn on all dev_tune lines, vote on
   eval_heldout with A, B, E, F, commit `passX5_weighted_eval_heldout.tsv`, DO NOT score it. Else say so.
## X19 (secondary, read-free; skip if X5 has used 60% of the cap)
`tools/tx_count_check.py` (`--help`, test): per line crop (benchmark crops: no.87 harvest/f178v etc., geo lines f178r; dint
images/f128_L0?; spinelli benchmark-tx/txeng/confirm/crops), expected sign count from the ink column profile vs the read's count;
tune the gap fraction on no.87 dev_tune only; report recall of lines with deleted/inserted errors at the share of lines flagged,
for no.87 (passA geo + dev_tune, L), dint (passA, passF), spinelli (passZ). No gate: a doubt signal; shelf row weak unless recall
>= 0.7 at <= 30%.
Write `benchmark-tx/txeng2/weight/RESULTS.md`, SYSTEM.md + tool_shelf.tsv rows (system_map_check passes); commit by path, push;
ROOM done line "for LANE TX-ENGINEER-2": X5 dev fixed/broken/p, uniform and permuted controls, eval file written y/n; X19 recall at
flagged share; "cost: the orchestrator get_session reading". Stop at 80% of cap or box with what exists committed. Never edit a
truth file; never AskUserQuestion. + `.claude/briefs/README.md` common tail.
