# R15-SURALIAS PREREG -- reader-code alias pass on inv. 373 scans 0702, 0730, 0758, re-scored with R14-SURDP's DP

Written 6 Oct 2026 ~17:58 UTC (date -u 17:56 before writing), pushed alone before alias_run.py exists or any scored run.
LANE-RUN15-account-2, job R15-SURALIAS. Verifier basis: R15-SURV (NOTES.md section, image checks of K, 0758 s, 0758 i j).

## Image check of the two 0730 codes (done before this file, R15-SURALIAS's own eye)
One service.archief.nl region `{base}/180,650,2240,450/full/0/default.jpg` (base as passes/inv373_0730_r13/crops/manifest.tsv;
pair lines L04-L06), crop step `python3 tools/iiif_lines.py --image <scratch>/r.jpg --out <scratch>/c --prefix p0730r --debug`
(6 lines), zoomed 3x by PIL. Not committed (folder over 30 MB).
- `[other: ss-like]` under "het" (L05 "3ÿ ſſ3λ" = "en het", L06 "3l#l ſſ3λ" = "en op het"): one ligature, a short long-s stroke
  joined to a tall looped long-s, one sign. Matches the period sheet's H row [sh-lig] "long-s / f with loop (Sh-like ligature)" = h.
- `[other: f-like]` under "is" (L04 "ʃ6" = "is", 6 = s H): a tall long f with a mid crossbar and a closed loop at the foot. Matches
  the sheet's long f (I/J row), reader code `f` = i (H in key_period_codes_nieuw.tsv).

## Aliases (fixed now; applied by alias_run.py to copies of the blind pass strings; the committed pass files are not edited)
| # | scans | reader string | alias to | sheet value |
|---|---|---|---|---|
| A1 | all three | `K` (outside brackets) | `k` | o (H) |
| A2 | 0758 | `s s` (two space-separated s tokens) then any single `s` token | `[sh-lig]` | h |
| A3 | 0758 | `i j` (adjacent tokens) | `[ij]` (dp_align's ALIAS -> `[y-fam]`, T = m|n) | n |
| A4 | 0730 | `[other: ss-like]` | `[sh-lig]` | h |
| A5 | 0730 | `[other: f-like]` | `f` | i (H) |
Not aliased (not image-checked): `[thorn]`, `[other: ss/ff ...]`, `[other: ff-like]`, lone 0758 `j`.

## Instrument
dp_align.py (R14-SURDP) functions loaded unchanged, the dp2_run.py driver pattern (drop `[plain` tokens). T = pooled sign_table.tsv
of the other scans (own scan left out: 0702 <- 0693+0730; 0730 <- 0693+0702; 0758 <- 0693+0702+0730), plus one entry from the period
sheet: `[sh-lig]` = {h} (no inv. 373 table has the code yet). The same T is used before and after aliasing.
Runs: every gloss-paired line of each scan (not a subset), seeds 702 / 730 / 758; C1 = gloss lines deranged between pairs, 1,000
draws, every pair re-aligned (it can vary on every statistic below).

## Numbers reported (both, per scan)
- Scan level, before and after: keyed aligned n, A, C1 mean / p99 / max, verdict as R14-SURDP (A >= 0.50 and A > C1 p99).
- Per alias (after only): n_al = aliased tokens DP-aligned to a gloss letter; a = share of those whose letter is in the alias's T set;
  C1 distribution of the same share over the same 1,000 deranged-gloss draws (mean, p99).

## Gate (per alias, per scan)
PASS iff n_al >= 5 and a >= 0.60 and a > C1 p99 of the alias share, AND the scan's A after >= A before - 0.010 and the scan verdict
after is still SAME SYSTEM (DP). n_al < 5: non-test. Otherwise FAIL.
Consequence of PASS: the aliased tokens count as grade S (cryptanalytic with a control) for the alias's value in inv. 373, and the
alias is written to `alias_r15.tsv` for later passes. key.tsv, key_period_*.tsv, conflicts.tsv and every transcription file stay
unchanged in this job whatever the result (the aliases are reader-code equivalences inside the inv. 373 passes, not map-key values);
a verifier decides any key-file entry. A FAIL is logged in HYPOTHESES.md as a FAIL of that alias with both numbers.
