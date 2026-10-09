# TXE2 round-2 jobs (LANE TX-ENGINEER-2; Opus 5.5; one job per worker; PREREG benchmark-tx/PREREG-txeng2-2.md is binding)

For LANE TX-ENGINEER-2 (account 4, session_01NmaB9fhuaMSMYexV4NaVsR). Written 9 Oct 2026 16:3x UTC by date -u. Every job:
first `git fetch origin && git checkout -B main origin/main`; `export CIPHERLAB_ACCOUNT=account-4`; `python3 tools/room.py
--start`; ROOM.md last 30 lines; claim with `python3 tools/room.py "<JOB> worker (account 4, Opus)" "claim ..." --push`; read
benchmark-tx/PREREG-txeng2-2.md (your section) and PREREG-txeng2-0.md (gate, pools, blindness), TRANSCRIPTION.md, CLAUDE.md
Usage 6 and rule 3; then the files your section names. Every tool: `--help`, offline test in tools/tests/, SYSTEM.md row,
tool_shelf.tsv row (system_map_check passes). Commit every output BEFORE tx_bench scores it; never score eval_heldout or
any eval item for an experiment (the lane spends looks); never edit a *.truth.tsv by hand; readers (where any) see crops and
the blind sheet/brief only; never AskUserQuestion; stage by path; never force-push. Stop before a unit that would cross 80%
of cap or box; commit what exists; done line "for LANE TX-ENGINEER-2" with every number and "cost: the orchestrator
get_session reading". Write `benchmark-tx/txeng2/<job>/RESULTS.md`. + `.claude/briefs/README.md` common tail.

| job | PREREG section | cap | box | inputs to read first |
|---|---|---|---|---|
| TXP-REBUILD | R | 4 | 50 min | benchmark-tx/build_dint-f89-gloss.py, build_dint-f98v-gloss.py, build_dint-f113-gloss.py, build_bir1591-f23r-gloss.py (+ each item's RESULTS.md and gloss.tsv), ciphers/fr3621-dinteville-1592/f128/print_align/key_print.tsv, benchmark-tx/dint128_label_map.tsv, tools/tx_bench.py, tools/tx_power.py |
| TXE2-SHEET | X1 | 7 | 75 min | benchmark-tx/txeng2/decode-scout-2026-10-09.md, ciphers/fr3621-dinteville-1592/f128/pass_instructions.md + images/f128_*, benchmark-tx/dint128_label_map.tsv, benchmark-tx/outputs/dint-f128-print/, benchmark-tx/txeng2/dint-f89-gloss/{passA,passB,passZ_pipeline}.tsv + crops, tools/glyph_atlas.py (features), benchmark-tx/txsheet/RESULTS.md (why TX-SHEET failed) |
| TXE2-LATT | X3 | 5 | 60 min | tools/key_decode_lattice.py (from-passes, decode, --confusion-matrix), tools/segmenter.py, benchmark-tx/txeng/conf/RESULTS.md (TXE-E), benchmark-tx/txeng/doubt/ (two-signal positions), ciphers/nevers-birago-fr3251-1572/atlas/topk/ (held-out top-3), research/TX-TAXONOMY-2026-10-09.md pairs |
| TXE2-CONF | X4 | 6 | 70 min | ciphers/nevers-birago-fr3251-1572/harvest/blind_pass_brief_1572.md + sign_sheet_blind_1572.png, the dev_tune crops (harvest/f178v/f178v_L01-12_s?.jpg), benchmark-tx/txeng/units/README.md (pass-A call grouping), tools/key_decode_lattice.py from-passes |
| TXE2-DOUBT | X9 + X17 | 4 | 50 min | tools/tx_doubt.py (+ benchmark-tx/txeng/doubt/RESULTS.md), benchmark-tx/txeng2/pair/ (classifier outputs), benchmark-tx/txeng2/weight/, benchmark-tx/txeng/geo/ (H, H2), outputs K2/V_s0/V_s1, tools/tx_sorter_curve.py |
