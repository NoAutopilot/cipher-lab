# PREREG CL571-9429 (14 Oct 2026, 19:2x UTC by date -u), pushed before any score is computed

Item: DECODE R9429, BnF Clairambault 417 f.236-237 ("Mémoire chiffré de Brasset, octobre 1648"), 3 pages, a cipher text with an
interlinear decipherment in a period hand (not a key table).

Question: which key's values does the cipher on f.236 use -- 9431 (Brasset, Clair 574 p.4-5, keys_decode/9431_key.tsv) or the
published Clair 421 f.160 Brasset-Mazarin table (keys_decode/clair421_published.tsv)? No decode campaign.

Pairs: `pairs.tsv`, (gloss unit, cipher number) read by eye by this worker from the interlinear gloss: set A = P1 lines 1-2, set B =
P3 lines 1 (one reader, not blind; set A's segmentation was made after looking at 421, set B's with 421 already in mind -- both are
M-grade alignments; this bias favours 421 and is reported, not removed). A pair is a numeric code group whose gloss unit is a
syllable or word; letter/symbol groups and units whose span is unclear are excluded.

Statistic: hits = unique pairs (unit, number) for which key K has a row whose normalised plaintext (lower case, accents removed,
apostrophes and spaces removed) equals one of the unit's listed spellings and whose code number equals the pair's number (series
mark ignored on both sides: the f.236 marks are not read reliably at this pass).
Control: the same count after permuting key K's code numbers over its rows, 2,000 permutations, seed 9429; report mean and p95.
Coverage: how many units have any row in K at all (a key cannot hit a unit it does not list).
Gate: K "fits" if hits > control p95 AND hits >= 0.6 x covered units; K "does not fit" if hits <= control p95. Reported for both keys.
Script: `score_9429.py [--check]` writes `score_9429.txt`.
