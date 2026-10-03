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
