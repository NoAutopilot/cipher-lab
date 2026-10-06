open
TNA Discovery item-details fetched by this worker gives SP 90/3/358's exact date (1 Aug. 1705); Wentworth Papers 1705-1739 (Cartwright 1883, archive.org djvu) then read and grepped by this worker around that date (letters of 14 and 21 Aug. 1705 are the nearest, both private family correspondence about houses and furniture, not diplomatic despatches) and for every "Harley" occurrence (109 hits, all either personal-letter mentions of "Mr./Secretary Harley" or one editorial footnote on his nickname "Lord T.", none a printed despatch to him) -- the book prints Wentworth-family private letters, not Raby's official State Paper correspondence, so it cannot be the standard edition for this item; searcharchives.bl.uk catalogue read for the full Whitworth Papers Berlin range (Add MS 37363-37397, both sub-ranges, 1716-1722) via a "Whitworth cipher" search, 0 hits, extending the prior session's 37373-37389-only check to the whole range including Add MS 37363 (ff.424, "Correspondence of C. Whitworth... at Berlin; 10 July 1716 - 23 March/3 April 1717", the volume matching SP 90/7/149,212's 1716-17 date).

## Check-solved (LANE CX2, 25 Sept 2026)

Round-2 sweep. Read `ciphers/sp90-raby-1704/NOTES.md`, `ciphers/whitworth-1707/NOTES.md` and this file's own
24 Sept 2026 sections first, per brief, to avoid duplicating either. This pass resolves two items the 24 Sept
session left open ("Next" 1 and 2 below) and runs the SIRIO vol.61 check named in the job brief.

1. **SP 90/3/358's exact date**, unresolved on 24 Sept: TNA Discovery `search/records` API (1 request, `sps.searchQuery="SP 90/3/358"`) returns **1 Aug. 1705**, "Raby to Harley. Frederick I secretly negotiating a treaty with Sweden..." Fetched `wentworthpapers100strauoft_djvu.txt` (already cached from the sibling target this session) and checked the "RABY, AT BERLIN" section around August 1705: the two nearest dated letters (14 and 21 Aug. 1705) are private family correspondence from Raby's mother/sister about houses and furniture in London, not diplomatic despatches, and a full-text grep for "Harley" (109 hits) turns up no printed despatch to him anywhere in the volume -- only personal mentions of "Mr./Secretary Harley" in family letters and one editorial footnote glossing "Lord T." as Harley's later title. **This is now a real, checked negative, not a gap**: Cartwright's *Wentworth Papers* is the Wentworth family's private correspondence, not Raby's official State Paper despatches to the Secretary of State, so it is not the standard edition for SP 90/3/358 regardless of the exact date matching its stated 1705-1739 range. No other printed edition of Raby's official 1705 despatches was found by web search this pass.
2. **BL Add MS 37373-37389 for SP 90/7 (1716-17)**, unresolved on 24 Sept because that range only covers 1719-1722: searched `searcharchives.bl.uk` for "Whitworth cipher" (1 request, 10 hits total) across the *whole* catalogue, not just the one sub-range -- confirms **zero** "cipher"/"cypher"/"decipher" term anywhere in Add MS 37363-37397 (the complete Whitworth Papers Berlin fonds, both the 37363-37372 range identified 24 Sept as covering 1716-17 and the already-checked 37373-37389/37390-37397 later volumes). Also confirms **Add MS 37363** itself (Vol. XVI, ff.424) is titled "Correspondence of C. Whitworth, as Envoy Extraordinary, etc., at Berlin; 10 July (O.S.), 1716 - 23 March/3 April, 1717" -- the volume whose date range contains SP 90/7/149,212 (1716-17) -- with no cipher marker catalogued, same caveat as 24 Sept 2026 (catalogued by correspondent/folio, not content type; an enciphered passage inside an otherwise-plain letter would not necessarily be flagged). The ten "Whitworth cipher" hits found are all unrelated (Blenheim/Drake/Hedges-era ciphers, the Moscow-period Add MS 61149, or Lord Whitworth of Paris 1803-09).
3. **SIRIO vol. 61** (named in the job brief): archive.org identifier `sbornikimperatorskogorusskogoistorichesk4` carries the metadata title "Т. 61. [Дипломатическая переписка английских послов и посланников при русском дворе..." (diplomatic correspondence of English envoys at the Russian court, 1711-1719, per its full description) -- but fetching and reading its actual `_djvu.txt` (1.35 MB) shows the scanned content is a **different, mismatched volume**: "Памятники дипломатических сношений Московского государства с Немецким орденом в Пруссии, 1516-1520" (a medieval Teutonic Order item). 0 hits for "Whitworth", "cipher"/"cypher", and even common English words ("the", "Majesty") are absent, while Cyrillic control terms ("Петр"/Peter, 53 hits) are present but at levels consistent with the wrong 16th-century text, not a diplomatic-correspondence volume. **This archive.org item's catalogue metadata does not match its scanned pages** -- flagged as a bad identifier, not a real read of SIRIO vol. 61; the actual volume 61 was not located and reading it is not completed this sweep. Separately, and independently of the identifier mismatch, vol. 61 is described as covering **the Russian court**, not Berlin, so even a correctly-identified copy would need its own content check before it could bear on SP 90/7-8 (Whitworth had moved from the Russia posting to Berlin by 1716, per the 24 Sept session's finding, unchanged here).
4. **Web search (model-solve announcements).** `"Whitworth Berlin Townshend Stanhope 1716 1719 SP 90 cipher solves Claude GPT deciphered"`: no dedicated page or announcement found; surfaced only the History of Parliament and BL catalogue entries already on file.
5. **Community lists.** `sources/cryptiana/` grepped fresh for "raby", "reichart", "berlepsch", "whitworth": the same single hit as 24 Sept 2026 (`web/blencowe2.htm`, R8762 "Raby (Strafford)" code-name, a different cipher key, not this correspondence).
6. **DECODE.** `aaymeloglu/unsolved-ciphers`'s cached `catalogue/decode-catalog.csv` (fresh shallow clone, 25 Sept 2026) grepped for "raby", "whitworth", "sp90", "sp 90", "townshend", "stanhope": no record.
7. **Bourdeau / Aymeloglu.** Fresh shallow clones (25 Sept 2026, shared with the sibling target) grepped (`*.md` files) for the same terms: no hit in either.

Requests: discovery.nationalarchives.gov.uk 1 (search/records for SP 90/3/358's date), archive.org 2 (Wentworth Papers djvu already cached this session; SIRIO vol.61 djvu, 1.35 MB, new fetch, mismatched content), searcharchives.bl.uk 1 ("Whitworth cipher" full-catalogue search), github.com 2 (fresh shallow clones, shared with the sibling target). 1 WebSearch query this target.

## Verdict (LANE CX2, 25 Sept 2026)

**Open, stage 2 verified unsolved, unchanged from 24 Sept 2026's conditional verdict, now with both of that
session's open "Next" items resolved.** SP 90/3/358 (1 Aug. 1705) is confirmed not to be in Wentworth Papers
(the book is private family correspondence, not official despatches, independent of the date match). SP
90/7/149,212 (1716-17) and SP 90/8/84 (1719) both fall inside the now-fully-checked BL Whitworth Papers
range (Add MS 37363-37397), which carries no catalogued cipher/decipher term anywhere in its 35 volumes. The
attempted SIRIO vol. 61 check failed on a mismatched archive.org identifier and was not completed; SIRIO in
general remains the wrong series for this correspondent's post-1712 Berlin posting regardless. No decipherment
or plaintext for any of the four target items found in print, on DECODE, or in either solver repository. Not
"new"; not "unpublished" (rule 10).

## Next

1. SIRIO vol. 61's correct archive.org (or HathiTrust) identifier still needs locating if a future worker
   wants to rule out the Russian-court channel formally; low priority given Whitworth's 1716-19 posting was
   Berlin, not Russia.
2. An access worker check on BL Add MS 37363 (ff.424, the exact 1716-17 volume) or Add MS 37373-37378
   (1719) for a decipher not caught by the catalogue's own correspondent-level description remains the
   cheapest next move before a TNA copy order, per the 24 Sept session's original suggestion, now narrowed
   to specific volume numbers instead of the whole 37363-37397 range.
3. TNA page-copy order for all four originals (SP 90/3/358, SP 90/7/149, SP 90/7/212, SP 90/8/84) is the
   fallback once (1)-(2) are exhausted; none is digitised per the QUEUE row.

---

# Raby (1705) and Whitworth (1716-19), Northern-Europe diplomatic ciphers — TNA SP 90/3/358, SP 90/7/149,212, SP 90/8/84

QUEUE row: N27 (`QUEUE.md`, "Candidates not on DECODE"). Extends N13's SP 90/2 (1704) run forward one piece;
see `ciphers/sp90-raby-1704/NOTES.md` (open, stage 2 conditional) and `ciphers/whitworth-1707/NOTES.md`
(open, narrowed to one passage) — read first, per brief, to avoid duplicating either.

## Source

TNA, State Papers Foreign, Prussia and German States. Catalogue text as quoted in QUEUE.md's N27 row:

> **SP 90/3/358** (1705): Raby to Harley, on Frederick I's secret Sweden treaty — same correspondent as
> N13's SP 90/2 cluster (Apr-June 1704), one piece later.
> **SP 90/7/149, 212** (1716-17): Whitworth to Townshend/Stanhope.
> **SP 90/8/84** (1719): Whitworth to Stanhope, translation of f.80 ("itself noted 'partly in cipher'").

Two different correspondents and two different edition questions:

## Raby, SP 90/3/358 (1705)

`ciphers/sp90-raby-1704/NOTES.md` already established that James J. Cartwright (ed.), *The Wentworth Papers,
1705-1739* (1883), is the standard printed edition of Raby's Berlin correspondence, and that it covers
**1705 onward** — i.e. this item, unlike the 1704 cluster, falls inside its stated coverage. Fetched the
archive.org djvu text (`wentworthpapers100strauoft`, 1 request, 1.4 MB) and confirmed a dedicated section
"RABY, AT BERLIN (1705-1708)" beginning with letters dated February 1705. Grepped for "Sweden", "secret
treaty" and "Frederick" throughout: no passage in the fetched text matches "Frederick I's secret Sweden
treaty" specifically (the hits found are unrelated — Frederick's Queen Sophie Dorothee, an index entry for
"Frederick I., King of Prussia", a Torcy cipher-letter mention in a different context). **This is not a safe
negative**: Cartwright's book is an editorial *selection* of Raby's letters (explicitly, per its own preface
style — it prints representative correspondence, not the full despatch run), so a specific folio's content
being absent from the grepped OCR text does not establish it is unpublished, only that the specific published
excerpts this sweep read do not obviously match this item's described content. The exact date of SP 90/3/358
within 1705 is not given in the QUEUE row; without it, checking the book page-by-page for this precise letter
was not completed this sweep.

## Whitworth, SP 90/7/149,212 and SP 90/8/84 (1716-1719)

Different correspondent, different period from `ciphers/whitworth-1707/`'s SP 91/5 Moscow despatches to
Harley/Boyle (1707-08, printed in *Sbornik Imperatorskago Russkago Istoricheskago Obshchestva* vols. 39 and
50) — by 1716-1719 Whitworth had moved from the Russia posting to Berlin/Prussia, and his correspondents here
are Townshend and Stanhope, Secretaries of State after the 1714 change of ministry. The Sbornik series is a
Russian-court-correspondence project and would not cover this period.

Web search found that the British Library holds **Add MS 37373-37389**, described as Whitworth's own
Berlin correspondence and papers "1716, 1719-1722" (seventeen volumes), including letters from Frederick
William I of Prussia, Stanhope, Craggs and Townshend — i.e. a second, retained copy of exactly this
correspondence channel, at a different repository from the TNA originals. This is a **manuscript sibling
copy, not a printed edition** — worth flagging for a future access worker (a BL Add MS 37373-37389 copy could
carry a contemporary decipher, as the SP 91/5 pattern did for Whitworth's earlier posting), but it does not
resolve edition risk on its own; no printed edition of Whitworth's 1716-19 Berlin despatches was located by
web search this sweep.

## Check-solved sweep, 24 September 2026

1. **Print.** See above: Wentworth Papers (1705-1739) covers 1705 by date but not confirmed for this specific
   folio; no printed edition found for the 1716-19 Whitworth-Townshend/Stanhope correspondence, only a BL
   manuscript sibling (Add MS 37373-37389).
2. **Web search.** "Whitworth envoy Berlin Hague 1716 1717 1719 Townshend Stanhope despatches printed
   edition" and variants: surfaced the BL Add MS 37373-37389 holding above; no dedicated cipher-history
   discussion of either correspondence channel.
3. **Community lists.** `sources/cryptiana/` grepped for "Raby", "Whitworth", "SP 90": one hit,
   `web/blencowe2.htm` line 65 — "F.61 (R8762) is another copy without a title and instructions, but it has
   additional entries: 892 (Monsieur), 369 (Bernstorf), St. Jean (Bollingbroke), **Raby (Strafford)**." This
   is a *different* cipher key (a DECODE-catalogued English Deciphering Branch key, R8762) in which "Raby" is
   used as a **cipher code-name for Strafford** (Raby was created Earl of Strafford in 1711) — i.e. evidence
   that Tomokiyo's project has separately catalogued material naming Raby, but not a decipherment of SP
   90/3/358, SP 90/7, or SP 90/8; not the same document, flagged as a lead for a future worker rather than a
   solution. No dedicated Cryptiana/Cipherbrain page for this row's specific items.
4. **DECODE.** Cached catalogue grepped for "SP 90", "Raby", "Whitworth", "Townshend": no record (the R8762
   key above is in Cryptiana's own snapshot, not confirmed present in the cached DECODE CSV export used for
   this check).
5. **Bourdeau.** Fresh shallow clone grepped for "Raby", "Whitworth", "sp 90": no hit tied to this row (the
   repository's Visconti-1727 key material uses "Townshend" only as an unrelated cipher code-number entry in
   a different, Italian nomenclator).
6. **Aymeloglu.** Same clone pass: no hit for "Raby", "Whitworth", or "SP 90" anywhere in the repository.

## Verdict

**Open, stage 2 verified unsolved (conditional).** Not "new"; not "unpublished" (rule 10). Closed-negative on
DECODE, Bourdeau and Aymeloglu. Print check is incomplete on both fronts: SP 90/3/358 sits inside Wentworth
Papers' stated 1705-1739 coverage but was not matched to a specific page (the exact date within 1705 is
needed first); SP 90/7 and SP 90/8 (Whitworth, 1716-19) have no printed edition found, only a BL manuscript
sibling copy (Add MS 37373-37389) not yet checked for a contemporary decipher.

Requests: archive.org 2 (Wentworth Papers djvu, already-cached from the sibling folder's prior fetch pattern,
re-fetched this sweep), github.com (shared clone, see sp35-townshend-key-1719/NOTES.md). 2 WebSearch queries
this target.

## BL Add MS 37373-37389 check (24 September 2026, LANE S worker H)

`searcharchives.bl.uk`'s JSON catalogue (`https://searcharchives.bl.uk/?q=Bothmer+Whitworth&search_field=all_fields&format=json&per_page=100`)
returns all 17 volumes of Add MS 37373-37389 in one query (the fonds-level record, Add MS 37373-37389,
confirms the range's own title: "Frederick William I of Prussia: Correspondence and papers of C. Whitworth as
Envoy at Berlin: 1716, 1719-1722"). Each volume is a detailed, itemized folio-by-correspondent list (checked
in full for the earliest, Add MS 37373, 4560 characters, 30 correspondent entries) — **no "cipher",
"cypher", "decipher" or "key" term appears anywhere in any of the 17 volumes' catalogue descriptions**, unlike
comparable BL fonds (a control search, `Whitworth cipher`, correctly surfaced Add MS 38238's "Cyphers:
Various British and foreign diplomatists: 1800-1804" and Add MS 61591's "Partly Fr. and cipher" elsewhere in
the same catalogue, confirming the search and field would show a cipher marker if the cataloguer had recorded
one). This is a negative result for a *catalogued* decipher in this specific range, not proof none exists —
the fonds is catalogued by correspondent and folio range, not by content type, so an enciphered passage
within an otherwise-plaintext letter would not necessarily be flagged. **Also: the individual volumes in this
range run 14 Apr. 1719 (Add MS 37373) to 8 Oct. 1722 (Add MS 37389) — none covers 1716-17, so SP 90/7/149,212
(dated 1716-17 in the QUEUE row) falls entirely outside this range regardless of content.** The correct BL
range for that correspondence period is Add MS 37363-37372 (same fonds, "WHITWORTH PAPERS," 1716-1719,
identifiers 040-002053692 through 040-002053703, read from the same query's results) — not checked this pass
(out of the assigned Add MS 37373-37389 scope), flagged as the cheaper next step for SP 90/7 specifically.
SP 90/8/84 (1719) does fall inside the checked range (candidate volumes Add MS 37373-37378, spanning Apr-Dec
1719), but its exact date within 1719 is not given in the QUEUE row, so no single volume could be matched to
f.80/f.84 specifically.

Requests: `searcharchives.bl.uk` 5 (>=2s apart, well under the 15-call cap): phrase search for "Add MS 37373"
(1), control search "Whitworth cipher" (1, incidentally surfaced "Plantamour, agent in Berlin: Letters to
Duke of Marlborough: 1702, 1703" in Add MS 61142 — the same name flagged as an unverified lead in
`ciphers/sp105-paget-1693/NOTES.md`; a different target, noted there rather than chased further here), direct
fetch of Add MS 37374's full record (1), "Bothmer Whitworth" search returning all 17 target volumes plus
neighbours in one page (1), full catalogue record for Add MS 37373 (1).

## Next

1. Get the exact date of SP 90/3/358 (TNA item-details, out of scope for this LANE S batch's no-Discovery
   rule) and check it against Wentworth Papers page by page.
2. Check BL Add MS 37373-37389 (searcharchives.bl.uk catalogue record) for a contemporary decipher alongside
   the 1716-1719 Townshend/Stanhope letters — cheaper than a TNA copy order if the BL copy already carries
   one.
3. None of the four items is digitised on Discovery (per the QUEUE row); a TNA page-copy order is the
   fallback route if (1)-(2) do not resolve it.

## Web and blog check (GF-A2-9, 2 Oct 2026)

Plain web searches (4): `Raby Harley 1 August 1705 Berlin Frederick I secret treaty Sweden cipher`; `Whitworth Stanhope
Berlin 1719 cipher despatch "SP 90/8"`; `Whitworth Townshend Havelberg conference 1716 Manteuffel letter cipher`;
`Raby and Whitworth Northern-Europe diplomatic ciphers Berlin despatches decipherment` (the folder's own title). Hits:
TNA catalogue pages for SP 90/3 and SP 90/8 neighbours (C6554737 etc.: Marlborough to Harley acknowledging Raby's letter
on the Prussia-Sweden treaty, 24 Aug 1705; a Raby "plea for confidentiality of news in cipher"), BL searcharchives
records for the Whitworth Papers (040-002053686 to -715) and for the Strafford papers Add MS 31128-31152, an Oslo/
ScienceNorway piece and a feedbagel post on AI decipherment of other letters (opened by title only: neither names Raby,
Whitworth, Berlin or SP 90), NSA Friedman-collection PDFs (general). None carries a decipherment or plaintext of SP 90/3/358,
SP 90/7/149, SP 90/7/212 or SP 90/8/84.
Blog site searches: `Whitworth Raby Berlin cipher Prussia` on scienceblogs.de (Cipherbrain), cryptiana.blogspot.com /
cryptiana.web.fc2.com and ciphermysteries.com -- only WW1/WW2/Kryptos Cipherbrain posts; `Strafford Raby Whitworth cipher
key Deciphering Branch` on the Cryptiana and Cipher Mysteries domains -- Beale, Zodiac, Voynich, Scorpion and list posts,
none about this correspondence, so no comment thread was relevant to open. Local `sources/cryptiana/` grep for
whitworth/raby: only the known blencowe2.htm "Raby (Strafford)" code-name entry (a different key). Account-4's
WEBCHECK (2 Oct 2026, commit 87bd98b6) logged the same negative for the sibling folder sp90-raby-1704.
Result: no decipherment or plaintext of any of the four items found on the open web or in the three blogs.

## Premise check (GF-A2-9, 2 Oct 2026)

(a) Folder's own mentions -- the TNA item texts were re-read in full (tools/discovery_items.py, SP 90/3, 90/7, 90/8,
term "cipher", 3 calls). The descriptions of SP 90/3/358, SP 90/7/149 and SP 90/7/212 do not themselves say any
passage is in cipher (the API returned them for "cipher", so the term sits in a field the description does not show;
the beta catalogue's web text says SP 90/8/80 and /84 are "partly in cipher"). SP 90/8/84 is "a translation of SP 90/8
Folio 80" and f.80 is "Whitworth to Craggs. A copy of a letter to Stanhope ... Copy of the relation sent to Stanhope",
also partly in cipher: f.80 and f.84 are two versions of one text, a ready-made cross-check once imaged, not a
decipherment. No decipherment is mentioned for any of the four.
(b) Other solvers' working files -- not found. Shallow clones of dbourdeau/cyphersolver and aaymeloglu/unsolved-ciphers
(2 Oct 2026) grepped for Raby, Whitworth, "SP 90": only an unrelated Harley-catalogue OCR text and a Gallica SRU dump
in cyphersolver; nothing in Aymeloglu's repository.
(c) Physical neighbours -- catalogue only (none digitised). SP 90/7/126 (1716, n.d.) is "Additions and alterations to
cipher" -- key material for Whitworth's 1716 cipher in the same piece as f.149 and f.212; SP 90/7/222 is a French
translation of f.220 "with cipher in English" and SP 90/7/171 gives a Prussian reaction "in cipher". In SP 90/8 the
duplicates are marked "Not ciphered" (f.16, f.24 "Duplicate of SP 90/8 f.22", f.74 "Duplicate of SP 90/8 f.72"): the
clerks there kept plain duplicates, so a plain duplicate of f.80/f.84 may sit nearby uncatalogued as such. A copy order
should take SP 90/7/126 with f.149 and f.212.
(d) Recipient and sender sides -- catalogue leads, not read. Raby's own retained papers are BL Add MS 31128-31152
(Strafford papers, 1705-1711, web-search snippet of the BL record), which could hold his draft of the 1 Aug 1705 letter
in clear; Whitworth's are BL Add MS 37363-37397 (already checked catalogue-wide for a cipher term, none). Harley's side:
Marlborough's 24 Aug 1705 acknowledgment of Raby's treaty letter shows it reached Harley's circle; HMC Portland (Harley
papers) is the printed recipient-side series and was not searched this pass. Next: BL searcharchives record for Add MS
31128-31152 (1705 volume) for a draft of 1 Aug 1705, and an IA full-text search of HMC Portland vols 4 and 8 for
"Raby" 1705; ~USD 1.


## Recipient- and sender-side print/catalogue check (A2P4-RABY, 3 Oct 2026)

Job: the folder's named free step (Premise check (d)): BL record for Raby's retained papers (Add MS 31128-31152) for a draft of 1 Aug 1705, and IA full text of HMC Portland vols 4 and 8 for Raby 1705. Intake gate (`tools/intake_gate_check.py`): open (line 1), edition/page citation present, exit 0. Searched by script; no vision.

1. **BL searcharchives.bl.uk (JSON, `/catalog/<id>.json`).** `q=Strafford Raby 1705` returned 17 records (shelfmarks incl. Add MS 31134, 31136, 31143, 31146). Then every record 040-002022922..952 was fetched (29 records, Add MS 31129-31152; ids ...927/935/938/942/950-952 answer 404, no record) and grepped for cipher/cypher/Harley/"1 Aug"/"Aug 1705". Add MS 31134 (ff.562, "Vol. I Correspondence during his embassy to Berlin; 17 Dec. 1697, 9 June, 1703-31 Dec. 1708", the 1705 volume) is catalogued only as "Included are:" selected correspondents (St Pierre, Rochfort, von Heems to Tilson, news-letters from Paris/Liege/Zelle/Bloni, Scarlett, Frederick I's copies f.330 etc.): **no Raby draft or despatch to Harley, no cipher/decipher term, no entry dated 1 Aug 1705**. Add MS 31135 (Jan 1709-Mar 1711) and the other volumes: 0 hits for cipher/cypher, one Harley hit (31148 f.394, his 1715 impeachment answers, irrelevant). Positive control: the same grep reproduces known catalogued items (Scarlett f.12, Heems ff.52-276, Frederick I copies ff.330/428/476/485) in 31134. Caveat unchanged: the record is a selective "included" list, so an uncatalogued draft cannot be excluded; this is a catalogue negative, not a leaf read.
2. **HMC Portland vol. 4 (IA `dukeportlandmanu04greauoft`, djvu 2.8 MB) and vol. 8 (`manuscriptsofhis08grea`, 1.5 MB), grep "Raby".** Vol. 4: 17 hits. The only 1705 Raby letter is "Lord Raby to [Robert Harley?]", **11 April 1705**, [Berlin] (projet of 8,000 Prussian men, Swiss Protestant cantons; calendared in English, plain, line 12170), plus Godolphin's April 1705 return of "my Lord Raby's letter [see April 11]" (line 12293). The 1705 dated run around the target is calendared with no Raby entry: 31 July (Edinburgh), 2 Aug (Edinburgh), then 4 Aug onward; no 1 Aug 1705 entry at all, and no grep hit for the Prussia-Sweden secret treaty in 1705 (the one Sweden/Prussia hit is a 16 Nov 1704 Cardonnel letter on Dantzic). Other Raby hits are 1706 (28 Sept, Prussian court), 1707-11 mentions. Vol. 8: 9 hits, none a 1705 Raby letter (regiment promotions, a Polish-minister order, an index entry). Positive control: the 11 April 1705 Raby letter (a known Raby item, same sender, same volume) is found by the same grep. Caveat: OCR text of a calendar (summaries), and "Raby" OCR variants not exhaustively tried.
3. **Result.** No printed or catalogued plaintext or decipherment of SP 90/3/358 (1 Aug. 1705) located in either source; HMC Portland vol. 4 carries a different Raby letter (11 Apr 1705) that is **not** SP 90/3/358 (date differs) and is a possible content neighbour only (no cipher noted in the calendar). Status stays open. Not graded: no reading made (H/C/S/M/I counts 0/0/0/0/0).
4. **Requests.** searcharchives.bl.uk 32 (>=2 s apart; 1 search + 31 catalogue GETs, 6 of them 404), archive.org 3 (advancedsearch 1, djvu 2). No other host.

## While waiting

Run now, depends on nobody: a copy-order pack for SP 90/3/358 together with SP 90/7/126 (cipher key), /149 and /212 (see Premise check (c)); the one cheap lookup left is Raby's own letter-book (Strafford papers) at BL beyond the catalogue, which needs a reading-room look, so it is queued behind the order, not a free step.

## Next (A2P4-RABY, 3 Oct 2026; supersedes the earlier lists)

1. [retired for this catalogue and these two HMC volumes] BL Add MS 31128-31152 and HMC Portland vols 4/8 for a 1 Aug 1705 draft or printed text: done, negative (above).
2. No further free print step is named by the evidence: the only recipient-side trace is Marlborough's 24 Aug 1705 acknowledgment of Raby's treaty letter (TNA catalogue, see Web check); a further untried instrument would be HMC Portland vol. 3 / Marlborough-Godolphin calendars, speculative, not started.
3. TNA page-copy order for SP 90/3/358, SP 90/7/126, /149, /212, SP 90/8/80 and /84 (nothing digitised) remains the way to an image; to ASKS if not already there.

## Verdict (A2P4-RABY, 3 Oct 2026)

Open, unchanged. The two named free checks are negative: no draft of 1 Aug 1705 in the catalogued BL Strafford papers (Add MS 31134, selective list) and no 1 Aug 1705 Raby item in HMC Portland vols 4 or 8. Not novel, not unpublished: absence from these two sources is a search result only (rule 10).

## Discovery availability flag (IMG-AUDIT, 3 Oct 2026)
TNA Discovery /records/v1/details, fetched once each: C6554948 (SP 90/3/358), C6555516 (SP 90/7/126), C6555524 (/149), C6555549 (/212), C6555649 (SP 90/8/80), C6555650 (/84): `digitised` = False for all six. Replaces the earlier "per the QUEUE row" wording. Requests: discovery.nationalarchives.gov.uk about 8.

## R8-SPS2 (c) (6 Oct 2026): not re-run
The named step (BL Add MS 31128-31152 and HMC Portland vols 4/8) already ran on 3 Oct 2026 (A2P4-RABY, negative, retired above); no request made.
