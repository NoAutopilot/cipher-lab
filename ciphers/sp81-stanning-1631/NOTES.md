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

## While waiting (3 Oct 2026, GAPS134)

- TNA Discovery API item-level search of SP 75 (Denmark), SP 82 (Hamburg) and SP 95 (Sweden), 1631-32, for "cipher" /
  "decipher" / "duplicate", to list any other cipher papers of the 1631-32 mission circuit (e.g. the Hamburg agent's)
  that might share f.284's system. Positive control: the same query on SP 81/37 must return ff.93/169/216. No vision,
  about USD 1. This depends on nobody. (The HMC Hamilton and Cowper routes to identifying Stanning are done: GAPS130,
  GAPS134. Reading the item still waits on the copy order, REQUEST.md.)
