# FT4s pre-registration (account-4, 3 Oct 2026, written 12:45 UTC by the clock, pushed before any registered score)

Second attempt at the f.266r/f.265r pair (FT4r was the first: whole-pair one-edit gate, real E unresolved for both 722
values). Rule 3's third-attempt clause: this is a different instrument (anchored split with f.206 C pins), not a longer
timeout; if it too comes back unresolved, the next step is not a third tuning of the same pair gate.

Instrument: `align/ft4s_seg.py`.
- Anchor rule (fixed before any score): cut at a code with an f.206 C value whose occurrence count in the f.266r groups equals
  the count of that value as a whole word in the expanded f.265r slip, so the k-th occurrence anchors to the k-th word. Of the
  f.206 C codes present in f.266r (22 de x7, 66 r x6, 581 au x2, 501 et x2), only 501 'et' qualifies (2 groups: 75, 139; 2 whole
  words 'et': word 45 "Bressan et le Bergamasc", word 78 "confins et de faire").
- Segment S1 = groups 0..74 (75 groups; f.213 is 84) and the slip words before word 45 (251 letters, ending "...couvrir le
  Bressan"). 722 (group 49, "180 722 180") lies in S1. Segments S2 (groups 76..138) and S3 (140..170) are not scored this step.
- Pins in S1, every occurrence, never released: 22 'de' (groups 2, 28), 66 'r' (56, 58), 581 'au' (30), and 722 = X.
  Model: the FT4l/FT4r one-edit CP-SAT (MAXLEN 12, every repeated code one identical chunk, free groups 1..12 letters, <= 1 edit,
  W release / D dropped group; a pinned occurrence is never released), E by decomposition per edit class + the no-edit model,
  sublimit 10 s, Pool(4), early exit on a fit. E in {1, 0, unresolved}.
- Run with X = 'ti' and X = 'i'; nothing else differs.
- Controls per X (can vary on E's axis: E depends on the order of both sides): seed 3, n 40, (s) S1 slip words shuffled / S1
  groups; (g) S1 group order shuffled / S1 slip; pins move with their tokens; unresolved counted E = 1 (high).
- Gate per X (unchanged from FT4l/FT4r): PASS iff E_real(X) = 1 AND each control's E=1 share <= 0.05 (<= 2 of 40).
  E_real = 1 with a share > 0.05: NON-INFORMATIVE. E_real(X) = 0: every class proved infeasible -> FAIL for X under the pinned
  one-edit model on S1 (a proof, not a score; conditional on the anchor, the pins and the slip expansion). Unresolved: NOT SCORED.
- Sizing before this commit on an UNREGISTERED draw only (seed 99, (g), X = ti): resolved, E 0, 1.9 s. So all 160 control draws
  fit the box. Run order: REAL ti, REAL i; then (s) and (g) n 40 for each X with E_real(X) = 1. Box 12:43-13:23 UTC, stop line
  13:15; a control not completed to n 40 is NOT SCORED with its draw count.

Outcomes for 722 (f.206 needs ti twice, C; f.213 minus group 73 fits only with i; f.249 cannot decide):
- O1 E(i) = 1, E(ti) = 0: S1 sides with f.213. If i also PASSes its controls: an independent pair supports 722 = i in this
  context; logged as a rule-4 data conflict with witnesses (f.206 ti; f.213, f.266r i), a 'reading ready'/VERIFY flag for a separate
  verifier, no majority settlement, nothing moves in key.tsv this step.
- O2 E(ti) = 1, E(i) = 0: S1 sides with f.206; f.213's i is isolated. Same verifier note if the ti controls PASS.
- O3 both 1: S1 does not decide 722 at this model's resolution (a PASS on both would still license the S1 pairing, not a value).
- O4 both 0: S1 needs >= 2 edits under either value with these pins (or the anchor/expansion is off); no 722 information.
- Any unresolved real: not scored for that value; with FT4r this is the second instrument to fail to resolve on this pair, and
  the next step names new material or a different instrument, not a longer timeout.
- Key rule: nothing enters or moves in key.tsv this step; any PASS goes to a separate verifier.
