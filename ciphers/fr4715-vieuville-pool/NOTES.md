open
BnF dépouillement of Français 4715 (archivesetmanuscrits.bnf.fr ark:/12148/cc577658, item 44, folio 67: "Lettre, avec chiffre, du Sr DE MONTHOLON. Tours, 15 avril 1590.") read by this worker from the cached notice in a fresh shallow clone of dbourdeau/cyphersolver (research/gallica_sweep/notice_cc577658.html and notice_cc577658_cd0e531.html, 2 Oct 2026); Tomokiyo's bnf4715.htm and nevers.htm (local mirror, cp932) read in full and grepped for no.44 / f.67 / "15 April 1590" (nevers.htm lists the item under the Vieuville-Nevers Cipher heading with no reading; bnf4715.htm has no no.44 section); Desenclos and Lasry, "An early French digit cipher: deciphering a letter from the King of France to the Duke of Nevers (1592)" (HistoCrypt, dspace.ut.ee PDF, 54 kB of text) grepped in full text: 0 hits for 4715, Montholon named twice as a digit-cipher user, no 1590 Montholon letter printed.

# BnF fr.4715 Vieuville-Nevers open sub-pool -- first cheap test on no.44 (f.67r), Montholon, Tours, 15 April 1590

Sibling of `ciphers/fr4715-montholon-1589` (no.58, f.81r). Pool register: `ciphers/fr4715-montholon-1589/POOL.md`
(CS-4715-POOL, 27 Sept 2026): 8 open/partial single-leaf letters in the same hand and key family -- no.21 f.44,
no.27 f.50, no.28 f.51, no.35 f.58, no.37 f.60, no.39 f.62, no.44 f.67, no.60 f.83 -- about 10,600 signs besides
no.58's 2,524. Key of record: `ciphers/fr4715-montholon-1589/keys/key_vieuville_nevers.tsv` (Tomokiyo's printed
Vieuville-Nevers table, nevers.htm; 35 rows, 33 numeric letter-homophones plus two glyphs; no j, k, v, w, z;
dotted groups are an undocumented word-code layer). This folder covers the pool's leaves other than no.58; each
leaf gets its own section, ciphertext file and reading. Row: `ciphers/_triage/likely-solves-2026-10-02.tsv` rank 1
(brief `.claude/briefs/runs/2026-10-02-account4-likely-phase2.md`).

Source image: Gallica ark:/12148/btv1b52509819x, canvas f149, manifest label '67r' (`tools/gallica_folio.py`,
cached manifest, no request), 4079x5720 native. Region 300,900,3500,4820 fetched once at native resolution
(`images/manifest.json`; 1 request to gallica.bnf.fr, 03:40 UTC 2 Oct 2026). The leaf is 32 lines of clear French
in a secretary hand with numeral cipher groups in the running text, the date line "ce 15 apuril a cinq heures du
soir" at the foot of the text block, and blank paper below (band 33 of the row profile is the blank lower leaf).

## Check-solved (LIKELY-1, 2 Oct 2026, account-4; minimal, per the brief's step 2)

1. BnF dépouillement, item 44: "Fol. 67 • 44 Lettre, avec chiffre, du Sr DE MONTHOLON. Tours, 15 avril 1590." --
   "avec chiffre" and nothing else, unlike the "en partie déchiffrée" and "Chiffre et déchiffrement" rows around
   it (items 21, 27-28, 35, 37, 39, 45-46, 47-48). No period decipherment is recorded for this leaf. Read from the
   cached notice in the fresh `dbourdeau/cyphersolver` clone (research/gallica_sweep/notice_cc577658.html, line
   "Fol. 67 • 44 ..."); a WebFetch of the live record (ark:/12148/cc577658/cd0e531) answered HTTP 403 this session,
   1 request, not retried.
2. Tomokiyo: `sources/cryptiana/web/nevers.htm` lists "no.44 (f.67) Letter of Montholon, Tours, 15 April 1590"
   under the Vieuville-Nevers Cipher heading with no status sentence and no reading; `bnf4715.htm` has no `no44`
   section (both files decoded cp932 and grepped, 0 hits for a reading).
3. Solver repositories, fresh shallow clones 2 Oct 2026 (grep `4715|montholon|vieuville|trespigny|52509819`):
   `dbourdeau/cyphersolver` -- hits only in research/gallica_sweep (the cached BnF notice and SRU results, the
   nevers/bnf4715 page mirrors), targets/r2276 (fr.4715 f.2 used as a reference alphabet image, a different
   cipher) and targets/nevers1589 (fr.3977, intercepts for Nevers 1589); no folder, key or reading for no.44, and
   SOLVED_CATALOGUE.md's Montholon row (POOL.md quotes it) names nos. 19, 27, 37, 47, 48, 58, 60, 62 only.
   `aaymeloglu/unsolved-ciphers` -- the only `4715` match is DECODE record id 4715 (Marburg, 1715), unrelated; no
   Montholon hit.
4. Scholarship: Desenclos and Lasry (HistoCrypt, "An early French digit cipher ... (1592)", dspace.ut.ee) -- full
   text grepped: 0 x "4715"; "Montholon" twice (digit ciphers "used by the French Monarchy (like Montholon or La
   Vieuville ...)"); the one 1590 Montholon item they cite is unrelated. Bourdeau PR #9 (fr.3977 no.96, Nevers
   intercepts 1589) read via WebFetch: no fr.4715, no April 1590, no folio 67.
5. DECODE: the 24 Sept 2026 cached crawl (POOL.md step 4) has no fr.4715 row; not re-crawled.

## Web and blog check (LIKELY-1, 2 Oct 2026)

Plain web searches (4): `Montholon Nevers 1590 lettre chiffre Tours "15 avril 1590"` -- hits: the BnF finding aid
(cc577658 and its cd0e531 item page, the catalogue entry above), Wikipedia pages; `"fr. 4715" OR "français 4715"
BnF chiffre Montholon Vieuville Nevers` -- the same finding aid, fr.4716, fr.3974-3995, fr.3623 notices; `"Vieuville-
Nevers" cipher Montholon 1589 decipherment` -- the Desenclos-Lasry PDF (opened, item 4 above), Bourdeau PR #9
(opened), dbourdeau.github.io index, an aryasn2026 fork of cyphersolver (same content), Wikipedia; `Montholon garde
des sceaux Ligue lettres 1589 1590 duc de Nevers correspondance chiffrée édition` -- BnF notices fr.3616, fr.3416
(a Montholon letter of 20 Jan 1590), fr.3623 (10 Aug 1590), fr.4715, and the Archives nationales Montholon-Sémonville
fonds (34 letters to Montholon 1588-89); none prints a reading of f.67.
Blog site searches (3): Cipherbrain / klausis-krypto-kolumne (scienceblogs.de): 0 hits for Montholon, Nevers or
4715. Cryptiana blog (cryptiana.blogspot.com): the 30 Nov 2018 post "Unsolved ciphers in the French archives
(ca.1586-1593)" names BnF fr.4715 as containing undeciphered material; opened, "No comments" -- 0 comments, no
decipherment. Cipher Mysteries (ciphermysteries.com): 0 hits (the only match is an unrelated 1715 Vieuville
genealogy post).
Verdict of the check: no decipherment or plaintext of fr.4715 no.44 (f.67) located in any of the above; a search
result (rule 10), not a novelty verdict. Status `open`.
