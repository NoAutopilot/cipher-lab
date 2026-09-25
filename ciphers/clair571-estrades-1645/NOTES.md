open
Négociations secrètes touchant la paix de Munster et d'Osnabrug (Le Clerc, 1725, tome II, archive.org
negociationssecr02lecl) read by this worker: printed extract of a D'Estrades letter to Mazarin, 23 Sept 1645
(djvu line ~71269, within the target's own Jul-Dec 1645 window), control words "Servien" (329 hits) and
"plénipotentiaire" (81 hits) confirm the OCR text is searchable for this period; the target's own ciphered
letter "adressée à l'un des plénipotentiaires" not found printed there or in tome III.

## Access (LANE YX worker YX-LOC571, 25 Sept 2026)

**The target letter is now pinned: Clairambault 575, p.1209.** Fetched the archivesetmanuscrits finding aid
`https://archivesetmanuscrits.bnf.fr/ark:/12148/cc13896b` (plain curl, browser UA, HTTP 200) in full (not just
page 1 -- the whole IR renders as one page, 944 lines of text). Its own item-level list gives, verbatim:
"Clairambault 575 • V Ambassades du maréchal d'Estrades (juillet-décembre 1645)" containing "P. 1209 • Lettre
chiffrée adressée à l'un des plénipotentiaires à l'occasion du traité de Münster." -- an exact string match to
QUEUE M27's own catalogue phrase, and Clair 575's own date span (juillet-décembre 1645) is exactly M27's
"Jul-Dec 1645" window (resolving the 24 Sept pass's open question "which of the twelve volumes"). No other
volume's item list contains this phrase.

**Table, from the same finding aid (one request), volume / date range / cipher-relevant entries / Gallica ark:**

| Vol. | Date range (finding aid) | Cipher-relevant entries in the finding aid | Gallica ark |
|---|---|---|---|
| Clair 571 | inventory only, covers 1637-1683 | (index volume, no letters) | not digitised |
| Clair 572 | 1637-1640 | none found | not digitised |
| Clair 573 | 1641-1644 | none found | not digitised |
| Clair 574 | Jan-Jun 1645 and 1649 | **p.4-5 "Chiffre employé par Brasset"** (= DECODE 9431) | not digitised |
| **Clair 575** | **Jul-Dec 1645** | **p.1209 "Lettre chiffrée adressée à l'un des plénipotentiaires à l'occasion du traité de Münster" -- the target** | not digitised |
| Clair 576 | 1646 | none found | query unreachable this pass (see below) |
| Clair 577 | 1647 | p.1 "Chiffre pour l'Italie" (= DECODE 9430) | not digitised |
| Clair 578 | 1648-1650 | none found | not digitised |
| Clair 579 | 1651-1654 | p.341 "Double du chiffre de Mazarin avec M. d'Estrades" -- new, not previously noted in this target's NOTES; matches Tomokiyo/Lasry's DE=-38 Clair.577/579 reconstruction (same cipher, a second copy) | not digitised |
| Clair 580 | 1655-1668 | p.89 "Chiffre de Mme d'Estrades" (= DECODE 9432, "p.89-95, Madame d'Estrades") | not digitised |
| Clair 581 | 1669-1675 | none found | not digitised |
| Clair 582 | 1676-1685 | none found | not digitised |

**None of Clairambault 571-582 is digitised on Gallica.** Checked every volume individually against Gallica's own
SRU catalogue (`https://gallica.bnf.fr/SRU?...&query=dc.source all "Clairambault NNN"`, the field a control query
proved matches: the identical query for "Clairambault 349" returns exactly one record, `ark:/12148/btv1b9000668z`,
the volume already on file for a sibling target). All of 571, 572, 573, 574, 575, 577, 578, 579, 580, 581, 582
returned `numberOfRecords=0`; 576 returned the same on a third attempt after two `ws_closed_mid_exchange` tunnel
resets (network-side, not a challenge -- logged, not retried further). This is a real "not digitised" result, not
an artefact of query syntax, given the control hit. Two other routes tried and stood down on: the SRU endpoint
`gallica.bnf.fr/services/engine/search/sru` (a different endpoint from the one that worked) returned Gallica's
own altcha "Vérification de sécurité" challenge page to both plain curl and a real headless-browser fetch
(`tools/browser_fetch.js`) -- one retry each, per the good-citizen rule, then stood down, not needed once the
working `gallica.bnf.fr/SRU` endpoint and query field were found. `catalogue.bnf.fr` (the general BnF catalogue,
not Gallica) answered a plain-text search but returned only unrelated `cb...` identifiers, no manuscript-specific
hit -- not pursued further, superseded by the SRU result.

Consequence: **no image of the target leaf (Clair 575 p.1209) or the Clair 574 key (p.4-5) can be fetched this
pass** -- there is nothing on Gallica to fetch. Cipher-line count and sign type (figures vs. symbols vs. mixed)
for the target letter are **not established** and cannot be until the physical volume is imaged some other way
(reading-room visit, a BnF reproduction order, or a future digitisation). This is a stronger, more specific
negative than the 24 Sept pass's "exact volume not established" -- the volume is now known, and it is simply not
on Gallica at all.

**Lasry/Biermann reconstructions (recap, not re-fetched beyond what NOTES already had -- within the 4-page
budget the brief allows, 0 further pages fetched since the check-solved pass already read this in full):**
`sources/cryptiana/web/louisxiv0.htm` (on disk) documents Lasry's 2025 interlinear-decipherment reconstruction of
**Clair 577** (p.1, "Chiffre pour l'Italie", 1647) and, per this pass's finding-aid read, the same DE=-38 cipher
recurs as a second copy at **Clair 579 p.341** ("Double du chiffre de Mazarin avec M. d'Estrades", 1651-1654) --
a "double" (duplicate copy) of the identical key, not a new reconstruction target. Neither is Clair 575 or Clair
574. DECODE listing not re-crawled this pass via `tools/decode_list.py` (key/N-A records are outside its
cipher-focused non-decrypted/decrypted sweep and the three record numbers, descriptions and dates were already
established and cited in this file's Check-solved section from the cached `unsolved-ciphers` catalogue CSV);
re-running the login-free RecordsList crawl to re-derive the same three rows would not move this forward and was
judged out of scope for this box.

**Cheapest recovery test now possible:** none, from Gallica -- the key (Clair 574 p.4-5, Brasset) and the target
letter (Clair 575 p.1209) sit in the same undigitised volume run. The cheapest next step is a single BnF
reproduction request (REQUEST.md, or a reading-room visit) naming both leaves together (Clair 574 p.4-5 and Clair
575 p.1209), since both are needed for the same recovery test (apply Brasset's own key to Brasset's own circle's
letter) and both come from the same undigitised fonds -- one request serves both. A transcription brief, once
images exist, needs: page images of Clair 574 p.4-5 (the key table) and Clair 575 p.1209 (the ciphered letter,
plus enough surrounding pages to catch any accompanying plain-French docket or address line), and this NOTES.md's
identification of the letter as addressed "à l'un des plénipotentiaires à l'occasion du traité de Münster" so a
transcriber can confirm the leaf by catalogue description alone if folio numbers are not visible on the images.

Requests this pass: archivesetmanuscrits.bnf.fr 1 (cc13896b, full finding aid, HTTP 200). gallica.bnf.fr 15 (1
diagnostic-query probe, 12 dc.source volume queries [2 needed one retry each on `ws_closed_mid_exchange`, both
recovered], 2 altcha-challenged `services/engine/search/sru` probes standing down per the one-retry rule) + 1
headless-browser fetch of the same challenged endpoint. catalogue.bnf.fr 1 (reachable, no useful hit). WebSearch
2. No DECODE requests this pass (cached catalogue data reused, per above). No subagents used.

## Check-solved (LANE CX, 2026-09-25)

Six-source sweep run fresh this pass (LANE CX worker CX-CLAIR), on top of -- not only quoting -- the 24 Sept
2026 LANE G2 pass kept below.

1. **Web search.** `Acta Pacis Westphalicae "Estrades" 1645 Brasset chiffre Clairambault` -- confirms APW's
   *Die französischen Korrespondenzen* covers this exact correspondence and date range (vol. for 25 Nov 1645-
   8 Jun 1646 named), but returned no page-level detail on this letter or on Clairambault; a Zenodo record
   ("Acta Pacis Westphalicae: Corpus français (APWCF)") surfaced as a possible full-text corpus, not opened
   this pass (budget). apw.digitale-sammlungen.de itself not reached this pass.
2. **Standard printed edition, opened and read.** archive.org `negociationssecr02lecl` and `negociationssecr03lecl`
   (Jean Le Clerc, *Négociations secrètes touchant la paix de Munster et d'Osnabrug*, 1725, tomes II-III --
   the edition the job brief names) fetched in full (`_djvu.txt`, both HTTP 200) and grepped. Tome II: control
   "Servien" 329 hits, "plénipotentiaire" 81 hits (OCR reads for this period); "Estrades" 7 hits, all letters
   or mentions from Aug-Sept 1645 (read in full at djvu line 71269: an "Extrait d'une lettre de Monsieur
   d'Estrades à Monsieur le Cardinal Mazarin, du 23 Septembre 1645," on Spanish peace overtures to the Dutch --
   a letter to Mazarin, not to a plenipotentiary, and not marked ciphered); "Brasset" 0 hits. Tome III:
   "Estrades" 0, "Brasset" 1, "chiffre"/"déchiffrer"/"chiffrer" 20+ hits (the edition routinely prints
   deciphered cipher correspondence in clear, the same pattern check-solved.md flags for Thurloe/Birch --
   worth a targeted read by a future worker, out of this pass's budget). No printed occurrence of M27's
   specific Jul-Dec 1645 letter "adressée à l'un des plénipotentiaires" found in either tome.
3. **Community lists.** `sources/cryptiana/web/louisxiv0.htm` re-read (on disk): confirms the 24 Sept findings
   below (Clair. 577/579 reconstructed by Lasry, Baluze 172 reconstructed, Clair. 574 "not found online" per
   Tomokiyo) -- no new content since 24 Sept. No Cipherbrain hit by web search this pass.
4. **DECODE.** `unsolved-ciphers/catalogue/decode-catalog.csv` (fresh clone, 25 Sept 2026) re-grepped for
   "clairambault 57": confirms the same two rows the 24 Sept pass found, record 9431 (Clairambault 574, p.4-5,
   1645-1649, Henri Brasset, Key) and record 9430 (Clairambault 577, p.1, 1647, Key) -- no new record, no
   record for 571-582 dated specifically Jul-Dec 1645. Login-gated RecordsView not opened (budget).
5. **Bourdeau** (fresh shallow clone, 25 Sept 2026, `github.com/dbourdeau/cyphersolver`). Grepped for
   "estrades", "clairambault 57": hits in `napoleon/unsolved.htm` (Clair. 577, 1647, Italian letter, solved by
   Lasry/Biermann 2025 -- same item as source 3, not M27), `colbert/NOTES.md` (lists a published "d'Estrades"
   key among 1665-74 Colbert-office ciphers, unrelated correspondent/date), `bordeaux/NOTES.md` (Brienne's
   1651 Cipher 2 "to d'Estrades" -- a different, later correspondence). No hit for 571-582 or Jul-Dec 1645.
6. **Aymeloglu** (fresh shallow clone, 25 Sept 2026, `github.com/aaymeloglu/unsolved-ciphers`). Grepped for
   "estrades", "clairambault 57": no hit beyond the catalogue CSV already covered under source 4.

Requests this section: archive.org 3 (1 advancedsearch, 2 `_djvu.txt` fetches, all `-L` follow, >=1.6s apart).
WebSearch 1. github.com 2 fresh shallow clones (shared with the other three targets in this brief).

## Verdict (confirmed, LANE CX 2026-09-25)

Stays **open**. The printed edition the job brief names (Le Clerc's *Négociations secrètes*) is now directly
read by this worker with a confirmed control, closing the gap the 24 Sept pass left (source 2 "not opened").
No source found the target's specific Jul-Dec 1645 ciphered letter to a plenipotentiary in print or in a
catalogue. The 24 Sept pass's caution stands: the exact volume among 571-582 is still not pinned, and the same
date/circle (Brasset/d'Estrades/Mazarin, 1645) already has DECODE Key records and Tomokiyo/Lasry
reconstructions in the immediate neighbourhood -- worth reading Clair. 574 and DECODE 9430/9431 directly, and
tome III's several clear-printed deciphered passages, before any fresh cryptanalysis.

---

# Letter to a plenipotentiary at the Peace of Münster, Jul-Dec 1645 -- BnF Clairambault 571-582

QUEUE row: M27 (sources/solver-diffs/2026-09-24-lane-g2-gallica4.tsv, "Fourth pass, 24 September 2026").

## Source

BnF, Département des Manuscrits, **Clairambault 571-582** ("Lettres et pièces originales relatives aux
missions diplomatiques et militaires de Godefroy, comte, puis maréchal d'Estrades, 1637-1685"), archivesetmanuscrits
ark `cc13896b`. QUEUE catalogue note: "Lettre chiffrée adressée à l'un des plénipotentiaires" at the
negotiation of the Peace of Münster, Jul-Dec 1645 -- one ciphered letter named within d'Estrades's own large
diplomatic-mission archive; no key or decipherment named. **Which of the twelve physical volumes (571-582)
this item actually sits in is not established by the QUEUE row and was not resolved this pass** (see verdict).

## Check-solved sweep (24 September 2026)

1. **Web search.** `"Clairambault 574" OR "Clairambault 571" chiffre Brasset 1645 Munster plénipotentiaire`
   returned catalogue detail beyond the QUEUE row: **Clairambault 571** is itself "an inventory of pieces
   concerning negotiations and ambassadies of the maréchal d'Estrades from 1637 until the Peace of Nimègue
   concluded in 1678" (i.e. an index/finding-aid volume, not a letter volume), and **Clairambault 574** covers
   "Ambassades du maréchal d'Estrades (January-June 1645 and 1649)" -- note this date span (Jan-Jun 1645) is
   *adjacent to but does not cover* M27's stated Jul-Dec 1645 window, so the target item likely sits in a
   still-unidentified volume, not necessarily 574. No solver/blog claim of this specific item surfaced.
2. **Printed correspondence.** *Lettres, mémoires et négociations de monsieur le comte d'Estrades* (multiple
   editions, Internet Archive identifiers `lettresmmoire01estr` etc., 1709 and 1743 printings, 26 IA items
   found) exists, but by its own title covers d'Estrades's *later* embassies -- Holland 1663-68, then "Italie,
   Angleterre, & Hollande... ambassadeur plénipotentiaire à la paix de Nimègue" (1678) -- years after 1645, when
   he was a junior figure at Münster, not yet the named plenipotentiary. **Not opened or read this pass**; the
   1743 multi-volume set's coverage of his earliest (1645-47) period is unconfirmed, flagged as a real gap.
   The actual French plenipotentiaries at Münster, Comte d'Avaux and Abel Servien, have their own large printed
   negotiation record (e.g. the "Négociations..." series for the Peace of Westphalia) -- not searched this pass.
3. **Calendars/state-paper series.** Not reached beyond item 2's caveat.
4. **Cryptiana / Cipherbrain.** Extensive related material, no direct hit on this item. `sources/cryptiana/
   web/louisxiv0.htm`, section "Ciphers in Correspondence of D'Estrades (1647-1653)" (anchor `#SEC1B`), is a
   letter-by-letter reconstruction of **Clairambault 577 and 579** (1647-1653) done with George Lasry: quoted
   verbatim, *"In 2025, George Lasry kindly provided me with his analysis. He not only reconstructed most of
   the keys by using interlinear decipherment, but he even identified some keys by using his solver for
   syllabic ciphers."* Every dated entry in this section runs from p.1 (1647) onward -- **none dated Jul-Dec
   1645** and none naming "un des plénipotentiaires" as recipient. Separately, the same page (line 46)
   documents **BnF Baluze 172** (a different shelfmark) containing letters *to* d'Avaux and Servien -- the
   actual Münster plenipotentiaries -- from Mazarin or the Comte de Brienne, Secretary of State, dated
   **1644-1645** (f.145, f.153, f.231, f.269), with a reconstructed cipher: same year and same negotiating
   circle as M27, different archive. And (line 67): *"BnF Clair 574 (1645 or 1649) (not found online) contains
   a cipher used by Brasset (f.3-4)"* -- Tomokiyo states he has **not** viewed Clair 574 itself (not digitised
   at time of writing). None of this quotes M27's specific letter, so it is not found-solved, but it shows this
   exact archive family and exact year/circle (d'Estrades/Brasset/Münster plenipotentiaries, 1645) is under
   active, detailed study by Tomokiyo and Lasry, with at least two cipher tables already reconstructed in the
   immediate neighbourhood (the Mazarin-D'Estrades cipher DE=-38 in Clair.577; the Baluze 172 Mazarin/
   Brienne-to-Avaux/Servien cipher). No Cipherbrain page found.
5. **DECODE.** Cached catalogue (`unsolved-ciphers/catalogue/decode-catalog.csv`, fresh clone, more complete
   than this repo's own non-decrypted-only cache) has **three Key-type records inside this exact 571-582
   volume run**: record **9431**, Clairambault 574, p.4-5, dated **1645-1649**, correspondent **Henri
   Brasset** (record_type Key, status N/A) -- the closest by date to M27's Jul-Dec 1645 window; record **9430**,
   Clairambault 577, p.1, 1647 (Key, N/A); record **9432**, Clairambault 580, p.89-95, 1655-1668, "Madame
   d'Estrades" (Key, N/A). A related fourth record, **9429**, is a **different** shelfmark (Clairambault 417,
   f.236, 1648, Henri Brasset) marked **Cipher/Decrypted**. None of the four names a Jul-Dec 1645 item
   addressed to "un des plénipotentiaires," and none was opened (RecordsView needs a DECODE login, not used
   this pass for budget reasons) -- so this is a strong proximity flag, not a match.
6. **Solver repositories.** Fresh shallow clones of `dbourdeau/cyphersolver` and `aaymeloglu/unsolved-ciphers`
   grepped for "Estrades", "Clairambault 57", "571-582", "Brasset", "Munster"/"plénipotentiaire": the only hit
   is `cyphersolver/napoleon/unsolved.txt`, itself a cached digest of Tomokiyo's own `unsolved.htm` (same
   D'Estrades-1647 entry as item 4, not independent). No curated CATALOGUE.md/TARGETS.md/SOLVED_CATALOGUE.md
   entry for this shelfmark or correspondent in either repository.

Requests: WebSearch 1 query. archive.org 1 advancedsearch query (26 hits, IDs recorded above, not opened).
github.com 2 shallow clones (shared across this worker's six rows). de-crypt.org 0 (RecordsView not opened).

## Verdict

**Open**, but flagged **high duplicate-risk / active-work** rather than a clean unsolved target. No source
found names M27's specific Jul-Dec 1645 item, so it is not found-solved -- but the same finding-aid volume
range (571-582) already has three DECODE Key records and two Tomokiyo/Lasry-reconstructed cipher tables in the
immediate date/circle neighbourhood (1645-1653, Brasset/d'Estrades/Mazarin/Brienne). Recommend **against**
starting fresh cryptanalysis on this item without first (a) pinning down which of the twelve volumes in
571-582 actually holds the Jul-Dec 1645 letter (the QUEUE row does not say), and (b) reading DECODE records
9430/9431/9432 and Clairambault 574 directly -- a real document read, not just the catalogue note -- since the
existing key for Clair 574 (1645-1649, Brasset) may already open this letter once located.

`python3 tools/room.py ... "nomination: ciphers/clair571-estrades-1645 | copy-free | cryptanalysis (LOW
PRIORITY -- see NOTES 'duplicate-risk') | exact volume among 571-582 unresolved; DECODE Key records
9430/9431/9432 and Lasry/Biermann's 577/579 (1647-53) reconstructions sit right next to this item's date --
check those and read Clair 574 before any fresh solving"`
