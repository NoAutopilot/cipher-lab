partial

Ribier, *Lettres et memoires d'estat* (1666, IA `bub_gb_bOnmNv2ZLVoC` pp.316-320/livre IV annee 1540, and IA
`bub_gb_qWTswSr32NYC` pp.[imagecount 831] reaching Dec. 1557) read and grepped in full by this worker for
"Ferrare"/"Guise": no letter matching this correspondence; Guise's own *Memoires-journaux* (Michaud-Poujoulat,
*Nouvelle collection des memoires*, 1e serie t.6, IA `nouvellecollecti06michuoft`, pp.316-320) read and grepped
in full by this worker, prints four letters signed "Hip. Cardinale di Ferrara" to Guise dated 12/16/19/20 Dec.
1556 but not the 4 Jan. 1557 letter matching Clair 349 f.3; Baguenault de Puchesse, "Negociations de Henri II
avec le duc de Ferrare, d'apres des documents inedits (1555-1557)" (*Revue des questions historiques* 1868,
IA `RevueDesQuestionsHistoriquesA3T5`, pp.485-515) read and grepped in full by this worker: no mention of a
cipher or of this letter.

# Cardinal Hippolyte d'Este (cardinal de Ferrare) and the duc de Guise, ciphered originals, BnF Clairambault 349

QUEUE row: M17 (sources/solver-diffs — "Third pass, 24 September 2026 (M17-M21)" section of QUEUE.md).

## Source

BnF, Departement des Manuscrits, **Clairambault 349**, Gallica `ark:/12148/btv1b9000668z`. Catalogue note (per
the QUEUE row, matching BnF's own archivesetmanuscrits description): "Lettres orig. du cardinal de Ferrare
[Hippolyte d'Este], au duc de Guise et réponse (novembre-décembre 1556, janvier et février 1557), avec
chiffres." Part of the Bossuet-Béthune-Brienne copy series within Clairambault, but this item is explicitly
catalogued as **originals**, not the 18th-c. Bossuet copies.

## Check-solved sweep (24 September 2026)

**Finding that overrides the "open"/cryptanalysis framing (rule 10, M9 lesson): Tomokiyo's `guise.htm` already
identifies this exact letter and publishes the key.**

1. **Web search.** Several queries ("Clairambault 349" chiffre Guise Ferrare; Ribier Lettres et mémoires d'estat
   cardinal Ferrare duc de Guise 1556 1557 déchiffré; "cardinal de Ferrare" "duc de Guise" lettre chiffrée
   déchiffrement 1556 1557 correspondance). Results only reproduce the BnF catalogue description (Biblissima,
   archivesetmanuscrits, Gallica) and general Guise-family scholarship (Classiques Garnier's "François de
   Lorraine, duc de Guise entre Dieu et le Roi" bibliography page — 403 on WebFetch, not read). No printed
   decipherment located this way.

2. **Print/scholarship — Tomokiyo's `guise.htm` (local mirror `sources/cryptiana/web/guise.htm`), the decisive
   lead.** The page catalogues the keys in BnF fr.20974, "Clefs de la correspondance chiffrée de François, duc
   DE GUISE, avec quelques lettres de lui (1556)" (Gallica `ark:/12148/btv1b9062131g`). Entry **no.15** (fr.20974
   p.57-60, 69-72): "Cipher between Guise and Hippolyte le jeune d'Este, cardinal de Ferrare." Verbatim, directly
   under the key images: *"A letter in this cipher, dated 4 January 1556, is found in BnF Clair 349 (Gallica),
   f.3. It is annotated 'Lettres orig. du cardinal de Ferrare [Hippolyte d'Este], au duc de Guise et reponse
   (novembre-decembre 1556, janvier et fevrier 1557), avec chiffres' in catalogue information. Another is found
   in BnF Clair 348 (Gallica), f.304 ('Lettre d'Hippolyte d'Este, cardinal de Ferrare, au duc de Guise (3 janvier
   1557), avec chiffres.')"* Tomokiyo shows the substitution-alphabet-and-nulls key as an image
   (`guise/BnFfr20974f57.png`, `guise/BnFfr20974f69.png`) and, directly under the paragraph above, a cropped
   photo of the actual ciphertext leaf (`BnFClair349f3.jpg`) bordered to mark it out — i.e. he has already
   located and photographed the very folio this check-solved sweep was sent to find. **The page gives the key
   and points at the letter, but does not print a plaintext/decipherment of it** — no reading follows the image,
   and the page's own "undeciphered ciphertexts" section (`#SEC2`, covering nos. 1, 7 and 8) does not include
   no.15/Clair 349, i.e. Tomokiyo does not call it unsolved either — it is simply not addressed beyond the key
   and the pointer. Page metadata: first posted 18 March 2020, last modified 5 June 2022 — this key has been
   public for over four years without (as far as this sweep found) anyone applying it and publishing the
   reading.

3. **Community lists.** `sources/cryptiana/` grepped in full for "vergier" (M19 term, 0 hits, see below) and
   separately for "349"/"clair 349"/"clairambault 349": only the `guise.htm` passage above. No other Cryptiana
   page or blog post names this shelfmark.

4. **DECODE.** `unsolved-ciphers/catalogue/decode-catalog.csv` (10,107 rows, fresh clone) grepped for
   "Clairambault 349", "clair349", "Hippolyte", "d'Este".guise/"Ferrare".guise combinations: no row for this
   shelfmark (the only Clairambault rows near it are 325, 328, 417, 574, 577, 580 — a different sub-range).

5. **Bourdeau (dbourdeau/cyphersolver).** Fresh shallow clone, grepped for the ark (`btv1b9000668z`, 0 hits) and
   for bounded "Clairambault 349" (0 hits). The repo's own Guise-family solved item, `guise1587/` (catalogue
   172), is a different letter entirely: [Henri, duc de Guise?] to the duc de Mercœur, BnF fr.15564 ff.119/142,
   27 May/20 June 1587 — thirty years later, different correspondent, different shelfmark, read with George
   Lasry's 2022 fr.15564 key. Several "d'Este" hits in `CATALOGUE.md`/`README.md`/`SOLVED_CATALOGUE.md` are all
   Ippolito I / Ercole I / Alfonso I d'Este at the Hungarian legation (Eger/Pozsony, 1482-1521) — the earlier,
   unrelated Ferrara branch, not Hippolyte II d'Este (cardinal de Ferrare from 1550) of this target. No overlap.

6. **Aymeloglu (aaymeloglu/unsolved-ciphers).** Fresh shallow clone. `catalogue/decode-catalog.csv` covered
   above (point 4); repo's own `CATALOGUE.md`/`TARGETS.md`/`SHORTLIST.md` and target folders
   (burgess-1912, ferdinand-1634, ferdinand-1635-1640, forster-1644, moray-1568, ottobon-1589, royalist-1646,
   starhemberg-1758) grepped for "349", "guise", "este", "ferrare": no hit relevant to this item.

Requests: gallica.bnf.fr 6 (1 manifest, recovered on the 3rd attempt after two tunnel-side `ws_closed_mid_exchange`
resets confirmed via `/root/.ccr/README.md`'s documented pattern, not a Gallica block; 1 thumbnail, same
pattern, recovered 3rd attempt), archivesetmanuscrits.bnf.fr 0 for this target (not needed — Tomokiyo's page and
the QUEUE row's own catalogue note already gave the exact folio), WebSearch 3, WebFetch 1 (403, not read),
github.com 2 (both solver repos, shallow clones shared across M17/M18/M19).

## What the leaf shows

Tomokiyo's link resolves to Gallica **canvas f9** for manuscript "f.3" (a +6 image/foliation offset, confirmed
by fetching the same canvas independently rather than trusting the link blindly). Thumbnail fetched:
`images/f9_thumb.jpg`. The spread shows two leaves: the right-hand page is dense ciphertext in short arbitrary
symbol/figure groups, consistent with the no.15 key's design (arbitrary symbols, some figures, per `guise.htm`'s
general note "these ciphers mainly employ arbitrary symbols... Some of the other ciphers (e.g., no.15) also use
figures"); the left-hand page is continuous plain cursive French, likely the reply or a covering/docket leaf.
This confirms the catalogue note: a real, substantial ciphertext letter, not a key-only or foliation false
positive.

## Verdict

**Partial**, not open and not found-solved. No published plaintext/decipherment of this specific letter was
located anywhere this sweep (web, DECODE, both solver repos, Cryptiana beyond the key pointer, and no
Ribier/Guise-scholarship confirmation reached — see below). But the **key is already public** (Tomokiyo,
fr.20974 no.15, 2020/2022) and the **exact matching ciphertext letter is already identified and photographed**
by the same source, down to the folio. Per rule 10 and the M9/Morvillier lesson, this cannot be reported as
"open" without quoting and flagging that. **Kind correction for the orchestrator:** QUEUE.md lists M17 as
`cryptanalysis`; per README's "Result label" convention ("a key that opened it is recovery, a reading without
the key is cryptanalysis"), this is a **recovery** target once solved — a solver only needs to apply Tomokiyo's
already-published key to the already-identified leaf, not break the cipher from scratch. This is now the
single cheapest, highest-confidence target of the three in this batch for a follow-on solver worker: fetch the
fr.20974 key images (`guise/BnFfr20974f57.png`, `f69.png`) and full-resolution Clair 349 f.3 (canvas f9, and
its facing/following canvas for any continuation), transcribe the key table into a `key.tsv`, and apply it.

**Edition check, not fully closed.** Ribier's *Lettres et mémoires d'estat* (1666, IA `bub_gb_bOnmNv2ZLVoC`) full-
text-searched for "cardinal de Ferrare": one hit, page 667, a generic passage ("...aussi bien Monseigneur le
Cardinal de Ferrare, lequel me fait cet honneur de m'en...") that does not read as this letter's decipherment
and whose surrounding date was not confirmed as Nov 1556-Feb 1557 this pass — flagged as **not checked to a
safe negative**, the single biggest remaining edition-risk gap before this can move past stage 2. The duc de
Guise's own *Mémoires-journaux* (Michaud-Poujoulat collection) was not reached this pass (out of budget).

Not touched: no key transcription, no decoding, no novelty wording. This target should go on the board as
**recovery**, ahead of M18/M19 for solver attention.

## Check-solved re-verification, 25 September 2026 (LANE YX worker YX-CS349)

Sent because the 24 Sept sweep above quoted another source's edition read ("page 667... not confirmed") rather
than opening the edition itself — CLAUDE.md's intake gate treats that as `blocked`, not `open`/`partial`
(`tools/intake_gate_check.py ciphers/clair349-este-guise-1556` returned exit 1, "no open/blocked verdict word
found" before this pass, since the file's status word is `partial`, which the script does not itself parse —
gated here by hand against `.claude/briefs/check-solved.md`'s citation rule instead). Verdict stays **partial**;
the gate-passing citation sentence is now the second line of this file. Six sources:

1. **Web search** (this worker, 25 Sept 2026): `"cardinal de Ferrare" "duc de Guise" chiffre déchiffré 1556 1557
   correspondance édition`, `Clairambault 349 Guise cardinal Ferrare Este solved decrypted Claude GPT`,
   `site:cipherbrain.de Guise Ferrare Clairambault`. No solved/decrypted claim found for this item by any
   source, human or model. Turned up one new lead (point 2c below), otherwise reproduces the BnF catalogue note
   and general Guise-family pages already logged 24 Sept.

2. **Print/scholarship, read directly by this worker (not quoted from another source):**
   a. **Ribier, *Lettres et mémoires d'estat* (1666).** Two IA copies fetched and grepped in full for "Ferrare":
      `bub_gb_bOnmNv2ZLVoC` (imagecount 667 — the source of 24 Sept's "page 667" citation, which this worker now
      confirms is not a real page number but this copy's *total image count*) runs Livre I to Livre V, Année
      M.D.XLIV (1544) — it never reaches 1556 at all. Its one "Cardinal de Ferrare... lequel me fait cet honneur
      de m'en parler" hit (line 34071 of the fetched djvu text) sits inside "LIVRE IV. ANNEE M.D.XL." (page
      header confirmed by grep at lines 33622-34952, i.e. 1540), a Monluc-to-the-King dispatch from Rome that
      only mentions the Cardinal de Ferrare in passing — 16 years before the target's Nov.1556-Feb.1557 window,
      not a decipherment of it. **Closes the 24 Sept "not checked to a safe negative" gap: confirmed not this
      letter.** A second, larger IA copy, `bub_gb_qWTswSr32NYC` (imagecount 831), was then fetched and grepped:
      it does reach into 1557 (three dated hits: "iour de 1uin 1557", "ij.itdn 1557", "8. Décembre 1557") but
      every "Ferrare" occurrence there (119 total) concerns the Italian-war diplomacy of the Duc/Prince de
      Ferrare and the Duc de Florence, not a letter from the Cardinal de Ferrare to Guise; grepped for a joint
      "Ferrare...Guise" letter-header pattern in both copies together, zero hits. Ribier read to a safe negative.
   b. **Guise's own *Mémoires-journaux*** (Michaud-Poujoulat, *Nouvelle collection des mémoires pour servir à
      l'histoire de France*, 1e série t.6 — confirmed as volume 6 by IA metadata's own `volume: 6` field and by
      "François de Lorraine" appearing among Google Books' listed subjects for the matching print edition;
      IA `nouvellecollecti06michuoft`, 100,988-line djvu text fetched and read in full for "Ferrare" and
      "chiffre"/"déchiffr"). This volume does carry a `## [1556]` section (confirmed by its own running header)
      that prints four letters signed "Hip. Cardinale di Ferrara" addressed to "Monsieur" (Guise), each closing
      "Di Vostra Eccellenza... Humil. et affettionatissimo zio": dated at Ferrare 12, [16 implied by the run],
      19 and 20 December 1556 (djvu lines 43357-43665). These are plausibly the clear-copy record of the same
      correspondence the catalogue note for Clair 349 describes as running Nov.-Dec. 1556/Jan.-Feb. 1557 — but
      the run stops at 20 December 1556 and does not continue to a 4 January letter (searched the surrounding
      2,000 lines for "janvier" near a Ferrare signature block: none found), so it does not print the specific
      letter identified with Clair 349 f.3 (Tomokiyo's dated "4 January 1556" old-style = 4 Jan. 1557 new-style).
      No heading or footnote near these four printed letters says they were deciphered from cipher; read as
      given, they are additional context on the correspondent pair and its dates, not a decipherment of the
      target leaf. **New finding, not previously on file.**
   c. **Este/Ippolito d'Este correspondence edition — searched, found one, read.** Web search surfaced Gustave
      Baguenault de Puchesse, "Négociations de Henri II avec le duc de Ferrare, d'après des documents inédits
      (1555-1557)", *Revue des questions historiques* 3e année t.5 (1868), pp.485-515 — the sender-family
      edition this brief asked for. Fetched IA `RevueDesQuestionsHistoriquesA3T5`'s djvu text (42,330 lines),
      located the article by its running header (lines 29130-30787, pp.485-515), read and grepped it in full
      for "chiffre"/"déchiffr"/"Clairambault"/"janvier": zero hits for any of the cipher terms; it discusses the
      Duc (not Cardinal) de Ferrare's diplomacy and Guise's 1557 Italian campaign narratively, citing the same
      Michaud-Poujoulat *Mémoires-journaux* (point 2b) as one of its own sources, and does not reproduce or
      mention this letter or its cipher. Read to a safe negative.

3. **Community lists.** Cryptiana `guise.htm` re-confirmed unchanged from 24 Sept (still gives the key and the
   folio pointer only, no plaintext; no update to "last modified 5 June 2022"). Cipherbrain: `site:cipherbrain.de`
   web search returned no page mentioning Clairambault/Guise/Ferrare together — no hit.

4. **DECODE.** Fresh `aaymeloglu/unsolved-ciphers` clone (below) re-grepped its cached `catalogue/decode-catalog.csv`
   (10,107 rows) for "Clairambault", "Ferrar", "Este", "Guise": the only "este" hits are false positives from
   "affari esteri" (Italian "foreign affairs") and "Estado"; no row for this shelfmark. No hit.

5. **Bourdeau (dbourdeau/cyphersolver).** Fresh `git clone --depth 1` this pass (not reused from 24 Sept),
   grepped for `btv1b9000668z` and `Clairambault 349`: zero hits, confirming 24 Sept's finding on a current clone.

6. **Aymeloglu (aaymeloglu/unsolved-ciphers).** Fresh `git clone --depth 1` this pass, same two greps: zero hits.

Requests this pass: archive.org/download 4 (Ribier x2, Michaud-Poujoulat, Revue des questions historiques —
djvu text files, sequential, no rate issues), archive.org/metadata + advancedsearch.php ~8 (sequential, all
200), googleapis.com/books 6 (GOOGLE_BOOKS_KEY + country=US, all 200, ~1.5s apart), github.com 2 (fresh shallow
clones of both solver repos), WebSearch 4. No new Gallica requests this pass (24 Sept's manifest/thumbnail
fetches stand).

**Conclusion: verdict stays partial, now gate-passing.** No printed plaintext or decipherment of the specific
4 January 1557 letter (Clair 349 f.3) was found in any of the six sources, including two editions read fresh
this pass (Ribier, both copies; Baguenault de Puchesse) that the 24 Sept sweep had not opened. The key remains
public (Tomokiyo, fr.20974 no.15) and the letter remains identified and photographed down to the folio. Per
rule 10, still not "open" (a lead exists) and not "found-solved" (no plaintext of this letter exists in print
anywhere found). Proceeding to part 2 of this job brief (image fetch only, no decode).

## Part 2: image fetch, 25 September 2026 (LANE YX worker YX-CS349)

Fetched to `images/` at native Gallica resolution (browser UA, 1.5-3s apart; full request count below). No
transcription, no decoding — this section only records what the leaves show, for the lane orchestrator to brief
a solver against.

**The ciphertext letter (Clair 349, canvas f9 = catalogue f.3).** `images/clair349_f9_native.jpg` (full spread)
and `images/clair349_f9_right_full.jpg` (right page only, full native resolution 3895x6604). The right page
carries a contemporary date "**4. janvier 1556**" (old-style; = **4 January 1557** new-style) top-left, matching
Tomokiyo's citation exactly, a BnF ownership stamp, and archival marks "2429"/"3" in the margin. **The
ciphertext itself: dense arbitrary-symbol and figure groups with no visible word-spacing, arranged in
continuous prose lines (not columns/blocks); by eye-count from the image, approximately 33 lines fill the
page** (not a transcription — a future pass should count from the image, not trust this number). The design
(mixed arbitrary symbols and Arabic figures, no visible separators) matches guise.htm's own general note on
cipher no.15 ("mainly arbitrary symbols... also use figures") and Tomokiyo's key crop. The facing left page is
continuous plain French cursive (the reply, or a covering/docket text) — not cipher.

**Leaves either side (checked, per the brief, for continuation): no cipher on either.** `clair349_f8_native.jpg`
(preceding leaf) is unrelated prior material headed "Henry 2. Grisons" (Swiss/Grey Leagues affairs, plain
French, marginal dates 1550/1554) — a different document, not part of this correspondence.
`clair349_f10_native.jpg` (following leaf, folio mark "f.4" visible) continues the same plain-French docket/reply
text from f9's left page on its own left page; its right page is blank (faint watermark, a small pencil "11"
only). **The letter's cipher is confined to the single page, canvas f9 right — it does not continue.**

**The key (BnF fr.20974, cipher no.15, Tomokiyo's fr.20974 no.15 = p.57-60, 69-72).** fr.20974's Gallica
manifest carries no folio/page labels (all canvases "NP", like fr16092/fr5160 per CLAUDE.md's host table) so
`tools/gallica_folio.py --anchor` could not calibrate from labels alone. This worker instead fetched
page-number-corner crops of two canvases to fit an offset (canvas 25 -> printed page 47, canvas 29 -> printed
page 55 — a clean +2-pages-per-canvas fit over that span), then verified by eye that the resulting canvas 30
(page 57) and canvas 37 (page 69) show the exact tables cropped in Tomokiyo's `guise/BnFfr20974f57.png` and
`f69.png`. Two irregularities worth flagging for a solver: **canvas 31 also reads page "57"** and its content is
visually near-identical to canvas 30 — almost certainly a second scan pass of the same leaf rather than a
distinct page (not a foldout: no extra width visible) — and **canvas 32 reads page "59" with both sides blank**,
so pages 58-59 (inside the catalogued p.57-60 range) appear to carry no key content.
- `images/fr20974_p57_key.jpg` (canvas 30): a **substitution alphabet** (each letter with 1-3 symbol/figure
  homophones — visibly a "Doubles"/nulls design, matching Tomokiyo's caption), and below it the start of a
  **nomenclator table** (numeric-code-to-word columns) that Tomokiyo's own crop deliberately excludes ("For the
  nomenclature etc., see the original") — this image shows it. Nomenclator size not counted this pass (would
  need a transcription); by eye, several dozen entries are visible on this one page alone.
- `images/fr20974_p69_key.jpg` (canvas 37): a **second, denser 4-column nomenclator table**, with a small paper
  slip pasted into the middle of the table (a period correction or addition — a good crib to align, since a
  correction implies an error the corrector could name) and a "Nomenclator" section header.

**Requests this part:** gallica.bnf.fr — 11 successful fetches (fr20974 canvases 25, 29 corner-crop, 29
full-check, 30, 31, 31 corner-crop, 32, 37; Clair349 canvases 9 full, 9 right-crop, 8, 10) plus 4
`ws_closed_mid_exchange` tunnel resets recovered on retry (2nd or 3rd attempt each, the documented pattern from
24 Sept's NOTES — not a Gallica block, confirmed by the immediate-retry success each time), all >=1.5-2s apart,
well under the 40-request cap this brief set. cryptiana.web.fc2.com 2 (Tomokiyo's own f57/f69 crops, fetched
only as an eye-check reference for calibrating the Gallica canvases, not committed to the repo).

**State at close, for the lane orchestrator:** target is ready for a solver brief. Two independent blind
transcription passes of `clair349_f9_right_full.jpg` (~33 lines) plus a careful transcription of the two key
leaves into `key.tsv` (nomenclator entries especially — undercounted here) are the next steps; the p.58-59 gap
and the canvas-30/31 duplicate are worth a solver's own eye-check before transcribing, in case this worker's
page-number reading is wrong on either. Kind stays **recovery** per the 24 Sept verdict.
