open

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
  1131/2   322212.  313312.  321118(1)  23312(3)  311021.  1412(5)
  a        guerra   de       Franc[a]   a         com      a
  3344325(4)  335422(5)  1811(4)  3290219(1)  3234124.
  Rus[sia]    si         a        parece       inevitavel.
  ```

  Read together: "a guerra de Franca com a Russia parece inevitavel" ("the war of France with Russia seems inevitable"). Note (M grade, my inference, not stated by the key text): "Franca" and "Russia" are not looked up whole -- the key trims a dictionary headword down to a fragment ("Franc", "Rus") and, for Russia, stitches three separate lookups together ("Rus" + "si" + "a"). So a proper noun or inflected form missing from the dictionary is spelled by concatenating trimmed fragments of several dictionary words, the way a syllabary or nomenclator code pads out a fixed vocabulary. This is a real mechanical detail of the system, worth knowing before any decode attempt, but it is read off one example, not asserted by the key's own prose.

## The book

**Not identified.** The key names only "o Diccionario" and, for the null-padding case, "o Diccionario Inglez" -- no title, author, edition or year anywhere on m0003-m0004. A page range of 1-999 (pages of 1 to 3 digits) with 3 columns per page is compatible with a great many dictionaries of the period (a "Diccionario" without qualifier, for a Portuguese diplomatic household of this date, is most likely a Portuguese-language dictionary -- plausibly Rafael Bluteau's *Vocabulario Portuguez e Latino* or a later single-volume abridgement, or a bilingual Portuguese-English dictionary such as Anthony Vieyra Transtagano's, which would also explain how the same physical work could double as "the English dictionary" the key describes switching to -- but nothing on the leaf supports picking one of these over another, so this stays a guess, not a finding). No specific edition is therefore online to check against. **Kind: blocked on the book** (not "recovery" -- the system is fully known, but the concrete lookup table it points to is not).

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

H (read from the image): the ciphertext's presence and rough extent on m0002; the key's full text and worked example on m0003-m0004.
M (inferred, not stated by the source): the fragment-concatenation mechanic for proper nouns; the family-member/date attribution above.
No book, key application, or decode was attempted -- the book is unidentified, so no group was decoded, per this brief's instruction to decode only if the book is online.

## Next steps (not run this pass, budget)

- Try to identify the specific "Diccionario" (candidates above are guesses); a period Portuguese-household dictionary bibliography search, or an ANTT archivist's note, might narrow it.
- Re-try `bportugal.pt`'s Textos Políticos PDF from a different route (it may simply block the proxy's egress IP; a direct browser fetch was not tried).
- Decode `ciphertext.tsv` once the dictionary is identified (LX-BOOK).

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
