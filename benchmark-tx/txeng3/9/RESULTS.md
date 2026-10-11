# TXE3-9 PINS: owner decisions as hard pins in the key-constrained lattice decode (Birago no.87) -- RESULTS

Worker TXE3-9 (account 3, Fable), 11 Oct 2026 05:48-06:0x UTC by date -u, for the account-3 parent
(session_0198Cv8ypBfBVfRToKVWx33M). PREREG `benchmark-tx/PREREG-txeng3-9.md` (commit 9be06341, register check `OK ... names
register rows and states a difference`), committed before any decode was scored; the six arm outputs committed with hashes
(`outputs/SHA256SUMS.prescore`, commit 7fd2dcf1) before `tools/tx_bench.py` ran. Read-free: no vision call, no reader, no
network; every number is a computation over the two blind passes already on disk. No frozen confirm item opened; no truth
file edited.

**Verdict: null (dev-FAIL on the brief's gate). Pinning the decided signs inside the decode gives the same reading as applying
them after it, apart from the three positions the decoder had at a coin-toss; no neighbouring sign moved through context.**

## What was built
`tools/key_decode_lattice.py decode --pins FILE` (commit 4dc3f12f): a TSV line, pos, sign of decided positions; at each the
candidate set becomes {sign: 1.0} before the Viterbi pass (`read_pins`, `apply_pins`); the JSON reports pins read / applied /
unmatched / differing from top-1; `P.decode.tsv` gains a `pinned` column and grade_cap `pin` (never S) at pinned rows.
Offline test `tools/tests/test_key_decode_lattice.py::test_pins_hold_position_and_report` (14/14 pass). Harness
`benchmark-tx/txeng3/9/run_pins.py` (`build` writes outputs without reading truth; `score` reads truth and runs the controls).

## Fixed inputs (as pre-registered)
Lattice = TX-DECODE's recipe through `benchmark-tx/txeng/conf/run_conf.py` (passes A/B of f178v + f179r, passC skeleton,
confusion_1572, no matrix, no stability), all 26 lattice lines (756 positions); arm (a) reproduces the committed
`passL_lattice_dev_tune_lam4.tsv` and `_lam1.tsv` byte for byte on the dev lines (identity check passed). Key
`key_pins.tsv` = key_1572_sheet.tsv + X_CE = s. LM it16dip, beam 64, lam 4 (lam 1 beside). f178r from L in every arm.
Pin sets (`pins_*.tsv`): P_L = the 7 NO87-LABELS X_CE relabels (all dev_tune); P_O = the owner's 4 Oct 2026 decisions as
X20 reads them (18 moved tiles at a T family, 1:1 boxes, + 1 family-sort cluster decision = 19; 11 dev, 8 eval; 6 differ
from L); P_LO = 26; P_S (exploratory) = P_LO + the owner's 179 `kept` tiles at their seeded pile family = 205 (43 differ
from L).

## Results, whole no.87 (`tools/tx_bench.py --item birago1572-no87 --exclude-flagged`; Wilson 95%; never the second figure alone)

| arm | what | as measured | flagged excluded | vs L (c): fixed / broken, p | vs (a): fixed / broken, p |
|---|---|---|---|---|---|
| a | lattice lam 4, no pins | 0.049 (39/803) 0.036-0.066 | 0.035 (28/792) 0.025-0.051 | 4 / 8, 0.39 | -- |
| **b** | **a + P_L pins (the brief's arm)** | **0.045 (36/803) 0.033-0.061** | **0.032 (25/792) 0.021-0.046** | **4 / 5, 1.00** | **3 / 0, 0.25** |
| c | L = reconcile + labels after (today's output) | 0.042 (34/803) 0.030-0.059 | 0.029 (23/792) 0.019-0.043 | -- | 8 / 4, 0.39 |
| b2 | a + P_LO pins (labels + owner 4 Oct) | 0.050 (40/803) 0.037-0.067 | 0.037 (29/792) 0.026-0.052 | 3 / 8, 0.23 | 4 / 5, 1.00 |
| c2 | passX20_owner (owner 4 Oct applied after) | 0.047 (38/803) 0.035-0.064 | 0.034 (27/792) 0.024-0.049 | 0 / 4, 0.13 | (b2 vs c2: 3 / 4, 1.00) |
| b3 | a + P_S pins (owner-seen, kept seeds too) | 0.092 (74/803) 0.074-0.114 | 0.080 (63/792) 0.063-0.100 | 3 / 36, <0.0001 | 4 / 33, <0.0001 |
| a1 | lattice lam 1, no pins | 0.087 (70/803) 0.070-0.109 | 0.074 (59/792) 0.058-0.095 | 7 / 42, <0.0001 | -- |
| b1 | a1 + P_L pins | 0.085 (68/803) 0.067-0.106 | 0.072 (57/792) 0.056-0.092 | 7 / 40, <0.0001 | 3 / 1, 0.63 |

Fixed / broken = sign-level position McNemar from `--paired` (exact sign test p); line-level sign tests in `score/`.
Per unit (position errors, `score/units.tsv`): dev_tune a 16/343, b 13/343, c 12/343; eval_heldout a = b = 15/376 (identical
BY CONSTRUCTION: every P_L pin lies on a dev line, as pre-registered), c 15/376. b2 eval 17/376 (the two owner moves on eval,
f178v L13.20 T98->T37 and L21.13 T85->T60, both wrong by the clerk sheet).

**Gate: NOT met.** err(b) + its Wilson half-width (0.045 + 0.014) is above err(a) and above err(c); (b) is 3 signs better than
(a) and 2 signs worse than (c). The pre-registered prediction (a null, b ~ c, both below a by about the relabel count) held.

## What the pins did, sign by sign (`score/changed_b.tsv`)
- Arms (a) and (b) differ at exactly the 7 pinned positions and nowhere else: a hard pin moved no neighbouring sign through
  the n-gram context. At those 7 the blind-pass lattice holds T92 (s) 0.473 against T50 (c) 0.457 -- a near tie; (a) chose
  T92 at 4 (right at value level) and T50 at 3 (wrong, f178v L04.4, L05.25, L08.10); the pin settles all 7 to X_CE (s). That
  is the whole 3 fixed / 0 broken.
- (b)'s 24 unpinned changes from top-1 (grade S, never H): 6 fixed (top-1 wrong -> right: L06.8, L06.18, L09.1, L11.29,
  L13.20, L15.14 -- four are T24->T29 and two the d pair T98->T18), 3 broken (right -> wrong: L02.9 T49->X_NEW, L03.24
  T11->X_NEW, L10.3 T18->T98), 11 wrong -> wrong, 4 unscored. These are the lattice's own TX-DECODE changes, unchanged by pins.
- (b) vs (c): 4 fixed / 5 broken -- the lattice fixes two d (T98/T18) and T60->T86 at L11.29 that L has wrong, and breaks
  L02.9, L03.24, L10.3, L11.4, L20.15 that L has right. The two outputs are a wash at 803 signs.
- Owner 4 Oct pins (P_O inside b2): 25 scored pins, 20 right / 5 wrong by the clerk sheet (L01.8 T95->T65, L02.8 T42->T60
  [the TX-TRUTH-VERIFY CORRECT row], L11.20, L13.20, L21.13); at 24 of the 25 the lattice top-1 was already right. Pinned
  inside the decode they do what X20 found applying them after: 0 fixed, 5 broken against the top-1.
- Owner-seen pins (P_S inside b3): 197 scored, 157 right / 40 wrong -- the 40 are seeded pile labels the owner left in place
  (`kept`), not decisions; pinning them is destructive (33 broken vs a). A kept tile is not a decision and must not be reused
  as one (consistent with X6: the seeds carry about 77% majority value).

## Controls (rule 3; `score/score.json` "controls")
1. **Shuffled key, same lattice, same pins (must not help): PASS.** 100 value-shuffled keys (seed 1), err on the 712 unpinned
   scored positions: real key 0.041 (29/712), rank 1 of 101; shuffled 0.076 min / 0.122 mean / 0.170 max; mean 4-gram z 4.3
   (real -0.935 vs shuffled max -1.165). With P_LO: real 0.040 (28/694), rank 1 of 101, shuffled 0.079-0.169, z 4.27. The
   control varied (every shuffle changed the unpinned choices), and none read as well as the real key: the (small) gain is not
   the language model inventing text. 4.3 s per 100 shuffles.
2. **Random pins of equal count from pass A (pinning itself vs the owner's quality): the real pin sets are not "pinning".**
   20 seeds each, random scored lattice positions outside the owner/labels set, pinned to pass A's aligned sign; base lattice
   32 wrong of 719 scored on the lattice lines.
   | n | random pass-A pins: wrong (min/mean/max) | fixed / broken vs a (means) | pins right | the real set at this n |
   |---|---|---|---|---|
   | 7 (P_L) | 31 / 32.0 / 33 | 0.10 / 0.10 | 6.6 of 7 | 3 fixed / 0 broken; 7 of 7 right |
   | 26 (P_LO) | 31 / 31.9 / 34 | 0.25 / 0.15 | 24.6 of 26 | 4 fixed / 5 broken; 20 of 25 scored right |
   | 205 (P_S) | 29 / 32.8 / 36 | 2.05 / 2.80 | 194.2 of 205 | 4 fixed / 33 broken; 157 of 197 scored right |
   Seven random pins do nothing (they land where the lattice already agrees with pass A); the 7 relabels fix 3 because they
   sit on the only positions where the lattice was tied -- the value of a pin is where it sits, not that it is pinned. At 26
   and 205 the owner's sets are WORSE than random pass-A pins: pass A is right at 94.7% of random positions, the owner's
   4 Oct moves at 80% (20/25) and the owner-seen seeds at 79.7%.
3. Identity shape (stated in the PREREG): eval_heldout (a) == (b) by construction for P_L; not a null on eval.

## What it means for the owner (three sentences)
Holding your decided signs fixed inside the decoder gives the same reading as applying them afterwards, except at the three
places where the decoder had been tossing a coin between two look-alike signs, and it never changed a neighbouring sign. Your
4 October moves on no.87, pinned, break five signs by the clerk's own sheet and fix none, and pinning the tiles you merely left
in their seeded piles breaks 33, so a tile you did not move must never be reused as a decision. The decoder's remaining errors
sit at 24 positions where its two best candidates are within 0.05 of each other (5 of its 32 wrong signs are there), and those
are the tiles worth asking you about, not the ones a ranking by cluster size or doubt count picks.

## Cost per run and what this cost
One Viterbi pass over the 26 lines (756 positions, beam 64) takes 0.01-0.05 s; the full build (6 arms) 3.7 s, the score stage
with 200 shuffled-key and 60 random-pin decodes 13.8 s. Dollar cost of this session: the orchestrator's `get_session` figure
(not visible to the worker); no subagent, no vision call. Box 05:48-07:48 UTC; finished well inside it.

## Next step, with its cost
Not a further pin experiment on no.87 (the mechanism is exhausted at this N: 3 signs). Two read-free follow-ups, about USD 1
each, 10 minutes, Sonnet or a script: (1) feed the lattice's near-tie positions (top-2 gap < 0.05; 24 on no.87, 5 of them
wrong) to the sorter as the focus list in place of the doubt-count ranking, and score the owner's next session's decisions on
them against BENCHMARK-TX (TRANSCRIPTION.md item 7, "the tiles whose answer moves the reading most"); (2) run `--pins` in the
f.117 / f.144 / f.168 decodes with the owner's four family-sort cluster decisions as pins under the folders' own PREREG and
power control, expecting a change of a few signs at most. A re-check of the five wrong 4 Oct moves against the clerk image is
an owner-side sorter item (about 10 tiles), not a worker job.

## Files
`PREREG-txeng3-9.md`; `run_pins.py`; `key_pins.tsv`; `pins_P_L.tsv`, `pins_P_O.tsv`, `pins_P_LO.tsv`, `pins_P_S.tsv`;
`base_topk.tsv`; `decode_{a,b,b2,b3,a1,b1}.tsv`; `outputs/pins_*.tsv` + `SHA256SUMS.prescore`; `build.json`;
`score/score.json`, `score/units.tsv`, `score/paired.tsv`, `score/changed_{a,b,b2,b3}.tsv`.
