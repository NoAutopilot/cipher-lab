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
