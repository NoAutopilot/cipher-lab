partial
RIDA vol. XIX "Florence, Modène, Gênes" (Driault 1912, Gallica bpt6k9630935d) full-text searched by this worker via Gallica's ContentSearch API (control: "Florence" 182 hits, "Genes" 263 hits, confirming the OCR search executes on this volume) for "Paget" (3 hits, none this Paget -- a footnote cross-reference and two unrelated index entries for "Pagès"/"Pages") and "Cagliari" (0 hits); AN AE/B/I sub-series (registers of orders/dispatches) only covers 1756-1793 per its own finding-aid description, so it cannot hold this 1714 letter regardless of digitisation; the actual holding series (AN Marine B7, per OX-PAGK's 25 Sept identification) is already queued at LOCAL-QUEUE.tsv row L11, not duplicated here.

## Check-solved (LANE CX2, 25 Sept 2026, CX2-MISC2)

Intake verdict: open. Fresh six-source sweep this pass, per the job brief's edition list (RIDA, AE B I consular inventory, Gallica SRU) plus the standard six:

1. **Web.** `Recueil des instructions données aux ambassadeurs Genes` (confirms vol. XIX = "Florence, Modène, Gênes", ed. Driault 1912, on Gallica `bpt6k9630935d`, no Genoa-specific RIDA volume before this one); `"correspondance consulaire" Gênes archives affaires étrangères B I inventaire` (AE/B/I registers of orders/dispatches run 1756-1793 only -- too late for 1714; consulate-of-Genoa records for this period sit in AN Marine sous-série B7, per the finding-aid PDF at archivesnationales.culture.gouv.fr, matching OX-PAGK's 25 Sept identification already queued at LOCAL-QUEUE L11); `Pierre Paget vice-consul Gênes Cagliari 1714 consul Sardaigne` (no new biographical source beyond OX-PAGK's Mezin/Ulbert/AN-inventory identification already in this file). No model-solve announcement search this pass (already covered 23-25 Sept, unchanged).
2. **Print/edition.** RIDA vol. XIX (Driault 1912, Gallica `bpt6k9630935d`) full-text searched via Gallica's ContentSearch API (an OCR search scoped to this one volume, distinct from the Gallica-wide SRU metadata search, which is metadata/title-only and returned irrelevant catalogue noise for "Paget"+"Cagliari" -- logged so a future worker does not repeat that mistake): "Florence" 182 hits and "Genes" 263 hits (control, proving the search engine returns real content from this book), "Paget" 3 hits (a Prussia-instructions footnote citing "G. Pagès" the historian, the word "pages", and an index entry "PAGES (Georges), 38" -- none the vice-consul), "Cagliari" 0 hits. "consul" errored twice (`Recv failure: Connection reset by peer`, one retry per the good-citizen rule, not retried again). This RIDA volume publishes instructions *sent* by Versailles to its resident minister at Genoa, not incoming consular correspondence *received* from a vice-consul -- a different genre from what would carry Paget's letters even if it covered 1714, which on this evidence it does not name him. AE/B/I dated-range exclusion as above (web search, item 1).
3. **Community lists.** Unchanged from 23 Sept sweep (cryptiana grepped, no hit beyond the unrelated Charles Paget/Mary Queen of Scots cipher already flagged); not re-run this pass (no new source appeared in items 1-2 to search for).
4. **DECODE.** Unchanged from 23 Sept (cached catalogue grepped for "paget", "clairambault 1225": no hit); not re-run this pass.
5. **Bourdeau.** Unchanged from 23 Sept (fresh-clone grep for "paget": no hit); not re-run this pass.
6. **Aymeloglu.** Unchanged from 23 Sept (fresh-clone grep for "paget": no hit); not re-run this pass.

No printed source located by this worker carries either Paget letter's ciphered passages in clear. Nothing here is claimed as new, unpublished or first (rule 10). Requests this pass: gallica.bnf.fr 6 (2 SRU metadata queries -- noted as not fit for purpose, superseded by 4 ContentSearch calls on the one scoped volume, all >=1.5s apart, one connection-reset on "consul" retried once and still failing), googleapis.com/books 0 (not needed this pass), WebSearch 4.

# "Lettres autogr. de Paget, avec chiffre, 1714" -- BnF Clairambault 1225

QUEUE row: M4 (sources/solver-diffs/2026-09-23-digitised-hits.tsv, "Digitised candidates, no copy needed").

## Source

BnF, Departement des Manuscrits, **Clairambault 1225**, Gallica `ark:/12148/btv1b9001034d` (268 leaves),
"CXV Melanges" (the last, catch-all volume of Clairambault's 120-volume "Minutes du Recueil pour servir a
l'histoire de l'Ordre... du Saint-Esprit" research series). BnF Archives et manuscrits notice (item-level
index) `http://archivesetmanuscrits.bnf.fr/ark:/12148/cc137837/cd0e29423`, precise entry: **"Fol. 48 --
Rosset de Fleury (testament du cardinal ; lettres autogr. de Paget, avec chiffre, 1714)."** The same
notice's name-index confirms this independently: **"PAGET -- Lettres chiffrees"** (plural), i.e. more than
one enciphered Paget letter. The item sits inside a single physical dossier grouped under the "Rosset de
Fleury" family name, alongside an unrelated cardinal's testament -- almost certainly a bundling of unrelated
autographs from one acquisition lot, not evidence the two items are historically connected.

## Check-solved sweep (23 September 2026)

1. **Web search.** `Paget 1714 lettre chiffre ambassadeur Constantinople OR "Lord Paget"` -- confirmed
   William Paget, 6th Baron Paget (ambassador at Constantinople 1692-1702) **died in 1713**, ruling him out
   for a 1714-dated letter. `"Henry Paget" OR "William Paget" 1714 letter cipher diplomat` -- surfaced the
   strongest lead: **Henry Paget (1663-1743), 7th Baron Paget**, who succeeded his father 26 Feb 1713 and
   was appointed Envoy Extraordinary to the Elector of Hanover on 1 May 1714 (refusing to go unless made an
   Earl; secured the earldom of Uxbridge from George I in October 1714) -- exactly the Hanoverian-
   succession window (Queen Anne died 1 Aug 1714, George I acceded) a cipher letter of this date would most
   plausibly concern. **Not confirmed by document inspection** (see below) -- reported as the best-sourced
   candidate, not an identification.
2. **Print/scholarship.** No dedicated edition search run beyond the web search above; History of
   Parliament Online's entry for Henry Paget was the source for his 1714 Hanover mission, not a
   cipher-specific source.
3. **Community lists.** `sources/cryptiana/web/mary.htm` names an entirely **different, unrelated** "Paget's
   Cipher": Charles Paget's correspondence with Mary Queen of Scots (SP53/15-16, 1585-86), keyed at SP53/22
   f.47 -- over a century earlier, a different Paget, a different cipher, a different archive. Flagging
   this explicitly so a future search for "Paget's Cipher" does not conflate the two. No other cryptiana
   page, and no cipher blog or list, mentions Clairambault 1225 or a 1714 Paget cipher.
4. **DECODE.** Cached catalogue grepped for "paget", "clairambault 1225": no hit.
5. **Bourdeau.** `cs-recheck/CATALOGUE.md`, `SOLVED_CATALOGUE.md`, `TARGETS.md` grepped for "paget": no
   hit.
6. **Aymeloglu.** `ay/CATALOGUE.md`, `TARGETS.md`, `SHORTLIST.md` grepped for "paget": no hit.

Requests: gallica.bnf.fr 6 (1 OAI GetRecord, 1 IIIF manifest, 1 Pagination service call [0 folio numbers],
1 ContentSearch call [0 OCR hits], 2 IIIF image probes), archivesetmanuscrits.bnf.fr 1 (HTTP 200, the
composite 120-volume finding aid, containing all of Clairambault 1111-1230; the specific "Clairambault
1225" section was located within it by heading search). WebSearch 2 queries.

**Requests, 25 September 2026 (OX-PAG, folio-pinning + imaging pass):** gallica.bnf.fr approximately 40
(1 IIIF manifest fetch via `tools/gallica_folio.py`, ~32 image/region fetches saved to
`images/bracket/` for the bracket search and corner-numeral checks, ~5 `info.json` size checks not saved
as files, 2 transient `Recv failure: Connection reset by peer` -- each retried once after a pause and
succeeded, no third attempt). All requests sequential, one at a time, >=1.5s apart (most loops used 1.6s).
No 429/403/challenge seen. This is a single Gallica "slot" (OX) per COMMON; released at the end of this
session (see ROOM.md).

## What the leaves show (25 September 2026, OX-PAG)

**Located and imaged.** Folio 48 is pinned with direct confirmation, not a guess: the leaf tab reads
"Rosset-de fleury." and the item heading reads "Testament de M. le Card. de Fleury Ministre d'Estat et
cyder. Precepteur du Roy Louis XV." -- Gallica canvas `f55` (IIIF `f`-number; see
`images/manifest.json`'s `folio_pinning` note for the corner-numeral method and offset). The prior sweep's
two probes (canvas `f48`, `f54`) were simply the wrong canvases, off by the offset now established; both
kept in `images/` for the record.

The dossier reads, in canvas order: Cardinal Fleury's testament (`f55`-`f56`, vol.folio 48-49, dated "fait
a Issy le 6 janvier 1743"), a biographical notice of Fleury (`f57`-`f59`, vol.folio 50-52, seen at 1400px,
not saved -- not part of either Paget letter), then **two enciphered autograph letters from Paget**,
writing from Genoa ("Gennes") to an unnamed French "Monseigneur", each opening "Monseigneur, J'ay receu
la/les lettre(s)..." and closing "Je suis avec tres profond respect, Monseigneur, De Vostre Excelence, Le
tres humble et tres obeissant serviteur, [signed] Paget":

- **Letter 1**: `f60` (start, right page only) through `f65` (left page, signed). Dateline **"A Gennes le
  8e Avril 1714."** Content: Venetian news via "M. l'Abbe Lomelini"; the France-Empire peace (Treaty of
  Rastatt, concluded March 1714) and whether "le Roy de Sicile" (Victor Amadeus II) is covered by it;
  Genoese banking-family news (the death of the banker marquis Pallavicino, the Grimaldi and Rospigliosi
  families); a new vice-consul, "Langier de Toulon"; and Paget's own request that Monseigneur send his
  "expeditions" so he can take up **"le consulat de la nation en Sardaigne"** that has been destined for
  him, referring back to a memoire on the duties of a consul he had sent in April 1712.
- **Letter 2**: `f65` (right page, start) through `f66` (both pages, signed). Dateline **"a Genes le 28
  aoust 1714."** Content: much more heavily enciphered throughout -- dynastic/marriage politics around
  Parma, "le Prince Francois Farnese", "le Roy d'Espagne" and "Madame la Duchesse", consistent with the
  run-up to Elisabeth Farnese's marriage to Philip V of Spain (September 1714, about a month after this
  letter).

**The cipher is a nomenclator**, not a full substitution: continuous French prose with isolated
period-separated numbers (2-3 digits, values roughly 1-300 seen so far) standing in for proper names,
places and sensitive terms; the surrounding French is never enciphered. Token density varies sharply by
passage -- some paragraphs (Genoa gossip, the plague news) carry no cipher numbers at all, others (most of
Letter 2) are almost continuously coded. **No interlinear or marginal gloss/decipherment was seen on any
leaf** (checked per `.claude/briefs/transcription.md`'s pre-pass rule (a) on every fetched image) -- this
looks like a live, unbroken nomenclator, not a found-solved leaf; nor was a second copy of either letter,
or a printed edition of the passages, checked for this pass (rules (b)/(c) of the same brief, left for the
next worker; see Next).

This resolves "which Paget": the document itself names only "Paget" (no forename or title given in what
was read), writing in French from Genoa about Mediterranean/Italian affairs and his own pending consular
appointment to Sardinia. Nothing here supports or requires the earlier "Henry Paget, 7th Baron
Paget/Hanover mission" lead from the 23 September web search (an English peer's Hanover mission does not
fit a French-language letter from Genoa about a French consulship in Sardinia); that lead is now
considered unlikely rather than the best-sourced candidate, but not formally ruled out by name-search this
pass. This is a document-based finding, not a web-search lead: grade C-adjacent for "sender = someone
named Paget, at Genoa, 1714" (read directly off the signature and dateline), nothing here is a
decipherment or claimed as new/unpublished/first (rule 10).

Full canvas-by-canvas description, IIIF URLs and the folio-pinning method are in `images/manifest.json`.

## Edition risk

**Unresolved, narrower now.** No scholarship, cipher blog, DECODE record or solver-repository entry names
Clairambault 1225 or this Paget correspondence (23 Sept sweep, sources 3-6 above). Not yet checked this
pass: a phrase/name search for "Paget" together with "consul" and "Sardaigne" or "Gennes"/"Genes" 1714 in
French diplomatic-history scholarship (AE Correspondance Politique Genes inventories, any published guide
to French consuls in Sardinia/Genoa), which the old-series page stamps ("239"..."281") suggest these
letters were extracted from -- a continuously paginated volume of outgoing/incoming consular
correspondence, not this Clairambault "Melanges" binder's own numbering. That volume, if identified, may
also hold the nomenclator's key or a decipherment.

## Verdict

**Partial: located, imaged, dated, signed and described; not yet transcribed or decoded.** Two Paget
letters confirmed (matches the finding aid's plural "PAGET -- Lettres chiffrees" exactly), dated 8 April
and 28 August 1714, Genoa. Nothing here is claimed as new, unpublished or unread (rule 10) -- only that a
search by the methods logged found nothing describing this correspondence.

## Next

1. **Transcribe.** Two independent blind Sonnet passes + `tools/reconcile_passes.py` per
   `.claude/briefs/transcription.md`, into `ciphertext.tsv` (nomenclator numbers only need to be captured
   accurately; the surrounding French can be read more loosely but should still be captured for context/cribs).
   Scope: 7 canvases (`f60`-`f66`, `images/manifest.json`), roughly 12 written pages, two letters. Not
   attempted this pass -- out of proportion for one Sonnet worker under a stall-alarm cap; this is really a
   `transcription.md`-scale job (its own $30 cap, Fable reconciliation) or a lane of its own.
2. **Old-series page numbers** ("239"-"281" on these leaves, distinct from this volume's own foliation --
   see `images/manifest.json`) are a strong hint these letters were extracted from a continuously paginated
   register, almost certainly BnF or AE (Ministere des Affaires etrangeres) Correspondance Politique,
   Genes, 1714. Identifying that register (an archives.diplomatie catalogue search, or a BnF/AE
   correspondence-politique guide) before transcribing could turn up a printed calendar, an index of
   consuls, or the key itself.
3. Search "Paget" + "consul" + "Sardaigne"/"Genes" 1714 in French diplomatic-history scholarship
   (OpenAlex/Persee/HAL per the Access playbook) and in any guide to the AE's Correspondance Politique
   Genes series, before a solver session assumes any identification of this Paget.
4. The Henry Paget/Hanover-mission lead (23 Sept sweep) can likely be dropped given the document's own
   French-language, Genoa/Sardinia content, but was not formally re-searched-and-ruled-out this pass.

## Transcription (25 September 2026, OX-PAGT)

**Correction to the 25 Sept OX-PAG note above.** OX-PAG's "What the leaves show" section says "No interlinear
or marginal gloss/decipherment was seen on any leaf". That is not quite right: letter 1 (not letter 2) carries
several small interlinear insertions, in what reads as the same hand as the running text, written directly
above short cipher runs and functioning as plaintext glosses for them -- e.g. "Mr l'abbé Lomeliny" written
above "M. 145.31.67.148.186.147.176." on f60R (verified by direct inspection at native resolution, not just
from a transcription pass), and "Gile de Labargue" above "147.46.146.87. / 232.66.45.204." on the same leaf.
This is **not** the transcription.md pre-pass rule (a) case ("every group has one -> recovery target, stop
before starting passes"): most cipher groups in both letters, and effectively all of letter 2, have no gloss
at all -- f66 (the densest cipher page) has none. So this was correctly run as a transcription target, not
handed to a solver first. But it does mean letter 1 is not a *blind* nomenclator throughout: it carries a
handful of contemporary(?) plaintext cribs for specific codes, listed below. Grade for this correction:
C-adjacent (read directly off the image at native resolution by this worker), not from either transcription
pass alone.

**Method.** Images: 13 native-resolution page-half crops (`images/f60R.jpg` ... `images/f66R.jpg`, 1700px
wide, 220px overlap across each book gutter so no token is cut between halves), cut from Gallica's full native
IIIF resolution (6648x5624 to 7931x6323 px per canvas) with `tools/iiif_lines.py` to fetch each canvas once,
then a one-off split script (not committed as a shared tool -- a single gutter-detection + crop call per
canvas, not reusable machinery); superseded OX-PAG's 1400px full-canvas images as the transcription source.
`images/manifest.json`'s `transcription_crops` block has the method, fetch log and reading order.

Two independent blind Sonnet passes (`passA.tsv`, `passA_context.md`, `passB.tsv`, `passB_context.md`), each
reading all 13 images cold, in order, with no access to the other pass or to any existing transcription,
instructed to number manuscript lines `<image>_L<NN>` and record every clear word and every cipher number
group as one token (kind: clear/cipher/insertion-clear/insertion-cipher/pagenum/heading/signature/dateline;
conf: H/M).

**Reconciliation.** The two passes' own line numbering disagreed by one line in several places (mainly
whether a leaf's old-series pagination stamp got counted as its own line), which cascades into a near-total
line-ID mismatch for everything after the split and made `tools/reconcile_passes.py`'s line-keyed alignment
next to useless on the raw files (33.7% agreement). Fixed with a per-target `reconcile.py` (committed here):
drop pagenum-only lines and renumber per image per pass, then align each image's full token sequence with
`tools/reconcile_passes.py`'s own Needleman-Wunsch aligner (imported, not reimplemented) instead of aligning
line-by-line -- legitimate here because each image is one page's continuous running prose with no internal
column break (the gutter split already happened when the crops were cut). Run `python3 reconcile.py` from
this folder to regenerate `ciphertext.tsv` from `passA.tsv`/`passB.tsv` (rule 7).

One classification bug caught and fixed during this session: an early draft inferred kind (clear/cipher) from
whether a token was a digit string, which miscounted the "1714" in both letters' own datelines (and other
plain-French numbers like "19." or "25. Octobre") as cipher groups. `reconcile.py` instead carries the kind
field through from whichever pass's row the aligned token came from, never re-infers it.

**Known reconciliation artifacts (not hand-fixed, so nothing here is silently repaired -- rule 2).** Five
`ciphertext.tsv` rows on f66L/f66R have kind `cipher/insertion-clear` or `clear/cipher`: the aligner matched a
digit token from one pass against a word token from the other at the same column. Checked directly against
the image for four of them (f66L positions 124/125/149/197): the words are right ("taille", "belle", "air",
"sa", matching visible interlinear insertions "La taille belle" over one cipher run and "d'esprit et un air"
over another) and the paired digit is an alignment artifact from a token-count mismatch a few positions
earlier, not a real second reading of the same span. Left as-is with the full alt detail rather than edited,
per rule 2; a future pass should re-derive f66L positions ~120-150 directly rather than trust either column.

**Stats.** `ciphertext.tsv`: 2340 tokens, 1957 H / 383 M (grade counts, not H/C/S/M/I per rule 4 -- this is a
transcription, not a claimed reading; every cipher token here is graded M or H for *transcription* confidence
only, not S for a cryptanalytic result, since nothing is decoded).

| | Letter 1 (8 Apr) | Letter 2 (28 Aug) |
|---|---|---|
| numeric cipher tokens | 96 | 404 |
| distinct codes | 51 | 109 |
| value range | 20-276 | 2-692 |
| codes seen >=2x | 22 (67 tokens) | 66 (361 tokens) |
| most frequent codes | 46, 45 (x6), 145/67/147/244/146/175 (x4) | 46 (x31), 146/41 (x16), 87/34 (x15), 221 (x13) |

Overall: 122 distinct numeric codes, 500 numeric cipher tokens (plus one hand-marked ILLEGIBLE group, f61L,
solid-inked over), range 2-692 (two-thirds of distinct codes are 2-3 digits; a handful of higher outliers,
mostly on f66, the hardest page -- both blind passes independently graded nearly every f66 cipher digit M, so
treat 66x-range values there as the least certain readings in the set, not confirmed high code values).
**38 of letter 1's 51 distinct codes recur in letter 2** -- strong evidence the two letters use the *same*
nomenclator key, which matters for a future solver: letter 2 alone gives a much bigger sample (404 vs 96
tokens) to key-fit, and any key recovered from one letter should be checked against the other.

**Nomenclator shape, from the ranges only (no decoding attempted).** The handful of codes glossed by name
(below) need 6-7 separate cipher groups to spell one proper name ("Lomeliny", 8 letters, glossed by 7 groups)
-- consistent with a per-letter or per-syllable substitution table, not a whole-word code. That is also
consistent with the frequency profile: the commonest codes (46: 37 occurrences across both letters; 146: 20;
41: 17; 87/34: 16 each) recur far too often for rare proper names and read like codes for common letters,
syllables, or short function words scattered through the "obscured" spans, while the ~60 hapax-or-rare codes
in the 100-300 range look like the less-common letters/syllables or the handful of actual glossed names. In
short: probably a homophonic/nomenclator table of a few hundred cells (codes seen top out under 300, aside
from the small number of higher outliers on the hardest page), mixing common-letter/syllable codes with
name/place codes, not a single-substitution cipher and not a large whole-word nomenclator.

**Interlinear glosses in letter 1 (the crib list for a future solver).** Every insertion-clear token pass A
and/or pass B read directly above a cipher run in letter 1 (grade M throughout -- the two passes disagree on
exact spelling in several cases, both readings kept in `ciphertext.tsv`'s alt column):

| Leaf | Gloss (as read) | Sits above | Cipher groups |
|---|---|---|---|
| f60R | "Mr l'abbé Lomeliny" / "Mr Labbé Lomeliny" | "M. 145.31.67.148.186.147.176. m'ecrit encore de Venise" | 145,31,67,148,186,147,176 |
| f60R | "Gile de Labargue" / "Sr de Gille Cabarque" | "147.46.146.87. / 232.66.45.204." | 147,46,146,87,232,66,45,204 |
| f61L | "on verra quelques personnes venue d'une procuration a Genes" | a passage about people coming to Genoa to treat/negotiate | (no adjacent single cipher run identified this pass -- longer insertion, not a name gloss) |
| f61L | "de l'Isle" (margin label; pass A misread it "de Sile", B's "l'Isle" is right -- checked directly against the image, native res, this worker) | "192.46.87.147.46.146. qui ont sceu les conferences ..." | 192,46,87,147,46,146 |
| f61L | "Labbe" (checked directly against the image: small, written right above "145.31.67.", underlined) | "... que j'avois eues avec 145.31.67. sur cette affaire" | 145,31,67 |
| f61L | "Labbe" / "l'abbé" (a third, separate recurrence later on f61L) | not re-checked against the image this pass | likely another "145.31.67."-style short reference, unconfirmed |
| f61R | "a la vente de cette isle" | "145.48.97.222.87.84.38.46.146." | 145,48,97,222,87,84,38,46,146 |

**145.31.67. = "l'abbé" [Lomeliny] is now confirmed at three separate points in letter 1**: the full 7-group
gloss on f60R ("Mr l'abbé Lomeliny" over "145.31.67.148.186.147.176."), and two short 3-group recurrences on
f61L, one of them ("...avec 145.31.67. sur cette affaire") re-glossed "Labbe" again and checked directly
against the image this pass (native resolution, not just a transcription pass's report) -- the clearest,
most repeated internal crib in this letter. "192.46.87.147.46.146." = "de l'Isle" (a name or place, not yet
identified) is a second, single-instance crib from the same direct check. Both are exactly the kind of
internal crib the "align known plaintext to key" pattern in LESSONS.md wants; not decoded this pass (out of
scope).

## Content summary (from both passes' context notes; full detail in passA_context.md / passB_context.md)

**Letter 1** (8 Apr 1714): Paget answers a letter of the 19th of the previous month; an "abbé Lomeliny/
Lomellini" writing from Venice; negotiations over a share ("une portion") and an island's sale ("la vente
de cette isle"); then, in plain French with no cipher at all (f62L-f64L), a long digression on Genoa/Italy
politics (the France-Empire peace and whether it covers the King of Sicily) and the death and succession
dispute of a rich Genoese banker, "le marquis Pallavicin[o]" (bastard son of Carlo Pallavicino); Paget's own
request to be sent his "expeditions" so he can take up the Sardinia consulate (referencing an April 1712
memoir on a consul's duties); closes naming the new vice-consul "Laugier de Toulon" (successor to "le Sr
Aubert[i]", 5 months in post).

**Letter 2** (28 Aug 1714): answers three letters of the 13th; the bulk of the letter (f65R-f66R, almost
solid cipher) is a formal physical and character portrait of "la Princesse de Parme et ses 2 oncles" --
both passes independently identify this as Elisabeth Farnese (matching birth year given in the text, "mil
six cens quatre vingt douze" = 1692; explicitly glossed "pour Reyne d'Espagne"/"reconnoit déjà pour Reyne
d'Espagne") -- consistent with her actual Sept 1714 proxy marriage to Philip V of Spain, about a month after
this letter. Covers her height, complexion, temperament, total submission to her mother the reigning
Duchess of Parma, the Farnese succession after the Duke's remarriage, and her uncles "le Prince Antoine [and
François] de Parme". Useful as a crib: the birth year and the "Reyne d'Espagne" phrase are exact, checkable
strings if a key is ever proposed.

Not verified against any printed source this pass (rule 10 -- report only, no novelty classification).

## Next

1. **Decode/key-recovery pass** (a solver session, not this worker): start from the confirmed cribs above --
   145=l'abbé-run first code (three independent occurrences), 192.46.87.147.46.146.="de l'Isle" -- and check
   whether the third "Labbe"/"l'abbé" recurrence on f61L and the other repeated short glosses (f60R's
   "Gile de Labargue"/"Sr de Gille Cabarque") pin the same or different code runs. Given 38 shared codes
   between the two letters, fit the key against both letters together, not letter 1 alone.
2. Re-derive f66L positions ~120-150 (the known reconciliation-artifact region above) from the image directly
   rather than trust `ciphertext.tsv`'s current alt-flagged rows there.
3. Old-series page-number identification (register search) from the earlier OX-PAG note is still open and
   unrelated to this pass's work.
4. A verifier has not looked at this target; nothing here is claimed as new/unpublished/first (rule 10).
5. Pass A flagged (passA_context.md) that several f66L cipher-group endings were recovered by reading a
   sliver of the same truncated line bleeding into f66R.jpg's own left margin (page-scan overlap) rather
   than from f66L directly -- worth a second look before trusting those specific digits. Also open: one
   uncertain word on f66L ("Rousse", conf M, clashes with "blonde" two words earlier -- may be misread);
   a likely scan-overlap duplicate between f61R's and f62R's opening lines (both transcribed literally,
   not deduplicated, per rule 2); and the old crossed-out pagination sequence (739/741/743/745/747 on the
   R images, then two readings on f65R/f66R that don't fit the expected +2 step -- at least one is
   probably misread).

## Cryptanalysis attempt 1 (25 September 2026, OX-PAGS)

**Result: negative for extending beyond the direct interlinear glosses, with a matched control. Status stays
partial.** One attempt per this session's brief; not retried.

### Cribs (from the glosses, re-checked directly against `images/f60R.jpg` and `images/f61L.jpg` at native
resolution, not taken on the transcription passes' word alone)

| Codes | Gloss (image-checked) | Occurrences | Grade |
|---|---|---|---|
| 145.31.67 | "Labbé"/"l'abbé" | f60R pos30-32 (as part of the 7-code group below); f61L pos104-106, glossed "Labbe" at pos110 | C (3 independent occurrences, same first/last code) |
| 145.65.67 | "Labbe" (fourth occurrence of the same word) | f61L pos146-148, glossed "Labbe" at pos152 | C for the word identity; **the middle code is 65, not 31** -- confirmed directly against `ciphertext.tsv` and independently by a fresh-instance subagent (see below). Same word, two different middle codes. |
| 148.186.147.176 | "Lomeliny" | f60R pos33-36, under a bracket in the manuscript grouping these 4 numbers specifically (image-confirmed) | C (single occurrence, but the manuscript's own bracket separates it cleanly from the "Labbé" codes before it) |
| 147.46.146.87 + 232.66.45.204 | a name, reading uncertain -- "Gile de"/"Isle de"/"Sile de" + "Labarque"/"Cabarque" (passes disagree; re-checked directly against `images/f60R.jpg`, still ambiguous at native resolution: the capital letter could be G, I or S) | f60R pos69-72 + 75-78, glossed "Gile de" at pos73 and "Labarque" (underlined) at pos86 | M (digits are H/agree in both passes and confirmed directly by me; the word itself is not resolved) |

Image method: cropped `f60R.jpg` (native 1700x2633) at 3-5x with Pillow (installed locally this session, no
network use) rather than trust the transcription passes' report for anything load-bearing; this caught the
145.65.67 variant (the transcription passes had already flagged it as an alt spelling of "Labbe" without
either pass or NOTES.md previously noting the *code* differs, only that the two passes' letter-spellings of
the gloss word itself differed).

### System hypothesis tested, and why it fails

Run-length arithmetic suggested a fixed "each code = one ~2-letter chunk of the plaintext, read left to
right" (bigram) rule: "Lomeliny" (8 letters) split cleanly into 4 codes (Lo-me-li-ny), which is the only one
of the four glossed groups whose letter-count divides evenly by 2. Under that rule, 148=Lo, 186=me,
**147=li**, 176=ny.

That rule is **falsified by two independent internal contradictions**, not merely unconfirmed:

1. **Code 147 takes two incompatible values.** The same code 147 opens the *other* glossed group
   (147.46.146.87), which the image confirms is a name beginning with a capital letter (G, I or S) --
   not "li" under any reading. 147 recurs twice more (f61L pos90, pos166) in runs the earlier transcription
   pass associated with "de l'Isle"/"la vente de cette isle," never in a position consistent with "li" either.
2. **The "Labbé" group is itself internally inconsistent.** The identical word, glossed identically ("Labbe")
   four times, is coded 145.31.67 twice and 145.65.67 once (the fourth occurrence, f61L pos146-148) -- first
   and last code agree, the middle does not. This eliminates any single fixed 3-code (or bigram) spelling for
   "Labbé" and instead points to genuine homophony (more than one valid code for whatever the middle position
   represents) rather than a bijective substitution table -- but homophony in one direction (many codes, one
   value) does not explain finding #1 (one code, two values), which a decipherable nomenclator should not have.

**Fresh-instance re-derivation** (a subagent given only `ciphertext.tsv`, the gloss list above and a one-
paragraph statement of the bigram hypothesis, no access to this session's own analysis) independently found
both contradictions unprompted, plus a third observation: codes 46 (~35-37 occurrences across both letters),
146 (~20) and 87 (~18) are far too frequent, and appear in long ungossed cipher runs throughout both letters
(including all of f65R/f66L/f66R, which carry no name-gloss at all), to be reserved letter-chunks specific to
"Labarque" or "Isle" -- consistent with OX-PAGT's original "common syllable/letter code" reading, but not
usable as a crib without an independent fix on what any one of them means. Conclusion: **"each number is a
fixed bigram" cannot be sustained as the system's rule from the cribs in hand; Lomeliny's clean 8/4 split
looks coincidental.** What kind of system it actually is (syllabic with true homophones, a mixed table of
whole-word and letter entries, or something else) is not established by this session.

### Matched control (rule 3)

`control_test.py` (this folder; deterministic, reproduces the numbers below on every run) builds a synthetic
French nomenclator of the **same shape** as the target -- ~500 coded tokens, ~117-122 distinct codes, one
8-letter name spelled by 4 clean bigram codes (mirroring "Lomeliny"), one 5-letter word spelled by 3 codes
(mirroring "l'abbé") -- but with a **true, self-consistent, built-by-construction bigram-per-code table** (no
homophony, no code reused for two values), embedded in a period-register French filler passage written for
this control. It then runs the identical procedure used on the real target: derive per-code values from the
two glossed groups, then check every other occurrence of those same 7 codes elsewhere in the control text for
consistency.

| | Target (real) | Control (synthetic, true bigram key) |
|---|---|---|
| Codes carrying a derived value from the glosses | 7 of 122 (5.7%) | 7 of 117 (6.0%) |
| Times a derived code recurred elsewhere and was checked | 2 (code 147 x1 cross-gloss; code 145/67 vs 65 within "Labbé") | 41 |
| Confirmations (value held) | 0 | 41 |
| Contradictions (value did not hold) | 2 | 0 |
| Tokens correctly readable via the derived codes | 13 of 500 (2.6%, the glossed spans only) | 41 of 503 (8.2%, glosses plus free extension) |

On a control of the same design where the bigram hypothesis is actually true, the identical crib-extraction
procedure extends for free to 8.2% of tokens with zero contradictions. On the real target, the same procedure
does not extend at all and produces two contradictions on the only two cross-checks available. This is a
design fact about Paget's cipher (rule 3's control), not evidence the procedure itself is broken.

### Forced-context extension (brief step 1c)

Checked whether any of the letter's substantively identifiable names/places sit in a "forced" clear-French
slot that would pin an unglossed code: **Pallavicino, Sardaigne, Aubert, Laugier, Toulon, Parme, Farnese and
d'Espagne are all already in clear text** in `ciphertext.tsv` (grep-checked), not coded. The coded spans are
specifically the content with no clear-text parallel elsewhere in the letter -- which removes the main source
of single-word contextual forcing (there is no known name already stated in clear next to an unglossed code
run to anchor it against). No code was forced this session; none is graded S.

### No key.tsv produced

Every attempt to decompose the two confirmed multi-code glosses into individual per-code values failed
internal cross-validation (above), so there is no validated single-code substitution to write into a
`decode.json`/`key.tsv` that `tools/decode_key.py` could apply -- doing so would assert per-token values this
session cannot defend (rule 4). The table above is the full extent of what is established; `ciphertext.tsv`
itself (unresolved codes as bare numbers) is the only defensible "reading." No `specs/clairambault1225-paget-1714.json`
exists, so `tools/judge_plaintext.py` was not run, and none was written (brief: do not write a spec).

### What stays unread

115 of 122 distinct codes (94.3%), 487 of 500 coded tokens (97.4%) in both letters. No novelty wording (rule
10) -- report only. A verifier has not looked at this target.

## Sibling and key search (25 September 2026, OX-PAGK)

**Result: Paget identified with two independent printed sources; recipient inferred, not confirmed; no
copy-free deciphered sibling or nomenclator table found; the one live archival lead (AN Marine B7) is not
reachable from this environment -- written up as a REQUEST.md-class next step, not attempted further.**
Cryptanalysis is still not the recommended next step (OX-PAGS's negative with control stands); this session
did not decode anything and reports identification/search results only (rule 10: no novelty wording below).

### Who Paget is (grade C -- printed sources, not yet checked against the manuscript itself)

**Pierre Paget.** Two independent printed sources agree and cross-confirm:

1. Anne Mézin, *Les consuls de France au siecle des lumieres (1715-1792)* (Peter Lang, 1998), entry "PAGET
   (Pierre)" (found via Google Books full-text search, snippet only, page number not visible in the snippet):
   "chevalier de l'ordre de Saint-Lazare et de Notre-Dame du Mont-Carmel avant 1731... [a] Genes jusqu'en 1714.
   Il est charge de l'interim du consulat pendant une absence du consul Aubert (voir notice)." -- i.e. Paget
   held no consular title of his own at Genoa; he stood in for the sitting consul, Aubert, during an absence,
   until 1714.
2. Jorg Ulbert, "L'origine geographique des consuls francais sous Louis XIV," *Cahiers de la Mediterranee* 98
   (2019) (read via WebFetch, journals.openedition.org/cdlm/11218), the article's consul-by-post table:
   - *Genes (consulat)*: "...1681-1699 Jean-Baptiste Aubert (Prov.); 1699-1723 Joseph-Marie Aubert (Prov.)."
     -- confirms "Aubert," the sitting consul at Genoa across our letters' whole date range, and matches
     Letter 1's own "le Sr Aubert[i], 5 months in post" mention (NOTES.md, Content summary, above) as almost
     certainly the same Joseph-Marie Aubert, consul 1699-1723 (a vice-consul's separate, shorter posting, not
     the consulship itself -- the letter's own "5 months in post" cannot be Aubert's 24-year consulship;
     re-read that passage as being about a different, junior vice-consular post at Genoa that changed hands
     twice in 1714, first to a "Sr Aubert[i]" then to "Laugier de Toulon," not about the consul Aubert
     himself).
   - *Cagliari (consulat)*: "...1692-1708 Henry Meritan (o.i.); 1714-1749 Pierre Paget (a.F.)." -- Paget
     becomes consul at Cagliari (Sardaigne) in exactly 1714, the year of both our letters, matching Letter 1's
     own request that Monseigneur send his "expeditions" so he can take up "le consulat de la nation en
     Sardaigne... destine" (a request he had apparently been pursuing since an April 1712 memoire, per this
     folder's existing Content summary section).

3. Corroborating archival citations, from Google Books full-text search over the Archives nationales' own
   printed series *Inventaire des archives de la marine* (Impr. nationale, 1964-1980; sous-serie **Marine
   B7**, the Secretary of State for the Navy's received/sent correspondence register -- see "Recipient"
   below) and one secondary history, all via `googleapis.com/books` with `GOOGLE_BOOKS_KEY` and `country=US`,
   snippets only (no page opened in full view):
   - *Inventaire des archives de la marine: Articles 1 a 20* (1964), an entry dated "2 decembre 1713. Le s.
     Paget... (Genes)" -- Paget already writing from Genoa by December 1713, register B7 20 (this volume's
     last "article").
   - *Inventaire des archives de la marine: Articles 21 a 47* (1964): one entry (date read from the snippet as
     "27 mars 1714", see caveat below) "Le s. Paget (Genes): reaction en Italie apres la paix de Rastadt; il
     demande le consulat de Sardaigne" -- content matching Letter 1 (8 Apr 1714)'s own Rastatt-peace
     discussion and Sardaigne-consulate request almost word for word; and a later entry, in an April-August
     1716 run keyed to "(B7 29)", "...Paget (Cagliari): il a achete quatre esclaves pour les galeres..." --
     Paget already installed and acting as consul at Cagliari by mid-1716, consistent with the 1714 start
     date above.
   - *Inventaire des archives de la marine: Articles 64 a 75* (1966), an entry keyed to "(B7 70)": "...Paget,
     vice-consul a Genes: nouvelles a transmettre en l'absence du s[r. Aubert]..." -- explicitly gives Paget's
     own title as **vice-consul** at Genoa, standing in during Aubert's absence, matching Mezin's "interim"
     note above word for word. (B7 70 is chronologically much later than our two letters -- this volume's
     range was not established this session -- so this is evidence of Paget's standing role over a run of
     years, not a register entry for either of our two specific letters.)
   - Georges Coulon [uncredited in the snippet; title only] / *Histoire des etablissements et du commerce
     francais dans l'Afrique barbaresque (1560-1793)* (1903): lists "Paget, agent a Cagliari" alongside
     "David, agent a Genes pour l'entrepot et la vente du corail," citing "Arch. nat. marine, B7" as the
     source -- a third, independent secondary-literature confirmation of Paget's post at Cagliari, with the
     same archival series.

   **Caveat on the "27 mars 1714" date.** Read only from a Google Books search-result snippet (no page image
   opened), so the date itself is not independently confirmed and could be a snippet-boundary misread; it
   precedes Letter 1's own "8e Avril 1714" dateline by about a fortnight, so this register entry is either (a)
   the same letter, registered/logged under an earlier date than its own dateline (transit-time or clerical
   date could differ), (b) an earlier, closely related letter on the same topic that is not one of our two
   Gallica items, or (c) a misread. Not resolved this session -- flagged for whoever can open the actual page
   (Google Books preview, or the volume in a library).

**Conclusion on identity: established beyond reasonable doubt that "Paget" is Pierre Paget, vice-consul (not
consul) at Genoa under consul Joseph-Marie Aubert until 1714, then consul at Cagliari (Sardaigne) 1714-1749** --
three independent printed sources (Mezin's dictionary, Ulbert's article, and the Archives nationales' own
printed *Inventaire* of the Marine B7 register) converge on the same person, post, dates and even the specific
"consulat de Sardaigne" request that Letter 1 itself makes in clear French. Grade C (from named printed
sources, not yet checked against the manuscript or against each other's primary citations) rather than H;
none of this required opening the ciphertext.

### Recipient ("Monseigneur") -- inferred, not confirmed

**Most likely Jerome Phelypeaux, comte de Pontchartrain, Secretaire d'Etat de la Marine (in office
1699-1715).** Consular correspondence for the Mediterranean/Levant network ran through the Secretary of
State for the Navy in this period (the "systeme Pontchartrain," Ulbert's own term for it, surfaced in a
WebSearch snippet on Pontchartrain's consular administration), and -- decisively -- Paget's letters are
indexed in the Marine ministry's own correspondence register (*Inventaire des archives de la marine*, sous-serie
B7, above), which only holds correspondence received by or sent from that Secretary of State's office. No
document naming Pontchartrain (or any other named recipient) for these two specific letters was read this
session; this is an inference from the holding series and the period's known administrative structure, not a
read of an address or a signature. Grade I. A fresh check of the letters' own salutation/address (if any
survives beyond "Monseigneur") against Pontchartrain's known hand or seal would upgrade this; not attempted
(would need the manuscript image, already on disk in `images/`, not re-examined this session -- out of this
session's brief, which was archival/printed search, not image re-inspection).

### Sibling / decipherment / nomenclator search -- negative this session, one live lead not reachable

- **Gallica** (`gallica.bnf.fr`): one SRU query, `"Paget" "Genes" "chiffre"` -- Gallica's `all` operator does
  an OR-style relevance search, not an AND of exact phrases (373,295 "hits," the top one an unrelated 1926
  press photograph of a different Paget, a golfer). Not a useful search as written; a future worker should
  use `gallica adj "chiffre de Paget"`-style adjacency/phrase clauses or the ContentSearch API scoped to a
  specific ark, not a bare cross-corpus SRU query. Combined with OX-PAGT's collection-wide check ("no second
  Paget item found" in the BnF finding aid's own name index, 25 Sept, cited above in this file) and the 23
  Sept check-solved sweep (DECODE, Bourdeau, Aymeloglu, cryptiana: no hit for "Paget" or "Clairambault 1225"),
  no second cipher exemplar or decipherment copy is known on Gallica or in the collections already swept.
- **BnF Archives et manuscrits** (`archivesetmanuscrits.bnf.fr`): not re-queried this session (OX-PAGT's pass
  already covered the Clairambault fonds' own name index).
- **FranceArchives** (`francearchives.gouv.fr`): the one finding-aid page fetched ("Affaires etrangeres.
  Correspondance consulaire; consulats") returned empty content to WebFetch (client-rendered page, not
  fetchable this way); not retried with the browser tool (out of scope for a plain-fetch/search pass at this
  cap).
- **Archives nationales / archivesdiplomatiques.diplomatie.gouv.fr**: `archivesnationales.culture.gouv.fr` --
  the host serving the AE/B/I and AE/B/III printed inventory PDFs (`AE_BI.pdf`, `AEBIII.pdf`) -- is
  **unreachable from this environment**: `curl` returns `Could not resolve host` on plain HTTP and the agent
  proxy returns `CONNECT tunnel failed, response 502` / "connect_rejected (organization policy)" on HTTPS,
  confirmed by the reachability test this session (`000`-equivalent, per CLAUDE.md's "Access playbook" test).
  Logged here and not retried, per the good-citizen rule. One PDF from `archivesdiplomatiques.diplomatie.gouv.fr`
  (a different, reachable host) was fetched but WebFetch could not extract text from it (raw PDF stream, not
  OCR'd for this tool); not pursued further with a local PDF-text extractor (no `pdftotext` installed, out of
  proportion for this cap).
- **No printed edition, nomenclator table, or "chiffre de M. Paget"/"chiffre pour Genes" was found** in any
  source searched this session (Google Books queries above, WebSearch queries on Pontchartrain/consuls/Genoa
  cipher terms). The 1903 Afrique-barbaresque history and the *Inventaire* volumes cite AN Marine B7 as an
  archival source, never reproduce or transcribe Paget's letters.

### The one live lead: AN Marine, sous-serie B7

Paget's original letters to the Secretariat of State for the Navy are catalogued within **Archives
nationales, Marine, sous-serie B7** (Correspondance recue par le secretaire d'Etat de la Marine), somewhere in
the volumes ("articles") the printed *Inventaire* numbers in the low-to-mid 20s for the 1713-1716 span (B7 20
still in December 1713; an April-1714-dated entry sits within "Articles 21 a 47"; B7 29 reaches August 1716) --
the exact article number for April and August 1714 specifically is **not pinned down this session** (would
need the actual volume, not just Google Books' snippet-level search, to see the full run of dates within each
article). If the Secretariat's cabinet du chiffre decoded Paget's coded passages on receipt in 1714 (as the
BnF Clairambault 1225 copy's own interlinear glosses in Letter 1 suggest someone did, at least partially, for
some passages -- see the "Interlinear glosses" table above), the AN Marine B7 original could carry either (a)
more/different interlinear decipherment than survives on the Clairambault copy, or (b) a separate loose
"dechiffrement" sheet filed with it -- either of which is exactly the "sibling with a contemporary
decipherment" LESSONS.md recommends looking for, and would settle far more of the 115 still-unread codes than
another cryptanalysis attempt. This is not digitised or online anywhere found this session (no Gallica IIIF,
no francearchives item-level record, no other digitisation project hit) and the AN's own online description
of the series is unreachable from this environment (above). **This is a REQUEST.md-class next step**: a
future access worker or the person would need to identify the exact article number (from the physical
inventory volumes, or from the AN's own online catalogue reached from an unrestricted network) and request or
photograph AN Marine B7, article ~21-29 (Genes/Paget correspondence, 1714), at Pierrefitte-sur-Seine. Not
written as a formal REQUEST.md entry yet (the article number is not narrow enough to make a useful request;
narrowing it needs one more search pass with the actual AN catalogue, not blocked on the person).

### What was not attempted this session

- Re-inspecting the manuscript images for the letters' own address/salutation beyond "Monseigneur" (would
  support or rule out the Pontchartrain inference) -- out of this session's brief (archival/printed search).
- Opening any Google Books result beyond the search snippet (would need a full-view/public-domain volume and
  a specific page number, neither established this session for the *Inventaire de la marine* volumes, which
  are library-search-only previews).
- A browser-tool fetch of the FranceArchives finding aid (its content is JS-rendered; plain WebFetch returned
  nothing).
- OpenAlex/Persee/HAL scholarship search specifically for "Paget" + "Genes"/"Cagliari" consul (the two
  sources found, Ulbert 2019 and Mezin 1998, came from ordinary web search and Google Books, not the
  open-index APIs); a next pass could check whether either is discussed further or corrected in later
  scholarship.

### Requests (this session)

`journals.openedition.org` 1 (WebFetch); `archivesdiplomatiques.diplomatie.gouv.fr` 1 (WebFetch, PDF,
unreadable by the tool); `francearchives.gouv.fr` 1 (WebFetch, empty/JS-rendered); `gallica.bnf.fr` 1 (one SRU
query, unhelpful as written -- logged above); `googleapis.com/books` 9 (search + volume-metadata calls,
`GOOGLE_BOOKS_KEY`+`country=US`, all sequential, well over 1.5s apart); `archivesnationales.culture.gouv.fr`
1 reachability test (blocked, not retried, logged above). WebSearch: 6 queries (no host/rate rules apply to
this tool). No Gallica image/IIIF fetches this session (no "Gallica slot" claim needed).

## NX-UNBLOCK (26 Sept 2026)

Tried the one materially different route this row's own text names as blocking ("the AN's own online catalogue
reached from an unrestricted network"): the AN's Salle de lecture virtuelle (SIV, `siv.archives-nationales.culture.gouv.fr`)
is now reachable from this environment (HTTP 200 landing page, `www.france-archives.fr` still 502s and plain
`francearchives.gouv.fr` still returns an empty JS shell -- unchanged from the earlier session's finding, but
SIV itself is a separate host and answers). Its simple-search action
(`/siv/rechercheconsultation/recherche/recherchesimple/rechercheSimple.action`) needs session state this pass's
one attempt did not reproduce (HTTP 500 on a bare `motRecherche=` GET with a fresh cookie jar) -- not retried
per the good-citizen single-retry rule. This is progress (the host itself is not blocked, unlike francearchives),
but the article number for AN Marine B7's April/August 1714 Genes/Paget correspondence is still not pinned down.
Next step for a future worker: reproduce SIV's search form properly (likely needs the landing page's own
jsessionid carried through, and possibly a POST rather than GET, the CalmView/Lambeth pattern already solved
for a different host in CLAUDE.md's Access playbook) before this becomes a narrow enough REQUEST.md target.

## While waiting (27 Sept 2026, WAIT-PASS-A)

Waits on pinning the AN Marine B7 article number (~21-29) via the SIV catalogue's search form, since 26 Sept
2026 (NX-UNBLOCK: host reachable, search form not yet reproduced).

- Reproduce SIV's search form (carry the jsessionid, try POST not GET, the CalmView/Lambeth pattern) -- the host answers, only the form is unsolved. M.
- Run the open-index scholarship pass (OpenAlex, Semantic Scholar, Persée, HAL) for "Paget" + "Genes"/"Cagliari" consul, flagged in NOTES as not yet tried beyond ordinary web/Google Books search. S, tools/print_check.py.
- Re-fetch the AAE PDF (archivesdiplomatiques.diplomatie.gouv.fr) through the browser tool/OCR rather than the raw WebFetch that returned it unreadable. S.

## Gloss alignment (2 Oct 2026, NEXT-PAG)

Ran the Verdict line's cheapest next step: tools/interlinear_align.py on (cipher run, gloss) pairs from both letters.
Files: `align/build_pairs.py` -> `align/pairs.tsv`; `align/evaluate.py` (train, held-out check, shuffle control,
full run) -> `align/align_{train,all}.tsv`, `align/key_{train,all}.tsv`, `align/eval_run.txt`, `align/grid.txt`;
`align/make_key.py [--check]` -> `key.tsv`. Every script regenerates its output from ciphertext.tsv and pairs.tsv.

**Pairs come from the page images, not from ciphertext.tsv's insertion-clear rows (rule 2).** Building the pairs
showed that ciphertext.tsv's kinds cannot be used as they stand. I looked at `images/f60R, f61L, f61R, f65L, f65R,
f66L, f66R.jpg` (the seven page-halves that carry cipher; whole-page or half-page crops, read by me, no subagent).
On every one, the period decipherment is written on the line above each cipher run, and in letter 2 it covers almost
every run. Both transcription passes recorded many of those above-line decipherments as running clear text, so
ciphertext.tsv kinds them `clear`. Examples: f66R "quoyque ce Dernier Duc n'ait que 36" over 77.87...204.36; "Il n'est pas marie et n'a" over
41.96...174; "sont charmés de la voir epouser" over 46.205...194; "une grande Partialité" over 48.175...233; f60R
"Venise" over 244.176.221. Other passes attached a gloss to the wrong line: passA gives f66R 33-43 "frere du Duc..."
where the image has "le Prince Antoine de Parme". Result: **501 of 505 cipher tokens (both letters) sit under a
period gloss.** The only run with no gloss is f66L 169-172 `400 4 19 600` ("une complaisance aveugle pour ...").
The previous "about 109 unglossed tokens" was a transcription artifact. Gloss attachment is one reader's reading
(mine), not two blind passes. The image-check gap below now covers a second, independent read.

**Two readings corrected by the image.** (1) f60R pos69-72 `147.46.146.87` is glossed "Lisle de" (l'Isle de), not
"Gile/Sile de". f61L has the same word twice, "de Lysle" over 192.46.87.147.46.146 and "Lysle" over 34.147.46.146.
So code 147 opens "li" in "Lomeliny" (148.186.147.176) and in "l'Isle" alike. OX-PAGS's contradiction 1 (147 taking
two values) came from the misread gloss, not from the cipher. (2) Contradiction 2 (l'abbé as 145.31.67 and 145.65.67,
plus 56.31.67 at f61L 199) stays as it was: the cipher has homophones.

Digit overrides (image over ciphertext.tsv, listed per pair in pairs.tsv `overrides`): f66L 51 95->97, f66L 125
35->33, f66L 189 20->220, f66R 59 52->32, f66R 61 154->174. Cipher numerals that repeat the gloss's own numeral were
passed as clear numerals, grade I: f65R 55 `2` ("ses 2 oncles"), f66L `22`/`25` ("22e annee le 25 Octobre"), f66L 290
`2` ("2e Nopces"), f66L 371 `44` ("agee de 44 ans"), f66R 23 `36`, f66R 63 `35`. The illegible group at f61L ~48 went
in as a doubtful token. It can take a chunk but never enters the key.

**Tool change (Usage 8: an option, not a private copy).** At the brief's settings (`--floor 1`, Thurloe defaults), the
alignment barely beat its control. Training self-agreement was 83/473 = 0.175, against a shuffled-pairing p95 of 0.184
(20 seeds). Held-out letters were 12/37 = 0.324, against a shuffle p95 of 0.324. The Thurloe scoring lets a code take
up to 14 letters and gives +1 for each word boundary, so from a flat start one code swallows a whole gloss word. This
cipher is syllabic, about two letters per code, and its chunks do not follow word boundaries. I added `--max-chunk`,
`--seg-bonus` and `--len-prior` to tools/interlinear_align.py. Its defaults are unchanged, and the existing offline
test still passes. A new offline case shows the syllabic toy recovering with the options and not under the defaults.
I chose the settings on training data only: 24-setting grid, 10 shuffle seeds each, ranked by margin of training
self-agreement over shuffle p95 (`align/grid.txt`). The pick was null-cost -3, max-chunk 4, seg-bonus 0.5, len-prior
0.5. The held-out pairs were scored once, after that choice.

**Result, with its controls (rule 3; the manipulation, the pairing, is what both statistics depend on).**

| | real pairing | shuffled pairing (20 seeds) |
|---|---|---|
| training self-agreement (aligned code tokens whose chunk equals the code's top value, n>=2) | 131/473 = 0.277 | mean 0.103, p95 0.126 |
| held-out known-answer letters (P10/P12/P14 l'abbé, P39 f66R 'le Prince Antoine de Parme') | 24/37 = 0.649 | mean 0.270, p95 0.378 |

Held-out spellings from the training key: 145.31.67 -> la.?.be (4/5 letters), 145.65.67 -> la.?.be (4/5),
56.31.67 -> l.el.be (3/5), P39 -> le.in.l.d.le.a.ne.de.p.me.s (13/22). Caveat: code 67's value 'be' comes from P01
("Labbe Lomeliny", training), which also contains l'abbé. The brief named the l'abbé pairs for hold-out; P01 holds the
name as well, so the l'abbé part of the check is not fully independent. In P39, the 'de Parme' run 87.201.156 spells
de.p.me: 87=de and 156=me hold, while 201 takes only 'p' (its 'ar' is lost).

**Key (rule 4).** `key.tsv`: 21 codes whose top chunk agrees in >=2 aligned occurrences and covers >=50% of them. 12 are
graded C (>=3 agreeing occurrences): 52 et, 67 be, 87 de, 147 li, 155 ma, 185 on, 196 po, 212 re, 221 se, 240 ion, 244
ve. Nine are graded M (2 agreeing): 77 q, 84 ce, 86 da, 116 g, 126 ch, 135 je, 158 mo, 174 na, 205 qui, 213 ma. All
meanings come from the period gloss; nothing is cryptanalytic. The full run (all 56 pairs) gives self-agreement 138/493
= 0.280. Per token over the 493 aligned code tokens: 53 agree with a C code, 20 with an M code, 45 sit on a key code
with a different chunk, and 375 sit on codes outside key.tsv. Frequent codes stay unsettled: 46 (37 occurrences, top
's' 9/37), 146 (20, 'le' 8/20), 145 (12, 'la' 4/12), 175 (16, 'ne' 5/16). Either these are true homophones or nulls, or
the gloss's own spelling drifts. One example of the drift: the f66R gloss "frere du Duc de Parme qui n'a que 35 ans
Mais" has no 87.201.156 under it, so the decipherer added "de Parme" for clarity. At the run level, the plaintext of
both letters' cipher passages is the period decipherment written above them (pairs.tsv `plain_raw`, one reader).
Code-level values for most codes are not established.

Not run: tools/decode_key.py (no decode.json yet; that is the retry step) and tools/judge_plaintext.py (no spec for
this target). Rule 10: nothing here is described beyond "read from the period interlinear decipherment". No
request to any outside host: the images were already on disk. Subagents: none.

## Decode script (2 Oct 2026, NEXT2-PAG)

`decode.json` + `python3 tools/decode_key.py ciphers/clairambault1225-paget-1714` regenerate `reading.txt` and
`reading_tokens.tsv` from ciphertext.tsv + key.tsv + exceptions.tsv + votes.tsv; `--check` exits 0 ("reading up to date").
`align/build_votes.py [--check]` regenerates votes.tsv (493 rows: the gloss chunk the alignment puts over each aligned
code token, located by pairs.tsv `positions`) and exceptions.tsv (12 rows: the five image digit overrides and the seven
cipher numerals that repeat the gloss's own numeral). Tool change (Usage 8, an option not a private copy):
tools/decode_key.py's tsv loader gained `conf_column`, `kind_column`/`sign_kinds` and accepts a header whose line column
is not the first cell; offline case tools/tests/decode_configs/clairambault1225-paget-1714.json passes. The same test
file's antt-linhares-chave and rah-canada-1869 cases fail with and without this change (checked by stashing it):
pre-existing config drift, not touched here.

Per-token grades (rule 4), 505 cipher tokens (kinds `cipher` and `cipher/insertion-clear`):

| grade | tokens | meaning here |
|---|---|---|
| H | 0 | no key sheet or period key table for this cipher |
| C | 71 | key.tsv value equals the period-gloss chunk aligned over this token (known plaintext) |
| S | 0 | nothing cryptanalytic |
| M | 47 | key value with a disagreeing aligned chunk (44), key value agreeing with the chunk but on a digit the transcription grades M (2), the f66R 61 image override 174 'na' (1) |
| I | 7 | cipher numerals repeating the gloss's own numeral (f65R 55, f66L 25/31/290/371, f66R 23/63) |
| U | 380 | code not in key.tsv (incl. the ILLEGIBLE group at f61L 48 and the four image overrides to unkeyed codes 97, 33, 220, 32) |

Firm (H+C+S) at token level: 71 of 505. Separately, the **run level**: 501 of 505 cipher tokens sit under the period
interlinear decipherment written above them (align/pairs.tsv `plain_raw`, one reader of the images, NEXT-PAG). That text is
read from the period's own decipherment, so the run-level plaintext of those 501 tokens is period-read (H at run level);
the key alone reads 71 tokens firmly and 47 doubtfully. The four tokens with neither are f66L 169-172 `400 4 19 600`.

`--split-check` (pasted): `split-check ciphertext.tsv: 505 signs; key range 52-244 (11 confident numeric codes); 103 flagged
tokens (387 occurrences), 0 with a candidate split`. All 103 flagged types are unkeyed (codes outside key.tsv's 21); 16 are
also out of the confident numeric range (e.g. 31, 35, 36, 44, 45, 46, 249, 267, and the unglossed 400 4 19 600). No digit
string cuts into two or three confident key codes, so the check offers no glued-digit candidate; with a 21-code key that is
expected and says nothing about the 5 image overrides, which the image already settled.

Judge: not run -- no `specs/clairambault1225-paget-1714.json` exists. Rule 10: readings described only as "read from the
period interlinear decipherment" and "key value agreeing with the aligned gloss".

## Key entries from the period glosses (PAGET-KEY, 2 Oct 2026)

Brief step 2: turn the period interlinear glosses into key entries, per-letter control first.
**Per-letter controls (align/per_letter.py -> align/per_letter.txt; NEXT-PAG's settings, fixed before this run: null-cost -3,
max-chunk 4, seg-bonus 0.5, len-prior 0.5; 20 shuffle seeds; the shuffle permutes the cipher/gloss pairing, which both
statistics depend on, so the control can fail differently from the real run).**

| letter | pairs | own self-agreement (real / shuffle mean / p95) | cross: key from the other letter, gloss letters recovered (real / shuffle mean / p95) | gate |
|---|---|---|---|---|
| L1, 8 Apr 1714 (f60R f61L f61R f65L) | 17 | 31/96 = 0.323 / 0.052 / 0.084 | 88/194 = 0.454 / 0.225 / 0.258 | PASS |
| L2, 28 Aug 1714 (f65R f66L f66R) | 39 | 82/397 = 0.207 / 0.102 / 0.133 | 283/829 = 0.341 / 0.184 / 0.229 | PASS |

Both letters clear both gates, so neither is held (the Szembek per-unit lesson): their glosses merge into one key.
**Key (align/make_key.py, regenerated; key.tsv 114 codes).** The 21 stable codes keep NEXT-PAG's values; 11 with >=3
agreeing occurrences are key-row H, 10 with exactly 2 are key-row C. The notes now give agreeing occurrences per letter
(e.g. 221 se L1 3 / L2 5; 147 li L1 2 / L2 2; 67 be L1 4 / L2 0). The other 93 codes are added at M, value = the gloss
chunk the alignment puts over them, tagged "single attestation" (39) or "unsettled" (54, top chunk under 50%: 46, 145,
146, 175 and others); decode.json's m_words keeps every token of these at M.
**Per-token grades (tools/decode_key.py --check, exit 0; decode.json voted_grade H, disagree_grade M, unvoted_grade C).**
H = the token's own aligned gloss chunk equals the key value, i.e. the period decipherment written over that very group
agrees with the value the code holds in >=2 aligned occurrences; C = keyed token with no aligned chunk of its own (none
arise: 493 of 505 tokens carry one); M = own chunk disagrees, or single/unsettled code, or uncertain digit.

| grade | tokens |
|---|---|
| H | 71 |
| C | 0 |
| S | 0 |
| M | 422 |
| I | 7 |
| U | 5 (f66L 169-172 '400 4 19 600', unglossed; the illegible group at f61L ~48) |

Firm (H+C+S) 71 of 505, unchanged in number from NEXT2-PAG's C 71: the same tokens, regraded from C to H because the
gloss over each is the period's own decipherment of that group (CLAUDE.md rule 4's AX2-172 usage). U drops from 380 to 5
because every glossed code now has an M entry. The code-to-chunk segmentation is the alignment's, not the decipherer's,
so H rests on the alignment's chunking, validated only to the per-letter levels above (self-agreement 0.21-0.32).
Tool change (Usage 8, an option): tools/decode_key.py gains `disagree_grade` (a vote that does not match; unvoted_grade
then covers only signs with no vote); tools/tests/decode_configs/clairambault1225-paget-1714.json updated and passes
(the antt-linhares-chave and rah-canada-1869 failures in the same test file are the pre-existing drift NEXT2-PAG logged).
Judge not run (no spec). Rule 10: readings described only as read from the period interlinear decipherment.

## Print step (A2-PAG, 2 Oct 2026)

Intake gate first (pasted): `clairambault1225-paget-1714: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`, exit 0.
Ran the Verdict's cheapest next step: the open-index pass and tools/print_check.py on the period-gloss phrases. A search log
for the solver side, not a novelty verdict (rule 10).
- `phrases.txt`: 16 phrases from align/pairs.tsv `plain_raw` (one reader's gloss read, NEXT-PAG), e.g. "la Princesse de Parme et
  ses 2 oncles", "le Prince Antoine de Parme", "Elle achevera sa 22e annee le 25 Octobre prochain", "a toujours este de genie
  Allemand", "on verra quelques personnes a Genes", "Labbe Lomeliny". `sources.tsv`: 3 OpenAlex and 2 CrossRef keyword rows
  (Paget + consul + Genes/Cagliari, Elisabeth Farnese 1714 marriage + consul Genes).
- `python3 tools/print_check.py ciphers/clairambault1225-paget-1714 --max-requests 150 --delay 1.6` -> print-check.tsv (75 rows),
  print-check-hosts.tsv. **IA full text (ia-global, 16 exact-phrase queries): 15 no hits**; "le Prince Antoine de Parme" 12 items, all
  general histories / Comedie-Italienne volumes naming Antonio Farnese, none a Paget letter. **OpenAlex: no phrase hit**; keyword rows 3 and 1
  works, none relevant (a 2026 Dix-huitieme siecle article on Compagnie colonisation projects, unrelated). **Google Books**: the phrase rows
  report 2-352 volumes because the API does not enforce the quotes; the listed titles (Saint-Simon, Dictionnaire de Bayle, Moreri, Revue des
  deux mondes...) are word-overlap noise. CrossRef: 1 query answered (noise), then 429. Semantic Scholar: 1 query answered (117 loose
  hits, none this letter), then 429 for the other 18 rows.
- Follow-up by hand (Google Books API with `country=US`, 7 queries reading `searchInfo.textSnippet`): `"Paget" "Gênes" 1714 Parme
  princesse` and `"Paget" "princesse de Parme" 1714` hit only the Inventaire des archives de la marine (1964; GssZAAAAYAAJ / XcsqAQAAMAAJ):
  register summaries, "Paget (Gênes) : le s. Saint-Hilaire est à Vienne ; le s. Santini, dit ... Parme à propos du mariage de la
  princesse de Parme. F° 265", the entries OX-PAGK already logged (no transcription of the cipher passages). `"Paget" Lomellini Gênes 1714`
  hit P. Masson, Histoire des établissements et du commerce français dans l'Afrique barbaresque (1903), a footnote "Paget à Gênes" in a
  Tunis/Concessions context, not these letters. `"genie allemand" duchesse Parme` hit Saint-Simon's Mémoires: "ses tantes, et sœurs
  de ces deux princes Farnèse, et qui ne sont pas plus de génie allemand que leurs dits frères" -- Saint-Simon's own text on the
  same marriage, a parallel phrase, not a print of Paget's letter (worth a note for a verifier: the phrase "génie allemand" for the
  Farnese circulated at the French court). `"Paget" consul Gênes Farnèse`, `"Paget" Courcy "paix d'Utrecht"`: 0.
- HAL API (`api.archives-ouvertes.fr/search`): `Paget AND consul AND (Gênes OR Genes OR Cagliari)` 0; `"princesse de Parme" AND 1714 AND
  consul` 0. Persée site search (`Paget Gênes consul 1714`, `Paget vice-consul Cagliari`): OR-matched result lists (331,728 and 145,303),
  top hits unrelated (medieval Genoese consuls, Seville 1873); no Paget article.
- Semantic Scholar single retry after a 20 s pause (`Paget consul Genoa 1714`, keyed): HTTP 200, 1 result, Hanna/Ottoman World 1660-1760
  survey, not this letter.
Result: no printed or online text of either letter's ciphered passages, and no decipherment of them, located by these methods on
2 Oct 2026 (a search result, rule 10). Not covered: JSTOR (owner-side; no row written, since the print step's brief named only the
open-index pass), Gallica full-text beyond RIDA XIX. Requests: be-api.us.archive.org 16, www.googleapis.com 16 (tool) + 12 (by hand,
5 of them a malformed loop whose output was discarded), api.openalex.org 19, api.semanticscholar.org 3, api.crossref.org 2,
api.archives-ouvertes.fr 2, www.persee.fr 2. Subagents 0, vision calls 0.

## Image check, blind line-crop passes (A2-PAG2, 2 Oct 2026)

Intake gate first (pasted): `clairambault1225-paget-1714: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`, exit 0.
Ran the Verdict's cheapest next step: the image-check blind passes and the key rebuild. Nothing else.
- **Crops (Usage 6, pasted command):** `python3 ../../tools/iiif_lines.py --image images/<half>.jpg --out images/lines --prefix <half> --distance 60
  --prominence 60 --lines-per-crop 2 --top-margin 90 --debug` on f60R f61L f61R f65L f65R f66L f66R -> 81 crops (8/11/13/12/6/11/12),
  each about 1700 x 250 px, two text lines plus 90 px above so every interlinear gloss sits in the crop with its run (crop boxes in
  `images/lines/manifest.json`; the crops and debug overlays are not committed, since they would take images/ over 30 MB --
  `imgcheck/regen_crops.sh` re-cuts them from the page-halves on disk). No network request: the page-halves were on disk.
- **Passes:** 14 blind Sonnet subagent calls, 2 per page-half (A, B), each given only its page's line crops and told to read no repo
  file; each wrote `imgcheck/pass{A,B}_<half>.tsv` (run, crop, words before, cipher groups, gloss written above, "?" on doubtful digits).
  Reconciliation: `imgcheck/compare.py` (aligns each pass's groups to ciphertext.tsv + pairs.tsv overrides per page, writes
  `imgcheck/digits.tsv` and `imgcheck/glosses.tsv`), then this worker's own look at the line crops for every disagreement (the 15th unit).
- **Digits, before this step's corrections (505 cipher tokens):** both blind passes equal the current reading on 472; both agree with
  each other against it on 12; the passes split on 3; 18 not reached by either pass. The 18 are all f66L line ends (e.g. f66L 13 `220`,
  39-40 `32 125`, 53-54 `39 692`, 124-125 `72 33`, 172 `600`): images/f66L.jpg stops at the gutter and those groups exist only in the
  left 220 px of images/f66R.jpg, which the f66R passes were told to ignore as the facing page. A crop-coverage gap, not a reading.
- **Corrections applied (image over transcription, rule 2; each added to align/build_pairs.py as a pair override, exceptions.tsv):**
  f61L 58 `96 -> 90` (A, B and this worker's look); f65L 38 `190 -> 192` (A, B; look agrees); f66L 273 `222 -> 223` (A, B; look agrees);
  f66R 183 `222 -> 223` (A 223, B 223?; look not contrary); f61R 32 `223 -> 233` (A 233?, B 293?; this worker reads 2-3-3 on a 2x zoom);
  f65R 65 `37 -> 87` (A, B both 82?; this worker reads 87, a bold 8 over the 7; grade M -- that 87 = 'de' fits the gloss "de Cette" is not
  used as evidence). **Gloss:** P17 is "en secret" only: "Ly passe" is running clear text in the main hand at the line start (both
  passes, and the crop f65L_L05), not part of the decipherment; NEXT-PAG had joined them.
- **Kept against the passes:** f66R 96 `196` (A, B 198; the hand's 6 is the b-shape it uses in 146, look reads 19b); f66R 184 `54` (B, look);
  f66R 169 `2` (A, B 7?; stays M, unsettled); f66L 223 `156` (A, B 150; ambiguous at the crop's edge, stays); f66L 193/278/345 (passes read a
  truncated group at the crop's right edge, not a different digit); the ILLEGIBLE group f61L 48 (both passes: X).
- **Glosses:** 46 of 56 pairs (A) and 47 (B) match the current gloss at letters-only similarity >= 0.85. The rest are line-end truncation
  (P25 "beaucoup", P29 "donnent", P35 "d'Infans", P36 "en avoir" sit at the f66L gutter), spelling (P04 Labarque/Cabargue, P09 Lysle/Lyle,
  P06 "venue"/"acte"/"cette"), or two readings kept against the passes after a look: P41 "et n'a" (passes "ni né"/"ny né"; the gloss runs on
  into the clear "nulle inclination", so "n'a" stays, M) and P49 "issu" (passes "ime"; read as long-s "iſſu", "issu de France", stays, M).
  No gloss was moved to a different run by either pass.
- **Key rebuild (rule 3, controls first, NEXT-PAG's fixed settings: null-cost -3, max-chunk 4, seg-bonus 0.5, len-prior 0.5, 20 shuffle seeds;
  the shuffle permutes the cipher/gloss pairing, which both statistics depend on).** `align/evaluate.py --max-chunk 4 --seg-bonus 0.5
  --len-prior 0.5 --write`: training self-agreement 131/472 = 0.278 vs shuffle mean 0.103, p95 0.121 (before: 0.277 vs p95 0.126); held-out
  letters 24/37 = 0.649 vs shuffle p95 0.378 (unchanged); full run 136/492 = 0.276 (before 138/493 = 0.280). Per-letter
  (`align/per_letter.py`): L1 own 28/95 = 0.295 vs p95 0.086, cross 0.463 vs p95 0.255, PASS; L2 own 83/397 = 0.209 vs p95 0.133, cross
  0.338 vs p95 0.226, PASS. `align/make_key.py` -> key.tsv 111 codes (was 114): 37, 190, 222 drop out (their only occurrences were
  corrected or lost the "y passe" letters), 90 and 233 rise to H, 212 're' and 221 'se' fall from H to M (P17's shorter gloss removed
  agreeing occurrences), 97 'en' -> 'e', 223 'nte' -> 'c'.
- **Per token (rule 4; tools/decode_key.py --check exit 0, "reading up to date"; make_key.py and build_votes.py --check exit 0):**
  H 64, C 0, S 0, M 428, I 7, U 6 of 505 (was H 71, M 422, I 7, U 5). The new U is f65L 48 `222` (no keyed value now). Firm 64. The run
  level is unchanged: 501 of 505 cipher tokens sit under a period gloss, and now 487 of those have been read by two blind passes
  besides NEXT-PAG. Judge not run: no specs/clairambault1225-paget-1714.json. tools/tests/test_decode_key.py: the Paget case passes;
  antt-linhares-chave and rah-canada-1869 fail as before (pre-existing drift, NEXT2-PAG).
Rule 10: readings described only as read from the period interlinear decipherment. Requests: none (all images on disk). Vision
calls: 14 subagent passes + this worker's own crop checks (12 crops).

## Gutter-strip blind passes (A2-PAG3, 2 Oct 2026)

Intake gate first (pasted): `clairambault1225-paget-1714: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`, exit 0.
Ran the Verdict's cheapest next step only: the 18 f66L line-end groups at the gutter that A2-PAG2's passes did not reach.
- **Crops (Usage 6, pasted command):** `python3 ../../tools/iiif_lines.py --image images/f66R.jpg --region 0,150,340,1800 --out images/gutter
  --prefix f66Lg --distance 40 --prominence 30 --lines-per-crop 3 --top-margin 40 --debug` -> 8 crops of 340 x 198-284 px (24 lines,
  pitch 72), each copied at x2 (LANCZOS) for the passes. Crop boxes in `images/gutter/manifest.json`; the jpgs are not committed
  (`imgcheck/regen_crops.sh` re-cuts them). No network request: images/f66R.jpg was on disk.
- **Passes:** 2 blind Sonnet subagent calls (A, B), each given only the 8 gutter crops and told to read no repo file:
  `imgcheck/passA_f66Lgutter.tsv`, `imgcheck/passB_f66Lgutter.tsv`. Reconciliation (the 3rd unit): this worker's look at crops L01, L02, L08.
- **Digits:** all 18 unreached tokens read the same in both passes and equal the reading: f66L 13 `220`, 39-40 `32 125`, 53-54 `39 692`,
  90 `116`, 124-125 `72 33`, 149 `233`, 172 `600` (B `600?`), 197 `238`, 228 `48`, 279 `48`, 301 `221`, 322-323 `35 212`, 346 `97`, 362 `221`.
  The preceding in-strip groups also agree with ciphertext.tsv (e.g. `126 244 211 220`, `212 43 214 32 125`, `46 97 157 39 692`,
  `245 220 116`, `145 238`, `45 48`, `213 34 194 48`, `105 45 175 221`, `38 174 54 35 212`, `200 100 33 97`, `97 58 221`).
  18/18 confirmed, 0 corrected; together with A2-PAG2, 505 of 505 cipher tokens have now been re-read by two blind line-crop passes
  (f61L 48 still ILLEGIBLE in both).
- **Gloss ends:** P25 "Moyenne, beaucoup" (both passes; unchanged); P29 "donnen[t] une" (A/B "donnen"/"donnez", the t at the gutter
  fold; "donnent" kept); P35 "...a pas eu d'Infans" (both; unchanged). **P36 changed:** the gloss over `97 58 221` runs on past "avoir"
  into a two-letter tail at the gutter, read "fe" by both passes and by this worker's look (crop f66Lg_L08) -- the hand's long s, "ſe",
  normalised to "se" as P49 "iſſu" was; it joins the clear "trouvant ... agée de 44 ans" on the next line ("se trouvant"). P36 is
  now "en avoir se" (align/build_pairs.py line 54; grade M). This conflicts with ciphertext.tsv f66L 365, an insertion-clear token
  OX-PAGT pass A read "sceu" (B "attendant", rows differ) off images/f66L.jpg, which stops at the gutter; the ciphertext row is left as
  transcribed (never silently repaired) and the conflict is logged here. That 221 'se' in key.tsv fits the new gloss is not used as evidence.
- **Key rebuild (rule 3, controls first, NEXT-PAG's fixed settings, 20 shuffle seeds over the cipher/gloss pairing, which both statistics
  depend on):** `align/evaluate.py --max-chunk 4 --seg-bonus 0.5 --len-prior 0.5 --write`: shuffle self-agreement p95 0.128, held-out
  letters 24/37 = 0.649 vs shuffle p95 0.378 (unchanged); full run 136/492 = 0.276 (unchanged). Per-letter (`align/per_letter.py`): L1 own
  0.295 vs p95 0.086, cross 0.463 vs p95 0.255, PASS; L2 own 0.209 vs p95 0.135, cross 0.337 vs p95 0.225, PASS. `align/make_key.py` ->
  key.tsv 111 codes; one value changes: 58 'av' -> 'avo' (M, single attestation); 221 stays 'se' (M).
- **Per token (rule 4; tools/decode_key.py . regenerated, then --check exit 0 "reading up to date"; build_votes.py rerun):** H 64, C 0, S 0,
  M 428, I 7, U 6 of 505 (unchanged); firm 64. Judge not run: no specs/clairambault1225-paget-1714.json.
Rule 10: readings described only as read from the period interlinear decipherment. Requests: none (all images on disk). Vision calls:
2 subagent passes + this worker's look at 3 crops.

## Remaining gaps (finish-or-blocker pass, 1 Oct 2026; updated 2 Oct 2026, NEXT-PAG, NEXT2-PAG, PAGET-KEY, A2-PAG, A2-PAG2 and A2-PAG3)
Read so far: (decode.json run 2 Oct 2026, A2-PAG2) token level H 64, M 428, I 7, U 6 of 505 (firm 64); run level 501 of 505 cipher tokens (99.2%) lie under a period interlinear gloss, read off the page images by NEXT-PAG and, for all 505 cipher tokens, re-read by two blind line-crop passes (A2-PAG2 487, imgcheck/: 476 digits agree with the reading, 6 corrected, 2 glosses corrected or kept by a look; A2-PAG3 the 18 f66L gutter tokens, all agree, P36 gloss tail added), so the run-level plaintext of both letters' cipher passages is in hand; code-level, key.tsv holds 111 codes, both letters having cleared per-letter controls (align/per_letter.txt).
- Code-level values for the 428 M tokens (single-attestation/unsettled codes in key.tsv at M, plus tokens whose own chunk disagrees with a stable code; frequent codes 46, 146, 145, 175 unsettled) - blocker: open-codes; the alignment (self-agreement 0.276 vs shuffle p95 0.121, A2-PAG2) does not hold one value for them, which fits homophones/nulls or a decipherer's gloss that paraphrases (f66R "de Parme" with no 87.201.156 under it); context does not narrow them further at run level, where the gloss already gives the plaintext
- f66L 169-172 '400 4 19 600' ("une complaisance aveugle pour ..."), 4 tokens - blocker: no-key-material; no gloss above this run on images/f66L.jpg (checked 2 Oct 2026), none of the four codes recurs under a gloss, and no key sheet is known (AN Marine B7 original waits on LOCAL-QUEUE L11)
- f61L, one cipher group solid-inked over (between 175 and 276, f61L ~pos48) - blocker: illegible; hand-marked ILLEGIBLE in both transcription passes; its gloss text ("on verra quelques personnes a Genes", P05) is read, its code number is not. The only other witness is the AN Marine B7 original (LOCAL-QUEUE L11, queued 25 Sept 2026, unanswered)

## Escalation (1 Oct 2026; updated 2 Oct 2026, NEXT-PAG, NEXT2-PAG, PAGET-KEY, A2-PAG, A2-PAG2 and A2-PAG3)
- [x] siblings: neighbouring leaves in the volume opened (f55-f59 Fleury testament and notice; f67/f70/f75 unrelated Puget/Peraud print; OX-PAG, images/manifest.json). The BnF Clairambault name index lists only this item for "PAGET -- Lettres chiffrees". The Paget 14 Jan 1713 sibling (ciphers/clairambault296-paget-1713) was not found in 314 of 316 Gallica canvases; canvases 28 and 36 are unread (LOCAL-QUEUE L23 done-blocked 27 Sept 2026), and the retry belongs to that target's NEXT-STEPS row 31 and ASKS row 51. DECODE, Bourdeau and Aymeloglu had no Paget hit (23 Sept 2026). The AN Marine B7 originals wait on LOCAL-QUEUE L11, and SIV form reproduction is NEXT-STEPS row 30 (NX-UNBLOCK, HTTP 500 once). No internal sibling step is left in this folder
- [x] clear-pages: no separate clear copy or decipherment sheet on the neighbouring leaves; the clear text is the letters' own interlinear decipherment, which on the images (2 Oct 2026) covers 501 of 505 cipher tokens, far more than ciphertext.tsv's insertion-clear rows record; used in full by the key-rebuild below
- [x] known-keys: already swept. KEY-CROSSMATCH.tsv has 45 rows for this ciphertext against every key on file: 28 none, 9 unusable-key, 8 no_corpus. The best coverage, 0.353, is fr7129's f275 code key (no_corpus); the nearest French nomenclator is Le Tellier 1659-ext at 0.196 (none). KEY-DESIGN-PRIORS.tsv row 12 (design_prior.py --unkeyed) ranks multi-sign (homophonic/nomenclator/syllabary) first (0.94), with lead vanbeuningen-dewitt-1657. KEY-OFFICES.tsv and KEY-DESIGN.tsv have no French Marine or consular key from 1700-1729 (grepped 1 Oct 2026). 'chiffre de M. Paget' and 'chiffre pour Genes' came back negative in Google Books and web search (OX-PAGK). A re-run against key.tsv's 21 codes is not worth doing before the retry step
- [x] print: 2 Oct 2026 (A2-PAG): tools/print_check.py on 16 gloss phrases (phrases.txt) + 5 keyword sources (sources.tsv) -> print-check.tsv: IA full text, OpenAlex, CrossRef, Google Books; plus Google Books snippet queries, HAL API and Persee. No print of either letter's text or decipherment located; the only Paget-specific print remains the Inventaire des archives de la marine B7 register summaries (OX-PAGK). Semantic Scholar and CrossRef 429 mid-run (one retry each per the good-citizen rule; S2 retry answered, no hit). Earlier: RIDA XIX (Driault 1912) ContentSearch 'Paget' 3 irrelevant hits, 'Cagliari' 0 (CX2-MISC2); Mezin 1998, Ulbert 2019 (OX-PAGK)
- [x] key-rebuild: 2 Oct 2026 (PAGET-KEY): per-letter controls both PASS (L1 own 0.323 vs p95 0.084, cross 0.454 vs 0.258; L2 own 0.207 vs 0.133, cross 0.341 vs 0.229); key.tsv 114 codes (11 H, 10 C, 93 M); decode H 71 M 422 I 7 U 5. Earlier, 2 Oct 2026 (NEXT-PAG): tools/interlinear_align.py over 56 image-read gloss pairs (52 training, 4 held out), with the new --max-chunk 4 --seg-bonus 0.5 --len-prior 0.5 options; training self-agreement 0.277 vs shuffled-pairing p95 0.126, held-out known-answer letters 24/37 = 0.649 vs shuffle p95 0.378 (both above control); key.tsv 21 codes (12 C, 9 M); the 1 Oct note's code-147 contradiction was a misread gloss ("Lisle", not "Gile"). At the brief's Thurloe defaults the same run did not beat its control (0.175 vs p95 0.184), logged above
- [x] image-check: 2 Oct 2026 (A2-PAG3): the f66L gutter strip, 8 crops from images/f66R.jpg's left 340 px, 2 blind Sonnet passes + a look: 18/18 unreached tokens confirmed, 0 corrected; P36 gloss "en avoir" -> "en avoir se"; controls PASS; key.tsv 111 codes (58 av -> avo); decode H 64 M 428 I 7 U 6. Earlier, A2-PAG2: 81 line crops (tools/iiif_lines.py --image, lines-per-crop 2, top-margin 90), 14 blind Sonnet passes (2 per page-half) + reconciliation by look; of 505 cipher tokens 472 matched the reading in both passes, 12 both-passes-differ, 3 split, 18 unreached (f66L gutter); 6 digits corrected (f61L 58 90, f61R 32 233, f65L 38 192, f65R 65 87, f66L 273 223, f66R 183 223), P17 gloss cut to "en secret"; controls re-run, both letters PASS; key.tsv 111 codes; decode H 64 M 428 I 7 U 6
- [x] retry: 2 Oct 2026 (PAGET-KEY): regraded decode --check exit 0, H 71 M 422 I 7 U 5. Earlier (NEXT2-PAG): decode.json + tools/decode_key.py --check over both letters, exit 0; C 71, M 47, I 7, U 380 of 505 ("Decode script" above); --split-check 0 candidate splits
Verdict: keep going: 1 internal gaps; cheapest next: the open-codes homophone pass (group the 428 M tokens' codes by agreeing aligned chunks across both letters, per-letter shuffle control first, align/ only, no images), ~$2

## Web and blog check (NEXT2-PAG, 2 Oct 2026)

Step "Open web and blog comment threads" of .claude/briefs/check-solved.md, run by this worker on 2 Oct 2026.
(a) Plain web searches (WebSearch, standard):
1. `Paget 1714 Gênes lettres chiffre Clairambault 1225` (sender + place + date + shelfmark + "chiffre"): hits were the
   BnF catalogue notice of the Clairambault catalogue (Lauer 1923-32), SOAS Paget papers (William, 6th Baron Paget,
   d. 1713 -- a different Paget), unrelated library records. No transcription or decipherment of this item.
2. `Paget vice-consul Genes 1714 lettre chiffrée Monseigneur Princesse de Parme` (sender + recipient + date + content):
   SOAS / AIM25 / TNA records of the 6th Baron Paget's papers (c.1684-1709, Vienna/Turkey). Nothing on this Paget.
3. `"Prince Antoine de Parme" "35 ans" 1714 Paget` (distinctive phrase from the period gloss): biographical hits for
   Antonio Farnese (b. 1679) and Sardinian library records; no page carrying the letter's text.
4. `"Lettres autogr. de Paget, avec chiffre"` (the folder's descriptive title, quoted): Bodleian and Wellcome
   autograph-letter collections of 19th-century Pagets; no hit on the BnF item.
(b) Site searches of the three blogs:
- **Cipherbrain** (scienceblogs.de/klausis-krypto-kolumne), `Paget Genoa 1714 cipher`: ten unrelated posts (Henry II
  device, pigpen, Bonn archive, Devil's letter, Bunch, D'Agapeyeff); no Paget or Genoa post.
- **Cryptiana blog** (cryptiana.blogspot.com, cryptiana.web.fc2.com), `Paget Gênes 1714 chiffre Clairambault`: no
  results. Local snapshot sources/cryptiana/ grepped for "Paget" and "Clairambault 1225": only the unrelated Charles
  Paget/Mary Queen of Scots cipher (already flagged above) and Louis XIV pages without this item.
- **Cipher Mysteries** (ciphermysteries.com), `Paget 1714 Genoa cipher letter Clairambault` (the search tool also
  ran variants): Guinigi, Beale, Voynich, La Buse, Milanese letters and other posts; no Paget or Genoa 1714 post.
(c) No hit was plausible enough to open a comment thread: none named this Paget, Genoa in 1714, or Clairambault 1225.
Result: no decipherment or plaintext of this item located on the open web or in the three blogs (a search result, not a
novelty verdict, rule 10). Requests: WebSearch 7 calls; no direct host fetch.

## Premise check (PAGET-KEY, 2 Oct 2026)

Adversarial pass per .claude/briefs/check-solved.md, trying to show the item is already done before step 2 of the brief.
- (a) Folder's own mentions -- found, already in use: the only decipherment the folder mentions is the period interlinear
  decipherment written over the cipher runs on f60R-f66R (NEXT-PAG, images on disk, opened again by reading NEXT-PAG's
  per-page notes). It is the letters' own contemporary decipherment, not a modern one, and it is the material this
  brief's step 2 turns into key entries; it makes the run-level plaintext period-read, which NOTES already says. No
  REQUEST.md or spec exists. No other decipherment, clear copy or key sheet is mentioned anywhere in the folder.
- (b) Other solvers' working files -- not found. Fresh shallow clones on 2 Oct 2026 (cyphersolver HEAD of 1 Oct 2026;
  unsolved-ciphers) grepped for paget, "clairambault 1225", btv1b9001034d across all files: Bourdeau carries this item only
  as a catalogue line in research/gallica_sweep/bnf_candidates.txt (line 319) and sru_chiffre_desc.json (the BnF
  description text); no target folder, rendering or apply-key script. His other "paget" hits are Charles Paget /
  Elizabethan targets (sp53, stafford1586, cobham1588) and one random-letter string. Aymeloglu: one false hit
  ('pagetexts' in a Python file). No key of theirs has been run on this text.
- (c) Physical neighbours -- not found (from OX-PAG, 25 Sept 2026, images/manifest.json): f55-f59 Fleury testament and
  notice; f67/f70/f75 unrelated print. No clear copy or decipherment sheet bound beside the letters; the decipherment is
  interlinear on the cipher leaves themselves.
- (d) Recipient side -- not found. The recipient is an unnamed "Monseigneur ... Vostre Excelence" (consular business: the
  Secretary of State for the Marine, Pontchartrain, is the likeliest office; Torcy at Foreign Affairs the other). WebSearch
  (3 queries, 2 Oct 2026): Paget + consul + Genes/Sardaigne + Torcy/Pontchartrain; Paget + consul + Cagliari 1714/1715
  (Italian-side scholarship: Ammentu articles on consuls in Cagliari, AE/B/I/301-312 Cagliari consular series 1672-1791 named,
  no Paget); Torcy's printed Journal (Masson 1903) covers 1709-1711 only, before these letters. No printed edition of
  Pontchartrain's incoming consular letters for 1714 located; the originals sit in AN Marine B7 (LOCAL-QUEUE L11). RIDA XIX
  (Genoa instructions) already searched (CX2-MISC2).
Result: no prior modern decipherment or print of these letters located; the item stays partial and step 2 proceeds
(a search result, not a novelty verdict, rule 10). Requests: github.com 2 clones; WebSearch 3.

## Next step (READ2-RELABEL, 3 Oct 2026)
Images are on disk and read: the Gallica leaves f55-f66 (Clairambault 1225, ark btv1b9001034d) are in images/ (f60-f66 L/R halves, gutter strip and bracket crops, manifest.json with folio_pinning), and two blind line-crop passes plus the f66L gutter pass re-read all 505 cipher tokens against them (A2-PAG2, A2-PAG3). The next step is therefore the open-codes homophone pass on the 428 M tokens, run on align/ alone (group the codes by agreeing aligned chunks across both letters, per-letter shuffle control first), ~$2; it needs nothing further from an archive. The only unread pieces are 4 tokens (f66L 169-172, no gloss) and one solid-inked group (f61L), both waiting on the Marine B7 originals (LOCAL-QUEUE L11), unchanged.

## READ2-PAG (3 Oct 2026)

Intake gate (pasted by LANE-READ2): `clairambault1225-paget-1714: partial (line 1) -- edition/page or full-text-search citation found
within 6 lines`, exit 0. Disk only: no network request, no vision call, no subagent. Tool shelf (`tools/tool_shelf.py "assign values
to homophone/null cipher codes from an interlinear gloss alignment"`) offered tools/interlinear_align.py [controlled-only]; used as the
aligner through align/evaluate.py (no private aligner).
- **Pre-registration** `align/PREREG_homophone.md`, pushed as 0cfc96eb before the first run: classes one-unit / homophones (read off
  the key, codes per value) / nulls (configuration C2, null-cost 0, empty chunk a value); statistic held-out agreement, each letter
  aligned alone, key_A = unique top chunk, scored on the other letter, both directions; control the gloss texts permuted within each
  letter, 200 seeds; gate above shuffle p95 both directions; per-code promotion only if the both-direction code count also clears
  its shuffle p95 and the value equals key.tsv's.
- **Result** (`align/homophone_pass.py` -> `align/homophone_pass.txt`, `align/homophone_codes.tsv`):

| configuration | L1 -> L2 real / shuffle mean / p95 | L2 -> L1 real / shuffle mean / p95 | gate | codes both directions real / mean / p95 |
|---|---|---|---|---|
| C1 null-cost -3 | 24/134 = 0.179 / 0.032 / 0.074 | 9/47 = 0.191 / 0.046 / 0.111 | PASS | 4 / 0.4 / 1 |
| C2 null-cost 0 | 22/166 = 0.133 / 0.359 / 0.466 | 14/55 = 0.255 / 0.440 / 0.574 | FAIL | 3 / 0.0 / 0 |

  C1's four codes: 87 de, 146 le, 196 po, 240 ion (four values, no homophone set shown; four codes is too few to argue against
  homophones). C2 fails: free nulls raise chance agreement on empty chunks above the real figure, so nulls get no support here.
- **Key and grades.** align/make_key.py now reads the passing configuration's codes: 146 'le' (the only M row among the four) becomes
  S, note "homophone pass S"; decode.json gains `s_words` (Usage 8: tools/decode_key.py option `s_words`, S where the token's own
  chunk agrees or is absent, disagree_grade where it disagrees; offline case in tools/tests/test_decode_key.py passes; the antt-linhares-chave
  and rah-canada-1869 failures there are the drift NEXT2-PAG logged). `tools/decode_key.py ciphers/clairambault1225-paget-1714 --check`:
  `ciphertext.tsv: tokens 505: H 64, I 7, M 420, S 8, U 6` / `reading up to date`. Per token (rule 4): **H 64, C 0, S 8, M 420, I 7, U 6**
  of 505; firm (H+C+S) 72. The 8 S are code 146 tokens whose own aligned chunk is 'le'; its other 12 stay M.
- Judge: not run -- no specs/clairambault1225-paget-1714.json. HYPOTHESES.md opened with this row and the instrument count (one aligner,
  four tests; the 420 M stay "untested-by-this-tool", the next step needs a different instrument or new material).
Rule 10: values described only as read from the period interlinear decipherment, or chosen by this test (S).
`tools/gaps_check.py clairambault1225-paget-1714` (pasted): `OK keep-going clairambault1225-paget-1714: keep going: 1 internal gap(s), 1 step(s) untried`.

## Remaining gaps (READ2-RELABEL, 3 Oct 2026; restates the 2 Oct 2026 section, nothing re-run)
Read so far: token level H 64, M 428, I 7, U 6 of 505 (firm 64), decode.json run 2 Oct 2026 (A2-PAG2); 99.2% of tokens lie under a period interlinear gloss read off the images on disk
- Code-level values for the 428 M tokens (single-attestation or unsettled codes; frequent codes 46, 146, 145, 175) - blocker: open-codes; alignment self-agreement 0.276 vs shuffle p95 0.121 does not hold one value for them, which fits homophones, nulls or a paraphrasing gloss; next: the homophone pass on align/, per-letter shuffle control first, ~$2
- f66L 169-172 '400 4 19 600', 4 tokens - blocker: no-key-material; no gloss above this run on images/f66L.jpg, none of the four codes recurs under a gloss; the Marine B7 original waits on LOCAL-QUEUE L11
- f61L, one solid-inked cipher group - blocker: illegible; hand-marked ILLEGIBLE in both passes, its gloss ("on verra quelques personnes a Genes") is read, its code is not; the only other witness is the Marine B7 original (LOCAL-QUEUE L11)

## Escalation (READ2-RELABEL, 3 Oct 2026; restates the 2 Oct 2026 ladder)
- [x] siblings: neighbouring leaves f55-f59, f67, f70, f75 opened (OX-PAG); the Paget 1713 sibling is another target's row; no internal sibling step left in this folder
- [x] clear-pages: no separate clear copy; the interlinear decipherment on the images covers 501 of 505 tokens and is used in full
- [x] known-keys: KEY-CROSSMATCH.tsv 45 rows, 28 none, 9 unusable-key, 8 no_corpus; no French Marine or consular key 1700-1729 on file
- [x] print: tools/print_check.py on 16 gloss phrases and 5 keyword sources (A2-PAG, 2 Oct 2026); nothing printed located
- [x] key-rebuild: per-letter controls both PASS (PAGET-KEY, A2-PAG2); key.tsv 111 codes; decode H 64 M 428 I 7 U 6
- [x] image-check: 81 line crops, 14 blind passes plus reconciliation (A2-PAG2) and the f66L gutter strip (A2-PAG3), all on disk
- [x] retry: decode --check exit 0 at the 2 Oct 2026 regrade; re-run it after the homophone pass
Verdict: keep going: 1 internal gaps; cheapest next: the open-codes homophone pass on the 428 M tokens (align/ only; the page images are on disk and already re-read), ~$2

## Remaining gaps (READ2-PAG, 3 Oct 2026)
Read so far: token level H 64, S 8, M 420, I 7, U 6 of 505 (firm 72), tools/decode_key.py --check 3 Oct 2026; 99.2% of tokens lie under a period interlinear gloss read off the images on disk, so the run-level plaintext of both letters' cipher passages is in hand
- Code-level values for the 420 M tokens (single-attestation or unsettled codes; frequent codes 46, 145, 175; 12 tokens of 146 whose own chunk disagrees) - blocker: open-codes; tools/interlinear_align.py has now run four tests on these codes (NEXT-PAG defaults and syllabic options, PAGET-KEY per-letter gates, READ2-PAG held-out homophone/null pass: C1 PASS 0.179/0.191 vs p95 0.074/0.111, 4 codes vs p95 1; C2 FAIL), and only 146 'le' moved; rule 3's third-attempt clause retires a fifth configuration of the same aligner; next: a different segmentation instrument that does not draw chunk boundaries from hard-EM on the same 56 pairs, or the Marine B7 originals (LOCAL-QUEUE L11)
- f66L 169-172 '400 4 19 600', 4 tokens - blocker: no-key-material; no gloss above this run on images/f66L.jpg, none of the four codes recurs under a gloss; the Marine B7 original waits on LOCAL-QUEUE L11
- f61L, one solid-inked cipher group - blocker: illegible; hand-marked ILLEGIBLE in both passes, its gloss ("on verra quelques personnes a Genes") is read, its code is not; the only other witness is the Marine B7 original (LOCAL-QUEUE L11)

## Escalation (READ2-PAG, 3 Oct 2026)
- [x] siblings: neighbouring leaves f55-f59, f67, f70, f75 opened (OX-PAG); the Paget 1713 sibling is another target's row; no internal sibling step left in this folder
- [x] clear-pages: no separate clear copy; the interlinear decipherment on the images covers 501 of 505 tokens and is used in full
- [x] known-keys: KEY-CROSSMATCH.tsv 45 rows, 28 none, 9 unusable-key, 8 no_corpus; no French Marine or consular key 1700-1729 on file
- [x] print: tools/print_check.py on 16 gloss phrases and 5 keyword sources (A2-PAG, 2 Oct 2026); nothing printed located
- [ ] key-rebuild: per-letter controls both PASS (PAGET-KEY, A2-PAG2); READ2-PAG held-out homophone/null pass C1 PASS, C2 FAIL, 146 'le' to S; key.tsv 111 codes. tools/interlinear_align.py has run four tests on these 56 pairs (NEXT-PAG x2, PAGET-KEY, READ2-PAG) and a fifth configuration of it is closed by rule 3's third-attempt clause; planned: a different segmentation instrument not drawn from hard-EM on the same pairs (tool_shelf candidates first, with their known-answer check), per-letter held-out control as in align/PREREG_homophone.md, ~$6
- [x] image-check: 81 line crops, 14 blind passes plus reconciliation (A2-PAG2) and the f66L gutter strip (A2-PAG3), all on disk
- [x] retry: tools/decode_key.py --check exit 0 after the homophone pass (READ2-PAG): H 64 S 8 M 420 I 7 U 6
Verdict: keep going: 1 internal gaps; cheapest next: a different segmentation instrument for the 420 M tokens (tool_shelf first, per-letter held-out control as in align/PREREG_homophone.md), ~$6


## RUN1-PAG (4 Oct 2026): a different segmentation instrument for the M tokens

Intake gate (re-run): `clairambault1225-paget-1714: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`,
exit 0. Disk only: no network request, no vision call, no subagent.
Tool shelf (`tools/tool_shelf.py "segment cipher group run against interlinear gloss / homophone code values"`, pasted in part):
`[controlled-only] interlinear_align.py ... last: READ2-PAG ... 3 Oct 2026` / `[controlled-only] seg_homophonic.py ... unseparated digit
cipher with no key` / `[weak] cipher_page_detector.py` / `[controlled-only] families/seeded_code.py` / `[proven] glyph_atlas.py`. None
is a non-hard-EM gloss segmenter (seg_homophonic splits unseparated digits with no gloss), so a new shared tool was written.
- **Instrument** `tools/gibbs_align.py` (Usage 8: shared tool, `--help`, offline test `tools/tests/test_gibbs_align.py`: synthetic
  homophonic syllabary with nulls and inserted words, planted values recovered 1.000 on the true pairing, 0.028 shuffled; SYSTEM.md row
  added). A collapsed Gibbs sampler: each code's chunk distribution has a Dirichlet-process prior (chunk-length prior x the gloss's own
  letter unigrams), each pair's chunk boundaries are sampled forward-filter backward-sample given all other pairs, nulls are length-0
  chunks under the prior, letters the decipherer added are an explicit insertion state; values are posterior modes over the kept
  sweeps. It takes nothing from the earlier alignments and is not hard-EM, so rule 3's third-attempt clause on interlinear_align does
  not cover it.
- **Pre-registration** `align/PREREG_seg2.md`, pushed as 6b029b41 before any run: tool defaults (not tuned); held-out agreement as
  READ2-PAG C1 (each letter sampled alone); step 1 matched known-answer control first (synthetic gloss on the real code runs of both
  letters, 10% nulls, Zipf-weighted 60-chunk inventory so codes share values, 15% runs with an inserted word; gate mean >= 0.50 both
  directions); step 2 per-letter gloss shuffle, 200 seeds (it can differ: the statistic depends on which gloss lies over which run);
  gate above shuffle p95 both directions; per-code promotion M -> S only when the value held in both letters equals key.tsv's value.
- **Result** (`align/gibbs_pass.py` -> `align/gibbs_pass.txt`, `align/gibbs_codes.tsv`; deterministic seeds, `--check`):

| step | L1 -> L2 | L2 -> L1 | gate | codes held in both letters |
|---|---|---|---|---|
| matched known-answer control, 10 synthetic seeds | mean 0.808 (min 0.548) | mean 0.731 (min 0.429) | PASS | planted-value recovery 0.980 |
| target vs per-letter gloss shuffle, 200 seeds | 110/211 = 0.521 / mean 0.015 / p95 0.066 | 47/69 = 0.681 / mean 0.016 / p95 0.067 | PASS | 18 / mean 0.2 / p95 1 |

  For comparison, the hard-EM aligner under the same statistic (READ2-PAG C1) gave 0.179 / 0.191 and 4 codes. 18 codes, 18 distinct
  values (no homophone set among them). Against key.tsv: 5 equal an existing H row (87 de, 90 du, 147 li, 233 te, 244 ve); **6 equal
  an M row and become S** (32 c, 47 t, 145 la, 175 ne, 212 re, 221 se; note "Gibbs pass S", align/make_key.py); **7 differ** and are
  logged, not changed (two instruments disagreeing is not a value): 31 b (key ab), 45 r (ar), 48 u (une), 97 en (e), 148 lo (le),
  176 ni (en), 204 que (ue). Most of the seven are boundary shifts of one letter (ab/b, ar/r, ue/que), which is what the two
  instruments segment differently.
- **Decode** `python3 tools/decode_key.py ciphers/clairambault1225-paget-1714 --check`: `ciphertext.tsv: tokens 505: H 64, I 7, M 397,
  S 31, U 6` / `reading up to date`. Per token (rule 4): **H 64, C 0, S 31, M 397, I 7, U 6** of 505 (was H 64, S 8, M 420); firm
  (H+C+S) 95. The 23 new S tokens are tokens of the six promoted codes whose own aligned chunk agrees or is absent; their tokens with
  a disagreeing chunk stay M. decode.json gains s_words "Gibbs pass S"; tools/tests/decode_configs/clairambault1225-paget-1714.json
  updated to match (test_decode_key.py: the 3 remaining failures are the antt-linhares-chave and rah-canada-1869 drift NEXT2-PAG logged).
- Judge: not run -- no specs/clairambault1225-paget-1714.json. Rule 10: values described only as read from the period interlinear
  decipherment, or chosen by a pre-registered test (S). Requests: none. Subagents: none.
- Suggestion (Usage 7, not done): the 7 disagreeing codes could be settled per token by reading each one's own chunk against both
  instruments' segmentations of the same pair (align/align_all.tsv vs a full-data gibbs_align run); ~$1.

## Remaining gaps (RUN1-PAG, 4 Oct 2026)
Read so far: token level H 64, S 31, M 397, I 7, U 6 of 505 (firm 95), tools/decode_key.py --check 4 Oct 2026; 99.2% of tokens lie under a period interlinear gloss read off the images on disk, so the run-level plaintext of both letters' cipher passages is in hand
- Code-level values for the 397 M tokens (mostly single-attestation codes, plus the 7 codes where the Gibbs pass and the aligner disagree: 31, 45, 48, 97, 148, 176, 204) - blocker: open-codes; two instruments now run (tools/interlinear_align.py, four tests; tools/gibbs_align.py, PREREG_seg2.md PASS 0.521/0.681 vs p95 0.066/0.067, 18 codes vs p95 1); a code seen once cannot be held in both letters by either; next: settle the 7 disagreeing codes per token from both segmentations, ~$1
- f66L 169-172 '400 4 19 600', 4 tokens - blocker: no-key-material; no gloss above this run on images/f66L.jpg, none of the four codes recurs under a gloss; the Marine B7 original waits on LOCAL-QUEUE L11
- f61L, one solid-inked cipher group - blocker: illegible; hand-marked ILLEGIBLE in both passes, its gloss ("on verra quelques personnes a Genes") is read, its code is not; the only other witness is the Marine B7 original (LOCAL-QUEUE L11)

## Escalation (RUN1-PAG, 4 Oct 2026)
- [x] siblings: neighbouring leaves f55-f59, f67, f70, f75 opened (OX-PAG); the Paget 1713 sibling is another target's row; no internal sibling step left in this folder
- [x] clear-pages: no separate clear copy; the interlinear decipherment on the images covers 501 of 505 tokens and is used in full
- [x] known-keys: KEY-CROSSMATCH.tsv 45 rows, 28 none, 9 unusable-key, 8 no_corpus; no French Marine or consular key 1700-1729 on file
- [x] print: tools/print_check.py on 16 gloss phrases and 5 keyword sources (A2-PAG, 2 Oct 2026); nothing printed located
- [x] key-rebuild: second instrument tools/gibbs_align.py (RUN1-PAG): matched control PASS 0.808/0.731, target PASS 0.521/0.681 vs shuffle p95 0.066/0.067, 18 codes vs p95 1; 6 codes M -> S, 7 disagreements logged; key.tsv 111 codes
- [x] image-check: 81 line crops, 14 blind passes plus reconciliation (A2-PAG2) and the f66L gutter strip (A2-PAG3), all on disk
- [x] retry: tools/decode_key.py --check exit 0 after the Gibbs pass: H 64 S 31 M 397 I 7 U 6
Verdict: keep going: 1 internal gaps; cheapest next: settle the 7 codes where tools/gibbs_align.py and tools/interlinear_align.py disagree, per token from both segmentations, ~$1

## RUN2-PAG (4 Oct 2026): the 7 codes where gibbs_align and interlinear_align disagree, settled per token

Intake gate (re-run): `clairambault1225-paget-1714: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`,
exit 0. Disk only: no network request, no vision call, no subagent; the segmentations on disk were enough (no crop was missing).
- **Table** `align/settle7.py` -> `align/settle7.tsv` (every occurrence of 31, 45, 48, 97, 148, 176, 204: pair, page, hard-EM chunk
  from align_all.tsv, the token's own chunk in the per-letter seed-0 Gibbs run that passed PREREG_seg2.md held-out, a pooled Gibbs
  run, the gloss, and both tools' segmentation of the whole pair) and `align/settle7_rulings.tsv` (54 occurrences, one ruling each).
  Deterministic; `--check` also fails if an S ruling is missing from exceptions.tsv.
- **Rule** (as briefed): S where the token's own Gibbs chunk equals the held-out-passed code value and the gloss word, with its firm
  (H/C/S) neighbours, admits it; otherwise M. No H. Three tokens whose own chunk agrees were demoted by eye (DEMOTE in the script):
  97 in "en secret" (f65L 52) and "en 2e Nopces" (f66L 289), where "en" could sit on an unsettled neighbour; 176 in "genie"
  (f66R 285), where ni needs 116 = ge against key.tsv's 116 = g (C).
- **What the context shows.** The hard-EM values were mostly one-letter boundary slips that firm neighbours expose:
  "Labbe" = 145 la (S) + 31 + 67 be (H), so 31 = b, not ab (ab gives "laabbe"); 31 = b also reads "Octo|b|re", "b|lo|n|de",
  "b|elle" (x3). "Lomeliny" = la b be **lo** me li **ni**; "blonde" again gives 148 = lo. 176 = ni in Venise (ve H, se S), unique,
  Dernier. 45 = r in verra, personnes, portion, penetrer (t S, re S), air, Farnese (ne S, se S), charmes, toujours, Labarque.
  48 = u in une/Jeune (ne S), un, unique, vente, toujours. 204 = que in "que 36", "que 35" (205 = qui C sits before it), unique,
  Labarque. 97 = en in "vente" (te H) and "en avoir".

| code | key was | now | occurrences | S | M (why) |
|---|---|---|---|---|---|
| 31 | ab | b | 8 | 8 | 0 |
| 45 | ar | r | 15 | 11 | 4 (donnent: nt; Parme: 201 = par already, 45 extra; Dernier idx 2: own chunk "eder"; le Roy d'Espagne) |
| 48 | une | u | 12 | 9 | 3 (donnent une: une at run end; epousa: a; le Roy: le) |
| 97 | e | en | 7 | 2 | 5 (en secret, en 2e: not pinned; mil: 1692 run unaligned; d'Infans: gloss "in"; n'ait: null) |
| 148 | le | lo | 2 | 2 | 0 |
| 176 | en | ni | 5 | 4 | 1 (genie: 116 conflict) |
| 204 | ue | que | 5 | 4 | 1 (qu'on: own chunk "quon") |
| total | | | 54 | 40 | 14 |

- **Key.** The 7 rows of key.tsv take the Gibbs value at grade M with an "unsettled per token" note (so every token not ruled S stays
  M); the 40 S tokens enter exceptions.tsv at grade S, value = code value, reason citing settle7_rulings.tsv. f66L 51 (ciphertext 95,
  pair 97 by the image override already in exceptions.tsv) is ruled M and its existing exception row is untouched.
- **Decode** `python3 tools/decode_key.py ciphers/clairambault1225-paget-1714 --check`: `ciphertext.tsv: tokens 505: H 64, I 7, M 357,
  S 71, U 6` / `reading up to date`. Per token (rule 4): **H 64, C 0, S 71, M 357, I 7, U 6** of 505 (was S 31, M 397); firm 135.
  tools/tests/test_decode_key.py: same 3 failures as before the change (antt-linhares-chave, rah-canada-1869 drift), checked with
  the change stashed.
- Not done (Usage 7): code 65 also reads "ab" over a "Labbe" (f61L 147) and is outside these seven; and 116 (g, C) vs "ge" in
  "genie"/"Visage" is a neighbour conflict this job did not settle.
- Requests: none. Subagents: none.
- `python3 tools/gaps_check.py clairambault1225-paget-1714`: `OK keep-going clairambault1225-paget-1714: keep going: 1 internal gap(s), 0 step(s) untried`

## Remaining gaps (RUN2-PAG, 4 Oct 2026)
Read so far: token level H 64, S 71, M 357, I 7, U 6 of 505 (firm 135), tools/decode_key.py --check 4 Oct 2026; 99.2% of tokens lie under a period interlinear gloss read off the images on disk, so the run-level plaintext of both letters' cipher passages is in hand
- Code-level values for the 357 M tokens (mostly single-attestation codes; the 7 Gibbs/hard-EM disagreements are settled per token, 40 S and 14 M, align/settle7_rulings.tsv) - blocker: open-codes; two instruments run (tools/interlinear_align.py; tools/gibbs_align.py, PREREG_seg2.md PASS) and the per-token pass done; a code seen once cannot be held in both letters by either; next: the same per-token reading for code 65 and the 116 g/ge conflict, ~$1
- f66L 169-172 '400 4 19 600', 4 tokens - blocker: no-key-material; no gloss above this run on images/f66L.jpg, none of the four codes recurs under a gloss; the Marine B7 original waits on LOCAL-QUEUE L11
- f61L, one solid-inked cipher group - blocker: illegible; hand-marked ILLEGIBLE in both passes, its gloss ("on verra quelques personnes a Genes") is read, its code is not; the only other witness is the Marine B7 original (LOCAL-QUEUE L11)

## Escalation (RUN2-PAG, 4 Oct 2026)
- [x] siblings: neighbouring leaves f55-f59, f67, f70, f75 opened (OX-PAG); the Paget 1713 sibling is another target's row; no internal sibling step left in this folder
- [x] clear-pages: no separate clear copy; the interlinear decipherment on the images covers 501 of 505 tokens and is used in full
- [x] known-keys: KEY-CROSSMATCH.tsv 45 rows, 28 none, 9 unusable-key, 8 no_corpus; no French Marine or consular key 1700-1729 on file
- [x] print: tools/print_check.py on 16 gloss phrases and 5 keyword sources (A2-PAG, 2 Oct 2026); nothing printed located
- [x] key-rebuild: tools/gibbs_align.py (RUN1-PAG) PASS 0.521/0.681 vs p95 0.066/0.067; RUN2-PAG per-token rulings on its 7 disagreements with interlinear_align: 40 S, 14 M; key.tsv 111 codes
- [x] image-check: 81 line crops, 14 blind passes plus reconciliation (A2-PAG2) and the f66L gutter strip (A2-PAG3), all on disk
- [x] retry: tools/decode_key.py --check exit 0 after RUN2-PAG: H 64 S 71 M 357 I 7 U 6
Verdict: keep going: 1 internal gaps; cheapest next: the same per-token reading for code 65 ("ab" over "Labbe") and the 116 g/ge neighbour conflict, ~$1

## N4-PAG65 (4 Oct 2026): codes 65 and 116 settled per token

Brief: `.claude/briefs/runs/2026-10-04-ytbiz-near4-wave1.md` section N4-PAG65 (LANE-NEAR4, account 2). Disk only: no network request,
no vision call, no subagent. Method: RUN2-PAG's `align/settle7.py`, extended in place (CODES/GIBBS gain 65 and 116, three DEMOTE
entries added, RUN2-PAG's P53 demotion of 176 lifted); same S/M rule. Neither code is in gibbs_codes.tsv (not held in both letters),
so the value used is the per-letter seed-0 Gibbs run's own chunk, the run that passed PREREG_seg2.md held-out: 65 = b (1/1, letter 1),
116 = ge (4/4, all letter 2, share 1.00 each).
- **65** (f61L 147, "Labbe"): 145 la (S) + 65 + 67 be (H); hard-EM's "ab" reads "laabbe", b reads "Labbe" -- the same slip as 31.
  Key 65: ab -> b (M, single attestation); the token is S through exceptions.tsv.
- **116**: key.tsv had g at grade C from interlinear_align 2/4. Its two g readings needed 176 = en in "genie" and 34 = ee in "agee";
  176 = ni since RUN2-PAG (4 S tokens elsewhere). With 87 de (H) left and 176 ni right, "de genie" needs 116 = ge (f66R 284, S),
  and RUN2-PAG's demotion of 176 at f66R 285 (made for this conflict only) is lifted (S). The other three are M: "Visage" (f66L 90,
  245/220/214 all M around it), "agee" (f66L 368, 30 and 34 M), "Mariage" (f66R 101, pair end, but 30 a M and 213 ma (C) reads
  against the gloss -- Gibbs gives 213 = ri there). Key 116: g (C) -> ge (M, unsettled per token).
- **Decode** `python3 tools/decode_key.py ciphers/clairambault1225-paget-1714 --check`: `ciphertext.tsv: tokens 505: H 62, I 7, M 356,
  S 74, U 6` / `reading up to date`, exit 0. Per token (rule 4): **H 64 -> 62, C 0, S 71 -> 74, M 357 -> 356, I 7, U 6** of 505; firm 136.
  Six tokens changed: f61L 147 ab -> b (M -> S); f66L 90 g -> ge (M); f66L 368 g -> ge (H -> M: its H rested on the vote "g", which
  needs 34 = ee); f66R 101 g -> ge (M); f66R 284 g -> ge (H -> S); f66R 285 ni (M -> S). `align/settle7.py --check`: up to date,
  43 S rulings in exceptions.tsv. tools/tests/test_decode_key.py: the same 3 failures as before (antt-linhares-chave,
  rah-canada-1869), none in this folder.
- The RUN2 state audited by A3V-VPAG and re-derived by A3V-RD117P has changed in these six tokens: a rule-7 re-derivation of the new
  state is owed (not done here).
- Found in passing, not settled (Usage 7): 213 = ma at grade C reads against "Mariage" (155 ma H sits before it; Gibbs gives 213 = ri).
- Requests: none. Subagents: none.

## N4-PAG213 (4 Oct 2026): code 213 settled per token

Brief: `.claude/briefs/runs/2026-10-04-ytbiz-near4-wave2.md` section N4-PAG213 (LANE-NEAR4, account 2). Disk only: no network request,
no vision call, no subagent. Method: `align/settle7.py` extended in place (CODES/GIBBS gain 213; three DEMOTE entries; the 116 "Mariage"
demotion's reason rewritten, ruling unchanged); same S/M rule as RUN2-PAG and N4-PAG65.
- **213**: key.tsv had ma at grade C from interlinear_align 2/4 (others ri:1, s:1). Those two ma readings put 155 on "pas"/"le", although
  155 = ma is H (4/7); with 155 = ma, 213 = ma reads "mama". The per-letter seed-0 Gibbs run (the run that passed PREREG_seg2.md held-out)
  gives 213 = ri at all four occurrences (all letter 2, share 1.00; the pooled run also 4/4), with 155 = ma before it in "Mari", "marie" and
  "Mariage". Key 213: ma (C) -> ri (M, unsettled per token; not held in both letters).
- Per token: f66L 276 "son Mari epousa" S (155 ma H on the left, the gloss word ends at "Mari"); f66L 134 "d'Esprit" M (right end pinned
  by 47 t S and 52 et H, left 96/43 both M, "ri" vs "pri" open); f66R 84 "marie" M ("rie" over 213 + 34, 34 M with 17 values); f66R 99
  "Mariage" M (30 a and 116 ge both M on the right).
- **Decode** `python3 tools/decode_key.py ciphers/clairambault1225-paget-1714 --check`: `ciphertext.tsv: tokens 505: H 60, I 7, M 357,
  S 75, U 6` / `reading up to date`, exit 0. Per token (rule 4): **H 62 -> 60, C 0, S 74 -> 75, M 356 -> 357, I 7, U 6** of 505; firm 135.
  Four tokens changed value ma -> ri: f66L 134 (M), f66L 276 (M -> S), f66R 84 (H -> M), f66R 99 (H -> M). `align/settle7.py --check`:
  up to date, 44 S rulings in exceptions.tsv; rulings now 10 codes, 44 S, 20 M.
- A rule-7 re-derivation of the new state (N4-PAG65's six tokens plus these four) is owed (not done here).
- Same C-vs-gloss shape, listed, not settled (Usage 7): the per-letter Gibbs run's chunk differs from the key's C value at 126 ch (Gibbs
  he 3/3), 84 ce (ette 2, cet 1, ato 1), 86 da (dame 2, de 1), 77 q (ceq/p/quoi), 158 mo (mils 1, mo 1); C codes where Gibbs agrees: 135 je,
  174 na, 205 qui. 126 is the cleanest next (one value at every occurrence, like 213).
- Requests: none. Subagents: none.

## Remaining gaps (N4-PAG213, 4 Oct 2026)
Read so far: token level H 60, S 75, M 357, I 7, U 6 of 505 (firm 135), tools/decode_key.py --check 4 Oct 2026; 99.2% of tokens lie under a period interlinear gloss read off the images on disk, so the run-level plaintext of both letters' cipher passages is in hand
- Code-level values for the 357 M tokens (mostly single-attestation codes; the 7 Gibbs/hard-EM disagreements plus 65, 116 and 213 are settled per token, 44 S and 20 M, align/settle7_rulings.tsv) - blocker: open-codes; two instruments run (tools/interlinear_align.py; tools/gibbs_align.py, PREREG_seg2.md PASS) and the per-token pass done; a code seen once cannot be held in both letters by either; next: the same per-token reading for the C codes where the per-letter Gibbs chunk differs (126 ch/he first, then 84, 86, 77, 158), ~$1
- f66L 169-172 '400 4 19 600', 4 tokens - blocker: no-key-material; no gloss above this run on images/f66L.jpg, none of the four codes recurs under a gloss; the Marine B7 original waits on LOCAL-QUEUE L11
- f61L, one solid-inked cipher group - blocker: illegible; hand-marked ILLEGIBLE in both passes, its gloss ("on verra quelques personnes a Genes") is read, its code is not; the only other witness is the Marine B7 original (LOCAL-QUEUE L11)

## Escalation (N4-PAG213, 4 Oct 2026)
- [x] siblings: neighbouring leaves f55-f59, f67, f70, f75 opened (OX-PAG); the Paget 1713 sibling is another target's row; no internal sibling step left in this folder
- [x] clear-pages: no separate clear copy; the interlinear decipherment on the images covers 501 of 505 tokens and is used in full
- [x] known-keys: KEY-CROSSMATCH.tsv 45 rows, 28 none, 9 unusable-key, 8 no_corpus; no French Marine or consular key 1700-1729 on file
- [x] print: tools/print_check.py on 16 gloss phrases and 5 keyword sources (A2-PAG, 2 Oct 2026); nothing printed located
- [x] key-rebuild: tools/gibbs_align.py (RUN1-PAG) PASS 0.521/0.681 vs p95 0.066/0.067; per-token rulings RUN2-PAG + N4-PAG65 + N4-PAG213 on 10 codes: 44 S, 20 M; key.tsv 111 codes
- [x] image-check: 81 line crops, 14 blind passes plus reconciliation (A2-PAG2) and the f66L gutter strip (A2-PAG3), all on disk
- [x] retry: tools/decode_key.py --check exit 0 after N4-PAG213: H 60 S 75 M 357 I 7 U 6
Verdict: keep going: 1 internal gaps; cheapest next: the same per-token reading for code 126 (ch, C; per-letter Gibbs he 3/3), then 84, 86, 77, 158, ~$1

## N4-PAG126 (4 Oct 2026): codes 126, 86, 84, 77, 158 per token

Brief: `.claude/briefs/runs/2026-10-04-ytbiz-near4-wave3.md` section N4-PAG126 (LANE-NEAR4, account 2). Disk only: no network request,
no vision call, no subagent. Method: `align/settle7.py` extended in place (CODES/GIBBS gain the five codes; two DEMOTE entries for 126);
same S/M rule as RUN2-PAG, N4-PAG65 and N4-PAG213 (S only where the token's own per-letter seed-0 Gibbs chunk equals the code value and
the gloss word admits it with firm H/C/S neighbours; else M).
- **126**: key ch (C) -> he (M). Gibbs he 3/3 (share 1.00, pooled 3/3, all letter 2). With 32 = c (S) the old value read "ducchsse"
  under "Duchesse". f66L 10 "achevera" **S** (32 c S left, 244 ve H right pin "he" exactly); f66L 186 and f66R 255 "Duchesse" M (32 c S
  left, but 46 s M before 221 se S: he/s vs h/es not pinned).
- **86**: key da (C) -> dame (M). Gibbs dame under "Madame" at f66L 182 and f66R 251, both **S** (155 ma H left, 145 la S right; the
  old da needed 145 = me against 145 = la S). f66R 338 under the abbreviation "Made" (period short form of Madame): Gibbs de, M.
- **84**: key ce (C) -> ce (M). Gibbs cet / ette / ette / ato, never ce: no token has two instruments agreeing, all four M. Eye note,
  not an instrument: under "cette mere" (f66L 257, 156 me + 212 re after it) and "cette isle" (f61R 34, 38 + 46 + 146 le after it) the
  whole word "cette" would sit on 84; listed, not applied.
- **77**: key q (C) -> q (M). Gibbs ceq / p / quoi (shares 0.39-0.60), never q: all three M.
- **158**: key mo (C) -> mo (M). f66L 143 "modeste" **S** (Gibbs mo 0.96; word start, 87 de H after); f66L 48 "meme mois" M (Gibbs
  mils, share 0.29, the pair has drifted).
- **Decode** `python3 tools/decode_key.py ciphers/clairambault1225-paget-1714 --check`: `ciphertext.tsv: tokens 505: H 50, I 7, M 363,
  S 79, U 6` / `reading up to date`, exit 0. Per token (rule 4): **H 60 -> 50, C 0, S 75 -> 79, M 357 -> 363, I 7, U 6** of 505; firm
  129 (was 135). **12 tokens changed**: 6 values (126 ch -> he x3, 86 da -> dame x3) and grades H -> M 7, H -> S 3, M -> S 1 (f66R 338
  value only, M stays M). `align/settle7.py --check`: up to date, 48 S rulings in exceptions.tsv; rulings now 15 codes, 48 S, 31 M.
- The fall in H is the two-instrument standard applied, not a lost reading: the five codes were C on interlinear_align alone.
- A rule-7 re-derivation of the state after N4-PAG65 + N4-PAG213 + N4-PAG126 is owed (LANE-NEAR4 briefs it; not done here).
- C codes left where Gibbs agrees with the key: 135 je, 174 na, 205 qui (N4-PAG213 list); no other C-vs-Gibbs conflict was listed.
- Requests: none. Subagents: none.

## Remaining gaps (N4-PAG126, 4 Oct 2026)
Read so far: token level H 50, S 79, M 363, I 7, U 6 of 505 (firm 129), tools/decode_key.py --check 4 Oct 2026; 99.2% of tokens lie under a period interlinear gloss read off the images on disk, so the run-level plaintext of both letters' cipher passages is in hand
- Code-level values for the 363 M tokens (mostly single-attestation codes; the 7 Gibbs/hard-EM disagreements plus 65, 116, 213, 126, 86, 84, 77, 158 are settled per token, 48 S and 31 M, align/settle7_rulings.tsv) - blocker: open-codes; two instruments run (tools/interlinear_align.py; tools/gibbs_align.py, PREREG_seg2.md PASS) and the per-token pass done on every listed C-vs-Gibbs code; a code seen once cannot be held in both letters by either; next: rule-7 re-derivation of the N4-PAG65/213/126 state (LANE-NEAR4), then audit, ~$2
- f66L 169-172 '400 4 19 600', 4 tokens - blocker: no-key-material; no gloss above this run on images/f66L.jpg, none of the four codes recurs under a gloss; the Marine B7 original waits on LOCAL-QUEUE L11
- f61L, one solid-inked cipher group - blocker: illegible; hand-marked ILLEGIBLE in both passes, its gloss ("on verra quelques personnes a Genes") is read, its code is not; the only other witness is the Marine B7 original (LOCAL-QUEUE L11)

## Escalation (N4-PAG126, 4 Oct 2026)
- [x] siblings: neighbouring leaves f55-f59, f67, f70, f75 opened (OX-PAG); the Paget 1713 sibling is another target's row; no internal sibling step left in this folder
- [x] clear-pages: no separate clear copy; the interlinear decipherment on the images covers 501 of 505 tokens and is used in full
- [x] known-keys: KEY-CROSSMATCH.tsv 45 rows, 28 none, 9 unusable-key, 8 no_corpus; no French Marine or consular key 1700-1729 on file
- [x] print: tools/print_check.py on 16 gloss phrases and 5 keyword sources (A2-PAG, 2 Oct 2026); nothing printed located
- [x] key-rebuild: tools/gibbs_align.py (RUN1-PAG) PASS 0.521/0.681 vs p95 0.066/0.067; per-token rulings RUN2-PAG + N4-PAG65 + N4-PAG213 + N4-PAG126 on 15 codes: 48 S, 31 M; key.tsv 111 codes
- [x] image-check: 81 line crops, 14 blind passes plus reconciliation (A2-PAG2) and the f66L gutter strip (A2-PAG3), all on disk
- [x] retry: tools/decode_key.py --check exit 0 after N4-PAG126: H 50 S 79 M 363 I 7 U 6
Verdict: keep going: 1 internal gaps; cheapest next: rule-7 re-derivation of the N4-PAG65 + N4-PAG213 + N4-PAG126 state (LANE-NEAR4 briefs it), ~$2

## A3V3-PAGR (4 Oct 2026, 06:35-06:5x UTC): per-token rulings on the A3V3-PAGA findings

Brief: `.claude/briefs/runs/2026-10-04-acct3-a3v3-wave2.md` section A3V3-PAGR (LANE-A3V3, account 3). Disk only: no network request,
no vision call, no subagent. Pre-registration `align/PREREG_pagr.md`, pushed as 161fc920 before any run.
- **Gloss transcription fix applied** (PAGA finding 5): `align/build_pairs.py` P23 "ne le meme mois" -> "nee le meme mois" (leaf "née";
  pairs.tsv regenerated, only that row changes). Finding 6 (f66L:189 `20` vs leaf `220`) was **already applied** before this job:
  exceptions.tsv "image reads 220, ciphertext.tsv 20 (image override: NEXT-PAG, A2-PAG2)" and pairs.tsv P28 override 189:20->220.
- **Instrument for findings 1-4 (77 ce, 20 qui, 84 cette, 34 e, 38 i) and 5 (158 mo at f66L:48 back to H)**: `align/pin_pagr.py`, a
  firm-neighbour pin (firm H/C/S tokens of the pre-job reading emit their value; other tokens 0-5 letters; overhang only at pair
  ends; a token is pinned when every complete alignment gives it the same chunk).
  | step | result | gate |
  |---|---|---|
  | 1 known-answer: hide each of the 129 firm tokens | pinned 11 (coverage 0.085), right 11/11 (accuracy 1.000) | >= 0.90 on >= 20 pinned: **FAIL** (too few pinned) |
  | 2 shuffled-value null, 200 seeds | target T = 1 proposal token pinned to its proposal (34 e at f66R:13); shuffle mean 0.00, p95 0, max 0; known-answer accuracy under shuffle 0.000 | T > p95: PASS |
  Step 1 failed, so by the pre-registration **no proposal is ruled S/H by this instrument**: every token stays M at its key value,
  logged as untested by this instrument at this firm density (25.5% of tokens firm: a token is almost never boxed in by firm
  tokens on both sides). Descriptive only (`align/pin_pagr_rulings.tsv`): the proposal is *not admitted* at 4 tokens -- 84 cette at
  f66R:272 (candidates a/at/ato/o/t/to, as PAGA suspected), 34 e at f61L:165 ("Lisle": i/is/l/li/lis/s), 38 i at f66L:319 (eg/reg...);
  admitted elsewhere, pinned only at f66R:13. Values in key.tsv unchanged (77 q, 20 ui, 84 ce, 34 de, 38 a, all M).
- **Consequence of the gloss fix through settle7.py** (its --check went STALE, as it re-runs the seed-0 per-letter Gibbs sampler on
  pairs.tsv): regenerated by its own unchanged rule. Four rulings move: **158 f66L:48 M -> S** (own Gibbs chunk now mo; seeds 0-9: mo
  10/10, was mils 10/10 on the misread gloss -- the fix removes the drift PAGA saw), **126 f66L:10 S -> M** (seed-0 chunk e), **86
  f66L:182 and f66R:251 S -> M** (seed-0 chunk ame). Seed spread on the corrected pairs, seeds 0-9: 126 he 5/10 (e 4, h 1) at all three
  occurrences (was he 9/10); 86 dame 6/10 (ame 2, da 1, dam 1) (was 9/10). So the 126/86 S rulings rested on one seed path that a
  one-letter gloss correction elsewhere in the letter changes; a multi-seed version of the settle7 rule would be a different
  instrument (suggestion for the lane, not done: Usage 7). exceptions.tsv: three S rows removed (values he/dame unchanged = key
  values, grade M), one S row added (f66L 48 mo). PAGA's "back to H" for 158 is not given: the pin did not pin it (66 candidates), and
  settle7's rule gives S, its maximum.
- **Counts** `python3 tools/decode_key.py ciphers/clairambault1225-paget-1714 --check`: `tokens 505: H 50, I 7, M 365, S 77, U 6` /
  `reading up to date`, exit 0. Per token (rule 4): **H 50 -> 50, C 0, S 79 -> 77, M 363 -> 365, I 7, U 6**; firm 129 -> 127 (25.1%).
  No token's value text changed (only grades). `align/settle7.py --check`: up to date, 46 S rulings (was 48 S / 30 M, now 46 S / 32 M).
  `align/pin_pagr.py --check`: up to date.
- Pre-existing, not from this job: `align/build_votes.py --check` (STALE exceptions.tsv) and `align/make_key.py --check` (exit 1) both
  fail at 161fc920 already (checked in a clean worktree): the settle7 rows and key edits since RUN2-PAG were made after those
  generators; they are no longer the source of truth for exceptions.tsv/key.tsv.
- **Held-out Gibbs pass re-run on the corrected pairs** (`align/gibbs_pass.py`, PREREG_seg2.md settings unchanged; its --check was
  STALE after the gloss fix): control PASS (0.810/0.747, recovery 0.974; was 0.808/0.731, 0.980); target L1->L2 106/210 = 0.505 vs
  shuffle p95 0.060, L2->L1 47/65 = 0.723 vs p95 0.071 -> **PASS** (was 0.521/0.681); 18 codes both directions vs p95 1 (unchanged).
  gibbs_codes.tsv: **97 en is no longer held in both letters**, 240 ion now is (already H in key.tsv, nothing to promote). settle7.py's
  GIBBS value for 97 cites gibbs_codes.tsv; its 2 S tokens (still own-chunk en under settle7's rule) now rest on a per-letter value only,
  like 65/116/213 -- flagged for the lane, not changed here (Usage 7).
- **rule-7 owed after A3V3-PAGR**: a fresh session re-derives this state (not done here, per the brief).
- Requests: none. Subagents: none.

## Remaining gaps (A3V3-PAGR, 4 Oct 2026)
Read so far: token level H 50, S 77, M 365, I 7, U 6 of 505 (firm 127), tools/decode_key.py --check 4 Oct 2026; 99.2% of tokens lie under a period interlinear gloss read off the images on disk, so the run-level plaintext of both letters' cipher passages is in hand
- Code-level values for the 365 M tokens (mostly single-attestation codes; settle7 rulings 46 S / 32 M on 15 codes; PAGA's eye readings 77 ce, 84 cette, 34 e, 38 i untested by the firm-neighbour pin, align/pin_pagr.txt known-answer FAIL 11 pinned) - blocker: open-codes; three instruments run (tools/interlinear_align.py; tools/gibbs_align.py, PREREG_seg2.md PASS; the pin, PREREG_pagr.md FAIL) and the per-token pass done; next: rule-7 re-derivation of the A3V3-PAGR state, then a multi-seed settle7 rule (the 126/86 rulings are seed-path dependent), ~$2
- f66L 169-172 '400 4 19 600', 4 tokens - blocker: no-key-material; no gloss above this run on images/f66L.jpg, none of the four codes recurs under a gloss; the Marine B7 original waits on LOCAL-QUEUE L11
- f61L, one solid-inked cipher group - blocker: illegible; hand-marked ILLEGIBLE in both passes, its gloss ("on verra quelques personnes a Genes") is read, its code is not; the only other witness is the Marine B7 original (LOCAL-QUEUE L11)

## Escalation (A3V3-PAGR, 4 Oct 2026)
- [x] siblings: neighbouring leaves f55-f59, f67, f70, f75 opened (OX-PAG); the Paget 1713 sibling is another target's row; no internal sibling step left in this folder
- [x] clear-pages: no separate clear copy; the interlinear decipherment on the images covers 501 of 505 tokens and is used in full
- [x] known-keys: KEY-CROSSMATCH.tsv 45 rows, 28 none, 9 unusable-key, 8 no_corpus; no French Marine or consular key 1700-1729 on file
- [x] print: tools/print_check.py on 16 gloss phrases and 5 keyword sources (A2-PAG, 2 Oct 2026); nothing printed located
- [x] key-rebuild: tools/gibbs_align.py (RUN1-PAG) PASS; per-token settle7 rulings on 15 codes 46 S / 32 M after the P23 gloss fix; firm-neighbour pin (A3V3-PAGR) known-answer FAIL, no ruling; key.tsv 111 codes
- [x] image-check: 81 line crops, 14 blind passes plus reconciliation (A2-PAG2) and the f66L gutter strip (A2-PAG3), all on disk; P23 gloss "nee" corrected from the leaf (A3V3-PAGA)
- [x] retry: tools/decode_key.py --check exit 0 after A3V3-PAGR: H 50 S 77 M 365 I 7 U 6
Verdict: keep going: 1 internal gaps; cheapest next: rule-7 re-derivation of the A3V3-PAGR state (rule-7 owed after A3V3-PAGR), ~$2

## RD7-PAGR (4 Oct 2026, 17:56-18:0x UTC): rule-7 for the A3V3-PAGR state already done
The brief asked for a rule-7 re-derivation of the A3V3-PAGR state. A3V3-PG7 had already done one (531b5754d, 07:36 UTC,
RD7-2026-10-04-a3v3.md): SAME 505/505 at H 50 S 77 M 365 I 7 U 6. It had not updated the Verdict above, which still read
"rule-7 owed". No folder commit since 531b5754d; `tools/decode_key.py --check` exit 0 at 17:58 UTC with the same counts. No
second run was made (deterministic chain, unchanged state). Note: RD7-2026-10-04-pagr.md.

## Remaining gaps (RD7-PAGR, 4 Oct 2026)
Read so far: token level H 50, S 77, M 365, I 7, U 6 of 505 (firm 127), tools/decode_key.py --check 4 Oct 2026; 99.2% of tokens lie under a period interlinear gloss read off the images on disk, so the run-level plaintext of both letters' cipher passages is in hand
- Code-level values for the 365 M tokens (mostly single-attestation codes; settle7 rulings 46 S / 32 M on 15 codes; PAGA's eye readings 77 ce, 84 cette, 34 e, 38 i untested by the firm-neighbour pin, align/pin_pagr.txt known-answer FAIL 11 pinned) - blocker: open-codes; three instruments run (tools/interlinear_align.py; tools/gibbs_align.py, PREREG_seg2.md PASS; the pin, PREREG_pagr.md FAIL) and the per-token pass done; rule-7 re-derivation of the A3V3-PAGR state done (A3V3-PG7, SAME 505/505); next: a multi-seed settle7 rule (the 126/86 rulings are seed-path dependent, PG7 reproduced he 5/10, dame 6/10), pre-registered, then rule-7 again, ~$2
- f66L 169-172 '400 4 19 600', 4 tokens - blocker: no-key-material; no gloss above this run on images/f66L.jpg, none of the four codes recurs under a gloss; the Marine B7 original waits on LOCAL-QUEUE L11
- f61L, one solid-inked cipher group - blocker: illegible; hand-marked ILLEGIBLE in both passes, its gloss ("on verra quelques personnes a Genes") is read, its code is not; the only other witness is the Marine B7 original (LOCAL-QUEUE L11)

## Escalation (RD7-PAGR, 4 Oct 2026)
- [x] siblings: neighbouring leaves f55-f59, f67, f70, f75 opened (OX-PAG); the Paget 1713 sibling is another target's row; no internal sibling step left in this folder
- [x] clear-pages: no separate clear copy; the interlinear decipherment on the images covers 501 of 505 tokens and is used in full
- [x] known-keys: KEY-CROSSMATCH.tsv 45 rows, 28 none, 9 unusable-key, 8 no_corpus; no French Marine or consular key 1700-1729 on file
- [x] print: tools/print_check.py on 16 gloss phrases and 5 keyword sources (A2-PAG, 2 Oct 2026); nothing printed located
- [x] key-rebuild: tools/gibbs_align.py (RUN1-PAG) PASS; per-token settle7 rulings on 15 codes 46 S / 32 M after the P23 gloss fix; firm-neighbour pin (A3V3-PAGR) known-answer FAIL, no ruling; key.tsv 111 codes
- [x] image-check: 81 line crops, 14 blind passes plus reconciliation (A2-PAG2) and the f66L gutter strip (A2-PAG3), all on disk; P23 gloss "nee" corrected from the leaf (A3V3-PAGA)
- [x] retry: tools/decode_key.py --check exit 0 after A3V3-PAGR: H 50 S 77 M 365 I 7 U 6; rule-7 re-derivation by A3V3-PG7 (531b5754d, RD7-2026-10-04-a3v3.md) SAME 505/505, state unchanged at 17:58 UTC (RD7-PAGR)
Verdict: keep going: 1 internal gaps; cheapest next: a multi-seed settle7 rule for the seed-path-dependent 126/86 rulings (pre-registered, then rule-7 again), ~$2

## Desk runner 4 Oct 2026 (DESK-LAND, account-3 worker; JSTOR rows J18-J21)

Source: the owner's browser runner, outreach/local-runner/DESK-2026-10-04.md. The four JSTOR rows AUDIT 1 queued on 4 Oct 2026
(AUDIT.md line ~142) are answered in JSTOR-QUEUE.tsv:

| row | query | hits | relevant |
|---|---|---|---|
| J18 | "Paget" AND ("Gênes" OR "Genoa" OR "Cagliari") AND 1714 AND (chiffre OR cipher OR consul) | 169 | no -- reference works and directories (top: Dictionary of World Biography 2016) |
| J19 | "Paget" AND ("princesse de Parme" OR "Farnese") AND (consul OR chiffre) | 58 | no -- periodical digests (top: Revue Historique 1896 "Recueils périodiques"), no Paget/Genoa match shown |
| J20 | "a toujours esté de genie Allemand" | 0 | -- |
| J21 | "le Prince Antoine de Parme" "35 ans" | 0 | -- |

Search results, not a novelty verdict (rule 10); for the verifier to carry into AUDIT.md's JSTOR line. No gap or escalation line
changes (the print step was already [x]).
- 5 Oct 2026 (PR-LAND-67): LOCAL-QUEUE L11 answer (PR 67) bounced by tools/lq_answer_check.py (missing holding-catalogue rung: catalogue_ladders.tsv has no Archives nationales/FranceArchives row); row back to queued, answer not landed.

## RUN6-PAGET (5 Oct 2026, 05:02-05:08 UTC by date -u): multi-seed settle7 rule

Brief: `.claude/briefs/runs/2026-10-05-acct1-run6-wave2.md` section RUN6-PAGET (LANE-RUN6, account 1). Disk only: no network
request, no vision call, no subagent. Pre-registration `align/PREREG_settle7ms.md`, pushed as 198aa77e before any run.
- **Rule** (registered, applied to all 15 settle7 codes, 78 rulings): per-letter Gibbs seeds 0..19; S only if the modal chunk
  equals the code value in >= 16/20 seeds and the token is not in DEMOTE; else M. GIBBS values and DEMOTE unchanged.
  `align/settle7.py` now implements it (seed-0 chunk kept as a column; rulings gain `modal_chunk`, `stability`, `seeds_0_19`).
- **126 / 86 (the flagged rulings)**: over 20 seeds 126 he 13/20 (0.65) at all three tokens; 86 dame 13/20 (0.65) at f66L:182 and
  f66R:251; 86 at f66R:338 ("Made") modal de 16/20, not the code value. **None passes; all six stay M** (no grade or value change).
  The seed 0-9 tallies (he 5/10, dame 6/10) were not a seed-0 accident in the other direction: the value is the mode, but not stable.
- **Seed-stable** (modal == seed-0 chunk and >= 16/20): 60 of 78 rulings. Not seed-stable: 18 -- 31 f60R:31, f61L:105, f61L:200
  (b 8/20); 45 f61L:40 (seed-0 r, modal qu 8/20), f66R:203 (desp/esp 7/20); 65 f61L:147 (b 8/20); 97 f66L:51 (cens/en 7/20),
  f66L:289 (seed-0 null, modal en 16/20, DEMOTE stays); the six 126/86 tokens; 84 f61R:34 (cet/ce 11/20), f66R:272 (ato 14/20);
  77 f65L:43 (ceq/ce 14/20), f66L:292 (p/ce 13/20).
- **Grades moved by the rule**: five seed-0 S rulings fail it and go to M, value unchanged (= key value): 31 at f60R:31, f61L:105,
  f61L:200; 45 at f61L:40; 65 at f61L:147. Their five S rows are removed from exceptions.tsv. No M ruling passes into S.
  settle7 now 41 S / 37 M (was 46 S / 32 M); `align/settle7.py --check`: up to date (41 S rulings in exceptions.tsv).
- **Rule 7** `python3 tools/decode_key.py ciphers/clairambault1225-paget-1714` then `--check`: `tokens 505: H 50, I 7, M 370, S 72,
  U 6` / `reading up to date`, exit 0. Per token (rule 4): **H 50, C 0, S 77 -> 72, M 365 -> 370, I 7, U 6**; firm 127 -> 122
  (24.2%). No token's value text changed (5 grades only). The "Labbe" codes 31/65 and the f61L:40 token are the whole loss: the L1
  letter's sampler mixes between b/ab-type segmentations seed to seed.
- Not run: `align/pin_pagr.py --check` fails in this container before any comparison (`git show 4b518e74:...` -- the clone is
  shallow, the object is absent); environment, not a result. A fresh rule-7 re-derivation by a separate session is owed for this
  state (orchestrator's step). Requests: none. Subagents: none.

## RUN6-PAGETR7 (5 Oct 2026, 05:22-05:24 UTC by date -u): rule-7 fresh-session re-derivation

Fresh session, not RUN6-PAGET's; worked from spec + key only, at HEAD 12d15aaef after `git fetch --unshallow origin main`.
- `python3 tools/decode_key.py ciphers/clairambault1225-paget-1714 --check`: "tokens 505: H 50, I 7, M 370, S 72, U 6 / reading up to date", exit 0.
- `python3 ciphers/clairambault1225-paget-1714/align/pin_pagr.py --check`: "pin_pagr up to date (0 S/H rulings in exceptions.tsv)", exit 0.
- Independent regeneration into a scratch copy of the folder (reading.txt and reading_tokens.tsv deleted first, then `decode_key.py` without --check): reading.txt byte-identical; reading_tokens.tsv 0 differing rows.
Verdict: **SAME**. Differing tokens beyond M: 0. No grade changes.

## Remaining gaps (RUN6-PAGET, 5 Oct 2026)
Read so far: token level H 50, S 72, M 370, I 7, U 6 of 505 (firm 122), tools/decode_key.py --check 5 Oct 2026; 99.2% of tokens lie under a period interlinear gloss read off the images on disk, so the run-level plaintext of both letters' cipher passages is in hand
- Code-level values for the 370 M tokens (mostly single-attestation codes; settle7 multi-seed rulings 41 S / 37 M on 15 codes, 18 of 78 rulings not seed-stable; PAGA's eye readings 77 ce, 84 cette, 34 e, 38 i untested by the firm-neighbour pin) - blocker: open-codes; four instruments run (tools/interlinear_align.py; tools/gibbs_align.py, PREREG_seg2.md PASS; the pin, PREREG_pagr.md FAIL; multi-seed settle7, PREREG_settle7ms.md); next: fresh-session rule-7 re-derivation of the RUN6-PAGET state, then audit, ~$2
- f66L 169-172 '400 4 19 600', 4 tokens - blocker: no-key-material; no gloss above this run on images/f66L.jpg, none of the four codes recurs under a gloss; the Marine B7 original waits on LOCAL-QUEUE L11
- f61L, one solid-inked cipher group - blocker: illegible; hand-marked ILLEGIBLE in both passes, its gloss ("on verra quelques personnes a Genes") is read, its code is not; the only other witness is the Marine B7 original (LOCAL-QUEUE L11)

## Escalation (RUN6-PAGET, 5 Oct 2026)
- [x] siblings: neighbouring leaves f55-f59, f67, f70, f75 opened (OX-PAG); the Paget 1713 sibling is another target's row; no internal sibling step left in this folder
- [x] clear-pages: no separate clear copy; the interlinear decipherment on the images covers 501 of 505 tokens and is used in full
- [x] known-keys: KEY-CROSSMATCH.tsv 45 rows, 28 none, 9 unusable-key, 8 no_corpus; no French Marine or consular key 1700-1729 on file
- [x] print: tools/print_check.py on 16 gloss phrases and 5 keyword sources (A2-PAG, 2 Oct 2026); nothing printed located
- [x] key-rebuild: tools/gibbs_align.py (RUN1-PAG) PASS; settle7 per-token rulings now multi-seed (RUN6-PAGET, 20 seeds, >= 16/20): 41 S / 37 M on 15 codes; 126/86 stay M; key.tsv 111 codes
- [x] image-check: 81 line crops, 14 blind passes plus reconciliation (A2-PAG2) and the f66L gutter strip (A2-PAG3), all on disk; P23 gloss "nee" corrected from the leaf (A3V3-PAGA)
- [x] retry: tools/decode_key.py --check exit 0 after RUN6-PAGET: H 50 S 72 M 370 I 7 U 6
Verdict: keep going: 1 internal gaps; cheapest next: fresh-session rule-7 re-derivation of the RUN6-PAGET state, ~$2

## D2-PAGR7 (5 Oct 2026, 23:01-23:1x UTC by date -u): second fresh-session rule-7 re-derivation of the RUN6-PAGET state
Scratch copy, committed reading and align outputs moved aside; settle7.py (20 seeds), decode_key.py, --check, gibbs_pass.py (200 seeds)
re-run as RUN6-PAGET's command list gives. settle7.tsv, settle7_rulings.tsv, gibbs_pass.txt, gibbs_codes.tsv, reading.txt and
reading_tokens.tsv all byte-identical; 0 of 505 tokens differ; H 50 S 72 M 370 I 7 U 6. Rule-7 SAME. pin_pagr.py --check not run
(shallow clone; RUN6-PAGETR7 ran it with full history). Commands and table: RD7-2026-10-05-def2.md.

## Remaining gaps (D2-PAGR7, 5 Oct 2026)
Read so far: token level H 50, S 72, M 370, I 7, U 6 of 505 (firm 122), tools/decode_key.py --check 5 Oct 2026 (re-derived twice in fresh sessions, RD7-2026-10-05-def2.md); 99.2% of tokens lie under a period interlinear gloss read off the images on disk, so the run-level plaintext of both letters' cipher passages is in hand
- Code-level values for the 370 M tokens (mostly single-attestation codes; settle7 multi-seed rulings 41 S / 37 M on 15 codes, 18 of 78 rulings not seed-stable; PAGA's eye readings 77 ce, 84 cette, 34 e, 38 i untested by the firm-neighbour pin) - blocker: open-codes; four instruments run (tools/interlinear_align.py; tools/gibbs_align.py, PREREG_seg2.md PASS; the pin, PREREG_pagr.md FAIL; multi-seed settle7, PREREG_settle7ms.md); rule-7 for this state done twice (RUN6-PAGETR7, D2-PAGR7) and AUDIT 2 written (VER1-PAG); next: a fifth instrument or new material for the single-attestation codes (the Marine B7 original, LOCAL-QUEUE L11), ~$2
- f66L 169-172 '400 4 19 600', 4 tokens - blocker: no-key-material; no gloss above this run on images/f66L.jpg, none of the four codes recurs under a gloss; the Marine B7 original waits on LOCAL-QUEUE L11
- f61L, one solid-inked cipher group - blocker: illegible; hand-marked ILLEGIBLE in both passes, its gloss ("on verra quelques personnes a Genes") is read, its code is not; the only other witness is the Marine B7 original (LOCAL-QUEUE L11)

## Escalation (D2-PAGR7, 5 Oct 2026)
- [x] siblings: neighbouring leaves f55-f59, f67, f70, f75 opened (OX-PAG); the Paget 1713 sibling is another target's row; no internal sibling step left in this folder
- [x] clear-pages: no separate clear copy; the interlinear decipherment on the images covers 501 of 505 tokens and is used in full
- [x] known-keys: KEY-CROSSMATCH.tsv 45 rows, 28 none, 9 unusable-key, 8 no_corpus; no French Marine or consular key 1700-1729 on file
- [x] print: tools/print_check.py on 16 gloss phrases and 5 keyword sources (A2-PAG, 2 Oct 2026); nothing printed located
- [x] key-rebuild: tools/gibbs_align.py (RUN1-PAG) PASS, regenerated byte-identical by D2-PAGR7; settle7 multi-seed (RUN6-PAGET, 20 seeds, >= 16/20): 41 S / 37 M on 15 codes; key.tsv 111 codes
- [x] image-check: 81 line crops, 14 blind passes plus reconciliation (A2-PAG2) and the f66L gutter strip (A2-PAG3), all on disk; P23 gloss "nee" corrected from the leaf (A3V3-PAGA)
- [x] retry: tools/decode_key.py --check exit 0; fresh-session re-derivation SAME twice (RUN6-PAGETR7, D2-PAGR7), 0 tokens differ
Verdict: keep going: 1 internal gaps; cheapest next: a fifth instrument or new material for the single-attestation codes, ~$2
