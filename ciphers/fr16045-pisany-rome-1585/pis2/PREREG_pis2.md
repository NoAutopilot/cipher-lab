# PREREG R9-PIS2: T31 per-token crop compare vs the T45 / T36 table cells (6 Oct 2026, written ~06:3x UTC by date -u)
Pushed before the blind reader's replies are opened.

Material (disk only, no network): 11 T31 tokens in tx86/ciphertext_f244r.tsv and 13 in tx86e/ciphertext_f275r.tsv
(pis2/tokens_pos.tsv). Each token located by eye on a full-line strip stitched from the committed line crops
(images/f244r_L*_s1/s2, images/f275rL_L*_s1/s2; s2 pasted at x=1360 / 1250), then cut full strip height, 150 px wide,
centred on the sign (pis2/tok/). f244r L09 i26 (T29 T18 [T31] T25 T21) was not located by eye: excluded, stays T31/M.
Table cells: henryiii_Vivonne5.png at key86.tsv cell_xy, 32x26, cut with
`python3 tools/iiif_lines.py --image sources/cryptiana/web/henryiii_Vivonne5.png --region <x-16>,<y-13>,32,26 --out
ciphers/fr16045-pisany-rome-1585/pis2/cells --prefix k_<T> --lines-per-crop 1 --distance 400 --prominence 1`
for T31 T36 T45 T30 T17 T49 T47 T42 (T31/T36/T45 the hypotheses; T47 a second x-form cell, also m; the rest distractors).
Note: tools/iiif_lines.py --region on the token windows picked the wrong ink row or clipped the sign (as in R9-PIS), so the
token crops are PIL crops (pis2/tokens_pos.tsv x_centre_strip, x +/- 75, full strip height); checked on a montage by eye.

Readers: 2 blind Sonnet calls, one per leaf. Each gets the 8 cells under neutral labels A-H (pis2/blind/cell_labels.tsv,
shuffled, seed 20261006) and that leaf's token crops under neutral ids (P01.. f.244r, Q01.. f.275r, shuffled). No key, no
copy, no transcription, no sign ids. Per token: the label of the best-matching cell for the sign at the crop's horizontal
centre, a second choice, confidence (low/medium/high), one-line shape description. Replies verbatim in pis2/blind/.

My eye classes (written before the replies, from the montage), as admissible cell sets:
- f.244r loop form (an x whose right arm closes in a loop, no crossing diagonal): L03 i5, i25, i35; L06 i15, i44; L07 i28,
  i45; L09 i20, i30 -> admissible {T45, T36} (my eye cannot choose between the two from these crops).
- f.244r L07 i33 (crossed double-f-like form) -> admissible {} (none of the eight).
- f.275r crossed X with a long diagonal and a small o/loop at lower right: L04 i7, L04 i39, L05 i0, L09 i3, L12 i5, L14 i28,
  L15 i9 -> admissible {T36}.
- f.275r bare x, no o: L03 i31, L07 i11, L10 i13, L15 i33; and L13 i11 (x-like with a dot) -> admissible {T31, T47}.
- f.275r L08 i0 (alpha / proportional-sign form) -> admissible {}.

Settlement rule per token: SETTLED-<cell> iff the reader's top choice is <cell>, its confidence is medium or high, and
<cell> is in my admissible set. A token with an empty admissible set is NOT-T31-SHAPE iff the reader's top choice is not
T31 at medium/high confidence; else UNSETTLED. Everything else UNSETTLED.

Effect (fixed now): settled labels are written to pis2/t31_tokens.tsv as transcription-label findings. In this job:
key86.tsv unchanged (T31 = m as published), committed transcriptions and readings unchanged, every T31 token stays M (a
relabel of tx86/tx86e and the kp86/kp86e re-score is a separate, named next step). A token settled T36 or T45 is a
transcription label slip (rule 4: the table cell is not contradicted); a token settled T31/T47 supports the table's m.
