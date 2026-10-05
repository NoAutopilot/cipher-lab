open
CSP Domestic Charles I 1637-38 (Bruce, IA `sim_great-britain-public-record-1625-1649-domestic-series_1637-1638`), *Calendar of the Clarendon State Papers* vol. 1 (IA `calendarofclaren01bodluoft`, Windebank's papers) and HMC Cowper vol. 2 (IA `manuscriptsofear02grea_1`, Coke's papers), each grepped whole by this worker 3 Oct 2026 for Roe, Hamburg and 15/25 July 1638 and read at the July 1638 entries (CSPD pp. 559-575; Cal. Clar. pp. 157-174; HMC Cowper ii pp. 187-190): no Roe-to-Secretary letter of 15/25 July 1638 is calendared; Cal. Clar. vol. 1 p. 215, no. 1486 item 14, lists 'Sir Thos. Roe's cypher. End. by Windebank.' (a period key, not a reading of this letter).

# Sir Thomas Roe to the Secretary of State, postscript in cipher — TNA SP 81/44/225

QUEUE row: N58 (sources/solver-diffs/2026-09-23-non-decode-hits.tsv, "Candidates not on DECODE").

## Source

The National Archives, Kew, **SP 81/44/225** (State Papers Foreign, German States), folio 225, 1638 July
15/25 (TNA Discovery, fetched 24 Sept 2026, id C7775394; `digitised: false` confirmed by direct record
fetch; no separate `note` field beyond the description text below): "Folio 225: Roe to Secretary of State,
with postscript in cipher." Sir Thomas Roe was Ambassador-Extraordinary to the Hamburg peace conference
(and afterwards Regensburg/Vienna) 1638-1640/42; the addressee "Secretary of State" is unnamed in the
catalogue snippet — both Sir John Coke and Sir Francis Windebank held the office jointly through this period
(Coke resigned 1640), and both appear as named correspondents elsewhere in this same piece (see below).

## Check-solved sweep (24 September 2026)

1. **Editions.** The only printed edition of Roe's negotiations/correspondence, Samuel Richardson (ed.),
   *The Negotiations of Sir Thomas Roe, in his Embassy to the Ottoman Porte, from the Year 1621 to 1628
   Inclusive* (1740, archive.org `bim_eighteenth-century_the-negotiations-of-sir-_roe-sir-thomas_1740`),
   covers by its own title and preface ("We here present to the publick the first volume... no more
   published") **only 1621-1628**, Roe's earlier Ottoman embassy — a hard exclusion by date, sixteen years
   before this 1638 item, not a search failure. WebSearch (`Sir Thomas Roe Hamburg 1638 1640 correspondence
   printed edition Negotiations Secretary Windebank Coke`) confirms no printed edition reaches the Hamburg
   period: Roe's manuscript letter-books for the 1638-42 Hamburg/Regensburg/Vienna negotiations were
   collected by Thomas Birch and bequeathed to the British Museum as five folio volumes, now BL Additional
   MSS (`Add MS 4168-4172` per the British Library's own catalogue, surfaced in this search) — unprinted, and
   BL is out of scope for this lane's hosts (also offline since the 2023 cyber attack per LESSONS.md). One
   modern printed edition touches this exact window from the other side: Nadine Akkerman's edition of the
   correspondence of Elizabeth Stuart, Queen of Bohemia (Oxford Scholarly Editions Online) includes letter
   402, "Roe [in Hamburg] to Elizabeth [in The Hague], 21 September 1638" — a different addressee (Elizabeth,
   not the Secretary of State) and a different date (21 Sept, not 15/25 July), so not our item, but it
   confirms Roe's Hamburg-period letters are printed at least in part in a modern scholarly edition covering
   this exact mission; that edition is paywalled (Oxford Scholarly Editions Online) and was not read past its
   search snippet this pass — a caveat, not a clearance, and worth a full check by whichever future worker
   holds an OSEO/library-proxy route (none available under this run's hosts).
2. **Sibling search (TNA Discovery, same piece) — a key/decipher lead.** `tools/discovery_items.py "SP 81"
   "SP 81/44" cypher decipher key postscript` found, in the same piece, **SP 81/44/88** (id C7775340, 1638
   May 30): "Folio 88: **Coke to Roe, with decipher and copy.**" This is Secretary John Coke writing *to*
   Roe two and a half months before the target, enclosing a decipher and a copy — direct evidence that this
   exact correspondence channel (Secretary of State <-> Roe at Hamburg) used a standing cipher for which TNA
   holds at least one contemporary decipherment, in the same piece as the target. A follow-up query for all
   "Roe" items in the piece (`tools/discovery_items.py "SP 81" "SP 81/44" Roe`) lists the surrounding
   correspondence (Oxenstierna, the Palatine, Scudamore, Boswell, Windebank, Leicester, all to/from Roe,
   June-August 1638) but found **no description explicitly naming a decipher of the 225 postscript itself**
   — f.88's decipher is dated 6-7 weeks before f.225 and most plausibly answers an earlier Roe cipher, not
   this one, though the two are not dated close enough to link by inspection alone and this was not resolved
   by reading either folio's image (neither is online). This is a genuine sibling-key lead, in the sense of
   LESSONS.md's "look for the sibling" section, worth flagging to whoever next holds an image or copy of the
   piece, not a confirmed key for this specific postscript.
3. **Community lists.** Web search (`Sir Thomas Roe 1638 "Secretary of State" postscript cipher SP 81/44
   Germany`) returned only general Roe biographical pages (DNB, History of Parliament, SSNE database,
   Wikipedia) and the EHR article title "Mission of Sir Thomas Roe to the Conference at Hamburg, 1638-40"
   (Oxford Academic, abstract only, paywalled — not read this pass, no JSTOR/library-proxy access under
   this run's hosts) — none names this item or a prior transcription/solve attempt. No Cryptiana or
   Cipherbrain hit; local grep of `sources/cryptiana/` for "roe"/"hamburg"/"SP 81/44": no hits.
4. **DECODE.** No login attempted. `sources/decode/` greped for "Roe"/"Hamburg"/"SP 81/44"/"Coke": no hits.
5. **Solver repositories.** Both freshly shallow-cloned (24 Sept 2026, shared across this run's four
   targets). `dbourdeau/cyphersolver` and `aaymeloglu/unsolved-ciphers`: grep for "roe.*163[0-9]|SP 81/44"
   across both trees returns zero matches naming this item or Roe's 1638 Hamburg mission (Bourdeau's tree
   has no Roe target at all, per this grep).
6. **General web search.** As (1) and (3). No result ties a decipherment, key, or prior reading to SP
   81/44/225 specifically.

**Host requests this pass:** discovery.nationalarchives.gov.uk 5 (piece search + item search + record-detail
fetch, >=3s apart, shared across all four targets this run), WebSearch 2, github.com 1 shallow clone each of
both repos (grepped, shared across all four targets), sources/decode/ and sources/cryptiana/ local greps (no
network).

## Verdict

**Status: open.** The only printed edition of Roe's correspondence (Richardson 1740) is a hard date exclusion
(1621-28 vs. 1638); Roe's actual Hamburg-period letter-books are unpublished BL manuscripts, out of this
lane's scope; a modern scholarly edition (Akkerman, Elizabeth of Bohemia's correspondence) touches this exact
mission but for a different addressee and was not read past its search snippet (a real caveat, flagged for a
future worker with library access). No community list, DECODE record, or solver-repository entry names this
item. The strongest finding this pass is not a clearance but a **lead**: SP 81/44/88, "Coke to Roe, with
decipher and copy," in the same piece, six-odd weeks earlier, confirms a standing Secretary-of-State/Roe
cipher existed and that TNA holds at least one contemporary decipherment for this channel — worth ordering
alongside the target (see REQUEST.md) rather than treating this as ciphertext-only from the start.

**Copy status:** no online image located (confirmed `digitised: false`); **copy-order**. See REQUEST.md.

## While waiting (27 Sept 2026, WAIT-PASS-B)

Waits on: a TNA page-copy order for SP 81/44/225 alongside the candidate key sibling f.88 (REQUEST.md).

- S: search SP 81/44's already-listed June-August 1638 items (Oxenstierna, Palatine, Scudamore, Boswell, Windebank, Leicester) for a decipher/key description closer in date to f.225 than f.88's 30 May.
- S: fetch f.88's full record detail (note field) individually -- only its description text has been checked so far.
- S: search OpenAlex/CORE_API_KEY (now set) for a free green-OA copy of the EHR article 'Mission of Sir Thomas Roe to the Conference at Hamburg, 1638-40', not tried with the newer keys.

## Web and blog check (GF4-BATCH7 (account-4), 3 Oct 2026)

Plain web searches (WebSearch): (1) `"Swyfte" Lockhart 1657 ...` and (3) `1642 1644 English cipher letter France State
Papers Foreign deciphered` (run for the sibling SP batch; no Roe hit); (2) site-restricted to the three blogs, `Thomas Roe
1638 cipher letter Hamburg` -- **Cipherbrain** (scienceblogs.de/klausis-krypto-kolumne: Louis XIV letter, Ferdinand III
posts, a 1783 letter, a WWII item), **Cipher Mysteries** (ciphermysteries.com page 8, Beale, fifteenth-century
cryptography), **Cryptiana blog** (cryptiana.blogspot.com / Tomokiyo's cryptiana.web.fc2.com: no Roe hit); (3) an earlier
query with the three blogs named in `site:` form returned general Roe biography (Wikipedia "Thomas Roe") and nothing on
this item; (4) `Sir Thomas Roe 1638 "Secretary of State" postscript cipher SP 81/44 Germany` (24 Sept 2026, item 3 above).
No hit names SP 81/44/225 or a reading of Roe's 1638 cipher, so no comment thread to read. Solver repositories re-cloned
shallow 3 Oct 2026 and grepped (`SP ?81/4[0-9]`, `Thomas Roe`): no Roe target in either; the only `Roe` hits are unrelated
words in other targets' source texts.

## Premise check (GF4-BATCH7 (account-4), 3 Oct 2026)

(a) Folder's own mentions of a decipherment: **found, not this item** -- SP 81/44/88 (30 May 1638) "Coke to Roe, with
decipher and copy" is a decipherment of a different letter six weeks earlier, same channel; Discovery `digitised: false`,
so not opened. New this pass, a period key for the channel: *Calendar of the Clarendon State Papers* vol. 1 p. 215,
no. 1486, "Keys to various Cyphers, principally those used by the Ambassadors resident abroad", item 14 "Sir Thos.
Roe's cypher. End. by Windebank." (Bodleian, Clarendon State Papers; the calendar gives no folio). If f.225's addressee
is Windebank, this is the key family to apply; it is a key source, not a reading -- the item stays `open`. (b) Other
solvers' working files: **not found** (no Roe folder in Bourdeau's or Aymeloglu's repository). (c) Physical neighbours:
**unreachable** -- f.225 and its neighbours are `digitised: false` (Discovery C7775394); the piece's term-sweep (24 Sept)
found no decipher item adjacent to f.225. (d) Recipient side: **not found** -- both possible recipients' papers were read
in print: Windebank's (Cal. Clar. vol. 1, July-Aug 1638 entries pp. 157-174, Roe appears only in third-party newsletters
and the agents' address list no. 1165) and Coke's (HMC Cowper vol. 2 pp. 187-190, July 1638, no Roe letter); CSP Domestic
1637-38 likewise (Roe in 19 entries, none this letter).

## While waiting (3 Oct 2026, GF4-BATCH7)

Waits on: the TNA page copy of SP 81/44/225 (REQUEST.md; consolidated TNA batch).

- S: [done 3 Oct 2026, FT4-sp81-roe-1638 -> LOCAL-QUEUE L40] find the Bodleian catalogue record for the Clarendon State Papers volume holding Cal. Clar. no. 1486 (keys, item 14 "Sir Thos. Roe's cypher") and quote its availability flag (tools/data/catalogue_ladders.tsv), ~$1.
- S: fetch SP 81/44/88's full Discovery record detail (note field) to see whether its "decipher" names the cipher used.

Requests this pass (shared with the sibling targets where noted): archive.org 6 (advancedsearch 3, djvu.txt 3), github.com
2 shallow clones (shared), WebSearch 2 for this target.

## FT4-sp81-roe-1638 (3 Oct 2026, account-4)

Step: the Clarendon key lead (Cal. Clar. i no. 1486 item 14). Results:

1. **Calendar entry pinned.** IA `calendarofclaren01bodluoft` djvu text, pp. 214-215: no. 1486 "Keys to various Cyphers,
   principally those used by the Ambassadors resident abroad", 20 items, placed among the calendar's undated papers at
   the end of 1640 (between no. 1485 and the 1 Jan 1640/1 entry no. 1487). Siblings in the same bundle: Boswell 30 July
   1632, Aston, Leander 1640, Hopton (one endorsed Oct. 1638), Curtius, Morton (Turin) 1635, Welford, Taylor, Avery
   (received 28 June 1638), Gerbier, Leicester (sent 26 Oct 1637), Lord Deputy, Hamilton, **14 "Sir Thos. Roe's cypher.
   End. by Windebank."**, Oliver Fleming, Fielding, Dawson, Elson, Hatton, five anonymous. The calendar prints no
   volume or folio. Volume: **not established**. MS. Clarendon 19 is a composite volume Sept 1640 - Jan 1640/1, 284
   leaves (web-search summary of the CELM/Bodleian description), so it is the likely home of an end-of-1640 undated
   bundle -- an inference from the calendar's order, not read in any catalogue.
2. **Availability.** Digital Bodleian JSON search (`/search/?q=...&format=json`, Accept: application/json): "Clarendon"
   52 objects, the only MS. Clarendon objects MS. Clarendon 128 and 155; "MS. Clarendon 19" 3 objects (all MS. Abinger);
   "cypher Windebank" 0; "cipher keys Clarendon" 2 (MS. Abinger e. 32, Arch. G c.7). A search result, not a
   digitisation verdict. The holding record (archives.bodleian.ox.ac.uk) answered the cloud with the Anubis bot page
   ("Making sure you're not a bot!"), one request, not retried -> **LOCAL-QUEUE L40** (catalogue-record row, quotes
   tools/key_livecheck.py 03:03 UTC: no credential applies to this host). Bodleian archives blog "Secret ciphers"
   (2 Aug 2021) is about the 1746 Villiers papers (Clarendon 2nd creation), not this bundle.
3. **DECODE (login-free).** On-disk key harvest (`sources/decode/keys-all-2026-09-28-merged.tsv` + `keys-na-*`,
   9,828 rows) grepped for Roe/Windebank/Clarendon/Hamburg/Coke/Boswell: no Roe key. All London/Kew/Oxford keys dated
   1628-1645 listed (26); record views opened for 8734, 9114, 370, 373, 7596, 414, 416, 418, 419. 8734 (BL Add MS 72438
   ff.144-145, 1638, homophonic + nomenclator) has origin city Constantinople, no correspondent -- 1638 Constantinople
   is not Roe's post (he left in 1628); 370 is Hopton's (and Anstruther's), 373 Aston's 1635, 414 Carleton's;
   416/418/419 (TNA SP 106/5, 1625-49) name no correspondent -- unnamed Charles I keys, not excluded as Roe's, not
   identified. Oxford holds no DECODE key record in this range.
4. **Solver repositories** (shallow clones 3 Oct 2026): Aymeloglu: no Roe hit. Bourdeau: no Roe target; his `hyde`
   target searched the Deciphering Branch key volume BL Add MS 32256 (DECODE R9113-R9219) by correspondent and opened
   every 1630-50 key -- R9115 is Windebank's 1640 cipher (an 18th-century reconstruction), none is Roe's.
5. **design_prior.py: does not apply** -- no ciphertext on disk (f.225 undigitised), and it predicts from sign
   statistics. KEY-DESIGN.tsv / KEY-OFFICES.tsv carry no 1630s English Secretary-of-State key. The nearest office
   evidence is DECODE's own description of two sibling Charles I keys of the same bundle's correspondents: 370 (Hopton,
   Spain 1630s) "homophonic substitution ... with nulls and a nomenclature ... over 400 codegroups ... numerals only",
   373 (Aston 1635) "roughly 700 codegroups", vowels 8 homophones. A Roe key of 1638 from Windebank's office is
   therefore expected to be a numeric homophonic nomenclator of a few hundred groups -- a prior, not an observation;
   if f.225's postscript is in numerals, this family fits; a key test needs both the key leaf and the ciphertext.

No image of the key is online that this pass could find; nothing fetched. Requests: archive.org 1 (djvu.txt),
digital.bodleian.ox.ac.uk 9 (2 HTML, 7 JSON), archives.bodleian.ox.ac.uk 1 (Anubis), blogs.bodleian.ox.ac.uk 1,
de-crypt.org 9 (RecordsView, no login), github.com 2 shallow clones, WebSearch 2. All >= 1.5 s apart per host.

## Remaining gaps (FT4-sp81-roe-1638, 3 Oct 2026)
Read so far: 0 tokens (no ciphertext on disk; f.225 is digitised: false)
- ciphertext of SP 81/44/225 postscript - blocker: waiting-on ASKS row 106 (TNA page copy); Discovery C7775394 digitised: false, REQUEST.md
- Roe's cypher key leaf (Cal. Clar. i no.1486 item 14) - blocker: waiting-on LOCAL-QUEUE L40; the Bodleian holding record is Anubis-challenged from the cloud and Digital Bodleian shows no MS. Clarendon 19 object (FT4 section above)
- SP 81/44/88 decipher (Coke to Roe, 30 May 1638) - blocker: waiting-on ASKS row 106 (TNA page copy); Discovery C7775340 digitised: false

## Escalation (3 Oct 2026)
- [x] siblings: SP 81/44 piece swept 24 Sept (f.88 decipher lead); DECODE 1628-45 English keys opened 3 Oct, none Roe's
- [n/a] clear-pages: no page of the letter is in hand, so no clear text exists to use
- [x] known-keys: Cal. Clar. i no.1486 item 14 located; BL Add MS 32256 (Bourdeau) and DECODE swept, no Roe key
- [x] print: CSPD 1637-38, Cal. Clar. i, HMC Cowper ii read 3 Oct (GF4-BATCH7), letter not calendared
- [n/a] key-rebuild: no ciphertext on disk to rebuild a key from
- [x] image-check: Digital Bodleian searched 3 Oct (no MS. Clarendon 19 object); TNA f.225 digitised: false
- [n/a] retry: nothing was attempted that failed and could be retried
Verdict: parked: every gap has an outside blocker (ASKS row 106; LOCAL-QUEUE L40)

## While waiting (3 Oct 2026, FT4-sp81-roe-1638)

Waits on: the TNA page copy of SP 81/44/225 (REQUEST.md) and LOCAL-QUEUE L40 (Bodleian record for the Roe key).

- S: fetch SP 81/44/88's full Discovery record detail (note field) to see whether its "decipher" names the cipher used, ~$0.5.
- 5 Oct 2026 (PR-LAND-67): LOCAL-QUEUE L40 answer landed, local-runner/L40-2026-10-05.md -- Calendar vol. i no. 1486 lies in MS. Clarendon 19 (ark:29072/x0bk128b21xs, "NOT AVAILABLE ONLINE"); catalogued at volume level only, so the Roe cypher's folio is not online.

## Bodleian reply, 5 Oct 2026 17:06 UTC (Mike Webb; logged 5 Oct 2026 18:33 UTC)

The key listed in Cal. Clar. S.P. I p.215, no.1486 item 14 ("Sir Thos. Roe's cypher") should be in **MS. Clarendon 19** (calendar
nos. 1415-1500; https://archives.bodleian.ox.ac.uk/repositories/2/archival_objects/172431). He has called the volume up and offers to
check whether it is there. Reply draft (yes please; quote if found) placed in Gmail for the owner.
