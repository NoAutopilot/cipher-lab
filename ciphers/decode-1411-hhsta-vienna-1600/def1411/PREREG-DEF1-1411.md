# PREREG-DEF1-1411: two frozen residue tables tested on unused numerals (written 5 Oct 2026 ~21:30 UTC by date -u)

Written and pushed before any numeral of the new material was read by this worker or a subagent. Nothing below is changed
after the first new numeral is read; any deviation is reported as a deviation.

## The two tables (both frozen)

- **T** = residue/frozen_table.tsv (GAPS146, unchanged): letter(n) = T[n mod 24]; 0 u, 1 w, 2 s, 3 y, 4 z, 5 a, 6 b, 7 c,
  8 d, 9 e, 10 f, 11 g, 12 s, 13 i, 14 k, 15 l, 16 m, 17 n, 18 o, 19 p, 20 g, 21 z, 22 s, 23 t.
- **T21r** = T with residue 21 read **r** instead of z (the GAPS150 blind re-read leaned to r at L confidence; the exploratory
  rise on the 176 GAPS146 numbers was seen after the fact, so those numbers are contaminated for this comparison and are
  NOT scored here). Every other residue identical to T. Script: def1411/tables.py.

## New material (never read before by any pass in this folder)

Unused cipher numerals of p.2 (IMG_R1411_I6596_P2.png, 4608x3456 double spread): the left page below the GAPS146 p2L crops
(those covered region y 100-1300 of x 700-2440 at full size, 11 lines) and the right page (f.183). Crops cut with
tools/iiif_lines.py --image (command pasted in NOTES.md), each crop under 2500 px. Two blind Opus subagent passes (numerals
only, crops only, no table, no gloss, no prior reading shown), reconciled with tools/reconcile_passes.py, the worker settling
splits from the crops (one reconciliation unit). A number either pass marks doubtful is decoded but graded M. Graphic signs,
in-text figures (sums, dates, folio numbers) and clear words are not decoded. Leading zeros read as their value. Each line's
numerals joined in reading order.

If fewer than 60 numerals result, the gate reads NON-TEST (too short) and nothing is concluded.

## Judge and controls (de1600 raw, tools/judge_plaintext.py NgramModel, as CORP-DE16/GAPS157)

The language judge was retired as a gate for this leaf by GAPS157 (rule 3 third-attempt clause: the leaf's own gloss scores
-1.423 under de1600, below every genuine window). It is therefore used only *relative to the gloss calibration*, never
against real_p05 alone (rule 3 ZX-DEC349 shape). Statistic: mean log10 4-gram probability per letter of the whole decode.

0. **ARM-C1 judge-void check, run before the target is scored:** one shuffled copy of the new numerals (seed 1411) decoded
   with T and with T21r, scored with tools/judge_plaintext.py (de1600). If either shuffled decode PASSes the judge
   (score > real_p05 and > null_p99), the judge is void as a gate here, the run stops at a NON-TEST, and the target decodes
   are reported only as numbers.
For each table X in {T, T21r}, at the decode's own N:
1. shuffled-target: the new number sequence permuted, 200 draws, seed 1411, decoded with X; p99 and count >= real.
2. shifted rules: X[(n+k) mod 24], k = 1..23; max and count >= real.
3. gloss calibration: the leaf's own 62-letter period gloss under de1600 = -1.423 (CORP-DE16; recomputed by the script).
   Reported beside: real_p05, null_p99, gloss letter-shuffled mean.
**PASS(X)** iff score(X) > shuffled-target p99 AND score(X) > shifted max AND score(X) >= gloss score (the decode is at least as
close to period prose as the leaf's own genuine gloss as transcribed) AND step 0 did not void the judge.
Beats 1 and 2 but below the gloss: "controls beaten, judge cannot decide" (as GAPS146/150/157).
Fails 1 or 2: the table is not supported on this new text (conditional on the transcription, rule 2); status stays open.

## T vs T21r (residue 21 only)

Residue-21 letter test on the new decode: hold every other residue of T fixed and set residue 21 to each of the 24 alphabet
letters in turn (a b c d e f g h i k l m n o p q r s t u w x y z), scoring each full decode. **r is favoured** iff the r
variant ranks first of 24 AND the number of new numerals with residue 21 is >= 5; z is favoured iff z ranks first under the
same count condition; otherwise "residue 21 undecided". This control can differ from the target on this statistic (it changes
the letter at every residue-21 position). Reported: rank of r, rank of z, the residue-21 count.

## Grades (rule 4)

No grade moves unless PASS(X). On PASS(X) for exactly one table (or for both, X = the one favoured by the residue-21 test, else
T): new numerals whose residue letter in X is gloss-backed (frozen_table source 'gloss', or residue 21 under the r test) move
M -> S; residues filled from the alphabet stay M; doubtful numbers stay M. On no PASS: all new numerals M. The 176 GAPS146
numbers and the 62 gloss pairs are not regraded by this job. A PASS is "worth a verifier", never "read" (rule 10): one ROOM
"reading ready" line, no status change by this worker.
