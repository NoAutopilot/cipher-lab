# Check Solved (Sonnet, cap $5 per target; the workflow check-solved.js when opted in)
Six blind searchers (web, print, community lists, DECODE, Bourdeau, Aymeloglu) and a reconciler. Each
searcher lists every query and URL; found=true only for a real solution, key, plaintext or documented
attempt with a status. Verdict appended to NOTES.md with the date. + common tail.
When a calendar or edition is unreachable (HathiTrust 403, paywall), do not log it as unreachable and move on: run
the HTRC Extracted Features word-count test (`tools/htrc_ef_headwords.py`, or the ef-api pages call) for the item's
names, dates and folio numbers, and treat a page that carries them as a probable calendar entry. Lesson of 23 Sept
2026 (Bowes 1583): stage 2 was set while CSP Scotland vi no. 389 calendared the very leaf with every cipher name in
clear. Editions first, and the leaf viewed before scoring (d'Avaux 1633).
A found-solved verdict states who did not know, as README's F0/F1/F2, and what correction or key it leaves to hand on.
