# TXE3-9 PINS -- RESCORE (11 Oct 2026, 17:0x UTC by date -u)

**Measurement correction: box-to-position map fixed (off by one), not a new gate look.**

Job x20-and-9 for the account-3 parent (session_0198Cv8ypBfBVfRToKVWx33M). No vision call, no reader, no image, no network
beyond git. No truth file, BENCHMARK-TX.tsv row or frozen confirm item was opened for editing.

## What was wrong and what changed

`run_pins.py` (and X20's `x20_owner.py` before it) joined sorter tile ids to no.87 positions through
`atlas/no87_box_token.tsv`. That file is a DP over box widths only, and it never looks at labels. On f178v L06 it gave token 9
to tile f178v_06_009, which the owner had marked NOT-LETTER, so every later tile on that line landed one position late. Lines
L06, L09, L11, L13, L21 and f179r L03 were affected. TXE3-9's second check found it: of the wrong pins, 32 of 35 kept and 3 of
5 owner pins equalled the truth at +/-1. The truth-free check on the old map put seed = L at 157 of 208 tiles, with 24 at -1
and 14 at +1. On the new map it is 188 of 203, with 1 at -1 and 2 at +1 (`no87_map.py --label-aware --check`).

**The only thing changed is the map file.** It is now `atlas/no87_box_token_labelaware.tsv` (`tools/box_token_align.py`,
commit ed5d42162). The run was otherwise exactly as committed:

    M=ciphers/nevers-birago-fr3251-1572/atlas/no87_box_token_labelaware.tsv
    python3 benchmark-tx/txeng2/sorter/x20_owner.py --map $M --tag boxmapLA            # arm c2 (X20) rebuilt
    python3 benchmark-tx/txeng3/9/run_pins.py build --map $M --x20 benchmark-tx/outputs/birago1572-no87/passX20_owner_boxmapLA.tsv --dir benchmark-tx/txeng3/9/rescore_boxmapLA
    python3 benchmark-tx/txeng3/9/run_pins.py score  (same three flags)
    python3 benchmark-tx/txeng3/9/rescore_boxmapLA/rescore_tables.py                   # tx_bench CLI, both masks -> rescore.json

`--map`, `--x20` and `--dir` (run_pins.py) and `--map`/`--tag` (x20_owner.py) are new. Without them, both scripts write
byte-identical files: `run_pins.py build` reproduces `outputs/SHA256SUMS.prescore`, and `x20_owner.py --check` reports
current. The rebuilt arm outputs were hashed (`rescore_boxmapLA/outputs/SHA256SUMS.prescore`) and pushed (b54d2eae6) before
anything was scored.

**Identity checks (map-independent parts).** `base_topk.tsv`, `key_pins.tsv` and `decode_{a,b,a1,b1}.tsv` are byte-identical
to the originals. The arm outputs `pins_{a,b,a1,b1}` differ only in their comment line. P_L is identical. The shuffled-key
control with P_L is identical (real 29/712, rank 1 of 101, z 4.3).

**Pin sets.** P_O went from 19 to 20, P_LO from 26 to 27, and P_S from 205 to 203 (kept 179 -> 176). P_S pins that differ from
the lattice top-1 fell from 50 to 15 (`build.json`).

## Results, whole no.87 (`tools/tx_bench.py --bench BENCHMARK-TX.tsv --item birago1572-no87 --exclude-flagged`; Wilson 95%)

| arm | what | before: as measured | before: flagged excl. | **after: as measured** | **after: flagged excl.** |
|---|---|---|---|---|---|
| a | lattice lam 4, no pins (map-free) | 0.049 (39/803) 0.036-0.066 | 0.035 (28/792) | same | same |
| b | a + P_L (map-free; the gate arm) | 0.045 (36/803) 0.033-0.061 | 0.032 (25/792) | same | same |
| c | L (map-free) | 0.042 (34/803) 0.030-0.059 | 0.029 (23/792) | same | same |
| b2 | a + P_LO (labels + owner 4 Oct) | 0.050 (40/803) 0.037-0.067 | 0.037 (29/792) | **0.047 (38/803) 0.035-0.064** | **0.034 (27/792)** |
| c2 | X20 (owner 4 Oct applied after L) | 0.047 (38/803) 0.035-0.064 | 0.034 (27/792) | **0.046 (37/803) 0.034-0.063** | **0.033 (26/792)** |
| b3 | a + P_S (+ kept seeds; exploratory) | 0.092 (74/803) 0.074-0.114 | 0.080 (63/792) | **0.049 (39/803) 0.036-0.066** | **0.035 (28/792)** |
| a1 / b1 | lam 1 (map-free) | 0.087 / 0.085 | 0.074 / 0.072 | same | same |

Per unit (position errors, `rescore_boxmapLA/score/units.tsv`, as measured):

| arm | dev_tune before -> after | eval_heldout before -> after |
|---|---|---|
| b2 | 15/343 -> 15/343 | 17/376 -> **15/376** (= a, b, c) |
| c2 | 15/343 -> 15/343 | 16/376 -> **15/376** |
| b3 | 22/343 -> **15/343** | 38/376 -> **16/376** |

## Paired, sign-level position McNemar (`--paired`; the two masks agree everywhere)

| pair | what it isolates | before: fixed / broken, p | **after** |
|---|---|---|---|
| b vs a, b vs c, a vs c, b1 vs a1 | map-free | 3/0 0.25; 4/5 1.00; 4/8 0.39; 3/1 0.63 | same |
| b2 vs a | labels + owner pins | 4 / 5, 1.00 | **4 / 3, 1.00** |
| b2 vs c | | 3 / 8, 0.23 | **4 / 7, 0.55** |
| b2 vs c2 | pinned inside vs X20 after L | 3 / 4, 1.00 | **4 / 4, 1.00** (against the rebuilt X20) |
| b2 vs b | the owner's 4 Oct pins alone | 1 / 5, 0.22 | **1 / 3, 0.63** |
| b3 vs a | | 4 / 33, <0.0001 | **4 / 4, 1.00** |
| b3 vs c | | 3 / 36, <0.0001 | **4 / 8, 0.39** |
| b3 vs b2 | the kept seeds alone | 0 / 28, <1e-8 | **0 / 1, 1.00** |
| c2 vs c | X20 vs L, whole item | 0 / 4, 0.13 | **0 / 3, 0.25** |
| b3 after vs b3 before | the map fix itself | -- | 30 / 1 |

## The pins, position by position (the harness's naive lookup; `rescore.json` "pins")

| set | before: scored, right / wrong | after: scored, right / wrong | arm a right at those positions (after) | wrong pin = truth at +/-1 (before -> after) |
|---|---|---|---|---|
| P_L | 7, 7 / 0 | 7, 7 / 0 | 4 | 0 -> 0 |
| P_O (owner 4 Oct) | 18, 13 / 5 (72%) | **19, 16 / 3 (84%)** | 19 | 4 -> 1 |
| kept seeds | 172, 137 / 35 (79.7%) | **168, 166 / 2 (98.8%)** | 166 | 32 -> 0 |
| P_S | 197, 157 / 40 | **194, 189 / 5** | 189 | 36 -> 1 |

After the fix, the 3 wrong owner pins are:
- f178v L01.8 T65. This is X20's cluster rule from the family sort on other letters, not a move on no.87.
- f178v L02.8 T60. The owner moved the tile out of T60 into a new one-tile pile T60-d, and it is scored as T60.
- f178v L11.9 T83. The owner moved the tile out of T83 into a one-tile pile T83-b, and it is scored as T83. Under the old map
  this tile sat in a 1:2 box and was never pinned.

The old wrong pins at L11.20, L13.20 and L21.13 were map shifts. Each tile now lands where L already carries the owner's sign.

The 2 wrong kept pins are f178v L22.2 T60 and f179r L02.8 T24. At both, L and arm a are wrong as well.

Pinned inside vs written over arm a afterwards (the first verifier's comparison, now computed by `rescore_tables.py`):

| pins | before: after / inside, neighbours moved | after: after / inside, neighbours moved |
|---|---|---|
| P_LO | 0.051 (41) / 0.050 (40), 1 (f178v L02.9, a fix) | 0.049 (39) / 0.047 (38), 1 (f178v L02.9, a fix) |
| P_S | 0.092 (74) / 0.092 (74), 7 | 0.049 (39) / 0.049 (39), 2 (f178v L02.9 fix; f179r L02.9 T92 -> X_NEW, a break) |

## Controls (rule 3), re-run as committed

1. **Shuffled key with P_LO: PASS, unchanged.** Real unpinned error went from 28/694 to 28/693, rank 1 of 101 both times;
   shuffled 0.078-0.170; z went from 4.27 to 4.29.
2. **Random pass-A pins of equal count.** The pool went from 521 to 524 positions because P_S moved. Naive wrong signs on the
   26 lattice lines:

   | set | real arm, before -> after | random band (min / mean / max), after | real pins right, before -> after | random pass-A pins right, after |
   |---|---|---|---|---|
   | P_LO | b2 33 -> **31** | 31 / 32.35 / 34 | 20/25 -> **23/26 (88%)** | 25.0/27 (93%) |
   | P_S | b3 68 -> **32** | 31 / 33.15 / 36 | 157/197 -> **189/194 (97%)** | 191.85/203 (95%) |

   Before the fix, the owner-seen set sat far outside the random band (68 against 29-36). After the fix it sits inside the
   band, and its pins are right more often than random pass-A pins.

## Does each conclusion change?

| # | conclusion as written (RESULTS.md / VERIFY.md) | after the map fix | changes? |
|---|---|---|---|
| 1 | Gate NOT met; verdict null | Arms a, b and c never touched the map, so this is unchanged. | **No** |
| 2 | Pinning inside = applying after; no neighbour moved (P_L) / 1 neighbour (P_LO) | P_L: 0 neighbours. P_LO: 1 (L02.9). P_S: 7 -> 2. | **No** (the P_S exception shrinks) |
| 3 | Owner 4 Oct moves, pinned, "break five signs and fix none" (VERIFY: 1 fixed by context / 5 broken, p 0.22; 13/18 right) | 3 broken at the pins, 1 fixed by context (L02.9). b2 vs b is 1 / 3, p 0.63, and 16/19 pins are right. All 3 breaks are on dev. On eval, b2 = a = 15/376 (was 17/376). | **Magnitude yes, direction no.** The owner pins still fix nothing at the pinned positions, and the net -2 is not significant. Of the 3 breaks, 1 is X20's cross-letter cluster rule and 2 are tiles the owner separated into one-tile split piles that the harness scores as the parent family. |
| 4 | Pinning kept tiles is destructive: "33 broken vs a" (VERIFY: 0 / 28 for the kept tiles alone); kept seeds ~80% right; "a tile you did not move must never be reused as a decision" | Kept alone is 0 / 1 (p 1.00); the 1 is a context move at f179r L02.9. b3 = a on count (39/803). Kept seeds are 166/168 right, and differ from arm a at only 5 of 176. | **Yes, reversed.** On no.87, pinning the kept seeds is neutral: it breaks none at the pins and fixes none. The damage measured before was the map. "A kept tile is a machine seed, not an owner decision" is still true by definition, but no measured harm now supports "must never be reused". |
| 5 | Owner-seen sets are worse than random pass-A pins (VERIFY: "supports the substance of claim 2") | P_S is now better than random pass-A (97% vs 95%) and inside the random wrong-count band. P_LO is still a little below random (88% vs 93%). | **Yes** for P_S; **no** for P_LO |
| 6 | Near-tie paragraph (24 positions) | `base_topk.tsv` is identical. Unchanged, with VERIFY.md's objection 4 standing. | No |
| 7 | Second check, objection 9: the owner/kept arms are "untested by this design" because of the map | With the corrected map they are now measured, as secondary or exploratory numbers with no gate. | Superseded by this file |

**Corrected owner sentence (replaces RESULTS.md's second owner sentence).** On no.87, your 4 Oct moves, locked into the
decoder, fixed nothing at the locked positions and broke 3 by the clerk's sheet. All 3 are on the tuning lines:
- one is a rule we carried over from your family sort on other letters;
- two are tiles you split off into new one-tile piles, which our scoring counts as the pile you split them from.

Locking in the tiles you left in place changed nothing (0 fixed, 1 broken, not significant), because they already agree with
the decoder at all but 5 of 176 positions.

## Follow-ups (one line each, not run)

- X6 (`benchmark-tx/txeng2/sorter/`, `tools/tx_sorter_curve.py --map atlas/no87_box_token.tsv`) used the old map, including
  the cluster-impurity figure "77.3% majority share" that RESULTS.md cites beside the kept-seed result. Re-run it with the
  label-aware map (script-only, no reader).
- Whether a one-tile split pile (T60-d, T83-b) should be scored as its parent family is a scoring-rule question for the lane.
  It is not settled here; scoring it any other way would be a new design, not a re-run.
- TXE3-7's `sorter/no87/owner_map.tsv` joins family-sort tiles on f.117/f.144/f.168 to atlas boxes by pixel distance. It is
  not the no.87 DP, and it was left unchanged as the brief said. X20's one family-sort move (L01.8) is the same under both
  maps.

## Files
- `run_pins.py` (with `--map`/`--x20`/`--dir`).
- `rescore_boxmapLA/`, which holds:
  - `pins_*.tsv`, `decode_*.tsv`, `base_topk.tsv`, `key_pins.tsv`, `build.json`;
  - `outputs/pins_*.tsv` + `SHA256SUMS.prescore`;
  - `score/{score.json,units.tsv,paired.tsv,changed_*.tsv}`;
  - `rescore_tables.py` -> `rescore.json`.
- X20's rebuilt files: `benchmark-tx/outputs/birago1572-no87/passX20*_boxmapLA.tsv` and
  `benchmark-tx/txeng2/sorter/x20_changes_boxmapLA.tsv`.

Cost: compute only, with no subagent and no vision call. Build 4 s, score 17 s, tables 10 s. The dollar figure is the
orchestrator's `get_session`.
