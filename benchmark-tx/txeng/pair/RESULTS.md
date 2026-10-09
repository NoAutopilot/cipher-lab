# TXE-C: thin-stroke targeted pair re-read (LANE TX-ENGINEER round 2, instrument C; 9 Oct 2026, 07:15-07:2x UTC by date -u)

Verdict: **FAIL on dev_tune** -- passJ_pair_dev_tune vs L_dev_tune: fixed 1, broken 1, sign test p = 1.0000 (gate fixed >
broken, p < 0.01, PREREG-txeng-2 amendment). 28 positions selected; err_true 0.041 (14/343) for both L and J. eval_heldout
NOT run (PREREG: a dev FAIL is not run on eval; its 51 selected positions are written, unread).

## Tool and rules (fixed before any read)
`tools/tx_pair_reread.py` select / build / resolve; test `tools/tests/test_tx_pair_reread.py` (synthetic hairline / mid /
blob page: select returns the hairline only, build writes one sheet + key, resolve applies A/B and keeps L on neither/?).
- Box -> position: label-blind width DP (costs of atlas/no87_map.py), 1:1 matches only (dev 333 of 354 positions mapped).
- Thin: `tx_taxonomy.erosion_share` on the harvest page image, below the page's lower-tercile cut over all its boxes.
- Partner rule: a listed pair is usable only when both codes have secure exemplar tiles (atlas/sheet_truth/sheet.tsv,
  non-no.87 leaves); a sign in several usable pairs gets the partner with the highest pair count in
  harvest/confusion_1572.tsv, ties by PREREG list order (so T76 -> T86, T45 -> T76).
- Unusable (a code without secure tiles): T76/T66, T64/T95, T64/T51, T92/T95, T92/T98, T83/T24, T13/T64.
- Change made before any reader call, stated here: the brief's cluster-label fallback for codes without secure tiles was
  built once on dev and inspected by the worker: it gave dot marks for T24 (cluster 84) and a mixed cluster (1/3 clerk
  votes) for T64 (cluster 8). It is off by default (`--cluster-fallback` keeps it), which removed the T24/T64/T13 pairs
  (dev selected 36 -> 28).
- Rendering: one zoom for every tile (`--zoom 1.6`): no.87 boxes run 40-110 native px, not the brief's ~40, so a literal 4x
  made 18,000 px sheets; 1.6 renders a tall sign at about 160 px. Sheets of 14 rows (2 sheets, about 2000 x 4500 px).

Counts (select): dev_tune boxes 333, thin 73, selected 28 (T18/T98 8, T45/T76 10, T53/T90 3, T60/T86 2, T76/T86 5);
eval_heldout boxes 381, thin 146, selected 51 (T18/T98 3, T36/T50 2, T45/T76 28, T53/T90 8, T60/T86 5, T76/T86 5).

## Reader (2 Opus 5.5 subagent calls, dev only; raw reads committed and pushed in 6d4454eec before scoring)
Task text (per sheet NN): "Read only benchmark-tx/txeng/pair/dev_tune/sheet_NN.png. For each numbered row, does the boxed
sign in the leftmost tile match exemplar row A, row B, or neither? Write benchmark-tx/txeng/pair/dev_tune/reads_NN.tsv: row,
pick (A/B/neither/?), conf (H/M/L), feature seen. Do not open any other file." (+ format line: TSV header, Write tool, no commit.)

Picks per pair (resolve): T18/T98 L kept 6, partner 1, neither 1; T45/T76 L kept 10; T53/T90 L kept 3; T60/T86 partner 1,
neither 1; T76/T86 L kept 5. Total 24 kept L by pick, 2 changed L, 2 neither.

## Score (tx_bench, dev)
```
birago1572-no87 [eval] err_true 0.041 (14/343) 95% 0.025-0.067 | wrong 14 deleted 0 inserted 0 | excluded 11 | lines missing 17
paired passJ_pair_dev_tune.tsv vs labels_dev_tune.tsv on birago1572-no87: 343 common scored signs; base wrong 14, output wrong 14; fixed 1, broken 1; sign test p = 1.0000
```
## Movement (tools/tx_taxonomy.py, L vs J, taxonomy_dev_tune.tsv/.md; read after the reads were pushed)
- fixed: f178v_L06.18 d, L T98 -> J T18 (thin, class 3, pair T18/T98).
- broken: f178v_L04.25 e, L T86 -> J T60 (thin, pair T60/T86).
- Ceiling: the selection held only 4 of L's 14 dev errors (L06.18, L10.31, L11.05, L11.29); at two of them the truth is
  outside the pair shown (L10.31 truth T36|T50 read T98, partner T18; L11.29 truth e read T60, partner T86 -- the reader said
  neither). So even a perfect reader could fix at most 3 on dev (L11.05 truth e read T76, shown T86: kept L, missed), and
  3-0 gives p = 0.25: the p < 0.01 dev gate was out of reach at this selection size. Most of L's dev errors are mid/heavy
  (8 of 14), or thin in pairs this list does not hold or cannot show (T64 and T96 reads).
- One reader note: sheet 2 row 11 showed an infinity-shaped sign against two hash rows (L T60/T86) -- a box -> position
  slip of the width DP, harmless here (neither keeps L) but a source of wrong rows.

Calls: 2 Opus vision (dev). Cost: not visible from inside the worker session; the lane reads get_session.
Follow-up (one line): a pair list built from the unit's own L-error confusions (T76 -> e, T60 -> e) and secure tiles for
T64/T24/T66/T92 would be needed before this instrument could reach the gate; not attempted (brief).
