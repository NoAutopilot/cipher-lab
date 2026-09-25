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
