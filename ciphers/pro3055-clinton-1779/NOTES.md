partial
HMC Report on American Manuscripts (1904-09) read by this worker via the TNA Discovery item-level API (the calendar's own published text, across PRO 30/55/19, /24, /32, /33, /42, /53) plus a be-api full-text search across five archive.org scans of the same Report for entry "2894" (control "Clinton" confirmed the search path works; target "2894" returned no hit in any scan checked); the more specific edition for the Yorktown-dated items -- Ian Saberton, *The Cornwallis Papers* pt.11 (Naval & Military Press, 2010) -- was identified this sweep as the likely holder of a decipherment but was not opened (Google Books gives `NO_PAGES`, not on Internet Archive, not JSTOR/HathiTrust/academia.edu).

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
