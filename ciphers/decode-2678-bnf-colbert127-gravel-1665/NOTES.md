# [The abbé de Gravel] to Jean-Baptiste Colbert, Ratisbon, 29 Jan 1665, BnF Mélanges de Colbert 127, f.349-350

**Status: open** (not attacked; already someone else's active work-in-progress — see below).
Sender correction (R8-G2678, 6 Oct 2026): the letter is **signed "Guibert", maître des courriers d'Allemagne** (canvas 355, signature crop `images/c355_signature.jpg`), docketed "M. Guibert"; not the abbé de Gravel as DECODE, Bourdeau and this folder's title say. See the section of that date.
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
