# PREREG addendum LVN-L04 (15 Oct 2026, 16:4x UTC by date -u, account 4, LANE DEFAULT-A4-1634-15) -- written before any blind read

Step: LVN-L05W's named next: the p1_L04 head of 4610 (images/04610_p1.jpg; eye-read "124, 127" by LVN-3R/LVN-4610U/LVN-4610H; not in
ciphertext_4610.tsv, which starts p1_L04 at 145) gets its own blind look by the LVN-L05W design. Disk only, requests 0.
Crops: `lvnl05/cut_w.py SCRATCH l04` (boxes in page pixels, placed by this session's own non-blind eye; 5x Lanczos, grey; scratch only,
no image in git): l04_head (170,170,285,212) = 124 | 127 | edge of 145; l04_ctl1 (507,170,582,212) = 71 | 73; l04_ctl2 (549,170,612,212)
= 73 | 36(clipped). Controls are same-line H tokens: p1_L04/6 71 H and p1_L04/7 73 H (numerals; the =tout word is not used, LVN-L05W).

Readers: two Sonnet subagent calls, each shown exactly two crops labelled X and Y and nothing else (no committed value, alternative,
decode, key or this file): call r1 X=l04_head, Y=l04_ctl1; call r2 X=l04_ctl2, Y=l04_head. Each reader reads every token left to right,
digit by digit, with an alternative where unsure, and marks a token clipped at either edge. Scored tokens by position after dropping any
token the reader marks clipped at the LEFT edge: l04_head tokens 1-2; l04_ctl1 token 1 (71); l04_ctl2 token 1 (73).

Gate: both controls (r1's 71, r2's 73) read exactly as committed (2/2). Else nothing is applied, the head stays untranscribed, logged.
Rulings (gate passed): a code read the same by both readers and equal to the eye reading (124 / 127) -> inserted at M through
`lvn10/inserts_lvneye.tsv` (line p1_L04, before_pre_pos 1), in order; a code where either reader differs from the eye -> inserted as `?`
(U) with both blind readings in the note. Value: key.tsv has no 124 or 127 row, so both decode U whatever the grade (codes > 120,
VIV-KEYSTONE). 145 (p1_L04/1 M) is not scored here; any blind reading of it goes to NOTES only.
Apply: lvn10/apply.py, then regenerate and --check every derived file (decode_key.py all decode*.json, lvn10/apply.py, settle.py,
axnames/revisions.py), counts before/after, AUDIT.md carried as LVN-L05W did. Stop: 80% of cap (2.0 of 2.5) or box (17:24 UTC).
