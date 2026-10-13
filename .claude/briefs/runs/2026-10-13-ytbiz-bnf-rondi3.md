# BNF-RONDI3 (Sonnet worker for LANE BNF-FOCUS, account 2 / ytbiz), 13 Oct 2026

Job: close the two check-solved gaps left on `ciphers/fr3613-rondinelli-1590` (Hercole Rondinelli to the duc de Nevers,
Paris, 11 Nov 1590, BnF fr.3613 no.33 f.62, a symbol cipher in Italian), nothing else: no transcription, no decode.
Cap USD 2, box 45 min. Units: blogs (~0.6), fr.3995 table screen by catalogue + up to 4 images (~0.8), write-up (~0.4).
Model: Sonnet.

Read first: CLAUDE.md (rules 1, 5, 6, 10; good-citizen rule), `.claude/briefs/check-solved.md` (the "## Web and blog check"
section), the folder's NOTES.md (BNF-Q13-CS, BNF-GOMB, BNF-RONDI, BNF-RONDI2), last 30 lines of ROOM.md.

Steps
1. ROOM claim (tools/room.py, single quotes) with box end and cap.
2. The three blogs, each searched on its own and logged with query, URL and hit count: Cipherbrain (Klaus Schmeh), the
   Cryptiana blog (local snapshot sources/cryptiana/blog/ first, then the live search once), Cipher Mysteries (Nick Pelling).
   Terms: Rondinelli, Rondinello, "Hercole" + Nevers, fr.3613, "3613". Comment threads count (check-solved.md).
3. Recipient-side tables: from Tomokiyo's fr.3995 catalogue (sources/cryptiana/web/nevers.htm) list every table dated
   1589-1591 that is a SYMBOL cipher or says Italian / Florence / Paris agent, with its folio; for at most the two best
   matches, fetch the table image once via `https://openapi.bnf.fr/iiif/image/v3/ark:/12148/btv1b525085665/f<N>/full/1600,/0/default.jpg`
   (never gallica.bnf.fr; <= 4 requests, 3 s apart) and compare its sign shapes by eye with f.62 (images on disk in the
   folder, or one openapi fetch of fr.3613 canvas 69 via its own ark btv1b90582263). Report: table, folio, shape match
   yes / partial / no, graded M. This is a key lead for later, not a check-solved source; record it under "## While waiting".
4. NOTES.md section "## BNF-RONDI3 (13 Oct 2026, account 2)". Line 1 per `.claude/briefs/check-solved.md`: if no blog or
   other source reports a decipherment and the edition step stands (Gomberville seconde partie read, BNF-GOMB + BNF-RONDI2),
   set `open` with line 2 naming the edition and pages read; paste `python3 tools/intake_gate_check.py fr3613-rondinelli-1590`.
5. Commit by explicit path, `tools/file_shrink_guard.py` on touched files, push (`tools/room.py --push <paths>`), ROOM done
   line "for LANE BNF-FOCUS (account 2)": verdict, blog hits, table lead, gate exit, requests per host.

Report what was found and where it was not found; do not classify novelty (rule 10). Never print credentials. Never the
words solved, cracked, novel, first, new for anything this project did. Never call AskUserQuestion. If `tools/room.py
--start` fails to push from a detached HEAD: `git push origin HEAD:main; git checkout -B main HEAD`.
