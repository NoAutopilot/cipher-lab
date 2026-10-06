open
No calendar of State Papers Domestic reaches 1745; Culloden Papers (1815, the government-side Forbes correspondence to 1748; IA cullodenpapersco00lond) djvu full text grepped by this worker (GF-A2-9, 2 Oct 2026) for "Ball", "cypher", "cipher", "Mareschal": three "Ball" hits, all dances, no cipher -- the item is not printed there.

# Z Ball to an unknown recipient, in cipher — TNA SP 36/74/1/60

QUEUE row: N62 (sources/solver-diffs/2026-09-23-non-decode-hits.tsv, "Candidates not on DECODE").

## Source

The National Archives, Kew, **SP 36/74/1/60** (State Papers Domestic, George II), folio 60, 1745 Nov. 19 (TNA
Discovery, fetched 24 Sept 2026, id C12771598; `digitised: false` confirmed by direct record fetch; no separate
`note` field). Scope content: "Folio 60. Z Ball to [unknown]. In cipher." 19 Nov. 1745 falls in the middle of the
Jacobite army's advance into England after crossing the border (the army took Carlisle 15 Nov, reached Preston
20 Nov, Manchester 28 Nov) — this piece is squarely intelligence/intercept material from the government side of
the '45 crisis, not Jacobite Rome-court correspondence (so HMC's *Calendar of the Stuart Papers* at Windsor,
which covers James Francis Edward Stuart's own court to Dec. 1718 only, does not apply here either).

## Check-solved sweep (24 September 2026)

1. **Editions.** The printed *Calendar of State Papers Domestic* series ends in Anne's reign (does not reach
   George II, 1745) — a hard exclusion by date, not a search failure, the same shape as sp36-stquentin's
   Stuart Papers exclusion and sp81-roe's Richardson 1740 exclusion. No other calendar or edition was located
   that covers SP 36 intercept material for Nov. 1745 specifically. "Z Ball" was not identified as a known
   historical figure by web search (`"Z Ball" OR "Zachary Ball" 1745 Jacobite intercepted letter cipher SP
   36`); results surfaced only general Jacobite-1745 research aids (jdb1745.net, TNA's own Jacobite Risings
   research guide) with no mention of this name or item.
2. **Sibling search (TNA Discovery).** `tools/discovery_items.py "SP 36" "SP 36/74" decipher` and `... Ball`
   return **only the target record itself** — no companion key or decipher elsewhere in the piece. A TNA-wide
   search (not piece-restricted) for the literal string `"Z Ball"` also returns only this one record.
   Government-side ciphers of this period were normally deciphered by the Deciphering Branch (Edward Willes)
   and often kept in **SP 106**; a targeted SP 106 search for this specific item was not run this pass (outside
   this run's search-term budget) — flagged as the next useful TNA query, not a clearance.
3. **Community lists.** WebSearch as above; local grep of `sources/cryptiana/` for "ball"/"SP 36/74": no
   relevant hits (matches, if any, are unrelated).
4. **DECODE.** No login attempted. `sources/decode/` greped for "Ball"/"SP 36/74"/"Z Ball": no hits.
5. **Solver repositories — a direct hit, corroborating rather than clearing.** Fresh shallow clone of
   `dbourdeau/cyphersolver` (24 Sept 2026, shared across this pass's four targets):
   `cyphersolver/oldest/scan_2026-09-23/hard_targets.md` — Bourdeau's own 23 Sept 2026 scan of "hard unsolved
   targets outside DECODE" — lists this **exact item** under "10. TNA intercepts flagged 'undeciphered'":
   > "Also: SP 78/111/93 (f. 212), a French letter 'entirely in cipher', 20/30 Sep 1642; SP 35/46/59
   > 'Undecyphered paper', c. 1723 (Atterbury plot); **SP 36/74/1/60 'Z Ball to [unknown]. In cipher', 19 Nov
   > 1745 (Jacobite rising).**"
   > "Images: State Papers Online (Gale, subscription) or TNA copy order; not free. Prior art: TNA catalogue
   > says undeciphered; nothing in print found."
   This is not a solve or a claim of novelty — it is Bourdeau's own team independently reaching the same
   verdict (unsolved, not free online, "nothing in print found") one day before this sweep, on their own
   search. `aaymeloglu/unsolved-ciphers`: zero matches for "Ball"/"SP 36/74."
6. **General web search.** As (1). No result ties a decipherment, key, or prior reading to SP 36/74/1/60
   specifically.

**Host requests this pass:** discovery.nationalarchives.gov.uk 4 (search x2, record detail x1, TNA-wide "Z
Ball" search x1, >=3s apart, shared budget with the other three targets this run), WebSearch 2, github.com 1
shallow clone each of both repos (grepped, shared across all four targets), sources/decode/ and
sources/cryptiana/ local greps (no network).

## Verdict

**Status: open.** No printed calendar reaches George II-era SP 36 (a hard date exclusion); "Z Ball" is
unidentified. No sibling key or decipher found under this piece's own search terms (an SP 106 Willes-branch
search was not run this pass and is the natural next step). No community list or DECODE record names this
item. dbourdeau/cyphersolver's own 23 Sept 2026 scan independently lists this exact shelfmark as unsolved and
not found in print, one day before this check — a second, independent negative search, not a clearance, and
not itself grounds for "never printed" wording (CLAUDE.md rule 10).

**Copy status:** no online image located; `digitised: false` confirmed by direct record fetch (id C12771598).
Bourdeau's scan separately notes the item is also on State Papers Online (Gale, subscription), not a free
route. **Copy-order.** See REQUEST.md.

**Recommended next steps (not run this pass):** (1) search TNA Discovery for an SP 106 (Deciphering Branch)
key or decipher tied to this correspondent or to Nov. 1745 Jacobite intercepts generally; (2) identify "Z Ball"
via Jacobite prosopography (jdb1745.net, the Jacobite Database of 1745, surfaced this pass but not queried
directly) or the government's own intercept-handling records; (3) once imaged, check whether the hand or cipher
matches other Nov. 1745 SP 36/74 intercepts in the same folder.

## Web and blog check (GF-A2-9, 2 Oct 2026)

Plain web searches (4): `"Z Ball" 1745 cipher letter` (sender + date); `"SP 36/74" cipher 1745 intercepted` (shelfmark);
`Ball 19 November 1745 letter in cipher Jacobite State Papers Domestic` (date + descriptive title); the folder has no
clear text to quote, so the fourth query is the blog one below. Hits: TNA catalogue pages (C15669207 = SP 36/78/1/39,
C16108299, C15668342 = SP 36/73/3/66 O'Brien to Charles Edward in cipher, SP 36/77/1/188 Perth servant's code list,
C12771605 = SP 36/74/1/72), Jeremy Black's Gale essay on State Papers, a 1724 Brougham-archive decipherment (dspace.ut.ee,
a different letter), the TNA blog post "secret diplomatic message deciphered after 350 years" (a 17th-century letter,
not this one), Columbia's Jay papers and a Zodiac page. None carries a decipherment or plaintext of SP 36/74/1/60.
Blog site searches: `Jacobite 1745 cipher letter intercepted Willes deciphered` on scienceblogs.de (Cipherbrain),
cryptiana.blogspot.com / cryptiana.web.fc2.com and ciphermysteries.com: Cipherbrain posts on Verne's turning grille, an
unsolved 1645 cipher, the 1783 Manchester letter, anamorphica and a Confederate cover; Cipher Mysteries' Beale, list and
review pages. None names Ball, SP 36 or a 1745 intercept, so no comment thread was relevant to open. Local
`sources/cryptiana/` (wallis*.htm and the rest) grepped for Ball/1745/Willes: nothing on this item.
Result: no decipherment or plaintext of the item found on the open web or in the three blogs.

## Premise check (GF-A2-9, 2 Oct 2026)

(a) Folder's own mentions -- none. The TNA text is only "Folio 60. Z Ball to [unknown]. In cipher."; Bourdeau's
hard_targets.md lists it as undeciphered. No decipherment, clear copy or gloss is mentioned anywhere in the folder.
(b) Other solvers' working files -- shallow clones of dbourdeau/cyphersolver and aaymeloglu/unsolved-ciphers
(2 Oct 2026) grepped for "Z Ball", "SP 36/74", "Ball to": the only hit is cyphersolver's
research/oldest/scan_2026-09-23/hard_targets.md (the listing already quoted above); no working files, no rendering, no
key run on it. Nothing in Aymeloglu's repository.
(c) Physical neighbours -- catalogue only (not digitised); one strong lead. SP 36/74/1/61 (Discovery C12771599, folios
61-62) is Lord Marischal to Charles Edward Stuart, from Paris, dated 30 Nov 1745 -- which is 19 Nov 1745 Old Style, the
same day as f.60 -- giving the French troop numbers (6,000 men and 500 dragoons for Scotland; "up to 12,000 men ready
to sail by 20 [December 1745 NS]"). A Paris letter to Charles Edward catalogued in clear immediately after an undated-
recipient cipher letter of the same day is the shape of an intercept and its deciphered or translated copy filed
together; whether f.61 is the clear text of f.60 cannot be settled from the catalogue. Ordering f.60 and f.61-62
together settles it. The other side, f.58-59 and f.72-73, are Newcastle's own drafts (to Lancashire's deputy
lieutenants; to Mr Vane), unrelated. The "Ball" channel continues in SP 36/78: f.41-42 "[Unknown] to Mr Ball.
Arrangements about meeting, written partly in cipher" with f.43-44 "Copy ... [Contents same]" (enclosed in SP
36/78/1/39, 23 Dec 1745, endorsed "Received from John Lewis on 31 March 1747" at Newcastle's office), and SP 36/78/2/
121-123 "[Unknown] to Mr Ball. Partially in cipher" with a copy at f.123 (31 Dec 1745). Those letters use cover names
(Griffith, Crofts, Cadogan, Rivers, Ratcliff, Talon, Blois, Booth, Anderton, Busby); the cataloguer summarised their
clear parts. Whether "Z Ball" of f.60 is the same Mr Ball, and whether the f.43-44 / f.123 copies carry the office's
deciphering of the cipher words, is unread.
(d) Recipient side -- recipient unknown. The Jacobite side's papers for Nov 1745 are the Stuart Papers at Windsor
(HMC calendar stops in 1718, as noted above) and the government side's printed Culloden Papers (line 2, grepped, no
Ball or cipher). Next: check Lord Marischal's 30 Nov 1745 letter in print (e.g. a full-text search for "6000" with
"Marischal" in the Stuart-papers and Elcho/Murray of Broughton editions on IA), then order SP 36/74/1/60-62 and SP
36/78/1/41-44 together; ~USD 1 for the search.


## Print check of Lord Marischal's 30 Nov 1745 letter, SP 36/74/1/61 (A2P4-BALL, 3 Oct 2026, 18:35-18:45 UTC)

Intake gate: `python3 tools/intake_gate_check.py sp36-ball-1745` -> "open (line 1) -- edition/page or full-text-search citation found within 6 lines" (exit 0). No transcription or cryptanalysis done; this pass is print search only.

Distinctive strings searched (from the catalogue summary of f.61, English, so wording in a printed French original may differ): Marischal + "6000 men" / "500 dragoons" / "12,000" / "ready to sail" / "20 December"; "SP 36/74" + Marischal; "Z Ball" 1745.

| Source | Query family | Result | Control |
|---|---|---|---|
| IA be-api fts (about 21 queries, whole index) | phrase/AND combinations above | no snippet pairs Marischal with the 6000/500-dragoon/12,000-sail figures; "SP 36/74" + Marischal = 2 hits (Duff, *The '45*, `450000duff`; Ridley, *The Jacobites*, `jacobitesnewhist0000ridi`), neither on the letter; "Z Ball" 1745 = noise only (Z. Ball of Michigan, electronics) | the same index returns Duff's note list citing other SP 36/74 items of 19 Nov 1745 (Spencer to DoN, Kendal; Wade to DoN, Hexham) and Ridley's "NA SP 36/74/1 ff. 79-81 Pattinson" -- so the index does read SP 36/74 citations in these two volumes |
| Duff, *The '45* (`450000duff`, lending-only: be-api snippets only, djvu 403 without a loan; no page number obtainable) | "Ball cipher", "Earl Marischal to ... Paris November 1745", "Marischal 6,000 dragoons" | 0 hits for Ball/cipher; no Marischal 30 Nov letter note | as above (SP 36/74 notes present) |
| Ridley, *The Jacobites* (`jacobitesnewhist0000ridi`) | "SP 36/74", Marischal "30 November" | one SP 36/74/1 note (ff.79-81), Marischal letters cited are RA SP/MAIN (Stuart Papers, Windsor) of 1744; no 30 Nov 1745 Marischal letter | SP 36/74 note reproduces |
| Mahon, *History of England from the Peace of Utrecht* vol. III (Google Books `5g4wAAAAMAAJ`, `VPdng8227KkC`, `CVAVAAAAQAAJ`, full view; `tools/gbooks_search_within.py`) | Marischal, dragoons, 12,000, 6000, Willes, cipher, Keith, Boulogne | Marischal pages 42-59, 162-164 (1740-44 Stuart Papers letters, appendix pp.345-353: Marischal to James 21 June 1740, Marischal 4 Nov 1743), none on 30 Nov 1745; the tool returns only the first 10 pages per word, so Marischal hits after p.353 and in the Nov 1745 chapter are not enumerated | endpoint reproduces known words (dragoons pp.193-203) |
| Google Books API (key, `country=US`, 5 queries; one 503, not retried) | Marischal + dragoons/6000 men/30th November; "Ball" in cipher 1745 State Papers | no volume with a snippet on the letter; Mahon appendix (Prince Charles to his father, Paris 30 Nov 1744 -- a year earlier) is the nearest date match and a different letter | API answered 200 with snippets |

Not found: no printed text, translation or abstract of SP 36/74/1/61, and no printed decipherment or plaintext of f.60, in Duff, Ridley, Mahon vol. III appendix, Culloden Papers (earlier pass) or the Google Books/IA full-text queries above. Not read: Blaikie *Origins of the Forty-Five* (SHS 1916), Elcho's *Short Account*, Murray of Broughton's *Memorials*, Browne, and the Stuart Papers themselves (Royal Archives, not printed after 1718 in the HMC calendar). These are the editions a later pass should open; this pass did not reach them (be-api's fuzzy matching made phrase hits unreliable, 25-minute box). A search miss, not a negative on the item.

Host requests: be-api.us.archive.org about 21; archive.org download/metadata 3 (djvu 403/empty for lending-only Duff); books.google.com SearchWithinVolume about 14; googleapis.com/books 5 (one 503); WebSearch 0; no vision calls; cost not read by the worker.

## Verdict (updated 3 Oct 2026)

Status stays **open**. The named free step (Marischal 30 Nov 1745 in print) found nothing in Duff, Ridley, Mahon, or open Google Books/IA full text; f.61 therefore remains uncertain as the clear copy of f.60, and only a copy order of SP 36/74/1/60-62 settles it (REQUEST.md). Next step: IA full-text on Blaikie (Origins of the Forty-Five), Elcho and Murray of Broughton for Marischal + Dunkirk/6000, then order SP 36/74/1/60-62 and SP 36/78/1/41-44 together; ~USD 1 for the search.

## While waiting

Run the SP 106 (Deciphering Branch) Discovery search for Nov 1745 [done 6 Oct 2026 R8-SPS1: no Ball/Marischal record] and the three unread editions above; none depends on the copy order.

## R8-SPS1 (a): SP 106 Deciphering Branch search for Nov 1745 (6 Oct 2026, 04:2x UTC)

Intake gate: `open (line 1)`. TNA Discovery API (`API/search/records`, series SP 106, 9 requests, 2 s apart, all HTTP 200). Terms Marischal, Mareschal, Dunkirk, 6000, Ball, Scotland: 0 records each (also 0 with a Oct 1745-Jan 1746 date window). `cipher` 14 and `decipher` 22 records in SP 106; 1745 items only: SP 106/23 and /25 (cipher, Keene and Villettes, printed), /24 and /26 (decipher / French decipher, printed), /41 (cipher in manuscript, French, 18th c.), /44-/46 ("Duplicate of Cipher"). None names Ball, Marischal or any Scottish/Jacobite correspondent. Found: no SP 106 record for this item. Not found is a search result only (Discovery indexes descriptions, not the content of the printed sheets; SP 106/44-46 and /41 undescribed beyond those words). Rule 10: no novelty claim. Next, unchanged: copy order SP 36/74/1/60-62 (REQUEST.md); Blaikie/Elcho/Murray of Broughton IA full text. Host requests: discovery.nationalarchives.gov.uk 9.
