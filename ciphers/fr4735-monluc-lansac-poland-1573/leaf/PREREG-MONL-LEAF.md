# PREREG MONL-LEAF (20 Oct 2026, written before any candidate leaf was fetched)

Question: which leaf carries the cipher of the clear text after f.140r L26 (c268 ends at L30, MONL-C268C)?
Candidates: c258, c262, c264 (brief), plus at most 3 more chosen from the overviews (c269 = f.138v first if it carries ink).
Per candidate: one overview; if it is cipher in Monluc's Cipher-1 hand, a native crop of its first two lines (tools/iiif_lines.py
or a levelled region as regen_monll26.sh), one blind read by the strongest model (no key, no clear text shown), then
`python3 leaf/leaf_score.py READ.tsv --window f.140r:L27-f.140r:L30` (statistic and control in its docstring: confirm share of keyed
tokens under align_c268.py's DP and key.tsv; control = 200 equal-length windows placed at random in a word-shuffled copy of the whole
clear letter, seed 2710).

Calibration done before any candidate (leaf/power.py, on c268's committed lines against the 4 clear lines where each truly starts):
- brief's gate, margin >= 0.229 (SUP-MONLUC's L26-L30 margin): true window passes 10/30 single lines, 12/29 line pairs; with 15%
  injected sign error 9/29 pairs. Wrong window (f.140r L27-L30): 0/30, 0/29. So the brief's gate has about one-third power at
  this length: a miss on it is not a negative.
- calibrated gate, margin >= 0.10 on two lines: true 26/29 (23/29 at 15% error), wrong window 0/29 (0/29 at 15% error).
Decision rule: margin >= 0.229 = PASS (brief's gate); 0.10 <= margin < 0.229 = LEAD (calibrated gate; needs lines 3-5 before a
leaf is named as the continuation); < 0.10 = no evidence for this window (not a negative for the leaf at 1/3 power, but a negative at the
calibrated gate, 23-26/29 power). Exploratory, not gated: where the same read lands when aligned against the whole clear letter.
Stop on the first PASS (name the leaf, folio, line range; transcribing it is the next job).

## Decision
(Block appended after the run: the PREREG pushed at 1de32897f lacked it; Belief and Would-change restate the pre-run text above.)
Belief: the cipher of the clear text after c268's end starts at f.140r L27 on one of the candidate leaves.
Would change it: a candidate's two-line read reaching margin >= 0.229 (PASS) or >= 0.10 (LEAD) over the p95 of 200 placed shuffled windows against f.140r L27-L30.
Observed: c269 (f.138v) -0.104 (p95 0.414), c264 -0.088, c258 -0.108; no PASS, no LEAD. Exploratory whole-letter alignment (registered as not gated): c269 lands at f.140r L26-L27 (confirm 0.534), c264 at L21-L22 (0.368), c258 at f.141r L08-L10 (0.419). Post hoc, not counted: window L26-L29 c269 margin +0.121 (c264 -0.088, c258 -0.027); longest exact decode run against the clear letter c269 14 letters "sadeursluiauro" (f.140r L27) vs 200 shuffled clears p95 8, max 10, 0/200; c264 6, c258 6 (within null).
Decision: change -- the window premise was wrong (c268 ends mid f.140r L26, not at L27); c269 is a post-hoc lead, to be confirmed by a two-pass transcription of c269 L01-L05 aligned as a continuation of the c268 stream (align_c268.py's design), not by re-scoring these reads.
Lesson: register the window from the alignment's own end point (results_align_c268.json clear_span and the last token's chunk), not from a line count; and a clear window full of [?] words is shorter than its line count implies, which lowers confirm share for a true match.
