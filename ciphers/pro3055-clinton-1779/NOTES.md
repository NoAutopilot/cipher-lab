partial

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

## Check-solved sweep (24 September 2026)

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
