# The abbé (R.) de Gravel to Jean-Baptiste Colbert, Ratisbon, 29 Jan 1665, BnF Mélanges de Colbert 127, f.349-350 (canvases 356-357)

**Status: partial** (verifier R10-DEC2678V, 6 Oct 2026: N3, key published, D2 about 73%, AUDIT.md. R9-DEC2678C, 6 Oct 2026: Tomokiyo's published Colbert-Gravel 1672 key passes a pre-registered gate on P2/P3, 11 of 15 tokens H; see the section of that date. Earlier: not attacked; Bourdeau's work-in-progress, see below).
Sender correction (R8-G2678, 6 Oct 2026): the letter is **signed "Guibert", maître des courriers d'Allemagne** (canvas 355, signature crop `images/c355_signature.jpg`), docketed "M. Guibert"; not the abbé de Gravel as DECODE, Bourdeau and this folder's title say. See the section of that date. **Reversed by R9-DEC2678 (6 Oct 2026), see the section of that date:** the Guibert signature is on f.348r, the end of Guibert's own letter (ff.347-348); the cipher letter ff.349-350 closes on f.349v (canvas 357) "a Ratisbone ce 29 Janvier 166[5]" and is signed "[R.] de Gravel[le]", as DECODE, Bourdeau and the BnF sommaire (Fol. 349, l'abbé de Gravel) say.
Premise check (R9-DEC2678, 6 Oct 2026): the brief asked for the title to be changed to Guibert; the image says Gravel, so the title keeps Gravel (now read from the leaf, not only the catalogue), with folios and canvases corrected. The **folder name keeps the old catalogue label** (`...-gravel-1665`), which turns out to be right. No status.json row or spec exists for this folder (checked 6 Oct 2026), so nothing else was edited.
Clément, *Lettres, instructions et mémoires de Colbert* (IA items colbert-lettres-instructions-et-memoires-de-colbert-v-1 to v-7), full-text search (be-api) for "Gravel", "Frichmann", "rixdales" and "Ratisbonne" run by this worker (GF-A2B-1, 3 Oct 2026): Gravel hits only Colbert's own letters to the abbé de Gravel at Mainz (1669-70, t. II pt 2, t. V) and editorial notes; no Gravel letter of 29 Jan 1665 and none of the enciphered pension names.

## Item

DECODE R2678 ("Non-decrypted"). Metadata (Aymeloglu `decode-records.jsonl`): author "[signature illegible to
the uploader]", receiver Jean Baptiste Colbert, region Germany, city Ratisbon, 24-29 Jan 1665, 1 page,
cleartext French, symbol set numerical with diacritics. QUEUE.md row **DC9**, scored `held_by: none`, next
step "transcription", 4 images. That match is **wrong**, corrected below: Bourdeau's repository already holds
this exact record.

Brief: `.claude/briefs/runs/2026-09-24-lane-n-csDC2.md`. de-crypt.org and archive.org not queried directly
(held by other LANE N workers); worked from committed TSVs, QUEUE.md, both solver-repo clones, and one
targeted WebSearch for a print trace.

## Check-solved sweep, 24 September 2026

- **Editions first.** Colbert's standard printed edition, Clément's *Lettres, instructions et mémoires de
  Colbert* (7 vols + supplements, on Gallica/HathiTrust/archive.org), focuses on Colbert's domestic ministerial
  functions (finance, marine, industry, fortifications) and is not confirmed to cover incoming diplomatic
  correspondence from a minor envoy at Ratisbon; not independently fetched this pass (Gallica/archive.org/
  Google Books all outside this brief's host list). One WebSearch for a print trace of this specific
  transaction (`"abbé de Gravel" Ratisbonne 1665 Colbert pension rixdales Allemagne`) returned only BnF
  archival-catalogue pages for neighbouring Mélanges de Colbert volumes (117-150), confirming this material is
  catalogued but not surfacing any printed edition or transcription of it. Bourdeau's own sibling search
  (below) separately checked Clément's edition (t. III, V, VIII) for the same box and found no relevant entry
  (for a related letter, not this one specifically) — the gap is a genuine unknown, not a positive negative
  finding for this exact letter, and is left as a next-worker task rather than a "blocked" verdict, since the
  strongest and most specific evidence (Bourdeau's own transcription and identification of this record) is
  already in hand and unambiguous about non-solution.
- **Web / lists (Cryptiana).** No page in the local `sources/cryptiana/` snapshot names this record or "Mél.
  Colbert 127" (checked by grep); not separately searched live.
- **Bourdeau (github.com/dbourdeau/cyphersolver).** `colbert/NOTES.md`, item **a** (read in full; quoted):
  *"Mél. Colbert 127, f. 349–350 | R2678 | ... 'l'abbé de Gravel' (La Roncière catalogue, t. I p. 270),
  Ratisbon, 29 Jan 1665, to Colbert ('Monseigneur'): receipt of a bill of exchange for 17,100 rixdollars 'pour
  le service du Roy en Allemagne'; the recipients of the pensions are enciphered as two-digit groups with
  overlines ... Names only; a letter/syllable cipher for names with a few code numbers. Different design from
  b–c. **Not attacked** (three names)."* `TARGETS.md` row 4 confirms: project status "stuck" overall (a
  related pair of letters, items b/c, tested against matched controls and not solved), but item a (this
  record) itself was never run through the annealer — only transcribed and identified. Bourdeau's sibling
  search (La Roncière & Bondois printed catalogue of the Mélanges Colbert, and Clément's edition) is complete
  and negative for what is findable online for the related items b/c, not independently re-run here for item
  a specifically.
- **Aymeloglu (github.com/aaymeloglu/unsolved-ciphers).** R2678 appears only in the raw catalogue harvest
  files; no separate write-up.
- **DECODE.** Not queried live (per brief). Census diff has `held_by: none` — **wrong**: `tools/solver_repo_diff.py
  --census`'s Bourdeau match evidently failed on this row (likely a shelfmark-normalisation miss on "Melanges
  de Colbert 127, f.349-350" vs Bourdeau's own "Mél. Colbert 127, f. 349–350"). Flagged in ROOM.md.

**Verdict: open.** This is a small, already-transcribed cipher (a handful of two-digit groups with overlines,
enciphering three pensioners' names and one code number) that another public solver (Bourdeau) has identified
and left untouched ("not attacked") because his project's effort went into two other, larger, related ciphers
in the same set of volumes (items b/c, which resisted a matched-control annealer attack). No solution, key or
published decipherment of this exact record was found. No novelty claim made (rule 10) — a fresh cryptanalysis
of this item would need a transcription (available from Bourdeau's own crop images if he shares them, or a
fresh one from DECODE's images) and is small enough (three names) that dictionary/crib attack on likely
pensioner names in the region may be feasible.

Six-source status: 6/6 checked; 0/6 found a decipherment of this exact record; 1/6 (Bourdeau) holds a verbatim
transcription and context but explicitly did not attack it.

## Capture and passes (24 Sept 2026)

LANE G2 worker K, brief `.claude/briefs/runs/2026-09-24-lane-g2-k-dc8-dc9-capture.md`, cap $7 shared with DC8.

**Ark and folio.** Found via archivesetmanuscrits.bnf.fr's free-text search (plain `POST resultatRechercheSimple.html`
with a JSESSIONID cookie from a prior GET, per LANE G2 worker F's method, QUEUE.md "Fourth pass"): query "Melanges
Colbert 127" surfaces the notice `ark:/12148/cc954302` ("Mélanges de Colbert 127-127bis. Correspondance de Colbert"),
whose pre-expanded sommaire tree names the sub-unit "Mélanges de Colbert 127 • Correspondance de Colbert de janvier
et février 1665" (585 feuillets) and, nested under it, "Fol. 349 • l'abbé « de Gravel »" — an exact match for this
record. `ajaxGetCompDisplay.html?eadCompId=FRBNFEAD000095430_d0e56` gives the digitised-document link:
**gallica.bnf.fr/ark:/12148/btv1b10035540v**.

**Manifest fetch failed; canvases found by content match instead.** `gallica.bnf.fr/iiif/.../manifest.json` and
`/services/Pagination` both answered `curl: (35) Recv failure: Connection reset by peer` every time this session
(logged in `/__agentproxy/status` as `ws_closed_mid_exchange` against `gallica.bnf.fr:443` — proxy-side, not a
Gallica denial: the plain host, `.thumbnail`, and the direct `/iiif/.../fN/.../native.jpg` image endpoint all
answered 200 throughout, just not reliably on the first try for larger payloads). `tools/gallica_folio.py` could
not run without the manifest. Folio-to-canvas mapping was done by eye instead: candidate canvases were fetched
directly by their Gallica image index and checked against Bourdeau's own quoted ciphertext (`colbert/NOTES.md`
item a, github.com/dbourdeau/cyphersolver, shallow-cloned to scratch and grepped, MIT code/CC BY 4.0 text —
credited here, not copied) rather than trusted from a folio-number stamp alone, after an inconsistency: canvas f356
(where the letter's own numeral stamp reads "349") carries Gravel's exact four cipher groups
(`29`; `80 62 41 73 3̄2̄ 51`; "Mr Frichmann" in clear; `48 93 71 37 60 92 580`), an unambiguous content match; an
earlier candidate canvas (f354) also appeared to read "349" on a first pass but carries unrelated content (a
"Sieur du Fresnoy" letter) — most likely a misread of "347" (7/9 are easily confused in this secretary hand), not
re-verified this pass. **Images kept: `images/dc9_letter.jpg`** (the cipher-bearing recto, canvas f356 right half)
and `images/dc9_address_panel.jpg` (the outer address fold, same canvas, left third — reads "Monseigneur Colbert"
in the addressee's own hand, confirming the recipient; a docket note in a filing hand nearby was read once, in
passing, as "M. Guibert" — inconsistent with "Gravel" and not resolved this pass, flagged in `images/manifest.json`
for a future worker rather than guessed at). `images/manifest.json` records both fetch URLs, the identification
reasoning, and the flagged f354 confusion.

**Transcription pass and agreement with Bourdeau.** One pass of this worker's own (`passA.tsv`), read directly
from `images/dc9_letter.jpg` without consulting Bourdeau's transcription first, then compared line-by-line where
the two overlap (`agreement.tsv`): all four cipher groups Bourdeau's NOTES.md quotes are confirmed digit-for-digit
in the same order with the same final values; the only difference is how the longest run (12 digits) is broken
into groups (this pass reads three blocks, Bourdeau's excerpt shows seven pairs) — a spacing/grouping question,
not a digit disagreement, and flagged rather than silently resolved. This pass did not extend the transcription
beyond what Bourdeau's excerpt already covers (item a is a single short page, and his NOTES.md itself says the
item is "not attacked" — meaning no cryptanalysis was attempted on it, not that his own quoted groups are
unreliable; they check out against the image).

**No decoding attempted.** Per the brief, this pass was capture + a transcription/agreement check only; item a's
cipher (three or four names/code-numbers behind two-digit groups with overlines) is still **not attacked** by
anyone as far as this pass found. Status word unchanged: **open**.

Requests this pass (shared host budget with DC8, one fetcher): gallica.bnf.fr ~15 (several connection resets on
full-page/large-crop fetches, one retry per URL per the good-citizen rule, routed around with smaller sizes or
narrower crops thereafter); archivesetmanuscrits.bnf.fr ~6 (shared search session with DC8, ≥1.5s apart, UA
`cipher-lab research script (contact via repository)`); github.com 1 shallow clone of dbourdeau/cyphersolver
(grepped for the colbert/ folder only, not read in full).

## Correction to QUEUE.md

DC9's `held_by` should be `bourdeau:colbert`, not `none` — flagged in ROOM.md, 24 Sept 2026, for the LANE N
orchestrator to correct the census-diff matcher (shelfmark normalisation across "Mélanges"/"Melanges"/"Mél."
spellings and accent-stripping should be checked).

## LANE N audit, 24 September 2026

**Normaliser fixed.** `tools/decode_neighbours_exclude.py`'s `volume_keys()` now folds combining diacritics
(`unicodedata.normalize('NFKD', ...)`, so "Mélanges"/"Melanges"/"Mél." all reduce the same way) and adds a
`mel(anges?)?\.?\s*(?:de\s*)?colbert\.?\s*(\d+)` pattern. Confirmed against this record's own two forms —
holder_raw "Melanges de Colbert 127" (no accent) and the census's abbreviated `shelfmark_code`
"BnF_Mel127_f349" (no "Colbert" at all, caught via holder_raw) — both now produce the volume key `bnf
melanges colbert 127`, matching Bourdeau's `colbert/NOTES.md` ("Mél. Colbert 127, f. 349–350"). Regression
cases added to `tools/tests/test_solver_repo_diff.py` (DC6/DC9 shapes); `tools/tests/test_solver_repo_diff.py`
and the tool's own `--help` both pass. Census diff regenerated: R2678's `held_by` is now `ours:catalog` (this
folder + QUEUE.md both now name it by id, which already wins over the volume match) and its `bourdeau_hit`
field, previously blank, now correctly shows `colbert[not read]` — the field the original miss was about,
even though `held_by`'s own top-level value had separately been fixed already by this folder's own creation.
Full `sources/decode/records-non-decrypted-2026-09-24-diff.tsv` regenerated and committed; isolating the
normaliser's own marginal effect (same run, normaliser reverted, current repo state otherwise unchanged) found
0 additional `none`→held rows — the 71→60 `none`-count drop between the stale and fresh diffs is entirely
attributable to six check-solved folders (this one plus DC1/DC2/DC4/DC6/DC7) having been created since the
stale diff was generated, not to the normaliser. The normaliser fix is nonetheless real and matters for the
*next* first-pass census run made before such folders exist — which is exactly the shape of miss DC6/DC9 were.

**DocumentsList check** (`DocumentsList?showmaster=records&fk_id=2678`): **"No records found"**. RecordsView:
`Available Documents:` (empty), `Inline Cleartext: Yes`, `Inline Plaintext: No`. No change to the verdict:
still **open**, cryptanalysis, Bourdeau's "not attacked" lead stands. Status word unchanged.

**DECODE login (shared across DC1/DC2/DC4/DC5/DC8/DC9), 24 Sept 2026.** One login
(`tools/decode_browser_login.js`), `--fetch-page` for RecordsView/1411, /1162, /9970, /2754, /2678 plus
`DocumentsList?showmaster=records&fk_id=` for all six ids (4450, 1411, 1162, 9970, 2754, 2678), `--delay 1700`.
**Tool bug found and fixed**: `safeFilename()` derived a page's saved filename from the URL's last path
segment only, so six `DocumentsList?...&fk_id=N` URLs (same path, different query) all collided on
`DocumentsList.html`, silently overwriting all but the last on a first attempt (`--max-files 11` also let
auto-discovery pull ~10 unwanted thumbnail images that pass hadn't asked for). Fixed to fold the query string
into the filename when present (`tools/decode_browser_login.js`), added `require.main` guards so the module is
requireable without touching Playwright/network, and an offline unit test
(`tools/tests/test_decode_browser_login_safefilename.py`, passes, no credentials/network). Re-ran clean with
`--max-files 0` (no `--fetch`, so 0 is correct for "no auto-discovered extras" — the fetch-page URLs are not
gated by `--max-files`); all 12 pages saved distinct, no attachment images pulled. Account name (visible on
every fetched page's nav bar) not quoted anywhere in this file or committed; no raw HTML committed. Total
de-crypt.org requests this job: 1 login + 6 RecordsView + 6 DocumentsList = 13 on the first (partially wasted)
attempt, + 1 login + 6 RecordsView + 6 DocumentsList = 13 on the clean re-run = **26 total**, all ≥1.6s apart,
well under the brief's 80-request cap.

## Solver-repo check (bourdeau, 2 Oct 2026)

Fresh shallow clone of github.com/dbourdeau/cyphersolver, HEAD 34e0fc89 (1 Oct 2026), diffed against this folder on 2 Oct 2026 (worker SOLVERDIFF-BOURDEAU, sources/solver-diffs/2026-10-02-bourdeau.tsv). Match class b (they attempted it and closed or explained it).
- Their page: https://github.com/dbourdeau/cyphersolver/blob/main/targets/colbert/NOTES.md ; TARGETS.md #4
- Their extent, in their words: attempted 16 Sept, stuck: Gravel (R2678) and Charost passages are one key; three designs tested against matched controls; not read
- Their date: 16 Sept 2026
- Note: already cited in our NOTES.md
Credit: D. Bourdeau, cyphersolver (code MIT, text CC BY 4.0). Status line unchanged; the parent decides any status change from the ROOM flag.

## Web and blog check (GF-A2B-1, 3 Oct 2026)

Plain web searches (WebSearch, 3 Oct 2026):
1. `"abbé de Gravel" Colbert Ratisbonne 29 janvier 1665 lettre de change rixdales pension` -- franco.wiki Robert de
   Gravel biography, isidore.science and Heidelberg HÜB records (Diet of Regensburg material), Zunz archive. Nothing on
   this letter or its enciphered names.
2. `"Mélanges de Colbert" 127 chiffre Gravel 1665` (shelfmark + cipher) -- BnF comité d'histoire notes on the Mélanges
   de Colbert collection, a Europeana Gallica record for another volume, generic Colbert pages. No hit.
3. `"Frichmann" 1665 Ratisbonne pension Gravel` (the one clear-text name in the cipher passage) -- no page naming
   Frichmann with Gravel; Wikipedia disambiguation, franco.wiki again.
4. `Gravel to Colbert Ratisbon 1665 cipher DECODE 2678 Tomokiyo unsolved Colbert correspondence` (descriptive title) --
   warhistory.org "Intelligence in the Era of the Sun King Part I" (general), TNA blog on a 350-year-old deciphered
   message (a different item), Cipherbrain 2020-06-14 "a king's encrypted letter on Satoshi Tomokiyo's list" -- opened
   with its 14 comments: a Charles I letter of 1648; no comment mentions Colbert, Gravel or Ratisbon.
Blog site searches:
5. Cipherbrain (`site:scienceblogs.de klausis-krypto-kolumne Colbert Gravel Mélanges cipher`): only author/archive
   index pages, no post on the Colbert/Gravel items.
6. Cryptiana (`site:cryptiana.blogspot.com Colbert Gravel`): no cryptiana.blogspot.com page returned. Tomokiyo's
   unsolved-list entry (the source of DECODE R2678's upload) is on disk under sources/cryptiana/ and was grepped on
   24 Sept with no decipherment.
7. Cipher Mysteries (`site:ciphermysteries.com Colbert cipher 1665 Gravel`): ciphermysteries.com/?p=7357 and
   "17th century cipher mystery meme" (2015-11-14) -- about the 1676 "Devil's letter" meme, not Colbert or Gravel.
No decipherment or plaintext of R2678 found in any post or comment thread. Requests: WebSearch 7, scienceblogs.de 1
(WebFetch), archive.org 1 (advancedsearch) + be-api.us.archive.org 13 (>=1.6 s apart).

## Premise check (GF-A2B-1, 3 Oct 2026)

(a) Folder's own mentions -- not found: no decipherment, gloss or clear copy is mentioned for item a; DocumentsList
"No records found" (LANE N audit above). The only clear text in the passage is the amounts and "Mr Frichmann".
(b) Other solvers' working files -- found (context, no rendering): dbourdeau/cyphersolver (shallow clone, HEAD e8b4287,
2 Oct 2026) `targets/colbert/NOTES.md` row a: R2678 transcribed and identified, "Not attacked (three names)";
item 6 repeats "Not attacked". No key file, rendering or apply-key script for item a in `targets/colbert/`
(files: control.py, solve_mono.py, solve_regions.py, ct_shared.txt work items b-c only). Correction to this file's own
"Solver-repo check (bourdeau, 2 Oct 2026)" section: Bourdeau's "the Charost and Gravel passages are one key" refers to
his item c (R2733, the abbé de Gravel's 1674 Mainz letter copied to Maulevrier), not to this record; his NOTES call
item a "a different, smaller cipher". aaymeloglu/unsolved-ciphers (HEAD d2800bb, 27 Sept): R2678 only in the
catalogue harvest (cited, not copied).
(c) Physical neighbours -- partly found: this folder's 24 Sept capture viewed canvas f356 (the cipher recto, Gallica
btv1b10035540v) and its address panel; Bourdeau names canvases 355-356 for ff. 349-350. A docket note read once as
"M. Guibert" is still unresolved. The facing page and canvas 355 were not re-viewed at native resolution this pass
(no Gallica requests in this gate-fix); no clear copy or decipherment is recorded beside it by either reader.
(d) Recipient-side editions -- searched, not found: Colbert is the recipient; Clément's edition (status-line citation
above) carries no Gravel letter of January 1665. The sender-side series (Gravel's dispatches from the Diet,
Archives des Affaires étrangères, Correspondance politique Allemagne; Auerbach's *La diplomatie française et la cour
de Saxe*/Recueil des instructions for the Diet) was not searched in this pass.

## While waiting

Next action that depends on nobody: re-view canvases 355-356 of btv1b10035540v at native resolution (facing page,
docket, any slip) through `tools/gallica_folio.py`/`tools/iiif_lines.py`, then a crib test of the three enciphered
names against the Diet of Regensburg pensioners of 1664-65 (Fürstenberg circle, Rhine League envoys) named in
Gravel's printed dispatches.

## fr17 re-judge (FR17-RJ2, 3 Oct 2026)

No reading on disk -- no reading: status open, passA.tsv transcription only, no decoding attempted (NOTES 'No decoding attempted'). No judge run (fr16 or fr17), no shuffled-decode control, no per-fold rate at a reading's N; the fr17 per-fold rates at N=138/300 are in tools/data/fr17/README.md.

## Next step (NO-CRACKS, 5 Oct 2026)

next: re-view canvases 355-356 of btv1b10035540v at native resolution (facing page, docket, slip) with tools/gallica_folio.py and tools/iiif_lines.py, then a crib test of the three enciphered names against the 1664-65 Regensburg pensioners named in Gravel's printed dispatches, ~$2. Who acts: agent. Source: this file's "Next action that depends on nobody"; written by NO-CRACKS (account 3) because tools/next_steps.py found no next-step line in this file.

## Canvases 355-356 re-view and crib test (R8-G2678, 6 Oct 2026)

Manifest fetched once with `tools/gallica_folio.py btv1b10035540v` (595 canvases, every label "NP", cached at
sources/gallica-manifests/btv1b10035540v.json); canvases 355 and 356 viewed whole at 1400 px, then four native
crops (`images/manifest.json`, entries by R8-G2678).

**Canvas 356** (as on 24 Sept): left = the outer address leaf ("Monseigneur / Monseigneur Colbert", two seals);
right = f.349r, the letter's first page with all four cipher passages. Docket, rotated, on the address leaf
(`images/c356_docket.jpg`): **"M. Guibert / [?] Janv. 166[5]"** -- the 24 Sept read "M. Guibert" is right.

**Canvas 355** (not viewed before): right = the letter's second page (folio stamp read "348" at 1400 px; not
re-read at native size, M), six closing lines (`images/c355_closing.jpg`): "d'attendre ces Rixd[alles] jusques
au premier Juillet prochain, que l'on ne manquera pas de les luy payer. J'attends en particulier cette grâce de
v[ost]re générosité après tant d'autres que nous avons receues en général et que vous croirez avec tout le
respect que je doibs" -- then "Monseigneur", the date line bottom left **"ce 29 Janvier 166[4/5]"** (last digit
looks like 4 by eye, M; the docket reads 1665), and the subscription (`images/c355_signature.jpg`):
**"V[ost]re très humble et très obéiss[an]t serviteur / Guibert m[aîtr]e des cour[rier]s d'Allemagne / a[ncien?]
directeur des bureaux de Normandie [et] Bretagne"** (name H; title words M). Left of canvas 355 = blank verso
with bleed-through. No slip, gloss, decipherment or clear copy on either canvas. No place name was seen on
either page: "Ratisbon" (DECODE metadata) is not on these two canvases.

What this changes (findings, not novelty claims): the writer is Guibert, a postal official (master of the German
couriers), not Gravel. The 24 Sept "Guibert vs Gravel" flag is resolved in Guibert's favour. The catalogue label
"l'abbé de Gravel" (La Roncière t. I p. 270, via Bourdeau) may name the person the letter concerns rather than the
writer; one reading consistent with the text is that `29` (15,000 of 17,100 Rd, a single code group) is Gravel or
the Diet envoy who distributes the money -- grade I, inferred only, not tested. The money arithmetic closes:
15000 + 500 + 600 + 1000 = 17100, the bill named in line 3, so every amount (including passA's "600 or 60") is
confirmed.

**Crib test: pre-registered, judged a non-test, not run** (`PREREG-crib-2026-10-06.md`, pushed 3dc99035a before
any candidate was tried). The 12 groups of the two spelled names are all distinct, so under any letter or syllable
substitution every candidate name of compatible length fits and so does every control name: the control cannot
fail differently from the target (CLAUDE.md rule 3, AX-5799/bCAS shape). No candidate list was drawn up and no
name is reported as fitting. The premise of the brief's candidate source ("Gravel's printed dispatches") is also
weakened by the sender correction. Grades: no token read (0 H, 0 C, 0 S, 0 M, `29`=Gravel 1 I).

Next (one line each, not done here): (1) find another Guibert-to-Colbert letter of Jan-Feb 1665 in Mélanges de
Colbert 127/127bis (same volume, btv1b10035540v; the BnF sommaire tree, ark:/12148/cc954302, lists writers per
folio) that uses the same two-digit groups -- the only route to a crib test that can fail; ~$2; (2) read La
Roncière t. I p. 270's entry for f.349 to see why it names Gravel.

Requests this job: gallica.bnf.fr 9 (1 manifest, 2 canvas overviews, 6 region crops; >= 2 s apart, all HTTP 200);
github.com 1 (shallow clone of dbourdeau/cyphersolver, grepped for item a).

## Writer re-check and sibling-letter search (R9-DEC2678, 6 Oct 2026)

Brief: `.claude/briefs/runs/2026-10-06-account1-run9-jobs.md` "R9-DEC2678": (1) change the premise to Guibert, (2) search
for other Guibert letters to Colbert. Step (1) was checked against the leaves before being applied, and the
leaves contradict it.

**Leaf order (Gallica btv1b10035540v, labels all "NP"; folio stamps read on the images).**
- Canvas 354 right = **f.347r** (stamp "347"): "Monseigneur / Pardonnez la hardiesse que je prens d'interrompre vos
  grandes occupations pour me plaindre a vous de la continuation ... M. du Fresnoy ... M. Boulliau(?) m[aîtr]e des
  courriers de Champagne et moy ..." (words M, read at 1400 px). Guibert's letter, in clear (`images/c354_overview.jpg`).
- Canvas 355 right = **f.348r**: the end of that letter, "ce 29 Janvier 166[4/5]", signed Guibert (R8's crops).
- Canvas 356 left = **f.348v**: Guibert's address leaf with his docket "M. Guibert / Janv. 166[5]"; right = **f.349r**,
  the cipher page (R2678).
- Canvas 357 left = **f.349v**: the end of the cipher letter, in clear: "... qui me sont deubs, si ce n'est, Monseigneur,
  que vous ayez eu la pensée de me les faire payer par quelque autre voye, sur quoy je me remets au bon plaisir de Sa
  Ma[jes]té. Il me suffit que les autres soient satisfaits ..." (words M), dated **"a Ratisbone ce 29 Janvier 166[5]"**,
  signed **"Vostre tres humble et tres obeissant serviteur / [R.] de Gravel[le]"** (name H at native resolution, initial M;
  `images/c357_dateline_subscription.jpg`, `images/c357_signature.jpg`). Right = f.350 (stamp "350"), blank at 1400 px.

So R8-G2678 joined f.348r (the end of Guibert's letter) to f.349r (the start of Gravel's): the two pages face each
other across canvases 355-356, but f.348r comes before f.349r, so it cannot be the second page of a letter that begins
on f.349r. Gravel is the writer: the signature on f.349v, the place "Ratisbone" (which R8 could not find because it is on
f.349v), the BnF sommaire (`archivesetmanuscrits.bnf.fr/ark:/12148/cc954302`: "Fol. 347 · « Guibert », maître des
courriers d'Auvergne [sic, BnF's reading] et directeur des bureaux de la poste de Normandie et Bretagne" and "Fol. 349 ·
l'abbé « de Gravel »", two separate entries), and DECODE's f.349-350 all agree. R8's inference "`29` = Gravel, the
distributor" (grade I) loses its basis, since Gravel is the writer, and is withdrawn. What R8 read on f.348r ("d'attendre
ces Rixd[alles] jusques au premier Juillet ...") belongs to Guibert's letter, not R2678. R8's amount arithmetic
(15000 + 500 + 600 + 1000 = 17100) is on f.349r itself and stands. Grades: no cipher token read (0 H, 0 C, 0 S, 0 M, 0 I).

**Sibling search: Guibert (as briefed) and Gravel (the real writer).** Thumbnail-level looks only, no decoding.

| Where | Searched | Result |
|---|---|---|
| BnF sommaire, Mél. Colbert 127-127bis (cc954302, 330 "Fol." entries) | grep Guibert, Gravel, courrier, chiffr, poste, Frichman | Guibert only at **Fol. 347** (this neighbour, clear). Gravel at **Fol. 349** (R2678) and **127bis Fol. 968, 1078** ("R. de Gravel") |
| BnF sommaire, Mél. Colbert 126 (Dec 1664; cc954291, 177 entries) | Guibert, Gravel, courriers | none |
| BnF sommaire, Mél. Colbert 128-128bis (Mar-Apr 1665; cc954319, 343 entries) | same | none (only "Graveline", the town) |
| 127bis f.968r-v, Gallica btv1b100355703 canvases 390-391 (anchors: canvas 389 = f.964, 393 = f.971, 394 = f.972) | look at 1000 px | Gravel to Colbert, **in clear**: reimbursement of the "ports des lettres" he advanced (via Louvois; a signed statement sent to "le S[ieu]r Pachau(?), commis de M. de Lionne") and his appointments, last remittance made at Frankfurt; dated "[?]bourg le [?] feb. 1665", signed "R. de Gravel", docket "M. de Gravel ... feb. 1665". No cipher groups seen |
| 127bis f.1078r-v, canvases 501-502 (anchor: canvas 499 = f.1076) | look at 1000 px | Gravel to Colbert, **in clear**: "J'ay receu advis du sieur H[e]nsel(?) que vous aviez eu la bonté de luy faire remettre l'argent des ports de lettres ..." about the Diet ("cette assemblée"); dated "a Ratisbonne ce [1?]6 [févr]ier 1665", signed Gravel. No cipher groups seen |
| DECODE RecordsView (login-free metadata): R2673, 2674, 2677, 2679, 2680, 2681, 2682, 2683 (every Colbert-volume record from 1662 to 1665 in the 24 Sept listing) | Author/Receiver/City | Nuchèze ×2, Fremont (Lisbon), Millet ×2 (Warsaw, Danzig), Schomberg, La Haye ×2. **No Guibert or Gravel** besides R2678 and R2733 (Gravel to Maulevrier, 1674, Aymeloglu harvest) |
| Google Books API (key, country=US): "Guibert" "maître des courriers"; "Guibert" "courriers d'Allemagne"; "Guibert" courriers Colbert 1665 | snippets | 8 / 334 (noise) / 2 hits: Vaillé, *Histoire générale des postes françaises* (Pierre Guibert, maître des courriers, 1644; a Guibert collecting a postal levy); *La Poste à Nantes* (Guibert, "l'homme de confiance" ...); La Roncière's *Catalogue des manuscrits ... Mélanges de Colbert* (1920) matches with no snippet. No cipher letter of Guibert cited |
| IA full text (be-api fts) "Guibert" "courriers" Colbert | top 10 | 7,928 hits with the terms ORed; top 10 unrelated (the comte de Guibert, the antipope Guibert, Colbert manuscript lists). Noise, not a search result on this question |

Finding for the "Next (1)" step: no other Guibert letter exists in Mél. Colbert 126-128bis, and Guibert's one
letter (ff.347-348) is in clear. The writer's two other letters in the same series (127bis ff.968, 1078, Feb 1665) are
in clear at thumbnail level, so neither gives a second text in the same two-digit groups that a crib test could be
checked against. One link worth recording: both Gravel letters and Guibert's neighbouring letter deal with postal
money ("ports des lettres") and debts owed to the writer. That may be why the two letters were filed together. It is
not evidence about the cipher.

Next (one line each, not done here): (1) Gravel's other cipher letters, not this series: R2733 (Mél. Colbert 168bis
f.553, 1674, Bourdeau's item c) and the Affaires étrangères Correspondance politique Allemagne volumes for Jan 1665,
where a Diet envoy's dispatches to Lionne would use the same office cipher; ~$3, needs an AE/Gallica volume locator first;
(2) La Roncière t. I p. 270 (via Bourdeau) now agrees with the leaf, so that step is closed.

Requests this job: gallica.bnf.fr 20 (canvases 354, 357 at 1400 px + 2 native crops of 357 = 4; SRU 5; btv1b100355703
manifest 1 + canvases 389-394, 499-502 at 1000 px = 10, of which 500 not used), >= 2 s apart, all HTTP 200;
archivesetmanuscrits.bnf.fr 3 (cc954302, cc954291, cc954319); de-crypt.org 8 (RecordsView, no login, >= 1.8 s apart);
googleapis.com 3; be-api.us.archive.org 1; github.com 1 (shallow clone of aaymeloglu/unsolved-ciphers, catalogue grepped,
nothing copied).

## Gravel's other cipher letters: locator (R9-DEC2678B, 6 Oct 2026)

Brief: `.claude/briefs/runs/2026-10-06-account1-run9-jobs.md` "R9-DEC2678B" (the "Next (1)" step above). Locator job only:
shelfmark, ark, canvas, and a thumbnail-level look at whether the same two-digit groups occur. Nothing transcribed or decoded;
no cipher token of R2678 read (0 H, 0 C, 0 S, 0 M, 0 I).

| Item | Where | Locator result | Thumbnail-level look |
|---|---|---|---|
| R2733, Gravel to Maulevrier, 16 Aug 1674 (copy) | Mél. Colbert 168bis (ff.292-596), Gallica **btv1b100349564**, manifest labels all "NP" | anchors read from folio stamps at 1000 px: canvas 393 right = f.554 (stamp crop), 404 = f.561, 422 = f.574, 432 = f.581, 453 = f.595. Letter on **canvases 392-393** (f.553r-554r); the passage Tomokiyo quotes ("je l'ay pris au mot et luy ay propose de 433 168 75 232 284 415 ...") is on canvas 393 right, upper half. Saved `images/mc168bis_c393_f553v-554r.jpg` | **Plain three-digit figure groups** (75-484), no over/underlines seen: a different design from R2678's two-digit groups with diacritics. Not a same-key sibling at this level (agrees with QUEUE-github-held.tsv row "colbert": figure groups 52-489 shared with Charost, Mél. Colbert 172) |
| Gravel to Colbert, 23 Apr 1672 (Tomokiyo, louisxiv0.htm "Colbert-Gravel Cipher (1672) (DE=23_)", key reconstructed on his page; `sources/cryptiana/keys/IMAGE-QUEUE.tsv` row 1113, image `louisxiv_0gravel1672.png` not on disk) | Mél. Colbert 159, Gallica **btv1b10035602g** (labels all "NP") | **canvas 107 right = f.102r** (stamp "102"), **canvas 108 left = f.102v**, dated "[...]bourg le 23e avril 1672", signed "l'abbé de Gravel". Saved `images/mc159_c107_f102r.jpg`, `images/mc159_c108_f102v.jpg` | **Two-digit groups (about 0-110) with overlines and underlines**, a contemporary **interlinear decipherment** over nearly every cipher line, and Tomokiyo's prime-accented nomenclature: the same design class as R2678 (two-digit groups with diacritics; R2678 passA shows 29 80 62 41 73 51 with overlined digits). Values 51, 62, 73, 80 occur in both at a glance. Same key not established -- seven years apart, and R2678 is signed "[R.] de Gravel" while f.102v is signed "l'abbé de Gravel" (two brothers, Robert at Ratisbon and the abbé Jacques at Mainz, is an inference, grade I, not checked here) |
| Gravel's Diet dispatches, Jan 1665 | Archives diplomatiques (La Courneuve), **Correspondance politique, Allemagne 194** ("1665. Correspondance entre la Cour et GRAVEL, à Ratisbonne. 194: 1er janvier - 30 mai; 266 folios"; 195: 4 June - 30 Oct), with **196-197** (1665 supplement: pièces jointes; correspondance entre Gravel et Lionne (fragm.), Colbert, Louvois), **193** (1664-65 Diet pieces) and **211** (Court to Gravel, 10 Jan 1665 - 31 Dec 1666, 423 ff.) | from *Inventaire sommaire des archives du Département des affaires étrangères. Correspondance politique* t. I (1903), Google Books full view (ids 7cW-64n2o8IC, 1XgvAAAAMAAJ, gnJBAAAAYAAJ; snippet text, page not cited -- the Books API gives no page) | **Not online** as far as found: Gallica SRU `"Gravel" and "Ratisbonne"` top 10 are all Mél. Colbert volumes and Auerbach, no AE CP volume. Images would come from the AD reading room or a reproduction request (owner-side step, not filed here) |

Finding: the nearest same-design text with a period decipherment is **Mél. Colbert 159 f.102 (1672)**, not R2733 (different,
three-digit design) and not the AE volumes (not online). The 1672 interlinear gloss is grade-H material for a key in the same
two-digit-with-diacritics family; whether it is R2678's key is the open question.

Next (one line each, not done here): (1) cheapest: read f.102r-v's interlinear decipherment into a (group, gloss) key with
`tools/interlinear_align.py` and test it on R2678 with a matched control (a shuffled-key decode of R2678 and a held-out line of
f.102), PREREG first; ~$3-4, a solver job with line crops via `tools/iiif_lines.py`; Tomokiyo's own reconstructed table
(louisxiv_0gravel1672.png) can be fetched as a cross-check, cited not copied; (2) Tomokiyo lists other letters in the same
"Colbert-Gravel" family only by this one folio -- a sweep of Mél. Colbert 158-160 sommaires for further Gravel letters (1672)
would enlarge the key pool; (3) AE CP Allemagne 194 Jan 1665: owner-side reproduction request, only if (1) fails.

Requests this job: gallica.bnf.fr 18 (manifests 2; canvas images 107, 108, 270, 340, 393, 404, 420, 422, 424, 432, 440, 448,
453 and stamp crops of 393, 424 = 15; SRU 1), mostly >= 2 s apart, all HTTP 200; googleapis.com 6 (key, country=US);
archive.org 1 (advancedsearch). No other host.

## The 1672 Gravel key tested on R2678 (R9-DEC2678C, 6 Oct 2026)

Brief: `.claude/briefs/runs/2026-10-06-account1-run9-jobs.md` "R9-DEC2678C" (R9-DEC2678B's cheapest next). Worker started 06:42 UTC.

**Key (step 1).** Tomokiyo's own reconstruction of the Colbert-Gravel cipher of 1672 (cryptiana.web.fc2.com/code/louisxiv0.htm,
"Colbert-Gravel Cipher (1672) (DE=23_)", built by him from the period interlinear decipherment of Mél. Colbert 159 f.102; credit
Tomokiyo, rule 8) was on his page as an image. It was fetched once and snapshotted unmodified at
`sources/cryptiana/keys/img/louisxiv_0gravel1672.png`. It was then transcribed cell by cell into `key_gravel1672.tsv` (code + mark:
`^` overline, `_` underline, `'` prime): 23 alphabet cells, 78 syllable cells (Tomokiyo's bracketed, inferred ones graded M) and 18
nomenclature cells. Because the published table already existed, f.102's interlinear pairs were not re-read and
`tools/interlinear_align.py` was not run. The brief's "held-out f.102 line" control was not possible either: that control needs a
key rebuilt without the held-out line, and Tomokiyo's table was built from the whole leaf. It was replaced by a matched synthetic
power control (same key, design, N and language; below). Key source class: published.

**Ciphertext re-read.** A native crop of canvas 356 (`images/src_ark_12148_btv1b10035540v_f356_4800_4950_3500_800.jpg`, cut with
`tools/iiif_lines.py`, and line crops `images/r9c_f349r_cipher_*`) settles the diacritics. They are written into `ciphertext.tsv`;
passA.tsv is left unchanged:
- P1: `29`
- P2: `80 62 41 73_ 22: 51`. The underline sits under "73". The next group is "22" with two points. passA's "73 3^(2)" reads one 3
  too many.
- P3: `48^ 93 71 37 60^ 92 58^ 0`. There are three overlines, over 48, 60 and 58. The stroke above the final 0 is the descender of
  "auquel" from the line above. That leaves 11 digits in P3, so one group (`0`) stands alone.

**PREREG (step 2).** `PREREG-gravel1672-2026-10-06.md` was pushed in ca9a62902 before the test script was written or run. It
discloses that the key and the groups had been on screen together before it was written.

**Result (step 3).** `gravel1672_test.py` writes `gravel1672_test.out` (`--check` exits 0):

| | value |
|---|---|
| decoded letters P2+P3 (exact (code, mark) cells only) | `so n f re [22:] e` / `le s c ha no i ne [0]` |
| T, mean trigram log10 per letter, fr17 | -0.9367 |
| control 1, value-shuffled key (2000) | p1 = 0.0000 |
| control 2, token order shuffled within each passage (2000) | p2 = 0.0035 |
| control 3, power at N = 14 (200 fr17 spans enciphered with the same key, 500 shuffles each) | 0.985 |
| marked tokens whose exact same-mark cell exists in the 1672 key | 4/5 (73_ re, 48^ le, 60^ no, 58^ ne) |
| gate (p1 < 0.05 and p2 < 0.05) | **PASS** |

Reading (`decode.json` -> `tools/decode_key.py`, `--check` exit 0; `reading_gravel1672.txt`, `reading_gravel1672_tokens.tsv`):
P1 `fi`; P2 `so n f re [22:] e`; P3 `le s c ha no i ne [0]`.
Grades, 15 tokens: **H 11, C 0, S 0, M 2, I 0, U 2.**
- M: `80` = so, because Tomokiyo's cell is bracketed. `29` = fi, because a single group naming a payee ("pour 29 auquel on doit
  donner 15000") is a nomenclature code. The 1672 syllable cell is kept only as the key's value (`exceptions_gravel1672.tsv`).
- U: `22:` and `0`, which have no cell in the 1672 key.
- No spec exists for this folder, so `tools/judge_plaintext.py` was not run. With about 20 letters, the fr17 judge would not have
  power anyway. The pre-registered trigram statistic with its controls stands in for it.

Context, not graded as a reading: with the clear words around them, the two passages fit "pour **les chanoine[s]** qui doivent
aussy recevoir 1000 Reichsdalles pour la demye année de leur pension" and "pour **son fr[èr]e** qui en doit avoir 500". The plural
"qui doivent" agrees with "les chanoines". "Son frère" needs `22:` = r. In the 1672 key r is `19_`, so that value is grade I
(context only) and is not entered in the key. Who "son frère" and the chanoines are was not searched in this job.

What this does and does not show: the 1672 cells read 12 of R2678's 14 P2/P3 groups as French syllables, the marks agree, and both
controls fail where the target passes. So the 1665 letter uses the same cipher design and largely the same cells, or a close
relative of that cipher. It does not show the two keys are identical: `22:`, `0` and the nomenclature code `29` fall outside the
1672 table. Found: the key and the reading above. Not found: any print of this letter's plaintext. No print search was run; that
is a verifier's job.

Requests this job: cryptiana.web.fc2.com 1 (key image, HTTP 200); gallica.bnf.fr 2 (info.json of f356 and one native region
crop, >= 2 s apart, HTTP 200). No subagent calls.

## Sommaire sweep of Mél. Colbert 126-130 for Ratisbon cipher letters (R10-DEC2678S, 6 Oct 2026)

Brief: `.claude/briefs/runs/2026-10-06-account1-run10-jobs.md` "R10-DEC2678S" (the key-rebuild step below). Locator job, no
decoding; no cipher token of R2678 read (0 H, 0 C, 0 S, 0 M, 0 I). Every volume's BnF sommaire (archivesetmanuscrits) was fetched
whole and grepped for Ratisbon/Gravel/chiffre and for every German or Rhine place and office (Allemagne, Francfort, Mayence,
Vienne, Cologne, électeur, Empire, Munich, Bavière, palatin, Brandebourg, Saxe, Hambourg, Strasbourg, Metz). Snapshots in
`sources/bnf-aem/` (MANIFEST rows of this date). The sommaires never say whether a letter is enciphered, so every Ratisbon hit,
and the one entry naming a person from R2678's clear text, was then looked at on Gallica at 1000 px.

| Volume (sommaire ark; Gallica) | Entries | Ratisbon / Gravel hits | Look at the leaf |
|---|---|---|---|
| 126, Dec 1664 (cc954291) | 177 | none (German posts: Grémonville at Vienna f.151, 434; Du Fresne at Mainz f.368-371) | -- |
| 127-127bis, Jan-Feb 1665 (cc954302) | 330 | f.349 (R2678 itself); 127bis f.968, 1078 R. de Gravel | already seen in clear (R9-DEC2678) |
| 128-128bis, Mar-Apr 1665 (cc954319) | 343 | none (Graveline only) | -- |
| 129-129bis, May 1665 (cc95432j; 129 = btv1b100355436) | 290 | none; but **f.329 "Frischmann, résident pour le service du Roi à Strasbourg"**, the "Mr Frichmann" named in clear in R2678's cipher passage | canvas 336 right = f.329r ("De Strasbourg ce 1er May 1665"), canvas 337 = f.329v-330r, signed "Frischmann, Résident pour le service du Roy à Strasbourg". **In clear**, no figure groups. Saved `images/mc129_c337_f329v_frischmann_1may1665.jpg` |
| 130, June 1665 (cc954341; btv1b100355453) | 316 (130+130bis) | **f.149 R. de Gravel, à Ratisbonne** | canvas 154 right = f.149r, canvas 155 = f.149v-150r, canvas 156 left = docket "M. de Gravel ... juin 1665". Dated "Ratisbonne le 11 Juin 1665", signed Gravel. **In clear**: two bills of exchange (2,000 and 4,000 "Reisdalles"), his appointments through a banker in the rue Quincampoix, the "Estat de la Recepte et de la dépense de l'argent de la Caisse de l'Alliance", and tin-plate workers ("Martelleurs et Blanchisseurs de fer blanc") from Bohemia. No figure groups. Saved `images/mc130_c155_f149v-150r_gravel_11jun1665.jpg` |
| 130bis, July 1665 (btv1b100309307, ff.515-1097) | (above) | **f.578 R. de Gravel, à Ratisbonne** | canvas 69 right = f.578r (canvas 72 right = f.581): "Ratisbonne le 2e Juillet 1665", signed Gravel, on finding two "Marteleurs" and two "blanchisseurs". **In clear**, one page; f.578v blank (canvas 70). Saved `images/mc130bis_c69_f578r_gravel_2jul1665.jpg` |

Finding: Mél. Colbert 126-130bis hold **no cipher letter from Ratisbon**. Gravel wrote to Colbert at least five times between
January and July 1665 (127 f.349, 127bis f.968 and f.1078, 130 f.149, 130bis f.578); only R2678 carries cipher, and only in the
pension passage. The sweep gives no second text for the 1665 cells `22:` and `0`. Two context links worth carrying forward, not
evidence about the cipher: the June letter's "Caisse de l'Alliance" accounts (that R2678's pension sums come from the same
Alliance fund is an inference, grade I), and Frischmann at Strasbourg writing to Colbert in clear on 1 May 1665.

Next (not done here): (1) the same sweep one step wider, Mél. Colbert 120-125 (1664) and 131-133 (Aug-Dec 1665): sommaire arks
cc95423k (120-120bis), cc95427j (124) and cc954358 (131-131bis) are already recorded in
`sources/solver-diffs/2026-09-24-lane-g2-servien.tsv`; ~$3; (2) AE CP Allemagne 194 (Jan-May 1665), owner-side reproduction
request, unchanged.

Requests this job: archivesetmanuscrits.bnf.fr 19 (home 1; free-text search POSTs 5, all answered "Requête incorrecte"; ark
records 8, of which the first three (including the known-good control cc577658) answered a "page n'existe pas" stub and, after one 20 s pause, every later one worked;
ajaxGetCompDisplay 4; one tools/browser_fetch.js render, also the stub), >= 2 s apart; gallica.bnf.fr 12 (manifests 3 via
tools/gallica_folio.py, canvas images at 1000 px 9), >= 2 s apart, all HTTP 200. No subagent calls.

## Remaining gaps (R9-DEC2678C, 6 Oct 2026; updated R10-DEC2678S)
Read so far: 11 of 15 cipher tokens H, 2 M, 2 U (reading_gravel1672_tokens.tsv)
- `29`, a single-group payee name (15,000 Rd) - blocker: open-codes; a 1665 nomenclature code outside the 1672 table, which no context on f.349 narrows; next: the 1665 nomenclature from AE CP Allemagne 194, an owner-side reproduction request
- `22:` and `0`, 2 groups with no 1672 cell - blocker: not-attempted; context suggests r and a plural s (grade I); Mél. Colbert 126-130bis swept 6 Oct 2026 (R10-DEC2678S), Gravel's four other 1665 letters there all in clear; next: the same sommaire sweep of Mél. Colbert 120-125 and 131-133, ~$3
- novelty above N3 (verifier R10-DEC2678V gave N3, 6 Oct 2026, AUDIT.md) - blocker: waiting-on JSTOR-QUEUE.tsv rows 301-303 and the SO-R2678 second-opinion answer; Haug 2015, the study closest to this pension list, is not readable from the cloud

## Escalation (R9-DEC2678C, 6 Oct 2026)
- [x] siblings: Mél. Colbert 127-127bis and 126/128 sommaires swept (R9-DEC2678); Gravel's two other 1665 letters are in clear
- [x] clear-pages: f.349r-v clear text read (R8-G2678, R9-DEC2678); it gives the context for P1-P3
- [x] known-keys: Tomokiyo's 1672 Colbert-Gravel key passes the pre-registered gate (this section)
- [x] print: verifier R10-DEC2678V ran print_check and a logged search, 6 Oct 2026 (AUDIT.md AUDIT 1: N3, key published, D2 about 73%); Haug 2015 not readable from the cloud, JSTOR rows queued
- [ ] key-rebuild: the 1665 cells `22:` and `0` need a second text in the same key; Mél. Colbert 126-130bis swept (R10-DEC2678S, 6 Oct 2026), no Ratisbon cipher letter; next: sweep Mél. Colbert 120-125 and 131-133
- [x] image-check: native crop re-read of all three passages (this section)
- [n/a] retry: first attempt passed its gate, nothing to retry
Verdict: keep going: 2 internal gaps; cheapest next: sommaire sweep of Mél. Colbert 120-125 and 131-133 for Ratisbon cipher letters in the same design, ~$3 (126-130bis swept 6 Oct 2026, none; verifier step done 6 Oct 2026, AUDIT.md)
