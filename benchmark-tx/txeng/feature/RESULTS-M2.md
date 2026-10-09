# TXE-M2 results: feature-first in two calls, with a compliance gate (LANE TX-ENGINEER, idea M24 retest; 9 Oct 2026, 08:11-08:2x UTC by date -u)

Brief `.claude/briefs/runs/2026-10-09-account4-txe-m2.md`; pre-registration `PREREG-M2.md` (d50c170c2, pushed before any read).

**Verdict: non-test: no compliant feature read.** The compliance gate failed on (c), the control, so no cell call was run,
nothing was scored and no eval look was taken (looks 0). (a) and (b) passed.

## Compliance (tools/tx_features.py comply; m2/comply_dev.txt; run on the committed call-1 reads 077ad90bb, 06bab4222, a0e38d9da)
| check | registered gate | result | |
|---|---|---|---|
| (a) signs per line vs pass A | every line within 10% | 12/12 lines; max dev 0.038 (L03 27 vs 26; L08, L09, L11 +1) | ok |
| (b) feature variety | two values on >= 10% of rows, each column varying in the cell table (dots exempt: 50/51 cells 0) | desc, asc, bars, loops, lean, tail all ok; dots 336/16/6 (exempt) | ok |
| (c) control: 51 printed sheet tiles, labels removed, seeded order | >= 70% of tiles within one feature of cell_features.tsv | 19/51 = 0.373; exact 7/7 4/51 | **FAIL** |

Per-feature agreement on the control: desc 33/51, asc 32, bars 27, loops 47, dots 49, lean 26, tail 36. Features
differing per tile: 0: 4, 1: 15, 2: 13, 3: 12, 4: 5, 5: 2. The disagreements, script value -> reader value
(m2/control_confusion.txt), are systematic:
- lean: left->upright 11, right->upright 9. The reader calls upright what the script's principal-axis shear calls leaning.
- bars: 2->0 9, 1->0 8, 2->1 5. The script counts flat loop tops and bowl bottoms as bars, the reader does not.
- asc/desc: long->none 9 (asc), short->none 11 (desc). The script's body band is narrower than the reader's sense of
  the body.

What the failure says: the gate cannot tell the two causes apart, but the pattern points to the table, not to a reader
ignoring the ink. The control reader wrote one note per tile describing each tile's shape, and its counts and variety on
the lines are faithful. Its written features disagree with the script table in the same directions throughout. A reader
writing from the ink does not share the script's feature vocabulary, so call 2 would have matched features against a
table they do not track. Then a `mismatch` flag or a "matching" cell measures the table's thresholds, not the hand. The
gate did what it was registered to do: it stopped a cell call that could not test feature-first deciding.

## Gate lines
Not run (compliance failed before any cell call): no passU2_feature_dev_tune.tsv, no tx_bench, no tx_taxonomy, no
mismatch table. Eval: not run, looks 0.

## Reader task text
Prompt (all three calls): "Your instructions are in the file <task>. Read that file first and follow it exactly. Besides
that file, open only the image(s) it names. Write only the TSV it names." Tasks: `m2/task1_c1.md`, `m2/task1_c2.md`
(18 crops each), `m2/task1_control.md` (one image, `m2/control_tiles.png`). The line task (crop list omitted):

```
# Feature read of hand-drawn signs (TXE-M2 call 1)

You describe the SHAPE of every mark on the images named below, one row per mark. You are not asked what the marks are or mean, and you get no list of sign names. Read ONLY the images named below; do not open any other file in this repository. Write only the TSV named below.

The images are horizontal segments of manuscript lines (a 16th-century cipher page; every mark is a cipher sign, upscaled 2x). Segments s1, s2, s3 of a line run left to right and overlap by about 100 px at the 2x scale (50 px native), so a sign that appears at the right edge of s1 and again at the left edge of s2 is ONE sign -- count it once, and continue the count across the segments. Small marks that look like punctuation ("=", "+", a slash between two dots, "3", "2", a crossed or barred stroke, a lone "o") are signs too; take every mark as a sign unless it is clearly a pen slip. A sign's own dots or ticks belong to it.

`passage` = the line id (L01, L02 ... from the file name), `pos` = 1-based position in the line, left to right.

Output: one TSV with this header and one row per sign:

    passage	pos	desc	asc	bars	loops	dots	lean	tail	conf	note

Each feature column holds exactly one value from its vocabulary:

    desc=none|short|long  asc=none|short|long  bars=0|1|2  loops=0|1|2  dots=0|1|2+  lean=left|upright|right  tail=none|left|right

- desc: ink below the main body of the sign, compared with the body's height (none: under a quarter; short: under three quarters; long: more).
- asc: ink above the main body, same scale.
- bars: long horizontal strokes running across most of the sign's width, 0, 1 or 2 (a flat loop top counts).
- loops: closed loops (enclosed holes), 0, 1 or 2.
- dots: separate small marks (dot, tick, accent) apart from the main stroke, 0, 1 or 2+.
- lean: the sign's main axis tilts left, stands upright, or tilts right.
- tail: the lowest part of the ink ends to the left or right of the sign's centre, or is centred (none).
- conf: H (features clear), M (one feature uncertain), L (hard to see).
- note: a few words on the shape (optional).

Look at the ink of each mark and write what you see. Do not name, classify or compare the marks with any sign list. When done, report in one short paragraph: rows per passage and how sure you were.

```
The control task differs only in the image paragraph ("numbered tiles, each holding one printed sign ... `passage` =
TILES, `pos` = the tile number"). Both line readers again reported that the overlap was wider than 100 px (5-6 signs) and
de-duplicated by eye; the sign counts still matched pass A's within 4%.

## Calls
Opus 5.5 vision calls: dev 3 (control 1, features 2), cells 0, eval 0. Cost: the lane reads get_session.

## Follow-up (one line, not attempted: brief)
Use a reader-derived cell table instead of the script table: one feature-only call on the unlabelled tiles (this control
read, or two reads reconciled) becomes the table call 2 matches against. Reader and table would then share one feature
sense, and (c) is replaced by a test-retest agreement of two tile reads. If that agreement is itself under 70%, the
seven-feature vocabulary is too loose to decide cells, and M24 is retired at this vocabulary.
