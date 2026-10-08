# BNF-SEGA-POOL (Sonnet worker for LANE BNF-FOCUS, account 2 / ytbiz), 8 Oct 2026

Job: check-solved + premise check for a pool of three numeric cipher pieces around Filippo Sega (bishop of Piacenza,
cardinal from 1591, papal nuncio/legate in France), settling the edition question with instruments the two earlier
passes did not use. Cap USD 5, box 60 min from your claim. Do not transcribe, decode or class.

Read first: CLAUDE.md (rules 1, 5, 6, 10; Access playbook), `.claude/briefs/check-solved.md` (line-2 citation rule,
intake gate, Premise check), `ciphers/fr3613-sega-caetani-1591/NOTES.md` (BNF-Q13-CS and BNF-SEGA-ED sections: what was
already searched -- do not repeat it), BNF-VALUE.md last ITERATE row.

Pool:
A. `ciphers/fr3613-sega-caetani-1591/` -- fr.3613 no.88 f.148v, Sega to Cardinal Caetani, Paris, 9 Jan 1591 (exists).
B. new `ciphers/fr3984-sega-memoirs-1593/` -- BnF Français 3984 no.6, ff.12-19, "Mémoire, en chiffre, adressé al sigr
   cardinale di Piacenza ... 14 maggio 1593" (Tomokiyo league.htm: "Entirely enciphered in Arabic figures.
   Undeciphered, except for the date and the recipient in the margin in Italian. See another article in Cryptologia")
   and no.8, f.22, "Lettre, en chiffre. Di Parigi, li 15 di maggio 1593" (Tomokiyo: "Fully enciphered in Arabic
   figures. Undeciphered. Continuous stream of figures. There are crossed 2, 6 and 9 as well as 0 with an overdot").
   Gallica btv1b9060633d (canvas ~ 2 x folio - 26 in this stretch per Bourdeau). Bourdeau: catalogue item 20 lists
   nos.6 and 8; his targets/sega1593/NOTES.md examined only ff.186/189 -- confirm from a fresh clone that nos.6/8 were
   never attempted.

New instruments (each logged as searched/unreachable, with what was searched):
1. Tomokiyo's Cryptologia article that league.htm points to for nos.6/8: identify it (OpenAlex/S2/CrossRef with keys;
   Tomokiyo's own pages, sources/cryptiana/web/ and the live cryptiana.web.fc2.com index) and read its abstract and any
   open version: does it decipher nos.6/8 or present them as unread? Its findings decide B's verdict.
2. The complete volume list of Acta Nuntiaturae Gallicae from the series' own publisher page (Éditions de l'École
   française de Rome / Gregorian Biblical Press) -- is there a Caetani 1589-90 or Sega 1591-93 volume?
3. The chapter BNF-SEGA-ED named (Penzi, Classiques Garnier): its footnotes or bibliography for any edition of Sega's
   French nunciature; and the Dizionario Biografico degli Italiani entries "SEGA, Filippo" and "CAETANI, Enrico"
   (treccani.it), whose bibliographies list the editions of their correspondence.
4. Mémoires de la Ligue (Goujet 1758) and Lettres de Henri IV for 14-15 May 1593 / 9 Jan 1591 pieces (IA full text).
5. Gallica: one low-res look at fr.3984 f.12 and f.22 (premise (c): any gloss or decipherment), at most 10 requests.
Verdicts: per piece on NOTES.md line 1 (open / found-solved / blocked), line 2 naming what this worker read. If the
publisher's list and the DBI bibliographies show no edition of these letters exists, `open` is the honest verdict --
say exactly that on line 2. Run `python3 tools/intake_gate_check.py` on both folders and paste the output.

Close: commit by explicit path including the new folder, push with tools/room.py --push, tools/file_shrink_guard.py on
touched files, ROOM done line "for LANE BNF-FOCUS" with verdicts, gate exit codes, requests per host. Report what was
found and where it was not found; do not classify novelty. Never print credentials. Never the words solved, cracked,
novel, first, new for anything this project did. Never call AskUserQuestion. If tools/room.py --start fails to push
from a detached HEAD: git push origin HEAD:main; git checkout -B main HEAD.
