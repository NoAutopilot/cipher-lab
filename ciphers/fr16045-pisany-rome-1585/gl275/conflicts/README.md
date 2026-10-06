# gl275 conflict crop compares (R9-PIS, 6 Oct 2026)
Page crops p_c1..p_c4_L01.jpg: one gloss token each, cut from images/f275vGL_L01_s1.jpg (c1-c3) and _s4.jpg (c4) with PIL
(boxes in NOTES.md "R9-PIS"; tools/iiif_lines.py --region on a single-token region found no line or cut off the sign).
Key-cell crops k_T*_L01.jpg: tools/iiif_lines.py --image sources/cryptiana/web/henryiii_Vivonne5.png --region (cell_xy -16,-13, 32x26)
--lines-per-crop 1 --distance 400 --prominence 1; k_T56 by PIL (the tool found 0 lines in that cell).
blind/: the same crops renamed P1-P4 / K01-K16 (map: klabels.tsv, kept outside blind/). One blind Sonnet read per page crop against all 16
cells, replies verbatim in reader_P*.txt. Outcome per conflict: conflicts.tsv.
