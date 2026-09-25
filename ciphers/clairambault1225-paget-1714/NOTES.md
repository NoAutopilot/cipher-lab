partial

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
