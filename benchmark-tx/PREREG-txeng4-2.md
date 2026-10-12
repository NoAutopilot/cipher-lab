# PREREG TXE4-2 DINT-PIC (account 3, Fable 5.1 worker, session_01MB4qh15ETboWcbSJxybVRL, 12 Oct 2026 01:2x UTC by date -u; pushed BEFORE any read or score)

One of ten TXE4 experiments the account-3 parent launched on 12 Oct 2026 (brief `.claude/briefs/runs/2026-10-11-acct3-txe4-2.md`,
commit 93b7bb321 or later; prerequisite TXE4-0 REPAIR landed at 6f84c5af). Question: on the Dinteville 1592 hand (fr.3621), the
worst-read hand in BENCHMARK-TX and one whose reader briefs give the alphabet only as about 27 word labels, does a PICTURE of each
label -- tiles cut by the machine from f.130r, a different letter in the same hand, joined to the blind passes' agreed positions
through tools/box_token_align.py -- make blind Sonnet readers of f.128r make fewer edits than the same readers given today's words-only
list, and does a shuffled picture (the same tiles under the wrong labels) fail to give the same gain?
Rules: the brief's common TXE4 rules R1-R10 bind. Readers blind (brief text + crops [+ sheet]; no key, no truth, no other pass, no
repository path); every reader output committed with its sha256 BEFORE any score (benchmark-tx/txeng4/2/SHA256SUMS.prescore); no
*.truth.tsv opened by anything but tools/tx_bench.py; the frozen confirm items never opened; nothing published, nobody contacted.
The f.128r truth (benchmark-tx/dint-f128-print.truth.tsv) is a scorer input only. No f.128 tile enters any sheet. No f.130 reading
product (f130/ciphertext.tsv, tokens.tsv, key_dk.tsv, reading*.txt, the words/ and repair/ folders) is opened: the tile pipeline
reads only f130/passA.tsv, f130/passB.tsv, the f130 crops and dint128_label_map.tsv.

## Hypothesis
H1: a pictured alphabet cut from the hand (arm P) lowers the readers' unit-cost edits on dint-f128-print below the words-only brief
(arm T) by the registered gate, and the shuffled picture (arm S) does not: the gain comes from the CONTENT of the tiles (right sign
under right label), not from the presence of a picture.
H0 (a result): no gate-sized gap between T and P, or S matches P (pictures ignored), or S is no worse than P while P beats T
(any picture helps, content irrelevant) -- each a different null, each reported as such.
Direction: this is the first IMPROVEMENT-direction test of the sheet-form effect (TXE3-8 and SHEET-VIV ran in the degradation
direction, on hands that already had a picture); the Dinteville hand never had one.

## Nearest prior (register rows) and what differs from them
- TXE3-8 SHEET (benchmark-tx/txeng3/8/RESULTS.md, VERIFY.md; SHEET-H2 half run, no gate): Birago no.87, the drawn key sheet
  (51 cells) against the same cells as a text list: 15 vs 67 edits of 343 as measured (10 vs 62 flagged-excluded), one run per arm.
  Differs: that sheet was the CLERK'S OWN DRAWINGS; here the picture is machine-cut tiles of the hand from a sibling letter, joined
  by a verified box-to-token map; Sonnet readers, two passes per arm, a third arm (S) that keeps the picture and breaks its content;
  the direction is improvement over the existing brief, not degradation of an existing sheet.
- SHEET-VIV and SHEET-VIV-C (benchmark-tx/txeng2/sheetviv/RESULTS.md, sheetvivc/RESULTS.md; dev-FAIL at the line level, edits
  58 for the drawn sheet vs 86 / 80 for the text list): same degradation direction on Vivonne; differs as above.
- TX-SHEET (TRANSCRIPTION.md line 176; benchmark-tx/txsheet/RESULTS.md; dev-FAIL): glyph_atlas atlas --from-truth --per 6 on no.87
  from 636 S-grade tiles of 11 sibling leaves: 0.077 vs pass A 0.069, fixed 16 / broken 22. Differs: TX-SHEET added a tile sheet to
  a brief that ALREADY carried the clerk's drawn sheet (no headroom on the picture axis); here the baseline brief has no picture
  at all, and the tiles are placed by the label-aware aligner with a bounded shift check (TX-SHEET's tiles came from a truth
  alignment, not a blind-pass join). k = 4 here, 6 there.
- TXE-S (register row O8, retired; RETIRED.tsv row 212 'high-resolution sibling leaves as the reference sheet (full-pass form)'):
  sibling-leaf secure tiles as 3 of each code's 4 library tiles in the exemplar COMPARE layout, fixed 0 / broken 7, p 0.016; the
  compare family is retired. This job reopens O8 (TXE-S) on new material and with a different instrument: new material,
  because the Dinteville hand never had any tile sheet and its brief is words-only (TXE-S and TX-SHEET added tiles to a hand that
  had a drawn key); a different instrument, because there is NO compare layout here (the retired form), the whole inventory is
  shown ONCE as one sheet that stands beside the brief, every label row keeps its words, and the tiles are placed by
  box_token_align with the join gate rather than by a truth alignment. The retired compare layout itself is not run (R4).
- X11 (research/TX-REGISTER.tsv row 129, queued: 'a grown sheet for an unseen hand, Dinteville named', folded into X1 and never
  run) and X1 (dev-FAIL, its read-free detector 0/21): X11 is the idea this job finally runs; X1's detector is not used.
- Dinteville baselines (BENCHMARK-TX.tsv dint-f128-print; benchmark-tx/PREREG-dint128.md): the two blind Sonnet passes of 3 Oct
  (A2-DIN) are the beside-only baseline (err_true 0.353 / 0.306 raw, 0.247 / 0.188 mapped on file; re-derived in step 1 below).
- TXE4-9 CALIB (benchmark-tx/txeng4/9/RESULTS.md, 12 Oct 2026, not distinguishable) ran on the fr.3619 1591 office hand
  (dint-f89-gloss), not this item; it is cited only for the Sonnet-reader error shape on a Dinteville hand (edit mass in
  insertions, 14-31 of 33-47) which a sheet may or may not reach -- reported beside, never pooled.
Retired instruments named in R4 (':' mark rule, transcribe-and-decode crossword, look-alike pass as accuracy, the exemplar compare
layout, M24 feature-first, err_2reader as predictor of err_true) are not used; tools/gloss_cut.py is not used, since R3b retired it on
this layout and this job brings no new material and no different instrument for it. Forbidden joins (R4a: atlas/no87_box_token.tsv, txeng3/7/f152r_box_token.tsv, txeng/compare and pair box_pos.tsv,
the width-DP copies) are not touched; no owner evidence of any kind (sorter pages, settled labels, owner piles, L74 answers) is an
input.

## Fixed inputs (frozen now; nothing below changes after a number is seen)
- Item: dint-f128-print (dev; 85 scored of 183 positions; no flags file -> --exclude-flagged gives the identical mask). Crops:
  ciphers/fr3621-dinteville-1592/images/f128_L0{2,3,4,5}_s{1,2}.jpg (8 files, 2400 px wide), copied to each reader's scratch dir.
- Baseline reader brief T: ciphers/fr3621-dinteville-1592/f128/pass_instructions.md VERBATIM (the A2-DIN brief of 3 Oct 2026).
- Tile source: f.130r only -- ciphers/fr3621-dinteville-1592/images/f130_L??_s?.jpg (1760 px wide, 2-3 rows per crop, the line is
  the middle row), f130/passA.tsv and f130/passB.tsv (the two blind Sonnet passes of A2-DIN2), f130/pass_instructions.md for the
  segment geometry (s1 = x 0-1760, s2 = x 1600-3360 of the region, overlap 160 px). benchmark-tx/dint128_label_map.tsv maps the
  f.130 labels D -> 4, al -> a, zh -> m, div -> -:-, plus -> + before any use.
- Label inventory for the sheet rows: the 27 labels of the f.128 brief, with their word descriptions verbatim, in
  benchmark-tx/txeng4/2/row_text.tsv (committed with this PREREG). A f.130 token whose mapped label is not one of the 27 (r, h, n,
  B, primed forms other than 0', NEW:..., ?) is kept as a token for the alignment but never labels a tile row.
- Qualifying f.130 segments (rule 2b, read-free, decided from the passes' CLEAR: tokens): a (line, segment) qualifies when NEITHER
  pass has a CLEAR: token in it. By that rule: L02 s1; L04 s2; L05 s1; L07 s1, s2; L08 s1, s2; L09 s1, s2; L10 s1, s2; L11 s1 (12
  segments). L01 s2 has no CLEAR: token but is excluded because the f130 brief says its cipher tail is 'partly cut at the crop
  top', so the middle-row rule cannot pick its line (declared here, before any segmentation). Excluded for CLEAR: L02 s2, L03 s1,
  L03 s2, L04 s1, L05 s2, L06 s2 (one pass has CLEAR:dy), L11 s2.
- Segmentation: glyph_atlas.py segment, default (connected-component) mode, one page per crop (page name = the crop stem), with
  --median-h pool over the 12 qualifying crops (R9-FLOR: a speck-dominated crop must not collapse its own median). Middle row: the
  smoothed row-ink profile's peak nearest the crop's vertical centre; a box is kept when its vertical centre lies within 0.9 x the
  pooled median sign height of that peak. Overlap dedupe (the TXE3-6 / OL1-BOXES rule): a box whose centre x is in the right 80 px
  of s1 or the left 80 px of s2 is dropped (the 160 px overlap cut at its midpoint); s2 x is offset by +1600 to the line's own
  coordinate. Only signs.tsv boxes are tiles; marks.tsv (dots, ticks above) are never tiles.
- Line reads for the join: per line, the qualifying segments' tokens of pass A in order (s1 then s2), labels mapped; pass B aligned
  to pass A per line by tools/reconcile_passes.py --method nw on wide-format files (line id, signs); --read-alt = pass B's label at
  each aligned pass-A position; KEEP.tsv = the pass-A positions where A and B carry the same mapped label (agreed positions). A
  line is one read line f130_Lnn whether one or two of its segments qualify.
- Round 1 (seed only): box_token_align --lam 0 (no labels) --keep-pos KEEP.tsv --count-tol 0.10: a line whose kept box count
  differs from its token count by more than 10% is skipped and listed; the kept 1:1 rows at agreed positions give R1 tokens
  (sid, label).
- Round 2: glyph_atlas.py classify --train-labels R1 --only-train-labels --page all --knn 5 --topk 3 (the kNN votes are the R1
  tokens; the box itself never votes for itself, the tool's own rule), then box_token_align --topk CLASSIFY.tsv --lam 1.5
  --neutral 0.5 (the tool's defaults), --loo (default on), --keep-pos KEEP.tsv --count-tol 0.10. A tile is kept when it is op 1:1
  at the SAME position in round 1 and round 2 (an 'unsure' leave-one-out row is not 1:1). Round 1 only seeds round 2.
- Shift check (R4a, step 2e2), read-free: check labels = each box's kNN top-1 (k1) written as a separate sid,label file. Because
  those labels also steered the map (through --topk), the BINDING verdict is `tools/join_check.py --map R2.tsv --check-labels k1.tsv
  --read <line reads> --steered` (the leave-one-out row); box_token_align's own --check-bound in-sample row and its printed
  'check' rows are pasted beside it. Bound = TXE4-0's (join_check B1-B3, draws 20, seed 20261012). On FAIL: drop the failing lines
  (listed), re-check ONCE; still FAIL -> non-test. UNCHECKABLE -> non-test ('f.130 tiles not verifiably placed').
- Purity gate (step 2f), three parts, all required before P and S are built: (i) among the labelled boxes at kept positions in
  round 2, the share with op 1:1 >= 0.80; (ii) at least 15 of the 27 labels have >= 2 kept tiles; (iii) the shift check PASSes.
- Fill rule (step 2g), registered now, used only if (ii) fails: tiles from the fr.3619 1591 office hand (crops under
  benchmark-tx/txeng2/dint-f89-gloss/crops/, dint-f98v-gloss/crops/read/, dint-f113-gloss/crops/; the committed blind Opus passes
  benchmark-tx/outputs/dint-f{89,98v,113}-gloss/passA.tsv and passB.tsv) fill ONLY the labels with fewer than 2 f.130 tiles, by
  the same two-round recipe with their own pasted shift check under the same bound; every fill tile's source is recorded and P is
  reported as 'mixed-hand fill'. If (ii) still fails after the fill, P and S do not run (non-test).
- Sheets: P = glyph_atlas.py atlas --from-tokens TILES.tsv --row-text row_text.tsv --codes @labels27 --per 4 --spread --trim 0.2
  --min-secure 2 --cell 96 --rows-per-sheet 27 (one image: the whole inventory once; a label with fewer than 2 tiles shows its
  label and words with no tiles; the tool's own tile resample, cubic at up to 3x, nothing tuned). S = the same command with
  --shuffle-rows 20261011: a seeded derangement of the hand tiles across the rows that have tiles; labels and words stay in place.
  The two sheets, TILES.tsv, the maps, the classify output and their sha256 are committed before any read.
- Briefs: T = pass_instructions.md verbatim. P and S = the same text plus ONE sentence, placed as its own line directly after the
  'Overbars or dots ...' line: "The sheet shows, for each label, up to four examples of that sign cut from another letter in the
  same hand." plus the sheet's file name in the task wrapper's file list. The diff T -> P/S is committed. The task wrapper (same for
  all arms but the sheet line) names the scratch dir, the 8 crops, the output file and 'read only the files listed here'.
- Tool options (brief TOOL CHANGE a-c): box_token_align.py --keep-pos / --tokens-out / --count-tol; glyph_atlas.py atlas
  --from-tokens / --shuffle-rows / --row-text. R7: tools/box_token_align.py carries a commit from another TXE4 session within the
  hour (6f84c5af, TXE4-0) and TXE4-1 is briefed to land (a) and (b) concurrently, so this job keeps both changes as
  benchmark-tx/txeng4/2/box_token_align.py.patch and glyph_atlas.py.patch with offline tests, applies them to scratch copies for its
  runs, and names the patches in ROOM; if TXE4-1's versions land first, theirs are used and said so.
- Normaliser: benchmark-tx/build_dint128.py's pass normaliser (drop CLEAR: rows, join each line's non-'-' signs in order, prefix
  f128_, renumber) is an inline loop of build() that also opens the alignment files, so benchmark-tx/txeng4/2/norm.py imports
  build_dint128.rd and repeats that loop only; step 1 checks it is byte-identical to the committed outputs on the committed passes
  before it is used on any new pass.

## Arms
- T (control, today's brief): 8 crops + pass_instructions.md verbatim.
- P (picture): 8 crops + sheet_P.png + the brief with the one sentence.
- S (shuffled picture): 8 crops + sheet_S.png + the identical brief and sentence.
Two passes per arm (round 1: T1 P1 S1; round 2: T2 P2 S2); each pass = ONE Sonnet (claude-sonnet-5) subagent call in a fresh
context over the 8 crops (+ sheet), scratch copies only, no repository path. Launch order: random.Random(20261011).shuffle(['T1','P1',
'S1']) gives the round-1 order; round 2 uses the same permutation on ['T2','P2','S2']. The three calls of a round are launched in
that order in one message and run concurrently (fresh contexts, so order cannot leak content).

## Endpoint
PRIMARY: each arm's mean over its 2 passes of the unit-cost edit total (S+D+I, tools/tx_bench.py's standard-SER numerator
`ser_errors`) on the 85 scored positions, value level, WITH --label-map benchmark-tx/dint128_label_map.tsv (mapped), from
`tools/tx_bench.py <norm.tsv> --bench BENCHMARK-TX.tsv --item dint-f128-print --coverage-diagnostic --strict --ci --label-map
benchmark-tx/dint128_label_map.tsv` run ONCE per output by the committed score.py. Beside: the raw (unmapped) run; --exclude-flagged
(identical mask, stated); err_true (0.75-indel) with Wilson 95%; --strict; S/D/I; position McNemar P vs T and P vs S per pass
(--paired, T or S as BASE); edits per label for labels with and without tiles (from the per-value confusion output); agreement
per arm (pass-to-pass unit-cost edit distance of the two normalised passes, difflib).

## Gate (the brief's, word for word)
Registered: P is adopted for word-list hands if mean(T) >= 1.25 x mean(P), AND mean(T) - mean(P) > the maximum within-arm pass
spread, AND mean(S) >= mean(P) + that spread. Otherwise the result is 'not distinguishable'.
Operational definitions, fixed now: means and spreads are mapped unit-cost edits; "within-arm pass spread" = |pass1 - pass2|
within T, within P and within S, the largest of the three; "that spread" in the third clause is the same maximum. A mean(S) below
mean(P) + spread with mean(T) >= 1.25 x mean(P) is reported as 'picture helps, content not shown' (a named null), still
'not distinguishable' for the gate. The gate is applied by score.py once.

## Control and why it can vary
T is today's brief in the same session with the same crops, model and layout; only the sheet differs, and the sheet acts on
matching (TXE3-8: 15 vs 67). S shows the same tiles under wrong labels: it can raise edits above P (misleading pictures) or match P
(pictures ignored) or sit between, so it separates the content of the picture from its presence; nothing in S's construction ties
its edit count to P's (separate calls, separate contexts, the same images, a deranged sheet). Declared limits: the gloss above
every f.128 line is the plaintext, visible in all arms, so the absolute level is an upper bound and the gate is per item, never
pooled (TX-RED F3); dev item of 85 positions; Sonnet readers; two passes per arm. No arm's signs come from a classifier (readers
score every arm), so no shuffled-label chance null is needed in the gate; the tile placement's own null is join_check's
within-page permutation (B2/B3).

## Units, order, cost and stop rule
U0 this PREREG + row_text.tsv + copied access_log.py/usage.py (done before any score). U1 step 1 baseline re-derivation and
normaliser check (5 min, no reader). U2 tool patches + offline tests (15 min). U3 f.130 segmentation, middle row, dedupe, line
reads, rounds 1-2, shift check, purity gate (15 min). U4 sheets P and S + briefs + sha256 commit (5 min). U5-U7 round-1 reads T1 P1
S1 (one Sonnet call each, about USD 0.35 and 6 min, concurrent). U8-U10 round-2 reads (same). U11 normalise, sha256, score once,
RESULTS, LEDGER, ROOM (15 min). Box 01:24-03:24 UTC (claim); no unit starts after 03:00 UTC. Running estimate = Fable floor USD
9.5 + 0.35 per reader call done + 0.5 for U2-U4 together: six calls reach 12.1 (the parent's line is 12; the sixth call is
started only if the clock is also under the line, else round 2 runs T2 and P2 only -- declared below). A call still running at a
line finishes; nothing new starts.
Declared reading by units done: purity gate or shift check failed -> non-test ('f.130 tiles not verifiably placed' or 'fewer than
15 labels pictured'), T reads not run, the tile numbers reported. Round 1 only (3 calls): numbers per arm for one pass; the gate
needs two passes and is reported as 'not distinguishable (one pass)'. Round 2 with T2 and P2 only: the T/P clauses on two passes,
the S clause on one pass, reported as 'S unreplicated'. All six: the gate above, word for word. A null is a result.

## What is NOT done
No truth file read by eye or by a tested arm; the f.128 truth opened only by tx_bench. No change to BENCHMARK-TX.tsv or any truth
or flag. No tuning after a score. No eval item (birago1572-no87, birago1572-f152r, gunther8246-p2, bir1591-f23r-gloss) is scored:
LOOKS.tsv gets no row from this job. No confirm item, no sorter page, no owner evidence. No f.130 reading product opened. Nothing
published. No follow-up (the next step is named in RESULTS with its cost, not run).

## Addendum (12 Oct 2026 01:5x UTC by date -u; read-free tile pipeline run; no reader call made, no score of any new output)
- PREREG pushed 908527f4 (01:29 UTC); baseline re-derivation (step 1, committed outputs only, scored by score.py): pass A mapped
  21/85 edits (err_true 0.247, S 13 D 2 I 6; raw 30/85 = 0.353), pass B mapped 16/85 (0.188, S 11 D 0 I 5; raw 26/85 = 0.306):
  the figures on file reproduce. norm.py is byte-identical to the committed outputs on both committed passes.
- Deviation, declared before any join or score: with --median-h pool (31.0 px over the 12 crops) glyph_atlas segment returned 0
  signs for f130_L02_s1 (its two rows are 84 px apart; the tool's line finder sets a minimum peak distance of 0.7 x 4 x mh = 86 px
  at 31 px and drops both), so that one crop was segmented alone at its own median (29 px, inside the pool's 28-35 range) and its
  rows merged into tiles/atlas; the other 11 crops are the pooled run. Read-free, before any number of the gate was seen.
- Line reads (tiles/reads/, --method nw --keep-dots): 419 pass-A tokens, 50 pass-B alternatives, 358 agreed positions.
- Round 1 (--lam 0, --count-tol 0.10): lines f130_L02 (32 boxes vs 37 tokens), L09 (60 vs 68) and L10 (61 vs 70) skipped by the
  count tolerance; 5 lines aligned; 178 1:1 boxes at agreed positions seed the kNN (21 labels).
- Round 2 (--topk from classify --only-train-labels on the round-1 tokens, --loo): 250 rows, ops 1:1 157, unsure 25, 1:2 56, 2:1 12.
- Shift check (R4a), pasted from tiles/r2_check_console.txt and tiles/r2_joincheck_steered.txt:
    tokens-out: 131 1:1 boxes at 358 agreed positions -> benchmark-tx/txeng4/2/tiles/r2_tokens.tsv
    check, new map, all its one-token tiles: n 182: at 0 76, -1 3, +1 7, +-2 16, none 80
    check, new map leave-one-out (own label hidden): n 178: at 0 53, -1 12, +1 14, +-2 19, none 80
    join_check --check-bound: PASS (steered=False) share0=0.418 (null p95 0.100) share+-1=0.055 (bound 0.170) -> benchmark-tx/txeng4/2/tiles/r2_map.tsv.joincheck.json
    join_check.py --steered (BINDING: the k1 labels steered the map through --topk):
    join_check: PASS n=178 share0=0.298 (null p95 0.084) share+-1=0.146 (bound 0.182) -> benchmark-tx/txeng4/2/tiles/r2_map.tsv.joincheck.json
      f130_L04: pass placed=23 {'none': 17, '0': 3, '+1': 2, '+-2': 1}
      f130_L05: pass placed=27 {'+1': 2, '0': 9, 'none': 11, '-1': 2, '+-2': 3}
      f130_L07: pass placed=50 {'0': 19, 'none': 20, '-1': 4, '+1': 2, '+-2': 5}
      f130_L08: pass placed=49 {'+-2': 7, '-1': 4, 'none': 20, '0': 11, '+1': 7}
      f130_L11: pass placed=29 {'none': 12, '0': 11, '-1': 2, '+-2': 3, '+1': 1}
  Verdict: PASS on the leave-one-out row (share at 0 0.298 vs null p95 0.084; share at +-1 0.146 under the bound 0.182; B1 holds on
  all five placed lines). The in-sample row also PASSes (0.418 vs 0.100; 0.055 under 0.170). No line dropped, no re-check needed.
- Purity gate (tiles/purity_console.txt): (i) share of 1:1 among the 216 boxes at agreed positions in round 2 = 131/216 = 0.606,
  FAIL at 0.80 (1:2 51, 2:1 10, unsure 24); (ii) tiles 1:1 at the same position in both rounds 34, labels with >= 2 tiles 9 of 27
  (#, 1, 0, a, f, y, m, v, sq), FAIL at 15; (iii) shift check PASS. Gate FAIL on (i) and (ii).
- Declared reading applied: NON-TEST, "f.130 tiles not verifiably placed" on part (i) (a box-count mismatch, not a shift: 61 of the
  216 boxes at agreed positions cover two tokens or share one, i.e. the default connected-component segmentation joins or splits
  this cursive hand's signs) and "fewer than 15 labels pictured" on part (ii). The fill rule (step 2g) covers only part (ii) and
  cannot repair part (i), so it is not run. P and S are not built; T is not read; LOOKS.tsv gets no row; no reader cost is spent.
