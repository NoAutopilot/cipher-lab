# TXE-M results: feature-first reading protocol (LANE TX-ENGINEER, idea M24; 9 Oct 2026, 07:59-08:1x UTC by date -u)

Brief `.claude/briefs/runs/2026-10-09-account4-txe-m.md`; pre-registration `benchmark-tx/txeng/feature/PREREG.md` (545ff8078,
pushed before any read), under `benchmark-tx/PREREG-txeng-2.md` (gate p < 0.01, one eval look).

**Verdict: FAIL on the registered dev gate, and the protocol was not carried out, so this is not a test of feature-first
deciding.** passU vs passA: fixed 9, broken 6, p = 0.61 (gate p < 0.01). Vs L: fixed 3, broken 9, p = 0.15. Eval not run
(eval looks 0). Neither reader wrote features from the ink before choosing the cell. Reader c1 (L01-06) said a script filled
`features` from the brief's cell table for the cell it had already picked; 167 of 167 rows match their cell's table row.
Reader c2 (L07-12) said most of its features were "the chosen cell's own row" and few were written from the ink, yet only 35
of its 185 rows match the table, so what it wrote is neither a copy of the table nor a documented ink read. What was
measured is the ordinary blind read with a feature table and an unenforced instruction in the brief. A real test would
need the features written in a separate call that cannot see the sheet, before a second call names the cell. That is a
different instrument (follow-up line below).

## Score (tx_bench, dev_tune; raw reads committed e635d2c76 (c2) and 38d482c55 (c1) before scoring)
```
birago1572-no87 [eval] err_true 0.061 (21/343) 95% 0.040-0.092 | wrong 19 deleted 1 inserted 1 | excluded 11 | lines missing 17
paired passU_feature_dev_tune.tsv vs passA_dev_tune.tsv on birago1572-no87: 343 common scored signs; base wrong 23, output wrong 20; fixed 9, broken 6; sign test p = 0.6072
paired passU_feature_dev_tune.tsv vs labels_dev_tune.tsv on birago1572-no87: 343 common scored signs; base wrong 14, output wrong 20; fixed 3, broken 9; sign test p = 0.1460
```

## Movement (tools/tx_taxonomy.py, A vs U vs L; taxonomy_dev_tune.tsv/.md, run after the reads were pushed)
- Fixed vs A (9): five are T50->T92 (L01.23, L03.4, L04.4, L05.25, L07.29), the same curled-omega sign TXE-H's pass also moved.
  The other four are L02.19 T83->T81, L06.18 T98->T18, L10.1 T92->T53 and L11.29 T60->T86, the same four non-omega fixes
  TXE-H's hinted pass made. Two blind Opus reads of these crops reach the same alternative read whatever the brief adds.
- Broken vs A (6): L01.12 T86->T60, L01.15 deleted, L01.16 T36->T27, L10.17 T76->T15, L11.6 T92->T50, L12.32 T96->X_NEW
  (line-end edge).
- Class 1 floor unchanged: e<-T76 x2, g<-T42, e<-T36, t<-T90 are wrong in A, U and L alike. U repeats 14 of its 20 errors
  from A (10 with the same sign).

## Feature vocabulary (tools/tx_features.py cells; cell_features.tsv, from the printed sheet only)
| feature | values | measure |
|---|---|---|
| desc | none/short/long | ink below the body band / body height (<0.25, <0.75, more) |
| asc | none/short/long | ink above the body band, same cut points |
| bars | 0/1/2 | rows whose longest ink run > 0.6 x width, grouped (counts flat loop tops too) |
| loops | 0/1/2 | enclosed holes >= 1% of the box |
| dots | 0/1/2+ | small components < 12% of the largest |
| lean | left/upright/right | principal-axis shear, |s| < 0.15 upright |
| tail | none/left/right | lowest 20% of ink rows vs mean x, |offset| < 0.15 width none |
The body band joins the runs of rows whose ink extent is >= 0.45 x width (runs at least half as long as the longest). Known
limits are in PREREG.md (T76 desc none, bar count includes loop tops).

## Self-consistency (tools/tx_features.py consist, >= 2 written features contradicting the chosen cell; consist_dev_c*.tsv)
| call | rows | wrong signs flagged | right signs flagged | note |
|---|---|---|---|---|
| c1 L01-06 | 167 | 0/8 | 0/159 | non-test: features script-filled from the chosen cell |
| c2 L07-12 | 185 | 8/11 (0.73) | 103/174 (0.59) | flags 60% of all signs; precision 8/111 = 0.07, about the base error rate 11/185 = 0.06 |
Wrong positions (wrong_dev_tune.tsv) come from the taxonomy's err_U rows, matched to read positions within +-2 (19 of 20 placed).
As a sorter flag the written features carry no signal here.

## Reader task text
Both calls: the unchanged `harvest/blind_pass_brief_1572.md`, then the section "Features first, then the cell" (the rule and the
51-row cell table), then task lines naming the sign sheet, the 18 crops and the output path: `reader_task_dev_c1.md`,
`reader_task_dev_c2.md`. Subagent prompt (both): "Your instructions are in the file <reader_task_dev_cN.md>. Read that file
first and follow it exactly. Besides that file, open only the images it names (the sign sheet and the crops). Write only the
TSV it names." Both readers again reported that the overlap was wider than the brief's 100 px (5-6 signs).

Calls: 2 Opus vision (dev), 0 eval. Cost: the lane reads get_session.
Follow-up (one line): to test feature-first deciding at all, use two calls per line. Call 1 sees the crop only (no sheet, no
table) and writes features per sign. Call 2 sees the crop, the sheet and call 1's features and names the cell, and the
compliance count (features written before and independently of the cell) is checked before scoring. Not attempted (brief).
