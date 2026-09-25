open
Pastor, *History of the Popes* vol. XXVIII (Urban VIII, archive.org `historyofpopes0000ludw_z2c4`), full-text searched by this worker (be-api fts, control "Olivares" 1 hit confirming the search functions): "Sacchetti" returns his 1624 Spain-nuncio appointment and instruction (p. ~530 by the index's own numbering) but no co-occurrence with "cipher"/"cypher" in any of the 5 returned snippets, and the volume's 5 "cipher" snippets all name later nuncios (Bagno, Pallotto, Pamfili, Monti, all post-1626) — no hit places a ciphered Sacchetti dispatch in print.

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
