# VERIFY-F61-LL: verifier on fr4715-f61-mayenne-1592 L02-opening LL (2 Oct 2026, written by LANE-A2PUSH, account 2)

Model: Opus 5.5. Cap USD 4, box 40 min. You are a verifier, separate from the solver (A2-F61); do not protect its conclusion.
Claim (A2-F61, ROOM 2 Oct 2026 21:54): `L02 0 insert LL` (a null) is endorsed by the pre-registered V13 foil read -- the clear
in-word ll of L07 "della" read O at 3/3 windows while the target read LL at 3/3 (anchors 9/9, LL in-span control, repeats PASS);
caveat: the foil was named from word context. Files: family/a2f61/ (PREREG.md, reply.tsv, key.json, score.py --check,
score_result.txt), NOTES.md step A2-F61. Merge would give meter 12/59/1/28 of 100.
1. `python3 tools/room.py --start` (detached HEAD: `git push origin HEAD:main; git checkout -B main HEAD`); `date -u`; claim
   `python3 tools/room.py "VERIFY-F61-LL (account 2, LANE-A2PUSH)" 'claim: verifier fr4715-f61-mayenne-1592 L02 LL; box ends <HH:MM> UTC'`.
2. Check PREREG.md was committed before reply.tsv (git log order); run score.py --check; read the crops yourself. Is the foil
   choice (named from word context) a leak that makes the test pass by construction (rule 3: can the control fail differently
   from the target)? Is 3/3 vs 3/3 above what chance gives at this N?
3. Rule: endorse (merge allowed, give the grade), downgrade (M, not merged), or reject; write it in NOTES.md under the A2-F61
   step and in AUDIT.md if one exists. If endorsed, do NOT merge yourself; name the merge as the next step in the Verdict line.
4. Commit by explicit path; file_shrink_guard; `python3 tools/room.py --push <paths>`; done line for LANE-A2PUSH (account 2) with
   the ruling and one reason. Never call AskUserQuestion; never print credentials.
