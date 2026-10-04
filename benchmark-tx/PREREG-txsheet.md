# PREREG TX-SHEET (4 Oct 2026, 14:3x UTC, account-3 worker; pushed before any read pass)

Research #4 of research/TRANSCRIPTION-PRACTICE-2026-10-04.md: a per-hand exemplar sheet (the palaeographer's alphabet)
replaces the canonical 51-cell sign sheet in one blind line-read pass of the eval item birago1572-no87.

## Sheet (built, frozen at this commit)

- Tool: `tools/glyph_atlas.py atlas --from-truth` (new option, this job). Command (repo root):
  `python3 tools/glyph_atlas.py atlas --out A --from-truth A/secure_tokens.tsv --per 6 --spread --exclude-leaf f178r
  --exclude-leaf f178v --exclude-leaf f179r --codes @A/sheet_truth/codes.txt --canonical
  ciphers/nevers-birago-fr3251-1572/harvest/sign_sheet_blind_1572.png --sheet-dir A/sheet_truth --sheet-prefix sheet`
  (A = ciphers/nevers-birago-fr3251-1572/atlas; defaults --trim 0.2 --cell 96 --rows-per-sheet 13 --min-secure 2).
- Output: `A/sheet_truth/sheet_01..04.png` (13+13+13+12 rows), `A/sheet_truth/sheet.tsv` (per code: secure count, shown,
  exemplar box ids). Each row: code, the printed (canonical) shape, then up to 6 tiles of the hand.
- Source rule (`A/secure_tokens.py`, its header): no no.87 leaf is read. No C/H-graded sign positions exist in this key
  family outside no.87 (the clerk sheet is no.87's), so every exemplar is an **S position where independent instruments
  agree**: blind readers A and B agree on the sign (passC_agreement status `agree`, neither conf L) AND the family atlas's
  kNN code for the box (classify with every no.87 box held out of the vote) is the same sign; box <-> token match by an LCS
  over each page's reading order on equal codes, kept only inside a run of >= 2 consecutive matches. 636 secure tiles on
  11 leaves (f139v 26, f144r 18, f152r 48, f162r 9, f174r 49, f174v 163, f174vB 146, f175v 34, f184r 86, f184v 45, f185r 12).
- Disclosed limit: the atlas's cluster names were partly set on no.87 tune lines (f178v L01-12, atlas/README.md). The atlas
  here only filters tiles the two blind readers already agree on; it never supplies a label alone. No no.87 tile is on the
  sheet.
- Per-sign secure counts (a code under 2 keeps the printed shape only): T10 0, T11 0, T13 1, T15 0, T17 1, T18 5, T19 34,
  T24 0, T25 35, T26 5, T27 7, T29 3, T33 30, T36 20, T37 49, T38 0, T42 0, T45 42, T46 0, T49 6, T50 6, T51 0, T52 5,
  T53 43, T54 4, T55 32, T56 0, T57 5, T58 31, T60 43, T63 13, T64 0, T65 9, T66 0, T70 13, T76 18, T78 0, T80 17, T81 6,
  T83 11, T84 0, T85 48, T86 24, T88 0, T89 9, T90 8, T92 0, T95 1, T96 32, T97 2, T98 18. 33 codes with hand rows,
  18 print-only (incl. T64, T92: two of no.87's error sources keep only the printed shape).
- Settings chosen before any pass, by eye on the sheet only: --per 6 --spread (brief), --trim 0.2 added after the first
  render showed a phi-shaped (mis-aligned) tile in the T86 row. **No tuning on the dev item dint-f128-print**: the Dinteville
  1592 hand is a different key family with no secure-position source of its own on disk; tuning there would need its own
  truth, outside this cap. So the eval pass uses the a-priori settings above, once.

## Pass (one, blind)

- Model Sonnet 5 (`claude-sonnet-5`), the pass-A brief `ciphers/nevers-birago-fr3251-1572/harvest/blind_pass_brief_1572.md`
  with only the sheet references changed (`benchmark-tx/txsheet/prompt.md`, diff = sheet wording), the same line crops
  (harvest/f178r, f178v, f179r `*_L??_s?.jpg`), the same call grouping as pass A: call 1 f.178r + f.179r (18 crops),
  call 2 f.178v L01-L10 (30 crops), call 3 f.178v L11-L23 (39 crops). 3 subagent calls, no reconciliation.
- Output: `benchmark-tx/txsheet/passE_{f178r,f179r,f178v_L01-10,f178v_L11-23}.tsv`, normalised to
  `benchmark-tx/outputs/birago1572-no87/passE_sheet.tsv` (line, pos, sign).

## Gate (all three, eval item birago1572-no87, 803 scored signs)

1. `tools/tx_bench.py passE_sheet.tsv --item birago1572-no87`: err_true **below 0.069** (pass A).
2. `tools/tx_bench.py passE_sheet.tsv --paired passA.tsv`: **fixed > broken** vs pass A.
3. In passE's top-confusions list, **d<-T98 below 7 and s<-T50 below 7** (pass A: 7 and 7).
Pass = adopt for line reads of this family (LESSONS.md line). Fail on any = not adopted; the row says which.
A missing or truncated call output (a line with no rows) is reported as such and scored as is (lines missing count).

## Cost

Per-pass estimate: about USD 1.2-1.5 per Sonnet call with 18-39 crops plus 4 sheet images (AX-COMP2 rate 1.46/call),
3 calls = USD 3.6-4.5; cost per 100 signs reported = job cost / 8.53 (853 signs) and the read-pass share alone.
