# PREREG-D4-1411P3: word-coverage test of frozen T21r (+ two h alternatives) on unread p.3 numerals (written 6 Oct 2026 12:46 UTC by date -u)

Written and pushed before any numeral of p.3 (IMG_R1411_I6597_P3.png, 4608x3456 double spread, sha1 509fe691... matching
images/manifest.json) was read by this worker or a subagent. The worker has looked only at a 1/4-size overview to place line
centres. Nothing below changes after the first p.3 numeral is read; any deviation is reported as a deviation.

## Tables (all frozen, no retuning after p.3 is seen)

- **T21r** (primary) = def1411/tables.py T21r, unchanged: 0 u, 1 w, 2 s, 3 y, 4 z, 5 a, 6 b, 7 c, 8 d, 9 e, 10 f, 11 g, 12 s,
  13 i, 14 k, 15 l, 16 m, 17 n, 18 o, 19 p, 20 g, 21 r, 22 s, 23 t.
- **T21r_h12** = T21r with residue 12 = h. **T21r_h22** = T21r with residue 22 = h. (GAPS150: the recurring "5"-like gloss
  form at residues 12/22 read s at M, h the alternative; DEF1-1411's post-hoc note. Two single-residue variants, not chosen
  by looking at which residue produced which p.2 word.) Script: d4p3/score_p3.py.

## Material

p.3 numerals: left page (f.183v?, lower block y ~2050-3000) and right page (f.184r, y ~380-3300). Crops with
tools/iiif_lines.py --image (command pasted in NOTES.md), each under 2500 px. Two blind Sonnet subagent passes (numerals only,
crops only, no table, gloss or prior reading shown), one call per pass; tools/reconcile_passes.py; the worker settles splits
from the crops (one reconciliation unit). A number either pass marks doubtful is decoded but graded M. Graphic signs, in-text
figures (dates such as "13", "15 huius", sums, folio numbers, enclosure letters) and clear words are not decoded. Leading
zeros read as their value. Reading order: left page then right page, line by line. Fewer than 60 numerals: NON-TEST.

## Statistic (a different instrument from the retired 4-gram judge)

Word coverage = tools/judge_plaintext.py NgramModel.cover (greedy longest-word segmentation, fraction of letters covered) of
the whole decode, lexicon = NgramModel(de1600) words (count >= 2; 10,487 words). Calibration computed BEFORE this prereg on
material already scored (not p.3): DEF1-1411's p.2 T21r decode 0.631, its shuffled-target mean 0.428 / p99 0.508, shifted max
0.385; the leaf's 62-letter period gloss 0.613; de1600 real windows p05 0.872; letter-shuffled real windows mean 0.430.
(Descriptive secondary: same with lexicon de1600+la17, 30,490 words.)

## Controls (each can vary on coverage: permuting or shifting the numbers changes which letters form words)

For each table X, at p.3's own N: (1) shuffled-target: the p.3 number sequence permuted, 200 draws, seed 1411, decoded with
X: p99 and count >= real; (2) shifted rules X[(n+k) mod 24], k = 1..23: max and count >= real; (3) the gloss calibration
(recomputed by the script). Reported beside: de1600 real-window coverage p05/median at N.

**PASS(X)** iff cover(X) > shuffled-target p99 AND cover(X) > shifted max AND cover(X) >= gloss cover.
Beats (1) and (2) but below the gloss: "controls beaten, coverage below the leaf's own gloss". Fails (1) or (2): X not
supported on p.3 (conditional on the transcription, rule 2). The primary verdict is T21r's; the h variants are reported
beside it and a variant is preferred over T21r only if it PASSes and its coverage exceeds T21r's.

## Letter tests (residues 12 and 22; residue 21 re-check)

For each residue R in {12, 21, 22}: hold every other residue of T21r fixed, set R to each of the 24 letters (a b c d e f g h i
k l m n o p q r s t u w x y z), score the full decode by coverage (primary) and by de1600 4-gram score (as DEF1-1411).
"h favoured at R" iff h ranks 1st of 24 on both statistics and p.3 has >= 5 numbers at residue R; "s favoured" likewise;
otherwise undecided. Residue 21: r confirmed iff r ranks 1st on both with >= 5 occurrences.

## Grades (rule 4)

No grade moves unless PASS(T21r) (or a preferred variant). On PASS: p.3 numerals whose residue letter is gloss-backed (frozen
source 'gloss', or residue 21) move M -> S; alphabet-filled residues and doubtful numbers stay M. No PASS: all M. Nothing else
in the folder is regraded. A PASS is "worth a verifier", never "read" (rule 10).
