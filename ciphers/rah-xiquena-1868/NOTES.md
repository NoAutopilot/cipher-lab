found-solved

**Status correction, 25 Sept 2026 (LANE R6 worker Y10):** the top line above was `open`, set by LANE CX2's
check-solved sweep before the image was seen. The image (all 8 leaves now fetched, see the "Y10" section
below) shows this item is not a cipher at all: the archived "Copia del telegrama cifrado" is a plaintext-only
file copy, certified `Es copia conforme` and signed by the Conde de Xiquena. Same pattern as
`ciphers/rah-canada-1869/AUDIT.md`'s correction of that target — a catalogue title naming a "telegrama/nota
cifrado" describes what was transmitted, not what the archive kept on file. Status word set to `found-solved` by the LANE R6 orchestrator, 25 Sept 2026 18:55 UTC: the archive keeps the telegram's clear text, so there is no ciphertext left to read, and `solved` would imply a decipherment of ours. Not classified as to novelty here
(rule 10) — routed to LANE V6.

**Verifier (V6-XIQ, 25 Sept 2026):** all 8 leaves eye-checked, no ciphertext anywhere; class **N0**, key n/a; status `found-solved` confirmed (no ciphertext survives, the cipher telegram's clear text is the archive's own). Board: retire, never count as a solve or a catch. See AUDIT.md for the safe sentence.

RAH's own OAI-PMH DIDL record (`oai:bibliotecadigital.rah.es:15711`, registro id 15711, found via a keyed Europeana search this pass) read in full by this worker: no `dc:description` field and no "Publicado" note anywhere in its metadata, only creator/date/title/rights/subject/8 page-image refs; Google Books full-text searched (`GOOGLE_BOOKS_KEY`, `&country=US`) for "Xiquena" + "telegrama" + "cifrado"/"Isabel", 6 hits, none a confirmed match (control: the query mechanism returns real full-view hits, e.g. `Diario de las Sesiones de Cortes` and `Gedeón` 1898, proving the search executes; none names this telegram); one leaf fetched via `tools/browser_fetch.js --binary` (idImagen 10141611, page 1 of 8) and eye-checked by this worker, confirming the catalogue's own "Leg. XXIV, nº 158" archival mark but showing only the dossier's blank cover, not the telegram text.

## Check-solved (LANE CX2, 25 Sept 2026, CX2-MISC2)

Fresh six-source sweep plus the job brief's three named leads (RAH OAI record, Gaceta de Madrid/BOE historical gazette, Hemeroteca Digital BNE, Burdiel's Isabel II biography):

1. **RAH catalogue record.** The 24 Sept sweep never located this item's own registro/OAI id (it only had the CONTENTdm-style viewer path `1008498`). Found this pass via Europeana's keyed search API (`api.europeana.eu/record/v2/search.json`, `wskey=$EUROPEANA_API_KEY`, query `Xiquena telegrama`): registro id **15711** (`bibliotecadigital.rah.es/es/consulta/registro.do?id=15711`), 8 page images `idImagen` 10141611-10141618. Fetched `https://bibliotecadigital.rah.es/oai/oai.do?verb=GetRecord&identifier=oai:bibliotecadigital.rah.es:15711&metadataPrefix=didl` directly with curl (not Anubis-blocked, per the Access playbook): the DIDL record's only `oai_dc:dc` fields are creator ("Toledo y Acuña, José Álvarez de, Conde de Xiquena" -- identifying him as subsecretario de Estado, per a separate RAH authority-record hit, `consulta_aut/registro.do?id=4913`), date 1868, format, two identifiers, language, rights (Public Domain Mark), subject ("Archivo de Isabel II"), type, and the title already on file -- **no `dc:description` field at all**, so no "Publicado por..." note exists to find (unlike the Rodríguez-Villa-printed Morillo despatches from the same 24 Sept RAH sweep, which did carry one).
2. **Gaceta de Madrid / BOE historical gazette.** `boe.es/diario_gazeta/hemeroteca.php?a=1868&m=5&d=3` loads (HTTP 200) but its search form (`buscar/gazeta.php`) indexes structured fields (reign period, department, document type) for official provisions -- laws, decrees, appointments -- not free-text search of gazette body content or private correspondence; no page-linked full text found this way. Genre mismatch noted: the Gaceta publishes government acts, not a private cipher telegram between the Queen and her subsecretario, so a miss here is expected rather than informative; not treated as a controlled negative.
3. **Hemeroteca Digital BNE.** `hemerotecadigital.bne.es` answered HTTP 403 to a plain curl fetch (both the card page and a results query), one attempt, not retried, per the good-citizen rule. Not reachable from this session; flagged for a future browser-tool or local-runner pass.
4. **Burdiel / Isabel II correspondence editions.** Google Books: Isabel Burdiel's *Isabel II* (2011, `W2yZuUMnzxgC`) is `NO_PAGES` (not full view from the cloud). A combined query `"Xiquena" "telegrama" Isabel` (6 hits) and `"Xiquena" "cifrado"` (6 hits) returned only `NO_PAGES` items (Vilches 2007, Pí y Margall 1902, Hernández-Girbal 1963, Cortés Cavanillas 1982) and several `ALL_PAGES` 19th-century `Diario de las Sesiones de Cortes` volumes (1877-1890) and the satirical weekly *Gedeón* (1898) whose co-occurrence of the three terms is very unlikely to describe this specific telegram (parliamentary-diary and satire-magazine corpora spanning decades) and was not opened page-by-page to confirm either way -- reported as an unconfirmed lead, not a hit.
5. **Community lists / DECODE / Bourdeau / Aymeloglu.** Unchanged from the 24 Sept sweep already in this file (no hit for "Xiquena" in any of the four); not re-run this pass, no new source surfaced in items 1-4 above to search for.
6. **Sibling items in the same RAH file.** Path 1008499 (undated, title/author only) still not opened -- unchanged, out of this brief's scope (check-solved only, no deep work).

**Image (one fetch, per this brief's cap).** `tools/browser_fetch.js --binary` on `idImagen=10141611` (page 1 of 8): a plain archival dossier cover reading "Leg. XXIV, nº 158" in a modern archival hand (verifier correction, 25 Sept 2026; was "period hand"), matching the catalogue's Legajo/Nº citation exactly, no cipher text on this leaf. Saved to `ciphers/rah-xiquena-1868/images/p1.jpg`. The remaining 7 leaves (10141612-10141618, presumably including the telegram text) are not fetched this pass (brief's one-fetch cap; a future access worker should pull the rest under a manifest, not one at a time by hand).

No source in this sweep identifies, quotes or describes the content of this telegram. Nothing here is claimed as new, unpublished or first (rule 10). Requests: `bibliotecadigital.rah.es` 2 (1 OAI GetRecord, 1 `browser_fetch.js --binary` image fetch, 2 navigation attempts inside that one fetch), `api.europeana.eu` 1, `boe.es` 2, `hemerotecadigital.bne.es` 2 (both 403, one retry, per host), `googleapis.com/books` 3, WebSearch 5.

# Copy of a ciphered telegram, Isabel II / Conde de Xiquena, 3 May 1868 — RAH Sig. 9/6963

QUEUE row: E1, "Europeana and Real Academia de la Historia digitised candidates" (LANE S scout of 24 September
2026). Real Academia de la Historia, Madrid, Archivo de Isabel II, Sig. 9/6963, Legajo XXIV, Nº 158. Catalogue
title: "[Cartas y documentos cruzados entre la Reina Isabel II y el Conde de Xiquena. Copia del telegrama
cifrado al Ministro de la Reina en Munich. 3 de mayo de 1868] [Manuscrito]." A copy of a ciphered telegram to
the Queen's minister in Munich, kept among an exchange of letters and documents between Isabel II and the
Conde de Xiquena (subsecretario de Estado in 1868). Same archive and reign as `ciphers/rah-canada-1869/`
(Sig. 9/6958) in the same batch; that target's search log is read and reused below where it applies —
different item, no key lead shared between them.

Same small RAH file (path 1008498 for this item) also holds path 1008497 (a plain minute on the Infanta's
wedding announcement, not ciphertext) and path 1008499 (undated, title/author fields only read, not opened
for content) — scout flagged 1008499 as a possible sibling worth a look before any solve attempt; not opened
this pass (out of this brief's scope, which is check-solved only).

## Editions-first check (24 September 2026)

No dedicated documentary edition of Isabel II's correspondence with the Conde de Xiquena, and no edition of
her 1868 exile-period diplomatic correspondence generally, was found. WebSearch (`"Conde de Xiquena" Isabel II
telegrama cifrado 1868`; `Isabel II exilio 1868 telegrama cifrado Munich ministro`; `Isabel II Xiquena
correspondencia edición cartas 1868 1869 archivo publicada`) returned general political-history material on
the September 1868 revolution and Isabel II's exile (the well-known "Todo arreglado. Prim" telegram of 19
September 1868 is a different, unrelated wire), numismatic pages (noise), and two archival leads, neither a
match: (1) the RAE's own catalogue of "Copias de cartas de Isabel II de los años 1869 a 1871"
(`archivo.rae.es/copias-de-cartas-de-isabel-ii-de-los-anos-1869-1871`) — already flagged unread in
rah-canada-1869/NOTES.md; its date range (1869-1871) sits after this item's 3 May 1868, so a match is unlikely
but not ruled out (still returns HTTP 403 to a plain fetch, per that target's note, not retried again this
pass under the one-retry rule); (2) RAH's own "Correspondencia seguida por S. M. Desde 1869 á 1875"
(`bibliotecadigital.rah.es/es/consulta/registro.do?id=13997`), also 1869 onward, not this item's 1868 date, not
opened. No biography of the Conde de Xiquena (Joaquín Gutiérrez de Rubalcava, or whoever held the title in
1868 — not confirmed by this pass) surfaced with a description of this telegram.

## Six-source sweep (24 September 2026)

1. **Web.** Covered above under editions-first.
2. **Print.** No calendar or documentary edition found describing this telegram or this exchange (see above).
   No CSP/HMC equivalent exists for Spanish royal correspondence of this period.
3. **Community lists.** `sources/cryptiana/` grepped case-insensitively for "Xiquena", "Isabel II", "Munich"
   telegram context: no hit at all for "Xiquena"; "Isabel II" and general Spanish-cipher hits
   (`spanish3.htm`, `spanish3D.htm`, `GL.htm`, `valle.htm`, `nevers.htm`) are all 16th-century material
   (Philip II, Farnese, Mendoza correspondence) — a different Isabel II is never referenced, no genuine match.
4. **DECODE.** No login attempted (broken, ASKS row 1). Aymeloglu's cached DECODE catalogue
   (`unsolved-ciphers/catalogue/decode-records.jsonl`, `decode-catalog.csv`, 1187/10107 rows) grepped for
   "Xiquena", "9/6963", "Isabel II" and "Munich": no match.
5. **Bourdeau's repository.** Fresh shallow clone, 24 Sept 2026 (shared with the rest of this batch). No
   target folder or catalogue mention of "Xiquena"; no genuine hit (a combined-pattern grep across the tree
   surfaced only noise from unrelated corpus/frequency files, none containing "Xiquena" itself).
6. **Aymeloglu's repository.** Fresh shallow clone, 24 Sept 2026 (shared). No target folder, no README/
   TARGETS/SHORTLIST/CATALOGUE mention, no BNE/PARES/DECODE scrape row for this item (the scout's own sweep
   already checked this repo's BNE tracker for other RAH items in this batch and found nothing for E1 either).

**GB queries pending** (no Google Books slot this batch): `"Conde de Xiquena" Isabel II telegrama cifrado`;
`Isabel II 1868 Munich ministro cifrado`; `"9/6963" RAH Isabel II`.

## Verdict

*Superseded 25 Sept 2026 by the Y10 capture and AUDIT.md: the item holds no ciphertext; status `found-solved`, N0. Kept as the CX2 record.*

**open**, stage 2 verified unsolved (conditional: the RAE 1869-71 letters catalogue and RAH's own "1869 á
1875" correspondence catalogue are both unread and post-date this item; the two unopened sibling items in the
same RAH file, especially undated path 1008499, are not ruled out as a plaintext or decipherment sitting
beside this telegram; PARES was not queried, out of this brief's hosts; Google Books is outstanding). No
source in this sweep identifies, quotes, or describes the content of this telegram. The item's own catalogue
record carries no "Publicado por..." note, unlike the two Rodríguez-Villa-printed Morillo despatches the scout
found in the same RAH sweep — a genuine cryptanalysis candidate if pursued, once the image is in hand and the
two sibling items are checked.

## Copy status

Copy-free per the scout's rights-field read: `bibliotecadigital.rah.es`, Public Domain Mark 1.0, no login. The
image itself was not opened at full resolution this pass (the record page's viewer is a JS-driven loader,
`catalogo_imagenes/grupo.do?path=1008498`, that did not yield a static image URL to curl) — this is an access
task for a future worker with the browser tool, not a copy order, so no REQUEST.md is drafted.

## Request counts (this target)

WebSearch: 4. `sources/cryptiana/`: local grep only, no network request. `github.com`: shared shallow clone
with the rest of this batch (2 clones total across N45/N46/N47/E1). No `bibliotecadigital.rah.es` calls this
pass (record already reachable per the scout's own sweep; re-checking it was not needed for a six-source
sweep). No TNA Discovery calls (n/a). No Google Books calls (queries logged above as pending).

## Y10: capture and sibling-key trial (25 Sept 2026, LANE R6)

**(1) Capture.** Fetched the remaining 7 leaves of OAI record 15711 (idImagen 10141612-10141618; p1/10141611
was already on disk from LANE CX2's one-fetch pass) via `tools/browser_fetch.js --binary --profile
/tmp/rah_profile_xiquena`. `bibliotecadigital.rah.es`'s Anubis challenge blocked the first 8 navigation
attempts on a fresh profile (all returned `text/html`, not the image); a plain HTML fetch on the same profile
then showed the challenge had actually cleared (the page rendered the real image in Chromium's native
viewer, title `imagen_id.do (3489×4859)`), and every fetch after that point served `image/jpeg` directly
(one more `text/html` retry on idImagen 10141613, then image/jpeg on attempt 2). All 8 images now on disk,
`images/manifest.json` updated with a one-line description of each leaf. Folder size 12 MB, well under the
30 MB cap. Requests: `bibliotecadigital.rah.es` 14 (7 target images + 6 challenge/retry navigations + 1 HTML
diagnostic fetch), all through the single browser profile, one at a time, ~3 s apart or more (the two initial
navigation bursts to the same idImagen were the exception, needed to establish whether the block was live or
already cleared — no page was fetched in parallel).

**(2) Page-by-page description (lead classes 1-3).** p1: blank dossier cover, "Leg. XXIV, nº 158" in a modern archival
hand (verifier correction; was "period hand"), no text. **p2-p8: continuous plain prose, no cipher signs anywhere** — no digits-as-code, no non-
alphabetic marks, nothing resembling `rah-canada-1869`'s digit+mark nomenclator. p2 opens with the heading
"Telegrama cifrado. 1350 Grupos. Madrid 3 de Mayo de 1868. El Ministro de Estado al Ministro de S.M. en
Munich," then the body starts directly in clear Spanish. Mid-p3 it switches to French for a quoted telegram
text addressed "A Leurs Majestés Apostoliques les Empereurs d'Autriche," announcing the betrothal of Infanta
Isabel and the Conde de Girgenti, signed "(Signé: Isabel. = Francisco.=)" at the top of p4, then reverts to
Spanish for the rest of the instruction. p8 closes "Es copia conforme: El Sub. Secretario de Estado: El Conde
de Xiquena" — a certified true copy, signed by the addressee of the QUEUE row's own biographical note (Conde
de Xiquena, subsecretario de Estado). Full transcription: `ciphers/rah-xiquena-1868/plaintext.txt`.

**Finding: this item carries no ciphertext at all, at any of its 8 leaves.** The catalogue title
("telegrama cifrado") and the document's own heading ("1350 Grupos") describe the telegram as it was actually
*transmitted* over the wire — in cipher, as diplomatic telegrams of this period were. What the ministry kept
on file, and what RAH holds and has digitised, is the office's own clear-text copy of that message, certified
and signed. This is the same pattern the LANE W verifier found and corrected for `rah-canada-1869`
(AUDIT.md): a catalogue description naming a cipher describes the transmission method or a related item, not
necessarily what survives on the leaf. Unlike `rah-canada-1869` (interlinear: cipher line directly below its
own plaintext line, same document), this item is **plaintext-only** — there is no interlinear or adjacent
cipher line to align against.

**(3) Transcription — not applicable.** No cipher signs exist to transcribe; a blind Sonnet pass B and
reconciliation were not run (nothing to transcribe as ciphertext; running a pass on prose that is already
plainly legible Spanish/French would not test anything). Per the brief's own instruction ("if the file carries
the clear text, align it and stop — that is the reading"), stopping here.

**(4) Sibling-key trial (rah-canada-1869's key) — not applicable, not run.** `rah-canada-1869/key.tsv` maps
Arabic digits and ~12 pen marks to Spanish letters (a monoalphabetic substitution for the Conde de la
Cañada's own hand). There is no ciphertext anywhere in this item to apply that key to, and no random-draw
control is meaningful without a ciphertext to test it against. This lead class is skipped for the same reason
lead class 3 stopped: the plaintext is already in hand, directly, with no encoding step to reverse.

**Content (from the plaintext).** Madrid, 3 May 1868. The Spanish Foreign Minister instructs the Minister
Plenipotentiary in Munich to travel at once to Vienna (wherever the Emperor of Austria may be) and: (1)
transmit a telegram from Isabel II and her consort Francisco announcing, in French, the arranged marriage of
Infanta Isabel to their cousin the Conde de Girgenti; (2) discreetly manage the fact that Girgenti — Prince
Cayetano, of the House of Bourbon-Two Sicilies, an Austrian cavalry officer — insists on first completing his
military discharge formalities in Vienna before the wedding, out of personal delicacy, and Isabel II wants the
Austrian Emperor, on replying to her telegram, to himself relieve Girgenti of his captaincy and voice a wish
to see him married — so that the initiative appears to come from Austria, not from the Spanish court, avoiding
any suspicion or complication. Historical context: this is the betrothal, months before the September 1868
revolution that deposed Isabel II, of Infanta Isabel (Princess of Asturias) to Prince Cayetano of
Bourbon-Two Sicilies, Conde di Girgenti — a marriage that did take place (19 May 1868) but ended within
months (Girgenti's suicide, 1871); not evaluated further here (out of this brief's scope).

**Not classified as to novelty** (rule 10) — the marriage and its diplomatic run-up are certainly documented
in general Isabel II historiography (the marriage itself is a known public event, unlike a private cipher
content); whether this specific instruction telegram or its wording has been printed anywhere is unchecked in
this pass and is a question for a verifier, not this worker. Routed **for LANE V6**.

**Sign-off.** No cipher, no key trial applicable, no HYPOTHESES.md row (family_run.py is for cryptanalytic
families; there is nothing here to run a family against). Hosts: `bibliotecadigital.rah.es` 14 (all this
pass; no other host touched). No subagents.
