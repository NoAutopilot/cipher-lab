## ATF55V: atlas re-pass on f55v (25 Sept 2026, LANE R7)

Worker R7-AT55V (Sonnet), 20:03-20:2x UTC. Brief `.claude/briefs/runs/2026-09-25-lane-r7-atf55v-salviati-atlas.md`.
Job: eyeball every code+mark type on f55v beside the atlas/each other to find near-duplicate types the transcription
split apart (LANE R6 CM/CM2's lever for the noise-tolerance gate), decide merges by eye only, and add `--merge` to
`control/codemark_curve.py`. f55v is one of the two lowest pass-agreement leaves (77.5%, NOTES.md).

**1. Setup.** `glyphs/crops` was missing; rebuilt with `build.sh`'s segment line (`python3 ../../tools/glyph_atlas.py
segment $(cat glyphs/segment_args.txt) --out glyphs --mark-h 0.8 --debug`). That run reproduced the sign/mark counts
per page (f55v: 499 signs, 153 marks) but did **not** reproduce `glyphs/signs.tsv`/`marks.tsv`/`bitmaps.npz` byte for
byte against the committed copies (some box heights differ, e.g. f54r_08_018 118px vs 40px this run) -- almost
certainly a library-version difference from whatever environment made the committed files, not a bug in this pass.
Since `clusters.tsv`/`labels.json` (and therefore `atlas.tsv`/`atlas.png`/all the per-page `_boxes.tsv` files) are
keyed to the *committed* signs.tsv/marks.tsv/bitmaps.npz, the three regenerated files were reverted
(`git checkout --`) before doing anything else, and the run's only kept output is `glyphs/crops/*.png` (the grey,
normalised full pages segment writes before any connected-component step -- deterministic regardless of the
component-detection difference, and not itself committed per `glyphs/.gitignore`). All crops below are cut from
`glyphs/crops/f55v.png` against the committed `signs.tsv`/`marks.tsv` box coordinates, never the regenerated ones.
**Flag for the next worker that runs `build.sh`'s segment step on this machine: check `git diff glyphs/signs.tsv
glyphs/marks.tsv glyphs/bitmaps.npz` before running `cluster`, and revert if it differs, or clusters.tsv/labels.json
will silently stop matching the boxes they were built from.**

**2. Types on f55v.** `python3 control/codemark_curve.py stats --leaves all`: f55v has 334 sign tokens, 36 base
codes, **93 code+mark types** (of the pooled 223), 35.3% marked, 165 plain boxes -- matches NOTES.md's LANE R6 CM
table exactly.

**3. Crop tool note.** `glyph_atlas.py crop --sid` cuts only the sign's own box + a 6px margin, which does **not**
include an attached mark (marks are separate components, further away than 6px). A mark comparison needs the sign's
box unioned with its mark component(s)' boxes from `glyphs/marks.tsv` (the sign's `marks` column lists mark ids by
`|`); this worker's crop montages (`glyphs/f55v_atlas_pass/cmpM_*.png`) do that union before cropping, the plain
`cmp_*.png` ones (base-code-only pairs, no marks involved) use the tool's own `--sid` crop directly.

**4. Candidates tested** (all pairs with >=3 occurrences on f55v on each side, drawn from two sources: CM2's own
pass-disagreement base-code confusions -- `#`/`+`, `g`/`y`, `bh`/`g`, `#`/`Z`, `bh`/`phi` -- and every code on f55v
carrying 2+ low-count mark variants that could be the same mark mis-spelled): see `merges_f55v.tsv` for the full
table (16 pairs checked, evidence file per row, 2 below the 3-occurrence threshold left unscored).

**5. Result: one merge found, all 16 scored candidate pairs stayed distinct.**

- **Merge:** `H^o|1` -> `H^1|o` (n=1 vs 4 on f55v). Not a mark confusion at all -- both type strings name the same
  two marks ("1" and a ring "o"), just in reverse pipe order; all five f55v occurrences show the identical "1 over
  o" ink in the same left-to-right order (`glyphs/f55v_atlas_pass/cmp_H_order.png`). A pooled-level string check
  (not crop-verified beyond this leaf) finds six more such reversed-order duplicate pairs across all eight leaves
  (`]`+dot/o, eps+1/dot, H+1/5, e+#/dot, v+#/1, v+1/5 -- 15 more tokens total); flagged for a future worker to
  crop-verify and fold in, since a codebook-wide mark-order canonicalisation could be worth several more merged
  types beyond what this leaf alone shows.
- **Kept distinct, all 15 other scored pairs** (`#`/`+`, `g`/`y`, `bh`/`g`, `#`/`Z`, `bh`/`phi`, `S7`/`S7#`,
  `S7`/`S7~`, `e`/`e#`, `g`/`g1`, `g`/`g5`, `g`/`gdot`, `lam`/`lam#`, `lam`/`lam5`, `e`/`edot`, `eps1`/`eps5`) --
  11 "sure", 4 "likely" (a minority of samples ambiguous but the majority shows a real separate mark). Two pairs
  left unscored below the 3-occurrence threshold (`S7`/`S7^1` n=2; `]^o`/`]^ot` n=1, leaning distinct).
- **One pair reversed a first impression: `e^` vs `e^#`.** At the 1600px reference both groups look identical --
  the base "e" glyph's own natural top stroke (a small crossbar, part of the letter, not a mark) is easy to mistake
  for the "#" mark at that resolution. Five native-resolution Gallica IIIF fetches (ark btv1b90600674, canvas f57,
  8150x5560 native; scale factor 4075/1600 = 2.546875 from the ref1600 crop, since it's the canvas's left half)
  resolved a real, separate small `#` mark floating above that crossbar with a visible gap in both `e^#` samples
  checked, absent from the `e^` sample -- kept distinct. This is exactly the "1600px too coarse" case the brief
  named; worth the native check before merging on a blurry reference. Same native pass also confirmed `g^` vs
  `g^1`/`g^5` (clean numerals visible at native res that were an ambiguous blob at 1600px) -- also kept distinct.
- **Transcription-accuracy finding, not a merge:** `f55v_03_006` is recorded as `g^` (marks empty), but the native
  crop (`images/native_g_check/g_bare_03_006.jpg`) clearly shows an unrecorded "3" mark touching the sign (fused
  into one connected component with it, hence no separate mark id in `glyphs/marks.tsv`). This is a missed mark on
  one specific token, not a type-label problem -- flagged here rather than corrected, since fixing it means editing
  `ciphertext_f55v.tsv`'s settled reading for that one box, outside this worker's brief (no reading/key edits).

A follow-up native check on `e^` vs `e^dot` (3 tight native crops, same line 7, `images/native_e_check/cmp_e_dot_native.png`)
was inconclusive rather than confirming: at this crop width the neighbouring sign's own mark bleeds into frame on
the right edge of every sample, bare included, so it could not settle whether the bare sample's faint upper-right
dot belongs to `e^` or to the next token. Left at "likely", not upgraded to "sure".

**6. Re-score with the merge applied** (`python3 control/codemark_curve.py stats --leaves all --merge
merges_f55v.tsv`):

| leaf | types before | types after |
|---|---|---|
| f54r | 94 | 93 |
| f54v | 93 | 92 |
| f55r | 85 | 85 |
| f55v | 93 | 92 |
| f56r | 86 | 86 |
| f56v | 96 | 95 |
| f57r | 95 | 94 |
| f57v | 74 | 74 |
| **pooled** | **223** | **222** |

**Gate (pooled types drop by a fifth or more, 223 -> <=178): not met.** One confirmed merge is a 0.4% reduction.
The tested candidates -- the ones CM2's own pass-disagreements and this leaf's low-count mark variants pointed to
-- turn out to be real distinctions at sufficient resolution, not transcription noise; the type count on f55v is
apparently not inflated by near-duplicate mark spellings the way the brief's premise expected. The one lever this
pass did find (mark-string order canonicalisation) is pooled-wide, not f55v-specific, and unverified beyond H on
this leaf; even taken at face value (7 groups, ~4 more types than this leaf's own 1) it does not reach the gate
either. Not run/decided here: whether to spend a further worker crop-verifying the other 6 order-swap groups, or
whether the gate itself should be revisited given how solid the "distinct" verdicts turned out to be under a
proper (native-resolution) check.

**Requests:** gallica.bnf.fr 13 (1 `info.json` + 12 region fetches, one retry after a `Recv failure: Connection reset
by peer`, all >=2s apart, browser User-Agent). No subagents.

**Regenerate:** `python3 control/codemark_curve.py stats --leaves all [--merge ../merges_f55v.tsv]` from `control/`;
the montages in `glyphs/f55v_atlas_pass/` are reproducible from `glyphs/f55v_atlas_pass/type_sids.json` +
`mark_boxes.json` (kept) via `tools/glyph_atlas.py crop` (raw per-sid crops themselves not committed, regenerable
and not needed beyond the saved montages).
