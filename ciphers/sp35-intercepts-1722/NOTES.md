found-solved

# 1722 domestic intercepts, Jacobite aliases "Mr Burton" / "Madame Lucy" / "Jery" — TNA SP 35/36/34-37

QUEUE row: N2 (sources/solver-diffs/2026-09-23-non-decode-hits.tsv, "Candidates not on DECODE").

## Source

TNA Discovery, **SP 35/36/34-37** (former refs H34-H37), Secretaries of State: State Papers Domestic,
George I. Full catalogue text, quoted verbatim from the TNA Discovery API
(`discovery.nationalarchives.gov.uk/API/search/records`, record ids C15416370-C15416373, fetched 24
September 2026):

> **SP 35/36/34** (H34): "Copy of cipher and cipher-key, enclosed in a cover to Mrs Burton at Mrs
> Whitten's house, Great Ryder Street, St James's [London, Middlesex]. Endorsed 'the original key was writ
> by the same person who frequently writes to Mrs Burton and who has been writ to from London and
> directed to by the name of Hooker'. With two further copies of the same."
>
> **SP 35/36/35** (H35): "Copy of cipher-key in French, directed to Mr Burton. With two further copies of
> the same."
>
> **SP 35/36/36** (H36): "Copy of cipher-key in French, directed to Mr Burton. With two further copies of
> the same."
>
> **SP 35/36/37** (H37): "Copy of cipher-key and cipher with Mr Farmer and Jery, enclosed under a blank
> cover to Mr Burton. With two further copies of the same."

Each record's `"context"` field (same API response) reads: **"Secretaries of State: State Papers Domestic,
George I. Papers relating to the Atterbury Plot (SP 35/35-39 and SP 35/71-72)."** — TNA's own catalogue
places this exact cluster inside the Atterbury Plot papers, confirming the QUEUE row's inference.

## Check-solved sweep (24 September 2026)

1. **Web search.** "Atterbury Plot Mr Burton Madame Lucy Jery cipher key 1722" and "Cipherbrain Atterbury
   Plot SP 35/36 1722" (WebSearch): no dedicated blog post found, but one result (a WebSearch synthesis of
   TNA's own listing) states as background: "Much of the correspondence in this subseries consists of
   copies taken by a 'secret department' of the Post Office... Some correspondence was written in cipher
   and decoded by decipherers" — TNA's own series-level description for SP 35/35-39, i.e. this whole
   cluster was routinely deciphered by the government at the time, which is why most of the neighbouring
   items (H1-H33, fetched in full below) already read as plain-English "Extract from..." summaries in the
   catalogue rather than as opaque cipher.
2. **Print — the decisive finding.** `sources/cryptiana/web/davys_e.htm` (already in the local snapshot,
   about John Davys's 1737 *Essay on the Art of Decyphering*) links to a dedicated Cryptiana page,
   `atterbury.htm`, not yet mirrored locally. Fetched it directly
   (`cryptiana.web.fc2.com/code/atterbury.htm`, 1 request): it has **individual sections and page images
   for H.34, H.35, H.36 and H.37 by name** ("H.34 Cipher enclosed to Mr Burton (p.329)", "H.35/H.36/H.37
   Cipher directed to Mr Burton (p.330)"), reproducing and analysing the cipher alphabets and code-number
   lists in each (e.g. H.34 "distinguishes slashed digits... 21-24 designate l, k, j, h... with a slash o,
   p, q, r"; H.37 "marked 'A Key and Cipher, with Mr. Farmer and Jery'... probably a cipher between the
   Pretender and Jernegan"). The page's References section cites these images to **"Reports from
   Committees of the House of Commons, Vol. 1 (1803)"** (Appendix H, pp. 329-330), with two Google Books
   scan links, and to **"A Complete Collection of State Trials, Vol. 6 (1730)... Vol. 16 (1816)"**. In
   other words: the H34-H37 key material itself was printed as a parliamentary appendix in 1723
   (reprinted 1803) and has already been transcribed, imaged and analysed on Cryptiana — exactly the
   "printed at trial" edition risk the brief named. Separately fetched the djvu text of *Cobbett's
   Complete Collection of State Trials*, Vol. 16 (archive.org `10394025bsb`, 1812 printing, 1 metadata +
   1 djvu request) and confirmed it contains the Layer/Plunkett/Atterbury proceedings (246 cipher/cypher
   mentions) discussing a different cipher, keyed to code names "Simmonds", "Timothy", "the Pretender" —
   not "Burton"/"Lucy"/"Jery" (0 hits for either alias in that volume): the printed trial cipher discussion
   is a different correspondent's key from the same Atterbury investigation, consistent with Cryptiana's
   attribution of H.34-H.37 to the separate "Mr Burton" surveillance channel, printed instead in the
   Commons committee report rather than at trial.
3. **Community lists.** Cryptiana: see above — a dedicated page exists and already covers this exact
   shelfmark cluster by name and page image. `sources/cryptiana/` also grepped for
   "burton"/"atterbury"/"jacobite": hits in `charlesi.htm`, `davys_e.htm`, `unsolved.htm`, `crypto.htm`
   (general Jacobite-cipher context, not this cluster specifically). Cipherbrain: WebSearch turned up no
   dedicated post; not fetched further (no specific URL found to check).
4. **DECODE.** Cached catalogue grepped for "SP 35"/"Burton"/"Atterbury": no hit. `site:de-crypt.org`
   web search for the same: no hit. This domestic-surveillance material is not on DECODE.
5. **Bourdeau.** `cs-recheck/CATALOGUE.md` etc. grepped for "SP 35/36", "Burton", "Atterbury": no direct
   hit (a few unrelated files matched "burton"/"atterbury" as substrings of other names/text).
6. **Aymeloglu.** `ay/CATALOGUE.md` etc. grepped for the same: no hit.

Requests: discovery.nationalarchives.gov.uk 3 (1 failed 500 on a malformed filter, retried successfully;
1 full SP 35/36 item-level fetch, 40 records, 1 request; 1 "decipher" cross-series search), archive.org
family 2 (metadata + djvu for State Trials Vol. 16), cryptiana.web.fc2.com 1. 12 WebSearch queries shared
across all three targets this session (see mornington-1798/NOTES.md and courten-diary/NOTES.md).

## Edition risk

**Realized.** The cipher-key material for exactly this cluster (H.34-H.37 = SP 35/36/34-37) was printed
as Appendix H of the 1723 House of Commons committee report on the Atterbury Plot, reprinted in *Reports
from Committees of the House of Commons*, Vol. 1 (1803), and has already been transcribed, imaged and
analysed section-by-section on Cryptiana (Tomokiyo), citing page numbers (pp. 329-330) and two separate
Google Books scans. This is not a case of "the key sits unused nearby" — the key has been in print for
three hundred years and in a specialist cryptology writer's published analysis for at least as long as
that Cryptiana page has existed. The associated surveillance letters (H1-H33) also already carry
plain-English catalogue summaries, consistent with TNA's own note that this subseries was "decoded by
decipherers" at the time.

## Verdict

**Found-solved — not a recovery target.** Not "new"; not "unpublished" (rule 10): the cipher tables for
SP 35/36/34-37 are already published (1723/1803 parliamentary report) and already described and imaged on
Cryptiana. Whether every individual surveillance letter in the same box (H1-H33) has been matched
letter-by-letter to this key by a modern solver is a narrower, much lower-value question the check-solved
sweep did not chase further, since the premise of the QUEUE row — an unused key next to unread cipher —
does not hold for this cluster.

## Next

Drop this cluster from the board; it does not need an access route. If anyone wants to follow up, the
narrower open question is whether a named modern researcher has run the Cryptiana-transcribed key against
each of H1-H33 individually (as opposed to just the government's contemporary "extract" summaries already
in the catalogue) — that would be a Bourdeau/Aymeloglu-style unique-solve check on a single already-keyed
item, not an access-and-decipher campaign, and does not need BL/TNA imaging to start (Cryptiana's images
of H.34-H.37 plus TNA's own transcribed extracts of H1-H33 may already be enough to attempt it from the
desk).
