# PREREG-MANT0136B (9 Oct 2026, 16:0x UTC by date -u, written before any pass result was read and before any score; LANE FAMILY-A2j account 2)

Leaf: HStA Dresden 10026 Loc. 694/08, film frame 0136 (fullsize 0136.jpg, one GET 9 Oct 2026 15:57 UTC; film card "Aufnahme Einheit
0137"), 4260x3938, sha256 prefix d7a77727676ea3d3 (= MANT-CEN2 inv08e.tsv row), stamp 102 (right page), Manteuffel to Flemming.
NOT 694/09 0136 (the "chiffre du proces" leaf of MANT-0136).
Premise (before this file): Acta Borussica, Behoerdenorganisation I (1894), IA diebehrdenorgan01posngoog _djvu.txt, p.212, "am 18. Juni
schrieb Manteuffel:" quotes this leaf's text with ellipses and the cipher names in clear ("[Blaspil et Krautt] se sont raccommodes ... a
l'exclusion de Grumbkow ... nous soulames chez Blaspil ... viennent originairement du Prince d'Anhalt ... Blaspil est mieux en cour ...
grace a Kameke le Grand-Maitre, et que le personnage que l'autre Kameke a joue"). So the leaf carries two known answers: its own
interlinear gloss and the editor's print. A key test, not a reading.
Question: does key.tsv (origin/main 7b6fcdbce) read this leaf's code runs the way (a) the leaf's own interlinear gloss and (c) the 1894
print read them?
Token count on the image before planning (worker eye, 16:00 UTC): about 64 code tokens in 18 run crops (left page ~19, right ~45); over 30,
so the leaf is gated on its own (no pooling with 0089), per page and pooled as below.

Protocol = PREREG-MANT0474 exactly (statistic, control, gate rule), with these inputs:
- codes: two blind Sonnet passes over the 18 run crops f0136_08/crops/c0136*_L01.jpg (both pages in one call per pass: the crops are short
  strips, 18 in all, as MANT-0089 did; pass B in reverse order) -> passA.tsv, passB.tsv; reconciled by this worker from the image where they
  disagree -> f0136_08/ciphertext.tsv, before any span is attached and before any score. Disclosure: this worker has seen key.tsv, the
  leaf's glosses at preview scale and the BO I print; digits are settled from the image, never from key values; doubtful ones marked low.
- gloss: ONE blind Sonnet gloss pass (gloss.tsv; V-BRANDT rule), used exactly as that pass wrote it (letters only; '?' letters dropped);
  this worker does not correct, complete or settle any gloss word. A crop the pass marks NONE has no gloss span.
- spans (gate a): f0136_08/gloss_spans.tsv, one row per gloss note. Where the pass gives several notes for one crop (' | '), they are
  assigned left to right to the code sub-runs of that crop (sub-runs = the [..] slots of runs.tsv, separated by clear words); if the
  number of notes and sub-runs differ, the crop is one span with the notes joined in order. Spans set by position only.
- spans (gate c, print): f0136_08/print_spans.tsv, one row per code sub-run that the BO I p.212 quotation covers, with the printed word(s)
  standing at that place in the quoted sentence as the "gloss" text (OCR of the djvu, normalised by eye only for OCR errors in letters,
  quoted in the row). Expected (from the print, before any pass): L02 'Grumbkow', L03 'Blaspil', R01 'Prince d'Anhalt', R07 'Blaspil',
  R08 'Kameke le Grand-Maitre', R09 'Kameke'. A sub-run the print elides ('...') or brackets ('[Blaspil et Krautt]' replaces 'Ils')
  is not a print span. Caveat stated now: the editor may have used the same interlinear gloss, so (c) is not independent of (a); it is
  reported as a second known-answer row, not as independent corroboration.

Statistic S: exactly f0474_08/gloss_gate.py's (copied as f0136_08/gloss_gate.py, seed 136; print rows scored by the same code on
print_spans.tsv). Name codes whose key value is a whole word (160 Manteuffel, 260 Kameke, 283 prince) match only when the gloss/print
spells that whole value; an abbreviated gloss ('Mant') scores them as a miss: S is a lower bound, as on 0474.
Control (rule 3): key.tsv values permuted over its codes, 1000 draws, seed 136, same spans and alignment (the permutation changes the
value-to-code assignment, which is what S measures: the control can differ from the target).
Gate (a), per page (L, R) and pooled; gate (c) pooled: PASS if S > p99 AND S >= 0.5 x keyed code tokens in the spans; fewer than 10 keyed
tokens = too short (neither). Deciding row for grades: gate (a) pooled (this leaf's pre-registered deciding row, as 0089). A span's codes
are grade C only if its row PASSes; everything else M.
Cross-witness (descriptive, no gate) -> f0136_08/candidates.tsv, never key.tsv: codes outside key.tsv (expected 254, 199 and any > 401),
MANT-0494's held 231-715 if present, rule-4 conflicts at any keyed code whose slot disagrees with its gloss/print letters.
Gate (b) (unglossed >= 15-token run): none expected (every long run is glossed or printed); not run if none.
