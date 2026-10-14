# PREREG-VIVHUMAN -- can a person's eye read this hand where the blind readers fail? (f.201r, ink 67)

Written 14 Oct 2026, 01:1x UTC by date -u, by the VIV-HUMAN worker (account 4, LANE VIV-KEYSTONE), brief
`.claude/briefs/runs/2026-10-13-acct4-keystone-viv-jobs.md` "Wave 3" / "VIV-HUMAN". Pushed BEFORE the sorter page is built and
before any answer exists. Nothing is scored by this job; the parent scores when the owner's answers are saved.

## Material
- Leaf: BnF fr.16105 f.201r (ink 67, Saint-Gouard to Charles IX, 20 Oct 1573), BENCHMARK-TX item `vivonne1573-f201r-dev`.
  Truth: `benchmark-tx/vivonne1573-f201r-dev.truth.tsv` (clerk's own decipherment, ink 68, forced through the published key).
- Passes: `benchmark-tx/outputs/vivonne1573-f201r-dev/{passA,passB}.tsv`; committed reconciliation `tx/f201r_rec.tsv`
  (= the item's `committed.tsv`, the `ref_sign` column of the truth).
- Only truth rows with status `scored` and an EMPTY flag column are used (454 rows: the two clerk reads agree, no align-conflict).

## Sets (computed by `tx/vivhuman/sets.py`, written to `tx/vivhuman/questions.tsv`; `--check` regenerates)
- Each pass is aligned to the truth rows with `tools/tx_bench.align` (the benchmark scorer's own alignment).
- A position can be a question only if it has ONE pen-unit tile: passA's aligned token is mapped `1:1` to exactly one tile in VIV-CLS's
  committed round-2 map `tx/vivcls/real/map_r2_f201r.tsv`. 217 of the 454 unflagged rows qualify.
- **W** = qualifying rows where passA or passB (or both) is wrong against the truth set: **13** (all taken).
- **R** = qualifying rows where both are right: 204; **12** sampled with `random.Random(20261014)`.
- The 25 question tiles are shuffled with the same generator and named Q01-Q25. (The brief planned 30 + 12 = 42; W has only 13
  qualifying rows, so "all of W if fewer" applies and the page carries 25.)

## The page (built after this file is pushed; tools/sign_sorter.py only, blind)
- Piles: every other qualifying f.201r tile (op 1:1 in the same map, one tile per passA token, any status), labelled with the
  committed reconciliation's sign label at its aligned truth row (`ref_sign`). No key value, no decode choice, no reader weight.
- The 25 question tiles do NOT sit in their committed pile: they all start in one neutral pile, `unsorted` (family "to place"),
  and in the "Taken out" tray (`--focus-to-tray`). Reason: on unflagged rows the committed label equals the truth by
  construction (committed flagged-excluded error 0.000, circular), so starting a question tile in its committed pile -- with the
  page's "it was right" one-tap keep on its own pile card -- would hand the answer over. The lede says: put each tile in the pile
  whose signs look the same, or "None of these: new sign".

## Scoring rule (fixed now)
Input: the page's saved db exported with the ArtifactData tool to a folder, then
`python3 tools/sign_sorter_apply.py --labels tx/sorter_human/labels.tsv --db <dir> --out <dir>/settled.tsv --page tx/sorter_human/sorter_viv_human.html`,
then `python3 ciphers/fr16104-vivonne-spain-1572/tx/vivhuman/score.py <dir>/settled.tsv`.
Per question tile, its final label (`new_sign`, merges followed by sign_sorter_apply):
- **correct** iff the label is in the truth set of that row (the truth set = every sign label the published key maps to the clerk's
  letter at that position, C rows; i.e. "pile label -> key value equals the truth value").
- a label that is no pile of the page as built (a page-made new pile, `unsorted-b` etc.) is **"new sign"**: wrong, unless the truth
  row is off-key (empty truth set), then correct.
- still in `unsorted` (no answer), `not-letter`, `aside`, `bad-cut`, `taken-out`: wrong; each counted separately in the report.
- An export row with mode `keyed` voids the run (blind page only).
Report: correct share on W (n 13) and on R (n 12), each with the count of new-sign / unanswered / aside, plus a per-tile table.

## Interpretation rule (fixed now)
- W share >= 0.60 (8 or more of 13) AND R share >= 0.90 (11 or more of 12): "a person is an instrument for disputed positions of
  this hand" -> a person's read of the disputed positions of ink 63 is the next instrument toward D2.
- W share < 0.40 (5 or fewer of 13): "not an instrument" -> the lane turns to key-side and alignment work.
- Anything else (including W >= 0.60 with R < 0.90): undecided; no change of course on this test alone.
- Fewer than 20 of the 25 tiles answered (placed in a pile or new sign): no verdict ("incomplete"); the parent may ask once more.

## Known limits (stated before any answer)
1. W is small (13); the 0.60 / 0.40 cut points are 8 / 5 of 13. An undecided result is likely and is reported as such.
2. Every W row here is a position the committed reconciliation already reads right (unflagged rows are where it equals the truth);
   the test asks whether a person matches the truth where one blind reader failed, not where both did.
3. The tile map is label-aware toward passA (VIV-CLS), so qualifying rows lean to positions where passA's label fits a single tile;
   W is therefore passB-heavy: 8 of 13 are passB-only errors (z for 3 x4; r, t, l, a for n, R, L, @) and 5 are passA S-for-s rows.
4. The piles are labelled by the committed reconciliation, which on this leaf is close to the truth (circular); on ink 63 the piles
   would be noisier. A pass here is an upper bound on what the same packet does on ink 63.
5. Nothing on the page names a key value; the pile names are the transcription's own sign labels (allowed on a blind page).

## Addendum A (14 Oct 2026, 01:1x UTC by date -u; after a first page build, BEFORE publishing and before any answer exists)
A box check by eye of the 25 question tiles on their line context (the worker could see each tile's committed label and truth set in
questions.tsv while looking; stated, not hidden): 23 boxes hold exactly the one sign at their position; two do not, both on f.201r L04
where VIV-CLS's map is crowded by joined pen units:
- **Q06** (W, f201r_L04_s2_01_015, truth row 42): the box sits on the sign after the s (passA's neighbouring tokens S P m x: the map is off
  by one there); a person could not answer it right.
- **Q10** (R, f201r_L04_s2_01_011, truth row 38): the box holds two signs (the 6 and the joined sign after it).
Both are dropped from the page and from the score (column `excluded` in questions.tsv; nothing is redrawn). The scored sets become
**W = 12, R = 11** (23 tiles). The interpretation rule's cut points restated on these n, with the shares unchanged:
W >= 0.60 means 8 or more of 12; R >= 0.90 means 10 or more of 11; W < 0.40 means 4 or fewer of 12. "Incomplete" = fewer than 19 of
the 23 answered. The page title becomes "Vivonne f.201r: 23 signs to place". Everything else above stands.

## Addendum B (14 Oct 2026, 02:4x UTC by date -u; attempt 2, written and pushed BEFORE the attempt-2 page is built)
Why: the owner asked (02:4x UTC 14 Oct) to try again on the tiles scored against him. The parent's pile check (NOTES "VIV-HUMAN result")
found the attempt-1 page's "z" pile dominated by 3-shaped tiles and its "3" pile mixed, because the piles were labelled from the committed
f.201r reconciliation, which carries the 3/z confusion. Attempt 2 changes only the following; it is reported as **attempt 2 beside
attempt 1, never replacing it**, and attempt 1's score and verdict (W 5/12, R 10/11, undecided) stand as registered.
1. **Question tiles:** Q04, Q14, Q15, Q19, Q12, Q23 (the six scored against him) and Q24, Q25 (the two lost to the recut defect R12),
   eight tiles, same sids and boxes as attempt 1, shuffled with `random.Random(20261014)` and starting in the neutral pile `unsorted`
   and the tray, as before. The owner has seen these tiles once (stated, not hidden: attempt 2 is not a fresh blind sample).
2. **Piles 3, z, L, l, s, S, h, k** (the look-alike families these tiles touch): a tile carrying one of these committed labels is a pile
   member only if (a) it maps 1:1 (`tx/vivcls/real/map_r2_f201r.tsv`, op 1:1) to a truth row of
   `benchmark-tx/vivonne1573-f201r-dev.truth.tsv` with status `scored` and an EMPTY flag column, and (b) its committed label lies in that
   row's truth set. Tiles of these labels that fail go to no pile and are left out of the page; their count per label is appended below
   (before/after). A pile left with fewer than 3 members is shown anyway and named here. Every other pile is built as in attempt 1.
   The page stays blind (sign labels only; no key value, decode choice or reader weight).
3. **Lede:** one sentence added: do not use "Fix the cut" on this page (a recut tile cannot be placed yet, sorter requirement R12).
4. **Scoring (unchanged rule, run by the parent, not this job):** the same score.py rule per tile (correct iff the final label is in the
   tile's truth set; new sign, unanswered, aside etc. wrong), on n = 8: the six W tiles plus Q25 (W) and Q24 (R). Reported per tile and as
   W k/7, R k/1 for attempt 2, beside attempt 1. **No interpretation-rule verdict is drawn from attempt 2 alone** (n too small, tiles
   already seen); it answers one question: with truth-consistent 3 and z exemplars, does the owner place the d-sign tiles in pile 3?
   "Incomplete" = fewer than 7 of the 8 answered.
Built by `tx/vivhuman/build_inputs.py --attempt 2` (an option on the attempt-1 script, not a copy), output `tx/sorter_human2/`.

### Addendum B, build result (14 Oct 2026, 02:4x UTC by date -u; BEFORE any attempt-2 page was published, no answer exists)
`tx/vivhuman/build_inputs.py --attempt 2` applied rule 2 as written (tx/sorter_human2/filter.tsv; before -> after, every removal was a
flagged or unscored row, none a label outside its truth set): **3: 8 -> 0**, z: 18 -> 1, S: 7 -> 0, k: 2 -> 0, L: 4 -> 1, h: 5 -> 3,
s: 40 -> 22, l: 0 -> 0. The 3 pile is empty: of the 7 scored, unflagged truth rows labelled 3 (all clerk letter d), four are the question
tiles Q04/Q14/Q15/Q19 themselves and three have no 1:1 tile; the page's other 3-labelled tiles sit on clerk-split, align-conflict,
off-key or unaligned rows. A pile with no members cannot be shown, so the page cannot ask its own question ("does he place the d-sign
tiles in pile 3?"). A contact sheet of every 3/z/h/k tile with its truth row (scratch only) shows the one surviving z tile (truth a) and
the clerk-split z tiles (truth a) are themselves 3-shaped: on this hand the key's z (a) and 3 (d) signs look alike, so the attempt-1
z pile was not only mislabelled d-signs. **Attempt 2 was not built or published**; the rule is not loosened here. Handed to the parent.

## Addendum C (14 Oct 2026, 02:5x UTC by date -u; the parent's decision on the empty pile 3, written and pushed BEFORE the attempt-2 page is built)
The parent (session_01D7XWmthshMVqxumdDvitPh, 02:5x UTC) chose the exemplar source for the look-alike piles. Replaces Addendum B rule 2
only; rules 1, 3, 4 of Addendum B stand.
2'. **Piles 3, z, S, k, h, L, l, s:** every member is a truth-consistent tile from ANY of the three truth leaves of this hand: f.102r
   (`benchmark-tx/vivonne1573-f102r-dev2.truth.tsv`, map `tx/vivcls/train/map_r2_f102r.tsv`), f.103r
   (`benchmark-tx/vivonne1573-f103r-confirm2.truth.tsv`, map `tx/vivcls/train/map_r2_f103r.tsv`) and f.201r (as Addendum B: map
   `tx/vivcls/real/map_r2_f201r.tsv` via passA's alignment). A tile qualifies iff it is the only op-1:1 tile on its position, the
   position's truth row has status `scored` and an EMPTY flag, and the committed label (the row's `ref_sign`) lies in the row's truth set;
   the pile label is that `ref_sign`. The eight question tiles are never pile members. Both piles of each look-alike pair are drawn by
   this one rule, so neither is privileged. **Each pile is capped at 12 members**, sampled with `random.Random(20261014)` from the
   qualifying tiles in (leaf, line, position) order; a pile with fewer than 3 members is shown with what it has and named in the build
   result below. Every other pile is f.201r's as in attempt 1.
   f.102r and f.103r tiles are shown on their own line crops (images/c105_*, c106_* as committed in images/manifest.json, no new request);
   f.201r tiles on the f.201r region as before. The page stays blind (labels only).

### Addendum C, build result (14 Oct 2026, 02:5x UTC by date -u; built and published, no answer exists)
tx/sorter_human2/filter.tsv (qualifying -> shown, by leaf f102r/f103r/f201r): **3 11 -> 11 (4/7/0)**, **z 9 -> 9 (5/3/1)**, s 57 -> 12
(7/0/5), L 5 -> 5 (3/1/1), h 5 -> 5 (0/2/3), **k 2 -> 2 (1/1/0), under 3, shown**; **S 0 and l 0: no qualifying tile, so no pile S or l
on the page** (a pile with no members cannot be shown; Q23's truth set P|s|z and Q12's L|g do not need S or l). Page: 537 tiles, 37 piles
(36 named + `unsorted`), the 8 question tiles in the tray; https://claude.ai/artifact/M1MRM2J7ZgF1VxCoqiJZgx.
