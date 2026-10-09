# TXE2 round-4 jobs (LANE TX-ENGINEER-2; Opus 5.5; one job per worker; PREREG benchmark-tx/PREREG-txeng2-4.md is binding)
Same preamble and rules as `.claude/briefs/runs/2026-10-09-account4-txe2-round2.md`; read also benchmark-tx/PREREG-txeng2-0.md
Amendment 2 and research/TX-RED-2026-10-09.md pass 1 (the findings these jobs answer). + `.claude/briefs/README.md` common tail.
| job | PREREG section | cap | box | inputs to read first |
|---|---|---|---|---|
| TXP-KP2C | C1 | 2 | 40 min | benchmark-tx/txeng2/kp2/RESULTS.md + benchmark-tx/truth_variant.py (or the kp2 code in the build scripts), build_dint128.py, ciphers/fr3621-dinteville-1592/f128/print_align/ (align_print.tsv, key_print.tsv), benchmark-tx/dint-f128-print.truth.tsv (the print truth), outputs/dint-f128-print/passB.tsv |
| TXV-152 | V1 | 3 | 45 min | benchmark-tx/txeng2/f152r/RESULTS.md, benchmark-tx/build_birago152.py (flag column), benchmark-tx/birago1572-no87.flags.tsv (the format TX-TRUTH-VERIFY used), ciphers/nevers-birago-fr3251-1572/harvest/f152r/slip_f151v_c154_1350_750_2350_1050.jpg + decipherment_slip.tsv, harvest/key_1572_sheet.tsv; the three positions' crops |
| TXE2-SHEET2 | X1b | 4 | 50 min | tools/tx_offsheet.py + benchmark-tx/txeng2/txe2-sheet/RESULTS.md, benchmark-tx/txeng/confirm/ (Spinelli crops, passA/B/Z, collapse_map), ciphers/spinelli-beinecke-c1515/images/ (sibling pages), glyphs/atlas_v2.*, benchmark-tx/txeng2/f152r/, benchmark-tx/txeng/units/labels_eval_heldout.tsv |
| TXE2-FEED | S4 | 3 | 40 min | benchmark-tx/txeng2/doubt/RESULTS.md + signal tables, tools/tx_doubt.py, tools/tx_sorter_curve.py, ciphers/nevers-birago-fr3251-1572/sorter/no87/ (focus.tsv format), research/TX-TAXONOMY-2026-10-09.md (the question per pair) |
| TXE2-COST2 | X8b | 6 | 70 min | benchmark-tx/txeng2/cost/RESULTS.md (arms, briefs, token accounting), ciphers/ceppo-nevers-fr3251-1570s/harvest/f87/ (crops, brief), benchmark-tx/outputs/ceppo-f87-S/, outputs/dint-f128-print/ |
