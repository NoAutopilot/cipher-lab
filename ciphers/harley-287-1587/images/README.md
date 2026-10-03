# images/ (A2-HAR6, 3 Oct 2026)

- `decode/` (NOT committed, 6 full-size JPEGs, ~73 MB): DECODE R8491 (Harley 287 f.84r, f.84v) and R8494 (f.90r-91v) full-size
  images, fetched in one browser login with `tools/decode_browser_login.js 8491 ... --fetch-page RecordsView/8494 --guess-fullsize`.
  sha1s in `decode_sha1.txt` (identical to A2-HAR's and A2-HAR5's fetches). Re-fetch the same way; nothing else is needed.
- `f84r/`: 15 gloss+cipher pair bands (`tools/iiif_lines.py --image .../IMG_R8491_I39193_P1.jpg --region 1950,500,4700,4600
  --centres 189,369,528,647,804,921,1098,1218,1342,1460,1560,1700,1770,1940,2135,2242,2382,2521,2750,2887,3062,3202,3365,3490,
  3802,3936,4064,4164,4299,4410 --lines-per-crop 2 --max-width 2450 --overlap 120 --top-margin 40 --bottom-margin 110`).
- `f90r/`: 7 three-line bands (`--image .../IMG_R8494_I39202_P1.jpg --region 2000,650,4750,3000 --lines-per-crop 3
  --max-width 2450 --overlap 120 --top-margin 60 --bottom-margin 60`), auto-detected lines; bands overlap.
