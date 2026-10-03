# F36R-REREAD blind pass A, f.36r rows r36n_L09-L14 (3 Oct 2026)

You are one of two independent readers of cipher signs in a 16th-century Italian letter (BnF fr.3252 f.36r). For each
cipher sign, record which cell of the sign sheet it matches by SHAPE.

Read ONLY: the 24 crops listed below and the sheet `/home/user/cipher-lab/ciphers/ceppo-nevers-fr3251-1570s/harvest/sign_sheet_blind.png`
(cells labelled S10..S97). Do not open any other file (no NOTES, keys, maps, other passes, other crops); the pass is void
if you do. The sheet gives no values; match shapes only. Ignore the small clerk's letters written above the signs.

## Crops
Each crop is one segment of one manuscript row, upscaled 2x. Segments _s1.._s4 of a row run left to right and do NOT
overlap: continue the position count across them. A sign cut at a crop edge is counted once, in the crop holding most of
it. The crop may show the bottoms of the row above and tops of the row below at its edges: read only the main row, the
large signs across the middle of the crop. All six rows are cipher from end to end (no prose).

/home/user/cipher-lab/ciphers/birago-fr3252-1571-72/harvest/f36r/crops/r36n_L09_s1.png
/home/user/cipher-lab/ciphers/birago-fr3252-1571-72/harvest/f36r/crops/r36n_L09_s2.png
/home/user/cipher-lab/ciphers/birago-fr3252-1571-72/harvest/f36r/crops/r36n_L09_s3.png
/home/user/cipher-lab/ciphers/birago-fr3252-1571-72/harvest/f36r/crops/r36n_L09_s4.png
/home/user/cipher-lab/ciphers/birago-fr3252-1571-72/harvest/f36r/crops/r36n_L10_s1.png
/home/user/cipher-lab/ciphers/birago-fr3252-1571-72/harvest/f36r/crops/r36n_L10_s2.png
/home/user/cipher-lab/ciphers/birago-fr3252-1571-72/harvest/f36r/crops/r36n_L10_s3.png
/home/user/cipher-lab/ciphers/birago-fr3252-1571-72/harvest/f36r/crops/r36n_L10_s4.png
/home/user/cipher-lab/ciphers/birago-fr3252-1571-72/harvest/f36r/crops/r36n_L11_s1.png
/home/user/cipher-lab/ciphers/birago-fr3252-1571-72/harvest/f36r/crops/r36n_L11_s2.png
/home/user/cipher-lab/ciphers/birago-fr3252-1571-72/harvest/f36r/crops/r36n_L11_s3.png
/home/user/cipher-lab/ciphers/birago-fr3252-1571-72/harvest/f36r/crops/r36n_L11_s4.png
/home/user/cipher-lab/ciphers/birago-fr3252-1571-72/harvest/f36r/crops/r36n_L12_s1.png
/home/user/cipher-lab/ciphers/birago-fr3252-1571-72/harvest/f36r/crops/r36n_L12_s2.png
/home/user/cipher-lab/ciphers/birago-fr3252-1571-72/harvest/f36r/crops/r36n_L12_s3.png
/home/user/cipher-lab/ciphers/birago-fr3252-1571-72/harvest/f36r/crops/r36n_L12_s4.png
/home/user/cipher-lab/ciphers/birago-fr3252-1571-72/harvest/f36r/crops/r36n_L13_s1.png
/home/user/cipher-lab/ciphers/birago-fr3252-1571-72/harvest/f36r/crops/r36n_L13_s2.png
/home/user/cipher-lab/ciphers/birago-fr3252-1571-72/harvest/f36r/crops/r36n_L13_s3.png
/home/user/cipher-lab/ciphers/birago-fr3252-1571-72/harvest/f36r/crops/r36n_L13_s4.png
/home/user/cipher-lab/ciphers/birago-fr3252-1571-72/harvest/f36r/crops/r36n_L14_s1.png
/home/user/cipher-lab/ciphers/birago-fr3252-1571-72/harvest/f36r/crops/r36n_L14_s2.png
/home/user/cipher-lab/ciphers/birago-fr3252-1571-72/harvest/f36r/crops/r36n_L14_s3.png
/home/user/cipher-lab/ciphers/birago-fr3252-1571-72/harvest/f36r/crops/r36n_L14_s4.png

## What to record per cipher sign
- `sign_id`: best-matching sheet cell `S##`; `X_THETA2` for an oval crossed by TWO horizontal bars; `X_POUND` for a
  pound/lb-like loop with a crossing stroke; `X_NEW` for any other shape not on the sheet (describe it in note); `?` if
  illegible. Small marks are signs too: "=", "+", a slash between dots, "3", "2", a lone "o", a crossed stroke. Compare
  dots, ticks, one bar vs two, lean, carefully.
- `alt`: a second candidate cell if two fit, else blank. `conf`: H / M / L.

## Output
Write exactly one TSV at `/home/user/cipher-lab/ciphers/birago-fr3252-1571-72/harvest/f36r/passA.tsv` with header
    passage	pos	sign_id	alt	conf	note
`passage` = the row id from the crop name (r36n_L09 .. r36n_L14). `pos` = 1-based within the row. Write each row as you
finish it (append), so nothing is lost. Reply with only: rows written per passage. Work crop by crop; do not stop early.
