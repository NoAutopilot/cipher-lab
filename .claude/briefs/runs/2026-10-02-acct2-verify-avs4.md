# VERIFY-AVS4: verifier on august-van-saksen-1561-64 WVO 124 alignment and three held pairings (2 Oct 2026, LANE-A2PUSH, account 2)

Model: Opus 5.5. Cap USD 4, box 40 min. Separate from the solver (A2-AVS4); do not protect its reading. No novelty claim in scope.
Claim (A2-AVS4, ROOM 22:58): WVO 124 f.134 aligned against its decipherment f.135 (align_124.txt, 679 signs; control 611/611 vs shuffled 0.100;
interlinear_align word signs 17/21 vs shuffled 1.4); key_98 rebuilt from 98+124; 126 now C 229 M 11. Three sure-but-held ~ pairings in align_124 header: 1=i, open-L as m, D as d. Files: align_124.txt, key_98.tsv, reading_tokens_126.tsv, NOTES A2-AVS4.
1. room.py --start (detached HEAD: `git push origin HEAD:main; git checkout -B main HEAD`); `date -u`; claim
   `python3 tools/room.py "VERIFY-F61R (account 2, LANE-A2PUSH)" 'claim: verifier august-van-saksen WVO 124 + 3 pairings; box ends <HH:MM> UTC'`.
2. Re-read the f.134/f.135 images on disk yourself (crops, no full page to a subagent; at most 2 subagent calls) at the three held pairings and a 20-sign sample of the alignment; check the control can fail differently (rule 3); decode_key --check.
   Rule 4: grade C only where the decipherment f.135 itself supplies the value.
3. Rule each held pairing: endorse (C) / keep held (M) / reject, one reason each; write under the A2-AVS4 step; apply endorsed ones to key_98 with --check.
   Carry any change into AUDIT.md and SECOND-OPINIONS-QUEUE.tsv rows for this target if they exist (rule 10 propagation).
4. Commit by explicit path; file_shrink_guard; room.py --push; confirm the commit is on origin/main; done line for LANE-A2PUSH (account 2).
   Never call AskUserQuestion; never print credentials.
