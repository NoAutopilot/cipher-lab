# PREREG-C1161-GLOSS9: gloss match + fr16 judge of the nine C1161-LOLO proposals vs key.tsv (4 Oct 2026, account-3 worker)

Written and pushed before any score is computed. Disk only. Brief `.claude/briefs/runs/2026-10-04-acct3-c1161-gloss9.md`.
Script `two/gloss9.py` (committed with this file, run only after the push). Outputs `two/gloss9.tsv`, `two/gloss9_gate.tsv`.
Instrument reused unchanged from RUN4-C1161GJ (tx/PREREG_glossjudge.md): G = glossctl statistic (difflib matching-block
letters of the 220-sign c186R block decode vs the 170 gloss letters, / 170; key.tsv reads 0.612); J = fr16 judge
`NgramModel.score` on the 3375-letter decode (key.tsv -1.233), read as a relative score only (gloss PASSes, decode FAILs).

## Values under test (A = key.tsv, B = C1161-LOLO proposal); c186R block tokens counted before this file was written
| sign | A | B | c186R block tokens |
|---|---|---|---|
| K | f | s | 2 |
| iib | l | d | 1 |
| l | s | f | 1 |
| ls | e | m | 2 |
| o | n | m | 5 |
| rot | r | h | 1 |
| spiralG | h | n | 0 |
| to | m | s | 2 |
| x | s | f | 1 |

## (a) Gloss half, per sign (each alone, the other 48 signs at key.tsv)
- dG = G(key.tsv with s=B) - G(key.tsv).
- dOcc = number of s's c186R occurrences that fall inside a difflib matching block under B, minus the same under A
  ("agreement at its own occurrences").
- Null: the folder's 50 shuffled-order anneal keys (`two/cons/key_shuf*_s*.tsv`, as RUN4-C1161GJ; absent signs take
  key.tsv), the same A->B swap in each; p95 of dG_null. It can differ from the real dG because the letters around s's
  positions differ under each shuffled key (the control varies the context the statistic counts).
- (a) holds iff block tokens >= 1 AND dG > 0 AND dOcc > 0 AND dG > null p95. Block tokens = 0 -> "no evidence" (never a pass).
  Note before scoring: RUN4-C1161GJ's G null p95 was 0.03-0.13 for 12-14-token signs; one token moves G by at most a few
  letters in 170 (~0.006 each), so a 1-2-token sign is expected to be unable to clear the null. That is reported as
  "no evidence at this gloss length", not as a refutation.

## (b) Judge half
- dJ9 = J(key.tsv + all nine B) - J(key.tsv), beside the same nine swaps in each of the 50 shuffled keys (report mean, p05, p95).
- Per sign dJ (alone) reported as information.
- (b) holds for a sign iff dJ of that sign alone >= 0 AND dJ of the final passing subset (all values that clear (a) and
  their own dJ >= 0, applied together) >= 0.

## Decision
A value passes iff (a) and (b) both hold. Passing values go to key.tsv at grade S naming the LOLO + gloss witnesses;
then decode_key --check, gaps_check, AUDIT propagation, depth_check. Nothing passes -> key.tsv unchanged, no grade moves,
no W/threshold/null re-tuning after the scores.
