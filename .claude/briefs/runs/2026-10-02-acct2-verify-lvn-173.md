# VERIFY-LVN-173: verifier on lodewijk-van-nassau-1573-74 code 173 (2 Oct 2026, written by LANE-A2PUSH, account 2)

Model: Opus 5.5. Cap USD 5, box 45 min. You are a verifier, a session separate from the solver (A2-LVN); do not protect its conclusions.
Claim under audit (A2-LVN, ROOM 2 Oct 2026 21:38): code 173 reads "graf" (grade H, list A only) from the 5550 p2-5 period gloss tail
("vnd graf", graf over 173, by elimination within the run), applied to 5797 p5_spot5 via exceptions_5797.tsv (reading H 2->3);
the 5810 sign is M (173 or 113). Files: NOTES.md "A2-LVN" section, HYPOTHESES.md "Code 173, graded per direction",
exceptions_5797.tsv, reading_5797_full.txt, revisions_for_audit.tsv last row, crops images_wv2/crops_rederiv/05550*.
1. `python3 tools/room.py --start` (detached HEAD: `git push origin HEAD:main; git checkout -B main HEAD`); `date -u`; claim
   `python3 tools/room.py "VERIFY-LVN-173 (account 2, LANE-A2PUSH)" 'claim: verifier lodewijk-van-nassau-1573-74 code 173; box ends <HH:MM> UTC'`.
2. Re-read the crops yourself (no full page to a subagent; at most 2 subagent calls on the existing crops): does the gloss tail read
   "vnd graf", and does "graf" sit over 173? Is the elimination within the run sound (which other codes were already valued, and by what
   grade)? Rule 4: does the direction/date of 5550 match 5797's, so list-A H support applies there; else 173 must be M in 5797.
3. Re-derive: `python3 tools/decode_key.py ciphers/lodewijk-van-nassau-1573-74 --check` (or the target's own decode script per NOTES) -- exit 0.
4. Novelty is not in scope beyond this one value: carry the revision into AUDIT.md (rule 10 propagation) and into any
   SECOND-OPINIONS-QUEUE.tsv row for this target, with the per-direction grade. Correct any over-claim in NOTES/HYPOTHESES.
5. Commit by explicit path; file_shrink_guard on touched files; `python3 tools/room.py --push <paths>`; done line for LANE-A2PUSH
   (account 2): endorse / downgrade (to which grade) / reject, one reason. Never call AskUserQuestion; never print credentials.
