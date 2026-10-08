# PREREG SUR-BLIND (8 Oct 2026, 22:2x UTC by date -u; pushed alone BEFORE either blind pass is read and before score.py exists)
LANE FAMILY (account 2), job SUR-BLIND. Folder Verdict's cheapest next: fresh held-out [ij]/[y-fam] units from FAM-SUR373's finds.

## Scope (stated deviation from the brief, forced by the cap)
The brief names 0743-0745 and 0701/0703 (about 8 written pages) at two blind passes per page plus a reconciliation: about 24 vision
units at ~1.5 each, about five times the USD 7 cap. This job runs ONE unit that can clear its own control alone: scan **0744 LEFT page**
(21 gloss+cipher pairs, crops_manifest.tsv), chosen on the 1400 px view because it is the densest single page with many visibly dotted
y/ij forms (the per-unit bar NZ-SURIJ/D1A-SURV set: a unit must clear its own control before any pooling). 0744 right, 0743, 0745,
0701, 0703 are not run (next step, priced in NOTES.md). 0744 is not in T (T = 0693+0702+0730 sign tables) and was never transcribed:
held out.

## Readers
Two independent blind Sonnet passes (A, B), each one call on the 21 crop paths only; told: 18th-century Dutch letter, each crop a
plain line above a cipher line; transcribe the plain line as written, and the cipher line sign by sign with the reader-code
vocabulary (Latin letter/digit look-alikes; [lambda] [delta] [hash] [psi] [w-tilde] [pi] [d-loop] &; [other: ...]); '|' at every
visible gap; **`[ij]` for a y/ij-shaped sign carrying two dots above, `y` for the same shape without dots** (the reader decides dots
from the image); '?' for illegible. No values, no key, no mention of what is being tested. Each pass's gloss rows are that pass's
gloss (no hand re-reading of the gloss). Cipher tokens are never edited.

## Score (score.py: R15-SURALIAS alias_run.run() unchanged, through R14-SURDP dp_align.py unchanged; T = pooled 0693+0702+0730
## sign tables + [sh-lig]={h}; C1 = 1,000 deranged-gloss draws, seed 744; every pair with tokens and gloss)
Run once per pass, each against its own gloss.
1. Scan level (held-out "same system under the current tables"): keyed aligned n, A, C1 mean/p99 -> SAME SYSTEM (DP) iff
   A >= 0.50 and A > C1 p99 (alias_run's rule).
2. [ij] class (alias A3, gated): every reader `[ij]` tagged; share of aligned tagged tokens whose gloss letter is in {m,n} (dp's
   [y-fam] = m|n), against the same share under C1 (can differ: derangement moves which letters face the tagged positions).
   Pass-level PASS iff n_al >= 10 and share >= 0.60 and share > C1 p99 of that share and scan A after >= A before - 0.010 and
   SAME SYSTEM. n_al < 10: non-test (D1A-SUR showed C1 p99 sits at ceiling below about 10).
   **Unit verdict: PASS iff BOTH passes PASS** (two independent blind readers; this replaces the reconciled single file, which the
   cap does not allow -- stated). One pass PASS: "not shown (readers disagree)". Both FAIL with n_al >= 10: FAIL.
3. Descriptive, no gate: the same share for the readers' undotted `y` (run 2 tags `y`); [ij] and y counts per pass; per-crop
   [ij] count agreement A vs B.
Consequence of a unit PASS: the dotted ij form reads in the m|n class on a held-out unit that cleared its own control (the per-unit
bar D1A-SURV named); handed to the lane for a separate verifier. No edit to key.tsv, key_period_*.tsv, conflicts.tsv or any
transcription file whatever the result. A FAIL or non-test changes nothing either.
