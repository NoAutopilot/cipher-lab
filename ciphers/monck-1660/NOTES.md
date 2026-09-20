# Letter partly in cipher relating to Gen. Monck, 1659-1660 (BL Add MS 32093 f.423, Malet collection)

- **Status:** open.
- **Plaintext language:** English, near-certain. The catalogue's own item description is in English with
  English names ("Gen. Monck"), the volume is otherwise English state papers by this date, and the adjacent
  items (ff. 421-424+) are English-language letters among Hyde, Sydney, Whitelocke and Winchilsea.
- **Ciphertext:** none transcribed. No digital image is online (BL's manuscript viewer has been offline since
  the 2023 cyber attack; this record's own "Digitised Content" facet is "No"). A copy must be requested; see
  `REQUEST.md`.

## What the catalogue says (BL Archives and Manuscripts Catalogue, checked 20 Sept 2026)

Source: https://searcharchives.bl.uk/catalog/040-002025830 (item record); parent
https://searcharchives.bl.uk/catalog/032-002025827. This is the BL's beta "interim" catalogue, which the site's
own banner says "contains catalogue records created before October 2023" and cannot list newly catalogued
items for now — it was reachable directly by curl with a browser user-agent, unlike the manuscripts viewer.

Parent collection, shelfmark Add MS 32091-32096, title verbatim: "STATE PAPERS, historical documents, and
official and private letters from 1086-7 to 1760; formerly belonging to the family of Malet, Baronets, of
Wilbury, co. Wilts., and chiefly collected by Sir John Malet, M.P. temp. Chas. II. Interspersed are also papers
collected by George Harbin... In six volumes. Vol. I. (ff. 279); 1087-1575. Vol. II. (ff. 333); 1576-1624.
Vol. III. (ff. 423); 1625-May, 1660. Vol. IV. (ff. 420) July, 1660-1676. Vol. V. (ff. 415) 1677-1697.
Vol. VI. (ff. 364); 1700-1762. The collection was described for the Historical MSS. Commission, 1876, 1879
(App. 5th Report pp.308-320; App. 7th Report pp.428-433)." Add MS 32093 = Vol. III (ff. 423, dated 1625-May
1660): one continuous volume, French religious/diplomatic material at the start, English state correspondence
later. (A stray web snippet calling this "1635-40" is unreliable and contradicted by the catalogue record.)

Item entry, quoted verbatim: **"113. Letter partly in cipher, undeciphered, relating, apparently to
Gen. Monck and his movements in 1659 and 1660. Imperfect. f. 423."** — immediately preceded by item 112, "Sir
Edw[ard] Hyde [Lord Chancellor, afterwards 1st Earl of Clarendon], to [Heneage Finch, 2nd] Earl of Winchilsea;
Breda, 23 May, 1660... f. 421." The index confirms both "Monck, George, 1st Duke of Albemarle, army officer,
1608-1670" and "Malet, John, alias Mallet; of Poynington, county Somerset" as names on this volume. "Imperfect"
suggests possible physical damage worth seeing before transcription starts.

BL access (checked 20 Sept 2026, bl.libguides.com): a Reader Pass issued after 21 March 2024 is needed to
consult the item in person; requests go through an online form (max 4 Western-MS requests active at once,
submit up to 28 days ahead). For a reproduction without a visit, bl.libguides.com/copyright/copying-at-the-british-library
says readers "may order hi-resolution digitisations from" BL Imaging Services with "a service fee to cover the
costs," but no fixed price is published online — expect an email/quote-based request. See `REQUEST.md`.

## Search before solving (CLAUDE.md rule 1), 20 Sept 2026

1. **Search engine.** "Add MS 32093" Malet Monck cipher, "32093" Malet Monck cipher undeciphered, "Add. 32093"
   Monck cipher: no hits referencing this item outside the BL catalogue itself. Nothing found.
2. **Printed correspondence.** Thurloe State Papers vol. 7 (british-history.ac.uk, Feb-Nov 1659) contains
   Monck/Clarges correspondence of this period and is fully digitised/searchable; the Calendar of Clarendon
   State Papers (Bodleian, ed. Macray), vol. 4 covers 1657-1660. Neither was searched page-by-page or
   full-text for a decipherment of this specific item — only a keyword web search was run, which is weak for
   19th-century-printed calendar text that is not fully OCR'd/indexed. **Not checked**: the Historical MSS
   Commission's own 1876/1879 description of this collection (5th Report pp.308-320, 7th Report pp.428-433) —
   an 1870s report predates modern digitisation and, per rule 10's Eckert 1864 lesson, is exactly the kind of
   sender/collection-specific edition that a plain web search misses. This is the first thing to check before
   treating this as unsolved for solving purposes.
3. **Community lists.** Grepped `sources/cryptiana/web/unsolved.htm` for "32093" and "Malet": zero matches;
   this item is not on Tomokiyo's list under either name. The same file lists a related but distinct item,
   "Undeciphered Superscription by Hyde (1659-1660)" (marked "Solved (as Nulls)"), citing BL Add MS 4166
   ff.92-93, a separate 1 Nov 1659 Hyde intercept with clear superscriptions "For the Lord General Monk" — this
   confirms Monck material of the same period circulated in cipher/code contexts elsewhere, but is not this
   item. See `ciphers/whitworth-1707/` for the adjacent period's other cipher work, and
   Bourdeau's `hyde/` folder below.
4. **Cipherbrain / Cipher Mysteries.** No relevant hits for "Monck cipher letter" beyond generic top-50 lists.
5. **DECODE.** de-crypt.org is reachable but a web search "site:de-crypt.org Monck" and "\"Add. 32093\" Monck
   cipher" returned no relevant record IDs. **Not logged in or browsed directly** — out of scope for this
   scouting pass; a future worker with a DECODE login should check.
6. **Solver repositories.** Grepped `/tmp/cyphersolver` and `/tmp/unsolved-ciphers` (shallow clones, 20 Sept
   2026) for monck|monk|32093|malet|clarges: no hit for this item in either repository. Bourdeau's repo does
   have an adjacent, already-solved target, `hyde/` ("Hyde's undeciphered superscriptions," Brussels
   1659-1660, solved as nulls per the 1724 Barwick-Life editor's note) — a different letter, different
   shelfmark (not BL: sourced from Peter Barwick's *Vita Johannis Barwick*, 1721/1724), same correspondent
   (Hyde) and years, whose key names both Monck and Clarges (see Key leads below).

**Confidence that this is not already published: moderate, not high** — three checks remain: the HMC 5th/7th
Report pages, a full-text pass of Thurloe vol. 7 and the Clarendon calendar, and a direct DECODE login/browse.
Per rule 10, "not found by the searches logged above" is the only claim this sweep supports.

## Key leads

- **Hyde-Barwick cipher key** ("THE=370"), a full 643-entry nomenclator (numbers 1-692: letters, syllables,
  words), transcribed from the engraved "Tabula Cryptographica" facing p.316 of Peter Barwick's *Vita Johannis
  Barwick* (London 1721; archive.org id `bim_eighteenth-century_vita-johannis-barwick-s_barwick-peter_1721`),
  reproduced at `/tmp/cyphersolver/hyde/barwick_key.py` (Bourdeau, MIT). Relevant entries: 589 "Hyde Lord
  Chancellor", 600 "Monke Lieutenant Gen.", 637 "Clarges Dr", 572 "Barwick", 573 "Council", 608 "Parliament",
  579/580 "England"/"English". This key was used between Hyde and Barwick in exactly 1659-60 and names both
  Monck and Clarges; Bourdeau's own tests show it does **not** decode the four Hyde superscriptions (those are
  deliberate nulls per contemporary editorial testimony), but it has **not** been tried against this letter.
  Once a transcription exists, this is the first key to test — a same-correspondent, same-period key already
  built is exactly the "sibling in the same circle" pattern `LESSONS.md` calls the most productive single move.
- Thurloe State Papers vol. 7 (british-history.ac.uk/thurloe-papers/vol7): fully digitised, worth a targeted
  phrase/date search once the plaintext or ciphertext content gives something to search on.
- Calendar of the Clarendon State Papers (Bodleian, ed. Macray), vol. 4 (1657-1660): available on archive.org;
  not yet checked page-by-page for a Monck cipher/key entry.
- Bodleian Archives & Manuscripts "Clarendon State Papers" collection page
  (archives.bodleian.ox.ac.uk/repositories/2/resources/7567): not yet fetched; may hold a key alongside Hyde's
  outgoing letters of this period.

## Ideas

This is a Restoration-crux document: Monck's "movements in 1659 and 1660" cover his march from Scotland to
London (Jan-Feb 1660) that precipitated the Restoration of Charles II, so the content is a decision-of-state
letter, not a routine dispatch. Get the image first (catalogue says "Imperfect" — check what survives), then
test the Hyde-Barwick key before any fresh cryptanalysis.
