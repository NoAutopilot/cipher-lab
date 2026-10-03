# TX-BENCH (account-3 orchestrator, 3 Oct 2026): known-answer transcription benchmark + scorer

Read TRANSCRIPTION.md (the standard this job serves). Model Opus 5.5. Cap USD 10, box 70 min.
vision calls: 0 x USD 1.5 = 0 (disk only: every item's truth and the pipeline outputs already exist in the folders).
Build BENCHMARK-TX.tsv: one row per known-answer item (folder, leaf/line ids, crop or tile paths, truth sign sequence,
truth source and grade, key family, hand, split dev|eval -- families never straddle splits). Items, in order: Birago
no.87 vs the clerk sheet (ciphers/nevers-birago-fr3251-1572, NEVBIR-87ALIGN, keys/key_1572_clerk.tsv); Birago 1571 f.36v L1
vs the period gloss; Ceppo f.21v and f.87 S-graded spans; colbert26 f.23/f.24 interlinear spans; Mercy H spans; any other
folder with an H/C-graded span over an existing two-pass transcription (grep NOTES.md for "known-answer"). Truth for a
sign = the sign that the known plaintext forces under the key, only where unambiguous; ambiguous positions excluded and
counted. Build tools/tx_bench.py PIPELINE_OUTPUT.tsv --bench BENCHMARK-TX.tsv: err_true per item, per sign class (top
confusions), dev vs eval, Wilson 95% intervals; offline test. Score what exists: passA, passB, reconciled, look-alike
output, per item. Write the numbers into TRANSCRIPTION.md "Today" rows 1 and 8 and a short "Benchmark" result paragraph.
Shared files: ROOM claim/done via tools/room.py; update the TRANSCRIPTION.md "Today" column and SYSTEM.md (system_map_check ok) for any new tool, with --help and an offline test in tools/tests/ (Usage 8). gaps_check/file_shrink_guard before the final push. Never print credentials, never name the owner, never AskUserQuestion. Done line "for the account-3 orchestrator" with the headline number.
