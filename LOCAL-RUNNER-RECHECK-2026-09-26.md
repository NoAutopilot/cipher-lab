date: 2026-09-26
runner: ChatGPT (owner's machine)
kind: review of prior local-queue runs
rows: L10, L12, L3, L4, L14, L5, L19, L24, L20, L21

# Desk recheck: ten prior local-queue runs

The owner requested a recheck of every prior run, then directed that gateway errors, bot checks and other failures be recorded accurately for later attention. This is a cross-row review, rather than a queued-row submission. Its PR title deliberately does not match an existing row's ingestion prefix. No queue entry, earlier answer, manuscript transcription or outreach draft is changed by this report.

Provenance: the prescribed runner label above is retained, but this work used ChatGPT's remote cloud browser and execution workspace, not the owner's physical computer or home IP. Browser observations, public-PDF extraction, search-index metadata and earlier reports are distinguished below. No credential was entered or saved. No CAPTCHA was interacted with or bypassed. No loan was created during this recheck; the prior L20 report records that its loan was returned.

Standing instructions were read from `tools/local_queue_runner_prompt.md` on main, blob `f05d17307aa206a97492e294177d06f8daf18394`. The owner's later request broadened this run to reviewing the ten existing reports. The catalogue ladder was consulted. Access failures are not absence findings.

## Outcomes

| Row | Prior PR | Recheck outcome | Evidence limit |
| --- | --- | --- | --- |
| L10 | [13](https://github.com/NoAutopilot/cipher-lab/pull/13) | blocked: Banco de Portugal security verification | Neither PDF was read; the earlier volume-2 tool size limit was a different failure. |
| L12 | [14](https://github.com/NoAutopilot/cipher-lab/pull/14) | answered: official 44-page article recovered and searched | No qualifying individual 1600–1610 Dutch key identified in this paper; DECODE itself was not exhaustively searched. |
| L3 | [15](https://github.com/NoAutopilot/cipher-lab/pull/15) | blocked: HathiTrust Cloudflare verification | Requested phrase searches could not run. |
| L4 | [18](https://github.com/NoAutopilot/cipher-lab/pull/18) | blocked on repeat access: same HathiTrust verification | Prior volume-level leads retained; no independent page-level confirmation. |
| L14 | [19](https://github.com/NoAutopilot/cipher-lab/pull/19) | blocked on repeat access: same HathiTrust verification | Prior successful reading of printed pp.176–177 retained, not independently confirmed again. |
| L5 | [20](https://github.com/NoAutopilot/cipher-lab/pull/20) | blocked: Gallica Altcha verification | Camusat attempted; Champollion-Figeac not attempted after the host block. |
| L19 | [22](https://github.com/NoAutopilot/cipher-lab/pull/22) | catalogue availability confirmed | Three volume results say “NOT AVAILABLE ONLINE”; no manuscript leaves inspected. |
| L24 | [23](https://github.com/NoAutopilot/cipher-lab/pull/23) | catalogue coverage expanded to A.24* and separated-material notes | No Stamford/Calais item or old-page-to-modern-folio mapping identified. |
| L20 | [24](https://github.com/NoAutopilot/cipher-lab/pull/24) | blocked on repeat access: 502 Bad Gateway | Prior successful reading retained; no loan created during recheck. |
| L21 | [25](https://github.com/NoAutopilot/cipher-lab/pull/25) | blocked: IA 502 and publisher Cloudflare verification | Publisher metadata confirms pp.65–66; disputed groups and message header could not be inspected. |

## L12 — recovered article and bounded negative

Target: `ciphers/oldenbarnevelt-brederode-1605`.

The exact [Uppsala repository PDF](https://uu.diva-portal.org/smash/get/diva2:1718372/FULLTEXT01) supplied in the queue loaded in the cloud browser. A direct public download returned HTTP 200, application/pdf, 7,750,993 bytes. The complete file has 44 PDF pages: a publisher cover followed by article pages 1–43.

Source: Megyesi, Tudor, Láng, Lehofer, Kopal, de Leeuw and Waldispühl, *Keys with nomenclatures in the early modern Europe*, DOI 10.1080/01611194.2022.2113185, online 3 November 2022. The journal issue assigns pp.97–139, Cryptologia 48(2), 2024. Citations below use the pagination actually printed in the downloaded version.

All 44 PDF pages were text-extracted. Case-insensitive searches for `Dutch`, `Oldenbarnevelt`, `Brederode`, `States-General`, `States General`, `1600`, `1605` and `1610` produced no text hits. Broader stems `Oldenbarnevel\w*` and `Brederod\w*`, `Staten`, `Holland`, and the 1600–1610 date range also produced no text hits. “Netherlands” occurs in general sample/archive descriptions, an affiliation and references.

Page checks:

- Article p.8 / PDF p.9, §4 “Sample of keys”: 1,610 keys had been registered in DECODE by 14 June 2021. Individual document images and metadata are in DECODE. Figure 3 aggregates keys by century and holding country; it does not supply an individual Dutch key dated 1600–1610.
- Article p.33 / PDF p.34, §8.3 “Regional tendencies”: the Netherlands is among the groups excluded from that regional analysis because they “contained less than 10 keys each.” This is a statement about the analysis described there, not a claim that the entire sample contains fewer than ten Dutch-held keys.
- Article pp.40–41 / PDF pp.41–42, Appendix, “List of Archives”: the Dutch institutions listed are Koninklijk Huisarchief (KHA), Museum voor Communicatie and Nationaal Archief, at The Hague. This appendix lists institutions rather than individual key shelfmarks, correspondents or dates.

Rendered page images for article pp.8, 33, 40 and 41 were inspected against the extracted text. No individually identified Dutch/Netherlands/Oldenbarnevelt/Brederode/States-General key dated 1600–1610 was found in the full extracted text, inspected figures or archive-list appendix. This is a finding about the paper; it does not rule out such a record in DECODE.

PDF SHA-256: `5773415c2feacb746fafd524d904adcbe378f753ddc863712f3d177da803e27c`.

Correction to carry forward: the earlier inability to read this article is resolved. The official repository PDF can be downloaded and searched locally.

## L19 and L24 — catalogue coverage and folio locations

Target: `ciphers/thurloe-printed`.

The [MARCO search for Rawl. A. 24](https://marco.ox.ac.uk/search?q=Rawl.+A.+24) initially displayed an Anubis check, then loaded automatically without interaction with the check. All three relevant volume results displayed “NOT AVAILABLE ONLINE”:

| Volume | MARCO record | Recheck observation |
| --- | --- | --- |
| MS. Rawl. A. 24/1 | [part 1](https://marco.ox.ac.uk/ark:29072/x0x920fw11hz) | Availability label in search results; direct record already quoted in PR22/23. |
| MS. Rawl. A. 24/2 | [part 2](https://marco.ox.ac.uk/ark:29072/x0qz20ss12rj) | Availability label in search results; direct record already quoted in PR23. |
| MS. Rawl. A. 24* | [part 3](https://marco.ox.ac.uk/ark:29072/x0f4752g9867) | Direct record opened: March 1655, 66 leaves, “NOT AVAILABLE ONLINE”, three Connections items. |

This supports the catalogue's stated online availability. It does not establish an absence of a decipherment on physical leaves. Digital Bodleian's earlier empty search results were not reused as proof of digitisation status.

### Collection-wide text extraction

The Archives & Manuscripts collection search for the exact phrase `"Rawl. A. 24"` returned 40 catalogue cards over two pages. Both pages' visible record cards were extracted together: 37 item records and three volume records. These are catalogue descriptions, not 40 manuscript images and not necessarily 37 distinct documents. The descriptions contain no `Stamford`, `Calais`, `cipher` or `decipher` text. “Translation” occurs in two cards.

Search source: [Rawlinson collection search, page 2](https://archives.bodleian.ox.ac.uk/repositories/2/resources/15417/search?q[]=%2A&op[]=&field[]=keyword&from_year[]=&to_year[]=&filter_q[]=%22Rawl.+A.+24%22&sort=&page=2). The companion page was reached through this collection's search UI. The earlier PR23 contains the individually opened 15 item records under A.24/1 and 19 under A.24/2. In this recheck those descriptions were reviewed through the extracted cards; their 34 detail pages were not all reopened.

### A.24* item records opened in this recheck

All three MARCO Connections records and all three linked full Archives & Manuscripts records were opened. Each MARCO record displayed “NOT AVAILABLE ONLINE”. The two March-dated records satisfy the date part of L24's request.

| Date | Modern shelfmark as displayed | Title / descriptive evidence | Item records and location notes |
| --- | --- | --- | --- |
| 16 Mar 1655 | MS. Rawl. A. 24*, fols.75,95,96 | “Intercepted letter [professedly on commercial business] from one Johan Laurens…” to Jacob von Oorschott. Summary: “With a translation.” | [MARCO x05q47rp5098](https://marco.ox.ac.uk/ark:29072/x05q47rp5098); [Archives 820474](https://archives.bodleian.ox.ac.uk/repositories/2/archival_objects/820474). **Separated Materials:** “For fol. 75, see MS. Rawl. A. 24/1.” |
| 7 Mar 1655 | MS. Rawl. A. 24*, fols.97,109–112 | “Four mercantile letters to Mr. Cornelius Vanderhoeve of Antwerp…” signed Rob. Shawe, Zach. Gardiner and initials. | [MARCO x0hh63sv97x3](https://marco.ox.ac.uk/ark:29072/x0hh63sv97x3); [Archives 820475](https://archives.bodleian.ox.ac.uk/repositories/2/archival_objects/820475). **Separated Materials:** “For fols. 97, 109–111, see MS. Rawl. A. 24/1.” |
| Date not recorded | MS. Rawl. A. 24*, fol.427 | “Prisoners bayled forth of his highness's Tower of London” | [MARCO x041687j33zv](https://marco.ox.ac.uk/ark:29072/x041687j33zv); [Archives 820476](https://archives.bodleian.ox.ac.uk/repositories/2/archival_objects/820476). No separated-material note displayed. |

The same titles/folio ranges also appear among the earlier A.24/1 or A.24/2 records. These are additional catalogue records and location evidence, not evidence for three additional letters. In particular, the A.24* shelfmark heading must be read alongside the full record's separated-material note before ordering leaves.

No inspected part-3 description names Stamford or Calais, or explicitly labels a cipher, decipherment or enclosure. “With a translation” does not by itself identify a decipherment. The modern folio corresponding to Birch's “vol. xxiv p.73, 76” remains **not found**. Old printed pagination must not be substituted for modern foliation.

### What the PDF button does, and its observed failure

On Archives & Manuscripts item 820440, the button's own help text says: “Download a PDF version of the catalogue for this entire collection”. It is a catalogue export for the Rawlinson collection, not a link to photographed manuscript leaves.

The collection is [Rawlinson Manuscripts, resource 15417](https://archives.bodleian.ox.ac.uk/repositories/2/resources/15417). The requested item URL contains archival-object ID 820440; that numeric difference alone is not proof of a broken export. The upstream ArchivesSpace route can resolve an item to its parent collection, while the exact deployed server behaviour was not established.

Observed failures: the UI export did not yield a download; the collection export navigation ended with `net::ERR_ABORTED`, and no download event/file appeared within 45 seconds. A separate direct HTTP attempt reached an Anubis page and was stopped. No 504 status was observed in these specific attempts, so none is asserted here. The server-side cause remains undiagnosed. The working catalogue HTML and the 40-card extraction provide an alternative way to inspect the descriptions without that export.

## Access failures and evidence retained

### L10 — Banco de Portugal

Target: `ciphers/antt-linhares-chave`.

Requested PDFs: [volume 1](https://www.bportugal.pt/sites/default/files/ocpep-7_t1.pdf) and [volume 2](https://www.bportugal.pt/sites/default/files/ocpep-7_t2.pdf).

blocked: both direct PDF requests returned HTTP 403 with HTML titled “A verificar se a ligação é segura / Checking if the site connection is secure”. Volume 2 in the cloud browser displayed Cloudflare verification and did not reach the PDF. This is a bot/security check, not a finding about book contents.

The earlier run's volume-2 error was a tool content-length limit of 39,059,461 bytes, not evidence of a publisher denial. This recheck distinguishes that earlier tool limit from the presently observed security screen. No pages or requested phrases were searched. An Internet Archive metadata query for the title and Coutinho/Souza/Sousa found an unrelated podcast entry, not a usable copy of these volumes.

### L3, L4 and L14 — HathiTrust

blocked: [HathiTrust full-text search](https://babel.hathitrust.org/cgi/ls) displayed “Just a moment…” and “Performing security verification”, with text identifying protection against malicious bots. It remained on that screen after passive observation. The shared host block prevented repeat searches/readings for all three rows; the individual readers were not probed through alternative routes after that block.

- **L3**, `ciphers/fr2980-gramont`: the requested searches including `faict ledit article a part`, `l adresse de dessus a vous`, `oster de suspecon` and Gramont/Villandry could not run. No hit count or book-content absence is claimed.
- **L4**, `ciphers/eckert-1864`: retain PR18's volume-level leads. *Louisiana Historical Quarterly*, v.24 (1941), Hathi ID `uva.x004123533`, was an earlier search match, with a “Limited - search only” reader. That does not establish the letter on a particular page. Earlier “cavalry depot here” results included Grant Papers v.15 copies `mdp.39015012429398`, `uc1.b3540506`, `wu.89062231824`, plus *Musical World* v.31 (1890), `hvd.32044043849850`. No candidate page was independently read in this recheck.
- **L14**, `ciphers/sp53-16-78` and `ciphers/sp53-16-79`: retain PR19's earlier reading of *Calendar of State Papers Scotland*, VIII, printed pp.176–177, Hathi ID `miun.abe1726.0008.001`, scans 211–212. That report quotes cipher placeholders in entry 227, “TO MR TEMPEST”, and entry 228, “TO DOCTOR BARRET”. Their earlier absence-of-decipherment finding is not independently reconfirmed here.

Internet Archive metadata searches for the Louisiana 1941 volume and the Boyd 1914 volume returned HTTP 502. Those failed searches supply no absence evidence.

### L5 — Gallica

Target: `ciphers/fr2980-gramont`.

blocked: the [Camusat 1619 texteBrut link](https://gallica.bnf.fr/ark:/12148/bpt6k5039434/texteBrut) led to “Gallica | Vérification de sécurité”. The page displayed “Pour poursuivre, merci de cocher cette case” and an unchecked “Je ne suis pas un robot” control. No interaction with the Altcha challenge was attempted.

The [Champollion-Figeac 1847 texteBrut link](https://gallica.bnf.fr/ark:/12148/bpt6k204021j/texteBrut) was not attempted after the same-host block, matching the actual sequence in PR20. The queue's statement that both books redirected is broader than that report supports. It should be treated as a host-level access obstruction, with only Camusat's redirect directly observed.

Neither raw text was obtained or searched. There is no supported “no hits” result for Gramont, Tarbe, Villandry, vingtiesme or the requested phrases. Internet Archive metadata searches for the two books also returned HTTP 502.

### L20 — Internet Archive Mercy volume

Target: `ciphers/espagnol142-mercy-1648`.

blocked: [IA item correspondancede0006jose](https://archive.org/details/correspondancede0006jose) returned “502 Bad Gateway” and “[Errno 111] Connection refused”. This is a gateway/connection failure; it does not establish a bot check or borrowing restriction. No loan was created during this recheck.

Retain the earlier successful reading in PR24, without representing it as reread now: printed p.647 / reader position 662 of 943, entry 1499, dated 11 June 1648, summarizes Peñaranda to Philip IV and mentions Mercy. It did not contain the requested 6 June instruction. The prior index reading at printed p.901 / reader 916 records “MERCY (L'abbé de), 647, 15, 20.” The 15 and 20 are line references on p.647. The prior loan was returned.

### L21 — Cryptologia article

Target: `ciphers/koehler-1944`.

blocked: the exact [IA issue sim_cryptologia_1981-04_5_2](https://archive.org/details/sim_cryptologia_1981-04_5_2) returned “502 Bad Gateway” and “[Errno 111] Connection refused”. The prior run reported “Borrow Unavailable” and a print-disability access tier; this recheck did not reach that loan interface, so the current error is recorded separately.

An alternative primary-source record was located through the web search index: [Taylor & Francis article metadata](https://www.tandfonline.com/doi/abs/10.1080/0161-118191855841) and its [issue contents](https://www.tandfonline.com/toc/ucry20/5/2?nav=tocList) identify David Kahn, “GERMAN SPY CRYPTOGRAMS”, Cryptologia 5(2) (1981), **pp.65–66**, DOI 10.1080/0161-118191855841. Browser access to the publisher then stopped at Cloudflare's “Performing security verification” page; no article image was obtained.

This metadata corrects the older reference to printed p.69 in the target's NOTES. A search API's `page_num` field should not be treated as a printed-page label without checking the page image. The later queue instruction already uses pp.65–66 correctly.

The six disputed five-letter groups and message-3 header/length remain unverified against this printing. No transcription was substituted from a secondary source.

## Follow-up register

- L10: retry the official PDFs later; retain both the historical tool-size failure and the current security-check result.
- L3/L4/L14: revisit HathiTrust when accessible. Preserve L4's unconfirmed candidate-volume scope and L14's earlier successful page reading.
- L5: retry Camusat later, then attempt Champollion-Figeac if the host permits access.
- L20: revisit after the gateway failure clears only if another independent read is needed; preserve the prior page/index evidence.
- L21: revisit IA or publisher access; metadata alone cannot settle the disputed letters.
- L19/L24: manuscript images and the Stamford modern-folio mapping remain unavailable from the inspected online records. The owner retains the reproduction request.

No manuscript solution status changed. No main-branch file was edited and no PR was merged.
