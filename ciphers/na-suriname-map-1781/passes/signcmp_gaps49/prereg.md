# GAPS49-na-suriname-map-1781 (account-4), 3 Oct 2026 -- pre-registration (pushed before the vision call)

Question. The period key (Nieuw Secreet Alphabet, NA 1.05.03 inv. 86 scan 0003) has two y-like signs: GAPS14's passes read
the M row as "y" (pass B: "with small loop/mark above") and the N row as "ij (y with dots)". 2077's reader code [u-dots]
(17 tokens) carries two dots above (GAPS45: dots 17/17) and is keyed n. GAPS45 read the n->m context (16/17 where Dutch wants
m) as the encipherer's use of the N sign. This step asks only: on the key sheet itself, which row's y carries the dots --
M, N, both or neither -- on each of the two pages (left alphabet, right reverse table)?

Crops (tools/iiif_lines.py --image, regions in native px; row letters and the N row's l/h lie outside every region):
  a left  95,1770,150,190  M row first sign      | b left 85,1950,115,170 N row first sign
  c right 130,1250,100,150 M row sign            | d right 128,1375,72,140 N row middle sign (between l and h)
  e left  405,440,75,100   A row [x-dots] (control: dots)
  f left  85,1560,115,120  K row b (control: no mark) | g right 55,1490,60,100 O row k (control: no mark)
Shuffled to T1-T7 (seed 20261003); mapping in blind_key.json, not shown to the reader. The reader is told only "handwritten
signs cut from an 18th-century sheet", no letters, rows, values or hypothesis. One blind Opus 5.5 vision call.

Per tile the reader reports: the main sign's shape; mark directly above its body: none / dots (count) / loop / stroke that
belongs to a sign in the line above / unclear; confidence 0-1. Then which tiles show the same sign (grouping).

Gate (scored first by apply.py): T(e) reported dots; T(f) and T(g) reported none (a stroke from the line above counts as
none). Fail -> "non-test (mark-reading gate failed)", nothing changes.

Outcomes (a page's M or N tile counts as dotted only at dots with confidence >= 0.6):
  A  N dotted, M not, on both pages -> key stands (N = dotted y, M = plain y). [u-dots] = n stays H; the n->m is the
     encipherer's use of the N sign (GAPS45), now with the sheet's own row labels confirmed. No value change.
  B  M dotted, N not, on both pages -> our M/N row assignment is swapped: [u-dots] -> m at H (17 tokens), via
     key_period_codes_nieuw.tsv, decode_key --check, GAPS23 gate re-run unchanged, AUDIT item 4 propagation note.
  C  both M and N dotted on a page AND the reader groups that page's M and N tiles as the same sign -> the sheet does not
     separate M from N for this sign: [u-dots] -> two-valued n|m at M (17 tokens), applied as in B.
  D  both dotted but grouped as different signs, or the two pages disagree, or anything else -> no value change; logged
     with the per-page result; the sheet's dots alone do not settle [u-dots].
Context (16/17 want m) is not used to choose an outcome. Rule 10: report only.
