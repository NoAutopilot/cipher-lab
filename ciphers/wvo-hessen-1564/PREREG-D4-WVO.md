# PREREG-D4-WVO -- crib-placement test on f.23 against settled/key.tsv (D4-WVO, 8 Oct 2026, pushed before any score)

Question: do the crib words listed in `wvo1111_transcription.md` "Crib candidates against the 1109 enclosure" (written
6 Oct 2026 by R8-WVO1111, before the interlinear gloss was noticed and before the settled key existed) occur in the f.23
cipher stream under the settled key more than words of the same lengths taken from unrelated period German text?
Not a reading: the leaf's own gloss is the period decipherment; this test asks whether the 1111/1109-Inhoud cribs are
in the enciphered text (the content question), and lists any sign values a placement would imply (grade I, not applied).

Stream: `settled/ciphertext.tsv`, rows C01-C10 concatenated in order (words run across rows), 258 tiles.
Key: `settled/key.tsv`; fixed tokens = grade C with a letter; every M, unvalued, or X-* (aside/bad-cut) tile is a wildcard.
Folding on both sides: lowercase, v->u, j->i, y->i, w kept.
Crib list (14 words, `d4wvo/crib_list.tsv`): zeitungen gemahlin frucht leibs gesegnet widderumb schwanger sterben
pestilentz plage sachsen augustus franckreich lothringen (candidates 1, 2, 4, 5 of that table, its spellings).

Instrument: `tools/crib_list_fit.py` (shared tool), anchor free over the whole stream, fixed grades C, with a new option
`--wild-span 1` (a wildcard tile consumes exactly one letter: the gloss alignment is one letter per sign; default (1,2)
kept for nomenclators). A word PLACES when the tool's own per-candidate fit rule holds at its best placement, tool
defaults: agree >= 0.6 x length, mismatch <= 1, fit (agree - mismatch) >= 6.
Statistic T = number of list words that place.

Controls (1000 draws each, seed 1564):
- P (positive, instrument power; read FIRST): 14 words from the leaf's own gloss (`r10tx/gloss_r10.tsv`), one per
  target word, chosen by rule: for each target length L in list order, the first unused gloss word (row order, folded,
  letters only) of length L, else L-1, L+1, L-2, L+2 ... Its null = control A built at the positive list's lengths.
  Gate P: T_pos > p95 of its null. If P fails: CONTROL BELOW GATE, the target T is reported but not interpreted (non-test).
- A (wrong-text crib): each target word replaced by a random word of the same length from the de1600 corpus vocabulary
  (`tools/data/de1600/*.gz`, Bezold Johann Casimir letters 1575-86 and Briefe und Acten 1599-1610; folded, letters only,
  the 14 target words excluded). Can differ from the target: different words fit different spots.
- B (shuffled key): the letters of the C-graded codes permuted among those codes, true crib list. Can differ: a placement
  needs the true letter at the true code.
Gate (target): PASS iff T_target > p95(A) and T_target > p95(B); FAIL otherwise. Ties at p95 are FAIL.
Reported besides: per-word best fit/placement, and for a placing word the M/U/X tiles it covers with the implied letter
(grade I, not applied to key.tsv).
