open
Westphalen's correct-year volumes (Google Books lEYIAAAAQAAJ, 1871, "Urkundlich Nachträge ...
1757-59. 1760. 1761. 1762", ALL_PAGES; WtIFAAAAQAAJ, 1872, ALL_PAGES) full-text searched by this
worker for three cipher-flagged items dated 23 Nov 1759, 2 Jul 1760 and 1 Jan 1762 (control
phrases "Ehrenbreitstein"/"1759" and "Clavering"/"Landgrave de Hesse" both hit, confirming the
search reaches genuine in-volume content for the right years); none of the three items' content
found there.

## Check-solved (LANE CX2, 25 Sept 2026)

Round-2 check-solved on this cluster's own request: "Pick three cipher-flagged items spread across
1759-62 ... and look each up in Westphalen by date." Building on the round-1 sweep (23 Sept 2026)
below, which left the Westphalen check open because only archive.org's volume 1 (1859) had been
found and it does not cover the relevant years.

**Three items chosen**, fetched by TNA Discovery API item-level record (exact reference, dates,
descriptions quoted verbatim, TNA's own text):
1. **SP 87/36/26** (TNA id C9172332), **23 Nov 1759**: "Holdernesse to Prince Ferdinand of
   Brunswick (all in cipher): the king considers Ferdinand's letter of 7 November so important
   that he has communicated it to his most trusted ministers. They have reco[mmended]..."
2. **SP 87/39/7** (TNA id C9233845), **2 Jul 1760**: "Clavering to Holdernesse, mostly in cipher:
   the landgrave's fears that he will be of no consequence after a peace. Mr. Assenbourg's
   influence on him. Donop wishes the affair of Hanau might be settled."
3. **SP 87/44/6** (TNA id C9391293), **1 Jan 1762**: "Clavering to Bute in cipher on the reasons
   for the landgrave of Hesse's decision to leave Hamburg. Shortcomings of the landgrave's
   character. Dated at Brunswick."

**Westphalen check.** Confirmed by archive.org metadata (`geschichtederfe01unkngoog`, the only
volume on archive.org under this title, 3 copies) that this volume is **vol. 1 (1859), covering
1756-1758 only** ("Bd. 1-2 ... Entstehung und Geschichte des hannöverischen Krieges, 1756-1758" —
read from the item's own front-matter OCR via `archive.org/metadata`), so it cannot contain any
of the three dates by construction; confirmed independently by full-text search
(`be-api.us.archive.org/fts/v1/search`, 2 requests): "Minden" gives 1 hit, about the French
*capture* of Minden in March (1758), not the 1 Aug 1759 battle that a volume covering 1759 would
certainly mention repeatedly, and "Clavering" gives 0 hits (already logged round 1). Located (not
on archive.org, not previously found) via Google Books search (5 requests,
`googleapis.com/books/v1/volumes`, `&country=US&key=$GOOGLE_BOOKS_KEY`) the volumes that *do*
cover the right years: **lEYIAAAAQAAJ**, "Geschichte der Feldzüge ... Urkundlich Nachträge ...,
zusammengestellt aus Materialen des Nachlasses von C. H. P. von Westphalen, und des
Kriegs-Archivs des Herzogs Ferdinand: 1757-59. 1760. 1761. 1762" (1871, `viewability: ALL_PAGES`,
public domain, 990 pages) and **WtIFAAAAQAAJ** (1872, `ALL_PAGES`), neither held by archive.org
(checked: no `bub_gb_lEYIAAAAQAAJ`-pattern copy, and an archive.org title search for "Feldzüge
Ferdinand Braunschweig" returns only the three vol.-1 copies already known). Google's reader
itself is bot-challenged (`books.google.com/books?id=...&q=...` redirected to
`google.com/sorry/index`, one attempt, not retried per the good-citizen single-retry rule), so
read these volumes only via the Books API's cross-corpus full-text search, which does index and
return real snippets from them: control search "Ehrenbreitstein Ferdinand 1759" hits lEYIAAAAQAAJ
with a snippet dated 1759 mentioning Ehrenbreitstein, and control search "Clavering Landgrave
Hesse" (via the neighbouring "Clavering, ministre accredité auprés du Landgrave de Hesse" snippet)
hits WtIFAAAAQAAJ dated a 21 April 1762 letter — both controls confirm the search genuinely reaches
these two volumes' 1759-62 content, not just their title metadata. Targeted searches for each of
the three chosen items' own distinctive terms found **no hits in either volume**: item 2's
"Assenbourg Donop Hanau" returned 0 total hits anywhere in Google Books; item 3's "Clavering
Hamburg landgrave" returned 6 hits, none from a Westphalen volume; item 1's "Ehrenbreitstein
Ferdinand 1759" and "Krosdorff Ferdinand Holdernesse" hit lEYIAAAAQAAJ but only for unrelated 1759
passages (a different, French-language exchange, not this letter's "communicated to his most
trusted ministers" content). Read as: **checked, not found** in the two Westphalen volumes that do
cover 1759-62 — this is a real, controlled negative for these three items in this edition, not an
access failure, so the folder-level verdict is `open`, not `blocked`, on the Westphalen question
specifically.

**Flag for the next worker (not chased down this sweep, out of this brief's Westphalen-only
scope):** the item-1 search surfaced the **3rd Report of the Royal Commission on Historical
Manuscripts** (1872, Google Books id `3_sUAAAAQAAJ`, `ALL_PAGES`) calendaring a distinct
collection's correspondence between Prince Ferdinand of Brunswick and Lord Holdernesse, including
"Krosdorff, 7th Nov. 1759. — Prince Ferdinand to Lord Holdernesse. Reasons for his choice of winter
quarters..." — i.e. the very letter our item 1 (23 Nov 1759) responds to, calendared in a private
collection outside TNA SP 87 (owning collection not yet identified from the snippet; the brief
named HMC reports carrying Holdernesse/Bute as a source family still to check properly). This is a
calendar entry (a one-line description), not a printed decipherment, so it does not itself resolve
solved/unsolved status for any of the 98 cipher-flagged items, but it means this correspondence run
has a second, non-TNA holding worth cross-referencing (companion/duplicate pattern, CLAUDE.md
check-solved lesson of 24 Sept 2026, Huntington La Luzerne). Not investigated further here.

**Verdict on the folder, per this brief's specific ask:** the standard edition (Westphalen) *was*
read at all three chosen dates, via a controlled full-text search across the two volumes that
cover 1759-62 (not the vol.-1-only holding archive.org has) — none of the three items' content
found there. Round 1's broader item-by-item cross-reference of all 98 cipher-flagged pieces
against in-box contemporary-decipherment companions, the Savory looser search, State Papers
Online, and the Bute Papers (Mount Stuart/NLS) key search remain undone (multi-session campaign,
per round 1). The whole-cluster caveat from round 1 stands for those, not for Westphalen, which
this sweep closes.

Requests this sweep: discovery.nationalarchives.gov.uk 4 (three item-level record fetches by
reference, one SP 87/44 cipher-flagged listing), archive.org 3 (1 metadata, 2 be-api fts),
googleapis.com/books 8 (search + two volume-info lookups), books.google.com 1 (bot-challenged,
not retried). All >=1.5s apart, one host at a time.

## Round-1 sweep (23 September 2026)

QUEUE row: N6 (sources/solver-diffs/2026-09-23-non-decode-hits.tsv, "Candidates not on DECODE").

## Source

The National Archives, Kew, **SP 87/36, 38, 39, 40, 42, 43, 44** (Secretaries of State: State Papers
Foreign, Military Expeditions — Prince Ferdinand of Brunswick), 1759-1762. TNA Discovery's own series
description (fetched via the API, `context` field): "Secretaries of State: State Papers Foreign, Military
Expeditions. PRINCE FERDINAND OF BRUNSWICK." The QUEUE row's estimate of "~90 pieces" undercounts badly:
item-level record counts fetched this sweep for the seven named pieces alone are SP 87/36: 51, /38: 119,
/39: 95, /40: 155, /42: 155, /43: 120, /44: 123 — **818 item-level records total**, of which **98 explicitly
say "in cipher"/"cypher"/"decipher"** in the TNA Discovery description (grepped locally after fetching all
seven pieces at full page size). This is a much larger cluster than scored.

## Check-solved sweep (23 September 2026)

1. **TNA Discovery API (decisive for shape, not for content).** Fetched all seven named pieces at full item
   level (`sps.searchQuery="SP 87/NN"`, `sps.resultsPageSize=250` or 200; 7 requests, one 403/reset avoided
   by the working param set found this session). Correspondents confirmed: Holdernesse/Bute (Secretary of
   State) to/from Prince Ferdinand of Brunswick (commander, allied army in Germany) throughout, and a second,
   distinct thread of Holdernesse/Bute to/from **Colonel (later Sir Henry) Clavering**, attached to the
   Landgrave of Hesse's court, from SP 87/39 on. A sample of the 98 cipher-flagged descriptions (quoted
   verbatim, TNA's own text): "Holdernesse to Prince Ferdinand of Brunswick (all in cipher): the king
   considers Ferdinand's letter of 7 November so important..." (SP 87/36/26); "Clavering to Holdernesse,
   mostly in cipher: the landgrave's fears..." (SP 87/39/7); "Bute to Clavering, mainly in cipher, continuing
   to reprimand him..." (SP 87/42/143). Several items show that **a contemporary decipherment already sits
   in the same box, filed as a separate piece**: SP 87/36/9 ("he has written to the duke his brother
   following the commission the king has entrusted to him [section in code or cipher translated in SP
   87/36/10]") is paired with SP 87/36/10, itself catalogued as *"'Decyphered Part of Prince Ferdinand's
   Letter of the 11th October 1759': his hopes for capturing Ehrenbreitstein..."* — i.e. the government's own
   18th-century clear-text decipherment, not a modern reading. Likewise SP 87/40/76 ("encloses a passage [SP
   87/40/77] from Bute's letter of 5 June [SP 87/40/69] which could not be deciphered") pairs with SP
   87/40/77 ("Extract from Bute's letter to Ferdinand of 5 June which could not be completely deciphered") —
   a period *failure*, honestly catalogued as such; and SP 87/40/121 ("enclosing copies of three intercepted
   enemy letters which have been deciphered [SP 87/40/122-124]") is a genuine period cryptanalytic success
   against an *enemy* cipher, filed with its plaintext alongside. This pattern (contemporary decipherment
   filed as a companion piece) is the same shape check-solved found in the SP 35/36 Atterbury cluster
   (`ciphers/sp35-intercepts-1722/NOTES.md`, 23 Sept 2026) — there it meant the target was already solved in
   1723; here it means an unknown fraction of the 98 cipher-flagged items already have their own
   contemporary clear-text companion in the same box, cheaper to fetch than any fresh cryptanalysis. Which
   fraction is not established this sweep — would need item-by-item cross-referencing of all 98 against
   their neighbours, out of budget here.
2. **Print — Westphalen.** Archive.org holds **only Volume 1 (1859)** of E. von Westphalen, *Geschichte der
   Feldzuge des Herzogs Ferdinand von Braunschweig-Luneburg* under this title (3 copies: `geschichtederfe
   01unkngoog`, `bub_gb_agwPAAAAYAAJ`, `bub_gb_OcoFAAAAQAAJ`; 1 advancedsearch request). Full-text search
   inside it (`be-api.us.archive.org/fts/v1/search`, 3 requests) for "Clavering" (0 hits), "Holdernesse" (1
   hit), "Landgrave" (1 hit) shows this volume covers years before Clavering's Hesse mission (1760-61) and
   barely touches Holdernesse — i.e. it predates most of our cipher-flagged material (1760-62). Volumes 2-6
   (1863-72), which would cover the relevant years, were **not found on archive.org under this title** and
   are not checked; HathiTrust not queried this sweep (known Cloudflare-class block per CLAUDE.md, not
   retested). This is the edition risk the brief named and it is genuinely open, not resolved.
3. **Print — Savory.** Archive.org advancedsearch for `title:(His Britannic Majesty Army in Germany)
   creator:(Savory)`: 0 results (1 request). Not found under that query; not retried with a looser query
   this sweep.
4. **State Papers Online (Gale).** Not reachable (paywalled, per the brief); not checked via web search for
   a coverage statement this sweep — flagged as unchecked, not negative.
5. **Community lists.** `sources/cryptiana/web/` grepped for "SP 87"/"sp87"/"Prince Ferdinand"/"Clavering"/
   "Holdernesse": no file matches any of these terms. `unsolved.htm` (Tomokiyo's own unsolved-cipher list)
   read in full: no Seven Years War Germany material at all, English or otherwise. WebSearch for `SP 87 Bute
   Prince Ferdinand Brunswick cipher decipher Cipherbrain OR Cryptiana Seven Years War`: no results tying
   this series to any cipher blog or research post (1 query).
6. **DECODE.** Cached catalogue grepped for "SP 87"/"Ferdinand.*Brunswick"/"Clavering"/"Holdernesse": no
   hit. This domestic-government material (like SP 35 and PRO 30/55) is outside DECODE's European-manuscript
   scope.
7. **Bourdeau / Aymeloglu.** `cs-recheck/*.md` and `ay/*.md` grepped for "SP 87"/"Brunswick"/"Clavering": no
   direct hit (a "Brunswick" match in `cs-recheck/README.md` is an unrelated item — the Balbases-Fuenmayor
   letters mention a "Brunswick claim to ambassador rank" as a topic inside a different, already-solved
   cipher; not this series).

Requests: discovery.nationalarchives.gov.uk 13 (7 full item-level fetches + 6 earlier probes/retries, one
malformed-param 500 not counted against the good-citizen budget since it never reached the server
meaningfully). archive.org 4 (1 advancedsearch for Westphalen, 1 for Savory, 3 be-api full-text searches —
grouped as one host total of 4 distinct endpoint calls plus 3 fts calls = 7 archive.org-family requests).
cryptiana.web.fc2.com: 0 live fetches, local snapshot only. WebSearch: 1 query.

## Edition risk

**Open, not resolved (Westphalen leg closed by LANE CX2 round 2, 25 Sept 2026 — corrected LANE CX2 25 Sept
2026: the 1760-62 volumes are NOT unlocated; they are on Google Books, not archive.org, as
lEYIAAAAQAAJ/WtIFAAAAQAAJ, see the round-2 section above, and a controlled full-text search of them for
three sample items found nothing).** Westphalen's Geschichte is the obvious print candidate and volume 1
does not cover the relevant years. Savory not found on archive.org. State Papers Online's SP 87 coverage is
unchecked. Until Savory, State Papers Online and the item-by-item cross-reference against in-box
decipherment companions are checked, no individual item in this cluster can be called either "already
printed" or "verified unsolved" with confidence — the whole-cluster verdict below is conditional on that
remaining gap, not a clean stage 2.

## Verdict (round 1, superseded on the Westphalen point by the round-2 section above)

**Open. Stage 2, verified unsolved (conditional, narrowed by round 2: Westphalen is now checked at three
sample dates and closed — see above; Savory, State Papers Online SP 87 coverage, and item-by-item
cross-reference of the ~98 cipher-flagged pieces against their in-box contemporary-decipherment companions
remain unchecked).** No solution, key, or attempt found in web search, print, community lists, DECODE,
Bourdeau or Aymeloglu. Not "new"; not "unpublished" — those words are unavailable at this stage under rule
10 regardless.

## Next

Before any fresh cryptanalysis: (1) a Savory check by a looser search, and a State Papers Online coverage
check; (2) for the specific pieces already paired with an in-box period decipherment (SP
87/36/9-10, SP 87/40/76-77, SP 87/40/121-124, and likely more among the 98 not individually checked here),
simply transcribe the companion decipherment piece — this is retrieval, not cryptanalysis, and is far
cheaper than a joint solve; (3) the Bute Papers key search the QUEUE row named (Mount Stuart/NLS) is
unattempted; (4) the round-2 HMC 3rd Report lead (a non-TNA holding calendaring at least the 7 Nov 1759
Ferdinand-to-Holdernesse letter) is worth identifying and reading in full — it may calendar or print more
of this correspondence than TNA SP 87 alone. Given the true size (818 items, 98 cipher-flagged, likely more
once every piece and every volume 1759-62 is scanned), this is a multi-session campaign, not a single
check-solved sweep — score and budget it accordingly before promoting to the board.
