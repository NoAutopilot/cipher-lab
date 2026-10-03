# A2-RAA7 crib pre-registration (written 3 Oct 2026 ~01:52 UTC, committed before any crib was scored)

Instrument: tools/crib_pattern.py (shared tool, H28) on the 370 leaf-2 cells (code = top digit + bottom digit,
ciphertext_209_leaf2_full.tsv kind c; struck columns kind x dropped; the one uncertain cell "?2" made --wild).
Groups: the cell stream is split at every clear-text insertion (kind w) and at the L13/L16 break (clear lines L14-L15),
so no placement crosses clear text. Corpus nl20 (tools/data/nl20, era-mismatched 1880s-1900s; rule 3 caveat).

Cribs (folded j->i, v->u by the tool), one run each, chosen from the clear words on the leaves, the item's own
catalogue title and the period's formula vocabulary, before looking at any placement:
  asiatische bataafsche republiek engelschen gouvernement commissarissen nederlandsche bezittingen
  onderhandelingen staatsbewind batavia prediger grasveld elout vrede
Two modes per crib: strict (no homophones; masc) and --homophones. 600 shuffled-order controls per run, seed 1.

Control first (synthetic Dutch cell-cipher, matched): 370 nl20 letters cut into the target's own group lengths, one
crib planted inside the longest group, enciphered with a random one-to-one map onto 24 two-digit cells (strict mode)
and with a homophonic map using the target's own cell-count profile (--homophones mode). Planted cribs: asiatische,
bataafsche, gouvernement (three controls per mode).
Control passes a mode when, for every planted crib, the planted start is the top-scoring placement AND its best score
has at most 30/600 shuffles at or above. If a mode's control fails, that mode licenses nothing on the target.

Target hit (per crib, per mode; Bonferroni over 15 cribs x 2 modes = 30 tests, alpha 0.05): real best score with
0/600 shuffles at or above. A hit is a candidate anchor for a partial key, never a reading; no reading is written
unless a hit occurs in a mode whose control passed.
