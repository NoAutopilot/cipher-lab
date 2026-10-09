# TXE2-VIV102-BASE: today's pipeline on the dev leaf vivonne1573-f102r-dev (PREREG-txeng2-14 DV1b), a dev baseline

LANE TX-ENGINEER-2 (account 4, incarnation 3), Opus 5.5 worker, Opus 5.5 readers, Sonnet adjudicators; 9 Oct 2026,
22:57-23:1x UTC by `date -u`. Binding: PREREG-txeng2-14 DV1b and its "DV1b re-priced" section (cap 22, box 120 min, packets
from the DISAGREE rows only, the S2-ADJ shape); brief row TXE2-VIV102-BASE in .claude/briefs/runs/2026-10-09-account4-txe2-round14.md.
**Dev, never a look.** Hosts: 0 requests.

**Openings of eval truth: 0.** Nothing of f.103r was opened (no c106 crop, nothing under outputs/vivonne1573-f103r-confirm2/
or txeng2/s2score/); the reader sheet and brief were derived from txeng2/s2read/ (sheet_SIGNS.md, reader_task.txt) and the
adjudication template from txeng2/s2adj/, as the brief names. No file under ciphers/fr16104-vivonne-spain-1572/tx/, no key
value, no decode was opened. The DEV truth (benchmark-tx/vivonne1573-f102r-dev.truth.tsv) was never opened by eye: it was
read only by scripts at the score step: the one tx_bench run (step 4) and `classify.py` (step 5, counts only). The
`committed.tsv` file was read only by that tx_bench run. Disclosure: tx_bench's own "top confusions" line prints truth
plaintext values beside read labels; it is in `tx_bench_out.txt` as the tool wrote it.

## Pricing correction (before any read)
The brief priced f.102r at 20 lines (3 calls per pass). The BENCHMARK-TX row is f102r_L01-L37 (74 crops, 37 lines), so the
cost was flagged to the lane before any read (ROOM 22:59). The lane re-priced: 5 calls per pass, packets from the DISAGREE
rows only, cap 22, box 120 min (PREREG-14 "DV1b re-priced"). Lane's get_session reading at 23:05: 10.95, after the reads,
during packet P04.

## Step 1: sheet, brief, crops (committed 1e9760e9f, before any read)
- `sheet_SIGNS_dv1.md` = ../s2read/sheet_SIGNS.md + the 6 committed labels S2-NOTE section 4 found missing, added as tokens
  (t, i, w to the lowercase list; Z, J, H as special tokens; H "with ONE crossbar, write # for the double-crossed sign"), with
  a changelog. Diff: two lines changed/added in the inventory plus the changelog; nothing else.
- `reader_task.txt` = ../s2read/reader_task.txt with the sheet path, c105_f102r crop names, f102r line ids, Z/J/H in the token
  list and the measured overlap sentence; "Do not resize, rescale, enhance or re-crop" kept.
- Overlap measured by `tools/overlap_audit.pixel_overlap` (`overlap_measure.py`, `overlap.tsv`): **250 native px on all 37
  lines, ncc 0.997-0.999, equal to the manifest boxes; sign width 46 px** (iiif_lines.ink_run_width median over 74 crops).
  Sentence written by `iiif_lines.overlap_sentence` (`overlap_note.md`), not typed. (f.103r was 150 px; the two leaves differ.)
- Overlay check (`overlay.py`, sheets in the scratchpad, sheets 0 and 3 viewed): no sign cut at the s1/s2 seam; not re-cut.
  Noted: L01 opens with plain words; L34 and L37 carry plain-script words mid-line.

| file | sha256 | commit |
|---|---|---|
| sheet_SIGNS_dv1.md | 08dd48d921ba896758ef152ab73f60c4d019ef36b33731714aeb1ccb10866c30 | 1e9760e9f |
| reader_task.txt | d7ebae3b28a5b4ca228f8d78ba2ea5066fbcea36588469bee818454511613dfc | 1e9760e9f |
| overlap_note.md | f2d0563ccacffc6e22fbfa1635aa296499174dce825efca387ea0fb3c7af1c2d | 1e9760e9f |
| overlap.tsv | e09ee15f209840752bed5d67871d1e9ee0340c14ccb94b1a2255e58c5724ed06 | 1e9760e9f |
| chunk tasks reads/task_{A,B}{1-5}.txt | SHA256SUMS_step1.txt | 1e9760e9f |

## Step 2: two blind Opus 5.5 passes (5 calls each, <= 8 lines per call)
Chunks L01-08, L09-16, L17-24, L25-32, L33-37; each call saw only its task file, the sheet and its crops. `assemble.py` (S2's,
paths changed) drops DUP and [...] rows, strips a trailing '?' (conf capped at M), renumbers. Both passes independently wrote
**L14 = DUP of L13** (a repeated band, as on f.103r L26/L27).

| call | tokens | call | tokens |
|---|---|---|---|
| A1 | 109,343 | B1 | 108,822 |
| A2 | 108,766 | B2 | 109,942 |
| A3 | 109,725 | B3 | 109,061 |
| A4 | 110,306 | B4 | 111,718 |
| A5 | 108,727 | B5 | 111,763 |
| **A** | **546,867** | **B** | **551,306** |

| output | signs | sha256 | commit |
|---|---|---|---|
| outputs/vivonne1573-f102r-dev/passA_dv1.tsv | 1,813 on 36 lines (L14 DUP) | 4e5f7a1024c310cade7d07987fa11bfade0e330a78e9f2bf7f94324729be6103 | 5e4301777 |
| outputs/vivonne1573-f102r-dev/passB_dv1.tsv | 1,811 on 36 lines (L14 DUP) | 0654504d5de3b8b04825899c571155b35eb410a4b8da5943b5b7b9aceccd8e69 | 22ed2f7f9 |

Raw chunk sha256s: SHA256SUMS_passA.txt, SHA256SUMS_passB.txt.

## Step 3: reconcile + packet adjudication (S2-ADJ shape)
`tools/reconcile_passes.py passA_dv1 passB_dv1 --keep-alts --out-dir rec`: **agreement 1595/1852 = 86.1%**; agreed-H 1,361,
agreed-uncertain 234, disagree 257. Queue `adjud_queue.tsv` (build_queue.py, S2's): 491 rows. Packets (`build_packets.py`):
the 257 disagree rows in queue order, 16 per packet -> **17 packets (16 x 16 + 1 x 1)**; the 234 agreed-uncertain rows keep
the agreed reading. Template `adjud_task_template.txt` = S2-ADJ's with the sheet, packet dir, f102r example and 250 px overlap
changed. Queue, packets, tasks and template committed with SHA256SUMS_packets.txt / SHA256SUMS_rec.txt in 22ed2f7f9 **before
any adjudication call**. One fresh claude-sonnet-5 call per packet, no resume:

| packet | lines | tokens | A | B | other | NONE | viewed |
|---|---|---|---|---|---|---|---|
| P01 | L01-L04 | 105,038 | 9 | 7 | 0 | 0 | 16/16 |
| P02 | L04-L07 | 105,086 | 7 | 7 | 0 | 2 | 16/16 |
| P03 | L07-L10 | 105,038 | 7 | 9 | 0 | 0 | 16/16 |
| P04 | L10-L13 | 105,001 | 4 | 10 | 0 | 2 | 16/16 |
| P05 | L15-L17 | 104,201 | 6 | 8 | 0 | 2 | 16/16 |
| P06 | L17-L18 | 102,857 | 8 | 7 | 1 | 0 | 16/16 |
| P07 | L18-L20 | 104,781 | 2 | 9 | 2 | 3 | 16/16 |
| P08 | L20-L22 | 103,837 | 8 | 6 | 1 | 1 | 16/16 |
| P09 | L22-L24 | 103,823 | 8 | 5 | 0 | 3 | 16/16 |
| P10 | L24-L26 | 105,344 | 7 | 5 | 0 | 4 | 16/16 |
| P11 | L26-L27 | 102,875 | 9 | 6 | 0 | 1 | 16/16 |
| P12 | L27-L29 | 104,508 | 11 | 2 | 0 | 3 | 16/16 |
| P13 | L29-L30 | 103,477 | 9 | 7 | 0 | 0 | 16/16 |
| P14 | L31-L33 | 104,290 | 12 | 4 | 0 | 0 | 16/16 |
| P15 | L33-L35 | 105,477 | 11 | 4 | 0 | 1 | 16/16 |
| P16 | L35-L37 | 105,132 | 9 | 3 | 1 | 3 | 16/16 |
| P17 | L37 | 100,480 | 0 | 1 | 0 | 0 | 1/1 |
| **total** | | **1,771,245** | **127** | **100** | **5** | **25** | **257/257** |

viewed = yes is each adjudicator's own report per row (`adjud_out.tsv`); every reply listed the crops of its lines as opened.
Conf: H 6, M 160, L 91. P04's reply said "15 rows", but its out file has the 16 queue rows in order (assemble_z.py asserts
it); a miscount in the reply only. The 5 "other" verdicts: L17 col 50 (none/z -> Z), L18 col 42, L19 col 23, L20 col 45
({swash}/{curl} -> V), L37 col 8 (pass A's raw token "{box" / none -> {boxed sign}).
`assemble_z.py`: passZ_dv1 = the reconciler's draft with the 257 verdicts applied (NONE drops), **1,827 signs**; 77 positions
differ from the draft's sign at a split.

| output | sha256 | commit |
|---|---|---|
| adjud_out.tsv | b849f7536e78e1504198defbfd00fd240902b921cea95067391105f5591f1737 | 9c7c53071 |
| **outputs/vivonne1573-f102r-dev/passZ_dv1.tsv** | **e5081ff031a69a7b1bcbd02995c58d81a7618030b33f9c45b39c9fed0762c4a0** | 9c7c53071 |
| packet outputs | SHA256SUMS_passZ.txt | 9c7c53071 |

## Step 4: ONE tx_bench run (`tx_bench_out.txt`)
`python3 tools/tx_bench.py passZ_dv1 passA_dv1 passB_dv1 --bench BENCHMARK-TX.tsv --item vivonne1573-f102r-dev --exclude-flagged
--paired committed.tsv`, run once (it scored each file separately, with a paired comparison against committed for each).

| output | as measured (1008 scored) | flagged excluded (403) | wrong / deleted / inserted | paired vs committed |
|---|---|---|---|---|
| **passZ_dv1** | 0.431 (434/1008), 0.400-0.461 | **0.199 (80/403), 0.163-0.240** | 371 / 21 / 42 | fixed 2, broken 64, p = 0.0000 |
| passA_dv1 | 0.445 (449/1008), 0.415-0.476 | 0.208 (84/403), 0.172-0.251 | 393 / 24 / 32 | fixed 2, broken 89 |
| passB_dv1 | 0.415 (418/1008), 0.385-0.445 | 0.161 (65/403), 0.129-0.200 | 360 / 24 / 34 | fixed 2, broken 56 |
| committed (TXP-VIV102's figure, beside) | 0.327 | 0.000 (home advantage) | | |
| TXP-VIV102 Sonnet passA / passB (beside) | 0.330 / 0.353 | 0.007 / 0.042 | | |

**The flagged-excluded figure binds.** The truth's control margin on this leaf is 0.003 (published key 0.552 vs shuffled max
0.549, TXP-VIV102), so no as-measured level is read as a figure; the as-measured column is reported only because the brief
asks for both. The adjudication did not beat the better blind pass: passZ 0.199 lies between A 0.208 and B 0.161.

## Step 5: read-free beside
Label counts (column sign; committed from txpool/vivonne1573-f102r-dev/RESULTS.md, 1,848 rows, not re-opened):

| file | ':' | 'S' | 's' | '3' | 'z' | signs |
|---|---|---|---|---|---|---|
| committed | 84 | 16 | 112 | 19 | 94 | 1,848 |
| passA_dv1 | 55 | 58 | 70 | 47 | 45 | 1,813 |
| passB_dv1 | 65 | 31 | 97 | 32 | 69 | 1,811 |
| passZ_dv1 | 56 | 36 | 93 | 38 | 54 | 1,827 |

Unlike S2 on f.103r (no '3', no 'V' at all), these readers used '3' (A 47, B 32) and 'V' (A 26, B 47). New sheet tokens used:
Z 12, i 6, t 6, H 1 across both passes; '{...}' descriptors 72.

Class split (`classify.py` = S2-NOTE's classify.py with the item set to f102r-dev and the example counter dropped; S2-NOTE's
norm_map.tsv unchanged; `classify_out.txt`). Totals equal tx_bench's.

| file | set | total | segmentation del / ins | read: = committed ref | read: other | notation |
|---|---|---|---|---|---|---|
| **passZ_dv1** | **flagged excluded** | **80** | **6 / 42** | 0 | **26** | **6** |
| passZ_dv1 | as measured | 434 | 21 / 42 | 276 | 87 | 8 |
| passA_dv1 | flagged excluded | 84 | 7 / 32 | 0 | 33 | 12 |
| passB_dv1 | flagged excluded | 65 | 5 / 34 | 0 | 22 | 4 |

**Segmentation is again the largest class of passZ's flagged-excluded errors: 48 of 80, mostly insertions (42).** Deletions
are far fewer than S2's on f.103r (S2: 21 deleted, 21 inserted of 75), but that is a different leaf, not a comparison of pipelines.
Not settled here (would need a truth view): whether the insertions sit in the plain-word stretches of L34/L37 or at the
250 px seam. Notation is small (6). The insertion count is the same as measured and flagged excluded (tx_bench charges
insertions to the line, not to a flagged position).

## For the lane
- Dev pool: passZ_dv1's flagged-excluded count is 80 (PREREG-14 says the dev pool grows by it, in a dated Amendment 9 line;
  left for the lane to write, not edited here).
- Suggestion (one line, not done): a read-free locator of passZ's insertions by line against the plain-word lines L01/L34/L37
  and the overlap zone (tools/overlap_audit.py already does the zone half with a truth).
- Cost: the lane's get_session reading (27 subagent calls: 10 Opus reads, 1,098,173 tokens; 17 Sonnet packets, 1,771,245 tokens).

| file | sha256 |
|---|---|
| tx_bench_out.txt | 8ecffa568b030fb0c9369436b01de15be9e196fc95c4a1d66dc9b33e53d1c71a |
| classify.py | e8a88521866381b563bdae9f54bd1791b571283d4a41930d621cfca3eb8eee83 |
| classify_out.txt | d5791c9222bd8cc3ffba13e6832d4eaee656769551196d1538ec7777a6a74af6 |
| assemble.py / assemble_z.py | 2ec0dec5... / 4fac3ba8... |
| build_queue.py / build_packets.py | 45c991bc... / f84cf8bf... |
| adjud_task_template.txt | 6ef38eedb5d0ad0edb07e6cf6184e977fe5ae84702e7394ba598156b33613281 |

Openings of eval truth: 0.

Verdict: measured: dev baseline of today's pipeline on vivonne1573-f102r-dev: passZ_dv1 0.199 (80/403) flagged excluded
(binding; as measured 0.431, not read as a figure), beside passA_dv1 0.208 and passB_dv1 0.161; split of passZ's 80
flagged-excluded errors: segmentation 48 (6 deleted, 42 inserted), read 26, notation 6.
