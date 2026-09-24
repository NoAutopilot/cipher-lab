open

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

**Real but only generically realized.** The 1745 Rising is, as the QUEUE row itself flags, one of the most
heavily published episodes in British history, and Blaikie's own edition already prints "Burnet" as the
Prince's standard cipher alias — so the code-name convention is not new. But this sweep found no printed
source that reproduces or discusses the actual ciphertext of SP 54/25/5 or SP 54/25/8B, or MacLean's specific
seizure, in any of the named works actually read (Blaikie's *Origins*). The two largest named sources (*The
Lyon in Mourning*, HMC *Stuart Papers*) remain unchecked.

## Verdict

**Open, stage 2 verified unsolved (conditional: *The Lyon in Mourning*, HMC *Stuart Papers*, Blaikie's
*Itinerary*, and Browne's *History* not read this sweep).** Not "new"; not "unpublished" (rule 10) — a search
result, not a discovery. Closed-negative on DECODE, Bourdeau and Aymeloglu.

Requests: archive.org 2 (Origins of the Forty-Five metadata + djvu text). 2 WebSearch queries this target
(3 counting the George Blaw check). github.com clone shared across this session's four targets (see
sp35-townshend-key-1719/NOTES.md).

## Next

Read *The Lyon in Mourning* (Forbes) and HMC *Stuart Papers* by date/name for MacLean's June 1745 arrest and
these two items specifically before treating as unread — both are large, so a targeted full-text search
(archive.org fts or a downloaded djvu grep) rather than a cover-to-cover read is the efficient route. Not
digitised on Discovery (per QUEUE row); TNA page-copy order is the fallback if the print check above closes
negative.
