Pool status: partial (mixed -- see per-row verdicts below; none of the 22 rows is `solved` or `closed-negative`)

CS-4715-POOL, 27 Sept 2026, parent worker for parent 7m (session_01QRJJ2EEfyvp7qtL6m6wufX). Brief:
`.claude/briefs/runs/2026-09-27-parent-ytbiz-cs-4715-pool.md`. Question: is BnF fr.4715's "Vieuville-Nevers
Cipher" group (nevers.htm's own heading) a sign pool (CLAUDE.md Pipeline 3, "pools first": one sender, office
and key family with 2,000+ signs) or is `ciphers/fr4715-montholon-1589` (f.81, no.58 only) a single short
letter. This file does not edit `NOTES.md` (MONT-4715C is appending to it this session).

## What was checked, and where (check-solved order, `.claude/briefs/check-solved.md`)

1. **Web/print source, primary**: `sources/cryptiana/web/nevers.htm` (local mirror, `id=BnFfr4715` anchor, the
   "Vieuville-Nevers Cipher" H4 subsection) and `sources/cryptiana/web/bnf4715.htm` ("Undeciphered Letters in
   BnF fr.4715", per-item `id=noNN` sections), both decoded as cp932 per the file's own declared
   `charset=SHIFT_JIS` (a utf-8 read mojibakes several printed glyphs, INTAKE-4715's finding, reconfirmed here).
2. **The BnF catalogue itself, independently of Tomokiyo**: the full dépouillement (item-by-item description)
   of BnF fr.4715 from `archivesetmanuscrits.bnf.fr` ark:/12148/cc577658, read from a cached copy already fetched
   by `dbourdeau/cyphersolver`'s own crawler (`research/gallica_sweep/notice_cc577658.html`, in that repository's
   git history, a page loaded once by their crawler and inspected here -- **0 fresh requests to
   archivesetmanuscrits.bnf.fr this job**, the notice's full "Fol. N • M ..." item list for every one of the 63
   items in the volume, article numbers matching Tomokiyo's `no.` numbering item-for-item). This is the single
   most informative source this job used: see "The BnF's own status per item" below.
3. **Solver repositories, before any verdict** (rule per this job's brief): fresh shallow clones of
   `github.com/dbourdeau/cyphersolver` and `github.com/aaymeloglu/unsolved-ciphers` into the scratchpad, grepped
   for `4715|Montholon|Vieuville|Trespigny|btv1b52509819x` and the folio numbers. Results below.
4. **DECODE** (`sources/decode/records-non-decrypted-2026-09-24.tsv`, `records-decrypted-2026-09-24.tsv`, the
   24 Sept 2026 cached crawl of every Cipher-type record, Non-decrypted + Partially decrypted + Decrypted): no
   row's holder field matches "fr.4715" / "Français 4715" and no row's holder/notes match Montholon, Vieuville
   or Trespigny (the three rows that do match "vieuville" are BnF fr.3975 f.101/f.30/f.28, a different volume,
   already the subject of Bourdeau's own `targets/vieuville1587/` -- not this pool). A no-hit search result
   (rule 10), not re-crawled live this job (the cache is 3 days old and DECODE's own crawl method,
   `sources/decode/NOTES.md`, needs no login and is unlikely to have changed for this volume).
5. **CATALOG.md / LESSONS-LASRY.md**: row 91, "BnF fr.4715 no.62 (f.85) | c.1590 | Partial (Lasry 2022,
   interim) | BnF fr.4715 | bnf4715.htm". Confirmed against `bnf4715.htm#no62`: "In 2022, George Lasry achieved
   interim results ([text](BnFfr4715f85decryption.txt))." **no.62 (f.85) is NOT in the Vieuville-Nevers Cipher
   list** -- bnf4715.htm never names a cipher family for no.62, and nevers.htm's Vieuville-Nevers section does
   not include it. It is adjacent context (same volume, Lasry's own interim, unrelated cipher), not a pool row.
6. **Phrase search** (Google Books `&country=US&key=$GOOGLE_BOOKS_KEY`, be-api fts) on Tomokiyo's printed
   glosses for no.3/no.6: `"la despence inutille"` (no.3) and `"aujourdhuy tresiesme"` (no.3) both **0
   totalItems** on Google Books (2 calls); be-api fts (not an exact-phrase engine by default -- it token-matches
   and ranks by relevance, confirmed by inspecting the raw response: 807 hits for "despence"/"inutille"
   separately, none with the two words adjacent in a highlight) found no source printing the phrase as a unit (1
   call, not repeated once the tool's own behaviour was understood). A no-hit search result (rule 10), not a
   novelty verdict -- and out of scope for this job anyway: no.3 is `found-solved` (below), so novelty of *our*
   contribution there is moot; this was run because the brief named it explicitly.

## The BnF's own status per item (the main finding)

The BnF cataloguer's own 19th/20th-century dépouillement marks each item with **"Chiffre et déchiffrement"**
(ciphered, and a decipherment already exists -- interlinear or bound in) or **"Chiffre non déchiffré"** /
**"en partie déchiffrée"** (undeciphered / partially deciphered), independently of anything Tomokiyo has
written up. nevers.htm's own "Vieuville-Nevers Cipher" list only flags three items by name as "Undeciphered"
(no.27, no.58, no.60); it is silent on the other nineteen, which reads as "nothing to report" but is not --
the BnF's own notice says several of the silent ones already carry a period decipherment and several others
are only partly read. This matters directly for the pool question: **more than half of the 22-item list the
Vieuville-Nevers heading names is not open cryptanalytic material at all.**

| no. (folio) | sender/date (nevers.htm) | Tomokiyo status sentence (verbatim, cp932-decoded) | BnF dépouillement (verbatim French; art. no. matches Tomokiyo's `no.`) | Verdict |
|---|---|---|---|---|
| 3 (f.3, spans f.3-18 per the BnF item) | Robert de la Vieuville and Duke of Nevers | *(no flag; HTML-comment-only partial group dump, "aujourdhuy tresiesme", "la despence inutille")* | "Fragments d'une correspondance en chiffre de ROBERT DE LA VIEUVILLE avec le duc de Nevers... **Déchiffrement interlinéaire.**" | **found-solved** -- period interlinear decipherment on the leaves themselves; multi-folio (f.3-18), not one leaf |
| 6 (f.24) | Vieuville to Duke of Nevers, 3 July 1589 | *(no flag)* | "Lettre en chiffre, **avec déchiffrement**, de ROBERT DE LA VIEUVILLE au duc de Nevers. Sy, 3 juillet 1589." | **found-solved** |
| 10 (f.28) | Vieuville to Duke of Nevers, Sy, 22 Aug 1589 | *(HTML comment: contains a copy of two Trespigny letters)* | "Lettre en chiffre, **avec déchiffrement**... Cette lettre contient la transcription de deux lettres adressées audit Sr de La Vieuville par le Sr DE TRESPIGNY." | **found-solved** |
| 12 (f.30, spans f.30-32bis) | Vieuville to Duke of Nevers | *(HTML comment gives a partial group dump reading as clear French)* | "Fragments d'une correspondance en chiffre de ROBERT DE LA VIEUVILLE... **Déchiffrement interlinéaire.**" -- the BnF notice itself quotes the plaintext in full ("Par celle que je vous ay escripte par le Sr Simonet...") | **found-solved** -- plaintext is published on the BnF's own public finding-aid page, quoted above |
| 21 (f.44) | **Jerome de Montholon**, Sr de Perousseaux (distinct from the "Sr de Montholon" of the other rows -- see caveat below), 21 Oct 1589 | "Montholon was 'conseiller au conseil d'Etat et au parlement'." (no Undeciphered flag) | "Lettre, avec chiffre, **en partie déchiffrée**, écrite de Tours..." | **partial** (open remainder) |
| 27 (f.50) | Letter of Montholon, 30 Oct 1589 | "Undeciphered. Partially deciphered in [bnf4715.htm]." Opening given, ends in an explicit "...". | "Lettres du Sr DE MONTHOLON. **En chiffre, en grande partie, avec déchiffrement de quelques passages seulement.**" (combined entry with no.28) | **partial** (existing folder's crib) |
| 28 (f.51) | Letter of Montholon, Tours, 3 Dec 1589 | *(bare title, no bnf4715.htm section -- no known-plaintext crib at all)* | same combined entry as no.27 | **open** (no crib on file; BnF says largely cipher, a few passages only) |
| 35 (f.58) | Montholon, Tours, 26 Nov 1589 | *(no flag -- reads as "nothing wrong" but isn't)* | "Lettre, avec chiffre, **en partie déchiffrée**, du Sr DE MONTHOLON. Tours, 26 novembre 1589." | **open/partial** (BnF says partial; Tomokiyo gives no crib for it) |
| 37 (f.60) | Letter of Montholon, Tours, 12 Dec 1589 | *(no flag)* | "Lettre avec chiffre, **en partie déchiffrée**, du Sr DE MONTHOLON. Tours, 12 décembre 1589." | **open/partial** (no Tomokiyo crib; image sampled, see Pool size) |
| 39 (f.62) | Montholon, Tours, 17 Dec 1589 | *(no flag)* | "Lettre du Sr DE MONTHOLON, avec chiffre, **en partie déchiffrée**. Tours, 17 décembre 1589." | **open/partial** |
| 41 (f.64) | Letter of Vieuville | *(no flag)* | "Lettre et fin de lettre de ROBERT DE LA VIEUVILLE." -- **no "chiffre" word at all**, unlike every other row | **flag, not scored** -- BnF's own silence on cipher here matches its phrasing for the letters Tomokiyo privately marked "plaintext only" elsewhere on the same page (no.31/32/34/40); this may not be ciphertext. Needs an image check before treating as pool material. |
| 42 (f.65) | Letter and end of a letter of Vieuville | *(no flag)* | same combined entry as no.41, same absence of "chiffre" | **flag, not scored** (same caveat) |
| 44 (f.67) | Letter of Montholon, Tours, 15 April 1590 | *(no flag, no bnf4715.htm section)* | "Lettre, avec chiffre, du Sr DE MONTHOLON." -- **cipher noted but no "déchiffrement" at all**, unlike the "en partie déchiffrée" rows | **open** (the most genuinely virgin row: no period decipherment of any kind, and no Tomokiyo crib; image sampled -- see Pool size, it turns out to be mostly clear French with scattered numeral codes, not a dense cipher leaf) |
| 47 (f.70) | Letter of Montholon | *(no flag; Bourdeau's own digest says "listed without a reading", see below)* | "Lettres du Sr DE MONTHOLON. **Chiffre et déchiffrement.**" (combined entry with no.48) | **found-solved** -- contradicts Bourdeau's own summary (below); the BnF's own dépouillement is unambiguous and uses the identical "chiffre et déchiffrement" phrasing it uses for every other already-deciphered item in the same volume |
| 48 (f.71) | Letter of Montholon | *(no flag; same Bourdeau caveat)* | same combined entry as no.47 | **found-solved** (same basis) |
| 50 (f.73) | Sr de Trespigny to Vieuville, sequel to no.12 | *(HTML comment: sequel note)* | "Fin d'une lettre du Sr DE TRESPIGNY au Sr de La Vieuville... **Chiffre et déchiffrement.**" | **found-solved** |
| 52 (f.75) | Vieuville to Duke of Nevers, Si, 20 June 1589 | *(no flag)* | "Lettre de ROBERT DE LA VIEUVILLE au duc de Nevers... **Chiffre et déchiffrement.**" | **found-solved** |
| 54 (f.77) | Letters of Montholon | *(no flag)* | "Lettres du Sr DE MONTHOLON. **Chiffre et déchiffrement.**" (combined entry with no.55) | **found-solved** |
| 55 (f.78) | Letters of Montholon | *(no flag)* | same combined entry as no.54 | **found-solved** |
| 57 (f.80) | Letter of Vieuville | *(no flag)* | "Lettre de ROBERT DE LA VIEUVILLE. **Chiffre et déchiffrement.**" | **found-solved** |
| **58 (f.81)** | Letter of Montholon, Tours, 8 Nov 1589 | "Undeciphered. Partially deciphered in [bnf4715.htm]." | "Lettre du Sr DE MONTHOLON. **Chiffre non déchiffré.** Tours, «8 nov.» 1589." | **open** (this pool's existing target folder; 2,524 signs on f.81r, MONT-4715/4715B: calibration z=1.58 at n=1,167, fails its gate, key untestable-by-this-transcription so far, not a negative on the key) |
| 60 (f.83) | Undeciphered. Partially deciphered in [bnf4715.htm]. | matches | "Fol. 82 à 86 • 59-63 **Chiffres non déchiffrés.**" (grouped with no.59/61/62/63, a different section of the volume, not all Vieuville-Nevers) | **open** -- but see caveat: bnf4715.htm's own `no.60` DUMP passage runs to a natural stop ("...precher te '14x x [n]ovembre") with **no explicit "...." truncation**, unlike no.27 and no.58, which both end mid-sentence in an explicit ellipsis. Tomokiyo's own modern reading may already be fuller than the BnF cataloguer's 20th-century "non déchiffré" reflects; not independently checked against the image this job (out of the U1-U4 scope) |

**Caveat on the Montholon identity.** Tomokiyo's `bnf4715.htm#no27` links "Sieur de Montholon" to François II
de Montholon (Wikipedia), Keeper of the Seals for the League. The BnF finding aid's own name index lists a
single entry, "Montholon, Jérôme de. • Lettres.", covering the whole volume's Montholon material -- it does not
separately index a "Montholon, François II de." The finding aid's own item 21 explicitly names the writer
"JEROME DE MONTHOLON, Sr DE PEROUSSEAUX", but items 27/28/35/37/39/44/47/48/54/55/58 just say "le Sr DE
MONTHOLON" unqualified. Whether all the unqualified "Sr de Montholon" letters are François II's (per Tomokiyo)
or some are Jérôme's (per the finding aid's one index entry) is not resolved here -- flagged for whoever reads
the letters, not decided.

## Solver repositories (U2, before any verdict above was finalised)

**Bourdeau (`dbourdeau/cyphersolver`)**: no dedicated `targets/` folder for any fr.4715 Montholon/Vieuville
letter. `SOLVED_CATALOGUE.md` line 236, in a list of catalogue rows "removed [from the 22 Sept new-solves
sweep] because a partial reading by others already exists" (prior-art check, not an active target), reads
verbatim: *"**Montholon and Vieuville to Nevers** (BnF fr. 4715 nos. 19, 27, 37, 47, 48, 58, 60, 62; catalogue
317): Partly read. Tomokiyo deciphered the openings of fr. 4715 nos. 27, 58 and 60 with the Vieuville–Nevers
cipher, no. 19 fits the 1592 Spanish syllabic cipher, Lasry has interim results on no. 62, and nos. 37, 47 and
48 are listed without a reading. 'fr. 3414' is not attested anywhere and may be fr. 4715 (checked 22 Sept
2026)."* This is Bourdeau's own paraphrase of Tomokiyo's pages, not independent work, and it is **wrong about
nos. 47/48**: the BnF's own dépouillement (above) marks both "Chiffre et déchiffrement" -- Bourdeau's digest
did not check the archival notice, only nevers.htm/bnf4715.htm's silence. `targets/r2276/`, `targets/orbais/`
and `SOLVED_CATALOGUE.md`'s Reims/Pellevé rows cite **fr.4715 f.2** as a reference cipher-alphabet image
(Nevers-Piles cipher, a *different* cipher family, a folio not in this pool) -- an incidental grep hit, not
pool material. `targets/vieuville1587/` is BnF fr.3975 f.101 (Nevers's Nevers cipher no. 16, 1587) -- a
different volume and a different key, matched only on the personal name "Vieuville". No hit on Trespigny or
`btv1b52509819x` beyond the same fr.3975-sourced files. No fraction_read figure exists for any of the 22 rows
above; Bourdeau has not read any of them beyond citing Tomokiyo.

**Aymeloglu (`aaymeloglu/unsolved-ciphers`)**: no hit at all on 4715/Montholon/Vieuville/Trespigny in
`CATALOGUE.md`, `SHORTLIST.md`, `README.md`, `AGENTS.md`, `CONVENTIONS.md`, or the DECODE catalogue crawl
(`catalogue/decode-catalog.csv`, `catalogue/decode-records.jsonl` -- one coincidental id-number match, an
unrelated 1715 Marburg record). This pool is entirely outside that repository's coverage as of this clone.

## Pool size (U4)

Fetched three not-yet-on-disk canvases at 600px (Gallica IIIF, browser UA, 1.5s apart) into this target's
`images/`: `pool_f50r_600.jpg` (no.27), `pool_f60r_600.jpg` (no.37), `pool_f67r_600.jpg` (no.44) -- all three
chosen from the **open/partial** rows, not the found-solved ones, since those don't count as attack material.
Eye-compared against f.81r (no.58, the known 2,524-sign full leaf, ~36 lines of dense continuous cipher):

- **f.50r (no.27)**: dense continuous cipher for about 22 lines (top ~60% of the leaf), a later hand's marginal
  notes below (not cipher), then blank. Estimated **~1,500 signs**.
- **f.60r (no.37)**: dense continuous cipher for about 22-24 lines, similar layout to f.50r. Estimated **~1,500-1,600
  signs**.
- **f.67r (no.44)**: **mostly clear French prose**, with only a handful of scattered numeral code-groups
  visible per line (a "mostly-clear leaf with scattered code tokens" shape, not a dense cipher leaf -- see
  README's malsburg-hessen-1636 per-leaf pricing precedent for this shape of job). Estimated **~50-150 signs**,
  not ~1,500 -- this row does not carry its weight toward the pool total the way a dense leaf would, despite
  being the "most open" row status-wise.

The other five open/partial rows (no.21 f.44≠no.44's own folio -- no.21's folio is f.44, no.44 the item's folio
is f.67, not a typo; no.28 f.51, no.35 f.58, no.39 f.62, no.60 f.83) were **not imaged this job** (over the
brief's 3-canvas unit budget). Estimating from the two dense-leaf samples above (no.27, no.37) as the closer
analogue for same-office, same-date-range Montholon/Vieuville single-leaf letters, at ~1,500 signs each:
5 x 1,500 = ~7,500 (a rough, unimaged estimate, stated as such, not a count).

**Pool total estimate (open/partial rows only): 2,524 (no.58, measured) + 1,500 (no.27, imaged) + 1,500-1,600
(no.37, imaged) + ~100 (no.44, imaged) + ~7,500 (no.21/28/35/39/60, unimaged estimate) ≈ 13,000-13,200 signs.**
Comfortably over the Pipeline 3 pool threshold (2,000+ signs, one sender/office/key family) even discounting
the unimaged estimate heavily -- the three imaged, non-found-solved rows alone (no.27, no.37, no.58) already
total ~5,500-5,600 measured/directly-eyeballed signs across two letters plus the one fully transcribed leaf.

If the 11 found-solved rows are counted too (not attack material, but real recovery-grade material: a period
decipherment exists and needs only transcription), the volume's total Vieuville-Nevers-cipher signed material
is considerably larger again -- no.3 and no.12 alone each span several folios of already-interlinear-deciphered
correspondence.

## For the parent

**This is worth a lane, but as two different jobs, not one pool-sized cryptanalysis campaign.**

1. **A genuine open cryptanalysis/completion sub-pool**: 8 single-leaf Montholon/Vieuville letters with the
   Vieuville-Nevers key already on file (no.21 f.44, no.27 f.50, no.28 f.51, no.35 f.58, no.37 f.60, no.39
   f.62, no.44 f.67, no.60 f.83) plus the existing no.58 f.81 target, at an estimated ~13,000-13,200 signs total
   (2,524 measured + ~10,650 imaged/estimated, above) -- well over the 2,000-sign pools-first bar, same key family (`keys/
   key_vieuville_nevers.tsv` already on disk and cross-validated), same sender's office, same 13-month date
   range (Oct 1589-Apr 1590). MONT-4715/4715B's finding on f.81r (calibration z=1.58 at n=1,167, key
   "untestable-by-this-transcription" not refuted, real key still beats shuffled mean rank 2 of 21) suggests
   the bottleneck across this whole sub-pool is likely to be **transcription accuracy against this hand**, not
   the key itself -- a reason to prioritise better crops/reconciliation methodology (MONT-4715B's crop-legibility
   fix, already documented in NOTES.md) over trying more leaves blind. no.44 f.67 is a different, cheaper shape
   of job (mostly clear French, a handful of scattered codes) and could be a fast separate win.
2. **A recovery/transcription sub-track**: 11 rows (no.3, 6, 10, 12, 47, 48, 50, 52, 54, 55, 57) already carry
   a period decipherment per the BnF's own catalogue (interlinear or bound), independently of anything
   Tomokiyo published online -- no.47/48 in particular contradict Bourdeau's own "listed without a reading"
   summary. These are not cryptanalysis targets; they are "photograph the leaf, transcribe the period
   decipherment that is already sitting on it" jobs, grade C/H the moment the image is read, and could produce
   several fast, citable readings before any codebreaking is attempted on the harder rows. no.3 and no.12 in
   particular are multi-folio (the BnF groups several physical leaves under one item number) and may be
   substantial on their own.
3. Two rows (no.41 f.64, no.42 f.65) need an image check before being placed in either track -- the BnF's own
   catalogue is silent on "chiffre" for them, unlike every other row, which may mean they are not ciphertext at
   all despite nevers.htm listing them under the Vieuville-Nevers heading.
4. Key of record: `ciphers/fr4715-montholon-1589/keys/key_vieuville_nevers.tsv` (already built, INTAKE-4715,
   cross-validated). No new key work is needed to start either sub-track.

## Register additions

- `KEY-ADJACENT.tsv`: one new row, "BnF fr.4715 Vieuville-Nevers pool (nos. 3,6,10,12,21,27,28,35,37,39,41,42,
  44,47,48,50,52,54,55,57,58,60) -- pool, CS-4715-POOL, see ciphers/fr4715-montholon-1589/POOL.md".
- `QUEUE.md`: one row, "queued, pool, CS-4715-POOL -- fr4715-montholon-1589 Vieuville-Nevers open sub-pool (8
  letters besides no.58: no.21, 27, 28, 35, 37, 39, 44, 60; ~10,600-10,700 signs estimated), see POOL.md" (at
  least one letter besides no.58 comes back open -- eight do).

## Requests this job

cryptiana.web.fc2.com: 0 fresh (both htm files already on disk from INTAKE-4715). archivesetmanuscrits.bnf.fr:
0 fresh (BnF notice read from Bourdeau's own repository cache, per the brief's "solver repositories FIRST"
step doubling as the BnF-notice source once found there). gallica.bnf.fr: 3 IIIF image fetches (600px canvases,
1.5s apart) + `tools/gallica_folio.py` cached-manifest reads (no network, manifest already cached). GitHub:
2 shallow clones (dbourdeau/cyphersolver, aaymeloglu/unsolved-ciphers). googleapis.com/books: 2 calls (both
`&country=US&key=$GOOGLE_BOOKS_KEY`). be-api.us.archive.org: 1 call. No DECODE live crawl (cached copy used).
No credentials printed. No AskUserQuestion. No novelty/first/unpublished wording (rule 10) -- every found-solved
verdict above is sourced to the BnF's own period cataloguer's notation, not claimed as our discovery.
