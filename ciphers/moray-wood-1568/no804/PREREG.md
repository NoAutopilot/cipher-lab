# Pre-registration: Bain ii no.804 crib test under key.tsv (GAPS15-moray-wood-1568, 2 Oct 2026, account-4)

Written and committed **before any image of the leaf exists** (ASKS row 103 asks the owner for it; REQUEST.md item 1).
Nothing below may be changed after a transcription of the leaf is on disk; a changed rule is a new, separately dated
pre-registration, and the result under this one is still reported.

**Item.** John Wood to Cecil, Edinburgh 6 Sept 1568, holograph (Bain, CSP Scotland ii no.804; archive.org
`CalendarStatePapersMaryQueenOfScotsVol2`, OCR line 38231, read GAPS13). By Bain's volume table TNA SP 52/15 (grade M,
the page decides). Bain's footnote marks one phrase "in cipher" and prints its plaintext:
*"and says he must neidis haif it be on meinis or uthir"* (11 words, 42 letters).

**Question.** Is that phrase written in the key of the f.213v postscript (Aymeloglu's key.tsv, aaymeloglu/unsolved-ciphers
moray-1568/key.json d2800bb, credited, rule 8)? If yes, the leaf is a known-plaintext crib in the same key and settles
M-graded values (Zz t/k, x3 e/n, Z5 y/i, the unattested L3.26 t-shape) by grade C.

**Candidate plaintexts (fixed).** Bain's wording with four spelling choices, 16 variants: says|sayis, neidis|nedis,
haif|haue, meinis|menis; every other word as Bain prints it. Normalised: lower case, spaces dropped, v->u, j->i (key.tsv
has one u/v class). 41-43 letters. Bain may have normalised Wood's spelling; spelling drift beyond these variants is
absorbed by the LCS statistic (insertions/deletions cost nothing but a lost match).

**Transcription and decode.** The leaf's cipher signs are labelled in the Moray label set (ciphertext.tsv) by the same
method as GAPS9's R2989 relabel (side-by-side with the postscript bands), one TSV with a `sign` column, '?' for a sign
with no Moray counterpart, '|' for a gap; low-confidence labels flagged in a `conf` column but the primary label is
scored (no variant search over labels). Decode: key.tsv sign by sign, word-signs U = the, o2 = and, person-signs 4b/Eb
dropped, any label absent from key.tsv = '?'. 'b' (in "be") has no sign in key.tsv and can never match.

**Statistic.** S = max over the 16 variants of LCS(decoded letters, variant letters) / len(variant).

**Nulls (200 each, seed 1).** A: every variant letter-shuffled, S recomputed on the same decode (frequency held, order
moved). B: 200 shuffled keys (single-letter values permuted among single-letter signs; word- and person-signs fixed),
decode recomputed, S against the true crib (transcription held, key moved). Both can move S (rule 3, not orthogonal).

**Pass.** S > 99th percentile of null A **and** of null B **and** S >= 0.60. Otherwise FAIL, worded "not shown to be in
key.tsv at this length and transcription"; it is read as "a different key" only if the positive control below passes
>= 80 pct at the leaf's own measured transcription error (two blind labelling passes; error = 1 - agreement).

**Controls, run now (control.tsv).** Reproduced by `python3 ciphers/moray-wood-1568/no804/no804_crib.py --control`
(seeds 1000+row, about 3 minutes on 4 CPUs):

| control (40 trials, nulls 200 each) | injected sign error | pass rate | mean S |
|---|---|---|---|
| positive: crib enciphered under key.tsv | 0 / 10 / 20 / 30 pct | 1.000 / 1.000 / 1.000 / 0.975 | 0.976 / 0.876 / 0.799 / 0.717 |
| false-pass: crib under a shuffled key | 0 / 10 / 20 / 30 pct | 0.000 / 0.000 / 0.000 / 0.000 | 0.381 / 0.379 / 0.367 / 0.372 |

Power at the expected length (39-42 signs): >= 97.5 pct up to 30 pct sign error, false-pass 0/40 at every level; the
length is long enough. What the control does not model: Wood's spelling outside the 16 variants beyond what LCS absorbs,
and a leaf whose cipher passage is not the phrase Bain prints (Bain's footnote decides which words were in cipher).

**Reference (not a gate).** The R2989 line (Add MS 4136 f.33, also Wood to Cecil 6 Sept 1568, 39 signs, GAPS9 relabel):
`--reference` gives S = 0.452 vs null A p99 0.475, null B p99 0.425 -> FAIL, consistent with GAPS9 and with Bourdeau's
align3/align4 (cyphersolver targets/wod1568) that Bain's cipher words do not align with that line.

**Run on arrival.** `python3 ciphers/moray-wood-1568/no804/no804_crib.py --score <leaf transcription.tsv>` (exit 0 PASS,
1 FAIL; writes `<stem>_no804.tsv` here). Offline test: `python3 ciphers/moray-wood-1568/no804/test_no804_crib.py`.
A PASS is a cryptanalytic match, reported with grades per rule 4 and for a separate verifier; no novelty wording (rule 10).
