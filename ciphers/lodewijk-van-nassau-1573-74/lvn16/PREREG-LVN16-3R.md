# LVN16-3R pre-registration (13 Oct 2026, written and pushed before the blind read is opened)

Job: LVN16-3R (LANE DEFAULT-A2-0710, account 2). NOTES.md Remaining gaps item 3, "4616 remainder ... next a per-token
zoomed third read".

Material: WVO 4616 p1 at 300 dpi, re-fetched once 13 Oct 2026 07:2x UTC (resources.huygens.knaw.nl, HTTP 200), rendered
`pdftoppm -png -r 300 -f 1 -l 1`, sha1 4f47b490f28e2cfeebaf5352c34f64af87636148 (identical to R12-LVN16). Line crops by the
logged command `python3 tools/iiif_lines.py --image 04616-1.png --out crops --prefix 04616_p1 --region 380,320,2080,880
--distance 45 --prominence 20 --top-margin 12 --bottom-margin 12 --debug` (13 lines, crop Lk = p1_L(k+4)). Per-token crops by
`lvn16/crops3r.py` from `lvn16/tok3r.tsv` (line, position, centre x, half-width in line-crop px; centres placed from the ink
profile and checked by eye on a contact sheet before this file): a tight crop (token only, 3x) and a context crop (token plus
about one token each side, 2x, a blue wedge above the token). Committed as `lvn16/crops3r/Tnn_{tight,ctx}.jpg`.

Rows (lvn16/key3r.tsv, shuffled, seed 20261013): 21 targets = every non-H numeral row of the cipher block (16 M) plus the 5
kept slash groups (22/112, 33/5, 25/81, 27/16, 92/2); 10 controls = H rows of the same page (p1_L06/3 37, L06/7 116, L06/11 71,
L08/2 64, L08/13 118, L10/6 112, L11/16 78, L13/9 40, L15/8 118, L17/7 120). The brief said 20 targets; the folder now holds
21 (R13-LVNFIX added M rows after the brief's count was written), all 21 are read.

Reader: one blind Sonnet subagent call, all 31 rows, shown only the crops and a candidate list per row: for targets the
values R12-LVN16 already logged (sign, 150-dpi pass B, A3, B3, edge marks stripped), for controls the H value plus one
look-alike fixed in key3r.tsv before the read; candidates unlabelled and shuffled; the reader may answer a value not listed,
or '?'. Never shown the key, the role, or which pass gave which value.

Control gate: >= 8/10 controls read exactly as the H value. Below gate: nothing changes (non-test), logged only.

Settle rule (gate passed only), per target:
- rows R13-LVNFIX/R12-LVNV set by a verifier's eye against A3 == B3 (p1_L07/8 13, p1_L16/2 20, p1_L16/4 85, p1_L16/19 81):
  confidence to H only if the read equals the current sign exactly (no '?'); if it equals A3 == B3 instead, the row stays M
  and the conflict is logged; never changes the sign.
- other M rows: settle when the read equals A3 or B3 of R12-LVN16 exactly (edge marks '?', '~' stripped from A3/B3 before the
  comparison), no '?' in the read; the sign becomes that value; confidence H only when every part is a key_full code,
  else M kept with the new sign. A read matching neither stays M, logged.
- slash groups: split into codes only when the read gives the same slash split as A3 or B3 and every part is a key_full code;
  the value becomes that split; otherwise kept whole.
Recount: reading_4616_full_tokens.tsv C/H/M/U before and after; NOTES.md "Read so far" line recomputed.
