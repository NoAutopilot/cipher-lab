# AUDIT -- fr16142-noailles-constantinople-1571

## AUDIT 1 (VER1-NOX, 5 Oct 2026) -- the basin reading (N8-NOX, N8-NOX2, RUN6-NOXREAD)

Verifier session VER1-NOX (LANE-VER1, account 2), brief `.claude/briefs/runs/2026-10-05-ytbiz-ver1-jobs.md` "VER1-NOX".
A fresh session, not the solver of any reading here; nothing decoded, no transcription, key or alignment touched. Clock read by
`date -u` at start (18:40 UTC) and before every dated line.

### Claim under audit
NOTES.md (N8-NOX, N8-NOX2, RUN6-NOXDEC, RUN6-NOXREAD, RUN6-NOXALIGN, 4-5 Oct 2026): the stream aligner's lock-on of the c510-516
atlas piles onto the clear copy in BnF Dupuy 521 ff.221R-226R is "a basin with one common key" (S 0.601 vs nulls 0.273/0.384);
that key agrees with Tomokiyo's published key on 7 of 17 bridge piles (PASS vs 4/5/5); mapped onto the reconciled c262 reader
signs it "reads c262 toward its period gloss beyond the four nulls" (R 0.309 vs p99 0.2404/0.2518/max 0.2003/0.2833, thin on
the non-locking arm); "every value stays grade M", "no reading is claimed", "0 open leaves decoded". This audit checks that
wording, classes what is read, and checks whether the c262 plaintext is in Charrière.

### 1. Extract (per item)
| item | leaves (Gallica btv1b9060927q) | date, sender -> recipient, place | what the repo reads | period decipherment / clear copy | solver's search |
|---|---|---|---|---|---|
| A | fr.16142 c262 (one cipher block of the letter c257-266; 384 reconciled reader signs, `witness/c262rc_recon.tsv`) | 25 April 1572, François de Noailles, bishop of Acqs (Dax) -> Charles IX, Constantinople (Pera) | the basin-key decode in `aln/results/noxread_summary.json` "decode": a 384-letter string with no French word in it ("emepdlmetsadlerprmmcrmreexlaedreteurtm..."); 'm' is the most frequent letter (75/384) | yes: running margin decipherment on the leaf (`gloss.tsv`, FT-D); Dupuy 521 36L-36R (date match, `dupuy521_align.tsv`) | Charrière III grepped whole (CS-4, FT-D), solver repos, blogs (CS-4, 3 Oct) |
| B | fr.16142 c510-516 (7 cipher pages, 9,904 atlas tiles, 108 owner piles) | 7 July 1574 (Dupuy: 6 July), Noailles -> Charles IX, Pera | nothing: the basin key was *learned* from this pair against Dupuy's clear text; no c510-516 decode is reported | no gloss on the leaves; Dupuy 521 221R-226R clear copy, text-confirmed at both ends (RUN1-NX); Charrière III pp.551-558 prints excerpts of the 7 July 1574 despatch (RUN1-NX) | as above |

### 2. Independent search (5 Oct 2026, 18:41-18:47 UTC)
Phrases (`phrases.txt`, written by this verifier, 5 lines): four from the c262 period gloss, one from the c516 clear lead-in. The
basin decode carries no word, so nothing from it could be phrase-searched. `tools/print_check.py ... --max-requests 60` ->
`print-check.tsv` / `print-check-hosts.tsv` (29 rows, 17 with hits).

| family | searched | result |
|---|---|---|
| (a) canonical series | Charrière, *Négociations de la France dans le Levant* III (1853), IA `ngociationsdel03charuoft` (cached djvu text, `sources/ia-fulltext/print-check/`), whole-volume grep by this verifier for the gloss words and the letter's opening | **c262's passage is printed.** Charrière III prints the evêque d'Acqs's letter "Constantinople, 25 avril 1572" ("Sire, depuis mon partement de Venize, j'ay escript à V. M. de Tassileger ...") from p.252; on p.258: "... voz huguenots ou autres veullent s'aller promener en Flandres par mer et par terre, vous ne vouldrez empescher l'antienne liberté des gens de guerre de vostre nation. Pendant le temps que la farce se jouera du costé de delà, il ne faudra pas qu'il s'endorme de deçà, car la partie est forte. Il est vray que j'ay trouvé ces gens-icy si comblés de bien et de mal, c'est-à-dire de richesses et de volupté en toutes sortes, qu'il semble qu'on leur feroit plaisir ..." (OCR normalised by eye; djvu lines ~19300-19340) = gloss.tsv L01-L13 almost line for line. The 7 July 1574 excerpts (pp.551-558) re-confirmed by print_check ("des conspirations faictes contre sa personne", 1 exact). |
| (b) sender/recipient-specific print | IA full-text across all items (ia-global, be-api) for the five phrases | "de richesses et de volupte en toutes sortes": 4 items -- Charrière III (two scans: `ngociationsdel03charuoft`, `baclac_1007364698_003`) and *Bulletin de la Société de Borda* (Dax), 1888 (`bulletindelasoc182unkngoog`; the Dax society's bulletin, where a study of the bishop of Dax would sit; page not read, one be-api request, no snippet returned); "car la partie est forte": 14 items, the same Borda volume among them; "des conspirations faictes contre sa personne": 3 items, all Charrière III scans. Lettres de Catherine de Médicis not searched by this verifier (CS-4 lists it as not read). |
| (c) documentary editions | Google Books API (key, `country=US`), five phrases | "car la partie est forte", "de richesses et de volupte...", "des conspirations faictes...": Charrière III (several Google scans), *Bulletin de la Société de Borda* 1888, *Collection de documents inédits* 1853 (= the Charrière series); "sendormir de ca" and "comblez de biens" queries return loose matches only |
| (d) holding archive / project pages | Gallica fr.16142 and Dupuy 521 described from NOTES.md (CS-4 notice reads, RUN1-NX date index, RUN6-NOXDUP text checks); not re-fetched by this verifier | Dupuy 521 carries the clear text of both letters (A by date, B by text) |
| (e) full text IA / HathiTrust / Google Books | as (b), (c); HathiTrust EF not used (the printed edition is already found) | -- |
| (f) solver repositories, blogs | shallow clones 5 Oct 2026: dbourdeau/cyphersolver (grep 16142/acqs/noailles), aaymeloglu/unsolved-ciphers (same) | Bourdeau: only the Venice 1558 Noailles candidate (`research/gallica_sweep/bnf_candidates.txt` line 125) and Tomokiyo mirrors (`targets/segur/henryiii.txt`); no fr.16142 target or reading. Aymeloglu: no hit. Cryptiana `henryiii.htm` (Tomokiyo) publishes the key for exactly this cipher and names fr.16142 ff.109-275 (CS-4). Blogs: CS-4's 3 Oct engine searches, not repeated. |
| (g) scholarship | OpenAlex (Bearer key; 5 phrases + 1 keyword query), CrossRef (2 keyword queries), Semantic Scholar (3 phrase queries answered, then HTTP 429, not retried -- 2 phrases and the keyword query unreached) | nothing on this letter or this cipher's decipherment |
| JSTOR | 2 rows appended to `JSTOR-QUEUE.tsv` (family i: "évêque d'Acqs" AND Constantinople AND 1572 AND chiffre; family ii: "si comblés de bien et de mal") | queued; does not block the class |

Requests: be-api.us.archive.org 6, archive.org 1 (metadata), www.googleapis.com 5, api.openalex.org 6, api.semanticscholar.org 4
(one 429), api.crossref.org 2, github.com 2 shallow clones. Unreachable: Semantic Scholar after one 429.

Judge on the basin decode (rule 7), run by this verifier on the `noxread_summary.json` "decode" string:
```
FAIL language: score=-2.045, null_p99=-1.854, real_p05=-0.889, real_median=-0.781, mode=both, N=384
ok   words: cover=0.523, min=0.5, real_text_median_cover=0.948
FAIL - fr16142-noailles-constantinople-1571 (a PASS is a gate for a verifier, not a reading; rule 10)
```
The decode scores below the shuffled-null p99: it is not French at any length, consistent with the solvers' own "no reading".

### 3. Classification
| item | N-class | key source | text | evidence quality / confidence |
|---|---|---|---|---|
| A c262 (25 Apr 1572) | **N0** | published (S. Tomokiyo, cryptiana henryiii.htm, credited) for key.tsv; the basin key is ours (learned by plain-copy alignment against Dupuy 521), and reads no word here | known | high: the period margin decipherment is on the leaf, a clear copy is in Dupuy 521 36L-36R, and the passage is printed in Charrière III p.258 (1853) and very probably in the *Bulletin de la Société de Borda* 1888 |
| B c510-516 (7 July 1574) | **N0** | the basin key: ours (learned from this very pair); published key not applied to it | known | high: Dupuy 521 221R-226R is the whole letter in clear (text-confirmed at both ends), Charrière III pp.551-558 prints excerpts; nothing has been decoded |

Earliest citations: Charrière III (Paris, Imprimerie impériale, 1853), pp.252-258 (A) and pp.551-558 (B); Dupuy 521 (17th-century
fair copy, both). Prior decipherment: yes for both, a period one (A: the margin gloss and Dupuy; B: Dupuy, the letter in clear).

### 3a. Depth (rule 4a)
| item | % H/C/S | unread | depth | check | content sentence |
|---|---|---|---|---|---|
| A | 0% (0 of 384 signs above M; RUN6-NOXALIGN's per-token alignment a non-test, S 0 = nulls 0) | all | **D0** | the basin key ranks above four nulls on the ratio R (0.309 vs p99 0.2404/0.2518/max 0.2003/0.2833, the non-locking arm thin: one subset in 924 ties) and agrees with the published key on 7 of 17 bridge piles; no word reads (judge -2.045, below the null p99) | -- (D0) |
| B | 0% (no decode) | all | **D0** | the basin itself (S 0.601 vs N1 p99 0.273, N2 max 0.384) is a property of the alignment, not a reading | -- (D0) |

Outward words: none beyond "a key learned from a clear copy agrees in part with the published key". Not "fragments read" (that is D1).

### 4. Postmortem
No outward sentence over-claims: NOTES.md says "no reading is claimed" and "all tokens M" at every step. Three corrections, dated:
1. NOTES.md (RUN1-NX, 4 Oct): "c510-516 + Dupuy 221R-226R is a ~9,750-sign known-plaintext pair on leaves no reader has seen
   before" -- "no reader has seen before" is a novelty word (rule 10) about the leaves, which BnF readers, the Dupuy copyist and
   Tomokiyo (who names ff.109-253 and reconstructed the key) have all handled. Safe form: "on leaves no reader in this repository
   had transcribed before". Correction note appended to NOTES.md.
2. `gloss.tsv` (FT-D's reconciled c262 margin gloss, the reference for every c262 gate: test0, NX-RECUT, RUN6-NOXDEC/NOXREAD/
   NOXALIGN) differs from Charrière's print of the same passage at several words: L01 "bruslent" (print: "veullent"), L04 "le
   bestial" (print: "l'antienne liberté"), L06 "la faim se trouva" (print: "la farce se jouera"), L08 "sendormir de ca" (print:
   "s'endorme de deçà"). The print rests on another copy and is itself OCR'd here, so neither side is authority by itself; but the
   gate reference carries reader error of its own, which lowers every R on c262 (the published key's 0.4548 ceiling included).
   Suggestion for the solvers (not done): re-read the gloss against Charrière III p.258 before any further c262 gate.
3. The c262 plaintext was not previously recorded as printed: CS-4/FT-D grepped Charrière III for "Noailles/Acqs/chiffre/dates"
   and the 1574 footnotes, not for the gloss words. It is printed (p.258). Any future "open" or "not in print" wording about
   c257-266 is wrong.

### 5. Safe and unsafe sentences
- A safe: "On BnF fr.16142 (25 April 1572), a key learned from the clear copy of a later letter, mapped onto one reader
  transcription, scores above four shuffled controls against the leaf's own period decipherment, but reads no words (D0); the
  letter's text was already known from that decipherment, from Dupuy 521 and from Charrière's 1853 edition (N0); key published
  by S. Tomokiyo."
- A unsafe: "We read Noailles' 25 April 1572 letter" / "the basin key deciphers c262" / any "new" or "first".
- B safe: "For the 7 July 1574 letter (fr.16142 c510-516), an alignment against the Dupuy 521 clear copy learns a consistent key
  (D0, nothing decoded); the letter's text is known from Dupuy 521 and in part from Charrière III (N0)."
- B unsafe: "c510-516 is an undeciphered letter" / "the July 1574 letter is decoded".

### depth_check
`python3 tools/depth_check.py` after adding the two status.json result rows (5 Oct 2026, 18:48 UTC), exit 0; the two rows are
D0 with no N3 claim, so they fall under "not counted D0/D1" and raise no flag:
```
unique solves (N3+ and D2+): 16 -- D4 1, D3 2, D2 13; not counted D0/D1: 13; legacy ungraded: 0
```
No SECOND-OPINIONS-QUEUE.tsv row: both items are N0 (a row is filed only at N3 or better).

## Revision after AUDIT
- DEF1-NOXG (5 Oct 2026): gloss.tsv L01-L06, L08 corrected from native crops of the c262 gloss (three of VER1-NOX's four print differences were gloss misreads; at L08 the leaf differs from Charrière p.258); RUN6-NOXREAD re-run PASS R 0.3506 (was 0.309), test-0 gates now pass -- NOTES.md "DEF1-NOXG".

## AUDIT 2 (D2-NOXA2, 5 Oct 2026)

Verifier session D2-NOXA2 (LANE DEFAULT-account-1-20261005-2217, account 1), brief `.claude/briefs/runs/2026-10-05-account1-default-2217-jobs.md`
"D2-NOXA2". A fresh session: not the solver of any reading here and not VER1-NOX. Nothing decoded, no gloss, key, transcription or reading
touched. Clock by `date -u`: start 23:01 UTC, searches 23:04-23:08 UTC. Audit 1 text above is left as written.

### Claim under audit
Audit 1 (VER1-NOX): A c262 N0 D0, B c510-516 N0 D0, both "text known". Revisions since Audit 1, carried here: DEF1-NOXG (gloss.tsv L01-L06,
L08 corrected from native crops; RUN6-NOXREAD R 0.309 -> **0.3506**, p99 0.2413/0.2496, max 0.2665, non-locking p99/max 0.2581/0.2749; test-0
gates FAIL -> PASS on pass B and pass D; NOXALIGN S 0 -> 2 of 41, very thin) and DEF1-NOXB (blind second read of the gloss crops, control
0.667 < 0.80 gate, a non-test). Job: try to break N0 -- is there a prior *decipherment* of these very leaves, as distinct from the plaintext
in print -- and set the depth count.

### 1. Extract
As Audit 1 section 1. Items unchanged: A = c262 (25 Apr 1572, 384 reconciled reader signs, period margin gloss on the leaf, clear copy Dupuy
521 36L-36R); B = c510-516 (Dupuy: vj Juillet 1574, "des Vignes de Pera"; Dupuy 521 221R-226R in clear; nothing decoded). Solver-side
searches: CS-4, FT-D, RUN1-NX (3-4 Oct), VER1-NOX's own pass (5 Oct, 18:41-18:47 UTC).

### 2. Independent search (5 Oct 2026, 23:01-23:08 UTC)
| family | searched | result |
|---|---|---|
| (a) canonical series: Charrière III | whole-volume grep of the cached djvu text (`sources/ia-fulltext/print-check/ngociationsdel03charuoft_djvu.txt.gz`) for "chiffr", "déchiffr", "Fréville", "16142", "Mortemart", the gloss words, the 7 July 1574 passages | **Prior modern decipherment in Charrière, but not of these leaves.** Charrière credits M. de Fréville (École des chartes) with deciphering fr.16142 letters left undeciphered: the 1569 Grandchamp letters (p.80-81 note: "Elles ont été déchiffrées par M. de Fréville ... quelques autres ... que j'indiquerai ci-après") and a Germigny despatch of 26 Jan 1580 (p.~852, "Cette pièce, dont le déchiffré n'existe plus, est une de celles qui ont exercé la sagacité de M. de Fréville"). Neither is item A or B, and no Fréville note attaches to the 25 Apr 1572 letter (pp.252-260 note) or the 7 July 1574 extracts (pp.551-552 "dans sa lettre du 7 juillet", and the 7 July 1574 letter to Catherine, p.557), which Charrière prints as text from period copies. So the c262 and c510-516 texts in Charrière are period clear text, not a 19th-century cryptanalysis -- but the same volume shows fr.16142's cipher was attacked in 1853 by Fréville, which any outward sentence about this volume must not ignore. |
| (a) Testa, *Recueil des traités de la Porte ottomane* I (1864) | Google Books API, `"Recueil des traités de la Porte ottomane" 1572 Noailles` | prints Noailles' memoir to Charles IX of March 1572 and a further "Dépêche de l'ambassadeur de Noailles" (snippet only; date not shown); not read; no decipherment note in snippets |
| (a) Hammer, *Histoire de l'Empire ottoman* | not searched (a narrative history; would not print a decipherment) | unreached by choice, logged |
| (b) sender-specific print | Google Books API: Tamizey de Larroque, *Lettres inédites de François de Noailles, évêque de Dax* (1865, = Revue de Gascogne VI); *Un évêque de Dax. François de Noailles* / *Bulletin de la Société de Borda* 1888 (IA `bulletindelasoc182unkngoog`, djvu text fetched and grepped); Louis Paris, *Le Cabinet historique* (1867); *Revue de Gascogne* 1930; *Lettres de Catherine de Médicis* (La Ferrière, snippets) | Borda 1888 pp.243-244 reprints the c262 passage ("la farce se jouera du costé de delà ... comblés de bien et de mal") **citing Charrière III pp.253-260 note** -- derivative, no new witness; its note lists the editions of Noailles' letters (Ribier, Vertot, Charrière, L. Paris in Cabinet historique XIX-XX, Tamizey in Revue de Gascogne VI, 1865) and says the originals are in the Harlay collection (= fr.16142's fonds), with copies in Béthune, Brienne, Dupuy, Gaignières, Mortemart. Tamizey 1865 is described in the Revue de Gascogne snippet as the Venice-embassy letters; the c262 phrases return no Tamizey hit. Revue de Gascogne 1930 prints a Constantinople letter of 22 Sept 1572 (a different letter). No "chiffre"/"déchiffr" note for A or B in any of these. Borda 1888 grep for "chiffr": only heraldic monograms. |
| (c) documentary editions | Google Books API (key, country=US), 10 queries: the c262 phrases, three phrases from the Dupuy 221R-226R clear copy of B ("liberation du filz de feu Aly Bassa", "les ministres du Roy d'Espagne sont merveilleusement diligens", "des Vignes de Pera" 1574 Acqs), "16142" Noailles chiffre, a déchiffrement query | B: "liberation du fils de feu Aly Bassa" -> only Charrière III (1853, several scans); the other two B phrases -> none / a different letter (22 Sept 1574, Borda 1928). A: Charrière and Borda only. "16142" chiffre and the déchiffrement query: 0 items |
| (d) holding archive / catalogue | BnF fr.16142 record and Dupuy 521 described from NOTES.md (CS-4, RUN1-NX) and the Gallica manifest on disk (`sources/gallica-manifests/btv1b9060927q.json`); the catalogue hit `cataloguemanfran03bibluoft` (BnF *Catalogue des manuscrits français*) surfaced in IA fts for "evesque d'Acqs" chiffre but was not opened | not re-fetched; no catalogue statement of a modern decipherment of these leaves known to this audit |
| (e) full text | IA advancedsearch (3), be-api fts (3: "comblez de biens", "farce se jouera", "evesque d'Acqs" chiffre) | "farce se jouera": Borda 1888 and *Revue de Gascogne* 44 among unrelated drama hits (Revue de Gascogne not opened); "evesque d'Acqs" chiffre: Charrière III and Fréville-era series volumes, *Mélanges* (Documents inédits), the BnF catalogue -- nothing pointing to a decipherment of 1572/1574 leaves |
| (f) solver repositories, cipher blogs, DECODE | Cryptiana `henryiii.htm` and `frencheastern.htm` (copies in `sources/cryptiana/web/`, read 5 Oct 2026); DECODE listings on disk (`sources/decode/records-*-2026-09-24.tsv`, `keys-all-2026-09-28*.tsv`, grep 16142/Noailles/Acqs/Constantinople); Bourdeau/Aymeloglu as VER1-NOX (not re-cloned) | **Tomokiyo (cryptiana henryiii.htm, section "Bishop of Acqs, Ambassador in Constantinople (1571-1574)")**: "His many letters from December 1571 to July 1574 ... used the following cipher (BnF fr.16142, f.109-f.253)", key reconstructed by him from these leaves; frencheastern.htm (posted 15 March 2026) says the same cipher reads BnF fr.15967 ff.167/180 "which I reconstructed from BnF fr.16142". So a modern key recovery of exactly this cipher, from this volume's letters, is published (both A and B fall inside ff.109-253 by date). DECODE: no record for fr.16142 / Noailles / Acqs in the 24-28 Sept listings (live site not re-queried). |
| (g) scholarship | OpenAlex (Bearer, 3 queries), CORE (Bearer, `v3/search/works/`, 2), CrossRef (2), HAL (2), Semantic Scholar (x-api-key, 2 sent: 1 answered, 1 HTTP 429, not retried) | nothing on a decipherment of these letters or this cipher; Persée not queried directly (HAL/CrossRef/OpenAlex cover its DOIs) |
| JSTOR | 2 rows appended for B (family i: "évêque d'Acqs" AND Constantinople AND 1574 AND chiffre; family ii: "merveilleusement diligens"); A's two rows were queued by VER1-NOX | queued; does not block the class |

Requests: www.googleapis.com 14, archive.org 6 (3 advancedsearch, 1 metadata, 2 djvu text of which one HTTP 500 then one 200), be-api.us.archive.org
3, api.openalex.org 3, api.core.ac.uk 2, api.crossref.org 2, api.archives-ouvertes.fr 2, api.semanticscholar.org 2 (one 429). Unreachable:
Semantic Scholar's second query (429); Hammer, Persée direct, the live DECODE site, Revue de Gascogne 44 and Tamizey 1865 page text (not opened).

### 3. Classification
| item | N-class | key source | text | change from Audit 1 |
|---|---|---|---|---|
| A c262 (25 Apr 1572) | **N0** (confirmed) | published (S. Tomokiyo, key reconstructed from fr.16142 ff.109-253; credited) for key.tsv; the basin key is ours and reads no word | known | prior decipherment of this very block confirmed three ways: the period margin gloss on the leaf, the Dupuy 521 clear copy, and Tomokiyo's published key recovery from this run of letters; plaintext printed Charrière III p.258 (1853) and reprinted Borda 1888 p.244 (from Charrière) |
| B c510-516 (7 July 1574) | **N0** (confirmed) | the basin key: ours (learned against Dupuy 521); the published key covers this letter by date (f.109-253, to July 1574) but has not been applied here | known | Dupuy 521 221R-226R is the whole letter in clear; Charrière III pp.551-558 prints extracts (p.551 to the King, p.557 to Catherine) (one Dupuy phrase found there only); Tomokiyo's key covers it |

The attempt to break N0 failed in the direction that matters: nothing suggests either text is unknown; the extra prior work found
(Fréville 1853 on other fr.16142 letters; Tomokiyo's recovery from ff.109-253) strengthens, not weakens, "already deciphered".

### 3a. Depth (rule 4a)
| item | % H/C/S | unread | depth | check | content sentence |
|---|---|---|---|---|---|
| A | 0% (all 384 reader signs graded M; DEF1-NOXG: "gloss words H-source, reading M") | all | **D0** | basin key on reader signs R 0.3506 vs p99 0.2413/0.2496, max 0.2665/0.2749 (DEF1-NOXG, corrected gloss); NOXALIGN S 2 of 41 vs null max 1 (very thin); judge on the basin decode FAIL -2.045 (VER1-NOX, old decode string). Tomokiyo's key on the reconciled signs shows "veullent s'aller promener en Flandre" in line 1 (DEF1-NOXG, used as a check only) -- a known-answer agreement with the gloss, not a graded reading; if a solver later grades it H it would be D1 at most and still N0 | -- (D0) |
| B | 0% (no decode) | all | **D0** | N8-NOX basin S 0.601 vs N1 p99 0.273 / N2 max 0.384, a property of the alignment | -- (D0) |

### 4. Postmortem
No over-claim found in NOTES.md, status.json rows 120-121 or PROGRESS.tsv rows 51-52 ("no reading", "all M", N0 D0 throughout). Corrections:
1. status.json rows 120 (A) still quote the pre-revision R 0.309 / p99 0.283 in `line` and `depth_check`; updated to DEF1-NOXG's 0.3506 with
   the revised nulls (rule 10 propagation). No SECOND-OPINIONS-QUEUE.tsv row exists for this target (N0), so nothing to carry there.
2. Gap in Audit 1 and the folder: neither records that Charrière III credits Fréville (1853) with deciphering other fr.16142 letters, nor
   that Tomokiyo's key was reconstructed *from this volume's letters* (Audit 1 says "publishes the key for exactly this cipher"). Any future
   sentence about an unglossed fr.16142 leaf must first check Fréville's restorations in Charrière III (pp.80-81 note and later notes) as a
   possible prior decipherment, and Tomokiyo's page as a prior key recovery: "undeciphered in the volume" is not safe for fr.16142 leaves.
3. Audit 1's "very probably in the *Bulletin de la Société de Borda* 1888" is confirmed: pp.243-244, quoted from Charrière III.

### 5. Safe and unsafe sentences
- A safe: as Audit 1, with the revised figure: "On BnF fr.16142 (25 April 1572), a key learned from the clear copy of a later letter, mapped
  onto one reader transcription, scores above four shuffled controls against the leaf's own period decipherment (R 0.35 vs 0.27), but reads no
  words (D0); the letter's text was already known from that decipherment, from Dupuy 521 and from Charrière's 1853 edition, and the cipher's
  key was reconstructed by S. Tomokiyo from this volume (N0)."
- A unsafe: "we read / deciphered the 25 April 1572 letter"; "the basin key deciphers c262"; any "new", "first", "previously unread".
- B safe: "For the 7 July 1574 letter (fr.16142 c510-516), an alignment against the Dupuy 521 clear copy learns a consistent key (D0, nothing
  decoded); the letter's text is known from Dupuy 521 and in part from Charrière III, and its cipher is covered by Tomokiyo's published key (N0)."
- B unsafe: "c510-516 is an undeciphered letter"; "the July 1574 letter is decoded"; "an independent key recovery" without naming Tomokiyo's.

### depth_check
`python3 tools/depth_check.py` after updating status.json rows 120-121 (5 Oct 2026, 23:08 UTC), exit 0; both rows D0, N0, under "not counted
D0/D1", no flag:
```
unique solves (N3+ and D2+): 16 -- D4 1, D3 2, D2 13; not counted D0/D1: 13; legacy ungraded: 0
```
PROGRESS.tsv rows 51-52: column `2` = x; `C` stays `.` (N0, D0). No SECOND-OPINIONS-QUEUE.tsv row (N0).
