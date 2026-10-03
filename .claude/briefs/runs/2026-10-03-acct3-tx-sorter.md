# TX-SORTER (account-3 orchestrator, 3 Oct 2026): active sorter that propagates across a key family

Read TRANSCRIPTION.md (pipeline step 7). Model Opus 5.5. Cap USD 8, box 60 min. Disk only: vision calls: 0 x USD 1.5 = 0.
Extend tools/sign_sorter.py and tools/sign_sorter_apply.py (no new private script): (1) --rank FILE: an optional TSV of
tile value scores (expected change in key rank or decode when the tile flips between its top-2 labels; compute it with
tools/key_decode_lattice.py if TX-DECODE has landed, else from look-alike confusion frequency x occurrences) shown as a
"Most useful first" box capped at 20 tiles; (2) cluster-level decisions: when tiles carry an atlas cluster id, a
person's relabel of one tile offers "apply to all N in this cluster" and sign_sorter_apply.py writes the decision to the
family atlas so every sibling letter's next build picks it up. Keep the existing db-capability save format backward
compatible (the published Birago and Florence sorters must still apply). Offline tests for both. Build one demo page in
scratch for Birago 1572 (do not publish; the account-3 orchestrator publishes).
Shared files: ROOM claim/done via tools/room.py; update the TRANSCRIPTION.md "Today" column and SYSTEM.md (system_map_check ok) for any new tool, with --help and an offline test in tools/tests/ (Usage 8). gaps_check/file_shrink_guard before the final push. Never print credentials, never name the owner, never AskUserQuestion. Done line "for the account-3 orchestrator" with the headline number.
