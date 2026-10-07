# BNF-Q13-CS (Sonnet worker for LANE BNF-FOCUS, account 2 / ytbiz), 8 Oct 2026

Job: check-solved + premise check only, three BnF letters in two digitised volumes, plus one key-availability look.
Four units at ~$1.5 each; cap USD 6, box 70 min from your claim; stop before starting a unit that would cross 80% of
either. Do not transcribe, decode or class (rule 10).

Read first: CLAUDE.md (rules 1, 5, 6, 9, 10; Access playbook), `.claude/briefs/check-solved.md` (whole file),
`.claude/briefs/README.md` common tail, BNF-VALUE.md section 3 (ITERATE rows of 7 Oct and the "Next best attempt"
line), ROOM.md last 30 lines. Search D. Bourdeau's github.com/dbourdeau/cyphersolver (fresh shallow clone, grep
README.md, CATALOGUE.md, targets/) and Tomokiyo's pages (sources/cryptiana/web/) FIRST: two of the last four queue
rows were already read there or in print (Bourdeau sessa1593; Desenclos and Lasry 2024).

BnF record text: `sources/bnf-findingaids/2026-10-07/` (parse with `python3 tools/bnf_findingaid.py --html <file>`).

## Units (one folder per letter; status word alone on NOTES.md line 1)
1. `ciphers/fr3613-sega-caetani-1591/` -- BnF Français 3613 no.88, fol. 148: "Lettre, avec chiffre, de FILIPPO SEGA,
   vescovo di Piacenza ... all' illmo ... Sor cardinale Caetano ... Di Parigi, li 9 di gennaro 1591". En italien.
   Gallica btv1b90582263 (link from the BnF notice). Tomokiyo (polyalphabetic.htm): Caetani's legation cipher of
   28 Sept 1589 is printed in Meister, *Die Geheimschrift im Dienste der päpstlichen Kurie* (1906), p.420; Tomokiyo
   also reconstructed a Mayenne-Sega cipher of Jan 1591 (Cryptologia, "How I reconstructed a Spanish cipher from
   1591") -- say which (if either) this letter's signs look like at low resolution, without decoding.
   Editions: Nuntiaturberichte / Acta Nuntiaturae Gallicae for Sega's 1590-91 mission (check what exists and is
   online), Meister 1906 itself (archive.org full text).
2. `ciphers/fr3613-rondinelli-1590/` -- same volume, no.33, fol. 62: "Lettre, avec chiffre, du Sr HERCOLE RONDINELLI
   au duc de Nevers. Di Parigi, il di XImo di 9bre 1590". Gomberville *Mémoires de Nevers* seconde partie
   (Google Books H2eV4wAmIr0C, tools/gbooks_search_within.py) for Nov 1590.
3. `ciphers/fr3622-nevers-gondi-1594/` -- BnF Français 3622 no.45, fol. 91: "Lettre, avec chiffre, de L[ODOVICO]
   G[ONZAGA, duc DE NEVERS] ... à Mr de Gondy ... De Veze, ce XXVIIe mars 1594". Gallica btv1b9058938q. Check the
   Nevers-Revol/no.60 folders (fr3985-..., fr3986-...) and KEYHUNT-2026-10-07.tsv: Nevers's 1593-94 Italian-journey
   copies may share key no.60.
4. Key availability (no folder): is Meister 1906 on archive.org / HathiTrust full view, and does p.420 print a full
   table? One line in each of units 1's NOTES.md.
For each letter: canvas via `tools/gallica_folio.py ARK --folio N`, one low-res look (cipher present? any interlinear
or marginal decipherment = premise (c)); at most 20 gallica.bnf.fr requests total, 1.5 s apart.

## Close
Per unit: verdict on line 1, line-2 citation of the edition this worker read, `python3 tools/intake_gate_check.py
<folder>` pasted into NOTES.md. Commit by explicit path including new folders, push with tools/room.py --push,
tools/file_shrink_guard.py on touched files, one ROOM done line "for LANE BNF-FOCUS" with verdicts, gate exit codes,
requests per host.

Report what was found and where it was not found; do not classify novelty. Never print credentials. Never the words
solved, cracked, novel, first, new for anything this project did. Never call AskUserQuestion. If tools/room.py --start
fails to push from a detached HEAD: git push origin HEAD:main; git checkout -B main HEAD.
