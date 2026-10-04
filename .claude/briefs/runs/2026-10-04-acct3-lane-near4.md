# LANE-NEAR4 (account 2) -- 4 Oct 2026 03:1x UTC (account-3 orchestrator)

Follows LANE-NEAR3 (STATUS.md "LANE NEAR3 handoff"). Operating rules exactly as `.claude/briefs/runs/2026-10-04-acct3-lane-near3-run1.md`
paragraph 1. Account 3's LANE-A3V does audits: hand it a ROOM line when a reading is ready for audit; never audit your own reading.

Jobs, in order:
1. clair1161-avis-flandre-1688 (C1POOL held-out PASS: key fitted on c185R+c186R reads the 4 new leaves above shuffled-key and order nulls).
   (a) Transcribe the remaining cipher leaves (c188R and any other cipher run in btv1b90010063 c185-c188) and re-check c187R/c188L slope;
   (b) pooled decode of all leaves with decode_key.py, per-token grades (S only where two instruments agree), reading.txt + English gist
   marked as interpretation in NOTES.md; (c) judge with the fr16/fr17 corpus whichever fits the 1688 date best (rule 3 era note);
   (d) ROOM line to LANE-A3V: "clair1161 ready for audit 1".
2. hellen-frederick-1752: NA Fagel inv. 5177 (De Leeuw n.32) -- English/Lyonet decipherments of Hellen letters No 1-37 (Oct-Dec 1751):
   catalogue flag + scans (Nationaal Archief route in CLAUDE.md host table); if cipher and plain survive side by side, a known-plaintext
   recovery of codes 1-800 (tools/interlinear_align.py, C grade) with a pre-registered held-out gate.
3. key_crossmatch leads of 4 Oct 02:50 (ROOM 02:53-02:55): fr3993-villeroy key_f159_letters vs august-van-saksen-1561-64 ct58/ct74/ct57
   (stat 8.66/7.22/6.48, gate 3.29) -- read by eye with a matched control (another letter-alphabet key of the same size on the same
   ciphertexts) before any claim; most likely a generic letter-frequency artefact, say so if it is. Also key_no25 vs fr3993-gonzague
   (expected: same key family, found-solved) -- one line confirming.
4. fr16142-noailles-constantinople-1571: turn RUN2-NXATL's sheets (run2/nxatl) into a sign_sorter page (tools/sign_sorter.py) for c510-516
   (9,904 tiles; err_2reader 39-57% so the owner's sort is the next pass); page built in scratch, never committed if over 30 MB; ROOM
   line for account 3 to publish. Coordinate with LANE-RUN2 (account 1) on its Noailles claim first.
5. Backlog: NEXT-STEPS runnable rows, S band first, not claimed by RUN2 or A3V.
