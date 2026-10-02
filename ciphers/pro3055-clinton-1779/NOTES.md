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

**2894 f.186 decipher pilot: 2 blind Sonnet passes + own reconciliation (3 vision units).** Crops: `tools/iiif_lines.py --image` on the text block of img829_full.jpg (defaults found 0 lines on this faint microfilm; `--distance 110 --prominence 40` gave 15 bands, some holding two lines; a second run on the endorsement strip gave 2). Passes `passes/p186_passA.tsv`, `passes/p186_passB.tsv` (17 rows each); reconciliation `passes/p186_reconciled.tsv`; reading `passes/p186_reading.txt`, regenerated by `passes/build_p186.py` (`--check` exits 0 on the committed text, rule 7). Agreement: 6 of 17 crops identical; of the 11 differing, 5 differ only in superscript notation, 5 in whether a line clipped at a crop edge was read at all, 1 in a word (Lawrence/Laurence; crop L11 reads "Laurence"). Tokens of the decipherment body (lines 1-23): **119, H 116, M 3, C 0, S 0, I 0** (rule 4: H because every token is read from the period decipherment itself, the key source; M for "Terney", "a" and "4", each read on the page view only or by one pass with a clipped crop). The fo.161v endorsement (line 25) is a single own read, outside the crop bands. No judge run: the target has no `specs/` entry and the reading is a transcription of clear text, not a decode. The text: "I have received your dispatches of Novr & January &c I have received Information from the Ministers of the 3d May Monsieur Terney is supposed to have sailed about the 3d May with seven ships of the line, & from 20 to 25 Transports &c having on board five Thousand two hundred land Forces & that their destination is stil supposed to be Canada – by Information I have received here the french Armament will assemble at Rhode Island, a division of which will proceed under the Command of the Marquis de Fayette by Connecticut Rivers and No 4 across the lakes to Saint Johns, the other by the river Saint Laurence; — H C 6th July / Copy." It matches HMC's 1904-09 paraphrase of 2894 ("a French force had sailed around 3 May with seven ships of the line...") word for word where HMC quotes, so the Kew cipher (PRO 30/55/24/76) and this decipherment are the same letter; 2894 moves to **text known, grade H** (not C: the text is in manuscript on the reel, not in print; the only prior text located anywhere is HMC's paraphrase). What this does not do: it does not verify the cipher against its key (the figure pairs on pages 184-185 are on disk but untranscribed); that is the next step below. Rule 10: report what was found and where it was not found; no novelty class is assigned here.

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

**The clause f.186 omits (`passes/clause_2894_1778.tsv`, 32 tokens: C 18, H 14, no I or M).** 16-7 16-30 16-13 16-22 16-20 16-7 16-24 = **Admiral** (16-24 l now H from line 16 "The Royal Regiment of Artillery, and Corps of Engineers") -- clear **A** -- clear **will be** -- 20-33 20-39 20-37 20-35 20-10 20-9 20-15 20-16 20-13 20-4 = **reinforced** (line 20 "The Dates of their Commissions, as they rank in each": r33 e39 i37 n35 f10 o9 r15 c16 e13 d4) -- 21-9 21-10 = **in** (line 21 of the 1778 page is "CORPS and in the ARMY": c-o-r-p-s-a-n-d-i-n, so i9 n10; Tomokiyo's 21-17 y is the 17th character, as GAPS3's better-supported candidate said) -- 1-3 1-5 1-11 1-3 1-13 1-5 1-15 1-10 1-11 1-12 = **proportion** (1-10 i now H). The clause reads **"Admiral A will be reinforced in proportion"**, with "A" the clerk's bare initial (Arbuthnot is the expansion GAPS3 proposed, not a cell) and "mar" opening the separate "Marquis" group. It is a reading from the key on H-1649 page 184 of a passage the period decipherment skipped, not located in f.186, HMC's paraphrase or any print searched on 2 Oct 2026 (a search result, rule 10); **clause ready for a verifier** (C 18, H 14).

**Folder size.** The folder stood at 29.8 MiB before this step; with the native 1778 page it crossed 30 MiB, so the superseded 1761 reference copy is re-stored at 1600 px wide (`images/armylist/n4_w1600.jpg`, manifest updated, regenerable from its URL) and the three 1520-px copies of H-1649 images 827-829, whose cited full-size files sit beside them, are deleted and marked `deleted` in `images/h1649/manifest.json` (regenerable by resizing the `_full` file or refetching); 29.85 MiB after. Requests per host this job: www.googleapis.com 5, archive.org 8, openlibrary.org 1; HathiTrust 0. KEY-OFFICES/KEY-DESIGN rows remain the lane's close-out step.

`python3 tools/gaps_check.py pro3055-clinton-1779` (06:2x UTC, after the edits below): `OK keep-going pro3055-clinton-1779: keep going: 7 internal gap(s), 2 step(s) untried` / `gaps_check: 1 checked: 0 parked, 1 keep-going, 0 FAIL, 0 skipped`, exit 0. `tools/intake_gate_check.py` after the step: exit 0.

## Remaining gaps (finish-or-blocker pass, 1 Oct 2026)
Read so far: 6 of 12 named items text known: 5 at grade C (3689, 3753, 3784, 3803, 3813, all from Stevens 1888 vol.2 page images; NOTES AX-STEV, AX-STEV2 "Status") and 2894 at grade H (119 tokens, H 116 M 3, the period decipherment on H-1649 page 186, GAPS 2 Oct 2026). 6009 and 6012 are clear covering notes printed in full (HMC vol.3 p.187, AX-HMC), so 5 of the 10 cipher documents proper are read. The token fraction is unmeasured: no ciphertext of any item is on disk in this folder. The only cipher tokens on disk are Tomokiyo's short opening extracts (figure pair + letter) for 2380, 2894, 3868 and 3853 in sources/cryptiana/web/haldimand.htm (cached 26 Sept 2026). The Kew items are not digitised (Discovery C16266110 digitised=false, 1 Oct 2026).
- 2894, PRO 30/55/24/76 (Clinton to Haldimand, 6 July 1780; the Kew copy is cipher only) - blocker: not-attempted; RESULT 2 Oct 2026 (GAPS): the period decipherment on H-1649 page 186 (= fo.161) is read, 119 tokens H 116 M 3 (passes/p186_reading.txt, build_p186.py --check exit 0), and matches HMC's paraphrase; RESULT 2 Oct 2026 (GAPS2): the cipher is transcribed (315 figure pairs, two passes agreeing 0.931, passes/cipher_reconciled.tsv) and checked against the key: 166 cells recovered, consistency 0.971 vs shuffled plaintext 0.459, Tomokiyo cells 79/81 exact vs shuffled key mean 5.85 (check_2894.json); grades H 264 C 18 M 33; the cipher carries a clause f.186 skips (Admiral A will be reinforced by proportion, read at C/H/M from the key) and spells Ternay; RESULT 2 Oct 2026 (GAPS3): archive.org listofgeneralfie00grea_0 is the 1761 edition (leaf n4 is the title page, n3 a blank flyleaf); mapped to the 1778 key by the fixed cells it keeps the 1778 wording on 14 of 25 lines (fixed cells 158/161 on those lines vs shuffled-letter controls at 0.06-0.28), and from those lines 23 of the 33 M tokens resolve at grade I: the clause reads Admiral A will be reinforced [in] proportion with the preposition open (21-9/21-10: 'as' on the 1761 Corps line, 'in' on the wording that fits all six of Tomokiyo's line-21 cells), grades now H 264 C 18 I 23 M 10, clause tokens C 18 H 2 I 10 M 2 (passes/clause_2894.tsv, title_1761_check.py --check exit 0); clause ready for a verifier; RESULT 2 Oct 2026 (GAPS4): the 1778 printing itself is on archive.org (listofgeneralfie00grea, Pittsburgh copy; Google Books full view has 1756, 1773 and 1834 only), title page page/n12 fetched and read (1 Sonnet pass + the worker's own, agreeing on all 30 lines); every key line is the same-numbered printed line, fixed cells 286/291 agree (the 5 all logged: 1-37, 13-11, 16-7, 23-25, 25-19; shuffled-character controls 0.03-0.28), the 11 lines the 1761 page left unconfirmed agree 125/126, and all 23 I and 10 M tokens read at H from the page: grades H 297 C 18; the clause reads 'Admiral A will be reinforced in proportion' (21-9/21-10 = 'in': line 21 is 'CORPS and in the ARMY'), clause tokens C 18 H 14 (passes/clause_2894_1778.tsv, title_1778_check.py --check exit 0); next: a verifier for the clause (a parent step, no further key work needed on 2894), ~$3
- 2380, PRO 30/55/19/98 (Clinton to Haldimand, 22 Oct 1779, copy and duplicate both in cipher, 4 + 3 pages) - blocker: not-attempted; HMC vol.2 p.53 prints no content (AX-HMC). Tomokiyo puts it at f.120-122 (Image 758-), decoded from f.134, opening "I was honored with your letter of the 19th July". His extract shows systematic -1 letter-position errors in the encipherment, so any later key check must allow an off-by-one rather than count it as a key failure. HMC's "fo.105" is BL foliation; next: Images ~758-776 (cipher plus decipher), two passes + reconciliation of the decipher pages, about 3 pages, ~$10
- 3868, PRO 30/55/33/65 (Clinton to Haldimand, 12 Nov 1781, in cipher, 3 pages) - blocker: not-attempted; HMC vol.2 p.348 prints no content, and the decipher citation "Vol.11 No.190" is untraceable (AX-HMC2). Tomokiyo puts it at f.382 (Image 1030), decoded on f.385; his extract decodes only "... of your proclamation and"; next: Images ~1030-1034, two passes + reconciliation of the f.385 decipher, ~$8
- 3853 cipher, PRO 30/55/33/47 (Robertson to Haldimand, 31 Oct 1781; HMC: "Auto draft. Vol.11 No.183; in cipher, 182 ... decipher 21807 fo.306") - blocker: not-attempted; correction to the classifier. Brymner's B.147 entry at "381" is not a clear covering letter. It paraphrases the decipherment: Brymner "381" = Tomokiyo f.381 "decoded extract" = HMC's BL "decipher fo.306", and Brymner's "406" = Tomokiyo f.406 = the cipher letter itself. So the content is already partly known (Brymner's paraphrase, plus the two sentences Tomokiyo quotes, "Sir Henry Clinton with about six thousand men went on board a fleat..."). The cipher letter opens in clear ("Dear Sir - Thanks for..."). Kew also holds Robertson's own autograph draft (No.183); next: Images ~1029 and 1056, two passes + reconciliation of the f.381 extract, then apply the period key to the f.406 cipher for any part the extract omits, ~$5
- Cipher enclosure of 4833, PRO 30/55/42/120 (Haldimand to Carleton, 23 June 1782, enclosing "a duplicate letter in cypher which he dispatched yesterday, overland", i.e. about 22 June 1782) - blocker: not-attempted; the 22 June letter is unidentified. Tomokiyo's Add MS 21808 list has no 22 June entry. His f.65A (Image 1142), Carleton to Haldimand, 3 Aug 1782, decoded on f.66-67, acknowledges "your excellency's letter of the 22[n]d June". The print/Discovery discrepancy is still open (AX-HMC, AX-HMC2: phrase searches only, never a date search). From 1782 the letters also use the word-code elements, some of which Tomokiyo left blank; next: page H-1649 Images ~1100-1145 (Tomokiyo f.31A-f.65A) for Haldimand's 22/23 June 1782 drafts and read the f.66-67 decipher, then grep the on-disk HMC vols 2-3 and Brymner djvu text for "June 22"/"22 June" 1782, ~$5
- The ciphered note forwarded by 6009/6012, PRO 30/55/53/7 and /10 (26 Oct 1782) - blocker: not-attempted; the note is unidentified. The candidate is Carleton to Haldimand, 26 Oct 1782 (HMC vol.3 p.187: draft PRO Vol.47 No.15, BM Add MS 21705 fos.71/78 and 21806 fo.20), and it is unconfirmed (AX-HMC). Correction to the classifier: H-1649 has only 1266 images, and Tomokiyo's Add MS 21808 list ends at f.123 (Image 1205, 25 Sept 1782). So the late-Oct 1782 leaves of 21808 probably run onto the next reel, not H-1649. Add MS 21807 begins at Image 637, which leaves Images 1-636 unidentified, and whether they hold 21806 is unconfirmed. Tomokiyo's "Vol.II begins at Image 1969" cannot be right on a 1266-image reel; his own f.1 = Image 1070 is the usable anchor; next: read Images 1 and ~600 and the last image of H-1649 for volume labels, find the reel holding late-1782 21808 and 21705 in the 48-reel Canadiana list, and read Carleton 26 Oct 1782 there, ~$4
- Completeness of the item list (unnamed Kew copies of Clinton-Haldimand cipher letters) - blocker: not-attempted; RESULT 2 Oct 2026 (GAPS): the date-bounded Discovery queries were run (discovery_clinton_to_haldimand_2026-10-02.tsv) and found six further Kew cipher copies outside the six swept pieces (2962, 3050, 3502, 3537, 4152, 4216) plus two unflagged siblings (3004, 3077), each with its reel decipherment at Tomokiyo's position; none is read yet; next: the f.186-style pilot (two passes + reconciliation of the reel decipherment) on each, cheapest first by page count, about $5 each, ~$30
- Kew-side physical copies (Clinton's retained copies of 2380, 2894, 3868, 4833; the PRO decipherments "Vol.11 Nos.117/190"; the Am. & W.I. 142 fo.150 and 145 fo.87 copies of 3868 and 4833) - blocker: needs-physical-access; Discovery C16266110 digitised=false (1 Oct 2026), and no image route is known. The recipient copies and period decipherments of the same letters are on H-1649, so this matters only if a token-level check against the Kew copy itself is wanted after the reel reads; next: only then, write REQUEST.md for a TNA copy order (a person step), ~$1

## Escalation (1 Oct 2026)
- [ ] siblings: Kew side done. AX-STEV2 swept all six pieces and found the 12 cipher-flagged items. AX-HMC2 traced old "vol 11" to 14 modern pieces, but Nos.117/190 are untraceable. DECODE had no hit (23/25 Sept). Not yet opened: the recipient-side volumes on LAC reel H-1649 (BL Add MS 21807 from Image 637, 21808 from Image 1070, 1266 images in all; re-checked 1 Oct 2026). They hold the Haldimand copies of 2380, 2894, 3868 and 3853 beside their period decipherments, and Tomokiyo lists about nine more sibling cipher letters of the same pair. Planned: the H-1649 fetches above, starting with 2894 -- done for 2894 on 2 Oct 2026 (route in images/h1649/manifest.json); the other seven follow.
- [ ] clear-pages: Done for the five Cornwallis-Clinton items (Stevens 1888, AX-STEV/AX-STEV2) and for the clear covering letters 4833, 6009 and 6012 (HMC). For 3853, Brymner's "381" entry is a paraphrase of the decipherment itself. Not yet read: the period decipherments themselves (Tomokiyo: f.134- for 2380, f.186 for 2894, f.385 for 3868, f.381 for 3853; f.66-67 for Carleton's 3 Aug 1782 reply), all on H-1649. These are the decipherments themselves, grade H once transcribed; f.186 (2894) transcribed 2 Oct 2026, 119 tokens H 116 M 3.
- [x] known-keys: KEY-OFFICES.tsv and KEY-DESIGN.tsv have no Clinton, Haldimand or Cornwallis row (grep, 1 Oct 2026). Saberton's "Common cipher" (JAR 2019) covers Cornwallis-Clinton 1780-81 and is moot for the five read items. Untried: the Haldimand-Clinton book cipher. Its figure pairs give a line and a letter in the title page of "A List of the General and Field Officers" (1778), per Tomokiyo, haldimand.htm, and LESSONS-TOMOKIYO.md rows 66-67, which were never linked to this target. Its explanation sheet is at Add MS 21807 f.323-326 (Tomokiyo f.402-405, Images 1051-1054), and Tomokiyo gives a 1782 word-code table. Done for 2894 on 2 Oct 2026 (GAPS2) without the title page itself: the 315 pairs of pages 184-185 against the f.186 decipherment recover 166 cells at consistency 0.971 (shuffled plaintext 0.459) and agree with Tomokiyo's independent cells 79/81 (shuffled key mean 5.85); the key is the title page as described, with omitted repeated first figures and a doubled letter dropped. The only title page on archive.org is the 1761 printing (GAPS3, 2 Oct 2026): it confirms the 1778 wording of 14 of the 25 key lines with cells and leaves 11 unconfirmed; the 1778 page itself is gap 1's next step. The 1778 page itself is on archive.org after all (listofgeneralfie00grea, GAPS4, 2 Oct 2026): it confirms all 25 key lines (286/291 fixed cells, the ampersand counted as a character) and reads every open cell of 2894 at H. Add the KEY-OFFICES/KEY-DESIGN rows at close-out.
- [x] print: Searched HMC Report vols 2-3 page images (AX-HMC); Stevens 1888 vols 1-2 (AX-STEV, AX-STEV2), which give the five C items; Brymner, Report on Canadian Archives 1884-89, B.147, phrase searches (AX-HMC2); the Google Books API (GBOOKS); Saberton CP pt.11, identified but NO_PAGES (LOCAL-QUEUE L16) and not needed for the five read items; JSTOR rows 129-130, one with no hit, one a Lafayette Papers chapter waiting on ASKS row 76 that concerns 3813, already read. No printed full text found for the Haldimand-side items; only Tomokiyo's incipits and Brymner's paraphrase of 3853's decipher. A date-keyed grep for 4833 is folded into its gap.
- [n/a] key-rebuild: No key is being extended. The 1779-81 items use a known period book key and have period decipherments in the same volume, and no ciphertext is on disk. Revisit only if the June 1782 (4833) or Oct 1782 (6009/6012) cipher uses the 1782 word-code entries Tomokiyo left blank.
- [x] image-check: All five read items were checked on Stevens 1888 page images; this corrected the OCR misread of 3689's "Original was written in Cypher" endorsement (AX-STEV). The other seven entries were checked on HMC vol.2-3 page images (AX-HMC). AX-HMC2 suspected Brymner's "406" was an OCR misread of "306"; it is not. Brymner's numbers match Tomokiyo's reel-volume foliation (406 = Robertson cipher, 381 = its decoded extract, 184 = Clinton 6 July 1780), while HMC's fo.306 is BL foliation. This should be confirmed on the H-1649 images during the reads.
- [x] retry: Until 2 Oct 2026 no ciphertext was on disk; 2894's cipher (pages 184-185) now is, beside its decipherment, and the verification pass named in the 02:55 Verdict ran the same day (GAPS2: key applied to the 315 figure pairs, compared with the f.186 text, numbers in gap 1). The other seven reel decipherments are still unread (gap 7).
Verdict: keep going: 7 internal gaps; 2894's key work is complete (H 297 C 18 on the 1778 page, GAPS4) and its omitted clause (Admiral A will be reinforced in proportion, C 18 H 14) waits on a verifier, a parent step; cheapest next: gap 6's reel-label read (H-1649 Images 1, ~600 and the last image, for the volume labels that place late-1782 Add MS 21808 and 21705 in the 48-reel Canadiana list, then Carleton 26 Oct 1782 there), ~$4; after it 3853 (Images ~1029 and 1056, two passes + reconciliation of the f.381 extract, ~$5)

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

Result: no decipherment or plaintext of item 2894 (or of any other Clinton-Haldimand cipher letter named in this folder) located by these queries on 2 Oct 2026; the only text of 2894 located anywhere is the period decipherment on the reel itself (below). A search result, not a novelty verdict (rule 10). Requests: WebSearch 8, cryptiana.blogspot.com 2, allthingsliberty.com 1, vermonthistory.org 1.
