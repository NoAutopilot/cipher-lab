open

# Nine (per QUEUE)/two-to-three (per finding aid) "en chiffres" letters, BnF Dupuy 452

QUEUE row: M6 (sources/solver-diffs/2026-09-23-digitised-hits.tsv, "Digitised candidates, no copy needed").

## Source

BnF, Departement des Manuscrits, **Dupuy 452**, Gallica `ark:/12148/btv1b10036146c` (295 leaves),
"Recueil de lettres et de documents, concernant les relations politiques de la FRANCE et de l'ITALIE
pendant la premiere moitie du XVIe siecle" (Gallica OAI title). BnF Archives et manuscrits notice
`http://archivesetmanuscrits.bnf.fr/ark:/12148/cc885911`. QUEUE M6's description: "Nine 'presque
entierement en chiffres' letters to Cardinal de Sens and others, incl. Alberto Pio da Carpi (Rome,
1520-1528)".

**Correction to the QUEUE description (found this sweep).** The finding aid's own item-list text
(Gallica OAI `dc:description`, the same text QUEUE quotes from) names only **two** letters explicitly
"presque entierement en chiffres": f.20 (Alberto Pio de Carpi to Madame [Louise de Savoie], Rome,
22 Oct 1525) and f.28 (Nicolas Raince, secretaire de l'ambassade de France a Rome, to the same, 25 Oct
1525), plus an unmarked "[par le meme?], s.d. (31)" whose cipher status is not stated. The Carpi letter
to the **Cardinal de Sens** (Antoine Duprat) at f.16, 18 May 1520, is NOT marked "en chiffres" in the
finding aid, and the leaf itself (viewed, see below) confirms it is plain. The volume also contains four
items catalogued as "**Dechiffrements**" (already-deciphered texts) of Rome dispatches, 16 April [1535]
(f.56) and 6 Nov. (f.60), and of Cardinal de Boulogne's dispatches (f.72, f.76, both undated) -- i.e. the
box already holds contemporary plaintext decipherments of *other*, later (1535) correspondence, a possible
"look for the sibling" lead for those items specifically, distinct from the 1525 Carpi/Raince cipher
letters. "Nine" does not match anything countable in the finding aid text; it may be a scout miscount of
every item involving Rome/Carpi correspondence generally, not every ciphered item. This is reported as a
correction, not an accusation -- the scout's QUEUE row correctly flagged the volume as worth checking.

## Check-solved sweep (23 September 2026)

1. **Web search.** `"Dupuy 452" Carpi chiffre OR cipher BnF` -- no hit connecting this shelfmark to any
   cipher scholarship or solver blog; only the BnF catalogue pages and Dorez's printed Dupuy-collection
   catalogue (Gallica) surfaced. `Alberto Pio da Carpi Louise de Savoie 1525 lettre chiffre Rome
   ambassade` -- the synthesis echoed this project's own catalogue-notice wording verbatim (i.e. it is
   circular, not an independent confirmation) and named no edition or decipherment. `"Alberto Pio da
   Carpi" "lettere americane" inediti cifra OR chiffre OR cipher` -- found a real Alberto Pio letter
   corpus, but a **different, unrelated one**: his 1512-1523 letters to Emperor Maximilian I and Matthaus
   Lang, now Univ. of Pennsylvania Ms. Coll. 637 ("lettere americane", published Carpi 2015 by Ori and
   Saetti) -- different correspondents, different archive, no cipher mentioned for that corpus either.
   Ruled out as the wrong Carpi letters. `Champollion-Figeac "Captivite de Francois Ier" Carpi ambassadeur
   Rome lettres` -- confirmed Champollion-Figeac's 1847 *Captivite du roi Francois Ier* does discuss the
   Rome embassy correspondence led by Carpi during the king's captivity (1525-26), the same window as the
   Louise-de-Savoie letters here; a real edition-risk candidate, checked further below.
2. **Print/scholarship.** Archive.org full-text search (be-api, no login) on Champollion-Figeac's
   *Captivite du roi Francois Ier* (identifier `bub_gb_DdUWAAAAQAAJ`, 1847, Paris, Imprimerie royale):
   query "Carpi" returned **0 hits**; query "chiffres" returned **0 hits**; query "Louise chiffre"
   returned 5 hits but all for unrelated "Louise de Savoie" mentions with no "chiffre" nearby (footnote
   numbers, not the word). This is a real, if partial, negative: this specific edition does not appear (by
   these terms) to print or discuss the Carpi/Raince cipher letters or their content. Not exhaustive (OCR
   errors on 1847 print, alternate spellings "Carpy"/"de Carpy" not tried).
3. **Community lists.** `sources/cryptiana/web/francis.htm` (Tomokiyo's page on Francis I's ciphers,
   covering BnF Clair.325/328/329/330/331/333/312/313, fr.2984/2980/3019/3045/3053/3081/20506, NAF 4206)
   grepped for "Carpi", "Dupuy 452": **no hit** -- this specific volume and these specific letters are not
   among the volumes Tomokiyo has already worked through, though the SAME general period/circle is (e.g.
   Nicolas Raince's OTHER ciphered letters in fr.2984, 1526, ARE published there with a reconstructed key
   -- see "Lead" below). `unsolved.htm` confirms the general 1520s French-cipher landscape (Calvimont-
   Duprat solved by Biermann 2021, Gramont/Tarbe and Bayonne solved by Lasry 2022, Galeaz Vesconte solved
   by Lasry 2023) but names none of these as touching Dupuy 452.
4. **DECODE.** Cached catalogue (`ay/catalogue/decode-catalog.csv`) grepped for "dupuy 452", "carpi",
   "duprat", "anhalt" (shared grep with M7): no hit for Dupuy 452 (the only "Carpi" hits are the unrelated
   1677 Carpio-Fuenmayor Brussels correspondence, a different person a century and a half later).
5. **Bourdeau.** `cs-recheck/CATALOGUE.md`, `SOLVED_CATALOGUE.md`, `TARGETS.md` grepped for "carpi",
   "duprat", "dupuy 452", "de sens": no hit.
6. **Aymeloglu.** `ay/CATALOGUE.md`, `TARGETS.md`, `SHORTLIST.md` grepped for the same terms: no hit.

**Lead, not applied (per brief).** Tomokiyo's `francis.htm` publishes a reconstructed key for Nicolas
Raince's *other* ciphered letters of 1526 in BnF fr.2984 (a different volume, same secretary, one year
later) sourced from Desenclos (2018), and separately publishes Calvimont-Duprat's, Gramont/Tarbe's,
Bayonne's and Galeaz Vesconte's 1520s keys. None of these is asserted to fit the Dupuy 452 Carpi/Raince
cipher (different hand/sender for the 1525 letters, and the visible symbol repertoire -- arithmetic
numeral groups with a few extra marks -- was not compared digit-for-digit against any of them this sweep).
If a solver session picks this up, checking Raince's fr.2984 key (1526, one year later, same person) against
the Dupuy 452 f.28 letter (Raince, 25 Oct 1525) is the most promising single check, since it is the same
scribe's own reused system, if he had one yet.

Requests: gallica.bnf.fr 15 (1 OAI GetRecord retried once on connection reset, 1 IIIF manifest, 13 IIIF
image fetches at reduced/high width), be-api.us.archive.org (fts) 3, WebSearch 5 queries.

## What the leaves show

Three leaves viewed (canvas 16, 19, 21, 23, 28, 31, 32, 33 sampled; three kept as images, see
`images/manifest.json`):
- **Canvas 16 (folio 16, "C. Carpi 1520"):** Alberto Pio de Carpi to the Cardinal de Sens, 18 May 1520 --
  plain French/Italian secretary hand throughout. No cipher.
- **Canvas 19:** a further plain letter signed "de Carpi" (not matched to a specific finding-aid folio this
  sweep; likely the f.17 Lautrec letter, undated in the finding aid). Plain.
- **Canvas 21 (folio 19):** Pope Adrian VI's Latin election letter, plain Latin.
- **Canvas 23 (folio 20, "C. Carpi 1526"):** **the genuine cipher letter.** Addressed "Madame..."
  (Louise de Savoie); roughly the first three-quarters is plain French; the final ~8-9 lines switch to a
  dense run of two-digit arithmetic-numeral groups (plus a handful of non-numeral marks), no spaces
  matching word boundaries obviously, no interlinear gloss and no facing decipherment on this leaf.
  Approximate token count for the cipher passage: **roughly 70-90 numeral/symbol groups** (rough count
  from 8-9 lines at ~9-10 groups/line; not an exact transcription, per the brief's "do not transcribe").
- **Canvas 32-33 (extrapolated position of folio 28, Raince's letter):** plain running French prose across
  both openings sampled; **the cipher passage of Raince's letter was not located this sweep** -- either
  the extrapolated canvas offset (based on the folio16-to-folio20 growth rate) undershot/overshot the
  actual leaf, or the cipher portion sits on a leaf not sampled. This is an open pinning gap, not a
  negative finding about Raince's letter.

Cipher type observed (f.20 letter only): **figures** (arithmetic numerals), not a symbol alphabet or
letter-substitution, consistent with an early-1520s French nomenclator/numeral cipher of the kind
Tomokiyo has reconstructed for several contemporaries. Decipherment: **none visible on the leaf itself**
(no interlinear gloss, no attached key on the same or facing folio, unlike Dupuy 468's Anhalt letter --
see ciphers/dupuy468-anhalt/NOTES.md for a contrasting case in a sibling volume).

## Edition risk

**Not realized on the evidence gathered.** Champollion-Figeac's *Captivite du roi Francois Ier* (1847),
the period-matching edition flagged as the highest-risk candidate, returns zero archive.org full-text
hits for "Carpi" or "chiffres" (see above) -- a real but not exhaustive negative (OCR/spelling variants
untested). No dedicated cipher scholarship, solver-repository entry or DECODE record names this shelfmark.
The "lettere americane" Alberto Pio corpus at UPenn is confirmed to be a different set of letters (1512-23,
to Maximilian I/Lang), ruled out as a false lead.

## Verdict

**Open, stage 2 verified unsolved (conditional: Champollion-Figeac checked only by archive.org full-text
search under two spellings, not read page-by-page; Guasti's Carpi edition, the *Negociations diplomatiques
entre la France et la Toscane*, and Letters and Papers Henry VIII/Brewer named in the brief were not
reached this sweep -- no route attempted beyond WebSearch, flagged as unchecked, not as negative).**
One genuine, digitised cipher passage confirmed by image (f.20/canvas23, Carpi to Louise de Savoie, ~70-90
numeral tokens, figures-type cipher, no key or decipherment on the leaf). A second named cipher item
(f.28, Raince) is real per the finding aid but its leaf was not located this sweep. No H or C reading
exists; nothing here is claimed as new, unpublished or unread (rule 10) -- this is a search result, not a
novelty verdict, and no verifier session has run.

## Next

1. **Pin folio 28 (Raince's cipher letter) precisely** -- canvases 30-35 were sampled without success;
   a denser bracket (every canvas 28-40) or the reading-room "aller a la page" folio-search box (not
   available to curl) would settle it.
2. **Transcribe the f.20/canvas23 cipher passage** (Carpi to Louise de Savoie, ~70-90 numeral groups) as
   the first solver step; check it token-for-token against Nicolas Raince's OWN published 1526 key
   (Tomokiyo's `francis.htm`, BnF fr.2984, one year later, same secretary/embassy) as the single most
   promising published-key lead, without applying it blind.
3. **Spot-check ff.56, 60, 72, 76** ("Dechiffrements" of 1535 Rome dispatches) by image -- these are
   *already-deciphered* period plaintexts sitting in the same box; if any corresponds to an otherwise-
   unread ciphertext elsewhere in the Dupuy/Clairambault Rome-embassy run, that would be a cheap recovery
   via the "look for the sibling" method (LESSONS.md), independent of the 1525 Carpi/Raince letters.
4. Reach Champollion-Figeac by page (not just full-text search), and Guasti/Negociations
   diplomatiques/Brewer's Letters and Papers Henry VIII, before treating this as cleanly open.
