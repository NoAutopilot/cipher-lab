# PREREG-HAR-F11 (15 Oct 2026, 08:2x UTC by date -u; LANE DEFAULT-A2-0810-15, account 2)

Pushed before R8477 (BL Harley MS 287 f.11) is viewed in this job and before any comparison. Job:
.claude/briefs/runs/2026-10-15-ytbiz-default-0810-jobs.md "HAR-F11". Shape follows keys/PREREG-HAR-KEYS.md (Fit A/B + control).

Inputs. Target: f11/ciphertext_f11.tsv, one row per cipher group of f.11 as read in one Opus look at full size
(crops in the session scratchpad; every sign grade M; columns line, group, tokens (space-separated signs, numerals kept as
numbers), sign descriptions in words, note). Reference (on disk, read by eye in HAR-KEYS, grade M): R328 letter signs =
keys/period_signs_HAR-KEYS.tsv rows `R328 commission` (three signs per letter, 23 letters); R328 codes and R330 list =
keys/codes_HAR-KEYS.tsv rows R328 / R330. No reference sign is re-read here.

Fit A (R328 alphabet). Each non-numeric f.11 sign is matched to the R328 shape(s) whose word description names the same shape
(matching done once, written to f11/match_f11.tsv before scoring; an unmatched sign stays '?'). Each group of >= 3 signs is
decoded to its candidate letter strings (each '?' a wildcard). Score = number of such groups whose decode contains an English
word of >= 4 letters (word list: tools/data/en16_repo/*.txt tokens, frequency >= 2). Control: the same count after 20 random
permutations of R328's letter labels (seed 0). Fit A = score >= 2 AND score > control maximum. Coverage (share of f.11 letter
signs with an R328 match) is reported beside it, not gated.

Fit B (R328/R330 nomenclature). Score = number of distinct f.11 numerals that R328 or R330 defines (a null counts as defined).
Control: 20 draws (seed 0) replacing each f.11 numeral by a uniform random integer with the same digit count; same count.
Fit B = score >= 2 AND score > control maximum. A defined numeral without Fit B is a LEAD (grade M), never a value.

Outcome. Fit A or Fit B -> a planned decode_key --try step written in NOTES.md; no key.tsv edit in this job. Neither -> the
f.11 comparison against R328/R330 is ticked done, none fits; the transcription stays for a later key comparison. If the f.11
image is not served (forbidden.png) the job stops before any score and says so. Too few groups (< 2 groups of >= 3 signs, or
< 2 numerals) makes that fit a non-test, logged as such, not a negative.
