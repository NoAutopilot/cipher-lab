open
CSP Domestic Charles I 1629-1631 (archive.org calendarofstatep0000john_l7u8) full-text search (be-api) by this worker 2 Oct 2026: 'Stanning' and 'Stannyng' 0 hits, positive control 'Sir Henry Vane' 1 hit (Mervyn to carry Vane over, 1631); SP 81 itself has no printed calendar for 1631, so this is the nearest edition, not the series' own.

# Duplicate of a paper sent by Mr Stanning, in cipher — TNA SP 81/37/284

QUEUE row: N60 (sources/solver-diffs/2026-09-23-non-decode-hits.tsv, "Candidates not on DECODE").

## Source

The National Archives, Kew, **SP 81/37/284** (State Papers Foreign, German States), folio 284, [?1631] (TNA
Discovery, fetched 24 Sept 2026, id C7774544; `digitised: false` confirmed by direct record fetch; no separate
`note` field). Scope content: "Folio 284: Duplicate of paper sent by Mr. Stanning in cipher." 1631 is the year
Gustavus Adolphus of Sweden entered the Thirty Years' War in earnest (Breitenfeld, Sept. 1631); Sir Henry Vane
the Elder was sent to Germany that September as English envoy to Gustavus Adolphus's camp, reporting to
Secretary of State Dudley Carleton, Viscount Dorchester.

## Check-solved sweep (24 September 2026)

1. **Editions.** No comprehensive printed calendar or edition covers SP 81 (German States) correspondence for
   1631 — this series has no CSP Foreign equivalent for the Caroline period, and WebSearch for a printed
   edition of Vane's 1631 Swedish-camp correspondence with Dorchester (`Henry Vane elder 1631 Swedish camp
   correspondence Dorchester printed edition letters`) returned only general Vane biography (Wikipedia, SSNE
   database, Find a Grave) with no edition named. "Mr Stanning" is too thin a name to search independently;
   WebSearch (`"Stanning" 1631 Vane Dorchester Gustavus Adolphus cipher correspondence English`) returned no
   identification and only tangential Thirty Years' War background.
2. **Sibling search (TNA Discovery, same piece) — a key/decipher lead.** `tools/discovery_items.py "SP 81"
   "SP 81/37" decipher` finds three items in the same piece with contemporary decipher work already noted by
   the cataloguer: **SP 81/37/93** ("Vane to 'my lord' with duplicate and decipher," 1631 Oct. 19), **SP
   81/37/169** ("Vane to Dorchester — 3 letters with decipher of one," 1631 Dec. 3), and **SP 81/37/216** ("Vane
   to [Dorchester], with portion deciphered," 1631 Dec. 11/22 (sic)). This confirms the piece as a whole carries
   active Vane<->Dorchester ciphered traffic from the Swedish-camp mission, with at least three folios TNA
   itself already marks as (partly) deciphered — the same "look for the sibling" shape as sp81-roe-1638's f.88
   lead, though here the target is explicitly a **duplicate** of a paper "sent by Mr. Stanning" rather than a
   Vane-Dorchester letter itself, so it is not certain the three decipher-marked folios share Stanning's key; a
   "duplicate" also implies an original survives, possibly catalogued or annotated elsewhere. Not resolved by
   image (none online).
3. **Community lists.** WebSearch and local grep of `sources/cryptiana/` for "Stanning"/"SP 81/37": no hits.
4. **DECODE.** No login attempted. `sources/decode/` greped for "Stanning"/"SP 81/37": no hits.
5. **Solver repositories.** Both freshly shallow-cloned (24 Sept 2026, shared across this pass's four targets).
   `dbourdeau/cyphersolver` and `aaymeloglu/unsolved-ciphers`: grep for "stanning|SP.?81.?37" across both trees:
   zero matches naming this item, this piece, or "Stanning."
6. **General web search.** As (1) and (3). No result ties a decipherment, key, or prior reading to SP 81/37/284
   specifically, or identifies "Mr Stanning" as a known historical figure of the period.

**Host requests this pass:** discovery.nationalarchives.gov.uk 3 (search x2, record detail x1, >=3s apart,
shared budget with the other three targets this run), WebSearch 2, github.com 1 shallow clone each of both
repos (grepped, shared across all four targets), sources/decode/ and sources/cryptiana/ local greps (no
network).

## Verdict

**Status: open.** SP 81 German States has no printed calendar for 1631; no edition of Vane's Swedish-camp
correspondence was located; "Mr Stanning" could not be identified. No community list, DECODE record, or
solver-repository entry names this item. The strongest finding this pass is a **lead, not a clearance**: three
neighbouring folios in the same piece (ff. 93, 169, 216) are already catalogued by TNA as carrying contemporary
decipher work on Vane-Dorchester correspondence from the same months — worth ordering alongside the target (see
REQUEST.md), on the chance the same office cipher covers "Mr. Stanning"'s paper too, though this is not
confirmed and the target is a duplicate, which may point to a different original and route.

**Copy status:** no online image located; `digitised: false` confirmed by direct record fetch (id C7774544).
**Copy-order.** See REQUEST.md.

**Recommended next steps (not run this pass):** (1) [run 3 Oct 2026 by GAPS126, not identified -- see the dated section at the end] identify "Mr Stanning" — a Merchant Adventurers or Eastland
Company agent in the Baltic/German trade is plausible given the context, not checked this pass; (2) once
imaged, compare f.284's cipher symbols against the deciphered stretches of ff.93/169/216 to test whether it is
the same office key; (3) HMC reports for correspondents connected to the 1631 Swedish mission (not searched
this pass, outside this run's hosts).

## Web and blog check (GF-A2-6, 2 Oct 2026)

Plain web searches (WebSearch, 2 Oct 2026):
1. `"Stanning" 1631 cipher Vane Dorchester` -- TNA catalogue records in SP 81/37 (C7774522, C7774510, C7774505, C7774593, C7774512: Vane-Dorchester 1631, incl. f.216 "with portion deciphered") and british-history.ac.uk node 60372 (opened: CSP Colonial vol. 1 index pp. 566-570, Vane entries only, no Stanning, no cipher). Nothing on f.284.
2. `"SP 81/37" cipher decipher 1631` -- the same TNA records (ff.163, 193, 216), HistoCrypt and Tartu papers (Heusner von Wandersleben to Oxenstierna 1637; Portuguese 1649) and TNA's blog "Secret diplomatic message deciphered after 350 years" (opened: Perwich to Arlington, SP 78/129 f.180, 1670; no comments section; not this item).
3. `"Duplicate of paper sent by Mr. Stanning"` (the catalogue's own wording in quotes) -- no exact hit; unrelated Founders Online, Royal Society, Bentham and Stanford results.
4. `Mr Stanning 1631 Germany agent English intelligence Gustavus Adolphus` -- SSNE entries (William Curtius, William Swann), Swedish Intelligencer, Runeberg; no "Stanning" anywhere.

Blog site searches:
- Cipherbrain (scienceblogs.de), `Stanning cipher 1631`: only "Who can break this enciphered letter written by Albrecht von Wallenstein?" (2016; a different letter, not English, no Stanning) and unrelated posts.
- Cryptiana (cryptiana.blogspot.com, cryptiana.web.fc2.com), `Vane 1631 cipher Stanning`: no results.
- Cipher Mysteries (ciphermysteries.com), `Stanning Vane 1631 cipher`: only Voynich, d'Agapeyeff and fifteenth-century posts; none on this item.
No plausible hit for this item, so no comment thread bears on it.

Not found: no decipherment, plaintext or prior attempt for SP 81/37/284, and no identification of "Mr. Stanning", on the open web or in the three blogs.

## Premise check (GF-A2-6, 2 Oct 2026)

(a) Decipherments the folder already mentions: three same-piece folios TNA catalogues with contemporary decipher work -- f.93 (Vane to "my lord", "with duplicate and decipher", 19 Oct 1631), f.169 (Vane to Dorchester, "3 letters with decipher of one", 3 Dec 1631), f.216 (Vane to [Dorchester], "with portion deciphered", 11/22 Dec 1631). None is said to decipher f.284, and none is online to look at (unreachable); they stay the named calibration lead in REQUEST.md. Not found for f.284 itself.
(b) Other solvers' working files: fresh shallow clones of dbourdeau/cyphersolver and aaymeloglu/unsolved-ciphers (2 Oct 2026) grepped for `stanning`, `SP.?81.?37`: zero matches in either (Aymeloglu cited, not copied). Not found.
(c) Physical neighbours: no image online (`digitised: false`), so the leaves beside f.284 and any slip cannot be viewed -- unreachable. TNA Discovery (tools/discovery_items.py "SP 81" "SP 81/37" Stanning duplicate, 2 Oct 2026): "Stanning" matches only f.284; the duplicates in the piece are ff.93, 98, 145, 256 (Dorchester to Vane, 31 Dec 1631, the nearest catalogued item before f.284) and f.284 itself. No original of Stanning's paper and no decipher of it is catalogued in SP 81/37. Not found.
(d) Recipient side: the paper presumably went to Vane or Dorchester. Dorchester's side: CSP Domestic 1629-1631 searched above (Stanning 0 hits). Vane's 1631-32 mission: no printed edition of his dispatches located (web search 4 and the 24 Sept sweep). The Swedish side (Oxenstierna's Rikskansleren Axel Oxenstiernas skrifter och brevväxling) was not searched this pass. Not found in what was read.

## GAPS126-sp81-stanning-1631 (3 Oct 2026, account-4): identify "Mr Stanning"

Step run: Recommended next step (1), identifying "Mr Stanning" from open sources so as to name the series where a
sibling cipher letter, key or decipherment would sit. No vision, no subagents, no reading. Clock read 13:36 UTC.

| Host | Query (variants Stanning / Stannyng / Stanninge / Staning / Stannings) | Result | Positive control |
|---|---|---|---|
| TNA Discovery API (`API/search/records`, dates 1620-1640) | each variant | the only State Papers hit is the target itself (SP 81/37/284); the rest are Chancery suits (C 2/ChasI/H36/9 Hele v Stanning; C 2/ChasI/L35/13 Leach v Stanninge; C 2/JasI/P13/14 Nicholas Standing alias Stanning; C 3/415/67 Robert Staninge, Myton, Yorks; C 8/84/88 William Staning, 1639, St Keyne/Duloe, Cornwall) and local deeds. None in SP 75, SP 95, SP 84 or SP 16 | the "Stanning" query itself returns the target (SP 81/37/284), so the search reaches this series |
| Internet Archive be-api full text | each variant in CSP Domestic Charles I 1629-31 and 1631-33, plus both volumes' indexes (4 items, `sim_great-britain-public-record-1625-1649-domestic-series_*`) | 0 hits in all 4 items for every variant | "Henry Vane": hits in 3 of the 4 items (1631-33 text, 1631-33 index, 1629-31 text; 0 in the 1629-31 index) |
| Internet Archive be-api, whole collection | "Mr. Stanning", "Mr Stanning" | 186 hits each, all 19th-20th century (fiction, a Lancashire parson, a jeweller); nothing 17th-century | n/a (whole-collection) |
| Google Books API (key, `country=US`) | "Stanning" with Vane 1631 / Gustavus / Hamburg merchant 1631 / cipher / Sweden-Stralsund-Danzig / Hamilton / agent | 0 relevant: the hits are Stanning family names in later records (Royalist Composition Papers, Lancashire, 1640s-50s), the place Stanningley and 19th-20th-century items | "Henry Vane" Gustavus 1631: 257 hits, incl. HMC Duke of Hamilton MSS (1887) on the 1631 Hamilton expedition |
| EMLO Solr (`solr/all/select`) | each variant | 0 records | "Vane": 137, including Sir Henry Vane 1589-1655 as a person record |

**Result: not identified.** "Mr Stanning" is not found in any calendar, catalogue or index searched above as an agent,
merchant or correspondent of 1631. The surname existed in England then (Chancery suits; a Cornish William Staning,
1639), but nothing links any of these people to the German mission. So no other series can be named for a sibling
letter, key or decipherment from the name. The nearest siblings stay the three same-piece folios TNA catalogues with
contemporary decipher work (SP 81/37 ff.93, 169, 216; REQUEST.md). Rule 10: this is a search result, not a finding
about the item.

Requests: discovery.nationalarchives.gov.uk 8, be-api.us.archive.org 26, archive.org advancedsearch 1,
www.googleapis.com 10, emlo.bodleian.ox.ac.uk 5; all one at a time, 1.6-2 s apart, no 429/403.

**Next step (cheapest):** recommended step (3): an IA full-text and Google Books search of HMC reports for the 1631
Swedish mission, starting with *The Manuscripts of the Duke of Hamilton* (HMC 11th Report app. VI, 1887). Hamilton led
the 1631 British expedition to Gustavus Adolphus, and the volume calendars letters of 1631. Search it for Stanning and
its variants, plus "cipher"/"cypher" on its 1631 pages. Cost: about USD 1, no vision. If that also fails, the target
can be read only from the image, so step (2) waits on the copy order (REQUEST.md).

## GAPS130-sp81-stanning-1631 (3 Oct 2026, account-4): HMC Hamilton MSS grep

Step run: GAPS126's named next step (recommended step 3), the HMC Hamilton volumes searched for "Mr Stanning" and for
cipher entries of the 1631 Swedish mission. Script grep of the full text, fetched once. No vision, no subagents, no
reading of the item. Clock read 13:54 UTC.

| Edition (IA identifier) | Route | Stanning / Stannyng / Staning / Stanninge / Stannings | cipher, cypher, decipher, character | Positive control |
|---|---|---|---|---|
| HMC 11th Report app. VI, *MSS of the Duke of Hamilton* (1887), `manuscriptsofduk00greauoft` (Toronto scan) | `_djvu.txt` (1.09 MB), regex | 0 | 30 hits. Most are the word "character" (a person's character, "of a historical character"). The only cipher entry of 1631-32 is **No. 59**, Hamilton to Charles I, Augsburg, May [1632], p. 81: "The first portion of this letter is in cypher, and seems to refer to an important interview between the King of Sweden and the English Ambassador" (the cipher part is not printed or deciphered in the calendar). All other cipher entries are 1647-50 (Nos. 270-396, Lanark and the Engagement; Camden Society 1880) | Vane: 6 hits, e.g. No. 39, Herbipoli [Würzburg] 9 Nov 1631 (Hamilton as umpire between Charles I "acting through Sir Henry Vane his ambassador" and Gustavus Horn); No. 52 (Vane's arrival in Germany); index "Vane, Sir Henry, ambassador; 74. arrives in Germany; 77". Gustavus 47, 1631 27 |
| Same edition, second scan, `manuscriptsofduk00grea_2` (Getty) | `_djvu.txt`, regex | 0 | 30 (same entries) | Vane 4, Gustavus 47 (an OCR cross-check, not an independent edition) |
| HMC 21, *Supplementary report on the MSS of the Duke of Hamilton* (1932), `supplementaryrep0000grea` | lending-only (`_djvu.txt` 401); be-api full-text search | 0 for each variant | cipher 1 item-level hit (passages "in cipher" to Lanark, 1640s; Sadler/Walsingham keys in the introduction), cypher 1 (1640s; index "Angus, cypher for England, 40") | Vane 1 (captains "recommended by Sir Henry Vane"), Gustavus 1 ("interview with Gustavus Adolphus described by, 21"; "an Imperial agent in the confidence of Gustavus nearly succeeded in preventing the expedition") |

**Result: not found.** No Stanning variant in either Hamilton report. Both searches passed the positive control:
the 1631 Hamilton-Vane-Gustavus entries are found in the same texts. The one cipher entry of the mission period is
Hamilton's own letter to the King (No. 59, May 1632). It is a separate cipher in Hamilton's papers. It is not a key or
decipherment for SP 81/37/284 and has no link to Stanning. Recorded as a possible later comparison: if the image of
f.284 is ever obtained, the Hamilton cipher of 1632 (Hamilton Archive, Lennoxlove) is one more 1631-32 Anglo-Swedish
cipher to set beside Vane's ff.93/169/216. That is a lead to check, not a finding. Rule 10: this is a search result
about the editions, not a finding about the item.

Requests: archive.org (metadata 3, download 3) 6, be-api.us.archive.org 8; one at a time, 1.6 s apart, no 429/403
(the 401 is the supplement's lending-only text, expected).

**Next step:** the open-source routes to identifying Stanning are now done: TNA Discovery, CSP Dom 1629-33, Google
Books, EMLO (GAPS126), and both Hamilton reports (this step). The item can only be read from its image, and step (2),
the copy order for f.284 and the siblings ff.93/169/216 (REQUEST.md), needs the owner. See "While waiting".

## GAPS134-sp81-stanning-1631 (3 Oct 2026, account-4): HMC Cowper (Coke) MSS grep

Step run: GAPS130's "While waiting" action. Secretary Coke's papers for 1631, as calendared in *The Manuscripts of the
Earl Cowper* (HMC 12th Report app. I-II, 1888), searched for "Mr Stanning", for cipher entries, and for the dates and
correspondents of the SP 81/37 siblings (f.93 Vane, 19 Oct 1631; f.169 Vane to Dorchester, 3 Dec 1631; f.216 Vane to
Dorchester, 11/22 Dec 1631). Script grep of the full text, fetched once. No vision, no subagents, no reading of the item.
Clock read 14:12 UTC.

| Edition (IA identifier) | Stanning / Stannyng / Staning / Stanninge / Stannings | cipher, cypher, decipher (1631-32 entries) | SP 81/37 sibling dates and correspondents | Positive control |
|---|---|---|---|---|
| Vol. 1 (1888), `manuscriptsofear01grea_0` (`_djvu.txt`, 1.92 MB; covers to May 1632) | 0 | 10 hits in the volume. Two fall in 1631: (a) p. 423, "1631", Coke's draft to Lord Conway on the intercepted letters of Du Molin and Short: "The deciphering of the letters is not yet perfected" (a French/Venetian intelligence matter, not the German mission); (b) p. 432, Sir Robert Anstruther to Coke, Vienna, June 1631: "I have no settled cypher with your honour". The rest are 1628-30 | none: no entry of 19 Oct, 3 Dec or 11/22 Dec 1631 from Vane; Vane's mission letters went to Dorchester, not Coke. The 1631 run has Anstruther (Vienna, 21 Oct O.S.), the Elector of Saxony's camp extract (10 Sept 1631, Breitenfeld) and naval and Irish business | Vane: 13 hits, incl. **1631, September 3, Bagshot, Sir H. Vane to Sir John Coke** (p. 440, the Bishop of Man vacancy, before Vane left for Germany); Vane to Coke from The Hague, 28 Mar 1630; Coke's copy letter of 16 May 1632 naming "the treaty now in hand by Sir H. Vane" |
| Vol. 2 (1888), `manuscriptsofear02grea_1` (`_djvu.txt`, 1.91 MB; starts 1632-3) | 0 | 3 hits, none 1631-32 (1630s-40s) | out of range (1631 occurs 3 times, all retrospective) | Vane: 18 hits, 1633-42 |

**Result: not found.** No Stanning variant in either Cowper volume, and no Coke-side copy or decipher of a Vane mission
letter of Oct-Dec 1631. Both volumes passed the positive control: Vane-Coke letters, including the 3 Sept 1631 Bagshot
entry, are found in the same text. The two 1631 cipher mentions concern other channels (Du Molin's intercepts; Anstruther
at Vienna, who says he had no cipher with Coke). They are not a key or decipherment for SP 81/37/284. Rule 10: this is a
search result about the edition, not a finding about the item.

Requests: archive.org (download) 2; one at a time, 1.6 s apart, no 429/403.

## GAPS139-sp81-stanning-1631 (3 Oct 2026, account-4): TNA Discovery sibling search, SP 75 / SP 82 / SP 95, 1631-32

Step run: GAPS134's "While waiting" action. TNA Discovery API (`API/search/records`, `sps.recordSeries`, `sps.dateFrom`
1631-01-01, `sps.dateTo` 1632-12-31), one term per call, 1.7 s apart, descriptive User-Agent. Keyword search sees only the
item description, not a separate `note` field (tools/discovery_items.py docstring), so an item noted "Partly in cipher"
only in its note is missed. No vision, no subagents, no reading of the item. Clock read 14:30 UTC.

| Series | cipher | cypher | decipher | character | Coverage control ("letter", same dates) |
|---|---|---|---|---|---|
| SP 81 (German States) -- positive control | 3, **incl. SP 81/37/284 (the target)** | 0 | 6 | 0 | n/a |
| SP 75 (Denmark) | 0 | 0 | 0 | 0 | 11 item-level hits (SP 75/12/*), so the series is catalogued at item level for these years |
| SP 82 (Hamburg) | 0 | 0 | 0 | 0 | 3 (SP 82/7/f16, 1631 Nov 26; f22, c. Mar 1632) |
| SP 95 (Sweden) | 0 | 0 | 0 | 0 | 3 (incl. SP 95/3/101, 1632 Aug 27/Sept 6) |

The positive control passed: the SP 81 "cipher" query returns the target. SP 81 cipher/decipher items of 1631-32 (all
by Vane, the mission's channel, beyond the three already in REQUEST.md):

| Reference | Date | Description (TNA) | Decipher noted |
|---|---|---|---|
| SP 81/37/93 | 1631 Oct. 19 | Vane to 'my lord' with duplicate and decipher | yes |
| SP 81/37/169 | 1631 Dec. 3 | Vane to Dorchester - 3 letters with decipher of one | yes |
| SP 81/37/216 | 1631 Dec. 11/22 | Vane to [Dorchester], with portion deciphered | yes |
| SP 81/38/76 | 1632 Feb. 20 | Vane to --- - decipher | yes |
| SP 81/38/206 | 1632 May 22 | Vane to ---, and decipher | yes |
| SP 81/38/250 | 1632 June 13/23 | Vane to Secretary of State - duplicate of despatch of 6/16 and extracts in cipher | no |
| SP 81/39/88 | 1632 Sept. 6 | Vane to Coke - decipher, and duplicate | yes |
| SP 81/39/402 | [? 1632] | 2 sheets of cipher [? fragments] | no |

Follow-up terms, same dates (6 calls): "duplicate" and "Vane" in SP 75 / SP 82 / SP 95. SP 75 "duplicate": 8 items, all
Averie (Joseph Averie, the Hamburg agent, filed in SP 75), Roe or [Vane] to Dorchester, 1631 (e.g. SP 75/12/220, 1631
Oct. 9, "[Vane] to Dorchester - and duplicate, with addition"); none mentions cipher. SP 75 "Vane": 19 items, the Denmark
leg of the mission (instructions SP 75/12/204, 210; credentials 198; Averie to Vane 1631-32; Vane to Anstruther and to
Hamilton, 7 Oct 1631). SP 82: 0 and 0. SP 95 "Vane": 1 (SP 95/3/108, Dec 1632, Vane's speech to the King of Sweden).
No Stanning in any description.

**Result.** No cipher, cypher, decipher or character item in SP 75, SP 82 or SP 95 for 1631-32, by description. The
three series are catalogued at item level for those years, so the zero is a search result, not a coverage gap. The
limit is that a cipher noted only in an item's `note` field would not appear. The 1631-32 cipher traffic that TNA
describes is all in SP 81 and all Vane's. **Sibling leads (same route or correspondents, not shown to share the key):**
the five further Vane decipher items in SP 81/38-39 (ff.38/76, 38/206, 39/88; and the cipher-only 38/250, 39/402) join
ff.93/169/216 as the pool that a key for Vane's mission cipher could be rebuilt from. Whether Stanning's paper used
Vane's cipher is not known. The duplicate was filed in Vane's piece, which is the only link. Averie's duplicated
letters to Dorchester and Vane (SP 75/12) are the nearest same-circuit traffic, but none is described as in cipher.
Rule 10: a search result about the catalogue, not a finding about the item.

Requests: discovery.nationalarchives.gov.uk 28 (16 term x series; 6 coverage: "letter" and "1631" per series, the "1631"
probes returning 0; 6 follow-up); one at a time, 1.7 s apart, all HTTP 200, no 429/403.

## GAPS143-sp81-stanning-1631 (3 Oct 2026, account-4): item records of the Vane 1631-32 cipher pool

Step run: GAPS139's "While waiting" action, but scoped down. The pieces are larger than a 30-request brief allows: SP 81/38
(Discovery id C5910245) has 141 items and SP 81/39 (C5910246) has 129, so a full `tools/discovery_items.py --notes` sweep
(children + details per item) would take about 272 requests. It is not run. Instead, item ids came from two keyword searches
("decipher", "cipher", series SP 81), followed by the `records/v1/details` record of each named item, using the same calls
`--notes` makes. Table: `sibling_pool.tsv` (6 items fetched this pass, plus the three SP 81/37 siblings from GAPS139's search
descriptions, not re-fetched).

| Item | Date | Correspondents | Description (verbatim) | Decipher noted |
|---|---|---|---|---|
| SP 81/37/284 (C7774544) | [? 1631] | Mr Stanning; recipient not stated | Duplicate of paper sent by Mr. Stanning in cipher. | no |
| SP 81/38/76 (C7774576) | 1632 Feb. 20 | Vane to --- | Vane to --- - decipher. | yes |
| SP 81/38/206 (C7774637) | 1632 May 22 | Vane to --- | Vane to ---, and decipher. | yes |
| SP 81/38/250 (C7774653) | 1632 June 13/23 | Vane to Secretary of State | ... duplicate of despatch of 6/16 and extracts in cipher. | no |
| SP 81/39/88 (C7774705) | 1632 Sept. 6 | Vane to Coke | Vane to Coke - decipher, and duplicate. | yes |
| SP 81/39/402 (C7774813) | [? 1632] | not stated | 2 sheets of cipher [? fragments]. | no |

**Result.** All six details records have an empty `note` field, no extent or physical description, `digitised: false`, and
no key noted. The details record adds nothing beyond the search description. **No record gives a cipher length**, so the pool's
total cipher length is not known from the catalogue. Whether it reaches the pool-first threshold (2,000 signs) can only be
measured from images. What the catalogue does establish: one sender (Vane) and one office (the Secretaries of State,
Dorchester then Coke) over Oct 1631 to Sept 1632, with six items carrying a contemporary decipher (ff.37/93, 37/169, 37/216,
38/76, 38/206, 39/88; f.216 partial) and two more carrying cipher only (38/250 extracts, 39/402 two sheets). Whether
Stanning's paper uses Vane's cipher is still unknown. The only link is that it was filed in Vane's piece. A key family is
also not shown, since the Secretary changed (Dorchester died Feb 1632, Coke followed) and the cipher may have changed with
him. Rule 10: a catalogue search result, not a reading.

Requests: discovery.nationalarchives.gov.uk 10 (2 search, 6 details, 2 children counts); one at a time, 1.7 s apart, all
HTTP 200.

## While waiting (3 Oct 2026, GAPS143)

- Pool-first input is in `sibling_pool.tsv`. The next step depends on the owner: the copy order in REQUEST.md, now with
  the 1632 pool as a second tier. Nothing else in the catalogue route stays cheap. The remaining step that depends on nobody
  is a full `tools/discovery_items.py --notes C5910245` / `C5910246` sweep (about 272 requests, over two sessions at <=150
  per host, about USD 1-2) to catch 1632 items noted "in cipher" only in the `note` field. It is low-yield, because all six
  details records checked here had an empty `note`. Next: that sweep, ~$1.5, only if a cheaper step is not on the board.
