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

## Web and blog check (GF-A2-11, 3 Oct 2026)

Run for LANE-A2PUSH (account 2), 3 Oct 2026, 00:27-00:33 UTC. WebSearch (plain web); hits checked against the BL
catalogue's own JSON records (`searcharchives.bl.uk/catalog/<id>?format=json`), which answer from the cloud.

(a) Plain web searches, four:
1. `Cardinal Gualterio correspondence cipher deciphered British Library Add MS Torcy 1700` -- hits: BL searcharchives
   records 036-002090595 (**Add MS 20318-20319, Torcy to Gualterio, one of our 14**), 040-002090908 (Add MS 20582,
   cipher tables), 036-002090711 (**Add MS 20416-20420, one of our 14**), 040-002091026, 040-002090616; NLI Sources
   records MS UR 036390/036392/066514/012536/043042 (Irish-interest index entries for the same BL volumes).
2. `"Add MS 20318" OR "Add MS 20371" OR "Add MS 20416" Gualterio cipher` -- BL records 040-002090908, 036-002090651
   (**Add MS 20365-20366, one of our 14**), 040-002090951, 040-002091026, 040-002090678, 040-002090609, 036-002090510;
   NLI Sources as above.
3. `Gualterio Papers British Library letters to Cardinal Gualterio in cipher Jacobite decipherment` -- BL records
   040-002090609/678/584/571, 036-002090651, 040-002023079/063/064; NLI MS UR 012536.
4. `Filippo Antonio Gualterio nunzio Parigi lettere cifrate decifrazione cardinale` -- Wikipedia (the cardinal), BL
   records 040-002090951/637, 036-002090651/619, 032-002090506; NLI.
(The 25 Sept section above also ran the model-solve query `Gualterio cardinal cipher "solves" Claude OR GPT`: no hit.)
No modern decipherment, blog post or paper reading any of the 14 volumes was found; every substantive hit is the BL's
own catalogue -- which, read in full below, states that 11 of the 14 volume groups carry **period decipherings** on
the leaf (Premise check (a)/(c)).

(b) Blog site searches:
- Cipherbrain: `site:scienceblogs.de Gualterio` -- no scienceblogs.de page returned (Wikipedia, BL records, VIAF only).
- Cryptiana: `site:cryptiana.blogspot.com Gualterio` -- no blog page returned. Tomokiyo's site page
  `cryptiana.web.fc2.com/code/gualterio.htm` was read in full by LANE CX (25 Sept 2026, above): its keys are for Add MS
  20359-20361 (D'Estrées), 20563 (Medinaceli) and one Gualterio-to-Torcy letter of 19 Apr 1718 with interlinear
  decipherment (no shelfmark) -- none of our 14 named.
- Cipher Mysteries: site search `ciphermysteries.com/?s=Gualterio` (WebFetch): "Nothing Found".

(c) Opened: the BL records above (JSON, full scope-and-content text). No blog post exists to open, so no comment thread
was read. Result: no modern decipherment found; the period decipherings are the BL's own description (below).

## Premise check (GF-A2-11, 3 Oct 2026)

**Finding: the BL's own catalogue describes period decipherings in 11 of the 14 target volume groups.** Each record
was read this pass from `searcharchives.bl.uk/catalog/<id>?format=json` (scope and content, verbatim except
abridged with "..."):

| volumes | BL record | correspondent | BL's words on cipher |
|---|---|---|---|
| 20318-20319 | 036-002090595 | Torcy, 1700-1726 | "Many in cipher, with deciphering." |
| 20338-20339 | 036-002090619 | Abbé de Pomponne (Venice, Paris), 1706-1730 | "Many partially in cipher, with decipherings." |
| 20365-20366 | 036-002090651 | M. Amelot (Madrid, Rome, Paris), 1705-1724 | "Many of the letters in Vol. I. contain portions in cipher, with decipherings" |
| 20369-20370 | 036-002090656 | de la Tour Guion, Bp of Cavaillon, 1707-1725 | "Partly in cipher, with decipherings." |
| 20371-20380 | 036-002090659 | Abbate Tamisier, 1706-1728 | "Some in cipher, with decipherings." |
| 20416-20420 | 036-002090711 | Card. Acquaviva, 1706-1724 | "Some in cipher, with decipherings." |
| 20426-20431 | 036-002090722 | Abbate Albicini, 1707-1718 | "a few in cipher, with decipherings." |
| 20466-20467 | 036-002090767 | Card. Ottoboni, 1706-1726 | "many in cipher, with decipherings." |
| 20473-20474 | 036-002090775 | Abbate Simonetti, 1706-1724 | "Some in cipher, with decipherings." |
| 20567-20568 | 036-002090887 | Spinola, Marqués de los Balbases, 1706-1721 | "a few in cipher, with decipherings." |
| 20570-20571 | 036-002090891 | Marqués de Villamayor, 1703-1721 | "a few in cipher, with decipherings." |
| 20510-20511 | 036-002090819 | Marquis Bentivoglio, 1707-1717 | "Many in cipher." (no decipherings named) |
| 20554-20556 | 036-002090872 | Count de Vernon, 1713-1727 | "many in cipher." (no decipherings named) |
| 20634-20635 | 036-002090968 | Abp of Myra (L. Gualterio), drafts, 1744-1753 | "DRAFTS of letters ... to be written in cipher, or in answer to letters in cipher" -- the clear side |

- **(a) Decipherments the folder already mentions: found, and now pinned to our volumes.** The folder knew Add MS
  20244's "Ciphers, with decipherings" (a companion volume) and drafted REQUEST.md to *ask* the BL whether 20318-20319
  had the same note. The BL's public record already answers it: yes, for 20318-20319 and ten more groups (table).
  The 24 Sept "Not digitised ... url_tsi empty" reading used the catalogue snippet, not the full scope-and-content field.
  Caveat: catalogue level, not leaf level -- "some"/"a few"/"many ... with decipherings" does not say every cipher
  passage is deciphered; whether any ciphered passage lacks a deciphering is unknown until a volume is seen.
- **(b) Other solvers' working files: not found.** dbourdeau/cyphersolver HEAD 2341682 (2 Oct 2026): `CATALOGUE.md`
  line for Gualterio/Botti (Add MS 20443, DECODE R8617-R8718; cipher tables Add MS 20244), moved off his list as "key
  already held"; no target folder, output or key run on any of our 14. aaymeloglu/unsolved-ciphers HEAD d2800bb (27
  Sept 2026): `catalogue/decode-catalog.csv` has Gualterio-network DECODE rows (the D'Estrées/Medinaceli/Botti
  volumes already named above), none of our 14 shelfmarks; no working files.
- **(c) Physical neighbours: found -- key tables.** Add MS 20582 (BL record 040-002090908): "TABLES of ciphers, used by
  Card. Gualterio in his correspondence with various persons, viz.: Cardinal Acquaviva, f. 3 b. M. Amelot, f. 5 b. The
  Comte du Luc ... f. 7 b. ..." -- the cardinal's own key book in the same acquisition, covering at least two of our
  correspondents; its full list (read this pass, to f. 85 b) names five of our correspondents: Acquaviva f. 3 b
  (20416-20420), Amelot f. 5 b (20365-20366), "Comte de Vernon" f. 74 b (20554-20556 -- one of the two groups whose
  record names no decipherings, so its key is in hand), "Villamayor" f. 78 (20570-20571), and "Cardinal Bentivoglio"
  f. 11 b (our 20510-20511 is the Marquis Luigi Bentivoglio, not the cardinal: a possible, unconfirmed match).
  Torcy, Pomponne, Cavaillon, Tamisier, Albicini, Ottoboni, Simonetti and Balbases are not in its list. Add MS 20244-20265 (nunciature despatches, "in cipher, with decipherings") and 20387,
  20329, 20620, 20681 (all "with decipherings", one "with a key prefixed") show the same practice through the papers.
  No leaf images: the BL has served no manuscript images online since the 2023 attack.
- **(d) Recipient's side: found -- Gualterio is the recipient, and his own office deciphered.** The decipherings above
  are the recipient's. Sender-side editions not searched this pass (Torcy's correspondence in the AE Correspondance
  politique Rome series, Ottoboni's and Acquaviva's papers); HMC Stuart Papers vol. I was read by LANE CX (25 Sept).

**Consequence (for the orchestrator, not acted on here):** for 11 of the 14 volume groups the plaintext of the
ciphered passages was written out at the time on or with the letters, so they are a key-recovery/alignment problem
(period key, grade H/C from the decipherings), not open cryptanalysis -- the same shape as 20244. Flagged in ROOM.md to
the account-3 orchestrator. Status line not changed by this worker (brief: status changes are the orchestrator's).
Bentivoglio (20510-20511) and Vernon (20554-20556) name no decipherings, but Vernon's key is in Add MS 20582 f. 74 b; 20634-20635 are clear drafts. REQUEST.md's
question to the BL is now answered from the public catalogue; its pilot choice stands but the ask can drop the
"does the description mention decipherings" clause.

Requests: searcharchives.bl.uk 33 (10 catalog JSON records, 12 search JSON, 11 catalog JSON; full scope texts saved to `bl_catalogue_2026-10-03.tsv`; 2 s apart, all HTTP 200),
ciphermysteries.com 1 (WebFetch site search), WebSearch 6.

`python3 tools/intake_gate_check.py bl-gualterio-1700` after both sections (3 Oct 2026, GF-A2-11): `bl-gualterio-1700: open (line 1) -- edition/page or full-text-search citation found within 6 lines`, exit 0 (exit 1 before).

## Next step (costed, CS-BATCH5, 3 Oct 2026)

Re-read of the verdict and premise check above, with no new search (both were completed 3 Oct 2026 and gate exit 0). Cheapest next step: send the REQUEST.md question to the BL (owner-side email, ~USD 0 agent cost) asking for the folio list of the leaves still in cipher, then a ~USD 3 transcription batch on one pilot volume once images or a copy arrive. Status unchanged (`open`).

## While waiting

- Fetch Add MS 20582 (the cardinal's key book) scope text and the Stuart Papers calendar entries for the Vernon group from the BL catalogue JSON already on disk (`bl_catalogue_2026-10-03.tsv`) and list which correspondents have a period key named; depends on nobody (~USD 0.5).

## D4-GUALT (6 Oct 2026, worker for LANE DEFAULT-account-4-20261006-1235)

Job: Add MS 20582 scope text and the Vernon-group Stuart Papers calendar entries, from disk. Search result only; status stays `open`.

- **Disk row truncated.** `bl_catalogue_2026-10-03.tsv` carries only 677 characters of the 20582 scope (ends at "Gergy ... f. 33 b, 35"), so the Vernon entry (f. 74 b) was not on disk. One request to `searcharchives.bl.uk/catalog/040-002090908.json` (HTTP 200) returned the full 1,777-character text. Request count: searcharchives.bl.uk 1.
- **Result:** `gualterio_20582_keylist_2026-10-06.tsv`, 34 key-table entries by folio (ff. 3 b to 85 b, last two "Uncertain"). Against our 14 volume groups:
  - Named in the key book (4 firm): Acquaviva f. 3 b (20416-20420), Amelot f. 5 b (20365-20366), **Comte de Vernon f. 74 b (20554-20556)**, Villamayor f. 78 (20570-20571).
  - Possible, unconfirmed (3): "Cardinal Bentivoglio" f. 11 b (ours is Marquis Luigi Bentivoglio, 20510-20511); "Chevalier du Bourck" f. 15 b (ours is du Bourg, 20335); "Cardinale della Trimoille" f. 69 b (our 20329 is Gualterio's drafts *to* Trémoille, so the key may be the same but the item is not a correspondent's letters). The 3 Oct section named five, so du Bourg and Trémoille are additions from this read.
  - Not in the list: Torcy, Pomponne, Cavaillon, Tamisier, Albicini, Ottoboni, Simonetti, Balbases, Furietti (20681), and the 20244/20387/20620/20634 items.
  - The record gives only folios and names. No key content, no dates for the tables beyond Cennini's addition of 29 Oct 1723, no images online (BL not serving manuscript images since 2023).
- **Vernon in the BL record 20554-20556:** Count F. de Vernon, Sardinian Minister in France 1719-1723, to Gualterio, 31 Jan. 1713-15 Jan. 1727, Italian, "many in cipher", with a few letters of his wife and two of his brother (Turin, 7 Aug. 1726 and 12 Feb. 1727, end of vol. III). The record names no decipherings, consistent with his key being at 20582 f. 74 b.
- **Stuart Papers calendar entries for the Vernon group: not found on disk, not fetched.** Nothing in this folder or `sources/` holds a HMC Stuart Papers entry for Vernon; the only HMC reading on file is vol. I pp. lxi-lxii and p. 345 (above), which names no individual shelfmark. The brief limits fetches to the BL catalogue JSON, so the calendar volumes (archive.org `calendarofstuart01grea` and later volumes, 7 in all) were not searched. Next step if wanted: grep the `_djvu.txt` of the seven volumes for "Vernon" (IA full text, ~7 requests, ~USD 0.5), a separate job.
