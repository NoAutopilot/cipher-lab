# PREREG LVN-4610U (15 Oct 2026, 14:5x UTC by date -u, account 4, LANE DEFAULT-A4-1441-15) -- written before any image is looked at

Step: LVN-4610H's named next "eye on the 9 undecided non-2 rows with a per-token zoom beside same-line exemplars".
Targets (fixed): p1_L28/5 78, p1_L32/2 128, p2_L06/17 81, p2_L10/20 128, p2_L22/19 81, p2_L30/6 28, p2_L34/4 141, p3_L04/3 131, p3_L30/17 118
(LVN-4610H's alternatives: 75, 123, 85, 123, 85, 26, 130/150, 135, 115).
Image: the committed 150-dpi line crops images/04610_<line>.jpg (on disk; no fetch). Zoom: the token region upscaled 4-6x (Lanczos) beside
exemplars of both candidate final digits cut from the same line or the nearest lines on the same page (scratch only, no image in git).
One Opus eye (this session), no subagent; NOT blind (committed value and alternative both known).
Ruling per target (final digit; first digits only if the alternative names them):
- **kept H**: the final glyph matches the committed digit's same-page exemplars and not the alternative's.
- **changed (-> M)**: the final glyph matches the alternative's exemplars and not the committed digit's; the row gets the alternative value, grade M.
- **undecided (H -> M)**: neither clearly; value left, grade lowered to M (a second eye could not confirm the committed digit; no H kept on doubt).
Control: before ruling, the eye names the final digit of 6 non-target H tokens on the same lines whose committed final digit is 5, 3, 1, 8, 6 or 0
(chosen mechanically: the first such H tokens on the target lines); >= 5 of 6 must match the committed digit, else nothing applied, all 9 listed undecided
with no grade change.
Apply: via lvn10/corrections_lvneye.tsv (tagged LVN-4610U) + lvn10/apply.py when the mechanism takes grade-only rows; else listed for the lane.
Then decode_key.py --check on every decode*.json, counts before/after, carried into AUDIT.md (rule 10). Codes >120 in key.tsv not edited.
Second unit (p1_L05 head "81, 125") only if >= 40% cap left after the first.
Stop: 80% of cap (2.4) or box (15:40 UTC).
