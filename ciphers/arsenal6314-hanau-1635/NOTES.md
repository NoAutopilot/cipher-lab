blocked

Status set to blocked by LANE G2, 24 Sept 2026 09:42 UTC: not digitised; REQUEST.md and ASKS row.

Order placed 4 Oct 2026: BnF reproduction of Ms-6314 ff.177-183 (black-and-white PDF from microfilm, 14 pages) paid; waiting on delivery (order reference in the private record). Next: transcribe on arrival.

# Instruction to the comte Jacob de Hanau, 28 October 1635 -- Bibliothèque de l'Arsenal, Ms-6314

QUEUE row: M23 (sources/solver-diffs/2026-09-24-lane-g2-gallica4.tsv, "Fourth pass, 24 September 2026").

## Source

Bibliothèque de l'Arsenal, **Ms-6314** (184quater. H.F, "Recueil de pièces"), archivesetmanuscrits ark
`cc86280s`. QUEUE catalogue note: "Coppie (chiffrée et déchiffrée) de l'instruction donnée au sieur comte
Jacob de Hanau," 28 Oct 1635 -- cipher and its own contemporary decipherment both named in the same item, the
M1/M15/M21 cheap-transcription pattern. Thirty Years' War era; "comte Jacob de Hanau" not further identified
this pass (a French instruction *to* a count of Hanau, or possibly a French agent operating in/for Hanau --
not resolved).

## Check-solved sweep (24 September 2026)

1. **Web search.** Two queries (`"Arsenal" "6314" chiffre déchiffrée Hanau 1635`; `"comte Jacob de Hanau" 1635
   instruction chiffre`) returned only the archivesetmanuscrits catalogue record itself (ark cc86280s) and
   unrelated Hanau-Münzenberg genealogy pages (Philipp Moritz, Johann Ernst, Philipp Ludwig III, Balthasar --
   none named "Jacob," none tied to a 1635 French instruction). No solver or blog claim.
2. **Printed correspondence.** Not searched this pass. An "instruction" of this kind (French court to/
   concerning a foreign count, Thirty Years' War) is exactly the genre collected in Avenel's edition of
   Richelieu's *Lettres, instructions diplomatiques et papiers d'État* -- a natural next place to check, not
   yet done. Flagged as a gap, not a negative.
3. **Calendars/state-paper series.** Not reached (see item 2).
4. **Cryptiana / Cipherbrain.** No hit for "Hanau" tied to this item. The one "Hanau" occurrence in the local
   snapshot (`sources/cryptiana/web/german.htm` and `unsolved.htm`, an 1646 undeciphered letter of Carl von
   Rabenhaupt to Amalie Elisabeth, *regent of Hesse-Kassel, née Countess of Hanau-Münzenberg*) is a different
   item, different year (1646 vs 1635), different correspondent and different cipher -- confirmed as
   unrelated, flagged here so a future search does not conflate the two (same convention as the
   Clairambault1225 "two different Pagets" note). No Cipherbrain page found.
5. **DECODE.** Cached catalogue (`unsolved-ciphers/catalogue/decode-catalog.csv`, fresh clone, 1360 Decrypted +
   non-decrypted rows) grepped for "6314" and "Hanau": no hit.
6. **Solver repositories.** Fresh shallow clones of `dbourdeau/cyphersolver` and `aaymeloglu/unsolved-ciphers`
   grepped for "6314" and "Hanau": the only "Hanau" hit is `cyphersolver/CATALOGUE.md`'s entry for BL Add MS
   32305 (DECODE R2978-R2979, a Dresden/Hague correspondence unrelated to this item, and itself already
   removed from that repo's active catalogue on 21 Sept 2026). No hit for "6314".

Requests: WebSearch 2 queries. github.com 2 shallow clones (shared across this worker's six rows). No
gallica.bnf.fr or archivesetmanuscrits.bnf.fr fetches (per brief, LANE G2 has fetchers there already).

## Verdict

**Open.** Genuine gap: the Richelieu printed-instructions edition (Avenel) most likely to already contain this
"instruction" in print was not checked this pass, for budget reasons -- flagged, not scored as a source-family
negative.

`python3 tools/room.py ... "nomination: ciphers/arsenal6314-hanau-1635 | copy-free | recovery | own
decipherment present (cheap-transcription pattern); Avenel's Richelieu Lettres/instructions edition not yet
checked for this instruction; 'comte Jacob de Hanau' unidentified"`

## Capture and passes (24 Sept 2026)

**Blocked before capture: no Gallica digitisation of Ms-6314.** Read the archivesetmanuscrits finding aid
(`https://archivesetmanuscrits.bnf.fr/ark:/12148/cc86280s`, fetched 24 Sept 2026) in full (`tools/html2text.py`
on the saved HTML). The finding aid's own item list gives the item a precise location: **Fol. 177**, item 44 --
"Coppie (chiffrée et déchiffrée) de l'instruction donnée au sieur comte Jacob de Hanau," 28 octobre 1635 -- with
item 45 immediately after (**Fol. 182**, "Mémoire (chiffré et déchiffré) pour M. le cardinal de La Valette,
lieutenant général du Roy en son armée," undated in the finding aid) as a second, unexamined chiffré/déchiffré
item in the same volume. But the page carries no Gallica link: the CSS class the site uses to flag a digitised
item (`avecDaoGal`, "avec DAO Gallica") is defined in the page's stylesheet but not applied to any element on
this record; the only `href`s to another BnF system are two `reservationrao.bnf.fr` reservation links, one for
the original (Ms-6314) and one for a reading-room substitute (**MICROFILM ARS R-242218**, black-and-white,
"Cote de la matrice (pour commander une reproduction)" the same). Confirmed independently with three Gallica SRU
queries (`gallica all "Arsenal Ms-6314"`, `gallica all "Ms-6314"`, and a combined Arsenal+6314+Hanau query):
none returned a `dc:source` matching Bibliothèque de l'Arsenal Ms-6314 (the `Ms-6314` query's 1868 hits are all
different institutions' unrelated shelfmarks that happen to contain the string "6314", e.g. Bibliothèque
municipale de Grenoble R.6314). **No route from this worker's two permitted hosts (gallica.bnf.fr,
archivesetmanuscrits.bnf.fr) can reach an image of this item.** Wrote `REQUEST.md`: the leaf needs either a
reading-room visit or a paid reproduction order against MICROFILM ARS R-242218.

Steps 2 (line crops, blind Sonnet passes) and the decipherment-leaf pass could not be attempted -- there is no
image to cut or transcribe. Status stays **open**, unchanged; this is an access blocker, not a solving attempt,
so rule 3's matched-control requirement does not apply (no reading was attempted).

Requests this section: archivesetmanuscrits.bnf.fr 1 (the finding aid page, already covered by the check-solved
sweep's earlier fetch conventions but re-read in full here for the item list and reservation section).
gallica.bnf.fr 4 (3 SRU queries as above, one of which hit a `ws_closed_mid_exchange` tunnel reset and was
retried once successfully per the brief's retry rule; plus the two lookups below, on the same host).

### Lookups for other lanes (brief item 3)

**(a) for LANE R2** (DC1, `decode-4450-bnf-fr20506-1525` and the fr.2988 target): found via Gallica SRU
(`gallica all "Français 20506"` / `"Français 2988"`, matched by `dc:source`) and pinned with
`tools/gallica_folio.py`:
- **BnF fr.20506** (Recueil Gaignières VII, lettres/dépêches chiffrées à Anne de Montmorency) = ark
  `btv1b525047581`. Folio 136: canvas **f275** (label "136r", 4129x5969) recto,
  `https://gallica.bnf.fr/iiif/ark:/12148/btv1b525047581/f275/full/full/0/native.jpg`; canvas **f276** (label
  "136v", 4228x5968) verso. Manifest offset is a single constant run (k=4, canvases f5-f504 = folios 1r-250v),
  no inconsistency.
- **BnF fr.2988** (Recueil de lettres et pièces originales) = ark `btv1b525240150`. Folio 9: canvas **f25**
  (label "9r", 4298x5845) recto, `https://gallica.bnf.fr/iiif/ark:/12148/btv1b525240150/f25/full/full/0/native.jpg`;
  canvas **f26** (label "9v") verso. Note for whoever fetches neighbouring folios in this manuscript: the
  offset is **not constant across the whole volume** -- `tools/gallica_folio.py` reports two runs, k=8 for
  canvases f9-f70 (folios 1r-31v) and k=6 for canvases f73-f270 (folios 34r-132v), with a range label
  (f71 = "32-33") at the join; folio 9 sits inside the first (k=8) run so this pinning is solid, but a folio
  above ~32 needs the label read directly, not the k=8 formula.

**(b) clair1108-duvergier canvas 251 (fol.247v) native.** Fetched
`https://gallica.bnf.fr/iiif/ark:/12148/btv1b90009665/f251/full/full/0/native.jpg` (1 request, 5,128,800 bytes,
7453x5700px) -- this replaces the low-resolution `probe_f251.jpg` thumbnail already in that target's
`images/`. It does **not** fit under that folder's 30 MB cap (already 29 MB before this file), so per this
brief it was **not committed**; it is in this session's scratchpad
(`clair1108/folio247v_canvas251_native.jpg`) and the fetch is recorded, with a re-fetch command, in
`ciphers/clair1108-duvergier/images/manifest.json` (new entry after `probe_f251.jpg`). Not inspected at native
resolution by this worker (out of budget/scope) -- a future pass on that target should look at it before
cutting line crops of the 247v cipher text from the thumbnail.

**Progress paragraph.** Target's own capture (step 1-2) is fully blocked: Ms-6314 has no Gallica digitisation,
confirmed from the finding aid page itself and three SRU queries; `REQUEST.md` written for a reading-room
visit or a microfilm reproduction order (MICROFILM ARS R-242218) covering Fol. 177 (this item) and, while at
it, Fol. 182 (a second, unexamined chiffré/déchiffré item in the same volume). The brief's two lookup tasks
(fr.20506 f.136 and fr.2988 f.9 arks/canvases for LANE R2; clair1108-duvergier canvas 251 native) are both
done and reported above/in ROOM. Well under the $6 cap (no subagents spawned, ~10 host requests total). Not
classifying novelty (none read).

## Web and blog check (GF-A2-13, 3 Oct 2026)

Worker GF-A2-13 (account 2, LANE-A2PUSH), 01:29-01:3x UTC. Gate-fix only (gate already exit 0: status `blocked`,
terminal). No image, no transcription.
(a) Plain web searches (WebSearch, standard):
1. `"comte de Hanau" instruction 1635 Richelieu Avenel` -- Avenel catalogue records (swisscollections, Heidelberg,
   NLI), a defense.gouv.fr digital-library page, OUP "Richelieu and his Age". No text of the instruction.
2. `"Arsenal" "Ms-6314" OR "ms 6314" chiffre déchiffrée Hanau` -- firearms and auction noise only.
3. `Jakob Johann Hanau-Münzenberg 1635 Frankreich Instruktion Chiffre Richelieu` -- Wikipedia (Philipp Moritz,
   Johann Ernst, Johanna of Hanau-Münzenberg); Jakob Johann left as regent of Hanau after 1634. No instruction.
4. `"instruction donnée au sieur comte Jacob de Hanau"` (the finding aid's own wording, quoted) -- CCFr records
   for other Hanau items (a 1504 note, a 1707 lettres patentes for Hanau-Lichtenberg), Deutsche Biographie (Jakob
   von Ramsay). No hit on this item.
(b) Site searches: `site:scienceblogs.de/klausis-krypto-kolumne Hanau 1635` -- no Cipherbrain page;
`site:cryptiana.blogspot.com Hanau OR Arsenal 6314 OR "La Valette" chiffre` -- no Cryptiana page;
`site:ciphermysteries.com Hanau 1635 OR Arsenal Richelieu cipher` -- no Cipher Mysteries page, but two Cipherbrain
posts surfaced: "Who can decipher this letter from Louis XIII?" (English version opened: Louis XIII, 6 April 1635,
recipient unknown, two pages; no mention of Hanau, Arsenal 6314, an instruction or La Valette; comments only on the
German version, 21 Nov 2022 -- not this item, by date and author, so its thread was not read) and the Rabenhaupt to
Amalie Elisabeth (née Hanau-Münzenberg) letter, already excluded on 24 Sept as a different item.
Result: no decipherment, plaintext or discussion of Arsenal Ms-6314 fol.177 on the open web or the three blogs.
Requests: WebSearch 7; WebFetch 1 (scienceblogs.de).

## Premise check (GF-A2-13, 3 Oct 2026)

(a) Decipherments the folder already mentions: **found (catalogued, not viewed).** The finding aid (ark cc86280s,
read 24 Sept) names item 44, Fol. 177, as "Coppie (chiffrée et déchiffrée)": the period decipherment is in the same
item, beside the cipher. Item 45, Fol. 182 (La Valette mémoire), is also "chiffré et déchiffré". Neither leaf is
digitised (MICROFILM ARS R-242218 only; ASKS rows 35 and 78), so the decipherment could not be opened. If the
leaves arrive, the item is a calibration/recovery read (cipher against its own clerk decipherment), not an
unread cipher.
(b) Other solvers' working files: **not found.** Fresh shallow clones (3 Oct 2026): dbourdeau/cyphersolver hits for
`hanau` are a word list in targets/malsburg1637/extra.txt (Hesse 1637 place names), targets/swieten1757 (Hanau in
French hands, 1757-58) and the README's Swieten row; none touches Ms-6314. `6314` hits are numerals in JSON/TSV
files. aaymeloglu/unsolved-ciphers: no `hanau`/`6314` working file. Cited, not copied.
(c) Physical neighbours: **unreachable.** No images of Ms-6314 at all; the catalogue neighbour after it is item 45
(Fol. 182, chiffré et déchiffré); the item before it was not re-read this pass.
(d) Recipient / sender-side edition: **found, mention only, not printed.** Avenel, *Lettres, instructions
diplomatiques et papiers d'État du cardinal de Richelieu*, t. V (1863; archive.org `bub_gb_YcCURbuwqiwC`,
`_djvu.txt` grepped for `hanau`, 5 hits, all read): no. CXCVI, Richelieu to the maréchal de Brézé, 30 Jan 1636
(pp. 410-411): "J'ay veu l'instruction donnée au comte Jacob de Hanau, que vous m'avez envoyée; je ne l'avois pas
veue auparavant. ... les CL mil [livres] qui estoient destinées par l'instruction du comte Jacob de Hanau pour les
trouppes du Langrave de Hesse". A memorandum of July 1635 in the same volume records "120,000 [livres] au comte de
Hanau" for 1,500 horse and 4,000 lansquenets of the landgrave of Hesse, and "le fonds de Coblentz par le comte de
Hanau". So the instruction concerned French subsidies for Hesse-Kassel's troops; Avenel describes it but does not
print it, and no other hit in t. V is the instruction. The 1636 letter shows a copy travelled to Brézé, so a clear
copy may also sit in the Affaires étrangères Correspondance politique (France 1635-36, or Allemagne/Hesse) --
not checked (not online). Not a decipherment of the item.
Result: no plaintext of the instruction found in print or online; status line unchanged (`blocked`, waiting on the
microfilm order).
Requests: archive.org 1 advancedsearch + 2 `_djvu.txt` (one 500, not retried); github.com shared clones.

## fr17 re-judge (FR17-RJ2, 3 Oct 2026)

No reading on disk -- no ciphertext or reading: status blocked (not digitised, REQUEST.md). No judge run (fr16 or fr17), no shuffled-decode control, no per-fold rate at a reading's N; the fr17 per-fold rates at N=138/300 are in tools/data/fr17/README.md.
