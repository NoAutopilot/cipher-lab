# clerville-francia-1648

Status: blocked
No standard edition identified or opened for Este's French embassy of 1648; archive.org full-text search for Clerville+Modena+1648+cifra returned 126 hits, none about an Este dispatch (the on-point one is an engineering study of the chevalier de Clerville, which does not concern this dispatch), and the Mazarin/Este correspondence editions were not located.

## What this is

Single Este-France dispatch filed together with the cipher-table sheet used to write it: "1648, aprile 27, con
il foglio del cifrario impiegata nel dispaccio" ("...with the cipher-table sheet used in the dispatch"),
Archivio Segreto Estense, Cancelleria, Carteggio ambasciatori — Francia, envoy Clerville cav., appendice. The
precise busta/fascicolo could not be extracted from the finding-aid PDF's table (a "Segnatura attuale" column
scrambled by `pdftotext -layout` against a repeating "APPENDICE" watermark column — flagged by the 24 Sept scout
for a PDF-table-aware re-extraction). QUEUE.md row IR5 (LANE N scout IT3 of 24 Sept 2026); source PDF
`ASE_Cancelleria_ambasciatori_francia_rev.pdf`, ASMo/Este archive.

Same-unit and key-with-letter are both stated directly by the finding aid ("con il foglio del cifrario impiegata
nel dispaccio" is explicit: the key sheet actually used for this dispatch is catalogued with it) — this is
CLAUDE.md/LESSONS.md's strongest pattern, "the key was in the archive beside the letter". `ciphertext.txt` is not
created; no image has been seen.

## Check-solved sweep, 24 September 2026

1. **Web.** WebSearch `"Clerville" Francia ambasciatore estense 1648 cifrario dispaccio Modena` and
   `"chevalier de Clerville" Modena Este ambasciatore Francia 1648`. Hits: the ASMo Spagna-fondo PDF, a
   Comune di Modena "Lettere e cifrari nell'Archivio di Stato" educational-visit page (fetched directly, see
   below), and Wikipedia/AFGC pages for Louis Nicolas de Clerville (1610-1677), Louis XIV's premier commissaire
   général des fortifications, active in France through the 1648 period — no source connects him, or any
   other Clerville, to the Este embassy at the French court, so it is not established whether "cav. Clerville"
   is this same engineer serving as an informal Este agent, or an unrelated, unidentified envoy. Not found.
2. **WebFetch** of the Comune di Modena page: general educational-programme text about ciphers "adopted in the
   past, in particular by the Este family"; no specific envoy names, dates or shelfmarks. Not a match.
3. **Print.** No printed Este-France diplomatic edition for 1648 located this pass. Not confirmed absent at
   verifier level.
4. **Lists.** `sources/cryptiana/` grepped locally for `clerville`: no hits.
5. **DECODE.** `sources/decode/records-non-decrypted-2026-09-24.tsv` grepped for `clerville|francia`: no
   matching envoy/shelfmark (the file's Modena rows are all Amb. Ung./Carteggio Principi Esteri, a different
   fondo). Live de-crypt.org not queried.
6. **Bourdeau/Aymeloglu.** Fresh shallow clones, `grep -ril "Clerville"` across both trees: 0 hits.

## Verdict

**Open.** No source located a solution, key, plaintext or documented attempt for this item. This is the strongest
"key beside the letter" candidate in the batch by the finding aid's own wording, but it is also the smallest
(one dispatch) and its shelfmark is still unresolved from the PDF — a worker with a PDF-table-aware extraction
of `ASE_Cancelleria_ambasciatori_francia_rev.pdf` page 67 (or the ASMo online viewer, if the France fondo has
one) should pin the busta/fascicolo before ordering a copy.

Copy-order (busta/fascicolo not yet resolved — see above). REQUEST.md below gives what can be specified without
it.

Requests this pass: WebSearch 2, WebFetch 1 (mymemo.comune.modena.it), github.com 0 (reused shared clones). No
SIAS, no Google Books, no DECODE login, no promotion, no decoding.


## Web and blog check (CS-A2-C, 2 Oct 2026)

WebSearch queries (standard) and what they returned:
- Clerville cavaliere ambasciatore estense Francia 1648 cifrario dispaccio decifrato (structurae and Clerville biography pages, HistoCrypt Louis XIV pieces; none connects Clerville to the Este post)

Blogs: Cipherbrain, Cryptiana blog and Cipher Mysteries were covered by the restricted web searches above and a local grep of `sources/cryptiana` and `sources/ciphermysteries`; 0 hits for the sender, recipient or shelfmark; no comment thread opened because no hit was relevant.

archive.org full-text (be-api, one request at a time, 2 s apart, unquoted-token behaviour so counts are upper bounds):
- Clerville Modena 1648 cifra (126 hits, none about the dispatch)

Solver repositories (shallow clones, grep only, 2 Oct 2026): clerville: 0 / 0 in both solver repos; 0 in sources/decode, sources/cryptiana. Aymeloglu cited, no code used.

DECODE: local grep of sources/decode (records-non-decrypted 24 Sept 2026 and later key lists) for the sender/recipient names: 0 rows; the 2 Oct 2026 login-free crawl (801 rows) by CS-A2-B is the same list. Live de-crypt.org not queried by this worker.

## Premise check (CS-A2-C, 2 Oct 2026)

- (a) found, unread: the folder says the cipher-table sheet used for the dispatch is filed with it ("con il foglio del cifrario"): a key beside the letter, not a decipherment; no image to open.
- (b) not found: no Clerville file in either solver repo.
- (c) unreachable: no image; busta/fascicolo unresolved (PDF table extraction).
- (d) not found/unreachable: no French-side edition (Mazarin letters, Recueil des instructions) identified; a Gallica/IA search of the 27 April 1648 date with Este envoy names is the next step.

Verdict: blocked. No solution, key, plaintext or documented attempt was found in anything searched, but no edition could be opened, so this is a search result for the log and not a statement that none exists. Status was `open` before this pass and failed the intake gate.

## fr17 re-judge (FR17-RJ2, 3 Oct 2026)

No reading on disk -- no ciphertext or reading: status blocked (REQUEST.md). No judge run (fr16 or fr17), no shuffled-decode control, no per-fold rate at a reading's N; the fr17 per-fold rates at N=138/300 are in tools/data/fr17/README.md.

## While waiting (RUN4-WAITBF, 4 Oct 2026)

- Action that depends on nobody: the step this folder's own pass (d) names -- a Gallica (SRU/ContentSearch) and archive.org full-text search of the 27 April 1648 date with the Este envoy's names in the French-side editions (Cheruel's Lettres du cardinal Mazarin, Recueil des instructions), ~$1 (estimate).


## Edition search: 27 April 1648 and the Este envoy's names (D2-CLERV, 06 Oct 2026 00:00 UTC)

Search results only (rule 10); not a novelty verdict. Status stays blocked (no image, no shelfmark; REQUEST.md unchanged).

**Opened:** Cheruel, *Lettres du cardinal Mazarin pendant son ministere*, t. III (Jan 1648-Dec 1650), IA , full  read by script (OCR is rough). Its chronological table of analysed letters for 27 Apr 1648 lists one letter (Paris, Mazarin to Plessis-Praslin: fall of Guise at Naples, Prince Thomas to command the fleet, marquis Ville's diversion in Piedmont; "Imprime dans l'Histoire des revolutions de Naples, par le comte de Modene"). 28 Apr: Portugal; 30 Apr: letters including one "Au duc de Modene" (Cheruel's table, same volume; not read in full). No Este dispatch of 27 Apr 1648 and no cipher mention in the volume for that date.
**Names found in print (leads, not matches):** (1) Cheruel t. III, Feb 1648 analysis: "le marquis Calcagnini (envoye du duc de Modene)", who returns to the Duke and is to brief d'Estrades; 100,000 francs to be paid to the Duke through him. That is a printed Este envoy at the French side in early 1648; the finding aid's "Clerville cav." is not matched to him or to anyone. (2) The chevalier de Clerville (Nicolas, 1610-1677, engineer) appears in the same volume as an engineer under Mazarin's orders (1649-50, and a 1650 note that he was to go to Piedmont for the next campaign, with d'Estrades, under the Duke of Modena and Plessis-Praslin); nothing there makes him an Este envoy. (3) Balthazar, French intendant sent to the Duke (Mar 1648). Whether the archive's "cav. Clerville" is that engineer remains unestablished.
**IA full text (be-api fts, unquoted tokens so counts are upper bounds):** "Clerville Modene 1648" 810; "Clerville" "duc de Modene" 498; Clerville Modene ambassadeur 1648 chiffre 569; "27 avril 1648" Modene Mazarin 55; Italian queries (Clerville Este Francia 1648 dispaccio cifra 15; Clerville Francesco I Este ambasciatore 27). Top hits are Cheruel t. III/VIII/IX, Colbert's Lettres (Clerville as engineer, 1662-63), Memoires du comte de Modene, Inventaire sommaire (Affaires etrangeres), Bourelly *Cromwell et Mazarin*; none read for a 1648 Este dispatch with a cipher sheet. Not opened beyond snippets: t. VIII (, Clerville in a 1650s letter) and the Cheruel t. II/IX volumes.
**Gallica SRU** (catalogue-level counts only; no full text opened): Calcagnini+Mazarin+Modene 168 (incl. Cheruel t. 2, Du Plessis-Besancon memoirs); chevalier de Clerville+Modene 613; Clerville+Este+1648 1024 (incl. BnF Recueil de lettres et memoires 1648-1665); Calcagnini+ambassadeur+Modene+1648 120. Titles only; hits are not shown to concern an Este dispatch.
**Not found:** any printed or catalogued mention of a 27 Apr 1648 Este dispatch from Clerville, its cipher sheet, or a decipherment. **Not searched:** Italian-side editions (Modena archive publications, Calcagnini correspondence), Gallica ContentSearch inside Cheruel/Memoires de Du Plessis-Besancon, the Memoires du comte de Modene text.
Requests: archive.org be-api 13, archive.org download 1, gallica SRU 5; all 200, 2 s apart.

## While waiting (D2-CLERV, update)

- Done: the French-side edition pass (Cheruel t. III, 27 Apr 1648). Next, no outside dependency: Gallica ContentSearch/IA fts of the Memoires de Du Plessis-Besancon and Cheruel t. II for "Calcagnini", then the ASMo finding aid with the name Calcagnini in case the "appendice" lists him (~USD 1).
