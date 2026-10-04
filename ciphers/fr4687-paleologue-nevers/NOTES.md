blocked
Catalogue general des manuscrits francais, Ancien fonds t.4 (Paris 1895), entry 4687 read in full by this worker from the Internet Archive text (p1cataloguegnr04bibluoft): items 1-3 'Lettres, en italien, avec chiffres', item 41 'Chiffre', no 'dechiffre' anywhere in the entry; Boltanski 2006 (Les ducs de Nevers et l'Etat royal) checked page by page by this worker through the HathiTrust HTRC Extracted Features word counts (mdp.39015062439453, 588 pages, search-only) and the Google Books search-within (volume dsInahmnar8C): '4687' on two pages only (seq 203-204, the Camille Volta footnote), and none of its seven cipher-vocabulary pages names Paleologue or 4687; the Dizionario Biografico degli Italiani entry (Tamalio 2008, vol. 70) lists no printed edition of her letters; Ferrari 1999 (D. Ferrari, 'I Gonzaga e Nevers / Les Gonzagues et Nevers', in U. Bazzotti ed., Mantova e i Gonzaga di Nevers, Bozzolo 1999, pp. 15-30, OCLC 44824603) is on no cloud-reachable route (IA 0 items, HathiTrust 0 records for the OCLC, Google Books 0 volumes, OpenAlex/Semantic Scholar/CORE 0 hits, 2 Oct 2026) and could not be opened by this worker, so the verdict is blocked on LOCAL-QUEUE.tsv row L33 (a library copy of the essay), per check-solved.md.

# BnF fr.4687 — Marguerite Paléologue, duchesse de Mantoue, to Louis de Gonzague, duc de Nevers, 1562-1564

Status: blocked (CHECK-fr4687-paleologue-nevers, account-4, 2 Oct 2026: every edition reachable from the cloud is now read, see line 2 and the section below; the one item still to be opened is Ferrari 1999, a 16-page exhibition-catalogue essay, queued as LOCAL-QUEUE.tsv row L33 after row L8's academia.edu route was bot-challenged from the owner's desk too (27 Sept 2026). The folder reopens as `open` when L33 is answered negative; it is `found-solved` if the essay prints a decipherment. Earlier status line: LANE CX 12:20 UTC 25 Sept 2026 corrected the worker's `open` to `blocked` because Ferrari 1999 had not been opened.)

Check-solved pass, 24 September 2026 (Sonnet, orchestrator brief for M13-M16). Editions-first + one-leaf pass;
a formal six-source check-solved run is still owed before board promotion.


## Check-solved (CHECK-fr4687-paleologue-nevers, account-4, 2 Oct 2026)

Brief: the account-4 parent's prompt of 2 Oct 2026 (a check-solved pass whose verdict names the edition and the pages
or full text actually read; `.claude/briefs/check-solved.md` and `.claude/briefs/runs/2026-10-01-account4-webcheck.md`
for the format). Clock read at start: 05:17 UTC 2 Oct 2026. `tools/intake_gate_check.py fr4687-paleologue-nevers`
before this pass: `fr4687-paleologue-nevers: blocked (line 1) -- already terminal, nothing to gate`, exit 0 -- the
gate had nothing to say because the word was already `blocked`; what was missing was a verdict line naming an
edition this worker read, which line 2 now carries. `tools/key_livecheck.py` run first: Google Books, OpenAlex,
Semantic Scholar, CORE, Europeana, DPLA all present and answering HTTP 200; IA/DECODE/JSTOR presence-only.

**What "Ferrari 1999" is.** Not an edition of the letters: Daniela Ferrari, "I Gonzaga e Nevers / Les Gonzagues et
Nevers", pp. 15-30 of *Mantova e i Gonzaga di Nevers / Mantoue et les Gonzague de Nevers*, ed. Ugo Bazzotti, the
bilingual catalogue of the exhibition at Nevers (Palais Ducal, 16 Oct-7 Nov 1999) and Mantua (Palazzo Te, 18 Feb-
26 Mar 2000), Bozzolo 1999 (Open Library: OCLC 44824603, no ISBN; the L8 runner's Helka record
helka.9935145810306253). Tomokiyo cites it as background for his fr.3995 catalogue, not for fr.4687.

**Editions and catalogues read by this worker (2 Oct 2026):**

1. *Catalogue général des manuscrits français, Ancien fonds*, t. 4 (Paris 1895, Omont and others), entry 4687, read
   in full from the Internet Archive OCR text (`p1cataloguegnr04bibluoft_djvu.txt`, fetched once, 5.5 MB, grepped;
   "4687" occurs twice, both in this entry). Items 1-3: "Lettres, en italien, avec chiffres, de Marguerite
   Paléologue, duchesse de Mantoue, au duc de Nevers, Louis de Gonzague, son fils. De 1562 à 1564. (Fol. 1 et
   suiv.)". Item 41: "Chiffre. Quelques lignes non chiffrées sont en italien. (Fol. 89.)". No item in the entry is
   marked déchiffré, and no interlinear or facing decipherment is described for any item (the Thurloe/Birch shape
   check-solved.md asks for). Items 17, 20, 23-24 and 47 concern the duke's claims on his mother's succession
   (1570s), in clear.
2. BnF Archives et manuscrits notice `ark:/12148/cc577374` (Français 4687, Anc. 9509), read in full for the first
   time in this folder through the headless browser (`tools/browser_fetch.js`, one request, after adding the
   proxy CA to Chromium's NSS store -- the setup script's fix had not run in this container; plain curl and WebFetch
   answer 403, as on 24 and 25 Sept). Same item list as the 1895 catalogue, EAD ids d0e120 (items 1-3) and d0e474
   (item 41); index entries "Mantoue, Marguerite Paléologue, duchesse de. Lettres." and "... Succession."; no
   bibliography block beyond the standard "Informations bibliographiques" header, no Ferrari, no Boltanski, no
   déchiffré; "Numérisation effectuée à partir d'un document de substitution", viewer ark btv1b90075058.
3. Ariane Boltanski, *Les ducs de Nevers et l'État royal* (Genève, Droz, 2006; OCLC 75253632), the one modern
   monograph on the recipient. HathiTrust bibliographic API: record 005412144, htid mdp.39015062439453, "Limited
   (search-only)". Page-by-page word-count test through the HTRC Extracted Features API (588 pages, 385,888 body
   tokens, one request): "4687" on seq 203 and 204 only, both also carrying "Paléologue" and "Volta"; "Paléologue"
   on 23 pages; cipher vocabulary ("chiffre", "chiffré", "chiffrée(s)", "chiffrés", "déchiffrée", "déchiffrement")
   on seven pages (seq 139, 195, 398, 425, 427, 435, 440), none of which carries "Paléologue" or "4687". Google
   Books search-within (volume dsInahmnar8C, `country=US`, key from the environment): the two "4687" snippets are
   the footnote on the chevalier Guazzo/Camille Volta ("... Marguerite Paléologue, sollicita Louis de Gonzague pour
   qu'il le reprenne à son service. Le chevalier fut dès lors ... 4687, 4691, 4693). Camille Volta est, durant
   presque toute la seconde mo[itié] ..."); the one cipher snippet is about "lettres chiffrées qu'Henriette de
   Clèves adressait à Louis de Gonzague, en avril 1585"; `inauthor:Boltanski "Paléologue" chiffre`,
   `inauthor:Boltanski chiffré Mantoue` and `inauthor:Boltanski "Marguerite Paléologue" lettres fils 1562` return 0.
   Boltanski cites fr.4687 for Volta's letters, not for the mother's cipher letters, and prints no decipherment.
4. Raffaele Tamalio, "Margherita Paleologo, duchessa di Mantova e marchesa del Monferrato", *Dizionario Biografico
   degli Italiani* 70 (2008), read online (treccani.it, one request): the only sentence on these years is "dalla fine
   del 1562 M. assunse ufficialmente il governo per conto del figlio ..."; the Fonti e Bibl. paragraph (quoted in
   full in the worker's transcript) lists her *copialettere* at the Archivio di Stato di Mantova, Archivio Gonzaga
   bb. 198, 335, 1946-1969, 3001-3003, Davari 1890-91, Boltanski 2006 and no printed edition of her letters.
   (Suggestion only, rule 7: the copialettere bb. 1946-1969 for 1562-64 would be the place to look for clear
   drafts of these very letters; not chased.)
5. Lettres de Catherine de Médicis, vol. 2 (1563-66): surfaced only by a footnote on Marguerite Paléologue
   (Google Books snippet); recipient-side background, not an edition of these letters; not read further.
6. *Due lettere inedite che riguardano Lodovico Gonzaga duca di Nevers* (W. Braghirolli, Mantova 1864, 16 pp.):
   checked because its title fits; Google Books (q0dEAQAAMAAJ, Memorie storiche ... Casale 1897, and Boltanski's
   own citation) says the two letters are Vigo Galvagni's and Filippo Cavriana's of 28 Feb and 6 Apr 1568 -- not
   the mother's, not cipher. Not on IA (advancedsearch and be-api 0).

**Ferrari 1999 by every cloud route (2 Oct 2026):** Internet Archive advancedsearch, titles "Gonzaga di Nevers" /
"Gonzague de Nevers" / "Gonzagues et Nevers" and Bazzotti+Nevers: 0 items; be-api full text: 0 for the title;
HathiTrust bibliographic API by OCLC 44824603: `{"records": {}, "items": []}`; Google Books API intitle/inauthor
Bazzotti: 0 volumes; OpenAlex (`Gonzaga Nevers Ferrari Bazzotti 1999`): 6 unrelated works; Semantic Scholar: 0;
CORE: only noise ("Ferrari" matches); open web (one search on the title and author): no copy, only Ferrari's
author pages. Academia.edu (the L8 route) is a 403 login wall from the cloud and was bot-challenged from the
owner's own browser on 27 Sept 2026 (L8, PR 38). So the essay is unread, and the verdict stays `blocked` on the
new LOCAL-QUEUE.tsv row L33 (a library copy, the route L8 did not try), in check-solved.md's wording. This
worker's assessment, for the parent to weigh (not a verdict): an exhibition-catalogue essay on the Gonzaga-Nevers
link is a low-probability place for a decipherment, and every edition that could be read says nothing of one.

**Six sources, this pass:** (1) web -- the "Web and blog check" section at the end of this file; (2) editions --
above; (3) community lists -- `sources/cryptiana/CRYPTO-INDEX.tsv` and the whole `sources/cryptiana/` snapshot
grepped for 4687 / Paleolog / Mantoue / Mantua / Margherita / Marguerite: the only "4687" hits are a digit string in
hardnuts.htm and a Blogger post id; `nevers.htm` (fr.3995) and `mantua.htm` (1590/1593, fr.3979/3983, a later
generation) are the nearest pages and name neither fr.4687 nor the 1562-64 letters; (4) DECODE -- the cached
listings of 24-28 Sept 2026 (decrypted 1360, non-decrypted 1186, keys 6324 rows) and a fresh login-free
`tools/decode_list.py` crawl of the newest 700 decrypted cipher records (14 requests, 2 Oct 2026, 0 records added
since the 24 Sept cache): no Paris / BnF / fr.4687 record; the only Mantua-related rows are Archivio di Stato di
Mantova items (Archivio Gonzaga E.V.3 busta 533 of 1395, decrypted; E.I.2 busta 423 keys dated 1540-1699, N/A;
record 1854 "Mantova enciphered letters", partially decrypted) -- a different holding, no correspondent match;
(5) Bourdeau (`dbourdeau/cyphersolver`, fresh depth-1 clone, HEAD 34e0fc8): fr.4687 appears once, as a harvested
Gallica notice line in `research/gallica_sweep/bnf_candidates.txt` (and the matching SRU JSON), no target folder,
no README / next / todo / planned line naming it; the GitHub issue and PR hits in the web search (Laurière
fr.3625, intercepts fr.3977) are other Nevers volumes; (6) Aymeloglu (`aaymeloglu/unsolved-ciphers`, fresh depth-1
clone, HEAD d2800bb): 0 hits for Paleolog / Mantoue; the "4687" line in `catalogue/decode-catalog.csv` is DECODE
record id 4687 (Marburg, a different item).

**Verdict: blocked** (line 1), on LOCAL-QUEUE.tsv row L33. No decipherment, key or plaintext of items 1-3 found in
any of the six sources or in the editions read above; where it was not found is listed above and in the web and
blog section. Novelty not classified (rule 10).

Requests this pass: archive.org 7 (3 advancedsearch, 1 metadata, 1 djvu text, 2 for the 1864 pamphlet),
be-api.us.archive.org 5, openlibrary.org 4, googleapis.com (Books API) 17, catalog.hathitrust.org 2,
data.htrc.illinois.edu 1, api.openalex.org 3, api.semanticscholar.org 2, api.core.ac.uk 3, de-crypt.org 14
(login-free listing), github.com 2 (shallow clones, deleted after grep), archivesetmanuscrits.bnf.fr 1 (browser),
treccani.it 1, cryptiana.blogspot.com 1, scienceblogs.de 1, ciphermysteries.com 1; WebSearch 10 queries. No
logins, no credentials printed, no vision calls, no transcription, no cryptanalysis.

## Check-solved (LANE CX, 25 Sept 2026)

Formal six-source sweep per `.claude/briefs/check-solved.md`, completing the 24 Sept "Class gate" section below
(which already did most of sources 1-3, 5-6) rather than repeating it, and adding source 4 (DECODE), which that
section did not check.

1. **Web search.** Three queries this pass: `"Marguerite Paléologue" "Nevers" chiffre cipher solved OR "Claude"
   OR "GPT" solves`, `"Marguerite Paléologue" "4687" cipher chiffre solved Vals AI Claude decipherment`, and a
   narrower Bourdeau-catalogue check. All surfaced only the BnF archivesetmanuscrits notice for fr.4687 itself
   (now indexed/readable via search snippet, confirming Français 4687 was formerly catalogued **Ancien fonds
   9509** — a new identifier, not previously on file, close to but not confirmed identical to the "no. 9510...
   Marguerite Paléologue... à M. de Nevers, 1559" entry the 24 Sept pass flagged from *Dictionnaire des
   manuscrits* as a different, earlier, unconfirmed letter), general Schneier/model-solve-announcement posts
   (Urquhart 1653, Cyphral Distich, medieval-cipher AI-assist stories — none about this letter), and academic
   ciphertext-decipherment papers unrelated to this correspondence. No hit names this letter, this cipher, or a
   solution to it.
2. **Standard edition/calendar.** As line 2 states and the 24 Sept "Class gate" section details at length:
   Boltanski 2006 search-within found real content from the book but nothing tying it to fr.4687; Ferrari 1999
   could not be opened (academia.edu 403) and is queued (LOCAL-QUEUE.tsv row L8, already present, not duplicated
   this pass). This is the gate-passing controlled full-text search per line 2.
3. **Community lists.** Tomokiyo's `nevers.htm` already read in full by the 24 Sept pass (no hit — confirmed the
   catalogue covers a different volume, fr.3995, by period and relationship, see "Key candidates" section below).
   No Cipherbrain/Schmeh-specific page found; the web search above is this worker's equivalent check.
4. **DECODE** (not covered by the 24 Sept "Class gate" section — this worker's addition). Aymeloglu's cached
   DECODE catalogue mirror (`catalogue/decode-catalog.csv`, fresh clone) grepped for "paleolog"/"paléolog"/
   "4687"/"mantoue"/"mantova": 10 hits, all **Archivio di Stato di Mantova** items (Archivio Gonzaga E.V.3/E.I.2,
   1395 and 1540-1699) — a different holding archive, different busta/folio numbers, different (mostly later or
   unspecified) dates, no correspondent match to Marguerite Paléologue or Louis de Gonzague as duc de Nevers.
   Zero hits for "4687" itself. `sources/decode/records-non-decrypted-2026-09-24.tsv` (local cache): zero hits
   for the same terms.
5. **Bourdeau** (`github.com/dbourdeau/cyphersolver`, fresh depth-1 clone by this worker, 25 Sept 2026, not the
   24 Sept pass's clone): `grep -ril "paleologue\|paléologue\|4687"` — zero hits, confirming the 24 Sept finding
   on a fresh clone.
6. **Aymeloglu** (`github.com/aaymeloglu/unsolved-ciphers`, fresh depth-1 clone by this worker, 25 Sept 2026):
   same grep (outside the DECODE-catalogue-mirror hits already covered under item 4) — zero hits.

**Verdict: open, unchanged.** The controlled full-text search (item 2/line 2) and the fresh DECODE/Bourdeau/
Aymeloglu checks (items 4-6) find nothing tying this correspondence, its cipher, or a decipherment to any prior
source. Ferrari 1999 remains the one open risk (paywalled, queued). The extensive ciphertext-only cryptanalysis
below (negative with matched controls at 900 signs) stands unchanged by this pass. Novelty not classified (rule
10; not this brief's job).

Requests this pass: github.com 2 (fresh shallow clones, dbourdeau + aaymeloglu, deleted after grep). WebSearch 3
queries. No other hosts (Google Books/academia.edu/JSTOR work reuses the 24 Sept pass's already-logged results,
not repeated). No subagents, no logins, no credentials.

## Correction to the queue row

QUEUE.md M14 dated the item "(undated, volume covers 1585-91 Nevers-Gonzaga affairs)". Gallica's own catalogue
description (via `services/OAIRecord`) dates items 1-3 precisely:

> Recueil de pièces originales et de copies concernant l'histoire de la maison de Nevers. De 1562 à 1625...
> 1-3 Lettres, en italien, avec chiffres, de MARGUERITE PALEOLOGUE, duchesse DE MANTOUE, au duc de Nevers, Louis
> de Gonzague, son fils. De 1562 à 1564.

Margherita Paleologa (1510-1566) was regent-mother of Mantua during this period; her son Louis/Ludovico de
Gonzague later became Duke of Nevers in France. **1562-1564, not 1585-91.** QUEUE.md M14 row updated accordingly.

The same volume's item 41 is listed separately as "Chiffre. Quelques lignes non chiffrées sont en italien" —
an undated ciphered item elsewhere in the recueil, possibly unrelated to items 1-3 (different sender/date), not
investigated this pass.

## Checked (24 Sept 2026)

- Fresh shallow clone of `dbourdeau/cyphersolver`: no hit on "4687", "Paleologue/Paléologue" or "Marguerite" tied
  to this volume.
- Fresh shallow clone of `aaymeloglu/unsolved-ciphers`: no hit.
- `sources/cryptiana/web/nevers.htm` (Tomokiyo's own catalogue of ciphers in BnF fr.3995, "the Nevers
  collection") read locally, no fetch needed: covers a *different* volume — the Duke of Nevers' own cipher
  keys and correspondence as ambassador/courtier (fr.3995, fr.3251, fr.3413, etc.) — not his mother's 1562-64
  letters to him. No hit on "4687", "Paleologue" or "Marguerite" in the full 1420-line mirror.
- WebSearch for Italian scholarship on Margherita Paleologa's correspondence with her son in this period found
  only general biographical material (Wikipedia, Treccani); no edition or article naming this specific
  correspondence or its cipher was located. Tomokiyo's own background bibliography for the Nevers material
  (Daniela Ferrari 1999, "Mantoue et les Gonzague de Nevers"; Ariane Boltanski 2006, *Les ducs de Nevers et
  l'État royal*) was not checked against this specific volume this pass — flagged as the next step, not chased
  further under the check-solved brief's scope.
- Gallica IIIF, canvas 5 (f.1, faint, mostly illegible clear Italian), canvas 7 (f.5, clear Italian salutation
  "Al Ill.mo... figlio caris[si]mo"), canvas 8 (f.6, **ciphertext confirmed**: dense two-digit numeral groups,
  roughly 15-25 groups per line across at least six lines on this one leaf alone — a high-resolution crop is at
  `images/f8_crop.jpg`). Short Italian phrases appear in the left margin beside each ciphered line (e.g.
  "questa una quan[to] a quello che...", "et como...", "vi sera che... seguira..."); these read as the clerk's
  catch-phrase cues for filing/reference, not a complete parallel plaintext — no full interlinear decipherment
  was seen on this leaf. Images: `images/f5.jpg`, `images/f7.jpg`, `images/f8.jpg`, `images/f8_crop.jpg`.

## Class gate (24 Sept 2026)

Question: is this correspondence, its cipher, or a decipherment already in print? Searched (WebSearch, Google
Books API with `&country=US` and `&key=$GOOGLE_BOOKS_KEY` never printed, IA advancedsearch, JSTOR/academia.edu
reachability):

- Daniela Ferrari (1999), "Mantoue et les Gonzague de Nevers" — the article/catalogue Tomokiyo's own
  bibliography cites via an Academia.edu link. `academia.edu` answered curl/WebFetch with HTTP 403 (login wall);
  not read this pass. A WebSearch attempt to locate the title by exact string mostly surfaced an unrelated 1999
  numismatic item ("Mantova e i Gonzaga di Nevers" / "Mantoue et les Gonzague de Nevers", a coins-and-medals
  piece, possibly the same underlying catalogue Tomokiyo cites, possibly a namesake — not disambiguated) and
  confirmed Daniela Ferrari's role as director of the Archivio di Stato di Mantova 1990-2014. IA advancedsearch
  for "Ferrari Mantoue Gonzague Nevers" returned zero hits. Not located in readable full text this pass.
- Ariane Boltanski (2006), *Les ducs de Nevers et l'État royal* (Droz) — found and reachable via the Google
  Books API (volume id `dsInahmnar8C`, no full-view/snippet search-inside without a matching-phrase hit,
  `country=US` applied). Two relevant snippets surfaced by phrase search: "Marguerite Paléologue demeure
  résolument habsbourgeoise" (a general political-alignment remark, footnote 68) and "Paléologue, qui reçoit de
  Catherine d'assez fréquentes lettres, conservées dans les archives mantouannes: A.M." — this second snippet is
  about letters Marguerite Paléologue *received from Catherine de Médicis*, held in the Mantua state archives,
  not letters she *sent to her son*, and not BnF fr.4687. Targeted phrase queries combining Boltanski with
  "chiffre" and with "duchesse de Mantoue" + "correspondance" returned no hit tying the book to fr.4687 or to
  a cipher. No full read of the book attempted (Droz academic monograph, not on IA/HathiTrust full view this
  pass).
- General Gonzaga-Nevers editions/scholarship: Google Books full-text search for `"Marguerite Paléologue" "duc
  de Nevers" 1562` surfaced one distinct catalogue entry worth flagging — *Dictionnaire des manuscrits, ou
  Recueil de catalogues de manuscrits* lists an item "9510. ... Marguerite Paléologue, Duchesse de Mantoue à M.
  de Nevers, 1559" in an unnamed manuscript collection. This is a **different, single, earlier letter** (1559,
  three years before the fr.4687 items 1-3 start), not confirmed as the same correspondence — flagged, not
  chased further this pass. No other edition, calendar, or article naming this correspondence, its cipher, or a
  decipherment was found.
- `archivesetmanuscrits.bnf.fr/ark:/12148/cc577374` (BnF's own manuscript-level catalogue notice for fr.4687,
  which may carry a fuller bibliography than the OAI record already quoted above): returned HTTP 403 to both
  curl and WebFetch this pass (Cloudflare-style block, consistent with the Access playbook's note on this
  family of BnF pages); not read. Worth a browser-tool retry in a future pass.
- JSTOR: host reachable (`curl -o /dev/null -w "%{http_code}"` returned 200), but its search page requires
  JavaScript and returned no results through WebFetch's static render; no article search completed. Not
  retried further this pass (one attempt, per the good-citizen rule).

**Class-gate verdict: no prior print or discussion of these letters, their cipher, or a decipherment located.**
This is a search result under rule 10, not a claim of absence; Ferrari 1999 in particular was not actually read
(paywalled), only searched for by title, and the BnF's own fuller catalogue notice was not reachable this pass —
both are open risks flagged for whoever promotes this target, same shape as the M13 fr.16092 flag in ROOM.md.

## Key candidates (24 Sept 2026)

Question: does Tomokiyo's catalogue of ciphers in BnF fr.3995 (`sources/cryptiana/web/nevers.htm`, read in full
locally, no fetch) contain a key that could apply to this correspondence? Checked by keyword (`Marguerite`,
`Mantoue`/`Mantua`, `Paleolog`/`Paléolog`, `mere`/`mère`, `1562`-`1564`) and by reading the catalogue's own
scope statement and date range.

**No candidate found.** Three independent reasons:

1. Tomokiyo's fr.3995 catalogue is explicitly about ciphers belonging to Louis de Gonzague *as Duke of Nevers*
   ("the collection probably belonged to the duke"), a title he did not hold until his 1565 marriage to
   Henriette de Clèves — one to three years *after* the last of these letters (1564). Its earliest entry,
   no.1 (fol.1), is dated June 1580, sixteen years after this correspondence ends; the whole catalogued run
   is 1580-1594 (with more ciphers from other volumes, fr.3251/3315/3413/3416/3612/3616/3633/3641/3974-3994/
   4702/4712/4715, in the same post-1580 political-correspondent range). No entry predates 1580.
2. Two catalogue entries are captioned "Chifre avec la Duch[ess]e" / "avec la Duchesse" (no.2, fol.3, Oct 1584;
   no.6, fol.13, 1585) — but "la Duchesse" in a Duke-of-Nevers cipher of 1584-85 is his wife Henriette de
   Clèves, duchesse de Nevers, not his mother the duchess of Mantua; no.4 (fol.8, 1585) is captioned
   explicitly "avec la Duchesse ma feme" (my wife), confirming the sense. No entry is captioned with
   "mère" (mother), "Mantoue", or "Paleologue"/"Paléologue" — zero hits for all of these across the full
   1244-line mirror.
3. No.19 (fol.38, 1588) and no.20 (fol.40, May 1589) are the catalogue's closest formal matches to fr.4687's
   cipher type (both "substitution by two-digit figures... in Italian", two-part code, enciphering/deciphering
   tables) — but both post-date this correspondence by roughly a quarter century and are captioned for
   different correspondents (place names, not "la Duchesse" or a mother-son pairing).

Conclusion: fr.3995 is the wrong volume by both period (Duke-of-Nevers-era ciphers, 1580s-90s) and relationship
(wife/political correspondents, not mother); no key transfer is plausible without an intervening, unstated
20-year reuse. No candidate key promoted; none of Tomokiyo's fr.3995-family ciphers were tested against
fr.4687's ciphertext this pass.

## Extent (24 Sept 2026)

Viewed Gallica IIIF canvases 5-15 (one request per canvas, 1.5s apart, descriptive User-Agent; one connection
reset on an `info.json` request, recovered on a single retry after a pause, per the good-citizen rule). Full
manifest and per-canvas content notes: `images/manifest.json`.

Of the eleven canvases covering items 1-3 in this range, **three carry cipher**: canvas 8 (dense multi-line
block, mid-letter-1, previously found and cropped as `images/f8_crop.jpg`), canvas 9 (one dense cipher line
near the close of letter 1, cropped as `images/f9_crop.jpg`), and canvas 10, left page (a six-line dense cipher
postscript closing letter 1, immediately after the clear-Italian line "lase le mie le posete brusare" — burn
these of mine — and above the signature; cropped as `images/f10_crop.jpg`). Canvas 6 is very faint
pencil/draft script on both pages, not legible enough at this resolution to classify as cipher or clear text
(flagged "uncertain" in the manifest, not chased further). Canvases 5, 7, 11, 12, 13, 14, and 15 are clear
Italian throughout wherever legible; canvas 15 (right page) carries what reads as letter 2 (or 3)'s closing
signature "vostra madre la Duchessa di Mantua" and a date "26 [di] 9bre [novembre] del 6-" (year's last digit
not legibly read at this resolution). This suggests the volume's three cipher passages found so far all belong
to the *first* of the three catalogued letters (the one opening near canvas 5/7 and closing on canvas 10), with
the second and/or third letters, as far as canvases 11-15 go, running entirely in clear Italian — not confirmed
beyond canvas 15, which is as far as this pass's brief went.

## Passes (24 Sept 2026)

Two blind Sonnet subagents transcribed the three cipher crops (`images/f8_crop.jpg`, `images/f9_crop.jpg`,
`images/f10_crop.jpg`) independently, neither shown the other's file: `passA.tsv`, `passB.tsv` (line, position,
group, confidence; clear Italian runs as `[PLAIN:"..."]` rows, flagged illegible spots as `[flagged: ...]`
rows). No reconciliation attempted, no decoding, no novelty wording. The two files are the primary record;
this is a description of them, not a merged reading.

Totals: pass A read 240 cipher-group rows + 25 PLAIN/flagged rows across 11+8+9=28 manuscript lines; pass B
read 171 cipher-group rows + 31 PLAIN/flagged rows across the same 28 line ids. Both passes independently
arrived at the same line count and the same high-level structure (one dense cipher block on f8, one cipher
line embedded in plain text on f9, one dense six-line cipher postscript on f10) without having seen each
other's file.

Per-line agreement, restricted to cipher-group rows and comparing by (line, position) where both passes
assigned some group to that exact slot (a coarse measure — it penalizes any upstream difference in how a
dense run was segmented into groups, not just misread digits):

| line | A groups | B groups | exact match at common positions |
|---|---|---|---|
| f8_L2 | 8 | 8 | 7/8 (88%) |
| f8_L3 | 20 | 17 | 3/17 (18%) |
| f8_L4 | 16 | 12 | 0/11 (0%) |
| f8_L5 | 13 | 8 | 0/8 (0%) |
| f8_L7 | 20 | 9 | 1/9 (11%) |
| f8_L8 | 17 | 12 | 2/12 (17%) |
| f8_L9 | 19 | 12 | 0/12 (0%) |
| f8_L10 | 21 | 11 | 0/11 (0%) |
| f8_L11 | 0 (flagged illegible/cropped) | 10 | n/a — passes disagree on whether this line is even legible |
| f9_L6 | 13 | 11 | 2/11 (18%) |
| f10_L2 | 13 | 11 | 0/11 (0%) |
| f10_L3 | 17 | 10 | 1/10 (10%) |
| f10_L4 | 18 | 10 | 0/10 (0%) |
| f10_L5 | 16 | 10 | 0/10 (0%) |
| f10_L6 | 15 | 11 | 0/11 (0%) |
| f10_L7 | 14 | 9 | 0/9 (0%) |

Overall: 16/160 (10%) position-exact agreement across the 16 cipher-bearing lines. f8_L2 (the shortest,
least-dense cipher line, 8 groups) is the one clear exception at 88%; every longer, denser line falls to
single digits of percent agreement, driven mostly by the two passes segmenting the same unbroken digit
string into a different number of groups (A consistently more groups than B on every dense line) rather than
by disagreement over individual digit shapes — both subagents independently flagged this same difficulty
(ambiguous group boundaries in a continuous cursive numeral hand) in their own reports. f8_L11 is a clean
disagreement about legibility itself, not just segmentation: pass A treated it as illegible/cropped (0 rows),
pass B read 10 groups from it.

Reading: at this crop resolution, the two passes agree closely on where cipher is present and on the overall
letter structure, but not, group-for-group, on where one cipher group ends and the next begins in the denser
lines — a transcription-quality finding, not a reconciled reading. No group boundary was adjudicated and no
group was decoded.

## Sources

- Gallica: `https://gallica.bnf.fr/ark:/12148/btv1b90075058`, OAI record via
  `https://gallica.bnf.fr/services/OAIRecord?ark=btv1b90075058`.
- `sources/cryptiana/web/nevers.htm` (S. Tomokiyo, "Ciphers in BnF fr.3995 (the Nevers collection)"), local
  mirror, no fetch.
- github.com/dbourdeau/cyphersolver, github.com/aaymeloglu/unsolved-ciphers (both checked, no relevant content;
  Aymeloglu has no licence, cite only, nothing copied).

## Requests, check-solved pass (24 Sept 2026, earlier)

gallica.bnf.fr: 1 OAI record + 4 IIIF image fetches (1 crop). github.com: 2 shallow clones (shared with M13,
deleted after grep). WebSearch: 1 query.

## Requests, literature+key-hunt+extent+passes worker (24 Sept 2026)

gallica.bnf.fr: 1 manifest.json + 8 canvas image fetches + 2 info.json (1 connection reset, retried once,
recovered) = 11. googleapis.com (Google Books, `&key=$GOOGLE_BOOKS_KEY&country=US`, key never printed): 9
queries. archive.org advancedsearch: 1. jstor.org: 1 reachability check + 1 WebFetch (no usable result,
JS-gated search page). academia.edu: 1 reachability check (403). archivesetmanuscrits.bnf.fr: 1 WebFetch (403).
WebSearch: 3 queries. No logins, no credentials printed. Two Sonnet subagents for the blind passes (within the
brief's fan-out limit).

## Segmentation (24 Sept 2026, reconciler, Opus)

Written before reconciling, from the page images. The on-disk crops (`f9_crop.jpg`, `f10_crop.jpg` at 800 px;
`f8_crop.jpg` upscaled) were too coarse to show separators, so three native-resolution IIIF regions were fetched
once (`images/f8_native_region.jpg`, `f9_native_region.jpg`, `f10_native_region.jpg`; regions and request log in
`images/manifest.json`). Evidence, read at about 400 dpi:

- **No separators.** Digits run at an even pitch across each line. There is no consistent space, point, virgule or
  superscript between groups. The dots are part of the letterforms: the tittle of `i` (the scribe writes 1 as a
  dotted i, and the dot often drifts left), the entry tick of `2` and `7`, and the ink blobs at the ends of the
  descenders of 4, 7 and 9. They occur at every position, so they do not mark group boundaries.
- **One non-digit sign, `y`** (an `ij`/`ÿ` shape with a long descender, sometimes with two dots). It occurs 28 times
  in 588 signs. Pass A saw it on its own and wrote it `11~`; pass B read it as 9 or 1. Here it is a separate sign.
  Its function (letter, null or divider) is not decided. It comes most often after 7, 4 or 3 and before 6 or 2.
- **4 and 9 are separate shapes.** 4 has a horizontal crossbar through the stem; 9 is a q with a plain descender.
  Most of the A/B digit disputes are 4/9 pairs, and the coarse crops lose the crossbar.
- **Scribal corrections** (flagged in the `note` column of ciphertext.txt): a superscript `24` over a struck group
  (f8_L4 start); an interlinear `y20` placed at a colon-shaped caret after `17` (f8_L9; pass A had put it in
  f8_L8); a superscript `17` over a blotted group (f9_L6); a superscript `2` over a blotted digit (f10_L7). Each
  replacement is one or two digits, or `y` plus two digits. None of them fixes a group length.
- **Statistical test** (`seg_test.py`). Under a fixed two-digit grid, the most frequent two-digit units should sit on
  one parity within a line. The parity lock is 0.577 with `y` kept as a sign and 0.629 with `y` dropped.
  Matched synthetic controls use the same line lengths, Italian letter frequencies and homophonic codes. A fixed
  two-digit control scores 0.716 / 0.657 / 0.643 (mean) at 0 / 5 / 10 % digit insertion-deletion error, with 5th
  percentiles 0.632 / 0.599 / 0.593. A mixed 1/2/3-digit control scores 0.584-0.586 (95th percentile about 0.62-0.63).
  Shuffled real lines score 0.611. The runs between `y` signs have odd length 24 times out of 44. So a strict
  two-digit grid with `y` as a one-sign token falls below every fixed-two-digit control's 5th percentile and sits
  at the mixed control's mean. With `y` dropped, the value is compatible with either design. The test is weak
  (shuffled lines overlap both controls) and **leans mixed-length without settling it.**

**Rule adopted.** The scribe marks no group boundaries, and neither the image nor the statistics settle the group
length. The transcription unit is therefore the **sign** (0-9 and y). Each pass's grouping is kept per sign as
an alternative (`a_start`, `b_start`), and every intra-line boundary counts as M. Frequent units are 17, 18,
20 and 22 (30, 26, 30 and 18 occurrences as adjacent pairs). They are consistent with a design built on 1x/2x
two-digit numbers plus single signs, which is a hypothesis for the solver, not a finding.

## Reconciliation (24 Sept 2026)

`reconcile.py` aligns pass A, pass B and the reconciler's native-resolution reading (`passC_native.tsv`, one sign
stream per line) and writes `ciphertext.txt` (line, pos, sign, conf, alt, a_start, b_start, note) and
`inventory.tsv`. `python3 reconcile.py --check` exits 1 if either file is stale. Confidence is H when A, B and
the native reading all give the same sign (at least two readings). Otherwise it is M, with the other readings
in `alt`. The alignment is difflib's, which pairs signs inside replaced blocks by position, so H is a slight
overcount wherever a pass dropped or added a sign.

| | count |
|---|---|
| lines | 17 (the 16 both passes read, plus f8_L11, which only pass B read; pass A called it cut off) |
| signs | 588 (H 480, M 108) |
| distinct signs | 11 (0-9, y) |
| intra-line boundaries | 572, all M under the rule; A and B agree on 327 (101 boundary, 226 no boundary), disagree on 134; one pass lacks the sign at 111 |
| distinct adjacent sign pairs | 99 |

Sign counts (inventory.tsv): 1 100, 2 93, 9 63, 4 56, 5 47, 7 45, 3 41, 8 41, 0 38, 6 36, y 28.
Top-20 adjacent pairs (candidate units, not established groups): 20 30, 17 30, 18 26, 51 19, 22 18, 41 15, 92 14,
32 14, 91 12, 61 12, 85 12, 19 11, 29 10, 24 10, 62 10, 84 10, 31 9, 73 9, 42 9, 01 8.
f8_L11 is M-heavy (15/37 H) because only one pass read it.

**Coverage gap: cipher the passes never saw.** The native regions show cipher outside the three old crops:
about 4 lines at the top of canvas 9's left page (from "...ogni cosa p. che 1759" to "...vostro S. Idio facia",
with clear words such as "et mi" mixed in), about 4 lines on canvas 8's left page (lower half, above "i cardinali
vostro fratello..."), and a twelfth cipher line on canvas 8's right page below f8_L11 (ending with a carried "184").
Estimate: about 280-300 more signs, so about 870-890 in all. They are in the native regions on disk. They need
two blind passes before anything is run on the whole text (a follow-up, not done here). Canvas 6 (faint) is
still unclassified.

**Enough for a solver run?** Not yet. `tools/nomenclator_anneal.py` takes pre-segmented group codes, and this text
has no settled segmentation. A run needs either a segmentation hypothesis fixed in advance (for example "1x/2x
are two-digit, 3-9 and y single") or a solver that infers segmentation jointly. It should also wait for the
missing ~300 signs to be transcribed. A matched control would need: Italian letter prose of the 1560s at the same
length (~880 signs); the same 11-sign alphabet with one ~5 % extra sign; the same code design as the hypothesis
under test; the text written as an unbroken stream at the same line lengths; about 18 % sign-level noise, 4/9
confusions in particular; and scoring by the same model (`tools/italian_ngram.py`, which was built on 15th-c.
Lombard chancery Italian, so a 1560s Mantuan corpus would be the better fit).

Requests this pass: gallica.bnf.fr 3 (IIIF regions, 2 s apart, all 200). No other host, no subagents, no logins.

## Joint-segmentation solver (24 Sept 2026)

Solver session (Opus, LANE G brief). Input: the reconciled 588 signs of `ciphertext.txt` only (first reading per
sign, `solver/signs.txt`). The ~290 signs of the extra regions were not included: `passA_extra`/`passB_extra`
had not been pushed when this ran. **Result: a clean negative with matched controls. No reading is claimed.
Grade counts: H 0, C 0, S 0, M 0, I 0 (no token read).**

**Model.** 16th-c. Italian letter model, built from six Internet Archive full texts: Ferrato's Gonzaga
princesses' letters (Mantua 1879), Caro, B. Tasso, letters to Aretino, Cibrario's *Lettere inedite di ...
principi* (manifest `tools/data/it16/manifest.json`). `tools/italian16_corpus.py` keeps paragraphs where
period letter markers outnumber editorial ones, giving 417 paragraphs and 282,755 letters. It feeds
`tools/italian_ngram.py build`, which fits an order-5 model. Every 10th paragraph is held out
(`solver/control_heldout.txt`) as control plaintext, and the control-solving model never saw it.

**Structure tests** (`solver/structure.py`, 20,000 shuffles of the real signs over the real line lengths):

| statistic | observed | shuffle mean | p |
|---|---|---|---|
| `1` at line end or before `y` | 0 | 7.4 | 0.00015 |
| `2` at line end or before `y` | 3 | 6.8 | 0.068 |
| `0` not preceded by `2` | 8 | 32.1 | <0.00005 |
| `7` not preceded by `1` | 15 | 37.5 | <0.00005 |
| `8` not preceded by `1` | 15 | 34.2 | <0.00005 |

`1` behaves as a prefix sign. It occurs 100 times and never ends a line or stands before `y`. `0` is almost
always the second half of `20`. The design most consistent with this is prefix-free: 1x and 2x are two-digit
units, and 0, 3-9 and `y` are single units. It parses the stream into 423 units of 30 types, with 3 exceptions
(a `2` before `y`). A single/double split does not mark vowels against consonants: adjacent single/double
alternation is 0.49, while Italian vowel/consonant alternation is 0.73. `y` is too rare for a word divider
(one per 15 units). This design is a hypothesis the statistics favour. It is not established.

**Solver** (`tools/seg_homophonic.py`, new). It takes a design (prefix set, with `y` as a letter or a null),
segments the stream, and anneals a homophonic key (any number of units per letter) against the model, with
restarts and a steepest-ascent finish. A unigram-divergence guard (weight 3) stops the collapse to an all-`i`
key that the first two runs fell into on both the target and the noisy controls. The design is chosen by
running each candidate and comparing it with nulls. Sign-shuffle nulls re-segment the shuffled signs; unit-shuffle
nulls keep the units and destroy their order.

**Matched controls (rule 3).** Held-out Italian of 360 letters under a random homophonic key over the same
29-unit inventory (1x/2x plus 0, 3-9 and `y`). It is cut into lines of the target's lengths at unit boundaries,
giving 584-646 signs against the target's 588. Sign noise is added (drops, insertions, 4/9 swaps), and the
text is solved blind with the same settings. Per-token letter accuracy, 5 seeds each (`solver/runs/control_*`):

| control | mean accuracy | per seed |
|---|---|---|
| 1x/2x, y letter, 0 % noise | 1.000 | 1.00 1.00 1.00 1.00 1.00 |
| 1x/2x, y letter, 5 % noise | 0.917 | 0.91 0.88 0.94 0.95 0.91 |
| 1x/2x, y letter, 10 % noise | 0.754 | 0.79 0.86 0.80 0.53 0.79 |
| 1x/2x, y letter, 15 % noise | 0.244 | 0.20 0.29 0.14 0.39 0.20 |
| 1x/2x, y null (6.6 %), 5 % noise | 0.781 | 0.21 0.90 0.92 0.95 0.93 |

**Target** (`solver/runs/target*`). Model score per unit, including the guard, against nulls:

| design | units | types | score/unit | null (kind) | z | output |
|---|---|---|---|---|---|---|
| 1x/2x, y letter | 423 | 30 | -3.489 | -3.802 ± 0.008 (signs) | 40.9 | not Italian |
| 1x/2x, y letter | 423 | 30 | -3.489 | -3.865 ± 0.044 (units) | 8.5 | not Italian |
| 1x/2x, y null | 395 | 29 | -3.538 | -3.789 ± 0.061 (signs) | 4.1 | not Italian |
| 1x only, y letter | 489 | 20 | -3.908 | -4.159 ± 0.045 (signs) | 5.6 | not Italian |
| 2x only, y letter | 515 | 21 | -3.866 | -4.147 ± 0.039 (signs) | 7.2 | not Italian |
| 1x/2x, y letter, 40 single-reader signs dropped | 390 | 30 | -3.458 | -3.822 ± 0.034 (units) | 10.7 | not Italian |
| 1x/2x, y null, same variant | 368 | 29 | -3.545 | -3.834 ± 0.083 (units) | 3.5 | not Italian |

The best output (1x/2x, y letter) begins `hcioteonaaleosiebratenesedrauinidratocalamabiracheonsihersosuleet
cittacarneet...`. It contains isolated short Italian strings (`che`, `et`, `citta`) but no run of words.

**Calibration.** On a 10 % noise control of the same size (`solver/runs/ctl_unitnull_n0.1.txt`), the solver
scored -3.392 per unit against a unit-shuffle null of -3.734 ± 0.043, z = 7.9. The target's -3.489 and
z = 8.5 are indistinguishable from it. True-key scores of controls are about -1.5 per unit at 0 % noise, -2.2
to -2.5 at 5 %, -2.9 to -3.1 at 10 % and -3.5 to -4.5 at 18 %. So the target's order carries some structure,
but its score sits where a noisy (roughly 10 %+) Italian control would sit, or where a non-Italian or
nomenclator design would. The solver cannot tell these apart at this length.

**What the negative means.** The solver reads a matched 1x/2x homophonic control at 100 % (clean) and 92 %
(5 % sign noise), and the target does not read under that design or any of the four others tried. The
negative holds only (a) for a pure letter-substitution design (no code words, no syllables), (b) for the
588 signs as reconciled (18 % of them M, and 40 seen by only one of the three readings), and (c) in 16th-c.
literary/chancery Italian. Margherita Paleologa's clear lines ("lase le mie le posete brusare") are strongly
Mantuan and phonetic, which the model does not cover. Above about 10 % transcription noise the control itself
fails (24 % at 15 %), so a negative on this transcription is weak evidence.

Next moves, most promising first. None of these was done here.
1. Add the ~290 extra signs once reconciled; at about 880 signs the 10-15 % noise band should be readable.
2. A second native-resolution reading of the M signs, especially 4/9 and the `A:-,B:-` signs.
3. A Mantuan dialect corpus (e.g. the Gonzaga women's letters in Ferrato 1879, weighted up).
4. A design with syllable or word codes among the 1x/2x units.

Requests this session: archive.org 13 (1 advancedsearch, 6 metadata, 6 `_djvu.txt` downloads), all 1.5 s
apart, descriptive User-Agent. No other hosts, no logins, no subagents.

## Extra regions, pass A (replacement)

Blind sign-by-sign transcription of the 8 extra-region line crops (`f8_left_L1-L4`, `f8_right_L12`, `f9_top_L1-L3`)
into `passA_extra.tsv`, replacing a run that was interrupted over budget before it pushed a pass A. Read only the
"Segmentation" section's sign set (0-9 plus `y`, no group boundaries) and the manifest's crop descriptions first;
did not read `passB_extra.tsv` content, `ciphertext.txt`, `passA.tsv`, `passB.tsv` or `passC_native.tsv` -- this
pass is blind by construction, not reconciled against anything. Sign counts per line: f8_left_L1 60, f8_left_L2 21
(+ clear Italian tail, not transcribed), f8_left_L3 41 (positions 1-6 flagged low-confidence, letter-like cursive
shapes), f8_left_L4 48, f8_right_L12 42 (39 inline + 3 for a "184" written below the line, flagged as possibly a
scribal carry rather than ciphertext), f9_top_L1 31 (7 signs, clear "et mi", then 24 more signs), f9_top_L2 43,
f9_top_L3 26 (+ clear Italian tail "mi suo ... Dio facia", not transcribed). Total 312 signs, close to the
manifest's ~280-300 estimate. Confidence marked `low` throughout except a handful of bolder, unambiguous shapes
marked `med` (8's, `y`'s, a couple of clear 0/2 digits); the whole set should be read as rough given the density
and the known 4/9 and 1/7 confusability noted in Segmentation. No reconciliation against pass B, no decoding, no
novelty wording. One Sonnet subagent was available per brief but not used -- the crop set was small enough for one
session to read directly.

## Full text: extras reconciled and solver rerun (24 Sept 2026)

Started by session_018fT9e8dT9qbRixPBdcv5Vb, which reconciled the extra-region signs and ran the target and the
noise controls (`solver/run_full.sh`). It went idle before the unit-null calibration solves and the crib test had
finished. An Opus finisher (LANE G) re-ran those two steps in the foreground from the same script, seeds and
models, with the model rebuilt from `tools/data/it16`. `calib_dump.py` reproduced the committed control ciphers
byte for byte. The outputs were committed after the process exited (04:41-04:56 UTC). **Result: a clean negative
with matched controls. No reading is claimed. Grade counts: H 0, C 0, S 0, M 0, I 0.**

**Input.** `ciphertext.txt` and `inventory.tsv` now cover all 24 lines in the file: 16 main lines plus the 8
extra-region lines (`f8_left_L1-L4`, `f8_right_L12`, `f9_top_L1-L3`). `reconcile.py --check` and
`solver/make_signs_full.py --check` both pass. That gives 900 signs, H 755 and M 145 (M share 16.1 %): 18.4 % of
the 588 main-line signs (108) and 11.9 % of the 312 extra-region signs (37). `solver/signs_full.txt` groups
them into 7 unbroken cipher runs, split wherever a clear-text phrase interrupts the cipher. Under the 1x/2x design
they parse into 642 units of 30 types, with 3 parse exceptions.

**Matched controls at the new length (rule 3).** These use held-out Italian, the same 1x/2x inventory and the
target's line lengths, with 540 units giving 862-961 signs. They are solved blind with the training model, 5
seeds each (`solver/runs_full/control_*`):

| control | mean letter accuracy | per seed | same control at 588 signs |
|---|---|---|---|
| y letter, 0 % noise | 0.998 | 1.00 0.99 1.00 1.00 1.00 | 1.000 |
| y letter, 5 % noise | 0.936 | 0.96 0.91 0.94 0.94 0.94 | 0.917 |
| y letter, 10 % noise | 0.864 | 0.88 0.84 0.87 0.88 0.85 | 0.754 |
| y letter, 15 % noise | 0.700 | 0.81 0.42 0.75 0.75 0.76 | 0.244 |
| y null (6.6 %), 5 % noise | 0.926 | 0.93 0.91 0.96 0.91 0.92 | 0.781 |

The extra length did what was hoped for: the 10-15 % noise band is now readable (86 % and 70 %, against
75 % and 24 % at 588 signs). The target's M share (16 %) is an upper bound on its misreading rate, because M
means the readings did not all agree, not that the sign is wrong. So the target sits inside the band the solver
now reads.

**Target** (`solver/runs_full/target*`). Model score per unit, guard included, against nulls:

| design | units | types | score/unit | null (kind) | z | output |
|---|---|---|---|---|---|---|
| 1x/2x, y letter | 642 | 30 | -3.484 | -3.982 ± 0.005 (signs) | 91.9 | not Italian |
| 1x/2x, y letter | 642 | 30 | -3.484 | -4.052 ± 0.024 (units) | 24.0 | not Italian |
| 1x/2x, y null | 600 | 29 | -3.640 | -4.033 ± 0.041 (signs) | 9.6 | not Italian |
| 1x only, y letter | 750 | 20 | -3.981 | -4.242 ± 0.037 (signs) | 7.0 | not Italian |
| 2x only, y letter | 779 | 21 | -3.909 | -4.219 ± 0.034 (signs) | 9.1 | not Italian |

The best output begins `datouaelomisuriaeileanoesaofrateleisoirisoltadifarle|imitaiacetroideuaelicenuosistrs...`.
It has scattered short strings (`fratel`, `di farle`, `stato et`, `consi`) but no run of words.

**Calibration, same unit-null solve** (`solver/runs_full/ctl_unitnull_n*.txt`). These controls are matched to the
target's length (558-568 units):

| | score/unit | unit-shuffle null | z | output |
|---|---|---|---|---|
| control, 10 % noise | -3.059 | -3.931 ± 0.031 | 27.8 | Italian, readable (`...deceesareconieearhaentoeconosecoutoterrore...`) |
| control, 15 % noise | -3.326 | -3.971 ± 0.035 | 18.5 | Italian, largely readable |
| **target** | **-3.484** | -4.052 ± 0.024 | 24.0 | not Italian |

At 588 signs the target's score could not be told apart from a 10 % noise control's (NOTES, "Joint-segmentation
solver"). At 900 signs it can. The target scores 0.43 per unit below the 10 % control and 0.16 below the 15 %
control, and its output does not read where theirs do. Its z against the unit null lies between the two
controls', so its sign order carries structure. That structure does not decode as Italian letters under this
design and model.

**Crib test** (`solver/cribs.py`, `solver/runs_full/cribs_*.txt`, 3 restarts). The anchor is the only long repeat
in the text: the 9-unit run `17 9 6 10 20 4 y 3 18`, found at f8_left_L1 pos 36-48 and f8_L3 pos 3-15. Each
9-letter candidate fixes those units, the rest of the key is annealed, and the result is compared with the
unconstrained solve.
- *Method control* (a synthetic cipher at 10 % noise, a 9-unit window of its true plaintext as the right crib, the
  same 20 wrong candidates). The true crib `apitornoi` scored +0.524 per unit. Every wrong crib scored between
  -0.467 and -1.639. The method separates the right crib from wrong ones by about 1.0 per unit.
- *Target* (unconstrained -3.549 per unit). 19 of the 20 candidates scored negative (-0.396 to -1.803), and
  `vostrofra` conflicts with the anchor. One candidate, `suofratel`, scored +0.128. That is a quarter of the
  control's true-crib margin, and in absolute terms (-3.422) it is only 0.06 above the 6-restart unconstrained
  target solve in the table above. The unconstrained solve already reads the anchor as `..oesaofrat..` both
  times, so this crib mostly confirms the solver's own optimum. With the crib fixed, the text around it still
  does not read (`dutocuelomiscriueilaanoasuofrateleisonrisoltadifarla`). This is not a reading, and no token is
  graded. `suo fratello` is a candidate for the next solver to test, not a result.

**What the negative means.** On a matched 900-sign 1x/2x homophonic control, the solver reads 99.8 % of letters
clean, 93.6 % at 5 % sign noise, 86.4 % at 10 % and 70.0 % at 15 %. The target does not read under any of the
four designs. The crib test is informative on the control and gives no reading on the target. The negative now
holds more firmly than at 588 signs: a transcription-noise explanation would need worse than 15 % noise, while at
most 16 % of the signs are uncertain. It still holds only (a) for a pure letter-substitution design over these
units, (b) for this transcription, and (c) in 16th-c. literary or chancery Italian as the it16 model captures it.
The live alternatives are a nomenclator or code-word design among the 1x/2x units, a segmentation other than the
prefix-free 1x/2x design, or a strongly Mantuan and phonetic orthography.

Not run: the last block of `run_full.sh` (the Ferrato-weighted model `it16_ferr10`, NOTES next move 3). It was
outside this brief. Suggested follow-ups: that block; a nomenclator-aware solver (units allowed to stand for
syllables or words); crib tests anchored on `suofratel` with 6 restarts and a matched control whose true crib sits
on a repeat. No network requests this session; compute only.

## Class gate, Ferrari 1999 (local runner, LOCAL-QUEUE L8, 27 Sept 2026)

Landed verbatim from the owner's desk runner, PR 38; row L8 asked whether Ferrari 1999 ("Mantoue et les Gonzague
de Nevers", cited in Tomokiyo's Nevers bibliography) prints or summarises Marguerite Paléologue's ciphered letters
to her son.

**blocked**, not a content answer: the academia.edu link -- "I Gonzaga e Nevers / Les Gonzagues et Nevers", in the
Ugo Bazzotti exhibition catalogue, pp. 15-30 (Nevers, Palais Ducal, 16 Oct-7 Nov 1999; Mantova, Palazzo Te, 18
Feb-26 Mar 2000; Bozzolo, Mantova, 1999) -- showed a "Just a moment..." / "Performing security verification" bot
check throughout the attempt (exact URL:
https://www.academia.edu/23839255/I_Gonzaga_e_Nevers_Les_Gonzagues_et_Nevers_in_Mantova_e_i_Gonzaga_di_Nevers_Mantoue_et_les_Gonzagues_de_Nevers_a_cura_di_U._Bazzotti_catalogo_della_mostra_Nevers_Palais_Ducal_16_octobre-7_novembre_1999_Mantova_Palazzo_Te_18_febbraio-26_marzo_2000_Bozzolo_Mantova_1999_pp._15-30
). No document reader or login interface was reached; zero pages of the paper were read. This is an access
failure, not an absence finding -- it does not say Ferrari is silent on the ciphered letters, only that this
attempt could not check. A Helka catalogue record for the bilingual 1999 exhibition catalogue was located
(https://kansalliskirjasto.finna.fi/Record/helka.9935145810306253) as an access lead only, no readable copy
obtained. `tools/data/catalogue_ladders.tsv` was consulted; this is an edition-content check, not a claim about
whether BnF fr.4687 itself has images online. Status unchanged: `blocked`.

## Web and blog check (CHECK-fr4687-paleologue-nevers (account-4), 2 Oct 2026)

Per `.claude/briefs/check-solved.md`, "Required step: Open web and blog comment threads" (28 Sept 2026). Ten WebSearch
queries, every plausible hit opened and its comment thread read (WebFetch; one request each).

(a) Plain web searches:
1. `"Marguerite Paléologue" "Louis de Gonzague" 1562 lettres chiffre Nevers` -- hits: the BnF Archives et manuscrits
   notices for Français 4682, 4687 (ark:/12148/cc577374), 4688, 4702, 4711, 4708, 3315, 3974-3995; Wikipedia "Louis
   de Gonzague, Duke of Nevers". The fr.4687 notice is the catalogue entry itself ("Lettres, en italien, avec
   chiffres ... De 1562 à 1564"); none names a decipherment.
2. `"français 4687" OR "fr. 4687" OR "fr.4687" BnF chiffre Nevers` -- hits: the same BnF notice, Wikidata/Wikipedia
   Nevers pages, two unrelated Gallica items (a Nevers town plan, a gradual). Nothing on the cipher.
3. `"lase le mie le posete brusare"` (the clearest clear-text phrase on the leaves, NOTES "What the negative means")
   -- no hit for the phrase; only dialect dictionaries for "brusare" (dialetticon.blogspot.com, Wiktionary,
   casalserugoedintorni.it, ilpavano.it). Not printed anywhere the engine indexes.
4. `Marguerite Paléologue duchesse de Mantoue lettres chiffrées au duc de Nevers 1562-1564 déchiffrement` (the
   folder's title) -- hits: the BnF notices again, the Biblissima IIIF collection manifest for Français 4687
   (iiif.biblissima.fr/collections/manifest/8ae9c5ab...), Clairambault 312-452, Wikipedia. No decipherment.
5. `"Margherita Paleologa" lettere cifrate figlio Ludovico Gonzaga Nevers 1562` (Italian) -- hits: Treccani DBI
   entry (opened; see the check-solved section, item 4: no edition of her letters, no cipher), lombardiabeniculturali
   "Ercole Gonzaga e Margherita Paleologa (1540-1551)" (an archival fonds, earlier years), genealogy and Wikipedia
   pages. Nothing on cipher letters.
6. `Daniela Ferrari "Les Gonzagues et Nevers" OR "I Gonzaga e Nevers" Bazzotti 1999 catalogo` -- hits: Ferrari's
   Festivaletteratura author page, Olschki's Bazzotti page, an academia.edu paper on Carlo I Gonzaga Nevers
   iconography (2013), iris.univr.it "Fine di una Dinastia" (1708), bookseller pages. No copy of the 1999 catalogue
   online.
   Model-solve announcements (check-solved.md): 7. `Paléologue Nevers Gonzaga cipher 1562 "solves" Claude OR GPT`
   -- hits: Schneier on Security "Claude Fable Solves a Historical Cipher" (Sept 2026, the Cyphral Distich), 36kr and
   dev.to and pasqualepillitteri.it reposts of the same, Bourdeau's site index (dbourdeau.github.io/cyphersolver),
   cyphersolver issue #13 (Laurière to Nevers, fr.3625 no.55, 1593) and PR #9 (intercepts for Nevers, fr.3977,
   1589-90, "a deciphered letter from Vincenzo Gonzaga, Duke of Mantua, to the duc de Nevers from September
   1590") -- all other Nevers volumes and a later generation; nothing names fr.4687 or the 1562-64 letters.
(b) Blog site searches:
8. Cipherbrain: `site:scienceblogs.de/klausis-krypto-kolumne Gonzaga Mantua Nevers` -- the only on-site hits are
   Kryptos (2016), "Who can decipher this encrypted letter from the Vatican?" (7 Mar 2018), "A crypto mystery from
   1948", a 2022 stamp post and a 2013 bad-crypto post. The Vatican post was opened and its 19 comments read: it
   is Pallotto to Barberini, 14 May 1628, Barb.lat.6956; the one "Mantova" is inside a commenter's transcription
   ("con le robbe per Mantova"); nothing on Nevers, Paleologue or 1562-64.
9. Cryptiana blog: `site:cryptiana.blogspot.com Nevers Mantua Gonzaga Paleologue` -- one on-site hit, the 2018 archive
   page (cryptiana.blogspot.com/2018), opened and read with its comments: the only Nevers mention is the post
   "Undeciphered letters from Duke of Guise? (ca.1581)" (20 Dec 2018) linking the fr.3995 catalogue; no Gonzaga,
   Mantua, Paleologue, Marguerite or 4687 anywhere on the page or in its comments. Tomokiyo's own pages: the on-disk
   snapshot `sources/cryptiana/` grepped first (zero requests), see the check-solved section, item (3).
10. Cipher Mysteries: `site:ciphermysteries.com Gonzaga Mantua Nevers cipher` -- hits: "Paolo Guinigi and ciphers"
   (2020, Lucca 1400s), "A little more on Savoy" (2010, opened: 15th-century Savoy and the Voynich, no Montferrat /
   Paleologue / Mantua / Nevers mention in post or comments), "New paper on fifteenth century cryptography" (2017),
   Kahn and Montefeltro reviews -- all 15th century; nothing on this correspondence.
(c) Also opened: the BnF notice (through the headless browser; check-solved section item 2) and the Treccani entry.

Result: no decipherment or plaintext of this item located by these queries on 2 Oct 2026 (a search result, never a
novelty verdict, rule 10). The status word stays `blocked` (line 1) on the unread Ferrari 1999 essay, LOCAL-QUEUE.tsv
row L33, not on this check.

## Crib test on `suofratel` with a repeat control (A2-PAL, account 2, LANE-A2PUSH, 3 Oct 2026)

Intake gate before work (01:21 UTC): `tools/intake_gate_check.py fr4687-paleologue-nevers` -> `fr4687-paleologue-nevers:
blocked (line 1) -- already terminal, nothing to gate`, exit 0. Status word unchanged (`blocked`, Ferrari 1999, LOCAL-QUEUE L33);
this step is the compute-only follow-up named at the end of "Full text: extras reconciled and solver rerun".

**Pre-registration (written and pushed before any control or target run).** Script `solver/cribs_repeat.py`. Control:
held-out Italian (`solver/control_heldout.txt`, unseen by `it16_train`), 540 letters, random homophonic key over the
1x/2x + y-letter inventory, the target's line lengths, 10 % sign noise; a 9-letter window of its own plaintext on 9
distinct units is copied 110 letters later with the same units, both copies protected from noise (as the target's anchor
`17 9 6 10 20 4 y 3 18` is seen intact twice). Seeds 1, 2, 3 (it16_train model). Cribs: the true window, 11 wrong
candidates (`cardinale francesco guglielmo monsignor suamaesta ilducadis monferrat lacorteet cheilrede nostrofra
ostrofrat`, cribs.py's 20 cut for the 45-min box) and `suofratel` as a wrong crib. Each crib: 6 restarts x 150,000
iterations, constrained score per unit. Statistic: rank of the focus crib and its margin over the best other crib.
Control passes a seed if the true crib ranks 1st with margin >= 0.30/unit; gate met at >= 2 of 3 seeds. Target
(it16_all model, the same 11 wrong cribs) runs only if the gate is met; `suofratel` reads only if it ranks 1st with
margin >= 0.30/unit. The margin depends on the cipher text itself, so the control's number can differ from the target's.
No token is graded unless both pass.

**Result (runs 01:25-01:43 UTC, `solver/runs_repeat/`).** Control first, then target; both numbers:

| run | focus crib | rank | margin over best other | best other | focus score/unit |
|---|---|---|---|---|---|
| control seed 1 | `ichiorest` (true) | 1/13 | +1.199 | cardinale | -2.729 |
| control seed 2 | `cheauanti` (true) | 1/13 | +0.680 | cheilrede | -3.124 |
| control seed 3 | `econsider` (true) | 1/13 | +1.245 | cardinale | -2.700 |
| **target** | `suofratel` | 1/12 | **+0.657** | cardinale | -3.413 |

Control gate met (3 of 3 seeds, gate 2 of 3). The target's `suofratel` clears its pre-registered gate (rank 1, margin
>= 0.30): its margin, +0.657, sits inside the control's true-crib range (+0.680 to +1.245), just below it. With 6
restarts the 24 Sept test's 3-restart margin over the best wrong crib (+0.524) firms up.

**What it does not show.** The text around the fixed crib still does not read
(`dutocuelomiscriueilaanoasuofrateleisoarisoltadifarle`), and its score per unit (-3.413) stays below the controls'
true-crib solves (-2.70 to -3.12) and barely above the unconstrained target solve (-3.484). The unconstrained solver
already reads the anchor as `..saofrat..`, so the crib mostly agrees with the solver's own optimum, and the wrong cribs
fight it; in the controls the unconstrained optimum is also close to the truth, so the control does not separate
"right crib" from "crib that matches the solver's optimum on a text that is not Italian letters". That confound is
untested. No token is graded S. Grade counts for this step: H 0, C 0, S 0, M 18 (the 9 anchor units at both
occurrences read `s u o f r a t e l` as a candidate), I 0. This is a candidate, not a reading.

Next step (compute only, ~10 min, ~USD 1): the confound control -- the same crib test on unit-shuffled target text
(3 shuffles), with the crib set to whatever the unconstrained solve reads on a 9-unit repeat there; if such
solver-optimum cribs also clear margin >= 0.30, the target's +0.657 means nothing. Only if they do not is the
`suofratel` hypothesis worth a nomenclator-aware or Mantuan-model pass.
Requests this step: none (compute only). Subagents/vision calls: 0.

## Unit-shuffle null for the `suofratel` crib test (A2-PAL2, account 2, LANE-A2PUSH, 3 Oct 2026)

Intake gate before work (02:01 UTC): `tools/intake_gate_check.py fr4687-paleologue-nevers` -> `fr4687-paleologue-nevers:
blocked (line 1) -- already terminal, nothing to gate`, exit 0. Status word unchanged (`blocked`, Ferrari 1999, LOCAL-QUEUE
L33). Brief: `.claude/briefs/runs/2026-10-03-acct2-a2-pal2.md` (the unit-shuffle null of A2-PAL's crib test, at least 20
shuffles, compute only). Note: this NOTES.md carries no "## Remaining gaps" / "## Escalation" sections (the target is
`blocked`, not `partial`, so `tools/gaps_check.py` skips it); the brief's Verdict text was taken from the brief itself.

**Design (written before the shuffles ran).** Script `solver/cribs_shuffle.py`, driver `solver/runs_shuffle/run.sh`,
outputs `solver/runs_shuffle/s-1.txt` (real target) and `s0.txt`-`s19.txt`. Each null copy keeps both anchor occurrences
(`17 9 6 10 20 4 y 3 18`) in place and permutes every other unit of the segmented target (642 units) across all
non-anchor positions (rng seed 7000+k): unit counts and passage lengths unchanged, order destroyed. Then the identical
test of `cribs_repeat.py target`: same 12 cribs (`suofratel` + the 11 wrong), same 6 restarts, same constrained score per
unit, same seed 11, same model (it16_all, rebuilt from tools/data/it16 as in run_full.sh), statistic = `suofratel` score
minus best other crib. The statistic depends on the context the shuffle destroys, so the null can differ from the target
(rule 3). Box sizing: at A2-PAL's 150,000 iterations one copy costs ~4 min (20 copies = 80 min, over this job's 30-min
box), so iterations were cut to 30,000 for every run and the real target was re-run at that same setting to keep the
two sides matched: it reproduces A2-PAL's margin exactly (+0.657 over cardinale, `suofratel` -3.416/unit vs -3.413 at
150k), so the cheaper setting reaches the same optimum on the real text.

**Result (runs 02:03-02:17 UTC).**

| run | `suofratel` score/unit | margin over best other | best other |
|---|---|---|---|
| real target (6 x 30k) | -3.416 | **+0.657** | cardinale |
| 20 unit shuffles | -4.349 to -4.144 | -0.015 to +0.228; mean +0.081, sd 0.070, p95 +0.207 | cardinale (18), suamaesta (2) |

The real margin is above every one of the 20 shuffles (empirical p < 1/21) and above the shuffle p95 (+0.207) by
+0.450, about 8 sd above the null mean; no shuffle reaches the 0.30 gate. So the pre-registered condition holds: the
candidate is **not** rejected by this null. What it shows: the anchor units plus the language model alone favour
`suofratel` slightly (it ranks first in 19 of 20 shuffles, but by +0.08 on average), and most of the real +0.657 comes
from the order of the units around it -- the unshuffled text holds sequential structure that agrees with the crib.

**What it does not show.** It does not separate "`suofratel` is the right reading" from "any crib that matches the
unconstrained solver's optimum on a sequentially structured text wins by this much": the shuffle removes that structure
for every crib alike. The surrounding text still does not read (`dutocuelomiscriueilaanoasuofrateleisoirisoltadifarle`),
and its score per unit (-3.416) stays below the controls' true-crib solves (-2.70 to -3.12). Grade counts for this step:
H 0, C 0, S 0, M 18 (the 9 anchor units at both occurrences, `s u o f r a t e l`, unchanged as a candidate), I 0. No
token is graded S; this is a candidate, not a reading.

Next step (compute only, ~15 min, ~USD 1): the solver-optimum crib null on the real target -- take 10-20 other 9-unit
windows (repeats first, then single windows), set each window's crib to what the unconstrained solve reads there, run
the same crib test (same 11 wrong cribs, 6 x 30k) and report where `suofratel`'s +0.657 falls among those
solver-optimum margins; only if it stands above their p95 is a nomenclator-aware or Mantuan-model pass worth running.
Requests this step: none (compute only). Subagents/vision calls: 0.

## Solver-optimum crib null on 15 other windows (A2-PAL3, account 2, LANE-A2PUSH, 3 Oct 2026)

Intake gate before work (02:39 UTC): `tools/intake_gate_check.py fr4687-paleologue-nevers` -> `fr4687-paleologue-nevers:
blocked (line 1) -- already terminal, nothing to gate`, exit 0. Status word unchanged (`blocked`, Ferrari 1999, LOCAL-QUEUE
L33). Brief: `.claude/briefs/runs/2026-10-03-acct2-a2-pal3.md` (the next step A2-PAL2 named, compute only). As A2-PAL2
noted, this NOTES.md has no "## Remaining gaps" / "## Escalation" sections (the target is `blocked`; `tools/gaps_check.py`
-> `SKIP fr4687-paleologue-nevers: status blocked; sections not required`), so the next step is written at the end here.

**Design (pre-registered in `solver/cribs_window.py`'s docstring, pushed as 92715ec0 before any window ran).** One
unconstrained solve of the real target (6 restarts x 30k, seed 11, it16_all): -3.649/unit over 642 units; it reads the
anchor as `niopretes` at this setting. Eligible windows: 9 consecutive units in one passage, 9 distinct unit types, not
overlapping either anchor occurrence -- 89 such windows, **none on a repeat** (the anchor is the target's only repeated
9-unit window), so 15 single windows were taken at evenly spaced positions (`solver/runs_window/windows.tsv`). Each
window's crib = the unconstrained solve's letters there; then the identical test of A2-PAL2's matched setting (that crib
+ the same 11 wrong cribs, 6 x 30k, seed 11, constrained score per unit); statistic = crib score minus best wrong crib.
Pre-registered condition: `suofratel`'s +0.657 (A2-PAL2, same setting) survives only if it stands above the p95 of the 15
window margins. Extra row A: the same test with the anchor's own solver-optimum crib `niopretes`. The window margins
depend on each window's own context, so they can differ from the anchor's (rule 3). Runs 02:41-02:58 UTC,
`solver/runs_window/w*.txt` (`run.sh` regenerates them).

**Result.**

| run | crib | score/unit | margin over best wrong | best wrong |
|---|---|---|---|---|
| anchor (A2-PAL2) | `suofratel` | -3.416 | **+0.657** | cardinale |
| anchor, solver optimum (A) | `niopretes` | -3.574 | +0.499 | cardinale |
| 15 other windows | solver optimum each | -3.626 to -3.558 | +0.225 to +0.848; mean +0.444, sd 0.169, **p95 +0.764** | cardinale 5, ilducadis 4, lacorteet 3, suamaesta 2, nostrofra 1, monsignor 1 |

Window margins in order 0-14: +0.506 +0.414 +0.488 +0.292 +0.375 +0.369 +0.335 +0.848 +0.349 +0.348 +0.225 +0.728 +0.606
+0.328 +0.444. `suofratel`'s +0.657 ranks 3rd of 16 (windows 7 `eintrolae` +0.848 and 11 `tadaceuoe` +0.728 are higher)
and sits below the window p95 (+0.764). 13 of the 15 solver-optimum cribs, none of which reads as Italian, also clear
A2-PAL's 0.30 gate. **The pre-registered condition fails:** on this target the crib test cannot tell `suofratel` from
whatever the solver happens to read at a window, so the margin gives the candidate no support. What does differ: at the
anchor, `suofratel` scores better (-3.416) than the solver's own reading there (-3.574) and than every window crib
(best -3.558), i.e. it is a better optimum the 30k unconstrained search did not find -- a score difference of about
0.14/unit, inside what a language-model optimum on a non-reading text can give, and not tested against a control here.

**What it does not show.** It is not a negative on the target's design or language: it says only that this crib test,
at this length and noise, has no discriminating power for a 9-letter crib on fr.4687 (rule 3, a test that could not
fail differently). Grade counts for this step: H 0, C 0, S 0, M 18 (the 9 anchor units at both occurrences, `s u o f r a t
e l`, kept as a candidate only), I 0; no token graded S. Rule 3's third-attempt clause: three crib-test passes (A2-PAL,
A2-PAL2, A2-PAL3) on the same hypothesis with the same instrument; the last one shows the instrument cannot license it,
so the `suofratel` crib test is [retired] as an instrument ("untested-by-this-tool", not refuted); only a different
instrument or new material reopens it.

Next step (not crib-test tuning): none cheap in compute on the present transcription. The status word stays `blocked`
on Ferrari 1999 (LOCAL-QUEUE L33); a different instrument for `suofratel` would be a nomenclator-aware solve (the
1x/2x + y inventory read as code groups, not letters) with its own matched control first, ~USD 3, only if a lane brief
names it. Requests this step: none (compute only, no network). Subagents/vision calls: 0.

## While waiting (RUN4-WAITBF, 4 Oct 2026)

- Action that depends on nobody: the different instrument this folder names for `suofratel` -- a nomenclator-aware solve reading the 1x/2x + y inventory as code groups, not letters, with its own matched control run first (tools/family_run.py discipline), ~$3, once a lane brief names it. Ferrari 1999 (LOCAL-QUEUE L33) stays the outside blocker for the status word.
