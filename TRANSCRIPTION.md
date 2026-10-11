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
| 1 | True per-sign error, measured against a known answer | <= 5% on symbol ciphers, <= 1% on digits | BENCHMARK-TX.tsv + `tools/tx_bench.py` (TX-BENCH, 3 Oct 2026). Held-out (eval) Birago no.87, 803 scored signs: single blind pass A 0.069 (0.053-0.088), pass B 0.100 (0.081-0.122), reconciled 0.053 (0.040-0.071), reconciled + NO87-LABELS relabels 0.045 (0.033-0.061); per leaf the reconciled read is 0.083 f.178r, 0.055 f.178v, 0.013 f.179r. Dev: f.36v gloss line 0.31-0.44 on 16 signs; Ceppo f.21v/f.87 single passes 0.04-0.13 on S spans. Value-level lower bounds (see Benchmark); TXB2 (3 Oct 2026), dev item dint-f128-print (fr.3621 f.128r, Dinteville 1592 hand, 85 scored / 98 excluded, truth = 1882 print through key_print agree==n>=2; reconciled read is the reference, not scored): blind Sonnet pass A 0.353 (0.260-0.459) raw / 0.247 (0.168-0.348) with --label-map; pass B 0.306 (0.218-0.410) raw / 0.188 (0.119-0.284) mapped -- a symbol hand far above the 5% target; the raw-vs-mapped gap is label inventory (D/al/zh split after the passes), not glyph error; fr3416 f.38, fr4715 f.38v, fr3993 ff.71-72 not built (one raw pass or no raw passes on disk); TX-VIEWS (4 Oct 2026, f.178r+f.179r of no.87, 164 signs, pre-registered pilot): three blind Sonnet view reads (pad 0.165, s125 0.159, warp 0.140) + A + B voted 5 ways = 0.085, identical to pass A; vs the current reconcile (passC 0.049) paired fixed 0 / broken 6, p = 0.031 -- FAIL, not adopted; 7 of the 6+8 errors are an f.178r L03 tail the fixed-band crop cuts off for every reader, and the views repeat 13-14 of A's 14 errors (phi with A 0.71-0.76), benchmark-tx/tx-views-2026-10-04.md **Today (9 Oct 2026, TX-TRUTH-VERIFY): no.87 pass L as measured 0.042 (34/803, after 2 image-backed truth corrections), flagged excluded 0.029 (23/792); floor 18/803 as measured, 7/792 flagged excluded; table below the targets.** **Today (9 Oct 2026 22:22 UTC, TX-ENGINEER-2 S2 look, product baseline on an UNSEEN hand): vivonne1573-f103r-confirm2 (Saint-Gouard clerk hand 1573, 1,068 scored): the frozen pipeline (two blind Opus passes + reconcile + packet adjudication) as measured 0.296 (316/1068), flagged-excluded 0.150 (75/500; flags from the two blind clerk reads, not the clerk image); single S2 passes 0.148/0.154; the builder's own earlier passes 0.048/0.074 beside; S2-NOTE found no notation effect (notation 0 / segmentation 42 / read 33 of the 75); the two figures are two scores under two masks, not bounds (outside review 10 Oct, research/SO-TX-TRANSCRIPTION-2026-10-10.md); corrected audit with the fixed scorer (10 Oct 01:12 UTC, benchmark-tx/txeng2/scorerfix/RESULTS.md): 0.150 / 0.296 reproduced, standard unit-cost SER 0.134 (S 37 D 19 I 11) / 0.288 beside, lines missing 0, line-level paired vs committed 0 improved / 23 worsened (the cannot-differ shape); value-level throughout; SCAN-103 found the truth's alignment NOT BEST by 155 letters (fair margin 0.0267 vs 0.03) and a re-anchored second truth (RE103, item -s6500) is being built, the frozen readings to be scored once against it and reported here beside, never replacing, the look (benchmark-tx/txeng2/s2score/).** **Update 10 Oct 02:5x UTC (lane incarnation 5; TX-RED F70): RE103 stopped at its own control tolerance (the 6500 alignment is the registered one to within 26 letters); no second truth, no re-score; the record stands on CA-S2. A witness-revised mask (item -w: 84 clerk-split flags confirmed by Groen van Prinsterer IV's independent print, TXV-GROEN) re-scores the same frozen passZ_S2b at 0.141 (81/576) flagged-excluded beside the record 0.150 (75/500); 0.296 unchanged; a corrected audit, never a second look (PREREG-txeng2-21).** **Today (11 Oct 2026, TXE3-3 CROSSHAND, a second hand): the no.87 two-pass Sonnet recipe on gunther8246-p2 L01-L17 (Willem van Oranje's German secretary, 1561; 17 of the page's 25 lines) reads 0.065 (14/214, 0.039-0.107) as measured, 0.034 (7/206) flagged-excluded: the registered gate (<= 0.050 as measured) FAILs on the point estimate, but the result cannot be told apart from 5% or from the same-session no.87 control (0.043, 11/253; Fisher p 0.31, about 15% power), so whether 5% carries over to this hand is undecided; the no.87 figure it replicates is itself 0.051 (41/803) as measured (benchmark-tx/txeng3/3/RESULTS.md, VERIFY.md).** |
| 2 | Every transcription reports its error with the method named | always: `err_true` (benchmark-calibrated) or `err_2reader`, never "agreement" alone | mixed |
| 3 | Signs are image tiles in one atlas per key family, not strings typed per letter | every symbol cipher | Birago 1572 family atlas built (TX-ATLAS-B72, 3 Oct 2026: 18 pages, 4,209 tiles, ciphers/nevers-birago-fr3251-1572/atlas/); on no.87 held-out the atlas top-1 reads err_true 0.162 (tx_bench, 61/376) vs line reads 0.040 on the same lines -- an atlas of connected components does not yet replace line reads on this hand **Today (11 Oct 2026, BOXMAP-RESCORE, ciphers/nevers-birago-fr3251-1572/atlas/RESCORE.md): the width-only box-to-token map (atlas/no87_box_token.tsv) put tiles one token off on 10 of 26 no.87 lines; joined through the label-aware map (tools/box_token_align.py, ed5d42162) the atlas top-1 reads 0.103 against line reads 0.059 on the same 370 joined held-out signs (sorter-only map 0.108; the old join gave 0.322 against 0.056 on 376). The map-free tx_bench figure above, 0.162 (61/376), is unchanged, so the atlas still does not replace line reads. Atlas-alone in the TX-DECODE lattice 0.191, was 0.392 (harvest/tx_decode/RESCORE.md); atlas clusters 94.6% majority-pure, 63 of 86 pure, was 77.3%, 31 of 92 (benchmark-tx/txeng2/sorter/RESCORE.md).** |
| 4 | Each sign carries top-k candidates with confidences | k=3 | `glyph_atlas.py classify --topk 3` (TX-ATLAS-B72): per-letter k1-k3 with distance and vote share in ciphers/nevers-birago-fr3251-1572/atlas/topk/; truth outside the atlas top-3 on 0.078 of no.87 held-out signs (370 joined through the label-aware map; sorter-only map 0.086; first recorded as 0.261 through the width-only map, one token off on 10 of 26 lines: ciphers/nevers-birago-fr3251-1572/atlas/RESCORE.md, 11 Oct 2026) |
| 5 | Ambiguity is settled with the key and the language in the loop, and reported as such (grade S, never H) | key-constrained decode over the candidate lattice | tools/key_decode_lattice.py (TX-DECODE, 3 Oct): on two-pass lattices no.87 err_true 0.081 -> 0.100 at the pre-registered lam 1 (fails) and 0.071 at lam 4 (tuned; held-out gain ~2 tokens). Only 27/97 errors have the truth in the lattice. TX-ALTS (4 Oct): `--keep-alts` + an a/b? pass rule did not raise it enough (f178r+f179r 12/35 vs gate 50%; lam 4 0 fixed / 0 broken): not adopted, though the a/b? reader put the truth in its own alternatives at 12 of its 29 errors (old pass A 0/18). At lam 4, f.144r / f.168 / f.117r go from rank 22 / 20 / 10 to 1/201 (z 3.10 / 2.77 / 3.66); shuffled-target control fails (z <= 1.91). Not readings |
| 6 | A person's decision on one tile propagates to every tile of that cluster in every letter of the key family | always | built 3 Oct (TX-SORTER): one move offers "apply to all N in this cluster"; `sign_sorter_apply.py --atlas-labels` writes it to the family atlas labels.json; waits on TX-ATLAS-B72's atlas for a real (not provisional) cluster run |
| 7 | The sorter asks the person only the tiles whose answer moves the reading most, about 10-20 per session | "Check these first": tiles where pass A and pass B disagree first, in reading order (TXE3-1, 11 Oct 2026), ahead of the --rank-lattice (expected change in key rank / judge score) and classifier-margin rankings | built 3 Oct (TX-SORTER): `--rank-lattice` scores each tile as reader weight on the runner-up x decode letters changed when forced (key_decode_lattice.py); Birago 1572 demo: 20 of 211 tiles ranked, on the family atlas (no.73, no.85, f.117: 458 tiles, 100 atlas clusters) the 20 ranked tiles reach 71 tiles through their clusters; 18 of the 20 are positions where the lattice decode overrode the top-1 label -- and TX-DECODE found the lam=1 decode raises err_true on no.87, so those overrides are questions for the person, not likely corrections **Today (11 Oct 2026, TXE3-1, benchmark-tx/txeng3/1/RESULTS.md, VERIFY.md, RESCORE.md): read-free simulation on no.87 eval_heldout, the benchmark truth playing the owner, pile propagation, k=20: asking the A/B disagreement tiles first leaves 6/376 wrong as measured (2/371 flagged-excluded) against a random 20-seed minimum of 7 (4), and reaches 2% in 10 questions as measured (2 flagged-excluded) against a random median of 93 (43). The registered gate (primary: pile, flagged-excluded, below the random minimum) is met by the disagreement order (2 against 4) and not by --rank-lattice or margin (4 each). It stood after the second check and after the box-map rescore; under whole-cluster propagation it is now the best of the three registered orders (k=20: 5 wrong flagged-excluded, 9 as measured, against lattice 8 (10) and margin 19 (24)), so the registered 'qualified: pile or per-tile only' caveat, which rested on the shifted map, is dropped from this order rule (how far a decision propagates is a separate open proposal below). Limits: the owner is simulated as an oracle, one leaf, and the lead over today's tx_doubt feed (a_doubt) is 6 vs 9 wrong as measured (2 vs 4), paired p 0.375-0.5, within chance; most of the gain is one five-tile d-read-as-s pile that the TXE3-10 d/s classifier also fixes. To build: the --focus list in this order (tools/sign_sorter.py shows focus.tsv as given and has no such builder today; named in the TXE4-0 brief's next steps).** |
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
t<-T90 x3, e<-T76 x3, l<-T64 x2. What this says: on the held-out item the reconciled line read is about 5% (passC 0.051, 41/803 as measured; L 0.042, 34/803) and two
readers' reconciliation roughly halves a single pass's error; the T98/T18 look-alike is now the largest remaining error source.
On a second hand (gunther8246-p2 L01-L17, TXE3-3, 11 Oct 2026) the same recipe read 0.065 (14/214) as measured and 0.034 (7/206)
flagged-excluded: a FAIL of the registered gate on the point estimate, not distinguishable from 5% or from the no.87 control run
beside it, so whether 5% carries over is undecided (row 1).
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
  look-alike residual. err_2reader is never reported as, or converted into, an err_true estimate: a power control that has
  only err_2reader states it as a split rate, not an error rate (TXE3-4 CALIB, 11 Oct 2026, registered NULL: across 13
  known-answer leaves in 7 hands err_2reader did not predict err_true -- Spearman 0.110, shuffle p 0.389; leave-one-out ratio
  MAE 0.090 against a constant's 0.087; per-leaf ratio err_true/err_2reader 0.14-5.39; benchmark-tx/txeng3/4/RESULTS.md,
  VERIFY.md).
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

## Open proposals (suggestive, 11 Oct 2026, not rules)

From the cross-experiment critic after the box-map fix (11 Oct 2026, 18:10 UTC; account-3 parent). None has a registered gate
behind it; each is a lead with its basis, and becomes a rule only through a parent, on a gated result. The licensed items of the
same pass are in rows 1, 3, 4, 7 and the first rule above.

- **"Check these first" build order.** Run the TXE3-10 d/s discriminator before building the disagreement list; after the disagreement tiles, continue with the rest of the tx_doubt feed; add TXE3-9's lattice near-tie list or the live no.87 kNN-margin-to-owner-piles focus only after each is simulated with tools/tx_sorter_curve.py on dev; before any further claim, re-simulate TXE3-1 on L plus X30's eval flips (dev first, read-free, about USD 1). Basis: the five-tile T98-for-T18 pile behind most of the disagreement order's gain is exactly X30's fixes (with them the eval base goes from 15/376 to 9/376 as measured, 10/371 to 4/371 flagged-excluded; the order has not been re-simulated on that base); the hybrid order is an unregistered exploratory run; the near-tie figure has no committed script; the margin order is at random level per tile (questions to 2% flagged-excluded: 52 before the rescore, 96 after).
- **Propagation (row 6, pipeline step 7).** A decision propagates to its pile (same atlas cluster and same current sign); cluster-wide only for a cluster shown value-pure on a shift-checked join. This replaces the first critic's "never whole-cluster", which rested on the map bug. Basis: label-aware rescores of TXE3-1 and X6 (benchmark-tx/txeng2/sorter/RESCORE.md): atlas 94.6% majority-pure; eval cluster propagation at k=20, disagree 5 and a_doubt 4 wrong against a base of 10, random mean 12.1, flagged-excluded (9, 9, 15, 16.6 as measured); on dev cluster propagation still ends above the base (disagree 21, random mean 16.7, against 14 flagged-excluded; 30, 22.4, against 19 as measured); pile is at least as good on every unit; no gate.
- **Join rule and 8a gate.** Every join of sorter tiles or atlas boxes to read positions is made with tools/box_token_align.py and passes its truth-free shift check (seed = read at offset 0 against -1/+1/+-2, against a stated bound) before anything is scored; a width-only DP is never used alone, and a KM-style permutation gate is never cited as proof that a map is right. Basis: the old map was one token off on 10 of 26 no.87 lines (seed = L at the mapped position 157/208 before, 188/203 after) and moved conclusions in TXE3-1, -2, -7, -9, -10, X6, X20, BIR87-ALIGN, MQS-SORTER A/B and the atlas naming; the MQS-SHEETS KM gate passed the shifted map (neighbour count 75 of 381 -> 3 of 373). TXE4-0 unit 1 (tools/join_check.py, designed 11 Oct, not launched) builds the gate and proposes the rule text.
- **Single-pass floor.** Where no err_true exists, report 0.5 x err_2reader as a rough single-pass floor only, and run power controls across about 0.5x to 2.6x err_2reader, not at err_2reader alone. Basis: TXE3-4, post hoc and unregistered: over whole lines the floor held on 8 of 13 leaves (all 5 misses are leaves whose truth was built from the same passes); the ratio's q10-q90 is 0.23-2.57; ties to rule 3 SALV-DIAG (bracket the measured error).
- **Adjudication on a new hand.** Keep two diverse blind readers; on a hand with no known-answer check of its own adjudicator, the disagreement rows go to the sorter, or to an adjudicator first calibrated on a known answer of that hand (or TXE4-6's page-agreed tiles), never to an uncalibrated blind Sonnet adjudicator. Basis: TXE3-3 second check, adjudicator right at 3 of 9 one-reader error events on gunther (2 of 7 substitutions) against 38/38 on no.87; a correct pick at every disagreement gives 0.037 (8/214) as measured, the reference transcription's own floor; in TXE3-8 the Opus twins agreed on 347/351 signs and were still wrong at 15/343.
- **Owner-decision scoring.** Only moved tiles count as owner decisions (kept tiles are machine seeds); a tile the owner split into a new one-tile pile (T60-d, T83-b) is scored as "not the parent family" or left unscored, never as the parent; owner decisions are scored only through a shift-checked join; "a kept tile must never be reused as a decision, it broke 28/33" is withdrawn by the rescore. Basis: TXE3-9 rescore (benchmark-tx/txeng3/9/RESCORE.md): kept seeds right at 166/168, kept-only pins 0 fixed / 1 broken (was 0/28); owner pins right at 16/19 with the decoder right at all 19, 2 of the 3 wrong pins being split-pile scorings; MQS-SORTER B owner family-pile tiles wrong at 1 of 175; no gate.
- **Owner sorts reused family-wide.** Add "propagated atlas-kNN labels never overwrite a line read automatically"; the first critic's "reuse is not an accuracy step" is dropped. Basis: TXE3-7 override arm after the rescore 0 fixed of 9 substitutions (A1 0/0, A2 0/4, p 0.125; the old 0/22 and 0/11 were mostly placement); atlas-mode gate still FAIL (41/33, p 0.42), but post hoc X_NEW-l = T19 gives 45/22, p 0.0067, and 62 of the 121 owner-vs-machine changes look like repairs of start labels attached one tile off, so the control is misjoined (TXE4-0 unit 3 re-attaches them).
- **Pictured alphabet.** A hand whose key survives as drawings is read against a pictured alphabet (the key drawing or machine-cut tiles of the hand), never a word-list description of the signs. Basis: TXE3-8 half run, one run per arm, one word list: 15 vs 67 of 343 as measured (10 vs 62 of 338 flagged-excluded), about three quarters of the excess on six signs; the picture is no better than the existing labels (fixed 4 / broken 7); the SHEET-H2 gate is unread; about 22,100 published Saint-Gouard signs rest on words-only alphabets (benchmark-tx/txeng3/SHEETFORM-SWEEP.md); TXE4-1 and TXE4-2 are designed to test it.
- **Box rules.** Keep the pen-unit default; do not treat the owner's L74 boxes as a measured accuracy step; route last-of-line boxes read '_' to the owner as a question, not an automatic filter; score any future box or unit test through line readers, or with a shuffled-label chance null inside its gate. Basis: TXE3-6 registered null (shuffled-label readers reproduce +0.084/+0.086 of the +0.091 gap); TXE3-5's gate PASSed against a size-matched control that was not position-matched; "drop each line's last box" scores 102, the same as the owner's full arm.
- **Process.** (a) A mechanical check that every flagged-excluded figure in an owner-facing paragraph has its as-measured partner; (b) before registering, tools/tx_power.py and a can-it-differ check on every gate clause and control; (c) any registered arm scored by a classifier carries a shuffled-label chance null in its gate (in the TXE4 briefs as rule R4a). Basis: "Never quote the flagged-excluded figure alone" (above) was broken in owner text by TXE3-1 ("7 vs 53") and TXE3-8 ("10 vs 62"); clauses or controls that could not discriminate in TXE3-1 (to-3% vacuous at a 2.7% base), TXE3-10 (passable only at 6/6), TXE3-7 (A3 null), TXE3-5 (size-matched control), TXE3-9 (gate unreachable) and TXE3-3 (rule (a) at about 15% power); TXE3-6's chance null reproduced its whole effect.
