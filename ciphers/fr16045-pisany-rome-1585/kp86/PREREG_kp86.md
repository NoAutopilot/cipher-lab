# PREREG kp86 -- fr16045 f.244r (17 Sept 1586) cipher vs its Colbert 16 pt II clear copy (RUN3-PISA, 4 Oct 2026)

Written and pushed before either blind pass of f.244r is read or decoded (passes not yet started).

Material.
- Cipher: fr.16045 f.244r = Gallica btv1b9060906j canvas 500 (offset here is canvas = 2 x folio + 12: c488 = f.238 dated
  9 Sept 1586, c492 = f.240 dated 17 Sept 1586, c500 carries the folio number 244). Nine cipher lines between the clear
  "... je voudrois que V.M. en feist proffit" and the clear "Et que si Sa S. vouloit assister ...". Crops
  images/f244r_L01_s1.jpg .. f244r_L09_s2.jpg (tools/iiif_lines.py, command in NOTES.md).
- Clear copy: BnF Melanges de Colbert 16 pt II (Gallica btv1b100341061) canvas 443 p.49 l.17 "le ruinant de reputation"
  to canvas 444 p.50 l.4 "s'il les abandonnoit", read once by this worker from the 1400 px canvas images; text in
  kp86/colbert_p49_50.txt. The copy is a 17th-century fair copy, so its spelling may differ from the cipher's.
- Key under test: Tomokiyo's table captioned "Vivonne's Cipher (1586-1587)" (sources/cryptiana/web/henryiii_Vivonne5.png;
  the caption itself names the years, so no paragraph-order inference is needed, unlike the 1585 table). Cut into 73
  value-blind cells T01-T73 by tx86/keycells86.py (tx86/SIGNSHEET86.png); values in key86.tsv. Alternatives Tomokiyo
  marks with "?" (T66, T67 for le; T73 for monsieur) are kept with their value.

Transcription: two blind Sonnet passes over SIGNSHEET86 labels (tx86/PASS_BRIEF86.md, values withheld), reconciled by
this worker against the crops (one unit), written to tx86/ciphertext_f244r.tsv. Passes A/B are also scored, not gating.

Decode rule (fixed now): each label -> its key86 value; word signs -> the whole word; nulls -> nothing; `?[...]` tokens
dropped and counted; a trailing `?` stripped. Letters normalised on both sides: lower case, accents stripped, j->i,
v->u, k and w kept as they are (the table has neither), apostrophes/punctuation removed.

Statistic (known-answer): tools/stream_align.nw_score(decoded letters, clear letters) = identical aligned letter pairs /
decoded length, semi-global banded alignment, free leading/trailing gaps on the clear side (the RUN2-NXALN statistic,
defaults unchanged).

Nulls (same statistic, same tokens, computed in the same run):
(a) key-shuffle: 1000 permutations of key86's value column over the 73 labels. Why it can differ from the target: the
    statistic counts letters that match the clear copy; a permutation changes which letter (or word) most signs yield,
    so the matched count can fall or rise independently of the order of signs.
(b) order-shuffle: 1000 shuffles of the reconciled token order, then decoded with key86. Why it can differ: the letter
    multiset is kept but the alignment needs the same letters in the same order as the copy; order-shuffling destroys
    that, so only a key that actually reads the page in sequence scores above (b).
Positive control (same run): the clear copy enciphered with key86 (uniform random homophone among the cells for each
letter; letters only, no word signs; letters without a cell dropped), sign noise at e = the measured err_2reader of
passes A/B (each sign replaced by a uniformly random other label with probability e), decoded and scored against its own
nulls (a) and (b) at 200 each; 5 seeds; passes if >= 4 of 5 seeds exceed both of their own p99s.

Gate: PASS if target > p99 of (a) AND > p99 of (b) AND the positive control passes. Control fails -> NON-TEST. Target
fails with err_2reader > 0.10 -> NON-TEST, not a negative (TRANSCRIPTION.md), unless the control passed at that e.
A PASS says Tomokiyo's 1586 table reads this page in sequence with the period clear copy (a known-answer check of the
table), nothing about novelty. Script: kp86/kp86.py -> kp86/kp86_result.json. No parameter changes after the first run.

Afterwards (not gated by this test): tools/interlinear_align.py stream on the reconciled tokens vs the clear copy for a
label -> letter map (grade C), compared cell by cell with key86, and the four 1585-sheet confusable groups (S15/S40/S13/S61,
S10/S41/S02, S36/S42/S23, S46/S48/S25) mapped to their 1586 look-alike cells where a look-alike exists, reported as
sorter/known_answer_hints.tsv (shape-level hints only: the 1586 table is a different key from the 1585 one).
