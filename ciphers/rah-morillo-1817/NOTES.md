partial GAPS203-rah-morillo-1817 (3 Oct 2026, account-4): item 1's numeral block on its own leaf (record 2242, f.32r-v) keyed from the leaf's period Descifrado (key_2242.tsv; `decode_key.py --check` C 237 / M 3 of 240); its plaintext is the 1908 print's, so item 1 stays found-solved.

Per item (moved off line 1 by the LANE NX orchestrator, 26 Sept 2026, rule 5): found-solved (item 1); item 2 partial (key described, not found); item 3 found-solved (V9-MOR, AUDIT.md, 26 Sept 2026: N0, plaintext in print in Portuguesa en Carabobo, 2021, p.37 n.100; key period). Item 3 citation (26 Sept 2026, NX-MOR2): Rodríguez Villa's t.4 (Google Books v3kzAQAAIAAJ, *Documentos justificativos ... contiene los últimos años*, 1908, publicDomain ALL_PAGES) read by full-text search for "Herrera" + "7 de noviembre de 1820" and for "Romerito" -- no hit for this exact letter (only a different, later Herrera-to-Morillo letter "de 20 del actual" re: Romerito/Ferrus/Pedraza is quoted there, p. cited in the volume's own text, a different date); Contreras, *Catálogo de la Colección Pablo Morillo* (Madrid 1988, Google Books ohJPjaGKOk8C), full-text search for "Romerito" "Guanare" confirms this item's own catalogue entry (Sig. 9/7666, ff.420-420v, 7 de noviembre de 1820) exists in print as a description only, no plaintext or cipher table given. t.2 (1815 docs) still not located digitised anywhere. **V9-MOR audit, 26 Sept 2026 (AUDIT.md): item 3 is N0, key `period`, text known** -- its plaintext is printed in Bolívar, González Segovia and Anzola, *Portuguesa en Carabobo* (2021), p.37 n.100 (IA `portuguesa-en-carabobo`), citing this shelfmark; t.2 is Google Books `pirVAAAAMAAJ` (searched, no hit). The H grades below should read C 86 / M 5 / U 6 (AUDIT.md section 3). GAPS-rah-morillo-1817 (2 Oct 2026, account-4): the 2021 print's words are folded into key_5186.tsv and exceptions.tsv (build_key_5186.py), and `tools/decode_key.py --check` now prints C 90 / M 7 / U 0 of 97 (section "GAPS-rah-morillo-1817" below); open-web and blog comment-thread check logged at the end of this file, no decipherment or plaintext beyond the 2021 print located.

# Royalist ciphered letters to/from General Pablo Morillo — RAH cluster (1817, 1817, 1820)

QUEUE row: N1, "Digitised candidates outside the BnF (scout of 24 September 2026)" (the N1 of that section —
**not** the N1 of the earlier "Candidates not on DECODE" TNA section, a different row with the same id).
Three items in one series at the Real Academia de la Historia, Madrid:

1. RAH Sig. 9/7658, leg. 15, ff. 32-34, record id 2242 — "Carta reservada y cifrada del General Enrile a
   Morillo..." 15 Jul 1817.
2. RAH Sig. 9/7657, leg. 14, ff. 155v-156v, record id 1957 — "Morillo al Ministro de la Guerra... propone
   una clave en cifra para comunicar los asuntos reservados." 19 Nov 1817.
3. RAH Sig. 9/7666, leg. 23, ff. 420-420v, record id 5186 — "Herrera a Morillo en carta cifrada dándole
   noticias de Romerito, que iba en busca de Bolívar." 7 Nov 1820.

## Editions-first check (24 September 2026)

Antonio Rodríguez Villa, *El teniente general don Pablo Morillo, primer conde de Cartagena, marqués de La
Puerta (1778-1837): estudio biográfico documentado* (Madrid, 1908-1910, 4 vols. — t.1 Biografía; t.2
Documentos 1815; t.3 Documentos 1816-1818; t.4 Documentos post-1818 to 1837). Found on Internet Archive:
`eltenientegener01villgoog` (Google/NYPL scan, matches t.3, 1816-1818 documents, by content — see below),
`eltenientegener00villgoog` (Google/NYPL scan, scattered dates 1806-1823, consistent with t.1, the
narrative biography), and a 1920 reprint in two volumes, `eltenientegenera01rodruoft` /
`eltenientegenera02rodruoft` (University of Toronto scan, also biography-narrative content, no Romerito/
Herrera hit). **t.2 (1815 documents) and t.4 (post-1818 documents, which would cover the 1820 item) were not
found digitised on Internet Archive under this title this pass** — only t.1 and t.3 are present among the
identifiers found. Fetched all four volumes' full `_djvu.txt` to disk (4 requests, ~4.4 MB total) and
grepped/read them directly (offline, no further host requests for the text search itself).

### Item 1 (9/7658, 15 Jul 1817, Enrile→Morillo) — already printed in clear, cipher passages marked

`eltenientegener01villgoog.txt` prints, under the heading "**Carta reservada y cifrada del general Enrile á
Morillo, dándole cuenta de sus gestiones en España. — Madrid, 15 de Julio 1817**" (matching the RAH
catalogue description verbatim, including the exact date), the full plaintext of the letter, with two
footnote markers in the original scan: `(1) Lo que sigue en cifra` ("what follows is in cipher") and later
`(1) Desde aquí en cifra` ("from here on in cipher"), which mark, paragraph by paragraph, which passages of
Morillo's own copy were originally enciphered. The letter opens: "Mi querido D. Pablo: Figúrese usted cuál
estaré con la carta que de usted he recibido de Chaguaramas, y con lo que en ella me deja usted de decir. No
la he descifrado aún toda..." (Enrile says he has not yet finished deciphering *Morillo's* letter to *him* —
a separate, reciprocal cipher use, not this folio). This is a direct, unambiguous identification of this
exact letter by date, sender, recipient and content, already deciphered and set in type in 1908. Per
CLAUDE.md rule 10, this rules out "open" for this item.

Grade: **H** (read from the printed edition itself, quoted verbatim above) for the letter's plaintext and
for the fact that it was originally in cipher; the underlying RAH manuscript's actual cipher signs were not
examined (no image opened this pass).

### Item 2 (9/7657, 19 Nov 1817, Morillo's cipher-key proposal) — letter text printed, key table not found in print

`eltenientegener01villgoog.txt`, item "655. — Morillo al Ministro de la Guerra sobre promesa de cumplir la
última Real orden reservada... y conveniencia de emplear una clave de cifras para su correspondencia
secreta. — Idem, id." (same dateline as the surrounding items, Cuartel general de Calabozo, 19 Nov 1817) —
again matching the QUEUE row's catalogue description almost verbatim. The letter's own text is printed in
full and is **not itself in cipher**: Morillo tells the Minister of War "por lo que toca á las cifras, me ha
parecido conveniente el proponer á V. E. las que demuestra la adjunta clave, que ya tengo usada en los
asuntos de reserva... con la diferencia de haberla variado ahora." The next item in the edition (656) moves
straight to an unrelated subject — **the "adjunta clave" (enclosed key table) referred to is not reproduced
in this printed edition**, consistent with 19th/20th-century editorial practice of omitting tabular
enclosures. So: the letter proposing the cipher is already in print (rules out "open" for the letter as
such), but the key itself, if it survives at RAH as this catalogue row implies, does not appear to be
published — a real "key was in the archive beside the letter" candidate (LESSONS.md) if the RAH folio still
holds the table Morillo describes.

### Item 3 (9/7666, 7 Nov 1820, Herrera→Morillo re: Romerito/Bolívar) — not found in the volumes checked

No "Herrera"/"Romerito" match relevant to this item in any of the four volumes fetched (t.1 and t.3 by
content; the two 1920-reprint volumes also biography-narrative, not documents-for-1820). A global
archive.org full-text search for "Romerito" (5,646 hits) returns entirely unrelated 20th-century material
(a footballer's nickname, novel and play characters) — far too generic a term to search usefully without
the specific volume. **t.4, the documents volume that would cover 1818-1837 and thus 1820, was not located
digitised on Internet Archive this pass** (searched by title variants; may exist only as a physical/
HathiTrust/Google Books copy not checked here — outside this brief's Google Books slot). This item stays
open pending that volume.

## Six-source sweep (24 September 2026)

1. **Web.** Not separately re-run this pass beyond the Europeana/RAH scout already on QUEUE.md (23-24
   Sept) that surfaced this cluster; the editions-first check above supersedes a generic web search for
   this specific claim.
2. **Print.** Rodríguez Villa, above — the decisive source. Morillo's own memoirs/*Relación de los
   principales sucesos* were not separately checked this pass (Rodríguez Villa's edition already quotes
   primary correspondence directly, a stronger source than a later memoir for this purpose).
3. **Community lists.** `sources/cryptiana/` grepped for "Morillo": one match (`web/venetian.htm`), a false
   positive — "Sforza[?] Palavicino" mentioned in an unrelated Venetian dispatch has no "Morillo" text
   nearby; re-checked, no actual "Morillo" string in that file (grep hit was on a different query in this
   sweep's shared search, corrected here: no cryptiana match for "Morillo").
4. **DECODE.** No login attempted (broken, ASKS row 1). Aymeloglu's cached DECODE and BNE catalogues
   (`unsolved-ciphers/catalogue/decode-records.jsonl`, `bne-records.jsonl`) grepped for "Morillo", "9/7657",
   "9/7658", "9/7666", "9/76": one apparent BNE hit on "9/76" is a false positive (`MSS/1869/76`, an
   unrelated 1622 letter of Gonzalo Fernández de Córdoba) — no genuine match.
5. **Bourdeau's repository.** Fresh shallow clone, 24 Sept 2026. No target folder or catalogue mention;
   the only "Morillo" hits are incidental mentions in unrelated corpus files (`napoleon/an_ir.txt`, period
   French text naming "Morillo" among other Spanish generals).
6. **Aymeloglu's repository.** Fresh shallow clone, 24 Sept 2026. No target folder, no README/TARGETS/
   SHORTLIST/CATALOGUE mention, no PARES/BNE scrape row (checked under DECODE above).

**PARES.** One attempt via the browser tool at `pares.mcu.es` searching "Morillo cifra" / "9/7657" /
"9/7658": not reached this pass (budget spent on the decisive Rodríguez Villa find; the RAH items are a
different repository from PARES's Consejo de Guerra/Estado holdings named in this brief, and the editions
check already answers the novelty question for item 1 without it). Left for a follow-up worker if
Consejo de Guerra/Estado companion papers are wanted.

**Google Books sweep (24 September 2026, LANE S worker H, holding the Google Books slot — key+country=US,
filter=full):** 3 queries run, >=2s apart. `"clave" Morillo Enrile 1817 cifra Rodríguez Villa` returned zero
results. Two returned real hits:
- `Rodríguez Villa Morillo tomo IV 1820 documentos` (4 results) confirms t.4 of Rodríguez Villa's edition
  exists in print (cited by other authors — e.g. Lecuna, *Crónica razonada de las guerras de Bolívar*, 1950,
  "Morillo al Ministro de la Guerra. Valencia, 28 de agosto de 1820. Rodríguez Villa, IV, 223") but none of
  the 4 hits is itself a full-view scan of t.4 that could be fetched and grepped — they are other books
  *citing* t.4's pagination, which corroborates that t.4 covers 1820 (as the Editions-first check inferred)
  but does not supply its text. t.4 remains not located in full view on Internet Archive or Google Books.
- `"Romerito" Bolívar Morillo 1820 Herrera` (2 results) — the more significant hit. Remedios Contreras
  (Real Academia de la Historia), *Catálogo de la Colección Pablo Morillo, conde de Cartagena* (Madrid,
  1988), a specialist archival catalogue of this exact RAH collection, prints consecutive entries: "4.528 ...
  Bolívar para Romerito. Guanare, 6 de noviembre de 1820. Manuscrito, firma autógrafa, 1 f. Sig. 9/7666, leg.
  23, f) f.419." and "4.529. Herrera a Morillo en carta cifrada dándole noticias de Romerito, que iba en
  busca de Bolívar" — matching item 3 (RAH Sig. 9/7666, leg. 23, ff. 420-420v, "Herrera a Morillo en carta
  cifrada dándole noticias de Romerito, que iba en busca de Bolívar," 7 Nov 1820) almost word for word, with
  the catalogue's f.419 sitting immediately before item 3's own f.420-420v. This is a professional archival
  catalogue's *description* confirming the item's existence, date and content — not a decipherment or
  plaintext transcription (the snippet gives no ciphertext or reading), so it does not move item 3 to
  found-solved. It does mean item 3's record is independently documented in a 1988 published catalogue, not
  only in the RAH's own online database — useful for a verifier's print-search log, and confirms this
  catalogue (Contreras 1988) as a source worth checking directly (not yet fetched in full) for items 1 and 2
  in this cluster too, and for any neighbouring ciphered items in the same legajo 23 the online catalogue may
  not have surfaced.

## Verdict

**found-solved** for item 1 (9/7658): F1-leaning — the letter's plaintext has been in print since 1908
(Rodríguez Villa), with its cipher passages explicitly marked, but neither the RAH catalogue record nor
Europeana's indexing of it (the source that surfaced this cluster) mentions the print edition — the
specialist edition is not linked from the catalogue. **partial** for item 2 (9/7657): the covering letter is
in print (not itself ciphertext), but its enclosed cipher key/table does not appear to be published — if the
RAH folio still holds the actual "adjunta clave," that key is an unpublished recovery candidate in the
LESSONS.md "key was in the archive beside the letter" pattern, worth a leaf view. **open** for item 3
(9/7666): not found in the two Rodríguez Villa volumes located on Internet Archive; t.2 and t.4 of the same
edition (which would most likely cover 1815 and 1818-1837 respectively) were not found digitised this pass
and remain the next print check before treating this item as unread.

## Copy status

Copy-free (per the 23-24 Sept scout): `bibliotecadigital.rah.es`, public domain / CC PDM, no login. Record
pages for all three ids re-checked reachable this pass (`registro.do?id=2242/1957/5186`, HTTP 307 each,
consistent with the site's session-redirect behaviour noted in QUEUE.md's caveats; not followed further, no
image opened, no transcription attempted — out of this brief's scope). No REQUEST.md needed.

## Request counts (this target)

archive.org (djvu.txt fetches): 4 (eltenientegener00villgoog 1.3 MB, eltenientegener01villgoog 1.6 MB,
eltenientegenera01rodruoft 0.8 MB, eltenientegenera02rodruoft 0.7 MB). archive.org advancedsearch: 2 (title
search, identifier-prefix search). archive.org be-api fts: 1 (global "Romerito" sanity check, ruled out as
too generic). bibliotecadigital.rah.es: 3 (record-page reachability only, >=2 s apart, shared with the
rah-canada-1869 budget in this batch — 3 of the 20-request cap used here). github.com: shared clone with
the rest of this batch. No TNA Discovery calls (n/a to this target). www.googleapis.com/books: 3 (24 Sept
2026, LANE S worker H, key+country=US, never printed; see Google Books sweep above).

## NX-MOR (26 September 2026, LANE NX worker, image fetch + eye check, items 2 and 3 only)

Route: `bibliotecadigital.rah.es/oai/oai.do?verb=GetRecord&identifier=oai:bibliotecadigital.rah.es:<id>&metadataPrefix=didl`
(plain curl, 200, no challenge) lists the page images as `imagen_id.do?idImagen=` refs; each fetched with
`tools/browser_fetch.js --binary` (Anubis clears intermittently, matching the rah-canada-1869 worked example).
All 5 images and crops in `images/`, manifest at `images/manifest.json`. Folder now 6.5 MB (well under the 30 MB cap).

### Item 2 (record 1957, 9/7657, ff.155v-156v) — 3 images, key table absent

Fetched all 3 page images the OAI record lists (`10077650.jpg`, `10077651.jpg`, `10077652.jpg`). This is
Morillo's own outgoing register/copybook (`dc:description: Copia`), running continuously with unrelated
entries before and after (N.196 "Guerra" starts mid-page on f.155v/156, ends on f.156v where a new, unrelated
entry N.125 begins immediately). The letter's full body is present and matches the print-edition text already
quoted in this file's 24 Sept 2026 section almost verbatim, including the sentence naming the key: f.156r
(`crop_1957_f156r_clave_ref.jpg`) reads "por lo que toca á las cifras, me ha parecido conveniente el proponer
á V.E. las que demuestra **la adjunta clave** [underlined in ms.], que ya tengo usada en los asuntos de
reserva y consequencia con los Gefes superiores de las Provincias y Divisiones, con la diferencia de haverla
variado ahora alterando la numeracion que da el valor a las letras a toda precaucion. Su sencillez y claridad
la hacen poco susceptible de equivocaciones." **No key table (a list of letters/words against figures or
signs) is present on any of the 3 images** — consistent with the earlier print-edition finding (the enclosure
was never reproduced there either) and consistent with this being the sender's own retained copy, not the
original-plus-enclosure that went to the Minister. The description itself is informative: the system is
described as numeric ("la numeracion que da el valor á las letras"), already in use with the provincial/
divisional chiefs, now varied only in its numbering — i.e. a substitution cipher assigning number values to
letters, the same family as item 3's leaf (see below), not a from-scratch design.

### Item 3 (record 5186, 9/7666, ff.420-420v) — 2 images, ciphertext present WITH ITS OWN INTERLINEAR DECIPHERMENT

Fetched both page images (`10088713.jpg` = f.420r, foliated "N.16" top right in this hand's own prior use, not
an RAH stamp; `10088714.jpg` = f.420v, foliated "420" top left in a different, later hand — the RAH's own
foliation). **f.420r carries ciphertext, and it is already deciphered on the leaf**: four lines of clear
Spanish ("Guanare y Nov.re 7 de 1820. Mi venerado Gral: en este momento recivo la favorecida de V. de 3 del
corriente quedando enterado de su contenido y dandole el debido cumplimiento. Nada ay por aqui de particular,
los enemigos de Apure no se mueven."), then **roughly 21 cipher groups across 6 rows** — Arabic numerals
(values seen: 3, 4, 5, 6, 7, 8, 10, 16, 18, 22, 24, 26, 27, 28, 30, 33, 50, 51, 56) plus two recurring
non-numeral marks, a "+" and a small box/square (□) — **each group has a plaintext word written interlinearly
beneath it, in what looks like the same period hand and ink**, not a modern pencil gloss. This is not blank
ciphertext: it is a decipherment already sitting on the document. Crop: `crop_5186_p1_cipher.jpg` (2400 px
wide, the full cipher block). f.420v is plaintext only (closing formula, "Q.B.S.M." signed "J.n Maria
Herrera", addressed "Exmo. S.D. Pablo Morillo" — confirms the catalogue's "Herrera a Morillo") — no further
cipher.

Eye-read a handful of the interlinear groups directly off the crop (illustrative only, not a transcription
pass — no key file written): `51.18.50.7.51.56.33.18.` = **Romerito** (8 signs, 8 letters, R-o-m-e-r-i-t-o,
matching the catalogue's own naming of "Romerito"); `24.18.51.` = **por**; `3.18.16.` = **con**;
`18.5.56.3.56.+.8.7.27.` = **oficiales**; `7.8.` = **el**. Cross-checking these five words against each other,
the values line up consistently wherever a letter repeats (18=o in Romerito/por/oficiales; 51=r in Romerito/
por; 56=i in Romerito/oficiales; 7=e in Romerito/el; 8=l in oficiales/el; 3=c in con/oficiales; +=a in
oficiales) — this is a real, internally consistent substitution, not a coincidence of a few words. The group
right after Romerito, `24.+.27.18.`, most likely reads a form of "paso" (24=p per "por", +=a, 27=s per
"oficiales", 18=o) rather than "bajo" as first guessed by eye — fits the catalogue's own description ("Herrera
a Morillo... dándole noticias de Romerito, que iba en busca de Bolívar"): "Romerito pas[ó/o] el..." Not
carried further (out of this brief's scope; a full alignment is the next-step line below).

**One-line eye check, item 2's key vs item 3's cipher (per this brief's step 3):** item 2's own key table is
not on the leaf to compare shapes against, but item 2's covering letter *describes* its system as Arabic-
numeral values assigned to letters ("la numeracion que da el valor á las letras"), which is exactly what
item 3's leaf shows in practice (values up to at least 56, plus two non-numeral auxiliary signs). Consistent
with the same cipher family described in the 19 Nov 1817 letter, three years later and, per that letter's own
words, in a varied numbering — not a like-for-like value match (no numbers were compared 1:1, since no table
survives for item 2), just a system-type match.

**Next step:** item 3's f.420r is a known-plaintext alignment job (grade C once done, per the rah-canada-1869
precedent and `tools/interlinear_align.py`) — align the ~21 cipher groups to their interlinear plaintext words
letter-by-letter to recover a numeral-to-letter key table, then check whether that same table opens any
passage of item 2's letter or any other ciphered item in this RAH cluster/legajo. This is a genuine "key was
in the archive beside the letter" case (LESSONS.md), stronger than item 2's (the decipherment is already
written out, not just implied).

**Request counts (this pass):** bibliotecadigital.rah.es OAI-PMH (`oai/oai.do`, curl): 3 (1 Identify
reachability check + 2 GetRecord/didl, >=2s apart, all HTTP 200, no challenge). `imagen_id.do` via
`tools/browser_fetch.js --binary`: 8 attempts for 5 images (10077650 needed 1 retry after an Anubis
challenge page and a 5s pause; 10077651 succeeded on attempt 2 of its own built-in 3x retry; 10077652
succeeded first try; 10088713 needed one extra manual retry after an 8s pause following its own 3 failed
internal attempts; 10088714 succeeded on attempt 2). One request at a time, >=4s apart between images, well
under the 60-request host cap. No other host touched this pass.

## NX-MOR2 (26 September 2026, LANE NX worker, item 3 key recovery + decode + spec)

### Intake

Re-searched for Rodríguez Villa t.4 (post-1818 documents, which would cover 1820) before any deep work, per
this job's brief: **found and read**, Google Books `v3kzAQAAIAAJ` ("...contiene los últimos años de la
estancia de Morillo en América...", 1908, `accessInfo.viewability: ALL_PAGES`, `publicDomain: true`) --
not on Internet Archive (re-searched `archive.org/advancedsearch.php?q=title:(teniente general Pablo
Morillo)`, 6 hits, none new), and Google Books' own PDF download link 403s/redirects for this account (not
worth a second attempt; the keyed search API already gives full-text snippets, which is what this citation
needed). Full-text searched via the Google Books API (key + country=US) for `"Herrera" "7 de noviembre de
1820"` and for `"Romerito"`: **no hit for this exact letter** in t.4 -- the only Herrera/Romerito passage
t.4 contains is a different, later letter ("Herrera desde Guanare, de 20 del actual...Romerito no esperó á
Ferrus, sino que se retiró á Pedraza"), a different date, quoted secondhand within Morillo's own narrative,
not this leaf's own text. Contreras, *Catálogo de la Colección Pablo Morillo* (Madrid 1988, Google Books
`ohJPjaGKOk8C`) independently confirms this item's own catalogue entry verbatim (Sig. 9/7666, ff.420-420v,
"Herrera a Morillo en carta cifrada dándole noticias de Romerito, que iba en busca de Bolívar", 7 de
noviembre de 1820) -- a description, not a plaintext. HathiTrust bibliographic API / HTRC Extracted
Features: not reached this pass -- chased through Open Library's search API first to find a matching
edition/OCLC to chain into HathiTrust, but Open Library's records for every "teniente general don Pablo
Morillo" title returned no `edition_key`, so there was nothing to chain; not pursued further since Google
Books already gave a decisive, directly full-text-searched answer for the specific citation needed. `t.2`
(1815 documents) still not located digitised anywhere. `intake_gate_check.py rah-morillo-1817` exits 0
after this citation was added to line 2 (below).

### Transcription (two blind Sonnet passes + direct image re-check)

Two blind Sonnet subagents, each given only `images/crop_5186_p1_cipher.jpg` (2400x1219, under the 2500px
split threshold, no halving needed) and no other context, transcribed the cipher block independently
top-to-bottom/left-to-right. Both agree on **21 real cipher groups across 6 rows** (row token-counts 3,4,4,4,
4,1 excluding one isolated, glossless mark) plus one likely-marginal isolated mark (row1, after "el": "5"
over "2" stacked, at the torn page edge, no interlinear word under it at all -- both passes flagged it as
possibly not a cipher group; excluded from the count and from all files below). Both passes agree on every
numeral in every group (no numeral-level disagreement anywhere) but disagree with each other, and in several
places with the correct reading, on individual **letters** of the interlinear gloss -- expected, since reading
a single cursive letter by eye is harder than reading a printed-style Arabic numeral, and neither pass
cross-checked its own letter guesses against the other groups' numerals for consistency (both said so
explicitly in their own reports).

The orchestrating session then re-examined the image directly (Python/Pillow crops at 3-5x zoom, by row and
by individual group) rather than trust either pass's word guesses at face value, because the numerals
themselves (which both passes read identically) are the reliable signal: the same numeral recurring across
different words must decode to the same letter if this is a simple substitution, and several of the two
passes' word-guesses (e.g. "Payo"/"Rayo" for what the numerals force to be "Paso"; "tenia" vs "benia" for
what the numerals force to be "benia") could be adjudicated this way without more image time than either
blind pass already spent.

### Key (grade H, `key_5186.tsv`, `tools/ciphers/rah-morillo-1817/build_key_5186.py`)

13 of the 21 groups are **fully clean**: every token's numeral agrees between the two blind passes, every
letter is unambiguous by eye, and the resulting word is a real, contextually sensible Spanish word or name
with no leftover unresolved sign. These 13 words (89 letter-token pairs) build the key, one cipher-code to
one letter, by majority count -- and every code that recurs across two or more of these 13 words agrees on
its letter **with zero exceptions** (the `conflict` column of `key_5186.tsv` is empty on every row):

| code | letter | count | words it was seen in |
|---|---|---|---|
| 18 | o | 9 | Paso, Romerito, bo, buscando, con, dijo, oficiales, por |
| + | a | 7 | Paso, a, benia, buscando, oficiales, para |
| 7 | e | 6 | Romerito, benia, de, el, oficiales, tres |
| 51 | r | 5 | Romerito, para, por, tres |
| 56 | i | 5 | Romerito, benia, dijo, oficiales |
| 27 | s | 4 | Paso, buscando, oficiales, tres |
| 16 | n | 3 | benia, buscando, con |
| 24 | p | 3 | Paso, para, por |
| 3 | c | 3 | buscando, con, oficiales |
| 4 | d | 3 | buscando, de, dijo |
| 6 | b | 3 | benia, bo, buscando |
| 33 | t | 2 | Romerito, tres |
| 8 | l | 2 | el, oficiales |
| 30 | j | 1 | dijo |
| 5 | f | 1 | oficiales |
| 50 | m | 1 | Romerito |
| BOX (small drawn square) | u | 1 | buscando |

17 distinct signs resolved (14 numerals, "+", and the small drawn box "BOX"; "BOX" recurs in two of the
flagged groups below too, at the same value both times, an 18th and 19th occurrence not counted toward the
key since those groups are not clean). "Paso" is included with one flagged caveat: both blind passes read
its third letter as "y" ("Payo"/"Rayo"), but the numeral there (27) is the same one `oficiales` and `tres`
independently give "s", and a direct 4x-zoom re-check shows this hand's flourished terminal "s" is visually
close to a "y" at this crop's resolution -- key-consistent, counted, and the letter-vs-eye disagreement is
reported here rather than silently resolved.

### Consistency control (rule 3, the Szembek/bMAT2/AX-5799 shape: a control that can actually fail)

`tools/ciphers/rah-morillo-1817/shuffle_control_5186.py`: real consistency (majority-agreement over every
recurring code among the 13 clean groups) = **1.000** (50 of 50 recurring-code token occurrences agree with
their own code's majority letter). Shuffle control: 20 permutations, each reassigning which of the 13
clean groups' gloss words is read against which group's cipher tokens, restricted to length-matched swaps
(a word's letters can only be tested against a token sequence of the same length) so every permutation
still produces a complete, comparable score -- shuffle mean **0.621**, p95 **0.800**, range 0.473-0.855. Real
beats shuffle p95 by 0.200: the recurring-code/recurring-gloss pairing discriminates cleanly at this N: it is
not the bMAT2/AX-5799 shape (a control that cannot fail by construction), since a length-matched word swap
genuinely can and does produce disagreement (mean 0.621 well below 1.000).

### Mechanical decode (`tools/decode_key.py ciphers/rah-morillo-1817 --check`, exits 0)

`tokens 97: H 91, U 6` (91 of 97 signs read H via the key; 6 unread signs -- 22 x3, 10 x1, 26 x1, 28 x1 --
left as `[code]`, not guessed, per rule 7). Full per-group table, numerals as transcribed, gloss as best read
by eye, and the key's own mechanical decode of the same tokens:

| group | cipher (dot-joined) | gloss as read | key-mechanical decode | |
|---|---|---|---|---|
| r1g1 | 51.18.50.7.51.56.33.18 | Romerito | romerito | clean |
| r1g2 | 24.+.27.18 | Paso (both passes read "Payo"/"Rayo") | paso | clean (see caveat above) |
| r1g3 | 7.8 | el | el | clean |
| r2g1 | 24.18.51 | por | por | clean |
| r2g2 | 6.+.51.56.16.51.33.+.27 | "barinituS"/"barinztus" (passes disagree; neither matches the key output) | **barinrtas** | **flag: gloss/key disagreement** |
| r2g3 | 3.18.16 | con | con | clean |
| r2g4 | 27.18.22.18 | "solo" (tentative; context, not confirmed) | so[22]o | flag: 22 unread |
| r3g1 | 33.51.7.27 | tres | tres | clean |
| r3g2 | 18.5.56.3.56.+.8.7.27 | oficiales | oficiales | clean |
| r3g3 | 4.56.30.18 | dijo | dijo | clean |
| r3g4 | 6.7.16.56.+ | benia (period spelling of venía) | benia | clean |
| r4g1 | 4.7 | de | de | clean |
| r4g2 | 30.BOX.+.22.+.16.+ | "guayana" (both passes; first letter reads visually as "g") | **jua[22]ana** | **flag: gloss/key disagreement at token 30 (g vs key's j, confirmed 1x elsewhere in "dijo")** |
| r4g3 | 6.BOX.27.3.+.16.4.18 | buscando | buscando | clean (resolves BOX=u) |
| r4g4 | + | a | a | clean |
| r4g5 | 6.18 | bo (trailing flourish after, possibly decorative) | bo | clean |
| r5g1 | 8.56.26.+.51 | "levar" (tentative) | li[26]ar | flag: 26 unread |
| r5g2 | 27.51.10.BOX.51.18 | "seguro" (tentative; does not fit key position-by-position) | **sr[10]uro** | **flag: gloss/key disagreement (position 2 is numeral 51, confirmed "r" 5x elsewhere, not "e")** |
| r5g3 | 24.+.51.+ | para | para | clean |
| r5g4 | 33.51.BOX | tru (word runs off the page edge, incomplete) | tru | clean (as far as it goes) |
| r6g1 | 28.56.22.18 | "xino" (tentative) | [28]i[22]o | flag: 28 and 22 unread |

Per this job's brief: these disagreements are reported **as data points, not corrections** -- the key's
mechanical output is not asserted to be more "correct" than the eye-read gloss at these positions, since both
readings come from the same worker's own eye on the same image; a future pass with better image resolution
(or the physical leaf) is the only way to adjudicate them. Grade counts for the 21-group cipher block: **H
17 codes / 91 of 97 tokens**, **U 6 of 97 tokens** (unread, not guessed). No C, S, M, or I grades apply --
every value here comes from the leaf's own interlinear decipherment (rule 4).

### Judge (spec written, `specs/rah-morillo-1817.json`)

`python3 tools/judge_plaintext.py specs/rah-morillo-1817.json --file <the 91-letter joined decode>`:
```
ok   length: got=91, min=60, max=1000000000
FAIL language: score=-1.172, null_p99=-1.698, real_p05=-0.919, real_median=-0.823, mode=both, N=91
FAIL - rah-morillo-1817 (a PASS is a gate for a verifier, not a reading; rule 10)
```
FAIL, reported as a FAIL (rule 7). Two things to weigh before reading this as a negative on the key itself:
(1) the language corpus is **not era-matched** -- `judge_plaintext.py`'s default `es` corpus (`LANG_CORPORA`)
is `es17`, Don Quijote and *Vida del Buscón*, both early-17th-century; this letter is dated 1820, two
centuries later, the same shape of mismatch CLAUDE.md's pt17/pt18 (Linhares) and es17c (Mercy) lessons warn
about, and no era-matched Spanish corpus exists yet in `tools/data` to swap in (out of this job's scope to
build one for a 91-letter fragment). (2) the candidate string itself concatenates all 21 groups with no word
spaces and includes two flagged, gloss-disagreeing groups (`barinrtas`, `jua[22]ana` with the bracket
stripped) and four groups with an outright unread sign -- exactly the kind of noise a word-cover or clean-text
check would penalize even from a genuinely correct key. The key's own evidence (grade H, zero internal
conflicts across 50 recurring-code occurrences, shuffle control discriminating by 0.200) stands independently
of this judge result.

### Item 2 vs item 3 compatibility (this job's brief, step 5)

Compatible in kind, not confirmed in value: item 2's covering letter (19 Nov 1817) describes its system in
exactly these terms -- "la numeracion que da el valor á las letras" (the numbering that gives value to the
letters), i.e. Arabic numerals substituting for individual letters, varied from an earlier version -- and
`key_5186.tsv` is precisely that: a monoalphabetic numeral-per-letter substitution, no word/name codes seen
in this span. But no 1:1 numeral comparison between the two items is possible: item 2's own key table
("la adjunta clave") is not preserved on any of its 3 images or in the printed edition, so there is nothing
to check item 3's specific values (18=o, +=a, 7=e, 51=r, ...) against, and item 2's letter itself says the
numbering was "varied" between uses -- so even a value mismatch, if the table existed, would not itself rule
out the same underlying system three years apart.

### Files, hosts, next step

Files: `ciphers/rah-morillo-1817/{build_key_5186.py, shuffle_control_5186.py, ciphertext_5186.tsv,
key_5186.tsv, gloss_5186.tsv, decode.json, reading_5186.txt, reading_5186_tokens.tsv}`,
`specs/rah-morillo-1817.json`. Hosts this pass: `www.googleapis.com/books` 6 (all keyed + country=US, >=1.5s
apart, never printed), `archive.org/advancedsearch.php` 1, `openlibrary.org/search.json` 1. No image host
touched (crops already on disk from NX-MOR). Next step: a second, independent reconciliation pass (or the
physical leaf / a higher-resolution scan) on the 8 flagged groups above, particularly r2g2 and r5g2 where the
key-mechanical decode and the eye-read gloss disagree outright rather than merely leaving a sign unread --
whoever does this should not start from this session's own zoom crops (a fresh eye, not a repeat of the same
misreading, is the point). Status stays **partial** (rule 5): a working, control-backed grade-H key exists
for part of one leaf, not a finished reading of the whole cipher block.

## NX-MOR3 re-derivation (26 September 2026, LANE NX worker, fresh-instance rule-7 check)

Fresh instance, per job brief: read only `specs/rah-morillo-1817.json`, `key_5186.tsv` and `decode.json`,
then transcribed `images/crop_5186_p1_cipher.jpg` independently (one blind Sonnet subagent pass, agent
`a374e93d81f51e10d`, working from the full 2400x1219 image with no crop tool, plus this session's own
direct Python/Pillow crop-and-zoom reads at 3-8x) before reading any of NX-MOR2's own ciphertext, gloss or
reading files. Files: `rederiv/ciphertext_rederiv.tsv` (own transcription, 21 groups, own gloss reads),
`rederiv/apply.py` (mechanical key application), `rederiv/reading_rederiv.txt` (output).

`python3 tools/decode_key.py ciphers/rah-morillo-1817 --check`:
```
ciphertext_5186.tsv: tokens 97: H 91, U 6
reading up to date
```
Exits 0 -- the committed reading is not stale.

### Verdict

**Re-derivation agrees except 0 tokens, all (vacuously) within the M-graded set** -- there is no M grade in
this target (grades are H/U only per NOTES.md's own NX-MOR2 table), and this worker's independent
transcription reproduces all 97 tokens of `ciphertext_5186.tsv` exactly, including the same 6 unread signs
at the same positions (codes 10, 22 x3, 26, 28), for all 21 committed groups. `rederiv/reading_rederiv.txt`
and `reading_5186.txt` are letter-for-letter identical once compared group by group (diff table below). Rule
7's re-derivation gate is met: nothing sends this reading back.

### Diff table (this worker's independent transcription vs. the committed `ciphertext_5186.tsv`/`reading_5186.txt`)

| group | codes (both agree) | committed decode | this worker's decode | diff |
|---|---|---|---|---|
| r1g1 | 51.18.50.7.51.56.33.18 | romerito | romerito | none |
| r1g2 | 24.+.27.18 | paso | paso | none |
| r1g3 | 7.8 | el | el | none |
| r2g1 | 24.18.51 | por | por | none |
| r2g2 | 6.+.51.56.16.51.33.+.27 | barinrtas | barinrtas | none (re-checked the disputed 6th numeral twice against confirmed 51/56 shapes elsewhere in the same group before matching committed; it is 51, not 56) |
| r2g3 | 3.18.16 | con | con | none |
| r2g4 | 27.18.22.18 | so[22]o | so[22]o | none (re-checked against the subagent's alternate "3.18.50.18"/"como" reading; zoom confirms committed's numerals) |
| r3g1 | 33.51.7.27 | tres | tres | none |
| r3g2 | 18.5.56.3.56.+.8.7.27 | oficiales | oficiales | none |
| r3g3 | 4.56.30.18 | dijo | dijo | none |
| r3g4 | 6.7.16.56.+ | benia | benia | none |
| r4g1 | 4.7 | de | de | none |
| r4g2 | 30.BOX.+.22.+.16.+ | jua[22]ana | jua[22]ana | none |
| r4g3 | 6.BOX.27.3.+.16.4.18 | buscando | buscando | none |
| r4g4 | + | a | a | none |
| r4g5 | 6.18 | bo | bo | none |
| r5g1 | 8.56.26.+.51 | li[26]ar | li[26]ar | none |
| r5g2 | 27.51.10.BOX.51.18 | sr[10]uro | sr[10]uro | none |
| r5g3 | 24.+.51.+ | para | para | none |
| r5g4 | 33.51.BOX | tru | tru | none |
| r6g1 | 28.56.22.18 | [28]i[22]o | [28]i[22]o | none |

The isolated stacked "5" over a second sign at the row-1 right margin (this worker read the second sign as
"28" on zoom) is the same mark NX-MOR2 already found and deliberately excluded ("one likely-marginal
isolated mark ... no interlinear word under it at all"), not a group this worker found that NX-MOR2 missed --
confirmed by re-reading NX-MOR2's own transcription section above after finishing this worker's own blind
pass. Not one of the 21 counted groups, on both readings.

### One finding for a successor: "bo" + "li[26]ar" read together as "Bolivar"

NX-MOR2's own `gloss_5186.tsv` already reads r4g5/r5g1 as "bo" / "levar (tentative; 26 unresolved)" -- two
separate groups. This worker independently arrived at the same numerals, but the subagent's blind pass read
them as one continuous run and proposed **"Bolivar"** (b-o-l-i-v-a-r), i.e. the same word split across the
manuscript's own line wrap ("...buscando a bo-" ends one line; "-livar..." starts the next), not two short
words. That resolves previously-unread code 26 as **v**. This is corroborated by print already cited on
NOTES.md line 3 and in NX-MOR2's own intake section: Contreras 1988's catalogue entry for this exact item
reads "Herrera a Morillo en carta cifrada dándole noticias de Romerito, **que iba en busca de Bolívar**" --
"who was going in search of Bolívar" lines up with this decode's own "...buscando a bo-li[26]ar" ("...looking
for Bo-livar") almost word for word. Per rule 4, this is not asserted above grade M for code 26 on this
worker's own say-so (one word, one worker's key/gloss reading), but the printed catalogue description is an
independent corroborating source already in the file, not new digging -- a strong candidate for a successor
to fold into `key_5186.tsv` as code 26 = v (grade M or S pending a second eye), rather than leaving it
unread. Not adopted into `key_5186.tsv` by this worker (a key-file change is outside this job's brief); flagged
here only. Rule 10: this is a reading of an already-published catalogue description matching an already-keyed
decode, not a claim of new plaintext or new discovery.

Status stays **partial** (rule 5); no change to the key, ciphertext, gloss or reading files (this job's brief
was a re-derivation check, not a key revision).

## NX-MOR4 (26 September 2026, LANE NX worker, key_5186 transfer search)

### Question and answer

Brief: does any OTHER cipher text in the Morillo papers at the RAH (Sig. 9/7650-9/7690, 1815-1821) carry
numeral ciphertext that `key_5186.tsv` (item 3's leaf-derived key) can be applied to? **Answer: no candidate
found this pass carries ciphertext compatible with key_5186's design.** Two genuinely ciphered documents were
found (records 1306, 1487, both Ministerio de Guerra dispatches TO Morillo), but both use a different, larger
numeral system (values up to 120+, heavy exact-multiples-of-ten) that cannot be key_5186 by inspection alone
(rule 3: "a different numeral range means a different key -- say so and stop", this job's own brief step 3a).
A third document (record 4332, Aldama to Morillo) carries a real period key table, but for vowels only, in a
tally/comb-glyph design with no numerals at all -- also incompatible by design. Full search log below.

### Step 1: RAH catalogue search (`bibliotecadigital.rah.es`, POST to `resultados_busqueda.do`)

Terms tried, `busq_general=`: `cifra`, `cifrada`, `cifrado`, `clave`, `en cifra`, `Herrera`, `Morillo cifra`,
`Morillo clave`, `Morillo a Herrera`, `Morillo Herrera espías Guanare`, `Nuevo Caño Herrera`. `cifra`/`en
cifra` each return the same 4 hits as the 24 Sept 2026 scout found (item 2's own proposal letter + 3
cartographic false positives, "cifra" = map-scale legend). `cifrado` returns the same 2 hits the 24 Sept scout
logged and flagged for a successor: records **RAH20090013407** (id 1487, Alós, 4 Dec 1819, "Despacho muy
reservado y cifrado") and **RAH20090011595** (id 1306, Eguía, 28 Oct 1818) -- both Ministerio de Guerra
dispatches to Morillo, both noted by RAH's own cataloguer as already printed in Rodríguez Villa. `clave`
(410 hits, far too broad on its own) and `Morillo clave` (a narrower, decisive combination) surface a set of
Morillo-fonds letters mentioning a cipher key that the earlier scout's narrower term list missed:
`RAH20090041851` (id 4332, Aldama→Morillo, 28 Apr 1819, "adjunta una nota con la clave"), `RAH20090043909`
(id 4537, Morillo→Pereira, 19 Jul 1819, "indicándole la clave que debe utilizar"), `RAH20090050488` (id 5195,
Morillo→Herrera, 28 Oct 1820, same legajo/signature as item 3, "clave para asuntos reservados"),
`RAH20090016125` (id 1759, a second copy of item 2's own 19 Nov 1817 letter, different legajo), plus two
letters explicitly saying the correspondent **lacks** a key (`RAH20090026988`, `RAH20100000069`, excluded) and
one idiom false positive ("lugares clave" = key/strategic locations, `RAH20090047891`, excluded). Full list
with record ids, signatures, dates and per-candidate notes: `rederiv_transfer/candidates.tsv`. Requests:
`bibliotecadigital.rah.es` POST search ~13 (>=3s apart), record-detail GETs ~11 (>=3s apart), all HTTP 200
except one single-hit query that 302-redirected straight to the record (RAH's own behaviour for a one-result
search, not an error).

### Step 1b: Contreras 1988 catalogue (Google Books, key+country=US)

Two queries: `cifra Contreras Coleccion Morillo` and `"carta cifrada" Morillo` (both keyed, `country=US`).
The `"carta cifrada" Morillo` query's only hit inside Contreras's own catalogue (`ohJPjaGKOk8C`) is the
snippet already on file for item 3 itself ("...Morillo en carta cifrada dándole noticias de Romerito... Sig.
9/7666, leg. 23, f), ff. 420-420v. Herrera a Morillo..." -- the same 4.529/4.530 entries NX-MOR2 already cited)
-- no other "carta cifrada" entry for this fonds turned up in this catalogue via full-text search. The other
7 hits from this query and the 2 hits from the first are unrelated 20th-century secondary works citing
Morillo's papers generically, not RAH catalogue entries. Requests: `www.googleapis.com/books` 2.

### Step 2: images fetched for 4 candidates (`tools/browser_fetch.js --binary`, OAI-PMH didl route)

Per this job's brief cap (up to 4 candidates), the four ranked highest by relevance to Herrera/Guanare or
Morillo's own headquarters were fetched in full; the two `cifrado`-tagged Ministry dispatches were fetched
afterward (time and folder-size budget allowed) since they are the only records anywhere in this search
confirmed by their own catalogue text to carry actual ciphertext. Full per-image findings are in
`images/manifest.json` (records 5195, 4332, 4537, 1306, 1487) and `rederiv_transfer/candidates.tsv`; summary:

| record (id) | sender→recipient, date | images | ciphertext? | key table? | verdict |
|---|---|---|---|---|---|
| 5195 | Morillo→Herrera, 28 Oct 1820 | 2/2 fetched | no | no | plaintext only; f.433 shows an uncatalogued continuation entry (Nuevo Caño, 12 Nov 1820) opening "he recibido las apreciables de V. de 7 y 8, la 1a en cifra" -- Morillo acknowledging Herrera's letters of the 7th (item 3) and 8th, confirming item 3 was ciphertext, but the reply's own text (not captured beyond this line) is not shown ciphered |
| 4332 | Aldama→Morillo, 28 Apr 1819 | 6/6 fetched | no | **yes** | f.624, headed "Aldama.": a-e-i-o-u each paired with a distinct tally/comb-stroke glyph (not numerals). Letter (f.625) says Aldama built this key himself, for future use, not this letter |
| 4537 | Morillo→Pereira, 19 Jul 1819 | 3/3 fetched | no | no | plaintext register copybook; names "la adjunta clave" repeatedly, table never present (same absence pattern as item 2) |
| 1759 | Morillo→Min. de Guerra, 19 Nov 1817 (2nd copy) | 0/2, fetch failed | -- | -- | RAH server returned a Java/Tomcat error page mislabelled `image/jpeg` on both images, twice (1 retry after 6s pause); not pursued further, lowest-priority candidate |
| 1306 | Eguía (Min. de Guerra)→Morillo, 28 Oct 1818 | 3 of 6 fetched | **yes** | **yes** | f.150-150v: long numeral cipher block (values 1-19, plus 10/40/50/60/100/120, a square and "+" auxiliary sign). f.151: the document's OWN period decipherment, headed "Adjunto al doc.to 754. Descifrado" |
| 1487 | Alós (Min. de Guerra)→Morillo, 4 Dec 1819 | 1 of 8 fetched | **yes** | not checked | f.158: partial cipher (names/places only), same numeral pattern as 1306 (10/40/50/60/100/120, square, "+") -- confirmed same system, not pursued further |

### Step 3: coverage/design gate against key_5186

Per this job's brief step 3(a), a different numeral range is grounds to stop without a full transcription
pass. `key_5186.tsv`'s 17 codes are `{18, +, 7, 51, 56, 27, 16, 24, 3, 4, 6, 33, 8, 30, 5, 50, BOX}` -- every
numeral code is <=56, and none of them recur as exact multiples of ten. Records 1306 and 1487's cipher blocks
are dominated by codes that are exact multiples of ten (10, 40, 50, 60, 100, 120) standing alongside small
values 1-19 -- a visibly different two-tier design, and several of their tokens (100, 120) exceed key_5186's
maximum code (56) outright, which key_5186 categorically cannot produce. This is decisive without transcribing
the full block: **design mismatch, not tested further** (rule 3's "match the design" lesson, restated in this
job's own brief). Record 4332's key table is vowel-only tally glyphs, not numerals at all -- also excluded by
design, and moot besides since that record's own letter is plaintext (no ciphertext exists there to test
coverage against). No coverage percentage is reported for any candidate: none of the fetched records pairs a
key_5186-compatible numeral cipher with anything to measure coverage on (rule 3's own requirement that a
control/comparison be capable of failing -- there is no numeral-per-letter ciphertext in this batch for
key_5186 to be tested against at all, so a coverage number would not test anything).

### Step 4: the 26=v (Bolivar) hypothesis

Not testable this pass: it requires a second key_5186-style numeral cipher text to test 26's occurrences
against, and no candidate found this pass carries one. Not adopted into `key_5186.tsv` (unchanged, per NX-MOR2/
NX-MOR3's own scope limits).

### A genuine finding, out of this job's scope: a second solved cipher in the fonds

Records 1306 and 1487 (Ministerio de Guerra→Morillo dispatches, 1818 and 1819) are real period ciphertext with
their own attached period decipherment (record 1306's f.151, "Adjunto al doc.to 754. Descifrado") and, per
RAH's own catalogue notes, already published (Rodríguez Villa t.III doc.754 pp.693-4 and t.IV doc.814
respectively) -- the same "found-solved" shape as item 1 (Enrile→Morillo, 9/7658). This is a fourth distinct
cipher system in the Morillo fonds (alongside key_5186's Herrera-Morillo field code, Aldama's personal
vowel-glyph code, and now this Ministerio de Guerra office nomenclator), used across at least two dispatches a
year apart with the same tens-pattern design -- a lead for a future scout/campaign (recovering this office's
own key from the attached decipherment would be a new key-recovery job, not a key_5186 transfer test), not
pursued further here since it is outside this job's brief.

### Files, hosts, status

Files: `ciphers/rah-morillo-1817/{NOTES.md, rederiv_transfer/candidates.tsv, images/manifest.json,
images/10088734.jpg, images/10088735.jpg, images/10085214-19.jpg, images/10089531-33.jpg,
images/10076236-38.jpg, images/10075658.jpg}`. Hosts: `bibliotecadigital.rah.es` POST search ~13, record-detail
GET ~11, OAI-PMH GetRecord ~6 (all >=2-3s apart, HTTP 200) + `imagen_id.do` via `tools/browser_fetch.js
--binary` ~23 attempts for 20 successful images (2 failed on record 1759 after 1 retry; a few needed the
tool's own internal retry for Anubis, none needed a second manual retry beyond the one used for 1759), one at
a time, >=3-4s apart; `www.googleapis.com/books` 2 (keyed, `country=US`, never printed). Images folder: 25 MB
(under the 30 MB cap). No subagents used. Status stays **partial** (rule 5) -- no key/reading file changed.
Per this job's brief: stopping here; the orchestrator decides whether a follow-up job pursues records 1306/1487
as their own key-recovery target.

## V9-MOR verifier (26 September 2026) -- pointer

Full audit in `AUDIT.md`. Item 3: **N0, key `period`, `text: known`.** The plaintext (clear closing sentence and the whole
cipher block, modernised) is printed in Wilfredo Bolívar, Armando González Segovia and Aleyda Anzola, *Portuguesa en
Carabobo. Diario llanero de una contienda en armas* (Aythaima, 2021, ISBN 978-980-18-2090-1), p.37 and n.100, citing
"Sig. 9/7666, leg. 23, f), ff. 420-420v" -- found by `tools/print_check.py`'s global IA pass (`phrases.txt`,
`print-check.tsv`). Corrections to sections above, by pointer rather than edit: (1) rule 4: the key comes from a
period *decipherment*, not a key sheet, so the tokens are **C**, not H, and the five key-vs-gloss disagreements are
**M**: C 86 / M 5 / U 6 of 97 (the key/decode files are unchanged; a later solver job applies this); (2) NX-MOR2's key
counts are 14 words / 59 letter-token pairs, not 13 / 89; (3) the 24 Sept "Verdict" ("open for item 3", "t.4 not
located") is superseded. The print reads r2g2 as "Caimital" (our gloss read "barinituS", key "barinrtas") and the
clear text as "no se reciben" (NX-MOR: "no se mueven"), and supplies the words over the six unread signs ("sólo",
"Guayana", "Bolívar", "seguro", "Trujillo"): an image question for the solver lane, not settled by the verifier.

## Grade correction applied (LANE NX orchestrator, 26 Sept 2026, 11:45 UTC)

V9-MOR (AUDIT.md) corrected rule 4: a key built from the leaf's own interlinear decipherment is known plaintext,
grade C, not H. `build_key_5186.py` now writes grade C; `key_5186.tsv`, `reading_5186*.txt/tsv` regenerated;
`decode_key.py --check`: tokens 97, C 91 / U 6, reading up to date. V9's finer split (C 86 / M 5 / U 6: 5 tokens in
the six tentatively glossed groups at M) is not yet applied -- it needs a per-group exceptions file, left as a
one-line next step. The printed text (Portuguesa en Carabobo p.37 n.100) reads r2g2 "Caimital" and "no se
reciben" where ours differ, and supplies the words over the 6 unread signs (solo, Guayana, Bolivar, seguro,
Trujillo): an image re-check of those groups against the print, then the 26 = v value at grade C from the print,
is the remaining housekeeping. Item 3 is found-solved; no further campaign.

## GAPS-rah-morillo-1817 (2 Oct 2026, account-4)

Brief `.claude/briefs/runs/2026-10-02-account4-gaps-step.md`; the "## Remaining gaps" Verdict step of 1 Oct 2026, run
verbatim and nothing else: fold the 2021 print's words into key_5186 via `build_key_5186.py` (26=v, 28=j, 10=g at C,
22/30 tested as merged signs) with V9-MOR's exceptions.tsv split and a `decode_key.py --check` rerun. Disk only; no
image opened, 0 vision calls, no numeral re-read (the three agreeing passes stand). Item 3 is N0 with its text in print
(AUDIT.md): this is key-table housekeeping on a dataset row, not a solve.

### What changed (rule 7: every file below regenerates from `build_key_5186.py` then `tools/decode_key.py`)

- `build_key_5186.py`: a `PRINT_WORDS` table (the print's word over each group the gloss key left unread or
  tentative, one letter per sign; source *Portuguesa en Carabobo*, 2021, p.37 n.100, as AUDIT.md section 2 quotes it)
  and a `print_fold` rule -- the gloss-built key (KEY_WORDS, unchanged, still the shuffle-control's input) is never
  overwritten by the print: a sign the key lacks takes the print's value(s); a sign that agrees gains a count and a
  word; a sign that disagrees keeps its value, records the print letter in the `conflict` column, and the position
  goes to `exceptions.tsv` at M (rule 4: two witnesses disagreeing are a data conflict, not a majority vote).
- `key_5186.tsv`: 21 signs (was 17), new `source` column (gloss / gloss+print / print). New at C from the print:
  **26 = v** (Bolivar, written bo|livar across the line wrap, as NX-MOR3 proposed), **28 = j** (Trujillo, tru|jillo),
  **10 = g** (seguro). Counts raised where the print confirms a gloss value: BOX = u now 4 words (was 1), 8 = l 3,
  51 = r 8, 56 = i 7, 18 = o 13, + = a 11, 27 = s 6, 16 = n 4, 33 = t 3.
- `exceptions.tsv` (new, generated; wired in `decode.json`): 7 rows at M -- V9-MOR's five (r2g2 positions 5 and 7;
  r4g2 position 0; r5g2 position 1; and r5g1 position 1 is **not** among them any more, see below) plus the three
  occurrences of sign 22.
- `gloss_5186.tsv`: a `print_2021` column beside the gloss as read.
- `reading_5186.txt` / `reading_5186_tokens.tsv`: regenerated; `ciphertext_5186.tsv` unchanged (git diff empty).

### The two merged-sign tests (the step's own question; witnesses, not a majority)

| sign | witness 1 | witness 2 | witness 3 | holds as one value? | logged as |
|---|---|---|---|---|---|
| 22 | r2g4 "solo" (print; gloss read "solo" tentatively) forces **l** | r4g2 "Guayana" (print; gloss "guayana") forces **y** | r6g1 "Trujillo" = tru\|jillo, five letters over four signs with 56 = i and 18 = o anchoring positions 1 and 3, forces **ll** | **no.** Three letters from three words. A yeismo class ll/y covers Guayana and Trujillo (2 of 3) but not "solo", and 8 already reads l in two gloss words (el, oficiales) and a third print word (Bolivar), so 22 is not simply a second l | key row `22 = l\|y\|ll`, grade M, conflict column "one sign, l in solo, y in Guayana, ll in Trujillo"; each occurrence an exceptions row with its own print letter at M |
| 30 | r3g3 "dijo" (gloss, clean, both passes) forces **j** | r4g2 "Guayana" (gloss "guayana" both passes + print) forces **g** | -- | **untestable at this N**: one word each way, no third occurrence to break the tie; a g/j merge is consistent with every other sign (no other sign reads g; 28 now reads j from Trujillo, so j would have two signs) but nothing on this leaf can distinguish "30 = g/j merged" from "30 = j, and Guayana enciphered with a slip" | key row stays `30 = j` (gloss), conflict column "g x1 (Guayana, print)"; r4g2 position 0 an exceptions row, value g (what both witnesses under that sign say), grade M |

Two more places where the print and the sign disagree, both left at the sign's value and graded M, not re-read (the
numerals were read identically by three passes; the Remaining-gaps section's image-check step is the instrument):
r5g2 position 1 (sign 51 = r in five gloss words and three print words; gloss and print "seguro" want e, sign 7) and
r2g2 (print "Caimital", 8 letters, cannot align with the group's 9 signs at all; gloss as read "barinituS"; key
"barinrtas"). r5g1 position 1 (56 = i): V9-MOR had it M against the tentative gloss "levar"; the print's "Bolivar"
has i there, so it is C with no exception row, as the step planned.

### Numbers

`python3 build_key_5186.py --check`: exit 0. `python3 tools/decode_key.py ciphers/rah-morillo-1817 --check`:
```
ciphertext_5186.tsv: tokens 97: C 90, M 7
reading up to date
```
exit 0. Grade counts (rule 4): **C 90 / M 7 / U 0 of 97** (was C 86 / M 5 / U 6 by AUDIT.md section 3, C 91 / U 6 by
the committed files). Of the 7 M: 2 in r2g2, 3 on sign 22, 1 on sign 30 (r4g2), 1 on sign 51 (r5g2). No H, S or I.
The print's letters are known plaintext (C) for the 5 words it supplies; 26, 28 and 10 are each attested in one word
only (C does not need two words; that is the S rule).

`shuffle_control_5186.py` (KEY_WORDS unchanged, re-run 2 Oct 2026): real 1.000, shuffle mean 0.621, p95 0.800,
range 0.473-0.855 -- the same figures as 26 Sept; the print fold-in adds no clean-gloss group to that control and
cannot change it (a control that cannot vary with this step is not a test of this step, rule 3; it is quoted only to
say the gloss-built base is the one V9-MOR audited).

Judge (rule 7; `tools/judge_plaintext.py specs/rah-morillo-1817.json`, es17 corpus, not era-matched, as NX-MOR2 noted):
```
our decode, 97 signs joined (98 letters, ll counted twice):
ok   length: got=98, min=60, max=1000000000
FAIL language: score=-1.043, null_p99=-1.77, real_p05=-0.935, real_median=-0.812, mode=both, N=98
FAIL - rah-morillo-1817
the 2021 print's own modernised text of the block, as a reference through the same judge (not a candidate):
ok   length: got=100, min=60, max=1000000000
ok   language: score=-0.915, null_p99=-1.741, real_p05=-0.92, real_median=-0.817, mode=both, N=100
PASS - rah-morillo-1817
the 26 Sept 91-letter decode, for comparison: FAIL, score=-1.172 (real_p05=-0.919, N=91)
```
Reported as a FAIL. The score moved from -1.172 to -1.043 with the six former U signs filled; the print's own text of
the same block sits at -0.915, just above the p05 gate, so the remaining gap between our decode and the gate is the
places where our signs still differ from the print ("barinrtas" for "Caimital", "srguro" for "seguro", no "rio") --
exactly the Remaining-gaps image-check step, not the key.

Rule 10: nothing here is new; the letters folded in come from a 2021 printed text of this very item (N0, AUDIT.md),
and the key stays `period` (rebuilt from the leaf's own decipherment, now with the print as a second witness).
One-line suggestions outside this brief: `specs/rah-morillo-1817.json`'s `ciphertext_note` still says "grade H" and
"13 of 21 groups" (stale since V9-MOR; a spec edit was not this step); status.json's dataset row still quotes C 86 /
M 5 / U 6 (the parent updates status.json); AUDIT.md section 3 carries a dated pointer to this section (rule 10's
propagation clause), its class unchanged.

## GAPS2-rah-morillo-1817 (3 Oct 2026, account-4): image check of the gloss letters and the clear line

Brief `.claude/briefs/runs/2026-10-02-account4-gaps-step.md`; the Verdict step of 2 Oct 2026, run and nothing else.
Crop step pasted first: `python3 tools/iiif_lines.py --image images/10088713.jpg --out <scratch> --debug` ->
"region 3000x3582, 13 lines, 13 bands x 2 segments; centres 572 1369 1609 1785 1967 2135 2323 2415 2535 2756 2967
3047 3191". The bands split the gloss rows from their numeral rows, so the five reading crops were cut at native
resolution from the same file by box (all under 2500 px): `images/gaps2/f420r_clear_l4.jpg` (0,2050,1700,2240),
`f420r_r1_margin.jpg` (2380,2240,3000,2490), `f420r_r2g2.jpg` (420,2460,1860,2690), `f420r_r4g2.jpg`
(440,2850,1520,3050), `f420r_r5g2.jpg` (860,3060,1780,3270). 10088714.jpg (f.420v) was not cropped: it carries
only the closing formula, and the clear line "los enemigos de Apure no se ..." is on f.420r (manifest). Vision calls:
2 of 3 (one localisation view of the lower leaf at half scale, for crop boxes; one fresh blind Sonnet read of the five
crops, told nothing about the key, the earlier reads or the print). The reconciliation below is textual, no third call.

| spot | blind read (3 Oct) | earlier reads | 2021 print | settles? |
|---|---|---|---|---|
| clear line 4, last word | "gos de Apure no se **mueben**." (b possibly l/h) | NX-MOR "mueven" | "reciben" (and "del Apure") | **yes, against the print**: two independent eyes read mue-ben; the leaf does not carry "reciben" |
| r2g2 gloss under 6 + 51 56 16 51 33 + 27 | b a [v\|r] [z\|i] n i t [u\|d\|a] S (9 letters, one per sign; this hand's r looks like v, as under r2g1 "por") | "barinituS" | "Caimital" | **the gloss is not "Caimital"**: no C, m or l under the group; it reads bari-nit-?-s, i.e. Barinitas (key "barinrtas"). Position 5 gloss i again (sign 51 = r: conflict stays M); position 7 [u\|d\|a] (key a fits Barinitas; not settled, M) |
| r4g2 gloss under 30 BOX + 22 + 16 + | [J\|I] u a [U\|ll\|H] a n a | "guayana" (two passes) | "Guayana" | partly: letter 0 is read J/I this time, g before -- a split, M; letter 3 reads as ll, so the gloss may spell "Guallana" (22 = ll, as in Trujillo), against the print's y -- M |
| r5g2 gloss under 27 51 10 BOX 51 18 | [t\|L\|f] r g u [v=r] o, i.e. long-s r g u r o | "seguro" (tentative) | "seguro" | split: this pass reads the gloss's second letter as r, following the sign (51 = r), against the earlier tentative e -- M |
| row-1 margin mark after r1g3 "el" | a "5" over a slanted bar, below it an unclear stroke [2\|n\|h] and a long diagonal flourish; reads as a flourish or paraph, not letters; the paper edge does not cut it (about 120 px inside) | NX-MOR2 "2", NX-MOR3 "28" (stacked 5 over a sign) | "paso el rio [Apure]" | **not a group for "rio"**: r-i-o under key_5186 would need three numerals (51 56 18); the mark carries one legible numeral, no dotted sequence and no gloss word. Stays excluded from the 97; the print's "río" is not enciphered on this leaf at that place (an editorial supply or taken from elsewhere -- not settled here) |

Grades (rule 4), `python3 build_key_5186.py --check` exit 0 and `python3 tools/decode_key.py ciphers/rah-morillo-1817
--check`: "ciphertext_5186.tsv: tokens 97: C 90, M 7 / reading up to date", exit 0 -- **C 90 / M 7 / U 0 of 97,
unchanged**. No token moved: every M position is still two period witnesses (the sign as read by three passes, the
gloss as read now by three) or the gloss and the print disagreeing, and a single fresh read that splits from two
earlier tentative ones is not a settlement. What changed is the record: the exceptions.tsv reasons for r2g2 5/7,
r4g2 0/3 and r5g2 1 now carry this pass's gloss letters (build_key_5186.py EXCEPTIONS; KEY_WORDS, the shuffle
control's input, untouched, so `shuffle_control_5186.py` cannot vary with this step and was not re-run -- rule 3). No
change to ciphertext_5186.tsv (git diff empty). The two print disagreements the 26 Sept audit handed to the solver lane
(AUDIT.md section 5) come out against the print both times ("mueben" on the leaf; no "Caimital" in the gloss), so the
2021 text is a modernised, partly re-read version of this leaf, not a character-level witness at those two places.
Rule 10: nothing here is new; item 3 stays N0 (AUDIT.md), key `period`.

## GAPS3-rah-morillo-1817 (3 Oct 2026, account-4): Aymeloglu PARES-cache grep for item 2's received original

Step (Verdict line of 3 Oct): grep A. Aymeloglu's cached PARES sweep for the Ministerio de la Guerra's received
original of Morillo's 19 Nov 1817 letter and its enclosed "clave". Source: github.com/aaymeloglu/unsolved-ciphers,
shallow clone of commit d2800bb2 (27 Sept 2026) to scratch, data files only (`catalogue/pares-hits.jsonl` 1115 lines,
`pares-pages.jsonl` 501, `pares-images.jsonl` 536, `pares-ranked.md`, `pares-exclude.txt`); cited, no code copied
(the repository has no licence). PARES itself not contacted (dead from the cloud). Requests: github.com 1 clone;
no other host.

Result: **no hit.** Over the 1115 distinct PARES units in the cache: "morillo" 0, "enrile" 0, "herrera" 0,
"cartagena" 0, "costa firme" 0, "ministerio de la guerra" 0; "clave" 8 (all 1615-1876 and none Morillo: AHN
Diversos-Títulos 1840-58, AHN Ultramar 1866-76, AGS CCA 1615-16); "1817" 20 units, all AGI ESTADO diplomatic
dispatches (London, St Petersburg, Brazil/Montevideo, Fernán Núñez, Campuzano), none from Costa Firme or the war
office, none dated November 1817.

What the negative covers (the control on the search itself): the cache does reach this period -- 80 units dated
1810-1825, so a cipher-described 1817 unit would be in it if its series was swept -- but those 80 sit in only three
series: AGI ESTADO (75), AHN DIVERSOS-COLECCIONES (4), AHNOB BAENA (1). It holds no unit from the Archivo General de
Simancas Secretaría de Guerra (SGU), the AGI Caracas or Santa Fe audiencias, or any war-office series (0 signaturas
containing GUERRA, SGU or CARACAS). And its six queries are cipher words only (cifrada 609, "carta cifrada" 190,
descifrada 181, "en cifra" 101, "cartas cifradas" 20, cifradas 14): a received covering letter described as
enclosing a "clave", or catalogued only by sender and date, would not have been retrieved. So this is a search
result on Aymeloglu's sweep, not evidence that no received original survives in a Spanish archive; which archive
holds the Ministry's 1817 file is still not established here.

Next for this gap: a PARES search from the owner's own browser (LOCAL-QUEUE row, not filed by this step):
"Morillo" AND "clave", and "Morillo" with date 1817-11, in AGS Secretaría de Guerra and AGI Caracas / Estado
(Costa Firme), recording archive, signatura and the digitised flag of any hit.

## GAPS186-rah-morillo-1817 (3 Oct 2026, account-4): PARES row filed; RAH-side metadata for item 2's other copies

Step (Verdict line of 3 Oct): file the LOCAL-QUEUE row for a PARES search from the owner's browser for item 2's
received original. PARES is dead from the cloud (CLAUDE.md host table: "dead host, 24 Sept 2026: the origin server's
own TLS cert chain is incomplete"), so no request was made to it. Filed **LOCAL-QUEUE.tsv row L48** (kind
`catalogue-lookup`, status `queued`): control search 'Morillo' first, then 'Morillo' AND 'clave', 'Morillo' AND
'cifra', 'Morillo' 1817-11-01 to 1818-06-30 in AGS Secretaría de Guerra and in AGI (Caracas, Santa Fe, Estado), and
'Calabozo' 1817; hit count, archive, signatura, title, date and digitised flag per search.

While-waiting action run in the same session (depends on nobody, 3 requests): RAH OAI-PMH `GetRecord`
(`metadataPrefix=didl`, plain curl; not behind Anubis) for the three unopened RAH records of the item-2 gap:
| record | catalogue title (abridged) | date | images (idImagen) |
|---|---|---|---|
| 1759 | Morillo al Ministro de la Guerra ... propone una clave de cifras ... Calabozo, 19 [Nov 1817]; "Copia"; "Publicado por Rodríguez Villa, t.° III, doc. n.° 655, pp. 462-463" | 1817 | 2: 10080060, 10080061 |
| 3893 | Morales a Morillo comunicándole el recibo de la clave de la correspondencia con Montero ...; "firma autógrafa" | 1819 | 3: 10084429-10084431 |
| 3886 | Morales a Morillo sobre los oficios enviados por Montero, la clave utilizada y su desconocimiento de la misma. Guardatinajas, 10 Sept 1819 | 1819 | 2: 10084370, 10084371 |

Record 1759's metadata answered at once (the earlier failure was the Tomcat error on its viewer page, NX-MOR4); its
catalogue entry says it is a copy, printed as Rodríguez Villa t.III doc. 655, the same printing that carries no key
table, so its two images are more likely the letter than the table -- unchecked until fetched. 3893 and 3886 are
about a Morales-Montero key of 1819, not the 1817 war-office key; whether either carries a table is unchecked.
Image ids are now on record for the next image fetch (`tools/browser_fetch.js --binary`). No reading changed; no
grade changed; `decode_key.py --check` not re-run (no key or transcription touched). Requests:
bibliotecadigital.rah.es OAI 3; PARES 0; no other host.

`python3 tools/gaps_check.py rah-morillo-1817` (3 Oct 2026): `OK keep-going rah-morillo-1817: keep going: 3 internal
gap(s), 1 step(s) untried`, exit 0. `python3 tools/next_steps.py --wait-only | grep rah-morillo`: empty (exit 1).

## GAPS192-rah-morillo-1817 (3 Oct 2026, account-4): the 7 RAH images of records 1759, 3893, 3886

Step (While-waiting line of 3 Oct): fetch the 7 images whose idImagen ids GAPS186 read from the OAI didl records, and
say per image whether it carries cipher, a key table or a clear copy relevant to item 2. Route: `tools/browser_fetch.js
--binary` on `imagen_id.do?idImagen=N` (the container lacked the proxy CA in Chromium's NSS store; added with certutil
per the Access playbook, then the fetches ran). No transcription, no reading.
| record | idImagen | leaf | what it shows |
|---|---|---|---|
| 3886 | 10084370 | f.419r | Morales to Morillo, Guardatinajas 10 Sept 1819; clear autograph letter (Montero's oficios, not knowing the key); no numerals, no table |
| 3886 | 10084371 | f.419v | continuation, signed; clear; no numerals, no table |
| 3893 | 10084429 | f.429r | Morales to Morillo, Guardatinajas 13 Sept 1819 (catalogue: 19 Sept); clear letter opening with receipt of "la clave"; no numerals, no table |
| 3893 | 10084430 | f.429v | continuation; clear; no numerals, no table |
| 3893 | 10084431 | f.430r | end of letter, signed; clear; no numerals, no table |
| 1759 | 10080060, 10080061 | 9/7656 f.524-524v | not seen: both answered HTTP 200 `image/jpeg` whose body is a Tomcat stack trace for the missing 401 error page (`ClassNotFoundException: org.apache.jsp._401_jsp`), on the first try and on the one retry after a 20 s pause; the same record's viewer gave a Tomcat error twice in NX-MOR4, so the image itself is refused (an access restriction on this record), not a route fault |

Result: neither 1819 Morales letter encloses or copies a key table, and neither carries ciphertext; the key they discuss
(Montero's, 1819) is not on these leaves. Record 1759 stays unseen; its catalogue entry says it is a copy printed by
Rodriguez Villa t.III doc. 655, which carries no table. Item 2's enclosed table is therefore not on any RAH leaf that
the RAH serves. Images: `images/gaps192/` (half-size re-encodes, the folder is at the 30 MB line; native size, bytes
and sha1 in `images/gaps192/manifest.json` for re-fetch). One vision call (a 5-image contact sheet, read by this
session). No reading or grade changed; `decode_key.py --check` not re-run (no key or transcription touched). Requests:
bibliotecadigital.rah.es imagen_id.do 10 browser fetches (7 first pass, 3 retries; each `--binary` fetch may retry
navigation internally); no other host.

## GAPS198-rah-morillo-1817 (3 Oct 2026, account-4): item 1's leaf, RAH record 2242 (9/7658 ff.32-34)

Step (Verdict line of 3 Oct): fetch record 2242 by OAI didl (`verb=GetRecord`, `metadataPrefix=didl`, 1 request: 8
idImagen ids, 10075159-10075164 and 10089847-10089848) then `tools/browser_fetch.js --binary` per image; one
contact-sheet vision call. No transcription, no reading. (Chromium again lacked the proxy CA; added with certutil per
the Access playbook before any image request reached the host.)
| idImagen | leaf | what it shows |
|---|---|---|
| 10075159 | f.32r | clear opening, Enrile to Morillo, Madrid 15 Jul 1817 ("No la he descifrado aun toda"); at the foot "(Sigue en cifra, cuyo descifrado en el siguiente)" and 2 lines of dot-separated numeral ciphertext |
| 10075160 | f.32v | about 17 lines of dot-separated numeral ciphertext (codes seen at a glance 1-20, 00, 120, 187, 400 and a triangle sign), crossed by two later violet strokes; then clear "En el correo proximo escribire mas largo ... Madrid 15 de Julio. P. Enrile" and a clear postscript ("Apodaca tranquiliza el reino ...") |
| 10075161 | f.33r | headed "Descifrado" (violet archivist's note "del doc.to 609"): the decipherment of the cipher block written out as running clear text in brown ink ("... creo q. he hecho quanto esta de mi parte, y procurare q. el indulto se cumpla ..."), ending "(vuelta)" |
| 10075162 | f.33v (presumed) | not fetched: 2 calls, no binary response (Anubis flakiness, not the Tomcat 401 that 1759 gives) |
| 10075163 | f.34r | 3 clear lines (end of the postscript), rest blank |
| 10075164 | f.34v | blank (bleed-through); docket "1817 Julio" |
| 10089847 | f.35 | not fetched (as 10075162); catalogue: folder note "Francisco Warleta, marzo-octubre 1816" |
| 10089848 | f.36r | later folder cover "Cartas del coronel Warleta ...", not part of the letter |

Result: leaf 2242 carries numeral ciphertext (f.32r foot + f.32v, about 19 lines) and a period decipherment of it on
a separate leaf (f.33r, continued on f.33v), so a key for this 1817 Enrile-Morillo cipher is recoverable at grade C by
aligning the numerals against the "Descifrado" (and against Rodriguez Villa t.III doc. 609's print as a second
witness). No key table on any leaf seen. On its face the notation (dot-separated 1-20 / 00 / 120 / 187 / 400) differs
from key_5186's (item 3, 1820); not tested. No reading or grade changed; `decode_key.py --check` not re-run (no key or
transcription touched). Images: `images/gaps198/` (6 half-size re-encodes, native size/bytes/sha1 in its
manifest.json; folder 29 MB). Vision calls: 1 (6-image contact sheet). Requests: bibliotecadigital.rah.es OAI 1;
imagen_id.do 12 `browser_fetch.js --binary` calls (8 first pass, 4 single retries; each call may retry navigation
internally; an earlier batch of 8 failed at the container's TLS store before reaching the host); no other host.

## GAPS203-rah-morillo-1817 (3 Oct 2026, account-4): item 1's key from the leaf's own Descifrado

Step (Verdict line of 3 Oct): re-fetch f.33v, crop, two blind numeral passes + reconcile, read the Descifrado, align to a
grade-C key with the per-leaf shuffle control, then try the key on the folder's other ciphertext.

- **Fetch.** f.33v (idImagen 10075162) answered on the first call this time (`tools/browser_fetch.js --binary`, native
  2453x3768, sha1 0ab71e4e...); f.32r and f.32v re-fetched natively (sha1 = the GAPS198 manifest); f.33r failed (no
  binary response after the tool's retries; its committed half-size copy was enough, it is not the Descifrado of this
  block, see below). Half-size f.33v added to `images/gaps198/` (manifest has native size and sha1); folder 29.97 MB.
- **What the Descifrado is.** f.33v carries, at the top, the end of the f.33r text ("... de estos particulares"), and
  at the foot a **pasted slip**: "No siento que hayan batido à la torre, sino el como, y el sitio, ¿pues que mas podian
  desear? ... Multiplicar correos y apretar sobre q. todo se pierde." The violet note on f.32v ("ojo aqui el
  descifrado", arrow) points to it, and its three paragraphs match the cipher block's three indented paragraphs. The
  f.33r(-v top) text ("Yo creo q. he hecho quanto esta de mi parte ... de estos particulares") is printed by Rodriguez
  Villa t.III p.331-332 under the same "(1) Lo que sigue en cifra" mark, but **its ciphertext is not on this leaf**: the
  numeral block of f.32r-v is the slip's text only. (The violet "No" before the first group on f.32r is an archivist's
  mark, not cipher.)
- **Crops** (pasted command, regions in `gaps203/crops_manifest.json`; crops not committed, 30 MB rule):
  `python3 tools/iiif_lines.py --image <native 10075159|10075160|10075162> --region <R> --out <dir> --prefix f32r|f32v|f33vslip --max-width 2460`
  -> 2 + 12 numeral line crops, 3 Descifrado bands.
- **Numerals.** Two blind Opus passes per page (4 calls; `gaps203/passA.tsv`, `passB.tsv`), `tools/reconcile_passes.py`:
  244/246 agree (99.2%). The two splits settled on the native image (1 reconcile unit): f32r_L01 col 10 = 15 (B), col 13
  = 5 (both passes misread it as 9/8; it is this hand's 5, as in "5 00 120" = hab-); the 5 groups under the ink blot of
  f32v_L01 (187.1?.1.13 struck) are the encipherer's own cancellation and are not carried. 240 tokens in
  `ciphertext_2242.tsv`.
- **Descifrado read**: 1 Opus pass (`gaps203/descifrado_slip.txt`), 10 lines. Two words the pass marked unsure follow
  the cipher and the 1908 print: "tanta" (pass: "ternura{?}"; the cipher reads 18 00 11 18 00 = t-a-n-t-a) and "que"
  (pass: "q.l{?}").
- **Key** (`align_2242.py`, hand-paired DP + hard EM, the interlinear_align shape; that tool's --code-prefix mode cannot
  give code 400 two letters): a letter cipher, one sign per letter, no word breaks, rr and ll written once, spelled by
  sound: a 00, b 120, c 187, d 1, e 2, g 4, h 5, i 6, l 9, m 10, n 11, o 13 (and 12 once, M), p 14, q 15, r 16,
  s 17 (also z in "porraso" and c in "operasiones"), t 18, u/v 19 and 20, y triangle, "ga" 400 (`key_2242.tsv`,
  22 codes).
- **Control (rule 3, the Szembek per-leaf paragraph)**: recurring-code majority-agreement 0.975 real against 0.234
  mean / 0.257 p95 / 0.262 max for the same EM on the Descifrado with its word order shuffled within each paragraph
  (20 seeds). The pairing clears its control decisively; nothing is held.
- **Reading** (`tools/decode_key.py . --check`, exit 0): `reading_2242.txt`, 240 tokens **C 237 / M 3 / H 0 / S 0 / I 0 / U 0**.
  M: f32v_L02 pos 11 (187 = c where the Descifrado has s: "decear"), f32v_L10 pos 17 (11 = n where it has s:
  "coreon y" for "correos y"), and the single 12. Reads "no siento que hayan batido a la tore sino el como y el sitio
  pues que mas podian decear un poraso ali se resiente en todas partes y rompe el nudo de las operasiones me encarga u
  que hable con energia con tanta he hablado que lo sabra u a su tiempo multiplicar coreon y apretar sobre que todo se
  pierde". This plaintext is in print (Rodriguez Villa t.III, 1908, p.332; item 1 is found-solved): what this step adds is
  the key; the plaintext was already in print.
- **Judge** (rule 7): `python3 tools/judge_plaintext.py specs/rah-morillo-1817.json --file <reading, letters only>`:
  `FAIL language: score=-0.944, null_p99=-1.813, real_p05=-0.921, real_median=-0.812, mode=both, N=241`. The leaf's own
  Descifrado through the same judge: `FAIL language: score=-0.899, null_p99=-1.832, real_p05=-0.894, real_median=-0.812,
  mode=both, N=245`. The genuine period text itself misses the gate, so at this length and register the judge cannot
  decide (the ZX-DEC349 shape); the reading's C grade rests on the Descifrado, not on the judge.
- **Payoff test, the key on the folder's other ciphertext**: the only other ciphertext on disk is item 3's block
  (ciphertext_5186.tsv, 1820, Herrera). key_2242 keys 27 of its 97 tokens and gives the key_5186 letter at 0 of them:
  a different key (no design check needed: 1817 Enrile letter cipher vs 1820 Herrera 1-56 table). No other numeral
  text in records 1306/1487/1957/3886/3893/4332/4537/5195 was keyed by it (none of those carries this notation: the
  Ministerio nomenclator, Aldama's tally glyphs, or clear letters, NX-MOR4/GAPS192). So the key reads nothing beyond
  its own leaf yet.
- Vision calls: 5 Opus (2+2 numeral, 1 Descifrado) + 1 reconcile unit (3 zooms read by the worker). Requests:
  bibliotecadigital.rah.es imagen_id.do 4 `browser_fetch.js --binary` calls (3 binary, 1 failed after internal
  retries); archive.org 1 (Rodriguez Villa t.III djvu text, scratch only); no other host.

## GAPS209-rah-morillo-1817 (4 Oct 2026, STALE4 account-1 worker for account 4): f.35 and the July 1817 Enrile sheet

Step (Verdict line of 3 Oct, re-run after account 4's 19:18 UTC 3 Oct claim went stale): fetch f.35 of record 2242
once, one look, then search the RAH catalogue for a separate July 1817 Enrile cipher sheet carrying the ciphertext of
the f.33r(-v top) Descifrado passage ("Yo creo q. he hecho quanto ... de estos particulares").

- **f.35 (idImagen 10089847).** First `tools/browser_fetch.js --binary` call: 3 internal attempts, all text/html (Anubis);
  a page fetch after a 20 s pause then rendered the image (title "imagen_id.do (2476x3299)"), and one `--binary` call
  with the same profile saved it (native 2476x3299, 770,910 bytes, sha1 ec72d059...; entry in
  `images/gaps198/manifest.json`, image not committed: folder at the 30 MB line). Three band crops (ImageMagick, half
  size), one Opus look: a **pencil folder divider only** -- "c)", folio "35", "Francisco Warleta", "Marzo-Oct. 1816";
  lower half blank, no ink text, no numerals. f.35 is excluded; it opens the next folder (record 2243, below).
- **Catalogue search** (`resultados_busqueda.do?busq_general=...` by GET through the browser tool; plain GET works, no
  POST needed): "Enrile cifra" 0 hits; "Enrile" 66 hits (positive control: record 2242 itself is hit 2; facets 1815 29,
  1816 19, 1817 9, 1818 2, 1819 3, 1820 2, undated 2); "Enrile 1817" 11 hits. The 1817 Enrile-authored records are
  three: 2242 (item 1, 15 Jul), **2240** (Enrile to Morillo, Madrid 26 Jun 1817, arrival and dealings with the King,
  Ministro and Junta de Indias; 1 f.; RV t.III doc. 607 p.296) and **2241** (Enrile to the Ministro de la Guerra,
  Madrid 19 Jun 1817; 20 ff.; RV t.III doc. 608 pp.296-330). OAI `oai_dc` for 2240, 2241 and 2243: neither 2240 nor
  2241 is described as cipher (only "Manuscrito, firma autógrafa" and the RV citation); 2243 is Warleta to Morillo,
  17 Mar 1816 (RV doc. 476), the start of the Warleta folder whose divider is f.35. The 1817 facet link itself failed
  to render twice (navigation race in the tool); the "Enrile 1817" query covers the same 9 records plus 2 others.
- **Result.** No separate July 1817 Enrile cipher sheet is catalogued in the RAH digital library under "Enrile", "Enrile
  1817" or "Enrile cifra"; record 2242's 8 images are now all seen (f.35 a divider, f.36r the Warleta cover). The
  ciphertext of the f.33r passage is not on any leaf of 2242, and the neighbouring records carry no cipher note. Not
  checked: the single leaf of record 2240 (catalogued as an autograph letter; one image). No key, transcription or
  reading changed; `decode_key.py --check` not re-run.
- Requests: bibliotecadigital.rah.es 13 (imagen_id.do 5 navigations in 3 browser calls; resultados_busqueda 5
  navigations in 4 browser calls, the facet link counted twice; OAI GetRecord 3 by curl), all >=2 s apart, no 401/403/429
  beyond the Anubis retries. Vision calls: 1 (3 band crops of f.35). No other host.
- Suggestion (not done, outside this brief): fetch record 2240's one leaf (OAI didl, 1 + 1-3 requests) to exclude it;
  if clear, the f.33r passage's ciphertext is a needs-physical-access question for the RAH (the sent cipher sheet may
  survive unscanned in leg. 15 or be lost).

## Remaining gaps (finish-or-blocker pass, 1 Oct 2026)
Read so far: item 3, 90 of 97 cipher tokens at C (92.8%), 7 M, 0 U (`tools/decode_key.py --check` on 2 Oct 2026 after GAPS-rah-morillo-1817 folded the 2021 print into key_5186.tsv and exceptions.tsv; was C 86 / M 5 / U 6 by AUDIT.md section 3); all 21 groups carry a period gloss word, and the block's plaintext is in print (Portuguesa en Carabobo, 2021, p.37 n.100). Item 1: its leaf's numeral block (record 2242, f.32r foot + f.32v) reads 240 tokens, C 237 / M 3 (`decode_key.py --check`, 3 Oct 2026, GAPS203; key from the leaf's own Descifrado); the letter's earlier cipher passage (RV t.III p.331-332) has no ciphertext on the leaf. Item 2 is a clear letter; its enclosed key table is unread.
Done 2 Oct 2026 (GAPS-rah-morillo-1817, section above): the former first gap -- the 6 U tokens and r5g1's M token -- is closed by the print fold-in: 26 = v, 28 = j, 10 = g at C; r5g1 position 1 C under "Bolivar"; sign 22 does not hold as one value (l / y / ll from three print words) and is logged M with each print letter in exceptions.tsv; sign 30 (j in dijo, g in Guayana) is untestable at this N and stays j with the conflict recorded and r4g2 position 0 at M; exceptions.tsv carries V9's split; `decode_key.py --check` C 90 / M 7 / U 0, exit 0.
Done 3 Oct 2026 (GAPS2-rah-morillo-1817, section above): the image check -- clear line reads "mueben" (print "reciben" not on the leaf); r2g2 gloss is bari-nit-?-s, no "Caimital"; r4g2 and r5g2 gloss letters split from the earlier reads (M kept); the row-1 margin mark is a "5" over a bar with a flourish, not a three-numeral r-i-o group, excluded from the 97; C 90 / M 7 / U 0 unchanged, `--check` exit 0.
- item 3, the 7 M tokens (r2g2 positions 5 and 7, sign 22 at r2g4/r4g2/r6g1, r4g2 position 0, r5g2 position 1) - blocker: open-codes; each is a single-occurrence conflict between period witnesses (the sign, read identically by three numeral passes; the interlinear gloss, now read by three eye passes that split at r4g2 position 0 and r5g2 position 1; the 2021 print, which GAPS2 found is not a character-level witness at r2g2 or the clear line), logged in exceptions.tsv with every witness; this leaf has no further occurrence to narrow them (GAPS2-rah-morillo-1817 section, 3 Oct 2026)
- item 1, the ciphertext of the f.33r(-v top) Descifrado ("Yo creo q. he hecho quanto ... de estos particulares", printed RV t.III p.331-332 as cipher) - blocker: not-attempted; done 3 Oct 2026 (GAPS203-rah-morillo-1817 section): the f.32r-v numeral block (240 tokens) is the pasted slip's text only, keyed from it at C 237 / M 3 (key_2242.tsv, control 0.975 vs shuffle p95 0.257); the earlier passage's ciphertext is not on ff.32-34; 4 Oct 2026 (GAPS209-rah-morillo-1817 section): f.35 is a pencil folder divider (Warleta 1816), all 8 images of 2242 now seen; RAH catalogue "Enrile" 66 / "Enrile 1817" 11 / "Enrile cifra" 0 hits, no separate July 1817 Enrile cipher sheet catalogued, neighbours 2240 (26 Jun 1817, 1 f.) and 2241 (19 Jun 1817, 20 ff.) carry no cipher note; next: fetch record 2240's single leaf once to exclude it, then file the passage as needs-physical-access (RAH leg. 15), ~$0.5
- item 2, the enclosed key table ("la adjunta clave", 19 Nov 1817), other RAH-side copies - blocker: needs-physical-access; the table is absent from the copybook copy, record 1957 (3 images, NX-MOR), and from Rodriguez Villa t.3, but the second copy, record 1759 (9/7656 f.524-524v), returned a Tomcat error page twice and was never seen, and records 3893 (Morales acknowledges receipt of a key, 19 Sept 1819) and 3886 (Morales on Montero's oficios and the key used, 10 Sept 1819) were not fetched, past NX-MOR4's 4-candidate cap (rederiv_transfer/candidates.tsv); 3 Oct 2026 (GAPS186-rah-morillo-1817): OAI didl metadata for all three answered (1759: 2 images, a copy, printed RV t.III doc. 655; 3893: 3 images; 3886: 2 images; idImagen ids in the GAPS186 section); 3 Oct 2026 (GAPS192-rah-morillo-1817 section): 3893 and 3886 fetched (5 images), all clear 1819 letters, no table, no ciphertext; 1759's two images refused by the RAH server (401 error page, twice), and its catalogue says it is the copy printed in Rodriguez Villa t.III doc. 655 without a table; blocker: needs-physical-access (record 1759 refused online; a reproduction request to the RAH is the only route)
- item 2, the original letter and enclosure as received by the Ministerio de la Guerra - blocker: waiting-on LOCAL-QUEUE L48; the RAH holds only Morillo's retained copies; done 3 Oct 2026 (GAPS3-rah-morillo-1817 section): Aymeloglu's cached PARES sweep (catalogue/pares-*.jsonl, commit d2800bb2, 1115 units) has no Morillo, Enrile, Herrera or Costa Firme unit and no Nov 1817 unit, but it covers only AGI ESTADO, AHN DIVERSOS-COLECCIONES and AHNOB BAENA for 1810-25 and was queried by cipher words only, never "clave" or a name, so the received original is unsearched rather than absent; PARES is dead from the cloud; 3 Oct 2026 (GAPS186-rah-morillo-1817): the PARES search is filed as LOCAL-QUEUE.tsv row L48 for the owner's browser (control 'Morillo' first; 'Morillo' AND 'clave'/'cifra'; 'Morillo' 1817-11 to 1818-06 in AGS Secretaría de Guerra and AGI Caracas/Santa Fe/Estado; 'Calabozo' 1817); blocker: waiting-on LOCAL-QUEUE L48

## Escalation (1 Oct 2026)
- [x] siblings: NX-MOR4 searched the RAH Morillo fonds (about 13 catalogue searches: cifra, cifrado, clave, Herrera and combinations) and opened records 5195, 4332, 4537, 1306 and 1487 (20 images): no ciphertext compatible with key_5186; 4332 carries Aldama's own vowel-only tally-glyph key, 1306/1487 a Ministerio de la Guerra tens-pattern nomenclator with its own "Descifrado" (f.151), already printed in Rodriguez Villa; 5195 f.433 has Morillo acknowledging Herrera's letters "de 7 y 8, la 1a en cifra" (so the 8 Nov letter is clear or unlocated); no DECODE neighbour (no Morillo record in Aymeloglu's cached DECODE catalogue, 24 Sept). Still unopened: 1759 (server error twice; 3 Oct images refused, 401); item 1's leaf 2242 opened 3 Oct 2026 (GAPS198): numeral ciphertext + period Descifrado; its last image f.35 opened 4 Oct 2026 (GAPS209): a Warleta 1816 folder divider; RAH catalogue "Enrile"/"Enrile 1817"/"Enrile cifra" searched 4 Oct 2026 (GAPS209): no separate July 1817 cipher sheet; 3893 and 3886 opened 3 Oct 2026 (GAPS192): clear 1819 letters, no table
- [x] clear-pages: item 3's f.420r carries the period interlinear decipherment under all 21 groups (the key's source, grade C) and f.420v is clear only; item 1's plaintext is printed with its cipher passages marked (usable as the crib for leaf 2242 once fetched); 1306 f.151 is that dispatch's own decipherment, a different design
- [x] known-keys: KEY-DESIGN.tsv holds only key_5186 for this fonds (line 133) and KEY-OFFICES.tsv has no Morillo row; Cryptiana and the Bourdeau and Aymeloglu repositories were grepped for Morillo (24 Sept; AUDIT.md section 4 (e)): no key; the fonds' two other keys (Aldama 1819, Ministerio de la Guerra nomenclator) were compared by design and excluded (NX-MOR4 step 3); design_prior.py not run, moot while no unkeyed ciphertext is on disk in the folder
- [x] print: Rodriguez Villa t.1-t.4 (IA djvu and Google Books search-inside with controls), Contreras 1988, Stoan 1974, Blanco y Azpurua, O'Leary Memorias, Lecuna, `print_check.py` with its global IA pass, OpenAlex, Semantic Scholar, CrossRef and 4 JSTOR rows (all done 26 Sept): item 1 printed 1908, item 3's plaintext printed 2021 (Portuguesa en Carabobo p.37 n.100), item 2's letter printed without its enclosure; no printing of the 1817 key table found
- [x] key-rebuild: done 2 Oct 2026 (GAPS-rah-morillo-1817): the 2021 print folded into key_5186.tsv via build_key_5186.py (26 = v, 28 = j, 10 = g at C; BOX = u confirmed in three more words), exceptions.tsv written for V9's split plus the three sign-22 positions; merged-sign tests: 22 = l|y|ll does not hold as one value (M), 30 = g/j untestable at one word each (M at r4g2); C 90 / M 7 / U 0
- [x] image-check: done 3 Oct 2026 (GAPS2-rah-morillo-1817): gloss letters at r2g2/r4g2/r5g2, the clear line and the row-1 margin mark read blind on native crops and reconciled against the print, C 90 / M 7 / U 0 unchanged; before that, the numerals were read by three passes (NX-MOR2 two blind, NX-MOR3 a third, 0 differences), all agreeing and none failing a gate, so the numeral read is settled rather than retired, and a fourth numeral pass is not proposed; planned: re-read the interlinear gloss letters at r2g2/r4g2/r5g2, the clear-text "mueven"/"reciben" and the row-1 margin mark against the print ("Caimital", "Guayana", "seguro", "reciben", "rio") on native crops
- [x] retry: the key-rebuild and image-check reruns are done (`decode_key.py --check` 2 and 3 Oct 2026, C 90 / M 7 / U 0, no token regraded, margin mark not a group); leaf 2242's numerals aligned to the leaf's own Descifrado (the pasted slip on f.33v) on 3 Oct 2026 (GAPS203): key_2242.tsv, C 237 / M 3 of 240, `--check` exit 0; the key does not read item 3 (0 of 27 keyed tokens agree with key_5186)
Verdict: keep going: 2 internal gaps, 1 needs physical access (RAH record 1759, refused online), 1 waiting on LOCAL-QUEUE L48 (PARES, owner's browser); cheapest next: item 1, fetch record 2240's single leaf (Enrile to Morillo, 26 Jun 1817) once to exclude it as the carrier of the f.33r passage's ciphertext, ~$0.5 (GAPS209, 4 Oct 2026: f.35 is a folder divider; no separate July 1817 Enrile cipher sheet in the RAH catalogue)

## While waiting

- item 1: fetch record 2240's single leaf (OAI didl, then `tools/browser_fetch.js --binary`) once to check for numeral ciphertext; key_2242.tsv (GAPS203, 3 Oct 2026) would read it at C if it is the same cipher; ~$0.5; depends on nobody while LOCAL-QUEUE L48 (PARES, owner's browser) is open. (f.35 and the catalogue search done 4 Oct 2026, GAPS209.)

## Web and blog check (GAPS-rah-morillo-1817, 2 Oct 2026)

The intake gate (`tools/intake_gate_check.py rah-morillo-1817`) exited 1 on 2 Oct 2026 for one reason only: no logged
open-web and blog comment-thread check (CHECK-SOLVED-WEB, 28 Sept 2026). Run before the key step above, per
`.claude/briefs/check-solved.md` "Required step". On-disk first: `grep -ril "morillo|romerito|guanare|9/7666|enrile"
sources/cryptiana/` -- 0 files (0 requests). Then, 2 Oct 2026, 01:58-02:02 UTC:

| # | query (web search unless noted) | result for THIS target |
|---|---|---|
| 1 | Herrera Morillo Guanare 7 noviembre 1820 carta cifrada Romerito | only the RAH catalogue's own listing pages and unrelated Bolivar/armistice pages; no blog, no decipherment |
| 2 | "9/7666" Morillo cifra OR cifrada OR cipher | noise (Caesar-cipher pages, a chord site); nothing on this shelfmark |
| 3 | "Romerito" "tres oficiales" "buscando a Bolívar" (the decoded phrase, quoted) | no page carrying the phrase; general Bolivar biographies only (the 2021 book itself, already in AUDIT.md, is not in the engine's results) |
| 4 | Enrile Morillo 1817 "carta reservada y cifrada" Real Academia de la Historia (item 1, the folder's title words) | RAH catalogue pages and an Armada Cuadernos PDF on Enrile (opened, below); no decipherment |
| 5 | site:scienceblogs.de klausis-krypto-kolumne Morillo (Cipherbrain) | no post or comment names Morillo |
| 6 | site:cryptiana.blogspot.com Morillo OR Venezuela OR realista cifra (Cryptiana blog) | no post; the 2018 archive page opened (below) |
| 7 | site:ciphermysteries.com Morillo OR Bolívar OR Venezuela cipher 1820 (Cipher Mysteries) | no post about any of the three items |
| 8 | Morillo cipher 1817 1820 solves Claude OR GPT (model-solve announcements) | the 2026 Urquhart "Cyphral Distich" and a 1809 Napoleonic-cipher story only; nothing Morillo |
| 9 | Morillo "clave en cifra" OR "clave de cifra" 1817 Ministro de la Guerra asuntos reservados (item 2) | RAH and Comunidad de Madrid catalogue listings; no key table, no decipherment |
| 10 | Pablo Morillo Chiffre OR verschlüsselt Brief 1817 OR 1820 Venezuela Klausis Krypto Kolumne | a Cipherbrain post on an 1817 letter (opened, below): LeRay de Chaumont to Rosseel, New York shorthand, not this target |
| 11 | "Herrera a Morillo en carta cifrada" (the catalogue title, quoted) | the RAH title index only |

Pages opened and read with their comment threads: (a) armada.defensa.gob.es Cuadernos IHCN 65 cap.4 "Pascual Enrile,
jefe de la escuadra de la expedición" (PDF, 1 request): no cifra/cifrada/clave sentence, no decipherment of item 1;
(b) cervantesvirtual.com "Gran Colombia y España 1819-1822" (PDF): HTTP 403 (the host is Cloudflare-blocked from the
cloud, CLAUDE.md host table), not retried, unreachable; (c) cryptiana.blogspot.com/2018 (1 request): posts on 1470s-1590s
Spanish, French and English ciphers, 0 mentions of Morillo, Venezuela, Herrera, Enrile, Guanare or Romerito in posts or
comments; (d) scienceblogs.de Cipherbrain, "Wer knackt diesen verschlüsselten Brief aus dem Jahr 1817?" (2 Jan 2015,
1 request): LeRay de Chaumont to Joseph Rosseel, Thevenot shorthand, 12 comments, none naming Spain, Morillo or Venezuela.
Requests: web search 11 queries; armada.defensa.gob.es 1; cervantesvirtual.com 1 (403); cryptiana.blogspot.com 1;
scienceblogs.de 1. No login, no credential.

Result: no decipherment or plaintext of items 1-3 located by these queries on 2 Oct 2026 beyond what the folder already
cites (item 1 printed in Rodríguez Villa t.3, 1908; item 3's plaintext in *Portuguesa en Carabobo*, 2021, AUDIT.md) --
a search result, not a novelty verdict (rule 10). Status word unchanged (`partial`, per item as line 2 states).

`python3 tools/intake_gate_check.py rah-morillo-1817` after this section (2 Oct 2026):
```
rah-morillo-1817: partial (line 1) -- edition/page or full-text-search citation found within 6 lines
```
exit 0 (was 1). `python3 tools/gaps_check.py rah-morillo-1817`: `OK keep-going rah-morillo-1817: keep going: 5 internal
gap(s), 2 step(s) untried`, exit 0.

## Premise check (GF4-BATCH5, 3 Oct 2026)

The adversarial pre-reading pass (`.claude/briefs/check-solved.md` "## Premise check"), run per item. No
cryptanalysis, transcription or image fetch was done. Result: **nothing new found.** Two items are already
found-solved, and the folder already says so:
- item 1: plaintext printed in Rodríguez Villa t.3 (1908), cipher passages marked;
- item 3: plaintext printed in *Portuguesa en Carabobo* (2021, p.37 n.100), N0 per AUDIT.md, and deciphered
  interlinearly on the leaf.

Item 2's enclosed key table ("la adjunta clave", 19 Nov 1817) was not found printed or held anywhere searched.
Status unchanged (`partial`, per item as line 2 states).

- **(a) Decipherments the folder already mentions: all opened earlier; none new.**
  - Item 3's interlinear decipherment on f.420r is the key's source, at grade C. Its 2021 print is folded into
    `key_5186.tsv`.
  - Item 1's printed clear (Rodríguez Villa t.3) is already in the folder.
  - Records 1306 (f.151 "Descifrado") and 1487 are Ministerio de la Guerra dispatches with their own
    decipherments, already printed (Rodríguez Villa t.III doc.754, t.IV doc.814). They are different items in a
    different system (NX-MOR4).
  - Record 4537 (Morillo to Pereira, "indicándole la clave", 1819) was opened by NX-MOR4: no compatible
    ciphertext.
  - Record 5195 has Morillo acknowledging Herrera's letters "de 7 y 8, la 1a en cifra", so item 3 is the
    enciphered one.
  - No mentioned decipherment is unopened. The unopened records 1759 (server error twice), 3893 and 3886 are
    candidate key-description letters, not decipherments of items 1-3. They are the folder's own named next step.
- **(b) Other solvers' working files: not found.** Fresh shallow clones on 3 Oct 2026: dbourdeau/cyphersolver
  HEAD a4292cb (2 Oct) and aaymeloglu/unsolved-ciphers HEAD d2800bb (27 Sept), grepped whole and
  case-insensitive for "morillo". Three hits, none a working file for this target:
  - Bourdeau `targets/napoleon/an_ir.txt`: a Napoleonic-era archive list naming a different Morillo in Spain;
  - `targets/esp318/lit/quijote.txt`: Cervantes;
  - `targets/matignon1586/corpus_words_v1.txt`: a word list.
  - Aymeloglu: no Morillo hit anywhere, including `catalogue/decode-*`, `bne-*` and `pares-*`.
- **(c) Physical neighbours: covered earlier; nothing new.**
  - Item 3: both sides of the leaf (f.420r cipher with gloss, f.420v clear close) were imaged by NX-MOR. The
    acknowledging reply, record 5195 ff.432v-433, was opened by NX-MOR4.
  - Item 2: the three copybook images (ff.155v-156v) were imaged. Entry N.196 runs mid-page into unrelated entries
    before and after, so the key table was never copied into the register beside it (NX-MOR).
  - Item 1's leaf (record 2242, ff.32-34) has never been imaged. Its plaintext is printed, so the leaf matters for
    key recovery, not for whether the item is read. It is already a named gap.
- **(d) Recipient side: not found.** Item 2's recipient is the Ministerio de la Guerra.
  - Aymeloglu's cached PARES sweep (`catalogue/pares-hits.jsonl` 1,115 rows, `pares-pages.jsonl` 501) was grepped
    for morillo, Venezuela, Tierra Firme and Costa Firme, and every 1815-1821 row was listed. The only
    1817-1820 American-war hit is AGI ESTADO,64,N.46, "Expedición a favor de insurgentes de Venezuela y Colombia"
    (1820), an unrelated file. No Ministerio de la Guerra file of Nov 1817 from Morillo appears.
  - That sweep was run only on cipher-keyword queries ("carta cifrada", "en cifra" and similar), so it cannot
    exclude a received original catalogued without such a word. This is a limited negative; PARES itself is dead
    from the cloud (host table).
  - IA full-text search (be-api, all items): `"numeracion que da el valor"` (item 2's own sentence) hits only
    Rodríguez Villa t.3 (`eltenientegener01villgoog`), the letter already cited, printed without its enclosure.
    `"adjunta clave" Morillo` hits only an unrelated 20th-century book. `"Romerito" Herrera Guanare 1820` hits
    *Portuguesa en Carabobo* (already AUDIT.md's N0 source), the *Archivo del general José Antonio Páez* t.I and
    O'Leary's *Memorias* t.II (already searched 26 Sept, per Escalation "print"). None prints item 2's key.
  - Items 1 and 3 were addressed to Morillo, so the RAH fonds itself is the recipient's archive. That side is
    covered by (a) and (c).

No new next step. The folder's Verdict line stands: the gloss image-check, then records 1759/3893/3886 and leaf
2242.

Hosts this pass: be-api.us.archive.org 3, github.com 2 clones (shared with the two other targets in this batch).
All requests were at least 1.6 s apart, with no 403, 429 or challenge. bibliotecadigital.rah.es was not
contacted. Rule 10: this is a search log; it makes no novelty claim.

`python3 tools/intake_gate_check.py rah-morillo-1817` (after this section):
```
rah-morillo-1817: partial (line 1) -- edition/page or full-text-search citation found within 6 lines
exit 0
```
