# PREREG-VIVPACKET3 (14 Oct 2026, 03:3x UTC by date -u; account-4 worker VIV-PACKET3 for LANE VIV-KEYSTONE)

Written and pushed BEFORE the page is built and before any answer exists. Brief: `.claude/briefs/runs/2026-10-13-acct4-keystone-viv-jobs.md`
"Wave 6", "VIV-PACKET3". Owner rules R12-R14 (`tools/data/sorter_owner_requirements.tsv`). Nothing here edits key.tsv,
reading_piece63.tsv, status.json or any committed reading; f.191r has no truth, so nothing on this page is scored against a truth.

## 1. Question tiles (f.191r, ink 63)
Source: `tx/viv63_f191/rec.tsv` + `decode.tsv` as committed at VIV-F191B (68b4d5693 lineage; `f191.py --check` up to date at build).
1. Eligible lines: L08-L16 and L29-L32.
2. A token is a candidate iff its decode grade is M or U, OR its passes split. "Split" = the vote cells of passes A, B, C (and D only
   on L01-L21, since pass D drifted from L22, NOTES "VIV-F191B") are not all the same sign ('-' counts as a different value). A merged
   `oo` token (two columns) is never a question (no single pen unit).
3. Priority: tier 1 = candidates inside the five "after" V_strict stretches (recomputed with f191.py's own `page_letters` and
   `viv53L_stretches.top(s, V, 5)`, the same call `--stats` makes), in stretch rank order then position; tier 2 = the other candidates
   in line order then position.
4. A candidate becomes a tile only if it maps to exactly one pen-unit box at op 1:1 (below, section 2). Untileable candidates are
   counted and listed (`tx/sorter_f191/questions.tsv`, column `tile` empty, reason given), never guessed.
5. Take tileable candidates in priority order up to **40**. Shuffle the 40 with `random.Random(20261014)`; they start in the
   "Taken out" tray (`--focus-to-tray`), all in the neutral pile `unsorted` (family "to place"), never in a pile named by their own
   committed label (R13: f.191r's committed labels are never pile names or pile members).

## 2. Tile boxes on f.191r
Crops: the VIV-F191 command verbatim (images/p63/manifest_vivf191.json; openapi.bnf.fr 1 request), untracked. Pen units: `tools/glyph_atlas.py
segment` on the eligible lines' crops, as `tx/vivcls/seg.py` does (default mode, `--median-h pool`, s1/s2 overlap deduped at its midpoint).
Token map: pass C's tokens for that line (pass C read exactly these crops) against the boxes with `tools/box_token_align.build_map`
(no labels, defaults). A rec.tsv position is linked to pass C's token through the column table `f191.cols` (the k-th non-'-' C cell is C's
k-th token). Tile = the one box the map places at op 1:1 on that C token. Positions where C has '-' are untileable.
Before publishing, every question tile is eyed on the contact sheet; a box that does not hold exactly one whole sign is dropped and named in
an Addendum (as VIV-HUMAN Addendum A), and the next tileable candidate in priority order replaces it, until 40 or the list is spent.

## 3. Piles: one per key sign, truth-consistent tiles only
Leaves with a pen-unit map on disk: f.102r (`benchmark-tx/vivonne1573-f102r-dev2.truth.tsv`, `tx/vivcls/train/map_r2_f102r.tsv`), f.103r
(`...-f103r-confirm2.truth.tsv`, `map_r2_f103r.tsv`), f.201r (`...-f201r-dev.truth.tsv`, `tx/vivcls/real/map_r2_f201r.tsv` via passA's
alignment, as tx/vivhuman/build_inputs.py). **Deviation, stated now:** f.201v and f.211r (named by the brief) have truth files but no pen-unit
map and no crops on disk, and the host budget (2 requests: f.191r and f.201r) cannot fetch them; they contribute no tiles in this job.
A tile is a member of pile X iff: it is the only op-1:1 tile on its truth position; the truth row has status `scored` and an EMPTY flag; its
committed label `ref_sign` = X lies in the row's truth set; X is a code of key.tsv; and the row's `plain` equals key.tsv's meaning for X.
The eight VIV-HUMAN2 question tiles are allowed (their truth is certain; they are not questions here). Cap 12 per pile, sampled with
`random.Random(20261014)` from qualifying tiles in (leaf, line, position) order. A key code with no qualifying tile gets no pile and is listed
in the build Addendum; a pile under 3 members is shown and named. No other piles (no f.191r tiles, no non-key labels).
Pile purity (brief): the build Addendum lists, per pile, the truth letters (`plain`) of its members -- one letter per pile by construction --
and a contact sheet of every pile is made and eyed. R14 caveat registered now: a key code may cover more than one glyph shape on this hand
(VIV-KEYV for e, VIV-HUMAN2 for z/s); a pile is one sign in the key's sense (one code, one letter), not guaranteed one shape.

## 4. The page
`tools/sign_sorter.py` only, blind (no values, no decode choices, no reader weights). Title "Vivonne f.191r: the signs that break the best
lines". Lede: each tile in the tray is one sign; put it in the pile whose signs look the same, or "None of these: new sign" if none does; do not
use "fix the cut" on this page (R12). `--cipher-lines` listing every page image. `tools/sorter_preflight.py` and `tools/cvd_check.py` pasted.
Committed under `tx/sorter_f191/` (HTML under 3 MB; no page image), published with the Artifact tool.

## 5. Consuming test (registered now; the parent runs it when the owner answers)
1. Export the page's db (ArtifactData), apply with `tools/sign_sorter_apply.py --labels tx/sorter_f191/labels.tsv --db DIR --out
   DIR/settled.tsv --page tx/sorter_f191/<page>.html`.
2. For each question tile: placed in pile X -> the rec.tsv position's sign becomes X, flag cleared (owner-settled; graded H if key.tsv's
   row for X is H, else M); "new sign" -> U (sign set to a code outside the key); unanswered or left in `unsorted` -> unchanged.
3. Re-decode f.191r with f191.py's own decode/statistics (an override option on f191.py, the committed rec.tsv untouched) -> longest all-H
   run, V_strict top-1/top-3 with the 200-shuffle null, b2 and 200 wrong keys, controls C1/C2 first, seed `20261014VIVF191`: before
   (VIV-F191B, 37 / 21) and after, side by side.
4. Decision: a stretch of >= 42 letters with no liberty (all H, no M/U inside) goes to a verifier (rule 7 re-derivation); otherwise the
   numbers are logged and f.191r stays D1 material. The owner's placements are not a truth: no accuracy figure is computed from this page.
