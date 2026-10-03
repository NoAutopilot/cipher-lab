# FT4u pre-registration (account-4, 3 Oct 2026, written 13:2x UTC by the clock, pushed before any registered score)

Step (FT4t's Verdict, part 1): the FT4s anchored split's other segments of the f.266r numerals / f.265r slip pair, S2 and S3,
as second witnesses for f.206 C codes other than 722. Neither segment holds 722 (checked by index, FT4t), so this is not a 722 test.
Same instrument as FT4s (resolved, PASS on S1), applied to unscored material: not a re-tuning (rule 3's third-attempt clause n/a).

Instrument: `align/ft4u_seg.py` (imports ft4s_seg's solve_pins/E unchanged; cut, model, MAXLEN 12, <= 1 edit, sublimit 10 s, Pool(4)).
- Cut (FT4s, unchanged): 501 'et' groups 75, 139 <-> whole words 45, 78; anchor tokens excluded.
- **S2** = groups 76..138 (63 groups) <-> slip words 46..77 ("le bergamasc ... audits confins", 163 letters).
  Pins (FT4s's pin family present in S2, every occurrence, never released): 22 'de' (3), 66 'r' (3), 581 'au' (1).
- **S3** = groups 140..170 (31 groups) <-> slip words 79..93 ("de faire de brescia ... sa residence", 75 letters).
  Pins: 22 'de' (2), 66 'r' (1). (279, 501 absent / anchor; 581 absent.)
- Controls per segment: seed 3, n 40, (s) slip words shuffled / real groups; (g) group order shuffled / real slip; pins move with
  their tokens; unresolved counted E = 1 (high).
- Gate per segment (FT4l/FT4r/FT4s/FT4t unchanged): PASS iff E_real = 1 AND each control's E=1 share <= 0.05 (<= 2 of 40).
  E_real = 1 with a share > 0.05: NON-INFORMATIVE. E_real = 0: FAIL (a proof under these pins and the slip expansion -- the pins or
  the pairing disagree beyond one edit). Unresolved real: NOT SCORED.
- Sizing on UNREGISTERED draws only (seed 99, (g)): S2 E 0 in 1.4 s, S3 E 0 in 0.6 s. Run order: REAL S2, REAL S3; controls (s), (g)
  for each segment with E_real = 1, serially (FT4t: four concurrent Pool(4) runs caused unresolved draws). Box 13:19-13:59 UTC, stop
  line 13:51; this step's own stop line 13:40 (step 2 needs the rest); a control short of n 40 is NOT SCORED with its count.

Decisive outcome and what it licenses:
- A segment PASS is a second independent witness (beyond f.206, and beyond f.216v for 22/66) for each code pinned in it: 22, 66, 581
  (S2) / 22, 66 (S3). Logged in NOTES; key.tsv may gain a "2nd witness f.266r Sx (FT4u gate PASS)" note on those rows only; no value,
  no grade moves (they are already C). A VERIFY flag line for a separate verifier. Never a status change.
- NON-INFORMATIVE or FAIL: no witness; a FAIL is logged as a pin/pairing conflict to look at (rule 4), no key edit.

Registered secondary readout (consistency of M codes; only on a segment that PASSes; no controls, so it licenses no grade change):
for every key.tsv M code present in that segment whose value has no '|', one real run with that M value pinned in addition to the
segment's C pins. E 1 = "consistent on f.266r Sx"; E 0 = "proved inconsistent with one edit under the C pins" (a rule-4 dispute noted
against the M value, no key edit); unresolved = not scored. S2 candidates: 121 ons, 188 lar, 834 kowitz, 344 mee, 303 fa, 444 en, 24 in,
534 ches, 347 con. S3: 121 ons, 10 a, 344 mee, 40 pro, 548 ve, 834 kowitz, 24 in. (Seen before this PREREG by a count of value
substrings in the segment text, no solver run: several values do not occur as substrings at all -- e.g. 834 'kowitz', 534 'ches' in S2 --
so those E 0 outcomes are expected by construction and are reported as such, not as discoveries.)
- Key rule: no value or grade moves in key.tsv this step.
