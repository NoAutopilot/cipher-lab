# BNF-K60-SYNC2 (Sonnet worker for LANE BNF-FOCUS, account 2 / ytbiz), 13 Oct 2026

Job: carry BNF-K60's key no.60 changes into the two copies it left unsynced, nothing else. Disk only, no network except
one shallow clone of github.com/dbourdeau/cyphersolver if you need his key60.txt. Cap USD 1.5, box 40 min. Model: Sonnet.

Read first: CLAUDE.md (rules 4, 7, 8), `ciphers/fr3986-nevers-revol-1593/key_changes_c60e6dd.tsv` and the BNF-K60 section
of `ciphers/fr3622-nevers-gondi-1594/NOTES.md`, last 30 lines of ROOM.md.

Steps
1. ROOM claim (tools/room.py, single quotes) with box end and cap.
2. For `ciphers/fr3987-nevers-revol-1593/key.tsv` and `tools/keys/key60.tsv`: apply every mapped row of
   key_changes_c60e6dd.tsv whose tag exists in that file's tag set (they may use different tag spellings: map only with
   certainty, list the rest as unmapped). Same grades and source string as fr3986's key.tsv; credit lines unchanged.
   Write a `key_changes_c60e6dd.tsv` beside each (or one section in tools/keys/README if that is the convention).
3. Rule 7: find every script reading either file (`grep -rl` for both paths) and run its `--check` (or decode_key.py
   `--check`); record which committed readings change. Regenerate only where a regen/--check script exists; list the rest
   in the owning folder's NOTES.md as stale against c60e6dd. Any offline test in tools/tests that loads key60.tsv must pass.
4. Commit by explicit path, `tools/file_shrink_guard.py` on every touched file, push (`tools/room.py --push <paths>`),
   ROOM done line "for LANE BNF-FOCUS (account 2)": rows changed per file, unmapped count, readings changed, tests.

Never print credentials. Never the words solved, cracked, novel, first, new for anything this project did. Never call
AskUserQuestion. If `tools/room.py --start` fails to push from a detached HEAD: `git push origin HEAD:main; git checkout
-B main HEAD`.
