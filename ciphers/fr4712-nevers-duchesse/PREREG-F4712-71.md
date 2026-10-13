# PREREG-F4712-71: key no.71 as an all-code text on fr.4712 f.10r

Worker F4712-71 for LANE DEFAULT-A1-0640 (owner account), 13 Oct 2026, written 07:4x UTC by date -u, pushed before any score below is
computed. Brief: `.claude/briefs/runs/2026-10-13-acct1-default-0640-jobs.md` "### F4712-71" unit (2); NOTES.md "Remaining gaps
(F4712-CENSUS)" item 2. Pattern: PREREG-F4712-K71.md.

## Inputs (fixed now)
- Key: the no.71 **"Motz" word list**, codes 11-99 complete: 11-17, 52-58, 92-99 from F4712-K71's eye rows; 18-51 and 59-91 added this
  job to `keys/key_no71.tsv` from the native region openapi.bnf.fr btv1b525085665 f256 600,4250,3700,1450 (crops images/k71/wc_L01-L10),
  one blind Sonnet read checked against this worker's eye read (0 code disagreements; 28 luy, 29 son, 36 n'a, 86 leuee|lence are M).
  The key reuses the same figures in other dotted columns (Villes 11-48, Provinces, Cavallerye 73-100); this test uses the Motz list only,
  the one complete word list, and says so. Persons: 8 = Roy, 10 = Royne mere (overlined on the key), fixed, not shuffled.
- Target: the 37 numbers of S1 (`score_key1.TOMO`), signs not counted.
- Marks (a fact about the crops, looked at before writing this file): at native resolution (images/f10b/f10c_L01_s1-s2, and
  images/src_ark_12148_btv1b9058289m_f18_4100_2750_3300_560.jpg) no dot or overline stands over any of the 37 figures on lines 1-3;
  the only mark is the cross above the line-opening loop sign. Under no.71 every word code needs a dot and every person code an overline.
- Language model: word bigrams over `LANG_CORPORA["fr16"]`, tokens lowercased, accents folded (judge_plaintext.FOLD), the corpus
  filtered to the Motz vocabulary + roy/royne (a telegraphic stream: what order key words come in); add-0.5 smoothing. Train on the
  first 70% of the filtered stream; controls drawn from the last 30%.

## Statistic W (primary)
W = mean log P(w_i | w_{i-1}) of the decoded 37-word sequence. Null: 200 keys with the 89 Motz values permuted among codes 11-99
(seeds 1-200). Report the target's rank of 201 and z.
- Power control P (matched N=37, no.71 Motz design, French): 20 windows of 37 consecutive tokens from the held-out 30% (seeds 50000+),
  encoded with the Motz list, each ranked against its own 200 permuted keys the same way. P = windows with rank <= 10 of 201.
- False-positive control F: 20 sequences of 37 codes drawn uniformly from 11-99 (seed 99), ranked the same way; F = rank <= 10.
- Why the controls can differ from the target: W depends on the order of the decoded words, and a value permutation changes every
  decoded word, so a real all-code French text should outrank its permutations (P measures whether it does at N=37); a random code
  sequence should not (F). The target can land anywhere 1-201.

## Gates
- P >= 10/20 and F <= 3/20, else NON-TEST (the statistic cannot tell at N=37).
- Then target rank <= 10 of 201: SIGNAL (the all-code reading is worth a second look); rank > 10: NO SIGNAL (control-backed negative
  for no.71's Motz list as an all-code text, conditional on S1 and on the Motz list being the column used).
- Grading (rule 4): every decoded word is M whatever the gate (no mark on the leaf); a SIGNAL licenses nothing above M.
- Descriptive only: the three f.13r H glosses on f.10r codes (82 "D. n.", 21 "Berry", 12 "b. Pal.") against the Motz values.
