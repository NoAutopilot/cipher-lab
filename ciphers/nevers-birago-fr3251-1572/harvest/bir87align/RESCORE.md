# BIR87-ALIGN -- RESCORE (11 Oct 2026, 18:0x UTC by date -u)

**Measurement correction: box-to-position map fixed (off by one), not a new gate look.**

Job BOXMAP-RESCORE (others) for the account-3 parent (session_0198Cv8ypBfBVfRToKVWx33M). Script-only: no vision call, no reader, no
image viewed, no network beyond git. No key, exceptions file, reading, truth file or BENCHMARK-TX.tsv row changed.

`relabel.py` gave no.87 tokens the owner's pile labels by joining sorter tiles to tokens through `atlas/no87_box_token.tsv`, which is
one token off on 10 of 26 lines (`../../atlas/RESCORE.md`), so on those lines a tile's pile went to the neighbouring token. **Only the
map changed.** `relabel.py --map FILE --dir DIR` and `run.py --dir DIR` are new; without them both write the committed files
byte-identically (checked). `rescore_boxmapLA/disagreements.py` is new: it rebuilds `disagreements.tsv` (committed on 4 Oct without its
script) and, with the old map and the committed run, reproduces it row for row. From `harvest/bir87align/`:

    python3 relabel.py --map ../../atlas/no87_box_token_labelaware.tsv --dir rescore_boxmapLA
    python3 run.py --dir rescore_boxmapLA                                  # about 8 min, 20 shuffled-sheet seeds
    python3 rescore_boxmapLA/disagreements.py ../../atlas/no87_box_token_labelaware.tsv rescore_boxmapLA rescore_boxmapLA/disagreements.tsv

Step 3 (from the repo root; `rescore_boxmapLA/pile_values_C.tsv` = the C rows of the rescored `piles.tsv`):

    N=ciphers/nevers-birago-fr3251-1572/harvest
    python3 $N/ownersort/ownersort.py --new-piles-unknown --corrections $N/bir87align/settled_corrected.tsv \
      --pile-values $N/bir87align/rescore_boxmapLA/pile_values_C.tsv [--pv-moved-only] --tag bir87[_moved]_boxmapLA
    # -> ownersort/v4_bir87_moved_boxmapLA/, ownersort/v4_bir87_boxmapLA/ ; with the committed pile_values_C.tsv the moved-only
    #    command reproduces ownersort/v4_bir87_moved/score.json exactly (checked)

## Step 1: sequences (`rescore_boxmapLA/relabel_counts.json`)

no.87, 853 tokens. Owner-labelled: 205 (186 kept, 18 moved, 1 not-letter) -> **202 (183 kept, 19 moved, 0 not-letter)**: the
NOT-LETTER tile f178v_06_009 is now skipped, as the owner marked it; f178v_11_009 (1:2 before) is now one-token and brings the one-tile
pile T83-b into the sequence. Piles reached: T45 52, T60 43, T37 41, T19 36, T89-b 10, X_NEW-l 7, T24-b 6, T86 2, T83-b 1, T60-d 1,
T85-b 1, T85 1, T33 1.

## Step 2: clerk-sheet alignment

| sequence | real 'agrees' before -> after | shuffled mean / max after | gate |
|---|---|---|---|
| committed labels | 0.896 -> 0.896 (map-free) | 0.351 / 0.376 | pass |
| **owner piles (primary)** | **0.848 -> 0.892** | 0.325 / 0.348 | pass |
| owner moves only | 0.890 -> 0.891 | 0.350 / 0.375 | pass |

Per owner pile, primary (C = n >= 2, agree >= 2, share >= 0.6, above the pile's own shuffled max):

| pile | before: n, value, share, grade | **after** |
|---|---|---|
| T45 | 52, e, 0.827, C | 51, e, **1.000**, C |
| T60 | 43, n, 0.860, C | 43, n, **0.977**, C |
| T37 | 42, a, 0.690, C | 41, a, **1.000**, C |
| T19 | 36, o, 0.861, C | 36, o, **1.000**, C |
| X_NEW-l | 7, o, 0.857, C | 7, o, 1.000, C |
| T89-b (word) | 10, che, 0.400, M | 10, che, **0.700, C** |
| T24-b | 6, f, 0.500, M | 6, f, **0.833, C** |
| T86 | 2, n, 0.500, M | 2, n, 0.500, M |
| T60-d, T85-b, T85, T33, (new) T83-b | 1 each: no evidence | 1 each (T83-b z): no evidence |

Every C value is still the printed 1572 value of the pile's family (T45 e, T60 n, T37 a, T19 o; now also T24-b f and T89-b che). Moves
only (sensitivity): T37 a 6/6 C, T60 n 5/5 C, T24-b f 3/3 M (not above its null), the rest no evidence.

## Where the owner pile and the committed label differ (`rescore_boxmapLA/disagreements.tsv`)

| | before (60 tokens) | **after (29 tokens)** |
|---|---|---|
| kept: clerk sides with committed / pile / both / neither | 30 / 1 / 11 / 11 (53) | **0 / 1 / 16 / 6 (23)** |
| moved: committed / pile / both / neither | 2 / 2 / 2 / 1 (7) | **0 / 2 / 4 / 0 (6)** |

## Step 3: re-decode gate (BIR-OWNER random-change control, 200 draws, seed 20261004)

The new C set adds T24-b (f) and T89-b (che); one f.117r tile (T24-b) and one f.168 tile (T89-b) now take a value instead of '?'.

| leaf | before: b, rank /201 (moves only) | **after** | before: as pre-registered | **after** |
|---|---|---|---|---|
| f.117r | -1.337, 39 | -1.336, 45 | -1.376, 70 | -1.375, 80 |
| f.144r | -1.655, 61 | -1.655, 58 | -1.655, 58 | -1.655, 63 |
| f.168 | -1.583, 194 | -1.557, 190 | -1.583, 193 | -1.557, 194 |
| pooled | -1.449 (p95 -1.398) | -1.443 (p95 -1.376) | -1.472 | -1.466 |

FAIL on every leaf and pooled, as before.

## Does the conclusion change?

- **The verdict holds and the key-value finding strengthens.** Every testable pile still takes exactly its printed value, now with
  near-perfect agreement (T45, T37, T19 1.000; T60 0.977), and two more piles reach C at their printed values. The re-decode gate still
  FAILs; BIR-ADJ's conflict is still not explained by wrong key values.
- **Two sentences reverse.** "The primary run's lower agreement (0.848 vs 0.896) is mainly these seeded kept tiles" -- it was the map:
  owner piles agree 0.892 against the committed labels' 0.896. "The seed's re-pilings the owner left in place are mostly wrong by the
  clerk" (clerk with committed 30, pile 1) -- with the right join the clerk sides with the committed label against the owner's pile on
  **0** of the 29 differing tokens; most differences are the owner's own new piles (X_NEW-l, T89-b, T24-b) carrying the same value as
  the committed sign. "The owner's own moves split evenly at this N" -> moved tokens: pile 2, both 4, committed 0.
- "No REAL homophone split is supported" stands (T19 vs X_NEW-l: both C, both o -> over-split, merge recommended; still not applied).
