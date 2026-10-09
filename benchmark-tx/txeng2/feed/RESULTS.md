# TXE2-FEED: the sorter feed as a product (PREREG-txeng2-4 S4; 9 Oct 2026, 17:48-17:5x UTC by date -u)

LANE TX-ENGINEER-2, account 4, Opus 5.5 worker. Brief `.claude/briefs/runs/2026-10-09-account4-txe2-round4.md`.
**Read-free: 0 vision calls, 0 subagents, 0 hosts, no truth file opened, no eval look, no tile resolved, no cluster
propagation, nothing published** (the orchestrator publishes). No experiment, no gate (S4 is a product).

## What was built
- `tools/tx_feed.py` (+ `tools/tests/test_tx_feed.py` ok, SYSTEM.md row, tool_shelf row; system_map_check ok): aligns other
  reads to a unit's line read, orders tiles combo tier first (the X9 rule, latt+vote4+selfcons "where inputs exist"; an
  absent column is reported in the feed header), then n_signals, and writes per unit `<unit>_feed.tsv` (full ordering, tier,
  candidate piles, question), `<unit>_feed_signals.tsv`, `<unit>_focus.tsv` (the sorter's "Check these first" format,
  `tile<TAB>question`, as `ciphers/nevers-birago-fr3251-1572/sorter/no87/focus.tsv`).
- `tiles.py` -> `<unit>_tiles.tsv`: the sorter inputs per focus tile. eval_heldout tiles are atlas boxes (sid, page, x, y, w,
  h from `atlas/signs.tsv`, the box `sign_sorter.py` cuts). f152r and spinelli have no per-sign box mapped to their line read:
  the row names the line's segment crops, so the page build needs one segmentation step first (not done here).
- `build.sh` regenerates everything from the repo root. `work/f152r_latt.*`: a plain lattice for f152r (from-passes A+B,
  confusion_1572, printed key_1572_sheet, it16dip, lam 4, beam 64) so f152r carries `latt` like eval_heldout; its own
  control: real key rank 1 of 21 (z 4.06 lattice, 3.96 top-1) against 20 value-shuffled keys. Truth-free.

Question per tile (research/TX-TAXONOMY-2026-10-09.md): "Which pile: A or B?" with the candidate piles sorted (the order never
shows which pile the line read chose), plus the feature that separates a taxonomy look-alike pair (T18/T98 "compare the
descender length", T90/T53 "look for the closed loop", T76/e-cells "look for the loop", T64/l-cells "look at the tail"),
"The band may cut the sign: open the line view" where bandcut = 1 and "Hairline ink: zoom on the tick or tail" where thin = 1
(class 2 and 3); a tile flagged only by a reader's own L confidence asks "A reader marked this sign unsure: which pile?". No
value, no colour, no machine pick.

## Per unit

| unit | positions | signals on file | combo columns present | focus tiles (share) | any-signal tiles |
|---|---|---|---|---|---|
| eval_heldout (no.87, f178v L13-23 + f179r L01-03) | 402 | TXE2-DOUBT signals3 (show, disagree, bandcut, thin, contrast, stab, freq, latt, pair, vote4) | latt, vote4 (selfcons absent) | 11 (2.7%) | 358 |
| f152r (birago1572-f152r) | 96 | latt (new, above), reader A / B differ, A / B low conf | latt (vote4, selfcons absent) | 4 (4.2%) | 12 |
| spinelli (spinelli-c1519-confirm) | 252 | reader A / B differ (txeq), A / B low conf | none: focus falls back to the any-signal tier | 22 (8.7%) | 22 |

eval_heldout's 11 focus tiles are the same 11 positions TXE2-DOUBT's latt+vote4 substitute flagged (11/376 at 2.9%).

## Predicted decisions to 2% (per tile, perfect owner; an upper bound, as TXE2-SORT's curve)

| unit | E / N (published) | 2% line | predicted | basis |
|---|---|---|---|---|
| eval_heldout | 15 / 376 | <= 7 wrong | **22 decisions** (focus 11 -> about 8 wrong, 2.1%) | measured: TXE2-DOUBT curve on this feed (`../doubt/sorter/summary_eval_heldout_feed_combo_none_m.json`: 7 removed by tile 8, 2% at 22); the within-tier order here (n_signals) may differ by a tile or two |
| f152r | 6 / 73 (5 wrong + 1 inserted) | <= 1 | **not reached inside the feed** | needs all 5 wrong signs fixed (an insertion is not a pile move); latt's eval recall 0.400 -> about 2 in the 4 focus tiles, at most about 3 in the 12 signalled; 3 of the 5 are truth-doubtful (TXP-152) |
| spinelli | 14 / 193 | <= 3 | **not reached inside the feed** | needs 11 of 14; A/B disagree's eval recall 0.400-0.500 -> about 6 in the 22 tiles (about 8 wrong, 4.1%); agreed-wrong positions carry no signal here |

Predictions use only published counts (units README, errormap pools) and TXE2-DOUBT's eval recall; no oracle run was made on
f152r or spinelli (it would open their truth, a look the lane has not spent).

## Note for the orchestrator to publish for the owner (TRANSCRIPTION.md item 7)

> Three short sorter queues are ready from the transcription benchmark, 37 tiles in all: 11 on Birago no.87 (f.178v-179r),
> 4 on Birago f.152r and 22 on the Spinelli letter. Each tile comes with one question that names the piles it could
> belong to and, where we know it, what to look at (the descender, a closed loop, a tail; whether the line band may have
> cut the sign; whether the ink is a hairline). The computer does not say which pile it thinks is right, and each answer
> moves that one tile only. On no.87 the simulation says the 11 tiles should take about half of the remaining errors out
> of that stretch; on f.152r and Spinelli the queues are shorter than the errors they hold, so they are a first pass, not
> a finish -- the readers agree on several wrong signs there, and nothing we have flags those yet.

## Gaps (one line each, not started)
- f152r and spinelli need per-sign boxes before a sorter page can show their tiles (segmentation of the listed crops, or
  the f152r atlas boxes, 218 on the page, mapped to passZ positions).
- selfcons (and vote4 on f152r / spinelli) need extra reads (vision calls): the lane's call.

Cost: the orchestrator's get_session reading.
