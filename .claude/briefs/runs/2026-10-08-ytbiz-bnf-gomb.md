# BNF-GOMB (Sonnet worker for LANE BNF-FOCUS, account 2 / ytbiz), 8 Oct 2026

Job: finish the check-solved of two blocked folders by reading the standard edition for the right months, with a
different instrument from the one that left them blocked. Two units at ~$1.5; cap USD 4, box 50 min from your claim.
Do not transcribe, decode or class.

Read first: CLAUDE.md (rules 1, 5, 6, 10; Access playbook, Gallica row), `.claude/briefs/check-solved.md` (line-2
citation rule, intake gate), both folders' NOTES.md (what BNF-Q13-CS already searched -- do not repeat it).

Units:
1. `ciphers/fr3613-rondinelli-1590/` -- Hercole Rondinelli to Nevers, Paris, 11 Nov 1590 (BnF fr.3613 no.33 f.62).
2. `ciphers/fr3622-nevers-gondi-1594/` -- Nevers to "Mr de Gondy", Veze, 27 Mar 1594 (BnF fr.3622 no.45 f.91).
Edition: Gomberville (ed.), *Les Mémoires de Monsieur le duc de Nevers* (1665), seconde partie -- Gallica
bpt6k64451005 (fr3986-nevers-revol-1593/NOTES.md used its ContentSearch from the cloud). Steps:
a. Gallica ContentSearch on bpt6k64451005 for: Rondinelli, Rondinel, Gondy, Gondi, Veze, Vezé, "1590", "1594", and
   the clear words nearest the cipher on each leaf if visible at low res (one look per leaf at most).
b. Locate the volume's order (its table or the dated pieces around the hits) and read the pages covering Oct-Dec 1590
   and Feb-Apr 1594 (Gallica page text via the ContentSearch hit pages or the IIIF images of those pages, not the
   texteBrut endpoint, which needs a local browser). Is either letter printed, in clear or deciphered?
c. Also check the première partie only if its table reaches 1590 (bpt6k6435941k).
Per unit: verdict on line 1 (open / found-solved / blocked), line 2 naming the pages read; `python3
tools/intake_gate_check.py <folder>` pasted into NOTES.md. Gallica requests at most 40, 1.5 s apart; on a challenge
or reset, one retry after a pause, then stop and log it.

Close: commit by explicit path, push with tools/room.py --push, tools/file_shrink_guard.py on touched files, ROOM done
line "for LANE BNF-FOCUS" with verdicts, gate exit codes and requests per host. Report what was found and where it was
not found; do not classify novelty. Never print credentials. Never the words solved, cracked, novel, first, new for
anything this project did. Never call AskUserQuestion. If tools/room.py --start fails to push from a detached HEAD:
git push origin HEAD:main; git checkout -B main HEAD.
