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
