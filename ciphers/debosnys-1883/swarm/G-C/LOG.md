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
| 03:20-03:22 | FR-SYLL blind, HARNESS unit rules (make_controls.py's syllabify() and 17-word FUNC list read as design; the control's plaintext source and window not read), injective | S 130/160, order 2/3, 2M iters x 3 | S160 o2 49.0; S130 o2 35.6; S130 o3 18.9; S160 o3 6.6 pct | not run | matching the unit definition lifts 9 -> 49 pct; trigram from the frequency-rank start searches worse than bigram |
| 03:23-03:25 | same, larger vocab / trigram refine | S 200, S 250 (o2, 3M x 4); S160 o2 2M x 3 then o3 refine 1.5M from the o2 key | S200 21.3; S250 7.6; S160+refine 50.0 pct | not run | a vocabulary much larger than the text's own unit count drowns the search; refine adds about 1 point |
| 03:26-03:31 | S160 o2 anneal + o3 refine, three seeds; polish.py (char 5-gram information gain + unit bigram, first-improvement hill-climb) | 4M x 4 + 3M refine; polish 3 sweeps on the 03:22 S160 key | seeds 11/12/13: 15.3 / 11.4 / 57.6 pct (o3 scores -5340 / -5256 / -4704: the best score is the best key, so blind selection by score works); polish 49.0 -> 52.7 | not run | search variance dominates; more seeds + pick by score + polish is the pipeline |
