# PREREG-GAPS146: frozen mod-24 residue rule, tested on unglossed numerals (written 3 Oct 2026 ~15:08 UTC)

Written and pushed before any unglossed numeral of R1411 was read by this worker or a subagent. Only gloss/pairs.tsv
(GAPS141, 62 glossed pairs of p.1 L01-L05) was used to build the rule.

## The rule (frozen; residue/rule.py, residue/frozen_table.tsv)

letter(n) = T[n mod 24], T built from the grade-C glossed pairs only (pairs with "?" in the number or grade M excluded):
- a residue seen in C pairs takes its majority gloss letter (tie -> the alphabet letter below; none occurred);
- an unseen residue takes the 24-letter alphabet a b c d e f g h i k l m n o p q r s t u w x y z laid on residues with a = 5.
On-page conflicts handled as declared: 56 (n/d) votes once for each under residue 8, which goes d (4 vs 1); 66 (u-ring/o)
votes under residue 18 with 42 = o, which goes o (2 vs 1); 22 = t (C) votes under residue 22 with 70 = s and 94 = s, which
goes s (2 vs 1); 22 = s at L01 pos 16 is grade M and excluded.
Frozen T: 0 u, 1 w, 2 s, 3 y, 4 z, 5 a, 6 b, 7 c, 8 d, 9 e, 10 f, 11 g, 12 s, 13 i, 14 k, 15 l, 16 m, 17 n, 18 o, 19 p,
20 g, 21 z, 22 s, 23 t. Declared weakness: no residue yields h or r (the glosses put s on 12 and z on 21, where the
alphabet has h and r), so a correct German decode under T will still show gaps where h/r stand; that is part of what is
tested and is not repaired after the score.

## New material

The unglossed numerals of p.1 below the glossed lines (lower block), cut with tools/iiif_lines.py --image; if the block
holds fewer than about 150 numbers, the cipher numerals of one further page (p.2 or p.3, whichever carries more numeral
runs in its thumbnail) are added. Two blind Opus 5.5 passes of the numerals only (one call each, crops only), reconciled
with tools/reconcile_passes.py, the worker settling splits from the crops. A number either pass marks doubtful is decoded
but graded M. Graphic marks and clear German words are not decoded; each cipher run is decoded as one string, runs joined
in reading order. Leading zeros (04, 09) are read as their value.

## Score and gate

Scorer: tools/judge_plaintext.py NgramModel on tools/data/de17 (1630-60 chancery German; the closest era-matched German
corpus on disk; de16 is a model-composed 8.5 KB text). Statistic: mean log10 4-gram probability per letter of the decode.
Controls, all at the decode's own length N:
1. judge: real_p05 and null_p99 from tools/judge_plaintext.py (200 real windows, 200 letter-shuffled windows); real_p01
   reported beside it. de17's own leave-one-file-out false-negative rate (tools/data/de17/holdout_*.log) is 38.2 pct at
   N=300 and 41.4 pct at N=1090 with per-fold spread 4.0-97.0 pct and 13.0-100.0 pct: a FAIL on (1) alone is of unknown
   reliability (CLAUDE.md rule 3, es17c/en paragraphs) and is logged as "judge cannot decide", not as a negative.
2. shuffled-target: the transcribed number sequence permuted (200 draws, seed 146) and decoded with T. Can differ from
   the real decode on this statistic (order changes 4-grams).
3. shifted rules: letter(n) = T[(n + k) mod 24] for k = 1..23. Can differ (changes every letter).
PASS iff score > judge null_p99 AND score > real_p05 AND score > shuffled-target p99 AND score > max over the 23 shifted.
Beats (2) and (3) but FAILs (1): "rule favoured over its controls, judge cannot decide" -> no reading-ready flag, the row
names a better corpus or more material as the next step. Fails (2) or (3): the frozen rule is not supported on new text
(conditional on this transcription, rule 2); status stays open (rule 5).
A PASS gets a "reading ready" ROOM line for a separate verifier, no status change. Grades (rule 4): glossed numbers C
(period gloss), unglossed numbers S only on PASS, else M; doubtful numbers M.
