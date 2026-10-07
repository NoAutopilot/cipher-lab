# PREREG-D1411P5: word-coverage test of frozen T21r (+ two h alternatives) on unread p.5 numerals (written 7 Oct 2026 10:20 UTC by date -u)

Job AM-D1411P5 (LANE LANE-AM-0914, account 2). A copy of d1411p4/PREREG-D1411P4.md (itself a copy of d4p3/PREREG-D4-1411P3.md with
its Addendum A), changed only in the page, the file names, the calibration line, the crop resolution and the pooled descriptive set.
Written and pushed before any numeral of p.5 (IMG_R1411_I6599_P5.png, 4608x3456, sha1 0a102250..., per images/manifest.json) was
read by this worker or a subagent. The worker has not yet opened the image (it is not on disk; one DECODE browser login will fetch it,
as in DEF1-1411/D4-1411P3/R12A-D1411P4); it will look only at a reduced overview and debug overlays to place line centres. Nothing
below changes after the first p.5 numeral is read; any deviation is reported as a deviation. Script: d1411p5/score_p5.py (a copy of
d1411p4/score_p4.py with paths changed and the pooled set extended to p.3+p.4+p.5); before this prereg it reproduced R12A-D1411P4's
committed p.4 T21r score exactly (cover 0.5806, shuffled p99 0.4516, shifted max 0.3669) when given d1411p4/numbers.tsv.

## Tables (all frozen, no retuning after p.5 is seen)

- **T21r** (primary) = def1411/tables.py T21r, unchanged: 0 u, 1 w, 2 s, 3 y, 4 z, 5 a, 6 b, 7 c, 8 d, 9 e, 10 f, 11 g, 12 s,
  13 i, 14 k, 15 l, 16 m, 17 n, 18 o, 19 p, 20 g, 21 r, 22 s, 23 t.
- **T21r_h12** = T21r with residue 12 = h. **T21r_h22** = T21r with residue 22 = h. Same variants as D4-1411P3; the f.184 gloss
  pairs recorded there (M) did not retune any table and do not here. Script: d1411p5/score_p5.py (a copy of d1411p4/score_p4.py
  with paths changed).

## Material

p.5 numerals, every cipher-number-bearing line of the spread, left page then right page, line by line. Crops with
tools/iiif_lines.py --image (commands pasted in NOTES.md), each under 2500 px; because the R12A-D1411LA lesson found 1840-px line
crops too small for digit shapes, each numeral line is cut as left/right half-line crops (--halves style, about 900-1000 px of
source) upscaled 2x LANCZOS (still under 2500 px), so digits are about twice the size the p.4 passes saw. Two blind subagent passes (Sonnet) (numerals only,
crops only, no table, gloss or prior reading shown), one call per pass, opposite reading orders; tools/reconcile_passes.py; the
worker settles splits from the crops (one reconciliation unit). A number either pass marks doubtful is decoded but graded M.
Graphic signs, in-text figures (dates, sums, folio numbers, enclosure letters, list numerals) and clear words are not decoded.
Leading zeros read as their value. Fewer than 60 numerals: NON-TEST.

## Statistic

Word coverage = tools/judge_plaintext.py NgramModel.cover (greedy longest-word segmentation, fraction of letters covered) of
the whole decode, lexicon = NgramModel(de1600) words (count >= 2). Calibration already on file (not p.5): p.2 T21r 0.631
(shuffled p99 0.508, shifts max 0.385); p.3 T21r 0.563 (shuffled p99 0.463, shifts max 0.370); p.4 T21r 0.581 (shuffled p99 0.452, shifts max 0.367); leaf gloss 0.613.

## Controls (each can vary on coverage: permuting or shifting the numbers changes which letters form words)

For each table X, at p.5's own N: (1) shuffled-target: the p.5 number sequence permuted, 200 draws, seed 1411, decoded with
X: p99 and count >= real; (2) shifted rules X[(n+k) mod 24], k = 1..23: max and count >= real; (3) the gloss calibration
(recomputed by the script). Reported beside: de1600 real-window coverage p05/median at N.

**PASS(X)** iff cover(X) > shuffled-target p99 AND cover(X) > shifted max AND cover(X) >= gloss cover.
Beats (1) and (2) but below the gloss: "controls beaten, coverage below the leaf's own gloss". Fails (1) or (2): X not
supported on p.5 (conditional on the transcription, rule 2). The primary verdict is T21r's; a variant is preferred over T21r
only if it PASSes and its coverage exceeds T21r's.

## Letter tests (residues 12 and 22; residue 21 re-check)

As D4-1411P3: for R in {12, 21, 22}, every other residue of T21r fixed, R set to each of 24 letters, ranked by coverage
(primary) and de1600 4-gram. "h favoured at R" iff h ranks 1st on both and p.5 has >= 5 numbers at R; "s favoured" likewise;
otherwise undecided. Residue 21: r confirmed iff r ranks 1st on both with >= 5 occurrences.
Secondary, descriptive only (named in the D4-1411P3 Remaining gaps): the same h-vs-s ranking on the pooled p.3 + p.5 numbers
(d4p3/numbers.tsv + d1411p4/numbers.tsv), reported as pooled ranks; it decides nothing on its own.

## Gloss agreement (D4-1411P3 Addendum A, carried over)

Both blind passes record, per number, any letter written directly above it (blank if none). At every number with a gloss letter
both passes agree on (after reconciliation): matches with T21r (and each h variant) / glossed numbers; control 10,000
value-shuffled T21r tables (seed 1411), p99 and count >= real. "Gloss agrees with T21r" iff real > control p99 and >= 8 glossed
numbers; fewer than 8: NON-TEST. u/v, i/j and u-with-ring count as one letter. Recorded pairs do not retune any table.

## Grades (rule 4)

No grade moves unless PASS(T21r) (or a preferred variant). On PASS: p.5 numerals whose residue letter is gloss-backed (frozen
source 'gloss', or residue 21) move M -> S; alphabet-filled residues and doubtful numbers stay M. No PASS: all M. Nothing else
in the folder is regraded. A PASS is "worth a verifier", never "read" (rule 10).

## Stop rule (cost)

If the p.5 numeral block needs more than one call per pass, it is split by half-page; the worker does not start a unit that would
cross 80% of the job cap (7.5) or of the box (ends 11:38 UTC; 80% at 11:22). A partial p.5 (fewer than 60 numerals) is a NON-TEST.
