# TXE2-BASE-GUN2: gunther8246-p2 baseline re-read on the sheet with its two shape slips fixed (PREREG-txeng2-11 B3b)

LANE TX-ENGINEER-2 (account 4), Opus 5.5 worker; brief .claude/briefs/runs/2026-10-09-account4-txe2-round11.md row
TXE2-BASE-GUN2; Amendment 9 option (b), TX-RED F35. 9 Oct 2026, 22:24-22:3x UTC by date -u.

**A baseline change, never a gain.** Openings of eval truth: 1 (the one tx_bench run below). No *.truth.tsv or
BENCHMARK-TX.tsv was opened or edited. passZ_pipeline.tsv was opened only by tx_bench at the score step.

## Method (order kept; each step committed before the next)
1. Sheet: `benchmark-tx/txpool/gunther8246-p2/sheet/calibration.tsv`, two shape slips relabelled (p1cal_L08 pos 15 `xb` -> `x`;
   p1cal_L09 pos 14 `ps` -> `p`). The four key-vs-print tiles (d6 L03.16 and L06.14, Ib L05.14, 34 L06.17) were kept as drawn and
   listed in `sheet/SHEET-CHANGELOG.md` as "shape correct, value disputed". One line in ciphers/gunther-van-schwarzburg-1561/NOTES.md
   hands the d6 = c? / Ib = s? / 34 = e? question to that folder's lane (no key edit).
2. Reader brief `blind_pass_brief_p2_gv2.md` = the TX-POOL-LEAF brief with two changes, diff in `brief_diff.txt`: (i) the label `p`
   added to the label list (the sheet's new label; without it the corrected tile names a label the list lacks); (ii) "do not resize"
   (PREREG-11 B3b, TX-RED F14) in place of the original "enlarge 2-3x". Change (ii) is a protocol difference from the original
   baseline's readers, who enlarged: part of the baseline change, not separable from the sheet change in this one score.
3. Two blind Opus 5.5 passes (A, B), 4 calls each (L01-L07, L08-L13, L14-L19, L20-L25), on the committed p.2 crops, no resizing.
   Readers saw only the brief, the sheet and their crops: never truth, decodes, the key, the old passes or passZ_pipeline.tsv.
4. `tools/reconcile_passes.py passA.tsv passB.tsv --out-dir rec` (nw): A 373, B 372 signs, agree 365/373 = 97.9%; 8 disagree +
   50 agreed-uncertain = 58 queue rows (the original protocol's queue shape, make_queue.py logic). Sonnet adjudication in packet
   shape: 4 packets (16/16/16/10 rows), one fresh claude-sonnet-5 call each, task from `adjud_task_template.txt`. viewed = yes on
   58/58 rows (the adjudicator's own report per row); 6 rows changed from the first candidate. `make_passZ.py` -> passZ_gv2 373 signs.
5. One score (pasted below).

## Commits and sha256
| step | commit | file | sha256 |
|---|---|---|---|
| 1 sheet + changelog + NOTES line | 00577705c | sheet/calibration.tsv | ef698c69006d8bf7dce029d03f320c7791151b3f77eebb6086960ae74bad635b (before: 01abf56bebd3c7809b16ed3a0b8e021392b283eee188623cb5bf552590cd54b9) |
| 2 brief (do not resize) + diff | d9cd3fbf2 | blind_pass_brief_p2_gv2.md | 92a17b426a20a073e942eb4f5ed09def75b48f44620122b470250d5e5414f5c7 |
| 3 pass A (parts e02061916) | 90adbec3c | passA.tsv | 357d44e9a964d5eef7f16f9c06498284a424c964fcd7f54f2aa7b6fd97c5571a |
| 3 pass B (part 54c28f74f) | 9e664697a | passB.tsv | c939595fea5ffe7c0756a6a545762112da111fc3a7063a0e0a3227d8ec114ca2 |
| 4 reconcile + queue + packets | a6160f9ec | SHA256SUMS_packets.txt | (per file in that list) |
| 4 adjudication P04 + make_passZ.py | 73f1ea94a | packets/P04_out.tsv | 9f6c9cdb685a04653f279efdf655daa2568dc2b65dacd9ba123aa8a486f0ceb4 |
| 4 adjudication P01-P03 + passZ | a01f061f7 | adjud_out.tsv | 0b37d85af66859021b34ad2c6a28055c6caf7bb40f3419f88f035934b1f2c16f |
| 4 output | a01f061f7 | benchmark-tx/outputs/gunther8246-p2/passZ_gv2.tsv | a9a11b91d14b4a438e592b39dcfb0404ecc941e9a7f22720b0448dd67199df43 |
Part and packet sha256s: parts/SHA256SUMS_parts.txt, SHA256SUMS_passes.txt, SHA256SUMS_packets.txt, SHA256SUMS_adjud.txt.
(The pass B commit message says "371 signs"; the file has 372.)

## Score (the one run)
```
$ python3 tools/tx_bench.py benchmark-tx/outputs/gunther8246-p2/passZ_gv2.tsv --bench BENCHMARK-TX.tsv --item gunther8246-p2 --exclude-flagged --paired benchmark-tx/outputs/gunther8246-p2/passZ_pipeline.tsv
gunther8246-p2 [eval] err_true 0.051 (16/317) 95% 0.031-0.080 | wrong 15 deleted 0 inserted 1 | excluded 55 | lines missing 0
  as measured 0.051 (16/317) | flagged excluded 0.020 (6/305) 95% 0.009-0.042 [12 flagged]
  top confusions (truth value <- read): s<-Ib x3, f<-x x2, c<-d6 x2, h<-aa x1, e<-v x1, e<-NEW:f-with-bars x1, e<-ps x1, d<-NEW:d-crossed x1
split eval: err_true 0.051 (16/317) 95% 0.031-0.080
paired passZ_gv2.tsv vs passZ_pipeline.tsv on gunther8246-p2: 317 common scored signs; base wrong 15, output wrong 15; fixed 6, broken 6; sign test p = 1.0000
```
| output | as measured | flagged excluded |
|---|---|---|
| passZ_gv2 (new baseline) | **0.051 (16/317)** 95% 0.031-0.080 | **0.020 (6/305)** 95% 0.009-0.042 |
| passZ_pipeline (old baseline), paired on the 317 common scored signs | 15 wrong of 317 | not re-scored here (one tx_bench run only) |

Old -> new, paired: 15 wrong -> 15 wrong; fixed 6, broken 6; sign test p = 1.0. Recorded as a baseline change, never a gain.
The top confusions are the flagged key-gap labels (Ib = s, x = f, d6 = c) and two NEW: signs (f-with-bars, d-crossed) that the
blind readers marked rather than forcing a label; none involves the two relabelled sheet tiles (x, p).

## Calls (tokens per call, from the subagent usage notes; the dollar cost is the lane's get_session reading)
Pass A (Opus): 107,998 / 108,217 / 106,361 / 108,059. Pass B (Opus): 107,087 / 108,223 / 108,165 / 108,057.
Adjudication (Sonnet): P01 105,811, P02 105,790, P03 106,429, P04 104,285. Total 12 subagent calls, 1,292,482 tokens. Host requests: 0.

## Deviations (declared)
- Adjudication priced at 2 calls; the original queue shape (disagree + agreed-uncertain) gave 58 rows, so 4 calls at <= 16 rows.
- Brief change (ii), "do not resize", taken from PREREG-11's wording; it departs from the original baseline's reader brief (see method 2).
- During orientation, before any read, this worker saw the first data row of the original passA.tsv and adjud_out.tsv (a `head -3`
  of the TX-POOL-LEAF folder). No reader or adjudicator saw them; the worker transcribed nothing.
- Two adjudicators (P03, P04) did not open the calibration crop images (they used calibration.tsv text only); P02 opened two.

Verdict: baseline change, never a gain: the sheet with its two shape slips fixed (plus "do not resize" and label p) reads gunther8246-p2 at 0.051 (16/317) as measured and 0.020 (6/305) flagged excluded, paired against the old baseline 15 -> 15 wrong (fixed 6, broken 6, p = 1.0); openings 1.
