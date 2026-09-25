open
HMC *Calendar of the Stuart Papers belonging to His Majesty the King* vol. I (1902, archive.org `calendarofstuart01grea`), read by this worker at pp. lxi-lxii and p. 345 (`_djvu.txt` lines 1155-1163, 2926-2928): the editors describe "the voluminous papers of Cardinal Gualterio in the British Museum (MSS., Additional, Nos. 20,241 to 20,583)" — a range covering 12 of our 14 target volumes — and cite extracts from them printed in Head's *The Fallen Stuarts*, but none of our 14 specific shelfmarks is individually named there or anywhere else in that volume (checked by exact-number grep, comma-formatted).

## Check-solved (LANE CX, 25 Sept 2026)

Re-verdict per `.claude/briefs/check-solved.md`; the prior 24 Sept 2026 section below (kept, not deleted) did not cite pages read or a controlled search near the verdict word (`tools/intake_gate_check.py` failed on it), so this worker reran the six searches itself.

1. **Web (a).** WebSearch `Sacchetti`-style model-solve check for this target: `Gualterio cardinal cipher "solves" Claude OR GPT decipherment` — no hit for this cipher network (only the unrelated Cyphral Distich and a different, unrelated "Carlo Gualterio" Wikipedia page).
2. **Print edition (b), with control — new lead this pass.** Located HMC's *Calendar of the Stuart Papers* (7 vols, 1902-1923, the standard Stuart-court calendar) on archive.org and full-text searched vol. I (`calendarofstuart01grea`, not access-restricted, `_djvu.txt` fetched directly, no login) for `Gualterio`: 1 matching document, 5 snippet hits (be-api fts) plus the full downloaded text. **Control**: query `Pretender` on the same identifier returns 1 matching document, confirming the search functions. Reading the full local text (not just be-api's 5-snippet cap) around the hits (djvu.txt lines 1155-1163, 2926-2928, page marks "lxii" and the surrounding folio numbers in the printed text) found the editors' own description: "Among the voluminous papers of Cardinal Gualterio in the British Museum (MSS., Additional, Nos. 20,241 to 20,583), purchased in 1854, there are several volumes of correspondence between the Cardinal and James III and Queen Mary. Among them is a volume (No. 20,293) consisting of letters of the Queen and her daughter, the Princess Louisa. Some extracts from these volumes have been printed in *The Fallen Stuarts* by Mr. Head" — and separately, "passages in Card. Gualterio's letters (MSS., Additional, 20,294) show this was the marriage with the niece of the Elector Palatine..." (a paraphrase of ciphered-or-plain content, not itself a decipherment of a ciphered passage). Checked every one of our 14 shelfmarks (comma-formatted, e.g. "20,318") against this volume's full text directly: **no exact match for any of our 14** — the editors describe the *acquisition* (20,241-20,583, which contains 12 of our 14 ranges: 20318-20319 through 20567-20571; only 20634-20635 falls outside it) but do not name our specific volumes or quote ciphered passages from them. This is a real, worker-read edition citation, not a web-search snippet.
3. **Community lists (c).** Tomokiyo's Gualterio page (`cryptiana.web.fc2.com/code/gualterio.htm`) fetched fresh by this worker (not from the local snapshot, which does not carry it) and read in full (1,388 lines of extracted text): covers three cipher reconstructions (D'Estrées Add MS 20359-20361, Medinaceli Add MS 20563, and an undated Gualterio-to-Torcy letter with no BL shelfmark) — grepped the full extracted text for every one of our 14 shelfmarks: **no hit for any of them.**
4. **DECODE (d).** Fresh Aymeloglu clone's cached `catalogue/decode-catalog.csv` grepped for every one of our 14 shelfmarks individually: no hit for any of them (the only Gualterio-network DECODE records remain the D'Estrées and Medinaceli ones above, neither ours).
5. **Bourdeau (e).** Fresh shallow clone's `CATALOGUE.md` grepped for "gualterio": one entry (line 61), "Cardinal Gualterio and Abbé Botti (BL Add MS 20443 (DECODE R8617-R8718, 48 records); catalogue 295): Gualterio cipher tables at the BL (Add MS 20244)" — both 20443 and 20244 are companion volumes in the same acquisition, neither is one of our 14.
6. **Aymeloglu (f).** Same fresh clone: no hit for "gualterio" or any of the 14 shelfmarks anywhere in the repository.

Lessons applied: the wider Gualterio acquisition (20,241-20,583) is now confirmed by a *standard printed calendar*, not only Bourdeau's catalogue note, to be a network with real print engagement (Head's *The Fallen Stuarts*) and at least three reconstructed/interlinear ciphers among its companion volumes (20244, 20359-361, 20443, 20563) — before any of our 14 volumes gets a reading-room request, Head's book and the full 7-volume Calendar run (not just vol. I) should be checked folio-by-folio against our specific shelfmarks, and any volume opened should be checked against Tomokiyo's D'Estrées/Medinaceli keys and Add MS 20244's interlinear-decipherment pattern first (unchanged advice from 24 Sept, now with a second print source to check).

**Verdict: open**, unchanged from 24 Sept 2026, now grounded in a worker-run reading of the standard Stuart-court calendar (pp. lxi-lxii, p. 345) plus a controlled full-text search, not only web-search snippets. Not "new"; not "unpublished" (rule 10) — a search result, not a discovery. Requests this pass: archive.org 4 (1 advancedsearch, 2 be-api fts, 1 direct djvu.txt download, all curl >=1.5s apart, all HTTP 200), `cryptiana.web.fc2.com` 1 (fresh fetch, curl -L with browser UA, 200 after one redirect), WebSearch 1, github.com 0 (reused this batch's shared shallow clones). No BL catalogue calls this pass (still offline post-2023 attack, not retried).

## Prior check-solved sweep, 24 September 2026 (superseded above, kept for the record)

# Cardinal Filippo Antonio Gualterio correspondence, 14 BL volumes — BL Add MS 20318-20635 (selected)

QUEUE row: N41 (`QUEUE.md`, "Candidates not on DECODE").

## Source

British Library, Western Manuscripts, 14 volumes: Add MS 20318-20319, 20338-20339, 20365-20366,
20369-20370, 20371-20380, 20416-20420, 20426-20431, 20466-20467, 20473-20474, 20510-20511, 20554-20556,
20567-20568, 20570-20571, 20634-20635 (1700-1730, it/fr/es). Per the QUEUE row: correspondence to Cardinal
Gualterio (nuncio in Paris 1700-06, then Cardinal Protector of Scotland from 1706 and of England from 1717,
one of the closest advisers to the exiled Stuart court) from French ministers, Spanish/Sardinian ambassadors
and fellow cardinals, most "partly in cipher". Not digitised (`url_tsi` empty on the two representative
volumes the scout checked).

## Check-solved sweep, 24 September 2026

1. **The wider Gualterio Papers is a known, partly-solved cipher network — not itself proof our 14 volumes
   are solved, but decisive context.** This is a single, large BL acquisition (the "Papers of Cardinal
   Gualterio", running roughly Add MS 20238-20649) of which our 14 target volumes are a subset. Three
   independent findings inside that same numeric run:
   - **BL catalogue, Add MS 20244** (`searcharchives.bl.uk/catalog/040-002090511`, fetched 24 Sept 2026):
     Vol. I of despatches to Gualterio as Vice-legate of Avignon and then Nuncio in France, 1697-1700. Quoted
     verbatim: *"Ciphers, with decipherings, occur at ff. 177, 215, 251, 260, and 276."* — i.e. this companion
     volume in the same collection already carries contemporary interlinear decipherments on the leaf, not a
     cipher waiting to be broken.
   - **Bourdeau's `CATALOGUE.md`** (fresh shallow clone, grepped for "gualterio"): lists "Cardinal Gualterio
     and Abbé Botti (BL Add MS 20443 (DECODE R8617–R8718, 48 records); catalogue 295): Gualterio cipher
     tables at the BL (Add MS 20244)" among items moved off his cryptanalysis list because **the key is
     already held** — confirming Add MS 20244 functions as a key volume for this correspondent network, and
     that DECODE already carries 48 records (R8617-R8718) for Add MS 20443, a *different* Gualterio-Papers
     volume (Abbé Botti correspondence, 1708-13) than any of our 14.
   - **Tomokiyo's Cryptiana**, "A Syllabic Cipher (ca.1715) of Cardinal Gualterio Reconstructed Manually"
     (`cryptiana.web.fc2.com/code/gualterio.htm`, fetched live 24 Sept 2026, not in the local snapshot).
     Quoted verbatim: *"the DECODE database has some papers in cipher from his correspondence with others."*
     Tomokiyo has reconstructed a syllabic cipher key from Add MS 20359-20361 (DECODE R8219-R8339, letters of
     Abbé Jean D'Estrées to Gualterio, 1703-1718) and Add MS 20563 (DECODE R8166-R8218, correspondence with
     F. L. de la Cerda and the Duke of Medina Celi, 1706-1725), and separately reconstructed a
     "Gualterio-Torcy Cipher (1718)" from a letter *from* Gualterio to French foreign minister Torcy dated
     Rome, 19 April 1718, "in cipher with interlinear decipherment" (no BL shelfmark given for that one letter
     — plausibly held in French, not British, archives, since Torcy was the recipient).
   - **None of these three shelfmarks (20244, 20443, 20359-20361, 20563) is in our 14-volume list.** Grepped
     `decode-catalog.csv` for every one of our 14 target Add MS numbers individually: no match for any of
     them. **Our specific 14 volumes are not yet on DECODE and not named in Tomokiyo's page or Bourdeau's
     catalogue.**
2. **Editions.** No dedicated printed edition of Gualterio's own Cardinal-era correspondence (1700-1730) was
   found. HMC *Stuart Papers* vol. 1 covers 1716 onward and Gualterio was Cardinal Protector of the Stuarts
   from 1706/1717, but web search found only a general confirmation of his role (Wikipedia), not a specific
   printed calendar entry naming any of our 14 shelfmarks; a companion volume, Add MS 20661 ("letters to
   Cardinal Gualterio, 1728-1744"), turned up in a search for HMC/Jacobite material but is not one of our 14
   either. Searched "Nunziatura di Francia Gualterio Istituto storico" (Italian): the Istituto storico
   italiano's *Nunziature/Acta Nuntiaturae* series has no located Gualterio-period France volume — only
   Bentivoglio's much earlier (1616-21) France nunciature is published in that series. **No dedicated edition
   of any of the 14 volumes found.**
3. **Web, general.** Searched "British Library Add MS 20244 Gualterio cipher" and "Gualterio Papers British
   Library Add MS 20240 cardinal correspondence" (results above); no Cipherbrain or Cipher Mysteries post
   found on Gualterio specifically (search returned unrelated BL cipher items — MS Add 10035, Add 32305).
4. **Community lists.** `sources/cryptiana/web/crypto.htm` (local snapshot) lists the Gualterio page in its
   index; the page itself (fetched live, see above) is the only community-list hit, and it does not name our
   14 volumes.
5. **DECODE.** Cached catalogue grepped for all 14 shelfmarks individually and for "gualterio": only the two
   companion-volume matches above (20244 context via Bourdeau; 20443 direct). No record for any of our 14.
6. **Bourdeau.** Fresh shallow clone; `CATALOGUE.md` hit as above (companion volumes, not ours). No target
   folder in the repository matches "gualterio".
7. **Aymeloglu.** Fresh shallow clone; no hit for "gualterio" or any of the 14 shelfmarks anywhere in the
   repository.

## Edition risk

**Elevated and specifically demonstrated, though not yet resolved for these exact volumes.** This is not an
isolated cipher: it is one network (Gualterio's incoming diplomatic post, 1697-1725+) in which at least two
different correspondents' ciphers are already reconstructed (D'Estrées, Medinaceli) and at least one companion
volume in the same numbered run already carries contemporary decipherings on the leaf (Add MS 20244). Per
CLAUDE.md rule 2 and LESSONS.md ("get the image, not the transcription"), any of our 14 volumes could turn out
the same way — solvable by a key already in hand, or already glossed — well before fresh cryptanalysis is
warranted. The scout's `kind: cryptanalysis` label for N41 should be revisited once a volume is actually opened.

## Verdict

**Open, stage 2 verified unsolved (conditional): none of the 14 target shelfmarks is named in DECODE, in
Tomokiyo's Gualterio page, or in either solver repository, and no printed edition covering them was located
this sweep.** Not "new"; not "unpublished" (rule 10) — a search result, not a discovery. The conditions are:
(a) HMC *Stuart Papers* full run and Add MS 20661 not checked folio-by-folio for overlap with our 14 volumes;
(b) the Istituto storico's published-volumes list not checked directly (inferred from web-search snippets);
(c) whichever volume is opened first should be checked against Tomokiyo's D'Estrées/Medinaceli keys and
against Add MS 20244's interlinear-decipherment pattern before any fresh cryptanalytic attempt, since the same
correspondence network has already yielded both routes elsewhere in this exact collection.

Not digitised (per QUEUE row); a BL reading-room request would be needed to view any volume. No REQUEST.md
drafted this sweep — the QUEUE row's own next-step (named-edition check, then reading-room request for the
Torcy/Acquaviva volumes) is unchanged and is not a copy-order decision for this worker to make.

Requests: BL `searcharchives.bl.uk` 4 (catalog/040-002090980 test hit wrong record, then the search page for
"Add MS 20244 Gualterio", then the full Add MS 20244 record; >=2s apart, well under the 20-request cap).
WebSearch 4 queries. WebFetch 1 (live Tomokiyo Gualterio page, via curl with browser UA after a redirect,
`/tmp` only, not committed). GitHub 2 shallow clones (shared across all four targets in this batch, not
re-cloned per target). No TNA Discovery, no Google Books slot used, no logins, no subagents.

## Next

1. Check HMC *Stuart Papers* (full run, not just vol. 1) and Add MS 20661 against the 14 shelfmarks' named
   correspondents (Torcy, Acquaviva, Ottoboni, ambassadors at Venice/Madrid/Turin/Genoa, Gualterio's nephew as
   Nuncio at Naples) for direct overlap.
2. Before any reading-room request, note in the request that ff. with interlinear decipherment are known
   elsewhere in this exact BL acquisition (Add MS 20244) — ask BL manuscripts staff whether the requested
   volume's description mentions "decipherings" the way 20244's does, which the online catalogue snippet may
   not reproduce in full.
3. If a volume turns out to use the D'Estrées or Medinaceli cipher (same correspondent, or a secretary shared
   across the network), Tomokiyo's published keys are the first thing to try, not fresh cryptanalysis.
