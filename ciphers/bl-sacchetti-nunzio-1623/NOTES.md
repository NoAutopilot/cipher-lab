open
Pastor, *History of the Popes* vol. XXVIII (archive.org `historyofpopes0000ludw_z2c4`) and Döllinger, *Akademische Vorträge* I (1888, archive.org `11534489bsb`), each full-text searched by this worker on 3 Oct 2026 (be-api fts, "Sacchetti" 1 hit each, "cipher" in Pastor naming only Bagno, Pamfili, Monti and Pallotto), plus the BL catalogue records for Add MS 8693-8698 (searcharchives.bl.uk JSON) read in full by this worker: no printed edition of the registers located, and the BL describes volumes I-IV as registers copied in the Curia with clear Italian incipits and only "some letters still in cipher" (Add MS 8697), see Premise check.

## Check-solved (LANE CX, 25 Sept 2026)

Re-verdict per `.claude/briefs/check-solved.md`; this worker read the target's prior 24 Sept 2026 check-solved section below (kept, not deleted) and reran the six searches itself rather than relying on it, since that section's conditional "open" did not cite pages read or a controlled search near the verdict word (`tools/intake_gate_check.py` failed on it).

1. **Web (a).** WebSearch `Sacchetti nuncio Spain cipher "solves" Claude GPT decipherment 2026` — no hit for this target; the only "solves"+Claude/GPT result is the unrelated Cyphral Distich (Urquhart, Vals AI blog, 31 Aug 2026). WebSearch `"Add MS 8693" OR "Add MS 8694" Sacchetti British Library cipher` — no hit (BL catalogue itself is still offline post-2023 attack; only unrelated Add MS numbers returned).
2. **Print edition (b), with control.** Identified Pastor's *History of the Popes* vol. XXVIII on the Internet Archive (`historyofpopes0000ludw_z2c4`, English translation, Urban VIII period, matching the brief's "vol.28/29" pointer) via `advancedsearch.php`. Full-text searched with the be-api fts endpoint (`be-api.us.archive.org/fts/v1/search`, not a login, not a loan): query `Sacchetti` returns 1 matching document with 5 snippet hits, all about Giulio Sacchetti's January 1624 appointment and instruction as nuncio to Spain (matches this target's own subject) — none mentions cipher/decipherment. Query `cipher` on the same volume returns 5 snippets, all naming *other, later* nuncios to Spain in cipher (Bagno's instruction Jan. 1629; Pamfili and Monti's reports; Barberini to Pallotto, Oct./Nov. 1629) — none is Sacchetti (1624-26). Query `cypher` returns 0. **Control**: query `Olivares` (a name certainly in this volume, per the target's own subject matter) returns 1 matching document, confirming the search index and query mechanics work on this identifier, not just returning empty results. This is a genuine, worker-run full-text search of the standard edition the brief named, not a quote of the prior sweep's summary.
3. **Community lists (c).** `sources/cryptiana/` grepped fresh for "sacchetti", "nunzio", "nuncio": no hit. No Cipherbrain/Cipher Mysteries post found by WebSearch.
4. **DECODE (d).** Cached `decode-catalog.csv` (`sources/decode/records-non-decrypted-2026-09-24.tsv` and the fresh Aymeloglu clone's `catalogue/decode-catalog.csv`) grepped for "sacchetti" and "869[3-8]": no hit for either. Nearest DECODE nunciature-cipher records remain Spain 1576-77 and Spain 1767 (neither Sacchetti, neither the 1620s).
5. **Bourdeau (e).** Fresh shallow clone (25 Sept 2026, depth 1) grepped for "sacchetti" and "8693" through "8698": no hit anywhere (the only numeric near-matches are coincidental substrings in unrelated filenames, e.g. `zeschau1841/ct_R5005.digits.txt`).
6. **Aymeloglu (f).** Same fresh clone: no hit for "sacchetti", "nunzio", or "8693"-"8698" anywhere in the repository.

Lessons applied: checked for an interlinear/facing-page decipherment convention in Pastor's own text (none found — Pastor discusses ciphered correspondence but does not print decipherments); checked "key lost" framing (not applicable, no edition of this register found at all, ciphered or not); no WVO record (not a WVO letter).

**Verdict: open**, unchanged from 24 Sept 2026, now grounded in a worker-run controlled full-text search of the standard edition the brief named rather than only web-search snippets. Not "new"; not "unpublished" (rule 10) — a search result, not a discovery. Requests this pass: archive.org 4 (1 advancedsearch, 3 be-api fts, all curl >=1.5s apart, all HTTP 200), WebSearch 2, github.com 1 shallow-clone reuse (shared with the other two targets in this batch), `sources/cryptiana/` grep 0 network. No DECODE login needed (cached catalogue sufficient).

## Prior check-solved sweep, 24 September 2026 (superseded above, kept for the record)

# Cardinal Giulio Sacchetti, papal nuncio to Spain: secret dispatch registers, partly in cipher — BL Add MS 8693-8698

QUEUE row: N29 (`QUEUE.md`, "Candidates not on DECODE").

## Source

British Library, Western Manuscripts, **Add MS 8693-8698** (6 registers). Catalogue text as quoted in
QUEUE.md's N29 row: "Six-volume register of copies of Sacchetti's secret dispatches as nuncio to Spain
(1624-26) and of Curia correspondence about him (Urban VIII, Cardinals Francesco and Antonio Barberini,
Philip IV, Olivares), 'partly in cipher', copied at the Papal Curia in 1626." Not itemised further at
catalogue level; `url_tsi` empty — not digitised.

Giulio Cesare Sacchetti (1587-1663), later cardinal, was nuncio to Spain from January 1624 to 1626 (confirmed
by web search against his Wikipedia biography and the Apostolic Nunciature to Spain succession list).

## Check-solved sweep, 24 September 2026

1. **Print — the named editions searched, not found for this exact material.** The brief named the
   *Nunziature di Spagna* / *Acta Nuntiaturae* series (Istituto storico italiano per l'età moderna) as the
   expected home of a printed edition. Web search for "Nunziatura di Spagna Sacchetti volume edited
   correspondence 1624 1625 1626 Istituto storico italiano" surfaced only unrelated ISIME nunciature volumes
   for other legations and periods (Buonvisi's Warsaw nunciature 1673-74; Millini's Spain nunciature
   1605-1607; the Naples nunciature series) — **no dedicated published edition of Sacchetti's own Spain
   dispatch registers (1624-26) was located**, and no evidence the ISIME's Spain-nunciature series has
   reached the 1620s Sacchetti period at all.
2. A second search found a genuinely relevant, but narrower, item: Yale University Library's catalogue holds
   *"Instruttione a Monsig. Sacchetti Vescovo d'Gravina Nuntio appo la Maesta Cattolica"* — "Copy of the
   instructions to Giulio Sacchetti, who was sent as Nuncio to Spain, January, 1624", 117 pages, citing
   **Pastor, *History of the Popes*, vol. XIII/1, p. 273** as a secondary reference. This confirms (a) Ludwig
   von Pastor's standard history discusses Sacchetti's Spain nunciature (a scholarly secondary source, not an
   edition of his own dispatches or their cipher), and (b) manuscript copies of Sacchetti-Spain material
   circulate outside BL Add MS 8693-8698 (Yale holds instructions, not dispatches) — worth checking Pastor
   vol. XIII (English translation on archive.org/HathiTrust) for whether he quotes or cites specific ciphered
   passages, not completed this sweep (budget).
3. **Web search, general.** No dedicated Cryptiana/Cipherbrain/Cipher Mysteries post or forum thread on
   Sacchetti's Spain cipher correspondence found.
4. **Community lists.** `sources/cryptiana/` grepped for "sacchetti", "nunzio", "nuncio": no hit anywhere in
   the local snapshot.
5. **DECODE.** Cached catalogue (`unsolved-ciphers/catalogue/decode-catalog.csv`) grepped for "sacchetti":
   no hit. A broader grep for "nunzio"/"nuncio" found several Vatican Secret Archive nunciature-cipher
   records (Segretario di Stato series, dossiers for Portugal 1757-61, Spain 1767, Spain 1576-77, France
   1573-1625) — **none for Spain in the 1620s**, and none naming Sacchetti; the closest by subject (Spain
   nunciature) is a century and a half later (1767) or half a century earlier (1576-77). Confirms this
   specific correspondent/period combination is not on DECODE.
6. **Bourdeau.** Fresh shallow clone grepped for "sacchetti" and "8693" through "8698": the only "86xx" hits
   are coincidental (DECODE record id R8694 in `harley7001/NOTES.md`, referring to an unrelated BL Add MS
   72438 key, not this shelfmark). No hit for "sacchetti" anywhere in the repository.
7. **Aymeloglu.** Same clone pass: no hit for "sacchetti", "nunzio", or "8693"-"8698" anywhere in the
   repository.

## Edition risk

**Elevated but unresolved.** A cardinal-nuncio's registers of this scale (6 volumes) covering Curia-Madrid
diplomacy at the height of the Thirty Years War buildup is exactly the kind of material the *Nunziature di
Spagna* project exists to publish, and Pastor's *History of the Popes* is known to discuss this nunciature —
but this sweep did not locate a specific published edition of Sacchetti's own dispatch text, ciphered or not,
and did not read Pastor's relevant volume for a direct citation of ciphered material.

## Verdict

**Open, stage 2 verified unsolved (conditional: Pastor vol. XIII not read for a direct citation; ISIME's
Nunziature di Spagna series not checked past its published-volume list; JSTOR/Scholar for modern nunciature
scholarship not searched this sweep).** Not "new"; not "unpublished" (rule 10) — a search result, not a
discovery. Closed-negative on DECODE, Bourdeau and Aymeloglu.

Requests: 3 WebSearch queries this target; Google Books API 2 calls (`&key=...&country=US`, this lane's held
slot) — "Sacchetti nunziatura Spagna cifra" and "Sacchetti nunzio Spagna 1624 1625 1626": no dedicated edition
of Sacchetti's Spain dispatches in either result set (closest near-misses: "La legazione di Ferrara del
cardinale Giulio Sacchetti" 2006, his *later* Ferrara legation, not Spain; "Il diario del viaggio in Spagna
del Cardinale Francesco Barberini" 2004, a different cardinal's Spain trip). Consistent with, not proof
against, "no published edition of this register exists" — Google Books' index is incomplete for older
Italian scholarship and journal literature.

## Next

1. Google Books search (this lane's held slot) for "Sacchetti" + "nunziatura" + "Spagna" restricted to
   `filter=full` for a published-volume hit, and for Pastor's *History of the Popes* vol. XIII (English
   edition) full text around p. 273 for any quoted cipher passage.
2. Check the ISIME (`iststor.it`) published-volumes list directly for "Nunziatura di Spagna" titles and their
   date coverage, rather than inferring from web-search snippets of unrelated volumes.
3. Not digitised (per QUEUE row); BL Imaging quote is the fallback route once (1)-(2) are exhausted — draft a
   REQUEST.md line if this target is promoted further, not done this sweep (six registers is a large ask to
   quote sight-unseen).

## Web and blog check (CS-A2-F, 3 Oct 2026)

Run for LANE-A2PUSH (account 2), 3 Oct 2026, 00:41-01:05 UTC.

(a) Plain web searches, five (WebSearch, standard):
1. `Sacchetti nuncio Spain 1624 1625 Barberini cipher dispatches decipherment` -- hits: the BL's own records (032-002029577, 036-002029578, 040-002029579..584), SNAC Barberini Taddeo, Yale Beinecke "Instruttione a Monsig. Sacchetti" (digital.library.yale.edu/catalog/33096754). No decipherment, edition or blog post.
2. `"Add MS 8693" Sacchetti British Library cifre` -- BL records again; TNA Discovery pages for unrelated BL collections; nothing on a decipherment.
3. `"Sacchetti" nunziatura di Spagna 1624-1626 edizione dispacci cifra Barberini Madrid` -- BL records, Folger catalogue record 223267 and SNAC; no printed edition of the dispatches.
4. `Registro di cifre Segreteria di Stato Urbano VIII Nuntio di Spagna Vescovo di Gravina Sacchetti` -- BL and Yale records only.
5. `site:scienceblogs.de Sacchetti OR site:cryptiana.blogspot.com Sacchetti OR site:ciphermysteries.com Sacchetti nuncio` -- Wikipedia (Giulio Cesare Sacchetti), Yale, unrelated ciphermysteries posts (Simonetta, Voynich).
(The 25 Sept section also ran the model-solve query with "solves" + Claude/GPT: no hit.)

(b) Blog site searches, by the sites' own search URLs (curl, descriptive UA):
- Cipher Mysteries `ciphermysteries.com/?s=Sacchetti`: HTTP 200, "Nothing Found".
- Cipherbrain `scienceblogs.de/klausis-krypto-kolumne/?s=Sacchetti`: HTTP 200, page carries the `no-results` marker.
- Cryptiana blog `cryptiana.blogspot.com/search?q=Sacchetti`: HTTP 200, "no results" text, no post list.

(c) Opened: BL records (below) and the Yale Beinecke record titles. No blog post exists, so no comment thread was read.

Other sources this pass: DECODE listing (cached `sources/decode/records-non-decrypted-2026-09-24-diff.tsv`) has no Sacchetti record; the only matches are tag lists on BL Add MS 72438 ff. 9-10 (our own target labels). Bourdeau: `sources/solver-diffs/2026-10-03-bourdeau.tsv` row bl-sacchetti-nunzio-1623 "no match, different item". Aymeloglu: `2026-10-03-aymeloglu.tsv` no row for it. Fresh clones not made; these are the 3 Oct 2026 diffs of the two repositories.

Requests: searcharchives.bl.uk 11 (2 s apart, all 200; first 2 attempts returned 301 because the `/catalog.json` path was wrong), archive.org 1 advancedsearch, be-api.us.archive.org 6, ciphermysteries.com 2, scienceblogs.de 2, cryptiana.blogspot.com 2, WebSearch 5.

## Premise check (CS-A2-F, 3 Oct 2026)

**(a) The folder's own mentions: found, and it changes the picture.** The BL records (`searcharchives.bl.uk/catalog/<id>`, Accept: application/json, read 3 Oct 2026):
- 032-002029577 (Add MS 8693-8698): "Copies, partly in cipher ... The six-volume registers were copied in the Papal Curia upon his return to Rome on 10 Aug. 1626 (see 8695, f. 1)". Digitised Content field empty. Access text: "Please request the physical items ... online collection item request form" (not a viewer link).
- 040-002029579 (8693): title "Registro di cifre alla Segreteria di Stato ... del Nuntio di Spagna"; incipit and explicit are clear Italian ("Al Signor Cardinale Barbarino / Alle Cifre di Vostra Illustrissima con lettere dei 12 e 13 Marzo"). It says a passage is quoted "from the present MS" in Döllinger, Akademische Vorträge I (1888), p. 258, a report of 16 Jan 1625.
- 040-002029582 (8696, vol. IV): "Registro di Cifre della Segreteria di Stato ... al Nuntio di Spagna"; incipit clear Italian ("La principal cagione di quello si scrive a Vostra Signoria").
- 040-002029583 (8697, vol. V): "Some letters still in cipher."
- 8694, 8695, 8698: no cipher statement in the catalogue text.
So the registers are Curia copies in which the "cifre" (cipher dispatches) already stand in clear Italian; the catalogue names only a residue in vol. V as still in cipher. Whether any cipher groups are inside 8693-8696 is not stated. This is catalogue text, not a view of the leaves. The earlier framing of the target (six volumes "partly in cipher") is the shelfmark-level phrase.
**(b) Other solvers' working files: not found.** Bourdeau and Aymeloglu diffs list no work on this item.
**(c) Physical neighbours / facing pages: unreachable.** Not digitised per the record; no image to view. Gate: only a copy order or visit can show which leaves, if any, carry cipher groups.
**(d) Recipient side: found, partial.** Döllinger 1888 (fts hit "Aus dem Codex des Britischen Museums Nr. 8693; Sacchetti, Nunziatura di Spagna") prints a German rendering of a clear passage from 8693 (Olivares to the nuncio); Pastor XXVIII cites Casanatense and Vatican copies of the Instruction. Neither prints cipher groups or a decipherment. Barberini-side editions (Vatican Barb. lat. nunciature series) not searched this pass.

Consequence for later work (not a novelty claim): before any money goes on a copy order, ask the BL for the folio list of the "still in cipher" letters in Add MS 8697 (REQUEST.md already asks for a scope note); most of 8693-8696 may be readable plain text, so the cryptanalytic content is probably small.

## Verdict (CS-A2-F, 3 Oct 2026)

`open`, now with a web and blog check and a premise check. Search results only; no decipherment or edition of these registers was located by this worker in the sources above.

## Next step (costed, CS-BATCH5, 3 Oct 2026)

Re-read of the verdict and premise check above, with no new search (both were completed 3 Oct 2026 and gate exit 0). Cheapest next step: send the REQUEST.md question to the BL (owner-side email, ~USD 0 agent cost) asking for the folio list of the leaves still in cipher, then a ~USD 3 transcription batch on one pilot volume once images or a copy arrive. Status unchanged (`open`).

## While waiting

- [done 6 Oct 2026, D22-FTS] Barberini-side nunciature editions searched by full text for "Sacchetti" with "cifra"/"ziffera": no printed Sacchetti cipher text found (section D22-FTS below). Left: Quazza, *La guerra per la successione di Mantova* vol. 1 quotes the nuncio's dispatches and was not read; a page read there is the one untried step (~USD 1).

## D22-FTS (6 Oct 2026)

Item 1 of the D22-FTS job (Sonnet worker, 22:2x-22:4x UTC), search only, no decoding. Grade I for anything below: archive.org's cross-corpus full-text (be-api) treats the quoted terms loosely and returns noise, and no page locators come back.
Queries (be-api fts, whole archive.org, 1.5-2 s apart; hit count = be-api "total"): `"Sacchetti" cifra nunzio` 17225 (top hits Pastor/Ludwig *History of the Popes* vol. on 1645-48 "Cifra al Nuntio di Venezia", none Sacchetti); `"Sacchetti" "cifra" 1623` 8350 (noise: Fresco­baldi, Pietro da Cortona, and `daspapstlichesta0001unse`, *Das päpstliche Staatssekretariat*, an archive guide listing "Madrid: 6124-6127, 6130 (1623-1631)" -- a finding aid, no Sacchetti text); `"Sacchetti" "ziffera"` 60 (noise); `"Giulio Sacchetti" nunzio Spagna` 613; `"Sacchetti" "Barb. lat." nunziatura Spagna 1623` 282; `"nunzio Sacchetti" cifra` 6; `"Giulio Sacchetti" "in cifra"` 134. archive.org advancedsearch for titles `nuntiaturberichte` (40 rows, all the German/Vienna/Paris series 1533-1688, none Spain 1620s), `nunziatura spagna` (0), `Barberini nunzio` (1, a 1605 oration). Google Books API (key, country=US): `"Sacchetti" nunzio Spagna cifra decifrata` 1 volume, *La Valtellina crocevia dell'Europa* (1998), snippet a note on "BAV, Barb. Lat. 5256 ... istruzione a Giulio [Sacchetti]" (an instruction, not a cipher text).
Leads that name the nuncio but print no cipher: Sforza Pallavicino, *Vita di Alessandro VII* ("il nunzio Sacchetti, amato da tutta la corte", Madrid, `vitadialessandro12palluoft`); Quazza, *La guerra per la successione di Mantova e del Monferrato 1628-1631* (`quazza-la-guerra-per-la-successione-di-mantova-e-del-monferrato-1628-1631-v-1`, "dal nunzio Sacchetti", quoting dispatches; the volume was not read); a catalogue list in `bub_gb_X5tfAAAAcAAJ` "Nunziatura di Spagna -- Giulio Sacchetti, vescovo di Gravina, 1624".
Result: no printed Sacchetti cipher dispatch or decipherment found in these searches; the Barberini-side series (Nuntiaturberichte) on archive.org are the German ones, so that family is not the right edition for Spain. Not a novelty verdict (rule 10). Requests: be-api 6, archive.org advancedsearch 3, Google Books 1.
