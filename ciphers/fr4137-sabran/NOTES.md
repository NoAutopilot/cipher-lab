# BnF Français 4137, f.129: "Memoyre que Mr de Sabran a envoyé en chiffre", 1637

closed-negative

Check-solved sweep, 23 September 2026 (~23:50 UTC; `date -u` read before writing). QUEUE row M10. Worker:
check-solved M8-M11 (Sonnet, cap $8 across all four targets).

## What the leaf actually is

BnF fr.4133-4138 is catalogued as a "**Recueil de copies** de pieces relatives aux ambassades du Sr de Sabran
en Allemagne, a Genes, en Italie et en Angleterre" -- a register of **copies**, not the ambassador's original
correspondence. Fr.4137 within it is "Livre des lettres et negociations de Mr de Sabran... Annees 1637 et
1638."

Finding aid (`archivesetmanuscrits.bnf.fr/ark:/12148/cc505343`, fetched 23 Sept 2026): "Fol. 128 - 112 Memoyre
que Mr DE SABRAN a envoye en chiffre a S. A. de Savoye, a Mr de Bordeaux et a Mr d'Hemery, le 3e??? septembre."

The leaf itself, viewed via Gallica IIIF (`images/f129_memoyre_plaintext.jpg`, canvas f133; the finding aid's
folio numbers ran one leaf ahead of the pencil foliation actually visible -- the item sits on **folio 129**, not
128, which is instead the tail of the preceding item; canvas-to-folio calibration in `images/manifest.json`),
carries the item's own heading in the clerk's hand: **"Memoyre que M. de Sabran a envoye en chiffre a S.A. de
Savoye, a M. de Bordeaux, et a M. d'Hemery, le 30 septembre 1637 et a La Tour."** The date in the heading (30
September) does not match the finding aid's damaged "3e??? septembre" reading -- the finding aid's own "???"
already flags this as uncertain; the leaf gives the real date.

**Everything below that heading, filling the rest of this page and the whole of the facing page, is plain
French prose** -- a first-person memoir/briefing text ("Mon nome Constance grand vous le mois d'avril..."),
readable straight through, with no cipher symbols, numerals, or ciphertext of any kind anywhere on the leaf.
The two neighbouring canvases (f132 = folio 128, the tail of the prior Chavigny letter; f134 = folio 130, the
start of the next Chavigny letter) are likewise entirely plain French, confirming this isn't a stray
mis-paged cipher passage sitting one leaf off.

**Conclusion: the catalogue's "en chiffre" describes how the original memo was transmitted in 1637, not the
state of the copy preserved here.** This "Recueil de copies" register holds the chancery's plain-text copy of
the memo's content (very likely made from the deciphered original, or from a working draft kept before
encipherment) -- the ciphertext itself does not survive in this manuscript. This is the same situation as
QUEUE M2 (Clairambault 351, "Chiffre du duc de Paliano" -- key present, no ciphertext letter) and M5
(Clairambault 361 -- two keys, no ciphertext), just the mirror image (plaintext present, no ciphertext).

## Editions and prior art

Not pursued beyond the leaf view: once no ciphertext survives, there is nothing here for cipher-lab to attempt,
and rule 1's edition search is not a productive use of budget on a non-target. `sources/cryptiana/web/` was
grepped for "Sabran"/"4137" earlier in this sweep (hits in GL.htm, servien.htm, variable2.htm, louisxiii.htm,
spanish2.htm) but not read in detail, since the image check already settles the verdict; if a future worker
wants Sabran's 1637 Savoy-front content for its own sake (the memo is a real, dateable diplomatic document),
those Cryptiana hits and the finding aid's full fr.4133-4138 item list are the starting point.

## Verdict

**Closed-negative: no ciphertext survives in this manuscript to attempt.** Not "unsolved" in the cipher-lab
sense -- there is nothing to solve here, only a plain-text register copy of a document that was once
enciphered. Do not promote to the board. QUEUE M10 should be dropped from the cryptanalysis/recovery lanes,
per the M2/M5 precedent.

Stage: not advanced past scout (no stage-2 verified-unsolved claim applies to a non-cipher item).

## Requests this pass

gallica.bnf.fr: 1 IIIF manifest.json, 5 IIIF image fetches (2 connection resets, each retried once after a
pause). archivesetmanuscrits.bnf.fr: 1 finding-aid page (`cc505343`, covering fr.4133-4138; shared with no
other target this sweep). No logins, no credentials used, no subagents.
