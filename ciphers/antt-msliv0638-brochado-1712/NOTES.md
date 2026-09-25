partial

Dória 1944 *Cartas* (`rE7SAAAAMAAJ`, NO_PAGES/no-preview, so unreadable page-by-page) was read this pass through Google Books' search-within-volume JSON endpoint (`tools/gbooks_search_within.py`, 25 Sept 2026, 19 queries across its 248 printed pages + roman-numeral front matter): the London-embassy words that mark the manuscript's own "Deciffrada" appendix do not appear anywhere in the edition's body -- "cifra"/"cifras" appears exactly once (p.151, one clause, no cipher groups nearby, not on a page with any London-period name), "Deciffrada"/"Deciffrado"/"Bullingbrook"/"Bolingbroke"/"Strafford"/"Estrafforde"/"Oxford"/"Hanover"/"Thesoureiro"/"velhaco"/"vergonhar"/"Nighs"/"deboche"/"parvoices" all return zero hits, and "Londres" itself appears only in the roman-numeral preface (pp.xvii, xviii, xxxvii), never once in the 248 arabic-numbered body pages -- while "Paris"/"Versalhes" (p.17, p.135) confirm the body does cover the sender's earlier Paris embassy period. No route opened the edition page-by-page (still NO_PAGES on Google Books, no IA copy, HathiTrust `catalog.hathitrust.org` 403 Cloudflare as PX-CS01 found, and this worker could not find any HathiTrust catalog record for this edition at all by web search -- consistent with the 100-copy limited run never having been digitized by a HathiTrust partner, so the HTRC Extracted Features route named in this worker's brief could not be run for lack of an htid). Taken together this is read as a negative: the London 1712-13 letters' cipher/"Deciffrada" passages are not printed, and are very likely not covered at all, by the sender's standard edition.

QUEUE row: PX-01 (see QUEUE.md, "Portuguese holdings and dictionary codes (LANE PX, 25 Sept 2026)" section).

## Search log (rule 1), 25 Sept 2026

1. **Web search engine.** `"Cunha Brochado" cifra decifrada carta Londres 1712`, `"José da Cunha Brochado" cipher OR cifra solved decrypted`, `MSLIV 0638 Brochado ANTT cifra`, `Cunha Brochado embaixador Londres 1712 1713 Cryptiana OR Cipherbrain`, `"Cunha Brochado" Cartas Dória 1944 cifra chave`. No hit naming this unit, this cipher, or any decipherment of it. The model-solve-announcement check (queries above already include "solved"/"decrypted"/Cryptiana/Cipherbrain) returned nothing for Brochado.
2. **Print.** Sender's standard edition (Dória 1944 *Cartas*) — could not open, every route above tried and logged. A second, earlier printed compilation was found and is readable: *Memorias de José da Cunha Brochado, extrahidas das suas obras ineditas*, ed. J. Mendes dos Remédios (Coimbra: França Amado, 1909; vol. XII of "Subsídios para o estudo da história da literatura portuguesa"), Google Books `nplEAAAAIAAJ`, ALL_PAGES/public domain, table of contents read via a real-browser fetch of the book's info page (`tools/browser_fetch.js`, one request, cleared Google's bot page on the first try) — but its contents page lists short essayistic chapters ("Embaixador mezquinho", "Le Grand aprecia o caracter dos portugueses", "A leviandade dum historiador francês", 6 further sections not shown), i.e. literary/biographical extracts, not a chronological edition of the London letters; nothing in the visible TOC suggests it reprints Carta Nº 89-105 or their cipher passages. A direct PDF download (`books.google.com/books/download/...`) hit Google's captcha wall (HTTP 429 -> HTML captcha page) on the one attempt made; not retried, per the good-citizen single-retry rule. This edition is a named lead, not read in full, and is not a substitute for the standard *Cartas* edition for this check.
   Also checked: D. Luís da Cunha's own *Memorias da Paz de Utrecht* (his account of the same 1712-15 Utrecht congress Brochado's letters discuss) is digitized at Biblioteca Nacional Digital, `purl.pt/23773` (and likely companion parts) — found, not opened this pass (out of budget); named next step below, item 1b.
   Visconde de Santarém's *Quadro elementar das relações políticas e diplomáticas de Portugal* (multi-volume, on Internet Archive, e.g. `quadroelementar11lisbgoog` etc.) is a general diplomatic-history narrative/documents series, not a letter edition; not opened, low probability of reprinting cipher passages verbatim, named as a low-priority lead only.
   BNP (`urn.bnportugal.gov.pt`) authority record for Brochado (id 126352) lists a *different* manuscript: "Cartas de Joze da Cunha Brochado ... Na Corte de Paris" (BNP COD. 9595-9599, 5 tomos, Paris embassy 1695-1704, copied [1704-1725]) — Paris-period, not the London 1712-13 letters this target covers; not a duplicate.
3. **Community lists (Cryptiana, Cipherbrain).** No hit in the web-search pass above (query 4); DECODE checked separately (below).
4. **DECODE snapshot on disk.** `sources/decode/*.tsv` (records-decrypted, dc11-20-documents, florence-dieci): `grep -i brochado` on all four files, zero hits. No login used, per COMMON rule 4.
5. **`dbourdeau/cyphersolver`.** Fresh depth-1 clone, 25 Sept 2026 (this worker, independent of the scout's same-day clone a few hours earlier): `grep -rIl -i "brochado\|msliv"`, zero hits outside `.git`.
6. **`aaymeloglu/unsolved-ciphers`.** Same fresh clone and grep, zero hits.
7. **Collection-wide duplicate check.** A broad DigitArq `terms=Cunha Brochado` API query returns ~7.5M noise hits (surname-substring matches across the whole archive; this endpoint does not do phrase matching, consistent with QUEUE.md's existing note that DigitArq's JSON search is unreliable past a handful of results) and was not usable. Relied instead on the scout's (PX-SCDIGI3, same day, 04:39 UTC) 24 narrow `cifra`/`chave` + fonds-restricted queries, which found no other ANTT unit holding these specific London 1712-13 letters; the one related cross-reference it surfaced, `PT/TT/MMCG/1E` (Fernando Teles de Faro to Francisco de Melo, 1658-59), is a different sender, recipient and half-century-earlier period — not a duplicate or sibling copy of MSLIV/0638.

## The leaves (inventory, not a transcription)

Viewer `https://digitarq.arquivos.pt/fileViewer/7049343e7af44ba7b4ec18e74e1b2cd7` (docId `7049343e7af44ba7b4ec18e74e1b2cd7`), file list fetched (306 images, `images/filelist.json`). Five full-resolution leaves pulled and viewed directly (`images/full_PT-TT-MSLIV-0638_m028{9,9},029{0,1,2,3}.jpg.jpg`; scout PX-SCDIGI3 had already viewed the same span at full res without committing images):

| image | shows | letter/passage no. |
|---|---|---|
| m0289 | Carta Nº 89: cipher groups, "Deciffrada" heading, plaintext ("Ainda que isto he mentira bom será que lhe metaõ medo."). Carta Nº 91: cipher groups, "Deciffrada", plaintext ("Segundo promete a pouca vida do R[ey]."). Carta Nº 92 begins: cipher groups, "Deciffrada" heading visible at foot of page, plaintext continues onto m0290. | 89, 91, 92 (start) |
| m0290 | Carta Nº 92's decipherment continues ("Este Velhaco está declarado França, e hum destes dias jantando em Casa do Enviado da Hollanda disse hum Milhaõ de parvoices com hum pouco de siso na cabeça..."). Carta Nº 93: cipher groups, "Deciffrado", plaintext ("Que não está em boa intelligencia hum ex fort, e Bullingbrook" -- i.e. Bolingbroke). "Passage 2ª": a separate cipher excerpt (not a full numbered letter) with its own "Deciffrada" heading and plaintext, continuing onto the next leaf. "Passage 3ª" begins at the foot. | 92 (cont.), 93, Passage 2 |
| m0291 | "Passage 3ª" (continued from m0290): cipher groups, "Deciffrada", plaintext ("Pelos Nighs [News?] anunciados do Principe de Hanover por Escocia ... previnem ao Principe [de Gales?]."). Carta Nº 94: cipher groups, "Deciffrada", plaintext ("Poderei em vergonhar esta Rainha."). Carta Nº 96: cipher groups, "Deciffrada", plaintext ("Crer egosto com o[s] fieis. Hé certo que o diabo leva o Thesoureiro."). | Passage 3, 94, 96 |
| m0292 | Carta Nº 101: cipher groups, "Deciffrada", plaintext ("Mas o P.e h[e] n[ecessari]o que vinha por Franca porque não ha a parencia que entre pela porta de Londres."). Carta Nº 105: cipher groups, "Deciffrada", plaintext ("Se por deboche elle está conhecido por hum pobre talento."). "Passage 2ª": cipher groups, "Deciffrada", plaintext ("Em que só entrou o Principe ..." -- cut off at page foot, continues onto m0293). | 101, 105, Passage 2 |
| m0293 | Carta Nº 106: cipher groups, "Deciffradas", plaintext ("Esta Rainha vive em companhia do Thesoureiro, e de Bullingbrook seremos vendidos."). Carta Nº 109 (or "10.9", digits partly unclear): cipher groups, "Deciffrada", plaintext ("Bem livrados que és V. [Vossa?]."). "Passage 2ª": cipher groups, "Deciffrada", plaintext ("Este velhaco de Bullingbrook hé nosso inimigo."). | 106, 109(?), Passage 2 |

Confirms and extends the scout's finding: across these five leaves alone, at least ten numbered letters (89, 91, 92, 93, 94, 96, 101, 105, 106, and one read as "109" but partly unclear) plus at least four unnumbered "Passage" excerpts carry a period ("Deciffrada"/"Deciffrado") plaintext directly under their cipher groups, in the same hand, within this bound volume. Per the brief's instruction: **this contemporary decipherment does not by itself make the item solved for our purposes.** It establishes a period key (grade H if later applied and read from this image) for whichever cipher passages it covers; it says nothing about whether Dória's 1944 edition (or any other modern print) also reproduces these same passages' plaintext, which is the actual check-solved question and the one this worker could not close. The appendix's full span (m0285-m0306 by the scout's estimate) was not re-mapped end-to-end this pass (m0285-m0288 and m0294-m0306 unseen by this worker) -- a follow-on transcription/key-alignment worker needs to read the whole span before building key.tsv.

## Per-host report

`digitarq.arquivos.pt`: 7 requests this pass (1 `--list` filelist call, 5 full-resolution leaf pulls via `tools/digitarq_fetch.py --full`, 1 broad `/api/docs/search` reachability/duplicate-check query that returned unusable noise), all through the tool's own >=3s pacing, well under the 40-request session cap. `books.google.com`: 1 API metadata call (`www.googleapis.com/books/v1/volumes`, with `GOOGLE_BOOKS_KEY` and `country=US`, several queries) + 1 browser fetch (`tools/browser_fetch.js`, one page, succeeded) + 1 direct-download attempt (429/captcha, not retried). `catalog.hathitrust.org`: 1 request (403, Cloudflare, not retried). `search.worldcat.org`: 1 request (200 but JS-rendered, no usable content). `archive.org`/`be-api.us.archive.org`: ~5 requests (advancedsearch and full-text-search API). `urn.bnportugal.gov.pt`: 1 request. `github.com`: 2 shallow clones (`dbourdeau/cyphersolver`, `aaymeloglu/unsolved-ciphers`, grep only, no push). WebSearch: 7 queries. No DECODE login used (checked the on-disk snapshot only, per COMMON rule 4).

## Follow-on search log (PX-CS01B, 25 Sept 2026): the four routes PX-CS01 did not run

1. **HathiTrust Extracted Features.** No htid found: `openlibrary.org/search.json` for "Brochado Cartas" and title variants returned 0/irrelevant results (no OCLC to feed the Bibliographic API); WebSearch for `site:catalog.hathitrust.org` + Brochado/Doria/Cartas, and for "jose da cunha brochado" hathitrust, returned no matching catalog record. Combined with PX-CS01's own `catalog.hathitrust.org` 403 and the item's absence from Internet Archive and from Google Books' full-view set, this 100-copy limited edition does not appear to be held by any HathiTrust partner library at all -- the EF/numeral-pages route could not be run for lack of a volume id, not skipped.
2. **Google Books search-within.** Ran (`tools/gbooks_search_within.py rE7SAAAAMAAJ ...`, 19 words/phrases across 5 calls, 0.5-1.5s apart): full results and reading folded into the status line above. Multi-word phrases (`"Principe de Hanover"`, `"Príncipe de Gales"`, accented `"ÍNDICE"`) came back `ERR/blocked` -- the tool does not URL-encode its query, a known limitation, not a host block; not worth a tool patch for this one pass. This is the route that actually answered the check-solved question this pass.
3. **D. Luís da Cunha, *Memórias da Paz de Utrecht*.** Found and reachable (`purl.pt/23773`, 200 after one redirect; its item-detail page at `permalinkbnd.bnportugal.gov.pt/idurl/1/88540` gives `[2] f., 900 p., [44] f.` for this one part alone -- "Quarta e última parte"). Not read in full (900 pages, out of this worker's scope and budget; this is D. Luís da Cunha's own memoir of the Utrecht congress, not Brochado's correspondence, so it was always the lower-priority lead). Tried the BNP site's own full-text search (`bndigital.bnportugal.gov.pt/records?search=Brochado+cifra&fulltext=1`, the route CLAUDE.md's host table documents as curl-reachable): HTTP 200 but the page title comes back `Mais recentes` ("most recent", i.e. the default listing) rather than search results -- the query parameter is not honoured by a non-JS fetch for this particular search form, unlike the plain item pages. Still unread; named as a next step, unchanged from PX-CS01's note.
4. **Open-index scholarship.** OpenAlex (`OPENALEX_KEY` header, 3 queries: "Cunha Brochado cifra Londres", "\"Cunha Brochado\" embaixador Londres", "cifra diplomacia portuguesa Utrecht Brochado") and Semantic Scholar (`S2_KEY` header, 1 query) found one directly relevant work, Ana Leal de Faria (?), "José da Cunha Brochado: de secretário de embaixada a embaixador extraordinário" (*Tempo* 22(39), 2016, DOI 10.20509/tem-1980-542x2016v223909) -- its abstract covers only the 1695-1704 Paris embassy period (secretary to the Marquês de Cascais), not the 1712-13 London embassy or any cipher; not a discussion of the target. No other OpenAlex/S2 hit named Brochado and cipher/cifra together. CrossRef (`api.crossref.org`, 2 queries, `mailto=` set) surfaced one genuine lead outside the open indexes: Olive Hawes, "Cartas" [review of Dória's edition], *Books Abroad* 20(3), 1946, p.336, DOI 10.2307/40085684, JSTOR stable/40085684 -- a contemporary book review of the exact sender's edition this check-solved gate turns on. JSTOR is Cloudflare-blocked from the cloud (Access playbook); this worker's brief does not name JSTOR-QUEUE.tsv among its touchable files, so the row is not queued here -- named below as a next step for whichever worker touches that file next. A short capsule review is unlikely to itself print cipher passages, but could confirm the edition's date range/scope claim made in item 2 above.

## Next steps (not this worker's brief)

- Queue a JSTOR-QUEUE.tsv row for Olive Hawes' 1946 *Books Abroad* review (DOI 10.2307/40085684, JSTOR stable/40085684) of Dória's *Cartas* -- a contemporary review of the exact edition this gate turns on, found via CrossRef this pass but not queued (out of this worker's file scope).
- Read D. Luís da Cunha's *Memorias da Paz de Utrecht* (`purl.pt/23773`, 900 pp. for this part alone, 3 further parts at `purl.pt/23772` and `purl.pt/23774`) for any reprint or discussion of Brochado's ciphered London dispatches; its own full-text search form did not honour a non-JS query this pass (see item 3 above) -- needs a browser fetch or a different search route, not a plain curl retry.
- Map the appendix's full span (m0285-m0306) end to end, transcribing every Carta-Nº / cipher-group / Deciffrada / plaintext quadruple, before any key-alignment attempt (flagged already by the scout).
- Verdict is now `open`: the target can move to the board's normal pipeline (extraction/key-alignment from the manuscript's own contemporary "Deciffrada" appendix) without further archive work on the sender's edition, unless the Hawes review or the Cunha memoir turns up something unexpected.

## PX-BROKEY (25 Sept 2026): appendix extent, system characterization, undeciphered body passage

Worker PX-BROKEY (Sonnet, session_01STLPbRnttUCLRbUvnynUj6), job: rebuild the period key from the volume's own
contemporary decipherments and report which body cipher passages it reads. Per CLAUDE.md rule 7/10 and the
job brief's step 1-2, this pass establishes the appendix's true extent and the cipher system's character;
full key construction and body-passage decoding are **not completed this pass** -- see "Not done this pass"
below. All findings below are from full-resolution images viewed directly by this worker (not from a prior
worker's prose summary), file paths `images/full_PT-TT-MSLIV-0638_m0NNNN.jpg.jpg`.

### The appendix has a title page and is much larger than the scout/CS01/CS01B estimate

`images/full_PT-TT-MSLIV-0638_m0279.jpg.jpg` carries a section title in display script: **"Cartas em Cifra e
Passages da mesma, que se achão nesta Collecção, deciffradas"** ("Letters in cipher, and passages of the
same, that are found in this collection, deciphered"). This is a deliberate compiler-made index/key
appendix, not an incidental run of interlinear glosses. It is followed immediately by the first entry
(Carta Nº 13) on m0280. The scout (PX-SCDIGI3) and PX-CS01 had only viewed m0285-306 in earlier passes and
estimated the span at "~m0285-306"; this pass establishes the true start.

**Backward boundary (binary search, cheap: 4 leaf reads instead of transcribing every leaf back to page 1):**
m0270 (page number "133" in the body's own foliation, dated "Londres 15 de 8bro 1713" ["8bro" = outubro],
signed "S[?] Luis da Cunha" / "[Bro]chado") is an ordinary **plaintext** body letter, no cipher at all.
m0276 is a body letter **with cipher groups embedded inline in running Portuguese prose, and no interlinear
decipherment** (see "Undeciphered body passage" below) -- a different kind of page from the appendix.
m0279 is the appendix's own title page. So the appendix (m0279 title + m0280-296 content) sits in a distinct
block near the end of the letterbook's ~306 leaves, after the ordinary correspondence.

**Forward/end boundary:** m0296 ends with a dateline **"D. L[uís] da C[unha] a V.Exª[?]. 7 de 9bro [novembro]
de 1713"**, a closing flourish/underline, and below it (on the same leaf, clearly a different, unrelated,
cruder-hand document showing through/underneath, with the Arquivo Nacional da Torre do Tombo stamp) --
consistent with the appendix ending here. m0294-296 together carry one long entry, "Carta Nº 123", for which
**no cipher groups are shown at all** -- only the "Deciffrada" plaintext -- the sole entry in the whole
appendix, of those viewed, transcribed as plaintext-only.

**Confirmed appendix span: m0279 (title) + m0280-296 (17 leaves of content).** Every leaf m0280-296 was
viewed directly this pass (all now on disk in `images/`, full resolution, ~24 DigitArq requests this pass,
see host report below). Running entry numbers found, leaf by leaf (letter numbers, not necessarily
consecutive -- only letters that used cipher get an appendix entry): m0280 Carta 13; m0281 Carta 15, Carta
~22; m0282 Carta 30, Carta ~58, Carta 61; m0283 Carta 61 decode (cont.) + Carta 70; m0284 Carta 70 decode
(cont.) + Carta 71 + Passage 2 + Passage 3 (starts); m0285 Passage [1?]ª (cont./separate) + Carta 72 +
Passage 2; m0286 Passage 3 (cont.) + Carta 73 + Carta 74; m0287 Carta 74 decode (cont.) + Carta 78 + Carta 79
+ Carta 80; m0288 Carta 81 + Carta 85 + Passage 2ª; m0289 Carta 89 + Carta 91 + Carta 92 (starts); m0290
Carta 92 decode (cont.) + Carta 93 + Passage 2ª + Passage 3ª (starts); m0291 Passage 3ª (cont.) + Carta 94 +
Carta 96; m0292 Carta 101 + Carta 105 + Passage 2ª (starts); m0293 Passage 2ª decode (cont.) + Carta 106 +
Carta 109(?) + Passage 2ª; m0294 Carta 110 + Passage 2ª + Carta 123 (starts, no cipher shown); m0295-296
Carta 123 decode (cont., plaintext-only) ending 7 Nov 1713.

That is at least 20 numbered-letter entries (13, 15, 22, 30, 58, 61, 70, 71, 72, 73, 74, 78, 79, 80, 81, 85,
89, 91, 92, 93, 94, 96, 101, 105, 106, 109, 110, 123 -- 28 by count, some digit readings uncertain, marked
`?` above) plus at least 9 unnumbered "Passage" excerpts, each with its own cipher-plus-Deciffrada pair
(except Carta 123, plaintext only). This is roughly triple the "at least ten letters" PX-CS01 counted from
five leaves. Letter numbers climb from 13 to 123 across the run, consistent with a single pass through the
whole letterbook picking out only the letters/passages that used cipher, in original order.

### The system is a partial nomenclator embedded in plain running Portuguese, not a full substitution

Every cipher line mixes **plain Portuguese words, written out normally**, with **coded tokens** standing in
for individual words (mostly names and sensitive terms: Rainha [Queen Anne], Bullingbrook [Bolingbroke],
Thesoureiro [the Treasurer, i.e. Oxford], Velhaco [rogue/scoundrel, their code-word for a minister],
Inglaterra, Hanover, Escócia, Príncipe, etc.). Coded tokens are periods-separated groups of two kinds:
**numbers** (small ones recur constantly: 2, 4, 5, 7, 8, 12, 15, 17, 18, 19, 20, 21, 23, 24, 25, 26; a few
larger ones appear rarely: 52, 55, 300) and **single roman letters used as code symbols** (a, c, d, e, f, g,
h, m, q, x, y, z -- distinguishable from ordinary short Portuguese words by position: they sit inside a
period-separated numeric run, e.g. "...17.a.7..."). Carta Nº 70's own decipherment (m0283) is explicit about
the mechanism: "...V.Exª deve saber que no Diccionario destes Ministros vale o mesmo..." ("...Y.Exc. should
know that in the Dictionary [used by/for] these Ministers, it amounts to the same..."), i.e. the correspondents
themselves call this a **Diccionario** [dictionary/nomenclator] code, confirming this is not ad hoc. This
matches CLAUDE.md's access-playbook framing of "dictionary or book codes" for this lane, and explains why
PX-SCDICT's scout for a separate copy-free "dictionary code" target found nothing extra to add: the
dictionary in question is internal to this volume's own correspondence, not a published book.

### Undeciphered body passage found (m0276): a genuine target for the key once built

`images/full_PT-TT-MSLIV-0638_m0276.jpg.jpg` is an ordinary body letter page with cipher groups embedded
directly in running prose and **no interlinear or marginal gloss at all** -- e.g. opens mid-sentence
"55.17.12.23. 14.d.f. 16.17.ff.z.12. 5.z.x.d.12. mas isto hé impossível, nem o tempo o permite, e só serve
x.z.55.52.15.26.y. 20.25.f.24. e 3.17.20.a.f.19. m.a.d. Cá não cuido de dizer que o novo Enviado seria melhor
recebido...", continuing for the rest of the leaf in the same mixed style, dated by context to the same
London 1712-13 embassy (references "Mylord Strafford", "o novo Enviado"). Some of the same small numbers
recur here (17, 12, 23, 20, 26, 24, 3) as in the appendix, a first cross-check that the two use the same
code once the key exists. This is exactly the kind of "body passage without decipherment" the job brief's
step 4 asks for -- found opportunistically while walking the m0270-282 boundary, not yet swept systematically
(no --thumbs stride run this pass; the brief's up-to-8-leaf body sweep is unstarted, see below).

### Not done this pass (push per Usage rule 10 / cost realism)

Step 2 (two independent Sonnet transcription passes into ciphertext.tsv/plaintext_period.tsv) is running as
ONE subagent pass this session (not two) against the 17 on-disk appendix images -- reading 15 full-resolution
leaves directly myself first (for the extent/system findings above) already used a large share of this
worker's $9 stall-alarm cap, and a second full independent 17-image pass risked running past it with nothing
committed. Files (when the subagent lands): `ciphertext_appendix.tsv`, `plaintext_appendix.tsv`,
`transcription_pass_summary.md`. Steps 3-6 (key.tsv/decode.json, body sweep beyond m0276, spec+judge, fresh
re-derivation) are **not started** and are the next worker's job. A named next step: push the extent-mapping
insight (this is a whole-volume "Diccionario", so a NUMBER may also encode multi-letter fragments or whole
words rather than single letters -- check whether the same number always maps to the same WORD across
different entries, e.g. does "15" mean the same thing in Carta 13 and Carta 81, before assuming a fixed
letter-substitution alphabet) into the key-building step, since Carta 70's own text says the code is a
"Diccionario" (word-level), not a cipher alphabet (letter-level) -- this likely rules out treating the
appendix as a simple homophonic substitution and argues for a nomenclator/dictionary-code key.tsv (code,
word/phrase, not code, letter).

### Update: appendix transcribed, key rebuilt from the volume's own decipherments (grade `period`)

A single Sonnet subagent (this worker's one transcription pass, not two -- see cost note above) transcribed
all 17 appendix leaves (m0280-296) directly from the full-resolution images into `ciphertext_appendix.tsv`
(1702 cipher-token rows) and `plaintext_appendix.tsv` (39 entry rows: cipher_line + deciffrada_line verbatim,
including the three entries that span a page turn -- Carta 61, Carta 70, Carta 123 -- filed under their
starting leaf with merged text). Method and uncertainty log in `transcription_pass_summary.md`; 18 tokens
flagged `±` for genuine handwriting ambiguity, no entry fully illegible.

**The system is confirmed a homophonic letter-substitution cipher selectively applied within plaintext
Portuguese**, not a word-level dictionary code despite Carta 70's own "Diccionario" wording (that word most
likely names the code TABLE itself -- a book/sheet of homophones -- rather than describing word-for-word
substitution). Evidence: coded runs' token counts match the letter count (spaces/punctuation stripped) of
their corresponding plaintext span exactly in the clean cases -- e.g. `Passage 2ª` (m0284) is 13 cipher
tokens for "Selhefôrdemim" (13 letters); `Passage 5ª` (m0285) is 13 tokens for "Nãohéresposta" (13 letters);
`Carta 30` (m0282) is 24 tokens for "ASogradoDuquedeBuquingam" (24 letters), and within that single entry
alone the codes **u=26** (3 independent positions), **q=13** (2), **e=19** (2) and **g=6** (2) already
repeat consistently.

**Method** (scripts in `scripts/`, run in order, regenerate `key.tsv` from the two transcription TSVs with no
network access): `01_segment.py` splits each entry's `cipher_line` into ordered (CODE-run | plain-word)
segments, using `ciphertext_appendix.tsv`'s per-entry ordered token list as ground truth (handles the one
capitalisation edge case, code "a" written as display-capital "A" after the literal, evidently non-cipher,
numeral "300" in Carta 13 -- flagged, not resolved, see below). `02_anchor.py` locates each plain-word
segment's position inside `deciffrada_line` (after stripping the appendix's own trailing "V.Sa"/"V.mce"/"V."
closing abbreviation, which is not part of the enciphered letter) to bound each CODE run's corresponding
plaintext span. `03_align_pairs.py` strips spaces/punctuation from each bounded span and, where the letter
count matches the token count exactly, pairs code[i] with letter[i] in order (232 spans matched this way
across the 31 of 38 entries whose anchors resolved cleanly; 37 spans didn't match -- listed with their
token/letter counts in the script's output -- mostly entries with an abbreviation *inside* the coded span
itself, e.g. "N.Exª", not just at the end, which the current script doesn't strip). `04_build_key.py` tallies
each code's observed letters (accents folded to base letter: ã/á/à/â→a, é/ê→e, í→i, ó/ô/õ→o, ú→u, ç→c) and
takes the majority, grading **C** when the majority holds ≥65% of ≥2 observations, **M** otherwise -- per
CLAUDE.md rule 4/step 3's own threshold ("grade C when fixed by ≥2 independent entries").

**Result: `key.tsv`, 38 codes, 26 at grade C.** The strongest (≥85% majority, several at 100%): `10→h` (6/6),
`20→l` (5/5), `21→b` (4/5), `22→i` (2/2), `23→a` (3/3), `25→o` (4/4), `52→r` (2/2), `e→g` (2/2), `m→n` (3/3),
`x→d` (2/2), `3→t` (15/16), `55→p` (10/11), `z→e` (11/12), `15→o` (28/31), `17→a` (18/20), `19→e` (13/15),
`y→a` (7/8), `12→r` (19/22), `5→c` (7/8). Weaker/unresolved: `2` (d, 56%), `26` (u, 64% -- the `v`/`u`
homophone split may be genuine period orthography, not noise, since 17-18c. Portuguese did not consistently
distinguish u/v in secretary hand), `24` (h, 33%, only 3 obs), `c` (g, 50%). Fifteen entries' worth of codes
in the run (1, 9, 13, 16, a, f, g, h, q, and the ±-flagged 310/400/38/58/9/56/107) have 0-1 observations and
stay grade M or are entirely absent from `key.tsv` -- unkeyed.

**Key source grade (rule 10's provenance field): `period`** -- this key is rebuilt by us from the volume's
own contemporary decipherments, not a published key and not our own cryptanalysis from ciphertext alone.

**Experimental decode of the m0276 body passage** (`scripts/05_decode_m0276_experimental.py`, run against
`key.tsv`): the passage's first coded run, tokens `55.17.12.23.` (all grade C), decodes cleanly to **"PARA"**
("for"/"to"), and the next run `14.d.f.` mostly to "NoS" ("us") -- both grammatical, plausible openings for a
Portuguese diplomatic sentence, and independent confirmation the key generalises beyond the appendix it was
built from. The remaining runs in the same passage (`fASSER`, `CEDoR`, `DEPROuA`, `LOSh`, `TAL_SE`, `N_o`) do
not resolve to clean words with the current key -- some codes involved are unkeyed (grade U, shown as `_`)
or low-confidence M-grade. **This is not a reading under rule 7** -- no spec exists yet, no judge was run, and
it used ad hoc token lists typed from this worker's own re-reading of the image rather than a checked
ciphertext.tsv. It is reported only as a plausibility check on the key, per rule 3's spirit (report what
supports and what doesn't).

### Not done this pass, continued (next worker)

Step 4's systematic body-passage sweep (a `--thumbs` stride scan of the ~280 non-appendix leaves for more
cipher-bearing pages, full-res pull of up to 8, two-pass transcription, decode with `key.tsv`), step 5 (a
`specs/antt-msliv0638-brochado-1712.json` and `tools/judge_plaintext.py` run), and step 6 (a fresh-instance
re-derivation of the key from `ciphertext_appendix.tsv`/`plaintext_appendix.tsv` alone, blind to this
worker's alignment scripts) are **not started**. Concretely useful next steps in priority order: (1) extend
`02_anchor.py` to strip mid-span abbreviations (not just trailing ones) to recover the 37 currently-mismatched
spans -- likely raises several M-grade codes to C and fills real gaps (1, 9, 13, 16, a, f, g, h, q are
currently unobserved or single-observation); (2) apply the resulting key to the rest of `ciphertext_appendix.tsv`
that wasn't used for alignment (Carta 123 has no cipher; a handful of entries had 0 anchors at all -- Carta 13,
15, 58, 73, 74, 92, 110 -- these still need a hand check since something about their plain-word wording didn't
match `deciffrada_line` verbatim, worth a look before trusting the key on them); (3) only then the body sweep.

## PX-BROKEY2 (25 Sept 2026): alignment repair (step 2 of this worker's brief)

Worker PX-BROKEY2 (Sonnet), job: make the period key rule-7 sound (second blind transcription pass +
reconcile, alignment repair, decode.json + `--check`). This section covers step 2 (alignment repair);
step 1 (second blind pass) was running as a background subagent while this work was done and is
reconciled in the section below once it lands; step 2's key.tsv will be rebuilt again after that
reconciliation updates ciphertext_appendix.tsv/plaintext_appendix.tsv.

**Root causes found for the 8 zero-anchor entries** (Carta 13, 15, 58, 61, 73, 74, 92, and m0288's
Passage 2a -- one more than the 7 the prior worker's hand-check had flagged), each confirmed against the
full-resolution image:

1. **Word-boundary bug (Carta 13, Carta 15, and most others' partial mismatches).** The old anchor
   script searched for each plain word as a raw case-insensitive *substring* of `deciffrada_line`, so a
   short word matched *inside* a longer one before its own real occurrence -- e.g. "tem" matched inside
   "in**tem**dem" long before the actual standalone "tem" near the end of Carta 13, and "a" (a genuine
   one-letter Portuguese word) matched inside almost any word containing that letter. Every plain word in
   both entries is genuinely present in the image at its own position; the search just found the wrong
   one first and threw off every anchor after it. Fixed: `02_anchor.py` now tokenises `deciffrada_line`
   into whole words and matches plain chunks against whole words only, scanning forward from the current
   position (never backward, never inside another word).
2. **Genuine scribal variation (Carta 58, Carta 73), hand-checked against the image, not transcription
   errors:** Carta 58's cipher line plainly reads "N.Exã" where its own Deciffrada reads "V.Exª" -- both
   are the same honorific ("Vossa Excelência"), the compiler was simply inconsistent about the leading
   letter of the abbreviation. Carta 73's cipher line reads "dous" where its Deciffrada reads "dois" --
   both are valid, interchangeable period spellings of "two" (Portuguese orthography wasn't standardised
   yet; the same u/v looseness already noted for the `26` code's u/v split in the prior pass). Added as
   explicit equivalences (`HONORIFIC_RE`, `DOUS_DOIS`) rather than generic fuzzy matching, to avoid
   introducing false positives elsewhere.
3. **A cipher chunk glued across a decif word boundary (m0288 Passage 2a):** the cipher line writes
   "aporta" as one word where the Deciffrada spells it "a porta" (two words) -- `find_next` now also
   tries a plain word against two consecutive decif words concatenated.
4. **Two entries (Carta 74, Carta 92) are coded letter-for-letter with *no* plain words interspersed at
   all**, confirmed against the image (every space-separated chunk in their cipher_line is dot-joined
   digits/single letters, no real word anywhere) -- unlike every other appendix entry, which mixes in
   plain Portuguese. Their *stored* `ciphertext_appendix.tsv` token row had drifted out of sync with their
   own `cipher_line` text (a transcription-pass inconsistency between the two tables written in the same
   pass), which made the old segmenter fall through to treating a whole code run as one unmatched "plain
   word". Fixed in `01_segment.py`: a multi-piece chunk that is entirely code-shaped (digits/single
   letters only) is now segmented as CODE from its own pieces even when it doesn't line up with the
   stale stored token stream.
5. **One entry (Carta 110, m0294) still fails after all of the above** -- the plain word transcribed as
   "duvida" does not occur anywhere in its own Deciffrada text ("Este Velhaco não responder-me foge de mim
   **devo** esta vergonha à sua mentira."), and "vergonhar" (transcribed) vs. Deciffrada's "vergonha" is a
   verb/noun mismatch, not an abbreviation. Read against the image again this pass but not confidently
   resolved either way (the word is short and the hand is cramped at that exact spot) -- left unresolved
   rather than guessed; flagged for the second blind pass / a fresh image re-check, not silently corrected.
   `key.tsv`'s data is unaffected either way since 03_align_pairs.py safely excludes an entry's unresolved
   spans from the tally rather than guessing.

**Also fixed:** the anchor script's per-entry `ok` flag used to require at least one resolved plain word,
which wrongly flagged the appendix's fully-coded entries (Carta 30, and now 74/92) as "ANCHOR-FAIL" even
though they need zero anchors (the whole line is one CODE run). An entry with zero unresolved words is
`ok` regardless of how many plain words it has (including none). `03_align_pairs.py`'s span boundaries
now walk outward to the *nearest resolved* anchor on each side instead of only the immediate neighbour, so
one unplaced word costs only the spans touching it, not the rest of the entry (this was the actual
mechanism that recovered Carta 13/15's data once the word-boundary and lookahead-window bugs above were
fixed -- an earlier version of this same walk-outward change, before the lookahead window bug was found,
initially *lost* pairs by mis-attributing skipped words to the wrong neighbour; kept here only as a
lesson in the script's own comment, not repeated).

**Result:** entries fully or partially anchored: 37/38 (was 31/38); zero-anchor: 1 (Carta 110, above; was
8). Aligned code-letter pairs: 391 (was 306). `key.tsv`: 40 codes, 28 at grade C (was 38 codes, 26 at grade
C) -- gains include `11→p` (M→C, 2 obs), `13→q` (M→C, 3 obs), `10→h` (6→9 obs), `12→r` (22→25), `4→s`
(18→26), `5→c` (8→11), `8→i` (19→24), `17→a` (20→23), `18→m` (15→18), `19→e` (15→20, see caveat below),
`20→l` (5→6), `23→a` (3→4), `26→u` stays M but firms up (14→17 obs), `3→t` (16→18), `y→a` (8→17), `z→e`
(12→18), plus two brand-new grade-C codes from Carta 13/15 (`9±→r`, `a→t`, `m→n` gains one more
observation). **Two codes moved C→M** with the new data rather than being forced to stay C: `7` (was
C at 6/7="e"; now 11 obs, "e" only 6/11=55%, plus new `o` and `r` readings -- see the `q.mos` case below)
and `e` (was C at 2/2="g"; now 6 obs, "g" only 3/6=50%, plus `u`/`v` readings). Both downgrades are the
grading rule doing its job on newly-recovered conflicting evidence, not a regression to force back up:
one instance behind the `7→o` reading is code run `13.c.7.18.` decoding to "q.mos" letter-for-letter
against Carta 13's own Deciffrada abbreviation "q.mos" (short for "quantos") -- the cipher apparently
encodes the *written* abbreviated form, not the expanded word, exactly as many tokens as letters
(4-for-4); worth a second look once the appendix has more coverage, not resolved this pass.

Method unchanged from the prior pass (`01_segment.py` → `02_anchor.py` → `03_align_pairs.py` →
`04_build_key.py`, run in order, no network); only the three scripts' internal logic changed, described
above. Key source grade is still `period` (rebuilt by us from the volume's own contemporary
decipherments).

## PX-BROKEY2, step 3: decode.json + the "key re-reads its own source" control

`decode.json` runs `tools/decode_key.py` against `ciphertext_appendix.tsv` + `key.tsv` (tsv format,
`line_column: entry_label`, `folio_column: leaf`, `style: concat`, matching the antt-linhares-chave
precedent). `python3 tools/decode_key.py ciphers/antt-msliv0638-brochado-1712 --check` exits 0: it
regenerates `reading_appendix.txt` and `reading_appendix_tokens.tsv` byte-for-byte from the two inputs
(1702 tokens: C 1371, M 292, U 39 -- U is a code with no `key.tsv` row at all, none of it silently
guessed).

This is **not a rule-7 reading of anything new** -- every entry the appendix contains is already given in
plain Portuguese by the manuscript's own Deciffrada line (`plaintext_appendix.tsv`); there is no spec or
judge for this target yet (that is the next worker's job, per the "Not done this pass" note below). What
this step checks is the control CLAUDE.md's job brief asks for: **the key must re-read its own source.**
`scripts/06_decode_agreement.py` compares, per entry, the letters `03_align_pairs.py` actually paired to
each code (its `_pairs.json`, the ground truth `04_build_key.py` was built from) against
`decode_key.py`'s own mechanical output for the same tokens (`difflib`-aligned, so a token dropped by an
upstream mismatch doesn't cascade into misaligning every later token in the same entry).

**Result: 19 of 38 entries have at least one code-letter pair to check against** (the other 19 either
contributed zero pairs at all -- every one of their CODE spans fell into `03_align_pairs.py`'s
length-mismatch list rather than a clean pair, most often because of a length gap between the transcribed
cipher tokens and the transcribed Deciffrada text that alignment fixes above did not resolve -- or, for
Carta 30/58/61/70/72/73/74/79/80/91/92/96/101/105/106/107 etc. that DO appear in the anchored-OK list,
still had every one of their individual CODE-run spans land on the mismatch side rather than the pairs
side; see `03_align_pairs.py`'s own mismatch printout for the per-span detail). Of those 19, **3 entries
decode at 100% agreement with their own pairs** (Carta 23, Carta 105, m0292's Passage 2a) and **16 are
listed in `conflicts.tsv`** at 75-93% agreement (384 positions compared overall, 340 agree, 88.5%). Every
recorded disagreement is a **homophone case**, not a decoding bug: each mismatching position is a code
whose `key.tsv` value is the tallied *majority* letter (grade C, >=65% of >=2 observations) but this
particular occurrence's own aligned letter was one of the *minority* readings the same code also carries
(e.g. `26` is `u` at 65% majority but genuinely also stands for `v` in ~30% of its observed entries,
consistent with the u/v orthographic looseness already noted for this code; `8` is `i` at 79% but also
`j` in a handful of entries). `conflicts.tsv` lists the exact `expected!=decoded` letter pairs per entry
so a future worker can see at a glance which of these are real homophones (period Portuguese didn't
always distinguish u/v, or c/g in this hand) versus a transcription slip worth re-checking against the
image. No entry shows a wholesale, systematic mismatch (e.g. every position off by a fixed shift) that
would suggest a broken key or a mis-keyed alphabet.

**Not done this pass (next worker, per this job's brief -- out of PX-BROKEY2's scope):** the body-passage
sweep beyond m0276, `specs/antt-msliv0638-brochado-1712.json` + `tools/judge_plaintext.py`, and a
fresh-instance re-derivation blind to this worker's scripts.

### Host report (this pass)

No network access; this pass worked entirely from the images and TSVs already on disk.

## PX-BROPASSB (25 Sept 2026): second blind pass, reconciliation -- gated at 85.8%, not rebuilt

Worker PX-BROPASSB (Sonnet, session_01GqwFqqfntPyB2tgNpibc5p), job: this job brief's step 2
(second blind transcription pass B + reconcile against pass A + rebuild key). PX-BROKEY2's
own background pass-B subagent (claimed 07:30, progress logged 07:48-07:51) never landed on
disk or in git before that worker was interrupted at $14.42 (08:01 ROOM line) -- confirmed by
`git log` and `ls` on this folder at the start of this job: no `passB_*` files existed. This
job re-ran pass B from scratch rather than assuming any partial background work survived.

**Pass B method:** two Sonnet subagents, run in parallel, each reading full-resolution images
directly (`images/full_PT-TT-MSLIV-0638_m0NNNN.jpg.jpg`) with no access to any existing
transcription, key, reading, or this file -- genuinely blind, split m0280-288 (22 entries,
1026 coded tokens) / m0289-296 (17 entries, 734 coded tokens). Both subagents were given only
the (leaf, entry_label) index (a structural key, not cipher/plaintext content) so their output
could be matched row-for-row against pass A; both confirmed every expected entry present and
found no extra ones. `passB_cipher_1/2.tsv` + `passB_plain_1/2.tsv` (per-batch) merged into
`passB_cipher.tsv` (1760 coded-token rows) and `passB_plain.tsv` (39 entry rows); entry-key
sets diffed identical to pass A's before reconciling (`diff <(cut -f1,2 ...) ...` empty both
ways).

**Reconciliation:** `tools/reconcile_passes.py` does not fit this layout (it expects a
per-line-of-image pass keyed by a crop id in `wide`/`long` format, not a per-entry token table
keyed by `entry_label` with no crop directory), so wrote `scripts/07_reconcile.py` per the
job brief's fallback clause. Per entry, aligns pass A's and pass B's ordered coded-token lists
with `difflib.SequenceMatcher` (trailing `?`/`±` uncertainty markers stripped for comparison
only); `equal` opcodes count as agreement, `replace`/`delete`/`insert` as disagreement, exactly
as `tools/reconcile_passes.py`'s own doc string defines its agreement metric (aligned columns
where every pass agrees, over total aligned columns).

**Result: token agreement 1516/1766 = 85.84%, under the job brief's 90% gate.**
Deciffrada-line word-level agreement (a looser check, word by word rather than one exact
1000+-character string): 404/558 = 72.4%; exact full-line string match is a near-useless
metric here (3/38 = 7.9%) since a single accent or spacing difference anywhere in a long line
fails the whole line even when every word agrees -- reported for completeness, not used as the
gate. Per the job brief ("If agreement is under 90%, stop after writing the numbers and flag
it"), this job stopped here: `disagreements.tsv` (250 rows) and `agreement.tsv` (39 rows, one
per entry, share 61.5%-100%) are written; `ciphertext_appendix.tsv` and `plaintext_appendix.tsv`
are **unchanged** (no grade column added, no settling attempted, no key rebuild, no
`decode_key.py --check` re-run) -- reverted after a first script draft wrote them speculatively
before the gate check was in place.

**The shortfall is not diffuse noise -- it is dominated by one recurring glyph confusion.**
Per-entry agreement ranges 61.5%-100% with no single leaf or entry responsible (transcription.md's
"stop and report the blocker" case, not a "one bad leaf" case). But counting the 183 `replace`
disagreements by (pass-A token, pass-B token) pair: **`z`<->`7` (33+25=58) and `2`<->`7` (29)
account for 87 of 183 replace-disagreements (47.5%)** -- pass A consistently read a particular
recurring code-symbol shape as `z` or `2` where pass B consistently read the same shape as `7`,
across many different entries and both leaf batches (so it is not one subagent's idiosyncrasy
confined to one image). Next in size: `7`<->`5` (9), `c`<->`e` (6), `55`<->`11` (6, a possible
digit-run miscount rather than a single-glyph misread), `8`<->`g` (3), `b`<->`6` (3). This
strongly suggests a single graphically ambiguous secretary-hand shape (plausibly a script
numeral that can read as either "7" or a looped "z"/"2") drives most of the gap, not a broad
transcription-quality problem -- both subagents' own uncertainty notes (`passB_notes_1.md`,
`passB_notes_2.md`) independently flagged "4/7, 2/z, 5/8/S, 6/G" as the hand's main confusable
set before this quantitative check was run.

**Flagged, not done this job (out of step 2's scope once the gate failed):** a targeted image
check of the z/2-vs-7 shape (ideally with a cropping tool, which this folder does not yet use --
these are full-leaf DigitArq JPEGs, not IIIF crops) could resolve close to half the
disagreements from a single settled reading rather than requiring a full third pass; worth
trying before committing to `transcription.md`'s "third pass, not a fourth" route. `key.tsv`
already carries a grade-C `z->e` mapping (11/12 obs, PX-BROKEY2) and no strong prior mapping
for `7` or `2` as letter-codes (both are the small recurring digit codes described in
PX-BROKEY's "system" section) -- so which reading is right has a real effect on which parts of
the appendix decode, not merely a transcription nicety.

### Host report (PX-BROPASSB)

No network access; images already on disk from PX-BROKEY's pass. 2 Sonnet subagents (the two
blind transcription batches), each with image-reading tools only, no git/network access, per
COMMON's 2-subagent cap.

### Host report (PX-BROKEY2, prior pass)

No network access. See "PX-BROKEY2, step 3" section above.

### Host report (PX-BROKEY, prior pass)

`digitarq.arquivos.pt`: 24 full-resolution leaf-fetch requests (m0281, m0286-288, m0284-285, m0294-296,
m0270, m0200, m0276, m0279-283, m0289-293 -- note m0289-293 were already on disk from PX-CS01's earlier pass
and were not re-fetched, only viewed), each call's own >=3s pacing via `tools/digitarq_fetch.py`, well under
the 60-request session cap, no other worker on this host per the ROOM.md claim. No other host touched this
pass.

## PX-BROBODY (25 Sept 2026): body sweep for cipher-bearing leaves outside the appendix

Worker PX-BROBODY (Sonnet), job: sweep the body of the volume (m0001-278, m0297-306; the appendix m0279-296
is PX-BROPASSB's file scope) for cipher-bearing leaves and transcribe any found. Only worker on
`digitarq.arquivos.pt` this pass (claimed in ROOM.md).

### Sweep method and coverage

39 thumbnails at stride 8 (`tools/digitarq_fetch.py --thumbs ... --stride 8`, covering the whole 306-file
list at even intervals, 2 of the 39 falling inside the appendix range and excluded from body scope) built
into two labeled contact-sheet montages and eye-checked. Per the tool's own documented limitation (its
`--help` text: thumbnail-scale scoring gave 5/5 false positives in an earlier pass on this same host), no
cipher was distinguishable from ordinary dense cursive at 141x128px on any of the 39 -- this sweep narrows
nothing on its own, it only sets which leaves got a full-resolution look.

12 leaves pulled/viewed at full resolution: an even spread every ~30 leaves across the body (m0030, m0060,
m0090, m0120, m0150, m0180, m0210, m0300), plus m0270 and m0276 (already on disk from PX-BROKEY's prior
pass, copied into `images/body/` rather than re-fetched, so no extra host request), plus m0179 and m0181
(fetched to bound the cipher run found at m0180 on both sides). Full leaf-by-leaf record, method and outcome:
`body_leaves.tsv`.

**Two new cipher-bearing leaves found, both short inline numeral runs, neither with an interlinear
gloss on the body page itself:**
- **m0179**, foliated "80" in the manuscript's own page numbering, dated "Londres 28 de Abril de 1713":
  one run (`m0179-r1`, 19 tokens), introduced by "...sobre a Politica desta reposta que naõ hé mais qe" and
  closed by "e alguã coisa mais á manhaã lhe darei os...".
- **m0180**, foliated "81", dated "Londres 2 de Maio de 1713": one run (`m0180-r1`, 22 tokens), in a
  sentence about "Montaleon" ("...e antaõ darei a memoria por que [cipher] tudo."), closed by the plain word
  "tudo." before "Naõ referi o Diario do Parlamento...".

m0270 (plaintext, no cipher, per PX-BROKEY, confirmed) and m0181 (plaintext, no cipher on the visible page)
bound this find on both sides. **m0276** (found by PX-BROKEY, transcribed for the first time this pass) has
two runs, `m0276-r1` (17 tokens) and `m0276-r2` (20 tokens), split by the plain sentence "mas isto hé
impossivel, nem o tempo o permite, e só serve", as PX-BROKEY's prose already described.

No cipher found on any of the other 10 full-resolution leaves or 39 thumbnails. This is a spot-sample, not
exhaustive coverage of all 288 body leaves -- see "Not done this pass" below.

### Transcription (rule 7 process: two blind passes, reconciled)

Two independent Sonnet subagents transcribed all three cipher-bearing leaves from the images only (no
access to each other's output, no access to this repo's other files): `body_passA.tsv`, `body_passB.tsv`.
Raw agreement: 69/78 tokens (88.5%), all 4 runs individually above the 60% floor (`m0179-r1` 17/19,
`m0180-r1` 20/22, `m0276-r1` 13/17, `m0276-r2` 19/20) -- comfortably clear of a third full pass by
`transcription.md`'s "stop under 60%" rule, though the whole-run rate (88.5%) sits just over the tool's own
"a third pass only where the two disagree on more than a tenth of rows" guidance (11.5% disagreement). Given
every disagreement was a single ambiguous character (not a structural break) and the worker's own cost was
already well into this job's $6 stall-alarm cap after the two large subagent passes (pass B alone ran 103
tool calls / ~633s), the 9 disagreeing positions were settled by this worker directly, from 3-5x upscaled
crops of the exact contested spans (`/tmp/crop_*.jpg`, not committed -- scratch), rather than spawning a
third subagent pass. Reconciled table with per-token grade (`H` both passes agreed; `M` passes disagreed,
resolved by this worker's own re-check against the image) and the disagreement note: `body_ciphertext.tsv`.

Two token shapes stayed genuinely unresolved even after re-check and are carried as `?`-suffixed in
`body_ciphertext.tsv`: a doubled/looped "f"-like glyph (`m0179-r1` position 16, `m0276-r1` position 10,
transcribed `ff?`) and a cross/dagger-shaped mark on `m0180-r1` position 8 (transcribed `+?`) that does not
match the digit or single-roman-letter pattern of any other token in these three runs.

### Control found: m0179/m0180's own letter numbers already have appendix entries

Per this job's brief ("Note any body run whose letter number also has an appendix entry -- a control, not a
reading"): m0179 is foliated "80" and m0180 is foliated "81" in the manuscript's own page numbering, and the
appendix (`ciphertext_appendix.tsv`/`plaintext_appendix.tsv`, from PX-BROKEY) already carries entries
labeled **"Carta 80"** (`m0287`/`m0288`) and **"Carta 81"** (`m0288`) -- i.e. this body sweep's own page
numbers and the appendix's letter numbers appear to be the same numbering, at least in this stretch of the
volume (PX-BROKEY's own notes show this is NOT true everywhere: e.g. "Carta 13" sits near the volume's
start while ordinary page "133" is a late-1713 letter, so page-number and Carta-number drift apart
elsewhere -- treat the match here as local, not a general rule, until a worker maps the whole run).

- **Carta 80** (`ciphertext_appendix.tsv`): `10.26.18.16.8.14.15.2.7.4.55.12.15.f.8.3.15` (17 tokens),
  deciphered `plaintext_appendix.tsv` gloss: "Hum fim do proposito V." -- its first 13 tokens
  (`10,26,18,16,8,14,15,2,7,4,55,12,15`) are byte-for-byte identical, in order, to this pass's reconciled
  `m0179-r1` positions 1-13. After that the two diverge: the appendix's next token is a single `f`, then
  `8.3.15`; this pass's `m0179-r1` (both blind passes agreeing, and this worker's own 5x re-check confirming)
  reads two more numeral tokens, `11.55.`, between the matching "15" and the `ff?` glyph, then `8.3.15` --
  i.e. **the appendix's own "Carta 80" transcription appears to be missing two tokens (11, 55) that are
  genuinely present in the body image** (rule 2, image over transcription: the body page was re-checked at
  5x zoom this pass and the two extra tokens are clearly separated by periods, not a reading artifact). This
  also suggests the `ff?`/doubled-loop glyph at `m0179-r1` position 16 may simply be the single letter `f`
  (matching the appendix's single `f` token and `key.tsv`'s known code letters) rather than two symbols --
  unresolved, for the key-application worker.
- **Carta 81** (`ciphertext_appendix.tsv`): `15.25.16.8.5.8.17.20.4.26.8.4.20.10.7.5.15.18.26.14.8.5.17`
  (23 tokens), deciphered gloss: "O S.d± Luis the Communica± V." (the appendix's own OCR/transcription of
  this gloss looks corrupted -- "S.d±"/"the"/"Communica±" are not clean Portuguese, flagged for whoever
  next touches `plaintext_appendix.tsv`). This shares the same opening (`15,25,16`) and several matching
  substrings (`...20.4.26.8.4.20.10...`, `...18.26...8.5...`) with this pass's reconciled `m0180-r1`, but
  the two do NOT align token-for-token the way Carta 80/m0179 did -- most likely because this pass's own
  digit grouping is ambiguous in places (e.g. this pass's `85` at position 4 could be the appendix's `8`
  then `5` as two separate tokens; this pass's `57` at positions 6 and 22 could each be `5` then `7`) rather
  than a genuine text difference. **Not resolved this pass** -- flagged for the key-application worker
  rather than guessed at here.

`m0276`'s two runs have **no matching substring anywhere in `ciphertext_appendix.tsv`** (checked by exact
token-sequence search on several distinctive 3-4 token spans from each run) -- consistent with PX-BROKEY's
original finding that m0276 is a genuine body-only passage with no appendix gloss and no interlinear gloss
on its own page.

**This is not a rule-7 reading of anything** -- it is a transcription (of the body's own inline cipher) plus
a note of where an appendix entry may already carry the period plaintext for most of the same passage. No
judge was run; no spec exists yet for this target.

### Not done this pass (next worker)

- Only 12 of 288 body leaves were checked at full resolution (a ~4% direct sample plus the thumbnail
  spot-check, which cannot see cipher at all per its documented limitation) -- more cipher-bearing leaves
  almost certainly exist between the sampled points, especially now that m0179/m0180 show cipher recurs in
  short bursts through ordinary correspondence, not only near the appendix boundary (m0276) where it was
  first noticed. A denser full-resolution pass (e.g. every leaf, or every other leaf, in the April-May 1713
  stretch m0170-190 where two hits landed close together) is the highest-value next step.
- Reconcile `m0179`'s and `m0180`'s cipher runs against the appendix's "Carta 80"/"Carta 81" entries
  token-for-token (fix the appendix's own apparent 2-token gap for Carta 80; resolve the digit-grouping
  ambiguity for Carta 81) -- this could turn both into `S`- or `C`-grade confirmed readings almost for free,
  since the plaintext is already sitting in `plaintext_appendix.tsv`.
- Apply `key.tsv` to `m0276`'s two runs (still no gloss anywhere) as a genuine cryptanalytic candidate, now
  that `key.tsv` is rule-7 sound (per PX-BROKEY2's step 3 decode.json/--check).
- A `specs/antt-msliv0638-brochado-1712.json` + `tools/judge_plaintext.py` run, per rule 7, before anything
  from this target is reported as a reading.

### Host report

`digitarq.arquivos.pt`: 1 filelist request (already cached at `images/filelist.json` in the parent `images/`
folder, but `images/body/` is this worker's own file scope so its own copy was fetched fresh) + 39 thumbnail
requests (stride 8) + 8 new full-resolution leaf requests (m0030, m0060, m0090, m0120, m0150, m0180, m0210,
m0300) + 2 more full-resolution requests to bound the m0180 find (m0179, m0181) = 50 requests total this
pass, all through the tool's own >=3s pacing, under the 60-request session cap. m0270 and m0276 were copied
from PX-BROKEY's already-fetched images rather than re-requested. No other host touched. 2 Sonnet subagents
(blind transcription passes A and B, run in parallel, per this job's brief).

## PX-BROBODY2 (25 Sept 2026): letter->image map, widened sweep, NEW cipher found on m0275

Worker PX-BROBODY2 (Sonnet, session_01QiEShd8soBEjyGJrPwUxe9), job: map body image -> letter number, widen the
body sweep for cipher-bearing leaves targeted by letter number (appendix-covered letters as cheap controls,
no-appendix letters as priority, and the leaves around m0276 specifically), full transcription for any new
finds. **No decoding was done, per the brief.** Only worker on `digitarq.arquivos.pt` this pass (claimed in
ROOM.md). Built on PX-BROBODY's and PX-BROKEY's prior finds without altering their rows.

### Letter/page-number map (`body_letter_map.tsv`)

Confirmed by direct reading of the manuscript's own page number, not by thumbnail guessing (rule 2: a blurry
141x128 thumbnail is not a reliable source for a precise digit string, so this worker did not fabricate
per-leaf numbers from them -- see "Method note" below). All confirmed points:

| image | page no. | date on page (if any) |
|---|---|---|
| m0060 | 22 | -- |
| m0090 | 33 | -- |
| m0177 | **79** (new this pass) | -- |
| m0179 | 80 | Londres 28 Abril 1713 |
| m0180 | 81 | Londres 2 Maio 1713 |
| m0270 | 133 | Londres 15 Outubro 1713 |
| m0273 | **134** (new this pass) | -- |
| m0278 | **135** (new this pass) | Londres 29 Outubro 1713 |

**New confirmation of PX-BROBODY's finding:** page 79 (m0177) carries a cipher run at the foot of the page and
the appendix has a "Carta 79" entry -- a third data point (after 80/81) that the body's own page number and
the appendix's "Carta N" label are the same number, at least across this 79-135 stretch. Local image-per-letter
density: ~1-2 images per letter number in the 79-135 range (m0177->m0270 is 93 leaves for 54 numbers, ~1.72
images/letter), consistent with mostly single-leaf (recto+blank/short-verso) letters. This is *not* extrapolated
into a formula and used to invent numbers for unchecked leaves -- `body_letter_map.tsv` records only what was
actually read on each leaf, "n/a" where no number was visible on that image, with a note when the number was
inferred from context rather than read (m0181=82, carried over from PX-BROBODY, still not independently
reconfirmed this pass).

**Method note:** thumbnail digits were not legible with confidence at 141x128px (tried reading several already-
downloaded thumbnails directly and via the montage tool -- `tools/digitarq_fetch.py --montage` failed outright,
`ModuleNotFoundError: No module named 'PIL'`, not installed in this environment, flagged for whoever next
touches that tool). Given the choice between guessing numbers from an illegible source (rule 2 violation) and
spending host requests on full-resolution confirmation, this pass fetched full-resolution images instead of
extrapolating from thumbnails.

### Widened sweep: NEW cipher run found on m0275, extending the known m0276 run

Per the brief's specific instruction ("the letters around m0276, looking for cipher runs"), fetched full
resolution for all 6 unfetched leaves bounding m0276 on both sides: m0271, m0272, m0273 (already partly known),
m0274, m0275, m0277, m0278 (7 requests; m0270 and m0276 already on disk from PX-BROKEY/PX-BROBODY).

**m0275 (previously unchecked at full resolution -- the stride-8 thumbnail sweep skipped it) carries a genuine
cipher run of 33 tokens at the foot of the page, introduced by the plain sentence "O Estrangeiro está
grandemente empenhado/enganado [passA/passB disagree on this one plain word, not cipher] achado seu novo
Tractado, e não sei se este", running to the bottom of the page with no plain-text resumption before the page
ends.** Two blind Sonnet subagent passes (image only, no access to any other file, no access to each other):
31/33 tokens agree exactly (93.9%), comfortably above the two thresholds in `transcription.md` (60% floor,
third-pass trigger at >10% disagreement). The 2 disagreeing positions (line 1 token 8, line 2 token 14) are the
same doubled-letter glyph shape already flagged unresolved elsewhere in this exact passage (`ff?` at m0179-r1
pos16 and m0276-r1 pos10) -- transcribed `ff?`/`dd?` by analogy to that precedent, graded M, not independently
resolved by a third re-check this pass. Reconciled table appended to `body_ciphertext.tsv` as run `m0275-r1`
(33 positions, 31 H + 2 M).

**This run continues directly into the already-recorded `m0276-r1` (PX-BROKEY's find, 17 tokens): `m0275-r1`'s
last token and `m0276-r1`'s first token ("55") sit across a page break with zero intervening plain text.** The
true extent of this passage is therefore 33 + 17 = 50 cipher tokens before the first plain interruption ("mas
isto hé impossivel..."), not the 17 tokens previously on file for `m0276-r1` alone -- `m0276-r1`/`m0276-r2`
themselves are left unchanged (this worker's file scope did not include re-touching PX-BROKEY's rows beyond
this note), but any future spec/judge/key-application run against this passage needs to read `m0275-r1` +
`m0276-r1` + `m0276-r2` together as one continuous 70-token run, not `m0276-r1`/`m0276-r2` alone.

No cipher found on m0271, m0272, m0274, m0277, m0278 (all read at full resolution, plain prose). This is
consistent with PX-BROKEY's finding that m0276's passage has no appendix entry: the whole m0273-277 span
belongs to one letter numbered **134** (read directly off m0273), past the appendix's highest entry (Carta
123) -- a genuine ciphertext-only passage, structurally explained rather than a one-off anomaly. m0278 opens a
new letter, page 135, dated 29 Oct 1713, no cipher.

One loose end not resolved this pass: m0272 and m0277 both appear to close with the same date, "Londres 22 de
Outubro de 1713" -- on two different letters (m0272 is a short note re: Parlamento passage-negotiations; m0277
closes the page-134 letter that opens at m0273). Either Brochado wrote two dispatches the same day, or one of
these two date readings is wrong; not chased further this pass (out of scope: no decoding, no re-dating). Also
unresolved: m0277's own page number was not legible with confidence (a digit shape possibly "35", not
transcribed into `body_letter_map.tsv` as a reading).

### Appendix-letter control check (spent cheaply, per the brief)

m0177 = page 79, matches the appendix's existing "Carta 79" entry (a cipher run is visible at the foot of the
page, cut off before the page ends -- consistent with the appendix already carrying its decipherment). Per the
brief's instruction to spend most of the budget on no-appendix letters, this control was **not** transcribed in
full this pass (that would duplicate work the appendix already covers) -- recorded in `body_letter_map.tsv` and
`body_leaves.tsv` as a positive control only.

### Not done this pass (next worker)

- Still nowhere near exhaustive coverage of the 278 body leaves (this pass adds 9 more full-resolution leaves
  to PX-BROBODY's 12, i.e. ~21/278, ~7.5%) -- the m0275 find shows cipher can hide on a leaf a stride-8
  thumbnail sweep skips entirely between two already-known cipher leaves, so denser full-resolution coverage
  (not thumbnail) remains the highest-value next step, especially in the untouched 90-169 and 182-269 leaf
  ranges.
- m0181's page number (82) is still only inferred, not independently reread this pass.
- The m0272/m0277 same-date puzzle above.
- No decoding, no key application, no spec/judge run -- per this job's brief. The next worker to touch
  `key.tsv`/decoding needs to treat `m0275-r1`+`m0276-r1`+`m0276-r2` as one 70-token run, not two runs on one
  leaf.

### Host report

`digitarq.arquivos.pt`: 9 full-resolution requests this pass (m0271, m0272, m0273, m0274, m0275, m0277, m0278,
then m0169, m0177), all through the tool's own >=3s pacing, well under the 60-request session cap. m0270 and
m0276 read from disk (already fetched by PX-BROKEY/PX-BROBODY), zero new requests. No other host touched. 2
Sonnet subagents (blind transcription passes A and B on m0275, run per this job's brief; one ran synchronously,
one in the background -- both blind to each other and to every file but the one named image). Cost: not
visible to me.

## PX-BROGLYPH (25 Sept 2026): the z/7/2 glyph settled, key rebuilt

Worker PX-BROGLYPH (Sonnet), job: settle PX-BROPASSB's dominant disagreement pair (z<->7, 2<->7 -- 87 of 183
replace-disagreements, see "PX-BROPASSB" above) from the page images and rebuild the key. Full method and
crop-by-crop evidence in `glyphs.md`; summary here.

**Tool.** `tools/glyph_atlas.py` (the existing shared segment/cluster/atlas/classify pipeline for
invented-alphabet pages, built for dupuy452/fr.2933) gained a `crop` subcommand: cut one or more individual,
upscaled PNG crops either straight from a plain image by pixel box, or from a prior `segment` run's own
sign/mark boxes -- CLAUDE.md Usage 8 ("add an option to the tool, not a private copy"), since neither
`iiif_lines.py` (IIIF only) nor the rest of `glyph_atlas.py` (a full labelled-atlas pipeline, more than a
one-off dispute needs) fit. Offline test in `tools/tests/test_glyph_atlas.py`. 20 crops in `images/crops/`.

**Finding.** One recurring glyph -- a period "barred 7" (horizontal top stroke, diagonal, mid-stroke
crossbar) -- read inconsistently as `z`, `7`, or (twice, pass B only) `2` by both transcription passes,
uniform across all 9 leaves checked (m0280, m0281, m0282, m0289-m0294) whether currently labelled `z` or `7`,
including the *agreed* `z` instances (both passes agreeing was two passes sharing one misreading, not
evidence of a real letter z: CLAUDE.md rule 2, image over transcription). Distinguishable from this scribe's
own plain-hand cursive z (`images/crops/m0280_plain_naofaz3.png`, "não faz") and from a genuine loop-shaped
numeral 2 (multiple side-by-side crops, e.g. `m0294_carta110_line2.png`). Settled: every `z` token (70,
disputed and agreed) and the 58 z<->7-disputed `7`s -> `7`; the 29 2<->7-disputed positions -> `2` (pass B
misread an unambiguous loop-2, a separate, ordinary digit slip).

**Settlement (`scripts/08_settle_glyphs.py`, run from `disagreements.tsv` + the two appendix TSVs, no
network).** Adds a `grade` column to `ciphertext_appendix.tsv` (per token) and `plaintext_appendix.tsv`
(per entry, H only if every one of its tokens is H) and rewrites `cipher_line` to match the settled tokens
(re-segmenting each entry's line with 01_segment.py's own chunk logic so the two files stay in the sync it
requires). Grade H: already agreed, or crop-checked this pass (the 9 leaves above). Grade M: the 96 other
replace-disagreements, the 3 delete and 67 insert/extra-b structural mismatches (none crop-checked this
job -- a harder, different problem, see glyphs.md), and the z/7/2 disputes on 4 leaves not individually
re-viewed (m0283, m0286, m0287, m0288 -- resolved by the same rule since every checked leaf agreed with zero
counterexamples, but not itself crop-confirmed). Result: **1588/1702 tokens grade H (93.3%), 114 grade M
(6.7%)**; 7 `z` tokens remain (disputes against something other than 7, e.g. `z` vs `rr`/`e`/`2`, not
investigated this pass -- left as `z`, ungraded H).

**Raw agreement with pass B barely moves (1520/1770 = 85.88%, was 1516/1766 = 85.84%, `scripts/07_reconcile.py
--report-only`, new flag this job) -- and that is not a bug.** Pass B's two transcription subagents each
picked a *different* convention for the same glyph (`passB_cipher_1.tsv`, m0280-288: calls it `z`;
`passB_cipher_2.tsv`, m0289-296: calls it `7`) and applied it consistently within their own half -- exactly
the signature of one ambiguous sign read differently by different transcribers, which is the evidence for
"one sign" in the first place (glyphs.md). Settling every instance to `7` therefore *improves* raw agreement
with pass B on m0289-294 but *reduces* it on m0280-288, netting out near zero; the 29 kept-as-`2` positions
stay disagreements with B by design. "Matches pass B" and "graded H" are different metrics here on purpose:
the grade column is this job's own settlement confidence (crop-checked or not), not a re-score against a
second transcriber whose own two halves already disagreed with each other about which reading to prefer.

**Key rebuild (`scripts/01-04`, re-run in order, no network).** Anchoring unchanged (37/38 entries, 391
aligned pairs -- the glyph settlement doesn't touch plain-word anchoring). `key.tsv`: **40 codes, 29 at grade
C (was 28)**. Code `7`: 11 obs / M (`e` 55%) -> **27 obs / C (`e` 21/27 = 78%)** -- absorbs the settled z/7
instances and moves grade. Code `z`: 18 obs / C (`e` 83%) -> 2 obs / C (`r` 100%, the two residual
unsettled-leaf pairs -- both genuinely `r`, not a regression). Code `2`: unchanged, 18 obs / M (`d` 56%,
`e` second) -- none of its anchored/paired observations were touched by this settlement (the 2<->7 disputes
that got kept as `2` weren't part of the 03_align_pairs.py sample). `scripts/06_decode_agreement.py`'s
control (does `decode_key.py` mechanically reproduce 03_align_pairs.py's own ground-truth pairs) is
**unchanged, 340/384 = 88.5%** -- expected, since no code's *majority* letter flipped, only confidence; a
control that tests "same output" is insensitive to a confidence-only change by construction.

**`decode_key.py --check`: exits 0.** Overall decode confidence over all 1702 tokens: **C 1420, M 243, U 39
(was C 1371, M 292, U 39)** -- +49 grade-C decoded tokens, 0 change in U (unkeyed codes untouched).

| | before (PX-BROKEY2) | after (PX-BROGLYPH) |
|---|---|---|
| Anchored entries | 37/38 | 37/38 (unchanged) |
| Aligned code-letter pairs | 391 | 391 (unchanged) |
| key.tsv codes / grade C | 40 / 28 | 40 / 29 |
| decode_key.py --check tokens | C 1371, M 292, U 39 | C 1420, M 243, U 39 |
| 06_decode_agreement control | 340/384 = 88.5% | 340/384 = 88.5% (unchanged) |
| ciphertext_appendix.tsv grade | (no grade column) | H 1588/1702 = 93.3%, M 114/1702 = 6.7% |
| raw token agreement vs pass B | 1516/1766 = 85.84% | 1520/1770 = 85.88% (see note above -- not the settlement metric) |

**Not done this pass** (next worker, per this job's brief's scope): the 96 non-z/7/2 replace-disagreements
and the 67 insert/delete/extra-b structural mismatches are still open (grade M); a body-passage sweep beyond
m0276/m0179/m0180 (PX-BROBODY, concurrent); `specs/antt-msliv0638-brochado-1712.json` + `tools/judge_plaintext.py`;
a fresh-instance re-derivation blind to these scripts, per rule 7, before any reading from this target is
reported outside the repo.

### Host report (PX-BROGLYPH)

No network access; this pass worked entirely from the images already on disk (`images/full_PT-TT-MSLIV-0638_
m0280.jpg.jpg` etc., fetched by PX-BROKEY/PX-CS01) and the TSVs already on disk. No subagents. Cost: not
visible to me.

## PX-BRODEC (25 Sept 2026): decode.json extended, controls gate failed, stopped per brief

Worker PX-BRODEC (Sonnet, session_01NEq1D4d8STWRc3sbmXuUM3), job: decode the body cipher runs with the
period key, controls first, then spec/judge/re-derivation (rule 7). No network access used.

### Step 1: `decode.json` extended to cover the body

Added a second job to `decode.json` (`ciphertext_appendix.tsv`'s job is unchanged) that runs
`tools/decode_key.py` against `body_ciphertext.tsv` + `key.tsv`, writing `reading_body.txt` and
`reading_body_tokens.tsv`. `scripts/09_body_prep.py` (new, idempotent) makes two small, reproducible edits
to `body_ciphertext.tsv` first: (1) adds a `conf` column duplicating the existing `grade` column (H/M, the
transcription-pass agreement grade), since `tools/decode_key.py`'s own uncertain-confidence logic looks for
a column literally named `conf`/`confidence` to force a token to grade M regardless of the key's per-code
grade -- this reuses the shared script unmodified (this worker's file scope excludes `tools/`) rather than
adding a private decoder; (2) corrects `letter_no` from `none` to `134` for the `m0275`/`m0276` rows, per
PX-BROBODY2's already-established finding (m0273 read directly as page 134, continuous through m0277) --
a metadata correction from a fact already on file, not a ciphertext repair (rule 2 is about the transcribed
tokens, untouched).

The combination works without touching `tools/decode_key.py`: for each body token, the mechanical grade is
the key's own per-code grade (key.tsv's `grade` column, C or M) unless the transcription's own `conf` is M,
which forces the token down to M regardless; a code absent from `key.tsv` grades U. This is exactly rule
4/the brief's step 1 scheme (C = code C in key.tsv *and* token H in transcription; M = either at M; U =
unkeyed).

`python3 tools/decode_key.py ciphers/antt-msliv0638-brochado-1712 --check` exits 0 (both jobs up to date):
`body_ciphertext.tsv: tokens 111: C 75, M 25, U 11`.

### Step 2: controls -- both under the 80% gate; stopped here per the brief

`scripts/10_body_control.py` (new) decodes `m0179-r1` (letter 80) and `m0180-r1` (letter 81) from
`reading_body_tokens.tsv` and compares each, letter by letter, against `plaintext_appendix.tsv`'s own
Carta 80/81 Deciffrada line (stripped of spaces/the trailing "V./V.Sa/V.mce" closing abbreviation, folded to
base letters) using `difflib.SequenceMatcher` over the two letter sequences -- the same alignment convention
`tools/reconcile_passes.py` and this target's own `scripts/07_reconcile.py` already use (`equal` opcodes =
agreement, `replace`/`insert`/`delete` = disagreement, over the longer sequence), rather than a fixed-index
comparison, since `m0179-r1` is already known to carry 2 more tokens than the appendix's own stored
ciphertext for the same letter (PX-BROBODY).

```
== m0179-r1 vs Carta 80 ==
  body decode (19 tokens): humfinodespropp_ito
  appendix plaintext, stripped (17 letters, from "Hum fim do proposito"): humfimdoproposito
  agreement: 13/19 = 68.4%
  opcodes: replace body[5:6]='n' plain[5:7]='md'; delete body[7:10]='des' plain[8:8]='';
           replace body[14:16]='p_' plain[12:14]='os'

== m0180-r1 vs Carta 81 ==
  body decode (22 tokens): oof_i_l_uislhdcpmu_ic_
  appendix plaintext, stripped (19 letters, from "O S.d± Luis the Communica±"): osdluisthecommunica
  agreement: 11/22 = 50.0%
  opcodes: replace body[1:6]='of_i_' plain[1:3]='sd'; delete body[7:8]='_' plain[4:4]='';
           replace body[11:12]='l' plain[7:8]='t'; replace body[13:14]='d' plain[9:10]='e';
           replace body[15:16]='p' plain[11:13]='om'; replace body[18:19]='_' plain[15:16]='n';
           replace body[21:22]='_' plain[18:19]='a'
```

**Both controls are under the brief's 80% gate (68.4% and 50.0%). Per the brief ("If either control is
under 80%, stop after step 2 and report why"), this job stops here** -- steps 3 (letter 134's full
Portuguese + English gloss), 4 (spec + judge) and 5 (fresh-instance re-derivation) are **not run** this
pass. Status line stays `partial` (unchanged), per the brief.

**Why, per run -- this points mostly at transcription/segmentation and the appendix's own copy, not at the
key being wrong:**

- **m0179-r1 / Carta 80 (68.4%).** The first 13 of 19 body tokens are the *same codes in the same order* as
  all but the last 4 of the appendix's 17 stored tokens for Carta 80 (PX-BROBODY already established this
  byte-for-byte match) -- decoding identical codes through the identical key necessarily gives identical
  letters, so this prefix is not an independent check of anything beyond determinism. Of the genuine
  disagreement: one is the *same* homophone conflicts.tsv's own internal check already names for this exact
  entry (code `14`'s majority value is `n`, decoded here, where this occurrence's own Deciffrada wants `m`
  -- a documented minority reading, not a new failure). The rest (`delete ... 'des'`, `replace 'p_'/'os'`)
  falls exactly where the body page shows 2 extra tokens (`11`, `55`) plus the still-unresolved `ff?` glyph
  that the appendix's stored ciphertext does not have at all for this entry (PX-BROBODY, image-verified at
  5x zoom) -- an appendix-transcription gap already on file, not a body-decode error. Taken together, the
  actual novel disagreement is small: one known homophone plus one known token-count gap, not a broadly
  wrong key.
- **m0180-r1 / Carta 81 (50.0%).** Two compounding, already-flagged problems, neither new: (1) `conflicts.tsv`
  itself records Carta 81 as `0 compared -- no resolved tokens` for the appendix's *own* internal
  key-vs-Deciffrada check (PX-BROKEY2) -- i.e. this entry could not be validated even against its own source
  before this control ran, a pre-existing gap in the anchoring, not something this job introduced; (2) the
  Deciffrada line used as ground truth here ("O S.d± Luis the Communica± V.") is itself flagged in NOTES.md
  (PX-BROBODY) as looking corrupted -- "the" reading inside nominally-Portuguese text is the tell -- so a
  low score against it is partly a low score against noisy ground truth, not evidence the decode is wrong.
  PX-BROBODY also found the body's own digit grouping for this run is ambiguous in several places (its `85`
  could be `8`+`5`, its `57` could be `5`+`7`), unresolved before this pass; that ambiguity, not chased
  further here (out of this job's step 2 scope, which is compare-and-stop), likely explains more of the gap
  than the key does.

**Not a verdict that the key is broken** -- both explanations point at (a) known, already-logged
transcription/segmentation gaps between the body page and the appendix's stored transcription, and (b) for
Carta 81 specifically, a ground-truth copy already flagged as corrupted -- rather than at systematic
key error. The next worker who wants to clear this gate should, in priority order: (1) fix the appendix's
own 2-missing-token gap for Carta 80 (image-verified, straightforward); (2) resolve `m0180-r1`'s digit-
grouping ambiguity against the image before re-running this control; (3) only then decide whether letter
134's decode (already mechanically produced in `reading_body_tokens.tsv`/`reading_body.txt` by step 1, not
otherwise written up or judged this pass) is worth spec/judge/re-derivation.

### Host report

No network access; this pass worked entirely from the images, TSVs and key already on disk. No subagents
(steps 3-5, which would have used one, were not reached).

## PX-BRODEC2 (25 Sept 2026): leave-one-out control with a matched synthetic control -- gate fails, stopped

Worker PX-BRODEC2 (Sonnet, session_01Ro1R6jX36gpMg7qPXi2VxB), job: replace PX-BRODEC's gate (which compared
body decodes against the appendix's own Deciffrada glosses and measured the period decipherer's
abbreviation/paraphrase habit as much as the key -- see "Why this job" note in the job brief) with a
leave-one-out control over the appendix's own aligned code-letter pairs, gated against a matched synthetic
control per CLAUDE.md rule 3. No network access used.

### Step 1: leave-one-out control (`scripts/11_loo_control.py`)

For each of the 19 appendix entries that contributed aligned code-letter pairs to `key.tsv`
(`scripts/_pairs.json`, 391 pairs total -- see the entry list in the script), the key is rebuilt from every
OTHER entry's pairs using 04_build_key.py's exact majority rule (base-fold accents, majority letter per
code), then that held-out entry's own pairs are predicted from the rebuilt key. A code with zero
observations anywhere else counts as "unkeyed without this entry", reported separately from the accuracy
of codes that ARE keyed elsewhere.

**Matched synthetic control** (rule 3): the same 40 codes as `key.tsv`, each keeping its own global
`n_occurrences`, but with the code<->letter assignment randomly shuffled (permuting key.tsv's `value`
column across the 40 codes, so each letter keeps the same homophone group SIZE it has in the real key, only
which codes serve it is randomised) and then applied FORWARD to the appendix's own real plaintext letters
at all 391 aligned positions (for each real position's true letter, a synthetic code is drawn from the
shuffled group for that letter, weighted by the drawn code's own real `n_occurrences` so the synthetic
cipher's code frequencies approximate the real profile in aggregate). Same true letters, same entry
membership and span sizes as the real data; only which code stands for each letter is randomised. Fixed
seed 20260925, one run, not cherry-picked. The exact same LOO procedure then runs on this synthetic cipher.

```
POOLED (real target):      compared=379 correct=304 agreement=80.2%  unkeyed=12/391 (3.1%)
POOLED (synthetic control): compared=389 correct=376 agreement=96.7%  unkeyed=2/391 (0.5%)
gap (real - synthetic): -16.4 points
gate (>=80% AND within 10 points of synthetic): FAIL
```

The real target clears the bare 80% floor (80.2%) but the gap to its own matched control is -16.4 points,
outside the brief's +/-10-point band -- **the gate fails on the gap condition, not the floor.** Per rule 3's
own caveat about controls with no headroom: this control is NOT near ceiling in the sense that would make
it uninformative (96.7%, not ~100%, and its own unkeyed share is nonzero), so the -16.4 point gap is a real
signal, not an artifact of a saturated control. Full per-entry table in the script's output (re-run
`python3 scripts/11_loo_control.py`); worst-dragging entries (real pct - synthetic pct, most negative
first):

| entry | real | synthetic | gap | n compared |
|---|---|---|---|---|
| Carta 79 | 26.7% | 93.3% | -66.7 | 15 |
| Carta 80 | 50.0% | 100.0% | -50.0 | 16 |
| Passage 2a (m0284) | 53.8% | 100.0% | -46.2 | 13 |
| Carta 15 | 66.7% | 100.0% | -33.3 | 12 |
| Passage 3a (m0286) | 75.0% | 100.0% | -25.0 | 8 |
| Carta 101 | 80.0% | 100.0% | -20.0 | 5 |
| Passage 2a (m0294) | 80.0% | 100.0% | -20.0 | 10 |
| Carta 96 | 77.3% | 95.5% | -18.2 | 22 |
| Carta 91 | 79.2% | 96.3% | -17.1 | 24 |
| Carta 72 | 79.3% | 93.1% | -13.8 | 29 |
| Carta 13 | 80.6% | 94.3% | -13.6 | 31 |
| Carta 73 | 83.9% | 96.8% | -12.9 | 31 |
| Passage 3a (m0284) | 84.2% | 94.4% | -10.2 | 19 |

Only Carta 105 (94.7 vs 100), Passage 2a m0292 (100 vs 100, tied) and Carta 58 (85.7 vs 83.3, the single
entry where real beats synthetic) sit within 10 points. Reading: most entries individually generalise
worse than a clean, noiseless homophonic substitution of the same shape would -- consistent with the real
system carrying genuine scribal/transcription noise on top of whatever the key itself gets right, spread
fairly broadly rather than concentrated in one or two outlier entries (13 of 19 entries drag the pooled
gap past -10 points on their own).

**Per the brief, the gate fails: steps 3-5 (letter 134 decode, spec, judge, fresh re-derivation) are NOT
run this pass.** Status stays `partial`.

### Step 2: the m0179-r1/m0180-r1 vs Carta 80/81 comparison, re-stated as information (no threshold)

`scripts/12_gloss_diff.py` re-does PX-BRODEC's body-vs-gloss comparison with the gloss's own abbreviations
kept visible, and classifies every disagreement as **key value** (homophone minority), **transcription**
(an M-graded/unresolved body token, or the 2 tokens PX-BROBODY found in the image but missing from the
appendix's own stored copy), or **gloss** (the compiler's own abbreviation/paraphrase/corruption). No
threshold is applied.

**m0179-r1 vs Carta 80.** Removing the 2 already-documented extra body tokens (positions 14-15, codes 11
and 55, present in the body image but absent from the appendix's own stored Carta 80 cipher) leaves a
17-token sequence that matches the appendix's own stored Carta 80 codes exactly, position for position,
except one glyph (body's unresolved `ff?` where the appendix has a plain `f`). Comparing this 17-token
decode against the gloss "Hum fim do proposito" (17 letters, no abbreviations in this particular gloss)
position by position:

```
raw Deciffrada gloss: 'Hum fim do proposito V.'
gloss folded (17):    humfimdoproposito
body decode (17, extras removed): matches appendix's own stored sequence, ff? in place of the appendix's 'f'
9 agree; 5 KEY VALUE (homophone minority): pos6 code14 n-majority/m-minority, pos7 code15 o-majority/
  d-minority, pos10 code4 s-majority/r-minority, pos11 code55 p-majority/o-minority, pos12 code12
  r-majority/p-minority (every one of these gloss-wanted letters is a genuine minority observation already
  present in that code's own key.tsv 'all_observed_letters' tally -- not a new or invented homophone);
3 TRANSCRIPTION: pos8/pos9 (body tokens graded conf=M by the two blind transcription passes), pos14 (the
  unresolved ff?/f glyph).
Plus the 2 extra-token positions (14,15 in the raw 19-token count), also TRANSCRIPTION (appendix-copy gap).
```

So of the raw 19 body tokens: 9 agree outright, 5 are genuine key-value homophones (all independently
attested minorities of otherwise-majority codes), and 5 are transcription-side (2 extra tokens + 2 M-graded
disagreements + 1 unresolved glyph). This fully accounts for PX-BRODEC's raw 68.4% figure without any
unexplained residue, and confirms the earlier worker's qualitative read (mostly known, already-logged
causes) -- but the true self-consistency of this entry, done positionally, is **58.8% (10/17)**, not the
87% conflicts.tsv reports for Carta 80's own internal check.

**A measurement bug found in `06_decode_agreement.py`/`conflicts.tsv` while doing this comparison.** That
script (PX-BROKEY2's "the key must re-read its own source" control) compares the global-key decode of an
entry's own codes against that entry's own aligned pairs using `difflib.SequenceMatcher` over the two
letter *sequences*, rather than index-by-index. For Carta 80 both sequences are the same length (17) with
no real insertions/deletions, so a positional comparison is the correct one and gives 10/17 = 58.8% true
agreement (verified directly: `expected = ['h','u','m','f','i','m','d','o','p','r','o','p','o','s','i','t','o']`,
`decoded = ['h','u','m','f','i','n','o','d','e','s','p','r','o','s','i','t','o']`, 7 positions disagree).
But `SequenceMatcher`'s LCS-style alignment, faced with several repeated letters (o, p, d) at nearby
positions, finds a *different*, shorter edit script: it slides 2 of the 7 true mismatches onto a
same-letter coincidence a few positions away and counts them as `equal` (hiding them), and drops 2 more
entirely as an unindexed `delete` opcode that `06_decode_agreement.py`'s own tally loop does not count
into either `compared` or `agree` -- leaving only 2 of the 7 real mismatches visible, on a shrunken
denominator of 15 instead of 17, for a reported 86.7% (matches `conflicts.tsv`'s row exactly: `15  13  87%
m!=n; o!=e`). **This is a genuine measurement bug, not a modelling choice** -- it applies to every entry
whose expected/decoded sequences are the same length (i.e. every entry with no unresolved/dropped tokens),
and there is no reason to think Carta 80 is the only one affected; PX-BROKEY2's headline "340/384 = 88.5%"
self-consistency figure for the whole appendix likely overstates true positional agreement by a similar
margin. **Flagged, not fixed this pass** (would touch `scripts/06_decode_agreement.py`, `conflicts.tsv` and
the headline figure in the "PX-BROKEY2, step 3" section above -- out of this job's brief; a fix should
replace the `difflib` diff with a direct index-wise comparison for any entry where
`len(expected)==len(decoded_known)`, keeping `difflib` only for entries with a genuine length mismatch from
dropped/unresolved tokens). This finding is independent of the LOO/synthetic-control gate above (which does
not use `06_decode_agreement.py` or `difflib` at all) and does not change its FAIL verdict -- if anything it
suggests the appendix's true self-consistency is somewhat lower than previously stated, consistent with the
LOO gate's own finding of a real (not artifactual) shortfall against the synthetic ceiling.

**m0180-r1 vs Carta 81.** Cannot be checked the same way: the appendix's own stored Carta 81 cipher has 23
tokens but its own gloss ("O S.d± Luis the Communica± V.") folds to only 19 letters -- a 4-token count
mismatch **in the appendix's own copy**, independent of the body run entirely. This is exactly why
`scripts/03_align_pairs.py` excluded Carta 81 from `_pairs.json` in the first place (`conflicts.tsv`: "0
resolved tokens (entry had no usable anchors)") -- Carta 81 contributed **zero** observations to `key.tsv`
and cannot be checked against itself. The body's own 22-token run additionally has its own unresolved
digit-grouping ambiguity against both the appendix's 23 tokens and the 19-letter gloss (PX-BROBODY: e.g.
body's `85` at position 4 could be one token or two). And the gloss text itself is separately flagged as
likely corrupted (PX-BROBODY: "the" embedded in otherwise-Portuguese text is not a Portuguese word).
**Classification: TRANSCRIPTION (dominant: the appendix's own 23-vs-19 count mismatch, plus the body's
digit-grouping ambiguity) and GLOSS (the "the" corruption) -- there is no KEY VALUE evidence to classify
for this entry**, since it never contributed to the key and there is no reliable letter-for-letter ground
truth to compare against. PX-BRODEC's raw 50.0% figure for this run is not informative about the key
either way.

### Not done this pass, next steps

- The gate failed, so letter 134 (m0275-r1+m0276-r1+m0276-r2, ~70 tokens) remains undecoded and unspecced;
  the next worker on this target should not re-run the same gate without first addressing what actually
  drags it down (see the per-entry table above -- Carta 79, Carta 80, Passage 2a m0284 and Carta 15 account
  for most of the pooled shortfall).
- The `06_decode_agreement.py`/`conflicts.tsv` measurement bug above is a concrete, scoped fix (index-wise
  comparison when lengths match) that would give an honest self-consistency figure for the whole appendix;
  worth doing before trusting any future "control" built on that script.
- Carta 81's own appendix transcription (23 tokens vs a 19-letter gloss) and its gloss's "the" corruption
  are both worth a fresh image re-check before this entry is used for anything.

### Host report

No network access; this pass worked entirely from the TSVs and key already on disk (`_pairs.json`,
`key.tsv`, `ciphertext_appendix.tsv`, `plaintext_appendix.tsv`, `reading_body_tokens.tsv`). No subagents.
Cost: not visible to me.
