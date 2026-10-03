# TX-ATLAS-B72 (account-3 orchestrator, 3 Oct 2026): one sign atlas for the Birago 1572 key family

Read TRANSCRIPTION.md. Model Opus 5.5. Cap USD 15, box 90 min. Pipeline steps 2-5 on every Birago 1572 letter at once:
nevers-birago-fr3251-1572 (nos.71, 73, 77, 82, 85, 86, 87, 90) and birago-fr3252-1571-72 f.117, using images already on
disk (no refetch). tools/glyph_atlas.py segment (all pages, --debug; check overlays) then cluster (over-split). Name
clusters from the no.87 clerk-sheet alignment first (known answer), then cluster exemplar sheets read by a model, one
call per sheet: vision calls: 8 x USD 1.5 = 12 (estimate; advisory per README). Extend glyph_atlas.py classify to emit
top-3 clusters with distances (top-k TSV), test included. Output an atlas folder in nevers-birago-fr3251-1572/atlas/
that sibling letters reuse, plus per-letter top-k TSVs. Score with tools/tx_bench.py if TX-BENCH has landed (else the
no.87 clerk-sheet truth directly): err_true of atlas top-1 vs the line-read reconciliation on the same signs. Do not
change any committed reading; this job produces inputs for TX-DECODE.
Shared files: ROOM claim/done via tools/room.py; update the TRANSCRIPTION.md "Today" column and SYSTEM.md (system_map_check ok) for any new tool, with --help and an offline test in tools/tests/ (Usage 8). gaps_check/file_shrink_guard before the final push. Never print credentials, never name the owner, never AskUserQuestion. Done line "for the account-3 orchestrator" with the headline number.
