# BIRAGO-NUM2 crib pre-registration (written 02 Oct 2026 22:48 UTC, before any crib was scored)

Stream: num/pooled_tokens.txt (BIRAGO-NUM phase.py output, f.119 + f.100r jointly: 476 pairs, 64 types). Each line is
a run; one-digit tokens (strays) and lines that are only the delimiter 76 are breaks. A crib never crosses a break.
Spelling: lower case, v->u, j->i, k->c, y->i, x->s, w->u, accents dropped (period Italian writes u for v: "uerità" in f.100r).

Cribs (all dragged over the WHOLE pooled stream, both letters jointly, every pair offset):
 1 carmagnola   2 bellagarda   3 bellegarda   4 ualletta   5 sauoia   6 turino
 7 duca         8 regina       9 ugonotti    10 centurione 11 maresciale 12 maesta
(1-8 from the brief; 9-11 from f.100r's own clear text, "Giulio Centurione", "il Maresciale di logis"; 12 "Sua Maestà".)

Placement admissible: the crib's codes are consistent (one code never stands for two letters within the placement).
Score of a placement: induced key M (code -> letter) applied to every pair token in both letters; sum over every adjacent
token pair (same run) with both codes in M, excluding the pairs inside the placement itself, of
log P(b|a) - log P(b) from an it16dip letter-bigram model (add-0.5). Statistic per crib = max score over admissible placements.
Null: the same crib dragged over the stream with pair tokens permuted across positions (run lengths and break positions
kept), 200 permutations, same statistic.
Accept a crib placement only if (a) the real max exceeds all 200 permuted maxima (p < 1/201) and (b) the accepted
placements of different cribs agree with each other on every shared code (joint consistency). With 12 cribs the
expected number of chance accepts at this threshold is about 0.06.
Power control (rule 3, run before reading the target result as a negative): synthetic it16dip text, 476 pairs, one
homophonic key of 40 cells (also 55), 5% stray digits, phased by the same phase.py em(); the crib inserted once
(and, separately, twice); the same drag + 200-permutation test; report the share of trials where the true placement is
accepted, per crib length. A target "no accept" is reported only beside that number.
Step 2 (joint anneal) runs only if accepted cribs fix >= 8 pair types.
