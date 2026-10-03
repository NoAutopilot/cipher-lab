# FT4t pre-registration (account-4, 3 Oct 2026, written 13:0x UTC by the clock, pushed before any registered score)

The FT4s anchored split (`ft4s_seg.py`, PREREG-FT4s.md) applied to the f.249 numerals / f.250 slip pair. f.249 was scored
before only whole-pair (FT4e strict: infeasible as transcribed; FT4i/FT4q one-edit: E 1 under ti and i, controls 0.80 / >= 0.60,
non-test). Different instrument from those (anchored segment with pins), the same one FT4s resolved on f.266r.

Instrument: `align/ft4t_seg.py` (imports ft4s_seg's solve_pins/E unchanged).
- Anchor rule (FT4s's, fixed before any score): a code with an f.206 C value whose count in the f.249 groups equals the count of
  that value as a whole word in the expanded f.250 slip. Checked over all twelve C codes: only 628 'hongrie' (1 group, index 38;
  1 word, index 26) and 279 'plus' (group 101; word 64) qualify. 501 and 581 are absent; 22 'de' is 5 groups vs 6 words; 208 'se'
  4 vs 2. 722 (index 76, "347 722 476", slip "continuera") lies between the two anchors.
- Segment S = groups 39..100 (62 groups; f.213 is 84, f.266r S1 75) and slip words 27..63 ("de la maniere ... derober le",
  193 letters); both anchor tokens excluded, as FT4s excluded 501/et. Transcription disputes 33|35 and 833|835 fall in S as single
  unrepeated codes (first reading used, free groups either way).
- Pins in S (FT4s's pin family: f.206 repetition-consistent C values present in S, every occurrence, never released):
  22 'de' (S-group 40 = f.249 group 79), 66 'r' (49, 62), and 722 = X. Not pinned: 208 'se', 781 'e' (pooled-gate C, not in FT4s's
  pin family). Model, E (decomposition, sublimit 10 s, Pool(4), early exit), MAXLEN 12, <= 1 edit: ft4s_seg unchanged.
- Run with X = 'ti' and X = 'i'; nothing else differs.
- Controls per X: seed 3, n 40, (s) S slip words shuffled / S groups; (g) S group order shuffled / S slip; pins move with tokens;
  unresolved counted E = 1 (high).
- Gate per X (FT4l/FT4r/FT4s unchanged): PASS iff E_real(X) = 1 AND each control's E=1 share <= 0.05 (<= 2 of 40).
  E_real = 1 with a share > 0.05: NON-INFORMATIVE. E_real(X) = 0: FAIL for X under the pinned one-edit model on S (a proof,
  conditional on anchors, pins, slip expansion). Unresolved: NOT SCORED.
- Sizing on an UNREGISTERED draw only (seed 99, (g), X = ti): resolved, E 0, 1.2 s. Run order: REAL ti, REAL i; then (s), (g)
  n 40 for each X with E_real(X) = 1. Box 13:00-13:40 UTC, stop line 13:32; a control short of n 40 is NOT SCORED with its count.

Outcomes for 722 (f.206 ti twice, C; f.213 minus group 73 fits only with i; f.266r S1 both fit, O3):
- O1 E(i) = 1, E(ti) = 0: S sides with f.213. If i also PASSes: a second independent pair supports 722 = i in this context;
  rule-4 data conflict with witnesses (f.206 ti; f.213, f.249 i), a VERIFY flag line for a separate verifier, no majority
  settlement, key.tsv unchanged this step.
- O2 E(ti) = 1, E(i) = 0: S sides with f.206 (f.213's i isolated). Same VERIFY note if the ti controls PASS.
- O3 both 1: S does not decide 722; then name whether f.266r S2/S3 can (they hold no 722: FT4q counted one more 722 on f.266r --
  checked post hoc by index only, reported, no score).
- O4 both 0: S needs >= 2 edits under either value with these pins; no 722 information.
- A decisive outcome is O1 or O2 with the deciding value's gate PASS AND the other value's E_real = 0 (a proof). Only then a
  VERIFY flag; never a status change or a key.tsv edit by this worker.
