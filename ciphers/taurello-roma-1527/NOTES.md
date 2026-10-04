# taurello-roma-1527

Status: blocked
Recipient-side edition opened 3 Oct 2026 (A2P4-TAUR): Ulysse Robert, "Philibert de Chalon, prince d'Orange, vice-roi de Naples, 18 mars 1502-3 août 1530" (Paris 1902), full OCR of both archive.org scans (philibertdechalo00robe, philibertdechal00robegoog) grepped for Taurello/Torello/Vetralla/24 juin: 0 hits. Sanuto, Pastor, Gayangos and the Boletin RAH series were not read. Earlier text of this line, now partly superseded: standard edition not opened: Ulysse Robert, "Philibert de Chalon, prince d'Orange 1502-1530. Lettres et documents" (Boletin RAH 1902, listed on cervantesvirtual.com, which is Cloudflare-blocked to this environment) and Sanuto/Pastor appendices were not read by this worker; archive.org full-text search (be-api) for Taurello+Orange+Vetralla returned 29 hits, none naming Pietr'Antonio Taurello's 24 June 1527 letter (hits were Murray handbooks and unrelated indexes), and the phrase "Pietrantonio Taurello" returned 0.

## What this is

Single Este-Rome dispatch entirely in cipher, 24 June 1527, from the mission of Petr'Antonio Taurello to
Filiberto di Chalons, Prince of Orange (imperial commander, later commander at the Sack of Rome, 6 May 1527 —
this letter is from five weeks after the sack began, sent from Vetralla near Rome). Archivio Segreto Estense,
Cancelleria, Carteggio ambasciatori — Roma, piece no. "32" as printed in the finding aid (flagged by the 24 Sept
scout as likely an early Appendice-I piece number, not a final ASMo shelfmark). Finding-aid note (verbatim):
"Questa lettera è tutta in cifra" ("this letter is entirely in cipher"). No key or sibling decipherment noted in
the finding aid. QUEUE.md row IR8 (LANE N scout IT3 of 24 Sept 2026); source PDF
`ASE_Cancelleria_ambasciatori_roma.pdf`, ASMo/Este archive.

Ciphered status is stated directly and unambiguously by the finding aid ("tutta in cifra"). No key is filed with
it, per the same entry — unlike IR1/IR2/IR4/IR5, this is a cryptanalysis candidate (single letter, unicity
distance depends on length, not yet known — LESSONS.md's "large nomenclator, one letter" failure class is the
relevant risk here until the item is seen). `ciphertext.txt` is not created.

## Check-solved sweep, 24 September 2026

1. **Web.** WebSearch `Taurello "tutta in cifra" 1527 Filiberto Chalons Orange Vetralla lettera` and
   `"Petronio Taurello" OR "Pietrantonio Taurello" Ferrara Este ambasciatore Roma 1527`. Hits: Wikipedia pages
   for Philibert of Chalon, Battle of Gavinana, Siege of Florence (all general Sack-of-Rome-era context, no
   Taurello mention); a search-index PDF and the ASMo Spagna-fondo PDF itself, noting Pietrantonio Taurello as
   Ferrara's orator to Spain with correspondence documented May 1525 – Nov 1526 (a different posting/fondo from
   the Roma dispatch under review, not necessarily inconsistent — envoys moved between courts). No hit names
   this specific 24 June 1527 letter, its cipher, or a decipherment. Not found.
2. **Print.** WebSearch for Pastor's *History of the Popes* appendix material on Este ambassadorial dispatches
   around the Sack of Rome returned only general Sack-of-Rome background, no specific citation of this letter or
   piece "32". Not confirmed absent at verifier level (Pastor's, Venturi's and Balan's appendices were not read
   page-by-page — out of one worker's budget).
3. **Lists.** `sources/cryptiana/` grepped locally for `taurello|torello`: no hits.
4. **DECODE.** `sources/decode/records-non-decrypted-2026-09-24.tsv` grepped for `taurello|torello|roma.*1527`:
   no matching envoy/shelfmark. Live de-crypt.org not queried.
5. **Bourdeau/Aymeloglu.** Fresh shallow clones, `grep -ril "Taurello"` (and "Torello") across both trees: 0
   hits for either spelling.

## Verdict

**Open.** No source located a solution, key, plaintext or documented attempt for this item. Given the historical
proximity to the Sack of Rome (Taurello was with the future Habsburg commander five weeks before it), this is
the kind of item worth checking specifically against Pastor/Sanuto/Sack-of-Rome documentary collections before
any solver attempt — the general web sweep this pass found only secondary/tertiary background, not the primary
diplomatic editions themselves.

Copy-order: no digitised image found; the piece number "32" is not a confirmed shelfmark (see above — a worker
should cross-check the Roma fondo's own key before requesting). REQUEST.md below gives what can be specified.

Requests this pass: WebSearch 4, github.com 0 (reused shared clones). No SIAS, no Google Books, no DECODE login,
no promotion, no decoding.


## Web and blog check (CS-A2-C, 2 Oct 2026)

WebSearch queries (standard) and what they returned:
- Taurello Filiberto di Chalons principe d'Orange 1527 Vetralla lettera cifra (Wikipedia/DBE Philibert pages, Robert's Lettres et documents on cervantesvirtual; no mention of the letter)
- Taurello 1527 Ferrara ambasciatore Roma "in cifra" Sacco di Roma dispaccio Este (ASMo finding aids Spagna/Firenze/Bologna/Parma; Taurello as orator 1525-26 only)
- Archivio di Stato Modena Carteggio ambasciatori Roma Taurello 1527 cifra decifrazione (ASMo cipher-lab PDF, unimore theses; no Taurello decipherment)

Blogs: Cipherbrain, Cryptiana blog and Cipher Mysteries were covered by the restricted web searches above and a local grep of `sources/cryptiana` and `sources/ciphermysteries`; 0 hits for the sender, recipient or shelfmark; no comment thread opened because no hit was relevant.

archive.org full-text (be-api, one request at a time, 2 s apart, unquoted-token behaviour so counts are upper bounds):
- Taurello Orange Vetralla (29 hits, none relevant)
- Taurello Vetralla 1527 (42, none relevant)
- "Pietrantonio Taurello" (0)

Solver repositories (shallow clones, grep only, 2 Oct 2026): taurello: 0 / 0 in both solver repos; "torello" hits only in Bourdeau buda1489 and it1583 (unrelated targets, not read as this item). Aymeloglu cited, no code used.

DECODE: local grep of sources/decode (records-non-decrypted 24 Sept 2026 and later key lists) for the sender/recipient names: 0 rows; the 2 Oct 2026 login-free crawl (801 rows) by CS-A2-B is the same list. Live de-crypt.org not queried by this worker.

## Premise check (CS-A2-C, 2 Oct 2026)

- (a) not found: folder mentions no decipherment, gloss or clear copy; the finding aid says only "tutta in cifra".
- (b) not found: no Taurello/Chalon file in either solver repo's working files (greps above).
- (c) unreachable: no image exists (REQUEST.md); piece no. "32" unconfirmed, so no neighbour leaf could be viewed.
- (d) unreachable: the recipient-side edition (Robert, Lettres et documents) was not opened; cervantesvirtual.com blocked. Next: try the Robert volumes via archive.org/Google Books (country=US) for 24 June 1527 / Vetralla / Taurello.

Verdict: blocked. No solution, key, plaintext or documented attempt was found in anything searched, but no edition could be opened, so this is a search result for the log and not a statement that none exists. Status was `open` before this pass and failed the intake gate.


## Robert volume check (A2P4-TAUR, 3 Oct 2026, 18:13-18:2x UTC)

Route: archive.org advancedsearch (title query) found two scans of Robert 1902 (`philibertdechalo00robe`, `philibertdechal00robegoog`;
also `philibertdechalo0000sois` is Soisson 2005, in copyright, not read). `_djvu.txt` fetched once each (1.41 MB, 1.38 MB) and grepped by script.
Not the Boletin RAH 1902 serial printing; same author and title family, so whether the serial printing holds extra documents is untested.

| Query (case-insensitive) | robe | robegoog |
|---|---|---|
| taurell / torell / vetralla | 0 | 0 |
| "24 juin" / "juin 1527" | 0 | 0 |

Positive/coverage control (OCR is readable and the volume covers the window): "juin 1527" absent, but dated June 1527 items are cited in robe
("8 juin 1527", Milanesi recueil, l.5373/5890; "17 juin 1527", l.6205); "Chalon" 237 / 289 hits; "Ferrare|Este" 195 / 169; "chiffre" 19 / 17, of
which two are Vienna "original avec chiffre et déchiffrement" source notes (l.10189, 10355: PA 95, Austrian archive, not the Este piece) and one
the prince deciphering with Verona's help (l.12892). Limit: the control shows the book covers the period, not that it would print Taurello's
letter if it existed; a miss is a result for this edition only.

Google Books API (key, country=US), 3 requests: "Taurello Vetralla" 4 hits, none relevant (Annali meteorologici, Gazzetta, Bullettino telegrafico,
and "Palaces of Lazio" 1991 with a Taurello index entry, a surname in an unrelated palace context, snippet only, not opened); "Taurello Orange 1527" 0;
quoted Taurello + Philibert Chalon 0. Control for the API: the same key/country returned hits for other queries this session (route works).

Requests: archive.org 6 (4 advancedsearch, 2 download; 2 s apart), googleapis 3. No vision calls, no cost beyond tokens.

Remaining gaps (not read): Sanuto *Diarii* vols 45-46 (June 1527); Pastor appendices; Gayangos CSP Spain vol. 3; Boletin RAH serial printing of Robert; ASMo piece number check.
Next: Sanuto Diarii full-text search for Taurello/Vetralla on archive.org (be-api), ~$0.5.

Verdict: blocked (standing; Sanuto/Pastor/Gayangos unread). Robert 1902 does not print or mention the letter, Taurello or Vetralla (2 scans, OCR grep). This is a search result for the log,
not a statement that nothing exists elsewhere; no image, key or decipherment has surfaced.

## NEAR3-TAUR (4 Oct 2026, 01:35-02:0x UTC)

Intake gate: `intake_gate_check.py taurello-roma-1527` -> "blocked (line 3) -- already terminal, nothing to gate", exit 0. This job is the edition read.

Identifiers: advancedsearch (metadata only) lists 51 Google scans `idiariidimarinoNNsanugoog` of Sanuto, *I Diarii* (F. Visentini). NN is the Google scan number,
not the volume number, and the metadata carries no volume field. Volume mapped from the OCR title page and running heads:
- `idiariidimarino19sanugoog` = TOMO XLV, "I Maggio MDXXVII - XXX Agosto MDXXVII": covers the window (24 June 1527).
- `idiariidimarino05sanugoog` = TOMO XLII, "I Luglio MDXXVI - XXX Settembre MDXXVI" (checked via its djvu.txt, one download).
- Vol. 46: NOT mapped to an identifier (scans 22 and 01 carry MDXXVII index/heading hits, not opened). Vol. 46 is outside the 24 June window by its date range as far as the XLV heading shows; the gap is logged, not closed.

Queries (be-api fts, one id per call, 1.6 s apart), run per id over scan numbers 00-55 for Taurello / Torello / Vetralla / Borbon / Orange, plus "24 zugno":
| Term, vol. XLV (id 19) | hits | what |
|---|---|---|
| Taurello | 0 | |
| Torello | 0 | |
| Vetralla | 1 (doc-level; 4 snippets) | camp letters from Vetralla 4 and 8 Zugno 1527 (Carlo Nuvolone; "l'Agnello"; Urbano to the duchess) and the index entry (pp. 284-285): not the Este-Rome letter |
| "Pietro Antonio" | 1 | index entries (a captain, a constable of Lazise): no Taurello |
| Oranges (Orange spelling in the text) | 1 | election of the Prince of Orange as captain general of the army at Borgo; Orange at Siena: context, not the letter |
| "24 zugno" | 1 | Bohemia diet on St John Baptist's day: unrelated |
| Borbon (positive control) | 1 in 19 | the control hits in volumes 01, 02, 07, 08, 13, 19, 27-30, ... but 0 in scan 45; a fts total is 1 per document, not a count |
Control reading: the control term and the Orange/Vetralla terms read in vol. XLV, so the search covers the right text. Limit: fts total is document-level (0 or 1), the OCR is Google's, and a miss is a result for this scan only.
One hit worth the record: vol. XLII (id 05, 1526) names a "Taurello (Torello), messo dell'Imperatore al papa" (index p. 571; text: Ferrara orator Lodovico's intercepted cipher letters from Granada, 5 July 1526, "el zonzer di Herera li el di Taurello vien in Italia"). This is the imperial envoy of 1526, one year before the 24 June 1527 Este letter; whether he is the same person as Pietr'Antonio Taurello is not established here. Other volumes with Torello/Taurello hits (02, 08, 11, 18, 24, 26, 27, 30, 35, 45, 47, 53, 54, 05) were not opened (Torello is also a common word).
Pastor, Geschichte der Paepste IV.2 Anhang: no identifier located in this job; not searched.

Result: in Sanuto vol. XLV the term Taurello is absent and the letter is not printed or reported in the snippets read; Vetralla appears only in other correspondents' June camp letters. No change to the check-solved verdict: `blocked` stands (Pastor, Gayangos, Boletin RAH, vol. 46 mapping unread). Next: map vol. 46's identifier (scan 22 or 01 heads), read vol. XLII's Taurello passage (id 05, line 41313 of its djvu) to see whether it ties him to Pietro Antonio.
Requests: archive.org advancedsearch 2, metadata 6, download 1; be-api fts about 400 (over the usual few hundred; all 1.6 s apart, one at a time). No subagent calls.

## While waiting (RUN4-WAITBF, 4 Oct 2026)

- Action that depends on nobody: the last pass's named next -- map Sanuto vol. 46's archive.org identifier (scan 22 or 01 heads) and read vol. XLII's Taurello passage (id 05, line 41313 of its djvu) to see whether it ties him to Pietro Antonio, ~$0.5 (estimate); keep be-api requests to a few dozen this time (the last pass used about 400).
