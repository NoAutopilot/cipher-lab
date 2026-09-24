# Oxenstierna, Gustav II Adolf to Axel Oxenstierna, Nürnberg 23 July 1632

**Status: found-solved** (verifier audit, 24 Sept 2026: letter 602 was deciphered and printed by R. Torpadie, "Några ord om chifferskrift", *Historisk tidskrift* 8 (1888), pp. 376-383, key table p. 382; class N0, see AUDIT.md. LANE R R3's reading below is an independent re-decipherment of the letter layer.)

> **Correction by the verifier, 24 Sept 2026.** (1) The letter is not unsolved: Torpadie solved it in 1888 from the printed ciphertext and printed the plaintext, the key of the letter layer and part of the codes (AUDIT.md). Every "open", "unsolved" or "partial" below describes what the searches found, not the state of the letter. (2) The edition volume (ser. II vol. 1, 1888) was edited by **Per Sondén**, not C. G. Styffe; "Styffe" below means Styffe's *Konung Gustaf II Adolfs skrifter* (1861) only where that book is named. (3) The editor's footnote gloss "[unsolved]" was true when the volume was printed.

## Item

Letter from King Gustav II Adolf (Gustavus Adolphus) to Rikskansler (Chancellor) Axel Oxenstierna, dated
"Nürnberg den 23 Julij" [1632] (printed "Anno 1682" is an OCR digit slip; Gustav Adolf died November 1632 and
the letter discusses the Nürnberg campaign and Banér). Printed in *Rikskansleren Axel Oxenstiernas skrifter och
brefvexling* (senare afdelningen, första bandet, ed. Per Sondén, 1888 [corrected from "C.G. Styffe's second series" by the verifier, 24 Sept 2026]), letter no. 602, pp. 821-822. Internet Archive identifier
`rikskanslerenax00styfgoog`, OCR (djvu text) lines 39880-39942. Found by the detector round 3, LANE S worker
(`.claude/briefs/runs/2026-09-24-lane-s-det3.md`), logged as QUEUE.md row W1 (section "Printed ciphertext
(detector round 3, LANE S, 24 September 2026)").

Approx. 150 cipher numerals (2-4 digit groups, values seen up to 3965) over ~40 lines of continuous
German/Swedish prose, cipher words interspersed with clear text word by word. The editor's own footnote states
the key could not be found: "Nyckeln till ofvanstående chifferbref har af utgifvaren icke i riksarkivet kunnat
återfinnas, men då intet tvifvel är om, att det är ett Konungens bref till Rikskansleren, hvartill möjligen en
lösning sedermera kan finnas, har det här blifvit meddeladt" (the key to the above cipher letter could not be
found by the editor in the Riksarkivet, but as there is no doubt it is a letter from the King to the Chancellor,
to which a solution may possibly be found later, it is included here [unsolved]). The footnote also names two
further cipher letters of the same day to Gustaf Horn ("duplett"/"triplett", same format), not located in the
round-3 sweep or this session — left as a next-worker note, not chased here (out of this brief's scope).

## Check-solved sweep, 24 September 2026

Run by this worker directly (not the Workflow tool), per `.claude/briefs/check-solved.md`'s six sources plus the
brief's editions-first list. Six-source status: 6/6 checked, 0/6 found a solution, key or documented attempt on
this specific letter.

**Editions first (this item's specific next-step list):**
- *Konung Gustaf II Adolfs skrifter*, ed. C.G. Styffe (Stockholm, P.A. Norstedt, 1861; IA `konunggustafiia01gustgoog`
  / `konunggustafiia00gustgoog`, same 647-p. Oxford-Google scan under two identifiers) — fetched the full djvu
  text (one fetch) and read the July-September 1632 section (djvu lines ~22400-22780). This volume prints letter
  no. 28 "Till Axel Oxenstierna, dat. lägret vid Nürnberg den 21 Juli Anno 1632" (in clear Swedish, from the
  Stjerneldska samlingen, Uppsala) immediately followed by letter no. 29 dated "Af lägret wed Nürenberg den 1
  Augusti år 1632" — no letter falls between them, so **this volume does not print the 23 July letter**, deciphered
  or otherwise; the two flanking letters it does print (21 July, 1 Aug) are plaintext originals from a different
  archival source (Stjerneldska samlingen / Kejserliga Biblioteket Petersburg), not from the same Riksarkivet
  transmission chain as the ciphered 23 July letter. be-api.us.archive.org full-text search for the exact printed
  footnote phrase ("Nyckeln till ofvanstående chifferbref") and for "Nürnberg den 23 Julii"/"den 23 Julii 1632"
  against both identifiers: 0 hits (consistent with the letter's absence).
- Hallwich/Irmer, *Die Verhandlungen Schwedens und seiner Verbündeten mit Wallenstein und dem Kaiser von 1631 bis
  1634*, vol. 1 (1631-1632), ed. Georg Irmer (Leipzig, Hirzel, 1888; IA `dieverhandlungen01irme`) — be-api
  full-text search for "Oxenstierna" + "23 Juli": 1 hit, p. LXXI (roman-numeral introduction, not the document
  body), a general remark on Swedish reports going to Oxenstierna and a citation of a separate 2 June 1632 letter
  in Arkiv I — not a citation of this letter. No further pages checked (this is a negotiations-with-Wallenstein
  document collection, not a natural home for a King-to-Chancellor operational letter; the introduction hit does
  not name our letter).
- Swedish cryptologic scholarship: a 2024 DECRYPT-project blog post and conference paper (Diallo/Waldispühl et al.
  via kopaldev.de and dspace.ut.ee) on deciphering DECODE record R3816 (Sigismund Heusner von Wandersleben to
  Oxenstierna, 1637) report that Michelle Waldispühl "has personally examined 15 letters received by Axel
  Oxenstierna ... sent by his ambassador in Germany during the Thirty Years' War, spanning from 1618 to 1648" —
  this is a *different* correspondent (an ambassador, not the King) and a different, wider set; neither the blog
  post (HTTP 503, unreachable this session) nor the paper (PDF text extraction failed, compression/encoding
  issues, not re-tried) could be read in full to confirm or rule out overlap with our letter. Logged as
  unreachable/inconclusive, not as a negative.
- Riksarkivet's own searchable edition database, `sok.riksarkivet.se/oxenstierna` (the modern online continuation
  of the *Axel Oxenstiernas skrifter och brev* project) — the search form is a plain GET (`/Oxenstierna/?Fornamn=
  ...&DatumFran=1632-07-23&DatumTill=1632-07-23`) but every query redirects to a CAPTCHA gate
  (`/captcha?returnUrl=...`), confirmed on the first attempt and one retry after a pause (good-citizen rule).
  Blocked; not retried further this session.
- Bourdeau's `riksarkivet1628/` (catalogue #207, DECODE R4282-R4341: Rusdorff-to-Oxenstierna 1628, Bremen
  archbishop-to-Salvius 1631 [read], an "1632?" Amsterdam letter R4306, June 1633 Oxenstierna letters) and
  `baner1640/` (Banér to Stålhandske, Dec. 1640) — fresh shallow clone, NOTES.md read in full: none dated 23 July
  1632, none from Gustav Adolf, and the numeral ranges don't overlap (R4306: 5-203 colon-separated; Bremen: bands
  8-103; our letter: 2-4 digit groups up to 3965, a much larger nomenclator) — no key to try here.

**Six sources:**
1. **web** — WebSearch, several phrasings ("Nyckeln"/"chifferbref" + Oxenstierna/Gustav Adolf 1632 Nürnberg;
   Swedish and German phrasings; Cipherbrain/Cipher Mysteries/DECODE query). No solution claim found. The one
   substantive lead (Waldispühl's 15-letter Oxenstierna-ambassador survey) is logged above as inconclusive, not
   a match.
2. **print** — see editions-first above (Styffe 1861: checked, absent; Irmer 1888: checked, one non-matching
   introduction hit). No CSP-style calendar exists for this Swedish series; the Rikskansleren edition itself
   *is* the calendar/edition for this correspondence, and its own footnote already states the key was not found.
3. **lists** — `sources/cryptiana/` grepped for "oxenstierna" and "gustav adolf"/"gustavus adolphus": zero hits.
   `CATALOG.md` and `LANDSCAPE.md` grepped: zero hits. Live Cipherbrain/Cipher Mysteries not separately browsed
   (WebSearch above covers a name+cipher query against them; no hit).
4. **decode** — de-crypt.org's public RecordsList search page returns only the app's static UI strings without
   login (no per-record results reachable, consistent with CLAUDE.md's "DECODE login is known broken" note; not
   attempted, per the one-attempt rule already spent by other workers today per ROOM.md). Fell back to the
   solver repos' own cached DECODE sweeps (Aymeloglu's `catalogue/decode-ranked.md`, which does index DECODE by
   sender/recipient): the only Oxenstierna-linked DECODE rows are R3816 (1637, Heusner von Wandersleben →
   Oxenstierna, partially decrypted) and R4332 (1637, → Oxenstierna, partially decrypted) — neither is this
   letter (wrong year, wrong sender).
5. **bourdeau** — github.com/dbourdeau/cyphersolver, fresh shallow clone: see editions-first above
   (`riksarkivet1628/`, `baner1640/` NOTES.md read in full). No folder or mention matching this letter.
6. **aymeloglu** — github.com/aaymeloglu/unsolved-ciphers, fresh shallow clone: `CATALOGUE.md` line 61 lists
   "Riksarkivet, Stockholm | 1600-1646, images public; R4332 (1637) carries both a decipherment and a key, so one
   key of the Oxenstierna circle is at hand for the rest" — a lead worth a solver's attention (a key already
   exists for *an* Oxenstierna-circle cipher, R4332, 1637; whether it fits a 1632 letter is untested, five years
   and possibly a different correspondent apart) but not a match to this letter itself. `catalogue/decode-ranked.md`
   and `pares-ranked.md` grepped: same R3816/R4332 rows as above, nothing else.

**Verdict: open.** [Wrong: corrected by the verifier, 24 Sept 2026. Torpadie, *Historisk tidskrift* 8 (1888) pp. 376-383, prints the solution; see AUDIT.md.] No solution, key, or documented prior attempt found on this specific letter in six sources
plus the editions named in the brief. Stage 2 (verified unsolved) reached, conditional on: the unreachable
Waldispühl blog/paper (may or may not cover this letter — logged, not resolved), the two Horn "duplett"/
"triplett" letters (not located), and the R4332 (1637) key's untested fit (a solver's task, not this worker's).

**Copy-free / image status:** copy-free. The full text is on Internet Archive (`rikskanslerenax00styfgoog`,
public OCR + page images at `https://archive.org/details/rikskanslerenax00styfgoog`); no REQUEST.md needed.

**Requests this session:** archive.org-family (advancedsearch, metadata, be-api fts, download, fulltext/inside.php)
13; WebSearch 6; WebFetch 2 (1 blocked HTTP 503, 1 unreadable PDF); sok.riksarkivet.se 2 (both redirected to
CAPTCHA, one retry per good-citizen rule, then stopped); github.com 2 shallow clones (bourdeau, aymeloglu).
de-crypt.org: 1 request to the public search page (no login attempted). No Google Books, no TNA Discovery.

## Extraction (stage-2 printed ciphertext), 24 September 2026

Per this worker's brief, since the check-solved verdict is open: fetched `rikskanslerenax00styfgoog_djvu.txt`
once (archive.org, `sources/ia-fulltext/rikskanslerenax00styfgoog_djvu.txt`, gitignored) and cut letter no. 602
(djvu-text lines 39871-39947) into `printed_ocr.txt`, `ciphertext.txt` and `tokens.tsv` with
`extract.py` (in the pattern of `tools/thurloe_extract.py`; deterministic, re-running regenerates byte-identical
output — checked). Clear words are kept verbatim (OCR errors and all, e.g. "8om" for "som", "tUl" for "till",
never repaired); numeral groups are classified CIPHER only if already a bare 1-4 digit run before any
substitution, with the OCR digit-lookalike fix (l/i→1, o→0) applied only to those; every doubt is flagged, not
resolved: `[?]` on a digit run that still isn't clean after normalisation, `[?]MERGED` on two digit groups run
together with no space ("26.24", one case), `[?]SYM` on 12 short letter-runs (r, rr, nn, mm, W, ee) interspersed
among the numerals that read as part of the cipher's own symbol set but are not reclassified as cipher by
inference, `[?]OCR` on one alphabetic token with a stray embedded digit ("8om"). The printed letter/place/date
heading ("602*). Nürnberg den 23 Juli 1682" — OCR digit slip for 1632) and the closing dateline formula ("Aff
lägret vidh Nürnberg den 23 Julij, Åhr 1632.") are printed apparatus in clear, not cipher: excluded from the
token stream and reported as their own `[HEADING]`/`[DATELINE]` lines so their digits are never miscounted as
cipher groups (an early version of this script did that; caught and fixed before committing).

**Counts (corrected from the round-3 detector's estimate):** 733 cipher tokens (not "approx. 150" — that figure
undercounted; this is a full per-token extraction, not a cluster estimate), 91 distinct numeral values, range
4-5152 (not "up to 3965" — 3965 is simply the highest value quoted in the QUEUE row's excerpt, not the letter's
actual maximum; 5152 occurs once, at djvu line 39886). 246 clear tokens. 39 of 979 total tokens flagged for OCR
doubt (about 4%).

**Leaf check:** archive.org's search-inside API (`ia601608.us.archive.org/fulltext/inside.php`, one query for
"Niirenberg") confirms printed p. 822 (the letter's closing lines) is BookReader leaf/page **n832**:
`https://archive.org/details/rikskanslerenax00styfgoog/page/n832`. Printed p. 821 (the letter's opening) should
be leaf **n831** by the same one-page offset (`https://archive.org/details/rikskanslerenax00styfgoog/page/n831`)
— not independently confirmed by a second search-inside query (one archive.org request judged sufficient for a
leaf check; a reader should verify both leaves against the image before trusting the OCR).

**Key-overlap check (not a decode):** the letter's numeral range (4-5152, mostly 2-4 digit groups) does not
overlap Bourdeau's `riksarkivet1628/` keys in any tested range (R4306: 5-203; Bremen bands: 8-103) or `baner1640/`
(2-98 two-digit homophones plus 14 three-digit code words 361-783) — none of those keys' value ranges reach into
the 1000s-5000s this letter uses, so none is a plausible fit by range alone. Aymeloglu's catalogue lists a
published key for DECODE R4332 (1637, Oxenstierna circle) whose value range was not checked here (out of this
brief's "do NOT apply any key" instruction — a solver's first cheap test, not decoding).

## Original letter hunt, 24 September 2026

Worker brief `.claude/briefs/runs/2026-09-24-lane-r-w1-original.md` (LANE R worker R5). Job: is the manuscript
of Gustav II Adolf's letter to Axel Oxenstierna, Nürnberg 23 July 1632 -- or a contemporary copy -- digitised at
Riksarkivet, and does it carry a decipherment written over or beside the cipher? Not a key hunt (that is the
"Key hunt, 24 September 2026" section above, a separate worker); this worker looked for the letter itself.
Host: `data.riksarkivet.se` Sök-API only, per brief. **Verdict: not digitised anywhere found; no route to a
decipherment on the leaf this session.**

**The received copy, identified.** `data.riksarkivet.se/api/records?text=Gustaf+Adolf&year_min=1632&year_max=1632`
surfaced `SE/RA/720701/II/01/B/I/E 614`, caption "Gustaf II Adolf", dated 1630-1632, inside the **Oxenstiernska
samlingen** (`SE/RA/720701`) hierarchy: Oxenstiernska samlingen > Oxenstierna af Södermöre > Axel Oxenstierna >
Inkomna brev och ansökningar > Furstars, ämbetsmäns och enskilda personer brev och ansökningar. This is Axel
Oxenstierna's own **incoming**-letters series -- the recipient's copy, i.e. the actual manuscript the King's
letter of 23 July 1632 would be bound into. Its catalogue note reads verbatim: "Breven finns tryckta i Axel
Oxenstiernas skrifter, Avd. II, Band 1." (the letters are printed in Axel Oxenstiernas skrifter, Section II,
Volume 1) -- confirming this bound volume, not some other copy, is the edition's (Sondén's, not Styffe's) own source for letter no. 602.
`onlyDigitisedMaterials: false` on the record; confirmed at the RDF/JSON-LD level
(`data.riksarkivet.se/archive/cigYyX8462FTV8KInbNGj6.jsonld`, fetched directly): its only `rico:hasInstantiation`
is typed `Analog`, no IIIF/image link in `_links` (contrast `SE/RA/1112.1/B/176` below, which does carry one).
No item-level (per-letter) breakdown is exposed by the API -- E 614 is catalogued as one bound volume spanning
1630-1632, not indexed letter by letter, so its 23 July 1632 leaf cannot be located or previewed without opening
the physical volume. **Not digitised. This is the strongest candidate for where an interlinear or marginal
decipherment, if Oxenstierna's own chancery made one on receipt, would actually be -- and it cannot be checked
this session.**

**Rikskansliets koncept/registratur, checked and ruled a different channel.** `text=Rikskansliets+koncept`: 0
hits, that exact series name does not exist in the catalogue. The broader `Riksregistraturet` fonds
(`SE/RA/1112.1`, 1523-1718) does exist and *is* digitised (`onlyDigitisedMaterials: true`); its 1632 volume is
`SE/RA/1112.1/B/176` (`text=1632` restricted to `facet=PartOfArchive:Riksregistraturet`, single hit), with a IIIF
manifest already resolvable (`https://lbiiif.riksarkivet.se/arkis!A0038671/manifest`, not fetched -- see below).
But its catalogue note is "rådets reg." (the Council's own register) and its provenance is "Kunglig Majestäts
kansli" -- this is the **domestic** chancery/Council's register of outgoing correspondence issued from Stockholm
while the King campaigned in Germany, not a record of the King's own field letters to Oxenstierna in the German
theatre. No text search (`text=Fältkansliet`, `text=Faltkansliet`) turned up a separate digitised field-chancery
or foreign-correspondence register for 1632 that could plausibly carry this specific letter. **Judged not a
match by provenance and content, not fetched** -- fetching ~300+ folio images of an unrelated administrative
register to search for one letter that would not be there is not what this brief's "<=120 requests" budget is
for; flagged here rather than pursued, per the "stop when the brief is met" usage rule.

**Horn duplicates, re-confirmed.** `SE/RA/720095/05/01/E 2348` ("Gustaf II Adolfs brev till Gustaf Horn",
1631-1632) reappears in the `text=Gustaf+II+Adolf&year_min=1632&year_max=1632` sweep above, still
`onlyDigitisedMaterials: false` -- same as the 24 Sept key-hunt worker already found for both E 2348 and E 2350.
No new information; not re-queried further to avoid duplicating that worker's session.

**Verdict for the brief's question: no.** Neither the manuscript this letter would be bound in (E 614), nor
either Horn duplicate (E 2348/E 2350), nor a plausible field-chancery register is digitised. The one digitised
volume found in this circle (`SE/RA/1112.1/B/176`, the Council's 1632 Stockholm registratur) is real and
IIIF-served but is the wrong archival channel for this specific royal field letter -- its images were not
fetched. **No interlinear or marginal decipherment could be checked this session; nothing was seen, because
nothing digitised was found to look at.** REQUEST.md item 3 below adds E 614 as a physical-access target.

**Requests this session:** `data.riksarkivet.se` about 37 attempts (roughly 25 succeeded 200 on first or retry;
the rest hit the session's known intermittent `SSL_ERROR_SYSCALL` through the agent proxy -- confirmed
transient, not a block: a plain reachability probe alternated 200/000 on requests seconds apart with no relay
failure logged by the proxy status endpoint; every failed query was eventually retried to a 200 except the two
noted below, each after >=2 s, forcing `--tlsv1.2` per the existing NOTES.md guidance); `sok.riksarkivet.se` 1
request (`/arkiv/<id>` for E 614's html link, 302 to the captcha gate, not pursued further -- API/JSON-LD already
gave the needed metadata). No image fetches (nothing digitised matched). No credentials, no subagents, no
decoding, no novelty wording.

## Next steps (for a later solver/access worker, not this brief)

- Locate the "duplett"/"triplett" Horn letters the footnote names, in case one is transcribed elsewhere.
- Try `sok.riksarkivet.se/oxenstierna` again with a real browser (may pass the CAPTCHA where curl cannot) if a
  worker's permission policy allows.
- Read the Waldispühl 15-letter Oxenstierna-ambassador survey properly (retry the kopaldev.de blog when the site
  is up, or find the paper's HTML/clean-text version) to see whether it names this letter.
- R4332 (1637, DECODE, Oxenstierna circle) has a published key per Aymeloglu's catalogue — a solver could test
  whether its nomenclator range (unknown here) overlaps this letter's numeral range (2-4 digits, up to 3965)
  before any ciphertext-only attempt; this is a key-fit test, not decoding, and was not run here per this
  brief's "do NOT apply any key" instruction.
- The numeral range (up to ~3965) implies a large nomenclator; per LESSONS.md, the productive route for a system
  like this is a sibling letter with a contemporary decipherment or the original key in the archive, not
  ciphertext-only cryptanalysis on ~150 tokens.

## Key hunt, 24 September 2026

Worker brief `.claude/briefs/runs/2026-09-24-lane-s-keyW1.md` (LANE S). Job: find where the key, a decipherment,
or the Horn "duplett"/"triplett" letters the editor's footnote names might survive, without applying any key.
Corrected numeral profile from the extraction above: 91 distinct values, range 4-5152.

**Route 1, QUEUE.md row R10 (SE/RA/721502/3/1, Oxenstiernaprojektets arkiv).** Re-confirmed via the Riksarkivet
Sök-API (`data.riksarkivet.se/api/records?text=Oxenstiernaprojektets`, fonds id `V1QZnA23KaW0Jkn0Wrqdi0`,
`SE/RA/721502`, "Oxenstiernaprojektet" 1998-2018, `onlyDigitisedMaterials: false`): this is the modern edition
project's own working papers ("Anteckningar om och kopior av källmaterial", notes and copies of source material),
not a primary holding — the row's own QUEUE.md text already carries the item's full catalogue note. Confirms
scout R's 24 Sept exclusion of this row as secondary/duplicate-of-editorial-process territory, not a fresh lead.
No new information beyond what QUEUE.md row R10 already states.

**Route 2, Riksarkivet cipher-key holdings 1630-1633 — the productive route.** The public Sök-API
(`data.riksarkivet.se/api/records`) is intermittently unreachable through this session's proxy
(`SSL_ERROR_SYSCALL`, matching scout R's 24 Sept note; forcing `--tlsv1.2` and retrying up to 3x per query, ~2s
apart, got most queries through — see request count below) but works. Broad sweeps: `text=chiffer` restricted to
`year_min=1628&year_max=1634` (the API searches both the record's own dating and its archive creator's dating) —
**5 hits**, one of them new and substantial:

- **`SE/RA/202/1` ("Chifferklaver", box/"låda" I, item 1, dated 1500-1640, not digitised)** — the item note lists
  the individual key booklets by hand: "I:6-17 ... 'Kanslichiffer 1620-1650-talen' [chancery cipher, 1620s-1650s],
  a thick bundle of 20 small booklets, one fire-damaged"; "I:14, cipher for the correspondence between Axel
  Oxenstierna and Lennart Torstensson"; "I:18 parts 1-2, Axel Oxenstierna, 'Anders Swensson Ciffrer' [Anders
  Svensson's ciphers], 2 bound books, bound together 1630"; "I:19 A, 'Ciffrer waanliga at brukas' [ciphers
  usually used] by Anders Svensson, plus L. Camerarius, 1 book"; "I:19 B, 3 envelopes: Wackenberg, Dietrich von
  Falckenberg, [V] Thuru, Spens"; "I:19 C, 'Dupletter Spens Ru'"; "I:22, Chifferklaver Ludvig Camerarij + B.
  Wolffsberg/Lennart Torstensson"; "I:22, 'Camerarius till Axel Oxenstierna'"; "I:24, bound book + duplicates."
  Anders Svensson (SBL id 5776) was a Swedish diplomat active with Oxenstierna and Salvius in 1629-30 preparing
  Gustav Adolf's German landing — squarely the right circle and years, though the note does not name Gustav II
  Adolf or Gustaf Horn by title. **This is a different box from Bourdeau's territory**: `riksarkivet1628/` and
  `baner1640/` are drawn from DECODE's Chifferklaver **låda II** (R4103-R4329, confirmed by grep of a fresh
  shallow clone of both solver repos — "låda II:113" etc. throughout, zero hits for "SE/RA/202", "låda I",
  "Anders Swensson"/"Svensson", "Camerarius" or "Falckenberg" in either repo), while this item is explicitly
  **låda I** — adjacent but distinct, not already worked. Not digitised (`onlyDigitisedMaterials: false` on both
  the fonds `SE/RA/202` and item `SE/RA/202/1`); a reading-room task, not a cryptanalysis one, and its own value
  range cannot be assessed without an image. Flagged as the best candidate for the key itself, conditional on
  archive access.
  Other 4 hits in this year-restricted sweep: `SE/RA/25.3/4/II/7/B` (1676-77 full powers, wrong period),
  `SE/RA/202` (the Chifferklaver fonds record itself, same as above), `SE/RA/1411/E/E VI/1` (Vellingk 1713-14,
  already QUEUE.md row R7), one WWII administrative hit outside the year filter's precision (`SE/KrA/0115`, date
  field empty, caught by a name match not a date match).
- Direct name/place queries found nothing further: `text=Gustaf Horn chiffer` (0), `text=chiffer Nürnberg` (0),
  `text=Skoklostersamlingen chiffer` (0), `text=Kanslikollegium chiffer` (1 hit, the same Vellingk R7 row), and
  the unrestricted `text=chiffernyckel` (5 hits — re-confirms scout R's R1/R2/R3 rows and one WWII item and one
  unrelated 19th-c. Falkenberg-family item; nothing new for 1630-1632).

**Route 3, Gustaf Horn's papers for the "duplett"/"triplett" letters — the second strong lead.** The fonds
search `text=Gustaf Horns arkiv` surfaced Gustaf Horn's own personal archive, held in two related fonds
("Bielkesamlingen" > "Horn-Bielkesamlingen" > "Riksmarsken Gustaf (Carlsson) Horns papper", `SE/RA/720095/05/01`)
plus "Gustaf Horns och Sigrid Bielkes arkiv" (`SE/RA/720900/B/i`). A `text=Gustaf Horn&year_min=1632&year_max=1632`
sweep (59 hits) found, inside the Horn-Bielkesamlingen fonds:
- **`SE/RA/720095/05/01/E 2348`, "Gustaf II Adolfs brev till Gustaf Horn" [Gustav II Adolf's letters to Gustaf
  Horn], dated 1631-1632** — the volume of the King's own letters to Horn covering exactly this letter's date.
- **`SE/RA/720095/05/01/E 2350`, "Kungliga skrivelser (dubletter) till Gustaf Horn" [Royal letters (duplicates)
  to Gustaf Horn], dated 1628-1644** — its title uses the word "dubletter" (duplicates), matching the printed
  footnote's own word "duplett" for the second Horn letter it names.
Both are `Volume`-level Sök-API records with no further item-level note text returned by the API (no per-letter
listing), not flagged `onlyDigitisedMaterials`, so not digitised — a reading-room task to open the volume and
check for the 23 July 1632 date, and for whether a contemporary decipherment rides with either cipher original
(the LESSONS.md "sibling letter" pattern). Not checked against Bourdeau/Aymeloglu material (below) because
neither repository mentions this fonds at all (grep, zero hits for "720095", "Horn-Bielke", "Bielkesamlingen",
"Riksmarsken" in either shallow clone).

**Route 4, Bourdeau's `riksarkivet1628/`/`baner1640/` key-range check.** Already done in full by this target's
24 Sept check-solved worker (see "Key-overlap check" above): this letter's range (4-5152, mostly 2-4 digit groups)
does not overlap `riksarkivet1628`'s keys (R4306: 5-203) or `baner1640`'s (2-98 homophones + 361-783 code words)
in any tested band — not re-run here to avoid duplicating that worker's session (ROOM.md "duplicate work ... is
what the room prevents"). This session's own grep of both repos (route 2/3 above) additionally confirms neither
repo has touched `SE/RA/202` (låda I) or the Horn-Bielkesamlingen fonds at all, so there is no overlap to check
there either — those are simply un-surveyed by either solver, not tested-and-rejected.

**Route 5, open-index scholarship.** OpenAlex answered "Rate limit exceeded ... $0 remaining" (network-wide daily
budget already spent by other lanes today, confirmed by the error body, not this worker's own calls) and
Semantic Scholar answered HTTP 429, both unreachable this session. `diva-portal.org` reset the connection twice
(`ws_closed_mid_exchange`, one retry per the good-citizen rule, then stopped) — unreachable this session, not
searched. WebSearch (several Swedish- and English-phrased queries for "Gustav II Adolf"/Oxenstierna/Horn +
chiffer/chifferbrev/chiffernyckel/1632/Nürnberg, and a DiVA-scoped query) found no scholarship or archival
announcement naming this letter, its key, or the Horn duplicates; the Riksarkivet's own modern Oxenstierna
edition-project search pages (`sok.riksarkivet.se/oxenstierna`) were fetched directly (not through the
captcha-walled query form) and do not mention cipher material at all.

**Verdict for a solver/access worker:** no digitised key, decipherment, or Horn duplicate is public. Two
un-surveyed, not-yet-excluded physical candidates, both needing a Riksarkivet i Stockholm/Täby reading-room
visit or reproduction order (see `REQUEST.md`): (1) `SE/RA/202/1`, Chifferklaver låda I, for the "Kanslichiffer
1620-1650-talen" bundle and named booklets (Anders Svensson, Camerarius, Falckenberg, Spens); (2)
`SE/RA/720095/05/01/E 2348` and `E 2350` in the Horn-Bielkesamlingen, for the King's 1631-1632 letters to Horn
and the "dubletter" volume that may hold the footnote's named duplicate/triplicate. Neither is confirmed to
contain this letter's key or the Horn cipher originals — both are catalogue-level, unopened leads, not a
confirmed match; a value-range assessment against this letter's 91 values (4-5152) is not possible without an
image. `keys/manifest.json` records both candidates and every route tried.

**Requests this session:** `data.riksarkivet.se` ~19 attempts, 11 succeeded (200), 8 hit transient
`SSL_ERROR_SYSCALL` through the agent proxy (forcing `--tlsv1.2` improved but did not eliminate this; consistent
with scout R's 24 Sept note that this host "needed 1-3 attempts, all eventually 200" — logged here for the next
worker rather than retried further); `sok.riksarkivet.se`/`lbiiif.riksarkivet.se` 1 direct fetch (no captcha this
time, static project page, no search query submitted); `api.openalex.org` 1 (429, network-wide budget spent);
`api.semanticscholar.org` 1 (429); `www.diva-portal.org` 2 (connection reset both times, not retried further);
`github.com` 2 shallow clones (dbourdeau/cyphersolver, aaymeloglu/unsolved-ciphers, grepped, not committed);
WebSearch 6; WebFetch 2 (`sok.riksarkivet.se/oxenstierna`, github wiki page). No logins, no credentials, no
subagents, no decoding, no novelty wording, no promotion.

## Image check, design, control and reading (LANE R worker R3, 24 September 2026)

Brief `.claude/briefs/runs/2026-09-24-lane-r-w1-solver.md`. Cryptanalytic result: no key source, no known plaintext.

**Step 1, image over OCR.** Letter 602 runs over three printed pages, not two: p.821 = leaf n830, p.822 = n831,
p.823 = n832 (the extraction note's "n831 = p.821" was off by one; n832 carries the last three cipher lines, the
dateline and the editor's note on the item). Images in `images/` with `manifest.json` (sha1, size, URL). Every printed
line was read against the image into `verified_lines.txt`; `build_verified.py` tokenises it and writes
`ciphertext_verified.tsv`, recording each difference from `tokens.tsv` (column `change_from_ocr`, 24 rows). Changes
that touch cipher tokens: `26.24` is two groups, 26 and 24 (printed with a stray dot); `11` is printed `ll`, a letter-sign
(twice, 822.19 and 822.32); `1102 J` is `1102½`; `O` after "när" is a `0`; p.823 line 1 `33` is `32`, and line 2 `76` is
`75`. The marks are kept: `65"` (7 times, reads ö) and `72°` (3 times, reads å) are distinct signs. The rest are
clear-word OCR repairs (som, till, måge, sambla ...). Token counts: 733 numerals (694 of them ≤100, 59 values plus the
two marked variants; 39 above 100, 30 values), 38 letter-signs (r, rr, nn, ee, gg, ll, u, d, aa, H, t, n, W, mm, 0),
208 clear words. The editor's note on p.823 says the original is a "tripplet" (a triplicate copy) on a quarto leaf,
with a "duplett" and a "triplett" to Gustaf Horn of the same day, meant to be read by the Chancellor too.

**Step 2, design.** The numerals ≤100 are a letter cipher with light homophony: IoC 0.044 (plain Swedish is about
0.064), the top 22 values carry 84% of the tokens, 17 values are hapax, and 26 alone is 12.4% (e). Runs of 1 to 39
letter symbols sit between clear Swedish words with no word division. Repeated trigrams (47 26 32 ×7, 44 62 80 ×5,
72 28 27 ×4) behave like Swedish letter strings. The groups above 100 (198-5152, 30 values, 3 repeat) break the letter
runs where a name or word would stand: a nomenclator. The printed letter-signs (r, rr, nn ...) sit where signs stand
in the manuscript; unread.

**Step 3, matched control first.** `solve.py control`: letter 604 (Gustav Adolf to Oxenstierna, Nürnberg 1 Aug 1632,
in his own hand, Swedish with Latin, same volume) laid onto the target's exact token layout (same 208 clear-word slots,
same letters per run, one word per code or sign slot), enciphered with a homophonic key that copies the target's
rank-frequency profile (61 letter values). Language model: the letter 4-gram model of `tools/subst_hillclimb.py`
trained on the same volume's djvu text with letters 602 and 604 removed (å, ä → a; ö → o; i=j; u=v). The solver
anneals value→letter maps (at most 6 values per letter) with the clear words fixed as context. It ran 8 restarts of 3M
iterations, blind.
Control: **98.0% of the 694 letter tokens correct** (solver −1.730 per token; the true key scores −1.741; a
shuffled-ciphertext null scores −1.878). `control_result.json`.
Target, same settings (`solve.py target`, `target_result.json`): best −1.599 per token against a shuffled null of
−1.778. All 8 restarts land within −1.600 to −1.608, and the output is Swedish.

**Reading.** `make_key.py` writes `key.tsv` from the annealed key plus 12 hand corrections, each from a crib in the
solver's own output (listed with the crib in `make_key.py`: 62=u from "kunne" ×3, 50/49=c from "och" and
"retranchera", 72°=å from "på foten", "påkomma", "åter", 65"=ö from "följa", "förste", 38=x from "bevuxen", 99=å from
"advancera åt det närmeste", and so on). `decode.json` + `tools/decode_key.py . --check` regenerates `reading.txt` /
`reading_tokens.tsv` and exits 0. Grades over 771 cipher tokens: **H 0, C 0, S 665, M 29, I 0, U 77** (S = letter
value seen ≥3 times, the class the control reads; M = rarer values; U = the 39 codes and the 38 letter-signs, not read).
Phrases that read clearly (normalised spelling): "icke mindre bakefter oss i ett godt positeur än här oppe"; "måge komma
opå medh thet aldraförste"; "hvardera ett [code] complett"; "anhålla hos [code]"; "någen annen god officerer";
"sambla någre [code]"; "både till att följa [code] på foten, så väl som till att resistera hvad som uhr [code]
påkomma kan"; "eder numera [codes] tilsamman"; "vele advancera åt det närmeste"; "allting [code] långsampt";
"medel som vij giorde vid Mitou [Mitau]"; "uhr det enare retrancherede"; "för än I veta hvar ... kunne antreffa";
"deran lände eder retranchera kunne"; "allestedes är medh höglar bevuxen"; "behöfve till att retranchera eder
allestädes rundt omkring"; "correspondere och flitige medh her Johan[?] Banér"; "kund göra oss hvad eder lider";
"sakerna"; "Sparre ... stött"; "allenest [codes] i [code] stark"; "slette bussar"; "alla vara complette"; "desse
höra en deel under Holcken, en deel under andra"; "deres ankompst"; "eder marche"; "avantage". In short, the King tells
Oxenstierna to join forces with Banér and the others, to entrench wherever he halts on the march, and gives news of the
enemy's regiments (Holk). Letter 601 of 21 July, in clear, gives the same orders ("at I sambla först ... ther fatta en
god posto och eder retrenchere"). The name after "her" at 821.05 (`17 81 26 24 8 96 99 [205] 70 51 26 27 44 26`)
reads "Stee.. [code] Bielke", probably Sten Bielke (named in letter 604), with 8 and 96 unresolved (M). Unresolved
stretches (kept as the key gives them, graded by value count): "omlopalath", "mistaboetium", "som droged [code]
tneder", "enore", "Tirskas", "befruell r stutta", "lw".

**Not done / suggestions (one line each).** The 39 codes (30 values) need the key or a parallel text: the Horn
"duplett"/"triplett" of the same day (REQUEST.md, Horn-Bielkesamlingen E 2348/E 2350) would give a second copy of the
same codes. A second reader should settle the M stretches from context. The printed letter-signs need the manuscript
(Riksarkivet), because the edition's r/rr/nn are its own stand-ins for signs.

**Search log for LANE V (what the solver checked; no novelty classified).** Earlier workers' logs above: the edition's
own footnote (the editor found no key); Konung Gustaf II Adolfs skrifter (Styffe 1861) does not print the letter;
Irmer 1888 has one unrelated hit; WebSearch; Cryptiana, CATALOG.md and LANDSCAPE.md (0 hits); Bourdeau and Aymeloglu
(no folder); DECODE through Aymeloglu's cached sweep (no row). sok.riksarkivet.se/oxenstierna sits behind a captcha and
was not searched. Unreachable on 24 Sept 2026: OpenAlex, Semantic Scholar, DiVA, the Waldispühl paper. This session ran
no new novelty search (brief: do not classify novelty). Phrases for the verifier's phrase search: "bakefter oss i ett
godt positeur", "vid Mitou", "höglar bevuxen", "retranchera eder allestädes rundt omkring", "en deel under Holcken".

**Requests this session:** archive.org 4 (3 page images, 1 djvu text), all 200, ≥2 s apart. No other host, no subagents, no logins.
