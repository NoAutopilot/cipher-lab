# TOOL-DK-HASH (tools/decode_key.py): a "#" cipher sign must not be read as a comment (3 Oct 2026, written by LANE-A2PUSH2, account 2)

Model: Opus 5.5 (claude-opus-5-5), never below. Cap USD 2, box 30 min from your claim. One tool, one fix. Disk only, no images.

Flag (A2-DIN2, ROOM 05:06): tools/decode_key.py's key and ciphertext readers skip any line starting with "#" (lines ~103, 139,
153, 207), so a cipher sign written "#" (fr3621-dinteville-1592) decodes as U; that folder works round it with a derived
key_dk.tsv. Fix: a line is a comment only when it starts with "# " (hash + space) or "#" followed by nothing, or sits before
the header row -- choose the narrowest rule that keeps every existing decode config working.
1. `python3 tools/room.py --start` (detached HEAD: `git push origin HEAD:main; git checkout -B main HEAD`); ROOM claim with box end (`date -u`).
2. Before editing: run `python3 tools/decode_key.py ciphers/<t> --check` on every folder that has a key.tsv/decode.json and save
   the pass/fail list (baseline). Run the tool's offline tests in tools/tests/.
3. Make the fix; add an offline test (a key whose sign is "#" decodes, a "# comment" line is still skipped); state in the
   docstring what the rule catches and what it must NOT treat as a comment (CLAUDE.md 8a).
4. Re-run the full --check sweep: the pass/fail list must be identical to the baseline except folders that use "#" as a sign
   (name them). Then show fr3621-dinteville-1592 decodes its "#" sign with the original key file (do not edit that folder's files;
   report the diff for A2-DIN3).
5. SYSTEM.md line if the tool's behaviour description changes (system_map_check ok). file_shrink_guard on touched files;
   commit by explicit path; tools/room.py --push; done line "for LANE-A2PUSH2 (account 2)" with baseline vs after counts.
   Confirm the commit on origin/main first. Never call AskUserQuestion; never print credentials; never name the owner.
