# TXE2-SHEETVIVC: the text-list control arm under SHEET-VIV's protocol on the dev leaf f.102r (dev2), PREREG-txeng2-21 SHEET-VIV-C

LANE TX-ENGINEER-2 (account 4, incarnation 5), Opus 5.5 worker, Opus 5.5 readers, Sonnet adjudicators; 10 Oct 2026,
03:38-03:5x UTC by `date -u`. Binding: benchmark-tx/PREREG-txeng2-21.md section SHEET-VIV-C (PREREG push d326cc43f, worked
from it); brief row TXE2-SHEETVIVC in .claude/briefs/runs/2026-10-10-account4-txe2-round21.md. **Dev, never a look.**
Hosts: 0 requests.

**Openings of eval truth: 0.** **dev openings: 1** (the dev2 truth was read only by tools/tx_bench.py, once per pairing as
the PREREG names; never by eye). Nothing of f.103r was opened. passZ_sv.tsv and passZ_dv1.tsv were used by path and sha256
only (tx_bench's --paired bases); their content was never opened. No key value, decode, truth file, other pass or the
pictured sheet reached a reader or an adjudicator (access logs below). Disclosure, as SHEET-VIV: tx_bench's "top confusions"
lines print truth values beside read labels; they stay in the two `tx_bench_out_vs_*.txt` files as the tool wrote them,
and were not viewed by this worker.

## The one change and what stayed the same
- **Sheet:** `benchmark-tx/txeng2/viv102base/sheet_SIGNS_dv1.md` (the text list, sha256 08dd48d9...) in place of the
  pictured sheet. The reader task's sheet sentence and token rule are DV1b's own lines, verbatim; the pictured sheet's
  40-token line is gone. `diff ../sheetviv/reader_task.txt reader_task.txt` shows exactly those three lines and nothing else.
  The adjudicator template is SHEET-VIV's with its two sheet lines replaced by DV1b's adjudicator sheet line (and the
  sheetviv -> sheetvivc paths).
- **Unchanged, byte-identical to SHEET-VIV:** the [PLAIN:...] sentence, the 250 px overlap sentence, "Do not resize,
  rescale, enhance or re-crop", the same 74 c105_f102r s1/s2 crops, 5 calls per pass (L01-08, L09-16, L17-24, L25-32,
  L33-37), two blind Opus passes, `tools/reconcile_passes.py --keep-alts --out-dir rec`, DISAGREE rows only, packets of
  <= 16 rows to fresh Sonnet calls; build_queue.py, build_packets.py, assemble.py, assemble_z.py and access_log.py copied with
  only paths, output names (`_tl`) and the allowlisted sheet path changed.

## Step 1 (committed 0de1d2ecd, before any read)
| file | sha256 |
|---|---|
| reader_task.txt | 4806ca67caf448514d2956a9e07e1ecef2af98923ffc1a7055e0b92b1871f831 |
| adjud_task_template.txt | 3368e86bf03068d03866142c15e760d6173aeff485c5cc61f1cb21a5a48ec771 |
| viv102base/sheet_SIGNS_dv1.md (the sheet reference) | 08dd48d921ba896758ef152ab73f60c4d019ef36b33731714aeb1ccb10866c30 |
| passZ_sv.tsv (paired base 1, path + hash only) | dbceb0dd6ed80ff6d62e9a29371a8ecea5718790d4040d1b484a1122faf587c0 |
| passZ_dv1.tsv (paired base 2, path + hash only) | e5081ff031a69a7b1bcbd02995c58d81a7618030b33f9c45b39c9fed0762c4a0 |
| chunk tasks reads/task_{A,B}{1-5}.txt, scripts | SHA256SUMS_step1.txt |

## Step 2: two blind Opus 5.5 passes (10 calls)
| call | tokens | call | tokens |
|---|---|---|---|
| A1 | 109,289 | B1 | 110,172 |
| A2 | 109,509 | B2 | 109,428 |
| A3 | 108,850 | B3 | 109,114 |
| A4 | 108,724 | B4 | 109,363 |
| A5 | 105,934 | B5 | 107,967 |
| **A** | **542,306** | **B** | **546,044** |

Both passes independently wrote **L14 = DUP of L13** (as DV1b and SHEET-VIV). [PLAIN] rows: pass A 4 (L01, L34 x2, L37),
pass B 3 (L01, L34, L37). Raw chunks were committed as they landed (e3d4892ec, 678643ff8, 06c56a20b, e330a46b4; the stop hook asked
for untracked files to be pushed) -- all before reconcile and before any score.

**Reader access log** (`access_log_reads.tsv`; F63): 190 tool calls. Every Read was the call's own task file, the text-list
sheet (10 reads, one per call) or one of its own crops; each of the 74 crops viewed exactly twice (once per pass).
**The checker printed 1 OUTSIDE**, adjudicated here and kept as printed: reader B2 ran one `python3 -c` that opened its own
16 crops with PIL to print their pixel sizes (`c105_f102r_L%02d_s%d.jpg` for L09-L16; the template string is what failed
the regex). No other file, no resize; the crops were then viewed with Read. Every other Bash call was the reader's own TSV
write. Calls touching a file outside the task's named files: 0.

| output | signs | sha256 | commit |
|---|---|---|---|
| outputs/vivonne1573-f102r-dev2/passA_tl.tsv | 1,830 on 36 lines | 586463118b581e7980d72d1deeb3fd3934bd755ae4b65429f735f636d42dd3ed | a9f62b228 |
| outputs/vivonne1573-f102r-dev2/passB_tl.tsv | 1,833 on 36 lines | babd58fc1e1dcf3c3548bcc5a952c0d450e7d254e9ea0aa02be6303f4a59c4de | a9f62b228 |

## Step 3: reconcile + packet adjudication
`reconcile_passes.py --keep-alts`: **agreement 1692/1868 = 90.6%** (SHEET-VIV 89.8%, DV1b 86.1%); agreed-H 970,
agreed-uncertain 722, disagree 176. Queue 898 rows. **11 packets** of 16. Queue, packets, tasks committed in a9f62b228
(SHA256SUMS_rec.txt, SHA256SUMS_packets.txt) before any adjudication call. One fresh Sonnet call per packet:

| packet | lines | tokens | A | B | other | NONE | viewed (reply) | crops opened (log) |
|---|---|---|---|---|---|---|---|---|
| P01 | L01-L05 | 107,033 | 4 | 11 | 0 | 1 | 16/16 | 10/10 |
| P02 | L05-L10 | 106,251 | 4 | 9 | 0 | 3 | 16/16 | 12/12 |
| P03 | L10-L16 | 107,138 | 4 | 11 | 0 | 1 | 16/16 | 12/12 |
| P04 | L17-L19 | 104,885 | 8 | 6 | 0 | 2 | 16/16 | 6/6 |
| P05 | L19-L23 | 108,542 | 5 | 5 | 1 | 5 | 14/16 | 10/10 |
| P06 | L23-L26 | 105,952 | 6 | 10 | 0 | 0 | 16/16 | 8/8 |
| P07 | L26-L28 | 104,362 | 11 | 5 | 0 | 0 | 16/16 | 6/6 |
| P08 | L28-L31 | 106,088 | 7 | 0 | 0 | 9 | 16/16 | 8/8 |
| P09 | L31-L33 | 103,934 | 8 | 8 | 0 | 0 | 16/16 | 6/6 |
| P10 | L34-L35 | 103,639 | 1 | 12 | 0 | 3 | 16/16 | 4/4 |
| P11 | L35-L37 | 104,470 | 9 | 4 | 0 | 3 | 16/16 | 6/6 |
| **total** | | **1,162,294** | **67** | **81** | **1** | **27** | **174/176** | **88/88** |

Not viewed (P05's own report, conf L): f102r_L19 cols 55, 56 -- the adjudicator could not locate them; verdicts kept as
returned, per the template. Conf: H 15, M 107, L 54.
**Packet access log** (`access_log_packets.tsv`; F63): every adjudicator opened its task, its queue, the text-list sheet and
every crop its task named. **The checker printed 2 OUTSIDE**, adjudicated and kept as printed: P01 and P02 wrote their
`P0x_out.tsv` with `printf > ... && cat >> P0x_out.tsv <<heredoc` -- the checker's `cat` verb rule fires on the write; no
read of any other file. Calls touching a file outside the task's named files: 0.
`assemble_z.py`: passZ_tl = the reconciler's draft with the 176 verdicts applied (NONE drops), **1,841 signs**; 59 positions
differ from the draft.

| output | sha256 | commit |
|---|---|---|
| adjud_out.tsv | d2a039853458f6aac48aaeb97e8ee440ccb3a796f47c6effb256e553fd3de616 | 6012cc631 |
| **outputs/vivonne1573-f102r-dev2/passZ_tl.tsv** | **8c8948ae864d881c176c0c6380a7b10dae363cc30b01a3e3744fc18511425ec7** | **6012cc631** |
| packet outputs, access log | SHA256SUMS_passZ.txt | 6012cc631 |

## Step 4: the score, one invocation per pairing (never merged)
`python3 tools/tx_bench.py passZ_tl.tsv passA_tl.tsv passB_tl.tsv --bench BENCHMARK-TX.tsv --item vivonne1573-f102r-dev2
--exclude-flagged --strict --paired <base>`, run once with base `outputs/vivonne1573-f102r-dev2/passZ_sv.tsv` (03:50:22 UTC,
`tx_bench_out_vs_sv.txt`, sha256 b24f125b27b30fddfd11788e81ec3d61eec20598d98b164079b04f3c0f8dcfed) and once with base
`outputs/vivonne1573-f102r-dev/passZ_dv1.tsv` (03:50:25, `tx_bench_out_vs_dv1.txt`, sha256
53f7a88e1200126a0866ba670f6ee99b3b4fce915e3511b5aa6a8abc44e4ebbe). The as-measured figures are from the same runs. Per item:
dev2 only. No second score.

**Value-level, flagged excluded (679 unflagged):**

| output | err_true (0.75 align) | SER (unit cost) | position errors / 679 + insertions / signs read | strict / visual-ID SER | as measured err_true / SER (1234) |
|---|---|---|---|---|---|
| **passZ_tl** | **0.128 (87/679)** | **0.127 (86/679)**: S 32 D 6 I 48 | 38/679 = 0.056 + 49/1,841 = 0.027 | 0.125 (85/679) | 0.272 / 0.271 |
| passA_tl | 0.107 (73/679) | 0.106 (72/679) | 37/679 + 36/1,830 | 0.105 | 0.262 / 0.261 |
| passB_tl | 0.134 (91/679) | 0.130 (88/679) | 43/679 + 48/1,833 | 0.127 | 0.276 / 0.274 |
| passZ_sv (SHEET-VIV, pictured) | 0.088 (60/679) | 58 edits | 29/679 + 31/1,835 | 0.083 | 0.246 / 0.245 |
| passZ_dv1 (DV1b, text list, "skip") | 0.124 (84/679) | 80 edits | 43/679 + 41/1,827 | | 0.276 |

**Pairing 1, passZ_tl vs passZ_sv (the sheet-form effect, [PLAIN:] held fixed), flagged excluded:** 36 lines;
**lines improved 7, worsened 13, tied 16; sign test p = 0.2632**; unit-cost edits **58 -> 86**. Position McNemar beside:
base wrong 29, output wrong 38; fixed 7, broken 16; exact p = 0.0931. As measured beside: lines 9/16/11, p 0.2295; edits
302 -> 334; McNemar fixed 19, broken 32, p 0.0919. Single passes beside: passA_tl 10/15/11, p 0.4244, edits 58 -> 72;
passB_tl 9/12/15, p 0.6636, edits 58 -> 88 (McNemar 7/21, p 0.0125).

**Pairing 2, passZ_tl vs passZ_dv1 (two text-list runs; [PLAIN:] sentence + run noise), flagged excluded:** 36 lines;
**lines improved 12, worsened 11, tied 13; sign test p = 1.0000**; unit-cost edits **80 -> 86**. Position McNemar beside:
base wrong 43, output wrong 38; fixed 18, broken 13; exact p = 0.4731. As measured beside: lines 12/10/14, p 0.8318; edits
337 -> 334; McNemar 32/19, p 0.0919. Single passes beside: passA_tl 13/10/13, p 0.6776, edits 80 -> 72; passB_tl
12/10/14, p 0.8318, edits 80 -> 88.

## Declared reading, applied word for word
- STANDS condition 1: passZ_tl's unit-cost edits on the 679 >= 1.25x passZ_sv's (58 -> >= 73): **86 >= 73, met**.
- STANDS condition 2: lines worsened > improved for passZ_tl vs passZ_sv: **13 > 7, met**; sign-test **p = 0.2632, not
  < 0.05**, so the declared wording is "stands on edits only", not "stands at the line level".
- NOT DISTINGUISHABLE condition: |edits(passZ_tl) - edits(passZ_dv1)| >= |edits(passZ_sv) - edits(passZ_tl)|:
  **|86 - 80| = 6 vs |58 - 86| = 28; 6 < 28, not met.**

**Verdict: the sheet-form effect STANDS (on edits only; line level p = 0.2632, not < 0.05). It is not "NOT DISTINGUISHABLE
from run spread": the two text-list runs differ by 6 edits, the two sheet forms under one protocol by 28.**

What this licenses, as the PREREG says: a sheet-form recommendation for THIS hand (the folder's reader brief) and the
second-hand PREREG (two runs per arm on a leaf of another hand with a drawn key). Never S1, never any f.103r step.
What it does not: a line-level claim (p 0.2632 at 36 lines; the line test's power was not simulated).

## For the lane (observations, not done)
- The [PLAIN:] confound SHEET-VIV named reads small here: with the text list, adding [PLAIN:] moved edits 80 -> 86 and
  insertions 41 -> 49 (lines 12/11). SHEET-VIV's insertion fall (41 -> 31) therefore goes with the pictured sheet, not
  with the [PLAIN:] sentence, on this one replicate.
- As in DV1b and SHEET-VIV, a single pass beats the two-pass pipeline output (passA_tl 0.106 vs passZ_tl 0.127).
- The text-list arm's agreement (90.6%) is higher than the pictured arm's (89.8%) while its accuracy is lower: agreement
  is not accuracy (TRANSCRIPTION.md).
- access_log.py's Bash rule false-flags `cat >> file <<heredoc` writes and printf-template paths; a one-line fix (exempt
  `cat >>` to an allowlisted output; resolve `%` templates) would stop the hand adjudication above. Not done (scope).
- Cost: the lane's get_session reading (21 subagent calls: 10 Opus reads, 1,088,350 tokens; 11 Sonnet packets, 1,162,294
  tokens).

| file | sha256 |
|---|---|
| tx_bench_out_vs_sv.txt | b24f125b27b30fddfd11788e81ec3d61eec20598d98b164079b04f3c0f8dcfed |
| tx_bench_out_vs_dv1.txt | 53f7a88e1200126a0866ba670f6ee99b3b4fce915e3511b5aa6a8abc44e4ebbe |
| access_log_reads.tsv, access_log_packets.tsv | SHA256SUMS_packets.txt, SHA256SUMS_passZ.txt |

Openings of eval truth: 0. dev openings: 1.
