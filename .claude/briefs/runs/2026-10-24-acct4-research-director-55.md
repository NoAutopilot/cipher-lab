# Research director, wave 55 (24 Oct 2026, 20:2x UTC by date -u): key-beside-cipher scout on DigitArq / ANTT (a host that serves images today)

Common tail .claude/briefs/README.md applies (ROOM claim/done with the usage phrase, wall-clock box, no AskUserQuestion, never a dollar
figure for yourself). Done line addressed for the account-4 parent. Gallica is not involved.

## JOB SCOUT-ANTT (account 4; Sonnet 5; cap USD 5; box 45 minutes; hosts: digitarq.arquivos.pt only through tools/digitarq_fetch.py (>=3 s apart, <=120 requests, CLAUDE.md host table row), archive.org full text (<=10) for the edition step; no images fetched beyond thumbnails needed to tell a key sheet from a letter (<=6 small images, kept in the scratchpad); Price: vision calls: 6 x USD 0.5 = 3)

Program C. This week's key-beside-cipher scouts (QUEUE.md sections dated 17-24 Oct 2026: "Key-beside-cipher candidates", "... non-BnF
(SCOUT-KEYS2)", "Fagel key register (SCOUT-FAGEL)", "Open-route candidates (SCOUT-OPEN)") covered TNA, the Nationaal Archief, LoC,
archive.org, Europeana/DPLA and DECODE's SP 106/6 keys; every hit was physical-only. DigitArq (ANTT) serves full working-resolution
images from the cloud and produced this project's one Portuguese reading (antt-linhares-chave: a key leaf beside the letters). Run
the same filter there: a candidate counts only if (a) a key, decipherment, gloss or clear copy is on file or in reach for it, AND
(b) the cipher item itself has NO surviving period decipherment and NO printed plaintext you can find.
1. Read first QUEUE.md's "Portuguese holdings" and "PARES / DigitArq cipher letters" sections and ciphers/antt-linhares-chave/NOTES.md
   (how the key leaf was found and what DigitArq's API really does -- the search endpoints ignore their own parameters; use the
   routes the tool docstring gives). List every ANTT fonds already scouted so you do not repeat them.
2. Catalogue sweep with tools/digitarq_fetch.py for "cifra", "chave da cifra", "cifrada", "em cifra", "decifra", "alfabeto" across
   the fonds the tool can search (Corpo Cronológico, Gavetas, Manuscritos da Livraria, Conselho de Guerra, MNE / Ministério dos Negócios
   Estrangeiros, Casa de Linhares and any other that answers); for each hit record docId, title, date, correspondents, whether the
   record carries a digital object (the real page list via the rdigital route), and whether the same fonds or neighbouring docIds hold
   a key ("chave") or a decipherment ("decifração", "tradução") -- that pairing is the whole point.
3. Edition step for each pair: the Portuguese printed series on archive.org (Corpo Diplomático Portuguez, Quadro Elementar, Provas da
   História Genealógica, Gavetas da Torre do Tombo) whole-volume grep by date and correspondents; Cryptiana's Portuguese pages
   (sources/cryptiana/web/, on disk, grep "Portug"); the two solver repositories by grep (sources/cyphersolver*, a shallow clone of
   aaymeloglu/unsolved-ciphers grepped only). `python3 tools/prior_work.py` cannot run without a folder -- grep QUEUE.md, CATALOG.md and
   ciphers/ for each docId and fonds instead and say so.
4. Score survivors with tools/scout_rubric.py (a pool of several letters in one key counts as a pool). Output: QUEUE.md section
   "## Key-beside-cipher candidates, DigitArq / ANTT (24 Oct 2026, SCOUT-ANTT)" with a table (id, fonds and docId, item, key-material
   evidence quoted, why no decipherment survives / is not printed, images yes/no with the page count, estimated signs, score) and
   harvest/SCOUT-ANTT-2026-10-24.tsv. Never promote to the board, never create a ciphers/<slug>/ folder, never decode. Report:
   candidates found, top two with their evidence, fonds swept, request counts, five lines.
