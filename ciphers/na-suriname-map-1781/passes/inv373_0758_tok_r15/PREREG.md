# R15-SUR758 PREREG -- per-token image check of 0758 reader `s` and `i j`, re-scored with R14-SURDP's DP

Written 6 Oct 2026 ~18:25 UTC (date -u before writing), pushed alone before any 0758 crop is fetched or looked at and before
retok_run.py exists. LANE-RUN15-account-2, job R15-SUR758. Basis: R15-SURALIAS (A2 blanket s -> [sh-lig] FAILed tolerance; A3 i j
non-test). The R15-SURALIAS A2 FAIL stands as logged; this is a separate test of image-labelled tokens only.

## Units (fixed from passes/inv373_0758_r14/passA_sonnet_blind.tsv, before looking)
- S-units (9): each reader `s s` pair counts as one unit, each lone `s` as one unit: L01 `s 3 l 6`; L04 `. s 3 v`; L04 `s s 3 r`;
  L05 `s [delta] i j`; L11 `s s e h`; L12 `r s e`; L13 `0 s b`; L13 `o s m`; L14 `3 s k`.
- IJ-units (4): L03 `e i j`; L05 `[delta] i j r`; L05 `e i j d`; L12 `[pi] i j n`.

## Labelling (worker's own eye, native region crop, cut with tools/iiif_lines.py, command pasted in NOTES.md)
Crop of the cipher row only, gloss line above excluded as far as the band allows. Labels fixed now:
- S-unit: `SH` = one tall long-s stroke with a closed loop, alone or joined to a short long-s stroke (the sheet's H row [sh-lig],
  as image-checked on 0730 by R15-SURALIAS); `S` = the sheet's script capital S form (reader `s`, = p); `TWO` = two separate signs
  (record both); `OTHER` = anything else, described; `?` = illegible / cannot locate the token.
- IJ-unit: `ONE` = one sign (a joined i-j / y-like form), `TWO` = two separate signs, `?` as above.
Caveat logged now: the worker has read R15-SURALIAS's post-hoc list of which A2 tokens hit h, so the labelling is not blind to the
gloss; to limit this, labels are decided on shape against the definitions above, and each label carries a one-line shape description.

## Re-score rule (retok_run.py; dp_align.py functions loaded unchanged, the alias_run.py driver; T = pooled 0693+0702+0730
## sign tables + [sh-lig] = {h}; C1 = gloss lines deranged between pairs, 1,000 draws, seed 758; every gloss-paired 0758 line)
- Only image labels change tokens: S-unit `SH` -> one `[sh-lig]` token (a `s s` pair becomes one token); `S`, `TWO`, `OTHER`, `?`
  -> unchanged reader tokens. IJ-unit `ONE` -> `[ij]` (dp sees [y-fam], T = m|n); `TWO`/`?` unchanged. No other token changes.
- Report scan-level before/after (keyed n, A, C1 mean/p99/max, verdict), and per class (SH, IJ-ONE): n_al, share in T, C1 share
  mean/p99.
## Gate (per class)
PASS iff n_al >= 5 and share >= 0.60 and share > C1 p99 of that share, AND scan A after >= A before - 0.010 AND the scan verdict
after is SAME SYSTEM (DP). n_al < 5: non-test (the IJ class has at most 4 units, so it is a non-test by construction here; reported
descriptively). Otherwise FAIL.
Consequence of PASS: image-labelled SH tokens grade S for h inside inv. 373 passes, written to retok_r15.tsv. key.tsv,
key_period_*.tsv, conflicts.tsv and every committed transcription/pass file stay unchanged whatever the result; a verifier decides any
key-file entry (ROOM flag).
