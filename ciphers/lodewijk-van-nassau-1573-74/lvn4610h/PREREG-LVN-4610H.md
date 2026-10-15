# PREREG LVN-4610H (15 Oct 2026, 13:1x UTC by date -u, account 4, LANE DEFAULT-A4-1236-15) -- written before any image is looked at

Step: the NOTES.md Verdict's named next "the rest of 4610's H tokens ending in 1 or 8" (the flat-foot hooked 2 read as 1 or 8, LVN-EYE / LVN-K15).
Targets (mechanical, `lvn4610h/targets.py`): every row of ciphertext_4610.tsv with confidence H, a pure-numeral sign ending in 1 or 8, outside
p1_L04 and p1_L09 (LVN-K15 ruled those): 279 rows (p1 92, p2 109, p3 78) on 85 transcription lines.
Image: WVO 04610.pdf (resources.huygens.knaw.nl, one request, 3,689,372 bytes), `pdftoppm -png -r 300`, pages 1-3 (sha1 0466fea481e7, c997f0cb8a35, a41b5df838e4 -- p3 = the R14-LVN10C render). Crops: the line boxes of
images/manifest.json (150-dpi box x2, padded 20 px), each line cut in two overlapping halves at ~1.2x, four lines to a sheet, the line's
transcription printed under it with targets bracketed (`lvn4610h/sheets.py`; scratch only, no image in git). One Opus eye (this session), no
subagent; NOT blind (the look knows the committed value).
Ruling per target (the final glyph only): **kept** (the eye sees the 1 or 8 committed); **changed** to the value with a final 2 when the final
glyph is the flat-foot hooked 2 (wide flat base, hook at the head) -- new grade M (LVN-EYE convention, no grade raised); **undecided** (value
and grade left, listed) when the eye cannot choose or cannot find the token on the strip (segmentation/line mismatch, notably p3 where the
transcription lines do not match the physical lines).
Positive control (gate): the H rows ending in 2 on the same sheets are read too; >= 90% of them must show the flat-foot 2 the eye uses as the
exemplar, and the eye must not call any of the LVN-K15 kept exemplar rows' 1/8 a 2 -- else nothing applied, all targets undecided.
Apply: changed rows appended to `lvn10/corrections_lvneye.tsv` (note tagged LVN-4610H, keyed by pre_pos), applied by `lvn10/apply.py`; then
`decode_key.py --check` on every decode*.json, the settle/apply --check chain, counts before/after, grade changes into AUDIT.md (rule 10).
Stop rule: 80% of cap (2.4) or box (14:00 UTC); pages in order p1, p2, p3; a page not reached is a listed remaining gap.
