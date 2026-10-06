partial
**Update, 25 Sept 2026 (parent worker FOLLOWUP-2315, L16): the two Cornwallis-to-Clinton letters that were blocking deep work (PRO 30/55/32/2 item 3689, 16 Aug 1781; PRO 30/55/33/7 item 3813, 3 Oct 1781) are both printed in B.F. Stevens, *The Campaign in Virginia, 1781* (1888), read from archive.org: text known for both, citations and page quotes in the "Stevens 1888" section below. The other six named items (2380, 2894, 3803, 3833/33 x2, 4833, 6009, 6012) are unaffected and stay at their existing footing (see "Verdict" below); status stays `partial` for the folder as a whole because most of its items remain unresolved.**
HMC Report on American Manuscripts (1904-09) read by this worker via the TNA Discovery item-level API (the calendar's own published text, across PRO 30/55/19, /24, /32, /33, /42, /53) plus a be-api full-text search across five archive.org scans of the same Report for entry "2894" (control "Clinton" confirmed the search path works; target "2894" returned no hit in any scan checked); the more specific edition for the Yorktown-dated items -- Ian Saberton, *The Cornwallis Papers* pt.11 (Naval & Military Press, 2010) -- was identified this sweep as the likely holder of a decipherment but was not opened (Google Books gives `NO_PAGES`, not on Internet Archive, not JSTOR/HathiTrust/academia.edu). GBOOKS pass (25 Sept 2026, below): Saberton's `NO_PAGES` confirmed unchanged even with `country=US`, but a separate, fully public-domain 1888 edition -- B. F. Stevens (ed.), *The Campaign in Virginia, 1781: An Exact Reprint of Six Rare Pamphlets on the Clinton-Cornwallis Controversy* -- explicitly cross-references both target letters by page number and tags the 3 Oct 1781 one `[In cypher.]`; not yet read (needs archive.org/HathiTrust, out of this worker's network scope).

## Check-solved round 2 (LANE CX2, 25 Sept 2026)

**New finding this sweep, decisive for the intake verdict below.** Ian Saberton, "Decoding British ciphers used in the South, 1780-81" (*Journal of the American Revolution*, 6 June 2019, `allthingsliberty.com/2019/06/decoding-british-ciphers-used-in-the-south-1780-81/`, fetched by this worker and read in full) describes and demonstrates breaking the **"Common cipher"**: a simple rotating-alphabet substitution (two concentric rings, alphabet vs. a fixed number sequence, keyed by whichever number is aligned with "A", given away by the first number in the enciphered text) used in correspondence between **Lt. Gen. Cornwallis** and his subordinates Rawdon, Turnbull, Tarleton and Craig, and explicitly also by **Gen. Sir Henry Clinton** "in his dispatch of July 11, 1781 to Cornwallis, who had by then entered Virginia" (footnote 3 cites Saberton's own edition, *The Cornwallis Papers: The Campaigns of 1780 and 1781 in the Southern Theatre of the American Revolutionary War* ("CP"), 6 vols, Naval & Military Press 2010, vol.5 p.139, for the deciphered text of that dispatch). The article states plainly: "I have come upon no evidence that any of the above ciphers was ever broken by the revolutionaries" -- i.e. these are not American wartime decrypts, they are Saberton's own modern editorial decipherments, published in CP.
Cross-checked against TNA Discovery (fresh item-level fetch, this worker, 25 Sept 2026): two of our eight named cipher items fall squarely inside the date range and correspondent pair the "Common cipher" covers --
- **PRO 30/55/32/2 (item 3689)**: "Cornwallis to Clinton. York Town [Yorktown], Virginia. [Original written in cypher]." Dated **16 Aug 1781**.
- **PRO 30/55/33/7 (item 3813)**: "Cornwallis to Clinton. Letter (part in cipher) relating to the situation at York Town." Dated **3 Oct 1781**.
Both dates sit inside Saberton's CP **pt.11**, "Evacuation of Portsmouth, occupation and siege of Yorktown and Gloucester: 23rd July to 19th October 1781" (confirmed via Google Books' part-volume listing for the 2010 Naval & Military Press edition, this worker, 25 Sept 2026) -- exactly the volume built around the correspondence the JAR article's worked example (Clinton to Cornwallis, 11 July 1781) is drawn from. Given Saberton is the editor who personally deciphered this exact cipher for this exact correspondent pair and date window, it is very likely his edition already prints these two items in clear. **This worker could not open it**: Google Books returns `NO_PAGES` for every edition/part found (`PPyytQEACAAJ`, `WJxDtAEACAAJ`, `cLR9zQEACAAJ`, `cRl7zQEACAAJ`, `Q8WBzQEACAAJ`), it is not on Internet Archive (`advancedsearch.php?q=Cornwallis+Papers+Saberton` -> 0 results), and it is not covered by any of the owner's credentialed routes (not JSTOR, not HathiTrust, not a Google Books full-view volume, not academia.edu) -- so no LOCAL-QUEUE/JSTOR-QUEUE row applies; a library copy or purchase is the only route, for the person.
By contrast, **PRO 30/55/33/65 (item 3868, Clinton to Haldimand, 12 Nov 1781)** and **PRO 30/55/33/47 (item 3853, Robertson to Haldimand, 31 Oct 1781)** are Haldimand correspondence, outside Saberton's Cornwallis-focused edition and outside the "Common cipher" article's named correspondents entirely (Haldimand is never mentioned in the JAR piece) -- these two stay on the older footing (HMC paraphrase only, no demonstrated key), not resolved by this finding.

1. **Web search.** `WebSearch` `"PRO 30/55" Cornwallis Clinton Haldimand cipher deciphered Saberton "Common cipher"` -> surfaced the JAR article above (new this sweep) and confirmed via a TNA Discovery beta-catalogue hit (`beta.nationalarchives.gov.uk/catalogue/id/C16309408`) that PRO 30/55 holds Clinton-Cornwallis correspondence from March 1781 onward, consistent with the series description already on file. The 23 Sept 2026 sweep's earlier search (`"PRO 30/55" Clinton Cornwallis cipher deciphered Clements Library`) is superseded by this better-targeted query; not re-run.
2. **Standard edition(s).** HMC Report: re-confirmed via fresh TNA Discovery item-level fetches (2 requests, PRO 30/55/32 and /33, 250 rows each) that entries 3689, 3803, 3813, 3868, 3853 all carry HMC's own plain-English calendar text delivered by the API, with exact dates now on record (above and in the source table). The HMC Report's own printed volume/page for these entries was not opened this sweep (unchanged from 23 Sept: "vol.3 or 4" not pinned down); superseded in importance by the Saberton finding for the two Cornwallis items. Saberton's CP pt.11: see "New finding" above -- identified, not opened.
3. **Community lists.** `sources/cryptiana/web/` grepped again for "PRO 30/55"/"Carleton Papers"/"Yorktown cipher": no hit (Cryptiana's scope is predominantly continental European). Aymeloglu's shallow-cloned repository (fresh clone, 25 Sept 2026): grepped for "cornwallis"/"haldimand"/"30.55"/"30/55" across the whole repository -- three superficial regex hits (`labbe1582/cipher_inventory.md` a raw digit string, `indus/results/predict_test139.md` an unrelated Indus-script prediction table, both coincidental "30...55"-shaped number sequences, not text mentions) and no real hit.
4. **DECODE.** `sources/decode/*.tsv` grepped for "clinton"/"cornwallis"/"haldimand"/"carleton": no hit (unchanged from 23 Sept).
5. **Bourdeau.** Shallow-cloned `dbourdeau/cyphersolver` fresh this session (25 Sept 2026, superseding the earlier `cs-recheck` clone referenced in the 23 Sept sweep, which no longer exists on disk). Grepped for "cornwallis"/"haldimand"/"30/55"/"30.55"/"clinton"/"carleton" across the whole repository: the only substantive hit is `oldest/scan_2026-09-23/hard_targets.md` line 149, **"Cornwallis Papers PRO 30/11 'undeciphered' (1780-81): Saberton decoded the southern British ciphers (JAR 2019)."** -- this is the same Saberton/JAR lead as above, but Bourdeau's own note names the wrong series (**PRO 30/11**, the Cornwallis Papers proper, not **PRO 30/55**, the Carleton/Clinton Papers our target is drawn from) and treats it as a closed "solved elsewhere" note without checking whether PRO 30/55's Cornwallis-Clinton items are the same correspondence under a different TNA series reference (they very plausibly are: Carleton, as Clinton's eventual successor, retained copies of Clinton's incoming/outgoing correspondence, so the same 16 Aug/3 Oct 1781 letters could appear catalogued in both PRO 30/11 and PRO 30/55 as sender's-copy and recipient's-copy). `dbourdeau/cyphersolver` has no dedicated target folder for this item. No `destaing`-style per-target NOTES.md exists for it.
6. **Aymeloglu.** See point 3 (checked together): no real hit.

Requests: discovery.nationalarchives.gov.uk 2 (item-level, /32 and /33), archive.org (advancedsearch + be-api fts, HMC Report re-check) 6, Google Books API 1, WebSearch 1, allthingsliberty.com 2 (search + article), 1.5-1.6 s apart throughout.

**Intake verdict: blocked.** Two of the eight named items (3689, 3813) now have a specific, named, almost-certainly-decisive edition (Saberton, *CP* pt.11) that this worker could not open -- per CLAUDE.md's Pipeline intake gate, "An edition you could not open makes it `blocked`, whatever else you found." `LOCAL-QUEUE.tsv` row **L16** (added LANE CX2 25 Sept 2026) asks the owner's home browser to try a logged-in Google Books search-inside of *CP* vol.6/pt.11 for the two dated dispatches, since the cloud-side API returns `NO_PAGES` for every edition/part found. The other six items (2380, 2894, 3803, 3833/33 x2, 4833, 6009, 6012 -- Haldimand/Carleton/general-staff correspondence, not Cornwallis's) remain at the older footing: HMC paraphrase in print since 1904-09, no demonstrated key, no edition beyond HMC identified this sweep or the last. No deep work (transcription, key application, cryptanalysis) should be briefed on PRO 30/55/32/2 or PRO 30/55/33/7 until Saberton's CP pt.11 is read (by the person, or via a library/ILL copy); the other six items stay at the 23 Sept 2026 "stage 2 conditional" footing pending the HMC Report's own printed pages and the Clements/Saberton PRO 30/11 cross-reference above.

## Google Books API (GBOOKS, 25 Sept 2026)

Parent worker GBOOKS, LOCAL-QUEUE.tsv row L16, per CLAUDE.md's Access playbook "Cloud fix" (`&country=US&key=$GOOGLE_BOOKS_KEY`). ~24 calls, 2s apart, key never printed.

**Re-check of the five named Saberton ids, with `country=US`:** `PPyytQEACAAJ`, `WJxDtAEACAAJ`, `cLR9zQEACAAJ`, `cRl7zQEACAAJ`, `Q8WBzQEACAAJ` — all still `viewability: NO_PAGES`, `accessViewStatus: NONE`. A sixth Naval & Military Press part found this pass (`I7LQYgEACAAJ`, the 6-volume set page) and two more individual parts (`OaWPzQEACAAJ` pt.4/5, `ZIN7zQEACAAJ` pt.6) are also `NO_PAGES`. `country=US` does not change Saberton's own edition's status: confirmed still unreadable from the cloud via the API, same as the 25 Sept LANE CX2 finding.

**New this pass, and it changes the picture: a different, fully public-domain 1888 edition already cross-references both target letters.** Broadening past `intitle:"Cornwallis Papers"` (which returns 0 for the target phrases — Saberton's title doesn't carry them) to a plain phrase+name search surfaced **Benjamin Franklin Stevens (ed.), *The Campaign in Virginia, 1781: An Exact Reprint of Six Rare Pamphlets on the Clinton-Cornwallis Controversy. With Very Numerous Important Unpublished Manuscript Notes*, London, 1888** — confirmed by title search (`intitle:"Clinton-Cornwallis Controversy"` → `BB36xwEACAAJ`, same 1888 date, matching author/description). Several Google scans of it are `viewability: ALL_PAGES`, `accessViewStatus: FULL_PUBLIC_DOMAIN`: `RZQoAQAAIAAJ`, `m5MoAQAAIAAJ`, `-i-gAAAAMAAJ`, `4ShNAQAAMAAJ`. This is **not** the HMC Report (a separate ALL_PAGES scan set, `7GtnAAAAMAAJ`/`WahkB2FaRP4C`, already known and searched via archive.org in the 23 Sept sweep above) and **not** Saberton — it is a 19th-century primary-source compilation not previously identified anywhere in this folder.

Verbatim snippets, all from `RZQoAQAAIAAJ` unless noted (both target dates hit):

- **16 Aug 1781 (→ PRO 30/55/32/2, item 3689):** `"... 14IB : CORNWALLIS to CLINTON , 16 August 1781 , ANSWER [ 185 ] i . 90 . With Clinton's Manuscript Notes . Earl Cornwallis to Sir Henry Clinton , K.B. dated York-town , 16th August , 1781 . Same as No. 141 with variations shown in margins pp..."` (page range cut off by the snippet window). The immediately preceding numbered item in the same apparatus is explicitly cipher-flagged: `"Number VII . [ 183 ] Sir Henry Clinton , K.B. to Earl Cornwallis , New-York , August 11 , 1781. ( In Cypher . ) ( Received August 16 , 1781. )"` — i.e. Clinton's own 11 Aug dispatch (received 16 Aug, the same day Cornwallis's reply is dated) is marked in cypher in this edition; whether item 185 (Cornwallis's reply) is separately cypher-flagged was not seen in any snippet window this pass.
- **3 Oct 1781 (→ PRO 30/55/33/7, item 3813):** `"... Cypher • BFS begin d E begins • EM read town , Virginia , October 3 , 1781. [ In cypher . ] Same as No. 163 with variations shown in margins pp 174-175- 163V : CORNWALLIS to CLINTON , 3 October ..."` and, from the French-translation cross-reference apparatus in the same volume: `"163V : CORNWALLIS to CLINTON , 3 October , Fr trans GERMAIN P 254 . Envoyé un Duplicata parle major Cochran le 3 octobre . Copie d'une lettre du comte Cornwallis à Sir Henri Clinton , datée de Yorktown en Virginie le 3 octobre 1781..."` — **this one is explicitly `[In cypher.]`**, with a page pointer (pp 174-175) to the transcribed text and a cross-reference to a French translation sent to Lord George Germain.

**What this settles and what it doesn't.** This is a strong, previously-unidentified, fully public-domain lead: both letters are catalogued in Stevens 1888 with explicit page pointers, and the 3 Oct letter is explicitly tagged `[In cypher.]` with a French-translation cross-reference — consistent with a transcription (deciphered or the cipher-groups themselves) actually printed at pp.174-175 and around "No. 141"/"[185]". **This worker did not read those pages** — this session's network is scoped to `www.googleapis.com/books` only, and the API's snippet mechanism gives only short matched windows, not continuous page text, even for an ALL_PAGES/public-domain book. Since the whole work is public domain (1888, ALL_PAGES), it is very likely also on Internet Archive or HathiTrust under a title such as "The Campaign in Virginia, 1781" or "Clinton-Cornwallis Controversy" — a future worker with archive.org/HathiTrust access should fetch it directly and read pp.174-175 (for the 3 Oct letter) and the pages around item "[185]"/"No. 141" (for the 16 Aug letter) for the actual transcribed/deciphered text, rather than repeating this snippet search.

LOCAL-QUEUE.tsv row L16 left `queued` (not `done`): Saberton himself is still unreadable (API-confirmed, `country=US` makes no difference), but the row's underlying question — are these two letters printed in clear anywhere reachable — now has a much better lead than Saberton, not yet followed to a page read. Row instruction rewritten to point at Stevens 1888 via archive.org/HathiTrust instead of a Google-Books-login browser check.

# Clinton, Cornwallis and Haldimand cipher letters — TNA PRO 30/55, American War of Independence

QUEUE row: N7 (sources/solver-diffs/2026-09-23-non-decode-hits.tsv, "Candidates not on DECODE").

## Source

TNA PRO 30/55 (the "Carleton Papers", intercepted/retained transcripts and originals relating to the
British high command in America — Sir Henry Clinton, Lord Cornwallis, Sir Guy Carleton and Frederick
Haldimand — held at The National Archives, Kew). QUEUE named eight pieces: **PRO 30/55/19, /24, /32, /33
(x2), /42, /53** (1779-82). TNA Discovery's own item descriptions for this series are drawn directly from
the *Report on American Manuscripts in the Royal Institution of Great Britain* (Historical Manuscripts
Commission, 4 vols, 1904-09) — every description fetched this sweep carries its original HMC calendar entry
number (e.g. "2894.", "3868.") as a prefix, confirming the two catalogues are the same text.

## Check-solved sweep (23 September 2026)

1. **TNA Discovery API — item-level detail (decisive).** Fetched all items under each of the six named
   piece numbers (`sps.searchQuery="PRO 30/55/NN"`, `sps.resultsPageSize=250`; 5 requests) and filtered for
   cipher language. Findings per piece, quoted verbatim from Discovery/HMC:
   - **PRO 30/55/19/98** — "2380. Clinton to Haldimand. Letter in cypher." No further note.
   - **PRO 30/55/24/76** — **"2894. [Letter in cypher, no date or names however it was found by comparison
     to be the same as one at British Museum.] Clinton to Haldimand stating that information received
     indicates that a French force had sailed around 3 May with seven ships of th[e line...]"** — this is
     the piece the QUEUE row flagged as "previously matched to plaintext by comparison to [...]". The
     bracket is the HMC cataloguer's own 1904-09 note: the *content* of this undated, unsigned ciphertext
     was established not by breaking the cipher but by finding a plain-language duplicate/related copy at
     the British Museum (now British Library). The cipher itself was not necessarily broken; its content is
     known from a comparison copy elsewhere.
   - **PRO 30/55/32** — five cipher-flagged items found (more than the QUEUE row's single-item count),
     including "3689. Cornwallis to Clinton. York Town [Yorktown], Virginia. [Original written in cypher].
     No detachment can be made from this place..." and "3803. Clinton to Cornwallis... Two copies of a
     document, the first in code..." — all given full plain-English calendar summaries by HMC despite being
     "in cypher"/"in code" in the original.
   - **PRO 30/55/33** — three cipher-flagged items (QUEUE said "x2"): "3868. [Clinton to General Haldimand]
     in cypher.", "3813. Cornwallis to Clinton. Letter (part in cipher)...", "3853. ...[A second letter in
     cypher is enclosed]." — again, each already carries an HMC plain-English summary.
   - **PRO 30/55/42/120** — "4833. Haldimand to Carleton... Enclosed is a duplicate letter in cypher which
     he dispatched yesterday, overland..." — summarized in clear by HMC.
   - **PRO 30/55/53** — "6009. George Beckwith to Major Fred Mackenzie... The ciphered note for General
     Haldimand sent an hour ago is to be forwarded..." and "6012. [Major] F[red] M[ackenzie] to Major
     General James Patterson. Is directed by the Commander-in-Chief to transmit a letter in cypher..." —
     these describe couriering a ciphered note, not necessarily deciphering it; content is given by HMC from
     the covering correspondence, not from breaking the enclosed cipher.
   **Pattern found across all six pieces: every cipher-flagged item already carries a full plain-English
   HMC calendar summary of its content**, dated 1904-09. This is not the same as a verified, token-level
   decipherment (rule 4) — HMC's Edwardian calendarists paraphrased from context, comparison copies (as
   explicitly stated for 2894), or, in some cases plausibly, from a decipherment no longer stated — but it
   means the substantive military content of these items has been in print, in English, for over a century.
2. **Print — the HMC Report itself.** Confirmed on archive.org: at least 14 separate scans of *Report on
   American Manuscripts in the Royal Institution of Great Britain* (1904, various vols/re-scans:
   `reportonamerica03dorcgoog`, `reportonamerican02grea`, `b24874930`, `reportonamerica02dorcgoog`,
   `amerimanuscript34greauoft`, `cu31924091754485/93/01`, `reportonamerica00britgoog`,
   `reportonamerica00dorcgoog`, `reportonamerican12greauoft`, `reportonamerican04grea`,
   `reportonamerica01dorcgoog`, plus a 1972 reprint `reportonamerican0000grea`; 1 advancedsearch request,
   20 results). Not opened page-by-page to verify entry numbers 2380/2894/3689-3868/4833/6004-6048 fall in
   specific volumes, or to check whether the calendar prints the cipher-text/decipherment or only the plain
   summary — left for the access step.
3. **Print — Saberton's Cornwallis Papers (2010) and the Clinton Papers calendar (Clements Library).** Not
   checked this sweep (both need either a purchase/loan or a specific finding-aid fetch not attempted). The
   Clements Library's own online exhibit page ("The Henry Clinton Papers", `clements.umich.edu`) was surfaced
   by web search but not read for content this pass.
4. **Community lists.** `sources/cryptiana/web/` grepped for "PRO 30/55"/"Clinton"/"Cornwallis"/"Haldimand":
   no hit for any of the three names; a *different* item is on Tomokiyo's `unsolved.htm` list in the same
   milieu but not this series: "An encoded letter from Admiral D'Estaing to Gerard, French minister in
   Philadelphia, dated 30 April 1779 is preserved in William L. Clements Library, Clinton Papers, 'vol
   64:14'. British Commander Sir Henry Clinton forwarded this intercepted letter home in July [1779]" — this
   is a Clements Library item, not TNA PRO 30/55, and is listed as unsolved by Tomokiyo; noted for context,
   not counted as covering our eight pieces. Bourdeau's own working notes (`cs-recheck/TARGETS.md`, item 14)
   independently list the same D'Estaing-Gerard letter as "skipped" — confirming it is a known, separate,
   still-open item that neither this sweep nor Bourdeau's project has connected to PRO 30/55. WebSearch for
   `"PRO 30/55" Clinton Cornwallis cipher deciphered Clements Library` surfaced only secondary/general
   sources (Journal of the American Revolution's "Decoding British ciphers used in the South, 1780-81",
   a Virginia Tech course blog on "Cornwallis and Lovell Ciphers") describing James Lovell's *American*
   decryption of intercepted British ciphers generally, not a decipherment of these specific eight TNA
   pieces (1 query).
5. **DECODE.** Cached catalogue grepped for "clinton"/"cornwallis"/"haldimand"/"carleton": no hit — outside
   DECODE's scope (predominantly continental European material).
6. **Bourdeau / Aymeloglu.** `cs-recheck/*.md` grepped: only the unrelated D'Estaing-Gerard item (above,
   `TARGETS.md` item 14, "skipped"). `ay/*.md` grepped for the same terms: no hit.

Requests: discovery.nationalarchives.gov.uk 5. archive.org 1 (advancedsearch for the HMC Report).
WebSearch: 2 queries.

## Edition risk

**Partially realized.** The HMC Report on American Manuscripts (1904-09) already gives a plain-English
calendar summary for every one of the cipher-flagged items checked across all six named pieces — this is
real prior publication of the *content*, though not a verified letter-by-letter decipherment, and (for
2894) explicitly not from breaking the cipher at all but from a comparison copy. Whether the HMC editors had
access to a now-lost contemporary decipherment, or paraphrased loosely from surrounding correspondence, is
not established and matters for how the plaintext should be graded (rule 4: a calendar paraphrase is not H
or C evidence of a specific cipher's key). This falls short of "found-solved" because no source demonstrates
a working key applied to the actual ciphertext, but it is well short of a clean, uncomplicated stage 2 too.

## Verdict

**Partial.** PRO 30/55/24/76 (HMC 2894) is content-known-elsewhere (matched to a British Museum copy) and
should not be treated as an open cryptanalysis target without first locating that BM copy and comparing it
directly. The other seven named items (19/98, 32/2, 33/65 or /7 or /47, 42/120, 53/7 or /10, and whichever
one QUEUE meant by "32" and the second "33") have HMC calendar paraphrases in print since 1904-09 but no
demonstrated key; **stage 2, verified unsolved (conditional: the HMC Report's own volume/page for each entry
number not opened to check whether it also prints a decipherment, and Saberton's Cornwallis Papers, the
Clements Library Clinton Papers calendar, and the British Museum/Library comparison copy for 2894, none
checked this sweep)**.

## Next

Open the HMC Report volume covering entry numbers 3689-3868 (vol. 3) and 6004-6048 (vol. 4) on archive.org
and read the actual pages for these entry numbers directly — the API description already gave the summary
text but not confirmation of whether a decipherment (versus a paraphrase) sits alongside it in the printed
calendar. Separately, identify the British Museum/Library item that matches PRO 30/55/24/76 by content (the
French-fleet, 3-May, seven-ships-of-the-line detail is a specific enough crib for a BL catalogue search) —
that may close this one item without any cryptanalysis. Do not order or email; this can all be done from the
desk with archive.org and the BL's own online catalogue.

## Stevens 1888 read from archive.org (25 Sept 2026, parent worker FOLLOWUP-2315, L16)

Per the GBOOKS lead above: B. F. Stevens (ed.), *The Campaign in Virginia, 1781: An Exact Reprint of Six Rare
Pamphlets on the Clinton-Cornwallis Controversy... With Very Numerous Important Unpublished Manuscript Notes*
(London, 1888), 2 vols. Both volumes are on archive.org, full text, no login: `campaigninvirgin01stevuoft` (vol.1,
the chronological reference list, "Number I/II/..." cross-referencing "Letter ii. <page>") and
`campaigninvirgin02stevuoft` (vol.2, "Letter ii", the actual reprinted correspondence with Clinton's manuscript
notes and the "Chronological Correspondence" catalogue of additional copies). Fetched both `_djvu.txt` files
(archive.org/download, browser UA, 2 requests 1.5s apart).

**16 Aug 1781, Cornwallis to Clinton (PRO 30/55/32/2, item 3689).** Vol.1's chronological list: "Number VIII. [185]
Earl Cornwallis to Sir Henry Clinton, K.B. dated York-town, i6th August, 1781. see Letter ii. 126." -- no
`(In Cypher.)` tag (contrast Number VII [183], Clinton's 11 Aug letter, and Number I [189], Cornwallis's 31 Aug
letter, both explicitly tagged `(In Cypher.)` in the same list). Vol.2's catalogue cross-references it as item
"141" ("141B: Cornwallis to Clinton, 16 August 1781, answer[185] i.90 ... Same as No. 141 with variations shown
in margins pp 127-128"; three copies B/F/S listed). At real printed pp.127-128 (vol.2 djvu text, running heads
"125/CLINTON-CORNWALLIS CONTROVERSY" and "CHRONOLOGICAL CORRESPONDENCE/129" bracket the passage; the margin
notes there cite copies S, B and F by letter, matching 141B/141F/141S), the letter is printed **in full, in
clear English, with no cipher notation anywhere in it**:

> "I have received your Excellency's Dispatches of the 15th & 26th Ult° which I shall answer by the first safe
> opportunity. I beg that your Excellency will be pleased to order it to be notified to the Port of New-York,
> that Portsmouth is evacuated, to prevent Vessels from going into that harbour. I have the honour to be with
> great respect, Sir, Your most obedient & most humble Servant. CORNWALLIS. His Excellency Sir Henry Clinton.
> K.B. &c &c &c."

This is short (the whole reply), which is consistent with vol.1's own list not tagging it as ciphered; it does not
by itself confirm or rule out that the manuscript at Kew (PRO 30/55/32/2, catalogued "[Original written in
cypher]" per NOTES.md's Source table) used cipher for a passage Stevens silently normalised, but no such passage
or cipher indicator appears in Stevens's transcription or its margin apparatus. Grade for a future reading: text
known (C), source published.

**3 Oct 1781, Cornwallis to Clinton (PRO 30/55/33/7, item 3813).** Vol.1: "Number XII. [201] Earl Cornwallis to
Sir Henry Clinton, K.B. dated York-Town, Virginia, October 3, 1781. (In Cypher.) see Letter ii. 174." Vol.2's
catalogue: "163 CORNWALLIS to CLINTON, 3 October 1781, ls ei 19/138. Answer [201] i.92, Correspondence [56] i.136,
with Clinton's Manuscript Notes from each," followed immediately by the full text at real pp.174-175 (running
heads "174/CLINTON-CORNWALLIS CONTROVERSY" and "CHRONOLOGICAL CORRESPONDENCE/175" bracket it):

> "York Town Virginia 3 Oct 1781. Sir, I received your Letter of the 25th of September, last night. The Enemy
> are encamped about two miles from us; on the night of the 30th of Sept they broke ground & made two Redoubts
> about eleven hundred Yards from our Works... They have finished their Redoubts, & I expect they will go on
> with their Work this night... I can see no means of forming a junction with me but by York River, and I do
> not think that any diversion would be of use to us. Our Accounts of the Strength of the French Fleet have in
> general been, that they were Thirty-five or Thirty-six Sail of the Line... I see little chance of my Being
> able to send persons to wait for you at the Capes, but I will if possible. I have the honour to be with great
> respect, Sir, Your most obedient and most humble Servant, CORNWALLIS. His Excellency Sir Henry Clinton K.B.
> &c. &c. &c."

with the editorial footnote at the end: **"*[From here partly in cypher with a translation.]"** -- i.e. Stevens's
1888 printed text is not merely a calendar paraphrase but includes a period/editorial translation of the passage
that was in cipher in the manuscript, so the full letter (cipher portion included) is readable in clear here.
This matches TNA's own catalogue tag for item 3813 (`[In cypher.]`) exactly, and Stevens's apparatus cross-refers
seven surviving copies of this letter (163B/F/S/V/E/R/M, across the Answer, Correspondence, Tarleton, Germain
French-translation, and two House-of-Lords copy series), all "same as No.163 with variations shown in margins
pp.174-175". Grade for a future reading: text known (C), source published, translation not original cipher-group
text.

**Requests.** archive.org 2 (download, browser UA, 1.5s apart), no login, no other hosts. Both volumes kept only
as scratch fetches this session (not committed to the repo; both are large full-book OCR dumps and the citation
above is sufficient to re-fetch: `archive.org/download/campaigninvirgin01stevuoft/campaigninvirgin01stevuoft_djvu.txt`,
`.../campaigninvirgin02stevuoft/campaigninvirgin02stevuoft_djvu.txt`).

**Caveat.** This is a djvu OCR read straight from the plain text, not a check against the page image; a future
worker should confirm both quoted passages against the actual page images at archive.org (BookReader,
`campaigninvirgin02stevuoft`, leaves around pp.127-128 and pp.174-175) before treating either as a final grade-C
reading, particularly the item-boundary for the 16 Aug letter, which this pass inferred from the page-range
citation and the matching copy-letter footnotes (S/B/F) rather than from an explicit "No. 141" heading directly
above the text.

## AX-STEV: Stevens 1888 page images (26 Sept 2026, LANE AX)

Per this section's own caveat (25 Sept 2026, FOLLOWUP-2315/GBOOKS), fetched the four printed pages as page images
and read them directly, rather than the djvu OCR text alone.

**Method.** `archive.org/metadata/campaigninvirgin02stevuoft` (1 request) gave the item's own
`_page_numbers.json`, which maps printed page 127/128/174/175 to leaf 135/136/182/183 (offset +8 throughout,
consistent across both target passages -- no offset-change or NP anomaly of the kind `tools/gallica_folio.py`
warns about for Gallica). Fetched each leaf's JP2 directly out of the item's own `_jp2.zip` via
`archive.org/download/<id>/<id>_jp2.zip/<id>_jp2%2F<id>_<leaf>.jp2` (no login; this zip-member route returns the
single-page JP2, HTTP 200, without downloading the 185 MB archive; the BookReaderImages.php route tried first
404'd, this route did not) and converted locally to JPEG (Pillow), 1400px wide for the repo. Images and a
manifest at `ciphers/pro3055-clinton-1779/images/stevens1888/` (4 files, 1.9 MB total, well under the 30 MB
folder cap). Requests: archive.org 5 (1 metadata + 4 leaves), 1.5-1.6s apart, browser User-Agent, no login.
Separately, re-checked TNA Discovery item-level records for pieces 30/55/32, /33, /42, /53, /19, /24 (6 requests,
1.5-1.6s apart, `sps.resultsPageSize=250`) to pin exact dates/correspondents for the re-plan table below (Discovery's
JSON gives `coveringDates`/`startDate`, which the 23 and 25 Sept sweeps had fetched but not transcribed into this
file for every item).

**What the images confirm.** Both passages read exactly as the 25 Sept OCR-based quotes gave them (page images at
`images/stevens1888/p127.jpg`, `p128.jpg`, `p174.jpg`, `p175.jpg`; full quotes and citations unchanged from the
"Stevens 1888 read from archive.org" section above). The 3 Oct 1781 letter's cipher footnote position is now
precise from the image: the asterisk sits in the body text immediately before the paragraph beginning "I can see
no means of forming a junction with me but by York River" (p.175), so the manuscript's ciphered portion is that
final paragraph only (French-fleet strength, junction, the Capes), not the whole letter -- the footnote itself
("[From here partly in cypher with a translation.]") is set below the signature block, not inline.

**Correction to the 25 Sept OCR-based read (16 Aug 1781 letter, item 3689).** That section stated: "no cipher
notation anywhere in it... no such passage or cipher indicator appears in Stevens's transcription or its margin
apparatus." This is wrong and the image shows why: the page-image's endorsement note, printed directly above the
letter on p.127, reads in full: "*Endorsed* Duplicate. Earl Cornwallis to Sir H. Clinton K.B. York 16th August
1781 Original rec<sup>d</sup> the 23<sup>d</sup> Aug<sup>t</sup> by the Swallow Dispatch Boat. rec<sup>d</sup>
30<sup>th</sup> Aug<sup>t</sup> ⅌ L<sup>t</sup> Col<sup>o</sup> de Buy 209. **The Original was written in
Cypher.**" This matches TNA's own catalogue tag for item 3689 ("[Original written in cypher]") exactly, and the
letter's own opening line ("This morning I received your Cyphered Letter of the 11th instant, by the Runner")
refers to *Clinton's* 11 Aug dispatch, a separate item. Grade is unaffected (Stevens prints the deciphered/plain
text either way; still text known, C), but the sentence claiming no cipher indicator was a misreading of the OCR
text, which had missed the endorsement's small print. Corrected here rather than silently edited in place, per
the repo's append-don't-rewrite convention for prior workers' sections.

**New cipher-flagged items found in piece /32 (not in the folder's prior 8/10-item count).** The TNA Discovery
re-check for exact dates (above) turned up two cipher items in piece 30/55/32 beyond 3689 and 3803, neither
previously named anywhere in this folder: **3753** (PRO 30/55/32/66, Cornwallis to Clinton, York/Virginia, 31 Aug
1781, "Two copies of the document, one in part cypher") and **3784** (PRO 30/55/32/97, Cornwallis to Clinton,
Yorktown, Virginia, 16-17 Sept 1781, "The rest of the document is in cypher"). This confirms the 23 Sept
check-solved sweep's "five cipher-flagged items found" note for piece /32 (only two, 3689 and 3803, had been
individually named until now) -- a fifth may still be uncaught: this piece has 311 total Discovery records and
only the first 250 (the same page size the 23/25 Sept sweeps used) were re-checked this session, so this is not
a complete sweep of /32, and pieces 33 (355 records, 250 checked), 42 (349, 250), 53 (289, 250), 19 (467, 250)
and 24 (1220, only 250 = 20%) are checked even less completely -- flagged for a future check-solved re-run, not
chased further this session (out of this worker's named steps).

**Correction to the "other six/eight" line (line 1 of this file, FOLLOWUP-2315).** That line lists item 3803
among items that "remain unaffected... at their existing footing" and the "Intake verdict" section (above)
describes the same six items as "Haldimand/Carleton/general-staff correspondence, not Cornwallis's". TNA
Discovery's own description of 3803 (`PRO 30/55/32/116`, re-fetched this session) reads "**Clinton to
Cornwallis**. New York. Two copies of a document, the first in code..." -- it *is* Cornwallis/Clinton
correspondence, catalogued in the same piece (/32) as 3689, and dated 30 Sept 1781, inside Saberton's CP pt.11
window. This item was miscategorised in that line; corrected in the table below.

**Re-plan: all 12 named cipher-flagged items across the target (26 Sept 2026).** The folder's item count was
never actually 8 -- the 23 Sept check-solved sweep found "five" in piece /32 alone (only two named at the time)
plus items in five other pieces; with 3753/3784 now named, 12 distinct cipher-flagged items are on record. Saberton's
"Common cipher" (JAR, 6 June 2019; CP pt.11, 23 Jul-19 Oct 1781) covers correspondence between Cornwallis and his
subordinates and Clinton, within that date window.

| Item | Date | Correspondents | Printed where | Text status | Next step |
|---|---|---|---|---|---|
| 3689 (PRO 30/55/32/2) | 16 Aug 1781 | Cornwallis to Clinton | Stevens 1888 vol.2 pp.127-128, page image checked this session | text known (C) -- full letter in clear; manuscript endorsed "Original was written in Cypher" | none; this item is found-solved |
| 3813 (PRO 30/55/33/7) | 3 Oct 1781 | Cornwallis to Clinton | Stevens 1888 vol.2 pp.174-175, page image checked this session | text known (C) -- full letter in clear; final paragraph only was "partly in cypher with a translation" | none; this item is found-solved |
| 3753 (PRO 30/55/32/66) | 31 Aug 1781 | Cornwallis to Clinton | not located this sweep -- new item, not previously named in this folder | text unknown | same correspondent pair/edition as 3689 and 3813 -- check Stevens 1888 vol.1's chronological list and vol.2 index for a 31 Aug 1781 entry first; falls inside Saberton's CP pt.11 window, so if Stevens does not have it, **a reading with the Common cipher would be a published-key reading, N2 at best** |
| 3784 (PRO 30/55/32/97) | 16-17 Sept 1781 | Cornwallis to Clinton | not located this sweep -- new item, not previously named in this folder | text unknown | same as 3753: check Stevens 1888 first; inside Saberton's CP pt.11 window, so **a reading with the Common cipher would be a published-key reading, N2 at best** if not found there |
| 3803 (PRO 30/55/32/116) | 30 Sept 1781 | Clinton to Cornwallis | not located this sweep | text unknown | correspondent pair and date both fit Saberton's CP pt.11 window -- check Stevens 1888 first; **a reading with the Common cipher would be a published-key reading, N2 at best** if not found there (corrects the "not Cornwallis's" miscategorisation above) |
| 2380 (PRO 30/55/19/98) | 22 Oct 1779 | Clinton to Haldimand | HMC Report calendar paraphrase only (1904-09), page not opened | partly known (paraphrase, not a verified decipherment) | outside Saberton's Common cipher scope (Haldimand, not Cornwallis/Clinton; also 2 years before the CP pt.11 window) -- open the HMC Report's own printed volume/page |
| 2894 (PRO 30/55/24/76) | 1780 (year only) | Clinton to Haldimand | content matched to a British Museum/Library comparison copy per HMC's own 1904-09 note | known elsewhere (via the BM/BL copy, not by breaking the cipher) | outside Saberton's scope; locate the BM/BL comparison copy directly (specific enough crib: French fleet, 3 May, seven ships of the line) |
| 3868 (PRO 30/55/33/65) | 12 Nov 1781 | Clinton to Haldimand | HMC Report calendar paraphrase only, page not opened | partly known | outside Saberton's scope (Haldimand correspondent; also after CP pt.11's 19 Oct 1781 end, i.e. after Yorktown's surrender) -- open the HMC Report |
| 3853 (PRO 30/55/33/47) | 31 Oct 1781 | Robertson to Haldimand | HMC Report calendar paraphrase only, page not opened | partly known | outside Saberton's scope (Robertson/Haldimand, not Cornwallis/Clinton) -- open the HMC Report |
| 4833 (PRO 30/55/42/120) | 23 June 1782 | Haldimand to Carleton | HMC Report calendar paraphrase only, page not opened | partly known | outside Saberton's scope entirely (different correspondents, different year, different theatre) -- open the HMC Report |
| 6009 (PRO 30/55/53/7) | 26 Oct 1782 | Beckwith to Mackenzie | HMC Report calendar paraphrase only, page not opened; describes forwarding a ciphered note, may not itself be cipher text | partly known / may not be a cipher-text item at all | outside Saberton's scope -- open the HMC Report |
| 6012 (PRO 30/55/53/10) | 26 Oct 1782 | Mackenzie to Patterson | HMC Report calendar paraphrase only, page not opened; describes transmitting a letter in cypher, may not itself be cipher text | partly known / may not be a cipher-text item at all | outside Saberton's scope -- open the HMC Report |

**Status.** Line 1 stays `partial`: 2 of 12 named items are text known (C), 10 remain text-unknown or
known-only-by-paraphrase/comparison-copy. No deep work (transcription, key application, cryptanalysis) on any of
the five Cornwallis-Clinton items (3689, 3813, 3753, 3784, 3803) until Stevens 1888 (or Saberton's CP pt.11) has
been checked for the three still-unlocated ones; the six Haldimand/Carleton/general-staff items stay at the HMC
paraphrase footing pending the HMC Report's own printed pages.

**Requests this session.** archive.org 5 (1.5-1.6s apart, browser User-Agent, no login); discovery.nationalarchives.gov.uk
6 (1.5-1.6s apart, descriptive User-Agent). No other hosts.

## AX-STEV2: 3753/3784/3803 located in Stevens 1888; Discovery sweep confirmed complete (26 Sept 2026, LANE AX)

**Method (pp.146-147, 156-157, 172-173).** Fetched vol.1's own full text (`campaigninvirgin01stevuoft_djvu.txt`, archive.org, 1 request, disk-only, not committed to the repo) and located its "CHRONOLOGICAL CORRESPONDENCE" apparatus (pp.135-136), which cross-references each dated letter to its page in vol.2 ("see Letter ii. NNN"): item **[48]**, "Lieutenant General Earl Cornwallis... York, in Virginia, August 31, 1781... see Letter ii. 146" (-> 3753); item **[52]**, "...York-Town, Virginia, September 16, 1781... see Letter ii. 156" (-> 3784); "[Clinton [Facing 55] to Cornwallis] New York, 30th Sept. 1781... see Letter ii. 172" (-> 3803). Re-fetched vol.2's `_page_numbers.json` (1 metadata + 1 file request) and confirmed the same +8 page-to-leaf offset AX-STEV found at pp.127-128/174-175 holds at all three new pairs: 146->154, 147->155, 156->164, 157->165, 172->180, 173->181 -- no offset change. Fetched all 6 leaves via the same `_jp2.zip` zip-member route (no login), converted to JPEG at 1400px wide (Pillow). 6 archive.org requests, 1.5-1.6s apart, browser User-Agent. Images at `images/stevens1888/p146.jpg` etc.; manifest.json updated (10 images total, 4.8 MB, well under the 30 MB cap).

**All three found, all printed in clear (deciphered) text.**
- **3753** (PRO 30/55/32/66, 31 Aug 1781, Cornwallis to Clinton): Stevens 1888 vol.2 pp.146-147, item 149. Endorsement: "Duplicate. Earl Cornwallis to Sir H. Clinton, K.B., York August 31st 1781 rec<sup>d</sup> the 4th Septr 1781..." Body printed in full, verbatim match to TNA's description ("A French Ship of the Line, with two Frigates, & the Loyalist, which they have taken, lay at the Mouth of this River, A Lieutenant of the Charon, who went with an Escort of Dragoons to Old Point Comfort, reports, that there are* between 30 and 40 Sail within the Capes, mostly Ships of War, & some of them very large"), with a footnote "* [From here in cypher with translation in margin]" after "large" — only the final clause was ciphered in the manuscript; Stevens prints the deciphered text throughout. Apparatus line 149B tags a duplicate copy "[In Cypher.]" explicitly.
- **3784** (PRO 30/55/32/97, 16-17 Sept 1781, Cornwallis to Clinton): Stevens 1888 vol.2 pp.156-157, item 156. Endorsement: "Cypher Duplicate. Earl Cornwallis to Sir Henry Clinton 16th & 17th Septr 1781." Body printed in full, verbatim match to TNA's description ("the Enemy's Fleet has returned. Two Line of Battle Ships, & one Frigate, lie at the mouth of this River; & three or four Line of Battle Ships, several Frigates & Transports, went up the Bay on the 12th & 14th"). No cipher-transition footnote appears on this leaf because the whole letter was sent enciphered per the "Cypher Duplicate" endorsement; the full deciphered text is printed.
- **3803** (PRO 30/55/32/116, 30 Sept 1781, Clinton to Cornwallis): Stevens 1888 vol.2 pp.172-173, item 162. "Sir Henry Clinton to Earl Cornwallis, dated New-York, September 30, 1781. [Duplicate, in Cypher.] [Received October 10, from Major Cockran.]" Body printed in full, verbatim match to TNA's description ("Assuring his lordship that he is doing everything in his power to relieve him by a direct move..."). Margin note on p.172 ("V in cypher to p 173 l 2") records that one manuscript variant was in cipher almost to the letter's end; the printed text is the full deciphered text.

All three are the same shape as 3689/3813 (AX-STEV, 25/26 Sept): a fully public-domain 1888 edition already prints the deciphered text, independent of Saberton's still-unreadable CP pt.11. Per rule 4, grade **C** (from known plaintext — a printed 19th-century edition, not a solver's own decipherment). Per rule 10 this worker does not classify novelty, only reports where the text is printed.

**TNA Discovery sweep: re-examined and found already complete, not merely 250-of-N (26 Sept 2026).** AX-STEV's flag that pieces 32/33/42/53/19/24 had only their first 250 Discovery records checked, against API-reported totals of 311/355/349/289/467/1220, rests on a misreading of the API's `count` field. Testing shows `sps.searchQuery="PRO 30/55/NN"` is a loose, relevance-ranked full-text match on the query string, not a piece-scoped listing: raising `sps.resultsPageSize` to the reported count (or to the API's actual cap, confirmed at 1000 — 1000 succeeds, 1220 returns HTTP 400) returns many records from *other* pieces that merely contain "NN" as a token somewhere in their reference (e.g. searching "PRO 30/55/32" also returned "PRO 30/55/30/32", "PRO 30/55/53/32", "DE/Rv/C1-C2852"...). Filtering each piece's returned records for an actual `reference` prefix match gives the true item count per piece, and in every case **all real matches fall inside the first 250 relevance-ranked results, and none exist beyond position 250** (checked out to the full loose-match count for 32/33/42/53/19, and out to position 1000 of 1220 for piece 24 in one pass):

| Piece | API's loose `count` | Real items (reference-prefix filtered) | Real matches beyond position 250 | Cipher-flagged (cypher/cipher/code in description) |
|---|---|---|---|---|
| 32 | 311 | 119 | 0 | 4 (3689, 3753, 3784, 3803 — all known) |
| 33 | 355 | 110 | 0 | 3 (3813, 3853, 3868 — all known) |
| 42 | 349 | 128 | 0 | 1 (4833 — known) |
| 53 | 289 | 116 | 0 | 2 (6009, 6012 — known) |
| 19 | 467 | 115 | 0 | 1 (2380 — known) |
| 24 | 1220 | 126 | 0 (of the 1000 fetched) | 1 (2894 — known) |

Piece 24's remaining 220 loose-match records (positions 1001-1220, unreachable in a single call because of the API's 1000-record cap) were separately checked by date-bucketing the same query into six per-year requests (`sps.dateFrom`/`sps.dateTo`, confirmed working params: 1778: 32, 1779: 28, 1780: 149, 1781: 41, 1782: 448, 1783: 469 loose matches, summing to 1167 of the 1220 — the remaining ~53 are presumably undated or fall outside a single calendar year and were not chased further, a residual gap logged here rather than closed). Every per-year bucket was small enough to fetch in one request each (max 469, under the 1000 cap), and the reference-prefix-filtered union across all six years is **the same 126 real items and the same single cipher hit (2894)** already found in the top-1000 sweep — full, not partial, coverage of piece 24's real item population under this method.

**Conclusion: the item-level sweep across all six named pieces is complete under this search method, and finds no cipher-flagged item beyond the 12 already logged in the table below.** This does not rule out an item whose description omits "cipher"/"cypher"/"code" outright (a paraphrase using "secret characters" or similar without those three words, or one of the ~53 undated/cross-year piece-24 records this date-bucket method could not reach) — flagged as a residual gap, not a closed negative, and not chased further this session (the brief's discovery.nationalarchives.gov.uk request budget was nearly used, see below).

Requests this session: discovery.nationalarchives.gov.uk 26 (1.5-1.6s apart throughout, descriptive User-Agent, under the 40-request cap); archive.org 10 (1 advancedsearch, 1 vol.1 djvu.txt, 1 vol.2 metadata, 1 vol.2 page_numbers.json, 6 leaf JP2 fetches; 1.5-1.6s apart, browser User-Agent, no login). No other hosts.

**Re-plan: updated 12-item table (26 Sept 2026).** Copied from AX-STEV's table above; only the three now-resolved rows (3753, 3784, 3803) are changed, the rest reproduced unchanged.

| Item | Date | Correspondents | Printed where | Text status | Next step |
|---|---|---|---|---|---|
| 3689 (PRO 30/55/32/2) | 16 Aug 1781 | Cornwallis to Clinton | Stevens 1888 vol.2 pp.127-128, page image checked | text known (C) — full letter in clear; manuscript endorsed "Original was written in Cypher" | none; this item is found-solved |
| 3753 (PRO 30/55/32/66) | 31 Aug 1781 | Cornwallis to Clinton | **Stevens 1888 vol.2 pp.146-147, item 149, page image checked this session** | **text known (C)** — full letter in clear; footnote marks only the final clause as "in cypher with translation in margin" | none; this item is found-solved |
| 3784 (PRO 30/55/32/97) | 16-17 Sept 1781 | Cornwallis to Clinton | **Stevens 1888 vol.2 pp.156-157, item 156, page image checked this session** | **text known (C)** — full letter in clear; endorsed "Cypher Duplicate" (whole letter enciphered in manuscript) | none; this item is found-solved |
| 3803 (PRO 30/55/32/116) | 30 Sept 1781 | Clinton to Cornwallis | **Stevens 1888 vol.2 pp.172-173, item 162, page image checked this session** | **text known (C)** — full letter in clear; tagged "[Duplicate, in Cypher.]" | none; this item is found-solved |
| 2380 (PRO 30/55/19/98) | 22 Oct 1779 | Clinton to Haldimand | HMC Report calendar paraphrase only (1904-09), page not opened | partly known (paraphrase, not a verified decipherment) | outside Saberton's Common cipher scope (Haldimand, not Cornwallis/Clinton; also 2 years before the CP pt.11 window) — open the HMC Report's own printed volume/page |
| 2894 (PRO 30/55/24/76) | 1780 (year only) | Clinton to Haldimand | content matched to a British Museum/Library comparison copy per HMC's own 1904-09 note (BL Add MS 21807, fos.159/161); **Brymner's Canadian calendar (B.147 = Add MS 21807, AX-HMC2 26 Sept) independently calendars a "Clinton to [Haldimand]. Letter in cypher" dated 6 July 1780, matching HMC's cited date exactly, but gives no content** | known elsewhere (via the BM/BL copy, not by breaking the cipher) | old-numbering decipher citation ("Vol.11 No.117") not found in modern Discovery (AX-HMC2, negative search logged); locate the BM/BL comparison copy directly (specific enough crib: French fleet, 3 May, seven ships of the line) |
| 3868 (PRO 30/55/33/65) | 12 Nov 1781 | Clinton to Haldimand | HMC Report calendar paraphrase only, page not opened | partly known | old-numbering decipher citation ("Vol.11 No.190") not found in modern Discovery (AX-HMC2, negative search logged); outside Saberton's scope (Haldimand correspondent; also after CP pt.11's 19 Oct 1781 end) — open the HMC Report |
| 3853 (PRO 30/55/33/47) | 31 Oct 1781 | Robertson to Haldimand | HMC Report calendar paraphrase only, page not opened; **Brymner's Canadian calendar (B.147 = Add MS 21807, AX-HMC2 26 Sept) independently calendars a matching pair of entries dated 31 Oct ("Robertson to Haldimand... Clinton went on board a fleet... to relieve Cornwallis" / "Same to the same. Letter in cypher"), content-consistent with HMC's "Writes in Sir Henry's absence", but gives no cypher content** | partly known | outside Saberton's scope (Robertson/Haldimand, not Cornwallis/Clinton) — open the HMC Report; the decipher itself (fo.306 per HMC) still unread |
| 4833 (PRO 30/55/42/120) | 23 June 1782 | Haldimand to Carleton | HMC Report calendar paraphrase only, page not opened; TNA Discovery's own description is materially fuller and cipher-tagged, source not identified (AX-HMC 26 Sept); **searched Brymner 1884-89 for the fuller content (AX-HMC2, distinctive phrases "Cedars"/"overland"/"despatched yesterday"), not found; discrepancy still open** | partly known | outside Saberton's scope entirely (different correspondents, different year, different theatre) — open the HMC Report; Haldimand's own outgoing-letterbook, if catalogued, may postdate the 1884-89 window checked |
| 6009 (PRO 30/55/53/7) | 26 Oct 1782 | Beckwith to Mackenzie | HMC Report calendar paraphrase only, page not opened; describes forwarding a ciphered note, may not itself be cipher text | partly known / may not be a cipher-text item at all | outside Saberton's scope — open the HMC Report |
| 6012 (PRO 30/55/53/10) | 26 Oct 1782 | Mackenzie to Patterson | HMC Report calendar paraphrase only, page not opened; describes transmitting a letter in cypher, may not itself be cipher text | partly known / may not be a cipher-text item at all | outside Saberton's scope — open the HMC Report |

**Status.** Line 1 stays `partial`: **5 of 12** named items are now text known (C) — all five Cornwallis-Clinton items inside Saberton's CP pt.11 window (3689, 3753, 3784, 3803, 3813) are fully resolved via Stevens 1888, independent of Saberton's own edition (still unreadable from the cloud, LOCAL-QUEUE row L16 unchanged). The remaining 7 items (2380, 2894, 3868, 3853, 4833, 6009, 6012 — Haldimand/Carleton/general-staff correspondence) stay at the HMC-paraphrase-only footing; no deep work (transcription, key application, cryptanalysis) on any of the 12 items — the 5 resolved ones are found-solved (no key application needed, the plaintext is already in a printed edition), and the other 7 need their own printed source read first, not a cryptanalytic attempt. The Discovery item-level sweep of all six named pieces is complete (above); no new cipher-flagged item was found.

## AX-HMC: HMC Report read directly for the remaining 7 items (26 Sept 2026, LANE AX)

Per this job's brief: located each of the 7 still-unresolved items (2380, 2894, 3868, 3853, 4833, 6009, 6012) in the
HMC Report's own printed calendar text and read the page image directly (not the djvu OCR alone, per this file's
own standing caveat).

**Method.** `archive.org/advancedsearch.php` (1 request) for "Report on American manuscripts... royal institution"
confirmed one archive.org scan per printed volume, distinct from the digest of 14+ duplicate/alternate scans already
on file: **vol.1** `reportonamerica03dorcgoog`, **vol.2** `reportonamerican02grea`, **vol.3**
`reportonamerica02dorcgoog`, **vol.4** `reportonamerican04grea`. Fetched all four `_djvu.txt` files (4 requests,
disk-only, not committed) and grepped for each item's date/correspondent pair rather than for the TNA Discovery
"2380."/"2894." style numbers, which **do not appear verbatim in the print** — those running numbers are TNA's own
Discovery item identifiers, not an HMC in-text numbering scheme (checked: `grep` for every one of the 7 numbers
across all four volumes' djvu text returns zero hits). All 7 items and 4833's cross-reference entry are in **vol.2**
(`reportonamerican02grea`) or **vol.3** (`reportonamerica02dorcgoog`) despite vol.2's IA metadata calling itself
"v.2" — the Haldimand/Carleton correspondence in this Report runs chronologically across the whole set and is not
neatly bounded by item-number range. Page->leaf mapping: vol.2's archive.org `metadata` response embeds a
`page_numbers` field directly (no separate fetch needed, 1 request used for it); vol.3's metadata has none, so its
two items' leaves were found via archive.org's search-inside API (`<server>/fulltext/inside.php?item_id=...&doc=...
&path=...&q="<exact phrase>"`, which returns a leaf number directly; 2 successful calls, 1 mistaken call to a wrong
per-item server hostname that reset the connection, not retried past the one accidental attempt) and cross-checked
against the nearest OCR'd page-number markers in the djvu text. Page images fetched via the `_jp2.zip` zip-member
route (`archive.org/download/<id>/<id>_jp2.zip/<id>_jp2%2F<id>_<4-digit-leaf>.jp2`, no login), 6 leaves, converted
locally to JPEG (Pillow, installed this session). Images and manifest at `images/hmc/` (6 files, 2.6 MB, well under
the 30 MB cap). Total archive.org requests this session: 24 (1.5-1.6s apart, browser User-Agent, no login) —
at the brief's 25-request ceiling; no further archive.org calls made after the 6th image.

**Per-item finding, exactly as printed (rule 4: no H or C grade below is a cryptanalytic result — these are
calendar entries, not decipherments):**

- **2380 (PRO 30/55/19/98), Gen. Sir Henry Clinton to Gen. Haldimand, [1779, October 22]** — vol.2 p.53 (leaf 65).
  Full entry: *"Copy and duplicate. Vol. 11, Nos. 14 & 11. 4 pages & 3 pages. Both in cipher. Copy in the British
  Museum, Addtl. MSS. 21807, fo. 105."* No content paraphrase at all, no decipherment noted anywhere in this entry.
  Text status: **unknown** — the BM copy is only "a copy," not stated to be a decipherment or a plain-text version.
- **2894 (PRO 30/55/24/76), [Gen. Sir Henry Clinton] to Gen. Haldimand, undated (comparison-dated 6 July 1780)** —
  vol.2 p.153 (leaf 165). Full entry: *"Cipher of a letter, no date nor names, but found by comparison to be the
  same as one in the British Museum, Additl. MSS. 21807, fos. 159 and 161, dated 6 July, 1780. Vol. 11, No. 12.
  1 page; decipher 11, No. 117; copy 18, No. 21."* This settles the brief's step (3): the BM/BL comparison copy is
  **British Library (British Museum) Additional MS 21807, folios 159 and 161** (the letter itself, dated 6 July
  1780) — not merely "the same content," a specific dated exemplar. New in this entry, not previously on file here:
  HMC's own note that **a decipherment of this cipher already exists as a manuscript in the same PRO 30/55
  collection, at "Vol. 11, No. 117"** (i.e., what is now catalogued as a piece within PRO 30/55/11), plus a further
  copy at "Vol. 18, No. 21." None of this — cipher, decipher, or copy — is itself printed in HMC; only the
  cross-reference is. Text status: **known elsewhere via the BM exemplar** (unchanged classification from the 23/25
  Sept sweeps), now with the exact shelfmark, and a live archival lead (PRO 30/55/11/117, if that old-numbering
  survives into TNA's modern piece numbering) for the decipherment manuscript itself, not yet located in Discovery
  under a modern reference. Whether BL Add MS 21807 is printed anywhere: WebSearch this session found it is part of
  the "Haldimand Papers" (BL Add MS 21661-21892), of which the "B series" transcripts were calendared by Douglas
  Brymner in the Canadian Report on Public Archives (1884-89) — a real printed calendar of this manuscript group,
  not yet opened or checked against fos. 105/159/161/162/306/308/310/325 (this job's brief did not extend to
  fetching it; named as next step, no copy order placed).
- **3868 (PRO 30/55/33/65), [Gen. Sir Henry Clinton] to Gen. Haldimand, 1781, November 12** — vol.2 p.348 (leaf
  360). Full entry: *"In cipher. Vol. 11, No. 194; decipher, No. 190. 3 pages each. Original in the Brit. Mus.,
  Addtl. MSS. 21807, fo. 308; copies 21807, fo. 310; Public Record Office, Am. & W. I. 142, fo. 150."* Same pattern
  as 2894: no content printed, but **a decipherment manuscript is again noted to exist in the same collection**
  ("Vol. 11, No. 190"). BM shelfmark for the original: Addtl. MSS. 21807, fo. 308 (copy at fo. 310). Text status:
  **unknown** (no plaintext content anywhere in this entry; the archival decipher, if its modern PRO 30/55/11 piece
  number can be found, is the live lead, not a cryptanalytic attempt).
- **3853 (PRO 30/55/33/47), Maj. Gen. James Robertson to Gen. Haldimand, 1781, October 31** — vol.2 p.345 (leaf
  357). Full entry: *"Writes in Sir Henry's absence. Auto draft. Vol. 11, No. 183; in cipher, 182. 1 page. Original
  in Brit. Mus., Addtl. MSS. 21807, fo. 325; decipher 21807, fo. 306."* A one-line paraphrase ("Writes in Sir
  Henry's absence") is printed — more than 2380/3868 get, but far short of the content TNA's Discovery description
  implies for other items in this run. Here the decipherment is explicitly located **in the British Museum
  manuscript itself** (fo. 306), not in the PRO 30/55/11 series. Text status: **paraphrase only**.
- **4833 (PRO 30/55/42/120), Gen. Haldimand to Sir Guy Carleton, 1782, June 23** — vol.2 p.532 (leaf 544). Full
  entry: *"Quebec.—No. 2. Duplicate signed letter. Vol. 11, No. 215. 1 page. Enclosed by Gen. Haldimand to Sir G.
  Carleton, 28 July, 1782. Copies in the Public Record Office, Am. & W. I. 145, fo. 87; State Papers, Foreign,
  Various, 321; British Museum, Addtl. MSS. 21808, fo. 36; 21806, fo. 3."* **No "in cipher" tag and no content
  paraphrase at this citation** — a bare bibliographic cross-reference. This does not match TNA Discovery's own,
  much fuller description for this same item (`C16349906`, re-fetched fresh this session: *"Enclosed is a duplicate
  letter in cypher which he dispatched yesterday, overland. With regard to the exchange of prisoners... engagements
  at the Cedars... exchanged many of the people of Vermont... wish for arrivals from England... Postscript, arrival
  of convoy, and still has not received letter of 5 April."*). Searched for this content directly: exact phrases
  ("engagements at the Cedars", "duplicate letter in cypher", "despatched yesterday" in British spelling) return
  **zero hits** in both vol.2's and vol.3's full djvu text and via archive.org's search-inside index on both
  volumes. **This is a real discrepancy, not resolved this session**: either TNA's cataloguers wrote an independent,
  fuller modern description from the original manuscript (not copied from this HMC calendar entry at all, unlike
  the pattern seen for the other 6 items in this run, where TNA's text visibly matches or condenses the print), or
  the fuller content is printed somewhere else in the Report under a heading this search missed (e.g. under
  Haldimand's own outgoing-letterbook section rather than under "received by Carleton," not checked this session).
  Text status: **paraphrase only in print** (no cipher tag here), but a materially fuller, cipher-tagged description
  exists in TNA's own catalogue from a source not identified in the print.
- **6009 (PRO 30/55/53/7), George Beckwith to Major Fred. Mackenzie, 1782, October 26** — vol.3 p.187 (leaf 203).
  Full entry printed in clear, in full (quoted in the "6009 (PRO 30/55/53/7)" row of the item table already on file,
  confirmed against the image this session, no change). This item is itself a plain-English covering note *about*
  forwarding a ciphered note; it is not itself a cipher document. Text status: **known** (it always was; confirmed
  against the page image rather than the API description alone). Immediately below it on the same page, *"[Sir Guy
  Carleton] to [Gen. Haldimand]. 1782, October 26. Draft. Vol. 47, No. 15. 1 page. Originals in the British Museum,
  Addtl. MSS. 21705 fos. 71 & 78; 21806 fo. 20..."* — no "in cipher" tag on this entry either, so this is **not**
  confirmed to be the ciphered note 6009/6012 describe forwarding; noted as a candidate, not claimed.
- **6012 (PRO 30/55/53/10), [Major] F[red] M[ackenzie] to Major Gen. James Patterson, 1782, October 26** — same
  page, vol.3 p.187 (leaf 203). Full entry printed in clear (confirmed against the image, no change from the
  existing table). Also a covering note about forwarding a letter in cipher, not itself the cipher text. Text
  status: **known** (confirmed against the image).

**What this changes.** The item table's "text known / partly known" column stays as before for all 7 (none of them
newly resolved to a plaintext this session — 6009/6012 were already counted as their own plain covering text, not
as the underlying cipher). What is new: (a) 2894 and 3868 each have a **named, specific archival decipherment**
already on file somewhere in the same collection (PRO 30/55/11, old numbering "No. 117" and "No. 190"), not
findable under that old numbering in a modern Discovery search this session did not attempt; (b) 2894's BM
comparison-copy shelfmark is now exact (Add MS 21807, fos. 159/161) and a plausible printed calendar of that
manuscript group (Brymner, Canadian Report on Public Archives 1884-89) is identified, not yet opened; (c) 4833's
TNA Discovery description contains substantial cipher-tagged content not found anywhere in this session's search of
the HMC print, an open discrepancy worth flagging rather than resolving by assumption.

**Next step per item:** 2380 — no further HMC-print lead, only the BM copy fo.105 (unconfirmed plain/cipher);
2894 — locate PRO 30/55/11 (old numbering) item "117" in modern Discovery, and separately open Brymner's Canadian
calendar for Add MS 21807; 3868 — same PRO 30/55/11 "No. 190" search; 3853 — the decipher is in BL Add MS 21807
fo.306 itself, no PRO-side lead; 4833 — resolve the print/Discovery discrepancy (check Haldimand's own
outgoing-letterbook section of the Report, not attempted this session) before treating either description as
complete; 6009/6012 — found-solved as covering notes; the underlying ciphered note they describe is not identified
with certainty (the "[Sir Guy Carleton] to Gen. Haldimand]" entry on the same page is a candidate, unconfirmed).

**Status.** Line 1 stays `partial`. Item-count unchanged at 5 of 12 text known (C); the other 7 stay at their
existing footing (2 known-elsewhere-via-comparison-copy [2894], 1 paraphrase [3853], 2 no-content-in-print [2380,
3868], 1 paraphrase/discrepant-with-Discovery [4833], 2 known-as-covering-notes-only [6009, 6012]). No decoding
attempted; no novelty classification made (rule 10, left to a verifier).

**Requests this session.** archive.org 24 (1.5-1.6s apart, browser User-Agent, no login: 1 advancedsearch, 4
djvu.txt, 2 metadata, 6 jp2 leaf fetches, 4 search-inside fulltext queries [1 failed on a wrong hostname, not
retried past that], plus the earlier IIIF-endpoint route tried and abandoned when it timed out); TNA Discovery 2
(1 failed with HTTP 500 on an item-level query, 1 succeeded on a piece-level query, `discovery.nationalarchives
.gov.uk`); WebSearch 1 (Haldimand Papers / Add MS 21807 printed-calendar lead).

## AX-HMC2: old-numbering concordance, Brymner's Canadian calendar, 4833 discrepancy (26 Sept 2026, LANE AX)

Per this job's brief: (1) map the "Vol. 11, No. 117" / "No. 190" old-numbering decipher citations (AX-HMC, above)
to a modern TNA Discovery reference; (2) open Brymner's *Report on Canadian Archives* (1884-89) for BL Add MS
21807 fos. 159/161 (2894) and fo. 306 (3853); (3) try to resolve 4833's HMC-print-vs-Discovery-description gap.

**(1) Old "Vol. 11" concordance -- negative, with the false lead ruled out explicitly.** Fetched TNA Discovery's
full item list for piece PRO 30/55/11 (`sps.searchQuery="PRO 30/55/11"`, 121 records) and tested the obvious
hypothesis that the modern sub-reference number (the trailing `/NNN`) preserves the old volume-internal item
number cited by HMC ("Vol. 11, No. 117"): **false**. PRO 30/55/11/117 (id C16174572) is a 29 Aug 1778 Treasury
coal-supply contract letter ("Robinson to Samuel Martin... accepting tender for supplying coal to North America"),
nothing to do with a decipherment, and its own `note` field reads `"Note (old vol 2) enclosed by Robinson to
Clinton, 31 Oct (see item no 1503)"` -- i.e. this item's *own* old-volume tag is **"old vol 2"**, not 11; modern
piece 11's sub-reference numbering (checked exhaustively: contiguous 1-120, no gaps) is TNA's own re-numbering
within the piece, unrelated to the old volume-and-item citation scheme HMC quotes. Searched Discovery instead for
the literal note text `"old vol 11"` (case/punctuation-insensitive on this API: `"old vol.+11"` returns the
identical set) -- 30 records across 14 different modern pieces (8, 11, 16, 19, 29, 31, 32, 39, 42, 46, 49, 51, 52,
62), confirming old volume 11's contents were dispersed across many modern pieces when enclosures were re-filed
with their covering letters (exactly the mechanism already inferred for 4833, see below -- one of the 30 hits
**is** PRO 30/55/42/120 = 4833 itself, tagged "old vol 11"). None of the 30 carries "117" or "190" as its own old
item number in the note text (`"old vol 11" 117` and `"old vol 11" 190` both returned 0 records), and a
site-wide check confirms "decipher" is a real, indexed term at this host (650 hits, mostly the unrelated SP 106
Decyphering Branch series) that simply never occurs in any PRO 30/55 description or note. **Conclusion: items
"Vol. 11, No. 117" and "No. 190" (the decipherments) cannot be located in modern Discovery by text search this
session** -- either they were never given their own catalogue-level item entry (folded into whatever item they
were re-filed with, without a distinguishing note), or their old item number isn't preserved in searchable text
at all. Not chased further (would need the physical box list or a piece-by-piece read of note fields with no
search shortcut). 9 discovery.nationalarchives.gov.uk requests this step (1 reachability probe, 1 HTTP 500 not
retried past the single allowed retry, 7 succeeded), 1.5-1.6s apart, descriptive User-Agent.

**(2) Brymner, *Report on Canadian Archives*, 1884-89 -- found, with an important numbering caveat.** Fetched
`archive.org/advancedsearch.php` (already covered by request budget above) then the full `_djvu.txt` for the six
annual volumes covering 1884-89 (`reportoncanadian1884publ`, `1885publ`, `1886publuoft`, `1887publuoft`,
`1888publ`, `1889publuoft`; 6 archive.org requests, browser User-Agent, 1.5-1.6s apart, disk-only, not committed).
Brymner cites the Haldimand Collection's "B series" (BL Add MS 21661-21892) by his own running volume label
`B.NNN`; grepping for the pattern `B.M., 21,80N` (the printed BL shelfmark, comma-separated) in
`reportoncanadian1887publuoft.txt` pins **BL Add MS 21807 = Brymner's B.147** exactly (B.146 ends at Add MS
21,806, the B.147 section runs from Add MS 21,807 to just before B.148/Add MS 21,808 -- confirmed by the printed
running heads "B.147 / HALDIMAND COLLECTION" bracketing the whole section, lines ~101883-103856 of that file).

- **2894 (Clinton to Haldimand, comparison-dated 6 July 1780, fos. 159/161).** Two candidate cypher entries found
  in B.147's 1780 section, and they are **not the same entry** -- this matters, see caveat below.
  - Dated **"July 6, New York"** in Brymner's own date column (exactly HMC's cited date): *"Clinton to the same
    [Haldimand]. Letter in cypher. 184"* -- no content given, immediately following an Admiral Arbuthnot entry
    about a 6-ship, 4,000-troop Brest force ("Page 182") and immediately followed by more July 1780 Quebec
    entries. This is the better match **by date**, independent of any page-number coincidence.
  - Dated **"May 15, Jamaica, Long Island"** (per the date-column sequence; two-column OCR reflow makes this
    pairing less certain than the July 6 one): *"Clinton to the same. Letter in cypher, also one from Knyphausen
    of same date. 158 to 161"* -- the page range 158-161 numerically brackets HMC's cited folios 159 and 161
    almost exactly, but the date (mid-May, not 6 July) does not match HMC's citation.
  **Caveat, not resolved this session: Brymner's "Page NNN" is very likely the pagination of his own transcript
  copy held at the Canadian Archives (Brymner's collection is copies made from the London originals for Canada,
  per this file's own "Add MS 21807... calendared by Douglas Brymner" note), not the British Library's own
  foliation of Add MS 21807 -- the two 1780 entries above use "Page" numbers that go 154, 155, 158-161, 162, 164,
  165, 171, 175, 179, 180, 181, 182, 184... i.e. climbing through the 150s-180s across entries from March through
  July 1780, which cannot all be BL folio numbers for a five-month span of a ~380-page-a-year volume unless
  Brymner's "Page" and the BL's "folio" happen to track closely by coincidence.** So the 158-161 folio-range
  match to HMC's fos. 159/161 may be exactly that -- a coincidence of two independent numbering schemes -- while
  the July 6 date match to Clinton-to-Haldimand-cypher is a stronger, numbering-independent match. Either way,
  **no plaintext or decipherment content is given for this item in Brymner** -- consistent with HMC's own
  admission that 2894's content is known only via comparison to the BM copy, not from a printed decipherment.
  This does not change 2894's status (still known-elsewhere-via-comparison-copy, not text known).
- **3853 (Robertson to Haldimand, 31 Oct 1781, decipher at fo. 306).** Found and a strong content+structure match:
  dated **"October 31, New York"**, two consecutive entries from Robertson to Haldimand --
  first the plain letter (*"Clinton went on board a fleet with 6,000 men, to relieve Cornwallis, who surrendered
  on the 19th, the day the fleet sailed. Sir Henry and Digby will consider the Vermont business on their return...
  381"*) -- matching HMC's own terse paraphrase for 3853, "Writes in Sir Henry's absence" (Robertson writing
  because Clinton has sailed with the relief fleet, exactly as this entry describes) -- immediately followed by
  *"October 31, Same to the same. Letter in cypher. 406"*. **"406" is very plausibly an OCR misread of "306"**
  (matching HMC's cited decipher folio, fo. 306, almost exactly) but this is not confirmed against a page image
  this session -- flagged for a future worker to check the actual leaf rather than trust the djvu OCR digit.
  As with 2894, **no content is given for the cypher portion** -- Brymner, like HMC, marks it "in cypher" and
  stops; this does not change 3853's status (still paraphrase-only, decipher location known but content
  unread/unprinted).

**(3) 4833 discrepancy -- not resolved, negative search logged.** AX-HMC's flag: TNA Discovery's own description
for PRO 30/55/42/120 (4833) carries substantial cipher-tagged content ("Enclosed is a duplicate letter in cypher
which he dispatched yesterday, overland... engagements at the Cedars... exchanged many of the people of
Vermont...") not found anywhere in the HMC print. This job's step (1) search (above) independently re-confirmed
4833 is itself tagged `"Note (old vol 11) enclosed by Haldimand to Carlton, 28 July 1782."` in Discovery -- i.e.
it is *also* an old-vol-11 enclosure, re-filed with its covering letter, same mechanism as the rest of that
volume's dispersed contents. Searched for the Discovery description's distinctive phrases ("Cedars", "overland",
"despatched/dispatched yesterday") across all six 1884-89 Brymner volumes: "Cedars" hits exist but all are
unrelated 1770s Lachine-canal/Cedars-garrison logistics entries (a common place name in this correspondence, nothing
to do with 1782 Haldimand-Carleton letters); no hit for "overland"+"yesterday" together, and no "Letter Book" /
"out-letters" / "outgoing" heading found in the 1888 or 1889 volumes to suggest a distinct Haldimand
outgoing-letterbook section exists in this window. **The discrepancy is not settled**: neither Brymner
(1884-89) nor a further HMC-print search (not re-attempted this session, out of scope for this job) has been
found to carry the fuller Discovery-only content. Two explanations remain open, as before: a modern TNA
cataloguer wrote 4833's Discovery description from the original manuscript directly (bypassing the HMC calendar
entirely), or the richer content sits in a Brymner volume/section not fetched this session (a Haldimand
outgoing-letterbook series may postdate 1889, i.e. outside this job's named window, or use different indexing
terms than tried here). No archive.org requests spent on this step beyond the six volumes already fetched for
(2) -- all searches were local greps of the on-disk text.

**Requests this session (AX-HMC2).** discovery.nationalarchives.gov.uk 9 (1.5-1.6s apart, descriptive
User-Agent; 1 of these got HTTP 500 on first try, retried once per the good-citizen rule, succeeded); archive.org
6 (djvu.txt fetches, browser User-Agent, 1.5-1.6s apart, disk-only, not committed to the repo -- large full-book
OCR dumps, re-fetchable from the identifiers above). No other hosts.

**Status.** Line 1 stays `partial`. Item count and text-known count unchanged at **5/12** -- nothing in this
session promotes 2894 or 3853 to text known; both gain an independent second printed source (Brymner) confirming
the cipher tag, date and correspondents, but neither source prints the deciphered content. 4833's discrepancy is
still open. No decoding attempted; no novelty classification made (rule 10, left to a verifier).

queued JSTOR rows, 26 Sept 2026, QUEUE-FILL.

## JSTOR runner, 26 Sept 2026

- `"Cornwallis" AND "Clinton" AND "York Town" AND 1781 AND cipher`: one **candidate, unread, reread needed**
  (the runner's browser was not logged in to JPASS on this run) -- Marquis de Lafayette, "Victory at Yorktown:
  August 30-December 23, 1781" (book chapter, Lafayette in the Age of the American Revolution -- Selected
  Letters and Papers, 1776-1790, vol. April 1-December 23, 1781), 1981, pp. 367-452,
  https://www.jstor.org/stable/10.7591/j.ctv75d1c8.9 (blocked: "Access through your school, college or
  institution", whether pp. 367-452 print, calendar or discuss the 3 October 1781 Cornwallis-to-Clinton letter
  could not be checked). Requeued in JSTOR-QUEUE.tsv, not `done`; see ASKS.md. Context only, not read: Willcox
  1945 (stable/1879815), Larrabee 1932 (stable/24601667), Greene Papers vol. IX 1997 (stable/10.5149/9781469687995_conrad.12).
- `"Common cipher" AND Cornwallis AND Saberton`: no relevant hit (0 results, none about the letter).

## GAPS-pro3055-clinton-1779 (2 Oct 2026, account-4)

Brief `.claude/briefs/runs/2026-10-02-account4-gaps-step.md`; Verdict step of 1 Oct 2026: H-1649 fetch + 2894 f.186 decipher pilot, with the Discovery date check in the same worker. Clock 02:44-03:3x UTC.

**H-1649 fetch (route recorded in images/h1649/manifest.json).** The Canadiana viewer page for any image of `oocihm.lac_reel_h1649` lists every image's IIIF Image API 2 identifier (saved to `images/h1649/seq_to_iiif.tsv`, all 1266, so no later worker needs the viewer page again). The image host `image-uab.canadiana.ca` answers 403 to a plain request (Cantaloupe "authorize") and 200 with a browser User-Agent plus a `Referer` of the viewer page. Fetched Images 825-830 at 1520 px (reference) and 827, 828, 829 native (6080x4056). Image 827 = reel page 184 = BL fo.159r, the cipher (columns of figure pairs with marginal English glosses by the copyist, address "His Excellency General Haldimand"); 828 = page 185 = fo.159v, the cipher's end, "H C / N. York 6th July 1780 / Cypher L. Initialled", fo.160 blank, fo.160v address, endorsement "From Sir Henry Clinton 6th July Recd 5th Sept by Ensn Cuff of the Nova Scotia Volunteers via Halifax"; 829 = page 186 = fo.161, the period decipherment in clear. Tomokiyo's "f.184 (Image 827) ... decoded on p.186" is confirmed on the images, and so is the 1 Oct note that his and Brymner's numbers are the copied volume's own pagination (page "184"/"186" printed on the leaf) while HMC's fos.159/161 are the BL foliation, written by the copyist in the margin ("fo.159", "fo.161"). Folder 26 MB after the fetch (under the 30 MB line).

**2894 f.186 decipher pilot: 2 blind Sonnet passes + own reconciliation (3 vision units).** Crops: `tools/iiif_lines.py --image` on the text block of img829_full.jpg (defaults found 0 lines on this faint microfilm; `--distance 110 --prominence 40` gave 15 bands, some holding two lines; a second run on the endorsement strip gave 2). Passes `passes/p186_passA.tsv`, `passes/p186_passB.tsv` (17 rows each); reconciliation `passes/p186_reconciled.tsv`; reading `passes/p186_reading.txt`, regenerated by `passes/build_p186.py` (`--check` exits 0 on the committed text, rule 7). Agreement: 6 of 17 crops identical; of the 11 differing, 5 differ only in superscript notation, 5 in whether a line clipped at a crop edge was read at all, 1 in a word (Lawrence/Laurence; crop L11 reads "Laurence"). Tokens of the decipherment body (lines 1-23): **119, H 116, M 3, C 0, S 0, I 0** (rule 4: H because every token is read from the period decipherment itself, the key source; M for "Terney", "a" and "4", each read on the page view only or by one pass with a clipped crop). The fo.161v endorsement (line 25) is a single own read, outside the crop bands. No judge run: the target has no `specs/` entry and the reading is a transcription of clear text, not a decode. The text: "I have received your dispatches of Novr & January &c I have received Information from the Ministers of the 3d May Monsieur Terney is supposed to have sailed about the 3d May with seven ships of the line, & from 20 to 25 Transports &c having on board five Thousand two hundred land Forces & that their destination is stil supposed to be Canada – by Information I have received here the french Armament will assemble at Rhode Island, a division of which will proceed under the Command of the Marquis de Fayette by Connecticut Rivers and No 4 across the lakes to Saint Johns, the other by the river Saint Laurence; — H C 6th July / Copy." It matches HMC's 1904-09 paraphrase of 2894 ("a French force had sailed around 3 May with seven ships of the line...") word for word where HMC quotes, so the Kew cipher (PRO 30/55/24/76) and this decipherment are the same letter; 2894 moves to **text known, grade H** (not C: the text is in manuscript on the reel, not in print; the only prior text located anywhere is HMC's paraphrase). [Corrected by VERIFY-CLINTON-2894, 2 Oct 2026, AUDIT.md: N0. The f.186 text is printed verbatim in Hist. Section, General Staff (Canada), Military and Naval Forces of Canada vol. III (1920), Illustrative Document 170, p.158; the clause is in TNA Discovery's own description of PRO 30/55/24/76 ("Admiral Arbuthnot will be reinforced in proportion") and in McLean to Haldimand, 24 July 1780, Doc. 181, p.165.] What this does not do: it does not verify the cipher against its key (the figure pairs on pages 184-185 are on disk but untranscribed); that is the next step below. Rule 10: report what was found and where it was not found; no novelty class is assigned here.

**Discovery date check (the Completeness gap, ~$1).** Nine date-bounded Discovery queries (`sps.searchQuery=Haldimand`, `sps.recordSeries=PRO 30/55`, `sps.dateFrom=sps.dateTo=` each of Tomokiyo's nine sibling dates) plus one phrase query `"Clinton to Haldimand"` across the series (25 records, saved with full descriptions to `discovery_clinton_to_haldimand_2026-10-02.tsv`). **Six Kew cipher copies not on this folder's item list**, all outside the six pieces AX-STEV2 swept: 2962 (PRO 30/55/25/18, 14 Aug 1780, "a large part of the despatch is encoded"; Tomokiyo f.226, decoded p.225), 3050 (PRO 30/55/26/2, 2 Oct 1780, "3 sides of coding"; Tomokiyo f.242-244, decoded f.245), 3502 (PRO 30/55/29/83, 8 May 1781, "Seven pages of coding"; Tomokiyo f.299, decoded p.308), 3537 (PRO 30/55/30/26, 31 May 1781, "two letters one in code"; Tomokiyo f.311, decoded f.313), 4152 (PRO 30/55/36/22, 22 Feb 1782, "Cypher letter"; Tomokiyo f.11, decoded f.8-10), 4216 (PRO 30/55/36/85, 10 Mar 1782, "In Cipher (second letter deciphred...)"; Tomokiyo f.18A, decoded p.19-20). Two more sibling dates have Kew copies whose descriptions carry content but no cipher flag: 3004 (PRO 30/55/25/60, 9 Sept 1780; Tomokiyo f.224-233 cipher, decoded f.234) and 3077 (PRO 30/55/26/30, 18 Oct 1780, "Number 24"; Tomokiyo f.247, decoded p.246). 9 Sept 1779 gives 2268-2270 (Clinton to Haldimand, prisoner exchanges, recommendations), no cipher flag. Every one of the eight has its Haldimand-side copy and period decipherment on H-1649 at Tomokiyo's positions. Requests: discovery.nationalarchives.gov.uk 10, 1.6 s apart.

Requests this job: heritage.canadiana.ca 3, image-uab.canadiana.ca 12, discovery.nationalarchives.gov.uk 10, WebSearch 8, cryptiana.blogspot.com 2, allthingsliberty.com 1, vermonthistory.org 1. Vision: 2 Sonnet blind-pass calls (17 crops each), 1 own reconciliation read of the 6 disputed crops, plus one orientation look at the three 1520-px page previews to place f.186. Suggested follow-up not run (Usage 7): the same pilot on the other seven decipherments Tomokiyo locates.

## GAPS2-pro3055-clinton-1779 (2 Oct 2026, account-4): the 2894 cipher transcribed and checked against its key

Brief `.claude/briefs/runs/2026-10-02-account4-gaps-step.md`; Verdict step as rewritten at 02:55 UTC 2 Oct 2026: transcribe the figure pairs of H-1649 pages 184-185 and check them against the f.186 decipherment with the 1778 Army List title-page key. Clock 04:24-04:5x UTC. No network: every input was on disk (`images/h1649/img827_full.jpg`, `img828_full.jpg`, `passes/p186_reading.txt`, `sources/cryptiana/web/haldimand.htm`). The plaintext is known (f.186, grade H, GAPS 2 Oct 2026), so this is key work, not a reading claim.

**Crops.** `passes/cut_cipher_cols.py` (column-strip cuts: the cipher is written in columns, so `tools/iiif_lines.py`'s line bands are the wrong unit; ink-profile valleys between the 8 columns of page 184 and the 7 of page 185, each strip split into two halves with one row of overlap and a tick, upscaled 2x) wrote 28 crops to `images/h1649/p184_cols/` and `p185_cols/` with manifests (3.2 MB; folder 28.8 MB).

**Transcription: 2 blind Sonnet passes + own reconciliation (3 vision units).** `passes/cipher_passA.tsv` (363 rows) and `passes/cipher_passB.tsv` (374 rows), one row per entry with the omitted first figure left empty as written; `passes/reconcile_cipher_passes.py` aligned them per crop: 375 aligned rows, 349 agree, 26 disputes (agreement 0.931). 25 of the 26 disputes are the same clear words split differently across written lines; one is a figure (p184_c6a row 12, A "-5" vs B "-15", settled "-5" on the crop). Reconciliation decisions are in `passes/build_reconciled.py` (crops p184_c6a, p185_c4a, p184_c3a viewed; "is sup-/posed to" and "& No 4" are own reads against both passes' "is imp-/possible" and "one 4"/"& the 4"). Result `passes/cipher_reconciled.tsv`: 362 rows, **315 figure pairs** (91 with a written first figure, 224 dash-only) and 47 clear entries (the opening "I have received your Dispatches of Novr & Jany &c" in clear, 17 further clear words or numbers inside the columns, the copyist's margin glosses "fo 159 / See decoded copy transcription p. 186 infra", and the signature block "H C / N. York / 6th July / 1780. / Cypher L. Initialled."). The Verdict line's "2894 cipher figure pairs" meant item 2894's pairs; the count is 315.

**Key check (`passes/check_2894_key.py`; outputs `key_2894.tsv`, `tokens_2894.tsv`, `check_2894.json`; `--check` exits 0).** Word segmentation at the manuscript's own rule lines; dynamic-programming alignment of the 98 cipher units to the 111 words of the f.186 body, iterated once with the majority cells as a prior (hard-EM, the `tools/interlinear_align.py` shape; that tool's numeral-group model does not take two-figure cells, a `--pair-groups` option would be its home); letters 1:1 inside a word, one of a doubled letter dropped as Haldimand's own N.B. prescribes ("supposed" is 7 pairs). Every letter comes from the period decipherment; the independent witness is Tomokiyo's cell table from OTHER letters of the pair (`passes/tomokiyo_key_pairs.tsv`, 210 cells, 9 of them his own flagged miscounts, excluded).

| statistic | target (2894) | control | seeds |
|---|---|---|---|
| cells recovered from f.186 | 166 (170 occurrences in cells seen twice or more) | | |
| internal consistency (occurrences carrying the cell's majority letter) | **165/170 = 0.971** | shuffled plaintext: mean 0.459, max 0.510 | 20 |
| agreement with Tomokiyo's cells, exact | **79/81** | shuffled key (his letters permuted over his cells): mean 5.85, max 9 | 20 |
| agreement with Tomokiyo's cells, -1/-2 tolerance | 79/81 | shuffled key: mean 13.5, max 19 | 20 |

Both controls vary on the statistic's own axis (rule 3): a permuted key or a permuted plaintext changes which letters land in which cells. The two Tomokiyo mismatches are explained, not errors of the key: (9,1) reads `o` here where his table itself carries both `a` (8) and `o` (2); (16,7) reads `e` from f.186's "Terney" where his cell and this cipher's own "Admiral" (below) both give `a` -- the clerk enciphered **Ternay**, and f.186's "Terney" (graded M on 2 Oct) is the decipherer's spelling. The 5 cells with a minority letter all come from the 10-pair "Connecticut" (one n dropped, the clerk's own count off by one inside the word) and "Johns"/"Island" (i/j share 17-4). The title page as the cipher reconstructs it (`check_2894.json`, `title_page_lines_from_2894`) reads as the known wording of the Army List title: line 1 `byp.r.iss.o.o...e....t....u` (By Permission of the Right Honourable), 2 `the.ecre.......a` (the Secretary at War), 9 `o.f.cers.n.....vera.....ment` (Officers in the several Regiments), 13 `br.t.shand.r` (British and Irish), 16 `t.e.o.e....imentofarti..e.yandco..s` (the Royal Regiment of Artillery and Corps), 18 `...themarineso..u.l.ndhal...y` (the Marines on full and half pay), 20 `...da..s.......comm.....ns` (the dates of their commissions) -- grade I as readings of the lines, offered only as the sanity check that the cells fall on an English title page of this book, never used as key.

**Per-token grades (rule 4), 315 pairs: H 264, C 18, M 33, S 0, I 0.** H: the letter is fixed by the period decipherment through an unambiguous word alignment and agrees with the cell's majority (the decipherment is the key source for these). C: a pair in a group f.186 has no counterpart for, read with a cell fixed by known plaintext elsewhere in this letter (below). M: a pair in a word whose length differs from the plaintext word's ("Ministers" 8 pairs, the clerk's "Minister"; "Rivers" 5 pairs, "River"; "Marquis" with its q written as a circled 0 because the title page has no q; "Connecticut"), a pair whose cell no known-plaintext word fixes, or a conflicting cell.

**What the cipher carries that f.186 does not.** Between "Canada" and "The french Armament" the cipher has three figure groups and two clear words with no counterpart in the decipherment: 16-7 16-30 16-13 16-22 16-20 16-7 16-24 (reads `admira.` with cells from Ternay, destination, Monsieur, Terney, line 16 of the title; **Admiral**), the clear "A" (rule under it), the clear "will be", 20-33 20-39 20-37 20-35 20-10 20-9 20-15 20-16 20-13 20-4 (`r......c.d` on own cells, `r...for c.d` adding Tomokiyo's 20-10/20-9/20-15: **reinforced**, 10 letters), 21-9 21-10 (**by**, the cell pair not fixed elsewhere), and 1-3 1-5 1-11 1-3 1-13 1-5 1-15 1-10 1-11 1-12 (`propo rt.on` on own cells plus Tomokiyo's 1-15 t and 1-12 n; **proportion**). The copyist's "By Information / I have received here / The" then follow in clear, and f.186 resumes with "by Information I have received here the french Armament". So the clause "Admiral A[rbuthnot] will be reinforced by [a] proportion" stands in the cipher and not in the period decipherment, whose dash after "Canada –" sits exactly where the clause is skipped (an eye-skip from one "by" to the next). The expansions Arbuthnot and the missing letters (16-24, 20-39/37/35, 20-13, 21-9/10, 1-10) are M; the clause is reported as read from the key at C/H/M, not as a reading at H, and it needs a verifier before it is quoted (rule 10: found in the cipher on H-1649 page 184, not located in f.186, HMC's paraphrase, or any print searched on 2 Oct). Smaller variants: the cipher has "May that Monsieur" where f.186 has "May Monsieur"; "200" in clear for "two hundred"; "& No 4" in clear where f.186 reads "No 4" (its M token confirmed); "a Division of which will" in clear (f.186's M token "a" confirmed).

**Not done, by the brief:** no network, so the 1778 title page itself (archive.org listofgeneralfie00grea_0, image n3, per Tomokiyo) was not fetched; the 15 M cells of the skipped clause and the within-word miscounts can be settled against it in one request. KEY-OFFICES.tsv / KEY-DESIGN.tsv rows for this key (Clinton-Haldimand, 1778-82, book cipher on a title page, line-letter pairs with omitted repeats) are the lane's close-out step, not this worker's. Vision: 2 Sonnet blind-pass calls (28 crops each), 1 own reconciliation (3 crops), plus 2 orientation looks at the 1520-px previews and 1 legibility check of one crop before the passes. Requests: none (no host contacted). Cost: see the lane ledger.

## GAPS3-pro3055-clinton-1779 (2 Oct 2026, account-4): the title page fetched is the 1761 edition; the omitted clause read at C/H/I with one preposition open

Brief `.claude/briefs/runs/2026-10-02-account4-gaps-step.md`; Verdict step as rewritten at 04:42 UTC 2 Oct 2026 (fetch the 1778 Army List title page, archive.org listofgeneralfie00grea_0 image n3, and read the 15 M cells of the clause f.186 omits and line 20 positions 33-39 against it). Clock 05:17-05:4x UTC. Key work on a text already read at H (f.186): not a reading claim.

**The archive.org item is the 1761 edition, not 1778.** Its metadata (images/armylist/metadata.json) gives date 1761, "Complete for 1761", printed for J. Millan; Tomokiyo's own note at haldimand.htm l.99 already says the Internet Archive copies are "of different editions". Leaf n3 (the brief's "image n3") is a blank flyleaf verso: Tomokiyo's link is a two-page-spread view (`page/n3/mode/2up`) in which the facing recto, n4, is the title page. Requests: archive.org 3 (metadata, n3, n4), 1.6 s apart; nothing else fetched. Images: `images/armylist/n4_w2400.jpg` (the native 3243x5221 file, 1.66 MB, is stored resized to keep the folder at 29.8 MiB; URL and sizes in `images/armylist/manifest.json`; n3 deleted as not the key page). Crops: `tools/iiif_lines.py --image ... --out images/armylist/lines --debug` (14 bands x 2 segments, boxes kept in `lines/manifest.json`, the 28 crop files and overlay deleted after the pass and regenerable with the same command). Vision: 1 Sonnet blind pass over the 28 crops (`passes/title1761_passA.tsv`, 37 printed lines, 2 `[?]` both in the bookseller's advertisement) + the worker's own read of the page preview; the two agree on every title-block line; reconciled text `passes/title1761_reading.txt` (27 lines, through "Just published").

**What a 1761 printing can and cannot give (`passes/title_1761_check.py`; outputs `title_1761_map.json`, `m_tokens_1761.tsv`, `clause_2894.tsv`; `--check` exits 0, and `check_2894_key.py --check` still exits 0).** The key counts letters only (no spaces or punctuation): the f.186 cells read lines 1-2 as "bypermissionoftherighthonourable / thesecretaryatwar". A 1761 line number is never trusted; each 1778 key line is mapped to a 1761 printed line by the cells already fixed on it (key_2894.tsv's 166 f.186 cells plus Tomokiyo's independent cells where f.186 has none, 291 cells on 25 lines) and accepted only where every fixed cell agrees with the 1761 text (`full`), or every disagreement is beyond the 1761 line's end or a conflict already logged (`full-allowed`: 16-7, f.186's Terney vs the clerk's Ternay; 13-11, Tomokiyo's j for i), or all cells up to a prefix agree with at least 8 agreeing cells (`prefix-K`, read only to position K). Result: the 1761 page keeps the 1778 wording on 14 of the 25 lines and not on 11, with the line numbers shifting from line 9 (1778 line 9 "Officers in the several Regiments" is three 1761 lines, 8-10; 1778 lines 18 "and the Marines on full and half pay" and 26-27 have no 1761 counterpart at all).

| 1778 line (cells) | 1761 line | agree | status | controls (same statistic): shuffled letters mean / other 1761 lines mean |
|---|---|---|---|---|
| 1 (24) | 1 By Permission of the Right Honourable | 23/24 (1-37 beyond the line) | full-allowed | 0.075 / 0.034 |
| 2 (13), 3 (1), 4 (4), 5 (5), 6 (14), 7 (13), 8 (4) | 2-7 and 5 (the 1761 "A / LIST / OF THE / General and Field-Officers / As they Rank in the Army / Of the") | all cells | full | 0.10-0.28 / 0.04-0.19 |
| 11 (10) | 12 Horse, Dragoons, and Foot | 10/10 | full | 0.105 / 0.077 |
| 13 (14) | 14 British and Irish Establishments | 13/14 (13-11 i/j) | full-allowed | 0.068 / 0.044 |
| 16 (29) | 18 The Royal Regiment of Artillery, Irish Artillery | 21/29: positions 1-27 "theroyalregimentofartillery" agree (16-7 the logged e/a), 28-35 do not (1778 continues "and Corps ...") | prefix-27 | 0.060 / 0.032 |
| 19 (4) | 15 With | 4/4 | full | 0.275 / 0.115 |
| 20 (11) | 16 The Dates of their Commissions, as they Rank in each | 11/11, including 20-33 r and 20-4/9/10/15/16 | full | 0.100 / 0.049 |
| 21 (6) | 17 Corps, and as they Rank in the Army | 5/6: Tomokiyo's 21-17 y vs 1761 n | none (5 agreeing cells, below the prefix floor) | 0.033 / 0.058 |
| 23 (19) | 21 Garrisons at Home and Abroad, with their Allowances, and the | 18/19 (23-25 u vs w) | prefix-24 | 0.074 / 0.040 |
| 9, 14, 15, 17, 18, 22, 24-27 | best 1761 line | 2/6 to 9/21 | none | at the control level |

On the 14 read lines the fixed cells agree with the 1761 text 158/161 (the 3 are the logged 16-7, 13-11 and 23-25); over all 25 best-line pairings 193/291. Both controls vary on the statistic's own axis (which letter sits at which position); on every read line the agreement is 10x or more the shuffled mean.

**Grades (rule 4).** A letter read from the 1761 page is **I** (inferred: the 1778 wording of that line is inferred from a 1761 printing that agrees with every cell fixed on it), never H: H needs the 1778 page itself. The 315 pairs now grade **H 264, C 18, I 23, M 10** (GAPS2: H 264, C 18, M 33); 23 of the 33 M tokens resolve, 10 stay M (21-9, 21-10; the three "Marquis" pairs on 1778 line 18, which 1761 lacks, though Tomokiyo's cells give u-i-s; 16-31 in "Connecticut", beyond the line-16 prefix; 22-6, 17-3, 17-5 in "River"; 17-4 j in "Johns"). Within-word checks: the 8-pair "Ministers" reads m-i-n-i-s-t-e-r from 1761 line 7, so the clerk wrote **Minister** (GAPS2 inferred this); "Rivers" opens r-i on line 1 and Tomokiyo's 22-6 v, 17-3 e, 17-5 r complete **River**; "Connecticut" reads c-o-n-a-e-c-t-c-u-t, the clerk's 16-19 (a) where 16-15 (n) was meant and one letter short, as GAPS2 said.

**The clause f.186 omits, read cell by cell (`passes/clause_2894.tsv`, 32 tokens: C 18, H 2, I 10, M 2).** 16-7 16-30 16-13 16-22 16-20 16-7 16-24 = **Admiral** (a-d-m-i-r-a-l: 16-7 is 'a' on the 1761 page and in Tomokiyo's table, 'e' only in f.186's "Terney"; 16-24 = l from 1761 line 18 within the agreeing prefix, grade I) -- clear **A** -- clear **will be** -- 20-33 20-39 20-37 20-35 20-10 20-9 20-15 20-16 20-13 20-4 = **reinforced** (r C, e I, i I, n I, f I, o I, r I, c C, e I, d C: 1761 line 16 "thedatesoftheircommissionsastheyrankineach", positions 33 r, 35 n, 37 i, 39 e in "as they rank in each"; the three cells fixed on this line beyond position 26 all agree) -- 21-9 21-10 = **M**: under the 1761 wording of the Corps line they read "as", but Tomokiyo's 21-17 y rules that wording out for 1778 and "Corps, and in the Army" (c1 p4 h12 e13 r15 y17) fits all six of his cells and reads **"in"**; the fixed cells cannot separate the two at positions 9-10 -- 1-3 1-5 1-11 1-3 1-13 1-5 1-15 1-10 1-11 1-12 = **proportion** (1-10 = i from line 1, grade I; 1-15 t and 1-12 n Tomokiyo's, H). The separate "ma." group (p185_c3a rows 1-3, 20-18 20-5 20-15) reads m-a-r, followed by the circled 0 that stands for q and 18-17 18-10 18-13 u-i-s: **Marquis** in seven signs, so GAPS2's "Marquis" alignment holds. The clause stands as "Admiral A[rbuthnot] will be reinforced [in] proportion"; the expansion Arbuthnot and the preposition are the open cells. It is a reading from the key on H-1649 page 184 of a passage the period decipherment skipped, not located in f.186, HMC's paraphrase or any print searched on 2 Oct 2026 (search result, rule 10); it needs a verifier before it is quoted.

**Not done, by the brief:** the 1778 title page itself was not located (archive.org holds only the 1761 printing; this worker's hosts were archive.org only). It is the one thing that turns the 23 I tokens to H, settles 21-9/21-10, and tests the 11 lines (131 cells) the 1761 page does not confirm. KEY-OFFICES/KEY-DESIGN rows remain the lane's close-out step.

## GAPS4-pro3055-clinton-1779 (2 Oct 2026, account-4): the 1778 title page itself is on archive.org; every open cell read at H, the clause's preposition is "in"

Brief `.claude/briefs/runs/2026-10-02-account4-gaps-step.md`; Verdict step as rewritten at 05:34 UTC 2 Oct 2026 (locate the 1778 title page: Google Books API full-view, else archive.org other printings, else a HathiTrust LOCAL-QUEUE row; read the 10 M cells and the cells on the 11 lines the 1761 page does not confirm). Clock 06:06-06:2x UTC. Intake gate exit 0 before the step. Key work on a text already read at H (f.186): not a reading claim beyond the clause GAPS2/GAPS3 already named.

**Routes, in the brief's order, each with its result.** (1) Google Books API (`country=US`, key from the environment, never printed), 5 requests: `intitle:"general and field officers"` with `filter=full` answered HTTP 200 with 8 items, none of them this title (a 1719 Law Military, two Cyclopaedias, Britannica -- the intitle operator was not honoured); the same without the filter 0 items; the quoted phrase `"list of the general and field officers"` with `filter=full` and a 1778-worded query both answered HTTP 503 "Service temporarily unavailable"; the one permitted retry of the quoted phrase (after the other hosts had been tried) answered 200 with 3 full-view volumes, dated 1756, 1773 and 1834 -- **no 1778 printing on Google Books full view**. (2) archive.org advancedsearch, 2 requests: `title:("general and field officers") OR title:("general and field-officers")` lists 16 items, among them J. Millan's printings of 1758, 1761, 1767, 1771, 1772, 1773, 1774, 1775, 1776 and **1778 (`listofgeneralfie00grea`, University of Pittsburgh copy, 270 images, 400 ppi, "to which is now added an alphabetical index")**; a year-bounded query (1770-1785) lists 11, the same 1778 item among them. GAPS3 had opened only `listofgeneralfie00grea_0` (1761) -- the suffixless identifier is the 1778 printing. Open Library, 1 request, confirms the same item as its 1778 edition (OCLC 11013774). (3) HathiTrust bibliographic API: 0 requests, not needed once the page was reached; no LOCAL-QUEUE row.

**The page.** archive.org metadata (1 request): date 1778, printed for J. Millan; `_scandata.xml` (1 request) types leaf 13 "Title", leaf 14 "Contents"; `_djvu.txt` (1 request) already carries the title block, including "CORPS and in the ARMY" and MDCCLXXVIII, used only to locate the page. The download path `page/nN` is offset by one from the scandata leaf number: `page/n13.jpg` (fetched first) is the Contents page, `page/n12.jpg` is the title page (fetched second; `images/armylist1778/n12_native.jpg`, 2406x4067, kept at native size as the key source; manifest, URL and sizes in `images/armylist1778/manifest.json`). archive.org requests in all: 8, 1.6 s apart. The imprint reads MDCCLXXVIII with a pencil "1778" under the rule. Crops: `tools/iiif_lines.py --image ... --out images/armylist1778/lines --debug`, 23 bands x 2 segments (boxes kept in `lines/manifest.json`; the 46 crop files and the overlay deleted after the pass, regenerable with the same command). Vision: 1 Sonnet blind pass over the 46 crops (`passes/title1778_passA.tsv`, 32 rows, 0 `[?]`) plus the worker's own read of the two page previews (`passes/title1778_own.txt`); the two readings agree letter for letter on all 30 printed lines (small capitals differ in case only); reconciled text `passes/title1778_reading.txt`.

**Every key line is the same-numbered printed line, and the page confirms all 25 (`passes/title_1778_check.py`; outputs `title_1778_map.json`, `tokens_2894_1778.tsv`, `clause_2894_1778.tsv`; `--check` exits 0, and `title_1761_check.py --check` and `check_2894_key.py --check` still exit 0).** No remapping: 1778 key line L is tested against printed line L with the 291 fixed cells (key_2894.tsv's 166 f.186 cells, Tomokiyo's 125 independent ones). Character convention settled by two of Tomokiyo's own cells: the ampersand counts as a character (27-9 is `&` in his table, line 27 "Clothing, &c."; 22-39 is `m`, which "... Governors, &c. of his Majesty's" gives at 39 only with the & counted); letters-only would give 284/291, with the & 286/291. No 2894 token sits on line 27 or past the & of line 22, so the convention changes no token. The five disagreements are all previously logged or Tomokiyo miscounts: 1-37 (beyond the 32 characters of line 1), 13-11 (i/j), 16-7 (f.186's "Terney" for Ternay: the page gives a), 23-25 (f.186's u for the page's w), 25-19 (Tomokiyo's s where the page has e; s is at 21). Controls on the statistic's own axis: the line's characters shuffled in place (20 seeds) agree at means 0.03-0.28 per line (line 3, a single character, trivially 1.0), every other printed line at means 0.03-0.17; on every line with 4 or more cells the agreement is 3x to 30x the shuffled mean. The 11 lines the 1761 page did not confirm (9, 14, 15, 17, 18, 21, 22, 24-27; 126 cells by this script's count, GAPS3 wrote 131) agree 125/126, the one miss being 25-19.

**Grades (rule 4).** A letter read from the 1778 page is **H** (read from the key source itself). The 315 pairs now grade **H 297, C 18** (GAPS3: H 264, C 18, I 23, M 10): all 23 I tokens become H with the 1778 letter equal to the 1761 letter in every case, and all 10 M tokens become H (none sits beyond its printed line). The 282 H and C tokens that already carried a letter agree with the page 278/282; the 4 are 16-7 three times and 23-25 once, both logged above. Words that were open: **Minister** (7-18 7-11 7-12 7-11 7-2 7-3 7-5 7-7 = m-i-n-i-s-t-e-r), **Marquis** (20-18 20-5 20-15 m-a-r, the circled 0 for q, 18-17 18-10 18-13 u-i-s), **River** (1-18 1-19 22-6 17-3 17-5 = r-i-v-e-r), **Johns** (17-4 i for j, 18-14 o, 18-23 h, 18-21 n, 18-13 s), and **Connecticut** as the clerk wrote it, c-o-n-a-e-c-t-c-u-t (16-31 c, 16-32 o, 16-15 n, 16-19 a, 16-25 e, 16-31 c, 16-21 t, 16-31 c, 1-27 u, 1-22 t: 16-19 a where 16-15 n was meant, one letter short), as GAPS2 and GAPS3 inferred.

**The clause f.186 omits (`passes/clause_2894_1778.tsv`, 32 tokens: C 18, H 14, no I or M).** 16-7 16-30 16-13 16-22 16-20 16-7 16-24 = **Admiral** (16-24 l now H from line 16 "The Royal Regiment of Artillery, and Corps of Engineers") -- clear **A** -- clear **will be** -- 20-33 20-39 20-37 20-35 20-10 20-9 20-15 20-16 20-13 20-4 = **reinforced** (line 20 "The Dates of their Commissions, as they rank in each": r33 e39 i37 n35 f10 o9 r15 c16 e13 d4) -- 21-9 21-10 = **in** (line 21 of the 1778 page is "CORPS and in the ARMY": c-o-r-p-s-a-n-d-i-n, so i9 n10; Tomokiyo's 21-17 y is the 17th character, as GAPS3's better-supported candidate said) -- 1-3 1-5 1-11 1-3 1-13 1-5 1-15 1-10 1-11 1-12 = **proportion** (1-10 i now H). The clause reads **"Admiral A will be reinforced in proportion"**, with "A" the clerk's bare initial (Arbuthnot is the expansion GAPS3 proposed, not a cell) and "mar" opening the separate "Marquis" group. It is a reading from the key on H-1649 page 184 of a passage the period decipherment skipped, not located in f.186, HMC's paraphrase or any print searched on 2 Oct 2026 (a search result, rule 10); **clause ready for a verifier** (C 18, H 14). [Corrected by VERIFY-CLINTON-2894, 2 Oct 2026, AUDIT.md: N0. The f.186 text is printed verbatim in Hist. Section, General Staff (Canada), Military and Naval Forces of Canada vol. III (1920), Illustrative Document 170, p.158; the clause is in TNA Discovery's own description of PRO 30/55/24/76 ("Admiral Arbuthnot will be reinforced in proportion") and in McLean to Haldimand, 24 July 1780, Doc. 181, p.165.]

**Folder size.** The folder stood at 29.8 MiB before this step; with the native 1778 page it crossed 30 MiB, so the superseded 1761 reference copy is re-stored at 1600 px wide (`images/armylist/n4_w1600.jpg`, manifest updated, regenerable from its URL) and the three 1520-px copies of H-1649 images 827-829, whose cited full-size files sit beside them, are deleted and marked `deleted` in `images/h1649/manifest.json` (regenerable by resizing the `_full` file or refetching); 29.85 MiB after. Requests per host this job: www.googleapis.com 5, archive.org 8, openlibrary.org 1; HathiTrust 0. KEY-OFFICES/KEY-DESIGN rows remain the lane's close-out step.

`python3 tools/gaps_check.py pro3055-clinton-1779` (06:2x UTC, after the edits below): `OK keep-going pro3055-clinton-1779: keep going: 7 internal gap(s), 2 step(s) untried` / `gaps_check: 1 checked: 0 parked, 1 keep-going, 0 FAIL, 0 skipped`, exit 0. `tools/intake_gate_check.py` after the step: exit 0.

## Premise check (GAPS5-pro3055-clinton-1779, 2 Oct 2026)

Adversarial pre-reading pass per `.claude/briefs/check-solved.md` "Premise check" (a)-(d), run 2 Oct 2026 13:26-14:0x UTC (clock read) on every item of this folder still open after item 2894's N0 (AUDIT.md), with (d) the recipient side weighted as the 2894 lesson requires. Scripts, not eyes: the recipient-side volumes were fetched once as archive.org `_djvu.txt` to the session scratchpad (not committed, re-fetchable by identifier) and grepped by date, correspondent and Tomokiyo's incipits. Sources: (d1) Historical Section of the General Staff (Canada), *A History of the Organization, Development and Services of the Military and Naval Forces of Canada ... with Illustrative Documents*, vol. III (1920), archive.org `vol1t3historyoforganiz01quebuoft` (vols I-III bound; the "(NNN)" document numbers below are the ones printed at the foot of each document, which run one higher than the volume's own table of contents from no. 259 on); (d2) Brymner, *Report on Canadian Archives* 1887 (`reportoncanadian1887publuoft`), sections B.147 (= Add MS 21807, lines 101883-103856 of the djvu) and B.148 (= Add MS 21808, from line 103857; the 1888 Report opens with B.149 = 21809) and 1888 (`reportoncanadian1888publ`); (d3) the Carleton/Dorchester papers are PRO 30/55 itself, read in HMC (AX-HMC) -- no other Dorchester edition located; (d4) Stevens's *Facsimiles*: **unreachable** this session (two archive.org advancedsearch title queries, 0 results; HathiTrust is cloud-blocked); (d5) Davies, *Documents of the American Revolution 1770-1783* (Colonial Office series): on archive.org as lending-only items (`documentsofameri00NNgrea`, 23 found), full text searchable through be-api fts without a loan; one "Haldimand" query each on vol. 19 and vol. 20 (= Transcripts 1781: its single returned snippet lists "Frederick Haldimand to Sir Henry Clinton, 29 September ... 233" and Haldimand-to-Germain letters of 23 Oct and 18 Nov 1781), the one-snippet-per-item limit means a Clinton-to-Haldimand letter in that volume would not show; **not settled** for 3868 (whose PRO copy "Am. & W.I. 142, fo.150" is CO 5, Davies's own series). Request count: archive.org 9 (3 djvu, 4 advancedsearch, 2 be-api fts), image-uab.canadiana.ca 3 (the reel frames, GAPS5 section below), 1.6 s apart, nothing else.

(a) folder mentions of decipherments, (b) other solvers' working files, (c) physical neighbours, (d) recipient-side editions:

- **2380** (PRO 30/55/19/98, Clinton to Haldimand, 22 Oct 1779). (a) found, not opened: Tomokiyo haldimand.htm (on disk) places the cipher at f.120-122 (Image 758-) and the decipherment at p.134-, incipit "I was honored with your letter of the 19th July"; HMC vol.2 p.53 cites no decipher. (b) not found: Bourdeau's and Aymeloglu's repositories grepped 25 Sept (CX2) and re-cloned by the verifier 2 Oct (AUDIT.md: no haldimand hit); Tomokiyo gives only the incipit. (c) found as citation only: Brymner B.147 p.118/120 (1887 Report), Knyphausen's and Robertson's letters of 31 Jan 1780 "covering a letter in cypher from Clinton, dated 22nd October, 1779, received in Quebec on the 24th of May, 1780"; **data conflict** -- Brymner describes the undated explanation at p.134 as "an abstract of the contents" of the 9 Sept 1779 letter (p.85), while Tomokiyo reads p.134 as the decode of 22 Oct 1779; to settle on the reel images, not here. (d) not found: no 22 Oct 1779 document in the 1920 vol. III (its narrative chapter does not mention the letter); the incipit "honored with your letter of the 19th July" absent from vol. III and from Brymner; Davies not seen. **Verdict: open, clear to test.**
- **3803** (PRO 30/55/32/116, Clinton to Cornwallis, 30 Sept 1781). Text known at C since AX-STEV2 (Stevens 1888 vol.2 pp.172-173, item 162, printed in full). (a)-(d) not re-run: the item is closed as text-known; nothing in this pass contradicts it. **Verdict: text-known (Stevens 1888 vol.2 pp.172-173).**
- **3868** (PRO 30/55/33/65, Clinton to Haldimand, 12 Nov 1781). (a) found, not opened: Tomokiyo f.382 (Image 1030), decoded p.385, extract "... of your proclamation and"; HMC's decipher "Vol.11 No.190" untraceable (AX-HMC2). (b) not found (as 2380). (c) citation only: p.385 beside p.382 on the reel. (d) **found in part**: 1920 vol. III p.214, doc. (262), "Series B, Vol. 147, p. 386", prints the postscript verbatim -- "P.S. General Arnold says Monsr. du Calvet, pere Floquet, Messrs. Hay, Cord, Freeman and Wattis were friends to the Rebels. Endorsed -- From A. 1781. Sir Henry Clinton. 12 Novr. Rec'd 14 May. 82 By Davis" -- and Brymner B.147 p.385 paraphrases the body ("Explanation. Approves generally of Haldimand's course; the change of boundaries may require an Act of Parliament, &c. Arnold says that Du Calvet, Pere Floquet, Hay, Cord, Freeman and Watts were friends to the rebels"). The body itself (p.385) is not printed in either; Davies vol. 20 unresolved (d5). **Verdict: partly text-known (postscript in print, body paraphrased); body open.**
- **3853** (PRO 30/55/33/47, Robertson to Haldimand, 31 Oct 1781). (a) found, not opened: Tomokiyo f.406 (Image 1056) cipher, decoded extract f.381; HMC decipher "21807 fo.306". (b) not found. (c) citation only. (d) **found**: 1920 vol. III p.214, doc. (261) (table of contents no. 260), "Series B, Vol. 147, p. 381", the decipherment printed in full: "Sir Henry Clinton with about six thousand men went on board a fleet of 28 sail of the line to try to relieve Lord Cornwallis. He was forced to surrender on the 19th, the very day our fleet sailed, we have not heard from Sir Henry nor of our fleet. Sir Henry and Mr. Digby who is a joint Commissioner on their arrival will consider and answer your letters about Vermont. I will willingly give a very good Estate in that Country and every Provincial interest to fix these People in the interest of the Crown but I doubt this recent event will defeat all your Trouble -- general Arnold says pere Floquet is an Inveterate Enemy, Jacob roue no better and indeed the gros of the Boston Leaders little better -- he had no Friendly aids from any of the Noblesse. Ever Yours James Robertson. Octr. 31/81. Rec'd 14th May 82." Brymner B.147 p.381 paraphrases the same. **Verdict: text-known (1920 vol. III p.214, from B.147 p.381); not read further.** Open only whether the f.406 cipher carries anything the p.381 extract omits.
- **Cipher enclosure of 4833** (PRO 30/55/42/120, Haldimand to Carleton, 23 June 1782, enclosing the cipher letter "dispatched yesterday"). (a) found, not opened: Tomokiyo's f.65A (Image 1142) Carleton 3 Aug 1782, decoded p.66-67, acknowledges "your excellency's letter of the 22[n]d June". (b) not found. (c)+(d) **found as calendar, and it resolves the AX-HMC/AX-HMC2 discrepancy**: Brymner B.148 (1887 Report) has two entries dated "June 22, Quebec" and one "June 23": Haldimand "to Sir Guy Carleton (No. 1). Congratulating him on his appointment to the chief command ... troops shall by degrees be moved to Isle aux Noix ... The confidential person from Vermont not arrived ... Scouts have been ordered to commit no hostilities in Vermont. [p.]39" and "Same to Clinton. Sends duplicate of letter already sent in cypher. In case the question of exchanges should be brought up, states that no exchange had been entered into, nor would be until the engagements of the Cedars and others had been fulfilled, the people of Vermont having, however, been excluded from this resolution ..." -- the latter is TNA Discovery's description of 4833 almost word for word, so Discovery's fuller text came from the letter itself (as Brymner calendars it), not from the HMC print. The 22 June cipher letter is therefore Haldimand's No. 1 of 22 June 1782 (B.148 p.39), known in Brymner's paraphrase only; no verbatim print (1920 vol. III has no 22/23 June 1782 document). **Verdict: content paraphrased in print; token-level text open.**
- **Ciphered note forwarded by 6009/6012** (PRO 30/55/53/7 and /10, 26 Oct 1782). (a) found, not opened: the candidate Carleton to Haldimand 26 Oct 1782 (HMC vol.3 p.187). (b) not found. (c)+(d) Brymner B.148 calendars one Carleton-to-Haldimand letter dated "October 26, New York"; the two-column OCR reflow leaves it either the p.117 entry ("Refers to him the claims of Dr. Smyth for settlement. Respecting the payment of messengers") or the p.123 entry ("Copies of letters in cypher"); 1920 vol. III: not found (its only 26 Oct 1782 document is Haldimand to Townshend). Since B.148 p.123 is Image 1205 (Tomokiyo) and the reel's END card is Image 1266 (GAPS5 below), pp.111-130 of 21808 are on H-1649 at about Images 1193-1212. **Verdict: open; cheapest next step is Images ~1199 (p.117) and 1205 (p.123), not another reel.**
- **Further Kew copies found 2 Oct (GAPS, discovery_clinton_to_haldimand_2026-10-02.tsv):** **2962** (14 Aug 1780) **found** verbatim, 1920 vol. III p.168, doc. (190), "Series B, Vol. 147, p. 223" ("Monsieur Ternay arrived the 12th ultimo at Rhode Island with seven sail of the line, three Frigates and about five Thousand Troops who are said to be sickly ... Endorsed: Chiffre du ch. Clinton du 14me d'Aout. 80") -- **text-known**; **3004** (9 Sept 1780) **found** verbatim, pp.170-171, doc. (197), "Series B, Vol. 147, pp. 234-5" ("On the 16th of last month I dispatched a Messenger by Land ... Endorsed. From Sir H. Clinton in Cypher of 9th Sept.") -- **text-known**; **4152** (22 Feb 1782) **found** verbatim, pp.217-218, doc. (267), "Series B, Vol. 48, pp. 98-9" (the B.48 letter-book copy, not B.148; "I think it right to send by Express to Your Excellency the following Intelligence which has just been communicated to me by the Honourable William Smith ...", matching Tomokiyo's f.8-10 incipit word for word) -- **text-known**; **3050** (2 Oct 1780), **3077** (18 Oct 1780), **3502** (8 May 1781), **3537** (31 May 1781), **4216** (10 Mar 1782): **not found** in vol. III by date or by incipit ("Arnold discovered", "West Point", "miscarriage of the Quebec", "Vermont deserves", "Drummond ... have not reached me", "scarcely to be expected" all absent) -- open. Aside, not in this folder's list: vol. III also prints Clinton to Haldimand 9 Nov 1780 "(in cypher)" (doc. 220, Discovery 3138, PRO 30/55/26/91) and Haldimand's own cipher letters to Clinton of 13 Aug 1780, 3 Jan 1781, July and 2 Aug 1781, 3 Oct 1781 and 28 Apr 1782 (docs 188, 221, 247, 248, 256, 271).

Summary: 5 items newly text-known from print (3853, 2962, 3004, 4152; 3868 in part), 1 explained (4833's Discovery text is Brymner's B.148 calendar entry), 0 found-solved beyond what AUDIT.md already holds; 2380, 3050, 3077, 3502, 3537, 4216, the 3868 body, the 22 June 1782 letter and the 26 Oct 1782 note stay open. A search result, not a novelty verdict (rule 10).

## GAPS5-pro3055-clinton-1779 (2 Oct 2026, account-4): reel labels of H-1649 read

Verdict step of the 1 Oct gaps section (gap 6): Images 1, 637 and 1266 of `oocihm.lac_reel_h1649` fetched once at 1400 px (image-uab.canadiana.ca, 3 requests, browser UA + Referer, route in images/h1649/manifest.json), stored at 700 px in images/h1649/ (the folder sits at 29.96 MiB), read on one three-frame montage (vision call 1 of 2). **Image 1 is the reel's "START / DEBUT" card only; Image 1266 is the "END OF REEL / FIN DE LA BOBINE" card only** -- neither carries a volume list. **Image 637 is the title leaf of Add MS 21807**: "Haldimand Papers. Correspondence with Sir H. Clinton, Sir Guy Carleton, and other Officers at New York, 1777-1783. Vol. I. Presented by W. Haldimand Esq. Jan. 1857. Mus. Brit. 21,807", confirming the 1 Oct inference that 21807 begins at Image 637 (so Images 1-636 hold an earlier volume, still unidentified: 21806/B.146 by position, unconfirmed). A typed LAC label strip stands beside the title leaf; the second vision call went to a mis-aimed crop (the leaf's edge, not the strip), so the strip is cropped correctly to images/h1649/img637_label_strip.jpg and left unread. What the step settles: the reel ends at Image 1266 with a plain END card, and Tomokiyo's B.148 p.123 = Image 1205, so the late-1782 pages of 21808 up to about p.180 are on this reel, not the next; the 48-reel Canadiana list was not opened (no request left under the 12-request ceiling) and is not needed for the 26 Oct 1782 note (Premise check, 6009/6012). Requests: image-uab.canadiana.ca 3; vision calls 2 of 2 (one montage read, one failed crop).

## GAPS6-pro3055-clinton-1779 (2 Oct 2026, account-4): the 26 Oct 1782 "ciphered note" identified -- B.148 p.123 (Image 1205), a cipher copy of Carleton to Haldimand, 25 Sept 1782

Verdict step of the gaps section (gap 6), run 14:19-14:4x UTC 2 Oct 2026 (clock read). Intake gate exit 0 before the step. Images 1199 and 1205 of `oocihm.lac_reel_h1649` fetched once at 1600 px (route in images/h1649/manifest.json; Image 1205 also at 3040 px and full/max to the session scratchpad for cropping, not committed), crops cut with `tools/iiif_lines.py --image` (centres by eye, recipe in images/h1649/p123_lines/manifest.json; the crops are polarity-inverted by a worker error, noted there), two blind Sonnet passes on the Image 1205 crops (passes/p123_passA.txt, p123_passB.txt) and one reconciliation look by the worker at the three disagreement crops (passes/p123_reconciled.tsv). Image 1199 is stored and unread (the three vision calls went to 1205).

**What the page shows (Image 1205 = the opening B.148 pp.122-123 of BL Add MS 21808).** The LAC label strip in frame reads "British Library, Haldimand Papers, Correspondence with Sir H. Clinton, Sir Guy Carleton and Other Officers at New York, n.d., 1782-1783, MG 21, Add. Mss. 21808, (B-148)" (both passes word for word; it is the 21808 counterpart of the 21807 strip GAPS5 left unread). p.123 is a cipher letter in the Haldimand-Clinton figure-pair system (first column 3-4, x16-31, -32, -15, -40, -20, -3, -35, -35: 8/8 agree with Tomokiyo's f.123 extract, haldimand.htm, after the fifth pair, read 48[?] by both passes, was settled as 40 on the crop), with the folio note "fo. 124", a pencil archivist's note "See another copy (Differently arranged) on pp. 126-8 infra. (For de-coded copy, see p. 102 supra; also B. 146, p. 54)", clear words in the last column "The L'Aigle of 44 Guns Capt. Latouche a valuable Ship of 20 Guns with bale goods from France were lately taken in", and the foot "Each column is continued on the page following." The facing p.122 is a faint clear letter neither pass could read (the one guessed address line disagrees: "Sir Henry Clinton" vs "Sir Guy Carleton"); no token is claimed from it.

**Identification (graded by what the page shows and by the print).** The cipher item at B.148 p.123 (Image 1205) is a copy of Carleton's cipher letter to Haldimand of **25 September 1782**, New York: (i) Tomokiyo's own list entry, "f.123 (Image 1205) Carleton to [Haldimand?], 25 September 1782, another copy on f.126-128 (Image 1208), decoded on f.102 (Image 1183)"; (ii) the pencil note on the page points to the same decoded copy (p.102) and the same second copy (pp.126-8); (iii) Brymner, *Report on Canadian Archives* 1887, B.148, calendars p.102 under "September 25, New York" as Carleton to Haldimand reporting the Congress/Pennsylvania preparations against the Indian country, Paterson ordered to reinforce from Nova Scotia, the fleets, and "'L'Aigle,' Captain Latouche, of 44 guns, and a valuable ship of 20 guns, loaded with bale goods from France, were taken in the Delaware" -- the clear words on p.123 word for word (C 18 of 21). Brymner calendars **p.123 itself under "October 26, New York": "Carleton to Haldimand. Copies of letters in cypher. 123"** -- the two-column OCR reflow that GAPS5 could not resolve resolves from the calendar's own order: its two New York entries for October (16th, 26th) stand against its two Carleton entries in order (p.117 "claims of Dr. Smyth ... payment of messengers", p.123 "Copies of letters in cypher"), so p.117 (Image ~1199) is the 16 Oct letter and p.123 the 26 Oct item. **So the "ciphered note for General Haldimand" that 6009 (Beckwith to Mackenzie, 26 Oct 1782) and 6012 (Mackenzie to Patterson, 26 Oct 1782) describe forwarding is, by this calendar and this page, Carleton's re-sent copies of his 25 Sept 1782 cipher letter -- B.148 p.123 ff. and the "differently arranged" copy pp.126-8 -- under Carleton's one-page covering letter of 26 Oct 1782 (HMC vol.3 p.187, draft PRO 30/55 vol.47 no.15; originals BL 21705 fos.71/78 and 21806 fo.20; the pencil note's "also B.146, p.54" is a further decoded copy in Add MS 21806 = B.146).** Grade of that link: I (inferred from the calendar date, the only 26 Oct 1782 New York entry in B.148 being the cipher copies), not read from a page naming 6009/6012; the content identification (p.123 = the 25 Sept letter) is C/H as graded below. HMC's reading of the 26 Oct draft as "1 page" fits a covering letter whose enclosure is these copies.

**Text status of the item.** The letter's content is in print as Brymner's calendar paraphrase (B.148 p.102 entry, 1887 Report); no verbatim print found: the 1920 *Military and Naval Forces of Canada* vol. III djvu (archive.org `vol1t3historyoforganiz01quebuoft`, one request) has no "Aigle", "Latouche", "Verplanck" or "Munsey" hit, so the 25 Sept 1782 letter is not among its Illustrative Documents -- a search result, not a novelty verdict (rule 10). Its period decipherment is on the reel at B.148 p.102 = Image 1183 (Tomokiyo), unread; no reading of the letter is claimed here.

**Grades (rule 4), identification tokens only:** H 66 (folio note 2, pencil annotation 20, foot 8, LAC label 30, binding label 5, one cipher pair beyond Tomokiyo's extract), C 27 (page number 1, 8 cipher pairs against Tomokiyo, 18 clear words against Brymner p.102), I 1 (the 6009/6012 link), M 0 (p.122 left unread rather than guessed). Pass agreement: identical on every identification field (page number, annotation, labels, foot, clear words, first-column pairs), with both passes marking the same three uncertainties (48/40, Bale/Sale, p.122), all three settled at reconciliation except p.122, which is dropped. Control for the pass pair: the two readings were produced independently from the same crops and agree with two independent external witnesses (Tomokiyo's figures 8/8, Brymner's words 18/21) -- a known-answer check, not a shuffle control; nothing cryptanalytic was done.

**Not done, and why:** Image 1199 not read (vision budget), identified as p.117 = 16 Oct 1782 by calendar position only (grade I); the full p.123 cipher not transcribed and p.102 not fetched (a reading step, outside this brief). Folder kept under 30 MiB by re-storing the uncited 1520-px reference copies of Images 825/826/830 at 760 px and deleting the two uncited `iiif_lines.py --debug` overlays in p186_lines/ (regenerable; logged in images/h1649/manifest.json `shrink_log`). Requests: image-uab.canadiana.ca 4 (1199@1600, 1205@1600, 1205@3040, 1205@max), archive.org 4 (two djvu texts, each with one redirect); vision calls 3 (2 blind Sonnet passes + 1 worker reconciliation montage) plus one 1520-px layout look at the frame before cropping (the tool's own "check the overlay" step) -- 4 image reads in all.

## GAPS7-pro3055-clinton-1779 (2 Oct 2026, account-4): the p.102 period decipherment of Carleton to Haldimand, 25 Sept 1782, read; the p.123 cipher cells match it on the 1778 key

Verdict step of the gaps section (gap 6), run 20:23-20:4x UTC 2 Oct 2026 (clock read). Intake gate exit 0 before the step.

**Housekeeping first (folder over the 30 MB line).** AX2-SHRINK pattern: `images_manifest_full.tsv` (every image file with its source and a `cited_by` column) and `regen_images.sh` (re-fetches every source URL into an output directory, never images/, and re-cuts every recorded crop from its manifest box) added. Byte-identical regen tested: Image 829 re-fetched at full size equals the committed `img829_full.jpg` (sha256 b87f13f9...3765); from it `p186_text_region.jpg`, `p186_bottom_region.jpg` and all 15 `p186_lines` crops re-derive byte-identically, and all 28 `p184_cols`/`p185_cols` crops re-derive byte-identically from the original frames through `passes/cut_cipher_cols.py` (now taking `CLINTON_H1649_DIR`); an offline run of the script reproduced the 47 checked crops. Then: `img827-829_full.jpg` (cited) re-encoded JPEG q70 at their own dimensions; the two uncited p186 region crops deleted; after the fetch, the uncited `--debug` overlay deleted and the 16 Stevens/HMC printed-page scans (cited by directory) re-encoded q70 at their own dimensions (their regen converts the archive.org jp2 again, the page not the bytes).

| | bytes (du -sb) |
|---|---|
| before | 31,247,964 |
| after shrink, before fetch | 26,506,937 |
| after Image 1183 and its crops | 26,031,409 |

**The page.** Image 1183 of `oocihm.lac_reel_h1649` (route in images/h1649/manifest.json; 1600 px copy kept, full size 5536x4056 held in the scratchpad for cropping) is the opening B.148 pp.101-102 of BL Add MS 21808. p.102 is a clear copy headed with the margin note "fo 98" and, in the margin, "See another copy transcribed in [B.146, p.54, not in the crops]; Do. in Q. 20, p. 384; Do. from C.O.5, Vol. 107, p. 289; Do. from R. I. Am. MSS. Vol. 47, Nos. 13 & 14. (For copies in cypher, see pp. 123 and 126 infra.)". The last reference ties this page to the p.123 cipher copy GAPS6 identified, and "R. I. Am. MSS. Vol. 47, Nos. 13 & 14" is the Royal Institution (now PRO 30/55) volume 47, the same volume as the 26 Oct covering draft HMC gives as Vol.47 No.15. The text block, 34 lines, ends "in the Delaware. - (Signed)"; Tomokiyo calls it "decoded on f.102".

**Reading** (`passes/p102_reading.txt`, from `passes/p102_reconciled.tsv`): "Congress and the Pensylvania assembly determined to make two incursions into the Indian Country the principle one under Major Genl. Potter will consist of four hundred continental Troops and six hundred Militia and Volunteers are to assemble at fort Munsey near the West branch of Susquehanah the eighth of Octr. and to march from there to the open of Peres Creek head and into the Seneca Country the other, under the Command of General Irwin will consist of one thousand Men a very few of Whom are Continental will assemble at fort Pit early in October and march towards lake Erie. The principal Object is supposed to be against the Seneca Country and the Information given by several Prisoners who have escaped from thence have contributed much to forward the present Expedition. As there is a large force in Nova Scotia I have given Orders to Major General Paterson who commands there to furnish you with any Assistance You may require. The French and Continentals under Genl. Washington are assembled at Verplank's Point. Our Fleet here and the French mostly at Boston - repairing New York - Septr 25th. The L' Aigle of 44 guns Cpt. Latouche and a valuable Ship of 20 Guns with Bale Goods from France were lately taken in the Delaware. (Signed)"

**Passes.** Two blind Sonnet passes on the 42 crops (34 text lines, 7 margin crops, 1 header; `tools/iiif_lines.py --image`, recipe in images/h1649/p102_lines/manifest.json): 31 of 34 body lines and 214 of 217 words identical, with raised-letter marks and punctuation set aside. The 3 differing words were settled in one reconciliation look at a montage of the 5 disputed crops. Line 7's opening "o7," is the tail of the margin "Vol. 107" running into the text crop and is dropped. "L' Aigle" is right, not "Ld.". "Sept 25th" is agreed. Margin "47" and "123 and 126" were also settled.

**Grades (rule 4).** Body 218 words: H 218, M 0 (a period decipherment in the manuscript, read from the image). Margin and header 43 tokens: H 43. Key cells C 21 (below).

**Key check, p.123 cipher cells against this decipherment.** The cipher cells on disk are Tomokiyo's f.123 extract (23 pairs) and the GAPS6 first-column read (9 pairs, 8/8 agreeing with him), in `passes/p123_cells.tsv`. There are 19 letter cells, 2 word-code elements and 1 head pair. Each letter cell was looked up on the 1778 title page (letters and & counted, as `title_1778_check.py`) and compared with the letter of the decipherment's opening it enciphers ("Congress" ... "Pensylvania"; `passes/check_p102.py`, output `check_p102.json`, `--check` exit 0).

| statistic | value |
|---|---|
| page letter = decipherment letter | 19 / 19 |
| shuffled-plaintext control, 1000 seeds (decipherment letters shuffled, same 19 positions) | mean 1.25, p95 3, max 5 |
| word-code elements 10-1, 5-19 = the decipherment's "and", "the" | 2 / 2 |
| distinct letter cells also recovered from 2894 (`key_2894.tsv`) | 10 of 14, agreeing 10 / 10 |

So the p.123 cipher opening is enciphered on the same 1778 title-page key as 2894, and p.102 is its decipherment. The control varies the plaintext side of every comparison, so it can fail where the target passes (rule 3). The head pair 3-4 has no letter value: line 3 is "A", and Tomokiyo gives "d-?". Limit: only the opening 21 cells of p.123 are on disk. A cell-by-cell match of the whole cipher copy (pp.123-124, continued) needs a transcription of its columns, which was not run here.

**Text status (rule 10).** The letter is in print as Brymner's calendar paraphrase only: *Report on Canadian Archives* 1887, B.148 p.102 entry (archive.org `reportoncanadian1887publuoft` djvu, one request). Its content words appear in the reading 44 of 57 times; the misses are paraphrase words and spellings ("preparations", "Pennsylvania", "Verplanck", "British", OCR "contiuentals"). Brymner reads "the British fleet mostly at New York, and the French fleet at Boston", where the page reads "Our Fleet here and the French mostly at Boston". Not found printed in Military and Naval Forces of Canada vol. III (1920, archive.org `vol1t3historyoforganiz01quebuoft` djvu, one request: 0 hits for Munsey, Potter, Aigle, Latouche, Verplank) or in Brymner beyond paraphrase, searched 2 Oct 2026. That is a search result, not a novelty verdict. The verbatim text has other copies the margin names (B.146 p.54, Q.20 p.384, C.O.5 vol. 107 p.289, PRO 30/55 vol. 47 nos. 13-14), none searched here.

Vision calls: 3 (2 blind Sonnet passes + 1 reconciliation montage), plus one layout look at a reduced copy of the frame before cropping (as GAPS6). Requests: image-uab.canadiana.ca 3 (Image 829 full size for the regen test, Image 1183 at 1600 px and full size), archive.org 2 (two djvu texts). Status unchanged: partial.

## GAPS8-pro3055-clinton-1779 (2 Oct 2026, account-4): the 3868 body read from its period decipherment (B.147 pp.385-386); the p.382 cipher cells match it on the 1778 key; the body is in print (Vermont Historical Society Collections vol. II, 1871)

Verdict step of the gaps section (gap 3, "the 3868 body"), run 20:50-21:0x UTC 2 Oct 2026 (clock read). Intake gate exit 0 before the step.

**The pages.** H-1649 (`oocihm.lac_reel_h1649`, route in images/h1649/manifest.json) Image 1030 = B.147 p.382 (BL fo.308): the cipher copy, opening in clear "Nov^r 12th 1781. I received your several Dispatches by His Majesty's Ship Garland, and as there was a Packet upon the point of Sailing for Europe when they arrived, I sent a Copy of your Letter of the 1st October", then six columns of figure pairs with the copyist's English glosses ("to the", "not", "they shall", "and also", "prepare", "marked", "with", "You will not expect more from me by this Conveyance"), address "His Excellency Genl. Haldimand"; margin "See the decyphered copy ... p.385 infra". Image 1033 = p.385 (fo.310): the decipherment in clear, margin "See the initialled cypher of this copied on p.382 supra" and "*Sic" against "proclama^n". Image 1034 = p.386 (fo.310v-311v): its last five lines, signature "H C", the P.S., "Copy", fo.311 blank, endorsement "From A 1781. Sir H. Clinton 12 Nov^r Rec^d 14th May 82 By D---". Tomokiyo's "f.382 (Image 1030) ... decoded on p.385" is confirmed on the images. Pp.383-384 (Images 1031-1032, the rest of the cipher) were not fetched.

**Reading** (`passes/p385_reading.txt`, from `passes/p385_reconciled.tsv`): "I recd. your several dispatches by His Majesty's Ship Garland, & as there was a Packet upon the point of sailing for Europe when they arrived, I sent a Copy of your Letter of the 1st Octr. Of your proclama^n and of the Letter marked a to the minister, not having time to prepare Copies of the Whole, but they shall be sent by the next Opportunity - and also laid before Admiral Darby, who is a joint Commissioner with me, as soon as he arrives in town - You will not expect more from me by this Conveyance Respecting your measures with the Leaders of Vermont than a general Declaration of my Confidence in your Endeavours to Separate that district from the Revolt, and my wish for its success - The extent of the Expectations of the People, and of your promise to meet them will I apprehend make it necessary for the crown to resort to parliament - for the truth is that the Powers of the present Commissioners extend only to granting pardons and restoring Provinces or Districts, {to the Kings} Pya^n Peace and this alone is the reason of my sending to the Secretary of State these Transactions and I hope you will find no difficulty in preventing our enemies from practising upon the jealousies of the Inhabitants of Vermont before the result of the public deliberations can be transmitted - H C" + P.S. "General Arnold says Monsr du Calvert, pere Floquet, Messrs. Hay, Cord, Freeman and Watts were friends to the Rebels - Copy."

**Passes.** Two blind Sonnet passes on 44 line crops (35 on p.385, 9 on p.386; `tools/iiif_lines.py --image ... --ink 45`, boxes in images/h1649/p385_lines/ and p386_lines/manifest.json) plus two cipher-column crops of p.382: 34 of 44 lines and 230 of 246 words identical. Instrument fault, recorded: `--columns 300:1900` also trimmed the crops' left edge (box x from 1820 where the writing starts near 1700), so the first word or letters of nine lines were cut, and both passes guessed there ("affording" for "not having", "was laid" for "also laid", "Ford"/"Cox" for "Cord"). Those words were settled at reconciliation on the 1600 px overlay of the whole region (which shows the full lines) and on a montage of the 14 disputed crops; "not having", "of the Letter", "minister", "time to" and "Copies" are also what the p.382 cipher cells spell (below). A later crop of this page should drop `--columns` or pass the full text width.

**Grades (rule 4).** 252 words: H 248, M 4 ("Letter[?]" (final s open; the cipher and the print give "letter"), the interlinear "to the Kings[?]", "Pya^n[?]" (struck?), "Floquet[?]" (A Floquet, B Flaquet)). Key cells: C 44.

**Key check, p.382 cipher cells against this decipherment** (`passes/check_3868.py`, output `check_3868.json`, `--check` exit 0). Cells: the first two of the six columns, 57 entries (53 cells, 4 glosses), two blind passes agreeing on 56/57 (pass B read one repeated "-4" once; kept as A, which "Letter" needs). Each cell (line, letter; "-N" repeats the previous line figure) looked up on the 1778 title page (letters and & counted, as `title_1778_check.py`), aligned by the copyist's own glosses:

| statistic | value |
|---|---|
| cells compared (of your / of the letter / a / minister / having time to / copies) | 44 |
| page letter = decipherment letter | 44 / 44 |
| shuffled-plaintext control, 1000 seeds (decipherment letters shuffled, same 44 positions) | mean 3.13, p95 6, max 10 |
| "proclamation" cells (1-3 -5 -11 2-6 18-18 -1 -4 -10 -14) | page letters "proclatio": p-r-o-c-l-a then t-i-o, the encipherer dropping "ma" and the final n; the decipherer wrote "proclama^n" and flagged it *Sic |
| distinct cells also in `key_2894.tsv` | 19 of 32, agreeing 19 / 19 |

So the 3868 cipher is enciphered on the same 1778 Army List title-page key as 2894 and the 1782 p.123 copy (GAPS7), and pp.385-386 are its decipherment. The control changes the plaintext side of every comparison, so it can fail where the target passes (rule 3). Limit: only columns 1-2 of six on p.382 are transcribed; columns 3-6 and pp.383-384 are not.

**Text status (rule 10; a search result, not a novelty verdict).** One be-api full-text phrase query (archive.org, "jealousies of the inhabitants of Vermont", 13 items) found the body printed in full: *Collections of the Vermont Historical Society* vol. II (Montpelier 1871), pp.198-199, "H. -- Sir Henry Clinton to Gen. Haldimand. New York, Nov. 6 [or 12], 1781" (archive.org `collectionsofver02vermuoft`, djvu text fetched, excerpt in `passes/vhs2_3868_print.txt`), with the P.S. and an endorsement "Sent overland per dispatched"; the same phrase is in Walton, *Records of the Governor and Council of the State of Vermont* vol. II (1874), Wilbur, *Ira Allen* (1928), and the *Vermont Historical Society Proceedings* 1941 (hits only, not opened). Word comparison of the reading's body with the VHS print: 214 of 229 words equal in order; the differences are "recd"/"received", "&"/"and", "sent" / "transmitted to the Minister" (the print moves "to the Minister" up from "the Letter marked A to the minister"), "Octr"/"of October", "proclama^n"/"proclamation", "had" (print adds), "Darby"/"Digby" (the copy-book reads "Darby"; Admiral Robert Digby is meant), "Pya^n"/"to the King's" (the print has the interlinear correction), "practising"/"practicing", "deliberations"/"deliberation", "H C" (print omits). The print is a different copy (it doubts the date, "Nov. 6 [or 12]") and gives no source or decipherment note in the excerpt. So the GAPS5 premise check's "the body itself is not in print" is corrected: the body is in print verbatim since 1871; the premise check searched the 1920 vol. III and Brymner, not the Vermont editions.

Vision calls: 3 (2 blind Sonnet passes + 1 reconciliation montage), plus four layout looks by the worker at reduced copies (Images 1030, 1033, 1034 at 1600 px; the p.385 and p.386 `--debug` overlays). Requests: image-uab.canadiana.ca 6 (Images 1030, 1033, 1034 at 1600 px and at full/max, full/max to the scratchpad only), archive.org 2 (be-api fts query, VHS vol. II djvu). Folder 27,887,615 bytes (du -sb) after the step: the 1600 px copies of Images 1033 and 1034 deleted (their crops carry the pages; manifest marks them), crops greyscale q70, all 46 new crops re-derive byte-identically from the full/max frames through `regen_images.sh` (`native_for_crops`, now with a quality field). Status unchanged: partial.

## GAPS9-pro3055-clinton-1779 (2 Oct 2026, account-4): 2380 read from its period decipherment (B.147 pp.134-135); the p.134 conflict settled; the p.120 cipher cells fit the 1778 key with a line-1 variant

Verdict step of the gaps section (gap 2, "2380 ... with the p.134 conflict"), run 21:10-21:2x UTC 2 Oct 2026 (clock read). Intake gate exit 0 before the step.

**Premise (print) first.** be-api full-text search on archive.org for the decipherment's opening, "honored with your letter of the 19th July" and "honoured with your letter of the 19th July": 0 items each (the same route found the 3868 body in 13 items, GAPS8, so it is a working path). The 1920 *Military and Naval Forces of Canada* vol. III (archive.org `vol1t3historyoforganiz01quebuoft`, djvu text fetched once to the scratchpad) lists Clinton-Haldimand documents of 1779 as Nos. 67, 76, 81, 108 and Haldimand's of 19 July, 29 Aug, 4 Sept, 1 and 4 Nov 1779, but no 22 Oct 1779 letter. Not located in print by these searches (a search result, rule 10); Brymner's B.147 entry remains the only calendar line. [VERIFY-CLINTON-3868-2380, 2 Oct 2026: superseded -- the text is printed in full in Collections of the Vermont Historical Society vol. II (1871) p.192, misdated under a 27 Oct 1781 heading and opening "I was favored"; the opening was the one phrase that could not find it. See AUDIT.md.]

**The pages and the p.134 conflict.** H-1649 Image 758 = B.147 p.120 (BL fo.105): "Copy", "N. York Octr 22d 1779", seven columns of figure pairs with underlined word ends, "19th July" in clear in column 1, address "His Excellency General Haldimand"; margin "See a decoded copy transcd. on p.134 infra". Image 772 = p.134 (fo.113): the decipherment in clear, "I was honored with your Letters of the 19th July ...", margin "See a cypher copy transcd. on p.120 supra". Image 773 = p.135 (fo.113v-114v): its last nine lines, "Copy", "fo.114 Blank", endorsement "Lettre en Chiffre 1779 du Genl Clinton recue a Quebec par Halifax le 18. Jan[?] 1780", then the next letter (Quebec, 17 Jan 1780). So Tomokiyo's placement holds and the conflict is settled on the images: p.134 is the decipherment of 2380, not an abstract of the 9 Sept 1779 letter as Brymner's calendar has it. [VERIFY-CLINTON-3868-2380: both hold -- p.134 is this cipher's decipherment and its content abridges the 9 Sept 1779 letter, as Brymner says; Tomokiyo's 9 Sept and 22 Oct cell extracts are identical.] Pp.121-122 (Images 759-760, Tomokiyo's f.120-122 span, probably the duplicate) were not fetched.

**Reading** (`passes/p134_reading.txt`, from `passes/p134_reconciled.tsv`): "I was honored with your Letters of the 19th July by the Matross of the Artillery - there are now no hopes of recovering the Army of the Convention by exchange, the Rebels having had nothing in view by the negociation they proposed for that purpose but to still the Clamours of their own Officers Prisoners with us, disappointed so my Expectations of a Reinforcement from the West Indies - however I sent you three Regiments, one of which was British which had they arrived would with the 650 Recruits and Artillery from Europe have amounted to rather more than your demand they sailed under Convoy of the Renown, but unfortunately met with a violent Storm which dispersed the Fleet and damaged the Ships - the Renown has since returned here with seven Companies and some Convalescents of the forty fourth and some part of the Regiment of Lossberg but the whole of the Regiment of Knyphausen and the remainder of the British are missing from the present Situation of Affairs Georgia will be exposed to great Danger unless South Carolina is reduced, having therefore no alternative left, I shall detach a considerable Armament for that Purpose - I hope your Indians will be prevailed upon to threaten the Frontiers of Virginia in great force which will operate in favor of the Southern movements/ while a considerable Fleet may probably be employed to cooperate in the Chesipeak. I have received your Dispatches by the Defiance/"

**Passes.** 49 line crops (36 on p.134, 13 on p.135; `tools/iiif_lines.py --image <full/max frame> --region ... --ink 45`, without `--columns`, the GAPS8 lesson) and four column crops of p.120 (columns 1-2, top and bottom halves). Two blind Sonnet passes: 40 of 49 lines identical; the nine differences are margin fragments the crops caught (".120", "a copy"), a raised flourish after "British", Chesipeak/Chesapeak, recue/reçue and the endorsement month; settled by the worker on one montage of the seven disputed crops. Cipher cells: 95 of 97 entries identical in value (one first figure cut by the crop edge in pass A, read 1-7 on the column preview; 6-77 marked ? by B), one underline differs (kept B). The passes read the crops at q60/q70; the committed crops were re-cut at q50/q45 by `passes/cut_2380_crops.py` to keep the folder under 29 MB (same boxes, same scale).

**Grades (rule 4).** Body 241 words: H 241, M 0. Endorsement: the month "Jan[?]" M (both passes "Jan^y"; the raised letter looks closer to r). Key cells: C 52 (below).

**Key check, p.120 cipher columns 1-2 against the decipherment** (`passes/check_2380.py`, output `check_2380.json`, `--check` exit 0). The underlines split the 96 cells into 26 cipher words; with "19th July" as anchor every one of the 25 word pairs has a cell count equal to the decipherment word's length with doubled letters written once ("leters", "matros", "artilery"), so the alignment is word for word. 93 cells compared (three name positions beyond their line, 2-99, 2-44, 6-77: M).

| statistic | target | shuffled-plaintext control, 1000 seeds |
|---|---|---|
| page letter = decipherment letter (exact) | 52 / 93 | mean 6.87, p95 11, max 15 |
| decipherment letter within +-2 positions on the same line | 89 / 93 | mean 26.6, p95 34, max 39 |
| line-1 cells matching the 1778 page | 25 / 63 | |
| line-1 cells matching "BY PERMISION of the RIGHT HONORABLE" (one s, no u) | 60 / 63 | |
| distinct cells also in `key_2894.tsv` (July 1780) | 19, agreeing 13; the 6 that differ are all line 1 (5) and 18-7 | |

So the 2380 cipher is on the same title-page key, but its encipherer counted line 1 as if it read PERMISION and HONORABLE: every line-1 cell after position 8 falls one place short, and after position 26 two places short, which is Tomokiyo's "-1/-2 error" pattern, here one systematic shift rather than scattered slips. The 2894 cells of July 1780 use the printed line 1. Whether this is a counting habit or a different printing is not settled here. Two other off cells: 9-15 (one place short, as if OFICERS) and 18-7. The cipher's second word reads f-a-v-o-r-e-d on the variant line 1 (1-13 f, 1-27 a, 9-15 v), so the cipher says "favored" where the decipherer wrote "honored"; of the three line-1 cells the variant leaves unmatched, two are this word (1-13, 1-27 against "honored") and one is 1-25 in "artillery" (r, one place long on either count). The control changes the plaintext side of each comparison, so it can fail where the target passes (rule 3). Limit: columns 3-7 of p.120 and pp.121-122 are not transcribed.

Vision calls: 3 (2 blind Sonnet passes + 1 reconciliation montage), plus layout looks by the worker at Images 758, 772 and 773 at 1600 px, a column preview and two `--debug` overlays. Requests: image-uab.canadiana.ca 6 (Images 758, 772, 773 at 1600 px, then the same three at full/max, all to the scratchpad only), archive.org 3 (two be-api fts queries, the 1920 vol. III djvu once). Folder 28,852,351 bytes (du -sb) after the new crops; `regen_images.sh` re-derives them byte-identically through `passes/cut_2380_crops.py` (tested). Status unchanged: partial.

## GAPS10-pro3055-clinton-1779 (2 Oct 2026, account-4): the 4833 enclosure (Haldimand to Carleton No. 1, 22 June 1782) is in print, and the reel copy is clear, not cipher

Verdict step of the gaps section (gap 5, "the 4833 enclosure ... B.148 p.39"), run 21:46-21:5x UTC 2 Oct 2026 (clock read). Intake gate exit 0 before the step. The print check came first and was done on interior phrases, not the incipit (the GAPS9 lesson: VERIFY-CLINTON-3868-2380 found 2380 in print where the opening alone had missed it).

**Print check (premise first).** Sources fetched once as archive.org `_djvu.txt` to the session scratchpad (not committed) and grepped: Brymner, *Report on Canadian Archives* 1887 (`reportoncanadian1887publuoft`); *Collections of the Vermont Historical Society* vol. II (1871, `collectionsofver02vermuoft`); Walton, *Records of the Governor and Council of the State of Vermont* vols II and III (`vermontgovrecords02waltrich`, `vermontgovrecords03waltrich`); the 1920 *Military and Naval Forces of Canada* vol. III (`vol1t3historyoforganiz01quebuoft`). Grep terms: Bellona, two mills, mills on the Mohawk, commit no hostil-, confidential person, and the date written four ways (22d/22nd June 1782, June 22 1782).
- Brymner 1887 calendars the letter twice: B.146 p.2 (Add MS 21806, "General Haldimand to Sir Guy Carleton. Congratulating him on appointment ... Loss of the Bellona ... Isle aux Noix ... Scouts sent to Albany and Johnstown, with orders not to commit hostilities in Vermont") with the 23 June covering letter at B.146 p.5; and B.148 p.39 ("Same to Sir Guy Carleton (No. 1)").
- **VHS Collections vol. II (1871) pp.280-282 prints the letter in full**: "H. -- General Haldimand to Sir Guy Carleton, [No. 1.] Quebec, 22nd June", from "I was last night honored with your letter of the 21st May" to "which the necessity of the service and the want of information have occasioned", with the endorsement "General Haldimand to Sir Guy Carleton, 22d June, 1782. Received July 26th, 1782. No. 7." (footnote source "State Papers, 449-55", i.e. Vermont's MS copies). The 23 June covering letter (= 4833) follows at once, "Duplicate. [No. 2.] Quebec, 23rd June, 1782. Sir: -- The enclosed is a duplicate of a letter in cypher which I yesterday had the honor to dispatch for your Excellency overland. The cypher is very tedious ...". So 4833 and its enclosure are both text-known from 1871.
- Walton vol. II (1874) pp.470-471 reprints the 22 June letter (grep hit "Bellona, which after a fortunate passage to the South Traverse"). Walton vol. III and the 1920 vol. III: no hit on any term.
- be-api full-text search on archive.org, four interior phrases from the 1871 wording (exact phrase, one request each): "fortunate passage to the South Traverse" 8 items; "Two mills only remain on the Mohawk" 4; "confidential person mentioned in my letter of the 27th of May" 4; "move the troops intended for it to the Isle aux Noix" 9. Every hit is a copy of VHS Collections II (`collectionsofver02vermuoft`, `collectionsofver02verm`, `collectionsverm00socigoog`, `collvermont02montrich`, `vermontcoinage00slaf_0`, which carries the same text) or of Walton vol. II (`vermontgovrecords02waltrich`, `recordsofgoverno02verm`, `bwb_Y0-BUJ-231`, `per_uncg_microfilm_walton-eliakim-per_1874_2_cr61`). Earliest located: 1871.

**The reel page.** H-1649 Image 1115 = B.148 p.39 (BL fo.33) and Image 1116 = p.40 (fo.33v-34), fetched at 1600 px (`images/h1649/img1115_w1600.jpg`, `img1116_w1600.jpg`, as fetched; manifest lines added; `regen_images.sh` refetches them byte-identically through its manifest loop). The page is headed "To Sir Guy Carleton / No. 1 / In Cypher", dated "Quebec 22d June 1782", and is written **in clear**: the text the cipher carried, not the cipher. Margin: "fo. 33 ... another copy transcd. in B 146 p.2 ... from C.O.5 106 p.361 ... draft copied from R.I. Am. MSS. Vol. [71?] No. 214". The two pages read by the worker agree with the 1871 print word for word where checked (opening, Bellona sentence, "Isle aux Noix", "confidential person mentioned in my letter of the 27th May", "a small ship that will sail for New York to-morrow"), with one variant: the reel copy reads "the Report of a general Accommodation", the 1871 print "the respect and general accommodation" (an 1871 misreading, by the look of it; not graded, since no reading is claimed). No figure pairs on either page.

**Key test: not possible from this reel.** Rule 3's cells-against-shuffled-plaintext control needs the cipher, and Haldimand's letterbook keeps only the clear text of what he sent. The enciphered copy went to Carleton: the duplicate enclosed in 4833 should sit with it in PRO 30/55 at Kew (not digitised, Discovery C16266110 digitised=false, 1 Oct 2026), and C.O.5/106 p.361 is a Colonial Office copy (also Kew, not checked). B.146 p.2 (Add MS 21806, another reel) is a second letterbook copy and probably clear as well (unchecked). So the token-level reading question is closed by the print, and the key-test question needs Kew (needs-physical-access), which does not hold the target open on its own: this is a key check on a text-known item, not text recovery.

Grades (rule 4): none claimed. No reading was produced and no `--check` script was added, because the text is in print and no cipher was read. Vision calls: 0 subagent calls (the worker looked at the two 1600-px pages directly to see whether they were cipher). Requests: image-uab.canadiana.ca 2 (Images 1115, 1116 at 1600 px, browser UA + Referer, 1.6 s apart); archive.org 10 (5 djvu texts, 1 advancedsearch, 4 be-api fts). Folder 29,253,312 bytes (du -sb) after the two pages. Status unchanged: partial. A search result, not a novelty verdict (rule 10).

## GAPS11-pro3055-clinton-1779 (2 Oct 2026, account-4): print check of the five open siblings -- 3502, 3537 and 4216 are in print (VHS Collections vol. II, 1871; 3502 and 4216 also Walton vol. II); 3050 and 3077 found only as Brymner's paraphrase

Verdict step of the gaps section (GAPS10's: "grep VHS II / Walton II-III / 1920 III for siblings 3050 3077 3502 3537 4216 before any reel pilot"), run 22:38-22:5x UTC 2 Oct 2026 (clock read). Intake gate exit 0 before the step. No vision calls, no image fetch; disk-only after the text fetches.

**Method.** Six archive.org `_djvu.txt` texts fetched once to the session scratchpad (not committed): Collections of the Vermont Historical Society vol. II, 1871 (`collectionsofver02vermuoft`); Walton, Records of the Governor and Council vols II and III (`vermontgovrecords02waltrich`, `vermontgovrecords03waltrich`); Military and Naval Forces of Canada vol. III, 1920 (`vol1t3historyoforganiz01quebuoft`); Brymner, Report on Canadian Archives 1887 (`reportoncanadian1887publuoft`, which calendars B.147 and B.148) and 1888 (`reportoncanadian1888publ`). Each text de-hyphenated across line breaks, whitespace collapsed, lowercased, then grepped per sibling for the date (written several ways), a correspondents-plus-date pattern, and three to five interior phrases taken from Tomokiyo's decoded extracts (sources/cryptiana/web/haldimand.htm) and the Discovery/Brymner descriptions, not only the incipit (VERIFY-CLINTON's lesson). Then eight be-api full-text phrase queries across all of archive.org, two of them positive controls on phrases already found in the djvu texts. Every query and count is below and in `print_check_siblings_2026-10-02.tsv` (with the first three contexts per hit). Counts include unrelated uses of generic phrases ("german troops", "second division", "blocked up"); each non-zero cell was read in context, and the per-sibling verdict rests only on the hits named in the findings.

| sibling | kind | pattern (case-insensitive, djvu text de-hyphenated) | VHS II 1871 | Walton II | Walton III | 1920 vol. III | Brymner 1887 | Brymner 1888 |
|---|---|---|---|---|---|---|---|---|
| 3050 | date | `2(?:d/nd)? October,? 1780/October 2(?:d/nd)?,? 1780/2nd October,? 1780` | 1 | 0 | 0 | 1 | 0 | 0 |
| 3050 | phr | `intention of giving up` | 0 | 0 | 0 | 0 | 0 | 0 |
| 3050 | phr | `complete victory` | 0 | 0 | 0 | 0 | 0 | 1 |
| 3050 | phr | `defection in the spanish` | 0 | 0 | 0 | 0 | 1 | 0 |
| 3050 | phr | `second division` | 1 | 0 | 1 | 5 | 3 | 1 |
| 3050 | phr | `great confusion` | 0 | 0 | 0 | 3 | 1 | 1 |
| 3050 | corr | `clinton to (?:general )?haldimand.{0,40}(?:2/2nd/2d) oct` | 0 | 0 | 0 | 0 | 0 | 0 |
| 3077 | date | `18(?:th)? October,? 1780/October 18(?:th)?,? 1780` | 0 | 1 | 0 | 0 | 0 | 0 |
| 3077 | phr | `miscarriage of the quebec` | 0 | 0 | 0 | 0 | 0 | 0 |
| 3077 | phr | `blocked up` | 0 | 0 | 0 | 6 | 1 | 3 |
| 3077 | phr | `cork fleet` | 0 | 0 | 0 | 2 | 2 | 3 |
| 3077 | phr | `accommodation with spain` | 0 | 0 | 0 | 0 | 1 | 0 |
| 3077 | phr | `quebec fleet` | 0 | 0 | 0 | 0 | 1 | 1 |
| 3077 | corr | `clinton to (?:general )?haldimand.{0,40}18 oct` | 0 | 0 | 0 | 0 | 0 | 0 |
| 3502 | date | `8(?:th)? May,? 1781/May 8(?:th)?,? 1781` | 6 | 3 | 0 | 0 | 0 | 0 |
| 3502 | phr | `vigilant attention` | 1 | 1 | 0 | 2 | 1 | 0 |
| 3502 | phr | `ensign drum+ond` | 2 | 1 | 0 | 1 | 5 | 0 |
| 3502 | phr | `7th (?:of )?february` | 1 | 5 | 0 | 8 | 0 | 2 |
| 3502 | phr | `have not reached me` | 0 | 0 | 0 | 0 | 0 | 0 |
| 3502 | corr | `clinton to (?:general )?haldimand.{0,40}8 may` | 0 | 0 | 0 | 0 | 0 | 0 |
| 3537 | date | `31(?:st)? May,? 1781/May 31(?:st)?,? 1781` | 2 | 0 | 0 | 0 | 0 | 0 |
| 3537 | phr | `german troops` | 5 | 0 | 0 | 37 | 48 | 23 |
| 3537 | phr | `cloathing/clothing &c` | 0 | 1 | 0 | 27 | 1 | 1 |
| 3537 | phr | `early departure` | 0 | 0 | 0 | 0 | 0 | 0 |
| 3537 | corr | `clinton to (?:general )?haldimand.{0,40}31 may` | 0 | 0 | 0 | 0 | 0 | 0 |
| 4216 | date | `10(?:th)? March,? 1782/March 10(?:th)?,? 1782` | 2 | 1 | 0 | 0 | 0 | 0 |
| 4216 | phr | `scarcely to be expected` | 1 | 1 | 0 | 0 | 0 | 0 |
| 4216 | phr | `january mail` | 1 | 1 | 0 | 1 | 0 | 0 |
| 4216 | phr | `powers adequate` | 1 | 1 | 0 | 0 | 0 | 0 |
| 4216 | phr | `accomplishment of the` | 1 | 1 | 0 | 0 | 0 | 0 |
| 4216 | corr | `clinton to (?:general )?haldimand.{0,40}10 march` | 0 | 0 | 0 | 0 | 0 | 0 |

be-api full-text search, all archive.org items, exact phrase (one request each):

| sibling | phrase | items | what the hits are |
|---|---|---|---|
| 3050 | "intention of giving up the forts" | 3 | unrelated: a William Bull biography (snippet read: "Bull had no intention of giving up the forts") and two copies of a textbook; not this letter |
| 3050 | "great defection in the Spanish" | 3 | Brymner 1887 (three scans): the B.147 paraphrase only |
| 3077 | "miscarriage of the Quebec fleet" | 0 | -- |
| 3077 | "blocked up at Rhode Island" | 182 | generic phrase; top eight are histories and periodicals, none a Haldimand print |
| 3537 | "clothing for the German troops" | 69 | generic (20th-century items); not this letter |
| 3537 | "victuallers from Halifax to Quebec" | 3 | Brymner 1887 (three scans): the B.147 paraphrase only |
| 3502 (control) | "Vermont deserves our vigilant attention" | 13 | VHS II (three scans), Walton II, four editions of Wilbur's Ira Allen, ... -- the control finds the print |
| 4216 (control) | "January mail could contain powers" | 4 | Walton II (four scans); VHS II's copy breaks the phrase across a line ("con- tain"), so it is missed by be-api, found by the djvu grep |

**Findings per sibling** (search results for a verifier, rule 10; none is a novelty verdict):
- **3050**, PRO 30/55/26/2 (Clinton to Haldimand, New York, 2 Oct 1780; Arnold, West Point; reel f.242-244, Image 886, duplicate f.239, decoded f.245): **not located in print** in any of the six volumes. Brymner 1887 B.147 "239 to 244" paraphrases it ("The discovery of the attempt by Arnold to give up the forts, &c., at West Point ... Great defection in the Spanish colonies. 245"). The 2 Oct 1780 date hits in VHS II and the 1920 vol. III are other documents (22 Oct 1780; 12 and 24 Oct 1780). Cipher on the reel: yes (Tomokiyo's cell extract, Image 886; seq_to_iiif.tsv row 886 present), decipherment f.245 on the reel.
- **3077**, PRO 30/55/26/30 (Clinton to Haldimand, New York, 18 Oct 1780, No. 24; Quebec fleet; reel f.247, Image 891, decoded p.246): **not located in print**. Brymner 1887 B.147 p.246 paraphrases it ("The greater part of the Quebec fleet has, he hears, been taken ... reason to believe in a speedy accommodation with Spain. 246 The letter in cypher follows"). The Walton II date hit is the Vermont Assembly's journal for 18 Oct 1780. Cipher on the reel: yes (Image 891), decipherment p.246 on the reel.
- **3502**, PRO 30/55/29/83 (8 May 1781; "seven pages of coding plus two separate letters"): **in print, both letters**. (a) The cipher letter (Tomokiyo f.299, Image 945, decoded p.308, "Vermont deserves our vigilant attention") is printed in VHS II (1871) pp.119-120ff ("H. -- Beverly Robinson to Gen. Haldimand. New York, May 8th, 1781"), and in Walton vol. II (1874) pp.416-417. VHS's editor attributes it to Beverly Robinson by inference ("The name of the writer is not given in the Haldimand Papers ... written by the order, if not in the name, of Sir Henry Clinton"); Discovery and Tomokiyo give Clinton. That attribution difference is for the verifier. (b) The second letter (Tomokiyo f.304, decoded p.307, "... Ensign Drummond of 15th Novr have not reached me") is printed in VHS II p.337 ("[Bev. Robinson] to Gen. Haldimand. New York, May 8, 1781. Sir: -- I received yours of the 7th of February, but the letters you mention to have sent me by ensign Drummond of the [15th? djvu OCR "loth"] of November has not reached me ..."), in the volume's section of letters "which have no reference to Vermont". Brymner 1887 B.147 "299 to 305" paraphrases both. Cipher on the reel: yes (Image 945 and f.304).
- **3537**, PRO 30/55/30/26 (Clinton to Haldimand, New York, 31 May 1781; reel f.311, Image 958, decoded f.313): **in print, cipher and translation**. VHS II prints the letter as its cipher specimen (pp.338-341, "Sir Henry Clinton to General Haldimand. New York, May 31, 1781", figure-pair groups interleaved with the clear words; the djvu OCR of the figures is garbled and was not used) followed by "TRANSLATION OF THE FOREGOING CYPHER" (pp.341-342: "Your letters of the 28th February and 1st of March, was received the 9th instant. Having wrote you fully on the 8th, I have now only to add that the clothing, camp equipage, &c., for the German troops in Canada ... The French fleet and troops are still at Rhode Island, and ours watching them. H. C."). The VHS front matter says "several in cypher, [one of them being inserted as a specimen,] of which translations are given in this volume". Brymner 1887 B.147 p.311 paraphrases it. Walton II and III: no hit (not a Vermont letter). Cipher on the reel: yes (Image 958).
- **4216**, PRO 30/55/36/85 (Clinton to Haldimand, New York, 10 March 1782; reel f.18A, Image 1090, decoded pp.19-20): **in print**: VHS II pp.253-254 ("Sir Henry Clinton to General Haldimand. New York, March 10th, 1782. It was scarcely to be expected that the January mail could contain powers adequate to the accomplishment of the wishes of the people of Vermont ...") and Walton vol. II pp.462-463 (same text; Walton's index "Clinton to Haldimand ... March 10, 1782"). The opening equals Tomokiyo's decoded extract word for word. Brymner 1887 B.148 p.16 paraphrases it. Cipher on the reel: yes (Image 1090).

So three of the five are text-known from 1871 (3502 both letters, 3537, 4216), and 3537's cipher itself is printed beside its translation. 3050 and 3077 are known only through Brymner's paraphrase, in these six volumes; their decipherments f.245 and p.246 are on H-1649, about Images 889-890 by Tomokiyo's positions (886 = f.242, 891 = f.247), so one adjacent pair of frames serves both. Not searched this step: Davies, Documents of the American Revolution (Colonial Office series; these are Haldimand Papers, BL, so unlikely), Clinton's own printed papers (none located), Google Books.

Grades (rule 4): none claimed; no reading produced. Vision calls: 0. Requests: archive.org 16 (1 advancedsearch, 6 djvu texts, 9 be-api fts), 1.6 s apart. A search result, not a novelty verdict (rule 10). Status unchanged: partial.

## GAPS12-pro3055-clinton-1779 (2 Oct 2026, account-4): 3050 and 3077 read from their period decipherments (B.147 pp.245 and 246); the p.242 and p.247 cipher cells match them on the 1778 key

Verdict step of the gaps section (GAPS11's: "the one pilot left for text, 3050 (2 Oct 1780) and 3077 (18 Oct 1780) ... confirm by frame label that Images ~889-890 are f.245 and p.246, then two passes + reconciliation"), run 22:57-23:1x UTC 2 Oct 2026 (clock read). Intake gate exit 0 before the step.

**Print check first (premise).** Two be-api full-text phrase queries on archive.org in Brymner's own paraphrase wording, beside GAPS11's: "the Quebec fleet has" 10 items -- the 1887 Report on Canadian Archives (`reportoncanadian1887publuoft`, `ldpd_11899132_000`: "The greater part of the Quebec fleet has, he hears, been taken", the B.147 p.246 paraphrase), three copies of a different calendar entry ("the greater part of the Quebec fleet has sailed": `reportoncanadia01halgoog`, `cihm_57154`, `reportoncanadian189397publuoft`, `report14canagoog`), and four unrelated (a fisheries report, the Canadian Encyclopedia twice, a gas journal); "defection in the Spanish colonies" 3 items, all copies of the 1887 Report (`cihm_57145`, `ldpd_11899132_000`, `reportoncanadian1887publuoft`). Two broader probes, "accommodation with Spain" (1,204 items) and "attempt by Arnold" (111), are generic; their top eight identifiers are unrelated works (not read further). So neither letter's text was located in print by these queries, beyond Brymner's paraphrase (a search result, rule 10).

**The frames** (H-1649, fetched once at 1600 px, browser UA + viewer Referer, 1.6 s apart; manifest lines in images/h1649/manifest.json, frames not committed, `regen_images.sh` refetches them and re-cuts the crops byte-identically, 73 of 73 tested): Image 886 = B.147 p.242 (fo.206), "N. York October 2d 1780", six columns of figure pairs with a few clear words (column 3 "&c &c at"), "His Excellency General Haldimand", "(turn Over)"; the left margin cross-refers to the copies on p.239 and the decoded copy on p.245 (read at layout size, wording approximate). Image 887 = p.243 (fo.206v), cipher continued. Image 888 = p.244 (fo.207), end of the cipher, "H C", and an endorsement (layout look only, not transcribed). Image 889 = **p.245** (fo.208): "Duplicate New York Octr 2d 80", the decipherment in clear, "H C / Dup. Copy", endorsement "From 1780 Sir Henry Clinton being the Explanation of his Letter in Cypher of the 2d October". Image 890 = **p.246** (fo.209): "New York 18 Octr 80", the decipherment in clear with P.S., "Copy", "[Endorsed]". Image 891 = p.247 (fo.210): "New York 18th October 1780", the opening in clear ("The 10th Instant I was honored with your Excellency's Letter of the 8th Ultimo, and a Subsequent one without date. I am concerned"), then eight columns of figure pairs with clear runs between them (column 2: "as I hear. Monsr Ternay's Fleet ... with his Company here"); margin "See a de-coded copy transcribed on p.246 supra" (layout size). So Tomokiyo's placements hold (f.242 Image 886, decoded f.245; f.247 Image 891, decoded p.246).

**Readings** (`passes/p245_reading.txt`, `passes/p246_reading.txt`, from `passes/p245_246_reconciled.tsv`):
- 3050, 2 Oct 1780: "General Arnold discovered an Intention of giving up the Forts &c &c at West Point, was obliged to fly, and has joined us, which has thrown the Rebels Army into the Greatest Confusion. Admiral Rodney is on this coast with a Superior Fleet, & there is little Probability of a second division of french ships this year. The Good News I sent Your Excellency in my Last, is true. Ld Cornwallis has gained a Compleat Victory over General Gates on the 16th of August at Camden - there is a great defection in the spanish Colonies. - H C"
- 3077, 18 Oct 1780: "The 10th Instant I was honored with Your Excellency's Letter of the 8th ultimo, and a Subsequent one without date. - I am concerned for the miscarriage of the Quebec Fleet, the greatest part of which has been taken as I hear. - Monsieur Ternay's Fleet and the French Army remain blocked up at Rhode Island, and Sir George Rodney still favors us with his Company here - Which has induced the Rebels to lay aside their Attempt on this Place, at least for the present - the English Fleet with Recruits and Stores is arrived, but the Cork Fleet which is much wanted has not yet made its appearance. - an Expedition of near 3000 Men sailed from hence two days ago, for the chesapeak under General Leslie, to favor the Operations of Lord Cornwallis, who by this Time is probably acting in North Carolina. - There is the greatest Reason to believe an Accommodation with Spain will speedily take Place. H C" + "P.S. The Bearer has been paid Ten Guineas by me - /"

**Passes.** 68 line crops (32 on p.245, 36 on p.246) cut by `tools/iiif_lines.py --image <1600 px frame> --region 530,110,640,880|960 --ink 120 --top-margin 8 --bottom-margin 8` (p.246 with `--centres` by eye: the profile missed its last eight lines), and five cipher-column crops (p.242 columns 1-3, p.247 columns 1-2, `--region` per column). Two blind Sonnet passes: 52/68 line crops identical in words between the two blind passes (most differences are margin notes one pass read into the line); by words 310 of 324 pass-A words equal in order (difflib), most of the rest margin text. The differences are margin notes one pass read into the line ("installed", "cypher.", "expect", "upa."), "disowned"/"discovered", "Forts as we"/"Fort as we" for "Forts &c &c", "oblig^d"/"obliged", "at"/"of least", and the endorsement-line fragments; settled by the worker on one montage of the disputed crops (vision call 3). Cipher cells: both passes dropped some repeated "-N" cells (p.247 col.1 "-1" after 5-2, "-7" after 1-6, the second "-18"; p.242 col.1 "-5" in "general"); the montage (the five columns at 3x) settles them; 98 of the 125 reconciled cells were read identically by both blind passes, so the rest rest on the worker's reading, made with the key and the decipherment in mind (stated, not hidden). The 1600 px frames sufficed (cells and text legible), so no full-size frames were fetched.

**Grades (rule 4).** 3050: 106 body words (with date, "Sir", "H C / Dup. Copy"), H 106, M 0. 3077: 175 body words with the P.S., H 175, M 0. Key cells: C 118.

**Key check, cipher cells against the decipherments** (`passes/check_3050_3077.py`, output `check_3050_3077.json`, `--check` exit 0). Cells: p.242 columns 1-3 and p.247 columns 1-2, aligned word for word by the copyist's underlines and clear words (alignment fixed before any lookup), each cell looked up on the 1778 title page as in `check_2380.py`:

| statistic | target | shuffled-plaintext control, 1000 seeds |
|---|---|---|
| page letter = decipherment letter, 3050 (general arnold discovered an intention of giving up the / west point was obliged) | 66/66 | |
| page letter = decipherment letter, 3077 (for / miscarriage of the quebec fleet / part / of which has been taken) | 52/52 | |
| both | 118 / 118 | mean 7.95, p95 13, max 19 |
| distinct cells also in `key_2894.tsv` (July 1780) | 34 of 76, agreeing 34 / 34 | |

Left out of the comparison and listed in the JSON: "forts", 4 cells reading f-r-t-s (the encipherer dropped the o); the q of "quebec", cell 8-8, beyond the end of title line 8 ("OF THE"), which has no q (the page has none to give); and one cipher word with no counterpart in the decipherment, 9-9 9-10 = "in", between "discovered" and "an" at the foot of p.242 column 1 (the decipherer left it out, or the encipherer wrote it in error). "miscarriage" is enciphered with both r's (11 cells), unlike 2380's collapsed doubles. Unlike 2380 (GAPS9) the line-1 cells here (1-1, 1-3 to 1-8, 1-12) fit the printed line 1 (BY PERMISSION ... HONOURABLE), as in 2894. The control changes the plaintext side of every comparison, so it can fail where the target passes (rule 3). Limit: p.242 columns 4-6, pp.243-244 and p.247 columns 3-8 are not transcribed; the cell check covers the opening of each letter only.

Not searched this step: Google Books, the Clinton Papers calendars beyond the HMC Report, Davies. Text status: not located in print by the queries above and GAPS11's six-volume grep (a search result, not a novelty verdict; rule 10; a verifier is wanted, ROOM line posted).

Vision calls: 3 (2 blind Sonnet passes + 1 reconciliation montage looked at by the worker), plus layout looks by the worker at a six-frame overview, three trial crops and two `--debug` overlays. Requests: image-uab.canadiana.ca 6 (Images 886-891 at 1600 px, to the scratchpad); archive.org 5 (be-api fts: "accommodation with Spain", "the Quebec fleet has" twice, "attempt by Arnold", "defection in the Spanish colonies"). Folder 29,902,771 bytes (du -sb) after the 73 crops; the frames are not committed. Status unchanged: partial.


## Remaining gaps (finish-or-blocker pass, 1 Oct 2026)
[Superseded 6 Oct 2026 by "Remaining gaps (R15-CLINGAP refresh, 6 Oct 2026)" at the end of this file; kept as the record of each gap's history.]
Read so far: 6 of 12 named items text known: 5 at grade C (3689, 3753, 3784, 3803, 3813, all from Stevens 1888 vol.2 page images; NOTES AX-STEV, AX-STEV2 "Status") and 2894 at grade H (119 tokens, H 116 M 3, the period decipherment on H-1649 page 186, GAPS 2 Oct 2026). 6009 and 6012 are clear covering notes printed in full (HMC vol.3 p.187, AX-HMC), so 5 of the 10 cipher documents proper are read. The token fraction is unmeasured: no ciphertext of any item is on disk in this folder. The only cipher tokens on disk are Tomokiyo's short opening extracts (figure pair + letter) for 2380, 2894, 3868 and 3853 in sources/cryptiana/web/haldimand.htm (cached 26 Sept 2026). The Kew items are not digitised (Discovery C16266110 digitised=false, 1 Oct 2026).
- 2894, PRO 30/55/24/76 (Clinton to Haldimand, 6 July 1780; the Kew copy is cipher only) - blocker: not-attempted; RESULT 2 Oct 2026 (GAPS): the period decipherment on H-1649 page 186 (= fo.161) is read, 119 tokens H 116 M 3 (passes/p186_reading.txt, build_p186.py --check exit 0), and matches HMC's paraphrase; RESULT 2 Oct 2026 (GAPS2): the cipher is transcribed (315 figure pairs, two passes agreeing 0.931, passes/cipher_reconciled.tsv) and checked against the key: 166 cells recovered, consistency 0.971 vs shuffled plaintext 0.459, Tomokiyo cells 79/81 exact vs shuffled key mean 5.85 (check_2894.json); grades H 264 C 18 M 33; the cipher carries a clause f.186 skips (Admiral A will be reinforced by proportion, read at C/H/M from the key) and spells Ternay; RESULT 2 Oct 2026 (GAPS3): archive.org listofgeneralfie00grea_0 is the 1761 edition (leaf n4 is the title page, n3 a blank flyleaf); mapped to the 1778 key by the fixed cells it keeps the 1778 wording on 14 of 25 lines (fixed cells 158/161 on those lines vs shuffled-letter controls at 0.06-0.28), and from those lines 23 of the 33 M tokens resolve at grade I: the clause reads Admiral A will be reinforced [in] proportion with the preposition open (21-9/21-10: 'as' on the 1761 Corps line, 'in' on the wording that fits all six of Tomokiyo's line-21 cells), grades now H 264 C 18 I 23 M 10, clause tokens C 18 H 2 I 10 M 2 (passes/clause_2894.tsv, title_1761_check.py --check exit 0); clause ready for a verifier; RESULT 2 Oct 2026 (GAPS4): the 1778 printing itself is on archive.org (listofgeneralfie00grea, Pittsburgh copy; Google Books full view has 1756, 1773 and 1834 only), title page page/n12 fetched and read (1 Sonnet pass + the worker's own, agreeing on all 30 lines); every key line is the same-numbered printed line, fixed cells 286/291 agree (the 5 all logged: 1-37, 13-11, 16-7, 23-25, 25-19; shuffled-character controls 0.03-0.28), the 11 lines the 1761 page left unconfirmed agree 125/126, and all 23 I and 10 M tokens read at H from the page: grades H 297 C 18; the clause reads 'Admiral A will be reinforced in proportion' (21-9/21-10 = 'in': line 21 is 'CORPS and in the ARMY'), clause tokens C 18 H 14 (passes/clause_2894_1778.tsv, title_1778_check.py --check exit 0); next: a verifier for the clause (a parent step, no further key work needed on 2894), ~$3
- 2380, PRO 30/55/19/98 (Clinton to Haldimand, 22 Oct 1779, copy and duplicate both in cipher, 4 + 3 pages) - blocker: not-attempted; HMC vol.2 p.53 prints no content (AX-HMC). Tomokiyo puts it at f.120-122 (Image 758-), decoded from f.134, opening "I was honored with your letter of the 19th July". His extract shows systematic -1 letter-position errors in the encipherment, so any later key check must allow an off-by-one rather than count it as a key failure. HMC's "fo.105" is BL foliation; next: Images ~758-776 (cipher plus decipher), two passes + reconciliation of the decipher pages, about 3 pages, ~$10 RESULT 2 Oct 2026 (GAPS5 premise check): not in print (1920 vol. III, Brymner B.147 covering-letter entry only); Brymner reads p.134 as the abstract of the 9 Sept 1779 letter, Tomokiyo as the decode of this one -- settle on the images first. RESULT 2 Oct 2026 (GAPS9): read -- p.134 is this letter's decipherment (margins cross-refer p.120 and p.134, endorsement "Lettre en Chiffre 1779 du Genl Clinton recue a Quebec par Halifax le 18. Jan[?] 1780"), so the conflict is settled for Tomokiyo; body 241 words H 241 (passes/p134_reading.txt, check_2380.py --check exit 0); not located in print (two be-api phrase queries, 0 items; 1920 vol. III has no 22 Oct 1779 document) [VERIFY-CLINTON-3868-2380: wrong -- printed 1871, VHS Collections vol. II p.192; text known, N0, AUDIT.md]; p.120 cipher columns 1-2 on the 1778 key: 52/93 cells exact (shuffled-plaintext p95 11), 89/93 within +-2 (p95 34), the line-1 cells fit a PERMISION/HONORABLE count 60/63; the cipher reads "favored" where the decipherer wrote "honored"; what stays open is columns 3-7 and pp.121-122 (Images 759-760); next: two passes on those against the read decipherment, ~$5 RESULT 3 Oct 2026 (A2P4-CLINT, 1920 vol. III grep, print1920_siblings.tsv): confirmed not in the 1920 vol. III by date and by B.147 pp.120-122/133-135 (0 hits each); the doc list has nothing between 4 Nov 1779 (doc 130) and 31 Jan 1780 from Clinton; text known from VHS II only. RESULT 6 Oct 2026 (R11-CLIN2380): p.120 columns 3-7 (273 cells) checked against the decipherment on the 1778 key, pre-registered gate met: 224/258 compared cells key-consistent with line 1 as the GAPS9 variant (printed page 174; shuffled-plaintext control mean 18.0, max 32; blind pass alone 219); two systematic patterns found after the score: line 9 counted as if OFICERS (240/258 with it) and doubled letters written as a doubled position figure (6-77 ll, 2-77 rr, 5-22 ff; GAPS9's three excluded cells fit the same rule); one cipher/decipherment conflict by witness (cipher "with us I a[m]", decipherment "with us, disappointed"); the p.120 cipher is checked in all 7 columns; what stays open is pp.121-122 (Images 759-760), which probably carry the cipher's continuation after "had they arrived" (about 150 decipherment words); next: confirm the frames, one blind pass per page on column crops + reconciliation against the read decipherment, ~$4. RESULT 6 Oct 2026 (R11-CLIN2380B): frames confirmed (Image 759 = p.121, fo.105v, 8 columns; Image 760 = p.122, fo.106, 6 columns incl. a P.S., signed, endorsed "22d Oct ... Recd 20th May 1780 by Express via Niagara"); p.121 (445 cells) checked against the decipherment, pre-registered gate met: 406/420 compared cells key-consistent with line 1 as the GAPS9 variant (printed page 324; with line 9 as OFICERS 411; with the doubled-figure rule 415; shuffled-plaintext control mean 29.7, max 45); the cipher runs "would have amounted ... having therefore" and has no "with the 650 Recruits and Artillery from Europe" (conflict by witness, below); what stays open is p.122 (Image 760; crops cut by passes/cut_2380_p121_122.py, not passed); next: one blind pass on the six p.122 column crops + reconciliation against the decipherment from "no alternative left", ~$3. RESULT 6 Oct 2026 (R11-CLIN2380C): p.122 (292 cells, P.S. included) checked, pre-registered gate met: 242/252 compared cells key-consistent under the GAPS9 line-1 variant (printed page 180; with line 9 as OFICERS 247; doubled-figure variant adds nothing, 247; shuffled-plaintext control mean 18.05, max 32); all three cipher pages pp.120-122 are now checked against the decipherment; three more cipher/decipherment differences by witness ("move" vs "movements", "Chesapeak" vs "Chesipeak", word division of "in favor of"); what stays open is the witness check of the four conflicts (Recruits-from-Europe clause, "I a[m]", "move", "Chesapeak") against VHS Collections II (1871) p.192; next: read that page for those four phrases, ~$1.5.
- 3868, PRO 30/55/33/65 (Clinton to Haldimand, 12 Nov 1781, in cipher, 3 pages) - blocker: not-attempted; HMC vol.2 p.348 prints no content, and the decipher citation "Vol.11 No.190" is untraceable (AX-HMC2). Tomokiyo puts it at f.382 (Image 1030), decoded on f.385; his extract decodes only "... of your proclamation and"; next: Images ~1030-1034, two passes + reconciliation of the f.385 decipher, ~$8 RESULT 2 Oct 2026 (GAPS5 premise check): text-known in part -- the postscript is printed verbatim in Military and Naval Forces of Canada vol. III (1920) p.214, doc. (262), B.147 p.386, and Brymner B.147 p.385 paraphrases the body; the body itself is not in print, so the p.385 read stays the step; Davies vol. 20 (Transcripts 1781) unresolved by one fts snippet. RESULT 2 Oct 2026 (GAPS8): read -- the period decipherment B.147 pp.385-386 (Images 1033-1034), 252 words H 248 M 4 (passes/p385_reading.txt, check_3868.py --check exit 0); p.382 cipher columns 1-2 match it on the 1778 key, 44/44 cells vs shuffled-plaintext p95 6; and the body is printed verbatim in Collections of the Vermont Historical Society vol. II (1871) pp.198-199 (214/229 words equal), so 3868 is text-known; what stays open is the cell-by-cell match of cipher columns 3-6 and pp.383-384 (Images 1031-1032); next: two passes on those columns against the read decipherment, ~$5 RESULT 3 Oct 2026 (A2P4-CLINT, 1920 vol. III grep, print1920_siblings.tsv): vol. III prints the postscript only (doc 261, p.214, B.147 p.386); the next doc, 262 (p.214-215, B.147 p.387), is Haldimand to Clinton 14 Nov 1781 No. 8 although the doc list calls it Clinton to Haldimand (endorsement: "Sir H. Clinton 14th Novr. Sent the 15th by Davis"). RESULT 6 Oct 2026 (R10-CLIN3868): p.382 cipher columns 3-6 (116 cells) checked against the decipherment on the 1778 key, pre-registered gate met: 97/100 comparable cells key-consistent (shuffled-plaintext control mean 6.9, max 17; blind pass alone 93/100), the cipher spells "Digby" where the copy-book decipherment writes "Darby" (the VHS print's reading); p.382 is now checked in full (6 of 6 columns); what stays open is pp.383-384 (Images 1031-1032, 13 columns, frames fetched to the scratchpad 6 Oct, not committed); next: one blind pass per page on column crops + reconciliation against the read decipherment, ~$4. RESULT 6 Oct 2026 (R10-CLIN3868B): pp.383-384 (Images 1031-1032, 14 columns, 562 cells) checked against the decipherment on the 1778 key, pre-registered gate met on each page: p.383 305/311 compared cells key-consistent (shuffled-plaintext control mean 21.5, max 36), p.384 221/224 (mean 16.0, max 28), pooled 526/535 (blind pass alone 492/514); the 3868 cipher is now checked in full (pp.382-384); the cipher cells confirm three M words of the decipherment ("to the Kings ... Peace": cells k-i-n-g-s and p-?-a-c-e under the gloss "to the"; "Floquet" f-l-o + q in clear + u-e-t; "Cord" c-o-r-d) and show nine disagreeing cells, eight of them clear on the image, so encipherer slips (section below); nothing stays open on 3868 on the reel.
- 3853 cipher, PRO 30/55/33/47 (Robertson to Haldimand, 31 Oct 1781; HMC: "Auto draft. Vol.11 No.183; in cipher, 182 ... decipher 21807 fo.306") - blocker: not-attempted; correction to the classifier. Brymner's B.147 entry at "381" is not a clear covering letter. It paraphrases the decipherment: Brymner "381" = Tomokiyo f.381 "decoded extract" = HMC's BL "decipher fo.306", and Brymner's "406" = Tomokiyo f.406 = the cipher letter itself. So the content is already partly known (Brymner's paraphrase, plus the two sentences Tomokiyo quotes, "Sir Henry Clinton with about six thousand men went on board a fleat..."). The cipher letter opens in clear ("Dear Sir - Thanks for..."). Kew also holds Robertson's own autograph draft (No.183); next: Images ~1029 and 1056, two passes + reconciliation of the f.381 extract, then apply the period key to the f.406 cipher for any part the extract omits, ~$5 RESULT 2 Oct 2026 (GAPS5 premise check): text-known -- the f.381 decipherment is printed verbatim in Military and Naval Forces of Canada vol. III (1920) p.214, doc. (261), "Series B, Vol. 147, p. 381"; not read further. Only the question whether the f.406 cipher carries more than the extract remains, a low-value step. RESULT 3 Oct 2026 (A2P4-CLINT, 1920 vol. III grep, print1920_siblings.tsv): confirmed: doc 260 (OCR "<260)"), p.214, B.147 p.381, prints the f.381 decipherment verbatim, "Sir Henry Clinton with about six thousand men..." to "Ever Yours James Robertson. Octr. 31/81. Rec'd 14th May 82"; the f.406 cipher is not printed.
- Cipher enclosure of 4833, PRO 30/55/42/120 (Haldimand to Carleton, 23 June 1782, enclosing "a duplicate letter in cypher which he dispatched yesterday, overland", i.e. about 22 June 1782) - blocker: not-attempted; the 22 June letter is unidentified. Tomokiyo's Add MS 21808 list has no 22 June entry. His f.65A (Image 1142), Carleton to Haldimand, 3 Aug 1782, decoded on f.66-67, acknowledges "your excellency's letter of the 22[n]d June". The print/Discovery discrepancy is still open (AX-HMC, AX-HMC2: phrase searches only, never a date search). From 1782 the letters also use the word-code elements, some of which Tomokiyo left blank; next: page H-1649 Images ~1100-1145 (Tomokiyo f.31A-f.65A) for Haldimand's 22/23 June 1782 drafts and read the f.66-67 decipher, then grep the on-disk HMC vols 2-3 and Brymner djvu text for "June 22"/"22 June" 1782, ~$5 RESULT 2 Oct 2026 (GAPS5 premise check): the discrepancy is resolved -- Brymner B.148 (1887 Report) calendars the 23 June covering letter in the words Discovery uses ("duplicate of letter already sent in cypher ... engagements of the Cedars ... people of Vermont") and the 22 June cipher letter as Haldimand to Carleton No. 1, 22 June 1782, B.148 p.39 (paraphrase, no verbatim print; 1920 vol. III has no 22/23 June 1782 document); the token-level text is still on the reel only. RESULT 2 Oct 2026 (GAPS10): text-known -- the 22 June 1782 letter (No. 1) is printed in full in Collections of the Vermont Historical Society vol. II (1871) pp.280-282, followed by the 23 June covering letter (= 4833) as No. 2, and reprinted in Walton, Governor and Council vol. II (1874) pp.470-471 (4 interior-phrase be-api fts queries, 4-9 items each, all copies of these two); the reel copy B.148 pp.39-40 (Images 1115-1116) is clear, headed 'In Cypher', so no cipher of this letter is on the reel and no key test is possible from it; the enciphered copy is with Carleton's papers at Kew (PRO 30/55, not digitised) or C.O.5/106 p.361 - blocker now: needs-physical-access, for a key check only (text known). RESULT 3 Oct 2026 (A2P4-CLINT, 1920 vol. III grep, print1920_siblings.tsv): no 22/23 June 1782 document in vol. III (date grep 0 hits; only two B.148 documents printed, 5 Mar and 28 Apr 1782).
- The ciphered note forwarded by 6009/6012, PRO 30/55/53/7 and /10 (26 Oct 1782) - blocker: not-attempted; the note is unidentified. The candidate is Carleton to Haldimand, 26 Oct 1782 (HMC vol.3 p.187: draft PRO Vol.47 No.15, BM Add MS 21705 fos.71/78 and 21806 fo.20), and it is unconfirmed (AX-HMC). Correction to the classifier: H-1649 has only 1266 images, and Tomokiyo's Add MS 21808 list ends at f.123 (Image 1205, 25 Sept 1782). So the late-Oct 1782 leaves of 21808 probably run onto the next reel, not H-1649. Add MS 21807 begins at Image 637, which leaves Images 1-636 unidentified, and whether they hold 21806 is unconfirmed. Tomokiyo's "Vol.II begins at Image 1969" cannot be right on a 1266-image reel; his own f.1 = Image 1070 is the usable anchor; next: read Images 1 and ~600 and the last image of H-1649 for volume labels, find the reel holding late-1782 21808 and 21705 in the 48-reel Canadiana list, and read Carleton 26 Oct 1782 there, ~$4 RESULT 2 Oct 2026 (GAPS5): reel labels read -- Image 1 is a START card, Image 1266 an END OF REEL card, Image 637 the 21807 title leaf (Vol. I, 1777-1783); no 48-reel list needed: B.148 p.123 = Image 1205 and the reel runs to 1266, so pp.111-130 of 21808 (the Oct 1782 entries, Brymner B.148: a Carleton-to-Haldimand letter dated 26 Oct 1782 at p.117 or p.123, the OCR reflow does not say which) are on H-1649 at about Images 1193-1212; next: fetch Images ~1199 and 1205, two passes + reconciliation, ~$3 RESULT 2 Oct 2026 (GAPS6): identified -- Image 1205 = B.148 p.123, a cipher copy of Carleton to Haldimand 25 Sept 1782 (Tomokiyo f.123; pencil note on the page "For de-coded copy, see p. 102 supra", another copy pp.126-8, also B.146 p.54; clear words match Brymner's p.102 paraphrase 18/21, first-column pairs match Tomokiyo 8/8), calendared by Brymner under 26 Oct 1782 "Copies of letters in cypher. 123" (the reflow resolved by the calendar's own order: p.117 = 16 Oct, Smyth claims); so the ciphered note 6009/6012 forwarded is Carleton's re-sent 25 Sept cipher copies under his 26 Oct covering letter (HMC vol.3 p.187), grade I for the link; content in print as Brymner's paraphrase only, not in the 1920 vol. III; Image 1199 stored unread; next: read the period decipherment at B.148 p.102 = Image 1183 (one frame, crops, two passes + reconciliation; text known in paraphrase, so a C/H transcription, no cryptanalysis), ~$4. RESULT 2 Oct 2026 (GAPS7): p.102 read -- the period decipherment of Carleton to Haldimand, New York, 25 Sept 1782, 34 lines, body H 218 M 0, passes 214/217 words identical (passes/p102_reading.txt, check_p102.py --check exit 0); the p.123 cipher cells on disk (Tomokiyo 23 + GAPS6 9) match it on the 1778 title page 19/19 letter cells (shuffled-plaintext control mean 1.25, p95 3) plus 2/2 word codes, and 10 of its 14 distinct cells are in the 2894 key, agreeing 10/10: same key; text in print as Brymner B.148 p.102 paraphrase only, not in the 1920 vol. III (search result, 2 Oct 2026); the 6009/6012 content is now read at H, its link to the 26 Oct covering letter stays grade I; remaining on this item, optional: a full transcription of the pp.123-124 cipher columns for a whole-copy cell match, ~$6. RESULT 3 Oct 2026 (A2P4-CLINT, 1920 vol. III grep, print1920_siblings.tsv): no 25 Sept 1782 document and no B.148 p.102/123 citation in vol. III; its only 26 Oct 1782 document (doc 282, p.229) is Haldimand to Townshend, Q.20 pp.343-4, not Carleton's letter.
- Completeness of the item list (unnamed Kew copies of Clinton-Haldimand cipher letters) - blocker: not-attempted; RESULT 2 Oct 2026 (GAPS): the date-bounded Discovery queries were run (discovery_clinton_to_haldimand_2026-10-02.tsv) and found six further Kew cipher copies outside the six swept pieces (2962, 3050, 3502, 3537, 4152, 4216) plus two unflagged siblings (3004, 3077), each with its reel decipherment at Tomokiyo's position; none is read yet; next: the f.186-style pilot (two passes + reconciliation of the reel decipherment) on each, cheapest first by page count, about $5 each, ~$30 RESULT 2 Oct 2026 (GAPS5 premise check): three of the eight are printed verbatim in Military and Naval Forces of Canada vol. III (1920) -- 2962 p.168 doc. (190) B.147 p.223; 3004 pp.170-171 doc. (197) B.147 pp.234-5; 4152 pp.217-218 doc. (267) B.48 pp.98-9 -- text-known, no reel read needed for them; 3050, 3077, 3502, 3537 and 4216 not found in print and stay the pilot candidates, ~$5 each, ~$25. RESULT 2 Oct 2026 (GAPS11, print check of the five, 6 djvu greps + 8 be-api fts, table in NOTES GAPS11 and print_check_siblings_2026-10-02.tsv): 3502 in print, both letters (VHS Collections vol. II, 1871, pp.119-120 and p.337, VHS attributing them to Beverly Robinson; the cipher letter also Walton vol. II pp.416-417), cipher on the reel (Image 945, f.304), next: none for text, a verifier only; 3537 in print, cipher specimen and translation (VHS II pp.338-341 and 341-342), cipher on the reel (Image 958), next: none for text, an optional key check from the printed specimen against its translation; 4216 in print (VHS II pp.253-254, Walton II pp.462-463), cipher on the reel (Image 1090), next: none for text, a verifier only; 3050 not located in print (Brymner 1887 B.147 pp.239-245 paraphrase only), cipher on the reel (Image 886, decoded f.245); 3077 not located in print (Brymner B.147 p.246 paraphrase only), cipher on the reel (Image 891, decoded p.246); next for 3050 and 3077: read their decipherments f.245 and p.246 at about Images 889-890 (confirm the frames first), two passes + reconciliation, one pilot for both, ~$6. RESULT 2 Oct 2026 (GAPS12): read -- Images 889 and 890 are B.147 p.245 and p.246 (frame labels and margins confirmed); 3050 body 106 words H, 3077 175 words H (passes/p245_reading.txt, p246_reading.txt; check_3050_3077.py --check exit 0); cipher cells p.242 cols 1-3 and p.247 cols 1-2 on the 1778 key: 118/118 equal to the decipherment letters vs shuffled-plaintext p95 13; not located in print by two more be-api phrase queries in Brymner's wording (Brymner 1887 paraphrase only); verifier wanted (ROOM). With this, every one of the eight Discovery siblings is text-known or read at H; what stays open for this gap is only the rest of each cipher (p.242 cols 4-6, pp.243-244, p.247 cols 3-8), an optional key check, not text recovery. RESULT 3 Oct 2026 (A2P4-CLINT, 1920 vol. III grep, print1920_siblings.tsv): of the eight siblings vol. III prints 2962 (doc 189 p.168), 3004 (doc 196 pp.170-171) and 4152 (doc 266 pp.217-218) in full, as GAPS5 had them; 3050, 3502, 3537 and 4216 are absent (date and B.147/B.148 page greps 0 hits); for 3077 it prints only its enclosure, La Fayette's proclamation in translation (doc 209, p.184, endorsed "inclosed in Sir H. Clinton's Letter the 18th Octr. 1780"); doc 271 (p.220, B.148 pp.24-9, Haldimand to Clinton 28 Apr 1782, "In Cypher") acknowledges 4216 ("that of the 10th March"). No gap item's text changes status.
- Kew-side physical copies (Clinton's retained copies of 2380, 2894, 3868, 4833; the PRO decipherments "Vol.11 Nos.117/190"; the Am. & W.I. 142 fo.150 and 145 fo.87 copies of 3868 and 4833) - blocker: needs-physical-access; Discovery C16266110 digitised=false (1 Oct 2026), and no image route is known. The recipient copies and period decipherments of the same letters are on H-1649, so this matters only if a token-level check against the Kew copy itself is wanted after the reel reads; next: only then, write REQUEST.md for a TNA copy order (a person step), ~$1

## Escalation (1 Oct 2026)
- [ ] siblings: Kew side done. AX-STEV2 swept all six pieces and found the 12 cipher-flagged items. AX-HMC2 traced old "vol 11" to 14 modern pieces, but Nos.117/190 are untraceable. DECODE had no hit (23/25 Sept). Not yet opened: the recipient-side volumes on LAC reel H-1649 (BL Add MS 21807 from Image 637, 21808 from Image 1070, 1266 images in all; re-checked 1 Oct 2026). They hold the Haldimand copies of 2380, 2894, 3868 and 3853 beside their period decipherments, and Tomokiyo lists about nine more sibling cipher letters of the same pair. Planned: the H-1649 fetches above, starting with 2894 -- done for 2894 on 2 Oct 2026 (route in images/h1649/manifest.json); Image 1205 (B.148 p.123, the 25 Sept 1782 cipher copy) fetched and identified 2 Oct 2026 (GAPS6); the rest follow.
- [ ] clear-pages: Done for the five Cornwallis-Clinton items (Stevens 1888, AX-STEV/AX-STEV2) and for the clear covering letters 4833, 6009 and 6012 (HMC). For 3853, Brymner's "381" entry is a paraphrase of the decipherment itself. Not yet read: the period decipherments themselves (Tomokiyo: f.134- for 2380, f.186 for 2894, f.385 for 3868, f.381 for 3853; f.66-67 for Carleton's 3 Aug 1782 reply), all on H-1649. These are the decipherments themselves, grade H once transcribed; f.186 (2894) transcribed 2 Oct 2026, 119 tokens H 116 M 3.
- [x] known-keys: KEY-OFFICES.tsv and KEY-DESIGN.tsv have no Clinton, Haldimand or Cornwallis row (grep, 1 Oct 2026). Saberton's "Common cipher" (JAR 2019) covers Cornwallis-Clinton 1780-81 and is moot for the five read items. Untried: the Haldimand-Clinton book cipher. Its figure pairs give a line and a letter in the title page of "A List of the General and Field Officers" (1778), per Tomokiyo, haldimand.htm, and LESSONS-TOMOKIYO.md rows 66-67, which were never linked to this target. Its explanation sheet is at Add MS 21807 f.323-326 (Tomokiyo f.402-405, Images 1051-1054), and Tomokiyo gives a 1782 word-code table. Done for 2894 on 2 Oct 2026 (GAPS2) without the title page itself: the 315 pairs of pages 184-185 against the f.186 decipherment recover 166 cells at consistency 0.971 (shuffled plaintext 0.459) and agree with Tomokiyo's independent cells 79/81 (shuffled key mean 5.85); the key is the title page as described, with omitted repeated first figures and a doubled letter dropped. The only title page on archive.org is the 1761 printing (GAPS3, 2 Oct 2026): it confirms the 1778 wording of 14 of the 25 key lines with cells and leaves 11 unconfirmed; the 1778 page itself is gap 1's next step. The 1778 page itself is on archive.org after all (listofgeneralfie00grea, GAPS4, 2 Oct 2026): it confirms all 25 key lines (286/291 fixed cells, the ampersand counted as a character) and reads every open cell of 2894 at H. Add the KEY-OFFICES/KEY-DESIGN rows at close-out.
- [x] print: Searched HMC Report vols 2-3 page images (AX-HMC); Stevens 1888 vols 1-2 (AX-STEV, AX-STEV2), which give the five C items; Brymner, Report on Canadian Archives 1884-89, B.147, phrase searches (AX-HMC2); the Google Books API (GBOOKS); Saberton CP pt.11, identified but NO_PAGES (LOCAL-QUEUE L16) and not needed for the five read items; JSTOR rows 129-130, one with no hit, one a Lafayette Papers chapter waiting on ASKS row 76 that concerns 3813, already read. No printed full text found for the Haldimand-side items; only Tomokiyo's incipits and Brymner's paraphrase of 3853's decipher. A date-keyed grep for 4833 is folded into its gap. Done 2 Oct 2026 (GAPS10): Collections of the Vermont Historical Society vol. II (1871) prints both the 22 June 1782 cipher letter (pp.280-282) and 4833 (from p.282), Walton vol. II (1874) pp.470-471 reprints the former; four interior-phrase be-api fts queries found only copies of these two.
- [n/a] key-rebuild: No key is being extended. The 1779-81 items use a known period book key and have period decipherments in the same volume, and no ciphertext is on disk. Revisit only if the June 1782 (4833) or Oct 1782 (6009/6012) cipher uses the 1782 word-code entries Tomokiyo left blank.
- [x] image-check: All five read items were checked on Stevens 1888 page images; this corrected the OCR misread of 3689's "Original was written in Cypher" endorsement (AX-STEV). The other seven entries were checked on HMC vol.2-3 page images (AX-HMC). AX-HMC2 suspected Brymner's "406" was an OCR misread of "306"; it is not. Brymner's numbers match Tomokiyo's reel-volume foliation (406 = Robertson cipher, 381 = its decoded extract, 184 = Clinton 6 July 1780), while HMC's fo.306 is BL foliation. This should be confirmed on the H-1649 images during the reads.
- [x] retry: Until 2 Oct 2026 no ciphertext was on disk; 2894's cipher (pages 184-185) now is, beside its decipherment, and the verification pass named in the 02:55 Verdict ran the same day (GAPS2: key applied to the 315 figure pairs, compared with the f.186 text, numbers in gap 1). The other seven reel decipherments are still unread (gap 7).
Verdict: keep going: 7 internal gaps (3 Oct 2026, A2P4-CLINT: the 1920 vol. III date and B-citation grep found no further printed text of any gap item, print1920_siblings.tsv), none blocked from outside except the Kew-side copies; 2894, 3868 and 2380 are N0 (AUDIT.md, VERIFY-CLINTON), 3853, 2962, 3004 and 4152 are text-known from the 1920 vol. III (GAPS5), the 26 Oct 1782 note is read (GAPS6/GAPS7), 4833 and its enclosure are text-known from VHS Collections II (GAPS10, key test needs the Kew cipher, needs-physical-access), 3502, 3537 and 4216 are text-known from VHS Collections II (GAPS11), and 3050 and 3077 are read from their period decipherments at H with their opening cipher cells matching on the 1778 key (GAPS12, 2 Oct 2026; not located in print by the searches run, verifier wanted); no text recovery is left on H-1649 for the named items; the 3868 cipher is checked cell by cell in full (p.382 R10-CLIN3868, pp.383-384 R10-CLIN3868B, 6 Oct 2026: 667/679 comparable cells key-consistent); the 2380 cipher p.120 is checked in all 7 columns (GAPS9 + R11-CLIN2380, 6 Oct 2026: columns 3-7 224/258 compared cells key-consistent); 2380 p.121 checked too (R11-CLIN2380B, 6 Oct 2026: 406/420 compared cells, control max 45); cheapest next: 2380 p.122 (Image 760, the last cipher page with the P.S.) against its read decipherment, one blind pass + reconciliation, ~$3 (a key-consistency check on a text-known item, low value; it may also show whether the P.S. carries the "650 Recruits" clause the p.121 cipher lacks), and a verifier for the three decipherment M words the 3868 cipher settles (ROOM flag, 6 Oct 2026).

## Web and blog check (GAPS-pro3055-clinton-1779, 2 Oct 2026)

Run first because `tools/intake_gate_check.py` exited 1 on the missing check alone (check-solved.md "Required step", 28 Sept 2026). Clock read 02:44 UTC, 2 Oct 2026. Searches are WebSearch (plain web) unless marked; blog hits opened with WebFetch and their comment threads read.

(a) Plain web searches, four:
1. `Clinton Haldimand 6 July 1780 letter cipher deciphered` -- hits: Saberton's JAR 2019 article (already on file, LANE CX2), Wikipedia "Haldimand Affair", the Clements Library "Spy letters" exhibit pages (Arnold-Andre book ciphers), an NSA Friedman lecture PDF. None names the 6 July 1780 letter or any Clinton-Haldimand decipherment.
2. `"PRO 30/55" Clinton Haldimand cypher 2894` -- hits: real-estate noise, a PSU catalogue record of Germain-Haldimand letters (1781), the Clements Clinton finding aid, TNA beta catalogue C16309398 (PRO 30/55/28/57, Haldimand to Clinton 28 Feb 1781, "does not appear to have survived"). No decipherment or plaintext of 2894.
3. `"I have received your dispatches" Clinton Haldimand 1780 cipher` (the decipherment's own opening, from Tomokiyo's incipit) -- hits: founders.archives.gov Washington Papers (Tallmadge, 1780), TNA beta C16309408. No hit quotes this letter.
4. `Haldimand Clinton book cipher "List of the General and Field Officers" 1778 solved` -- hits: Leighton & Matyas, "The History of Book Ciphers" (CRYPTO 1984, LNCS 196, Springer; dl.acm.org / link.springer.com, the source Tomokiyo cites at haldimand.htm l.421), whose abstract/snippet says the Haldimand-Clinton book cipher's key is the 1778 Army List and that "Barbara Harris of New York solved the simple numerical substitution"; the Cryptiana blog root; vermonthistory.org SmithAndHaldimand1.pdf; Clements Clinton subject index; Wikipedia "Haldimand Affair", "Arnold Cipher". The Leighton-Matyas hit concerns the cipher *system* (key book identified, system solved), not a printed decipherment of item 2894; its text was not opened (ACM/Springer paywalls; LESSONS-TOMOKIYO.md rows 66-67 already carry the same fact from Tomokiyo).
   Model-solve announcements (check-solved.md): `Haldimand Clinton cipher solved Claude OR GPT OR ChatGPT` -- hits are Kryptos K4, Enigma and a 370-year-old petition cipher stories; none mentions Haldimand or Clinton.

(b) Blog site searches, three (WebSearch restricted to the domain):
- Cipherbrain (scienceblogs.de/klausis-krypto-kolumne): `Haldimand Clinton cipher` -- 0 posts about Haldimand, Clinton or this correspondence across five result pages (Confederate, Madison, Bunch, WW1/WW2 items only).
- Cryptiana blog (cryptiana.blogspot.com) and Tomokiyo's pages: the on-disk snapshot `sources/cryptiana/web/haldimand.htm` (cached 26 Sept 2026, 0 requests) is Tomokiyo's own article on this cipher and lists the reel positions used below; the blog search `cryptiana.blogspot.com/search?q=Haldimand` returns one post, "A British Book Cipher during the American Revolutionary War" (27 Apr 2026, cryptiana.blogspot.com/2026/04/a-british-book-cipher-during-american.html), opened: it announces the haldimand.htm article and adds that the book cipher was also used in letters from Lord Germain; **0 comments** in its thread; no decipherment or plaintext of any letter in the post.
- Cipher Mysteries (ciphermysteries.com): `Haldimand Clinton cipher` -- 0 posts about it across three result pages (Zodiac, Beale, Ohio, Gentlemen's cipher only).

(c) Comment threads opened: Saberton, JAR 6 June 2019 (allthingsliberty.com/2019/06/decoding-british-ciphers-used-in-the-south-1780-81/): 3 comments (Daigler 6 June 2019, Saberton 10 June 2019, "Sophia" 23 Apr 2024), none mentions Haldimand, Quebec or any Clinton-Haldimand letter. Cryptiana 27 Apr 2026 post: 0 comments. vermonthistory.org SmithAndHaldimand1.pdf (Vermont History, the Haldimand negotiations) opened and text-extracted (5,376 words, 24 mentions of Clinton): no cipher text and no quotation of the 6 July 1780 letter; its one 1780 citation is a William Smith letter of 10 Nov 1780.

Result: no decipherment or plaintext of item 2894 (or of any other Clinton-Haldimand cipher letter named in this folder) located by these queries on 2 Oct 2026; the only text of 2894 located anywhere is the period decipherment on the reel itself (below). A search result, not a novelty verdict (rule 10). Requests: WebSearch 8, cryptiana.blogspot.com 2, allthingsliberty.com 1, vermonthistory.org 1. [Corrected by VERIFY-CLINTON-2894, 2 Oct 2026, AUDIT.md: N0. The f.186 text is printed verbatim in Hist. Section, General Staff (Canada), Military and Naval Forces of Canada vol. III (1920), Illustrative Document 170, p.158; the clause is in TNA Discovery's own description of PRO 30/55/24/76 ("Admiral Arbuthnot will be reinforced in proportion") and in McLean to Haldimand, 24 July 1780, Doc. 181, p.165.]

## VERIFY-CLINTON-2894 corrections (2 Oct 2026)

Verifier audit in AUDIT.md: item 2894 N0, key source period, text known; the clause N0 (floor N1). Over-claims corrected in place above (bracketed): "not located in ... any print" for the clause, and "the only text of 2894 located anywhere". The decipherment is printed (1920, Doc. 170, p.158, from B.147 p.183), the clause is in TNA Discovery C16304855 and McLean's printed letter (Doc. 181, p.165). Re-derivation: all four `passes/*.py --check` exit 0 in a fresh session. Witness variants vs the 1920 print: Ministers/Minister, Terney/Ternay, stil/still, Rivers/River, Laurence/Lawrence (AUDIT.md section 4).
Suggestion (Usage 7; run 3 Oct 2026 by A2P4-CLINT, see "1920 vol. III sibling grep" below): the same 1920 vol. III prints Haldimand Papers documents chronologically with B-series citations; grep its djvu text (archive.org `vol1t3historyoforganiz01quebuoft`) for the sibling dates of gaps 2-7 (22 Oct 1779, 14 Aug, 9 Sept, 2 and 18 Oct 1780, 8 and 31 May, 31 Oct, 12 Nov 1781, 1782) before any further reel transcription; disk-only, ~$1.

## VERIFY-CLINTON-3868-2380 corrections (2 Oct 2026)

Verifier session (account 4), separate from GAPS8/GAPS9. Classes in AUDIT.md: **3868 N0** (key period, text known: VHS
Collections vol. II, 1871, pp.198-199; Brymner 1888 calendars p.385 as "Explanation"); **2380 N0** (key period, text
known: VHS Collections vol. II, 1871, p.192, run on under a 27 Oct 1781 "Intelligence" heading; Brymner 1888 calendars
p.134 as the explanation of a cipher letter abridging the 9 Sept 1779 letter, which Davies, DAR vol. 17 p.204 prints in a
longer clear form). Corrected here: GAPS9's "not located in print" (three places, bracketed) and its "not an abstract of
the 9 Sept 1779 letter" (both readings hold). The 1871 print reads "favored", supporting GAPS9's cell finding against the
decipherer's "honored". What stays open is unchanged (cipher columns 3-7 / 3-6 and the duplicate pages), now as
key-check work on text-known items, not text recovery.

## VERIFY-CLINTON-3050-3077 corrections (2 Oct 2026)

Verifier (account 4, separate from GAPS11/GAPS12), AUDIT.md "items 3050 and 3077". Both **N0, key `period`, text not in
print** (the period decipherments on B.147 pp.245-246 are prior decipherments of these very items; precedent
szembek-bk1560). Rule 7: `passes/check_3050_3077.py --check` OK, exit 0 in the verifier's session. No sentence of GAPS11
or GAPS12 over-claims ("not located in print ... a search result" stands). Sources added to the print check, none
printing either letter: HMC American MSS vol. II (1906) p.188 (3050) and p.192 (3077), location-only entries naming clear
copies sent to Germain (PRO Am. & W. I. 138, fo.657 for 3077); Davies, DAR vol. 16 (Calendar 1780) lists 3077 as
enclosure ix of No. 2596 (page not read, lending-only), vol. 18 prints neither; Michigan Pioneer and Historical
Collections vols X, XIX, XX and both indexes: no hit; 21 further be-api interior-phrase queries and 8 Google Books
queries: only Brymner 1888. Not read: HathiTrust full text (unreachable), the DAR vol. 16 page. JSTOR rows queued.

## 1920 vol. III sibling grep (A2P4-CLINT, 3 Oct 2026)

Source: archive.org `vol1t3historyoforganiz01quebuoft` (advancedsearch: title "A history of the organization, development and services of the military and naval forces of Canada...", volume field "1"; the scan binds vols I-III, vol. III title leaf at djvu line 39766, "VOLUME III. The War of the American Revolution ... 1778-1784"), `_djvu.txt` fetched once, 3,289,074 bytes, sha1 2974958a09e1411af4e09182ac38fcf2f28082ae, scratchpad only. Requests: archive.org 2.
Method: script only, no vision. The vol. III document list (calendar entries "N. date. summary, p. X") and the document bodies (headers "(N)" followed by "Series B, Vol. ..., p. ...") were parsed; each sibling date was grepped in both, with day-month and month-day forms, and each B-citation page range named in the gaps (B.147 pp.120-122, 133-135, 239-247, 293-319, 381, 405-407; any B.148) was grepped in the bodies.
Positive control: 2894's decipherment found as doc 170, p.158, B.147 p.183 ("I have received your dispatches of Novr & January..."), matching AUDIT.md.
Result (table: print1920_siblings.tsv): printed in full, already on file from GAPS5: 2962 (doc 189 p.168, B.147 p.223), 3004 (doc 196 pp.170-171, B.147 pp.234-5), 3853's f.381 decipherment (doc 260 p.214, B.147 p.381), 4152 (doc 266 pp.217-218, B.48 pp.98-9); printed in part: 3868, postscript only (doc 261 p.214, B.147 p.386), and 3077, its enclosure only (doc 209 p.184, La Fayette's proclamation in translation); not printed in vol. III: 2380, 3050, 3502, 3537, 4216, the 22 June 1782 cipher letter and 4833, Carleton's 25 Sept 1782 cipher and its 26 Oct 1782 cover. The doc list mislabels doc 262 (B.147 p.387, 14 Nov 1781) as Clinton to Haldimand; its endorsement shows it is Haldimand's No. 8 to Clinton. These are search results in one edition, for the verifier; no reading of ours changes and no gap's status changes.

## R10-CLIN3868 (6 Oct 2026, account 2, LANE RUN10): 3868 cipher p.382 columns 3-6 checked against the decipherment on the 1778 key

Run 07:39-07:48 UTC 6 Oct 2026 (clock read). Step: gap 3's named next, p.382 first (brief R10-CLIN3868). Pre-registered in
`PREREG_R10-CLIN3868.md` (pushed d6e02ac03 before the scored run). Script `passes/check_3868_c36.py` (output
`passes/check_3868_c36.json`, `--check` exit 0; `check_3868.py --check` still exit 0, the reading is unchanged).

**Images.** H-1649 Images 1030, 1031, 1032 at full/max (5448x4056, 5440x4056, 5440x4056) fetched to the scratchpad only
(the folder is at 29.95 MB, so no image is committed; `regen_images.sh`'s route re-fetches them). Crops: PIL boxes on Image
1030 (full/max coordinates) c3 2350,1290,2640,3220; c4 2600,1290,2935,3220; c5 2905,1290,3170,3220; c6 3120,1290,3480,3220
(`tools/iiif_lines.py --image ... --region ... ` was run first and cut 100 px horizontal bands with no line centres found in a
figure column, so the columns were cut by box as GAPS8 did; command and boxes in this paragraph).

**Pass and reconciliation.** One blind Sonnet pass on the four column crops (`passes/p382_c36_passA.tsv`, 116 cells, 4 glosses
"they shall", "and also", "with", "You will not expect more from me by this Conveyance", rules marked). The worker re-read the
cells that failed the key on zoomed crops and changed 5 (`passes/p382_c36_reconciled.tsv`, note column): c4.3 -24 -> -27
(a loose 27), c4.7 -14 -> -17 (image ambiguous 14/17), and c6.20-22 "-15, 1-4, -3" -> "-5, -4, 1-3" (a lone 4 set above the
pair 1-3). The copyist's rules mark word ends, except "respecting", which carries two extra rules.

| statistic (pre-registered gate: share >= 0.80 and count > control max) | blind pass | reconciled |
|---|---|---|
| cells read | 116 | 116 |
| comparable cells (word cell count = letter count) | 100 | 100 |
| page letter = decipherment letter (i = j) | 93 | 97 |
| strict (j counted apart) | 92 | 96 |
| shuffled-plaintext control, 1000 seeds: mean / p95 / max | 6.96 / 11 / 19 | 6.95 / 11 / 17 |
| gate | PASS | PASS |
| distinct cells also in key_2894.tsv | | 33 of 67, agreeing 33/33 |

The words spelled: "of the whole but [they shall] be sent by the next opportunity [and also] laid be(l)ore ad-rl Digby who is
a ioint commisioner [with] me as soon as he arrives in town [You will not ... Conveyance] respecting". Apart from the gate:
"Admiral" is 5 cells (a d i r l: an abbreviation, the third cell 18-10 is i where m would be 18-7), "commissioner" is 11
cells spelling "commisioner" exactly. The three remaining disagreements: "before" 18-18 l for f (18-16; the image clearly
shows 18, an encipherer's slip), and **the name: cells 11-6 4-2 11-9 1-1 16-6 spell "digby"** (d i g b y), where the copy-book
decipherment on p.385 writes "Darby". The printed VHS text (1871) has "Digby", and Rear-Admiral Robert Digby is the joint
commissioner meant; so the cipher agrees with the print and the p.385 "Darby" is the decipherer's or copyist's error. The
reading `passes/p385_reading.txt` stays as written (it transcribes the decipherment); this is a note on its content, flagged
for a verifier in ROOM.

**Grades (rule 4), the 116 cells against the decipherment:** C 108 (97 key-consistent comparable cells + the 11 of
"commisioner"), M 8 (the 5 cells of the abbreviated "Admiral", the l of "before", the i and g of "Digby", which disagree
with the decipherment but agree with the print). With GAPS8's 44/44 on columns 1-2, p.382 is checked in full: 141 of 144
comparable cells key-consistent.

**Not done (stopped before the next unit by the brief's 80% cap rule):** pp.383-384 (Images 1031-1032; p.383 has 7 columns,
p.384 6 columns plus the P.S. figures and the clear "H.C. P.S." and "Cypher L. Initialed"). Frames are known good at full/max.
Requests: image-uab.canadiana.ca 4 (Images 1030, 1031, 1032 at full/max; 1032 answered HTTP 500 once, the one retry after
20 s gave 200). Vision calls: 1 blind Sonnet pass, plus worker looks at 4 quarter-size frames/contact sheets and 3 zoomed crops.
Status unchanged: partial.


## R10-CLINV (6 Oct 2026, account 2, LANE RUN10): verifier of R10-CLIN3868

Verifier verdict in AUDIT.md section "R10-CLINV". PREREG predates the scored output; re-score reproduces (blind 93/100, reconciled
97/100 vs shuffled max 19/17, PASS). Cells 11-6 4-2 11-9 1-1 16-6 eye-checked on Image 1030: they spell DIGBY on the 1778 key (two
cells from different key lines, not a slip from "Darby" = 11-6 11-8 11-7 1-1 16-6). [R10-CLINV correction to R10-CLIN3868's
sentence "the p.385 'Darby' is the decipherer's or copyist's error": this is a rule-4 data conflict -- cipher (sender side) DIGBY,
period decipherment p.385 (recipient side) DARBY, 1871 print Digby -- recorded by witness, not settled.] `passes/p385_reading.txt`
keeps "Darby" (it transcribes the decipherment). No reading change; no SECOND-OPINIONS row to propagate.

## R10-CLIN3868B (6 Oct 2026, account 2, LANE RUN10): 3868 cipher pp.383-384 checked against the decipherment on the 1778 key

Run 07:58-08:08 UTC 6 Oct 2026 (clock read). Step: gap 3's named next after R10-CLIN3868. Pre-registered in
`PREREG_R10-CLIN3868B.md` (pushed 10e0744a4 before the scored run; same statistic, control and gate as PREREG_R10-CLIN3868).
Script `passes/check_3868_p383_384.py` (output `passes/check_3868_p383_384.json`, `--check` exit 0; `check_3868.py --check`
and `check_3868_c36.py --check` still exit 0, the reading file is unchanged).

**Images and crops.** H-1649 Images 1031 and 1032 at full/max (5440x4056 each) fetched to the scratchpad only (folder at the
30 MB line; `regen_images.sh`'s route re-fetches them). `tools/iiif_lines.py --image img1031.jpg --region 1700,580,1800,2950
--out il1031` was run first and found 0 line centres in a figure column (as on p.382), so columns were cut by PIL box,
inverted to dark-on-light: Image 1031 c1-c7 x 1725-2030, 1995-2280, 2250-2510, 2470-2760, 2720-2985, 2935-3185,
3120-3460, y 560-3500; Image 1032 c1 1720-2005 (y 560-3340), c2-c5 1990-2250, 2220-2460, 2440-2670, 2640-2880 (y 560-3200),
c6-c7 (the P.S. columns) 2840-3080, 3060-3330 (y 1700-3100); boxes checked on a 1/5 overlay before the passes.

**Passes and reconciliation.** One blind Sonnet pass per page on the column crops (`passes/p383_passA.tsv`, 339 rows;
`passes/p384_passA.tsv`, 257 rows). The worker re-read every cell that failed the key, and the glosses, on zoomed crops
(`passes/p383_reconciled.tsv`, `passes/p384_reconciled.tsv`, note column per cell): p.383 "leaders" -13 -> -1;
"declaration" -14 -> two cells -1, -4 (the pass merged them); a phantom -1 after "your" (c4.12) and a spilled "and" from
the next column (c6.48) dropped; "will" 4-7 -> 4-1 (7 is out of range on the 4-letter line LIST; the hand's 1 has a
hooked top; M); the gloss "I" (pass -3[?]); "parliament" -4 -16 -9 -> -7 -6 -2; "truth" damaged (14/17, then 4 5 6
tightly written: 6 cells, reported apart); "peace" 15-2, -1 -> a lone -2 then 15-1. p.384 "reason" -16 -> -6;
"transactions" 2-16 -> -1 + 2-6; "practising" 2-16 -> 2-6; "inhabitants" a lone -1 inserted; "Arnold" 3-15 -> 3-1
(the 5 is the next column's); the pass's "a" and "Next" are a q written in clear (the key page has no q) and the gloss
"Mess[rs]".

| statistic (gate: share >= 0.80 and count > control max) | p.383 pass A | p.383 reconciled | p.384 pass A | p.384 reconciled | pooled reconciled |
|---|---|---|---|---|---|
| cells read | 323 | 323 | 237 | 239 | 562 |
| compared cells | 313 | 311 | 201 | 224 | 535 |
| page letter = decipherment letter (i = j) | 295 | 305 | 197 | 221 | 526 |
| strict | 295 | 305 | 196 | 220 | 525 |
| shuffled-plaintext control, 1000 seeds: mean / p95 / max | 22.1 / 30 / 38 | 21.5 / 30 / 36 | 14.2 / 20 / 25 | 16.0 / 23 / 28 | 37.6 / 47 / 58 |
| gate | PASS | PASS | PASS | PASS | PASS |

Distinct cells 128, of which 58 are also in key_2894.tsv, agreeing 58/58 (same key). The copyist's glosses on these pages:
"General", "Confidence", "that", "the", "of the" (x3), "and of", "I apprehend make", "to", "and", "of", "to the" (x3), "and
this", "and I hope you will find no difficulty", "from", "H.C.", "P.S.", "says Monst- du", "q", "Mess", "and", "were".

**The nine disagreeing cells** (`mismatches` in the json): p.383 "measures" 18-4 t for m (18-7; image 4/7 ambiguous),
"declaration" 20-4 d for e (20-3; image 4), "crown" 24-1 24-3 24-2 for c-r-o (positions 1, 3, 2 are c, r, o on line 21
CORPS; the image clearly writes 24: a wrong line number), "peace" -2 on line 1 (y) for e (a clear lone 2); p.384
"preventing" 6-9 n for g (6-1; a clear 9), "result" 18-14 18-15 o-n for e-s (clear). **Apart (cell count differs):**
"promise" 6 cells p-r-o-i-s-e (m omitted), "practising" 9 cells (a omitted), "before" 5 cells b-f-o-r-e (e omitted),
"Arnold" one cell 3-1 a (an initial), "truth" 6 cells on a damaged spot.

**The cipher against the decipherment's M words.** p385_reading.txt marks "{to the Kings[?]} Pyan[?] Peace", "Floquet[?]"
and the initial of "Cord" (pass split Ford/Cox). The cipher has the gloss "to the" then cells k-i-n-g-s and
p-[y]-a-c-e, so the line reads "to the kings peace" (the VHS print's "to the King's Peace"); "Floquet" is f-l-o, q in
clear, u-e-t; "Cord" is 21-1 21-2 21-3 21-8, c-o-r-d. The reading file is a transcription of the decipherment and is
left as written; this is evidence for a verifier on those three words (ROOM flag). AUDIT.md not touched (R10-CLINV
edits it concurrently).

**Grades (rule 4), the 562 cells against the decipherment:** H 526 (key-consistent compared cells, period key and
period decipherment), M 36 (the 9 disagreeing cells and the 27 cells of the five words apart). With p.382 (141/144
comparable cells, GAPS8 + R10-CLIN3868), the 3868 cipher is checked in full: 667/679 comparable cells key-consistent.
Requests: image-uab.canadiana.ca 2 (Images 1031, 1032 at full/max, both 200). Vision calls: 2 blind Sonnet passes (one
per page), the worker's own looks at 2 overlays and 16 zoomed crops. Status unchanged: partial.

## R10-CLINV2 (6 Oct 2026, account 2, LANE RUN10): verifier of R10-CLIN3868B's three words

Verdict in AUDIT.md section "R10-CLINV2". PREREG predates the score (10e0744a4 08:00:46 < 854780ec0 08:08:22 UTC); re-score
reproduces (all three check scripts --check exit 0). Decipherment image (taller crops of Images 1033/1034) read with the cipher
cells as corroboration: "{to the Kings}" and "Floquet" lose their [?] (H); "Pyan[?]" stays M (struck "Pya", which is the cipher's
p-y-a written out literally); "Cord" confirmed. `p385_reading.txt` regenerated from `p385_reconciled.tsv`: H 248 M 4 -> H 250 M 2.
Status unchanged: partial.

## R11-CLIN2380 (6 Oct 2026, account 2, LANE RUN11): 2380 cipher p.120 columns 3-7 checked against the decipherment on the 1778 key

Run 09:17-09:2x UTC 6 Oct 2026 (container clock read). Step: gap 2's named next (brief R11-CLIN2380). Intake gate exit 0
("partial (line 1) -- edition/page or full-text-search citation found within 6 lines"). Pre-registered in
`PREREG_R11-CLIN2380.md` (pushed c5d45b736 before the scored run). Script `passes/check_2380_c37.py` (output
`passes/check_2380_c37.json`, `--check` exit 0; `check_2380.py --check` still exit 0; `p134_reading.txt` unchanged).

**Image and crops.** H-1649 Image 758 (B.147 p.120) at full/max, 6032x4056, fetched once to the scratchpad only (folder at the
30 MB line; `regen_images.sh` line 107 re-fetches it). `tools/iiif_lines.py --image img758.jpg --region 2350,650,1250,2950 --out
il758` was run first and found 14 scattered line centres, no usable rows in a figure column (as on pp.382-384), so the columns were
cut by PIL box, inverted, each split into top/bottom halves with 120 px overlap: c3 x 2340-2600, c4 2570-2835, c5 2800-3060, c6
3030-3285 (y 680-3420), c7 3260-3560 (y 680-3560).

**Pass and reconciliation.** One blind Sonnet pass on the ten half-column crops (`passes/p120_c37_passA.tsv`, 273 cells: c3 51,
c4 51, c5 57, c6 55, c7 59). The worker re-read the failing cells on zoomed crops (`passes/p120_c37_reconciled.tsv`, note column)
and changed 7: five flat-topped 5s the pass read as 3 (c3.5 3-5 -> 5-5, c4.23 3-1 -> 5-1, c4.42 3-3 -> 5-5, c5.36 1-3 -> 1-5,
c6.34 3-1 -> 5-1) and two doubled figures (c4.51 6-27? -> 6-77, c7.55 2-12 -> 2-77). The decipherment text covered runs from
"convention" (after GAPS9's 25 aligned words) to "had they arrived"; the length-only alignment put 55 of 58 cipher words on
equal-count decipherment words, in order, with no gap until "with us".

| statistic (gate: variant share >= 0.80 and count > control max) | blind pass | reconciled |
|---|---|---|
| cells read | 273 | 273 |
| compared cells | 258 | 258 |
| page letter = decipherment letter, printed 1778 page | 169 | 174 |
| same, line 1 as GAPS9's variant PERMISION/HONORABLE (pre-registered) | 219 (0.849) | 224 (0.868) |
| shuffled-plaintext control, 1000 seeds: mean / p95 / max | 17.7 / 24 / 32 | 18.0 / 24 / 32 |
| gate | PASS | PASS |

**Off cells, two systematic patterns (found after the score, not gated).** (1) Line 9: every line-9 cell beyond position 3 is one
place short of the printed "OFFICERS in the several REGIMENTS", as if the encipherer's line 9 read OFICERS: 9-15 for v (six times:
five here -- convention, having, view, however, arrived -- and GAPS9's own), 9-4 for c (clamours), and "regiments" written as the run
9-20 ... 9-28. Re-scored with line 9 as OFICERS: 240/258. This is the same shape as GAPS9's line-1 shift (PERMISION/HONORABLE).
(2) Doubled figures: a cell L-PP whose two digits repeat stands for the letter at P written twice -- 6-77 "ll" in "still", 2-77 "rr"
in "arrived", 5-22 "ff" in "officers" here, and GAPS9's three excluded cells fit the same rule (2-99 "tt" in "letters", 2-44 "ss" in
"matross", 6-77 "ll" in "artillery"), so the encipherer did not drop doubled letters there; he wrote them as a doubled position. The
gate counts these three as failures (pre-registered rule); the json lists them under `doubled_figure_cells_not_in_gate`.
Line 1 is not fully fitted by the variant either: 1-25 stands for r five times (purpose, clamours, their, three, GAPS9's artillery),
where the variant has o and the printed page n; and 1-9/1-11 ("so") and 1-23 ("however") fit the printed page, not the variant.

**Remaining mismatches, clear on the zoomed image (encipherer slips):** 13-16 for d in "had" (d is 13-10), 1-24 for t in
"negociation", 18-7 for u in "purpose" (GAPS9 also has an 18-7; u is 18-17), 6-16 for a in "clamours", 6-10 for "I" (i is 6-12),
6-22 for e in "three" (e is 6-21). **Cipher/decipherment conflict (rule 4, by witness, not settled):** after
"with us" the cipher has three more words, `1-7|` (i), and `1-27 -16|` (a + e/h, or a-m if the second cell is -6: the image
shows 16 or 6 with a stroke that may be the 7 above, M), before "disappointed"; the period decipherment (recipient side, p.134)
has "with us, disappointed so my Expectations" with no "I am". The aligner paired `1-27 -16` with "us", so two gate failures
there are alignment, not key. Witnesses: cipher p.120 (sender's encipherment as copied at Quebec) "I a[m]"; decipherment p.134
omits; VHS II (1871) p.192 not checked for this phrase in this run.

**Grades (rule 4), the 273 cells against the decipherment:** C 224 (key-consistent compared cells under the pre-registered
variant), M 49 (34 mismatching compared cells, 15 cells not compared: 12 in "reinforcement", 12 cells for 13 letters, page letters r-e-n-f-o-?-c-e-m-e-n-t: the i omitted and
one cell 5-17 out of range, reported apart -- and the 3 unpaired cells `18-17 4-3` "us" and `1-7` "i"). With GAPS9 (columns
1-2), the p.120 cipher is now read against the decipherment in all 7 columns.

**Not done:** pp.121-122 (Images 759-760). The p.120 cipher ends at "had they arrived"; the decipherment runs on about 150 words
("would with the 650 Recruits ... by the Defiance"), so pp.121-122 probably carry the continuation (GAPS9 guessed duplicate; not
looked at). Stopped here by the brief's rule (another page would cross 80% of the cap). Requests: image-uab.canadiana.ca 1 (Image
758 full/max, 200). Vision calls: 1 blind Sonnet pass; worker looks at a 1/5 frame, one contact sheet and four zoom montages.
Status unchanged: partial.

## R11-CLINV3 corrections (6 Oct 2026, account 2, LANE RUN11; verifier of R11-CLIN2380, AUDIT.md section "R11-CLINV3")

- R11-CLIN2380 "after 'with us' the cipher has three more words": two after "us" (`1-7`, `1-27 -16`); the native crop reads the
  second cell plainly as ditto-16 (not "16 or 6"), so the cipher word is a-e / a-h on the key and "I a[m]" is inferred (m = I grade).
  The conflict with the decipherment stands, by witness.
- c5.51 `15-5?` reads 15-55 ("pp" in disappointed, line 15 letter 5 = p): a seventh doubled-figure cell. Pre-registered count with it
  corrected: 223/258 (0.864), gate still PASS (control max 32). `passes/p120_c37_reconciled.tsv` not edited here; next session that
  re-runs `check_2380_c37.py` changes that row and the JSON together (rule 7).
- Line 9: all 16 compared cells fit "one place short"; 9 of them are one run, and no cell has P <= 3, so OFICERS is one reading of the
  shift, not established over another. Gate, PREREG order and the 224/258 re-score confirmed.
## R11-CLIN2380B (6 Oct 2026, account 2, LANE RUN11): 2380 cipher p.121 checked against the decipherment on the 1778 key

Run 09:35-09:5x UTC 6 Oct 2026 (container clock read). Brief R11-CLIN2380B (continue R11-CLIN2380 on pp.121-122).
Pre-registered in `PREREG_R11-CLIN2380B.md` (pushed 4aa284973 before the scored run). Script `passes/check_2380_p121.py`
(output `passes/check_2380_p121.json`, `--check` exit 0; it reuses check_2380_c37.py's alignment and carries the line figure
and the decipherment position from p.120). AUDIT.md not touched (R11-CLINV3 is working there).

**Frames.** H-1649 Image 759 = B.147 p.121 (BL fo.105v, 8 cipher columns, ends with a slash); Image 760 = p.122 (fo.106,
5 columns + a "P.S." column, "(Signed) H. Clinton", endorsement fo.106v "From Sir Henry Clinton 1779 / 22d Oct Recd 20th May
1780 by Express via Niagara"). Both fetched once at full/max to the scratchpad only (6016x4056, 6024x4056; folder at the
30 MB line, not committed). So pp.120-122 are one copy of the cipher, the continuation, not a duplicate; this copy came by
Niagara and was received 20 May 1780, while the p.134 decipherment's endorsement says the cipher letter came "par Halifax"
and was received 18 Jan 1780 -- two routes, two copies.

**Crops.** `python3 tools/iiif_lines.py --image img759.jpg --region 1900,600,1900,2900 --out il759` (and the same for 760):
"wrote 0 crops", no usable rows in a figure column, as on pp.120, 382-384. Columns cut by PIL box with
`passes/cut_2380_p121_122.py IMG_DIR OUT_DIR` (boxes in the script). The first cut (SHEAR=0 PAD=0) clipped the right-hand
figures low on the page, because the columns drift right by 50-90 px down the page; the blind pass marked 153 of 440 cells
uncertain. The recut (default SHEAR=0.025, PAD=30) shears that drift out and widens each box.

**Pass and reconciliation.** One blind Sonnet pass on the sixteen first-cut half-column crops of p.121
(`passes/p121_passA.tsv`, 440 cells). Because of the clipping the reconciliation became a full re-read by the worker of
every cell on the recut crops, done before any scoring (`passes/p121_reconciled.tsv`, 445 cells, passA aligned beside it).
On the 287 cells the pass read without "?", the two agree on 282 (0.983); the 5 differences are 3 figures and 2 underlines.
Two cells settled on a zoom and graded M: c5.42 1-1 (pass A's reading; a short hooked top as this hand writes 1) and
c6.51 6-6 (the stroke before the 6 is the tail of the 7 above).

| statistic (gate: (b) share >= 0.80 and (b) count > control max) | p.121 |
|---|---|
| cells read / cipher words | 445 / 90 |
| compared cells (equal-count word pairs) | 420 |
| (a) page letter = decipherment letter, printed 1778 page | 324 |
| (b) line 1 as GAPS9's PERMISION/HONORABLE (gated) | 406 (0.967) |
| (c) (b) + line 9 as OFICERS (secondary) | 411 (0.979) |
| (d) (c) + doubled-figure cells as the letter at single P (secondary) | 415 (0.988) |
| shuffled-plaintext control, 1000 seeds, under (b): mean / p95 / max | 29.7 / 38 / 45 |
| same under (c) / (d): max | 45 / 46 |
| gate | PASS |

Both p.120 patterns recur as pre-registered secondaries: line 9 one place short (9-15 for v in "have", "seven", "convalescents",
"having" and "violent", with 9-16 for e in "seven") and doubled figures (5-55 "ee" in "fleet", 1-88 "ss" in "missing" and
"unless", 5-22 "ff" in "affairs"; the read below prints these single, as the decoder takes the letter once). The cipher read under (d), unedited: "would have amounted to rather more thae your demand they sailed under conhoy of
the renown but unfortunately met with aviolent storm which dispersed the flet and damaged the ships the renown has since
returned here with seven companies and some convalescents of the forty fourth and some part of the regiment of loosberg but
the whole of the regiment of anyphausen and the remainder of the british are mising nrom the present situation of afairs
georgia will be eyposed to great danger unles south carolina is reduced having therefore".

**Remaining mismatches (5), clear on the recut crops, so encipherer's slips:** 1-4 for n in "than" (e), 1-15 for v in
"convoy" (h), 20-34 for k in "Knyphausen" (a; k is two places on), 6-9 for f in "from" (n; f is two places on), 1-2 (via the
ditto after 1-4) for x in "exposed" (y). Reported apart by count, not in the gate: "a violent" written as one cipher word
(8 cells), "will" with ll as two cells 6-7 6-7, "Loosberg" for "Lossberg" (1-10 o twice, c5.42 1-1 b at M), and the first
cipher word "would" which the length-only aligner paired with "Europe" (below).

**Cipher/decipherment conflict (rule 4, by witness, not settled):** the p.120 cipher ends "had they arrived" and p.121 begins
"would have amounted to rather more than your demand"; the period decipherment (p.134, Halifax copy, received 18 Jan 1780)
reads "had they arrived would with the 650 Recruits and Artillery from Europe have amounted". Witnesses: cipher pp.120-121
(Niagara copy, received 20 May 1780) omits the clause; decipherment p.134 has it; VHS Collections II (1871) p.192 checked R12-CLINVHS: print has the clause (follows the decipherment)
for this phrase in this run. Whether the clause is in the p.122 P.S. is not known (p.122 not passed).

**Grades (rule 4), the 445 cells against the decipherment:** C 406 (key-consistent compared cells under the pre-registered
variant), M 39 (14 compared cells failing (b): 5 line-9, 4 doubled figures, 5 slips; 25 cells in the four count-differing
words). The p.121 cipher ends at "having therefore", so p.122 should run from "no alternative left" to "by the Defiance" plus
the P.S.

**Not done:** p.122 (Image 760; six column crops cut by the script, no pass). Stopped by the brief's rule: by the brief's
price list (session floor 1.5 + one Sonnet pass 1.5 + the full re-read as the reconciliation unit 1.5) the job stood near
4.5 of the 5 cap, past 80%, so another page would cross it. Requests: image-uab.canadiana.ca 2 (Images 759, 760 full/max,
200 each, 2 s apart). Vision calls: 1 blind Sonnet pass; worker looks at two 1/5 frames, two grid previews, five montages,
one zoom. Status unchanged: partial.

## R11-CLINV4 corrections (6 Oct 2026, account 2, LANE RUN11; verifier of R11-CLIN2380B, AUDIT.md section "R11-CLINV4")

- The PREREG hash 4aa284973 cited in "R11-CLIN2380B" and in `passes/check_2380_p121.py` is not on origin/main (folded by a push
  rebase); `PREREG_R11-CLIN2380B.md` reached origin in a9a1f8d62 (09:40:25 UTC), an ancestor of the scoring commit eb2319c59
  (09:45:32 UTC). Order holds.
- The gate (406/420, control max 45) re-scores exactly. Beside it: pass A alone scores 256/420 (0.610, FAIL on share) because 139
  compared cells were unread on the clipped first cut; on the 281 it read, about 256 fit under (b) and 274 under (d). The PASS
  rests on the worker's key-aware re-read; quote both figures.
- The "Recruits and Artillery from Europe" conflict is confirmed by eye on both images (cipher p.121 c1 goes "would" -> "have" with
  nothing between; decipherment p.134 has the clause). Held by witness, unsettled: Niagara cipher copy without, Halifax-route
  decipherment with. `check_2380_p121.json`'s `unpaired` list omits the six skipped decipherment words (leading gap).

## R11-CLIN2380C (6 Oct 2026, account 2, LANE RUN11): 2380 cipher p.122 checked against the decipherment on the 1778 key

Run 09:55-10:02 UTC 6 Oct 2026 (container clock read). Brief R11-CLIN2380C (continue R11-CLIN2380B on p.122). Pre-registered
in `PREREG_R11-CLIN2380C.md` (pushed e2861d54e before the scored run). Script `passes/check_2380_p122.py` (a copy of
check_2380_p121.py that reruns p.121's alignment to find p.122's start; output `passes/check_2380_p122.json`, `--check` exit 0;
check_2380_p121.py and check_2380_c37.py `--check` still exit 0). AUDIT.md not touched (R11-CLINV4 is working there).

**Image and crops.** R11-CLIN2380B's crops were in its scratchpad only, so Image 760 was fetched once more at full/max (6024x4056,
scratchpad, not committed). `python3 tools/iiif_lines.py --image img760.jpg --region 1900,600,1900,2900 --out il760` wrote 0 crops
(as before); the six columns were cut with `passes/cut_2380_p121_122.py IMG_DIR OUT_DIR` (default SHEAR 0.025, PAD 30), twelve
half-column crops.

**Pass and reconciliation.** One blind Sonnet pass on the twelve crops (`passes/p122_passA.tsv`, 292 cells: c1 50, c2 55, c3 56,
c4 52, c5 39, c6 = the P.S. column 40; 2 cells marked ?). The worker re-read on the native crops the 2 uncertain cells, the 5
key-failing compared cells and the word boundaries of the count-differing words (`passes/p122_reconciled.tsv`, note column); no
cell changed (c2.33 4-1 kept at M, a hooked tail after the 1). Length-only alignment from "no alternative left": 59 cipher words
on 59 decipherment words, in order, no gap, ending "by the Defiance" (the P.S. column is the decipherment's last two lines,
"I have received your Dispatches by the Defiance").

| statistic (gate: (b) share >= 0.80 and (b) count > control max) | p.122 |
|---|---|
| cells read / cipher words | 292 / 59 |
| compared cells (equal-count word pairs) | 252 |
| (a) printed 1778 page | 180 |
| (b) line 1 as GAPS9's PERMISION/HONORABLE (gated) | 242 (0.960) |
| (c) (b) + line 9 as OFICERS (secondary) | 247 (0.980) |
| (d) (c) + the doubled-figure rule verified by R11-CLINV3 (secondary, separate variant) | 247 (0.980) |
| shuffled-plaintext control, 1000 seeds, under (b): mean / p95 / max | 18.05 / 25 / 32 |
| same under (c) / (d): max | 31 / 31 |
| gate | PASS |

(d) adds nothing here: no compared cell is a doubled figure. Doubled letters on p.122 are written as two repeated cells instead
("shall" and "will" twice: 4-1 4-1; "fleet" 1-4 1-4; "cooperate" 21-2 21-2), which makes those words count-differ and puts them
outside the gate. The cipher read under (c), unedited: "no alternative left i shall detach a considerable armament for that
purpose i hope your indians will be prevailed upon to threaten the nrontiers of virginia in great force which will operate
infavor o f the southern move while a considerable nieet may probably be employed to cooperate ib the chesapeak i havl
received your dispatches by the defianca".

**Remaining mismatches (5).** Four clear on the native crops, so encipherer's slips: 6-9 for f in "frontiers" and again in "fleet"
(word apart; with 6-12 for l) -- the same 6-9-for-f as p.121's "from", three times now, so it may be a line-6 variant rather than a
slip (not tested); 1-1 for n in "in [the Chesapeak]" (b); 4-1 for e in "have" (l); 2-13 for e in "Defiance" (a). The fifth is not a
slip: 6-6 (a, clear) in "Chesipeak" -- the cipher spells "Chesapeak", the decipherment "Chesipeak" (below).

**Cipher/decipherment conflicts (rule 4, by witness, not settled).** Witnesses: cipher p.122 (Niagara copy, received 20 May 1780);
decipherment p.134-135 (Halifax copy, received 18 Jan 1780); VHS Collections II (1871) p.192 checked R12-CLINVHS: "move" and "Chesapeake" follow the cipher.
(1) "Southern movements": the cipher has `1-6 1-10 9-15 1-4|` "move", underlined, the next cell starting "while"; the decipherment
has "movements". (2) "Chesapeak" (cipher) vs "Chesipeak" (decipherment). (3) Word division only, no text difference: the cipher
writes "in favor" as one word (no underline under c3's last 1-11 or before c4's 5-2) and "of" as two (1-12| 1-13|).
The Recruits-from-Europe clause (R11-CLIN2380B's conflict) is not in the P.S.: the P.S. is "I have received your Dispatches by
the Defiance" only.

**Grades (rule 4), the 292 cells against the decipherment:** C 242 (key-consistent compared cells under the pre-registered
variant), M 50 (10 compared cells failing (b): 5 line-9 cells that fit OFICERS, 4 slips, 1 Chesapeak; 40 cells in the nine
count-differing words). With R11-CLIN2380 (p.120), R11-CLIN2380B (p.121) and GAPS9 (p.120 columns 1-2), all three pages of this
cipher copy (pp.120-122) are now checked cell by cell against the period decipherment, and the cipher ends where it does.

Requests: image-uab.canadiana.ca 1 (Image 760 full/max, 200). Vision calls: 1 blind Sonnet pass; worker looks at a 1/5 frame,
one six-column contact sheet and two native-resolution montages. Status unchanged: partial.

## R11-CLINV5 corrections (6 Oct 2026, account 2, LANE RUN11; verifier of R11-CLIN2380C, AUDIT.md section "R11-CLINV5")

- The PREREG commit e2861d54e cited in R11-CLIN2380C and in `passes/check_2380_p122.py` does not resolve on origin/main; the
  reachable one is 99d7ccc3e (10:00:17 UTC), ahead of the scoring commit 62c179565 (10:02:35 UTC). Order holds.
- Conflict (3) is half wrong: c4.6 `1-12` has no underline on the image (only the paper's printed ruling), so "of" is one cipher
  word `1-12 1-13|`. Only "infavor" is a word-division difference. With c4.6 corrected: 254 compared, (b) 244/254, (c)/(d) 249,
  control max 32, PASS; grades C 244 / M 48. `p122_reconciled.tsv` is left as committed (the verifier does not edit the worker's
  files); a later session that touches it should drop the bar at c4.6 and rerun `check_2380_p122.py`.
- Confirmed by eye: "move" (cipher) vs "movements" (decipherment), "Chesapeak" vs "Chesipeak", and the P.S. without the
  Recruits-from-Europe clause. Blind pass alone scores the same 242/252 (no cell changed at reconciliation).

## R12-CLINVHS (6 Oct 2026, 11:2x-11:4x UTC by date -u): the 2380 witness conflicts against VHS Collections II (1871) p.192

Witness record only (rule 4: no majority vote; key, readings and grades unchanged). Source: archive.org `collectionsofver02vermuoft`
djvu text (OCR; excerpt in `passes/vhs2_2380_print.txt`; not a page image, the OCR of these lines is clean). The print: "H. -- Sir Henry
Clinton to General Haldimand. Intelligence. 27th October, [1781.]", p.192, the letter running from "As for affairs at Cornwallis' army"
to "I have received your dispatches by the Defiance." and then the next entry, "Oct. 27. Col. Walbridge wrote ...". The print has no
postscript. Per conflict:
1. **"with the 650 Recruits and Artillery from Europe" (p.121 cipher omits, p.134 decipherment has it):** the print follows the decipherment:
   "which, had they arrived, would, with the 650 recruits and artillery from Europe, have amounted to rather more than your demand".
2. **"with us I a[m]" / "with us, disappointed" (p.120):** the print follows the cipher: "still the clamors of their own officers
   prisoners with us. I am disappointed in my expectations of a re-inforcement from the West Indies." (sentence break after "us",
   then "I am"); the decipherment p.134 omits "I am".
3. **"move" / "movements" (p.122):** the print follows the cipher: "operate in favor of the southern move, while a considerable fleet ...".
4. **"Chesapeak" / "Chesipeak" (p.122):** the print spells "Chesapeake", agreeing with the cipher's a (the cipher stops at "-peak"; the
   decipherment's i has no support in the print).
5. Word division "in favor of" (no text difference): the print has "in favor of" (OCR "favor" in one word; "of" one word), i.e. the
   one-word reading of "of" the verifier R11-CLINV5 found on p.122.
6. Postscript on p.122: the print carries none, so it neither supports nor contradicts the cipher's P.S.
Both witnesses are therefore split: the print follows the decipherment on 1 and the cipher on 2, 3 and 4; the print is a third copy
(Vermont's MS transcript, misdated 27 Oct 1781) and is a witness, not a key source. Requests: archive.org 2 (one 302 + one 200 for the same
djvu file, 1.67 MB); no page image fetched.

**p.122 bar correction (asked by R11-CLINV5, ROOM 10:20 UTC):** `passes/p122_reconciled.tsv` c4.6 entry 1-12| -> 1-12 (no underline; "of" is one
cipher word, 1-13| ends it). Rerun `check_2380_p122.py` (exit 0), `--check` OK: cipher words 59 -> 58, compared cells 252 -> 254,
(b) gated line-1 variant 242 -> 244/254 (0.961), (c) 249, (d) 249; shuffled-plaintext control (b) mean 18.06, p95 25, max 32; gate PASS
(same as the verifier's 244/254). 5 mismatches, 7 apart, 1 unpaired (was 9 apart, 0 unpaired).

## Remaining gaps (R15-CLINGAP refresh, 6 Oct 2026)
Refresh only, 17:2x UTC 6 Oct 2026 (worker R15-CLINGAP, LANE RUN15, account 2): each gap restated from the dated sections GAPS-GAPS12, A2P4-CLINT, R10-CLIN3868/3868B, R10-CLINV/CLINV2, R11-CLIN2380/B/C, R11-CLINV3-5 and R12-CLINVHS; no new reading, no request made. The 1 Oct 2026 section above is superseded.
Read so far: 20 of 20 items text-known or read at grade H/C -- the 12 named items (3689, 3753, 3784, 3803, 3813 at C from Stevens 1888; 6009, 6012 clear and printed; 2894, 3868, 2380 period decipherments read at H, N0 in AUDIT.md; 3853's f.381 decipherment printed 1920 vol. III doc 260; 4833 and its 22 June 1782 enclosure printed VHS Collections II pp.280-282) and the 8 Discovery siblings (2962, 3004, 4152 printed 1920 vol. III; 3502, 3537, 4216 printed VHS II; 3050, 3077 read at H from B.147 pp.245-246, N0) plus the 26 Oct 1782 note (Carleton 25 Sept 1782, p.102 read at H, GAPS7). Cipher side checked cell by cell on the 1778 Army List key: 2894 all 315 pairs (GAPS2), 3868 all four pages (GAPS8 cols 1-2 + R10: p.382 cols 3-6 97/100, pp.383-384 526/535), 2380 all three pages pp.120-122 (GAPS9 + R11: 224/258, 406/420, 244/254 after the R11-CLINV5/R12 bar fix); partly: 3050/3077 (118/118 opening cells, GAPS12) and the 25 Sept 1782 p.123 copy (32 opening pairs, GAPS7). Witness conflicts (Digby/Darby; the 650 Recruits clause, "I am", move/movements, Chesapeak) are recorded per witness (R10-CLINV, R12-CLINVHS), not gaps. What is left is cipher-side checking, one of which can still add text (3853).
- 3853 cipher, f.406 (Robertson to Haldimand, 31 Oct 1781, PRO 30/55/33/47) - blocker: not-attempted; the printed f.381 text is a "decoded extract" (Tomokiyo), so the f.406 cipher may carry more than the extract -- the only remaining step that can change text rather than confirm a key; the frame is unconfirmed (about Image 1056 by Tomokiyo's f.1 = Image 1070 anchor arithmetic, GAPS gap 4); next: fetch the frame by the image-uab.canadiana.ca route in images/h1649/manifest.json, confirm the page label, cut column crops (tools/iiif_lines.py --image or passes/cut_cipher_cols.py), PREREG a key-consistency gate against the 1920 doc 260 text with the shuffled-plaintext control used in R10/R11, one blind Sonnet pass + reconciliation, ~$4.5
- 3537 key check from the print (Kew sibling, VHS Collections II pp.338-341 prints a cipher specimen, pp.341-342 its translation; reel cipher Image 958) - blocker: not-attempted; text already known, a key check only (GAPS11); next: fetch the archive.org djvu text of collectionsofver02vermuoft once, parse the printed figure pairs and apply the 1778 key (passes/key_2894.tsv / check_2894_key.py logic) against the printed translation with a shuffled-plaintext control, script only, no vision, ~$1
- Reel ciphers of the other text-known siblings not checked: 2962, 3004, 3502 (Image 945), 4152, 4216 (Image 1090), and the rest of 3050/3077 (p.242 cols 4-6, pp.243-244, p.247 cols 3-8) - blocker: not-attempted; key-consistency checks on items whose text is printed or read at H, low value (GAPS11, GAPS12); next: per page, frame fetch + one blind pass + reconciliation, ~$3-4.5 a page, only after the 3853 step
- Rest of the 25 Sept 1782 p.123 cipher (Image 1205, on disk as images/h1649/img1205_w1600.jpg; only 32 opening pairs checked, GAPS6/GAPS7) - blocker: not-attempted; text read at H from p.102 (218 words), a key check only; it may show the 1782 word-code elements Tomokiyo left blank; next: column crops from the native frame, PREREG, one blind pass + reconciliation, ~$3.5
- Cipher of the 22 June 1782 letter enclosed in 4833 (Haldimand to Carleton No. 1) - blocker: needs-physical-access; the reel copy B.148 pp.39-40 (Images 1115-1116) is clear, headed "In Cypher" (GAPS10), so the enciphered copy exists only at Kew (PRO 30/55, Discovery digitised=false) or C.O. 5/106 p.361; text known (VHS II pp.280-282), a key check only
- Kew-side physical copies (Clinton's retained copies of 2380 incl. its duplicate, 2894, 3868; PRO decipherments "Vol.11 Nos.117/190"; Am. & W.I. 142 fo.150, 145 fo.87) - blocker: needs-physical-access; Discovery C16266110 digitised=false (1 Oct 2026), no image route; every one of these letters is already read from the recipient-side reel, so this matters only for a token-level Kew-copy comparison (REQUEST.md for a TNA copy order would be a person step, ~$1 to draft)

## Escalation (6 Oct 2026, R15-CLINGAP refresh)
- [x] siblings: Kew side swept (AX-STEV2, AX-HMC2), the date-bounded Discovery queries found the 8 further siblings (GAPS, discovery_clinton_to_haldimand_2026-10-02.tsv); all 8 are text-known or read at H (GAPS5, GAPS11, GAPS12, A2P4-CLINT); DECODE no hit (23/25 Sept)
- [x] clear-pages: every period decipherment on H-1649 for the named items and siblings is read (f.186 2894, pp.385-386 3868, pp.134-135 2380, pp.245-246 3050/3077, p.102 the 25 Sept 1782 copy); 3853's f.381 extract and the 4833 enclosure are in print
- [x] known-keys: the 1778 Army List title-page key (archive.org listofgeneralfie00grea, GAPS4) is confirmed against the cipher of 2894, 3868, 2380, 3050/3077 and p.123 with shuffled-plaintext controls; KEY-OFFICES.tsv/KEY-DESIGN.tsv have no Clinton-Haldimand row yet (a close-out step, not a gap)
- [x] print: HMC vols 2-3, Stevens 1888, Brymner 1884-89, 1920 vol. III (A2P4-CLINT), VHS Collections II and Walton II (GAPS10-11, R12-CLINVHS), Google Books, JSTOR rows; verifiers VERIFY-CLINTON-* logged N0 for 2894, 3868, 2380, 3050, 3077
- [n/a] key-rebuild: no key is being extended; the 1778 key reads every checked cell, and the 1782 word-code blanks matter only for the p.123 rest and the Kew 4833 cipher
- [x] image-check: frames confirmed on the images (Image 759 = p.121, 889/890 = B.147 pp.245/246, 1205 = B.148 p.123, 1115-1116 = B.148 pp.39-40); every key-failing cell in R10/R11 re-read on zoomed crops; Brymner's foliation matches the reel (AX-HMC2, R11-CLIN2380B)
- [ ] retry: the remaining cipher pages above are not yet passed; planned: the 3853 f.406 pass first (the one step that can add text), then the 3537 print check
Verdict: keep going: 4 internal gaps; cheapest next: 3537 key check of VHS Collections II's printed cipher specimen against its printed translation on the 1778 key, script on one archive.org djvu text, no vision, ~$1 (the step that can still add text is the 3853 f.406 cipher against the printed f.381 extract, ~$4.5); 2 gaps blocked outside (needs-physical-access, Kew/C.O. 5); the 2380 p.122 step named in the 1 Oct Verdict ran (R11-CLIN2380C) and the 3868 verifier ran (R10-CLINV2)
