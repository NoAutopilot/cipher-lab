# PREREG-HEID1621G (written before any fetch, crop or reader call; 15 Oct 2026, 21:2x UTC by date -u)

Job: two-block transcription for ciphers/brederode-heidelberg-1621. Brief: .claude/briefs/runs/2026-10-15-acct4-depth-steps-2.md, JOB HEID-1621G.
No decode, no key, no reading; nothing here assigns a value to any unit.

## Material
- Block A: NA 1.01.02 inv. 6021 scan 375 (signed letter, Heidelberg 13 Aug 1621), left-page numeral block.
- Block B: scan 423 (letter of 17 Sept 1621, signed on 424), two lines of dotted numeral groups inside the prose.
- Reference for the control: ../ciphertext.tsv (= scan 379, the duplicate of block A's letter, HEID-1621; all M).

## Fetch (service.archief.nl <= 8, >= 3.1 s apart, take/release lines in ROOM.md)
Scans 375 and 423 at 1200 px (2 requests) to place the blocks; then one native-resolution region per block (2 requests;
the same route as HEID-1621's 379 crops, so the control compares like with like); up to 4 spare for a region re-cut.
Nothing committed; sha1s into ../images/manifest.json (key heid_6021g). Crops by `tools/iiif_lines.py --image <region> --out <dir>`,
command pasted in NOTES.md before the first reader call.

## Readers
Per block: two blind Sonnet readers (independent, same prompt, no key, no 379 text, no prior sighting shown), given only the line
crops; each returns text only, per line, tokens in order: numerals, dots, letters, other signs, and clear words abridged as [clear].
Then one reconciliation per block by a third call (or this worker) against the crops, settling only where A and B split.

## Unit grammar (recorded before reading)
A unit is a maximal run of numeral tokens followed by one letter token (the letter closes it). Forms:
- P: two numbers + letter ("22 23 x"); S1: one number + letter ("22.x"); N: numbers with no closing letter before a clear word, a sign
  or the block end (bare numbers, "43"); L: a letter with no number before it (bare letter, "a").
- Dots are separators and are recorded but do not change the unit. A unit may wrap across a line end.
- Unit id = numbers joined by "." + "." + letter (letter lower-cased; "x" and "r" not merged: kept as transcribed).

## Grades
Per token: both readers agree (after reconciliation shows the same reading) = S for the digits/letters as transcribed; any split = M,
with the alternative in `alt`. No value is read, so nothing is H or C. (S here means "transcribed sign agreed by two blind readers",
not a deciphered value.)

## Known-answer control (gate, run on block A before block B's result is used)
Units of block A (scan 375 reconciled) vs units of ../ciphertext.tsv (scan 379), aligned in order (difflib SequenceMatcher on the unit
id sequences). Per-unit agreement = matched units / max(units in 375, units in 379). **Gate: >= 0.90.** Below the gate the pass is a
non-test: block B's transcription is still written (graded M throughout) but no inventory claim is made from it.
Note (rule 3, control able to fail): the 379 text was itself read by two blind readers + reconciliation; the two witnesses are
separate scribal copies, so a real copying variant also lowers agreement -- disagreements are listed per unit, not explained away.
Also reported: per-token agreement (numbers and letters separately) and the A-vs-B reader split rate per block.

## Outputs
ciphertext_6021_423.tsv and ciphertext_6021_375.tsv (line, pos, unit, numbers, letter, confidence, why);
agree_375_379.tsv (per-unit alignment); units.tsv (unit id, form, numbers, letter, n_13aug, n_17sept); units.py regenerates
agree and units from the two TSVs and ../ciphertext.tsv (rule 7 --check).

## Question fixed in advance
For every S1 unit of block B: is its number the first number of some P unit in block A/379 with the same letter? Report k of n.
Stop rule: the cap USD 11 or 80% of the 90-minute box (22:43 UTC end), whichever first; no unit started past 80%.
