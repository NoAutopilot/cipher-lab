# AUDIT: rah-canada-1869, "Nota cifrada del Conde de la Cañada" (RAH 9/6958, Leg. XIX nº 117/2-3)

Verifier: LANE W worker E (Opus), 24 Sept 2026, 07:12-07:25 UTC. Parent orchestrator session_011UFnhZnyCntZ8Bn9FpKyTq.
This session did not solve the item. It did not decode anything and does not defend the solver's conclusions.

Claim under audit (NOTES.md, R8 section; status.json results row): "every cipher line of 117/2-3 read, 667 cipher
signs: H 665, M 2 ... a recovery from the document, not a cryptanalytic result." The repo made no novelty claim. This
audit decides the class.

## Verdict

| Item | Class | Prior plaintext | Prior decipherment | Evidence | Confidence |
|---|---|---|---|---|---|
| Nota cifrada, 117/2-3, "Hoy 15 Noviembre" [1869] | **N0** | **Yes, on the item itself.** Every cipher line sits under a clear Spanish line in the same hand. The clear text went to the Queen with the cipher ("La remito tal y como ha sido recibida"). The page has been public-domain and online at bibliotecadigital.rah.es since at least 4 Mar 2020 (OAI datestamp; catalogue record created 21 Oct 2010). | Yes, in substance: the item carries its own plaintext, so it has been readable ever since it was written. No printed key table or sign-by-sign mapping was located. | Strong. I checked it on the page image (117/2): clear lines with the cipher interlined beneath them, one hand. | High |

**Safe sentence:** "The Conde de la Cañada's note (RAH 9/6958, Leg. XIX nº 117/2-3, 15 Nov 1869) carries its own clear
Spanish text above each cipher line. We aligned the two to set out its simple substitution key (28 signs), and the key
reproduces the note's clear text (N0: the plaintext was already on the item)."

**Unsafe sentence:** "We deciphered/solved/read for the first time the Conde de la Cañada's ciphered note to Isabel II."
Also unsafe: "unsolved", "open cipher" or "cryptanalysis candidate" for this item, and "recovered the plaintext".
The plaintext was never lost. What this project produced is the key table and a machine check of the alignment.

## 1. Item extract

- **Date:** "Hoy 15 Noviembre", with no year on the note. The covering letter is dated Biarritz, 18 Nov 1869, and the
  catalogue gives 18 de noviembre de 1869. The note's occasion is the Queen's saint's day (Santa Isabel, 19 Nov).
- **Sender:** the Conde de la Cañada. He signs "El Conde de la Cañada" in clear and in cipher. The title is not
  identified further here. **Intermediary:** Luis González Bravo, former Ministro de la Gobernación, in exile in
  Biarritz. **Recipient:** Queen Isabel II, in exile after Sept 1868.
- **Plaintext (clear lines on the leaf, as read by R8):** Cañada asks González Bravo to pass the note to the Queen. He
  congratulates her on her saint's day and hopes to do so again with her "sentada ... en el trono de San Fernando".
  He writes that "gana por momentos la idea de la justisima restauracion" and that "nadie me aventaja en deseos de ser
  uno de los primeros que se jueguen su vida por llevarla a feliz termino". It closes "A.L.R.P. de VV. MM. y Real
  familia".
- **Ciphertext:** `ciphertext.tsv`, 26 lines, 667 signs: digits plus pen marks, simple letter substitution
  (NOTES.md R8).
- **Identifiers:** RAH Sig. 9/6958; Legajo XIX, nº 117 (/1 is the covering letter, /2-3 the note); record id 14495;
  MARC control RAH20100072714; images idImagen 10137299-10137303; OAI id oai:bibliotecadigital.rah.es:14495.
- **What the solver side searched** (NOTES.md 'Editions-first', 'Six-source sweep', R8 search log): WebSearch x2;
  sources/cryptiana grep; the Aymeloglu DECODE/BNE/PARES catalogues; both solver repositories; Google Books x3 (LANE S).
  Their stated gaps were the RAE copies (403), the two Historia Contemporánea articles, and DECODE.

## 2. Central question: what does the interlinear clear text do to the class?

Rule 10 defines N0 as "plaintext and decipherment of this very item already known". The fr5160 precedent
(`ciphers/fr5160-letellier-1653/AUDIT.md` s.2) ruled that N0 does not need print. A manuscript decipherment of the
item, publicly viewable and described in the catalogue, is enough.

This item is a stronger N0 than fr.5160:

1. **The clear text is not a later gloss by a recipient. It is the note's own text.** On 117/2 the clear Spanish runs
   in normal cursive, with the cipher line written in beneath each line in the same hand and ink. The cipher does not
   break where the clear lines break: it runs on about half a line behind (R8). That fits a clear text written first
   and enciphered underneath it, an encipherment laid out with its own clear text. It does not fit a decipherment
   added afterwards. Either way the plaintext of this very item is on this very item.
2. **The plaintext was delivered with the cipher.** González Bravo's covering letter (117/1) says he sends the note
   "tal y como ha sido recibida". The Queen received the clear text and the cipher together. At no point in its
   history was the note unreadable to anyone who held it.
3. **The item is catalogued and public.** The MARC/DC record names it "Nota cifrada del Conde de la Cañada". The record
   was created 21 Oct 2010 and its OAI datestamp is 4 Mar 2020. The images are public domain (CC PDM) and anyone can
   read the clear lines on screen. The catalogue does not transcribe the note or say that it carries its own clear
   text. That is the same caveat fr.5160 had: catalogued at item level, contents not described.
4. **N3 would be false on its own terms.** N3 means "no prior plaintext or decipherment located". A plaintext was
   located, on f.117/2-3 itself. N1 and N2 describe plaintext known from another source, which is not the case here.

**Ruling: N0.** Qualifier: the known plaintext is manuscript and on the item. No print of the note, its plaintext or
its key was found (section 3). The only thing this project added that may not exist elsewhere is the explicit
sign-to-letter table (key.tsv) and the machine-checked alignment. That is a small dataset, not a decipherment. It may
be described as "key table set out from the note's own clear text", with no novelty qualifier.

**Result kind:** **recovery**. The key was taken from the item's own clear text (README: "a key that opened it is
recovery"). An argument for **contribution** exists, since the deliverable is a dataset (key table + aligned
transcription) handed on. It is not cryptanalysis: no sign was read without the clear text beside it. Recommendation
to the orchestrator: keep "recovery" and add the words "from the note's own clear text".

## 3. Search to disprove (independent, 24 Sept 2026)

| Family | What was searched | Result |
|---|---|---|
| (d) Holding archive catalogue | RAH OAI-PMH GetRecord 14495, `oai_dc` and `marc21` (plain curl, descriptive UA); ListMetadataFormats | Title only: "[Cartas y documentos cruzados entre la Reina Isabel II y Luis González Bravo ... Carta de González Bravo. Nota cifrada del Conde de la Cañada. 18 de noviembre de 1869.]", Archivo de Isabel II, Manuscritos, PD mark. No transcription, no mention of the clear text or of a key. |
| (d) RAH blog/exhibition, other legajo items | Not searched: every HTML path is Anubis-challenged (playbook), and this audit did not open a browser against it | unreachable by policy. The LANE N RAH OAI scout (claim 07:12) is harvesting the collection and may surface sibling items in the same cipher |
| (d)/(b) RAE "Copias de cartas de Isabel II 1869-1871" | archivo.rae.es page, one plain GET | **403**, not retried (second 403 today on that host). Unread. It could hold a copy of the Queen's side of this exchange. That would not change N0. |
| (c)/(g) Historia Contemporánea | Fetched open access from ojs.ehu.eus and full-text grepped: "González Bravo o el final de la era isabelina ... La Nueva Iberia" (doi 10.1387/hc.23683, 2024); "El primer exilio de Isabel II visto desde la prensa vasco-francesa (Pau, sept-nov 1868)" (doi 10.1387/hc.6614, 2012) | Neither mentions Cañada. "cifra" appears only as "se cifraban" (budget) and "clave" only as "palabras clave". hc.6614 ends in Nov 1868, before this note. Their bibliographies cite Burdiel 2010 (biography of Isabel II) and Comellas: see gaps. |
| (g) CrossRef | 7 queries: González Bravo + Isabel II exilio; "Conde de la Cañada" 1869; González Bravo final era isabelina; Isabel II exilio correspondencia González Bravo; Isabel II París exilio restauración 1869 cartas; Isabel II correspondencia exilio carta cifrada | No item on this note. The Cañada hits are the 18th-century 1st Conde (Juan Acedo Rico) and places named Cañada. |
| (g) OpenAlex, Semantic Scholar | one query each | **429 both** (shared-IP daily budget, as all morning). Logged unreachable, not retried. |
| (g) HAL | "González Bravo" AND "Isabel II" | 0 |
| (g) Dialnet | "Conde de la Cañada González Bravo" (buscar/documentos) | 11 theses, none relevant (restoration of buildings etc.) |
| (e) BNE Hemeroteca Digital | one GET on its results page | **403 security challenge**. Stopped, not retried. |
| (e) Internet Archive full text | be-api fts, whole collection: "Conde de la Cañada" "González Bravo" (96); "justísima restauración" (3); "trono de San Fernando" felicitar (390); "nota cifrada" "Conde de la Cañada" (2); "Conde de la Cañada" 1869 Isabel (268); top 10 read each | No hit on the note. "justísima restauración" hits are a Montevideo museum annal (unrelated). The Cañada hits are the 18th-century Conde and 1850s Mallorcan press. The Moreno "Isabel II biografía" (isabeliibiografi0000more) hits only on González Bravo. |
| (e) Google Books | Not this session's (LANE V holds it). Queries posted to ROOM 07:14 UTC. LANE S had already run 3 queries (NOTES.md): no hit | open for LANE V; cannot change N0 |
| (f) Solver repos | fresh shallow clones 24 Sept 2026: dbourdeau/cyphersolver @85a3850, aaymeloglu/unsolved-ciphers @2495c45; grep cañada / conde de la ca.ada / gonz.lez bravo / 9/6958 / 14495 / bibliotecadigital.rah | Aymeloglu: none. Bourdeau: only `docs/search.json`, a note on a different RAH item (lopehurtado) saying bibliotecadigital.rah.es 403s its automation. Not this note. |
| (f) Cipher blogs | sources/cryptiana (solver side, grep) | none (false hits on the country Canada) |
| DECODE | not searched by this session (login lane is LANE N) | gap, cannot change N0 |
| (b) Printed Isabel II exile correspondence / González Bravo | Not read: Burdiel, *Isabel II. Una biografía* (2010); Comellas, *Isabel II* (1999); any edition of the Queen's exile letters | gap. It could only move the class to "N0 and also printed". |
| JSTOR | no rows queued: the class rests on the item itself, and no scholarship result can lower N0 | n/a |

**Second-opinion prompt:** not written. The brief asks for one only at N3 or higher.

## 4. Did we first-decipher?

No. The note was written with its plaintext. What this project did was align cipher to clear and tabulate the key.
Whether anyone has tabulated that key before was not established either way: no such table was found in the
families above.

## 5. Postmortem and corrections

- **Failure:** the note was carried as "open, stage 2 verified unsolved ... a genuine cryptanalysis candidate"
  (NOTES.md 'Verdict'; QUEUE.md row N2 kind "cryptanalysis") for about an hour. Then the first worker with the image
  saw the clear text above every cipher line. Check-solved judged a catalogue title ("Nota cifrada") without the image.
  Lesson: check-solved on an item with public images looks at one page image before it says "unsolved". An
  interlinear or facing clear text makes the target N0 on arrival and a recovery-only job.
- **Grade inconsistency:** R8 grades the reading H ("read from the document's own interlinear plaintext"). Rule 4
  reserves H for a key source and C for known plaintext. R4 called it C, and clair1067's interlinear alignment uses C.
  The interlinear clear text is known plaintext, so the correct grade is **C 665, M 2**. I did not regrade. key.tsv's
  grade column and reading.txt are the solver's generated files, and my brief says do not decode. Suggestion for LANE
  R: change H→C in build_align.py and rerun `decode_key.py --check`. status.json's "H 665" line should follow; the
  orchestrator owns that file.
- **Corrections made:** NOTES.md gets a dated correction under 'Verdict' (not unsolved: plaintext on the leaf; N0) and
  under the R8 grade line. Nothing in the folder used "new", "first", "unpublished" or "never printed" about the
  reading. The one "never printed" in NOTES.md refers to the Google Books key and stays.

## 6. Requests (this audit)

bibliotecadigital.rah.es 3 (OAI: GetRecord oai_dc, ListMetadataFormats, GetRecord marc21). archivo.rae.es 1 (403).
api.crossref.org 7. api.openalex.org 1 (429). api.semanticscholar.org 1 (429). api.archives-ouvertes.fr 1. doi.org 2.
ojs.ehu.eus 4. dialnet.unirioja.es 1. hemerotecadigital.bne.es 1 (403). be-api.us.archive.org 5. github.com 2 shallow
clones. All requests were made one at a time, at least 2 s apart, with the descriptive UA except for the single RAE
GET.

## Google Books queries (LANE V runner), 24 Sept 2026

LANE V worker (Sonnet), running the queries posted by LANE W worker E in ROOM.md 07:15 UTC. This session only ran
the queries and records what came back; it does not decode and does not assign or change a class. The class here is
already N0 (section 1 above: the plaintext is on the item itself), so nothing below can lower it; it is recorded for
completeness per the brief.

**Queries (8, verbatim from ROOM.md):** "nota del Conde de la Cañada"; "Conde de la Cañada" "González Bravo" 1869;
"la justísima restauración" Isabel; "gana por momentos la idea"; "sentada V. M. en el trono de San Fernando"; "me
aventaja en deseos"; "tal y como ha sido recibida" González Bravo; "Conde de la Cañada" carlista OR alfonsino 1869.
Full results: `google-books-2026-09-24.tsv`.

**Hit counts:** 5 of 8 queries returned 0 items (`"Conde de la Cañada" "González Bravo" 1869`; `"la justísima
restauración" Isabel`; `"gana por momentos la idea"`; `"sentada V. M. en el trono de San Fernando"`; `"tal y como ha
sido recibida" González Bravo`). 3 returned hits:

- `"nota del Conde de la Cañada"` -- 1 item (1 after `filter=full`).
- `"me aventaja en deseos"` -- 4 items (2 after `filter=full`).
- `"Conde de la Cañada" carlista OR alfonsino 1869` -- 3 items (0 after `filter=full`).

**Hits whose snippet contains the quoted phrase:**

1. `"nota del Conde de la Cañada"` -- volume `TbUZAAAAMAAJ`, *Catálogo de los manuscritos relativos a los antiguos
   Jesuítas de Chile* (Biblioteca Nacional de Chile, 1891): "Nota del Conde de la Cañada participando queda
   enterado del estado en que se hallan los expedientes pendientes de las Temporalidades de Chile. Madrid, 21 de
   agosto. 1793." -- **a different note, dated Madrid, 21 Aug 1793**, about Jesuit temporalities in Chile, 76 years
   before this letter and a different subject; a coincidental title match on a formulaic catalogue heading ("Nota
   del Conde de la Cañada..."), not the same document.
2. `"me aventaja en deseos"` -- four items, all Spanish parliamentary/literary use of the same stock phrase ("nadie
   me aventaja en deseos de..."), none about this letter: volume `nD3hZbSKPwAC`, *La Campana del terror, ó, Las
   vísperas sicilianas* (Garci-Sánchez del Pinar, 1857); volume `eBoBAVf722MC`, *Diario de las sesiones de Cortes*
   (1889); volume `Yj5IAQAAMAAJ`, *Diario de las sesiones...* (Congreso de los Diputados, 1876); volume
   `KsE3AQAAMAAJ`, *Diario de las Sesiones de Cortes, Congreso de los Diputados* (1844). All four predate or postdate
   1869 and are unrelated speeches/fiction, not the Cañada note.
3. `"Conde de la Cañada" carlista OR alfonsino 1869` -- three items, all about a different, 19th-century Carlist-era
   "Conde de la Cañada" as a political figure, not this letter's content: volume `GeMCAAAAYAAJ`, *Narración militar
   de la guerra carlista de 1869 á 1876* (Spain, Cuerpo de Estado Mayor, 1885), no snippet returned; volume
   `eHI_4wLzQEMC`, *Desamortización eclesiástica en la provincia de Ciudad Real, 1836-1854* (Ángel Ramón del Valle
   Calzado, 1995): "...carlistas, como algunos otros miembros de esa élite como el Conde de la Cañada..."; volume
   `0eNrvqCpvkoC`, *Elecciones y parlamentarios* (González Calleja/Moreno Luzón, 1993): "...conde de la Cañada y
   organizador del partido a escala provincial... 1869, 1871 y septiembre de 1872...".

**Non-decisive, for the record.** None of these seven hits quotes this note's own text (the "sentada... trono de San
Fernando", "gana por momentos la idea de la justísima restauración" or "tal y como ha sido recibida" phrases all
returned 0). The 1793 Cañada catalogue note and the Carlist-era "Conde de la Cañada" are different people/documents
sharing a title; "me aventaja en deseos" is a stock 19th-century Spanish phrase. Nothing here changes section 2's
ruling (N0, plaintext already on the item).

Requests this session: www.googleapis.com 11 (8 base queries + 3 `filter=full` re-runs on the queries with hits),
one at a time, at least 3 s apart, key never printed. No other host.
