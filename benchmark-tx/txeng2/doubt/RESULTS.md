# TXE2-DOUBT: doubt detector re-tuned (PREREG-txeng2-2 X9 + X17; 9 Oct 2026, 16:43-16:5x UTC by date -u)

LANE TX-ENGINEER-2, account 4, Opus 5.5 worker. Brief `.claude/briefs/runs/2026-10-09-account4-txe2-round2.md`.
**Read-free: 0 vision calls, 0 hosts, no reader.** Every eval_heldout figure below is a read-free recall table (signals
already on file, truth opened only through `tools/tx_bench.py position_errors`), **not an eval look**; the lane's look count
is unchanged. No truth file was edited.

**Verdict (registered gate: recall >= 0.7 at <= 15% flagged on dev, the same rule >= 0.6 on eval read-free): dev met,
eval FAIL as registered -- overall FAIL.** Dev re-chooses `latt+vote+selfcons`, 10/12 = 0.833 at 14.0% flagged. Two of
those three signals (vote, selfcons) have **no input on eval_heldout** (X5's vote and the K2 / V_s0 / V_s1 presentations
exist for dev_tune only), so on eval the registered rule reduces to `latt`: 6/15 = 0.400 at 1.9%.

Order kept: tool + signal tables committed and pushed (fa7d817f6) before any truth was opened; dev measure + the vote4
substitute tables (next commit) before any eval recall was computed.

## Signals added (`tools/tx_doubt.py extend`; test `tools/tests/test_tx_doubt.py` ok)
Every other read is aligned to L per line (`tx_bench.align`, L as reference; a sign the other read drops counts as differing).

| signal | definition (PREREG X9 wording) | input | dev coverage | eval coverage |
|---|---|---|---|---|
| pairclf | tx_pair_clf output != L (it moves a sign only where its margin passes t) | outputs/.../passX2_pair_dev_tune.tsv | 354/354 | none (X2 failed dev; no eval file) |
| vote | X5 weighted (LOO) or uniform vote != L | passX5_weighted / passX5_uniform _dev_tune | 354/354 | none |
| conf | X4 top-1 p < 0.7 | txeng2/conf/passX_dev_tune.tsv (X4's file existed, 849f158c4) | 354/354 | none (X4 dev only) |
| selfcons (X17) | K2 / V_s0 / V_s1 presentations vs pass A differ; on geo H vs H2 | passK2_sr4, passV_s0, passV_s1 _dev_tune; passH/H2_geo | 354/354; geo 188/188 | none |
| countchk (X19) | line flagged by tx_count_check (reported though weak) | txeng2/weight/x19_count_no87_L_{dev_tune,geo}.tsv | 354/354 | none |

Dev pool: the PREREG names dev_tune + dint_B + f87 + f36v "where signals exist". tx_doubt's base signals (atlas boxes,
tiles, contrast, lattice) and every new signal exist for no.87 only, so the pool is dev_tune (12 lines, 343 scored).
L errors on dev_tune now read 12 (TXE-O read 14 before the round-0 truth changes).

## Dev_tune (vs L, 12 wrong / 343; vs pass A, 21 wrong)

| signal | vs L recall | vs A recall | share |
|---|---|---|---|
| show | 10/12 0.833 | 18/21 | 0.501 |
| disagree | 2/12 0.167 | 10/21 | 0.090 |
| bandcut / thin / contrast | 5/12 each 0.417 | 5 / 10 / 8 of 21 | 0.172 / 0.230 / 0.210 |
| stab | 1/12 | 1/21 | 0.052 |
| freq | 5/12 | 6/21 | 0.356 |
| latt | 5/12 0.417 | 12/21 | 0.055 |
| pair | 11/12 0.917 | 11/21 | 0.446 |
| **pairclf** | 2/12 0.167 | 2/21 | 0.038 |
| **vote** | 6/12 0.500 | 14/21 | 0.087 |
| **selfcons** | 7/12 0.583 | 16/21 0.762 | 0.114 |
| **conf** | 7/12 0.583 | 15/21 0.714 | 0.262 |
| **countchk** | 7/12 0.583 | 14/21 | 0.822 |

Best OR-of-<=k at the cap (dev chooses): k=1 <=15% selfcons 7/12 at 11.4%; k=2 <=15% latt+vote 9/12 = 0.750 at 10.5%;
**k=3 <=15% latt+vote+selfcons 10/12 = 0.833 at 14.0% (48/343)**; vs pass A the same rule 19/21 = 0.905.
Full tables: `measure_dev_tune.md` / `.json`.

**Selection control** (`selection_null.py` -> `selection_null.json`): the same search (14 signals, k <= 3, <= 15%) on dev
with L's wrong labels permuted over the 343 positions, 200 seeds: best recall mean 0.207, p95 0.333, max 0.500, none
>= 0.7; real 0.833, p = 0.005. The dev result is not an artefact of searching 469 combinations. Caveat: vote's weighted
leg was learnt on dev_tune truth (leave-one-line-out, so no line's own truth), and the K2 / V presentations were designed
on dev_tune; both are dev-native.

## Eval_heldout, read-free (rule not re-chosen; vs L 15 wrong / 376)

| rule | recall | flagged |
|---|---|---|
| **latt+vote+selfcons as registered (vote, selfcons absent = 0)** | **6/15 = 0.400** | 7/376 = 1.9% |
| same vs pass A | 7/18 = 0.389 | 1.9% |
| substitute, disclosed (not registered): latt+vote4+selfcons, vote4 = uniform vote of A, B, E, F (the readers on file for eval; `vote4_uniform_*.tsv`, truth-free) | 9/15 = 0.600 | 11/376 = 2.9% |
| the same substitute on dev | 10/12 = 0.833 | 45/343 = 13.1% |
| latt+vote4 (dev / eval) | 6/12 0.500 at 6.1% / 9/15 0.600 at 2.9% | |

The substitute reaches 0.600 on eval at 2.9%, but on eval it is latt+vote4 only (selfcons absent), and it was formed after
the registered rule's inputs were found missing; it is a lead for the lane, not a gate pass.

## X17 selfcons on the geo unit (H vs H2, TXE-B), read-free
selfcons 3/15 = 0.200 of L's geo errors at 8/169 = 4.7% (vs pass A 4/23); countchk 12/15 at 81.7% (useless share). geo
includes f178v_L22 (an eval_heldout line); read-free, not a look. H vs H2 crop-geometry disagreement finds few errors.

## Sorter curve per tile, new feed (`tx_sorter_curve --propagate none`; `sorter/`)
Feed `<unit>_feed_combo.tsv` = the dev rule first, then n_signals; `signals2/3` = n_signals over every column. Oracle owner;
upper bounds. Disclosed: the two feed tables were derived from committed signal tables and committed with the curves, not before.

| unit / truth rows | feed | to 2% | removed at 10 / 20 | TXE2-SORT doubt feed (none) |
|---|---|---|---|---|
| dev m (12/343) | combo | 20 | 3 / 6 | 17; 4 / 6 |
| dev m | n_signals (14 cols) | 23 | 3 / 5 | |
| dev x (7/338) | combo | 1 | 3 / 5 | 1; 3 / 5 |
| eval m (15/376) | combo (= latt on eval) | 22 | 7 / 7 | 32; 2 / 4 |
| eval m | n_signals (with vote4) | 27 | 2 / 4 | |
| eval x (10/371) | combo | 4 | 3 / 5 | 16; 2 / 3 |
| random (10 seeds) | | dev m 6/10 reach (125-183); eval m 7/10 | ~0.3-0.5 / 0.6-0.8 | |

On eval the combo feed removes 7 of L's 15 wrong signs in the first 10 tiles (6 from the 7 latt positions), against 2 for
the earlier n_signals feed.

## Reading
The new two-reader signals (vote, selfcons) are the best narrow doubt signals measured on no.87 so far, and on dev they
carry the gate with room; but they are only as available as the extra reads that feed them, and none exists on
eval_heldout. The gate as written cannot be tested on eval until the K2 / V_s0 / V_s1 presentations (selfcons) and a
vote input exist for the eval lines -- that is a reading job (vision calls), outside this read-free brief. conf (X4)
recalls 7/12 but at 26% share; pairclf and countchk add nothing inside the cap.

## Follow-ups (one line each, not started)
- Run the K2 / V_s0 / V_s1 presentations on eval_heldout lines (one look's worth of reads, the lane's call) to test
  latt+vote+selfcons as registered.
- latt+vote4 needs no new read and holds 0.600 at 2.9% on eval; it could be registered as its own rule for a fresh unit.

Files: `{dev_tune,eval_heldout,geo}_signals{,2}.tsv`, `*_signals3.tsv` (+vote4), `measure_{dev_tune,eval_heldout,geo}.md`,
`selection_null.{py,json}`, `vote4_uniform_*.tsv`, `*_feed_combo.tsv`, `sorter/`, `sorter_*_latt+vote+selfcons.txt`.
Cost: the orchestrator's get_session reading.
