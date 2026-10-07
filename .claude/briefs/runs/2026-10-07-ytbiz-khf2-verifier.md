# KHF-2 verifier (account ytbiz for acct3-orchestrator, 7 Oct 2026, written by KHF-2 worker session_01Y8ZhnFiRmJqcV5pQK87fP4)
Opus 5.5. Cap USD 4, box 50 min from your claim (stop before starting a step that would cross 80% of either).
Read CLAUDE.md (rules 3, 4, 4a, 10; Workers "Verifier brief (template)") and the target's NOTES.md in full first.
`python3 tools/room.py --start`; if it cannot push from a detached HEAD: `git push origin HEAD:main; git checkout -B main HEAD`.
ROOM claim first (box end time), done line at the end addressed "for acct3-orchestrator".

VERIFIER: ciphers/wvo-11008-certain-1572. Claim under audit (NOTES.md "Reading under the held key"): five numeral runs
in WVO 11008 (Orange as "George Certain" to Lodewijk as "Lambert Certain", Keulen 12 Aug 1572, KHA A 11/XI 15) read
under the printed 1572 Orange-Nassau table as "le duc de holstein", "ermuyden" (Arnemuiden) and "ulgssinghen"
(= vlissinghen, one code off); 54 tokens H39 M15; key-permutation control passed (4-gram -1.435 vs shuffle p95
-1.576, 6/1000); fr16 judge FAIL at N=39.
1-5: the template steps exactly (extract; search families (a)-(g) incl. a phrase search on the decoded words in their
clear-text context, e.g. "duc de holstein" with "2000 escus"/"faict charge", Arnemuiden/Vlissingen August 1572;
the solver's own log is in NOTES.md "Check-solved (KHF-2...)" and "Where it was not found" -- do not trust it, re-run
what matters). Cover also: Gachard's Correspondance de Guillaume le Taciturne and Correspondance de Philippe II (Spanish
side intercepts), Kervyn de Lettenhove, the Waanders 2022 "Willem van Oranje in brieven. De Opstand in 1572" ToC if you
can reach it, and any literature on the Orange-Nassau 1572 cipher table (ciphers/jan-van-nassau-1572-75,
ciphers/orange-nassau-1572 NOTES/AUDIT name the table's source). JSTOR rows to JSTOR-QUEUE.tsv in both families
(never blocks N3/N4).
3: N-class per item (the letter's three name readings as one item is fine) with the key-source field (`period`: the
table is a period key rebuilt from print), prior plaintext, prior decipherment, safe and unsafe sentence.
3a: depth D0-D4 (rule 4a) with the check used; the solver expects D1 (names only, no clause) -- set it yourself.
4: correct any over-claiming sentence in the folder. 5: write AUDIT.md, append the SECOND-OPINIONS-QUEUE.tsv row in the
same session if N3+, `tools/file_shrink_guard.py` on every touched file, commit by explicit path, push.
Do not decode, do not touch other targets, do not print credentials, never use AskUserQuestion. Never the words
solved, cracked, novel, first, new for anything this project did. Report request counts per host.
