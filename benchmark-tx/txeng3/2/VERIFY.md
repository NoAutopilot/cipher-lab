# VERIFY TXE3-2 FLOOR (verifier for the account-3 parent, session_0198Cv8ypBfBVfRToKVWx33M; 11 Oct 2026, 14:3x-14:5x UTC by date -u)

This is a separate verifier session. I did not run TXE3-2 and I did not try to protect its conclusions. Everything here is
re-derived from committed files with the committed scorers. I made no model reading pass, no image or vision read and no
network call beyond git. I opened no confirm or single-look item and wrote nothing to oracle1 or the owner's sorter pages.
None of the experiment's own files was changed; this file is the only one this verifier commits.

The two claims told to the owner at about 07:05 UTC:

1. "The 18 always-wrong signs on no.87 are not cut errors; they are sign mix-ups." -- **WRONG.**
2. "No tool we have would remove more than about 1 point of error from that floor." -- **OVERSTATED.**

The verdict the experiment registered for itself still stands. Its control failed the gate, so the per-sign classes are a
NON-TEST (7/18 = 0.389 against a gate of <= 0.25). Only the read-free insertion/deletion share counts as a measured result,
and that number re-derives exactly. Both claims to the owner were built from parts of the classifier that this gate voided.
The repository's own read-free files contradict the first claim.

## 1. Re-derivation (reported vs re-derived)

These are the commands, run on a scratch copy so that the experiment's files were not overwritten:
`python3 -I score_floor.py`, which regenerates floor.tsv byte-identical to the committed one;
`tools/tx_bench.py --bench BENCHMARK-TX.tsv --item birago1572-no87 --exclude-flagged <output>` for each of labels (L), passA,
passB, passC, passE_sheet and passF_fable; and `tools/tx_taxonomy.py` over the same six with `--boxes atlas/signs.tsv
--box-token atlas/no87_box_token.tsv --harvest harvest`, which reproduces positions6.tsv cell-identical in all 803 rows x 34 columns.

| quantity | reported (RESULTS.md) | re-derived | note |
|---|---|---|---|
| floor set (wrong in all six of L A B C E F) | 18 | 18, same positions | positions6.tsv cell-identical |
| control draw (seed 20261011, same line, right in all six, unflagged) | 18 | same 18 | replayed build_items.py draw |
| control invented-cause rate (PREREG step 6) | 7/18 = 0.389 | 7/18 = 0.389 | gate <= 0.25: FAIL |
| floor share with a cause other than (v) | 11/18 | 11/18 | 12/18 if PREREG step 5 is applied as worded (see objection 6) |
| control share with a cause other than (v) | 5/18 | 5/18 | 15/18 if step 5 is applied as worded |
| Fisher two-sided p | 0.32 | 0.3175 is 11/18 vs **7/18** (the registered comparison) | RESULTS prints it beside the 11/18 vs 5/18 row, whose own p is 0.092 |
| Q1 cut/joined | floor 0/18 | floor 0/18, controls 4/18 | Fisher p = 0.10, i.e. the cut flag fired only on right signs |
| classifier top-1 = readers' sign (floor) | 10/18 | 10/18 | |
| truth-set sign in top-2 (floor) | 1/18 | 1/18 | f178v L11.5 |
| control top-1 in truth set / = readers' sign | 12/18 / 11/18 | 12/18 / 11/18 | mean confidence 4.17 |
| image-side causes (Q1/Q2/Q4): control vs floor | 4/18 vs 6/18 | 4/18 vs 6/18 | |
| ampersand/abbreviation found at flagged positions | 4 of 11 | 4 of 11 | all alignment-doubtful |
| mapped floor classes | i 0, ii 5, iii 4 (flagged), iv 2, v 7 | same | |
| "instrument reach" | sorter 7/803, 3/792; box 4/803, 2/792; key decode 1/803, 1/792 | same | from the mapping the gate voided |
| floor size | 18/803 = 0.022; 7/792 = 0.009 | 0.0224; 0.0088 | |
| S/D/I as measured: A, B, C, L, E, F | 45/8/0, 64/8/6, 41/0/0, 34/0/0, 49/9/2, 52/19/2 | identical | tx_bench standard SER |
| S/D/I flagged-excluded: A, B, C, L, E, F | 34/8/0, 53/8/6, 30/0/0, 23/0/0, 39/8/2, 42/18/2 | identical | |
| I+D share: pooled six; single passes A B E F | 0.159 / 0.190; 0.205 / 0.236 | identical | |
| cost | USD 14.17 (LEDGER, parent fill from get_session, commit 967feff2b) | not re-derivable here | |

Every headline number re-derives. The objections below are about what the numbers are taken to mean, not about the
arithmetic.

## 2. Pre-registration order

- PREREG and positions6.tsv are commit 171be8be0 (committer time 05:54:54 UTC). This commit is an ancestor of another session's
  commit b18b355eb (05:55:17), so it was on origin by then.
- The items, answer.json files, floor.tsv, score_floor.py and RESULTS.md all appear first in bb1b45dcb (06:01:35).
- The appendix of the PREREG lists the 18 floor positions before any image was cut.
- The answer files carry no timestamps. So "pushed before any image call" is consistent with git but cannot be verified
  independently beyond push order. The whole run took about 6.7 minutes from the PREREG push to the results push: 13 line
  calls, the build and the write-up. That is fast but possible at four calls at a time.
- No deviation is declared. There is one undeclared deviation in the mapping (objection 6). It does not change the gate.

## 3. Gate, as registered

> "The floor classification is INFORMATIVE only if the invented-cause rate on the 18 controls is <= 0.25 (<= 4 of 18) AND lower
> than the share of floor positions given a cause other than (v) ... If the control rate is above 0.25, the classifier invents
> causes and the per-position classes are reported as 'unreliable at this N', the instrument ranking is NOT issued from them,
> and only the read-free I/D-vs-S share stands."

On the numbers, 7/18 = 0.389 > 0.25, so the result is NON-TEST. The registered verdict follows from the gate and the
experiment applied it correctly in its verdict line. Two sections of RESULTS.md then go past it:

- "Two observations that do not depend on the gate" reports 0/18 cut and top-1 = the readers' sign 10/18. Both are answers from
  the same classifier, so both fall under the gate.
- "Instrument reach if the mapping were trusted (it is not; for scale only)" prints the per-instrument numbers anyway, although
  the PREREG says the ranking is NOT issued.

The parent's two claims are built on exactly these two sections.

## 4. Control (rule 3)

The control can vary on the statistic. Floor and control positions are interleaved blind on the same line calls, with the same
crop, hand and reference sheet. The invented-cause statistic comes from the classifier's own answers, and it did vary: 7/18 on
the control against 11/18 non-(v) on the floor, and Q1 0/18 on the floor against 4/18 on the control.

The control measures false positives only. Nothing measures sensitivity: no position known to be cut was included as a
positive control. The f.178r L03 tail signs would have served, since TX-VIEWS (4 Oct 2026) records that the fixed-band crop cuts
them off for every reader. So even with a passing gate, "0/18 judged cut" could not have licensed "not cut" (rule 3: no
negative without a control that could have shown the positive).

What the control failure is made of: 6 of the 7 control inventions are sign-ID misses against the printed sheet. Two of those
are on f.178r L03 controls whose boxes were placed by proportion (46 boxes for 35 positions), and three are atlas boxes the
classifier saw as two signs joined. So part of the failure is material quality, not invented causes. It is a FAIL either way.

## 5. Split

no.87 is an **eval** item (BENCHMARK-TX.tsv). This job tuned nothing and produced no reader pass, so I see no eval look used for
tuning. Two cautions follow:

- The "next step" in RESULTS.md (a second classifier on Opus with the hand's exemplars, re-run on the same 18 floor signs) would
  be the same instrument with knobs changed, on the same eval positions.
- Any fix designed from this floor analysis (a sorter question, a box rule) has been designed while looking at eval truth, so it
  needs scoring on another item.

## 6. Claims

### Claim 1: "The 18 always-wrong signs on no.87 are not cut errors; they are sign mix-ups." -- WRONG

The verdict is "wrong" and not merely "overstated" because the repository's own committed read-free evidence points the other
way.

- **The classifier that produced "0/18 cut" failed its gate**, and its cut flag fired on 4/18 right signs and 0/18 floor signs.
  It also had no positive control (section 4).
- **The question it answered was about the atlas tile, not about the readers' crop.** Its own free notes put the sign at or
  below the crop's bottom edge at four floor positions, and each time it still answered Q1 "whole":
  - f178r L02.19: "the verticals extend slightly below the box";
  - f178v L02.12: "the box extends below the line crop";
  - f178v L05.1: "box reaches the bottom edge of the crop";
  - f178v L11.5: "bottom edge is close to the crop edge".
- **Read-free crop geometry, in the experiment's own committed positions6.tsv:** the atlas box runs outside the readers' line band
  (`band_edge = cut`) at 6 of the 14 floor positions the atlas covers: f178v L02.12, L05.1, L10.4, L11.5, L22.2 and L22.24. That
  is 43%, against 92/614 = 15% of the positions every reader got right (two-sided Fisher p = 0.013) and against 110/698 of all
  other positions (p = 0.016). This is an association, not a demonstrated cause, but it contradicts "not cut".
- **Prior committed findings:**
  - TX-VIEWS (benchmark-tx/tx-views-2026-10-04.md) records that the fixed-band crop cuts off the sloping f.178r L03 tail
    (positions 24-25 and 30-34) for every reader. Floor positions L03.31 and L03.34 are on that tail and were deleted by 4 and 3
    of the six outputs.
  - TXE-T (benchmark-tx/taxonomy/FLOOR-AUDIT.md) lists the 7 reader-wrong floor positions as "three T76 for an e-sign on
    band-cut lines" (L05.1, L10.4, L11.5), "two crop deletions on the f.178r L03 sloping tail" (L03.31, L03.34), and two it could
    not explain (f178r L02.19, f179r L02.8).
- **A tool on file already reads floor signs right after re-cropping.** The band-extent re-crop reads (TXE-B/B2,
  `tools/iiif_lines.py --band-extent`; benchmark-tx/outputs/birago1572-no87/passH_geo.tsv and passH2_geo.tsv) cover 10 of the 18
  floor positions:
  - H reads f178r L02.19 as T57, which is in the truth set; all six fixed-band outputs read T70 there.
  - H2 reads L02.19 (T57), L03.31 (T36) and f178v L05.1 (T66), all in the truth set.
- **Net:** among the 7 unflagged floor signs, six have crop evidence on file. Only f179r L02.8 (read T24 for e) has none.
- **"Sign mix-ups" is not what was measured.**
  - 11 of the 18 are positions where the truth itself is already flagged doubtful by TX-TRUTH-VERIFY: alignment-doubtful 8,
    clerk-doubtful 3.
  - The experiment's own reading is that on the page the signs look like what the readers read (top-1 = the readers' sign 10/18;
    truth in top-2 1/18). That is the opposite of a reader mix-up between look-alikes, and it comes from the voided classifier
    in any case.
  - The mapped look-alike class was 5/18, from the voided mapping.

**Corrected sentence:** "The cause of the 18 is not settled. 11 sit where the truth itself is already flagged doubtful. Of the
other 7, six have crop evidence already on file: two on the f.178r L03 tail the fixed-band crop cuts off, three e-signs on lines
whose crop cuts the sign's box, and one that both re-crop reads got right. One (f179r L02.8) is unexplained. The blind image
judge's 'none is cut' does not count, because it named a cause on 7 of 18 correctly read signs (gate 4) and was never tested
on a sign known to be cut."

### Claim 2: "No tool we have would remove more than about 1 point of error from that floor." -- OVERSTATED

- **Where the per-tool numbers come from:**
  - The numbers behind "about 1 point" (owner sorter 7/803 = 0.87 points, box check 0.50, key decode 0.12) come from the class
    mapping that the pre-registered gate voided.
  - RESULTS.md itself says "if the mapping were trusted (it is not; for scale only)".
  - No tool was run on the floor in this experiment.
- **The floor's own size:**
  - As measured, the floor is 18/803 = **2.2 points**. With the 11 truth-doubt flags excluded it is 7/792 = 0.9 points.
  - "About 1 point" is the flagged-excluded size of the whole floor. That is a ceiling set by the floor's size, not a measured
    limit of any tool, and it is quoted without the as-measured 2.2 (TRANSCRIPTION.md: "Never quote the flagged-excluded
    figure alone").
- **The ceiling, mapping-free:**
  - A reading tool can reach at most the 7 unflagged floor signs, 7/803 = 0.87 points as measured, unless some of the 11 flags
    are wrong.
  - A truth verifier resolving those 11 flags could move as-measured err_true by up to 11/803 = 1.4 points.
- **What tools on file actually reach**, scored here read-free against the current truth:
  - the band-extent re-crop read H2: 3 floor signs, on the 10 it covers;
  - the lattice key-constrained decode (all six TXE3-9 pins arms, and passL_lattice): 1 (f178v L11.5);
  - the owner-sort outputs passX20_owner and passX20b_no87sort: 0 of 18.

  So the size of the number is about right as a ceiling. Its stated basis, a tool evaluation, is not.

**Corrected sentence:** "The floor is 2.2 points of error as measured (18/803) and 0.9 points with the 11 truth-doubt flags set
aside (7/792). A reading tool can reach at most the 7 unflagged signs, about 0.9 points, unless those flags are wrong. So far
the tools on file reach 1 floor sign (key-constrained decode) to 3 (the band-extent re-crop read, which covered 10 of the 18).
This experiment issued no per-tool estimate of its own, because its judge failed its control."

## 7. Rule issues

- **Flagged-excluded quoted alone.** Claim 2's "about 1 point" corresponds to the 7/792 figure or to the voided mapping. The
  as-measured 2.2 points (18/803) is missing. RESULTS.md itself reports both figures.
- **Cost.** USD 14.17 against the USD 15 cap: under the cap.
  - It is above the PREREG's own 80% stop line (USD 12) and 3.5x its USD 4 estimate.
  - The worker could not read its own usage, so the stop line could not be enforced from inside.
  - The estimate priced the 13 Sonnet calls (USD 0.3 each) and not the Fable session itself (Usage 6, per-pass pricing).
- **Novelty words.** None in the claims. The PREREG's "first image-based classification" is about method, not a reading
  (rule 10 does not apply).
- **Rule 7.** All inputs and outputs needed to re-derive are committed, and all re-derive. The exact tx_taxonomy command line
  for positions6.tsv is not recorded. I reproduced it with the atlas and harvest arguments, cell-identical.

## 8. Objections

1. RESULTS.md, "Two observations that do not depend on the gate": both observations are outputs of the voided classifier, so
   they do depend on the gate. The 0/18-cut observation is also contradicted by the classifier's own Q5 notes and by
   positions6.tsv's band_edge.
2. RESULTS.md, "Instrument reach if the mapping were trusted": the PREREG says the ranking is NOT issued on a gate FAIL.
   Printing it "for scale" is how claim 2 reached the owner.
3. RESULTS.md, "For the owner", and the ROOM done line ("For the box-check team: boxes bound at about a fifth of a single pass
   error on no.87 and none of the floor") are wrong on two counts:
   - The I+D share is not an upper bound on what boxes or crops can fix, because a cut sign is usually read as a different sign
     (a substitution). Pass L has 0 insertions and deletions but 10 of its 34 errors on band-cut positions (positions6_summary,
     tx_taxonomy's crop class).
   - "None of the floor" is contradicted by the H/H2 re-crop reads (3 floor signs right) and the band-cut association.
4. Q1 asked whether the blue box on the atlas tile covers one sign. That box is not the readers' crop band, so even a passing
   Q1 would not answer "was the sign cut for the readers".
5. There is no positive control for the cut/joined judgement (section 4).
6. score_floor.py departs from PREREG step 5 without declaring it.
   - It adds "readers' sign not in the truth set" to the look-alike branch, and requires the readers' sign or a truth sign in
     the top-2 before hard_pair maps to (ii).
   - Applied as worded, step 5 gives floor (ii) 6 / (v) 6 and control (ii) 11 / (v) 3. On right signs the readers' sign is a
     truth sign, so the worded rule makes nearly every control a "look-alike".
   - The fix is sensible, but it should be declared. It does not touch the gate statistic (step 6).
7. RESULTS.md says every floor top-1 is off the truth set "by construction". That is wrong: it is an empirical 18/18, and the
   classifier could have named a truth-set sign.
8. The Fisher p = 0.32 is printed beside the "11/18 vs 5/18" row. It belongs to the registered 11/18 vs 7/18 comparison; the
   5/18 row's own p is 0.092.
9. The box placement on f.178r is not reliable. L03 used proportional boxes (46 found for 35 positions), and the classifier said
   one floor box (L03.34) was off the sign. Four of the 18 floor positions, and the L03 controls behind two of the control
   misses, rest on that placement.

## 9. Owner-safe sentence

TXE3-2 did not find out why the 18 signs fail. Its blind judge failed its own control, so "not cut" does not stand, and files
already on disk tie six of the seven unflagged floor signs to the crop. The floor is 2.2 points of error as measured and 0.9
with the 11 truth-doubt flags set aside. Its one measured result is the share of insertions and deletions (about a fifth of a
single reader's errors), and that share is not a cap on what better boxes or crops could fix.

## Second check (11 Oct 2026, written about 16:4x UTC by the account-3 parent from the second verifier's report; workflow wf_35ed2244-0e6)

A second, independent agent ruled on each objection and non-holds verdict above, re-running the commands itself. Where it disagrees with this file, this section governs.

### Rulings on the first verifier's objections

- **agree**: 1. RESULTS.md 'Two observations that do not depend on the gate' (0/18 cut; top-1 = readers' sign 10/18) are outputs of the voided classifier, so they do depend on the gate.
  - Evidence: PREREG-txeng3-2.md Gate: on a control rate above 0.25 'only the read-free I/D-vs-S share stands'. score_floor.py re-run on a scratch copy regenerates floor.tsv byte-identical and prints control invented-cause 7/18 = 0.389, so the gate fails. Q1 and Q3 are fields of the same answer.json files. The classifier's own sign-ID put top-1 in the truth set on only 12/18 right signs, so its floor top-1 says little. The ROOM done line (ROOM.md line 14643) repeats both observations as 'Stands anyway'.
- **agree**: 2. RESULTS.md 'Instrument reach if the mapping were trusted (... for scale only)' is printed although the PREREG says the instrument ranking is NOT issued on a gate FAIL; it became claim 2.
  - Evidence: The PREREG Gate says 'the instrument ranking is NOT issued from them'. RESULTS prints sorter 7/803, box 4/803 and key decode 1/803, then concludes 'no instrument reaches more than about 0.9 points'. That is where claim 2's 'about 1 point' comes from.
- **agree**: 3. RESULTS 'For the owner' and the ROOM line to the box-check team ('boxes bound at about a fifth of a single pass error on no.87 and none of the floor') are wrong: the I+D share is not an upper bound because cut signs are read as substitutions (pass L 0 I/D but 10/34 errors band-cut), and 'none of the floor' is contradicted by the H/H2 re-crops.
  - Evidence: Conclusion right, one supporting word too strong. Verified: positions6_summary.md shows L at 10/34 errors on band_edge=cut. TXE-B2 (txeng/geo/RESULTS-B2.md): the band-extent re-crop H2 against labels_geo fixed 7 and broke 4 positions where L has 0 insertions/deletions, so better crops change substitutions and the I+D share is no cap. f178r L02.19 (T70 in all six) is read T57, in the truth set, by both H and H2, so 'none of the floor' fails. The ROOM line is verbatim at line 14643. Correction: 'a cut sign is usually read as a different sign' is not supported for f178v. TXE-B (txeng/geo/RESULTS.md lines 89-97) found the band-cut class did not move under re-crop (A 5/14, H 5/14, H2 4/14) and called those errors 'look-alike misreads of a sign now fully visible'.
- **partly**: 4. Q1 asked whether the blue box on the atlas tile covers one sign, not whether the readers' line crop cut it, so 0/18 cut does not measure crop cuts.
  - Evidence: The premise is misdescribed. The prompt (items/*/prompt.md) defines Q1 'cut' as 'only part of a sign is in the box, or the crop edge cuts the sign'. build_items.py draws the blue box only on the readers' line crop (harvest s1/s2/s3), not on the tile. But the enlarged tiles are cut from the full source page (src.crop with a 14 px margin), so they always show the whole sign. The conclusion stands on the answers. Read-free geometry from committed seg_f178r/signs.tsv and the f178r manifest: L02.19's seg-exact box runs 25 of its 59 px below the readers' fixed band (y 251-310 vs band 155-285), and Q1 says 'whole'. Q1 says 'cut' on none of the roughly 12 band-cut boxes among the 36 (one 'joined'). Of the four Q5 notes quoted, L02.19 and L02.12 do place the sign or box past the crop edge, L05.1 says 'reaches', and L11.5 says only 'close to the crop edge'. Two control notes say the same kind of thing (L02.18, L03.15), so the notes are not floor-specific.
- **agree**: 5. No positive control for the cut/joined judgement (e.g. the f.178r L03 tail TX-VIEWS records as cut off), so a 'not cut' negative is unlicensed (rule 3).
  - Evidence: The PREREG control set is right signs only (step 2), and step 6 measures false positives only. Nothing measured sensitivity. tx-views-2026-10-04.md line 50: 'Seven f.178r L03 signs (pos 24-25, 30-34) ... the fixed-band crop cuts the sloping L03 tail off'. The floor already held two such signs (L03.31, L03.34), both answered 'whole'. Their boxes were proportional and possibly off the sign (L03.34's box lies wholly below the band, y 431-487 vs 285-420), so even those could not act as a valid in-sample positive control.
- **partly**: 5b (JSON). positions6.tsv has band_edge=cut at 6/14 atlas-covered floor positions vs 92/614 all-right (Fisher p 0.013); this contradicts 'not cut' and is not mentioned in RESULTS.
  - Evidence: Numbers verified: 6/14 vs 92/614, p = 0.0129; against all other positions 110/698, p = 0.016. grep confirms RESULTS.md never mentions band_edge. But 'contradicts' is too strong. The association is partly sign shape: right e-positions are band-cut 23/87, right T45 e-signs 21/54. Within plain e, floor 4/6 vs right 23/87 gives p = 0.057. The direct test already on file, TXE-B/B2's band-extent re-crop of f178v L05/L10/L22, did not move the band-cut class. TXE-B: 'L05.1 and L10.4 stay wrong: A, H and L all read T76 at L10.4'. So this is evidence against licensing 'not cut', not evidence that the crop is the cause.
- **partly**: 5c (JSON). The band-extent re-crop reads passH_geo/passH2_geo read 3 floor signs right (f178r L02.19, L03.31, f178v L05.1) where all six fixed-band outputs were wrong.
  - Evidence: Re-scored with tools/tx_taxonomy.py over the committed outputs. H covers 10 floor positions and reads 1 right (L02.19). H2 covers the same 10 and reads 3 right (L02.19, L03.31 T36, L05.1 T66). Only L02.19 is in both reads. H and H2 agree on 95.3% of positions, and H2 vs H is fixed 5 / broken 2, p 0.45, so H2's extra two are within read-to-read variance. The same re-crops still read L03.34 as T90, L10.4 as T76, L22.2 as T60 and L22.24 as T90. That is enough to refute 'none of the floor', not to show crop is the cause of most of it.
- **partly**: 6. score_floor.py departs from PREREG step 5 without declaring it; applied as worded, step 5 gives floor (ii) 6/(v) 6 and control (ii) 11/(v) 3, making nearly every control a look-alike.
  - Evidence: The deviation is real and undeclared. score_floor.py adds 'rsign not in truth' and requires rsign or a truth sign in the top-2 before hard_pair maps to (ii). Floor (ii) 6/(v) 6 as worded is verified. The control 11/3 figure only follows from a loose reading in which 'the other' may be the readers' sign itself. Read naturally, 'the other' is the other of the two candidates, and step 5 gives controls (ii) 2/(v) 12/(i) 4. The deviation then moves one floor position (L03.34) and one control (L03.15), not 'nearly every control'. Gate statistic (step 6) unaffected: agree.
- **agree**: 7. RESULTS says every floor top-1 is off the truth set 'by construction'; it is an empirical 18/18.
  - Evidence: The classifier saw a value-blind sheet of T10-T98 and could name any sign. floor.tsv shows all 18 floor top-1s outside the truth set, and truth in the top-2 at 1/18 (L11.5, T66). That is an observed result, not a constructed one.
- **agree**: 8. Fisher p = 0.32 is printed beside the 11/18 vs 5/18 row; it belongs to 11/18 vs 7/18 (the registered comparison); the 5/18 row's own p is 0.092.
  - Evidence: score_floor.py computes fisher(caused_f=11, ..., inv_c=7, ...), which gives 0.3175. Recomputed: 11 vs 7 gives 0.3175, 11 vs 5 gives 0.0922. The PREREG gate compares the control invented-cause rate with the floor's non-(v) share.
- **partly**: 9. f.178r box placement is not reliable: L03 used proportional boxes (46 for 35), the classifier said the L03.34 box was off the sign; four floor positions and the L03 controls behind two control misses rest on it.
  - Evidence: items.tsv records 'seg-proportional(46/35)' for all six L03 labels. Recomputed geometry puts the L03.34 box entirely below the readers' band (y 431-487 vs 285-420), consistent with the classifier's 'box sits off the sign'. Control misses L03.13 and L03.15 are on proportional boxes. But only 3 floor positions are on proportional boxes. L02.19's box is seg-exact (31 boxes for 31 positions), so the count is 3, or 4 only if 'f.178r placement' includes the seg-exact L02 boxes.
- **partly**: Claim-1 evidence: FLOOR-AUDIT.md (TXE-T) calls 5 of the 7 reader-wrong floor signs crop-related.
  - Evidence: FLOOR-AUDIT.md line 58 reads 'three T76 for an e-sign on band-cut lines (the n/e look-alike pair, key_real 76 e 3 = exactly these three), two crop deletions on the f.178r L03 sloping tail'. The same audit names the three as a look-alike pair, which supports 'mix-up' for them as much as 'crop'.
- **partly**: Verifier's corrected claim-1 sentence: 'Of the other 7, six have crop evidence already on file' (two L03 tail, three band-cut e-signs, L02.19).
  - Evidence: Overstated in the crop direction. Crop is directly implicated at L02.19: its box is 25/59 px below the band, and both re-crops read it right. It is implicated at L03.31: deleted by 4 of 6 outputs on the cut tail, right only in H2. At L03.34 the crop explains its 3 deletions, but every read that sees the pixels (C, L, H, H2) gives T90. At L05.1, L10.4 and L11.5 TXE-B's direct re-crop test did not help as a class. L10.4 stays T76 in both re-crops, L05.1 is right in H2 only, and L11.5 is uncovered. f179r L02.8 has nothing on file.
- **partly**: Rule issue: claim 2's 'about 1 point' quotes the flagged-excluded figure alone (TRANSCRIPTION.md line 36).
  - Evidence: RESULTS derives 'about 0.9 points' from the largest mapped reach, the sorter at 7/803 = 0.0087 as measured. That is an as-measured number from the voided mapping, which happens to equal 7/792. The TRANSCRIPTION.md breach is not established. The real defect is that the claim omits the floor's as-measured size (18/803 = 2.2 points) and rests on a voided basis.
- **agree**: Rule issue: cost USD 14.17 under the 15 cap but above the PREREG's own 80% line (USD 12) and 3.5x its USD 4 estimate; the estimate priced the Sonnet calls, not the Fable session.
  - Evidence: LEDGER.md line 4241: 14.17. The PREREG stop rule gives cap 15, stop line USD 12 and estimate USD 0.3 x 13 calls = USD 4, with no line for the orchestrating session.

### Final verdict on each claim told to the owner (11 Oct ~07:05 UTC)

- **wrong**: The 18 always-wrong signs on no.87 are not cut errors; they are sign mix-ups.
  - Evidence: (a) The basis is the TXE3-2 classifier, and its registered gate failed: score_floor.py re-derives 7/18 = 0.389 against <= 4/18. The PREREG then lets only the I/D share stand. The 'cut' answer never fired on a band-cut box, including L02.19, whose box runs 25/59 px below the readers' band, and no positive control existed. (b) 11 of the 18 carry verified TX-TRUTH-VERIFY flags (8 alignment, 3 clerk): there the clerk-text answer is the doubtful side, not a reader mix-up. (c) Of the 7 unflagged, the crop is implicated at f178r L02.19 (both band-extent re-crops H/H2 read T57, all six fixed-band outputs T70) and at L03.31 (deleted by 4 of 6 outputs on the tail TX-VIEWS records as cut off; right in H2). Against the crop: the f178v band-cut e-signs did not move under TXE-B's band-extent re-crop ('look-alike misreads of a sign now fully visible'; L10.4 T76 in A, H, L and H2). L03.34 is read T90 by every read that sees its pixels (C, L, H, H2). FLOOR-AUDIT calls the three T76 e-signs the n/e look-alike pair. f179r L02.8 has nothing on file. So the cause is mixed. The first verifier's 'six of seven have crop evidence' overstates in the other direction.
  - Corrected: The cause of the 18 is not settled, because TXE3-2's blind judge failed its control and its 'none is cut' does not count. Eleven of the 18 are places where the clerk-text answer itself is flagged doubtful, so they are not reader mix-ups. Of the other seven, the crop is implicated at two on f.178r: L02.19, which a wider crop read right twice, and L03.31, which the fixed band cuts off for most readers. An earlier wider-crop test did not fix the f.178v cut-edge e-signs, which look like reader look-alike errors. L03.34 is read the same wrong way whenever it is visible, and f.179r L02.8 is unexplained.
- **overstated**: No tool we have would remove more than about 1 point of error from that floor.
  - Evidence: 'About 1 point' comes from RESULTS' 'instrument reach if the mapping were trusted (it is not; for scale only)': the sorter's mapped reach of 7/803 = 0.87 points. That mapping is voided by the gate, the PREREG forbids issuing it, and no tool was run on the floor in TXE3-2. As a mapping-free ceiling the size is roughly right: a reading tool can reach at most the 7 unflagged signs (7/803 = 0.87 points) unless the flags are wrong. The claim omits the floor's as-measured size, 18/803 = 2.2 points (0.9 points, 7/792, with the flags set aside), and a truth verifier settling the 11 flags could move as-measured error by up to 11/803 = 1.4 points. Tools on file, re-scored: the band-extent re-crop reaches 1 (H) to 3 (H2) of the 10 floor signs it covers, the lattice key decode (passL_lattice and all six TXE3-9 pins arms) reaches 1 (f178v L11.5), and the owner-sort outputs passX20_owner and passX20b reach 0 of 18.
  - Corrected: The floor is 2.2 points of error as measured (18/803) and 0.9 points with the 11 doubtful answers set aside (7/792). A reading tool can recover at most the 7 unflagged signs, about 0.9 points, unless some flags are wrong. The tools on file so far reach 1 floor sign (the key-constrained decode) to 3 (a wider-crop re-read, which covered 10 of the 18). TXE3-2 itself produced no per-tool estimate, because its judge failed its control.
- **wrong**: (Downstream, to the box-check team, ROOM.md line 14643 and RESULTS 'For the owner'): boxes are bounded at about a fifth of a single pass's error on no.87 and none of the floor.
  - Evidence: The I+D share (0.205 single passes, re-derived) counts only insertions and deletions. Better crops also change substitutions: TXE-B2's H2 against L (which has 0 I/D) fixed 7 and broke 4, and f178r L02.19, wrong in all six fixed-band outputs, is read right by both band-extent re-crops. So the I+D share is no upper bound, and 'none of the floor' is contradicted on file. On the other side, TXE-B found the f178v band-cut errors did not move with a fuller crop, so the gain from boxes on no.87 is unmeasured, not large.
  - Corrected: Insertions and deletions are about a fifth of a single reader's errors on no.87 (0.15-0.29 by reader). That is not a cap on what better boxes or crops can fix, since a fuller crop has already corrected substitutions, including one floor sign. On f.178v the cut-edge errors did not move under an earlier fuller crop.

### Sentence the parent may give the owner

TXE3-2 did not find out why the 18 signs every method gets wrong on no.87 fail. Its blind image judge named a cause on 7 of 18 signs that were read correctly (the registered limit was 4), so its "none is cut" and its per-tool estimates do not stand. Files already on disk show that 11 of the 18 sit where the clerk-text answer itself is flagged doubtful, that a wider crop has already read one of the other seven right twice, and that an earlier wider crop did not fix the f.178v cut-edge signs. The floor is 2.2 points of error as measured (0.9 with the 11 doubtful answers set aside). The one measured result, insertions and deletions at about a fifth of a single reader's errors, is not a cap on what better boxes or crops could fix.
