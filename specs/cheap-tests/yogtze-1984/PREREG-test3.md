# PREREG -- yogtze-1984 spec test 3 (R8-YOG3, 6 Oct 2026, written before any scored run)

Test: anagram enumeration of the six letters Y O G T Z E (all 720 orderings) against German and English word lists.
A lexical search, not a reading. Script: `test3_anagrams.py` (this folder); output `test3_output.json`.

Word lists (fixed now, built once from tools/data corpora, lower-cased, letters a-z only after folding
ae/oe/ue/ss for umlauts/eszett; a word counts if it occurs >= 2 times in the corpus):
- de: tools/data/de20 (7 Gutenberg novels) + tools/data/de19 (3 texts).
- en: tools/data/en (3 texts) + tools/data/pg1661_holmes.txt + tools/data/pg2701_mobydick.txt.

Reading set (the folder's look-alike freedom, fixed now): base YOGTZE; YOGZE (T read as struck, as D2B-YOG);
and the six single-letter handwriting look-alike variants (letter->letter swaps only): Y->V, G->C, T->F, Z->S, E->F, O->D. So 1 + 1 + 6 = 8 strings.

Statistics, per language, per string, then summed over the reading set:
- S1 = number of distinct orderings of all the string's letters that are one word in the list.
- S2 = number of distinct orderings that split into two words, each of length >= 2, both in the list (any split point).
Headline statistic H = S1 + S2 summed over the 8 strings (orderings are counted distinct per string).

Control (can differ from the target on H by construction -- it changes the letters themselves, not only their order):
1000 draws per language of 6 *distinct* letters (YOGTZE has no repeat), sampled without replacement from that
language list's own letter frequency (token-weighted). Each draw gets the same freedom: its 5-letter "struck" form drops
its 4th letter (as YOGZE drops T, position 4), and the same look-alike map is applied to whichever of its letters are in
the map's domain, one swap at a time. Seed 20261006.

Report: target H and the control's distribution (mean, median, p05, p95) and the target's percentile P = fraction of
control draws with H <= target H. Pre-registered reading: P < 0.05 -> "fewer anagrams than random letters" (consistent with
no lexical anagram reading); P > 0.95 -> "anagram-rich" (list the hits for a person to judge, no reading claimed);
otherwise non-discriminating. Any individual one-word hit (S1 > 0) is listed whatever P is. In every case the lexical
family (tests 1-3) is logged exhausted unless a one-word hit in the base string is a common word a person would accept.
