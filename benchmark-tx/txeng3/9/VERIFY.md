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
