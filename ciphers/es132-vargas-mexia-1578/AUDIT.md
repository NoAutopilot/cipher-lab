# AUDIT 1 (A3V2-ES132A1, 4 Oct 2026): novelty class and reading depth of the f.89 and f.119 letters' readings

Verifier: worker A3V2-ES132A1 (account 3, for LANE-A3V2), brief `.claude/briefs/runs/2026-10-04-acct3-a3v2-wave2.md`
section A3V2-ES132A1 (cap as amended 05:3x UTC). A session separate from every solver of this target (CS-1, FT-B test 0,
RUN1-ES132 test 1, RUN2-ES132 / N4-ES132 / N4-ES132B test 2, A3V2-ES132C4) and from the rule-7 re-derivation session
(A3V2-ES7, `RD7-2026-10-04.md`). Clock by `date -u`: 05:38 UTC at claim, searches 05:41-05:50 UTC. No decoding here;
`key.tsv`, every `ciphertext_*.tsv`, every `reading_*.txt` and the three `test*_result.json` are unchanged by this audit.

**Claim under audit** (brief wording): the `test0.py`/`test1.py`/`test2.py` readings of the f.89 letter (f.89r-f.91r) and the
f.119 letter (f.119r-f.120r), rule-7 SAME 2842/2842 (A3V2-ES7, 4 Oct 2026), with the Teulet-printed paragraphs graded C
and the unprinted paragraphs graded M only, each page through the pre-registered gate (a) (known-answer alignment) or (b)
(es16 4-gram statistic against token-order and key shuffles).

## 1. The items, as the repository states them

| field | f.89 letter | f.119 letter | source |
|---|---|---|---|
| shelfmark | BnF Espagnol 132 f.89r-f.91r, Gallica ark:/12148/btv1b10032556x canvases 86-88 | BnF Espagnol 132 f.119r-f.120r, canvases 116-117 | NOTES.md tests 1-2 |
| holding record | archivesetmanuscrits.bnf.fr/ark:/12148/cc34747q: f.89 and 93 "En chiffre"; digitised (Gallica ark quoted in the record), microfilm MF 8506 | same record: f.119 "En chiffre" | A3V2-ES132C4 (b) |
| sender / recipient / date | Philip II to Juan de Vargas Mexia (ambassador in Paris), Madrid, 19 Sept 1578 (clear dating line f.91r) | Philip II to Vargas Mexia, Madrid, 15 Oct 1578 (clear dating line f.120r) | NOTES.md; Tomokiyo TOC nos.42-43 and 55 |
| duplicate on the volume | **f.93-96 is a second copy of the same letter** (Tomokiyo TOC: "no.42-43 (no.42 is a duplicate of no.43) (f.89, 93)"; BnF record: f.89 and 93 "En chiffre"; DECODE record 1980 "f.89-92, f.93-96") -- untranscribed | none listed | sources/cryptiana/web/spanish3D.htm; DECODE 1980 |
| cipher | Cp.30 = "Vargas Mexia's Cipher 3": syllabic table (base + vowel indicator + consonant mark above) plus a nomenclature of cursive words and numbers >= 38 | same | key.tsv header |
| key source | **published**: Tomokiyo's cp30.png (after Devos 1950 Cp.30 and Alcocer 1921 pp.628-640), one correction 35 = pr from el-descifrador/cabinet-noir `cle/cp30_complements.tsv` (CC BY 4.0). The nomenclature is not on disk | same | key.tsv |
| transcription | 2 blind Sonnet passes per page on line crops, reconciled; err_2reader 9.8-19.8% per page; '?' tokens 44/36/31/2 on f.89r/f.89v/f.90r/f.91r | err_2reader 10.3-22.4%; 12 '?' on f.119v upper | NOTES.md tests 1-2 |
| reading, grades (rule 4, result JSONs) | 1,940 tokens = H 0 / C 217 / S 0 / M 1,526 / I 0 / U 197 (f.89r 445, f.89v 428, f.90r 494, f.90v 453, f.91r 120) | 902 tokens = H 0 / C 146 / S 0 / M 660 / I 0 / U 96 (f.119r 363, f.119v upper 212, f.119v lower 184, f.120r 143) | test1/test2 `grades_reconciled` |
| where the C comes from | f.90v L10-L26 = Teulet's printed "Déchiffr. officiel" paragraph (Scotland, Guaras, Mendoza); gate (a) S_a 0.918-0.925 vs key-shuffle p99 0.395 and wrong-window p99 0.352 | f.119v L07-L13 + f.120r L01-L04 = Teulet's printed paragraph (Scottish ambassador, 4,000 men); S_a 0.917-0.941 vs p99 0.48-0.65 | tests 0-2 |
| rule 7 | SAME 445+428+494+453+120 of the same, fresh session | SAME 363+212+184+143 | RD7-2026-10-04.md |
| judge | `tools/judge_plaintext.py` with es16/es17 FAILs every decode and the printed Teulet text alike (es16 held-out false negative 60.7-70.3%, one volume): "judge cannot decide" | same | NOTES.md tests 0-1 |

Distinctive text available for a phrase search: the printed paragraphs (Teulet's own wording, a positive control) and,
from the M-graded paragraphs, the clauses the solvers read by eye: f.89r "arçobispo de Nazaret", "prohibir de veras y
castigar con rigor", "tan injusta y de tan mal nombre"; f.89v "con las palabras que me parescio convenir", "todo lo que ha
hecho el de Alanzon"; f.90r "el de Alanzon y el de Bearne", "andamientos y pretension de ... Bearne" (f.91r); f.90v "Diego
Luis ... naos de Indias", "lo que toca a la navegacion de las Indias", "lo del trigo"; f.119r "se ha dado en esa villa a las
predicas", "se han atrevido a introduzir"; f.120r "sobre lo de las piraterias".

What the solvers searched before this audit: CS-1 (3 Oct 2026: 9 web queries, Gachard 1875 vol.1-2, Teulet vol.5, Mignet
1846 whole-volume greps, cabinet-noir clone, DECODE records 1960/1979/2025 opened), A3V2-ES7 print check (4 Oct: 12
phrases through `tools/print_check.py` -- IA global, Google Books, OpenAlex, CrossRef, Semantic Scholar, the three listed
djvu texts), A3V2-ES132C4 (4 Oct: holding record, Cryptiana/Cipherbrain/Cipher Mysteries comment threads).

## 2. Independent search (this session, 4 Oct 2026, 05:41-05:50 UTC)

Full texts fetched once from archive.org (`_djvu.txt`, descriptive UA, >= 1.6 s apart) into the scratchpad and grepped
for the names and phrases above; every hit on a generic phrase was read in context.

| family | source | searched by | result |
|---|---|---|---|
| (a) canonical series | Teulet, *Papiers d'état ... relatifs à l'histoire de l'Écosse au XVIe siècle*, t. III (Bannatyne Club, Paris 1860; IA papiersdetatpiec03teuluoft, 3.08 MB) | grep "passastes", "Setiembre 1578", "Octubre 1578", all phrases | **prints the same two paragraphs** as Relations politiques: pp.196-197 (19 Sept 1578, "Liasse B. 47, n° 8. Déchiffrement officiel", 15 lines from "De consideracion es lo que passastes" to "al recaudo que soleis", dated "De Madrid, à xix de Setiembre 1578") and pp.202-203 (15 Oct 1578, "n° 6", "A lo que passastes ... lo que convenga"), each with a French analysis. **Earliest print of the printed paragraphs is therefore 1860, not 1862.** Nothing else of either letter: 0 hits for navegacion de las Indias, piraterias, Diego Luis, monesterio, Alanzon+Bearne, tan injusta; the "predicas" (1, England 1586), "trigo" (3, English provinces), "Bearne" (5, 1580s) hits are other documents |
| (a) | Teulet, *Relations politiques de la France et de l'Espagne avec l'Écosse*, t. V (1862; IA relationspolitiq05teul_0, second copy) | grep | the same two extracts (lines 8169 ff., 8452 ff.); the solvers' `teulet_19sep1578.txt` / `teulet_15oct1578.txt` match them |
| (a) | Kervyn de Lettenhove, *Relations politiques des Pays-Bas et de l'Angleterre*, t. X (IA relationspolitiq10nethuoft, 1577-78, 2.63 MB) and t. XI (relationspolitiq11nethuoft, 1578-79) | grep Vargas, Nazaret, Diego Luis, Guaras, embaxador de Escocia, piraterias, predicas, Alanzon, Alençon+Bearn | **no letter of Philip II to Vargas**; "Vargas" 1 hit (t. X: "el pliego de Joan de Vargas" in a Spanish dispatch), Guaras 24/6 hits (his London arrest, other correspondents), Alanzon 7/6 (English and Spanish dispatches), predicas 1 (unrelated). Control: both volumes print hundreds of 1578 Spanish dispatches, so the OCR reads Spanish |
| (b) sender-side editions | Gachard, *Correspondance de Philippe II sur les affaires des Pays-Bas* (IA correspondancede01-05phil) ends 1577; Lefèvre's *deuxième partie* t. I (1577-1580, Brussels 1940) is the volume that could carry an analysis of these weeks | IA advancedsearch (7 Gachard volumes, none past 1577); Google Books API (Lefèvre t. III 1956 and t. IV 1960 indexed, t. I not full view) | **Lefèvre t. I not reachable from the cloud** (no IA copy; HathiTrust page text cloud-blocked): logged unreachable, not a negative |
| (b) recipient side | Vargas Mexia's own despatches: Teulet (Vargas to Philip II, 19 Sept 1578 "De Paris" and 27 Oct 1578, Papiers d'état t. III lines 9599, 9832); *Les Sources inédites de l'histoire du Maroc*, 1re série, Espagne t. I (IA pt02lessourcesindi01castuoft: Vargas to Philip II, 10 Oct and 6 Dec 1578, "Descifrada"); Navarrete, *Biblioteca marítima española* (Google Books: Vargas letters of 25 March, 7 Oct, 8 Dec 1578 "sobre los corsarios") | grep / API | these are Vargas's letters *to* the king, not the king's to him; none quotes the 19 Sept or 15 Oct letter. They do fix the context the M-graded paragraphs read (corsairs and the Indies navigation, Oct 1578; the archbishop of Nazareth, Frangipani, in Paris: Tomokiyo TOC no.44 = f.97, his letter to Philip II of 25 Sept 1578; "Le salut par les armes" 2011 via Google Books: Nazareth at the Mons talks July-Aug 1578, AGS K 1546) |
| (c) documentary editions | CODOIN and *Nueva colección de documentos inéditos*: IA global full-text "Vargas Mexia" 1578 (572 items, top 50 identifiers listed) and "Juan de Vargas Mexia" (269) | be-api fts | no CODOIN / Nueva colección volume among the top 50; the hits are Teulet's two editions, the Maroc *Sources inédites*, Mignet/Perez literature, Parker, Hume, catalogues. Cabrera de Córdoba 1625 (A3V2-ES7's hit for "el de Alanzon y el de Bearne") is narrative prose, not the letter. Mignet 1846: 0 hits on any phrase (A3V2-ES7, confirmed) |
| (d) holding archive | BnF finding aid cc34747q (quoted in NOTES.md A3V2-ES132C4: f.89, 93, 119 "En chiffre", no decipherment noted for them; f.169 and f.177 are the only "Déchiffrement" items); Gallica SRU `gallica all "Vargas Mexia"` (290 records; top 10 titles read: the Espagnol 132 record itself, *Nouvelles archives des missions*, Laforge, Gazette, Figaro ...) ; Gachard 1875 p.416 "à toutes celles qui sont chiffrées (sauf une seule) le déchiffrement manque" (CS-1) | SRU, record read | no decipherment of f.89 or f.119 catalogued or digitised beside the leaves |
| (e) full text | be-api fts global, 11 queries: positive control "passastes con el embaxador de Escocia" -> 6 items, all Teulet editions (method works); "arcobispo/arçobispo de Nazaret" -> Teulet 1586 (Mendoza), Council of Trent, Cyprus histories, none 1578 Vargas; "arzobispo de Nazaret" 78 (Rome 1580s, crusades); "Diego Luis" naos 1578 -> Indies catalogues, unrelated; "Vargas Mexia" cifra 226 -> Teulet, *Revista de archivos* 1877 (Osorio letters *to* Vargas), Maroc; "embaxador de Escocia" Vargas 12 -> Teulet only; "hiziese rostro" 6 (chronicles); "monesterio de San Lorenzo" Vargas 57 (Escorial literature) | be-api | **no print of any unprinted paragraph's wording** |
| (e) | Google Books API (`country=US`, key), 14 queries: `"Vargas Mexia" "19 de septiembre de 1578"` (19, catalogues), `"15 de octubre de 1578"` (12: Teulet 1862 x6 -- the 27 Oct Vargas letter mentions the king's 15 Oct), `cifra descifrada 1578` (0), `"Espagnol 132" Vargas` (4: Morel-Fatio, *Études sur l'Espagne* 1925 and *Annales* 1906 quote **f.14**, Philip II to Vargas 31 Jan 1578 -- a clear letter, not these), `"Espagnol 132" fol. 89/119/90` (348, none this volume's leaves), `"navegacion de las Indias" "Vargas Mexia"` (38: Navarrete), `"sobre lo de las piraterias"` (2: 1568-71 Germany), `"arcobispo de Nazaret" 1578 Vargas` (1: Vázquez de Prada, *Felipe II y Francia* 2004, snippet only), `"tornareis a hazer"` (4: Documenta polonica, chancery formula), Lefèvre (166) | API | nothing prints or deciphers the unprinted text; one scholarly monograph (Vázquez de Prada 2004) works the AGS K Vargas correspondence and may summarise these weeks: **not opened** (snippet only), logged |
| (e) | HathiTrust full text / page images | - | cloud-blocked (CLAUDE.md host table); not searched |
| (f) solver repositories | fresh shallow clones 4 Oct 2026 05:4x UTC: el-descifrador/cabinet-noir HEAD 47b6db9 (2 Oct 2026 14:15 UTC, unchanged), dbourdeau/cyphersolver HEAD a439937 (3 Oct), aaymeloglu/unsolved-ciphers HEAD d2800bb (27 Sept) | folder list; grep -il vargas / "espagnol 132" / btv1b10032556x | cabinet-noir es132-vargas-mexia/ still the same 30 letter folders, **no f089/f093/f119/f120**; cyphersolver hits are its Gallica sweep listing ("Espagnol 132 \| 24 items"), its DECODE harvest JSON and the unrelated vargas1552 target; unsolved-ciphers 0 |
| (f) DECODE | records 1980 ("Espagnol 132, f.89-92, f.93-96", Status Decrypted) and 1983 ("f.115-116", key name BnF_es132_f119 -- a mislabel: f.115 is the 14 Oct letter, TOC no.53) read **without login** (RecordsView answers plain curl, HTTP 200) | 2 requests | both carry only the two key documents ("Cp30 [key]", "Vargas Mexia's Cipher 3 [key]"), "Inline Plaintext: No": "Decrypted" is key-attached status, as CS-1 found for 1960/1979/2025; no plaintext |
| (f) cipher blogs | Cryptiana snapshot `sources/cryptiana/web/spanish3D.htm` (TOC nos.41-56 read; Tomokiyo's 23 June 2024 note that the es.132 letters are "not printed in Teulet" holds for every paragraph but the two Scotland extracts); Cipherbrain, Cipher Mysteries, Cryptiana comment threads: A3V2-ES132C4's read of 4 Oct stands (no reading claim) | local grep | nothing |
| (g) scholarship | OpenAlex (key, 4 queries): `"Vargas Mexia"` 43 works (the Gallica record "Espagnol 132" itself, his testament clauses, Rubino 2012 *The Secrets of Antonio Pérez Decoded*, Zúñiga/Rome, Guise 2025, Milan policing -- none a decipherment); `"Espagnol 132" Bibliothèque nationale` 2 (Rubino; an unrelated 2026 literary article); `embajador cifra` 0; `Philip II Vargas Mexia cipher letters Paris 1578` 1 (Rubino). CrossRef 1 query (noise). Semantic Scholar (key): 1 query answered (noise), second 429 -- its 1 request/s pool, not retried. Web: 3 WebSearch queries (BL Add MS 28421 catalogue, BYU De Vargas collection, Francisco de Vargas biographies; no page on these letters). JSTOR: 4 rows appended to `JSTOR-QUEUE.tsv`, families (i) and (ii) | APIs | nothing located; Rubino 2012 (not opened, cited by Tomokiyo for f.198) concerns the Perez Cipher 4 letters, not Cp.30 |

Requests by host this session: archive.org 8 (3 advancedsearch, 5 djvu downloads), be-api.us.archive.org 12,
www.googleapis.com 14 (one HTTP 503, retried once), api.openalex.org 4, api.crossref.org 1, api.semanticscholar.org 2
(second 429, stopped), gallica.bnf.fr 1 (SRU), de-crypt.org 2 (no login), github.com 3 shallow clones, WebSearch 3.
No credentials printed; the DECODE login was not spent.

## 3. Classification (rule 10) and depth (rule 4a)

The item is the letter; each letter splits into text that is in print and text that is not, and the two parts earn
different classes and different depths. They are reported side by side, not blended.

| item | part | prior plaintext | prior decipherment | class | key | text | our grade |
|---|---|---|---|---|---|---|---|
| f.89 letter (19 Sept 1578) | printed paragraph, f.90v L10-L26 (217 C tokens) | yes: Teulet, *Papiers d'état* t. III (1860) pp.196-197 = *Relations politiques* t. V (1862) pp.161-162, from the period "Déchiffrement officiel" (AN Simancas fonds B.47 n° 8) | yes, period (the embassy's own) | **N0** | published | known | C |
| f.89 letter | unprinted paragraphs, f.89r, f.89v, f.90r, f.90v L01-L09 + L27, f.91r (1,526 M + 197 U tokens) | **none located** in print after the search above | a period decipherment of the whole letter is attested (Teulet's source) but **not located in print**; its archive copy (AN Simancas fonds, returned to AGS Estado K in 1941) is not online | **N3** | published | not located | M only (no S) |
| f.119 letter (15 Oct 1578) | printed paragraph, f.119v L07-L13 + f.120r L01-L04 (146 C tokens) | yes: *Papiers d'état* t. III pp.202-203 = *Relations politiques* t. V pp.167-168 (B.47 n° 6) | yes, period | **N0** | published | known | C |
| f.119 letter | unprinted paragraphs, f.119r, f.119v upper, f.119v L02-L06, f.120r L05-L08 (660 M + 96 U) | none located | as above | **N3** | published | not located | M only |

Not N4 for the unprinted parts: Lefèvre t. I (1577-1580), Vázquez de Prada 2004, the BL Add MS 28421 Vargas papers
(1579-1614 per the BL catalogue, so probably later) and the AGS Estado K minutes were not read; HathiTrust and JSTOR were
unreachable from this session (JSTOR rows queued). Not N2: no printed plaintext of those paragraphs exists to map to.
Not N0/N1 for them: Teulet printed only the Scotland paragraph of each letter, as Tomokiyo's 2024 note already implies.

**Depth.**
- Both letters carry one C-graded stretch far above the authentication distance (217 and 146 tokens agreeing with a
  period decipherment at S_a 0.92 against shuffle nulls of 0.35-0.65). By the rule-4a scale that is **D2** for each
  letter, with `depth_pct` = the C share: **f.89 letter about 11% (217/1,940; 12% of the 1,743 cipher-letter tokens)**,
  **f.119 letter about 16% (146/902; 18% of 806)**; `depth_check` = known-text alignment with a matched shuffle control
  (gate (a)); `decode_status` Partially decrypted.
- The D2 clause is in both cases the **N0 text**. The N3 text -- everything the solvers added -- is **D1**: scattered
  Spanish words and phrases read by eye from M-graded syllables, no S-graded stretch, no code value read in two contexts
  by the solvers (nomenclature tokens are all U), and gate (b) measures Spanish-likeness of the key-applied text against
  shuffles, which the solvers themselves call "weak support ... nothing more". M-only text is not S.
- **Unique-solve test (N3+ and D2+ on the same text): fails.** The part that is N3 is D1; the part that is D2 is N0.
  No `SECOND-OPINIONS-QUEUE.tsv` row is filed and AUDIT 2 is not due. The parent's status.json entry, if one is
  created, should carry `depth: D2`, the percentages above, `key: published`, `text: known` for the C part and
  `claim_scope` other than recovered-passages/completed-reading, so `tools/depth_check.py` does not count it.

**One true sentence about the content (D2, from the C text, verifier's own words).**
- f.89 letter: Philip II tells Vargas that the Scottish ambassador's proposal to send an agent from Bilbao to Scotland will
  be weighed, that he is to keep the ambassador in hand, report whether the French king or the Guises are doing anything
  for Queen Mary and whether she still has intelligences in Scotland, and tell him that Bernardino de Mendoza has been
  ordered to press for Antonio de Guaras's release.
- f.119 letter: the king defers any decision on men or money for Scotland until Vargas answers his last letter, and
  tells him to ask the Scottish ambassador, as if of his own motion, whether the 4,000 men asked for would be natives or
  foreigners, who would command them, where, when and for how many months they would serve, and what pay captains,
  officers and soldiers draw in that kingdom.
- Not graded, for the record: the M text's sense by eye is consistent with the recipient-side record (Vargas's reports
  on English corsairs and the Indies navigation, Oct 1578; Frangipani, archbishop of Nazareth, in Paris, Sept 1578;
  Alençon and Béarn), but nothing in it is read at S.

**Safe sentence** (rule 10 wording): "Two Cp.30 letters of Philip II to Vargas Mexia in BnF Espagnol 132 (19 Sept and 15
Oct 1578, about 1,940 and 900 cipher tokens) have been decoded with the published key; the one paragraph of each that
Teulet printed in 1860 from the period decipherment reads at grade C (S_a 0.92 against shuffle nulls of 0.35-0.65); the
remaining paragraphs are key-applied text graded M only, for which no prior plaintext was located in Teulet, Kervyn de
Lettenhove, the Maroc *Sources inédites*, CODOIN, Mignet, the solver repositories or DECODE on 4 Oct 2026 (N3; Lefèvre
1940 and the AGS K minutes not read)."
**Unsafe sentence** (not to be used): "Two unpublished letters of Philip II have been deciphered for the first time" --
the deciphering is a published key applied by others before us (cabinet-noir on 30 sibling letters), the printed
paragraphs are N0, and the unprinted text reads at D1.

## 4. Postmortem and corrections

- No over-claim found: NOTES.md, RD7-2026-10-04.md and both PREREG files say "key-applied, cryptanalytic result only",
  "reported as found", "search result, not a novelty verdict" throughout; a grep for new/first/unpublished/never finds
  only a Bourdeau citation and tool prose.
- Correction of record, not of a claim: the earliest print of the two paragraphs is Teulet's *Papiers d'état* t. III
  (Bannatyne Club, 1860) pp.196-197 and 202-203, not the 1862 *Relations politiques* alone; the two editions give the
  same text and the same Simancas references (B.47 n° 8 and n° 6). NOTES.md's "Teulet vol.5 (1862)" stays correct as a
  citation; this file carries the earlier one.
- Two facts for the solvers, written here where established (CLAUDE.md "write it where the fact is established"):
  (1) **f.93-96 is a second ciphered copy of the 19 Sept letter** (Tomokiyo TOC nos.42-43, BnF record, DECODE 1980). A
  duplicate ciphertext of the same plaintext is the one instrument this hand lacks for measuring true reader error
  (err_true "not measurable" on every page so far) and for settling the 113 '?' tokens of the f.89 letter without eye
  arbitration; it is the named next step in NOTES.md. (2) DECODE record 1983's key name "BnF_es132_f119" labels the
  f.115-116 letter (14 Oct 1578, TOC no.53); the f.119 letter has no DECODE record of its own that this session found.
- Rule-4a propagation: depth and class are written here only; status.json has no entry for this target yet (checked
  4 Oct 2026 05:4x UTC), so nothing to propagate; the parent creates the entry from this file.
- `JSTOR-QUEUE.tsv`: 4 rows appended (two per family), status queued. A queued row never blocks the class (CLAUDE.md
  verifier template step 2).

## 5. Propagation (rule 10): reading revised after this AUDIT (A3V3-ES132S, 4 Oct 2026, 06:4x UTC by `date -u`)
The f.89 letter's transcription changed after this file was written: 43 of its 113 '?' tokens were settled from the f.93-95 duplicate copy
(PREREG_dupsettle.md, settle_dup.py, dup_settled.tsv; NOTES.md section "Duplicate settlement"): 25 flags removed, 18 tokens replaced, all
on the unprinted pages f.89r, f.89v, f.90r, f.91r; f.90v (the printed paragraph, C text) is untouched. Effect on this file's numbers: the
f.89 unprinted part is now **1,525 M + 198 U** (was 1,526 M + 197 U; f.89r 410/35 -> 408/37, f.90r 429/65 -> 430/64); the C part (217) and the
letter total (about 1,940 tokens) are unchanged, so the depth percentages (about 11% / 12%) and D2 (C text) / D1 (N3 text) stand; every
settled token is M, so no N3 text moves toward S. Gate (b) still passes on every settled page (S_b f.89r -1.109, f.89v -1.177, f.90r -1.073).
The class (N0 printed / N3 unprinted), the safe sentence ("about 1,940 ... cipher tokens", "graded M only") and the unsafe sentence need no
change. No SECOND-OPINIONS-QUEUE.tsv row exists for this target (grep, 4 Oct 2026), so nothing to propagate there. A fresh rule-7
re-derivation of the settled pages is owed (RD7-2026-10-04.md predates the settlement).

## JSTOR run (local runner, 4 Oct 2026, second sitting)

JSTOR query "Vargas Mexia" "Espagnol 132": 1 result, Geoffrey Parker, review of Reinbold and Vázquez de Prada, The American Historical Review 112 (2007) 930-931, https://www.jstor.org/stable/40006809 -- snippet: "a volume of secret correspondence left by one ambassador, Juan de Vargas Mexia, when he died in Paris may be found in the Bibliotheque Nationale de France (Manuscrit Espagnol 132)". Identifies the volume; prints nothing. The three Vargas Mexía phrase queries returned 0.
