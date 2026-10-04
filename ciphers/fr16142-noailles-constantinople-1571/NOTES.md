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

(Step 2, Dupuy 521 date index, in progress at 01:2x UTC; section continues below when done.)
