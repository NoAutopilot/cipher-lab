# PREREG-MONL-R0S (15 Oct 2026, account 1, for LANE DEFAULT-A1-1426-15) -- committed before any scoring

Question: does the code-wide hypothesis K14 = s (R0s of MONL-K14TRY: n 51 over c172 + c268 L01-L25, statistic +549.8 bits over p,
value-class null p95 419.3, positional null "could not be built") clear a positional null, so that it is licensed, kept M, or refused?

Why the tool's null failed: `tools/decode_key.py --try` null 1 draws n = 51 pseudo-code positions among tokens whose current value
equals K14's (p); only 24 non-K14 tokens read p (K34, K47), so the pool is too small.

## The positional null (script: k14try/r0s/run_r0s.py, imports tools/decode_key.py's Crossword and lm, fr16, window 8, as MONL-K14TRY)
- Statistic: the --try statistic, sum over the code's occurrences of score(window with the code read s) - score(window read p),
  every other token as in key.tsv (same as R0s).
- Null draw: n positions sampled without replacement from the pool; each is set to a pseudo-code whose current value is p; the
  same statistic (s minus p) is computed at those positions. 200 draws per null, Random(1573).
- Pool N1 (primary): every sign position in both streams with a one-letter value, code not in the tested code set, current value
  not s (genuine s tokens would mimic a true s code) and not null/unknown.
- Pool N2 (sensitivity): N1 restricted to positions whose current value is a consonant (not a e i o u y), since p is a consonant.
- What it permutes: which positions carry the p-vs-s question. What it can do differently from the target (rule 3 orthogonal-control
  clause): the statistic depends on each occurrence's neighbours, and the null changes the neighbours (different positions); it
  measures the s-over-p preference French gives at a random non-s spot from letter frequency alone, which is exactly what R0s's
  +549.8 must beat. It is not a coverage- or order-only control.

## Controls (same null construction, code-wide, chosen by the key table, not by the clear text)
- PC (power): every table-s token (K17, K37, K67; n expected 29) relabelled to a pseudo-code with current value p, try s. Must be
  above both N1 and N2 p95 at its own n.
- NC (negative): every table-p token other than K14 (K34, K47; n expected 24), current p, try s. Must NOT be above the N1 p95.
- If PC fails (no power) or NC passes (null too lax): the test is a non-test; R0s stays **undecided, K14 stays p (M where it
  faces s)**, nothing written.

## Decision for R0s (controls passed)
- **Licensed (grade S lead)**: statistic above the N1 p95 AND the N2 p95 AND the value-class p95 (recomputed), AND no more than a
  quarter of the 51 occurrences lose over 3 bits (the tool's breakage rule). Written ONLY to k14try/r0s/LEAD-K14s.tsv (code, value,
  grade S, the numbers); **key.tsv is not edited** (a code-wide change of a published-table value, against 7 p-facing occurrences,
  is a verifier's step; the lead file names it).
- **Refused**: statistic at or below the N1 p95 (controls passed): "K14's s-preference is no greater than a random non-s code's";
  logged in NOTES, K14 stays p.
- **Stays M (undecided)**: any other combination (above N1 but not N2 or the value class, or the breakage rule fails).
- Reported with the empirical p (share of draws >= statistic) for each null; no re-run with other seeds or pools after scoring.
