# TX-ENGINEER (txeng) experiments on the width-DP box_pos files -- RESCORE (11 Oct 2026, 18:0x UTC by date -u)

**Measurement correction: box-to-position map fixed (off by one), not a new gate look.** No model read is re-run (no model call in
this job): the reader experiments are rescored by exposure; the read-free ones are re-run.

Job BOXMAP-RESCORE (others) for the account-3 parent (session_0198Cv8ypBfBVfRToKVWx33M). Script-only: no vision call, no reader, no
image viewed, no network beyond git. No truth file, BENCHMARK-TX.tsv row, confirm item or eval look touched.

`compare/box_pos.tsv` (`tools/tx_compare.py map`, the same file as `gate/box_pos.tsv`) and `pair/{dev_tune,eval_heldout}/box_pos.tsv`
(`tools/tx_pair_reread.py`) were built by copies of `atlas/no87_map.py`'s width DP; they match `atlas/no87_box_token.tsv` on every
shared box (714 of 714; 333 of 333) and add f178r. They carry the same off-by-one shifts on f178v L06, L07, L09, L11 (dev_tune) and
L13, L17, L21, f179r L01-L03 (eval_heldout) (`ciphers/nevers-birago-fr3251-1572/atlas/RESCORE.md`).

    python3 benchmark-tx/txeng/rescore_boxmapLA/box_pos_la.py     # box_pos.tsv rebuilt from the label-aware map (f178r rows kept),
                                                                  # per-unit 1:1 files, shifted_positions.tsv
    python3 benchmark-tx/txeng/rescore_boxmapLA/exposure.py       # exposure.tsv, exposure_positions.tsv

**156 positions** have a different 1:1 box under the label-aware map (51 dev_tune, 105 eval_heldout): `shifted_positions.tsv`.

## Reader experiments (not re-run): how much of each result sat on a shifted box

`exposure.py` classes every position a pass changed against L (paired, as measured) as fixed / broken / both-wrong / homophone (both
right) and marks it `shifted` when its tile came from the neighbouring token's box. "Right boxes" = the changed positions whose box
the fix does not move.

| experiment (pass) | changed (on shifted boxes) | fixed / broken, all | **fixed / broken, right boxes** | reading |
|---|---|---|---|---|
| TXE-A compare (passG_compare) | 48 (36) | 4 / 16, p 0.012 against | **3 / 6, p 0.51** | 10 of 16 breaks were wrong tiles |
| TXE-A M1b H_all / H_top1 | 30 (26) | 2 / 12 | **2 / 1** | 11 of 12 breaks were wrong tiles |
| TXE-A M1b any_top1 | 45 (36) | 4 / 14 | **3 / 4** | |
| TXE-S library (passG2) | 23 (19) | 0 / 7, p 0.016 against | **0 / 1** | 6 of 7 breaks were wrong tiles |
| TXE-S library r1 / r2 | 25 (19) | 1 / 7; 0 / 8 | **1 / 1; 0 / 2** | |
| TXE-L ordered / shuffled | 38 (25) / 36 (26) | 2 / 10; 2 / 7 | **1 / 7; 1 / 4** | both arms read the same tiles |
| TXE-K adjud Fable / Opus | 19 (5) / 7 (3) | 0 / 1 each | **0 / 0 each** | the one break each was a wrong tile |
| TXE-C pair re-read (passJ) | 2 (0) | 1 / 1 | 1 / 1 | untouched |
| TXE-J stab (passR_stab) | 16 (4) | 1 / 4 | 0 / 4 | breaks untouched |
| TXE-D2 4x read (passK2_sr4) | 48 (6) | 3 / 11 | 2 / 11 | breaks untouched |

TXE-A's show rule itself ran through the map: of its 165 shown items, 45 were cut from a shifted box, 30 of them shown because "atlas
top-1 differs from L" -- the atlas was reading the neighbouring sign. TXE-S showed 120 items, 24 from shifted boxes.

## Read-free experiments (re-run with the rebuilt box_pos)

| experiment | before (old box_pos; re-run today where the truth changed since) | **after** | verdict |
|---|---|---|---|
| TXE-F tile gate (`tx_tile_gate.py gate --box-pos`; `rescore_boxmapLA/gate/`) | dev recall 0.429 at 19.2% flagged (committed; today 0.417 at 19.2% on the TX-TRUTH-VERIFY truth); eval 0.333 at 18.4% | dev **0.417 at 17.2%**; eval **0.333 at 17.3%** (6 positions per unit now have no box) | NOT MET, unchanged |
| TXE-O doubt (`tx_doubt.py signals --box-pos`; `rescore_boxmapLA/doubt/`) | best dev combination disagree+latt 6/12 (0.500) at 10.5%; eval 9/15 at 6.1% | identical (the combination reads no box) | FAIL, unchanged |
| TXE-O single box-based signals | `show` eval 14/15 at 40.2% flagged; `thin` 8/15 at 38.0% | `show` **14/15 at 20.2%**; `thin` 6/15 at 36.2%; `bandcut`, `stab`: recall within 1, flagged within 4 | (signals, no gate) |
| TXE-D proxy (`rescore_boxmapLA/prep/rebench.py`: the committed per-setting top-k re-joined; old map reproduces all 10 bench files) | best sr4 0.192 vs plain 0.216, fixed 9 / broken 1, p 0.0215 | sr4 **0.190 vs plain 0.207, 8 / 1, p 0.039**; combo 0.187, 10 / 3, p 0.092 | FAIL (gate p < 0.01), unchanged |

TXE-J stab was not re-run (its stability prior needs the jitter re-cut of every box); none of its 4 breaks is on a shifted box.

## Does the conclusion change?

- **Every txeng verdict stands as a gate result**: no experiment's registered gate (fixed > broken with p < 0.01, or the doubt/tile-gate
  recall bars) is met on the right boxes either.
- **The compare family's "wrong direction" is mostly the map.** TXE-A (4 / 16, p 0.012 against), its M1b re-resolutions (2 / 12) and
  TXE-S (0 / 7, p 0.016 against) were the three runs behind "under rule 3's third-attempt clause the compare family is retired"
  (library/RESULTS.md). On the right boxes they are 3 / 6, 2 / 1 and 0 / 1: no sign of help, but no significant harm either, and the
  retirement rested on three attempts whose damage was mostly wrong tiles. Rule 3's clause logs such a family "untested-by-this-tool",
  not refuted; the rescore says the three attempts were not clean tests of the compare layout on 4 of 12 dev lines. Whether to reopen
  it is the lane's call.
- TXE-K's single break per arm was on a wrong tile; on the right boxes the adjudicator changed nothing scored (its FAIL stands: it
  fixed nothing either). TXE-L's ordered-vs-shuffled comparison, TXE-C, TXE-J, TXE-D/D2, TXE-F and TXE-O are not materially affected.
- The doubt feed's `show` signal halves its flag rate on eval at the same recall: relevant to anyone building a sorter queue from it.

Subfolders: one-paragraph RESCORE.md in compare/, library/, adjud/, shuffle/, gate/, doubt/, prep/, pair/, stab/ point here.
