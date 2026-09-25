partial
Check-solved verdict (YX-CS349, 25 Sept 2026; restated here so it sits beside the status word): Ribier, *Lettres et memoires d'estat* (1666, IA bub_gb_bOnmNv2ZLVoC and bub_gb_qWTswSr32NYC) read and grepped in full; Guise *Memoires-journaux* (Michaud-Poujoulat 1e serie t.6, IA nouvellecollecti06michuoft, pp.316-320) read -- the 4 Jan 1557 letter is not printed; full section further down.

## YX-TR349 (25 Sept 2026): key transcription, step 1 of 3

`python3 tools/intake_gate_check.py ciphers/clair349-este-guise-1556`:
```
ciphers/clair349-este-guise-1556: partial (line 1) -- edition/page or full-text-search citation found within 6 lines
EXIT: 0
```
Gate passes; proceeded to deep work per this brief (`.claude/briefs/runs/2026-09-25-lane-yx-tr349.md`).

**Step 1 (key transcription) done at reduced confidence; steps 2-3 (ciphertext transcription, decode) not started this
session -- see "Handoff" below.**

**Image quality correction, first action this session.** The key images already on disk (`images/fr20974_p57_key.jpg`,
`images/fr20974_p69_key.jpg`, fetched by YX-CS349) were only 750x600px (a Gallica `,600` IIIF size request), too low-
resolution for confident symbol-level reading -- individual homophone digits and signs are only a few pixels tall at
that size. Fetched full native resolution for both canvases (`f30/full/full/0/native.jpg`, `f37/full/full/0/native.jpg`,
~7460x5960px each, 2 Gallica requests, 2s apart, browser UA, both HTTP 200) as `fr20974_p57_native.jpg` /
`fr20974_p69_native.jpg`; manifest.json updated with both new entries and corrections to the old entries' content
descriptions, which turned out to be wrong once native resolution was available (no "4-column nomenclator" table, no
pasted correction slip on either leaf -- both leaves in fact carry the *same* template: Alphabet / Doubles+Nulles /
Monosillabes x2 rows / a further word row, plus a facing-page word list, differing between p.57 and p.69 mainly in
that word list, i.e. in the addressee-specific names -- the Doubles-row digits read identically on both leaves,
22.18.66.69.76.106.52.56.54.58.9, consistent with a fixed chancery template in fr.20974 personalised per
correspondent; not confirmed against a third key in the book). This determines a design correction: the earlier
description of the ciphertext as "arbitrary symbols and figures" (YX-CS349) is more precisely a **substitution
alphabet mixing numeral homophones and invented non-numeral signs for the same letters** (e.g. this pass's letter B
has one digit homophone, `3`, and one non-digit sign homophone), not a symbol-only design.

**Method.** Cropped six sections per key leaf (alphabet row, doubles+nulles row, two monosyllable rows, a further
word row, and the facing-page word list) at native resolution. Two Sonnet subagents (the brief's cap of at most two)
each blind-read all twelve crops (six per leaf) independently, neither seeing the other's output or this worker's own
reading, and returned a TSV with a grade (H/M) and note per cell. This worker then closely re-examined the alphabet
row itself at very high zoom (3-5x on 100-200px-wide slices) since it is the single highest-value section, resolving
several genuine three-way disagreements from the image directly (e.g. letter B's cell holds a non-digit sign *plus*
the digit 3, which one subagent had conflated into "3" alone and the other could not read at all; letter F's homophone
is a non-digit sign that happens to resemble the letter "H", distinct from the real letter H's own cell two columns
over, which both subagents had partly confused).

**Result: the front half of the alphabet (A-I/J) plus the whole Doubles/Nulles row settle at grade H** (cross-checked
across this worker's own read, both blind subagent passes, and -- for Doubles -- the identical row on the p69 leaf):
A={12,14,28; 16 struck/void}, B={a sign + 3}, C=9, D=5, E={26,16,62}, I/J={60,64,24}, Doubles pc/cc/ff/ll/mm/nn/pp all
read cleanly (22,18,66,69,76,106,52). **The back half of the alphabet (L through &) and most of the Monosillabes/
word-list code columns do not settle this pass** -- the manuscript is genuinely crowded there (up to 3 stacked
homophones per letter in a narrow column, several ligatured abbreviations that may be bleed-through from the facing
page rather than codes), and this worker's own close reading did not converge with either subagent closely enough to
commit a confident reading; see `key_alpha.tsv` rows marked `unresolved`/M and the note on each. The word LISTS
(monosyllables, the facing-page name/place list) are mostly legible as **words** even where their numeric/sign codes
are not -- captured in `key_nomen.tsv` with the words at reasonable confidence and codes graded M or left `?`.

**Files:** `key_alpha.tsv` (47 rows: 20 H / 27 M -- Alphabet A-I/J plus all ten Doubles digits, and the two Nulles-
adjacent sign IDs, at H; L-Z and both Nulles rows' exact sign shapes at M), `key_nomen.tsv` (59 rows: 5 H / 54 M --
mostly words at M because their codes did not resolve), `images/atlas/` (17 reference crops: 6 alphabet-row segments
`p57_alpha_seg1-6.jpg` at 1.5x zoom, `p57_doubles_nulles.jpg`, `p57_monosyl_row1/2.jpg`, `p57_lastword_row.jpg`,
`p57_left_wordlist.jpg`, and the p69 equivalents for cross-checking -- these are section-level crops, not one crop
per individual sign as the brief's "S01, S02..." scheme implies; a genuine per-glyph atlas of the ~15-20 distinct
non-digit signs identified (coded S01-S26 in the two TSVs by description only, not yet cropped to their own files)
is follow-up work, noted below). `images/manifest.json` updated. Total `images/` folder size 23MB (cap 30MB).

**Grades:** H 25 / M 81 across both TSVs (106 rows total); 0 I/C (no known-plaintext or key-source-independent
readings attempted this pass -- this whole key is itself the "key source", graded H only where the manuscript image
is unambiguous to two-plus independent readers).

**Hosts this session:** gallica.bnf.fr 2 requests (native-resolution key leaves, browser UA, 2s apart, both HTTP
200). No other hosts. 2 Sonnet subagents (blind key-table reads, within the brief's 2-subagent cap).

**Handoff for steps 2-3 (not started, time-boxed out):** Ciphertext line-cutting was tested (not committed) --
`python3 tools/iiif_lines.py --image images/clair349_f9_right_full.jpg --out ciphers/clair349-este-guise-1556/images
--prefix f9right --debug` on the already-fetched full-resolution right page detects 37 line-bands (pitch ~119px);
eye-count from YX-CS349 was ~33, so a few detected bands are likely blank margin/date-line artifacts at the top and
bottom, not real ciphertext lines -- check the debug overlay before starting passes, per transcription.md. The
ciphertext itself (checked directly, not merely assumed) is a genuine mix of numeral groups and a smaller number of
non-numeral signs matching this key's design, consistent with cipher no.15. Next steps in order: (1) a further
close-reading or expert pass to settle the L-Z alphabet cells and the Nulles/Monosillabes codes this pass left
unresolved -- ideally with a column-boundary detection script (an ink-projection profile like `iiif_lines.py`'s row
detection, but on columns) rather than eyeballing, since manual column assignment is the main source of remaining
disagreement; (2) per this brief's step 2, cut the ciphertext line crops for real, two blind subagent passes against
the atlas, reconcile with `tools/reconcile_passes.py`, gate at 60% agreement; (3) per step 3, merge `key_alpha.tsv`
+ `key_nomen.tsv` into a decode.json-driven `tools/decode_key.py` run (an option to merge two key files will be
needed, per the brief, since this target has two separate TSVs rather than one key.tsv+exceptions.tsv pair), write
`specs/clair349-este-guise-1556.json`, and run `judge_plaintext.py`. Kind stays **recovery** per the 24 Sept
verdict (key source: `published` identification of a `period` key sheet, per this brief).

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

## YX-TR349B (25 Sept 2026): ciphertext transcription (step 2 of 3) — partial, gate marginal, step 3 not attempted

`python3 tools/intake_gate_check.py ciphers/clair349-este-guise-1556` at 12:57 UTC: `partial (line 1) --
edition/page or full-text-search citation found within 6 lines`, `EXIT: 0`. Gate passes; proceeded per this
brief (`.claude/briefs/runs/2026-09-25-lane-yx-tr349b.md`), continuing YX-TR349's step 2/3.

**Line-boundary correction (first action, before any transcription).** YX-TR349's handoff ran
`tools/iiif_lines.py` on `clair349_f9_right_full.jpg` and got 37 detected bands against an eye-count of "~33",
flagging the debug overlay as unchecked. This worker checked it: **37 is not "~33 plus noise" by coincidence —
the true mapping is offset by 3 at the top and 1 at the bottom, not a uniform miscount.** Reading each edge
crop directly: band 1 (centre 568) and band 2 (centre 1316) are blank upper margin; band 3 (centre 1444) is
the "4. januier 1556" date line plus the BnF seal and archival marks "2429"/"3" — real content, but not
cipher; bands 4–36 (centres 1792…5781, **33 bands**) are the real ciphertext lines; band 37 (centre 6402) is
blank lower margin. Confirmed by viewing `f9right_L01_s1.jpg`/`f9right_L37_s1.jpg` (both blank) and
`f9right_L03_s1.jpg`/`f9right_L36_s1.jpg` (date line; last real cipher line) directly, and by re-drawing the
overlay with the paper's own printed red/blue ruling lines suppressed (they were being mistaken for the
detection overlay in the original debug jpg at low zoom). The 33-line eye-count from YX-CS349 turns out to be
exactly right — but the earlier handoff had not verified *which* 33 of the 37 detected bands were the real
ones, and would have handed a transcription pass two junk lines (date/seal, blank margin) folded in.

Cut each real line (bands 4–36) from `clair349_f9_right_full.jpg` via `tools/iiif_lines.py --overlap 0`, then
re-stitched each line's two 2400px segments myself with the actual ~905px right-anchored overlap trimmed
(`s1` cropped to native x∈[0,1495), `s2` appended unchanged) — `--overlap 0` on the CLI does not eliminate the
tool's own two-segment overlap for a line wider than one segment, so a naive stitch of the raw segments
double-prints about a third of each line. `images/lines/line01.jpg`..`line33.jpg` (33 files, one full-width
image per real cipher line, 4.3MB) are the result; committed with a manifest.json entry documenting the exact
recipe (deterministic from `clair349_f9_right_full.jpg`, already on disk) since the raw intermediate segment
crops and the (uninformative, paper-ruling-confounded) debug overlay were deleted to stay under the 30MB
folder cap (was 34MB with them, 27MB without).

**Two blind passes** (the brief's cap of 2 subagents, both Sonnet), each given only the 33 line images — not
each other's output, not the key's letter values, not even the key's sign atlas (S01–S26; giving it would
have biased which non-digit shapes a pass "sees" toward the letter alphabet's own homophone signs, when the
ciphertext may also use nomenclator/word-code signs not on the alphabet row at all). Each pass segmented by
visible pen-lift gaps, transcribed digit tokens literally, and invented its own short label per recurring
non-digit sign shape (kept consistent within its own pass only). `passA.tsv`: 1083 tokens (678 digit / 405
sign), 568 H / 515 M. `passB.tsv`: 949 tokens, 73 H / 876 M — B graded far more conservatively than A on
identical material, not a sign of a worse read (its own report reserved H "for clearly isolated multi-digit
clusters and a handful of unmistakable recurring ligatures"). Both independently flagged the same two things
unprompted: an ink blot over part of line 11 (B), and a "2429" numeral set apart on line 1 that might not be
part of the main code stream at all (both A and B) — **confirmed by this worker's own close reading of line 1
(below): "2429" is the same BnF archival item number already noted in the margin of the full-page image by
YX-CS349, not a ciphertext token.**

**Reconciliation — three numbers, because the naive one is close to uninterpretable here.** Per
transcription.md's "Symbol alphabets" lesson (a page mixing digits and invented signs needs a *shared*
ciphertext-side glyph atlas before two passes are reconciled, or their independent sign vocabularies cannot be
compared row by row) — a step this worker's time box did not leave room to do properly before running the two
passes (flagging this as the gap for a successor, not glossing over it):

| basis | agree | note |
|---|---|---|
| raw (`passA.tsv`/`passB.tsv` as committed) | **453/1135 = 39.9%** | dominated by sign-label vocabulary mismatch, not real disagreement — see below |
| sign-normalized (every `sign`-kind token → placeholder `SIGN`) | **746/1137 = 65.6%** | loose upper bound: "did both passes agree a sign belongs here", not which one |
| partial cross-pass sign atlas (8 confident shape correspondences only) | **591/1139 = 51.9%** | tighter, more honest measure: only the sign pairs this worker actually has evidence for (matching descriptions in both passes' own notes, confirmed by the NW aligner already placing them at the same column repeatedly before any remapping — `z-flourish`≈`tie-flourish`, `Ao-ligature`≈`Ao-lig`, `ff-ligature`≈`ff-lig`, `hash-mark`≈`hash`, `tc-ligature`≈`tc-sign`, `uu-ligature`≈`uu-sign`, `loop-Y`≈`Y-mark`, `to-ligature`≈`to`) count as agreement; everything else (roughly 30 more distinct labels per pass, `R-loop`/`R-mark`, `cross-mark`/`plus-mark` or `x-mark`, `m-ligature`/`m-sign`, `flag-mark`/`loop-sign`, `tau-mark`/`pi-mark`, `f-hook`/`bar`, and more) stays unmapped rather than guessed |
| digit-only (sign rows dropped, digit rows renumbered per line) | **437/717 = 60.9%** | agreement on the decode-critical digit stream alone, unconfounded by sign vocabulary |

All four regenerate exactly via `python3 ciphers/clair349-este-guise-1556/reconcile_metrics.py` (pasted output
above). Per-line breakdown (partial-atlas basis, `--rows`): **no line reaches 0.70; most sit 0.4–0.65, several
(lines 7, 8, 12, 17, 25, 29, 31, 32) are at or below 0.45.** This is a materially worse and more informative
picture than the sign-normalized number's "mostly 0.6–0.9 on lines 1–20" — the loose metric was crediting a
lot of matches between signs that are probably not the same mark. Real difficulty is spread across the whole
page, not concentrated only in the bottom third as the looser measure suggested (though the bottom third,
lines 21–33, is still the weaker half on every measure tried).

**Gate call: marginal on the loose measures, arguably FAILS on the tighter one — step 3 not attempted this
session.** The raw/sign-normalized/digit-only figures (39.9%/65.6%/60.9%) sit at or above PROCESS-2026-09-24
proposal 4's 60% line by the aggregate number the tool itself prints (matching how YX-BARB reported its own
normalized number as the single headline figure), but the partial-atlas figure — built from only the sign
correspondences this worker actually has evidence for, rather than crediting "any sign matches any sign" —
comes in at 51.9%, under the line. Read together, these four numbers say the same thing PROCESS-2026-09-24
predicted for a mixed digit/sign page without a shared atlas: the ciphertext-side glyph atlas this worker did
not have time to build properly (only 8 of an estimated ~30-38 distinct sign shapes cross-mapped, from textual
description alone, not full re-inspection of every occurrence) is the actual blocker, not a third blind pass.
Given that, this worker is treating the gate as **not safely passed** rather than leaning on the loosest
number available. But unlike YX-BARB
(who, at 90.5%, settled all 38 real disagreements from the image by hand before calling the target done), this
worker did **not** hand-settle the 391 sign-normalized (682 raw) disagreement columns from the image — with
roughly half the individual lines still under 60% even on the fairest measure, and ~30 minutes left in the
box, eye-checking all of them honestly was not going to fit, and a rushed partial settle risks looking more
final than it is. `ciphertext_draft.tsv` (committed) is therefore the **mechanical** reconciliation only —
agreed positions at H, disagreements resolved to pass A's value at M (the tool's documented fallback when
there is no real majority) — **not eye-verified**, and deliberately left named `ciphertext_draft.tsv` rather
than promoted to `ciphertext.tsv`, so a decode script never silently treats it as settled. Per this brief,
step 3 is conditional on the gate passing; given the gate is a technical pass but the underlying transcription
is unsettled and the key itself (YX-TR349) is still mostly unresolved past the front half of the alphabet, a
decode run against this material would not produce a reading worth grading either H/C (no key/plaintext
source) or a meaningful S (the ciphertext it would run against is not this worker's own settled read) — so no
decode.json, no spec, no judge_plaintext.py run this session. This is the conservative call this worker is
making unsupervised, logged per the no-human-watches rule, not a step skipped by oversight.

**One eye-check actually done, as a worked example and to settle the "2429" question**: line 1 at 2x crop
(`/tmp` scratch, not committed) reads, left to right: a short cursive fragment before the digit stream begins
(both passes independently flagged this as possibly a plaintext heading/salutation remnant rather than a
coded sign — plausible but not resolved here either) — then a run of digit/sign codes — then, set apart to the
upper right and in a visibly different, smaller hand, "2429" (with "3" faintly below, matching the "2429"/"3"
archival marks already logged on the full-page image). **This is not a ciphertext token; both passes were
right to flag it and wrong (B) or right (A) to include/exclude it — a future reconciliation pass should drop
it from the line entirely rather than align it as a disagreement.**

**Files:** `images/lines/line01.jpg`–`line33.jpg` (the 33 real cipher lines, corrected boundary mapping,
recipe in `images/manifest.json`); `passA.tsv`, `passB.tsv` (blind transcriptions, committed as each pass
produced them); `passA_norm.tsv`/`passB_norm.tsv`, `passA_digitsonly.tsv`/`passB_digitsonly.tsv`,
`passA_atlas.tsv`/`passB_atlas.tsv`, `reconcile_metrics.py` (the four-metric reproducibility script, its
`CANON` dict of the 8 confident sign correspondences, and its inputs — a successor extending `CANON` with more
correspondences and re-running the script is the fastest way to improve on 51.9%); `disagreements.tsv`,
`ciphertext_draft.tsv`, `agreement.tsv` (raw reconciliation, mechanical only, not eye-settled — see above).
`tools/decode_key.py` gained a `load_keys`/merge-key-file option (job `"key"` as a list, e.g.
`["key_alpha.tsv", "key_nomen.tsv"]`) and a more permissive key-TSV header/column detector (needed once
key_alpha.tsv's/key_nomen.tsv's value-first, non-`code`-led headers are actually used for step 3), plus a
same-code-different-value collision guard (`merge_key_row`, catches `key_alpha.tsv`'s own C=9/DOUBLES:ss=9
double-use of digit 9) — built and tested (`tools/tests/test_decode_key.py`, 4 new cases, all pass) this
session in the time before both passes landed, ready for whichever session next attempts step 3. Three
pre-existing, unrelated `test_decode_key.py` failures (`antt-linhares-chave`, `rah-canada-1869` — both stale
committed readings from other lanes' work today) confirmed present before this session's changes too, via
`git stash`; not this worker's to fix (out of this brief's file scope).

**Grades (rule 4):** 0 H/C/S claimed as a "reading" this pass — nothing decoded. The transcription itself:
passA.tsv 568 H(-transcription-confidence)/515 M(-transcription-confidence) tokens, passB.tsv 73/876 — these
H/M grades describe *transcription* confidence (is the mark on the page legible), not a cryptanalytic grade;
no letter of plaintext has been read yet at any grade.

**Hosts this session:** none (all work from images already on disk; `pip install numpy pillow scipy` for
`tools/iiif_lines.py`'s dependencies, not a research host). 2 Sonnet subagents (the brief's cap), each one
blind pass over the 33 line images, no other tool use by them beyond image reads and writing their own TSV.

**Handoff, one line:** next step is either (a) build a real ciphertext-side glyph atlas (cluster the ~15-25
distinct non-digit shapes actually seen across passA.tsv+passB.tsv's sign tokens, à la
`ciphers/dupuy468-carpi-1520/glyphs/`) and re-reconcile against it before eye-settling disagreements line by
line, prioritizing lines 21-33 which are weakest, or (b) if a successor has more time budget, eye-settle
`disagreements.tsv` directly from `images/lines/*.jpg` without an atlas, line by line, starting from line 1
(this worker's one worked example above) — either way, decode.json/spec/judge (step 3) waits until
`ciphertext_draft.tsv` is eye-settled and promoted to `ciphertext.tsv`.

## ZX-349 (25 Sept 2026)

`python3 tools/intake_gate_check.py ciphers/clair349-este-guise-1556` at 15:44 UTC (run by the lane orchestrator):
`partial (line 1) -- edition/page or full-text-search citation found within 6 lines`, `EXIT: 0`. Gate passes;
proceeded per this brief (`.claude/briefs/runs/2026-09-25-lane-zx-349.md`), continuing YX-TR349B's handoff.

**Step 1: ciphertext-side glyph atlas built from the key (this worker's own visual read, no subagents used for
this step).** All 26 non-digit sign codes already assigned in `key_alpha.tsv`/`key_nomen.tsv` (S01-S26 --
`grep -c sign` both files) now have one crop each in `images/atlas/` (`S02_sign.jpg`..`S26_sign.jpg`; `S01` reuses
the crop YX-TR349 already made, `S01_letter_B_sign.png`), located by this worker directly in the existing
section-level key-leaf crops (`p57_alpha_seg2.jpg`, `p57_alpha_seg5.jpg`, `p57_doubles_nulles.jpg`,
`p57_monosyl_row2.jpg`, `p57_lastword_row.jpg`, `p57_left_wordlist.jpg` -- all already on disk from YX-TR349, no
new host fetch this step) via visual inspection at 2-3x zoom (several signs, esp. in `p57_left_wordlist.jpg`,
needed two or three zoom-and-recrop passes before the pixel box was right -- an ink-density row-profile script
was tried first and rejected: the code column's x-position drifts down the page by 100-150px, so a fixed-x
vertical profile missed most rows; direct visual measurement from wide crops was faster and more reliable).
`images/atlas/atlas.tsv` (code, crop path, shape description only -- **no letter value or meaning**, checked by
re-reading every description before writing it) and a 6-column contact sheet `images/atlas/sheet.jpg` (labelled
by code only) regenerate from `build_atlas.py` (hand-measured pixel boxes, documented in-script; rerun with
`python3 build_atlas.py`). Added the code `X?` (no crop) for a shape a pass sees that matches nothing on the
sheet, per the brief, rather than have a pass guess an existing code. Grades: this is a transcription aid, not a
reading -- no H/C/S grade applies; the crops are the same manuscript ink already graded H/M in `key_alpha.tsv`/
`key_nomen.tsv`, reused, not re-graded.

`images/` folder size after this step: 28MB (cap 30MB) -- checked with `du -sh`, room for the two blind passes'
own output (TSV, no new images) but not for another image-heavy step in this folder without pruning.

Hosts this step: none (all crops cut from images already fetched by YX-TR349; no gallica.bnf.fr requests). No
subagents this step (atlas-building was this worker's own visual/scripted work, within the brief's step 1, which
does not call for subagents until step 2).

**Step 2: two fresh blind passes against the atlas.** Two Sonnet subagents (the brief's cap of 2), each given only
`images/lines/line01.jpg`..`line33.jpg` and `images/atlas/sheet.jpg`+`atlas.tsv` -- not each other's output, not
`key_alpha.tsv`/`key_nomen.tsv`, not `passA.tsv`/`passB.tsv` -- transcribed every token as a digit group or an
atlas code (S01-S26, or `X?` for a shape matching none of the 26). Both independently flagged the "2429"/"3"
archival stamp on line 1 and excluded it per instructions (confirmed correct again this session, see below).
`passC.tsv`: 1155 tokens (506 digit / 649 sign, 635 H / 520 M, 252 `X?`). `passD.tsv`: 1063 tokens (549 digit / 514
sign, 455 H / 608 M, 341 `X?`). One process note for the ledger: this worker committed `passC.tsv` once already
(commit 134cd3f) while its subagent was still mid-write (1090 of 1155 rows -- the agent had not yet returned);
caught via the repo's stop-hook untracked-file check plus a rebase conflict, fixed with a follow-up commit once
the agent's actual completion notification arrived and the file was verified against the agent's own reported
totals (506/649/635/520/252, exact match). Lesson for the next worker: wait for the subagent's completion report,
not just for the output file to exist, before committing/pushing its output -- an async agent can still be
writing to a file that already exists on disk.

**Step 3: reconciliation and gate.** `python3 tools/reconcile_passes.py passC.tsv passD.tsv --crops images/lines
--rows`:

```
line  A-signs  B-signs  agree  cols  share
01  33  22  17  33  0.52
02  35  27  13  36  0.36
03  33  36  20  41  0.49
04  36  29  21  38  0.55
05  35  32  17  37  0.46
06  37  35  19  38  0.50
07  39  41  21  46  0.46
08  36  31  16  37  0.43
09  40  33  21  42  0.50
10  39  38  20  45  0.44
11  41  58  19  62  0.31
12  37  38  18  44  0.41
13  37  33  15  40  0.38
14  38  36  20  42  0.48
15  39  32  17  43  0.40
16  39  31  19  39  0.49
17  30  32  11  33  0.33
18  25  35   5  35  0.14
19  35  42  13  47  0.28
20  30  32  13  33  0.39
21  32  27  15  34  0.44
22  33  31  19  38  0.50
23  30  27  11  31  0.35
24  40  35  14  43  0.33
25  39  29  15  39  0.38
26  33  26   8  33  0.24
27  39  24  14  40  0.35
28  35  26  17  35  0.49
29  38  28  13  39  0.33
30  28  27   8  30  0.27
31  29  28   8  31  0.26
32  36  35  12  41  0.29
33  29  27  13  32  0.41
lines 33  signs A 1155  B 1063  agree 502/1277 = 39.3%  (nw)
```

**Gate call: FAILS clearly.** 39.3% pooled, against the brief's 60% line; no line reaches 0.55 (line 04 is the
best at 0.55, then line 01 at 0.52); the weakest (line 18) is 0.14. Unlike the two loose/tight-split numbers
YX-TR349B reported last session (39.9%/65.6%/60.9%/51.9%, where the aggregate figure the tool itself prints sat
at or above 60% on three of four measures and only the partial-atlas figure fell under), this session's number
is the single, honest measure: passC and passD share the *same* atlas vocabulary by construction (both were
shown the identical 26-crop sheet and told to use its codes), so there is no loose/tight split left to argue
about -- a literal S0x-vs-S0x (or digit-vs-digit) string match on the shared codes already *is* the tight
measure. **The atlas did not fix the underlying disagreement; it just removed the excuse that the two passes
were using incomparable private vocabularies.** That the tightened, apples-to-apples number (39.3%) comes in
*below* last session's own tightest figure (51.9%, the partial 8-correspondence CANON mapping) says the atlas
approach was the right call methodologically (transcription.md's lesson), but this particular leaf is genuinely
this hard to transcribe blind, not merely hard to reconcile across mismatched vocabularies.

**Diagnostic: segmentation-policy mismatch tested and ruled out as the main cause.** `passC.tsv` tokenizes small
inter-group separator/virgule/vertical-bar marks as their own `X?` sign far more often than `passD.tsv` does (237
such tokens in passC vs 90 in passD -- grep -c on each pass's note column for "separator|virgule|vertical
(bar|stroke)|double-dash"), which looked like it could be inflating the disagreement count by itself. Tested by
stripping every such token from both passes and re-running the reconciler: agreement *drops* to 33.5% (352/1050),
not up -- so the passes actually agree on placing separator marks about as often as they agree on anything else,
and removing them just removes some of the easier matches. The 39.3% gap is real disagreement about what the ink
says, not a segmentation-policy artifact. (Script: ad hoc, not committed -- filters both passes' `X?` rows whose
note matches the separator regex and re-runs `reconcile_passes.py`; reproduce from this note if needed.)

**One eye-check done, as the brief allows ("settle disagreements... on lines where time allows").** Read line 1
(`images/lines/line01.jpg`) at 3x vertical stretch, split left/right. Confirms two things at high confidence:
(1) the "2429"/"3" archival stamp both passes correctly excluded is genuinely there, upper right, in a smaller
hand, matching prior workers' identification -- unchanged. (2) **New finding: token 1 in both passes (passC
"cursive fragment... possibly plaintext heading tail" / passD "cursive script before first digit, possible
plaintext salutation") is neither cipher nor plaintext -- it is a circular BnF library ownership stamp
("BIBLIOTHEQUE IMP[ERIALE]..." or similar, an oval/circular stamp with radial lettering) partially overlapping
the start of the line, the same kind of archival mark already identified on the *key* leaf (fr.20974 p.57's
"BIBLIOTHEQUE IMP" stamp next to the Nulles row, images/atlas/p57_doubles_nulles.jpg). Both passes' grade-M
"plaintext fragment" reading of this mark should be dropped from any future pass/draft as a stamp, not
transcribed as text or cipher. Recorded here rather than silently edited into `ciphertext_draft.tsv` -- the
draft stays exactly as the reconciler wrote it (see below).

**Did not attempt full per-line hand-settlement beyond that one check.** Line 1 is the *lowest*-disagreement line
in the whole table (16 columns) and even it does not resolve cleanly by eye: several of its 16 disagreement
columns are not competing readings of the same mark but a genuine segmentation mismatch (e.g. col 5, passC token
5 = `X?` "double-dash separator" between the digit groups at that point in the line, passD has no token there at
all -- passD's own segmentation simply did not split a pen-lift gap that passC did). Forcibly picking a winner at
each such column would not add real confidence, it would just look more settled than it is (the exact trap
YX-TR349B's handoff flagged). Given the diagnostic above shows this is not a fixable-by-atlas or
fixable-by-hand-eyeballing-one-line problem but a genuine high-disagreement leaf, this worker is stopping at the
gate report rather than manufacturing a partial settle.

**`ciphertext_draft.tsv` (regenerated by this session's reconciler, committed) stays the mechanical draft, NOT
promoted to `ciphertext.tsv`.** Per the brief: gate fails, so step 4 (decode.json, spec, judge, matched control,
re-derivation) is not attempted this session. `disagreements.tsv` and `agreement.tsv` also regenerated
(overwriting last session's passA/passB-based versions).

**Files:** `passC.tsv`, `passD.tsv` (this session's two blind passes); `disagreements.tsv`,
`ciphertext_draft.tsv`, `agreement.tsv` (regenerated from passC/passD via `tools/reconcile_passes.py`, replacing
the passA/passB-based versions from last session -- `passA.tsv`/`passB.tsv` and their `_norm`/`_atlas`/
`_digitsonly` derivatives and `reconcile_metrics.py` are left in place as the prior session's record, not deleted).

**Grades (rule 4):** 0 H/C/S claimed as a reading this pass -- nothing decoded, same as last session. The
transcription confidence grades (H/M) describe legibility, not cryptanalysis.

**Handoff:** the atlas removed one confound (mismatched sign vocabulary) and the diagnostic above rules out
another (segmentation-policy noise) -- what remains is that this leaf's ink is genuinely hard to read blind at
~50% or worse per line even with a shared reference sheet. Two ways to move this forward that this worker did not
have time for: (a) a third, non-blind pass whose only job is to settle `disagreements.tsv` column by column
against the image with the two passes' notes open side by side (not blind -- explicitly a reconciliation pass,
the brief's step "past the gate" tooling but run *before* the gate as a deliberate exception, since blind
re-passes have now been tried twice at the 51.9%/39.3% level without closing the gap); (b) tighten the atlas
crops further where a single S0x code may be conflating two distinct marks (this worker cut each crop from a
single occurrence in the key, not checked against multiple occurrences in the ciphertext itself -- a sign that
looks unambiguous once in the key may still be one of several ciphertext-only marks with no key-row match at
all, which is exactly what `X?` is for, but a pass under time pressure may reach for the nearest S0x instead).
Kind stays **recovery** (key source: `published` identification of a `period` key sheet).
