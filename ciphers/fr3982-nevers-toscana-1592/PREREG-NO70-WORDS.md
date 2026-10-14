# PREREG-NO70-WORDS (worker NO70-WORDS, Opus, LANE DEFAULT-A2-2209-14, account 2), written 14 Oct 2026 23:2x UTC by date -u

Committed and pushed before any power or target score. Brief: .claude/briefs/runs/2026-10-14-ytbiz-default-2209-jobs.md
"### NO70-WORDS". Instrument unchanged: `q7test/screen.py` (PREREG-Q7-SCREEN.md, Addendum A beam 6.0, nulls (a) key
shuffle within class, (b) digit shuffle). Wrapper for the power conditions: `q7test/no70w/no70w.py`.

## Key
`q7test/key_no70_full_codes.tsv` = key no.70 alphabet + nulls (q7test/key_no70_codes.tsv, 64 rows, unchanged) + the 24
barred Arabic-figure codes of the f.131r nomenclator (54, 56-78; `keys/key_no70_nomenclator.tsv`, this job). The barred
figures are entered as polyphones of the same two digits (f.25's transcription does not record bars). The letter-coded
and Roman-numeral word columns cannot occur in an all-digit string and are not in the screen key.

## Power (before the target number is read)
50 held-out Italian windows (letterediprincip03char, as PREREG-Q7-SCREEN), enciphered with this key by screen.encipher
(3% nulls; a word code is used only when an Italian word equals a folded meaning, which in practice never happens --
declared: the control measures the alphabet-plus-word-code decoder on alphabet-enciphered text), 100 + 100 nulls each,
seed 70. Conditions: C1 0.115 and C2 0.160 digit error (screen.corrupt mix), C3 "8-loss" (every 8 rendered 6, 3, 01 or
dropped, as PREREG-TUSC-XM) + 0.07 error.
**Licence: power >= 0.80 at C2 AND at C3.** Otherwise the target result is a NON-TEST for key no.70 (alphabet + word
codes) at this transcription, whatever it reads; reported as such.

## Target
`screen.py target --key q7test/key_no70_full_codes.tsv` on ciphertext.tsv (`?` removed, N = 260; not ciphertext_v2.tsv),
1000 + 1000 nulls, seed 25. Fit iff p_a <= 0.01 AND p_b <= 0.01 (as PREREG-Q7-SCREEN). Reported beside the alphabet-only
run of 13 Oct (S -1.259, p_a 0.078, p_b 0.26). The best path is a draft, grade M at most; a licensed fit goes to a
separate verifier, a licensed no-fit is "no fit at this transcription"; an unlicensed run is a non-test either way.
