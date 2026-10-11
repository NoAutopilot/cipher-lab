# PREREG-F4712-K71: key no.71 (BnF fr.3995 f.133r) on fr.4712 f.10r, with matched controls

Worker F4712-K71 for LANE DEFAULT-A1-1840 (account 1), 11 Oct 2026, written about 19:0x UTC by date -u, pushed before any
score below is computed. Brief: `.claude/briefs/runs/2026-10-11-acct1-default-1840-jobs.md` "F4712-K71". Disk only.

## Inputs (fixed now)
- Key: `keys/key_no71.tsv` (copied this job; 26 letter rows from BIRAGO-NUM-KEYEYE3 + the strip-end sign, 44 word/person rows read
  by eye from the same native crop). Design: code + mark; letters plain 1-97, words dotted 11-99, persons overlined.
- Target: the 37 numbers of segmentation S1 (Tomokiyo's division, `score_key1.TOMO`, digits checked on the leaf by DUCH-KEY1B);
  the two line-opening signs are not counted in N. f.10r's figures carry **no dot or overline** visible on `images/f10b/` (looked at
  by this worker before writing this file; recorded as a fact about the crops, not a statistic).
- Language model: `tools/judge_plaintext.py` `LANG_CORPORA["fr16"]` 4-gram; synthetic plaintext from the same fr16 files.

## Statistic D (primary, design consistency)
L = how many of the 37 S1 numbers are no.71 **letter** codes (25 1 10 20 23 24 30 40 50 60 63 64 65 70 73 74 75 80 83 84 85 90 93 94
95 97). Since the leaf carries no marks, under no.71 every unmarked figure should be a letter; a no.71 text written with its marks
dropped still has most tokens on letter codes.
- Control C1 (matched N=37, no.71 design, French): 1000 synthetic texts, each a run of consecutive fr16 words from a random start,
  enciphered with no.71 -- a word in the key's transcribed dotted word list takes its code, every other word is spelled with letter
  codes (homophones uniform; j->i, v->u, k->c, w->u u; x takes the non-numeric triangle and y/z their M codes; signs not counted),
  marks dropped, first 37 numbers kept.
- Control C2 (generous word table, the key's word columns are only partly on the crop): as C1 but the 89 most frequent fr16 words
  are all word codes (dotted 11-99), so C2's L is lower than any no.71 text could plausibly give.
- Null N0: 1000 draws of 37 figures uniform on 8-99 (the target's range).
- Rule 3 check: L is a function of the code values, so the target, C1, C2 and N0 can all differ on it -- not a non-test by construction.
- Gate: **CONSISTENT** if L_target >= C2 p05. **INCONSISTENT** if L_target < C2 p01 **and** C2 p05 > N0 p95 (the control separates
  from noise). Anything else: **NON-TEST** (the statistic cannot tell no.71 from noise at N=37).

## Statistic R (secondary, reading)
Decode S1: a letter code -> its letter; otherwise a read word/person value -> [value]; otherwise ?. Score = fr16 4-gram mean over the
decoded letters plus word values. Rank of the target among 200 keys with letter values shuffled among letter codes and word values
among word codes (seeds 1-200); z against those 200.
- Power control: 20 C1 texts (seeds fixed in the script) decoded and ranked the same way. Power = share with rank 1 of 201 and z >= 3.
- Gate: if power < 10/20 the target's rank is a **NON-TEST** whatever it is (expected at N=37). Only power >= 10/20 and target rank 1
  with z >= 3 would count as a reading signal.

## Descriptive (no gate)
- f.13r's H-glossed codes that also have a value on the no.71 crop: list both values side by side, count agreements.
- The no.71 alphabet strip ends with a non-numeric sign (loop with a cross above); report whether it matches f.10r's line-opening sign
  (DUCH-KEY1B's description) -- a shape observation, not a statistic.

## Grading (rule 4)
Every decoded f.10r token is **M** (applying a key whose identity with this letter is unshown) unless D is CONSISTENT **and** R passes
its gate, in which case letter tokens on H key rows would be H. Tokens on unread codes are listed as unread, never guessed.
Script: `k71_decode.py [--check]` writes `k71_decode.tsv` (per token) and `k71_score.tsv`; `--check` exits 1 if stale (rule 7).
