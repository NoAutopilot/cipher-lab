# PREREG-THURBM -- Blank-Marshall (Bruges) key, Birch 1742 vol 6 (written 10 Oct 2026, 14:4x UTC by date -u, before any score)

Job: THUR-BM, LANE FAMILY-A2r (account 2). Brief: .claude/briefs/runs/2026-10-10-ytbiz-family-1410-jobs.md "### THUR-BM".
Letters: four glossed Blank-Marshall letters in Birch 1742 vol 6 (bim_ copy, djvu lines 40469 p.338, 65889 p.550, 77385 pp.645-646,
89881 p.756) and the unglossed l.44535 (p.374, 8 July 1657 N.S.). Leaves 377-378 checked: no printed decipherment of l.44535.

## Data (fixed before scoring)
- Two blind Sonnet passes (B1, B2) per glossed letter on line crops (bm/crops/), each writing per numeral group the token and the small-type
  gloss printed above it. Pass A is the djvu OCR (numerals only; its gloss rows are unreadable OCR noise, so A is not used for the gloss).
- The gloss is the known answer and is NOT reconciled before scoring (V-BRANDT rule): every fold is scored per blind pass, pass k's key
  trained on pass k's three letters and scored against pass k's fourth letter's gloss, k = 1, 2.
- Normalisation of gloss and key meaning before comparison (PX-BRODEC rule, both sides alike): lower case, letters only, long s = s,
  u = v, i = j; a code meaning that is a name or word compares on that normalised string.

## Key build (per fold, per pass)
- bm/<line>_pairs_B<k>.tsv in the folder's pairs format (plain_raw = the row's glosses in order, cipher_raw = the row's numerals and clear
  words in order) -> `tools/interlinear_align.py align` (default --floor 100) on the three training letters concatenated -> key TSV.
- A code enters the training key at its majority meaning (count >= 1).

## Statistic and control
- Held-out agreement = share of the held-out letter's numeral groups with a non-blank gloss AND whose value is in the training key, for
  which the training key's meaning equals the normalised gloss above that group. Reported separately for groups < 100 (letter/syllable)
  and >= 100 (word/name codes), and pooled. Coverage = share of the held-out letter's glossed groups whose value the training key covers,
  reported beside it.
- Control (can differ: agreement depends on which meaning sits on which code): permute the training key's meanings over its codes,
  >= 200 draws (seeded 0..199, numpy-free random.Random(seed).shuffle), same covered set, same scoring; record the p95.

## Gate
PASS only if, for BOTH passes: every one of the four folds' real agreement is above that fold's own shuffled-key p95, AND pooled held-out
agreement (all four folds, groups on codes the training key covers) >= 0.70. Anything else is FAIL (logged in HYPOTHESES.md, no decode).

## On PASS (step 3)
- Full key = interlinear_align.py on all four letters, once per pass; codes whose meaning agrees between the B1 and B2 keys enter
  bm/key_blankmarshall.tsv (grade C: meaning from Birch's printed decipherment, the folder's print-gloss convention); a code whose two
  pass meanings differ is listed with both and graded M.
- l.44535 numerals: reconciled from A (OCR) and one Sonnet pass (B1) by eye on the crops, a second pass if A and B1 differ on > 10%.
- Decode with a --check script; per-token grades: C for a group whose code is in the agreed key, M for a two-meaning code, unread
  otherwise. Control on l.44535 (no known answer): English 4-gram score (mean log10 per letter, letters from groups < 100 only, codes
  and unread as breaks) of the decode vs 200 shuffled-key decodes (same permutation scheme); report real vs p95. The folder has no spec,
  so judge_plaintext.py is run only if a spec exists; the 4-gram corpus for this control is the clear English prose of vol 6 itself
  (djvu, lines outside the five letters' windows), era-matched (1657-58 intelligence letters).
