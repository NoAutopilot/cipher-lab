# PREREG-FT4w (account-4, 3 Oct 2026, written 13:55 UTC by the clock; pushed before any draw below is run)

Job: finish the f.249/f.250 one-edit control draws under the FT4l solver so the pair has its own gate result.
Nothing new is registered: design, statistic, draws and gate are exactly amendment FT4l (PREREG-FT4i.md, 75bf2422)
as run by FT4n (PREREG-FT4n.md, 4b43952c). This file only fixes the run plan of this box.

- Command, unchanged: `python3 align/one_edit_seg.py --pair f249 --ctrl s|g --dec --draws i-j` (seed 3, n 40,
  sublimit 10 s, Pool(4)). Draws are the registered seed-3 draws; FT4n's (s) 0-9 (0 of 10 fit, all resolved,
  `ctrl_s_f249_dec_b1.out`, `_b2.out`) and real E = 1 (`real_f249_dec.out`) stand and are not re-run.
- Environment note: fresh container, ortools 9.15 installed from PyPI (FT4n's version not recorded). A draw is solved
  exactly or reported unresolved, so a version difference can only move a draw between resolved and unresolved.
- Run: (s) 10-39 then (g) 0-39, blocks of 5 draws, foreground, nothing else running in the container; commit and push
  the block outputs about every 30 min. Pooled summary `ctrl_s_f249_dec_pooled.out`, `ctrl_g_f249_dec_pooled.out`.
- Box 160 min from 13:56 UTC; stop before a block that would start after the 80 pct line 16:04 or is likely to cross it.
- Gate (unchanged, PREREG-FT4i/FT4l): PASS iff E_real = 1 AND each control's E=1 share <= 0.05 (<= 2 of 40), unresolved
  draws counted E = 1. Share > 0.05 with resolved fits > 2 of 40: NON-INFORMATIVE (one edit fits wrong pairings).
  Share > 0.05 from unresolved only: NON-INFORMATIVE (power); the one-edit gate is then [retired] for this solver on f.249.
  A control not completed is reported as not scored with its draw count, never as a partial gate.
- Decisive outcome and key rule: a PASS licenses only "the f.249 groups and the f.250 slip are the same passage up to one
  edit" (FT4i's nine fitting edits, all at FT4e's suspect codes 253/242/66); it does not move any value. Nothing enters or
  moves in key.tsv this step whatever the result; a PASS gets a VERIFY flag line in ROOM.md, never a status change.
