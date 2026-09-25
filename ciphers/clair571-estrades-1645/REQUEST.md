status: waiting on the owner

# Request: clair571-estrades-1645 (QUEUE row M27, BnF Clairambault 571-582)

No personal data below; log the person's own archive request separately, by date and archive only, per
CLAUDE.md rule 9.

**What's needed:** colour digital reproductions (research use) of three leaves, in one batched request, all
from BnF, Département des Manuscrits, Collection Clairambault (archivesetmanuscrits ark `cc13896b`):

1. **Clairambault 575, p.1209** (volume V, "Ambassades du maréchal d'Estrades," juillet-décembre 1645) -- the
   target itself: "Lettre chiffrée adressée à l'un des plénipotentiaires à l'occasion du traité de Münster."
   Request the facing and following page as well (p.1208 and p.1210 or thereabouts), in case the letter runs
   onto a neighbouring leaf or carries an address/docket line on the back.
2. **Clairambault 574, f.3-4** ("Chiffre employé par Brasset," Jan-Jun 1645 and 1649; DECODE record 9431,
   correspondent Henri Brasset) -- the best-dated candidate key: same collection, adjacent volume, same
   half-year, same diplomatic circle (Brasset served alongside d'Estrades and the Münster plenipotentiaries).
3. **Clairambault 579, p.341** ("Double du chiffre de Mazarin avec M. d'Estrades," 1651-1654) -- a second,
   later copy of the reconstructed Mazarin-d'Estrades cipher (DE=-38, the same key Lasry and Tomokiyo already
   read from Clairambault 577 p.1, 1647; see `sources/cryptiana/web/louisxiv0.htm`). Worth a comparison copy
   even though it postdates the target by six to nine years, in case Mazarin's office reused this key earlier.

**Why each leaf:** the recovery test this request enables is the cheapest one available for this target --
apply the Clair 574 Brasset key (item 2) to the Clair 575 letter (item 1) directly. If that key does not open
it, the Clair 579 double (item 3) gives a second, independently-copied instance of the neighbouring
Mazarin-d'Estrades cipher to compare against, and either could turn up a mapping between the two ciphers if
they share design features. All three sit in the same undigitised volume run, so one request serves the whole
test.

**Why a request is needed:** confirmed 25 Sept 2026 (LANE YX worker YX-LOC571) that none of Clairambault
571-582 is digitised on Gallica -- every volume individually queried against Gallica's own SRU catalogue
(`gallica.bnf.fr/SRU?...&query=dc.source all "Clairambault NNN"`, a query proven against a control: the
identical query for "Clairambault 349" returns exactly one record, the volume already on file for a sibling
target) returned `numberOfRecords=0`. Full table of all twelve volumes, their date ranges and cipher-relevant
entries is in NOTES.md, "Access (LANE YX worker YX-LOC571, 25 Sept 2026)". The Département des Manuscrits'
finding aid itself (`archivesetmanuscrits.bnf.fr/ark:/12148/cc13896b`) offers only a reading-room reservation
of the originals; no substitute microfilm cote was found for these items this pass.

**Format requested:** colour digital scan (photograph), research use -- the cheapest reproduction tier BnF
offers; no print or certified copy needed.

**Where to send it:** BnF, Département des Manuscrits, Reproduction/permissions request. Public contact
routes, read from the BnF's own site on 25 Sept 2026 (`www.bnf.fr/fr/reproduire-un-document`, 2 curl requests,
browser User-Agent, >=1.6s apart): the page itself renders under a `path-reproduire-un-document` body class
but currently serves the site's 404 template (title "404 - Page non trouvée"), so no reproduction-specific
form URL or fee schedule could be read directly this pass -- confirm the current page before sending. Its
surrounding navigation still resolves to two live routes: **SINDBAD**, the library's own reference-question
form, `www.bnf.fr/fr/une-question-pensez-sindbad`, and the general contact page `www.bnf.fr/fr/contacter-la-bnf`.
This matches CLAUDE.md's own Access playbook row for BnF archivesetmanuscrits ("images not public domain --
permission via manuscrits@bnf.fr or the SINDBAD form"): use SINDBAD, or the manuscrits@bnf.fr address that row
already names, whichever the current site offers when you open it.

---

Subject: Demande de reproduction -- Collection Clairambault 574, 575, 579 (Manuscrits)

À l'attention du Département des Manuscrits,

Je souhaiterais obtenir une reproduction numérique couleur (usage recherche) des documents suivants,
conservés dans la Collection Clairambault :

1. Clairambault 575, p.1209 (et la page en regard ou suivante) ;
2. Clairambault 574, f.3-4 ;
3. Clairambault 579, p.341.

Ces documents ne semblent pas numérisés sur Gallica. Je vous remercie de bien vouloir m'indiquer la procédure
et le tarif applicables.

Bien cordialement,
[sign-off]

---

**Status:** waiting on the owner. Target stays at stage 2 (verified unsolved) -- see NOTES.md's check-solved
and Access sections. No copy order, payment or quote request goes forward until the owner sends this.
