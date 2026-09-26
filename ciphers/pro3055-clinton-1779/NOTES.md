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
| 2894 (PRO 30/55/24/76) | 1780 (year only) | Clinton to Haldimand | content matched to a British Museum/Library comparison copy per HMC's own 1904-09 note | known elsewhere (via the BM/BL copy, not by breaking the cipher) | outside Saberton's scope; locate the BM/BL comparison copy directly (specific enough crib: French fleet, 3 May, seven ships of the line) |
| 3868 (PRO 30/55/33/65) | 12 Nov 1781 | Clinton to Haldimand | HMC Report calendar paraphrase only, page not opened | partly known | outside Saberton's scope (Haldimand correspondent; also after CP pt.11's 19 Oct 1781 end) — open the HMC Report |
| 3853 (PRO 30/55/33/47) | 31 Oct 1781 | Robertson to Haldimand | HMC Report calendar paraphrase only, page not opened | partly known | outside Saberton's scope (Robertson/Haldimand, not Cornwallis/Clinton) — open the HMC Report |
| 4833 (PRO 30/55/42/120) | 23 June 1782 | Haldimand to Carleton | HMC Report calendar paraphrase only, page not opened | partly known | outside Saberton's scope entirely (different correspondents, different year, different theatre) — open the HMC Report |
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
