found-solved
Wheatstone's 1862 published decipherment (Philobiblon Society *Miscellanies*, read in full by this worker via
*The Scientific Papers of Sir Charles Wheatstone*, archive.org id `the-scientific-papers-of-sir-charles-wheatstone`,
pp.321-330) matches BL Add MS 6912's own catalogue record (`searcharchives.bl.uk/catalog/032-003442981`, read in
full) on physical description, date range and acquisition mode — a strong circumstantial identification (the
pamphlet itself states no shelfmark), not a documentary certainty.

## Check-solved (LANE CX, 25 Sept 2026) — Wheatstone match resolved: found-solved

The prior sweep (24 Sept 2026, below) found Wheatstone's 1862 pamphlet but could not confirm it was Add MS 6912
specifically, because neither the pamphlet nor the *Notes and Queries* bibliography entry gives a shelfmark. This
pass fetched the pamphlet's own full text and the BL's individual catalogue record (not just the QUEUE row's
truncated quote) and compared them point by point:

1. **The pamphlet itself, read in full.** Fetched
   `ia600901.us.archive.org/9/items/the-scientific-papers-of-sir-charles-wheatstone/...djvu.txt` (1 request; this
   volume of Wheatstone's collected scientific papers reprints the 1862 Philobiblon Society piece complete,
   pp.321-330, found via `be-api.us.archive.org/fts/v1/search?q="pour le Sieur de Goffe"`, which also returned the
   *Notes and Queries* 1877 bibliography hit from the prior pass among 15 total hits). It contains Sir Henry
   Ellis's covering letter of 1 June 1858 to Wheatstone, quoted verbatim: "A good many years ago the Trustees of
   the British Museum purchased, at a large price, what appeared, and no doubt must be, a very important document
   in cipher; occupying seven folio pages closely filled with numerals; every page signed at top by King Charles
   the First, and countersigned below by Lord Digbye." The deciphered text itself is headed "INSTRUCTIONS POUR LE
   SIEUR DE GOFFE" and concerns "le marriage du prince et la princesse" — i.e. the 1641 marriage of Prince William
   of Orange to Princess Mary, Charles I's daughter — addressed to the agent Stephen Goffe for delivery to the
   Prince of Orange.
2. **BL's individual catalogue record, read in full** (not just QUEUE's truncated quote): fetched
   `searcharchives.bl.uk/?q=Add+MS+6912&search_field=all_fields&format=json` then
   `searcharchives.bl.uk/catalog/032-003442981.json` (2 requests). Fields, quoted verbatim: `scope_and_content_tsi`
   "Long original paper in cypher, signed by King Charles I, and countersigned by George, Lord Digby, on every
   page. It has originally been indorsed 'Instructions for Digbie'."; `date_range_tsi` "1640s" (`start_date_tsi`
   1640, `end_date_tsi` 1649); `extent_tsi` "1 volume (5 folios)"; `source_of_acquisition_tsi` "Purchased in
   18--".
3. **Four points of agreement, none individually conclusive, jointly strong:**
   - Physical description is essentially verbatim: "every page signed at top by King Charles the First, and
     countersigned below by Lord Digbye" (Ellis, 1858) vs "signed by King Charles I, and countersigned by George,
     Lord Digby, on every page" (BL catalogue). A page-by-page Charles-I-signs/Digby-countersigns pattern is an
     unusual, specific detail unlikely to recur by chance across two different manuscripts.
   - Date range: BL's 1640-1649 bracket squarely contains 1641, the year of the Orange marriage the deciphered
     text is about.
   - Acquisition mode: BL's "Purchased in 18--" matches Ellis's account of a Trustees' purchase "at a large
     price", rather than a gift, bequest or transfer — a distinguishing, not generic, provenance fact.
   - Extent: BL's "5 folios" is compatible with Ellis's "seven folio pages" (a folio has two sides; five folios
     can carry up to ten written pages, so seven written pages fits without contradiction), though this point
     alone would not discriminate a match from a near-miss.
   - Set against this: the pamphlet's own heading names Goffe, and the BL docket names Digby — but these are not
     in tension once read as different things (the docket is who the instructions were entrusted to /
     countersigned by; the enciphered text's own internal heading is who the mission's instructions are for), the
     same resolution the 24 Sept pass already proposed without being able to confirm it.
   - No source read by either pass states the BL shelfmark inside the pamphlet or the *Notes and Queries* entry;
     the identification rests entirely on this multi-point circumstantial match, not a documentary link.
4. **Bruce, *Charles I in 1646* (Camden Society, 1856)**, checked per this batch's job brief: fetched in full
   (`archive.org` id `charlesiinlette00chargoog`, `_djvu.txt`, 1 request) and grepped for cipher/cypher/Digby/
   Goffe (30 hits). This is a **different** correspondence — Charles I's own letters in cipher to Queen Henrietta
   Maria, 1646, deciphered by Bruce's own 19th-century key — with no mention of Goffe, the Orange marriage, or a
   document matching Add MS 6912's description; Digby appears only as a name in the letters' content (recipient
   of instructions elsewhere), not as a countersigning party to any cipher discussed. Ruled out as the relevant
   edition for this item.

**Verdict: found-solved, README class F1** (the plaintext is in print — Wheatstone's 1862 decipherment — but BL's
own catalogue record for Add MS 6912 does not cite it, so the specialist catalogue does not link this manuscript
to its published reading). Not "new"; not "first" (rule 10) — Wheatstone read and published this 164 years before
this sweep, if the identification holds. **What this leaves to hand on:** (a) Wheatstone's full translation and
his numeral-substitution key (letters + a French vocabulary keyed by number, e.g. 320=les/the, 376=pour/for,
474=Angleterre, 495=le roi d'Angleterre) are already in `/tmp/wheatstone_papers.txt` this session (not committed;
pp.321-330 of the archive.org text) and should be transcribed into this folder as a machine-readable key/reading
if the identification is confirmed; (b) a correction to BL's own catalogue record (it cites no published
decipherment) is a contribution in its own right, independent of whether Add MS 6912 is or is not this exact item.
**Confidence and what would raise it to certain:** examining the physical item (or a photograph) against
Wheatstone's plate of the cipher key, or finding the pamphlet's own manuscript source note (the Philobiblon
Society's presentation copies sometimes name the lending institution and shelfmark on a flyleaf not reprinted in
the *Scientific Papers* reprint) would settle it; this worker did not attempt either (out of scope: no images, no
cryptanalysis). A verifier session should treat this as the primary open question before any outward report.

Requests this pass: `archive.org`-family 3 (`be-api.us.archive.org/fts/v1/search`, the Wheatstone scientific-papers
`_djvu.txt`, the Bruce 1856 `_djvu.txt`), `searcharchives.bl.uk` 2 (search + individual record JSON). No
subagents, no images, no logins.

# King Charles I's cipher instructions countersigned by Lord Digby — BL Add MS 6912

QUEUE row: N44 (`QUEUE.md`, "Candidates not on DECODE").

## Source

British Library, Western Manuscripts, **Add MS 6912**. Catalogue text as quoted in QUEUE.md's N44 row: "Long
original paper in cypher, signed by King Charles I, and countersigned by George, Lord Digby, on every page. It
has originally been indorsed instructions for Digbie." A single item, multi-page, page-by-page countersigned.
No decipherment or key mentioned in the BL catalogue record. Not digitised.

## Check-solved sweep, 24 September 2026 — major lead, not yet a confirmed match

**A specific, named, published 1862 decipherment of a Charles-I-in-cipher / Digby-countersigned document
exists and must be checked against this shelfmark before any fresh cryptanalysis is attempted.** Chased down
via the following chain, tightening from vague web-search paraphrase to a primary bibliographic citation:

1. Initial web search for "Add MS 6912" turned up no direct hit, but a search for "Wheatstone deciphered
   Charles I letter cipher Goffe Digby Victorian" surfaced a widely repeated (if unsourced in the search
   snippets themselves) description: a cipher document "comprising seven folio pages of closely written
   numerals, each page initialed at the top by King Charles I and countersigned by Lord Digbye", concerning
   instructions to the royalist agent Dr Stephen Goffe, deciphered by the Victorian physicist Charles
   Wheatstone, written in French, using a numeral-substitution code with a vocabulary of higher numbers (e.g.
   320 = "les/the", 376 = "pour/for", 474 = England, 478 = France, 495 = King of England).
2. Chased the primary citation directly rather than trusting the paraphrase. Fetched
   `archive.org` full-text search (`be-api.us.archive.org/fts/v1/search`) for the phrase "Interpretation of an
   important Historical Document in Cipher" and got a hit in a freely downloadable periodical: *Notes and
   Queries*, 1 Sept 1877, vol. 8 no. 192
   (`ia601502.us.archive.org/28/items/sim_notes-and-queries_1877-09-01_8_192/..._djvu.txt`, fetched 24 Sept
   2026). Quoted verbatim from that page (a bibliography of cryptography works):
   > "Wheatstone, Profr. Interpretation of an important historical Document in Cipher. (Instructions [by
   > Charles I.] pour le Sieur de Goffe.) Philebiblon [sic, Philobiblon] Society, [1]862, 8vo."
3. This confirms a real, findable, already-published 1862 pamphlet (Wheatstone, *Interpretation of an
   important Historical Document in Cipher*, Philobiblon Society, 8vo, 1862 — almost certainly in the
   Philobiblon Society's serial *Miscellanies*, vol. 7, per a separate, less precisely sourced web-search
   result naming that volume and year; the exact volume identifier on archive.org was not located this sweep,
   tried `miscellaniesofthephilobiblon7`/`8`, both empty/non-existent items) — subtitled "Instructions [by
   Charles I] pour le Sieur de Goffe", i.e. French-language ciphered instructions from Charles I concerning
   (addressed to, or about) Stephen Goffe, deciphered and printed in full 164 years ago.
4. **This does not confirm Add MS 6912 is the same document.** The BL catalogue's own endorsement text for
   our shelfmark reads "instructions for Digbie" — naming Digby, not Goffe, as the addressee/subject named on
   the docket. Digby was Principal Secretary of State 1643-1645 and routinely countersigned the King's
   ciphered instructions to various continental agents in that role, so a Digby countersignature does not by
   itself identify the addressee: Wheatstone's 1862 item (to/concerning Goffe) and our Add MS 6912 (endorsed
   "for Digbie") could be the *same* item under two different descriptions across centuries of cataloguing, or
   two *different* letters from the same King's-hand-plus-Digby-countersignature pattern, possibly sharing the
   same cipher system. Neither the BL catalogue snippet nor the *Notes and Queries* bibliography entry gives
   an archive shelfmark for Wheatstone's source document, so this sweep cannot resolve which.
5. **Print, general.** Confirms Digby and Goffe were correspondents in fact: a 1646 pamphlet, *"The Lord
   George Digby's Cabinet and Dr. Goff's Negotiations; together with his Majesties, the Queen's, and the Lord
   Jermin's, and other Letters taken at the Battle of Sherborn"*, printed captured Digby/Goffe correspondence
   from the Civil War (found via the DNB *Goffe, Stephen* article on Wikisource) — a different, earlier (1646,
   in clear or already-broken) publication than Wheatstone's 1862 cipher decipherment, but confirming the
   Digby-Goffe correspondence channel was real and already partly in print by the 1640s.
6. **Community lists.** No Cipherbrain or Cipher Mysteries post found naming this item or Wheatstone's 1862
   pamphlet specifically.
7. **DECODE.** Cached catalogue grepped for "6912" and "digby": no record.
8. **Bourdeau / Aymeloglu.** Fresh shallow clones grepped for "digby" and "6912": no target folder or catalogue
   entry for this item in either repository (the earlier combined grep across both repos for "digby"/"6912"
   matched only incidental word/number coincidences in unrelated files — Voynich results, JSON keys, page
   numbers — checked individually, none is this shelfmark or subject).

## Edition risk

**High and specifically named, not merely generic.** A published 1862 decipherment of a closely matching
document (King's-hand cipher, Digby countersignature on every page, French-language instructions to a named
royalist agent) exists in print. Per LESSONS.md's rule on quoting the identifying sentence before writing
"open": the *Notes and Queries* bibliography entry above is quoted verbatim, but it names Goffe, not Digby, as
the addressee, and gives no shelfmark — so it does not by itself identify Add MS 6912 as "this very letter" in
the sense that rule requires. The match is close enough that this is not treated as a clean "open" without the
caveat below.

## Verdict

**(superseded by the found-solved verdict at the top of this file, LANE CX, 25 Sept 2026 — the Wheatstone
identification this section calls "a check this sweep could not complete" was completed in that pass.)**

**Open, stage 2 verified unsolved (conditional on a check this sweep could not complete): whether BL Add MS
6912 is the same document Wheatstone deciphered and published in 1862, or a sibling in the same
King's-hand/Digby-countersigned cipher family.** Not "new"; not "unpublished" (rule 10) regardless of how that
check resolves. Closed-negative on DECODE, Bourdeau and Aymeloglu specifically for this shelfmark.

Not digitised (per QUEUE row). No REQUEST.md drafted — a reading-room request for this item now, before
resolving whether it duplicates an already-published 1862 decipherment, risks wasted archive time; the next
step below should be done first.

Requests: archive.org 3 (be-api.us.archive.org full-text search; the *Notes and Queries* 1877 `_djvu.txt`
fetch; two dead-end metadata probes for a Philobiblon-Society-vol-7 identifier). WebSearch 6 queries chasing
the Wheatstone citation down to its primary source. WebFetch/browser-tool 3 (King's College London Wheatstone
exhibition page, 403 to plain curl and to WebFetch, retrieved via `tools/browser_fetch.js`; two DNB/Wikisource
pages via WebFetch). GitHub 2 shallow clones (shared across this batch's four targets). No BL API calls needed
this sweep (catalogue text already in the QUEUE row). No TNA Discovery, no Google Books slot, no logins, no
subagents.

## Next

1. Locate Wheatstone's 1862 pamphlet itself (Philobiblon Society *Miscellanies*, reportedly vol. 7) on
   archive.org/HathiTrust under its correct identifier, or via the Philobiblon Society's full serial run, and
   read its opening paragraph for the source manuscript's shelfmark or holding institution.
2. If that shelfmark is Add MS 6912 (or a manuscript later renumbered into the Additional Manuscripts series
   at that number), this target reclassifies to found-solved (F0/F1 depending on whether the pamphlet is
   itself the "discovery" or reports an even earlier one) and the reading is Wheatstone's, already 164 years
   in print.
3. If the shelfmark differs, Add MS 6912 remains open but Wheatstone's 1862 key/method (numeral vocabulary,
   e.g. 320="les/the", 376="pour/for", place/person codes) is the first thing to try against it before fresh
   cryptanalysis, since both are King Charles I's own cipher hand with a Digby countersignature and may share
   a system.
