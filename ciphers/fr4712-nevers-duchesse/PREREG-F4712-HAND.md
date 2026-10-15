# PREREG-F4712-HAND (worker F4712-HAND, LANE DEFAULT-A1-0447-15, account 1, 15 Oct 2026, written ~05:05 UTC by date -u)

Pushed before any image of this job is looked at and before the scored call. Question: is f.13r's figure hand the same as
f.10r's? Output is a same-writer **lead graded M at most**, never a reading. This job changes no grade in f13_carry.tsv: the six
C carries rest on ASKS 113 (5 Oct 2026); a result here is logged beside them as supporting or conflicting evidence.

## Panels (value-free: images only, no code values, readings or glosses typed by us)
- **R (reference)**: f.10r line 1, `images/f10_L01_s1.jpg`, `images/f10_L01_s2.jpg` (~33 digits, several 8s). 2 images.
- **P (positive control, same writer by construction)**: f.10r line 2, `images/f10_L02_s1.jpg`, `images/f10_L02_s2.jpg` (~30 digits). 2 images.
- **T (target)**: f.13r lines 1, 3, 6, 7, 13, 15, each `images/f13r/f13g_LNN_s1.jpg` stacked over `..._s2.jpg` into one image
  (codes 6 82 58 / 41 3 40 / 39 4 9 11 / 21 40 10 / 37 93 / 54 58 41 by DUCH-F13's two passes: ~33 digits, all of 0-9, 8 three times). 6 images.
- **N (negative control, a different hand in the same volume)**: f.107v foot, the Arabic-figure account columns (249427, 74446,
  332127 ..., F4712-C107), an account clerk's figures in a financial document, not Nevers' letters; one native region from
  openapi.bnf.fr (canvas 118), cut into 2 strip images. If the region shows fewer than ~20 digits, a second region from the same
  columns is fetched (<= 3 requests in all). 2 images.
Total 12 images. Size and ink weight are not to be weighed (f.13r is a larger, heavier hand by DUCH-F13's note); the subagent is told
to compare construction (strokes, loops, entry/exit, closure), which is what a hand comparison of figures uses.

## Blinding
P, T, N go to the subagent as candidates labelled W, X, Y (order from `random.Random(4712).sample(['P','T','N'],3)`, computed by
script after this file is pushed; the subagent never sees this file or the folio names). R is labelled R.

## Call (one unit)
One Sonnet subagent call. It writes, per digit 0-9: R's form (one line), then for each candidate `same` / `different` / `absent` /
`unsure`; then one overall score 0-10 per candidate (10 = surely the same writer as R); then a separate line on how each panel writes 8.

## Metrics and gates (fixed now)
- share_X = same / (same + different) over digits not absent or unsure in X. score_X = the overall score.
- **Calibration gate**: score_P >= 6 AND score_P - score_N >= 3 AND share_P - share_N >= 0.30. If any fails: **NON-TEST**, nothing
  about the hand is concluded (as R11A-F4712).
- If calibration passes:
  - **same-writer lead (M)**: score_T >= score_P - 1 AND share_T >= share_P - 0.15;
  - **different-writer lead (M)**: score_T <= score_N + 1 OR share_T <= share_N + 0.15;
  - otherwise **undecided**.
- The 8-form line is reported beside the verdict and does not override it.
- No second call, no re-labelling, no change of panels after the result. A second shuffled replication is run only if the
  calibration passes and the first call leaves cost under 80% of the cap; it is reported, not used to overturn the first.
