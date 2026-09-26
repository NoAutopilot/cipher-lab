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
