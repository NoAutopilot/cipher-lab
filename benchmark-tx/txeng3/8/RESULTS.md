# TXE3-8 SHEET: the sheet-form effect on a second hand (PREREG-txeng2-21 SHEET-H2, run as registered under PREREG-txeng3-8)

Account 3, Fable worker (session_01JABsEdZ9LuiUNtZAzPS9gv), Opus 5.5 readers, Sonnet adjudicators; 11 Oct 2026, 05:47-06:1x UTC by
`date -u`. Binding: benchmark-tx/PREREG-txeng3-8.md (pushed 253ae443b at 05:59 UTC, before any read), which runs PREREG-txeng2-21's
SHEET-H2 protocol, endpoints and gate unchanged. **Dev only (no.87 dev_tune, f178v L01-L12, 343 scored / 338 unflagged); eval lines L13-L23
and f179r never copied, named or scored. Openings of eval truth: 0. dev openings: 2 (one tx_bench call per run, by script, never by eye).**
Hosts: 0 requests. Nothing published, owner not contacted.

## What was run
Order drawn by `random.Random(20261010)`: **P2, T2, P1, T1**. Runs P2 and T2 ran; **P1 and T1 did not start**, by the pre-registered stop
rule (after two runs the calibrated estimate for a third run plus this session's allowance was 15.8 against the 12 line; see Cost). So this
is **SHEET-H2 half run: one run per arm, within-arm run spread unmeasured** -- the declared 2-run reading applies, no gate.

| arm | sheet form | passes | agreement A/B | disagree rows -> packets | passZ signs |
|---|---|---|---|---|---|
| P2 | pictured `sign_sheet_blind_1572.png` + `blind_pass_brief_1572.md` as is | 2 x Opus 5.5 (2 calls each, L01-06 / L07-12) | **347/351 = 98.9%** | 4 -> 1 packet (A 2, B 1, NONE 1) | 350 |
| T2 | the same 51 cells as a value-blind text list `sheet_text_1572.md` + brief_T.md (4 lines differ) | 2 x Opus 5.5, same layout | **301/354 = 85.0%** | 53 -> 4 packets (A 15, B 36, other 1, NONE 1; viewed 53/53) | 353 |

Every read, reconcile, queue, packet and passZ was committed with its sha256 before the next step (c286bd1c1, 8a15b2121, 10575a2e2,
35ae9e532; SHA256SUMS_*.txt). Each run was scored ONCE (`run.py score`, scores/P2.txt, scores/T2.txt): `tools/tx_bench.py passZ_<run>.tsv
<run>_passA.tsv <run>_passB.tsv --bench BENCHMARK-TX.tsv --item birago1572-no87 --coverage-diagnostic --exclude-flagged --strict --paired
benchmark-tx/txeng/units/labels_dev_tune.tsv`.

## Numbers (value-level; Wilson 95%; strict/visual-ID beside; `--coverage-diagnostic`: 12 of 29 truth lines, missing lines listed not charged)

| output | err_true as measured (343) | err_true flagged excluded (338) | strict (as measured / flagged excl.) | unit-cost edits vs L base (as measured 12 / flagged excl. 7) | lines improved / worsened / tied (flagged excl.) |
|---|---|---|---|---|---|
| **passZ_P2** (pictured) | 0.044 (15/343) 0.027-0.071 | **0.030 (10/338)** 0.016-0.054 | 0.070 / 0.065 | 15 / **10** | 2 / 5 / 5, p 0.45 |
| P2 pass A | 0.047 (16/343) 0.029-0.074 | 0.033 (11/338) 0.018-0.057 | 0.073 / 0.068 | 16 / 11 | 2 / 5 / 5 |
| P2 pass B | 0.052 (18/343) 0.033-0.081 | 0.038 (13/338) 0.023-0.065 | 0.076 / 0.071 | 18 / 13 | 1 / 7 / 4 |
| **passZ_T2** (text list) | 0.195 (67/343) 0.157-0.241 | **0.183 (62/338)** 0.146-0.228 | (in scores/T2.txt) | 67 / **62** | 0 / 12 / 0, p 0.0005 |
| T2 pass A | 0.198 (68/343) 0.160-0.244 | 0.186 (63/338) 0.148-0.231 | | 68 / 63 | 0 / 12 / 0 |
| T2 pass B | 0.190 (65/343) 0.152-0.234 | 0.178 (60/338) 0.140-0.222 | | 65 / 60 | 0 / 12 / 0 |
| L baseline (labels_dev_tune) | 0.035 (12/343) 0.020-0.060 | 0.021 (7/338) 0.010-0.042 | | 12 / 7 | -- |
| X21 Opus pipeline (prior P-form run, other reconcile step; beside, not pooled) | 0.044 (15/343) 0.027-0.071 | 0.030 (10/338) 0.016-0.054 | | 15 / 10 | 2 / 4 / 6 |

Position McNemar vs the L base, flagged excluded: passZ_P2 fixed 4 / broken 7 (p 0.55); passZ_T2 fixed 3 / broken 55 (p < 1e-4). The T2
errors are substitutions (S 61 D 0 I 1 flagged-excluded), i.e. the readers found the signs and matched them to the wrong cells.

## Declared reading, applied word for word (PREREG-txeng3-8 "Declared readings by run count", 2 runs)
- PRIMARY endpoint per run, unflagged dev_tune edits: **P2 = 10, T2 = 62.** Between-arm gap **52** (T2 / P2 = 6.2x; the registered 1.25x
  threshold would be 12.5).
- Within-arm run spread: **unmeasured** (one run per arm). What stands beside it: the within-run reader spread (P2 passes 11 vs 13; T2 passes
  63 vs 60: 2-3 edits), the Vivonne same-form spread (6), and a prior pictured-sheet run on this same unit under a different reconcile step
  (X21: 10, identical to P2). Both single passes of each arm sit where their arm's passZ sits; no P output is within 47 edits of any T output.
- **Verdict (no gate, as declared): SHEET-H2 half run. The sheet-form effect replicates in direction on the second hand and is far larger
  than on Vivonne: text list 62 vs pictured 10 edits (err_true 0.183 vs 0.030 flagged excluded; 0.195 vs 0.044 as measured), against
  within-run reader spreads of 2-3.** The registered gate (mean(T) >= 1.25 x mean(P) and gap > max within-arm spread) is not evaluated: it
  needs P1 and T1 (next step below). Direction and size make the registered gate's outcome hard to miss, but that is a prediction, not a
  result.

## Control (rule 3) and what can vary
Arm T is the control for arm P's sheet form: same crops, same 51 cells, same reader model, same call layout, same reconcile and packet
protocol, the same adjudicators' sheet form as their arm; the one manipulation is the FORM of the inventory, which acts on exactly the
statistic measured (edits against truth). It varied: 10 vs 62. The agreement figure moved the same way (98.9% vs 85.0%), and -- as on Vivonne
-- agreement is not accuracy: P2's two readers agreed on 347 of 351 signs and were still wrong at 10 unflagged positions each; T2's agreed on
301 and were wrong at 60-63. The X21 prior run gives the P form a second, independent-protocol replicate at exactly the same figure (10/15).

## What the readers said (their closing paragraphs; not evidence, context)
- P arm: hardest pairs T60/T86, T18/T98, T90/T84, T95/T51, T50/T92, T76/T89; both P readers wrote the same counts per line and the same three
  weak reads (L05.1, L05.7, L06.9) -- near-deterministic twins under one prompt, which is why the within-run spread is small and why a second
  RUN per arm is the only honest spread measure (SHEET-H2's design).
- T arm: the readers could not place recurring shapes from the descriptions -- "two verticals on a baseline" (one took T33, one T86, one X_NEW),
  "a reversed 3 joined to a c" (T29 / T83 / T97 across readers), "circle with a crossed stem rising above it" (T65 inverted?) -- and said so.
  The text list was written honestly from the sheet image, but a 3-8 word description cannot carry the distinctions a tile carries; the 51
  cells differ by dots, bars and lean, and the hand's actual strokes differ from the key-sheet exemplars in ways a picture absorbs and a
  phrase does not. This is the Vivonne mechanism, stronger here because the inventory is larger (51 vs 40) and more look-alike.
- All eight readers reported the segment overlap as 4-7 signs, not the brief's "about 100 px at 2x" (benchmark-tx/txeng2/overlap/RESULTS.md
  already measured f178v at 425 native px); kept as is in both arms (arm P is "the brief as is"), a known brief error, not an arm difference.

## Access log (F63 shape; access_log_all.tsv, 14 subagents incl. the P2 packet)
Every Read was the call's own task, its sheet form or one of its own crops; every crop of each packet's lines was opened. The checker printed
4 OUTSIDE rows, all in T2_P03 and T2_P04: `cd <own dir>; cat queue.tsv; cat sheet_text_1572.md` (reading the task's own named files with cat
instead of Read) and own out.tsv clean-ups (`sed -i`, `grep -v '^$' out.tsv > o2 && mv`); adjudicated by this worker from the command text
and kept as printed. **Calls touching a file outside the task's named files: 0.** No reader or adjudicator saw a truth, key value, decode,
labels_dev_tune, another pass or the other arm's sheet. `tx_bench`'s truth-value confusion lines stay in scores/*.txt, filtered from the
worker's screen by run.py.

## Cost (usage.py over the subagent transcripts; input_all = all input tokens summed over API turns)
| call | API turns | input_all |
|---|---|---|
| P2 reads A1 / A2 / B1 / B2 (Opus 5.5) | 9 / 9 / 9 / 10 | 1.03M / 1.03M / 1.03M / 1.14M |
| T2 reads A1 / A2 / B1 / B2 (Opus 5.5) | 10 / 10 / 9 / 10 | 1.16M / 1.15M / 1.04M / 1.15M |
| P2 packet P01 (Sonnet) | 5 | 0.55M |
| T2 packets P01 / P02 / P03 / P04 (Sonnet) | 5 / 5 / 7 / 4 | 0.56M / 0.55M / 0.79M / 0.43M |

8 Opus reads + 5 Sonnet packets. At the pre-registered calibration (0.75 per Opus read, 0.30 per packet) that is 7.5 for the subagents; the
third run would have added about 3.3, and with the USD 5 allowance for this Fable session the estimate for three runs was 15.8 > the 12 line,
so P1 and T1 were not started (the rule, not a judgement). The session's actual figure is the parent's get_session reading (this worker's
get_session shows no cost field). Elapsed: 05:47 to about 06:1x UTC, about 25 minutes for two runs.

## For the owner, in three plain sentences
On the Birago clerk hand, the machine readers given a PICTURE of the 51 signs made 10 errors on 338 signs, and the same readers given the same
51 signs described in WORDS made 62 -- six times as many -- on the very same line images. This is the same effect that was seen on the
Vivonne hand, only much larger, so a letter whose key survives as drawings should always be read against a sheet cut from those drawings,
never against a typed list of sign names. The two runs per arm that the registration asked for are not finished (one per arm so far), so
the formal gate is still open, but no output of one arm came within 47 errors of any output of the other.

## Next step and its cost
Runs P1 and T1 under the same PREREG (scratch dirs for P1 are already prepped by `run.py prep P1`; `prep T1` then the same four steps per
run): about USD 3.3-4 per run at this job's rate (4 Opus reads + 1-4 packets), about 12 minutes each, run by a worker with a cap of
at least USD 10 so both fit under its 80% line. That completes SHEET-H2 as registered and lets the gate be read; if it passes, the
reader-brief rule "a hand with a drawn key gets a pictured sheet cut from the drawings before any read" enters TRANSCRIPTION.md's pipeline
text and the live-letter briefs, as SHEET-H2 says (never the Today column, never an eval look). Also for the lane: the brief's overlap
sentence ("about 100 px at 2x") should be corrected to the measured 425 native px for f178v in the next baseline change (both arms here
carried the old sentence).

| file | sha256 (16) |
|---|---|
| outputs/passZ_P2.tsv | 8b488c4749ac5d40 |
| outputs/passZ_T2.tsv | 50c678f20bf346ee |
| scores/P2.txt, scores/T2.txt | in SHA256SUMS_scores.txt |
| sheet_text_1572.md (arm T list) | b96608a72312b10a |

Openings of eval truth: 0. dev openings: 2.
