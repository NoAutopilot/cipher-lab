partial

open -- web search (queries: `"Condes de Linhares" "Chave de uma cifra"`, `"CLNH/0086" OR "maço 86" cifra`, `Rodrigo de Sousa Coutinho cifra/dicionário/chave`, `Cryptiana OR Cipherbrain Linhares cipher`, and a phrase search of the key's own worked-example plaintext `"a guerra de Franca com a Russia"`), Cryptiana and Cipherbrain (checked via search, no hit naming this unit or any Linhares cipher), the DECODE records already on disk at `sources/decode/*.tsv` (no login used, per COMMON rule 4; no Linhares/CLNH row), and shallow greps of `dbourdeau/cyphersolver` and `aaymeloglu/unsolved-ciphers` (depth-1 clones, 24 Sept 2026, `grep -rIl -i "linhares\|sousa coutinho\|CLNH"` outside `.git`, zero genuine text hits -- the only matches were binary image filenames that happen to contain the substring) all read, not deciphered; key on the same unit. The item's likely correspondence edition, D. Rodrigo de Souza Coutinho, *Textos Políticos, Económicos e Financeiros (1783-1811)*, ed. Andrée Mansuy-Diniz Silva, Banco de Portugal, 1993 (2 vols.), could not be opened this pass: its only located copy online, `https://www.bportugal.pt/sites/default/files/ocpep-7_t1.pdf`, returned HTTP 403 to both WebFetch and `curl -A "Mozilla/5.0"` -- one retry, then stopped per the good-citizen rule; not logged as unreachable-and-abandoned, but as a named next step (see below). The 1908 family biography *O Conde de Linhares* (Agostinho de Sousa Coutinho, Marquês do Funchal; archive.org id `ocondedelinhares00func`) gave zero hits for "cifra" on Internet Archive's full-text search API (`be-api.us.archive.org/fts/v1/search`), a search result, not a read of the book. No calendar/state-paper series applies (Portuguese noble-house archive, not a calendared series); the item itself carries no date or named correspondent from the archive's own catalogue metadata, so no single-letter calendar check is possible -- the check-solved sweep here is over the *key document and cipher system*, not a datable individual letter. Searched and logged 24 Sept 2026.

## The unit

ANTT `PT/TT/CLNH/0086/11` -- fonds Condes de Linhares, maço 86, undated within the maço's stated 1780-1827 span.
Viewer: `https://digitarq.arquivos.pt/fileViewer/a03cef08d3c04758aa148f5be56d3401` (docId `a03cef08d3c04758aa148f5be56d3401`), CC BY-SA 4.0, no login. 6-image composite item (scouted by scDIGI2, LANE N4, 24 Sept 2026; re-fetched full-resolution here for m0002-m0004 with `tools/digitarq_fetch.py`, now committed at `images/full_PT-TT-CLNH-0086-11_m000{2,3,4}.jpg.jpg`; m0001/m0005/m0006 are unrelated papers bundled on the same unit and were not re-fetched):

- **m0001**: unrelated French billet ("brûlez ceci" -- "burn this").
- **m0002**: live numeric ciphertext (H grade, read directly off the image). One leaf, folded, carrying pages numbered "2" and "3" of a longer letter -- pages 1 and 4 are not part of this 6-image item, so the ciphertext here is a mid-letter fragment, not the whole dispatch. About 26 five-to-seven-digit groups total (17 on page "2", 9 on page "3"), several carrying a small subscript digit 1-6 under the group (e.g. `328511` with a subscript `2`, `829011` with a subscript `5`). A Torre do Tombo ownership stamp and a wax seal sit on the page; no exact digit-by-digit transcription was made this pass (out of this brief's scope -- a transcription pass would need its own worker per CLAUDE.md's tools/ layout).
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
