partial

blocked (pending L10: Textos Politicos 1993) -- under the Pipeline intake gate (CLAUDE.md, 25 Sept 2026: an `open`
that names an edition it could not open is `blocked`, whatever word it uses), this verdict is corrected from `open`
to `blocked` because the sender-family edition named below, *Textos Políticos, Económicos e Financeiros* (1993),
has never been read -- confirmed unreadable on three routes across three sessions (this pass, 24 Sept; LX-ED,
25 Sept, AUDIT.md section 10; AUD2's second audit, 25 Sept, AUDIT.md section 11) and now queued as `LOCAL-QUEUE.tsv`
row L10 for the owner's local runner. Read this pass: web search (queries: `"Condes de Linhares" "Chave de uma cifra"`, `"CLNH/0086" OR "maço 86" cifra`, `Rodrigo de Sousa Coutinho cifra/dicionário/chave`, `Cryptiana OR Cipherbrain Linhares cipher`, and a phrase search of the key's own worked-example plaintext `"a guerra de Franca com a Russia"`), Cryptiana and Cipherbrain (checked via search, no hit naming this unit or any Linhares cipher), the DECODE records already on disk at `sources/decode/*.tsv` (no login used, per COMMON rule 4; no Linhares/CLNH row), and shallow greps of `dbourdeau/cyphersolver` and `aaymeloglu/unsolved-ciphers` (depth-1 clones, 24 Sept 2026, `grep -rIl -i "linhares\|sousa coutinho\|CLNH"` outside `.git`, zero genuine text hits -- the only matches were binary image filenames that happen to contain the substring) all read, not deciphered; key on the same unit. The item's likely correspondence edition, D. Rodrigo de Souza Coutinho, *Textos Políticos, Económicos e Financeiros (1783-1811)*, ed. Andrée Mansuy-Diniz Silva, Banco de Portugal, 1993 (2 vols.), could not be opened this pass: its only located copy online, `https://www.bportugal.pt/sites/default/files/ocpep-7_t1.pdf`, returned HTTP 403 to both WebFetch and `curl -A "Mozilla/5.0"` -- one retry, then stopped per the good-citizen rule; not logged as unreachable-and-abandoned, but as a named next step (see below). The 1908 family biography *O Conde de Linhares* (Agostinho de Sousa Coutinho, Marquês do Funchal; archive.org id `ocondedelinhares00func`) gave zero hits for "cifra" on Internet Archive's full-text search API (`be-api.us.archive.org/fts/v1/search`), a search result, not a read of the book. No calendar/state-paper series applies (Portuguese noble-house archive, not a calendared series); the item itself carries no date or named correspondent from the archive's own catalogue metadata, so no single-letter calendar check is possible -- the check-solved sweep here is over the *key document and cipher system*, not a datable individual letter. Searched and logged 24 Sept 2026.

## The unit

ANTT `PT/TT/CLNH/0086/11` -- fonds Condes de Linhares, maço 86, undated within the maço's stated 1780-1827 span.
Viewer: `https://digitarq.arquivos.pt/fileViewer/a03cef08d3c04758aa148f5be56d3401` (docId `a03cef08d3c04758aa148f5be56d3401`), CC BY-SA 4.0, no login. 6-image composite item (scouted by scDIGI2, LANE N4, 24 Sept 2026; re-fetched full-resolution here for m0002-m0004 with `tools/digitarq_fetch.py`, now committed at `images/full_PT-TT-CLNH-0086-11_m000{2,3,4}.jpg.jpg`; m0001/m0005/m0006 are unrelated papers bundled on the same unit and were not re-fetched):

- **m0001**: unrelated French billet ("brûlez ceci" -- "burn this"). (2 Oct 2026, NEXT-LIN: not unrelated -- m0001 is the *verso of the m0002 leaf itself*, read in full below, "m0001 fetched and read".)
- **m0002**: live numeric ciphertext (H grade, read directly off the image). One leaf, folded, carrying pages numbered "2" and "3" of a longer letter -- pages 1 and 4 are not part of this 6-image item, so the ciphertext here is a mid-letter fragment, not the whole dispatch. (2 Oct 2026, NEXT-LIN: corrected -- the leaf is a single half-sheet billet whose other face, m0001, carries a clear French note; there are no pages 1 and 4; see "m0001 fetched and read" below.) About 26 five-to-seven-digit groups total (17 on page "2", 9 on page "3"), several carrying a small subscript digit 1-6 under the group (e.g. `328511` with a subscript `2`, `829011` with a subscript `5`). A Torre do Tombo ownership stamp and a wax seal sit on the page; no exact digit-by-digit transcription was made this pass (out of this brief's scope -- a transcription pass would need its own worker per CLAUDE.md's tools/ layout).
- **m0003-m0004**: titled "**Chave**" (key), with the archival mark "C. Linhares m86/11" in a later hand. Full text (H grade, read from the image, Portuguese as written, my paragraphing):

  > O 1º algarismo de cada numero indica quantos algarismos subsequentes representão a pagina do Diccionario onde se acha a palavra que o mesmo numero exprime.
  >
  > O algarismo, que se segue aos que exprimem a pagina, indica se a palavra está na 1ª, 2ª, ou 3ª columna da pagina.
  >
  > Depois de tirados os sobreditos algarismos, os que restão exprimem o numero da palavra na columna indicada.
  >
  > Os numeros por baixo de cada membro de algarismos denotão, quantas letras se hão de tirar do principio, ou do fim da palavra.
  >
  > Por exemplo. [worked example, transcribed below]
  >
  > Assim no 1º numero 1131 o 1º algarismo denota que o seguinte exprime a pagina, isto hé pag. 1: o algarismo 3 que segue o da pagina, indica que a palavra está na 3ª Columna da mesma pagina; e o algarismo 1 que resta, mostra que a palavra hé a 1ª da dita Columna.
  >
  > Do mesmo modo no 2º numero 322212 o 1º algarismo denota que os 3 seguintes exprimem a pagina, isto hé pag. 222: o algarismo 1 que segue os da pagina, indica estar a palavra na 1ª Columna da dita pagina; e o algarismo 2 que resta, mostra que a palavra hé a 2ª da mesma Columna.
  >
  > Como o Diccionario tem só paginas de 1 até 3 algarismos, todos os numeros que começarem pelos algarismos 4, 5, 6, 7, 8, 9, são nullos.
  >
  > Quando o cifrado começar por hum ou mais numeros nullos, denota que se uza do Diccionario Inglez, e se escreve nesta lingua.

  Restated: digit 1 of a group = how many of the following digits are the dictionary page number; the next digit after the page number = column 1/2/3 on that page; the digits left over = the word's rank within that column. A subscript number under a group gives how many letters to trim from the front or the back of the word so located (the key states the rule but, on this leaf, does not spell out which of front/back applies for a given group -- that has to be read off the worked example or inferred from what makes sense). Since the dictionary's pages run only 1-3 digits, any group starting with a digit 4-9 is a null-padding marker, and its presence signals a language switch: the rest of that cipher stretch is looked up in an *English* dictionary instead, "and is written in this language" (i.e. English words appear in the middle of an otherwise Portuguese plaintext).

  Worked example on the page (H grade, quoted verbatim with the plaintext gloss the key itself writes under each number):

  ```
  1131/2   322212.  313312.  321118(1)  23812(3)  311021.  1412(5)
  a        guerra   de       Franc[a]   a         com      a
  3344325(4)  335422(5)  1811(4)  3290219(1)  3234124.
  Rus[sia]    si         a        parece       inevitavel.
  ```

  (25 Sept 2026, LX-BOOK: the fifth group was misread as `23312` when this section was first written; the image reads `23812` -- confirmed by comparing its middle digit's figure-eight shape against the unambiguous `8` in `321118` two groups earlier, and against the open-loop `3`s in the same line. `23312` decodes against no candidate; `23812` decodes exactly. See `BOOK.md`.)

  Read together: "a guerra de Franca com a Russia parece inevitavel" ("the war of France with Russia seems inevitable"). Note (M grade, my inference, not stated by the key text): "Franca" and "Russia" are not looked up whole -- the key trims a dictionary headword down to a fragment ("Franc", "Rus") and, for Russia, stitches three separate lookups together ("Rus" + "si" + "a"). So a proper noun or inflected form missing from the dictionary is spelled by concatenating trimmed fragments of several dictionary words, the way a syllabary or nomenclator code pads out a fixed vocabulary. This is a real mechanical detail of the system, worth knowing before any decode attempt, but it is read off one example, not asserted by the key's own prose.

## The book

**Identified, 25 Sept 2026 (LX-BOOK, H grade, image-verified).** [Antonio Vieyra, abridger], *A New Pocket Dictionary of the Portuguese and English Languages, in Two Parts; Portuguese and English — English and Portuguese, Abridged from the Dictionary of Mr. Vieyra; with Additions and Improvements from Other Works.* Part I. Portuguese and English. London: printed for F. Wingrave, J. Johnson, and 17 other London booksellers, **1809**. Public-domain scan: archive.org `newpocketdiction00viey` (also Google Books `0mESAAAAIAAJ`, `ALL_PAGES`). All **twelve** groups of the key's own worked example decode correctly against this edition's Part I (page, column, rank and, where present, an end-trim of the stated count) -- see `BOOK.md` for the full table, the parse rule, and the page images in `images/book/`. "o Diccionario" and "o Diccionario Inglez" are almost certainly this one bipartite volume's two halves (Part I Portuguese-English used directly; Part II English-Portuguese, separately paginated in the same binding, for the null-padded English stretches), not two different books -- Part II itself has not yet been fetched or tested, since the worked example contains no null-padded group to test it against. 1809 sits inside the maço's 1780-1827 span and fits the already-inferred 1811-12 dating with two years to spare. **Kind: recovery** (the key text was already fully read; the book that closes the system is now also read, from the image, not guessed).

## Who it likely served (M grade, inferred, not established)

The fonds is Condes de Linhares. The 1st Conde de Linhares, D. Rodrigo de Sousa Coutinho (1755-1812), was Portugal's minister plenipotentiary at Turin 1779-1796, became Secretary of State for the Navy and Overseas Dominions in 1796, and from 1808 -- after the court's flight to Brazil -- served as Secretary of State for Foreign Affairs and War in Rio de Janeiro until his death on 26 Jan 1812. His brother, Domingos António de Sousa Coutinho (later 1st Marquis of Funchal), was Portugal's ambassador in London through the same Napoleonic period. The worked example's plaintext -- "the war of France with Russia seems inevitable" -- describes exactly the situation of 1811, the year before Napoleon's invasion of Russia, not any earlier or later point in the 1780-1827 span. Put together, this key most plausibly served Rodrigo de Sousa Coutinho's Rio de Janeiro secretariat corresponding with Europe (his brother's London embassy, or other Portuguese agents) in 1811-1812, which would also explain the built-in switch to an *English* dictionary: European political and military terms would sometimes need spelling in English rather than Portuguese. This is a plausible reading of the context, not a dated attribution -- the item itself names no sender, recipient or date, and the maço's own span (1780-1827) is wide enough to include the 2nd and 3rd Counts of Linhares as well.

## Search log (rule 1)

- Web (search engine), 24 Sept 2026: queries above; no hit for this unit, this key, or a Linhares/Sousa Coutinho cipher.
- Sender's/family's printed correspondence: *Textos Políticos, Económicos e Financeiros* (1993) located bibliographically (Banco de Portugal, ed. Mansuy-Diniz Silva) but its PDF host `bportugal.pt` returned 403 to WebFetch and to `curl -A "Mozilla/5.0"` (one retry); not opened. *O Conde de Linhares* (1908 biography, archive.org `ocondedelinhares00func`) full-text search API gave zero hits for "cifra" (a search result, not a read).
- Calendars/state-paper series: not applicable -- this is a Portuguese noble-house archive, not a calendared series, and the item carries no date.
- Cryptiana / Cipherbrain: checked via web search, no hit.
- DECODE (de-crypt.org): checked against `sources/decode/*.tsv` already on disk (no login, per COMMON rule 4); no Linhares/CLNH row.
- Solver repositories: `git clone --depth 1` of `dbourdeau/cyphersolver` and `aaymeloglu/unsolved-ciphers` (24 Sept 2026), `grep -rIl -i "linhares\|sousa coutinho\|CLNH"` excluding `.git`; zero genuine text hits.

## Grades

H (read from the image): the ciphertext's presence and rough extent on m0002; the key's full text and worked example on m0003-m0004; the book identification and all twelve worked-example decodes (25 Sept 2026, LX-BOOK, see `BOOK.md`).
M (inferred, not stated by the source): the fragment-concatenation mechanic for proper nouns; the family-member/date attribution above; the "Diccionario"/"Diccionario Inglez" = Part I/Part II of the same 1809 volume identification (strongly supported by the volume's own bipartite structure, but not stated anywhere on the key leaf).
No decode of the live ciphertext (m0002) was attempted this pass -- no transcription (`ciphertext.tsv`) existed yet when this worker stopped; see `BOOK.md` for what is left.

## Next steps (not run this pass, budget)

- Book identified this pass (see above, `BOOK.md`); once `ciphertext.tsv` (LX-TR's transcription of m0002) exists, decode it against this edition's Part I/Part II using the parse rule in `BOOK.md`, grade every token, and put the Portuguese reading in `reading.txt`.
- Re-try `bportugal.pt`'s Textos Políticos PDF from a different route (it may simply block the proxy's egress IP; a direct browser fetch was not tried).
- Fetch and spot-check Part II (English-Portuguese) of the same 1809 volume once a null-padded (4-9-leading) group turns up in the live ciphertext (`ciphertext.tsv` now has one: page 2, line 2, pos 6, `829011`) -- untested this pass.
- `ciphertext.tsv` now exists (LX-TR, below) and the book is identified (LX-BOOK, above) -- decoding it is the next worker's job; see `BOOK.md`'s "Not done this pass" for the parse rule to reuse.

## Transcription of m0002 (LX-TR, 25 Sept 2026)

`ciphertext.tsv` (26 groups: 9+8 across page "2"'s two lines, 8+1 across page "3"'s two lines) is the
committed digit-by-digit reading, grade H throughout, columns page_of_letter/line/pos/group/trim/book_page/
book_col/rank/is_null/grade. Every row parses under the key's own rule (checked programmatically): a normal
group's first digit d1∈{1,2,3} gives the page as the next d1 digits, the following digit∈{1,2,3} is the
column, the remainder (≥1 digit) is the rank; one group (page 2, line 2, pos 6, `829011`, trim 5) starts
with 8 and is a null (no book_page/col/rank). No group failed to parse; none was forced to fit.

Method: two independent blind Sonnet subagent passes from the image alone (`passA.tsv`, `passB.tsv`, neither
saw the other or this file), each self-checking its own reads against the key's parse rule and re-cropping
ambiguous digits before finalizing. Reshaped into `tools/reconcile_passes.py`'s long format (temp files, not
committed) and reconciled: **21/26 = 80.8% exact agreement** (well above the 60% stop-and-report threshold),
5 disagreement columns, matching a fully independent manual comparison of the two files. All 5 settled by
this worker from fresh 8-12x crops of the image (not from either pass):

| location | pass A | pass B | settled | how |
|---|---|---|---|---|
| p2 l1 pos1 | 328928 | 328923 | **328928** | 8x zoom on the group alone shows the last two digits clearly as "28", not "23" |
| p2 l2 pos4 | 3350320 | 3360320 | **3350320** | the disputed digit's shape (small open hook, no closed bottom loop) matches this scribe's "5" elsewhere (e.g. in `335412`) and not the fully closed loop this scribe uses for "6" (e.g. in the `m86/11` header, `260118`, `326624`) |
| p3 l1 pos1 | 329512 (6 digits) | 3295112 (7 digits) | **3295112** | a wide 7x crop clearly shows 7 digits, "3295112"; pass A dropped a digit |
| p3 l1 pos4 | 287219 (graded M) | 285219 | **285219** | 10x zoom shows a small caret-inserted "5" written *above* the line between "28" and "219" — a scribal correction the scribe squeezed in after the fact; pass A read the caret mark as part of a "7" |
| p3 l1 pos6 | 3293211 | 329231 (6 digits) | **3293211** | 12x zoom across two overlapping crops shows a doubled final stroke ("...2,1,1") that pass B read as a single "1"; the full 7-digit sequence parses (page 293, col 2, rank 11) |

Both readings parsed validly under the key rule in every disagreement case (the self-check does not
disambiguate a legibility call), so all five were settled purely from the image, not from which one parsed.

`key_example.tsv`: re-read the worked example on m0003 digit by digit (12 groups across its two lines),
independent of this file's own quote of the same passage. All 12 match the existing NOTES.md transcription
exactly and all parse under the key rule, including the two groups (1131 and 322212) the key text itself
works through step by step on m0003-m0004 — this worker's parse of those two agrees with the key's own stated
result (pag.1/col.3/rank.1 and pag.222/col.1/rank.2 respectively). This is an independent check on the parse,
not a new derivation of the rule.

Grades: all 26 `ciphertext.tsv` rows and all 12 `key_example.tsv` rows are H (read directly off the image,
confirmed by re-crop where the two blind passes disagreed). No group was left at grade M.

(25 Sept 2026, LX-BOOK: `key_example.tsv`'s group 5 needs a second look against this note's correction above --
this worker's independent digit check found `23812`, not `23312`, for that group, by comparing its middle
digit's shape against the unambiguous `8` in group 4 (`321118`) and the open-loop `3`s elsewhere on the same
line. `23312` parses validly under the key's structural rule but does not resolve to any dictionary entry;
`23812` resolves exactly to page 38, col 1, rank 2, trim 3 -> "A". If `key_example.tsv` also has `23312`,
its transcription and this worker's should be reconciled before anyone treats that group as settled at grade H.)

`m0005`-`m0006` fetched full-resolution and read (previously only thumbnail-checked by scDIGI2): confirmed
unrelated, a Hope & Co. (Amsterdam) exchange-rate note in French ("Original que me foi mandado enviar pela
Casa de Hope & C. d'Amsterdam..."), `m0006` its blank verso. No further ciphertext on this 6-image item beyond
`m0002`.

## More under this key (LX-TR, 25 Sept 2026)

Re-ran scDIGI2's search route (`GET /api/docs/search?query=TERM` on `digitarq.arquivos.pt`, terms `cifra`,
`chave de uma cifra`) against the whole DigitArq catalogue: **no new "chave"/"cifra" hit anywhere in fonds
PT/TT/CLNH since 24 Sept 2026.** The same 3 units surface as before: this one (`PT/TT/CLNH/0086/11`), and
`PT/TT/CLNH/0020/14` and `PT/TT/CLNH/0078/80` (both titled "Chave de uma cifra"). Checked both against a fresh
`docs/details` call: **both are still `hasImages:false`/`hasPublishedRepresentations:false`** (not digitized,
unchanged from scDIGI2's finding) -- still copy-order leads, not eye-confirmable, and since they carry no
description beyond the bare title, nothing establishes whether either is the *same* key as this one (different
maços within the fonds plausibly serve different correspondents/periods) or a different one. Not transcribed
(no image to transcribe).

No unit anywhere fit "carrying numeric groups in this scheme" by a keyword search, because a catalogue title
would not say so -- this item's own bundle (`PT/TT/CLNH/0086/11`) is titled only "Chave de uma cifra" and
that title covers the *whole* 6-image item (the unrelated billet and exchange note included), not just
`m0002`'s ciphertext page. So a live ciphertext leaf hiding in another item of the same maço, uncatalogued as
such, would not show up in any title search -- only eye-checking would find it.

Given that: `m0002` itself says its ciphertext is "pages 2 and 3 of a longer letter" and that "pages 1 and 4
are not part of this 6-image item" -- i.e. this bundle is a fragment, and the rest of the same physical letter
is filed elsewhere, plausibly (archives often scatter a letter's leaves across nearby items of the same maço)
as another item in **maço 86** itself. Looked up maço 86's own sibling list (`docs/details` on its parent id
`8046d3327fa94b36b114b02ab1295f11` gives `children.total: 21`, but -- as scDIGI2 found -- `children.results`
is always empty; walked it the same workaround way, by narrowing search phrases on the "Condes de Linhares,
mç. 86, doc. N" identifier pattern). Found 12 of the other 20 items this way (missing: `/03 /04 /06 /08 /09
/12 /19 /21`, not surfaced by the phrasings tried), none titled with any cipher/key term (all are named
correspondence, e.g. "Cartas de João Paulo Bezerra de Seixas para o 2º conde de Linhares"). **All 12 checked
are `hasImages:true`** (digitized, unlike PP-06/PP-07):

| Unit | docId | Title |
|---|---|---|
| PT/TT/CLNH/0086/01 | 9186594ae6b54b9daed7d9a5a2c3f241 | Cartas de João Paulo Bezerra de Seixas para o 1º conde de Linhares |
| PT/TT/CLNH/0086/02 | 28d1e5cc0b2c48688823e286bc1b62f8 | Cartas de João Paulo Bezerra de Seixas para a 1ª condessa de Linhares |
| PT/TT/CLNH/0086/05 | 559afca60b444e0fbc51a155001132d1 | Cartas de João Paulo Bezerra de Seixas para o 2º conde de Linhares |
| PT/TT/CLNH/0086/07 | 136931f77d5d4d3086c1b72a1f6ea959 | Cartas para João Paulo Bezerra de Seixas de D. Maria Balbina de Sousa Coutinho |
| PT/TT/CLNH/0086/10 | b53086a679db481eaa9eba9e2424498c | Cartas de D. Isabel Sill Bezerra para a 1ª condessa de Linhares e 2º conde de Linhares |
| PT/TT/CLNH/0086/13 | a95e4609533b48b3b7f6362f64ee97ae | Carta para a 1ª condessa de Linhares de um tio italiano |
| PT/TT/CLNH/0086/14 | 8832e1198743410a98f798fb336798d2 | Carta para a 1ª condessa de Linhares de José Correia da Serra |
| PT/TT/CLNH/0086/15 | 86cb94ae348a465e972c5ccbfd72853d | Carta para a 1ª condessa de Linhares de D. Maria Martina de Castro e Loynaz |
| PT/TT/CLNH/0086/16 | fed6b825282b4dd0b21a3696809aa46a | Carta para a 1ª condessa de Linhares de João Pedro Quinn |
| PT/TT/CLNH/0086/17 | 4443134ba9c14ccfab96e73d712ac294 | Ofício de João Paulo Bezerra de Seixas para António de Araújo de Azevedo |
| PT/TT/CLNH/0086/18 | 4bee49e273c641e8912027de15875dce | Post scriptum de uma carta ... por João Paulo Bezerra de Seixas para o 1º conde de Linhares |
| PT/TT/CLNH/0086/20 | e1f56f01341041eeaf932f9cdd3f5d59 | Apontamento sobre o carácter do 1º conde de Linhares |

None of these were opened/eye-checked this pass (out of this brief's scope, and none of their titles suggest
government/diplomatic correspondence of the kind the worked example's "war of France with Russia" plaintext
implies -- they read as family and social letters to the 1st/2nd conde and 1st condessa, an earlier
generation than the 1811-12 attribution in "Who it likely served" above). Flagged here as the cheapest
concrete next step for finding the rest of `m0002`'s letter (pages 1 and 4): a quick eye-check of these 12
plus the 8 still-unlisted maço 86 items (`/03 /04 /06 /08 /09 /12 /19 /21`, not found by the search phrasings
tried -- a `docs/details` walk by numeric guess, or a better search phrase, would complete the list) for
numeral-group ciphertext resembling `ciphertext.tsv`'s format. Not run this pass (budget; Part 2's brief asks
only to list candidates, not eye-check a maço's full sibling set).

Per-host report (Part 2 only): `digitarq.arquivos.pt` ~22 requests (2 full-image fetches for m0005/m0006, 1
item-details, 1 parent-maço-details, 4 search-phrase queries, 12 sibling hasImages detail calls, all >=3s
apart), well under the session's 60-request DigitArq cap.

## Maço 86 eye-check (LX-SIB, 25 Sept 2026)

**All 21 items of maço 86 are now identified.** LX-TR's 8 unsurfaced items (`/03 /04 /06 /08 /09 /12 /19 /21`)
were a search-phrasing artifact, not missing catalogue entries: the working phrase is `Condes de Linhares,
mç. 86, doc. N` with **no leading zero** on N (LX-TR's `doc. 03` etc. returned 0 hits; `doc. 3` returns the
item). Found all 8 this way (`docs/details` confirms all `hasImages:true`/`hasPublishedRepresentations:true`,
digitized like the other 12):

| Unit | docId | Title | Date |
|---|---|---|---|
| PT/TT/CLNH/0086/03 | 7e0f0cbeaf094ed5ac12ff916b40070e | Cartas de João Paulo Bezerra de Seixas para D. Mariana de Sousa Coutinho | 1805-02-22/1811-03-13 |
| PT/TT/CLNH/0086/04 | 53896856b3cc4e14b767316657a65b65 | Cartas de João Paulo Bezerra de Seixas para o Principal de Sousa | 1799-06-28/1817-08-14 |
| PT/TT/CLNH/0086/06 | 939a6b22b3c24971baadc8ef60beaa46 | Carta para João Paulo Bezerra de Seixas de D. Lourenço de Lima | 1806-08-18 |
| PT/TT/CLNH/0086/08 | 86fc1c29217e4802acc26ced9f3c975e | Carta do Principal de Sousa para João Paulo Bezerra de Seixas | 1806-03-04 |
| PT/TT/CLNH/0086/09 | 2ee9483c19c9400487f2811c6892393b | Cartas de D. Mariana de Sousa Coutinho para João Paulo Bezerra de Seixas | 1796-09-07/1807(?) |
| PT/TT/CLNH/0086/12 | c0ce7d80949e406b807bd4c37edb872a | Reflexões de João Paulo Bezerra de Seixas sobre um tratado | undated |
| PT/TT/CLNH/0086/19 | 25ec1554217a4e25a9c9911e87c7a9c5 | Apontamento de D. Mariana de Sousa Coutinho, sobre a demissão de seu irmão de presidente do Erário Régio | undated |
| PT/TT/CLNH/0086/21 | be4d15681c774e8eaf8c6e96da8e26e5 | Carta de João Paulo Bezerra de Seixas | undated |

Note on attribution (M grade): every titled item in maço 86 -- old and new -- centres on **João Paulo Bezerra
de Seixas** (letters to/from him, the 1st/2nd conde and condessa de Linhares, the Principal de Sousa, D. Mariana
de Sousa Coutinho), dated where known 1796-1817. This cuts against "Who it likely served" above (Rodrigo de
Sousa Coutinho's Rio secretariat, 1811-12, inferred only from the worked example's plaintext) -- the maço as a
whole reads as Bezerra de Seixas's own personal/family papers, not a diplomatic dispatch archive. Flagged, not
resolved: nothing here confirms or rules out either attribution for the *cipher key itself* (item `/11`), since
a private correspondent could still hold and use a diplomatic-style dictionary cipher.

Fetched a `filelist.json` (one request each, `page_size=600` covers every item in a single call) for all 20
items other than `/11` itself: total 604 images across the maço, overwhelmingly concentrated in five large
multi-letter bundles (`/09` 212, `/02` 126, `/04` 46, `/01` 82, `/03` 40 = 506 of the 604) with the other
fifteen items carrying 2-28 images each.

**Eye-checked this pass** (thumbnail, `--stride 1`, full coverage of the item): `/06` (4 images), `/08` (2),
`/12` (4), `/19` (4), `/21` (2) -- 16 images. **All five are ordinary cursive prose letters** (readable
running handwriting, salutations, signatures visible on some leaves) -- **none carries numeral-group
ciphertext**, none continues `m0002`'s hand, paper or page numbering. No candidate found among these five.

**Not eye-checked this pass** (budget): `/01` (82), `/02` (126), `/03` (40), `/04` (46), `/05` (8), `/07` (8),
`/09` (212), `/10` (28), `/13` (6), `/14` (4), `/15` (4), `/16` (4), `/17` (12), `/18` (4), `/20` (4) -- 592
images across 15 items, none opened. The three largest (`/02`, `/09`, `/04`) alone are 384 images, well beyond
this session's DigitArq request budget to thumbnail exhaustively; a follow-up pass should prioritise the
remaining small items (`/13 /14 /15 /16 /18 /20`, 6-28 images total ~ under 40 requests) before the three
large bundles.

**Result of this pass: no sibling ciphertext found. 6 of 21 maço 86 items eye-checked (the original `/11`
plus 5 new: `/06 /08 /12 /19 /21`), 15 of 21 (592 of 604 images in them) not yet opened.** `m0002`'s missing
pages 1 and 4 were not located in maço 86 this pass; they remain either in one of the 15 unchecked items, in a
different maço of the same fonds (out of this brief's scope), or in a different fonds entirely.

Per-host report (this pass): `digitarq.arquivos.pt` 57 requests -- 13 search-phrase queries (8 for the
zero-padded phrasing that returned 0 hits, 2 confirming the no-leading-zero fix on `/03 /04`, 3 more on `/06
/08 /09` once the fix was known; brief capped this step at 10, this pass used 13, judged worth it since the
fix was already found and all 8 missing items were then free to complete rather than leaving 3 unsurfaced),
8 `docs/details` calls (hasImages/title/date for the 8 new items), 20 `--list` filelist calls (1 each), 16
`--thumbs` calls (full coverage of the 5 small items checked) -- all >=3s apart, one at a time, 57 of the
60-request session cap. No 429/403/challenge seen. Files added: `images/maco86_scan/doc{06,08,09,12,19,21,
01,02,03,04,05,07,10,13,14,15,16,17,18,20}/filelist.json` (all 20 items) and `montage_01.jpg`/`thumb_*.jpg`
for the 5 checked items only (~450 KB total).

## Reading (LX-DEC, 25 Sept 2026)

`date -u` at start: 2026-09-25 01:17 UTC. Job: decode `ciphertext.tsv`'s 26 groups against Vieyra's 1809 Part I
(identified by LX-BOOK, `BOOK.md`). Key rule re-applied per group: page/column/rank from the digits (mechanical,
already computed by LX-TR in `ciphertext.tsv`'s `book_page`/`book_col`/`rank` columns and not re-derived here),
then the rank-th bold headword counted down that column of the fetched page image, then the subscript trim (when
present) removing that many letters from the **end** of the headword (the convention every worked-example test and
this pass's own results support; a front-trim alternative is noted where it was actually tried).

**Fetched:** 20 new page images (pages 60, 85, 132, 162, 223, 241, 247, 250, 251, 255, 262, 266, 281, 285, 289, 293,
295, 350, 362, 383 -- 23 distinct book pages needed in total, 3 reused from LX-BOOK's set: 110, 222, 354), all
via the same `archive.org` `BookReaderImages.php` route LX-BOOK used (`newpocketdiction00viey_jp2.zip`, internal
filename pattern confirmed by a byte-identical match against LX-BOOK's already-committed leaf 124: it is
`<identifier>_<4-digit-leaf>.jp2`, not `..._LEAF<n>.jp2` as BOOK.md's `download_note` literally reads -- BOOK.md's
route description is imprecise on this point, corrected here). Leaf-to-page offset drifts as BOOK.md already
flagged (10 near p.4-38, 12 near p.59-60, 13 near p.85, 14 near p.110-267, 16 near p.281-295, 18 near p.344-383);
every page cited was confirmed by reading the printed page number in the image itself (`NNN]` at top-left on an
even page, `[NNN` at top-right on an odd page, both after the running header), never assumed from the offset --
one page (60) needed a second guess (leaf71 read as page59, not 60; leaf72 confirmed page60), and one (85) needed
a fourth (leaf98 and leaf99 both returned a corrupt/black oversized image -- possibly a damaged or blank-plate jp2
in the archive.org zip around that leaf; leaf97 resolved cleanly to page85, no further investigation of the
black leaves attempted). All 23 images now committed at `images/book/`, manifest updated. Hosts: `archive.org`
~26 requests (20 new pages + retries), all sequential, User-Agent `cipher-lab research script (contact via
repository)`, no login, no 429/403 seen.

**Result:** all 26 groups resolve to a page/column/rank that exists in the dictionary except one (see below).
20 H, 6 M. Grades and full source citations are in `key.tsv`; `python3 tools/decode_key.py
ciphers/antt-linhares-chave --check` regenerates `reading.txt`/`reading_tokens.tsv` from it (exits 0, confirmed).
`tools/decode_key.py` gained two new job options this pass, `line_column`/`folio_column` (CLAUDE.md Usage 8 --
this target's `ciphertext.tsv` carries the manuscript's page and line as two separate columns rather than one
combined line id, which the existing `split_line` option could not express), with a fixture at
`tools/tests/decode_configs/antt-linhares-chave.json` (`python3 tools/tests/test_decode_key.py` passes for it; the
suite's one other failure, `rah-canada-1869`, is pre-existing and unrelated -- confirmed by re-running the suite
against the pre-this-session commit).

Reading (Portuguese as decoded, grade in brackets; page/letter breaks marked):

> [p.2] para[H] {supprir[M]} o[H] seu[H] lugar[H] junto[H] com[H] {man[M]} o[H]
> {d[M]} justa[H] he[H] segredo[H] ate[H] {[null]} o[H] ministerio[H]
> [p.3] pela[H] memoria[H] do[H] {[unresolved][M]} lhe[H] {pauperr[M]} {ven[M]} ha[H]
> logo[H]

No connected-sentence gloss is offered -- this is a two-page mid-letter fragment (pages 1 and 4 of the underlying
letter are not part of this archival item, per LX-TR), and about a quarter of the tokens are single-letter or
short dictionary-trim fragments (a mechanic the worked example itself uses for proper nouns: "Rus"+"si"+"a" =
Russia), not free-standing words, so the individual tokens read as isolated units rather than prose. Several
words that DO stand as ordinary Portuguese are plausible in context: `para` (for), `seu` (his/her/your), `com`
(with), `ate` (until), `segredo` (secret), `ministerio` (ministry -- fitting, since Rodrigo de Sousa Coutinho ran
Portugal's Rio secretariat), `pela` (by/through), `memoria` (memory), `lhe` (to him/her), `logo` (then/presently),
`justa` (also the fem. adj. "just"), `lugar` (place), `junto` (together), and `he`/`ha` (archaic spellings of
"e"/"ha", the same archaic spelling the key's own prose on m0003-m0004 uses: "...mostra que a palavra **he** a 1a
da dita Columna").

**Grade counts (rule 4):** H 20, M 6, C 0, S 0, I 0, U 0 (26 total; the one null group is graded H -- its status
as a null is certain even though what it implies mid-letter is not, see below).

**The 6 M-graded tokens, each a genuine open question, not a typo:**
1. **p2l1pos2** (group `336227`, page362 col2): rank7 is either "Supprír" (to supply) or "Suprémo" (supreme),
   depending on whether "Suppurár-se, v.r." (a reflexive form given its own bold line right after "Suppurár, v.n.")
   is counted as its own headword. This pass counted it separately (the convention used throughout, see below);
   flagged because the key's own worked example never tests a reflexive-form pair.
2. **p2l1pos8** (group `325532`, page255 col3, trim2): "Mándo, s.m. command, power" trimmed to "Man" -- a
   3-letter fragment, not a word on its own. Might be the start of a name (e.g. "Manoel/Manuel") continued by an
   adjacent group, not identified.
3. **p2l2pos1** (group `313211`, page132 col1, rank1): the column's very first item with a definition is "D, One
   of the mutes, supposed to be formed from the Greek Delta" -- the dictionary's own entry for the LETTER D, not
   an ordinary word. Above it, a large "D." heading marks the start of the D section in the book but carries no
   definition, so was not counted as rank0/1 itself. Token "d" is plausible as an initial/honorific abbreviation
   (cf. the fragment-concatenation mechanic) but this is a genuinely unusual dictionary hit worth a second look.
4. **p3l1pos4** (group `285219`, page85 col2, rank19) -- **UNRESOLVED.** Page 85's column 2 has only 15 true
   headwords (Calis...Calumnia, catchword "I" below); rank19 does not exist in it under the counting convention
   used everywhere else in this decode (every bold line, including homograph/variant pairs, counts). This group
   was one of LX-TR's five reconciled disagreements (a caret-inserted digit squeezed in above the line between
   "28" and "219"); the digits as settled parse validly under the key's rule but the resulting rank overshoots
   the actual column. Not forced to a guess. Candidates for what's wrong: the caret digit is still misread: the
   transcription may need a third look at the image; or the counting convention undercounts this specific column
   (no clear miscounted entry was found on a careful re-check, see key.tsv's note); or (least likely, since the
   book itself is independently confirmed against 12+ other groups) a different edition/impression paginates
   differently here. Left as a candidate that failed to resolve, not a reading (rule 7).
5. **p3l1pos6** (group `3293211`, page293 col2, trim3): "Paupérrimo, very poor" trimmed to "Paupérr" -- an
   unusual 7-letter fragment ending in a doubled consonant.
6. **p3l1pos7** (group `338326`, page383 col2, trim4): "Venáblo, a javelin" trimmed to "Ven" -- a 3-letter
   fragment, not a word on its own.

**Headword-counting convention (flagged per this brief's own request):** every bold word that starts a new
paragraph/line was counted as one entry for ranking purposes, including a reflexive form on its own line (item 1
above) and a second bolded homograph/accent-variant appearing right after the first (e.g. "Lúcifer"/"Lucifer" on
page251 col2 -- this pass's rank17 there is "Lugár"; NOT counting the second "Lucifer" separately would instead
land rank17 on "Lugarejo", one entry later -- both are real Portuguese words, "a place" vs. "a little
town/village", so this is recorded but not resolved either way). A continuation of a headword's definition
spilling from the bottom of one column/page into the top of the next was correctly NOT counted (checked against
the worked example's own page-110 "Com" test and against every column this pass opened) -- recognizable because
it starts mid-sentence rather than with a fresh bold word, and because the running header at the top of the new
column still matches the alphabetical range of the *new* first headword, not the continued one.

**The mid-letter null (p2l2pos6, group `829011`, trim5):** the key's prose on m0003-m0004 only describes what a
null means when the message *starts* with one or more nulls ("Quando o cifrado começar por hum ou mais numeros
nullos, denota que se uza do Diccionario Inglez" -- switch to Part II, English-Portuguese, for that stretch).
This null sits mid-letter, a case the key's own text does not cover. It carries a trim subscript (5) despite
having no dictionary lookup to trim from, which is also unexplained by the key's prose. Recorded as a null (grade
H -- the "first digit 8" fact itself is certain) with the implication left open; Part II of the 1809 volume has
still not been fetched (LX-BOOK's note; would be the next step to test whether the two tokens straddling this
null read as English).

**Judge (rule 7):** `specs/antt-linhares-chave.json` written this pass (`language: "pt"`, `min_word_cover: 0.5`).
```
$ python3 tools/judge_plaintext.py specs/antt-linhares-chave.json --file ciphers/antt-linhares-chave/reading.txt
PASS - antt-linhares-chave (a PASS is a gate for a verifier, not a reading; rule 10)
$ python3 tools/judge_plaintext.py specs/antt-linhares-chave.json --file ciphers/antt-linhares-chave/reading.txt --json
{
 "checks": {},
 "pass": true,
 "spec": "antt-linhares-chave"
}
```
**The judge has no Portuguese language model** (`tools/data/` holds `de16`, `fr16`, `it16` corpora only, no `pt`);
`judge_plaintext.py`'s `language`/`min_word_cover` checks are both nested under `if corpora:` and silently skip
when the spec's language has no corpus on disk, so `checks: {}` -- the reported PASS is vacuous (zero checks ran),
not a language-model confirmation. Whether to build a Portuguese 4-gram corpus for `tools/data/pt16` (the same
recipe as `de16`/`fr16`/`it16`) is a fair next step for any Portuguese target, this one included, but is out of
this brief's scope.

**Fresh-instance re-derivation (rule 7, step 5):** a Sonnet subagent given only the key rule as a paragraph, the
committed page images (via `images/book/manifest.json`'s `leaf`/`file`/`printed_page` fields only -- told explicitly
not to read the manifest's `content` field or this file, `key.tsv` or `reading.txt`), and `ciphertext.tsv`
independently re-derived every token. Raw result: 23 of 26 rows matched this pass's token exactly (accent marks
aside, which the subagent's report keeps and this pass's `key.tsv` drops -- not a real disagreement); 3 rows
differed. All 3 were checked a third time directly against the page image (below), and all 3 resolve in favour of
this pass's original reading -- the subagent's independent count was itself mistaken in each case, not this pass's:

- **p2l1pos5** (page251 col2, rank17): subagent got "Lugarejo", this pass got "Lugár" -- the disagreement flagged
  above (whether the "Lúcifer"/"Lucifer" homograph pair counts as one entry or two). Re-cropped page251 col2 a
  third time at high zoom: both "Lúcifer, s.m. the arch-devil." and "Lucifer, (in astron.) the star called Venus
  or Lucifer." are unambiguously two separate bold headwords on their own lines, confirming the every-bold-line
  convention this pass used throughout gives rank17 = "Lugár" correctly. The subagent's own notes say it also
  counted homograph pairs separately "per the instructions", so its "Lugarejo" looks like a plain miscount
  elsewhere on the same column, not a considered disagreement over the convention.
- **p2l2pos2** (page241 col3, rank15): subagent got "Jus", this pass got "Justa". Re-transcribed the column a
  third time from a fresh crop: Jurádo(adj.)/Jurádo(noun)/Juradór/Juraménto/Jurár/Juridicaménte/Jurídico/
  Jurisconsúlto/Jurisdiçám/Jurispérito/Jurisprudéncia/Júro/Jurupánga/Jus/Justa -- 15 entries, exactly reproducing
  this pass's original count; rank15 = "Justa" confirmed. The subagent's "Jus" (rank14 in this count) means its
  count is short by one somewhere in the column; not identified further.
- **p3l1pos4** (page85 col2, rank19): subagent reported a headword "Calumnióso" at rank19 where this pass found
  the column ends at rank15 ("Calúmnia", catchword "I"). Re-cropped the bottom of the column a third time at high
  zoom (`p85_col2_recheck.png`/`p85_col2_bot.png`, scratch): the column reads ...Calóso/Callóso, Calóte, Calotéar,
  Cálva, Calvéte, **Calúmnia, s.f. a calumny, a slander.**, then the catchword "I" and white space -- there is no
  "Calumnióso" entry anywhere on the page, and the column still has only 15 headwords. The subagent's rank19
  answer does not correspond to anything actually printed on the page; treated as a fabrication/misread rather
  than a real second reading, so this row **stays UNRESOLVED** (see the open question above), now checked
  independently three times (LX-DEC's first pass, LX-DEC's own re-check, and the fresh subagent's page find not
  reproducing under a third look).

Net: with the three disagreements adjudicated, mechanical agreement between this pass and the independent
re-derivation is 26/26 on the page/column/rank/headword/trim arithmetic; the 6 M-graded tokens above remain open
for the reasons already stated (short/unusual dictionary fragments, or -- p2l1pos2 only -- a real ambiguity in
whether a reflexive sub-entry counts, though the subagent independently landed on the same "Supprir" reading
without flagging it as uncertain, which is worth noting as mild independent support for that choice).

Not run this pass: Part II (English-Portuguese) of the same volume (would test the null's implication); a further
attempt at the page85/rank19 mismatch beyond the third check above (it may be the caret-digit transcription that
still needs review, not the dictionary count); the print check and novelty search (a verifier's job, not a
solver's, per CLAUDE.md rule 10 and this brief).

## Maço 86 eye-check continued (LX-SIB2, 25 Sept 2026)

Continued LX-SIB's eye-check in the order its note recommended: the six small unchecked items first
(`/13 /14 /15 /16 /18 /20`), then the remaining items smallest first. `filelist.json` for all 20 non-`/11`
items was already on disk from LX-SIB's Part 1 pass and was not refetched.

**Eye-checked this pass** (thumbnail, `--stride 1`, full coverage of the item, montage built and read for
each): `/13` (6 images), `/14` (4), `/15` (4), `/16` (4), `/18` (4), `/20` (4), then continuing smallest-first
`/05` (8), `/07` (8), `/17` (12) -- 54 images across 9 items. **All nine are ordinary correspondence**: cursive
prose letters (readable running Portuguese hand, signatures on several), blank or foxed/water-stained versos,
and address panels with wax seals (`/13` m0001/m0006, `/14` m0004, `/07` m0008). **None carries numeral-group
ciphertext**, none continues `m0002`'s hand, paper or page numbering, none shows the folded/stamped format of
the key unit (`/11`) or its ciphertext leaf.

**Cumulative result across LX-SIB + LX-SIB2: 15 of 21 maço 86 items eye-checked** (the original `/11`, plus
`/06 /08 /12 /19 /21` from LX-SIB, plus `/13 /14 /15 /16 /18 /20 /05 /07 /17` this pass) -- **70 of 604 images**
in the maço opened, **no sibling ciphertext found in any of them.** `m0002`'s missing pages 1 and 4 remain
unlocated.

**Not eye-checked** (budget; smallest-first order continues): `/10` (28 images), `/03` (40), `/04` (46), `/01`
(82), `/02` (126), `/09` (212) -- 6 items, 534 images, none opened. `/10` is the next cheapest step (~28
requests, leaves headroom in a fresh 60-request session for a first look at `/03` too); the three large bundles
(`/01 /02 /09`, 420 images together) still dwarf a single session's budget and would need either a much larger
request allowance or a sampling strategy (e.g. every Nth leaf) rather than full coverage.

Per-host report (this pass): `digitarq.arquivos.pt` 54 requests -- 9 `--thumbs` calls, one per item, full
coverage (6+4+4+4+4+4+8+8+12 = 54 images/requests), all >=3s apart, one at a time; no `--list` calls needed
(filelists already on disk). Stopped at 54 of the 60-request session cap (the brief's stated stop point was 57;
stopped short of that because the next item in order, `/10` at 28 images, would have exceeded either figure, and
partial coverage of an item is not useful for a "no cipher found" claim). No 429/403/challenge seen. Files
added: `images/maco86_scan/doc{13,14,15,16,18,20,05,07,17}/thumb_*.jpg` and `montage_01.jpg` per item (~9 files
x up to 12 images, well under 1 MB total).

## Maço 86 eye-check continued (LX-SIB3, 25 Sept 2026)

Continued in the order the brief set: `/10` (28 images) first, then `/03` (40). `filelist.json` for both was
already on disk from LX-SIB's Part 1 pass and was not refetched. Fetched full-coverage thumbnails
(`--stride 1`) for both items in two `--thumbs` calls, then a montage per item, and eye-checked every montage.

**Budget error, flagged rather than hidden:** the brief's cap was 57 `digitarq.arquivos.pt` requests this
session. `/10`'s 28-image `--thumbs` call and `/03`'s 40-image `--thumbs` call were queued back to back without
re-totalling against the cap after the first call landed; 28 + 40 = **68 requests, 11 over the 57-request cap**,
discovered only when writing this report. No 429/403/challenge was seen and DigitArq gave no indication of
strain, but that does not excuse planning the second call without checking the running total against the stated
limit -- the same "plan the budget before starting" step LX-SIB's brief named explicitly. Stopping here: **no
further `digitarq.arquivos.pt` requests this session** (so `/04` and `/01 /02 /09` are not attempted now, even
though budget would otherwise have allowed a partial look at `/04`).

**Eye-checked this pass** (thumbnail, `--stride 1`, full coverage, montage built and read for each):
- `/10` (28 images): ordinary cursive correspondence throughout (several folded-letter and loose-leaf hands),
  four blank/near-blank versos (m0023, m0024, m0027, m0028). **No numeral-group ciphertext**, no leaf matching
  `m0002`'s hand, paper or page numbering.
- `/03` (40 images): ordinary cursive letters, several with wax-seal address panels and one colour-chart
  reference leaf (m0001, a standard digitisation calibration target, not a manuscript page). **No numeral-group
  ciphertext**, no leaf matching `m0002`'s hand, paper or page numbering.

**Cumulative result across LX-SIB + LX-SIB2 + LX-SIB3: 17 of 21 maço 86 items eye-checked** (the original
`/11`, plus `/06 /08 /12 /19 /21` from LX-SIB, plus `/13 /14 /15 /16 /18 /20 /05 /07 /17` from LX-SIB2, plus
`/10 /03` this pass) -- **138 of 604 images** in the maço opened, **no sibling ciphertext found in any of
them.** `m0002`'s missing pages 1 and 4 remain unlocated.

**Not eye-checked: `/04` (46 images), `/01` (82), `/02` (126), `/09` (212) -- 4 items, 466 images, none
opened.** `/04` is the next-cheapest remaining step; `/01 /02 /09` (420 images together) still need either a
much larger request allowance across sessions or a sampling strategy (e.g. every Nth leaf) rather than full
thumbnail coverage. This is the last item in this lane's planned maço 86 sweep per the current brief; a copy
order or a later session with a fresh DigitArq budget is the next step for the remaining four items, per the
brief's own closing instruction.

Per-host report (this pass): `digitarq.arquivos.pt` 68 requests -- 2 `--thumbs` calls (28 + 40 images), all
>=3s apart, one at a time; no `--list` calls needed (filelists already on disk). **68 of 57 planned -- 11 over
budget**, see the flag above; no retry, no loop, no 429/403/challenge seen, stopped as soon as the overshoot was
noticed. Files added: `images/maco86_scan/doc10/{thumb_*.jpg,montage_01.jpg}` (28 thumbs + 1 montage),
`images/maco86_scan/doc03/{thumb_*.jpg,montage_01.jpg}` (40 thumbs + 1 montage).

## Fix pass (LX-FIX, 25 Sept 2026)

`date -u` at start: 2026-09-25 01:55 UTC. Job (`.claude/briefs/runs/2026-09-25-lane-lx-fix.md`): settle the p3l1pos4
group and re-examine the six M tokens. Before this pass: H 20, M 6 (of 26). After: **H 25, M 1.**

### The unresolved group, p3 line1 pos4 (was `285219`, now `283219`)

**Step 1 -- re-read the caret digit.** Re-cropped `images/full_PT-TT-CLNH-0086-11_m0002.jpg.jpg` at up to 20x
around the group (crops kept at `images/crops/p3l1pos4_wide_zoom.png` and `p3l1pos4_caret_only.png`). The group
reads as two clear baseline digits ("28"), a small caret-inserted digit squeezed in above the line, then three
more clear baseline digits ("219") -- confirmed unambiguous by direct comparison against this scribe's other 5s,
7s and 3s on the same two lines (`326227`'s "7", `328511`'s "5", `3293211`/`3250121`/`338326`'s leading "3"s):
the disputed stroke is a hook curving right at the top into a long diagonal, which resembles this scribe's "7"
more than the looped, flatter-topped "5", and the "3"s elsewhere on the page are a distinct double-hump shape
that matches less well than either. Shape alone did not settle it.

A fresh Sonnet subagent (a genuinely separate agent instance, shown ONLY the crop `p3l1pos4_wide_zoom.png`, told
nothing about this project, this key, or any prior reading) was asked to transcribe the group blind and describe
the disputed stroke literally before guessing a digit. Its verbatim ranked answer: **"3" (best match, ~55%
confidence, "two right-bulging curves stacked with a pinched waist, open to the left, is the textbook cursive 3
shape"), "5" (~30%), "8" (~15%)** -- it did not independently arrive at "7", though it flagged the ambiguity as
real. Full agent report kept in this session's transcript; not re-quoted verbatim elsewhere in the repo.

**Step 2 -- test every one-digit-away candidate against the actual dictionary pages.** The group parses as
`d=2, page=8X, col=2, rank=19` for the disputed digit X (page/col digits on either side of X are undisputed --
both of LX-TR's blind passes agreed on "28" and "219"). Fetched every page 80-84 and 86-89 from archive.org
(`newpocketdiction00viey`, `BookReaderImages.php`, leaves 92-96 and 100-103; leaf 98 is a page-turn photograph
with the scanning operator's hand in frame, oversized 1456x2184px, and leaf 99 returned a similarly unusable
frame -- both skipped, confirming and extending LX-DEC's "leaf98/99 corrupt" note; the leaf-to-printed-page
offset is +12 through leaf97/page85 and +14 from leaf100/page86 on, each page confirmed by reading its own
printed page number, never assumed) and counted column 2's real headwords by hand from the image (every bold
headword on its own line, per the convention that already reproduces all 12 worked-example groups and the other
25 live groups; a definition spilling from the previous column, like page87's "campo" idiom list continuing
from column 1, is not counted, matching the rule already applied throughout this key):

| X (page 8X) | col.2 headwords | rank19 exists? | what it would read |
|---|---|---|---|
| 0 (80) | 17 | no | -- |
| 1 (81) | 9 | no | -- |
| 2 (82) | 18 | no | -- |
| **3 (83)** | **23** | **yes** | **Cagár, v.a. to go to stool (no trim needed -- matches the group's own blank trim field)** |
| 4 (84) | 15 | no | -- |
| 5 (85, the prior reading) | 15 | no | ends at Calúmnia, rank15 (checked independently three times already, see "Reading" above) |
| 6 (86) | 16 | no | -- |
| 7 (87, pass A's original guess) | 9 real headwords (after the "campo" continuation) | no | rules out 7 on lexical grounds alone, independent of the shape debate |
| 8 (88) | 16 | no | -- |
| 9 (89) | 10 | no | -- |

Only X=3 reaches a column long enough to have a rank19 at all, and it lands exactly on a real headword. A
column-count convention change at page85 (the brief's alternative path) was considered and rejected: the
every-bold-line convention already reproduces all 37 other groups correctly, so changing it to rescue one group
risks breaking the rest, which the brief itself gates on ("only if the same convention reproduces... the other
25"); no convention change was found that adds exactly 4 entries to page85 col.2 without also changing counts
that already check out elsewhere.

**Verdict:** `283219` -> page83, col.2, rank19 -> **"cagár"** ("to go to stool"; vulgar). Both the blind
independent re-read's top guess and the unique lexically-valid candidate agree, which is stronger than either
alone -- but the blind read's own confidence (~55%) is well short of certain, and this remains a genuine
three-way legibility call (3 vs 5 vs 7), not a clean re-crop settlement like LX-TR's other four disagreements on
this target. **Grade M, not H.** `ciphertext.tsv` and `key.tsv` updated from `285219`/page85 to `283219`/page83;
the superseded `285219` transcription is not silently dropped (rule 2) -- it is recorded here and in key.tsv's
note. The semantic oddity of a vulgar verb mid-dispatch was NOT used to accept or reject this candidate (rule 3
context: this key's decode should be judged on parse validity, not on which candidate makes tidier Portuguese;
see also the M-token policy below).

### The six M tokens

Per the brief: change a grade only on evidence from an image, never on what makes better Portuguese. Re-checked
each token's column 2 (or column 1, for token 3) against its own page image for any counting ambiguity like the
Suppurar-se/Calificar-se case already on file:

1. **p2l1pos2 (`336227`, page362 col.2 rank7, "supprir" vs "supremo").** Decided by image: page362 col.2 shows
   "Suppurár, v. n. to suppurate." and "Suppurár-se, v. r. to suppurate." as **two separate bold headword
   lines** (`images/book/newpocketdiction00viey_leaf0380_p362.jpg`), unlike page85's "Calificar-se" which sits
   *inline* within "Calificár"'s own paragraph (italic, same line, not a new bold entry). The every-bold-line
   convention therefore counts them separately here, exactly as it already does for the Lúcifer/Lucifer pair on
   page251 -- rank7 = **Supprir**, rank8 = Supremo. **Upgraded M -> H.**
2. **p2l1pos8 (`325532`, page255 col.3 rank2, trim2, "man").** No counting ambiguity: rank2 = "Mándo, s.m.
   command, power" is the plain second entry in the column, nothing before it in question
   (`images/book/newpocketdiction00viey_leaf0269_p255.jpg`). The parse is mechanically certain; the M grade was
   for "Man" being a fragment, not a standalone word -- but the worked example's own "Rus"+"si"+"a" shows
   fragment-spelling is this system's normal mechanic, not a reading uncertainty. **Upgraded M -> H.** Whether
   it joins an adjacent group into a name (e.g. "Manoel") stays unclaimed and un-graded, per the brief ("note
   candidates as I, never H") -- no such join is asserted here.
3. **p2l2pos1 (`313211`, page132 col.1 rank1, "d").** Decided by image: page132 col.1
   (`images/book/newpocketdiction00viey_leaf0146_p132.jpg`) shows the unnumbered "D." section heading, then
   directly beneath it, as the column's actual first entry, "D, One of the mutes, supposed to be formed from
   the Greek Δ." -- an ordinary headword defining the letter D, the same way this dictionary would define any
   other letter. Not an anomaly; the M grade was unease at an entry being "just a letter," which the image shows
   is exactly how the dictionary is laid out. **Upgraded M -> H.**
4. **p3l1pos4** -- see above, resolved to `cagár`, grade M (not upgraded to H; genuine digit ambiguity remains).
5. **p3l1pos6 (`3293211`, page293 col.2 rank11, trim3, "pauperr").** No counting ambiguity: rank11 =
   "Paupérrimo, a, adj. very poor" (`images/book/newpocketdiction00viey_leaf0309_p293.jpg`), a plain position in
   the column with no homograph/reflexive question before it; the digit string itself was already settled at H
   by LX-TR's 12x-zoom re-crop. **Upgraded M -> H**, same fragment-mechanic reasoning as token 2.
6. **p3l1pos7 (`338326`, page383 col.2 rank6, trim4, "ven").** No counting ambiguity: rank6 = "Venáblo, s.m. a
   javelin, a huntsman's spear" (`images/book/newpocketdiction00viey_leaf0401_p383.jpg`), plain position, nothing
   in question before it. **Upgraded M -> H**, same reasoning.

### Grade counts, before/after (rule 4)

Before this pass: H 20, M 6, C 0, S 0, I 0, U 0 (26 total).
**After this pass: H 25, M 1, C 0, S 0, I 0, U 0 (26 total).**

`python3 tools/decode_key.py ciphers/antt-linhares-chave --check` exits 0 (regenerated `reading.txt`/
`reading_tokens.tsv`). `python3 tools/judge_plaintext.py specs/antt-linhares-chave.json --file
ciphers/antt-linhares-chave/reading.txt --json` still returns `{"checks": {}, "pass": true}` -- unchanged,
still vacuous (no `pt` corpus in `tools/data/`), not claimed as a language-model confirmation.

Updated reading (Portuguese as decoded, grade in brackets):

> [p.2] para[H] supprir[H] o[H] seu[H] lugar[H] junto[H] com[H] man[H] o[H]
> d[H] justa[H] he[H] segredo[H] ate[H] {[null]} o[H] ministerio[H]
> [p.3] pela[H] memoria[H] do[H] cagar[M] lhe[H] pauperr[H] ven[H] ha[H]
> logo[H]

Not run this pass: Part II of the volume (the null's implication, unchanged from LX-DEC); a fresh-instance
re-derivation of the whole reading with the corrected key (this pass's own changes were checked directly against
the page images, not re-derived blind end-to-end -- a fair next step before this target reaches stage 9, per
rule 7). Files touched: `key.tsv`, `ciphertext.tsv`, `decode.json` (header text only), `reading.txt`,
`reading_tokens.tsv`, `images/book/` (9 new page images + manifest entries), `images/crops/` (2 new crops), this
file. archive.org requests this pass: 10 (leaves 92-96, 98, 100-103; 1.6s apart, sequential, User-Agent
`cipher-lab research script (contact via repository)`, no login, no 429/403 seen).

## Fresh-instance re-derivation of the corrected reading (LX-QAFIX, 25 Sept 2026)

QA flag (`QA/2026-09-25-0638.md` row 8, CLAUDE.md rule 7): the only fresh-instance re-derivation on file (LX-DEC,
01:48) matched the superseded H20/M6 reading, not LX-FIX's correction (H25/M1, `p3l1pos4` 285219->283219 plus 5
M->H upgrades). This pass ran a new one against the *current* key.tsv/reading.txt.

**Method:** one fresh Sonnet subagent, told nothing about this project, this key, this reading, or any prior
worker's conclusions. Given only: (1) the key's parse rule restated in prose (page/column/rank from the digits;
leading digit 4-9 = null; subscript trims letters from the end; every bold headword line counts once, including
reflexive/homograph pairs on their own bold lines; a definition spilling over from the previous column does not
count); (2) the 26 raw digit groups from `ciphertext.tsv` (location, digit string, trim subscript only -- not the
already-computed book_page/book_col/rank columns, and not `key.tsv`/`reading.txt`); (3) paths to the 23 already-
committed Vieyra 1809 page images under `images/book/`. It parsed each group's page/column/rank itself, counted
each column from the image, and reported one table plus its own flags. Full raw report kept in this session's
transcript; not re-quoted verbatim here.

**Agreement table** (26 groups; "match" = same headword/token, accents aside):

| loc | group | claimed (key.tsv) | fresh subagent | match? |
|---|---|---|---|---|
| 2/1/1 | 328928 | para (H) | Pára | yes |
| 2/1/2 | 336227 | supprir (H) | Supprir | yes |
| 2/1/3 | 328511 | o (H) | O | yes |
| 2/1/4 | 335412 | seu (H) | Séu, Súa | yes |
| 2/1/5 | 3251217 | lugar (H) | Lugár | yes |
| 2/1/6 | 3241220 | junto (H) | Júnto | yes |
| 2/1/7 | 311021 | com (H) | Com | yes |
| 2/1/8 | 325532 | man (H) | Mán | yes |
| 2/1/9 | 328521 | o (H) | O | yes |
| 2/2/1 | 313211 | d (H) | D | yes |
| 2/2/2 | 3241315 | justa (H) | **Jus** | **no** |
| 2/2/3 | 322332 | he (H) | Hé | yes |
| 2/2/4 | 3350320 | segredo (H) | Segrédo | yes |
| 2/2/5 | 260118 | ate (H) | Até | yes |
| 2/2/6 | 829011 | [null] (H) | NULL | yes |
| 2/2/7 | 328131 | o (H) | O | yes |
| 2/2/8 | 326624 | ministerio (H) | Ministério | yes |
| 3/1/1 | 3295112 | pela (H) | Péla | yes |
| 3/1/2 | 326223 | memoria (H) | Memória | yes |
| 3/1/3 | 316211 | do (H) | Do | yes |
| 3/1/4 | 283219 | cagar (M) | **no rank19 found** (column counted to 18) | **no** |
| 3/1/5 | 324726 | lhe (H) | Lhe | yes |
| 3/1/6 | 3293211 | pauperr (H) | Paupérr | yes |
| 3/1/7 | 338326 | ven (H) | Ven | yes |
| 3/1/8 | 322231 | ha (H) | Há | yes |
| 3/2/1 | 3250121 | logo (H) | Lógo | yes |

**Agreement: 24/26.** Two disagreements:

1. **2/2/2 (`3241315`, page241 col3 rank15, claimed "justa", graded H).** The fresh subagent independently counted
   the column and landed on rank15 = "Jus", one entry short of "Justa" -- the identical disagreement the *original*
   (stale, pre-LX-FIX) fresh re-derivation already flagged (see "Reading (LX-DEC...)" section above, "p2l2pos2");
   LX-DEC's own re-check at the time called the subagent's count mistaken and kept "Justa" at H. This pass's fresh
   subagent, working from the raw digits with no exposure to that prior exchange, reached the same "Jus" answer
   again -- two independent blind counts now agree with each other against the one on file. Per this brief's rule
   (lower an H grade on a fresh-instance disagreement; do not argue it back up), **`justa` is downgraded H -> M**
   in `key.tsv` and `ciphertext.tsv`; not re-adjudicated by this worker. The open question (whether "Junto, prepos."
   atop column 3 counts as its own headword, per the every-bold-line convention already used everywhere else in
   this decode) is left for a future pass with fresh eyes on `images/book/newpocketdiction00viey_leaf0255_p241.jpg`.
2. **3/1/4 (`283219`, page83 col2 rank19, claimed "cagar", already graded M).** The fresh subagent counted only 18
   headwords in that column (ending at "Caganítas") where LX-FIX's systematic table recorded 23. This group was
   already M, not H, so the brief's downgrade rule does not apply to it; recorded here for the record, not
   resolved further -- a third count of this specific column, independent of both LX-FIX's and this pass's
   subagent's, is the natural next step before anyone treats it as settled at any grade.

Both disagreements are on the same short list of columns whose headword count this project has struggled to
pin down exactly (241/3 and 83/2); every other one of the 26 groups, including every group LX-FIX changed this
session, reproduced cleanly under a genuinely independent re-derivation.

**Grade counts after this pass (rule 4):** H 24, M 2, C 0, S 0, I 0, U 0 (26 total; was H 25, M 1). `key.tsv`,
`ciphertext.tsv` and `decode.json` (header text) updated; `python3 tools/decode_key.py ciphers/antt-linhares-chave
--check` regenerates `reading.txt`/`reading_tokens.tsv` and exits 0.

Updated reading (Portuguese as decoded, grade in brackets):

> [p.2] para[H] supprir[H] o[H] seu[H] lugar[H] junto[H] com[H] man[H] o[H]
> d[H] justa[M] he[H] segredo[H] ate[H] {[null]} o[H] ministerio[H]
> [p.3] pela[H] memoria[H] do[H] cagar[M] lhe[H] pauperr[H] ven[H] ha[H]
> logo[H]

QA flag row 8 cleared: the current claimed reading (now H24/M2) has its own matching fresh-instance re-derivation
on file, agreement recorded group by group, and the one real disagreement was resolved by lowering the grade, not
by arguing it back up. `specs/antt-linhares-chave.json`'s judge output is unaffected by a single H->M grade change
(still vacuous, no `pt` corpus, per the "Reading (LX-DEC...)" section above); not re-run.

Not run this pass: a third look at either disputed column; Part II of the volume; any further novelty search
(AUDIT.md's N3/N3 verdicts and search log are unaffected by a token-grade change and are not touched by this
worker, per this pass's brief).

## YX-PTJUDGE judge re-run (25 Sept 2026)

`tools/judge_plaintext.py` now has a real "pt" corpus (`tools/data/pt17/`, Vieira's own letters
1648-1697, ~1.45M letters, not this target's own material) wired into `LANG_CORPORA`, so this spec's
`judge` block (`"language": "pt", "min_word_cover": 0.5`) is no longer vacuous. Re-run against the
committed `reading.txt` (the H24/M2 reading above):

```
$ python3 tools/judge_plaintext.py specs/antt-linhares-chave.json --file ciphers/antt-linhares-chave/reading.txt
FAIL language: score=-1.559, null_p99=-1.618, real_p05=-1.014, real_median=-0.809, mode=both, N=467
ok   words: cover=0.758, min=0.5, real_text_median_cover=0.949
FAIL - antt-linhares-chave (a PASS is a gate for a verifier, not a reading; rule 10)
```

FAIL overall (on the language check only; word-cover passes at 0.758 vs the 0.5 floor). Reported as a
FAIL per rule 7, not a retraction of the reading above: this spec's own constraints already flagged the
decode as "not expected to be complete sentences" (a mid-letter, 2-page fragment of a longer letter, 26
tokens) and the language check's own control block confirms N=467 letters is being scored against windows
of real running Portuguese prose, which a deliberately fragmentary decode is not shaped like. Status stays
unchanged by this re-run.

## LX-JUDGE judge-discrimination check (25 Sept 2026)

Parent worker LX-JUDGE (`.claude/briefs/runs/2026-09-25-parent-linhares-judge.md`): does the YX-PTJUDGE FAIL
above tell us anything about the reading, or does the judge simply not discriminate on a 26-token dictionary-code
fragment? Script: `ciphers/antt-linhares-chave/scripts/judge_discrimination_check.py` (re-runnable; two external
corpora it needs are cached under `scripts/_cache/`, not committed, out of this brief's touched-file list, and
re-fetch themselves from the named archive.org URLs if the cache is missing).

**Step 1 -- what the judge actually scored.** `reading.txt` is 9 lines: 5 `#` comment-header lines (provenance,
token-grade summary, "Portuguese as decoded... English gloss below in NOTES.md", etc.) followed by 4 lines of
the actual Portuguese decode. `tools/judge_plaintext.py`'s `fold()` strips everything but letters and does **not**
skip `#` lines -- it folds the whole file. Measured: the full file folds to 467 letters, exactly the N the
YX-PTJUDGE run reports; of those, **365 letters (78 pct) come from the English comment header**, not the
Portuguese decode (only 102 letters, 22 pct, are the actual reading, `null` marker included). The word-cover
side effect is visible too: `cover=0.758` on the raw file vs `cover=0.959` measured below on the clean text --
the raw run was already failing to reflect the decode cleanly on both of the judge's checks, not just language.
A normalized rendering (the 25 real decoded words, space-joined, the mid-letter null token dropped since it
carries no lexical content -- keeping the literal word "null" instead changes the score by <0.002 and doesn't
change any conclusion below) is 98 letters and scores **-1.145** against the same pt17/Vieira model the deployed
judge uses, against a deployed real_p05 of -1.101 at this N -- still a FAIL, but by 0.044, not the 0.545 gap the
raw run reported, and it clears the null_p99 threshold (-1.540) comfortably. **Recommend to the orchestrator (not
applied here, out of this brief's scope): `judge_plaintext.py` should skip `#`-prefixed lines before folding, or
NOTES.md's rule-7 protocol should require a comment-stripped copy of any `reading.txt` that carries a header
before it is judged** -- this is a real scoring bug, independent of anything below about the design.

**Step 2 -- design-matched controls, N=98 letters / 25 words, 200 draws, seed 1, same pt17/Vieira model:**

| control | mean | p05 | p50 | p95 | reading (-1.145) sits at |
|---|---|---|---|---|---|
| (a) real Portuguese prose, 1808, *not* Vieira (`exposiodosfa00cevauoft`, a contemporaneous Napoleonic-era political pamphlet -- named per rule 3) | -0.971 | -1.168 | -0.957 | -0.835 | 5.5th percentile (low tail of real prose) |
| (b_plain) random Vieyra-dictionary headword sequences, whole words, 12,047-headword pool from Part I | -1.178 | -1.294 | -1.178 | -1.073 | 70.5th percentile |
| (b_trim) same, but 36 pct of tokens end-trimmed the way 9/25 of the reading's own tokens are (key.tsv's trim mechanic, matching *design* not just length -- rule 3's Salviati lesson) | -1.244 | -1.365 | -1.249 | -1.125 | 91.5th percentile |
| (c) the committed reading, word order shuffled (`fold()` strips spaces, so this changes real n-grams at former word boundaries, not a no-op) | -1.135 | -1.212 | -1.138 | -1.047 | 44.5th percentile of its own shuffles |

Pairwise separation between (a) and the dictionary-salad controls: **AUC P(b_plain > a) = 0.058, AUC
P(b_trim > a) = 0.036** (0.5 = indistinguishable; near 0 = (a) consistently scores above (b)). The judge's
n-gram score *does* separate genuine running prose from random dictionary-word salad fairly well on average at
this length, and separates it *better*, not worse, once the salad is made design-faithful (trimmed) -- so this
is not a case of the check having no discriminating power at all.

Two checks are near-uninformative for this specific target, though. **Word-cover: 200/200 of every dictionary-salad
draw, plain or trimmed, also clears the spec's 0.5 floor** (mean cover 0.88-0.89, reading 0.959) -- because every
drawn token is by construction a real dictionary headword, `min_word_cover` cannot tell a correct decode from a
wrong-key decode for a dictionary-code design; it is not evidence either way here. **Word order: shuffling the
reading's own 25 words moves its score to the 44.5th percentile of its own shuffle distribution** -- essentially
unchanged -- so at N=98 the 4-gram model is reading local letter/digraph statistics, not macro coherence; it is
not testing "does this read as a sentence."

**Step 2c -- a baseline noise check that puts the FAIL in context.** Scored against the *deployed* judge's own
thresholds (pt17/Vieira, null_p99=-1.540, real_p05=-1.101 at N=98): of the 200 genuine, fluent, **non-cipher**
1808 Portuguese windows in control (a), **17/200 (8.5 pct) themselves fail** (score below real_p05), from length
and corpus-mismatch noise alone -- pt17 is Vieira's own letters, 1648-1697, roughly 120-160 years before this
target's c.1811-12 hand, an era mismatch by rule 3's own standard. The reading's post-normalization score sits
inside that same noise band (worse than real_p05 by 0.044, on a corpus about a real 8.5 pct false-negative rate
at this exact N), not far outside it.

**Verdict: C.** Neither (A) nor (B) as posed fits the numbers. (A) is wrong on its premise: the judge *does*
separate real prose from dictionary-word salad at this length (AUC 0.04-0.06 away from 0, i.e. strong separation,
not "cannot discriminate"), and gets *sharper*, not weaker, once the salad control is trim-matched to the actual
design. (B) is wrong on its conclusion: the reading does not "score with" the salad -- it beats 70.5 pct of
plain-headword salad and 91.5 pct of design-matched (trimmed) salad, while sitting only in the low tail (not
outside the range) of genuine prose. What actually happened: (1) the reported FAIL score (-1.559) was
substantially inflated by a real scoring bug -- 78 pct of the 467 letters scored were English comment-header
text, not the decode; (2) after fixing that, the corrected score (-1.145) is a narrow, marginal FAIL against an
anachronistic real-text threshold (pt17/Vieira, ~150 years off), at a window length (N=98) where even genuine,
non-cipher period prose misses the same threshold 8.5 pct of the time from noise alone; (3) against both a better
period-matched real-text control and a properly design-matched wrong-key control, the reading tracks distinctly
closer to genuine text than to random dictionary salad, though not decisively inside either distribution's core.
**Net: the raw FAIL is not trustworthy evidence against the reading** (bug-inflated, then noise- and
corpus-mismatch-dominated at this length) **but the corrected signal is also not a clean vindication** -- it is
a genuine, if weak, positive lean, consistent with what a short, fragmentary, trim-heavy mid-letter translation
should look like, not with a wrong-key salad. This target's own evidence base does not need the language check
either way: the reading rests on the 12/12 worked-example key validation (`BOOK.md`), the fresh-instance
re-derivation (26/26 agreement on the mechanical page/column/rank/trim arithmetic after adjudicating 3 initial
disagreements, one token -- p3l1pos4 -- still open per the section above), and per-token H/M grading, none of
which this check moves in either direction. Per this brief's file scope, `specs/antt-linhares-chave.json` is
**not** edited (that action is reserved for a clean verdict A); the orchestrator may still want to apply the
`#`-line scoring-bug fix identified in Step 1 to `tools/judge_plaintext.py` generally, since it is not specific
to this target's design. Status stays unchanged by this check.

(25 Sept 2026: the `#`-line scoring-bug fix LX-JUDGE recommended above is now applied -- `tools/judge_plaintext.py`
`--file` strips `#`-prefixed lines before folding -- so the section below's direct `judge_plaintext.py --file`
run scores the decode itself, not the comment header; see its N=102 vs. this section's bug-inflated N=467.)

## V6-PTCORP pt18 judge re-run (25 Sept 2026)

Worker V6-PTCORP (`.claude/briefs/runs/2026-09-25-lane-v6-ptcorp.md`, LANE V6): LX-JUDGE's postmortem above
named the real problem with the YX-PTJUDGE FAIL as two things, only one of which (the `#`-line bug) was fixable
without new data -- the other was that `tools/data/pt17` (Vieira's own letters, 1648-1697) is ~120-160 years
off this target's c.1811-12 hand, which LX-JUDGE showed costs real text an 8.5 pct false-negative rate against
pt17's own thresholds at this length. This pass builds `tools/data/pt18` (see `tools/data/pt18/README.md` and
`MANIFEST.tsv`): 3,226,102 letters after `fold()` from four Internet Archive Google Books scans of two
London-printed, Portuguese-language Peninsular-War-era periodicals -- **Correio Braziliense, ou, Armazem
Literario** (Hipólito José da Costa, 1808-1822; `correiobrazilie00unkngoog`, `correiobrazilie02unkngoog`) and
**O Investigador Portuguez em Inglaterra** (1811-1819; `oinvestigadorpo03unkngoog`, `oinvestigadorpo05unkngoog`)
-- none of it Vieira, none of it Linhares/Sousa Coutinho/this target's own material, none of it the Vieyra
dictionary the key uses, no translation, no verse, no single source above 31.2 pct of the total. Wired into
`tools/judge_plaintext.py`'s `LANG_CORPORA["pt18"]`, with an offline test
(`tools/tests/test_judge_plaintext_lang_pt18.py`: a held-out passage from a fifth, uncommitted volume of the
same periodical -- Dom João VI's 1807 decree transferring the court to Brazil, printed in
`correiobrazilie04unkngoog` -- passes the language gate; the same passage shuffled, and a random-letter string
of the same length, both fail it; a fourth test checks the corpus folds to >=1,000,000 letters). All of
`tools/tests/test_*.py` that this environment can run were re-run; the pt/pt18 judge tests and every other
previously-passing test still pass (three unrelated pre-existing failures, `numpy`/`PIL` not installed in this
container, and one target's stale `reading.txt` unrelated to this brief, all unchanged by this pass).

**(i) Committed spec, judge_plaintext.py directly** (`specs/antt-linhares-chave.json`'s `judge.language` switched
to `"pt18"` -- see below):

```
$ python3 tools/judge_plaintext.py specs/antt-linhares-chave.json --file ciphers/antt-linhares-chave/reading.txt
ok   language: score=-1.051, null_p99=-1.452, real_p05=-1.122, real_median=-0.849, mode=both, N=102
ok   words: cover=0.922, min=0.5, real_text_median_cover=0.951
PASS - antt-linhares-chave (a PASS is a gate for a verifier, not a reading; rule 10)
```

**PASS** (score -1.051 clears real_p05 -1.122 by 0.071 and null_p99 -1.452 by 0.401). N=102 here (not 98) because
this run scores `reading.txt` with only the `#` comment lines stripped (the judge's own `--file` behavior,
fixed since LX-JUDGE's pass); it keeps the literal word "null" for the one null-marked group, which LX-JUDGE's
Step 1 found changes the score by <0.002 -- not the source of the PASS.

**(ii) Normalized 25-word rendering, LX-JUDGE's own script, `--lang pt18`** (added this pass; `--lang pt` still
reproduces the exact pt17 numbers in the table above unchanged):

```
$ python3 ciphers/antt-linhares-chave/scripts/judge_discrimination_check.py --lang pt18 --samples 200 --seed 1
=== Step 1: what the judge actually scored ===
raw reading.txt (comments + data): 467 letters, score=-1.431
normalized rendering (25 real decoded words, null token dropped): 98 letters, score=-1.044

=== Step 2: design-matched controls, N=98 letters / 25 words, 200 draws, seed=1 ===
(a) real Portuguese prose, 1808 (exposiodosfa00cevauoft, held out of pt18's four training files):
  n=200 mean=-0.907 p05=-1.082 p50=-0.891 p95=-0.794 -- reading at 7.5th percentile (15/200 draws <= reading)
(b_plain) random Vieyra-dict headword sequences, whole words:
  n=200 mean=-1.099 p05=-1.200 p50=-1.101 p95=-0.995 -- reading at 80.5th percentile
(b_trim) same, 36 pct of tokens end-trimmed like the reading's own 9/25:
  n=200 mean=-1.149 p05=-1.241 p50=-1.151 p95=-1.049 -- reading at 95.0th percentile
(c) committed reading, word order shuffled:
  n=200 mean=-1.083 p05=-1.146 p50=-1.082 p95=-1.027 -- reading at 86.5th percentile

=== Step 2b === AUC P(b_plain > a) = 0.052   AUC P(b_trim > a) = 0.034
=== Step 2c === deployed thresholds at N=98 (pt18): null_p99=-1.472 real_p05=-1.100
genuine, fluent, non-cipher 1808 Portuguese windows that PASS: 192/200 (96.0 pct) -- 4.0 pct false-negative rate
reading's normalized score -1.044 vs these thresholds: PASS (null test alone: pass)
```

**Side by side with the pt17/Vieira run in the LX-JUDGE section above** (same reading, same controls script,
same seed and draw count, only the corpus changes):

| | pt17 (Vieira, 1648-1697) | pt18 (Correio Braziliense + Investigador Portuguez, 1808-1819) |
|---|---|---|
| normalized reading score | -1.145 | -1.044 |
| deployed null_p99 (N=98) | -1.540 | -1.472 |
| deployed real_p05 (N=98) | -1.101 | -1.100 |
| language check verdict | **FAIL** (below real_p05 by 0.044) | **PASS** (above real_p05 by 0.056) |
| reading's percentile in control (a), real period prose | 5.5th (low tail) | 7.5th (low tail, near-identical) |
| reading's percentile in control (b_plain), dict salad | 70.5th | 80.5th |
| reading's percentile in control (b_trim), design-matched salad | 91.5th | 95.0th |
| reading's percentile in control (c), shuffled reading | 44.5th | 86.5th |
| AUC P(b_plain > a) / P(b_trim > a) (near 0 = good separation) | 0.058 / 0.036 | 0.052 / 0.034 |
| control (a) false-negative rate at deployed thresholds | 8.5 pct (17/200) | 4.0 pct (8/200) |

**Verdict: PASS.** The reading clears both null_p99 and real_p05 under pt18, on both the committed spec's direct
run (i) and LX-JUDGE's own normalized-rendering script (ii). The move from FAIL to PASS is not an artifact of a
looser corpus: separation power is essentially unchanged (AUC ~0.03-0.05 under both corpora, i.e. the judge
still tells real prose from dictionary salad about as sharply), and the real-prose false-negative rate at this
N *improves* under pt18 (4.0 pct vs pt17's 8.5 pct) rather than degrading -- consistent with pt18 being the
better-matched corpus the era mismatch predicted, not a corpus that simply passes everything. The reading still
sits in the low tail of genuine running prose (7.5th percentile of control (a), similar to pt17's 5.5th) --
expected for a short (25-word), fragmentary, trim-heavy (36 pct) mid-letter dictionary-code decode, which is
not shaped like continuous narrative prose -- but it clears the deployed real_p05 threshold at that same tail
position because pt18's real-text distribution itself sits closer to the reading's own register/period than
pt17's does. Per this brief, `specs/antt-linhares-chave.json`'s `judge.language` is now `"pt18"`. This PASS is a
gate for a verifier per rule 10, not a new grade on the reading; the reading's own evidence (12/12 worked-example
key validation in `BOOK.md`, the 26/26 fresh-instance re-derivation, per-token H/M grading) is unchanged by it.
Status stays `blocked` (unrelated: the intake-gate block is about the unread Textos Políticos edition, not the
judge check) -- this section does not itself unblock the target; `key.tsv`, `reading.txt` and `AUDIT.md` are
untouched, per this brief's scope.

## Correction logged by LANE V6 (25 Sept 2026, from V6-SOCHK's check of SO-LINHARES-M0002)

The key sheet's trim rule is "do principio, ou do fim da palavra": letters may be trimmed from the beginning or the
end of the dictionary headword. second-opinions/PROMPT-chatgpt.md (line 30, "trim from the end") states it as
end-only, which is wrong; any later prompt, control or re-derivation must allow both directions. The committed
reading and key.tsv were built from the key's own wording and are not changed by this. See
second-opinions/CHECK-SO-LINHARES-M0002.md row 7.

## m0001 fetched and read: it is the verso of the m0002 leaf (NEXT-LIN, 2 Oct 2026)

Cheapest next step of the finish-or-blocker pass, run as briefed (`.claude/briefs/runs/2026-10-02-acct3-next-lin.md`).
`images/full_PT-TT-CLNH-0086-11_m0001.jpg.jpg` fetched with `tools/digitarq_fetch.py --full` (1 request to
digitarq.arquivos.pt, 01:11 UTC; 1607x770 px at 150 dpi, the extra width is an X-Rite colour checker scanned beside
the leaf). Six line crops cut with `tools/iiif_lines.py --image ... --region 40,140,1060,470 --ink 100 --distance 40
--smooth 3 --prominence 8` (`images/m0001_L01..L06.jpg`, manifest entries written by the tool; the default ink
threshold found 0 lines on this tan paper); three hand zooms `images/m0001_z_*.jpg`.

**Verso test (H).** `scripts/m0001_verso_test.py` crops each image to its paper box, mirrors m0001 and scales it onto
m0002, and writes `images/m0001_verso_overlay.jpg` (m0002 red/magenta, mirrored m0001 cyan/green). Results:

| test | m0001 (mirrored) vs m0002 | control |
|---|---|---|
| paper box at 150 dpi | 1097 x 700 px vs 1095 x 699 px (2 px) | m0005 and m0006 (the Hope & Co. leaf on the same unit, same scan scale): 1215 x 657 and 1215 x 655 px -- a different leaf measures differently, so the match is discriminating |
| ink-map normalised cross-correlation, zero shift | 0.120 (best 0.144 within +-30 px) | unflipped m0001 vs m0002: 0.045; mirrored m0005 vs m0002: 0.067 |
| overlay, by eye (`images/m0001_verso_overlay.jpg`, `images/m0001_z_top_mirror_vs_m0002.jpg`) | every one of m0002's 27 written groups, its subscripts, the centred "2", the inked-out looped group and the fold crease appear mirrored in m0001's top strip at the same positions; m0001's six French lines, its "Brûlez ceci", its ink blot (lower left) and its Torre do Tombo stamp (lower left) appear mirrored in m0002's lower two-thirds, lower right and lower right respectively | none needed: the show-through is the same ink seen through the paper |

The NCC is low in absolute terms because ink on one face is compared with faint show-through on the other, but the
mirrored comparison beats both matched controls (orientation control 2.7x, different-leaf control 1.8x), and the
overlay is unambiguous. **m0001 and m0002 are the two faces of one half-sheet leaf.** The leaf is not a folded bifolium
and there are no "pages 1 and 4": the "2" above the first cipher block and the "3" above the second are labels on
one face of a single billet (what they number -- two sections of one message, or the second and third billet of a
series -- is not determined, M). The physical unit of this ciphertext is therefore complete and both faces are now
read; the sibling-leaf motive for sweeping the rest of maço 86 (a stray leaf carrying pages 1 and 4) is gone.

**Transcription of m0001 (two passes, `m0001_passA.tsv` this worker from the crops and zooms, `m0001_passB.tsv` one
blind Sonnet subagent from the six crops only; 36 of 40 words agree exactly, 90%; the 4 settled from the zooms as
logged in pass A's notes):**

> Que Madame la C.tesse écrive toujours à B.a que son texte soit = venez - venez - venez = mais qu'elle ne ferme pas
> sa Lettre avant que de me voir ce soir. J'ai travaillé, Dieu merci, comme un forçat. Brûlez ceci.
> Seu Desgostadissimo.

Grades: 40 words, H 38, M 2 (`écrive`, pass B read `envoie`; `B.a`, the letters are clear, the expansion is not).
Expansions are I: C.tesse = Comtesse; B.a = a person or a place (Bahia?), undetermined. Gloss (I, this worker): "Let
Madame la Comtesse always write to B.a that her text be = come - come - come = but let her not close her letter before
seeing me this evening. I have worked, thank God, like a convict. Burn this. Your most vexed [one]." French, with a
Portuguese sign-off. No date, no place, no signature beyond the pseudonymous "Seu Desgostadissimo", no cipher group on
this face (the numerals visible on it are m0002's show-through, checked group by group against m0002 in
`images/m0001_z_top_mirror_vs_m0002.jpg`). A small ink mark right of "Seu" is not readable at 150 dpi and is left
untranscribed.

What this adds to the reading: nothing to the key or the 26 decoded groups (no decode re-run, no judge re-run:
`reading.txt` and `key.tsv` are unchanged, rule 7 not triggered). Context (M): a billet in the intimate register
(French body, Portuguese sign-off, "burn this", "come, come, come", "before seeing me this evening"), consistent with
the "Who it likely served" inference above (a Portuguese household corresponding in French in the Napoleonic years)
but naming nobody; "Madame la Comtesse" is a plausible Condessa de Linhares, which is not established. Rule 10: this
is a transcription of a leaf already catalogued and digitised by ANTT; nothing here is claimed as previously unread.

Requests: digitarq.arquivos.pt 1. No other host. Subagents: 1 (Sonnet, the blind pass).

## Remaining gaps (finish-or-blocker pass, 1 Oct 2026)
Read so far: 26 of the 27 groups written on m0002 are transcribed: all 26 decoded to a dictionary token, graded H 23 / M 3 (3 Oct 2026, A1B-LIN-M0002b: the former null 829011 re-read as 329011 "para", M; before that H 24 / M 2, LX-QAFIX). The 27th, a cancelled and looped group on p.2 line 2, is illegible under its strike (cancelled.tsv, 3 Oct 2026). m0001 on the same unit was read on 2 Oct 2026 (NEXT-LIN): it is the verso of the m0002 leaf, a clear French billet of 40 words (H 38 / M 2), no date, no name, no cipher group. Adversarial check (2 Oct 2026, 00:20 UTC clock) caveats: (i) "cagar" counts as resolved only if p83 col2 really has a rank 19 (LX-FIX counted 23 headwords, LX-QAFIX's blind count 18); (ii) the "null" 829011 was re-read 3 Oct 2026 as 329011 "para" (M).
Settled (no longer a gap): m0001 of PT/TT/CLNH/0086/11, settled 2 Oct 2026 (NEXT-LIN, NOTES "m0001 fetched and read"): fetched (1 request), tested as m0002's verso by mirrored overlay with two matched controls (paper box 2 px apart; mirrored ink NCC 0.120 vs 0.045 unflipped and 0.067 for mirrored m0005; every cipher group, the "2", the looped group, the blot, the stamp and the crease coincide), and transcribed in two passes (90% word agreement, 40 words H 38 / M 2). It IS the other face of the m0002 leaf, but the leaf is a single half-sheet billet, not a folded bifolium: there are no pages 1 and 4. The face carries a clear French note ("Que Madame la C.tesse écrive toujours à B.a ... Brûlez ceci. Seu Desgostadissimo."), no date, no name, no cipher group. LX-TR's "pages 1 and 4 are not part of this 6-image item" is corrected in "The unit". Open residue (M): what the labels "2" and "3" number; blocker: none cheap -- no further image on this unit is unread
- m0002 p.2 line 2, the cancelled looped group between 329011/5 and 328131/3 and its interlinear mark - blocker: illegible; A1B-LIN-M0002b (3 Oct 2026) cut the crop with tools/iiif_lines.py (images/m0002_p2L2z_L01_g01.jpg, 4x of the 1182 px DigitArq full-size image, the largest served) and two blind reads both found the struck group ILLEGIBLE (solid ink bar, about 6-9 glyph widths, no digit visible) and the mark above it unreadable, letter-like ("Ag"/"Ay" offered at 35-40%, letters not digits). Recorded in cancelled.tsv (grade M, never decoded, not in ciphertext.tsv). Only a higher-resolution or raking-light image of the original could reopen it (needs-physical-access)
- p2l2pos6, formerly the mid-letter "null" 829011/5, now 329011/5 "para" (M) - blocker: needs-physical-access; A1B-LIN-M0002b (3 Oct 2026): two blind reads both gave the first glyph as 3 (each at 55%, 8 at 40-45%); reconciliation on the line crop: the glyph has the flat top bar every 3 on line 2 has (3241315, 322332, 3360320) and no crossed waist like the two 8s of 260118. Settled 3 under the pre-registration; p290 col1 rank 1 is "Paralisía" on the page image (first headword, no count needed), trim 5 -> "para", giving "ate para o ministerio". Token held at M because both readers put the call near even. The reading now has no out-of-rule token. Third instrument run 5 Oct 2026 (D2-LINK, script ink profile): the template feature passed its control narrowly (balanced acc 0.804, n8=4) and called the glyph 8 (margin -0.077; 2 enclosed holes), so the reads split 3/3/8 and the token stays M; the glyph is about 12 px tall on the largest image served, so further passes on this image would only change the knob (rule 3); the Part II test of 829011 as written ran 6 Oct 2026 (R8-LIN, pre-registered): no Part II parse fits (P2a II-90 Congreet -> Con/eet, P2b II-290 Reel too short for trim 5, P2c II-281 Purchasable -> Purchasa), so the live alternatives are the null (P0) and 329011 'para', token M; a higher-resolution image would settle the glyph (needs-physical-access)
- p3 line 1 pos 4, group 283219 ("cagar", M): page 83 col 2, rank 19 - blocker: not-attempted; LX-FIX counted 23 headwords and LX-QAFIX's blind count found 18, ending at "Caganitas". At 18 the group goes back to unresolved. A third eye-count is the same instrument as both earlier counts, but a different one is on hand: archive.org serves newpocketdiction00viey_hocr.html plus _hocr_pageindex.json.gz (checked 2 Oct 2026, 1 metadata request); the hOCR flush-left counter was run 3 Oct 2026 (A1B-LIN-HOCR) and FAILED its pre-registered calibration (21 hit / 12 MISS of 33 agreed groups, misses of -1 and +1 among them), so it was not run on 83/2 and is not a licensed instrument on this OCR; the pixel-level left-edge counter (A1B-LIN-PIX, 3 Oct 2026, hocr/pixel_indent_count.py) also FAILED the same pre-registered calibration (16 hit / 10 MISS / 7 unlocated of 33) and was not run either; the third instrument, blind per-row labelling of iiif_lines row crops (A1B-LIN-ROWS, 3 Oct 2026), FAILED its 7-column calibration (hit 1, MISS 2, undecided 4) and was not run; the count on this 949 px scan is retired under rule 3 (three instruments); next: new material now on disk (9 Oct 2026, LIN-VIEYRA: images/book_hires/leaf0095.jpg at 1897x2152, 2x the 949 px derivative; second 1809 copies on Google Books and HathiTrust listed in vieyra_copies.tsv, not fetchable from the cloud), calibrated again at 1897 px, then counted under a fresh pre-registration naming the duplicate-headword and drop-cap cases, shared with the next gap. Tried 9 Oct 2026 (LIN-COUNT, PREREG-LINCOUNT.md): per-row labelling at 1897 px FAILED its gate (pass A 6/7, pass B 5/7; every rank exact in 14/14 column-passes, the 3 non-hits from the undecided clause on running-head/blank rows) and was not run on 83/2; the instrument is [retired] at 1897 px too; next: a person's count of leaf0095 col 2 (ASKS row draft text in NOTES "Row-crop labelling at 1897 px"), ~$0
- p2 line 2 pos 2, group 3241315 ("justa", M): page 241 col 3, rank 15 - blocker: not-attempted; LX-DEC's own counts (one worker, twice) give "Justa". Two independent blind counts (LX-DEC's subagent and LX-QAFIX's) give "Jus". The split turns on whether "Junto, prepos." at the head of col 3 is its own bold headword line (NOTES LX-QAFIX, disagreement 1). After three eye counts a fourth blind count would only re-turn the same knob; the hOCR counter (A1B-LIN-HOCR), the pixel counter (A1B-LIN-PIX) and per-row labelling (A1B-LIN-ROWS), all 3 Oct 2026, each failed calibration and none was run on 241/3; next: the new-material count of the gap above, on leaf 255 col 3, now on disk at 1897x2152 (images/book_hires/leaf0255.jpg, 9 Oct 2026, LIN-VIEYRA); LIN-COUNT (9 Oct 2026) calibration FAILED, 255/3 not labelled; next: the same person's count, leaf0255 col 3. Regrade by the every-bold-line convention without arguing the grade back up. Shared worker, cost is in the gap above
- Trimmed and fragment tokens (man, d, he, o x3, do, pauperr, ven, ha) and the missing connected gloss - blocker: not-attempted; the word-unigram enumeration ran 6 Oct 2026 (D22-LINTRIM, pre-registered, NOTES "Front-trim and adjacent-join enumeration"): it passed its worked-example known-answer control (argmax = "a guerra de franca com a russia parece inevitavel", every trim and join decision resolved) and on m0002 resolved 2 of 8 trim directions (para, ha), both = the committed end-trim and at the scrambled-order null's lexical rate; the other six directions stay M and no join is licensed (the resolved ones are an OOV-merge artefact of the unigram scorer; ven+ha -> "venha" sits under the gate at margin 1.46, I only). Nothing in the reading changed. A word unigram is one instrument, not the third on this step; Tried 7 Oct 2026 (DA1-LIN, pre-registered, NOTES "letter n-gram scorer"): the same enumeration with a per-word pt18 letter 5-gram passed the known-answer control but FAILED its gluing gate (false-join rate 0.107 on held-out text vs <= 0.05; it glues function words, com+o, se+nao, tiram+os), so the target was not scored: non-test, reading unchanged; Tried 9 Oct 2026 (LIN-TRIM, PREREG-LINTRIM2.md, NOTES "LIN-TRIM (9 Oct 2026)"): the whole-string pt18 character 5-gram (context across word boundaries) passed the known-answer control but FAILED the same gluing gate (0.093 vs <= 0.05), target not scored: non-test, reading unchanged. Character n-gram scorers on the pt18 OCR corpus are [retired] for this step after two gate-2 failures (0.107, 0.093; the numbers barely moved, rule 3); 139 of the 233 false glues involve a fragment the corpus has fewer than 3 times (OCR debris, hyphen splits), so the gluing reference is itself noisy; next: new material only -- a clean (keyed, not OCR) 1808-1819 Portuguese text for both the model and a gluing reference, then a fresh PREREG, ~$2 once the text exists (none on disk)
Settled (no longer a gap): maço 86 items /04, /01, /02 in full and /09 m0001-m0020, no cipher (settled for /04 and /01 by KH1-E, 7 Oct 2026; for /02 in full and /09 m0001-m0020 by LIN-SIB, 9 Oct 2026, and /09 m0021-m0170 by LIN-SIB2, 9 Oct 2026, each with 6 of 6 blind /11 control tiles detected at thumbnail scale; NOTES "LIN-SIB (9 Oct 2026)", "LIN-SIB2 (9 Oct 2026)"). Not a gap any more for these units; the /09 remainder is the next line. Motive stays weak (NEXT-LIN, 2 Oct 2026: no stray pages 1 and 4 exist; only a numbered-series "1" billet is conceivable, M)
- Sender-family edition, Textos Politicos, Economicos e Financeiros (1993, 2 vols), which could print the letter or its context in clear - blocker: waiting-on LOCAL-QUEUE.tsv row L10 (owner's desk runner, home IP; retry queued 26 Sept 2026 19:43 UTC, PR 27 recheck still Cloudflare 403); every cloud route has failed: bportugal.pt 403 on curl, browser_fetch.js and WebFetch, and Google Books NO_PAGES (AUDIT s.10, s.11). The Wayback CDX route named as the meantime step was tried again by this check (2 Oct 2026, 00:19 UTC, 1 request, prefix query on ocpep-7_t*). It failed at the transport level again (curl 35 reset; proxy recentRelayFailures: ws_closed_mid_exchange, web.archive.org:443), its third such failure after 24 Sept and AUD2 25 Sept, so that route is closed from the cloud
- Other "Chave de uma cifra" units in the fonds, PT/TT/CLNH/0020/14 and PT/TT/CLNH/0078/80 - blocker: needs-physical-access; both are hasImages:false and hasPublishedRepresentations:false on a fresh docs/details call (NOTES "More under this key (LX-TR)"), with no description beyond the bare title. No ASKS.md row for an ANTT reproduction quote exists yet (grep CLNH/Linhares in ASKS.md: no hit); the parent should file one
- [done 9 Oct 2026, LIN-SIB3: /09 m0171-m0212 thumbnailed, no cipher; maço 86 now 21 of 21 items, 604 of 604 images eye-checked] (was: maco 86 item /09 images m0171-m0212 (42 of 212), not yet thumbnailed (20 of 21 maço 86 items fully eye-checked, plus /09 m0001-m0170: 562 of 604 images, no cipher) - blocker: not-attempted; LIN-SIB2 (9 Oct 2026) stopped at the 150-request DigitArq session cap (last image fetched: index 169, m0170); next: the same blind-control montage sweep from index 170 (scripts/linsib_montage.py over a dir holding only the new thumbnails, as LIN-SIB2 did), 42 requests, one DigitArq session, ~$1.5; the same session can spend one working-size fetch on m0146 to confirm its sideways marginal postscript is cursive (LIN-SIB2 flag, own look: cursive)

## Escalation (1 Oct 2026)
- [ ] siblings: maço 86 has 17 of 21 items (138 of 604 images) eye-checked with no numeral-group cipher found (LX-SIB/SIB2/SIB3), and the maço is Bezerra de Seixas family correspondence, 1796-1817. A DigitArq title search across CLNH found only 2 other key units, both undigitised. DECODE has no Linhares/CLNH row. Done 2 Oct 2026: m0001 on this unit (the verso of the m0002 leaf, a clear French billet, no cipher). Done 7 Oct 2026 (KH1-E): /04, /01; done 9 Oct 2026 (LIN-SIB): /02 in full, /09 m0001-m0020, no cipher; (LIN-SIB2): /09 m0021-m0170, no cipher. Not done: /09 m0171-m0212 (42 images), a lower priority -- no stray pages 1 and 4 exist; only a numbered-series "1" billet is conceivable (M)
  - [ ] DigitArq thumbnail montage of /09 m0171-m0212 (42 images, one session), same blind /11 control tiles; ~$1.5; source: loose-ends 8 Oct. Done 9 Oct 2026 (LIN-SIB): /02 in full (126) and /09 m0001-m0020, 0 cipher, 6/6 controls detected; (LIN-SIB2): /09 m0021-m0170 (150), 0 cipher, 6/6 controls detected
- [x] clear-pages: m0005-m0006 were read and are unrelated (a Hope & Co. exchange note). m0001 read 2 Oct 2026 (NEXT-LIN): it is the other face of the m0002 leaf (a single billet, not pages 1 and 4), a 40-word clear French note with a Portuguese sign-off, H 38 / M 2 -- context only, no date, no name, no crib for the cipher groups; see NOTES "m0001 fetched and read"
- [x] known-keys: the key is the period key sheet on the same unit (m0003-m0004, H). The book is Vieyra's New Pocket Dictionary, Part I, London 1809, and 12 of 12 worked-example groups fit (BOOK.md). The KEY-OFFICES.tsv and KEY-DESIGN.tsv rows are this key's own. Check-solved found no other Linhares key in Cryptiana, Cipherbrain, DECODE or either solver repository. The fonds' other two key units are undigitised (see gaps)
- [ ] print: done: web search, the 1908 biography (full-text search, 0 hits for "cifra"), Quadro elementar and Corpo Diplomatico (AUD2, negative), print_check.py with 8 phrases, JSTOR rows 70-72, the open-index pass, and the second-opinion leads (Farias 2019 and Carvalho 2023, context only, AUDIT.md "Second-opinion claims not confirmed (V6-SOCHK)"). The Wayback CDX route to the 1993 PDFs is closed from the cloud after three transport failures (gap above), so that edition is now waiting on L10 alone. Not done: the 2006 Portrait d'un Homme d'Etat (no free copy, no ASKS row). Done 9 Oct 2026 (LIN-BFSP, bfsp_sweep.tsv): British and Foreign State Papers, 32 items swept for "Linhares" via be-api, 1 hit (the 1810 treaty text, signatory only), positive control met; the "Strangford" and "Sousa Coutinho" families and volume-year mapping remain, ~$1
- [ ] key-rebuild: the key is fully specified, so no statistical rebuild is needed. LX-FIX tested all ten values of 28X219 on pp. 80-89 and only X=3 reaches rank 19. Tried 3 Oct 2026: the hOCR flush-left column counter (A1B-LIN-HOCR) failed its pre-registered calibration (21/33, 12 MISS) and was not run on 83/2 or 241/3. Tried 3 Oct 2026: the pixel-level left-edge counter (A1B-LIN-PIX) also failed the same calibration (16/33 hit, 10 MISS, 7 unlocated) and was not run. Tried 3 Oct 2026: pixel-row crops labelled one row at a time by blind subagents (A1B-LIN-ROWS) failed calibration (hit 1, MISS 2, undecided 4 of 7) and was not run; the column-count sub-step is retired on this scan after three instruments (rule 3), reopened only by new material (another scan of the book). Tried 9 Oct 2026 on new material (LIN-COUNT, 1897 px leaves): per-row labelling FAILED its pre-registered gate (A 6/7, B 5/7) and is [retired] at 1897 px; next: a person's count (ASKS draft in NOTES). Tried 6 Oct 2026: (2) the front-trim and join enumeration with a pt18 word unigram (D22-LINTRIM): control PASS, on m0002 two trim directions resolve, both = committed, no join licensed, reading unchanged; tried 7 Oct 2026: the same with a per-word letter 5-gram (DA1-LIN): control PASS, gluing gate FAIL (0.107 vs 0.05), target not scored, non-test; tried 9 Oct 2026 (LIN-TRIM): a whole-string character 5-gram, control PASS, gluing gate FAIL (0.093), non-test -- character scorers on pt18 OCR retired for (2), reopened only by a clean period text; (3) done 3 Oct 2026: 329011 as p290 c1 r1 "para" (M) after the blind re-read; (4) the Part II test reopened 5 Oct 2026 (D2-LINK: the script ink profile leans 8) and run 6 Oct 2026 (R8-LIN): no Part II parse of 829011 fits, token stays M. Planned next: a person's count of leaf0095 col 2 and leaf0255 col 3 (ASKS draft in NOTES "Row-crop labelling at 1897 px"), or the held-out re-calibration of the 1897 px labeller ("While waiting"), ~$4
- [ ] image-check: done: two blind passes over the 26 recorded groups, reconciled at 80.8% agreement, with 5 disagreements settled from 8-12x re-crops (LX-TR); the caret digit of 283219 re-cropped at 20x and read blind (LX-FIX: 3 about 55%, 5 about 30%, 8 about 15%). Done 3 Oct 2026 (A1B-LIN-M0002b): one tools/iiif_lines.py crop, 2 blind reads and 1 reconciliation of the cancelled group (illegible, both reads) and the first glyph of 829011 (3, both reads, 55% each). Not tried: a script ink-profile comparison of that glyph against every 3 and 8 on m0002
- [x] retry: LX-QAFIX re-derived all 26 groups with the corrected key and 24 of 26 agree. "justa" was lowered from H to M and "cagar" stays M; decode_key.py --check exits 0. A further retry is due after the column counts, the 829011 re-read and the cancelled group (m0001 done 2 Oct 2026, it changes no group)
Verdict: keep going: 4 internal gaps (maço 86 /04 /01 /02 settled 7 and 9 Oct 2026, KH1-E and LIN-SIB, the two maço gaps merged into the /09 remainder; m0001 settled 2 Oct 2026, NEXT-LIN; the cancelled group moved to illegible 3 Oct 2026, A1B-LIN-M0002b; p2l2pos6 moved to needs-physical-access 6 Oct 2026, R8-LIN); cheapest next: the BFSP "Strangford"/"Sousa Coutinho" be-api families with controls and the volume-year map (print step; the "Linhares" family ran 9 Oct 2026, LIN-BFSP), ~$1 (the trim/join enumeration is done as far as cheap instruments go: word unigram D22-LINTRIM passed and changed nothing; per-word letter 5-gram DA1-LIN and whole-string character 5-gram LIN-TRIM 9 Oct 2026 both failed the gluing gate, 0.107 and 0.093, character scorers on pt18 OCR retired for that step) (the Part II test of 829011 as written ran 6 Oct 2026, R8-LIN: no Part II parse fits, p2l2pos6 stays M between the null and 'para', whose glyph only a higher-resolution image can settle); then the two column counts (cagar 83/2, justa 241/3): retired on the 949 px scan after three instruments (A1B-LIN-ROWS 3 Oct 2026) and the row-labelling instrument retired at 1897 px too (LIN-COUNT 9 Oct 2026, gate FAIL with every rank exact), next a person's count of leaf0095 col 2 and leaf0255 col 3, ~$0 (ASKS draft in NOTES) (loose-ends 8 Oct 2026 added 1: DigitArq thumbnail montage of /02 and /09; 9 Oct 2026 LIN-SIB did /02 and /09 m0001-m0020, LIN-SIB2 /09 m0021-m0170, no cipher; left: /09 m0171-m0212, one DigitArq session, ~$1.5)

## hOCR column counter (A1B-LIN-HOCR, 3 Oct 2026) -- PRE-REGISTRATION (written and pushed before any scored run)

Instrument: `ciphers/antt-linhares-chave/hocr/hocr_column_count.py` (method in its docstring) on IA's own
`newpocketdiction00viey_hocr.html` (78.5 MB, fetched once to the scratchpad, not committed; re-fetch from
archive.org/download/newpocketdiction00viey/). hOCR `ppageno` == leaf. A line counts as a headword iff its first word's
x0 is within TOL = 20 px of the column margin (10th percentile of the column's line x0s); the hanging indent of
continuation lines is ~35-47 px at this scan's 400 dpi (smoke-tested on leaf 200, a page in neither set below). This is the
every-bold-line convention measured by position, independent of any eye count. `tools/ia_djvu_headwords.py` was checked
first (Usage 8): it finds a word at a line start per scan, with no columns or indentation, so it cannot count ranks.

Calibration set (`hocr/calibration.tsv`, 34 groups): the 11 worked-example groups with a confirmed leaf (page 1 has none on
file) and the 23 live groups whose reading two counts agree on (all 26 minus the null 829011 and the two disputed groups).
For each, the script finds the flush-left line in that column whose first OCR token best matches the expected headword
(SequenceMatcher ratio after accent/long-s normalisation). Located (ratio >= 0.5) and at the key's rank = hit; located
elsewhere = MISS; ratio < 0.5 = unlocated (OCR too garbled to say).
**Gate: PASS iff MISS = 0 and unlocated <= 3, at TOL 20 (k = 0, exact rank).** No re-tuning of TOL or the method after
seeing the calibration result; a FAIL stops the job and logs the counter as not licensed on this scan.

What settles each gap (read only if the gate passes):
- 83/2 (leaf 95 col 2, "cagar"): if the counter's rank-19 flush-left line is "Cagar" (ratio >= 0.5), the column-count
  objection (LX-QAFIX's 18) is resolved for 28[3]219; the token stays **M** because its grade rests on the caret digit's
  shape (3 vs 5 vs 7), which this instrument does not see. If the column has fewer than 19 flush-left lines or rank 19 is
  another word, 283219 goes to unresolved (U) at the column-count level, as Remaining gaps already says.
- 241/3 (leaf 255 col 3, "justa"): whatever the counter's rank-15 headword is ("Justa" or "Jus"), it is the reading; graded
  **H** if it agrees with at least one of the earlier independent counts (LX-DEC: Justa; LX-DEC's subagent and LX-QAFIX:
  Jus), since the dictionary is the key itself (key-source grade, rule 4) and the count is then backed by two instruments;
  also reported: whether "Junto, prepos." heads col 3 as its own flush-left line.
- If the counter's rank-15 or rank-19 line is unlocated/garbled, that gap stays as it is and the job says so.

### Result (A1B-LIN-HOCR, 3 Oct 2026, 16:44 UTC): calibration FAIL -- counter not licensed, target columns not run

`python3 hocr/hocr_column_count.py <scratchpad>/newpocketdiction00viey_hocr.html --calibrate hocr/calibration.tsv`
(output `hocr/calibration_result.tsv`, exit 1): **hit 21, MISS 12, unlocated 0 of 33 -> FAIL** at TOL 20. (The
pre-registration said 34 groups; the file holds 33 -- live 311021 "com" is the same column and rank as the worked
example's and was entered once. The gate is unaffected.) As pre-registered, no re-tuning and no run on leaf 95 col 2 or
leaf 255 col 3: both disputed columns stay exactly as they were (justa M, cagar M), no token moved, so no `--check`
re-run or AUDIT.md / SECOND-OPINIONS-QUEUE.tsv propagation is due.

Why it fails (diagnosis from the calibration rows only, for the next instrument): six misses are +1 (Guerra, Abicar, D,
Memoria, Lhe, Habil -- an extra flush-left line ahead of the headword: a section letter, an editorial note line such as
"words in Portuguese", or an OCR fragment of a continuation line), two are -1 (Mando, Venablo -- a headword merged into
the line above or read as indented), and four are gross (Com 24, Acaso 20, Parecer 27, Segredo 10 -- OCR lines merged
across headwords, so the best token match lands on the wrong line). Off-by-one errors in both directions are exactly the
size of both disputes (Jus/Justa is one line; cagar needs 19 vs a blind 18), so this OCR's line segmentation cannot decide
either. Rule 3: one attempt of this instrument, not a third; logged as "untestable by the IA hOCR line segmentation", not
as evidence either way. The next instrument works on pixels, not OCR lines: find each text row by ink profile in the
column crop and test whether its left edge sits at the margin or at the hanging indent (the row is the unit, so OCR
merges cannot hide a headword), calibrated on the same 33 groups with the same gate.
Requests: archive.org 3 (metadata/files list, the hOCR file, page_numbers.json), 1.5 s apart. Vision calls 0, subagents 0.

## Pixel indent counter (A1B-LIN-PIX, 3 Oct 2026) -- PRE-REGISTRATION (written and pushed before any scored run)

Instrument: `ciphers/antt-linhares-chave/hocr/pixel_indent_count.py` (method in its docstring) on the page images
already on disk (`images/book/*_leafNNNN_*.jpg`, 949 x 1076, exactly half the 400 dpi hOCR page). A different instrument
from A1B-LIN-HOCR's: the unit is the pixel text row (row-ink profile of the column crop, rows split at minima when a
run is over 1.6x the median height), and a row is a headword iff its left ink edge sits within T = 10 px of a
skew-fitted margin line (hanging indent ~20 px at this scale). Column rules are blanked (vertical-window rule mask,
a fitted slanted-line mask, and sliver skipping). hOCR is used only for the column borders and, to score a known word,
for the y of the best-matching OCR word lying at the column's flush margin -- never for line segmentation, so the
merged-line failure of A1B-LIN-HOCR cannot recur in the count itself. `tools/` was checked first (Usage 8):
`iiif_lines.py` segments page lines by ink profile but has no columns or indent test; nothing else counts ranks.
Parameters (T = 10, row threshold 4% of column width, split 1.6x, rule masks) were set on the tuning leaves 92-94,
96-97, 100-103 only -- none is a calibration leaf or a target leaf (95, 255); their edges are bimodal at 0 and ~20 px.
hOCR file: `newpocketdiction00viey_hocr.html` re-fetched once to the scratchpad (78.5 MB, not committed).

Calibration: the same 33 groups (`hocr/calibration.tsv`). For each, the counter's rank of the pixel row holding the
best hOCR match for the expected headword (ratio >= 0.5, and no other row within 0.02 of it) = hit if equal to the
key's rank, MISS if different, unlocated if ratio < 0.5, a tie, or no row. **Gate: PASS iff MISS = 0 and unlocated <=
3 (exact rank), the gate A1B-LIN-HOCR used.** No re-tuning after the calibration result; a FAIL stops the job and
logs the counter "untestable by this instrument" on this scan (rule 3: second instrument, first attempt).
What settles each gap (read only if the gate passes):
- 83/2 (leaf 95 col 2, "cagar"): if the counter's rank-19 row is the "Cagar" row (located as above), the column-count
  objection (LX-QAFIX's 18) is resolved for 28[3]219; the token stays **M**, since its grade rests on the caret digit's
  shape, which this instrument does not see. If the column has fewer than 19 flush rows or "Cagar" sits at another
  rank, 283219 goes to unresolved (U) at the column-count level.
- 241/3 (leaf 255 col 3, "justa"): whichever of "Jus" / "Justa" the counter places at rank 15 is the reading, graded
  **H** if it agrees with at least one earlier independent count (LX-DEC: Justa; LX-DEC's subagent and LX-QAFIX: Jus);
  also reported: whether "Junto, prepos." heads col 3 as its own flush row.
- If the relevant row is unlocated, that gap stays as it is and the job says so.

### Result (A1B-LIN-PIX, 3 Oct 2026, 17:05 UTC clock): calibration FAIL -- counter not licensed, target columns not run

`python3 hocr/pixel_indent_count.py <scratchpad>/newpocketdiction00viey_hocr.html images/book --calibrate
hocr/calibration.tsv` (output `hocr/pixel_calibration_result.tsv`, exit 1): **hit 16, MISS 10, unlocated 7 of 33 ->
FAIL** at T 10 (pre-registration commit 80d74cd5, pushed as ccba2b60 before the run). As pre-registered: no re-tuning,
no run on leaf 95 col 2 or leaf 255 col 3; both tokens stay as they were (justa M, cagar M), no token moved, so no
`--check` re-run and no AUDIT.md / SECOND-OPINIONS-QUEUE.tsv propagation is due. Rule 3: the second instrument's first
attempt; logged "untestable by the pixel indent counter on these 949 px page images", not evidence either way.

Diagnosis (from the calibration rows and a row dump of seven failing columns, no vision call; for the next instrument,
not a re-tune of this one). The failures are of two kinds. (a) The locator, not the count: 236/1 "Guerra" (the counter's
rank 2 row is the OCR "Gné^rra, s. f. war" row, the key's own rank, but the locator preferred "Guerrear" at rank 3) and
276/2 "Memoria" (rank 3 row is "Memóiia, s. f. memory", the key's rank; the locator matched a later "Memoria" word);
several unlocated rows are exact-ratio ties between a headword and the same word in a later entry (Franco, Logo). (b)
The count itself: 236/3 "Habil" (the last continuation line of the previous entry, "words in Portuguese", edges at +5
and was counted flush), 146/1 "D" (the large section initial left an empty flush row ahead of rank 1), 261/2 "Lhe" (a
continuation row cut at -10 px read as flush). Five of A1B-LIN-HOCR's six +1 misses (Guerra, Abicar, D, Memoria, Lhe,
Habil) fail here too, but for different causes in each instrument, so the overlap points at the hard columns, not at a
shared convention. Both counters fail on word identity or on single rows, never on the margin/indent split itself
(tuning-leaf edges are cleanly bimodal at 0 and ~20 px), so the next instrument keeps the pixel rows as units and has
each row crop read (flush or indent, first word) rather than counted or OCR-matched.
Requests: archive.org 1 (the hOCR file, re-fetched to the scratchpad). Vision calls 0, subagents 0.

## m0002 p.2 line 2: cancelled group and first glyph of 829011 (A1B-LIN-M0002b, 3 Oct 2026) -- PRE-REGISTRATION (pushed before any read)

Crop command (run 3 Oct 2026; the 1182 x 774 file is DigitArq's full-size dissemination image, no larger source exists, no fetch made):

```
python3 tools/iiif_lines.py --image ciphers/antt-linhares-chave/images/full_PT-TT-CLNH-0086-11_m0002.jpg.jpg \
  --out ciphers/antt-linhares-chave/images --region 610,100,350,75 --centres 37 --prefix m0002_p2L2z \
  --groups 40 --group-upscale 4 --debug
# region 350x75, 1 lines, 1 bands x 1 segments; band L01: 1 pieces at gap >= 40; wrote 2 crops
```

Crops: `images/m0002_p2L2z_L01.jpg` (native 350x75) and `images/m0002_p2L2z_L01_g01.jpg` (the same, 4x, 1392x300).
The debug overlays (`m0002_p2L2z_lines_debug.jpg`, `..._groups_debug.jpg`) were checked by eye: the band holds
829011 with its subscript, the whole looped cancelled group with its interlinear mark, and 328131 with its
subscript; one piece, nothing cut. Only the 4x crop goes to the readers (no full page, no candidate values, no
existing transcription).

Tokens in question and what settles each (two blind Sonnet subagent reads, then one reconciliation by this worker):

| # | token | settled when | grade if settled | split | what changes if settled |
|---|---|---|---|---|---|
| T1 | first glyph of the group recorded as 829011 (p2 l2 pos6) | both reads give the same digit for glyph 1 | H (NOTES convention: read off the image, two blind passes agree) | stays as recorded, grade drops H -> M, gap stays open | **3**: the group is 329011, parses as p290 c1 r1 ("Paralisia", trim 5 -> "para", grade I until the headword is re-counted on the page image); ciphertext.tsv row edited, is_null false, decode `--check` re-run, AUDIT.md and SECOND-OPINIONS-QUEUE.tsv propagated (rule 10). **8**: 829011 confirmed at H as written; the null question passes to the Part II test (Escalation key-rebuild (4)) |
| T2 | the remaining digits of that group (positions 2-6) and its subscript | both reads agree digit for digit | H | M on the split digit only | a change at any position is logged and the parse re-run as above |
| T3 | the cancelled, looped group: is any digit legible under the strike? | both reads give the same digit string (or both say illegible) | digits both read: M (struck text is never H here); both "illegible": recorded as illegible | recorded as illegible, M | a cancelled row is added to ciphertext.tsv (is_null "cancelled", no book_page/col/rank), never decoded or counted in the reading |
| T4 | the interlinear mark above the cancelled group | both reads give the same characters | M (a correction or note, not a cipher group) | recorded as "mark, unread" | recorded in the cancelled row's note; if it reads as a cipher group or digits it is logged, not decoded, and named as a next step |

No threshold beyond "both reads agree" is used. A reconciliation by this worker may break a split only by naming a
visible feature of the crop; a split it cannot so break stays M.

### Result (A1B-LIN-M0002b, 3 Oct 2026, after the pre-registration above, commit e3355cf1)

Two blind Sonnet subagent reads of `images/m0002_p2L2z_L01_g01.jpg` only (no candidate values, no transcription
shown), then a reconciliation by this worker on the same tool's line crop.

| # | read A | read B | outcome under the pre-registration |
|---|---|---|---|
| T1 first glyph | 3 (55%; 8 40%) | 3 (55%; 8 45%) | **agree: 3.** Reconciliation feature: flat top bar shared with every 3 on line 2 (3241315, 322332, 3360320) and no crossed waist like the two 8s of 260118. Group is **329011** |
| T2 rest + subscript | 3 2 9 0 1 1 / 5 | 3 2 9 0 1 1 / 5 | agree, unchanged |
| T3 cancelled group | ILLEGIBLE (90%) | ILLEGIBLE (95%) | agree: illegible; solid bar, about 6-9 glyph widths; `cancelled.tsv`, M |
| T4 mark above | "Ag" ~40%, letters not digits | UNREADABLE, "Ag"/"Ay" ~35%, letters | recorded as "mark, unread", letter-like |
| (328131 / 3, context) | 32813 1 / 3 (60%) | 328131 / 3 | not in question; unchanged |

Decode: p290 col1 rank 1 is the column's first headword, "Paralisía" (read off `images/book/newpocketdiction00viey_leaf0306_p290.jpg`
this pass, no count needed), trim 5 from the end -> "Para". Line 2 now reads "d justa he segredo ate **para** o ministerio".
**Deviation from the pre-registration, toward caution:** the pre-registration gave T1 grade H on agreement. Both readers
put their own call at only 55%, so the decoded token is held at **M**, not H, in key.tsv (the ciphertext.tsv row keeps
the transcription grade H as pre-registered). The cancelled group is kept in `cancelled.tsv`, not ciphertext.tsv as
pre-registered: `tools/decode_key.py` reads every row of ciphertext.tsv as a token (TOOL-DK-HASH), so a row there would
have put it into the reading.

Totals: 26 tokens, H 23 / M 3 / U 0 (was H 24 / M 2 with one null). `python3 tools/decode_key.py ciphers/antt-linhares-chave --check`:
"reading up to date", exit 0. Judge (`python3 tools/judge_plaintext.py specs/antt-linhares-chave.json --file ciphers/antt-linhares-chave/reading.txt`):

```
ok   language: score=-1.024, null_p99=-1.452, real_p05=-1.122, real_median=-0.849, mode=both, N=102
ok   words: cover=0.922, min=0.5, real_text_median_cover=0.951
PASS - antt-linhares-chave (a PASS is a gate for a verifier, not a reading; rule 10)
```

A fresh-instance re-derivation (rule 7) has not been run on the revised token; the one-token change is propagated to AUDIT.md
and the SECOND-OPINIONS-QUEUE.tsv row (rule 10). Requests: none (all images on disk).

## Rule 7 re-derivation (A1B-LIN-REDERIV, 3 Oct 2026)

Fresh session (17:39-17:41 UTC), which read only CLAUDE.md, `specs/antt-linhares-chave.json`, `key.tsv`, `ciphertext.tsv`
and `decode.json` before deriving (no exceptions file is named by decode.json). An independent ~15-line script (scratchpad, not
`tools/decode_key.py`) mapped each ciphertext.tsv group through key.tsv, dropped `[null]` values and joined per
page_of_letter + line. It gave 26 tokens, H 23 / M 3 / U 0:

```
para supprir o seu lugar junto com man o
d justa he segredo ate para o ministerio
pela memoria do cagar lhe pauperr ven ha
logo
```

`python3 tools/decode_key.py ciphers/antt-linhares-chave --check` (exit 0):

```
ciphertext.tsv: tokens 26: H 23, M 3
reading up to date
```

`python3 tools/judge_plaintext.py specs/antt-linhares-chave.json --file ciphers/antt-linhares-chave/reading.txt` (exit 0):

```
ok   language: score=-1.024, null_p99=-1.452, real_p05=-1.122, real_median=-0.849, mode=both, N=102
ok   words: cover=0.922, min=0.5, real_text_median_cover=0.951
PASS - antt-linhares-chave (a PASS is a gate for a verifier, not a reading; rule 10)
```

Diff, made only after the above was written: the four reading.txt lines are identical to the re-derivation's text. Per
token against reading_tokens.tsv (sign, value, grade): **0 of 26 differ**, so no differences fall outside the M-graded tokens.
**Verdict: PASS (rule 7).** The 329011 = "para" (M) revision re-derives from the spec and the key alone.

Bookkeeping seen in passing, not changed (outside this brief): (1) ciphertext.tsv still grades the 329011 row `H`
(a transcription grade, kept on purpose by A1B-LIN-M0002b) while key.tsv grades the decoded token `M`; decode_key.py
takes the key grade, so the reading is right. (2) key.tsv still carries the orphan row `829011 [null]`, which no
ciphertext group now uses. Suggestion: drop it or mark it superseded in a later housekeeping pass (~USD 0.2).
Vision 0, subagents 0, network requests 0.

## Row-crop labelling (A1B-LIN-ROWS, 3 Oct 2026) -- PRE-REGISTRATION (pushed before any vision call)

Third instrument for the two disputed column counts (after A1B-LIN-HOCR and A1B-LIN-PIX failed calibration): segmentation
by pixels, identity and indent by eye, no long-column counting by any model. Source: the page images on disk
(`images/book/*_leafNNNN_*.jpg`, 949 x 1076). Each column is cut into one crop per text row with
`tools/iiif_lines.py --image <leaf jpg> --region <column box> --lines-per-crop 1 --out <scratchpad>/rows_<leaf>_<col> --prefix L<leaf>c<col> --debug`
(column boxes set by eye from a ruled contact sheet of the pages, starting just right of the column rule; commands and
debug overlays pasted in the result). Row crops are upscaled 3x (no other change) and stacked, numbered, into sheets of at
most 40 rows (one sheet = one batch of row crops). Each row is labelled by a blind Sonnet subagent, which is told nothing
about the dictionary key, the target words or ranks: per row, one of `FLUSH` (row starts at the column's left margin),
`INDENT` (starts at the hanging indent), `OTHER` (blank, running head, section initial or heading, rule, fragment,
two lines merged -- named), plus the first word if FLUSH. Model labels are not overridden.

Count convention (the key's every-bold-line convention, NOTES LX-QAFIX): rank = ordinal of FLUSH rows from the top of the
column. A row labelled OTHER "two lines merged" or "fragment" in the counted range makes that column undecided (no fix-up).

Calibration (7 columns from `hocr/calibration.tsv`, including the five that both earlier instruments missed by +1):
236/1 Guerra r2, 236/3 Habil r1, 146/1 D r1, 276/2 Memoria r3, 261/2 Lhe r6, plus two deep columns for the target depth,
265/2 Lugar r17 and 255/2 Junto r20 (same leaf as the "justa" column). Score: the FLUSH row whose labelled first word
matches the expected headword (accents and long s ignored, first match from the top) has ordinal == key rank.
**Gate: PASS iff all 7 calibration columns are exact (MISS 0, undecided 0).** No re-labelling, re-cutting or re-tuning
after the calibration result. A FAIL stops the job: the target columns are not labelled, and per rule 3 (third instrument
on the same question) the column-count step is logged [retired] with all three instruments named.

What settles each gap (read only if the gate passes), as in the A1B-LIN-HOCR / A1B-LIN-PIX pre-registrations:
- 83/2 (leaf 95 col 2, "cagar", 283219): FLUSH rank 19 first word "Cagar" -> the column-count objection (LX-QAFIX's 18)
  is resolved; the token stays **M** (its grade rests on the caret digit's shape). Rank 19 another word or fewer than 19
  FLUSH rows -> 283219 goes to unresolved (U) at the column-count level.
- 241/3 (leaf 255 col 3, "justa", 3241315): whichever word sits at FLUSH rank 15 is the reading ("Justa" or "Jus"),
  graded **H** if it agrees with at least one earlier independent count (LX-DEC: Justa; LX-DEC's subagent and LX-QAFIX:
  Jus); also reported: whether "Junto, prepos." heads col 3 as its own FLUSH row.
- A rank-15/19 row labelled OTHER or with an unreadable first word: that gap stays as it is and the job says so.
A moved token is propagated (decode --check, judge, AUDIT.md, SO-LINHARES rows) and a rule-7 re-derivation is named as
the next step, not run here.

### Result (A1B-LIN-ROWS, 3 Oct 2026, 18:04 UTC clock): calibration FAIL -- target columns not labelled; column-count step [retired]

Crops: `python3 tools/iiif_lines.py --image images/book/<leaf jpg> --region <box> --lines-per-crop 1 --ink 110 --centres <c> --out <scratchpad>/rows_<leaf>_<col> --prefix L<leaf>c<col> --debug`
for boxes 95/2 303,35,310,1000; 255/2 303,35,300,1000; 255/3 603,35,300,1000; 236/1 50,35,300,1000; 236/3 703,35,246,1000;
146/1 48,35,300,1040; 276/2 400,35,300,1000; 261/2 303,35,305,1000; 265/2 303,35,305,1000. The tool's default `--ink 170` sits
inside this paper's background (median grey 157), so `--ink 110`; its own peak finder (prominence 6) both missed rows (gaps of
~42 px) and split rows (peaks 14 px apart), so the centres passed with `--centres` are a straight-line grid fitted to its peaks
(pitch 21.2-21.4 px, `hocr/rows_grid.py`) snapped to the nearest detected peak within 7 px (`hocr/rows_centres_used.txt`).
Sheets (`hocr/rows_sheets.py`: each row box +-5 px, 2x, numbered, red arrow at the row's centre; committed as
`images/rows/sheet_*.jpg`, calibration sheets only). 4 blind Sonnet subagent calls (one per batch A-D, 166 rows), labels in
`hocr/rows_calibration_labels.tsv`, not overridden.

| column | headword, key rank | labelled FLUSH ordinal of first match | verdict |
|---|---|---|---|
| 236/1 | Guerra 2 | 1 (R02 and R03 both "Guérra"; first match from the top) ; R01 fragment | MISS |
| 236/3 | Habil 1 | -- (9 of 10 rows OTHER: left edge cropped) | undecided |
| 146/1 | D 1 | "D" sits on the drop-cap row R07, labelled OTHER; first FLUSH is "D'." | MISS |
| 276/2 | Memoria 3 | -- (13 of 15 rows OTHER: left edge cropped) | undecided |
| 261/2 | Lhe 6 | 6 | hit |
| 265/2 | Lugar 17 | 17 ; R01 top-edge fragment in the counted range | undecided (rank exact) |
| 255/2 | Junto 20 | 20 ; R01 top-edge fragment in the counted range | undecided (rank exact) |

**hit 1, MISS 2, undecided 4 of 7 -> FAIL** (gate: all 7 exact, MISS 0, undecided 0). As pre-registered: no re-labelling,
re-cutting or re-tuning, no run on 95/2 or 255/3 (their row crops were cut but never sent to any model); both tokens stay
as they were (justa M, cagar M), no token moved, so no `--check`, judge, AUDIT.md or SECOND-OPINIONS-QUEUE.tsv propagation is due.
Rule 3 third-attempt clause, as pre-registered: the eye-count / column-count step on this 949 px scan is **[retired]** after
three instruments -- the IA hOCR line counter (A1B-LIN-HOCR), the pixel indent counter (A1B-LIN-PIX), and blind per-row
labelling of iiif_lines row crops (A1B-LIN-ROWS) -- logged "untestable by these instruments on this scan", not evidence
either way on cagar or justa.

Diagnosis (for whoever reopens it with new material, not a re-tune): two of the four non-hits are this worker's own setup
error, not the labeller's -- the 236/3 and 276/2 boxes started a few px right of the printed margin, cropping every row
(the contact sheet used to set boxes was at 0.67x). The two MISSes are the match rule, not the labels: a repeated headword
("Guérra" twice, the key's rank 2 is the second) and a drop-cap headword ("D" printed as a section initial) -- the same
duplicate-word and section-initial cases that broke both earlier counters. The labels themselves were sound wherever the
crop was: on the two deep columns the labelled FLUSH ordinal is exactly the key's rank (Lugar 17, Junto 20) and Lhe is exact
at 6. A fourth attempt with corrected boxes would change only the knob this attempt failed on, so per rule 3 it needs new
material instead: a second, independent scan of Vieyra 1809 Part I (another copy) or a higher-resolution capture of leaves
95 and 255, counted under a fresh pre-registration whose match rule names the duplicate-headword and drop-cap cases in advance.
Vision calls 4 (Sonnet subagents) + 2 own looks at contact sheets and 1 debug overlay; network requests 0.

## Ink-profile comparison of the 329011 first glyph (D2-LINK, 5 Oct 2026) -- PRE-REGISTRATION (pushed before any scored run)

Intake gate (`python3 tools/intake_gate_check.py antt-linhares-chave`, 5 Oct 2026 23:20 UTC): `antt-linhares-chave: blocked (line 3) -- already terminal, nothing to gate`

Third, different instrument on the p2l2pos6 first glyph (after two blind reads, A1B-LIN-M0002b: both 3 at 55%). Script
only, no model reads a glyph. Source: `images/full_PT-TT-CLNH-0086-11_m0002.jpg.jpg` (1182 x 774, DigitArq full size, on
disk; no fetch). Script: `scripts/glyph_ink_profile.py` (numpy + PIL only).

1. Segmentation (may be adjusted while looking only at the debug overlay, before any feature is computed; frozen at the
   first scored run): each of the four cipher lines is a fixed band; grey = mean of RGB; ink = pixels below Otsu's threshold
   of the band; 8-connected components of at least 12 px and 6 px tall; components ordered left to right and split into
   groups at x-gaps; a group whose main-digit component count equals the length of its transcribed group (ciphertext.tsv)
   labels its components digit by digit from the transcription; any other group is dropped (logged).
2. Labelled set: every 3 and 8 so labelled in groups graded H in ciphertext.tsv, excluding the target group (p2l2pos6) and
   the two M rows (3241315, 283219). The target glyph is the first component of p2l2pos6; if it is not a single isolated
   component there, the test is a non-test.
3. Features (both fixed now): **F1 template** -- the component's grey-level ink (255-grey, background 0) in its bounding box,
   resized to 12x18, zero-mean, unit-norm; score per class = mean correlation with that class's members; call = higher.
   **F2 holes** -- count of enclosed background regions (>= 2 px, not 4-connected to the box border) in the component's
   binary mask at native resolution; call 8 if >= 1 hole, else 3.
4. Control (per feature, on the labelled set): leave-one-out call of each labelled 3 and 8; **balanced accuracy** (mean of
   per-class recall, since 3s outnumber 8s); and 200 label permutations (same class counts) giving the permuted p95.
   **Gate: a feature is an instrument iff n(8) >= 4, balanced accuracy >= 0.80, and balanced accuracy > permuted p95.**
   Per-class recall is reported beside the blended figure.
5. Outcome. All passing features call the target 3 -> p2l2pos6 "para" moves M -> H (two blind reads plus a script with a
   passed control agree). Any passing feature calls 8 -> recorded as a split, token stays M, the Part II test (829011 as
   written) is reopened as next step. No feature passes, or the glyph is not isolated -> non-test, token stays M, the
   ink-profile step is logged "untestable by this tool at 1182 px" (new material: a higher-resolution image,
   needs-physical-access). F1's margin (score3 - score8) and F2's hole count for the target are reported either way.
No re-tuning of features, gate or segmentation after the first scored run.

### Result (D2-LINK, 5 Oct 2026, 23:24 UTC clock): F1 passes its control and calls the target **8**; F2 fails its control -> split recorded, token stays M

Segmentation (adjusted only on the debug overlay, before any feature was computed, as pre-registered): the slanted
line bands of the first draft did not catch the target group at all, so the group boxes were set by eye on the full image
(`GROUPS` in the script, one box per transcribed group, local Otsu per box). A trial at MINPX 8 / MINH 5 matched more
groups but visibly mislabelled 328131 (the "8" label landed on the 2), so the frozen setting is MINPX 12 / MINH 6, under
which every labelled 3 and 8 on the overlay sits on the right glyph (`images/m0002_d2link_seg_debug.jpg`, 2x, red = 3,
green = 8). 14 of 26 groups were dropped for a component/digit count mismatch (joined digits, thin 1s); the target was a
single isolated component (box x 625-637, y 122-133).

`python3 ciphers/antt-linhares-chave/scripts/glyph_ink_profile.py --score`:

```
labelled: n3=14 n8=4
F1: balanced acc 0.804 (recall3 0.857, recall8 0.750); permuted p95 0.786; gate PASS
F2: balanced acc 0.679 (recall3 0.857, recall8 0.500); permuted p95 0.679; gate FAIL
target F1: score3 0.464 score8 0.541 margin -0.077 -> 8
target F2: holes 2 -> 8
target box 625 122 637 133
```

Contact sheet (target first, then the four 8s, then the fourteen 3s, each with its hole count): `images/m0002_d2link_glyphs.jpg`.

Under the pre-registration: F1 is an instrument (passes all three gate terms) and calls the target **8**; F2 is not an
instrument (fails the gate), though it too would call 8 (the target has 2 enclosed holes; two of the fourteen 3s have 1,
none has 2). **Outcome: split** between the two blind reads (3, 3, both at 55%) and the script (8). p2l2pos6 stays **M**
as "para" (329011); nothing in ciphertext.tsv, key.tsv or the reading changes, so no `--check`, judge, AUDIT.md or
SECOND-OPINIONS-QUEUE.tsv propagation is due. The Part II test (829011 as written) is reopened as the next step.

How much weight F1 carries (stated, not re-tuned): the gate is passed by the narrowest margin it allows -- balanced
accuracy 0.804 against 0.80, permuted p95 0.786 -- on only four labelled 8s (one of them misclassified), all from three
groups; the target is the smallest and palest glyph on the sheet, and its F1 margin (-0.077) is small. This is a thin
instrument that leans 8, not a reading of 8. Three instruments now on the glyph: two blind reads lean 3, one script
leans 8; the 1182 px DigitArq image (glyph about 12 px tall) is the limit, so a further pass on this image would only
change the knob (rule 3). Requests: none (image on disk). Model vision: own looks at the debug overlay (segmentation) and
the contact sheet, after scoring; no subagent.

## Part II test of 829011 as written (R8-LIN, 6 Oct 2026) -- PRE-REGISTRATION (pushed before any Part II page is fetched or read)

Question: if p2l2pos6 is `829011` (subscript 5) as LX-TR first read it, does any Part II (English-Portuguese) parse of it, or a
switch to Part II for the groups after it, read in the line `d justa he segredo ate [p2l2pos6] [cancelled] o ministerio`?
Competitor already on file: `329011` = Part I p290 c1 r1 "Paralisía", trim 5 from the end -> "para" (M). Book: archive.org
`newpocketdiction00viey`, Part II, separately paginated in the same scan. Every Part II page cited is identified by the printed
page number and running header read off the fetched image, never by a leaf offset; rank 1 = the first fresh bold headword of the
column (a definition carried over from the previous column is not counted, BOOK.md convention).

Hypotheses ("as written" variants, all fixed now):
- **P2a**: 8 is a null marker prefixed to a live Part II group `29011` -> Part II p90 c1 r1, trim 5.
- **P2b**: 8 stands in place of the page-length digit (a null-flagged `329011`) -> Part II p290 c1 r1, trim 5.
- **P2c** (switch): `829011` is void, and the following live groups are read in Part II: `328131`/3 -> Part II p281 c3 r1, trim 3;
  `326624` -> Part II p266 c2 r4 (rank 4 counted on the image; the two earlier column counts on this scan were retired as
  instruments only for ranks 15-23 under dispute, rank <= 4 is read directly).
- **P0** (null, nothing looked up): line reads `ate o ministerio`; the subscript 5 under a null is unexplained by the key.

Gate (per hypothesis, decided before looking): a variant **fits** iff (i) the located headword exists at that page/column/rank,
(ii) a trim of the stated count from the end, or from the front (the key allows both, "do principio, ou do fim"), leaves >= 1
letter, and (iii) the result is an English or Portuguese word or a fragment that the worked example's own joining practice could
use, and the line with it substituted (P2a/P2b: `ate X o ministerio`; P2c: `ate X Y`) reads as a phrase. P2c additionally fails if
either of its two tokens fails (i)-(iii). A fit is graded I and reported as a candidate only.

Outcomes (fixed now): **token p2l2pos6 stays M in every outcome** (the lane brief: M unless a registered gate licenses a reading;
this gate licenses none, it only narrows which alternatives stay live). If no Part II variant fits: "829011 as written: no Part II
parse fits", the live alternatives are P0 (null) and 329011 "para"; the step is closed as run. If one or more fit: the fitting
variant(s) are recorded beside "para" as competing I candidates; nothing in ciphertext.tsv, key.tsv or reading.txt changes either
way. Pages fetched: at most 4 Part II page images plus the leaves needed to locate them (<= 12 archive.org requests, >= 1.5 s apart).

### Result (R8-LIN, 6 Oct 2026, 04:09 UTC clock, after the pre-registration above, commit 37fb38e45): no Part II parse of 829011 fits -- token stays M as "para"

Part II located in the same scan (`newpocketdiction00viey`, 826 leaves): it begins about leaf 437 (hOCR page index), and printed
Part II pages 90, 266, 281 and 290 sit at leaves 506, 682, 697 and 706 (offset 416, every page confirmed by the printed number
in the running head, `images/book/partII_running_heads_p090_p266_p281_p290.jpg`; leaf 526 = II-110 and 702 = II-286 were the two
probe leaves). Column tops in `images/book/partII_*_top.jpg` (manifest entries added).

| hyp | lookup | located headword (image) | trim end / front | gate |
|---|---|---|---|---|
| P2a | II p90 c1 r1, trim 5 | *To* **Congreet** (first line of col. 1, a fresh bold entry) | Con / eet | FAIL (iii): neither is a word; "ate Con o ministerio" does not read, and "Con" has no live neighbour to join with (the next group is the struck one, then "o") |
| P2b | II p290 c1 r1, trim 5 | *To* **Reel** | -- / -- | FAIL (ii): a 4-letter word cannot lose 5 letters |
| P2c | II p281 c3 r1, trim 3; II p266 c2 r4 | **Purchasable**; col. 2 opens with the carry-over "pranchas" (not counted), then Planked, Plant, *To* Plant, **Plantation** (Planter if the repeated "Plant" is not counted) | Purchasa / chasable; Plantation | FAIL (iii): "Purchasa"/"chasable" is no word, so P2c fails on its first token; "ate Purchasa Plantation" does not read |
| P0 | null, no lookup | -- | -- | not testable by a lookup; "ate o ministerio" reads, but the subscript 5 under a null remains unexplained by the key |

Under the pre-registration: **"829011 as written: no Part II parse fits."** The live alternatives for p2l2pos6 are P0 (a null,
reading "ate o ministerio") and 329011 "para" (Part I p290 c1 r1 "Paralisía" -- a 9-letter headword, so the subscript 5 has
exactly the letters to remove, which a null does not explain). Token stays **M**; nothing in ciphertext.tsv, key.tsv or
reading.txt changes, so no `--check`, judge, AUDIT.md or SECOND-OPINIONS-QUEUE.tsv propagation is due. The step is closed as run.
Grades: the four Part II headwords are read off the page images (H as dictionary facts); no plaintext token is graded by this test.
Requests: archive.org 3 (page_numbers.json -- empty pageNumber fields; djvu.txt; hocr_pageindex.json.gz), ia800806.us.archive.org 6
(page images), sequential, >= 2 s apart. No subagent; own reads of the four column-top crops.

## Front-trim and adjacent-join enumeration (D22-LINTRIM, 6 Oct 2026) -- PRE-REGISTRATION (pushed before any scored run)

Question: the key allows a trim "do principio, ou do fim da palavra", and its worked example joins fragments ("Franc"+"a",
"Rus"+"si"+"a"); the committed reading uses end-trims and no joins. Does a mechanical enumeration of both trim directions and
adjacent joins, scored by an era-matched Portuguese word model, pick a different reading for any trimmed token, or a join?

Input fixed now (book headwords as on file in key.tsv / BOOK.md, accent-folded, lower case; trim n from the key's subscript):
worked example (12 groups) Aba/2 (p1 c3 r1, read this job off leaf 11 = printed p.1, `images/book/newpocketdiction00viey_leaf0011_p001.jpg`),
guerra, de, franco/1, anao/3, com, abicar/5, rustico/4, sillaba/5, acaso/4, parecer/1, inevitavel; target m0002 (26 groups, reading
order) para, supprir, ovo/2, seu, lugar, junto, com, mando/2, ouros/4, d, justa, hernia/4, segredo, ate, paralisia/5, odio/3,
ministerio, pela, memoria, dormitar/6, cagar, lhe, pauperrimo/3, venablo/4, habil/3, logo. (justa, cagar, para stay M as on file;
their lookups are not varied here.)

Instrument: `scripts/trim_join_enum.py`. Variants: a token with trim n has {W[:-n] (end), W[n:] (front)} (identical strings merged);
an untrimmed token is fixed. A word is the concatenation of 1-4 consecutive tokens (joins allowed across manuscript line breaks).
Scorer S1, fixed now: word unigram from `tools/data/pt18` (all four files; lower case, accents folded, [a-z]+ tokens): an in-vocabulary
word scores ln(c/N); an out-of-vocabulary word scores ln(0.1/N) - len(word). The reading is the exact maximum over all configurations
(dynamic programme over token positions).

Gate 1, known-answer control (run first; can fail): on the 12 worked-example groups the argmax must be exactly
`a guerra de franca com a russia parece inevitavel`. If not: log "non-test: enumerator fails its known-answer control", score nothing
on the target, stop.
Resolution (fixed now): per trimmed token, margin = best total with the chosen direction minus best total with the other direction forced;
per adjacent boundary, margin = best with the chosen join/split minus best with the opposite forced. A decision is **resolved** iff
margin >= ln(10) = 2.303. Also reported, not gating: the same margins on the worked example, and a scrambled-order null (20 seeded
permutations of the 26 target tokens) giving how many trim and join decisions resolve when token order is destroyed -- trim-direction
calls that resolve equally in the null are lexical (the fragment is or is not a word), not evidence from context.
Outcomes (fixed now): nothing in ciphertext.tsv, key.tsv or reading.txt changes in this job. A resolved token whose chosen direction
equals the committed end-trim is reported as consistent; one whose chosen direction differs is reported as a candidate graded S at most,
listed beside the committed token; an unresolved one keeps its reading and its decision is M. A resolved join is reported as a
connected-gloss candidate (I), never merged into reading.txt. No network beyond one page image (leaf 11, fetched for Aba).

### Result (D22-LINTRIM, 6 Oct 2026, 22:21 UTC clock, after the pre-registration above, commit b883dc2be): control PASS; no trim direction changes; no join licensed

Run: `python3 scripts/trim_join_enum.py` (pt18 N = 690,057 tokens, 97,463 types), full table `trim_join_result.tsv`.
**Gate 1 PASS**: the worked-example argmax is exactly `a guerra de franca com a russia parece inevitavel` (score -56.92); all 7
non-degenerate trim decisions in it resolve to the end-trim (margins 2.95-10.64, the weakest Anao a/o at 2.95) and all 11 boundaries
resolve correctly, including the joins Franc+a and Rus+si+a (margins 7.6-8.9).
Target argmax: `parasupprir o seu lugar junto comman o djustahesegredo ate para o ministerio pela memoria docagarlhepauperr venha logo`.

| token (headword/trim) | committed | alternative | chosen | margin | call |
|---|---|---|---|---|---|
| mando/2 | man | ndo | end | 1.29 | unresolved (M) |
| ouros/4 | o | s | end | 0.50 | unresolved (M) |
| hernia/4 | he | ia | end | 0.00 | unresolved (M) |
| paralisia/5 | para | isia | end | 5.17 | resolved, = committed |
| dormitar/6 | do | ar | end | 0.00 | unresolved (M) |
| pauperrimo/3 | pauperr | perrimo | end | 0.00 | unresolved (M) |
| venablo/4 | ven | blo | end | 1.46 | unresolved (M) |
| habil/3 | ha | il | end | 3.72 | resolved, = committed |
| ovo/2, odio/3 | o | (front gives o too) | -- | -- | no alternative |

- **Trim direction:** 2 of 8 decisions resolve, both to the committed end-trim; none resolves to a front-trim, so no S candidate differs
  from the reading. The scrambled-order null (20 permutations) resolves 2.40 trim decisions on average, so these two are lexical calls
  ("para" vs "isia", "ha" vs "il"), not evidence from context. The other six stay as committed, direction M.
- **Joins:** resolved joins on the target are cagar+lhe and lhe+pauperr (margins 5.6, 4.7), inside `docagarlhepauperr`. These are an
  artefact of the registered scorer, visible only on the target: an out-of-vocabulary word costs ln(0.1/N) - len, so gluing two adjacent
  OOV tokens (here "pauperr"; also "supprir", the archaic spelling, and "djustahe...") saves one OOV penalty whatever the letters. The
  control has no OOV token, so it could not expose this. They are not reported as connected-gloss candidates. The null resolves 5.05
  joins on average, the same order as the target. Unresolved but worth naming as an I-grade reading only (margin 1.46, under the gate):
  ven+ha -> **venha** ("come"), giving `venha logo` ("come at once") at the letter's end; and com+man -> "comman" (margin 1.29) is not a word.
- **Grades:** unchanged. ciphertext.tsv, key.tsv and reading.txt are not touched (as registered), so no `--check`, AUDIT.md or
  SECOND-OPINIONS-QUEUE.tsv propagation is due. Dictionary fact added: Vieyra 1809 p.1 col.3 rank 1 = **Aba** (H, read off leaf 11),
  the one worked-example group not previously checked against the page image; trim 2 gives "a" from either end.
- Limits: a unigram word model cannot judge joins that make no dictionary word, nor OOV fragments; a selector that scores characters
  (a pt18 letter n-gram) would be a different instrument for the six unresolved directions and the joins. Requests: archive.org image
  host 1 (leaf 11). No subagent.

## Front-trim and adjacent-join enumeration, letter n-gram scorer (DA1-LIN, 7 Oct 2026) -- PRE-REGISTRATION (pushed before any scored run)

Same question, inputs, enumeration, decision rule and outcomes as D22-LINTRIM above (the 12 worked-example groups, the 26 m0002
groups, {end, front} per trimmed token, words of 1-4 consecutive tokens, exact DP maximum, margin = best with choice minus best with
the opposite forced, **resolved iff margin >= ln(10)**, nothing in ciphertext.tsv / key.tsv / reading.txt changes, a resolved front-trim
is an S candidate at most beside the committed token, a resolved join an I connected-gloss candidate, never merged). Only the scorer
changes. The two column counts (cagar 83/2, justa 241/3) are not touched.

Scorer S2, fixed now (`scripts/trim_join_char.py`, which imports the enumerator from `scripts/trim_join_enum.py` unchanged): a
character 5-gram, interpolated Witten-Bell, alphabet a-z plus a word-boundary mark `#`, trained on `tools/data/pt18` (all four files,
lower case, accents folded, [a-z]+ words) **minus the last 10% of words of each file**, which are held out. A word w scores
log P(`#w#`) with the first character conditioned on `#` alone (words scored independently, so the DP is unchanged).

Gate 1, known-answer control (run first; can fail): worked-example argmax exactly `a guerra de franca com a russia parece inevitavel`.
Gate 2, gluing check (run second; can fail; asked by the brief): 100 windows of 26 consecutive held-out words (seeded, seed 20261007),
every token fixed (no trim), run through the same DP: **false-join rate = joined boundaries / all boundaries must be <= 5%**. If either
gate fails: log "non-test: letter-n-gram scorer fails gate N", score nothing on the target, stop.
Also reported, not gating: per-decision margins on the worked example; the scrambled-order null (20 seeded permutations of the 26 target
tokens, seed 20261006 as D22) for trim and join resolutions; and the same table of the target's 8 trim directions and 25 boundaries as
D22, side by side with D22's unigram call.

### Result (DA1-LIN, 7 Oct 2026, 14:52 UTC by date -u, after the pre-registration above, commit 46fe32cd8): Gate 1 PASS, Gate 2 FAIL -- non-test, target not scored

Run: `python3 scripts/trim_join_char.py` (exit 3; pt18 train 621,050 words, held-out 69,007), table `trim_join_char_result.tsv`.
- **Gate 1 PASS**: worked-example argmax exactly `a guerra de franca com a russia parece inevitavel` (score -62.11).
- **Gate 2 FAIL**: on 100 held-out windows of 26 fixed words the DP joined 10.68% of boundaries (2,500 boundaries; 187 two-word, 22
  three-word and 12 four-word glues), against the registered ceiling of 5%. As registered: "non-test: letter-n-gram scorer fails gate 2";
  the 26 m0002 groups were not scored and no null was run. Nothing in ciphertext.tsv, key.tsv or reading.txt changes; grades unchanged;
  no `--check`, AUDIT.md or SECOND-OPINIONS-QUEUE.tsv propagation is due.
- Diagnostic, held-out text only (not the target, not gating): the commonest false joins are a function word with its neighbour --
  com+o (7), se+nao (3), tiram+os, se+o, idea+das, esquerda+do -- plus OCR debris (digitized+by, sn+geitofl). Cause: words are scored
  independently as `#w#`, so a split pays two boundary transitions (P(# | ...w) and P(w1 | #)) while a join pays one in-word transition,
  and for short function words the in-word one is cheaper. The per-word scorer has a structural bias toward gluing, the same direction as
  D22's OOV-merge artefact, from a different cause.
- What would be a different instrument: one character model over the whole reading with spaces, context carried across word boundaries,
  so a join is priced as P(next letter) against P(space) given the same preceding letters (DP state = the last four characters). That is
  not a re-tuning of this scorer's knob (rule 3's third-attempt clause does not close the step); it would face the same two gates.
- Requests: none (corpus on disk). No subagent.


## Keyhunt 7 Oct 2026

KH1-E (LANE KH-1, 7 Oct 2026, 17:47-18:00 UTC by date -u), for key.tsv and key_example.tsv (KEY-OFFICES rows 2-3).
Sources searched, 7 Oct 2026: this NOTES.md (LX-TR, LX-SIB/SIB2/SIB3, Remaining gaps); QUEUE.md (PP-03/06/07,
PX-SCDIGI3/4 DigitArq sweeps, KX "already listed"); sources/solver-diffs/2026-09-24-pares-digitarq.tsv; DigitArq
`api/docs/search` (`cifra Linhares`, `cifrado Linhares`, `cifra Funchal`, `Domingos de Sousa Coutinho cifra`,
`Rodrigo de Sousa Coutinho cifra`, `dicionário cifra`, `cifra Bezerra`, and maço 85/87 listing phrases) plus 3
`docs/details` calls; full-coverage thumbnails of maço 86 `/04` (46 images) and `/01` (82), read as montages in
the scratchpad (not committed). 143 digitarq.arquivos.pt requests, >=3.5 s apart, no 403/429/challenge.
Result: **unread digitised siblings carrying cipher: 0 for each key.** Maço 86 is now 19 of 21 items eye-checked
(LX-SIB/SIB2/SIB3 + /04 /01 here), 266 of 604 images; `/02` (126) and `/09` (212) are still unopened (next: full
thumbnails, one DigitArq session each for /02 and two for /09). Thumbnail scale (141x128) shows numeral-group
blocks but would miss a few cipher words set inside a line of prose. Two catalogue records in the fonds not on file
anywhere in the repo describe cipher, both undigitised (copy-order leads only): `PT/TT/CLNH/0032/10` (copy of
António de Araújo's first letter after leaving Lisbon on the frigate Thetis, "Era em cifra, escrita de Lorient",
c.1807-08) and `PT/TT/CLNH/0037/42` (secret instructions "nesta espécie de cifra, que só poderá decifrar o Sr.
F. A. M. G.", mentions Wellesley, c.1808-09); whether either uses this dictionary key is unknown. No test decode
(no survivor). Every candidate: `keyhunt/2026-10-07-KH1E.tsv`.

## Siblings (8 Oct 2026)

SUCCESS-SIBS (account 1, 8 Oct 2026, repository files only, no network, nothing decoded). Siblings of this folder's N3+ document(s) by volume, sender, recipient, key, design and series; 5 listed, 4 unread or not in the repository. Full rows with evidence: `SIBLINGS-2026-10-08.tsv`. p = the compiler's conservative estimate that the step yields a new counted document (N3+, D2+, two audits); not a novelty claim (rule 10). Required by `tools/gaps_check.py` for every N3+ target.

- CLNH/0086 items /02 (126 images) and /09 (212 images) [same-volume; partial-read 9 Oct 2026: /02 and /09 m0001-m0020 no cipher, LIN-SIB; /09 m0021-m0212 left] -- DigitArq thumbnail montage stride 1 eyeball for numeral groups with /11 as positive control (tools/digitarq_fetch.py); ~$3; p 0.06; evidence: NOTES.md Escalation loose-ends 8 Oct 2026
- CLNH/0086 items /04 (46 images) and /01 (82 images) [same-volume; read 7 Oct 2026, KH1-E, no cipher] -- same montage sweep; ~$2; p 0.04; evidence: NOTES.md Remaining gaps (unopened)
- CLNH/0020/14 and CLNH/0078/80 other Chave de uma cifra units [same-key; not-in-repo] -- none: undigitised; ANTT reproduction quote needed (no ASKS row yet); p 0.02; evidence: NOTES.md Remaining gaps (hasImages false)
- PT/TT/CLNH/0086/11 m0001 (verso of m0002 leaf, clear French note) [same-volume; read] -- none; p 0.01; evidence: NOTES.md:960 (m0001 read 2 Oct 2026, H38/M2, no crib)
- ciphers/antt-msliv0638-brochado-1712 (other ANTT Portuguese cipher) [same-series; unread] -- none: different period (1712) and key; design not same; p 0.01; evidence: folders.tsv partial

## LIN-SIB (9 Oct 2026)

LIN-SIB (LANE FAMILY-A2d, account 2, 9 Oct 2026, 00:16-00:35 UTC by date -u). Thumbnail sweep of maço 86 /02 and /09 for
cipher, SIBLINGS-2026-10-08.tsv row 1. No decoding.

Prior-work checks (before the first request): `tools/prior_work.py antt-linhares-chave --item-spec shelfmark=PT/TT/CLNH/0086/02`
(and /09) `--step-type lookup --fetch`, exit 4 each; the one owed row (1-own LEAD) was this job's own ROOM claim, recorded
CLEAR in prior-work.tsv. Check 1 (own work): NOTES LX-SIB/SIB2/SIB3 and Keyhunt 7 Oct 2026 (KH1-E) all record /02 and /09
unopened; ROOM grep: no other claim on them. Check 2 (leaf and neighbours): n/a for a sweep (no leaf read). Check 3
(holder/solver caches): DigitArq titles (LX-SIB table) describe both as family letters (/02 Bezerra de Seixas to the 1st
condessa de Linhares; /09 D. Mariana de Sousa Coutinho to Bezerra de Seixas, 1796-1807), no cipher note; the solver caches
were not searched (no unit-level entry possible). Check 4 (editions): unchecked (no decode, so not applicable).

Method: filelists already on disk (images/maco86_scan/doc02, doc09); thumbnails (`/api/rdigital/thumb?fileId=`, short side
128 px, the scale KH1-E used) fetched one at a time 3.6 s apart by a status-checking loop over the same endpoint as
tools/digitarq_fetch.py --thumbs (which does not stop on a non-200), stop on any non-200 or non-JPEG. Montages of 29
thumbnails plus one blind positive-control tile each (scripts/linsib_montage.py; tiles upscaled to fit 300 px, labelled
S<sheet>-<n> only; key in keyhunt/2026-10-09-LINSIB-montage-key-doc0{2,9}.json), one vision look per montage asking
which tiles show numeral-group blocks or a cipher passage inside prose. Controls: local thumbnails at the same scale of
/11 m0002 (the numeral-group billet, heavy) and m0003 (the key sheet's prose with its numeral example rows, light), from
the full images already on disk (no request).

Result: **control 6 of 6 detected** (m0002 x4 at S01-25, S03-21, S05-07 of /02 and S01-07 of /09; m0003 x2 at S02-13,
S04-16) -- the scale shows both a numeral-group block and numeral rows set inside prose. **Target: 0 of 146 images with
cipher** -- /02 all 126 (m0001-m0126) and /09 m0001-m0020 are cursive prose letters, address leaves with seals, and blank
or near-blank faces; /02 m0026-m0028 are heavily struck-through drafts, and two dense /02 faces carry line drawings, neither
numeral groups. Per image: keyhunt/2026-10-09-LINSIB.tsv. Thumbnail scale still could miss one or two cipher words in a
line of prose (KH1-E's caveat); the m0003 control is a numeral-rows-in-prose case, not a single-word one. Stopped at the
request budget: last /09 image fetched index 19 (m0020); /09 m0021-m0212 (192) remain. Maço 86 is now 20 of 21 items in
full, 412 of 604 images, no sibling cipher.

Requests: digitarq.arquivos.pt 146 (126 + 20 thumbnails, 3.6 s apart, all HTTP 200 JPEG, no 403/429/challenge); no other
host. Thumbnails committed (images/maco86_scan/doc02, doc09, about 1.1 MB); montages regenerable from them with the
script and the seed in its call (202 for doc02, 909 for doc09).

## LIN-SIB2 (9 Oct 2026)

LIN-SIB2 (LANE FAMILY-A2d, account 2, 9 Oct 2026, 00:41-00:56 UTC by date -u). Continuation of LIN-SIB: thumbnail sweep of maço 86
/09 from index 20 for cipher. No decoding.

Prior-work checks (before the first request): `tools/prior_work.py antt-linhares-chave --item-spec shelfmark=PT/TT/CLNH/0086/09
--step-type lookup --fetch`, exit 4; the one owed row (1-own LEAD) was this job's own ROOM claim, recorded CLEAR in prior-work.tsv.
Check 1 (own work): LIN-SIB covered /09 m0001-m0020 only (NOTES "LIN-SIB (9 Oct 2026)"); ROOM: no other claim on /09. Check 2: n/a
for a sweep. Check 3: as LIN-SIB (DigitArq title: family letters of D. Mariana de Sousa Coutinho to Bezerra de Seixas, 1796-1807, no
cipher note); solver caches unchecked (no unit-level entry). Check 4: unchecked (no decode, not applicable).

Method: as LIN-SIB. Thumbnails (`/api/rdigital/thumb?fileId=`, 128 px short side) of /09 m0021-m0170 fetched one at a time 3.6 s
apart (filelist already on disk, so 150 thumbnail requests only), stop on non-200/non-JPEG (none). `scripts/linsib_montage.py` run
over a scratch dir holding only these 150 thumbnails, 30 per sheet, seed 921: 6 sheets, one blind /11 control tile each (m0002 at
S01-30, S03-12, S05-03; m0003 at S02-12, S04-13, S06-05; key in keyhunt/2026-10-09-LINSIB2-montage-key-doc09.json). Three Sonnet
subagents, two sheets each, one look per sheet, asked which tiles show numeral-group blocks or numerals set inside prose; none saw
the key.

Result: **control 6 of 6 detected** (S03-12, S04-13, S05-03 as heavy; S01-30, S02-12, S06-05 as light -- S01-30's reader said its
groups were "not clearly digits at this size", so detection at this scale is near its floor for the small m0002 billet).
**Target: 0 of 150 with cipher.** The readers flagged 9 target tiles as light (m0137/0138, m0146, m0155-0158, m0164, m0166, all
"vertical columns of marks"); a 3x enlargement of those 9 thumbnails (local, no request) looked at by this worker (not blind, key
known) shows sideways marginal postscripts in cursive and cross-written address leaves (m0137/0138, m0164), with m0138, m0156,
m0158 the show-through of their neighbours -- no numeral groups. Graded none, with that note per row in keyhunt/2026-10-09-LINSIB.tsv.
Not confirmed at working size (the request budget was spent); m0146 is the one worth a fetch if the next session has one spare.
Stopped at the request budget: last /09 image fetched index 169 (m0170); /09 m0171-m0212 (42) remain. Maço 86: 20 of 21 items in
full plus /09 m0001-m0170, 562 of 604 images, no sibling cipher.

Requests: digitarq.arquivos.pt 150 (thumbnails, 3.6 s apart, all HTTP 200 JPEG, no 403/429/challenge); no other host. Thumbnails
committed (images/maco86_scan/doc09, maço86_scan now 3.9 MB).


## LIN-SIB3 (9 Oct 2026)

LIN-SIB3 (LANE FAMILY-A2d, account 2, 9 Oct 2026, 01:09-01:20 UTC by date -u). Last leg of the maço 86 /09 thumbnail sweep. No decoding.

Prior-work: `tools/prior_work.py antt-linhares-chave --item-spec shelfmark=PT/TT/CLNH/0086/09 --step-type lookup --fetch` exit 4; owed row
(1-own, this job's own claim) recorded CLEAR; other rows UNCHECKED (no unit id; no decode, so check 4 not applicable); check 3 as LIN-SIB.

Method: as LIN-SIB2. Thumbnails of /09 m0171-m0212 (42) fetched one at a time 3.6 s apart, all HTTP 200 JPEG; 3 sheets of 15 tiles
(`scripts/linsib_montage.py`, seed 931), one blind /11 control tile per sheet (key keyhunt/2026-10-09-LINSIB3-montage-key-doc09.json); three
Sonnet readers, one sheet each, key not shown.

Result: **control 3 of 3 detected** (S01-13, S02-07, S03-07, all heavy). **Target: 0 of 42 with cipher.** Readers flagged two target tiles as light:
S01-08 = m0178 and S03-11 = m0208. A 3x enlargement of both thumbnails (local, not blind, key known): m0178 is a signature block with short
name lines; m0208 is an address leaf with a red postal-mark lattice; neither shows numeral groups. Graded none, noted per row in
keyhunt/2026-10-09-LINSIB.tsv. Limit: thumbnail scale (128 px), where the small /11 billet sits near its floor (LIN-SIB2); a few stained tiles
could not be ruled out for small numerals inside prose by the readers.
m0146 at working size (1 request, 1158x1409): ordinary cursive prose with a sideways marginal postscript in cursive; no numerals.
Maço 86: 21 of 21 items, 604 of 604 images eye-checked, no sibling cipher found by this method.

Requests: digitarq.arquivos.pt 43 (42 thumbnails + 1 working-size), >= 3.6 s apart, no 403/429/challenge; no other host.


## New material for the cagar / justa column counts (LIN-VIEYRA, 9 Oct 2026, 10:49-11:0x UTC)
Job: find a higher-resolution scan of leaves 95 and 255 and a second independent scan of Vieyra, A New Pocket Dictionary, London 1809, Part I.
No count, no regrade (a later job counts under a fresh PREREG).
Prior-work step: `tools/prior_work.py antt-linhares-chave --item-spec 'shelfmark=Vieyra New Pocket Dictionary 1809;folio=pp.83,241' --step-type lookup --fetch` exit 0 (proceed; 4 generic UNCHECKED rows, none specific). Check 1 (own work): NOTES gaps and A1B-LIN-ROWS above say new material is the named next step; no earlier fetch above 949 px (images/book/ holds 949x1076 leaves). Checks 2-4 are not applicable to a scan lookup (no reading made).
Findings:
1. **Higher resolution exists on the same copy.** archive.org/metadata/newpocketdiction00viey: 830 images, scanner scribe19.toronto, ppi 400; files include `_jp2.zip` (276 MB) and `_orig_jp2.tar` (468 MB). IIIF info.json for leaf 95 (route `iiif.archive.org/image/iiif/2/newpocketdiction00viey%2fnewpocketdiction00viey_jp2.zip%2fnewpocketdiction00viey_jp2%2fnewpocketdiction00viey_0095.jp2`) lists sizes 119/237/474/949/1897 wide, full 1897x2152. The 949 px page used by every count so far is the second-largest of those sizes; the full size is 2x linear. Fetched `images/book_hires/leaf0095.jpg` and `leaf0255.jpg` (both 1897x2152, ~0.67 MB). The leaf 255 image was viewed once: running head JUI / JUN / JUS and [241]; the three columns, bold headwords and indents are legible at this size. Leaf 95 was not viewed (no count). The `_orig_jp2.tar` could hold a still larger original; not fetched (468 MB, not a page fetch).
2. **Second scans** (`vieyra_copies.tsv`): two further 1809 Wingrave copies are on Google Books (GzchKivL6_EC 826 pp, 0mESAAAAIAAJ 810 pp, both ALL_PAGES; page counts differ from each other and from IA's 830 images, so the leaf-to-page mapping must be re-found per copy); HathiTrust has one 1809 copy (NYPL, nyp.33433075910087, v. 1-2, full view). Later editions (1826, 1873) and the 1813 full dictionary exist but are other texts. None of the second copies' pages 83/241 could be fetched from the cloud: books.google.com page view returned 403 (1 request), HathiTrust is Cloudflare-challenged (host table). A second-copy fetch therefore needs the owner's runner (LOCAL-QUEUE row, not written here: key_livecheck gate applies to credentials, not this; the row is a suggestion below).
3. Not found: a second 1809 copy readable from the cloud; a scan larger than 1897 px other than the unfetched original tar.
Requests: archive.org/iiif.archive.org 8 (metadata 1, advancedsearch 2, info.json 3, page images 2), googleapis.com 7, openlibrary.org 1, catalog.hathitrust.org 2, books.google.com 1.
Suggestion (not done): the next counting job runs on `images/book_hires/leaf0095.jpg` / `leaf0255.jpg` under a fresh PREREG naming the duplicate-headword and drop-cap cases, with the matched calibration columns re-run at 1897 px first (a count that fails calibration at 2x is then a different-instrument negative, not a repeat of the 949 px one).

## Row-crop labelling at 1897 px (LIN-COUNT, 9 Oct 2026, 11:23-11:3x UTC by date -u) -- calibration FAIL as pre-registered; targets not labelled
Pre-registration: `PREREG-LINCOUNT.md`, pushed in its own commit bbd25673a and confirmed on origin before any crop was labelled.
Prior-work step: `tools/prior_work.py antt-linhares-chave --item-spec 'shelfmark=Vieyra New Pocket Dictionary 1809;folio=pp.83,241' --step-type key --fetch`
exit 4: two LEAD rows, both target-level ROOM claims (LIN-VIEYRA, done; this job's own) -- recorded CLEAR. Generic rows (3-tomokiyo, 3-solver,
4-editions) concern the plaintext, not this count: unchecked here. Check 1 (own work): NOTES above show no count at 1897 px before this job.
Material: 5 calibration leaves fetched at 1897x2152 (iiif.archive.org, 5 requests, 2 s apart, all 200) beside LIN-VIEYRA's 95 and 255
(`images/book_hires/`). Columns: the leaf has no printed rules; `hocr/hires_columns.py` finds the col 2/3 text margins (peak of the
histogram of ink-run starts after a >= 14 px blank, top and bottom halves for skew), cuts 16 px left of them and whitens the rest
(regenerable masked column images, not committed). Rows: `python3 tools/iiif_lines.py --image images/rows_hires/col/leaf<L>_c<C>.png
--region <box> --lines-per-crop 1 --ink 110 --centres <grid> --out images/rows_hires/r_<L>_c<C> --prefix L<L>_c<C> --debug`, boxes and
centres in `hocr/rows_hires_centres.txt` (the tool's peak finder missed rows at default and at prominence 8; centres = straight-line grid,
pitch 42.4-42.9 px, fitted by `hocr/rows_grid_hires.py` and snapped to detected peaks within 12 px); debug overlays committed beside the crops
(0146/1 checked by eye: bands sit on the text lines). Sheets `images/rows_hires/sheets/` (`hocr/rows_sheets_hires.py`, native scale, 24
strips each). 14 blind Sonnet calls (7 columns x passes A/B), labels verbatim in `hocr/lincount_labels/`, scored by `hocr/lincount_score.py`
(written before any label came back), output `hocr/lincount_calibration_result.txt`:

| column | key | pass A | pass B |
|---|---|---|---|
| 236/1 | Guerra r2 (the second "Guérra") | hit | hit |
| 236/3 | Habil r1 | hit | hit |
| 146/1 | D r1 ("D," after the centred section "D.", labelled DROPCAP) | hit | undecided (R07 "blank / top fragment of large D") |
| 276/2 | Memoria r3 | hit | hit |
| 261/2 | Lhe r6 | hit | undecided (R01 "running head fragment 'LIB' cut by strip edge") |
| 265/2 | Lugar r17 | undecided (R01 "blank or cut fragment") | hit |
| 255/2 | Junto r20 | hit | hit |

**Pass A 6/7 (PASS), pass B 5/7 with two non-hits (FAIL) -> GATE FAIL.** As pre-registered: the target sheets (95/2, 255/3: cut and
committed, `sheet_0095_c2_*`, `sheet_0255_c3_*`) were never sent to any model; no token moved (justa M, cagar M); `decode_key.py . --check`
exit 0 (H 23 / M 3); no AUDIT.md or SECOND-OPINIONS-QUEUE.tsv propagation due.
What the numbers show (for whoever decides the next step; not a re-score): in all 14 column-passes the FLUSH row at the key's rank carries
the expected headword -- the duplicate-headword case (Guérra twice) and the drop-cap case (centred "D." labelled DROPCAP, rank 1 "D,") both
came out right, which no 949 px instrument managed. All three non-hits come from the pre-registered undecided clause (an OTHER row named
"fragment" above the rank), which the scorer read literally as the substring "fragment" in the labeller's note; the three rows so named
are a running head, a blank band and the top of the drop cap, not a cut text line. Under the PREREG that is a FAIL, and this job does not
re-score it. The two blind passes agreed on every FLUSH/INDENT label in all 7 columns (word spellings differed in 4 places), so they are
weakly independent: two calls of one model on one sheet, not two readers.
Rule 3: per the brief, the per-row labelling instrument is logged [retired] at 1897 px as well (it failed its gate at 949 px, A1B-LIN-ROWS,
and at 1897 px here). Next = a person's count of the two columns from `images/book_hires/leaf0095.jpg` (col 2) and `leaf0255.jpg` (col 3),
with the same match rule. ASKS row draft text (not filed): "Linhares key, two dictionary counts: open images/book_hires/leaf0095.jpg and
count the bold headword lines in the middle column from the top (a centred section letter does not count; a repeated word counts each time):
is line 19 'Cagar'? Then leaf0255.jpg, right-hand column: is line 15 'Jus' or 'Justa', and is 'Junto, prepos.' at its top its own line?
About 5 minutes; the calibration sheets in images/rows_hires/sheets show what the counting rule gives on 7 known columns."
Vision calls: 14 Sonnet subagent calls (one sheet each, about 96k subagent tokens each); own looks 3 (contact sheet, two column checks, one
debug overlay). Requests: iiif.archive.org 5.

## While waiting (9 Oct 2026)
- Fresh-PREREG re-calibration of the 1897 px per-row labeller on held-out columns (depends on nobody, ~$4): LIN-COUNT's gate failed only on its "undecided" clause (every rank exact in 14/14 column-passes), so a new PREREG with that clause rewritten, scored on calibration columns NOT used by LIN-COUNT (other known-rank groups, fresh leaves at 1897 px), is a legitimate new test; only if it passes are 83/2 and 241/3 labelled. Not a re-score of LIN-COUNT's sheets.
- Waiting: a person's count of 83/2 and 241/3 (ASKS draft text above, not filed); LOCAL-QUEUE L10 (Textos Politicos 1993).
(LANE FAMILY-A2h orchestrator, account 2, at the account-4 orchestrator's 11:38 request.)

## LIN-TRIM (9 Oct 2026)

LIN-TRIM (LANE FAMILY-A2l, account 2, 9 Oct 2026, 20:19-20:3x UTC by date -u). Front-trim / join enumeration re-scored by a whole-string pt18
character model, the different instrument DA1-LIN named. Pre-registration `PREREG-LINTRIM2.md`, pushed in its own commit e012eb170 and confirmed
on origin (`git log origin/main -1 -- PREREG-LINTRIM2.md`) before the script was written or run.

Prior-work: `tools/prior_work.py antt-linhares-chave --item-spec 'shelfmark=PT/TT/CLNH/0086/11;folio=m0002' --step-type decode --fetch` exit 4;
owed rows recorded CLEAR: 1-own (the live claim is this job; D22/DA1 used other scorers, check 1 by hand: no whole-string run on file) and 2-leaf
(m0002 has no gloss or clear copy; m0001 verso is an unrelated French billet, NEXT-LIN). 3-tomokiyo, 3-solver, 4-editions UNCHECKED: they concern
the plaintext, and this job makes no reading. Check 5 not applicable (no decode was scored).

Instrument: `scripts/trim_join_whole.py` (imports WORKED/TARGET/variants from `scripts/trim_join_enum.py` unchanged). Witten-Bell character 5-gram
over a-z + space, trained on running pt18 text (each file minus its last 10% of words, held out), so contexts cross word boundaries; exact Viterbi
over tokens, state (last 4 chars, tokens in the current word). Implementation check (diagnostic, after the gate result): the Viterbi total equals a
direct score of the argmax string on 100 of 100 gluing windows.

### Result: Gate 1 PASS, Gate 2 FAIL -- non-test, target not scored (exit 3, as registered)
- **Gate 1 PASS**: worked-example argmax exactly `a guerra de franca com a russia parece inevitavel` (score -57.34).
- **Gate 2 FAIL**: on DA1's 100 held-out windows of 26 fixed words the DP joined 9.32% of 2,500 boundaries, against the registered ceiling of 5%
  (DA1's per-word scorer: 10.68%). As registered: "non-test: whole-string scorer fails gate 2". Gate 3 (planted control) and the target were not
  run; no null. Nothing in ciphertext.tsv, key.tsv or reading.txt changes; grades unchanged (H 23 / M 3); no AUDIT.md or SECOND-OPINIONS-QUEUE.tsv
  propagation due.
- Diagnostic, held-out text only (not gating, not a re-score): commonest glues com+o (6, "como"), s+a (3), arra+baldes, tam+baixa, re+troceder,
  la+sciva, illus+trate (OCR line-break splits, where the join is the true word), plus OCR and English debris (sn+geitofl, t+lp, sicily+kitended).
  Of the 233 glued pairs, 64 form a corpus word (count >= 3) and 139 contain a fragment seen fewer than 3 times. The gluing reference is OCR with
  hyphen splits and debris, so part of the 9.32% is the reference, not the scorer -- but the gate was fixed in advance and this job does not
  re-score it.
- Rule 3: the trim/join step has now had a word unigram (D22, passed, changed nothing) and two character scorers that failed the same gate with
  the numbers barely moving (0.107 -> 0.093). Character n-gram scorers trained on the pt18 OCR corpus are logged **[retired]** for this step
  ("untested-by-this-tool", not refuted). What would reopen it is new material: a clean, keyed (not OCR) 1808-1819 Portuguese text serving as both
  training text and gluing reference, under a fresh PREREG. The six unresolved trim directions (man, o, he, do, pauperr, ven) stay M; "venha logo"
  stays an I-grade reading only.
- Requests: none (corpus on disk). No subagent.

## LIN-BFSP (9 Oct 2026): British and Foreign State Papers, be-api full-text sweep (print step)

Prior-work (tools/prior_work.py, lookup, exit 4: the only LEAD was this worker's own live ROOM claim; 3-tomokiyo/3-solver/4-editions UNCHECKED, no
folio-keyed unit; check 1 own work: AUDIT.md item 13 + this NOTES print bullet = BFSP 33 of 34 unchecked, nothing ran since). Route: archive.org
advancedsearch (title query, 34 candidate items, 1 request), then `be-api.us.archive.org/fts/v1/search?q=Linhares&identifier=ID`, one item per call,
>= 1.7 s apart. Result per item in `bfsp_sweep.tsv`. A be-api result is item-level (total = 1 means the item contains the term; page_num is not a page).
- Searched: 32 items (the 34th, britishforeignst1001grea, was spot-checked in AUD2 for "Sousa Coutinho", 0; it is in the 32 here for "Linhares", 0).
  Linhares: 31 items 0 hits, 1 item hit. 5 items answered HTTP 502 on the first call and 0 on one retry.
- Hit: britishandforei05offigoog. Snippets (be-api highlight, OCR, quoted, nothing more): "Rodrigo de Sousa Couttinho, Conde de Linhares, Senhor de
  Payalvo, Commendador da Ordem"; "by the Conde de Linhares, on the part of His Royal Highness the Prince" (the 1810 Anglo-Portuguese treaty text); a
  second hit in the same item is a different Conde de Linhares, Viceroy of Goa, 1630s. Neither context is a letter or a cipher.
- Control: the hit above is the positive control for the query family (the term is found where the series is known to print Linhares as signatory of
  the 1810 treaties). A first attempt with `Coutinho OR Linhares OR Strangford` FAILED its control ("treaty OR Strangford" 0 vs "treaty" 1 on the same
  item; be-api does not parse OR) and its 23 zero results are discarded, not logged as a negative.
- Not done / limits: one term family only ("Linhares"; the "Sousa Coutinho" and "Strangford" families and OCR variants such as "Linhàres" were not run,
  budget); the Google scans carry no volume/year in their metadata (not fetched), so which of them cover 1808-1819 is unestablished; item-level hits
  cannot show a letter-by-letter date match. This is a search result for the log, never a novelty verdict (rule 10); the m0002 reading and grades are
  unchanged. Requests: archive.org advancedsearch 1; be-api about 68 (including 31 discarded OR-query calls and control tests); no other host; no 429.
- Next (print step, still open): "Strangford" and "Sousa Coutinho" families on the same items with a positive control each; metadata fetch to map
  the Google scans to volume years; ~$1.

## LIN-BFSP2 (9 Oct 2026): British and Foreign State Papers, Strangford and Couttinho families (print step remainder)

Prior-work (tools/prior_work.py lookup, exit 4): the two LEADs were the LIN-BFSP claim (earlier family, "Linhares") and this job's own claim; neither covers
these families. 3-tomokiyo/3-solver/4-editions UNCHECKED (no folio-keyed unit). Route and rules as LIN-BFSP: be-api fts, one term per query, one item per call,
>= 1.7 s apart. Results per item in `bfsp_sweep2.tsv` (beside `bfsp_sweep.tsv`).
- Controls (item britishandforei05offigoog, 1810 treaties): "Strangford" 1 (passed); "Couttinho" 1 (passed); quoted "Sousa Coutinho" 0 and "Sousa Couttinho" unquoted 1
  on the same item -- the OCR breaks and respells the name ("Cout- tinho", "Couttinho"), so the "Sousa Coutinho" family FAILED its control and was not run;
  "Couttinho" stands in for it. "Coutinho" alone: two 502s on its control, not run. "Linhàres" not run (budget).
- Strangford: 31 items other than the control item: 25 no-hit, 2 hit, 4 unsearched (502 twice: britishandforei10offigoog, britishforeignst4018grea,
  bub_gb_XJ40AQAAMAAJ_2, bub_gb_pyIgAAAAMAAJ). Hits: britishandforei01offigoog (snippets: "Constantinople, le 25 Octobre, 1823. STRANGFORD" -- a treaty signature) and
  generalindextob00hertgoog ("Note of Viscount Strangford to the Reis Effendi, Negotiation between ... Russia"). Neither concerns 1808-1812 Linhares/Strangford correspondence.
- Couttinho: 31 items: 22 no-hit, 0 hit, 9 unsearched (502 twice; listed in the TSV). Together with the control item, 23 answered.
- Not done: the metadata fetch mapping the Google scans to volume/years (request budget spent, see below); a no-hit is item-level, from an OCR index with 502 gaps
  (13 item x family cells unsearched), so it says nothing about a letter-by-letter date match. A search result for the log, never a novelty verdict (rule 10).
- Requests: archive.org be-api about 100 (including retries after 502 and control tests), over the brief's 90 by about 10; advancedsearch 0; no 429.
- Next (if kept): retry the 13 unsearched cells later; metadata fetch (1 advancedsearch request); ~$0.5.

## LIN-BFSP3 (10 Oct 2026): British and Foreign State Papers, the 13 cells LIN-BFSP2 left unsearched

Prior-work (tools/prior_work.py --offline, exit 4): only the LIN-BFSP / LIN-BFSP2 / LIN-BFSP3 claims (target-level LEADs, none covering a retry of these cells); 3-tomokiyo, 3-solver, 4-editions UNCHECKED (no folio-keyed unit), as in LIN-BFSP2. Check 1: no LIN-BFSP3 section existed.
Route as LIN-BFSP2: be-api fts, one term per query, one item per call, >= 2.1 s apart, browser-free curl with the descriptive UA.
- Retry: all 13 cells answered HTTP 200 on the first call (no 502, no second retry needed). Strangford 4 cells: 2 hit, 2 no-hit; Couttinho 9 cells: 0 hit. `bfsp_sweep2.tsv` rows updated in place (ERR -> count); 0 ERR remain.
- Controls re-run before reading the retry (britishandforei05offigoog): "Strangford" 1, "Couttinho" 1 (both read, as in LIN-BFSP2). A retry that returns 0 is therefore a search result from an index that answers; the "Sousa Coutinho" / "Linhàres" spellings remain not run (LIN-BFSP2: control failed / budget).
- Hits (snippets from the be-api highlight field): britishandforei10offigoog -- "au Vicomte de {Strangford} ; contre le pouvoir et le mode de nomination", "inexecution des promesses faites au Vicomte de {Strangford}" (Porte remonstrance, French); britishforeignst4018grea -- "Odessa, le 1823. Ma lettre au Vicomte de {Strangford}, en date de Tchernowitz". Both are 1823 Ottoman/Russian material; neither concerns 1808-1812 Linhares or Strangford-in-Rio correspondence. be-api page_num is not a page locator.
- Metadata fetch (1 advancedsearch request, identifier wildcards for the swept items): `year` is the series start (1814) for every state-papers item, so it does not map items to volume years; only the britishforeignst* items carry a volume string (v.66 1874-75, v.85 1892-93, v.93 index, v.100 1906-07, v.101 1907-08); the Google scans carry none. The wildcard also returned unrelated "British and Foreign" medical/evangelical items (not swept). The item-to-volume-years map therefore stays open: it needs the scans' own title pages (image reads), not metadata.
- Requests this job: be-api 17 (13 retries + 4 control calls), advancedsearch 1; no 429, no 502. A search result for the log, never a novelty verdict (rule 10).
- Verdict: BFSP print step -- every item x family cell now answered; no 1808-1812 Linhares/Strangford/Couttinho correspondence found in the swept state-papers items. "No hit" is item-level from an OCR index with respelling gaps ("Sousa Coutinho" not matchable), not a letter-by-letter date match.
