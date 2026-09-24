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
Before scoring a printed-cipher item as open, or handing it to extraction or a solver, check whether the same
edition prints a decipherment on the facing page or between the cipher's lines (an interlinear gloss, a
"deciphered" heading, or a translation printed immediately after). Lesson of 24 Sept 2026 (Thurloe P11-13,
Montagu 1656): Birch's 1742 edition prints the decipherment above every cipher line for this correspondent;
check-solved and extraction both missed it and a solver had to find it (RETRO-2026-09-24b, LEDGER row "Solver:
Thurloe P11-13 Montagu 1656"), the same shape as Raince/Jacqueton and Dupuy 468/RTA JR II the same week. A
series known to carry interlinear decipherments for some letters (Thurloe/Birch, any calendar that prints
"deciphered") gets this check on every letter in it, not only the one that happened to be checked already.
When an edition prints a cipher as unsolved ("key lost", "olöst", "not deciphered"), search the national historical
journal and the learned-society proceedings for the five years after that volume appeared, by the letter's number,
date and the words "cipher/chiffer/chiffre", before scoring it open. Lesson of 24 Sept 2026 (Gustav II Adolf to
Oxenstierna, 23 July 1632, W1): Torpadie printed the solution in Historisk tidskrift 8 (1888), the year the edition
appeared; check-solved and a solver both ran before a verifier found it (LEDGER row "Verifier: Gustav II Adolf").
When Tomokiyo's page, a solver repository's README, or any other named source in the search log identifies
the specific letter under review (by date, sender, recipient or shelfmark, not just the cipher family),
quote its sentence about that letter verbatim in the verdict before writing "open". Lesson of 24 Sept 2026
(M9, fr.2996 Morvillier): the worker had Tomokiyo's page open and still wrote "open", though the page says
Lasry broke that very letter in 2023 (RETRO-2026-09-24 proposal 3).
