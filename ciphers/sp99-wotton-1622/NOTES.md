open
Pearsall Smith, Life and Letters of Sir Henry Wotton vol. 2 (1907; archive.org in.ernet.dli.2015.184194, djvu full text) grepped by this worker 2 Oct 2026 for cipher/cypher/159/Nys: 7 cipher hits (the 1622-23 ones on the Calvert letters near pp. 215 and 231), none naming SP 99/24/251 or a correspondent '159'.

# Letter in cipher from "159," Sir Henry Wotton's hand — TNA SP 99/24/251

QUEUE row: N59 (sources/solver-diffs/2026-09-23-non-decode-hits.tsv, "Candidates not on DECODE").

## Source

The National Archives, Kew, **SP 99/24/251** (State Papers Foreign, Venice), folio 251, [?1622] (TNA Discovery,
fetched 24 Sept 2026, id C6915573; `digitised: false` confirmed by direct record fetch; `note` field: "? Wotton's
hand"). Scope content: "Letter in cipher from 159." Sir Henry Wotton was resident ambassador at Venice through
most of 1616-1624 (with breaks), so a Venice-series item catalogued to his hand in 1622 falls squarely in his
third embassy.

## Check-solved sweep (24 September 2026)

1. **Editions.** CSP Venetian calendars documents held *in the Archives of Venice* about English affairs (the
   Venetian ambassadors' own dispatches), not the English out-letters and intercepts held at TNA as SP 99 — so
   it is not the calendar for this collection, and was not pursued further as a source for this specific item
   (WebSearch confirmed CSP Venetian vol. 17, ed. Hinds 1911, covers April 1621-April 1623, but by scope, not
   shelfmark). The one edition that could calendar an SP 99 item directly, Logan Pearsall Smith's *Life and
   Letters of Sir Henry Wotton* (1907, 2 vols), was fetched in full text from archive.org
   (`in.ernet.dli.2015.184194`, vol. 2, covers the Venice years) and grepped: 7 hits for "cipher"/"cypher", none
   naming this item, "159," or SP 99/24; no hit for "159" as a correspondent name. Two footnotes on "Nys"
   confirm **Daniel Nys**, an art-purchasing agent employed by Wotton, Sir Dudley Carleton and Sir Isaac Wake at
   Venice (his major purchase, the Mantua/Gonzaga collection, came later, 1628) — a real Wotton-Venice
   correspondent, but not tied by the text to this cipher letter or to the number "159."
2. **Sibling search (TNA Discovery, same piece).** `tools/discovery_items.py "SP 99" "SP 99/24" decipher` and
   `... 159` return, besides the target, only **SP 99/24/159** itself: "Nys to [Carleton]," 1622 Oct. 25/Nov. 5,
   id C6915544 — a plain (non-cipher) item at folio 159 in the same piece. This does not confirm "159" in the
   cipher letter's description is a folio cross-reference rather than a numeric code-name for a person (both
   readings are possible from the catalogue text alone, and TNA's phrasing "from 159" reads more naturally as a
   correspondent identity than a folio pointer). No decipher, key, or duplicate record for SP 99/24/251 itself
   found in the piece under either search term. Numeric code-names for named persons are independently attested
   for a *different* Wotton (Edward Wotton, ambassador in Scotland, 1585, BL Add MS 32657 — solved by
   dbourdeau/cyphersolver, `wotton1585/`: 19 = Arran, 39 = Master of Gray, 10 = King James), which is suggestive
   of the convention but not evidence for this item or this "Wotton."
3. **Community lists.** WebSearch for "Wotton Venice 1622 correspondent 159 cipher code number intelligence"
   and a second pass on "St Quentin"-style phrasing returned only general Wotton biography (Wikipedia, LRB) and
   Venetian cryptology scholarship (Atlas Obscura, Iordanou 2018) with no mention of this item, "159," or SP
   99/24. Local grep of `sources/cryptiana/` for "wotton": no hits.
4. **DECODE.** No login attempted. `sources/decode/` greped for "159", "Wotton", "SP 99/24", "Venice 1622": the
   "159" hits are unrelated items (BRAH Signatura 9/25, BL Add MS 4136, BL Cotton MS Vespasian C IV, BnF
   Mélanges de Colbert 159) — none Venice, none Wotton.
5. **Solver repositories.** Fresh shallow clones (24 Sept 2026, shared across this pass's four targets).
   `dbourdeau/cyphersolver`: grep for "wotton|SP.?99.?24|159" across the tree surfaces only two *different*
   Wotton items, both read/partly read — Edward Wotton (Scotland) 1585 (`wotton1585/`, catalogue items 81-82,
   read) and Dr Nicholas Wotton 1554 (`harley1582r8499/`, catalogue 120, read in part) — neither is Sir Henry
   Wotton at Venice, and neither is SP 99. `aaymeloglu/unsolved-ciphers`: zero matches.
6. **General web search.** As (1) and (3). No result identifies "159" as a known intelligence code-name tied to
   Wotton's Venice network specifically, nor connects this shelfmark to any published edition or prior attempt.

**Host requests this pass:** discovery.nationalarchives.gov.uk 4 (search x2, record detail x1, >=3s apart,
shared budget with the other three targets this run), archive.org 2 (metadata + full-text fetch of Pearsall
Smith vol. 2), WebSearch 4, github.com 1 shallow clone each of both repos (grepped, shared across all four
targets), sources/decode/ and sources/cryptiana/ local greps (no network).

## Verdict

**Status: open.** No calendar reaches this collection (CSP Venetian calendars the wrong archive; Pearsall
Smith's edition of Wotton's own letters was searched in full and does not name this item or "159"). The
sibling search found a same-piece item at folio 159 ("Nys to [Carleton]") that may or may not explain the
catalogue's "from 159," but no decipher or key for folio 251 itself. No community list, DECODE record, or
solver-repository entry names this item; the two other "Wotton" targets in the solver repos are different
people (Edward Wotton 1585, Nicholas Wotton 1554), already read, and unrelated to this one.

**Update 3 Oct 2026 (A2P4-WOTT):** printed evidence (Pearsall Smith vol. 1 p. 320 n. 1) shows Wotton's 1604 cipher assigned numerals 130-160 to individuals, so "159" as a person code-name is more likely than a folio pointer (grade I). Status stays open: no printed decipherment of this letter found. Next: order f.251 and f.159 (REQUEST.md); read Kerr/modern Wotton biographies; TNA SP 99/25 for numbered-agent lists.

**Copy status:** no online image located; `digitised: false` confirmed by direct record fetch (id C6915573).
**Copy-order.** See REQUEST.md.

**Recommended next steps (not run this pass):** (1) resolve whether "159" in the description is a correspondent
code-name or a folio cross-reference — read folio 159 itself ("Nys to [Carleton]") once ordered, alongside 251;
(2) if a numeric code-name, check whether Wotton's Venice network used a standing numbered-agent list
documented elsewhere in SP 99/24 or SP 99/25 (the following volume); (3) [print lookup done 3 Oct 2026, see "Print lookup" below; Kerr and modern biographies still not reached] Daniel Nys is a real, identifiable
Wotton-Venice correspondent worth checking against Venice-period Wotton scholarship (Logan Pearsall Smith's
notes, or Gordon Kerr / other modern Wotton biographies) not reached under this run's hosts.

## Print lookup: "159" code-name or folio (A2P4-WOTT, 3 Oct 2026)

Intake gate (3 Oct 2026): `python3 tools/intake_gate_check.py sp99-wotton-1622` -> "open (line 1) -- edition/page or full-text-search citation found within 6 lines". No transcription or cryptanalysis was done; print lookup only, no vision calls.

**Sources read, by script (archive.org djvu full text, 2 requests, >=2 s apart):** Pearsall Smith, *Life and Letters of Sir Henry Wotton* vol. 1 (`lifelettersofsir01smituoft`) and vol. 2 (`lifelettersofsir02smituoft`), grepped for `Nys|Nuis|cipher|cypher|numbered|159`.
Positive control per source: both volumes return many known Wotton letters and cipher passages (vol. 1: 32 cipher-line hits; vol. 2: 20), so the grep can see this author's cipher talk.

Evidence found:
1. **Vol. 1, p. 320 n. 1** (letter 52, Wotton to [Salisbury], Dec. 1604, sending a cipher): "The ciphers Wotton used were of simple numerical kind; the vowels had five variants, the consonants two. In his first cipher ... Higher numerals stood for individuals, 130 Philip III, 134 the Pope, 148 the Duke of Savoy, 160 the Papal Nuncio, etc. Numerals below 6 had no meaning. Almost all the dispatches in the Record Office have already been deciphered." Printed, from the editor (no source cited in the note). It is the 1604 cipher, not a 1622 one.
2. **Vol. 2, p. 210** (letter 345, Wotton to Calvert, April 1621): "Daniel Nuis" is named in clear as the conveyer of a postscript ("whose conveyance I use"); n. 1 (the editor): Daniel Nys, agent employed by Wotton, Carleton and Wake to collect pictures, Mantua collection 1628. Vol. 2 p. 258 n. 4 queries "Daniel Nys?" for an unnamed person in a Dec. 1622 letter. In print Nys appears under his own name, never as a number.
3. Vol. 2 also prints new ciphers sent in Sept. 1621 (to Aston) and 1623 (to Donne): the number scheme was reissued, so the 1604 individual-numerals range cannot be assumed for 1622.
4. Vol. 1/2 indexes: cipher *names* printed are Blotius (Ferdinand I), Plese (Burghley), Taxis (Darcy): all word-names from the 1580s-90s, none numeric; no numbered-agent list, no "159" as a person, no SP 99/24 f.251 in either index. Appendices: nothing further under these terms.
5. **Sources not reached:** CSP Venetian vol. 17 (1621-23): not located on IA by two searches (title/creator queries returned other volumes); by scope it calendars the Venetian archive, so it was not pursued further. OpenAlex (3 queries, key header, 1.5 s apart) found nothing on Daniel Nys as intelligencer (one Gonzaga/Mantua query returned two unrelated art-history papers); one 2026 title, "Decoding Conspiratorial Rhetoric in Sir Henry Wotton's Diplomatic Correspondence on the Jesuits" (doi 10.1163/22141332-12340030), is about rhetoric and was not opened. Semantic Scholar answered 429 twice (one pause, no loop); not run. Kerr and other modern biographies: not reached.

**Decision (grade I, inferred; nothing printed states it):** the evidence favours "159" as a numeric code-name for an individual over a folio cross-reference, for two reasons: (a) a printed Wotton cipher gave persons numbers in the 130-160 range (130, 134, 148, 160 attested), so 159 falls in the attested band for individuals; (b) the TNA description's wording "Letter in cipher from 159" plus Pearsall Smith's use of Nys's name in clear for other letters weakens the idea that 159 stands for Nys. Against: the number scheme was reissued in 1621-23 (item 3), and f.159 in the same piece is "Nys to [Carleton]" (Oct. 25/Nov. 5, 1622), so the folio reading is not excluded. Counts: 1 H-grade-adjacent printed statement (item 1, 1604, a different cipher), 0 C, 0 S, 3 I. Not a reading of the target; no key or plaintext exists.

## Web and blog check (GF-A2-6, 2 Oct 2026)

Plain web searches (WebSearch, 2 Oct 2026):
1. `Henry Wotton Venice 1622 cipher letter "159"` -- hits: fadedpage.com (Pearsall Smith e-text), british-history.ac.uk node 75610 (CSP Venetian), Sotheran's sale of *The State of Christendom*, Eton College catalogue, Camden Society chapter on Wotton and Paolo Sarpi, Chalmers' biography. None names this item, SP 99/24/251 or a correspondent "159".
2. `"SP 99/24" cipher Wotton` -- ten TNA catalogue records in SP 99/24 (Wotton to Calvert / Carleton, 1622); none is f.251 and none carries a decipherment.
3. `"Letter in cipher from 159" Wotton` (the catalogue's own wording in quotes) -- no exact hit; only unrelated Wotton items (William Wotton, Donne letters, Huntington, Bodleian, MPESE).
4. `Wotton Venice cipher letter 1622 decipherment Daniel Nys` -- HistoCrypt proceedings papers (liu.se, on Venetian/papal ciphers), Donne Variorum, TNA SP 99/24 records; none about this letter.

Blog site searches:
- Cipherbrain (scienceblogs.de/klausis-krypto-kolumne), `Wotton cipher State Papers Venice` and two follow-ups: only "An unsolved pigpen cipher from Venice" (a ceiling inscription, opened: not this item, no Wotton in post or comments) and unrelated Top-50/Voynich posts.
- Cryptiana (cryptiana.blogspot.com, cryptiana.web.fc2.com), `Wotton 1622 cipher`: no results.
- Cipher Mysteries (ciphermysteries.com), `Henry Wotton cipher`: only unrelated posts (WWI battery cipher, Gentlemen's Cipher, BL cipher manuscript update 2008); none mentions Wotton or SP 99.
Combined three-blog query `Wotton Venice cipher`: same pigpen post plus Voynich posts. No plausible hit for this item, so no comment thread bears on it.

Not found: no decipherment, plaintext or prior attempt for SP 99/24/251 on the open web or in the three blogs' posts and comments.

## Premise check (GF-A2-6, 2 Oct 2026)

(a) Decipherments the folder already mentions: none for this item. The only lead the folder names is f.159 ("Nys to [Carleton]", plain), a possible cross-reference for "from 159"; it is not a decipherment, and no image is online to look. Not found.
(b) Other solvers' working files: fresh shallow clones of dbourdeau/cyphersolver and aaymeloglu/unsolved-ciphers (2 Oct 2026) grepped for `wotton`, `SP.?99.?24`: Bourdeau's hits are the Edward Wotton 1585 (Scotland) and Nicholas Wotton 1554 targets and catalogue-harvest rows for them -- different people, different keys; Aymeloglu's tree has none (cited, not copied). No key of theirs has been run on this text. Not found.
(c) Physical neighbours: no image online (`digitised: false`), so the leaves either side of f.251 and any facing page or slip cannot be viewed -- unreachable. TNA Discovery (tools/discovery_items.py "SP 99" "SP 99/24" Wotton 1622, 2 Oct 2026) lists 24 Wotton letters in the piece up to f.195 (to Calvert, Carleton, Arundel); none is catalogued "with decipher" and none sits beside f.251. Catalogue neighbours: not found; images: unreachable.
(d) Recipient side: the letter's addressee is not stated; Wotton's 1622 recipients in this piece are Calvert and Carleton, whose own edited sides are CSP Domestic James I 1619-23 (calendars SP 14, not SP 99) and Pearsall Smith vol. 2 (read above). Pearsall Smith prints no letter from or to "159". A Venice-side source (CSP Venetian vol. 17, 1621-23) calendars the Venetian archive, not this English leaf. Not found in what was read; CSP Domestic 1619-23 not searched this pass.

## Folio 159 question: catalogue evidence (D2B-WOTT, 5 Oct 2026)

Job: NOTES.md recommended step (1), resolve whether "159" is a correspondent designation or a folio cross-reference, from the TNA
Discovery API (no decoding, no images: both leaves are `digitised: false`). Requests: discovery.nationalarchives.gov.uk 7 (2 details,
1 children listing of the piece, 4 series searches; one at a time, >=2 s apart, all HTTP 200); archive.org 1 (Pearsall Smith vol. 2
djvu text, `lifelettersofsir02smituoft`). Fetched 5 Oct 2026, 23:52-23:55 UTC by date -u.

1. **Details records.** SP 99/24/251 (C6915573): description "Letter in cipher from 159.", note "? Wotton's hand", date "[? 1622]",
   parent C3666170; `physicalDescription`, `relatedMaterials`, `publications`, `unpublishedFinding`, former references all null.
   SP 99/24/159 (C6915544): "Nys to [Carleton].", 1622 Oct. 25/Nov. 5, note null, no cross-reference fields. Neither record points
   at the other.
2. **The whole piece (children of C3666170, 105 items, one listing).** Folio 159 is one of a run of Nys-to-Carleton letters (ff. 136,
   144, 146, 158, 159, 161, 173, 177, 179, 210); none is described as cipher, as to Wotton, or as carrying an enclosure. Folio 251 is
   the last item and sits in a tail of out-of-sequence and undated matter (f.214 "Letter to Dominis, enclosed in letter at f. 189";
   ff. 220, 239 Dominis papers; ff. 243-249 offices and letters of Mar.-May 1622; f.251). So f.251 is filed as a stray or enclosure,
   which fits either reading, but nothing attaches it to f.159.
3. **How this catalogue writes a cross-reference.** The one cross-reference in the piece is written "enclosed in letter at f. 189"
   (f.214). A Discovery search of the whole SP 99 series for `"at f"` returns only that item; a search for `cipher` in SP 99 returns 4
   items (SP 99/24/251; SP 99/4/219 "To Camillo Bacco", 1607; SP 99/2/71 and 2/103, Wilson 1602), and `"cipher from"` returns only
   f.251. So the series' cataloguer marks a folio pointer with "f." and an enclosure verb; "from 159" has neither. No other SP 99 item
   names a numeral as a sender, so there is no in-series parallel for the numeric-sender form either.
4. **Print (Pearsall Smith vol. 2, re-grepped for cipher context).** Vol. 2 pp. 169-170 (Wotton to Naunton, June 1621) shows the
   practice the f.251 description would fit: Wotton received intelligence from an unnamed correspondent at Rome "in cipher" and
   copied it out "translated from the Italian ad verbum". New Wotton ciphers were sent to Aston (24 Sept 1621, n. 2 on the Aston
   letter, citing G.C.C. MS 317 f.29) and to Donne/Fielding (1623, "a larger cipher"); none is printed with its numerals, so no printed
   1622 table gives 159 a value. Not found: any "159" as person or any reference to SP 99/24 f.251.

**Decision on step (1) (grade I, inferred; no source states it):** the catalogue evidence leans to "159" being a correspondent
designation (a numeral code-name, or a numeral the cataloguer read on the letter as its signature/heading) rather than a folio pointer:
this cataloguer writes pointers as "at f. N" with an enclosure verb (f.214), the two records carry no cross-reference fields, and f.159
is an ordinary plain Nys-to-Carleton letter in a long Nys run, with nothing in its description suggesting an enclosure in cipher. The
1604 printed cipher's 130-160 band for persons (A2P4-WOTT) is consistent but is a different, reissued cipher. Not excluded: that an
older finding-aid pencilled "159" as a pointer and the calendar copied it without "f."; only the leaves settle it. Counts: 0 H, 0 C,
0 S, 4 I (items 1-4 above are catalogue/print facts; the decision is I). Step (1) is answered as far as the catalogue can answer it;
the image check stays with REQUEST.md (f.251 and f.159), which is unchanged. Status stays open.

Suggestion (not run): if the f.251 image is ordered, read whether "159" stands at the head or foot of the leaf in Wotton's hand (a
signature/heading numeral) or is a later archivist's pencil folio note; that one look closes step (1) at grade H/C.
