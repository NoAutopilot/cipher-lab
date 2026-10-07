# D07-CEP21 pre-registration: f.21v S10/S26 and S13/S69 by witness shape (7 Oct 2026, account 1)

Written and pushed BEFORE any f.21v tile of these pairs was opened in this job. Brief:
`.claude/briefs/runs/2026-10-07-account1-default-0042-jobs.md` (D07-CEP21), for LANE DEFAULT-account-1-20261007-0042.

## What the witness holds (read from files before any tile; no new gloss read)
- Printed sheet (`sources/cryptiana/web/img/nevers_add1.png`, boxes in `../../sign_id_map.json`): S13 = g, a small closed oval with a
  short tick inside; S69 = f, a cursive loop crossed by ONE horizontal bar running out past both sides; S60 = r, a steeper loop with
  one bar; X_THETA2 (off-sheet) = r, an oval with TWO bars. S10 = s (row 4) and S26 = s (row 1, a 9-like loop with a dot, underlined).
- fr.3252 f.36v glosses (`../../witness_f36/alignment_pairs.tsv`, HARVEST-D; birago `harvest/f36/recon.tsv` grade C):
  S13 glossed **g** x1 (v36top_L01_s2 pos 15, both gloss readers g); S26 glossed **s** x2; the double-barred oval glossed **r** x1
  (v36top_L01_s1 pos 3; that position was read S69 by one sign reader and X_THETA2 by the other). **No glossed S69 and no glossed S10.**

## Rules
- R-g: a small closed oval with a mark inside it and NO stroke crossing outside the oval -> S13 (g). Glossed side (x1).
- R-bar: an oval/loop crossed by a bar that runs out past both sides of the loop: one bar -> S69 (f); two bars -> X_THETA2 (r).
  The single-bar = f side rests on the printed sheet only (no gloss): it is the weak side.
- R-s: S10 vs S26 cannot change a letter (both s). The tiles are read and the label recorded, but no value or grade can move;
  the five S10/S26 split tokens are already S (s). Reported, not scored.
- A tile whose interior mark or bar cannot be judged at 4x is UNDECIDED and keeps its label and grade.

## Units
Primary (S13/S69 family, value-bearing): L06.2.15 (passD S13 M), L10.6, L11.4, L11.22 (passD S69 M); also L09.3 (passD X_NEW; B S13),
L11.2 (passD X_NEW; cand S13), L06.2.12 (passD X_THETA2 M; cands S60/S69). Secondary: S10/S26 splits L03.24, L04.10, L04.15, L05.7,
L05.28, L07.34. Tiles cut at 4x from `../c23_cipher_w.jpg`, located by passD neighbours (crop command pasted in NOTES.md). Reader:
this worker's eye, value-blind (reads written to `s13s69_reads_f21v.tsv` before any decode or score is run). No subagent.

## Decision and gates (as D22-CEPPO21 / A1B-CEPPO-87)
A label change is made only if (i) the rule settles the tile, (ii) `../../decode_control.py <seq> --shuffles 200 --windows 20 --err 0.15
--extra X_THETA2=r` ranks 1/201 with power >= 18/20 (seed 1; seeds 2-3 if a label changes), and (iii) the judge score is not worse
than the current reading (each flip alone, then the set). Grades: M -> S only if the tile is decided on the GLOSSED side (R-g -> S13, or
R-bar two bars -> X_THETA2) and the score agrees; a tile decided on the unglossed single-bar side (S69) stays M whatever the score
(no gloss behind it). A flip whose score drops keeps the current value at M. Current S tokens the rule contradicts: data conflict, M.
Control that can vary on the statistic (the score): the same number of random g<->f relabels among f.21v's S13/S69/X_NEW-family
tokens, 500 draws, p = share reaching the real score -- run only if a label changes.
Retirement: if fewer than 4 of the 7 primary tiles are decidable at 4x, the step is [retired] for f.21v (instrument: R-g/R-bar read
at 4x on c23_cipher_w.jpg).

## Correction (appended after the read, 7 Oct 2026 01:2x UTC; the text above is unchanged)
This file was written to disk at 01:12:56 UTC, before the first tile (01:13:34) and the reads file (01:14:50) existed (file mtimes),
but it was NOT pushed before the read: the `tools/room.py "<role>" "<text>" --push <path>` call committed only the ROOM.md line
(629f40012), not this file. It is committed with the results. The "pushed BEFORE" line above is therefore wrong; the rule was fixed
before the read on this worker's disk only, which a reviewer cannot check from git.
