# BnF fr.16092 — Dépêches de la Cour à André Hurault de Maisse, ambassadeur à Venise, août 1582-décembre 1585

Status: open

Check-solved pass, 24 September 2026 (Sonnet, orchestrator brief for M13-M16). Not a full six-source check-solved
run; this is the editions-first + one-leaf pass the brief asked for. A formal check-solved (blind, six sources)
is still owed before this goes on the board at stage 2.

## What the target is

Gallica ark `btv1b90612993`, 932 canvases (all labelled `NP`, no 1:1 folio map). Full title/description via
`services/OAIRecord`:

> Dépêches originales de la Cour à André Hurault de Maisse, ambassadeur à Venise (1581-1588 et 1592-1596)... I
> Août 1582-décembre 1585. Très nombreuses lettres orig. de Henri III, 1582-1585 (f.12, etc.) — et de Nicolas de
> Neufville [Villeroy], 1582-1585 (f.7, etc.) ; Nombreuses lettres orig. de Catherine de Médicis, 1582-1585
> (f.15, etc.) ; ... Instructions orig. données à Mr de Maisse, août 1582 (f.1), et février 1583 (f.54) : Chiffre
> de la correspondance de Mr de Maisse (f.5).

This is the *first* of a two-volume run (fr.16092 = 1582-85, fr.16093 = 1586-96); the two are catalogued and
digitised separately.

## Checked (24 Sept 2026)

- Tomokiyo, "French ciphers during the Reigns of Charles IX and Henry III" (`henryiii.htm`), mirrored without a
  fresh fetch in `sources/cryptiana/web/` is absent, so read via a fresh shallow clone of
  `dbourdeau/cyphersolver` (`gallica_sweep/src/henryiii.txt` carries a full-text mirror of the same page).
  Verbatim: *"BnF fr.16092 (Gallica) contains 'La Clef du chiffre de Mr de Maisse Ambassadeur a Venise' (f.5).
  It is a numerical cipher as follows, but I have not seen its actual use. The many letters in BnF fr.16092 from
  Henry III (countersigned Neufville (i.e., Villeroy)) to de Maisse in 1582-1585 employs the following cipher,
  which is typical of the French ciphers at the time. The same cipher is also used in many letters in 1586 to
  May 1587 in BnF fr.16093 (ff.1-159)."* Per rule 10, this is quoted rather than paraphrased: Tomokiyo has
  reconstructed the key from the image but states plainly he has not confirmed it against an actual ciphertext
  passage in this volume.
- Fresh shallow clone of `dbourdeau/cyphersolver` (24 Sept 2026): the only Maisse work is `maisse1592/`, which
  covers fr.16093 (**not** fr.16092), a different, later cipher (1592-93), broken by aligning the ciphertext
  against clean 17th-c. clerk copies in Fonds Brienne (NAF 6984 = "Brienne Ms. 13") via the Berger de Xivrey
  pièce-number index — a different method (contemporary sibling clear copy) from what would be needed here (a
  cipher key never yet matched to a ciphertext passage). No hit on "16092" anywhere in the repo.
- Fresh shallow clone of `aaymeloglu/unsolved-ciphers` (24 Sept 2026): no hit on "16092", "Maisse" outside
  unrelated filenames.
- WebSearch: `"fr. 16092" OR "fr.16092" Maisse Venise Henri III chiffre clef` surfaced a GitHub PR
  (`dbourdeau/cyphersolver#7`, "Henri IV to Maisse, Venice 1592-93...") — confirms the above, still fr.16093.
  Also surfaced the archivesetmanuscrits.bnf.fr catalogue confirming fr.16092 covers Aug 1582-Dec 1585.
- Editions: *Lettres de Henri III, roi de France*, ed. Champion/François/Boucher, tome V (8 Apr 1580-31 Dec
  1582) and tome VI (4 Jan 1583-20 Mar 1585) cover exactly this volume's date range and are both published
  (2000, 2006). **Not resolved this pass**: whether Boucher's edition already prints any of these specific
  letters in clear (e.g. from a lost contemporary decipherment, the way Bourdeau found for fr.16093/Brienne).
  This is the single biggest open risk before committing a transcription budget — check her apparatus for
  "chiffré"/"déchiffré" source notes on fr.16092 items before transcribing.
- Gallica IIIF, one leaf and three extra probes (932-canvas volume, no reliable folio map; costs logged under
  Requests below): canvas 12 = the key itself, "La clef du chiffre de Mr. de Maisse Ambassadeur a Venise" (a
  numeral nomenclator: numbers 12-65 for names/places/words, a letter alphabet a-y as figures 40-61, nulls) —
  image saved `images/f12.jpg`. Canvas 20 = a plain-French clear extract of a royal letter, 1 Feb 1583
  (`images/f20.jpg`). Canvas 30 = folio 14, Villeroy to Maisse, clear French, no cipher (`images/f30.jpg`).
  Canvas 70 = folio 21, Villeroy to Maisse, 21 Jan 1583, clear French, no cipher (`images/f70.jpg`). **No actual
  ciphertext passage was located in this four-leaf sample** — consistent with, not contradicting, Tomokiyo's own
  "I have not seen its actual use." Folio-to-canvas offset is uncalibrated (canvas 12 sits near the key's stated
  f.5-f.9 but canvas 70 = folio 21, i.e. offset ≈ +49, similar to the +48/+49 offset Bourdeau found for the
  neighbouring fr.16093), so this is not a systematic sweep.

## Verdict

Open at stage 2 is **not yet safe to set** — the modern edition check is incomplete (see above), and this pass
did not confirm ciphertext actually appears in the volume, only that a key and several clear letters do. Grade:
no reading attempted, nothing to grade.

Cheapest next step, in order: (1) check whether Boucher tomes V/VI print any fr.16092 letter from a lost
decipherment (a few hours against her critical apparatus, no image fetches needed); (2) if that comes back
negative, page further into the volume (real folios roughly 25-105, i.e. canvas range roughly 74-154 at the
offset above) looking for actual numeral groups matching the f.5-f.9 key range, before transcribing anything.
This is exactly the fr.16093/Brienne pattern (Bourdeau, `maisse1592/NOTES.md`) one volume earlier — worth
checking whether an earlier Brienne volume (COLLECTION DE BRIENNE 11-12, before NAF 6984 = vol.13) covers
1582-85 and could do the same alignment trick here.

## Sources

- Gallica: `https://gallica.bnf.fr/ark:/12148/btv1b90612993`, OAI record via
  `https://gallica.bnf.fr/services/OAIRecord?ark=btv1b90612993`.
- S. Tomokiyo, "French ciphers during the Reigns of Charles IX and Henry III", cryptiana.web.fc2.com/code/henryiii.htm,
  read via `dbourdeau/cyphersolver`'s mirror (`gallica_sweep/src/henryiii.txt`), not our own `sources/cryptiana/`
  mirror (that copy does not include this page).
- github.com/dbourdeau/cyphersolver, `maisse1592/NOTES.md` (fr.16093, cite only, code MIT / text CC BY 4.0).
- github.com/aaymeloglu/unsolved-ciphers (checked, no relevant content; no licence, cite only, nothing copied).
- Champion/François/Boucher, *Lettres de Henri III, roi de France*, tomes V-VI (2000, 2006) — bibliographic
  identification only, text not consulted this pass.

## Requests this pass

gallica.bnf.fr: 1 OAI record + 4 IIIF image fetches (one connection reset on a later attempt for a different
target, not this one). github.com: 2 shallow clones (dbourdeau/cyphersolver, aaymeloglu/unsolved-ciphers, both
deleted after grep). WebSearch: 2 queries.

## Locate-ciphertext + print check pass, 24 September 2026 (Sonnet, orchestrator brief, cap $10)

Two-part job: (A) find any ciphered leaf in the volume by working from the BnF item-level catalogue notice
plus wider Gallica probing; (B) print check the same edition gap the check-solved pass flagged (Boucher's
apparatus for tomes V-VI unread). Neither decoding nor novelty wording attempted, per brief.

### (A) BnF catalogue notice, read in full for the first time this pass

The 24 Sept check-solved pass had not yet pulled the fr.16092-specific (as opposed to fr.16092-16093 combined)
archivesetmanuscrits.bnf.fr notice. Found it via the AJAX component endpoint the site's own JS uses
(`https://archivesetmanuscrits.bnf.fr/ajaxGetCompDisplay.html?eadCompId=FRBNFEAD000046224_d0e62`; a WebSearch
hit for the combined fr.16092-16093 notice initially led to the wrong sibling node, `..._d0e136`, which is
fr.16093 -- caught by checking the returned cote before using it). Full "Présentation du contenu" for
fr.16092, quoted because it is short and the wording matters for rule 10:

> Très nombreuses lettres orig. de Henri III, 1582-1585 (f. 12, etc.), — et de Nicolas de Neufville [Villeroy],
> 1582-1585 (f. 7, etc.) ; — Nombreuses lettres orig. de Catherine de Médicis, 1582-1585 (f. 15, etc.) ; —
> Quelques lettres orig. de Mr de Sève, 1583 (f. 106, 136, etc.), et 1585 (f. 113, etc.), — et de Pierre
> Brulart, 1583-1585 (f. 132, etc.) ; — Lettre orig. de Claude Pinart, 1583 (f. 141) ; — Copies de lettres de
> Henri III à la République de Venise, 1584 (f. 179, etc.), — et de divers personnages, notamment : Louis de
> Gonzague, duc de Nevers, 1582 (f. 133), — Guillaume, duc de Mantoue, 1583 (f. 135), — et Hugues de Loubenx,
> grand-maitre de Malte, 1584 (f. 183) ; — Pièces diverses, concernant l'ambassade de Mr de Maisse (f. 6, 49,
> etc.) ; — Instructions orig. données à Mr de Maisse, août 1582 (f. 1), — et février 1583 (f. 54): — Chiffre
> de la correspondance de Mr de Maisse (f.5).

**No individual despatch in this notice is flagged "chiffre" or "chiffré"** -- the word "Chiffre" appears
exactly once, for the key itself at f.5 (already imaged, canvas 12, previous pass). This is a real fact about
the catalogue, not proof the volume holds no ciphertext (archivists don't reliably flag cipher use item by
item), but it means there is no catalogue-given shortcut to a specific ciphered folio; any leaf has to be
found by looking. The notice also gives the volume's true extent: **459 feuillets**, reservation cote
Français 16092, substitute document MF 33938 (microfilm), matrix R 16098 -- useful if a copy order is ever
needed instead of Gallica.

Also surfaced by the same WebSearch: **BnF Français 17834**, "Registre des lettres et dépêches adressées par
André Hurault de Maisse à la Cour... pendant son ambassade à Venise", volume III (Jan 1587-Aug 1588) -- i.e.
Maisse's own outgoing register, the mirror-image collection to fr.16092/93 (Court-to-Maisse). Its numbering
implies volumes I-II exist covering Nov 1582 onward, which would overlap fr.16092's date range from the other
side of the correspondence. Not fetched or catalogue-checked this pass (out of scope/budget) -- flagged as a
lead: if the Court used cipher toward Maisse, his own register might carry the corresponding clear drafts, or
a note of what he received in cipher.

### Gallica probing, offset problem

The brief's calibration instruction (two known points: canvas 30 = folio 14, canvas 70 = folio 21) does not
actually resolve to a single constant: 30-14=16 against 70-21=49, a 33-canvas discrepancy in the *offset* over
only a 7-folio span, not a rounding error. Read literally as "canvas per folio" it is worse (932 canvases /
459 folios ≈ 2.03, i.e. the volume is close to 2 canvases per folio overall -- consistent with recto+verso --
but 30→70 is 40 canvases for only 7 folio numbers, ≈5.7/folio locally). Likely explanation: unfoliated
enclosures, covers, or blank leaves clustered in that stretch, not a bad reading of either folio number. This
pass did not resolve it definitively; a spot check on canvas 106 (see below) read as folio "62" with low
confidence (small, faded pencil numeral, French secretary hand), which would put offset at 44 there -- a
third, different value again. **Treat any folio number quoted from an offset formula in this file as
approximate (grade I), not read (grade H), until someone reads the actual numeral on the leaf.**

Given the brief's own "cheapest next step" pointed at the offset≈49 hypothesis (matching Bourdeau's +48/+49
for the sibling fr.16093), this pass probed that range as instructed rather than re-deriving a new formula:
**canvases 74-154 at 4-canvas intervals (21 leaves: 74, 78, 82, ..., 154), IIIF thumbnails (500px wide) to
keep bandwidth and image-review cost down**, one request ≥1.5s apart (two transient connection resets, both
recovered on the single allowed retry, no 403/altcha). Reviewed as a single labeled contact sheet
(`images/probe_contact_sheet.jpg`) rather than 21 separate views. **Every one of the 21 is either a clear
cursive French letter/docket (several with visible dates, signatures, wax-seal remnants, "Secretaire d'Estat
a Mr de Maisse" endorsements) or a blank verso/cover leaf. None shows the dense numeral groups the f.12 key
would produce if used** -- consistent with, not proving beyond, Tomokiyo's "I have not seen its actual use."
Individual thumbnails kept as `images/probe_c74.jpg` … `probe_c154.jpg`.

Combined with the earlier pass's 4-canvas sample (12, 20, 30, 70), **25 leaves spread across roughly the first
sixth of the volume's canvases have now been looked at; none carries ciphertext.** This is a sample, not a
census -- 907 canvases remain unchecked -- so this stays a negative-with-a-sample, not a closed search.

### (B) Print check: Boucher's apparatus, and other editions

- **Boucher, *Lettres de Henri III, roi de France*, tome V (8 Apr 1580-31 Dec 1582) and tome VI (4 Jan
  1583-20 Mar 1585)**, Société de l'Histoire de France, 2000/2006: confirmed by WebSearch (Persée reviews,
  Cairn.info notice for tome VI) as covering exactly fr.16092's date range, ~1,057 letters in tome VI alone.
  **Not on Internet Archive** (`archive.org/advancedsearch.php?q=title:(Lettres de Henri III)` returns only
  19th-century items -- Baschet's *Les comédiens italiens*, an 1855/1863 Maisse-in-England pamphlet, 19th-c.
  manuscript catalogues -- nothing from Boucher's 2000s critical edition, as expected for an in-copyright
  scholarly monograph). **Not found on HathiTrust** by a guessed OCLC number (empty record; not pursued
  further -- a real record lookup would need a correct OCLC/record number, not attempted this pass). Google
  Books: `"Maisse" "chiffre" Boucher Henri III` = 0 hits; `"Hurault de Maisse" chiffre` = 300 hits but the
  first page is all 19th-century catalogues, Baschet, and the 1595-98 England embassy -- none is Boucher's
  edition or a discussion of fr.16092's cipher specifically. **Her apparatus itself remains unread** -- this
  pass could only test whether it is discoverable full-text online (it is not) and whether anyone citing it
  online mentions cipher for this correspondence (no one does, in what these searches surfaced). The check
  Champion/Boucher's own footnotes flag a lost decipherment (the way a modern edition sometimes does) still
  requires the physical/scanned book, not a web or IA/HathiTrust/Google Books search.
- *Négociations diplomatiques de la France avec la Toscane* and comparable Venice-embassy edited-correspondence
  series: WebSearch for a Venice-specific equivalent surfaced only the BnF catalogue pages and fr.17834 (see
  above), no dedicated printed edition of the Maisse-Venice correspondence distinct from Boucher's Henri III
  letters. No Venice-specific series was located to check; if one exists under a different title it was not
  found by this pass's queries.
- Tomokiyo (cited in full in the check-solved pass above, not re-fetched) and Bourdeau's fr.16093 work (cited,
  not re-cloned this pass) still stand as before: key reconstructed, no confirmed use seen by Tomokiyo, no
  fr.16092 work in Bourdeau's repository.

### Verdict

**Status stays `open`.** No ciphered leaf located (25-canvas sample, sixth of the volume, all clear); no
print edition confirms or rules out a lost decipherment (Boucher's apparatus, the one edition that could
settle this quickly, is not searchable online and remains unread). Grade: nothing read, nothing to grade. Per
rule 10, nothing here may be called new, unpublished, first, or never printed -- the honest state is "not yet
located, not yet checked against the one edition that matters."

Cheapest next step, in order: (1) get eyes on Boucher tome V/VI directly (library/BnF reading room copy, or a
copy order against MF 33938 if Gallica access is ever blocked) and grep her footnotes for "chiffre"/
"déchiffr" near any f.5-f.183 citation -- this is the single check that would close the print-check gate
either way; (2) if that comes back silent, widen the Gallica sample past canvas 154 (folios past ~105) in the
same 4-canvas-interval style, budget permitting; (3) a cheap side check of fr.17834 vol. I-II (Maisse's own
outgoing register, if it exists and covers Aug 1582 onward) for any note of what he received enciphered.

### Requests this pass

gallica.bnf.fr: 23 (1 manifest.json, 21 probe thumbnails canvas 74-154, 1 recalibration fetch at canvas 106;
two transient connection resets, both recovered on the single allowed retry; no 403/altcha). archivesetmanuscrits.bnf.fr:
3 (parent combined notice, one wrong sibling node caught before use, the correct fr.16092 AJAX component).
googleapis.com/books: 2 (with `&key=$GOOGLE_BOOKS_KEY&country=US`, key never printed). archive.org: 2
(advancedsearch + be-api.us.archive.org full-text search, both inconclusive/negative). catalog.hathitrust.org:
1 (guessed OCLC, empty). WebSearch: 4. No subagents, no logins, no credentials printed.

## Maisse outgoing registers (fr.16089-16091 series), 24 September 2026

Access-worker pass (Sonnet, LANE G, cap $10). Job: chase the previous pass's "fr.17834" lead -- the register of
Maisse's own outgoing letters, the mirror-image collection to this folder's fr.16092/93 (Court-to-Maisse). Two
findings: the series exists and is fully digitised, but **it is not fr.17834** -- that shelfmark was a
misattribution in the earlier pass's WebSearch, corrected here before any fetching against it.

### Correction: fr.17834 is not the register series

`archivesetmanuscrits.bnf.fr/ark:/12148/cc473324` (FRBNFEAD000047332) confirms Français 17834 (ancienne cote
Saint-Germain français 7161) is *"Instructions à divers ambassadeurs français, et autres pièces historiques, de
la fin du XVIe siècle et du commencement du XVIIe"* -- a compilation of instructions to various named
ambassadors (Rambouillet, Turenne, La Fin, Nevers, La Clyelle, La Borde, Lambert, Baradat), of which one item is
"Instruction ... à monsieur de Maisse [Italie], s. d. (f. 169)". This is a single instruction among eleven to
different people, not Maisse's outgoing register, and it is a different Gallica item (ark `btv1b9061239t`) from
either register series. The earlier pass's WebSearch snippet had matched on the word "Maisse" without checking
the returned cote against the notice text -- exactly the mistake this folder's own NOTES.md flagged as a risk
after the fr.16092/93 canvas-node mixup. **This item was not investigated further and nothing was fetched from
it beyond its own catalogue notice.**

### The real series: Français 16089-16091 (Harlay 265 (10-12))

Found by re-deriving the register's own title's shelfmark rather than trusting the earlier WebSearch: the OAI
record for the Gallica item titled "Registre des lettres et dépêches adressées par André Hurault de Maisse à la
Cour... III Janvier 1587-août 1588" (`services/OAIRecord?ark=btv1b90613009`) gives `dc:source` = "Bibliothèque
nationale de France. Département des Manuscrits. Français 16091", not 17834, and points to the catalogue notice
`archivesetmanuscrits.bnf.fr/ark:/12148/cc46222m/cd0e99`. That notice's parent (`cc46222m`, EAD id
`FRBNFEAD000046222`) is the 3-volume series **Français 16089-16091**, and its own AJAX tree endpoint
(`ajaxGetCompDisplay.html?eadCompId=FRBNFEAD000046222`) lists all three children directly (component ids
`_d0e57`, `_d0e78`, `_d0e99`), fetched individually below. So the register series sits immediately *before*
fr.16092 in the shelfmark sequence (16089-91 outgoing, 16092-93 incoming) -- both halves of the same
correspondence, catalogued as neighbouring but separate multi-volume units under "Département des Manuscrits >
Français > Français 15370-17058 [Saint-Germain] > Français 15912-16669".

| Cote | Ancienne cote | Volume | Feuillets | Ark | Canvases | Substitute |
|---|---|---|---|---|---|---|
| Français 16089 | Harlay 265 (10) | I, Nov 1582-Dec 1583 | 609 | `btv1b9061233b` | 624 | MF 33935 / R 16095 |
| Français 16090 | Harlay 265 (11) | II, Jan 1584-Dec 1586 | 678 | `btv1b9061232x` | 690 | MF 33936 / R 16096 |
| Français 16091 | Harlay 265 (12) | III, Jan 1587-Aug 1588 | 884 | `btv1b90613009` | 790 | MF 33937 / R 16097 |

All three are digitised (Gallica, from the substitute microfilm). **None of the three archivesetmanuscrits
notices flags "chiffre" anywhere** -- each notice is just cote/ancienne cote/date-range/extent/subject headings
(Ambassades. Venise.; France à Venise (1582-1595), Hurault de Maisse.; Hurault de Maisse, Paul.; Ambassades à
Venise (1582-1589).), with no item-level content list at all (unlike fr.16092's notice, which does list
individual correspondents by folio and explicitly names the cipher key at f.5). This is a fact about the
catalogue's granularity for this series, not evidence either way about whether cipher appears inside it.

### Contact-sheet sample: 78 of 2,104 canvases, no ciphertext

Sampled each volume's canvases at a roughly even stride (IIIF thumbnails, `,500` width, one request at a time,
>=1.5s apart, UA `cipher-lab research script (contact via repository)`), reviewed as one labelled contact sheet
per volume (`images/reg16089/contact_sheet.jpg`, `reg16090/contact_sheet.jpg`, `reg16091/contact_sheet.jpg`):

- **Français 16089** (I): 26 of 624 canvases (stride ~24), all fetched. Every leaf is clear cursive French
  secretarial-hand copybook text -- headers such as "Lettre a Monsieur de [...]", "Lettre au Roy", "Response par
  lettre du Roy au sieur..." -- exactly the register-copy format expected. No numeral or symbol groups on any
  sampled leaf.
- **Français 16090** (II): 27 of 690 canvases targeted (stride ~26); 25 fetched, canvases 384 and 410 gave
  HTTP 500 on both the first attempt and the single allowed retry (not a 403/altcha/challenge -- treated as a
  server-side fault at that specific canvas number, logged and left unfetched rather than retried further). All
  25 fetched leaves are clear cursive French, same copybook format ("Au Roy", "Response par...", "Depesche
  envoyee...", one leaf addressed to "Monsieur le Cardinal d'Este"). No numeral/symbol groups.
- **Français 16091** (III): 27 of 790 canvases (stride ~29), all fetched. Same pattern -- clear cursive French,
  dated headers ("Aoust 1587", "Mars 1587"), addressed e.g. "A Monsieur de Villeroy", "Au Roy". No numeral/symbol
  groups.

**Across all three volumes, 78 of 2,104 canvases sampled (~3.7%), none ciphered.** This is a sample, not a
census, and (as with fr.16092's own probe) does not rule out an enciphered passage in the ~96% unchecked, but it
is consistent with what would be expected of a register: a clerk's fair copy of outgoing letters *as sent*,
which for a cipher despatch would ordinarily record the plaintext draft rather than the enciphered text that
actually went out (the encryption happens at the point of dispatch, not in the office copy retained). No native
fetches were made (step 3 of the brief is conditional on finding a ciphered leaf; none was found).

### Verdict

Status for fr.16092 itself is unchanged (`open`, still no ciphertext located in it either). This pass adds: the
fr.17834 lead was a misidentification, now corrected; the real Maisse-outgoing register series (fr.16089-16091)
exists, is fully digitised, and a 78-leaf sample across all three volumes found no enciphered passage and no
catalogue "chiffre" flag. It does not settle whether Maisse's side of the correspondence was ever enciphered
(registers by their nature would likely carry the plaintext draft even for despatches sent in cipher); the
Boucher print-check gap (previous pass, still open) remains the cheapest way to close that question, since a
modern edition's apparatus is more likely than a register copy to note a lost decipherment.

### Requests this pass

archivesetmanuscrits.bnf.fr: 8 (reachability probe; the candidate-but-wrong Français 17834 notice `cc473324`;
the vol III notice `cc46222m/cd0e99`; the parent notice `cc46222m`; the parent's `ajaxGetCompDisplay` tree
listing (3 children); the two sibling `ajaxGetCompDisplay` fetches for vols I and II; one static JS file to
confirm the AJAX endpoint pattern), one at a time, >=1.5s apart, no 403/altcha. gallica.bnf.fr: ~97 (1
reachability probe with 1 transient reset+retry; 1 OAIRecord; 3 manifest.json fetches with 2 transient
resets+retries; ~89 IIIF thumbnail fetches for the 78-canvas sample, including 2 permanently-failed-with-500
canvases each retried once per the single-retry rule and then left unfetched), one at a time, >=1.5s apart, no
403/altcha seen. One local issue, not a site block: a single thumbnail request hung for over a minute with no
response (neither an error nor a completion) after several genuine transient resets on the same run; it was
killed locally after being judged a stalled connection rather than waited out further, and the remaining
fetches were run with `--connect-timeout 10 --max-time 25` to avoid a repeat. WebSearch: 2. No subagents, no
logins, no credentials. Images: `images/reg16089/`, `images/reg16090/`, `images/reg16091/` (78 thumbnails +
3 contact sheets, ~1MB total); manifest at `images/registers_manifest.json`.
