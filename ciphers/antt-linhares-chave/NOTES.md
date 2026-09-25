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
