# f.23 sign sorter (R9-WVOSORT, account 4, 6 Oct 2026)

For the owner: settle the sign inventory of WVO 1109's cipher enclosure (Kassel, f.23, "ad 1564. Sept. 18.") before any
further machine pass or the crib-placement test (R8-WVO1111 "Next"; CLAUDE.md Usage 6: NX-WVO174's two passes split
290 vs 335 tokens).

- Page: `f23_sorter.html` (sign_sorter.py, template 2026-10-06.1), 258 tiles in 28 provisional shape piles `k01`-`k28`
  (k-means on HOG, seed 1564 -- shape groups, not readings), 24 "Check these first" tiles. Publish with capabilities
  `{"db": {}}`; the person's choices land in db collections piles / moves / newpiles; apply them with
  `tools/sign_sorter_apply.py`.
- Preflight (`python3 tools/sorter_preflight.py ciphers/wvo-hessen-1564/sorter/f23_sorter.html`): **PASS** (template ok;
  answerable 24 focus / 28 named piles / 0 unanswerable; 258 tiles all on the 10 cipher rows; 0 wide, 0 strip-height
  boxes, 7 = 2.7% ink outside 3-60%). Contact sheet `f23_sorter.preflight.png`: all 24 tiles eyed against their rows by
  the building worker -- 20 are one whole cipher sign; 4 are faults the page's own buttons handle (C06_01_003 a stray
  loop below the row, C09_01_031 half of a split final sign, C03_01_025 a descender fragment, C04_01_027 the gutter edge).
- Rows: only the ten cipher rows are tiled (`cipher_lines.tsv`; C10 only strip x 0-900, left of the signature). The
  ten rows of ordinary German handwriting written between them are not tiled.
- Focus box: the tiles whose two nearest pile centres are closest. **Not** "every pass split", as the brief asked:
  NX-WVO174's passes cut the leaf into 18 bands over what are 20 written rows (10 cipher + 10 clear, alternating), so
  most of its bands hold the lower half of one row and the upper half of the next and its tokens cannot be matched to
  a tile; this also accounts for much of its 290 vs 335 split.

Pipeline (re-run: `sh ciphers/wvo-hessen-1564/sorter/run_all.sh` from the repo root, then the sign_sorter.py command
below). Crop step: `python3 tools/iiif_lines.py --image ciphers/wvo-hessen-1564/images/01109_p3_400full.jpg --out
ciphers/wvo-hessen-1564/sorter/strips --region 550,130,2750,1800 --centres 80,170,250,315,400,470,570,645,735,810,920,
1005,1090,1180,1280,1365,1470,1550,1620,1710 --prefix f23 --debug` (centres placed by eye on the debug overlay; even
bands are the cipher rows). `make_strips.py` cuts full-width strips (band +-48 px; C09 +90 below, the row falls across
the leaf) to `pages/`; glyph_atlas segment (`--merge-vgap 0.15`) on them; `make_seg_in.py` fits each row's baseline
to those boxes and whitens everything outside baseline -95..+18 px (`seg_in/`, not kept); glyph_atlas segment again;
`build_inputs.py` drops slivers, the signature, and short boxes riding above the row (clear-row letters), clusters,
and writes signs/labels/marks/focus/dropped.tsv.
```
python3 tools/sign_sorter.py --signs $D/signs.tsv --labels $D/labels.tsv --pages $D/pages --marks $D/marks.tsv \
  --focus $D/focus.tsv --cipher-lines $D/cipher_lines.tsv --title "Orange 1564 Sign Sorter" --lede "..." \
  --out $D/f23_sorter.html          # D=ciphers/wvo-hessen-1564/sorter
```
Known cut faults left for the page's "Fix the cut": a few cipher signs still carry a touching letter of the clear row
above them (connected ink cannot be split by the zone mask), and a few final signs of C09 are split in two.
