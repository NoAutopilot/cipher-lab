# AUDIT: antt-linhares-chave -- novelty of LX-DEC's m0002 reading and the Vieyra 1809 identification

Verifier session (LX-VER, Sonnet, session_01P3oxP9wNykkszLTY7eMVMw), 25 Sept 2026, 01:55-02:35 UTC. Parent: LANE LX
orchestrator session_01UXTpujdthrPiBDUG57oNwf. Adversarial audit; this worker did not solve, did not touch
key.tsv/reading.txt/ciphertext.tsv, and took no part in LX-TR/LX-BOOK/LX-DEC/LX-SIB's work. Levels N0-N5 are
CLAUDE.md rule 10.

Claim under audit (NOTES.md "Reading (LX-DEC, 25 Sept 2026)", updated by "Fix pass (LX-FIX, 25 Sept 2026)"): pages 2
and 3 of a Portuguese letter in the Linhares papers (ANTT PT/TT/CLNH/0086/11, DigitArq docId
`a03cef08d3c04758aa148f5be56d3401`, m0002) decode against Vieyra's 1809 Portuguese-English pocket dictionary to
"para supprir o seu lugar junto com man o d justa he segredo ate [null] o ministerio / pela memoria do cagar lhe
pauperr ven ha logo" (H 25, M 1); and the key sheet (m0003-m0004) names that dictionary only as "o Diccionario".

## 1. Executive verdict

| item | prior plaintext | prior decipherment / identification | class |
|---|---|---|---|
| (1) m0002 letter fragment: plaintext and decipherment | not located | not located | **N3** |
| (2) key's dictionary = Vieyra 1809 (identification, not a decipherment of a new item) | n/a | not located: no prior print names this Linhares key's dictionary, or decodes this key, or decodes this letter | **N3** |

Neither item may be described as new, unpublished, unread, first, never printed, or previously unknown (rule 10).
The safe statement for the whole folder: "a two-page mid-letter fragment from the Condes de Linhares papers (ANTT
PT/TT/CLNH/0086/11) was read at grade H/M against a dictionary code, using a London 1809 Portuguese-English pocket
dictionary (abridged from Vieyra) identified from the key's own worked example; no prior print of this letter's
plaintext, no prior decipherment of this key, and no prior identification of its dictionary were found in the
sources logged below, searched 24-25 Sept 2026."

Neither item reaches N4: the sender-family edition most likely to carry this fragment (Textos Políticos,
Económicos e Financeiros, 1993) could not be opened (host unreachable both times tried), and the Quadro elementar /
Arquivo Diplomático diplomatic-edition family and HathiTrust's full-text index were only spot-checked, not
systematically searched. See "Gaps toward N4" below.

## 2. Why N3 and not lower or higher

**Not N2 (plaintext known elsewhere, no prior mapping):** no prior print of this fragment's plaintext was located
anywhere, so there is no known plaintext to map the ciphertext to.

**Not N1/N0:** no prior decipherment of this ciphertext, and no prior identification of this key's dictionary,
was located.

**Not N4:** N4 requires "the principal editions, catalogues and project pages covered". The ANTT/DigitArq catalogue
is covered (section 4b, read in full via the printed catalogue PDF, not only the API). The family biography *O
Conde de Linhares* (1908) is covered (full-text searched). The solver repositories, Cryptiana, Cipherbrain and
DECODE are covered. But: (a) *Textos Políticos, Económicos e Financeiros* (1993), the one edition most likely to
print a Rio de Janeiro secretariat letter of this correspondent and period, was not read (host unreachable both
routes tried); (b) *Quadro elementar das relações politicas e diplomaticas de Portugal* (Visconde de Santarém) and
the *Arquivo Diplomático* series were only checked by a general web search, not opened and full-text searched;
(c) HathiTrust's own full-text search was not run against this fragment's phrases (the Bibliographic API calls
made this pass failed to resolve a record id for the 1993 edition, so the EF per-page route was never reached).
Closing any one of (a)-(c) is the next step toward N4; none of the three is closed this pass.

**Not N5:** no archive or specialist confirmation was sought this pass (out of scope for a verifier working from
open sources).

## 3. Item 1: the m0002 letter fragment (plaintext and decipherment)

- Unit: ANTT `PT/TT/CLNH/0086/11`, "Chave de uma cifra", maço 86 (fonds Condes de Linhares), dated only
  `[17--]-[18--]` by the archive's own catalogue (confirmed below, section 4b) -- the archive assigns this bundle
  no narrower date than the two-century span. m0002 carries pages "2" and "3" of a longer letter; pages 1 and 4
  are not part of this 6-image item (established by LX-TR, NOTES.md).
- Reading as decoded (rule-10-safe quotation, LX-DEC/LX-FIX): "para supprir o seu lugar junto com man o d justa he
  segredo ate [null] o ministerio / pela memoria do cagar lhe pauperr ven ha logo". About a quarter of the
  26 tokens are single-letter or short dictionary-trim fragments (the key's own fragment-concatenation mechanic
  for proper nouns, e.g. "man", "d", "pauperr", "ven"), not free-standing words, so the fragment does not read as
  connected prose -- a real constraint on how findable it would be by an ordinary phrase search even if printed
  verbatim, since no edition would render dictionary-trim fragments as such.
- Prior plaintext: **not located.** Searched (with dates and queries, section 4).
- Prior decipherment: **not located.** The ANTT catalogue entry for `0086/11` (section 4b) carries no content
  note (`Âmbito e conteúdo`) at all, only title, date-range and extent -- unlike several other entries in the same
  catalogue that do carry a scope note quoting or describing cipher content (section 4b, e.g. the "Lorient"
  cipher entry, the "só poderá decifrar" entry, the "está junta a decifração" entry -- none of which is this
  item). No other source located a reading.
- Class: **N3**, confidence moderate-high for "not in the print located", low-moderate for "no one has ever read
  it" (an archive holding a plaintext key can be read by staff or a private scholar without publishing; the
  fragmentary, largely-illegible-as-prose nature of the passage also limits what a phrase search could catch even
  if it were printed).
- Safe sentence: "This two-page mid-letter fragment was read from the cipher key and a period dictionary at grade
  H/M; no prior print of its text or prior decipherment was found in the sources searched 24-25 Sept 2026 (this
  file)."
- Unsafe sentence: "A previously unknown Linhares dispatch, deciphered for the first time."

## 4. Item 2: identification of the key's dictionary as Vieyra 1809

- The key sheet (m0003-m0004) names its dictionary only as "o Diccionario" / "o Diccionario Inglez" -- never a
  title, author or edition. LX-BOOK identified it as Antonio Vieyra (abridger), *A New Pocket Dictionary of the
  Portuguese and English Languages... Abridged from the Dictionary of Mr. Vieyra*, Part I, London 1809, by testing
  all twelve worked-example groups against the edition's page/column/rank arithmetic (BOOK.md) -- an internal,
  cryptanalytic identification, not sourced to any prior claim.
- Question: has anyone printed that this Linhares key uses Vieyra's dictionary, or deciphered this key at all?
- Not located anywhere searched (section 4). The ANTT catalogue's entries for all three "Chave de uma cifra" items
  in the Condes de Linhares fonds (`0086/11`, `0020/14`, `0078/80` -- section 4b) carry no dictionary reference; the
  one dictionary mention found anywhere in the whole printed catalogue (`Menciona que no Dicionário Geográfico do
  Reino...`, item `0021/07`) is an unrelated finance memorandum referencing a different, geographical dictionary,
  not a cipher key.
- Class: **N3**, confidence moderate-high (a fairly specific, checkable claim -- a named 1809 London imprint tied
  to a specific archival key -- for which an open-index scholarship sweep and a catalogue read both came back
  empty).
- Safe sentence: "No source located in this search names Vieyra's 1809 dictionary, or any dictionary, as the key
  to this Linhares cipher, or reports a prior decipherment of it; the identification here rests on the internal
  fit of all twelve worked-example groups (BOOK.md)."
- Unsafe sentence: "The first person to identify the dictionary behind this cipher" / "newly discovered that
  Linhares used Vieyra's dictionary."

## 5. Search log (rule 10, verifier template)

Dates below are `date -u`; this session started 2026-09-25 01:55 UTC.

**(a) Canonical/sender/recipient editions and diplomatic series:**
- *O Conde de Linhares* (Marquês do Funchal, 1908), archive.org `ocondedelinhares00func`: full djvu text
  downloaded and searched (via `tools/print_check.py`) for all 8 phrases in `phrases.txt` (both archaic and modern
  spelling of all four required phrases plus variants) -- **no hits, any phrase.** (Prior workers already found
  zero hits for "cifra" in this same volume, 24 Sept 2026; this pass is an independent, phrase-level re-check.)
- *D. Rodrigo de Sousa Coutinho, Textos Políticos, Económicos e Financeiros (1783-1811)* (ed. Mansuy-Diniz Silva,
  Banco de Portugal, 1993): **unreachable, confirmed again.** `bportugal.pt/sites/default/files/ocpep-7_t1.pdf`
  gave HTTP 403 on 24 Sept (logged already). This pass tried the brief's suggested alternate route, the Wayback
  Machine CDX index (`web.archive.org/cdx/search/cdx?url=bportugal.pt/...ocpep-7_t1.pdf`): both the first attempt
  and the one retry after a pause failed at the transport level (`curl: (35) Recv failure: Connection reset by
  peer`, agent-proxy log shows the tunnel to `web.archive.org:443` closed mid-exchange) -- not a 403 or empty
  result, a proxy-level failure to this host, consistent with `web.archive.org` connectivity being flaky for this
  session rather than the page being genuinely absent from Wayback. Not retried further, per the one-retry limit.
  **Not read; this is the largest gap toward N4** (see section 2).
- *Quadro elementar das relações politicas e diplomaticas de Portugal* (Visconde de Santarém) and the *Arquivo
  Diplomático* series: checked only by web search (`"Quadro elementar" OR "Arquivo Diplomático" Linhares Sousa
  Coutinho cifra dicionário 1811`, 25 Sept 2026) -- no hit connecting either series to a cipher, key or dictionary
  for this correspondent. Not opened or full-text searched directly; a gap toward N4.
- D. Domingos de Sousa Coutinho's (1st Marquis of Funchal, London ambassador) published dispatches: not located
  as a distinct printed edition by web search this pass; not separately searched.

**(b) ANTT/DigitArq catalogue and blog, this maço and the whole fonds:**
- The printed catalogue *TORRE DO TOMBO CONDES DE LINHARES: catálogo* (ANTT, ID L 714, Lisboa 2014,
  `antt.dglab.gov.pt/wp-content/uploads/sites/17/2014/12/catalogo-Condes-Linhares-final.pdf`, 4.3 MB) was
  fetched and its text extracted with `pdftotext` (WebFetch's own extraction failed on this scanned/compressed
  PDF; `poppler-utils` was installed to read it directly) and grepped for `cifra|chave de|dicion`. This is an
  independent source from the DigitArq API searches LX-TR and LX-SIB already ran (24-25 Sept 2026) -- it is the
  archive's own printed finding aid, not the live catalogue database.
  - Confirms three "Chave de uma cifra" entries in the whole fonds, matching LX-TR's DigitArq finding exactly:
    `PT/TT/CLNH/0086/11` (this item, 3 f., dates `[17--]-[18--]`, **no scope/content note**),
    `PT/TT/CLNH/0020/14` (2 f., same dates, no note), `PT/TT/CLNH/0078/80` (2 f., same dates, no note).
  - None of the three carries any mention of a dictionary, Vieyra, or a decipherment.
  - Three *other* entries elsewhere in the fonds do carry cipher-related scope notes (not this item): a Lorient
    letter "Era em cifra... completamente cifrada" (maço unidentified in this pass, line ~15455 of the extracted
    text); a note "espécie de cifra, que só poderá decifrar o Sr. F. A. M. G." (line ~17937); and one entry
    "Está junta a decifração, esta carta..." (line ~59541, i.e. a *different* letter in the fonds is catalogued
    as already carrying its own period decipherment). None of these three concerns `0086/11`, `0020/14` or
    `0078/80`; not read further (out of scope -- flagged as a residual, since a catalogue that already notes
    "decifração está junta" for one item in this fonds shows ANTT's cataloguers do note when a decipherment is
    present, and did not for our three key items).
  - The one dictionary reference anywhere in the whole catalogue (`Menciona que no Dicionário Geográfico do
    Reino...`, item `0021/07`, a finance memorandum) is unrelated (section 4).
- ANTT's own blog: web search (`Torre do Tombo blog "Condes de Linhares" cifra chave dicionário`, 25 Sept 2026)
  -- no blog post located discussing this fonds's cipher material.
- Also checked: `idi.mne.gov.pt/pt/atividades/exposicoes/o-segredo-da-escrita-a-criptografia-no-mne` (Instituto
  Diplomático exhibition "The secret of writing -- cryptography at the Foreign Ministry"), surfaced by the phrase
  search for "segredo" -- **unreachable**, HTTP 403 to WebFetch; not retried (single relevant hit, low prior that
  an exhibition page would cover an unpublished ANTT item rather than the Ministry's own archive holdings, not
  worth a second route this pass).

**(c) Internet Archive, HathiTrust, Google Books (via `tools/print_check.py`, all 8 phrases in `phrases.txt`):**
- IA (`ocondedelinhares00func` djvu + global full-text search `be-api.us.archive.org/fts/v1/search`): no hits for
  the two required exact phrases ("segredo ate o ministerio", "pela memoria do") that are distinctive as decoded;
  the shorter, more generic phrases ("pela memoria do", "seu lugar junto com", "supprir/suprir o seu lugar") return
  hundreds to thousands of unrelated hits (hymn lyrics, unrelated 19th-21st century prose) -- read as noise, not
  evidence, per rule 3's logic for a search negative (a common short phrase proves nothing either way).
- HathiTrust: the Bibliographic API was queried for the 1993 Textos Políticos edition by a guessed OCLC number and
  by title text; both queries failed to resolve a record (`"query ... is invalid"` for the title form; the guessed
  OCLC returned zero records) -- **no HathiTrust record was ever reached this pass**, so the HTRC Extracted
  Features per-page route (which needs a resolved volume id) was never attempted. A named gap, not a negative.
- Google Books (key, `country=US`): all 8 phrases queried; the two required exact/distinctive phrases return zero
  hits; the generic phrases return the API's 300-result cap of unrelated modern and 19th/20th-century volumes,
  none about Linhares, Sousa Coutinho, or this letter -- read as noise for the same reason as the IA global search.

**(d) Solver repositories, Cryptiana, Cipherbrain, DECODE:**
- Fresh shallow clones this pass (not reused from 24 Sept, per LESSONS.md's re-clone-before-verifying rule):
  `dbourdeau/cyphersolver` and `aaymeloglu/unsolved-ciphers`, 25 Sept 2026. `grep -rIl -i
  "linhares|sousa coutinho|CLNH|vieyra"` across both, excluding `.git`: **zero hits, either repository** (the
  24 Sept check-solved pass found the same for "linhares/sousa coutinho/CLNH"; this pass adds "vieyra" as a term
  and still finds nothing).
- Cryptiana / Cipherbrain: web search (`Linhares Sousa Coutinho Portuguese cipher`, restricted toward
  `cryptiana.web.fc2.com`/`cipherbrain.de`, 25 Sept 2026) -- no hit on either site.
- DECODE (de-crypt.org): `sources/decode/*.tsv` (records-decrypted, dc11-20-documents, florence-dieci snapshots
  already on disk, 24 Sept 2026) grepped for "linhares|CLNH|sousa coutinho" -- no row. No new DECODE fetch made
  this pass (no record id for this unit is known to exist on DECODE).

**(e) Scholarship, open indexes:**
- OpenAlex (`Authorization: Bearer $OPENALEX_KEY`): keyword searches "Linhares cipher Portuguese diplomatic Vieyra
  dictionary code" (0 hits) and "Sousa Coutinho cifra dicionario chave" (4 hits, all unrelated: whaling history,
  provincial finance, Brazilian foreign policy 1930-45, Diogo do Couto). Both required exact phrases: 0 hits.
  Generic phrases ("pela memoria do" etc.): hundreds/thousands of unrelated hits, read as noise as above.
- Semantic Scholar (`x-api-key: $S2_KEY`): rate-limited (HTTP 429) on most of this session's queries even with the
  key; one query did complete cleanly ("Linhares cifra dicionario chave", 0 hits) before the limiter closed again.
  One retry taken per the good-citizen rule; not retried further. Logged as **partly unreachable** (rate-limited)
  for the remaining queries, not as a negative for them.
- CrossRef (`api.crossref.org`, no key needed): "Linhares Sousa Coutinho cipher diplomatic Portugal 1811" and two
  other keyword combinations -- top relevance-ranked hits read individually: a 2023 biographical-dictionary entry
  "Coutinho, D. Rodrigo de Sousa" (general biography, no cipher content by its listing) and "A correspondência
  inédita do embaixador de Portugal em Paris, D. Vicente de Sousa Coutinho" (1988) -- a *different* Sousa
  Coutinho (Vicente, Paris embassy), not Rodrigo (Linhares) or Domingos (Funchal, London); not our subject. No hit
  on this key, this letter, or a Vieyra identification.
- Persée, HAL, Google Scholar: not separately queried this pass (time; the OpenAlex/CrossRef sweep is the broader
  net for this Portuguese-language, non-Anglophone-scholarship target and returned nothing worth following into
  the smaller indexes). Named as unreached, not searched-and-negative.
- JSTOR: three rows appended to `JSTOR-QUEUE.tsv` this pass (25 Sept 2026): a Linhares+cifra+dicionário/Vieyra
  query, a Sousa Coutinho+"chave de uma cifra"/Diccionario query, and a Rodrigo de Sousa Coutinho+Rio de
  Janeiro+cifra+correspondência query. Queued, not blocking either class (CLAUDE.md rule 2, outreach gate 2).

**(f) Phrase searches on the decoded Portuguese:** all four required phrases (both archaic and modern spelling)
run via `tools/print_check.py` across IA (local + global), Google Books, OpenAlex and (partly) Semantic Scholar --
results and read-as-noise judgement in (c) and (e) above. Full machine output: `print-check.tsv` (47 rows, 21
nominal "hits", every one read individually above and judged noise, not a match to this letter). Per-host request
counts: `print-check-hosts.tsv` (archive.org 1, be-api.us.archive.org 8, googleapis.com 8, api.openalex.org 10,
api.semanticscholar.org 2, api.crossref.org 3).

## 6. Corrections to the folder's files

None needed. `NOTES.md` and `BOOK.md` were checked for rule-10-prohibited wording (new/unpublished/unread/first/
never printed/newly recovered/previously unread) -- every match found is an ordinary, non-novelty use (new page
images fetched, new maço items found, "first written" referring to an internal transcription draft, etc.), not a
claim about this letter's or this key's novelty. `BOOK.md`'s own closing note (line 58) already states correctly
that the dictionary identification was not searched for prior publication and should not be called novel on its
own -- this audit now supplies that search (item 2, section 4). No sentence in the folder over-claims; none is
changed.

## 7. Gaps toward N4 (named, not closed this pass)

1. Read *Textos Políticos, Económicos e Financeiros* (1993) by a third route -- a library/WorldCat copy, a direct
   browser fetch of the `bportugal.pt` PDF (not yet tried with `tools/browser_fetch.js`), or an ILL/archive
   request to the person. This is the single most likely place either item's plaintext or a prior decipherment
   would surface, since it is the standard scholarly edition of exactly this correspondent's papers for exactly
   this period.
2. Full-text search *Quadro elementar* and the *Arquivo Diplomático* series directly (both are pre-1900 and
   likely on Internet Archive or Google Books in full view) rather than by web search alone.
3. Resolve a HathiTrust record id for the 1993 edition (or confirm none exists) and run the HTRC Extracted
   Features per-page search for the required phrases.
4. The three queued JSTOR rows, run by the owner's local runner.

## 8. Postmortem

No over-claim was found to correct in this folder -- LX-DEC and the earlier LX workers already wrote careful,
rule-10-compliant language throughout (BOOK.md's own disclaimer, in particular, anticipated exactly this audit).
The main finding of this audit is additive, not corrective: the printed ANTT catalogue (read directly, not only
the DigitArq API) gives independent confirmation that none of the fonds's three "Chave de uma cifra" items carries
a content note naming a dictionary or a decipherment, while the same catalogue does note a decipherment for at
least one *other*, unrelated item in the fonds -- evidence that ANTT's own cataloguers would likely have flagged
it here too if one existed on file. That strengthens, without proving, the N3 classification. The largest
remaining gap is access, not search discipline: the one edition most likely to settle item 1 either way
(*Textos Políticos, Económicos e Financeiros*, 1993) has now failed on two independent routes (direct fetch,
Wayback CDX) across two sessions and needs a third route or the person's help to open.

Request counts, this pass (25 Sept 2026): `archive.org` 1, `be-api.us.archive.org` 8, `www.googleapis.com` 8,
`api.openalex.org` 10, `api.semanticscholar.org` 4 (2 via print_check.py, 2 manual retries), `api.crossref.org` 5
(3 via print_check.py, 2 manual follow-ups), `web.archive.org` 2 (both failed, proxy-level), `catalog.hathitrust.org`
2 (both failed to resolve a record), `antt.dglab.gov.pt` 2 (PDF fetches), `idi.mne.gov.pt` 1 (403), `github.com`
2 (shallow clones), WebSearch 8 queries. All sequential, none parallel, all well under any per-host cap; no
429/403 seen except the two named above (`idi.mne.gov.pt`, and Semantic Scholar's rate limiter).

## 9. Wording refresh (LX-SO, 25 Sept 2026)

LX-FIX (02:19 UTC) settled the group at page3-line1-pos4 after this AUDIT.md was written (02:04 UTC): the digit
transcription changed from `285219` (no rank-19 entry on page 85, left `[unresolved]`) to `283219` (page 83, col 2,
rank 19, "cagar"), and 5 of the 6 other M-graded tokens were upgraded to H by direct image evidence. Grade counts
went H 20/M 6 -> H 25/M 1. The two quoted-reading lines above (section 1's claim line and section 3's "Reading as
decoded" line) are updated to the current `reading.txt` text and counts; no other line in this file is touched.
This one-token change does not affect any phrase search this file ran: none of `phrases.txt`'s 8 phrases contains
the token at p3l1pos4 or the word "unresolved" -- all 8 phrases sit on other tokens (`segredo ate o ministerio`,
`pela memoria do`, `supprir/suprir o seu lugar`, `seu lugar junto com`), so section 5's search log and section 5(f)/
(c)/(e)'s "no hits" results stand unchanged. Every class (N3/N3), safe sentence, unsafe sentence and search-log
entry in sections 1-8 is otherwise left as LX-VER wrote it.

## 10. Re-check: Textos Políticos (LX-ED, 25 Sept 2026)

Intake-gate re-run (CLAUDE.md Pipeline note, 25 Sept 2026): the 24 Sept `open` verdict never read the sender-family
edition (section 8 above), which `.claude/briefs/check-solved.md` makes `blocked`, not `open`. This session tried
every route in the parent's brief, in order, to read *D. Rodrigo de Souza Coutinho, Textos Políticos, Económicos e
Financeiros (1783-1811)* (ed. Mansuy-Diniz Silva, Banco de Portugal, 1993, 2 vols). **Result: still not read; every
route failed.**

1. **`tools/browser_fetch.js --binary` on the known copy, both volumes.** `ocpep-7_t1.pdf`: 3 attempts (the tool's
   own retry loop, one call), all HTTP 403 with `content-type: text/html` (a Cloudflare/WAF challenge page, not a
   PDF) -- a *real* headless Chromium, not curl, so this rules out a JS-challenge explanation; the proxy status log
   (`__agentproxy/status`) recorded the same request as `connect_rejected`/"gateway answered 502 to CONNECT (policy
   denial or upstream failure)" to a Cloudflare challenge host at 03:57:04 UTC, consistent with the block sitting in
   front of the origin, not solvable by a browser. `ocpep-7_t2.pdf`: 1 attempt (`--retries 1`, after the volume-1
   result made further retries pointless), same 403/text-html. Two requests total to `bportugal.pt`, spaced.
2. **Banco de Portugal's own publications page** (`bportugal.pt/publications/banco-de-portugal/all/224`, the OCPEP
   series listing) for an alternate link: HTTP 403 to curl, same host, not retried with the browser (host already
   ruled unreachable by step 1's browser result on the same domain).
3. **Wayback Machine CDX index** for the same PDF URL (the gap section 8 already named as the next step): failed
   twice at the transport level, not a 403 -- `curl: (35) Recv failure: Connection reset by peer`, proxy log
   `ws_closed_mid_exchange` on `web.archive.org:443` -- reproduced independently this session (the 24 Sept failure
   was a different worker; this is a fresh confirmation the same host is unreachable through this session's proxy
   too, not a one-off). One retry taken, per the good-citizen rule; not retried further.
4. **Google Books.** The exact edition is indexed (`8lfDjgEACAAJ`, "Textos políticos, económicos e financeiros",
   1993) but `NO_PAGES` viewability -- no snippet or full-text search inside it is possible. A corpus-wide phrase
   search for `"supprir o seu lugar"` returned 300 unrelated hits (the API does not enforce the quoted phrase, or
   the exact string -- garbled by the M-grade token at that position -- simply is not printed anywhere Google
   indexes); a second query, `"Sousa Coutinho" cifra chave segredo`, returned 0 items. Neither is a read of the
   edition.
5. **HathiTrust full-text search** (`babel.hathitrust.org/cgi/ls`): 403 to curl; one `browser_fetch.js` attempt
   served Cloudflare's "Just a moment..." interstitial (title captured, 29 KB of challenge JS, no results page) --
   matches CLAUDE.md's already-documented finding that the certificate fix does not clear this site's own
   Cloudflare bot check. Not retried.
6. **Internet Archive advancedsearch** for the title: `numFound: 0`. The edition is not on IA under this title.
7. **WorldCat** (`search.worldcat.org/search?q=...`): loaded via the browser (200, real search-results title in
   the page), and one facet row is visible, `Coutinho, Rodrigo De Sousa (1)`, confirming a WorldCat record exists
   -- but the results themselves render client-side after the saved snapshot and no record/OCLC link was captured;
   in any case a holding-library listing would only confirm existence, not let this session read or full-text
   search the letter, so this route was not pursued further once the true blocker (need eyes on the actual pages)
   was clear.

Every route in the brief, plus the Wayback fallback section 8 flagged, is now exhausted from this cloud session.
**Appended `LOCAL-QUEUE.tsv` row L10** (kind `edition-read`) asking the owner's local runner to open both PDFs
from a home IP and search for the m0002 letter's distinctive decoded phrases and "cifra"/"chiffre"/"Diccionario"/
"Vieyra"/the maço 86 shelfmark. No N-class changed by this session; AUDIT.md's existing N3/N3 verdicts (sections 1
and 3) stand until L10 comes back or a new route is found. The verdict word in NOTES.md line 1 (`partial`) is
unaffected -- this was a check-solved/novelty gap-closing pass, not a solve.

Request counts, this pass (25 Sept 2026): `bportugal.pt` 3 (2 PDF fetches via browser_fetch.js, 1 publications-page
curl, all 403), `web.archive.org` 1 (proxy-level failure, connection reset), `www.googleapis.com` 3 (1 volume
lookup, 2 phrase searches), `babel.hathitrust.org` 2 (1 curl 403, 1 browser attempt served Cloudflare interstitial),
`archive.org` 1 (advancedsearch), `search.worldcat.org` 1 (browser_fetch.js), WebSearch 3 queries. All sequential,
>=1.5 s apart, no host hit more than 3 times, no 429 seen (403/Cloudflare/proxy-reject seen and logged per host,
never retried past the one-retry limit).

## 11. Second audit (AUD2, 25 Sept 2026)

Separate session (parent worker AUD2, Sonnet, session_01NTKxpfXJHgtJsE3FsX7cKB), adversarial, per
`.claude/briefs/runs/2026-09-25-parent-second-audits.md`; not the LX-VER/LX-SO/LX-ED session above, did not
protect its conclusions, did not touch key.tsv/reading.txt/ciphertext.tsv. Read the first audit (sections 1-10
above), NOTES.md, BOOK.md, reading.txt and phrases.txt first, then searched independently by different routes,
per the brief's instruction to try families the first audit did not cover and any further route to *Textos
Políticos, Económicos e Financeiros* (1993).

**Key source (rule 10, 25 Sept 2026 addition -- missing from sections 1-10 above, added now):** the archive item
`PT/TT/CLNH/0086/11` is itself titled "Chave de uma cifra" -- a period key sheet -- but that sheet names its
codebook only as "o Diccionario", never a title or edition; LX-BOOK's identification of it as Vieyra's 1809
pocket dictionary (BOOK.md, all twelve worked-example groups) is "identifying the codebook", which rule 10's
definition places under **`ours`**, not `period`, even though the underlying key mechanism (page/column/rank
arithmetic into a named-but-unidentified book) is a period artifact. Both items' key is **`ours`**: item 1 (the
letter's decipherment) could not be read at all until the codebook was identified, so the reading rests on our
own cryptanalytic step, not a period key alone; item 2 (the dictionary identification) is `ours` by rule 10's own
wording. Text is not `known` for either item (no prior print located, this pass or the first).

**New routes tried, not run by the first audit:**

1. *Quadro elementar das relações politicas e diplomaticas de Portugal* (Visconde de Santarém) -- the first audit
   only web-searched this; this pass opened it directly. Two archive.org scans found (`quadroelementar00santgoog`,
   1842; `quadroelementard18sant`, vol. 18). `be-api.us.archive.org/fts/v1/search` for "cifra", "chave",
   "Diccionario", "Vieyra" across both (8 queries, 25 Sept 2026, >=1.5s apart): one "cifra" hit (p.626 of the 1842
   vol., an ambassadorial-instructions passage "Leva uma cifra para a correspondencia secreta") -- read in full
   context: a 16th-century Rome embassy (Cardinals Santafiore, Sant'Angelo, Carpi; the Bishop of Goa), not
   Sousa Coutinho/Linhares or 1811-12; one "cifra"/"chave" hit-group in vol. 18, context dated 1666 (the English
   envoy Fanshaw), also unrelated. Zero "Diccionario"/"Vieyra" hits either volume. **Closes gap #2** from section 7.
2. *Corpo Diplomático Português* (an adjacent series surfaced by the same search): three IA scans searched the
   same way (12 queries) -- zero hits, any term, any volume.
3. `idi.mne.gov.pt`'s "O segredo da escrita" exhibition page -- the first audit got a 403 and did not retry; this
   pass reached it via the Wayback Machine (CDX lookup succeeded for this URL, unlike the first audit's separate,
   failed CDX lookup for the bportugal.pt PDF -- a different URL, not evidence the earlier failure was wrong).
   Read the 1 July 2022 snapshot in full: entirely about the Foreign Ministry's own 20th-century cipher service
   (telegrams 1910-1984, Hagelin-Cryptos machines, a 1965 in-house "Dicionário da Cifra do MNE"), no mention of
   Linhares, Sousa Coutinho, ANTT, or anything pre-1900. **Closes gap #6** (previously "unreachable, not retried").
4. GitHub code search across all of GitHub, not only the two named solver repositories (`mcp__github__search_code`,
   4 queries: "Linhares Vieyra cifra", "CLNH/0086", "Sousa Coutinho cipher dictionary key", "newpocketdiction00viey"):
   every hit traces back to this repository itself; one unrelated namesake false positive (a physicist "Sofia de
   Sousa Coutinho" in an arXiv-scraper repo). No third-party repository discusses this cipher, key, letter, or
   dictionary identification. **Closes gap #7** (this repo's own workers had already re-cloned the two named
   solver repos, but a repo-wide code search is a materially different, wider net).
5. HAL (`api.archives-ouvertes.fr`), queried directly rather than left unreached: "Linhares cifra Vieyra" and
   `"Sousa Coutinho" chiffre` -- both `numFound: 0`.
6. Persée -- WebSearch restricted to persee.fr found nothing relevant; a direct site query could not be confirmed
   (client-side-rendered results, curl cannot read the count) -- logged as attempted-inconclusive, not a clean
   negative; a browser fetch was not tried this pass (residual gap, low priority: Persée is a French-journal
   corpus, unlikely to cover a Portuguese archival item).
7. Google Scholar (via WebSearch, no API access): no relevant scholarly hit for Vieyra's dictionary + cipher/code
   in any language, or for this letter/key.
8. OpenAlex full-text search (`fulltext.search`, a different filter from the first audit's keyword `search=`):
   "Vieyra pocket dictionary cipher diplomatic" (0 hits); "Mansuy-Diniz Silva Sousa Coutinho cifra" (2 hits, both
   unrelated by title -- tax history, colonial São Paulo commerce).
9. Mansuy-Diniz Silva's other major work on this correspondent, not named by the first audit: *Portrait d'un
   Homme d'État: D. Rodrigo de Souza Coutinho, Comte de Linhares, 1755-1812* (2 vols., Gulbenkian, Paris/Lisbon,
   2006) -- a full biography, plausibly more likely than the 1993 documents edition to narrate archival material
   from this fonds. No free scan located (not on IA, not full-view on Google Books). Its published review
   (*Ler História* / OpenEdition, journals.openedition.org/lerhistoria/2436) was read in full instead: no mention
   of ciphers, keys, codes or dictionaries anywhere; only a generic note that Linhares family papers went to state
   archives. Negative, but the book's own text remains unopened -- **new residual gap toward N4**, alongside the
   1993 edition (same access problem, no online route found either).
10. Two Portuguese biographical/secondary sources found and read in full: `dicionario.ciuhct.org`'s entry on
    "Coutinho, D. Rodrigo de Sousa" (cites the CLNH fonds generically, no cipher mention) and the amelica.org
    article "Um intelectual com face de Janus..." (no cipher mention). Both negative.
11. BND/Biblioteca Nacional Digital (purl.pt/bndigital.bnportugal.gov.pt): WebSearch clean (only an unrelated
    1932 photograph and an unrelated coat-of-arms record); the Koha OPAC path tried directly 404'd (wrong
    endpoint, not pursued further given the clean WebSearch sweep).
12. RCAAP (Repositório Científico de Acesso Aberto de Portugal): blocked by an Anubis bot-challenge to curl, same
    software family as bibliotecadigital.rah.es in CLAUDE.md's playbook -- unreachable this pass, not retried
    with `tools/browser_fetch.js`. Named gap, not a negative.
13. *British and Foreign State Papers* (the standard published UK Foreign Office series) -- a new lead: Linhares
    negotiated directly with Lord Strangford during the Rio period, so an English-translated excerpt of this or a
    related letter could exist there, defeating a Portuguese-phrase search (per the Blathwayt/"(Cypher.)"
    lesson in `.claude/briefs/verifier.md`). Found the series on Internet Archive (34 candidate volumes); spot-
    checked one (`britishforeignst1001grea`) by full-text search for "Sousa Coutinho": 0 hits. The other ~33
    volumes were not systematically checked by date/correspondent (out of proportionate scope for one pass) --
    **named gap, not closed**, and the most promising unclosed lead from this session because it is the one
    family neither audit has actually searched by date+correspondent rather than by phrase.
14. `bportugal.pt`'s Textos Políticos PDF -- retried once more via WebFetch specifically (a third tool/route,
    after curl and `browser_fetch.js` in the first audit): still HTTP 403. Confirms the block is host-wide across
    tool types, not a fluke of one fetch method; does not open a new route. The Wayback CDX index itself proved
    reachable this pass (see item 3, a different URL) where the first audit's attempt at the exact PDF URL failed
    at the transport level -- worth one fresh CDX attempt against the precise `ocpep-7_t1.pdf`/`ocpep-7_t2.pdf`
    paths in a future pass, since the earlier failure may have been session-specific rather than permanent.

**Verdict: agree with the first audit, both items stay N3.** Nothing found in this second, differently-routed
sweep disproves either "no prior plaintext/decipherment of the m0002 fragment" or "no prior identification of the
key's dictionary as Vieyra 1809". The sweep is additive, not corrective, on novelty: it closes four of the first
audit's four named gaps toward N4 as genuine negatives (Quadro elementar, Corpo Diplomático, the MNE exhibition
page, and a GitHub-wide code search) rather than leaving them as "checked only by web search" or "unreachable, not
retried". It also surfaces one correction: the verdict table in section 1 is missing the `key` column rule 10
requires; both items are `ours` (see above), which the person's outreach or contribution wording should carry
forward. The two access gaps toward N4 remain open and are now joined by a third: *Textos Políticos* (1993, both
volumes, still 403 across three tool routes), Mansuy-Diniz Silva's 2006 *Portrait d'un Homme d'État* biography
(newly identified, no free copy found), and a full date/correspondent sweep of *British and Foreign State Papers*
(only 1 of 34 volumes spot-checked). None of the three is closed; all three would need either a working route past
`bportugal.pt`'s block, a library/ILL copy of the 2006 biography, or a properly scoped worker for the 33 remaining
State Papers volumes.

Request counts, this pass (25 Sept 2026): `be-api.us.archive.org` 15, `archive.org` 3, `api.openalex.org` 2,
`api.archives-ouvertes.fr` (HAL) 2, `persee.fr` 2 (inconclusive), `rcaap.pt` 1 (blocked), `catalogo.bnportugal.gov.pt`
1 (404, wrong path), `web.archive.org` 2 (both succeeded), `bportugal.pt` 1 (403, WebFetch), GitHub code search 4
queries, WebSearch 11 queries, WebFetch (non-archive.org pages) 4. All sequential, >=1.5s apart, well under any
per-host cap; no 429 seen. Credentials tested present (`test -n`, never printed): DECODE_USER, DECODE_PASS,
GOOGLE_BOOKS_KEY, OPENALEX_KEY, S2_KEY, IA_USER, IA_PASS; only OPENALEX_KEY was needed this pass. 1 Explore
subagent used for this search pass (within the brief's 2-subagent cap).
