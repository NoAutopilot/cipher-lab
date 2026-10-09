# TXE2-MODEL (PREREG benchmark-tx/PREREG-txeng2-5.md X21): the reader model as an instrument

LANE TX-ENGINEER-2, account 4 (incarnation 2), worker TXE2-MODEL (Opus 5.5). Run 9 Oct 2026, 18:37-18:5x UTC by date -u.
Dev pool only: dev_tune + dint-f128-print + ceppo-f87-S (f36v's 16 positions left out). No eval item was scored or opened,
no truth file was edited, and no host was contacted.

## Arms
The full folder pipeline was run twice on the SAME crops of each item. The only difference between the runs is the reader model.
- **Sonnet arm**: the two existing blind Sonnet passes A/B on each item.
- **Opus arm**: two blind Opus 5.5 passes.
- **Both arms then went through the same steps**:
  - Value-blind reconcile by `ciphers/ceppo-nevers-fr3251-1570s/harvest/reconcile_blind.py`, the folder's own tool, unchanged.
    It aligns the two passes, keeps agreements, and applies the one-H-side rule. A one-reader sign at H goes to '?'; a
    one-reader sign below H is dropped.
  - `adjudication_sheet.py`'s sheet: four agreed neighbours on each side, both candidates, both notes.
  - A third, value-blind **Sonnet** adjudicator. Both arms got the same prompt text and never saw which arm they were
    settling (`adj_prompts.py`; `harvest/f178v/adjudicate_in/out.tsv` is the worked example).
  - `reconcile_blind.py --adjudicated` to apply the answers.
- The script is `pipeline.py`; every rule in it was declared in its docstring before any score.

| item | Sonnet readers (existing) | Opus reader 1 | Opus reader 2 | crops (same for both arms) |
|---|---|---|---|---|
| dev_tune (no.87 f178v L01-12) | f178v/passA.tsv + passA_L11-23.tsv; passB likewise | fresh, 2 calls (L01-06, L07-12) | fresh, 2 calls | committed `harvest/f178v/f178v_L??_s{1,2,3}.jpg`, 36 crops; brief `blind_pass_brief_1572.md` + `sign_sheet_blind_1572.png` |
| dint-f128-print | f128/passA.tsv, passB.tsv | X8 arm b `cost/reads/armB_page.tsv` (reused) | X8b arm b2 `cost2/reads/dint_b2.tsv` (reused) | the 8 native crops `images/f128_L0?_s{1,2}.jpg`, one call per page, as passes A/B |
| ceppo-f87-S | f87/passA.tsv, passB.tsv | X8b arm a `cost2/reads/c87_a_L0?.tsv` (reused, 5 per-line calls) | fresh, 1 call | `f87/lines2x/f87_L0?_s?.png`, 18 crops; brief `blind_pass_brief.md` + `sign_sheet_blind.png` |

Crop step (pasted). No crop was cut fresh:
- dev_tune and dint used the committed s1/s2/s3 crops.
- Ceppo's tracked 2x crops are gitignored and were regenerated with `python3 ciphers/ceppo-nevers-fr3251-1570s/harvest/cut_folio_lines.py`
  (output `f87 15 18`: 18 lines2x crops, the set passes A/B read).
- Readers got copies of the crops in a scratch folder, with no repository path in view.

## Disclosed choices and deviations (all found before scoring)
1. **dint: arm-b reads reused instead of re-reading.**
   - The PREREG reuses X8/X8b arm a "only if their crops are the s1/s2 crops pass A/B saw, else re-read". The arm-a crops were
     4-piece 2x re-renders, so the arm-a reads were not used.
   - The X8 arm b and X8b arm b2 reads are two Opus 5.5 readers on exactly the 8 native crops passes A/B saw, read in pass A/B's
     own one-call layout. That is what a re-read would have produced. They are used as the Opus pair, which saved 2 calls.
   - The lane may rule this out. If it does, the dint row of the tables below is void, and so is the pool.
2. **Ceppo Opus reader 1 used a different call layout from the Sonnet passes.**
   - It is X8b arm a: the same crops, but one call per line.
   - Reader 2 and both Sonnet passes read all the crops in one call.
3. **dint passes carry no per-sign conf.**
   - Every dint sign was given conf H in both arms, so every split and every one-reader sign went to the adjudicator.
   - Rows marked `CLEAR:` and the `-` mark were dropped (convert.py rule).
4. **NO87-LABELS (dev_tune).**
   - The committed pipeline L carries 7 value-blind relabels (T50 -> X_CE).
   - The same rulings were transferred to both arms, read-free, by aligning each arm's lines to the committed passC.
   - Transferred: Sonnet arm 7, Opus arm 0 (at those positions the Opus readers had not written T50).
   - Raw scores, with no transfer, are reported beside.
5. **The adjudicator calls varied in quality.**
   - The Sonnet-arm dev_tune L01-06 adjudicator made its own 3x zooms. The prompt did not forbid this.
   - The Sonnet-arm Ceppo adjudicator reported that it often could not locate positions by counting. It leaned on the readers'
     confidence and wrote generic notes, with 0 of 48 rows at H.
   - The Opus-arm Ceppo adjudicator said the same, more mildly.
   - All were kept as written. Re-running one arm's adjudicator alone would break the identical-protocol condition.
6. **Overlap stated wrongly in the brief.** One Opus dev_tune reader measured the s1/s2/s3 overlap as about 425 px at 2x, not
   the about 100 px the folder's brief states. That brief text is the same one the Sonnet passes got.

## Calls and tokens (subagent transcripts, `usage.py` from cost2; input exact, output a lower bound; `usage_raw.txt`)
| call | model | API turns | input (all) | cache write | output >= |
|---|---|---|---|---|---|
| d87_r1_a (L01-06) | Opus | 9 | 871,503 | 110,861 | 4,101 |
| d87_r1_b (L07-12) | Opus | 9 | 872,304 | 110,380 | 3,313 |
| d87_r2_a | Opus | 9 | 871,538 | 110,983 | 4,293 |
| d87_r2_b | Opus | 15 | 1,545,909 | 119,164 | 4,786 |
| c87_r2 (f87 page) | Opus | 8 | 800,744 | 85,207 | 2,960 |
| adj dint, Sonnet arm (26 rows) | Sonnet | 4 | 344,009 | 104,691 | 62 |
| adj dint, Opus arm (28 rows) | Sonnet | 4 | 343,911 | 104,535 | 136 |
| adj dev_tune, Sonnet arm L01-06 (17) | Sonnet | 10 | 1,024,978 | 85,869 | 108 |
| adj dev_tune, Sonnet arm L07-12 (22) | Sonnet | 7 | 679,824 | 87,703 | 4,592 |
| adj dev_tune, Opus arm (11 rows, 7 lines) | Sonnet | 5 | 446,087 | 72,259 | 142 |
| adj ceppo, Sonnet arm (48) | Sonnet | 6 | 574,538 | 81,524 | 53 |
| adj ceppo, Opus arm (36) | Sonnet | 4 | 352,062 | 79,375 | 120 |

That is 12 subagent calls: 5 fresh Opus reads and 7 Sonnet adjudications. Reused reads: dint 2, Ceppo 1 (5 per-line calls,
from X8b). Reader agreement before adjudication:

| item | Sonnet A/B agreement | Opus agreement |
|---|---|---|
| dev_tune | 318/359 (0.89) | 341/353 (0.97) |
| dint | 165/191 (0.86) | 165/193 (0.85) |
| ceppo | 156/217 (0.72), equal to HARVEST-D2's 156/217 and 48 sheet rows | 165/205 (0.80) |

## Committed before any score (sha256 beside the commit)
All the outputs below are in `sha256_before_score.txt`: 37 files, every passX21_* output, every read, every adjudicate_out. That
file was committed in **15eb3f17** (pushed 18:50 UTC) before `score.py` was run at all. Reader prompts: **1fd962db** (before any read).
| file | sha256 (leading 16 hex) | commit |
|---|---|---|
| outputs/birago1572-no87/passX21_opus_pipeline.tsv | 314d30d988843f5c | 15eb3f17 (written 162e40cc) |
| outputs/birago1572-no87/passX21_sonnet_pipeline.tsv | 7940527ad1aae762 | 15eb3f17 |
| outputs/birago1572-no87/passX21_opus_pipeline_raw.tsv | fc38f656934eb1c2 | 15eb3f17 |
| outputs/birago1572-no87/passX21_sonnet_pipeline_raw.tsv | d61e2c7e1a921ebd | 15eb3f17 |
| outputs/dint-f128-print/passX21_opus_pipeline.tsv | 0dafc0508fcf4c0a | dfe0ba6f |
| outputs/dint-f128-print/passX21_sonnet_pipeline.tsv | d01c38bb4b1ed548 | dfe0ba6f |
| outputs/ceppo-f87-S/passX21_opus_pipeline.tsv | 9b921f807cbf9559 | 15eb3f17 |
| outputs/ceppo-f87-S/passX21_sonnet_pipeline.tsv | 5b17c3413902302f | db6190f3 |
| txeng2/model/reads/d87_r1_a, d87_r1_b, d87_r2_a, d87_r2_b, c87_r2 | 27cab993f4467e1f, 60a91148fdfb035c, f63857a1487044bc, 6ffd73b32c3d9bb6, 8ffe0a1df5f28900 | dfe0ba6f / 1aa873b2 |

## Per-item scores (`score.py`, a wrapper over tools/tx_bench.py's own functions; full output `score.txt`)
err_true (Wilson 95%). The flagged-excluded figure is identical except on dev_tune, which is shown in brackets.
| item | Opus pipeline | Sonnet pipeline | paired Opus vs Sonnet base: fixed / broken, p | reverse direction |
|---|---|---|---|---|
| dev_tune (343; flagged-excl 338) | 0.044 (15) 0.027-0.071 [0.030 (10)] | 0.050 (17) 0.031-0.078 [0.036 (12)] | 8 / 6, p 0.79 (flagged-excl 8 / 6, 0.79) | 6 / 8, p 0.79 |
| dint-f128-print (85, label-mapped) | 0.247 (21) 0.168-0.348 | 0.212 (18) 0.138-0.310 | 4 / 8, p 0.39 | 8 / 4, p 0.39 |
| ceppo-f87-S (139) | 0.173 (24) 0.119-0.244 | 0.050 (7) 0.025-0.100 | 2 / 19, p 0.0002 | 19 / 2, p 0.0002 |

Single readers on the same scale:

| item | Sonnet A | Sonnet B | Opus r1 | Opus r2 |
|---|---|---|---|---|
| dev_tune | 0.064 | 0.093 | 0.038 | 0.052 |
| dint | 0.247 | 0.188 | 0.235 | 0.318 |
| ceppo | 0.043 | 0.129 | 0.165 | 0.129 |

On dev_tune the Opus readers are each better than either Sonnet reader. On Ceppo both Opus readers are worse than Sonnet A,
the result X8b already showed for single passes.

## Pooled (dev_tune + dint-f128-print + ceppo-f87-S)
| | Opus pipeline | Sonnet pipeline |
|---|---|---|
| err_true | 0.106 (60/567) 0.083-0.134 | 0.074 (42/567) 0.055-0.099 |
| flagged excluded | 0.098 (55/562) | 0.066 (37/562) |
| paired, Sonnet pipeline vs Opus base | fixed 33, broken 14, two-sided sign test **p 0.0079** (flagged excluded: 33 / 14, p 0.0079) | |
| paired, Opus pipeline vs Sonnet base | 14 / 33, p 0.0079 | |

## Control (fresh Sonnet arm beside the committed Sonnet pipelines)
| item | committed pipeline | fresh Sonnet arm | paired, fresh arm vs committed base |
|---|---|---|---|
| dev_tune | L 0.035 (12/343) | 0.050 (17/343) | fixed 1, broken 6 |
| ceppo-f87-S | folder passC 0.050 (7/139) | 0.050 (7/139) | -- |

- **dev_tune.** The fresh arm is worse than L, not better. The gap is reader-spread sized: Sonnet B vs A was 10 / 17. Part of
  the gap is the 7-row relabel step: the fresh arm without the transfer reads 0.070.
- **Ceppo.** The fresh arm reproduces the folder's own passC exactly, at the same error.
- The no-leakage condition holds: the fresh arm does not beat L. The test is a valid test, not a non-test.

## Declared gate and outcome, as registered
Gate: two-sided sign test, p < 0.05 pooled.

**Outcome: the Sonnet pipeline wins, 33 fixed / 14 broken, p 0.0079.** As registered, a Sonnet win fires Amendment 3's
re-baselining rule. That is the lane's act; this worker re-baselines nothing.

The same numbers, said plainly:
- **The pooled win comes from one item.** Ceppo-f87-S gives 19 / 2. Without Ceppo, Opus is ahead 12 / 14 (dev_tune 8 / 6,
  dint 4 / 8), which is a null.
- **dev_tune does not show it.** On dev_tune (no.87's hand, the eval hand's leaf) Opus readers read better singly, and the
  Opus pipeline is not worse.
- **Two caveats on the Ceppo margin.**
  - Its Opus pair mixes a per-line reader with a page reader (deviation 2).
  - Both Ceppo adjudicators were shallow (deviation 5).
- **dint rests on deviation 1** (reused arm-b reads).

The result is per hand. That bears on the lane's rule from Amendment 3 ("no eval look on an item whose baseline model differs
from the instrument's reader"), and the lane decides.

Openings of eval truth: 0
