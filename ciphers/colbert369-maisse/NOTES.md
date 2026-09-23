found-solved

# Register of instructions and despatches to Andre Hurault de Maisse, ambassador at Venice — BnF Cinq cents de Colbert 369

QUEUE row: M1 (sources/solver-diffs/2026-09-23-digitised-hits.tsv, "Digitised candidates, no copy needed").

## Source

BnF, Departement des Manuscrits, **Cinq cents de Colbert 369**, Gallica `ark:/12148/btv1b100339414`
(394 leaves), BnF Archives et manuscrits notice `http://archivesetmanuscrits.bnf.fr/ark:/12148/cc917396`.
Full title (BnF Archives et manuscrits, `Presentation du contenu`, quoted verbatim, fetched 23 September
2026):

> « Registre des instructions, pouvoirs et depesches baillees a Monsieur [Andre Hurault] de Maisse par le
> deffunt roy Henry troisiesme, le renvoyant pour la seconde fois ambassadeur ordinaire vers la Seigneurye
> de Venize, lequel se partit de la Cour, qui estoit a Tours, au mois d'avril 1589 » (13 mars 1589-11 avril
> 1594). ... En tete du volume, se trouve le chiffre de la correspondance entre l'ambassadeur et la Cour. —
> Lettres de Henri III, Andre Hurault de Maisse, Horatio Russelay ou Rucellai, Henri IV, Francois de
> Luxembourg, envoye pres du pape Sixte-Quint... — En outre, on trouve dans le registre : « Interpretatio
> litterarum potentissimi et invittissimi monarche Sultan Murad Hami ad serenissimum Henricum caesarem
> regni Galliae et regem Navarrae » (f.126, 261 v°). — « Credenza di Maestro fra Alessandro Franceschi...
> in Fiorenza, alli 14 d'ottobre 1592 » (f.272).

André Hurault de Maisse was ambassador in Venice 1582-1596 (with a gap 1588-89); this register covers his
second embassy, opened by Henri III just before his assassination and continued under Henri IV.

## Check-solved sweep (23 September 2026)

1. **Web search.** WebSearch `"Cinq cents de Colbert 369" Maisse chiffre` — no dedicated blog, blog comment
   thread or scholarship post found naming this shelfmark; general BnF catalogue-collection pages only
   (Comite d'histoire BnF, Biblissima, the 1907 La Ronciere printed catalogue on IA/Gallica). No hit
   connecting this specific volume to a cryptanalysis attempt.
2. **Print / scholarship — the decisive finding.** Fetched the BnF Archives et manuscrits notice
   (`archivesetmanuscrits.bnf.fr/ark:/12148/cc917396`, plain curl with a browser User-Agent, HTTP 200 — this
   route works for this notice type, contrary to the general "JS-rendered" caution in the Access playbook)
   and the Gallica IIIF manifest and images (below). **The cipher table at the head of the volume (ff.3-5,
   at least three distinct keys headed "Chiffre du Roy, escript au Sr de Maisse", "Chiffre envoye a Mons.r
   de Maisse" and a further "Brefves, a de Maisse" table) matches, digit for digit, the key already
   published by Satoshi Tomokiyo as an image ("Maisse's Cipher (1592)", `henryiv_Maisse1.png`) and already
   applied by Bourdeau's `cyphersolver` to BnF fr. 16093 ff.370/373 (catalogue id 17, solved and removed
   from Bourdeau's open catalogue 19-20 September 2026; `cs-recheck/maisse1592/NOTES.md`,
   `cs-recheck/SOLVED_CATALOGUE.md` row 40).** Bourdeau's key1.tsv: `a 7 b 8 c 9 d 10 e 11 f 1 g 2 h 3 i 4
   l 5 m 6 n 12 o 13 p 14 q 15 r 16 s 17 t 18 u 19 x 20 y 21 z 22`, doubles `ff 66 mm 67 nn 68 ss 72 uu 73`.
   The f3 image here reads identically: `a-7 b-8 c-9 d-10 e-11 f-1 g-2 h-3 i-4 l-5 m-6 n-12 o-13 p-14 q-15
   r-16 s-17 t-18 u-19 x-20 y-21 z-22`, doubles `ff-66 mm-67 nn-68 ... ss-72 ...-73`. Tomokiyo's own page
   (`henryiii.htm`, mirrored locally; `henryiv.htm`, cached in `cs-recheck/gallica_sweep/src/henryiv.txt`)
   says he reconstructed this key from de Maisse's own 1590s letters and cites Savasse (1997), who
   reconstructed it independently from the "Manuscrit Revol"; neither text names Colbert 369 as the source
   — this appears to be the same key surviving as a period document, not previously tied by name to this
   shelfmark in the sources checked. Nothing here is claimed as a discovery (rule 10); it is reported as
   what was and was not found.
3. **Community lists.** `sources/cryptiana/web/henryiii.htm` and `henryiv.txt` (cached) discuss Maisse's
   ciphers at length (fr.16092, fr.16093, NAF 22070) but never cite Colbert 369. `sources/cryptiana/`
   grepped for "colbert 369"/"colbert369": no hit anywhere in the mirror.
4. **DECODE.** Cached catalogue (`ay/catalogue/decode-catalog.csv`) grepped for "colbert 369", "maisse":
   no hit.
5. **Bourdeau.** `cs-recheck/CATALOGUE.md`, `SOLVED_CATALOGUE.md`, `TARGETS.md` grepped for "maisse":
   the fr.16093 target (`maisse1592/`, catalogue id 17) is the only hit, already solved and removed
   19-20 Sept 2026 (see point 2). No mention of Colbert 369 by shelfmark anywhere in the repo.
6. **Aymeloglu.** `ay/CATALOGUE.md`, `TARGETS.md`, `SHORTLIST.md` grepped for "maisse"/"colbert 369":
   no hit.

Requests: gallica.bnf.fr 22 (1 manifest already cached by the digitised scout, 1 new manifest metadata
read, 19 new IIIF image fetches at reduced width incl. 2 connection resets each retried once per the
good-citizen rule), archivesetmanuscrits.bnf.fr 1 (HTTP 200, plain curl). WebSearch 3 queries (shared
across M1-M3, see clairambault351-paliano/NOTES.md and dupuy111-sarpi/NOTES.md). archive.org 2 (both failed,
"Temporarily Offline" outage confirmed by other workers tonight; not pursued further, unrelated to M1's
verdict).

## What the leaves show

Viewed at reduced width (~900px): f1 (blank flyleaf), f2 (blank flyleaf, Bibliotheca Regia stamp, matches
the scout's earlier view), **f3, f4, f5 — three or more full-page cipher key tables** in the same period
hand, headed "Chiffre du Roy, escript au Sr de Maisse" (a substitution alphabet on 22 letters plus
homophone "doubles" and a nomenclator of place/office names, dated internally "Allarme d'Italie, au mois de
Mars 1591"), "Chiffre envoye a Mons.r de Maisse" (a second, symbol-based key) and a further page naming
"Brefves, a de Maisse" (matching Savary de Breves, Maisse's fellow ambassador who shared a cipher with him
per Tomokiyo). **f6v/f7r — the illuminated title leaf** ("Registre des Instructions Pouvoirs et Despesches
Baillees a Monsieur de Maisse...") and the start of the register text. **f8-f20, f130, f270 (18 leaves
sampled across the volume, including one dated entry "Du Roy, du premier Novembre 1592" at f270, one day
before the fr.16093 letter Bourdeau already decoded) — all plain French (and occasional Latin) secretary
hand, prose instructions and letter copies, with no cipher symbols, numeral groups or interlinear
decipherment anywhere in the sample.** The register reads as a clerk's clear-text minute-book of the
instructions and despatches sent to and received from Maisse — functionally the same kind of source as
Brienne 13 (NAF 6984), which Bourdeau used as the independent clear-text control for the fr.16093 letters.
The two items named separately in the catalogue ("Interpretatio litterarum" f.126/261v; "Credenza" f.272)
were not viewed this sweep — the catalogue's own wording ("Interpretatio", "Credenza... data in scritto")
suggests further clear translations/administrative copies, consistent with the sampled pattern, but this is
inferred, not confirmed by image.

Sample coverage: 18 of 394 leaves (4.6%), concentrated at the front matter plus two spot checks in the
body. This is not exhaustive; a leaf-by-leaf pass could in principle find an isolated enciphered entry the
sample missed, but nothing in 18 leaves across the volume's date range suggests one.

## Edition risk

**Realized, by key identity rather than by a printed text of this register.** The register's own text
(sampled) is not itself in cipher, so there is no unread ciphertext in it to check against a printed
edition. But its front-matter cipher table (ff.3-5) is, digit for digit, the same key Tomokiyo published
and Bourdeau already applied to decode four Henri IV-to-Maisse letters in the companion volume BnF
fr. 16093 (ff.370, 373, 406, 410; catalogue id 17, credited to Bourdeau, key traced by him to Tomokiyo's
2020s reconstruction and to Savasse 1997). This register is very likely the period source (or a period
duplicate) of that same key, for the same correspondence stream, in the same 1589-1594 window as the
already-solved letters (3 Nov 1592-27 Apr 1593 falls inside this register's 13 Mar 1589-11 Apr 1594 span).

## Verdict

**Found-solved / not a valid recovery target as scored.** Two independent facts, both against rule 10
wording (no claim of new, unpublished, first): (a) the register's own text, sampled across 18 leaves
spanning its full date range, is plain French/Latin prose, not ciphertext — there is nothing here to
decode; (b) its cipher table matches the key already published (Tomokiyo, image) and already applied
(Bourdeau, 19-20 Sept 2026, catalogue id 17) to the related fr. 16093 correspondence. The register's value,
if any, is as a possible additional clear-text control alongside Brienne 13 for that already-solved target,
or as a bibliographic note on the key's period source — not as a fresh cryptanalysis or recovery target.

## Next

Drop M1 from the board; it does not need a copy order or further imaging under this project's "What counts
as a result" (README) — it does not produce an unread text. If anyone wants the narrower follow-up: (1) a
Bourdeau/Aymeloglu-style note that Colbert 369 ff.3-5 is a/the period source of "Maisse's Cipher (1592)"
would be a bibliographic contribution, not a decipherment, and belongs with that repository, not here;
(2) the two unviewed named items (Sultan Murad "Interpretatio", f.126/261v; the Florentine "Credenza",
f.272) were not checked by image this sweep and could be spot-checked (canvas indices roughly f126-130 and
f272-276 on the manifest) if anyone wants to close that small residual gap, but nothing in the catalogue's
own wording for either suggests ciphertext.
