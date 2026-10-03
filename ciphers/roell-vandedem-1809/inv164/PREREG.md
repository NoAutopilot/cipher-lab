# READ2-ROELL pre-registration (3 Oct 2026, 23:4x UTC, committed before any vision call or native fetch)

Brief: `.claude/briefs/runs/2026-10-03-acct2-read2-roell.md`. Question: does the large one-part word table of
NA 1.02.20 inv. 164 (scans 1-8, 1747) key the letter R1469+R1470 (2,585 groups, Bourdeau's parse of the DECODE
transcription, `decode_transcription/`)? Conditional on that transcription (rule 2: no page image of the letter).

## Words (fixed now, before reading any function-word entry)
de, la, le, et, que, les, des, a (à), en, du, pour, qui, il, est, ne, pas, par, sur, se, au  (20 words).
Every code number the table assigns to one of these words counts, including variants written in the same entry
(e.g. "a" and "à", homophone numbers in the same cell). Entries that only contain the word as part of a phrase
("de la", "que le") count as a separate code under the first word only if the reader records them; they are listed
but scored in S1 only when the entry is the bare word (phrase entries reported separately).

## Statistics
- S1 (primary): sum over the read codes of the letter's frequency of that number (2,585 groups).
- S2 (secondary): how many of the read codes are among the letter's 20 most frequent groups.

## Control (rule 3 orthogonality)
Shuffling group order cannot change a frequency, so the control is a random-code-set null: 1,000 sets of the same
size k (k = number of read function-word codes), drawn without replacement uniformly from the integers the table's
read columns cover (every integer in a one-part numbered table is a code). Same statistics. PASS = S1 above the
control's p99 (20 words tested at once; p99, not p95). S2 compared with the control's p99 likewise, reported only.
A second control draws from 1..3000 (the whole table range) and is reported beside it.

Expected sizes if the table keys the letter: ~20 French function words carry roughly 25-35% of running tokens, so
S1 of several hundred groups; random k~20-30 codes give about k x 0.86 (2,585 / 3,000) groups.
A heavily homophonic code (Bourdeau: no group above 1%) whose homophones are not in this one-part table would also
read as a miss; that is part of what a miss means ("this table, as one code per word, does not key the letter").

## Range share (computed before looking at the table, on the letter's groups)
2,585 groups, 931 distinct, max 7205 (two misreads per Bourdeau, 5100 and 7205; next 3264).
Share at or below 3000: 99.88% (2,582 of 2,585). The table's range (1 - about 3000, LIKELY-7 headers of scans 1
and 3) covers the letter; range is not exclusionary.
Top 20 letter groups: 460, 804, 1576, 394, 850, 1390, 75, 357, 185, 1341, 331, 255, 686, 226, 577, 211, 35, 1285, 296, 554.
