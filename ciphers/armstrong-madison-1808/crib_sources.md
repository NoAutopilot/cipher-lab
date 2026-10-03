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

## H70 context crib sheet (ARM-A-H70, 3 Oct 2026)

Worker ARM-A-H70 (LANE-ARM-A, account 1, session_01VXG4dyHsuCJvU991UoLBjF), 19:22-19:41 UTC by `date -u`. Brief
`.claude/briefs/runs/2026-10-03-acct1-arma-h70-crib.md`. **Context only: no scoring of the target, no decoding, no
reading, so no grades (rule 4 not applicable).** What the 20 Feb 1808 letter most plausibly talks about, built from
what Armstrong wrote and was told in the weeks around it. Scoring any of this against the ciphertext is LANE-ARM-B's.

**Material (all under `h70/`, fetched once):**
- Founders Online Early Access transcriptions (PJM-SS series, no editorial notes printed for any of these items --
  every page's apparatus is the bare "DNA: RG 59--DD--Diplomatic Despatches, France" source line): the whole
  "More between these correspondents" Armstrong<->Madison chain from 12 Nov 1807 to 25 June 1808 (27 items: 25 Armstrong
  to Madison, Madison to Armstrong 8 Feb and 2 May 1808) and the Armstrong<->Jefferson chain 28 Oct 1807 to 28 July 1808
  (5 items). Walked by `h70/crawl.py` (headless Chromium, `tools/browser_fetch.js`; the Founders API and plain curl
  answer 202/403 CloudFront). Extracted text in `h70/letters.txt`, index with URLs in `h70/letters.tsv`,
  `h70/chain_madison.tsv`, `h70/chain_jefferson.tsv`; the raw HTML was kept out of the repo (re-fetch with
  `python3 h70/crawl.py`).
- American State Papers, Foreign Relations vol. III (Gales & Seaton 1832), IA `americanstatepap_o03unit` (Pittsburgh
  scan; the other three "v.3" ASP items on IA are other classes), `_djvu.txt` pp. 247-252 cut to `h70/asp_fr3_excerpt.txt`
  (No. 216, France: the despatches of Jul 1807-Aug 1808 that Jefferson sent to Congress).
- On disk already: Bourdeau's THE=972 decodes of the 15 and 22 Feb 1808 letters (`tools/data/uscodes-1800/decodes/`,
  dbourdeau/cyphersolver, MIT, credited there); `tools/data/en18` (Madison *Writings* VIII, Jefferson *Writings* IX,
  Ford ed.); line B's B15 read of the 22 Feb postscript (`line-b/NOTES.md`).
- Counts: `h70/cribs.py` (offline; the target 99-01-02-2728 excluded from every count; numeral groups and editorial
  brackets stripped, so a word only inside a THE=972 passage is not counted) -> `h70/crib_counts.tsv` (Nov 1807-June
  1808, 32 Armstrong letters: 30 to Madison, 2 to Jefferson), `h70/crib_counts_jan_mar.tsv` (Jan-Mar 1808, 12 letters:
  11 to Madison + 15 Feb to Jefferson), `h70/formulas.tsv` / `h70/formulas_jan_mar.tsv` (opening words, closing
  formula verbatim, the 12 words before it).

### (1) Timeline, Nov 1807 - Apr 1808

| Date | What | Source |
|---|---|---|
| 12 Nov 1807 | Armstrong's letter to Champagny on the Nov 1806 (Berlin) decree; Champagny's answer extends it to the high seas (the *Horizon* case) | ASP FR III 247; Founders 99-01-02-2320 |
| 15 Nov 1807 | Emperor leaves Fontainebleau for Italy/Spain/Portugal; Portugal "taken from the Braganzas"; **US "to be invited to make common cause against England"**; Russia's adhesion not yet ascertained; distance as the argument against a European coalition; "the demarcation of Louisiana, or the transfer to us of the Floridas" -- France "has done, I fear, all you have to expect from her" | 99-01-02-2332 (Triplicate) |
| 24 Nov / 1 Dec 1807 | Champagny (Milan) to Armstrong: US tolerates British search, blockades, impressment, so must allow French reprisals; "take with the whole continent the part of guarantying itself" | ASP FR III 247-8; 99-01-02-2382 |
| 17 Dec 1807 | Milan decree (the "December 1807" decree in every later letter) | 99-01-02-2472 and after |
| Dec 1807 (Washington) | US Embargo Act (described in Madison's 8 Feb letter; its news reached Paris by 22 Feb 1808, below) | ASP FR III 249 (Madison 8 Feb) |
| 27-29 Dec 1807 | Copy of "a second and very extraordinary decree" by Mr. McElhonny; Talleyrand (T______d) disapproves but dare not object (THE=972); Emperor expected in Paris on the 31st; P.S.: the Emperor wished to seize the Portuguese royal family; Minister of Marine's order holding vessels of "friendly and allied powers" in port; 29 Dec: England accepts Austrian mediation | 99-01-02-2472; ASP FR III 248 |
| 13 Jan 1808 | Vessel embargo meant for allies only ("the word neutral crept into it merely by mistake"); Champagny's answer on the 17 Dec *arrêté*: captures "in the nature of detentions", released if the US excludes British commerce; Austrian peace mediation failed; "The Emperor's views seem to be seriously turned towards Spain. I labor most diligently the adjustment of our disputes with that power"; repeats his 15 Nov advice ("The measure ... ought not to be delayed") | 99-01-02-2560; ASP FR III 248 (dated 22 Jan there) |
| 15 Jan 1808 | Champagny's note: "War exists, then, in fact, between England and the United States; and His Majesty considers it as declared"; American prizes "remain sequestered" pending the US decision | ASP FR III 248-9 |
| 27 Jan 1808 | Emperor's special decision confiscating the *Julius Henry* and *Juniatta* (reported 22 Feb) | 99-01-02-2733 |
| 2 Feb 1808 | French take Rome; 1 Feb Junot proclaims a provisional government of Portugal | 99-01-02-2733 |
| 3 Feb 1808 (about) | Champagny verbally repeats his 15 Jan assurances to Armstrong ("seven days" after 27 Jan) | 99-01-02-2733 |
| 8/18 Feb 1808 (Washington) | Madison's instruction: a formal remonstrance against the decrees; explain the embargo as precaution; Erskine's communication of the British Orders of 11 Nov; Hamburg/Bremen/Holland/Leghorn vexations. **Reached Armstrong only on 26 March (by Lt. Lewis)** -- not known to him on 20 Feb | ASP FR III 249-50; 99-01-02-2678; 99-01-02-2907 |
| 13-14 Feb 1808 | Armstrong to the Minister of Marine on the *James Adams* (13th); his "2d letter of the 14th of February" to Champagny (unanswered by 28 Feb); a letter to Champagny of the 16th is cited on 2 Apr | 99-01-02-2709, -2758; ASP FR III 251 |
| **15 Feb 1808** | **Special messenger** (the seaman recommended to Jefferson the same day). THE=972 passages, Bourdeau's decode: France offers "the blessings of equal [alliance?]" with one hand and menaces war with the other; "and with both they pick our pockets"; "a cession of the Floridas and settlement of a [western boundary]" as the price; "In either case, do not suspend a moment the seizure of the Floridas"; encloses Erving's last letter; "Our business here has taken ... an extraordinary turn, and will require on your part some extraordinary measures" | 99-01-02-2703; `decodes/armstrong_1808-02-15.txt`; Jefferson 99-01-02-7420 |
| 17 Feb 1808 | Minister of Marine's answer (prizes at sea not covered by the forbearance promised for vessels in port); King of Holland's "outlawry of our Commerce" ("omitted mentioning in my letter of the 15th") | 99-01-02-2709; ASP FR III 250 |
| **20 Feb 1808** | **The target.** Clear frame: "Paris 20th feby 1808 / Sir, / The" + 369 groups and 35 shorthand passages + "I have the honor to be, sir, with very high consideration, your most obedient & very humble servant / John Armstrong" | 99-01-02-2728; `ciphertext.txt` |
| 22 Feb 1808 | By Mr. Patterson: "Nothing has occurred here since the date of my public dispatches (the 17th. inst.)"; council of administration -- Emperor "highly indignant", decrees "should suffer no Change", "the Americans Should be compelled to take the positive character, either of allies or of enemies"; 160 sequestered cases, >100 million francs; Russia to seize Finland, France & Denmark Sweden; Prince of Ponte Corvo in Holstein; Charles V, the Sound and the Dardanelles; the Pope, Rome, Junot in Portugal, 150,000 French in Spain; P.S.: another attempt on "the two offensive decrees" next Wednesday; "The news of the Embargo came in good time -- by verifying one of my predictions, it gave new weight to others" | 99-01-02-2733; ASP FR III 250-1; line-b B15 (frame 0035) |
| 28-29 Feb 1808 | Audience with the Prince of Benevento (Talleyrand); cases *Vermont* (Capt. Lyman), *Speculator*, brig *Edward*, *Charleston Packet* (retroactive operation of the December decree); agents of prize causes, Skipwith's fees | 99-01-02-2758, -2761 |
| 5-9 Mar 1808 | Five notes to the Foreign and Marine ministers unanswered; "Friday" (THE=972) note; 6 Mar: report that the King of Spain will abdicate, Russia presses French mediation with the Porte; 8 Mar: Emperor would consent to an exception from the November decree; Hamburg sequestration raised, Hamburg/Bremen to furnish 2,000 seamen | 99-01-02-2780, -2781, -2798 |
| 15-26 Mar 1808 | Note on the exception given to Talleyrand; notes of the 19th and 20th to Champagny (certificates of origin, Hamburg); French army reported in Madrid | 99-01-02-2818, -2871 |
| 5-25 Apr 1808 | Formal remonstrance of 2 Apr presented; Emperor leaves for Spain; Lewis sent via Falmouth; Murat in Madrid; 17 Apr order to seize all American vessels; Napoleon refuses to acknowledge Ferdinand | 99-01-02-2907 ... -2994; ASP FR III 251-2 |
| 2 May 1808 (Washington) | Madison acknowledges "your several letters of 27th of December, 22d of January, 15th and 17th of February" -- **not the 20th or the 22nd**; Jefferson the same day: "be more frequent & full in your communications with us" | ASP FR III 252; en18 Jefferson *Writings* IX 193-4 |
| 15-20 May 1808 | Madison: "The undecyphered letter from A. ... No such Cypher is in the office"; Graham forwards a "Duplicate ... in Cypher" with a postscript | 99-01-02-3082; 99-01-02-3101 (line-b B15) |

### (2) Ranked crib list (for LANE-ARM-B to test; nothing here is scored)

Rank is this worker's judgement of how likely the word or phrase is to occur *inside the coded body*, from (a) the
topics of the five days on either side (15, 17, 22 Feb), (b) how often Armstrong uses it, and (c) whether he would
think it worth hiding (the THE=972 letters show what he chose to encipher: Talleyrand's private views, the Floridas,
the French price for an alliance, Danish/Swedish/Russian moves). Counts: letters containing it in clear, Jan-Mar 1808
(of 12) / Nov 1807-June 1808 (of 32), and total clear occurrences in the 32.

| Rank | Crib | Why | Jan-Mar / all (hits) | Numerals that could travel with it |
|---|---|---|---|---|
| 1 | Emperor (also "His Majesty", "H. M.", "Napoleon") | subject of nearly every despatch; 22 Feb's two facts are both the Emperor's acts | 5/12, 15/32 (25); H.M. 2/12, 4/32 (11); Napoleon 1/12, 4/32 (7) | -- |
| 2 | Florida / the Floridas | 15 Feb's coded close ("seizure of the Floridas", "cession of the Floridas"); always enciphered or private, hence 0 in clear Jan-Mar | 0/12, 2/32 (6) in clear; 1 coded occurrence 15 Feb (Bourdeau) | -- |
| 3 | decree(s) of November 1806 / December 1807 | the standing grievance; named as a pair in 22 Feb, 28-29 Feb, 5 Mar | 8/12, 11/32 (29) | 1806, 1807, "21 Nov.", "17 Dec." |
| 4 | allies / alliance / "allies or enemies" | 15 Feb coded ("equal [alliance]"), 22 Feb ("compelled to take the positive character, either of allies or of enemies"), 15 Nov ("common cause against England") | 2/12, 4/32 (5); enemy 1/12, 3/32 | -- |
| 5 | England / Great Britain / British | the other belligerent; Champagny's "war exists in fact" | 3/12, 8/32 (25) | "11 November" (British Orders) |
| 6 | Spain (Spanish, King of Spain, Prince of Asturias) | 13 Jan "views ... seriously turned towards Spain"; 22 Feb 150,000 French in Spain; 15 Feb boundary/cession is a Spanish question | 4/12, 11/32 (25) | 150,000 |
| 7 | war | 15 Feb coded (menace of war), Champagny 15 Jan | 2/12, 4/32 (4) | -- |
| 8 | Champagny ("Mr. Champagny", "the Minister of Foreign/Exterior Relations") | his 15 Jan note and verbal assurances, Armstrong's notes of the 14th and 16th | 4/12, 7/32 (9) | 15 January, 14th, 16th |
| 9 | Prince of Benevento / Talleyrand (written T______d in clear 27 Dec) | the 15 Feb Jefferson letter names Talleyrand; 27 Dec enciphered Talleyrand's private opinion; audience 28 Feb | 3/12, 5/32 (5) | -- |
| 10 | sequestered / sequestration / confiscated / captured | 22 Feb (160 cases, *Julius Henry*, *Juniatta*), 17 Feb (*James Adams*) | sequest 7/12, 10/32 (16); confisc 3/12; captur 5/12 | 160; 27 January; 100 millions; ship names |
| 11 | embargo | 13 Jan (the French vessel embargo); news of the US Embargo arrived by 22 Feb | 3/12, 8/32 (9) | -- |
| 12 | Russia, Sweden, Denmark, Finland, Prussia, Austria | 22 Feb's survey of Europe (coded: "Russia ... assists him in accomplishing one half of the object") | Russia 2/12, 5/32 (12); Sweden 2/12; Denmark 1/12; Austria 2/12 | -- |
| 13 | Portugal, Rome, the Pope, Junot, Holland | 22 Feb and 17 Feb | Portugal 1/12 (5 hits in 32); Holland 1/12 | 1st and 2nd (Feb) |
| 14 | "our business" / "our affairs" / "this Government" / "the United States" (U. S.) | his stock nouns for the subject (15 Feb "Our business here has taken ... an extraordinary turn") | our business/affairs 3/12; this Government 2/12; U. S. 2/12, 9/32 (11) | -- |
| 15 | "the 15th" / "the 17th instant" / "my letter of the" / "my last letter" | he opens by citing his previous letter in 13 Jan, 17 Feb, 15 Mar, 26 Mar, 6 Jun; the target follows letters of the 15th and 17th | Nth instant 5/12, 9/32 (10); my (last) letter 2/12, 5/32 (7) | 15, 17 (instant) |
| 16 | enclosed / inclosed / subjoin / copy | most despatches forward a copy | 7/12, 15/32 (17) | -- |
| 17 | messenger / conveyance / dispatch | 15 Feb special messenger, 22 Feb Mr. Patterson | messenger 2/12; conveyance 1/12; dispatch 4/12, 11/32 | "twelve hundred francs" (15 Feb) |
| 18 | Erving (Irving), Pinkney, Skipwith, Monroe, Livingston | named correspondents; Madison's "concerted with another correspondent" | Erving 1/12; Skipwith 2/12; Pinkney 0/12, 2/32 | -- |

Caveat that governs the whole list: Madison wrote that the cipher "must be one concerted with another correspondent"
and that the letter was "probably misaddressed". If so, the body may be a private letter (to Monroe, Livingston or
another), and the despatch topics above are a prior, not a constraint. Against that, see (3): the clear frame is
Armstrong's *official* despatch frame, not his private one.

### (3) Armstrong's opening and closing formulas (the structural cribs)

From `h70/formulas.tsv` (32 letters, Nov 1807-June 1808; the target excluded), verbatim where quoted.

- **Salutation.** "Sir," in all 30 to Madison that carry one; "Dear Sir," in both to Jefferson (15 Feb, 15 Jun 1808).
  The target has "Sir," -- the official form.
- **Closing.** The target's clear closing is "I have the honor to be, sir, with very high consideration, your most
  obedient & very humble servant". Armstrong's closing variants in the 32 (counts of letters):
  - "I have the honor to be[,] [Sir,] with very high consideration, your most obedient [&] [very] humble Servant"
    -- 15 Nov 1807 (exact: "I have the honor to be Sir, with very high consideration, your most obedient, & very humble
    Servant"), 18 Nov, 29 Feb, 15 Mar, 26 Mar 1808 (the last three end "your most Obedient [humble] Servant"); with
    "very great respect" / "much respect" instead: 27 Dec, 13 Jan, 31 May, 6 Jun. "I have the honor to be" in 12 of
    32 letters (5 of 12 Jan-Mar).
  - "I am, Sir, with very high consideration, ..." / "With very high consideration, I am Sir, ..." -- 5 Mar, 5 Apr,
    12 Apr, 15 Apr, 23 Apr, 25 Apr.
  - "... and am, Sir, With very high [respect and] consideration, ..." (the formula grows out of the last sentence)
    -- 29 Nov, 1 Dec 1807, 15 Feb 1808.
  - "With the highest respect, I am, Sir, ..." 17 Feb; "... believe me to be with the highest consideration, ..."
    22 Feb; private: "with the truest attachment and respect, D Sir" (Jefferson, 15 Feb).
  - "with very high consideration" (or "very high respect and consideration") in 17 of 32 letters, 5 of 12 Jan-Mar;
    "most obedient" 22/32; "humble servant" 17/32.
  **Structural consequence for the cipher (an inference, not tested):** in 11 of the 12 letters where "I have the
  honor to be" occurs, it begins a new sentence (the preceding word ends a sentence; 27 Dec lacks the stop in the
  Founders text but has it in ASP FR III 248; the exception is 25 Jun, "With very high respect, Sir, I have the honor
  to be"): e.g. 13 Jan
  "... it may be readily relinquished. I have the honor ..."; 15 Mar "... The channel thro' which my information comes
  is correct."). So the target's last coded group (`170.`) most probably closes a sentence, and the clear closing does
  not continue a coded "and am". Where the closing *does* grow out of the text ("and am, Sir," 3 letters; "believe me to
  be" 22 Feb) the formula starts "with ...", not "I have the honor to be".
- **What precedes the closing (the last coded sentence, by analogy):** often a short summing-up or a forward look:
  "If found unnecessary, it may be readily relinquished." (13 Jan); "Our's, in being more temperate, will not, I flatter
  myself, be less firm." (17 Feb); "This Short Statement Sufficiently indicates the course we ought to take." (15 Feb,
  mid-letter); "To neither of those Notes have I yet received an answer." (5 Mar); "The channel thro' which my
  information comes is correct." (15 Mar); "we can only do our duty by preparing for the worst." (6 Jun).
- **Opening.** The target's first word, in clear, is "The". Armstrong's body opens with "The" in 6 of 32 letters:
  "The Emperor left Fontainebleau yesterday" (15 Nov), "The enclosed copy of a letter from the Prefect of ..." (18 Nov),
  "The conjecture offered in my last letter with regard to ..." (13 Jan), "The conversation alluded to in the copy of
  the letter ..." (9 Mar), "The writer of the letter appended to this note ..." (8 Apr), "The St. Michael arrived at
  l'Orient ..." (25 Jun). Four of the six continue with a reference to an earlier letter or an enclosure within the
  first ten words. Other first sentences cite the last letter directly: "I Stated in my last letter ..." (15 Mar), "My
  last letter was of the 15th. inst." (26 Mar), "In my letter of the 16th. ultimo ..." (6 Jun). Note: the target's
  coded body begins immediately after "The" (`453. 240. 760. 1480.`), so if Armstrong enciphered from the second word,
  the code's first value is a noun or adjective of a "The ___" subject.
- **Dateline.** "Paris 20th feby 1808" matches his ordinary form ("Paris 15 february 1808", "Paris 22 february 1808",
  "Paris 29 Feby. 1808"); an ordinal in the dateline is less usual (28th Oct, 15th Nov, 22d Dec 1807 only).
- **Numbers in clear.** Armstrong writes dates and sums in clear around the THE=972 passages ("the 17th. inst.",
  "1806", "twelve hundred francs", "150,000 men"); Bourdeau's two decodes on file (15, 22 Feb) contain no enciphered
  date or sum. Inference from those two letters only: a numeral in the target's body is more likely a code value than
  a literal date.

### (4) Searched and not found

- **No editorial note on any of the 32 Founders items** fetched (Early Access: source line only), so PJM-SS's
  annotation for Jan-Mar 1808 is not online; the printed PJM-SS volume for 1808 was not reached (no IA/HathiTrust copy
  searched this pass; Founders prints PJM-SS text as Early Access).
- **No letter from Armstrong to Madison dated 18-19 or 21 Feb 1808** in the Founders chain (sequence 15, 17, 20, 22,
  28, 29 Feb), and none to Jefferson between 15 Feb and 15 Jun 1808.
- **22 January 1808** is printed in ASP FR III as an extract dated 22 Jan; the Founders chain has the same text as
  **13 January** (99-01-02-2560) and no separate 22 Jan item -- either ASP misdates it or a second copy was dated the
  22nd; not resolved (it does not bear on the target).
- **ASP FR III prints no extract of the 15 Feb (coded) or 20 Feb letters**; the 22 Feb extract stops at "... that you
  will immediately take your's", omitting the coded survey of Europe. Madison's 2 May acknowledgement lists 27 Dec,
  22 Jan, 15 and 17 Feb only.
- **Madison to Armstrong between 8 Feb and 2 May 1808:** none in the Founders chain; the 8 Feb instruction (with an
  18 Feb continuation) was the only one in transit at the target's date and had not arrived.
- **Founders API** (`/API/docdata/...`): 202 to curl, CloudFront 403 to the headless browser -- not usable; document
  pages work through `tools/browser_fetch.js`.
- Not searched this pass: Monroe's papers for an Armstrong letter of Feb 1808 (H71/H72 and ASKS 97 cover the
  catalogues), Brant's *James Madison: Secretary of State* narrative (no full text found to grep), newspapers.

Requests this pass: founders.archives.gov 40 (38 document pages + 1 curl API 202 + 1 browser API 403, headless,
one at a time, 2 s apart); archive.org 7 (2 advancedsearch, 4 metadata, 1 djvu.txt); be-api.us.archive.org 4. Log in
`h70/requests.log`. No subagents, no vision calls.

## H76 French-side context (ARM-A-H76, 3 Oct 2026)

What Napoleon told Champagny to tell Armstrong in the weeks around the 20 Feb 1808 letter, and what the Paris police
noted. Sources in `sources/h76/`. Nothing scored here; quotes are short, translations ours.

| Date | Item | Source |
|---|---|---|
| 12 Jan 1808 | Napoleon to Champagny (No. 13446): "Repondez a M. Armstrong" that the US will surely declare war on England over its decree of 11 November; Napoleon regards war between England and America as declared from the day England published its decrees; American vessels stay under sequestration. | *Corresp. Napoleon* XVI 244 |
| 2 Feb 1808 | Napoleon to Champagny (No. 13516): tell the American minister **verbally** that if war comes between America and England and Americans send troops into the Floridas to help the Spaniards against the English, he would approve; and let him glimpse that if America made a treaty of alliance and "cause commune", Napoleon would intervene with the court of Spain to obtain the cession of the Floridas to the Americans. | XVI 301 |
| 9 Feb 1808 | Police bulletin, Paris rumours: H.M. has ordered the American government to send away the English minister; the Emperor is to cede colonies to the Americans. | Hauterive IV, bulletin 9 Feb, item 101 |
| 11 Feb 1808 | Napoleon to Champagny (No. 13545): write to the American minister, answering his letters of the **4th and 8th**, that France's treaty with America rests on "free ships, free goods" ("le pavillon couvre la marchandise"); "Sa Majeste a traite avec l'Amerique independante et non avec l'Amerique asservie"; submitting to the English decree of 11 Nov gives up the flag's protection; if Americans treat it as an act of hostility, H.M. "est prete a faire droit a tout". | XVI 319-320 |
| 25 Feb 1808 | Police bulletin: Marseille report of 17 Feb, colonial prices up on rumour of an American-British rapprochement. | Hauterive IV, item 158 |
| 31 Mar 1808 | Napoleon to Champagny: note to the American minister that American ships carrying colonial goods really come from London; the US embargo proves they do not come from America; confiscate. Same day the *Osage* arrives at Lorient with dispatches for Armstrong. | XVI 459; Hauterive IV, bulletin 31 Mar |
| 14 Apr 1808 | Police read ~4000 letters from the US brought by the *Osage*; letters of "20 fevrier et jours suivants" (US side) say the US-British negotiation (Rose) is broken off. | Hauterive IV, item 294 and note |

Crib relevance (for LANE-ARM-B, unscored): the 2 Feb verbal message (Floridas for an alliance) is exactly the kind of
offer a minister would put in cipher; if Champagny delivered it promptly it falls before 20 Feb (inferred, not established); Armstrong's own notes of
4 and 8 Feb and the reply ordered on 11 Feb fall in the same window. Candidate words: Floridas, alliance, Spain, cession,
treaty, flag, decree(s), England, war, sequestration/sequester, verbally. This duplicates H70's ranked list for Floridas,
Spain, decrees and England and adds alliance/cession/treaty/flag.

## H75 Bowdoin (ARM-A-H75, 3 Oct 2026)

Adds no Jan-Mar 1808 clear text: Bowdoin left Paris by 26 Oct 1807 and no Armstrong-Bowdoin letter after 16 Sept 1807
is printed (NOTES.md "## H75 Bowdoin"). For the frame only: Armstrong's letters to Bowdoin (1806-07, printed in
*Bowdoin and Temple Papers* pt. II, `sources/h75/bt2_djvu.txt`) open "Sir," and close "I am, Sir, very respectfully
yrs." -- a colleague frame, not the despatch frame H70 found for the target; vocabulary in the Sept 1807 letters
(Champagny, Prince of Benevento, Florida(s), Spain, "the Emperor") overlaps H70's list and adds nothing ranked.
