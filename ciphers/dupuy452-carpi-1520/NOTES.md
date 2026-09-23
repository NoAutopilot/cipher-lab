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

## Transcription (23 September 2026)

Worker: transcription, no subagent tool available in this session's tool set (checked; the
fallback of two independent readings by the same worker was used instead of two Sonnet
subagents, and only partly executed -- see below). Cap ~$15, good-citizen rule followed
(request counts at the end of this section).

**Method.** Read `date -u` first (23 Sept 2026, 20:35 UTC at start). Full-resolution IIIF fetches
of the canvases the 20 Sept check-solved sweep had only viewed as 900px thumbnails
(`images/img/`), native-resolution line-block crops under 2400px wide (`images/crops/`), single
careful reading (not two independent passes reconciled -- see below), written up in
`ciphertext.txt` (item 20) and `ciphertext_f28.txt` (item 28).

**Major correction to the 20 Sept check-solved characterisation of item 20 (f.20, Carpi to
Madame).** That sweep, working from a 900x672 thumbnail, described "a dense run of
arithmetic-numeral cipher groups" confined to "the final third" of one leaf, "roughly 70-90"
tokens. Full-resolution imaging shows instead:
- The cipher is an **invented symbol/glyph alphabet** (letter-like shapes, not arabic-numeral
  groups), consistent with the 1520s French "chiffre a figures" family Tomokiyo documents for
  this circle.
- **The passage does not end on the recto.** It continues onto the leaf's own **verso** (per the
  brief's "check the verso" instruction) for ~22 more lines, then onto the recto of the following
  leaf -- foliated **"21"** in the manuscript's own period ink, confirmed by eye -- for ~13 more
  lines, before the letter closes in plain French, dated "Rome ce xxvij [27] jour d'Octobre l'an
  mil Vc xxv [1525]", signed "de Carpi". That closing date does not match the finding aid's "22
  oct. 1525" for this item; since the letter reads as one continuous document (no fresh
  salutation restarts on the verso or on folio 21), the likelier explanation is a roman-numeral
  misreading (xxij/xxvij) in the finding aid rather than a second, uncatalogued letter -- flagged,
  not resolved; this is not a claim of a new item (rule 10).
- **Total extent is roughly 44 cipher lines across 3 page-sides** (folio 20 recto tail ~9,
  verso ~22, folio 21 recto ~13), on the order of **500 tokens**, not "70-90" on "one leaf".

Only the originally-scoped portion (folio 20 recto's own cipher tail, 9 lines, 86 tokens by this
reading) is transcribed in `ciphertext.txt`, as a single pass, every token graded M. The zero
repeated tokens across 86 is flagged in `reconciliation.md` as evidence this single pass has not
yet converged on one consistent code per glyph -- a real second, independent pass (ideally with a
glyph inventory fixed from clean exemplars first, per `reconciliation.md`) is needed before this
text supports anything beyond "this letter uses a substitution alphabet of roughly this size and
shape." The verso and folio 21 recto (~35 more lines, not transcribed) have native-resolution
crops saved for that follow-up.

**Job 2: folio 28 (Raince to Madame) -- located and characterised, same cipher, NOT transcribed.**
Paged forward from folio 21 past folio 24 (Nicolas Raince to "Monseigneur" [Florimond Robertet],
IIIF f29-f31 -- itself substantially enciphered in the same alphabet despite carrying no "en
chiffres" note in the finding aid, a second finding-aid omission, flagged only) to folio 28 (IIIF
f34, period foliation "28" confirmed), which matches the finding aid's item 28 exactly (opens
"Madame, pour ce que par les depesches de monseigneur le conte...", closes on f36 "de Rome ce
xxv[e] jour Doctobre l'an mil Vc xxv" [25 Oct 1525], signed "Nicolas Raince"). **Same cipher as
item 20**, confirmed by eye: same glyph repertoire, and a specific rare mark (a distinctive "three
small boxes in a row") recurs on both folio 20 recto and folio 28 recto -- real (if informal)
evidence of one shared embassy cipher used by both Carpi and Raince in Rome, Oct 1525. Item 28 is
markedly **larger than item 20**: folio 28 recto ~15 cipher lines, then folio 28 verso + folio 29
recto (one opening) **entirely in cipher, both full pages**, ~30 lines each, then 6 more lines on
folio 29 verso before the plain close -- roughly **80 cipher lines, ~900-1000 tokens**, about
twice item 20's corrected size and 10-12x the original ~70-90-token estimate for the smaller item.
Not transcribed token-by-token (out of proportion to this worker's cap given item 20 already
exceeded it); a representative sample crop of the recto's cipher opening is saved
(`ciphertext_f28.txt`, `images/crops/f34_folio28r_cipherstart_sample.jpg`) confirming the alphabet
match, plus 1600px-wide reference images of all three canvases (`images/img/`) so a follow-up
transcription worker does not need to re-locate this item.

**Job 3: the four 1535 "Dechiffrement" leaves (ff.56, 60, 72, 76) -- NOT located this pass.**
Gallica's `ContentSearch` (search-inside) service returns 0 results for this ark (manuscripts are
not OCR'd on Gallica, only printed books), so there is no shortcut past canvas-by-canvas paging.
The canvas-to-folio offset is confirmed non-linear (it grows irregularly as unfoliated
address/wrapper leaves are inserted -- see `images/manifest.json`'s note), so extrapolating a
fixed offset from folio 20/21/28's position (+3 to +6) does not reliably predict where folio 56
falls. Canvases sampled at reduced width without a positive identification: f58, f60, f62, f64,
f66, f68, f70, f72, f74, f76, f78 (a period marginal annotation resembling "Segrement..." was seen
near f64 but not confirmed as one of the four "Dechiffrement" items, and not investigated
further). None of the four leaves was viewed; whether they carry interlinear or parallel plaintext
is therefore still unknown. Next worker should either page more densely in this range with full-
resolution fetches (period foliation is only reliably visible at full IIIF resolution, not at the
900px width used for this scan) or use the reading-room "aller a la page" folio box, which is not
available to curl/browser_fetch.

**Job 4: key-family leads (grep only, not applied).** `sources/cryptiana/web/francis.htm`
(Tomokiyo) grepped for "carpi", "duprat", "louise": no exact-match key exists for this volume's
correspondents (confirming the 20 Sept sweep's finding). The strongest candidate for a solver,
unchanged in kind but strengthened by this sweep's direct glyph comparison, is **Raince's Cipher**
(BnF fr.2984, 1526, reconstructed by Tomokiyo from Desenclos 2018; the same system recurs in fr.3040,
1526, and fr.3091, 1529) -- it is by the SAME secretary who wrote Dupuy 452's item 28, one year
later, and every 1520s-1530s French cipher this page describes (Raince's, Calvimont-Duprat's
[BnF Clair.325 f.67, solved by Biermann 2021], Bayonne's [BnF Clair.328/329/330, solved by Lasry
2022], Gramont's [BnF Clair.330 f.53, solved by Lasry 2022/2023]) is the SAME cipher type observed
here: an invented monoalphabetic symbol substitution, never a numeral-group cipher (grepped
"numeral"/"digit"/"figure" in francis.htm: no hits at all -- this whole family is symbol-based).
No other page in `sources/cryptiana/web/` names Carpi, Duprat-as-recipient-of-Carpi, or Louise de
Savoie as a cipher's addressee. A solver's first check should be Raince's own fr.2984 key against
item 28 (same author, one year on) and then, if it fits, against item 20 (same embassy, same
fortnight) -- not applied here, per the brief.

**What a next solver needs:** (1) a genuine second, independent transcription pass reconciled
against this session's single pass for folio 20 recto (`reconciliation.md` says how), (2) a first
transcription pass for folio 20 verso + folio 21 recto (crops saved, ~35 lines) and for all of
item 28 (crops/reference images saved, ~80 lines) with a glyph inventory fixed in advance from
clean exemplars rather than assigned ad hoc while reading running text, (3) Raince's fr.2984 key
tested against item 28 first, (4) the four 1535 leaves still need locating and viewing (job 3),
(5) the finding aid's "22 oct." date for item 20 vs. this leaf's own "27 oct." dateline needs
resolving (roman-numeral misreading vs. two letters), (6) item 24 (Raince to Robertet) is also
substantially enciphered despite no "en chiffres" note in the finding aid -- a third finding-aid
omission in this volume, worth a one-line check-solved note but not pursued further here.

Requests this pass: gallica.bnf.fr approx. 55 (1 full IIIF manifest, 1 Pagination service call,
~50 IIIF image fetches at reduced/1600px/full width incl. 3 connection resets each retried,
1 ContentSearch call), archivesetmanuscrits.bnf.fr 3 (1 plain-curl 403 needing a UA/protocol
retry, then 2 https fetches at HTTP 200). No WebSearch used. No subagents (none available; see
reconciliation.md).

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

## Print check, class gate (23 September 2026)

Worker: print-check (Sonnet, cap ~$6, no subagents). Read `date -u` first (21:16 UTC). Question:
are the three Oct 1525 letters (f.20/21 Carpi to Louise de Savoie, f.28 Raince to Madame, f.24
Raince to Robertet) already in print, and has this cipher already been read anywhere, before any
transcription spend proceeds. This gates on top of, and does not repeat, the 23 Sept check-solved
sweep already in this file.

**Per letter:**
- **f.20/21, Carpi to Louise de Savoie, Rome, 22 or 27 Oct 1525** -- not found printed in clear,
  not found printed as cipher, in any edition or scholarship reached this sweep.
- **f.28, Raince to "Madame" [Louise de Savoie], 25 Oct 1525** -- same, not found anywhere.
- **f.24, Raince to Robertet, [24] Oct 1525** -- same, not found anywhere.

**Has the cipher itself (the embassy's Oct 1525 symbol alphabet) been read anywhere?** Not found.
The one cipher-reading project that touches this same secretary, Nicolas Raince, is Bourdeau's
`cyphersolver/raince/` (checked below) -- but it is built entirely on **fr. 2984, fr. 3040 and
fr. 3091 (1526 and 1529)**, a full year or more later and a different volume, using Tomokiyo's
published key reconstructed from Desenclos (2018). Neither that folder, nor any file this sweep
reached, ever names Dupuy 452, folio 20/21/24/28, or any 1525 date for Raince's or Carpi's cipher.
It is a real, named lead for a solver (Raince's own hand, one year on) but is not itself a prior
reading of these three letters.

### 1. Champollion-Figeac, *Captivité du roi François Ier* (1847), archive.org identifier
`bub_gb_DdUWAAAAQAAJ` (already identified by the 23 Sept check-solved sweep; not re-identified
here). Full text downloaded once (`archive.org/download/bub_gb_DdUWAAAAQAAJ/bub_gb_DdUWAAAAQAAJ_djvu.txt`,
1 fetch, reused for all queries below rather than re-querying be-api per term where a local grep
sufficed) and be-api full-text-search queried per term (5 queries, all against this one identifier):

| query | be-api hits | what it is |
|---|---|---|
| "Raince" | 0 | -- |
| "Carpi" | 0 (checked by the 20/23 Sept sweep already; not re-run) | -- |
| "chiffres"/"chiffre" | 1 (page 762) | Louise de Savoie ("LOYSE") to the King, undated, "Section IV -- Délivrance du roi" (1526, after the king's release terms): "Monseigneur, pour ce que par le chiffre vous serez entièrement satisfait de ce que vous a pieu mander par Babou..." -- names a cipher passage carried by the messenger Babou but does not quote or discuss it, and is not about Rome, Carpi or Raince. Not our letters. |
| "Robertet" | 1 (page 762, same neighbourhood) | No. CLXXIX, "Lettre du secrétaire Robertet à Madame la duchesse d'Alençon", dated "ce vij d'octobre" [no year given in the OCR'd heading; context is Section III "Captivité en Espagne", i.e. late 1525/early 1526, Madrid] -- Robertet writing *to* Marguerite d'Alençon about the king's Spanish captivity, not Raince or Carpi writing *to* Louise de Savoie from Rome. A different letter, different sender, different recipient, different place. Not our letters. |
| "dechiffr" | 0 | -- |
| "Carpy" (spelling variant) | 0 | -- |

Every hit read in full context (lines around each match in the downloaded djvu text). **Negative,
and now checked under more spelling/term variants than the 23 Sept sweep's two** ("Carpi",
"chiffres" only): this edition does not print or discuss the three Oct 1525 Rome letters or their
cipher, under any of Raince, Robertet, chiffre(s), déchiffr*, or Carpy. Still not exhaustive for
OCR error on an 1847 print (e.g. a mis-OCR'd "Carpi" is possible but the surrounding terms --
Robertet, Raince, Madame -- give six independent ways in and none hit the right passage).

### 2. Desenclos (2018) and Tomokiyo's `francis.htm`
WebSearch confirmed the paper's full title and venue: Camille Desenclos, "Unsealing the Secret:
Rebuilding the Renaissance French Cryptographic Sources (1530-1630)", *Proceedings of the 1st
International Conference on Historical Cryptology* (HistoCrypt 2018). Its own title's date range
(1530-1630) already excludes 1525-26 material by a few years, though Tomokiyo credits it with
locating the 1526 Raince letters in fr.2984, so the range is evidently not exact. `francis.htm`
(grepped again this sweep for "Raince", "2984", "Carpi", "Dupuy 452", "Dupuy452" -- same negative
the 23 Sept sweep found, re-confirmed): the page's "BnF fr.2984 (1526)" section names only 1526
Raince letters (ff.21/25/29/33/41/47/99/105/117/123, May-Dec 1526) and a 1529 set (fr.3091 f.19);
**no mention of Dupuy 452, no mention of 1525, no mention of Carpi anywhere on the page.** The
"BnF fr. 2984 (1526)" section explicitly gives dates from 1 May to 7 Dec 1526 -- a full year after
the Oct 1525 letters in Dupuy 452.

`cyphersolver/raince/NOTES.md` (Bourdeau's repo, fresh local clone from 23 Sept 2026, git HEAD
`2e9ec01`, reused rather than re-cloned -- see item 4) gives the fullest published account of what
has and has not been read in the Raince corpus Tomokiyo/Desenclos cover: the 1526 fr.2984 letters
have a mix of prior decipherment (Mignet 1886's clear duplicate for the 9 June letter, Bourrilly
1901's printed cipher passages for 17 June/20 Aug, contemporary interlinear glosses for several),
Bourdeau's own 2026 reconstruction work on the unread residue (13 May and 20 Nov letters), and
DECODE holds two of the set (fr.3040, fr.3091) as already decrypted. **None of this is Dupuy 452**:
different shelfmark, different year (1526/1529 vs 1525), and the folder never names Dupuy 452,
Carpi, or any Oct 1525 date (grepped `NOTES.md` and every `.json`/`.txt` file in the folder for
"dupuy 452", "dupuy452", "1525"; only unrelated hit was Bourrilly's aside "the Carpi letters of
the volume" -- referring to *fr.2984's own* Carpi correspondence, a different, uncounted item in
that other manuscript, not Dupuy 452).

### 3. Other editions (WebSearch)
- `Guiffrey "Lettres de Louise de Savoie" OR "Négociations diplomatiques" Alberto Pio Carpi Rome
  1525 chiffre` -- no edition surfaced beyond the BnF finding aid notice itself (which the search
  engine echoes back, circular, as in the 23 Sept sweep).
- `Guasti "Alberto Pio da Carpi" corrispondenza lettere edizione` -- confirms the only modern
  Alberto Pio letter edition is Ori/Saetti, *Alberto Pio da Carpi e l'arte della diplomazia. Le
  "lettere americane" e altri inediti* (Carpi, 2015) -- the UPenn corpus already ruled out by the
  23 Sept sweep as a *different* set of letters (1512-23, to Maximilian I/Lang). No Guasti edition
  of Carpi's letters was found to exist as a distinct, separate work; may be a misremembered
  citation, not chased further (out of scope for a $6 cap).
- `"Revue d'histoire diplomatique" Carpi ambassadeur Rome 1525 François Ier captivité` -- surfaced
  general scholarship on the 1525-26 captivity and on Rodolfo Pio da Carpi (Alberto's nephew, a
  different, later Carpi, Bishop of Faenza) and Acta Nuntiaturae Gallicae volumes for 1535-1540
  papal nuncios Carpi/Ferrerio -- again a different, later Carpi. Nothing naming our three letters
  or an edition of them.
- `Bourrilly OR Desenclos Nicolas Raince ambassade Rome 1525 Carpi lettres chiffre Dupuy` -- every
  result traces back to the same BnF finding-aid notice (`archivesetmanuscrits.bnf.fr/ark:/12148/cc885911`)
  already known from this project's own prior sweeps; no independent edition or scholarly citation
  of these three letters found.
- Guasti's *Négociations diplomatiques entre la France et la Toscane* and Brewer's *Letters and
  Papers, Foreign and Domestic, Henry VIII* were named in the brief as candidates but not reached
  by page (as the 23 Sept check-solved sweep also flagged) -- WebSearch surfaced no evidence either
  prints this correspondence, but this remains an unchecked gap, not a negative, per the earlier
  sweep's own caveat.

### 4. Solver repositories
Reused the fresh shallow clones already present in this session's shared scratchpad rather than
re-cloning (no new network requests): `cyphersolver` (dbourdeau, git HEAD `2e9ec01`, committed
2026-09-23 08:37 local) and `unsolved-ciphers` (aaymeloglu, git HEAD `6f9c462`, committed
2026-09-21 17:08). Grepped both, case-insensitive, for "dupuy 452", "dupuy452", "carpi", "raince":
- `cyphersolver`: no file anywhere in the repo names "Dupuy 452"/"Dupuy452". "carpi"/"raince" hits
  are confined to `cyphersolver/raince/` (fr.2984/3040/3091, see item 2 above) and one Bourrilly
  citation aside; `CATALOGUE.md`, `SOLVED_CATALOGUE.md`, `SOLVED_RANKING.md` have no Dupuy-452 or
  Carpi row (consistent with the 23 Sept check-solved sweep's own grep of these same files).
- `unsolved-ciphers`: `CATALOGUE.md` and `catalogue/bne-ranked.md` matched only on unrelated
  substrings (checked, no Dupuy 452/Carpi/Raince row).

### Requests this section
be-api.us.archive.org (fts): 5 queries. archive.org: 2 (1 `metadata`, 1 djvu.txt download, both
against the identifier already known from the 23 Sept sweep). WebSearch: 7 queries. No new git
clone (reused existing checkouts, 0 network requests for the repo grep). No HathiTrust API call
needed (archive.org full text was usable, per the brief's fallback condition). No logins used.

### Gate verdict

All three letters unprinted in clear and unprinted as cipher, under every source and spelling
variant reached (Champollion-Figeac full text, Desenclos's own paper title/venue and Tomokiyo's
page built from it, WebSearch across Guiffrey/Négociations/Guasti/RHD, and both solver
repositories' full text). The embassy's Oct 1525 cipher itself has not been read anywhere found;
the nearest thing to a lead is Raince's own, later (1526/1529) reconstructed key for a different
manuscript (fr.2984/3040/3091), not a reading of Dupuy 452. Per rule 10, this is a search result,
not a novelty verdict, and none of the words "new", "unpublished", "first" or "never printed" is
used above or should be used elsewhere in this file until a verifier session runs.

**Gate: best case N3; transcription may proceed.**
