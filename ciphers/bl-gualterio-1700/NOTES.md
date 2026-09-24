open

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
