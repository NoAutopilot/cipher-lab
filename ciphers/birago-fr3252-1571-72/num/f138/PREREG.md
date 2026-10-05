# RUN6-BIR138 pre-registration (5 Oct 2026, before any target statistic)

Question: is fr.3251 no.71 (f.138, 7 Feb 1572) a third letter in the Nov 1571 numerical system (f.119 + f.100r) or in the 1572 key?
Target cipher: NEVBIR-138 located it at the foot of f.139v (5 lines, ../../../nevers-birago-fr3251-1572/harvest/f139v/, crops on disk).
Note found before this PREREG (context, not a statistic): NEVBIR-138 already transcribed those 5 lines against the 1572 symbol sheet
(161 signs, 21 off-sheet) and the 1572 key ranked 1/201 (z 3.60; verifier N3). A sheet-bound transcription cannot show digits, so the
shape question is put to a blind reader without a sheet.

S1 (shape, blind): one Sonnet subagent call, no sheet, no key, no folio names. Three montages, s1 crop of lines L02-L06 each,
shuffled labels: f.139v (target), f.100r L02-L06 (positive control: Nov 1571 numerical, 565 digits), f.178v L02-L06 (negative control:
no.87, 1572 symbol key). Reader returns per montage: fraction of signs that are Arabic numerals 0-9 (0-1), and presence (y/n) of dots over
figures, a divide-like sign, inline m/n/h/f letters.
Gate: control discriminates iff f.100r >= 0.8 and f.178v <= 0.3. If it does not, S1 is a non-test (logged as such).
  - target >= 0.8 -> numerical-system candidate; S2 is licensed (next job; needs a digit transcription).
  - target <= 0.3 -> not in the numerical system by shape; S2 (6-mer overlap) has no digit stream and is not applicable.
  - 0.3 < target < 0.8 -> mixed, undecided; next step named.
S2 (6-mer overlap vs f.100r+f.119, null = shuffled target, matched control = a digit cipher of another key on disk truncated to the
target's N): run ONLY if S1 says numerical candidate. Not run in this job otherwise.
Vision budget: 1 subagent call (3 images) + at most 1 eye check by this worker. Cap USD 2.
