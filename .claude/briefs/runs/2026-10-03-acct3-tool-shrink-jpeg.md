# TOOL-SHRINK-JPEG (account-3 orchestrator, 3 Oct 2026): tools/file_shrink_guard.py crashes on JPEG paths

Flag from CLOSER-40 / GAPS29 (account-4, 06:05-06:18 UTC): file_shrink_guard.py crashes when a touched path is a JPEG
(binary). Fix: treat binary files (images, PDFs; detect by extension or a NUL byte in the first 8 KB) by byte size, or skip
them with a note, never decode them as text; keep the text-file behaviour and the --help scope statement (CLAUDE.md Usage 8a:
docstring names what it must catch and what it must NOT block). Offline test in tools/tests/ covering a JPEG, a PNG and the
existing text cases. Also check tools/room.py --push (it calls the same check) does not crash on an image path. Model Opus 5.5,
cap USD 2, box 20 min, disk only: vision calls: 0 x USD 1.5 = 0. Done line "for the account-3 orchestrator".
