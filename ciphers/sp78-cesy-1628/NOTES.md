open

# Louis XIII to the Marquis de Cesy, ambassador at Constantinople — TNA SP 78/83/62

QUEUE row: N34 (sources/solver-diffs/2026-09-23-non-decode-hits.tsv, "Candidates not on DECODE").

## Source

The National Archives, Kew, **SP 78/83/62** (State Papers Foreign, France), folio 147, 1628 Aug 31/Sept 10.
TNA Discovery's own catalogue description (already in QUEUE.md/the TSV, not re-fetched this pass — the
Discovery API was not called): "Folio 147: Louis XIII to Cesy, partly in cipher." Philippe de Harlay, comte
de Cesy, was French ambassador to the Ottoman Porte at Constantinople from 1619 to c.1631/32.

## Check-solved sweep (24 September 2026)

Six sources checked (as a Sonnet subagent under this worker's $10 cap; TNA Discovery API not called this
pass, per this run's host rules — the catalogue text above is already in hand).

1. **Editions, printed correspondence of Cesy and of Louis XIII.**
   - Eugène and Jules Halphen, *Lettres inédites du roi Louis XIII à monsieur de Cesy, ambassadeur de France
     à Constantinople, du 28 janvier 1631 au 14 avril 1639* (1904), on Gallica (ark:/12148/bpt6k5758477g —
     not fetched, out of scope for this lane). Its stated coverage, **28 Jan 1631 to 14 Apr 1639**, excludes
     our item (1628 Aug 31/Sept 10) entirely by date. Not found digitised on Internet Archive by title
     search (`title:(Lettres inédites du roi Louis XIII Cesy)`, `title:(Louis XIII Cesy)` — both zero
     results), so its introduction/appendix (which might reach back before Jan 1631) was not checked.
   - Avenel's edition of Richelieu, *Lettres, instructions et papiers d'état* (8 vols, 1853-77), vol. 3
     (1628-1630, archive.org id `lettresinstructi03richuoft`), full-text-searched via
     `be-api.us.archive.org/fts/v1/search?q=Cesy&identifier=lettresinstructi03richuoft`: one matching volume,
     three highlight snippets returned — "A M. DE CESY, AMBASSADEUR, À CONSTANTINOPLE. 9 mars 1629"; an
     unrelated fragment about "mademoiselle de Cesy"; "Lettre à M. de Cesy, ambassadeur à Constantinople". All
     are letters **from Richelieu**, not Louis XIII, and the one dated sample (9 March 1629) does not match
     our item's date (Aug/Sept 1628). Per CLAUDE.md's caveat, the fts API's `page_num` is not a real locator
     and this was not an exhaustive read of the volume's every "Cesy" occurrence — a partial check, not a
     clearance of the whole volume.
   - Google Books queries pending (this worker does not hold the Google Books slot): `site:books.google.com
     "Cesy" "1628"`; `intitle:"Lettres, instructions" Richelieu Avenel Cesy 1628`; `"Cesy" "31 août 1628" OR
     "10 septembre 1628"`; `"monsieur de Cesy" "1628" chiffre`.

2. **Tomokiyo (sources/cryptiana/).** `sources/cryptiana/web/louisxiii.htm` ("French Ciphers during the Reign
   of Louis XIII") has a section "Ambassadors in Constantinople" describing Cesy's ciphers, quoted verbatim:
   "The Cesy-Coeuvres Cipher was used by d'Estrees (Coeuvres), Cardinal de Sourdis, and Sillery in Rome in
   1620-1623 in writing to Cesy, Ambassador in Constantinople. Sillery (and Bethune) used another cipher
   (Cesy-Sillery Cipher) in writing to Cesy in 1624." Both ciphers are BnF fr.16149/fr.16151, correspondents
   writing *to* Cesy (never Louis XIII himself), and cover only 1619-1624 — nothing past 1624, nothing about
   TNA or SP 78. The companion post "More Ciphers from Louis XIII's Time"
   (cryptiana.blogspot.com/2020/09/more-ciphers-from-louis-xiiis-time.html, fetched live) has no mention of
   Cesy or Constantinople at all.

3. **Community lists.** Web search for "Cesy Constantinople cipher unsolved cryptiana OR cipherbrain" and
   "SP 78/83 cipher Louis XIII Cesy National Archives" found nothing specific to this item. One TNA
   Collection Blog post surfaced, "Hidden in plain sight: an undeciphered letter from Louis XIV's France" —
   **Louis XIV**, a different reign, not this target; noted here so it is not confused with SP 78/83/62. No
   Cipherbrain post names Cesy or SP 78/83.

4. **DECODE (de-crypt.org).** Login not attempted (known broken). Public/cached material in this repo
   (`sources/cryptiana/web/decode20.htm`, the solver-diffs TSVs) greped for "Cesy"/"SP 78": the only hit is
   this project's own QUEUE-derived catalogue row, i.e. no DECODE record for this item found in the cache.

5. **Solver repositories.** Fresh shallow clones of both. `dbourdeau/cyphersolver`: no target folder or
   catalogue entry for "Cesy"; the only incidental hits are inside a cached mirror of the same Tomokiyo page
   (`gallica_siblings/src/louisxiii.htm`) and unrelated files; zero hits combining "SP 78" with
   Cesy/Constantinople/1628. `aaymeloglu/unsolved-ciphers`: zero matches for "cesy" anywhere in the tree,
   including its DECODE catalogue caches. Neither repository has picked this item up.

6. **General web search.** Several French- and English-language queries on Cesy's embassy and its ciphers
   turned up the BnF Cesy papers series (fr.16149-16164, Gallica — out of scope) and academic literature on
   the Cesy embassy (e.g. a Cairn.info piece on 1620-1638) with no cipher content, and nothing naming this
   specific letter or SP 78/83/62.

**Host requests this pass:** archive.org (advancedsearch + be-api fts) 4, WebSearch 6 queries, WebFetch 1
(cryptiana.blogspot.com). No TNA Discovery API calls, no Gallica/archivesetmanuscrits fetches, no Google
Books API calls, no DECODE login attempt.

## Verdict

**Status: open.** Nothing above places a decipherment, a solution attempt, or even a prior sighting of this
specific letter (TNA SP 78/83/62 f.147, Louis XIII to Cesy, 1628 Aug 31/Sept 10) in any of the six sources
checked. The one identified published edition of Louis XIII's letters to Cesy (Halphen & Halphen 1904)
excludes this item by date (its coverage starts over two years later, Jan 1631); Avenel's Richelieu vol. 3
covers the right years but the samples returned are letters from Richelieu, not the king, and do not match
this date; Tomokiyo's detailed page on Cesy's ciphers covers only 1619-1624 material in a different archive
(BnF, not TNA) and never reaches 1628; neither solver repository has touched this item.

This does not clear the Halphen edition's own introduction/front matter (not digitised where checked) or an
exhaustive read of Avenel vol. 3 beyond the fts API's three samples — both remain caveats, not closed
questions.

**Copy status:** no online image of TNA SP 78/83 f.147 was located this pass (the Discovery API, which would
show digitisation status, was not queried under this run's host rules). Likely needs a **TNA page-copy
order** for f.147 — see REQUEST.md.

**GB queries pending:** `site:books.google.com "Cesy" "1628"`; `intitle:"Lettres, instructions" Richelieu
Avenel Cesy 1628`; `"Cesy" "31 août 1628" OR "10 septembre 1628"`; `"monsieur de Cesy" "1628" chiffre`.

**Recommended next step:** confirm digitisation status via TNA Discovery (not run this pass); if undigitised,
order a page copy of f.147 (REQUEST.md); separately, check whether the Halphen 1904 edition's introduction
reaches back before Jan 1631 (would need the Gallica copy, out of this lane's scope, or an Internet
Archive/HathiTrust copy if one surfaces).
