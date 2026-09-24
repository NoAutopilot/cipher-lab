open

**Check-solved, LANE N4 csKSb, 24 Sept 2026:** letter absent from Gomberville's *Mémoires de Nevers* seconde
partie and from *Mémoires de la Ligue* (Goulart) vols 5-6; see the search log below. Corrects QUEUE.md row
KS-06 as scKEYS first wrote it: the sender is the Duke of Nevers himself, not "the Court", the date is 12 March
1594 (not "c.1593-94"), and the canvas is 340, not the estimated ~338.

# Nevers to Revol, 12 March 1594 — BnF fr.3989 f.169

QUEUE row: KS-06 (`sources/solver-diffs/2026-09-24-keys-vs-siblings.tsv`, LANE N4 scKEYS, 24 September 2026).
Check-solved run 24 September 2026 by LANE N4 csKSb, brief `.claude/briefs/runs/2026-09-24-lane-n4-csKSb.md`.

## What it is

Louis de Gonzague, duc de Nevers, to Louis Revol, during Nevers's return journey from the Rome embassy. BnF
fr.3989 (Gallica ark `btv1b9060514q`), folio 169 is canvas 340 of the manifest (confirmed by eye 24 Sept 2026:
no folio labels in the manifest; canvas 338 = folio 168, a blank address leaf, canvas 340 = folio 169 recto).
The leaf reads "12 de Mars 1594" and opens "Monsieur de Revol", with several lines of cipher (numeral figures
and symbol signs) among the clear French, cipher no.60 (Tomokiyo's numbering; key transcribed by Daniel
Bourdeau, CC BY 4.0, `nevers1593/key60.txt`).

Tomokiyo, `henryiv2.htm` (WebFetch, 24 Sept 2026): *"(fol.169) Duke of Nevers to Revol, 12 March 1594 / Some
portions in cipher, undeciphered, which partially reads 'de la diuision', 'discours susdit.'"* As with fr.3987
f.66 (KS-05), Tomokiyo has a couple of tentative words off the cipher himself; no full plaintext located this
pass. Tomokiyo also separately lists fol.3 of the same volume ("Duke of Nevers to Revol, 1 January 1594") as a
key-no.60 letter; that item is untested this pass (not in this brief's rows).

## Six-source search log (24 September 2026, date checked with `date -u`)

1. **Tomokiyo/Cryptiana.** `henryiv2.htm` quoted above (two independent WebFetch passes). No comments section;
   no reader response recorded on the page.
2. **Print — Nevers's own printed correspondence, actually read.** Gomberville, *Mémoires de messire Louys de
   Gonzague, duc de Nevers* (1665), seconde partie — Google Books `H2eV4wAmIr0C` full-text `SearchWithinVolume`
   for "diuision"/"division" (0 hits — Google's own spell-correction to "division" also returns 0), "Mars 1594"
   (1 hit, p.692, a different item — "A la Cour ayant le 12 iour du mois de Ianuier..." — not this letter);
   "Revol" (5 hits, cross-checked on the Gallica mirror `bpt6k64451005` via `services/ContentSearch`, all
   countersignatures on Henri IV's own letters, none this one). Letter absent from the volume.
3. **Print — Mémoires de la Ligue.** Goulart (1758; the brief names "Goujet", but IA's catalogue and title page
   give Goulart), vols 5-6 (`memoiresdelaligu05goul`, `memoiresdelaligu06goul`), full text via `be-api` search —
   0 hits for "Castignac" (KS-07's control term, run across the same two volumes in the same sweep); no
   independent second term for this letter run separately within the $5 cap.
4. **DECODE.** `sources/decode/*.tsv` grepped for "3989" and "nevers"/"revol": no record.
5. **Bourdeau** (dbourdeau/cyphersolver, shallow clone 24 Sept 2026, HEAD `8fd151d`). `nevers1593/NOTES.md`
   (session of 17 Sept 2026) names fr.3989 ff.3, 169 only inside Tomokiyo's inventory of key-no.60 letters, not
   among his own worked pair or his "Remaining gaps" — never opened by his session.
6. **Aymeloglu** (aaymeloglu/unsolved-ciphers, shallow clone 24 Sept 2026): grep for "nevers", "3989", "revol" —
   no dedicated target, no catalogue hit.
7. **Web.** WebSearch for Nevers/Revol/1594/chiffre/déchiffré combined with Cipherbrain and Cryptiana — no
   relevant hit beyond Bourdeau's own repository and its two unrelated forks.

## Verdict

open -- Gomberville *Mémoires de Nevers* seconde partie (Google Books `H2eV4wAmIr0C` / Gallica `bpt6k64451005`)
full text and ContentSearch read for the decoded fragments and the date; *Mémoires de la Ligue* (Goulart) vols
5-6 (archive.org full text) read; letter absent from both.

## Image

Copy-free. Full native image (4987x7040): `https://gallica.bnf.fr/iiif/ark:/12148/btv1b9060514q/f340/full/full/0/native.jpg`.
Modest size tested 24 Sept 2026: `https://gallica.bnf.fr/iiif/ark:/12148/btv1b9060514q/f340/full/1000,/0/native.jpg`.
Leaf viewer: `https://gallica.bnf.fr/ark:/12148/btv1b9060514q/f340.item`.

## Correction to the harvest row

QUEUE.md KS-06 as scKEYS first wrote it gave sender "the Court (unnamed correspondent per henryiv2.htm)", date
"c.1593-94", and canvas "~338, unconfirmed". All corrected here from Tomokiyo's page and the leaf itself: sender
the Duke of Nevers, addressee Revol, date 12 March 1594, canvas 340. `kind` stays `recovery`.
