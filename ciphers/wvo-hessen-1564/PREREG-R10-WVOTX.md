# PREREG R10-WVOTX -- f.23 alignment re-run on a careful gloss transcription (written and pushed before any scored run)

Worker R10-WVOTX, account 4, 6 Oct 2026 (09:4x UTC by date -u), for LANE LANE-RUN10-account-4.
Brief: .claude/briefs/runs/2026-10-06-account4-run10-jobs.md job R10-WVOTX.

Only the gloss input changes. Everything else is PREREG-R9-WVOALIGN.md, unchanged:
- gloss: two blind Sonnet passes over gloss-row-only crops (r10tx/passA.tsv, r10tx/passB.tsv), crops cut by
  `tools/iiif_lines.py --image ciphers/wvo-hessen-1564/images/01109_p3_400full.jpg --out ciphers/wvo-hessen-1564/r10tx/crops
  --region 530,120,2790,1840 --centres 90,180,260,325,410,480,580,655,745,820,930,1015,1100,1190,1290,1375,1480,1560,1630,1720
  --lines-per-crop 1 --max-width 1000 --overlap 120 --top-margin 25 --bottom-margin 50 --prefix f23G` (a first cut at --top-margin 15
  --bottom-margin 10 clipped the sloping right end of the rows; re-cut and both passes restarted before any output, 09:5x UTC)
  (the 10 odd-numbered bands = the German rows kept, the cipher bands deleted), reconciled by this worker against those crops
  and r9align/crops_m/ (1 unit) into r10tx/gloss_r10.tsv, which replaces r9align/gloss_reconciled.tsv (the R9 sketch is kept
  as r9align/gloss_reconciled_r9.tsv).
- cipher labels, statistic (CONSISTENT, top >= 2, >= 2 rows, share >= 0.6), aligner parameters (`--code-prefix @ --seg-bonus 0
  --keep-fs --null-cost -1.0`, 6 iterations), control (row-derangement shuffle, 1000 draws, seed 1564) and gate (primary:
  pile ids, real > p95 -> PASS) are R9-WVOALIGN's. Secondary label sets passA/passB codes reported with their own controls.
- Reported beside the R9 numbers: CONSISTENT real, shuffle mean/p95/max/p for each label set; key.tsv C/M counts before and
  after; decode grade counts before and after; per-pile letter changes.
No parameter is tuned after seeing a score; if the new gloss scores lower than the sketch, that is reported as it is.
