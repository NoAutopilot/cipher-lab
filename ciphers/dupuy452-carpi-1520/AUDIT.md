# AUDIT: Raince to Madame [Louise de Savoie], Rome, 25 Oct 1525 (BnF Dupuy 452 ff.28r-29v)

Verifier session, 24 Sept 2026, 01:19-01:22 UTC (`date -u` read at start). Sonnet, cap $4, no subagents.
Orchestrator: session_01SepNMpYrr6L2EwqL43aTnm. This is a separate session from the solver's
(commit ae97605); it did not write reading.txt, key.tsv, ciphertext.txt or decode.py and does not
protect their conclusions.

**Claim under audit** (solver, commit ae97605, NOTES.md "Solver: the 1526 key applied" section, and
the ROOM.md flag line of 00:59 UTC): "the letter reads with Tomokiyo's 1526 Raince key (H 5,281 /
C 77 / M 355 / U 12 of 5,725), and its plaintext is printed in Jacqueton, *La politique extérieure
de Louise de Savoie* (1892), P.J. XXXIII pp.366-370, from the decipherment at f.31; our reading
agrees with it on 87% of letters."

## 1. Item extract

- **Date / sender / recipient / place:** 25 October 1525, Nicolas Raince (secrétaire de l'ambassade
  de France à Rome) to "Madame" [Louise de Savoie], written from Rome.
- **Plaintext as read:** `reading.txt` (5,725 tokens, decoded by `decode.py` from `ciphertext.txt` +
  `key.tsv`; grades H 5,281 / C 77 / M 355 / U 12, no I).
- **Ciphertext:** `ciphertext.txt` (BnF Dupuy 452, ff.28r-29v; Gallica `ark:/12148/btv1b10036146c`).
- **Distinctive phrases:** listed and checked in §2 below.
- **Archive identifiers:** BnF Dupuy 452 (Gallica ark above; finding aid
  `archivesetmanuscrits.bnf.fr/ark:/12148/cc885911`); archive.org `lapolitiqueext00jacquoft`.
- **What the solver searched (from NOTES.md, "Solver" section, 24 Sept):** Google Books API, keyed,
  6 queries, phrase search "Raince" "Madame" 1525; archive.org, 3 fetches (Champollion djvu,
  advancedsearch, Jacqueton djvu, full text read once); github.com, 1 shallow clone (Bourdeau's repo,
  for the key image only, not re-searched for prior Dupuy 452 mentions). No Gallica in this pass.
  This built on three earlier sweeps in the same file (23 Sept check-solved, print check/class gate,
  and the 23 Sept transcription pass), which had searched Champollion-Figeac (1847), Tomokiyo's
  `francis.htm`, Bourdeau's and Aymeloglu's repositories, and DECODE's cached catalogue, and found
  nothing there — **but had not searched Jacqueton (1892)**, the edition that turns out to carry the
  plaintext.

## 2. Independent search (this session)

**(a) Canonical series / documentary editions for the period.** Jacqueton, *La politique extérieure
de Louise de Savoie: relations diplomatiques de la France et de l'Angleterre pendant la captivité de
François Ier (1525-1526)* (Paris: É. Bouillon, 1892) is itself the standard documentary edition for
this exact correspondence and window; confirmed genuine and correctly identified: fetched
`archive.org/metadata/lapolitiqueext00jacquoft` directly (not reused from the solver's cache) —
title, date (1892), publisher (É. Bouillon, Paris) all match. **Correction:** the author is
**Gilbert Jacqueton** (archive.org creator field: "Jacqueton, Gilbert, 1864-"), not "P. Jacqueton" as
NOTES.md line 490 has it — a citation slip, corrected below, not a rule-10 issue but relevant to any
future outreach citation (rule 8, Outreach gate 6).

**(b)/(c) The print itself, read independently.** Re-fetched the relevant excerpt already saved at
`print/jacqueton1892_PJ33.txt` and read it in full (not just the passages the solver quoted). It is
headed "XXXIII. — 25 OCTOBRE 1525", "Nicolas Raince à Madame", and states explicitly: **"B. N. ms.
Dupuy 452, f° 28 et 31. — Original chiffré au f° 28 et déchiffrement au f° 31."** This is an exact
match on shelfmark, folio numbers (28 for the cipher, matching `ciphertext.txt`'s own source leaves,
and 31 for a contemporary decipherment), sender, recipient, date and place. The heading line, quoted
verbatim as required by the brief:

> B. N. ms. Dupuy 452, f° 28 et 31. — Original chiffré an f° 28 et déchiffrement au f° 31.
> (OCR renders "au" as "an" in the first instance; the second instance OCRs correctly as "au".)

**Five distinctive phrases, checked by eye against `reading.txt` (decoded French run together, word
signs in brackets, `<cross4>` unsettled):**

1. Print: "vous verrez par ce que l'on escript (1) du bon tour que faict le marquis de Pesquère à
   ceulx qui s'estoyent trop fiez de luy" ↔ reading.txt f28r 12: "dubontourfaictpar[marquis de
   Pesquère]aceulxqui" + f28r 13 "sesonttropfiezdeluy...". Match, including the editor's own footnote
   marker "(1) Commencement du chiffre" falling exactly at the reading's own cipher start.
2. Print: "qui est de cinq cens mil ducatz qu'il leur vouloit payer" ↔ reading.txt f28v 35-36:
   "quiestdecinqcensmilducatzquitdeuruouxoitpayer". Match.
3. Print: "cinquante voilles par mer et une armée de trente mil combatans par terre là où il leur
   plairoit" ↔ reading.txt f29r 01-02: "...decinquanteuoixesparmeretune armeedetrantemil[con]batantz
   parterelaouilleurplairoit". Match (uoixes~voilles, batantz~combatans — consistent with the
   transcription's own known q/ρ and homophone-merger noise already logged in NOTES.md).
4. Print: "les Espaignolz avoyent demandé au duc de Bar estre saisiz de la ville et chasteau de
   Crémonne pour l'Empereur" ↔ reading.txt f28r 30-31: "lesespaignolzauoyentdemandeau[duc de
   Bar]sestresaisyzdelauixeetcyasteaudecremonepour[l'empereur]". Match (uixe~ville, cyaste~chasteau,
   consistent with the reading's documented y/h-merge convention where "cy" stands for "ch").
5. Print: "Madame, ce jourd'huy matin, estant allé vers nostre sainct Père" ↔ reading.txt f28r 26:
   "[Madame]ceiourdyuymatinestantaxedeuers[le pape]". Match ("axe" for "allé", "le pape" as a word
   sign standing in for "nostre sainct Père" — a paraphrase-level rather than letter-level match, but
   the same clause in the same place).

All five land at the same place in both texts, in the same order, with the same surrounding content.
Combined with the reproducible `compare_print.py` letter-agreement figure (re-run this session:
`reading letters 5605, print letters 5973, common 5211 (87.2%), ratio 0.900` — reproduces the
solver's claimed 87.2% exactly), this independently confirms the reading and the print are the same
letter, not a coincidental partial match.

**(d) Holding archive's own catalogue.** Fetched `archivesetmanuscrits.bnf.fr/ark:/12148/cc885911`
fresh (not reused from the 23 Sept cache) and located the volume's item-list text:

> ... 1525, autogr., presque entièrement en chiffres (28) ; — [par le même ?], s. d. (31) ; — par «
> el vescovo de Baieux » ...

This confirms **f.31 exists as a listed item in the same volume** (undated, "[by the same
person?]", i.e. BnF's own catalogue leaves its content and authorship as a query, not stated to be a
decipherment). BnF's own finding aid does **not**, on its own text, identify f.31 as a decipherment —
that identification comes from Jacqueton's edition, which is a scholarly source independent of and
more specific than BnF's catalogue entry (editors of the 1892 edition would have examined the leaf
itself, not just relied on the finding aid, which in any case is a later, retrospective description).
No contradiction: BnF's ambiguity about f.31 and Jacqueton's specific citation of it as the
"déchiffrement" are consistent (the finding aid under-describes the volume's contents in several
other places too, per NOTES.md's own findings on ff.24 and 56/60/72/76). f.31 is on Gallica as part
of the same digitised volume (`ark:/12148/btv1b10036146c`) that already supplied ff.28-29 for the
transcription; its image was **not fetched** this session, per the brief's "without fetching images."

**(e) Full-text search / Google Books / archive.org.** The solver's own Google Books phrase search
("Raince" "Madame" 1525) is what surfaced Jacqueton 1892; independently confirmed the identifier is
real and correctly described (see (a) above) rather than re-running the same Google Books query
(would cost quota for no new information — the hit is verifiable directly from the book's own text,
which this session read in full for the excerpt window).

**(f) Solver repositories and cipher blogs — re-checked independently, not reused from NOTES.md's
citations of its own prior greps.**

- `sources/cryptiana/` (Tomokiyo): grepped all of `sources/cryptiana/web/*.htm` for "dupuy" (case-
  insensitive): hits only in `GL.htm`, `francis.htm`, `danzay.htm`, `louisxiii.htm`, all naming
  **Dupuy 44, 265, 547, 687 or 937** — never 452. Grepped for "jacqueton": **no hit anywhere** in
  `sources/cryptiana/`.
- **Fresh shallow clone of `dbourdeau/cyphersolver`** (HEAD `763a3b98ab1c`, cloned this session, not
  reused from the solver's or NOTES.md's earlier clone): grepped the whole tree for "dupuy" (hits
  only for Dupuy 44/265/547/687/937, as above, none for 452); grepped for "jacqueton" (**no hit**);
  grepped every file containing "1525" for "raince" in the same file (only nav-link cross-references
  in `docs/raince.html`, e.g. "Mellon MS 29 c. 1525", never Dupuy 452 or this letter). The `raince/`
  folder's own files (its 1526 fr.2984/fr.3040/fr.3091 work) contain no "452" and no "1525" anywhere.
- **Fresh shallow clone of `aaymeloglu/unsolved-ciphers`** (HEAD `2495c45e8b94`, cloned this session):
  grepped for "dupuy", "jacqueton", "raince" — **zero hits for all three**, anywhere in the repository.

Confirms, independently of the solver's own greps recorded in NOTES.md's "Solver" and earlier
sections: **neither Tomokiyo, Desenclos (as cited by Tomokiyo), nor either solver repository has ever
connected BnF Dupuy 452 f.28, or Jacqueton's 1892 edition, to Raince's 1526 key or to this letter.**
The 1526 key's applicability to this 1525 letter (same secretary, one year earlier) is this project's
own finding, independent of the print; Jacqueton's edition prints the plaintext but does not carry or
discuss a cipher key.

**(g) JSTOR / Scholar / dissertations.** Not reached this session (out of scope for a $4 Sonnet cap,
and unnecessary once (b)/(c) established a same-item contemporary decipherment already in print — see
classification below). Logged as unreached, not as a negative.

## 3. Classification

- **Prior plaintext:** Yes. Printed in full, Jacqueton 1892, *La politique extérieure de Louise de
  Savoie*, Pièces justificatives XXXIII, pp.366-370. Earliest known citation: 1892.
- **Prior decipherment:** Yes, of this very ciphertext. Jacqueton's edition states it was made "from
  the decipherment at f°31" — a **contemporary (1525-6) decipherment physically in the same
  manuscript volume as the cipher itself**, not a modern cryptanalytic reading. This is not merely
  "the plaintext is known from another source" (which would be N1/N2); it is a decipherment of this
  specific ciphertext, already made, already in the archive, already in print.
- **Evidence quality:** High. Confirmed independently: (i) the archive.org identifier, title, author
  and date are genuine (fetched fresh, not reused); (ii) the print's own heading names this exact
  shelfmark, both folios, sender, recipient and date; (iii) five distinctive phrases land at matching
  positions in both texts; (iv) the reproducible `compare_print.py` script gives 87.2% letter
  agreement on independent re-run; (v) BnF's own finding aid independently confirms f.31 as an item
  in the same volume (though it does not itself state f.31's content, unlike Jacqueton).
- **Confidence:** High.
- **Class: N0** — plaintext and decipherment of this very item already known (rule 10: "N0 plaintext
  and decipherment of this very item already known"). The f.31 leaf is the prior decipherment; the
  Jacqueton 1892 edition is where it was published, 134 years before this project's reading.
- **Safe sentence:** "This project's contribution is a machine-readable key-to-glyph mapping for the
  Carpi/Raince embassy hand, reconstructed independently from the ciphertext image and Tomokiyo's
  published 1526 Raince key, and an independent re-decipherment that agrees with the printed
  plaintext (Jacqueton 1892, from a contemporary decipherment already in the manuscript at f.31) on
  87% of letters; the plaintext and a contemporary decipherment of this specific letter were already
  known and in print before this project began."
- **Unsafe sentence (do not use):** Any claim that this reading is new, unpublished, previously
  unread, a first decipherment or a newly recovered plaintext — all false; a contemporary
  decipherment already exists in the manuscript and has been in print since 1892.

## 4. Postmortem

**What happened.** The 23 Sept "Print check, class gate" section (NOTES.md, lines 254-379) ran a
real, logged search across Champollion-Figeac (1847, full text, multiple spelling variants),
Desenclos (2018) and Tomokiyo's `francis.htm`, WebSearch across several named editions (Guiffrey,
Négociations diplomatiques, Guasti, *Revue d'histoire diplomatique*), and both solver repositories —
but never searched **Jacqueton (1892)**, the actual standard modern edition of exactly this
correspondence (Louise de Savoie's diplomacy during the king's captivity, 1525-26 — the letter's own
subject and years). The gate's own "Other editions" search queries named Guiffrey and Guasti by name
but not Jacqueton, even though Jacqueton's title is the closest possible match to the material (a
monograph specifically on Louise de Savoie's foreign policy in exactly this window) and would likely
have surfaced in a slightly broader WebSearch query (e.g. "Louise de Savoie diplomatie 1525 édition"
rather than author-name-first queries for editions that turned out not to exist). The gate concluded
"best case N3" (NOTES.md line 379) on the strength of that search; the class implied by the gate's
own name ("best case") flagged its own limits, but the sentence still stood unqualified as the class
ceiling in the file until this audit. This repeats, in miniature, the lesson CLAUDE.md rule 10
already records for the Eckert 1864 case (searching the general series but not the sender-specific
edition) — worth restating here since it recurred on a second target in the same repository within
four days.

**Files/sentences corrected by this audit** (see diff): NOTES.md line 379 ("Gate: best case N3;
transcription may proceed.") gets a dated correction appended in place, not a deletion, per the
brief. NOTES.md line 490 ("P. Jacqueton" → "Gilbert Jacqueton", citation accuracy). NOTES.md line 1
status line set to `found-solved`. No other sentence in the folder claims novelty wording needing
correction (the solver's own write-up already avoided "new"/"unpublished"/"first" throughout, per
its own rule-10 discipline — confirmed by grep, see the class-gate section's list of hits above,
none is an over-claim).

**One-line lesson:** the class gate searched the general captivity historiography (Champollion-
Figeac 1847) and the cipher-scholarship pages (Tomokiyo, Bourdeau) but not the specific modern
documentary edition of Louise de Savoie's 1525-26 diplomacy (Jacqueton 1892) — a WebSearch query
naming the correspondent and the exact years, not just the shelfmark or the cipher, would have found
it.

## Requests this session

archive.org: 1 (`metadata/lapolitiqueext00jacquoft`, fresh, not reused). archivesetmanuscrits.bnf.fr:
1 (`ark:/12148/cc885911`, fresh, curl with browser UA, HTTP 200 first try). github.com: 2 shallow
clones (`dbourdeau/cyphersolver`, `aaymeloglu/unsolved-ciphers`), both deleted after grepping, no
files retained. No Gallica images fetched (per brief). No WebSearch used (the print itself, already
on disk, answered every question this audit needed). No logins, no credentials.

Desenclos check, 4 Oct 2026 (DESENCLOS-PREMISE, account 3): no hit. Searched 17 open full texts of the 36 items in sources/desenclos/2026-10-04/bibliography.tsv (HAL PDFs, DSpace Tartu HistoCrypt 2024/2025 PDFs, OpenEdition HTML; built from HAL, theses.fr, OpenAlex, Semantic Scholar, CrossRef, Google Books) for this item's shelfmark, sender/recipient, place and date (terms.tsv, search-log.tsv, search.py); none names this item, its key or its plaintext. Not read: her 2014 thesis (theses.fr: not online) and 2017/2021 cryptography chapters (not open; JSTOR-QUEUE rows of 4 Oct 2026).

## AUDIT 2 (VER1-LOWB, 5 Oct 2026)

Verifier VER1-LOWB (for LANE-VER1, account ytbiz), 5 Oct 2026, 19:03-19:2x UTC by `date -u`. A separate session from Audit 1's
(24 Sept 2026) and from the solver's (commit ae97605); second adversarial audit under CLAUDE.md Outreach gate 2. No decoding;
reading, key and ciphertext unchanged. The task for an N0 item: try to overturn N0 (wrong edition, wrong letter, print of a
different text) and look for an earlier print than the one Audit 1 found.

**Checks, all fresh this session:**
- **The print, re-fetched** (`archive.org/download/lapolitiqueext00jacquoft/..._djvu.txt`, not the folder's `print/` copy):
  Jacqueton 1892, P.J. XXXIII, heading "25 octobre 1525. Nicolas Raince à Madame. B. N. ms. Dupuy 452, f° 28 et 31. --
  Original chiffré au f° 28 et déchiffrement au f° 31. Au dos : A Madame." This is the very item and names a period
  decipherment of it in the same volume. N0 stands.
- **Earlier print?** Jacqueton's own introduction (djvu lines 12428-12452) says Mignet "ne semble pas s'être servi des
  lettres du ms. Dup. 452 que nous donnons dans nos Pièces Justificatives" and that the Italian historians of Morone
  (Müller, Gioda) "n'ont pas connu les dépêches françaises du ms. Dupuy 452"; he cites P.J. XXXIII for the Carpi/Como
  opinion of Pescara. No earlier print was found in any family below; earliest known print stays 1892.
- **Rule 7:** `python3 decode.py --check` -> OK {H 5281, M 355, C 77, U 12}; `python3 compare_print.py` -> 87.2% of print
  letters common, ratio 0.900 (same as Audit 1).

**Search log, 5 Oct 2026** (one request at a time per host, >=1.5 s apart):

| family | status | what | result |
|---|---|---|---|
| Canonical/documentary edition (Jacqueton 1892) | searched | IA djvu, fresh; be-api fts `Raince` in `lapolitiqueext00jacquoft` | prints this item from the f.31 decipherment (N0) |
| Google Books API (keyed, country=US) | searched | `"Nicolas Raince" "Madame" 1525 chiffre`; `"Raince" "Dupuy 452"`; `"Dupuy 452" déchiffrement` | only Jacqueton 1892 (and its EPHE series reissue) prints the letter; Catalogue Dupuy 1899 and the 1868 BnF catalogue are catalogues; Du Bellay Correspondance (1969) cites other Raince letters (Dupuy 452 f.80v, 1530) |
| IA full text (be-api fts) | searched | `"Nicolas Raince" "Dupuy 452"` | endpoint returned a non-JSON error once; not retried (good-citizen rule) |
| OpenAlex (Bearer) | searched | `Raince Louise de Savoie cipher 1525`; `Raince chiffre Rome 1525 Carpi` | 0 |
| Semantic Scholar (x-api-key) | searched | `Raince Louise de Savoie 1525` | 3: a review of Jacqueton 1892, two unrelated |
| HAL API | searched | `Raince 1525 chiffre` | 0 |
| CrossRef | searched | `Raince 1525 chiffre` | no relevant item in top rows (OR-ranked) |
| Persée | searched | `Raince 1525 chiffre` | OR-ranked result list, not discriminating; no item verified |
| Solver repos (shallow clones, grepped, deleted) | searched | `Raince`, `Dupuy 452` in dbourdeau/cyphersolver and aaymeloglu/unsolved-ciphers | Bourdeau lists Raince's 1526 letters (BnF fr.2984, Tomokiyo's 1526 key) and Gallica sweep rows for other Raince letters; no row for Dupuy 452 ff.28-31; Aymeloglu: none |
| Desenclos bibliography | not repeated | covered by DESENCLOS-PREMISE, 4 Oct 2026 (above) | -- |
| JSTOR | queued | 2 rows appended to JSTOR-QUEUE.tsv 5 Oct 2026: family (i) names+date+cipher keyword, family (ii) bare phrase `"aultre opinion que maulvaise"` | pending; does not block the class |

**Classification (Audit 2).**
- **Class N0 upheld.** Key `published` (Tomokiyo's 1526 Raince key, credited). Text `known` (printed 1892 from the period
  decipherment at f.31).
- **Depth D2** (rule 4a). Tokens H 5281 + C 77 = 5358 of 5725 = 93.6% H/C/S; external check = the 1892 print (87.2% letter
  agreement, `compare_print.py`). D3's percentage bar is cleared but its gap condition is not: the 367 unread tokens are mostly
  single cipher letters (333 of 355 M tokens are one-letter values; 10 U are the `<cross4>` sign), not name/code groups, so D2,
  not D3. D3 is reachable if the M letters are settled against the print; that is the solver's step, not this audit's.
- **Depth sentence:** Raince writes that the cardinal of Como and his colleague had never held any but a bad opinion of the man
  and had believed what they were told of him (f.28r lines 17-18, matching Jacqueton's "aultre opinion que maulvaise", which
  he glosses as their view of Pescara).
- **Safe sentence:** "Raince's cipher letter to Louise de Savoie of 25 October 1525 (BnF Dupuy 452 ff.28r-29v) was deciphered
  in its own time (decipherment at f.31) and printed by Jacqueton in 1892 (N0, two audits). Applying Tomokiyo's published 1526
  key to a fresh transcription regenerates that text at 87% letter agreement: an independent re-decipherment of a known text,
  partially deciphered by the depth standard (about 94% of tokens graded)."
- **Unsafe sentence:** "We deciphered / first read Raince's 1525 letter"; "previously unread"; "key recovered".

**Postmortem (Audit 2).** No over-claim found in the folder: NOTES.md status `found-solved`, status.json row `N0` with
`key: published`. The folder name says "carpi-1520" while the item is Raince 1525; that is a naming legacy (the folder also holds
the f.20 Carpi and f.24 transcriptions), recorded here, not renamed. Audit 1's text is left as written.

**depth_check (5 Oct 2026, after the status.json update):** `python3 tools/depth_check.py` -> exit 0; summary line: "unique solves (N3+ and D2+): 16 -- D4 1, D3 2, D2 13; not counted D0/D1: 13; legacy ungraded: 0"
