# TXE3-9 PINS -- verifier's check (11 Oct 2026, 15:29 UTC by date -u)

Verifier for the account-3 parent (session_0198Cv8ypBfBVfRToKVWx33M). I did not run TXE3-9 and do not protect its
conclusions. Method: re-derived from committed files only, in a sparse worktree at origin/main adc6909af. No model reading
pass, no image, no network beyond git, no sorter page or L74 oracle touched, no frozen confirm item opened. The experiment's
own files are unchanged; this file is the only one committed.

## Verdicts on the two claims told to the owner

| # | Claim as told | Verdict | Corrected sentence |
|---|---|---|---|
| 1 | Locking the owner's decisions into the decoder gives the same result as applying them afterwards. | **overstated** (mildly) | On Birago no.87, locking decided signs into the decoder gave almost the same output as writing them over it afterwards. For the 7 label rulings the two were identical. For your 19 decisions of 4 Oct one neighbouring sign changed (f178v L02.9, a fix). Neither way gained anything. This is one letter, and only 13 of the pins differed from what the decoder had already chosen. |
| 2 | A tile he merely left in place must never be counted as a decision (pinning kept tiles broke 33 signs); his 4 Oct moves pinned broke 5 and fixed none. | **overstated** | Treating tiles you left in their seeded piles as decisions is harmful on no.87, so don't count them as decisions. Pinning them broke 28 signs and fixed none. That arm was registered as exploratory, and the pinned value is the machine's seed label, not your choice. Your 4 Oct moves, pinned, were wrong at 5 of their 18 scored positions, where the decoder already had all 18 right. Through context they fixed one neighbouring sign, so the net was 1 fixed and 5 broken (p 0.22). One of the 5 is a family-sort cluster ruling made on other letters, and one sits on a truth row marked corrected:key-doubtful. |

Why claim 2 is overstated: the 33 is arm b3 against arm a. Arm b3 pins the label rulings, the 4 Oct moves and the kept
tiles all together, so the 33 already includes the 5 breaks from the 4 Oct moves. The kept tiles' own increment (b3 against
b2, `tx_bench --paired`) is 0 fixed and 28 broken: 27 at the kept positions and 1 through context, exact p < 1e-8.
"Fixed none" is true only at the pinned positions themselves. Adding the 4 Oct moves to arm b gives 1 fixed and 5 broken.

## Re-derivation (committed scorer `tools/tx_bench.py --bench BENCHMARK-TX.tsv --item birago1572-no87 --exclude-flagged`)

The six arm outputs match `outputs/SHA256SUMS.prescore` and are unchanged since the prescore commit 7fd2dcf1. I re-ran
`run_pins.py build` from a scratch copy and every output, decode, pin set, key, top-k file and build.json came back
byte-identical. Re-running `run_pins.py score` reproduced score.json except for its two timing fields, and the other score
files byte-identical.

| arm | reported as measured | re-derived | reported flagged-excl. | re-derived |
|---|---|---|---|---|
| a lattice lam 4 | 0.049 (39/803) 0.036-0.066 | 0.049 (39/803) 0.036-0.066 | 0.035 (28/792) | 0.035 (28/792) |
| b + P_L | 0.045 (36/803) 0.033-0.061 | 0.045 (36/803) 0.033-0.061 | 0.032 (25/792) | 0.032 (25/792) |
| c = L | 0.042 (34/803) | 0.042 (34/803) | 0.029 (23/792) | 0.029 (23/792) |
| b2 + P_LO | 0.050 (40/803) | 0.050 (40/803) | 0.037 (29/792) | 0.037 (29/792) |
| c2 = X20 | 0.047 (38/803) | 0.047 (38/803) | 0.034 (27/792) | 0.034 (27/792) |
| b3 + P_S | 0.092 (74/803) | 0.092 (74/803) | 0.080 (63/792) | 0.080 (63/792) |
| a1 lam 1 | 0.087 (70/803) | 0.087 (70/803) | 0.074 (59/792) | 0.074 (59/792) |
| b1 lam 1 + P_L | 0.085 (68/803) | 0.085 (68/803) | 0.072 (57/792) | 0.072 (57/792) |

Paired position McNemar (`--paired`, both masks agree):

| pair | reported | re-derived |
|---|---|---|
| b vs a | 3 / 0, p 0.25 | 3 / 0, p 0.25 |
| b vs c | 4 / 5, p 1.00 | 4 / 5, p 1.00 |
| a vs c | 4 / 8, p 0.39 | 4 / 8, p 0.39 |
| b2 vs a | 4 / 5, p 1.00 | 4 / 5, p 1.00 |
| b2 vs c | 3 / 8, p 0.23 | 3 / 8, p 0.23 |
| b2 vs c2 | 3 / 4, p 1.00 | 3 / 4, p 1.00 |
| b3 vs a | 4 / 33 | 4 / 33 |
| b1 vs a1 | 3 / 1, p 0.63 | 3 / 1, p 0.63 |
| **b2 vs b** (the 4 Oct moves alone; not reported) | -- | **1 / 5, p 0.22** (fix: L02.9 by context) |
| **b3 vs b2** (the kept tiles alone; not reported) | -- | **0 / 28** (27 at kept pins + 1 by context) |

Same decoder, pinned inside vs overwritten after. TXE3-9 registered no arm for this. I built it by overwriting arm a (or a1)
with the same pin set and scoring with tx_bench:

| pins | overwrite after | pinned inside | pinned vs after | neighbours moved |
|---|---|---|---|---|
| P_L, lam 4 | 0.045 (36/803) | 0.045 (36/803) | 0 / 0 | 0 of 749 unpinned |
| P_LO, lam 4 | 0.051 (41/803) | 0.050 (40/803) | 1 / 0 | 1 (f178v L02.9) |
| P_S, lam 4 | 0.092 (74/803) | 0.092 (74/803) | 1 / 2 | 7 |
| P_L, lam 1 | 0.083 (67/803) | 0.085 (68/803) | 0 / 1 | 1 (f178v L05.27) |

Pin accuracy, counted the way the harness counts it (naive position lookup):

| set | scored | right | wrong | arm a right at those positions |
|---|---|---|---|---|
| P_L | 7 | 7 | 0 | 4 |
| P_O | 18 | 13 | 5 | 18 |
| P_LO | 25 | 20 | 5 | 22 |
| kept only | 172 | 137 | 35 | 170 |
| P_S | 197 | 157 | 40 | 192 |

## Pre-registration order

| commit | time | content |
|---|---|---|
| 979e75e5 | 05:56:03 | PREREG (authored 05:54:58) |
| 9be06341 | 05:56:03 | wording only: retired instruments named as different |
| 4dc3f12f | 05:57:32 | `--pins` in the tool, with its test |
| 7fd2dcf1 | 05:59:31 | arm outputs and SHA256SUMS.prescore |
| 8c7f5502 | 06:03:49 | RESULTS and score files |

The build path reads no truth: `run_conf.learn` is never called and `matrix=None`. The prereg came before any score, and no
deviation was needed. The gate as registered reads: "(b) beats BOTH (a) and (c) when err(b) + its Wilson 95% half-width <
err(a) and < err(c) on the as-measured whole-no.87 figure". On the numbers, 0.0448 + 0.0144 = 0.0592, which is above both
0.0486 and 0.0423, so the gate is **NOT met**. The reported verdict, null, follows. Calling it "dev-FAIL" mislabels it: the
gate is on the whole of an eval item.

## Controls (rule 3)

**Shuffled key.** It can vary: the Viterbi choice at an unpinned position depends on the key values, and the shuffled runs
did vary (0.076-0.170 against real 0.041, rank 1 of 101; z 4.3 and 4.27). PASS. It controls for the language model
inventing text. It does not test either owner-facing claim.

**Random pass-A pins.** These can vary too: the band was 31-33 wrong at n=7 and 29-36 at n=205. At n=205 they fixed 2.05 and
broke 2.80 on average, against the owner-seen set's 4 fixed and 33 broken. That separates the kept-seed damage from pinning
as such, and supports the substance of claim 2. One caveat: the harness scores this control by naive position lookup, not
by tx_bench's alignment. Arm a has 32 wrong on the lattice lines that way against 31 aligned, and b3 has 68 against 60. The
gap is small and does not flip any comparison.

**Claim 1 has no registered control.** It rests on an identity check that I re-derived, and that check has little power:
only 7 label pins and 6 owner pins differed from the decoder's own choice. Where more pins differed (P_S, 52), context moved
7 neighbours.

## Dev / eval split

The split was registered as dev_tune f178v L01-12 and eval_heldout f178v L13-23 plus f179r L01-03. lam 4 was tuned on the
dev lines in TX-DECODE, so the whole-item headline mixes tuned lines with held-out ones. The prereg declares this and shows
the split. Nothing was chosen on eval.

On eval_heldout, a, b and c all score 15/376 (flagged-excluded 10/371). b2 scores 17/376: two of your eval moves are wrong
(L13.20, L21.13).

## Objections

1. The 33 in claim 2 is misattributed. It is b3 against a, and it includes the 5 breaks from the 4 Oct moves. The kept
   tiles alone broke 28 (b3 against b2). RESULTS.md says "33 broken vs a" for the kept tiles, and the parent copied it.
2. RESULTS.md labels several P_LO figures as the owner's own:
   - "Owner 4 Oct pins (P_O inside b2): 25 scored pins, 20 right / 5 wrong ... at 24 of the 25 the lattice top-1 was already
     right" counts P_LO, so the 7 label pins are included. For P_O alone it is 18 scored, 13 right and 5 wrong; the top-1
     was right at 17 and the decode at 18.
   - "the owner's 4 Oct moves at 80% (20/25)" should read 72% (13/18).
   - "the 40 are seeded pile labels the owner left in place" should be 35 kept and 5 moves.
3. "Fixed none" holds only at the pinned positions. The owner pins fixed f178v L02.9 through context: X_NEW became T49, which
   is right. That pin, L02.8 = T60, is itself one of the 5 wrong. This also contradicts the owner paragraph's "it never
   changed a neighbouring sign". That holds for the 7 label pins at lam 4. It does not hold for the owner's pins (1
   neighbour), for kept pins (7) or at lam 1 (1).
4. The owner paragraph's near-tie sentence has two problems.
   - It is not pre-registered, and no committed script computes it (rule 7). I re-derived it from base_topk.tsv: 24
     positions with a top-2 gap under 0.05, and 5 of arm a's wrong signs among them.
   - It is misleading. "The decoder's remaining errors sit at 24 positions" is false, because 26 or 27 of the 31-32 errors
     sit elsewhere. Also, 3 of the 5 near-tie errors are the X_CE positions the label rulings already fix. After those
     rulings (arm b), 2 of 28 lattice-line errors are near-ties, and 7 of the 24 near-ties are already settled.
   - It should not steer the order of sorter questions (TXE3-1's question) without its own registered test.
5. The registered gate could not be met: the prereg says so itself. So "null" carries no information about pins. Both
   owner-facing claims rest on secondary and exploratory numbers (the paired counts, and the exploratory b3 arm), and they
   should say so.
6. "Offline test 14/14 pass" does not reproduce here: 13/14 pass. `test_probs_top3_replaces_hml` fails on an exact float
   comparison (0.7000000000000002). It also fails at the pre-TXE3-9 commit 387a9d9f, so it is not caused by `--pins`.
   `test_pins_hold_position_and_report` passes.
7. One of the 5 wrong owner moves, L02.8, sits on a truth row flagged `corrected:key-doubtful`. That row stays scored, so
   "broke 5" is measured partly against a truth whose key value is marked doubtful.
8. Rule 3, third-attempt shape. TX-ALTS (not adopted), TXE-E (dev-FAIL), TXE-J (dev-FAIL) and now TXE3-9 (null) each
   changed a different input of the same lattice on no.87, and none passed. RESULTS.md's own "not a further pin experiment
   on no.87" is right. The next lattice attempt on no.87 should need new material, not another knob.

## Rule checks

- **Cost:** USD 11.26, from the parent's get_session (LEDGER 967feff2), under the USD 15 cap and the 12 stop line. Wall
  clock 05:48 to about 06:06.
- **Flagged-excluded figure:** never quoted alone in RESULTS or the ROOM done line.
- **Novelty words:** none.
- **Grading:** pinned positions are graded `pin`, never S.
- **ROOM:** the first done line cited the wrong hash and was corrected at 06:06. The claim line's estimated time was
  corrected at 05:53.

## Second check (11 Oct 2026, written 16:28 UTC by date -u, by the account-3 parent from the second verifier's report; workflow wf_35ed2244-0e6)

A second, independent agent ruled on each objection and non-holds verdict above, re-running the commands itself. Where it disagrees with this file, this section governs.

### Rulings on the first verifier's objections

- **partly**: 1. RESULTS' 'pinning them is destructive (33 broken vs a)' misattributes the 33; the kept tiles alone are 0 fixed / 28 broken (b3 vs b2).
  - Evidence: Re-ran `tools/tx_bench.py --item birago1572-no87 --exclude-flagged --paired` at origin/main c9c20626b.
- b3 vs a: 4 fixed / 33 broken.
- b3 vs b2: 0 / 28.
- b2 vs b: 1 / 5.
So the attribution point is right: the 33 includes the 5 breaks from the 4 Oct moves.

But 28 is not the settled figure for the kept tiles alone:
- The arm outputs and the truth file share the same 853 positions (checked line by line), so a direct position lookup is valid here. By that lookup, b3 vs b2 is 0 fixed / 35 broken: 33 at kept pins and 2 through context.
- Error went from 40/803 to 74/803 (+34).

More important, 32 of the 33 kept-pin breaks are pins whose sign is the clerk-sheet truth one position away (see ruling 11). They measure our box-to-position map, not the seed labels. Neither 33 nor 28 should go to the owner as 'what your kept tiles did'.
- **agree**: 2a. 'Owner 4 Oct pins (P_O inside b2): 25 scored, 20 right / 5 wrong ... top-1 already right at 24 of 25' are P_LO counts; P_O alone is 18 scored, 13 right / 5 wrong, top-1 right 17, decode right 18.
  - Evidence: Recounted from pins_P_O.tsv, pins_P_LO.tsv, decode_a.tsv and the truth file:
- P_O: 19 pins, 18 scored, 13 right / 5 wrong; top-1 right 17; arm a right 18.
- P_LO: 25 scored, 20 right; top-1 right 24.
The two sets do not overlap. Only 6 of the 19 P_O pins differ from arm a's sign: the 5 wrong ones plus L12.23, which is unscored.
- **agree**: 2b. 'the owner's 4 Oct moves at 80% (20/25)' should be 72% (13/18).
  - Evidence: 13/18 = 72% is the right arithmetic for P_O. But the figure itself is confounded:
- 3 of the 5 'wrong' moves (L11.20, L13.20, L21.13) equal the truth at the adjacent position, on lines whose kept pins are shifted the same way.
- 1 (L02.8) is a new one-tile split pile, T60-d, scored as plain T60.
- 1 (L01.8) is X20's script cluster rule, not a move made on no.87.
Neither 80% nor 72% measures the owner's accuracy.
- **agree**: 2c. 'the 40 are seeded pile labels the owner left in place' should be 35 kept + 5 moves.
  - Evidence: P_S has 197 scored pins and 40 wrong: 35 kept (of 172 scored kept) + 5 P_O + 0 P_L. 32 of the 35 kept 'wrong' equal the truth at position +/-1.
- **agree**: 3. 'Fixed none' holds only at the pinned positions (L02.9 fixed through context), and the owner paragraph's 'it never changed a neighbouring sign' holds only for P_L at lam 4.
  - Evidence: I rebuilt the write-over-afterwards arms myself (arm a or a1 with each pin set written over it) and compared them sign by sign with the pinned-inside arms:
- P_L, lam 4: 0 positions differ.
- P_LO: 1 (f178v L02.9, X_NEW to T49, truth u; tx_bench 1 fixed / 0 broken).
- P_S: 7 (tx_bench 1/2).
- P_L, lam 1: 1 (L05.27, a break).
Also b2 vs b: 1 fixed (L02.9, context) / 5 broken. The pin that caused the L02.9 fix (L02.8 = T60) is itself one of the 'wrong' pins.
- **agree**: 4. The near-tie sentence (24 positions, 5 of the errors) is not pre-registered, computed by no committed script, and misleading.
  - Evidence: Re-derived from base_topk.tsv:
- 24 lattice positions have a top-2 gap under 0.05.
- Arm a: 5 of its 32 lattice-line errors are near-ties (direct position lookup). 3 of those 5 are P_L positions.
- Arm b: 2 of 29 lattice-line errors are near-ties.
- 7 of the 24 near-ties are P_L pins.
run_pins.py contains no near-tie or 0.05 computation (grep). 'The remaining errors sit at 24 positions' is false.
- **agree**: 5. The registered gate was declared unreachable in the prereg, so the null carries no information about pins; both owner claims rest on secondary or exploratory numbers.
  - Evidence: The PREREG gate section says the gate 'cannot be met by (b)'. On the numbers: 0.0448 + 0.0144 = 0.0592, above both a (0.0486) and c (0.0423). b3 is declared exploratory in the PREREG.
- **agree**: 6. 'Verdict: null (dev-FAIL ...)' mislabels a gate set on the whole of an eval item.
  - Evidence: The PREREG names birago1572-no87 'split eval', and the gate is on the whole-no.87 as-measured figure. 'FAIL on the registered whole-item gate' is the right label; 'dev-FAIL' is not.
- **agree**: 7. Offline tests: 13/14 pass, not 14/14; test_probs_top3_replaces_hml fails, it is pre-existing, and it is unrelated to --pins.
  - Evidence: pytest on tools/tests/test_key_decode_lattice.py gives 1 failed, 13 passed.
- The tool and the test file are byte-identical to 4dc3f12f.
- parse_top3 at 387a9d9f also returns 0.7000000000000001, so the failure is deterministic and predates TXE3-9.
- test_pins_hold_position_and_report passes.
- **partly**: 8. Truth row f178v_L02 pos 8 (one of the 5 'broken' owner moves) is flagged corrected:key-doubtful and still scored.
  - Evidence: The fact is right: flag corrected:key-doubtful, truth T42|T70|T88 = g. tx_bench keeps 'corrected:' rows scored by design (is_flagged).

The doubt does not rescue the pin. It concerns whether T42 can read g instead of m, and the pinned T60 reads n, against a g the flags file calls clear on the clerk sheet.

The real problem is elsewhere: settled_no87.tsv shows this tile's seed was already T60. The owner moved it into a NEW one-tile pile, T60-d, which does not exist among his family-sort piles (T60, T60-b, T60-c only). The harness then scored that pile as plain T60. Reading 'separated from T60' as 'is T60' reverses his signal.
- **partly**: 9. Rule 3 third-attempt shape: TX-ALTS, TXE-E, TXE-J and TXE3-9 each changed one input to the same no.87 lattice and none passed, so the next attempt needs new material.
  - Evidence: The advice not to re-run pins on no.87 is sound, and RESULTS says the same.

TXE3-9 should not count as a third failed attempt, though:
- Its gate was declared unreachable in advance.
- Its owner and kept arms (P_O, P_S) went through a box-to-position map that is off by one in places.
- Only P_L was a clean test, and it took all 3 signs available to it.

Log it 'untested by this design', not as another failure of the lattice on no.87.
- **disagree**: 10. run_pins.py scores by direct position lookup rather than tx_bench alignment (arm a 32 vs 31; b3 68 vs 60); 'a small scorer inconsistency that changes no conclusion'.
  - Evidence: The gap is not small where it matters. It sits almost entirely in b3, and it is the visible symptom of a bad join:
- tx_bench finds 7 deletion+insertion pairs in b3 (L06, L09, L11, L13, L21, f179r L03), against 1 in b2.
- In those runs the pinned signs equal the truth one position over.
- Of the wrong pins, 32 of 35 kept and 3 of 5 P_O equal the truth at position +/-1. At +/-2 and +/-3 they match only 1-4 of 35, which is chance level. Right pins match +/-1 in 1 of 137.
- A check that uses no truth agrees: of 208 no.87 sorter tiles with a 1:1 box, the seed label equals the L sign at the mapped position for 157, at position -1 for 24, at +1 for 14, at +/-2 for 0.

The cause: run_pins.py, and X20's x20_owner.py before it, join sorter tile ids to positions through atlas/no87_box_token.tsv. That file is a label-blind DP over box widths only. Example: on L06 it maps tile f178v_06_009, which the owner marked NOT-LETTER, to token 9, and every later tile on that line lands one position late.

This changes conclusions. Kept-alone breaks read 28 by aligner and 35 by position, and both are mostly map shifts.
- **disagree**: (First verifier's control section) Random pass-A pins 'separate the kept-seed damage from pinning as such, and support the substance of claim 2'.
  - Evidence: The random pins are placed by passA_at, which uses pass A's own difflib alignment to the skeleton and never touches no87_box_token.tsv. The owner and kept pins do go through that map. So the control cannot vary on the one step that produces most of the owner-set 'wrong' pins (rule 3: a control orthogonal to the cause).

Allowing for the one-position shift, the kept seeds read 137 right at their mapped position plus up to 32 at the adjacent one, out of 172. Chance would give about 5 of those 32, so roughly 95-98% right, comparable to pass A's 94.7%.

The control's 'owner sets worse than random' difference is the map, not the seeds or the owner.

### Final verdict on each claim told to the owner (11 Oct ~07:05 UTC)

- **overstated**: Locking the owner's decisions into the decoder gives the same result as applying them afterwards.
  - Evidence: Same decoder, pinned inside vs written over afterwards. I rebuilt this from the committed arm outputs and scored it with tx_bench:
- P_L at lam 4: identical at every position.
- P_LO (labels + the 4 Oct decisions): 1 neighbour moved (f178v L02.9, a fix).
- P_S: 7 neighbours moved (1 fixed / 2 broken).
- P_L at lam 1: 1 neighbour moved (a break).

Only 13 pins differed from the decoder's own choice (7 label pins, 6 owner pins). No arm beat the current reading L: b vs c 4/5, b2 vs c 3/8.

The owner's pins were also placed through atlas/no87_box_token.tsv, which is off by one in places, so P_O is partly not his decisions at the positions he meant. That does not change the inside-vs-after mechanics.
  - Corrected: On Birago no.87, locking decided signs into the decoder gave almost the same reading as writing them over it afterwards. It was identical for the 7 label rulings; with your 4 Oct decisions added, one neighbouring sign changed (f178v L02.9, for the better). Neither way beat the current reading. One letter only, and only 13 pins differed from what the decoder already chose.
- **wrong**: A tile he merely left in place must never be counted as a decision (pinning kept tiles broke 33 signs); his 4 Oct moves pinned broke 5 and fixed none.
  - Evidence: The counts are real outputs of the harness, but they measure our box-to-position map, not the owner's sorting or the seed labels.

The counts:
- Kept tiles alone: 0 fixed / 28 broken by tx_bench, 0 / 35 by exact position. The 33 was b3 vs a, which includes the moves.
- The 4 Oct moves: 1 fixed / 5 broken (b2 vs b, p 0.22), not 'fixed none'.

What the breaks are:
- 32 of the 33 kept-pin breaks are signs equal to the clerk-sheet truth one position away. They run in same-direction stretches per line: L06, L09, L11, L13, L17, L21, f179r L02 and L03.
- A check that uses no truth shows the same shift: 38 of 208 sorter seed labels equal L's sign one position away, and 0 two positions away.
- Of the 5 'wrong' moves:
  - 3 (L11.20 T24, L13.20 T37, L21.13 T60) equal the truth at the adjacent position, on lines shifted the same way.
  - L02.8 is a new one-tile pile, T60-d, that the owner split out of T60 and the harness scored as T60.
  - L01.8 is X20's script cluster rule from his sort of other letters (T65 = the truth at pos+1).
- His 13 other scored moves are all right.

X20 (the 4 Oct decisions applied after: 0 fixed / 4 broken) used the same join (x20_owner.py lines 49-51, 84-87), so it inherits the same problem.
  - Corrected: Withdrawn as stated. On no.87 the tiles you left in place and 3 of your 5 'wrong' 4 Oct moves mostly carry the clerk sheet's sign for the neighbouring position: our width-only box-to-position map (atlas/no87_box_token.tsv) is off by one on several lines. A fourth is your new pile T60-d scored as plain T60, and the fifth is a cluster rule from your sort of other letters. These numbers say nothing about the quality of your sorting or of the seeds. No rule about kept tiles or moves should rest on them until the map is fixed and the arms re-scored.

### Sentence the parent may give the owner

On Birago no.87, locking your decided signs into the decoder gave practically the same reading as applying them afterwards: identical for the 7 label rulings, and one neighbouring sign changed, for the better, once your 4 Oct moves were added. Neither way improved on the current reading. Please disregard what we told you about your kept tiles and your 4 Oct moves 'breaking' signs: almost every one of those 'wrong' tiles carries the right sign for the position next to it, which shows our tile-to-position map is off by one on several lines. It says nothing about your sorting, and we will fix the map and re-score before drawing any rule from it.
