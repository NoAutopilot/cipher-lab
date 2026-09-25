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

## ZX-349B (25 Sept 2026)

`python3 tools/intake_gate_check.py ciphers/clair349-este-guise-1556` at 16:38 UTC: `partial (line 1) --
edition/page or full-text-search citation found within 6 lines`, `EXIT: 0` (also run by the lane orchestrator at
15:44 UTC before this brief). Gate passes; proceeded per this brief
(`.claude/briefs/runs/2026-09-25-lane-zx-349b.md`), continuing ZX-349's key-fit question: does the fr.20974 key
(as transcribed by YX-TR349) actually fit this ciphertext, or is the 39.3% blind-pass agreement evidence of a
wrong or mismatched key?

**Method note, logged up front (no bounding boxes exist for ciphertext tokens).** Unlike
`dupuy452-carpi-1520/glyphs/classified.tsv` (the brief's named pattern), which has real per-glyph pixel
positions, `passC.tsv`/`passD.tsv` record only `line, position` (a token's rank within the line), not `x,y,w,h`.
`xq_sample.py` (new, this session) estimates a crop window proportionally (token position / that pass's token
count for the line, times line width) and cuts a generous margin around it; `xq_index.tsv`/`sign_index.tsv`
record the estimate and the pass's own note text for every sampled token, so an off-centre crop can still be
judged from the description. Several of the 40+40 sampled crops landed on blank margin or the page's dark
binding edge for this reason (visible in `images/atlas/xq_sheet.jpg`/`sign_sheet.jpg`) -- flagged, not silently
dropped. Fixed seed 42 throughout (`python3 xq_sample.py {xq|sign} --seed 42 --n 40`).

**Step 1a: what IS an X? token, across the whole population (593 tokens, both passes pooled), not just the
40-sample.** Before clustering the 40-sample by eye, categorised all 593 X? notes by keyword (script, not
committed as a separate file -- reproduce from the note column of `passC.tsv`/`passD.tsv`):

| category | count | share |
|---|---|---|
| separator/punctuation mark (vertical bar/stroke, z-shaped curl, double-dash) | 328 | 55.3% |
| letter-like / ligature cluster (candidate cipher sign) | ~241-244 | ~41% |
| ink blot / damage / illegible | 13 | 2.2% |
| plaintext fragment bleeding through (not cipher) | 10 | 1.7% |
| cut at crop edge | 1 | 0.2% |

**This changes the question.** Only the "letter-like" ~41% is a candidate pool for "does this shape appear on
the key" at all -- the majority (55.3%) are punctuation the atlas was never meant to cover, and cross-checking
punctuation against the key's letter/word rows is not the right test for it. The X?-rate reported by ZX-349
(39.3% pooled disagreement, ~22-32% of each pass's tokens coded X?) therefore overstates the "missing from key"
problem: at most 10-13% of all ciphertext tokens (the letter-like fraction of the X? fraction) are actually
candidates for a key-leaf search; the rest is either not a sign at all or a metric/segmentation issue already
ruled out by ZX-349's own diagnostic.

**Step 1b: the 40 X?-sample (fixed seed 42), clustered by eye + note text, written to
`images/atlas/xq_types.tsv`** (type, population_count, population_share, sample_idx, sample_count, description,
key_leaf_match -- full table in that file). Headline sub-types, with population counts recomputed from all 593
X? tokens by a finer keyword match (script, not committed):

- **separator_vertical_bar** (157, 26.5%) and **separator_z_curl** (162, 27.3%): both very high, regular
  per-line frequency (approx. 4-5 occurrences per line each, every line) -- too frequent and too regular for a
  single letter homophone (LESSONS.md "structure before search": a real code sign should track French letter
  frequency, not recur this uniformly), so on structural grounds these are more likely genuine punctuation
  between cipher groups, as both passes independently judged, not a missing key sign. Not checked against the
  key leaf on that basis; flagged that this reasoning is inference from frequency alone, not a formal test.
- **sign_to_ligature** (35 occurrences, 5.9% of all X?): a recurring "to"-like ligature. **FOUND on the key
  leaf**, directly: `p57_alpha_seg3.jpg` (bottom right, under the crowded O/P/Q cluster), `p57_alpha_seg4.jpg`
  ("to.102"), `p57_monosyl_row1.jpg` (code row, cut at the crop's lower edge but the shape is visible),
  `p69_alpha_full.jpg` ("to . 102", clearly legible on the less-crowded p69 rendering of the same template row).
  All four sightings sit in rows `key_alpha.tsv`/`key_nomen.tsv` left graded M/"unresolved" (L-Z alphabet
  stretch, Monosillabes row 1) -- present on the key leaf, just never isolated into an atlas S-code because that
  part of the key image itself was too crowded to read with confidence (YX-TR349's own limitation, not a
  ciphertext problem).
- **sign_R_loop** (25, 4.2%): a looped capital "R" with a trailing tail. Plausible match in
  `p57_left_wordlist.jpg`'s code column (near the "hault. Lorraine"/nomenclator name rows) -- same shape family,
  not confirmed as the identical mark at matched precision.
- **sign_Ao_ligature** (39, 6.6%, the single largest specific letter-like sub-type after the two separator
  families): a bold capital "A" joined to a small loop, checked directly this session by cropping three fresh
  instances (line03 pos7, line08 pos24, line11 pos18) -- a compact, closed, consistent ligature across all
  three. **NOT found** on any key-leaf section viewed this pass (both alphabet rows, both Doubles/Nulles rows,
  both Monosillabes rows, both word lists). This shape closely resembles the period secretary-hand abbreviation
  "Ao" for "an"/"annee" (year) -- which would make it a plaintext/date fragment bleeding through, like the
  "quel"/"bon"/"que" fragments already found, rather than a cipher sign at all -- but at roughly 1.2 occurrences
  per line it recurs far too often for a date reference. **Genuinely unresolved; the single highest-value open
  question from this pass.**
- **sign_Y_like** (12), **sign_u_like** (10), **sign_s_like** (9): not checked against the key leaf this pass
  (time budget), flagged as follow-up.
- **sign_other_letterlike** (114, a long tail of one-off descriptions, e.g. "capital A-like flourish", "ligature
  cluster (nao g-like)", "capital ligature cluster (Cml-like)"): this worker's scan of `p57_left_wordlist.jpg`
  and `p57_monosyl_row2.jpg` shows several small loop/curl marks in the same general family (a cursive "e"-loop,
  an "8"-loop, a "y", a plus/cross, a spiral), but no side-by-side comparison at matched crop precision was done
  for these -- not resolved.

**Step 1c: 40 matched-sign-token sample (fixed seed 42), `images/atlas/sign_sheet.jpg`/`sign_index.tsv`.**
Distribution: S13 (plus/cross) 12, S24 6, S06 5, S20 4, S09 3, S07 3, S01 2, S23 2, S16 2, S10 1. Same crop-window
imprecision as step 1b applies (several crops landed on margin or digit-only regions with the target sign just
outside the window). Where ink was visible in the window, no crop showed an obviously wrong shape for its
claimed code (no case where the visible mark is clearly a different, unrelated shape from the claimed S0x's
atlas description) -- this is a qualitative spot check, not a rigorous per-token confirmation, and is reported
with that limit stated rather than as a clean "yes, all confirmed."

**Step 2: control, `dupuy452-carpi-1520` (found-solved; key confirmed to fit by shape-match, grade H, per its own
`key.tsv`).** The brief's named pattern is `dupuy468-carpi-1520`, which does not exist as a folder; the actual
Carpi-1520 target with a glyph atlas is `dupuy452-carpi-1520` (its `glyphs/` directory, `classified.tsv` with
real per-token `x,y,w,h`, `key.tsv`, `contact_sheet.jpg` -- used instead, logged here as the conservative
reading of the brief's typo rather than treating "no exact folder name" as "none on disk"). Because this target
already has real pixel bounding boxes and an existing, graded (H-level) shape-to-key correspondence across its
whole 5,725-token population, this worker used that existing correspondence directly (`key.tsv`'s `kind` column
against `glyphs/classified.tsv`'s `type` column) rather than re-cropping a fresh 40+40 sample -- a stronger
measurement (n=5,725, not n=80) of the same question the brief's 40+40 procedure asks, and viewed
`glyphs/contact_sheet.jpg` (already on disk, one row per type, every occurrence of that type shown) to confirm
by eye that each type's occurrences are visually tight and consistent (they are -- the sheet's rows are
near-identical within a row, unlike this session's `xq_sheet.jpg`/`sign_sheet.jpg`).

Result: **49 of 51 distinct glyph types (99.8% of 5,725 tokens) map to a `key.tsv` entry graded `letter`,
`word` or `null`; only 2 types (`cross4`, `?`; 12 tokens, 0.2%) are `open` (not yet resolved to a key value).**
This is the profile of a key that genuinely fits: almost nothing is unmatched, and what is unmatched is a small,
named residue, not a broad population of unexplained shapes. Contrast with clair349's ~41% letter-like-candidate
X? rate (even after removing punctuation) -- clair349 is far short of this profile, but per step 1 above a real
part of that gap is explained by the key's own incomplete transcription (to-ligature, R-loop found on the leaf
but never atlas-coded) rather than by the key being wrong.

**Verdict in numbers (per the brief's step 3).** Neither of the brief's two clean branches is fully supported:

- NOT "most X? types are absent from the key" -- of the letter-like sub-types actually checked against the key
  leaf this pass (to-ligature 35, R-loop 25 = 60 tokens, the two largest specific types after the punctuation
  families and the unresolved Ao-ligature), both were found on the leaf, in rows the key transcription itself
  left unresolved. No sub-type was confirmed ciphertext-side and confirmed ABSENT after a real search of the
  full key leaf; every non-match this pass is "not checked" or "not found in the sections viewed," not
  "searched exhaustively and ruled out."
- NOT "most X? types are on the key leaf, extend atlas.tsv" either -- most of the letter-like population (Ao-
  ligature 39, Y-like 12, u-like 10, s-like 9, other 114 = 184 of 244, 75%) is either not yet checked or (Ao-
  ligature specifically) checked and NOT found, with a live alternative explanation (a plaintext date
  abbreviation) not ruled out.
- The control shows what "this key fits" actually looks like quantitatively (99.8% type-to-key match) --
  clair349 is not at that level, but the shortfall traces at least partly to the key's OWN incomplete
  transcription (L-Z alphabet, most Monosillabes and word-list codes still graded M/unresolved,
  `key_alpha.tsv`/`key_nomen.tsv`), not to evidence the fr.20974 key is the wrong key for this letter.

**Conservative call, taken unsupervised per the no-human-watches rule:** not extending `atlas.tsv` with new
S27+ codes this session -- the to-ligature/R-loop matches found are visual correspondences from an estimated
(not exact) ciphertext crop to a similarly not-yet-precisely-isolated key row, not the same grade of evidence as
the existing S01-S26 crops (each of which came from a confidently isolated key cell). Also not concluding the
key does not fit or setting `closed-negative` -- the evidence found points the other way (concrete matches, no
confirmed non-matches) and rule 3 requires a matched control before any negative; this pass's one control
(dupuy452) shows what a genuine fit looks like, not what a genuine non-fit looks like, so it cannot itself
support a negative verdict either. Status stays **partial**.

**Next brief's line (this worker's own choice, not a third blind pass, not an atlas extension yet):** resolve
the key leaf's own unresolved rows for the two shapes this pass actually found (to-ligature, R-loop) with a
close, non-blind read targeted at just those two shapes (not the whole crowded L-Z/Monosillabes cluster) --
if that produces a real crop and column position, add S27 (to-ligature)/S28 (R-loop) to `atlas.tsv` from the KEY
image, not the ciphertext guess. Separately, resolve the Ao-ligature question (39 occurrences, once per line) by
checking French-period-letter epistolary convention for a per-line marginal/interlinear date or paragraph mark
that would explain a once-per-line recurrence, since "cipher homophone" does not fit that frequency either. Only
after both are resolved does a third, non-blind reconciliation pass (ZX-349's option (a)) or a further blind
pass make sense -- a third blind pass alone would very likely reproduce the same ~39% agreement ZX-349 already
found twice.

**Files:** `xq_sample.py` (new; samples+crops+builds a contact sheet for X? or matched-sign tokens, fixed seed);
`xq_index.tsv`, `sign_index.tsv` (per-sample idx/pass/line/position/token/note/crop/estimate-window);
`images/atlas/xq_crops/` (40 files), `images/atlas/sign_crops/` (40 files), `images/atlas/xq_sheet.jpg`,
`images/atlas/sign_sheet.jpg` (contact sheets, this worker's own visual read); `images/atlas/xq_types.tsv` (the
brief's requested type/count/description/key_leaf_match table); `images/manifest.json` (new entry for the
derived crop/sheet files, imprecision caveat recorded). `images/` folder size after this session: 29MB (cap
30MB, checked with `du -sh`). No changes to `key_alpha.tsv`, `key_nomen.tsv`, `atlas.tsv`, `passC.tsv`,
`passD.tsv`, `ciphertext_draft.tsv` this session.

**Grades (rule 4):** 0 H/C/S claimed as a reading -- nothing decoded, this pass is entirely about whether the
key-fit question can be answered, not a decode. The to-ligature/R-loop key-leaf sightings are this worker's own
visual read (not a grade-H committed key entry -- no crop was cut from a confidently isolated key cell this
session).

**Hosts this session:** none (all work from images already on disk). No subagents (the brief's step 1 does not
call for subagents; this worker's own visual/scripted work throughout, consistent with ZX-349's step 1
precedent).

## ZX-KEY349 (25 Sept 2026)

Intake gate `partial`, exit 0 (orchestrator 15:44 UTC, ZX-349B 16:38 UTC, re-run by this worker 17:12 UTC). Brief:
`.claude/briefs/runs/2026-09-25-lane-zx-key349.md`. Opus, one key-reading session, no host requests (all from the
native images already on disk; no Gallica fetch was needed), one Sonnet subagent for the blind cross-read.

**Why the earlier reads stalled.** The key is written sideways on fr.20974 p.57 (and p.69). Turned 90 degrees clockwise
(`build_key_cells.py` documents the frame), every column of the L-Z alphabet, the Doubles, the Nulles, both
Monosillabes rows, the last word row and the name list reads cleanly at native resolution: the columns are not crowded,
the earlier section crops were read on their side. p.69 carries the same template in the same hand and was read as a
cross-check cell by cell (alphabet, Doubles, Nulles, name list agree with p.57; differences noted per row).

**Step 1: every cell read.** `build_key_cells.py` holds one hand-measured box per cell and writes
`images/atlas/key_cells/` (104 crops at 0.4 scale), `key_alpha.tsv` and `key_nomen.tsv` (same columns as before; new
`kind` values `void` for A's struck 16 and `none` for list entries with no code); `--check` exits 1 if the TSVs are
stale. Values read (value: codes, top to bottom):

A 12 14 [16 struck] 28 | B S01 3 | C 9 | D 5 | E 26 16 62 | F S02 | G S03 | H 17 | I/J 60 64 24 | L S27 5 | M S28 S29 |
N S30 15 | O 82 44 | P S31 | Q S32 | R S33 S34 | S S35 S36 | T S37 S38 | V 102 7 104 | X S39 | Y 73 | Z S40 | & S04 S05.
Doubles: sc?/22 cc/18 ff/66 ll/69 mm/76 nn/106 pp/52 rr/56 long-ss/54 tt/58 round-ss/9. Nulles (ten signs, two rows,
under a heading read on p.69 as "Pour lire suivante: sont la precedente nulle", wording M): S06-S10, S41-S45.
Monosillabes, last row and name list: see `key_nomen.tsv` (60 rows; 56 carry a code).

Homographs in the key as drawn (logged, not resolved): 5 is D's only code and L's second; 22 is the Doubles "sc?" code
and "pour"; 9 is C and the round-ss double; S37 ("to") is T's first homophone and "fit"; S17 (two crossed t) is
"Monsr" and "fist"; S32 is Q and "n'aye". A letter-level decode will need context (or the gloss, below) to split them.

| table | before (YX-TR349) | after (this pass) |
|---|---|---|
| key_alpha.tsv | 47 rows: 20 H / 27 M, 9 `unresolved` | 62 rows: 52 H / 10 M, 0 unresolved |
| key_nomen.tsv | 59 rows: 5 H / 54 M, 33 without a code | 60 rows: 44 H / 16 M, 4 without a code (3 of them have none on the leaf) |

**Blind cross-read of the M cells:** one Sonnet subagent read the 27 M cells blind (native-scale crops, values hidden, labels m01-m27; key in the worker's scratchpad). Its code agreed with this worker's on 21 of 27 (M/S28+S29, T/S37 (second read 'ta' for S38), &/S04+S05, sc?/22, the eleven word codes fist, fit, dict, n'aye, avec, une, mon, florin, douze, arm., escus, beaute, munitions?, Le Roy mre (read as digit 4), Sienne?, and 'no code' on Nemours and Espagnols?). Disagreed or unread on 6: D (saw a hook squiggle, not 5), S (saw S35+S36 as one tall crossed sign), rr (read 16 for 56), long-ss and round-ss (crop cut the digit; the Doubles band is now extended to y 1520 in the script) and 'cy?' (unclear). Taken over from the blind read: florin(s) (was florens), beaute (was beaulte?), douze? (this worker had Venize; two readers against one). Those rows stay or go M as noted in the TSVs.

**Corrections (row, old, new, reason):**

| row | old | new | reason |
|---|---|---|---|
| H | 17 M | 17 H | directly under the H header on both leaves |
| L | ? unresolved | S27 + 5 | rotated read; ff-like sign and 5 are L's column |
| M | ? unresolved | S28 + S29 | "cm" and "uu" signs |
| N | ? unresolved | S30 + 15 | "cma" sign and 15 |
| O | ? unresolved | 82 + 44 | the "82" YX-TR349 placed in the M/N cluster is O's |
| P | ? unresolved | S31 | circle-on-cross |
| Q | ? unresolved | S32 | |
| R | ? unresolved | S33 + S34 | S34 is the "Ao" shape (see question b) |
| S | 73 M | S35 + S36 | 73 is Y's, not S's |
| T | 104 M | S37 + S38 | "to" and "tc"; 104 is V's |
| V | ? unresolved | 102 + 7 + 104 | |
| X | 73 M | S39 | 73 is Y's |
| Y | ? unresolved | 73 | |
| Z | S04 M | S40 | the # (S04) is &'s first code |
| & | S05 M | S04 + S05 | |
| F | S02 M (crop wrong) | S02 H, re-cropped | ZX-349's S02 crop showed G's header "6 ." |
| G | S03 M | S03 H | |
| DOUBLES qq / ff2 / st / ss | 56 / 54 / 58 / 9 | rr / long-ss / tt / round-ss, same digits | pair letters re-read; digits unchanged |
| NULLES | 5 signs (S06-S10) | 10 signs (S06-S10, S41-S45) | second row of five was never read |
| MONOSYL1 (14 rows, all `?`) | codes unresolved; "je" | codes S46, S17, S37, S47, S32, S48, S49, S50, 22, S51, S52, S53, S54, S55; "il" | code row read (the earlier crop cut it); "Jl" is il |
| MONOSYL2 avec / tout | 8 / 2 | S56 / S57 | both are signs, not digits |
| MONOSYL2 fault..quant, mon | ? | S58-S65 | read |
| LASTWORD de / florence / douze / ami / escu / beaute / ? | ? / ? / ? / A / ? / T / ? | S66 / S67 (florin(s)) / S68 (douze?) / S69 (arm.) / S71 / S72 / S73 (munitions?) | re-read; "ami" was a misreading; "A" on arm. is A+hooked v, not a plain A |
| LASTWORD mal | M | S70 (mil) | word is mil |
| LEFTLIST Le Roy mre (new), L'Empereur (new) | absent | S74, S75 | two top rows were not in the table |
| LEFTLIST Aumale / Naples / Milan / Florence | letter_sign A / c / dd / y | S76 / S77 / S78 / S79 | given atlas codes so passes can use them |
| LEFTLIST Suisse/Savoie | S19 M | Suisses S19 H | long ss legible |
| LEFTLIST Sienne | ? | S80 ("de sire" cluster) M | |
| LEFTLIST_P69 | one summary row | dropped | p.69 list read in full: same names and same codes as p.57 (Le Roy d'[Angleterre] and aumalle struck on p.69) |

**Step 2: atlas extended.** `images/atlas/atlas.tsv` and `sheet.jpg` now carry S01-S80 (S27-S80 new, crops from the
key image only, shape descriptions only; S02 re-cropped). ciphertext types from `images/atlas/xq_types.tsv` that now
have an atlas code: sign_to_ligature -> S37; sign_Ao_ligature -> S34; sign_R_loop -> S33 (R) or S20 (gendarmerie),
two candidates; sign_Y_like -> S32 or S79; sign_u_like -> S29; sign_s_like -> S35. separator_z_curl -> no sign: it is
the digit 2 (question a). separator_vertical_bar, separator_double_dash, sign_other_letterlike (114): no code assigned
(the last is a catch-all of one-off descriptions; S28 "cm" and S30 "cma" match its "Cml-like" / "nao"-like notes by
description but no token was checked).

**Step 3, the three questions.**

The first check that settles all three: **the ciphertext leaf carries a small interlinear hand above many codes.**
YX-TR349B, ZX-349 and ZX-349B logged these as "plaintext fragments bleeding through" ("quel", "que", "bon"). At native
resolution on `images/clair349_f9_right_full.jpg` they sit one above each code, in a smaller hand, and on the tokens this
worker checked they agree with the key values read above: 64 under "j", 12 under "a", 73 under "y", S34 under "r" (three
times), 26 and 62 under "e", 16 under "e", 9 under "c", 104 under "u", S27 under "l", 5 under "l", 58 under "tt", S33
under "r", S31 under "p", 82 under "o", 15 under "n", and |22| under "pour". This is a contemporary decipherment on the
original, i.e. known plaintext for most of the letter (grade C once transcribed). It was used here only as evidence
about the key; no line was decoded and nothing is reported as a reading (brief step 4).

(a) **separator_vertical_bar (157) and separator_z_curl (162).** Neither is in the Nulles row (S06-S10, S41-S45; the
nearest shape, S45, a small reversed-3, is not the ciphertext's z). The z-curl is **the digit 2** in this hand, the same
z-form the key itself uses for 12, 22, 62, 82, 102. Checked against the gloss on about ten instances in lines 1, 3, ~12
and ~20: 1z glossed a (12, twice), z8 a (28, twice), z4 i (24), z6 e (26, three times), 6z e (62, twice), 2z pour (22).
Passes that coded it as a separator split two-digit groups (12 became '1' + separator). The vertical bar (and a slanted
'/' variant) is not in the key at all; on the instances checked it falls at word boundaries (line 1 between a word ending
in S36 and one starting with 5; line 3 on both sides of 22, glossed 'pour'; line ~20 between a word ending in 26 and one
starting with S31), so it reads as a **word divider**, not a null and not a cipher sign; it also tells a pass that a code
standing alone between bars (|22|) is a word code rather than the Doubles pair that shares its digits. Not every one of
the 319 was checked; the claim is 'every checked instance', about 10 z and 4 bars.

p.69 re-check after the blind read (17:28 UTC): R's two homophones are clean there (S33, S34); D's code is the same
s-form 5 as on p.57; in the S column the long s's foot runs straight into the x, so the key drawing alone leaves S35/S36 as one sign or two; the ciphertext settles it: line ~20 has the x standing
alone, glossed 's', so S36 is S's own second homophone (graded M on the key cell, now with that ciphertext support); p.69's E column carries two struck numbers between 16 and 62 that p.57 lacks.

**By-eye atlas coverage check (17:30 UTC).** Four half-lines at native resolution (lines ~12 and ~20, about 70
tokens) read against the new sheet: every non-digit mark but two matched an S01-S80 shape (S27, S31, S32, S33, S34,
S36, S38, S40, S52 and S35 or S51 seen); the two unmatched are a t-with-long-s cluster ending line ~20a (possibly S46 or
S02) and a q-like mark opening line ~20b. Line ~20 also carries two more Ao (S34) glossed 'r', and 7 glossed 'u', 14
'a', 15 'n', 9 'c', agreeing with the key.

(b) **Ao-ligature (39).** It is in the key: R's second homophone, S34 (p.57 and p.69, R column, row 2), a hooked A
joined to o. Three ciphertext instances checked against the gloss: line 1 (after 73), line 3 (after |22|), line 8
(after 12): all three glossed "r" (two more on line ~20, also "r": five of five). Not a plaintext abbreviation. (The key's S69, the code of "arm.", is a similar A
with a hooked v, and S76, Aumale's code, is a plain A; passes must keep the three apart.)

(c) **Share of the ciphertext's recurring sign types with an atlas code.** Pooled passC+passD (2218 tokens): 1625
already carried a digit or S01-S26; adding the z-curl as digit 2 (162) and the six named letter-like types (to 35, Ao
39, R-loop 25, Y 12, u 10, s 9 = 130) gives **1917 / 2218 = 86.4%** of tokens with a key code; the bar (157, 7.1%) is
explained as a word divider; unexplained: sign_other_letterlike 114 + double dash 7 = 121 (5.5%); noise (gloss 10,
blot 13, crop edge 1) 1.1%. By type, all six named recurring letter-like types now have a candidate code (6 of 6) and
the two separator families are explained. dupuy452's control: 99.8% of 5725 tokens on a key entry. clair349 is not yet
at that level, but on this count the gap is the 5.5% catch-all, not the key; and the 86.4% rests on shape matches by
type, not per-token checks, so it is an upper-bound estimate until fresh passes code against the new atlas.

**Next job (one line):** two fresh blind passes over `images/lines/line01-33.jpg` against `images/atlas/sheet.jpg`
S01-S80, told that the z-shaped mark is the digit 2 (write "12", "62", never a separator), that a vertical bar or slash is
transcribed as `|` (a word divider, not a null and not a sign), that the small interlinear letters above the codes
are a gloss to be transcribed in a separate column (not as cipher tokens), and to keep S34 / S69 / S76 apart; then a
third, separate job transcribes the gloss line by line as known plaintext (C), which will settle the key's homographs
(5, 22, 9, S17, S32, S37) before any decode. The line crops cut off part of the gloss: the gloss job should recut the
lines from `clair349_f9_right_full.jpg` with the band above each line included.

Files: `build_key_cells.py` (new), `key_alpha.tsv`, `key_nomen.tsv`, `images/atlas/atlas.tsv`, `images/atlas/sheet.jpg`,
`images/atlas/S02_sign.jpg` (re-crop), `images/atlas/S27-S80_sign.jpg`, `images/atlas/key_cells/` (104). Removed:
`images/atlas/xq_crops/`, `images/atlas/sign_crops/` (their sheets `xq_sheet.jpg`, `sign_sheet.jpg` remain) to keep
`images/` under 30 MB (29.2 MB after). Grades (rule 4): no reading claimed; H/M above grade legibility of key cells.
Hosts: none. Status stays `partial`. cost: see the lane ledger.

## ZX-TR349C (25 Sept 2026)

Intake gate `partial`, exit 0 (orchestrator 15:44 UTC; ZX-KEY349 17:12 UTC; re-run by this worker 17:35 UTC, same
result). Brief: `.claude/briefs/runs/2026-09-25-lane-zx-tr349c.md`, common `.claude/briefs/runs/2026-09-25-lane-zx-COMMON.md`.
Sonnet, wall-clock box 90 minutes from 17:35:56 UTC start (`date -u`), at most 2 subagents at once. Continues
ZX-KEY349's handoff: settle the ciphertext side with the gloss included, no decode.

**Step 1: recut the 33 lines with the gloss band.** `images/lines` (YX-TR349B/ZX-349/ZX-349B's crops) has the same
bottom-anchored band edges as the key ciphertext line but its TOP edge (the midpoint between each line's centre and
the line above it) sits too close to the code row and clips the top of the small interlinear gloss ZX-KEY349 found.
No existing tool option did this, and `.claude/briefs/transcription.md`/CLAUDE.md Usage item 8 are explicit: "add
an option to the tool if it lacks one," not a private crop script -- so `tools/iiif_lines.py` gained `--top-margin PX`
(new; subtracts PX from each band's TOP edge only, clamped to 0, bottom edge unchanged; default 0 so every other
target's existing invocation is unaffected). Ran `tools/tests/test_iiif_lines.py` before and after: all 7 checks
still pass. This one line (`tools/iiif_lines.py`) is the only file touched outside `ciphers/clair349-este-guise-1556/**`
this session -- logged here as a deliberate, conservative reading of the brief's "touch only this target" line against
CLAUDE.md's stronger, repo-wide "shared scripts before new ones" rule, per the no-human-watches instruction to log a
judgment call rather than ask.

Re-ran `python3 tools/iiif_lines.py --image images/clair349_f9_right_full.jpg --overlap 0 --top-margin 45 --prefix
f9right --debug --out <tmp>`: band detection is bit-identical to the recorded YX-TR349B run (same 37 centres:
568 1316 1444 1792 1922 2054 2182 2300 2416 2533 2643 2753 2891 3020 3245 3359 3467 3589 3686 3803 3889 4060 4182
4306 4422 4551 4667 4780 4904 5044 5158 5241 5365 5497 5612 5781 6402; same pitch 119, distance 83, prominence
207.4) -- confirms bands 4-36 are still the correct 33 real cipher lines and the recut does not shift which lines
are which. --top-margin 45 chosen after a by-eye pixel probe (ad hoc, not committed) on the shortest (83px, line29)
and a middling (118px, line05) inter-centre gap: at 40-50px the gloss stroke directly above a code (e.g. the small
loop above line05's first "6") is fully visible and unclipped at the crop's top edge; at 90px on the tight-pitch
line the previous line's own row is pulled in almost whole. 45 sits in the range that captures the gloss everywhere
checked without reliably duplicating a full extra line. Segments and stitching reproduce YX-TR349B's method exactly
(s1 [0,2400) cropped to [0,1495), s2 [1495,3895) appended, 905px overlap trimmed so no token appears twice; ad hoc
stitch script, not committed, reproducible from the command above).

**Eye-check (brief's minimum: first, middle, last).** `images/lines_g/line01.jpg` (first): archival stamp, the
"2429"/"3" marginalia and the "4 januier 1556" date line are now visible above line01's own codes (expected --
line01's whitespace-above extends into the previous, non-cipher band), line01's own text and gloss fully visible,
un-clipped at the bottom. `line17.jpg` (middle): gloss marks visible above every code across the row, a thin sliver
of the previous line's tail at the very top, current line's own text un-clipped. `line33.jpg` (last): the final
cipher line's text and gloss fully visible, followed by blank lower-page margin, matching the page's actual bottom.
No clipping of any checked line's own content found in any of the three.

**Folder cap.** `images/lines` (33 files, no gloss margin, 4.3 MB) + `images/lines_g` (33 files, with margin, 6.0 MB)
together put `images/` at 35.4 MB (cap 30 MB). Per the brief ("you may delete images/atlas/xq_crops and sign_crops")
those are already gone (removed by ZX-KEY349). Deleted `images/lines/` instead: nothing on disk loads it by path
(checked with grep across `.py`/`.tsv`/`.json`/`.md`; only NOTES.md prose and the manifest entry named it), it is
strictly superseded for this job's purpose by `lines_g` (same lines, more top margin, identical bottom edge and
segment/stitch method), and it is bit-for-bit reproducible any time from `clair349_f9_right_full.jpg` with the
recorded command (`--top-margin 0`, i.e. omitted). `images/` is 31 MB after (mostly `fr20974_p57_native.jpg` 6.0 MB,
`fr20974_p69_native.jpg` 6.4 MB and `images/atlas/` 7.5 MB, all pre-existing). Recipe recorded in
`images/manifest.json` (new entry: source command, band-identity confirmation, stitch method, why `images/lines`
was deleted and how to regenerate it).

**Grades (rule 4):** no reading claimed this step -- a transcription-crop recipe, not cryptanalysis.

**Hosts:** none (all from `clair349_f9_right_full.jpg`, already on disk; no Gallica or other host request). No
subagents this step (step 1 is this worker's own scripted/visual work, consistent with ZX-349's and ZX-KEY349's
precedent of not spawning subagents for crop/atlas steps).

Files: `tools/iiif_lines.py` (new `--top-margin` option), `images/lines_g/line01.jpg`..`line33.jpg` (new),
`images/manifest.json` (new entry), `images/lines/` (deleted, 33 files). Status stays `partial`. cost: see the lane
ledger.

**Step 2: two fresh blind passes, with a gloss column.** Two Sonnet subagents (the brief's cap of 2, run together),
each given only `images/lines_g/line01.jpg`..`line33.jpg`, `images/atlas/sheet.jpg` and `images/atlas/atlas.tsv` --
not each other, not `passC.tsv`/`passD.tsv`, not `key_alpha.tsv`/`key_nomen.tsv` -- with the brief's rules verbatim
(z-curl = digit 2, never a separator; bar/slash = `|` word divider, its own token; every other mark an atlas code or
`X?` with a description; keep S34/S69/S76 apart; small letters ABOVE a token go in a `gloss` column on that token's
own row, blank if none, `?` if present but illegible; skip the BnF stamp and the "2429"/"3" archival numbers).
Waited for each subagent's own completion report (not just file-on-disk existence -- checked live subagent status
with the agent list before committing passF.tsv, since the file had already appeared on disk while the agent still
showed `running`, exactly the ZX-349 trap) and verified the committed file's row/kind/grade/gloss counts against
what each subagent's own report claimed before every commit.

`passE.tsv`: 1101 tokens (560 digit / 361 sign / 111 X? / 69 divider; 70 H / 1031 M; 142 non-blank gloss).
`passF.tsv`: 1019 tokens (549 digit / 257 sign / 119 X? / 94 divider; 355 H / 664 M; 58 non-blank gloss). Both
subagents independently flagged short cursive fragments in several lines that read as plaintext-looking French
words/phrases sitting in a larger, more fluent hand than the tiny digit-glosses (passE: lines 07/11/14/17/18/19/31/33;
passF: recurring "qual sua"/"quel"/"fait"/"fau..." across several lines) -- both treated these as a third thing,
neither cipher nor gloss, and recorded them as `X?` rather than invent a token kind the brief didn't define. This
matches YX-TR349B/ZX-349/ZX-349B's earlier "plaintext fragment bleeding through" calls and ZX-KEY349's identification
of the interlinear hand as a contemporary decipherment -- consistent with there being *two* distinct annotation
layers above the code line (the small per-token gloss letter, and occasional larger marginal words), not one.

**Step 3: reconciliation, gate, and gloss agreement.** `tools/reconcile_passes.py` had no notion of a `gloss` column
(it recognises `sign`/`token`/`group`/`code` and `conf`/`confidence`, nothing else) -- per transcription.md/CLAUDE.md
Usage item 8, added optional gloss support to the shared tool rather than a private script: `load_pass` now returns
`(sign, flagged, gloss)` triples (gloss `''` where a pass has no `gloss` column, so every other target's existing
invocation is byte-for-byte unaffected -- confirmed with `tools/tests/test_reconcile_passes.py`, both checks still
pass); when any loaded pass has a `gloss` column, `ciphertext_draft.tsv` gains a `gloss` field (majority value per
aligned column, blank where neither pass wrote one) and the run prints a separate gloss-agreement figure over
columns where every pass had a token there and every one of them wrote a non-blank gloss.

`python3 tools/reconcile_passes.py passE.tsv passF.tsv --crops images/lines_g --rows`:

```
line  A-signs  B-signs  agree  cols  share
01  29  31  18  33  0.55
02  38  26  14  41  0.34
03  38  32  15  44  0.34
04  25  30  13  33  0.39
05  30  30  16  33  0.48
06  38  37  16  40  0.40
07  36  37  22  39  0.56
08  32  31  20  34  0.59
09  38  37  20  41  0.49
10  34  34  18  40  0.45
11  44  41  17  48  0.35
12  33  28  11  36  0.31
13  38  39  23  40  0.57
14  33  36  20  37  0.54
15  34  30  16  35  0.46
16  31  34  17  37  0.46
17  31  28  15  32  0.47
18  32  30  15  34  0.44
19  31  37  15  38  0.39
20  29  27  11  32  0.34
21  32  31  13  35  0.37
22  31  32  16  35  0.46
23  27  27  11  29  0.38
24  35  31  12  37  0.32
25  30  27  13  31  0.42
26  34  30  15  37  0.41
27  30  29  14  32  0.44
28  33  30  19  36  0.53
29  30  21  12  30  0.40
30  33  27  10  34  0.29
31  50  29  15  51  0.29
32  34  29  13  34  0.38
33  28  21  9  33  0.27
lines 33  signs A 1101  B 1019  agree 504/1201 = 42.0%  (nw)
disagreement columns 697; draft signs 1201, of which M 744
gloss agreement (aligned columns where every pass wrote a gloss): 10/19 = 52.6%
```

**Gate call: FAILS.** 42.0% pooled, against the brief's 60% line and beside ZX-349's 39.3% (same 60% gate, the
un-margined `images/lines`, no gloss column) -- the recut with the gloss band moved the number by +2.7 points, not
past the gate. No line reaches 0.60; the best is line08 at 0.59, then line13 at 0.57. **Gloss agreement is worse
than token agreement and rests on a tiny sample**: only 19 of 1201 aligned columns have both passes writing a
non-blank gloss at all (most gloss cells are blank in one or both passes -- passE wrote 142 non-blank glosses,
passF only 58, over 2218 pooled ciphertext tokens, i.e. each pass caught a gloss mark on roughly 5-14% of tokens,
not "many" as the brief's own step 2 instruction assumed), and of those 19, only 10 agree on the letter (52.6%).
This is consistent with ZX-KEY349's own account of reading the gloss: a careful, zoomed, native-resolution read of
isolated hand-picked instances (about 20 checked in total, all agreeing with the key) -- not a full blind pass over
compressed line-wide crops, which is what steps 2-3 here actually tested.

`ciphertext_draft.tsv` (regenerated, both columns as the brief asks): header `line position sign gloss confidence
alt why`; `sign` carries the brief's "token" (kept the tool's existing column name rather than rename it project-wide);
`confidence` is H where the passes agree, M where the reconciler took the majority/one side, exactly as
`disagreements.tsv`/`agreement.tsv` (regenerated, replacing the passC/passD-based versions) already documented for
the sign column; the `gloss` column follows the same rule (H/M is not repeated per-gloss -- one confidence field per
row, as the brief's phrasing implies by describing one combined row).

**Step 4: key-vs-gloss consistency.** New script `key_vs_gloss.py` (target-specific, not a shared-tool candidate):
for every column where both passes wrote the *same* non-blank gloss (the 10 agreed-gloss tokens from step 3, found
by re-running the same alignment via `tools/reconcile_passes.py`'s own `load_pass`/`columns` functions rather than
reimplementing alignment), compares that gloss against `key_alpha.tsv`/`key_nomen.tsv`'s value(s) for the column's
consensus code, and writes `key_vs_gloss.tsv` (code, key_values, n_agreed_gloss_tokens, n_match, n_mismatch,
match_share, example_mismatches).

```
code    key_values      n_agreed_gloss_tokens  n_match  n_mismatch  match_share
104     V               2                      0        2           0.00   (both glossed 'u')
10      (not in key)    1                      0        1           0.00
115     (not in key)    1                      0        1           0.00
12      A               1                      1        0           1.00
167     (not in key)    1                      0        1           0.00
23      (not in key)    1                      0        1           0.00
S30     N               1                      0        1           0.00
S37     T,fit           1                      0        1           0.00
X       (not in key)    1                      0        1           0.00
```

Raw match rate 1/10 (10.0%). **Read with care, not at face value: the sample is 10 tokens.** One of the two
"disagreeing more than once" instances (code 104, both passes glossed `u`) is very likely NOT a real conflict --
104 is V's code (`key_alpha.tsv`), and LESSONS.md's own workflow section already names "French with u for v" as the
standard period-spelling convention this project expects; crediting that convention, the true match rate on codes
actually present in the key is 2/4 = 50% (12/A, and both 104/V-as-u instances), not 1/10 as the raw string compare
shows. The other five mismatches (codes 10, 115, 167, 23, X) are pass-invented tokens not in `atlas.tsv`/the key at
all -- a symptom of the same low pass-agreement step 3 already found, not new information about the key. S30 (key
value N) glossed 'd' and S37 (key values T/fit) glossed 'po' are the two genuine, unexplained disagreements, each
n=1 -- below the brief's "more than once" bar, so **no code disagrees with the key more than once** once the u/v
convention is credited (with it uncredited, only code 104 clears that bar, and per the paragraph above that one
case has a known, non-key-breaking explanation). This step does not resolve any key homograph and does not decode
anything, per the brief.

**Likeliest cause of the still-failing gate (brief's fallback for a FAIL).** Three candidate causes, not mutually
exclusive: (1) **genuine cursive density**, unchanged from ZX-349's own diagnostic -- this hand is hard to
segment and read blind regardless of margin or atlas; (2) **the atlas crops are single exemplars from the KEY
leaf**, a different ink instance in a less cramped hand than the ciphertext's own run-on cursive, so a shape that
is unambiguous on the key leaf can still be hard to match confidently against a similar-but-not-identical
ciphertext stroke -- ZX-349B's finding that concrete ciphertext-side shapes (to-ligature, R-loop) matched the key
only after this worker's own close, non-blind, targeted look, not a blind pass; (3) **new this session, not
previously flagged: `images/lines_g` crops are 3895 px wide** (the full stitched line, following YX-TR349B's own
stitching convention), well over `tools/iiif_lines.py`'s own `--max-width` default of 2400 and the "under the
2500 px reading limit" convention CLAUDE.md's Access playbook names elsewhere for exactly this reason (a wider
image risks the model's own image ingestion downscaling it, losing resolution on the smallest marks -- the tiny
interlinear gloss letters most of all, consistent with each pass catching a gloss on only 5-14% of tokens despite
ZX-KEY349 reading it clearly at native zoom on hand-picked instances). Untested this session (time budget); the
next job could re-cut `lines_g` as the two native two-segment crops (`_s1`/`_s2`, each under 2500 px, each with
the same `--top-margin`) instead of stitching them back into one wide image, and re-run steps 2-3 to see whether
narrower crops raise either agreement figure before concluding the leaf itself is the limit.

**Next job's line (gate failed, per the brief's fallback, not the pass-branch).** Do not decode yet. Try the
narrower (un-stitched, <2500px) crop hypothesis above first, since it is cheap (recut + two passes, no new
key-reading needed) and, if it moves the gate, avoids hand-settling `disagreements.tsv`'s ~700 columns against a
leaf this hard to read blind; if it does not move the gate, hand-settle `disagreements.tsv` from the image (ZX-349's
option (a), still not attempted) is the remaining path before any `tools/decode_key.py` run, fr16-corpus judge, or
re-derivation.

**Grades (rule 4):** no reading claimed this session -- steps 2-4 are transcription, reconciliation and a
key-consistency check, not cryptanalysis; the interlinear gloss itself stays grade C (known plaintext, per
ZX-KEY349) only where a human or a future careful non-blind pass actually reads it, not from this session's blind
passes.

**Hosts:** none (all from images already on disk). Subagents: 2 (the brief's cap), run together, Sonnet, step 2
only.

Files: `passE.tsv`, `passF.tsv` (new, this session's blind passes); `disagreements.tsv`, `ciphertext_draft.tsv`,
`agreement.tsv` (regenerated from passE/passF, replacing the passC/passD-based versions); `key_vs_gloss.py` (new),
`key_vs_gloss.tsv` (new); `tools/reconcile_passes.py` (new optional gloss-column support, tests still pass).
Status stays `partial`. cost: see the lane ledger.

## ZX-TR349D (25 Sept 2026)

Intake gate `partial`, exit 0 (orchestrator 15:44 UTC). Brief: `.claude/briefs/runs/2026-09-25-lane-zx-tr349d.md`,
common `.claude/briefs/runs/2026-09-25-lane-zx-COMMON.md`. Opus worker, Opus subagents (the brief overrides the
COMMON's Sonnet line for this job), wall-clock box 100 minutes from 18:22:58 UTC. No host requests.

**Step 1: crops under 2500 px.** `tools/iiif_lines.py --image clair349_f9_right_full.jpg --top-margin 45 --prefix
f9right --debug` (default `--max-width 2400`, default overlap): same 37-band detection as lines_g (pitch 119, distance
83, prominence 207.4; bands 4-36 = line01..line33). The two native segments of each line are kept apart, not stitched:
`images/lines_h/lineNN_s1.jpg` (page x 0-2400) and `_s2.jpg` (page x 1495-3895), 2400 px wide each. Overlap page x
1495-2400; counting boundary page x 1950, drawn on every crop as two small red ticks (5x12 px) at the top and bottom
edges only (s1 x=1950, s2 x=455), so no mark in the text band is covered; the passes were told to stop s1 and start s2
at the ticks, a straddling token going to the side holding its centre. Recorded in `images/manifest.json` (overlap
x-range, boundary, per-crop boxes). `images/lines_g` deleted (the stitched 3895 px form of the same segments,
reproducible from its manifest recipe). `images/` after: 31,332,255 bytes = 29.9 MiB (31.3 MB decimal; it was 31.08 MB
before this job, so the swap added 0.25 MB; under the cap read as MiB, marginal read as decimal -- logged, nothing else
deleted). Eye-check: line01 (s1 carries the stamp and "Monsieur", s2 the "2429"; codes and the gloss above them fully
visible, e.g. glosses above 64 12 73 Ao 26 9 16 104), line17 (short band, 147 px; gloss letters above each code visible,
a sliver of line 16 at the top), line33 (last line whole, blank margin below). No clipping of a line's own codes or
gloss seen.

**Step 2: two blind passes, four Opus subagents.** One prompt for all four (scratchpad copy, summarised here): only the
lines_h crops for the subagent's range, `images/atlas/sheet.jpg`, `atlas.tsv` and the Sxx crops; the ZX-TR349C rules
(z-curl is digit 2; `|` divider its own token; atlas code or `X?` with a description; S34/S69/S76 kept apart; small
letters above a code in that row's `gloss`; larger marginal plain words kind `plain`; skip stamp and "2429"/"3"); stop
s1 and start s2 at the red ticks; zoom sub-regions 2x wherever a mark is small; one added hint about the hand (the 4
is a cross-like stroke with a tail, a digit not a sign). Pass G = G1 (lines 1-17) + G2 (18-33); pass H = H1 + H2;
no subagent saw another's output. Each file was committed only after its subagents' completion reports arrived.
Assembly: kind `numeral` (the subagents' word) written as `digit`, as in passE; `plain` rows carry a `w:` prefix on
the token so `tools/reconcile_passes.py` drops them from alignment by its existing rule (no tool change needed).

| pass | tokens | digit | sign | X? | divider | plain | non-blank gloss |
|---|---|---|---|---|---|---|---|
| passG.tsv | 1233 | 805 | 278 | 41 | 104 | 5 | 866 |
| passH.tsv | 1201 | 748 | 312 | 35 | 97 | 9 | 863 |

(passE/passF for comparison: 1101/1019 tokens, 142/58 glosses.) What the subagents flagged: (a) **"line11" is two
text rows** in one band (the 3020-3245 gap between band centres is 225 px, about two pitches): the leaf has 34 cipher
rows, not 33; G1 and H1 each transcribed both rows under line 11 (upper row first), so line numbers stay as before;
(b) line 17's last ~5 tokens slope below its crop (read later from the top of line18_s2); (c) H1 reported that the
atlas images did not display in its session, so H's lines 1-17 sign codes rest on atlas.tsv's shape descriptions,
and part of its lines 1-12 reading on the unzoomed crop; (d) recurring unmatched shapes: a "ua"/"na" ligature (G2 and
H2, ~6 times, lines 19-32), a large A fused with a crossed f (H1), a Y stem with a 9-loop; (e) number splits (10+2 vs
102, 2+6 vs 26, 26+4 vs 2+64) are the commonest doubt.

**Step 3: reconciliation.** `python3 tools/reconcile_passes.py passG.tsv passH.tsv --crops images/lines_h --rows` (`--halves` not used: the passes already number positions across the whole line, s1 then s2, so the per-line alignment needs no joining):

```
line  G-signs  H-signs  agree  cols  share
01	24	24	23	24	0.96
02	35	34	29	35	0.83
03	34	35	28	35	0.80
04	33	33	28	33	0.85
05	32	30	25	32	0.78
06	38	41	32	41	0.78
07	37	40	32	40	0.80
08	36	38	25	39	0.64
09	39	43	33	43	0.77
10	36	38	31	38	0.82
11	71	72	52	74	0.70
12	28	36	22	37	0.59
13	39	39	31	40	0.78
14	41	40	32	43	0.74
15	37	39	27	39	0.69
16	37	35	29	38	0.76
17	33	32	18	38	0.47
18	39	39	27	42	0.64
19	35	32	26	35	0.74
20	31	31	26	32	0.81
21	38	34	28	38	0.74
22	37	36	29	38	0.76
23	38	34	26	38	0.68
24	42	40	34	42	0.81
25	32	29	20	32	0.62
26	38	31	17	38	0.45
27	41	34	21	42	0.50
28	39	32	20	39	0.51
29	40	35	26	40	0.65
30	38	33	24	38	0.63
31	35	33	28	36	0.78
32	40	35	25	41	0.61
33	35	35	28	36	0.78
lines 33  signs A 1228  B 1192  agree 902/1276 = 70.7%  (nw)
disagreement columns 374; draft signs 1276, of which M 390
gloss agreement (aligned columns where every pass wrote a gloss): 441/728 = 60.6%
```

**Gate: PASSES.** Pooled token agreement **70.7%** (902/1276 columns) against the 60% gate, beside 39.3% (ZX-349, Sonnet,
un-margined stitched crops) and 42.0% (ZX-TR349C, Sonnet, stitched 3895 px crops with the gloss band). 26 of 33 lines
are at or over 0.60; under it: 12 (0.59), 17 (0.47, the truncated tail), 26 (0.45), 27 (0.50), 28 (0.51). **Gloss agreement 441/728 = 60.6%** (columns where both passes wrote a gloss), against
10/19 in ZX-TR349C: the gloss is now read on about 70% of tokens by each pass, not 5-14%. What changed between the
runs is three things at once (narrower crops, Opus instead of Sonnet, a zoom instruction), so this run does not say
which of them moved the number.

**Key-vs-gloss on the G/H agreed-gloss set (before settling), `key_vs_gloss.py --pass-a passG.tsv --pass-b
passH.tsv`:** 262/441 = 59.4% exact; with the new `--lenient` option (u=v, i=j, a gloss that is the prefix of a word
code such as `po` for pour, a DOUBLES code glossed with its pair) 295/441 = 66.9%. Clean codes (n >= 10, share >= 0.9):
12 A 25/25, 14 A 22/22, S37 T 31/31, S38 T 11/11, 82 O 10/10, 15 N 37/39, S34 R 20/21, S31 P 14/15, 5 D/L 27/30, S29 M
9/10. The systematic mismatches are transcription conventions or atlas confusions, not key errors, on what the
glosses show: `4` glossed f (26/26; the cross-like mark read as a digit 4 is probably F's sign S02, "crossed x joined
to a t", or an f/long-s form -- the hint in the pass prompt about the 4 may have pushed this; logged as a lead, not
settled); `10` glossed u (19/19; 102 = V split as 10 + 2, or 104 split); `S40` (Z) glossed r (7/7; the R-loop sign is
being matched to S40 instead of S33, confirmed by eye on line 02 s1 at x~1450, where the R-loop glossed with the z-form
r follows 60); `S79` (Florence) glossed que/quel (the Y-shape is S32 = Q); `68` glossed ll (the Doubles ll code is 69);
`S35` glossed "so"; `8` glossed a/o (28 or 82 split); `60` (I) mixed t/l/r (12/23 match). The settle step below
inherits these as known confusions.

**Step 4: settle, promote, key-vs-gloss.** The gate passed, so every non-agree column was settled from the lines_h
crops: 683 columns (374 sign, 309 gloss-only), laid out by a scripted alignment (`settle_aligned.tsv`: the
reconciler's nw alignment with both passes' sign, gloss and note per column). 683 columns were more than this worker
could read by eye inside the box, so the settling was done by four Opus subagents under this worker (lines 01-08,
09-16, 17-25, 26-33; they had the crops, the atlas and the two passes' values, not the key TSVs and not each other),
each told to zoom 2-3x on every column and to write G, H, a third value, `DEL` (a column that is an artefact of one
pass splitting a code the other kept whole) or `?`; this worker checked coverage (one settled row per non-agree
column, 684 rows = 683 + 1 added) and eye-checked one pattern (below). Decisions: G 272, H 173, both (gloss choice) 75,
new value 60, DEL 103, unsettled `?` 2 signs (06/22, 11/56). Rules the four applied alike, from the image: 1-0-z tight
= one code 102 (not 10 + 2); `4 4` under one o gloss = 44; `2 6`, `2 8`, `6 4`, `8 2` under one gloss = 26, 28, 64,
82; a two-part gloss (curve plus separate top tick) = e, a one-stroke flagged curve = c; long descenders from the
line above are not glosses. Line 17's sloping tail was confirmed from the top of line18_s2 (G already had it).

`promote_settled.py` (new; `--check` exits 1 if stale) writes **`ciphertext.tsv`**: line, position, sign, gloss,
confidence, source, why; **1174 rows** (1075 cipher tokens + 99 dividers), **593 H** (both blind passes agree on token
and gloss) / **581 M** (settled from the image); 874 rows carry a gloss. Rows per line: 01:24 02:34 03:34 04:33 05:30
06:38 07:37 08:35 09:39 10:35 11:68 (two text rows) 12:33 13:38 14:40 15:36 16:35 17:33 18:38 19:33 20:30 21:34 22:35
23:34 24:40 25:30 26:32 27:37 28:34 29:37 30:33 31:34 32:37 33:34. `ciphertext_draft.tsv`, `disagreements.tsv` and
`agreement.tsv` are the reconciler's G/H outputs of step 3. Plain marginal words (14 rows across the passes) are left
out of ciphertext.tsv.

`python3 key_vs_gloss.py --ciphertext ciphertext.tsv [--lenient]` (full settled gloss set, 872 glossed tokens):
**exact 472/872 = 54.1%; lenient (u=v, i=j, prefix of a word code, Doubles pair) 530/872 = 60.8%.** Match share per
code (n >= 4; `key_vs_gloss.tsv` has all 62, written by the lenient run):

| code | key | n | match | share | | code | key | n | match | share |
|---|---|---|---|---|---|---|---|---|---|---|
| 16 | E | 75 | 63 | 0.84 | | 102 | V | 15 | 14 | 0.93 |
| 26 | E | 55 | 39 | 0.71 | | 44 | O | 15 | 13 | 0.87 |
| 15 | N | 43 | 39 | 0.91 | | 104 | V | 14 | 14 | 1.00 |
| 5 | D,L | 42 | 31 | 0.74 | | 28 | A | 14 | 14 | 1.00 |
| 60 | I | 37 | 17 | 0.46 | | S35 | S | 12 | 1 | 0.08 |
| S34 | R | 36 | 29 | 0.81 | | S29 | M | 11 | 9 | 0.82 |
| 12 | A | 33 | 31 | 0.94 | | S38 | T | 11 | 11 | 1.00 |
| S37 | T,fit | 33 | 32 | 0.97 | | 22 | sc?,pour | 9 | 6 | 0.67 |
| 9 | C,ss | 32 | 25 | 0.78 | | S27 | L | 9 | 4 | 0.44 |
| 62 | E | 28 | 23 | 0.82 | | S16 | Guyse | 7 | 0 | 0.00 |
| 14 | A | 23 | 22 | 0.96 | | S33 | R | 7 | 3 | 0.43 |
| 64 | I | 22 | 7 | 0.32 | | S30 | N | 6 | 6 | 1.00 |
| 7 | V | 22 | 20 | 0.91 | | S52 | ne | 6 | 0 | 0.00 |
| S31 | P | 18 | 17 | 0.94 | | 24 | I | 5 | 2 | 0.40 |
| S32 | Q,n'aye | 18 | 9 | 0.50 | | S28 | M | 5 | 5 | 1.00 |
| 82 | O | 17 | 16 | 0.94 | | 17, 73 | H, Y | 4, 4 | 2, 2 | 0.50 |
| S40 | Z | 16 | 1 | 0.06 | | S23, S44 | armee de mer, nulle | 4, 4 | 0, 0 | 0.00 |

Not in the key at all: 210 of 1075 tokens -- `4` 82 (gloss s 33, blank 21, f 13, o 9), `2` 31 (gloss blank 25), `X`
29, `6` 21, `10` 20 (gloss u 18), `8` 9, `68` 8 (gloss ll 7), and eight singletons. **What the mismatches point at
(leads for the decode job, not settled here):**
1. **The lone `4` glossed s/f (82 tokens) is most likely S36, S's second homophone, not a digit.** Eye-checked at
   line 02 s1 x~1180-1260 (`26` then the mark): a tall stroke from gloss height runs down through a crossing bar,
   the shape of the key's S36 ("x crossed over a long descender"), not a 4 with a separate long-s gloss. The pass
   prompt's one added hint ("the 4 is a cross-like stroke with a tail, a digit not a sign") very likely pushed all
   four passes into this reading; that hint was this worker's and is logged as a fault in the prompt. The ones
   glossed f are candidates for S02 (F, "crossed x joined to a t").
2. `10` glossed u (20): leftover 102/104 splits the settle did not reach (agreed rows were not re-opened).
3. `S40` (Z) glossed r (15/16): the passes match the ciphertext's R-loop to S40; it is R's S33 (seen on line 02).
4. `S35` glossed "so"/"vo" (11/12) and `S32` glossed que/quel: the gloss writes a syllable or word above a sign,
   so a prefix rule is not enough; the decode should read these as word or syllable glosses.
5. Lone `2` / `6` / `8` with blank gloss: the other half of a 26/62/28/82 split in rows the passes agreed on (S4:
   "both passes split 2 e | 6" at 31/8-9, 33/4-5); `68` glossed ll is the Doubles ll code 69.
6. `60` (I) at 0.46 and `64` (I) at 0.32: the crossed-z gloss over 60/64 was transcribed `z`; whether it is a
   secretary-hand i/j or a real z is for the decode job to settle against the key, not here.

Eleven codes (n >= 10, share >= 0.9: 15, 12, S37, 14, 7, S31, 82, 102, 104, 28, S38) account for 230 of 243 glossed tokens agreeing with the key (a selection by
share, so descriptive, not evidence by itself); the overall figures above are the ones to cite. No line has been decoded and
nothing here is a reading; grade C is available for the glossed tokens once the decode job applies the key and reads
the gloss against it.

**Grades (rule 4):** no reading claimed. ciphertext.tsv's confidence column grades the transcription (H two blind
passes agree, M settled from the image), not plaintext.

**Hosts:** none (all from images on disk). Subagents: 8, all Opus, at most 4 at once (4 blind-pass halves, then 4
settlers). Files: `images/lines_h/` (66, new), `images/lines_g/` (deleted), `images/manifest.json`, `passG.tsv`,
`passH.tsv`, `disagreements.tsv`, `ciphertext_draft.tsv`, `agreement.tsv` (regenerated from G/H),
`settle_aligned.tsv`, `settled.tsv`, `promote_settled.py`, `ciphertext.tsv` (all new), `key_vs_gloss.py` (new
`--ciphertext`, `--lenient`; default output unchanged, 1/10 on passE/passF as before), `key_vs_gloss.tsv`
(regenerated). tools/ not touched. Status stays `partial`. cost: see the lane ledger.

**Next job (one line):** decode job: first recode the 82 lone `4`s as S36/S02 from the image (and re-open the
agreed 10/2, 2/6, 8/2 splits), then apply key_alpha/key_nomen with `tools/decode_key.py`, grading glossed tokens C
where gloss and key agree and flagging every gloss-key conflict for a look at the image.

## ZX-DEC349 (25 Sept 2026)

Brief `.claude/briefs/runs/2026-09-25-lane-zx-dec349.md` (Opus, box 75 min from 20:08 UTC). Intake gate re-run 20:08 UTC:
`clair349-este-guise-1556: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`, exit 0.
No host requests. Two Opus subagents (step 0 recoding only).

**Step 0: recodes.** 190 doubtful tokens (every lone `4`, `10`, `2`, `6`, `8`, `68`, and `S40` glossed r) went to two
Opus subagents with lines_h crops (lines 01-21 and 22-33). The second stopped after 12 rows and was resumed once to
finish. Both returned 200 rows, including partner rows. `corrections.tsv` (line, position as in ZX-TR349D's
ciphertext.tsv, old, new, partner, reason, grade M) holds the **172 applied changes**. Ten rows the subagents marked `?` were
left as they were (2/19, 3/13, 8/32, 18/18, 26/7, 27/11, 29/16, 30/18, 32/34, 33/12). The commonest changes: `4` to
S36 about 45 times and `4` to S02 4 times; a digit merged into one code with DEL on its partner about 55 times (102 15,
44 9, 26 9, 82 5, 104 5 and others); `S40` to S33 11 times. All 68s stayed 68: the second digit is a two-loop 8 on
every instance, so it may be the writer's own form of 69. `promote_settled.py` now applies corrections.tsv, and its
`--check` exits 0. ciphertext.tsv has 1123 rows (was 1174).
Key-vs-gloss on ciphertext.tsv (`key_vs_gloss.py --ciphertext ciphertext.tsv [--lenient]`): **exact 544/862 = 63.1%
(was 54.1%); lenient 619/862 = 71.8% (was 60.8%).**

**Step 1: homograph rules, from the gloss.** `build_decode.py` applies them per token and writes each one to
exceptions.tsv with its reason. The counts below are glossed tokens in the pre-recode set (the recount after the recodes
is in exceptions.tsv).
- 22 = **pour**: gloss po/pu 7 of 9, bo 1, w 1, never sc. 3 of the 7 are `|22|` standing alone.
- S37 = **t**: gloss t 32 of 35, never fit.
- 9 = **c**: gloss c 22 of 33. The 3 glossed s sit in receu (01), escrire (02) and ce (03), which need c, so the
  gloss mark there is a c. Never the round-ss double.
- 5 = **d or l**: gloss d 21, l 10. No positional rule separates them. Where there is a gloss it decides (C); the 22
  unglossed 5s stay `d|l` at M.
- S32 = **q** before a V code (gloss q 9), **que** otherwise (gloss que/quel 8), never n'aye.
- S17 = fist where glossed f (1). The other token is unresolved (`fist|Monsr`, M).
- Named transcription confusions where the gloss value is taken at I:
  - S16 (Le Duc de Guyse) glossed d/du, 7 tokens.
  - 68 glossed ll (the ll code is 69), 7 tokens.
  - S35 glossed so/vo/vos, 5 tokens, read as the vous sign S51.
  - A word code inside spelled text glossed with one letter: S52, S23, S76 and others, 12 tokens.
  - Unkeyed `X` with a gloss, 19 tokens.
- Every other disagreement between gloss and key keeps the key value at M.

**Step 2: decode.** Files:
- `decode.json` points tools/decode_key.py at `key_decode.tsv`.
- `key_decode.tsv` is generated by build_decode.py from key_alpha.tsv + key_nomen.tsv. They are unchanged, and
  build_decode.py `--check` exits 0.
- **Deviation, logged (conservative choice):** the brief named `["key_alpha.tsv","key_nomen.tsv"]` directly. Their
  value columns hold `DOUBLES:tt`, `NULLES:n` and upper-case letters, which decode_key.py would print literally. The
  derived table flattens these (tt, NULL, lower case; V as u because the gloss writes u) and is regenerated
  mechanically.
- Other inputs: `gloss_votes.tsv` (the gloss normalised to the key's convention) and `exceptions.tsv` (348 rows).
- Outputs: `reading.txt` (concat style; a space marks a divider; [word] marks word and double codes) and
  `reading_tokens.tsv`. `python3 tools/decode_key.py ciphers/clair349-este-guise-1556 --check`: `reading up to date`
  (exit 0).
- **Grades (1025 tokens): H 41, C 261, M 598, I 103, U 22.** M is large because every token settled from the image (conf
  M) is downgraded to M even when key and gloss agree ("any M in the chain"). There are 22 U tokens: 10 `?` recodes and
  unglossed unkeyed marks.

**Step 3: reading vs gloss** (`reading_vs_gloss.py`; both sides normalised: lower case, j=i, v=u, long s=s; the crossed-z
gloss counts as i; a prefix such as po/pour counts as agreeing):
- (a) all glossed tokens: **703/857 = 82.0%**.
- (b) values taken from the key only, leaving out the tokens whose value came from the gloss itself: **637/785 = 81.1%**.
Per line, agree/glossed: 01:18/22 02:22/26 03:21/26 04:24/27 05:24/25 06:24/26 07:25/29 08:27/28 09:29/30 10:27/30
11:47/55 12:18/24 13:30/32 14:18/26 15:24/28 16:25/27 17:19/25 18:20/27 19:17/24 20:20/24 21:16/25 22:18/23 23:18/24
24:24/29 25:15/22 26:14/23 27:17/25 28:16/19 29:19/22 30:21/27 31:15/21 32:18/21 33:13/15.
All 154 disagreements are listed in `reading_vs_gloss.tsv`. Likeliest causes:

| cause | tokens |
|---|---|
| transcription (settled token) or gloss misread | 69 |
| key cell graded M (mostly 60/64 glossed t/l, S36 glossed f) | 35 |
| gloss misread or transcription on a blind-agreed token | 32 |
| unresolved homograph (5, S17) | 12 |
| gloss abbreviation or a gloss spanning more than one token | 6 |

**Step 4: judge and matched control.** `specs/clair349-este-guise-1556.json` is new (judge {"language": "fr"}, fr16).
```
$ python3 tools/judge_plaintext.py specs/clair349-este-guise-1556.json --file ciphers/clair349-este-guise-1556/reading.txt
FAIL language: score=-1.109, null_p99=-1.904, real_p05=-0.882, real_median=-0.783, mode=both, N=1371
FAIL - clair349-este-guise-1556 (a PASS is a gate for a verifier, not a reading; rule 10)
```
Control: `control_shuffle.py` shuffles the same decoded token values within each line, with dividers fixed, over 5
seeds, and judges them the same way:

| | score | null_p99 | real_p05 |
|---|---|---|---|
| target (same renderer as the control) | -1.081 | -1.906 | -0.878 |
| shuffle seeds 0-4 | -1.644, -1.647, -1.652, -1.650, -1.617 | -1.906 | -0.878 |

The target clears the null by a wide margin and sits about 0.56 above every shuffled control. It still falls short of
the corpus's real-text 5th percentile, so the judge verdict is **FAIL**.

A calibration point from before the recodes: the gloss column itself, rendered the same way (the period decipherer's
own letters, with gaps where no gloss was read), scores -1.545. That is below this reading, so the real_p05 gate is out
of reach for any text with this letter's gaps and word-code debris.

Before the recodes the reading scored -1.152 and the controls -1.65 to -1.70.

The FAIL is reported as a FAIL. Lines 01-17 read as continuous French; lines 18-33 carry word codes such as
[haulte ligue], [armee de mer] and [Le Roy mre] inside spelled text, which are atlas confusions in those lines'
transcription.

**Step 5: what the letter says**, at its grades. `reading_en.txt` holds the normalised French and the English.

Lines 01-17, mostly C and M with some I: Este acknowledges Guise's letters of the twenty-first of the previous month,
written in answer to what Scipion reported about the business he had come for. He is very glad to learn that the forces
Guise is bringing are as Guise writes, both for that business, should an occasion arise to attempt it this way, and for
all other occasions. There is a passage on how things will go, ending "faire ainsi que vous adviserez" (do as you think
fit). A reference to "la pratique du cappitaine" follows (the captain's name is unread).

Lines 18-33 give only fragments: "meilleure volonté", "à ceste heure", "vers lui pour adviser", "que faudra tenir",
"s'espargner", "encores rien", "me fait penser que les choses...". This is the reading at the tokens' grades, not an
edited text.

Not done here (brief): the fresh-session re-derivation (rule 7) and any novelty class (rule 10).

Next job (one line): re-transcribe lines 18-33 against the atlas for the signs coded S21/S23/S74/S76/S80 inside spelled
text (the gloss column gives the target letter for most), then rerun build_decode.py, decode_key.py and the judge.

Files:
- new: `corrections.tsv`, `build_decode.py`, `decode.json`, `key_decode.tsv`, `gloss_votes.tsv`, `exceptions.tsv`,
  `reading.txt`, `reading_tokens.tsv`, `reading_vs_gloss.py`, `reading_vs_gloss.tsv`, `control_shuffle.py`,
  `reading_en.txt`, `specs/clair349-este-guise-1556.json`
- changed: `promote_settled.py`, `ciphertext.tsv`, `key_vs_gloss.tsv`

Status stays `partial`. cost: see the lane ledger.
