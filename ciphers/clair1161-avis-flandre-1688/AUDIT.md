# AUDIT 1 (A3V2-C1161A1, 4 Oct 2026): novelty class and reading depth of the merged 3,389-sign reading

Verifier: worker A3V2-C1161A1 (account 3, for LANE-A3V2), brief `.claude/briefs/runs/2026-10-04-acct3-a3v2-wave1.md`; a
session separate from every solver of this target (READ2-C1161, READ2-C1161B, NEAR3-C1*, N4-C1) and from the rule-7
re-derivation session (N4-RD1161, LANE-NEAR4). Clock by `date -u`: 04:56 UTC at claim, searches 04:58-05:2x UTC. No
decoding here; key.tsv, ciphertext.tsv and reading.txt are unchanged by this audit.

**Claim under audit** (ROOM 04:31 UTC, commit 94f1bf9b, NOTES.md "N4-C1"): key.tsv (S 15 / M 28 / C 6 signs) decodes the
3,389 cipher signs of the six cipher leaves/blocks at c185R-c188L to a reading graded C 353 / S 1697 / M 1325 / U 33;
two-instrument agreement 0.624 vs shuffled-order max 0.351 (PASS); fr16 judge FAIL -1.233 vs real_p05 -0.905, while the
c186R period marginal gloss PASSes the same judge at -0.808.

## 1. The item, as the repository states it

| field | value | source |
|---|---|---|
| shelfmark | BnF Clairambault 1161, Gallica ark:/12148/btv1b90010063, canvases c185R, c186L, c186R block, c187L, c187R, c188L (IIIF f186-f189); ink foliation "162"-"164" on the leaves | IMG-GALLICA1, N4-C1 |
| finding aid | archivesetmanuscrits.bnf.fr ark:/12148/cc137837/cd0e35310, "Fol. 106 et suiv.", the composite Noailles note: "... Avis de Flandre, chiffrés ; lettre orig. de François II de Noailles, évêque de Dax, au marquis de Villars, 20 déc. 1570" | M20 check-solved |
| headings on the leaves | c186R "Advis de flandres"; c187L "Autres advis"; c187R carries the clear date "Juil 23" (year not written) | IMG-GALLICA1, N4-C1 |
| date | c. 1570: the leaves are mounted in the same bundle as, and immediately before, the clear letter signed "Noailles e. d'Acqs", Paris, [20?] Dec 1570 (c188R). The slug's "1688" is the volume's chronological slot in the Saint-Esprit minutes series, not the item's date | N4-C1 "Dating and the slug" |
| sender / recipient | **not established**. The Avis carry no signature or address; the bundle is a Noailles-family dossier (the Dax letter is to Honorat de Savoie, marquis de Villars) | all passes |
| cipher | pen-sign homophonic-type alphabet, 57 sign types over the six leaves, 49 keyed; design_prior: homophonic plausible, code excluded | READ2-C1161 |
| period gloss | a contemporary marginal note of about 12 short lines beside the c186R block, read as clear French (170 letters, `align/pairs_c186R_v0.tsv`): "...seigneurs a par[ticulier] / ?x foys escript et mander / [a l]a royne quelle / n'est pas[se]... / beaucoup [de] chose quant au fet / [de l]a Religion en ce Royaulme / [ro]m de Espaigne sa / ...e ce peuple et gens / ... / [e]n grand Repoz" | READ2-C1161 |
| key source | **ours**: a blind homophonic anneal (fr16 corpus) on c185R + the c186R block, 6 signs confirmed at grade C from the period gloss, 15 signs S by agreement with a second blind anneal on the four other leaves, 28 M | READ2-C1161B, N4-C1 |
| reading | `reading.txt` / `reading_tokens.tsv` by `tools/decode_key.py` (`--check` exit 0 on 4 Oct 2026): tokens 3408 = C 353, S 1697, M 1325, U 33 (U = clear words, `/` marks and 7 unkeyed NEW_* shapes); cipher tokens 3375 | N4-C1 |

Distinctive text available for a phrase search: the finding-aid title; the gloss's clear phrases; and the decode's
C/S-graded clauses (c185R L01 "les aultres prisonniers", L06 "entreprinse ... seraient par ... executee", L15 "reportees a
la cour", L16 "ce qui sera execute", c186R L05 "religion en ce royaul[me]", L08 "en plus grand repo[s]", c187R L20 "leur
conseil et tout").

What the solvers searched before this audit (NOTES.md): LANE G and LANE CX check-solved (24-25 Sept 2026: web, Rousset
*Louvois* IV full text, Cryptiana, DECODE catalogue CSV, both solver repositories), GF4-BATCH11 web/blog check and Premise
check (3 Oct 2026: three blogs, Cabinet Noir, fresh solver-repo clones, Gallica neighbours). N4-C1 searched nothing new.

## 2. Independent search (this session, 4 Oct 2026, 04:58-05:2x UTC)

Full texts were fetched once from archive.org (`_djvu.txt`, descriptive UA, >= 1.8 s apart, 8 requests) and grepped
after folding accents, u/v and i/j, for: "a(d)vis de flandre(s)", "chiffr", "Noailles", "(evesque de) Dax / d'Acqs",
"Villars", the gloss phrases ("fet de la religion", "religion en ce roya(ulme)", "grand repo(s/z)", "escript et mand(er)"),
and the decode's clauses ("aultres prisonniers", "entreprinse", "dissimulation"). A hit on a generic phrase is listed
when it was read in context and found to be unrelated.

| family | source | searched by | result |
|---|---|---|---|
| (a) canonical series | Kervyn de Lettenhove, *Relations politiques des Pays-Bas et de l'Angleterre*, t. V (IA relationspolitiq05nethuoft; years 1568-70) and t. VI (relationspolitiq06nethuoft; 1570-73) | full text grep | **no** "Avis/Advis de Flandre(s)"; no Noailles-Dax or Villars 1570 piece. Control: both volumes print many "(en chiffre)" Spanish dispatches, 203 and 169 "chiffr" hits, so the OCR reads. The one "fait de la religion" hit (t. V) is an unrelated English passage |
| (a) | Gachard, *Correspondance de Philippe II sur les affaires des Pays-Bas*, t. II (correspondancede02phil; 1568-73) | full text grep | no; "fait de la religion" x5 and "plus grand repos" x1 are Alba/Philip II formulae, not this text |
| (a) | *Lettres de Catherine de Médicis*, t. III (lettresdecatheri03cathuoft; 1567-70) and t. IV (lettresdecatheri04cathuoft; 1570-74) | full text grep | no Avis de Flandre; "Villars" 12/11 hits are the marquis's Guyenne command; "d'Acqs" 6 hits (t. IV) are the Constantinople embassy 1571-74; "en plus grand repos en son royaulme" and "escript et mande" occur in Catherine's own letters: court idiom shared with the gloss, not a print of it |
| (b) sender / recipient editions | no sender is established. Noailles side: Charrière, *Négociations de la France dans le Levant*, t. III (ngociationsdel03charuoft; François de Noailles 1571-74) | full text grep | no ("d'Acqs" 193 hits, all the embassy; "Villars" 2, Guyenne 1570 and a Lucca remittance) |
| (b) | Vertot, *Ambassades de Messieurs de Noailles en Angleterre* (1553-57; ambassadesdemess01-05vert) | phrases only, via print_check (t. V in sources.tsv) | see section 2a; wrong decade, listed for completeness |
| (b) | Gallica btv1b100339270, "Extraits de la correspondance de François de Noailles, évêque de Dax, ambassadeur à Constantinople, avec la cour de France (mai 1571-sept. 1574)" | located by web search; **not opened** (a manuscript, later than 1570) | logged for the next step, not a negative |
| (b) | Villars side: no printed correspondence of Honorat de Savoie, marquis de Villars, exists; La Mothe-Fénelon, *Correspondance diplomatique*, t. III (correspondanced03coopgoog; 1569) and t. IV (correspondanced04coopgoog; 1570-72), the London embassy that relayed Flanders news to the court | full text grep | no Avis de Flandre, no Noailles/Dax/Villars cipher; "en plus grand repos en son royaulme" x1 (t. IV) is Catherine's letter again |
| (c) documentary editions | as (a)-(b). **Not searched**: Calendar of State Papers Foreign 1569-71 and CSP Spanish (Simancas) II (British History Online), Teulet *Relations politiques ... avec l'Écosse* (no IA copy found by advancedsearch) | - | unreachable/not searched this session; a cipher avis in French would in any case appear there only as an English abstract |
| (d) holding archive | BnF finding aid cc137837/cd0e35310 (quoted above); Gallica SRU `gallica all "Advis de Flandres"` (6,273 records, top 10 titles read: a printed *Advis de Flandres* of 25 Jan 1620, "Lettres originales de plusieurs ambassadeurs français aux Pays-Bas ... 1571-1594", Terre-sainte recueils); Lauer, *Catalogue des manuscrits de la collection Clairambault*, t. II (Gallica bpt6k209158x) | SRU; Gallica ContentSearch on the Lauer ark for "Flandre" (HTTP 200, countResults 0: the OCR index answered nothing, not a negative); texteBrut altcha-blocked (GF4-BATCH11, 3 Oct); Google Books API returns the catalogue (ids Qi2qCpRVLQQC 1923, QVLgAAAAMAAJ 1924) for the exact query `"Avis de Flandre, chiffrés"`, viewability NO_PAGES, no snippet; HathiTrust bibliographic API for OCLC 39559023 (Open Library) returned no items | **Lauer's entry for 1161 exists and contains the phrase, but its text is unread from the cloud** (LOCAL-QUEUE item named by GF4-BATCH11). No BnF blog or project page on the item (web searches 1-3 below) |
| (e) full text | Internet Archive full-text search across all items, Google Books API (`country=US`, key), HathiTrust (HTRC EF; babel is cloud-blocked) | `tools/print_check.py` on `phrases.txt` (13 phrases) + `sources.tsv` (8 IA volumes) -- section 2a | see 2a |
| (e) | Google Books API, 11 direct queries: `"Avis de Flandre" chiffrés Clairambault`, `"Advis de Flandres" 1570`, `"Clairambault 1161"` (28 hits: Saint-Simon *Mémoires* editions citing fols 28, 188, 190, 251-256 of this volume, other items), `Noailles "évêque de Dax" Villars "1570" chiffre`, `"quant au fet de la religion"`, `"escript et mandé à la royne"`, `"en plus grand repos" Flandres 1570 advis`, and four Lauer-targeted forms | API | nothing on this item's text or decipherment; the only hits for the exact title are Lauer's catalogue (above) |
| (f) solver repositories | fresh shallow clones 4 Oct 2026 05:0x UTC: dbourdeau/cyphersolver HEAD a439937, aaymeloglu/unsolved-ciphers HEAD d2800bb, el-descifrador/cabinet-noir HEAD 47b6db9 | grep -i "clairambault 1161", "avis de flandre", "advis de flandre", "btv1b90010063" | **0 / 0 / 0**; "noailles" hits are Gallica sweep notices (cyphersolver), a word list (unsolved-ciphers) and 1743 clear passages (cabinet-noir) |
| (f) cipher blogs | Cryptiana local snapshot `sources/cryptiana/` (grep "Villars": Joyeuse-Villars 1594 and Marshal Villars 1710 only; "Clairambault 1161" 0; the Noailles pages are the 1553-70 ambassador ciphers of Tomokiyo's elizabeth/mary/henryii-iii/frencheastern pages, none this item); web site-search of cryptiana.web.fc2.com (no indexed hit); DECODE: the 25 Sept catalogue CSV grep (NOTES.md) stands, not re-run live (no login spent) | grep, WebSearch | nothing |
| (g) scholarship | OpenAlex (key, 4 queries: "Noailles cipher 1570 Flanders" 1 unrelated; "Clairambault 1161" 28 works, top 5 read by title, none on a cipher -- the nearest, "Dans l'ombre des ordres : les ordres de chevalerie et les territoires de la collection Gaignières" (2023), concerns the Saint-Esprit volumes and was not opened; `"Avis de Flandre" chiffre` 0; "Noailles Dax Villars 1570 chiffre" 0); Semantic Scholar (key, 2 queries, 0); CrossRef (1 query, noise); HAL (1 query, 0); Persée reachable (HTTP 200) but not queried further; JSTOR: 4 rows appended to `JSTOR-QUEUE.tsv` in both families (i) sender/place/date + cipher keyword and (ii) bare quoted phrase | APIs | nothing located; JSTOR pending (a queued row never blocks N3/N4 on its own) |
| web | WebSearch, 7 queries (3 standard + 1 extended on the title/sender/date/shelfmark, 2 on Kervyn and Lauer, 1 on `"Clairambault 1161"`) | - | no page discusses or deciphers the item; the extended search surfaced only the BnF finding aids, Wikipedia on the Noailles brothers and the Gallica manuscript btv1b100339270 above |

Requests this session (outside print_check): archive.org 17 (9 advancedsearch, 8 `_djvu.txt` downloads), googleapis.com 11, api.openalex.org 4, api.semanticscholar.org 2, api.crossref.org 1, api.archives-ouvertes.fr 1,
persee.fr 1, gallica.bnf.fr 2 (SRU, ContentSearch), openlibrary.org 2, catalog.hathitrust.org 1, github.com 3 clones,
WebSearch 7; plus print_check.py's own counts in `print-check-hosts.tsv`. One host at a time, >= 1.6 s apart, no 403/429/
challenge seen. Subagent calls: 0.

### 2a. print_check.py

`python3 tools/print_check.py ciphers/clair1161-avis-flandre-1688 --max-requests 220 --delay 1.6` (05:09-05:14 UTC): 12 phrases
x 10 listed sources = 148 rows, 30 with hits, `print-check.tsv`; hosts `print-check-hosts.tsv` (archive.org 8, be-api 12,
googleapis 12, openalex 13, crossref 2; Semantic Scholar answered HTTP 429 on its first call and was not retried, so the
s2 column reads "not searched"). Every hit was read:
- Listed IA volumes: "Advis de flandres" 1 exact in Vertot t. V = the common phrase "aduis de Flandres" (news from
  Flanders) in a 1550s Noailles dispatch, not this item; "en plus grand repos" 1 exact and "en grand repoz" 2 near in
  Catherine's letters t. III, "religion en ce royaulme" 1 near each in Fénelon t. III and Vertot t. V -- all court idiom
  in other letters. No listed volume carries two of the gloss phrases together or any decode clause in context.
- IA full-text across all items: the 1620 printed *Advis de Flandres*, chronicles (Froissart, Molinet) for "les aultres
  prisonniers", William of Orange's correspondence for "leur conseil et tout", 18th-c. Illinois records for "ce qui sera
  execute": generic French, no 1570 Noailles item.
- Google Books: Lauer's catalogue is the only volume returned for the exact title; the phrase hits are 16th-19th-c.
  texts using the same idioms. One query ("entreprinse seraient par") got HTTP 503 and was not retried.
- OpenAlex: the 1620 pamphlet and four unrelated articles. CrossRef: Noailles-family biographical entries.
Result: **no printed plaintext and no decipherment of these leaves found by this method on 4 Oct 2026** (a search result,
not a novelty verdict).

## 3. Classification

**Prior plaintext: no** (none located in (a)-(g)). **Prior decipherment: no** -- except that the leaf itself carries a
contemporary marginal gloss that is a period decipherment of one 220-sign block (c186R), which is part of the source, not
a prior publication; it is what makes the 6 C grades possible and it is the external check in section 4.

**Class: N3** -- no prior plaintext or decipherment located after the search logged above. Not N4: the volume's own
catalogue entry (Lauer t. II, the fullest description of the item and the one place a date or sender might be recorded)
is unread from the cloud; the sender is unidentified, so no sender-specific edition can be declared covered; CSP
Foreign/Spanish were not searched. **Key: ours. Text: not known in print.**

Evidence quality: the two matched controls (two-instrument 0.624 vs shuffled max 0.351; gloss match 0.594 vs shuffled-order
anneals max 0.312) show the key carries real sign-order information; the judge FAIL on a reading whose own period gloss
PASSes the same judge says the key is right on its frequent signs and wrong or unsettled on many others, as the grades
say. Confidence in N3: high for "not in the editions read"; medium overall, because the item's sender and exact date are
unknown and Lauer is unread.

- **Safe sentence:** "A key recovered by cryptanalysis (ours) decodes the six 'Advis de flandres' cipher leaves in BnF
  Clairambault 1161 (c. 1570, Noailles bundle; 3,389 signs) at grades C/S on about 61% of the signs, in fragments rather
  than running text; the leaf's own contemporary marginal gloss is a period decipherment of one 220-sign block and
  agrees with the recovered key on 0.59 of its letters against a shuffled-order maximum of 0.31; no prior plaintext or
  decipherment was located after the search logged in AUDIT.md (N3)."
- **Unsafe sentence:** "The Noailles 'Avis de Flandre' cipher of 1570 has been deciphered for the first time."
  (Depth is D1, so "deciphered" in any form is wrong; "first" is barred below N4 by rule 10.)

## 4. Depth (rule 4a, step 3a)

| measure | value |
|---|---|
| cipher tokens | 3,375 (3,408 minus 33 U) |
| H / C / S | 0 / 353 / 1,697 = **2,050 = 60.7%** at C or better; M 1,325 (39.3%) |
| key coverage | 49 of 57 sign types keyed; 21 of 49 at C/S, 28 M |
| longest contiguous C/S run | **12 tokens** (c187L L21 "outencoresta", c186R L05 "relilionince" = gloss "religion en ce"); 7 runs >= 10, none >= 15; median run 2 (`reading_tokens.tsv`, runs broken at line ends) |
| authentication distance | for a 49-sign homophonic design the unicity distance is already of the order of 10^2 letters before the liberties taken (0.08-0.10 two-reader transcription error, 28 M signs); no C/S stretch comes within a factor of 5 of it |
| external check | the c186R period gloss: letter agreement 0.594 (0.612 after repair) on one block of 220 signs; both the block's decode (-1.154 vs real_p05 -1.002) and the full reading FAIL the fr16 judge that the gloss itself PASSes (-0.808) |
| judge | FAIL -1.233 (real_p05 -0.905, null_p99 -1.758, N 3375) |
| rule 7 | see section 5 |

**Depth: D1 ("fragments read").** Scattered words and short clauses read (prisonniers, entreprinse, descouvertes,
reportees a la cour, religion en ce royaulme, en plus grand repos, conseil, dissimulation); no stretch above the
authentication distance; the one external check confirms the key at letter level on one block, not a clause-level reading
that could be quoted without the gloss beside it. A D2 would need either a C/S stretch of the order of 100 letters or a
block whose decode a reader can quote as a sentence and the gloss confirms word for word; the c186R block decode
("...relilion in ce royaule ... en plus lrautre pore...") is not that. This verifier therefore writes no `depth_sentence`:
everything true that can be said about the content ("letters written several times to the queen about religion in this
kingdom and about Spain; the people; greater repose") comes from the period gloss, not from the reading.

status.json: `depth D1`, `depth_pct 60.7`, `depth_check "period-gloss letter agreement 0.594 on one 220-sign block;
judge FAIL; longest C/S run 12"`, `decode_status Non-decrypted` (written on the target's `near` entry; it has no `results`
row and, at D1, is not counted). Outward wording: "fragments read", never "partially deciphered" or "deciphered".

**Unique solve (N3+ and D2+): no.** No SECOND-OPINIONS-QUEUE.tsv row is added (the N3 is real, the D2 is not).

## 5. Rule 7 (re-derivation by N4-RD1161, LANE-NEAR4)

`RD7-2026-10-04.md` (N4-RD1161, account 2, 04:53-05:08 UTC, commits 9f8c28be / 755d6b79; read by this verifier at 05:12 UTC
after the search steps above): **SAME**. A fresh session that had seen only the spec, key.tsv, ciphertext.tsv and the scripts'
headers regenerated reading.txt and reading_tokens.tsv byte-identical to 94f1bf9b (3408 tokens, 0 differ in value or grade,
against 1325 M allowed), and re-ran instrument 2's eight anneals (8/8 key files byte-identical; agreement 0.624 vs shuffled
max 0.351 reproduced). Its scope note holds for this audit too: the re-derivation checks the pipeline from transcription to
reading, not the transcription against the images, and not whether instrument 2's recipe is the right one. The classes above
are therefore **not provisional**; depth D1 does not depend on it.

## 6. Postmortem and corrections

- No sentence in NOTES.md, HYPOTHESES.md, NEAR.md or status.json calls the reading new, first, unpublished or
  deciphered; every solver section ends "novelty is not classified here". Nothing to retract.
- One wording tightened under rule 4a: NEAR.md's row said "3389 signs read"; changed to "3389 signs decoded under key.tsv
  (depth D1, AUDIT 1)". The reading is a decode at 60.7% C/S with a FAIL judge, which the row's own numbers already said.
- Named for the next step (not actioned here): Lauer t. II's entry for Clairambault 1161 (owner's browser; may carry a
  date or sender); the Gallica manuscript btv1b100339270 (Noailles-Dax correspondence 1571-74) as a possible source of
  the same hand or key; the 28 M signs (N4-C1's multi-seed instrument). None of these changes the class; the first could.
