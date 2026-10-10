# Transcription standard (owner's ask, 3 Oct 2026: "a 10x effort on the tool we use for every cipher")

Every account, lane and worker that turns a page image into signs follows this file. It sets the target, the
measurement and the pipeline. `.claude/briefs/transcription.md` is the job template that applies it; CLAUDE.md Usage 6
points here. Changes go through a parent (SYSTEM.md row, UPDATES.md line), like any shared rule.

## Why

Transcription, not keys, is now the bottleneck. On 3 Oct 2026 every unread Birago 1572 letter (f.117, f.144, f.168)
already has its key; each stalls because two readers split 15-33% of signs, and at that error a power control
cannot license a key on a short letter. Same for Birago 1571 f.36/f.47 (0.33), Florence c.127 (0.17), Debosnys (0.28).
The look-alike pass showed that agreement can rise while accuracy does not (LESSONS.md "Look-alike pass").

## What excellent means (targets)

| # | Property | Target | Today (3 Oct 2026) |
|---|---|---|---|
| 1 | True per-sign error, measured against a known answer | <= 5% on symbol ciphers, <= 1% on digits | BENCHMARK-TX.tsv + `tools/tx_bench.py` (TX-BENCH, 3 Oct 2026). Held-out (eval) Birago no.87, 803 scored signs: single blind pass A 0.069 (0.053-0.088), pass B 0.100 (0.081-0.122), reconciled 0.053 (0.040-0.071), reconciled + NO87-LABELS relabels 0.045 (0.033-0.061); per leaf the reconciled read is 0.083 f.178r, 0.055 f.178v, 0.013 f.179r. Dev: f.36v gloss line 0.31-0.44 on 16 signs; Ceppo f.21v/f.87 single passes 0.04-0.13 on S spans. Value-level lower bounds (see Benchmark); TXB2 (3 Oct 2026), dev item dint-f128-print (fr.3621 f.128r, Dinteville 1592 hand, 85 scored / 98 excluded, truth = 1882 print through key_print agree==n>=2; reconciled read is the reference, not scored): blind Sonnet pass A 0.353 (0.260-0.459) raw / 0.247 (0.168-0.348) with --label-map; pass B 0.306 (0.218-0.410) raw / 0.188 (0.119-0.284) mapped -- a symbol hand far above the 5% target; the raw-vs-mapped gap is label inventory (D/al/zh split after the passes), not glyph error; fr3416 f.38, fr4715 f.38v, fr3993 ff.71-72 not built (one raw pass or no raw passes on disk); TX-VIEWS (4 Oct 2026, f.178r+f.179r of no.87, 164 signs, pre-registered pilot): three blind Sonnet view reads (pad 0.165, s125 0.159, warp 0.140) + A + B voted 5 ways = 0.085, identical to pass A; vs the current reconcile (passC 0.049) paired fixed 0 / broken 6, p = 0.031 -- FAIL, not adopted; 7 of the 6+8 errors are an f.178r L03 tail the fixed-band crop cuts off for every reader, and the views repeat 13-14 of A's 14 errors (phi with A 0.71-0.76), benchmark-tx/tx-views-2026-10-04.md **Today (9 Oct 2026, TX-TRUTH-VERIFY): no.87 pass L as measured 0.042 (34/803, after 2 image-backed truth corrections), flagged excluded 0.029 (23/792); floor 18/803 as measured, 7/792 flagged excluded; table below the targets.** **Today (9 Oct 2026 22:22 UTC, TX-ENGINEER-2 S2 look, product baseline on an UNSEEN hand): vivonne1573-f103r-confirm2 (Saint-Gouard clerk hand 1573, 1,068 scored): the frozen pipeline (two blind Opus passes + reconcile + packet adjudication) as measured 0.296 (316/1068), flagged-excluded 0.150 (75/500; flags from the two blind clerk reads, not the clerk image); single S2 passes 0.148/0.154; the builder's own earlier passes 0.048/0.074 beside; S2-NOTE found no notation effect (notation 0 / segmentation 42 / read 33 of the 75); the two figures are two scores under two masks, not bounds (outside review 10 Oct, research/SO-TX-TRANSCRIPTION-2026-10-10.md); corrected audit with the fixed scorer (10 Oct 01:12 UTC, benchmark-tx/txeng2/scorerfix/RESULTS.md): 0.150 / 0.296 reproduced, standard unit-cost SER 0.134 (S 37 D 19 I 11) / 0.288 beside, lines missing 0, line-level paired vs committed 0 improved / 23 worsened (the cannot-differ shape); value-level throughout; SCAN-103 found the truth's alignment NOT BEST by 155 letters (fair margin 0.0267 vs 0.03) and a re-anchored second truth (RE103, item -s6500) is being built, the frozen readings to be scored once against it and reported here beside, never replacing, the look (benchmark-tx/txeng2/s2score/).** |
| 2 | Every transcription reports its error with the method named | always: `err_true` (benchmark-calibrated) or `err_2reader`, never "agreement" alone | mixed |
| 3 | Signs are image tiles in one atlas per key family, not strings typed per letter | every symbol cipher | Birago 1572 family atlas built (TX-ATLAS-B72, 3 Oct 2026: 18 pages, 4,209 tiles, ciphers/nevers-birago-fr3251-1572/atlas/); on no.87 held-out the atlas top-1 reads err_true 0.162 (tx_bench, 61/376) vs line reads 0.040 on the same lines -- an atlas of connected components does not yet replace line reads on this hand |
| 4 | Each sign carries top-k candidates with confidences | k=3 | `glyph_atlas.py classify --topk 3` (TX-ATLAS-B72): per-letter k1-k3 with distance and vote share in ciphers/nevers-birago-fr3251-1572/atlas/topk/; truth outside the atlas top-3 on 0.261 of no.87 held-out signs |
| 5 | Ambiguity is settled with the key and the language in the loop, and reported as such (grade S, never H) | key-constrained decode over the candidate lattice | tools/key_decode_lattice.py (TX-DECODE, 3 Oct): on two-pass lattices no.87 err_true 0.081 -> 0.100 at the pre-registered lam 1 (fails) and 0.071 at lam 4 (tuned; held-out gain ~2 tokens). Only 27/97 errors have the truth in the lattice. TX-ALTS (4 Oct): `--keep-alts` + an a/b? pass rule did not raise it enough (f178r+f179r 12/35 vs gate 50%; lam 4 0 fixed / 0 broken): not adopted, though the a/b? reader put the truth in its own alternatives at 12 of its 29 errors (old pass A 0/18). At lam 4, f.144r / f.168 / f.117r go from rank 22 / 20 / 10 to 1/201 (z 3.10 / 2.77 / 3.66); shuffled-target control fails (z <= 1.91). Not readings |
| 6 | A person's decision on one tile propagates to every tile of that cluster in every letter of the key family | always | built 3 Oct (TX-SORTER): one move offers "apply to all N in this cluster"; `sign_sorter_apply.py --atlas-labels` writes it to the family atlas labels.json; waits on TX-ATLAS-B72's atlas for a real (not provisional) cluster run |
| 7 | The sorter asks the person only the tiles whose answer moves the reading most, about 10-20 per session | ranked by expected change in key rank / judge score | built 3 Oct (TX-SORTER): `--rank-lattice` scores each tile as reader weight on the runner-up x decode letters changed when forced (key_decode_lattice.py); Birago 1572 demo: 20 of 211 tiles ranked, on the family atlas (no.73, no.85, f.117: 458 tiles, 100 atlas clusters) the 20 ranked tiles reach 71 tiles through their clusters; 18 of the 20 are positions where the lattice decode overrode the top-1 label -- and TX-DECODE found the lam=1 decode raises err_true on no.87, so those overrides are questions for the person, not likely corrections |
| 8 | Cost per 100 signs known and falling | reported per job | one figure on file: HARVEST-D2 (Ceppo f.21v + f.35 + f.87, 547 signs, two blind passes + reconcile + decode + controls, USD 35.90 on Fable) = about USD 6.6 per 100 signs, an upper bound since it includes decoding; no other transcription job ledgers its sign count (TX-BENCH, 3 Oct 2026); TXB2 (3 Oct 2026): A2-DIN (fr.3621 f.128r, 183 signs, two blind passes + reconcile + gloss alignment, USD 5.01 on Opus 5.5) = about USD 2.7 per 100 signs, job-level upper bound (per-pass cost not ledgered); X8/X8b (9 Oct 2026, LANE TX-ENGINEER-2, benchmark-tx/txeng2/cost/, cost2/): one per-page Opus 5.5 call reads at 0.29-0.30x the input tokens of per-line 2x calls (dint 332k vs 1,096k input tokens per 100 reference signs) at an accuracy within one reader's spread, N=2 readers x 2 hands; neither Opus arm beats the best Sonnet single pass (reader-model test X21 running) |

### No.87 truth verification (TX-TRUTH-VERIFY, 9 Oct 2026)

A verifier session (not LANE TX-ENGINEER) decided TXE-T's 13 proposed truth-doubtful positions one by one from the clerk
clear-sheet image (canvas 182, `harvest/f179r_sheet/dec_L??_s?.jpg`), the printed 1572 key and NEVBIR-87ALIGN: 11 FLAG (8
alignment-doubtful: three "et" the clerk writes as one ampersand, "questo", "catholici", "hugonotti", "malta contentezza"; 3
clerk-doubtful: "guase", "lamossi", "de rauelli"), 2 CORRECT (f178v L02.8: clerk g + printed T42 = g, T42 accepted for g
there; f178v L11.17: the clerk wrote "eio", the shape of his "io" in L14, not "ero" -- truth r -> i), 0 KEEP. Verdicts and
reasons: `benchmark-tx/birago1572-no87.flags.tsv`; flag column in the truth file; `tools/tx_bench.py --exclude-flagged`.
As measured now includes the two corrections; the pre-verify column is BENCHMARK-TX as committed before this pass.
Never quote the flagged-excluded figure alone.

| output | pre-verify | as measured | flagged excluded (95%) | flagged |
|---|---|---|---|---|
| reconciled + NO87-LABELS (L) | 0.045 (36/803) | 0.042 (34/803) | 0.029 (23/792) 0.019-0.043 | 11 |
| pass A | 0.069 (55/803) | 0.066 (53/803) | 0.053 (42/792) 0.040-0.071 | 11 |
| pass B | 0.100 (80/803) | 0.097 (78/803) | 0.085 (67/792) 0.067-0.106 | 11 |
| reconciled (C, committed) | 0.053 (43/803) | 0.051 (41/803) | 0.038 (30/792) 0.027-0.054 | 11 |
| E (TX-SHEET) | 0.077 (62/803) | 0.075 (60/803) | 0.062 (49/792) 0.047-0.081 | 11 |
| F (TX-FABLE) | 0.093 (75/803) | 0.091 (73/803) | 0.078 (62/792) 0.061-0.099 | 11 |
| floor (wrong in all six of A B C L E F) | 20/803 | 18/803 | 7/792 | 11 |

TXE instruments' committed outputs (dev_tune lines, 343 scored, 5 flagged; others as named):

| output | as measured (95%) | flagged excluded (95%) | flagged |
|---|---|---|---|
| passD | 0.049 (8/164) 0.025-0.093 | 0.043 (7/163) 0.021-0.086 | 1 |
| passG2_library_dev_tune | 0.067 (23/343) 0.045-0.099 | 0.053 (18/338) 0.034-0.083 | 5 |
| passG2_library_dev_tune_r1 | 0.064 (22/343) 0.043-0.095 | 0.050 (17/338) 0.032-0.079 | 5 |
| passG2_library_dev_tune_r2 | 0.070 (24/343) 0.048-0.102 | 0.056 (19/338) 0.036-0.086 | 5 |
| passG_compare_dev_tune | 0.087 (30/343) 0.062-0.122 | 0.074 (25/338) 0.051-0.107 | 5 |
| passG_compare_dev_tune_m1b_H_all | 0.079 (27/343) 0.055-0.112 | 0.065 (22/338) 0.043-0.097 | 5 |
| passG_compare_dev_tune_m1b_H_top1 | 0.079 (27/343) 0.055-0.112 | 0.065 (22/338) 0.043-0.097 | 5 |
| passG_compare_dev_tune_m1b_any_top1 | 0.082 (28/343) 0.057-0.116 | 0.068 (23/338) 0.046-0.100 | 5 |
| passH2_geo | 0.077 (13/169) 0.045-0.127 | 0.049 (8/164) 0.025-0.093 | 5 |
| passH_geo | 0.089 (15/169) 0.054-0.141 | 0.061 (10/164) 0.034-0.109 | 5 |
| passJ_pair_dev_tune | 0.035 (12/343) 0.020-0.060 | 0.021 (7/338) 0.010-0.042 | 5 |
| passK2_sr4_dev_tune | 0.061 (21/343) 0.040-0.092 | 0.047 (16/338) 0.029-0.075 | 5 |
| passL_lattice_dev_tune_lam1 | 0.082 (28/343) 0.057-0.116 | 0.068 (23/338) 0.046-0.100 | 5 |
| passL_lattice_dev_tune_lam4 | 0.050 (17/343) 0.031-0.078 | 0.035 (12/338) 0.020-0.061 | 5 |
| passM_conf_dev_tune | 0.050 (17/343) 0.031-0.078 | 0.035 (12/338) 0.020-0.061 | 5 |
| passM_conf_dev_tune_lam1 | 0.079 (27/343) 0.055-0.112 | 0.065 (22/338) 0.043-0.097 | 5 |
| passM_confshuf_dev_tune | 0.050 (17/343) 0.031-0.078 | 0.035 (12/338) 0.020-0.061 | 5 |
| passM_confshuf_dev_tune_lam1 | 0.079 (27/343) 0.055-0.112 | 0.065 (22/338) 0.043-0.097 | 5 |
| passP_hints_dev_tune | 0.041 (14/343) 0.025-0.067 | 0.027 (9/338) 0.014-0.050 | 5 |
| passR_stab_dev_tune | 0.044 (15/343) 0.027-0.071 | 0.030 (10/338) 0.016-0.054 | 5 |
| passR_stabshuf1_dev_tune | 0.047 (16/343) 0.029-0.074 | 0.033 (11/338) 0.018-0.057 | 5 |
| passR_stabshuf2_dev_tune | 0.044 (15/343) 0.027-0.071 | 0.030 (10/338) 0.016-0.054 | 5 |
| passR_stabshuf3_dev_tune | 0.044 (15/343) 0.027-0.071 | 0.030 (10/338) 0.016-0.054 | 5 |
| passR_stabshuf4_dev_tune | 0.044 (15/343) 0.027-0.071 | 0.030 (10/338) 0.016-0.054 | 5 |
| passR_stabshuf5_dev_tune | 0.044 (15/343) 0.027-0.071 | 0.030 (10/338) 0.016-0.054 | 5 |
| passS_adj_fable_dev_tune | 0.044 (15/343) 0.027-0.071 | 0.030 (10/338) 0.016-0.054 | 5 |
| passS_adj_opus_dev_tune | 0.038 (13/343) 0.022-0.064 | 0.024 (8/338) 0.012-0.046 | 5 |
| passT_ordered_dev | 0.130 (15/115) 0.081-0.204 | 0.123 (14/114) 0.075-0.196 | 1 |
| passT_shuffled_dev | 0.104 (12/115) 0.061-0.174 | 0.097 (11/114) 0.055-0.165 | 1 |
| passU_feature_dev_tune | 0.055 (19/343) 0.036-0.085 | 0.041 (14/338) 0.025-0.068 | 5 |
| passV_s0_dev_tune | 0.064 (22/343) 0.043-0.095 | 0.050 (17/338) 0.032-0.079 | 5 |
| passV_s1_dev_tune | 0.050 (17/343) 0.031-0.078 | 0.035 (12/338) 0.020-0.061 | 5 |
| passV_shift_dev_tune | 0.050 (17/343) 0.031-0.078 | 0.035 (12/338) 0.020-0.061 | 5 |

## The pipeline (target state; each step names its tool)

1. **Images once** (CLAUDE.md Usage 4): `tools/gallica_folio.py`, `tools/iiif_lines.py --debug` (check the overlay).
2. **Segment every sign into a tile** across ALL letters of the key family at once: `tools/glyph_atlas.py segment`.
3. **Cluster** tiles by shape, deliberately over-split: `glyph_atlas.py cluster`. One atlas per key family, kept in
   the family's lead folder and reused by every sibling letter (Birago 1572: ciphers/nevers-birago-fr3251-1572).
4. **Name clusters, not tiles**: known answers first (clerk sheets, glossed lines, printed key shapes), then a model
   reader on cluster exemplar sheets (one call per sheet, not per line), then the person in the sorter.
5. **Classify** every tile to top-k clusters with distances: `glyph_atlas.py classify` (extended to emit top-k).
6. **Key-constrained decode** (to build, TX-DECODE): given top-k per sign, the key and a language model, choose the
   most probable reading; every changed sign is graded S and listed; controls as rule 3 (shuffled key, power at
   err_true).
7. **Active sorter** (to build, TX-SORTER): `tools/sign_sorter.py` gains a ranking of tiles by expected change in the
   decode, and `sign_sorter_apply.py` writes cluster-level decisions that every letter of the family picks up.
8. **Measure**: `tools/tx_bench.py` (to build, TX-BENCH) scores any pipeline output against BENCHMARK-TX.tsv and
   prints err_true per sign class; a job's NOTES.md pastes that line.

LLM line reading (two blind passes + `tools/reconcile_passes.py` + `tools/lookalike_pass.py`, its re-reads cut with `windows`, never the
echo-prone `packet`/`audit` line-crop prompts: 7/7 copied passC on Vivonne, N7-LKTOOL 4 Oct 2026) stays the fallback for
pages the segmenter cannot cut (joined hands, digits run together) and for numeral ciphers, and it must still report
err_true where a benchmark item of the same hand exists.

## Benchmark (BENCHMARK-TX.tsv, built by TX-BENCH)

Known-answer items, each with image, the sign sequence a person or period source fixes, and the source of truth:
Birago no.87 (clerk sheet, canvas 182); Birago 1571 f.36v L1 (period gloss); Ceppo f.21v and f.87 (published key
decode, the S-graded spans); colbert26 f.23/f.24 (interlinear keys); Mercy (H-graded spans); later Florence c.111/c.127.
Splits: tune on some, report on held-out ones (BENCHMARK.tsv's own rule). A pipeline change is adopted only when it
lowers held-out err_true.

**Result (TX-BENCH, 3 Oct 2026).** Four items built, disk only (`benchmark-tx/build_birago87.py`, `build_ceppo.py` regenerate the
truth files and the normalised pipeline outputs in `benchmark-tx/outputs/`). Truth for a sign = the set of signs whose key value is
the plain letter the known answer gives at that position (a homophone swap is invisible, so every figure is a value-level lower
bound on sign error); positions the known answer does not force (unaligned, off-sheet, key-split, uncertain span, M/I/U tokens) are
excluded and counted. `python3 tools/tx_bench.py OUTPUT.tsv --bench BENCHMARK-TX.tsv` aligns each line to the reference by edit
distance and reports wrong + deleted + inserted over scored, Wilson 95%, top confusions.

| item | split | truth | scored / excluded | pass A | pass B | reconciled | after look-alike / labels |
|---|---|---|---|---|---|---|---|
| birago1572-no87 (f.178r-179r) | eval | clerk clear sheet, C | 803 / 50 | 0.069 | 0.100 | 0.053 | passD 0.049 (f.178r+f.179r only, 164 signs); labels 0.045 |
| ceppo-f36v-gloss (fr.3252 f.36v L1) | dev | period interlinear gloss, C | 16 / 22 | 0.312 | 0.375 | 0.438 (`?` at splits) | passD 0.438 |
| ceppo-f21v-S | dev | S tokens of the committed decode | 189 / 78 | 0.048 | 0.053 | passC 0.005; committed = truth source | -- |
| ceppo-f87-S | dev | S tokens of the committed decode | 139 / 65 | 0.043 | 0.130 | passC 0.050; committed = truth source | -- |

Top confusions on no.87 (reconciled): s<-T50 x7 (the curled Ce, fixed by the labels), d<-T98 x7 (the T18/T98 pair, still open),
t<-T90 x3, e<-T76 x3, l<-T64 x2. What this says: on the held-out item the reconciled line read is at the 5% target and two
readers' reconciliation roughly halves a single pass's error; the T98/T18 look-alike is now the largest remaining error source.
The earlier 0.178/0.071 (LOOKALIKE-TOOL) counted letters outside matching blocks and included f.178r's uncertain opening; this
scorer is per sign against the key-forced set, so the two are not comparable figures. Limits: the no.87 sheet was aligned on the
reconciled sequence, so a segmentation error there is invisible and passC has a home advantage on segmentation; the Ceppo S items
are not independent of their committed reading (only the single passes are scored there) and cover only signs read at H, so they
understate error; the f.36v item is 16 signs. Not built: colbert26 f.23/f.24 (no raw reader passes on disk, and the gloss is
word-level: the sign-level alignment agrees on 63 of 294 tokens), Mercy (no independent known answer: S under an annealed key).
Next items: the f.36v gloss read beyond line 1 (F36-GLOSS bands) and the Florence c.111/c.127 glossed lines; and per TX-ATLAS-B72,
no.87 stops being held-out if that job names clusters from the no.87 sheet -- its eval figure then needs another Birago 1572 item.

## Rules for every account (effective 3 Oct 2026)

- A transcription job reports `err_true` (with the benchmark item used) or says "err_true not measurable: no benchmark
  item of this hand/key", plus `err_2reader`. Power controls use err_true when it exists, else err_2reader -- never a
  look-alike residual.
- A symbol cipher with siblings in the same key family is segmented into the family atlas before any line read; a
  brief that skips it says why.
- Person time goes through the sorter only, never blocking (CLAUDE.md Usage 6).
- Owner sorts are reused family-wide (owner, 5 Oct 2026: "point number four is really good"). Before any machine pass
  or new owner sorter session on a letter, apply every owner decision already made in its key family
  (`tools/sign_sorter_apply.py`, cluster-level) and use the owner-labelled tiles as the exemplar sheet for that hand.
  A brief that asks the owner to sort tiles of a family whose earlier owner decisions were not applied first is the
  brief's error. Each owner session's decisions are scored afterwards against BENCHMARK-TX where a benchmark item
  exists ("my work isn't gospel", owner, 5 Oct 2026): owner labels are one strong reader, not ground truth.
- New capability goes into the shared tools above (Usage 8), never a private script in a target folder.

## Build plan (3 Oct 2026, account-3 orchestrator; jobs in WORK-QUEUE.tsv)

| Job | What | Done when |
|---|---|---|
| TX-BENCH | BENCHMARK-TX.tsv + tools/tx_bench.py + test; score the current line-read pipeline | err_true per item, held-out, in this file |
| TX-ATLAS-B72 | One atlas for every Birago 1572 letter (nos.71-90, f.117) with glyph_atlas; clusters named from the no.87 clerk sheet; top-k classify | err_true on no.87 held-out vs line reads |
| TX-DECODE | tools/key_decode_lattice.py: key-constrained decode over top-k, controls built in | f.117/f.144/f.168 re-tested; known-answer check on no.87 |
| TX-SORTER | sorter ranks tiles by value, decisions propagate per cluster across the family | one Birago session of <=20 tiles moves a letter's test |
| TX-VIEWS | multi-view voting: iiif_lines --views + reconcile over N passes with vote share and error correlation (research/TRANSCRIPTION-PRACTICE-2026-10-04.md #1, owner approved 4 Oct) | no.87 paired fixed > broken vs current 2-pass reconcile; built 4 Oct (`iiif_lines.py --views`, `reconcile_passes.py --vote --err-truth`, `tx_bench.py --paired`); pilot FAILed (fixed 0 / broken 6), see row 1 |
| TX-AGREEAUDIT | lookalike_pass audit of signs both readers agreed on, 5% planted-error control (research #2) | catches >= 80% planted; flags known agreed-but-wrong no.87 signs  **Today (4 Oct 2026, TX-AGREEAUDIT): `lookalike_pass.py audit`/`audit-score` built; on no.87 the planted control caught 7/10 firmly (0.70 < 0.80) = NON-TEST; target side 2/26 agreed-wrong flagged, 0/158 false flags, fixed 2 / broken 0 (p 0.25), err_true 0.053 -> 0.051; not adopted (benchmark-tx/outputs/birago1572-no87/agreeaudit/RESULTS.md)** |
| TX-ALTS | a/b? alternatives kept into the decode lattice, reconcile --keep-alts (research #3) | truth-in-lattice above 27/97 on no.87; lattice err_true paired gain  **Ran 4 Oct 2026: not adopted** -- tool options built (`--keep-alts` on key_decode_lattice from-passes and reconcile_passes); no.87 existing passes 27/97 unchanged; new a/b? pass on f178r+f179r: truth in lattice 12/35 (gate 50%), lam 4 paired 0 fixed / 0 broken (NOTES.md "TX-ALTS") |
| TX-SHEET | per-hand exemplar sheet (palaeographer's alphabet): `glyph_atlas.py atlas --from-truth --per 6 --spread --exclude-leaf` (research #4) | pass A + sheet below 0.069, paired fixed > broken, d<-T98 and s<-T50 down  **Today (4 Oct 2026, TX-SHEET): FAIL, not adopted** -- sheet from 636 S-grade secure tiles on 11 non-no.87 leaves (atlas/sheet_truth/); one blind Sonnet pass on no.87: err_true 0.077 vs A 0.069, paired fixed 16 / broken 22 (p 0.42); d<-T98 7->2 but s<-T50 7->15 (the hand's T50 tiles pull the off-sheet curled Ce into T50); about USD 0.74 per 100 signs job-level (benchmark-tx/txsheet/RESULTS.md) |
| TX-FABLE | swap the reader model: one blind Fable (`claude-fable-5-1`) pass per BENCHMARK-TX item, same crops/sheet/pass-A prompt (owner, 4 Oct) | pooled paired fixed > broken p<0.05 vs better Sonnet single pass AND err_true lower on no.87 + 3 of 4 dev  **Today (4 Oct 2026, TX-FABLE): FAIL, worse** -- no.87 0.093 vs A 0.069 (fixed 23 / broken 42, p 0.025); dint 0.271 vs 0.188; f21v 0.058 vs 0.048; f87 0.295 vs 0.043; f36v 0.500 vs 0.312; pooled fixed 40 / broken 95 (p 2.5e-6, wrong way); lower on 0 of 5; ~USD 1.0/100 signs vs Sonnet ~0.74 (benchmark-tx/txfable/RESULTS.md) |

Results land here (the "Today" column) as they come.
