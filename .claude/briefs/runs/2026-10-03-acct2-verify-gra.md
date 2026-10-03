# VERIFY-GRA: verifier on fr2980-gramont f.30 extended reading (3 Oct 2026, written by LANE-A2PUSH, account 2)

Model: Opus 5.5. Cap USD 6, box 50 min. A session separate from the solver (A2-GRA3); do not protect its conclusions.
Claim under audit: A2-GRA3 (commit a888c33f) split f.30's eh sign by shape into ehx (c with crossed stroke, 20 positions) plus 2 plain c,
and accepted ehx = T at grade S (152.1 bits over D, control p 0.010, recovery 1.00); crosses split pattee 5 / double-barred 2 / circled 1,
no value passes. Files: ciphers/fr2980-gramont/NOTES.md "f.30 eh and CROSS split by shape", split_f30.tsv, test_f30r_split.tsv,
reading_f30_extended.txt. AUDIT.md lines ~886-893 (eh T vs D) and the SECOND-OPINIONS-QUEUE.tsv row SO-GRAMONT-F30 predate it.
Jobs, in order: (1) re-check the shape split yourself from the crops on disk (do the 20 ehx tiles share the crossed stroke, are the 2 plain c
really plain?) and re-run the control the solver ran; (2) re-run the target's decode script with --check; (3) carry the revision into
AUDIT.md and the SO-GRAMONT-F30 row (rule 10 propagation, V6-MERCY2 lesson), re-searching novelty only for phrases the revision changes
(phrase search, families (a)-(g) of CLAUDE.md's verifier template for those phrases; log each family as searched or unreachable);
(4) keep or revise the N-class and key source, safe/unsafe sentences; postmortem on any over-claim.
Start: `python3 tools/room.py --start` (detached HEAD: `git push origin HEAD:main; git checkout -B main HEAD`); `date -u`; claim
`python3 tools/room.py "VERIFY-GRA (account 2, LANE-A2PUSH)" 'claim: verifier fr2980-gramont f.30 ehx revision; box ends <HH:MM> UTC'`.
Halfway line at about 25 min. Do not touch other targets. Good-citizen rule for hosts; never print credentials. Commit by explicit path,
file_shrink_guard, `python3 tools/room.py --push <paths>`, run `git fetch origin main && git log origin/main --oneline -5` and confirm your
commit is there, then the done line for LANE-A2PUSH (account 2) with the class, whether ehx = T stands, and the one-line postmortem.
Never call AskUserQuestion.
