# AUDIT -- rah-morillo-1817 item 3 (RAH Madrid, Colección Morillo, Sig. 9/7666, leg. 23, ff.420-420v, record 5186)

Verifier: V9-MOR (LANE V9, session_01R95PtsBBhjZBjAnveu1XyQ), 26 Sept 2026, from 11:26 UTC (clock read). Not the solver
(LANE NX: NX-MOR, NX-MOR2, NX-MOR3, NX-MOR4); does not protect its conclusions. No decoding, alignment or key change
was done. Items 1 and 2 of this folder are not audited here.

**Claim under audit** (LANE NX orchestrator, ROOM.md 10:58): item 3 read at grade H from the leaf's own interlinear
period decipherment under each group; `key_5186.tsv` 17 signs, 0 conflicts over 50 recurring occurrences;
shuffle-consistency 1.000 vs shuffle p95 0.800; `decode_key.py --check` H 91 / U 6 of 97 tokens; re-derivation NX-MOR3
0 differences; es17 judge FAIL (not era-matched); Rodríguez Villa t.4 searched, no hit; Contreras 1988 describes the
item only. "Bolívar, 26=v" is a hypothesis outside the key.

## 1. Extract (template step 1)

| Field | Value (source) |
|---|---|
| Date, place | Guanare, 7 Nov 1820 (clear dateline on f.420r; RAH record title; Contreras 1988 no. 4.529) |
| Sender | "J.n María Herrera" (signature f.420v, as NX-MOR read it). Rodríguez Villa t.4 p.274 names a "teniente coronel don José María Herrera" as Morillo's commissioner to Bolívar at Cúcuta in 1820 -- probably the same man, not established here (grade I) |
| Recipient | "Exmo. S.D. Pablo Morillo" (address, f.420v) |
| Clear text before the cipher | "Guanare y Nov.re 7 de 1820. Mi venerado Gral: en este momento recivo la favorecida de V. de 3 del corriente quedando enterado de su contenido y dandole el debido cumplimiento. Nada ay por aqui de particular, los enemigos de Apure no se mueven." (NX-MOR eye-read) |
| Cipher block | 21 groups, 97 tokens, 6 rows; 14 numerals + "+" + a drawn box resolved, codes 10/22/26/28 unread (`ciphertext_5186.tsv`) |
| Plaintext as read | `reading_5186.txt`: romerito paso el / por barinrtas con so[22]o / tres oficiales dijo benia / de jua[22]ana buscando a bo / li[26]ar sr[10]uro para tru / [28]i[22]o. Gloss as read (`gloss_5186.tsv`): Romerito Paso el por barinituS con solo tres oficiales dijo benia de guayana buscando a bo levar seguro para tru xino (several words tentative) |
| Identifiers | RAH `registro.do?id=5186`, OAI `oai:bibliotecadigital.rah.es:5186`, images 10088713 (f.420r) / 10088714 (f.420v); Contreras, *Catálogo de la Colección Pablo Morillo* (Madrid 1988, Google Books ohJPjaGKOk8C) no. 4.529 (4.530 in V9-MOR's own snippet: the entry number and the physical description share a line in the Google Books OCR, so the number is ambiguous by one); the neighbouring f.419 is the entry before it, "Bolívar para Romerito. Guanare, 6 de noviembre de 1820" |
| What the solver searched | 24 Sept: Rodríguez Villa t.1 and t.3 via IA djvu (`eltenientegener00villgoog`, `...01villgoog`) and the 1920 reprint (`eltenientegenera01/02rodruoft`), grep Romerito/Herrera: 0; IA global "Romerito": noise; Cryptiana, Bourdeau, Aymeloglu (incl. cached DECODE/BNE catalogues): 0; Google Books 3 queries, found Contreras 1988's entry. 26 Sept (NX-MOR2/NX-MOR4): Rodríguez Villa t.4 (v3kzAQAAIAAJ) searched for "Herrera" + "7 de noviembre de 1820" and "Romerito": only a different letter (Herrera from Guanare "de 20 del actual", p.330); Contreras 1988 "carta cifrada" Morillo: this entry only |
| **Found by this audit** | **The plaintext is in print.** Wilfredo Bolívar, Armando González Segovia and Aleyda Anzola, *Portuguesa en Carabobo. Diario llanero de una contienda en armas* (Aythaima Grupo Editor, digital edition, 2021; Depósito Legal PO2021000018, ISBN 978-980-18-2090-1), p.37, with footnote 100 -- Internet Archive `portuguesa-en-carabobo` (uploaded 24 May 2025) |

## 2. Prior print (the decisive result)

*Portuguesa en Carabobo* (2021), p.37 (IA `portuguesa-en-carabobo`, `_djvu.txt` fetched once today, line 2023-2025):

> "De manera simultánea el mismo 7 de noviembre desde Guanare, en respuesta a pliegos de Morillo, basado en deficientes
> informes de inteligencia sobre la movilización del teniente coronel Juan Antonio Romero hacia Barinas, en carta
> cifrada le escribe Herrera: “Nada hay por aquí de particular, los enemigos del Apure no se reciben. Romerito pasó el
> río [Apure] por Caimital con sólo tres oficiales. Dijo venía de Guayana buscando a Bolívar, seguro para Trujillo”."

Footnote 100: "Oficio de José María Herrera a Morillo, fechado en Guanare el 7 de noviembre de 1820 - BDRAHE; Ib.,
Signatura: Sig. 9/7666, leg. 23, f), ff. 420-420v. Se ha corregido la ortografía." The same book reproduces the leaf as a
figure (caption: "Carta cifrada del coronel realista José María Herrera a Miguel de la Torre desde Guanare el 7 de
noviembre de 1820. Una forma secreta de comunicarse -- Cortesía: Biblioteca Digital Real Academia de la Historia de
España"; the caption names La Torre, the footnote and the leaf's address name Morillo).

This is the same letter by date, place, sender, shelfmark and folios, and the quoted text is the clear closing sentence
plus the whole cipher block in modernised spelling. The authors read it from the RAH digital images, so the words under
the cipher were almost certainly taken from the period interlinear gloss; they give no key and do not describe the
cipher. It prints **"Caimital"** where NX-MOR2 read the gloss of r2g2 as "barinituS" and the key gives "barinrtas", and
**"no se reciben"** where NX-MOR read the clear text as "no se mueven" -- two places where the print and our eye-reads
of the same leaf differ, for the solver lane to settle from the image (section 5).

Found by `tools/print_check.py`'s unasked ia-global run on three of the seven phrases ("Romerito paso el", "tres
oficiales dijo venia de", "venia de Guayana buscando a Bolivar"), then confirmed by an identifier-restricted be-api search
("tres oficiales" 1 hit) and by reading the full text.

## 3. Verdict

Token accounting (task 2), measured from `build_key_5186.py` (KEY_WORDS / OTHER_GROUPS) against `gloss_5186.tsv`:
**every one of the 21 groups has a period gloss word written under it; no group is gloss-less**, so no part of the
reading is "filled by our key where the period decipherer left nothing".

| Part | Groups | Tokens | Class | Key | Text in print | Confidence |
|---|---|---|---|---|---|---|
| A. Groups whose gloss is legible and agrees letter for letter with the key (the 14 KEY_WORDS groups, 59 tokens, plus r5g4 "tru", 3 tokens) | 15 | 62 | **N0** | `period` | **yes**, *Portuguesa en Carabobo* (2021) p.37 | high |
| B. The 6 flagged groups (r2g2, r2g4, r4g2, r5g1, r5g2, r6g1): gloss present but read only tentatively. Of their 35 tokens, 24 agree with the gloss as read, **5 disagree** (r2g2 positions 6 and 8, r4g2 position 1 j/g, r5g1 position 2 i/e against "levar", r5g2 position 2 r/e), 6 are unread (22 x3, 10, 26, 28) | 6 | 35 | **N0** | `period` | **yes**, same page: "Caimital", "sólo", "Guayana", "Bolívar", "seguro", "Trujillo" | high on the words (gloss + print); low on our letter-level rendering |

**Whole item: N0, key `period`, `text: known`.** N0 = "plaintext and decipherment of this very item already known",
here twice over: (1) a contemporary hand wrote the plaintext under every cipher group on f.420r; (2) that plaintext has
been in print since 2021, with the shelfmark, in *Portuguesa en Carabobo*. The same shape as clair349-este-guise-1556
(N0, gloss on the leaf and the text in print), not szembek-bk1560 (N0, no print). **Prior plaintext:** yes (2021,
earliest citation found). **Prior decipherment:** yes (the period interlinear one on the leaf; the 2021 authors quote its
result). **Prior mapping of this ciphertext to a key:** none found -- `key_5186.tsv` (17 signs) is a key rebuilt by us from
the period gloss, which gives it the `period` label, not `ours`.

**The 6 U tokens.** Five words need one of them: r2g4 so[22]o, r4g2 jua[22]ana, r5g1 li[26]ar, r5g2 sr[10]uro, r6g1
[28]i[22]o. The print gives the words: "sólo", "Guayana", "Bolívar" (split bo|livar across the line, NX-MOR3's reading
confirmed), "seguro", and "Trujillo" (r5g4 "tru" + r6g1). The print is known plaintext (grade C) for those words, but
the letter each unread code stands for is not settled here: "sólo" wants 22=l and "Guayana" wants 22=y, which a
one-value key cannot give both, and r4g2's first sign already reads j against the print's G. Not resolved by this
verifier (no decoding); section 5.

**Key source:** `period` (rebuilt by us, NX-MOR2, from the leaf's own contemporary interlinear decipherment).

**Revision pointer (rule 10 propagation; GAPS-rah-morillo-1817, 2 Oct 2026, account-4, not the verifier).** The reading was
revised after this audit: the 2021 print's words were folded into `key_5186.tsv` (26 = v, 28 = j, 10 = g at C) with an
`exceptions.tsv` carrying this section's five M positions and the three occurrences of sign 22 (one sign, three print
letters: l / y / ll, M); `decode_key.py --check` now prints **C 90 / M 7 / U 0** of 97 (r5g1 position 1 is C under the
print's "Bolivar"). Class, key source and the safe sentence's substance are unchanged (N0, `period`, text known); the
safe sentence's count reads C 90 / M 7 / U 0 from this date. Details: NOTES.md "GAPS-rah-morillo-1817 (2 Oct 2026)".

### Grade check (rule 4) -- correction

- The reading is graded **H** throughout (`key_5186.tsv`, `reading_5186.txt`, `decode.json`, NOTES.md NX-MOR2, STATUS.md,
  ROOM 10:58). Rule 4's H is "read from a key source"; no key sheet or cipher book exists for item 3, only a
  decipherment, which is known plaintext for the tokens it sits over: **C**, as V8-SZEM ruled for the same shape
  (szembek-bk1560/AUDIT.md section 2). The reading's substance does not change; the label does. The 5 part-B tokens where
  the key's letter contradicts the gloss as read (and, at r2g2, the print) are **M**. Corrected counts, for the next edit
  of the key/decode files (outside this verifier's brief, which forbids touching them): **C 86, M 5, U 6** of 97.
- Count slips in NOTES.md NX-MOR2 (not over-claims): the key is built from **14** clean words and **59** letter-token
  pairs (sum of `key_5186.tsv`'s count column; `build_key_5186.py` KEY_WORDS has 14 entries), not "13 ... 89"; recurring
  codes carry 55 of the 59. `shuffle_control_5186.py` re-run today: real 1.000, shuffle mean 0.621, p95 0.800 (it
  scores 13 groups). The control result stands.

## 4. Search log (task 3), 26 Sept 2026

| Family | Searched / unreachable | What | Result |
|---|---|---|---|
| (a) Rodríguez Villa, all four volumes | searched | Google Books search-inside (books.google.com `?id=VOL&q=`, parsed from the page's own `search_results` block), a live control term per volume: **t.4** `v3kzAQAAIAAJ` (documents 1819-1837; control "Morillo" 14): "Romerito" 1 (p.330), "Guanare" 6, "Herrera" 6, "7 de Noviembre de 1820" 3, "enemigos de Apure" 10, "tres oficiales" 10, "buscando a Bolívar" 3, "de particular" 10; **t.3** `TyvVAAAAMAAJ` (1816-1818; control 11): "Romerito" 0, "Guanare" 2; **t.2** `pirVAAAAMAAJ` (documents to 1815; control 11): "Romerito" 0, "Guanare" 1; **t.1** (biography) IA `eltenientegener00villgoog` be-api: control "Morillo" 1, "Romerito" 0. `E6_8X3ErA4MC` (no-view copy): no results even for the control, unsearchable | Every hit read from its snippet is another document. The one Romerito hit (t.4 p.330) is Morillo quoting a *later* Herrera letter from Guanare "de 20 del actual" (Romerito "no esperó á Ferrus, sino que se retiró á Pedraza"). The 7 Nov letter is not in the edition. Page text (`output=text`) 403 x3 and the PDF 429 x1, not retried |
| (a') Stoan, *Pablo Morillo and Venezuela, 1815-1820* (1974) | searched | IA `pablomorillovene0000stoa` be-api: control "Morillo" 1, "Romerito" 0, "Herrera" 0; `pablomorilloand00stoagoog` "Romerito" 0 | not discussed |
| (b) Venezuelan documentary editions | partly | Blanco y Azpurúa, *Documentos para la historia de la vida pública del Libertador* (IA `documentosparal00bolgoog`, 1875, one volume; control "Morillo" 1, "Romerito" 0); *Colección de documentos relativos a la vida pública del Libertador* (`colecciondedocu00bolgoog` control 1 / Romerito 0; `colecciondedocum10cara` control 0, so no test); O'Leary, *Memorias* (`bub_gb_8XEqAAAAYAAJ`) "Romerito" 0; Lecuna, *Cartas del Libertador* t.VII, t.VIII "Romerito" 0 (sweep subagent, no control logged). **Not searched:** the other Blanco y Azpurúa volumes (vol. 7, 1819-1821, not located on IA), O'Leary's *Documentos* volumes (the 2021 book cites "O'Leary, XVII" nearby), the Boletín de la Academia Nacional de la Historia (IA volumes located, not searched) | no print of the letter found in these; the family is incomplete, which no longer matters for the class (section 2 already puts the text in print) |
| (c) holding archive | searched | RAH OAI-PMH `GetRecord` oai_dc for 5186, with **record 1306 as a positive control**: 1306's record carries "El documento, cifrado en su mayor parte, aparece publicado por Rodríguez Villa, en el tomo III, con el n.° 754, y en las pp. 693-694"; 5186's carries no publication note. Contreras 1988 (the RAH's printed catalogue, Google Books snippet, sweep subagent and NX-MOR2/4): describes the item only | the archive records no edition; it does not know of the 2021 book |
| (d) phrase search | searched | `tools/print_check.py` with `phrases.txt` (7 phrases: 2 from the clear opening, 5 from the gloss/decode), 6 listed IA items + ia-global + Google Books + OpenAlex + CrossRef + Semantic Scholar (`print-check.tsv`) | **3 phrases hit `portuguesa-en-carabobo` on ia-global -- the decisive find (section 2).** Google Books: 0 for every decoded phrase ("buscando a Bolivar" 300, generic); "nada hay por aqui de particular" 1 unrelated (Río de la Plata history, 1878). Semantic Scholar 429 on the last call, not retried |
| (e) solver repos, Cryptiana | searched | fresh shallow clones of dbourdeau/cyphersolver and aaymeloglu/unsolved-ciphers grepped for morillo/guanare/romerito/9-7666; `sources/cryptiana/` grep; cryptiana.web.fc2.com index (2 requests) | 3 cyphersolver hits, all word-list/corpus substrings (a Quijote text, "montmorillon"); 0 elsewhere |
| (f) scholarship | searched | OpenAlex (Bearer key), Semantic Scholar (key), CrossRef: "Morillo cifra", "Morillo correspondencia cifrada", "Romerito Bolívar", "criptografía guerra independencia Venezuela", "royalist cipher Morillo"; CORE: CORE_API_KEY unset, not run | nothing on this letter; one title-only lead, *El gobierno del general Pablo Morillo (1815-1820)*, not opened |
| (g) JSTOR | done 26 Sept 2026 | 4 rows in `JSTOR-QUEUE.tsv`: family (i) "Morillo" AND "Herrera" AND 1820 AND cifra/cifrada/cipher; "Romerito" AND Bolívar AND (Guanare OR Barinas) AND 1820; family (ii), exact phrases, no cipher keyword: "enemigos de Apure no se mueven"; "Romerito" AND "tres oficiales" | context-only hits on the first two (none about this letter), a blocked book chapter (Spillemaeker 2026, no online viewer) on the second, no relevant hit on the two exact-phrase rows; already N0 from section 2, so no class change |

Requests by host (this session, verifier + subagent): books.google.com 19 (search-inside 15 at 200, page text 3 at 403, PDF 1 at 429);
www.googleapis.com 16 (1 volume listing, print_check 7, subagent 8); be-api.us.archive.org
~40; archive.org ~20; bibliotecadigital.rah.es 2 (OAI only, no images); api.openalex.org 12; api.crossref.org 10;
api.semanticscholar.org 10 (one 429); cryptiana.web.fc2.com 2; github.com 2 clones. No key or credential printed.

## 5. Postmortem and corrections

**Failure:** the item was carried from "open" (24 Sept) to a reading-ready "partial" with the audit question framed as
"is it in Rodríguez Villa or Contreras?" -- the two print sources the lane already knew. Nobody ran a phrase search on
the decoded words before the hand-over; `print_check.py`'s global Internet Archive pass found the 2021 book on its first
run. The lesson is the one rule 10 already states ("a phrase search on the decoded text"), and the precise gap is that
the solver's search log (NX-MOR2 "Intake") checked named editions only; a solver-side `print_check.py` run on two or three
decoded phrases would have cost a few cents and would have told the lane that the text was known before NX-MOR3 and
NX-MOR4 ran.

**Over-claims found:** none in wording -- no file calls the reading new, first or unread. Corrected here and by a
pointer in NOTES.md: (1) grade H should be C (86) / M (5) / U (6), section 3; (2) the key's word and token counts;
(3) NOTES.md's 24 Sept "Verdict" line "open for item 3" and its "t.4 ... not located" are stale (t.4 is on Google Books
and was searched; the text is in print elsewhere).

**For the solver lane (not done here, no decoding):** the 2021 print is known plaintext (grade C) for the five words
that carry unread signs and for r2g2, and it disagrees with our gloss read at r2g2 ("Caimital" vs "barinituS") and with
the clear-text read "no se mueven" ("no se reciben"). Whether those are the 2021 authors' modernisation or our misreading
is an image question. It is also the only test the Bolívar 26=v hypothesis can get from this leaf; it does not make the
result new.

**Safe sentence:** "Item 3 (Herrera to Morillo, Guanare, 7 Nov 1820, RAH 9/7666 ff.420-420v) carries its own period
interlinear decipherment, and its plaintext was printed in 2021 (Bolívar, González Segovia and Anzola, *Portuguesa en
Carabobo*, p.37, n.100); we rebuilt the 17-sign letter key from that period decipherment and regenerate the reading
mechanically (C 86 / M 5 / U 6 of 97 tokens). N0, key period, text known."

**Unsafe sentence:** "We deciphered a previously unread royalist cipher letter about Romerito's search for Bolívar" --
the letter was deciphered on the leaf in 1820 and its text has been in print since 2021.

**Status recommendation for the parent:** item 3 is N0 with `text: known`; per the folder's per-item line it can read
`found-solved` for item 3 (as item 1 does), with key `period`. The folder's first-line status is the lane's to set (this
verifier does not touch status.json).

Pointer (3 Oct 2026, GAPS2-rah-morillo-1817, NOTES.md section of that name): the two print-vs-eye disagreements handed to the solver lane above were image-checked on native crops with a fresh blind read: the leaf reads "no se mueben" (not "reciben"), and the r2g2 gloss reads bari-nit-?-s, with no "Caimital". No reading token changed (C 90 / M 7 / U 0); class N0 and key `period` unchanged.

---

# AUDIT 2 (A3V-VN0, 4 Oct 2026): item 3 (RAH 9/7666 leg. 23 ff.420-420v, record 5186), second audit of the N0 class

Verifier A3V-VN0, account 3, for LANE-A3V, 4 Oct 2026 (clock read 03:13 UTC start, `date -u`). Brief
`.claude/briefs/runs/2026-10-04-acct3-a3v-wave2.md` section A3V-VN0. A session separate from the solvers (LANE NX
NX-MOR..NX-MOR4; GAPS, GAPS2, GAPS203, account 4) and from audit 1 (V9-MOR); it does not protect either. No decoding, no
key, ciphertext or reading change. Touches only this file and PROGRESS.tsv (GAPS209 ran 02:05-02:13 today, done).

**Claim under audit:** audit 1 (V9-MOR) plus its revision pointer: N0, key `period`, text known (*Portuguesa en Carabobo*,
2021, p.37 n.100); `key_5186.tsv` C 90 / M 7 / U 0 of 97 after the 2021 print fold-in.

## 1. The cited print, opened

archive.org `portuguesa-en-carabobo` -- the djvu file is `Portuguesa en Carabobo_djvu.txt` (the identifier-named
`portuguesa-en-carabobo_djvu.txt` answers 404; found via the item's file list), 1 request, scratchpad, not committed. IA
metadata: Wilfredo Bolívar, Armando González Segovia, Aleyda Anzola, date 2021, uploaded 24 May 2025. Lines 2021-2025 and
footnote 100 (lines 2036-2037), quoted as served:

> "... en carta cifrada le escribe Herrera: "Nada hay por aquí de particular, los enemigos del Apure no se reciben.
> Romerito pasó el río [Apure] por Caimital con sólo tres oficiales. Dijo venía de Guayana buscando a Bolívar, seguro para
> Trujillo"." -- n.100: "Oficio de José María Herrera a Morillo, fechado en Guanare el 7 de noviembre de 1820 - BDRAHE;
> Ib., Signatura: Sig. 9/7666, leg. 23, f), ff. 420-420v. Se ha corregido la ortografía."

Same letter by date, place, sender, shelfmark and folios: **audit 1's N0 basis is real.** Positions compared by this
verifier, group by group, `reading_5186.txt` against the print (orthography modernised by the print, as its note says):

| # | group | ours | print | agree |
|---|---|---|---|---|
| 1 | r1g1 | romerito | Romerito | yes |
| 2 | r1g2-g3 | paso el | pasó el [río Apure] | yes; the print adds "río" without brackets -- no cipher group carries it |
| 3 | r2g2 | barinrtas (M x2) | Caimital | **no** (GAPS2's blind gloss read bari-nit-?-s; no C/m/l under the group) |
| 4 | r2g4 | solo | sólo | yes |
| 5 | r3g1-g2 | tres oficiales | tres oficiales | yes |
| 6 | r3g3-g4 | dijo benia | Dijo venía | yes (b/v spelling) |
| 7 | r4g2 | guayana | Guayana | yes (r4g2 pos 0 and 3 are M; the print is their only C source) |
| 8 | r4g3-g5, r5g1 | buscando a bo livar | buscando a Bolívar | yes |
| 9 | r5g2 | srguro (M at pos 1) | seguro | yes on the word; the sign says r |
| 10 | r5g3-r6g1 | para tru jillo | para Trujillo | yes |

9 of 10 agree on the word; 1 (r2g2) disagrees, already M and image-checked by GAPS2. The print is not independent of the
leaf for the 7 positions where `key_5186.tsv` takes its value from it (signs 10, 26, 28 and the three readings of 22):
those agree with the print by construction, which is what grade C from known plaintext means, not a confirmation.

## 2. Earliest print (credit)

be-api fts, global: `"buscando a Bolívar, seguro para Trujillo"` 1 item, `"Romerito pasó el río"` 1 item -- both
`portuguesa-en-carabobo`; `"con sólo tres oficiales"` 10 items, the other nine unrelated (1824 newspapers, Gómez de
Arteche, a Guatemalan gazette, etc.). Google Books (key, `country=US`): `"seguro para Trujillo" Romerito` returned 1 total
with unrelated loose items (first call 503 "service temporarily unavailable", one retry after a pause). OpenAlex
`search=Portuguesa en Carabobo`: 616 loose hits, none this book in the top 5. Audit 1's Rodríguez Villa (4 vols), Stoan,
Blanco y Azpurúa, O'Leary, Lecuna, RAH OAI record (no publication note, with record 1306 as positive control) and Contreras
1988 searches are accepted, not repeated. **Earliest print located: 2021**, as audit 1 says. No earlier article by the same
authors carrying the passage was found (searched: the three phrases above; not searched: Venezuelan regional journals off
the open indexes).

## 3. Rule 7 spot check

`python3 tools/decode_key.py ciphers/rah-morillo-1817 --check`: "ciphertext_5186.tsv: tokens 97: C 90, M 7 /
ciphertext_2242.tsv: tokens 240: C 237, M 3 / reading up to date", exit 0. Matches the committed counts.

## 4. Key-source field

Audit 1 labels the key `period`. Checked against `key_5186.tsv`'s `source` column: 17 of 21 key rows rest on the leaf's
interlinear gloss (`gloss` or `gloss+print`); **4 rows are `print` only** -- 26=v, 10=g, 28=j (C) and 22=l|y|ll (M) --
aligned by us (GAPS, 2 Oct) to the 2021 print's plaintext. Those four are a plain-copy alignment, i.e. `ours` by CLAUDE.md
rule 10's definition, on a published plaintext with no published key. **Found, not applied (status.json is the parent's):**
key = `period` (17 signs from the leaf's own decipherment) with 4 signs `ours` aligned to the 2021 print; the whole-item
label stays `period`, since every group carries the period gloss and the print only supplies letters the gloss renders
illegibly. `text: known`.

## 5. Verdict

**Item 3: N0 confirmed.** Prior plaintext: yes, 2021 (*Portuguesa en Carabobo*, p.37 n.100; earliest located). Prior
decipherment: yes, the period interlinear one on f.420r. Evidence quality: high (print opened, 10 positions compared, 9
agree). Confidence: high. Key source: `period`, with 4 print-aligned signs `ours` (section 4).

Safe sentence (audit 1's, count updated as its pointer already says): "Item 3 (Herrera to Morillo, Guanare, 7 Nov 1820,
RAH 9/7666 ff.420-420v) carries its own period interlinear decipherment, and its plaintext was printed in 2021 (Bolívar,
González Segovia and Anzola, *Portuguesa en Carabobo*, p.37, n.100); we rebuilt the letter key from that period
decipherment, with four signs aligned to the 2021 print, and regenerate the reading mechanically (C 90 / M 7 / U 0 of 97
tokens). N0, key period, text known."

Unsafe sentence: "The 2021 print gives Herrera's letter exactly as written" -- it modernises spelling, adds "río", and
gives "Caimital" and "no se reciben" where the leaf reads otherwise (GAPS2, 3 Oct).

Postmortem: no over-claim found in the folder's files, NEAR.md (no row) or PROGRESS.tsv; the only slip is that audit 1's
revision pointer left the key-source field undifferentiated after the print fold-in (section 4). JSTOR: audit 1 queued 4
rows in both families; none added. N0 queues no SECOND-OPINIONS row. PROGRESS.tsv audit-2 column set to x from this verdict.
