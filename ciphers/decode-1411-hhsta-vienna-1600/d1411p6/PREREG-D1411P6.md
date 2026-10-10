# PREREG-D1411P6: word-coverage test of frozen T21r (+ two h alternatives) on unread p.6 numerals, copy spans excluded (written 10 Oct 2026 02:5x UTC by date -u)

Job D1411-P6 (LANE FAMILY-A2n, account 2). A copy of d1411p5/PREREG-D1411P5.md, changed in the page, the file names, the calibration
line, and one addition required by AM-D1411V: **numbers aligning to an already-read page are excluded before scoring** (the copy mask).
Written and pushed before any numeral of p.6 (IMG_R1411_I6600_P6.png, 4608x3456, sha1 0f597628..., per images/manifest.json) is read
by this worker or a subagent. The image is not on disk; one DECODE browser login will fetch it. The worker will look only at a reduced
overview and debug overlays to place line centres (and, for the prior-work 2-leaf check, to note any clear text or gloss on the leaf).
Nothing below changes after the first p.6 numeral is read; any deviation is reported as a deviation.

Script: d1411p6/score_p6.py (a copy of d1411p5/score_p5.py, paths changed, plus copy_mask from d1411v/rescore_v.py generalised to every
prior page). Before this prereg, `score_p6.py --reproduce-p5` reproduced AM-D1411V's p.5 independent set exactly (mask against p.2
only, as rescore_v.py: N=136, five spans 10/7/46/15/52, T21r cover 0.5882, h12 0.5882, h22 0.5441).

## Tables (all frozen, no retuning after p.6 is seen)

- **T21r** (primary) = def1411/tables.py T21r, unchanged: 0 u, 1 w, 2 s, 3 y, 4 z, 5 a, 6 b, 7 c, 8 d, 9 e, 10 f, 11 g, 12 s,
  13 i, 14 k, 15 l, 16 m, 17 n, 18 o, 19 p, 20 g, 21 r, 22 s, 23 t.
- **T21r_h12** = T21r with residue 12 = h. **T21r_h22** = T21r with residue 22 = h (beside; h12 had no independent support on p.5).

## Material

p.6 numerals, every cipher-number-bearing line of the spread, left page then right page, line by line. Crops as AM-D1411P5:
line centres placed on a reduced overview / tools/iiif_lines.py --image debug overlay (commands pasted in NOTES.md), then each numeral
line cut into left/right half-line crops by d1411p6/cut_halves.py (a copy of d1411p5/cut_halves.py), upscaled 2x LANCZOS, each under
2500 px; every _a/_b boundary checked against the overview before the passes (the AM-D1411P5 split lesson). Two blind Sonnet
passes (numerals only, crops only, no table, gloss or prior reading shown), one call per pass, opposite reading orders;
tools/reconcile_passes.py; the worker settles splits from the crops (one reconciliation unit). A number either pass marks doubtful
is decoded but graded M. Graphic signs, in-text figures (dates, sums, folio numbers) and clear words are not decoded.

## Copy mask (applied before scoring)

copy_mask (score_p6.py): for each already-read page sequence -- p.1 (residue/numbers.tsv p1L), p.1 gloss lines (gloss/pairs.tsv),
p.2 (residue p2L + def1411 p2Lb/p2R), p.3 (d4p3), p.4 (d1411p4), p.5 (d1411p5), each in its numbers.tsv order --
difflib.SequenceMatcher(autojunk=False) against the whole p.6 number sequence; matching blocks of >= 4 numbers; consecutive blocks
whose gaps are <= 3 numbers on both sides merge into one span; every p.6 number inside a span is masked; the union over pages is
excluded. The remaining **independent** numbers are the registered material. Calibration of the rule before p.6 (descriptive,
run on disk): p.3 against p.1/p.1 gloss/p.2 masks 0 of 311 (no chance blocks); p.4 against p.1/p.1 gloss/p.2/p.3 masks 136 of 248
(p.4 right page aligns to p.1 and the p.1 gloss lines -- a further copy, logged in NOTES; it does not change p.4's registered result,
which was already below the gloss). The all-p.6 (unmasked) coverage is reported beside, descriptive only.
Independent N < 60: NON-TEST.

## Statistic

Word coverage = tools/judge_plaintext.py NgramModel.cover (greedy longest-word segmentation, fraction of letters covered) of the
independent decode, lexicon = NgramModel(de1600) words (count >= 2). Calibration on file: p.2 T21r 0.631; p.3 0.563; p.4 0.581;
p.5 independent 0.588 (AM-D1411V); leaf gloss 0.613.

## Controls (each can vary on coverage)

For each table X, at the independent set's own N: (1) shuffled-target: the independent sequence permuted, 200 draws, seed 1411:
p99 and count >= real; (2) shifted rules X[(n+k) mod 24], k = 1..23: max and count >= real; (3) the gloss calibration (gaps150
gloss_text, recomputed). Reported beside: de1600 real-window coverage p05/median at N.

**PASS(X)** iff cover(X) > shuffled p99 AND cover(X) > shifted max AND cover(X) >= gloss cover. Beats (1) and (2) but below the
gloss: "controls beaten, coverage below the leaf's own gloss". The primary verdict is T21r's; a variant is preferred only if it
PASSes and its coverage exceeds T21r's.

## Letter tests (residues 12, 21, 22), on the independent set

As AM-D1411P5: R set to each of 24 letters, ranked by coverage and de1600 4-gram; "h favoured at R" iff h ranks 1st on both with
>= 5 numbers at R; residue 21 r confirmed iff r 1st on both. Pooled p.3+p.4+p.5+p.6-independent ranks: descriptive only.

## Gloss agreement (Addendum A, carried over), on the independent set

Both passes record any letter written directly above a number; at pass-agreed gloss numbers: matches with T21r / glossed; control
10,000 value-shuffled T21r tables (seed 1411), p99. "Agrees" iff real > p99 and >= 8 glossed; fewer: NON-TEST. Pairs retune nothing.

## Grades (rule 4)

No grade moves unless PASS(T21r) (or a preferred variant) **on the independent set**. On PASS: independent p.6 numerals graded 'ok'
(both passes agree, no flag) whose residue letter is gloss-backed (tables.py source 'gloss', or residue 21) move M -> S; masked copy
numbers, alphabet-filled residues and doubtful numbers stay M. No PASS: all M. Nothing else in the folder is regraded. A PASS is
"worth a verifier", never "read" (rule 10).

## Stop rule (cost)

Cap USD 6.5, box 02:45-04:35 UTC 10 Oct (80% at 04:13). The worker does not start a unit that would cross 80% of either. A partial
p.6 with fewer than 60 independent numerals is a NON-TEST.
