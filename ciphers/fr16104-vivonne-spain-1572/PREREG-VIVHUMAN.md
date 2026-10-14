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
