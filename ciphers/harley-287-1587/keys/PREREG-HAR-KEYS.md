# PREREG-HAR-KEYS (15 Oct 2026, 05:3x UTC by date -u; LANE DEFAULT-A2-0509-15, account 2)

Pushed before any key record below is viewed. Job: .claude/briefs/runs/2026-10-15-ytbiz-default-0509-jobs.md "HAR-KEYS".

Records: DECODE R330 (SP 106/1 f.50, 1587), R1819/R3822/R3823 (SP 12/193 no.54, 1586), R338/R328/R933 (SP 106/1,
undated), R9260-R9262 (Add MS 4136 ff.177-185, 1560-87). R9261 (Smith 1563) and R9262 (Throckmorton 1560) get their
record page only unless the request budget (<= 25 de-crypt.org requests, one login) leaves room for their images.

Reference (ours, on disk): gloss/key_f84_f90.tsv (Cobham alphabet from the f.84r/f.90r gloss pairs) and Bourdeau's
cobham1588/signs.tsv (github.com/dbourdeau/cyphersolver HEAD 0445769, MIT): glossed codes 7 = her Majesty,
10 = Lord Admiral, 15 = Duke of Parma, 16 = King of Spain. Open groups: 42 (f.70r), 22, 27, the square (f.80r) and
the f.11 (R8477) groups 80, wh24, circled cross, square, Nrp54.

Recording step (before scoring): for each key read from its image, one row per letter in keys/period_signs_HAR-KEYS.tsv:
record, letter, sign shape(s) described in words, and whether the shape is one of Cobham's named shapes for ANY
letter (cup, caret, +, 8, infinity, barred t, 7, barred H, barred x, stem+bowl, inverted T, omega, circle+stem,
horizontal S, double cross, slanted double cross, 2-shape, d, theta-loop, V, gamma, two dots, dot-and-stroke).
Also every number/symbol code the key gives with its referent, and the design class (alphabet only / homophonic /
nomenclator with N codes / code list).

Fit A (alphabet). Score = number of the 16 Cobham letters with gloss n >= 10 (n e c u t d g f i a r l h w y o)
whose principal Cobham sign is listed for the SAME letter in the key. Control: the same count after a random
permutation of the key's letter labels (20 permutations, seed 0). Fit A = score >= 6 AND score > the control maximum.

Fit B (nomenclature). Score = number of Cobham's four glossed codes (7, 10, 15, 16) whose referent the key gives at
the same code. Control: 20 random permutations of the key's code->referent assignment. Fit B = score >= 2 AND
score > the control maximum. A key that gives a value for an open group (42, 22, 27, square, 80, wh24, circled
cross, Nrp54) without Fit A or Fit B is a LEAD only (grade M, a planned decode_key --try step), never a value.

Outcome: a key with Fit A or Fit B becomes a planned --try step; no key.tsv edit in this job (brief). No key with
either fit -> the known-keys rung for the catalogued DECODE keys is ticked [x] (done, none fits); a record whose
image is not served stays named in the line as not seen. This is a lookup against period keys, not a solver run:
the controls test the fit statistic, not the cipher.
