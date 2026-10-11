# TXE3-5 BOXES: verification (11 Oct 2026, 15:0x UTC by date -u)

The verifier is a separate session (a subagent of the account-3 parent, session_0198Cv8ypBfBVfRToKVWx33M). It did not run the
experiment and does not defend it. It re-derived the numbers from committed files only, in a sparse worktree of origin/main at
77c613a3e. It made no reader or vision call and used no network beyond git. It wrote nothing to the oracle pages or answers and
read no frozen confirm item. The experiment's own files are unchanged; this file is the only addition.

Under audit: the parent's two sentences to the owner (about 07:05 UTC 11 Oct 2026):
1. "The owner's box fixes gave fewer errors than the machine's boxes, and all 20 random edits of the same size made things worse."
2. "The gain is small: 4 errors in 343, all of it from the shadows he threw out (none from his re-cuts)."

## Verdicts

| # | claim | verdict | corrected sentence |
|---|---|---|---|
| 1 | owner's boxes beat the machine's; all 20 random same-size edits worse | **overstated** | "On one Birago page (12 lines), scored through the atlas classifier, which gets about 30% of signs wrong, your box fixes cut errors from 106 to 102 of 343. All 20 random deletions of boxes the same size did worse. But those random boxes were mostly real signs. Two rules that need no person do as well or better: dropping the last box of each line, or dropping the boxes the classifier itself calls unknown. So this does not show that your judgement on boxes lowers true error. Vivonne and La Luzerne were not tested." |
| 2 | gain 4 in 343, all from the trashed shadows, none from the re-cuts | **holds** (as arithmetic) | "The gain is small: 4 errors in 343 (0.309 -> 0.297; 0.299 -> 0.287 with the flagged signs left out). Removing the 11 shadows alone saves 5. The 3 re-cuts save nothing on their own and give one back when combined. The whole gain is 5 fewer extra tokens at line ends: no real sign is read better (1 fixed, 2 broken, all from the re-cuts). The line readers never emitted those shadows (passC has 0 insertions on these lines)." |

Gate as registered: **PASS reproduces** under both readings of its paired statistic (below). The PASS rests on a control that matches
the box sizes but not their position on the line. A position-matched check, run here after the fact, puts the owner's trash level
with a rule that needs no person.

## Re-derivation (committed scorer tools/tx_bench.py, unchanged since 6896cf0e, 10 Oct; BENCHMARK-TX.tsv unchanged since the run)

Chain re-run end to end into a scratch directory:
- build_arms.py (arms only): `arms/all_boxes.tsv` is byte-identical.
- `glyph_atlas.py classify --boxes ... --topk 3 --boxes-median-h 68`, re-run: `arms/all_boxes.k.tsv` is byte-identical, 30 s for
  7,990 boxes.
- The 48 output files: all byte-identical.
- score_arms.py, with only its output path changed: `scores.tsv` is identical, all 24 rows.
- proxy.py: `proxy.txt` is identical.
- `tools/tests/test_glyph_atlas.py`: ok.

So rule 7 holds for every figure in RESULTS.md.

| figure | reported (RESULTS.md / scores.tsv) | re-derived | note |
|---|---|---|---|
| machine err_true, as measured | 0.309 (106/343), S68 D26 I12 | 0.309 (106/343), S68 D26 I12 | same |
| machine, flagged excluded | 0.299 (101/338) | 0.299 (101/338) | same |
| owner err_true, as measured | 0.297 (102/343), S61 D33 I8 | 0.297 (102/343), S61 D33 I8 | same |
| owner, flagged excluded | 0.287 (97/338) | 0.287 (97/338) | same |
| owner vs machine, lines better/worse/tied | 5 / 1 / 6, sign p 0.22 | 5 / 1 / 6, p 0.2188 | paired line bootstrap of the SER difference: -0.024..0.000 (touches 0) |
| owner vs machine, sign-position McNemar (the registered "fixed - broken") | not reported | **fixed 1, broken 2 (92 -> 93 wrong)**, both masks | the registered paired statistic is -1 for the owner |
| trash only | 0.294 (101/343), -5 | 0.294 (101/343), -5; position fixed 0 / broken 0 | the gain is only inserted tokens: tx_bench "inserted" 14 -> 9 |
| re-cuts only | 0.309, net 0; "one box fixed, one broken" | 0.309, net 0 edits; **position fixed 1, broken 2** | broken: f178v L05.14 (T13 -> `_`), L11.32 (T52 had matched a T52-or-T96 truth); fixed: L11.30 (T83). RESULTS' "one broken" should read two |
| owner minus trash-only | (implied 0) | **+1 edit** | in combination the re-cuts cost one edit |
| controls, 20 seeds | err mean 0.326 (0.321-0.332), edits +4..+8, mean +5.65 | same; position fixed-broken -5..-8 per seed (6-10 signs broken each) | every seed deletes real signs |
| shadows' classes | `_` 8, T95 3 | `_` 8, T95 3; each the last sign box of its line, L07 the only line untouched | same |
| committed line reads, same 12 lines | passC 0.055, labels 0.035 | passC 0.055 (19/343, I 0), flagged-excl 0.041; labels 0.035 (12/343), 0.021 | same |
| lines scored | "12 of 27 lines, 15 missing" | 12 of **29** lines, **17** missing (tx_bench) | a slip in the count only; the figures are unaffected |
| Vivonne / Luzerne count proxy | sum\|boxes-ref\| 71 -> 87 (ctl 87.2) / 99 -> 68 (ctl 68.7); non-test | same | the worker's own non-test call is right |

### Verifier's post-hoc checks (not registered; eval tune lines; diagnostics only, never a gate or a tuning input)

Deleting a box does not change how any other box is classified. classify --boxes is a kNN over the atlas, per box, with the median
height fixed at 68. So each deletion arm below is the machine rows of the committed `arms/all_boxes.k.tsv` (kind=sign, in pos
order) with the named boxes removed, scored with `tx_bench --item birago1572-no87 --coverage-diagnostic --exclude-flagged --paired
outputs/machine.signs.tsv`. As a sanity check, "last box of every line except L07" reproduces the committed trash-only arm exactly
(101 / 96).

| arm (no person in the loop unless named) | edits as measured /343 | flagged excl /338 | position fixed / broken vs machine |
|---|---|---|---|
| machine | 106 | 101 | 0 / 0 |
| owner (trash + re-cuts) | 102 | 97 | 1 / 2 |
| owner trash only | 101 | 96 | 0 / 0 |
| drop the last box of all 12 lines | 102 | 97 | 0 / 1 |
| drop the last box of 11 of 12 lines (12 position-matched variants) | 101-103 (the owner's choice is the only 101; 6 variants 102, 5 variants 103) | 96-98 | 0 / 0-1 |
| drop the last box if the classifier reads `_` or T95 | 101 | 96 | 0 / 0 |
| drop every box the classifier reads `_` (29 boxes) | **95** | **90** | 0 / 0 |
| owner boxes, then drop every `_` | 95 | 90 | 1 / 2 |
| owner trash only, then drop every `_` | 94 | 89 | 0 / 0 |
| the 20 controls, then drop every `_` | 100-103 | -- | -- |

How to read this: once the classifier's own "unknown" tokens are dropped, which needs no person, the owner's boxes add 0 edits
(95 vs 95). The shadows alone add 1 (94). Under this metric, dropping an unknown token can only remove an insertion or turn a
substitution into a deletion, so it is close to free. That is also the whole mechanism of the owner's gain.

## Prereg order and deviations

- Order: the PREREG and the `--boxes` tool went in at f3e32015 (2026-10-11T06:01:28Z). Every output and score went in at c3641a35
  (06:06:01Z). The ROOM claim is stamped 05:58. The prereg was committed before the first committed score. The classify re-run
  takes 30 s here, so the 4.5-minute window is feasible. Commit order is the only evidence: no file timestamps survive.
- Declared: the proxy-1 S/D/I figures were read before the PREREG. The tune-line contamination of the Birago lines. The 26 scripted
  openings of eval truth.
- **Undeclared deviation 1 (the statistic):** the gate reads "the owner's paired improvement (fixed - broken) exceeds the control's
  at 19 of 20 seeds". In tx_bench, "fixed" and "broken" are the sign-position McNemar counts. RESULTS instead uses the unit-cost
  edit delta, and never reports the owner's fixed/broken, which is 1/2 (net -1). The gate still passes on the literal statistic:
  -1 beats every control's -5..-8. But under the registered statistic the owner arm improves no sign position. It is only less
  harmful than deleting random signs.
- Undeclared deviation 2 (harmless): the PREREG says "23 classify calls". The run made 1 call over all 24 arms. Classification is
  per box, so the two are equivalent.
- Slip: "12 of 27 lines / 15 missing" should read 12 of 29 / 17.

## Gate

Registered: "PASS if owner err_true < machine err_true AND the owner's paired improvement (fixed - broken) exceeds the control's at
19 of 20 seeds (p <= 0.05 one-sided against the control distribution) AND the control's mean is not below the machine's".

On the numbers:
- 0.297 < 0.309: yes.
- Owner beats the controls at 20/20 seeds: yes on fixed-broken (-1 vs -5..-8) and yes on edits (-4 vs +4..+8).
- Control mean 0.326 >= 0.309: yes.

**PASS.** RESULTS' "PASS, small" follows from the rule. The rule itself is weak (next section).

## Control (CLAUDE.md rule 3)

- The control can vary on the statistic, and it did: +4..+8 edits, 6-10 signs broken per seed. It is not a non-test.
- It does not match the design. The owner's 11 trashes are the last box of 11 of 12 lines, as the PREREG itself notes ("last-of-line
  boxes the line readers never read as signs"). The control deletes size-matched boxes anywhere on the line, which are almost all real
  signs, so "worse" was nearly certain by construction. The PREREG's own proof of variability says as much: "deleting a box that
  carries a true sign adds a deletion".
- This is rule 3's "match the design, not only the length and symbol count" (the Salviati lesson). A position-matched control
  (delete the last box of 11 random lines) scores 101-103 against the owner's 101. A no-person rule matches him (101) or beats him
  (95).
- The worker's own Vivonne/Luzerne count proxy is correctly labelled a rule-3 non-test, and reproduces.

## Split

- birago1572-no87 is eval. The 12 lines are the atlas's own tune lines, so the absolute figures are contaminated. This was declared,
  and the endpoint is the paired difference.
- No parameter was tuned on eval. median_h 68, knn 5, topk 3 and the mark rule are all fixed in the PREREG.
- Vivonne and Luzerne are dev and were used only for the count proxy.
- No frozen confirm item was read: proxy.py reads vivonne1573-f102r-dev, not f103r-confirm2.

## Rule issues and objections

1. Scope. Claim 1 speaks of "the owner's box fixes" in general. Only the Birago page (11 trashes, 3 re-cuts) was scored. His 11
   Vivonne merges and 31 Luzerne trashes were not tested, and the proxy for them is a non-test.
2. Pipeline. The tested route is an atlas kNN classifier at 0.30. The line readers on the same lines score 0.035-0.055 and emit no
   insertions (passC I 0), so the shadows the owner removed never reach the readers' output. The result says nothing about whether
   his boxes lower true error in the reading route.
3. Strength. Line level 5 better / 1 worse, sign test p 0.22. The paired bootstrap of the difference is -0.024..0.000. The Wilson
   intervals overlap almost entirely. RESULTS' owner paragraph says "the direction is real", which is stronger than this evidence:
   the direction is real only against random deletion of real signs.
4. Registered statistic swapped for edits, undeclared (above).
5. Cost: LEDGER shows USD 9.81 against the USD 15 cap; within cap. Flagged-excluded figures are always given beside the as-measured
   ones (TRANSCRIPTION.md). No novelty wording.
6. Next step, a suggestion only, not run here. Any re-test of the owner's boxes should compare against (a) a position-matched
   deletion control and (b) the machine pipeline with unknown tokens dropped, and should be scored on a route where boxes matter.
   RESULTS' cheaper next step, routing line-end dark boxes to the sorter as a question, is consistent with this. A filter rule would
   need its own pre-registered dev test before use; the numbers here come from eval lines.

## Re-derivation commands (from the worktree root)

```
python3 tools/glyph_atlas.py classify --out ciphers/nevers-birago-fr3251-1572/atlas --labels ciphers/nevers-birago-fr3251-1572/atlas/labels.json \
  --boxes benchmark-tx/txeng3/5/arms/all_boxes.tsv --tsv /tmp/k.tsv --topk 3 --boxes-median-h 68   # cmp with arms/all_boxes.k.tsv
python3 tools/tx_bench.py benchmark-tx/txeng3/5/outputs/owner.signs.tsv --item birago1572-no87 --coverage-diagnostic --exclude-flagged \
  --paired benchmark-tx/txeng3/5/outputs/machine.signs.tsv --ci     # owner: 102/343, 97/338; McNemar fixed 1 broken 2
# deletion arms: rows of arms/all_boxes.k.tsv with box 'machine|...' and kind=sign, sorted by (line, int(pos)), named boxes
# dropped, renumbered pos 1..n per line, written as line/pos/sign (code column), scored with the tx_bench line above
```

## Second check (11 Oct 2026, written 16:28 UTC by date -u, by the account-3 parent from the second verifier's report; workflow wf_35ed2244-0e6)

A second, independent agent ruled on each objection and non-holds verdict above, re-running the commands itself. Where it disagrees with this file, this section governs.

### Rulings on the first verifier's objections

- **partly**: 1. The registered paired statistic 'fixed - broken' (the sign-position McNemar) was swapped, without saying so, for the unit-cost edit delta, and the owner's fixed 1 / broken 2 is never reported.
  - Evidence: I re-ran tx_bench on owner.signs.tsv with --paired machine.signs.tsv. The McNemar is fixed 1, broken 2 (base wrong 92 -> 93; 87 -> 88 with flagged signs excluded), and RESULTS.md never reports it. That part of the objection holds.

But calling it an undeclared swap goes too far. tx_bench's own docstring (TOOL-SCORER-FIX, 10 Oct, before the PREREG) makes the per-line unit-cost edit total the --paired headline 'so an insertion repair counts'. paired_positions() is labelled 'the pre-fix headline; legacy and the beside figure', and the McNemar leaves insertions out by design. Insertions are exactly the mechanism the PREREG predicts (removing line-end shadows). The PREREG's own control paragraph argues in 'edit-distance score' terms. So the PREREG is ambiguous, and the worker used the scorer's documented headline.

The real faults are two: the McNemar was not printed beside the edit delta, and the gate never said which reading it used. The gate passes either way: owner -1 vs controls -5..-8 on the McNemar, and -4 vs +4..+8 on edits, 20/20 seeds both times.
- **agree**: 2. The control matches box size, not line-end position. The owner's 11 trashes are the last box of 11 of 12 lines, while the random picks are mostly real signs, so 'all 20 worse' was nearly guaranteed. This is rule 3's 'match the design' failure.
  - Evidence: I checked the 11 not-letter sids in settled.tsv against the last kind=sign box of each line in all_boxes.k.tsv. They are exactly the last boxes of the 11 lines other than L07.

Re-scored McNemar per control seed: fixed 0-3, broken 6-10, so fixed - broken runs -5..-8 and edits +4..+8. The machine reads 251 of 343 positions right, so deleting a random sign box costs an edit about 74% of the time.

The PREREG itself says the trashes are 'last-of-line boxes', so the position feature was known when the control was designed. The control did vary, so it is not a non-test. The fault lies in the registered design, not in how it was run.
- **partly**: 3. Post-hoc checks: dropping every '_' scores 95 vs the owner's 102. With that rule applied first, the owner's boxes add 0 (95 vs 95) and trash-only adds 1 (94). Dropping the last box of 11 random lines scores 101-103 vs the owner's 101.
  - Evidence: Every number reproduces exactly, using my own script over all_boxes.k.tsv and tx_bench:
- drop every '_' (29 boxes): 95/343 (90/338)
- owner then drop '_': 95
- trash-only then drop '_': 94
- the 20 controls then drop '_': 100-103
- drop the last box of 11 of 12 lines: 101-103. The owner's L07-skip is the only variant at 101; 6 variants score 102 and 5 score 103.
- drop the last box of all 12 lines: 102

Two caveats the verifier understates:
(a) The rule 'drop the last box if read _ or T95' (101), which VERIFY.md and the report cite as a no-person rule that matches the owner, was fitted after the fact. T95 was picked because the 3 non-'_' shadows read T95, and BENCHMARK-TX.tsv lists T95 as a real key sign (s|l). The untailored rule 'drop the last box if read _' scores 102. So honest line-end rules tie the owner's full arm (102) but trail his trash alone (101), and his trash choice ranks first of the 12 position-matched variants.
(b) 'Drop every _' wins under this metric by construction. In tx_bench, '_' is not an abstention token and never matches truth, so dropping it can only remove an insertion or turn an S into a D. It is a diagnostic of the metric and this pipeline, run on eval tune lines, not a validated rule.
- **agree**: 4. RESULTS says 'the 3 re-cuts net 0 (one box fixed, one broken)'. The McNemar for re-cuts only is fixed 1, broken 2, and combined with the trash the re-cuts cost +1 edit.
  - Evidence: Per-position alignment through tx_bench.align (truth values not printed):
- L05 pos 14 broken: the T13 read is lost and the re-cut box reads '_'.
- L11 pos 30 fixed: the re-cut box now reads T83 there.
- L11 pos 32 broken: the old box's T52 match is lost.
- L10: the re-cut changes only which token is an insertion.

In recut-only, the L11 change also absorbs one insertion (14 -> 13), so the edit total is 106, net 0. When the trash is also applied, that insertion is already gone, so the owner arm is 102 against trash-only 101: +1. The McNemar is 1/2 in both arms. 'One box fixed, one broken' is box-level shorthand; at the position unit the PREREG uses, it is 1 fixed and 2 broken.
- **agree**: 5. RESULTS says '12 of 27 lines, 15 missing'; the item has 29 lines, 17 missing.
  - Evidence: BENCHMARK-TX.tsv row 4 lists f178r_L01-03, f178v_L01-23 and f179r_L01-03, which is 29 lines. tx_bench prints 'lines missing 17'. Only the count is wrong; no figure changes.
- **partly**: 6. The PREREG says 23 classify calls; the run made 1 call over 24 arms. Undeclared but harmless.
  - Evidence: Harmless: agreed. Undeclared: too strong. RESULTS.md 'Numbers of record' states 'Classify calls: 1 (7,990 boxes)'. It just doesn't flag this as a deviation, and the PREREG's own 23 was an off-by-one: 4 named arms + 20 controls = 24.

Why one call is safe: classify_boxes fixes mh at 68 (--boxes-median-h), binarises per source image, projects with the atlas-fitted proj, and votes kNN over atlas boxes only. Empirically, no (box, geometry) pair gets a different label in any of the 24 arms.
- **agree**: 7. Scope: the test pipeline is an atlas classifier at 0.30, while the line readers on these lines score 0.035-0.055 with no insertions, so the result says nothing about the reading route.
  - Evidence: Filtered to f178v L01-12:
- passC: 0.055 (19/343), S19 D0 I0
- labels: 0.035 (12/343), I0

I also checked passA (I 1) and passB (I 4). On every one of the 12 lines, their last two tokens equal passC's, so their insertions sit mid-line. No line reader emits a trailing shadow. Line readers read line crops, not these boxes.
- **agree**: 8. RESULTS' 'so the direction is real' is stronger than line p 0.22 and a CI touching zero.
  - Evidence: Lines go 5 better / 1 worse / 6 tied, sign test p 0.2188. The paired line bootstrap of the SER difference is -0.024..0.000. The Wilson intervals (0.251-0.348 vs 0.262-0.360) overlap almost entirely. The only support for 'real' is the 20/20 control, which is the weak, size-matched one from objection 2.

### Final verdict on each claim told to the owner (11 Oct ~07:05 UTC)

- **overstated**: The owner's box fixes gave fewer errors than the machine's boxes, and all 20 random edits of the same size made things worse.
  - Evidence: The figures reproduce: 102 vs 106 of 343 (97 vs 101 of 338 flagged-excluded), and the controls score 110-114. But:
- Only one Birago page was tested (12 lines, eval, the atlas's tune lines), through an atlas kNN at 0.30.
- Lines: p 0.22, and the bootstrap CI touches 0.
- The control removed mostly real signs.
- Untailored no-person rules (drop each line's last box, or drop it only if read '_') score 102, the same as the owner's full arm. Dropping every '_' scores 95, but that rule wins under this metric by construction.
- The owner's trash choice alone (101) does rank first of 12 position-matched variants, an edge of 1-2 edits.
- The line readers never emit the shadows.
- Vivonne and Luzerne were only count-proxied, which is a non-test.

The verifier's 'overstated' is right. Its supporting rule 'drop last if _ or T95' was fitted after the fact and should not be cited.
  - Corrected: On one Birago page (12 lines), read through the atlas classifier, which gets about 30% of signs wrong, your box fixes cut errors from 106 to 102 of 343 (101 to 97 of 338 with flagged signs left out). All 20 random edits of the same size did worse, but those mostly removed real signs. Two simple automatic rules, dropping each line's last box or dropping it only when the classifier reads it as unknown, also reach 102 (checks run afterwards on the same lines, not tested rules). So this does not show that your box judgement adds accuracy beyond such a rule. Vivonne and La Luzerne were not tested.
- **holds**: The gain is small: 4 errors in 343, all of it from the shadows he threw out (none from his re-cuts).
  - Evidence: Owner 102 vs machine 106 of 343, and 97 vs 101 of 338 flagged-excluded.
- Trash-only is 101 (-5). The 5 come from 5 insertions removed at the ends of L01, L02, L03, L10 and L11; no sign position changes (McNemar 0/0).
- Re-cuts only: 106 (net 0). Combined with the trash they cost +1, with McNemar fixed 1, broken 2.

The verifier's corrected sentence ('no real sign is read better') needs 'on balance', because one position is fixed by a re-cut. With only 3 re-cuts, 'none from re-cuts' is arithmetic, not evidence that re-cuts don't help.
  - Corrected: The gain is small: 4 errors in 343 (0.309 -> 0.297; 0.299 -> 0.287 with flagged signs left out). Throwing out the 11 shadows saves 5, all of them extra tokens at line ends; no sign position changes. The 3 re-cuts save nothing alone and cost one when combined (one sign fixed, two broken), which is too few re-cuts to judge them.

### Sentence the parent may give the owner

On the one Birago page we could score (12 lines, read through the atlas classifier), your box fixes cut errors from 106 to 102 of 343. The whole gain came from the 11 line-end shadows you threw out; the 3 re-cuts added nothing. But a simple automatic rule we checked afterwards on the same lines, dropping each line's last box, also gets 102, so this does not yet show that your box judgement lowers true error, and Vivonne and La Luzerne were not tested.
