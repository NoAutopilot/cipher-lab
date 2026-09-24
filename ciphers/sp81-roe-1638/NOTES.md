open

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
