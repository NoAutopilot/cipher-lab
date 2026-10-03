# clairambault1225-paget-1714 -- hypotheses and instrument results (append-only)

Opened 3 Oct 2026 (READ2-PAG). Rule 3: every row gives the target and control numbers side by side.

## Open-codes homophone/null pass (READ2-PAG, 3 Oct 2026)

Pre-registered in align/PREREG_homophone.md (commit 0cfc96eb, before the run); script align/homophone_pass.py -> homophone_pass.txt,
homophone_codes.tsv. Statistic: held-out agreement (key from one letter's own alignment, scored on the other letter's aligned
chunks, both directions). Control: gloss texts permuted within each letter, 200 seeds.

| configuration | L1 -> L2 (real / shuffle mean / p95) | L2 -> L1 (real / shuffle mean / p95) | gate | codes held in both directions (real / shuffle mean / p95) |
|---|---|---|---|---|
| C1 one-unit, null-cost -3 | 24/134 = 0.179 / 0.032 / 0.074 | 9/47 = 0.191 / 0.046 / 0.111 | PASS | 4 / 0.4 / 1 |
| C2 nulls free, null-cost 0 | 22/166 = 0.133 / 0.359 / 0.466 | 14/55 = 0.255 / 0.440 / 0.574 | FAIL | 3 / 0.0 / 0 |

Reading: one-unit (C1) passes; the nulls-free configuration fails (letting codes take nothing inflates chance agreement on empty
chunks above the real figure), so the null hypothesis class gets no support from this test; the C2 list of null-in-both codes (56)
is reported only. Homophony read-off: C1's 4 codes take 4 distinct values (87 de, 146 le, 196 po, 240 ion), so the test shows no
homophone set; with only 4 codes held, that is not evidence against homophones either. Promoted: 146 'le' (the only one of the 4
graded M in key.tsv) to S; 87, 196, 240 were already H. Tokens: 8 of 146's 20 move M -> S; 12 stay M (own chunk disagrees).
Expected chance codes at this gate: 0.4 (shuffle mean).

Instruments on these codes so far (rule 3 third-attempt clause): one aligner, tools/interlinear_align.py, under four tests --
(1) Thurloe defaults (NEXT-PAG: 0.175 vs shuffle p95 0.184, did not beat control); (2) syllabic options, pooled self-agreement and
held-out pairs (NEXT-PAG: 0.277 vs 0.126; 24/37 vs 0.378); (3) per-letter own/cross gates (PAGET-KEY, A2-PAG3: both PASS); (4) this
held-out homophone/null pass (C1 PASS, C2 FAIL). Each pass moved the aggregate but not the bulk of the codes: 420 tokens stay M.
Standing for those 420: untested-by-this-tool beyond what it now holds (not refuted); a fifth configuration of the same aligner is
not the next step -- that needs a different instrument (a segmentation that does not take its chunk boundaries from hard-EM on these
same 56 pairs) or new material (the AN Marine B7 originals, LOCAL-QUEUE L11; the Paget 1713 sibling).
