# PREREG BAL-169C (account 4, LANE DEFAULT-A4-0645-15), 15 Oct 2026 09:1x UTC (09:12 by date -u) by date -u -- pushed before any fetch or score

Target: the two f.22r numerals still M: 13: (key.tsv Mr, H) at L03 pos 13 and the 65 at L04 pos 0 (plain form, hypothesis = 65' ra).
Also logged if seen (not the main test): a glossed bare 7 or 5 (c275-hand question, Baluze 167).
Material: glossed d'Avaux-key continuation canvases in Baluze 169 (btv1b9001488b) named by BAL-169 A4: c224 (La Barde f.110r), c231-232 (La Barde f.112),
c297-302 (Chavigny f.144), c344-347 (Chavigny f.169), "c419-421" = f.206-207 (BAL169-FIN: the one short run is on c418; c420-421 are f.208, the
Saint-Chamond key, gate FAIL by BAL-169 A4, excluded).
1. Fetch: openapi.bnf.fr IIIF v3 `full/2400,`, <= 10 requests, one at a time, >= 3.3 s, ROOM take/release, scratchpad only. Order (c346 carries
   "M. le duc Bernard" per BAL169-FIN, the likeliest 13:): c346, c345, c347, c298, c299, c302, c301, c231, c224, c418. c297, c232, c344 only if a
   request is left. Stop before a canvas that would cross 80% of cap (USD 3) or box (10:11 UTC).
2. Key-identity gate per letter (not per canvas, for cost; a letter = one sender's continuation): place >= 8 marked numerals under their gloss (or all
   placeable if fewer); pass if >= 75% give the key.tsv value. A letter that fails is excluded and reported, its pairs not scored.
3. Values fixed now (as BAL-169 A4): 13: = Mr; plain 65 = ra. Wrong-mark negatives: 13' co, 13 sued; other 65 forms.
4. Pairs go to f22mk/glossed_pairs_169c.tsv; scorer f22mk/score_marks_169c.py = score_marks_169.py with that fourth file and TARGET 13:, 65 (plain)
   added. Call rule unchanged: S if >= 3 glossed occurrences give the value and that is >= 3/4 of the sign's glossed occurrences, AND real matches beat
   every one of 200 within-run gloss shuffles; else M (under 3: M, reported as a count).
5. Any value reaching S: `tools/decode_key.py ciphers/baluze167-davaux-1637 --try` at every occurrence with --try's own power control before it enters
   exceptions/key; undecided/reject or a failed control -> reported, not entered.
6. Reader: my eye at 2400 px with zooms of each target numeral; not blind (I know key.tsv); a mark I cannot settle is left out, not guessed.
