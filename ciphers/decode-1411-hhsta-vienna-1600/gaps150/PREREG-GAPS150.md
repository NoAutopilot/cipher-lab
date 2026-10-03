# PREREG-GAPS150: blind re-read of the gloss letters behind residues 12, 21, 2, 22; old vs revised table (written 3 Oct 2026 ~15:30 UTC)

Written and pushed before the re-read subagent was called and before any revised decode was computed.

## Why
GAPS146 (residue/PREREG-GAPS146.md) froze T[n mod 24] from the 54 grade-C gloss pairs. After its score it noted (post hoc)
that its decode of 176 unglossed numbers reads more like German if residue 21 (glossed z) were r and residues 6/12
(alphabet b, glossed s) were h. That idea came from those 176 numbers, so any revised-table score on them is selection-
contaminated (see Gate). The only new evidence this step adds is an independent, blind look at the gloss letters themselves.

## Blind re-read (one Opus 5.5 subagent call)
Input: the 9 existing gloss crops of lines L01, L03, L05 (images/p1g_crops/p1g_L0{1,3,5}_s{1,2,3}.jpg) and a neutral
letter-shape sheet (text: how a German chancery/Kurrent hand of c.1600 writes a b c d e f g h i k l m n o p r s(long and
round) t u w z, every letter described on equal terms). No candidate words, no table, no decode, no previous gloss reading
is shown. The subagent is asked, for 15 probe positions given only as "line, n-th number, the number's value", which
letter is written above that number (free answer, one letter or "?" plus a confidence H/M/L and a one-line shape note).
Probe positions (9 in question + 6 decoys the agent cannot tell apart):
L01: 2nd (81), 5th (70), 6th (22), 9th (21), 10th (32), 12th (93), 16th (22?);
L03: 2nd (41), 4th (50), 6th (36), 9th (94), 12th (56);
L05: 2nd (29), 4th (12), 6th (68).
In question: residue 21 = L01 9th (21), L01 12th (93); residue 12 = L03 6th (36), L05 4th (12); residue 2 = L03 4th (50);
residue 22 = L01 5th (70), L01 6th (22), L01 16th (22?), L03 9th (94).
Decoy check: if fewer than 5 of the 6 decoys (expected e, d, n, d, a, g) are read as the table/gloss letter, the re-read is
declared unreliable and the table is NOT revised (result logged, no revision).

## Rule for changing the frozen table (only rule; decided now)
For each residue in question (2, 12, 21, 22), take the blind read letters at its C-graded probe positions (L01 16th is M and
counts only as a tie-breaker). The residue's letter changes to X only if X is read at H or M confidence at a strict majority
of its C positions (residue 21: both of 2; residue 12: both of 2; residue 2: its 1; residue 22: at least 2 of 3) and X
differs from the frozen letter. "?" or L confidence counts as agreeing with the frozen table. Residue 6 (b) has no gloss
and cannot be changed by this step (declared: the "b may be h" idea stays untested here). No other residue changes.
If no residue changes, the revised table equals the frozen table and only one decode is reported.

## Score
Same scorer and corpus as GAPS146 (tools/judge_plaintext.py NgramModel on tools/data/de17; tools/data/de16 is a model-
composed 8.5 KB text, not a corpus; no 16th-c./c.1600 German chancery or newsletter corpus exists in tools/data, so de17 is
the only option). Same 176 numbers (residue/numbers.tsv), same controls at the decode's own N: judge real_p05, real_p01,
null_p99; shuffled-target (200 draws, seed 150); 23 shifted rules. de17's leave-one-file-out spread is reported beside
every score: N=300 FN 4.0-97.0 pct per fold (blended 38.2), N=1090 13.0-100.0 pct (blended 41.4). The judge is of unknown
reliability here (rule 3) and will be called so.
Calibration (rule 3, ZX-DEC349): the leaf's own period gloss text (the 62 gloss letters of L01-L05 in reading order, as
reconciled in gloss/pairs.tsv, u-ring as u; and, if the table is revised, the same text with the re-read letters) is
scored through the same judge at its own N beside the decodes, with its own letter-shuffled controls.

## Gate
PASS (each table separately) iff score > null_p99 AND > real_p05 AND > shuffled-target p99 AND > max of the 23 shifted.
Frozen table: a PASS gives a "reading ready" ROOM line. Revised table: because the residues to re-read were chosen after
reading these 176 decodes, a PASS is reported as "revised table passes on contaminated material" and gives NO reading-ready
flag; it names the fresh p.2 numerals (next job) as the test. A revised score better than the frozen one is descriptive only.
Grades (rule 4): the 176 numbers stay M unless the frozen table PASSes; gloss pairs re-read by the subagent keep their C
grade only where the re-read agrees with gloss/pairs.tsv; a disagreement is logged as a data conflict (rule 4), both readings
kept.
