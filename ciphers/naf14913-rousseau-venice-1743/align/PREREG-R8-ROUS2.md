# PREREG R8-ROUS2 (6 Oct 2026, account 2 worker for LANE-RUN8-account-2), written and pushed before the scored run

Question: do Hatzenberger 2015 p.326's code values (République 136, Sénat 219, ambassadeur 404) fit the Lorenzi-Montaigu cipher on disk?
Data: the four slip-backed pairs (ciphertext_f213/slip_f214r, ciphertext_f216v/slip_f217r, ciphertext_f249/slip_f250,
ciphertext_f266r/slip_f265r) as transcribed; slips normalized only by case/accents (r[eé]publique, ambassad*, s[eé]nat).
Statistic: per code, its count vector over the four cipher passages; per word, its count vector over the four slips.
A code "fits" a word when its count vector equals the word's (whole-word code, one group per occurrence).
Pre-registered calls:
 (1) République: 136 fits iff its vector equals the slips' République vector. Control: the number of distinct codes (of all codes
     occurring in the four passages) whose vector equals that word vector -- a chance-match rate that can vary with the word vector.
     If exactly one code fits and it is not 136, Hatzenberger's 136 is contradicted for this cipher (grade of that code's value: I,
     count-level only, not a key change; no key.tsv edit this job).
 (2) Sénat / ambassadeur: slip count vector is expected all-zero. 219 and 404 are contradicted on f.249 iff they occur there while the
     f.250 slip has 0 Sénat / 0 ambassadeur. f.165 (no plain side): context only, at most M; no grade or key change.
No threshold tuning after the run; script align/r8rous2_fit.py, output align/r8rous2_fit.out.
