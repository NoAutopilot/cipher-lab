# D22-CEPPO21 pre-registration: f.21v S65/S80 by the R-8 witness shape rule (6 Oct 2026, account 2)

Written and pushed BEFORE any f.21v 8-tile was opened in this job. Brief: `.claude/briefs/runs/2026-10-06-account2-default2209-jobs.md`
(D22-CEPPO21), for LANE DEFAULT-account-2-20261006-2209.

## Rule (reused, not re-derived)
R-8 from `../../../../birago-fr3252-1571-72/harvest/witness_pairs/PREREG.md` (e1760f2e; fr.3252 f.36v period gloss): an 8 with a
stroke through the waist running out past BOTH sides -> S80 (a, glossed x6); an 8 with no such stroke -> S65 (et, glossed x1).
A tile whose bar cannot be judged (ink blot, overlap, faint) is UNDECIDED and keeps its current label and grade.
No new glossed plain 8 is sought (the witness's single plain-8 gloss stays the only one; the S65 side of the rule is the weak side).

## Units
Primary: the 15 f.21v S65/S80 split tiles in `f21v_L01-06_tiles.tsv` / `f21v_L07-11_tiles.tsv` (status split+adj):
L01.4, L01.10, L01.27, L02.2.2, L03.20, L03.26, L03.28, L03.34, L03.39, L04.17, L06.2.1, L06.2.6, L06.2.13 (passC S80; A S65, B S80),
L09.5 (passC S80; A S80, B S65), L11.9 (passC S65; A S80, B S65).
Secondary (same read, reported, no grade change unless the rule disagrees with the label): the other f.21v S80/S65 tokens in
`../../reading_f21v_tokens.tsv` (L01.32 S65 and the S80 tokens outside the split list), as far as the cap allows.
Location: by passC neighbours on 4x tiles cut from `../c23_cipher_w.jpg` (crop command pasted in NOTES.md). Reader: this worker's
own eye, value-blind to the decode (no decode run until all tiles are judged and written to `r8_reads_f21v.tsv`).

## Decision rule and gates (as CEPPO-WITNESS-PAIRS / VERIFY-CEPPO-WP / A1B-CEPPO-87)
A token's label is changed, and graded S, only if (i) R-8 settles the tile, (ii) the re-decode's key control at f.21v's two-reader
error (0.15; `decode_control.py <seq> --shuffles 200 --windows 20 --err 0.15 --extra X_THETA2=r`, seeds 1-3) still ranks 1/201 with
power >= 18/20 in every seed, and (iii) the judge score (`tools/judge_plaintext.py specs/ceppo-nevers-fr3251-1570s.json`) is not
worse than the current reading. Flips are scored as a set and, if (iii) fails for the set, one at a time; a flip whose own
score drops keeps the current value at M (shape and score disagree -> M). A token whose shape AGREES with its current label and
is currently M moves to S (score unchanged by construction; the shape is the new evidence). Current S tokens that the rule
contradicts are a data conflict for the verifier, not regraded here beyond M.
Matched control for the flip set (can vary on the statistic, the judge score): in-family flips -- the same number of random
S80<->S65 flips among f.21v's 8-tokens, 500 draws, p = share reaching the real set's score (as CEPPO-WITNESS-PAIRS). Reported
beside the real number.
Instrument retirement: if fewer than 8 of the 15 primary tiles are decidable at 4x, the step is marked [retired] for f.21v with
the instrument named (R-8 witness shape read at 4x on c23_cipher_w.jpg).
