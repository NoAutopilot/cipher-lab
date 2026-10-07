# PREREG D07-PISSD: f.302v T40 tokens vs the page's own C-graded T17 tokens, blind same/different (7 Oct 2026, written ~01:1x UTC by date -u)
Pushed before the blind reader is called. Disk only. Follows D07-PIST40 (table-cell compare a NON-TEST, control 1/5).

Question (HYPOTHESES.md "kp87b witness"): are the 10 located f.302v T40 tokens (table a, plain n) the same page sign as the
page's C-graded T17 tokens (table s, n with a curved descender), i.e. a reconciliation label merge as with T31?
No table crops: every image is cut from the same page.

Material: line strips stitched from images/f302v_L*_s1/s2 exactly as D07-PIST40 (pissd/strip.py; verified against 3 pist40/tok
crops, mean abs pixel difference < 1). Tokens pissd/tokens.tsv (120 px wide, full strip height, centred at x_centre_strip):
10 test T40 (pist40 positions), 3 C-graded T17 (S1-S3), 5 C-graded T16 (M1-M5, table r, an m whose last leg descends:
the hardest look-alike of the T17 shape on the page; located by eye on ruler views by context, montage checked),
2 C-graded T46 (Y1-Y2). Caveats fixed now: S3 (L03 i9) stands beside the excluded double-labelled L03 i8 sign, so its crop is busy;
M2's m sits a little left of centre. The red triangle marks the sign to judge in each half.

Pairs pissd/pairs.tsv (27): 10 test (each T40 token vs one T17 control, rotating S1-S3); 7 known-same (T17-T17 x3,
T16-T16 x3, T46-T46 x1); 7 known-different (T17-T16 x4 = hard, T17-T46 x2, T16-T46 x1); 3 decoys (T40 vs T16, descriptive).
`python3 pissd/pissd.py build` shuffles pair order and left/right (seed 20261007) into pissd/blind/Q01-Q27.jpg; the answer
key pissd/blind/key.tsv is not shown to the reader.

Reader: 1 blind Sonnet call, the 27 pair image paths only. No key, copy, transcription, sign ids, values, or the fact that
some pairs are controls. Per pair: SAME or DIFFERENT (same written sign type, allowing for hand variation), confidence
low/medium/high, one-line reason. Reply verbatim pissd/blind/reader.txt (tab-separated q, answer, confidence, reason).

Control gate (per class, not blended; CLAUDE.md rule 3 unbalanced-class lesson): a control is right iff the answer is correct
at medium/high confidence. PASS iff known-same >= 6/7 AND known-different >= 6/7 AND hard T17-T16 >= 3/4.
The control can fail differently from the test: a reader that lumps all n-with-descender signs calls the T17-T16 pairs SAME;
a reader that splits on hand variation calls the known-same pairs DIFFERENT.
If the gate fails: no test pair counts; logged non-test; this is the third instrument on T40 (rule 3 third-attempt clause) and the
step is marked [retired] with the instrument named, unless a genuinely different instrument remains.

Test settlement: SAME-T17 iff answer SAME at medium/high; DIFF-T17 iff DIFFERENT at medium/high; else UNSETTLED.
Verdict: MERGE iff >= 6 of 10 SAME-T17 and 0 DIFF-T17 -> the "T40 aligns to s 5 of 7" witness is withdrawn as a label merge
(the settled tokens are T17 = s, consistent with the copy); DISTINCT iff >= 6 DIFF-T17 and 0 SAME-T17 -> the table conflict
stands as a real witness; otherwise OPEN.
Effect in this job, every outcome: key86.tsv, tx87b, the f.302v reading and grades unchanged. Committing relabels to tx87b
(pre-edit copy, decode --check, regrade, verifier flag since f.302v is in AUDIT.md) is a separate named next step.

My eye (montage, before the reply): every test token has the T17 curved-descender n shape, except A4 (L06 i36) whose descender
is straight -- expect SAME on 9, A4 unsure; T16 controls show three legs and a straight descender. This is the hypothesis, not a result.
