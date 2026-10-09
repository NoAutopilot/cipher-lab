# PREREG-D2-CRAV -- craven-rupert-1648 spec test 2 (key-family test), registered 8 Oct 2026 before any score is computed

Target: ciphertext.txt as committed (R8447, 42 tokens). Token X (struck, illegible) is dropped; "18?" is used as 18; "183h"/"311h" are used as 183/311 (the half mark ignored). Target N = 41 tokens in 7 lines.

Candidate tables (test2/*.tsv, read by D2-CRAV from the DECODE full-size images of the sibling records in one login, 8 Oct 2026, and from Cryptiana):
T_8446 (R8446 attested pairs), T_8446x (R8446 pairs extended along the two regular odd series they sit on: grade I, a hypothesis table),
T_8448 (R8448 attested), T_8445 (R8445 attested), T_NR (Tomokiyo's Nicholas-Rupert July 1645 letter table, with his "-" nulls).
R8449 (ff.146-147) carries no cipher with decipherment on its four images (a clear estimate of ships' charges): no table. THE=g4 (Tomokiyo's private
reconstruction from Add MS 18982 f.79): no published table found (charlesi.htm snapshot and live copy, the 25 Sept 2023 blog post): not tested.

Statistics, per table T:
- COV = number of target tokens whose code is in T.
- WL = letters inside dictionary words: decode each line, an uncovered token breaks the run; within each run, a DP picks non-overlapping
  words (length >= 3) from the word list that maximise covered letters; WL is that total. Word list: every word of length >= 3 occurring
  >= 2 times in tools/data/en16_repo/*.txt (Thurloe, 1650s English, era-matched), lowercased, u/v and i/j folded.
Controls (1000 draws each, seed 2026):
- C1 random-code control for COV: T's values on the same number of codes drawn uniformly without replacement from 1..max(T's codes).
  (COV can differ from the target under C1; a shuffled-order or shuffled-value control cannot change COV and is not used for it -- rule 3, bCAS.)
- C2 shuffled-key control for WL: T's values permuted over T's codes (same codes, so same COV; WL can differ).
Gate (Bonferroni over 5 tables: one-sided p99): a table PASSes on the target only if COV > C1 p99 AND WL > C2 p99.
Matched-design control (rule 3, design): for each table T, 20 synthetic ciphertexts of N=41 tokens in the target's 7 line lengths, plaintext
from a random offset in en16_repo, enciphered with T itself (a letter -> a random code among T's homophones for it; a word that T codes
whole is coded whole; a letter T lacks -> a code outside T, i.e. uncovered). The same statistic and gate are applied. If fewer than 16/20
(80%) synthetic letters PASS, a FAIL of T on the target is logged "non-test at this N for T", not a negative.
Outcome words: PASS (worth a reader, not a reading); FAIL with control >= 80% (control-backed negative for that table); non-test.
Script: test2/key_family_test.py (writes test2/results.tsv; --check re-derives and compares).

## Deviation 1 (8 Oct 2026, 08:1x UTC, recorded after the first run)
tools/data/en16_repo turned out to be tagged reading files (comment headers, token format): 311 dictionary words and garbled synthetic
plaintext. The word list and the synthetic plaintext now come from tools/data/en/pg*.txt (modern English, not era-matched; a dictionary and a
plaintext source, not a judge). The registered run (results.tsv) then gives: every table FAIL on the target and the matched-design control
passes 0/20 (T_8446, T_8448, T_8445), 1/20 (T_8446x), 14/20 (T_NR): all five are NON-TEST under the registered WL gate. WL has no power at N=41
in seven short lines (a self-enciphered synthetic reads WL 17 under its true key against a shuffled-key p99 of 35).

## Amendment A1 (registered before it is computed): coverage-exclusion gate
Question: could R8447 have been enciphered with the key a table samples? Statistic COV as above. Key-true control distribution, 200
synthetic N=41 letters in the target's line lengths: for T_8446 the synthetic is enciphered with T_8446x (the full series hypothesis) and scored
with the attested T_8446 (what our quarter-page sample of R8446 would cover if R8447 used R8446's key); for T_8446x, T_NR, T_8448, T_8445 it is
enciphered with the table itself (for T_8448/T_8445, which are partial samples, this is an upper bound and is flagged so).
EXCLUDED if target COV < the 1st percentile of the key-true COV distribution AND the key-true p01 exceeds the random-code C1 p99 (so the
control can fail differently from the target -- rule 3); NOT EXCLUDED if target COV is at or above that p01; non-test if key-true p01 <= C1 p99.
Script: test2/coverage_exclusion.py --check.

## Amendment A2 (CRAV-49, 8 Oct 2026, registered before it is computed): A1 unchanged, two more tables
Tables: test3/T_8452.tsv (Charles R., "my owne Cypher", St Germains 3 Aug 1649; R8451 is the same letter and adds no pairs) and
test3/T_8453.tsv ("L. Gerrards Cypher", Charles R., Jersey 15 Nov [1649]); single-reader M pairs from the period interlinear glosses.
R8454 (f.195, 2 images) was not fetched (the session's one login hit its file cap first): not tested.
Statistic, controls, seeds and verdict rule exactly as A1 (key-true synthetic = each table enciphering itself, flagged as an upper bound
because each is a one-letter sample of its key; random-code C1 p99 over 1..max(code)). Script: test3/coverage_a2.py --check.
If a table is NOT EXCLUDED: decode R8447 under it with a shuffled-key control (brief CRAV-49). Note recorded before scoring: R8447 carries
9 of 41 tokens above 269 (T_8452's highest code) and 4 above 557 (T_8453's), so neither table's key can cover the whole letter as sampled.

## Amendment A3 (CRAV-54, 8 Oct 2026 ~20:00 UTC, registered before it is computed): A1 unchanged, two more tables
Tables: test3/T_8454.tsv (R8454, BL Add MS 18982 f.195, Charles R. to "Deare Cousin", Jersey 4 Dec [1649]; single-reader M pairs from
the period interlinear gloss) and test3/T_G.tsv (the union of T_8453 and T_8454, T_8453's value kept on a conflict), because R8454 shares
its key with R8453 ("L. Gerrards Cypher"): of the R8454 codes also in T_8453, most carry the same value (counted in NOTES.md).
Statistic, controls, seeds and verdict rule exactly as A1/A2 (key-true synthetic = each table enciphering itself, an upper bound; random-code
C1 p99 over 1..max(code)). Script: test3/coverage_a3.py --check. If a table is NOT EXCLUDED: decode R8447 under it with a shuffled-key control.
Note recorded before scoring: R8454's highest code is 583; R8447 carries 4 of 41 tokens above 583 (852, 922, 1037, 1067).

## Amendment A4 (CRAV-8450, 9 Oct 2026 ~11:5x UTC by date -u, registered before it is computed): A1 unchanged, one more table
Table: test3/T_8450.tsv (R8450, BL Add MS 18982 ff.177-178, Edward Hyde to Prince Rupert, The Hague 28 Feb [1648/9]; single-reader M/I pairs
from the period interlinear gloss). A design of small letter codes (2-87) plus word codes (89-491). Statistic, controls, seeds and verdict rule
exactly as A1-A3 (key-true synthetic = the table enciphering itself, an upper bound; random-code C1 p99 over 1..max(code)).
Script: test3/coverage_a4.py --check. If NOT EXCLUDED: decode R8447 under it and report with a shuffled-key control, no reading claimed.
Note recorded before scoring: R8450's highest glossed code read is 491 (465 'will' on f.177v; one unglossed group '965' on f.178r was not
read with confidence); R8447 carries 4 tokens above 583 (852, 922, 1037, 1067).
