LANE R6 S0 -- CHECK-SOLVED, fr2933-salviati-1525 (Sonnet, cap $4, box 40 minutes). Common: 2026-09-25-lane-r6-common.md.
Why: `tools/intake_gate_check.py fr2933-salviati-1525` exits 1 (live output, 25 Sept 15:42 UTC): "open (line 1) with no standard-edition
citation (page number or full-text-search phrase) within 6 lines -- ... must read `blocked` instead". The 24 Sept verdict left one real gap:
Desjardins/Canestrini, Négociations diplomatiques de la France avec la Toscane, tome II (1525) was never full-text searched. No leaf work
starts on this target until the gate passes.
Job, per `.claude/briefs/check-solved.md`: (1) Desjardins Toscane II (and I if 1525 falls there): full text on archive.org (djvu txt or
be-api fts), grep Salviati, "16 octobre 1525", "XVI octobris", "chiffre"; control word to prove the OCR reads. (2) Printed Salviati
legation/nunciature letters of 1525-26 (e.g. Lettere di principi; Balan, Monumenta reformationis/saeculi XVI; any Nunziature di Spagna
volume; Castiglione's Lettere, as he was nuncio in Spain at the same time): find what is on archive.org / Google Books (key + &country=US)
and full-text search for the date and for a letter from Salviati in October 1525. (3) The model-solve announcement search (check-solved.md).
Write the verdict at the top of ciphers/fr2933-salviati-1525/NOTES.md in the check-solved form: status word alone on line 1, line 2 the one
sentence naming the edition(s) and pages or phrase search THIS worker read; a new section "## Check-solved (LANE R6 S0, 25 Sept 2026)" with
the query log. If the letter or its decipherment is in print, the status is found-solved (say F0/F1/F2). If an edition cannot be opened, the
status is blocked with what blocked it. Then run `python3 tools/intake_gate_check.py fr2933-salviati-1525` and paste its output into your section.
Hosts: archive.org, be-api.us.archive.org, googleapis.com (Books), web search. Not Gallica. ROOM done: "for LANE R6: salviati gate <exit>".
