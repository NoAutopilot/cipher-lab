open
Bergenroth, *Calendar of Letters, Despatches, and State Papers ... Simancas*, vol. I (1862, 1485-1509, archive.org `dli.ministry.01111`) and its *Supplement to Volumes I and II* (1868, archive.org `dli.ministry.03718`) read in full text (both volumes' `_djvu.txt` fetched to disk and grepped whole, not sampled) for "Messina"/"Mesina", "Sicily", "viceroy", and "1503": no calendar entry for this letter or for any 27 April 1503 dispatch from Sicily in either volume (both volumes calendar England-Spain diplomatic correspondence, chiefly the Puebla/Estrada embassy and the Katharine/Juana marriage papers, not the Sicilian viceroyalty's internal correspondence, so the absence is unsurprising but is a real negative on the two volumes actually searched).

# BnF Espagnol 318, item 94: the viceroy of Sicily to Ferdinand, Messina, 27 April 1503

Target as set by job NX-E318 (LANE NX, 26 Sept 2026): BnF Espagnol 318 (Gallica ark `btv1b52503046q`), item 94,
"Lettre en chiffre du vice-roi de Sicile au Roi Catholique," Messina, 27 April 1503, about four pages, folios
120r-121v (canvases 452-455 per Bourdeau's `lab2canvas.json`).

## Check-solved, six sources + web, 26 Sept 2026

Order per `.claude/briefs/check-solved.md` and job NX-E318 step 1.

**(a) dbourdeau/cyphersolver, shallow clone, commit `fc0c9e865d0fae67ca92d19750d2b09ab11972e0` (dated 25 Sept 2026
by its own git log, fetched 26 Sept 2026).** His `esp318/` folder is an active, detailed working file
(`esp318/NOTES.md`, 24 KB) covering all five ciphered letters in the volume (nos. 5, 92, 93, 94, 95). His own
table (line 35): "94 | 120-121v | 452-455 | The viceroy of Sicily to Ferdinand, Messina, 27 Apr 1503. Spanish,
clear and cipher mixed, four pages | unidentified; RRCC architecture, code initials g/l/m/n/p/r/v/z | **open**."
His text states in full (lines 20, 39-40): "Nos. 93 and 94 remain unread" and "There is no decipherment anywhere
in the volume for nos. 93, 94 or 95." His "Remaining gaps" section (line 275): "No. 94 (ff. 120r-121v), whole
letter - blocker: not-attempted; never transcribed; Bergenroth's Gran-cifra list not tested against it." His
"Next step, in order" section names transcribing no. 94 as step 1 of his own plan, with Bergenroth's *Gran cifra*
(BNE MSS 20.211/52, re-found by the CNI in 2018, photographs in his `esp318/lit/berg/`) as the suspected key, and
the unpublished "Cifra del visorrey" (BRAH 9/15 ff. 1-6, described but not reproduced by Galende Díaz 1994) as a
second, untested candidate specific to a viceroy's letter. **He does not hold a reading of item 94** -- no
decipherment, no transcription -- so job NX-E318's stop condition ("if Bourdeau holds a reading of item 94, stop
at step 1 and flag it") is not triggered on the letter of the rule. But this is a live, active duplicate-effort
risk (flagged already by SCOUT-OWN-2026-09-26.md before this job started): his folder already holds full-page
images of ff. 120r/120v/121r/121v (`esp318/full/f12{0,1}{r,v}.jpg`), the folio-to-canvas map, the code-initial
architecture analysis, and both key candidates. See "Flag" below.

**(b) aaymeloglu/unsolved-ciphers, shallow clone, commit `2495c45e8b94ffbc4f09a085224aa5ebce5cdf9f` (dated 23
Sept 2026).** Grepped the whole repository (`.md`, `.txt`, `.json`) for `318`, `Sicil`, `Messina`, `1503`: no
genuine hit. The only `318`/`1503` matches are unrelated numeric substrings inside other targets' data files
(`starhemberg-1758` cipher codes containing the digits 318/1503, a folio range `f. 313-318` in an unrelated BRAH
manuscript). This repository does not treat BnF Espagnol 318 at all.

**(c) Tomokiyo on disk, `sources/cryptiana/web/spanish.htm`.** States, under "Unidentified Ciphers ... BnF
Espagnol 318 (Gallica) includes, in addition to the two mentioned above, the following letters in cipher,
undeciphered": "f.120-121, no.94 Viceroy of Sicily to Ferdinand, 27 April 1503." Independent confirmation that as
of this snapshot Tomokiyo lists item 94 as undeciphered; no reading, no key given for it (his page's only
decipherment claim for this volume is Lasry's 2022 "approximate" key for item 95, a different item).

**(d) Standard edition -- read by this worker.** Bergenroth's *Calendar*, vol. I (1485-1509) and its *Supplement
to Vols I and II*: full text fetched and grepped as above (line 2). No entry. These are the standard English-
language calendars for this correspondence series and this is the search this worker itself ran, not a quote of
someone else's.

**(e) DECODE snapshot on disk**, `sources/decode/records-{decrypted,non-decrypted}-2026-09-24*.tsv`. Grepped for
`318`, `Sicil`, `Messina`, `Espagnol`: no BnF Espagnol 318 record of any kind; the only `318` hits are an
unrelated BRAH folio range (9/28 f. 313-318) and BL Sloane MS **3188** (substring match on "318", not this
manuscript).

**(f) Web search**, `"Espagnol 318" Sicile 1503 chiffre Messine vice-roi` and `"viceroy of Sicily" Messina 1503
cipher deciphered Ferdinand`. Top hits are BnF's own catalogue page (`archivesetmanuscrits.bnf.fr/ark:/12148/
cc349255`, the finding aid for Espagnol 318 itself, no decipherment claimed there) and general Sicilian-viceroy
reference pages (Wikipedia lists of viceroys, unrelated). No solve announcement, no Vals-AI/model-solve post, no
scholarly treatment of this specific letter found. One incidental find: `github.com/arya1515/cyphersolver`
(commit `52719204a24cf5c3debf1959567bba4cf7911412`, dated 19 Sept 2026) is an earlier snapshot of the same
`dbourdeau/cyphersolver` folder structure (same `esp318/` layout, same file names) -- not an independent
research effort, just an older copy/fork under a different account name; not counted as a seventh source.

## Verdict: open

No decipherment or transcription of item 94 exists in any of the six sources plus web search. Per rule 10, this
is a search result, not evidence of absence beyond what was checked -- BRAH 9/15 (the unpublished "Cifra del
visorrey") and BNE MSS 20.211/52 (Bergenroth's Gran-cifra manuscript) were not searched for a prior decipherment
of this specific letter (not sources this worker could open from the cloud; Bourdeau's folder has photographs of
the latter only).

## Flag: duplicate-effort risk with Bourdeau's live folder (for the LANE NX orchestrator)

Per job NX-E318's own rule 10 clause, this is not a stop condition (no reading exists to stop on), but the
overlap is total: Bourdeau's own "Next step 1" is "Transcribe no. 94, ff. 120r-121v. It is the better of the two
open targets" -- the identical target this lane just opened, with the identical Bergenroth Gran-cifra hypothesis
already named in his notes as the test to run first. His folder is the more advanced position: he already holds
full-page images of all four leaves, a folio/canvas map, and a code-initial architecture read (RRCC-style
homophonic alphabet + CVC nomenclator groups `gag rah mnb mms nob gik luy mei nen mok pol pat par paq vaz mal nyb
nyl gob gib lob moe nak rag lue`). SCOUT-OWN-2026-09-26.md flagged this exact risk before the job was briefed
("esp318 item 94 (Bergenroth Gran-cifra key untested, duplicate-effort risk vs Bourdeau live folder)"). Recommend
the orchestrator weigh this against the other four NX targets before committing a transcription/key-application
campaign here, since a public repository (MIT/CC BY 4.0, citable per CLAUDE.md item 8) is already working the
same letter with the same key hypothesis and a head start on the images.

## Intake gate

```
$ python3 tools/intake_gate_check.py esp318-sicilia-1503
esp318-sicilia-1503: open (line 1) -- edition/page or full-text-search citation found within 6 lines
```
Exit 0. Gate passed; proceeding to the image step.

## Image step (job NX-E318 step 2), 26 Sept 2026

Folio-canvas map placed independently of Bourdeau's `lab2canvas.json`, same answer:
```
$ python3 tools/gallica_folio.py btv1b52503046q --folio 120 --side r --json
```
confirms `[213, 452, 455, "120r", "121v"]` -- ff.120r-121v = canvases 452-455, offset k=213 in a run that is
internally consistent from f.118 through f.127 (k=211..226), i.e. item 94's four leaves sit in one of the
manuscript's cleanly-numbered stretches, not a jump or gap.

Line crops, one page (f.120r, canvas 452) as the sample, per the mandatory crop step:
```
$ python3 tools/iiif_lines.py --ark btv1b52503046q --canvas 452 --out ciphers/esp318-sicilia-1503/images --prefix f120r --dry-run
  -> region 4141x5359, 33 lines, pitch 99
$ python3 tools/iiif_lines.py --ark btv1b52503046q --canvas 452 --out ciphers/esp318-sicilia-1503/images --prefix f120r --debug
  -> wrote 66 crops (33 bands x 2 segments) and images/manifest.json
```
`f120r_lines_debug.jpg` checked by eye: the 33 detected bands track the manuscript's ruled lines correctly across
the page, including the two-line superscription at the top ("Muy alto y muy poderoso y catholico principe Rey y
señor") and the body text below it; band edges fall in interlinear whitespace with only minor drift near the
foot of the page (the hand's baseline wanders slightly, not a detection fault). No other canvases (453-455)
cropped in this job -- one sample page is enough for the image step; the next job cuts the remaining three.
Folder size after this step: 6.9 MB (well under the 30 MB budget), 67 files (66 crops + 1 debug overlay + 1
cached full-page source).

**Sign inventory, from one sample crop (`f120r_L04_s1.jpg`, one full manuscript line).** The line reads (left to
right): a raised numeral-like sign with a tilde/bar above it; a two-letter cluster resembling "ao"; a dash-like
separator stroke; a letter with a superscript roman-numeral-style flourish (resembling "iii"); the plain Spanish
word "pat" or similar; a barred abbreviation mark over a two-letter cluster; a dash; a three-character cluster
combining a letter and two digit-like signs; a raised-bar mark over a letter; a doubled-long-s ("ff") ligature
followed by two digit-like signs; another "ff" ligature followed by a digit and a combining tilde; a dash; and
the plain Spanish word "mas" ("más") in clear, followed by a large flourished sign (loop over a stroke,
resembling a figure-8 or delta). This matches Bourdeau's own description of the architecture exactly: single
invented symbols (the tilde-numeral, the barred abbreviation marks, the "ff" ligature, the terminal flourish) for
letters or nulls, interleaved with short (2-4 character) alphanumeric-looking nomenclator groups, with plain
Spanish words dropping into clear mid-line (here "mas") -- the same clear/cipher mixture the catalogue entry and
Bourdeau's table both describe for this four-page letter. Rough group count on this one line: about 6-7 discrete
cipher groups/symbols plus 2 clear words; a full-page estimate (33 lines at a similar density) would put the
letter in the same few-hundred-group range as Bourdeau's counts for nos. 92/93. This is a look-and-report only,
per the brief -- no transcription, no group-by-group reading, and no attempt to test the Bergenroth or "Cifra del
visorrey" candidates against it in this job.

## Key candidate (job NX-E318 step 3)

Bergenroth's *Gran cifra* of the Gran Capitán, 1501-1504: manuscript BNE MSS 20.211/52, re-found by the CNI
(Centro Nacional de Inteligencia) in 2018 per A. Quirantes, *El CNI y el (no tan secreto) código del Gran
Capitán* (2018). Not on Gallica or archive.org; Bourdeau holds photographs of it in his `cyphersolver` repository
at `esp318/lit/berg/jbc.bj.uj.edu.pl.NDIGORP0177{56,59,63,64,65,66,67,68,69,72,76}.txt` (these are OCR/text
extractions of the 12-volume *Documentos del Archivo General de Simancas de Gustav Bergenroth* digitised by the
Jagiellonian Digital Library, `jbc.bj.uj.edu.pl`, 1869 imprint, also independently findable there: search
`creator:Bergenroth` on archive.org turns up the same 12 volumes as `jbc.bj.uj.edu.pl.NDIGORP017{556,556..776}`,
confirmed 26 Sept 2026, so this key source does not depend on Bourdeau's repository and can be re-fetched
directly from archive.org if needed). A second, untested candidate specific to a viceroy's letter: the
unpublished "Cifra del visorrey" (BRAH 9/15, ff. 1-6), described but not reproduced by J.C. Galende Díaz (1994);
not accessible from the cloud (BRAH's own site is Anubis-challenged, per CLAUDE.md's host table). Key source
grade if used: `published` (Bergenroth's 19th-century reconstruction printed as an appendix to his own edition;
"ours" only if a fresh key is built from the manuscript photographs, since nobody has yet demonstrated it against
this specific letter).

## Hosts (this job, total)

archive.org: 6 requests (2 advancedsearch, 2 metadata, 2 download), 1.5s+ apart, no logins. gallica.bnf.fr: 2
requests (1 manifest fetch via `gallica_folio.py`, cached; 1 native-image fetch via `iiif_lines.py`, cached), one
retry after a connection reset on the first manifest fetch, both with a browser-style User-Agent, no
403/429/challenge otherwise. Web search: 2 queries (Claude's built-in search tool, not a direct host fetch).
github.com: 3 shallow clones (dbourdeau/cyphersolver, aaymeloglu/unsolved-ciphers, arya1515/cyphersolver), not
rate-limited hosts under the good-citizen rule (git protocol, not HTTP scraping).

## Positive control on the Bergenroth search (LANE NX orchestrator, 26 Sept 2026, 10:20 UTC; answers V9-QA9 finding 1)

Re-fetched both `_djvu.txt` files from archive.org (4 requests, 2 s apart). Gotcha: the files' own names contain a
literal `%20`/`%28`, so the download URL must encode the `%` itself (`938.111%2520C%252016%2528 23%2529_djvu.txt`
without the space); a naive URL returns a 146-byte nginx 404 page that greps as "zero hits" for every term -- check
the file size before trusting a zero. Counts in the real files (case-insensitive `grep -c`, lines):

| Term | vol. I (`dli.ministry.01111`, 1,642,046 bytes) | Supplement (`dli.ministry.03718`, 1,550,697 bytes) |
|---|---|---|
| Ferdinand (positive control) | 846 | 194 |
| Sicily | 19 | 2 |
| Viceroy | 2 | 6 |
| 1503 | 60 | 1 |
| Messina / Mesina | 0 / 0 | 0 / 0 |

Every Sicily and Viceroy hit was read in context: none is a letter from the viceroy of Sicily or from Messina (the
viceroy hits are Columbus and the Castilian governors/viceroys of 1506-1520); the April 1503 hits are Isabella's and
Ferdinand's despatches to the Duke de Estrada (England). The search surfaces text when present, and the verdict
`open` stands on a controlled search. Rule 10: search result only.

## Solver-repo check (bourdeau, 2 Oct 2026)

Fresh shallow clone of github.com/dbourdeau/cyphersolver, HEAD 34e0fc89 (1 Oct 2026), diffed against this folder on 2 Oct 2026 (worker SOLVERDIFF-BOURDEAU, sources/solver-diffs/2026-10-02-bourdeau.tsv). Match class b (they attempted it and closed or explained it).
- Their page: https://github.com/dbourdeau/cyphersolver/blob/main/targets/esp318/NOTES.md ; https://dbourdeau.github.io/cyphersolver/esp318.html
- Their extent, in their words: no. 94 (ours) unread: "nos. 93 and 94 remain unread"; nos. 92 and 95 read; known-keys, key-rebuild and retry steps open
- Their date: 17-21 Sept 2026
- Note: already cited in our NOTES.md
Credit: D. Bourdeau, cyphersolver (code MIT, text CC BY 4.0). Status line unchanged; the parent decides any status change from the ROOM flag.

## Web and blog check (WEBCHECK-esp318-sicilia-1503, 2 Oct 2026)

Required step of `.claude/briefs/check-solved.md` ("Open web and blog comment threads", CHECK-SOLVED-WEB, 28 Sept 2026),
run 2 Oct 2026 01:05-01:10 UTC (clock read) per `.claude/briefs/runs/2026-10-01-account4-webcheck.md`. Target: BnF
Espagnol 318 item 94, ff.120r-121v, the viceroy of Sicily to Ferdinand, Messina, 27 April 1503. Every query and every
hit opened is listed; "no hit" means no result about this letter, not an empty result page.

**(a) Plain web searches (built-in search tool; it ignores `site:` operators, so the blog site-searches in (b) were run
through each blog's own search page instead).**

| # | Query | Result for this letter |
|---|---|---|
| 1 | `viceroy of Sicily Ferdinand Messina 27 April 1503 cipher letter` (sender + recipient + date) | no hit: Wikipedia viceroy lists (Lanuza, Cardona, Moncada), an academia.edu paper on Juan de Vega 1551-52, CSP Spain vol. 6 index -- none about this letter |
| 2 | `"Espagnol 318" cifra OR chiffre OR cipher Sicile 1503` (shelfmark + cipher word) | one relevant hit, opened: the BnF finding aid itself, `archivesetmanuscrits.bnf.fr/ark:/12148/cc349255/cd0e103`, which lists item 94 as "Lettre en chiffre du vice-roi de Sicile au Roi Catholique", Messine, 27 avril 1503 -- a catalogue entry, no decipherment claimed; the rest are French-Spanish dictionary pages for "chiffre" |
| 3 | `"vice-roi de Sicile" "Roi Catholique" chiffre Messine 1503` (French, the finding aid's language) | no hit: viceroy lists and general Sicily pages |
| 4 | `"Viceroy of Sicily to Ferdinand" 1503 undeciphered OR deciphered OR solved` (Tomokiyo's own wording of the item) | no hit: viceroy lists only |
| 5 | `"Lettre en chiffre du vice-roi de Sicile au Roi Catholique"` (the folder's own descriptive title, quoted) | the same BnF finding aid as query 2; nothing else about this letter |
| 6 | `"virrey de Sicilia" 1503 cifra Mesina "Rey Católico" carta cifrada Lanuza` (Spanish) | no hit: viceroyalty institutional papers (1665-75), Lanuza's Wikipedia page, a Palermo imprint bibliography |
| 7 | `"Fernando de Andrada" Benavides Carvajal 1503 Mesina OR Messina galea nao virrey Sicilia` (names from the letter's own clear-text passages, as quoted in Bourdeau's `targets/esp318/NOTES.md`: "donde llegó don Fernando de Andrada y Benavides y Carvajal") | no hit about this letter; Prescott's *Ferdinand and Isabella* (public-library.uk ebook) names Andrada, Cardona and Benavides at Seminara, 21 April 1503 -- historical context for the clear text, not a reading of the cipher |
| 8 | `"passar esta nao" OR "passamos en anocheçiendo" OR "en lo de la hazienda luego" 1503` (the most distinctive clear-text phrases, quoted exactly; the folder holds no transcription or decoded text of its own, so the clear-text excerpts in Bourdeau's notes are the only quotable phrases) | no hit: RAE dictionary entry for "anochecer", Mexican haciendas, unrelated modern pages |
| 9 | `"Espagnol 318" cipher solves Claude OR GPT OR "AI" 1503 Sicily` (model-solve announcements, check-solved.md's "solves" + "Claude"/"GPT" query) | no hit for this letter: the Sept 2026 "Claude solves a 370-year-old cipher" coverage (Schneier, 36kr, kucoin, blockchain.news) concerns a 1650s item, not Espagnol 318; Bourdeau's index page `dbourdeau.github.io/cyphersolver/index.html` and a fork `github.com/setsunaatto/cyphersolver` surfaced -- both opened under (c) |
| 10 | `cyphersolver esp318 "no. 94" OR "item 94" viceroy Sicily transcription decipherment` | no hit: the "item 94" matches are Bourdeau PR #9 (fr. 3977 no. 96, Nevers 1589) and the arya1515 fork already logged above; neither concerns this letter |
| 11 | `"Gran Capitán" cifra 1503 Sicilia virrey carta cifrada descifrada Mesina Fernando el Católico Bergenroth` (the suspected key family) | one plausible hit, opened under (c): *El Debate*, "El Gran Capitán y Fernando el Católico, cartas secretas descifradas ahora" (15 Feb 2018, José Luis Orella) on the CNI's 2018 decipherment of four 1502-03 Ferdinand/Gran Capitán letters -- no mention of Sicily, Messina, a viceroy, the BnF or Espagnol 318; the letters are the AGS/BNE Gran Capitán correspondence, not this one |

**(b) Site searches of the three blogs, each through the blog's own search page (one request at a time, >= 1.5 s
apart; no 403/429/challenge on any host).**

- **Cipherbrain** (`scienceblogs.de/klausis-krypto-kolumne/?s=...`): `Espagnol 318` -> "Wir konnten leider keine
  Beiträge finden, die zu Ihrer Anfrage passen" (no posts); `Sizilien 1503` -> same, no posts; `Lasry Spanish` -> no post
  matching; the results shown (WWII ciphertexts, Voynich) mention none of Espagnol 318, Sicily, Messina, 1503, Ferdinand
  of Aragon or the Gran Capitán. Query 6 under (a) (`site:scienceblogs.de ... Sizilien 1503 Vizekönig Ferdinand Espagnol
  318`) returned only Cipherbrain's Ferdinand III (1630s) posts, a different Ferdinand and century. No Cipherbrain post
  to open, so no comment thread to read.
- **Cryptiana blog** (`cryptiana.blogspot.com/search?q=...`): `Espagnol 318`, `Sicily` and `1503` each return exactly one
  post, "Unsolved Spanish Ciphers in French Archives (1497-1504)", 21 Jan 2019,
  `cryptiana.blogspot.com/2019/01/unsolved-spanish-ciphers-in-french.html`, whose line about this item reads "f.120-121,
  no.94 Viceroy of Sicily to Ferdinand, 27 April 1503" under "BnF Espagnol 318 (Gallica) includes undeciphered letters."
  Opened live on 2 Oct 2026: the comment section reads "No comments:"; its Atom comment feed
  (`cryptiana.blogspot.com/feeds/6150222904528966435/comments/default`) carries `openSearch:totalResults` = 0. The
  on-disk snapshot `sources/cryptiana/blog/2019_01_unsolved-spanish-ciphers-in-french.html` (committed 2 Oct 2026
  00:22 UTC) shows the same "No comments:". The neighbouring post "Two more unsolved Spanish ciphers" (15 Jan 2019,
  `cryptiana.blogspot.com/2019/01/two-more-unsolved-spanish-ciphers.html`) was opened too: it does not mention
  Espagnol 318, Sicily, Messina, 1503 or no.94, and its comment section also reads "No comments:" (live and on disk).
  Tomokiyo's own pages, grepped on disk first (`sources/cryptiana/`, zero requests): `web/spanish.htm` line 963,
  `web/unsolved.htm` line 120 and `web/unsolved-2026-09-24.htm` line 127 all list "f.120-121, no.94 Viceroy of Sicily to
  Ferdinand, 27 April 1503" under "undeciphered"/"unknown ciphers"; `web/GL.htm` line 186 gives Lasry's 2022
  "approximate" solution for no.95 only. Live re-reads on 2 Oct 2026: `cryptiana.web.fc2.com/code/unsolved.htm` (page
  dated 27 September 2026) still lists no.94 among the three "unknown ciphers" of Espagnol 318, with the Lasry note
  attached to no.95 only; `code/spanish.htm` (dated 29 May 2022) lists no.94 as "undeciphered"; `code/GL.htm` (last
  modified 15 April 2026) mentions only no.95 and claims no solution for the 27 April 1503 letter.
- **Cipher Mysteries** (`ciphermysteries.com/?s=...`): `Espagnol 318` -> "Nothing Found. Apologies, but no results were
  found for the requested archive."; `viceroy Sicily 1503` -> same; `Lasry Catholic Monarchs` -> same. No post to open.
  The on-disk snapshots `sources/ciphermysteries/`, `sources/schmeh/`, `sources/vals-ai/`, `sources/openai/` and
  `sources/lasry/` were grepped for "Espagnol 318", "viceroy of Sicily", "vice-roi de Sicile", "virrey de Sicilia" and
  "Messina ... 1503": no file matches.

**(c) Every plausible hit opened, with its comment thread where one exists.**

1. `dbourdeau.github.io/cyphersolver/esp318.html` (page "updated 24 September 2026"): no. 94 "The viceroy of Sicily to
   Ferdinand, Messina, 27 Apr 1503; Spanish, clear and cipher mixed, four pages", "Both are not deciphered" (nos. 93 and
   94), "No decipherment survives anywhere in the volume for nos. 93, 94 or 95." No comment thread on the page.
2. `raw.githubusercontent.com/dbourdeau/cyphersolver/main/targets/esp318/NOTES.md` (live, HEAD of 2 Oct 2026): table row
   "| 94 | 120-121v | 452-455 | The viceroy of Sicily to Ferdinand, Messina, 27 Apr 1503. Spanish, clear and cipher mixed,
   four pages | unidentified; RRCC architecture, code initials g/l/m/n/p/r/v/z | **open** |"; "Nos. 93 and 94 remain
   unread, but they are no longer 'unidentified ciphers': both are standard ciphers of Ferdinand's secretariat"; the
   remaining-gaps line "No. 94 (ff. 120r-121v), whole letter - blocker: not-attempted; never transcribed; Bergenroth's
   Gran-cifra list not tested against it". The file quotes clear-text passages of the letter ("para poder passar esta nao
   la galea de allá ... donde llegó don Fernando de Andrada y Benavides y Carvajal y bolvióse de los aquí ...", "commo esto
   passamos en anocheçiendo", "En lo de la hazienda luego ...") and the f.121v endorsement "Del virrey de Siçilia en çifra"
   -- these are the letter's own clear portions, not a decipherment of its cipher. Used as the quoted phrases of (a) 7-8.
3. `github.com/dbourdeau/cyphersolver/pulls?q=is:pr+esp318` -> "0 results"; `.../issues?q=is:issue+esp318` -> "0
   results". No PR or issue thread discusses this volume.
4. `github.com/setsunaatto/cyphersolver` ("forked from dbourdeau/cyphersolver", 1,996 commits): its
   `targets/esp318/NOTES.md` carries the same no. 94 row ("open"), the same "not-attempted; never transcribed" blocker and
   the same clear-text excerpts as the upstream file -- a fork, not an independent reading. `github.com/arya1515/
   cyphersolver` was already logged on 26 Sept 2026 above as an older copy of the same folder.
5. *El Debate* article of 15 Feb 2018 (query 11): the CNI's four deciphered 1502-03 letters are between Ferdinand and the
   Gran Capitán; the article names no archive and contains no sentence about Sicily, Messina, a viceroy, the BnF or
   Espagnol 318. Not this letter.
6. Not opened, with reason: the Schneier/36kr/kucoin/blockchain.news items of query 9 report a 1650s solve and do not
   name Espagnol 318, Sicily or 1503 in title or snippet; the Wikipedia viceroy lists and dictionary pages of queries
   1-6 are not about any cipher.

**Result.** No decipherment or plaintext of this item located by these queries on 2 Oct 2026 (a search result, never a
novelty verdict, rule 10). The status word on line 1 stays `open`. Hosts (this job): scienceblogs.de 3 requests,
ciphermysteries.com 3, cryptiana.blogspot.com 6 (3 searches, 2 posts, 1 comment feed), cryptiana.web.fc2.com 3,
github.com 3 page views + 1 raw file, eldebate.com 1, dbourdeau.github.io 1; all answered HTTP 200, none rate-limited
or challenged; 11 queries through the built-in web search tool (not a direct host fetch); `sources/` grepped on disk
first with zero requests.

```
$ python3 tools/intake_gate_check.py esp318-sicilia-1503
esp318-sicilia-1503: open (line 1) -- edition/page or full-text-search citation found within 6 lines
(exit 0)
```

## Premise check (GF4-BATCH3, account-4, 3 Oct 2026)

Adversarial pass per `.claude/briefs/check-solved.md` (try to prove the item already done), before any first test.
**Result: not found on (a) (b) (c); (d) one recipient-side edition not page-read (a gap, named below); status stays `open`.**

- **(a) Decipherments the folder mentions -- not found.** The folder names three: Lasry's 2022 "approximate"
  alphabet (item **95**, a different letter, Tomokiyo GL.htm), Parisi 2020's reading (item **5**, and Bourdeau's
  partial no. 92), and the key sources Bergenroth's *Gran cifra* sheet (BNE MSS 20.211/52) and the "Cifra del
  visorrey" (BRAH 9/15 ff.1-6). The last two are keys, not decipherments of no. 94. Bourdeau's copy of Galende
  Díaz 1994 (`targets/esp318/lit/galende1994.txt`, grepped 3 Oct 2026) lists "Cifra del visorrey (folios 1 a 6)"
  in an inventory (l.340) and nothing that reproduces it or reads a 1503 Messina letter. No interlinear or gloss on
  ff.120r-121v (f.121v carries only the superscription, the seal and the endorsement "Del virrey de Siçilia en
  çifra", Bourdeau `targets/esp318/NOTES.md` l.38-40: "There is no decipherment anywhere in the volume for nos.
  93, 94 or 95").
- **(b) Other solvers' working files -- not found.** Fresh shallow clone dbourdeau/cyphersolver main 2341682
  (3 Oct 2026), `targets/esp318/`: working files exist for no. 92 (`ct92_*`, `f116_reading.md`), no. 93
  (`ct93_eye.txt`, `solve93.py`) and no. 95 (`f122r_*`, `*95.py`) -- **nothing for no. 94** (no `f120`/`f121` text,
  no rendering, no key run); his `keys/` holds only `cifra_general.json/.txt`, which his own notes exclude for 93/94
  by code-initial range. Status line l.3: "nos. 94 and 95 f. 122v unread"; gaps l.275 "No. 94 ... blocker:
  not-attempted; never transcribed". Aymeloglu (main d2800bb): nothing for Espagnol 318 no. 94.
- **(c) Physical neighbours -- not found.** Gallica btv1b52503046q, 1400 px, 3 Oct 2026: canvas 451 (the page
  facing f.120r) and canvas 456 (after f.121v) are both blank modern guard sheets of the binding (the volume mounts
  each letter between blanks); no slip, no clear copy laid in. ff.120r-121v themselves are on disk (canvases
  452-455). Item 95 (ff.122-122v, canvases 458-459) is a separate wholly-cipher 1497 piece, not a clear copy.
- **(d) Recipient's side -- not found; one gap.** Recipient Ferdinand the Catholic. Bergenroth CSP Spain vol. I and
  Supplement read in full above (no entry). Google Books API (`country=US`, key), interior phrases and names, not the
  opening: `"Fernando de Andrada" Mesina 1503 virrey` (3: a 1994 biography of Fernando de Andrade, encyclopaedias),
  `"virrey de Sicilia" "27 de abril de 1503"` (5: Cerignola narratives), `"commo esto passamos en anocheçiendo"`
  (0), `"Lanuza" virrey Sicilia 1503 carta cifra` (1: *Los fondos documentales del archivo del reino de Aragón*
  (2000), an inventory line "Cartas del virrey de Sicilia a don Juan de Lanuza. Otra de Claver en cifra" -- other
  letters, a lead for sibling material, not this one). **Gap:** A. de la Torre, *Documentos sobre relaciones
  internacionales de los Reyes Católicos* vol. VI (1498-1504, Madrid 1949-66), the recipient-side documentary
  edition, is snippet-only; its index shows "Sicilia. 1498: 78-80, 188 ..." but two title-restricted queries for
  "virrey de Sicilia"/Mesina 1503 returned 0, so whether it prints a register copy or summary of this letter is
  unverified -- a LOCAL-QUEUE/HathiTrust page read of vol. VI's index under "Sicilia" and "Lanuza" settles it.

Requests this pass: gallica.bnf.fr 2, googleapis.com 7, github.com (clone shared with decode-2754). Next cheap test
(Bourdeau's own named step, unrun by anyone): two-pass transcription of ff.120r-121v from the crops already on disk,
then Bergenroth's Gran-cifra list against it with a matched control.

## First cheap test: f.120r two-pass transcription + Gran-cifra key test (FT4-esp318-sicilia-1503, account-4, 3 Oct 2026, 00:47-01:0x UTC)

**Scope actually run: f.120r only** (1 of 4 pages). Vision calls: 2 (two blind Opus passes, one page per call, on the
66 line crops already on disk from `tools/iiif_lines.py --ark btv1b52503046q --canvas 452 ... --prefix f120r`, the
26 Sept command above; no new crop run needed for this page). No reconciliation call: see "Pass agreement".
ff.120v-121v not transcribed (full-page images exist in Bourdeau's clone, `targets/esp318/full/f12{0v,1r,1v}.jpg`,
3819x5115; cut with `tools/iiif_lines.py --image` when the alphabet is settled). Requests: elprofedefisica.naukas.com 1
(the key image), gutenberg.org 1 (La Celestina, considered as an era corpus and not used: it is a modernised,
copyrighted edition), github.com 1 shallow clone (dbourdeau/cyphersolver HEAD 810a777, 2 Oct 2026). Gallica 0.

**Key source.** Bergenroth's *Gran cifra* of the Gran Capitán, 1501-04, BNE MSS 20.211/52, as photocopied and
published by Arturo Quirantes (elprofedefisica.naukas.com, 2 Feb 2018, image `Clave-Gran-Capitan-1.jpg`; credited).
Bourdeau's `lit/berg/` turned out to hold only OCR of Bergenroth's *Documentos* volumes (unreadable, manuscript
facsimiles), not the key, so the key was read here from Quirantes's image: `key/gran_cifra_alpha_rows_*.jpg`,
`key/gran_cifra_codes.jpg` (crops), `key/key_gran_cifra.tsv` (23 sign rows a-z + ll, the anulante, 50 code entries;
codes with two values on the sheet, e.g. tao = na|nos, nom = franceses|esto, are graded M). Key grade if it ever reads:
`published` (Bergenroth's reconstruction).

**Pass agreement.** `tools/reconcile_passes.py passes/f120r_passA.tsv passes/f120r_passB.tsv --keep-plain`:
A 1117 tokens, B 1175; agree 439/1183 = **37.1%** (agreed-H 34, agreed-uncertain 405, disagree 744). Class counts:
clear words A 83 / B 85, code groups 214 / 187, sheet-matched signs 335 / 452, unmatched signs 485 / 451. Both readers
graded nearly every sheet match L ("look-alike guesses"); they agree on the clear Spanish (superscription L01-02, L05-06
"don fernando de andrada y benavides y caravajal y bolviosse dellos aqui", L12, L15, L25, L28 "para la roqua de angito
... el despacho del armada", L32-33) and on the frequent code groups. The split is far above a tenth and the cause is
an unsettled sign inventory (letters vs groups, and the sheet's 19th-c. hand vs the 1503 hand), so per CLAUDE.md Usage 6
and `tools/lookalike_pass.py`'s own "Must NOT be used for" clause the look-alike pass was **not** run (it would make
three machine readers agree on a wrong sheet) and no third machine pass or model reconciliation was spent: the next
transcription step is the owner's sign sorter. A sheet-crop fault also hurt both passes: row m of the key fell on the
seam between the two alphabet crops, so no reader could label an m sign (re-cut with overlap next time).
`ciphertext.tsv` = `passes/ciphertext_draft.tsv` (majority/A sign, confidence per token, alt column), a draft, not a
settled transcription.

**Key test 1 -- code overlap** (`code_overlap.py`, `--check` OK): 38 distinct code groups agreed by both passes
(115 tokens); 2 match a Gran-cifra code after merging look-alike letters (mok~moc "con", nob~uob "la"; 4 tokens).
Control, 200 random code lists with the key's own length profile and letters: mean 0.58, p95 2, max 3. **At chance:
a mismatch, not a negative** -- the five commonest groups (otto 22, rah 21, mal 10, mys 6, ml 6) are not on the
list, and Bergenroth's list is partial (~50 of the 200+ codes Quirantes and the CNI count). It does not exclude the
Gran cifra; it says this partial list cannot be shown to be the key of no. 94.

**Key test 2 -- sign alphabet** (`gran_cifra_test.py`, `--check` OK): cipher-only stream from the draft, 377 letters,
es 4-gram judge (es17: Cervantes/Quevedo, about a century late; no early-16th-c. Spanish corpus on disk -- rule 3 era
mismatch noted, not fixed). Target -2.015 per letter; shuffled-key control (200 keys): p50 -2.059, p95 -1.781, 81/200 at
or above target; judge real_p05 -0.894, null_p99 -1.857. **Non-test**: on a transcription whose sheet labels are L-graded
guesses at 37% inter-pass agreement, any key scores at the control median. The decoded stream is a/c/f/r/s soup because
the readers mapped the commonest shapes (7, q/9, a, x) to a3/c3/f1/r1. Grades per token: none claimed (no reading).

Both rows in `HYPOTHESES.md`. `decode.json`/`tools/decode_key.py` not used: there is no reading to regenerate; the two
scripts above are the rule-7 checks for the numbers reported.

**Not found:** no Gran-cifra reading of no. 94 on f.120r; no evidence for or against the key beyond chance.

## GAPS-esp318-sicilia-1503 (3 Oct 2026, account-4, 01:28-01:4x UTC)

Verdict step run: fetch the "Cifra del visorrey", BRAH 9/15 ff.1-6. **Result: not fetchable from the cloud; no holding
record online.** Galende Díaz 1994 (Bourdeau's text copy, `targets/esp318/lit/galende1994.txt` l.327-346 and n.9) places
it in a 25-leaf folio volume, vellum, lettered "Cifras de los Reyes Católicos", B.R.A.H. sign. 9/15, ff.1-6, followed by
the Cifra general (ff.7-9), Silva-Garcilaso (11-14), Diego de Muros (15), Mauleón (16), Juan Manuel (18).
- RAH Koha OPAC (catalogo.rah.es), call-number phrase search "9/15": 5 hits, none is 9/15 itself (3/2271/2272,
  15-7-9/15, 15-2-9/15(I-XIII), 9/3780(9-15 y 17-19), 23-Caja 9/15) -- the OPAC does hold some 9/xxxx manuscripts
  (9/3780), so the absence is a real search result, not a wrong index. Keyword "cifras reyes católicos", "cifras"
  (manuscripts), "cifra visorrey": 0 each.
- RAH Biblioteca Digital (headless browser): "cifras" 13 hits, none the volume; "visorrey" 0; a third query met the
  Anubis challenge and the host was not retried. OAI-PMH has one set ("driver"), no search route.
- **Availability flag: none quotable** -- no holding record for 9/15 in either catalogue; Bourdeau's notes agree
  ("RAH 9/15 is not online", `targets/esp318/NOTES.md` l.121). Manifest of the routes: `key/visorrey_manifest.json`
  (no images).
- Shape inventory against the sorter's 40 piles: **not done** (no image of the key exists to compare). Vision calls 0.
- Route: the RAH library copy order already open in ASKS 68 (RAH sent its request form 28 Sept); one line for 9/15
  ff.1-9 added as ASKS 105 for the owner.
Requests: catalogo.rah.es 6 (one proxy error, one retry), bibliotecadigital.rah.es 4 browser + 2 OAI (one Anubis
page, stopped), github.com 1 shallow clone, web search 3; all at least 1.5 s apart.

## Remaining gaps (FT4-esp318-sicilia-1503, 3 Oct 2026; GAPS 3 Oct)
Read so far: 0% of cipher tokens read; clear Spanish on f.120r (about 85 words) agreed by two blind passes.
- Sign alphabet of no. 94 - blocker: waiting-on ASKS 104 (owner's sign sort, page https://claude.ai/artifact/92bH8f981H2M95JNM3PVBL, built FT4b 3 Oct 2026); two machine passes split 63% because the inventory is unsettled (passes/agreement.tsv), so the next pass is a person's (CLAUDE.md Usage 6)
- ff.120v-121v - blocker: not-attempted; never transcribed, held until the alphabet is settled; next: crops via tools/iiif_lines.py --image from Bourdeau's full/ pages, after the alphabet is settled, ~$3/page for two passes
- Cifra del visorrey key (BRAH 9/15 ff.1-6) - blocker: waiting-on ASKS 105 (RAH copy order, riding ASKS 68); no online record or image, GAPS 3 Oct 2026 (key/visorrey_manifest.json)
- Nomenclator of no. 94 - blocker: open-codes; commonest groups otto/rah/mal/mys/ml are not in Bergenroth's partial list (code_overlap.json)

## Escalation (3 Oct 2026)
- [ ] siblings: Lanuza/Claver letters of the viceroy of Sicily (Archivo del reino de Aragón inventory line, Premise check (d)) not yet located
- [x] clear-pages: clear Spanish on f.120r transcribed by both passes; usable as context, not as a crib for coded spans yet
- [ ] known-keys: Gran cifra tested (code overlap at chance, sign test a non-test); Cifra del visorrey BRAH 9/15 searched 3 Oct 2026, no online record or image, waiting-on ASKS 105; next untried key: none named
- [ ] print: A. de la Torre, Documentos sobre relaciones internacionales vol. VI index under Sicilia/Lanuza (LOCAL-QUEUE/HathiTrust page read), named in Premise check (d)
- [ ] key-rebuild: Bourdeau's named tool (groups as unknown words, sign alphabet annealed against Spanish) not built; needs a settled transcription first
- [x] image-check: key sheet re-cut with overlap, row m read zoomed: 4 signs (key/key_gran_cifra.tsv m1-m4; A4-RFESP 6 Oct 2026); every row re-counted, 44 phantom slots removed, 90 signs + anulante (D4-ESPLL 6 Oct 2026)
- [ ] retry: none yet
Verdict: keep going: 2 internal gaps; cheapest next: once ASKS 104 settles the alphabet, label the sorter piles against the full key sheet (key/ crops now cover every row and the TSV's slot counts match the sheet, D4-ESPLL; visorrey key on ASKS 105); no disk-only step left before ASKS 104

## Sign sorter (FT4b-esp318-sicilia-1503, account-4, 3 Oct 2026)

Built the owner's sign-sorter page for f.120r: https://claude.ai/artifact/92bH8f981H2M95JNM3PVBL (private; ASKS row 104).
`sorter/build_tiles.py` re-cuts the 33 lines at full width from the committed source image (the s1/s2 half crops overlap
by 659 px and would double signs), boxes every ink piece with `tools/iiif_lines.py --groups 4` (gap from L04's blank-run
histogram), and piles the 1,937 pieces into 40 provisional k-means clusters (c01-c40, 1 `wide`); `tools/sign_sorter.py`
built the page (10.2 MB). No pass label is attached to a tile: the passes carry no x coordinate (README.md).
"Check these first": 40 tiles, one per commonest (A, B) split pair from passes/disagreements.tsv, placed by proportional
position along the line. No reading, no vision call; requests 0. Gaps step "Sign alphabet" now waiting-on ASKS 104.
Rebuild and apply-after-sort: sorter/README.md.

## While waiting

- (Done 6 Oct 2026: every row of key/key_gran_cifra.tsv re-counted against the sheet -- D4-ESPLL.)
- Depends on nobody: nothing disk-only named; the A. de la Torre vol. VI index read (Escalation, print) is the one step that waits on no ASKS row.
- (Done 6 Oct 2026: key sheet re-cut with overlap, row m read -- A4-RFESP.)
- (Done 3 Oct 2026: the Cifra del visorrey search -- no online record or image; ASKS 105.)

## Key-sheet re-cut, row m (A4-RFESP, account 4, 6 Oct 2026, 00:02-00:0x UTC)

Step: the image-check line ("re-cut the key sheet with overlap so row m is visible; read crops zoomed"). The full source
was not on disk, so Quirantes's image was fetched once (`Clave-Gran-Capitan-1.jpg`, 2467x3489, 300 dpi; kept in the
session scratchpad, not committed; entry in images/manifest.json `key_sheet`). New crops: `key/gran_cifra_alpha_rows_k-o_overlap.jpg`
(rows k-o, box 150,1300,1450,1720 at full size, row m whole) and `key/gran_cifra_row_l-ll-m_zoom2x.jpg` (rows l/ll/m, 2x).
Read by eye, no subagent call.

**Row m has 4 signs, not 6.** The FT4 key TSV had m1-m6 as placeholders (no reader could see the row). Now, grade H for
the value m (sheet row), shapes as read: m1 Z with a top bar over a crossed 4; m2 an open epsilon with no middle bar
(distinct from the barred epsilons of row ll); m3 a p-loop on a long descender crossed at the foot; m4 i followed by a
looped, crossed-stem ligature (il/lp-like). m5/m6 removed from `key/key_gran_cifra.tsv`. `gran_cifra_test.py --check`
and `code_overlap.py --check` still OK (the sign test and code list do not depend on the m slot count).
Seen in the same crop, not changed (outside the step): row l shows 3 signs (dagger, dotted T, 6) and row ll 3 (two barred
epsilons, a circled-dot with "="), where the TSV carries l1-l5 and ll1-ll5 -- a re-count of every row is the next
disk-only step (While waiting). Bearing on no. 94: m2 (open epsilon) and the ll epsilons are a look-alike pair for the
sorter; nothing read in the cipher. Requests: elprofedefisica.naukas.com 3 (two HTML pages, one image), >= 2 s apart.


## D4-ESPLL (account 4, 6 Oct 2026, 12:43-12:47 UTC by date -u)

Step: the While-waiting re-count. Every row of `key/key_gran_cifra.tsv` checked by eye against `key/gran_cifra_alpha_rows_a-ll.jpg`,
`key/gran_cifra_alpha_rows_m-z.jpg`, `key/gran_cifra_alpha_rows_k-o_overlap.jpg` and `key/gran_cifra_row_l-ll-m_zoom2x.jpg`
(rows a, o, r, t also zoomed 2x in scratch). No subagent call, no network request.

**Not only l and ll: every row except m (already fixed by A4-RFESP) carried exactly 2 phantom slots** -- FT4's TSV seems to have
padded each row by two. Sheet counts (old -> new): a 9->7, b 3->1, c 7->5, d 7->5, e 7->5, f 3->1, g 5->3, h 5->3, i 7->5,
j 4->2, l 5->3, ll 5->3, n 7->5, o 8->6, p 5->3, q 3->1, r 9->7, s 6->4, t 9->7, u 5->3, y 6->4, z 5->3 (m 4, k empty, tt1
the anulante, unchanged). 44 labels removed (the highest two of each row); the sheet now gives 90 signs + anulante.
Notes added: a6 is struck through with an X on the sheet (kept, value a); r5 is followed by a parenthesised struck-out
u-like alternative, not counted as a slot; l3 = 6 with a dot; ll3 = dotted reversed-c with a trailing "=".
Effect: none on any committed result. Every sheet label used in `ciphertext.tsv` (a3 a4 c2-c4 e1 f1 g1 h1 l1 l3 ll1 n3 r1
r6 s2 s3 t2 tt1 u3) is within the corrected counts; a value depends only on the row, and `gran_cifra_test.py`'s control
permutes row->letter, not slots. `gran_cifra_test.py --check` OK and `code_overlap.py --check` OK after the change.
For the sorter (ASKS 104): the alphabet to label against is 90 shapes, not 134. Requests: none.
