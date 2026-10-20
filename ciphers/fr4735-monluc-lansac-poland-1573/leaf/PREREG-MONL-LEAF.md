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
