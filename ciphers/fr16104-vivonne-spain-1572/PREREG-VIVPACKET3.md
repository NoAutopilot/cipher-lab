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

## Addendum A (14 Oct 2026, 03:4x UTC by date -u; box check before publishing; the page is NOT published and no answer exists)
Build (`python3 tx/vivhuman/build_inputs.py --packet3`): 150 candidates on L08-L16/L29-L32; 75 tileable under section 2 (63 with no single 1:1
box on pass C's token, 12 where pass C has no token); 40 taken (tier 1: 3, tier 3: 1, tier 5: 2, the rest by line from L08; the cap is reached on
L14, so L15-L16 and L29-L32 bar Q10 get no question). Piles: 24 of 32 key codes, each one truth letter (tx/sorter_f191/piles.tsv); no qualifying
tile for S, A, y, oo, b, Zu, V, e (V and e have no row in the truth files' sets; y, S were never truth-consistent at a scored unflagged row).
Page built by tools/sign_sorter.py (246 tiles, 25 piles, 1.9 MB; preflight checks run by the build: PASS).
**Section 2's eye check fails the map:** of the 40 boxes, 15 do not hold one whole sign (a dot, a stroke fragment, empty paper or two signs)
and 15 hold one whole sign that no pass wrote at that position (the pass-C-to-box map is offset: e.g. Q01 votes x/x/x/2, box on an m; Q02 votes
S/S/s/s, box on oo); 6 undetermined by eye; 4 plausible (Q05, Q10, Q32, Q34). Per tile: tx/sorter_f191/box_check.tsv. Replacing from the
remaining 35 tileable candidates (same map, same error rate expected) would give a handful of tiles, not a packet. Rule 2's replacement
clause cannot rescue a map that is wrong three times in four, so **the page is not published**: tiles on the wrong sign would feed the wrong
position into section 5's re-vote, and R14 says a badly cut tile is the page's fault. Nothing here changes sections 1, 3 or 5; a rebuild
needs a different box instrument (parent's decision, written as Addendum B before any rebuild).

## Addendum B (14 Oct 2026, 04:0x UTC by date -u; account-4 worker VIV-PACKET3B; written and pushed before any box is touched; no answer exists)
Parent's decision (brief "VIV-PACKET3B"): option (b), hand-cut boxes per question, plus an f pile. Sections 1, 3 (except as below) and 5 stand.
1. **Questions.** The same 40 question tiles (tx/sorter_f191/questions.tsv `taken` = 1, same qids, same tray order). For each, the worker sets the
   box by eye on the f.191r line crop (the VIV-F191 crops, regenerated by its command, 1 request) so that it holds exactly the one sign the
   vote names at that rec.tsv position (line, pos; the position is found by reading the line's committed vote sequence against the crop, left to
   right, never by the old pen-unit map). One look per line crop, several boxes per look. Every box is logged in
   `tx/sorter_f191/boxes_handcut.tsv` with the old (map) box beside the new one and a verdict per tile: `whole` (one whole sign, the voted
   position), `unsure` (a sign is boxed but the position count is uncertain), `none` (no box can be set: e.g. the sign is lost in a blot).
2. **Box check (gate, registered now):** re-run on the new boxes, by eye on a contact sheet of the 40 tiles: a tile passes iff it holds exactly one
   whole sign at the voted position. **Gate: >= 36 of 40 pass**; tiles that fail are dropped from the page (not replaced: the remaining tileable
   candidates sat on the same offset map) and named here after the check. Under 36: the page is not published, as in Addendum A.
3. **Pile f (new).** Members: the rows of `tx/viv63_fkey/f_tiles.tsv` whose reader label is `g` (VIV-FKEY: the f-sign is the g-like glyph under
   label g) on the leaves with crops on disk (f.102r, f.103r, f.201r; f.201v and f.211r have no crops and the host budget is spent on f.191r and
   f.201r). Box: the label-aware VIV-CLS map tile at that position if one exists at op 1:1, else hand-cut by eye; each is eyed and kept only if it
   holds one whole g-like sign. Cap 12 (all of them if fewer). Pile name `f`, one truth letter (f). The p-at-f (affaire double f), o and y rows are
   not used (other shapes; VIV-FKEY "SPLIT" per label).
4. **Pile g** stays truth-r only (section 3's rule already requires plain = key meaning r); the build asserts it.
5. **Consuming test, one addition (brief):** an owner placement of a question tile into pile `f` keys that position's token as f, grade S
   (owner-read), in section 5's re-vote. Nothing else in section 5 changes. Nothing on this page is scored by this worker.
6. Lede and page as section 4 (blind, R12 sentence, no fix-the-cut); preflight + cvd_check pasted; committed under tx/sorter_f191/ (HTML < 3 MB).

### Addendum B result (14 Oct 2026, 04:1x UTC by date -u; VIV-PACKET3B; no answer exists, nothing scored)
Crops regenerated (openapi.bnf.fr 2 requests; f.191r boxes identical to manifest_vivf191.json 72/72); `build_inputs.py --packet3` reproduced VIV-PACKET3's
inputs exactly before any change. Boxes hand-cut on the line crops (positions counted against f191.py's committed vote sequence), then every box checked
at 2.5x zoom with a pixel ruler and corrected where off (14 corrected in a second pass); log with old and new boxes and the verdict per tile:
`tx/sorter_f191/boxes_handcut.tsv` (columns check, check_note).
**Box check: 34 of 40 hold one whole sign at the voted position (gate >= 36): FAIL.** Before (Addendum A, map boxes): 4 plausible of 40. The six that cannot
be boxed as one whole sign: Q12, Q13, Q25 (label V, the long diagonal stroke, fused into or crossing its neighbour; Q12 also holds verso bleed-through),
Q18 (sign under an ink blot), Q24 (the L loop overlaps the Z-like 3 before it), Q26 (the small e is two ticks; the tile holds one). None is a cut fault a
better box fixes: they are shapes that do not separate on this page. Per item 2 the page is **not published**; the committed tx/sorter_f191 inputs stay
VIV-PACKET3's; `--packet3b` regenerates the 3b inputs (the six dropped by the check column).
Pile F (item 3): 6 of the 11 label-g truth-f positions on the three leaves have one op-1:1 map tile (f.102r L04, L15, L26; f.103r L22, L35; f.201r L18);
the other 5 were not hand-cut (the page was not built). Eyed: f.102r L04, L26 and f.103r L35 hold one whole sign, a looped-top stem with a lower loop,
visibly unlike the truth-r g tiles (g with a descender); f.102r L15 holds two signs, f.103r L22 and f.201r L18 only the top. Pile named `F`, not `f`:
key.tsv code f already means l. Pile g truth-r only (asserted); one g member (f.102r L23) looks d-like. Report-only, not a test.

## Addendum C (14 Oct 2026, 04:3x UTC by date -u; parent's decision, session_01D7XWmthshMVqxumdDvitPh, 04:2x UTC; written and pushed before the page is built; no answer exists)
1. The page is published with the **34 question tiles whose hand-cut box passed** the Addendum B check (tx/sorter_f191/boxes_handcut.tsv `check` = pass),
   same qids, same tray order minus the dropped six. Addendum B item 2's gate (>= 36) is superseded for this page by the parent: its purpose, that no
   badly cut box reaches the owner, is met by dropping the failures.
2. Dropped by name: **Q12, Q13, Q25** (label V, the long diagonal stroke, fused into or crossing a neighbour), **Q18** (under an ink blot), **Q24** (the
   L loop overlaps the Z-like 3), **Q26** (the two-tick e; a tile holds one tick). These six are not readable as single tiles on this page; their
   positions stay as committed (M/U or split) and the re-vote leaves them unchanged.
3. Pile **F** (plaintext f; key code f means l): only the members that held one whole sign in Addendum B's eye check -- f.102r L04
   (f102r_L04_s1_01_007), f.102r L26 (f102r_L26_s2_01_011), f.103r L35 (f103r_L35_s2_01_013); the other three map tiles (f.102r L15 two signs, f.103r
   L22 and f.201r L18 top only) are listed in tx/sorter_f191/f_drop.tsv and left out. The five label-g truth-f positions with no single map tile are not
   added. Pile F is a three-tile pile and is named as such in the build line. Pile g stays truth-r only. All other piles as registered (section 3),
   f.201r members included (host budget raised by the parent to 4 requests so the f.201r crops can be re-fetched).
4. Section 5's consuming test stands on the 34, with Addendum B item 5 (a placement in F keys the position as f, grade S, owner-read).
5. Page as section 4: blind, title "Vivonne f.191r: the signs that break the best lines", R12 sentence in the lede, preflight + cvd_check pasted,
   committed under tx/sorter_f191/ (HTML < 3 MB), published with the Artifact tool.

## Addendum D (15 Oct 2026 00:5x UTC, account-4 parent, written before any placement was read): tie-break given to the owner mid-test

While sorting Q01 (f191r_L13_s2_01_020) the owner asked which pile to use when the look-alike shape appears in several piles. Checked against the page's own DATA (every pile's tiles rendered to one sheet, scratchpad q01/all_piles.png): the z-with-stroke shape is 3 of 9 tiles in pile z, 1 of 12 in pile 3 (its last tile) and 1 of 12 in pile x (its seventh) -- the readers' merged labels leaking into the truth-consistent exemplars (R13/R15). The rule given to the owner, in these words: pick the pile where your shape is the biggest share of the pile; if it is a lone stray everywhere and no pile is built around it, choose "None of these: new sign"; ignore the single oddballs inside a pile. Consequence for scoring (s.5): the owner's label still replaces the plurality at that position as registered; a "new sign" answer still leaves U. The post-hoc tag on the result records that this tie-break was supplied during the test, not before it, and the three piles named here (z, 3, x) are listed in the result so a verifier can see which positions it could have touched. No pile, label or tile was changed.
