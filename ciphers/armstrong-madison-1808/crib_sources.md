# Crib/summary/decode sources for Armstrong to Madison, 20 Feb 1808 -- ARM-REC pass, 26 Sept 2026

Job: is a key, a decode, or a later summary of the letter's content extant anywhere; secondarily, any
candidate crib phrase or sibling letter in the same private code. Per CLAUDE.md rule 10, this worker reports
what was found and where it was not found; it does not classify novelty.

## Answer to the main question: no decode and no summary of content found

**The most authoritative statement on file is negative, and it is not this worker's own conclusion --
it is Angela Kreider's (editor, Papers of James Madison, U.Va.), already quoted in
`sources/cryptiana/web/madison_armstrong.htm` (re-read this pass, not re-fetched): the 20 Feb 1808 letter**
"was docketed by State Department chief clerk John Graham, but we've found no evidence that it ever was
decoded, nor that Madison acknowledged receiving it." Kreider's team has already checked this against their
own edition's materials; a fresh sweep of what is reachable from this container this pass turned up nothing
that contradicts it, and one new piece of evidence that supports it (below).

**New this pass: no abstract of the letter in the Library of Congress's own finding aid for Armstrong's
letters.** `www.loc.gov/item/mss31021a016/` ("James Madison Papers: Series 7, Addenda ... Abstracts of
letters and papers; Armstrong, John, 1804-1823") is a 17-image manuscript volume titled "Letters from John
Armstrong. 1804-1814," a chronological hand-written abstract of each Armstrong-to-Madison letter with a
one-paragraph content summary and page count, evidently made by an LC or State Department archivist for
finding-aid purposes decades later. Two page images read directly (viewer, not OCR; images at
`tile.loc.gov/image-services/iiif/service:mss:mss31021a:002:04:000{2,3}/full/pct:25/0/default.jpg`):
the sequence runs 1804 July 2 -> 1804 July 15 -> 1805 May 4 -> **1808 August 30** -> 1808 October 20 -> 1809
March 30 ... with no entry for February 1808 at all (neither 15, 20, nor 22 Feb). If this volume's compiler
had access to a decoded or otherwise readable text of the 20 Feb letter, it is not reflected in its own
abstract series -- consistent with Kreider's "never decoded." (Caveat: only 2 of 17 images were read; the
volume could resume 1804-1807 material out of order elsewhere, though the two pages read are contiguous and
strictly chronological, so a hidden Feb 1808 entry elsewhere in the same volume is unlikely, not excluded.)

**No candidate sibling letter located in DECODE's own cached listing.** Re-checked (no new fetch;
`sources/decode/records-{decrypted,non-decrypted}-2026-09-24*.tsv`, already crawled by TOMO-REPLY) for any
English-language or clearly-American numeric-code item, 1807-1809: none. Every dated item in the 1800s
decade in these files is Dutch (Nationaal Archief legations) or the unrelated Vatican item; no US diplomatic
material of any kind is catalogued in DECODE. This is a clean re-confirmation of TOMO-REPLY's "no hit,"
not a new negative.

**NARA catalog.archives.gov: unusable without the missing API key, as already documented** (Access playbook:
requires an `x-api-key`, requested by email, not set in this environment). Both the `api/v2/records/search`
endpoint and the plain `/search` UI page returned the bare React-app shell (5454 bytes, identical for both
URLs) with no server-rendered data -- confirms the existing "functionally unusable" note, not a new finding.
No M34 roll-14 item-level locator found this pass (would need the key or a differently-indexed search this
worker did not find).

## What is new: a genuine "Armstrong to Jefferson, 15 Feb 1808" letter exists -- but it is not a crib

QUEUE row 27's cheap-test sentence and TOMO-REPLY's correction to it (`NOTES.md`, "No 'Krajcovic' connects to
Armstrong... There is no 'Armstrong to Jefferson, 15 Feb 1808' letter found anywhere in this sweep") both
missed something reachable this pass: **`www.loc.gov/item/mtjbib018243/`, "John Armstrong to Thomas
Jefferson, February 15, 1808," in the Thomas Jefferson Papers at the Library of Congress** (found via the
Jefferson Papers collection search, `dates=1808`, `q=Armstrong`; not in the Madison Papers collection, which
is why an earlier Madison-only sweep would not surface it). Two page images read directly this pass
(`tile.loc.gov/storage-services/master/mss/mtj/mtj1/040/1000/{1068,1069}.jpg`, docketed "Armstrong Genl Paris
Feb 15.08 rec Apr.7"):

- **Entirely in clear** (ordinary handwritten English prose, no code groups, no cipher of any kind).
- **A short, personal letter of recommendation**, not a diplomatic despatch: it introduces the bearer, a
  sailor who had carried despatches to Talleyrand in Poland the year before, mentions Admiral La Touche
  Tréville, notes something said against the young man's morals ("food for powder... by no means one
  qualified to take charge of a school or a parish"), then turns to Lafayette's financial difficulties over
  his Louisiana land grant, and closes with the enclosed copy of a Conseil d'État act concerning M. Skipwith.
  Signed "John Armstrong. 15 Feb. 1808. Paris."
- **So this does correct TOMO-REPLY's specific claim** that no such letter exists -- one does, catalogued at
  LOC, dated the same day as the well-known Armstrong-to-Madison 15 Feb letter (Founders 99-01-02-2703,
  THE=972, ~72% coherent per Bourdeau) -- **but it is a different letter to a different recipient in a
  different register**, and it carries no cipher and no content plausibly overlapping the 20 Feb letter's
  diplomatic subject matter. It does not supply "Krajcovic's crib" (that name still connects to nothing found
  anywhere in this repository or the solver repositories, per TOMO-REPLY), and its vocabulary (personal favor,
  Louisiana land grant, Lafayette) is too far from the 20 Feb letter's evident register to serve as test 1's
  crib on its own; it is at most one more data point for a period-idiolect vocabulary prior, alongside the two
  already known (15 Feb and 22 Feb 1808 to Madison).
- **Not itself checked against the 20 Feb letter's 216 distinct values** (out of this brief's scope: this
  worker was not asked to run cryptanalysis, per CLAUDE.md's solver/verifier split).

Correction filed for the lane orchestrator: TOMO-REPLY's specific sentence "There is no 'Armstrong to
Jefferson, 15 Feb 1808' letter found anywhere in this sweep" in `NOTES.md` is **wrong on the narrow factual
point** (such a letter exists) though its broader conclusion (no Krajcovic crib, no key transplant available)
stands. NOTES.md's own text is left as TOMO-REPLY wrote it (out of this brief's file-edit scope beyond
appending); this file and the paragraph below are the correction record.

## Kreider's named "other correspondent" candidates -- checked this pass

Per Kreider (via Tomokiyo): potential recipients of coded Armstrong correspondence outside the State
Department in 1808 are Pinkney, Monroe, Erving, Livingston, or Armstrong's New York circle.

- **James Monroe Papers** (`loc.gov/collections/james-monroe-papers/`): searched `q=Armstrong`, **0 results**.
  (The collection exists and is browsable; whether it is fully text-searchable for correspondent names was
  not established -- a 0-result search here is weaker evidence than the Madison/Jefferson collection searches
  above, which returned known items correctly.)
- **George W. Erving**: searched `"John Armstrong" "George W. Erving"` across all of loc.gov, no direct
  Armstrong-to-Erving (or Erving-to-Armstrong) manuscript item found; only secondary histories ("The Purchase
  of Florida," "The West Florida Controversy") turned up, which may discuss their diplomatic relationship in
  prose but are not a located letter.
- **Robert R. Livingston**: query timed out twice on loc.gov (host went briefly unresponsive, see Requests
  below); not completed this pass.
- **William Pinkney**: not searched by name-pair this pass (time budget); Pinkney-to-Madison letters of Feb
  1808 are on file (`mjm015074`, `mjm022254`, `mjm022258`) but these are the wrong direction (Pinkney writing
  TO Madison, in the ordinary channel, not Armstrong writing to Pinkney in a private code).
- **Armstrong's New York political circle**: not searched (no names given to search by; Kreider's note names
  no specific correspondent here).

None of these four turned up a coded Armstrong letter to test as a sibling/pool. This matches the existing
NOTES.md conclusion ("none of their 1808 correspondence has been located or checked against this code") --
extended by one collection-level negative (Monroe Papers) and one name-pair negative (Erving), not resolved.

## Requests this session

web.archive.org: 1 successful CDX reachability ping (200), then 3 failed fetch attempts (connection reset
mid-exchange, confirmed via the agent proxy's own relay-failure log as a genuine host-side instability, not a
proxy misconfiguration) -- stopped per the good-citizen rule after the second failed retry; Founders Online's
own editorial notes to 99-01-02-2728, the 21 Feb-31 Aug 1808 Armstrong letter sweep, and the Madison-to-
Jefferson/Madison-to-Armstrong sweep this brief's step 1 asks for were **not completed this pass** because of
this outage. loc.gov: approximately 14 requests (Madison Papers collection x3, Jefferson Papers collection x1,
Monroe Papers collection x2, item-level metadata x2, image fetches x4, general search x2 succeeded + 2 timed
out on complex quoted-phrase queries after one retry each, per the good-citizen rule). catalog.archives.gov:
2 (API and UI, both return the unrendered app shell, confirming the existing "needs x-api-key" finding, not a
new fetch of real data). DECODE: 0 new fetches (re-read cached TSVs on disk only). No logins, no credentials
touched, all fetches >=1.5s apart, descriptive User-Agent.

## Still open for a successor

1. Founders Online's own editorial apparatus for 99-01-02-2728 (the source notes, and any note on later
   correspondence referencing this letter) -- blocked this pass by the web.archive.org outage; retry when the
   host is stable, or try `data.web.archive.org`/a different Wayback mirror path.
2. The remaining 15 of 17 abstract-volume images (`mss31021a016`) -- only pages 2-3 (of 17) were read; the
   volume nominally covers to 1814 and the two pages read do not rule out an anomalous placement.
3. Livingston-Armstrong correspondence search (timed out, not completed).
4. Whether the 15 Feb 1808 Armstrong-to-Jefferson letter (`mtjbib018243`) has a Founders Online document ID
   of its own (would need Founders/Wayback, also blocked this pass) -- if so, its editorial note may say
   whether Jefferson forwarded or discussed it with Madison.

## ARM-REC2 pass, 26 Sept 2026 -- attempted step 1 again; web.archive.org still unreachable

**Host retested, still down.** Per this job's brief ("web.archive.org answered again at 07:26"), retested at
07:29-07:32 UTC: a plain fetch of `https://web.archive.org/` (no path) and a CDX query for
`founders.archives.gov/documents/Madison/99-01-02-2728` both returned `curl: (35) Recv failure: Connection
reset by peer`, confirmed via the agent proxy's own status endpoint as `ws_closed_mid_exchange` (tunnel closed
mid-exchange, not a proxy-side fault) -- the same failure signature ARM-REC logged at 07:11, now reproduced
twice more with several minutes of real elapsed time between attempts, well past the one-retry-after-a-pause
rule. `archive.org` itself (the non-Wayback host, `advancedsearch.php`) answered HTTP 200 in the same window,
so the outage is specific to the `web.archive.org` Wayback subdomain, not Internet Archive generally. Founders
Online's own site retested once directly (`https://founders.archives.gov/Metadata/founders-online-metadata.json`,
a byte-range GET, browser UA): still the CloudFront empty-202 challenge, not retried further (per the
existing playbook note). No other Wayback mirror or Memento aggregator is reachable from this container
(`timetravel.mementoweb.org` does not resolve through the egress proxy). **Founders Online's own editorial
notes to 99-01-02-2728, and the full text of every Feb-Aug 1808 Armstrong/Madison/Jefferson letter below, are
still not fetchable this pass.** This is the second consecutive worker to find the host down; a third attempt
should wait for a parent check-in to confirm the host has actually recovered before spending more requests on it.

**Fallback route used instead: WebSearch title/index matching (not a page fetch).** Google's index carries
exact Founders Online page titles and dates even though the pages themselves cannot be fetched from this
container; this surfaces which documents exist and their document IDs, but **not** their editorial-note text
(WebSearch's own synthesized "answer" text is unreliable here -- one query's summary restated the discredited
AFIO "Decrypted Text" as if it were a real decode of the 20 Feb letter, which it is not, per Bourdeau's and
Tomokiyo's adjudications already on file above; only the titles/URLs below are treated as evidence, not the
prose summaries). Document IDs located this way, none of them fetched or confirmed against their own page
content this pass:

| Founders ID | Title (as indexed) | Collection |
|---|---|---|
| 99-01-02-2703 | To James Madison from John Armstrong, Jr., 15 February 1808 | Madison (already known, THE=972, ~72% coherent) |
| 99-01-02-2728 | To James Madison from John Armstrong, Jr., 20 February 1808 | Madison (the target letter) |
| 99-01-02-2745 | From James Madison to Thomas Jefferson, 25 February 1808 | Madison |
| 99-01-02-2907 | To James Madison from John Armstrong, Jr., 5 April 1808 | Madison |
| 99-01-02-2949 | From James Madison to Thomas Jefferson, 15 April 1808 | Madison |
| 99-01-02-2962 | To James Madison from John Armstrong, Jr., 18 April 1808 | Madison |
| 99-01-02-3082 = 99-01-02-8003 | To Thomas Jefferson from James Madison, 15 May 1808 | Madison / Jefferson (cross-listed; **new this pass**: the Jefferson-collection ID 8003 was not previously on file, only the Madison-collection 3082) -- this is the "undecyphered letter from A." letter, already quoted above from Tomokiyo |
| 99-01-02-8006 | To Thomas Jefferson from James Madison, 16 May 1808 | Jefferson -- one day after the "undecyphered letter" note; **not** a reply from Jefferson, another Madison-to-Jefferson letter; not fetched, unknown whether it continues the topic |
| 99-01-02-3466 | To James Madison from John Armstrong, Jr., 30 August 1808 | Madison (the postscript letter; content already known, see below) |
| 99-01-02-8145 | To Thomas Jefferson from John Armstrong, Jr., 15 June 1808 | Jefferson |
| 99-01-02-8708 | To Thomas Jefferson from James Madison, 18 September 1808 | Jefferson |
| 99-01-02-7420 | To Thomas Jefferson from John Armstrong, Jr., 15 February 1808 | Jefferson -- **answers this brief's Armstrong-to-Jefferson question, see below** |
| 99-01-02-7484 and 99-01-02-7514 | both indexed once each as "To Thomas Jefferson from James Madison" for late Feb 1808 (one search returned "25 February 1808" for 7484, a separate search returned "29 February 1808" for 7514) | Jefferson -- **the two dates may be a search-snippet conflation, not two confirmed distinct letters; unresolved, flag only** |

No editorial-note text, no letter body, and no confirmation of a reference to the 20 Feb letter, a duplicate,
or a changed cipher was obtained for any row above (title/date only). **This table is a fetch list for a
successor once web.archive.org recovers, not a completed sweep of step 1.**

**Armstrong-to-Jefferson, 15 Feb 1808 (this brief's specific question): Founders Online does print it, and no
part of it is in cipher.** `99-01-02-7420` ("To Thomas Jefferson from John Armstrong, Jr., 15 February 1808",
Jefferson Papers) is indexed with title and paraphrase content matching, word for word close, ARM-REC's own
direct read of the loc.gov manuscript (`mtjbib018243`): the messenger who had carried despatches to Talleyrand
in Poland, Admiral La Touche Tréville, and Lafayette's Louisiana land-grant difficulties. This is the same
letter as loc.gov's item, now with its Founders Online document ID identified (not previously on file); ARM-REC's
own direct manuscript read already established it is entirely in clear (no cipher, no code groups), so this pass
adds only the Founders cross-reference, not a changed answer -- **no part of the 15 Feb Armstrong-to-Jefferson
letter is in cipher**, confirmed independently by the primary-source read, not by the (unverified) Founders title
match alone.

**30 Aug 1808 postscript: code and first groups (from Bourdeau's page, already on disk, no host needed).**
Bourdeau's own write-up (`sources/cryptiana/blog/dbourdeau-cyphersolver-armstrong.html`, already fetched by
ARM-REC, re-read here) answers this without needing Founders/Wayback at all: the postscript is in **THE=972**,
Armstrong's ordinary office code with Madison (the *same* code that reads the 15 Feb and 22 Feb letters at
~72% and ~90%+, and *not* the unknown code of the 20 Feb letter). Founders Online prints the groups
undeciphered as Early Access document **99-01-02-3466**. Bourdeau's own transcription of the first line
(quoted exactly): "1394. 1116. 1273. 250. 1165. 1405." -- decoding (per his table) to "Ru-s-s-el ought to"
(1394=Ru inferred from three independent alphabetical-neighbour checks, 1116=s from the known-plaintext 1806
letter, 1273=el inferred, 250=ought inferred, continuing into the next line "970.[=the, Founders misprints
"970" for the manuscript's "972"] 148. 1459. 1482. 1201. 821. 130. 821." Bourdeau's full decoded postscript
(49 groups, 48 determined, one probable slip): "Russel ought to be the consul: he is an American by birth, and
is much better qualified than any other candidate. In a word, he is above men in general. Next to him in
fitness is O'Mealy, but he is, like Warden, an Irishman[-re, one digit short of 'man']." This is the private
letter recommending a candidate (John Russel, over David Bailie Warden and one O'Mealy) for the Paris consular
post -- unrelated in subject and code to the 20 Feb letter, but it is the one Armstrong-Madison cipher passage
from 1808 that has actually been read, and Bourdeau's own page states plainly that Founders prints it
undeciphered and no full decipherment was found in archive, print, or online before his own recovery.

## Requests this pass (ARM-REC2)

web.archive.org: 3 failed (connection reset, host outage persists, confirmed via the agent proxy's own
relay-failure log, not a proxy fault) -- stopped per the good-citizen rule, no further attempts this pass.
founders.archives.gov: 1 (the metadata JSON, byte-range, browser UA; empty CloudFront 202, not retried, matches
the existing playbook note). archive.org: 2 (one `advancedsearch.php` confirming the host is up generally, one
broad keyword search that returned noise and was not pursued further). www.archives.gov: 1 (the Founders
Online metadata dataset page, confirms the JSON dump is metadata-only -- titles/dates/ids, not editorial-note
text -- so it would not have answered this brief's question even if fetchable). WebSearch: 7 queries (title/ID
lookups per the table above). No DECODE, no logins, no credentials touched.

## Still open for a successor (updated)

1. Every document ID in the table above needs an actual fetch (via Wayback once it recovers, or Founders
   Online directly if its own CloudFront challenge ever clears for scripts) to read its editorial notes and
   body text -- this pass only located titles/dates, not content.
2. 99-01-02-7484 vs 99-01-02-7514 (both "Madison to Jefferson", late Feb 1808, two different dates from two
   different searches) needs a direct fetch to resolve which date is correct and whether they are the same or
   different letters.
3. Jefferson's own reply to Madison's 15 May 1808 "undecyphered letter" note (99-01-02-3082/8003) has still not
   been located; 99-01-02-8006 (16 May, Madison to Jefferson again) is the nearest candidate by date but is not
   confirmed to touch the topic.
4. The 21 Feb-31 Aug 1808 Armstrong-to-Madison/Madison-to-Armstrong sweep (this brief's own step 1) is only
   partially covered by the table above (5 of the roughly 15-20 letters in that window that Founders is likely
   to hold); a successor with web.archive.org access should step through Founders' own per-correspondent index
   pages rather than guessing document-ID titles one at a time via WebSearch.

## ARM-REC3 pass, 26 Sept 2026 (LANE ARM worker ARM-REC3) -- Founders apparatus via Wayback (host now up), loc.gov Armstrong pool, Livingston/Pinkney

**Step 0, reachability: web.archive.org is up this pass**, unlike the two consecutive outages ARM-REC/ARM-REC2
found. `curl` to the bare root returned HTTP 200 and a CDX query returned real snapshot rows immediately. Fetches
of individual documents remained intermittently unstable (a `Connection reset by peer` / `SSL_ERROR_SYSCALL` on
roughly half of all first attempts, confirmed host-side via the same signature ARM-REC/REC2 logged, not a proxy
fault), but every document below succeeded on a retry after a short pause (one retry after a pause is this
project's own limit; in practice 1-3 retries, several minutes apart in aggregate, were needed across the batch --
recorded honestly, not glossed as "one clean pass"). **The host has recovered enough to be usable, just not
reliably enough for a single-attempt policy; a successor should expect to retry roughly half of all fetches.**

**Step 1: Founders' own editorial apparatus for 99-01-02-2728 (the target letter itself) -- there is none beyond
the source citation.** Fetched via its own latest Wayback snapshot (20260117203945). The Early Access page prints
the full body (matching `ciphertext.txt` at a glance: same opening groups "453. 240. 760. 1480. symbol / 35. 681.
1752. 1841. 1314." etc., same closing "5. 760. 47. 38. 580. 170.") and, below it, only the source line: **"DNA: RG
59—DD—Diplomatic Despatches, France."** No footnote, no editorial note, no cross-reference to any other letter, no
comment on the cipher at all -- this Early Access page carries no annotation apparatus whatsoever, consistent with
Kreider's own "we've found no evidence that it ever was decoded" (already on file) and with this being flagged
Early Access (not the final annotated volume). This directly answers this brief's step 1 first clause: there is no
"source note and footnotes" to quote beyond the bare archival citation.

**The 13-id table, fetched and read (9 of 13; resolves the 7484-vs-7514 question; nothing found bearing on the
20 Feb letter):**

| Founders/loc.gov id | Date | Content (read directly) | Bears on the 20 Feb letter / cipher? |
|---|---|---|---|
| 99-01-02-2745 = 99-01-02-7484 | 25 Feb 1808, Madison to Jefferson | "the grounds of a message communicating Pinkney's & Armstrong's letters ... Armstrong's letter is in the hands of General Dearborn." | No cipher mention; **confirms 7484 and 2745 are the same letter, cross-listed between the Madison and Jefferson collections, not two distinct letters** -- resolves this brief's named open question |
| 99-01-02-7514 | 29 Feb 1808, Madison (Sec. of State) to the President, for the Senate | A formal report on impressed-seamen statistics (Nos. 1-13 of returns from Gen. Lyman, London agent) | **A genuinely distinct letter from 7484/2745**, different date, different subject (routine Senate report) -- resolves the "search-snippet conflation" flag: they are not the same letter |
| 99-01-02-2907 | 5 Apr 1808, Armstrong to Madison | not fetched -- CDX query itself timed out 3 times (host instability, distinct from the fetch-stage resets above), stopped per the good-citizen rule | unknown |
| 99-01-02-2949 | 15 Apr 1808, Madison (Sec. of State) report to the President | Concerns the source and date of an extract in Armstrong's 22 Jan 1808 letter (unrelated to 20 Feb) | No |
| 99-01-02-2962 | 18 Apr 1808, Armstrong to Madison | Quotes a forwarded letter from Mr. Lear re Algiers/tribute troubles -- wholly in clear | No |
| 99-01-02-3082 = 99-01-02-8003 | 15 May 1808, Madison to Jefferson | The already-quoted "undecyphered letter from A." passage, confirmed verbatim; **also**: "I send letters from Armstrong, Pinkney & Harris" in the same letter -- Armstrong's and Pinkney's dispatches were routinely forwarded to Jefferson together | Confirms the already-known quote; the Armstrong+Pinkney pairing is routine mail-handling, not evidence of a cipher between them |
| 99-01-02-8006 | 16 May 1808, Madison to Jefferson | "There are letters from Erving but old & not worth forwarding" -- Erving named as an active correspondent being forwarded through Madison at exactly this date, one day after the "undecyphered letter" note | No direct link to the 20 Feb letter or a cipher, but corroborates Erving as a live, contemporaneous correspondent (Kreider's own candidate list) |
| 99-01-02-8145 | 15 June 1808, Armstrong to Jefferson | Long, frank political letter (Floridas, war preparations) -- wholly in clear, no code | No |
| 99-01-02-8708 | 18 Sept 1808, Madison to Jefferson | "Letters from Armstrong & Ervine recd." forwarded together again; also "Marat's[sic] dispatches to Turreau were in reality put under Irvine's[sic] cover to the Dept of State" (i.e. one correspondent's mail is sometimes physically carried under a different correspondent's cover) | No cipher mention, but a second instance of Armstrong+Erving being handled as a pair, and evidence that dispatches were sometimes routed under a different name's cover -- relevant background for "one concerted with another correspondent" |

Not fetched this pass: 99-01-02-2907 (CDX timeout, see above). No document among the 9 read makes any reference to
the 20 Feb letter, a duplicate of it, a changed or private cipher, or names a specific correspondent for one --
consistent with Kreider's "never decoded" and with nothing in this apparatus discussing the letter at all.

**Step 2: loc.gov independent search -- 14-item pool built and screened, all page-1 thumbnails read clear;
Livingston and Pinkney name-pair searches done.**

Full table in `pool/LOC-ARMSTRONG.tsv`. Searched the James Madison Papers and Thomas Jefferson Papers collections
separately (`?q=Armstrong&dates=1807/1809&fo=json`) rather than RG 59/M34 (already covered by ARM-POOL): Madison
Papers returned 28 hits (8 genuine Armstrong-Madison correspondence items in the window, the rest addenda/finding-
aid volumes); Jefferson Papers returned 32 hits, of which **13 are direct Armstrong<->Jefferson correspondence
items, 1807-1809** -- a standing, multi-year private correspondence channel between Armstrong and Jefferson
running parallel to, and independent of, the official Armstrong-Madison State Department channel. This channel is
**not named in Kreider's own list of candidate "other correspondents"** (Pinkney, Monroe, Erving, Livingston, the
New York circle) but is real and dated back to March 1807, well before the 20 Feb 1808 letter.

Fetched page-1 (or nearest small-thumbnail page) images for 14 of these items via `tile.loc.gov` (the "q"/service
thumbnails, ~460-600px wide, well under any per-host size concern) and had one Sonnet subagent classify each
page's visible content as clear_text / numeral_code / code_with_marks, per this brief's step 2. **Result: all 14
read clear_text -- no numeral groups visible on any of the 14 pages checked.** This is a page-1-only sample (2
of the 14 items run to 10-12 manuscript pages; only the first page of each was checked), so it does not rule out
a coded passage appearing later in a longer letter the way the target's own cipher groups begin only after the
opening word "The" -- but it is a real negative at the granularity checked: **no candidate sibling coded letter
found in either collection's Armstrong correspondence, 1807-1809, on the pages sampled.**

Two same-date items (`mjm015148`, Armstrong to Madison, 20 Oct 1808; `mtjbib019197`, Armstrong to Jefferson, 20
Oct 1808) are flagged but not resolved this pass -- possibly the same letter cross-filed, possibly two genuinely
distinct letters Armstrong wrote to his two correspondents on the same day; a successor should compare their
content directly.

**Livingston name-pair**: `"John Armstrong" "Robert R. Livingston"` as a free-text site-wide query returned 605
hits of pure noise (unrelated Washington/Monroe/Livingston-family material, no date filtering available on the
site-wide endpoint) -- not usable. Narrowed to the Madison Papers collection with `q="Robert R. Livingston"`,
`dates=1807/1809` (no "Armstrong" term, since the combined query returned 0): **5 genuine Livingston-to-Madison
letters in the window** (22 Mar 1807, 17 May 1807, 8 Jan 1808, **5 Feb 1808** -- fifteen days before the target
letter -- and 24 Jan 1809), confirming Livingston was an active correspondent with the State Department in this
exact period. None of these is Livingston<->Armstrong directly (they are Livingston<->Madison, the ordinary
channel), and none was fetched for content this pass (out of this brief's step 2 scope, which asks only for the
name-pair search, not a content read) -- flagged for a successor as the most promising unread lead: a Livingston
letter timed 15 days before the target's letter is worth reading for any reference to Armstrong or a private
cipher.

**Pinkney name-pair**: `"William Pinkney" Armstrong` in the Madison Papers collection, `dates=1807/1809`: **0
hits.** Broadened to `"William Pinkney"` alone (same collection/dates): 43 hits, all Pinkney<->Madison (the
ordinary Britain-legation channel) or Pinkney<->third-party (Robert Smith, George Joy) -- no direct
Pinkney<->Armstrong item found. This matches ARM-REC's own earlier finding (Pinkney-to-Madison items already on
file, wrong direction) and extends it to a genuine 0-hit direct-pair search: **no Armstrong-Pinkney correspondence
located in the James Madison Papers.**

## Requests this pass (ARM-REC3)

web.archive.org: 1 root reachability check (200) + CDX queries for 11 document ids (2 timed out after retries:
99-01-02-2907's CDX itself, twice) + document fetches for 9 ids (each needed 1-3 attempts due to intermittent
resets, all eventually succeeded). loc.gov: 2 collection searches (Madison Papers Armstrong, Jefferson Papers
Armstrong) + 14 item-metadata `?fo=json` fetches + 2 Livingston-name-pair queries + 2 Pinkney-name-pair queries +
1 spot item-metadata fetch (mjm015063, not pursued further) = 21. tile.loc.gov: 14 thumbnail image fetches. All
>=1.5s apart, descriptive User-Agent, no logins, no credentials touched.

## ARM-LIV pass, 26 Sept 2026 (LANE ARM2 worker ARM-LIV) -- the five Livingston-to-Madison letters, content read

ARM-REC3 (above) located the five Livingston-to-Madison letters in the loc.gov Madison Papers window (1807-09) via
`q="Robert R. Livingston"&dates=1807/1809` but did not read them (out of that pass's scope). This pass re-ran the
same query (confirms the same 5 loc.gov item ids and dates) and read all five for content, per this job's brief.
Full table in `pool/LIVINGSTON.tsv` (item_id, date, founders_id, pages, route, class, note).

**Route**: tried the Founders Online text (via Wayback) first for each, prioritizing 5 Feb 1808. WebSearch for the
exact Founders document id succeeded for only 2 of 5 (17 May 1807 = `99-01-02-1698`; 24 Jan 1809 = `99-01-02-3948`);
for the other 3 (22 Mar 1807, 8 Jan 1808, 5 Feb 1808) two targeted WebSearch queries each returned only nearby/
unrelated Founders documents, never the exact id, so per this brief's step 3 fallback those three were read from
`tile.loc.gov` page images instead (thumbnails for all pages; the one letter with a cipher-relevant passage, 22 Mar
1807, was also fetched at native resolution for a legible read of the passage in question). A CDX query attempting
to find the Founders "search all correspondence between Madison and Livingston" listing page (which might have
supplied the missing 3 ids in one fetch) failed twice with `Recv failure: Connection reset by peer` -- the same
web.archive.org instability ARM-REC/REC2/REC3 already logged -- and was not retried further (one retry after a
pause is this project's limit).

**Result: all five letters are wholly ordinary correspondence -- clear text throughout, no numeral groups on any
page, no reference to any cipher, key, or private correspondence between Livingston and Armstrong.** None
corroborates the "sibling code" hypothesis (family E). Two letters are worth flagging even though neither bears on
Armstrong's own cipher:

- **22 Mar 1807** (`mjm014713`, no Founders id located) discusses the Burr conspiracy (Aaron Burr's "plans," their
  "total defeat," General Wilkinson, and co-conspirators Bollman and Swartwout) and contains a genuine period
  "cypher" reference -- but about the already-public Wilkinson/Burr cipher, not Armstrong's: **"What folly led him
  to write in cypher without having previously settled a key? And by what means has his letters been deciphered?
  These are enigmas which I cannot unriddle."** (read directly off the native-resolution page image, p1). This is
  Livingston commenting on the 1807 Burr trial's own already-solved cipher correspondence (Wilkinson's own
  decipherment of Burr's letter was public trial evidence by this date), unconnected to the 20 Feb 1808 target.
- **8 Jan 1808** (`mjm015043`, no Founders id located) asks Madison to forward a personal letter to Livingston's
  family in France "with your dispatches," citing "keeping open the intercourse with Genl Armstrong" -- the
  ordinary diplomatic pouch to the Paris legation, not a private cipher or key. p2 discusses the Embargo's hardship
  on Americans in Europe.
- **5 Feb 1808** (`mjm015063`, no Founders id located; the letter fifteen days before the target and this brief's
  priority item): a routine office-seeking recommendation (a Mr [Philip?] Livingston for a seamen's-agent post at
  Jamaica) plus congratulations on Madison's election as President. No mention of Armstrong, a cipher, or a key at
  all.
- **17 May 1807** (`mjm014751`, Founders `99-01-02-1698`) and **24 Jan 1809** (`mjm015230`, Founders
  `99-01-02-3948`): personal/domestic matters (a son-in-law's passport request and NY election politics; a Merino
  wool sample sent as a gift), no cipher or Armstrong mention.

**Reading: family E's Livingston lead is closed as a negative** (a search result, not a control-backed test --
this is a "no coded passage found" screen, not a shuffle test, rule 3) -- the five letters in the window contain no
cipher, no key reference, and no mention of Armstrong beyond the ordinary diplomatic-pouch channel. This does not
touch WE027 (Livingston's own unpublished code per Weber 1979, NOTES.md line 96), which remains untested for lack
of a reachable table, not because of anything found this pass.

Requests this pass: loc.gov 1 collection search (`?q="Robert R. Livingston"&dates=1807/1809&fo=json`) + 5
item-metadata `?fo=json` fetches = 6. tile.loc.gov: 7 page-thumbnail fetches (`...q.jpg`/`...dq.jpg` pattern) + 1
native-resolution fetch (22 Mar 1807 p1, `0600d.jpg`) = 8. web.archive.org: 2 CDX queries (both succeeded) + 2
document fetches (both succeeded on the first attempt) + 1 CDX query that failed twice (connection reset, not
retried further) = 5. All >=1.5s apart, descriptive User-Agent, no logins, no credentials touched. No subagent
used (7 small page images read directly, cheaper and simpler than a classification call for this volume).
