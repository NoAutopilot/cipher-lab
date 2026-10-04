partial

Charrière, Négociations de la France dans le Levant, tome III (Paris, Imprimerie impériale; archive.org `ngociationsdel03charuoft`, 3.5 MB full text) was read as whole-volume grep by this worker on 3 Oct 2026 for "Noailles", "Acqs", "chiffre", "déchiffr", "Constantinople" and dates (227 "Acqs" lines; the volume prints Noailles' Constantinople despatches only as quoted excerpts, sourced to Ms. Mortemart/Colbert/Suppl. fr. 503 etc., with no "déchiffr" note for 1571-76), and tomes II and IV were grepped likewise.

# BnF fr.16142 ff.109-275 — François, then Gilles de Noailles, Constantinople to Charles IX / Catherine de Médicis / Anjou / Henry III, 1571-76

QUEUE row: LANE-POOLS scout, 3 Oct 2026, row 4 "P2-C-noailles-constantinople-1571-76" (`sources/pools-scout/2026-10-03/P2.tsv`).
Do not merge with `ciphers/fr3151-noailles-1558` (Antoine/François at Venice, a different cipher).
Worker: LANE-POOLS CS-4 (account 1), 3 Oct 2026. No transcription, decoding or key application done.

## Verdict (found, not classified for novelty)

**A clear copy of the same correspondence exists and is online: BnF Dupuy 521** (Gallica btv1b100339270, 259 canvases, 256 feuillets,
title "Extraits de la correspondance de François DE NOAILLES, évêque de Dax, ambassadeur à CONSTANTINOPLE, avec la cour de France.
(Mai 1571-sept. 1574.)", AEM notice ark:/12148/cc88656k, date field "1601-1700"). Canvases 8 and 120 viewed: a 17th-c. fair hand in plain
French, running text of despatches (canvas 8: the King's letter to the Signory of Venice, presented by du Ferrier; canvas 120: Noailles
to the King on Polish election, Bassa, Venice). It is extracts, not a leaf-by-leaf decipherment, and it is not yet matched to fr.16142
folios. If its extracts cover the ciphered passages it is a grade-C key source (known plaintext) and the target is a known-plaintext
alignment job, not cryptanalysis. Until a per-letter match exists the status stays `partial`, never `open`-as-untouched.

Other found items:
- Tomokiyo (`sources/cryptiana/web/henryiii.htm`), verbatim: "His many letters from December 1571 to July 1574 to the King, Queen Mother, and Duke of Anjou used the following cipher (BnF fr.16142, f.109-f.253). The same cipher was also used in 1574-1576 by Gilles de Noailles ... (BnF fr.16142, f.254-275; BnF fr.4735, f.276)." He has reconstructed the key (key printed on his page; "another article").
- Tomokiyo, `frencheastern.htm` (15 Mar 2026): a Moldavia/Pasha cipher letter set (to 2 June 1574) uses the same cipher; "The deciphered copies of these letters appear to be extant and are printed on p.522-523n and p.523-524n in Négociations de la France dans le Levant, vol.3." So Charrière III prints deciphered copies of at least those letters in footnotes (pages not independently checked by this worker beyond the Moldavia section around OCR lines 38210-38880).
- Same page for Grandchamp (1569, fr.16142 ff.3-27, a different earlier ambassador and key): "Some are deciphered in the margin, on separate pages, or between the lines. Others are not deciphered, of which at least some are deciphered by M. de Fréville in Négociations ... p.80." Charrière III's own footnote (OCR line 8692-8695) confirms Fréville deciphered Grandchamp's 1569 letters. Not Noailles' cipher.

## Per-letter table

Not built: fr.16142's per-letter list (folio, date, cipher/clear) is not in any catalogue text this worker could reach (AEM notice for fr.16142 not fetched; Gallica texteBrut needs a local browser), and Charrière's OCR is too noisy for a date-keyed match by script. Pool size is the scout's low-confidence 15,000 signs over ~166 folios (ff.109-275); letters open: unknown (est. all cipher folios, since no marginal decipherment was seen on the leaves viewed below); open est. signs: ~15,000 minus whatever Dupuy 521 and Charrière cover.

## Web and blog check (CS-4, 3 Oct 2026)
Queries (WebSearch): (1) `"fr. 16142" Noailles Constantinople chiffre déchiffré dépêches évêque d'Acqs` -> BnF AEM hits, Wikipedia (François/Gilles de Noailles), Levantine Heritage PDF of French consular archive (Nantes 166PO); (2) `Noailles bishop of Dax Constantinople cipher BnF fr.16142 deciphered` -> **Gallica Dupuy 521 title page**, BnF Français 7161 notice, dbourdeau.github.io/cyphersolver index, a pangoleen/desportes-1593 repo, no 16142 reading; (3) `Tomokiyo Cryptiana Noailles Acqs Constantinople Duke of Anjou cipher reconstructed fr.16142` -> Cipherbrain 14 Jun 2020 post (king's letter, unrelated), carter.church Marmont, no Noailles; (4) `ciphermysteries OR cryptiana.blogspot OR scienceblogs.de/klausis-krypto-kolumne Noailles Constantinople 1572 cipher` -> cryptiana.blogspot 2018 archive, ciphermysteries page 21, nothing on Noailles/Constantinople. Hit pages' comment threads opened: none carried a Noailles item (the search snippets showed none); the three blogs were searched through the engine, not by their own site search boxes (not done).
Solver repositories (shallow clones, 3 Oct 2026): dbourdeau/cyphersolver grep for 16142/Noailles/Constantinople: only the fr.3151 Venice 1558 Noailles items and unrelated Constantinople targets (Brèves 1603, Haga 1620, Hentér 1707); no fr.16142. `research/gallica_sweep/bnf_candidates.txt` lists no fr.16142. aaymeloglu/unsolved-ciphers: no fr.16142 or Noailles-Constantinople entry in `catalogue/decode-catalog.csv` (10,106 rows, harvest 18 Sept 2026) or `decode-records.jsonl`. DECODE live query: the RecordsList plain `psearch` GET ignored the term (same 154,876-byte page both times), so DECODE is checked only through Aymeloglu's harvest, not live. Model-solve announcements ("solves"+"Claude"/"GPT"): not searched.

## Premise check (CS-4, 3 Oct 2026)
(a) folder's own mentions: not found — the folder did not exist; the scout's row says "marginal and interlinear decipherments on some letters (Tomokiyo, seen on canvas 160)". My view of canvas 160 (a blank leaf numbered 77) and 161 (an address/docket leaf, 1571 docket "... a l'evesque de Dax") shows the scout's canvas number does not match; that claim is unconfirmed for the Noailles range. Tomokiyo's marginal-decipherment remark is about the Grandchamp 1569 leaves.
(b) other solvers' working files: not found for this item (greps above). Tomokiyo's reconstructed key itself is a solver working file for exactly this cipher: found, applied to nothing we have seen.
(c) physical neighbours: partial. fr.16142 canvases 160, 161, 200 viewed at 1000 px (not native resolution): blank leaf, docket leaf, Italian memorandum (f.96). No cipher leaf of ff.109-253 was located, so no facing-page decipherment was checked. Not done: native-resolution view of any cipher leaf and its neighbours. 3 canvases of 567.
(d) recipient/period side: **found** — BnF Dupuy 521 (clear extracts of the same correspondence, May 1571-Sept 1574); Charrière III excerpts and some footnote-deciphered copies (Moldavia letters, p.522-524n per Tomokiyo). Not read: Lettres de Catherine de Médicis (recipient side), Lettres de Henri III, Hammer/Zinkeisen, Gilles de Noailles' 1574-76 printed letters; Tomokiyo's "another article" on the key was not opened.

## Remaining gaps (CS-4, 3 Oct 2026)
Read so far: 3 of 567 fr.16142 canvases viewed (none a cipher leaf), 2 of 259 Dupuy 521 canvases viewed, 0 of 166 cipher folios matched to a clear copy; Charrière III grepped whole, pages not read.
- Per-letter list of fr.16142 ff.109-275 (date, addressee, cipher/clear) - blocker: not-attempted; AEM notice and canvas contact sheets untried; next: sample every third canvas of ff.109-275 as contact sheets, ~$2
- Dupuy 521 extracts aligned to fr.16142 folios by date - blocker: not-attempted; decides known-plaintext vs cryptanalysis; next: index Dupuy 521 despatch dates and match to the fr.16142 list, ~$3
- Charrière III pp.522-524n and other Noailles footnotes with printed decipherments - blocker: not-attempted; OCR too noisy to match by script; next: read the footnote pages from the volume text, ~$1
- Lettres de Catherine de Médicis recipient-side grep for 1571-76 - blocker: not-attempted; recipient side untouched so far; next: whole-volume grep of the IA text for the dates found above, ~$1

## Escalation (3 Oct 2026)
- [ ] siblings: fr.16144 Savary de Lancosme (same office, CS-2) and fr.16142 ff.3-62 Grandchamp leaves with marginal decipherments; planned step: read their glosses for the same sign shapes
- [ ] clear-pages: Dupuy 521 clear extracts and Charrière III footnote decipherments; planned step: match by date to fr.16142 folios
- [x] known-keys: Tomokiyo's reconstructed Noailles key found on henryiii.htm and the "another article"; not yet applied to anything, not opened further
- [x] print: Charrière III whole-volume grep done 3 Oct 2026; Catherine de Médicis letters not yet grepped
- [n/a] key-rebuild: Tomokiyo key exists, rebuild only after clear-page alignment
- [ ] image-check: a native-resolution look at cipher leaves ff.109-253 and their neighbours; planned step: contact sheets then native crops
- [n/a] retry: nothing has been attempted yet to retry
Verdict: keep going: 4 internal gaps; cheapest next: Charrière III footnote pages, ~$1

## While waiting
Nothing is waiting on anyone: the next step (index Dupuy 521 dates against fr.16142 folios) needs only Gallica, which answers from the cloud.

Requests per host: archive.org 5 (3 djvu + 2 advancedsearch-style), gallica.bnf.fr 8 (2 manifests, 5 images, 1 failed none), archivesetmanuscrits.bnf.fr 1, de-crypt.org 2, github.com 2 clones, dbourdeau.github.io 1, WebSearch 4.

## First cheap test: leaf survey and test 0 (LANE-POOLS FT-D, account 1, 3 Oct 2026 22:25-22:58 UTC)

Brief: `.claude/briefs/runs/2026-10-03-acct1-pools-first-tests.md` target D. Intake gate (`tools/intake_gate_check.py`, run at 22:25):
`fr16142-noailles-constantinople-1571: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`, exit 0.
Tool shelf (`tools/tool_shelf.py "survey a Gallica manuscript's canvases as low-res contact sheets to count cipher pages"`):
gallica_folio.py (used: the manifest has no folio labels, 567 canvases all 'NP', so canvases were surveyed directly);
cipher_page_detector.py is [weak] (recall 0.69 on its own gate) and was not used; the survey is one look per canvas by this worker.

**Step 0, leaf survey** (`survey.tsv`, `letters_coverage.tsv`). Canvases 215-567 (ff.104-278), IIIF `full/400,/0/default.jpg`, 351 fetched,
2 returned 404 (c438, c452), every one looked at on 5x4 contact sheets. Classes: 67 full cipher pages, 48 part cipher, 21
separate-sheet decipherments, 71 clear, 144 blank/address/docket. The cipher is a drawn-symbol homophonic substitution with a
nomenclator (Tomokiyo's table). Where the plaintext already sits:
- 1572 letters to the King: a running **margin decipherment** in a small contemporary hand beside the cipher (c225, c257-266,
  c297-303, c318-324, c346-351, Nov 1572 letters). Confirmed at native resolution on c262 only; elsewhere a 400 px judgement.
- From May 1572 on: **"Dechiffré de la precedente"** sheets after many letters (c291, c366, c387, c393, c458, c480, c492, c544, c550).
- **"Duplicata de la precedente"**: enciphered second copies of glossed originals (c306-311, c334-340, c354-355, c362-364, c375,
  c460-461, c484-486): unglossed, but their plaintext is the original's gloss (a same-plaintext pair, useful for key checks).
- **No decipherment on the leaves**: c510-516, Noailles to the King, July 1574 (about 6.5 full cipher pages, the bulk);
  c409-410 (Sept 1572); c464 and c472-473 (March 1573). Estimated open signs ~14,000 (rough: ~1,500 per full page, not counted),
  plus ~9,500 in letters whose gloss status was unclear at 400 px. The pool clears the 2,000-sign bar on c510-516 alone,
  conditional on Dupuy 521 (clear extracts to Sept 1574) and Charrière III not covering that letter. Charrière III quotes clear
  excerpts of Acqs's letters of **7 July and 16 July 1574** (OCR lines ~41015 and ~41586, from Mortemart/Brienne copies) and of
  4, 8 and 22 June 1574 on pp.520-524 (the footnote pages CS-4 named; read here: clear excerpts sourced "Ms. Mortemart, Brienne",
  not cipher decipherments of fr.16142 leaves). Not matched to c510-516 (its day is unread at 400 px).

**Key**: Tomokiyo's published reconstruction (cryptiana henryiii.htm, table image CharlesIX_Acqs2.png, fetched 3 Oct 2026, kept
out of the repo); `key.tsv` records it verbally. Key source class: published.

**Test 0, known-answer on a glossed leaf** (`scripts/test0.py`, `witness/`). Leaf c262 (April 1572 letter to the King): crops by
`tools/iiif_lines.py --ark btv1b9060927q --canvas 262 --out .../images --prefix c262 --debug`, then `--image <src> --region ...`
for the cipher block (c262ci) and the margin gloss (c262gl). Two blind Sonnet passes named each sign by its row in Tomokiyo's
table (A and B, unreconciled); one Sonnet pass read the margin gloss (low confidence), reconciled by this worker before any decode
was seen (`gloss.tsv`; raw pass in `gloss_passA.tsv`). Statistic: letter similarity (difflib ratio) of decode vs gloss over the
block (11 cipher rows vs 13 gloss lines, not paired by line). Two nulls of 200 draws each: key letter-values shuffled among the
glyphs (can change the statistic), and gloss word order shuffled with the decode fixed (keeps letter frequencies, destroys
sequence). Gate written before pass B was seen (`witness/gate_passB.txt`, 22:53 UTC): beat both nulls' maxima.

| pass | real | key-shuffle mean / p95 / max (rank) | gloss-order mean / p95 / max (rank) | N |
|---|---|---|---|---|
| A (exploratory, '#'=e) | 0.3177 | 0.1314 / 0.2031 / 0.2161 (1/201) | 0.1642 / 0.2396 / 0.3021 (1/201) | 392 tokens, 315 gloss letters |
| A ('#'=o) | 0.3307 | 0.1362 / 0.1875 / 0.2083 (1/201) | 0.1649 / 0.2214 / 0.2526 (1/201) | same |
| **B (gate)** | **0.2799** | 0.1244 / 0.1696 / 0.2180 (1/201) | 0.2016 / 0.2665 / **0.2988 (6/201)** | 391 tokens |

**Result: the known-answer gate FAILS (pass B rank 6 of 201 on the gloss-order null): non-test at this transcription error**
(rule 3 calibration paragraph), not a negative on the key; no unglossed leaf was scored (brief item 4). Both passes beat every key
shuffle and sit above the gloss-order p95. Interpretation, not a graded reading: pass B's decode carries runs of the gloss, e.g.
"...endorm c de de ca o la partie faict fore..." beside the gloss's "s'endormir de ca. Car la partie est forte", "de le gens de
geerre" beside "de gens de guerre". Why it is weak: the c262ci crops are 93 px slices of lines sloping ~2.9 degrees (both passes
had to stitch and deskew; a cutting error of this worker's, `--centres` given without `--follow-slope`), and the passes split on
the two '#'-like glyphs (o vs e) and on the box-on-stem nomenclator sign (A: 'roy', B: 'le'); p comes out far above French rates.
Grades (rule 4): the gloss words are period decipherment (source H, reading M); no decoded token is graded above M; no reading
is claimed.

Judge (rule 7; `python3 tools/judge_plaintext.py specs/fr16142-noailles-constantinople-1571.json --file .../witness/c262_passB_decode.txt`):
```
FAIL language: score=-1.507, null_p99=-1.867, real_p05=-0.903, real_median=-0.785, mode=both, N=428
ok   words: cover=0.72, min=0.5, real_text_median_cover=0.946
FAIL - fr16142-noailles-constantinople-1571 (a PASS is a gate for a verifier, not a reading; rule 10)
```
Corpus fr16 is era-matched (Catherine de Médicis letters). The decode is a calibration read of a glossed leaf, not a candidate.

Requests: gallica.bnf.fr 354 (manifest 1, thumbnails 352 incl. one 429 at c217 retried once after 20 s and two 404s, native c262 1),
cryptiana.web.fc2.com 4 (2 redirects + 2 images), archive.org 1 (Charrière III djvu text). Subagents: 3 Sonnet calls (2 cipher, 1 gloss).

## Remaining gaps (FT-D, 3 Oct 2026)
Read so far: 351 of 353 canvases surveyed at 400 px; 1 leaf (c262) transcribed twice, 0 open leaves decoded; known-answer gate failed
- Transcription error on the c262 block too high for the known-answer gate - blocker: not-attempted; re-cut c262 with `tools/iiif_lines.py --follow-slope` one row per crop, settle the '#' pair and box-on-stem sign; next: two passes + reconciliation, re-run scripts/test0.py, ~$5
- July 1574 letter c510-516 (bulk of the open signs) undecoded - blocker: not-attempted; waits on a test-0 PASS; next: day read at native resolution, Charrière 7/16 July 1574 excerpts and Dupuy 521 matched by date, ~$2
- Gloss presence on 31 C/P pages judged only at 400 px - blocker: not-attempted; the open-sign count depends on it; next: native look at the 'unclear' rows of letters_coverage.tsv, ~$1
- Dupuy 521 extracts not aligned to fr.16142 letters - blocker: not-attempted; decides whether c510-516 is really open; next: index its despatch dates (CS-4 gap, still open), ~$3

## Escalation (FT-D, 3 Oct 2026)
- [x] siblings: the duplicata/original pairs in this volume found (letters_coverage.tsv): same plaintext enciphered twice
- [ ] clear-pages: Dupuy 521 and Charrière 7/16 July 1574 excerpts against c510-516; planned step: match by date
- [x] known-keys: Tomokiyo's published key applied to c262 (test 0); beats all 200 key shuffles, gate failed on transcription
- [x] print: Charrière III pp.520-524 read and the July 1574 excerpts located (3 Oct 2026)
- [n/a] key-rebuild: a published key exists and beats every shuffle
- [ ] image-check: native-resolution crops with --follow-slope of c262 and of c510-516; planned step: re-cut and re-pass
- [ ] retry: test 0 with the better crops (a different crop instrument, not the same knob); planned step: as gap 1
Verdict: keep going: 4 internal gaps; cheapest next: native look at unclear-gloss rows, ~$1

## c262 re-cut and the same known-answer gate once (LANE-JM NX-RECUT, account 1, 3 Oct 2026, from 23:44 UTC)

Brief: `.claude/briefs/runs/2026-10-03-acct1-jm-wave1.md` NX-RECUT. Only knob changed: the crops. Key, sign set, `scripts/test0.py`, `gloss.tsv` and `witness/gate_passB.txt` unchanged.
Crop step (run before any subagent call; source = the native canvas 262 already on disk from FT-D's fetch, so no new request; the block is the same one FT-D read, from the blotted row beside the gloss line "bruslent" to the row beside "Il semble quil leur feroit": 10 cipher rows):
```
python3 tools/iiif_lines.py --image ciphers/fr16142-noailles-constantinople-1571/images/src_ark_12148_btv1b9060927q_f262_full.jpg --region 1330,1980,3470,1420 --centres 209,335,444,609,748,859,993,1101,1223,1338 --follow-slope 300 --slope-margin 15 --max-width 1800 --overlap 100 --prefix c262rc --out ciphers/fr16142-noailles-constantinople-1571/images --debug
ciphers/fr16142-noailles-constantinople-1571/images/src_ark_12148_btv1b9060927q_f262_full.jpg (local): region 3470x1420, 10 lines, 10 bands x 2 segments; pitch 0 distance 0 prominence 0.0
  centres (region y): 209 335 444 609 748 859 993 1101 1223 1338
  band L01: slope fit y = 218.7 + -0.04529*x (12 window peaks kept); drift over the region -157 px (pitch 122)
  band L02: slope fit y = 362.5 + -0.05833*x (11 window peaks kept); drift over the region -202 px (pitch 122)
  band L03: slope fit y = 423.0 + -0.00667*x (6 window peaks kept); drift over the region -23 px (pitch 122)
  band L04: slope fit y = 630.2 + -0.04746*x (12 window peaks kept); drift over the region -165 px (pitch 122)
  band L05: slope fit y = 768.2 + -0.05563*x (12 window peaks kept); drift over the region -193 px (pitch 122)
  band L06: slope fit y = 889.3 + -0.05730*x (12 window peaks kept); drift over the region -199 px (pitch 122)
  band L07: slope fit y = 1008.8 + -0.05383*x (12 window peaks kept); drift over the region -187 px (pitch 122)
  band L08: slope fit y = 1128.3 + -0.04730*x (11 window peaks kept); drift over the region -164 px (pitch 122)
  band L09: slope fit y = 1239.5 + -0.04636*x (12 window peaks kept); drift over the region -161 px (pitch 122)
  band L10: slope fit y = 1363.9 + -0.04944*x (12 window peaks kept); drift over the region -172 px (pitch 122)
  wrote 20 crops and ciphers/fr16142-noailles-constantinople-1571/images/manifest.json
```
Centres were read from the row ink profile of the left 500 px of the block (where the lines start; FT-D's fixed-y `--centres` cut without `--follow-slope` was the fault). Lines rise ~160-200 px across the block (slope -0.045 to -0.058, ~2.6-3.3 deg), more than one pitch (122 px): every crop is now a sheared strip on its own line. Overlay and the 20 crops checked by eye: one text row per crop. L03 (the short line ending in a flourish) fitted flat on 6 peaks and its _s2 strip caught the end of L04; `c262rc_L03_s2.jpg` was cut to x<760 (after the flourish). Every _s2 crop carries corner ticks at x=130, the end of its overlap with _s1 (manifest note).

**Passes** (2 Sonnet subagent calls, blind to each other and to FT-D's passes, crop paths + Tomokiyo's table image only; prompt
kept in the worker's scratchpad; raw files `witness/c262rc_passC_raw.tsv`, `witness/c262rc_passD_raw.tsv`; the scored files only
collapse each `?{description}` to a bare `?`, the same for both). C 390 tokens, D 392. `tools/reconcile_passes.py`: agree 273/395
aligned columns = 69.1%, **err_2reader 30.9%** (122 disagreement columns). Most splits are one glyph named two ways throughout
(D: box-on-stem = W:que, 6-with-cross = o5, 2-with-stem-circle = m1/u1, loop-S = e3 vs C's m1, cup-on-stem s2 vs C's o3), so the
error is in naming signs against the table, not in the cutting. Reconciliation (`witness/c262rc_recon.tsv`, log
`witness/c262rc_recon_log.tsv`, by this worker before any decode of C or D was printed, gloss not consulted): glyph rulings from the
table image -- 2-with-stem-circle = n1, 6-with-cross-above = t2 (row 2 under t, so key.tsv's s3 "b-crossed" sits in the t column;
noted, key.tsv not changed), box hanging from the top bar with the stem running down = W:le (roy has a cross above its box), loop-S = e3,
cup-on-stem = s2, theta-with-tail = d1; 74 columns by rule, 36 one-reader signs kept, 12 one-off splits to pass C (M). 384 signs.

**Same gate, re-run once** (`scripts/test0.py` and `gloss.tsv` unchanged, `git diff` clean; gate pass pre-registered in
`witness/gate_recut.txt` before either output was seen = pass D, the counterpart of FT-D's pass B):

| text | '#' | real | key-shuffle max (rank /201) | gloss-order max (rank /201) | N tokens | gate |
|---|---|---|---|---|---|---|
| **D (gate pass)** | e | **0.1928** | 0.2342 (25) | 0.2590 (41) | 392 | **FAIL** |
| **D (gate pass)** | o | **0.1736** | 0.2507 (64) | 0.2231 (22) | 392 | **FAIL** |
| reconciled | e | 0.4548 | 0.2658 (1) | 0.2904 (1) | 384 | beats both |
| reconciled | o | 0.3973 | 0.2575 (1) | 0.3233 (1) | 384 | beats both |
| C (blind, not gated) | e | 0.4176 | 0.2473 (1) | 0.3379 (1) | 390 | beats both |
| C (blind, not gated) | o | 0.3846 | 0.2308 (1) | 0.2637 (1) | 390 | beats both |

(FT-D on the old crops: pass B 0.2799, rank 1 / rank 6.) **Verdict, as pre-registered: the known-answer gate FAILS on the gate pass
-- non-test at this transcription error; the target (c510-516) was not scored.** Reported beside it, not substituted for it: one
blind pass (C) and the reconciled text clear both nulls' maxima at both '#' resolutions, the highest scores this block has given
(reconciled 0.45 vs FT-D's best 0.33). Reading what differs: the two readers on the same new crops split 31% and land on opposite
sides of the gate, so the re-cut removed the cutting fault but the gate now measures which reader named the look-alike glyphs right;
the reconciled text's pass rests on this worker's glyph rulings (not blind, and a single reconciler), so it licenses nothing alone.
Interpretation of the reconciled decode, not a graded reading: L08 "...plaisir..." beside the gloss's "plaisir" two lines later; no
token is graded above M (rule 4).

**Rule 3 third-attempt clause.** This is the second attempt at the c262 known-answer gate, with only the crops changed; it failed on
the gate pass. A third attempt at the same c262 known answer is not another re-cut and not a third Sonnet pass on these crops: it
needs a different instrument (a settled glyph inventory -- `tools/glyph_atlas.py` exemplars per Tomokiyo row put to the person in
the sign sorter, TRANSCRIPTION.md steps 2-4, so readers name signs from settled labels rather than from the table image) or new
material (a second glossed leaf, e.g. c257-266 neighbours, scored with a gate pre-registered on its own blind pass).

Requests: cryptiana.web.fc2.com 2 (henryiii.htm + CharlesIX_Acqs2.png, image kept out of the repo); gallica.bnf.fr 0 (native c262
already on disk). Calls: 2 Sonnet passes + this worker's reconciliation (3 units).

## Remaining gaps (NX-RECUT, 3 Oct 2026)
Read so far: 351 of 353 canvases surveyed at 400 px; c262 block transcribed 4 times (2 on old crops, 2 on re-cut crops) + 1 reconciliation; known-answer gate failed twice on the pre-registered pass; 0 open leaves decoded
- Glyph naming against Tomokiyo's table unsettled (readers split 31% on the same crops) - blocker: not-attempted; the c262 known-answer gate cannot be retried without it (rule 3 third-attempt clause retired the table-image Sonnet pass for this gate, NX-RECUT); next: glyph_atlas exemplars per table row from c262 + a duplicata pair into the sign sorter for the person to settle, then blind passes against the settled labels, ~$6
- July 1574 letter c510-516 (bulk of the open signs) undecoded - blocker: not-attempted; waits on a known-answer PASS; next: day read at native resolution, Charrière 7/16 July 1574 excerpts and Dupuy 521 matched by date, ~$2
- Gloss presence on 31 C/P pages judged only at 400 px - blocker: not-attempted; the open-sign count depends on it; next: native look at the 'unclear' rows of letters_coverage.tsv, ~$1
- Dupuy 521 extracts not aligned to fr.16142 letters - blocker: not-attempted; decides whether c510-516 is really open; next: index its despatch dates (CS-4 gap, still open), ~$3

## Escalation (NX-RECUT, 3 Oct 2026)
- [x] siblings: the duplicata/original pairs in this volume found (letters_coverage.tsv): same plaintext enciphered twice
- [ ] clear-pages: Dupuy 521 and Charrière 7/16 July 1574 excerpts against c510-516; planned step: match by date
- [x] known-keys: Tomokiyo's published key applied to c262; reconciled text and one blind pass beat every null, gate pass failed
- [x] print: Charrière III pp.520-524 read and the July 1574 excerpts located (3 Oct 2026)
- [n/a] key-rebuild: a published key exists
- [x] image-check: c262 re-cut with --follow-slope, one row per crop, checked by eye (NX-RECUT)
- [ ] retry: known-answer with settled glyph labels (sign sorter) or on a second glossed leaf; planned step: glyph_atlas + sorter sheet
Verdict: keep going: 4 internal gaps; cheapest next: native look at unclear-gloss rows, ~$1; the known-answer retry needs the sorter first

`python3 tools/gaps_check.py fr16142-noailles-constantinople-1571` (NX-RECUT):
```
OK keep-going fr16142-noailles-constantinople-1571: keep going: 4 internal gap(s), 2 step(s) untried
gaps_check: 1 checked: 0 parked, 1 keep-going, 0 FAIL, 0 skipped
```

## Gloss presence at 1500 px + Dupuy 521 date index (LANE-RUN1 RUN1-NX, account 1, 4 Oct 2026, from 00:48 UTC)

Brief: `.claude/briefs/runs/2026-10-04-acct1-run1-wave1.md` RUN1-NX. No known-answer retry (rule 3 third-attempt clause), no transcription, no decode.
Intake gate (00:48 UTC): `fr16142-noailles-constantinople-1571: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`, exit 0.

**Step 1, gloss presence** (`letters_coverage.tsv`, new column `gloss_1500px_RUN1NX`; existing columns untouched). The 31 C/P canvases of
the letters whose cover was unclear, '?' or open were fetched once at IIIF `full/1500,` (31 requests) and read by this worker, two
pages per look; c275's faint "interlinear" lines got one native-resolution region (`pct:10,22,85,14`, 1800 px). No Sonnet call was
needed (brief allowed 2). Per letter:

| canvases | 400 px cover (FT-D) | 1500 px (this pass) |
|---|---|---|
| 231-232 | unclear | absent on c231; **c232 is not cipher**: a blank verso showing c231 through the paper |
| 245-246 | unclear | absent; clear text = the c464 letter (8 March 1573 to the King): an enciphered pair, both unglossed |
| 268 | unclear | **present** (running margin text beside both cipher blocks) |
| 275-276 | interlinear? | absent: the faint lines are verso show-through (native region) |
| 287-289 | sheet + interlinear? | partial: interlinear words over some signs on ~9 of ~67 lines (plus sheet c291-292) |
| 330 | unclear | absent |
| 358-361 | unclear (copy) | absent; heading "Coppie de la despesche du 8me d'aoust avec ung postscripta du xviii et ung autre du xx du mois 1572" |
| 409-410 | open | open: 3-4 interlinear words on ~3 lines, no running gloss |
| 464 | open | absent; pair with c245-246 |
| 472-473 | open | absent (margin note beside a clear line only) |
| 510-516 | open | absent on all 7; **heading c510 "7 Juillet 1574 Pera"** (the day FT-D could not read) |
| 520-521 | margin? | **present** on c520 (running margin column); c521's faint cipher-like lines look like c520 show-through (uncertain) |
| 560-561 | margin? | **present** on both |

Open-sign estimate (est_signs column, rough): letters with no gloss and no sheet now sum to ~23,600 signs (c231 ~1,500 + 245-246
1,000 + 275-276 2,200 + 330 700 + 358-361 4,500 + 409-410 2,200 + 464 800 + 472-473 1,000 + 510-516 9,750); glossed after all: 268,
520(-521), 560-561 (~3,300). FT-D's "~14,000 open + ~9,500 unclear" becomes ~23,600 open (c232 dropped), of which c245-246/c464 are
an enciphered same-text pair.

**c510-516 is not wholly open.** c516 carries a clear lead-in followed by cipher: "Sire quelques jours avant recevoir vre depesche du
xv(?)me d'Avril j'avois entendu ce qu'il plaist a vre Mag^te me mander" + cipher (image: canvas 516, `pct:5,8,90,25`). Charrière,
*Négociations dans le Levant* III (IA `ngociationsdel03charuoft`, djvu text lines ~41266-41285, between the page heads 553 and 556), prints from the evêque
d'Acqs's "dépêche du 7 juillet 1574" (sources "Corr. de Turquie, ms. Mortemart, Brienne, etc.", line 41473): "Quelques jours avant
recevoir vostre dépesche javois entendu ce qu'il plaist à V. M. me commander des conspirations faictes contre sa personne et son
estat, lesquelles les ministres de vos voisins avoient bien faict sonner en autre façon par deçà; mais j'en ay esclaircy ledit bassa
selon la vérité de vos commandemens ..." -- the clear words on the leaf match the printed sentence's opening (the leaf has "mander"
where the print has "commander"), so the cipher after "mander" is very probably the printed continuation from "des conspirations".
A second excerpt of the same despatch is printed at lines ~41016-41060 (pp.551-552) ("Quant à l'opposition que V. M. me commande faire aux
recherches qu'aucuns princes et estats d'Italie font ..."), and a 7 July 1574 letter to Catherine de Médicis at lines ~41512-41540 (pp.556-558).
Not tested here (no decode in this brief): the printed text is a crib candidate for c516 and for whatever part of c510-515 the
excerpts cover; the copy the print rests on may be a decipherment, abridged or re-worded.

**Step 2, Dupuy 521 date index** (`dupuy521_dates.tsv`, `dupuy521_align.tsv`). Gallica OCR does not exist for this manuscript (a
17th-c. fair copy; the AEM notice cc88656k lists no items), so the route was the IIIF images: 259 canvases (each an opening) fetched
once at `full/1000,` and read by two blind Sonnet subagent passes (canvases 1-128 and 129-259), each writing every piece start,
heading and date line; 475 rows. Spot-checked by this worker on canvases 36, 76, 221 and 226. Dupuy 521 runs 24 May 1571 (the
instructions) to 25 Sept 1574 in date order, with the King's, Queen's and Sultan's letters interleaved; Acqs writes from Venice
(Jul 1571-Jan 1572), Pera (Mar 1572-Sept 1574) and Branza by Ragusa (Nov 1572-Jan 1573).

Alignment to fr.16142 (`dupuy521_align.tsv`): of the 24 fr.16142 cipher letters dated within Dupuy's range, 21 have a Dupuy piece of
the same date and addressee; 2 are confirmed by text, the rest by date only:
- **c510-516 (7 July 1574, to the King) = Dupuy 521 canvases 221R-226R (ff.~111-112 by the leaf numbers on the images), text-confirmed
  at both ends.** Dupuy 221R: "Au Roy / Sire, Le dernier du passé j'ay receu la depesche qu'il a pleu a Vostre Majesté me faire du
  xvij avril, j'avois pensé quelques jours auparavant la reception d'icelle que ..." -- word for word the clear lead-in on c510
  before its cipher starts, continued in clear. Dupuy 226R: "Sire quelques jours avant recevoir vostre depesche du dix huictiesme
  d'avril j'avois entendu qu'il plaist a Vostre Majesté me mander des conspirations faictes contre sa personne ..." -- the c516 lead-in
  and Charrière's excerpt; ends "... de Pera lez Constantinople ce vj Juillet 1574" (fr.16142's heading has 7). About 5 openings
  (~10 pages) of clear text against ~6.5 cipher pages: likely the whole letter, possibly abridged (the volume calls itself
  "Extraits"); not compared line by line.
- **c275-276 (25 April 1572, to Anjou) = Dupuy 36R-37L, text-confirmed.** Dupuy 36R "Monseigneur, Encores que ma venue en ce pays
  nayt esté moins agreable aux Turcs pour me veoir arriver bien tost apres la perte de leur armée de mer, que ..." = c275's clear
  lead-in before the cipher.
- Date-only matches for the other open letters: c330 (8 July 1572, Queen) = 64R-65L; c358-361 (Aug 1572 copy + PS 18/20 Aug) =
  71L-73R; c409-410 (6 Sept 1572) = 76L-77L (opening consistent); c245-246 + c464 (8 March 1573, King) = 121R-122L; c472-473 (8 March
  1573 + PS 12 March, Queen) = 122L-123R.
- No Dupuy piece found: c231-232 ("Relation d'une bataille", 1571) and c225-226 (2 Dec 1571, glossed anyway); c520 onward is after
  Dupuy's range.

**What this changes.** The CS-4 question "is c510-516 really open?" is answered: it is not -- its plaintext (as Dupuy's copyist has
it) sits in Dupuy 521, and Charrière III prints parts of it. Of the ~23,600 signs left without a gloss or sheet on the leaves (step
1), all but c231 (~1,500) now have a date-matched clear copy in Dupuy 521, two of them text-confirmed. The target's open part shrinks
to the "Relation d'une bataille" and to whatever Dupuy abridged. For the key, c510-516 + Dupuy 221R-226R is a ~9,750-sign
known-plaintext pair on leaves no reader has seen before -- the "new material" rule 3's third-attempt clause asked for (NX-RECUT),
usable once the glyph inventory is settled. Not done here (no transcription, no decode in this brief).

Requests: gallica.bnf.fr 296 (31 fr.16142 pages at 1500 px, 2 native regions c275/c516, 1 Dupuy manifest, 2 trial + 259 Dupuy
openings at 1000 px, 1 extra trial fetch of c258 at 600 px), all HTTP 200, 1.6-2 s apart; archivesetmanuscrits.bnf.fr 1 (notice
cc88656k); archive.org 1 (Charrière III djvu text). Calls: 2 Sonnet subagents (Dupuy index), 0 for step 1.

## Remaining gaps (RUN1-NX, 4 Oct 2026)
Read so far: 351 of 353 canvases surveyed at 400 px, 31 open/unclear C/P pages re-read at 1500 px; Dupuy 521 indexed whole (259 openings); 21 of 24 in-range cipher letters matched to a Dupuy copy (2 by text); c262 transcribed 4 times, gate failed twice; 0 open leaves decoded
- Glyph naming against Tomokiyo's table unsettled (readers split 31% on the same crops) - blocker: not-attempted; every known-answer use (c262 gloss, c510-516 vs Dupuy) waits on it (rule 3 third-attempt clause, NX-RECUT); next: glyph_atlas exemplars per table row from c262 + c510 into the sign sorter for the person to settle, then blind passes against the settled labels, ~$6
- c510-516 known-plaintext pair with Dupuy 521 221R-226R not yet used - blocker: not-attempted; outside this brief (no transcription); next: two passes transcribing Dupuy 221R-226R clear text (10 pages, crops per page), then a pre-registered known-answer gate on c510's first cipher lines once the sorter labels exist, ~$4
- Date-only Dupuy matches (c330, c358-361, c409-410, c245/c464, c472-473) not text-checked - blocker: not-attempted; outside this brief's index scope; next: one native look per pair at the clear lead-in words on the fr.16142 leaf vs the Dupuy opening, ~$1
- "Relation d'une bataille" c231 has no clear copy found - blocker: not-attempted; not named in this brief; next: grep Charrière III and the Lepanto relations in print for its clear opening "Le gain de ceste grande bataille advenue en saison incommode", ~$1

## Escalation (RUN1-NX, 4 Oct 2026)
- [x] siblings: the duplicata/original pairs in this volume found (letters_coverage.tsv); c245-246/c464 found to be a further same-text pair (RUN1-NX)
- [x] clear-pages: Dupuy 521 indexed and aligned by date (dupuy521_align.tsv); c510-516 and c275-276 text-confirmed; Charrière III 7 July 1574 excerpts located
- [x] known-keys: Tomokiyo's published key applied to c262; reconciled text and one blind pass beat every null, gate pass failed
- [x] print: Charrière III pp.520-524 and pp.551-558 read for the June-July 1574 excerpts
- [n/a] key-rebuild: a published key exists
- [x] image-check: c262 re-cut with --follow-slope (NX-RECUT); 31 open/unclear pages re-read at 1500 px (RUN1-NX)
- [ ] retry: known-answer with settled glyph labels (sign sorter), on c262 or on c510 against Dupuy 221R; planned step: glyph_atlas + sorter sheet
Verdict: keep going: 4 internal gaps; cheapest next: text-check the date-only Dupuy matches, ~$1; the known-answer retry needs the sorter first

`python3 tools/gaps_check.py fr16142-noailles-constantinople-1571` (RUN1-NX):
```
OK keep-going fr16142-noailles-constantinople-1571: keep going: 4 internal gap(s), 1 step(s) untried
gaps_check: 1 checked: 0 parked, 1 keep-going, 0 FAIL, 0 skipped
```

## Dupuy 521 221R-226R clear text transcribed (LANE-RUN2 RUN2-NXDUP, account 1, 4 Oct 2026, from 02:47 UTC)

Brief: `.claude/briefs/runs/2026-10-04-acct1-run2-wave1.md` RUN2-NXDUP. Full report: `run2/nxdup/REPORT.md`. No decode, no alignment.
Intake gate (02:47 UTC): `partial (line 1) -- edition/page or full-text-search citation found within 6 lines`, exit 0.

The clear copy of the 7 July 1574 letter to the King (c510-516) is now on disk: Dupuy 521 221R.03 ("Sire.") to 226R.23 ("des Vignes
de Pera les Constantinople ce vj Juillet 1574"), 11 pages, 277 line crops (`iiif_lines --follow-slope`), two blind Sonnet passes
per page (22 calls) reconciled by this worker against the page images: `run2/nxdup/dupuy221_226_diplomatic.txt` and
`dupuy221_226_norm.txt` (2,088 words, 9,425 letters; rule-3 normalisation, u/v and i/j as written), regenerated and `--check`ed by
`run2/nxdup/build_texts.py`. err_2reader 0.218 raw / 0.129 loose (per page 0.096-0.197 loose); each pass vs the reconciled text
0.184 / 0.202 -- the passes share errors, so the two-reader figure understates reader error; err_true not measured (no benchmark
for this hand). 21 tokens left [?].
For the wave-2 alignment (RUN2-NXALN): the copy ends "... vous succedent mal &c." straight into the date -- a copyist's
truncation mark, so the cipher original may run past the copy's end (**possible omission at the tail**); a dittography at
223L.14-15 is marked `{DITTO}` and dropped from the normalised text; the c516 clear lead-in is 226R.03-.06, so c516's cipher
corresponds to 226R.07-.21 and c510-515 to 221R.03-226R.02; 225L.09-.13 is the passage Charrière III pp.551-552 prints.
Requests: gallica.bnf.fr 7. Subagent calls 22 (Sonnet).

## Remaining gaps (RUN2-NXDUP, 4 Oct 2026)
Read so far: 351 of 353 canvases surveyed at 400 px, 31 open/unclear C/P pages re-read at 1500 px; Dupuy 521 indexed whole (259 openings); 21 of 24 in-range cipher letters matched to a Dupuy copy (2 by text); Dupuy 221R-226R clear text transcribed (2 passes + reconciliation, 9,425 letters); c262 transcribed 4 times, gate failed twice; 0 open leaves decoded
- Glyph naming against Tomokiyo's table unsettled (readers split 31% on the same crops) - blocker: not-attempted; in progress in LANE-RUN2 wave 1 (RUN2-NXATL atlas, RUN2-NXTA/NXTB blind passes); next: sorter labels then the wave-2 gate, ~$6
- c510-516 known-plaintext pair with Dupuy 521 221R-226R not yet aligned - blocker: not-attempted; the clear side is now done (RUN2-NXDUP); next: RUN2-NXALN pre-registered held-out alignment gate (interlinear_align + gibbs_align) once the c510/c511/c515/c516 passes land, ~$8
- Date-only Dupuy matches (c330, c358-361, c409-410, c245/c464, c472-473) not text-checked - blocker: not-attempted; outside this brief; next: one native look per pair at the clear lead-in words on the fr.16142 leaf vs the Dupuy opening, ~$1
- "Relation d'une bataille" c231 has no clear copy found - blocker: not-attempted; not named in this brief; next: grep Charrière III and the Lepanto relations in print for its clear opening "Le gain de ceste grande bataille advenue en saison incommode", ~$1

## Escalation (RUN2-NXDUP, 4 Oct 2026)
- [x] siblings: the duplicata/original pairs in this volume found (letters_coverage.tsv); c245-246/c464 a further same-text pair (RUN1-NX)
- [x] clear-pages: Dupuy 521 indexed and aligned by date (RUN1-NX); Dupuy 221R-226R transcribed in full, two passes + reconciliation (RUN2-NXDUP)
- [x] known-keys: Tomokiyo's published key applied to c262; reconciled text and one blind pass beat every null, gate pass failed
- [x] print: Charrière III pp.520-524 and pp.551-558 read for the June-July 1574 excerpts
- [n/a] key-rebuild: a published key exists
- [x] image-check: c262 re-cut with --follow-slope (NX-RECUT); 31 open/unclear pages re-read at 1500 px (RUN1-NX)
- [ ] retry: known-answer alignment of c510-516 against the Dupuy clear text with settled glyph labels; planned step: RUN2-NXALN (wave 2)
Verdict: keep going: 4 internal gaps; cheapest next: text-check the date-only Dupuy matches, ~$1; the c510-516 alignment (RUN2-NXALN) waits on the wave-1 cipher passes

`python3 tools/gaps_check.py fr16142-noailles-constantinople-1571` (RUN2-NXDUP):
```
OK keep-going fr16142-noailles-constantinople-1571: keep going: 4 internal gap(s), 1 step(s) untried
## Two blind passes of c516 + c515 L01-L20 (LANE-RUN2 RUN2-NXTB, account 1, 4 Oct 2026, 02:46-03:00 UTC)

Brief: `.claude/briefs/runs/2026-10-04-acct1-run2-wave1.md` RUN2-NXTB. Intake gate re-run 02:46 UTC: `fr16142-noailles-constantinople-1571:
partial (line 1) -- edition/page or full-text-search citation found within 6 lines`, exit 0. No decode, no alignment, key.tsv untouched.
Full report: `run2/nxtb/REPORT.md`. c516's cipher is 18 lines (3 above the clear lead-in, 15 below; ~520 signs, not ~1,200);
c515 is 40 cipher lines (~1,250 signs at ~31/line). Crops for all 58 lines in `run2/nxtb/crops/` (`regen.sh`).

| leaf | signs (A/B) | err_2reader raw | after `recon_rules.py` |
|---|---|---|---|
| c516 | 515/504 | 57.0% | 27.8% (rules fitted on this leaf) |
| c515 L01-L20 | 608/610 | 46.1% | 45.4% (rules frozen before the passes ran: held out) |

The rules that took c516 from 57% to 28% bought c515 under one point: the readers describe the same unnamed shapes in new words
on each leaf, so reconciling by rule over descriptions does not transfer. Every reader on both leaves failed to name the same three
shapes against Tomokiyo's table (the 2-with-a-cross, the swash zp, the hash family #/H-hash/triple bar); `focus.tsv` ranks the split
pairs for the sign sorter. This is a third leaf (after c262) where table-image naming by Sonnet readers splits 28-57%: the glyph
inventory, not the cutting, is the limit (the rule 3 third-attempt situation NX-RECUT logged for c262, now seen on new material).
`reconciled.tsv` keeps both readings where they split (grade M); H only where both blind passes agree untouched (c516 169, c515 279).

## Remaining gaps (RUN2-NXTB, 4 Oct 2026)
Read so far: 351 of 353 canvases surveyed at 400 px, 31 open/unclear C/P pages re-read at 1500 px; Dupuy 521 indexed whole; c262 transcribed 4 times, gate failed twice; c516 cipher (18 lines) and c515 L01-L20 read by two blind passes each (err_2reader 57% / 46% raw); 0 open leaves decoded
- Glyph naming against Tomokiyo's table unsettled (readers split 28-57% on c262, c516, c515) - blocker: not-attempted; every known-answer use waits on it; next: owner sorts focus.tsv pairs (run2/nxtb/focus.tsv, c515/focus.tsv) with RUN2-NXATL's cluster sheets in the sign sorter, then blind passes against the settled labels, ~$6
- c515 L21-L40 not read by any pass - blocker: not-attempted; stopped at cap (USD 6.9 of 10 after the L01-L20 group); next: 2 passes x 2 calls on the existing crops after the sorter labels exist, ~$4
- c510-516 known-plaintext pair with Dupuy 521 221R-226R not yet used - blocker: not-attempted; wave 2 (RUN2-NXALN) by design; next: alignment with its pre-registered gate once NXDUP's clear text and settled labels exist, ~$4
- Date-only Dupuy matches (c330, c358-361, c409-410, c245/c464, c472-473) not text-checked - blocker: not-attempted; outside this brief; next: one native look per pair at the clear lead-in words, ~$1
- "Relation d'une bataille" c231 has no clear copy found - blocker: not-attempted; outside this brief; next: grep Charrière III and the Lepanto relations in print for its clear opening, ~$1

## Escalation (RUN2-NXTB, 4 Oct 2026)
- [x] siblings: the duplicata/original pairs in this volume found (letters_coverage.tsv); c245-246/c464 a further same-text pair (RUN1-NX)
- [x] clear-pages: Dupuy 521 indexed and aligned by date; c510-516 and c275-276 text-confirmed; Charrière III 7 July 1574 excerpts located
- [x] known-keys: Tomokiyo's published key applied to c262; reconciled text and one blind pass beat every null, gate pass failed
- [x] print: Charrière III pp.520-524 and pp.551-558 read for the June-July 1574 excerpts
- [n/a] key-rebuild: a published key exists
- [x] image-check: c262 re-cut (NX-RECUT); 31 pages at 1500 px (RUN1-NX); c516 + c515 cut with --follow-slope, one line hand-sheared off an ink smear (RUN2-NXTB)
- [ ] retry: known-answer with settled glyph labels (sign sorter), on c262 or c510-516 against Dupuy 221R-226R; planned step: sorter on focus.tsv + RUN2-NXATL clusters
Verdict: keep going: 5 internal gaps; cheapest next: text-check the date-only Dupuy matches, ~$1; every transcription step now waits on the sorter, not on more machine passes

`python3 tools/gaps_check.py fr16142-noailles-constantinople-1571` (RUN2-NXTB):
```
OK keep-going fr16142-noailles-constantinople-1571: keep going: 5 internal gap(s), 1 step(s) untried
gaps_check: 1 checked: 0 parked, 1 keep-going, 0 FAIL, 0 skipped
```

## c510 two blind passes (LANE-RUN2 RUN2-NXTA, account 1, 4 Oct 2026, from 02:46 UTC)

Brief: `.claude/briefs/runs/2026-10-04-acct1-run2-wave1.md` RUN2-NXTA; full report `run2/nxta/REPORT.md`. No decode, no alignment.
Intake gate (02:46 UTC): `fr16142-noailles-constantinople-1571: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`, exit 0.
c510 done in full (37 cipher lines, L00 = cipher tail of manuscript line 4 + L01-L36); c511 not started (0 lines). Native c510 crops
(`run2/nxta/regen.sh`), 2 blind Sonnet passes x 3 line groups, reconciled by family rules (`run2/nxta/reconciled.tsv`, `rebuild.sh --check`).
First real sign count for c510: A 1130, B 1123, reconciled 1156 (FT-D estimated ~1,500 per full page).
**err_2reader 41.8% raw, 39.1% after mapping the readers' free descriptions to table labels**; reconciled H 538 / M 618. Audit by this
worker on 2 lines not used to set the rules (L06, L30): reconciled text 0.409 sign error, H-graded signs 0.25 wrong (one more reader, not
a benchmark; err_true not measurable). The splits are glyph-naming families (focus.tsv: hash # / H-with-bars / ###; Y vs W:les vs s2; the
box-on-bar nomenclator signs; n1/u1; e3/r2/m1), some with both readers agreeing on the wrong label. c511 was not read: the same instrument
would add the same ~40% noise; the atlas (RUN2-NXATL) and sorter labels are the next instrument. No sorter sheet was cut here; `focus.tsv`
is the sign-pair list for one.

## Remaining gaps (RUN2-NXTA, 4 Oct 2026)
Read so far: 351 of 353 canvases surveyed at 400 px, 31 open/unclear C/P pages re-read at 1500 px; Dupuy 521 indexed whole; 21 of 24 in-range cipher letters matched to a Dupuy copy (2 by text); c262 transcribed 4 times, gate failed twice; c510 transcribed twice + reconciled (1156 signs, audit err ~0.41); 0 open leaves decoded
- Glyph naming against Tomokiyo's table unsettled (c262 split 31%, c510 split 39% after the label convention, audit ~41%) - blocker: not-attempted; every known-answer use waits on it; next: RUN2-NXATL atlas exemplar sheets + run2/nxta/focus.tsv into the sign sorter for the person to settle, then re-label passes A/B of c510 against the settled labels, ~$6
- c510-516 known-plaintext pair with Dupuy 521 221R-226R not yet used - blocker: not-attempted; wave 2 (RUN2-NXALN) by the lane's plan; next: pre-registered alignment of c510 (reconciled.tsv, or atlas cluster ids) against the Dupuy 221R text, ~$4
- c511 not transcribed - blocker: not-attempted; same instrument judged not worth a second leaf at ~40% error (RUN2-NXTA); next: two passes against settled sorter labels once they exist, ~$5
- Date-only Dupuy matches (c330, c358-361, c409-410, c245/c464, c472-473) not text-checked - blocker: not-attempted; outside this transcription brief; next: one native look per pair at the clear lead-in words vs the Dupuy opening, ~$1
- "Relation d'une bataille" c231 has no clear copy found - blocker: not-attempted; outside this transcription brief; next: grep Charrière III and Lepanto relations in print for its clear opening, ~$1

## Escalation (RUN2-NXTA, 4 Oct 2026)
- [x] siblings: the duplicata/original pairs in this volume found (letters_coverage.tsv); c245-246/c464 a further same-text pair (RUN1-NX)
- [x] clear-pages: Dupuy 521 indexed and aligned by date (dupuy521_align.tsv); c510-516 and c275-276 text-confirmed
- [x] known-keys: Tomokiyo's published key applied to c262; reconciled text and one blind pass beat every null, gate pass failed
- [x] print: Charrière III pp.520-524 and pp.551-558 read for the June-July 1574 excerpts
- [n/a] key-rebuild: a published key exists
- [x] image-check: c262 re-cut (NX-RECUT); c510 cut at native with --follow-slope, overlay checked (RUN2-NXTA)
- [ ] retry: known-answer with settled glyph labels (sign sorter), on c262 or c510 against Dupuy 221R; planned step: atlas + focus.tsv into the sorter
Verdict: keep going: 5 internal gaps; cheapest next: text-check the date-only Dupuy matches, ~$1; the known-answer retry needs the sorter first

`python3 tools/gaps_check.py fr16142-noailles-constantinople-1571` (RUN2-NXTA):
```
OK keep-going fr16142-noailles-constantinople-1571: keep going: 5 internal gap(s), 1 step(s) untried
gaps_check: 1 checked: 0 parked, 1 keep-going, 0 FAIL, 0 skipped
```

## Family atlas c510-516 + c262 (LANE-RUN2 RUN2-NXATL, account 1, 4 Oct 2026, from 02:46 UTC)

Full report: `run2/nxatl/REPORT.md`. No decode, no Dupuy alignment, no key.tsv on c510-516 (wave 2 stays blind).
- Native f510-f516 fetched once (7 Gallica requests); lines cut with `tools/iiif_lines.py --follow-slope 300` and `--centres`
  from each block's left 600 px (output in `run2/nxatl/iiif_lines_out.txt`; overlays checked, one row per band).
- Clear text: c510 L01-L04 + the first 22 tiles of L05 ("Jours au paravant La reception d'icelle que"): cipher starts c510 L05.
  c516 has no clear lead-in: L04-L05 are a clear passage inside the cipher, L20-L23 the clear closing and subscription
  ("vj^e de Juillet 1574"); L19 may end in a short clear tail (kept, flagged M).
- `tools/glyph_atlas.py segment` per strip + one-line/overlap/intrusion filter; sizes in leaf units. **Segmentation check on c262:
  403 tiles vs 384 reconciled signs (1.05), every line within 25% (0.84-1.14)** -- in-sample (the filter was chosen on c262).
- **Count of c510-516: 253 cipher lines, 9,904 tiles, ~9,440 signs at c262's tile/sign ratio** (FT-D estimated 9,750).
  Per leaf in `run2/nxatl/sign_counts.tsv`.
- Cluster k=120 (over-split), marks k=24; `classify --topk 3` with cluster ids as labels (kNN = own cluster 90.9%).
  `run2/nxatl/sequences.tsv` = every tile in reading order with cluster and top-3 cluster ids -- the second instrument for
  RUN2-NXALN (no reader names a sign).
- Provisional names from c262 tile positions (hard-EM NW alignment to `witness/c262rc_recon.tsv`, grade M):
  74 of 120 clusters named, 17 with support >= 3 and purity >= 0.6; weighted purity 0.593 vs 0.311-0.356 with cluster ids
  shuffled (20 seeds; descriptive, not a gate). `run2/nxatl/cluster_provisional_names.tsv`.
- Exemplar sheets (sorter-ready): `run2/nxatl/sheets/atlas_k*.jpg`, 20 clusters x 12 exemplars per image.
- Rule 7: `bash run2/nxatl/regen.sh WORK --check` (exact against `source_manifest.json` sha1s; Gallica re-encoded c513/c514
  on a second fetch, so a refetch runs a 1% tile-count check -- c513 1,625 -> 1,621, the rest identical).

## Remaining gaps (RUN2-NXATL, 4 Oct 2026)
Read so far: c510-516 segmented whole (253 cipher lines, 9,904 tiles in 120 clusters); c262 block aligned to its reconciled labels; 0 open leaves decoded
- Glyph naming against Tomokiyo's table unsettled (c262 split 31%, c510 39% per RUN2-NXTA) - blocker: not-attempted; atlas and exemplar sheets now exist (RUN2-NXATL); next: account 3 publishes the sorter from run2/nxatl (sheets + clusters.tsv) with run2/nxta/focus.tsv and the person settles the clusters, then blind passes against settled labels, ~$2 to publish
- c510-516 known-plaintext pair with Dupuy 521 221R-226R not yet used - blocker: not-attempted; wave 2 (RUN2-NXALN) after RUN2-NXDUP's clear text; next: pre-registered alignment of run2/nxatl/sequences.tsv (cluster ids) and the wave-1 blind passes to the Dupuy text, ~$5
- c511 not transcribed by readers (segmented only, run2/nxatl) - blocker: not-attempted; RUN2-NXTA judged the table-image pass not worth a second leaf at ~40% error; next: two passes against settled sorter labels once they exist, ~$5
- Date-only Dupuy matches (c330, c358-361, c409-410, c245/c464, c472-473) not text-checked - blocker: not-attempted; not in this brief; next: one native look per pair at the clear lead-in words, ~$1
- "Relation d'une bataille" c231 has no clear copy found - blocker: not-attempted; not in this brief; next: grep Charrière III and the Lepanto relations for its clear opening, ~$1

## Escalation (RUN2-NXATL, 4 Oct 2026)
- [x] siblings: the duplicata/original pairs in this volume found (letters_coverage.tsv)
- [x] clear-pages: Dupuy 521 indexed and aligned by date; c510-516 text-confirmed against Dupuy 221R-226R (RUN1-NX)
- [x] known-keys: Tomokiyo's published key applied to c262; reconciled text and one blind pass beat every null, gate pass failed
- [x] print: Charrière III pp.520-524 and pp.551-558 read
- [n/a] key-rebuild: a published key exists
- [x] image-check: c262 re-cut (NX-RECUT); c510-516 native line bands with --follow-slope, overlays checked (RUN2-NXATL)
- [ ] retry: known-answer with settled glyph labels or cluster ids on c510 against Dupuy 221R; planned step: RUN2-NXALN (wave 2)
Verdict: keep going: 5 internal gaps; cheapest next: text-check the date-only Dupuy matches, ~$1; the c510-516 alignment is wave 2

`python3 tools/gaps_check.py fr16142-noailles-constantinople-1571` (RUN2-NXATL):
```
OK keep-going fr16142-noailles-constantinople-1571: keep going: 4 internal gap(s), 1 step(s) untried
gaps_check: 1 checked: 0 parked, 1 keep-going, 0 FAIL, 0 skipped
```

## Known-plaintext alignment c510-516 vs Dupuy 221R-226R (LANE-RUN2 RUN2-NXALN, account 1, 4 Oct 2026, from 03:18 UTC)
Pre-registered (`run2/nxaln/PREREG.md`, pushed before any alignment output; amendment 1 adds a control at Tomokiyo's key shape, ~109
symbols). New shared option `tools/interlinear_align.py stream` (`tools/stream_align.py`, test `tools/tests/test_stream_align.py`):
banded, anchored, progressively grown hard-EM alignment of the whole cipher stream against the whole clear copy. Atlas instrument
(train c510-513, held-out c514-516): target held-out accuracy **0.363** vs nulls (a) shuffled key p99 0.365, (b) shuffled-text
retraining max 0.368, (c) wrong text p99 0.366 -- **FAIL, and a non-test**: the design-matched control at the atlas's measured ~40%
cluster impurity fails its own gate on 2 of 3 seeds (0.447 / 0.537 / 0.430 vs nulls ~0.43-0.46), while the same control passes at 25%
(0.667) and 10% (0.756); the 41-symbol control passes at all three levels. Learned key `run2/nxaln/key_learned.tsv`, all grade M
(aligners agree 13/98; c262 provisional labels agree 9/66). Line-read instrument not run (box/cap; brief's atlas-first rule). Details and
the order of runs: `run2/nxaln/REPORT.md`. Rule 7: `python3 run2/nxaln/nxaln.py check` exits 0. No reading is claimed.

## Remaining gaps (RUN2-NXALN, 4 Oct 2026)
Read so far: c510-516 segmented whole (9,904 tiles, 120 clusters); whole-letter alignment to Dupuy 221R-226R run on the atlas clusters, non-test at ~40% impurity; 0 open leaves decoded
- Glyph naming / cluster impurity (~40% from c262 purity 0.593) too high for the stream aligner (design control crosses its gate between 25% and 40%) - blocker: not-attempted; RUN2-NXALN design curve; next: account 3 publishes the sorter from run2/nxatl (sheets + clusters.tsv) and the person settles the clusters, then re-run `nxaln.py target` unchanged on the settled labels, ~$2 to publish + ~$1 to re-run
- c510-516 alignment by line reads (instrument 2: train c510, held-out c516 + c515 L01-L20) not run - blocker: not-attempted; RUN2-NXALN ran the atlas first by the brief's rule; next: same pipeline with a 40%-noise 41-symbol and design control first, ~$2
- c511 not transcribed by readers (segmented only, run2/nxatl) - blocker: not-attempted; next: two passes against settled sorter labels once they exist, ~$5
- Date-only Dupuy matches (c330, c358-361, c409-410, c245/c464, c472-473) not text-checked - blocker: not-attempted; not in this brief; next: one native look per pair at the clear lead-in words, ~$1
- "Relation d'une bataille" c231 has no clear copy found - blocker: not-attempted; not in this brief; next: grep Charrière III and the Lepanto relations for its clear opening, ~$1

## Escalation (RUN2-NXALN, 4 Oct 2026)
- [x] siblings: the duplicata/original pairs in this volume found (letters_coverage.tsv)
- [x] clear-pages: Dupuy 521 221R-226R transcribed (RUN2-NXDUP) and aligned whole to c510-516 (RUN2-NXALN, non-test at the atlas's noise)
- [x] known-keys: Tomokiyo's published key applied to c262; reconciled text and one blind pass beat every null, gate pass failed
- [x] print: Charrière III pp.520-524 and pp.551-558 read
- [n/a] key-rebuild: a published key exists
- [x] image-check: c262 re-cut (NX-RECUT); c510-516 native line bands with --follow-slope, overlays checked (RUN2-NXATL)
- [ ] retry: the same pre-registered alignment on settled sorter labels (impurity <= ~25%), or on the line reads with their own control; planned step: re-run `run2/nxaln/nxaln.py` after the sorter pass
Verdict: keep going: 5 internal gaps; cheapest next: line-read instrument with its control, ~$2, or text-check the date-only Dupuy matches, ~$1

`python3 tools/gaps_check.py fr16142-noailles-constantinople-1571` (RUN2-NXALN):
```
OK keep-going fr16142-noailles-constantinople-1571: keep going: 4 internal gap(s), 1 step(s) untried
gaps_check: 1 checked: 0 parked, 1 keep-going, 0 FAIL, 0 skipped
```

## Sign-sorter page c510-516 (LANE-NEAR4 N4-NXS, account 2, 4 Oct 2026, 04:17-04:5x UTC)
Built one sign-sorter page from RUN2-NXATL's atlas (committed cluster ids) and the RUN2-NXTA/NXTB reader splits: 9,863 tiles,
120 piles = 120 atlas clusters, 86 "Check these first" tiles, 13.9 MB with the size options this job added to
`tools/sign_sorter.py` (92 MB at the defaults). Not committed (the folder is 24 MB): `sorter/build.sh WORKDIR` rebuilds it
(7 Gallica requests) and `sorter/README.md` gives the build, the checks and the publish/apply commands. No decode, no reading.

## Remaining gaps (N4-NXS, 4 Oct 2026)
Read so far: c510-516 segmented whole (9,904 tiles, 120 clusters); sorter page buildable, not yet published or sorted; 0 open leaves decoded
- Glyph naming / cluster impurity (~40% from c262 purity 0.593) too high for the stream aligner - blocker: waiting-on the account-3 orchestrator publishing `sorter/build.sh`'s page and the owner's sort (ROOM 4 Oct 2026, N4-NXS done line); next: `tools/sign_sorter_apply.py --clusters run2/nxatl/clusters.tsv --atlas-labels run2/nxatl/labels_clusterid.json`, then re-run `nxaln.py target` unchanged on the settled labels, ~$1
- c510-516 alignment by line reads (instrument 2: train c510, held-out c516 + c515 L01-L20) not run - blocker: not-attempted; RUN2-NXALN ran the atlas first by the brief's rule; next: same pipeline with a 40%-noise 41-symbol and design control first, ~$2
- c511 not transcribed by readers (segmented only, run2/nxatl) - blocker: not-attempted; next: two passes against settled sorter labels once they exist, ~$5
- Date-only Dupuy matches (c330, c358-361, c409-410, c245/c464, c472-473) not text-checked - blocker: not-attempted; not in this brief; next: one native look per pair at the clear lead-in words, ~$1
- "Relation d'une bataille" c231 has no clear copy found - blocker: not-attempted; not in this brief; next: grep Charrière III and the Lepanto relations for its clear opening, ~$1

## Escalation (N4-NXS, 4 Oct 2026)
- [x] siblings: the duplicata/original pairs in this volume found (letters_coverage.tsv)
- [x] clear-pages: Dupuy 521 221R-226R transcribed (RUN2-NXDUP) and aligned whole to c510-516 (RUN2-NXALN, non-test at the atlas's noise)
- [x] known-keys: Tomokiyo's published key applied to c262; reconciled text and one blind pass beat every null, gate pass failed
- [x] print: Charrière III pp.520-524 and pp.551-558 read
- [n/a] key-rebuild: a published key exists
- [x] image-check: c262 re-cut (NX-RECUT); c510-516 native line bands with --follow-slope, overlays checked (RUN2-NXATL)
- [ ] retry: the same pre-registered alignment on settled sorter labels (impurity <= ~25%), or on the line reads with their own control; planned step: re-run `run2/nxaln/nxaln.py` after the sorter pass (page: `sorter/build.sh`)
Verdict: keep going: 4 internal gaps (1 waiting on the sort); cheapest next: line-read instrument with its control, ~$2, or text-check the date-only Dupuy matches, ~$1

`python3 tools/gaps_check.py fr16142-noailles-constantinople-1571` (N4-NXS):
```
OK keep-going fr16142-noailles-constantinople-1571: keep going: 4 internal gap(s), 1 step(s) untried
```
