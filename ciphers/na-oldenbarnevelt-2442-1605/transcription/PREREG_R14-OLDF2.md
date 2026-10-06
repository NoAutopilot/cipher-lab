# PREREG R14-OLDF2 (6 Oct 2026, written and pushed before the blind call)

Job: NOTES section 18 Verdict step (f'). LANE LANE-RUN14-account-2. Rules of transcription/PREREG_R14-OLDF.md items 2-4 apply unchanged.

1. Units: C1_29, C1_31, C1_36, C1_44 (the four R14-OLDF rows the reader shifted) plus C1_05 (flagged b8s424 / b8ss424).
   Crops re-cut tight on native scan 006: `python3 scripts/token_crops_R14OLDF2.py` -> images/crops_R14OLDF2/T1-T5.png,
   neutral labels (map in transcription/R14OLDF2_labels.tsv), order shuffled against the text so a shift cannot land on a neighbour.
   Each crop eye-checked by the worker against a wider view of lines 1 and 4-6 before the call.
2. One blind Sonnet call on the five 3x crops; the reader reports one row per file name (label in every row), no key, no committed
   rows, no values; OLD-PASS2 notation.
3. Change rule: PREREG_R14-OLDF item 3 (blind reader names a different sign AND the image settles it; look-alike naming pairs 9/q,
   f/p long descender, v/r, l/t, u/v-2 never count as a change). A sign insertion (doubled s, doubled p, extra sign) counts as a change
   under the same two conditions.
4. Re-judge only if a sign changes: scripts/segment_judge.py unchanged under PREREG_R13-OLDSEG.md; otherwise no judge run.
