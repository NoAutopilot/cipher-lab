# PREREG_seg -- RUN1-SEG acceptance of `tools/glyph_atlas.py segment --cursive` on the real hand

Written and committed 4 Oct 2026 (RUN1-SEG, account 1 worker for LANE-RUN1) BEFORE the mode is run on R9528 f.194.

Instrument: `tools/glyph_atlas.py segment --cursive` with its defaults as committed in this same commit
(--rel 0.78 --ghost 0.55 --dark-q 0.1 --ghost-px 0.75 --core 0.5 --band 1.0 --min-side 0.25 --gap 0.7 --split-w 4.0
--piece 2.8), one --page per line crop.

Crops: R9528 f.194 (DECODE IMG_R9528_I44887_P2.jpg, sha1 9710dd1e...), cut with JM-ALPHA's own command
`tools/iiif_lines.py --image IMG_R9528_I44887_P2.jpg --region 1860,200,1620,2200 --prefix f194 --follow-slope 300
--slope-margin 22` (31 crops; rows 9, 11, 23, 26 are JM-ALPHA's duplicates, dropped as in scripts/test1.py DUP).

Development, disclosed: the defaults were set on R9529 f.199 only (the other page with two passes), where the
committed defaults give 12 of 26 lines within 25% overall and 11 of 15 cipher-only lines (f.199 carries ~12 clear-
Spanish lines that readers tokenised as words), median box height 2.43 x xh. On f.194 nothing was segmented before this
commit; only one half of crop L02 was looked at by eye (to see the hand).

Reference per line: the mean of pass A's and pass B's token counts (passes/f194_A.tsv, f194_B.tsv; whitespace tokens,
clear words in brackets counted as words, '?'-tokens counted). Lines with reference 0 are skipped. Also reported: the
subset of lines where A and B give the same count.

Gate (both must hold):
1. per-line box count within +-25% of the reference on >= 70% of f.194's lines;
2. median box height >= 0.6 x the page x-height estimate (the median of the per-strip x-heights the tool writes to
   pages.json). Limitation stated in advance: the x-height comes from the same tool's core-band profile, so (2) checks
   that boxes are sign-sized rather than stroke fragments (the 4 px failure), not an independent x-height.

Report the numbers whether it passes or fails. If it fails: one tuning round (named parameters only, numbers reported),
then stop and log; a third configuration is closed by rule 3's third-attempt clause.

Script: `python3 ciphers/rah-juan-manuel-1521/sorter/seg_accept.py --page f194 --crops <crops> --out <dir>`.
