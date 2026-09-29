# DEB-SWARM-C log (group C: syllabic or mixed system; control FR-SYLL)

Session: DEB-SWARM-C (worker for the owner-account orchestrator), 29 Sept 2026, box 03:10-06:10 UTC.
Hypothesis: each sign = a French unit that is a syllable, a short (function) word or a single letter; the verse
rhymes line-final (h8/H5), so the unit is at syllable scale. Scorer: `../score.py` frozen ed4a3743 (blob d80e6baa).
Tools here: `syll.py` (syllabifier, mixed tokenizer, unit bigram/trigram LM, planted controls, annealer),
`solve_control.py` (blind fit on a harness control's ciphertext only, then `score.py --control`).
Nothing here is a reading. Rule 10 wording throughout.

| time (UTC) | method | parameters | control result | real-text held-out pct | why it failed / what it shows |
|---|---|---|---|---|---|
| 03:12-03:19 | own planted mixed control (syll.py --plant), unit bigram, homophones, no channel term | N 658-2600, K 124, S 60, W 10 | token recovery 0.0-0.23 | not run | the fitted keys scored FAR above the true key (N 658: -1475 vs -1990; N 2600: -6208 vs -7879): the objective, not the search, was wrong -- a unit-LM score alone rewards piling many signs on frequent units. Fix: add the homophone channel term (-sum_u C_u log C_u, the MLE p(sign given unit)); after it the true key outscores the found key (N 658: -3941 vs -4008), so search becomes the limit. Transferable to any homophonic solver scoring P(plaintext) alone |
| 03:15-03:19 | FR-SYLL blind (solve_control.py), own syllabifier, top-17 corpus words, injective (one sign per unit, as the design), fr19 prose + Fleurs du Mal | S 150/200, order 2/3, 1.5M iters x 3 | recovery 9.0 (o2), 3.2 (o3), 7.2 (o3, S 200) pct | not run | far below 70; own-design planted twin (same rules, own syllabifier) reads 40.5 pct at 0.8M iters, so part of the gap is unit-definition mismatch with the harness |
