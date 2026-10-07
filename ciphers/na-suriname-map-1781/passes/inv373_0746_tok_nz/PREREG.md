# NZ-SURIJ PREREG -- per-token image check of 0746 y-family and S tokens for the [ij] and [sh-lig] classes

Written 7 Oct 2026 09:48 UTC (date -u read 09:47), pushed alone before any 0746 image is fetched and before retok_run.py exists.
LANE LANE-NZ-0914, job NZ-SURIJ (account 4). Method copied from R15-SUR758 (passes/inv373_0758_tok_r15/PREREG.md).

## Premise correction (found before looking, from passA_sonnet_blind.tsv)
R15-SURALIAS/R15-SUR758 said 0746 "carries the same reader codes" `i j` and `s`. It does not: the R14-SUR746 blind reader wrote no
`i j` and no lowercase `s` on 0746. Its candidates are 75 y-family tokens (58 `y` + 4 `y` at line end + 13 `[y-fam]`; the one
`[y-fam] j` in L13 counts as one unit with its `j`) and 14 S-family tokens (11 `S`, 3 `[other: S-like]` in R02). So the [ij] form, if
present, hides inside the reader's `y` / `[y-fam]` codes, and [sh-lig], if present, inside `S` / S-like.

## Units (fixed now, in reading order per crop from passA_sonnet_blind.tsv)
- Y-units: every `y` and `[y-fam]` token (75; L13 `[y-fam] j` = one unit).
- S-units: every `S` and `[other: S-like]` token (14).

## Labelling (worker's own eye, native region crops cut with tools/iiif_lines.py using R14-SUR746's centres, command pasted in
## NOTES.md; the cipher row zoomed by PIL)
- Y-unit: `IJ` = i joined into j in one stroke with two dots above (the Dutch ij form as labelled ONE on 0758); `Y` = the y-form
  ([y-fam]) without two separate dots; `?` = cannot locate or cannot decide. Within a crop the units are matched to the image in reading
  order; if the count of y-family shapes seen differs from the reader's count, every unit of that crop is `?`.
- S-unit: `SH` = tall looped long-s, alone or joined to a short stroke (the [sh-lig] of 0730/0758); `S` = script capital S form (= p);
  `OTHER` described; `?`.
Labels are decided on shape, each with a one-line description; the worker has seen the gloss lines of R14-SUR746 (not blind to gloss),
caveat logged now. Units not labelled before the stop line are `?` (reported, never imputed).

## Re-score rule (retok_run.py: R15-SUR758's driver -> R15-SURALIAS alias_run.py -> R14-SURDP dp_align.py, unchanged; T = pooled
## 0693+0702+0730 sign tables + [sh-lig]={h}, as R15-SUR758; C1 = gloss deranged between pairs, 1,000 draws, seed 746; every
## gloss-paired 0746 line)
- Y-unit `IJ` -> `[ij]` token (dp sees [y-fam], T = m|n, as R15-SUR758); `Y`/`?` unchanged. S-unit `SH` -> `[sh-lig]` (T = h);
  `S`/`OTHER`/`?` unchanged. Since dp already reads `y` as [y-fam], the IJ relabel does not change any dp token value; the class
  statistic is the share of IJ-tagged aligned tokens whose gloss letter is in {m,n}, against the same share under C1 (which CAN differ:
  the deranged gloss moves which letters face the tagged positions).
- Report scan-level before/after (keyed n, A, C1 mean/p99, verdict) and per class (IJ, SH): n_al, agree, share, C1 share mean/p99.
  Also descriptive (no gate): the same share for the Y-labelled tokens (is the IJ form better on m/n than the plain y-form?).
## Gate (per class, 0746 alone -- rule 3 per-unit: 0746 must clear its own control before any pooling with 0758's 4/4)
PASS iff n_al >= 5 and share >= 0.60 and share > C1 p99 of that share, AND scan A after >= A before - 0.010 AND the scan verdict after
is SAME SYSTEM (DP). n_al < 5: non-test. Otherwise FAIL. Pooled 0746+0758 IJ is reported descriptively only, and only if 0746 PASSes.
Consequence of PASS: image-labelled tokens grade S inside inv. 373 passes (retok_nz.tsv). key.tsv, key_period_*.tsv, conflicts.tsv and
every committed transcription/pass file stay unchanged whatever the result; a verifier decides any key-file entry (ROOM flag).

## Step 2 (no score; descriptive same/different, fixed now)
Crops of the 4.VEL [s-loop] (2039 legend f, q; Remarque L2, L3; 2046 d) and [s-hook] (2046 e-h) tokens beside 0730/0758 [sh-lig] crops;
one blind look (worker's eye or one Sonnet call on crops only) with in-call controls: a known-same pair (two 0758 SH tokens) and a
known-different pair (0758 SH vs 0758 S1 short s-form). The look counts only if both controls come out right. No alias or key entry is
made from step 2 alone; a SAME verdict names the next pre-registered alias test.
