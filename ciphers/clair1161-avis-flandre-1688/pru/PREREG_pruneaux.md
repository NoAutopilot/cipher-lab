# PREREG: fr.3281 f.4 "Chiffre envoyé en Flandres à monseigneur Des Pruneaux" shape test (D2-C1161PRU, 5 Oct 2026)

Written and pushed before the key sheet's cipher rows are transcribed and before any score.

Source: Gallica ark:/12148/btv1b9060310c (BnF fr. 3281; catalogue record archivesetmanuscrits.bnf.fr ark:/12148/cc49738j,
SRU dc:rights "domaine public", "Numérisation effectuée à partir d'un document de substitution"), canvas 5 right page,
folio number "4" read on the leaf (crop pru/images/fr3281c5_L01_s2.jpg). Item 3 of the volume's contents note.

Test (same shape as N4-C1 step 4, fr16142):
1. Transcribe the sheet's letter alphabet: each plaintext letter and the shapes of its cipher symbols (Tomokiyo: two
   homophones per letter), from line crops cut by tools/iiif_lines.py (pasted in NOTES.md). Two blind passes + one
   reconciliation; disagreements stay listed.
2. Map each fr.3281 symbol to a tx/labels_v2.md label by SHAPE WORDS ONLY, or to "none". A label may collect the letters of
   several fr.3281 symbols (homophones / look-alikes): cell = (label, set of fr.3281 letters).
3. Statistic: number of matched labels whose key.tsv value is in the cell's letter set.
4. Null: 10,000 permutations (seed 1) of key.tsv's value column over the same matched labels; report mean, p99, P(null >= obs).
   The control can differ from the target on this statistic (it permutes the values the statistic compares).
5. Gate: FIT iff obs > null p99 AND obs >= 4. Otherwise NO FIT. Instrument 2 (two/two_instr.py's letter, as in
   two/tomokiyo.tsv) reported beside, not gated.
6. One test, no re-tuning after the score. A FIT licenses step 3 of the brief (decode under matched cells only); C grade only
   where the sheet gives the value directly.

Disclosure: this worker has seen key.tsv rows +, 2, 3, 4 (e, r, e, o) and two/tomokiyo.tsv (16 rows of key values) before
writing this; the shape mapping is fixed from shape words, and labels whose value this worker already knows are flagged.
Prior expectation: weak. fr.3281 is c. 1578-79 (Alençon's envoy to the States General); the Clair. 1161 item's own date is
unsettled (c. 1570 by content per earlier sections). Design per Tomokiyo: 2 homophones/letter, double-letter signs, code WORDS.
