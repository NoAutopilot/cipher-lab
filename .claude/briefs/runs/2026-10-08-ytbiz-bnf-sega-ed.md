# BNF-SEGA-ED (Sonnet worker for LANE BNF-FOCUS, account 2 / ytbiz), 8 Oct 2026

Job: one question, for `ciphers/fr3613-sega-caetani-1591/` (BnF Français 3613 no.88, f.148v: Filippo Sega, bishop of
Piacenza, to Cardinal Enrico Caetani, Paris, 9 Jan 1591, Italian, ~200 cipher digits). Does ANY printed or online
edition print (or calendar) Sega's letters of 1590-91 from Paris, or the letters Caetani received as legate in France
(1589-90) and after? Cap USD 4, box 50 min from your claim. Do not transcribe, decode or class.

Read first: CLAUDE.md (rules 1, 5, 6, 10), `.claude/briefs/check-solved.md` (the line-2 citation rule and the intake
gate paragraph), the folder's NOTES.md (BNF-Q13-CS's verdict `blocked`: "no printed edition of Sega's 1590-91 letters
could be opened"), BNF-VALUE.md ITERATE row of 8 Oct. Note: Sega was nuncio in France 1591-92 after Caetani's
legation; check both men.

Search (log every query and result in a section "## Edition search (BNF-SEGA-ED, 8 Oct 2026)"):
1. The Acta Nuntiaturae Gallicae series' own volume list (Gregorian University Press / École française de Rome): is
   there a volume for Caetani 1589-90 or Sega 1591-92? Nuntiaturberichte aus Deutschland (Sega was nuncio in Germany
   1586-87, a different mission -- note it, do not confuse). Ehses' work on the 1589 legation (Meister 1906 cites
   "Ehses, Nuntiaturberichte I, 2, S. LX").
2. OpenAlex and Semantic Scholar with the keys (CLAUDE.md access playbook), Google Books API (key + country=US),
   Persée, HAL, Internet Archive advancedsearch + be-api full text: "Sega" + "Caetani"/"Caetano" + 1591; "legazione
   Caetani"; "nunziatura di Francia" 1591; Pastor, Geschichte der Päpste X-XI appendices (documents printed);
   Richard, "La légation du cardinal Caetani en France" (if it exists); Lettres de Henri IV / Mémoires de la Ligue
   (Goujet 1758) for a 9 Jan 1591 Sega letter.
3. Phrase/date check: any work quoting a Sega letter "di Parigi, li 9 di gennaro 1591".
Verdict rule: if an edition exists and is reachable, read it for 9 Jan 1591 and give open/found-solved with the
line-2 citation; if one exists but is unreachable, stay `blocked` naming it (LOCAL-QUEUE row only after
`tools/key_livecheck.py` per CLAUDE.md); if, after the log above, no edition of these letters exists, set `open`
with line 2 naming exactly what was checked ("no edition of Sega's 1590-91 Paris letters exists: checked <list>").
Run `python3 tools/intake_gate_check.py fr3613-sega-caetani-1591`, paste the output in NOTES.md.

Close: commit by explicit path, push with tools/room.py --push, tools/file_shrink_guard.py on NOTES.md, ROOM done line
"for LANE BNF-FOCUS" with the verdict, gate exit code and requests per host. Report what was found and where it was not
found; do not classify novelty. Never print credentials. Never the words solved, cracked, novel, first, new for anything
this project did. Never call AskUserQuestion. If tools/room.py --start fails to push from a detached HEAD: git push
origin HEAD:main; git checkout -B main HEAD.
