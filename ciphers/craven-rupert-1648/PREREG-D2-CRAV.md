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
