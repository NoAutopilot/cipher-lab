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

## FT4-sp54-maclean-1745 (3 Oct 2026, account-4): Lyon vol. 1 retry, crib list, planned crib test

No cryptanalysis was run in this job. The ciphertext of SP 54/25/5 and 8B is **not on disk**: SP 54/25 is not digitised,
and the TNA page copy is still awaited (REQUEST.md, ASKS row 57). So `tools/design_prior.py` was **not run**, because it
has no input. The design statement below comes from the period sources, not from sign statistics.

**(1) Lyon in Mourning vol. 1, by a different route.** The djvu.txt download failed (HTTP 500) on 25 Sept and again on
3 Oct. This time Internet Archive's full-text API answered: `be-api.us.archive.org/fts/v1/search?identifier=lyoninmourningor01forbuoft`,
10 calls, 9 at HTTP 200 and 1 at 502 ("Burnet"; not retried). Hits: "Hector", "Mac Lean" and "Castlehill" all return the
same passage: "...loyalty did upon the fifth of June last cause apprehend Sir Hector Mac Lean and George Blair [sic] of
Castlehill, by three o'clock in the morning, being informed they were to set out...". This is a third independent
confirmation of the 5 June 1745 arrest. "Barclay" returns only unrelated hits (James Barclay in a list of Elcho's men; R.
Barclay of Dorking, an 1892 manuscript owner). "cipher", "cypher" and "Linlithgow" return 0 hits. The API returns one
snippet per item and no real page number (CLAUDE.md access playbook), so this is not a whole-volume read. The
volume is **not** cleared for print risk. It is now reachable but unread, not unreachable.

**(2) Crib list.** Sources: Murray of Broughton's *Memorials* (SHS 1898, `memorialsofjohnm00murr`, refetched and grepped
3 Oct 2026) and Blaikie's *Origins* (`originsoffortyfi00blaiuoft`, refetched 3 Oct 2026). Grades follow rule 4: H/C for
what a source states, I for what we infer about the seized papers.

| crib | where stated | grade for "in the seized papers" |
|---|---|---|
| Linlithgow; "Wednesday" (the meeting day, 6 June 1745) | Memorials p.136 (Barclay letter: "go with him to Linlithgow on the Wednesday"), p.157 ("an appointment ... att Linlithgow with the D.") | C for the Barclay letter's clear content; I for the cipher letters |
| "the D." / Duke of Perth | p.157 (as the Justice Clerk read "the D."); p.135 (packet "not to be opened till the Duke of Perth was present") | C (Barclay letter), I (8B) |
| ague, vomit, the bark (the writer's illness) | p.136 | C, Barclay letter only |
| signatures "J. Barclay" and "Barclay" (Murray) | p.136 and p.101 note (Bell: aliases used by Murray) | C for the 5/8B group *only if* the Barclay letters are among SP 54/25/5's three (not checked; TNA item description next) |
| the Prince's "intended voyage, and the signals he was to make" | p.135 (what Maclean told Murray orally) | I (plausible content of the Burnet packet; not stated as written) |
| addressee Murray, under a cant name; the Prince signing "Burnet" | catalogue text of 8B; *Origins* glossary and pp.60-62 (Burnet = the Prince, Fisher = the King of France, Cuming, Moore, Martin, Morris as cant names in clear) | H for "Burnet" (catalogue); I for the rest |
| Lord John Drummond's regiment; recruiting; George/John Blaw of Castlehill | catalogue text of SP 54/25/5 (QUEUE N37); Memorials pp.126, 135 | H for the catalogue wording |
| people near the packet: Duke of Perth, Lochiel, Elcho, Traquair, Sir James Steuart, Macleod of Macleod, Sheridan, Balhaldy | Memorials pp.126-137, 396-397; *Origins* pp.60-66 | I |

**Design these cribs would fit.** In 1744 Murray wrote to "Mr. Burnet" in a mixed system: plain English with cant names in
clear, and names and places in numeric groups up to about 1950. Blaikie prints these groups with meanings on pp. 60-66 of
*Origins*. His note says they were "deciphered partly by comparison with other ciphers; partly from information given by
Murray in his Memorials; occasionally by conjecture". Examples:

- 636 616 1614 12 30 1392 = probably Captain Clephan
- 425 1876 1614 = Rotterdam
- 434 1054 1730 = Captain Anderson
- 598 1614 = probably officers of his regiment
- 1389 1051 C13 = Lord Elcho
- Sir 1293 43C 1055 1744 1045 1948 1679 1778 = Sir James Steuart (printed with 948 instead of 1948 on p.66)

Footnotes on pp. 64-66 also gloss the Duke of Perth, Lochiel, Traquair and Macleod. One name takes several groups, and
1614 recurs as a final group across different names. That looks like a numeric syllabary or letter-group nomenclator,
not a one-code-per-name list. "Letters, partly in cipher, from Burnet" fits this design: the Prince's side of the same
correspondence, a year later. This is inferred, not checked against the image.

**(3) Planned crib test, pre-registered here, to run only once the TNA copy is transcribed:**
1. *Known-code overlap.* Statistic: the number of distinct numeric groups in 5/8B that also appear in Blaikie's printed
   1744 Murray-Burnet groups, about 40 distinct groups on pp. 60-66. List the groups mechanically from the djvu text, then
   check them against the page image. Matched control: 10,000 draws of the same number of distinct groups, uniform over the
   target's own observed range, and separately a digit-permuted copy of the target's groups. Each control's overlap can
   differ from the target's on this statistic, so it is not a non-test (rule 3, the "control that cannot vary" paragraph).
   PASS needs the target's overlap above the 99th percentile of the uniform draws AND above the digit-permuted copy.
   Also needed: at least 3 shared groups whose Blaikie meaning fits the plain-text slot around them (a name slot gets a
   name). A PASS means "same code family, worth a key rebuild", not a reading.
2. *Crib placement (only after 1 passes).* Place the multi-group name cribs from the table (Perth, Linlithgow, Murray's
   cant name, Lord John Drummond, Blaw) at every slot whose plain-text context says "name". Count the slots where a
   placement agrees with a code already fixed by Blaikie or by another placement. Matched control: the same count on a
   synthetic letter of the target's N, built from a random relabelling of a 1,950-group syllabary over the same cribs.
   Gate: rule 3's headline control-first order. Do not read a target count until the synthetic control shows the count
   recovers a planted crib at that N. N is unknown until transcription; the control's N is set from the transcription, never guessed.
3. Graded output: per-token H/C/S/M/I counts; `tools/judge_plaintext.py` with an era-matched English corpus before any
   PASS is reported (rule 3, the pt18 paragraph; en18 is the nearest corpus).

Requests this job: be-api.us.archive.org 10 (fts, 1.6 s apart; one 502, not retried), archive.org 2 (Memorials djvu,
Origins djvu; refetches, since the earlier session's copies were not on this container's disk). No WebSearch.

## Remaining gaps (FT4-sp54-maclean-1745, 3 Oct 2026)
Read so far: 0 of 2 items (no image or transcription of SP 54/25/5 or 8B on disk)
- SP 54/25/5 and 8B ciphertext - blocker: waiting-on ASKS row 57 (TNA page copy, REQUEST.md); not digitised on Discovery
- print risk: Lyon in Mourning vol. 1 read only by fts snippets - blocker: not-attempted; vol. 1 reachable by be-api fts but the djvu file 500s; next: be-api fts for "Burnet" (502 today), "Drummond", "Perth" plus a person's read in the IA reader if a hit lands, ~$1
- item-level description of SP 54/25/5 (are the "Barclay" letters among the three?) - blocker: not-attempted; the While waiting step of 3 Oct names it and nobody has run it; next: tools/discovery_items.py "SP 54" "SP 54/25", ~$0.5

## Escalation (FT4-sp54-maclean-1745, 3 Oct 2026)
- [n/a] siblings: no sibling cipher letter on disk; the 1744 Murray-Burnet letters are in print only (Origins pp.60-66), used as known keys below
- [x] clear-pages: Memorials pp.134-137, 157 give the Barclay letters' clear content (crib table above)
- [ ] known-keys: Blaikie's printed 1744 Murray-Burnet numeric groups (Origins pp.60-66) are the planned overlap test, waiting on the transcription
- [ ] print: Lyon vol. 1 fts for "Burnet", "Drummond", "Perth"; Browne's History vol. ii appendix (prints a "J. Barclay" letter, Memorials p.101 note) unread
- [n/a] key-rebuild: no ciphertext on disk to rebuild a key against
- [n/a] image-check: no image of SP 54/25 is available; waiting on TNA copy
- [ ] retry: Lyon vol. 1 "Burnet" fts query (502 on 3 Oct), once, on a later day
Verdict: keep going: 2 internal gaps; cheapest next: tools/discovery_items.py "SP 54" "SP 54/25" for the item description, ~$0.5
