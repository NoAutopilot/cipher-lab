# TXE3-6 UNIT results: box in pen strokes or in signs? (account 3, Fable, session_0168bM3qJgyNJdKy6fE6dMAr; 11 Oct 2026 05:48-06:2x UTC by date -u)

Pre-registration: benchmark-tx/PREREG-txeng3-6.md (committed fdb7a4fec before any segment, classify or score; amendment 1
dropped f102r_L14, which has no truth rows, before any figure was read). Brief: the account-3 parent's TXE3 batch (11 Oct 2026).
**Verdict: null on the pre-registered gate, the owner's pen-unit rule stands.** Splitting joined shapes at the segmenter's
column-ink minima made the downstream read worse, not better, and the machine's cuts read no better than cuts placed at
random inside the same boxes. The test is conditional on a weak classifier (below); it is a dev result (no eval item in a
joining hand is unfrozen).

## Item and split

- **vivonne1573-f102r-dev2** (dev; Saint-Gouard clerk hand 1573; truth = the clerk's period decipherment under the published
  Tomokiyo key; truth sha256 007a8be9...). Chosen from counts, not scores: no.87 does not join (340 pen-unit boxes for 354
  truth positions on its 12 oracle lines; the owner's box check merged 0 of 343 tiles), Vivonne f.102r does (516 for 610).
- **Test lines** (scored): f102r_L02, L04, L08, L10, L16, L18, L20, L24, L28, L30, L32, L34, L36 -- 13 lines, 662 truth
  positions, 417 scored (245 excluded by the truth's own status), 201 of the scored flagged by the truth build (clerk-split,
  align-conflict). **Train lines** (labels and the (W, P) choice only): the other 22 truth lines of L01-L36, including all 12
  oracle manifest lines (L37 is in neither set). Nothing was written under benchmark-tx/txeng2/oracle1/; the owner's answers were not read.

## Recipe (benchmark-tx/txeng3/6/seg.py, labels.py, classify.py; all read-free: no model call anywhere)

1. Boxes: `tools/glyph_atlas.py segment`, one page per line crop (74 crops), boxes mapped to line coordinates by the crop's
   manifest x0, the s1/s2 overlap deduped at its midpoint (the OL1-BOXES rule), order by centre x, marks not tokens.
   - (a) **pen units**: default mode as it stands (connected components + x-overlap merge; never splits a component).
   - (b) **sign units**: the new `--split-wide W --split-piece P` option (shared tool + offline test, commit f7406b2a9): a
     merged box wider than W x median height is cut into max(2, round(w / (P x mh))) pieces at the column-ink minimum within
     +-0.35 piece of each equal-width cut. W 1.5, P 0.85 chosen on TRAIN lines only by sum |boxes - truth positions| over
     the registered 4 x 4 grid (grid.tsv: 66, train boxes 1135 vs 1145 truth; pen units 992).
   - (c) **control**: `--split-random SEED` (seeds 1, 2, 3): the same boxes, the same piece count, cuts at uniformly random
     columns. Can it vary? 150 / 150 / 144 of the 653 (c) boxes on the test lines (22-23%) have a different geometry from the
     (b) box at the same place -- the manipulation moved the statistic's input (PREREG rule-3 check).
2. Classifier (identical in every condition): one frozen exemplar set from the train lines' (b) boxes -- round 0 (count-matched
   lines L03, L25, L33) 154 labels; round 1 (alignment-propagated, registered because round 0 < 400) +210 = **364
   exemplars, 27 codes** (labels_train.tsv, labels_report.txt). `glyph_atlas.py classify --page all --knn 5 --topk 3`, every
   test page held out from voting.
3. Decode: `tools/key_decode_lattice.py decode` on the top-3 lattice, key = the folder's key.tsv as sign/value (32 rows),
   --lang fr16, --lam 4, 100 shuffled keys, seed 1.
4. Score: `tools/tx_bench.py` against truth_test.tsv (the 13 test lines' rows of the committed truth, byte-identical, source
   sha256 in its header) through bench_test.tsv; both masks; --paired per line; --ci 1,000-resample line bootstrap.

## Numbers (13 test lines, 417 scored; Wilson 95%; flagged-excluded 216 scored)

Top-1 (the primary endpoint, before any decode):

| box set | boxes (truth 662) | err_true as measured | flagged excluded | standard SER (S / D / I) |
|---|---|---|---|---|
| (a) pen units | 569 | **0.772 (322/417) 0.730-0.810** | 0.875 (189/216) | 0.712 (219 / 64 / 14) |
| (b) sign units, ink-minimum cuts | 653 | **0.863 (360/417) 0.827-0.893** | 1.069 (231/216) | 0.799 (264 / 28 / 41) |
| (c) random cuts, seed 1 | 653 | 0.830 (346/417) 0.791-0.863 | 1.005 (217/216) | 0.782 (231 / 44 / 51) |
| (c) random cuts, seed 2 | 653 | 0.854 (356/417) 0.817-0.884 | 1.014 (219/216) | 0.813 (248 / 39 / 52) |
| (c) random cuts, seed 3 | 653 | 0.861 (359/417) 0.824-0.891 | 1.069 (231/216) | 0.789 (244 / 38 / 47) |

(err_true's numerator counts insertions, so under the flagged-excluded mask it exceeds its denominator; the standard SER
beside it is the bounded figure. Never quote the flagged-excluded column alone.)

After the lattice decode (secondary): pen 0.770 (321/417) 0.727-0.808; sign 0.825 (344/417) 0.786-0.858; random seeds
0.801 / 0.849 / 0.847. The decode's own control fails in every condition: the real key ranks 8-12 of 101 shuffled keys on the
lattice score (z 1.29-1.55) and 2 of 101 on the top-1 score (z 2.61-2.91) -- the language model is inventing text over a
lattice this noisy, so the decode licenses nothing here and the top-1 comparison is the result.

Paired per line (tools/tx_bench.py --paired, as measured):

| comparison | lines improved / worsened / tied | line sign-test p | unit-cost edits | McNemar fixed / broken (p) | SER difference, 95% line bootstrap |
|---|---|---|---|---|---|
| (b) sign vs (a) pen | 3 / 8 / 2 | 0.227 | 297 -> 333 | 46 / 39 (0.52) | +0.024 .. +0.160 (worse) |
| (c) seed 1 vs (b) | 5 / 3 / 5 | 0.727 | 333 -> 326 | 42 / 38 (0.74) | -0.050 .. +0.010 |
| (c) seed 2 vs (b) | 3 / 7 / 3 | 0.344 | 333 -> 339 | 39 / 39 (1.00) | -0.014 .. +0.043 |
| (c) seed 3 vs (b) | 7 / 5 / 1 | 0.774 | 333 -> 329 | 52 / 45 (0.54) | -0.044 .. +0.022 |

Per-line counts (truth / pen / sign; the three random sets equal sign by construction): L02 56/52/69, L04 52/46/47,
L08 49/38/44, L10 47/40/54, L16 57/45/50, L18 52/50/52, L20 53/38/49, L24 52/43/46, L28 51/44/50, L30 52/46/48, L32 50/45/53,
L34 40/37/45, L36 51/45/46. The split touched 66 of the 569 pen boxes on the test lines and made 150 pieces of them.

## Gate (PREREG): FAIL for sign units; case "(a) <= (b): pen units stand"

- err_true(b) 0.863 is not below err_true(a) 0.772; the paired bootstrap of the SER difference excludes zero on the wrong
  side (+0.024 .. +0.160); 8 lines of 13 got worse.
- (b) is not below every random seed: it is the worst of the four split sets (0.863 vs 0.830 / 0.854 / 0.861), and no seed
  differs from it beyond noise (p 0.34-0.77, fixed about equal to broken). So the column-ink minimum is not finding sign
  boundaries on this hand: a piece cut there classifies no better than a piece cut anywhere.
- What the split does: deletions fall (64 -> 28; the joined box no longer swallows its neighbours) but substitutions rise
  (219 -> 264) and insertions rise (14 -> 41), and the two added columns outweigh the one saved. The count matches better
  (653 vs 569 for 662) while the reading gets worse -- box count is not accuracy, the same shape as "agreement is not
  accuracy" (LESSONS.md, Look-alike pass).

## Limits (read before using the number)

- **Weak classifier.** A kNN over 364 truth-labelled exemplars reads this hand at err_true 0.77 even on pen units (accepted-
  token error 0.54), far from the product reader's 0.15 on the same hand (S2 single passes). The comparison is therefore
  "which unit a weak shape classifier reads better", and a stronger reader could in principle use sign-unit boxes
  differently; it is not a test under the product pipeline. No model read was possible in this design: the account's
  rate-limit status was `allowed_warning` at start (no new workers), and the brief caps subagent image calls anyway.
- **Dev result.** The only eval or confirm item in a joining hand is vivonne1573-f103r-confirm2 (frozen, single look); the
  hold-out here is a within-item line split, the (W, P) grid and the labels never saw a test line.
- The exemplar labels are propagated through an alignment that keeps only positions the round-0 classifier already got right
  or could pair 1:1 (210 of about 980 remaining train boxes): a biased sample toward easy shapes, identical for all
  conditions.
- Value-level truth: a homophone swap is invisible, so every figure is a lower bound on sign error (TX-BENCH).
- The flagged-excluded mask removes 201 of 417 scored positions (clerk-split and align-conflict flags); on that mask the
  ordering is the same (pen 0.875, sign 1.069, random 1.005-1.069 as measured by err_true; SER 0.727 vs 0.889).

## What it means for the owner (three plain sentences)

Your rule -- one box for whatever the pen wrote without lifting -- is the better unit for the machine as it stands: cutting
those shapes apart made the machine's read worse, not better, on thirteen lines of the Vivonne letter. The machine's own
cuts at the thinnest ink were no better than cuts placed at random inside the same shapes, so it does not know where one
sign ends inside a joined shape, and only a person's cut can be trusted there. The shape classifier used here is still far
from usable on this hand (about three signs in four wrong either way), so on Vivonne the reader, not the box, is the
bottleneck.

## Recommendation to the box-check team (TX-ENGINEER-2, account 4)

Keep **pen units** as the box unit for the owner's check and for the atlas on joining hands: an auto-split at column-ink
minima (`glyph_atlas.py segment --split-wide`) is a non-improvement on Vivonne f.102r (top-1 err_true 0.863 vs 0.772 pen,
8 of 13 lines worse, paired bootstrap +0.02 .. +0.16) and is indistinguishable from random cuts (three seeds 0.830-0.861,
p 0.34-0.77), so the segmenter cannot be the one that decides where a joined shape divides. The joined shapes the parent's
two blind passes flagged as "likely several" (9 of 16) are the right thing to show the owner as a cut question in the sorter
("where does this divide?"), with the owner's cut recorded as geometry; do not pre-split them for the page, and do not score
a machine split as a sign-unit set until a reader at product accuracy has shown a gain on it with this same control. The
tool option stays available for that test (it is off by default; a page with no wide box is unchanged, offline-tested).

## Next step and cost

The same (a)-vs-(b)-vs-(c) design under the product reader: two blind Sonnet line passes on the 13 test lines with numbered
box overlays, one label per box (26 calls at about USD 0.15 = about USD 4, plus reconcile, about USD 6 all in), when the
rate-limit status allows new workers. If pen units still win there, the question is closed for this hand; if sign units win
there but random cuts tie them, the gain is box count, not boundaries, and the owner's cuts (L74 recuts, geometry only,
about USD 1 of kNN) become the third set to score. Not re-run with a further tuning of W or P (rule 3's third-attempt clause).

## Files

seg.py, labels.py, classify.py (the recipe; `seg/{pen,sign,rand1,rand2,rand3}/boxes.tsv` + segment.log kept, the grid
runs' and classify directories' bitmaps and crops ignored by .gitignore and regenerable in about 2 minutes), grid.tsv,
labels_train.tsv, labels_report.txt, truth_test.tsv, bench_test.tsv, key_sv.tsv, outputs/*.top1.tsv *.topk.tsv *.dec.tsv,
scores/*.txt (tx_bench output as pasted above), dec/*.json *.decode.tsv *.plain.txt. Cost: not visible to a worker
(COMMON item 1; the parent reads get_session); elapsed 05:48-06:2x UTC; zero network, zero model calls.
