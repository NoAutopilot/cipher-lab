# Check Solved (Sonnet, cap $5 per target; the workflow check-solved.js when opted in)
Six blind searchers (web, print, community lists, DECODE, Bourdeau, Aymeloglu) and a reconciler. Each
searcher lists every query and URL; found=true only for a real solution, key, plaintext or documented
attempt with a status. Verdict appended to NOTES.md with the date. + common tail.
A verdict of `open` is written only in the same sentence as the edition (or calendar) read and the page(s)
checked, e.g. "open -- Ribier 1666 vol.2 pp.140-145 read, letter absent." A verdict with no edition named in
it defaults to `blocked`, never `open` (RETRO-2026-09-24e: csCS2a and csCS2c both posted "open" rows with the
edition unread despite the same rule already stated in the LANE N COMMON tail -- a rule read once at claim
time does not survive a five-row batch; putting it in the verdict sentence itself makes the gap visible to
whoever reads the row).
For a target from the Trew Briefsammlung, a physician's correspondence, or any German/Latin medical-humanist
collection, add aerztebriefe.de (Schlagwort "Geheimschrift") as a seventh search before scoring. Lesson of 24
Sept 2026 (Posthius to Eysenmenger 1614/1618): the six standard sources missed a listed decipherment there;
a solver read both letters (H96 M13, $1.79) before a verifier found both N0 (RETRO-2026-09-24e).
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
When an edition prints a cipher as unsolved ("key lost", "olöst", "left undeciphered", "not deciphered", or a
footnote saying the key could not be found), search the national or period historical journal(s) and the
learned-society proceedings for the five years after that volume appeared, by the edition's title, the letter's
number, date and the words "cipher/chiffer/chiffre" — an editor who could not find the key often published it
later, in that journal, from other letters of the same cipher. Then run a phrase search on the decoded text
(`tools/print_check.py`), in both normalised and period spelling, before scoring it open or reporting a verdict.
Lesson of 24 Sept 2026 (Gustav II Adolf to Oxenstierna, 23 July 1632, oxenstierna-gustav-adolf-1632 letter 602):
Torpadie printed the solution in Historisk tidskrift 8 (1888), the year the edition appeared; check-solved and a
solver both ran, and a key hunt and an original-letter hunt also took the footnote at face value, before a
verifier found it on the fourth phrase-search query, an hour after a fresh reading had already been posted
(LEDGER row "Verifier: Gustav II Adolf"; AUDIT.md, "Postmortem").
Before scoring an archive item open, search the holding collection as a whole (not just the item's record) for a
duplicate, triplicate, draft or copy of the same letter: senders sent ciphered dispatches in duplicate, and the
recipient often deciphered only one. Lesson of 24 Sept 2026 (Huntington mssDE 108(A), La Luzerne to Destouches,
16 Jan 1781): its 'Duplicata' mssDE 108(B), deciphered by Destouches, sat in the same collection; two solver sessions
rebuilt a partial key before a verifier's collection-wide CONTENTdm query found it (LEDGER row "Verifier: Luzerne").
When Tomokiyo's page, a solver repository's README, or any other named source in the search log identifies
the specific letter under review (by date, sender, recipient or shelfmark, not just the cipher family),
quote its sentence about that letter verbatim in the verdict before writing "open". Lesson of 24 Sept 2026
(M9, fr.2996 Morvillier): the worker had Tomokiyo's page open and still wrote "open", though the page says
Lasry broke that very letter in 2023 (RETRO-2026-09-24 proposal 3).

For a letter from the Willem van Oranje database (WVO, resources.huygens.knaw.nl/wvo), read the record's
Brongegevens line before writing a verdict: code GPA means printed in Groen van Prinsterer's Archives (GPAS its
Supplément), JC means Japikse's Correspondentie. Open the cited page and check whether the cipher passage is printed
in clear (Groen printed 5200, 5218, 5222, 4503 and 5811 with their cipher passages deciphered; Japikse prints the
deciphered insertions in spaced type, as in 8246). Lesson of 24 Sept 2026: three lanes captured and read five WVO
letters that were already in print, because the harvest treated the source codes as "inferred".
