# PREREG-F4712-8 (worker F4712-8, LANE DEFAULT-A1-0447-15, account 1, 15 Oct 2026, written ~05:50 UTC by date -u)

Pushed before any image of this job is looked at, before any tile is cut and before the scored call. Question: is f.13r's figure 8
constructed the same way as f.10r's (the one figure F4712-HAND did not compare: its reader did not recognise f.10r's open ɑ-form as an
8)? Output is a same-writer **lead on the 8, graded M at most**, never a reading. This job changes no grade in f13_carry.tsv: the six
C carries rest on ASKS 113 (5 Oct 2026); a result here is logged beside F4712-HAND's lead as supporting or conflicting evidence.

## Tiles (one figure 8 each; all at native resolution; no code values, readings, glosses or folio names given to the reader)
The 8 positions come from the committed transcriptions (ciphertext_f10_digits.tsv; f13_passA/B.tsv), placed by my own look at the
line crops (a placement look, not a judgement). Each tile is a tight box around one 8 with ~20% margin (neighbour strokes may show at
the edges), converted to greyscale with autocontrast, and scaled so all 12 tiles have the same height.
- **R (reference), 3 tiles**: f.10r line 1, the 8s of the opening "82 82" and of "85" (`images/f10_L01_s1/_s2.jpg`, native).
- **P (positive control, same writer by construction), 3 tiles**: f.10r's other 8s -- line 1 "...92 8 59" and line 2 "78", "85"
  (`images/f10_L01_s2.jpg`, `images/f10_L02_s1/_s2.jpg`); if one is unusable (blot, overlap), line 3's "81" (`images/f10_L03_s1.jpg`).
- **T (target), 3 tiles**: f.13r's three 8s -- line 1 "82" and "58", line 15 "58" (`images/f13r/f13g_L01_s1/_s2.jpg`,
  `images/f13r/f13g_L15_s1/_s2.jpg`, native).
- **N (negative control, a different hand in the volume), 3 tiles**: 8s from f.107v's Arabic-figure account columns (canvas 118, the
  account clerk's figures F4712-HAND used as its N), fetched at native resolution from openapi.bnf.fr, region `pct:0,55,50,45`
  (1 request). If that region shows fewer than 3 legible 8s, a second region from the same leaf's figure columns (<= 4 requests in all).
  If still fewer than 3: N uses what there is (>= 2) and this is reported; with fewer than 2 the job stops as NON-TEST before the call.

## Blinding
P, T, N go to the reader as groups labelled W, X, Y (order from `random.Random(8).sample(['P','T','N'],3)`, computed by script after
this file is pushed); tiles within a group in transcription order, named e.g. `X2.jpg`. R's tiles are R1-R3. The reader is told only that
each tile is cut around one handwritten figure 8 from 16th-century manuscripts and that writers form an 8 in different ways (a closed
figure-of-eight, an S-like single stroke, an open ɑ-like loop, others). The identity "8" is given because it is the subject of the panel
(F4712-HAND's reader read the open form as a crossed 0); nothing else is.

## Call (one unit)
One Sonnet subagent call, 12 images. It writes: R's construction (stroke order if visible, number of passes, which bowls are closed,
entry and exit, any crossing) from R1-R3; then for every candidate tile `same` / `different` / `unsure` against R's construction;
then one score 0-10 per group (10 = surely the same writer's way of making an 8 as R). Size and ink weight are not to be weighed.

## Metrics and gates (fixed now, the same structure as PREREG-F4712-HAND.md)
- share_G = same / (same + different) over G's tiles not `unsure`; score_G = the group score.
- **Calibration gate**: score_P >= 6 AND score_P - score_N >= 3 AND share_P - share_N >= 0.30. If any fails: **NON-TEST**, nothing
  about the 8 is concluded. (The control can differ from the target on this statistic: N's 8s are a different writer's, and if that
  writer happens to make the same open 8, the gate fails and the job says so rather than reading T.)
- If calibration passes:
  - **same-8 lead (M)**: score_T >= score_P - 1 AND share_T >= share_P - 0.15;
  - **different-8 lead (M)**: score_T <= score_N + 1 OR share_T <= share_N + 0.15;
  - otherwise **undecided**.
- No second call, no re-labelling, no change of tiles after the result. No replication (cap 3 on an Opus floor of ~2.4).
- Interpretive limit, fixed now: an open ɑ-form 8 was a common period form (key no.1's sheet in this volume writes it too, NOTES
  DUCH-KEY1B), so even a same-8 lead is weak evidence of one writer; a different-8 lead is evidence of a different habit, which one
  writer can also show in two documents. Either is logged as M beside ASKS 113, never as a grade change.
