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
When Tomokiyo's page, a solver repository's README, or any other named source in the search log identifies
the specific letter under review (by date, sender, recipient or shelfmark, not just the cipher family),
quote its sentence about that letter verbatim in the verdict before writing "open". Lesson of 24 Sept 2026
(M9, fr.2996 Morvillier): the worker had Tomokiyo's page open and still wrote "open", though the page says
Lasry broke that very letter in 2023 (RETRO-2026-09-24 proposal 3).
