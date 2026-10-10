# TXE2-SHEETVIV: the pictured key sheet in place of the text-list sheet on the dev leaf f.102r (dev2), PREREG-txeng2-21 SHEET-VIV

LANE TX-ENGINEER-2 (account 4, incarnation 5), Opus 5.5 worker, Opus 5.5 readers, Sonnet adjudicators; 10 Oct 2026,
02:56-03:1x UTC by `date -u`. Binding: benchmark-tx/PREREG-txeng2-21.md section SHEET-VIV (PREREG push 8212de547, worked from
c29543f04); brief row TXE2-SHEETVIV in .claude/briefs/runs/2026-10-10-account4-txe2-round21.md. **Dev, never a look.**
Hosts: 0 requests.

**Openings of eval truth: 0.** **dev openings: 1** (the one tx_bench run of step 4; `classify.py` was not run, so the dev2 truth
was read once, by that script only, never by eye). Nothing of f.103r was opened: no c106 crop, nothing under
outputs/vivonne1573-f103r-confirm2*/, txeng2/s2score/, s2read/ or witflags/. The reader and adjudicator tasks were derived from
txeng2/viv102base/ (reader_task.txt, adjud_task_template.txt). passZ_dv1.tsv was used by path and sha256 only (as tx_bench's
--paired base); its content was never opened. No key value, decode, file under ciphers/fr16104-vivonne-spain-1572/tx/ or
sheet_SIGNS_dv1 reached a reader or an adjudicator (access logs below). Disclosure, as DV1b: tx_bench's own "top confusions" lines
print truth values beside read labels; they stay in `tx_bench_out.txt` as the tool wrote them.

## The one change (the treatment) and what stayed the same
- **Sheet:** `ciphers/fr16104-vivonne-spain-1572/glyphs/sheet_tomokiyo_v1.png` (SH-VIV; 40 tiles, value-blind, cut from
  Tomokiyo's published drawings) in place of `viv102base/sheet_SIGNS_dv1.md`, with its token list from sheet_tomokiyo_v1.tsv
  in the task text. The token rule now reads "the token of the sheet tile whose drawn shape it matches (or {1-3 words} for a
  shape on no tile)". The text descriptions of the old list are gone, and so are the old list's i, w and J (they are not tiles).
- **[PLAIN:...] sentence (Amendment 9 (24)):** plain-script stretches are written as ONE `[PLAIN:words]` row, never as signs
  (DV1b's task said "skip them"). assemble.py drops these rows, as before.
- **Unchanged:** the measured 250 px overlap sentence; "Do not resize, rescale, enhance or re-crop"; the same 74 c105_f102r
  s1/s2 crops DV1b read (no re-cut); 5 calls per pass (L01-08, L09-16, L17-24, L25-32, L33-37); two blind Opus passes;
  `tools/reconcile_passes.py --keep-alts`; DISAGREE rows only, packets of <= 16 rows to fresh Sonnet calls; assemble.py,
  build_queue.py, build_packets.py and assemble_z.py copied with only their paths and output names changed.
- **Overlay check** (`overlay.py`, sheets 0 and 3 viewed, scratchpad only): no sign is cut at the s1/s2 seam, so nothing was re-cut.

## Step 1 (committed a1635d222, before any read)
| file | sha256 |
|---|---|
| reader_task.txt | 3f4a2098efe527f753ef232e0381c9f389f6c145f01277fab2b0296376976469 |
| sheet_tomokiyo_v1.png (the sheet reference) | 999812049a2885645fc3... (full in SHA256SUMS_step1.txt) |
| sheet_tomokiyo_v1.tsv | 85f5a1a03893a194cc34... |
| passZ_dv1.tsv (paired base, path + hash only) | e5081ff031a69a7b1bcbd02995c58d81a7618030b33f9c45b39c9fed0762c4a0 |
| chunk tasks reads/task_{A,B}{1-5}.txt, overlay.py | SHA256SUMS_step1.txt |

## Step 2: two blind Opus 5.5 passes (10 calls)
| call | tokens | call | tokens |
|---|---|---|---|
| A1 | 112,995 | B1 | 112,807 |
| A2 | 114,911 | B2 | 113,058 |
| A3 | 111,706 | B3 | 114,129 |
| A4 | 112,974 | B4 | 113,524 |
| A5 | 110,575 | B5 | 110,773 |
| **A** | **563,161** | **B** | **564,291** |

Both passes independently wrote **L14 = DUP of L13**, as DV1b did. [PLAIN] rows: 3 per pass, on L34 and L37. Reader remarks,
kept as given: A3 left out signs cut off at s2's right edge; B1 said its images displayed at reduced size. Brace tokens: 5 per pass.

**Reader access log** (`access_log_reads.tsv`, `access_log.py`, from the session's subagent transcripts; F63): 189 tool calls.
Every Read was the call's own task file, the sheet png, or one of its own c105_f102r crops. Each of the 74 crops was viewed once
per pass, the sheet 10 times. Each Bash call was the reader's own TSV write. **Calls outside the allowlist: 0.**

| output | signs | sha256 | commit |
|---|---|---|---|
| outputs/vivonne1573-f102r-dev2/passA_sv.tsv | 1,817 on 36 lines | bb145964726788033eaac58429fa1f7173d5c4f688cfd73f75089034214fd249 | 5dd420b64 |
| outputs/vivonne1573-f102r-dev2/passB_sv.tsv | 1,822 on 36 lines | 37936450e635c862749a0afdca883b57a02e07a4df298eb39eead9233938d686 | 5dd420b64 |

## Step 3: reconcile + packet adjudication
`reconcile_passes.py --keep-alts`: **agreement 1657/1846 = 89.8%** (DV1b 86.1%); agreed-H 1,000, agreed-uncertain 657,
disagree 189. The queue has 846 rows. **12 packets** (11 x 16 + 1 x 13). Queue, packets, tasks and template were committed in
5dd420b64 before any adjudication call. One fresh Sonnet call per packet:

| packet | lines | tokens | A | B | other | NONE | viewed (reply) | crops opened (log) |
|---|---|---|---|---|---|---|---|---|
| P01 | L01-L04 | 110,791 | 10 | 6 | 0 | 0 | 16/16 | 8/8 |
| P02 | L04-L08 | 108,963 | 16 | 0 | 0 | 0 | 16/16 | 8/8 |
| P03 | L08-L13 | 111,115 | 10 | 6 | 0 | 0 | 16/16 | 10/10 |
| P04 | L13-L18 | 111,556 | 8 | 8 | 0 | 0 | 16/16 | 10/10 |
| P05 | L18-L21 | 110,432 | 5 | 8 | 0 | 3 | 16/16 | 8/8 |
| P06 | L21-L25 | 110,455 | 5 | 10 | 0 | 1 | 16/16 | 10/10 |
| P07 | L25-L27 | 108,408 | 9 | 6 | 0 | 1 | 16/16 | 6/6 |
| P08 | L27-L28 | 107,739 | 9 | 6 | 0 | 1 | 16/16 | 4/4 |
| P09 | L29-L30 | 107,245 | 13 | 3 | 0 | 0 | 16/16 | 4/4 |
| P10 | L30-L32 | 110,185 | 6 | 6 | 0 | 4 | 16/16 | 6/6 |
| P11 | L32-L35 | 111,047 | 9 | 6 | 1 | 0 | 16/16 | 8/8 |
| P12 | L35-L37 | 107,264 | 5 | 7 | 0 | 1 | 13/13 | 4/4 |
| **total** | | **1,315,200** | **105** | **72** | **1** | **11** | **189/189** | **86/86** |

**Packet access log** (`access_log_packets.tsv`; F63): every adjudicator opened its task, its queue, the sheet and every crop its
task named. **Calls outside the allowlist: 0.** Conf: H 4, M 115, L 70. Disclosure: P02 chose candidate A on all 16 of its rows.
Its notes describe a shape for each row ("tailed z shape", "r before y"), so the verdicts were kept as returned. A rule-shaped
pattern cannot be excluded from the file alone.
`assemble_z.py`: passZ_sv = the reconciler's draft with the 189 verdicts applied (NONE drops), **1,835 signs**; 48 positions
differ from the draft.

| output | sha256 | commit |
|---|---|---|
| adjud_out.tsv | d39991b4b03bfaa86823d3af4004f45c4a87ad3606d20825fbdbe12643031bbf | 617286fd6 |
| **outputs/vivonne1573-f102r-dev2/passZ_sv.tsv** | **dbceb0dd6ed80ff6d62e9a29371a8ecea5718790d4040d1b484a1122faf587c0** | **617286fd6** |
| packet outputs, access logs | SHA256SUMS_passZ.txt, SHA256SUMS_packets.txt | 617286fd6 / 5dd420b64 |

## Step 4: ONE score (`tx_bench_out.txt`, sha256 a0fbdd77ed575ac6382331babaca98afeeca6437f8c209597ebdf0521e488b07)
`python3 tools/tx_bench.py passZ_sv.tsv passA_sv.tsv passB_sv.tsv --bench BENCHMARK-TX.tsv --item vivonne1573-f102r-dev2
--paired benchmark-tx/outputs/vivonne1573-f102r-dev/passZ_dv1.tsv --exclude-flagged --strict`, run once at 03:11:48 UTC. The
as-measured figures come from the same run (--exclude-flagged prints both). Per item: dev2 is the only item.

**Headline, value-level, flagged excluded (679 unflagged), against passZ_dv1:**

| output | err_true (0.75 align) | SER (unit cost) | position errors / 679 + insertions / signs read (F48) | strict / visual-ID SER | as measured err_true / SER (1234) |
|---|---|---|---|---|---|
| **passZ_sv** | **0.088 (60/679)** | **0.085 (58/679)**: S 24 D 5 I 29 | 29/679 = 0.043 + 31/1,835 = 0.017 | 0.083 (56/679) | 0.246 / 0.245 |
| passA_sv | 0.077 (52/679) | 0.075 (51/679) | 30/679 + 22/1,817 | 0.071 | 0.244 / 0.244 |
| passB_sv | 0.074 (50/679) | 0.072 (49/679) | 27/679 + 23/1,822 | 0.069 | 0.239 / 0.238 |
| passZ_dv1 (base, Amendment 9 (24)) | 0.124 (84/679) | 80 edits | 43/679 + 41/1,827 | | 0.276 |

**Gate endpoint, passZ_sv vs passZ_dv1, line level, flagged excluded:** 36 lines; **lines improved 16, worsened 8, tied 12;
line sign test p = 0.1516**; unit-cost edits on the 679 unflagged **80 -> 58 (0.725x, a 27.5% fall)**.
Position McNemar, beside: 679 common positions; base wrong 43, output wrong 29; **fixed 22, broken 8, exact p = 0.0161**.
As measured, beside: lines 21 / 7 / 8, p = 0.0125; edits 337 -> 302; McNemar fixed 43, broken 17, p = 0.0011.
The single passes, beside only (not the gated output), flagged excluded: passA_sv lines 18/7/11, p 0.0433, edits 80 -> 51;
passB_sv lines 18/4/14, p 0.0043, edits 80 -> 49. As on the DV1b leaf, the single pass B beats the two-pass pipeline output
(0.074 vs 0.088).

## Verdict (as declared)
Declared gate: PASS = lines improved > lines worsened at line sign test p < 0.05 AND unit-cost edits on the 679 unflagged
at most 0.8x passZ_dv1's. Measured: 16 > 8, but **p = 0.1516, not < 0.05**; edits 0.725x, which meets the second condition.
**dev FAIL.**

What this licenses: no product recommendation on sheet form and no second-hand test from this gate. Never an S1 claim, never
any f.103r step. The direction favours the pictured sheet on every figure: edits -27.5%, position McNemar 22/8 at p 0.016, and
both single passes significant at the line level. These are beside-figures, and the declared line-level endpoint did not reach
p < 0.05 at 36 lines. The line-level test's power was not simulated (PREREG, said, not hidden). A FAIL with the effect pointing
the declared way is a reason for the lane to price a line-level power check or a second dev leaf. It is not a reason to
re-score this one: no second score was run, and the gate was not loosened.

## For the lane (suggestions, not done)
- The insertion count fell from 41 to 31 and position errors from 43 to 29. The [PLAIN:] sentence and the sheet are confounded
  in this protocol (both were declared in step 1), so the insertion fall is not attributable to the sheet alone.
- Cost: the lane's get_session reading (22 subagent calls: 10 Opus reads, 1,127,452 tokens; 12 Sonnet packets, 1,315,200 tokens).

| file | sha256 |
|---|---|
| tx_bench_out.txt | a0fbdd77ed575ac6382331babaca98afeeca6437f8c209597ebdf0521e488b07 |
| adjud_task_template.txt | 77937ffe9702d7436ebc46c94a2ee04955352558296a7adcc3af9be6841adad5 |
| access_log_reads.tsv | f797ce552128fd08b42d041b32bc7f4608ab41b2c9c76370eae92ea871005495 |
| access_log_packets.tsv | 8eac2fabd26bd26d2b99181804a6b92c53744fb572c1cfb02e5476d3d3124d7a |

Openings of eval truth: 0. dev openings: 1.

## Citation correction (lane incarnation 5, 10 Oct 2026 03:5x UTC by date -u; TX-RED pass 17 F80)
The header's "PREREG push 8212de547" names PREREG-21's first push (02:11, which did not yet hold SHEET-VIV); the SHEET-VIV section entered
in **c29543f04 (02:54:18 UTC)**, which is this job's PREREG push of record. The order holds: reader_task.txt committed a1635d222 (03:01:47)
after it, before the first read.
