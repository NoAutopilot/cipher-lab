# PREREG SUR-PARTIAL (9 Oct 2026, 07:5x UTC by date -u; pushed in its own commit BEFORE any draw; partial.py pushed with it, unchanged after)
LANE FAMILY-A2g (account 2), job SUR-PARTIAL. Question (SUR-POOLPC's next): SUR-POOLPC measured power 1.000 at 65 pooled lines against a
FULL split (every m-facing y-family token written with another sign). How much of a PARTIAL split -- a second m sign used for a fraction f of
the m tokens -- would the same statistic detect, and so what does the real pooled NO SPLIT SHOWN exclude? CPU only, no fetch, no vision.

## Design (partial.py; imports poolpc.py unchanged)
- Same scaffolds (per pass A/B from the 65 pooled lines of 0744 L, 0744 R, 0745 L), same statistic S = n/(m+n), same DP aligner with T's
  [y-fam]={m,n} steer, same K = 300 deranged-gloss C1 draws per synthetic unit, same verdict rule (LEANS n iff S > p99.5; non-test iff
  m+n < 10, < K/2 usable draws, or p0.5 == p99.5), same master seed 20261010, 200 units per level per pass scaffold, all at 65 lines.
- Planted arm: each gloss m the scaffold draws as [y-fam] is written 'Mx' (not in T) with probability f, else stays [y-fam].
  Levels f = 0.25, 0.50, 0.75 (f = 1.00 is SUR-POOLPC's H1, detection 1.000/1.000; f = 0 is its H0, false LEANS 1/100).
- `partial.py --selftest` (run before this file, no verdict computed) checks only the planted share: 0.277 / 0.500 / 0.734 on 20 draws.

## Read-out (no pass/fail gate on the target; nothing real is re-scored)
Detection (LEANS n share) per level per scaffold. The real pooled NO SPLIT SHOWN (SUR-POOLPC, unchanged) is read as excluding, at power
>= 0.80, a second m sign used for a share >= f*, where f* is the smallest tested level with detection >= 0.80 on BOTH scaffolds; levels below
f* are stated as not excluded by this test. If no tested level reaches 0.80, f* = 1.00 (SUR-POOLPC) and 0.25-0.75 are not excluded.
No interpolation is claimed as measured; any between-level figure is labelled an interpolation.
Stated limits: the scaffold's facing distributions come from the steered aligner (control and target share the steer); 300-draw p99.5 is
noisier than the real run's 10,000; only one alternative (a second m sign) is planted, not a second n sign (the real S sits on the m side).

## Consequences
Whatever the result: no edit to key.tsv, key_period_*.tsv, conflicts.tsv, any transcription file, token grade, earlier .out file or N-class.
HYPOTHESES.md row with both numbers, NOTES section "SUR-PARTIAL (9 Oct 2026)", Remaining gaps / Escalation, gaps_check. Rule 10: report only.
