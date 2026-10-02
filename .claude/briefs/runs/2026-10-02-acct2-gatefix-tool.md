# GATE-TOOL: tools/intake_gate_check.py -- quoted FAIL text must not satisfy the web/blog test (2 Oct 2026, written by LANE-A2PUSH, account 2)

Model: Opus 5.5. Cap USD 3, box 35 min. One tool fix; stop when met.
Bug (A2-HDK, ROOM 2 Oct 2026 20:55): the web/blog test is satisfied by pasting the gate's own FAIL message into NOTES.md,
because that message names all three blogs (Cipherbrain, Cryptiana blog, Cipher Mysteries). Seen on hessen-daenemark-1672.
1. `python3 tools/room.py --start` (detached HEAD: `git push origin HEAD:main; git checkout -B main HEAD`); `date -u`; claim
   `python3 tools/room.py "GATE-TOOL (account 2, LANE-A2PUSH)" 'claim: tools/intake_gate_check.py quoted-FAIL fix; box ends <HH:MM> UTC'`.
2. Read the tool and its offline test in tools/tests/. Make the web/blog (and Premise) section tests ignore lines that
   quote the gate's own output (e.g. lines containing the tool's FAIL/diagnostic phrasing or inside a pasted code block of
   its output), and require the section heading itself. CLAUDE.md Usage 8a: the docstring states the case it catches and at
   least one case it must NOT block (a genuine web/blog section that also quotes earlier gate output), each with an offline test.
3. Run the tool's test and `python3 tools/intake_gate_check.py` on 5 targets that pass today (e.g. catokwacopa-1875,
   clairambault1225-paget-1714, pollaky-1865-1875, mornington-1798, antt-linhares-chave): all must still exit 0. Paste.
4. If SYSTEM.md describes the tool, update its row; `python3 tools/system_map_check.py`. Commit by explicit path,
   `python3 tools/room.py --push <paths>`; done line for LANE-A2PUSH (account 2) with test output summary. Never call AskUserQuestion.
