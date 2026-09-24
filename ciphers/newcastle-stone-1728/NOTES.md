open

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
