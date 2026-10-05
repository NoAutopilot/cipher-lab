found-solved
No cipher in this item: TNA Discovery's own description of SP 36/9/118 (record C8106544, fetched by this worker 3 Oct 2026) gives the note's full text in clear -- Newcastle asking the King whether the Grimaldi paragraph should be "writ in cypher", with the King's answer -- and Coxe's *Memoirs of Sir Robert Walpole* (1800, vols 1-3) and *Memoirs of Horatio, Lord Walpole* (1808, vols 1-2) were grepped whole-volume by this worker (archive.org djvu full text) with no copy of the note.

# Andrew Stone reporting Mr Stanhope and Walpole's private letter to the King — TNA SP 36/9/118

QUEUE row: N47, "Candidates not on DECODE" (N41-N66 block, scoring pass of 24 September 2026). The National
Archives, Kew, SP 36/9/118 (folios 118-119). Catalogue description: "Note from (Newcastle) to the King.
Finding upon a second reading of Mr. Stanhope and Mr. Walpole's private letter..." dated 19 December 1728. The
"Mr Stanhope" is most likely William Stanhope (later 1st Earl of Harrington), envoy to Spain and a Secretary
of State's circle correspondent in this period per the Camden Third Series volume *William Stanhope, later
Lord Harrington, Horatio Walpole, Stephen Poyntz 1728-1730* — not confirmed against the manuscript itself
(TNA Discovery is out of this brief's hosts, so the item's full description was not re-fetched this pass; the
catalogue snippet above is as recorded in `sources/solver-diffs/2026-09-23-non-decode-hits.tsv` row 106 and
`2026-09-24-non-decode-scored.tsv` row 14). Andrew Stone (1703-1773) did not become under-secretary of state
to Newcastle until 1734 per his DNB entry; in December 1728 he would have been an early, informal member of
Newcastle's circle — this note is attributed to Stone in the QUEUE row and TSV, but the exact authorship
relationship is not independently confirmed this pass and is worth checking against the manuscript hand or a
printed calendar before relying on it.

A neighbouring SP 36 item is worth flagging for whoever picks this fonds up next: SP 36/37/44 (14 Nov 1735,
"Andrew Stone to [Newcastle]. The Dutch post brought a letter in cypher from...") is already scored as N65 in
the same non-decode scoring pass — same correspondent, same series, a different year and item, not checked
against this one this pass.

## Editions-first check (24 September 2026)

The brief names William Coxe's *Memoirs of the Life and Administration of Sir Robert Walpole* (1798, 3 vols,
with original correspondence) and HMC reports as the relevant editions. Located on `archive.org`:
`bim_eighteenth-century_memoirs-of-the-life-and-_coxe-william_1798_1` (vol. 1, 1798) and, per WebSearch,
further volumes exist (HathiTrust record `000108542`); Coxe's separate *Memoirs of Horatio, Lord Walpole*
(1802, `archive.org/details/memoirsofhoratio02coxeuoft`) also covers 1678-1757 and specifically the
1728-1730 Stanhope/Walpole/Poyntz correspondence per its own subtitle. Neither volume's full text was searched
this pass for the note's own language ("second reading," "private letter to the King," the 19 December 1728
date) — this is the concrete next step for a print-check worker, via `archive.org`'s be-api full-text search or
`_djvu.txt` on the two identifiers above, before any TNA page-copy order. No HMC report naming Newcastle's
papers for this exact date was identified by title this pass.

## Six-source sweep (24 September 2026)

1. **Web.** Covered above under editions-first; also searched `"SP 36/9/118" OR "Stanhope and Walpole" 1728
   Newcastle King second reading letter` (returned only the catalogue snippet itself, restated by a search
   crawl, and general Andrew Stone/Newcastle biographical material — no prior print or decipherment claimed
   anywhere) and `Andrew Stone Newcastle Stanhope Walpole 1728 cipher letter "SP 36/9"` (same result).
2. **Print.** Coxe's two Walpole memoir volumes are the named candidate editions (see above); neither
   confirmed or ruled out this pass — full text not searched.
3. **Community lists.** `sources/cryptiana/` grepped for "Andrew Stone," "Stanhope," "Newcastle," "Walpole,"
   "SP 36": the only genuine "Stanhope" hits are Philip Stanhope, 2nd Earl of Chesterfield's 1659 enciphered
   memoir passage (`unsolved.htm`, `blog/2022_02_enciphered-passage-about-princess.html`, solved by George
   Lasry in 2022) — a different Stanhope (Chesterfield, not William Stanhope/Harrington), a different century,
   not this item. `charlesi.htm`'s "Stanhope" hit is likewise unrelated 17th-century material. No mention of
   Andrew Stone, Newcastle's 1728 note, or SP 36/9/118 anywhere in the Cryptiana snapshot.
4. **DECODE.** No login attempted (broken, ASKS row 1). Aymeloglu's cached DECODE catalogue grepped for
   "Andrew Stone," "Stanhope," "SP 36/9": no genuine match (a combined-pattern grep surfaced only unrelated
   files whose paths happen to contain the literal substring "decode," e.g. `decode.py` scripts in other
   target folders — noise, not content matches on this item).
5. **Bourdeau's repository.** Fresh shallow clone, 24 Sept 2026 (shared with the rest of this batch). No
   target folder or catalogue mention of "Andrew Stone," "SP 36/9/118," or "Stanhope and Walpole" as this
   1728 item.
6. **Aymeloglu's repository.** Fresh shallow clone, 24 Sept 2026 (shared). No target folder, no README/
   TARGETS/SHORTLIST/CATALOGUE mention. The many "Stanhope" filename hits in this clone (`starhemberg-1758/
   decode.py`, `ottobon-1589/decode.py`, etc.) are all literal matches on the word "decode" in unrelated
   scripts, not on "Stanhope" — false positives from an earlier case-insensitive sweep, checked and ruled out.

**GB queries pending** (no Google Books slot this batch): `"Stanhope and Mr. Walpole's private letter" 1728`;
`Coxe Walpole memoirs 1728 "second reading" Stanhope cipher`; `Andrew Stone Newcastle 1728 December cipher`.

## Verdict

**open**, stage 2 verified unsolved (conditional: Coxe's two 1798/1802 Walpole memoir volumes are named,
readily available editions from exactly this circle and period that have not actually been full-text searched
against this note's own language yet — that is the cheap next step, before any TNA page-copy order). No source
in this sweep identifies, quotes, or describes the content of this note. Highest-weight single item of this
sweep's non-DECODE TNA rows given who is named (Newcastle, Stanhope, Walpole, the King), though the folio
itself is a short note rather than a whole despatch, per the scout's own scoring note.

## Copy status

Not digitised (TNA manuscript; TNA Discovery API is out of this brief's hosts, so `digitised` was not
re-confirmed this pass — the 24 Sept scoring pass's own detail-call sweep records it as false for the
shortlisted TNA pieces of that batch, and this item was not itself among the 14 detail-checked that pass).
REQUEST.md drafted for a TNA page-copy order for f.118-119, per the scout's own next-step note, contingent on
the Coxe full-text check above turning up nothing.

## Request counts (this target)

WebSearch: 4. `archive.org`: 0 (identifiers located by WebSearch only this pass; no full-text fetch made —
left as the next worker's first move). `github.com`: shared shallow clone with the rest of this batch. No TNA
Discovery calls (out of this brief's hosts). No Google Books calls (queries logged above as pending).

queued JSTOR rows, 26 Sept 2026, QUEUE-FILL.

## JSTOR runner, 26 Sept 2026

- `"Andrew Stone" AND Newcastle AND 1728 AND cipher`: no relevant hit (1 result, none about the letter).
- `"Stanhope" AND "Walpole" AND "private letter" AND 1728`: one **candidate, unread, reread needed** (the
  runner's browser was not logged in to JPASS on this run) -- Basil Williams, "The Foreign Policy of England
  under Walpole (Continued)", The English Historical Review 16(62), 1901, pp. 308-327,
  https://www.jstor.org/stable/548655 (blocked: "This is a preview. Log in through your library", whether pp.
  308-327 discuss the 19 December 1728 note could not be determined). Requeued in JSTOR-QUEUE.tsv, not `done`;
  see ASKS.md. Context only, not read: Thompson 2006 (stable/10.7722/j.ctt14brtmp.13), Hatton 2001
  (stable/j.ctt1bh4cbj.15).

## While waiting (27 Sept 2026, WAIT-PASS-B)

Waits on: a TNA page-copy order for SP 36/9/118-119 (REQUEST.md, since the 24 Sept 2026 check-solved sweep,
now folded into the consolidated TNA batch, ASKS row 73) and a JSTOR reread of Williams 1901 (stable/548655,
ASKS row 76, since 26 Sept 2026).

- S: full-text search Coxe's two Walpole memoir volumes (already located, not yet searched) for 'second reading'/19 Dec 1728 -- tools/print_check.py.
- S: run the three pending Google Books queries this NOTES.md already lists ("GB queries pending"), key+country=US, not yet run.
- S: cross-check SP 36/37/44 (14 Nov 1735, same correspondent Andrew Stone, already scored N65) against this item's own content, not compared yet.

## Check-solved re-run (GF4-BATCH13, account-4, 3 Oct 2026)

Gate fix (the verdict lacked a logged web/blog pass; the Coxe full-text search was still undone). Per `.claude/briefs/check-solved.md`.

1. **Holding catalogue, full description (the decisive find).** `tools/discovery_items.py "SP 36" "SP 36/9" "second reading"`
   (TNA Discovery API, 1 request) returned SP 36/9/118, 1728 Dec. 19, id C8106544, description verbatim: "Folios 118-119. Note from
   (Newcastle) to the King. Finding upon a second reading of Mr. Stanhope and Mr. Walpole's private letter, that the intelligence
   about Mons. Grimaldi came from the Sicilian priests and the Auditor de Rota, and that Mr. Walpole desires it may be kept
   secret, I have presumed to mention it only in general terms and proposed to write it in cypher. If your Majesty would have it
   written out in cypher I humbly beg your Majesty will be pleased to honour me with your commands. The King's answer appended.
   The secret being recommended as to what relates to Mr. Grimaldi it will be more proper to have that paragraph writ in
   cypher." The item is a clear note about whether to cipher a paragraph of an outgoing despatch; it carries no ciphertext, and
   its whole text is in the catalogue. The QUEUE row's "Andrew Stone" attribution is not in TNA's description (it reads
   "(Newcastle)"); the 24 Sept notes already doubted it.
2. **Editions (whole-volume grep, archive.org djvu, long-s OCR allowed for: "[sf]econd reading", "Soi[sf][sf]ons").** Coxe,
   *Memoirs of the Life and Administration of Sir Robert Walpole* (1800 ed., `memoirsoflifeadm01coxeuoft`,
   `memoirsoflifeadm02coxeuoft`, `memoirsoflifeadm03coxeuoft`) and Coxe, *Memoirs of Horatio, Lord Walpole* (1808,
   `memoirsofhoratio01coxeuoft`, `memoirsofhoratio02coxeuoft`): queries "second reading" (7 hits, all parliamentary bill
   readings), "private letter" (21 hits, none this note), "Dec. 19"/"December 19" (0), "Grimaldi" not needed after step 1,
   "Andrew Stone"/"Mr. Stone" (7, all 1740s), "Soissons" (8 incl. OCR variants, narrative only). The note is not printed there.
   Not read: the Camden Third Series volume *William Stanhope, later Lord Harrington, Horatio Walpole, Stephen Poyntz
   1728-1730* (Cambridge Core, abstract only seen) -- immaterial here, since the item has no cipher to be printed deciphered.
3. **Google Books API** (`"second reading" Stanhope Walpole "private letter" 1728`, key + country=US): 47 results, none this note
   (History of Parliament, Mahon's History, booksellers' circulars).
4. **Community lists, DECODE, Bourdeau, Aymeloglu:** as 24 Sept, no hit; not re-cloned.

**Verdict: found-solved (F0).** There is nothing to decipher in SP 36/9/118: the note is in clear and its full text, with the
King's answer, is in TNA's own catalogue description. The scout row read "cypher" in the description as a cipher item. The
ciphered paragraph it talks about would sit in Newcastle's outgoing despatch to William Stanhope and Horatio Walpole at the
Congress of Soissons of about 19-20 Dec 1728 (SP 78 or the Newcastle papers in BL Add MSS), a different item not checked here
-- one-line suggestion for a scout, not a step of this folder. REQUEST.md's copy order is moot, and so are this target's
queued JSTOR-QUEUE.tsv rows (left for the parent to waive; not edited here).

Requests: discovery.nationalarchives.gov.uk 2 (one empty "Stanhope" query, one hit; >=2 s apart); archive.org 5 djvu (shared
with the batch, 1.6 s apart); googleapis.com 1; WebSearch 4 + 3 blog-site searches.

## Web and blog check (GF4-BATCH13, account-4, 3 Oct 2026)

- Plain web: `Newcastle to George II 19 December 1728 Grimaldi Stanhope Walpole cypher` (Wikipedia pages, Chesterfield papers at
  OAC, the Camden volume's abstract -- nothing on this note); `"SP 36/9" Newcastle King 1728 cypher` (TNA beta catalogue page
  C8106544 for this item, same clear description as above; sibling SP 36/9 notes C8106550, C8106566); `"intelligence about Mons.
  Grimaldi" OR "Sicilian priests" "Auditor de Rota" 1728` (Grimaldi biographies only); `Andrew Stone Newcastle note to the King
  Stanhope Walpole private letter 1728` (Stone biographies; no item).
- Cipherbrain (site:scienceblogs.de, `Newcastle 1728 Stanhope Walpole letter cipher Andrew Stone`): unrelated posts (Cheltenham
  stones, pigpen) -- no hit.
- Cryptiana (site:cryptiana.blogspot.com / cryptiana.web.fc2.com, `Newcastle Stanhope Walpole 1728 cipher`): no results.
- Cipher Mysteries (site:ciphermysteries.com, same query): Beale, Gentlemen's cipher, d'Agapeyeff -- no hit.
- Result: no blog or comment thread treats the item.

## Premise check (GF4-BATCH13, account-4, 3 Oct 2026)

- (a) Folder's own files: NOTES.md quotes the catalogue snippet "Finding upon a second reading..."; opening the full description
  behind it (step 1 above) shows the item is clear text -- found (the premise that it is a cipher item fails).
- (b) Other solvers' working files: none for this item in Bourdeau or Aymeloglu (24 Sept grep) -- not found.
- (c) Physical neighbours: SP 36/9 is undigitised; the neighbouring catalogue entries are further clear Newcastle-to-King notes
  (C8106550, C8106566, seen only as search titles) -- not opened; no image route.
- (d) Recipient's side: the despatch to Stanhope and H. Walpole (the side where the cypher paragraph went) is a separate item --
  not checked, named in the verdict as a scout suggestion.

## JSTOR runner, 4 Oct 2026

read 4 Oct 2026 (page viewer, no download), Basil Williams 1901 https://www.jstor.org/stable/548655: the only "private letter" match is p.311: "In a private letter of 6 Feb. 1728 the duke [Newcastle] writes to Lord Waldegrave, then at Paris, warning him strongly against Chauvelin" (n.1 Add. MS. 32754, f. 234 as read from the page image); no Stanhope/Walpole letter of 1728 and no cipher mentioned on the matched page
