# TOOL-SHELF (account-3 orchestrator, 3 Oct 2026): make the tools we already built findable at briefing time

Owner, 3 Oct 2026: "anything else we built that'd be helpful?" Audit found shared tools never used on the targets they
fit (tools/glyph_atlas.py on Birago/Florence; tools/seg_homophonic.py, tools/key_crossmatch.py, tools/cipher_page_detector.py
on the Birago numerical system). Model Opus 5.5. Cap USD 6, box 50 min. Disk only: vision calls: 0 x USD 1.5 = 0.
(1) Add a "Tool shelf" table to SYSTEM.md (or extend its tools table): one row per tools/*.py|js with a "use when"
column phrased as the problem a briefer has (e.g. "unseparated digit cipher, no key" -> seg_homophonic.py; "a key on
disk might read another ciphertext" -> key_crossmatch.py; "find cipher pages in a whole volume" -> cipher_page_detector.py;
"leaf with a clerk's plaintext" -> decode_witness.py / interlinear_align.py; "sign shapes unsettled" -> glyph_atlas.py,
sign_sorter.py), and the count of target folders that cite it. (2) tools/tool_shelf.py "<problem words>": prints the
best-matching shelf rows (keyword match over use-when + docstring), with test. (3) .claude/briefs/README.md common tail
and .claude/briefs/parent.md "Opening a lane": before briefing a new instrument or a private script, run
tools/tool_shelf.py on the problem and name the tool in the brief or say why it does not fit. (4) List in the done line
every tool cited by 0-1 folders whose use-when matches an open/partial target in NEXT-STEPS.tsv (the next jobs).
ROOM claim/done via tools/room.py; SYSTEM.md + system_map_check ok for any tool change, offline test (Usage 8); file_shrink_guard before the final push. Report what was found and where it was not found; do not classify novelty. Done line "for the account-3 orchestrator".
