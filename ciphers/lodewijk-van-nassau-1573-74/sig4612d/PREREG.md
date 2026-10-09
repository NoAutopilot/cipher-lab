# SIG-4612D pre-registration -- crib placement on 4612 v3, attempt 2 of 3 (changed design)

Written 9 Oct 2026 04:0x UTC by date -u, worker SIG-4612D (Opus) for LANE SIG-4 (account 1), before `sig4612d/crib_place2.py` exists
and before any new control run or any 4612 score. Brief: `.claude/briefs/runs/2026-10-09-acct1-sig4-jobs.md` "## SIG-4612D".
Attempt 1 (SIG-4612C, `sig4612c/PREREG.md`, b35f566e4) failed control (a) on false reassignments (mean 2.5 per seed vs <= 2.0).
Rule 3's third-attempt clause: this attempt changes the DESIGN (which reassignments are admitted), not a threshold.

## Unchanged from sig4612c/PREREG.md (copied by reference, not relaxed)
Data and stream rule; key_full folding; word-share rule (fr16 lexicon, words >= 3 letters); the same 25 topical cribs; placement share
THETA = 0.60; overlap resolution; contradiction rule (step 3); statistic G; f calibration grid and procedure (20 seeds, seed 9000+s);
control (a) seeds (perturbation seed s, crib draw seed 1000+s, s = 0..9) and its Groen IV CDLXXXIII crib pool; RECOVERED / FALSE /
RECOVERABLE definitions; pools and seeds of (b) (46120+d, 200 draws) and (c) (46220+k, 200 shuffles); p95 'linear'; gate (target)
(a) passes AND G_topical > p95(b) AND G_topical > p95(c). 276 is not used as a value anywhere.

## The design change: admission filter (new step 3a, identical for target and every control)
After step 3 gives the consistent reassignments {c -> L}, a reassignment is ADMITTED only if (i) or (ii):
(i) Two-placement support: c -> L is implied by >= 2 distinct kept placements. Kept placements never overlap (step 2), so any two
    distinct kept placements are non-overlapping windows; this satisfies "different cribs or non-overlapping windows".
(ii) One placement plus a whole-stream per-code check: c -> L is implied by exactly one kept placement P, and over O = every
    occurrence of c in the stream (all segments) outside P's window:
      |O| >= 3, and
      cov(O | key with c -> L alone) - cov(O | key) >= 0.20,
    where cov(O | k) = share of positions in O that lie inside an fr16 word of >= 3 letters under key k, by the same word_share rule
    (a position is covered if some lexicon word of >= 3 letters spans it within its null-skipped segment). "key" is the key the
    procedure runs with (the perturbed key in control (a), key_full on 4612 and in (b)/(c)); no other reassignment is applied in the check.
Only admitted reassignments enter G and the RECOVERED/FALSE counts. Non-admitted ones are reported but not applied.

## Gate (a), re-fixed recall bar (reason written before the run)
Gate (a): pooled recall sum(RECOVERED)/sum(RECOVERABLE) >= 0.30 AND mean FALSE per seed <= 2.0 (unchanged) AND mean G > 0 (unchanged).
sum(RECOVERABLE) == 0 is a FAIL. Reason for 0.30 (was 0.50): attempt 1 reached 0.512 recall with 22.5% of its consistent reassignments
false; the point of this design is fewer, better-supported reassignments, so the filter is expected to cost recall, and the brief fixes
0.30 as the floor. Recall at 0.30 still means the procedure restores nearly a third of the planted errors it can reach. RECOVERABLE is
unchanged (the denominator does not shrink with the filter).
If (a) fails any bar: stop, CONTROL BELOW GATE, attempt 2 of 3 logged, 4612 not scored.

## On PASS only
As sig4612c/PREREG.md: apply admitted reassignments through a decode config (never hand-edit key_full.tsv), reassigned codes graded S
at most, tokens inside a crib placement M; `tools/decode_key.py ... --check` exit 0; judge_plaintext on the 4612 decode and on a
shuffled-control decode through the same judge (ARM-C1 clause).

No parameter (0.20 margin, |O| >= 3, 0.30 recall, the rest above) is changed after this file is pushed.
