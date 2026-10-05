# RUN6-BIR3637 pre-registration (5 Oct 2026, 05:4x UTC, before the reconciliation call)

Job: one reconciliation call (1 Sonnet subagent call = 1 unit; no other vision call) on the 193 split positions of the kept
F36-READ rows (r36_L01-L08, v36top_L01-L06, v36mid_L01-L06, r37_L01-L02; all but r36_L09-L15), F36R-REREAD's method:
`adjudicate_in.tsv` (build_in.py) -> `adjudicate_out.tsv` (prompt_R.md, crops from cut_lines.cut(..., 850, 0, 120, 65, 2)).

Measures, fixed now:
1. E before = (one-sided 40 + split 193) / 700 = 0.333 (F36R-REREAD error.tsv). This is the blind two-reader figure and stays it.
2. E after (reconciled residual) = (one-sided 40 + splits NOT settled at H or M) / 700. Only H/M choices are applied, as F36R-REREAD.
   Reported beside E before; it is a residual-disagreement figure after one eye, not a measured per-sign error (TRANSCRIPTION.md).
3. Control (rule 3): `decode_control.py passD_v3.tsv --shuffles 200 --windows 20 --err <whole-letter E before = 0.286> --extra X_THETA2=r
   --seed 1,2,3` on the spliced transcription (v2 with the H/M choices applied). Gate: the printed key ranks 1/201 on every seed.
   Report z beside v2's 6.25 / 6.51 / 7.82 (reconciled v2). A higher real-key score with the same shuffle distribution reads as
   "the reconciled rows read better under the printed key"; a lower one is reported as such. No C grades from this job.
4. If more than half the 193 come back '?' or L, the call is reported as non-discriminating and nothing is spliced.
