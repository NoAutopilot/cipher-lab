# Oxenstierna, Gustav II Adolf to Axel Oxenstierna, Nürnberg 23 July 1632

**Status: open**

## Item

Letter from King Gustav II Adolf (Gustavus Adolphus) to Rikskansler (Chancellor) Axel Oxenstierna, dated
"Nürnberg den 23 Julij" [1632] (printed "Anno 1682" is an OCR digit slip; Gustav Adolf died November 1632 and
the letter discusses the Nürnberg campaign and Banér). Printed in *Rikskansleren Axel Oxenstiernas skrifter och
brefvexling* (C.G. Styffe's second series), letter no. 602, pp. 821-822. Internet Archive identifier
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

**Verdict: open.** No solution, key, or documented prior attempt found on this specific letter in six sources
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
