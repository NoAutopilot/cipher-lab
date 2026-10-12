# PREREG TXE4-8 BOX-ANCHOR (account 3, Fable 5.1 worker, session_014V4uay7sV21NShHzNwq1sU, 12 Oct 2026 01:3x UTC by date -u; pushed BEFORE any read or score)

One of ten TXE4 experiments the account-3 parent launched on 12 Oct 2026 (brief `.claude/briefs/runs/2026-10-11-acct3-txe4-8.md`,
commit 93b7bb321 or later; owner's go 00:14 UTC). Question: on a joining hand (Saint-Gouard's clerk, BnF fr.16105 f.102r), does
drawing the machine's own numbered pen-unit boxes on the line crops and asking the reader for one answer per box cut unit-cost
edits, against a free line read (N) and against randomly placed boxes at the same count (R)?
Rules: the brief's common TXE4 rules R1-R10 bind. Readers blind (task text + sheet picture + crops, overlaid or not; no key, no
truth, no other pass, no repository path); every reader output committed with its sha256 BEFORE any score
(benchmark-tx/txeng4/8/SHA256SUMS.prescore); no *.truth.tsv edited; the frozen confirm items never opened; no owner evidence (sorter
pages, statuses, piles, settled_labels, owner_map, L74 oracle1 answers or merges, passX20*, no87_box_token_labelaware.tsv,
key_pins.tsv) enters any arm; nothing published, nobody contacted. Truth and flags are opened only by tools/tx_bench.py.
Disclosure: while checking the file format before this PREREG the worker printed the header and the first three rows of
benchmark-tx/txeng3/6/truth_test.tsv (f102r_L02 pos 1-3) to its own transcript; no reader receives anything from the worker but
the brief's named files, so no arm is steered by it; it is recorded here, not hidden.

## Hypothesis
H1: on the 13 TXE3-6 test lines, arm O (pen-box overlay, one answer per numbered box) has fewer single-pass unit-cost edits
(S+D+I, tx_bench `ser_errors`) than arm N (free line read), by the gate below, and arm R (random geometry at the pen count)
does not share the gain: good boxes, not merely answering per box, carry it.
H0 (a result): O does not beat N by the gate; or R matches O (the output format, not the boxes, carries any gain); or O's
gain is only in indels, which one-row-per-box limits by construction.

## Nearest prior (register rows) and what differs from them
- `SHEET-VIV` and `SHEET-VIV-C` (txeng2, dev-FAIL): the drawn sheet `sheet_tomokiyo_v1.png` with free line reads of this very
  item by Sonnet, two blind passes and a passZ reconcile; on dev2 insertions were half the flagged-excluded edits (passZ_sv
  S24 D5 I29; passZ_tl S32 D6 I48). Arm N here IS that configuration (same task text, sheet, crops, model) restricted to the
  13 test lines, run fresh as the in-session control; arms O and R add a numbered box overlay and a one-row-per-box output,
  which SHEET-VIV never had. Neither row is retired.
- `ORACLE-LOCATION-1` (txeng2, queued; PREREG-txeng2-17/19, LANE TX-ENGINEER-2, account 4): its arm B gives readers
  OWNER-verified numbered boxes on its 12 manifest lines, all TXE3-6 TRAIN lines. This job is the automated counterpart on the
  disjoint TEST lines with the MACHINE's boxes (segmenter default, not tuned on dev2) and never touches the oracle1 boxes,
  answers or merges.tsv. A ROOM line addressed to LANE TX-ENGINEER-2 said so at the claim (01:18 UTC).
- TXE3-6 UNIT (benchmark-tx/txeng3/6/RESULTS.md, VERIFY.md; null, not in the register): the same 13 test lines and the same
  pen boxes (seg/pen/boxes.tsv, 569 boxes for 662 truth positions) scored under a weak kNN (err_true 0.77); it named this
  job as its own next step ("two blind Sonnet line passes on the 13 test lines with numbered box overlays, one label per
  box"). VERIFY-6 found its random-cut control confounded with box COUNT; here R has the same count as O by construction
  and differs only in geometry (can-vary count below).
- TXE-K / BOXMAP-LA (benchmark-tx/txeng/RESCORE.md; ed5d42162): a width-only box-to-token DP put tiles one token off on
  10 of 26 no.87 lines. The PRIMARY arms here join nothing to positions: a numbered box IS the position, so the DP is
  avoided; only the SECONDARY (N packets) uses tools/box_token_align.py under R4a.
Retired instruments named in R4 (':' mark rule, transcribe-and-decode crossword, look-alike pass as accuracy, exemplar compare
layout, M24 feature-first, err_2reader as predictor) are not used; no width-only box map is used anywhere.

## Fixed inputs (frozen now; nothing below changes after a number is seen)
- Item: vivonne1573-f102r-dev2 (dev, never eval/confirm). Scored lines: the 13 TXE3-6 TEST lines f102r_L02, L04, L08, L10,
  L16, L18, L20, L24, L28, L30, L32, L34, L36 (bench `benchmark-tx/txeng3/6/bench_test.tsv`, truth rows
  `benchmark-tx/txeng3/6/truth_test.tsv`, 662 truth positions, 417 scored, 216 scored after the flagged-excluded mask).
- Crops: `ciphers/fr16104-vivonne-spain-1572/images/c105_f102r_L{line}_s{1,2}.jpg` (26 files, 1600 x 102 px native, 250 px
  overlap between s1 and s2), used as committed, never resized.
- Boxes (arm O): `benchmark-tx/txeng3/6/seg/pen/boxes.tsv`, the test-line rows (569 boxes; columns line, pos, sid, page,
  x_line, x, y, w, h; x,y,w,h in the named crop's own pixels; the s1/s2 overlap already deduplicated at its midpoint, so each
  box has one page and one number per line, numbered 1..N in reading order by `pos`).
- Boxes (arm R): `tools/iiif_lines.py --box-overlay <pen rows> --random-geometry 20261013`: per line the same box count as
  the pen rows, boundaries at seeded uniform random x positions (line coordinates) within the line's ink extent (columns of the
  two crops with ink under the segmenter's threshold 170, s2 mapped through its x_line offset), height = the line's pen box
  band (min y to max y+h over its pen boxes), each box drawn on the crop that holds its centre (clipped to that crop if it
  straddles an edge). Written to benchmark-tx/txeng4/8/boxes_R.tsv before any read.
- Overlay drawing (new `--box-overlay BOXES.tsv --overlay-out DIR`): a copy of the committed crop with a 44 px light band
  appended below; each box outlined dashed in Okabe-Ito blue #0072B2 and orange #B35900 alternating, the box number in dark
  ink #000000 on the light tint band under the box (#F0E442 tint and white alternating with the outline colour). Colours
  are the `sheets_light` palette of tools/cvd_check.py; the overlay's colour set is run through `tools/cvd_check.py --marks
  '#0072B2,#B35900,#000000' --bg '#ffffff' --tints '#F0E442' --text '#000000' --tint-text '#F0E442:#000000'` and its
  output pasted in RESULTS; a FAIL stops the job before any read.
- Sheet: `ciphers/fr16104-vivonne-spain-1572/glyphs/sheet_tomokiyo_v1.png` (the brief's `glyphs/sheet_tomokiyo_v1.png`; the
  40 printed tokens as in the SHEET-VIV task text).
- Task text N: `benchmark-tx/txeng2/sheetviv/reader_task.txt` as is, with LINES_HERE / FILECOUNT / OUTPUT_PATH filled and the
  repository paths replaced by the scratch copies' paths. Task text O and R: the same text plus one paragraph: for every line
  the reader gets four images, s1 unmarked, s1 with numbered boxes, s2 unmarked, s2 with numbered boxes; it reads ONLY the
  numbered boxes, one row per box: `line box signs alt conf`, signs = the sheet token(s) of the sign(s) inside the box,
  space-separated if the box holds several, `-` if the box holds no cipher sign (plain words, a blot, empty); it never adds a
  row for ink outside a box; the overlap is numbered once. R's task text is identical to O's (the reader is not told the boxes
  are random). The task texts are committed in benchmark-tx/txeng4/8/tasks/ before the first call.
- Readers: Sonnet (claude-sonnet-5) subagents, fresh context per call, one call per pass over all 13 lines (N: 26 images;
  O and R: 52 images). Fallback, declared now: if a call fails or returns fewer than 13 lines, that pass is re-run as two calls
  of 7 and 6 lines (L02-L20 / L24-L36), and then EVERY remaining pass of every arm runs as two calls too; a pass already
  complete in one call is kept. Each reader gets a scratch directory with copies of its files only (task.txt, the sheet copy,
  its crops) and no repository path.
- Order of the five passes, `random.Random(20261013).shuffle([N1, O1, R1, N2, O2])` run 01:3x UTC before any read:
  **R1, O1, N1, N2, O2**.
- Scoring (committed `benchmark-tx/txeng4/8/score.py`): O and R box rows -> positions (tokens in box order, a `-` box adds no
  position, several tokens add several positions), written as `line pos sign alt conf`; N read as is. Then
  `tools/tx_bench.py --bench benchmark-tx/txeng3/6/bench_test.tsv --exclude-flagged --strict --coverage-diagnostic --ci
  [--json]` per output, S/D/I from the JSON. Each output scored once.
- Access log and usage: copies of benchmark-tx/txeng3/8/access_log.py and usage.py adapted to this session's scratch dirs,
  committed with their outputs.

## Arms
- N (control, free read): SHEET-VIV task text, 2 passes.
- O (treatment): pen-box overlay, one row per numbered box, 2 passes.
- R (control, geometry): random-geometry overlay at the pen count, same task text and output format as O, 1 pass.

## Endpoint
PRIMARY (co-primary, both masks): each arm's mean single-pass unit-cost edits (tx_bench `ser_errors` = S+D+I), as measured
(417 scored) AND flagged-excluded (216 scored). Reported with err_true and its Wilson 95% interval on both masks, --strict
beside, S/D/I beside. Never the flagged-excluded figure alone.
BESIDE: O's insertions+deletions against N's (expected lower by construction, not gated); TXE4-1 arm D passes quoted beside N
if committed before RESULTS, never pooled.

## Gate (the brief's, word for word)
PRIMARY: each arm's mean single-pass unit-cost edits, as measured (417) AND flagged-excluded (216), co-primary. The overlay is
adopted for joining hands if all of these hold:
- mean(N) >= 1.15 x mean(O) as measured;
- mean(N) > mean(O) flagged-excluded;
- the gap > the maximum within-arm spread;
- O's substitutions <= N's substitutions, so the gain is not only indels, which one-row-per-box limits by construction;
- mean(R) >= mean(O) + O's pass spread.
Beside: O's insertions+deletions against N's. They are expected to be lower by construction and are not gated.
Reading of the gate: "the gap" is mean(N) - mean(O) as measured; "the maximum within-arm spread" is max(|N1-N2|, |O1-O2|) as
measured; "O's pass spread" is |O1-O2| as measured. The five conditions are evaluated on the as-measured counts except the
second, which is the flagged-excluded count. Any condition failing = gate NOT MET (a null is a result).

## Control and why it can vary
N runs in the same session with the same model, sheet and crops; its edits vary with reader input (SHEET-VIV-C). R uses the same
overlay machinery, task text and output format as O, with wrong geometry at the same count, so it can fail differently from O:
it separates good boxes from merely answering per box. Can-vary count, computed BEFORE any read and pasted in the addendum
below: the share of R boxes whose IoU with every pen box of the same line is below 0.5 (line coordinates). R must differ from
O in geometry at an equal count (VERIFY-6's count confound); if that share is under 0.5 the R set is regenerated once with seed
20261014 and the second share stands, declared here.

## SECONDARY (only if the five passes finish under 80% of the time box and of the running estimate)
Reconcile O1/O2 with `tools/reconcile_passes.py --by-box` and N1/N2 by nw; send the DISAGREE rows to tools/tx_adjudicate.py
packets. O windows at the exact box coordinates. N windows from a `tools/box_token_align.py` map of N's reconciled read to the
pen boxes with `--tile-labels <O1's per-box tokens at its one-token boxes> --loo --check-labels <O2's per-box tokens>
--check-bound` (R4a; TXE4-0 REPAIR landed 6f84c5af and tools/join_check.py exists). Its shift-check rows are pasted before any
packet is built; on FAIL the failing lines are dropped and the check re-run once; if it still FAILs or is UNCHECKABLE, N's
packets are built only from passing lines and the comparison is reported on those lines only. Compare passZ edits and the
adjudicator's accuracy at one-reader-error rows. Not part of the gate.

## Units, stop rule and declared reading per number of units done
Units (brief estimates): (1) tools + offline tests, 35 min; (2) R boxes + can-vary count, 10 min; (3)-(7) the five passes in
the order above, about 10 min and USD 0.6 (O, R) or 0.45 (N) each; (8) scoring, 10 min. Box 01:18-03:18 UTC (120 min from the
claim); no unit starts after 02:54 UTC (96 min) or when the running estimate (Fable floor USD 9-10 + units done) would pass
USD 12. A unit started is finished.
- 0-2 passes done: no comparison; RESULTS reports the tools, the R set and the can-vary count only ("not run").
- R1, O1, N1 done (3 passes): single-pass comparison, no spread terms available; the gate's spread conditions are
  "untestable at one pass per arm", the first, second and fourth conditions are reported on the single passes, verdict
  "indicative only, gate not evaluable".
- R1, O1, N1, N2 done (4 passes): N's spread known, O's not; the gate is evaluated with O's spread taken as N's spread
  (declared substitute), verdict labelled "O spread substituted".
- All five: the gate as written.
A null is a result. The SECONDARY runs only under the 80% rule above.

## Addendum (filled before any read; appended, never edited above this line)
- 01:2x-01:3x UTC 12 Oct 2026 (the header's "01:3x" was written before the clock was re-read; the claim is at 01:18, the
  PREREG commit at 01:27 by date -u). Tools landed before any read: `tools/iiif_lines.py --box-overlay BOXES.tsv --overlay-out
  DIR [--random-geometry SEED] [--overlay-lines IDS]` with `tools/tests/test_box_overlay.py`, and `tools/reconcile_passes.py
  --by-box` with `tools/tests/test_reconcile_by_box.py` (both OK, 0 fails). Overlays: benchmark-tx/txeng4/8/overlays/{O,R}/
  (26 pages each, 569 boxes each), built from boxes_O.tsv (the 569 test-line pen rows) and boxes_R.tsv (seed 20261013).
- Can-vary count (computed by the tool before any read): **423 / 569 = 0.743** of R boxes have IoU < 0.5 with every pen box
  of their line (>= 0.5, so the seed-20261013 set stands; no regeneration).
- cvd_check on the overlay palette (`--marks '#0072B2,#B35900,#000000' --bg '#ffffff' --tints '#F0E442' --text '#000000'
  --tint-text '#F0E442:#000000'`): normal worst pair #0072B2 vs #000000 dE2000 39.2 margin +19.2; protan 38.1 +18.1; deutan
  38.3 +18.3; tritan 41.5 +21.5; **PASS**.
- Task texts: benchmark-tx/txeng4/8/tasks/{N1,O1,R1}.txt (N2, O2 identical to N1, O1 but for the scratch path), built by
  build_tasks.py; O and R texts identical. One call per pass (N 26 images, O/R 52 images).
- Scorer: benchmark-tx/txeng4/8/score.py (checks the read's sha256 against SHA256SUMS.prescore before scoring).
