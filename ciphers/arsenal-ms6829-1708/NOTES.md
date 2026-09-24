blocked

# Single "Lettre chiffrée, non déchiffrée" -- Bibliothèque de l'Arsenal, Ms-6829

QUEUE row: M22 (`sources/solver-diffs/2026-09-24-lane-g2-gallica4.tsv`, LANE G2 worker F's archivesetmanuscrits
item-level sweep).

## Source

Bibliothèque de l'Arsenal, **Ms-6829** (196ter. H.F, "Recueil de pièces, XVIIe-XVIIIe siècles"), BnF Archives
et manuscrits notice `ark:/12148/cc87337r`. One named item in the recueil: a ciphered letter dated **5 January
1708**, catalogued by the cataloguer's own words as **not yet deciphered** ("non déchiffrée"). No sender,
recipient, key or sibling decipherment is named in the catalogue text carried into the QUEUE row. This is the
harvest's own text; per the brief, gallica.bnf.fr and archivesetmanuscrits.bnf.fr were not re-fetched this
pass (LANE G2 has two fetchers on that host already) -- the item page was not opened, no image viewed.

## Check-solved sweep (24 September 2026)

1. **Search engine.** `"Arsenal" "6829" chiffrée OR "non déchiffrée" 1708` -- the only shelfmark-specific hits
   are the BnF Archives et manuscrits notice itself (`cc87337r/cd0e1303`, `cc87337r/cd0e230`); no cipher blog,
   forum or scholarly page discusses this item. No sender/recipient is named, so no correspondent-specific
   search (printed correspondence, calendars) could be run this pass -- a genuine gap, not a checked-and-clear
   result, flagged for whoever opens the image and can read a name from the letter itself.
2. **Printed correspondence / calendars.** Not run: no correspondent identified in the catalogue text to
   search by name.
3. **Cryptiana.** Local snapshot (`sources/cryptiana/`) grepped for "Arsenal", "6829", "Ms-6829": the only
   "Arsenal" hits (`spanish3D.htm`, `venetian.htm`) are unrelated mentions of the Arsenal library in a
   bibliography title, not this item.
4. **Cipherbrain.** `cipherbrain OR klausis "Arsenal" chiffre 1708 OR 1713 OR 1745 unsolved` -- no hit naming
   this item or shelfmark; returned Cipherbrain's generic unsolved-cipher index pages only.
5. **DECODE.** Aymeloglu's cached `catalogue/decode-catalog.csv` (10,107 rows, fresh shallow clone this
   session) grepped for "arsenal": no hit. This repo's own local harvest
   (`sources/decode/records-non-decrypted-2026-09-24.tsv`, 1187 rows) also has no "arsenal" row.
6. **Solver repositories.** Fresh shallow clones of both `dbourdeau/cyphersolver` and
   `aaymeloglu/unsolved-ciphers` this session, grepped for the shelfmark ("Ms-6829", "Arsenal 6829") and the
   ark (`cc87337r`) exactly, not just the bare number (which coincidentally appears in dozens of unrelated
   filenames/JSON blobs in both repos, e.g. `feats.npy`, `manifest_btv1b9060633d.json`): zero exact matches in
   either repo.

## Verdict

**Open, stage 2 verified unsolved (conditional).** Not found in a search engine, Cryptiana, Cipherbrain,
DECODE's cached catalogue, or either solver repository, searched by shelfmark and ark on 24 Sept 2026. The
cataloguer's own "non déchiffrée" note is itself only a catalogue-level claim, not an image-confirmed reading
of the leaf -- not yet checked against the image. Conditional because: (a) no correspondent name is available
to check against printed correspondence or calendar series -- this needs the image; (b) the catalogue text
itself, not the leaf, is all that has been read this pass.

Requests: WebSearch 2 queries. github.com 2 shallow clones (grepped locally, no further requests). No
gallica.bnf.fr, no archivesetmanuscrits.bnf.fr fetch (per brief, LANE G2 owns that host this pass). No
subagents.

## Digitisation check (24 Sept 2026, LANE G2 worker O)

**Digitised: no** (finding aid without DAO; SRU `gallica all "Arsenal Ms-6829"` 571 records, none a
`dc:source` match; 24 Sept 2026). Fetched the archivesetmanuscrits finding aid
(`https://archivesetmanuscrits.bnf.fr/ark:/12148/cc87337r`) in full: the site's own digitised-item marker
(`avecDaoGal`/"Consultable sur gallica") is defined in the page's stylesheet but applied to no element on this
record, and the page carries no `gallica.bnf.fr` href anywhere. Confirmed independently with the Gallica SRU
query above (arsenal6314-hanau-1635 precedent method): none of the 571 hits' `dc:source` values name Ms-6829.
The finding aid's only reservation link is `reservationrao.bnf.fr/submitCote?...Cote=Ms-6829&typecote=orig` --
original only, no `typecote=sub` (microfilm) offered, unlike M23/Ms-6314's MICROFILM ARS R-242218. Wrote
`REQUEST.md`. Status set to blocked.

Requests this section: archivesetmanuscrits.bnf.fr 1, gallica.bnf.fr 3 (the SRU query above needed 2
tunnel-reset retries, `ws_closed_mid_exchange`, before the 200 that returned the 571 hits checked).
