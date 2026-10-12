# PREREG TXE4-1 VIV-HAND (account 3, Fable 5.1 worker, session_01GcMxkniJHMYkrLFu9JrsMf; 12 Oct 2026 01:3x UTC by date -u; pushed BEFORE any read or score)

One of ten TXE4 experiments the account-3 parent launched on 12 Oct 2026 (brief `.claude/briefs/runs/2026-10-11-acct3-txe4-1.md`,
commit 93b7bb321; prerequisite TXE4-0 REPAIR landed 6f84c5af7 with `tools/join_check.py`). Question: on the Saint-Gouard
1572-74 clerk hand (BnF fr.16105 f.102r, item vivonne1573-f102r-dev2, the 13 TXE3-6 test lines), does a Sonnet reader given
its alphabet as a PICTURE read better than one given the same alphabet in WORDS (the form the three published readings used),
and do the clerk's own strokes, cut by the machine from the sibling page f.102v with no truth and no person, add anything to
the key drawing? Rules: the brief's common TXE4 rules R1-R10 bind. Readers blind (task text + crops + the arm's sheet only, no
key, no truth, no other pass, no repository path); every reader output committed with its sha256 BEFORE any score
(benchmark-tx/txeng4/1/SHA256SUMS.prescore); no truth or flags file edited; the frozen confirm items never opened; nothing
published, nobody contacted. Truth and flags are opened only by tools/tx_bench.py.

## Hypothesis
H1 (G-DEFAULT): a pictured alphabet reads this hand better than the word list: the W arm's unit-cost edit total is at least
1.25x the H arm's as measured, and above it flagged-excluded, by more than the within-arm pass spread.
H1b (G-HAND): the clerk's own strokes add to the drawing: D (drawing only) makes at least 1.15x H's edits as measured, and
Hx (the same tiles in the wrong rows) does not read as well as H.
H0 (a result): the forms are not distinguishable from pass spread on these 13 lines, or the tiles cannot be built (non-test).

## Nearest prior (register rows) and what differs from them
- `SHEET-VIV` and `SHEET-VIV-C` (txeng2, dev-FAIL, TX-ENGINEER-2, 10 Oct 2026; Opus readers, the whole 36-line dev2 item):
  the drawn sheet `glyphs/sheet_tomokiyo_v1.png` made 58 unit-cost edits flagged-excluded on 679 positions against 86 and
  80 for the text list; as measured 302 vs 334 (+11%), line sign test p 0.26. This job differs in the reader (Sonnet), the
  scored set (TXE3-6's 13 test lines, 417 / 216 scored), the paired design (four arms in one session, two passes each) and
  in adding two arms that no prior run had: hand tiles cut by the machine from f.102v (H) and the same tiles deranged (Hx).
- `TXE3-8` (benchmark-tx/txeng3/8/RESULTS.md, VERIFY.md; SHEET-H2 half run on Birago no.87 dev_tune, Opus readers, one run
  per arm): the pictured 51-cell sheet made 15 edits as measured and 10 flagged-excluded; the same cells in words 67 and 62
  (4.5x as measured). The readers said the hand's strokes differ from the key-sheet exemplars; this job tests exactly that
  remark with hand tiles beside the drawing, on a second hand, with two passes per arm so the spread is measured.
- `TX-SHEET` (tx-build, dev-FAIL, 4 Oct 2026) used hand tiles as a REPLACEMENT sheet on no.87 and failed 16/22 because an
  off-sheet sign had no row. Here the drawn cell stays first in every one of the 40 rows (`--canonical-boxes`), so no row
  is lost; tiles are added, never substituted.
- `O8` is reopened here on new material (the f.102v blind consensus) and with a different instrument (a sheet with the
  drawn cell first, no compare layout), the retired row being RETIRED.tsv 212 (high-resolution sibling leaves as the
  reference sheet in full-pass form, TX-SHEET and the TXE-S compare layout), and this PREREG argues the reopening on three
  points. (1) New material: this hand has never had a sheet of its own strokes; the f.102v blind consensus (N5-VIVK
  passes A and B, 4 Oct 2026) is new material for a sheet, joined to boxes only through the corrected aligner
  `tools/box_token_align.py` (R4a). (2) A different instrument: there is no compare layout, no exemplar sits beside a
  doubtful tile, and the whole inventory is shown once, as a sheet; the rows are the key drawing's cells with up to four
  hand tiles after each. (3) The drawn cell stays first in every row, so the TX-SHEET failure mode (a sign with no row)
  cannot recur. The retired compare family (`TXE-S`, tx_compare.py library) is not run.
- `TXE3-6` (benchmark-tx/txeng3/6/RESULTS.md, VERIFY.md; null): the pen-unit segment recipe and the 13 test lines come from
  it; its verifier found the f.102r kNN barely above chance with shuffled labels, so this job's round-2 kNN carries the
  join gate's own permuted-label null (UNCHECKABLE is a declared non-test, R4a) and every arm is reader-scored, not
  classifier-scored.
Retired instruments named in R4 (the ':' mark rule, the transcribe-and-decode crossword, the look-alike pass as an accuracy
step, the exemplar compare layout, M24 feature-first, err_2reader as a predictor) are not used.

## Fixed inputs (frozen now; sha256 by `sha256sum` at 01:2x UTC)
- Item: vivonne1573-f102r-dev2, scored through `benchmark-tx/txeng3/6/bench_test.tsv` (5f3a2ac9...) against
  `benchmark-tx/txeng3/6/truth_test.tsv` (66dda383...; 13 test lines f102r_L02, L04, L08, L10, L16, L18, L20, L24, L28, L30,
  L32, L34, L36; expected 417 scored as measured, 216 flagged-excluded). Truth is opened by tx_bench only.
- Test crops (26): `ciphers/fr16104-vivonne-spain-1572/images/c105_f102r_L{02,04,08,10,16,18,20,24,28,30,32,34,36}_s{1,2}.jpg`
  (1600 x about 102 px, s1/s2 overlap 250 px as the SHEET-VIV task text states).
- Tile source (read-free, no truth): the 74 f.102v crops `images/c106_f102v_L01..L37_s{1,2}.jpg` with `images/manifest.json`
  (199f0d03...; s1/s2 overlap 220 px on every line by the manifest boxes); the two N5-VIVK blind passes `tx/f102v_passA.tsv`
  (0add9bf3...) and `tx/f102v_passB.tsv` (e9c4c0b8...). `tx/f102v_rec.tsv` carries no per-position status, so it is not used;
  the agreement comes from `tools/reconcile_passes.py --method nw` on the two passes.
- The key drawing `sources/cryptiana/web/henryiii_Vivonne1.png` (1ca6cd24...), its cell boxes
  `glyphs/boxes_tomokiyo_v1.tsv` (dc91442e...; 40 tokens) and the drawn sheet `glyphs/sheet_tomokiyo_v1.png` (99981204...).
- The sheet's 40 tokens (sheet_tomokiyo_v1.tsv, 85f5a1a0...): a b d e g h j k l m n o p r s t x y z tz to 3 # : P S f A @ V R
  L Z H 4 6 7 c 2 8.
- Task texts: D = `benchmark-tx/txeng2/sheetviv/reader_task.txt` (3f4a2098...) as is (LINES_HERE = the 13 lines, FILECOUNT
  = 26, OUTPUT_PATH = the scratch read.tsv, the sheet path = a scratch copy); W = `sheetvivc/reader_task.txt` (4806ca67...)
  with `viv102base/sheet_SIGNS_dv1.md` (08dd48d9...) as is; H and Hx = the D text with the sheet path replaced by the hand
  sheet's image paths and ONE sentence changed, the parenthesis describing the sheet: 'each row: the token, the key drawing
  first, then up to four examples of the same sign cut from another page of this hand'. The committed diffs are
  benchmark-tx/txeng4/1/task_*.diff.
- Readers: Sonnet (claude-sonnet-5) subagents in fresh contexts, one per pass; each gets a scratch directory holding only
  task.txt, the arm's sheet copy and the 26 crops; no repository path. ONE call per pass over all 26 crops; if a call cannot
  hold them, two calls of 7 and 6 lines for every arm, declared in RESULTS.
- Never used (R4, R4a): any frozen confirm item, f.103r, truth or flags edits, sorter pages or statuses, owner piles,
  settled_labels, owner_map, L74 oracle1, passX20*, atlas/no87_box_token*.tsv, key_pins.tsv, the old width-DP maps, and the
  f.102r outputs passA.tsv / passB.tsv (the truth's reference inputs). f.102v has no truth, so no known answer enters a tile.

## Tiles (read-free; benchmark-tx/txeng4/1/tiles.py, every step logged)
2a. `tools/glyph_atlas.py segment`, default pen-unit mode, one page per f.102v crop (74), boxes mapped to line coordinates
    by the crop's manifest x0, the s1/s2 overlap deduplicated at its midpoint, ordered by centre x, marks not tokens
    (TXE3-6's seg.py recipe; each crop holds its one line along its middle, so the segment's row is the line).
2b. Both passes converted to long form (line, pos, sign, conf): [PLAIN:...] stretches and '.' dropped, a trailing '?' stripped
    (conf M), as reconcile_passes does; `tools/reconcile_passes.py --method nw`; the agree positions are the aligned columns
    whose why is `agree` or `agree-flagged`, mapped back to pass A's own pos (a column counts toward pass A's pos unless
    disagreements.tsv shows pass A absent there).
2c. Round 1 (seed only): `box_token_align.py --signs <line-coordinate signs> --read <pass A long> --lam 0 --keep-pos <agree>
    --count-tol 0.10 --tokens-out tokens_r1.tsv`. Lines whose box count and pass-A token count differ by more than 10% are
    skipped and listed. Round 1 never stands alone.
2d. Round 2: `glyph_atlas.py classify --page all --only-train-labels --train-labels tokens_r1.tsv --knn 5 --topk 3
    --pca-scale unit` (vote() never lets a box vote for itself, so every box's top-k is leave-itself-out); then
    `box_token_align.py --signs ... --read <pass A long> --topk <that classify TSV> --keep-pos <agree> --count-tol 0.10
    --tokens-out tokens_r2.tsv` (--loo on, lam default).
2e. A tile is kept only where the box is op 1:1 at the same (line, pos) in both rounds, that pos is an agree position, and the
    read sign is one of the sheet's 40 tokens: tokens.tsv (sid, code, page, line, pos).
2e2. Shift check (R4a), before any sheet: the round-2 run repeated with `--check-labels <each box's kNN top-1 from 2d>
    --check-bound` (the same file steers the map, so the tool takes the leave-one-out positions); the printed rows and the
    verdict go into the addendum below and into RESULTS. On FAIL the failing lines are dropped, listed, and the check
    re-run once; a second FAIL, or UNCHECKABLE, means nothing from the join is scored.
2f. Purity gate, three parts, all needed for H and Hx to run: (i) the share of op-1:1 boxes among the boxes on the lines
    that passed --count-tol (every one of them carries a kNN label) is at least 0.80; (ii) at least 25 of the 40 tokens have
    2 or more kept tiles; (iii) 2e2 is PASS. Any part failing: H and Hx do not run (declared non-test: 'f.102v tiles not
    separable, or not verifiably placed, at pen units'), W and D run alone.

## Sheets (k = 4 fixed, nothing tuned)
- H: `glyph_atlas.py atlas --from-tokens tokens.tsv --canonical-boxes glyphs/boxes_tomokiyo_v1.tsv --canonical-dir
  sources/cryptiana/web --codes <the 40 tokens> --per 4 --spread --trim 0.2 --rows-per-sheet 10` (four images of 10 rows,
  cell 96 px; a token with under 2 tiles shows the drawn cell alone).
- Hx: the same with `--shuffle-rows 20261012` (a seeded derangement of the hand tiles across rows; no hand tile stays in
  its own row; drawn cells and row labels stay put).
- Both sheets, their tile tables (source page, line, sid of each tile) and sha256 are committed before any read.

## Arms and order
W (words), D (drawing), H (drawing + hand tiles), Hx (drawing + deranged hand tiles). Two Sonnet passes per arm.
`random.Random(20261012).shuffle(['W','D','H','Hx'])` gives round 1 = **D, H, W, Hx**; round 2 repeats that order.

## Endpoint (co-primary masks)
Per arm, the mean over its passes of the unit-cost edit total (tx_bench's err_true numerator, S+D+I at value level) on the
13 test lines: as measured (417 scored) AND flagged-excluded (216 scored). Scoring, once per pass: `tools/tx_bench.py
<pass> --bench benchmark-tx/txeng3/6/bench_test.tsv --item vivonne1573-f102r-dev2 --exclude-flagged --strict
--coverage-diagnostic --ci`; paired per-line calls `--paired` against the other arms' passes of the same round (H as the
base for W, D, Hx; D as the base for W). Wilson 95% on every err_true; --strict beside; S/D/I beside.

## Gates (word for word from the brief)
- G-DEFAULT (a picture by default for this hand): mean(W) >= 1.25 x mean(H) as measured, AND mean(W) > mean(H)
  flagged-excluded, AND mean(W) - mean(H) > the maximum within-arm pass spread.
- G-HAND (the clerk's strokes add to the drawing): mean(D) >= 1.15 x mean(H) as measured, AND mean(D) > mean(H)
  flagged-excluded, AND the gap > the maximum within-arm spread, AND mean(Hx) >= mean(H) + the maximum within-arm spread.
Anything less is 'not distinguishable from pass spread', with every number. Beside the gates: position McNemar H vs W and
H vs D; the line bootstrap; S/D/I; per-arm reader agreement (reconcile_passes nw); edits on tokens that have hand tiles
against tokens that do not.

## Control and why it can vary
W and D run in the same session with the same crops, model, call layout and output format; only the alphabet form differs.
The alphabet form acts on matching, and the edit total counts matching: on this leaf two forms moved it 58 vs 86 while
same-form runs moved it by 6 (SHEET-VIV-C); on no.87 the forms gave 15 vs 67 (TXE3-8). Hx keeps every pixel of H's sheet
but moves each hand tile into a wrong row; that changes how a reader matches against the tiles, so Hx's edits can rise or
fall against H. It separates the right strokes from simply having more picture area. The join gate's permuted-label null
(join_check B2/B3) is the chance null for the one classifier in the pipeline (the round-2 kNN); it can PASS, FAIL or be
UNCHECKABLE independently of the target lines.

## Units, cost accounting and stop rule (R9)
Units: tools + PREREG + tiles + sheets (the brief's 'about 5', the Fable floor included as its cost line says), one pass =
about USD 0.6 and 8 minutes (TXE3-2 / TXE3-3 ledger rows), scoring + RESULTS about 3 (mandatory, reserved up front). The
running estimate before starting pass n is 5 + 3 + 0.6 n; a pass is not started when that exceeds 12 (80% of the cap) or
when the clock passes 02:57 UTC (96 minutes from the claim at 01:21). So at most 6 passes are started under this rule
(8 + 3.6 = 11.6; a seventh would read 12.2). Note for the parent, flagged in ROOM: R9's other sentence ('the Fable floor
for this shape, about USD 9-10, plus the units done') would allow only 4-5 passes; this PREREG takes the accounting the
brief's own cost line and declared readings were built on, and the parent's get_session is the figure of record. If the
parent answers in ROOM before round 2 starts, that answer governs. Passes run four at a time per round.

## Declared readings by passes done
- 8 passes: both gates.
- 6-7 passes: the gates on arms with two passes; the other arms reported as 'one replicate, spread unmeasured'. Under the
  registered order, 6 passes = D and H twice, W and Hx once: G-HAND's D-vs-H clauses are gated with the D/H spreads, its
  Hx clause and G-DEFAULT are reported against the measured D/H spread with W and Hx as single replicates.
- Fewer than 6 passes: no gate, report only.
- Purity gate failed: non-test for H and Hx; W and D reported against each other with the same spread rule.
Cross-session: TXE4-8's arm N is the same configuration as D (Sonnet, drawn sheet, free read, same 13 lines); if its passes
are committed before RESULTS they are quoted beside D, never pooled.

## Addendum (filled 12 Oct 2026 01:3x UTC by date -u, before any sheet or read; the 2e2 shift check and the purity gate)
Tiles (read-free, benchmark-tx/txeng4/1/tiles.py; the patched aligner benchmark-tx/txeng4/1/box_token_align.patch):
- 2a: 74 f.102v crops -> 1,819 pen-unit boxes, 1,661 after the s1/s2 overlap dedupe (pass A reads 1,819 tokens: the hand joins).
- 2b: reconcile nw: agree 1,440 of 1,859 aligned columns (77.5%); 1,440 agree positions in pass A's numbering (walk check: no line mismatch).
- 2c round 1 (--lam 0, --keep-pos agree, --count-tol 0.10): 32 of 37 lines skipped by the count tolerance (boxes 10-33% under the
  token count on every one of them); 5 lines pass (L18, L29, L30, L34, L35); 159 1:1 tokens, 25 codes (maps/round1.log).
- 2d round 2: kNN from those 159 (classify --only-train-labels, leave-itself-out vote, --knn 5 --topk 3) on all 1,819 boxes;
  label-aware re-map on the same 5 lines: ops 1:1 120, 2:1 64, 1:2 78, unsure 24; 95 1:1 tokens (maps/round2.log).
- 2e2 shift check (join_check --steered, seed 20261012; the kNN top-1 of every box as the check label, leave-one-out positions
  because those labels steered the map), printed rows:
    join_check: FAIL n=140 share0=0.200 (null p95 0.087) share+-1=0.150 (bound 0.208)
      f102v_L18: pass placed=26 {+1: 4, none: 14, 0: 6, +-2: 1, -1: 1}
      f102v_L29: pass placed=29 {none: 13, +1: 5, 0: 7, +-2: 2, -1: 2}
      f102v_L30: pass placed=23 {none: 12, +1: 2, -1: 2, +-2: 4, 0: 3}
      f102v_L34: fail placed=34 {none: 25, 0: 3, -1: 3, +-2: 2, +1: 1}
      f102v_L35: pass placed=28 {none: 18, 0: 9, +1: 1}
  (the tool's own --check-bound run printed PASS with steered=False because the check file was a copy of the top-1 column,
  not the --topk file itself; the steered run above is the one of record, R4a.) L34 dropped, re-checked once (maps/map_r2b.tsv):
    join_check: PASS n=106 share0=0.236 (null p95 0.105) share+-1=0.160 (bound 0.226); L18, L29, L30, L35 all pass B1.
  Verdict of record: PASS on four lines after the one allowed drop; the leave-one-out share at 0 is 0.236, under a quarter of
  the placed tiles, against a permuted-label p95 of 0.105.
- 2e kept tiles (1:1 in both rounds at the same agree position, code among the 40): **24 tiles, 13 codes, 7 codes with >= 2
  tiles** (g 4, tz 3, d 3, ':' 2, '#' 2, o 2, 7 2, y/a/R/k/p/6 one each); benchmark-tx/txeng4/1/tokens.tsv.
- 2f purity gate: (i) share of op-1:1 boxes on the four passing lines 92 / 197 = **0.467 < 0.80 FAIL**; (ii) **7 of 40 codes
  with >= 2 tiles, < 25 FAIL**; (iii) shift check PASS after the drop. **Gate FAILED on (i) and (ii): declared non-test
  'f.102v tiles not separable, or not verifiably placed, at pen units'. H and Hx do not run; W and D run alone**, in the
  registered order with H and Hx removed (D, W; D, W), two passes each = 4 passes, inside the 6-pass stop rule.
- Context (step 1, Opus SHEET-VIV passes rescored on the 13 test lines, scores/context_pass*_sv.txt): unit-cost edits as
  measured 101 / 104 / 106 of 417 (A / B / Z), flagged-excluded 13 / 16 / 18 of 216. Never a baseline arm.
