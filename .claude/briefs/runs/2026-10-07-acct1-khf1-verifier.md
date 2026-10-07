# KHF-1 verifier (account 1 for acct3-orchestrator, 7 Oct 2026, written by KHF-1 worker session_01LdaWpkFdQ4Q6GVN9huMpM7)
Opus 5.5. Cap USD 4, box 50 min from your claim (stop before starting a step that would cross 80% of either).
Read CLAUDE.md (rules 3, 4, 4a, 10; Workers "Verifier brief (template)") and the target's NOTES.md in full first.
`python3 tools/room.py --start`; if it cannot push from a detached HEAD: `git push origin HEAD:main; git checkout -B main HEAD`.
ROOM claim first (box end time), done line at the end addressed "for acct3-orchestrator".

VERIFIER: ciphers/erving-monroe-1806. Claim under audit (NOTES.md "Ciphertext and reading", "Grading (KHF-1...)"):
George W. Erving to James Monroe, Lisbon 23 May 1806 (LOC James Monroe Papers mss33217 reel 3 frames 0828-0830), five
coded lines (34 groups) read under the WE028 Monroe-Madison code table as "[Randolph asked] when Mister Monroe would return
home -- the president [answered] not until his successor arrives. [the other bluntly observed that he] Mister Monroe would
be the next president." Grades H29 M4 I1 of 34; shuffled-key control 0/200 (en18 4-gram -0.723 vs shuffle p95 -1.087);
en18 judge PASS at N=105.
1-5: the template steps exactly (extract; search families (a)-(g) incl. a phrase search on the decoded words in their
clear-text context: "next president" / "successor arrives" with Randolph, Monroe, 1806; the Randolph-Jefferson-Monroe 1806
succession talk). The solver's own log is in NOTES.md "Check-solved (KHF-1...)", "Web and blog check" and "Premise check" --
do not trust it, re-run what matters. Cover also: the annotation (not only the table of contents) of Preston, *Papers of
James Monroe* vol. 5 (2014), esp. notes to "To John Randolph, 16 June 1806" -- the solver read only the TOC; Ammon's and
Cunningham's Monroe biographies and Adams's/Risjord's Randolph literature (the "Monroe for president" 1806 scheme is well
known -- the question is whether *this coded passage* was ever read or quoted); W&M Swem / UMW Monroe project pages;
Weber, *United States Diplomatic Codes and Ciphers*, and Tomokiyo's WE028 page. JSTOR rows to JSTOR-QUEUE.tsv in both
families (never blocks N3/N4).
3: N-class with the key-source field (`published`: Tomokiyo's modern transcription of the period table, credited -- argue
`period` instead only if you find reason), prior plaintext, prior decipherment, safe and unsafe sentence.
3a: depth D0-D4 (rule 4a) with the check used; set it yourself (34 groups, 105 letters, two clauses).
4: correct any over-claiming sentence in the folder. 5: write AUDIT.md, append the SECOND-OPINIONS-QUEUE.tsv row in the
same session if N3+, `tools/file_shrink_guard.py` on every touched file, commit by explicit path, push.
Do not decode, do not touch other targets, do not print credentials, never use AskUserQuestion. Never the words
solved, cracked, novel, first, new for anything this project did. Report request counts per host.
