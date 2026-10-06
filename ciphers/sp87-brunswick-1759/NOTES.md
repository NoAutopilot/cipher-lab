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

## Check-solved addendum (GF4-BATCH12 (account-4), 3 Oct 2026)

Standard edition and pages actually read: the verdict on line 2 stands -- Westphalen's *Geschichte der Feldzüge des Herzogs
Ferdinand von Braunschweig-Lüneburg* (Google Books lEYIAAAAQAAJ 1871 and WtIFAAAAQAAJ 1872, full-text searched for three
sample items, LANE CX2 25 Sept 2026). Added this pass: the HMC lead from round 2 re-run by Google Books full-text API
(`"Krosdorff" Holdernesse Ferdinand`, `"Prince Ferdinand to Lord Holdernesse"`, `"commander of the allied forces in Germany,
Lord Holdernesse"`; key + country=US, 3 Oct 2026): the 3rd Report of the HMC (1872; 3_sUAAAAQAAJ, 9sULAQAAIAAJ and five other
scans of the same appendix) calendars a run "between Prince Ferdinand of Brunswick, as commander of the allied forces in
Germany, Lord Holdernesse, Secretary of State, and the King, relating to the military operations" (entries for Windeken 14
Apr 1759, Ziegenhayn 27 Apr 1759, Krosdorff 7 Nov 1759, and a 24 June 1756 King of Prussia paper); the owning collection's
heading did not appear in any snippet, so it is still unidentified. One-line calendar entries, no cipher text, no
decipherment. And a sibling lead from the same searches: HMC *Rutland* vol. 2 (1889; euULAQAAIAAJ and five other scans)
calendars Granby's received despatches of 1760 with their contents ("Holdernesse to the Marquess of Granby. 1760, August 26.
Whitehall. Despatch, chiefly in cypher ... Prince Ferdinand's message requesting reinforcements ..."), so the Granby side of
the 1759-62 correspondence is calendared from the recipients' deciphered copies. None of this cluster's 98 cipher-flagged
items was matched to a printed full text. Status unchanged: **open**.

## Web and blog check (GF4-BATCH12 (account-4), 3 Oct 2026)

WebSearch, 3 Oct 2026: (1) `Prince Ferdinand of Brunswick Holdernesse cipher letters 1759 1760 deciphered` -- TNA Discovery
item pages (C9164991 Korbitz 29 Sept 1759, C9205728, C9187983), a QRH museum Warburg page, a BL Untold Lives post on ciphers in
BL manuscripts (2016, general), BL Add MS 32708 (Newcastle Papers catalogue); no decipherment or transcription of an SP 87
item. The hit "Ferdinand reading page ... aaymeloglu/unsolved-ciphers PR #6" is **Emperor Ferdinand III, 1634-40**, not this
Ferdinand -- checked in a fresh clone (d2800bb, 27 Sept 2026): folders `ferdinand-1634`, `ferdinand-1635-1640` only. (2)
`"SP 87" Ferdinand Brunswick cipher decipher Granby 1760` -- TNA item pages (SP 87/37/12, SP 87/32/104, SP 87/32/115), an
academia.edu PDF "Volume 2: 1759-1760: The Operations of the Allied Army under the command of Prince Ferdinand of Brunswick"
(a modern translation/study; academia.edu is 403 from the cloud, not opened -- see While waiting), allthingsliberty's 1780-81
cipher article (unrelated). (3) site-restricted to **Cipherbrain** (scienceblogs.de), **Cipher Mysteries** and **Cryptiana**
(blogspot and web.fc2), `Ferdinand Brunswick Seven Years War cipher` -- only Klausis Krypto Kolumne's 2017 post on Thomas
Ernst's Ferdinand III decipherment (a different Ferdinand); no post on this cluster, so no comment thread to read. Not found
on the open web.

## Premise check (GF4-BATCH12 (account-4), 3 Oct 2026)

(a) Folder's own mentions of a decipherment: **found, unreachable as images** -- the round-1 sweep already lists period
clear-text decipherments filed as companion pieces: SP 87/36/10 ("Decyphered Part of Prince Ferdinand's Letter of the 11th
October 1759", companion of 36/9), SP 87/40/77 (an incomplete period decipherment of Bute's 5 June letter, 40/69), SP
87/40/122-124 (deciphered intercepted enemy letters, with 40/121). Those items are calibration material (period plaintext
exists beside them), not unsolved targets; TNA digitised=false for all, so not opened. The other ~92 flagged items are not
yet paired. (b) Other solvers' working files: **not found** -- fresh clones 3 Oct 2026, Aymeloglu d2800bb and Bourdeau
4aedb40, grepped for brunswick/holdernesse/granby/"SP 87": Aymeloglu has only DECODE catalogue rows for BL Add MS 32270
(Brunswick-Wolfenbüttel keys, 1719-1763, R8011-R8020, a different holding and series) and Bourdeau only SP 87/24/33 (del
Puerto, 1748, outside this cluster). (c) Physical neighbours: **unreachable** (not digitised); catalogue neighbours are the
companion pieces in (a). (d) Recipient's side: **partly found** -- Westphalen prints from Ferdinand's own archive (the
recipient of Holdernesse's and Bute's letters; three samples absent, LANE CX2); HMC 3rd Report calendars a second
Ferdinand-Holdernesse run (collection unidentified); HMC Rutland vol. 2 calendars Granby's deciphered copies. No full
recipient-side text of a sampled item located. Status stays **open**.

## While waiting (3 Oct 2026, GF4-BATCH12)

Waits on: TNA page copies of the six paired items (REQUEST.md, ASKS row 57).

- S (FT4, 3 Oct 2026; R8-SPS2 6 Oct: API snippets only, addressee/date still open): read Westphalen 1871 (Google Books CUoSqn-TycQC, full view) at the "composition secrète ...
  Ehrenbreitstein" passage and record addressee and date against SP 87/36/9 (11 Oct 1759) -- a browser page read, no
  login, no payment (books.google page view is captcha-blocked only from the cloud).
- S: identify the HMC 3rd Report collection that calendars the Ferdinand-Holdernesse run -- read the 1872 report's appendix
  table of contents on archive.org/Google Books full view (search "Ziegenhayn" in the full-view volume 3_sUAAAAQAAJ and read
  the section heading above it), then check whether that collection's items duplicate any cipher-flagged SP 87 piece by
  date -- no login, no person.

Requests this pass (3 Oct 2026): googleapis.com/books 5, archive.org 2 (advancedsearch, no hit), github.com 2 (shallow clones,
shared with the other two targets of this batch). WebSearch 3.
Gate re-run (GF4-BATCH12, 3 Oct 2026): `sp87-brunswick-1759: open (line 1) -- edition/page or full-text-search citation found within 6 lines`, exit 0 (was exit 1: no Web and blog check section). `tools/next_steps.py --wait-only | grep sp87-brunswick`: no line.

## FT4-sp87-brunswick-1759 (3 Oct 2026, account-4)

Step run (GF4-BATCH12's premise lead): are the period-decipherment calibration items online or printed with cipher AND
decipherment, and are they in the target's key/design?

**Design prior: non-test.** `tools/design_prior.py` needs a token stream; this folder holds no `ciphertext.txt` (no SP 87
cipher leaf has been transcribed or imaged -- every item is digitised=false, below). Office prior instead, from
KEY-DESIGN.tsv / KEY-OFFICES.tsv: no key on file from the 1740s-1770s at all (decades on file jump from 1720s to 1780s),
and no British Secretary of State's office key later than Thurloe's 1650s set. So neither the statistics nor the office
register support any design family for this channel yet; that waits on a transcribed leaf.

**Availability, TNA Discovery API (3 Oct 2026; search by reference, then `records/v1/details/<id>`):**

| Ref | TNA id | Date | What | digitised | Same channel as target? |
|---|---|---|---|---|---|
| SP 87/36/9 | C9172233 | 11 Oct 1759 | Ferdinand to Holdernesse, section in cipher | false | yes (Ferdinand <-> SoS) |
| SP 87/36/10 | C9172234 | 11 Oct 1759 | "Decyphered Part of Prince Ferdinand's Letter of the 11th October 1759" | false | yes -- the office decipherment of 36/9 |
| SP 87/40/69 | C9272078 | 5 June 1761 | Bute to Ferdinand (ff. 150-152; office copy/draft) | (search record; not fetched) | yes |
| SP 87/40/76 | C9272109 | 12 June 1761 | Ferdinand to Bute, encloses passage that "could not be deciphered" | false | yes |
| SP 87/40/77 | C9272110 | 5 June 1761 | extract of 40/69 "which could not be completely deciphered" (ff. 172-173) | false | yes -- Ferdinand's side, partial decipherment |
| SP 87/40/78 | C9272112 | 29 June 1761 | Bute to Ferdinand, partly in cipher: "has ordered his letter of 5 June [40/69] to be enciphered in a simpler manner" | (search record) | yes -- **design evidence**: the 5 June letter used a more complex encipherment than usual, then was re-sent simpler |
| SP 87/40/121 | C9276876 | 29 Sept 1761 | Bute encloses three deciphered intercepts | false | no |
| SP 87/40/122, /123 (and /124) | C9276877, C9276878 | 30 Jul, 10 Aug 1761 | De Broglie/Choiseul intercepts, deciphered copies | false (122) | **no** -- French army/ministry cipher, a different key; not calibration for the British-Ferdinand channel |
| SP 87/4/234 | C8951001 | 1712 | intercepted letters from Namur, partly in cipher | (search record) | **no** -- 1712, wrong decade and channel; drop as a sibling |

Result (a): **none of the calibration items is digitised by TNA**; State Papers Online (Gale) is the owner's paywall -- a
REQUEST.md item, not a fetch. Result (b), key/design: the in-channel pairs are 36/9-10 (cipher + office decipherment) and
40/69 + 40/77 + 40/78 (clear office text of the same letter, Ferdinand's partial decipherment of it, and its simpler
re-encipherment) -- the second is the richer key-rebuild set, since the clear text of the enciphered passage is in the
box at the sending end. 40/122-124 and 4/234 are out of design.

**Print lead found this pass (Google Books API, keyed, country=US):** Westphalen's 1871 volume (Google Books
CUoSqn-TycQC, `ALL_PAGES`, 988 pp.) carries a French first-person Ferdinand text: "... Ehrenbreitstein par une composition
secrète avec le commandant françois. Si cela arrive, j'ay du temps de reste pour prendre encore la ville de Giessen;
peutêtre pourrai-je prendre aussi Francfort et établir mes quartiers d'hyver ..." -- the same subject as SP 87/36/10's
catalogue line ("his hopes for capturing Ehrenbreitstein"). Renouard, *Geschichte des Krieges in Hannover, Hessen und
Westfalen* (1864; LsFhAAAAcAAJ and copies) cites a Ferdinand letter "an Holdernesse, datirt aus Crosdorf 11. Oktober 1759"
on the same matter, and Mediger/Klingebiel 2011 (uV9RAQAAIAAJ, snippet) footnotes "Holdernesse, 1759 September 29 /
Oktober 11 / November 7". **Not established** whether the Westphalen text is the 11 Oct letter to Holdernesse itself or
another Ferdinand letter of those days (the snippet's neighbours mention "No. 58" and "Holdernesse me repond au sujet de la
Lettre du comte de Starem[berg]", which reads as Ferdinand writing to a third party about Holdernesse). If it is, it is a
printed plaintext for the 36/9 cipher section (an N1-shaped calibration, not a target reading). The page itself cannot be
read from the cloud (books.google page view is captcha-blocked, access table; no archive.org copy -- `bub_gb_CUoSqn-TycQC`
and `bub_gb_lEYIAAAAQAAJ` metadata empty).

Nothing fetched (no usable online cipher+decipherment pair), so no manifest. Requests: discovery.nationalarchives.gov.uk 12
(6 searches, 6 details), googleapis.com/books 7, archive.org 2. All 1.6 s apart. Vision calls 0.

## Remaining gaps (FT4-sp87-brunswick-1759, 3 Oct 2026)
Read so far: 0 of 98 cipher-flagged items read; no leaf imaged or transcribed.
- calibration pairs SP 87/36/9-10 and 40/69+77+78 - blocker: waiting-on ASKS row 57 (REQUEST.md TNA page copies; or State Papers Online access, REQUEST.md item 2); TNA digitised=false for every item, checked 3 Oct 2026
- Westphalen 1871 CUoSqn-TycQC Ehrenbreitstein passage - blocker: not-attempted; reading the page needs a browser that clears books.google's captcha; next: owner-desk/LOCAL-QUEUE page read of CUoSqn-TycQC at the "composition secrète" hit to identify addressee and date, ~$0.5
- the other ~92 cipher-flagged items - blocker: waiting-on ASKS row 57 (no images; design prior needs a transcribed leaf)

## Escalation (3 Oct 2026)
- [x] siblings: calibration items located and flagged in TNA Discovery, all digitised=false (this pass)
- [n/a] clear-pages: no leaf of this cluster imaged yet
- [x] known-keys: KEY-DESIGN.tsv has no 1740s-1770s key and no later British SoS key (this pass)
- [ ] print: Westphalen 1871 CUoSqn-TycQC passage to be read at the page (owner desk)
- [n/a] key-rebuild: needs a cipher+decipherment pair in hand first
- [n/a] image-check: no images exist from the cloud
- [n/a] retry: no failed method to retry here
Verdict: keep going: 1 internal gaps; cheapest next: read Westphalen 1871 CUoSqn-TycQC at the "composition secrète" hit (owner-desk LOCAL-QUEUE row; addressee + date vs SP 87/36/9), ~$0.5

## R8-SPS2 (a) pass (6 Oct 2026, 04:22-04:30 UTC): Westphalen 1871 "composition secrète" via Books API
googleapis.com/books/v1 with country=US and key, 7 requests (volume record 1, searches 6), books.google.com page view not used (blocked from the cloud). CUoSqn-TycQC ("Geschichte der Feldzüge des Herzogs Ferdinand von Braunschweig-Lüneburg", 1871, ALL_PAGES) is the only volume returned for the quoted phrase combined with Ehrenbreitstein. Snippets read: "...Ehrenbreitstein par une composition secrète avec le commandant françois. Si cela arrive, j'ay du temps de reste pour prendre encore la ville de Giessen; peutêtre pourrai-je prendre aussi Francfort et établir mes quartiers d'hyver..." and, in a second snippet, a header-like fragment "1759 ... No.58 ... C'est avec une joïe infinie, que j'ay lû les bonnes ..." and "Holdernesse me repond au sujet de la Lettre du comte de Staremberg". Snippets give no addressee or date line, so the match to SP 87/36/9 (11 Oct 1759) is not established; the passage reads as Ferdinand's own letter in the Westphalen print (grade I). The Books API gives no page text or page locator; the LOCAL-QUEUE row stands. Status unchanged: `open`.
