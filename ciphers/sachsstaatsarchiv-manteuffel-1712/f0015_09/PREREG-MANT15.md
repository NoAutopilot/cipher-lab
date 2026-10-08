# PREREG-MANT15 (FAM-MANT15, 8 Oct 2026, written before any pass was read or any score computed)

Target: Loc. 694/09 URL files 0015 (f.8) + 0016 (f.8v), unglossed letter-range code runs (extract of a relation of 3 Jan 1713
sent with Manteuffel's letter of 13 Jan 1713). Key: key.tsv (Krauske 1893 rows + licensed rows), unchanged by this job.

Statistic: mean log10 4-gram probability per letter (tools/judge_plaintext.py NgramModel, corpus fr18 = the spec's judge
language) of the letter string obtained by decoding every code token of the reconciled runs that key.tsv maps to a letter
value (value of 1-3 letters, first alternative of an "a|b" value; name/word codes and U codes dropped, run order kept, runs
concatenated in page order).

Control (rule 3, can differ from the target on the statistic): 1000 shuffled keys, seed 15: the letter values of key.tsv's
letter-valued codes are permuted among those codes; the same token sequence is decoded and scored. Gate: PASS if the real
key's score is above the shuffled keys' p99 (i.e. at most 10 of 1000 shuffles at or above it). Also reported, not a gate:
judge_plaintext's real_p05 / null_p99 at the same N.

Power control (run first, same code): 694/09 0085 runs 9 + 10 (f0085_09/reconciled.tsv, glossed, read by Krauske's table
under its period gloss, R13-MANT85). If the power control's real key is not above its own shuffled p99, the method has no
power at this length and the target result is logged "non-test", not PASS/FAIL.

Grades: tokens decoded through C rows of key.tsv are C only where the reading is a key application; since this leaf has no
gloss, every decoded token is graded at most as its key row's grade and the reading as a whole is a key application, not a
known-answer check. Name identifications are I.

## Addendum (8 Oct 2026, 16:3x UTC, before 0052's passes were read or scored)
0015+0016 results are in gate.out (computed after this file's first commit 1110da1cd). For 694/09 0052 (f.36 slip, P.S. to
Manteuffel's letter of 11 Feb 1713) the same statistic, control (1000 shuffled keys, seed 52) and PASS rule apply, on
f0052_09/ciphertext.tsv; the power control is the same 0085 runs 9+10 result. Codes outside key.tsv (394, 405, 520) are
dropped from the letter string and stay U; no value is proposed for them (no gloss). The small interlinear numerals over
the first run are transcribed but are not decoded into the letter string (their role is unsettled).
