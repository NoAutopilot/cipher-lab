# f117_txer crops (TXE-R, 9 Oct 2026)
Cut from the committed native region (../f117/src_ark_..._f118_4380_1400_3150_1300.jpg) by tools/iiif_lines.py, three runs:
1. L01-L09: `--centres 103,223,347,462,580,702,815,944,1062,1210 --max-width 1100 --overlap 60 --band-extent 0.1 --mask-neighbours --overlap-note --note-scale 2 --follow-slope 300 --only-lines 1,...,9 --check-boxes ../../../nevers-birago-fr3251-1572/atlas/signs.tsv --check-page f117r --debug`
   (every line falls to the right, +33 to +125 px over the region, pitch 120; the flat-band overlay showed L07-L09 leaving their bands).
2. L10 flat (its slope fit came out -0.022, the tracker had jumped onto L09's tail): `--region 0,0,1170,1300 --max-width 1240 --only-lines 10`, one crop
   `f117r_L10.jpg` (L10 is a short line, ends near x=1150; wider cuts admitted L09's sloped tail and one L09 sign).
manifest.json: one entry per crop (stale entries from superseded cuts removed). lines2x/ = 2x LANCZOS reader copies, gitignored, regenerable.
band_check.tsv: the atlas has 9 lines on f117r against our 10 bands, so its per-line cut/admit figures for L09/L10 are a line-assignment mismatch, not a cut.
