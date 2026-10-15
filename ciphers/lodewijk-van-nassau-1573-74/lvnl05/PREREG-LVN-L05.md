# PREREG LVN-L05 (15 Oct 2026, 15:1x UTC by date -u, account 4, LANE DEFAULT-A4-1441-15) -- written before any blind read

Step: LVN-4610U's named next: (1) an insert path in lvn10/apply.py and the p1_L05 head "81, 125" entered at M after a second blind look;
(2) a second blind reader on LVN-4610U's five found-on-the-way rows. Disk only (images/04610_p1.jpg and the committed 150-dpi line crops).
Crops: lvnl05/cut.py (boxes in page/line-crop pixels, 5x Lanczos, grey; scratch only, no image in git). Boxes were placed by this session's
own (not blind) eye with a pixel ruler; the readers are not told any committed value, alternative or decode.

Targets (fixed) and their controls (H tokens on the same line, value known to this session, not to the reader):
| crop | row | committed | LVN-4610U alternative | control crop | control row (H) |
|---|---|---|---|---|---|
| h_head | p1_L05 head (untranscribed) | -- | 81, 125 (one eye) | h_ctl | p1_L05/4 28 |
| t80 | p1_L05/3 | 80 H | 89 or 88 | t80_ctl | p1_L05/2 8 |
| t25 | p2_L22/9 | 25 H | 26 | t25_ctl | p2_L22/8 82 |
| t35 | p2_L30/2 | 35 H | 36 | t35_ctl | p2_L30/3 31 |
| t141 | p1_L32/1 | 141 H | 241 | t141_ctl | p1_L32/5 21 |
| tfut | p1_L04/3 | =fut M (B:=este) | =este | tfut_ctl | p1_L04/4 =tout |

Readers: one Sonnet subagent call per target line (two crops each: target and control, labelled X and Y in an order fixed here --
h, t25, t141 target=X; t80, t35, tfut target=Y), each asked to read every digit (or the word) in each crop, digit by digit, with an
alternative where unsure. A reader sees nothing else. Deviation from "one crop per call": a control rides in the same call so the control
measures the same reader.

Gate: >= 5 of 6 controls read exactly as committed; else nothing is applied and every target is listed as undecided, no grade change.

Rulings (the blind reader's first reading, compared with the committed value and LVN-4610U's eye):
- head: blind reads 81 and 125 -> insert both at M (two eyes, one blind, agree). A code read differently -> inserted as `?` (U) with both
  readings in alt. 125 has no key.tsv value; not valued here (VIV-KEYSTONE's codes > 120).
- five rows: blind = committed -> kept at its grade (LVN-4610U's doubt recorded in NOTES only); blind = LVN-4610U's alternative ->
  changed to the alternative, grade M; blind = neither -> value kept, H -> M (undecided). =fut: blind reads "este" -> =este M; else kept M.
Apply: lvn10/corrections_lvneye.tsv (tag LVN-L05) and a new lvn10/inserts_lvneye.tsv read by lvn10/apply.py (insert before a pre_pos);
then decode_key.py --check on every decode*.json, the folder chain LVN-4610U ran, counts before/after, AUDIT.md carried (rule 10).
p1_L04 head "124, 127" is not in this job (named next). Stop: 80% of cap (2.4) or box (15:53 UTC).
