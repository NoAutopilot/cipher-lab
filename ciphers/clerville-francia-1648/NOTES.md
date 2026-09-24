# clerville-francia-1648

Status: open

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
