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

## NOX-OWNERSORT (4 Oct 2026)
Account-3 worker for the account-3 orchestrator, 07:31-07:4x UTC; brief `.claude/briefs/runs/2026-10-04-acct3-nox-ownersort.md`.
Input: the owner's quick pass (`sorter/owner-sort-2026-10-04/`: 18 pile merges over 1,835 tiles, 36 moves, 4 bad cuts). Pre-registered
in `sorter/owner-sort-2026-10-04/nox/PREREG.md` (commit 0da5f9b6, 07:33 UTC, before any statistic; three deviations logged there).
Script `nox/nox_ownersort.py` (`--check` exits 0). No decode, no reading; the owner's piles are a third reader, not ground truth.

Reader signs (RUN2-NXTA c510, RUN2-NXTB c516 + c515 L01-L20, each pass separately) were placed on atlas tiles two ways: P1 the
build's label-blind same-fraction rule (about +-2 tiles, so noisy), P2 a per-line alignment scored by hard-EM P(label|cluster)
(sharper, partly circular). Statistic per merge: chance that a reader gives a tile in pile a and a tile in pile b the same label,
against 64 size-matched pile pairs.

**Step 1, per merge** (`nox/merges.tsv`): P1 (pre-registered decision) corroborated 3, weak 5, not corroborated 6, readers silent 4;
P2 corroborated 9, weak 3, silent 6. Read together:
- held up: k029, k042, k106 (both placements); k013, k056 -> k107 (the a2 pile), k088, k116 -> k091 (o1/e2), k093 -> k098,
  k094 -> k064 (also c262's labels, S 0.59) on P2; k018 and k037 -> k115 by the sibling check (both read a1, P2 100th pct;
  k115 itself has no reader signs).
- doubtful: **k026 / k076 -> k060** (the two sources share no reader label on either placement, 0th pct; c262 supports k076 ~ k060,
  so k026 is the suspect); **k104 -> k034** (P1 not corroborated, P2 S 0.009).
- readers cannot judge: k009, k083 -> k065 and k080 -> k000 sit in the hash family (r1 vs o1/e2), the shapes the readers
  themselves split on (RUN2-NXTA focus.tsv); k002 -> k035 weak, too few reader signs on P2.

**Step 2, transcription error** (`nox/impurity.tsv`): err_true not measurable (no fr16142 row in BENCHMARK-TX.tsv). err_2reader is
unchanged by a sort (41.8% c510, 46-57% c515/c516 raw; the sort relabels tiles, not reader passes). Pile impurity against the 963
(P1) / 1,040 (P2) signs both passes of a reader agree on: **before 0.690 -> after 0.688 (P1), 0.163 -> 0.170 (P2)**. 200 random sets
of 18 size-matched merges raise it by 0.013 (P1, p05 0.008) and 0.079 (P2, p05 0.058); **0 of 200 random sets do as well as the
owner** on either placement. So the merges are real (they join piles of the same sign), but they cut the pile count (120 -> 108)
without lowering impurity, and impurity is what RUN2-NXALN's aligner needs below ~25% (its design control fails at ~40%).

**Step 3, what is left** (`nox/next_targets.tsv`, 3 piles + 40 tiles): the pre-registered P1 rule found no mixed pile (placement too
noisy); ranked on P2 instead (exploratory). Piles: **k065** (now 498 tiles; 41 agreed signs split r1 19 / o1/e2 13), **k079**
(o1/e2 7 / t2 5), **k060** (re-check the k026/k076 merge). Tiles: 40 where both passes of a reader agree on a label of a different
letter from the pile's majority, weighted to tiles whose own atlas neighbours vote elsewhere (14 in k065, 6 in k000, 6 in k079,
5 in k060). How much impurity the readers can see as removable: top 3 piles 9.4 points (P1) / 3.8 (P2); c262's provisional names put
the top 3 clusters at 11.7 and the top 10 at 25.5 of its 40.7%.

**Verdict for the owner:** deeper sorting would help only as splitting, not merging, and only in a few places: the 18 merges were
right (better than every random control) but left impurity where it was, and what the readers still see mixed sits in the hash
family (k065, k000) and k079, plus one doubtful merge (k026 into k060). Cheapest first: re-run `run2/nxaln/nxaln.py target` on the
settled labels (~$1) to measure where the aligner now stands; then a short split pass on next_targets.tsv (3 piles + 40 tiles,
about 10-15 minutes of the owner's time) and re-measure.

## Remaining gaps (NOX-OWNERSORT, 4 Oct 2026)
Read so far: c510-516 segmented whole (9,904 tiles, 120 clusters); owner quick sort folded in and checked against both readers (merges real, impurity unchanged); 0 open leaves decoded
- Cluster impurity (~40% from c262) too high for the stream aligner; the owner's merges did not lower it (0.690 -> 0.688 on P1) - blocker: not-attempted; next: re-run `run2/nxaln/nxaln.py target` unchanged on `sorter/owner-sort-2026-10-04/settled_labels.tsv`, ~$1, then the owner's split pass on `nox/next_targets.tsv` if it still fails, ~$1 to rebuild the page
- c510-516 alignment by line reads (instrument 2: train c510, held-out c516 + c515 L01-L20) not run - blocker: not-attempted; next: same pipeline with a 40%-noise 41-symbol and design control first, ~$2
- c511 not transcribed by readers (segmented only, run2/nxatl) - blocker: not-attempted; next: two passes against settled sorter labels, ~$5
- Date-only Dupuy matches (c330, c358-361, c409-410, c245/c464, c472-473) not text-checked - blocker: not-attempted; not in this brief; next: one native look per pair at the clear lead-in words, ~$1
- "Relation d'une bataille" c231 has no clear copy found - blocker: not-attempted; not in this brief; next: grep Charrière III and the Lepanto relations for its clear opening, ~$1

## Escalation (NOX-OWNERSORT, 4 Oct 2026)
- [x] siblings: the duplicata/original pairs in this volume found (letters_coverage.tsv)
- [x] clear-pages: Dupuy 521 221R-226R transcribed (RUN2-NXDUP) and aligned whole to c510-516 (RUN2-NXALN, non-test at the atlas's noise)
- [x] known-keys: Tomokiyo's published key applied to c262; reconciled text and one blind pass beat every null, gate pass failed
- [x] print: Charrière III pp.520-524 and pp.551-558 read
- [n/a] key-rebuild: a published key exists
- [x] image-check: c262 re-cut (NX-RECUT); c510-516 native line bands (RUN2-NXATL); owner sort of the atlas piles (4 Oct 2026, checked by NOX-OWNERSORT)
- [ ] retry: the same pre-registered alignment on the owner's settled labels; planned step: re-run `run2/nxaln/nxaln.py target` on `sorter/owner-sort-2026-10-04/settled_labels.tsv`
Verdict: keep going: 4 internal gaps; cheapest next: re-run nxaln.py on the settled labels, ~$1

`python3 tools/gaps_check.py fr16142-noailles-constantinople-1571` (NOX-OWNERSORT):
```
OK keep-going fr16142-noailles-constantinople-1571: keep going: 4 internal gap(s), 1 step(s) untried
gaps_check: 1 checked: 0 parked, 1 keep-going, 0 FAIL, 0 skipped
```

## NOX-ALN (4 Oct 2026)
Account-3 worker for the account-3 orchestrator, 08:55-09:3x UTC; brief `.claude/briefs/runs/2026-10-04-acct3-nox-aln.md`. Pre-registered
in `sorter/owner-sort-2026-10-04/aln/PREREG.md` (commit d6bb89b5, 08:56 UTC, before any run). Script `aln/nox_aln.py` imports
`run2/nxaln/nxaln.py` unchanged; `python3 aln/nox_aln.py check` exits 0. No reading is claimed; every learned value stays grade M.

**Pre-registered result.** RUN2-NXALN's atlas instrument re-run unchanged on the owner's settled labels (116 symbols: 108 piles plus
8 one-tile ghosts, see deviation): held-out accuracy **0.355** vs null (a) shuffled key p99 0.360, (b) shuffled-text max 0.361 (40),
(c) wrong text p99 0.360 -> **FAIL** (before the sort: 0.363, also FAIL). The licensing design control at the post-sort pile count
(108 piles, 40% impurity) now **passes 3 of 3 seeds** (0.544 / 0.451 / 0.552 vs nulls <= 0.444; at 120 piles it passed 1 of 3), so on
the pre-registered rule this FAIL is control-backed at 40% noise -- though seed 1 clears by 0.007 and the control's noise is uniform
random relabelling, not the real hash-family confusion. Random-merge control (20 sets of 18 size-matched merges, owner's moves and bad
cuts kept): owner delta -0.007 (0.363 -> 0.355); random deltas mean +0.021; 4 of 20 random sets at or below the owner.
Two-reader numbers (quoted from NOX-OWNERSORT `nox/impurity.tsv`, same labels): err_2reader unchanged by a sort (41.8% c510, 46-57%
c515/c516); pile impurity vs reader-agreed signs before -> after 0.690 -> 0.688 (P1), 0.163 -> 0.170 (P2); 0 of 200 random 18-merge
sets do as well as the owner.

**Exploratory finding (not pre-registered; from the random-merge control).** Two random sets (7, 11) scored 0.534 / 0.518, far above
their own nulls (shuffled key p99 0.387 / 0.385, wrong text 0.396 / 0.394; `aln/results/diag_rand.json`); their train paths end at
letter ~5,734 (6,218 tiles: 1.08 tiles per letter, the c262 ratio 1.05) where every failing run ends at ~6,100-6,370 (drift). The only
merge both share is **k014 -> k077**. Owner labels + that one merge, full pipeline unchanged (`aln/full_pair.py k014 k077`): held-out
**0.630** vs (a) p99 0.380, (b) max 0.406 (40 shuffled-text retrainings), (c) p99 0.397 -> **passes all three nulls**. The atlas
clusters before the sort + the same merge do not lock on (0.369, path end 6,138): the owner's sort is part of it. Read: the aligner
locks onto Dupuy 221R-226R when the inventory falls in the right basin; the failing runs are a search failure, not only noise. Caveats:
post hoc (found among 20 + 1 tries, so not a licensed pass); c262 provisional names call k014 i2 and k077 o1/e2, different letters, so
the merge may be wrong as a sign identity even if it unlocks the search. Every value stays grade M. Files: `aln/results/`.

**Step 3, for the owner** (`aln/next_targets.tsv`, `aln/targets.json` with sids): piles 1 **k014 + k077** (are they one sign? decides
whether the lock-on is a real merge), 2 **k065** (score 77: reader agreed signs r1 19 / o1/e2 13; 163 of 236 aligned tiles off its modal
letter), 3 **k000** (score 18.6: o1/e2 24 / r1 5); k060's doubtful merge drops to 4th (score 15.4) and keeps its 5 tiles among the 40.
Tiles: NOX-OWNERSORT's 40 reader-conflict tiles re-ranked (chosen piles first, then by pile score).

Deviation: 39 tiles absent from settled_labels.tsv kept their atlas cluster as pre-registered; 8 of them sit in merged-away piles, so
the after-sort run carries 8 one-tile ghost symbols (116 not 108). 8 of 9,900 tiles cannot move the 0.005 gap; not re-run.

## Remaining gaps (NOX-ALN, 4 Oct 2026)
Read so far: c510-516 segmented whole (9,904 tiles, 120 clusters -> 108 owner piles); the stream aligner locks onto Dupuy 221R-226R on owner labels + k014->k077 (held-out 0.630, all nulls passed, exploratory); 0 open leaves decoded
- Lock-on is post hoc: k014->k077 found from the random-merge control - blocker: not-attempted; next: pre-register and run the confirmation (fresh seeds for the nulls, design control at the same pile count, plus 10 other single merges as a specificity control), ~$1.5; and the owner's look at k014 vs k077 on the page
- Key from the locked-on alignment not extracted or graded - blocker: not-attempted; next: after confirmation, key_learned from `aln/results/full_pair_k014_k077_counts.tsv` vs key.tsv (Tomokiyo) agreement, then decode a leaf not aligned to Dupuy, ~$2
- c510-516 alignment by line reads (instrument 2) not run - blocker: not-attempted; next: same pipeline with its control first, ~$2
- c511 not transcribed by readers - blocker: not-attempted; next: two passes against settled labels, ~$5
- Date-only Dupuy matches (c330, c358-361, c409-410, c245/c464, c472-473) not text-checked - blocker: not-attempted; next: one native look per pair, ~$1
- "Relation d'une bataille" c231 has no clear copy found - blocker: not-attempted; next: grep Charrière III and the Lepanto relations, ~$1

## Escalation (NOX-ALN, 4 Oct 2026)
- [x] siblings: the duplicata/original pairs in this volume found (letters_coverage.tsv)
- [x] clear-pages: Dupuy 521 221R-226R transcribed and aligned whole; on owner labels + k014->k077 the alignment locks on (exploratory)
- [x] known-keys: Tomokiyo's published key applied to c262; reconciled text and one blind pass beat every null, gate pass failed
- [x] print: Charrière III pp.520-524 and pp.551-558 read
- [n/a] key-rebuild: a published key exists
- [x] image-check: c262 re-cut; c510-516 native line bands; owner sort of the atlas piles (checked by NOX-OWNERSORT, re-aligned by NOX-ALN)
- [ ] retry: pre-registered confirmation of the k014->k077 lock-on with a specificity control; planned step: `aln/full_pair.py` under a new PREREG
Verdict: keep going: 6 internal gaps; cheapest next: pre-registered confirmation of the lock-on, ~$1.5

`python3 tools/gaps_check.py fr16142-noailles-constantinople-1571` (NOX-ALN):
```
OK keep-going fr16142-noailles-constantinople-1571: keep going: 4 internal gap(s), 1 step(s) untried
gaps_check: 1 checked: 0 parked, 1 keep-going, 0 FAIL, 0 skipped
```

## NOX-CONFIRM (4 Oct 2026)
Account-3 worker for the account-3 orchestrator, 09:43-10:1x UTC; brief `.claude/briefs/runs/2026-10-04-acct3-nox-confirm.md`.
Pre-registered in `sorter/owner-sort-2026-10-04/aln/PREREG-CONFIRM.md` (commit b4c42a98, 09:44 UTC, before any run). Script
`aln/confirm.py` (imports `nox_aln.py` and `run2/nxaln/nxaln.py` unchanged); results `aln/results/confirm_*.json`,
`confirm_summary.json`. Requests 0, subagents 0.

**Verdict: FAIL (not confirmed as specific to k014->k077).** Arm 1 passes, Arm 2 fails.
- Arm 1, fresh seeds (owner labels + k014->k077, nulls a/c 200, b 40 max): held-out acc 0.630 at every seed (the train
  alignment is deterministic, so this is the rule-7 reproduction of NOX-ALN's 0.6298; only the nulls are re-drawn). Seed 20261005:
  a p99 0.375, b max 0.407, c p99 0.396; 20261006: 0.376 / 0.404 / 0.399; 20261007: 0.378 / 0.404 / 0.394 -> locks on 3/3.
- Arm 2, specificity (20 nearest single merges in place of k014->k077, nulls a/c 200, b 10 max): **8 of 20 lock on** (gate: at
  most 1). Six of them clear 0.50: k014->k017 0.628, k017->k077 0.626, k014->k048 0.598, k014->k010 0.594, k014->k031 0.544,
  k108->k077 0.528; two pass marginally: k109->k077 0.390, k014->k078 0.382. Seven pass a and c alone. The other 12 sit at
  0.353-0.401, at their nulls.

**What it means, in plain words.** The k014->k077 merge is not special: changing the inventory by one merge in several different
ways, most of them involving k014 or k077, puts the aligner in the same state. All six high-scoring runs end their train path at
letter 5,732-5,735, the same as the target, while the failing runs end around 6,100. So there is a stable alignment of c510-513
against Dupuy 521 221R-226R that scores 0.53-0.63 on held-out c514-516 against nulls near 0.40. The search reaches it only when
the inventory is perturbed near k014/k077. That supports NOX-ALN's reading that the earlier failures were a search failure, but it
gives **no evidence that k014 and k077 are one sign**. This job licenses nothing beyond NOX-ALN: no position map and no
candidate values are promoted, every value stays grade M, and no reading is claimed. Because the run FAILed, the brief's
PASS-only listing (what the lock-on licenses, the position map) is not written.

One-line suggestion (not done, outside the brief): pre-register a basin test. Do the six high-scoring runs learn the same key on the
same piles (pairwise agreement of `decode(counts)` vs a matched null)? If they do, the basin is a real property of the stream, not
of any one merge, and its common key is the thing to grade; ~$1.

## Remaining gaps (NOX-CONFIRM, 4 Oct 2026)
Read so far: c510-516 segmented whole (9,904 tiles, 120 clusters -> 108 owner piles); the stream aligner locks onto Dupuy 221R-226R on owner labels + k014->k077 (held-out 0.630, all nulls passed at 3 fresh seeds; NOX-CONFIRM: not specific to that merge, 8/20 alternatives also lock on); 0 open leaves decoded
- Lock-on basin not characterised: NOX-CONFIRM found it is not specific to k014->k077 (8/20 nearest single merges also lock on, 6 at 0.53-0.63, same path end ~5,734) - blocker: not-attempted; next: pre-registered basin test (do the six locked runs learn one common key vs a matched null?), ~$1; and the owner's look at k014 vs k077 (and k017) on the page
- Key from the locked-on alignment not extracted or graded - blocker: not-attempted; next: after the basin test, key_learned from `aln/results/full_pair_k014_k077_counts.tsv` vs key.tsv (Tomokiyo) agreement, then decode a leaf not aligned to Dupuy, ~$2
- c510-516 alignment by line reads (instrument 2) not run - blocker: not-attempted; next: same pipeline with its control first, ~$2
- c511 not transcribed by readers - blocker: not-attempted; next: two passes against settled labels, ~$5
- Date-only Dupuy matches (c330, c358-361, c409-410, c245/c464, c472-473) not text-checked - blocker: not-attempted; next: one native look per pair, ~$1
- "Relation d'une bataille" c231 has no clear copy found - blocker: not-attempted; next: grep Charrière III and the Lepanto relations, ~$1

## Escalation (NOX-CONFIRM, 4 Oct 2026)
- [x] siblings: the duplicata/original pairs in this volume found (letters_coverage.tsv)
- [ ] basin test: do the locked-on runs share one key (pre-registered, vs matched null); planned step: `aln/confirm.py` results + a new PREREG
- [x] clear-pages: Dupuy 521 221R-226R transcribed and aligned whole; on owner labels + k014->k077 the alignment locks on (exploratory)
- [x] known-keys: Tomokiyo's published key applied to c262; reconciled text and one blind pass beat every null, gate pass failed
- [x] print: Charrière III pp.520-524 and pp.551-558 read
- [n/a] key-rebuild: a published key exists
- [x] image-check: c262 re-cut; c510-516 native line bands; owner sort of the atlas piles (checked by NOX-OWNERSORT, re-aligned by NOX-ALN)
- [x] retry: pre-registered confirmation of k014->k077 (NOX-CONFIRM): fresh seeds 3/3 lock on, specificity 8/20 alternatives also lock on -> FAIL as a specific merge
Verdict: keep going: 6 internal gaps; cheapest next: pre-registered basin test of the locked-on runs, ~$1


`python3 tools/gaps_check.py fr16142-noailles-constantinople-1571` (NOX-CONFIRM):
```
OK keep-going fr16142-noailles-constantinople-1571: keep going: 4 internal gap(s), 1 step(s) untried
gaps_check: 1 checked: 0 parked, 1 keep-going, 0 FAIL, 0 skipped
```

## N8-NOX basin test (4 Oct 2026)
LANE-NEAR8 worker N8-NOX (account 2), 16:40-16:5x UTC by `date -u`; brief `.claude/briefs/runs/2026-10-04-ytbiz-near8-wave2.md`.
Pre-registered in `sorter/owner-sort-2026-10-04/aln/PREREG-BASIN.md` (commit 29a256ef, 16:42 UTC, before any statistic). Script
`aln/basin.py` (imports nox_aln / confirm / nxaln / stream_align unchanged); keys `aln/results/basin_keys.json` (79 learned keys),
numbers `aln/results/basin_summary.json`; `python3 aln/basin.py check` exits 0 (six locked keys re-learned identically). Disk only:
requests 0, subagents 0. No reading is claimed; every value stays grade M; key.tsv unchanged.

**Step 1, basin (PASS).** The six locked runs (alt 04, 05, 06, 08, 12, 14; held-out 0.53-0.63) learn largely one key: mean pairwise
agreement over shared piles (102-106 per pair) **S = 0.601** (token-weighted 0.730; with the k014->k077 target as a 7th run 0.617;
pairs 0.40-0.91). Matched nulls, same N of six runs and same inventory family: **N1 non-locking** (every 6-subset of the 12 runs that
failed NOX-CONFIRM's gate, 924 subsets) mean 0.207, **p99 0.273** (max 0.285); **N2 shuffled Dupuy** (the six locked merges re-learned
against word-shuffled Dupuy 221R-226R, 10 seeds) mean 0.294, **max 0.384**. S beats both -> PASS. In plain words: the lock-on is a
property of the c510-513 stream against Dupuy 221R-226R, not of any one merge; the locked runs converge on a common key, the failing
runs and the shuffled-text runs do not.

**Step 2, key_learned vs key.tsv via the c262 bridge (FAIL on the registered rule).** The only bridge from atlas piles to Tomokiyo's
key is `run2/nxatl/cluster_provisional_names.tsv` (c262 tile majority under key.tsv, itself grade M). 17 piles qualify; the locked
consensus (>= 4 of 6 runs) exists on 11, and agrees with the provisional letter on **6 of 11, K = 0.545**: k022 e, k053 s, k060 l,
k073 t, k102 d, k115 a agree; k021 d (prov. x), k045 x (f), k071 m (e), k086 r (y), k117 e (n) do not. Null (a) value permutation
p99 0.364 -> passed; null (b) non-locking 6-subsets' consensus p99 **1.000** (mean 0.701) -> not passed, so FAIL as registered.
Caveat on null (b), found after scoring and not used to override it: the non-locking subsets reach a >= 4-of-6 majority on only
2.2 of the 17 piles on average (0-6; 10 subsets none), mostly the high-frequency piles k115 a, k053 s, k022 e, so their share is a
ratio over 1-3 piles and sits near 1.0 by small N. Counted as hits instead (exploratory): locked 6, non-locking mean 1.3, max 3. The
registered null had no power at this consensus size (the rule-3 "control that cannot fail differently" shape in a milder form); this
step is "judge cannot decide at 11 piles", not a negative on the basin's key.

**Verdict.** Step 1 PASS: the basin has one common key (S 0.601 vs N1 p99 0.273, N2 max 0.384). Step 2 FAIL as registered (K 0.545
vs permutation p99 0.364 passed, non-locking p99 1.000 not passed), with a null that was degenerate at this N. Nothing promoted;
every value grade M. One-line suggestion (not done): re-register step 2 with a count-based statistic (hits among piles where the
locked consensus exists, null = the same count for the non-locking runs' own keys taken one run at a time, and a shuffled-Dupuy arm),
or widen the bridge by placing c262 tiles under the owner's labels so more than 17 piles carry a key.tsv value, ~$1.

## Remaining gaps (N8-NOX, 4 Oct 2026)
Read so far: c510-516 segmented whole (9,904 tiles, 120 clusters -> 108 owner piles); the stream aligner's lock-on onto Dupuy 221R-226R is a basin with one common key (N8-NOX step 1 PASS, S 0.601 vs nulls 0.273/0.384); 0 open leaves decoded
- Basin key not yet tied to Tomokiyo's key: N8-NOX step 2 FAIL as registered (6/11 piles agree, permutation p99 passed, non-locking null degenerate at 1-3 piles) - blocker: not-attempted; next: re-registered count-based step 2 with a shuffled-Dupuy arm, or a wider c262 bridge under the owner's labels, ~$1
- Decode of a leaf not aligned to Dupuy with the basin consensus key not run - blocker: not-attempted; next: after the key is tied to key.tsv, decode c511 or c262 with the consensus key and judge it, ~$2
- c510-516 alignment by line reads (instrument 2) not run - blocker: not-attempted; next: same pipeline with its control first, ~$2
- c511 not transcribed by readers - blocker: not-attempted; next: two passes against settled labels, ~$5
- Date-only Dupuy matches (c330, c358-361, c409-410, c245/c464, c472-473) not text-checked - blocker: not-attempted; next: one native look per pair, ~$1
- "Relation d'une bataille" c231 has no clear copy found - blocker: not-attempted; next: grep Charrière III and the Lepanto relations, ~$1

## Escalation (N8-NOX, 4 Oct 2026)
- [x] siblings: the duplicata/original pairs in this volume found (letters_coverage.tsv)
- [x] basin test: the locked-on runs share one key (N8-NOX, pre-registered, PASS vs non-locking and shuffled-Dupuy nulls)
- [ ] key tie: basin consensus vs key.tsv; planned step: re-registered count-based step 2 or a wider c262 bridge
- [x] clear-pages: Dupuy 521 221R-226R transcribed and aligned whole; the alignment locks on in a basin with a common key
- [x] known-keys: Tomokiyo's published key applied to c262; reconciled text and one blind pass beat every null, gate pass failed
- [x] print: Charrière III pp.520-524 and pp.551-558 read
- [n/a] key-rebuild: a published key exists
- [x] image-check: c262 re-cut; c510-516 native line bands; owner sort of the atlas piles
- [x] retry: pre-registered confirmation of k014->k077 (NOX-CONFIRM, FAIL as specific) and basin test (N8-NOX, PASS)
Verdict: keep going: 6 internal gaps; cheapest next: re-registered count-based key tie of the basin consensus to key.tsv, ~$1

`python3 tools/gaps_check.py fr16142-noailles-constantinople-1571` (N8-NOX):
```
OK keep-going fr16142-noailles-constantinople-1571: keep going: 4 internal gap(s), 1 step(s) untried
gaps_check: 1 checked: 0 parked, 1 keep-going, 0 FAIL, 0 skipped
```

## N8-NOX2 count-based key tie (4 Oct 2026)
LANE-NEAR8 worker N8-NOX2 (account 2), 17:08-17:2x UTC by `date -u`; brief `.claude/briefs/runs/2026-10-04-ytbiz-near8-wave3.md`.
Pre-registered in `sorter/owner-sort-2026-10-04/aln/PREREG-KEYTIE.md` (commit 4c5d72d9, 17:10 UTC, before any key-tie statistic). Script
`aln/keytie.py` (reads N8-NOX's `results/basin_keys.json` unchanged, no re-learning; asserts the 17-pile bridge equals N8-NOX's); numbers
`aln/results/keytie_summary.json`; `python3 aln/keytie.py check` exits 0. Disk only: requests 0, subagents 0. key.tsv unchanged.

**Re-registration.** N8-NOX's step 2 used a >= 4-of-6 majority; the non-locking control reached a majority on 0-6 of 17 piles, so it
could not fail differently. Here every run votes for its letter weighted by its train-token count on the pile (runs whose own merge
touches the pile abstain), so the consensus exists on every pile with any vote, for the target and every control alike.
Statistic H = number of the 17 c262-bridge piles where the consensus letter is in the pile's provisional (Tomokiyo-key) letter set.
Control (b) degeneracy check, registered in advance: passed (924 subsets take 6 distinct H values 1-6; 0% of subsets leave more than
3 piles without a vote), so (b) can differ from the target on H.

| run set | H (of 17) |
|---|---|
| **locked six, count-based consensus** | **7** (k022 e, k053 s, k060 l, k073 t, k080 r, k102 d, k115 a; 16 piles carry a consensus) |
| (a) permutation of letter sets across piles, 10000 | mean 1.36, p99 4, max 6 |
| (b) non-locking 6-subsets, 924 | mean 3.41, p99 5, max 6 |
| (c) shuffled Dupuy, six locked merges, 10 seeds | 3 1 2 1 5 2 2 1 3 1, max 5 |
| secondary: locked six + target k014->k077 | 7 |
| secondary: each locked run alone | 8, 8, 5, 6, 6, 8 |

**Verdict: PASS as registered** (7 > 4, 7 > 5, 7 > 5). In plain words: the key the locked runs share agrees with Tomokiyo's published
key, through the c262 bridge, on 7 of 17 piles, more than any shuffled-Dupuy run set, more than 99% of non-locking run sets and of
letter-set permutations. Margins are small (2 piles over (b) and (c) gates; one non-locking subset and one permutation reach 6), and
the agreeing piles are mostly high-frequency letters (a, e, s, t, r, d, l), so this is a modest tie, not a per-sign confirmation.
The consensus does not beat the best single locked runs (8). Disagreements: k021 d (prov. x), k045 x (f), k071 m (e), k086 r (y),
k117 e (n), k041 m / k101 p / k112 l (prov. e or o), k072 s (i); k076 (prov. l) has no vote. Every value stays grade M (the bridge
labels are Tomokiyo's key applied to c262, grade M); no reading is claimed; key.tsv unchanged.

One-line suggestion (not done): decode a leaf not aligned to Dupuy (c511 or c262) with the basin consensus key and judge it against
its own shuffled control; or widen the bridge (c262 tiles under the owner's labels) so more than 17 piles carry a key.tsv value, ~$1-2.

## Remaining gaps (N8-NOX2, 4 Oct 2026)
Read so far: c510-516 segmented whole (9,904 tiles, 120 clusters -> 108 owner piles); the stream aligner's lock-on onto Dupuy 221R-226R is a basin with one common key (N8-NOX step 1 PASS, S 0.601 vs nulls 0.273/0.384) that agrees with Tomokiyo's key on 7 of 17 bridge piles (N8-NOX2 PASS vs nulls 4/5/5); 0 open leaves decoded
- Decode of a leaf not aligned to Dupuy with the basin consensus key not run - blocker: not-attempted; next: decode c511 or c262 with the consensus key and judge it against a shuffled control, ~$2
- Bridge from atlas piles to key.tsv covers only 17 piles - blocker: not-attempted; next: place c262 tiles under the owner's labels so more piles carry a key.tsv value, ~$1
- c510-516 alignment by line reads (instrument 2) not run - blocker: not-attempted; next: same pipeline with its control first, ~$2
- c511 not transcribed by readers - blocker: not-attempted; next: two passes against settled labels, ~$5
- Date-only Dupuy matches (c330, c358-361, c409-410, c245/c464, c472-473) not text-checked - blocker: not-attempted; next: one native look per pair, ~$1
- "Relation d'une bataille" c231 has no clear copy found - blocker: not-attempted; next: grep Charrière III and the Lepanto relations, ~$1

## Escalation (N8-NOX2, 4 Oct 2026)
- [x] siblings: the duplicata/original pairs in this volume found (letters_coverage.tsv)
- [x] basin test: the locked-on runs share one key (N8-NOX, pre-registered, PASS vs non-locking and shuffled-Dupuy nulls)
- [x] key tie: basin count-based consensus vs key.tsv via the c262 bridge (N8-NOX2, pre-registered, PASS 7/17 vs 4/5/5)
- [ ] decode: a leaf not aligned to Dupuy with the consensus key; planned step: c511 or c262 decode + judge with its shuffled control
- [x] clear-pages: Dupuy 521 221R-226R transcribed and aligned whole; the alignment locks on in a basin with a common key
- [x] known-keys: Tomokiyo's published key applied to c262; reconciled text and one blind pass beat every null, gate pass failed
- [x] print: Charrière III pp.520-524 and pp.551-558 read
- [n/a] key-rebuild: a published key exists
- [x] image-check: c262 re-cut; c510-516 native line bands; owner sort of the atlas piles
- [x] retry: NOX-CONFIRM (FAIL as specific), N8-NOX basin (PASS), N8-NOX2 key tie re-registered with a non-degenerate control (PASS)
Verdict: keep going: 6 internal gaps; cheapest next: decode a leaf not aligned to Dupuy with the basin consensus key, ~$2

`python3 tools/gaps_check.py fr16142-noailles-constantinople-1571` (N8-NOX2):
```
OK keep-going fr16142-noailles-constantinople-1571: keep going: 4 internal gap(s), 1 step(s) untried
gaps_check: 1 checked: 0 parked, 1 keep-going, 0 FAIL, 0 skipped
```

## RUN6-NOXDEC (5 Oct 2026)
LANE-RUN6 worker RUN6-NOXDEC (account 1), 04:45-04:49 UTC by `date -u`; brief `.claude/briefs/runs/2026-10-05-acct1-run6-wave1.md`.
Pre-registered `sorter/owner-sort-2026-10-04/aln/PREREG-DECODE.md` (commit 6de3a59e, 04:47 UTC, before any statistic). Script
`aln/decode262.py` (imports keytie.consensus unchanged; basin_keys.json unchanged, no re-learning); numbers
`aln/results/decode262_summary.json`; `python3 aln/decode262.py check` exits 0. Disk only: requests 0, subagents 0. key.tsv unchanged.
Leaf: c262 (403 atlas tiles -> 64 piles after the owner's 18 merges, all keyed). Not c511: it is a TRAIN leaf of the Dupuy alignment.
Statistic R = test0.py's difflib ratio, decode vs c262 period gloss (315 letters).

| run | R |
|---|---|
| **basin consensus (six L, count-based)** | **0.1838** |
| (a) shuffled key, 1000 | mean 0.152, p99 0.2479 |
| (b) letter-order shuffle of the decode, 1000 | mean 0.1607, p99 0.2563 |
| (c) shuffled Dupuy, 10 seeds | max 0.2033 |
| (d) non-locking 6-subsets, 924 | mean 0.1594, p99 0.2528 |
| reported: single L runs | 0.147-0.242 |
| reported: c262 tiles under the bridge's provisional (Tomokiyo-key) labels | 0.2199 |
| quoted: NX-RECUT reconciled reader transcription (different stream) | 0.4548 |

**Verdict: FAIL as registered** (0.1838 under every gate; inside the null bodies). Not a negative on the basin key: the reported
ceiling -- Tomokiyo's published key reaching the same atlas tiles through the bridge labels -- also scores 0.2199, under every p99,
while the same key on a reader transcription scores 0.4548. So at the atlas tiling (1.05 tiles/sign, k-means piles) R against the
gloss has no power on this block: the tile stream, not the key, is the limit (rule 3: a control that cannot read licenses no negative).
Rule 3 third-attempt clause: do not re-run this tile-stream decode with another key variant; the next instrument is a reader
transcription of c262 under settled labels (owner piles), decoded with the basin key mapped to those labels. All tokens grade M.

## Remaining gaps (RUN6-NOXDEC, 5 Oct 2026)
Read so far: c510-516 segmented whole (9,904 tiles, 120 clusters -> 108 owner piles); the stream aligner's lock-on onto Dupuy 221R-226R is a basin with one common key (N8-NOX PASS) that agrees with Tomokiyo's key on 7 of 17 bridge piles (N8-NOX2 PASS); c262 atlas-tile decode with that key FAILs vs its gloss, but the published-key ceiling on the same tiles fails too (RUN6-NOXDEC, non-test); 0 open leaves decoded
- Decode of c262 with the basin key on a reader transcription (not atlas tiles) not run - blocker: not-attempted; next: map basin piles to the reconciled c262 signs (c262_tile_alignment.tsv) and score R with the same four nulls, ~$1
- Bridge from atlas piles to key.tsv covers only 17 piles - blocker: not-attempted; next: place c262 tiles under the owner's labels so more piles carry a key.tsv value, ~$1
- c510-516 alignment by line reads (instrument 2) not run - blocker: not-attempted; next: same pipeline with its control first, ~$2
- c511 not transcribed by readers - blocker: not-attempted; next: two passes against settled labels, ~$5
- Date-only Dupuy matches (c330, c358-361, c409-410, c245/c464, c472-473) not text-checked - blocker: not-attempted; next: one native look per pair, ~$1
- "Relation d'une bataille" c231 has no clear copy found - blocker: not-attempted; next: grep Charrière III and the Lepanto relations, ~$1

## Escalation (RUN6-NOXDEC, 5 Oct 2026)
- [x] siblings: the duplicata/original pairs in this volume found (letters_coverage.tsv)
- [x] basin test: the locked-on runs share one key (N8-NOX, pre-registered, PASS vs non-locking and shuffled-Dupuy nulls)
- [x] key tie: basin count-based consensus vs key.tsv via the c262 bridge (N8-NOX2, pre-registered, PASS 7/17 vs 4/5/5)
- [retired] decode on atlas tiles: c262 tile-stream decode vs gloss (RUN6-NOXDEC FAIL; published-key ceiling 0.2199 also under nulls), instrument atlas-tile stream + test0 ratio
- [ ] decode on a reader transcription: basin key mapped onto the reconciled c262 signs; planned step: score R with the four RUN6-NOXDEC nulls
- [x] clear-pages: Dupuy 521 221R-226R transcribed and aligned whole; the alignment locks on in a basin with a common key
- [x] known-keys: Tomokiyo's published key applied to c262; reconciled text and one blind pass beat every null, gate pass failed
- [x] print: Charrière III pp.520-524 and pp.551-558 read
- [n/a] key-rebuild: a published key exists
- [x] image-check: c262 re-cut; c510-516 native line bands; owner sort of the atlas piles
- [x] retry: NOX-CONFIRM (FAIL as specific), N8-NOX basin (PASS), N8-NOX2 key tie (PASS), RUN6-NOXDEC tile decode (FAIL, non-test)
Verdict: keep going: 6 internal gaps; cheapest next: basin key on the reconciled c262 reader transcription, ~$1

## RUN6-NOXREAD (5 Oct 2026)
LANE-RUN6 worker RUN6-NOXREAD (account 1), 05:03-05:08 UTC by `date -u`; brief `.claude/briefs/runs/2026-10-05-acct1-run6-wave2.md`.
Pre-registered `sorter/owner-sort-2026-10-04/aln/PREREG-NOXREAD.md` (commit 1f39b1f1, 05:04 UTC, before any statistic): RUN6-NOXDEC's
statistic, four nulls and gate unchanged, only the stream changed. Script `aln/noxread.py` (imports decode262/keytie unchanged);
numbers `aln/results/noxread_summary.json`; `python3 aln/noxread.py check` exits 0. Disk only: requests 0, subagents 0. key.tsv unchanged.
Stream: NX-RECUT's reconciled c262 reader signs (`witness/c262rc_recon.tsv`, 384 signs, 41 labels). Map: each label takes its
majority owner pile in RUN2-NXATL's tile alignment (`run2/nxatl/c262_tile_alignment.tsv`, no gloss in it); 41/41 labels mapped onto
30 piles; a sign reads as the basin consensus letter of its pile.

| run | R vs c262 gloss (315 letters) |
|---|---|
| **basin consensus (six L) on the reader signs** | **0.3090** |
| (a) shuffled key, 1000 | mean 0.1464, p99 0.2404 |
| (b) letter-order shuffle, 1000 | mean 0.1547, p99 0.2518 |
| (c) shuffled Dupuy, 10 seeds | max 0.2003 |
| (d) non-locking 6-subsets, 924 | mean 0.1554, **p99 0.2833**, max 0.3090 (one subset ties) |
| reported: single L runs | 0.127-0.312 |
| positive reference: Tomokiyo's key on the same stream (recomputed) | 0.4548 |
| for comparison: same basin key on atlas tiles (RUN6-NOXDEC) | 0.1838 |

**Verdict: PASS as registered** (R > every gate). Thin on (d): 0.309 vs p99 0.2833, and the best of 924 non-locking subsets
reaches 0.309 exactly, so the margin over keys the aligner did not lock with is about one subset in a thousand, not a wide gap.
What it licenses, and only this: the key learned against Dupuy on c510-516, mapped to the reader signs, reads c262 toward its period
gloss beyond the four nulls; it sits under the published key on the same stream (0.309 vs 0.4548). Reading what differs: on this
stream the basin letter equals the label's own Tomokiyo letter for 12 of 34 letter labels (a1 a2 c1 d1 e3 l2 m2 p1 p2 r1 s2 t2),
independently of key.tsv (the basin never saw it); the most frequent sign o1/e2 (66 of 384) reads 'm' under the basin key, which
alone costs much of the gap to Tomokiyo. Conditional on one reconciler's labels, RUN2-NXATL's unchecked alignment and the owner's
merges. All tokens M (the gloss is the period decipherment; C would need a per-token alignment, not in this brief).

## Remaining gaps (RUN6-NOXREAD, 5 Oct 2026)
Read so far: c510-516 segmented whole (9,904 tiles, 120 clusters -> 108 owner piles); the stream aligner's lock-on onto Dupuy 221R-226R is a basin with one common key (N8-NOX PASS) that agrees with Tomokiyo's key on 7 of 17 bridge piles (N8-NOX2 PASS); that key mapped onto the reconciled c262 reader signs reads toward the gloss beyond four nulls (RUN6-NOXREAD PASS, thin vs non-locking keys; atlas-tile decode a non-test); 0 open leaves decoded
- Per-token alignment of the c262 basin decode to the gloss (would move tokens off M) not run - blocker: not-attempted; next: tools/interlinear_align.py on decode vs gloss with a shuffled-gloss control, ~$1
- Bridge from atlas piles to key.tsv covers only 17 piles - blocker: not-attempted; next: place c262 tiles under the owner's labels so more piles carry a key.tsv value, ~$1
- c510-516 alignment by line reads (instrument 2) not run - blocker: not-attempted; next: same pipeline with its control first, ~$2
- c511 not transcribed by readers - blocker: not-attempted; next: two passes against settled labels, ~$5
- Date-only Dupuy matches (c330, c358-361, c409-410, c245/c464, c472-473) not text-checked - blocker: not-attempted; next: one native look per pair, ~$1
- "Relation d'une bataille" c231 has no clear copy found - blocker: not-attempted; next: grep Charrière III and the Lepanto relations, ~$1

## Escalation (RUN6-NOXREAD, 5 Oct 2026)
- [x] siblings: the duplicata/original pairs in this volume found (letters_coverage.tsv)
- [x] basin test: the locked-on runs share one key (N8-NOX, pre-registered, PASS vs non-locking and shuffled-Dupuy nulls)
- [x] key tie: basin count-based consensus vs key.tsv via the c262 bridge (N8-NOX2, pre-registered, PASS 7/17 vs 4/5/5)
- [retired] decode on atlas tiles: c262 tile-stream decode vs gloss (RUN6-NOXDEC FAIL; published-key ceiling 0.2199 also under nulls), instrument atlas-tile stream + test0 ratio
- [x] decode on a reader transcription: basin key mapped onto the reconciled c262 signs (RUN6-NOXREAD, pre-registered, PASS 0.309 vs p99 0.2404/0.2518/max 0.2003/0.2833)
- [x] clear-pages: Dupuy 521 221R-226R transcribed and aligned whole; the alignment locks on in a basin with a common key
- [x] known-keys: Tomokiyo's published key applied to c262; reconciled text and one blind pass beat every null, gate pass failed
- [x] print: Charrière III pp.520-524 and pp.551-558 read
- [n/a] key-rebuild: a published key exists
- [x] image-check: c262 re-cut; c510-516 native line bands; owner sort of the atlas piles
- [x] retry: NOX-CONFIRM (FAIL as specific), N8-NOX basin (PASS), N8-NOX2 key tie (PASS), RUN6-NOXDEC tile decode (FAIL, non-test), RUN6-NOXREAD reader-sign decode (PASS, thin)
Verdict: keep going: 6 internal gaps; cheapest next: per-token alignment of the basin decode to the c262 gloss, ~$1

## RUN6-NOXALIGN (5 Oct 2026)
LANE-RUN6 worker RUN6-NOXALIGN (account 1), 05:21-05:27 UTC by `date -u`; brief `.claude/briefs/runs/2026-10-05-acct1-run6-wave3.md`.
Pre-registered `sorter/owner-sort-2026-10-04/aln/PREREG-NOXALIGN.md` (commit a5c1277d, before any statistic). Script `aln/noxalign.py`;
numbers `aln/results/noxalign_summary.json`; `python3 aln/noxalign.py check` exits 0. Disk only: requests 0, subagents 0. key.tsv unchanged.
Method: leave-one-label-out masked alignment of RUN6-NOXREAD's basin decode (384 reader signs, 41 labels) to the c262 gloss; a masked
sign is recovered only inside an equal-length difflib 'replace' gap <= 3 between anchors; settled = >=3 recovered, plurality >=2 and >=50%.
(interlinear_align.py not used: its hard-EM would re-key the stream.)

| run | S = labels settled to own basin letter |
|---|---|
| **basin decode, masked per label** | **0 / 41** |
| (g) shuffled gloss, 200 | mean 0, p99 0, max 0 |
| (k) shuffled basin key, 200 | mean 0, p99 0, max 0 |
| reported: labels settled to Tomokiyo letter, basin anchors | 1 (i2) |
| reference: Tomokiyo-anchored, letter labels settled to Tomokiyo letter | 8 of 34 (12 settled at all) |

**Verdict: FAIL as registered, and a non-test**: S ties both nulls at 0 (the bMAT2/bSZL tie shape, rule 3) -- at R 0.309 the basin
decode has too few anchors for short-gap recovery; only 4 labels recover >=3 positions at all. Not a negative on the basin key.
Basin vs Tomokiyo disagreements (22 letter labels: a3 e1 f2 g2 h1 i2 i3 l1 m1 m3 n1 n2 o1/e2 o2 q1 r2 s1 u1 u5 x1 y1 z1): the gloss settles
one, i2 -> 'i' (Tomokiyo; recovered i,i,i,p; basin 's'); o1/e2 (basin 'm', Tomokiyo 'e') settles to 'o' on 3 recovered (e,o,o) -- neither,
3 positions only; l1, n1, u1 each recover 1 position, all Tomokiyo's letter (l, n, u), below the settle rule; the other 17 recover 0.
All tokens M (FAIL). Conditional on one reconciler's labels, RUN2-NXATL's unchecked alignment and the owner's merges.

## Remaining gaps (RUN6-NOXALIGN, 5 Oct 2026)
Read so far: c510-516 segmented whole (9,904 tiles, 120 clusters -> 108 owner piles); the stream aligner's lock-on onto Dupuy 221R-226R is a basin with one common key (N8-NOX PASS) that agrees with Tomokiyo's key on 7 of 17 bridge piles (N8-NOX2 PASS); that key mapped onto the reconciled c262 reader signs reads toward the gloss beyond four nulls (RUN6-NOXREAD PASS, thin); per-label masked alignment of that decode to the gloss a non-test (RUN6-NOXALIGN, S 0 = nulls 0); 0 open leaves decoded
- Per-token alignment with denser anchors (basin decode too sparse at R 0.309) not run - blocker: not-attempted; next: same masked procedure anchored on a hybrid decode (Tomokiyo letters on the 12 agreeing labels, basin elsewhere) or with gap <= 5, pre-registered with nulls g/k, ~$1
- Bridge from atlas piles to key.tsv covers only 17 piles - blocker: not-attempted; next: place c262 tiles under the owner's labels so more piles carry a key.tsv value, ~$1
- c510-516 alignment by line reads (instrument 2) not run - blocker: not-attempted; next: same pipeline with its control first, ~$2
- c511 not transcribed by readers - blocker: not-attempted; next: two passes against settled labels, ~$5
- Date-only Dupuy matches (c330, c358-361, c409-410, c245/c464, c472-473) not text-checked - blocker: not-attempted; next: one native look per pair, ~$1
- "Relation d'une bataille" c231 has no clear copy found - blocker: not-attempted; next: grep Charrière III and the Lepanto relations, ~$1

## Escalation (RUN6-NOXALIGN, 5 Oct 2026)
- [x] siblings: the duplicata/original pairs in this volume found (letters_coverage.tsv)
- [x] basin test: the locked-on runs share one key (N8-NOX, pre-registered, PASS vs non-locking and shuffled-Dupuy nulls)
- [x] key tie: basin count-based consensus vs key.tsv via the c262 bridge (N8-NOX2, pre-registered, PASS 7/17 vs 4/5/5)
- [retired] decode on atlas tiles: c262 tile-stream decode vs gloss (RUN6-NOXDEC FAIL; published-key ceiling 0.2199 also under nulls), instrument atlas-tile stream + test0 ratio
- [x] decode on a reader transcription: basin key mapped onto the reconciled c262 signs (RUN6-NOXREAD, pre-registered, PASS 0.309 vs p99 0.2404/0.2518/max 0.2003/0.2833)
- [ ] per-token alignment: masked per-label alignment on basin anchors a non-test (RUN6-NOXALIGN, S 0 = nulls 0); denser-anchor variant untried
- [x] clear-pages: Dupuy 521 221R-226R transcribed and aligned whole; the alignment locks on in a basin with a common key
- [x] known-keys: Tomokiyo's published key applied to c262; reconciled text and one blind pass beat every null, gate pass failed
- [x] print: Charrière III pp.520-524 and pp.551-558 read
- [n/a] key-rebuild: a published key exists
- [x] image-check: c262 re-cut; c510-516 native line bands; owner sort of the atlas piles
- [x] retry: NOX-CONFIRM (FAIL as specific), N8-NOX basin (PASS), N8-NOX2 key tie (PASS), RUN6-NOXDEC tile decode (FAIL, non-test), RUN6-NOXREAD reader-sign decode (PASS, thin), RUN6-NOXALIGN masked alignment (FAIL, non-test)
Verdict: keep going: 6 internal gaps; cheapest next: denser-anchor masked alignment of the c262 decode to the gloss, ~$1

## RUN6-NOXDUP (5 Oct 2026, 05:38-05:5x UTC by date -u, account-1 worker)
Job: text-check the five date-only Dupuy 521 matches of `dupuy521_align.tsv`; one native look per pair, no decoding. Images fetched once
to scratch at `full/1500,` (fr.16142 `btv1b9060927q` canvases 330, 358, 409, 245, 464, 472; Dupuy `btv1b100339270` canvases 64, 65, 71,
76, 121, 122, 123, 124; 14 requests gallica.bnf.fr, 2 s apart, 0 errors). Reads are by eye by this worker (clear text only; no cipher read).
Re-fetch: `curl -A "Mozilla/5.0" "https://gallica.bnf.fr/iiif/ark:/12148/<ark>/f<canvas>/full/1500,/0/default.jpg"`.

| pair | fr.16142 leaf (heading, opening / clear words) | Dupuy 521 | result |
|---|---|---|---|
| c330 | "8 Juillet 1572 Pera, De l'Evesque d'Acqs a la Reyne", "Madame partant presentement le Seigneur de Malatesta avec le sr de Germiny...", 2nd para "Madame voz Mtés entendront du sr de Germiny comme en fin l'Empereur a esté conseillé de payer le tribut ... trente mil ducats et vingt grands vaisseaux d'or ou d'argent doré portez par xx hommes"; clear tail "Le Roy d'Espagne ne fait par monstre general des presents..." | 64R-65L (heading "La Royne"; ends "Pera lez Constantinople le huictiesme Juillet 1572, Noailles Evesque d'Acqs"): "Madame vos Majestés entendront du sr de Bevigny comme en fin l'Empereur a esté conseillé d'envoyer le present pas ca que ceulx cy appellent tribut ... trente mil ducats et vingt cinq grands vaisseaux d'or ou d'argent doré portez par xx hommes ... Le Roy d'Espagne ne fait par monstre general ..." | **match** (text, same date, same length ~1 leaf; Dupuy spells the copyist's "Bevigny" for Germiny, "vingt cinq" vs leaf "vingt"; Dupuy also carries the deciphered passages in clear) |
| c358-361 | heading "Copia de la despesche du 8me d'aoust avec ung postscripta du xviii et ung autre du xx", "Sire Le dernier jour du mois passé je vous feis une depesche accusant la reception de celle qu'il avoit pleu a Vre Mté me faire du ..me de May dont le duplicata sera avec la presente, par laquelle je vous diray Sire que des le lendemain qui fut le premier de ce moys je fus veoir le Bassa..." | 71R (heading "Au Roy"): "Sire le dernier du moys passé je vous fis une depesche accusant la reception de celle qu'il avoit pleu a Vostre Majesté me faire du vingtiesme de May dont le duplicata sera avec la presente par laquelle je vous diray que des le lendemain qui fut le premier de ce moys je fus voir le Bassa auquel je fis entendre ce que vous commandiez a quoy j'adjoutay et diminuay selon qu'il me semblait estre necessaire pour vostre service..." (previous letter ends "derniers Juillet 1572") | **match** (opening ~60 words, same wording; the leaf's heading date "8 Aoust" is the despatch date, Dupuy dates the piece by its Aug 18 PS) |
| c409-410 | "6 Septembre 1572 Pera, De l'Evesque d'Acqs au Roy", "Sire, Le (dernier?) du passé et ...de cestuy j'ay bien au long escript a vre Majesté et a Monseigneur ..." then cipher; clear mid-text "la cause principalle qui plus m'a sollicité est ce que Vre Majesté m'a escript du ... May" | 76R-77L (heading "Autre Lre au Roy du sixiesme Septembre 1572"): "Sire j'ay escript a Vostre Majesté et a Monseigneur la resolution que j'avois eue du Bassa sur le fait d'Auger ... je me hasté de conclure ... Il y a bien d'apparence qu'elle ... la cause principalle qui plus m'a solicité est que Vostre Majesté m'a escript du vi? may ..." | **match, opening abridged** (mid-letter clear phrase verbatim; Dupuy's first sentence is a digest of the leaf's opening, not a word-for-word copy) |
| c245-246 + c464 | both leaves headed "8 Mars 1573 Pera, De l'Evesque d'Acqs au Roy" (c245's year reads 1572 at 1500 px, scribal slip; c464 reads 1573), identical clear text: "Sire quant Vre Majesté aura entendu que la paix des Venitiens a esté conclue huict jours apres mon arrivée icy elle congnoistra que mon retour estoit necessaire par deça ... Voila Sire comment lesd. Venitiens vous en doibvent ung bon grand mercy. Quant aux affaires de Poulongne j'escris a Monseigneur ..." then "Sire arrivé ... Pera lez Constantinople ce vj? jour de Mars 1573", then a cipher block with clear words ("que luy porta le sr de la Tuquie nadmenne de sorte que sans Cypren commandement que le sr de Germiny m'apporta de vre Mté"), ending cipher + "Votre plus humble ... Noailles" | 121R-122L ("Au Roy"): "Sire quand Vostre Majesté aura entendu que la paix des Venitiens a esté conclue huict jours apres mon arrivée icy elle congnoistra que mon retour estoit necessaire de-ça..." ; 122L runs on with the deciphered middle ("...par le dessous que luy porta le sr de Triquerie nadmanne de sorte que sans ... commandement que le sr de Bevigny m'apporta de Vostre Majesté") | **match, both copies** (c245 and c464 carry the same clear text; the two leaves are one letter in two copies, the pair premise holds). Note: Dupuy here carries the decipherment of a cipher block of this letter in clear (a period reading by Dupuy's copyist, not ours; not used as H/C here) |
| c472-473 | "8 Mars 1573 Pera, De l'Evesque d'Acqs a la Reyne": "Madame oultre le duplicata de la depesche que j'envoyay avant hier a vre Mté et de quelle pourra voir par celle que presentement je fais au Roy et a Monseigneur je n'ay voulu faillir tout fois d'escrire ce petit mot ..."; "Postscripta du xijme Mars: Madame j'ay presenté le sr de Germiny et luy ay fait baiser la main du grand seigneur ..." ; clear mid-PS "de quelle vehemence et audace" | 123R only: "Post Scripta a la Royne du douziesme de Mars 1573. Madame j'espere que Vostre Majesté sera quelque jour amplement informée de quelle vehemence et audace j'ay proposé le fait de Pologne ..." (a short PS); the 8 March Queen body is **not** on 122R-124L: 122-123L carry the King's letter and its signature, 124L opens Anjou ("Monseigneur") | **partial**: shared phrase with the PS ("de quelle vehemence et audace", Pologne) only; the c472 opening and the "j'ay presenté le sr de Germiny" paragraph were not found in Dupuy 122-124. Dupuy abridges or omits this Queen letter's body. Not a no-match (same date, same addressee, shared phrase) and not a text match |

Caveat: the quoted French is this worker's eye-read of 1500 px images, normalised in spelling and with `...` for elisions; it is for matching, not a transcription (grade M at best).
Counts: 4 pairs text-confirmed (c330, c358, c409, c245/c464 = 5 leaf groups), 1 partial (c472-473), 0 no-match. Dupuy 521 therefore
carries the clear text of at least these letters; for c245/c464 and c330 it also carries deciphered passages in clear. Length:
Dupuy and leaf agree to within one opening for c330, c358, c409; Dupuy is shorter than the leaf cipher+clear for c472.
Where not found: no line-by-line comparison (opening, date line, one mid-letter phrase per pair only); no cipher-leaf signs read; c472's
8 March Queen letter body not located in Dupuy. No decoding, no key change, no grades; nothing here is H/C/S.
Cost: no subagent calls; 14 image reads by this worker (~USD 0.9, see the lane ledger).

## Remaining gaps (RUN6-NOXDUP, 5 Oct 2026)
Read so far: c510-516 segmented whole (9,904 tiles, 120 clusters -> 108 owner piles); the stream aligner's lock-on onto Dupuy 221R-226R is a basin with one common key (N8-NOX PASS) that agrees with Tomokiyo's key on 7 of 17 bridge piles (N8-NOX2 PASS); that key mapped onto the reconciled c262 reader signs reads toward the gloss beyond four nulls (RUN6-NOXREAD PASS, thin); per-label masked alignment of that decode to the gloss a non-test (RUN6-NOXALIGN, S 0 = nulls 0); 0 open leaves decoded
- Per-token alignment with denser anchors (basin decode too sparse at R 0.309) not run - blocker: not-attempted; next: same masked procedure anchored on a hybrid decode (Tomokiyo letters on the 12 agreeing labels, basin elsewhere) or with gap <= 5, pre-registered with nulls g/k, ~$1
- Bridge from atlas piles to key.tsv covers only 17 piles - blocker: not-attempted; next: place c262 tiles under the owner's labels so more piles carry a key.tsv value, ~$1
- c510-516 alignment by line reads (instrument 2) not run - blocker: not-attempted; next: same pipeline with its control first, ~$2
- c511 not transcribed by readers - blocker: not-attempted; next: two passes against settled labels, ~$5
- Date-only Dupuy matches text-checked (RUN6-NOXDUP): c330, c358, c409, c245/c464 confirmed, c472-473 partial (12 Mar PS only; 8 Mar Queen body not in Dupuy 122-124) - blocker: not-attempted; next: if the c472 body matters, check Dupuy 133L-134 (Queen letters of 21 Apr 1573 are unrelated; the 8 Mar Queen body may be abridged away), ~$0.3
- "Relation d'une bataille" c231 has no clear copy found - blocker: not-attempted; next: grep Charrière III and the Lepanto relations, ~$1

## Escalation (RUN6-NOXDUP, 5 Oct 2026)
- [x] siblings: the duplicata/original pairs in this volume found (letters_coverage.tsv)
- [x] basin test: the locked-on runs share one key (N8-NOX, pre-registered, PASS vs non-locking and shuffled-Dupuy nulls)
- [x] key tie: basin count-based consensus vs key.tsv via the c262 bridge (N8-NOX2, pre-registered, PASS 7/17 vs 4/5/5)
- [retired] decode on atlas tiles: c262 tile-stream decode vs gloss (RUN6-NOXDEC FAIL; published-key ceiling 0.2199 also under nulls), instrument atlas-tile stream + test0 ratio
- [x] decode on a reader transcription: basin key mapped onto the reconciled c262 signs (RUN6-NOXREAD, pre-registered, PASS 0.309 vs p99 0.2404/0.2518/max 0.2003/0.2833)
- [ ] per-token alignment: masked per-label alignment on basin anchors a non-test (RUN6-NOXALIGN, S 0 = nulls 0); denser-anchor variant untried
- [x] clear-pages: Dupuy 521 221R-226R transcribed and aligned whole; the alignment locks on in a basin with a common key
- [x] known-keys: Tomokiyo's published key applied to c262; reconciled text and one blind pass beat every null, gate pass failed
- [x] print: Charrière III pp.520-524 and pp.551-558 read
- [n/a] key-rebuild: a published key exists
- [x] image-check: c262 re-cut; c510-516 native line bands; owner sort of the atlas piles
- [x] retry: NOX-CONFIRM (FAIL as specific), N8-NOX basin (PASS), N8-NOX2 key tie (PASS), RUN6-NOXDEC tile decode (FAIL, non-test), RUN6-NOXREAD reader-sign decode (PASS, thin), RUN6-NOXALIGN masked alignment (FAIL, non-test)
Verdict: keep going: 6 internal gaps; cheapest next: denser-anchor masked alignment of the c262 decode to the gloss, ~$1

## Correction note (VER1-NOX verifier, 5 Oct 2026)
AUDIT.md "AUDIT 1 (VER1-NOX)": c262 and c510-516 both N0, D0, key published (Tomokiyo) / basin key ours. Two corrections to text
above, not rewritten in place: (1) RUN1-NX's "on leaves no reader has seen before" reads "on leaves no reader in this repository had
transcribed before" (rule 10); (2) the c262 passage (gloss.tsv L01-L13) is printed in Charrière III p.258, in the evêque d'Acqs's
letter "Constantinople, 25 avril 1572" (from p.252), and differs from gloss.tsv at L01 "bruslent" (print "veullent"), L04 "le bestial"
("l'antienne liberté"), L06 "la faim se trouva" ("la farce se jouera"), L08 "sendormir de ca" ("s'endorme de deçà"). One-line
suggestion (not done): re-read the c262 gloss against Charrière III p.258 before any further c262 gate.

## DEF1-NOXG: c262 gloss re-read against the leaf and Charrière III p.258 (5 Oct 2026, 20:46-21:0x UTC by date -u, account-1 worker)
Brief: `.claude/briefs/runs/2026-10-05-account1-default-2039-jobs.md` DEF1-NOXG (LANE DEFAULT-account-1-20261005-2039). Follows VER1-NOX's
correction note above. Requests: archive.org 1 (`ngociationsdel03charuoft_djvu.txt`), gallica 0 (native canvas 262 already on disk). Subagents 0.

**Print.** Charrière, *Négociations de la France dans le Levant* III, IA `ngociationsdel03charuoft`, printed p.258 (djvu text lines ~19310-19330;
letter of the évêque d'Acqs, Constantinople 25 April 1572, from p.252): "...voz huguenotz ou aultres veullent s'aller promener en Flandres par mer et
par terre, vous ne vouldrez empescher l'antienne liberté des gens de guerre de vostre nation. Pendant le temps que la farce se jouera du costé de
delà, il ne faudra pas qu'il s'endorme de deçà, car la partie est forte. Il est vray que j'ay trouvé ces gens-icy si comblés de bien et de mal,
c'est-à-dire de richesses et de volupté en toutes sortes, qu'il semble qu'on leur feroit plaisir..." (OCR normalised by eye).

**Crop step** (mandatory, run before any read; source = native canvas 262 on disk, 4981x7160):
```
python3 tools/iiif_lines.py --image ciphers/fr16142-noailles-constantinople-1571/images/src_ark_12148_btv1b9060927q_f262_full.jpg --region 470,2130,1000,800 --centres 56,150,246,340,436,530,630,726 --follow-slope 300 --slope-margin 15 --max-width 2400 --prefix c262gx --out ciphers/fr16142-noailles-constantinople-1571/images --debug
```
8 crops `images/c262gx_L01..L08.jpg` (1000 x 124-126 px, one gloss line each, overlay `c262gx_lines_debug.jpg` checked by eye). The old
`c262gl_*` crops (FT-D) are the same lines at 1060 px; the new ones are cut on the line slope.

**Read.** One read of each crop by this worker (no subagent). Not blind to the print: per the brief's order the Charrière text and VER1-NOX's
four differences were read first; blind to every decode (no decode was printed before gloss.tsv was rewritten). Normalised (rule 3, PX-BRODEC):
lower case, accents and apostrophes dropped, 'vre' -> vostre, 'vo9' -> vous.

| gloss line | leaf reads (DEF1-NOXG) | Charrière III p.258 | gloss.tsv had (FT-D) | decision |
|---|---|---|---|---|
| L01 w1 (VER1-NOX spot 1) | veullent | veullent | bruslent | corrected from leaf |
| L01 w3-5 | promener en fland[res] (end under an ink blot) | promener en flandres | promptement ou | corrected from leaf; "res" print-only, grade C at most, bracketed |
| L02 w6 | vous (v + o + -us mark) | vous | bien | corrected from leaf |
| L03 | vouldrez empescher lantienne | vouldrez empescher lantienne | bien d'ung empesche tant | corrected from leaf |
| L04 w1-2 (spot 2) | liberte des | (lantienne) liberte des | le bestial de | corrected from leaf ("l'antienne" ends L03, "liberté" opens L04) |
| L05 w1 | vre (= vostre) | vostre | bonne | corrected from leaf, abbreviation expanded |
| L06 w3-6 (spot 3) | farce se jouera | farce se jouera | faim se trouva | corrected from leaf |
| L08 w1-3 (spot 4) | sendormir de deca | quil sendorme de deca | sendormir de ca | leaf keeps gloss.tsv's "sendormir" against the print's "s'endorme"; leaf has no "qu'il"; "de deca" (second word d-e-c-a, the e unclear) replaces "de ca" |
| L07, L09-L13 | not re-cut (L07 matches print on the overview) | | unchanged | unchanged |

So of VER1-NOX's four differences, three (L01, L04, L06) were gloss.tsv misreads and the leaf agrees with the print; at L08 the leaf
differs from the print (infinitive "s'endormir", no "qu'il"): Charrière's text is not a letter-for-letter copy of this gloss, so the
print cannot stand in for the leaf here. Independent check from the cipher side (not used to decide any word): Tomokiyo's key on NX-RECUT's
reconciled c262 signs decodes line 1 as "ueupllentleallerpremcnerenflandre..." (witness/results_rc_recon_e.json), i.e. "veullent s'aller
promener en Flandre". Grades: gloss words H-source (period decipherment), reading M, as before; the bracketed "res" C (print only).

**Gate re-run (RUN6-NOXREAD, as registered in PREREG-NOXREAD.md, no new thresholds).** `aln/noxread.py score`, then `check` exits 0.

| | old gloss (315 letters) | corrected gloss (329 letters) |
|---|---|---|
| R, basin key on reader signs | 0.3090 | **0.3506** |
| (a) shuffled key p99 | 0.2404 | 0.2413 |
| (b) letter order p99 | 0.2518 | 0.2496 |
| (c) shuffled Dupuy max | 0.2003 | 0.2665 |
| (d) non-locking p99 / max | 0.2833 / 0.3090 | 0.2581 / 0.2749 |
| Tomokiyo key, same stream (reference) | 0.4548 | 0.5215 |
| verdict | PASS (thin on d) | **PASS** (R above all 924 non-locking subsets) |

Both the target R and the published-key reference rise together while the nulls stay put: what a corrected reference text looks like,
not threshold-shopping.

**Other scripts that read gloss.tsv, re-scored so their rule-7 checks stay green** (scripts unchanged; each `check` exits 0 after):
`scripts/test0.py` (all ten `witness/results_*.json`), `aln/decode262.py`, `aln/noxalign.py`. Old -> new, same registered rules:

| run | old | new | registered verdict old -> new |
|---|---|---|---|
| FT-D gate pass B (e = o), real / key-max / gloss-order-max (rank) | 0.2799 / 0.218 / 0.2988 (6) | 0.3250 / 0.2193 / 0.3144 (1) | FAIL -> **PASS** (witness/gate_passB.txt) |
| NX-RECUT gate pass D, e | 0.1928 / 0.2342 / 0.2590 | 0.3324 / 0.2757 / 0.2865 | |
| NX-RECUT gate pass D, o | 0.1736 / 0.2507 / 0.2231 | 0.2811 / 0.2541 / 0.2649 | FAIL -> **PASS**, thin on o (0.016 over gloss-order max) (witness/gate_recut.txt) |
| pass A e / o | 0.3177 / 0.3307 | 0.3606 / 0.3453 | (exploratory) |
| pass C e / o | 0.4176 / 0.3846 | 0.4663 / 0.4474 | (reported) |
| reconciled e / o | 0.4548 / 0.3973 | 0.5215 / 0.4812 | (reported) |
| RUN6-NOXDEC atlas tiles R (ceiling) | 0.1838 (0.2199) | 0.1913 (0.2389) | FAIL -> FAIL |
| RUN6-NOXALIGN S (g p99, k p99) | 0 (0, 0) | 2 (0, 0; g max 1) | FAIL -> PASS, very thin: 2 of 41 labels (l2, r1, both where basin = Tomokiyo) |

Consequence, stated narrowly: the known-answer gates of test 0 failed partly because the reference gloss was misread at 7 of 13 lines; on the
leaf-corrected gloss the published key plus a blind Sonnet glyph pass (B on FT-D's crops, D on the re-cut) carries the gloss's sequence above
both nulls at both '#' resolutions. That lifts the gate's own condition ("no target leaf is scored" until it passes); nothing was scored on
c510-516 here (not in this brief). These flips rest on this worker's single, print-aware read of eight gloss lines; a second read of
c262gx_L01..L08 by a session that has not seen the print would make them firmer.
Cost: no subagents; 9 image reads by this worker.

## Remaining gaps (DEF1-NOXG, 5 Oct 2026)
Read so far: c510-516 segmented whole (9,904 tiles, 120 clusters -> 108 owner piles); the stream aligner's lock-on onto Dupuy 221R-226R is a basin with one common key (N8-NOX PASS) that agrees with Tomokiyo's key on 7 of 17 bridge piles (N8-NOX2 PASS); that key mapped onto the reconciled c262 reader signs reads toward the gloss beyond four nulls (RUN6-NOXREAD PASS, 0.3506 on the leaf-corrected gloss); c262 gloss L01-L08 re-read on native crops (DEF1-NOXG), known-answer gates of test 0 now pass on it; 0 open leaves decoded
- c262 gloss L09-L13 not re-read on native crops (overview suggests L13 "quon" where gloss.tsv has "quil") - blocker: not-attempted; next: cut L09-L13 with the same command (--centres extended), one read, re-run the scripts listed above, ~$0.5
- Second, print-blind read of the eight c262gx crops (the gate flips rest on one print-aware read) - blocker: not-attempted; next: one Sonnet pass on images/c262gx_L01..L08.jpg with no print or gloss shown, diff against gloss.tsv, ~$0.5
- Test 0's gate now passes: score an unglossed target block with Tomokiyo's key under the same test0 rule - blocker: not-attempted; next: two blind passes on a c510-516 line set against the settled labels + Dupuy 221R-226R as reference, ~$5
- Per-token alignment with denser anchors (basin decode S 2 of 41, thin) not run - blocker: not-attempted; next: same masked procedure anchored on a hybrid decode or gap <= 5, pre-registered with nulls g/k, ~$1
- Bridge from atlas piles to key.tsv covers only 17 piles - blocker: not-attempted; next: place c262 tiles under the owner's labels so more piles carry a key.tsv value, ~$1
- c510-516 alignment by line reads (instrument 2) not run - blocker: not-attempted; next: same pipeline with its control first, ~$2
- c511 not transcribed by readers - blocker: not-attempted; next: two passes against settled labels, ~$5
- c472-473 8 March Queen letter body not located in Dupuy 122-124 - blocker: not-attempted; next: check Dupuy 133L-134, ~$0.3
- "Relation d'une bataille" c231 has no clear copy found - blocker: not-attempted; next: grep Charrière III and the Lepanto relations, ~$1

## Escalation (DEF1-NOXG, 5 Oct 2026)
- [x] siblings: the duplicata/original pairs in this volume found (letters_coverage.tsv)
- [x] basin test: the locked-on runs share one key (N8-NOX, pre-registered, PASS vs non-locking and shuffled-Dupuy nulls)
- [x] key tie: basin count-based consensus vs key.tsv via the c262 bridge (N8-NOX2, pre-registered, PASS 7/17 vs 4/5/5)
- [retired] decode on atlas tiles: c262 tile-stream decode vs gloss (RUN6-NOXDEC FAIL, 0.1913 on the corrected gloss, still under nulls), instrument atlas-tile stream + test0 ratio
- [x] decode on a reader transcription: basin key mapped onto the reconciled c262 signs (RUN6-NOXREAD PASS; corrected gloss 0.3506 vs p99 0.2413/0.2496/max 0.2665/0.2581)
- [ ] per-token alignment: masked per-label alignment PASS by the letter on the corrected gloss (S 2 vs p99 0/0, g max 1), too thin to use; denser-anchor variant untried
- [x] clear-pages: Dupuy 521 221R-226R transcribed and aligned whole; the alignment locks on in a basin with a common key
- [x] known-keys: Tomokiyo's published key applied to c262; on the leaf-corrected gloss the registered gate passes (pass B, pass D)
- [x] print: Charrière III pp.258, 520-524 and 551-558 read; p.258 differs from the leaf gloss at L08
- [n/a] key-rebuild: a published key exists
- [x] image-check: c262 re-cut; c262 gloss L01-L08 native crops (DEF1-NOXG); c510-516 native line bands; owner sort of the atlas piles
- [x] retry: NOX-CONFIRM (FAIL as specific), N8-NOX basin (PASS), N8-NOX2 key tie (PASS), RUN6-NOXDEC tile decode (FAIL, non-test), RUN6-NOXREAD reader-sign decode (PASS), RUN6-NOXALIGN masked alignment (thin), DEF1-NOXG gloss re-read
Verdict: keep going: 9 internal gaps; cheapest next: print-blind second read of the c262gx gloss crops, ~$0.5

## DEF1-NOXB: blind second read of the c262gx gloss crops (5 Oct 2026, 21:05-21:1x UTC by date -u, account-1 worker)
Pre-registered in PREREG-DEF1NOXB.md (committed before any crop was viewed). One blind read by this session of
images/c262gx_L01..L08.jpg, without Charrière, gloss.tsv, reading files, AUDIT.md or DEF1-NOXG's commit; the read is in
read-DEF1NOXB.tsv (committed before gloss.tsv was opened). Scored by word alignment after normalisation (case, accents,
punctuation and apostrophes dropped, u/v i/j merged, y->i; [?] counts as a miss).

**Control (L02, L03, L05, L07): 14/21 = 0.667, below the 0.80 gate. The test-line comparison licenses nothing.**
Brief error found on opening gloss.tsv: its DEF1-NOXG header says L01-L06 and L08 were corrected and only L07 unchanged, so
three of the four control lines (L02, L03, L05) were themselves DEF1-NOXG's corrected text, not an independent known answer;
the control is therefore not independent of the reading it was meant to check. Even so the control is below gate.

| line | gloss.tsv (DEF1-NOXG) | DEF1-NOXB blind read | words agree |
|---|---|---|---|
| L02 (ctl) | par mer et par terre, vous ne | par mer et par terre bonne no[?] | 5/7 |
| L03 (ctl) | vouldrez empescher lantienne | bien d'en[?] empescher lautrem[?] | 1/3 |
| L05 (ctl) | vostre nation / pendant le temps | bonne nation pendant le temps | 4/5 |
| L07 (ctl) | de dela il ne faudra pas | de dela je ne faudray pas de[?] | 4/6 |
| L01 | veullent s'aller promener en fland[res] | beaucoup s'allier[?] fomenter en flandres | 2/5 (differ: veullent, s'aller, promener) |
| L04 | liberte des gens de guerre de | liberte du pays[?] de guerre de | 4/6 (differ: des gens) |
| L06 | que la farce se jouera du coste | que la france se joindra du coste | 5/7 (differ: farce, jouera) |
| L08 | sendormir de deca. Car la partie | s'endormir[?] de deca car la partie | 5/6 (sendormir agreed but marked [?] = miss) |

Reading: the blind eye's misses on the controls are mostly the abbreviated words (vo9 -> "bonne", vre -> "bonne"), which is
where a second, crop-level instrument is needed; the agreements are the plain words. Nothing here confirms or refutes
DEF1-NOXG's corrections. gloss.tsv not edited. Cost well under the $2 cap; no network requests (local crops only).

## D2-NOXB2: blind read of the c262 gloss with a valid control (5 Oct 2026, 23:19-23:25 UTC by date -u, account-1 worker)
Brief: `.claude/briefs/runs/2026-10-05-account1-default-2217-jobs.md` D2-NOXB2 (LANE DEFAULT-account-1-20261005-2217).
Intake gate: `fr16142-noailles-constantinople-1571: partial (line 1) -- edition/page or full-text-search citation found within 6 lines` (exit 0).
Pre-registered in PREREG-D2NOXB2.md before any crop was viewed. Which gloss lines 4ef591e8c (DEF1-NOXG) changed was taken from a
script printing only the line-id column of that commit's gloss.tsv diff: L01-L06 and L08; unchanged L07, L09-L13. Control = L07, L09, L10.
One blind Opus read of images/c262gl_L01..L10.jpg (FT-D whole-line crops), written to read-D2NOXB2.tsv and pushed (fa93058f3) before
gloss.tsv was opened; scored by `scripts/d2noxb2_score.py` (PX-BRODEC normalisation, difflib, exit 3 below gate).

| line | role | gloss.tsv | D2-NOXB2 blind read | agree |
|---|---|---|---|---|
| L07 | control | de dela il ne faudra pas | de dela je ne faudra pas [?] | 5/6 |
| L09 | control | est forte / il est vray que jay trouve | est forte / il est vray que j'ay tenu | 6/8 |
| L10 | control | ces gens icy si comblez de biens | [?] gens icy si comble de bruits | 4/7 |
| **control pooled** | | | | **15/21 = 0.714, gate 0.80: FAIL** |
| L01 | target | veullent s'aller promener en fland res | veullent s'aller presenter en flandres | 4/7 |
| L02 | target | par mer et par terre, vous ne | same | 7/7 |
| L03 | target | vouldrez empescher lantienne | vouldrez empescher l'autonne | 2/3 |
| L04 | target | liberte des gens de guerre de | liberte de gens de guerre de | 5/6 |
| L05 | target | vostre nation / pendant le temps | same | 5/5 |
| L06 | target | que la farce se jouera du coste | que la [?] se joindra du coste | 5/7 |
| L08 | target | sendormir de deca car la partie | s'endormir de deca car la partie | 5/6 |

The control fails, so the target comparison licenses nothing. Sensitivity (not the gate): the registered normaliser splits "j'ay" into two
tokens where gloss.tsv writes "jay" (the PX-BRODEC notation trap again, on my own side); joining apostrophes gives 16/21 = 0.762, still FAIL.
The real control misses are L07 je/il, L09 tenu/trouve, L10 ces/[?], comblez/comble, biens/bruits. Against DEF1-NOXB's earlier blind read,
this read agrees with DEF1-NOXG on L01 "veullent s'aller", L04 "gens" and L05 "vostre" (where DEF1-NOXB had "beaucoup", "pays", "bonne"), and
agrees with DEF1-NOXB, not DEF1-NOXG, on L06 "joindra" (DEF1-NOXG "jouera"). gloss.tsv not edited. Charriere not opened. No network
requests (local crops only). Rule 3 repeat clause: two whole-line blind eyes have now failed their control on these crops; the next attempt
is the word-level two-pass instrument named in Remaining gaps, not a third whole-line read.

## Remaining gaps (D2-NOXB2, 5 Oct 2026)
Read so far: c510-516 segmented whole (9,904 tiles, 120 clusters -> 108 owner piles); the stream aligner's lock-on onto Dupuy 221R-226R is a basin with one common key (N8-NOX PASS) that agrees with Tomokiyo's key on 7 of 17 bridge piles (N8-NOX2 PASS); that key mapped onto the reconciled c262 reader signs reads toward the gloss beyond four nulls (RUN6-NOXREAD PASS, 0.3506 on the leaf-corrected gloss); c262 gloss L01-L08 re-read on native crops (DEF1-NOXG), known-answer gates of test 0 now pass on it; 0 open leaves decoded
- c262 gloss L09-L13 not re-read on native crops (overview suggests L13 "quon" where gloss.tsv has "quil") - blocker: not-attempted; next: cut L09-L13 with the same command (--centres extended), one read, re-run the scripts listed above, ~$0.5
- Second, print-blind read of c262 gloss L01-L08: two whole-line blind Opus reads have now missed their own control (DEF1-NOXB 0.667 on a control three-quarters changed by DEF1-NOXG; D2-NOXB2 0.714 on the valid unchanged control L07/L09/L10, gate 0.80), so DEF1-NOXG's corrections stay supported by one print-aware read only; disputed words L01 promener, L03 lantienne, L06 farce/jouera are unconfirmed, not refuted (both blind reads give 'joindra' on L06) - blocker: not-attempted; next: two independent blind passes on word-level crops of L01-L10 (tools/iiif_lines.py, 2-3 words per crop; a different instrument from the whole-line eye, which rule 3's repeat clause now bars from a third try), control L07/L09/L10 scored by scripts/d2noxb2_score.py, ~$1.5
- Test 0's gate now passes: score an unglossed target block with Tomokiyo's key under the same test0 rule - blocker: not-attempted; next: two blind passes on a c510-516 line set against the settled labels + Dupuy 221R-226R as reference, ~$5
- Per-token alignment with denser anchors (basin decode S 2 of 41, thin) not run - blocker: not-attempted; next: same masked procedure anchored on a hybrid decode or gap <= 5, pre-registered with nulls g/k, ~$1
- Bridge from atlas piles to key.tsv covers only 17 piles - blocker: not-attempted; next: place c262 tiles under the owner's labels so more piles carry a key.tsv value, ~$1
- c510-516 alignment by line reads (instrument 2) not run - blocker: not-attempted; next: same pipeline with its control first, ~$2
- c511 not transcribed by readers - blocker: not-attempted; next: two passes against settled labels, ~$5
- c472-473 8 March Queen letter body not located in Dupuy 122-124 - blocker: not-attempted; next: check Dupuy 133L-134, ~$0.3
- "Relation d'une bataille" c231 has no clear copy found - blocker: not-attempted; next: grep Charrière III and the Lepanto relations, ~$1

## Escalation (D2-NOXB2, 5 Oct 2026)
- [x] siblings: the duplicata/original pairs in this volume found (letters_coverage.tsv)
- [x] basin test: the locked-on runs share one key (N8-NOX, pre-registered, PASS vs non-locking and shuffled-Dupuy nulls)
- [x] key tie: basin count-based consensus vs key.tsv via the c262 bridge (N8-NOX2, pre-registered, PASS 7/17 vs 4/5/5)
- [retired] decode on atlas tiles: c262 tile-stream decode vs gloss (RUN6-NOXDEC FAIL, 0.1913 on the corrected gloss, still under nulls), instrument atlas-tile stream + test0 ratio
- [x] decode on a reader transcription: basin key mapped onto the reconciled c262 signs (RUN6-NOXREAD PASS; corrected gloss 0.3506 vs p99 0.2413/0.2496/max 0.2665/0.2581)
- [ ] per-token alignment: masked per-label alignment PASS by the letter on the corrected gloss (S 2 vs p99 0/0, g max 1), too thin to use; denser-anchor variant untried
- [x] clear-pages: Dupuy 521 221R-226R transcribed and aligned whole; the alignment locks on in a basin with a common key
- [x] known-keys: Tomokiyo's published key applied to c262; on the leaf-corrected gloss the registered gate passes (pass B, pass D)
- [x] print: Charrière III pp.258, 520-524 and 551-558 read; p.258 differs from the leaf gloss at L08
- [n/a] key-rebuild: a published key exists
- [x] image-check: c262 re-cut; c262 gloss L01-L08 native crops (DEF1-NOXG); c510-516 native line bands; owner sort of the atlas piles
- [x] retry: NOX-CONFIRM (FAIL as specific), N8-NOX basin (PASS), N8-NOX2 key tie (PASS), RUN6-NOXDEC tile decode (FAIL, non-test), RUN6-NOXREAD reader-sign decode (PASS), RUN6-NOXALIGN masked alignment (thin), DEF1-NOXG gloss re-read, DEF1-NOXB blind second read (control 0.667 < 0.80 gate, licenses nothing), D2-NOXB2 blind read with valid control (0.714 < 0.80, licenses nothing; whole-line eye not to be re-tried)
Verdict: keep going: 9 internal gaps; cheapest next: c262 gloss L09-L13 native cut and read, ~$0.5
