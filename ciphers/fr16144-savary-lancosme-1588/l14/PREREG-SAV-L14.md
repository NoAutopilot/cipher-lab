# PREREG SAV-L14 (15 Oct 2026, written 03:0x UTC by date -u, before any gloss was read or scored)
Question: is the L14 left-margin gloss on c251-c252 (f.123r-v, letter dated "xxx^e d'Apvril 1586") a decipherment of a passage
that Charriere IV pp.499-502 ("Constantinople, 30 avril 1586") prints in clear?
Material: gloss read on native line crops (one Sonnet read + one Sonnet checker, crops in scratchpad, not committed);
print = l14/print_charriere_l14.txt (main column only).
Normalisation (PX-BRODEC, both sides identically, tools in l14/collate.py): lowercase; strip accents; v->u, j->i, y->i; drop
punctuation, apostrophes, illegible marks "[..]"; expand amb/ambr/amb' -> ambassadeur, seig/sr seig -> seigneur, G. S. -> grand
seigneur, V. M. -> vostre maieste, S. M. -> sa maieste; "&" -> et.
Statistic: word-level gloss recall = |LCS(gloss words, print words)| / |gloss words| over the best contiguous print window
(DP over the whole print, i.e. global LCS), and the matched print span.
Control (can differ: same statistic, different printed text of the same sender, register and length class): the same gloss
against Charriere IV's "Constantinople, 14 et 28 mai 1586" letter main column (first ~same word count), and against the gloss
words shuffled (20 shuffles, mean) vs the 30 Apr print.
Decision: DECIPHERMENT-OF-PRINT if recall(30 Apr) >= 0.50 AND >= recall(14/28 May control) + 0.25 AND >= shuffle mean + 0.25.
UNRELATED if recall(30 Apr) <= control + 0.10. Between: UNDECIDED (report numbers). Gloss tokens graded by the readers'
agreement; only words both readers agree on enter the score (disagreed words reported separately).
No key edit, no sign alignment in this job.
