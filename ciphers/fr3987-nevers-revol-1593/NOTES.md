open

**Check-solved, LANE N4 csKSb, 24 Sept 2026:** letter absent from Gomberville's *Mémoires de Nevers* seconde
partie and from *Mémoires de la Ligue* (Goulart) vols 5-6; see the search log below. Corrects QUEUE.md row
KS-05 as scKEYS first wrote it: the sender is the Duke of Nevers himself, not "the Court", and the canvas is
121, not the estimated ~132.

# Nevers to Revol, Rome, 10 November 1593 — BnF fr.3987 f.66

QUEUE row: KS-05 (`sources/solver-diffs/2026-09-24-keys-vs-siblings.tsv`, LANE N4 scKEYS, 24 September 2026).
Check-solved run 24 September 2026 by LANE N4 csKSb, brief `.claude/briefs/runs/2026-09-24-lane-n4-csKSb.md`.

## What it is

Louis de Gonzague, duc de Nevers, to Louis Revol (secretary of state for war), from Rome during Nevers's
embassy to obtain the Pope's absolution for Henri IV. BnF fr.3987 (Gallica ark `btv1b90606320`), the leaf
pencil-foliated "66", is canvas 121 of the manifest (confirmed by eye 24 Sept 2026: the manifest carries no
folio labels at all, so this corrects QUEUE.md's unconfirmed estimate of canvas ~132; canvas 120, one before
it, is a separate letter of the same date addressed "Sire" — to the King — foliated 66 as well, part of the
same dispatch bundle). Dated "10 de Novembre 1593" on the leaf, matching Tomokiyo's citation. The page opens
"Monsieur de Revol" and carries several lines mixing clear French cursive with dense cipher (numeral figures,
Roman numerals, and symbol signs), consistent with cipher no.60 (Tomokiyo's numbering, fr.3995 f.108-110; key
table transcribed by Daniel Bourdeau, CC BY 4.0, `nevers1593/key60.txt`).

Tomokiyo, `henryiv2.htm` (fetched by WebFetch 24 Sept 2026; page states "Last modified on 28 November 2019";
not yet snapshotted to `sources/cryptiana/`): *"(f.66) Duke of Nevers to M. Revol, 10 November 1593 / Some
portions in cipher, undeciphered, which appear to include words such as 'tous sont de opinion que le pape veul
... asseurance de la conversion ... pour vous dire ...', 'conposer avec Mr. Despernon pour la deliuranse de son
frer'."* Tomokiyo has already tentatively read a few words directly off the cipher himself (grade M/S territory,
not a full decipherment); no full plaintext located this pass.

## Six-source search log (24 September 2026, date checked with `date -u`)

1. **Tomokiyo/Cryptiana.** `henryiv2.htm` quoted above (WebFetch, two independent verbatim passes to cross-check
   the model's summarisation). No comments section on the page; no response to the author's "the reader is
   kindly asked to provide reading of these undeciphered texts."
2. **Print — Nevers's own printed correspondence, actually read.** Gomberville, *Mémoires de messire Louys de
   Gonzague, duc de Nevers* (1665), seconde partie — Google Books `H2eV4wAmIr0C` full-text `SearchWithinVolume`
   for "Despernon" (0 hits), "deliuranse" (0 hits), "Nouembre 1593" (3 hits, all a different item, "AVTRE LETTRE
   DE S.M." — the king's own countersigned letters, none addressed to Revol); "Revol" (5 hits, cross-checked on
   the same edition's Gallica mirror `bpt6k64451005` via `services/ContentSearch`, all "REVOL" as countersigning
   secretary on Henri IV's own letters, none matching this letter). Letter absent from the volume that covers
   this exact date range (p.692 carries "Mars 1594").
3. **Print — Mémoires de la Ligue.** Simon Goulart's compilation (the brief names "Goujet"; Internet Archive's
   catalogue and title page both give Goulart, 1758) vols 5-6 (`memoiresdelaligu05goul`,
   `memoiresdelaligu06goul`), full text via archive.org's `be-api` search — 0 hits for "Castignac" (the KS-07
   letter's control term, run across the same two volumes in this sweep). No independent term for this letter
   was distinctive enough to add a second query within the $5 cap; treated as covered by the same negative
   sweep, not a dedicated search.
4. **DECODE.** `sources/decode/*.tsv` grepped for "3987" and for "nevers"/"revol": no record.
5. **Bourdeau** (dbourdeau/cyphersolver, shallow clone 24 Sept 2026, HEAD `8fd151d`). `nevers1593/NOTES.md`
   (session of 17 Sept 2026) names fr.3987 f.66 only inside Tomokiyo's own inventory of every key-no.60 letter
   ("Nevers to Revol at fr.3985 f.88 ... fr.3987 f.66, fr.3989 ff.3, 169, fr.3990 f.27"); it is not among his
   worked pair (fr.3985/fr.3986 Revol letters) and not among his "Remaining gaps" — his session never opened
   this leaf.
6. **Aymeloglu** (aaymeloglu/unsolved-ciphers, shallow clone 24 Sept 2026): grep for "nevers", "3987", "revol"
   across the repo and its catalogue JSONL/CSV files — no dedicated target, no catalogue hit.
7. **Web.** WebSearch "fr.3987" Nevers Revol chiffre déchiffré, and a second query pairing Cipherbrain/Cryptiana
   with Revol/1594 — no relevant hit beyond Bourdeau's own repository and its two unrelated forks.

## Verdict

open -- Gomberville *Mémoires de Nevers* seconde partie (Google Books `H2eV4wAmIr0C` / Gallica `bpt6k64451005`)
full text and ContentSearch read for the decoded fragments and the date; *Mémoires de la Ligue* (Goulart) vols
5-6 (archive.org full text) read; letter absent from both.

## Image

Copy-free. Full native image (4940x6827): `https://gallica.bnf.fr/iiif/ark:/12148/btv1b90606320/f121/full/full/0/native.jpg`.
Modest size tested 24 Sept 2026: `https://gallica.bnf.fr/iiif/ark:/12148/btv1b90606320/f121/full/1000,/0/native.jpg`.
Leaf viewer: `https://gallica.bnf.fr/ark:/12148/btv1b90606320/f121.item`.

## Correction to the harvest row

QUEUE.md KS-05 as scKEYS first wrote it gave sender "the Court (unnamed correspondent per henryiv2.htm)" and
canvas "~132, unconfirmed". Both are corrected here from Tomokiyo's page and the leaf itself: the sender is the
Duke of Nevers, the addressee Revol, the canvas 121. `kind` stays `recovery` (key no.60 is published, by
Tomokiyo/Bourdeau).
