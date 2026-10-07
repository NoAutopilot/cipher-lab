# PREREG D07-PIST40: f.302v T40 per-token crop compare vs the key86 a and s cells (7 Oct 2026, written ~00:5x UTC by date -u)
Pushed before the blind reader is called.

Question (HYPOTHESES.md "kp87b witness"): the 12 f.302v tokens labelled T40 (table a, an `n` with no descender at 8,73)
align to the Colbert copy as s 5, r 1, o 1 (5 unaligned). Is the page sign the table's T40 cell (a conflict with the
table) or another cell the readers labelled T40 -- above all T17 (table s, the circled `n` with a descender at 370,34)?

Material (disk only, no network). Line strips stitched from the committed crops images/f302v_L*_s1/s2 (s2 pasted at
x=1600 from its own x=656, i.e. source x 944 + 656; manifest boxes). Tokens located by eye on 1x/1.6x/2.5x ruler views
of those strips by context (pist40/tokens_pos.tsv), then cut 120 px wide, full strip height, centred on the sign
(PIL crop; tools/iiif_lines.py --region on single-token windows picks the wrong ink row, as in R9-PIS/R9-PIS2), checked
on a montage. Excluded, stay T40/M: L03 i8 (pass A has T16 T17 here and pass B T16 T40 T17; on the strip only one
n-with-descender sign stands between the T16 `m` and the `/`, the same sign as i9 -- a reconciliation double label);
L07 i8 (not located with confidence between the `m` and `a` signs). L11 i11 / i16 are located by estimate plus being the
only n-like signs in their windows (eye-shape-uncertain). 10 test tokens.
Table cells: sources/cryptiana/web/henryiii_Vivonne5.png at key86.tsv cell_xy, cut with
`python3 tools/iiif_lines.py --image sources/cryptiana/web/henryiii_Vivonne5.png --region <x-16>,<y-13>,32,26 --out
ciphers/fr16045-pisany-rome-1585/pist40/cells --prefix k_<T> --lines-per-crop 1 --distance 400 --prominence 1`
for T17 T36 T49 T16 T46 T04, and `--region=0,<y-13>,28,26` for T40 T01 T23 (x=8, x-16 < 0). Nine cells: the a cells
T40 T01 T23, the s cells T17 T36 T49, and distractors T16 (r, circled m), T46 (u, y), T04 (d, an n-like box).

Matched control (must pass before any test token counts), 5 C-graded f.302v tokens whose decoded letter equals the
copy's: T17 x3 (L02 i16, L02 i26, L03 i9; the same n-with-descender shape) and T46 x2 (L03 i6, L04 i2). It can fail
differently from the test: a reader that cannot tell T17 from T40 at the 688 px table copy calls the T17 controls T40.
Control gate: at least 4 of 5 controls SETTLED to their own label (rule below, admissible set = {own label}).
If the gate fails: no test token counts; all are UNSETTLED; logged "non-test at this resolution".

Reader: 1 blind Sonnet call, all 15 crops (shuffled ids R01-R15) and the 9 cells under shuffled labels A-I (seed 20261007,
pist40/blind/cell_labels.tsv, token_ids.tsv -- not shown to the reader). No key, no copy, no transcription, no sign ids,
no values. Per token: best-matching cell label for the sign at the crop's horizontal centre, a second choice, confidence
(low/medium/high), one-line shape description. Reply verbatim in pist40/blind/reader.txt.

My eye classes (from the montage, before the reply), as admissible sets:
- n with a curved descender (the T17 shape): L04 i4, L06 i26, L06 i34, L07 i27, L08 i10, L09 i6, L11 i11, L11 i16, L11 i40
  -> {T17}.
- L06 i36: n whose second leg runs down in a long straight stroke -> {T17, T40}.
- Controls: T17 tokens -> {T17}; T46 tokens -> {T46}.

Settlement rule per token: SETTLED-<cell> iff the reader's top choice is <cell>, confidence medium or high, and <cell> is
in the admissible set. Everything else UNSETTLED. A test token whose top choice is T40 at medium/high is logged READ-T40
(descriptive, a witness for the table conflict) whether or not admissible.

Effect (fixed now): findings go to pist40/t40_tokens.tsv by `python3 pist40/pist40.py` (`--check`). A test token SETTLED-T17
is a transcription label slip: the table's T40 = a is not contradicted by it, and its copy alignment (s) is the T17 value.
If at least 6 of the 10 settle T17 and none is READ-T40, the HYPOTHESES.md "T40 aligns to s 5 of 7" witness is withdrawn as
a label merge (cf. T31). In this job key86.tsv is unchanged in every outcome, the committed tx87b transcription and the
f.302v reading/grades are unchanged; the grade movement a relabel would give is computed on a scratch copy with
kp87b/cgrades87b.py's method and reported descriptively. Committing the labels to tx87b (with a pre-edit copy, decode
--check, regrade, and a verifier flag since f.302v is in AUDIT.md) is a separate, named next step.
