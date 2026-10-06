# PREREG R9-WVOX -- does f.23's gloss key share sign->letter values with the 1069 and 174 keys? (written and pushed before scoring)

Worker R9-WVOX, account 4, 6 Oct 2026 (06:3x UTC by date -u), for LANE LANE-RUN9-account-4. Brief: .claude/briefs/runs/2026-10-06-account4-run9-jobs.md job R9-WVOX.
Disk only, no new crops (the two f.23 crops opened, r9align/crops_m/f23M_L01_s1.jpg and _s2.jpg, were cut by R9-WVOALIGN; its command is in PREREG-R9-WVOALIGN.md).

Inventories (letter-stripped copies in r9wvox/, ids opaque):
- A = f.23: the 26 shape codes of R9-WVOALIGN's blind passes (`r9wvox/f23_shapes.tsv`, shape descriptions written by this worker from
  the code names and two crops). Letter = the code's top aligned gloss letter where pass A's and pass B's keys
  (`r9align/key_passA.tsv`, `key_passB.tsv`) agree; codes where they disagree carry no letter and drop out of scoring. Not the pile key
  (r9align/key.tsv): piles mix shapes and carry no shape description.
- B = 1069 (`willem-van-hessen-1567/siblings/key_1069.tsv`, 41 classes, H; 'o' = the decipherer's null mark -> label NULL): `r9wvox/k1069_shapes.tsv`.
- C = 174 key leaf alphabet rows (`key_174_nomenclator.tsv`, 20 rows, each description may list homophones): `r9wvox/k174_shapes.tsv`.

Concordance (who decides which shapes are the same): one Sonnet subagent, text only, given ONLY the three letter-stripped description
files, asked for every pair (A-B, A-C, B-C) it judges to be the same written shape, confidence high/medium/low. Output
`r9wvox/concordance.tsv` committed as returned. This worker has seen the keys, so the concordance is delegated to keep letters out of it;
the residual leak is that this worker wrote A's descriptions (stated, not removable at this cost).

Statistic: for each key pair, S = number of high+medium concordant pairs whose two letters are equal (`r9wvox/score.py`).
Control: letter labels permuted within each key over that key's labelled signs (10000 draws, seed 1564), S recomputed on the same
concordance. It can vary on S: the concordance is fixed, the letters on the matched shapes move, so S under the null takes a spread of
values (mean, p95 and max reported); if a key pair's permutation distribution is degenerate (p95 = max = real), it is reported as a non-test.
Gate per key pair: S_real > permutation p95 -> PASS. Primary: f23 vs 1069 and f23 vs 174. 1069 vs 174 reported with the same gate.

On PASS for f23 vs 174: apply f.23's pass-agreed letters at M to the 174 letter body's transcribed spans that have no value (if any
transcription of the 174 letter body exists on disk; say if none). On PASS for f23 vs 1069: report which values are shared and say
what that implies (same key family 1563/1564), M only, no key.tsv change in either folder (a verifier grades). On FAIL: log in both
folders' HYPOTHESES.md.
