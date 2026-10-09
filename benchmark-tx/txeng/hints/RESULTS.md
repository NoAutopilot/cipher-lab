# TXE-H results: pair hints in the reader's brief (LANE TX-ENGINEER, idea M17; 9 Oct 2026, 07:34-07:4x UTC by date -u)

Brief `.claude/briefs/runs/2026-10-09-account4-txe-h.md`; pre-registration `benchmark-tx/PREREG-txeng-2.md` (units, blindness,
Amendment: single-instrument gate p < 0.01). Taxonomy class addressed: 1 (inventory look-alike pairs).

**Verdict: FAIL on the registered dev gate.** passP (hinted brief) vs passA (same reader kind, unhinted): fixed 11, broken 3,
two-sided sign test p = 0.057 (gate p < 0.01). Vs L (today's best): fixed 3, broken 4, p 1.0. Eval not run (looks taken 0).
Most of the gain over A is NOT from the hints: 7 of the 11 fixes are one sign read T92 instead of T50 (an omega with a small
right curl), a pair that is not in the hints (T92 has no secure tiles, so no T92 pair could be derived); L already carries
those 7. Movement inside the hinted pairs is 2 fixed / 1 broken.

## Derived hints (`tools/tx_pair_hints.py derive`, hints_dprime.tsv; secure tiles of non-no.87 leaves only, committed 09960c768 before any read)

| pair | n tiles | d' descender / loops / bars | kept as | sentence |
|---|---|---|---|---|
| T18/T98 | 5/18 | 1.97 / 0.65 / 0.15 | kept (descender d 1.97) | T18 vs T98: T18's tail goes below the line by about half of its height; T98's only by about a fifth. |
| T90/T53 | 8/43 | 0.06 / 0.94 / 1.64 | kept (bars d 1.64) | T90 vs T53: T90 has one long horizontal bar across most of its width; T53 has no long horizontal bars. |
| T76/T66 | 18/0 | 0.00 / 0.00 / 0.00 | dropped: too few secure tiles (T76 18, T66 0; need 3) |  |
| T76/T86 | 18/24 | 0.69 / 1.15 / 1.59 | kept (bars d 1.59) | T76 vs T86: T76 has no long horizontal bars across most of its width; T86 has one long horizontal bar. |
| T76/T45 | 18/42 | 0.91 / 0.06 / 1.18 | kept (bars d 1.18) | T76 vs T45: T76 has no long horizontal bars across most of its width; T45 has one long horizontal bar. |
| T64/T95 | 0/1 | 0.00 / 0.00 / 0.00 | dropped: too few secure tiles (T64 0, T95 1; need 3) |  |
| T64/T51 | 0/0 | 0.00 / 0.00 / 0.00 | dropped: too few secure tiles (T64 0, T51 0; need 3) |  |
| T50/T36 | 6/20 | 1.41 / 2.11 / 2.46 | kept (bars d 2.46) | T50 vs T36: T50 has no long horizontal bars across most of its width; T36 has one long horizontal bar. |
| T92/T95 | 0/1 | 0.00 / 0.00 / 0.00 | dropped: too few secure tiles (T92 0, T95 1; need 3) |  |
| T92/T98 | 0/18 | 0.00 / 0.00 / 0.00 | dropped: too few secure tiles (T92 0, T98 18; need 3) |  |
| T83/T24 | 11/0 | 0.00 / 0.00 / 0.00 | dropped: too few secure tiles (T83 11, T24 0; need 3) |  |
| T60/T86 | 43/24 | 0.00 / 2.17 / 4.01 | kept (bars d 4.01) | T60 vs T86: T60 has two long horizontal bars across most of its width; T86 has one long horizontal bar. |

Dropped: 6 of 12 pairs, all for want of secure tiles (T66, T64, T51, T92, T24 have 0 on non-no.87 leaves; T95 has 1); none
dropped for d' < 1. Caveat seen on the hints sheet before the read (not changed, the statistic is the brief's): the "bar"
statistic (an ink run wider than 0.6 x width) also counts the flat top of a loop, so "T36 / T45 has one long horizontal bar"
describes a loop top, not a crossbar; T90's and T60's bars are true crossbars.

## Score (tx_bench, dev_tune; raw reads committed d69201ec8 before scoring)
```
birago1572-no87 [eval] err_true 0.047 (16/343) 95% 0.029-0.074 | wrong 15 deleted 0 inserted 1 | excluded 11 | lines missing 17
paired passP_hints_dev_tune.tsv vs passA_dev_tune.tsv on birago1572-no87: 343 common scored signs; base wrong 23, output wrong 15; fixed 11, broken 3; sign test p = 0.0574
paired passP_hints_dev_tune.tsv vs labels_dev_tune.tsv on birago1572-no87: 343 common scored signs; base wrong 14, output wrong 15; fixed 3, broken 4; sign test p = 1.0000
```

## Movement (tools/tx_taxonomy.py, A vs P vs L, taxonomy_dev_tune.tsv/.md; run after the reads were pushed)
- Fixed vs A (11): L01.23, L03.4, L04.4, L05.25, L07.29, L08.10, L10.5 T50->T92 (truth s; outside the hint list);
  L02.19 T83->T81 (b); L06.18 T98->T18 (d; hinted pair); L10.1 T92->T53 (t); L11.29 T60->T86 (e; hinted pair).
- Broken vs A (3): L08.16 T60->T86 (n; hinted pair); L10.17 T76->T15 (n); L12.32 T96->? (i, line-end edge).
- Per hinted pair, positions changed each way (A -> P on aligned positions): T98->T18 2 (1 fixed, 1 neutral); T60->T86 2
  (1 fixed, 1 broken); T90/T53, T76/T86, T76/T45, T50/T36: 0 changed. 26 aligned positions changed in all.
- Class 1 floor unchanged: e<-T76 x3, g<-T42, e<-T36, t<-T90 are wrong in A, P and L alike. P's errors repeat A's at 12/15.
- Thin-stroke errors 12 -> 7 (A -> P), most of it the T50/T92 sign.
- Possible indirect route (not testable from this read): the hints sheet showed T50's tiles (an omega followed by a long s),
  which may have led the reader to put the plain curled omega in T92. That would be the sheet working as an exemplar, not the
  sentence.

## Reader task text
Both calls: the unchanged `harvest/blind_pass_brief_1572.md` + hints.md as a section + task lines naming the sign sheet,
hints_sheet.png, the 18 crops and the output path: `reader_task_dev_c1.md` (L01-06), `reader_task_dev_c2.md` (L07-12).
Subagent prompt (both): "Your instructions are in the file <reader_task_dev_cN.md>. Read that file first and follow it
exactly. Besides that file, open only the images it names (the sign sheet, the pair-examples picture and the crops). Write
only the TSV it names." Both readers said the overlap is much wider than the brief's 100 px (5-6 signs), the class 2c fault
TXE-B's crops_note fixes; it was left alone here (the brief says nothing else changes).

Calls: 2 Opus vision (dev), 0 eval. Cost: lane reads get_session.
Follow-up (one line): the one movement worth a test is the T50/T92 sign (7 dev positions); a T92 secure-tile source (labels or
a sibling letter) would let a T50/T92 hint be derived and tested -- not attempted (brief).
