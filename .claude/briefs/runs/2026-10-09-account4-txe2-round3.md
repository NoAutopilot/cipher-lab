# TXE2 round-3 jobs (LANE TX-ENGINEER-2; Opus 5.5; one job per worker; PREREG benchmark-tx/PREREG-txeng2-3.md is binding)

Same preamble and rules as `.claude/briefs/runs/2026-10-09-account4-txe2-round2.md` (first commands, claim line, PREREG-txeng2-0
gate and blindness, tools with --help/test/SYSTEM/shelf rows, outputs committed before any score, no eval scoring, no truth
edits, readers see crops + blind sheet/brief only, 80% stop, done line "for LANE TX-ENGINEER-2" with every number and "cost:
the orchestrator get_session reading", RESULTS.md under benchmark-tx/txeng2/<job>/). + `.claude/briefs/README.md` common tail.

| job | PREREG section | cap | box | inputs to read first |
|---|---|---|---|---|
| TXP-KP2 | R2 | 3 | 40 min | benchmark-tx/txeng2/rebuild/RESULTS.md + diagnose.py, the four build_*.py (their --variant option), key_print.tsv, dint128_label_map.tsv, tools/tx_power.py |
| TXE2-SAME | X7 | 7 | 75 min | benchmark-tx/txeng2/doubt/RESULTS.md (the combo feed's dev_tune positions file), benchmark-tx/txeng2/latt/ (lattice d runner-ups), tools/tx_compare.py (build/resolve code to reuse for sheets; NOT its exemplar source), atlas/signs.tsv + no87_box_token.tsv (sid, line, pos, sign columns only), harvest/f178v page image, research/TX-TAXONOMY-2026-10-09.md pairs, benchmark-tx/txeng/compare/RESULTS.md (why the compare family failed) |
| TXE2-COUNT | X12 | 6 | 60 min | ciphers/fr3621-dinteville-1592/f128/pass_instructions.md + images/f128_*, benchmark-tx/outputs/dint-f128-print/, benchmark-tx/dint128_label_map.tsv, ciphers/ceppo-nevers-fr3251-1570s/harvest/f87/ (crops, pass brief), benchmark-tx/outputs/ceppo-f87-S/ |
| TXE2-CELLS | X13 | 6 | 60 min | benchmark-tx/txeng2/doubt/ (dev_tune combo positions), benchmark-tx/txeng2/latt/ (lattice d top alternatives), harvest/sign_sheet_blind_1572.png, the dev_tune crops, tools/tx_pair_reread.py (sheet build/resolve code), benchmark-tx/txeng/pair/RESULTS.md |
| TXE2-COST | X8 | 8 | 70 min | ciphers/fr3621-dinteville-1592/f128/pass_instructions.md + images/f128_*, benchmark-tx/outputs/dint-f128-print/, dint128_label_map.tsv, TRANSCRIPTION.md target 8 figures, tools/tx_prep.py (2x rendering) |
| TXE2-PAIR2 | X2b | 5 | 60 min | benchmark-tx/txeng2/pair/RESULTS.md + tools/tx_pair_clf.py (reuse: add `--train-domain dev_tune --loo-lines`), atlas/no87_box_token.tsv (training step may read sid, line, pos, sign, truth for TRAINING lines only; the apply step reads no truth), atlas/bitmaps.npz, benchmark-tx/txeng/units/labels_dev_tune.tsv, PREREG-txeng2-1 X2 |
