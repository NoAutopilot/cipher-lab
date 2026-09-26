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
