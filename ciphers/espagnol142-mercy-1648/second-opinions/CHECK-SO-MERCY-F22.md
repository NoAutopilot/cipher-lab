# Citation check: SO-MERCY-F22 (PR 16, chatgpt-2026-09-26.md)

Verifier: V8-SO16 (Sonnet, session_011VT63hJtoLER8ZHuMKvK6X), 26 Sept 2026, from 05:10 UTC (`date -u`). Parent: LANE V8
(session_01YRuw3TCf7d1w85DLmYNnw4). Brief: `.claude/briefs/runs/2026-09-26-lane-v8-so16.md`. Method:
`.claude/briefs/verifier.md` "Second opinions from outside models". Did not decode, did not touch key.tsv,
corrections.tsv, ciphertext.tsv or reading.txt. Did not merge, close or comment on PR 16.

## Claims table

| # | Claim (PR file) | Source checked | Verdict | Note |
|---|---|---|---|---|
| 1 | Morel-Fatio, *Catalogue des manuscrits espagnols et des manuscrits portugais* (1892), item 11, tome III, fols 22-22v, "Autre instruction chiffrée pour le même. Barneton, 6 juin 1648. Copie." | IA `cataloguedesmanu00bibl_0` reachable (be-api fts: "Barneton" present); full text of item 11 already read verbatim by AUDIT.md S2.2 row 2 (pp.133-135) | **confirmed** (page cited as 135 vs AUDIT's "pp.133-135" is a page-span nuance, not a discrepancy) | No decipherment noted at that entry -- matches the existing AUDIT.md negative, no new information |
| 2 | Cousin, *Madame de Chevreuse*, 7e éd., Paris, Perrin, 1886, pp.525-531; prints P. Ernest de Mercy's 27 Sept 1647 memoir; p.531 asks for a confidant "tant pour l'aider aux chiffres et choses de correspondance" | fetched gutenberg.org/files/52011/52011-h/52011-h.htm (HTTP 200); title page reads "SEPTIÈME ÉDITION ... PARIS ... PERRIN ET CIE ... 1886"; memoir runs pp.526-531, signed "P. Ernest de Mercy" at the close; p.531 text found verbatim: "...un qui soit confident et bien connu des ministres de S. A., tant pour l'aider aux chiffres et choses de correspondance..." | **confirmed**, edition/pages/quote all match | New detail beyond AUDIT.md (which cited this appendix but not the p.531 cipher-assistant line); does not print or paraphrase the 6 June 1648 instruction itself, so does not move the class |
| 3 | Cuvelier-Lefèvre VI (1937) p.647 nos.1498-1499; no.1499 is a June 1648 Peñaranda-to-Philip IV letter on Brun/Schwarzenberg's cipher and Mercy-Chevreuse | already established, AUDIT.md S2.2 row 1 | **confirmed** (matches the repo's own prior finding; PR correctly does not re-verify, flags it as the repo's own advance) | No new claim to check |
| 4 | Lonchay 1896 p.445 n.2: Brussels SEE t.LXIV f.16 (15 April instructions) and t.LXV f.181 (30 Aug dispatch) | already established, AUDIT.md section 4 row (b) | **confirmed** (repo's own prior finding, correctly cited) | No new claim |
| 5 | DECODE records 958-965, "Brussels secretariat chiffres 1647-98", unverified key candidates | already established, AUDIT.md key-source paragraph | **confirmed as an accurate restatement** of the repo's own lead, correctly labelled "unverified key candidates" | No new claim |
| 6 | Vignal Souleyreau, richelieuletters.hypotheses.org/114692, Pierre Ernest de Mercy = "sommelier de courtine" for Leopold Wilhelm | fetched (HTTP 200); page confirms office "sommelier de courtine"13 for "l'archiduc Léopold-Guillaume de Habsbourg"; page carries "Mise à jour du 3 août 2026" and citation DOI 10.58079/16lwn | **confirmed**, including the update date the PR said it could not establish (page states it plainly) | PR's "unverified here, ... date not independently established" is over-cautious, not wrong -- it is a hedge, not an invented fact |
| 7 | Hüttl, "Luise Henriette, Kurfürstin von Brandenburg...", *Neue Deutsche Biographie* 15 (1987), pp.499-500; electoral couple's extended Kleve residence runs to June 1648 | fetched deutsche-biographie.de/downloadPDF?url=sfz55091.pdf (HTTP 200, 7pp PDF); text: "Während eines längeren Aufenthaltes des Kurfürstenpaares in Kleve bis Juni 1648 ..."; citation footer: "Ludwig Hüttl, ... in: Neue Deutsche Biographie 15 (1987), S. 499 f." | **confirmed**, author/volume/year/pages/content all match exactly | New citation, not previously in AUDIT.md; correctly used only as background plausibility, not as evidence identifying Mercy's mission or restoring CLEUES |
| 8 | Internal: committed reading is 522 tokens (S496/M26), not the prompt's 521; 38 key rows = 36 numeric + 2 mark categories; 522 - 3 mark occurrences (2 box, 1 frac) = 519 numeral-sign tokens | `reading_tokens.tsv` (522 data rows: 496 S, 26 M grades), `key.tsv` (38 rows, tail 2 rows are `[MARK:box]`/`[MARK:frac]`), grep for non-numeric sign column (2 box occurrences r07/r09, 1 frac occurrence v01) | **confirmed exactly** against the files on disk | Internal, no host request |
| 9 | Internal: ELEUES (not CLEUES) is the current reading at r14:7; `exceptions.tsv`/`corrections.tsv` still carry stale "five exceptions"/"Cleues" language although NOTES.md's own table shows the count dropped to two (r06, r17) after R7-MREV | `exceptions.tsv` line 2, `corrections.tsv` lines 2/7/8, `NOTES.md` lines 745-763 | **confirmed exactly** | Internal, no host request; correctly describes the post-audit reading change already logged in AUDIT.md's final section |

## Access-gap statements (not citations, not checked as claims)

The PR's own reported failures -- APW search endpoint, Google Books "search within this book", BnF finding aid,
"search-within" on the Cuvelier-Lefèvre VI Google Books record -- are consistent with AUDIT.md's own record of the
same hosts (APW returns HTTP 505; BnF finding-aid pagination is browser-only) and were not independently re-tried
here per the brief (citation check, not a fresh sweep).

## Verdict: **merge**

Every factual claim and citation checked traces to a real source that says what the PR says it says. The two new
citations (Cousin p.531's cipher-assistant sentence; Hüttl's NDB entry) are accurate and add real, if peripheral,
context; neither is invented. The PR is unusually careful about labelling what it did not verify ("unverified here",
"unverified independently here") rather than asserting it. Its internal corrections (token/grade counts, the stale
Cleues/five-exceptions language) are also exactly right against the files on disk. No confirmed lead prints or
deciphers the 6 June 1648 instruction itself, and none names a period key with matching values -- **no confirmed
lead moves the N3 class in AUDIT.md.** Unconfirmed items (marked "unverified"/"unreachable" by the PR itself): APW,
Google Books search-within on two records, BnF finding-aid pagination, richelieuletters full independent read (only
spot-checked here), DECODE 958-965 folio contents. These stay open leads, not confirmed prints.

## Counts

Confirmed: 9 (7 external citations/leads + 2 internal file-based claims covering 5 sub-counts). Not confirmed
(PR's own admitted access gaps, not independently re-tried): 4 (APW, Google Books search-within x2, BnF finding
aid). Unreachable: 0 (every host this session tried answered). No JSTOR-only leads to queue.

## Requests (this session)

archive.org/be-api.us.archive.org 1 (fts, cataloguedesmanu00bibl_0); gutenberg.org 2 (HEAD + GET);
deutsche-biographie.de 2 (HEAD + GET); richelieuletters.hypotheses.org 1. All >=1.5 s apart, one host at a time.
No key used, none printed.
