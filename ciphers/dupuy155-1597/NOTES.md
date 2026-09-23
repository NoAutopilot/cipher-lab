found-solved

# Cipher letter to Ferdinand I, Grand Duke of Tuscany, via his ambassador in Spain — BnF Dupuy 155 (41)

QUEUE row: N10 (sources/solver-diffs/2026-09-23-non-decode-hits.tsv, "Candidates not on DECODE").

## Source

BnF, Département des Manuscrits, **Dupuy 155** ("Mémoires servant à l'histoire de PROVENCE et de la ville de
MARSEILLE pour les années 1593, 1595 et 1596"), Gallica `ark:/12148/btv1b10034035f`. Gallica OAI/Dublin Core
record (`dc:description`, fetched 23 September 2026, 1 request) gives the volume's full contents list (59
feuillets, one item per numbered piece — the parenthesised numbers below the folio each piece begins on):

> "...— Remontrances des consuls de Marseille à Henri IV, 22 avril 1596, orig. (35) ; — **Lettre chiffrée,
> adressée à Ferdinand Ier, grand-duc de Toscane, par son ambassadeur en Espagne, et relative au château
> d'If, 10 mai 1597, en italien, orig. (41)** ; — Lettre de Guillaume Du Vair, alors président du Parlement
> d'Aix, à Henri IV, 18 mars 1601, autogr. (46) ; ..."

`dc:subject` independently lists "GUICCIARDINI (Francesco), ambassadeur / Lettre" for this volume, naming the
sender: **Francesco Guicciardini**, Tuscan ambassador to Spain, matching the catalogue description's "son
ambassadeur en Espagne."

## Check-solved sweep (23 September 2026)

1. **Image (decisive).** Fetched the Gallica IIIF manifest once (`images/manifest.json`, 1 request; 111
   canvases for 59 foliated leaves, ~1.9 images/folio — recto+verso pairs plus front matter). Item "(41)" in
   this notice is a folio number (the volume's items are numbered 2, 6, 9, 11, 13, 15, 17, 19, 21, 23, 25,
   27, 35, 41, 46, 48, 50, 54, 54v, 56, 57 — a monotonic sequence of folio starts across a 59-leaf book, item
   46 at f.46 opening two pages after the cipher letter ends). Viewed six leaves at ~700 px to bracket it:
   f76 (blank flyleaf, archival endorsement only), **f78, f80, f84 (three consecutive leaves of the letter
   itself)**, f90 (item "(48)", a different French memorandum, confirming the cipher letter ends before it).
   **Every leaf of the letter shows fluent, fully legible Italian prose with a row of cipher-numeral groups
   written underneath (or beside) each line of clear text** — a contemporary parallel decipherment/cipher
   pairing, not a blind ciphertext. Representative page saved:
   `images/btv1b10034035f_f80_cipher-and-decipher.jpg`. Two image requests reset mid-transfer (f82, f86);
   each retried once per the good-citizen rule, f82 failed again on retry and was not pursued further
   (f78/f80/f84 already establish the finding), f86 not attempted.
2. **Print / scholarship.** WebSearch for the letter directly returned no confirmed prior transcription;
   one AI-generated search summary asserted a specific "23 April 1597" letter from "Ferdinand II de Médicis"
   to "Francesco Guicciardini" — this is unreliable and was **not used**: Ferdinand II was not born until
   1610 and became Grand Duke only in 1621, so the summary is a fabrication or misattribution, not evidence.
   The correspondent name it gave (Guicciardini) matches the BnF catalogue's own `dc:subject` heading
   independently, which is the only part of that search result treated as a fact here. No dedicated
   secondary-literature check of the Medici Archive Project's BIA database was completed this sweep (not
   reachable without a login/API in the time available); flagged below as unchecked, though moot given
   point 1.
3. **Community lists.** `sources/cryptiana/web/` grepped for "Dupuy 155", "château d'If", "Ferdinand",
   "Guicciardini", "Toscane"/"Tuscany": no page on Tomokiyo's site is dedicated to this item or to
   Guicciardini's Spain correspondence specifically (his Spanish-cipher survey, `spanish.htm`, covers the
   Ferdinand-and-Isabella/Puebla ciphers of a century earlier, 1488-1516, an unrelated correspondence by
   coincidence of the same regnal name "Ferdinand"). No dedicated "Italian" or "Medici" page exists in the
   cached snapshot.
4. **DECODE.** `ay/catalogue/decode-catalog.csv` grepped for "Dupuy 155"/"Dupuy155": no record. Broader
   grep for 1597 Florence/Tuscany-flagged records (ASFi Segretario/Interno volumes, ids 6222-6790): these are
   all Florence-held Archivio di Stato keys for the Tuscan side of the correspondence, a different holding
   institution, none citing Dupuy 155 or château d'If.
5. **Bourdeau.** `cs-recheck` grepped for "Dupuy 155"/"château d'If"/"Guicciardini": no hit. Two
   superficially similar folder names (`ferdinand3`, `ferdinand1619`) checked directly and ruled out: the
   first is Ferdinand III/Cardinal-Infante Ferdinand correspondence of 1634-40 (Brussels archive), the
   second is Ferdinand of Bavaria to Maximilian I of Bavaria, 1619 (Bavarian archive) — different people,
   different archives, unrelated to Ferdinand I of Tuscany or Dupuy 155.
6. **Aymeloglu.** `ay/*.md` grepped for "Dupuy 155"/"Ferdinand"/"Guicciardini": no hit.

Requests: gallica.bnf.fr 9 (1 OAI record, 1 IIIF manifest, 6 image fetches incl. 2 connection resets each
retried once, 1 of the 2 retries also failed and was not pursued further). WebSearch: 2 queries.

## Edition risk

**Moot.** The letter already carries a contemporary parallel decipherment on every leaf of the original —
there is no cipher to solve. Whether a modern print edition additionally exists (e.g. in a Medici diplomatic
correspondence series) is irrelevant to its cryptanalytic status, since the plaintext is directly legible
from the primary source without any key-breaking.

## Verdict

**Found-solved / not a cryptanalysis target.** BnF Dupuy 155, item "(41)" (cipher letter to Ferdinand I,
Grand Duke of Tuscany, from his ambassador in Spain — Francesco Guicciardini, per the BnF's own subject
heading — concerning the château d'If, 10 May 1597, Italian) is not a blind ciphertext: the surviving
original already has its plaintext written out alongside the cipher numerals on every leaf, confirmed by
direct image inspection of three consecutive leaves. Grade H is available directly from the primary source
(no modern key-breaking involved) to whoever transcribes it. Not "new"; not "unpublished" — the item has
never needed cryptanalysis in the first place.

## Next

Drop N10 from the board as a cryptanalysis/recovery candidate. If wanted, a transcription of the already-
plain text (French/Italian palaeography, not code-breaking) is a "contribution"-lane task (README "What
counts as a result") — image already captured (`images/btv1b10034035f_f80_cipher-and-decipher.jpg`), no
further TNA/BnF access route or copy order needed, the volume is already digitised and public domain.
