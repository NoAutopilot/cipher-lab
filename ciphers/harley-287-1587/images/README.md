# images/ (A2-HAR6, 3 Oct 2026)

- `decode/` (NOT committed, 6 full-size JPEGs, ~73 MB): DECODE R8491 (Harley 287 f.84r, f.84v) and R8494 (f.90r-91v) full-size
  images, fetched in one browser login with `tools/decode_browser_login.js 8491 ... --fetch-page RecordsView/8494 --guess-fullsize`.
  sha1s in `decode_sha1.txt` (identical to A2-HAR's and A2-HAR5's fetches). Re-fetch the same way; nothing else is needed.
- `f84r/`: 15 gloss+cipher pair bands (`tools/iiif_lines.py --image .../IMG_R8491_I39193_P1.jpg --region 1950,500,4700,4600
  --centres 189,369,528,647,804,921,1098,1218,1342,1460,1560,1700,1770,1940,2135,2242,2382,2521,2750,2887,3062,3202,3365,3490,
  3802,3936,4064,4164,4299,4410 --lines-per-crop 2 --max-width 2450 --overlap 120 --top-margin 40 --bottom-margin 110`).
- `f90r/`: 7 three-line bands (`--image .../IMG_R8494_I39202_P1.jpg --region 2000,650,4750,3000 --lines-per-crop 3
  --max-width 2450 --overlap 120 --top-margin 60 --bottom-margin 60`), auto-detected lines; bands overlap.

## A4-RFHAR, 5 Oct 2026
- One browser login: `tools/decode_browser_login.js 8492 <scratchpad> --fetch-page RecordsView/8482,...,8487,8496
  --guess-fullsize --max-files 45`. All 12 full-size images were served (none is DECODE's forbidden.png): R8492 f.88r/v
  (P1, P2), R8482-R8487 ff.70r-72v (one image each), R8496 ff.96-97 (P1-P4). sha1s and sizes in `decode_sha1.txt`;
  ~158 MB, NOT committed (re-fetch the same way). Only f.88r was cut and read.
- `f88r/`: 23 lines x 2 segments (`tools/iiif_lines.py --image .../IMG_R8492_I39196_P1.jpg --region 2050,600,4500,3800
  --centres 258,441,582,734,869,1009,1180,1322,1439,1558,1692,1834,1958,2147,2289,2470,2633,2812,2993,3179,3293,3470,3662
  --lines-per-crop 1 --max-width 2450 --overlap 120 --follow-slope 400 --slope-local --prefix f88r --debug`); centres
  from a left-strip ink profile (two spurious auto peaks dropped), checked by eye.
