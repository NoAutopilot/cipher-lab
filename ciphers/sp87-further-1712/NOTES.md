open
Graham's *Annals and Correspondence of ... the Earls of Stair* (1875) vol.1 and vol.2 both read and grepped in full by this worker (archive.org djvu, `annalscorrespond01grahiala`/`02grahuoft`): vol.1 ends at p.403 (Second Earl, Chapter VIII, no 1742 material at all) and vol.2 has zero hits on the May 1742 Hyndford/Stair/Villiers letters; TNA Discovery item-details for all 13 items across the 8 pieces confirm `digitised: false`, re-fetched by this worker today.

## Check-solved (LANE CX2, 25 Sept 2026)

Six-source sweep per .claude/briefs/check-solved.md, worker CX2-SP87A. This target folds 13 items across 8 pieces (SP 87/4, 8, 16, 17, 21, 30, 32, 45); prior passes (24 Sept, LANE S) already ran editions, community lists, DECODE, Bourdeau, Aymeloglu and Google Books (7 queries) — this pass re-runs all six source families fresh rather than re-citing, and closes the one edition gap the 24 Sept notes flagged as incomplete (Graham vol.1).

1. **Web search.** Three queries today: `"SP 87/8" Hyndford Stair 1742 cipher solved OR "Namur" 1712 intercepted letters cipher Utrecht plenipotentiaries`, `Harrington Cumberland Fawkener Ligonier 1745 cipher SP 87 solved`, `Clavering Halifax Holdernesse Granby SP 87 cipher 1758 1760 1762 solved`, plus a fourth targeted `"Namur" 1712 intercepted letters cipher solved OR "SP 87/4/234" plenipotentiaries Utrecht`. All four surface only TNA Discovery's own catalogue text for these items (confirming, not adding to, what is already in this file) and general background on the 1712 Blencowe/d'Alonne/Jaupain interception apparatus already noted below — no item-specific solve, no model-solve announcement, no scholarly citation naming SP 87/4/234, SP 87/8/45,51,59, or any of the 1745-63 items in this cluster.
2. **Standard edition/calendar, read by this worker.**
   a. TNA Discovery item-details fetched today for all 13 items (ids C8951001, C9232930, C9232936, C9232944, C9189257, C9189258, C9233504, C9233568, C9067846, C9122843, C9147558, C9394295, C9433647): **`digitised: false` for all 13**, closing the "copy status not determined" gap the 24 Sept pass left open.
   b. **Graham, *Annals and Correspondence of the Viscount and the First and Second Earls of Stair* (1875).** 24 Sept checked vol.2 in full (negative) but left vol.1 only spot-probed. This pass downloaded and grepped vol.1 in full (`annalscorrespond01grahiala_djvu.txt`, 806 KB): the volume runs only to p.403 ("Second Earl of Stair — Chapter VIII") with **zero** occurrences of "1742" anywhere in the text — the volume's own content ends well before the year of SP 87/8/45,51,59, confirming (not just presuming) it cannot contain them. Combined with 24 Sept's vol.2 result (zero hits on Hyndford/Villiers/1742 content), **Graham's edition is now fully read and closed as a negative for the SP 87/8 Hyndford/Villiers items** — the "high" edition risk the original QUEUE row flagged is resolved, not merely narrowed.
   c. **New this pass, Google Books full-text search** (key+country=US) beyond the 24 Sept sweep's 7 queries: `"SP 87/8" Hyndford Stair 1742` and `"Namur" 1712 intercepted letters cipher Utrecht plenipotentiaries` returned no on-topic hits (background cipher-history and unrelated modern pages only, per the web-search results above).
3. **Community lists.** `sources/cryptiana/` regrepped today for "Hyndford", "Namur", "Harrington", "Clavering", "Holdernesse", "Boyd": the only "Namur" hits are two unrelated 16th-century items (`mary.htm` SP53/14 no.89, 1584; `spanish3.htm`, Don Juan of Austria's 1577 siege of Namur) — different series, different century, already ruled out 24 Sept, reconfirmed today.
4. **DECODE.** `sources/decode/` TSVs (fetched 24 Sept 2026) regrepped today for "Hyndford", "Namur", "Harrington", "Clavering", "Holdernesse", "Boyd", "Granby", "Halifax", "Villiers", "Stair", "Ligonier", "Fawkener": no record for any term.
5. **Bourdeau.** Fresh shallow clone of `github.com/dbourdeau/cyphersolver` (25 Sept 2026) grepped for all 13 items' correspondent names and shelfmarks: no target folder or catalogue row matches; no "SP 87" hit anywhere in `CATALOGUE.md`/`catalogue.json`.
6. **Aymeloglu.** Fresh shallow clone of `github.com/aaymeloglu/unsolved-ciphers` (25 Sept 2026): 8 targets total, none matching any correspondent or shelfmark in this cluster.

**Sibling decipherment re-check.** TNA Discovery class-wide phrase search for "deciphered" restricted to record series "SP 87" re-run today: 8 hits total (SP 87/2/70, 5/62, 40/121, 40/77, 24/35, 36/13, **32/45**, 40/76). One of these, **SP 87/32/45**, falls in the same piece as our SP 87/32/115 (Holdernesse-Granby); fetched its full description: "Holdernesse to Lieutenant Colonel Browne: as the correspondence for which he received two ciphers and deciphers has been terminated by the death of the duke of Marlborough, he is to deliver them to Lord George Sackville" (7 Nov 1758) — an administrative note about returning cipher tables after Marlborough's death, a different correspondent (Browne, not Granby) and a different date (Nov 1758 vs Aug 1760), **not a sibling decipherment** of SP 87/32/115. No other of the 8 hits falls in pieces 4, 8, 16, 17, 21, 30 or 45 either — confirmed no sibling decipherment exists anywhere in this cluster's 8 pieces.

**Verdict: open (stage 2 verified unsolved), upgraded from 24 Sept's "stage-2 candidate" pass.** All three gaps the 24 Sept notes left open are now closed: Graham's edition fully read (vol.1 and vol.2, both negative), TNA digitised flags fetched for all 13 items (all `false`, no online route), and a fresh six-source sweep today (web, community lists, DECODE, both solver repos, Google Books) found no solve, no key, and no sibling decipherment for any item in the cluster. The 1712 Namur item (SP 87/4/234) remains the one item sitting in a *documented* but not *item-specific* interception milieu (Jaupain/d'Alonne/Blencowe successfully broke other 1712 traffic, per Wikipedia's Blencowe article, re-surfaced in today's web search) — background, not a hit. De Leeuw's Black Chamber scholarship (a non-OCR'd scanned PDF) remains unreached; not pursued this pass (out of brief scope: no OCR tooling named). Not "new"; not "unpublished" — a search result, not a discovery (rule 10).

**Requests today (25 Sept 2026):** discovery.nationalarchives.gov.uk 16 (13 item-details re-fetches + 1 class-wide "deciphered" search + shelfmark searches to resolve each item's C-id where not already on file, all >=1.6s apart); archive.org 1 (Graham vol.1 djvu, freshly fetched; vol.2 already on disk from 24 Sept, re-read not re-fetched); googleapis.com/books 2 (key+country=US); github.com 2 (git-protocol shallow clones). WebSearch: 4 queries. No logins, no credentials printed.

---

# SP 87 class, further pieces beyond N6's scored cluster — TNA SP 87/4, 8, 16, 17, 21, 30, 32, 45

QUEUE row: N28 (sources/solver-diffs/2026-09-23-non-decode-hits.tsv, "Candidates not on DECODE").

## Source

The National Archives, Kew, State Papers Foreign, Military Expeditions, SP 87. Thirteen items across eight
pieces, none inside N6's already-scored SP 87/36,38-40,42-44 (1759-62; see ciphers/sp87-brunswick-1759):

- **SP 87/4/234** (1712, whole year): "Series of intercepted letters from Namur, partly in cipher, concerning
  the French plenipotentiaries to the [Utrecht negotiations]."
- **SP 87/8/45** (30 Apr 1742): Earl of Hyndford to Stair, mediation between Maria Theresa and the king of
  Prussia.
- **SP 87/8/51** (5 May 1742): Lord Hyndford to Stair, perfidy of the king of Prussia.
- **SP 87/8/59** (13 May 1742): Thomas Villiers to Stair, on relations between Prussia, France and Saxony.
- **SP 87/16/12** (23 Jan 1745): duplicate of SP 87/16/10, Ostend.
- **SP 87/16/13** (21 Jan 1745): duplicate of SP 87/16/11, Maubeuge and Cambrai.
- **SP 87/17/58** (17 Jun 1745): Harrington to Cumberland.
- **SP 87/17/122** (4 Aug 1745): Harrington to Fawkener.
- **SP 87/21/45** (3 Oct 1746): Harrington to Ligonier, enclosing a list of officers (SP 87/21/46).
- **SP 87/30/4** (23 Feb 1758): Boyd to Holdernesse, quoting a captured French courier's letter (fuller TNA
  text found this pass: "reinforcements to Louisburg... surrender of Rotenburg, abandonment of Ottersberg and
  Verden, capture of Hoya... headquarters at Hudemühlen").
- **SP 87/32/115** (26 Aug 1760): Holdernesse to Granby.
- **SP 87/45/36** (12 Nov 1762): Clavering to Halifax.
- **SP 87/45/92** (31 May 1763): Halifax to Clavering.

All at The National Archives, Kew.

## Check-solved sweep (24 September 2026) — editions and community-list pass

A Sonnet subagent under this worker's $10 cap ran editions and community-list checks (not a full six-source
check-solved sweep with a TNA sibling-decipherment search — the TNA Discovery API was not called this pass,
per this run's host rules). Reused rather than re-derived: the "already checked" findings in
ciphers/sp87-brunswick-1759/NOTES.md (N6), ciphers/sp87-chesterfield-1747/NOTES.md (N15) and
ciphers/sp87-newcastle-1743/NOTES.md (N14) for the same correspondent networks.

1. **Graham 1875, *Annals and Correspondence of the ... Earls of Stair*** — the item flagging "high" edition
   risk for SP 87/8. Internet Archive has full public-domain scans of both volumes (`annalscorrespond01grahiala`,
   `annalscorrespond02grahuoft`, plus several `*grahgoog` copies). Vol. 2 (`annalscorrespond02grahuoft`) covers
   the 2nd Earl's later career including 1742; its full djvu text was downloaded and grepped directly (not
   relying on the be-api's unreliable `page_num` field):
   - "Hyndford" occurs 3 times, all genealogical/index entries, never in a letter body, never near 1742.
   - "Villiers", "Breslau", "Maria Theresa", "Dresden": zero hits anywhere in vol. 2.
   - "cypher"/"cipher": exactly one hit in the whole volume — "...by the means of Jeffereys he has endeavoured
     to make us break off with the king of Prussia by strange representations (all in cypher)..." (p.407,
     headed "Second Earl of Stair — Chaps. XIV and XV" but internally dated **Whitehall, Dec. 28, 1719** — a
     different Prussia episode 23 years before our items, source cited there as "Stair Papers, vol. xix, B").
     The other "decipher" hit (p.279) is a figurative use in an unrelated 1741 letter.
   - The 1742 material vol. 2 does print (pp.280-290ish) is Stair's own military correspondence with Ligonier
     in Flanders, a different thread from the Hyndford-to-Stair diplomatic mediation letters (SP 87/8/45,
     51, 59).
   - Vol. 1 not fully downloaded, only two targeted fts probes run (Hyndford: 1 index-only hit; "1742": 0
     hits), consistent with vol. 1 predating 1742.
   - **Conclusion: Graham's edition, checked exhaustively for vol. 2, does not print the May 1742
     Hyndford-Stair-Villiers letters and contains no cipher passage tied to 1742.** This narrows, but (given
     vol. 1's incomplete check) does not fully close, the "high" edition risk the QUEUE row flagged.
2. **Harrington-Cumberland/Fawkener/Ligonier (87/16,17,21, 1745-46).** No dedicated printed edition of
   Cumberland's 1745-46 correspondence found by search; the Royal Archives "Cumberland Papers" (Windsor, a
   different repository) and Nottingham University's "1745 Rebellion" teaching transcripts exist but are not
   confirmed to include SP 87 material and are not full-text searchable. Not checked against archive.org full
   text this pass (budget) — flagged unreached, not negative.
3. **Boyd-Holdernesse (87/30/4) and Holdernesse/Halifax-Clavering (87/32/115, 45/36, 45/92).** Per N6's own
   notes, Westphalen (only vol. 1 on archive.org, predates 1760-62) and Savory (0 archive.org hits) remain
   open gaps for this correspondent network; our items add Granby and Halifax as correspondents (not in N6's
   set) and Boyd is an earlier (1758), separate correspondent. No edition or community hit found for any of
   Boyd, Granby or Halifax in a cipher context.
4. **Namur 1712 intercepts (SP 87/4/234).** The same interception apparatus (Jaupain in Brussels, deciphered
   by Abel Tassin d'Alonne and William Blencowe) is documented as active and successful against other 1712
   traffic in the run-up to Utrecht (Malknecht-van Putten correspondence, per Karel de Leeuw's scholarship and
   Wikipedia's Blencowe/d'Alonne articles) — but no source names Namur specifically or the "French
   plenipotentiaries" traffic this item describes. Tomokiyo's own page `sources/cryptiana/web/blencowe2.htm`
   covers exactly this milieu (BL Add MS 32256, Utrecht-adjacent ciphers c.1712-14, Raby/Strafford, St
   John/Bolingbroke) but has zero hits for "Namur" or "SP 87" anywhere in the file — background confirming
   Tomokiyo has researched the period, not a hit on this item. A de Leeuw academic PDF (pure.uva.nl, "The
   Black Chamber in the Dutch Republic during the War of the Spanish Succession") is a scanned, non-OCR'd
   image and could not be searched — an unreached lead, not a negative.
5. **Community lists.** Recursive grep of `sources/cryptiana/web/` and `blog/` for "SP 87", "Stair",
   "Harrington", "Clavering": zero hits. "Namur" hits only in `mary.htm` and `spanish3.htm`, both 16th-century
   (1577-84, SP 53, Don Juan of Austria/Governor of Namur) — unrelated era and series, ruled out.
6. **DECODE (de-crypt.org).** Public/cached only, no login attempted.
   `unsolved-ciphers/catalogue/decode-catalog.csv` grepped for all correspondent names and shelfmarks: the
   only hits are five unrelated "Edward Villiers, Earl of Jersey (1656-1711)" records (Yale Beinecke,
   1699-1700 — a different Villiers, different institution/period from our Thomas Villiers, SP 87/8/59). No
   DECODE record for any of the 13 items or their correspondents.
7. **Solver repositories.** Both already cloned locally. No on-topic match in either for SP 87, Hyndford,
   Stair, Harrington, Clavering, Holdernesse, or Namur; the only string hits were incidental (an unrelated
   "Brunswick" mention inside an already-solved Balbases-Fuenmayor item, and "Namur"/"Holdernesse"/"Harrington"
   inside unrelated source texts for other targets — confirmed by file path to be different ciphers).
   `aaymeloglu/unsolved-ciphers`: zero hits for every term searched.

**Host requests this pass:** archive.org-family (advancedsearch + be-api fts + one djvu download) 13, mostly
>=2-3s apart; WebSearch 7; WebFetch 3 (a TNA blog post — wrong item, a Wikipedia article, an unreadable
scanned PDF). No TNA Discovery API calls, no Gallica/archivesetmanuscrits fetches, no DECODE login attempt, no
fresh solver-repo clones needed.

## Verdict

**Status: open** (a stage-2 candidate, not yet "verified unsolved" — this pass covered editions and
community lists only, not a full TNA sibling-decipherment/digitised-flag sweep). No item in the cluster is
found-solved. Graham's Stair edition, checked exhaustively for vol. 2, narrows but does not eliminate the
"high" edition risk flagged for the SP 87/8 Hyndford/Villiers items (vol. 1 incompletely checked). No printed
edition, community list, DECODE record, or solver-repository entry was found for any of the 13 items or their
correspondents. The 1712 Namur item sits in a documented, successful interception milieu (Jaupain/d'Alonne/
Blencowe) but was not itself named in any source checked.

**Google Books sweep (24 September 2026, LANE S worker H, holding the Google Books slot — key+country=US, filter=full):**
7 queries run, >=2s apart. Six returned zero results: `intitle:"Cumberland" intitle:"correspondence" 1745`;
`"Harrington to Cumberland" 1745 cipher`; `"Fawkener" "Ligonier" 1745 Flanders letters`; `"Duke of Cumberland"
despatches 1745 1746 Newcastle papers calendar`; `"Namur" "intercepted" 1712 cipher plenipotentiaries`;
`intitle:correspondence Utrecht 1712 Namur intercepted`. One had a hit: `"French plenipotentiaries" Namur
1712` returned 1 volume, *The History of the Treaty of Utrecht ... The Second Edition, with Additions*
(England, 1713), snippet "...1712. and of our Reign the Eleventh... Thơ' the French Plenipotentiaries...
Namur. Charleroy and Newport, was produc'd by the Ministers of Great Britain..." — this is period diplomatic
history discussing the Namur/Charleroy/Newport towns handed over under the 1712 Utrecht armistice terms, not
a citation of SP 87/4/234 or its intercepted-letters content; no cipher/decipherment language in the snippet.
Not a hit on this item.

**Remaining gaps before a stage-2 verdict:** the Google Books queries above; a full TNA Discovery
sibling-decipherment and digitised-flag sweep (not run this pass); archive.org full-text checks for
Cumberland/Ligonier printed correspondence; OCR access to de Leeuw's Black Chamber scholarship for the Namur
item; Graham vol. 1 fully downloaded and grepped.

**Copy status:** not determined this pass (TNA Discovery API, the only route to each item's `digitised` flag,
was not called). Sibling NOTES.md files (N6, N14, N15) show `digitised: false` for comparable SP 87 items of
this class/period — plausible but unverified per item here.

Not "new"; not "unpublished" — a search result, not a discovery (rule 10). QUEUE.md's own next-step note said
to fold this into N6's campaign rather than open separately; this folder exists per this run's brief
(slug `sp87-further-1712`), and a future orchestrator pass may want to merge it into N6's when N6 is
re-scored as a multi-session campaign.

## Check-solved addendum (GF4-BATCH12 (account-4), 3 Oct 2026)

Standard edition and pages actually read: line 2 stands for the SP 87/8 Stair items (Graham, *Annals and Correspondence of
the Earls of Stair*, 1875, vols 1-2 read and grepped in full, LANE CX2 25 Sept 2026). Added this pass, for the recipient's
side of **SP 87/32/115** (Holdernesse to Granby, 26 Aug 1760): HMC *The Manuscripts of His Grace the Duke of Rutland,
preserved at Belvoir Castle*, vol. 2 (1889; archive.org `manuscriptshisg00unkngoog`, djvu.txt fetched and grepped
3 Oct 2026, 54,445 lines), p. 225 (OCR line 17739, between the p. 224 and p. 226 markers), calendars Granby's own received
copy: "The EARL OF HOLDERNESSE to the MARQUESS OF GRANBY. 1760, August 26. Whitehall.--Despatch, chiefly in cypher,
concluding with mention of the joyful news that the King of Prussia had gained a signal victory over General Landohn.
Signed. Refers to Prince Ferdinand's message requesting reinforcements to recomplete the British troops in Germany by the
month of September; and showing the impossibility of complying with the request. **Copy deciphered.**" So a period
clear-text copy of this despatch is at Belvoir (Rutland MSS), and its gist is in print -- a calendar summary, not the full
text, so the item is not found-solved; it is **calibration material** (a period decipherment exists) rather than an
unsolved target. The volume's other three "cypher" hits (lines 20053, 20190, 28328) are other letters, not checked against
this cluster. Also from Google Books full-text API (3 Oct 2026): Skrine, *Fontenoy and Great Britain's Share in the War of
the Austrian Succession* (1906, Q6FnAAAAMAAJ, full view) cites Harrington-to-Fawkener letters of 1745 from SP 87 by date
(Sept 20; the 4 Aug 1745 item SP 87/17/122 not seen in snippets) -- a print lead for the 1745 items, not opened. Status
unchanged: **open** for the cluster.

## Web and blog check (GF4-BATCH12 (account-4), 3 Oct 2026)

WebSearch, 3 Oct 2026: (1) `"intercepted letters from Namur" 1712 cipher French plenipotentiaries Utrecht` -- Wikipedia
(Blencowe, Jaupain, Prior, Peace of Utrecht), an archive.org d'Estrades letters volume (Nijmegen, 1710), unrelated cipher news;
the Jaupain/Blencowe pages say Jaupain copied 1712 intercepts of the Bavarian Elector's secretary (Malknecht) for d'Alonne and
Blencowe, who both decrypted them -- context, not this item. (2) `Hyndford Stair 1742 cipher letters Villiers Prussia
deciphered "SP 87/8"` -- TNA item pages (C9232935, C9232936, C9232958, C9233009: SP 87/8/51-52), the Bodleian archives blog's
cryptography tag (a 1746 letter to Villiers in Berlin revealing a British diplomatic cipher -- a different, later letter), a
Walpole-Mann 1742 letter (Yale); no decipherment of an SP 87/8 item. (3) site-restricted to **Cipherbrain** (scienceblogs.de),
**Cipher Mysteries** and **Cryptiana** (blogspot and web.fc2), `Utrecht 1712 intercepted cipher Namur OR Cumberland 1745 cipher
letters` -- only TNA catalogue pages (SP 87/4/234's fuller TNA text: "concerning the French plenipotentiaries to the
Netherlands, the choice of Utrecht for the negotiations, and the interests of the electors of Bavaria and Cologne"); no blog
post on any of the 13 items, so no comment thread to read. Not found on the open web.

## Premise check (GF4-BATCH12 (account-4), 3 Oct 2026)

(a) Folder's own mentions of a decipherment: **not found** -- NOTES.md and REQUEST.md name no decipherment of any of the 13
items (the Jaupain/d'Alonne/Blencowe milieu is context). (b) Other solvers' working files: **not found** -- fresh clones
3 Oct 2026, Aymeloglu d2800bb and Bourdeau 4aedb40, grepped for hyndford/stair/namur/cumberland/granby/"SP 87": Bourdeau's
only SP 87 item is SP 87/24/33 (del Puerto 1748, not in this cluster), Aymeloglu none. (c) Physical neighbours: **unreachable
as images** (digitised=false, LANE CX2); not re-searched by catalogue. (d) Recipient's side: **found for one item** --
SP 87/32/115's recipient copy "Copy deciphered" at Belvoir, calendared in HMC Rutland II p. 225 (above). For SP 87/4/234 the
TNA wording (Bavarian and Cologne electors' interests, 1712) matches the Malknecht intercepts that d'Alonne and Blencowe are
recorded as decrypting -- a possible period decipherment elsewhere (Blencowe's papers / BL Add MSS), **inferred, not checked**.
Other items' recipients (Stair, Cumberland, Fawkener, Ligonier, Granby, Clavering) not opened. Cluster stays **open**; SP
87/32/115 is calibration.

## While waiting (3 Oct 2026, GF4-BATCH12)

Waits on: TNA page copies (REQUEST.md, ASKS row 57).

- [done 3 Oct 2026, FT4-sp87-further-1712: neither item cited] read Skrine's *Fontenoy* (1906) for SP 87/17/58 or 17/122.
- S (refreshed 3 Oct 2026, FT4-sp87-further-1712): one DECODE browser login (`tools/decode_browser_login.js`, with
  `--guess-fullsize`) on key record 8957 (BL Add MS 32264 f.3-4, 1710) and 8763-8765 (Add MS 61575, 1711-1713, English),
  to test whether their images are served and whether any key names the French plenipotentiaries or Malknecht -- no person.

Requests this pass (3 Oct 2026): googleapis.com/books 5, archive.org 2 (advancedsearch 1, djvu 1), github.com 0 (clones
shared with sp87-brunswick-1759 above). WebSearch 3.
Gate re-run (GF4-BATCH12, 3 Oct 2026): `sp87-further-1712: open (line 1) -- edition/page or full-text-search citation found within 6 lines`, exit 0 (was exit 1: no Web and blog check section). `tools/next_steps.py --wait-only | grep sp87-further`: no line.

## FT4-sp87-further-1712 (account-4), 3 Oct 2026

Step run: the "While waiting" action above (Skrine's *Fontenoy*), plus the brief's key-availability checks. No ciphertext of
any of the 13 items is on disk (all `digitised: false`, LANE CX2 25 Sept 2026; not re-fetched), so `tools/design_prior.py`
has nothing to read and no test was run on a target. Nothing here is a reading, a negative, or a novelty claim (rules 3, 10).

1. **Skrine, *Fontenoy and Great Britain's Share in the War of the Austrian Succession* (1906)**, archive.org
   `cu31924027889686`, full djvu.txt (779,973 bytes) fetched and grepped 3 Oct 2026. "cypher|cipher|decipher": 1 hit
   (line 553, figurative "cypher in council"), none tied to a letter. Harrington letters it cites by date: to Cumberland
   June 9, June 22, July 26, Hanover August 13, October 6/8/19/20; to Fawkener September 20 (the date GF4-BATCH12 saw in
   snippets). **Neither 17 June 1745 (SP 87/17/58) nor 4 August 1745 (SP 87/17/122) is cited**, and Skrine gives no
   archive reference ("State Papers"/"Record Office" 0 hits) beyond correspondent and date. Result: no print of either
   item's text found in Skrine; a search result, not a negative on print elsewhere.
2. **Period key for SP 87/4/234 (1712), register check.** KEY-OFFICES.tsv / KEY-DESIGN.tsv: years 1700-1720 give only
   `antt-msliv0638-brochado-1712` (Portuguese) and `na-schonenberg-1678-1716` (Spanish) -- no British Secretary of State
   or Utrecht-milieu key in hand. Cached DECODE key catalogue (`sources/decode/keys-all-2026-09-28-merged.tsv`, login-free
   crawl of 28 Sept 2026; not re-crawled) filtered to BL Add MS 322xx (Blencowe/Newcastle cipher papers) and Add MS 61575
   (Blenheim) dated within 1708-1715: **11 key records** -- 8957 (Add MS 32264 f.3-4, 1710), 8761-8767 (Add MS 61575
   ff.60-75, 1711-1714, three tagged English, four French?), 8762/8768-8770 (Add MS 61575 ff.61-79, 1702-1723). All
   status N/A; DECODE full-size images are account-gated (CLAUDE.md host table; re-test per record). These are the
   candidate period keys for the 1712 Utrecht traffic; **none is in hand**, and none is known to belong to the French
   plenipotentiaries' (or Malknecht's) cipher rather than a British office's own -- an intercepted French letter would
   be read with a decipherer's reconstructed key (d'Alonne/Blencowe), which is what Add MS 32264 might hold. No
   known-key test run (brief: only if a key is in hand).
3. **TNA Discovery digitised flag:** not re-fetched; LANE CX2's 25 Sept 2026 fetch of all 13 items (`digitised: false`)
   stands.

**Planned test (pre-registered here, run when copies arrive).** Unit: SP 87/32/115 first (calibration: Granby's
"Copy deciphered" at Belvoir, HMC Rutland II p.225), then SP 87/4/234. (a) Transcribe the cipher passages
(two blind passes per TRANSCRIPTION.md). (b) Run `tools/design_prior.py` on the transcription. (c) If a candidate key
(a DECODE record above, or an SP 87 key of the Holdernesse office for 1760) is in hand: decode, statistic = share of
decoded tokens forming dictionary words of the language (en18 or fr18 corpus, era-checked per rule 3) over the
cipher spans, gate = real-key share >= the 99th percentile of 200 value-shuffled keys (same key, codes permuted;
the control varies on the statistic's own axis), and then `tools/judge_plaintext.py` on the reading plus the
same judge on the shuffled-target decode (ARM-C1). For 87/32/115 the HMC calendar gist (Ferdinand's reinforcement
request, Prussian victory over Laudon) is a C-grade crib check only on content words it names. (d) With no key:
`tools/family_run.py` with the matched control at the transcription's own N and the design design_prior names.

Requests this pass (3 Oct 2026): archive.org 2 (advancedsearch 1, djvu 1, 1.5 s apart). DECODE, TNA: 0 (cached files).

## Remaining gaps (FT4-sp87-further-1712, 3 Oct 2026)
Read so far: 0 of 13 items (no ciphertext on disk; all 13 `digitised: false`)
- all 13 SP 87 items (cipher text) - blocker: waiting-on ASKS row 57; TNA page copies per REQUEST.md, no online images (LANE CX2 digitised flags)
- SP 87/4/234 period key - blocker: no-key-material; 11 DECODE key records (BL Add MS 32264, 61575, 1702-1723) are candidates only; images ARE served after one login (IMG-DECODE1, 3 Oct 2026: R8957 P2 full size is a French code table), but nothing ties any of them to the French plenipotentiaries' or Malknecht's cipher, and there is no ciphertext on disk to test a key against
- SP 87/32/115 period decipherment - blocker: needs-physical-access; Granby's "Copy deciphered" is in the Rutland MSS at Belvoir, calendared only (HMC Rutland II p.225)

## Escalation (3 Oct 2026)
- [n/a] siblings: no sibling ciphertext of these offices on disk
- [n/a] clear-pages: no images of any item exist online
- [x] known-keys: KEY-OFFICES/KEY-DESIGN and cached DECODE key list checked 3 Oct 2026, 11 candidate records, none in hand
- [x] print: Graham vols 1-2, HMC Rutland II, Skrine Fontenoy read in full; none prints an item's text
- [n/a] key-rebuild: no ciphertext on disk to rebuild from
- [n/a] image-check: all thirteen items digitised false
- [n/a] retry: no prior test exists to retry
Verdict: parked: every gap has an outside blocker

## Second pass (CS-BATCH2 (account-2 worker), 3 Oct 2026)

Status unchanged: open (parked: every gap has an outside blocker). Fresh WebSearch for Hyndford/Stair 1742 and Namur 1712 intercepts with Blencowe/Malknecht: TNA catalogue records only (C9232913-C9233028 area, C8951001, C9188938); nothing names a decipherment, key or edition. The earlier passes' editions, DECODE key-record candidates and solver-repository greps (3 Oct 2026) were not repeated; nothing found today changes them. No Discovery notes sweep run on the eight pieces (about 2,000 items; would exceed the host budget). Requests: WebSearch 1.
Verdict: open, parked on ASKS row 57 (TNA page copies); next step (costed): `--notes` listing of SP 87/4 and SP 87/32 only (~$0.2, ~150 requests) to catch note-field decipherments, on a free request-budget slot.

## Discovery --notes listing of SP 87/4 and SP 87/32 (TNA-NOTES (account-2 worker), 3 Oct 2026)

Status unchanged: open. Command: `python3 tools/discovery_items.py --notes C3116442` (SP 87/4) and `--notes C3116470` (SP 87/32); parent ids read from the `parentId` of SP 87/4/234 (C8951001) and confirmed by the first child record of each piece (SP 87/32/1). Both listings complete: SP 87/4 = items /1-/268 (268 rows), SP 87/32 = items /1-/150 (150 rows), each row's separate `note` field fetched from the details record, 14:59-15:19 UTC. Request count, discovery.nationalarchives.gov.uk only: about 430 (268 + 150 details, 2 children listings, plus 5 by-hand calls to find the parent ids and check the children); this is above the ~150 the Verdict estimated, because SP 87/4 alone holds 268 items. No 429, 403 or challenge.

Result. The `note` field is empty on all 418 items of both pieces, so no note-field decipherment, key or "in clear" remark exists to find. Cipher word in the description (the tool's cipher flag): SP 87/4 /27, /43, /44, /47, /49, /133, /173, /234; SP 87/32 /45, /55, /62, /115. Target items: **SP 87/4/234** (Namur intercepts, ff. 645-671): description reads "partly in cipher", nothing on a decipherment, key or clear copy. **SP 87/32/115**: "partly in cipher", nothing on a decipherment (Granby's "Copy deciphered" at Belvoir stays as already recorded). Two other lines name a decipherment, neither of a target letter: SP 87/4/47 (Cardonnel to Tilson, 9 Oct 1708, "partially in cipher, later decoded interlinearly") and SP 87/32/45 (Holdernesse to Browne, 7 Nov 1758, the two ciphers and deciphers returned after the death of the correspondent); SP 87/32/62 (29 Aug 1759) records Granby returning the ciphers. These are different items from /234 and /115; recorded with their references, nothing else set. The listing is a catalogue search result for the log, not a verdict on any other source (rule 10). Other six pieces of the folder (SP 87/8, 16, 17, 21, 30, 45) not listed. Files: scratchpad TSVs, not committed.

Verdict: open, parked on ASKS row 57 (TNA page copies); the `--notes` step for SP 87/4 and SP 87/32 is done with no note-field hit, no free step left on these two pieces; next step (costed): the page-copy order in REQUEST.md.

## IMG-DECODE1: DECODE key records 8957, 8763-8765 (account 2 worker for LANE-IMAGES, 3 Oct 2026)

Step run: the "While waiting" item S above. One browser login (`tools/decode_browser_login.js ... --guess-fullsize --listen`,
shared with two other targets). Images are not committed: each RecordsView says "The image is not in the public domain.
Publishing it is only possible with the permission of the Library." Sha1s and URLs are in `images/manifest.json`.

| Record | Shelfmark (DECODE) | DECODE date | Sender / receiver | Type, language | Seen |
|---|---|---|---|---|---|
| R8957 | BL Add MS 32264 f.3-4 | 1710 | both blank | Key; simple substitution + nomenclature, nulls; language blank | **full size served** (P2, 4260x5507). A numbered code table with French meanings (e.g. 19 plenipotentiaire, 202 la Hollande, 316 l'electeur de, 211 ratification). No title or holder named in the top third of P2. P1 thumbnail is a blank cover |
| R8763 | BL Add MS 61575 f.62-63 | 1711-1713 | blank | Key; homophonic + nomenclature; English | P1 thumbnail only (200 px): nearly blank, no caption legible |
| R8764 | BL Add MS 61575 f.64-65 | 1712-1713 | blank | Key; nomenclature; English | P1 thumbnail only: two columns of name entries, not legible at 200 px |
| R8765 | BL Add MS 61575 f.66-68 | 1712-1713 | blank | Key; homophonic + nomenclature; English | P1 thumbnail only: a list, not legible at 200 px |

Answers to the brief:
- **Are full-size images served?** Yes (tested on R8957 P2). Thumbnails are served for all four.
- **Does any record's text name the French plenipotentiaries or Malknecht?** No. Every sender/receiver field is blank and
  there is no caption. The one look (vision call 3 of the job, at contact-sheet resolution) found no such name on the R8957 P2
  head or on the four P1 thumbnails.
- R8957's French vocabulary ("plenipotentiaire", "la Hollande", "l'electeur de", "ratification") fits peace-negotiation traffic
  of 1710. That is an inference from a few words, not an attribution.
Nothing was tested, because no ciphertext of any of the 13 items is on disk. Status unchanged: open, parked on ASKS row 57. Grades: none.
Requests: de-crypt.org 9 for this target (4 RecordsView, 1 full-size image, 4 thumbnails), part of about 39 for the shared
one-login job. Vision calls: 1 for this target.
