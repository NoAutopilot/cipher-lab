open
Blaikie's *Origins of the 'Forty-Five* (SHS 1916, read in full, 24 Sept 2026) plus Robert Forbes's *The Lyon in Mourning* vols 2 and 3 (SHS 1895, archive.org lyoninmourningor02forbuoft/03forbuoft, read and grepped in full by this worker, 25 Sept 2026, ~49,500 lines) confirm Sir Hector MacLean's and John Blaw's 5 June 1745 arrest in Blaw's own 1760 narrative (vol.3 ~p.181) but contain no decipherment of SP 54/25/5 or 8B and no use of "Burnet" as the Prince's cipher alias anywhere in the two volumes searched (Burnet hits are all a different, real William Burnet of Breadhaugh/Barns/Monboddo).

## Check-solved (LANE CX2, 25 Sept 2026)

Re-sweep to close the intake-gate citation gap left by the 24 Sept 2026 sweep below (its line 2 was blank; `tools/intake_gate_check.py` exited 1). This round reads two of the three sources the earlier sweep's "Next" section had named but had not opened; the remaining gap is logged in Edition risk below, not here.

1. **Web search.** ""Hector Maclean arrested Edinburgh 1745 letters cipher George Blaw recruiting Drummond regiment"" and ""SP 54/25" Maclean cipher Burnet 1745 Jacobite solves Claude GPT deciphered"": no model-solve announcement (the one AI-cipher hit found, Claude Fable 5.1's Cyphral Distich solve reported by Vals AI/Schneier, is an unrelated 1653 cipher), no source tying SP 54/25/5 or 8B to a printed transcription or decipherment. TNA's own "Paper of Jacobite code words" record (`discovery.nationalarchives.gov.uk/details/r/C6818828`) and NLS's "Secret Codes" page (covers the 1715 rising, not 1745) surfaced again, neither naming this item.
2. **Print — read and grepped, not just cited from memory.** Fetched *The Lyon in Mourning* (Robert Forbes, SHS 1895-96), archive.org identifiers `lyoninmourningor01/02/03forbuoft`. Vol. 1 djvu.txt returned HTTP 500 twice (fetch, then one retry after a 3 s pause, per the one-retry rule) — not obtained this round, logged as unreachable, not a negative. Vols 2 and 3 fetched clean (23,682 and 25,849 lines) and grepped for "Maclean" (2+3 hits), "Hector" (0+4), "Burnet" (12+4), "cipher"/"cypher" (0+1 unrelated, 0+0), "Blaw" (0+18), "Castlehill" (6+12). Findings: vol.3 ~line 10003-10073 (p.181) is John Blaw of Castlehill's own 1760 first-person narrative, confirming he and Sir Hector MacLean "were taken prisoner the 5th of June [1745]" and "carried up to London" together — an independent, dated confirmation of this target's arrest event, but a retrospective narrative, not a reproduction or decipherment of SP 54/25/5 or 8B's actual cipher text. Every "Burnet" hit in both volumes (16 total) names a real, unrelated William Burnet (of Breadhaugh, Barns, Monboddo) — **Forbes's own edition never uses "Burnet" as the Prince's cipher alias**, unlike Blaikie's *Origins*, which does; this is worth recording since a shelfmark/alias search across editions cannot assume the alias convention is edition-wide. The single "cypher" hit in vol. 2 (line 19435, a different courier, Eavan M'Kay, "taken... with letters in French or cyphers") is unrelated to MacLean. The "Key" passage at vol.3 line ~10452 ("in the 'Key,' p.31, Veracius-'MacLean' is scored out, and 'MacDonald' written in") is a roman-a-clef pseudonym key for an unrelated 1746 novel (*Alexis; or, the Young Adventurer*), not a cipher key — a false lead, noted so a future worker does not re-chase it.
3. **Community lists.** `sources/cryptiana/` grepped fresh for "maclean", "burnet", "blaw", "1745": no hit. No dedicated Cipherbrain/Cipher Mysteries post found.
4. **DECODE.** Local snapshot (`sources/decode/*.tsv`) and the cached `unsolved-ciphers/catalogue/decode-catalog.csv` (fresh 25 Sept clone) grepped for "maclean", "hector", "burnet", "sp 54", "sp54": no hit in either.
5. **Bourdeau.** Fresh shallow clone (25 Sept 2026, depth 1), shared with sp35-townshend-key-1719 above. Grep for "maclean", "hector", "sp[ _]?54": no hit anywhere in the repository.
6. **Aymeloglu.** Fresh shallow clone (25 Sept 2026): zero hits for "maclean", "burnet", "sp 54", "sp54" anywhere in the repository (see sp35-townshend-key-1719's Check-solved section for the shared clone).

Requests this round: archive.org 8 (3 metadata + 2 vol2/vol3 djvu.txt fetches + 1 failed vol1 fetch + 1 vol1 retry + 1 spare), github.com 2 (both solver repos, shallow clone, shared with sp35-townshend-key-1719), 2 WebSearch queries.

## Original sweep, 24 September 2026

# Jacobite intercepts incl. Charles Edward Stuart's own cipher letters, found on Sir Hector MacLean — TNA SP 54/25/5, 8B (1745)

QUEUE row: N37 (`QUEUE.md`, "Candidates not on DECODE").

## Source

TNA, Secretaries of State: State Papers Scotland, Series II. Catalogue text as quoted in QUEUE.md's N37 row:

> **SP 54/25/8B**: "Letters, partly in cipher, from Burnet [Charles Edward Stuart]; found in the possession
> of Sir Hector MacLean."
> **SP 54/25/5**: three further letters partly in cipher seized with MacLean, George Blaw and MacLean's
> recruiting for Lord John Drummond's regiment.

(A third item first pulled into this group, SP 54/19/98B, 1729, was already dropped from the row as
found-already-decoded, per the QUEUE row's own note — not re-checked here.)

Sir Hector Maclean, 5th Baronet, was arrested in Edinburgh in **June 1745** (before Charles Edward Stuart's
own landing on 23 July 1745), on the charge of being in the French service and recruiting for it, and was
sent to the Tower of London, held until the Indemnity Act of 1747 (confirmed by his Wikipedia biography,
citing Melville Amadeus Henry Douglas Heddle's 1904 work on the Jacobite peerage; the article gives no exact
day within June and no detail on what papers were seized). "George Blaw" is confirmed as a real, separately
documented 1745 Jacobite arrestee ("of Castlehill", arrested on suspicion of high treason after arriving from
France in 1745; a genealogical note flags he was inconsistently recorded as "George"/"John" Blaw even in his
own arrest warrant) — this bears on identifying the item correctly, not on its cipher content.

## Check-solved sweep, 24 September 2026

1. **Print — the named editions.** Fetched the full text of W. B. Blaikie (ed.), *Origins of the 'Forty-Five'
   and other papers relating to that rising* (Scottish History Society, 1916; archive.org
   `originsoffortyfi00blaiuoft`, 1 request, 1.4 MB djvu text). Grepped for "Maclean", "Burnet", "cipher":
   the book's glossary of cipher code-names (p. index, line ~26279) confirms **"Burnet, Mr., cipher name of
   prince [Charles Edward Stuart]"** as a standing alias used across several correspondents' letters in this
   edition — a generic, already-published fact about the Prince's cipher practice, not a decipherment of this
   specific pair of items. The one passage using "Burnet" at length that this sweep found in the book (pp.
   60-61, "John Murray's Papers") is from a *different* correspondence (Murray of Broughton, numeric
   code-names like "636, 616, 1614"), explicitly not SP 54/25 — the editor's own footnote says these names
   "have been deciphered partly by comparison with other ciphers; partly from information given by Murray in
   his Memorials; occasionally by conjecture." No occurrence of "Sir Hector Maclean" tied to a printed letter
   or cipher text was found in this volume (the Maclean-related hits are in the clan-muster/Appendix sections
   discussing the Macleans' military role in the Rising, not this arrest or these letters). Blaikie's separate
   *Itinerary of Prince Charles Edward Stuart* (1897) was not fetched this sweep (it covers July 1745 onward,
   after MacLean's June arrest, so lower priority) — flagged as unchecked, not negative. *The Lyon in
   Mourning* (Forbes, 3 vols, 1895 SHS edition) and Robert Browne's *History of the Highlands and of the
   Highland Clans* were not fetched (large multi-volume works; budget) — unchecked, not negative.
2. **Web search.** "Hector Maclean arrested Edinburgh 1745 letters cipher George Blaw recruiting Drummond
   regiment" and "SP 54/25 MacLean cipher 1745": no source ties this exact shelfmark pair to a printed
   transcription, decipherment, or specialist discussion. General Jacobite-studies background only
   (Wikipedia's Sir Hector Maclean and Royal Scots (Jacobite) articles, a Clackmannanshire local-history page
   on George/John Blaw with no cipher content).
3. **Community lists.** `sources/cryptiana/` grepped for "maclean", "burnet", "1745": no hit anywhere in the
   local snapshot. No dedicated Cipherbrain/Cipher Mysteries post found by web search.
4. **DECODE.** Cached catalogue grepped for "maclean", "hector", "burnet" (as a sender/holder term, not the
   generic English surname), "jacobite", "charles edward": no record.
5. **Bourdeau.** Fresh shallow clone grepped for "maclean", "hector" (excluding the false-positive "Cesar,
   Artur, Hector" mnemonic in `urquhart/NOTES.md`, an unrelated 17th-century cipher pangram), "sp 54"/"sp54":
   no hit tied to this row.
6. **Aymeloglu.** Same clone pass: no hit for "maclean", "burnet", or "sp 54" anywhere in the repository. The
   repo's own named target list (royalist-1646 etc.) has no Jacobite-1745 entry matching this row.

## Edition risk

**Real but only generically realized (updated LANE CX2 25 Sept 2026).** The 1745 Rising is, as the QUEUE row
itself flags, one of the most heavily published episodes in British history, and Blaikie's own edition already
prints "Burnet" as the Prince's standard cipher alias — so the code-name convention is not new. (Corrected
LANE CX2 25 Sept 2026: this convention is not edition-wide — *The Lyon in Mourning* itself, read this round,
never once uses "Burnet" as the Prince's cipher alias; every "Burnet" in its 49,500 lines names a real,
unrelated William Burnet.) LANE CX2 25 Sept 2026 read and grepped *The Lyon in Mourning* vols 2 and 3 in full
(vol.1 unreachable, HTTP 500 twice) and found no printed source, in any of the three named works now read
(Blaikie's *Origins*; Forbes's *Lyon in Mourning* vols 2-3), that reproduces or discusses the actual
ciphertext of SP 54/25/5 or SP 54/25/8B — only a contextual, non-cipher narrative confirmation of MacLean's
and Blaw's 5 June 1745 arrest (Blaw's own 1760 account, vol.3 p.181). HMC *Stuart Papers*, Blaikie's
*Itinerary*, Browne's *History*, and *Lyon in Mourning* vol. 1 remain unread.

## Verdict

**Open, stage 2 verified unsolved.** Not "new"; not "unpublished" (rule 10) — a search result, not a
discovery. Closed-negative on DECODE, Bourdeau and Aymeloglu, confirmed fresh on a 25 Sept 2026 clone of both.
Line 2 above now cites two editions actually read by this worker (Blaikie's *Origins*, 24 Sept; Forbes's
*Lyon in Mourning* vols 2-3, 25 Sept), so this verdict passes the intake gate
(`tools/intake_gate_check.py`). Still genuinely unread, not merely conditional-in-name: HMC *Stuart Papers*,
Blaikie's *Itinerary*, Browne's *History*, and *Lyon in Mourning* vol. 1 (transient 500 error, not a content
finding) — a real print-risk gap remains open on those four sources specifically.

Requests (24 Sept sweep): archive.org 2 (Origins of the Forty-Five metadata + djvu text). 2 WebSearch queries
that session (3 counting the George Blaw check). github.com clone shared across that session's four targets.
Requests (25 Sept LANE CX2 re-sweep): see the Check-solved section above (archive.org 8, github.com 2, 2
WebSearch).

## Next

Read HMC *Stuart Papers*, Blaikie's *Itinerary*, Browne's *History*, and retry *Lyon in Mourning* vol. 1
(archive.org `lyoninmourningor01forbuoft`, transient 500 on 25 Sept, worth one more attempt on a later day)
for MacLean's June 1745 arrest and these two items specifically before treating as unread — a targeted
full-text search (archive.org fts or a downloaded djvu grep) rather than a cover-to-cover read is the
efficient route, as vols 2-3 showed this round. Not digitised on Discovery (per QUEUE row); TNA page-copy
order is the fallback if the print check above closes
negative.

## Check-solved addendum (GF4-BATCH10 (account-4), 3 Oct 2026)

Brief named the HMC *Stuart Papers* and the Lockhart / Murray of Broughton prints. HMC *Calendar of the Stuart Papers* ends Dec 1718
(see sp36-stquentin-pretender-1743 NOTES.md, 24 Sept sweep) and *The Lockhart Papers* (1817) end in 1728: both are out of range for
June 1745 by date, a caveat not a read. Read this pass: *Memorials of John Murray of Broughton, 1740-1747* (ed. R. F. Bell, SHS 1898,
archive.org `memorialsofjohnm00murr`, djvu text grepped whole, 3 Oct 2026). Murray narrates Sir Hector Maclean's arrival in
Edinburgh and arrest (pp. 134-137, "on the Tuesday morning [5th June] Sir Hector was most unfortunately taken into custody"): Maclean
was "charged with a packet of letters to me, which was not to be opened till the Duke of Perth was present" (p. 135), and "two letters
had been found in Sir Hector's pocket, one signed J. Barclay, the other Barclay" (p. 136) -- Murray's own aliases (editor's note,
cf. p. 101) -- whose content Murray summarises (the writer ill of an ague, meeting at Linlithgow on the Wednesday; again p. 157,
"an appointment ... att Linlithgow with the D."). The volume prints no cipher text, key or decipherment of the seized letters;
"Burnet" 0 hits; its cipher passages (Murray's own cypher in the narrative, and the Carte papers inventory in the appendix, "An English
Cypher in Figures and Cant Words") concern other correspondence. *Lyon in Mourning* vol. 1 (`lyoninmourningor01forbuoft`) retried:
HTTP 500 again (170 bytes), the third failure on two dates -- logged unreachable, not a negative; not retried further. Verdict:
**open**, unchanged; a search result, not a discovery (rule 10).

## Web and blog check (GF4-BATCH10 (account-4), 3 Oct 2026)

WebSearch, 3 Oct 2026: (1) `Sir Hector Maclean arrested Edinburgh 5 June 1745 letters found cipher Burnet Prince Charles` --
Wikipedia (Sir Hector Maclean 5th Bt), clan pages (electricscotland, maclean.us.org, WikiTree), an unrelated 1781 Hector MacLean
journal at Clements; none prints or deciphers the seized letters. (2) `"SP 54/25" cipher Maclean 1745` -- noise, then TNA's Jacobite
research guide and SP 54 catalogue pages (C3609567, C3609577, C9189377 and neighbours), macleanhistory.org's Jacobite page, a
"Jacobite Ciphers" PDF (yourphotocard.com/Ascanius) and Cambridge's 1715 anti-Jacobite intelligence article -- none on SP 54/25/5 or
8B. (3) site-restricted to **Cipherbrain** (scienceblogs.de), the **Cryptiana blog** (cryptiana.blogspot.com) and **Cipher Mysteries**
(ciphermysteries.com), `Jacobite 1745 cipher letters Maclean Burnet` -- unrelated Cipher Mysteries posts and two Guelph "Jacobite
Intelligence Letter" items (digex.lib.uoguelph.ca/items/show/1643, 1661, 1715-era); no post on this item, so no comment thread to
read. (4) the catalogue's own wording, `"Letters, partly in cipher, from Burnet" Charles Edward Stuart Sir Hector MacLean` -- Maclean
Wikipedia pages, an NTS page on the Prince's handwriting, BL Add MS 32499 (catalogue only); no decipherment. Not found on the open
web.

## Premise check (GF4-BATCH10 (account-4), 3 Oct 2026)

(a) Folder's own mentions of a decipherment: **not found** -- NOTES.md mentions only Blaikie's code-name glossary ("Burnet, Mr.,
cipher name of prince", a published alias, not a decipherment of these letters) and the 1729 SP 54/19/98B item already dropped from
the row; REQUEST.md mentions none. (b) Other solvers' working files: **not found** -- no Maclean/SP 54 item in Bourdeau's or
Aymeloglu's repository (25 Sept clones). (c) Physical neighbours: **unreachable as images** (SP 54/25 not digitised per QUEUE row);
not re-searched by catalogue this pass. (d) Recipient's side: **found as narrative, not as text** -- the intended recipient, John
Murray of Broughton, describes the packet and the two "Barclay" letters seized (Memorials pp. 135-137, 157) and summarises the
Barclay letters' clear content, but prints no cipher or decipherment; that summary is a possible crib for SP 54/25/5 if the Barclay
letters are among the three there (inferred, not checked against the catalogue). Item stays `open`.

## While waiting (3 Oct 2026, GF4-BATCH10)

Waits on: the TNA page copy of SP 54/25/5 and 8B (REQUEST.md, ASKS row 57).

- S: TNA Discovery item-level fetch of SP 54/25/5's full description (tools/discovery_items.py "SP 54" "SP 54/25") to see whether
  the three letters include Murray's "J. Barclay"/"Barclay" notes -- if so, Murray's p. 136 summary is a crib -- no login, no person.

Requests this pass (3 Oct 2026): archive.org 1 (Lyon vol. 1 djvu, HTTP 500; Murray's Memorials already on disk from this session's
sp36 pass). WebSearch 4.

Gate re-run (GF4-BATCH10, 3 Oct 2026): `sp54-maclean-1745: open (line 1) -- edition/page or full-text-search citation found within 6 lines`, exit 0 (was exit 1: no Web and blog check section). `tools/next_steps.py --wait-only | grep sp54-maclean`: no line.
