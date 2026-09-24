open

**Check-solved, LANE N4 csKSb, 24 Sept 2026:** letter absent from Gomberville's *Mémoires de Nevers* seconde
partie, *Mémoires de la Ligue* (Goulart) vols 5-6, and *Lettres missives de Henri IV* (Berger de Xivrey vol.4 +
Guadet supplement — checked though the letter runs the wrong direction for that edition, see below). Corrects
QUEUE.md row KS-07 as scKEYS first wrote it: the sender is the Duke of Nevers, the addressee is Henri IV
himself (reversed from "the Court -> Nevers"), and the canvas is 55, not the estimated ~54.

# Nevers to Henri IV, [5 or 6] May 1594 — BnF fr.3990 f.27

QUEUE row: KS-07 (`sources/solver-diffs/2026-09-24-keys-vs-siblings.tsv`, LANE N4 scKEYS, 24 September 2026).
Check-solved run 24 September 2026 by LANE N4 csKSb, brief `.claude/briefs/runs/2026-09-24-lane-n4-csKSb.md`.

## What it is

Louis de Gonzague, duc de Nevers, to Henri IV ("Sire"). BnF fr.3990 (Gallica ark `btv1b90068799`), folio 27 is
canvas 55 of the manifest (confirmed by eye 24 Sept 2026: no folio labels in the manifest; canvas 53 = folio 26
blank verso, canvas 54 = folio 27 verso/docket carrying a later endorsement "Receu le 25 aoust..." dated
"[?] May 1594", canvas 55 = folio 27 recto, the letter itself). The dateline reads "[5 or 6] de May 1594" (the
digit is a compressed cursive form; Tomokiyo reads it as 6, this worker's own reading leans 5 — worth a second
eye-check before a solver commits to either). The clear-text portion (about two-thirds of the page) reports
that Rethel has submitted to the King's obedience through the offices of "Monsieur de Castignac" and that
Nevers is working the towns along the Aisne toward Rocroy and Mézières for the road to Reims; the bottom third
of the page is several lines of dense, unbroken cipher (numeral figures and non-figure symbols), cipher no.60
(Tomokiyo's numbering; key transcribed by Daniel Bourdeau, CC BY 4.0, `nevers1593/key60.txt`).

Tomokiyo, `henryiv2.htm` (WebFetch, 24 Sept 2026): *"(fol.27) Duke of Nevers to Henry IV, 6 May 1594 /
Undeciphered."* No tentative words offered for this one (unlike KS-05/KS-06), and no full plaintext located
this pass.

## Six-source search log (24 September 2026, date checked with `date -u`)

1. **Tomokiyo/Cryptiana.** `henryiv2.htm` quoted above (two independent WebFetch passes). No comments section;
   no reader response recorded on the page.
2. **Print — Nevers's own printed correspondence, actually read.** Gomberville, *Mémoires de messire Louys de
   Gonzague, duc de Nevers* (1665), seconde partie — Google Books `H2eV4wAmIr0C` full-text `SearchWithinVolume`
   for "Castignac" (0 hits) and "Mai 1594" (0 hits); Gallica mirror `bpt6k64451005` `services/ContentSearch` for
   "Castignac" (0 hits) and "Retel"/"Rethel" (12 hits, all generic mentions of the comté/duché de Rethel as part
   of the Nevers title, none the May 1594 submission of the town). Letter absent from the volume.
3. **Print — Lettres missives de Henri IV.** Berger de Xivrey's edition collects only the King's own outgoing
   letters, so a letter addressed *to* the King from Nevers would not be printed there in the King's own voice;
   checked anyway per the brief's routing, on the chance an editorial note quotes or cites it. Internet Archive
   full text (`be-api`): vol.4 (`recueildeslettre04henr`, 1593-95 span) for "Castignac" — 0 hits; the Guadet
   1566-1610 supplément (`bub_gb_m22_ykS5xqYC`) for "Castignac" — 0 hits. Absent from both; this is the weaker
   of the two checks given the direction mismatch, flagged rather than treated as decisive.
4. **Print — Mémoires de la Ligue.** Goulart (1758; the brief names "Goujet", but IA's catalogue and title page
   give Goulart), vols 5-6, full text via `be-api` — 0 hits for "Castignac" across both volumes.
5. **DECODE.** `sources/decode/*.tsv` grepped for "3990" and "nevers": no record.
6. **Bourdeau** (dbourdeau/cyphersolver, shallow clone 24 Sept 2026, HEAD `8fd151d`). `nevers1593/NOTES.md`
   (session of 17 Sept 2026) names fr.3990 f.27 only inside Tomokiyo's inventory of key-no.60 letters, not among
   his own worked pair or his "Remaining gaps" — never opened by his session.
7. **Aymeloglu** (aaymeloglu/unsolved-ciphers, shallow clone 24 Sept 2026): grep for "nevers", "3990" — no
   dedicated target, no catalogue hit.
8. **Web.** WebSearch for Nevers/Revol/1594/chiffre/déchiffré combined with Cipherbrain and Cryptiana — no
   relevant hit beyond Bourdeau's own repository and its two unrelated forks.

## Verdict

open -- Gomberville *Mémoires de Nevers* seconde partie (Google Books `H2eV4wAmIr0C` / Gallica `bpt6k64451005`)
full text and ContentSearch read for "Castignac" and the Rethel context; *Mémoires de la Ligue* (Goulart) vols
5-6 and *Lettres missives de Henri IV* vol.4 + Guadet supplement (all archive.org full text) read for the same
term; letter absent from all four.

## Image

Copy-free. Full native image (4014x5766): `https://gallica.bnf.fr/iiif/ark:/12148/btv1b90068799/f55/full/full/0/native.jpg`.
Modest size tested 24 Sept 2026: `https://gallica.bnf.fr/iiif/ark:/12148/btv1b90068799/f55/full/1000,/0/native.jpg`.
Leaf viewer: `https://gallica.bnf.fr/ark:/12148/btv1b90068799/f55.item`. Docket leaf (canvas 54):
`https://gallica.bnf.fr/iiif/ark:/12148/btv1b90068799/f54/full/1000,/0/native.jpg`.

## Correction to the harvest row

QUEUE.md KS-07 as scKEYS first wrote it gave sender "the Court (unnamed correspondent per henryiv2.htm)" and
canvas "~54, unconfirmed". Corrected here: sender the Duke of Nevers, addressee Henri IV himself, canvas 55.
`kind` stays `recovery`.
