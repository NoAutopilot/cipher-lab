# GAPS33 pre-registration (3 Oct 2026, written and pushed before any reading; clock read 06:20 UTC)

Step (GAPS31 Verdict): a blind reading of each band occurrence's local window in 5810/5811 against Groen's print,
mixed with masked C null and C letter occurrences as the known-answer control, graded per class. Third instrument
family on gap 1 after the fr16 char LM (A2-LVN3), fr16 word segmentation (GAPS28) and interlinear_align (GAPS31).

Material: `gaps33/build.py` (deterministic, seed 33; locate rule in its docstring, fixed before any reading) wrote
`windows.txt` (67 items, shuffled) and `answers.tsv` (never shown to a reader). Each item: the key_full decode of up to
15 tokens either side with the target masked as [?] (C/H nulls dropped, unread codes as `_`, codes never shown) and the
Groen print around the located spot (Groen IV CDLXVIII for 5810, CDLXXXIII for 5811), no marker in the print.
Kept: band 17 (140 x4, 142 x4, 139 x3, 149 x3, 147 x2, 125 x1), C null 25 (codes 121-144, at most 3 per code),
C letter 25 (single-letter C codes, at most 3 per code). Dropped by the locate rule: band 6 (all of 150's 2, one each
of 140/142/149/139), C null 4, C letter 4 (`dropped.tsv`). Classes are balanced 25/25 in the control, so the shuffle
floor is not class-dominated (AX-NAMES per-class paragraph); per-class figures are reported, never a blended one alone.

Readers: two blind Opus 5.5 passes (subagents, text only, the windows pasted into the prompt, told not to open any
file), each answering per item NULL (the masked cipher token stands for no printed letter) or one letter, with
confidence high/low. One reconciliation pass (Opus 5.5) sees both passes' answers and the windows (never answers.tsv)
and gives one final call per item, or SPLIT if it cannot settle it. A SPLIT counts as wrong in the control and as no
observation for a band code.

Gate on the reconciled calls (all three, else nothing is applied):
- G1: C-null items called NULL >= 0.80 (>= 20 of 25).
- G2: C-letter items called letter (class, not value) >= 0.80 (>= 20 of 25).
- G3: false-NULL rate on C-letter items q <= 0.316 (<= 7 of 25), so 4 unanimous NULL calls on a letter code have
  probability <= 0.01. Letter value accuracy on C-letter items is reported, not gated.
The control can come out differently from the target on this statistic (a reader can call a masked null a letter or a
masked letter NULL), so it is a test, not a by-construction tie (rule 3).

Licence (only if G1-G3 pass): a band code becomes NULL at grade C (class b) iff >= 4 reconciled NULL calls and 0
letter calls in this run AND no occurrence contradicts names.tsv's observation at the same occurrence (rule 4: a
conflict is logged, never settled by majority). A band code with >= 4 calls of one same letter and 0 NULL is recorded
as an M hypothesis in HYPOTHESES.md, not applied. At this N only 140 and 142 can reach 4; 139/149/147/125 cannot and
are recorded only. If a code is lifted: key_full row with source "GAPS33 local-window reading", readings regenerated,
decode --check exit 0.
If the gate fails: this is the third instrument failing (or contradicted) on the same band codes; per rule 3's
third-attempt clause the band step is logged [retired] for these instruments and the Verdict names new material.
No item, prompt rule or threshold is changed after the first reading.
