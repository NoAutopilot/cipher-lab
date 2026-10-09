# UNA-CEPPO pre-registration: f.21v count-1 split pairs, for coverage only (9 Oct 2026, account 4)

Written and pushed BEFORE any f.21v tile of these four tokens is cut or opened in this job, and before any score. Brief:
`.claude/briefs/runs/2026-10-09-account4-orch-unassigned-jobs.md` (UNA-CEPPO). D2-CEP21M (8 Oct 2026): no f.21v passage (max 39
letters) can reach AD 165, so nothing here can lift depth; this is coverage (S share) only.

## Rule sources searched (files on disk only, read 05:47-05:50 UTC by date -u, before any tile)
- Printed sheet (`sources/cryptiana/web/img/nevers_add1.png`, ids in `../../sign_id_map.json`): S61 = h (row 1), S94 = s (row 3),
  S32 = r (row 4), S40 = l (row 2), S25 = q (row 1), S26 = s (row 1, 9-like loop with a dot), S10 = s (row 4, 'L' with a dot in the
  angle). X_NEW is the off-sheet catch-all (no key value, decodes U).
- Glossed witness, fr.3252 f.36r/f.36v (`../../witness_f36/alignment_pairs.tsv`, 28 rows): glossed ids are S16, S45, NEW(=X_THETA2),
  S84, S80, S30/S49, S17, S26 (s x2), S89, S75, S70, S62, S57, S31, S24, S13. **S61, S94, S32, S40 and S25 are not glossed.**
- `../../witness/` (f.27, f.82 calibration witnesses) use key-row ids, not sheet S-ids, with no crosswalk on disk; not a rule source
  for this job (building one would be inventing a rule, which the brief forbids).

## Per pair
| token | passD | split | glossed side | rule |
|---|---|---|---|---|
| L01.11 | S61 (h) M | S61/S94 (h/s) | none | **no rule** -- skipped, no tile, stays M |
| L05.13 | S40 (l) M | S40/S32 (l/r) | none (S32 looped family [retired] for blind reads) | **no rule** -- skipped, no tile, stays M |
| L11.2 | X_NEW (U) L | X_NEW/S25 (-/q) | none | **no rule** -- skipped, no tile, stays U |
| L07.34 | S26 (s) L | S26/X_NEW (s/-) | S26 = s x2 (f.36v v36top_L01_s2 pos 13 H; f.36r r36_L09_s3 M) | **R-s** below |

R-s (L07.34 only): reference forms are (a) the two glossed S26 occurrences on fr.3252 f.36v/f.36r, cut at 4x from
`../../witness_f36/c38_f36v_top.jpg` and `c37_f36r_cipher.jpg`, and (b) the printed S26 and S10 cells. The tile is read by this
worker's eye, value-blind, written to `una_ceppo_reads_f21v.tsv` before any score:
- S26-FORM: a 9-like closed loop with a descending tail and a dot (the glossed form) -> rule decides **s** (S26).
- S10-FORM: an 'L' with a dot in the angle -> rule decides **s** (S10, printed only; value-neutral with S26).
- OTHER: neither form (e.g. the '2'-with-trailing-dash D07-CEP21 saw on a strip) -> rule decides **not-s** (X_NEW, U).
- UNDECIDED: cannot be judged at 4x -> no change.

## Gate (strict rule of D22/D07, pre-registered)
Change a label or grade only where (i) the rule decides the tile AND (ii) the decode score does not prefer the other value:
- S26-FORM: L07.34 conf L -> H (grade M -> S) only if the score with L07.34 = s is >= the score with L07.34 = X_NEW (U).
- S10-FORM: label S26 -> S10 with conf H (grade S, value s, the side rests on print only so the value, not the id, is what the
  witness backs); same score condition.
- OTHER: S26 -> X_NEW (U) only if the score with U is >= the score with s; else stays S26 at M (data conflict noted).
- (iii) `../../decode_control.py <seq> --shuffles 200 --windows 20 --err 0.15 --extra X_THETA2=r` ranks 1/201 with power >= 18/20 on
  seeds 1, 2, 3, before and after any change (run before on passD as committed regardless).
Placement control (can vary on the score, D07-CEP21 shape, `una_ceppo_control.py --n 500 --seed 1`): one random letter-bearing f.21v
token (not L07.34) set to s, 500 draws; report mean, p95 and the share reaching the real L07.34=s score; and one random letter-bearing
token set to U (deleted), 500 draws, against the L07.34=U score. Reported beside the target; the gate is (i)+(ii)+(iii).
Retirement: one decidable tile is the whole unit; if L07.34 is UNDECIDED at 4x the R-s read of L07.34 is [retired] for f.21v
(instrument: R-s eye read at 4x on c23_cipher_w.jpg), since D07-CEP21 already left it UNDECIDED on a strip.
Any changed token gets "VERIFIER WANTED" in an AUDIT.md grade note.
