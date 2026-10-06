# Harley 287 f.88r sign sorter (R11A-HAR, 6 Oct 2026)

Page: `harley287_f88r_sorter.html` (self-contained, 2.6 MB; publish with capabilities `{"db": {}}`, from the account-3
orchestrator per the RUN11 brief; this worker did not publish it). Preflight: `python3 tools/sorter_preflight.py
ciphers/harley-287-1587/sorter/f88r/harley287_f88r_sorter.html --cipher-lines ciphers/harley-287-1587/sorter/f88r/cipher_lines.tsv` -> PASS
(template ok; 12 focus tiles answerable, 29 named piles; 305 tiles, 0 off the cipher lines, shape 15 = 4.9% < 5%).
Contact sheet `harley287_f88r_sorter.preflight.png`, 24 random tiles eyed by the building session: 19 single cipher signs,
5 cut problems (3 merges of two signs, 1 wide merge `1##` on L14, 1 overline fragment on L13), all on cipher runs, none
clear text; "Fix the cut" handles them.

How it was built (disk only, no fetch):
1. `cipher_runs.tsv`: x-ranges of the cipher runs on each `images/f88r` line crop, set by eye from 0.6x montages with a
   100 px ruler. Clear English between runs is excluded. s1 ranges stop at x 2390 and s2 ranges start at x 60, so the
   120 px s1/s2 overlap is not tiled twice. L01, L11, L15-L20, L22-L23 hold no cipher run (L19's struck interlinear
   `+ΛT##` left out). L06_s1 650-1220 is included although pass A thought L06 might not be cipher.
2. Each run is cut to `pages/<crop>_r<n>.jpg` (28 runs).
3. `tools/glyph_atlas.py segment --median-h pool` (default component mode; `--cursive` was tried first and merged or
   fragmented most signs of this separated hand) -> 312 boxes; `glyph_atlas.py cluster --k 30 --pca-scale shared`.
4. Clean-up: 7 boxes dropped (3 specks, ink < 3%; 4 solid blots, ink > 60% -- one may be the filled dot sign on L08/L09,
   still visible in the line view); 9 strip-height boxes clipped to the central 120 px band.
5. Piles = the 30 shape clusters, named k00-k29. **They are not letters and not Bourdeau's sign names**: the person merges,
   splits and renames them. `--auto-clusters 3` adds provisional sub-clusters for "apply to all in this cluster".
6. `focus.tsv` (no header): the oddest tile (largest distance to its centroid) of each of the 12 largest piles, with the
   readers' look-alike pairs from `tx/f88r_lookalike/confusion_f88r.tsv` named in prose. `rank.tsv`: `--rank-confusion`
   triage order only.

Apply the person's choices with `tools/sign_sorter_apply.py` (see its --help); then the next machine passes read against the
settled labels (TRANSCRIPTION.md, CLAUDE.md Usage 6). Images: DECODE R8492 full-size, crops already committed in images/f88r.
