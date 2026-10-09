# TXE2-MODEL2 (PREREG benchmark-tx/PREREG-txeng2-6.md X21b): the reader model on independent truths only

LANE TX-ENGINEER-2, account 4 (incarnation 2), worker TXE2-MODEL2 (Opus 5.5). Run 9 Oct 2026, 19:13-19:2x UTC by date -u.

**Scope**
- The pool is the three items whose truth does not depend on any reader:
  - dev_tune (birago1572-no87 f178v L01-12): clerk sheet.
  - dint-f128-print: the 1882 print.
  - ceppo-f36v-gloss: the period interlinear gloss, 16 scored positions.
- ceppo-f87-S and f21v are left out (Amendment 4).

No eval item was scored or opened, no truth file was edited, and no host was contacted.

## Arms (same crops per item; only the reader model differs; same reconcile + Sonnet adjudication for both arms)

| item | Sonnet arm readers | Opus arm readers | crops | reconcile / adjudication |
|---|---|---|---|---|
| dev_tune | X21's (committed `passX21_sonnet_pipeline.tsv`, reused as it is; sha256 7940527ad1aae762, unchanged since X21) | X21's fresh Opus pair (`passX21_opus_pipeline.tsv`, 314d30d988843f5c, unchanged) | f178v s1/s2/s3, 36 | as X21 |
| dint-f128-print | folder passA/passB (Sonnet) | **two fresh blind Opus 5.5 calls** (`reads/dint_o1.tsv`, `dint_o2.tsv`), one page per call, the 8 native crops `images/f128_L0?_s{1,2}.jpg` unresized, brief = the folder's `f128/pass_instructions.md` verbatim | 8 | Sonnet arm: `pipeline.py prep` regenerated an adjudicate_in byte-identical to X21's (26 rows), so X21's Sonnet adjudication was reused and the pipeline output is identical to `passX21_sonnet_pipeline.tsv`. Opus arm: fresh Sonnet adjudicator, 18 rows (candA 4, candB 12, NONE 2) |
| ceppo-f36v-gloss | **two fresh blind Sonnet calls** (`reads/f36_s1.tsv`, `f36_s2.tsv`) | **two fresh blind Opus 5.5 calls** (`f36_o1.tsv`, `f36_o2.tsv`) | committed `witness_f36/cited/v36top_L01_s{1,2}.jpg` + `sign_sheet_blind.png` | one fresh Sonnet adjudicator per arm: Sonnet arm 3 rows (candA 2, candB 1), Opus arm 1 row (candA) |

**f36v readability.** All 16 positions were read in one call each: 19-21 signs per reader, 0 `?` rows. f36v was not dropped.

**Scripts.**
- `pipeline.py` and `adj_prompts.py` are copies of `../model/` with only the item list and output names changed. The f36v adjudication layout text is added.
- `score.py` is model/score.py with the pool changed.
- Reader prompts were committed in **0b44b9dc8**, before any read.
- Readers were blind subagents. They got scratch copies of the crops, plus the sheet or the brief. They never saw truth, decodes, or other passes.

**Crop step.** No crop was cut. All crops are the committed files listed above.

## Calls and tokens (subagent_tokens from each call's completion notice)

| call | model | tokens | tool uses |
|---|---|---|---|
| dint_o1 (page) | Opus 5.5 | 138,073 | 17 |
| dint_o2 (page) | Opus 5.5 | 146,847 | 19 |
| f36_o1 | Opus 5.5 | 103,700 | 6 |
| f36_o2 | Opus 5.5 | 103,704 | 6 |
| f36_s1 | Sonnet | 103,127 | 6 |
| f36_s2 | Sonnet | 103,100 | 6 |
| adj dint, Opus arm (18 rows) | Sonnet | 106,175 | 12 |
| adj f36v, Sonnet arm (3 rows) | Sonnet | 102,651 | 7 |
| adj f36v, Opus arm (1 row) | Sonnet | 102,361 | 7 |

That is 9 calls against 8 units priced: 6 reads and 3 adjudications. The cost is the orchestrator's get_session reading.

Reader agreement before adjudication:

| item | Sonnet pair | Opus pair |
|---|---|---|
| dint | 165/191 (0.86, folder A/B) | 171/189 (0.90, fresh) |
| f36v | 16/21 (0.76) | 19/22 (0.86) |

## Committed before any score

All 28 files are listed with their full sha256 in `sha256_before_score.txt`, committed in **2383f4e86** before `score.py` was run. Intermediate commits: ef8cc8840, 83f415f5f, db7c0e721.

| file (benchmark-tx/) | sha256 (leading 16 hex) | commit |
|---|---|---|
| outputs/dint-f128-print/passX21b_opus_pipeline.tsv | 44d30b9ab9508cfa | 2383f4e86 |
| outputs/dint-f128-print/passX21b_opus_r1.tsv / _r2 / _reconcile | 4bde128a2c74608c / 365ec14023f63b51 / ff0f53f716b8267c | db7c0e721 |
| outputs/dint-f128-print/passX21b_sonnet_pipeline.tsv | fab625caeb5c6530 | ef8cc8840 |
| outputs/dint-f128-print/passX21b_sonnet_A / _B / _reconcile | c3944f924b2a500e / 303657ac972910c7 / b025a40e56924c01 | ef8cc8840 |
| outputs/ceppo-f36v-gloss/passX21b_opus_pipeline.tsv | aa27630dd10f3c5b | ef8cc8840 |
| outputs/ceppo-f36v-gloss/passX21b_opus_r1 / _r2 / _reconcile | b83c86801dd32505 / d6ba9e5b6102c0ac / 170a063be654e26d | ef8cc8840 |
| outputs/ceppo-f36v-gloss/passX21b_sonnet_pipeline.tsv | 7f4a2d628fb4aa06 | ef8cc8840 |
| outputs/ceppo-f36v-gloss/passX21b_sonnet_A / _B / _reconcile | 6ba32f7c8cdd8a69 / 3db7032cb73aa08c / 41467d699bc05685 | ef8cc8840 |
| outputs/birago1572-no87/passX21_opus_pipeline.tsv (reused) | 314d30d988843f5c | 15eb3f17 (X21) |
| outputs/birago1572-no87/passX21_sonnet_pipeline.tsv (reused) | 7940527ad1aae762 | 15eb3f17 (X21) |
| txeng2/model2/reads/dint_o1, dint_o2 | 6f2c9689e4a8b258, 37df99728d6b902d | 83f415f5f, db7c0e721 |
| txeng2/model2/reads/f36_o1, f36_o2, f36_s1, f36_s2 | 02f0f290f0f045da, 2ce53417a52b4a5c, 8365080f65561aec, 654465063bf79595 | ef8cc8840 |
| work/*/adjudicate_out.tsv (dint opus, dint sonnet, f36v opus, f36v sonnet) | 96747df43b906887, eb2ec8e89ba91ccf, 45d4497aafa102ba, 3b823bebf83751f8 | 2383f4e86 / ef8cc8840 |

## Per-item scores (`score.py`, full output in `score.txt`)

The scores are err_true with Wilson 95% intervals. The flagged-excluded figure is identical except on dev_tune, where it is shown in brackets.

| item | Opus pipeline | Sonnet pipeline | Opus vs Sonnet base: fixed / broken, p | reverse |
|---|---|---|---|---|
| dev_tune (343; 338) | 0.044 (15) 0.027-0.071 [0.030] | 0.050 (17) 0.031-0.078 [0.036] | 8 / 6, p 0.79 | 6 / 8, p 0.79 |
| dint-f128-print (85, label-mapped) | 0.176 (15) 0.110-0.271 | 0.212 (18) 0.138-0.310 | 5 / 3, p 0.73 | 3 / 5, p 0.73 |
| ceppo-f36v-gloss (16) | 0.188 (3) 0.066-0.430 | 0.312 (5) 0.142-0.556 | 4 / 2, p 0.69 | 2 / 4, p 0.69 |

Single readers on the same scale:

| item | Sonnet A | Sonnet B | Opus r1 | Opus r2 |
|---|---|---|---|---|
| dev_tune | 0.064 | 0.093 | 0.038 | 0.052 |
| dint | 0.247 | 0.188 | 0.188 | 0.200 |
| f36v | 0.250 | 0.375 | 0.188 | 0.125 |

## Pooled (independent truths only: dev_tune + dint-f128-print + ceppo-f36v-gloss)

| | Opus pipeline | Sonnet pipeline |
|---|---|---|
| err_true | 0.074 (33/444) 0.053-0.103 | 0.090 (40/444) 0.067-0.120 |
| flagged excluded | 0.064 (28/439) | 0.080 (35/439) |
| paired, Opus pipeline vs Sonnet base | fixed 17, broken 11, two-sided sign test **p 0.345** (flagged excluded the same) | |

## Controls

**The fresh Opus dint pair agrees with itself.**
- The two readers agree on 171/189 signs (0.90).
- Their own spread is 2 fixed / 2 broken (r2 vs r1).
- Both single readers (0.188, 0.200) fall inside the Sonnet A/B range (0.247, 0.188).
- X21 reused the X8/X8b arm-b reads for this pair and got 0.235 and 0.318. The fresh pair reads better than those reads did.

**Sonnet dint arm against the folder's committed reconcile: a non-test by construction.**
- The dint truth is built from the folder's reconciled read. The BENCHMARK-TX row says that read "scores 0 by construction and is not scored".
- So no arm can beat it, and this control cannot fail (CLAUDE.md rule 3, a control that cannot vary).
- What it does show: the Sonnet arm here is byte-identical to X21's Sonnet dint pipeline. Nothing in that arm changed between X21 and X21b.

**f36v: the fresh Sonnet arm against the folder's committed `recon.tsv`.**
- The fresh arm scores 0.312; the folder's recon scores 0.438. Paired, that is 2 fixed / 0 broken, p 0.50.
- This is within reader spread: Sonnet B vs A is 0 / 2, and the gap is one error-pair either way.
- The fresh arm does not beat the committed reconcile by more than reader spread.

**dev_tune** is unchanged from X21. The Sonnet arm against L is 1 fixed / 6 broken, so it is not better than L.

## Declared gate and outcome, as registered

The gate is a two-sided sign test, p < 0.05 pooled.

**Outcome: null.** The Opus pipeline is ahead 17 fixed / 11 broken, p 0.345.
- No item is significant, and all three items lean the same way (Opus).
- As registered, the result is logged as **"untested at this N on independent truths"**, and the reader rule stands.
- X21's pooled Sonnet win (33/14) does not reproduce once the Ceppo S item is removed. That is consistent with TX-RED F15.
- This worker changes no rule; the lane decides.

## Deviations (all fixed before scoring)

1. **Three adjudication calls, not two.** One Sonnet adjudicator was used per f36v arm, so that each arm has the identical protocol and neither adjudicator sees the other arm. The calls came to 9 against 8 units priced.
2. **dint Sonnet arm adjudication reused from X21.** The regenerated adjudicate_in is byte-identical to X21's. The PREREG asks for the "folder's passA/passB reconciled by the same protocol (as X21 did)".
3. **The overlap figure in the dint brief is wrong.** Both fresh Opus readers measured the s1/s2 overlap at about 1,100-1,300 px. The folder's `pass_instructions.md` (unchanged, the same text the Sonnet passes A/B got) states about 150 px, and so does the adjudicator prompt, which is the same as X21's. Both readers say they transcribed each sign once. X21 found the same kind of misstatement on dev_tune.
4. **f36v reader brief.** The brief is the folder's `blind_pass_brief.md` with a layout preface. The preface says the s1/s2 crops overlap, as these cited crops do, and that the small letters above the signs are to be ignored. The brief's own header line names fr.3251, where this leaf is fr.3252; it was left as the folder wrote it.
5. **dint reader o1 measured pixel profiles with a script** in its scratch folder to place signs. It opened no other file. This is disclosed, not voided.
6. **f36v n = 16 is small,** and its interval is wide (BENCHMARK-TX row note).

Openings of eval truth: 0
