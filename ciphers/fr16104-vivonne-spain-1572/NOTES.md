partial
Read by this worker (3 Oct 2026, full-text grep of the whole volume plus reading of the hits): Gachard, *La Bibliothèque nationale à Paris* II (1875, IA labibliothquen02gachuoft) Saint-Gouard section from p.362 (per-letter analyses of fr.16104-16106 with "chiffres, avec/sans le déchiffrement" flags); d'Ars, *Jean de Vivonne* (1884, IA lepredemadamede00dargoog, whole volume, 136 Saint-Gouard hits, notes citing fr.16104/16105/16106); La Ferrière, *Lettres de Catherine de Médicis* IV and V (IA lettresdecatheri04cathuoft, 05cathuoft, whole volumes); Groen van Prinsterer, *Archives de la maison d'Orange-Nassau* 1re sér. IV (IA archivesoucorre03housgoog, whole volume, 48 "Goard" hits).

- Target: BnF fr.16104 (btv1b9009609w), fr.16105 (btv1b9009663p), fr.16106 to f.198 (btv1b90096628); Jean de Vivonne, sr de Saint-Gouard, ambassador in Spain, to Charles IX / Catherine / Henry III, 1572-74. Scout row P2-A (QUEUE.md "LANE-POOLS scout, 3 Oct 2026", POOLS.tsv row, sources/pools-scout/2026-10-03/P2.tsv). Worker: LANE-POOLS CS-5, 3 Oct 2026.
- Check-solved ledger label: no transcription, decoding or key use done; a found decipherment is recorded, not used.

## What the sources say about this pool
Verdict sentence: **the cipher letters are largely already deciphered on the leaves.** Gachard (1875) flags each Saint-Gouard dispatch he analyses: "(En chiffres, avec le déchiffrement)" for the great majority of cipher letters, "(En partie chiffrée, sans le déchiffrement)" for two. Tomokiyo (henryiii.htm, sources/cryptiana/web/henryiii.htm, read 3 Oct 2026) says: "The cipher used from April 1572 to November 1574 in BnF fr.16104 ..., fr.16105 ... and fr.16106 (up to f.198) use the following cipher" -- key image only (henryiii_Vivonne1.png, not on disk as a table), "Occasionally, decipherments in the archives are misplaced and misdated, as reported in Mousset p.xlviii" (fr.16105 f.38/41/43/45).

Counts by this worker (regex over OCR text of Gachard II; OCR damage undercounts, so these are floors):

| Volume | Years | dispatch entries matched | "chiffr" mentions | "avec le déchiffrement" | "sans le déchiffrement" |
|---|---|---|---|---|---|
| fr.16104 | 1572 | 21 | 26 | 10 | 1 (8 Sept 1572 per OCR, "En partie chiffrée"; the leaf reads 5 Sept, see N4-VIV) |
| fr.16105 | 1573 | 17 | 22 | 7 | 1 (4 June 1573, "En partie chiffrée") |
| fr.16106 | 1574 (+1579) | 67 (all years) | 28 | 9 | 0 |

Per-letter table: not built (Gachard's flags are OCR text, the leaves were not individually opened by this worker). Status per letter: period decipherment on the leaf (flag "avec le déchiffrement"): at least 26 letters; open (flag "sans"): 2 letters (8 Sept 1572, fr.16104; 4 June 1573, fr.16105), both only partly in cipher; unflagged / not analysed: unknown. Open est. signs: under about 600 for the two flagged letters (est., not measured); the scout's 20,000 figure (P2.tsv, 8 sampled canvases) counts cipher signs that mostly sit beside a clerk's decipherment. Printed plaintext: d'Ars (1884) quotes many of the dispatches in French from these volumes (notes cite the fr.16104/16105 leaves by letter date; e.g. the 9 Sept 1572 St Bartholomew dispatch), Groen IV prints extracts of about 25 Saint-Gouard letters of 1572-73 (e.g. 18 Oct 1572, 8 June, 9 July, 18 Aug, 3 Nov 1573) with ellipses; whether a given quoted extract is from a ciphered paragraph was not determined (OCR text only). d'Ars lists the volumes (p. "Récapitulation des sources"): 16104 Jan-Dec 1572, 16105 Jan-Dec 1573, 16106 1574 and 1579.

Totals: open letters 2 flagged (plus unknown unflagged); open signs est. < 600 flagged; letters already deciphered on the leaf >= 26.

## Web and blog check (CS-5, 3 Oct 2026)
Plain searches (WebSearch), each logged with what it returned:
1. "Vivonne Saint-Gouard ambassadeur Espagne 1572 chiffre déchiffrement dépêches fr. 16104" -> BnF AEM/Gallica notices for Français 16104-16111 (cc462349), Wikipedia Jean de Vivonne; no decipherment or solver page.
2. "\"Saint-Gouard\" \"Vivonne\" cipher Spain 1572 Charles IX decipherment" -> Wikipedia, dbourdeau.github.io/cyphersolver index (no Vivonne target), Gallica fr.16110 notice; nothing on this pool.
3. "BnF français 16104 Vivonne Saint-Gouard dépêches Espagne cipher" -> AEM cc462349 (403 on direct fetch, not retried), Gallica fr.16110, dbourdeau/cyphersolver issue #16 (Espagnol 144 Mercy, a different item); nothing.
4. "cryptiana.blogspot.com OR ciphermysteries.com OR scienceblogs.de Vivonne Saint-Gouard Henry III cipher Spain" -> Wikipedia and genealogy pages only.
5. "Vivonne Saint-Gouard cipher solves Claude OR GPT unsolved cipher" -> Vals AI/Cyphral Distich and GPT-6 Astra Napoleon-general stories; no Vivonne.
Blog site searches (domain-restricted): cryptiana.blogspot.com / cryptiana.web.fc2.com -> one hit, the 2018 forum page on earlier Spanish ciphers, no Vivonne; ciphermysteries.com -> Voynich pages only; scienceblogs.de Klausis Krypto Kolumne -> unrelated posts. Search-engine site searches, not each blog's own search box, and no comment thread was opened because no post names the target.
DECODE: not searched by this worker (sender listing not run; scout P4 searched DECODE by sender 3 Oct 2026, see P4.md). Solver repositories: own shallow clones of dbourdeau/cyphersolver and aaymeloglu/unsolved-ciphers, grep for vivonne|gouard|16104|16105|16106: only Bourdeau's mirror of Tomokiyo's henryiii.txt and SRU JSON catalogue noise (a Louis-Victor / Jehan de Vivonne marriage contract in fr.16110-era notice); no target, output or planning line for this item; Aymeloglu: no hit. Tomokiyo: the sentence quoted above is the only mention.

Requests per host: archive.org about 30 (advancedsearch 8, djvu downloads 17), github.com 2 clones, web searches 8, archivesetmanuscrits.bnf.fr 1 (403), gallica none.

## Premise check (CS-5, 3 Oct 2026)
(a) folder's own notes: not applicable, the folder did not exist; the scout row (P2.tsv) itself names clerk decipherments on fr.16105 canvases 48 and 200 and Tomokiyo's key: found.
(b) other solvers' working files: no output, key application or planning text for fr.16104-16106 in Bourdeau or Aymeloglu clones: not found. Tomokiyo's key table is an image (not on disk); whether anyone ran it on this text: not found.
(c) physical neighbours: Gachard's flags show a clerk's decipherment accompanies most cipher letters (>= 26); Tomokiyo documents fr.16105 f.41 and f.45 as "dechifre de la precedente" leaves, misplaced. Not independently viewed by this worker at native resolution (images not opened, no transcription per brief): found via Gachard and Tomokiyo, leaf-level check unreachable within this job.
(d) recipient side: Catherine de Médicis IV-V print letters *to* Saint-Gouard (about 30 in vol. IV, 1 mention in V), not his cipher dispatches; Groen IV and d'Ars quote his dispatches; Spanish-side copies (AGS Estado K, Archivo documental español) not searched: unreachable/not done. The same fr.16104-06 dispatches are summarised by Gachard II.

## RUN1-VIV2 (4 Oct 2026, account 1 worker for LANE-RUN1): Mousset grep and a partial leaf look
**1. Mousset 1912 (IA dpchesdiplom00longuoft, `_djvu.txt` read in full, 1 request).** The passage Tomokiyo cites as "p.xlviii" is on printed p. xlviii, but it is about Longlée's volumes (fr.16109, 16110; Longlée 1582-90), not Vivonne's: "Malheureusement l'ignorance du chiffre ayant fait commettre, lors de la constitution de ces manuscrits, de nombreuses erreurs (déchiffrements déplacés, dates mal rétablies, interversion de folios chiffrés), la description de Gachard est légèrement inexacte." The Avertissement adds "quelques dates ont été mal lues et beaucoup de déchiffrements mal placés ... certains originaux chiffrés se présentent sans déchiffrements ni indications de date". Grep of the whole OCR for 16104, 16105, "Vivonne": 0 hits; "Saint-Gouard" occurs only as predecessor of Longlée (his last dispatches in fr.16108 ff.380-382 are named, 3 Sept 1582). Found: Mousset's misplacement remark concerns the Longlée volumes. Not found: any statement about fr.16104/16105 f.38/41/43/45 in Mousset (OCR text only; OCR-damaged). Tomokiyo's attribution of the fr.16105 leaves to Mousset p.xlviii is therefore not supported by the text of that page as read.
**2. Gachard II (IA labibliothquen02gachuoft, same grep, 1 request).** "sans le déchiffrement" flags: 8 Sept 1572 (entry L, "En partie chiffrée, sans le déchiffrement") and 4 June 1573 (entry XXXVIII); 8 June 1573 is "presque entièrement chiffrée, avec le déchiffrement" and a footnote says of one of the two copies "celle-ci n'a pas été déchiffrée". Gachard gives no folio numbers.
**3. fr.16104 leaves (btv1b9009609w, 324 canvases, all labelled NP; one canvas = an opening of two pages; stamped folio on the right page runs about canvas minus 12-13 at canvases 150-230: c150 f.139, c170 f.157, c180 f.166, c190 f.179 (19 Sept 1572, "du Sr de St Gouard au Roy", plain French, cipher in the last 3 lines), c200 f.189, c210 f.194, c230 f.213 (7 Oct 1572 enclosure)). Viewed at 1000 px: c170-172 (f.157-159), one letter, plain French at first then cipher; c171-172 are full cipher pages with no clerk's decipherment on the leaves (only verso bleed-through); c180 (f.165-166) full cipher pages, no decipherment on those leaves. So the 8 Sept 1572 letter lies between f.138 and f.179; the candidate is the f.157-159 letter (partial cipher, wholly or mostly cipher after a plain opening), but its date was not legible at 1000 px nor in two crops (docket at foot of c172 and head of c170) -- NOT confirmed, not graded. Estimated cipher lines in c171-172 about 90 (est., not counted line by line).
Not done (cap/box): the fr.16105 4 June 1573 leaf (no label anchors; needs the same bisection, ~10 canvas views); the count of letters lacking a clerk's leaf. Observation only: on the cipher pages seen the clerk's decipherment was not adjacent, so "avec le déchiffrement" (Gachard) means present in the volume, not necessarily on the next leaf; not measured.
Requests: archive.org 3, gallica.bnf.fr 12 (iiif images). No transcription, no decode. Cost: see the lane ledger.

## Remaining gaps (finish-or-blocker pass, 3 Oct 2026)
Read so far: 26 of at least 28 flagged cipher letters (about 93%) are flagged by Gachard as carrying a period decipherment; the number of unflagged cipher letters is unmeasured because the leaves were not opened.
- Leaves of the two "sans le déchiffrement" letters (fr.16104 8 Sept 1572, fr.16105 4 June 1573) and unflagged cipher letters - blocker: not-attempted; fr.16104 candidate f.157-159 found but date unconfirmed, fr.16105 untouched; next: read the date of the f.157-159 letter at native crop, bisect fr.16105 (canvases NP) for 4 June 1573, count letters lacking a clerk's leaf, ~$1.5
- Spanish-side copies (AGS Estado K) and Gachard vol. I - blocker: needs-physical-access; AGS is not digitised in a route this worker could open
## Escalation (3 Oct 2026)
- [ ] siblings: fr.16106 f.207+ Longlée pool is scout row P2-B, a separate check; neighbouring clear letters not yet matched
- [ ] clear-pages: clerk's leaves exist per Gachard; open the two "sans" letters, planned step above
- [x] known-keys: Tomokiyo's table (image henryiii_Vivonne1.png) is the known key; not run on this text by any solver found
- [x] print: Gachard II, d'Ars, Catherine IV-V, Groen IV read (see top); phrase search on decoded text not possible before a reading exists
- [n/a] key-rebuild: no reading attempted under this brief
- [ ] image-check: leaves not viewed at native resolution; planned step above
- [ ] retry: nothing has been tried yet to retry
Verdict: keep going: 1 internal gap; cheapest next: native-crop date of the f.157-159 letter, then fr.16105 bisection, ~$1.5

## While waiting
Nothing waits on a person. The action that depends on nobody: fetch fr.16104 and fr.16105 canvases of the two "sans" letters with `tools/gallica_folio.py` and look for a clerk's leaf.

## Gate output (3 Oct 2026)
```
intake_gate_check: fr16104-vivonne-spain-1572: partial (line 1) -- edition/page or full-text-search citation found within 6 lines (exit 0)
gaps_check: OK keep-going fr16104-vivonne-spain-1572: keep going: 2 internal gap(s), 4 step(s) untried
next_steps --wait-only | grep fr16104: no line
```

## N4-VIV (4 Oct 2026, LANE-NEAR4 worker, account 2): leaves and dates of the two "sans le déchiffrement" letters
Brief: .claude/briefs/runs/2026-10-04-ytbiz-near4-wave2.md "N4-VIV". No transcription, no decode, no subagent calls; images viewed by this worker directly (1200 px thumbnails plus one native crop).

**fr.16104 (btv1b9009609w): the f.157-159 letter is Gachard's entry L, dated 5 Sept 1572, not 8 Sept.**
- The letter ends on canvas 173, left page (f.159v), with the subscription and the date line, then the signature. Native crop (`python3 tools/iiif_lines.py --ark btv1b9009609w --canvas 173 --region 740,4375,3300,920 --out ciphers/fr16104-vivonne-spain-1572/images --prefix c173_date --debug`: 4 lines, 8 crops, images/c173_date_*.jpg, manifest.json) reads "... de Madril ce v^me jo[ur] de sept[em]b[re] 1572" (crop c173_date_L03_s2.jpg, year on L04). The day numeral is a single "v" with "me" raised above a dot; a blank stretch sits between them and no faded minims were seen at 2x enlargement of the native crop. Reading: 5 Sept 1572 (uncertainty: a lost "iii" in the blank cannot be excluded by eye, but nothing is visible).
- Gachard II's entry L, as OCR'd ("L. -- Au roi, Madrid, S septembre 1572. (En partie chiffrée, sans le déchiffrement.) Audience qu'il a eue du roi le 27 août"), has "S" for the day. The same OCR prints 5 as "S" elsewhere ("1S72", "iS72"), so the 3 Oct reading "8 Sept" came from the OCR and the printed figure is probably 5 (inferred: the printed page itself was not seen). Content match: Gachard quotes the passage on the army sent "avecques mons^r le duc de Longueville, son gouverneur en Picardye" and the duc d'Albe's suspicion; "Monsieur de Longueville" and "duc d'Alve" are legible in the plain French on canvas 170 (left page). So the f.157-159 letter is the flagged entry L: canvases 170-173, cipher from the lower third of f.157 (canvas 170, right page) to the top of f.159v (canvas 173, left page). No interlinear gloss on canvases 170, 172 or 173 (171 not re-viewed; on 3 Oct it showed full cipher and only bleed-through). Docket on f.160 (canvas 173, right page) foot reads "Juin et Juillet 1572", a later folder label, not this letter's date. Bisection of fr.16104 not needed.
- Size, est. by eye on the thumbnails (not counted): about 150-175 cipher lines.

**fr.16105 (btv1b9009663p, 249 canvases, all labelled NP; manifest fetched to sources/gallica-manifests/): the 4 June 1573 letter is ff.99-108v, canvases 102-112.**
Bisection (1200 px thumbnails): c150 = f.147 "dechiffré de la precedente", docket 30 juillet 1573; c130/131 = ff.126v-128, a full-cipher letter signed; c126 = f.123 to the Queen, docket 18 juin 1573; c120 = f.117 "dechiffré de la precedente", docket 18 juin 1573; c116 = ff.112v-113, full cipher; c114 = f.111 "du S^r de S^t Goard au Roy", docket 18 juin 1573, cipher with an interlinear gloss over its first lines only (f.110v = address leaf of the 8 June letter to the Queen, endorsed "8 juin 1573"); c113 = ff.109v-110 address leaf; c112 = f.109 to the Queen, docket "8 Juin 1573", plain French, dated "de Madrid ce [?] de Juing 1573" (left page f.108v = end of the preceding letter); c110 = f.107, plain French (Middelburg, Goulette); c109 = ff.105v-106 plain French; c106 = ff.102v-103, cipher to the foot of f.103, then plain French starting "Je baise ... les mains"; c104 = ff.100v-101, full cipher; c103 = f.100, plain French then cipher from about line 19; c102 = f.99, docket "4 Juin 1573 / Madrid", heading "du S^r de S^t Goard au Roy", opening "Sire, ..."; f.98v (address leaf) endorsed "4 juin 1573"; c101 = ff.97v-98, address leaf of the preceding letter.
- Identification: f.100 carries, in plain French just before the cipher starts, the passage Gachard quotes under XXXVIII (4 June 1573): "Le dernier de May feut juré a S^t Hyeronyme Monsieur le prince de Castille, Leon et Grenade ...". f.99 mentions the Corpus Christi procession and the audience the next day (Gachard's summary of XXXVIII). Docket on the leaf and on the address leaf: 4 June 1573. Match on docket and content.
- Cipher block: from about line 19 of f.100 to the foot of f.103, so f.100 (lower half), ff.100v, 101, 101v, 102, 102v, 103. No interlinear gloss on canvases 103, 104 or 106 (105 = ff.101v-102 not viewed). Size, est. by eye (not counted): about 240 cipher lines, i.e. several thousand signs, well above the 3 Oct estimate of "< 600 signs for the two letters"; Gachard's "en partie chiffrée" covers a long cipher block.
- **Possible decipherment through a duplicate (observation, not checked):** Gachard's XL-XLI (8 June 1573, "Presque entièrement chiffrée, avec le déchiffrement") says "Cette lettre est un duplicata de celle du i 3" (OCR; "4" is the likely figure), with a footnote "C'est pourquoi celle-ci n'a pas été déchiffrée" whose anchor is lost in the OCR. The plain passages Gachard quotes under XL ("L'empereur faict tout ce qu'il peult de reconcillier le prince d'Oranges ...", "Le filz dudict prince est tousjours estudiant en Arcala ...") are on f.108v, the end of the 4 June letter. If XL is a duplicate of 4 June carrying a clerk's decipherment, the 4 June cipher block has a period decipherment in another copy, and the footnote would mean the 4 June original was left undeciphered for that reason. The 8 June duplicate to the King was not found in sequence: f.109 is 8 June to the Queen and f.111 begins the 18 June letter. Not located in this job.
- Observation: these leaves also carry an older ink numbering at the top right (f.99 "40", f.109 "42", f.111 "43", f.117 "44", f.123 "45"/"46"). Tomokiyo's fr.16105 "f.38/41/43/45" (misplaced decipherments) may follow this older series rather than the stamped folios. Not checked.

Requests: gallica.bnf.fr 18 (fr.16104: 3 thumbnails, 1 native region; fr.16105: 1 manifest, 13 thumbnails), all >= 2.5 s apart, all HTTP 200; archive.org 1 (Gachard II djvu.txt, labibliothquen02gachuoft). Subagent calls: 0. Cost: see the lane ledger.

## Remaining gaps (N4-VIV refresh, 4 Oct 2026)
Read so far: 26 of at least 28 flagged cipher letters (about 93%) carry a period decipherment per Gachard's flags; the two "sans" letters are now located (fr.16104 ff.157-159v, 5 Sept 1572, about 150-175 cipher lines est.; fr.16105 ff.99-108v, 4 June 1573, about 240 cipher lines est.), neither has an interlinear gloss on the pages viewed; unflagged cipher letters unmeasured.
- fr.16105 4 June 1573 cipher block (ff.100-103) - blocker: not-attempted; Gachard calls the 8 June letter a duplicate "avec le déchiffrement" (N4-VIV); next: locate the 8 June 1573 letter to the King and its decipherment in fr.16105 (old-number series 40-46 and Tomokiyo's f.38/41/43/45 first, then bisect outside ff.97-150), and check whether its cipher matches ff.100-103, ~$1
- fr.16104 5 Sept 1572 cipher block (ff.157-159v) - blocker: not-attempted; no decipherment located, no duplicate named by Gachard; next: transcribe the block (crops via tools/iiif_lines.py, two blind passes + reconciliation per page, 4 pages) and apply Tomokiyo's published key table (henryiii_Vivonne1.png) once it is put on disk as key.tsv, ~$8
- Unflagged cipher letters and letters lacking a clerk's leaf - blocker: not-attempted; Gachard gives no folio numbers and the leaf survey is incomplete; next: one 1200 px pass over fr.16104/16105 canvases with a per-letter table (cipher yes/no, decipherment leaf, gloss), ~$3
- Spanish-side copies (AGS Estado K) and Gachard vol. I - blocker: needs-physical-access; AGS is not digitised in a route this worker could open
## Escalation (4 Oct 2026)
- [ ] siblings: the 8 June 1573 duplicate of the 4 June letter (Gachard XL-XLI) is the planned step above; fr.16106 f.207+ Longlée pool is scout row P2-B, a separate check
- [x] clear-pages: both "sans" letters opened (N4-VIV): canvases 170-173 (fr.16104) and 102-112 (fr.16105); no clerk's gloss on the pages viewed
- [ ] known-keys: Tomokiyo's table (image henryiii_Vivonne1.png) is the known key; not yet on disk as key.tsv nor applied; planned after transcription
- [x] print: Gachard II, d'Ars, Catherine IV-V, Groen IV read (see top); phrase search on decoded text not possible before a reading exists
- [n/a] key-rebuild: a published key exists, rebuild is not needed unless it fails
- [x] image-check: both letters viewed, the fr.16104 date line at native resolution (images/c173_date_*.jpg)
- [ ] retry: nothing has been tried yet to retry; the first test is the duplicate search above
Verdict: keep going: 3 internal gaps; cheapest next: locate the 8 June 1573 duplicate and its decipherment in fr.16105, ~$1

## N4-VIV2 (4 Oct 2026, LANE-NEAR4 worker, account 2): the 8 June 1573 "duplicate" and its decipherment
Brief: .claude/briefs/runs/2026-10-04-ytbiz-near4-wave3.md "N4-VIV2". No transcription, no decode, no subagent calls; images viewed by this worker directly (4 image reads: two 1200 px openings, two region crops). Folio/canvas map for fr.16105 (btv1b9009663p, every label NP): `python3 tools/gallica_folio.py btv1b9009663p --anchor 102=99 --anchor 112=109 --anchor 114=111 --anchor 120=117 --anchor 150=147` -> canvas = 1.000 x folio + 3.00, residuals 0.0 on all five N4-VIV anchors; one canvas = one opening, left page f.(c-4)v, right page f.(c-3)r.

**Found: the clerk's decipherment is ff.104r-108v, immediately after the cipher letter ff.99-103v (canvases 107 right page to 112 left page).**
- f.104r (canvas 107, right page; crop images/fr16105_c107_f104_head.jpg): later docket top left "8 Juin 1573", heading in the clerk's hand "dechiffré de la precedente", old ink piece number "41" top right (the cipher letter f.99 carries "40", f.109 "42"), stamped folio 104. The text of f.104r is very faded in the Gallica scan: lines are present but not legible at the resolution fetched, even after contrast stretching (one 2000 px region, ImageMagick -normalize/-level). So the opening words of the decipherment were NOT read.
- ff.104v-108r: plain French in a clerk's widely spaced decipherment hand (canvas 111 = ff.107v-108 viewed at 1200 px: Angleterre, "la Catholique", Flandres, the duc d'Albe's dealings with the English). N4-VIV's "c109 = ff.105v-106 plain French; c110 = f.107 plain French (Middelburg, Goulette)" are these decipherment pages, not part of the letter.
- f.108v (canvas 112, left page; crop images/fr16105_c112_f108v_end_norm.jpg): the decipherment ends "... qu'il perde ses Estatz s'il veult continuer a les remedier par la force, ce qu'il ferat en ung jour tout seul faisant une reconcilliation avecques ses subgectz. Mais l'on m'asseure qu'il n'a donné nulle esperance voulloir entendre a nul party ; toutesfois je ne sçay ce que enfin il fera pour remedier ses affaires. Le filz dudict prince est tousjours estudiant en Arcala avecques toute liberté, mais assez mal tenu et pourveu de ses necessitez." (read by eye, spelling normalised where the hand is unclear) -- then blank: no closing formula, no date, no signature. These are the passages Gachard quotes under XL-XLI. N4-VIV took f.108v for the end of the 4 June letter; it is the end of the decipherment.
- The cipher letter itself ends on f.103v (canvas 107, left page): a few lines of plain French at the head of the page (a report "hyer ... publia ung bruict" about the Turk and forty or fifty thousand men, Lombardy), then the closing "Sire, je supplie le Createur donner a V[ost]re Ma[jes]té ... De Madrid ce [day] jour de Juing 1573" and the subscription and signature. The day numeral was not settled at 1200 px (iiij or viij); not re-read at native resolution (vision budget spent).

**Does the decipherment cover the cipher text of ff.100-103?** Inferred (grade I), not confirmed token by token:
1. Heading "dechiffré de la precedente", placed directly after the letter, with consecutive old piece numbers 40 (letter) / 41 (decipherment).
2. The decipherment stops at "necessitez" with no closing, where the cipher letter's cipher block stops at the foot of f.103 before its plain postscript and closing on f.103v: a decipherment of the cipher block only, as on f.117 and f.147 ("dechiffré de la precedente", N4-VIV).
3. Size: about 9.5 decipherment pages (f.104r-108v) against about 240 cipher lines in ff.100-103 (N4-VIV's eye estimate) -- proportionate, not measured.
4. Content: everything Gachard summarises or quotes under XL-XLI (the audience on the duc d'Albe's arrangement with the English, the Orange reconciliation the King pretends not to know, the Flemings vs Spaniards on the general pardon after Haarlem, the Emperor's mediation, the son at Alcalá) sits in the decipherment.
Not done: a cipher-side anchor (a few cipher groups read with Tomokiyo's key against the decipherment's wording) -- needs the key on disk and a transcription; and the decipherment's first lines (f.104r, faded) against the plain sentence that ends just before the cipher on f.100 ("... Le jurement des autres provinces se remect aux cours de Monson").

**Reinterpretation of Gachard's numbering (inference, checked on four pieces):** Gachard's roman numerals in this section equal the old ink piece numbers on the leaves: XL = ink 40 (f.99, the cipher letter), XLI = ink 41 (f.104, its decipherment), XLIII-XLIV = ink 43-44 (f.111 the 18 June letter, f.117 its "dechiffré de la precedente"), XLV = ink 45 (f.123, to the Queen, 18 June). If that holds, then:
- Gachard's XL-XLI ("8 juin 1573, presque entièrement chiffrée, avec le déchiffrement ... duplicata de celle du 4") is the letter ff.99-103v with its decipherment ff.104-108v; his "8 juin" likely comes from the decipherment's docket, while the letter's own docket and address leaf read 4 June (N4-VIV).
- Gachard's XXXVIII ("4 juin 1573, en partie chiffrée, sans le déchiffrement") is a different piece, ink no. 38, the other copy of the same letter, somewhere before f.99. N4-VIV matched ff.99-103 to XXXVIII by the plain passage "Le dernier de May feut juré ...", which both copies would carry; the docket match ("4 Juin") also fits either copy. Candidate place: N4-VIV saw an address leaf on f.98v endorsed "4 juin 1573" (canvas 101), i.e. the piece just before f.99 is a 4 June item.
- Gachard's footnote ("C'est pourquoi celle-ci n'a pas été déchiffrée") then reads: the 4 June copy (XXXVIII) was not deciphered because its duplicate (XL) was. The OCR "celle du i 3" = "celle du 4" + footnote anchor 3 (inferred from the footnote order: 1 Grenade, 2 cours, 3 this one).
- So the open cipher block of the "sans" letter is ink piece 38, not ff.100-103; ff.100-103 has a period decipherment on the next leaves.
Caution (Tomokiyo, henryiii.htm, sources/cryptiana/web/henryiii.htm): in this same volume (stamped ff.38/41/43/45, March 1573) a decipherment was filed after the wrong letter and "there appear to be textual differences" between a cipher text and the decipherment of its twin ("desagreable" in cipher reads "mauvais" in the decipherment). A duplicate's decipherment is a crib, not a token-for-token key, until aligned.

**Known-plaintext route (next step, estimate):** (a) locate ink piece 38: view fr.16105 canvases 95-101 at 1200 px (ff.92-98), read the old ink numbers and dockets, confirm a 4 June 1573 letter partly in cipher with no decipherment leaf (~4 Gallica requests, ~$0.5); (b) if found, its cipher block's plaintext is the ff.104-108v decipherment (to be checked for textual differences): transcribe the ink-38 cipher block (crops via tools/iiif_lines.py, two blind passes + reconciliation per page) and transcribe the decipherment once (plain French; f.104r needs a native-resolution fetch with contrast stretching), put Tomokiyo's key (henryiii_Vivonne1.png) on disk as key.tsv, apply it with tools/decode_key.py, and use the decipherment as the C-grade check (~$10-14 depending on block length). (c) If no ink 38 is found before f.99, then XXXVIII and XL are the same piece in Gachard's description and the "sans" letter of 1573 has its decipherment at ff.104-108v: the fr.16105 gap closes as "period decipherment on the leaf" and only fr.16104 ff.157-159v (5 Sept 1572) remains open.

Requests: gallica.bnf.fr 8 (4 x 1200 px openings c105/c107/c108/c111, of which c108 returned HTTP 503 once and was refetched once, 200; 2 region crops on c107, 1 on c112), all >= 2.5 s apart; archive.org 1 (Gachard II djvu.txt, labibliothquen02gachuoft). c105 and c108 fetched to scratch but not viewed (vision budget). Subagent calls: 0. Cost: see the lane ledger.

## Remaining gaps (N4-VIV2 refresh, 4 Oct 2026)
Read so far: 26 of at least 28 flagged cipher letters (about 93%) carry a period decipherment per Gachard's flags; of the two "sans" letters, the fr.16105 one is now probably a second copy (ink piece 38) of a letter whose other copy ff.99-103v has its clerk's decipherment at ff.104-108v (N4-VIV2); fr.16104 ff.157-159v (5 Sept 1572) has none located; unflagged cipher letters unmeasured.
- fr.16105 ink piece 38 (Gachard XXXVIII, 4 June 1573 copy "sans le déchiffrement") - blocker: not-attempted; its leaves not yet located (Gachard gives no folios, vision budget of N4-VIV2 spent); next: view canvases 95-101 for old ink no. 38 and a 4 June docket, then transcribe its cipher block and align with the ff.104-108v decipherment and Tomokiyo's key, ~$0.5 to locate, ~$10-14 to read
- fr.16104 5 Sept 1572 cipher block (ff.157-159v) - blocker: not-attempted; no decipherment located, no duplicate named by Gachard; next: transcribe the block (crops via tools/iiif_lines.py, two blind passes + reconciliation per page, 4 pages) and apply Tomokiyo's published key table (henryiii_Vivonne1.png) once it is put on disk as key.tsv, ~$8
- Unflagged cipher letters and letters lacking a clerk's leaf - blocker: not-attempted; Gachard's numerals appear to be the old ink piece numbers (N4-VIV2), so a per-piece table can be built from the ink numbers; next: one 1200 px pass over fr.16104/16105 canvases with a per-letter table (ink no., cipher yes/no, decipherment leaf, gloss), ~$3
- Spanish-side copies (AGS Estado K) and Gachard vol. I - blocker: needs-physical-access; AGS is not digitised in a route this worker could open
## Escalation (4 Oct 2026, N4-VIV2)
- [ ] siblings: ink piece 38 (other copy of 4 June 1573) is the planned step above; fr.16106 f.207+ Longlée pool is scout row P2-B, a separate check
- [x] clear-pages: the decipherment of ff.99-103v found at ff.104-108v (N4-VIV2); both "sans" letters opened (N4-VIV)
- [ ] known-keys: Tomokiyo's table (image henryiii_Vivonne1.png) is the known key; not yet on disk as key.tsv nor applied; planned after transcription
- [x] print: Gachard II, d'Ars, Catherine IV-V, Groen IV read (see top); phrase search on decoded text not possible before a reading exists
- [n/a] key-rebuild: a published key exists, rebuild is not needed unless it fails
- [x] image-check: f.104r head and f.108v end viewed (images/fr16105_c107_f104_head.jpg, fr16105_c112_f108v_end_norm.jpg); f.104r text too faded at the fetched resolution
- [ ] retry: f.104r opening lines at native resolution with contrast stretching, with the ink-38 search
Verdict: keep going: 3 internal gaps; cheapest next: view fr.16105 canvases 95-101 for ink piece 38 (the 4 June copy without decipherment), ~$0.5

Gate output (N4-VIV2, 4 Oct 2026): `OK keep-going fr16104-vivonne-spain-1572: keep going: 3 internal gap(s), 3 step(s) untried`

## N4-VIV3 (4 Oct 2026, LANE-NEAR4 worker, account 2): ink piece 38 and the legibility of the 8 June decipherment
Brief: .claude/briefs/runs/2026-10-04-ytbiz-near4-wave4.md "N4-VIV3". No transcription, no decode, no subagent calls. Two image reads of two contact sheets made from seven 1200 px openings (committed downscaled: images/fr16105_c95-98_1200px_sheet.jpg, images/fr16105_c99-101_1200px_sheet.jpg), one image read of a native crop. Folio map as N4-VIV2 (canvas c = left page f.(c-4)v, right page f.(c-3)r).

**(1) Canvases 95-101 (ff.91v-98r), what is on them (read at 1200 px, by eye):**
| canvas | left page | right page |
|---|---|---|
| 95 | f.91v plain French, full page (a letter already running; its first leaf is before f.91v, not viewed) | f.92r plain French for about the upper half, then cipher (letter-alphabet groups with # separators, the Saint-Gouard notation) to the foot |
| 96 | f.92v cipher, full page | f.93r cipher, full page |
| 97 | f.93v cipher, full page | f.94r cipher, full page |
| 98 | f.94v cipher, full page | f.95r cipher, full page to about 85% of the page; at the foot a subscription-like mark ("subject ... Vivonne"), not explained at 1200 px (offset or a false start; check at native) |
| 99 | f.95v cipher for about 26 lines, then about 4 lines of plain French | f.96r about 7 lines plain French (the same report as the plain head of f.103v: "... le Turc ... quarante ou cinquante mil hommes ... Lombardye"), then the closing "Sire, je supplie le Createur donner a V[ost]re Ma[jes]té ... De Madrid ce iiij^me [?] de Juing 1573" and the signature; docket top left "4 Juin 1573" |
| 100 | f.96v address/endorsement leaf with seal traces, endorsed (vertical) "... 4 juing 1573" | f.97r new piece: heading "du s^r de S^t Gouard a la Reyne", docket "4 Juin 1573 Madrid", old ink no. "39" top right; plain French letter to the Queen ending "De Madrid ce iiij^me de Juing 1573", signed; no cipher seen |
| 101 | f.97v blank (show-through only) | f.98r blank |

Result: **a second copy of the 4 June 1573 letter to the King, partly in cipher with no decipherment leaf after it, ends on f.96r; its cipher block runs from the middle of f.92r to f.95v** (about 7.5 pages; by eye roughly 35-40 lines per full page, so about 250-280 cipher lines -- an estimate, not a count). Ink no. 39 is the 4 June letter to the Queen at f.97r and ink no. 40 the cipher letter at f.99 (N4-VIV2), so this piece, immediately before 39, is ink no. 38 by sequence -- **inferred (grade I): the "38" itself was not seen**, since it would stand on the piece's first leaf, before f.91v (canvas 94 or earlier, not fetched; the 7-request budget was spent on 95-101). This matches Gachard XXXVIII ("4 juin 1573, en partie chiffrée, sans le déchiffrement"): plain head, cipher middle, plain postscript and closing, no clerk's leaf. Its closing passage is the same as the plain head of f.103v (the ink-40 copy), so the two are copies of one letter, as Gachard's footnote says; the clerk's decipherment ff.104r-108v ("dechiffré de la precedente") is therefore the plaintext of both cipher blocks, subject to the textual differences Tomokiyo warns of between twin copies (N4-VIV2 caution).

**(2) f.104r legibility (native crop):** `python3 tools/iiif_lines.py --ark btv1b9009663p --canvas 107 --region 4300,900,3800,1100 --out ciphers/fr16104-vivonne-spain-1572/images --prefix c107_f104r --debug` -> "region 3800x1100, 4 lines, 4 bands x 2 segments; pitch 154 distance 107 prominence 17.4; centres (region y): 192 424 583 829; wrote 8 crops" (canvas 107 native is 8277 x 5962). Prominence 17.4 against 155 on the f.173 date crop of fr.16104 (same tool, same day) measures how faint the ink is. Viewed with autocontrast (1% cutoff) at half scale: about 7 text lines are visible as word shapes, no word can be read with confidence. **Verdict: f.104r (the first page of the decipherment, about one page of 9.5) is illegible in the Gallica scan, at native resolution and with contrast stretching; ff.104v-108v are legible** (N4-VIV2 read f.108v's last paragraph and c111's ff.107v-108 by eye at 1200 px). f.104r is a gap of about 10% of the decipherment's plaintext -- the plaintext of the start of each cipher block -- and needs a better image (BnF reproduction, or a multispectral/UV capture) or must be left as a gap.

**(3) Facts for the transcription + alignment brief (not run here):**
- Cipher block A, ink 38 (no period decipherment beside it): fr.16105 f.92r (lower half) - f.95v (about 26 lines), canvases 95 right - 99 left, about 7.5 pages, ~250-280 lines.
- Cipher block B, ink 40 (the f.99 copy): ff.100-103r, canvases 103-107 (N4-VIV/N4-VIV2), ~240 lines by eye.
- Plaintext, ink 41: ff.104r-108v, canvases 107 right - 112 left; f.104r illegible (above), ff.104v-108v legible plain French in a widely spaced clerk's hand, about 8.5 pages.
- Key: Tomokiyo's table is NOT on disk as data -- sources/cryptiana/web/henryiii.htm references henryiii_Vivonne1.png ... Vivonne6.png and VivonneSig.png (line 203 onward) but none of the PNGs is in sources/cryptiana/web/ (checked by `find sources -iname "*vivonne*"`, 4 Oct 2026). They must be fetched from cryptiana.web.fc2.com once and turned into key.tsv (one vision read per image, ~1-2 images for the alphabet + nomenclator).
- Best anchor: the END of the blocks, not the start. The cipher block's last lines (f.95v of block A, f.103r of block B) should read as the decipherment's last paragraph, already read by eye on f.108v ("... Le filz dudict prince est tousjours estudiant en Arcala ... de ses necessitez"); the start is anchored to the illegible f.104r and is the wrong place to test.
- Per-pass estimate (CLAUDE.md Usage 6, priced per subagent call at the AX-COMP2 rate of ~USD 1.5 per Sonnet one-page call; 2 blind passes + 1 reconciliation = 3 units per page): one cipher page ~USD 4.5; block A whole ~7.5 pages ~USD 34; decipherment ff.104v-108v one pass per page (plain French, checked by the alignment) ~8.5 calls ~USD 13; key PNGs to key.tsv ~USD 3. Cheapest real test: key on disk (~3) + f.95v cipher page (~4.5) decoded with tools/decode_key.py against f.108v's read paragraph, ~USD 8, with a matched control (the same page decoded under a shuffled key) for the agreement statistic, pre-registered.

Requests: gallica.bnf.fr 9 (7 x 1200 px openings c95-c101, all 200; 1 info.json for c107; 1 native region of c107), >= 2 s apart. Vision reads: 3 (two sheets, one crop). Subagent calls: 0. Cost: see the lane ledger.

## Remaining gaps (N4-VIV3 refresh, 4 Oct 2026)
Read so far: 26 of at least 28 flagged cipher letters (about 93%) carry a period decipherment per Gachard's flags; of the two "sans" letters, the fr.16105 one is ink piece 38 by sequence (cipher block ff.92r-95v, N4-VIV3), a second copy of the letter whose other copy ff.99-103v has its clerk's decipherment at ff.104r-108v (f.104r illegible in the scan); fr.16104 ff.157-159v (5 Sept 1572) has none located; unflagged cipher letters unmeasured.
- fr.16105 ink 38 cipher block ff.92r-95v (Gachard XXXVIII) - blocker: not-attempted; located (N4-VIV3), plaintext available as ff.104v-108v of the ink-41 decipherment, key not yet on disk; next: fetch Tomokiyo's henryiii_Vivonne PNGs and build key.tsv, transcribe f.95v (2 blind passes + reconciliation) and decode against f.108v's last paragraph with a shuffled-key control, ~$8
- fr.16105 f.104r, first page of the ink-41 decipherment - blocker: illegible; native Gallica crop with autocontrast shows word shapes only (N4-VIV3, prominence 17.4); a BnF reproduction or multispectral image would be needed
- fr.16104 5 Sept 1572 cipher block (ff.157-159v) - blocker: not-attempted; no decipherment located, no duplicate named by Gachard; next: transcribe the block (crops via tools/iiif_lines.py, two blind passes + reconciliation per page, 4 pages) and apply Tomokiyo's key once on disk as key.tsv, ~$18
- Unflagged cipher letters and letters lacking a clerk's leaf - blocker: not-attempted; Gachard's numerals appear to be the old ink piece numbers (N4-VIV2, consistent with ink 39 at f.97 seen by N4-VIV3); next: one 1200 px pass over fr.16104/16105 canvases with a per-letter table (ink no., cipher yes/no, decipherment leaf), ~$3
- Spanish-side copies (AGS Estado K) and Gachard vol. I - blocker: needs-physical-access; AGS is not digitised in a route this worker could open
## Escalation (4 Oct 2026, N4-VIV3)
- [x] siblings: ink 38 located at ff.~90-96r (cipher ff.92r-95v), twin of ink 40 ff.99-103v (N4-VIV3); fr.16106 f.207+ Longlée pool is scout row P2-B, a separate check
- [x] clear-pages: the decipherment of ff.99-103v found at ff.104-108v (N4-VIV2); both "sans" letters opened (N4-VIV, N4-VIV3)
- [ ] known-keys: Tomokiyo's table (henryiii_Vivonne1-6.png) is the known key; PNGs not on disk, not yet key.tsv nor applied; planned with the f.95v test
- [x] print: Gachard II, d'Ars, Catherine IV-V, Groen IV read (see top); phrase search on decoded text not possible before a reading exists
- [n/a] key-rebuild: a published key exists, rebuild is not needed unless it fails
- [x] image-check: canvases 95-101 viewed at 1200 px; f.104r at native resolution with contrast stretch (illegible) (N4-VIV3)
- [ ] retry: ink 38's first leaf (canvas 94 or earlier) not yet viewed to see the "38" itself; one 1200 px request
Verdict: keep going: 3 internal gaps; cheapest next: Tomokiyo key PNGs to key.tsv + f.95v cipher page decoded against f.108v's read paragraph with a shuffled-key control, ~$8

## N5-VIVK (4 Oct 2026, LANE-NEAR5 worker, account 2): known-plaintext test of the 4 June 1573 cipher letter (ink 40) against its clerk decipherment (ink 41)
Brief: .claude/briefs/runs/2026-10-04-ytbiz-near5-wave1.md "N5-VIVK". Intake gate rc=0 (pasted by LANE-NEAR5). PREREG-N5VIVK.md pushed
(4410086c) before any decode of f.103r existed; amendment 1 (a52d5574, plaintext widened to f.105v on training-side evidence) also before.

**Key on disk.** Tomokiyo's key images fetched once from cryptiana.web.fc2.com/code/ into sources/cryptiana/web/ (unmodified:
henryiii_Vivonne1.png = the April 1572 - Nov 1574 Saint-Gouard cipher; Vivonne2-6 = later ciphers, VivonneSig = a signature, kept for
completeness). key_tomokiyo.tsv = Vivonne1's alphabet mapped by eye onto the transcription labels of tx/SIGNS.md (30 codes; a few of
Tomokiyo's homophones and nulls have no separate label). Key source: `published` (S. Tomokiyo, Cryptiana, henryiii.htm "Vivonne in Spain").

**Crops** (pasted per CLAUDE.md Usage 6; debug overlays checked, red centres on the lines; a first 2400 px-segment cut was discarded
because its two segments overlapped by ~1750 px):
```
$ python3 tools/iiif_lines.py --ark btv1b9009663p --canvas 105 --region 4820,380,2950,4850 --out ciphers/fr16104-vivonne-spain-1572/images --prefix c105_f102r --follow-slope 400 --distance 60 --max-width 1600 --overlap 150 --debug
  region 2950x4850, 37 lines, 37 bands x 2 segments; pitch 112 distance 60 prominence 186.2; wrote 74 crops
$ python3 tools/iiif_lines.py --ark btv1b9009663p --canvas 106 --region 1200,520,2980,4500 --out ciphers/fr16104-vivonne-spain-1572/images --prefix c106_f102v --follow-slope 400 --distance 60 --max-width 1600 --overlap 150 --debug
  region 2980x4500, 37 lines, 37 bands x 2 segments; pitch 111 distance 60 prominence 192.3; wrote 74 crops
$ python3 tools/iiif_lines.py --ark btv1b9009663p --canvas 106 --region 4950,300,3050,4700 --out ciphers/fr16104-vivonne-spain-1572/images --prefix c106_f103r --follow-slope 400 --distance 60 --max-width 1600 --overlap 150 --debug
  region 3050x4700, 40 lines, 40 bands x 2 segments; pitch 104 distance 60 prominence 205.5; wrote 80 crops (L38-L40 = plain subscription "Je baise ...", excluded)
```
Slope-tracked bands produced duplicate lines (readers marked DUP: f.102r L14; f.102v L31, L33, L37; f.103r L27) -- so up to five real
lines may be missing from the transcription (not re-cut; see gaps). Decipherment pages ff.105v-108v (canvas 109 left - 112 left): line
detection missed lines on the widely spaced hand and would have pushed images/ past 30 MB, so they were read from scratch strips
(native region fetch, 7-8 horizontal strips cut at ink minima, each in two halves with 400 px shared), not committed; regenerate with
the regions L=700,150,3600,5650 / R=4200,150,3950,5650 at native size.

**Cipher transcription** (two blind Sonnet passes per page, `tools/reconcile_passes.py`, then tx/reconcile_vivk.py: six label rules
settled by eye on f.102r/f.102v crops -- S/s -> s, c/: -> :, 4/{t} -> 4, y/V -> y, z/r -> z, x/r -> x -- all other splits left at pass A):
| page | signs (reconciled) | err_2reader (DUP lines excluded) | splits settled by rule | splits left at pass A | one-pass gaps |
|---|---|---|---|---|---|
| f.102r | 1849 | 0.083 | 26 | 66 | 61 |
| f.102v | 1862 | 0.226 | 125 | 121 | 175 |
| f.103r | 2034 | 0.101 | 2 | 105 | 98 |
err_2reader is two-reader disagreement, not err_true (no benchmark item for this hand). f.102v's high figure is mostly one reader
writing S for the short s throughout; after the label rule the residual is about 0.16.

**Plaintext** (two blind Sonnet passes per page, merged by tx/merge_dec.py: A/B word agreement 0.66-0.71 per page -- the clerk's hand is
hard; normalized per PREREG to tx/dec_norm.txt, 9,554 letters, ff.105v-108v). Not an edition-quality reading: about a third of the words
differ between the two passes.

**Result (tx/vivk_test.py, PREREG statistic, 200 draws per null, rng 20261004; tx/vivk_result.json):**
anchor j0 = 1265 (score 0.463; f.102r begins about 92% of the way down f.105v); training 3,524 codes; held-out f.103r 1,945 codes; H = 4,781 letters.
| arm | real | coverage of f.103r codes | shuffled-key null median / p95 | shuffled-order null median / p95 | verdict |
|---|---|---|---|---|---|
| A: stream_align from flat start on f.102r+f.102v, key frozen | 0.434 | 0.993 | 0.376 / 0.428 | 0.427 / 0.448 | FAIL |
| B: Tomokiyo's published key, no training | 0.545 | 0.910 | 0.288 / 0.340 | 0.348 / 0.362 | PASS |
No null median near ceiling (all < 0.43), so neither arm is void. Arm A's frozen key agrees with Tomokiyo's on 2 of 30 codes with >= 3
training occurrences (list in vivk_result.json): the learner did not lock on, so its "disagreements" are not data conflicts. A post-hoc
diagnostic (tx/vivk_diag_slope.py, NOT pre-registered, no gate) restarted it at the observed 1.52 letters per sign instead of 1.0: 0 of 30
agree. Arm A is logged as **untested-by-this-tool** (tools/stream_align.py, flat start, on a noisy two-sided transcription with ~1.5 plaintext
letters per cipher sign), not as evidence against the key.
By eye (interpretation, not a gate): Arm B's held-out decode of the last lines of f.103r reads "... ung iour tout seul faisant une reconciliation
avecques ses subiectz mais l'on ... nulle esperance voulloir entendre a nul partie ... le filz dudict prince est tousiours estudiant en Alcala
avecques toute liberte ... de ses necessitez", which is the decipherment's closing paragraph on f.108v (N4-VIV2). So the cipher block ends where
the decipherment ends, and the decipherment is the plaintext of ff.100-103r (no longer only grade I).

**key.tsv** (tx/key_support.py, reproducible): Tomokiyo's 30 values; each code's support = how often the decipherment letter aligned to it (whole
stream f.102r-103r against dec_norm[j0:], same DP as nw_score) equals the value. 4,487 keyed signs aligned, 2,616 match (0.583, a floor: both
transcriptions are noisy). 26 codes graded C (the key value is the top aligned letter, >= 3 matches), 4 graded M and listed, not settled (rule 4):
S=b (top aligned a: one pass wrote S for the short s), y=h (aligned l/r/h about evenly: the y label likely merges the swash lead-in glyph with y),
b=z (0 of 13) and A=c (2 of 5, top aligned c tied with p and a -- too few to grade). Codes outside the key: V 147, c 86, 2 55, o 54 (others under 15) -- labels the readers used for glyphs
Tomokiyo's table names differently or for nulls; not mapped.
Grade counts for the held-out page under Arm B (published key, checked against the decipherment): no H; C-supported values cover 0.91 of f.103r's codes;
this is a check of the published key against the period decipherment, not a reading of an unread text.

Not done (brief step 5: stop here): applying key.tsv to fr.16104 ff.157-159v (wave 2); ink 38 (ff.92r-95v) not touched.
Requests: gallica.bnf.fr about 27 (2 x 1600 px openings c105/c106, 4 x c109-c112, 1 info.json, 15 native regions incl. re-fetches after the
tool downscaled its cached sources, 1 connection reset on c112 not retried until later), all >= 2 s apart; cryptiana.web.fc2.com 7 (1.6 s apart).
Subagent calls: 20 Sonnet (6 cipher passes, 14 decipherment passes). Cost: see the lane ledger.

## Remaining gaps (N5-VIVK refresh, 4 Oct 2026)
Read so far: 26 of at least 28 flagged cipher letters carry a period decipherment per Gachard; ink 40 (ff.100-103r) is now checked against its
decipherment ink 41 with Tomokiyo's published key (held-out PASS, N5-VIVK); ink 38 (ff.92r-95v) is its twin copy; fr.16104 ff.157-159v (5 Sept 1572)
has no decipherment located; unflagged cipher letters unmeasured.
- fr.16104 5 Sept 1572 cipher block (ff.157-159v) - blocker: not-attempted; key.tsv now checked on ink 40 (N5-VIVK); next: crops + two blind passes per page against tx/SIGNS.md (fix the S/s and y labels first), decode with tools/decode_key.py or tx/key_support.py's decode, judge fr16, ~$12
- Transcription labels S, y, b, V, c, 2 - blocker: not-attempted; the four M codes and the unmapped labels come from the passes' inventory, not the key; next: one look-alike pass (tools/lookalike_pass.py) on f.102v/f.103r crops for those labels, then re-run tx/key_support.py, ~$3
- Missing duplicate-band lines (up to 5 lines, the DUP rows) - blocker: not-attempted; the slope-tracked bands fitted the same line twice; next: re-cut those bands with --centres from the debug overlays, one pass each, ~$2
- fr.16105 f.104r, first page of the decipherment - blocker: illegible; native crop shows word shapes only (N4-VIV3)
- Unflagged cipher letters and letters lacking a clerk's leaf - blocker: not-attempted; Gachard's flags cover only the letters he analysed; next: one 1200 px pass over fr.16104/16105 with a per-letter table, ~$3
- Spanish-side copies (AGS Estado K) and Gachard vol. I - blocker: needs-physical-access; AGS is not digitised in a route this worker could open
## Escalation (4 Oct 2026, N5-VIVK)
- [x] siblings: ink 38 located (N4-VIV3); ink 40 vs ink 41 aligned (N5-VIVK); fr.16106 f.207+ Longlée pool is scout row P2-B
- [x] clear-pages: decipherment ff.104-108v is the plaintext of ff.100-103r (N5-VIVK: f.103r's last lines read as f.108v's last paragraph under the published key)
- [x] known-keys: Tomokiyo's 1572-74 key on disk (key_tomokiyo.tsv, key.tsv) and held-out PASS against the period decipherment (N5-VIVK, 0.545 vs null p95 0.362)
- [x] print: Gachard II, d'Ars, Catherine IV-V, Groen IV read (see top)
- [retired] key-rebuild: tools/stream_align.py from a flat start did not converge on this material (Arm A, 2 of 30 codes; slope diagnostic 0 of 30); a published key exists
- [x] image-check: canvases 95-101, 105-106, 109-112 viewed; f.104r illegible (N4-VIV3)
- [ ] retry: fr.16104 ff.157-159v with key.tsv (wave 2 of LANE-NEAR5)
Verdict: keep going: 4 internal gaps; cheapest next: fr.16104 ff.157-159v transcribed against tx/SIGNS.md and decoded with key.tsv, ~$12

Gate output (N5-VIVK, 4 Oct 2026): `OK keep-going fr16104-vivonne-spain-1572: keep going: 4 internal gap(s), 1 step(s) untried`

## N5-VIV5S (4 Oct 2026, LANE-NEAR5 worker, account 2): premise check on the 5 Sept 1572 letter -- a clerk decipherment exists (ff.162r-163r); stopped at step 0
Brief: .claude/briefs/runs/2026-10-04-ytbiz-near5-wave1.md "N5-VIV5S", step 0 ("If one exists, stop after recording it ... the test becomes
a known-plaintext check like N5-VIVK and is a separate brief"). No crops, no transcription, no decode, no subagent calls, no PREREG.

**Found: "dechiffré de la precedente", dated 5 Sept 1572, on f.162r (canvas 176, right page), two leaves after the letter.**
- f.162r head (native crop images/c176_f162r_head.jpg, region 4000,150,4100,700 of canvas 176, manifest.json "premise_n5viv5s"):
  later docket top left "5 Septemb / 1572"; heading in the clerk's hand "dechiffré de la precedente"; old ink piece number "51" before
  the stamped folio "162" top right. The letter ff.157-159v is Gachard's L, i.e. old ink piece 50 if N4-VIV2's rule (Gachard's roman
  numeral = the old ink number) holds here too; the decipherment is the next piece, 51. The next leaf, f.164 (canvas 178), carries
  "52" and is a separate full-cipher letter "du S^r de S^t gouard a la Reyne", docket "5 Septembre 1572".
- f.161v (canvas 176, left page) is the letter's address leaf, endorsed in the margin "... S^t Goard au Roy / 5 septembre 1572";
  ff.160-161 (canvases 174-175) carry the letter's end (f.159v: last ~17 cipher lines, the closing "De Madril ce v^me jo[ur] de
  sept[em]b[re] 1572" and signature, N4-VIV) and a blank leaf with the seal trace.
- Decipherment text, by eye at 1200 px plus the native head crop (not transcribed): plain French in a widely spaced clerk's hand on f.162r
  (~26 lines), f.162v (~26 lines) and f.163r (~25 lines, three paragraphs, ending about two-thirds down the page). Opening: "Je fus
  conduit en ceste audience pour les soubçons de leurs depportemens et preparatifs, et aussi de la bonne continuance d'iceluy qu'ils ont
  pour les advertissements ..." -- it continues the account of the 27 August audience that Gachard's L summarises from the plain
  part (Gachard II p.592-593, quoted passages all plain French: "Nonobstant cela ... l'audience ... pour le vingt-septiesme du passé",
  Longueville, the duc d'Alve's suspicion, the troop routed near Mons). Names legible on f.162r-163r at 1200 px: "M. l'Admiral",
  "la Religion nouvelle", "Flandres", "le duc d'Alve", "Millan", "Don Joan d'Austria", "la Hollande", "Amsterdam", "Utrecht", "Grenade",
  "S^t Hieronyme", "l'Escurial".
- So Gachard's flag on L, "(En partie chiffrée, sans le déchiffrement.)", is not borne out on the leaves: the letter's period decipherment
  is filed as the next piece. Gachard's next numbered entries after L are the 12 Sept letter (numeral lost in the OCR) and LV-LVI
  (19 Sept, "avec le déchiffrement"); he gives no entry for piece 51. The 5 Sept 1572 cipher block is therefore **not an unread text**:
  the step that remains is a known-plaintext check of key.tsv on it, as N5-VIVK did for 4 June 1573 (separate brief, per step 0).
- **Open question for that brief (observation, not measured):** the decipherment looks short for the cipher block. By eye it is ~2.5
  pages of a large hand (~75 lines), while N4-VIV estimated 150-175 cipher lines for ff.157r (lower third)-159v; in fr.16105 the ratio
  ran the other way (~9.5 decipherment pages for ~5.5 cipher pages, N5-VIVK: 9,554 plaintext letters for ~5,700 cipher signs). Either
  N4-VIV's line estimate is high (the block may hold more plain French than the thumbnails showed), or the decipherment covers only
  part of the cipher block (a second "dechiffré" leaf elsewhere, or part left undeciphered). First step of the next brief: count the
  cipher lines on canvases 170-173 and the decipherment's letters, then align the decipherment's first and last sentences to cipher
  lines with key.tsv before transcribing everything.

Requests: gallica.bnf.fr 8 (7 x 1200 px openings, canvases 174-180, all viewed but 179-180; 1 native region of canvas 176), all >= 2.5 s apart,
all HTTP 200; archive.org 1 (Gachard II djvu.txt, labibliothquen02gachuoft, for entry L and its neighbours). Subagent calls: 0. Cost: see the
lane ledger. Canvases 179-180 (ff.164v-165, the 5 Sept letter to the Queen) were fetched but not needed once f.162 was found.
Suggestion (not done, Usage 7): the 5 Sept 1572 letter to the Queen, f.164 (old piece 52, full cipher), needs its own decipherment check
(Gachard's entry for it, if any, and the leaves after it).

## Remaining gaps (N5-VIV5S refresh, 4 Oct 2026)
Read so far: 27 of at least 28 flagged cipher letters carry a period decipherment on the leaves (Gachard's 26 "avec" plus the 5 Sept 1572 letter,
whose decipherment ff.162r-163r N5-VIV5S found despite Gachard's "sans"); ink 40 (fr.16105 ff.100-103r) checked against its decipherment with
Tomokiyo's published key (held-out PASS, N5-VIVK); ink 38 (ff.92r-95v) is its twin copy; unflagged cipher letters unmeasured.
- fr.16104 5 Sept 1572 cipher block (ff.157-159v) against its decipherment ff.162r-163r - blocker: not-attempted; decipherment found at step 0 (N5-VIV5S), so the job is a known-plaintext check, not a reading; next: count cipher lines (c170-173) vs decipherment length, then crops + two blind passes per page against tx/SIGNS.md, decipherment read twice, key.tsv decode aligned as in tx/vivk_test.py, ~$15
- fr.16104 f.164 letter to the Queen, 5 Sept 1572 (old piece 52, full cipher) - blocker: not-attempted; seen at 1200 px only (N5-VIV5S); next: Gachard II entry for it and the leaves after f.165 for a "dechiffré", ~$1
- Transcription labels S, y, b, V, c, 2 - blocker: not-attempted; the four M codes and the unmapped labels come from the passes' inventory, not the key; next: one look-alike pass (tools/lookalike_pass.py) on f.102v/f.103r crops for those labels, then re-run tx/key_support.py, ~$3
- Missing duplicate-band lines (up to 5 lines, the DUP rows) - blocker: not-attempted; the slope-tracked bands fitted the same line twice; next: re-cut those bands with --centres from the debug overlays, one pass each, ~$2
- fr.16105 f.104r, first page of the decipherment - blocker: illegible; native crop shows word shapes only (N4-VIV3)
- Unflagged cipher letters and letters lacking a clerk's leaf - blocker: not-attempted; Gachard's flags cover only the letters he analysed and his "sans" flag on L proved wrong; next: one 1200 px pass over fr.16104/16105 with a per-letter table (cipher yes/no, old piece number, "dechiffré" leaf), ~$3
- Spanish-side copies (AGS Estado K) and Gachard vol. I - blocker: needs-physical-access; AGS is not digitised in a route this worker could open
## Escalation (4 Oct 2026, N5-VIV5S)
- [x] siblings: ink 38 located (N4-VIV3); ink 40 vs ink 41 aligned (N5-VIVK); 5 Sept 1572 decipherment (piece 51, ff.162r-163r) found (N5-VIV5S); fr.16106 f.207+ Longlée pool is scout row P2-B
- [x] clear-pages: decipherments ff.104-108v (fr.16105) and ff.162r-163r (fr.16104) are on the leaves
- [x] known-keys: Tomokiyo's 1572-74 key on disk (key_tomokiyo.tsv, key.tsv) and held-out PASS against the period decipherment (N5-VIVK, 0.545 vs null p95 0.362)
- [x] print: Gachard II, d'Ars, Catherine IV-V, Groen IV read (see top); Gachard II entry L re-read for N5-VIV5S
- [retired] key-rebuild: tools/stream_align.py from a flat start did not converge on this material (Arm A, 2 of 30 codes; slope diagnostic 0 of 30); a published key exists
- [x] image-check: canvases 95-101, 105-106, 109-112 (fr.16105) and 170-178 (fr.16104) viewed; f.104r illegible (N4-VIV3)
- [ ] retry: fr.16104 ff.157-159v with key.tsv against its decipherment ff.162r-163r (known-plaintext check, separate brief)
Verdict: keep going: 5 internal gaps; cheapest next: Gachard II entry and following leaves for the f.164 letter to the Queen, ~$1

## N5-VIVTAB (4 Oct 2026, LANE-NEAR5 worker, account 2): per-piece table of fr.16104/16105 -- which cipher pieces lack a clerk decipherment
Brief: .claude/briefs/runs/2026-10-04-ytbiz-near5-wave1.md "N5-VIVTAB". No transcription, no decode, no subagent calls. Output: `piece_table.tsv`
(76 rows: Gachard's entry headers for both volumes, plus every piece seen on the leaves by this and earlier workers).

**Scope actually covered (not the full pass the brief asked for).** Gallica's IIIF answered at 60-118 s per 1200 px image from 07:48 to about
08:04 UTC (two dropped connections), so the planned 266-image sweep (every second canvas of both volumes) was stopped after 2 requests and replaced
by targeted openings; when the server sped up (1-10 s) the tail of fr.16105 was swept. Viewed at 1200 px by this worker: fr.16104 c182, c184,
c186, c187, c188 (= c189, a second capture of the same opening), c190, c191; fr.16105 c192, c194-c200, c202, c204, then c206-c248 every second
canvas (read on contact sheets of six). **Not viewed: fr.16104 c1-c169 and c192-c324 (except the single canvases earlier workers list), fr.16105
c1-c94 and c113-c191 (except N4-VIV's bisection canvases).** Gachard's printed headers stand in for those stretches only where he gives an entry.

**From Gachard II (IA labibliothquen02gachuoft djvu.txt, entry headers pp.362-454, grepped and read by eye):** vol. I (= fr.16104) is ink pieces
I-CI, vol. II (= fr.16105) I-LXXIII (his own count; the leaves run to 77). Gachard analyses about 37 pieces of vol. I and 29 of vol. II and gives
cipher pieces a double number when the decipherment follows (his own rule, stated for the 1581-82 volume of the same series). His "sans le
déchiffrement" flags in these two volumes: **L (5 Sept 1572), XXXVIII (4 June 1573) and LXIII (10 Oct 1573)**; the 3 Oct 2026 count of "2" missed
LXIII (OCR "cliiffrée ... décliijlremenl"). Not in these volumes but noted: vol. III (fr.16106) XLIV is a "Déchiffrement d'une lettre à la reine,
du 7 septembre 1574" printed without its cipher piece (the reverse case).

**Found on the leaves:**
- **fr.16105 ink 63, 10 Oct 1573, to the King (Gachard LXIII, "sans"): no decipherment.** f.187r (canvas 192) docket "10 Octobre 1573 Madrid",
  heading "du S^r de S^t Gourd au Roy"; ff.187r-189v plain French (the passport asked for the King of Poland, Çayas, the audience of S^t Michel --
  Gachard's summary); cipher from the head of f.190r to about line 20 of f.194r, then a few plain lines and the closing "de Madrid ce x^me jour
  d'octobre 1573", signed (canvases 195-199). About 8.5 dense pages of cipher, ~340 lines by eye (estimate, not counted). No interlinear gloss
  seen. f.194v is its address leaf; the next pieces are 64 (f.195r, a short plain letter of the same day to the King), 65 (f.197r, plain, to the
  Queen), 66 (f.199r, a Spanish letter of the marqués de Mondéjar, Perpignan, 12 Oct), 67 (20 Oct, cipher) with its own decipherment 68 ("dechiffré
  de la precedente", opening "Sire, Encores que ...", the same as 67's). No piece from 64 to the end of the volume (77, c248) is a decipherment of 63.
  Gachard's flag is borne out here, unlike his flag on L.
- **fr.16104 ink 52, 53 and 54: three cipher pieces with no decipherment piece next to them, none analysed by Gachard** (his entries jump from
  L to LV-LVI):
  - 52, 5 Sept 1572, to the Queen, full cipher ff.164r-168r (canvases 178-182; c182 = ff.167v-168r full cipher), address leaf f.169v endorsed
    "5 Septembre 1572". About 9 pages, ~270 lines est. (c179 and c181 not viewed).
  - 53, 5 Sept 1572, "du S^r de S^t gouard au Duc d'Anjou", f.170r: six plain lines then cipher; f.171v ~22 cipher lines, then "de Madril ce
    v^me de Sept 1572", signed; f.172r address leaf. ff.170v-171r (c185) not viewed; ~100 lines est. if they are cipher.
  - 54, 7 Sept 1572 (docket and closing "vij^e de Sept 1572"), "du S^r de S^t gouard au Roy", f.173r: three plain lines then cipher to f.173v
    (~50 lines est.), signed; f.174 address leaf endorsed 7 Sept 1572. **A few cipher groups on f.173r-v carry small interlinear words** (not
    read at 1200 px): a partial period gloss, to be read at native resolution before this piece is treated as unread.
  - Then ink 55 (f.175r, 19 Sept 1572, Gachard LV-LVI "avec"). RUN1-VIV2's "c190 = f.179" is f.175 (stamped folio read at c190 right).
  So the 5-7 Sept 1572 group is four cipher letters (50, 52, 53, 54) and one decipherment (51, of 50). Whether any of 52-54 has a decipherment
  filed elsewhere (as fr.16106's XLIV shows can happen) was not checked.
- fr.16105 tail confirmed as Gachard implies: 70 -> 71 "dechiffré de la precedente" (4 Nov 1573); 74 (13 Dec) and 75 (Dec, full cipher) -> 76
  "dechiffré de la precedente". Whether 76 covers both 74 and 75 (twin copies, as 38/40) was not checked.

**Result: cipher pieces in fr.16104/16105 with no decipherment leaf located (each a candidate for a later read with key.tsv):**
| volume | ink | date | to | cipher folios (canvases) | est. cipher lines | note |
|---|---|---|---|---|---|---|
| fr.16105 | 63 | 10 Oct 1573 | King | f.190r-194r (195-199) | ~340 | Gachard LXIII "sans"; no decipherment to the end of the volume |
| fr.16104 | 52 | 5 Sept 1572 | Queen | ff.164r-168r (178-182) | ~270 | not in Gachard |
| fr.16104 | 53 | 5 Sept 1572 | duc d'Anjou | ff.170r-171v (184-186) | ~100 | not in Gachard; c185 unseen |
| fr.16104 | 54 | 7 Sept 1572 | King | f.173r-v (187-188) | ~50 | not in Gachard; a few interlinear words |
| fr.16105 | 38 | 4 June 1573 | King | ff.92r-95v (95-99) | ~250-280 | twin of 40, whose decipherment 41 exists (N4-VIV3, N5-VIVK) |
Line counts are estimates by eye at 1200 px, not counts. The unviewed stretches (above) may hold more.

Requests: gallica.bnf.fr 47 (2 dropped by the stopped sweep; 4 endpoint/timing tests including .lowres/.medres; 40 by the targeted queue,
39 x 200 + 1 dropped connection; 1 retry of c196, 200), one at a time, >= 2 s apart; archive.org 1 (Gachard II djvu.txt). Vision reads: 18
(single openings and contact sheets). Subagent calls: 0. Cost: see the lane ledger. Committed evidence sheets (downscaled 700 px):
images/n5vivtab_fr16104_c184-190_sheet.jpg (c184, c187, c188, c190), images/n5vivtab_fr16105_c192-202_sheet.jpg (c192, c196, c199, c202).

## Remaining gaps (N5-VIVTAB refresh, 4 Oct 2026)
Read so far: of the cipher pieces seen on the leaves, these carry a period decipherment: 40 (by 41), 43 (44), 67 (68), 70 (71), 74/75 (76) in
fr.16105 and 50 (51) in fr.16104, plus Gachard's double-numbered "avec" entries; ink 40 checked against 41 with Tomokiyo's key (held-out PASS,
N5-VIVK). Pieces with no decipherment located: fr.16105 63, fr.16104 52, 53, 54 (and 38, whose twin is deciphered).
- fr.16105 ink 63 (10 Oct 1573) cipher block ff.190r-194r - blocker: not-attempted; no decipherment in the volume (N5-VIVTAB), Tomokiyo's key checked on ink 40; next: crops + two blind passes per page against tx/SIGNS.md, decode with key.tsv, judge fr16, ~$15-20 (8.5 pages)
- fr.16104 inks 52, 53, 54 (5 and 7 Sept 1572) - blocker: not-attempted; no decipherment piece beside them (N5-VIVTAB); next: native crop of f.173r-v's interlinear words (piece 54) and a look at c179/c181/c185, then the smallest (54, ~50 lines) read with key.tsv as the first test, ~$1 to inspect, ~$6 to read 54
- fr.16104 5 Sept 1572 cipher block (ff.157-159v) against its decipherment ff.162r-163r - blocker: not-attempted; known-plaintext check, not a reading; next: count cipher lines (c170-173) vs decipherment length, then crops + two blind passes against tx/SIGNS.md, key.tsv decode aligned as in tx/vivk_test.py, ~$15
- Unviewed stretches of the per-piece table (fr.16104 c1-c169, c192-c324; fr.16105 c1-c94, c113-c191) - blocker: not-attempted; Gallica answered at ~90 s per image for part of this job; next: the same pass at 1200 px every second canvas, contact sheets of six, when the server answers in seconds, ~$3
- Transcription labels S, y, b, V, c, 2 - blocker: not-attempted; the four M codes and the unmapped labels come from the passes' inventory, not the key; next: one look-alike pass (tools/lookalike_pass.py) on f.102v/f.103r crops, then re-run tx/key_support.py, ~$3
- Missing duplicate-band lines (up to 5 lines, the DUP rows) - blocker: not-attempted; the slope-tracked bands fitted the same line twice; next: re-cut those bands with --centres from the debug overlays, one pass each, ~$2
- fr.16105 f.104r, first page of the decipherment - blocker: illegible; native crop shows word shapes only (N4-VIV3)
- Spanish-side copies (AGS Estado K) and Gachard vol. I - blocker: needs-physical-access; AGS is not digitised in a route this worker could open
## Escalation (4 Oct 2026, N5-VIVTAB)
- [x] siblings: ink 38 located (N4-VIV3); ink 40 vs 41 aligned (N5-VIVK); 5 Sept 1572 decipherment 51 found (N5-VIV5S); per-piece table built for the stretches viewed, 4 undeciphered cipher pieces located (N5-VIVTAB)
- [x] clear-pages: decipherments 41, 44, 51, 68, 71, 76 are on the leaves
- [x] known-keys: Tomokiyo's 1572-74 key on disk (key_tomokiyo.tsv, key.tsv) and held-out PASS against the period decipherment (N5-VIVK, 0.545 vs null p95 0.362)
- [x] print: Gachard II, d'Ars, Catherine IV-V, Groen IV read (see top); Gachard II entry headers for vols I-II tabulated (N5-VIVTAB)
- [retired] key-rebuild: tools/stream_align.py from a flat start did not converge on this material (Arm A, 2 of 30 codes; slope diagnostic 0 of 30); a published key exists
- [x] image-check: fr.16105 c95-101, 105-106, 109-112, 192-248; fr.16104 c170-191 viewed at 1200 px; f.104r illegible (N4-VIV3)
- [ ] retry: fr.16104 ink 54 (~50 lines, 7 Sept 1572) and fr.16105 ink 63 (~340 lines, 10 Oct 1573) read with key.tsv; no decipherment located for either
Verdict: keep going: 6 internal gaps; cheapest next: native crop of fr.16104 f.173r-v (ink 54) interlinear words, then read ink 54 with key.tsv, ~$1 + ~$6

Gate output (N5-VIVTAB, 4 Oct 2026): `OK keep-going fr16104-vivonne-spain-1572: keep going: 6 internal gap(s), 1 step(s) untried`

## N5-VIV54 (4 Oct 2026, LANE-NEAR5 worker, account 2): ink piece 54 (7 Sept 1572, to the King, fr.16104 f.173r-v) read with key.tsv
Brief: .claude/briefs/runs/2026-10-04-ytbiz-near5-wave1.md "N5-VIV54". Started 08:35 UTC, box to 10:35 UTC.

**Step 0, premise (08:40 UTC).** Gachard II (IA labibliothquen02gachuoft djvu.txt, fetched once to scratch): grep for "septembre 1572"
gives only L (5 Sept, "sans") and the 12 Sept letter (his n.: filed as LIX-LX among 1573) and LV-LVI (19 Sept); no 7 Sept 1572 entry.
La Ferrière, Catherine IV (sources/ia-fulltext/print-check/lettresdecatheri04cathuoft_djvu.txt.gz): grep for "septiesme", "du vii",
"7 septembre" and all 30+ "Gouard" hits -- no reply or note naming a Saint-Gouard letter of 7 Sept 1572 (its p.108 note dates his first
post-St-Bartholomew report to 19 Sept). Leaves: c189 (1000 px) is a second capture of the c188 opening (f.173v | f.174r blank); c190 is
f.174v (address, endorsed "7 septembre 1572") | f.175r (ink 55, 19 Sept). No "dechiffre" leaf; no printed plaintext located. Proceed.

**Layout (c187, c188 at 1600 px).** f.173r: docket "7 Septembre 1572", heading "du S^r de S^t gouard au Roy", ink 54; two and a half plain
lines ("Sire, j'ay receu la depesche de v^re ma^te par le courrier Johan ... Monsieur ... receu par le roy de ... celle qu'il luy a pleu
me [escrire] du ... d'aoust") then cipher to the foot (L04-L27); f.173v: 20 cipher lines, then the plain closing "Sire, je supplie le
Createur donner a v^re ma^te ... de Madril ce vij^e de Sept 1572", signed. Interlinear words above some groups on both pages.

**Crops** (debug overlays checked: f.173r L01 is the initial's flourish / show-through, not a line; L02-L27 one band per written line,
no duplicate bands; f.173v L01-L20 one band per line):
```
$ python3 tools/iiif_lines.py --ark btv1b9009609w --canvas 187 --region 4150,1180,3750,3800 --out ciphers/fr16104-vivonne-spain-1572/images --prefix c187_f173r --follow-slope 400 --distance 90 --max-width 1600 --overlap 150 --debug
  region 3750x3800, 27 lines, 27 bands x 3 segments; pitch 138 distance 90 prominence 258.4; wrote 81 crops
$ python3 tools/iiif_lines.py --ark btv1b9009609w --canvas 188 --region 1250,750,3050,2900 --out ciphers/fr16104-vivonne-spain-1572/images --prefix c188_f173v --follow-slope 400 --distance 90 --max-width 1600 --overlap 150 --debug
  region 3050x2900, 20 lines, 20 bands x 2 segments; pitch 133 distance 90 prominence 226.7; wrote 40 crops
```
**Units, stated before the first subagent call:** 2 pages x (2 blind Sonnet passes + 1 reconciliation) = 6 units at ~USD 1.5 (N5-VIVK rate),
+ 1 gloss look at native resolution by this worker = ~USD 10.5 of the 12 cap; reconciliation is tx/reconcile_vivk.py's label rules plus
this worker's eye on listed splits only.

**Transcription** (4 blind Sonnet calls, one per page per pass, crop paths only; tx/viv54_clean.py drops [PLAIN:] stretches and writes pass
A's π as P; `tools/reconcile_passes.py` on the _c passes; tx/reconcile_vivk.py f173r f173v --viv54 = N5-VIVK's rules + one rule settled by
eye on f.173r L05 s1-s2: ':' vs 'o' for the small solid dots -> ':'; N5-VIVK's f102r/f102v/f103r outputs regenerate unchanged):
| page | lines | signs (reconciled) | err_2reader | splits settled by rule | splits left at pass A | one-pass gaps |
|---|---|---|---|---|---|---|
| f.173r | 24 cipher-bearing (L04-L27) | 1118 | 0.223 | 50 | 89 | 112 |
| f.173v | 20 | 934 | 0.193 (0.150 without L19-L20, which pass B could not read) | 4 | 74 | 102 |
f.173r L02/L03 crops are near-identical (mean pixel difference 5.5; no other neighbouring pair under 8): both are the plain "Monsieur ..."
line, so the plain "Sire, j'ay receu ..." line has no crop of its own -- no cipher lost. err_2reader is reader disagreement, not err_true.

**Interlinear words** (read by this worker at native resolution BEFORE any decode, 14 native strips; tx/glosses54.tsv): f.173r "n e le ..." and
"napaud?" over L07, "au faict" over L08's first group, "en ainsi" over L18; f.173v "nostre royau..?" over L08, "il ... peult/vault" over L11,
"peup" over L17, "e partisan contre" over L19. Four further marks are cipher signs written above the line with a caret ("Km", "^p", f.173r
L19/L23/L24): corrections of the cipher, not glosses. Several others are illegible (rows use=no).

**Gates (PREREG-N5VIV54.md, pushed d0c73a87 before any decode; tx/viv54_test.py, seed 20260958, 200 draws; tx/viv54_result.json):**
| gate | target (ink 54 under key.tsv) | control / null | verdict |
|---|---|---|---|
| (a) gloss check, mean LCS(gloss, decode window)/len | **0.609** (per gloss 1.00, 0.50, 0.71, 0.57, 0.27, 0.71, 0.50, 0.60) | shuffled-key null median 0.271, p95 0.354 | **PASS** (> p95 and >= 0.60; null not near ceiling) |
| (b) fr16 judge, 4-gram score per letter | -1.658 (N 1793; word cover 0.795) | positive control f.103r under key.tsv: -1.714, **FAILs** the judge (real_p05 -0.927); shuffled-key decodes median -2.120, p99 -1.767, 0/200 PASS | **judge not a gate** (rule 1 of the PREREG) |
Caveats on (a), stated plainly: the PREREG text says "7 rows" but the frozen tx/glosses54.tsv carries 8 use=yes rows; the statistic ran on the
8 frozen rows as the PREREG's procedure says. The margin over the null is wide (0.609 vs p95 0.354), the 0.60 floor is met by 0.009 only:
dropping the best gloss ("nele", 1.00) gives 0.553 (descriptive, not a gate). (b): the judge cannot tell the known-good f.103r decode (same
hand, key, length) from real text at this transcription noise, so its FAIL on ink 54 says nothing; descriptively ink 54 scores above the f.103r
control and above every shuffled-key decode.

**Reading** (tx/viv54_decode.py writes reading_piece54.tsv, `--check` passes; piece54_decode.txt = letters only). 1,990 tokens: **H 1,475**
(both readers agree or a label rule settled it, code graded C in key.tsv), **M 318** (an M code S/y/b/A, or an unsettled split / one-pass gap),
**U 197** (code not in key.tsv: V, c, 2, o ...); no C, no S. H here = read with a published key (Tomokiyo) whose values the clerk decipherment
checked on ink 40 (N5-VIVK), not a period decipherment of this letter. Stretches that read as French by eye (interpretation, not a gate):
f.173r L09 "...dangier...", L19 "...el grand...", L21 "toute [d]iligence de [f]aire ... toute", L22 "...[m]unition...", L25 "...[l]iberation...",
L26 "c'est au..."; f.173v L03 "tousiours ont doubte que c'este...", L05 "grand ... est ... dict avoir", L19 "...contre..." directly under the
gloss "partisan contre". The ': :' dot pair seems to stand for one c (decode "dicct", "ccest"): two readers wrote each dot as a sign, so the
decode doubles c; not corrected (would be a change to the key's labels, a later job). Most lines are still letter salad between such stretches.

**print_check** (phrases.txt, sources.tsv: Gachard II, Catherine IV, d'Ars, Groen IV; print-check.tsv): the listed sources hit only generic
words ("dict avoir", "munition du roi") in unrelated passages; the global searches return hundreds of generic hits for each common phrase. One
Google Books hit worth a look: Kervyn de Lettenhove, *Les Huguenots et les Gueux 1572-1576* (1884), for "saint gouard septembre 1572 chiffre"
-- not opened. Report: no printed plaintext of ink 54 found in the sources named; not found by this method on 4 Oct 2026. Novelty not classified.

Requests: gallica.bnf.fr 21 (c187, c188 at 1600 px; c189, c190 at 1000 px; 2 native regions by iiif_lines; 1 info.json; 14 native gloss
strips + 3 re-fetches wider), one at a time >= 2 s apart; archive.org 1 (Gachard II djvu) + print_check's archive.org 2, be-api 6,
googleapis 6, openalex 6, semanticscholar 6, crossref 6. Subagent calls: 4 Sonnet. Cost: see the lane ledger.

## Remaining gaps (N5-VIV54 refresh, 4 Oct 2026)
Read so far: ink 40 checked against its decipherment 41 with Tomokiyo's key (N5-VIVK PASS); ink 54 (7 Sept 1572) read with key.tsv, gloss
check PASS (0.609 vs null p95 0.354), judge not a gate, H 1,475 / M 318 / U 197 of 1,990 tokens, much of it still unreadable letter strings.
Pieces with no decipherment located: fr.16105 63, fr.16104 52, 53 (and 38, whose twin is deciphered).
- ink 54 clean reading - blocker: not-attempted; err_2reader 0.19-0.22 and the ': :' pair read as two signs leave long unreadable stretches; next: a third pass / tools/lookalike_pass.py on the split signs of f.173r-v, the ': :' pair as one sign, re-decode, ~$4
- Lattice decode of ink 63 with a learnt confusion matrix (VIV-LAT, 14 Oct 2026) - blocker: not-attempted; dev f.102r gained (fx lines 14/3, p 0.013, lam 2) but the confirm2 look FAILed (3/6, err 0.296 vs 0.291) with truth in the lattice for only 29/234 of the top-1 errors: untested-by-this-tool at this error; next: a reader step that puts the true sign among the candidates (a per-sign top-3 pass with probabilities on this hand, or a confusion matrix learnt per reader on the same reader set that reads the target), re-gated on confirm2 only with a new design, ~$6
- Judge calibration for this hand - blocker: not-attempted; the fr16 judge FAILs the known-good f.103r control at this noise; next: score a lower-noise control (the clerk decipherment's own text, or f.103r after a lookalike pass) to see whether the judge can gate at all, ~$2
- Kervyn de Lettenhove, Les Huguenots et les Gueux (1884) - blocker: not-attempted; Google Books hit for Saint-Gouard Sept 1572; next: find the IA copy and grep for "7 septembre" / "Saint-Gouard", ~$1
- fr.16105 ink 63 (10 Oct 1573) cipher block ff.190r-194r - blocker: not-attempted; no decipherment in the volume (N5-VIVTAB); next: crops + two blind passes per page against tx/SIGNS.md, decode with key.tsv, ~$15-20
- fr.16104 inks 52, 53 (5 Sept 1572) - blocker: not-attempted; no decipherment beside them (N5-VIVTAB); next: look at c179/c181/c185, then read 53 (~100 lines) with key.tsv, ~$8
- fr.16104 5 Sept 1572 cipher block (ff.157-159v) against its decipherment ff.162r-163r - blocker: not-attempted; known-plaintext check, not a reading; next: crops + two blind passes, aligned as tx/vivk_test.py, ~$15
- Unviewed stretches of the per-piece table - blocker: not-attempted; fr.16104 c1-c169, c192-c324 and fr.16105 c1-c94, c113-c191 not viewed (N5-VIVTAB); next: 1200 px pass every second canvas, contact sheets, ~$3
- fr.16105 f.104r, first page of the decipherment - blocker: illegible; native crop shows word shapes only (N4-VIV3)
- Spanish-side copies (AGS Estado K) and Gachard vol. I - blocker: needs-physical-access; AGS is not digitised in a route this worker could open
## Escalation (4 Oct 2026, N5-VIV54)
- [x] siblings: ink 38 located; ink 40 vs 41 aligned (N5-VIVK); decipherment 51 found (N5-VIV5S); per-piece table (N5-VIVTAB); ink 54 read (N5-VIV54)
- [x] clear-pages: decipherments 41, 44, 51, 68, 71, 76 are on the leaves; ink 54's own interlinear words used as a gloss check (N5-VIV54)
- [x] known-keys: Tomokiyo's 1572-74 key on disk and held-out PASS (N5-VIVK); applied to ink 54, gloss check PASS (N5-VIV54)
- [x] print: Gachard II, d'Ars, Catherine IV-V, Groen IV read; print_check on ink 54 phrases (N5-VIV54)
- [retired] key-rebuild: tools/stream_align.py from a flat start did not converge on this material (Arm A, 2 of 30 codes); a published key exists
- [x] image-check: fr.16104 c170-191 and fr.16105 c95-112, c192-248 viewed; f.173r-v at native resolution (N5-VIV54)
- [ ] retry: ink 54 re-transcribed (lookalike pass, ': :' as one sign) and re-decoded; fr.16105 ink 63 read with key.tsv
Verdict: keep going: 7 internal gaps; cheapest next: Kervyn (1884) grep, ~$1, then a lookalike pass on ink 54, ~$4

Gate output (N5-VIV54, 4 Oct 2026): `OK keep-going fr16104-vivonne-spain-1572: keep going: 7 internal gap(s), 1 step(s) untried`; `tx/viv54_decode.py --check`: reading_piece54.tsv up to date

## N6-KERV (4 Oct 2026, 10:3x UTC): Kervyn de Lettenhove, Les Huguenots et les Gueux, grep

Route: archive.org advancedsearch (title + creator) listed 16 items; the six-volume set `leshuguenotsetle01kerv` .. `leshuguenotsetle06kerv` (1883-85) was fetched once as `_djvu.txt` to scratch (not committed), 6 downloads + 1 search = 7 requests to archive.org, >= 2 s apart. Greps: "Gouard", "Saint-Gouard", "déchiffr", "chiffr", "5/7/8/9/10 septembre 1572", "10 octobre 1573" (and 8-11 octobre 1573), "Vivonne", "16104". Hits by volume ("Gouard" lines): v1 0, v2 31, v3 81, v4 11, v5 2, v6 21. The Google Books hit for "saint gouard septembre 1572 chiffre" is accounted for: it is the Saint-Gouard material in v3 ch. 1, "Après la Saint-Barthélemy" (leaf context lines 350-450 of the v3 djvu text).

Found:
- Kervyn quotes and cites Saint-Gouard letters dated 2 Sept 1572 (v3, note on Huguenot risings), 12 Sept 1572 (cited "Gachard, La Bibl. Nat. de Paris, t. II, p. 395"), 19 Sept 1572 (to Catherine, to the duc d'Anjou, and to the king; also "Groen, Suppl. p. 127"), then 15 Nov and 17 Nov 1572, 6 Jan, 22 Feb, 10 Mar (Gachard II p. 419), 6 Apr, 8 Jun, 9/17/30 Jul, 13/18 Aug, 20 Oct, 3 Nov 1573, and 1574 letters. Quote (v3, ch. 1): "il y joignit une lettre pour le duc d'Anjou où il glorifiait sa main et sa tête" (19 Sept 1572, to Anjou).
- He cites printed or archive copies (Gachard II, Groen, Arch. Nat. K. series, Simancas), not fr.16104 or any BnF fonds-français shelfmark; "Vivonne" and "16104" do not occur in the volumes' text as grepped.
- "chiffr" hits in v2-v6 concern other correspondents (Walsingham, Dale, Mansfeld, Marnix, d'Esquerdes, Espinosa); none is a Saint-Gouard cipher passage and none summarises a decipherment of a Saint-Gouard letter.

Not found: no passage in Kervyn's text dated 5 Sept or 7 Sept 1572 from Saint-Gouard (ink 53's date is 5 Sept; the nearest cited letters are 2 and 12 Sept), none dated 10 Oct 1573 (ink 63; nearest are 20 Oct and 3 Nov 1573), and nothing that prints or summarises inks 52, 53, 54 or 63 as a decipherment. Limits: OCR of one edition only; a variant date or a paraphrase without a date would not be caught by these greps; the volumes' index pages were not read. This is a search result for the log, not a novelty verdict (rule 10).

Follow-up (one line, not run): the 19 Sept 1572 and 12 Sept 1572 letters Kervyn cites are in Gachard II (already on file, `labibliothquen02gachuoft`) at p. 395 ff.; a page check there is the cheaper route to what Kervyn's 12 Sept note rests on.

## N6-VIV53 (4 Oct 2026, LANE-NEAR6 worker, account 2): ink piece 53 (5 Sept 1572, to the duc d'Anjou, fr.16104 ff.170r-171v) read with key.tsv
Brief: .claude/briefs/runs/2026-10-04-ytbiz-near6-wave1.md "N6-VIV53". Started 10:15 UTC, box to 12:45 UTC (80% at 12:15).

**Step 0, premise (10:20 UTC).** Gachard II (sources/ia-fulltext/print-check/labibliothquen02gachuoft_djvu.txt.gz, whole-volume grep): his
table lists Saint-Gouard letters to the duc d'Anjou of 16 July 1572 (p.384) and 19 Sept 1572 (p.402) only; no 5 Sept 1572 letter to Anjou.
Gachard I (labibliothque01gach): no "septembre 1572" / Gouard-Anjou hit. La Ferrière, Catherine IV: no reply or note naming a 5 Sept letter
to Anjou. d'Ars (lepredemadamede00dargoog): cites Saint-Gouard to Anjou 16 July and 19 Sept 1572, not 5 Sept. Leaves: c184 = f.169v (address
leaf of 52, endorsed "5 septembre 1572") | f.170r; c185 = ff.170v-171r, both full cipher; c186 = f.171v (cipher, closing "de Madril ce v^me
de Sept^bre 1572", signed) | f.172r (address leaf "Monseigneur", docket 5 Sept 1572); c187 = f.172v | f.173r (ink 54). No "dechiffré" leaf
between 53 and 54, none found for 53 (N5-VIVTAB saw none from 52 to 55). No decipherment or printed plaintext of 53 located. Proceed.

**Layout (c184-c186 at 1600 px).** f.170r: docket "5 Septembre 1572", heading "du S^r de S^t gouard au Duc d'Anjou", old ink "53"; seven plain
lines ("Monseigneur, Comme je n'ay intention que a bien et fidellement servir ... ce que j'ay traicté avecques le Roy catholique en l'audiance
..."), then cipher from "Jntenon:" (L01) to the foot, 22 lines; f.170v 29 cipher lines; f.171r 30 cipher lines; f.171v 18 cipher lines then the
plain closing. 99 cipher lines in all (N5-VIVTAB's ~100 est.). **Interlinear words** above some groups on f.170r (L03), f.170v (L14-L15) and
f.171r (L07, L09, L10, L19, L23, L25 at least) -- gate (a) applies.

**Crops** (debug overlays checked; f.171r's slope fits crossed between L18-L19 and L23-L26 because of the glosses, and the detector merged
the "smp#" line into its neighbours, so f.171r was re-cut as fixed bands with centres set by eye from the first run's fits, +15/+40 px margins):
```
$ python3 tools/iiif_lines.py --ark btv1b9009609w --canvas 184 --region 4700,2000,3150,2950 --out ciphers/fr16104-vivonne-spain-1572/images/p53 --prefix c184_f170r --follow-slope 400 --distance 90 --max-width 1600 --overlap 150 --debug
  22 lines, 22 bands x 3 segments; wrote 66 crops
$ python3 tools/iiif_lines.py --ark btv1b9009609w --canvas 185 --region 1300,880,2900,4050 --out ciphers/fr16104-vivonne-spain-1572/images/p53 --prefix c185_f170v --follow-slope 400 --distance 80 --max-width 1600 --overlap 150 --debug
  29 lines, 29 bands x 2 segments; wrote 58 crops
$ python3 tools/iiif_lines.py --ark btv1b9009609w --canvas 185 --region 4620,850,3100,4000 --out ciphers/fr16104-vivonne-spain-1572/images/p53 --prefix c185_f171r --centres 195,311,429,547,666,790,925,1059,1190,1313,1452,1586,1714,1854,1984,2117,2241,2355,2469,2636,2760,2895,3023,3140,3260,3400,3541,3673,3807,3927 --top-margin 15 --bottom-margin 40 --max-width 1600 --overlap 150 --debug
  30 lines, 30 bands x 3 segments; wrote 90 crops
$ python3 tools/iiif_lines.py --ark btv1b9009609w --canvas 186 --region 1250,1330,2950,2300 --out ciphers/fr16104-vivonne-spain-1572/images/p53 --prefix c186_f171v --follow-slope 400 --distance 80 --max-width 1600 --overlap 150 --debug
  18 lines, 18 bands x 2 segments; wrote 36 crops
```
**Units, stated before the first subagent call:** 4 pages x (2 blind Sonnet passes + 1 reconciliation) = 12 units at ~USD 1.3 = ~15.6, plus
the gloss look -- over 80% of the USD 15 cap (N5-VIV54 ran ~4 per page all in). So **3 pages are read: f.170r, f.170v, f.171r** (9 units,
~11.7, where the interlinear words are); f.171v (18 lines, ~USD 4) is left as a named gap with its crops cut and committed to the manifest.

**Transcription** (6 blind Sonnet calls, one per page per pass, crop paths only; tx/viv54_clean.py (unchanged) drops [PLAIN:] and writes π as P;
`tools/reconcile_passes.py` on the _c passes -> tx/rec_<page>/; tx/reconcile_vivk.py f170r f170v f171r --viv54 = N5-VIVK's six rules + N5-VIV54's
':'/'o' rule, nothing added; tx/f173r/f173v and N5-VIVK outputs not regenerated):
| page | lines | signs (reconciled) | err_2reader (1 - nw agreement) | splits settled by rule | splits left at pass A | one-pass gaps |
|---|---|---|---|---|---|---|
| f.170r | 22 | 1069 | 0.147 | 0 | 115 | 42 |
| f.170v | 29 | 1286 | 0.210 (L28 0.49, L09 0.64 worst) | 22 | 145 | 103 |
| f.171r | 30 | 1408 | 0.067 | 0 | 57 | 38 |
err_2reader is reader disagreement, not err_true. f.171r's two passes came back with the same token total (1390/1390); checked: 2 of 30 rows identical
and pass B's transcript shows no read of pass A's file -- independent reads; the fixed bands with margins (crop note above) may simply be easier.
Commonest unsettled splits on f.170r: 4 vs '+' (pass B's token for the crossed-descender sign, 20), a vs u (15; reconcile_vivk.py maps a drafted u to a,
but a split is still graded M -- inherited method, not changed), 4 vs p (14), z vs 3 (7).

**Interlinear words** (read by this worker at native resolution from the cached source regions BEFORE any decode; tx/glosses53.tsv, committed
9af8ad2d before the decode): f.170v "myssent" over the end of L14, "en quelque" over the start of L15 (then "pou ~ e", not used); f.171r "e l'Infanct"
over L07, "longuement" over L19 (followed by a struck-through word), "Catixanura" over L22 (letters clear, word not recognised), "po?tent" over L25.
Not used (illegible or line uncertain): f.170r over L03, f.171r "Cote/Lote" (L08/L09) and "Fealy/Italy" (L10).

**Gates (PREREG-N6VIV53.md, pushed 8ce9ea2b with the frozen transcription before any decode; tx/viv53_test.py, seed 20260957, 200 draws;
tx/viv53_result.json):**
| gate | target (ink 53 ff.170r-171r under key.tsv) | control / null | verdict |
|---|---|---|---|
| (a) gloss check, mean LCS(gloss, window)/len, 6 glosses | **0.577** (myssent 0.571, enquelque 0.778, infant 0.500, longuement 0.400, catixanura 0.500, portent 0.714) | shuffled-key null median 0.262, p95 0.353 (not near ceiling) | **FAIL as registered**: above the null p95 by a wide margin, but under the 0.60 floor |
| (b) fr16 judge, 4-gram score per letter | -1.678 (N 3438; word cover 0.766) | positive control f.103r: -1.714, FAILs the judge (real_p05 -0.927) again; shuffled-key decodes median -2.133, p99 -1.757, 0/200 PASS | **judge not a gate** (PREREG rule 1) |
Stated plainly: (a) is the only gate and it fails its absolute floor (0.577 < 0.60); the margin over the shuffled-key null (0.577 vs p95 0.353) is about
the size N5-VIV54 saw (0.609 vs 0.354). No window, gloss row or floor was changed after the decode. (b) is descriptive: ink 53 scores above the f.103r
control and above every shuffled-key decode, as ink 54 did.

**Reading** (tx/viv53_decode.py writes reading_piece53.tsv, `--check` passes; piece53_decode.txt = letters only). 3,607 tokens: **H 2,856**, **M 582**,
**U 169**; no C, no S. H = both readers agree or a label rule settled it AND the code is grade C in key.tsv (Tomokiyo's published key, checked against
the period decipherment of ink 40 in N5-VIVK) -- key-source grading, not legibility, and not a period decipherment of this letter.
By eye (interpretation, not a gate; spelling normalised): long stretches read as French, more than on ink 54 -- f.170r L04 "...inutile ... negotier...",
L11 "...intelligence...", L13 "...ministres...", L16 "...intention..."; f.170v L06 "...frontiere...", L07 "...subiect...", L11 "...bon chrestien s'il est
bien...", L16 "...tiendra..."; f.171r L08 "...bonne intention...", L15 "de contradiction il ne pourroit doubter...", L19 "...pourroit autant...", L21
"...intention ... oubliant...", L22 "...esuaignole..." (espaignol?), L29 "...subtilite...", L30 "...grand bien qui en adviendroit". Other lines are still mixed with
letter salad; the ': :' pair again decodes as a doubled c ("dicct", "ccest"), not corrected (key-label change, a later job).

**print_check** (phrases_53.txt, 5 phrases; sources.tsv incl. Kervyn vol. 3 as N6-KERV left it; print-check-53.tsv, print-check-hosts-53.tsv -- the
default hosts file was restored to N5-VIV54's): the listed sources hit only "bonne intention" in unrelated passages (Gachard II, Catherine IV, Kervyn III);
global searches give unrelated or generic hits ("grand bien qui en adviendroit": 6 Google Books volumes, none on Saint-Gouard; "inutile de negotier": a
1703-17 Savoy work); "de contradiction il ne pourroit doubter" and "inutile de negotier" unsearched on Google Books (HTTP 503), Semantic Scholar and
CrossRef 429 on some calls. Report: no printed plaintext of ink 53 found in the sources named; not found by this method on 4 Oct 2026. Novelty not classified.

Not done: f.171v (18 lines, crops cut, ~USD 4), stopped for the cap per the unit plan above.
Requests: gallica.bnf.fr 7 (c184-c186 at 1600 px, 3 info.json; 4 native regions by iiif_lines -- f.171r's re-cuts read the cached region), >= 2 s apart;
print_check: archive.org 1, be-api 5, googleapis 5, openalex 5, semanticscholar 5, crossref 2. Subagent calls: 6 Sonnet. Cost: see the lane ledger.
Images: crops and source regions kept out of git (images/p53/.gitignore); manifest.json and the four debug overlays committed; regenerate with the
crop commands above.

## N6-VIV63 (4 Oct 2026, LANE-NEAR6 worker, account 2): fr.16105 ink 63 (10 Oct 1573, to the King, ff.190r-194r) read with key.tsv
Brief: .claude/briefs/runs/2026-10-04-ytbiz-near6-wave1.md "N6-VIV63". Started 10:15 UTC, box to 14:14 UTC.

**Step 0, premise (10:17 UTC).** Gachard II (labibliothquen02gachuoft djvu.txt, on disk) LXIII, "Au roi. Madrid, 10 octobre 1573 (En partie
chiffrée, sans le déchiffrement)", pp.435-436: his summary covers only the plain part (audience of 22 Sept, passport for the King of Poland,
St Michel audience, Çayas on the 4th); no plaintext of the cipher. Gachard I (labibliothque01gach): no "Gouard" at all. La Ferrière,
Catherine IV (lettresdecatheri04cathuoft): no letter to Saint-Gouard after 10 Oct 1573 and no note naming a 10 Oct letter (Oct-Dec 1573
entries go to Danzay, Tavannes, Damville, Bellièvre, de Thou, Rambouillet). Neighbouring leaves: N5-VIVTAB viewed fr.16105 c192-c248: no
decipherment of 63 to the end of the volume. N6-KERV (this lane, same hour): Kervyn has no passage dated 10 Oct 1573. Not checked: a
decipherment filed in another volume (fr.16106 holds one such stray, Gachard vol. III XLIV). No printed plaintext located; proceed.

**Layout (c195-c199 at 1600 px, 10:18 UTC).** f.190r = c195 right (stamped "190"); f.190v/f.191r = c196 (stamped "191"); f.191v/f.192r = c197;
f.192v/f.193r = c198; f.193v/f.194r = c199 (stamped "194"). Offset for these leaves: canvas c shows f.(c-6)v left | f.(c-5)r right (N5-VIVK's
c-4/c-3 near f.100 no longer holds). f.190r opens with a plain line ("en ce faict ce que j'en asseureray de v^re mag^te ...") and plain words are
mixed into the first cipher lines ("hardiment avec dilligence ... Il non"); "Il non" recurs inside the cipher on f.190v and f.191v (as on ink 54).
f.194r: ~21 cipher lines, then plain ("... v^re mag^te auroit eu quatre jours plustost son courrier ...", the bodies of the late Emperor, the
Empress, Queens Mary and Eleanor carried to the Escorial), closing "de Madrid ce x^me d'octobre 1573". 8 full pages of 34-36 lines + 21 lines
= about 300 cipher lines, denser than ink 54 (25 lines/page). No interlinear words seen at 1600 px on any of the five openings (gate b applies).

**Crops** (debug overlays checked: one band per written line; f.190r's right edge narrowed to exclude the next leaf's margin strip; f.190v and
f.191v re-cut higher after the first cut missed the top lines; crops not committed (24 MB), manifest committed, regenerate with these commands):
```
$ python3 tools/iiif_lines.py --ark btv1b9009663p --canvas 195 --region 4850,650,2720,4650 --out ciphers/fr16104-vivonne-spain-1572/images/p63 --prefix c195_f190r --follow-slope 400 --distance 70 --max-width 1600 --overlap 150 --debug
  region 2720x4650, 35 lines, 35 bands x 2 segments; pitch 116; wrote 70 crops
$ python3 tools/iiif_lines.py --ark btv1b9009663p --canvas 196 --region 1250,800,2880,4400 --out ciphers/fr16104-vivonne-spain-1572/images/p63 --prefix c196_f190v --follow-slope 400 --distance 70 --max-width 1600 --overlap 150 --debug
  region 2880x4400, 34 lines, 34 bands x 2 segments; pitch 120; wrote 68 crops
$ python3 tools/iiif_lines.py --ark btv1b9009663p --canvas 196 --region 5020,540,2760,4400 --out ciphers/fr16104-vivonne-spain-1572/images/p63 --prefix c196_f191r --follow-slope 400 --distance 70 --max-width 1600 --overlap 150 --debug
  region 2760x4400, 36 lines, 36 bands x 2 segments; pitch 112; wrote 72 crops
$ python3 tools/iiif_lines.py --ark btv1b9009663p --canvas 197 --region 1250,520,2880,4500 --out ciphers/fr16104-vivonne-spain-1572/images/p63 --prefix c197_f191v --follow-slope 400 --distance 70 --max-width 1600 --overlap 150 --debug
  region 2880x4500, 35 lines, 35 bands x 2 segments; pitch 114; wrote 70 crops
```
**Units, stated before the first subagent call (10:21 UTC).** 8.5 pages x 3 units (2 blind Sonnet passes + 1 reconciliation) x ~USD 1.3-1.5 =
~USD 35-38 > the USD 30 cap (80% = 24), and these pages carry ~35 lines against ink 54's ~25, so per pass ~1.4x ink 54's. Plan: **4 pages
(f.190r, f.190v, f.191r, f.191v) = 8 Sonnet passes + 4 reconciliations = 12 units, ~USD 17-20 with this worker's own share**, then decode what is
done; ff.192r-194r (4.5 pages) go to Remaining gaps with their cost. Reconciliation = tools/reconcile_passes.py + tx/reconcile_vivk.py's label
rules (+ RULES54) + this worker's eye on listed splits only.

**Transcription** (8 blind Sonnet calls, one per page per pass, crop paths only, prompt: SIGNS.md + the page's crops, overlap signs once,
DUP/[PLAIN:] marks; tx/viv63_clean.py; `tools/reconcile_passes.py` on the _c passes; tx/viv63_decode.py applies tx/reconcile_vivk.py's RULES +
RULES54 + five rules settled by this worker's eye on crops BEFORE any decode, listed in its header: 3/z -> 3 (f.191r L01 s1 pos 6, 26: the sign
with a descender is SIGNS.md's 3, the flat z sits on the line), P/p -> p (f.191r L04 s1 pos 10, 14: p with a crossed descender), and R/r, R/n,
n/r -> R/n (f.190v L01 s1 pos 15, f.191v L05 s1 pos 5: the "rt"-like sign; key.tsv reads R and n both as t, so no decoded letter changes).
Not settled: r/z (f.190r L05 s1 pos 12 is a small r-rotunda, not the flat z), 2/z, c/e, h/k. Both readers wrote the plain "Il non" on f.190v L01
and L17 as four signs ("H n o n"); the clean step removes it (crop checked: ordinary script), as on f.190r L02 and f.191v L09/L22 where they
marked it plain. f.190r L01 and the head of L02 are plain (the readers' [PLAIN:...] reads only; not transcribed here).
| page | bands (cipher) | signs A / B | err_2reader | splits settled by rule | splits left at pass A | one-pass gaps |
|---|---|---|---|---|---|---|
| f.190r | 35 (34) | 1683 / 1692 | 0.134 | 54 | 106 | 71 |
| f.190v | 34 (33; L10 DUP in both) | 1711 / 1713 | 0.211 | 194 | 111 | 62 |
| f.191r | 36 (36) | 1816 / 1828 | 0.156 | 99 | 101 | 92 |
| f.191v | 35 (35) | 1823 / 1839 | 0.102 | 56 | 78 | 56 |
err_2reader = 1 - two-reader agreement from tools/reconcile_passes.py; reader disagreement, not err_true (no benchmark item for this hand).

**Gates (PREREG-N6VIV63.md, pushed cb382868 before any decode; tx/viv63_test.py, seed 20260967, 200 draws each; tx/viv63_result.json):**
s = mean log10 4-gram probability per letter (fr16 NgramModel), RELATIVE to nulls of the same decode.
| arm | C1 f.103r (1,770 letters) | C2 ink 54 (1,793) | target ink 63 ff.190r-191v (6,220) | verdict |
|---|---|---|---|---|
| b1 vs shuffled-key null p99 | -1.715 vs **-1.674: FAILs** | -1.658 vs -1.824 pass | -1.514 vs -1.792 | **not a gate** (rule 1: positive control C1 fails) |
| b2 vs letter-order-shuffle null p99 | -1.715 vs -1.909 pass | -1.658 vs -1.829 pass | **-1.514 vs -1.824** | **PASS** (both controls pass with headroom; null medians -1.962 / -1.878 / -1.856) |
Per page (descriptive, each about the controls' length): b2 f.190r -1.489 vs -1.730, f.190v -1.638 vs -1.856, f.191r -1.441 vs -1.797, f.191v
-1.490 vs -1.820: every page passes alone; b1 every page passes too. Word cover 0.814 (C1 0.709, C2 0.795). The target scores above both
controls, consistent with its lower reader disagreement.
Post-hoc diagnostic, NOT pre-registered, no gate (tx/viv63_diag_wrongkey.py, tx/viv63_diag_wrongkey.json): 50 wrong (shuffled) keys run through
b2 exactly as the target: 5 of 50 pass b2, margin median -0.029, max +0.061; the real key's margin is +0.311. So b2 has a ~10% false-pass rate at
this length on its own, and the key.tsv decode sits about five times the best wrong key's margin above its null. Stated plainly so the audit can
weigh it: b2 passed as registered; the diagnostic says the margin, not the bare pass, is what separates it from wrong keys.

**Reading** (tx/viv63_decode.py writes reading_piece63.tsv and the four tx/<page>_rec.tsv; `--check` passes; piece63_decode.txt = letters only).
6,866 tokens: **H 5,551** (0.808), **M 669**, **U 646**; no C, no S. Per page H/M/U: f.190r 1348/144/162, f.190v 1330/209/114, f.191r 1414/159/212,
f.191v 1459/157/158. H = both readers agree (or a label rule settled it) AND the code is graded C in key.tsv: key-source grading (Tomokiyo's
published key, values checked against the clerk decipherment of ink 40 in N5-VIVK), not legibility and not a period decipherment of this letter.
U codes: c 115, V 102, single o 99, e 81, 2 67, r 59, l 25 (labels outside key.tsv).
Stretches that read as French by eye (interpretation, not a gate; the decoded string verbatim, '_' = unread code, then a reading in brackets):
f.190r L04 "ctionde_oulouigneet" [-ction de Poulougne et], L10 "touteenthaordi_aireet_onuzitee" [toute extraordinaire et non usitée], L08
"seconiunctureuce" [ceste conjuncture], L31 "duroaders_oulouig_eet" [du roy ... Poulougne et]; f.190v L05 "cestoiten_bueurdutadorange" [c'estoit en
... d'Orange], L32 "tresgrande", L33-34 "co_tandeur" x3, "cardinah" [cardinal ... commandeur?]; f.191r L01 "duco_tandeur", L02
"__rlandreseta_resu_sieurs" [Flandres et après plusieurs], L10 "ungtresgrande", L11 "dangier", L19 "garderuneboune_ort" [garder une bonne porte?],
L20 "aonsieurdesauoa" [Monsieur de Savoie?]; f.191v L01 "trois_archandqge_euoiz" [trois marchands genevois], L02 "constantingentilh..." [Constantin
gentilh(omme)], L19 "_oabredecheuaulq_rhhartilerieet" [nombre de chevaulx ... artillerie et], L26-27 "lestroublesou_arh_ardoulceurdun_arhd|
oncgenerah_etbienaa_le" [les troubles ou par douceur d'un pardon general et bien ample]. Between such stretches many lines are still letter salad.
The recurring "h_" (codes
"y o m" 27x, "y o s" 24x) sits where French wants "qu"/"l": the M code y and the single o (U) look like the place to start the next key review
(suggestion only; key.tsv untouched).

**print_check** (phrases_63.txt, 8 phrases; sources.tsv as on file incl. Kervyn III; output pc63/print-check-63.tsv, pc63/print-check-hosts.tsv,
kept apart from the sister job's print-check.tsv): exact hits only for "le prince dorange" in unrelated passages (Gachard II on 1568; Groen IV;
Kervyn III, on Henri III); ia-global, Google Books, OpenAlex and CrossRef return keyword-relevance lists (e.g. Granvelle's Correspondance for
"pardon general et bien ample", not opened), no quoted match to any decoded phrase; Semantic Scholar 429 after 7 calls (stopped, not retried).
Caveat: phrase 3 ("le prince dorange") and phrase 1's "extra" go beyond the decoded letters (f.190v L05 decodes "...dutadorange", no "prince"); they are weak search keys. Report: no printed plaintext of ink 63's cipher found in the sources named; not found by this method on 4 Oct 2026. Novelty not classified.

Requests: gallica.bnf.fr 15 (c195-c200 at 1600 px, 2 info.json, 7 native regions incl. 2 re-cuts), one at a time >= 2 s apart; print_check:
archive.org 1, be-api 8, googleapis 8, openalex 8, crossref 8, semanticscholar 7 (429). Subagent calls: 8 Sonnet (2 per page). Cost: see the lane
ledger. Stopped at 4 of 8.5 pages as planned in the unit statement above.

## Remaining gaps (N6-VIV53 refresh, 4 Oct 2026)
Read so far: ink 40 checked against its decipherment 41 with Tomokiyo's key (N5-VIVK PASS); ink 54 read with key.tsv, gloss check PASS (0.609 vs null
p95 0.354, N5-VIV54); ink 53 ff.170r-171r read with key.tsv, gloss check FAIL as registered (0.577 vs null p95 0.353, floor 0.60; N6-VIV53), H 2,856 /
M 582 / U 169 of 3,607 tokens, long French stretches by eye. Pieces with no decipherment located: fr.16105 63 (N6-VIV63 at work), fr.16104 52 (and 38,
whose twin is deciphered).
- ink 53 f.171v (18 cipher lines) - blocker: not-attempted; crops cut (images/p53, manifest), stopped for the cap (N6-VIV53); next: 2 blind passes + reconciliation, extend tx/viv53_decode.py PAGES, re-run viv53_test.py descriptively (the PREREG gate is spent), ~$4
- ink 53 gloss gate under 0.60 - blocker: not-attempted; the gate failed its floor, not its null; a second test needs a different instrument or new material (rule 3), not a re-run with moved windows; next: a fresh pre-registered check on independent material -- the f.171v interlinear words (if any, read before decoding) or a lookalike pass (tools/lookalike_pass.py) on the split signs 4/+/p, a/u, z/3 with the gate fixed in advance, ~$4
- ink 54 clean reading - blocker: not-attempted; err_2reader 0.19-0.22 and the ': :' pair read as two signs leave long unreadable stretches; next: a third pass / tools/lookalike_pass.py on the split signs of f.173r-v, the ': :' pair as one sign, re-decode, ~$4
- Judge calibration for this hand - blocker: not-attempted; the fr16 judge FAILs the known-good f.103r control at this noise (N5-VIV54, N6-VIV53); next: score a lower-noise control (the clerk decipherment's own text, or f.103r after a lookalike pass) to see whether the judge can gate at all, ~$2
- fr.16104 ink 52 (5 Sept 1572, to the Queen, ~270 lines) - blocker: not-attempted; no decipherment beside it (N5-VIVTAB); next: look at c179/c181, then crops + 2 blind passes per page, decode with key.tsv, ~$30
- fr.16104 5 Sept 1572 cipher block (ff.157-159v) against its decipherment ff.162r-163r - blocker: not-attempted; known-plaintext check, not a reading; next: crops + two blind passes, aligned as tx/vivk_test.py, ~$15
- Unviewed stretches of the per-piece table - blocker: not-attempted; fr.16104 c1-c169, c192-c324 and fr.16105 c1-c94, c113-c191 not viewed (N5-VIVTAB); next: 1200 px pass every second canvas, contact sheets, ~$3
- fr.16105 f.104r, first page of the decipherment - blocker: illegible; native crop shows word shapes only (N4-VIV3)
- Spanish-side copies (AGS Estado K) and Gachard vol. I - blocker: needs-physical-access; AGS is not digitised in a route this worker could open
## Escalation (4 Oct 2026, N6-VIV53)
- [x] siblings: ink 38 located; ink 40 vs 41 aligned (N5-VIVK); decipherment 51 found (N5-VIV5S); per-piece table (N5-VIVTAB); ink 54 read (N5-VIV54); ink 53 ff.170r-171r read (N6-VIV53)
- [x] clear-pages: decipherments 41, 44, 51, 68, 71, 76 are on the leaves; inks 54 and 53 interlinear words used as gloss checks (N5-VIV54 PASS, N6-VIV53 FAIL at the floor)
- [x] known-keys: Tomokiyo's 1572-74 key on disk and held-out PASS (N5-VIVK); applied to inks 54 and 53
- [x] print: Gachard I-II, d'Ars, Catherine IV-V, Groen IV read; Kervyn I-VI grepped (N6-KERV); print_check on ink 54 and ink 53 phrases
- [retired] key-rebuild: tools/stream_align.py from a flat start did not converge on this material (Arm A, 2 of 30 codes); a published key exists
- [x] image-check: fr.16104 c170-191 and fr.16105 c95-112, c192-248 viewed; f.173r-v and ff.170r-171r native regions (N5-VIV54, N6-VIV53)
- [ ] retry: ink 53 f.171v read and a fresh pre-registered check on independent material; ink 54 lookalike pass; fr.16105 ink 63 (N6-VIV63)
Verdict: keep going: 7 internal gaps; cheapest next: ink 53 f.171v passes + its interlinear words read before decoding, ~$4
Gate output (N6-VIV53, 4 Oct 2026): `OK keep-going fr16104-vivonne-spain-1572: keep going: 7 internal gap(s), 1 step(s) untried`; `tx/viv53_decode.py --check`: reading_piece53.tsv up to date; `tx/viv54_decode.py --check`: reading_piece54.tsv up to date

## Remaining gaps (N6-VIV63 refresh, 4 Oct 2026; merges the N6-VIV53 refresh above, both kept)
Read so far: ink 40 checked against its decipherment 41 with Tomokiyo's key (N5-VIVK PASS); ink 54 read with key.tsv, gloss check PASS (0.609 vs null
p95 0.354, N5-VIV54); ink 53 ff.170r-171r read, gloss check FAIL at its 0.60 floor (0.577 vs null p95 0.353, N6-VIV53); ink 63 ff.190r-191v (4 of ~8.5
cipher pages) read with key.tsv, order gate b2 PASS (-1.514 vs null p99 -1.824; controls f.103r and ink 54 pass b2), b1 not a gate, H 5,551 / M 669 /
U 646 of 6,866 tokens (N6-VIV63). Pieces with no decipherment located: fr.16105 63, fr.16104 52, 53, 54 (and 38, whose twin is deciphered).
- ink 63 ff.192r-194r (4.5 cipher pages, ~160 lines; f.194r cipher ends ~L21) - blocker: not-attempted; stopped at 4 pages for the cap as planned (N6-VIV63); next: crops with the same iiif_lines settings (c197 right, c198 L/R, c199 L/R; canvas c = f.(c-6)v | f.(c-5)r), 2 blind passes per page, extend tx/viv63_decode.py PAGES, a pre-registered amendment of PREREG-N6VIV63 before decoding them, ~$10
- ink 63 key questions (the "h_" pattern) - blocker: not-attempted; codes y (M) and single o (U) sit where French wants "qu"/"l" ("y o m" 27x, "y o s" 24x), and c, V, e, 2, r are unread labels (646 U tokens); next: a code-context table of y, o, c, V, 2 against ink 40's decipherment alignment (tx/key_support.py) and these reads, proposals only, key.tsv changed only by a separate graded step, ~$3
- ink 63 r/z, 2/z, c/e splits - blocker: not-attempted; left at pass A (M); next: tools/lookalike_pass.py on those sign pairs of ff.190r-191v, re-decode, ~$3
- ink 53 f.171v (18 cipher lines) - blocker: not-attempted; crops cut (images/p53, manifest), stopped for the cap (N6-VIV53); next: 2 blind passes + reconciliation, extend tx/viv53_decode.py PAGES, re-run viv53_test.py descriptively (the PREREG gate is spent), ~$4
- ink 53 gloss gate under 0.60 - blocker: not-attempted; the gate failed its floor, not its null; a second test needs a different instrument or new material (rule 3), not a re-run with moved windows; next: a fresh pre-registered check on independent material -- the f.171v interlinear words (if any, read before decoding) or a lookalike pass (tools/lookalike_pass.py) on the split signs 4/+/p, a/u, z/3 with the gate fixed in advance, ~$4
- ink 54 clean reading - blocker: not-attempted; err_2reader 0.19-0.22 and the ': :' pair read as two signs leave long unreadable stretches; next: a third pass / tools/lookalike_pass.py on the split signs of f.173r-v, the ': :' pair as one sign, re-decode, ~$4
- Judge calibration for this hand - blocker: not-attempted; the fr16 judge FAILs the known-good f.103r control at this noise (N5-VIV54, N6-VIV53); next: score a lower-noise control (the clerk decipherment's own text, or f.103r after a lookalike pass) to see whether the judge can gate at all, ~$2
- fr.16104 ink 52 (5 Sept 1572, to the Queen, ~270 lines) - blocker: not-attempted; no decipherment beside it (N5-VIVTAB); next: look at c179/c181, then crops + 2 blind passes per page, decode with key.tsv, ~$30
- fr.16104 5 Sept 1572 cipher block (ff.157-159v) against its decipherment ff.162r-163r - blocker: not-attempted; known-plaintext check, not a reading; next: crops + two blind passes, aligned as tx/vivk_test.py, ~$15
- Unviewed stretches of the per-piece table - blocker: not-attempted; fr.16104 c1-c169, c192-c324 and fr.16105 c1-c94, c113-c191 not viewed (N5-VIVTAB); a decipherment of 63 filed in another volume (fr.16106 holds one such stray) not checked; next: 1200 px pass every second canvas, contact sheets, ~$3
- fr.16105 f.104r, first page of the decipherment - blocker: illegible; native crop shows word shapes only (N4-VIV3)
- Spanish-side copies (AGS Estado K) and Gachard vol. I - blocker: needs-physical-access; AGS is not digitised in a route this worker could open
## Escalation (4 Oct 2026, N6-VIV63)
- [x] siblings: ink 38 located; ink 40 vs 41 aligned (N5-VIVK); decipherment 51 found (N5-VIV5S); per-piece table (N5-VIVTAB); ink 54 read (N5-VIV54); ink 53 ff.170r-171r read (N6-VIV53); ink 63 ff.190r-191v read (N6-VIV63)
- [x] clear-pages: decipherments 41, 44, 51, 68, 71, 76 are on the leaves; inks 54 and 53 interlinear words used as gloss checks (N5-VIV54 PASS, N6-VIV53 FAIL at the floor); ink 63 has none (order gate b2 instead)
- [x] known-keys: Tomokiyo's 1572-74 key on disk and held-out PASS (N5-VIVK); applied to inks 54, 53 and 63
- [x] print: Gachard I-II, d'Ars, Catherine IV-V, Groen IV read; Kervyn I-VI grepped (N6-KERV); print_check on ink 54, 53 and 63 phrases
- [retired] key-rebuild: tools/stream_align.py from a flat start did not converge on this material (Arm A, 2 of 30 codes); a published key exists
- [x] image-check: fr.16104 c170-191 and fr.16105 c95-112, c192-248 viewed; native regions of f.173r-v, ff.170r-171r, ff.190r-191v (N5-VIV54, N6-VIV53, N6-VIV63)
- [ ] retry: ink 63 ff.192r-194r read (pre-registered amendment first); ink 53 f.171v read and a fresh pre-registered check on independent material; ink 54 lookalike pass
Verdict: keep going: 11 internal gaps; cheapest next: ink 63 key questions (y, single o, c, V, 2) as a context table, ~$3, then ink 63 ff.192r-194r, ~$10

Gate output (N6-VIV63, 4 Oct 2026): `OK keep-going fr16104-vivonne-spain-1572: keep going: 10 internal gap(s), 1 step(s) untried`; `tx/viv63_decode.py --check`: reading_piece63.tsv + rec files up to date; `tx/viv54_decode.py --check`: reading_piece54.tsv up to date

## N6-VIV63B (4 Oct 2026, LANE-NEAR6 worker, account 2): fr.16105 ink 63, the remaining cipher pages from f.192r
Brief: .claude/briefs/runs/2026-10-04-ytbiz-near6-wave2.md "N6-VIV63B". Started 10:50 UTC, box to 12:52 UTC. Continues "N6-VIV63" exactly.

**Units, stated before the first subagent call (10:54 UTC).** Remaining: f.192r, f.192v, f.193r, f.193v (~35-37 lines each) + f.194r (21 cipher
lines) = ~4.6 pages. Rate from the ledger's nearest rows (N6-VIV53: 3 pages for 9.14 all in; N6-VIV63: 4 pages for 13.25) = ~USD 3.0-3.3 per
page (2 blind Sonnet passes + 1 reconciliation by script + this worker's eye). 80% of the USD 12 cap = 9.6 -> **3 pages: f.192r, f.192v,
f.193r = 6 Sonnet passes + 3 reconciliations = 9 units, ~USD 9-10 all in**; f.193v and f.194r go to Remaining gaps (~USD 5). If the third
page would start past 80% of the box (12:28 UTC), stop at two.

**Crops** (debug overlays checked; f.193r re-cut from y=500 after the first cut at y=620 clipped line 1; c197 answered HTTP 500 once, one
retry after a pause succeeded; crops not committed, manifest committed):
```
$ python3 tools/iiif_lines.py --ark btv1b9009663p --canvas 197 --region 5000,700,2920,4250 --out ciphers/fr16104-vivonne-spain-1572/images/p63 --prefix c197_f192r --follow-slope 400 --distance 70 --max-width 1600 --overlap 150 --debug
  36 bands x 2 segments; wrote 72 crops
$ python3 tools/iiif_lines.py --ark btv1b9009663p --canvas 198 --region 1200,700,2900,4250 --out ciphers/fr16104-vivonne-spain-1572/images/p63 --prefix c198_f192v --follow-slope 400 --distance 70 --max-width 1600 --overlap 150 --debug
  36 bands x 2 segments; wrote 72 crops
$ python3 tools/iiif_lines.py --ark btv1b9009663p --canvas 198 --region 4880,500,3050,4220 --out ciphers/fr16104-vivonne-spain-1572/images/p63 --prefix c198_f193r --follow-slope 400 --distance 70 --max-width 1600 --overlap 150 --debug
  37 bands x 2 segments; wrote 74 crops
```
Layout seen at 1600 px (c197-c199): f.192r opens with the plain "Il" then cipher to the foot; f.192v and f.193r full cipher pages, f.193r has
"Il non" in ordinary script inside L19 and L21 (as on ff.190v/191v); f.193v full cipher; f.194r ~21 cipher lines then the plain close (as N6-VIV63
described). No interlinear words on c197-c199 at 1600 px.

Correction to the layout line above: f.192r's first sign looked like a plain "Il" at 1600 px; at native resolution it is a three-stroke sign that
both readers wrote P (left as read).

**Transcription** (7 blind Sonnet calls: f.192r A/B, f.192v A/B, f.193r A/B, plus one re-run of f.192v pass B -- the first B returned 1,117 signs,
~30 per line against pass A's 2,081, a skimmed read; it was overwritten by a fresh blind B before reconciliation, one extra priced unit).
Prompt as N6-VIV63 (SIGNS.md + the page's crops, overlap once, DUP/[PLAIN:]). tx/viv63_clean.py and tools/reconcile_passes.py unchanged
(default settings reproduce rec_f191v byte for byte). **No new label rules**: the commonest unsettled pair on f.192r, 6/b (19x; key: 6 = l, b = z
at grade M), was left at pass A (graded M) rather than settled from a partial look; suggestion for the key review below. f.192r L20/L21 is one
written line cut as two bands (both readers marked L21 DUP; checked on the crops). Transcription frozen at b06f4eb4 before any decode.
| page | bands (cipher) | signs A / B | err_2reader | splits settled by rule | splits left at pass A | one-pass gaps |
|---|---|---|---|---|---|---|
| f.192r | 36 (35; L21 DUP) | 1941 / 1986 | 0.182 | 32 | 123 | 223 |
| f.192v | 36 (36) | 2081 / 1980 | 0.164 | 54 | 97 | 199 |
| f.193r | 37 (37; "Il non" plain in L19, L21) | 1922 / 1935 | 0.297 | 61 | 236 | 311 |
err_2reader = 1 - two-reader agreement (reader disagreement, not err_true). f.193r's 0.297 is the highest of the seven ink-63 pages; one-pass gaps
are ~3x N6-VIV63's per page, and the decode shows readers writing the s1/s2 overlap twice ("dangieringier", "quontquont", "rendrendre"):
a duplicated stretch inflates letters and is a known noise source, not cleaned here.

**Gates (PREREG-N6VIV63B.md, pushed 1d9a6dd0 before any decode; tx/viv63b_test.py, seed 20260967, 200 draws; tx/viv63b_result.json).**
tx/viv63_test.py re-run on ff.190r-191v reproduces tx/viv63_result.json unchanged (it now reads PAGES_A).
| arm | letters | s | b2 null p99 | null median | verdict |
|---|---|---|---|---|---|
| C1 f.103r (positive control) | 1,770 | -1.715 | -1.909 | -1.962 | passes, headroom |
| C2 ink 54 (positive control) | 1,793 | -1.658 | -1.829 | -1.878 | passes, headroom |
| (i) new pages ff.192r-193r | 5,592 | **-1.560** | -1.809 | -1.836 | **PASS** |
| (ii) whole piece ff.190r-193r | 11,812 | **-1.536** | -1.826 | -1.847 | **PASS** |
Per page (descriptive): f.192r -1.579 vs -1.795, f.192v -1.644 vs -1.790, f.193r -1.453 vs -1.769: each passes alone. Word cover: new 0.811,
whole 0.813 (C1 0.709, C2 0.795).
**Specificity check (registered rule: PASS iff real whole-piece margin > wrong-key margin p99):** 200 wrong keys (key.tsv values permuted across
codes, seed 20260967-spec) through b2 on the whole piece: **39 of 200 (19.5%) pass b2 on their own**; wrong-key margin median -0.024, p95 +0.024,
p99 **+0.043**, max +0.069; real key margin **+0.290** -> **PASS** (about 4x the best wrong key). As in N6-VIV63's diagnostic, b2's bare pass is not
specific at this length (19.5% false-pass, higher than N6-VIV63's 10% at 6k letters); the margin is what separates the key from wrong keys.

**Reading** (tx/viv63_decode.py, PAGES = ff.190r-193r; `--check`: reading_piece63.tsv + rec files up to date; piece63_decode.txt = whole piece).
Whole piece 12,901 tokens: **H 9,984 (0.774), M 1,828, U 1,089**; no C, no S. New pages H/M/U: f.192r 1541/319/131, f.192v 1565/347/134, f.193r
1327/493/178 (ff.190r-191v unchanged from N6-VIV63). H = both readers agree (or a label rule settled it) AND the code is grade C in key.tsv:
key-source grading (Tomokiyo's published key), not legibility and not a period decipherment of this letter. U codes on the new pages: o 109,
c 73, V 47, e 37, 2 27, l 22, 9 17, r 17.
Stretches that read as French by eye (interpretation, not a gate; decoded string verbatim, then a reading in brackets): f.192r L01
"tresg_andes_intel_igencces" [très grandes intelligences], L06 "dangier", L28 "ccesteheure" [ceste heure], L35 "toutescchooes" [toutes choses];
f.192v L07/L11/L13 "co_tande" [commande(ur)] again, L16 "soitsonseruice" [soit son service], L21 "ccesbrbueseqeccution" [... exécution];
f.193r L06 "seruiceeth_are_utationde" [service et la réputation de], L10 "enanglete_" [en Angleterre], L15 "unglentilho_ttangloisnode"
[ung gentilhomme anglois ...], L22-23 "seirneursoanaglois_eaisontenrlandres" [seigneurs anglois ... en Flandres], L36 "ungtresbon".
England, Flanders and an English gentleman are new themes against ff.190r-191v; the doubled "cc" is the ':' sign read twice as on ink 53.

**print_check** (phrases_63b.txt, 6 phrases, bridged gaps noted in the file -- weak keys; pc63b/print-check-63b.tsv, pc63b/print-check-hosts.tsv):
exact hits only for the generic "toutes choses" (Gachard II, Catherine IV, d'Ars, Housset/archives, Kervyn III) and "ung tres bon" (Catherine IV,
on Soderini), none in a passage about Saint-Gouard's letter of 10 Oct 1573; "service et la reputation", "ung gentilhomme anglois", "seigneurs
anglois en flandres", "tres grandes intelligences": no hits in the five listed sources; Google Books, OpenAlex, CrossRef return relevance lists,
no quoted match; Semantic Scholar 429 after 2 calls (stopped). Report: no printed plaintext of ink 63's cipher found in these sources by this
method on 4 Oct 2026. Novelty not classified.

**Suggestions (not applied; key.tsv untouched):** 6/b split (19x on f.192r) for the lookalike pass; the s1/s2 overlap duplication (readers
writing the overlap twice) for a dedup step in tx/viv63_clean.py, pre-registered before it touches a gated decode.

Requests: gallica.bnf.fr 9 (3 canvases at 1600 px, 2 info.json, 4 native regions incl. 1 HTTP 500 + its one retry and the f.193r re-cut);
print_check: be-api 6, googleapis 6, openalex 6, crossref 6, semanticscholar 2 (429). Subagent calls: 7 Sonnet. Cost: see the lane ledger.
Stopped at 3 of 4.6 pages as planned in the unit statement; ff.193v-194r remain.
**Result line: fr16104-vivonne-spain-1572 piece 63 ready for audit 1 (pages read so far: ff.190r-193r; ff.193v-194r unread)** -- b2 (i) and (ii)
PASS and the specificity check PASS, both positive controls passing b2 with headroom, as PREREG-N6VIV63B.md requires.

## N6-VIV53B (4 Oct 2026, LANE-NEAR6 worker, account 2): ink 53 f.171v, the last cipher page, and the piece-53 gates
Brief: .claude/briefs/runs/2026-10-04-ytbiz-near6-wave2.md "N6-VIV53B". Started 10:50 UTC, box to 12:05 UTC. Continues "N6-VIV53" exactly.

**Units, stated before the first subagent call:** 1 page x (2 blind Sonnet passes + 1 script reconciliation) = 3 units at ~USD 1.3 = ~4, under 80% of
the USD 6 cap.

**Crops.** N6-VIV53's f.171v region (1250,1330,2950,2300) **missed the first 3 cipher lines** (checked against c186 at 1600 px: "dtz dp ym...", "ymoomy#...",
"zmpm ym..." sit above it); re-cut before any pass, f.171v has **21** cipher lines, not 18:
```
$ python3 tools/iiif_lines.py --ark btv1b9009609w --canvas 186 --region 1250,950,2950,2680 --out ciphers/fr16104-vivonne-spain-1572/images/p53 --prefix c186_f171v --follow-slope 400 --distance 80 --max-width 1600 --overlap 150 --debug
  21 lines, 21 bands x 2 segments; wrote 42 crops
```
(Crops kept out of git as before; manifest + overlay committed. The old 18-line crops regenerated byte-identical boxes before the re-cut.)

**Interlinear words:** none on f.171v -- read by this worker at native resolution (8 tiles of the source region, all 21 lines) before any pass returned
or any decode. Gate (a) of the brief therefore does not apply (0 < 3); recorded in PREREG-N6VIV53B.md.

**Transcription** (2 blind Sonnet calls, crop paths + SIGNS.md only; tx/viv54_clean.py; tools/reconcile_passes.py -> tx/rec_f171v/; tx/reconcile_vivk.py
f171v --viv54, nothing added; frozen at ff56211b before decode):
| page | lines | signs (reconciled) | err_2reader (1 - nw agreement) | splits settled by rule | splits left at pass A | one-pass gaps |
|---|---|---|---|---|---|---|
| f.171v | 21 | 947 | 0.180 | 6 | 77 | 87 |
err_2reader is reader disagreement, not err_true. Commonest unsettled pairs: S/d 7, 3/z 7, r/x 3, g/y 3, P/r 3, @/V 3. Pass B called itself low-confidence on L01-L07.

**Gates (PREREG-N6VIV53B.md pushed d2acd3d7 before any f.171v decode; tx/viv53b_test.py, seed "20261053", 200 draws; tx/viv53b_result.json).**
Disclosed in the PREREG: the ff.170r-171r decode was on file when b2 (PREREG-N6VIV63's statistic, unchanged) was reused; only (b-i) is on unseen material.
| gate | target | controls / null | verdict |
|---|---|---|---|
| (b-i) b2 on f.171v alone (869 letters) | s -1.620 vs letter-order null p99 -1.817 | C1 f.103r subsampled to 869: -1.695 vs p99 -1.901 PASS; C2 ink 54 subsampled: -1.673 vs -1.801 PASS | **PASS** |
| (b-ii) b2 on the whole piece ff.170r-171v (4,307 letters) | s -1.667 vs p99 -1.843 | C1 full -1.715 vs -1.905 PASS; C2 full -1.658 vs -1.826 PASS (headroom ok) | **PASS** |
| (c) specificity, 200 wrong keys through b2 on the whole piece | real margin (s - p99) **0.176** | wrong-key margins: median -0.032, p95 0.032, p99 0.051, max 0.077; **44/200 (22%) wrong keys pass b2 alone** | **PASS** (0.176 > 0.051) |
Stated plainly: b2 alone is not key-specific on this hand (22% of wrong keys pass it, as N6-VIV63's post-hoc 5/50 suggested); the real key's margin is
2.3x the largest wrong-key margin, which is the registered pass. The ff.170r-171r gloss gate FAIL (0.577 < 0.60) stands and was not re-run
(tx/viv53_test.py still on ff.170r-171r; re-running it reproduced tx/viv53_result.json byte-identical). Descriptive, not gated: per-page b2 all pass
(f.170r -1.797 vs -1.870, f.170v -1.643 vs -1.756, f.171r -1.619 vs -1.799, f.171v as above); b1 (shuffled-key null) passes on the whole piece
(-1.667 vs p99 -1.782) and on f.171v, not on f.170r.

**Reading** (tx/viv53_decode.py, PAGES now ff.170r-171v; `--check` passes; piece53_decode_all.txt = whole-piece letters; piece53_decode.txt unchanged,
it is the frozen gate's candidate). Whole piece 4,521 tokens: **H 3,539, M 768, U 214**; f.171v alone 914: H 683, M 186, U 45. No C, no S. H = both
readers agree or a label rule settled it AND the code is grade C in key.tsv -- key-source grading, not legibility, not a period decipherment.
By eye (interpretation, not a gate; spelling normalised): f.171v L03 "...grand...", L03/L12 "...frontiere(s)...", L13 "...toute...contre", L14 and L19
"...vostre altesse..." (the address due to the duc d'Anjou), L15 "...capitaine qu'il entend...", L16 "...bien...oublier a rien", L18 "estoient c'est...".

**print_check** (phrases_53b.txt, 5 phrases; print-check-53b.tsv, print-check-hosts-53b.tsv; the default files restored): listed sources hit only
"sur les frontieres" in unrelated passages; global hits are generic or unrelated ("capitaine qu'il entend": Antwerp maritime law and 1860 merchant-marine
volumes; "saint gouard frontieres capitaine": Catherine de Medicis Lettres vols for 1582-85). No printed plaintext of ink 53 f.171v found in the sources
named; not found by this method on 4 Oct 2026. Novelty not classified.

**piece 53 ready for audit 1** under PREREG-N6VIV53B (gates b-ii and c).
Requests: gallica.bnf.fr 4 (1 HTTP 500 on a 1600 px overview, 1 retry ok, 1 info.json, 1 native region); print_check: be-api 5, googleapis 5,
openalex 5, semanticscholar 5, crossref 5. Subagent calls: 2 Sonnet. Cost: see the lane ledger.

## Remaining gaps (N6-VIV53B refresh, 4 Oct 2026; merges the N6-VIV63 refresh above, both kept; N6-VIV63B lines to be merged by that job)
Read so far: ink 40 checked against its decipherment 41 with Tomokiyo's key (N5-VIVK PASS); ink 54 read with key.tsv, gloss check PASS (0.609 vs null
p95 0.354, N5-VIV54); ink 53 ff.170r-171v read (all 4 cipher pages): gloss check on ff.170r-171r FAIL at its 0.60 floor (0.577 vs null p95 0.353, N6-VIV53, stands); order gate b2 PASS on f.171v alone (-1.620 vs null p99 -1.817; subsampled controls pass) and on the whole piece (-1.667 vs -1.843), wrong-key specificity PASS (real margin 0.176 vs 200 wrong keys p99 0.051), H 3,539 / M 768 / U 214 of 4,521 tokens (N6-VIV53B); ink 63 ff.190r-191v (4 of ~8.5
cipher pages) read with key.tsv, order gate b2 PASS (-1.514 vs null p99 -1.824; controls f.103r and ink 54 pass b2), b1 not a gate, H 5,551 / M 669 /
U 646 of 6,866 tokens (N6-VIV63). Pieces with no decipherment located: fr.16105 63, fr.16104 52, 53, 54 (and 38, whose twin is deciphered).
- ink 63 ff.192r-194r (4.5 cipher pages, ~160 lines; f.194r cipher ends ~L21) - blocker: not-attempted; stopped at 4 pages for the cap as planned (N6-VIV63); next: crops with the same iiif_lines settings (c197 right, c198 L/R, c199 L/R; canvas c = f.(c-6)v | f.(c-5)r), 2 blind passes per page, extend tx/viv63_decode.py PAGES, a pre-registered amendment of PREREG-N6VIV63 before decoding them, ~$10
- ink 63 key questions (the "h_" pattern) - blocker: not-attempted; codes y (M) and single o (U) sit where French wants "qu"/"l" ("y o m" 27x, "y o s" 24x), and c, V, e, 2, r are unread labels (646 U tokens); next: a code-context table of y, o, c, V, 2 against ink 40's decipherment alignment (tx/key_support.py) and these reads, proposals only, key.tsv changed only by a separate graded step, ~$3
- ink 63 r/z, 2/z, c/e splits - blocker: not-attempted; left at pass A (M); next: tools/lookalike_pass.py on those sign pairs of ff.190r-191v, re-decode, ~$3
- ink 53 audit 1 - blocker: not-attempted; b2 + wrong-key gates passed (PREREG-N6VIV53B); next: verifier session (novelty + depth, as VIV54-A1), ~$9
- ink 53 label questions - blocker: not-attempted; the ': :' pair decodes as a doubled c (N6-VIV53), f.171v splits S/d (7) and 3/z (7) left at pass A; next: tools/lookalike_pass.py on those pairs of ff.170r-171v, ': :' as one sign proposal, re-decode, ~$3
- ink 54 clean reading - blocker: not-attempted; err_2reader 0.19-0.22 and the ': :' pair read as two signs leave long unreadable stretches; next: a third pass / tools/lookalike_pass.py on the split signs of f.173r-v, the ': :' pair as one sign, re-decode, ~$4
- Judge calibration for this hand - blocker: not-attempted; the fr16 judge FAILs the known-good f.103r control at this noise (N5-VIV54, N6-VIV53); next: score a lower-noise control (the clerk decipherment's own text, or f.103r after a lookalike pass) to see whether the judge can gate at all, ~$2
- fr.16104 ink 52 (5 Sept 1572, to the Queen, ~270 lines) - blocker: not-attempted; no decipherment beside it (N5-VIVTAB); next: look at c179/c181, then crops + 2 blind passes per page, decode with key.tsv, ~$30
- fr.16104 5 Sept 1572 cipher block (ff.157-159v) against its decipherment ff.162r-163r - blocker: not-attempted; known-plaintext check, not a reading; next: crops + two blind passes, aligned as tx/vivk_test.py, ~$15
- Unviewed stretches of the per-piece table - blocker: not-attempted; fr.16104 c1-c169, c192-c324 and fr.16105 c1-c94, c113-c191 not viewed (N5-VIVTAB); a decipherment of 63 filed in another volume (fr.16106 holds one such stray) not checked; next: 1200 px pass every second canvas, contact sheets, ~$3
- fr.16105 f.104r, first page of the decipherment - blocker: illegible; native crop shows word shapes only (N4-VIV3)
- Spanish-side copies (AGS Estado K) and Gachard vol. I - blocker: needs-physical-access; AGS is not digitised in a route this worker could open
## Escalation (4 Oct 2026, N6-VIV53B; from the N6-VIV63 list)
- [x] siblings: ink 38 located; ink 40 vs 41 aligned (N5-VIVK); decipherment 51 found (N5-VIV5S); per-piece table (N5-VIVTAB); ink 54 read (N5-VIV54); ink 53 ff.170r-171v read (N6-VIV53, N6-VIV53B); ink 63 ff.190r-191v read (N6-VIV63)
- [x] clear-pages: decipherments 41, 44, 51, 68, 71, 76 are on the leaves; inks 54 and 53 interlinear words used as gloss checks (N5-VIV54 PASS, N6-VIV53 FAIL at the floor); f.171v has none (N6-VIV53B); ink 63 has none (order gate b2 instead)
- [x] known-keys: Tomokiyo's 1572-74 key on disk and held-out PASS (N5-VIVK); applied to inks 54, 53 and 63
- [x] print: Gachard I-II, d'Ars, Catherine IV-V, Groen IV read; Kervyn I-VI grepped (N6-KERV); print_check on ink 54, 53 and 63 phrases
- [retired] key-rebuild: tools/stream_align.py from a flat start did not converge on this material (Arm A, 2 of 30 codes); a published key exists
- [x] image-check: fr.16104 c170-191 and fr.16105 c95-112, c192-248 viewed; native regions of f.173r-v, ff.170r-171v, ff.190r-191v (N5-VIV54, N6-VIV53, N6-VIV63)
- [ ] retry: ink 63 ff.192r-194r read (pre-registered amendment first); ink 53 label questions (lookalike pass); ink 54 lookalike pass
Verdict: keep going: 10 internal gaps; cheapest next: ink 53 audit 1 (verifier, b2 + wrong-key gates passed), ~$9; ink 63 key questions context table, ~$3

## Remaining gaps (N6-VIV63B refresh, 4 Oct 2026; merges the N6-VIV53B refresh above, both kept)
Read so far: ink 40 checked against its decipherment 41 with Tomokiyo's key (N5-VIVK PASS); ink 54 read with key.tsv, gloss check PASS (0.609 vs null
p95 0.354, N5-VIV54); ink 53 ff.170r-171v read (all 4 cipher pages): gloss check on ff.170r-171r FAIL at its 0.60 floor (N6-VIV53, stands); b2 PASS on
f.171v and the whole piece, wrong-key specificity PASS (real 0.176 vs p99 0.051), H 3,539 / M 768 / U 214 of 4,521 (N6-VIV53B); ink 63 ff.190r-193r
(7 of ~8.6 cipher pages) read with key.tsv: b2 PASS on ff.190r-191v (N6-VIV63), on ff.192r-193r alone (-1.560 vs -1.809) and on the whole (-1.536 vs
-1.826), wrong-key specificity PASS (real 0.290 vs p99 0.043; 19.5% of wrong keys pass b2 alone), H 9,984 / M 1,828 / U 1,089 of 12,901 tokens
(N6-VIV63B). Pieces with no decipherment located: fr.16105 63, fr.16104 52, 53, 54 (and 38, whose twin is deciphered).
- ink 63 ff.193v-194r (1 full page + 21 cipher lines of f.194r) - blocker: not-attempted; stopped at 3 pages for the cap as planned (N6-VIV63B); next: crops c199 left (f.193v, region ~1300,700,2900,3980) and right (f.194r cipher only, ~4820,600,3100,1930) with the same iiif_lines settings, 2 blind passes per page, add to PAGES_B, re-run tx/viv63b_test.py descriptively (or a pre-registered addendum), ~$5
- ink 63 audit 1 - blocker: not-attempted; b2 (new + whole) + wrong-key gates passed (PREREG-N6VIV63B); next: verifier session (novelty + depth, as VIV54-A1) on ff.190r-193r, ~$9
- ink 63 key questions (the "h_" pattern) - blocker: not-attempted; codes y (M) and single o (U) sit where French wants "qu"/"l", and c, V, e, 2, r are unread labels (1,089 U tokens over ff.190r-193r); next: a code-context table of y, o, c, V, 2 against ink 40's decipherment alignment (tx/key_support.py) and these reads, proposals only, ~$3
- ink 63 label splits and overlap duplication - blocker: not-attempted; r/z, 2/z, c/e (ff.190r-191v) and 6/b (f.192r, 19x) left at pass A; readers wrote some s1/s2 overlaps twice (f.192r L06, L34; f.193r L07); f.193r err_2reader 0.297; next: tools/lookalike_pass.py on those pairs + a pre-registered overlap-dedup step in tx/viv63_clean.py, re-decode, ~$4
- inks 53/54 N4 - blocker: not-attempted; audit 1 done for both (54: VIV54-A1 AUDIT 1; 53: VIV53-A1 AUDIT 2, N3, D1 fragments read, key published); next: a LOCAL-QUEUE row for the owner's browser to read Ribera (2007) note 139 and RQH 35 (1884) in full, ~$1; audit 1 of 53 done 4 Oct 2026 (VIV53-A1, AUDIT.md AUDIT 2: N3, D1 fragments read, key published)
- ink 53 label questions - blocker: not-attempted; the ': :' pair decodes as a doubled c (N6-VIV53), f.171v splits S/d (7) and 3/z (7) left at pass A; next: tools/lookalike_pass.py on those pairs of ff.170r-171v, ': :' as one sign proposal, re-decode, ~$3
- ink 54 clean reading - blocker: not-attempted; err_2reader 0.19-0.22 and the ': :' pair read as two signs leave long unreadable stretches; next: a third pass / tools/lookalike_pass.py on the split signs of f.173r-v, the ': :' pair as one sign, re-decode, ~$4
- Judge calibration for this hand - blocker: not-attempted; the fr16 judge FAILs the known-good f.103r control at this noise (N5-VIV54, N6-VIV53); next: score a lower-noise control (the clerk decipherment's own text, or f.103r after a lookalike pass) to see whether the judge can gate at all, ~$2
- fr.16104 ink 52 (5 Sept 1572, to the Queen, ~270 lines) - blocker: not-attempted; no decipherment beside it (N5-VIVTAB); next: look at c179/c181, then crops + 2 blind passes per page, decode with key.tsv, ~$30
- fr.16104 5 Sept 1572 cipher block (ff.157-159v) against its decipherment ff.162r-163r - blocker: not-attempted; known-plaintext check, not a reading; next: crops + two blind passes, aligned as tx/vivk_test.py, ~$15
- Unviewed stretches of the per-piece table - blocker: not-attempted; fr.16104 c1-c169, c192-c324 and fr.16105 c1-c94, c113-c191 not viewed (N5-VIVTAB); a decipherment of 63 filed in another volume (fr.16106 holds one such stray) not checked; next: 1200 px pass every second canvas, contact sheets, ~$3
- fr.16105 f.104r, first page of the decipherment - blocker: illegible; native crop shows word shapes only (N4-VIV3)
- Spanish-side copies (AGS Estado K) and Gachard vol. I - blocker: needs-physical-access; AGS is not digitised in a route this worker could open
## Escalation (4 Oct 2026, N6-VIV63B; merges the N6-VIV53B list)
- [x] siblings: ink 38 located; ink 40 vs 41 aligned (N5-VIVK); decipherment 51 found (N5-VIV5S); per-piece table (N5-VIVTAB); ink 54 read (N5-VIV54); ink 53 ff.170r-171v read (N6-VIV53, N6-VIV53B); ink 63 ff.190r-193r read (N6-VIV63, N6-VIV63B)
- [x] clear-pages: decipherments 41, 44, 51, 68, 71, 76 are on the leaves; inks 54 and 53 interlinear words used as gloss checks (N5-VIV54 PASS, N6-VIV53 FAIL at the floor); f.171v has none (N6-VIV53B); ink 63 has none (order gate b2 instead)
- [x] known-keys: Tomokiyo's 1572-74 key on disk and held-out PASS (N5-VIVK); applied to inks 54, 53 and 63
- [x] print: Gachard I-II, d'Ars, Catherine IV-V, Groen IV read; Kervyn I-VI grepped (N6-KERV); print_check on ink 54, 53 and 63 phrases (N6-VIV63B: pc63b/)
- [retired] key-rebuild: tools/stream_align.py from a flat start did not converge on this material (Arm A, 2 of 30 codes); a published key exists
- [x] image-check: fr.16104 c170-191 and fr.16105 c95-112, c192-248 viewed; native regions of f.173r-v, ff.170r-171v, ff.190r-193r (N5-VIV54, N6-VIV53, N6-VIV63, N6-VIV63B)
- [ ] retry: ink 63 ff.193v-194r read; ink 63 and 53 label questions (lookalike pass, overlap dedup); ink 54 lookalike pass
Verdict: keep going: 11 internal gaps; cheapest next: ink 63 ff.193v-194r passes, ~$5 (N6-VIV63C running), then audit 1 of ink 63 (verifier), ~$9

Gate output (N6-VIV63B, 4 Oct 2026): `OK keep-going fr16104-vivonne-spain-1572: keep going: 11 internal gap(s), 1 step(s) untried`; `tx/viv63_decode.py --check`: reading_piece63.tsv + rec files up to date; `tx/viv54_decode.py --check` and `tx/viv53_decode.py --check`: up to date; tracked folder 27.7 MB (crops gitignored, manifest committed)

## N6-VIV63C (4 Oct 2026, LANE-NEAR6 worker, account 2): fr.16105 ink 63, the last cipher pages ff.193v-194r
Brief: .claude/briefs/runs/2026-10-04-ytbiz-near6-wave2.md "N6-VIV63C". Started 11:26 UTC, box to 12:26 UTC. Continues "N6-VIV63B" exactly.
PREREG-N6VIV63C.md pushed 36de39f5 before any crop, pass or decode. Units stated in ROOM.md at 11:30 before the first subagent call (4 Sonnet passes).

**Crops** (c199 at 1600 px viewed first: f.193v left = 36 cipher lines; f.194r right = 19 cipher lines + a mixed line 20 whose head is cipher and
whose rest is the plain close; no interlinear words). Crops gitignored, manifests committed:
```
$ python3 tools/iiif_lines.py --ark btv1b9009663p --canvas 199 --region 1300,600,2980,4560 --out ciphers/fr16104-vivonne-spain-1572/images/p63 --prefix c199_f193v --follow-slope 400 --distance 70 --max-width 1600 --overlap 150 --debug
  36 bands x 2 segments; wrote 72 crops
$ python3 tools/iiif_lines.py --ark btv1b9009663p --canvas 199 --region 4800,200,2950,2600 --out ciphers/fr16104-vivonne-spain-1572/images/p63 --prefix c199_f194r --follow-slope 400 --distance 70 --max-width 1600 --overlap 150 --debug
  20 bands x 2 segments; wrote 40 crops
# f.194r lines 11-20 re-cut (see below): the 2950x2700 native region of the same canvas (4800,200,2950,2700) rotated -1.4 deg (PIL BICUBIC,
# fill 255, no expand), rows 1500-2640 saved as f194r_low_rot.jpg, then
$ python3 tools/iiif_lines.py --image f194r_low_rot.jpg --out ciphers/fr16104-vivonne-spain-1572/images/p63 --prefix c199_f194r_low --distance 80 --max-width 1100 --overlap 150 --debug
  10 bands x 3 segments; wrote 30 crops   (manifest: images/p63/manifest_f194r_low.json)
```
**Crop failure on f.194r, found from the passes and fixed before any decode.** The lines on f.194r slope more steeply and unevenly than on the
earlier pages (fit slopes -0.008 to -0.041). With `--follow-slope` the per-band fit snapped onto neighbouring lines: both readers marked bands L12, L16 and
L19 DUP. A crop stack checked by eye shows that page lines 14 and 16 had no band, and that bands L05-L10 straddle two written lines. The readers
took different lines there: by row similarity pass A L08 ~ B L09 0.83, A L09 ~ B L10 0.91, A L10 ~ B L11 0.94, against 0.76-0.93 on the same row for L01-L04.
A `--centres` re-cut with `--follow-slope` snapped the same way. Fix: page lines 11-20 were deskewed and cut flat (3 segments), and two more blind Sonnet passes
were run on those 10 bands (6 Sonnet calls in all, not 4). Page lines 5-10 are **dropped** (top rows L05-L10 not used; a Remaining gap). tx/viv63c_f194r_compose.py
builds tx/f194r_pass{A,B}.tsv from top rows L01-L04 and low rows L01-L10 (as L11-L20); pass A only joins pass A. It also rewrites one nested '[...]'
inside a [PLAIN:] (low pass A L10) as '(...)', so the plain close is removed whole; no sign changed. Transcription frozen at 65ee9708 before any decode.
**No new label rules** (commonest unsettled split on f.193v is 2/z, 25x, left open as in N6-VIV63).
| page | lines read (cipher) | signs A / B | err_2reader | splits settled by rule | splits left at pass A | one-pass gaps |
|---|---|---|---|---|---|---|
| f.193v | 36 | 1862 / 1934 (raw) | 0.153 | 39 | 137 | 123 |
| f.194r | 14 rows: lines 1-4, 11-19 + head of 20 (lines 5-10 dropped) | 13 / 14 rows kept after clean | 0.206 | 16 | 46 | 83 |

**Gates (PREREG-N6VIV63C.md; tx/viv63c_test.py, seed 20260967, 200 draws; tx/viv63c_result.json; 6 min run).**
| arm | letters | s | b2 null p99 | null median | verdict |
|---|---|---|---|---|---|
| C1 f.103r full | 1,770 | -1.715 | -1.909 | -1.962 | passes, headroom (reproduces N6-VIV63) |
| C2 ink 54 full | 1,793 | -1.658 | -1.829 | -1.878 | passes, headroom (reproduces N6-VIV63) |
| C1 "subsampled" to new-pages N | 1,770 | -1.715 | -1.909 | -1.962 | passes, headroom |
| C2 "subsampled" to new-pages N | 1,793 | -1.658 | -1.827 | -1.876 | passes, headroom |
| (i) new pages ff.193v-194r | 2,408 | **-1.602** | -1.820 | -1.865 | **PASS** |
| (ii) whole piece ff.190r-194r | 14,220 | **-1.547** | -1.835 | -1.851 | **PASS** |
Disclosure on (i): the PREREG assumed that the controls were longer than the new pages. They are not: the new pages decode to 2,408 letters, the controls
to 1,770/1,793. So the registered window (from token 0 up to 2,408 letters) took each whole control, and (i) ran against full-length controls shorter
than the target. That is the conservative direction (rule 3: a shorter control has less power, so its pass is the harder one), but it is not the
matched-N subsample the PREREG named. A matched-N control would need a longer known-good decode; none exists for this hand. Per page (descriptive):
f.193v -1.579 vs p99 -1.808; f.194r (644 letters) -1.665 vs -1.824. Both pass alone. Word cover: new 0.799, whole 0.811.
**Specificity (registered rule: PASS iff real whole-piece margin > wrong-key margin p99):** 200 wrong keys (seed 20260967-spec-C).
**48 of 200 (24.0%) pass b2 on their own**; wrong-key margin median -0.022, p95 +0.033, p99 **+0.048**, max +0.078; real margin **+0.288** -> **PASS**.
That is about 3.7x the best wrong key. As in N6-VIV63B, b2's bare pass is not key-specific at this length (24% false-pass, rising with length); the margin is.

**Reading** (tx/viv63_decode.py, PAGES = ff.190r-194r; `--check` up to date; viv54/viv53 `--check` still up to date; piece63_decode.txt = whole piece).
Whole piece 15,461 tokens: **H 11,932 (0.772), M 2,288, U 1,241**; no C, no S. New pages H/M/U: f.193v 1443/321/112, f.194r 505/139/40. H = both readers agree
(or a label rule settled it) AND the code is grade C in key.tsv. That is key-source grading (Tomokiyo's published key), not legibility and not a period
decipherment of this letter. U codes on the new pages: e 39, V 27, o 24, Z 10, t 7, c 6.
Stretches that read as French by eye (interpretation, not a gate; decoded string verbatim, then a reading in brackets): f.193v L01
"uigilantetcurieuzsaethaicterall_aires" [vigilant et curieux ... affaires], L09 "_qsontreshuableettresal_ecction" [... sont très humble(s) et très
affection(nés)], L11 "treshuableaentcceccontenteraedounera" [très humblement se contentera ... donnera], L26 "_lusgrandeet_lus" [plus grande et plus],
L30 "deulqcchooesqesisont" [de(s) choses qui sont], L32 "toutaboncco_tandeaen" [tout à bon commande ...]; f.194r L04 "acesteheu" [à ceste heure], L11
"toutediligence", L15 "g_andcco_tandeur" [grand commandeur], L17 "bienientostenrlandres" [bien tost en Flandres]. Many lines between them are still
letter salad (f.193v L02, L19; f.194r L14, L16).

**print_check** (phrases_63c.txt, 6 phrases, gaps bridged -- weak keys; pc63c/print-check-63c.tsv, pc63c/print-check-hosts.tsv). Exact hits only for generic
phrases: "toute diligence" (Gachard II, Catherine IV, Housset), "grand commandeur" (Gachard II, Catherine IV, Housset, and Kervyn III, which quotes Saint-Gouard
at Madrid on the grand commandeur and the Emperor -- not opened past the snippet; N6-KERV found no passage dated 10 Oct 1573 in Kervyn), "plus grande et
plus" (d'Ars; near hits elsewhere). "vigilant et curieux", "tres humble et tres affection" and "bientost en flandres" got no hits in the five listed sources.
ia-global, Google Books, OpenAlex and CrossRef return relevance lists, no quoted match (ia-global HTTP 502 once on "grand commandeur", not retried). Report: no
printed plaintext of ink 63's cipher found in these sources by this method on 4 Oct 2026. Novelty not classified.

Requests: gallica.bnf.fr 7 (c199 at 1600 px, 1 info.json, 4 native regions incl. the 2780-row and 2700-row re-cuts, one at a time >= 2 s apart);
print_check: be-api 6, googleapis 6, openalex 6, crossref 6. Subagent calls: 6 Sonnet (f.193v A/B, f.194r A/B, f.194r lower block A/B). Cost: see the lane ledger.
**Result line: fr16104-vivonne-spain-1572 piece 63 ready for audit 1 (all pages except f.194r lines 5-10).** b2 (i) and (ii) both PASS, with both positive
controls passing with headroom (for (i) at full length, shorter than the target, as disclosed above), and the specificity check PASSes, as PREREG-N6VIV63C.md requires.

## Remaining gaps (N6-VIV63C refresh, 4 Oct 2026; supersedes the N6-VIV63B list above, all its other lines kept)
Read so far: ink 40 checked against its decipherment 41 with Tomokiyo's key (N5-VIVK PASS); ink 54 read with key.tsv, gloss check PASS (N5-VIV54); ink 53
ff.170r-171v read, b2 + wrong-key PASS (N6-VIV53B); ink 63 ff.190r-194r read except f.194r lines 5-10: b2 PASS on every part (N6-VIV63, N6-VIV63B,
N6-VIV63C), whole piece -1.547 vs p99 -1.835, wrong-key specificity PASS (real 0.288 vs p99 0.048), H 11,932 / M 2,288 / U 1,241 of 15,461 tokens.
Pieces with no decipherment located: fr.16105 63, fr.16104 52, 53, 54 (and 38, whose twin is deciphered).
- ink 63 f.194r lines 5-10 - blocker: not-attempted; the --follow-slope cut straddled lines there (N6-VIV63C); next: deskew rows ~500-1500 of the c199 region 4800,200,2950,2700 by -1.4 deg, iiif_lines --image flat cut as for the lower block, 2 blind Sonnet passes on 6 bands, append to tx/viv63c_f194r_compose.py, re-decode, b2 descriptive, ~$1.5
- ink 63 N4 (audit 1 done 4 Oct 2026 by VIV63-A1, AUDIT.md AUDIT 3: N3, D1 fragments read, key published; recipient the King; no decipherment in fr.16105 c95-c248) - blocker: not-attempted; Flament, L'ambassade du marquis de Saint-Gouard en Espagne 1572-1574 (1996, OCLC 988579745) and Ribera (2007) unread, fr.16105 c1-c94 and the fr.16106 pieces Gachard skips not viewed; next: a LOCAL-QUEUE row for Flament and Ribera on 10 Oct 1573 (interlibrary or the owner's browser), ~$1
- tools/iiif_lines.py on steep, uneven line slopes - blocker: not-attempted; --follow-slope (and --centres with it) snapped bands onto neighbouring lines on f.194r; next: an option to deskew the region by a fitted angle before a flat cut (what N6-VIV63C did by hand with PIL), with an offline test, ~$2
- ink 63 key questions (the "h_" pattern) - blocker: not-attempted; codes y (M) and single o (U) sit where French wants "qu"/"l", and c, V, e, 2, r are unread labels (1,241 U tokens over ff.190r-194r); next: a code-context table of y, o, c, V, 2 against ink 40's decipherment alignment (tx/key_support.py) and these reads, proposals only, ~$3
- ink 63 label splits and overlap duplication - blocker: not-attempted; r/z, 2/z (f.193v 25x), c/e and 6/b (f.192r, 19x) left at pass A; readers wrote some s1/s2 overlaps twice (f.192r L06, L34; f.193r L07); f.193r err_2reader 0.297; next: tools/lookalike_pass.py on those pairs + a pre-registered overlap-dedup step in tx/viv63_clean.py, re-decode, ~$4
- ink 53 audit 1 - blocker: not-attempted; b2 + wrong-key gates passed (PREREG-N6VIV53B); next: verifier session (novelty + depth, as VIV54-A1), ~$9
- ink 53 label questions - blocker: not-attempted; the ': :' pair decodes as a doubled c (N6-VIV53), f.171v splits S/d (7) and 3/z (7) left at pass A; next: tools/lookalike_pass.py on those pairs of ff.170r-171v, ': :' as one sign proposal, re-decode, ~$3
- ink 54 clean reading - blocker: not-attempted; err_2reader 0.19-0.22 and the ': :' pair read as two signs leave long unreadable stretches; next: a third pass / tools/lookalike_pass.py on the split signs of f.173r-v, the ': :' pair as one sign, re-decode, ~$4
- Judge calibration for this hand - blocker: not-attempted; the fr16 judge FAILs the known-good f.103r control at this noise (N5-VIV54, N6-VIV53); next: score a lower-noise control (the clerk decipherment's own text, or f.103r after a lookalike pass) to see whether the judge can gate at all, ~$2
- fr.16104 ink 52 (5 Sept 1572, to the Queen, ~270 lines) - blocker: not-attempted; no decipherment beside it (N5-VIVTAB); next: look at c179/c181, then crops + 2 blind passes per page, decode with key.tsv, ~$30
- fr.16104 5 Sept 1572 cipher block (ff.157-159v) against its decipherment ff.162r-163r - blocker: not-attempted; known-plaintext check, not a reading; next: crops + two blind passes, aligned as tx/vivk_test.py, ~$15
- Unviewed stretches of the per-piece table - blocker: not-attempted; fr.16104 c1-c169, c192-c324 and fr.16105 c1-c94, c113-c191 not viewed (N5-VIVTAB); a decipherment of 63 filed in another volume (fr.16106 holds one such stray) not checked; next: 1200 px pass every second canvas, contact sheets, ~$3
- fr.16105 f.104r, first page of the decipherment - blocker: illegible; native crop shows word shapes only (N4-VIV3)
- Spanish-side copies (AGS Estado K) and Gachard vol. I - blocker: needs-physical-access; AGS is not digitised in a route this worker could open
## Escalation (4 Oct 2026, N6-VIV63C; from the N6-VIV63B list)
- [x] siblings: ink 38 located; ink 40 vs 41 aligned (N5-VIVK); decipherment 51 found (N5-VIV5S); per-piece table (N5-VIVTAB); ink 54 read (N5-VIV54); ink 53 ff.170r-171v read (N6-VIV53, N6-VIV53B); ink 63 ff.190r-194r read except f.194r lines 5-10 (N6-VIV63, N6-VIV63B, N6-VIV63C)
- [x] clear-pages: decipherments 41, 44, 51, 68, 71, 76 are on the leaves; inks 54 and 53 interlinear words used as gloss checks (N5-VIV54 PASS, N6-VIV53 FAIL at the floor); f.171v has none (N6-VIV53B); ink 63 has none (order gate b2 instead)
- [x] known-keys: Tomokiyo's 1572-74 key on disk and held-out PASS (N5-VIVK); applied to inks 54, 53 and 63
- [x] print: Gachard I-II, d'Ars, Catherine IV-V, Groen IV read; Kervyn I-VI grepped (N6-KERV); print_check on ink 54, 53 and 63 phrases (pc63b/, pc63c/)
- [retired] key-rebuild: tools/stream_align.py from a flat start did not converge on this material (Arm A, 2 of 30 codes); a published key exists
- [x] image-check: fr.16104 c170-191 and fr.16105 c95-112, c192-248 viewed; native regions of f.173r-v, ff.170r-171v, ff.190r-194r (N5-VIV54, N6-VIV53, N6-VIV63, N6-VIV63B, N6-VIV63C)
- [ ] retry: ink 63 f.194r lines 5-10 (deskewed cut); ink 63 and 53 label questions (lookalike pass, overlap dedup); ink 54 lookalike pass
Verdict: keep going: 12 internal gaps; cheapest next: ink 63 f.194r lines 5-10, ~$1.5; audit 1 of ink 63 done (VIV63-A1, AUDIT 3)

Gate output (N6-VIV63C, 4 Oct 2026): `OK keep-going fr16104-vivonne-spain-1572: keep going: 12 internal gap(s), 1 step(s) untried`; `tx/viv63_decode.py --check`: reading_piece63.tsv + rec files up to date; `tx/viv54_decode.py --check` and `tx/viv53_decode.py --check`: up to date; tracked folder 28.0 MB (crops gitignored, manifests committed)

## N7-VIV54L (4 Oct 2026, LANE-NEAR7 worker, account 2): ink 54 look-alike pass and pre-registered re-decode
Brief: .claude/briefs/runs/2026-10-04-ytbiz-near7-wave1.md "N7-VIV54L". Claimed 12:17 UTC, box to 13:36 UTC. PREREG-N7VIV54L.md pushed 2293e372
before any re-read or re-decode.
**Units, stated before the first subagent call (12:2x UTC):** scripts (tx/viv54L_prep.py, confusion, tx/viv54L_sheet.py, packet x2, audit) run;
3 Sonnet calls -- f.173r re-read (195 tiles, crops of the 24 lines with a tile), f.173v re-read (176 tiles, 20 lines), one audit re-read (80 agreed
positions, 4 planted, 36 lines) -- + 1 reconciliation by this worker, ~USD 1.2 each = ~4.8 against the 4.5 cap; the audit call is the one dropped
if the page calls overrun.

**Inputs and rules.** PREREG-N7VIV54L.md (2293e372, before any re-read/re-decode) + Addendum A (fb005948, before the window re-reads). tx/viv54L_prep.py
turns every page's reconcile_passes draft into lookalike_pass.py's shapes (no label changed; passC = the committed N5-VIV54 sequence, asserted);
confusion over all 18 Vivonne pages (tx/lookalike54/confusion.tsv: 2,206 swaps in 26,615 aligned pairs; top 3/z 257, 2/z 96, R/r 77, c/e 73).
Packet --top 0: f.173r 195 tiles (86 splits + gaps), f.173v 176 (74 + gaps). Sheet = text cells (id + SIGNS.md words; the passes read words, not a picture).

**First instrument (lookalike_pass.py packet/audit prompts, 3 Sonnet calls): VOID.** All three readers reported defaulting to the shown passC label
(f.173r 65 M + 130 L "closer to a confirmation of passC"; f.173v 176 L; audit 80 L). Rows entered reconcile at conf L (two f.173r tiles the reader
did look at kept); audit-score **NON-TEST** (planted catch 0/4, gate 0.80). Same failure as N7-VIV53L's four calls on ink 53 (ROOM 12:26). Its
re-decode and gates were computed and are kept as tx/viv54L_result_void.json (b2 -1.6367 vs p99 -1.8256 PASS; wrong-key margin 0.189 vs p99 0.048).
**Second instrument (N7-VIV53L's per-tile windows, tx/viv54L_windows.py importing tx/viv53L_windows.py; 2 Sonnet calls): real reads.** Splits only:
f.173r 86 tiles H 4 / M 41 / L 41 (firm = reader A 32, = reader B 11, neither 2); f.173v 74 tiles H 14 / M 41 / L 19 (= A 30, = B 23, neither 2).
2-of-3 (tx/viv54L_merge.py -> reconcile): settled f.173r 43 / relabelled 11, f.173v 53 / relabelled 23; one-pass gaps not re-read (stay M).

| measure | before (N5-VIV54) | after (N7-VIV54L) |
|---|---|---|
| err_2reader (1 - agreed/columns; reader disagreement, not error) | f.173r 0.223, f.173v 0.193 | unchanged (no new blind pass) |
| 2-of-3 residual (unsettled / signs; agreement, not accuracy) | -- (all 389 splits+gaps open: 0.190) | **0.134** (275 / 2,052: f.173r 152, f.173v 123) |
| planted-audit true-error estimate on agreed signs | none | **NON-TEST** (catch 0/4; no unit left for a window audit) |
| tokens H / M / U | 1,990: 1,475 / 318 / 197 | **1,954: 1,488 / 271 / 195** (37 ': :' pairs merged by L1) |
| b2 (s vs letter-order p99) | -1.658 vs -1.829 PASS | **-1.636 vs -1.812 PASS** |
| positive controls (same run, seed 20261054L) | C1 f.103r -1.715 vs -1.915 PASS; C2 ink 53 whole -1.667 vs -1.846 PASS (headroom ok) | same |
| (c) specificity, 200 wrong keys | real margin 0.171 vs wrong p99 0.038 (18/200 pass b2 alone) | **0.176 vs p99 0.043 PASS** (23/200 = 11.5% pass b2 alone; max 0.058) |
| longest repair-free stretch, registered statistic | 59 vs shuffle median 59 / p99 59 | 57 vs 57 / 57: **non-discriminating** (vocabulary of corpus 2-letter tokens covers shuffled text too) |
| same, post-hoc strict vocabulary (descriptive only) | 35 vs shuffle median 26 / p99 45 | 26 vs 26 / 41: real does not exceed its shuffle control |
(tx/viv54L_result.json, tx/stretch54*_*.txt; `tx/viv54L_decode.py --check` passes; reading_piece53/54/63 `--check` all still pass.)

**PREREG (ii) listing: no mechanically found stretch beats its own shuffle control,** so the registered top-10 lists (tx/stretch54*_registered.txt)
are noise-level word covers and are not offered as clauses. By-eye stretches on the re-decode (interpretation, not gated; liberties as AUDIT 2 4a
counts them; the auditor re-counts): f.173r L21 "toute [d]iligence de [U][f]aire" -- decoded "touteailigencede_aire", 21 letters, word division,
1 letter repair (a->d), 1 U sign standing for a letter; f.173v L03 "tousiour[s] [q]ont doubte [q]u c'este" -- "tousiouroqontdoubteuceste", 25 letters,
word division, 1 repair (o->s), the "q" placement and a missing q (2 liberties), L1 used once (": :" -> c); f.173v L05 "...est ... et dict avoir" --
"etdictauoir" 11 letters clean with word division, L1 once. Nothing reaches the ~42-letter authentication distance. L1 did remove the doubled c
("dicct" -> "dict", "ccest" -> "cest", 37 merges): one liberty fewer per such stretch, not a longer stretch. print_check not run: no new
repair-free stretch >= 20 letters (PREREG/brief threshold).

**Key question (the a/u "qae" target, not settled, stays as read).** "to z m" occurs 13 times (decoded "qae"); no reader on any of 18 pages ever
wrote another label for that z (confusion table: no a/z or u/z split), so the 2-of-3 rule cannot reach u, and ink 40's alignment against its
clerk decipherment gave z -> a 77, r 8, i 7, never u (key.tsv n_aligned). Question for the key image (Tomokiyo henryiii_Vivonne1.png, cell u):
is there a z-like u homophone, or does the sender write "qua"/omit u after q (then "to" alone = qu)? Not repaired.
**Owner's sign sorter:** tx/lookalike54/viv54L_f173r_focus.tsv + viv54L_f173v_focus.tsv, 275 questions (tools/sign_sorter.py --focus), the step
TRANSCRIPTION.md / CLAUDE.md Usage 6 names when machine readers cannot separate signs.

**Verdict for the lane:** b2 + specificity pass on the re-decode as registered -> **piece 54 ready for audit (depth re-check)**. Stated plainly so the
auditor does not have to dig: the cleaner transcription is modest (residual 0.190 -> 0.134 on 2-of-3 agreement, H +13, M -47), the true-error
estimate is a non-test, and no stretch longer than about 25 letters without a letter repair was found.
Requests: none to any external host. Subagent calls: 5 Sonnet (3 void, 2 window). Cost: see the lane ledger.

## Remaining gaps (N7-VIV54L refresh, 4 Oct 2026; supersedes the N6-VIV63C list above, all its other lines kept)
Read so far: ink 40 checked against its decipherment 41 with Tomokiyo's key (N5-VIVK PASS); ink 54 read with key.tsv, gloss check PASS (N5-VIV54), window look-alike pass + re-decode, b2 + wrong-key PASS (N7-VIV54L); ink 53
ff.170r-171v read, b2 + wrong-key PASS (N6-VIV53B); ink 63 ff.190r-194r read except f.194r lines 5-10: b2 PASS on every part (N6-VIV63, N6-VIV63B,
N6-VIV63C), whole piece -1.547 vs p99 -1.835, wrong-key specificity PASS (real 0.288 vs p99 0.048), H 11,932 / M 2,288 / U 1,241 of 15,461 tokens.
Pieces with no decipherment located: fr.16105 63, fr.16104 52, 53, 54 (and 38, whose twin is deciphered).
- ink 63 f.194r lines 5-10 - blocker: not-attempted; the --follow-slope cut straddled lines there (N6-VIV63C); next: deskew rows ~500-1500 of the c199 region 4800,200,2950,2700 by -1.4 deg, iiif_lines --image flat cut as for the lower block, 2 blind Sonnet passes on 6 bands, append to tx/viv63c_f194r_compose.py, re-decode, b2 descriptive, ~$1.5
- ink 63 N4 (audit 1 done 4 Oct 2026 by VIV63-A1, AUDIT.md AUDIT 3: N3, D1 fragments read, key published; recipient the King; no decipherment in fr.16105 c95-c248) - blocker: not-attempted; Flament, L'ambassade du marquis de Saint-Gouard en Espagne 1572-1574 (1996, OCLC 988579745) and Ribera (2007) unread, fr.16105 c1-c94 and the fr.16106 pieces Gachard skips not viewed; next: a LOCAL-QUEUE row for Flament and Ribera on 10 Oct 1573 (interlibrary or the owner's browser), ~$1
- tools/iiif_lines.py on steep, uneven line slopes - blocker: not-attempted; --follow-slope (and --centres with it) snapped bands onto neighbouring lines on f.194r; next: an option to deskew the region by a fitted angle before a flat cut (what N6-VIV63C did by hand with PIL), with an offline test, ~$2
- ink 63 key questions (the "h_" pattern) - blocker: not-attempted; codes y (M) and single o (U) sit where French wants "qu"/"l", and c, V, e, 2, r are unread labels (1,241 U tokens over ff.190r-194r); next: a code-context table of y, o, c, V, 2 against ink 40's decipherment alignment (tx/key_support.py) and these reads, proposals only, ~$3
- ink 63 label splits and overlap duplication - blocker: not-attempted; r/z, 2/z (f.193v 25x), c/e and 6/b (f.192r, 19x) left at pass A; readers wrote some s1/s2 overlaps twice (f.192r L06, L34; f.193r L07); f.193r err_2reader 0.297; next: tools/lookalike_pass.py on those pairs + a pre-registered overlap-dedup step in tx/viv63_clean.py, re-decode, ~$4
- ink 53 audit 1 - blocker: not-attempted; b2 + wrong-key gates passed (PREREG-N6VIV53B); next: verifier session (novelty + depth, as VIV54-A1), ~$9
- ink 53 label questions - blocker: not-attempted; the ': :' pair decodes as a doubled c (N6-VIV53), f.171v splits S/d (7) and 3/z (7) left at pass A; next: tools/lookalike_pass.py on those pairs of ff.170r-171v, ': :' as one sign proposal, re-decode, ~$3
- ink 54 clean reading - blocker: not-attempted; window look-alike pass done (residual 0.134), true-error audit a non-test, no stretch near ~42 letters (N7-VIV54L); next: owner's sign sorter on tx/lookalike54/*_focus.tsv (275 questions) or a window-instrument audit (lookalike_pass.py audit + viv53L_windows.py audit), ~$1.5
- ink 54 key question "to z" (qae) - blocker: not-attempted; 13 occurrences, no reader split, ink 40 alignment never gives u for z (N7-VIV54L); next: read Tomokiyo's cell u / q on henryiii_Vivonne1.png for a z-like homophone or a "qu" sign, ~$0.5
- ink 54 audit (depth re-check) - blocker: not-attempted; b2 + wrong-key PASS on the re-decode (PREREG-N7VIV54L); next: verifier session (account 3), ~$5
- Judge calibration for this hand - blocker: not-attempted; the fr16 judge FAILs the known-good f.103r control at this noise (N5-VIV54, N6-VIV53); next: score a lower-noise control (the clerk decipherment's own text, or f.103r after a lookalike pass) to see whether the judge can gate at all, ~$2
- fr.16104 ink 52 (5 Sept 1572, to the Queen, ~270 lines) - blocker: not-attempted; no decipherment beside it (N5-VIVTAB); next: look at c179/c181, then crops + 2 blind passes per page, decode with key.tsv, ~$30
- fr.16104 5 Sept 1572 cipher block (ff.157-159v) against its decipherment ff.162r-163r - blocker: not-attempted; known-plaintext check, not a reading; next: crops + two blind passes, aligned as tx/vivk_test.py, ~$15
- Unviewed stretches of the per-piece table - blocker: not-attempted; fr.16104 c1-c169, c192-c324 and fr.16105 c1-c94, c113-c191 not viewed (N5-VIVTAB); a decipherment of 63 filed in another volume (fr.16106 holds one such stray) not checked; next: 1200 px pass every second canvas, contact sheets, ~$3
- fr.16105 f.104r, first page of the decipherment - blocker: illegible; native crop shows word shapes only (N4-VIV3)
- Spanish-side copies (AGS Estado K) and Gachard vol. I - blocker: needs-physical-access; AGS is not digitised in a route this worker could open
## Escalation (4 Oct 2026, N7-VIV54L; from the N6-VIV63C list)
- [x] siblings: ink 38 located; ink 40 vs 41 aligned (N5-VIVK); decipherment 51 found (N5-VIV5S); per-piece table (N5-VIVTAB); ink 54 read (N5-VIV54); ink 53 ff.170r-171v read (N6-VIV53, N6-VIV53B); ink 63 ff.190r-194r read except f.194r lines 5-10 (N6-VIV63, N6-VIV63B, N6-VIV63C)
- [x] clear-pages: decipherments 41, 44, 51, 68, 71, 76 are on the leaves; inks 54 and 53 interlinear words used as gloss checks (N5-VIV54 PASS, N6-VIV53 FAIL at the floor); f.171v has none (N6-VIV53B); ink 63 has none (order gate b2 instead)
- [x] known-keys: Tomokiyo's 1572-74 key on disk and held-out PASS (N5-VIVK); applied to inks 54, 53 and 63
- [x] print: Gachard I-II, d'Ars, Catherine IV-V, Groen IV read; Kervyn I-VI grepped (N6-KERV); print_check on ink 54, 53 and 63 phrases (pc63b/, pc63c/)
- [retired] key-rebuild: tools/stream_align.py from a flat start did not converge on this material (Arm A, 2 of 30 codes); a published key exists
- [x] image-check: fr.16104 c170-191 and fr.16105 c95-112, c192-248 viewed; native regions of f.173r-v, ff.170r-171v, ff.190r-194r (N5-VIV54, N6-VIV53, N6-VIV63, N6-VIV63B, N6-VIV63C)
- [ ] retry: ink 63 f.194r lines 5-10 (deskewed cut); ink 63 and 53 label questions (lookalike pass, overlap dedup); ink 54 sorter/window audit and key question (lookalike pass done, N7-VIV54L)
Verdict: keep going: 14 internal gaps; cheapest next: ink 54 key question on the key image, ~$0.5, then ink 54 audit (depth re-check), ~$5


Gate output (N7-VIV54L, 4 Oct 2026): `OK keep-going fr16104-vivonne-spain-1572: keep going: 14 internal gap(s), 1 step(s) untried`; `tx/viv54L_decode.py --check`: reading_piece54_L.tsv up to date; viv53/viv54/viv63 `--check` up to date

## N7-VIV53L (4 Oct 2026, LANE-NEAR7 worker, account 2): ink 53 look-alike pass and pre-registered re-decode
Brief: .claude/briefs/runs/2026-10-04-ytbiz-near7-wave1.md "N7-VIV53L". Claimed 12:17 UTC, box to 14:07 UTC. PREREG-N7VIV53L.md pushed 57c1dbd3
before any re-read or re-decode. Inputs: the N6-VIV53/53B two-reader drafts (tx/rec_<page>/ciphertext_draft.tsv); key.tsv and every file behind
reading_piece53/54/63.tsv untouched (all three `--check` pass).
**Units (the brief's plan; written here after the first calls, not before -- a slip):** 4 page re-read calls + 1 audit call + reconciliation by
this worker, ~USD 1.2 each. Actually used: **9 Sonnet calls** -- 4 voided + 4 window re-reads + 1 audit (below).

**Crops** regenerated from the manifest's commands (NOTES N6-VIV53, N6-VIV53B; 4 Gallica native regions, >= 3 s apart), kept out of git as before.
**Inputs for tools/lookalike_pass.py** (tx/viv53L_prep.py -> tx/lookalike53L/): per page agreement.tsv (status agree | split | gap; an N6
reconcile_vivk label rule counts as agree) and passC.tsv (= the N6 reconciled sequence; 1069/1286/1408/947 signs, as N6). `confusion` over the
four pages: 4,440 aligned pairs, 392 label swaps; top pairs 3/z 47, g/y 21, +/4 20, S/d 17, 4/p 16, a/u 15, r/y 14, 2/z 10.

**First instrument voided (VOID1).** `packet --top 0` (split + gap tiles: 155/248/95/164) with the tool's value-blind prompt, an id-only sheet
(tx/lookalike53L/sheet.png: this hand has no reference-shape sheet) and 40-90 whole line crops per call: **all four Sonnet calls echoed passC**
(three said so in their reports; one wrote H/M grades over copied labels). Kept as tx/lookalike53L/*/53L_*_reread_VOID1.tsv, never folded in.
Under the 2-of-3 rule an echo of reader A would have "settled" every split for A: a tool-level hazard for any hand without a shape sheet.
**Second instrument: per-tile windows** (tx/viv53L_windows.py): for each SPLIT tile the line's segments are stitched on source x, the tile's x
is estimated as pos/len along the inked span, a window of about +-6 sign widths is cut (2x, red tick at the estimate), 6 windows per montage;
the prompt gives the 3 labels before/after and the candidates ALPHABETICALLY with SIGNS.md shape descriptions, never which one is the current
reading. Gap tiles (one reader only) were not re-read and stay M (PREREG rule 2 covers splits). Echo check (tx/viv53L_echo.py: re-read label =
reader A / reader B / neither): f170r 38/57/18, f170v 63/60/22, f171r 33/16/8, f171v 36/35/6 -- real reads. Re-read grades H/M/L: f170r
12/88/13, f170v 28/110/7, f171r 9/40/8, f171v 13/54/10. Montages are not committed (~120 MB); regenerate with prep + windows.

**Fold-in** (`lookalike_pass.py reconcile`, fixed 2-of-3 rule, on the split tiles only):
| page | split tiles | settled 2-of-3 | relabelled | UNSETTLED | gaps (not re-read, M) | err_2reader before (N6) |
|---|---|---|---|---|---|---|
| f.170r | 113 | 83 | 50 | 30 | 42 | 0.147 |
| f.170v | 145 | 119 | 60 | 26 | 103 | 0.210 |
| f.171r | 57 | 43 | 13 | 14 | 38 | 0.067 |
| f.171v | 77 | 65 | 32 | 12 | 87 | 0.180 |
| piece | 392 | 310 | 155 | **82 (2-of-3 residual 0.017 of 4,710 signs)** | 270 (0.057) | -- |
The 2-of-3 residual is agreement, not accuracy; the 270 one-reader gaps are a separate, untouched uncertainty.

**Planted audit (true-error estimate on agreed signs, PREREG (iii)).** `lookalike_pass.py audit --sample 100 --plant 0.05 --seed 53 --k 3` (4,037
signs where A, B and passC agree; 100 drawn, 5 planted), shown through the same window instrument (`tx/viv53L_windows.py audit`), one Sonnet call
(H/M/L 73/24/3). `audit-score`: **planted catch 5/5 = 1.00 (gate 0.80) -> control PASS**; unplanted flagged **4/95 = 4.2% (Wilson 95% 1.6-10.3%)**;
one of the four is a -> u, the same code after the MAP, so 3/95 = 3.2% (1.1-8.9%) would change a decoded letter. Read: on signs both readers agree
on, roughly 1 in 25-30 is still wrong (a coarse figure: only 5 plants). Flags are listed in tx/lookalike53L/audit/, not applied (PREREG rule 4).

**Re-decode** (tx/viv53L_decode.py, `--check` passes; reading_piece53_L.tsv, piece53_L_decode.txt): look-alike fold-in, '+' -> 4 after the
vote, "o o" -> oo, then **126 ': :' pairs joined** into one ':' (key cell col c row 1, value c).
| | tokens | H | M | U |
|---|---|---|---|---|
| before (N6-VIV53B, reading_piece53.tsv) | 4,521 | 3,539 (78.3%) | 768 | 214 |
| after (N7-VIV53L, reading_piece53_L.tsv) | 4,394 | 3,641 (82.9%) | 540 | 213 |
H remains key-source grading (published key, checked on ink 40) on a settled sign, not a period decipherment of this letter; no C, no S.
Effects seen by eye: every doubled-c repair is gone ("deccontradicction" -> "decontradiction", f.171r L15; "estecconth" -> "estecont", f.170r L20;
"ericcainutile" -> "ericainutile", f.170r L04). One look-alike change made a word worse: f.171v L15 "capitaine" -> "caglitaine" (pos 31: readers p / 6,
the window re-read chose 6 at M, so 2-of-3 settled 6 = l); reported, not reversed (no "decodes better" overrides).

**Gates (PREREG (iv) = PREREG-N6VIV53B's (b-ii) and (c), rule unchanged; tx/viv53L_test.py, seed "20261053L"; tx/viv53L_result.json):**
| gate | target (whole piece, 4,181 letters) | controls / null | verdict |
|---|---|---|---|
| (b-ii) b2 | s -1.607 vs letter-order null p99 -1.831 | C1 f.103r -1.715 vs -1.891 PASS; C2 ink 54 -1.658 vs -1.827 PASS (headroom ok) | **PASS** |
| (c) specificity, 200 wrong keys | real margin **0.224** | wrong-key margins median -0.034, p95 0.021, p99 0.063, max 0.091; 34/200 (17%) pass b2 alone | **PASS** (0.224 > 0.063) |
Before (N6-VIV53B): s -1.667 vs p99 -1.843, real margin 0.176 vs p99 0.051, 22% of wrong keys passing. Per page (descriptive): f.170r -1.632 vs
-1.834, f.170v -1.615 vs -1.790, f.171r -1.567 vs -1.795, f.171v -1.622 vs -1.795, all pass (N6: f.170r -1.797 vs -1.870). The gloss gate
(0.577) stands; the six gloss windows were not re-scored (not done, cap).

**D2-candidate statistic (PREREG (ii), tx/viv53L_stretches.py, tx/viv53L_stretches.json): a NON-TEST as registered.** Vocabulary = fr16 tokens
with count >= 5 (10,325 forms) includes OCR fragments ("nt", "ur", "hh", "ae"), so letter salad splits into "words": real top-1 90 letters, top-3
mean 79, against the shuffled-letter null median 98 / 86 (p99 194 / 125) -- the real decode is not above its null; the listed 90-letter
"stretch" is salad. **Post-hoc diagnostic, NOT pre-registered, no gate:** vocabulary = fr16 forms with count >= 100 and length >= 3 plus 40
common short words (774 forms): real top-1 20, top-3 mean 15.7, null median 11 / 10.3, p99 17 / 13.0 (200 shuffles) -- real above p99, but the
vocabulary was chosen after seeing the first result.
**Longest repair-free stretches** (post-hoc vocabulary and by eye; liberties as AUDIT 2 4a counts them; no letter substitution in any):
| # | where | letters | decoded (division) | liberties |
|---|---|---|---|---|
| 1 | f.170r L16-L17 | 20 | intention a entrer en ce | word division (5 words), 1 line end, 1 look-alike-settled token, 1 joined ': :'; 0 M |
| 2 | f.171r L15 | 19 | de contradiction il ne | word division (4), 2 joined ': :' (both c's), 2 look-alike-settled, 1 M; continues "rauldhoit doubter" = "[p]ou[r]roit doubter", 3-4 letter repairs |
| 3 | f.170r L04 | 18 | inutile a ne negotier | word division (4), 1 look-alike-settled; 0 M |
| (with repair) | f.171r L30 | 25 | grand bien q[s->u]i en a dviendroit | 1 letter repair, 1 M, u/v; unchanged from N6 |
None reaches the ~42-letter authentication distance (AUDIT 2 4a). The pass shortens repairs (the doubled c's) but does not join the fragments.

**print_check** (phrases_53L.txt: the two stretches >= 19 letters; print-check-53L.tsv, print-check-hosts-53L.tsv; default hosts file restored):
listed sources (Gachard II, Catherine IV, d'Ars, Groen IV, Kervyn III) no hit; global hits generic or unrelated ("de contradiction il ne":
Aristotle and modern philosophy volumes; "intention a entrer en ce": 1891 treaty collection, 1879 encyclopaedia); Semantic Scholar 429 on one
call. No printed plaintext of ink 53 found in the sources named; not found by this method on 4 Oct 2026. Novelty not classified.

**Ready for audit (depth re-check):** b2 (b-ii) and specificity (c) pass on the re-decode, so piece 53 is ready for audit (depth re-check). The depth
verdict is the auditor's.
Requests: gallica.bnf.fr 4 (native regions, >= 3 s apart); print_check: be-api 2, googleapis 2, openalex 2, semanticscholar 2 (one 429), crossref 2.
Subagent calls: 9 Sonnet (4 voided echo calls, 4 window re-reads, 1 audit). Cost: see the lane ledger.

## Remaining gaps (N7-VIV53L refresh, 4 Oct 2026; supersedes the N7-VIV54L list above, all its other lines kept)
Read so far: ink 40 checked against its decipherment 41 with Tomokiyo's key (N5-VIVK PASS); ink 54 read with key.tsv, gloss check PASS (N5-VIV54), window look-alike pass + re-decode, b2 + wrong-key PASS (N7-VIV54L); ink 53
ff.170r-171v read, b2 + wrong-key PASS (N6-VIV53B), window look-alike pass + ': :' join + re-decode, b2 + wrong-key PASS again (N7-VIV53L); ink 63 ff.190r-194r read except f.194r lines 5-10: b2 PASS on every part (N6-VIV63, N6-VIV63B,
N6-VIV63C), whole piece -1.547 vs p99 -1.835, wrong-key specificity PASS (real 0.288 vs p99 0.048), H 11,932 / M 2,288 / U 1,241 of 15,461 tokens.
Pieces with no decipherment located: fr.16105 63, fr.16104 52, 53, 54 (and 38, whose twin is deciphered).
- ink 63 f.194r lines 5-10 - blocker: not-attempted; the --follow-slope cut straddled lines there (N6-VIV63C); next: deskew rows ~500-1500 of the c199 region 4800,200,2950,2700 by -1.4 deg, iiif_lines --image flat cut as for the lower block, 2 blind Sonnet passes on 6 bands, append to tx/viv63c_f194r_compose.py, re-decode, b2 descriptive, ~$1.5
- ink 63 N4 (audit 1 done 4 Oct 2026 by VIV63-A1, AUDIT.md AUDIT 3: N3, D1 fragments read, key published; recipient the King; no decipherment in fr.16105 c95-c248) - blocker: not-attempted; Flament, L'ambassade du marquis de Saint-Gouard en Espagne 1572-1574 (1996, OCLC 988579745) and Ribera (2007) unread, fr.16105 c1-c94 and the fr.16106 pieces Gachard skips not viewed; next: a LOCAL-QUEUE row for Flament and Ribera on 10 Oct 1573 (interlibrary or the owner's browser), ~$1
- tools/iiif_lines.py on steep, uneven line slopes - blocker: not-attempted; --follow-slope (and --centres with it) snapped bands onto neighbouring lines on f.194r; next: an option to deskew the region by a fitted angle before a flat cut (what N6-VIV63C did by hand with PIL), with an offline test, ~$2
- ink 63 key questions (the "h_" pattern) - blocker: not-attempted; codes y (M) and single o (U) sit where French wants "qu"/"l", and c, V, e, 2, r are unread labels (1,241 U tokens over ff.190r-194r); next: a code-context table of y, o, c, V, 2 against ink 40's decipherment alignment (tx/key_support.py) and these reads, proposals only, ~$3
- ink 63 label splits and overlap duplication - blocker: not-attempted; r/z, 2/z (f.193v 25x), c/e and 6/b (f.192r, 19x) left at pass A; readers wrote some s1/s2 overlaps twice (f.192r L06, L34; f.193r L07); f.193r err_2reader 0.297; next: tools/lookalike_pass.py on those pairs + a pre-registered overlap-dedup step in tx/viv63_clean.py, re-decode, ~$4
- ink 53 audit (depth re-check) - blocker: not-attempted; AUDIT 2 (VIV53-A1) set N3 / D1; the N7-VIV53L re-decode passes b2 + wrong-key again (PREREG-N7VIV53L) but no repair-free stretch reaches ~42 letters (longest 20); next: verifier session (account 3) on reading_piece53_L.tsv, ~$5
- ink 53 residual label questions - blocker: not-attempted; 82 split tiles left UNSETTLED by the 2-of-3 rule and 270 one-reader gaps never re-read (tx/lookalike53L/*/focus.tsv), the ': :'-as-null alternative, and "rauldhoit" (f.171r L15, where French wants "pourroit") unresolved (N7-VIV53L); next: owner's sign sorter on the focus files, or a window re-read of the gap tiles (tx/viv53L_windows.py extended to gaps), ~$2
- ink 54 clean reading - blocker: not-attempted; window look-alike pass done (residual 0.134), true-error audit a non-test, no stretch near ~42 letters (N7-VIV54L); next: owner's sign sorter on tx/lookalike54/*_focus.tsv (275 questions) or a window-instrument audit (lookalike_pass.py audit + viv53L_windows.py audit), ~$1.5
- ink 54 key question "to z" (qae) - blocker: not-attempted; 13 occurrences, no reader split, ink 40 alignment never gives u for z (N7-VIV54L); next: read Tomokiyo's cell u / q on henryiii_Vivonne1.png for a z-like homophone or a "qu" sign, ~$0.5
- ink 54 audit (depth re-check) - blocker: not-attempted; b2 + wrong-key PASS on the re-decode (PREREG-N7VIV54L); next: verifier session (account 3), ~$5
- Judge calibration for this hand - blocker: not-attempted; the fr16 judge FAILs the known-good f.103r control at this noise (N5-VIV54, N6-VIV53); next: score a lower-noise control (the clerk decipherment's own text, or f.103r after a lookalike pass) to see whether the judge can gate at all, ~$2
- fr.16104 ink 52 (5 Sept 1572, to the Queen, ~270 lines) - blocker: not-attempted; no decipherment beside it (N5-VIVTAB); next: look at c179/c181, then crops + 2 blind passes per page, decode with key.tsv, ~$30
- fr.16104 5 Sept 1572 cipher block (ff.157-159v) against its decipherment ff.162r-163r - blocker: not-attempted; known-plaintext check, not a reading; next: crops + two blind passes, aligned as tx/vivk_test.py, ~$15
- Unviewed stretches of the per-piece table - blocker: not-attempted; fr.16104 c1-c169, c192-c324 and fr.16105 c1-c94, c113-c191 not viewed (N5-VIVTAB); a decipherment of 63 filed in another volume (fr.16106 holds one such stray) not checked; next: 1200 px pass every second canvas, contact sheets, ~$3
- fr.16105 f.104r, first page of the decipherment - blocker: illegible; native crop shows word shapes only (N4-VIV3)
- Spanish-side copies (AGS Estado K) and Gachard vol. I - blocker: needs-physical-access; AGS is not digitised in a route this worker could open
## Escalation (4 Oct 2026, N7-VIV53L; from the N7-VIV54L list)
- [x] siblings: ink 38 located; ink 40 vs 41 aligned (N5-VIVK); decipherment 51 found (N5-VIV5S); per-piece table (N5-VIVTAB); ink 54 read (N5-VIV54); ink 53 ff.170r-171v read (N6-VIV53, N6-VIV53B); ink 63 ff.190r-194r read except f.194r lines 5-10 (N6-VIV63, N6-VIV63B, N6-VIV63C)
- [x] clear-pages: decipherments 41, 44, 51, 68, 71, 76 are on the leaves; inks 54 and 53 interlinear words used as gloss checks (N5-VIV54 PASS, N6-VIV53 FAIL at the floor); f.171v has none (N6-VIV53B); ink 63 has none (order gate b2 instead)
- [x] known-keys: Tomokiyo's 1572-74 key on disk and held-out PASS (N5-VIVK); applied to inks 54, 53 and 63
- [x] print: Gachard I-II, d'Ars, Catherine IV-V, Groen IV read; Kervyn I-VI grepped (N6-KERV); print_check on ink 54, 53 and 63 phrases (pc63b/, pc63c/)
- [retired] key-rebuild: tools/stream_align.py from a flat start did not converge on this material (Arm A, 2 of 30 codes); a published key exists
- [x] image-check: fr.16104 c170-191 and fr.16105 c95-112, c192-248 viewed; native regions of f.173r-v, ff.170r-171v, ff.190r-194r (N5-VIV54, N6-VIV53, N6-VIV63, N6-VIV63B, N6-VIV63C)
- [ ] retry: ink 63 f.194r lines 5-10 (deskewed cut); ink 63 label questions (lookalike pass, overlap dedup); ink 53 residual unsettled tiles and gaps (window look-alike pass done, N7-VIV53L); ink 54 sorter/window audit and key question (lookalike pass done, N7-VIV54L)
Verdict: keep going: 14 internal gaps; cheapest next: ink 54 key question on the key image, ~$0.5, then the ink 53 and ink 54 audits (depth re-check), ~$5 each

Gate output (N7-VIV53L, 4 Oct 2026): `OK keep-going fr16104-vivonne-spain-1572: keep going: 14 internal gap(s), 1 step(s) untried`; `tx/viv53L_decode.py --check`: reading_piece53_L.tsv up to date; viv53/viv54/viv63/viv54L `--check` up to date

## N7-VIV63G (4 Oct 2026, LANE-NEAR7 worker, account 2): ink 63 f.194r lines 5-10, whole-piece gates re-run, key-questions context table
Brief: .claude/briefs/runs/2026-10-04-ytbiz-near7-wave1.md "N7-VIV63G". Claimed 12:37 UTC, box to 13:53 UTC. PREREG-N7VIV63G.md pushed c8c6983d before any
crop, pass or decode. Units stated in ROOM.md before the first subagent call (2 blind Sonnet passes + 1 script reconciliation; table by script).

**Crop** (1 Gallica request: c199 native region 4800,200,2950,2700, the N6-VIV63C region; crops gitignored, manifest committed):
```
# region rotated -1.4 deg (PIL BICUBIC, fill 255, no expand); rows 840-1530 saved as f194r_mid_rot.jpg (a first try at rows 770-1450 caught
# page line 4 on top and cut line 10 off: seen on the overlay, discarded before any pass), then
$ python3 tools/iiif_lines.py --image f194r_mid_rot.jpg --out crops --prefix c199_f194r_mid --distance 80 --max-width 1100 --overlap 150 --debug
  f194r_mid_rot.jpg (local): region 2950x690, 6 lines, 6 bands x 3 segments; pitch 114 distance 80 prominence 260.2
  centres (region y): 57 172 286 396 516 632; wrote 18 crops   (manifest: images/p63/manifest_f194r_mid.json)
```
Overlay checked by eye before any pass: one written line per band. Page-line identity: band 1 begins "to z m o m d" (= the old top-cut L05, which the
old cut had straddled) and band 6 is the line directly above the low block's L01 ("d d n tz b @ ..."). Same-row pass A/B similarity 0.80-0.92 against
0.16-0.32 off the diagonal: the two readers read the same line in every band (the N6-VIV63C failure, readers on different lines, is absent).
Two blind Sonnet passes (tx/f194r_mid_pass{A,B}.tsv) frozen at b8a6ebde, composed as f.194r rows L05-L10 by tx/viv63c_f194r_compose.py (extended; rows
L01-L04 and L11-L20 unchanged), then tx/viv63_clean.py f194r, tools/reconcile_passes.py, tx/viv63_decode.py. No new label rule.
| new lines | signs A / B | agree (nw) | err_2reader | H / M / U |
|---|---|---|---|---|
| f.194r L05-L10 | 301 / 307 | 258/310 = 83.2% | 0.168 | 219 / 41 / 41 (301 tokens) |
Whole piece before -> after: 15,461 -> **15,762 tokens; H 11,932 -> 12,151 (0.772 -> 0.771), M 2,288 -> 2,329, U 1,241 -> 1,282.** f.194r reconcile now
20 lines, agreement 80.8% (819/1014). `tx/viv63_decode.py --check` up to date; viv53/viv54 `--check` unchanged and up to date.

**Gates (PREREG-N7VIV63G.md; tx/viv63g_test.py = viv63c_test.py with the new set f.194r L05-L10 and '-G' seed tags; tx/viv63g_result.json; ~6 min).**
| arm | letters | s | b2 null p99 | null median | verdict |
|---|---|---|---|---|---|
| C1 f.103r full | 1,770 | -1.715 | -1.909 | -1.962 | passes, headroom (reproduces N6-VIV63) |
| C2 ink 54 full | 1,793 | -1.658 | -1.829 | -1.878 | passes, headroom (reproduces N6-VIV63) |
| C1 subsampled to 260 letters | 260 | -1.644 | -1.779 | -1.917 | passes, headroom |
| C2 subsampled to 260 letters | 260 | -1.579 | -1.707 | -1.859 | passes, headroom |
| (i) new lines f.194r L5-10 | 260 | **-1.599** | -1.742 | -1.894 | **PASS** |
| (ii) whole piece ff.190r-194r | 14,480 | **-1.548** | -1.836 | -1.851 | **PASS** |
**Specificity** (registered rule unchanged; 200 wrong keys, seed 20260967-spec-G): 43 of 200 (21.5%) pass bare b2; wrong-key margin median -0.023,
p95 +0.040, p99 **+0.064**, max +0.122; real margin **+0.288** -> **PASS**. (Different wrong-key draws from N6-VIV63C's, so its p99 0.048 / max 0.078
are not reproduced; the real margin is.) This is a re-run of the existing gates on a piece that is ~98% already gated, not a fresh test.

**Reading of the new lines** (decoded, verbatim; by eye, interpretation, not a gate): L05 "qae_eochentunggentilho_t_bgen_esho_t_deconridanc_" [... un
gentilhom(me) ... de confidanc(e)], L06 "..._ectdutroubleqriaestin" [... du trouble ...], L08 "...dauoit...", L09 "...ccesteocba_ioneturrendre..."
[... ceste oc(c)asion et ... rendre]. Longest all-H, gap-free decoded stretch in the new lines: **11 letters** ("deconridanc", L05; then "leqriaestin"
L06 11, "etauosloit" L08 10). Nothing near the ~42-letter authentication distance (AUDIT 2 4a); depth is not this job's to set.

**Key-questions context table** (tx/viv63g_keyctx.py, writes tx/viv63g_keyctx.tsv, `--check`; PREREG-N7VIV63G "not a gate"; **proposals only, key.tsv
untouched**). ink40 = letters the clerk decipherment aligns to the code (tx/key_support.py's DP); ink63 n = occurrences in reading_piece63.tsv;
context = decoded 2 letters either side; fill = each letter a-z substituted at every ink-63 position, 4-gram (fr16) gain over the window, top 3.
| code | role | key value | ink40 n | ink40 aligned top5 | ink63 n | context top5 | fill top3 | fill top = key |
|---|---|---|---|---|---|---|---|---|
| y | question | h | 260 | l:19,r:18,h:17,t:17,e:16 | 564 | re._e:5,es._e:4,en._a:4,er._e:4,cc.oo:4 | l:+0,i:-94,n:-246 (n_win 470) | no |
| o | question | - | 54 | s:7,e:7,c:4,u:4,o:3 | 238 | eh.es:3,sh.es:3,ul.ie:3,eh.ai:3,ih.eu:3 | i:+0,l:-81,s:-313 (n_win 225) | - |
| c | question | - | 86 | u:12,l:9,a:8,r:5,t:5 | 194 | de.ou:3,it.ar:3,ae.ui:3,nt.re:3,re.ri:3 | l:+0,p:-71,i:-82 (n_win 192) | - |
| V | question | - | 147 | n:14,l:13,s:12,t:11,m:8 | 179 | di.ai:3,ce.es:3,eo.ou:3,.he:3,te.u:2 | n:+0,s:-100,l:-112 (n_win 173) | - |
| e | question | - | 10 | i:2,u:1,r:1,s:1,l:1 | 161 | co.ta:18,ho.t_:3,ho.ta:2,st._h:2,it.oi:2 | n:+0,l:-13,i:-24 (n_win 148) | - |
| 2 | question | - | 55 | p:5,a:5,l:4,u:4,m:4 | 97 | ce.ec:2,he.oi:2,de.en:2,it.ai:1,ot.ar:1 | l:+0,n:-31,s:-43 (n_win 96) | - |
| r | question | - | 0 | - | 85 | la.ee:1,et.cr:1,ou.es:1,tt.oa:1,el.a_:1 | i:+0,e:-12,l:-31 (n_win 79) | - |
| m | known-answer (held out) | e | 859 | e:645,i:20,a:19,u:16,s:16 | 2379 | _a.nt:16,cc.st:16,oi.nt:14,h_.ur:10,nt.nd:10 | e:+0,i:-1139,a:-2129 (n_win 1961) | yes |
| x | known-answer (held out) | s | 202 | s:118,o:9,n:7,r:6,e:6 | 647 | ce.te:10,ae.ae:7,qe.el:7,on.er:7,ce.ae:5 | s:+0,n:-301,l:-318 (n_win 608) | yes |
| g | known-answer (held out) | r | 305 | r:167,s:12,u:11,t:8,l:8 | 884 | ai.es:8,se.ui:8,_a.ti:6,cc.oa:6,sg.an:6 | r:+0,l:-568,i:-776 (n_win 817) | yes |
| a | known-answer (held out) | u | 100 | u:64,s:5,a:4,d:3,l:3 | 366 | _a.oi:5,ea.oi:3,en.oa:3,da.oi:3,re.ce:2 | i:+0,l:-58,s:-180 (n_win 352) | no |
| R | known-answer (held out) | t | 60 | t:36,c:4,r:3,y:2,l:2 | 219 | ou.eo:4,en.en:3,en.te:2,en.:2,oi.au:2 | i:+0,t:-5,l:-22 (n_win 200) | no |
| j | known-answer (held out) | l | 49 | l:30,u:3,r:3,m:2,d:2 | 106 | ou.ou:3,ae.eo:3,au.at:2,cu.ie:2,ai._a:2 | l:+0,n:-64,t:-68 (n_win 105) | yes |
| 3 | known-answer (held out) | d | 116 | d:43,m:13,l:6,p:6,r:5 | 280 | an.eu:5,an.e_:3,ne.eo:3,on.e_:2,ne.eh:2 | l:+0,s:-58,d:-67 (n_win 269) | no |
| 6 | known-answer (held out) | l | 97 | l:45,m:6,t:6,e:6,s:5 | 270 | ae.qa:11,ou._i:5,au.qa:4,au.tr:4,se.qa:4 | l:+0,i:-190,r:-195 (n_win 259) | yes |
| L | known-answer (held out) | r | 30 | r:12,e:5,t:3,l:2,q:1 | 81 | oi._a:2,st.oa:2,un.en:1,t_.ra:1,_e.oa:1 | i:+0,n:-27,l:-31 (n_win 74) | no |
| to | known-answer (held out) | q | 33 | q:10,n:4,e:2,h:1,m:1 | 96 | el.ae:16,ul.io:2,el.se:2,el._e:2,ul.ae:2 | l:+0,i:-39,e:-71 (n_win 89) | no |
| h | known-answer (held out) | d | 27 | d:11,l:2,m:2,p:1,a:1 | 80 | en.re:4,an.re:3,en.ra:3,an.ea:3,an.e_:2 | d:+0,t:-7,l:-12 (n_win 79) | yes |
| k | known-answer (held out) | d | 33 | d:12,c:2,t:1,o:1,m:1 | 165 | en.re:12,an.es:4,ea.ue:3,an.eu:3,en.qu:3 | d:+0,l:-94,i:-129 (n_win 160) | yes |

**Method check (known answer, held out):** the fill's top letter is the key's own value for 3/3 high-frequency codes (m, x, g; 600-2,000 windows) but only
**5/9 at the question codes' own N** (74-352 windows: j, 6, h, k right; a, R, 3, L, to wrong), and every miss lands on **i or l**. So the proposals y->l,
o->i, c->l, 2->l, r->i fall exactly inside the method's bias and are **not evidence** at this N. Weak proposals that sit outside that bias: **V -> n** (fill
n, margin 100; ink 40 aligns n:14 top but diffuse) and e -> n (margin only 13). For **y** the ink-40 alignment (l:19, r:18, h:17) and the fill (l) agree on l over
the key's h, which is the strongest of the seven but still M (diffuse alignment, biased method). **e**'s dominant context "co.ta" (18x) is the
"co_tandeur" [commandeur] pattern: no single letter in that slot gives the French (the fill's n gives "contandeur"), which points to e being a sign for
"m(m)" or an abbreviation, or to a misread of the following t -- a question for Tomokiyo's key image (cells m, n), not settled here (rule 4: never the
reading that decodes better). None of these is applied anywhere; a key change is a separate graded step with its own PREREG and control.

Requests: gallica.bnf.fr 1 (one native region). Subagent calls: 2 Sonnet (blind passes A, B). print_check not run (no new stretch >= 20 letters).
Cost: see the lane ledger. Report: what was found is above; no printed plaintext of these lines was searched for beyond the existing AUDIT 3 log. Novelty not classified.
**Result line: piece 63 whole-piece gates re-run after f.194r L5-10: PASS** (b2 (i) and (ii) with both controls passing with headroom, specificity PASS).

## Remaining gaps (N7-VIV63G refresh, 4 Oct 2026; supersedes the N7-VIV53L list above, all its other lines kept)
Read so far: ink 40 checked against its decipherment 41 with Tomokiyo's key (N5-VIVK PASS); ink 54 read with key.tsv, gloss check PASS (N5-VIV54), window look-alike pass + re-decode, b2 + wrong-key PASS (N7-VIV54L); ink 53
ff.170r-171v read, b2 + wrong-key PASS (N6-VIV53B), window look-alike pass + ': :' join + re-decode, b2 + wrong-key PASS again (N7-VIV53L); ink 63 ff.190r-194r read in full (f.194r L5-10 added by N7-VIV63G): b2 PASS on every part (N6-VIV63, N6-VIV63B,
N6-VIV63C, N7-VIV63G), whole piece -1.548 vs p99 -1.836, wrong-key specificity PASS (real 0.288 vs p99 0.064), H 12,151 / M 2,329 / U 1,282 of 15,762 tokens.
Pieces with no decipherment located: fr.16105 63, fr.16104 52, 53, 54 (and 38, whose twin is deciphered).
- ink 63 N4 (audit 1 done 4 Oct 2026 by VIV63-A1, AUDIT.md AUDIT 3: N3, D1 fragments read, key published; recipient the King; no decipherment in fr.16105 c95-c248) - blocker: not-attempted; Flament, L'ambassade du marquis de Saint-Gouard en Espagne 1572-1574 (1996, OCLC 988579745) and Ribera (2007) unread, fr.16105 c1-c94 and the fr.16106 pieces Gachard skips not viewed; next: a LOCAL-QUEUE row for Flament and Ribera on 10 Oct 1573 (interlibrary or the owner's browser), ~$1
- tools/iiif_lines.py on steep, uneven line slopes - blocker: not-attempted; --follow-slope (and --centres with it) snapped bands onto neighbouring lines on f.194r; next: an option to deskew the region by a fitted angle before a flat cut (what N6-VIV63C did by hand with PIL), with an offline test, ~$2
- ink 63 key questions (y, single o, c, V, e, 2, r) - blocker: not-attempted; context table done (N7-VIV63G, tx/viv63g_keyctx.tsv): the 4-gram fill is right on only 5/9 held-out codes at this N and biased to i/l, so only y->l (alignment + fill agree), V->n and e as an "m(m)" sign in "co_tandeur" stand as weak proposals; next: read cells h, l, m, n of Tomokiyo's key image (henryiii_Vivonne1.png) for a y-like l homophone, a V-like n and an e-like m/mm sign, then a PREREG'd key-change step with the wrong-key control, ~$1.5
- ink 63 label splits and overlap duplication - blocker: not-attempted; r/z, 2/z (f.193v 25x), c/e and 6/b (f.192r, 19x) left at pass A; readers wrote some s1/s2 overlaps twice (f.192r L06, L34; f.193r L07); f.193r err_2reader 0.297; next: tools/lookalike_pass.py on those pairs + a pre-registered overlap-dedup step in tx/viv63_clean.py, re-decode, ~$4
- ink 53 audit (depth re-check) - blocker: not-attempted; AUDIT 2 (VIV53-A1) set N3 / D1; the N7-VIV53L re-decode passes b2 + wrong-key again (PREREG-N7VIV53L) but no repair-free stretch reaches ~42 letters (longest 20); next: verifier session (account 3) on reading_piece53_L.tsv, ~$5
- ink 53 residual label questions - blocker: not-attempted; 82 split tiles left UNSETTLED by the 2-of-3 rule and 270 one-reader gaps never re-read (tx/lookalike53L/*/focus.tsv), the ': :'-as-null alternative, and "rauldhoit" (f.171r L15, where French wants "pourroit") unresolved (N7-VIV53L); next: owner's sign sorter on the focus files, or a window re-read of the gap tiles (tx/viv53L_windows.py extended to gaps), ~$2
- ink 54 clean reading - blocker: not-attempted; window look-alike pass done (residual 0.134), true-error audit a non-test, no stretch near ~42 letters (N7-VIV54L); next: owner's sign sorter on tx/lookalike54/*_focus.tsv (275 questions) or a window-instrument audit (lookalike_pass.py audit + viv53L_windows.py audit), ~$1.5
- ink 54 key question "to z" (qae) - blocker: not-attempted; 13 occurrences, no reader split, ink 40 alignment never gives u for z (N7-VIV54L); next: read Tomokiyo's cell u / q on henryiii_Vivonne1.png for a z-like homophone or a "qu" sign, ~$0.5
- ink 54 audit (depth re-check) - blocker: not-attempted; b2 + wrong-key PASS on the re-decode (PREREG-N7VIV54L); next: verifier session (account 3), ~$5
- Judge calibration for this hand - blocker: not-attempted; the fr16 judge FAILs the known-good f.103r control at this noise (N5-VIV54, N6-VIV53); next: score a lower-noise control (the clerk decipherment's own text, or f.103r after a lookalike pass) to see whether the judge can gate at all, ~$2
- fr.16104 ink 52 (5 Sept 1572, to the Queen, ~270 lines) - blocker: not-attempted; no decipherment beside it (N5-VIVTAB); next: look at c179/c181, then crops + 2 blind passes per page, decode with key.tsv, ~$30
- fr.16104 5 Sept 1572 cipher block (ff.157-159v) against its decipherment ff.162r-163r - blocker: not-attempted; known-plaintext check, not a reading; next: crops + two blind passes, aligned as tx/vivk_test.py, ~$15
- Unviewed stretches of the per-piece table - blocker: not-attempted; fr.16104 c1-c169, c192-c324 and fr.16105 c1-c94, c113-c191 not viewed (N5-VIVTAB); a decipherment of 63 filed in another volume (fr.16106 holds one such stray) not checked; next: 1200 px pass every second canvas, contact sheets, ~$3
- fr.16105 f.104r, first page of the decipherment - blocker: illegible; native crop shows word shapes only (N4-VIV3)
- Spanish-side copies (AGS Estado K) and Gachard vol. I - blocker: needs-physical-access; AGS is not digitised in a route this worker could open
## Escalation (4 Oct 2026, N7-VIV63G; from the N7-VIV53L list)
- [x] siblings: ink 38 located; ink 40 vs 41 aligned (N5-VIVK); decipherment 51 found (N5-VIV5S); per-piece table (N5-VIVTAB); ink 54 read (N5-VIV54); ink 53 ff.170r-171v read (N6-VIV53, N6-VIV53B); ink 63 ff.190r-194r read in full (N6-VIV63, N6-VIV63B, N6-VIV63C, N7-VIV63G)
- [x] clear-pages: decipherments 41, 44, 51, 68, 71, 76 are on the leaves; inks 54 and 53 interlinear words used as gloss checks (N5-VIV54 PASS, N6-VIV53 FAIL at the floor); f.171v has none (N6-VIV53B); ink 63 has none (order gate b2 instead)
- [x] known-keys: Tomokiyo's 1572-74 key on disk and held-out PASS (N5-VIVK); applied to inks 54, 53 and 63
- [x] print: Gachard I-II, d'Ars, Catherine IV-V, Groen IV read; Kervyn I-VI grepped (N6-KERV); print_check on ink 54, 53 and 63 phrases (pc63b/, pc63c/)
- [retired] key-rebuild: tools/stream_align.py from a flat start did not converge on this material (Arm A, 2 of 30 codes); a published key exists
- [x] image-check: fr.16104 c170-191 and fr.16105 c95-112, c192-248 viewed; native regions of f.173r-v, ff.170r-171v, ff.190r-194r (N5-VIV54, N6-VIV53, N6-VIV63, N6-VIV63B, N6-VIV63C, N7-VIV63G)
- [ ] retry: ink 63 key questions on the key image (context table done, N7-VIV63G); ink 63 label questions (lookalike pass, overlap dedup); ink 53 residual unsettled tiles and gaps (window look-alike pass done, N7-VIV53L); ink 54 sorter/window audit and key question (lookalike pass done, N7-VIV54L)
Verdict: keep going: 13 internal gaps; cheapest next: ink 54 key question on the key image, ~$0.5, then the ink 53 and ink 54 audits (depth re-check), ~$5 each

## N7-VIV54Q (4 Oct 2026, LANE-NEAR7 worker, account 2): ink 54 key question "to z" = "qae", checked against the key image
Brief: .claude/briefs/runs/2026-10-04-ytbiz-near7-wave1.md "N7-VIV54Q". Claimed 13:18 UTC, box to 13:58 UTC. Disk only: 0 Gallica, 0 cryptiana
requests (the key image sources/cryptiana/web/henryiii_Vivonne1.png and the native f.173r-v line crops c187_f173r_* / c188_f173v_* were on disk;
the crops are native, 1600 px windows of the 3750 px region). 0 subagent calls; read by this worker's own eye.

**Key image (Tomokiyo, henryiii_Vivonne1.png, 543 x 213 px).** Column u has four entries, not the two key_tomokiyo.tsv/key.tsv record: row 1 "oo",
row 2 "a", **row 3 a Σ-shaped sign** (top bar, upright stem bending back, bottom bar; no diagonal), row 4 a k-like sign with an arrow to a circled
variant. Column a row 3 is the flat z (diagonal stroke), which key.tsv maps z -> a. Column q has "to" (row 1) and the looped @ (row 5). Below the
table, the codeword row gives "Espagnaols / quel? / que / votre majeste"; its "que" entry is a single two-part sign, not "to" + a letter sign.

**The crops (native, autocontrast only).** Montage tx/viv54Q/to_sign_evidence.jpg (key cells col a and col u at top; then f.173r L11, L14, L17, L20,
L05-end, f.173v L12 x2; then two ordinary z's for comparison, f.173r L14 pos 4 and L07 "tz z a"). In all 7 "to"+sign occurrences in the montage, the
sign after "to" is the same Σ/I shape as col u row 3: two horizontal bars joined by a near-upright stem. The ordinary z's on the same lines are
different glyphs: a crossed z (L14) and a 2-shaped z with a diagonal (L07). Also seen in the line stacks (not in the montage): f.173v L04 (both
"to"s), L14 and L17 carry the same shape after "to". Those include positions the passes labelled R (f.173v L12 "to R m" at the line start) and x (L04 "to x P").
f.173r L10 and f.173v L02 "to z tz" look 3-like (ʒ) at this scale; not settled.

**Contexts in the committed transcriptions (all 18 pages, *_rec.tsv):** the label after "to" is z 57 times, x 23, 2 23, a 12, then a tail. On
f.173r-v: "to z m" 8 (que), "to z tz" 4 (decoded "qai", French "qui"), "to z P" 1; f.173v also "to R" 3, "to x" 1. Reading "u" in that slot gives
que/qui throughout; the stated z -> a and x -> s give "qae"/"qai"/"qs". This is a context fact, not the evidence: the evidence is the glyph shape matched to a
key cell. The 2-of-3 rule could not reach it because no reader ever wrote a separate label for it (N7-VIV54L).

**Answer to the key question (grade of the evidence: the key cell is H, read from the published key; the per-position identification is by eye,
7 positions in the montage).** The "z" after "to" in ink 54 is not the col-a flat z but the col-u row-3 sign, = u. key.tsv is **not changed**: key.tsv maps
transcription labels, and no label in the transcription isolates this glyph (z, R and x each merge it with their own cells). Changing z -> u
would be wrong for the other ~120 aligned z's (ink 40: z -> a 77). Changing it only after "to" would be a context rule. Either way that is settling a
label by what decodes better (PREREG-N7VIV54L (i)), so reading_piece54_L.tsv is unchanged and nothing moved. Next step (gaps list): a pre-registered
new label for col u row 3, relabelled position by position from the native crops (not by context), then re-decode with --check. That
would remove one letter repair from every que/qui (about 13 on ink 54; the "to z"/"to x" contexts on inks 53/63 need the same per-position check
first). Also noted: key_tomokiyo.tsv and tx/SIGNS.md omit col u rows 3-4 and col q's codeword "que" sign. Adding them is part of that step, not done here.
Report what was found and where it was not found; no novelty classified. Requests: none. Subagent calls: 0. Cost: see the lane ledger.

## Remaining gaps (N7-VIV54Q refresh, 4 Oct 2026; supersedes the N7-VIV63G list above, all its other lines kept)
Read so far: ink 40 checked against its decipherment 41 with Tomokiyo's key (N5-VIVK PASS); ink 54 read with key.tsv, gloss check PASS (N5-VIV54), window look-alike pass + re-decode, b2 + wrong-key PASS (N7-VIV54L); ink 53
ff.170r-171v read, b2 + wrong-key PASS (N6-VIV53B), window look-alike pass + ': :' join + re-decode, b2 + wrong-key PASS again (N7-VIV53L); ink 63 ff.190r-194r read in full (f.194r L5-10 added by N7-VIV63G): b2 PASS on every part (N6-VIV63, N6-VIV63B,
N6-VIV63C, N7-VIV63G), whole piece -1.548 vs p99 -1.836, wrong-key specificity PASS (real 0.288 vs p99 0.064), H 12,151 / M 2,329 / U 1,282 of 15,762 tokens.
Pieces with no decipherment located: fr.16105 63, fr.16104 52, 53, 54 (and 38, whose twin is deciphered).
- ink 63 N4 (audit 1 done 4 Oct 2026 by VIV63-A1, AUDIT.md AUDIT 3: N3, D1 fragments read, key published; recipient the King; no decipherment in fr.16105 c95-c248) - blocker: not-attempted; Flament, L'ambassade du marquis de Saint-Gouard en Espagne 1572-1574 (1996, OCLC 988579745) and Ribera (2007) unread, fr.16105 c1-c94 and the fr.16106 pieces Gachard skips not viewed; next: a LOCAL-QUEUE row for Flament and Ribera on 10 Oct 1573 (interlibrary or the owner's browser), ~$1
- tools/iiif_lines.py on steep, uneven line slopes - blocker: not-attempted; --follow-slope (and --centres with it) snapped bands onto neighbouring lines on f.194r; next: an option to deskew the region by a fitted angle before a flat cut (what N6-VIV63C did by hand with PIL), with an offline test, ~$2
- ink 63 key questions (y, single o, c, V, e, 2, r) - blocker: not-attempted; context table done (N7-VIV63G, tx/viv63g_keyctx.tsv): the 4-gram fill is right on only 5/9 held-out codes at this N and biased to i/l, so only y->l (alignment + fill agree), V->n and e as an "m(m)" sign in "co_tandeur" stand as weak proposals; next: read cells h, l, m, n of Tomokiyo's key image (henryiii_Vivonne1.png) for a y-like l homophone, a V-like n and an e-like m/mm sign, then a PREREG'd key-change step with the wrong-key control, ~$1.5
- ink 63 label splits and overlap duplication - blocker: not-attempted; r/z, 2/z (f.193v 25x), c/e and 6/b (f.192r, 19x) left at pass A; readers wrote some s1/s2 overlaps twice (f.192r L06, L34; f.193r L07); f.193r err_2reader 0.297; next: tools/lookalike_pass.py on those pairs + a pre-registered overlap-dedup step in tx/viv63_clean.py, re-decode, ~$4
- ink 53 audit (depth re-check) - blocker: not-attempted; AUDIT 2 (VIV53-A1) set N3 / D1; the N7-VIV53L re-decode passes b2 + wrong-key again (PREREG-N7VIV53L) but no repair-free stretch reaches ~42 letters (longest 20); next: verifier session (account 3) on reading_piece53_L.tsv, ~$5
- ink 53 residual label questions - blocker: not-attempted; 82 split tiles left UNSETTLED by the 2-of-3 rule and 270 one-reader gaps never re-read (tx/lookalike53L/*/focus.tsv), the ': :'-as-null alternative, and "rauldhoit" (f.171r L15, where French wants "pourroit") unresolved (N7-VIV53L); next: owner's sign sorter on the focus files, or a window re-read of the gap tiles (tx/viv53L_windows.py extended to gaps), ~$2
- ink 54 clean reading - blocker: not-attempted; window look-alike pass done (residual 0.134), true-error audit a non-test, no stretch near ~42 letters (N7-VIV54L); next: owner's sign sorter on tx/lookalike54/*_focus.tsv (275 questions) or a window-instrument audit (lookalike_pass.py audit + viv53L_windows.py audit), ~$1.5
- ink 54 key question "to z" (qae) - blocker: not-attempted; the key image answers it at the cell (N7-VIV54Q: the sign after "to" is Tomokiyo col u row 3, a Σ/I shape, = u; readers merged it into label z, or R/x), but no transcription label isolates it, so the reading has not moved; next: PREREG a new label (e.g. "Z_u", key.tsv grade H, col u row 3) and relabel only positions where the glyph is checked by eye on native crops (13 "to"+sign on f.173r-v, then the 57 "to z" / 23 "to x" contexts on the other 15 pages), regenerate reading_piece54_L/53_L/63 with --check, ~$1.5
- ink 54 audit (depth re-check) - blocker: not-attempted; b2 + wrong-key PASS on the re-decode (PREREG-N7VIV54L); next: verifier session (account 3), ~$5
- Judge calibration for this hand - blocker: not-attempted; the fr16 judge FAILs the known-good f.103r control at this noise (N5-VIV54, N6-VIV53); next: score a lower-noise control (the clerk decipherment's own text, or f.103r after a lookalike pass) to see whether the judge can gate at all, ~$2
- fr.16104 ink 52 (5 Sept 1572, to the Queen, ~270 lines) - blocker: not-attempted; no decipherment beside it (N5-VIVTAB); next: look at c179/c181, then crops + 2 blind passes per page, decode with key.tsv, ~$30
- fr.16104 5 Sept 1572 cipher block (ff.157-159v) against its decipherment ff.162r-163r - blocker: not-attempted; known-plaintext check, not a reading; next: crops + two blind passes, aligned as tx/vivk_test.py, ~$15
- Unviewed stretches of the per-piece table - blocker: not-attempted; fr.16104 c1-c169, c192-c324 and fr.16105 c1-c94, c113-c191 not viewed (N5-VIVTAB); a decipherment of 63 filed in another volume (fr.16106 holds one such stray) not checked; next: 1200 px pass every second canvas, contact sheets, ~$3
- fr.16105 f.104r, first page of the decipherment - blocker: illegible; native crop shows word shapes only (N4-VIV3)
- Spanish-side copies (AGS Estado K) and Gachard vol. I - blocker: needs-physical-access; AGS is not digitised in a route this worker could open
## Escalation (4 Oct 2026, N7-VIV54Q; from the N7-VIV63G list)
- [x] siblings: ink 38 located; ink 40 vs 41 aligned (N5-VIVK); decipherment 51 found (N5-VIV5S); per-piece table (N5-VIVTAB); ink 54 read (N5-VIV54); ink 53 ff.170r-171v read (N6-VIV53, N6-VIV53B); ink 63 ff.190r-194r read in full (N6-VIV63, N6-VIV63B, N6-VIV63C, N7-VIV63G)
- [x] clear-pages: decipherments 41, 44, 51, 68, 71, 76 are on the leaves; inks 54 and 53 interlinear words used as gloss checks (N5-VIV54 PASS, N6-VIV53 FAIL at the floor); f.171v has none (N6-VIV53B); ink 63 has none (order gate b2 instead)
- [x] known-keys: Tomokiyo's 1572-74 key on disk and held-out PASS (N5-VIVK); applied to inks 54, 53 and 63
- [x] print: Gachard I-II, d'Ars, Catherine IV-V, Groen IV read; Kervyn I-VI grepped (N6-KERV); print_check on ink 54, 53 and 63 phrases (pc63b/, pc63c/)
- [retired] key-rebuild: tools/stream_align.py from a flat start did not converge on this material (Arm A, 2 of 30 codes); a published key exists
- [x] image-check: fr.16104 c170-191 and fr.16105 c95-112, c192-248 viewed; native regions of f.173r-v, ff.170r-171v, ff.190r-194r (N5-VIV54, N6-VIV53, N6-VIV63, N6-VIV63B, N6-VIV63C, N7-VIV63G)
- [ ] retry: ink 63 key questions on the key image (context table done, N7-VIV63G); ink 63 label questions (lookalike pass, overlap dedup); ink 53 residual unsettled tiles and gaps (window look-alike pass done, N7-VIV53L); ink 54 sorter/window audit (lookalike pass done, N7-VIV54L) and the col-u-row-3 relabel (key cell found, N7-VIV54Q)
Verdict: keep going: 13 internal gaps; cheapest next: ink 54 col-u-row-3 relabel (PREREG, per-position by eye), ~$1.5, then the ink 53 and ink 54 audits (depth re-check), ~$5 each

## N7-VIV54R (4 Oct 2026, LANE-NEAR7 worker, account 2): ink 54, the col-u row-3 sign as its own label
Brief: .claude/briefs/runs/2026-10-04-ytbiz-near7-wave1.md "N7-VIV54R". Claimed 13:45 UTC, box to 14:30 UTC. Disk only (0 requests).
PREREG-N7VIV54R.md pushed 9210e52f before any window, judgement or relabel. Units stated there: scripts + 1 Sonnet judge call + tally.

**Key cell.** Tomokiyo's henryiii_Vivonne1.png, column u row 3, read at 3x: a Sigma/I-shaped sign under "a", plainly legible -> key.tsv
row `Zu` -> u, grade C (published key; no clerk-alignment support, n_aligned 0), also in key_tomokiyo.tsv. No transcription uses the label
yet, so every committed reading is unchanged (all five --check pass). Not added: col u row 4 (k-like sign) and the col q codeword "que" sign.

**Instrument (PREREG).** Every ink 54 position labelled z, x, R, 3 or 2 in N7-VIV54L's settled sequence: 169 (f.173r z 54, x 15, 3 10,
2 2, R 1; f.173v z 55, x 24, R 6, 3 2). Windows by the N7-VIV53L instrument (tx/viv54R_windows.py, 29 montages, regenerable, not
committed: 45 MB) + a reference image (tx/lookalike54/viv54R_win/ref.png: col u row 3 vs col a row 3 flat z). One value-blind Sonnet
call: no decoded text, key value or hypothesis in the prompt. Classes SIGMA / ZED / OTHER / UNSURE (tx/lookalike54/viv54R_judge.tsv).

**Result: NON-TEST, not applied.** SIGMA 9 (H 4, M 5), ZED 102, OTHER 42, UNSURE 16. Built-in check: of the 18 positions right after a
"to" label (the known-positive subset; the PREREG named N7-VIV54Q's 13 eye-checked ones, the script counts every after-"to" position,
18), only **3 SIGMA at H/M vs >= 7 required**; other positions 6/151 SIGMA (<= 50%, that half passes). The reader said the red ticks were
often off and it located signs from neighbour labels, and its note column is one generic phrase in every row (no stroke feature), so the
instrument, not the glyph question, failed: this result neither confirms nor refutes N7-VIV54Q's by-eye identification of 7 positions.
tx/lookalike54/viv54R_relabel.tsv is written empty; reading_piece54_L.tsv is unchanged (`tx/viv54L_decode.py --check` up to date).
Because the re-decode did not change, b2 + specificity were not re-run: N7-VIV54L's numbers stand (b2 -1.636 vs p99 -1.812 PASS; wrong-key
margin 0.176 vs p99 0.043 PASS; controls C1 -1.715 vs -1.915, C2 -1.667 vs -1.846). tx/viv54R_test.py (seed 20261054R) is in place for
the next attempt.

**Three longest repair-free stretches (unchanged from N7-VIV54L; liberties as AUDIT 2 4a counts them; the auditor re-counts):**
f.173v L03 "tousiour[s] [q]ont doubte [q]u c'este", 25 letters, word division, 1 repair (o->s), 2 q liberties, L1 once; f.173r L21
"toute [d]iligence de [U][f]aire", 21 letters, word division, 1 repair (a->d), 1 U sign; f.173v L05 "etdictauoir", 11 letters clean with
word division, L1 once. Nothing near ~42 letters; no new stretch >= 20 letters without repair, so print_check not run.
**Next step:** the instrument is the limit: per-position crops placed by hand-marked x on the native crops (not pos/len estimates), the
same PREREG decision rule; inks 53/63's "to z"/"to x" contexts are not relabelled and need the same check first.
Report what was found and where it was not found; no novelty classified. Requests: none. Subagent calls: 1 Sonnet. Cost: see the lane ledger.

## Remaining gaps (N7-VIV54R refresh, 4 Oct 2026; supersedes the N7-VIV54Q list above, all its other lines kept)
Read so far: ink 40 checked against its decipherment 41 with Tomokiyo's key (N5-VIVK PASS); ink 54 read with key.tsv, gloss check PASS (N5-VIV54), window look-alike pass + re-decode, b2 + wrong-key PASS (N7-VIV54L); ink 53
ff.170r-171v read, b2 + wrong-key PASS (N6-VIV53B), window look-alike pass + ': :' join + re-decode, b2 + wrong-key PASS again (N7-VIV53L); ink 63 ff.190r-194r read in full (f.194r L5-10 added by N7-VIV63G): b2 PASS on every part (N6-VIV63, N6-VIV63B,
N6-VIV63C, N7-VIV63G), whole piece -1.548 vs p99 -1.836, wrong-key specificity PASS (real 0.288 vs p99 0.064), H 12,151 / M 2,329 / U 1,282 of 15,762 tokens.
Pieces with no decipherment located: fr.16105 63, fr.16104 52, 53, 54 (and 38, whose twin is deciphered).
- ink 63 N4 (audit 1 done 4 Oct 2026 by VIV63-A1, AUDIT.md AUDIT 3: N3, D1 fragments read, key published; recipient the King; no decipherment in fr.16105 c95-c248) - blocker: not-attempted; Flament, L'ambassade du marquis de Saint-Gouard en Espagne 1572-1574 (1996, OCLC 988579745) and Ribera (2007) unread, fr.16105 c1-c94 and the fr.16106 pieces Gachard skips not viewed; next: a LOCAL-QUEUE row for Flament and Ribera on 10 Oct 1573 (interlibrary or the owner's browser), ~$1
- tools/iiif_lines.py on steep, uneven line slopes - blocker: not-attempted; --follow-slope (and --centres with it) snapped bands onto neighbouring lines on f.194r; next: an option to deskew the region by a fitted angle before a flat cut (what N6-VIV63C did by hand with PIL), with an offline test, ~$2
- ink 63 key questions (y, single o, c, V, e, 2, r) - blocker: not-attempted; context table done (N7-VIV63G, tx/viv63g_keyctx.tsv): the 4-gram fill is right on only 5/9 held-out codes at this N and biased to i/l, so only y->l (alignment + fill agree), V->n and e as an "m(m)" sign in "co_tandeur" stand as weak proposals; next: read cells h, l, m, n of Tomokiyo's key image (henryiii_Vivonne1.png) for a y-like l homophone, a V-like n and an e-like m/mm sign, then a PREREG'd key-change step with the wrong-key control, ~$1.5
- ink 63 label splits and overlap duplication - blocker: not-attempted; r/z, 2/z (f.193v 25x), c/e and 6/b (f.192r, 19x) left at pass A; readers wrote some s1/s2 overlaps twice (f.192r L06, L34; f.193r L07); f.193r err_2reader 0.297; next: tools/lookalike_pass.py on those pairs + a pre-registered overlap-dedup step in tx/viv63_clean.py, re-decode, ~$4
- ink 53 audit (depth re-check) - blocker: not-attempted; AUDIT 2 (VIV53-A1) set N3 / D1; the N7-VIV53L re-decode passes b2 + wrong-key again (PREREG-N7VIV53L) but no repair-free stretch reaches ~42 letters (longest 20); next: verifier session (account 3) on reading_piece53_L.tsv, ~$5
- ink 53 residual label questions - blocker: not-attempted; 82 split tiles left UNSETTLED by the 2-of-3 rule and 270 one-reader gaps never re-read (tx/lookalike53L/*/focus.tsv), the ': :'-as-null alternative, and "rauldhoit" (f.171r L15, where French wants "pourroit") unresolved (N7-VIV53L); next: owner's sign sorter on the focus files, or a window re-read of the gap tiles (tx/viv53L_windows.py extended to gaps), ~$2
- ink 54 clean reading - blocker: not-attempted; window look-alike pass done (residual 0.134), true-error audit a non-test, no stretch near ~42 letters (N7-VIV54L); next: owner's sign sorter on tx/lookalike54/*_focus.tsv (275 questions) or a window-instrument audit (lookalike_pass.py audit + viv53L_windows.py audit), ~$1.5
- ink 54 key question "to z" (qae) - blocker: not-attempted; key cell added (key.tsv Zu -> u, col u row 3, N7-VIV54R) but the pre-registered per-position window judge was a NON-TEST (3/18 after-"to" positions SIGMA at H/M vs >= 7 required; ticks off, no per-sign stroke notes), so no position is relabelled and the reading has not moved; next: per-position crops cut at hand-marked x (not pos/len estimates) for the 169 z/x/R/3/2 positions, or the owner's sign sorter with Zu as a pile, then the same PREREG decision rule, ~$1.5
- ink 54 audit (depth re-check) - blocker: not-attempted; b2 + wrong-key PASS on the re-decode (PREREG-N7VIV54L); next: verifier session (account 3), ~$5
- Judge calibration for this hand - blocker: not-attempted; the fr16 judge FAILs the known-good f.103r control at this noise (N5-VIV54, N6-VIV53); next: score a lower-noise control (the clerk decipherment's own text, or f.103r after a lookalike pass) to see whether the judge can gate at all, ~$2
- fr.16104 ink 52 (5 Sept 1572, to the Queen, ~270 lines) - blocker: not-attempted; no decipherment beside it (N5-VIVTAB); next: look at c179/c181, then crops + 2 blind passes per page, decode with key.tsv, ~$30
- fr.16104 5 Sept 1572 cipher block (ff.157-159v) against its decipherment ff.162r-163r - blocker: not-attempted; known-plaintext check, not a reading; next: crops + two blind passes, aligned as tx/vivk_test.py, ~$15
- Unviewed stretches of the per-piece table - blocker: not-attempted; fr.16104 c1-c169, c192-c324 and fr.16105 c1-c94, c113-c191 not viewed (N5-VIVTAB); a decipherment of 63 filed in another volume (fr.16106 holds one such stray) not checked; next: 1200 px pass every second canvas, contact sheets, ~$3
- fr.16105 f.104r, first page of the decipherment - blocker: illegible; native crop shows word shapes only (N4-VIV3)
- Spanish-side copies (AGS Estado K) and Gachard vol. I - blocker: needs-physical-access; AGS is not digitised in a route this worker could open
## Escalation (4 Oct 2026, N7-VIV54R; from the N7-VIV54Q list)
- [x] siblings: ink 38 located; ink 40 vs 41 aligned (N5-VIVK); decipherment 51 found (N5-VIV5S); per-piece table (N5-VIVTAB); ink 54 read (N5-VIV54); ink 53 ff.170r-171v read (N6-VIV53, N6-VIV53B); ink 63 ff.190r-194r read in full (N6-VIV63, N6-VIV63B, N6-VIV63C, N7-VIV63G)
- [x] clear-pages: decipherments 41, 44, 51, 68, 71, 76 are on the leaves; inks 54 and 53 interlinear words used as gloss checks (N5-VIV54 PASS, N6-VIV53 FAIL at the floor); f.171v has none (N6-VIV53B); ink 63 has none (order gate b2 instead)
- [x] known-keys: Tomokiyo's 1572-74 key on disk and held-out PASS (N5-VIVK); applied to inks 54, 53 and 63
- [x] print: Gachard I-II, d'Ars, Catherine IV-V, Groen IV read; Kervyn I-VI grepped (N6-KERV); print_check on ink 54, 53 and 63 phrases (pc63b/, pc63c/)
- [retired] key-rebuild: tools/stream_align.py from a flat start did not converge on this material (Arm A, 2 of 30 codes); a published key exists
- [x] image-check: fr.16104 c170-191 and fr.16105 c95-112, c192-248 viewed; native regions of f.173r-v, ff.170r-171v, ff.190r-194r (N5-VIV54, N6-VIV53, N6-VIV63, N6-VIV63B, N6-VIV63C, N7-VIV63G)
- [ ] retry: ink 63 key questions on the key image (context table done, N7-VIV63G); ink 63 label questions (lookalike pass, overlap dedup); ink 53 residual unsettled tiles and gaps (window look-alike pass done, N7-VIV53L); ink 54 sorter/window audit (lookalike pass done, N7-VIV54L) and the col-u-row-3 relabel (key cell found, N7-VIV54Q; window judge NON-TEST, N7-VIV54R; next instrument: hand-placed per-position crops)
Verdict: keep going: 13 internal gaps; cheapest next: ink 54 col-u-row-3 relabel with hand-placed per-position crops (PREREG-N7VIV54R rule), ~$1.5, then the ink 53 and ink 54 audits (depth re-check), ~$5 each

## VIV-BREMOND (4 Oct 2026, 18:39-18:5x UTC, account-3 worker): d'Ars 1884 print check for 5 and 7 Sept 1572 and 10 Oct 1573
Brief: .claude/briefs/runs/2026-10-04-acct3-viv-bremond.md (lead: Ribera 2007 note 18, "Ibid., de Madrid, le 5 septembre 1572 ; BNF, Fr., 16104 ;
cité par G. de ...", ROOM 18:18). A print check, not a decode; novelty not classified.
- Book: Guillaume de Bremond d'Ars, *Jean de Vivonne, sa vie et ses ambassades* (Paris, 1884) = IA lepredemadamede00dargoog, already in sources.tsv
  and on disk (sources/ia-fulltext/print-check/lepredemadamede00dargoog_djvu.txt.gz, 20,802 OCR lines). No network request was made by this job.
- Date search (regex over the OCR, OCR-tolerant spellings of septembre/octobre and of 1572/1573): d'Ars cites Saint-Gouard letters of 7 Aug, 9, 12,
  "IS" [12/15/18?], 18 and 19 Sept 1572 and 18 Oct 1573 (plus one whose day the OCR lost, below). **No citation of a 5 Sept 1572, 7 Sept 1572 or
  10 Oct 1573 letter was found.** The only "7 septembre" in the 1572 chapter is narrative (p.44, "Dans la soirée du samedi 7 septembre, un courrier
  fit son entrée ... dans Madrid": the St Bartholomew news), cited to Saint-Gouard to Charles IX, 9 Sept 1572, fr.16104.
- Every Saint-Gouard quotation in the St Bartholomew pages (pp.43-47) is from letters written after the courier's arrival on the evening of 7 Sept.
  The one footnote whose day is lost (p.44) quotes, OCR exactly: "La nonvclle iIdr ivéaement du jour S.iînt-Biirthàleoiy est arrivée en r li(>ii un
  Fini CatliuliijUi; pur nn LiitUTicr rli-pe«cliP pur ilon Dic[>o, la nurJy an ioir nepùnme Hr ce luoys..." (worker's reading of the OCR: "La nouvelle
  de l'événement du jour Saint-Barthélemy est arrivée ... au Roi Catholique par un courrier dépêché par don Diego, le samedy au soir septiesme de ce
  moys"), cited "Saint-Gouard à Charles IX, [day lost] septembre 1572, fr.16105 (par erreur, cette lettre est avec celles de 1573)". It reports the
  7 Sept evening in the past and sits in fr.16105, so it is not ink 53 (5 Sept, fr.16104 ff.170-171) or ink 54 (7 Sept, fr.16104 f.173).
  The p.45 quotations ("Et ne pourront dire que j'y soye allé ...", "il se prit à rire ...") are cited to 12 Sept 1572 (fr.16105), p.46 to "IS" Sept.
- Script comparison (tx/bremond_kmer.py; letters only, accents stripped, u=v, i=j=y): shared k-mers between each decode and d'Ars, with Gachard II
  and Catherine IV as unrelated background of the same period and language:

| decode | letters | d'Ars 10-mers | Gachard II 10-mers | Catherine IV 10-mers | d'Ars 12-mers | d'Ars 15-mers |
|---|---|---|---|---|---|---|
| ink 53 (piece53_L_decode.txt) | 4,181 | 9 | 48 | 51 | 2 ("contradiction") | 0 |
| ink 54 (piece54_decode_L.txt) | 1,759 | 6 | 15 | 8 | 2 ("reunegrandea") | 0 |
| ink 63 (piece63_decode.txt) | 14,480 | 38 | 126 | 133 | 1 ("aireentendre") | 0 |

  Text sizes: d'Ars 608,134 letters, Gachard II 1,206,922, Catherine IV 1,475,373; per letter of book text d'Ars sits at or below the background
  (ink 53: 1.5e-5 vs 4.0e-5 / 3.5e-5). No 15-mer of any decode is in d'Ars. Limit: no matched positive control was run (a quoted cipher passage
  at our decodes' noise level), so this says "no overlap found at k>=12 beyond generic words", not that a short quote is impossible.
- print_check.py, offline, sources.tsv + d'Ars, on the union of the folder's phrase files (phrases_bremond.txt, 38 phrases; print-check-bremond.tsv,
  requests: none): d'Ars hits only "plus grande et plus" (1), "sur les frontieres" (1), "toutes choses" (2), each in unrelated passages (Poland
  election, mathematics lessons). 70 d'Ars rows "no hits".
- Where it was not found: d'Ars 1884 (OCR, whole volume). Not searched: Gallica texteBrut of another d'Ars copy (OCR could differ), Ribera 2007 in
  full, Flament 1996. Ribera's "G. de ..." is not confirmed to be d'Ars for the 5 Sept letter.

## Remaining gaps (VIV-BREMOND refresh, 4 Oct 2026; supersedes the N7-VIV54R list above, all its other lines kept)
Read so far: ink 40 checked against its decipherment 41 with Tomokiyo's key (N5-VIVK PASS); ink 54 read with key.tsv, gloss check PASS (N5-VIV54), window look-alike pass + re-decode, b2 + wrong-key PASS (N7-VIV54L); ink 53
ff.170r-171v read, b2 + wrong-key PASS (N6-VIV53B), window look-alike pass + ': :' join + re-decode, b2 + wrong-key PASS again (N7-VIV53L); ink 63 ff.190r-194r read in full (f.194r L5-10 added by N7-VIV63G): b2 PASS on every part (N6-VIV63, N6-VIV63B,
N6-VIV63C, N7-VIV63G), whole piece -1.548 vs p99 -1.836, wrong-key specificity PASS (real 0.288 vs p99 0.064), H 12,151 / M 2,329 / U 1,282 of 15,762 tokens.
Pieces with no decipherment located: fr.16105 63, fr.16104 52, 53, 54 (and 38, whose twin is deciphered).
- ink 63 N4 (audit 1 done 4 Oct 2026 by VIV63-A1, AUDIT.md AUDIT 3: N3, D1 fragments read, key published; recipient the King; no decipherment in fr.16105 c95-c248) - blocker: not-attempted; Flament, L'ambassade du marquis de Saint-Gouard en Espagne 1572-1574 (1996, OCLC 988579745) and Ribera (2007) unread (d'Ars 1884 checked by VIV-BREMOND: no citation of 10 Oct 1573, no decode overlap above background), fr.16105 c1-c94 and the fr.16106 pieces Gachard skips not viewed; next: a LOCAL-QUEUE row for Flament and Ribera on 10 Oct 1573 (interlibrary or the owner's browser), ~$1
- tools/iiif_lines.py on steep, uneven line slopes - blocker: not-attempted; --follow-slope (and --centres with it) snapped bands onto neighbouring lines on f.194r; next: an option to deskew the region by a fitted angle before a flat cut (what N6-VIV63C did by hand with PIL), with an offline test, ~$2
- ink 63 key questions (y, single o, c, V, e, 2, r) - blocker: not-attempted; context table done (N7-VIV63G, tx/viv63g_keyctx.tsv): the 4-gram fill is right on only 5/9 held-out codes at this N and biased to i/l, so only y->l (alignment + fill agree), V->n and e as an "m(m)" sign in "co_tandeur" stand as weak proposals; next: read cells h, l, m, n of Tomokiyo's key image (henryiii_Vivonne1.png) for a y-like l homophone, a V-like n and an e-like m/mm sign, then a PREREG'd key-change step with the wrong-key control, ~$1.5
- ink 63 label splits and overlap duplication - blocker: not-attempted; r/z, 2/z (f.193v 25x), c/e and 6/b (f.192r, 19x) left at pass A; readers wrote some s1/s2 overlaps twice (f.192r L06, L34; f.193r L07); f.193r err_2reader 0.297; next: tools/lookalike_pass.py on those pairs + a pre-registered overlap-dedup step in tx/viv63_clean.py, re-decode, ~$4
- ink 53 audit (depth re-check) - blocker: not-attempted; AUDIT 2 (VIV53-A1) set N3 / D1; the N7-VIV53L re-decode passes b2 + wrong-key again (PREREG-N7VIV53L) but no repair-free stretch reaches ~42 letters (longest 20); next: verifier session (account 3) on reading_piece53_L.tsv, ~$5
- ink 53 residual label questions - blocker: not-attempted; 82 split tiles left UNSETTLED by the 2-of-3 rule and 270 one-reader gaps never re-read (tx/lookalike53L/*/focus.tsv), the ': :'-as-null alternative, and "rauldhoit" (f.171r L15, where French wants "pourroit") unresolved (N7-VIV53L); next: owner's sign sorter on the focus files, or a window re-read of the gap tiles (tx/viv53L_windows.py extended to gaps), ~$2
- ink 54 clean reading - blocker: not-attempted; window look-alike pass done (residual 0.134), true-error audit a non-test, no stretch near ~42 letters (N7-VIV54L); next: owner's sign sorter on tx/lookalike54/*_focus.tsv (275 questions) or a window-instrument audit (lookalike_pass.py audit + viv53L_windows.py audit), ~$1.5
- ink 54 key question "to z" (qae) - blocker: not-attempted; key cell added (key.tsv Zu -> u, col u row 3, N7-VIV54R) but the pre-registered per-position window judge was a NON-TEST (3/18 after-"to" positions SIGMA at H/M vs >= 7 required; ticks off, no per-sign stroke notes), so no position is relabelled and the reading has not moved; next: per-position crops cut at hand-marked x (not pos/len estimates) for the 169 z/x/R/3/2 positions, or the owner's sign sorter with Zu as a pile, then the same PREREG decision rule, ~$1.5
- ink 54 audit (depth re-check) - blocker: not-attempted; b2 + wrong-key PASS on the re-decode (PREREG-N7VIV54L); next: verifier session (account 3), ~$5
- Judge calibration for this hand - blocker: not-attempted; the fr16 judge FAILs the known-good f.103r control at this noise (N5-VIV54, N6-VIV53); next: score a lower-noise control (the clerk decipherment's own text, or f.103r after a lookalike pass) to see whether the judge can gate at all, ~$2
- fr.16104 ink 52 (5 Sept 1572, to the Queen, ~270 lines) - blocker: not-attempted; no decipherment beside it (N5-VIVTAB); next: look at c179/c181, then crops + 2 blind passes per page, decode with key.tsv, ~$30
- fr.16104 5 Sept 1572 cipher block (ff.157-159v) against its decipherment ff.162r-163r - blocker: not-attempted; known-plaintext check, not a reading; next: crops + two blind passes, aligned as tx/vivk_test.py, ~$15
- Unviewed stretches of the per-piece table - blocker: not-attempted; fr.16104 c1-c169, c192-c324 and fr.16105 c1-c94, c113-c191 not viewed (N5-VIVTAB); a decipherment of 63 filed in another volume (fr.16106 holds one such stray) not checked; next: 1200 px pass every second canvas, contact sheets, ~$3
- fr.16105 f.104r, first page of the decipherment - blocker: illegible; native crop shows word shapes only (N4-VIV3)
- Spanish-side copies (AGS Estado K) and Gachard vol. I - blocker: needs-physical-access; AGS is not digitised in a route this worker could open
- Ribera 2007 note 18 "cité par G. de ..." for the 5 Sept 1572 letter (fr.16104) - blocker: waiting-on LOCAL-QUEUE L50 (Ribera full text; not cloud-reachable beyond a Google Books API snippet); d'Ars 1884 does not cite a 5 Sept 1572 letter in its OCR (VIV-BREMOND), so the 'G. de ...' is either another author or a d'Ars citation the OCR lost; next: read note 18 in full with the 5 Sept 1572 L50 row
## Escalation (4 Oct 2026, VIV-BREMOND; from the N7-VIV54R list)
- [x] siblings: ink 38 located; ink 40 vs 41 aligned (N5-VIVK); decipherment 51 found (N5-VIV5S); per-piece table (N5-VIVTAB); ink 54 read (N5-VIV54); ink 53 ff.170r-171v read (N6-VIV53, N6-VIV53B); ink 63 ff.190r-194r read in full (N6-VIV63, N6-VIV63B, N6-VIV63C, N7-VIV63G)
- [x] clear-pages: decipherments 41, 44, 51, 68, 71, 76 are on the leaves; inks 54 and 53 interlinear words used as gloss checks (N5-VIV54 PASS, N6-VIV53 FAIL at the floor); f.171v has none (N6-VIV53B); ink 63 has none (order gate b2 instead)
- [x] known-keys: Tomokiyo's 1572-74 key on disk and held-out PASS (N5-VIVK); applied to inks 54, 53 and 63
- [x] print: Gachard I-II, d'Ars, Catherine IV-V, Groen IV read; d'Ars re-checked by date and by k-mer/phrase overlap against inks 53, 54, 63 (VIV-BREMOND); Kervyn I-VI grepped (N6-KERV); print_check on ink 54, 53 and 63 phrases (pc63b/, pc63c/)
- [retired] key-rebuild: tools/stream_align.py from a flat start did not converge on this material (Arm A, 2 of 30 codes); a published key exists
- [x] image-check: fr.16104 c170-191 and fr.16105 c95-112, c192-248 viewed; native regions of f.173r-v, ff.170r-171v, ff.190r-194r (N5-VIV54, N6-VIV53, N6-VIV63, N6-VIV63B, N6-VIV63C, N7-VIV63G)
- [ ] retry: ink 63 key questions on the key image (context table done, N7-VIV63G); ink 63 label questions (lookalike pass, overlap dedup); ink 53 residual unsettled tiles and gaps (window look-alike pass done, N7-VIV53L); ink 54 sorter/window audit (lookalike pass done, N7-VIV54L) and the col-u-row-3 relabel (key cell found, N7-VIV54Q; window judge NON-TEST, N7-VIV54R; next instrument: hand-placed per-position crops)
Verdict: keep going: 13 internal gaps (+1 waiting-on); cheapest next: ink 54 col-u-row-3 relabel with hand-placed per-position crops (PREREG-N7VIV54R rule), ~$1.5, then the ink 53 and ink 54 audits (depth re-check), ~$5 each

## Desk runner 4 Oct 2026 (DESK-LAND, account-3 worker; LOCAL-QUEUE L50, L51, L52, JSTOR rows J1-J9)

Source: the owner's browser runner, outreach/local-runner/DESK-2026-10-04.md. Note: VIV-BREMOND earlier today searched d'Ars's
1884 **book** (*Jean de Vivonne, sa vie et ses ambassades*, IA lepredemadamede00dargoog); L51 is a different text by the same
author, the **article** G. de Bremond d'Ars, "La Saint-Barthélemy et l'Espagne d'après la correspondance de Jean de Vivonne de
Saint-Gouard", *Revue des questions historiques* 35 (1884), pp.386-412 (IA RevueDesQuestionsHistoriquesA18T35, from n391).
VIV-BREMOND's "no 5 Sept 1572 citation" holds for the book only.

**L51 (RQH article).** Volumes listed p.387 n.1 (fr.16104 = Jan-Dec 1572, 16105 = 1573, 16106-16108). The 5 Sept 1572 letter is
cited: p.395 n.4 "Saint-Gouard à Charles IX, 5 septembre 1572. Ms. Bibl. nat., F. fr. 16104", with Philip II's words as reported:
« Vous remercierez Sa Majesté de ma part, mais vous la prierez aussi de choisir des gens sûrs à cause des inconvénients qui résultent
du mauvais choix des gardeurs de frontières ». Other citations: 12 Sept 1572 (bound in fr.16105 by error) pp.396-401, 403; 19 Sept
1572 (fr.16104) pp.402, 403, 406; 18 Oct 1572 pp.402, 404; 16 July 1572 to Anjou p.393 n.4 ("impénétrable le taciturne monarque").
No 1573 citation; no mention of cipher or decipherment.

**Is the quoted passage in the clear text or the cipher block of the 5 Sept letter (ink 50, ff.157r-159v)?** In the clear text.
Gachard II (cached sources/ia-fulltext/print-check/labibliothquen02gachuoft_djvu.txt.gz, entry L, pp.592-594, OCR lines
~17483-17570) prints the audience of 27 August from the letter's plain part, and its last paragraph is Philip's answer: "... et quant
à l'ordre que Vostre Majesté veult mectre sur ses frontières de crainte des événements futurs, qu'il l'approuve et trouve très-bon,
mais qu'il est bien besoing aussy d'y employer gens fidelles et non suspectz à ce qui a apporté l'occasion à tant de misères ...".
d'Ars's sentence is a modernised paraphrase of that plain passage (thanks, "gens sûrs" = "gens fidelles et non suspectz", the
frontier guards), not a quotation of the cipher. So d'Ars had **no** reading of the cipher block, and the passage is **not** a crib.
Also, the brief's premise is out of date: the cipher block ff.157r-159v is not unread -- its clerk decipherment, piece 51, ff.162r-163r
"dechiffré de la precedente", was found by N5-VIV5S (4 Oct 2026); what remains there is a known-plaintext check (gap list below,
unchanged). Ribera 2007 note 18 "cité par G. de ..." for the 5 Sept 1572 letter: consistent with this RQH article (d'Ars cites
exactly that letter and shelfmark); the Ribera gap is closed as answered.

**L50 (Ribera 2007, Google Books 7p3mENOa3U0C).** Snippet view only: "monarque taciturne et impénétrable" on p.335 (running head
only shown); "Saint-Gouard" 20 pages (pp.326, 519, 521 shown). Note 139 and any citation of the 5/7 Sept 1572 or 10 Oct 1573
letters not visible.

**L52 (Flament 1996).** SUDOC 201366568: maîtrise, Lille 3, 1996, 158 p., dir. Labourdette; held Lille, Bib. G. Lefebvre (HARTIS),
cote D 1996 3, "Non disponible pour le PEB" -- not lendable; no digitised copy. WorldCat stopped at a bot check (not attempted).

**JSTOR J1-J9 (JSTOR-QUEUE.tsv answered).** One relevant item, twice (J1, J5): "Recueils périodiques et sociétés savantes",
*Revue Historique* 25/1 (1884), pp.192-224, https://www.jstor.org/stable/40937194 -- a digest of the same RQH article (d'Ars "pense
et montre ... que Saint-Gouard ne connaissait nullement le prétendu plan arrêté par la cour d'un massacre général"); not opened, no
cipher content. All other rows: no relevant hit (J2 1 unrelated; J3, J4, J6-J9 0). Search results, not a novelty verdict (rule 10).


## Remaining gaps (DESK-LAND refresh, 4 Oct 2026; supersedes the VIV-BREMOND list above, all its other lines kept)
Read so far: ink 40 checked against its decipherment 41 with Tomokiyo's key (N5-VIVK PASS); ink 54 read with key.tsv, gloss check PASS (N5-VIV54), window look-alike pass + re-decode, b2 + wrong-key PASS (N7-VIV54L); ink 53
ff.170r-171v read, b2 + wrong-key PASS (N6-VIV53B), window look-alike pass + ': :' join + re-decode, b2 + wrong-key PASS again (N7-VIV53L); ink 63 ff.190r-194r read in full (f.194r L5-10 added by N7-VIV63G): b2 PASS on every part (N6-VIV63, N6-VIV63B,
N6-VIV63C, N7-VIV63G), whole piece -1.548 vs p99 -1.836, wrong-key specificity PASS (real 0.288 vs p99 0.064), H 12,151 / M 2,329 / U 1,282 of 15,762 tokens.
Pieces with no decipherment located: fr.16105 63, fr.16104 52, 53, 54 (and 38, whose twin is deciphered).
- ink 63 N4 (audit 1 done 4 Oct 2026 by VIV63-A1, AUDIT.md AUDIT 3: N3, D1 fragments read, key published; recipient the King; no decipherment in fr.16105 c95-c248) - blocker: not-attempted; d'Ars 1884 book (VIV-BREMOND) and d'Ars's RQH 35 (1884) article pp.386-412 (L51, DESK-LAND) both checked: neither cites 10 Oct 1573; Ribera 2007 seen as Google Books snippets only (L50: note 139 not visible); fr.16105 c1-c94 and the fr.16106 pieces Gachard skips not viewed; next: Ribera 2007 in full through the owner's interlibrary loan (ILL-SWEEP batch), reading note 139 and every 1573 Saint-Gouard citation, ~owner minutes + $0.5 to land
- Flament 1996 (L'ambassade du marquis de Saint-Gouard en Espagne, maîtrise Lille 3, 158 p.) - blocker: needs-physical-access; only copy located Lille, Bib. G. Lefebvre, cote D 1996 3, "Non disponible pour le PEB" (SUDOC 201366568, L52, 4 Oct 2026); no digitised copy
- tools/iiif_lines.py on steep, uneven line slopes - blocker: not-attempted; --follow-slope (and --centres with it) snapped bands onto neighbouring lines on f.194r; next: an option to deskew the region by a fitted angle before a flat cut (what N6-VIV63C did by hand with PIL), with an offline test, ~$2
- ink 63 key questions (y, single o, c, V, e, 2, r) - blocker: not-attempted; context table done (N7-VIV63G, tx/viv63g_keyctx.tsv): the 4-gram fill is right on only 5/9 held-out codes at this N and biased to i/l, so only y->l (alignment + fill agree), V->n and e as an "m(m)" sign in "co_tandeur" stand as weak proposals; next: read cells h, l, m, n of Tomokiyo's key image (henryiii_Vivonne1.png) for a y-like l homophone, a V-like n and an e-like m/mm sign, then a PREREG'd key-change step with the wrong-key control, ~$1.5
- ink 63 label splits and overlap duplication - blocker: not-attempted; r/z, 2/z (f.193v 25x), c/e and 6/b (f.192r, 19x) left at pass A; readers wrote some s1/s2 overlaps twice (f.192r L06, L34; f.193r L07); f.193r err_2reader 0.297; next: tools/lookalike_pass.py on those pairs + a pre-registered overlap-dedup step in tx/viv63_clean.py, re-decode, ~$4
- ink 53 audit (depth re-check) - blocker: not-attempted; AUDIT 2 (VIV53-A1) set N3 / D1; the N7-VIV53L re-decode passes b2 + wrong-key again (PREREG-N7VIV53L) but no repair-free stretch reaches ~42 letters (longest 20); next: verifier session (account 3) on reading_piece53_L.tsv, ~$5
- ink 53 residual label questions - blocker: not-attempted; 82 split tiles left UNSETTLED by the 2-of-3 rule and 270 one-reader gaps never re-read (tx/lookalike53L/*/focus.tsv), the ': :'-as-null alternative, and "rauldhoit" (f.171r L15, where French wants "pourroit") unresolved (N7-VIV53L); next: owner's sign sorter on the focus files, or a window re-read of the gap tiles (tx/viv53L_windows.py extended to gaps), ~$2
- ink 54 clean reading - blocker: not-attempted; window look-alike pass done (residual 0.134), true-error audit a non-test, no stretch near ~42 letters (N7-VIV54L); next: owner's sign sorter on tx/lookalike54/*_focus.tsv (275 questions) or a window-instrument audit (lookalike_pass.py audit + viv53L_windows.py audit), ~$1.5
- ink 54 key question "to z" (qae) - blocker: not-attempted; key cell added (key.tsv Zu -> u, col u row 3, N7-VIV54R) but the pre-registered per-position window judge was a NON-TEST (3/18 after-"to" positions SIGMA at H/M vs >= 7 required; ticks off, no per-sign stroke notes), so no position is relabelled and the reading has not moved; next: per-position crops cut at hand-marked x (not pos/len estimates) for the 169 z/x/R/3/2 positions, or the owner's sign sorter with Zu as a pile, then the same PREREG decision rule, ~$1.5
- ink 54 audit (depth re-check) - blocker: not-attempted; b2 + wrong-key PASS on the re-decode (PREREG-N7VIV54L); next: verifier session (account 3), ~$5
- Judge calibration for this hand - blocker: not-attempted; the fr16 judge FAILs the known-good f.103r control at this noise (N5-VIV54, N6-VIV53); next: score a lower-noise control (the clerk decipherment's own text, or f.103r after a lookalike pass) to see whether the judge can gate at all, ~$2
- fr.16104 ink 52 (5 Sept 1572, to the Queen, ~270 lines) - blocker: not-attempted; no decipherment beside it (N5-VIVTAB); next: look at c179/c181, then crops + 2 blind passes per page, decode with key.tsv, ~$30
- fr.16104 5 Sept 1572 cipher block (ff.157-159v) against its decipherment ff.162r-163r - blocker: not-attempted; known-plaintext check, not a reading; next: crops + two blind passes, aligned as tx/vivk_test.py, ~$15
- Unviewed stretches of the per-piece table - blocker: not-attempted; fr.16104 c1-c169, c192-c324 and fr.16105 c1-c94, c113-c191 not viewed (N5-VIVTAB); a decipherment of 63 filed in another volume (fr.16106 holds one such stray) not checked; next: 1200 px pass every second canvas, contact sheets, ~$3
- fr.16105 f.104r, first page of the decipherment - blocker: illegible; native crop shows word shapes only (N4-VIV3)
- Spanish-side copies (AGS Estado K) and Gachard vol. I - blocker: needs-physical-access; AGS is not digitised in a route this worker could open
## Escalation (4 Oct 2026, DESK-LAND; from the VIV-BREMOND list)
- [x] siblings: ink 38 located; ink 40 vs 41 aligned (N5-VIVK); decipherment 51 found (N5-VIV5S); per-piece table (N5-VIVTAB); ink 54 read (N5-VIV54); ink 53 ff.170r-171v read (N6-VIV53, N6-VIV53B); ink 63 ff.190r-194r read in full (N6-VIV63, N6-VIV63B, N6-VIV63C, N7-VIV63G)
- [x] clear-pages: decipherments 41, 44, 51, 68, 71, 76 are on the leaves; inks 54 and 53 interlinear words used as gloss checks (N5-VIV54 PASS, N6-VIV53 FAIL at the floor); f.171v has none (N6-VIV53B); ink 63 has none (order gate b2 instead)
- [x] known-keys: Tomokiyo's 1572-74 key on disk and held-out PASS (N5-VIVK); applied to inks 54, 53 and 63
- [x] print: Gachard I-II, d'Ars (book 1884 and RQH 35 article, L51), Catherine IV-V, Groen IV read; Ribera 2007 snippets (L50); d'Ars re-checked by date and by k-mer/phrase overlap against inks 53, 54, 63 (VIV-BREMOND); Kervyn I-VI grepped (N6-KERV); print_check on ink 54, 53 and 63 phrases (pc63b/, pc63c/)
- [retired] key-rebuild: tools/stream_align.py from a flat start did not converge on this material (Arm A, 2 of 30 codes); a published key exists
- [x] image-check: fr.16104 c170-191 and fr.16105 c95-112, c192-248 viewed; native regions of f.173r-v, ff.170r-171v, ff.190r-194r (N5-VIV54, N6-VIV53, N6-VIV63, N6-VIV63B, N6-VIV63C, N7-VIV63G)
- [ ] retry: ink 63 key questions on the key image (context table done, N7-VIV63G); ink 63 label questions (lookalike pass, overlap dedup); ink 53 residual unsettled tiles and gaps (window look-alike pass done, N7-VIV53L); ink 54 sorter/window audit (lookalike pass done, N7-VIV54L) and the col-u-row-3 relabel (key cell found, N7-VIV54Q; window judge NON-TEST, N7-VIV54R; next instrument: hand-placed per-position crops)
Verdict: keep going: 13 internal gaps (Ribera note 18 answered by L51; Flament not lendable); cheapest next: ink 54 col-u-row-3 relabel with hand-placed per-position crops (PREREG-N7VIV54R rule), ~$1.5, then the ink 53 and ink 54 audits (depth re-check), ~$5 each


## DEF1-VIV54 (5 Oct 2026, 21:05-21:1x UTC by date -u, account-1 worker for LANE DEFAULT-account-1-20261005-2039): ink 54 col-u-row-3 relabel, hand-placed crops
Brief: .claude/briefs/runs/2026-10-05-account1-default-2039-jobs.md "DEF1-VIV54". Disk only (0 requests). Rule: PREREG-N7VIV54R.md unchanged (decision
rule, classes, built-in check); the instrument swapped is the one N7-VIV54R named: per-position crops placed at hand-marked x instead of pos/len ticks.

**Placement.** tx/viv54H_place.py cut native windows (+-8 signs around the old estimate, pixel ruler) of every after-"to" position (the PREREG's
known-positive subset, 18 positions); this worker read the ruler and marked each sign's strip x by eye (three lines, f.173r L11/L14/L17, start
far right of the estimate and were placed from a wider view). Plus 5 foils marked the same way: ordinary z/x positions N7-VIV54Q named as
the non-Sigma comparison (f.173r L14.5, L07.26; f.173v L04.21, L04.40, L02.44). x marks: tx/lookalike54/viv54H_xmarks.tsv.
tx/viv54H_crops.py cut strip x +-110 px native, 2x, red ticks at the mark, opaque ids C01-C23 shuffled (seed 20261054H; map in
viv54H_key.tsv), plus the same ref.png (col u row 3 vs col a row 3). Sanity look at the first montage: ticks sit on the sign in every crop.
One value-blind Sonnet call (no decoded text, no key value, no hypothesis); answers tx/lookalike54/viv54H_judge.tsv, tally tx/viv54H_tally.py
-> tx/viv54H_tally.json. This time the reader gave a per-sign stroke note in every row (the gap N7-VIV54R logged).

**Result: built-in check FAILS again -> NON-TEST, not applied.** After-"to" (18): SIGMA 0, ZED 13 (M 9, L 4), OTHER 4, UNSURE 1 (f.173r L17.7:
"blank between ticks" -- this worker's one misplaced mark). Required >= 7 SIGMA at H/M. Foils (5): ZED 1, OTHER 4 (3-like loops), SIGMA 0.
Because the after-"to" check fails on the full known-positive subset, placing the other 151 positions could not change the verdict, so they
were not placed (no unit spent on them). No position relabelled; key.tsv row Zu stays as N7-VIV54R wrote it (unused by any transcription);
reading_piece54_L.tsv unchanged (`tx/viv54L_decode.py --check`: up to date); b2/specificity not re-run (no change); AUDIT.md and SO-VIV54 untouched
(rule 10 propagation applies only to a changed reading).
**What the difference from N7-VIV54R means.** N7-VIV54R's failure could be blamed on misplaced ticks; here the ticks are on the sign and the reader
names a diagonal stroke top-right to bottom-left for 13 of the 18 after-"to" signs. So a blind reader, given the same two key cells, does not
see the col-u-row-3 Sigma shape in that slot; N7-VIV54Q's by-eye identification (a worker who knew the "que" context) is not reproduced.
This does not refute "to"+sign = "qu(e)" (a scribal z-like u homophone, or a ligature, could still be meant); it says the shape test cannot
separate it from the flat z at this image quality with this reader. Second instrument on the same hypothesis (windows N7-VIV54R, hand-placed
crops here), both failing the same check: one more tuning of a machine shape judge is not the next step (rule 3 third-attempt clause would retire
it); the next is a different instrument -- the owner's sign sorter with Zu as a pile, or a clerk-aligned occurrence (a deciphered sibling,
ink 40/41, ink 50/51) showing which sign the clerk wrote for u after "q".
Report what was found and where it was not found; no novelty classified. Requests: none. Subagent calls: 1 Sonnet.

## Remaining gaps (DEF1-VIV54 refresh, 5 Oct 2026; supersedes the DESK-LAND list above, all its other lines kept)
Read so far: ink 40 checked against its decipherment 41 with Tomokiyo's key (N5-VIVK PASS); ink 54 read with key.tsv, gloss check PASS (N5-VIV54), window look-alike pass + re-decode, b2 + wrong-key PASS (N7-VIV54L); ink 53
ff.170r-171v read, b2 + wrong-key PASS (N6-VIV53B), window look-alike pass + ': :' join + re-decode, b2 + wrong-key PASS again (N7-VIV53L); ink 63 ff.190r-194r read in full (f.194r L5-10 added by N7-VIV63G): b2 PASS on every part (N6-VIV63, N6-VIV63B,
N6-VIV63C, N7-VIV63G), whole piece -1.548 vs p99 -1.836, wrong-key specificity PASS (real 0.288 vs p99 0.064), H 12,151 / M 2,329 / U 1,282 of 15,762 tokens.
Pieces with no decipherment located: fr.16105 63, fr.16104 52, 53, 54 (and 38, whose twin is deciphered).
- ink 63 N4 (audit 1 done 4 Oct 2026 by VIV63-A1, AUDIT.md AUDIT 3: N3, D1 fragments read, key published; recipient the King; no decipherment in fr.16105 c95-c248) - blocker: not-attempted; d'Ars 1884 book (VIV-BREMOND) and d'Ars's RQH 35 (1884) article pp.386-412 (L51, DESK-LAND) both checked: neither cites 10 Oct 1573; Ribera 2007 seen as Google Books snippets only (L50: note 139 not visible); fr.16105 c1-c94 and the fr.16106 pieces Gachard skips not viewed; next: Ribera 2007 in full through the owner's interlibrary loan (ILL-SWEEP batch), reading note 139 and every 1573 Saint-Gouard citation, ~owner minutes + $0.5 to land
- Flament 1996 (L'ambassade du marquis de Saint-Gouard en Espagne, maîtrise Lille 3, 158 p.) - blocker: needs-physical-access; only copy located Lille, Bib. G. Lefebvre, cote D 1996 3, "Non disponible pour le PEB" (SUDOC 201366568, L52, 4 Oct 2026); no digitised copy
- tools/iiif_lines.py on steep, uneven line slopes - blocker: not-attempted; --follow-slope (and --centres with it) snapped bands onto neighbouring lines on f.194r; next: an option to deskew the region by a fitted angle before a flat cut (what N6-VIV63C did by hand with PIL), with an offline test, ~$2
- ink 63 key questions (y, single o, c, V, e, 2, r) - blocker: not-attempted; context table done (N7-VIV63G, tx/viv63g_keyctx.tsv): the 4-gram fill is right on only 5/9 held-out codes at this N and biased to i/l, so only y->l (alignment + fill agree), V->n and e as an "m(m)" sign in "co_tandeur" stand as weak proposals; next: read cells h, l, m, n of Tomokiyo's key image (henryiii_Vivonne1.png) for a y-like l homophone, a V-like n and an e-like m/mm sign, then a PREREG'd key-change step with the wrong-key control, ~$1.5
- ink 63 label splits and overlap duplication - blocker: not-attempted; r/z, 2/z (f.193v 25x), c/e and 6/b (f.192r, 19x) left at pass A; readers wrote some s1/s2 overlaps twice (f.192r L06, L34; f.193r L07); f.193r err_2reader 0.297; next: tools/lookalike_pass.py on those pairs + a pre-registered overlap-dedup step in tx/viv63_clean.py, re-decode, ~$4
- ink 53 audit (depth re-check) - blocker: not-attempted; AUDIT 2 (VIV53-A1) set N3 / D1; the N7-VIV53L re-decode passes b2 + wrong-key again (PREREG-N7VIV53L) but no repair-free stretch reaches ~42 letters (longest 20); next: verifier session (account 3) on reading_piece53_L.tsv, ~$5
- ink 53 residual label questions - blocker: not-attempted; 82 split tiles left UNSETTLED by the 2-of-3 rule and 270 one-reader gaps never re-read (tx/lookalike53L/*/focus.tsv), the ': :'-as-null alternative, and "rauldhoit" (f.171r L15, where French wants "pourroit") unresolved (N7-VIV53L); next: owner's sign sorter on the focus files, or a window re-read of the gap tiles (tx/viv53L_windows.py extended to gaps), ~$2
- ink 54 clean reading - blocker: not-attempted; window look-alike pass done (residual 0.134), true-error audit a non-test, no stretch near ~42 letters (N7-VIV54L); next: owner's sign sorter on tx/lookalike54/*_focus.tsv (275 questions) or a window-instrument audit (lookalike_pass.py audit + viv53L_windows.py audit), ~$1.5
- ink 54 key question "to z" (qae) - blocker: not-attempted; key cell added (key.tsv Zu -> u, col u row 3, N7-VIV54R); two machine shape judges under PREREG-N7VIV54R failed its built-in check: windows (3/18 SIGMA, ticks off; N7-VIV54R) and hand-placed crops (0/18 SIGMA, 13/18 ZED with ticks on the sign; DEF1-VIV54), so no position is relabelled and the reading has not moved; next: a different instrument -- the owner's sign sorter with Zu as a pile (tx/lookalike54/viv54H_xmarks.tsv gives the 18 positions), or a clerk-aligned u-after-q in ink 40/41 or 50/51, ~$1
- ink 54 audit (depth re-check) - blocker: not-attempted; b2 + wrong-key PASS on the re-decode (PREREG-N7VIV54L); next: verifier session (account 3), ~$5
- Judge calibration for this hand - blocker: not-attempted; the fr16 judge FAILs the known-good f.103r control at this noise (N5-VIV54, N6-VIV53); next: score a lower-noise control (the clerk decipherment's own text, or f.103r after a lookalike pass) to see whether the judge can gate at all, ~$2
- fr.16104 ink 52 (5 Sept 1572, to the Queen, ~270 lines) - blocker: not-attempted; no decipherment beside it (N5-VIVTAB); next: look at c179/c181, then crops + 2 blind passes per page, decode with key.tsv, ~$30
- fr.16104 5 Sept 1572 cipher block (ff.157-159v) against its decipherment ff.162r-163r - blocker: not-attempted; known-plaintext check, not a reading; next: crops + two blind passes, aligned as tx/vivk_test.py, ~$15
- Unviewed stretches of the per-piece table - blocker: not-attempted; fr.16104 c1-c169, c192-c324 and fr.16105 c1-c94, c113-c191 not viewed (N5-VIVTAB); a decipherment of 63 filed in another volume (fr.16106 holds one such stray) not checked; next: 1200 px pass every second canvas, contact sheets, ~$3
- fr.16105 f.104r, first page of the decipherment - blocker: illegible; native crop shows word shapes only (N4-VIV3)
- Spanish-side copies (AGS Estado K) and Gachard vol. I - blocker: needs-physical-access; AGS is not digitised in a route this worker could open
## Escalation (5 Oct 2026, DEF1-VIV54; from the DESK-LAND list)
- [x] siblings: ink 38 located; ink 40 vs 41 aligned (N5-VIVK); decipherment 51 found (N5-VIV5S); per-piece table (N5-VIVTAB); ink 54 read (N5-VIV54); ink 53 ff.170r-171v read (N6-VIV53, N6-VIV53B); ink 63 ff.190r-194r read in full (N6-VIV63, N6-VIV63B, N6-VIV63C, N7-VIV63G)
- [x] clear-pages: decipherments 41, 44, 51, 68, 71, 76 are on the leaves; inks 54 and 53 interlinear words used as gloss checks (N5-VIV54 PASS, N6-VIV53 FAIL at the floor); f.171v has none (N6-VIV53B); ink 63 has none (order gate b2 instead)
- [x] known-keys: Tomokiyo's 1572-74 key on disk and held-out PASS (N5-VIVK); applied to inks 54, 53 and 63
- [x] print: Gachard I-II, d'Ars (book 1884 and RQH 35 article, L51), Catherine IV-V, Groen IV read; Ribera 2007 snippets (L50); d'Ars re-checked by date and by k-mer/phrase overlap against inks 53, 54, 63 (VIV-BREMOND); Kervyn I-VI grepped (N6-KERV); print_check on ink 54, 53 and 63 phrases (pc63b/, pc63c/)
- [retired] key-rebuild: tools/stream_align.py from a flat start did not converge on this material (Arm A, 2 of 30 codes); a published key exists
- [x] image-check: fr.16104 c170-191 and fr.16105 c95-112, c192-248 viewed; native regions of f.173r-v, ff.170r-171v, ff.190r-194r (N5-VIV54, N6-VIV53, N6-VIV63, N6-VIV63B, N6-VIV63C, N7-VIV63G)
- [ ] retry: ink 63 key questions on the key image (context table done, N7-VIV63G); ink 63 label questions (lookalike pass, overlap dedup); ink 53 residual unsettled tiles and gaps (window look-alike pass done, N7-VIV53L); ink 54 sorter/window audit (lookalike pass done, N7-VIV54L) and the col-u-row-3 relabel (key cell found, N7-VIV54Q; window judge NON-TEST, N7-VIV54R; hand-placed judge NON-TEST 0/18, DEF1-VIV54; next instrument: sign sorter / clerk alignment, hand-placed per-position crops)
Verdict: keep going: 13 internal gaps; cheapest next: the ink 53 and ink 54 audits (depth re-check), ~$5 each; the col-u-row-3 question needs a different instrument (sign sorter or clerk alignment), not a third machine shape judge

## R7A-VIV53 (6 Oct 2026, 01:48-02:0x UTC by date -u, account-1 worker for LANE LANE-RUN7-account-1): ink 53 one-reader gap tiles, window re-read
Brief: .claude/briefs/runs/2026-10-06-account1-run7-jobs.md "R7A-VIV53". Step still undone (no dated section after N7-VIV53L ran it).
PREREG-R7VIV53G.md pushed (9e7021164) before any window was cut or read. key.tsv and every 53L file untouched (viv53L_decode.py --check passes).
**Instrument:** tx/viv53G_windows.py = tx/viv53L_windows.py's window()/montage() unchanged, on the 270 gap tiles (42/103/38/87) plus 12 agreed-sign
decoys per page (seeded), shuffled together, candidates alphabetical = the tile's candidates + NONE; answer key in tx/lookalike53G/<page>/items.tsv
(never shown). Crops regenerated from the four images/p53 commands (gallica.bnf.fr 4 requests, >= 3 s apart); montages not committed.
**Units:** 4 Sonnet calls (one per page) + this worker's fold-in. Re-read grades H/M/L: f170r 7/28/19, f170v 26/70/19, f171r 19/24/7, f171v 7/25/67.
**Control gate (ii), decoys:** 40/48 firm-correct = **0.833** (gate 0.80), firm NONE 0/48 (gate <= 0.10) -> **PASS**, fold-in applied.
**Gap verdicts (iii)** (echo = answer equals the present label): f170r present 20 / removed 0 / kept 22; f170v 60 / 9 / 34; f171r 21 / 5 / 12;
f171v 20 / 2 / 65; total **121 present, 16 removed, 133 kept** (flagged M as before). On f.171v the reader could not find most places (67 L);
its window x-estimates are least reliable there.
**Re-decode** (tx/viv53G_decode.py, `--check` passes; reading_piece53_G.tsv, piece53_G_decode.txt; reading_piece53_L.tsv kept as the N7 reading):
| | tokens | H | M | U |
|---|---|---|---|---|
| N7-VIV53L | 4,394 | 3,641 (82.9%) | 540 | 213 |
| R7A-VIV53 | 4,380 | 3,732 (85.2%) | 436 | 212 |
H is key-source grading on a settled sign (published key), no C, no S. 14 lines change letters (e.g. f.171r L15 "doubteranentrasten" -> "doubteraentrasten").
**Gates (PREREG-N7VIV53L (iv) rule, seed "20261053G"; tx/viv53G_result.json):** C1 f.103r -1.715 vs p99 -1.893 PASS, C2 ink 54 -1.658 vs -1.829 PASS
(headroom ok); **b2 whole piece -1.604 vs p99 -1.838 PASS**; **wrong keys: real margin 0.234 vs p99 0.050 (max 0.064), 32/200 pass b2 alone -> PASS**
(N7-VIV53L: -1.607, margin 0.224 vs 0.063).
**Longest repair-free stretch (V_strict = fr16 forms count >= 100, length >= 3, + viv54L_stretch.STRICT_SHORT, 772 forms; pre-registered here):**
before (53L) top-1 **20**, top-3 mean 18.3 vs shuffled-letter null median 13 / p99 21; after (53G) top-1 **20**, top-3 18.3 vs null 13 / 19.
Top stretch unchanged both times: f.170r L16-L17 "intention a entrer en ce" (word division, 1 line end, 1 look-alike-settled, 1 joined ': :').
The second, f.171r L24 (20), is short-word salad ("ueu o ont a san o entre aul"). **No stretch approaches the ~42-letter authentication
distance; the gap pass raises the H share but does not join the fragments.** No depth suggestion for a verifier from this job.
Not done (cap): the 82 UNSETTLED split tiles (PREREG (iii) allowed them only if cap remained).
Requests: gallica.bnf.fr 4. Subagent calls: 4 Sonnet. Cost: see the lane ledger.


## D1-F16104I (6 Oct 2026, 13:06-13:3x UTC by date -u, account-1 worker for LANE DEFAULT-account-1-20261006-1240): ink 53 audit (depth re-check)
Verifier hat, no decoding, nothing in key/reading/tx changed. Written up as AUDIT.md AUDIT 4. `tx/viv53G_decode.py --check` and `tx/viv53L_decode.py --check`
exit 0; `tx/viv53G_decode.py --gates` re-run (4 min 7 s), tx/viv53G_result.json byte-identical (b2 whole -1.604 vs p99 -1.838 PASS; wrong keys 0.234 vs
p99 0.050 PASS). Grades before/after: N7-VIV53L H 3,641 / M 540 / U 213 of 4,394 (82.9%) -> R7A G H 3,732 / M 436 / U 212 of 4,380 (85.2%).
Longest all-H run 37 per line, 41 across line ends, both salad; registered stretch top-1 20 before and after. **Depth held at D1.**
Observation: the G decode (4,168 letters) has no f, m, p, v, x, y; key.tsv gives no label the meanings f, m, p, so those letters fall into U or wrong
values (U label e before "rontiere" 3/3 and before "aict" 2x). Named as the D2 path in Remaining gaps. status.json ink-53 depth fields updated;
SO-VIV53 prompt given a dated note. Requests 0, subagent calls 0 (no vision call: no stretch long enough to check on the image).

## D1-F16104K (6 Oct 2026, 13:26-13:3x UTC by date -u, account-1 worker for LANE DEFAULT-account-1-20261006-1240): ink 53 f/m/p key cells against the U labels
PREREG-D1VIV53K.md pushed (34fc1ea36) before the scored run. Candidate cells read by shape from the key image (henryiii_Vivonne1.png) alone:
e->f (col f r1), o->p (col p r1), II->m (col m r1), Z->m and 2->m (col m r2), r->n (col n r2), c->o (col o r2), V->x (col x r2); H->f (col f r4) below the n>=3 floor.
**Instrument:** tx/viv53K_cells.py; fr16 4-gram score (same model as the b2 gates) of the whole ink-53 G stream with one label -> each of 22 letters;
control = wrong-cell assignment (the other 21 letters at the same positions). PASS = candidate ranks 1st of 22 and beats the label-dropped decode (base -1.6037).
| label (n) | cand | cand score | rank /22 | best wrong (score) | PASS |
|---|---|---|---|---|---|
| e (16) | f | -1.6077 | 14 | r (-1.5993) | no |
| o (33) | p | -1.6066 | 9 | i (-1.5990) | no |
| II (4) | m | -1.6037 | 12 | a (-1.6023) | no |
| Z (4) | m | -1.6047 | 9 | r (-1.6029) | no |
| 2 (28) | m | -1.6024 | 10 | n (-1.5936) | no |
| r (32) | n | -1.5987 | 3 | s (-1.5971) | no |
| c (31) | o | -1.6124 | 19 | n (-1.5950) | no |
| V (16) | x | -1.6155 | 21 | c (-1.6014) | no |
**Result: no label PASSes; key.tsv, reading_piece53_G.tsv and every decode unchanged (no overlay written, gates not re-run, since (iv) needs a PASS).**
Logged as a negative for this instrument only (one meaning per whole label, scored over the whole piece).
Descriptive, not gated (looked at after the scored run): label e stands in "co[e]te" 6x (fits "comte", an m) and before "rontie" 3x and "aict" 2x
(fits f); label o stands in "rinci[o]ale" (fits p) but in many contexts that fit nothing. So the labels e and o look like two or more signs merged
by the passes, which a one-meaning-per-label test cannot separate. Requests 0, subagent calls 0.

## D07-VIV53 (7 Oct 2026, 00:51-01:0x UTC by date -u, account-1 worker for LANE DEFAULT-account-1-20261007-0042): ink 53 e/o per-position crops vs key cells f, m, p
Brief: .claude/briefs/runs/2026-10-07-account1-default-0042-jobs.md "D07-VIV53". Step undone before this job (D1-F16104K named it next).
PREREG-D07VIV53P.md pushed (430c73b9f) before placement and any judge call; placement marks pushed (28b3b98db) before the judge calls.
**Crop step (pasted):** the four images/p53 commands of NOTES lines 555-561/858 re-run (`tools/iiif_lines.py --ark btv1b9009609w --canvas 184
--region 4700,2000,3150,2950 --out .../images/p53 --prefix c184_f170r --follow-slope 400 --distance 90 --max-width 1600 --overlap 150 --debug`, and
canvas 185 f170v / f171r, canvas 186 f171v as recorded); 256 crops, boxes identical to the committed manifest except 10 f171v boxes by 1 px
(manifest and debug image restored from git, crops not committed). gallica.bnf.fr 4 requests.
**Placement:** tx/viv53P_place.py sheets (ink runs numbered) for the 49 e/o tokens and 12 known-answer controls (3 each of d, m, p, g, H-graded,
seed 20261053P); x marked by this worker, then checked on +-300 px strips with an offset ruler and corrected (first-pass marks were off by up to
115 px; tx/lookalike53P/viv53P_xmarks.tsv holds the corrected marks), then a 61-tile +-70 px sheet confirmed the mark sits on the sign.
**Judge:** tx/viv53P_crops.py, strip x +-110 px, 2x, red ticks, opaque ids K01-K61; reference sheet of 10 key cells under A-J (f1, g1, m1, m2, m5,
p1, o1, e1, n1, r1; map viv53P_refkey.tsv). Two independent blind Sonnet calls, different montage orders; answers viv53P_judge_A/B.tsv;
tally tx/viv53P_tally.py -> tx/lookalike53P/viv53P_tally.json.
**Result: control gate FAILS in both passes -> NON-TEST, nothing applied.** Pass A: 4/12 controls on the right cell at H/M, 4 firm wrong (gate
>= 8 and <= 2); pass B: 5/12, 0 firm wrong. The judge names the g controls correctly (r1 at H/M in 5 of 6 answers) and one d control (K56) in both passes, but misses m and p
(e.g. control p read as e1 or r1, control m as r1/m2/NONE). key.tsv, reading_piece53_G.tsv and every decode unchanged; gates not re-run (no
overlay); AUDIT.md and SO-VIV53 untouched (no reading change).
Descriptive only (not gated, not applied): both passes put label e on col f row 1 at H/M for 6 of 16 positions (K15, K19, K24, K29, K45, K58;
5 more f1 in pass A only, 4 of those g1 at L in pass B); label o has no stable cell (9 NONE/NONE, p1 agreed at any confidence on 1 of 33, f1/f1 on 2).
This is the second instrument on the e/o question (D1-F16104K's whole-label n-gram rank, then this hand-placed shape judge), both without a usable
result; a third tuning of a machine shape judge is not the next step (rule 3 third-attempt clause). Next instrument: the owner's sign sorter with the
49 positions as piles beside the f1/m1/m2/m5/p1 cells, or a clerk-aligned f/m/p in ink 40/41 or 50/51.
Report what was found and where it was not found; no novelty classified. Requests: gallica.bnf.fr 4. Subagent calls: 2 Sonnet.

## Remaining gaps (D07-VIV53 refresh, 7 Oct 2026; supersedes the D1-F16104K list, all its other lines kept)
Read so far: ink 40 checked against its decipherment 41 with Tomokiyo's key (N5-VIVK PASS); ink 54 read with key.tsv, gloss check PASS (N5-VIV54), window look-alike pass + re-decode, b2 + wrong-key PASS (N7-VIV54L); ink 53
ff.170r-171v read, b2 + wrong-key PASS (N6-VIV53B), window look-alike pass + ': :' join + re-decode, b2 + wrong-key PASS again (N7-VIV53L); ink 63 ff.190r-194r read in full (f.194r L5-10 added by N7-VIV63G): b2 PASS on every part (N6-VIV63, N6-VIV63B,
N6-VIV63C, N7-VIV63G), whole piece -1.548 vs p99 -1.836, wrong-key specificity PASS (real 0.288 vs p99 0.064), H 12,151 / M 2,329 / U 1,282 of 15,762 tokens.
Pieces with no decipherment located: fr.16105 63, fr.16104 52, 53, 54 (and 38, whose twin is deciphered).
- ink 63 N4 (audit 1 done 4 Oct 2026 by VIV63-A1, AUDIT.md AUDIT 3: N3, D1 fragments read, key published; recipient the King; no decipherment in fr.16105 c95-c248) - blocker: not-attempted; d'Ars 1884 book (VIV-BREMOND) and d'Ars's RQH 35 (1884) article pp.386-412 (L51, DESK-LAND) both checked: neither cites 10 Oct 1573; Ribera 2007 seen as Google Books snippets only (L50: note 139 not visible); fr.16105 c1-c94 and the fr.16106 pieces Gachard skips not viewed; next: Ribera 2007 in full through the owner's interlibrary loan (ILL-SWEEP batch), reading note 139 and every 1573 Saint-Gouard citation, ~owner minutes + $0.5 to land
- Flament 1996 (L'ambassade du marquis de Saint-Gouard en Espagne, maîtrise Lille 3, 158 p.) - blocker: needs-physical-access; only copy located Lille, Bib. G. Lefebvre, cote D 1996 3, "Non disponible pour le PEB" (SUDOC 201366568, L52, 4 Oct 2026); no digitised copy
- tools/iiif_lines.py on steep, uneven line slopes - blocker: not-attempted; --follow-slope (and --centres with it) snapped bands onto neighbouring lines on f.194r; next: an option to deskew the region by a fitted angle before a flat cut (what N6-VIV63C did by hand with PIL), with an offline test, ~$2
- ink 63 key questions (y, single o, c, V, e, 2, r) - blocker: not-attempted; context table done (N7-VIV63G, tx/viv63g_keyctx.tsv): the 4-gram fill is right on only 5/9 held-out codes at this N and biased to i/l, so only y->l (alignment + fill agree), V->n and e as an "m(m)" sign in "co_tandeur" stand as weak proposals; next: read cells h, l, m, n of Tomokiyo's key image (henryiii_Vivonne1.png) for a y-like l homophone, a V-like n and an e-like m/mm sign, then a PREREG'd key-change step with the wrong-key control, ~$1.5
- ink 63 label splits and overlap duplication - blocker: not-attempted; r/z, 2/z (f.193v 25x), c/e and 6/b (f.192r, 19x) left at pass A; readers wrote some s1/s2 overlaps twice (f.192r L06, L34; f.193r L07); f.193r err_2reader 0.297; next: tools/lookalike_pass.py on those pairs + a pre-registered overlap-dedup step in tx/viv63_clean.py, re-decode, ~$4
- ink 53 D2 (depth re-check done 6 Oct 2026, D1-F16104I, AUDIT.md AUDIT 4: hold D1, H 85.2%) - blocker: not-attempted; two instruments on the e/o labels, both without a usable result: whole-label key-cell n-gram rank (D1-F16104K, no label 1st of 22) and hand-placed per-position crops judged blind against 10 key cells (D07-VIV53, PREREG-D07VIV53P: known-answer control 4/12 and 5/12 against a gate of 8/12 -> NON-TEST, nothing applied; descriptively both passes put 6 of 16 e positions on col f row 1 at H/M, not usable as a gate); next: a different instrument -- the owner's sign sorter with the 49 e/o positions as piles beside the f1/m1/m2/m5/p1 key cells (tx/lookalike53P/viv53P_xmarks.tsv gives hand-placed x), or a clerk-aligned occurrence of f/m/p in ink 40/41 or 50/51 to fix the clerk's own f, m, p signs, ~$1.5
- ink 53 residual label questions - blocker: not-attempted; the 270 one-reader gaps were window re-read under PREREG-R7VIV53G (decoy control PASS): 121 settled present, 16 removed, 133 still flagged; the 82 UNSETTLED split tiles, the ': :'-as-null alternative and "rauldhoit" (f.171r L15) remain; f.171v gap windows mostly unfindable (65 of 87 kept, the reader called 56 NONE but mostly at L) -- the window x-estimate drifts on that page; next: hand-placed per-tile crops (DEF1-VIV54's method) for the 82 splits + the 133 kept gaps, or the owner's sign sorter, ~$2.5
- ink 54 clean reading - blocker: not-attempted; window look-alike pass done (residual 0.134), true-error audit a non-test, no stretch near ~42 letters (N7-VIV54L); next: owner's sign sorter on tx/lookalike54/*_focus.tsv (275 questions) or a window-instrument audit (lookalike_pass.py audit + viv53L_windows.py audit), ~$1.5
- ink 54 key question "to z" (qae) - blocker: not-attempted; key cell added (key.tsv Zu -> u, col u row 3, N7-VIV54R); two machine shape judges under PREREG-N7VIV54R failed its built-in check: windows (3/18 SIGMA, ticks off; N7-VIV54R) and hand-placed crops (0/18 SIGMA, 13/18 ZED with ticks on the sign; DEF1-VIV54), so no position is relabelled and the reading has not moved; next: a different instrument -- the owner's sign sorter with Zu as a pile (tx/lookalike54/viv54H_xmarks.tsv gives the 18 positions), or a clerk-aligned u-after-q in ink 40/41 or 50/51, ~$1
- ink 54 D2 (depth re-check done 7 Oct 2026, DA1-VIV, AUDIT.md "AUDIT (ink 54 depth re-check, DA1-VIV)": hold D1, H 76.2%; rule-7 --check and b2 + wrong-key gates re-run, verdicts reproduce) - blocker: not-attempted; the decode has no f, m, p, v, x, y and s at 2.2% (no key label carries f, m, p), and "que" reads "qae" (13x); next: the same different instrument as ink 53's e/o question (owner's sign sorter or a clerk-aligned f/m/p and u-after-q in ink 40/41 or 50/51), then a PREREG'd key-change step with the wrong-key control, ~$1.5
- Judge calibration for this hand - blocker: not-attempted; the fr16 judge FAILs the known-good f.103r control at this noise (N5-VIV54, N6-VIV53); next: score a lower-noise control (the clerk decipherment's own text, or f.103r after a lookalike pass) to see whether the judge can gate at all, ~$2
- fr.16104 ink 52 (5 Sept 1572, to the Queen, ~270 lines) - blocker: not-attempted; no decipherment beside it (N5-VIVTAB); next: look at c179/c181, then crops + 2 blind passes per page, decode with key.tsv, ~$30
- fr.16104 5 Sept 1572 cipher block (ff.157-159v) against its decipherment ff.162r-163r - blocker: not-attempted; known-plaintext check, not a reading; next: crops + two blind passes, aligned as tx/vivk_test.py, ~$15
- Unviewed stretches of the per-piece table - blocker: not-attempted; fr.16104 c1-c169, c192-c324 and fr.16105 c1-c94, c113-c191 not viewed (N5-VIVTAB); a decipherment of 63 filed in another volume (fr.16106 holds one such stray) not checked; next: 1200 px pass every second canvas, contact sheets, ~$3
- fr.16105 f.104r, first page of the decipherment - blocker: illegible; native crop shows word shapes only (N4-VIV3)
- Spanish-side copies (AGS Estado K) and Gachard vol. I - blocker: needs-physical-access; AGS is not digitised in a route this worker could open
## Escalation (7 Oct 2026, D07-VIV53; from the D1-F16104K list)
- [x] siblings: ink 38 located; ink 40 vs 41 aligned (N5-VIVK); decipherment 51 found (N5-VIV5S); per-piece table (N5-VIVTAB); ink 54 read (N5-VIV54); ink 53 ff.170r-171v read (N6-VIV53, N6-VIV53B); ink 63 ff.190r-194r read in full (N6-VIV63, N6-VIV63B, N6-VIV63C, N7-VIV63G)
- [x] clear-pages: decipherments 41, 44, 51, 68, 71, 76 are on the leaves; inks 54 and 53 interlinear words used as gloss checks (N5-VIV54 PASS, N6-VIV53 FAIL at the floor); f.171v has none (N6-VIV53B); ink 63 has none (order gate b2 instead)
- [x] known-keys: Tomokiyo's 1572-74 key on disk and held-out PASS (N5-VIVK); applied to inks 54, 53 and 63
- [x] print: Gachard I-II, d'Ars (book 1884 and RQH 35 article, L51), Catherine IV-V, Groen IV read; Ribera 2007 snippets (L50); d'Ars re-checked by date and by k-mer/phrase overlap against inks 53, 54, 63 (VIV-BREMOND); Kervyn I-VI grepped (N6-KERV); print_check on ink 54, 53 and 63 phrases (pc63b/, pc63c/)
- [retired] key-rebuild: tools/stream_align.py from a flat start did not converge on this material (Arm A, 2 of 30 codes); a published key exists
- [x] image-check: fr.16104 c170-191 and fr.16105 c95-112, c192-248 viewed; native regions of f.173r-v, ff.170r-171v, ff.190r-194r (N5-VIV54, N6-VIV53, N6-VIV63, N6-VIV63B, N6-VIV63C, N7-VIV63G)
- [ ] retry: ink 53 f/m/p key cells for the U labels (AUDIT 4; whole-label test negative, D1-F16104K; hand-placed per-position shape judge NON-TEST, control 4-5/12 vs 8/12, D07-VIV53; next instrument: sign sorter or clerk alignment); ink 63 key questions on the key image (context table done, N7-VIV63G); ink 63 label questions (lookalike pass, overlap dedup); ink 53 residual unsettled tiles and kept gaps (window look-alike pass N7-VIV53L; gap re-read R7A-VIV53, 137/270 settled); ink 54 sorter/window audit (lookalike pass done, N7-VIV54L) and the col-u-row-3 relabel (key cell found, N7-VIV54Q; window judge NON-TEST, N7-VIV54R; hand-placed judge NON-TEST 0/18, DEF1-VIV54; next instrument: sign sorter / clerk alignment, hand-placed per-position crops)
Verdict: keep going: 13 internal gaps; ink 54 audit (depth re-check) done 7 Oct 2026 (DA1-VIV, hold D1); cheapest next: the ink 53 e/o question (D2 path) needs a different instrument (sign sorter or clerk alignment of f, m, p), ~$1.5, the machine shape judge being a NON-TEST at this image quality (D07-VIV53); the col-u-row-3 question needs a different instrument (sign sorter or clerk alignment)

## DA1-VIV (7 Oct 2026, 14:49-15:0x UTC by date -u, account-1 verifier for LANE DEFAULT-account-1-20261007-1440): ink 54 audit (depth re-check)
Verifier hat, no decoding; nothing in key/reading/tx changed except one added file. Written up as AUDIT.md "AUDIT (ink 54 depth re-check, DA1-VIV)". `tx/viv54L_decode.py --check` exit 0;
`tx/viv54L_test.py` re-run: target and control scores identical, nulls shifted slightly (key.tsv row Zu added by N7-VIV54R after the registered run changes the
shuffle draws), verdicts unchanged (b2 PASS, wrong-key PASS); re-run saved as tx/viv54L_result_DA1VIV.json, registered file kept. Grades H 1,488 / M 271 / U 195 of
1,954 (76.2%), as VER1-VIV. Seeded 4-line crop spot check: no H sign contradicts the image. Missing letters: no f, m, p, v, x, y. **Depth held at D1.**
status.json ink-54 `grade` field corrected from the stale N5 counts. Requests 0, subagent calls 0.

## VIV-ANCHOR (8 Oct 2026, 02:41-03:0x UTC by date -u, account-1 worker for acct3-orchestrator): clerk word anchors on ink 40 for the unkeyed labels
Brief: .claude/briefs/runs/2026-10-08-acct3-scout-jobs.md "## VIV-ANCHOR". Intake gate exit 0. PREREG-VIVANCHOR.md pushed (f735c938) before any score. Disk only.
**Instrument (new for this target):** tx/vivanchor.py. Ink 40 (ff.102r-103r, 5,451 tokens after N5-VIVK's reader, brace nulls dropped) against the 300 distinct
>= 7-letter words of the clerk's ink-41 decipherment (dec_f105v-f108v_merged, {del:} removed, uncertain words dropped). A window anchors when every non-target
letter of the word decodes exactly under key_tomokiyo.tsv; the label at each target slot is collected, unique positions only. 110 anchoring windows (shuffled-
order null: median 3, max 7 over 20 shuffles), 140 decided positions.
**Known-answer control (gate >= 5 of 7, n >= 3 at share >= 2/3): 5/7 PASS.** d 3 at 1.00, t 11 at 1.00, o 8 at 1.00, r 9 at 0.78, c 4 at 0.75 recover;
n 28 at 0.54 (V takes 7 of the n slots, which is the assignment below) and s 22 at 0.27 (d 7, x 6) do not.
**Assignments:** label V -> n, 7 of 8 positions (0.875): f102v:L03:40 ("anglois"), f102v:L17:22, f103r:L07:29, f102r:L20:43, f102v:L28:43, f102v:L20:11,
f102r:L12:21; one s. Added to key.tsv, grade C (clerk decipherment). This agrees with N7-VIV63G's weak V->n proposal and is distinct from D1-F16104K's
V->x candidate, which failed. Not assigned: 2 (u 2, m 1), o (p 2), c (p 1), e and r (no anchored position; e has 10 tokens in ink 40, as expected).
Cells: m 4 positions (label 3 x2, 2, z), p 3 (o 2, c 1), qu 4 (z 2, 2 2): none reach 3 at 2/3. Cell f: label p at 4 of 6 (0.67), i.e. two "affaires" spelled
p p (f102v L07:46-47, L34:33-34). **CONFLICT:** p is keyed n, so key unchanged (logged in Remaining gaps). f, m and p stay under 3 decided positions; the next
instrument is the ink 50/51 known plaintext (fr.16104 ff.157-159v against ff.162r-163r), about $15. Not started.
**Re-decode (rule 7):** tx/viv63_decode.py, tx/viv53G_decode.py, tx/viv54L_decode.py regenerated, each --check exit 0. The superseded readings that also read key.tsv (tx/viv53L_decode.py, tx/viv53_decode.py, tx/viv54_decode.py) were regenerated too so every --check passes. Letters moved: 179 (63), 16 (53), 4 (54).
Grades before -> after: 63 H 12,151 / M 2,329 / U 1,282 -> 12,290 / 2,369 / 1,103; 53 H 3,732 / M 436 / U 212 -> 3,744 / 440 / 196; 54 H 1,488 / M 271 / U 195 ->
1,491 / 272 / 191 (counted from the reading TSVs).
**Gates, new seeds (tx/vivanchor_gates.py; tx/vivanchor_gates_{63,53,54}.json; registered result files untouched):**
| ink | C1 f.103r b2 | C2 b2 | target s vs b2 p99 | b2 | 200 wrong keys: real margin vs p99 (b2 passes) | verdict |
|---|---|---|---|---|---|---|
| 63 | PASS | ink 54 PASS | -1.5329 vs -1.8258 | PASS | 0.2929 vs 0.0445 (45/200) | PASS |
| 53 | PASS | ink 54 PASS | -1.6037 vs -1.8340 | PASS | 0.2303 vs 0.0527 (39/200) | PASS |
| 54 | PASS | ink 53 PASS | -1.6342 vs -1.8217 | PASS | 0.1875 vs 0.0455 (18/200) | PASS |
Ink 53 registered V_strict stretch (seed 20261008VA-53-stretch): top-1 20 ("intention a entrer en ce"), top-3 mean 18.33, null median 13, p99 24: unchanged, below its null p99.
**Longest H run per ink (every M/U token breaks it, across line ends), against the ~42-letter AD the verifiers used:** 63: 40, f191v L27-28
"leaqesoailquonttousouautoutrailantcereoe" (before: same 40); 53: 41, f171r L27-28 (before: same 41, salad); 54: 26, f173v L07 (before: 26). No ink reaches about 42
letters of readable text; the 40 and 41 runs are letter salad with words in them.
**Pardon clause, f.191v L26-27:** unchanged by V -> n (no V in it). Decode "estroublesou_arh_ardoulceurdun_arhdoncgenerah_etbienaa_le" for "les troubles ou
par doulceur d'un pardon general et bien ample": p missing three times (U labels in "par", "pardon", "ample"), y read h three times (key y = h, grade M:
"_arh", "arhdon", "generah"), "ample" reads "aa_le" (m as a). It still needs those repairs.
**Rule 10:** the readings of inks 63, 53 and 54 changed after AUDIT.md (V letters filled). AUDIT.md and SO-VIV53/54/63 not edited by this worker; flagged in ROOM for a
verifier. No depth or N-class set. Report what was found and where it was not found; no novelty classified. Requests 0; subagent calls 0.

## Remaining gaps (VIV-ANCHOR refresh, 8 Oct 2026; supersedes the D07-VIV53 list, all its other lines kept)
Read so far: ink 40 checked against its decipherment 41 with Tomokiyo's key (N5-VIVK PASS); ink 54 read with key.tsv, gloss check PASS (N5-VIV54), window look-alike pass + re-decode, b2 + wrong-key PASS (N7-VIV54L); ink 53
ff.170r-171v read, b2 + wrong-key PASS (N6-VIV53B), window look-alike pass + ': :' join + re-decode, b2 + wrong-key PASS again (N7-VIV53L); ink 63 ff.190r-194r read in full (f.194r L5-10 added by N7-VIV63G): b2 PASS on every part (N6-VIV63, N6-VIV63B,
N6-VIV63C, N7-VIV63G), whole piece -1.548 vs p99 -1.836, wrong-key specificity PASS (real 0.288 vs p99 0.064), H 12,151 / M 2,329 / U 1,282 of 15,762 tokens. VIV-ANCHOR (8 Oct 2026): key.tsv V -> n (grade C, clerk word anchors) re-decodes all three inks: H 12,290 / M 2,369 / U 1,103 of 15,762 (63), 3,744 / 440 / 196 (53), 1,491 / 272 / 191 (54); b2 and 200-wrong-key gates PASS on each under new seeds.
Pieces with no decipherment located: fr.16105 63, fr.16104 52, 53, 54 (and 38, whose twin is deciphered).
- ink 63 N4 (audit 1 done 4 Oct 2026 by VIV63-A1, AUDIT.md AUDIT 3: N3, D1 fragments read, key published; recipient the King; no decipherment in fr.16105 c95-c248) - blocker: not-attempted; d'Ars 1884 book (VIV-BREMOND) and d'Ars's RQH 35 (1884) article pp.386-412 (L51, DESK-LAND) both checked: neither cites 10 Oct 1573; Ribera 2007 seen as Google Books snippets only (L50: note 139 not visible); fr.16105 c1-c94 and the fr.16106 pieces Gachard skips not viewed; next: Ribera 2007 in full through the owner's interlibrary loan (ILL-SWEEP batch), reading note 139 and every 1573 Saint-Gouard citation, ~owner minutes + $0.5 to land
- Flament 1996 (L'ambassade du marquis de Saint-Gouard en Espagne, maîtrise Lille 3, 158 p.) - blocker: needs-physical-access; only copy located Lille, Bib. G. Lefebvre, cote D 1996 3, "Non disponible pour le PEB" (SUDOC 201366568, L52, 4 Oct 2026); no digitised copy
- tools/iiif_lines.py on steep, uneven line slopes - blocker: not-attempted; --follow-slope (and --centres with it) snapped bands onto neighbouring lines on f.194r; next: an option to deskew the region by a fitted angle before a flat cut (what N6-VIV63C did by hand with PIL), with an offline test, ~$2
- ink 63 key questions (y, single o, c, 2, r; e) - blocker: not-attempted; V settled as an n homophone by VIV-ANCHOR (8 Oct 2026, 7 of 8 clerk-anchored ink-40 positions, control 5/7 PASS; key.tsv row V, grade C); e -> m added by VIV-KEY (14 Oct 2026, PREREG-VIVKEY, tx/vivkey_tally.tsv: ink 40 none + ink 67 m 4 of 5, all four in "comm-"; key.tsv row e, grade C; b2 + 200-wrong-key gates PASS on inks 63, 53, 54 but are non-discriminating for one row -- e = i passes too, post-hoc; decode_key --try on ink 63 rejects e=m, prefers i, weak at this noise): ink 63 U 1,103 -> 942; still open: whether e is m or a double-m sign, and the crossword disagreement -- next: a verifier shape look at the 161 ink-63 e tiles against the ink-67 "comme" tiles (f201r L05/L10/L12/L13), ~$2; plaintext p and f still have no key row: pooled clerk anchors (VIV-KEY) give c p 9 of 19 (0.47), single o p 7 of 16 (0.44), both under 2/3; label 2 a CONFLICT (ink 40 u 2 of 3, ink 67 e 3 of 5); y r 11 / l 9 of 34 (not h); context table (N7-VIV63G, tx/viv63g_keyctx.tsv, its --check stale since VIV-ANCHOR); next: ink 67 f.201v-203r against ink 68 ff.205v-207 for more c/o/2 anchors (tx/viv67_labels.py on the longer stream, then tx/vivkey.py), ~$12
- ink 63 label splits and overlap duplication - blocker: not-attempted; r/z, 2/z (f.193v 25x), c/e and 6/b (f.192r, 19x) left at pass A; readers wrote some s1/s2 overlaps twice (f.192r L06, L34; f.193r L07); f.193r err_2reader 0.297; next: tools/lookalike_pass.py on those pairs + a pre-registered overlap-dedup step in tx/viv63_clean.py, re-decode, ~$4
- ink 53 D2 (depth re-check done 6 Oct 2026, D1-F16104I, AUDIT.md AUDIT 4: hold D1, H 85.2%) - blocker: not-attempted; three instruments on f, m, p now: whole-label key-cell n-gram rank (D1-F16104K, negative), hand-placed shape judge (D07-VIV53, NON-TEST), and clerk word anchors on ink 40 (VIV-ANCHOR, PREREG-VIVANCHOR: control PASS, but f, m, p each under 3 decided positions: m 4 split 3:2/2:1/z:1, p 3 split o:2/c:1; f 4 of 6 on label p, which the key reads n -- a CONFLICT, key unchanged: "affaires" is written p p twice, so readers' label p merges an f-sign); V -> n moved 16 ink-53 letters, longest H run 41 (unchanged, salad), V_strict top-1 20 (unchanged, null p99 24); next: the ink 50/51 known plaintext (fr.16104 ff.157-159v vs ff.162r-163r) for more f, m, p anchors, then split label p by shape at the anchored f positions, ~$15
- ink 53 residual label questions - blocker: not-attempted; the 270 one-reader gaps were window re-read under PREREG-R7VIV53G (decoy control PASS): 121 settled present, 16 removed, 133 still flagged; the 82 UNSETTLED split tiles, the ': :'-as-null alternative and "rauldhoit" (f.171r L15) remain; f.171v gap windows mostly unfindable (65 of 87 kept, the reader called 56 NONE but mostly at L) -- the window x-estimate drifts on that page; next: hand-placed per-tile crops (DEF1-VIV54's method) for the 82 splits + the 133 kept gaps, or the owner's sign sorter, ~$2.5
- ink 54 clean reading - blocker: not-attempted; window look-alike pass done (residual 0.134), true-error audit a non-test, no stretch near ~42 letters (N7-VIV54L); next: owner's sign sorter on tx/lookalike54/*_focus.tsv (275 questions) or a window-instrument audit (lookalike_pass.py audit + viv53L_windows.py audit), ~$1.5
- ink 54 key question "to z" (qae) - blocker: not-attempted; key cell added (key.tsv Zu -> u, N7-VIV54R); two machine shape judges NON-TEST (N7-VIV54R, DEF1-VIV54); clerk anchors on ink 40 (VIV-ANCHOR) give the u-after-q slot to z 2 and 2 2 of 4 positions: undecided (no share >= 2/3); next: the owner's sign sorter with Zu as a pile (tx/lookalike54/viv54H_xmarks.tsv), or the ink 50/51 known plaintext for more qu anchors, ~$1
- ink 54 D2 (depth re-check done 7 Oct 2026, DA1-VIV, hold D1, H 76.2%) - blocker: not-attempted; ink 40 clerk anchors (VIV-ANCHOR) fixed V -> n only (4 ink-54 letters moved, H 1,491 of 1,954, longest H run 26, unchanged); f, m, p and u-after-q stay under 3 positions; next: the ink 50/51 known plaintext (fr.16104 ff.157-159v against ff.162r-163r), then a PREREG'd key-change step with the wrong-key control, ~$15
- label p carries f in ink 40 (VIV-ANCHOR CONFLICT) - blocker: not-attempted; 4 of 6 clerk-anchored f slots hold label p (key n), at f102v L07:46-47 and L34:33-34 ("affaires" both times); the key has no f row; crops cut and a sorter page built (D4-VIV, 8 Oct 2026: tx/sorter_fp/, 4 focus tiles + 2 p-labelled refs + the readers' f sign, preflight PASS); next: the owner sorts tx/sorter_fp/sorter_viv_fp.html, then tools/sign_sorter_apply.py and a PREREG'd key-change step with the wrong-key control, ~$1
- Judge calibration for this hand - blocker: not-attempted; the fr16 judge FAILs the known-good f.103r control at this noise (N5-VIV54, N6-VIV53); next: score a lower-noise control (the clerk decipherment's own text, or f.103r after a lookalike pass) to see whether the judge can gate at all, ~$2
- fr.16104 ink 52 (5 Sept 1572, to the Queen, ~270 lines) - blocker: not-attempted; no decipherment beside it (N5-VIVTAB); next: look at c179/c181, then crops + 2 blind passes per page, decode with key.tsv, ~$30
- fr.16104 5 Sept 1572 cipher block (ff.157-159v) against its decipherment ff.162r-163r - blocker: not-attempted; known-plaintext check, not a reading; next: crops + two blind passes, aligned as tx/vivk_test.py, ~$15
- Unviewed stretches of the per-piece table - blocker: not-attempted; fr.16104 c1-c169, c192-c324 and fr.16105 c1-c94, c113-c191 not viewed (N5-VIVTAB); a decipherment of 63 filed in another volume (fr.16106 holds one such stray) not checked; next: 1200 px pass every second canvas, contact sheets, ~$3
- fr.16105 f.104r, first page of the decipherment - blocker: illegible; native crop shows word shapes only (N4-VIV3)
- Spanish-side copies (AGS Estado K) and Gachard vol. I - blocker: needs-physical-access; AGS is not digitised in a route this worker could open
## Escalation (8 Oct 2026, VIV-ANCHOR; from the D07-VIV53 list)
- [x] siblings: ink 38 located; ink 40 vs 41 aligned (N5-VIVK); decipherment 51 found (N5-VIV5S); per-piece table (N5-VIVTAB); ink 54 read (N5-VIV54); ink 53 ff.170r-171v read (N6-VIV53, N6-VIV53B); ink 63 ff.190r-194r read in full (N6-VIV63, N6-VIV63B, N6-VIV63C, N7-VIV63G)
- [x] clear-pages: decipherments 41, 44, 51, 68, 71, 76 are on the leaves; inks 54 and 53 interlinear words used as gloss checks (N5-VIV54 PASS, N6-VIV53 FAIL at the floor); f.171v has none (N6-VIV53B); ink 63 has none (order gate b2 instead)
- [x] known-keys: Tomokiyo's 1572-74 key on disk and held-out PASS (N5-VIVK); applied to inks 54, 53 and 63
- [x] print: Gachard I-II, d'Ars (book 1884 and RQH 35 article, L51), Catherine IV-V, Groen IV read; Ribera 2007 snippets (L50); d'Ars re-checked by date and by k-mer/phrase overlap against inks 53, 54, 63 (VIV-BREMOND); Kervyn I-VI grepped (N6-KERV); print_check on ink 54, 53 and 63 phrases (pc63b/, pc63c/)
- [retired] key-rebuild: tools/stream_align.py from a flat start did not converge on this material (Arm A, 2 of 30 codes); a published key exists
- [x] image-check: fr.16104 c170-191 and fr.16105 c95-112, c192-248 viewed; native regions of f.173r-v, ff.170r-171v, ff.190r-194r (N5-VIV54, N6-VIV53, N6-VIV63, N6-VIV63B, N6-VIV63C, N7-VIV63G)
- [ ] retry: ink 53 f/m/p key cells for the U labels (AUDIT 4; whole-label test negative, D1-F16104K; hand-placed per-position shape judge NON-TEST, control 4-5/12 vs 8/12, D07-VIV53; clerk word anchors on ink 40, VIV-ANCHOR 8 Oct 2026: control 5/7 PASS, V -> n assigned, f/m/p/qu under 3 positions, f on label p a conflict; next instrument: ink 50/51 known plaintext or sign sorter); ink 63 key questions on the key image (context table done, N7-VIV63G); ink 63 label questions (lookalike pass, overlap dedup); ink 53 residual unsettled tiles and kept gaps (window look-alike pass N7-VIV53L; gap re-read R7A-VIV53, 137/270 settled); ink 54 sorter/window audit (lookalike pass done, N7-VIV54L) and the col-u-row-3 relabel (key cell found, N7-VIV54Q; window judge NON-TEST, N7-VIV54R; hand-placed judge NON-TEST 0/18, DEF1-VIV54; next instrument: sign sorter / clerk alignment, hand-placed per-position crops)
Verdict: keep going: 14 internal gaps; V -> n added from the clerk anchors (VIV-ANCHOR, 8 Oct 2026), gates PASS on all three inks, no stretch or clause changed; the four f-on-label-p crops are on a sorter page (D4-VIV, 8 Oct 2026, tx/sorter_fp/sorter_viv_fp.html), cheapest next: the owner sorts them, ~$0 agent cost; the f, m, p question needs more clerk anchors: ink 50/51 known plaintext (fr.16104 ff.157-159v vs ff.162r-163r), ~$15


## VIV52 (8 Oct 2026, 12:43-13:0x UTC by date -u, account-1 lane orchestrator for acct3-orchestrator): ink 52 premise; image step blocked by Gallica
Brief: .claude/briefs/runs/2026-10-08-acct3-sibs-ledger3.md "## VIV52". Step 1 (premise) done; steps 2-4 not run.

**Step 1, premise, print (files on disk, sources/ia-fulltext/print-check/, no network):**
- Gachard II (labibliothquen02gachuoft): the Saint-Gouard 1572 headers run "L. Au roi, Madrid, 5 septembre 1572 (En partie chiffrée, sans le
  déchiffrement)" (OCR line 17479), then "Au roi, Madrid, 12 septembre 1572" (numeral lost), then "LV, LVI. Au roi, 19 septembre" (17743). No entry for a
  5 Sept 1572 letter to the Queen (ink 52), nor for 53 or 54; "reine" in that stretch only inside LV-LVI's summary. Same finding as N5-VIVTAB.
- d'Ars 1884 (lepredemadamede00dargoog): no "à la Reine" passage cites a 5 Sept 1572 letter; VIV-BREMOND's date search (no 5 or 7 Sept 1572 citation) stands.
- La Ferrière, Catherine IV and X; Gachard I: no "5 septembre 1572" / "v sept 1572" and no fr.16104 citation of this letter (regex over the OCR).
- Result: no printed plaintext or abstract of ink 52 located in these four works. Not searched this job: Ribera 2007 in full, Flament 1996 (both blocked, see gaps).

**Step 1, premise, leaves:** already known from N5-VIVTAB and N6-VIV53: c184 = f.169v (52's address leaf, endorsed 5 Sept 1572) | f.170r (ink 53);
c184-c190 carry 53, 54 and 55 (19 Sept, own decipherment 56), no "dechiffré" leaf for 52 between f.169 and f.175. **Not yet seen: c179, c181, c183**
(ff.164v-165r, 166v-167r, 168v-169r): the job meant to view c178-c183 at 1200 px before cropping.

**Blocker: gallica.bnf.fr blocked this container.** IIIF image requests `https://gallica.bnf.fr/iiif/ark:/12148/btv1b9009609w/f{178..183}/full/1200,/0/default.jpg`
with a browser User-Agent, 2.5 s apart, 12:50 UTC: all six HTTP 403, an HTML page "Sorry, you have been blocked / You are unable to access gallica.bnf.fr"
(4.5 kB). One retry of c178 after a 7-minute pause (12:52 UTC): 403, same page. Per the good-citizen rule no further request (and no headless-browser
attempt, which would be working round a block). The worker should have stopped at the first 403 rather than sending all six; logged in ROOM.md 12:5x.
Earlier today other sessions also logged Gallica challenge/503 (ROOM 09:35, 10:37). So no crops, no passes, no decode, no control, no verifier for ink 52.

Plan that was priced and not spent (for the next brief): c179/c181/c183 at 1200 px ~$0.5; then ~9 pages x (2 blind Sonnet passes + 1 reconciliation) at
~$1.3-1.5 per pass (N6-VIV63's ledger rate) = ~$35-40 all in, over this brief's $35 cap at 80% -- so a single job would read about 6 pages and leave
the rest named. Expected depth, stated before any reading: inks 53, 54 and 63 all held D1 under the same pipeline and key (AUDIT.md), and nothing in
ink 52 suggests it would read further: a reading of 52 is likely D1 unless the f/m/p and qu key questions (ink 50/51 known plaintext) are settled first.

Requests: gallica.bnf.fr 7 (all 403); no other host. Subagent calls: 0. Sessions spawned: 0. Cost: see get_session.

## Remaining gaps (VIV52 refresh, 8 Oct 2026; supersedes the VIV-ANCHOR list, all its other lines kept)
Read so far: ink 40 checked against its decipherment 41 with Tomokiyo's key (N5-VIVK PASS); ink 54 read with key.tsv, gloss check PASS (N5-VIV54), window look-alike pass + re-decode, b2 + wrong-key PASS (N7-VIV54L); ink 53
ff.170r-171v read, b2 + wrong-key PASS (N6-VIV53B), window look-alike pass + ': :' join + re-decode, b2 + wrong-key PASS again (N7-VIV53L); ink 63 ff.190r-194r read in full (f.194r L5-10 added by N7-VIV63G): b2 PASS on every part (N6-VIV63, N6-VIV63B,
N6-VIV63C, N7-VIV63G), whole piece -1.548 vs p99 -1.836, wrong-key specificity PASS (real 0.288 vs p99 0.064), H 12,151 / M 2,329 / U 1,282 of 15,762 tokens. VIV-ANCHOR (8 Oct 2026): key.tsv V -> n (grade C, clerk word anchors) re-decodes all three inks: H 12,290 / M 2,369 / U 1,103 of 15,762 (63), 3,744 / 440 / 196 (53), 1,491 / 272 / 191 (54); b2 and 200-wrong-key gates PASS on each under new seeds.
Pieces with no decipherment located: fr.16105 63, fr.16104 52, 53, 54 (and 38, whose twin is deciphered).
- ink 63 N4 (audit 1 done 4 Oct 2026 by VIV63-A1, AUDIT.md AUDIT 3: N3, D1 fragments read, key published; recipient the King; no decipherment in fr.16105 c95-c248) - blocker: not-attempted; d'Ars 1884 book (VIV-BREMOND) and d'Ars's RQH 35 (1884) article pp.386-412 (L51, DESK-LAND) both checked: neither cites 10 Oct 1573; Ribera 2007 seen as Google Books snippets only (L50: note 139 not visible); fr.16105 c1-c94 and the fr.16106 pieces Gachard skips not viewed; next: Ribera 2007 in full through the owner's interlibrary loan (ILL-SWEEP batch), reading note 139 and every 1573 Saint-Gouard citation, ~owner minutes + $0.5 to land
- Flament 1996 (L'ambassade du marquis de Saint-Gouard en Espagne, maîtrise Lille 3, 158 p.) - blocker: needs-physical-access; only copy located Lille, Bib. G. Lefebvre, cote D 1996 3, "Non disponible pour le PEB" (SUDOC 201366568, L52, 4 Oct 2026); no digitised copy
- tools/iiif_lines.py on steep, uneven line slopes - blocker: not-attempted; --follow-slope (and --centres with it) snapped bands onto neighbouring lines on f.194r; next: an option to deskew the region by a fitted angle before a flat cut (what N6-VIV63C did by hand with PIL), with an offline test, ~$2
- ink 63 key questions (y, single o, c, e, 2, r) - blocker: not-attempted; label e ruled by VIV-KEYV (14 Oct 2026, AUDIT 7): key row e -> m now grade M -- label e merges >= 3 signs, (A) e-loop + n compound = mm (ink-67 comm- anchors, 15 ink-63 "-omman-"), (B) hooked c before 6 (plus contexts), (C) Tomokiyo col f row 1 (faict/France contexts); next for e: split label e into three labels on the existing crops (tools/lookalike_pass.py with the three pile exemplars in tx/vivkeyv_tiles.tsv, or the owner's sign sorter), re-decode with (A)+n -> mm, (C) -> f, (B) -> p as candidates, each through the PREREG'd anchor + wrong-key gates, ~$3; V settled as an n homophone by VIV-ANCHOR (8 Oct 2026, 7 of 8 clerk-anchored ink-40 positions, control 5/7 PASS; key.tsv row V, grade C); context table (N7-VIV63G, tx/viv63g_keyctx.tsv): y->l and e as an "m(m)" sign remain weak proposals; in ink 40 the clerk anchors give 2 (u 2, m 1), o (p 2), c (p 1), e (0): none reaches 3 positions; next: the ink 50/51 known plaintext (fr.16104 ff.157-159v against ff.162r-163r: crops + two blind passes, then tx/vivanchor.py on that stream), ~$15
- ink 63 label splits and overlap duplication - blocker: not-attempted; r/z, 2/z (f.193v 25x), c/e and 6/b (f.192r, 19x) left at pass A; readers wrote some s1/s2 overlaps twice (f.192r L06, L34; f.193r L07); f.193r err_2reader 0.297; next: tools/lookalike_pass.py on those pairs + a pre-registered overlap-dedup step in tx/viv63_clean.py, re-decode, ~$4
- ink 53 D2 (depth re-check done 6 Oct 2026, D1-F16104I, AUDIT.md AUDIT 4: hold D1, H 85.2%) - blocker: not-attempted; three instruments on f, m, p now: whole-label key-cell n-gram rank (D1-F16104K, negative), hand-placed shape judge (D07-VIV53, NON-TEST), and clerk word anchors on ink 40 (VIV-ANCHOR, PREREG-VIVANCHOR: control PASS, but f, m, p each under 3 decided positions: m 4 split 3:2/2:1/z:1, p 3 split o:2/c:1; f 4 of 6 on label p, which the key reads n -- a CONFLICT, key unchanged: "affaires" is written p p twice, so readers' label p merges an f-sign); V -> n moved 16 ink-53 letters, longest H run 41 (unchanged, salad), V_strict top-1 20 (unchanged, null p99 24); next: the ink 50/51 known plaintext (fr.16104 ff.157-159v vs ff.162r-163r) for more f, m, p anchors, then split label p by shape at the anchored f positions, ~$15
- ink 53 residual label questions - blocker: not-attempted; the 270 one-reader gaps were window re-read under PREREG-R7VIV53G (decoy control PASS): 121 settled present, 16 removed, 133 still flagged; the 82 UNSETTLED split tiles, the ': :'-as-null alternative and "rauldhoit" (f.171r L15) remain; f.171v gap windows mostly unfindable (65 of 87 kept, the reader called 56 NONE but mostly at L) -- the window x-estimate drifts on that page; next: hand-placed per-tile crops (DEF1-VIV54's method) for the 82 splits + the 133 kept gaps, or the owner's sign sorter, ~$2.5
- ink 54 clean reading - blocker: not-attempted; window look-alike pass done (residual 0.134), true-error audit a non-test, no stretch near ~42 letters (N7-VIV54L); next: owner's sign sorter on tx/lookalike54/*_focus.tsv (275 questions) or a window-instrument audit (lookalike_pass.py audit + viv53L_windows.py audit), ~$1.5
- ink 54 key question "to z" (qae) - blocker: not-attempted; key cell added (key.tsv Zu -> u, N7-VIV54R); two machine shape judges NON-TEST (N7-VIV54R, DEF1-VIV54); clerk anchors on ink 40 (VIV-ANCHOR) give the u-after-q slot to z 2 and 2 2 of 4 positions: undecided (no share >= 2/3); next: the owner's sign sorter with Zu as a pile (tx/lookalike54/viv54H_xmarks.tsv), or the ink 50/51 known plaintext for more qu anchors, ~$1
- ink 54 D2 (depth re-check done 7 Oct 2026, DA1-VIV, hold D1, H 76.2%) - blocker: not-attempted; ink 40 clerk anchors (VIV-ANCHOR) fixed V -> n only (4 ink-54 letters moved, H 1,491 of 1,954, longest H run 26, unchanged); f, m, p and u-after-q stay under 3 positions; next: the ink 50/51 known plaintext (fr.16104 ff.157-159v against ff.162r-163r), then a PREREG'd key-change step with the wrong-key control, ~$15
- label p carries f in ink 40 (VIV-ANCHOR CONFLICT) - blocker: not-attempted; 4 of 6 clerk-anchored f slots hold label p (key n), at f102v L07:46-47 and L34:33-34 ("affaires" both times); the key has no f row; crops cut and a sorter page built (D4-VIV, 8 Oct 2026: tx/sorter_fp/, 4 focus tiles + 2 p-labelled refs + the readers' f sign, preflight PASS); next: the owner sorts tx/sorter_fp/sorter_viv_fp.html, then tools/sign_sorter_apply.py and a PREREG'd key-change step with the wrong-key control, ~$1
- Judge calibration for this hand - blocker: not-attempted; the fr16 judge FAILs the known-good f.103r control at this noise (N5-VIV54, N6-VIV53); next: score a lower-noise control (the clerk decipherment's own text, or f.103r after a lookalike pass) to see whether the judge can gate at all, ~$2
- fr.16104 ink 52 (5 Sept 1572, to the Queen, ~270 lines) - blocker: not-attempted; premise in print negative (VIV52, 8 Oct 2026: Gachard II has no entry, d'Ars 1884 and Catherine IV no citation); leaves c179, c181, c183 still unviewed and no image step run, because gallica.bnf.fr blocked this container (VIV52: 403 "Sorry, you have been blocked" on 7 IIIF requests 12:50-12:52 UTC incl. one retry after a 7-min pause); next: from a container Gallica serves, view c178-c183 at 1200 px for a gloss or "dechiffré", then crops + 2 blind passes + 1 reconciliation per page under PREREG (gate b2 + wrong-key, as N6-VIV63), ~$30
- fr.16104 5 Sept 1572 cipher block (ff.157-159v) against its decipherment ff.162r-163r - blocker: not-attempted; known-plaintext check, not a reading; next: crops + two blind passes, aligned as tx/vivk_test.py, ~$15
- Unviewed stretches of the per-piece table - blocker: not-attempted; fr.16104 c1-c169, c192-c324 and fr.16105 c1-c94, c113-c191 not viewed (N5-VIVTAB); a decipherment of 63 filed in another volume (fr.16106 holds one such stray) not checked; next: 1200 px pass every second canvas, contact sheets, ~$3
- fr.16105 f.104r, first page of the decipherment - blocker: illegible; native crop shows word shapes only (N4-VIV3)
- Spanish-side copies (AGS Estado K) and Gachard vol. I - blocker: needs-physical-access; AGS is not digitised in a route this worker could open
## Escalation (8 Oct 2026, VIV52; from the VIV-ANCHOR list)
- [x] siblings: ink 38 located; ink 40 vs 41 aligned (N5-VIVK); decipherment 51 found (N5-VIV5S); per-piece table (N5-VIVTAB); ink 54 read (N5-VIV54); ink 53 ff.170r-171v read (N6-VIV53, N6-VIV53B); ink 63 ff.190r-194r read in full (N6-VIV63, N6-VIV63B, N6-VIV63C, N7-VIV63G)
- [x] clear-pages: decipherments 41, 44, 51, 68, 71, 76 are on the leaves; inks 54 and 53 interlinear words used as gloss checks (N5-VIV54 PASS, N6-VIV53 FAIL at the floor); f.171v has none (N6-VIV53B); ink 63 has none (order gate b2 instead)
- [x] known-keys: Tomokiyo's 1572-74 key on disk and held-out PASS (N5-VIVK); applied to inks 54, 53 and 63
- [x] print: Gachard I-II, d'Ars (book 1884 and RQH 35 article, L51), Catherine IV-V, Groen IV read; Ribera 2007 snippets (L50); d'Ars re-checked by date and by k-mer/phrase overlap against inks 53, 54, 63 (VIV-BREMOND); Kervyn I-VI grepped (N6-KERV); print_check on ink 54, 53 and 63 phrases (pc63b/, pc63c/); Gachard I-II, d'Ars, Catherine IV and X re-grepped for ink 52 (VIV52, none)
- [retired] key-rebuild: tools/stream_align.py from a flat start did not converge on this material (Arm A, 2 of 30 codes); a published key exists
- [x] image-check: fr.16104 c170-191 and fr.16105 c95-112, c192-248 viewed; native regions of f.173r-v, ff.170r-171v, ff.190r-194r (N5-VIV54, N6-VIV53, N6-VIV63, N6-VIV63B, N6-VIV63C, N7-VIV63G); ink 52 c179/c181/c183 not viewed: Gallica 403-blocked this container (VIV52, 8 Oct 2026)
- [ ] retry: ink 53 f/m/p key cells for the U labels (AUDIT 4; whole-label test negative, D1-F16104K; hand-placed per-position shape judge NON-TEST, control 4-5/12 vs 8/12, D07-VIV53; clerk word anchors on ink 40, VIV-ANCHOR 8 Oct 2026: control 5/7 PASS, V -> n assigned, f/m/p/qu under 3 positions, f on label p a conflict; next instrument: ink 50/51 known plaintext or sign sorter); ink 63 key questions on the key image (context table done, N7-VIV63G); ink 63 label questions (lookalike pass, overlap dedup); ink 53 residual unsettled tiles and kept gaps (window look-alike pass N7-VIV53L; gap re-read R7A-VIV53, 137/270 settled); ink 54 sorter/window audit (lookalike pass done, N7-VIV54L) and the col-u-row-3 relabel (key cell found, N7-VIV54Q; window judge NON-TEST, N7-VIV54R; hand-placed judge NON-TEST 0/18, DEF1-VIV54; next instrument: sign sorter / clerk alignment, hand-placed per-position crops)
Verdict: keep going: 14 internal gaps; ink 52 premise in print negative but its image step blocked by Gallica (VIV52, 8 Oct 2026); cheapest next: the owner sorts tx/sorter_fp/sorter_viv_fp.html (D4-VIV), ~$0 agent cost; then ink 52 c178-c183 from a container Gallica serves, ~$0.5, and the ink 50/51 known plaintext for f, m, p, ~$15

## VIV52-O (13 Oct 2026, 07:13-07:2x UTC by date -u, owner-account worker for LANE DEFAULT-A1-0640): ink 52 leaf premise, f.164r-f.164v transcribed and decoded
Brief: .claude/briefs/runs/2026-10-13-acct1-default-0640-jobs.md "### VIV52-O" (VIV52 steps 1-3 scoped to cap USD 10). Host: openapi.bnf.fr (BnF's
IIIF Image API v3; gallica.bnf.fr not used), 6 requests, all HTTP 200, >= 3 s apart, take/release lines in ROOM.md.

**Prior work** (`tools/prior_work.py ... --item-spec 'shelfmark=BnF fr.16104;folio=164r-168r;date=1572-09-05;sender=Vivonne;recipient=Catherine de
Medicis' --step-type transcribe --fetch`, exit 4): owed LEAD 1-own (this worker's own claim; recorded CLEAR), LOOK 2-leaf (answered by the leaf views
below; recorded CLEAR), UNCHECKED 4-editions Catherine I-IV/IX-X (VIV52 already grepped Catherine IV and X for "5 septembre 1572": no citation) and
Charriere III (Levant, out of scope); KEY-SOURCE rows point at ff.157-159v vs ff.162r-163r (the 5 Sept letter to the King and its decipherment), not
at ink 52. Check 5 after decode (`--reading piece52_decode.txt --offline`): "no distinctive phrase extracted" -- G3 unchecked (network print search
not in this wave's hosts).

**Step 1, leaf premise (finished).** c178, c179, c181, c183 at 1200 px (images/p52/ov_c*_1200.jpg): ink 52 runs **f.164r to f.168v**, 10 pages, not
ff.164r-168r: f.164r opens plain "Madame." then cipher (heading "du S^r de S^t gouard a la Reyne", old ink "52", docket "5 Septembre 1572" on f.163v);
ff.164v-168r full cipher (~30 lines a page); f.168v 15 cipher lines then plain "Madame ... l'Infante ... porte" and the closing "de Madril ce v^me jour
de Sept^bre 1572", signed; f.169r blank; f.169v the address leaf (c184, N5-VIVTAB). **No "dechiffré" leaf or clear copy on c178-c183**, and no
interlinear words on the native f.164r/f.164v regions. With the print premise (VIV52) negative, proceed.

**Crops** (debug overlays checked: one band per line; f.164r band L26 repeats L25, both readers marked it DUP independently):
```
$ python3 tools/iiif_lines.py --iiif-host openapi --ark btv1b9009609w --canvas 178 --region 4650,900,3250,3900 --out ciphers/fr16104-vivonne-spain-1572/images/p52 --prefix c178_f164r --follow-slope 400 --distance 80 --max-width 1600 --overlap 150 --debug
  ... 30 bands x 3 segments; wrote 90 crops and ciphers/fr16104-vivonne-spain-1572/images/p52/manifest.json
$ python3 tools/iiif_lines.py --iiif-host openapi --ark btv1b9009609w --canvas 179 --region 1200,700,2950,4100 --out ciphers/fr16104-vivonne-spain-1572/images/p52 --prefix c179_f164v --follow-slope 400 --distance 80 --max-width 1600 --overlap 150 --debug
  ... 30 bands x 2 segments; wrote 60 crops and ciphers/fr16104-vivonne-spain-1572/images/p52/manifest.json
```
Crops, overviews and debug overlays committed (images/p52, about 7 MB); source regions ignored (src_*, regenerate with the commands above).

**Units, stated before the first subagent call:** 2 pages x (2 blind Sonnet passes + 1 reconciliation) = 6 units at ~1.4 = ~8.4 + leaf views, as briefed.
**Transcription** (4 blind Sonnet calls, one per page per pass, crop paths only, SIGNS.md prompt as N6-VIV63; pass B worked bottom-up; passes frozen in
815a4fb1 before reconciliation; tx/viv63_clean.py unchanged; `tools/reconcile_passes.py` -> tx/rec_f164r, tx/rec_f164v). One pass-A call could not write
its file through Bash (auto-mode refusal) and wrote it through the Write tool on resumption, transcript unchanged by its own report.
| page | lines | signs A / B | err_2reader | splits settled by rule | splits left at pass A | one-pass gaps |
|---|---|---|---|---|---|---|
| f.164r | 29 (+1 DUP) | 1441 / 1395 | 0.152 | 48 | 94 | 78 |
| f.164v | 30 | 1359 / 1353 | 0.184 | 42 | 79 | 142 |
err_2reader is reader disagreement, not err_true. Commonest unsettled pair z/2 (26): f.164r L02 s2 eyed, a flat z-like sign with a short tail, the same
open pair as ink 63 -- left at pass A, graded M. One notation rule added to tx/viv52_decode.py before its first run (not committed before that run,
stated plainly): pass B wrote the pi sign "II", SIGNS.md's token is P (11 splits, one sign in two spellings). No other rule beyond the inherited
reconcile_vivk RULES + RULES54 + RULES63.

**Gates (PREREG-VIV52O.md, pushed 09fc0b67 before the passes returned; tx/viv52_test.py, seed '20261013VIV52O', 200 draws, 200 wrong keys; tx/viv52_result.json):**
| arm | C1 f.103r (1,831 letters) | C2 ink 54 (1,795) | target ink 52 f.164r-v (2,621) | verdict |
|---|---|---|---|---|
| b1 vs shuffled-key null p99 | -1.704 vs -1.736 pass | -1.658 vs -1.732 pass | -1.514 vs -1.739 | descriptive (pass) |
| b2 vs letter-order-shuffle null p99 | -1.704 vs -1.898 pass | -1.658 vs -1.824 pass | **-1.514 vs -1.775** | **PASS** (both controls pass with headroom) |
| c, 200 wrong keys through b2 | | | real margin **0.262** vs wrong-key margin p99 0.026 (max 0.066; 16/200 wrong keys pass b2 alone) | **PASS** |
Per page (descriptive): b2 f.164r -1.549 vs -1.769, f.164v -1.478 vs -1.746. key_tomokiyo.tsv (no V row): -1.507, b2 p99 -1.782, word cover 0.809
(key.tsv 0.808) -- the two keys differ only on V (U under key_tomokiyo).
fr16 judge, pasted (descriptive; the f.103r control fails this judge, N5-VIV54/N6-VIV53):
```
$ python3 tools/judge_plaintext.py specs/fr16106-vivonne-longlee-1579.json --file ciphers/fr16104-vivonne-spain-1572/piece52_decode.txt
FAIL language: score=-1.622, null_p99=-1.905, real_p05=-0.863, real_median=-0.783, mode=both, N=2621
ok   words: cover=0.727, min=0.5, real_text_median_cover=0.947
FAIL - fr16106-vivonne-longlee-1579 (a PASS is a gate for a verifier, not a reading; rule 10)
```
(no spec exists for this folder; the fr16106 spec carries the same fr16 corpus judge.)

**Reading** (tx/viv52_decode.py writes reading_piece52.tsv and tx/f164r_rec.tsv, tx/f164v_rec.tsv; `--check` passes; piece52_decode.txt = letters only).
2,727 tokens: **H 2,217** (0.813), **M 404**, **U 106**; no C, no S. H = both readers agree (or a rule settled it) AND the code is grade C in key.tsv --
key-source grading, not legibility, not a period decipherment of this letter. U codes: single o 23, {curl} 19, r 16, 2 12, II 7 (pass-A-only P/II gaps),
e 7. Longest H run 24 letters (f.164r L18; f.164v L19-20 "...dudangierournuo..."), under the ~42-letter stretch the ink 54 audit used.
**Expected depth, stated before reading: D1. Result: D1-like, as inks 53, 54 and 63** -- scattered words and short phrases, no clause above the
authentication distance (interpretation, not a gate; spelling normalised, decoded string in brackets): f.164r L04 "bien considere" [biencconoidere],
L05 "intention", L12-13 "intention", L17 "avoir traicte avecq ses" [auoirtraiccteaueccqses], L20 "intelligence de ce", L21 "craint ce ... aultre",
L25 "relation de ce", L28 "bien ... travailloit a continuer ... bonne" [traauailoitaccontignueraunhaboune]; f.164v L03 "apparence ... infinite",
L05 "apporter ... alteration", L10 "diligence de", L11 "venir du temps ... Flandre" [dutequou_uinten_landre], L14 "conduicte", L18 "contre ...
Flandre", L20 "du dangier", L21 "charge de France", L25 "contentement ... grand", L27 "religion", L28 "d'Orange?" [dauarange], L29 "Espaigne il
... estoit de leur". Between them, letter salad. No reading is claimed beyond D1 fragments; step 4 (first verifier) is the lane's.

Not done: ff.165r-168v (8 pages, ~230 lines), stopped at the unit plan. Requests: openapi.bnf.fr 6 (4 overviews, 2 native regions). Subagent calls:
4 Sonnet (one resumed once to write its file). Cost: not visible to this session.

## V-VIV52 (13 Oct 2026, 07:36-07:5x UTC by date -u, owner-account verifier for LANE DEFAULT-A1-0640): ink 52 f.164r-v audit 1
AUDIT.md "AUDIT 5": `tx/viv52_decode.py --check` up to date; `tx/viv52_test.py` re-run byte-identical (b2 -1.514 vs p99 -1.775 PASS; wrong-key
margin 0.262 vs p99 0.026 PASS); judge FAIL as reported. **N3, key published, D1 ("fragments read"), 2 of 10 pages.** Gachard II's own September 1572
table lists no 5 Sept letter to the Queen; d'Ars, Forneron II, Catherine IV/X cite other folios. Lead for the solver side: La Ferriere, Catherine IV
intro p. cxx, quotes a Saint-Gouard letter to the Queen (Anjou as king of England, "la peau de l'ours", the Infante; before Catherine's 29 Aug letter
arrived) citing fr.16104 f.191v -- not ff.164-168, but not excluded for ink 52's unread pages. print_check on 6 decoded phrases (print-check-52.tsv):
generic hits only; Google Books 503 throughout. SO-VIV52 queued. No over-claim found in VIV52-O.

## VIV-191V (13 Oct 2026, 09:45-09:5x UTC by date -u, account-4 worker for LANE DEFAULT-A4-0935): f.191v and its docket, the La Ferriere lead
Brief: .claude/briefs/runs/2026-10-13-acct4-default-0935-jobs.md "### VIV-191V". Host openapi.bnf.fr (IIIF Image API v3), 4 requests, all HTTP 200,
>= 3 s apart, take/release lines in ROOM.md; gallica.bnf.fr not used. Prior work (`tools/prior_work.py fr16104-vivonne-spain-1572 --item-spec
'shelfmark=BnF fr.16104;folio=191v;date=1572-09-19;sender=Vivonne;recipient=Catherine de Medicis' --step-type lookup --offline`, exit 4): the owed
LEAD 1-own rows are this folder's own image-check (c170-c191 viewed; c205-c208 never viewed) and V-VIV52's lead itself, which this job answers;
4-editions Catherine I-IV/IX-X UNCHECKED by the tool (Catherine IV p. cxx is the lead's own source, V-VIV52).

**Canvas.** `tools/gallica_folio.py btv1b9009609w --folio 191 --anchor 190=175r --anchor 187=173r --anchor 178=164r` (cached manifest, every label
'NP'): estimate c206-c208, centre c207. Checked by eye on the stamped folio numbers: c205 = f.188v / f.189r (stamped "189"), c206 = f.189v / f.190r
("190"), c207 = f.190v / f.191r ("191"), **c208 = f.191v (left) / f.192r ("192")**. One canvas per opening here, as at c178-c183.
Images (1600 px wide): images/p191/ov_c207_1600.jpg and ov_c208_1600.jpg committed; ov_c205/ov_c206 not committed (tracked images already ~35.5 MB, over the 30 MB line before this job) -- re-fetch from the URLs in images/manifest.json "viv191v"; local upscaled crop of
f.191v lines 15-20 from the overview (no request): images/p191/crop_c208_f191v_infante_ours.jpg. No subagent or vision call beyond this worker's eye.

**(a) Cipher or clear.** f.191v is **clear script, a clerk's decipherment**, not cipher: f.191r (c207 right) is headed "dechiffré de la precedente",
with docket "19 Sept. 1572" and old ink number "58" beside the stamped "191"; f.191v and f.192r continue the same clear hand. The cipher letter it
deciphers ("la precedente") runs in cipher on ff.188v-189v (c205, c206 left; its first page, on c204 or earlier, not viewed) and ends on f.190r
(c206 right): two cipher lines, then plain text ("Madame, les Infantes ... la Royne de Montaigne [?] ... Jenvoye a V. Mag.te des lectres que luy
escript le Roy Catholique ..."), the closing "de Madril ce xix^e jour de Sep^bre 1572" and the signature "De Vivonne". f.190v (c207 left) is the
address leaf, endorsed "19 Septemb. 1572" (the address itself, written across the fold, not read at this size).
**(b) Date, sender, addressee as written.** 19 Sept 1572 (docket on f.191r; close on f.190r "xix ... Sep^bre 1572"); sender De Vivonne (signature
f.190r); addressee "Madame" (opening of f.191r, "Madame, je remercie ..."; f.190r "V. Mag.te"), i.e. the Queen. Read from the image only.
**(c) Same letter as ink 52 f.164r-v?** **No.** Different date (19 Sept vs 5 Sept), different leaves (ink 52 runs ff.164r-168v, closed "de Madril
ce v^me jour de Sept^bre 1572", VIV52-O), and the text does not match. Three ink-52 decoded phrases looked for on f.191v (and f.191r/f.192r at
overview): "avoir traicte avecq ses" (f.164r L17) -- not found; "Flandre" (f.164v L11, L18) -- not found; "d'Orange?" [dauarange] (f.164v L28) --
not found. Converse: f.191v's own key words ("Angleterre", "Infante", "Ysabel", "ours", "Diego", "Austriche") occur 0 times in piece52_decode.txt
(grep, spaces stripped). The overview is legible only word-by-word in places, so this is a "not seen at 1600 px" result, not a full collation.
**(d) Is it the passage La Ferriere quotes?** **Yes.** f.191v lines 15-20 (underlined in the manuscript) read, by eye from the crop, spelling
approximate: "... [Monsieur ... Roy] d'Angleterre et le marier avecques Madame l'Infante Dona Ysabel. Je dictz que je trouverois cela tres bon et a
propos si c'estoit chose que l'on peult esperer, mais qu'en France nous avions ung proverbe qui dict que nous achetons la peau de l'ours premier
qu'il soit mort, et que pour asseurer a la maison d'Austriche tous ses estatz il ne seroit pas mal a propos ..." -- the Anjou/England/Infante
proposal and the "peau de l'ours" answer that Catherine IV p. cxx cites to "fonds français n° 16104, f° 191 v°".
**Consequence for ink 52:** the lead does not touch ink 52. La Ferriere's quotation is from the period decipherment (ink 58, ff.191r-192r+) of
the 19 Sept 1572 letter to the Queen, not from ff.164r-168v; ink 52 gains no known plaintext from it and its premise stays as V-VIV52 left it.
Side finding for the per-piece table: the 19 Sept 1572 letter to the Queen (cipher ending f.190r) has its clerk decipherment on ff.191r-192r+
(ink 58) -- a cipher/decipherment pair on the leaf, usable as a known-plaintext check like inks 40/41 and 50/51; piece_table.tsv not edited
(its ink numbers for the cipher piece, probably 57, not seen). Requests: openapi.bnf.fr 4. Cost: not visible to this session.

## VIV-DECH (13 Oct 2026, 10:29-10:4x UTC by date -u, account-4 worker for LANE DEFAULT-A4-0935): ink 52 misplaced-decipherment residual, dechiffre heads
Brief: .claude/briefs/runs/2026-10-13-acct4-default-0935-jobs.md "### VIV-DECH". Host openapi.bnf.fr (IIIF Image API v3), 10 requests (the job's limit),
all HTTP 200, >= 3 s apart, take/release lines in ROOM.md; gallica.bnf.fr not used. Prior work (`tools/prior_work.py fr16104-vivonne-spain-1572
--item-spec 'shelfmark=BnF fr.16104;folio=164r-168v;date=1572-09-05;sender=Vivonne;recipient=Catherine de Medicis' --step-type lookup --offline`,
exit 4): the owed rows are LEAD 1-own live claims (VIV52-O, V-VIV52, V2-VIV52 and this job's own), all on ink 52 itself; 4-editions Catherine
I-IV/IX-X UNCHECKED by the tool (VIV52 grepped IV and X by hand). Not --recorded (the job answers the V2-VIV52 lead, it does not change its item).
No canvas numbers for these leaves were on disk (piece_table.tsv has none past c190; Gachard gives no folios), so canvases were placed by the
folio offset (canvas minus 15-17 here) and checked on the stamped folio and old ink numbers. All views 1600 px, read by this worker's eye; no
subagent or vision call. Committed: images/pdech/ov_c196_1600.jpg, ov_c213_1600.jpg, ov_c219_1600.jpg (the three dechiffre heads); the other
seven are listed with their URLs in images/manifest.json "vivdech" (folder already over the 30 MB line before this job, 38 MB images/).

**Ink 52's opening and phrases used for the comparison** (VIV52-O): f.164r heading "du S^r de S^t gouard a la Reyne", docket 5 Septembre 1572,
plain "Madame." then cipher; closing f.168v "de Madril ce v^me jour de Sept^bre 1572". Decoded phrases: (1) "derniere de la" (f.164r first lines,
in "...avoir ... derniere de la ..."), (2) "bien considere" (f.164r L04), (3) "avoir traicte avecq ses" (f.164r L17). A misplaced decipherment
of ink 52 would open "Madame", carry a 5 Sept docket or close, and show these phrases near its head.

| canvas | folio | ink | head as written (date / addressee / first words, spelling approximate) | ink 52? |
|---|---|---|---|---|
| c196 | f.181r | 56 | docket "19 Septembre 1572", heading "dechiffré de la precedente"; no salutation line: "[D']aller devers le Roy cath. ... que l'entreprise faicte par luy ... le marquis d'Aimon[t] ... ceste nouvelle ... la Royne [de] Montaigne ... Don Diego ... Vos[tre] Mat." -- to the King (f.180v left: ink 55's address leaf, endorsed "... Septembre 1572", "19 septemb. 1572") | **no**: 19 Sept, King, opens without "Madame"; content after the 7 Sept news; none of the three phrases in the 30 visible lines |
| c213 | f.197r | 60 | docket "19 Septemb. 1572", heading "dechiffré de la precedente", ink "60" beside stamped "197"; "Elle ne doubte point que ... soudaine resolution et mutation aux affaires de France n'aye apporte de dela une grande joye ... affaires de Flandres ... dissimulation ... le marquis d'Aimon[t] ... V[ost]re Altesse"; whole decipherment on this page, closed "De xix^e septembre 1572" -- to the duc d'Anjou (its cipher, ink 59, opens f.195r "du S^r de S^t gouard au Duc d'Anjou", "Monseigneur, je loue et remercie Dieu ...", c211) | **no**: 19 Sept, Anjou ("Vostre Altesse"), St Bartholomew aftermath ("mutation aux affaires de France"); 18 lines, far short of ink 52's ~290 cipher lines; none of the three phrases |
| c219 | f.202r | 62 | docket "2[3/5] Sept. 1572" (Gachard: 23 Sept), heading "dechiffré de la precedente", ink "62" beside stamped "202"; "Sire, Ce matin a fort bonne heure m'a envoie dire le Roy catholique une nouvelle qui luy est venue ceste nuict des affaires de Flandres, qui est que le duc d'Alve avoit par deux fois batu ses ennemis ... [prince d']Orange ..." -- to the King (its cipher, ink 61, f.198r "du S^r de S^t Gouard au Roy", c214; ends f.200r, signed De Vivonne, c216 = c217) | **no**: "Sire", 23/25 Sept, the King; news of Alba's victories; none of the three phrases |

**Oct-Dec 1572 pairs: not reached.** Two probes placed them: c288 = f.266v | f.267r, cipher ending in plain "... le Roy Catholique ... la Royne et
Madame la Princesse de Portugal ... nouveau president ...", closed "de Madril ce xxij? de Novembre 1572", signed, "Sire" -- the 22 Nov letter to the King
(ink 88; Gachard LXXXVIII-LXXXIX); c296 = f.274r, a clear letter (no cipher, no "dechiffré" heading) "du S^r de S^t gouard a la Reyne", docket
"17 Decemb. 1572", old ink 9[3 or 5] (not settled at this size), "Madame, j'ay faict tant ... en la pratique dont je escrivis dernierement a
V. Maj^te ... affaires de Flandres ... l'aisnee des Infantes ... prince d'Orange ... la princesse de Portugal" -- not ink 52 (17 Dec; content on
the Infantes and the Emperor). So the dechiffre leaves of 89 and 91 (the 22 Nov letter to the Queen) lie at about c289-c295, those of 78 and
83 between c220 and c287, and 97 and 101 after c296; none viewed. f.201r (c218) is a near-blank slip between ink 61's end and its address leaf.
**Answer on this evidence:** no decipherment of the 5 Sept 1572 letter to the Queen (ink 52) is filed among the post-19 Sept September
decipherments (inks 56, 60, 62): each is headed "dechiffré de la precedente" and dated and addressed as its own cipher letter. The Oct-Dec
pairs remain unviewed (gap line updated). No prior plaintext for ink 52 found; nothing to flag. Requests: openapi.bnf.fr 10. Cost: not
visible to this session.

## VIV-DECH2 (13 Oct 2026, 10:52-11:0x UTC by date -u, account-4 worker for LANE DEFAULT-A4-0935): Oct-Dec 1572 dechiffre heads vs ink 52
Brief: .claude/briefs/runs/2026-10-13-acct4-default-0935-jobs.md "### VIV-DECH2". Host openapi.bnf.fr (IIIF Image API v3), 8 requests (the job's
limit), all HTTP 200, >= 3 s apart, take/release lines in ROOM.md; gallica.bnf.fr not used. Prior work: `tools/prior_work.py fr16104-vivonne-spain-1572
--item-spec 'shelfmark=BnF fr.16104;folio=164r-168v;date=1572-09-05;sender=Vivonne;recipient=Catherine de Medicis' --step-type lookup --offline`,
exit 4, the same eight LEAD 1-own rows VIV-DECH listed (this lane's own ink-52 work) plus 4-editions UNCHECKED; not --recorded (no change to the item).
The manifest labels every canvas "NP"; canvases were placed by the stamped folio (offset canvas minus 21-22 here) and checked on the leaf. Same
method and comparison set as VIV-DECH (ink 52 opens "Madame.", docket 5 Septembre 1572; phrases "derniere de la", "bien considere", "avoir traicte
avecq ses"). All views 1600 px, read by this worker's eye; no subagent or vision call. Committed: images/pdech/ov_c265, c275, c289, c292, c315
(_1600.jpg); c300, c303, c305 listed with URLs in images/manifest.json "vivdech2" only (folder over the 30 MB line before this job).

| canvas | folio | ink | head as written (date / addressee / first words, spelling approximate) | ink 52? |
|---|---|---|---|---|
| c265 | f.243v (end) | 78 | end of a dechiffre in the clerk's hand: "... grand presse aux affaires ... apoplexie ... malladie ...", closed "Du vij^e No^bre 1572"; f.244r docket "Novembre", blank face. Head (about f.243r or f.242r, c264) not viewed | **no**: closed 7 Nov 1572 (Gachard 77-78, to the King) |
| c275 | f.254r | 83 | docket "15 novemb", heading "dechiffré de la precedente"; text "... de l'Albanie que la raison veult ... Constantinople ...", whole decipherment on the page, closed "Sire, Je supplie le Createur donner a V^re Mag^te ... de Madrid ce [xv] jour de No^bre 1572", signed De Vivonne (left, f.253v: ink 82 cipher, its lower half in clear) | **no**: 15 Nov, "Sire", the Turk and Albania; none of the three phrases |
| c289 | f.268r | 89 | docket "22 Nov 1572", heading "dechiffré de la precedente", ink 89 beside stamped 268; "... depuis mes dernieres ... nouvelles du S^r Don Jehan d'Austria ... Roy catholique ... entreprise ... Don Jehan ... Secille ..." (left, f.267v: ink 88's address leaf, endorsed "22 novemb. 1572") | **no**: 22 Nov, to the King (ink 88); Don John's enterprise; none of the three phrases in the 30 visible lines |
| c292 | f.271r | 91 | docket "22 novemb 1572", heading "dechiffré de la precedente", ink 91 beside stamped 271; "Le S^r Conte ... charge ... ambassadeur ... Flandres ... duc d'Alve ... M^r de Guise ... V. Ma^te", whole decipherment on the page, closed "de Madril ce xxij^e no^bre 1572" (left, f.270v: ink 90's address leaf) | **no**: 22 Nov, to the Queen; 21 lines against ink 52's ~290 cipher lines; none of the three phrases |
| c315 | f.292v-293r | 97 or 101 | dechiffre body in the clerk's hand, no heading on this opening: "... Roy de Portugal ... navigation ... gentilhomme Anglois ... Thomas Stuc[ley] ... Irlande ..." | **no** on content seen (Stukeley and Ireland, Dec 1572 news; none of the three phrases in ~45 lines); head and date not viewed |

Probes that were not dechiffre leaves: c300 = f.277v | f.278r, a short clear letter docketed "1[2/3] Decembre 1572" and an address leaf;
c303 = f.280v | f.281r, ink 96 cipher head, "17 Decembre 1572", "du S^r de S^t goard au Roy", "Sire"; c305 = f.282v | f.283r, ink 96 cipher
continued. So ink 97's dechiffre head lies after f.283 (c306 or later) and runs to or past f.293 unless c315 is already ink 101.
**Answer on this evidence:** among the Oct-Dec 1572 decipherments, those of inks 83, 89 and 91 were viewed at the head and each is "dechiffré
de la precedente" of its own letter (15 Nov King, 22 Nov King, 22 Nov Queen); ink 78's closes 7 Nov; a December dechiffre body (97 or 101)
carries Stukeley/Ireland news. None opens "Madame" with a 5 Sept docket and none shows the three ink-52 phrases. Not viewed: the heads of 78
(c264), 97 (c306-c31x) and 101. No prior plaintext for ink 52 found; nothing to flag. Requests: openapi.bnf.fr 8. Cost: not visible to this session.

## VIV-HEADS (13 Oct 2026, 18:54-19:1x UTC by date -u, account-1 worker for LANE DEFAULT-A1-1840): heads of the dechiffre leaves of inks 78, 97, 101 vs ink 52
Brief: .claude/briefs/runs/2026-10-13-acct1-default-1840-jobs.md "### VIV-HEADS". Host openapi.bnf.fr (IIIF Image API v3), 8 requests (the job's limit),
all HTTP 200, >= 3 s apart, take/release lines in ROOM.md; gallica.bnf.fr not used. Prior work: `tools/prior_work.py fr16104-vivonne-spain-1572
--item-spec 'shelfmark=BnF fr.16104;folio=164r-168v;date=1572-09-05;sender=Vivonne;recipient=Catherine de Medicis' --step-type lookup --offline`,
exit 4: the owed rows are LEAD 1-own (this lane's own ink-52 work and this job's claim) plus 4-editions UNCHECKED, as VIV-DECH/VIV-DECH2; not
--recorded (no change to the item). Same method and comparison set as VIV-DECH (ink 52 opens "Madame.", docket 5 Septembre 1572; phrases
"derniere de la", "bien considere", "avoir traicte avecq ses"). All views 1600 px, read by this worker's eye; no subagent or vision call. Canvas
= right page f.(c-21)r here (c262 -> f.241r, c310 -> f.288r, c321 -> f.299r). Committed: images/pdech/ov_c262_1600.jpg and ov_c310_1600.jpg (the
two heads found); the other six are listed with URLs in images/manifest.json "vivheads" only (folder over the 30 MB line before this job).

| canvas | folio | ink | head as written (date / addressee / first words, spelling approximate) | ink 52? |
|---|---|---|---|---|
| c262 | f.241r | 78 | docket "7 Novembre 1572", heading "dechiffré de la precedente", ink "78" beside stamped "241"; no salutation line: "J'ay voullu actendre le retour ... ung peu de temps ... Vostre Mat^e ne vouldroit nullement du duc d'Alve ... mauvaise procedure ... affaires de Flandres ..."; left page f.240v is the address leaf endorsed "... St Gouard au Roy ... Novembre 1572"; body continues c263 (f.241v-242r) and c264 (f.242v-243r): Flandres, Alba, prince d'Orange, marquis d'Aimont | **no**: 7 Nov, to the King, opens without "Madame"; none of the three phrases in the ~95 lines seen on c262-c264 |
| c310 | f.288r | 97 | docket "17 Decembre 1572", heading "dechiffré de la precedente", ink "97" beside stamped "288"; "Et je luy fis entendre comme il me sembla qu'il venoit a propos pour le service et dignité de Vostre Ma^te ... la rebellion de la Rochelle ..."; left page f.287v the address leaf (endorsed "... 18 decemb."); its cipher, ink 96, ends f.287r with the plain close "de Madrid ce xvij^e jour de decembre 1572", signed (c309); body continues c311 (f.288v-289r: la Rochelle, galleys, duc d'Alve) | **no**: 17 Dec, to the King (ink 96), la Rochelle; none of the three phrases in the ~85 lines seen |
| c321 | f.298v-299r | 100 | not a dechiffre: a few plain lines then cipher on f.298v, cipher on f.299r -- the 23 Dec 1572 cipher letter to the King (ink 100) still running | not reached: ink 101's head lies after f.299r (c322-c324); no request left |

Other views: c308 = f.285v-286r, ink 96 cipher (f.286r signed); c309 = f.286v-287r, ink 96 cipher end and close (above).
**Answer on this evidence:** the heads of the dechiffre leaves of inks 78 (f.241r, 7 Nov 1572, King) and 97 (f.288r, 17 Dec 1572, King) are each
"dechiffré de la precedente" of their own letter; neither opens "Madame", carries a 5 Sept docket, or shows the three ink-52 phrases. Ink 101's head
was not reached: ink 100's cipher still runs on f.299r (c321), so 101 begins on c322-c324 (one or two requests). No decipherment of the 5 Sept 1572
letter to the Queen found; nothing to flag. Requests: openapi.bnf.fr 8. Cost: not visible to this session.

## VIV-101 (13 Oct 2026, 19:20-19:3x UTC by date -u, account-1 worker for LANE DEFAULT-A1-1840): head of the dechiffre leaf of ink 101 vs ink 52
Brief: .claude/briefs/runs/2026-10-13-acct1-default-1840-jobs.md "### VIV-101". Host openapi.bnf.fr (IIIF Image API v3), 1 request (limit 4), HTTP 200,
take/release lines in ROOM.md; gallica.bnf.fr not used. Prior work: `tools/prior_work.py ... --step-type lookup --offline` with VIV-HEADS's item-spec,
exit 4, the same owed rows (LEAD 1-own: this lane's own ink-52 work; 4-editions UNCHECKED); not --recorded (no change to the item). Same method and
comparison set as VIV-DECH/VIV-HEADS (ink 52 opens "Madame.", docket 5 Septembre 1572; phrases "derniere de la", "bien considere", "avoir traicte avecq
ses"). One 1600 px view, read by this worker's eye; no subagent or vision call. Committed: images/pdech/ov_c322_1600.jpg (manifest key "viv101").

| canvas | folio | ink | head as written (date / addressee / first words, spelling approximate) | ink 52? |
|---|---|---|---|---|
| c322 | f.300r | 101 | docket "24 decemb. 1572", heading "dechiffré de la precedente", ink "101" beside stamped "300"; no salutation line: "Je ne fauldray comme ... sur les ... du duc d'Alve ..." (~32 lines, hand fast, words approximate); left page f.299v: ink 100 cipher ends, then a plain postscript "Sire, depuis ma lettre escripte le Seigneur Cayas ..." (passeports, Roy Catholicque, Don Diego), close "... de Madrid ce ... decembre 1572", signed "De Vivonne" to "Vostre Mag^te" | **no**: 24 Dec, decipherment of ink 100 (to the King, "Sire"), opens without "Madame"; none of the three phrases in the ~32 lines seen |

**Answer on this evidence:** the head of ink 101 (f.300r) is the "dechiffré de la precedente" of ink 100, the 23-24 Dec 1572 letter to the King; it is not
ink 52. With VIV-DECH, VIV-DECH2 and VIV-HEADS, every post-19 Sept 1572 dechiffre head in fr.16104 named in the residual has now been viewed; no
decipherment of the 5 Sept 1572 letter to the Queen found among them. Nothing to flag. Requests: openapi.bnf.fr 1. Cost: not visible to this session.

## VIV-LAT (14 Oct 2026, 00:00-00:1x UTC by date -u, account-4 worker for LANE VIV-KEYSTONE): key-constrained lattice decode with a confusion matrix learnt on this hand
Measurement only (PREREG-VIVLAT.md, pushed c65d5063 before any score); key.tsv, reading_piece63.tsv, status.json untouched. Runner
`tx/vivlat/run_vivlat.py` (prep / dev / devctl / devplain / confirm --lam 2), results `tx/vivlat/dev_result.json`,
`tx/vivlat/confirm_result.json`, every tx_bench output under `tx/vivlat/dev/*.bench.txt` and `tx/vivlat/confirm/*.bench.txt`.
Instrument: tools/key_decode_lattice.py from-passes A B --confusion-matrix M --matrix-only (spread 0.3), decode --lang fr16; M =
learn-confusion on passes A, B, Z vs truth (add-0.5 over the 32 key signs); baseline = argmax of the plain two-reader lattice;
scorer tools/tx_bench.py --exclude-flagged --paired.

Prior work (tools/prior_work.py --item-spec 'shelfmark=BnF fr.16105;folio=103r;sender=Saint-Gouard;recipient=Charles IX'
--step-type decode --known-answer item:vivonne1573-f103r-confirm2, exit 4): plaintext KNOWN (expected: the clerk decipherment is
the benchmark's truth); the four LEAD rows are this folder's own [x] clear-pages/siblings lines (N4-VIV2, N4-VIV3, N5-VIVK), i.e.
the source of the truth, not a prior run of this step; grep of NOTES.md and benchmark-tx/txeng*/ for a lattice run on this hand: none.

Step 1, dev (vivonne1573-f102r-dev2, two folds odd/even lines, M from the other fold, pooled): plain top-1 err as measured 0.280
(345/1234), flagged-excluded 0.130 (88/679).

| lam | err meas | err fx | fx lines impr/wors (p) | fx signs fixed/broken | meas lines impr/wors (p) |
|---|---|---|---|---|---|
| 1 | 0.259 | 0.115 | 14/4 (0.031) | 24/12 | 20/4 (0.0015) |
| **2** | **0.256** | **0.111** | **14/3 (0.013)** | **24/10** | **20/4 (0.0015)** |
| 4 | 0.266 | 0.115 | 11/2 (0.023) | 19/8 | 14/5 (0.064) |
| 8 | 0.271 | 0.121 | 9/3 (0.146) | 15/8 | 11/5 (0.210) |

Chosen lam 2 (dev rule: largest improved - worsened); dev stop rule passed. Controls at lam 2 (not gating): off-diagonal-shuffled
M 0.268 / 0.116, fx lines 10/2 (p 0.039); plain lattice + LM with no M 0.271 / 0.119, fx lines 10/3 (p 0.092). Most of the dev gain
is the language model and generic flip mass, not the learnt confusion pattern (real M adds about 0.005 err_fx over the shuffled
one). Truth-in-lattice on the held folds (top-1 wrong scored positions whose truth set meets the lattice candidates): 82/279
(odd 43/144, even 39/135) all, 34/45 flagged-excluded.

Step 2, confirm, one look (vivonne1573-f103r-confirm2, lam 2, M from all of dev2, passA_S2 + passB_S2):

| | err meas | err fx |
|---|---|---|
| plain top-1 | 0.291 (311/1068) | 0.146 (73/500) |
| lattice lam 2 | 0.296 (316/1068) | 0.150 (75/500) |

Gate (a) fx lines improved 3 / worsened 6, p 0.508 (signs fixed 4 / broken 6): FAIL; (b) 0.296 > 0.291: FAIL; (c) real key rank 1
of 101 value-shuffled keys, z 4.93 (lattice mean 4-gram -1.229 vs shuffles mean -1.868, max -1.566); top-1 decode rank 1, z 4.21:
PASS. 140 positions changed. **Gate verdict: FAIL.** Truth-in-lattice on confirm2: 29/234 = 0.124 of the top-1's wrong scored
positions (flagged-excluded 5/32 = 0.156); the plain lattice 7/234 = 0.030. Under 50%: the ceiling explains the failure (the
learnt flip rarely puts the true sign in the lattice on the S2 readers, whose errors differ from the dev readers'), so it is
logged untested-by-this-tool at this error, not a negative on the idea (TX-DECODE 27/97 shape). Step 3 (ink 63) not run, by
the registered rule. The dev gain did not transfer from the dv1 readers to the S2 readers; a confusion matrix learnt on one
reader set is not a property of the hand alone.
Suggestion (not done, outside the brief): add this result to tools/data/tool_shelf.tsv's `key_decode_lattice.py
--confusion-matrix` row (second hand, dev PASS / confirm FAIL, ceiling 0.124).

## VIV-67 (14 Oct 2026, 00:01-00:2x UTC by date -u, account-4 worker for LANE VIV-KEYSTONE): ink 67 / ink 68, a second known-plaintext pair of this hand
Brief: .claude/briefs/runs/2026-10-13-acct4-keystone-viv-jobs.md "VIV-67". Measurement only: key.tsv, reading_piece63.tsv, status.json and
every committed reading untouched. PREREG-VIV67.md pushed (1a2ace2f) before any pass, decode or alignment.

Prior work (`tools/prior_work.py fr16104-vivonne-spain-1572 --item-spec 'fr.16105 f.201r ink 67 cipher + ff.205r-205v ink 68 dechiffre'
--step-type transcribe`, exit 4; ink 67 has no items.tsv row): owed LOOK 2-leaf (answered by this job's 600 px overview of c206/c210/c211,
below: plain head + cipher on f.201r, no gloss on the cipher leaf; the decipherment is on its own leaves) and UNCHECKED 3-tomokiyo / 3-solver /
4-editions (by hand: Tomokiyo's henryiii.htm page covers the key only, no ink-67 plaintext on disk; neither solver cache names fr.16105 f.201r;
the ink-67 plaintext is the clerk's ink 68 by construction, so this known-answer step does not depend on print). Novelty not in question
(a period decipherment is the truth); no N-class (rule 10).

**Leaves (by eye, 600 px overviews, openapi.bnf.fr):** c206 right = f.201r, "20 Octobre 1573 / Madrid", "du s.r de S.t Goard au Roy", ink "67 / 201":
four plain lines ("Sire, Encores quil ne se presente occasion de consequence ... de sa certaine") then 24 cipher lines; c210 right = f.205r, "dechiffre de
la precedente", ink "68 / 205", opening "Sire. Encores quil ne se presente ..." (as piece_table row 68); c211 left = f.205v. Offset canvas = folio + 5 here.

**Crops** (pasted per Usage 6; overlays checked; a first 3 x 1600 px cut with the text starting mid-s1 and a second at x 800 that clipped
line starts were discarded before any pass):
```
$ python3 tools/iiif_lines.py --ark btv1b9009663p --canvas 206 --iiif-host openapi --region 4100,350,3650,5350 --out ciphers/fr16104-vivonne-spain-1572/images/p67 --prefix c206_f201r --follow-slope 400 --distance 70 --max-width 1600 --overlap 150 --debug
  (fetch; 29 bands incl. header and duplicate slope bands -- crops discarded)
$ python3 tools/iiif_lines.py --image .../images/p67/src_image_v3_ark_12148_btv1b9009663p_f206_4100_350_3650_5350.jpg --region 680,1500,2970,3700 --out ciphers/fr16104-vivonne-spain-1572/images/p67 --prefix c206_f201r --follow-slope 400 --distance 70 --max-width 1560 --overlap 150 --debug
  region 2970x3700, 25 lines, 25 bands x 2 segments; pitch 126 distance 70 prominence 223.3; wrote 50 crops   (L01 = 4th plain line, L02-L25 cipher)
$ python3 tools/iiif_lines.py --ark btv1b9009663p --canvas 210 --iiif-host openapi --region 4300,350,3600,5500 ... --lines-per-crop 3 --debug   (fetch; crops discarded)
$ python3 tools/iiif_lines.py --ark btv1b9009663p --canvas 211 --iiif-host openapi --region 150,100,3750,5750 ... --lines-per-crop 3 --debug   (fetch; crops discarded)
$ python3 ciphers/fr16104-vivonne-spain-1572/tx/viv67_strips.py <c210 src> --out images/p67/dec --prefix c210_f205r --strips 8   # ink-minimum strips, halves sharing 400 px
$ python3 ciphers/fr16104-vivonne-spain-1572/tx/viv67_strips.py <c211 src> --out images/p67/dec --prefix c211_f205v --strips 7
```
Line detection on the widely spaced clerk hand is unreliable (as N5-VIVK found), so the decipherment pages were read from ink-minimum strips
(checked by eye: every cut falls between lines). No image is committed; images/manifest.json "viv67" holds the URLs and the regenerate commands.

**Passes** (6 Sonnet subagent calls, blind, one page per call): f.201r A and B (tx/SIGNS.md); ff.205r, 205v A and B (tx/DEC_READ.md).
- Cipher: tools/reconcile_passes.py then tx/reconcile_vivk.py's six label rules unchanged -> tx/f201r_rec.tsv, 1,339 signs; **err_2reader 0.201**
  (agree 1,070 / 1,340 aligned, 270 disagreement columns; label rules settled 17, 172 splits left at pass A, 81 one-pass gaps). Top splits:
  3/z 15, o/p 14, c/u 12, S/s 11, h/k 9, o/u 7, n/r 7. Tokenisation fix (tx/viv67_prep.py, before reconcile_passes): the whitespace tokenizer split
  multi-word [PLAIN:...] groups (L01's plain line, and "[PLAIN:Il non]" which both readers wrote inside L12 and L17) into 17 word tokens that entered
  the cipher stream; joined into one token, re-reconciled; the gating control was the same to four places before and after (0.7443).
- Decipherment: tx/viv67_merge_dec.py (tx/merge_dec.py's rules, imported) -> tx/dec67_norm.txt, 2,102 letters; A/B word agreement f.205r 0.661
  (pass B wrote 36 output lines for ~24 manuscript lines, partly repeating the h1/h2 overlap), f.205v 0.803. tx/dec_norm.txt (ink 41) untouched.

**Gate (PREREG-VIV67; benchmark-tx/build_vivonne_f201r.py, tx/vivk67_result.json):** whole f.201r stream (1,270 collapsed codes) vs whole dec67
(2,102 letters), confirm2's align() and control, seed 20261014:
| key | real match share | aligned keyed | 200 value-shuffled keys mean / p95 / max | rank | verdict |
|---|---|---|---|---|---|
| published (key_tomokiyo.tsv), gating | **0.744** | 1,009 | 0.453 / 0.507 / 0.527 | 1 of 201 | **PASS** |
| key.tsv full set (report only, 50 draws) | 0.739 | 1,026 | 0.457 / 0.498 / 0.531 | 1 of 51 | PASS |
For comparison, ink 40 f.103r (confirm2 control): 0.605 vs p95 0.498. Aligned span dec67[298:1701] (control window +-200 = [98:1901]): the ~300 letters before it are the four plain lines
(not in cipher) and the 401 letters after it are not reached by f.201r -- consistent with the cipher continuing on f.201v.

**Truth item registered:** benchmark-tx/vivonne1573-f201r-dev.truth.tsv (split=dev, BENCHMARK-TX.tsv row, sha256 6c145337...; `--check` ok):
1,339 positions, 894 scored (unaligned 178, off-key 82, align-uncertain 67, letter-off-key 62, key-M y 36 / S 15 / b 5); flags at build: align-conflict 163,
clerk-split 356, unflagged 454; no verifier flags file yet. Scores (tools/tx_bench.py, as measured / flagged-excluded): passA 0.185 / 0.037, passB 0.199 /
0.046, committed reconciliation 0.160 / 0.000 -- the committed figure is circular (the truth was aligned to it), as confirm2's is.

**Unkeyed and M labels against the clerk letter** (tx/viv67_labels.py -> tx/viv67_labels.tsv per occurrence with DP confidence, tx/viv67_labels_summary.tsv;
counts only, NO key edit; top aligned letters, all occurrences / at local confidence >= 0.5):
| label | status | n | aligned | top aligned | conf >= 0.5 |
|---|---|---|---|---|---|
| y | M (y=h) | 44 | 36 | r 11, l 9, n 4, e 4 | r 11, l 9, e 4, h 3 |
| o (single) | outside key | 30 | 16 | p 5, e 3, i 3, r 2 | p 5, e 3, i 2, r 2 |
| c | outside key | 25 | 18 | p 8, e 5, u 2, i 2 | same |
| S | M (S=b) | 24 | 15 | b 10, a 1, e 1, g 1 | b 10 |
| V | outside published key (key.tsv V=n, C) | 17 | 13 | n 7, s 2, t 1, m 1 | same |
| t | outside key | 7 | 5 | g, r, s, u 1 each | -- |
| {curl} | outside key | 7 | 6 | scattered | -- |
| 2 | outside key | 6 | 5 | e 3, u 1, m 1 | same |
| i | outside key | 6 | 3 | q, p, i 1 each | -- |
| b | M (b=z) | 5 | 5 | z 2, f, p, m 1 each | same |
| r | outside key | 5 | 4 | l, q, m, p 1 each | -- |
| e | outside key | 5 | 5 | m 4, s 1 | same |
| Z | outside key | 3 | 2 | l 1, y 1 | -- |
| l, 5, 8, H, {scribble}, {blot} | outside key | 1-2 each | | | |
Totals: 193 occurrences of 19 labels, 138 aligned. Read beside ink 40's anchors (VIV-ANCHOR): V -> n again the top letter (7 of 13); S's published value b is
the top letter (10 of 15) on this leaf, where ink 40 had a above b; y does not take h (r 11, l 9: the reader label y still merges more than one sign); e -> m
(4 of 5) matches N7-VIV63G's weak "m(m)" proposal; c and single o both lean p (8 of 18, 5 of 16), 2 leans e (3 of 5). Interpretation only, no gate run on
any label; a key change is a later PREREG'd job with the wrong-key control.

Not done (brief met at step 4 + outputs): f.201v-203r (the rest of ink 67) and ff.205v end-207 (rest of ink 68) not fetched; no lattice/VIV-LAT recipe
run on the new item; no verifier flags. Requests: openapi.bnf.fr 6 (3 x 600 px overviews, 3 native regions, all HTTP 200, >= 3 s apart, take/release
lines in ROOM.md); gallica.bnf.fr 0. Subagent calls: 6 Sonnet (2 cipher, 4 decipherment). Cost not visible to this session.

## VIV-KEY (14 Oct 2026, 00:36-00:5x UTC by date -u, account-4 worker for LANE VIV-KEYSTONE): key rows for the unkeyed labels from the pooled clerk anchors of ink 40 and ink 67
Brief: .claude/briefs/runs/2026-10-13-acct4-keystone-viv-jobs.md "Wave 2" / "VIV-KEY". PREREG-VIVKEY.md pushed (0795fa90e) before any pooled tally,
key change, gate or score. Disk only: requests 0, subagent calls 0. Rule 3 third-attempt clause: VIV-ANCHOR's instrument on new material (the ink-67 anchors).

Prior work (`tools/prior_work.py fr16104-vivonne-spain-1572 --item-spec 'fr.16105 ink 63 ff.190r-194r key rows for unkeyed labels (pooled clerk anchors
ink 40 + ink 67)' --step-type key`, exit 4): owed LEAD 1-own = this job's own ROOM claim (recorded CONTEXT in prior-work.tsv); UNCHECKED 3-tomokiyo /
3-solver / 4-editions are generic (no unit identity) -- this step adds key rows from the clerk's own period decipherments, so it does not rest on print.

**Tally (tx/vivkey.py -> tx/vivkey_tally.tsv, tx/vivkey_result.json; `--check` 0):** ink 40 = VIV-ANCHOR's word-anchored positions (confidence 1.0);
ink 67 = VIV-67's DP-aligned occurrences at dp_conf >= 0.5. Rule: top letter >= 3 positions and >= 2/3 of pooled counting positions; ink-40 vs ink-67 top
disagreement = CONFLICT.
| label | key before | ink 40 | ink 67 (conf >= 0.5) | pooled top / n | decision |
|---|---|---|---|---|---|
| e | -- | (none) | m 4, s 1 | m 4/5 = 0.80 | **-> m** (row added, grade C) |
| 2 | -- | u 2, m 1 | e 3, u 1, m 1 | -- / 8 | **CONFLICT** (ink 40 top u, ink 67 top e): no row |
| c | -- | p 1 | p 8, e 5, u 2, i 2, s 1 | p 9/19 = 0.47 | under rule |
| o (single) | -- | p 2 | p 5, e 3, i 2, r 2, a 1, l 1 | p 7/16 = 0.44 | under rule |
| t | -- | n 1 | g, r, s, e 1 each | -- / 5 | under rule |
| r | -- | -- | l, q, m, p 1 each | -- / 4 | under rule |
| i | -- | -- | q 1, i 1 (p 1 below conf) | -- / 2 | under rule |
| Z, 5, 8, l | -- | | 1-2 each | | not a candidate (< 3 aligned) |
| V (keyed n C) | | n 7, s 1 | n 7, s 2, t, m, q, o 1 | n 14/21 = 0.67 | confirms key n; report-only |
| S (keyed b M) | | | b 10 of 14 | 0.71 | confirms key b; report-only, no grade change |
| y (keyed h M) | | | r 11, l 9, e 4, h 3 ... | r 11/34 = 0.32 | under rule; report-only (y still merges signs) |
| b (keyed z M) | | | z 2, f, p, m 1 | 0.40 | under rule; report-only |
Plaintext p and f: no label reaches the rule (p leads on c and on single o, at 0.47 and 0.44); m: label e only.
**The four e -> m anchors are all inside "comm-"** (f201r L05:53 "command", L10:59, L12:36, L13:14 "comme"; the fifth, L15:52, aligns to s): consistent
with an m homophone and equally with a double-m sign (N7-VIV63G's weak "m(m)" proposal). The row reads one m. Every anchor is on one leaf of one letter.

**Key change:** key.tsv row `e  m  C` (source: clerk decipherments ink 41 + ink 68 pooled, VIV-KEY; n_aligned 5, n_match 4, note with the positions).
Re-decoded, each `--check` exit 0: tx/viv63_decode.py, viv53G_decode.py, viv54L_decode.py, viv53L_decode.py, viv53_decode.py, viv54_decode.py,
viv52_decode.py (and tx/viv67_labels.py, unchanged). Pre-existing, not from this job: tx/viv63g_keyctx.py `--check` already exited 1 before the key change.
Letters moved (every label-e token, U -> H/M): 63: 161; 53 (G, L, base): 16; 54 (L): 7, 54 base: 6; 52: 7.
| ink (reading) | before H / M / U | after H / M / U |
|---|---|---|
| 63 (reading_piece63.tsv) | 12,290 / 2,369 / 1,103 | 12,368 / 2,452 / 942 |
| 53 (reading_piece53_G.tsv) | 3,744 / 440 / 196 | 3,760 / 440 / 180 |
| 54 (reading_piece54_L.tsv) | 1,491 / 272 / 191 | 1,494 / 276 / 184 |
| 52 (reading_piece52.tsv) | 2,217 / 404 / 106 | 2,221 / 407 / 99 |
(83 of the 161 ink-63 e tokens grade M because the readers split on them or one pass is missing; 78 grade H.)

**Gates (PREREG (v); tx/vivanchor_gates.py, new `--seed/--tag` options, defaults unchanged; tx/vivkey_gates_{63,53,54}.json):**
| ink | seed | C1 f.103r b2 | C2 b2 | target s vs b2 p99 | 200 wrong keys: real margin vs p99 (b2 passes) | verdict |
|---|---|---|---|---|---|---|
| 63 | 20261014VK-63 | PASS | ink 54 PASS | -1.5349 vs -1.8360 | 0.3011 vs 0.0517 (49/200) | PASS |
| 53 | 20261014VK-53 | PASS | ink 54 PASS | -1.6036 vs -1.8373 | 0.2337 vs 0.0531 (33/200) | PASS |
| 54 | 20261014VK-54 | PASS | ink 53 PASS | -1.6345 vs -1.8204 | 0.1859 vs 0.0509 (20/200) | PASS |
Ink 53 registered V_strict stretch (seed 20261014VK-53-stretch): top-1 20, top-3 mean 18.33, null median 13, null p99 20: not above its null p99.
**What the gates can and cannot say (rule 3, post-hoc, not in the PREREG):** the target statistics barely move (53: -1.6037 under VIV-ANCHOR -> -1.6036;
54: -1.6342 -> -1.6345), because 7-161 changed letters cannot move a whole-text score. One post-hoc run of ink 54 with the row read `e = i` instead
(tx/vivkey_posthoc_e_i_gates_54.json, same seed, key.tsv restored after) also PASSes both gates, with a slightly better target score (-1.6306). So these gates
show the key change did not break the decode; they cannot tell e = m from another letter. The row rests on the clerk anchors alone.
**Crossword check (report-only, PREREG (iv)):** `tools/decode_key.py` needs a ciphertext file; ink 63's codes were written one line per row to a scratch
file and run against key.tsv as it stood before this job (`--ciphertext <scratch>/ct63.txt --key <scratch>/key_before.tsv --try e=m --lm fr16`):
```
e=m: n 161, current -, statistic -1543.6 bits over I; null p95 positions , value class -287.6; reject (no better than the runner-up) [non-blind]
e=mm: n 161, current -, statistic -2557.8 bits over I; ... reject (no better than the runner-up) [non-blind]
e=e: n 161, current -, statistic -1461.9 bits over I; ... reject
e=s: n 161, current -, statistic -1012.5 bits over I; ... reject
e=i: n 161, current -, statistic 155.7 bits over NULL; null p95 positions , value class -548.1; undecided (a null could not be built ...) [non-blind]
```
On ink 63's own contexts the fr16 character model prefers i at the label-e positions and puts m below the random-letter p95. The tool's letter control is
Danzay (clean text, 19/23); ink 63 reads at a per-sign error of 0.15-0.30 and its decode is salad, so this is a weak counter-signal, not a test. It is,
however, the only signal from ink 63 itself, and it disagrees with the clerk anchors. **For the verifier:** the anchors (4, one leaf, all "comm-") against
the crossword (161 positions, prefers i); a shape look at the ink-63 e tiles against the ink-67 "comme" tiles would settle which.

**Reported, not gated (PREREG (vi)):** fr16 judge mean log10 P over ink 63's decode letters: -1.5329 (14,659 letters) -> -1.5349 (14,820). Longest H run
(every M/U breaks it, across line ends): 63: 40 -> 40 (f191v L27-28, unchanged); 53: 41 -> 41; 54: 26 -> 26. Five longest ink-63 H stretches after:
40 f192r L11-12 "riccationatouteoccesacctionsnelotiations"; 40 f191v L27-28 "leaqesoailquonttousouautoutrailantcereoe"; 38 f192r L08-09
"ieoccaauaruarticculariteqetenouisccert"; 36 f194r L03 "uaueooienteientenqenoedentcemieneuio" (new: an e token now reads m); 36 f194r L02-03
"cedeoonseruictsiqeselqseoroistelestc". No stretch reaches the ~42-letter authentication distance; no clause gained.
**Rule 10 / verifier:** the readings of inks 63, 53, 54 and 52 changed after AUDIT.md; AUDIT.md and the SO rows are not edited by this worker. Per-token grade
counts above; no depth or N-class set. Report what was found and where it was not found; no novelty classified.

## VIV-CLS (14 Oct 2026, 00:36-01:0x UTC by date -u, account-4 worker for LANE VIV-KEYSTONE): a supervised sign classifier trained on f.102r + f.103r, one look at f.201r
Brief: .claude/briefs/runs/2026-10-13-acct4-keystone-viv-jobs.md "Wave 2", "VIV-CLS". Measurement only: key.tsv, reading_piece63.tsv, status.json and every
committed reading untouched. PREREG-VIVCLS.md pushed f7bf5aecb (00:50 UTC) and its Addendum A (chosen setting) eecb5560c (00:54 UTC), both before any f.201r
tile was classified for the gate or its truth opened. Full figures: tx/vivcls/RESULTS.md.

Prior work (`tools/prior_work.py fr16104-vivonne-spain-1572 --item-spec 'fr.16105 f.201r ink 67 tiles; f.102r/f.103r ink 40 tiles: supervised sign
classifier' --step-type transcribe`, exit 4; run LATE, after the one c206 region fetch and the training-leaf fit, not before the first priced step as the
brief asks -- no f.201r score had been computed yet): owed LEAD 1-own (the VIV-KEY claim: key rows, not tiles; recorded CLEAR), LOOK 2-leaf (f.201r viewed by
VIV-67 at 600 px and by this job's native overlay: no gloss; CLEAR), UNCHECKED 3-tomokiyo / 3-solver (a known-answer measurement against the clerk's ink 68,
not a reading; CLEAR), UNCHECKED-NET 3-solver registry and 4-editions (not run: no reading). Earlier classifiers on this hand: TXE3-6 (f.102r only, kNN
0.772 vs chance 0.818, VERIFY-6), TXE4-4/8/10 (f.102r): none trained on two leaves or tested on a third.

**Images:** one openapi.bnf.fr request (c206 native region 4100,350,3650,5350, HTTP 200, take/release lines); f.201r re-cut with VIV-67's exact command
(25 bands x 2, overlay checked by eye); f.102r / f.103r crops on disk. Nothing committed; images/manifest.json "vivcls" holds the commands.
**Tiles and map:** tools/glyph_atlas.py segment (pen units, --median-h pool), one atlas for the three leaves (tx/vivcls/seg.py): 1,655 / 1,835 / 1,139 tiles.
tools/box_token_align.py, round 1 width only, round 2 label-aware with a cross-leaf top-k (LOO guard on). Coverage (scored positions with exactly one 1:1
tile): **f.102r 0.504, f.103r 0.464, f.201r 0.464** (against passA; 0.447 against its own ref skeleton) -- the clerk joins signs, so about half of every page
has no single tile.
**Fit:** glyph_atlas classify --only-train-labels on 961 truth-labelled tiles; cross-leaf CV over 8 settings 0.354-0.391 top-1 error (majority 0.84); chosen
hog+zone+topo / LDA / k 5.
**One look, f.201r (vivonne1573-f201r-dev, 415 covered scored positions):**
| | as measured | flagged-excluded |
|---|---|---|
| passA top-1 err / classifier top-1 err | 0.154 / **0.313** | 0.023 / 0.240 |
| fixed / broken; lines improved / worsened | 16 / 82; 1 / 20 | 4 / 51; 1 / 16 |
| truth in classifier top-3 among passA's wrong | **0.359 (23 / 64)** | 0.80 (4 / 5) |
tx_bench --paired (hybrid = passA with the top-1 at covered tokens): 0.253 vs passA 0.185 as measured, lines 2 improved / 20 worsened, p 0.0001.
**Gate: (a) FAIL, (b) FAIL** (0.359 < 0.50). **Control** (training labels permuted, seed 20261014): top-1 err 0.848 vs chance 0.908; registered band
>= 0.858, missed by 0.010, so formally the real numbers license nothing; the miss is the label-aware map leaning the covered set toward positions where any
label agrees with passA, a bias that favours the classifier, so it does not rescue the fail. The top-3 is not fed to key_decode_lattice.py.
Reading: the fit transferred across letters as CV predicted (0.313 on f.201r vs CV 0.354), but an image kNN on this hand's pen units reads at about twice
the readers' error and covers half the page; its top-3 holds the truth for 0.359 of the readers' covered errors (vs the readers' own lattice, 0.124 on
f.103r), i.e. 23 of passA's 165 errors on the page. Descriptive only: where its top-1 agrees with passA, passA is wrong 0.10 of the time; where they
disagree, 0.28.
Not done: no lattice run, no ink-63 change, no glyph_atlas.py option added (the existing classify options did the fit; the pass-format output is in
tx/vivcls/run.py). Requests: openapi.bnf.fr 1; gallica.bnf.fr 0. Subagent calls: 0. Cost not visible to this session.

## VIV-70 (14 Oct 2026, 01:13-01:2x UTC by date -u, account-2 worker for LANE VIV-KEYSTONE, account 4): ink 70 / ink 71, a third known-plaintext pair of this hand
Brief: .claude/briefs/runs/2026-10-13-acct4-keystone-viv-jobs.md "VIV-70" (= VIV-67 with the 70/71 names). Measurement only: key.tsv,
reading_piece63.tsv, status.json and every committed reading untouched. PREREG-VIV70.md pushed (9ddc481a6) before any native fetch, pass or alignment.

Prior work (`tools/prior_work.py fr16104-vivonne-spain-1572 --item-spec 'fr.16105 f.211r ink 70 cipher + ff.215r-215v ink 71 dechiffre' --step-type
transcribe`, exit 4): LEAD x2 = the live VIV-KEYV and VIV-KEY claims on this slug (other units: the e -> m row; not ink 70); LOOK 2-leaf answered by this
job's 600 px overviews (below: plain head + cipher on f.211r, no gloss on the cipher; the decipherment is on its own leaves); UNCHECKED 3-tomokiyo / 3-solver
by hand as VIV-67 (Tomokiyo's page covers the key only; no solver cache names fr.16105 f.211r); the ink-70 plaintext is the clerk's ink 71 by construction.
No N-class (rule 10).

**Leaves (by eye, 600 px overviews, openapi.bnf.fr; offset canvas = folio + 5 as VIV-67 found):** c216 right = f.211r, "4 Novembre 1573 / Madrid", "du s.r de S.t
Gouard au Roy", ink "70 / 211": about 20 lines of plain French ("Sire, Le xx.e Octobre j'escripvis a V[ost]re Ma[jes]te par ung courrier depesche en Flandres ...")
then a mixed line ("Et a ce qui j'entendz ... autre partz de son Roy . de tres beaux ..." -- both readers wrote it all [PLAIN]) and 10 cipher lines ending on the
page with a full stop. c220 right = f.215r, "dechiffre de la precedente", ink "71 / 215", opening "Quant a l'apparence de leurs affaires et ce que ilz y ...";
c221 left = f.215v. The decipherment covers only the cipher part and runs ff.215r-217 (brief), so f.211r's 10 lines are about the first fifth of it: the
cipher of ink 70 very likely continues on f.211v ff. (not viewed). f.211v NOT added: the block is under 15 lines, but one more page (1 request + 2 calls +
reconciliation) would have projected the job over its cap.

**Crops** (pasted per Usage 6; overlay and every band checked by eye; images untracked, images/p70/.gitignore; regenerate per images/manifest.json "viv70"):
```
$ python3 tools/iiif_lines.py --ark btv1b9009663p --canvas 216 --iiif-host openapi --region 4100,350,3650,5350 --out .../images/p70 --prefix c216_f211r --debug
  region 3650x5350, 32 lines (fetch; crops discarded)
$ python3 tools/iiif_lines.py --image .../images/p70/src_image_v3_ark_12148_btv1b9009663p_f216_4100_350_3650_5350.jpg --region 250,2960,3400,1340 --out .../images/p70 --prefix c216_f211r --follow-slope 400 --distance 60 --max-width 1560 --overlap 150 --debug
  12 bands x 3 segments, wrote 36 crops   (band L10 was a duplicate of L09 by eye on all three segments: deleted, L11/L12 renamed L10/L11; L01 = mixed line, L02-L11 cipher)
$ python3 tools/iiif_lines.py --ark btv1b9009663p --canvas 220 --iiif-host openapi --region 4300,350,3600,5500 ... --lines-per-crop 3 --debug   (fetch; crops discarded)
$ python3 tools/iiif_lines.py --ark btv1b9009663p --canvas 221 --iiif-host openapi --region 150,100,3750,5750 ... --lines-per-crop 3 --debug   (fetch; crops discarded)
$ python3 ciphers/fr16104-vivonne-spain-1572/tx/viv67_strips.py <c220 src> --out images/p70/dec --prefix c220_f215r --strips 8   (every cut between lines, by eye)
$ python3 ciphers/fr16104-vivonne-spain-1572/tx/viv67_strips.py <c221 src> --out images/p70/dec --prefix c221_f215v --strips 7
```

**Passes** (6 Sonnet subagent calls, blind, one page per call, crop paths only): f.211r A (top-down) and B (bottom-up) with tx/SIGNS.md; ff.215r, 215v A and B with tx/DEC_READ.md.
- Cipher: tx/viv70_prep.py ([PLAIN:...] tokenisation fix, as viv67_prep.py), `tools/reconcile_passes.py tx/f211r_passA_c.tsv tx/f211r_passB_c.tsv --out-dir tx/rec_f211r`
  (signs A 516, B 530, agree 452 / 534 = 84.6%, 82 disagreement columns: **err_2reader 0.154**), then `tx/reconcile_vivk.py f211r` (six label rules unchanged: settled 3,
  left at pass A 57, one-pass gaps 22) -> tx/f211r_rec.tsv, 534 signs (519 codes after confirm2's o o collapse).
- Decipherment: `tx/viv67_merge_dec.py f215r f215v --out dec70_norm.txt` (the script gained an --out option; its default still writes dec67_norm.txt, re-run byte-identical)
  -> tx/dec70_norm.txt, 2,614 letters; A/B word agreement f.215r 0.840, f.215v 0.801.

**Gate (PREREG-VIV70; benchmark-tx/build_vivonne_f211r.py --control-only, tx/vivk70_result.json):** whole f.211r stream (519 codes) vs whole dec70 (2,614 letters), seed 20261014:
| key | real match share | aligned keyed | 200 value-shuffled keys mean / p95 / max | rank | verdict |
|---|---|---|---|---|---|
| published (key_tomokiyo.tsv), gating | **0.700** | 456 | 0.602 / 0.661 / 0.701 | **2 of 201** | **FAIL** (real > p95, but one shuffled key 0.7007 above it) |
| key.tsv full set (report only, 50 draws; carries VIV-KEY's e -> m) | 0.689 | 466 | 0.598 / 0.649 / 0.661 | 1 of 51 | PASS |
Per the PREREG: no truth item, no label table; raw counts only -- 81 of 519 codes are outside the published key or M in key.tsv: {curl} 24, y 20, S 7, V 6, o 5,
8 3, e 3, c 3, 9 2, and t, (, 5, {omega}, i, Z, ",", b 1 each. benchmark-tx/build_vivonne_f211r.py was NOT run past --control-only; nothing is registered in BENCHMARK-TX.tsv.

**Why it failed (diagnosis after the verdict, not a gate; tx/viv70_diag_trim.py -> tx/vivk70_diag_trim.json):** the published-key decode of tx/f211r_rec.tsv reads the
opening of dec70 plainly ("...de leurs affaires et ce ... il semble ... iour en iour il leur uiendra de pires nouuelles de leurs pais bas ... nulle nouuelle expedition ...
iusques a auoir seu l'arriuee du grand commandeur en attendant que courrier est depesche pour expedition dargent et la resolution de sa depesche est prinse en six heures ..."),
but the band DP spread the 510 aligned signs across dec70[400:2213] (a 2,614-letter target for 519 codes; band 400 around a linear reference that assumes the cipher covers
the whole target), so both the real share and the null (mean 0.602, against 0.453 on f.201r) were measured over a smeared alignment. VIV-67's pair had 1,270 codes for
2,102 letters; here the cipher is about a fifth of its decipherment. With the target trimmed to the opening, length fixed by ink 67's own ratio (1,403 letters / 1,270 codes)
+ 200 = 773 letters: real **0.769** vs 200 shuffled keys mean 0.458, p95 0.522, max 0.572, rank 1 of 201. That number is post hoc and licenses nothing (rule 3, PREREG);
it names the instrument fault (confirm2's align() with a whole-text target when the cipher covers a small fraction of it) and the next registered run.

Not done (stopped at the failed gate, as the brief says): truth item vivonne1573-f211r-dev, label table tx/viv70_labels*.tsv (script tx/viv70_labels.py written, not run),
f.211v ff. (rest of ink 70), ff.216r-217 (rest of ink 71). Requests: openapi.bnf.fr 6 (3 x 600 px overviews, 3 native regions, all HTTP 200, >= 3 s apart, take/release
lines in ROOM.md); gallica.bnf.fr 0. Subagent calls: 6 Sonnet (2 cipher, 4 decipherment). Cost not visible to this session.

## VIV-KEYV (14 Oct 2026, 01:11-01:3x UTC by date -u, account-4 verifier for LANE VIV-KEYSTONE): ruling on key row e -> m (AUDIT 7)
Verifier hat (separate from VIV-KEY). Full write-up: AUDIT.md "AUDIT 7". Prior work (`tools/prior_work.py ... --step-type key`, run after the
image step, late): exit 4, the owed LEADs are own work (VIV-KEY and this job's claim); generic UNCHECKED 3-tomokiyo / 3-solver / 4-editions do not bear
on a key-row ruling from the clerk's own decipherments. Requests: openapi.bnf.fr 3 (HTTP 200: c206 f201r, c199 f193v, c198 f192v native regions);
subagent calls 1 (Sonnet, blind shape grouping). No image committed (crops untracked; tx/vivkeyv_tiles.py rebuilds the montage).
**Finding:** label e merges at least three signs in ink 63: (A) a small e-loop joined to an n-like stroke with a long descender ("e n", the sign of
all four ink-67 comm- anchors; 40 of 161 ink-63 e tokens precede n, 15 as "d e n s p" = "-omman-"); (B) a hooked open c before 6 ("[e]6oox" = plus);
(C) the large looped g-like sign of Tomokiyo col f row 1 ("[e]s tz : #" = faict, "[e]rance"). Blind Sonnet call: all four (C) tiles one group, both
(B) tiles one group, neither grouped with any comm- tile; ink-63 (A) tile a6 grouped with ink-67 anchors (tx/vivkeyv_blind.txt, tx/vivkeyv_tiles.tsv;
tile choice by the verifier, not blind). Tomokiyo's table: the sheet's label-e tile is col g row 1; no plainly-e-shaped sign carries m there.
**Ruling: key.tsv e -> m downgraded C -> M** (m holds for sign (A) only, and there the following n is the second m; the crossword's i preference is
explained by the merge). Re-decoded, all seven `--check` exit 0; decode letters unchanged, grades only: ink 63 H 12,368 -> 12,290, M 2,452 -> 2,530,
U 942. Depth D1 held on inks 63, 53, 54, 52 (longest H runs 40 / 41 / 26 / 24, salad); status.json depth fields refreshed; N3 unchanged; SO prompts
unchanged (grades only; see AUDIT 7 section 6).
Next (in Remaining gaps): split label e into (A)/(B)/(C) on the existing crops, then per-sign key rows with their own anchors.

## VIV-HUMAN (14 Oct 2026, 01:11-01:3x UTC by date -u, account-4 worker for LANE VIV-KEYSTONE): the owner's blind packet on f.201r
Brief: .claude/briefs/runs/2026-10-13-acct4-keystone-viv-jobs.md "Wave 3", "VIV-HUMAN". Builds the pre-registered test of whether a person's
eye reads the positions where the blind readers fail, on the known-answer leaf f.201r (vivonne1573-f201r-dev, truth = the clerk's ink 68).
Nothing scored; key.tsv, every reading and status.json untouched. PREREG-VIVHUMAN.md pushed b81df8bdb (01:16 UTC) before the page was built;
Addendum A 9a123cedb (01:18 UTC) before publishing and before any answer.

Prior work (`tools/prior_work.py fr16104-vivonne-spain-1572 --item-spec 'fr.16105 f.201r ink 67 tiles: blind sorter packet for a person
(VIV-HUMAN)' --step-type transcribe`, exit 4): owed LEAD 1-own (VIV-KEY's live claim: key rows, not this packet; CLEAR), LOOK 2-leaf (f.201r
viewed by VIV-67 and VIV-CLS, no gloss; CLEAR), UNCHECKED 3-tomokiyo / 3-solver and UNCHECKED-NET 3-solver / 4-editions (a known-answer
measurement, not a reading; not run). Same rows VIV-CLS recorded CLEAR.

**Sets** (tx/vivhuman/sets.py, `--check`; answer sheet tx/vivhuman/questions.tsv): 454 unflagged scored truth rows; 217 have one pen-unit tile
(passA's aligned token mapped 1:1 in VIV-CLS's tx/vivcls/real/map_r2_f201r.tsv). W (passA or passB wrong) = 13, all taken; R (both right) =
204, 12 sampled, seed 20261014; shuffled as Q01-Q25. W is 8 passB-only (z for 3 x4; r, t, l, a for n, R, L, @) and 5 passA S-for-s.
**Addendum A** (box check by eye, before publishing): Q06 (W; box on the sign after the s, map off by one on L04) and Q10 (R; box holds two
signs) dropped; scored n W 12, R 11; cut points 8/12, 10/11, 4/12; incomplete under 19 of 23 answered.
**Page:** tools/sign_sorter.py, blind (no key values, no decode choices, no reader weights; `mode blind` in the page data): 577 tiles of
f.201r in 37 piles named by the committed reconciliation's sign labels, plus the 23 question tiles in a neutral pile `unsorted` (family
"to place") and the tray (--focus-to-tray). Why not their committed piles: on unflagged rows the committed label equals the truth (circular),
and the page's own-pile-first card with its one-tap keep would hand the answer over. Tile y/h from the ink rows of each tile's column span in
the sheared line crop, mapped to the region with the crop's slope fit (tx/vivhuman/build_inputs.py). Context image: the f.201r region at 0.5
scale (embedded). Size 1.6 MB.
Build: `python3 ciphers/fr16104-vivonne-spain-1572/tx/vivhuman/build_inputs.py` then, in tx/sorter_human/,
`python3 tools/sign_sorter.py --signs signs.tsv --labels labels.tsv --pages pages --focus focus.tsv --focus-to-tray --cipher-lines
cipher_lines.tsv --title "Vivonne f.201r: 23 signs to place" --lede "..." --page-scale 0.5 --page-quality 60 --tile-quality 80 --out
sorter_viv_human.html` (the page image tx/sorter_human/pages/f201r.jpg is untracked, regenerated from the "vivcls" manifest commands).
**Scoring** (the parent, when the owner answers): ArtifactData export of the page's db to DIR, then `python3 tools/sign_sorter_apply.py --labels
ciphers/fr16104-vivonne-spain-1572/tx/sorter_human/labels.tsv --db DIR --out DIR/settled.tsv --page
ciphers/fr16104-vivonne-spain-1572/tx/sorter_human/sorter_viv_human.html` and `python3 ciphers/fr16104-vivonne-spain-1572/tx/vivhuman/score.py
DIR/settled.tsv`. `score.py --selftest` (synthetic exports): all-right 1.0/1.0 -> instrument; a person who reads like passB -> W 0.333 "not an
instrument"; all new-sign -> not an instrument; empty -> incomplete; a keyed row refused.
Known limits (PREREG): small W; every W row is one the committed reconciliation already reads right; map leans to passA; piles near-truth
on this leaf (an upper bound for ink 63).
Requests: openapi.bnf.fr 1 (c206 native region, HTTP 200, take/release lines); gallica.bnf.fr 0. Subagent calls 0. Cost not visible to this session.
**Published:** https://claude.ai/artifact/WAPAiDSVDwYjvDotTgBFhA (private to the owner, capabilities db; db collections moves and piles listed empty after publishing); repo copy tx/sorter_human/sorter_viv_human.html (1.6 MB, sha256 779748ba...).
Preflight (`python3 tools/sorter_preflight.py ciphers/fr16104-vivonne-spain-1572/tx/sorter_human/sorter_viv_human.html`):
```
PASS template: ok, Fix the cut present, marker 2026-10-09.7
PASS answerable: 23 focus tiles, 37 named piles of 38, 0 unanswerable
PASS right line: 577 tiles; 0 tile(s) off the cipher lines, 1 of 1 listed lines have tiles; shape: 3 wide (>2.5x median 45 px), 0 strip-height boxes, 2 ink outside 3-60% of 577 measured; 5 = 0.9% (limit 5%) [list: ciphers/fr16104-vivonne-spain-1572/tx/sorter_human/cipher_lines.tsv]
PASS contact sheet: 24 tiles beside their line strips -> ciphers/fr16104-vivonne-spain-1572/tx/sorter_human/sorter_viv_human.preflight.png (seed 20261006; eye it before publishing)
PASS colour: tokens, tints, box colours and person-facing text pass tools/cvd_check.py
PASS gestures: owner rules R05 (tap = to the tray, hold = the card, every box; swipes move nothing) and R02 (lines above and below) hold on iPhone 13, iPhone SE and a mouse: 217 checks, 16 skipped (a tile kind this page lacks, counted per device) [test_gestures.js]
PASS pan: owner rule R09 (slide the card's picture to look around) holds on an iPhone 13: 3 checks [test_pan.js --probe]
preflight: PASS
exit 0
```
cvd_check (`python3 tools/cvd_check.py --palette sorter_light`): normal/protan/deutan/tritan worst pair #0072B2 vs #767676, margins +1.8/+0.7/+3.1/+1.1, sorter_light: PASS, exit 0.

## Remaining gaps (VIV-HUMAN refresh, 14 Oct 2026; supersedes the VIV-KEYV list, all its other lines kept)
Read so far: ink 40 checked against its decipherment 41 with Tomokiyo's key (N5-VIVK PASS); ink 54 read with key.tsv, gloss check PASS (N5-VIV54), window look-alike pass + re-decode, b2 + wrong-key PASS (N7-VIV54L); ink 53 Ink 52 f.164r-v read (VIV52-O, 13 Oct 2026): H 2,217 / M 404 / U 106 of 2,727, b2 + 200-wrong-key PASS.
ff.170r-171v read, b2 + wrong-key PASS (N6-VIV53B), window look-alike pass + ': :' join + re-decode, b2 + wrong-key PASS again (N7-VIV53L); ink 63 ff.190r-194r read in full (f.194r L5-10 added by N7-VIV63G): b2 PASS on every part (N6-VIV63, N6-VIV63B,
N6-VIV63C, N7-VIV63G), whole piece -1.548 vs p99 -1.836, wrong-key specificity PASS (real 0.288 vs p99 0.064), H 12,151 / M 2,329 / U 1,282 of 15,762 tokens. VIV-ANCHOR (8 Oct 2026): key.tsv V -> n (grade C, clerk word anchors) re-decodes all three inks: H 12,290 / M 2,369 / U 1,103 of 15,762 (63), 3,744 / 440 / 196 (53), 1,491 / 272 / 191 (54); b2 and 200-wrong-key gates PASS on each under new seeds.
Ink 67 f.201r checked against its decipherment 68 (ff.205r-205v) with Tomokiyo's key (VIV-67, 14 Oct 2026: 0.744 vs shuffled p95 0.507, rank 1 of 201; benchmark item vivonne1573-f201r-dev).
Pieces with no decipherment located: fr.16105 63, fr.16104 52, 53, 54 (and 38, whose twin is deciphered).
- ink 63 N4 (audit 1 done 4 Oct 2026 by VIV63-A1, AUDIT.md AUDIT 3: N3, D1 fragments read, key published; recipient the King; no decipherment in fr.16105 c95-c248) - blocker: not-attempted; d'Ars 1884 book (VIV-BREMOND) and d'Ars's RQH 35 (1884) article pp.386-412 (L51, DESK-LAND) both checked: neither cites 10 Oct 1573; Ribera 2007 seen as Google Books snippets only (L50: note 139 not visible); fr.16105 c1-c94 and the fr.16106 pieces Gachard skips not viewed; next: Ribera 2007 in full through the owner's interlibrary loan (ILL-SWEEP batch), reading note 139 and every 1573 Saint-Gouard citation, ~owner minutes + $0.5 to land
- Flament 1996 (L'ambassade du marquis de Saint-Gouard en Espagne, maîtrise Lille 3, 158 p.) - blocker: needs-physical-access; only copy located Lille, Bib. G. Lefebvre, cote D 1996 3, "Non disponible pour le PEB" (SUDOC 201366568, L52, 4 Oct 2026); no digitised copy
- tools/iiif_lines.py on steep, uneven line slopes - blocker: not-attempted; --follow-slope (and --centres with it) snapped bands onto neighbouring lines on f.194r; next: an option to deskew the region by a fitted angle before a flat cut (what N6-VIV63C did by hand with PIL), with an offline test, ~$2
- ink 63 key questions (y, single o, c, e, 2, r) - blocker: not-attempted; label e ruled by VIV-KEYV (14 Oct 2026, AUDIT 7): key row e -> m now grade M -- label e merges >= 3 signs, (A) e-loop + n compound = mm (ink-67 comm- anchors, 15 ink-63 "-omman-"), (B) hooked c before 6 (plus contexts), (C) Tomokiyo col f row 1 (faict/France contexts); next for e: split label e into three labels on the existing crops (tools/lookalike_pass.py with the three pile exemplars in tx/vivkeyv_tiles.tsv, or the owner's sign sorter), re-decode with (A)+n -> mm, (C) -> f, (B) -> p as candidates, each through the PREREG'd anchor + wrong-key gates, ~$3; V settled as an n homophone by VIV-ANCHOR (8 Oct 2026, 7 of 8 clerk-anchored ink-40 positions, control 5/7 PASS; key.tsv row V, grade C); context table (N7-VIV63G, tx/viv63g_keyctx.tsv): y->l and e as an "m(m)" sign remain weak proposals; in ink 40 the clerk anchors give 2 (u 2, m 1), o (p 2), c (p 1), e (0): none reaches 3 positions; ink 67 f.201r against its decipherment 68 (VIV-67, tx/viv67_labels_summary.tsv, counts only): c p 8 / e 5 of 18, single o p 5 of 16, 2 e 3 of 5, e m 4 of 5, y r 11 / l 9 (not h), S b 10 of 15, V n 7 of 13 -- c, o, e and S now reach 3+ aligned positions on one leaf, but no per-label gate has been run; next: a PREREG'd per-label anchor test on the ink 67 stream (tx/vivanchor.py's gates on tx/f201r_rec.tsv vs tx/dec67_norm.txt, wrong-key control), disk only, ~$2; then ink 67 f.201v-203r for more occurrences, ~$12
- ink 63 label splits and overlap duplication - blocker: not-attempted; r/z, 2/z (f.193v 25x), c/e and 6/b (f.192r, 19x) left at pass A; readers wrote some s1/s2 overlaps twice (f.192r L06, L34; f.193r L07); f.193r err_2reader 0.297; next: tools/lookalike_pass.py on those pairs + a pre-registered overlap-dedup step in tx/viv63_clean.py, re-decode, ~$4
- ink 53 D2 (depth re-check done 6 Oct 2026, D1-F16104I, AUDIT.md AUDIT 4: hold D1, H 85.2%) - blocker: not-attempted; three instruments on f, m, p now: whole-label key-cell n-gram rank (D1-F16104K, negative), hand-placed shape judge (D07-VIV53, NON-TEST), and clerk word anchors on ink 40 (VIV-ANCHOR, PREREG-VIVANCHOR: control PASS, but f, m, p each under 3 decided positions: m 4 split 3:2/2:1/z:1, p 3 split o:2/c:1; f 4 of 6 on label p, which the key reads n -- a CONFLICT, key unchanged: "affaires" is written p p twice, so readers' label p merges an f-sign); V -> n moved 16 ink-53 letters, longest H run 41 (unchanged, salad), V_strict top-1 20 (unchanged, null p99 24); next: the ink 50/51 known plaintext (fr.16104 ff.157-159v vs ff.162r-163r) for more f, m, p anchors, then split label p by shape at the anchored f positions, ~$15
- ink 53 residual label questions - blocker: not-attempted; the 270 one-reader gaps were window re-read under PREREG-R7VIV53G (decoy control PASS): 121 settled present, 16 removed, 133 still flagged; the 82 UNSETTLED split tiles, the ': :'-as-null alternative and "rauldhoit" (f.171r L15) remain; f.171v gap windows mostly unfindable (65 of 87 kept, the reader called 56 NONE but mostly at L) -- the window x-estimate drifts on that page; next: hand-placed per-tile crops (DEF1-VIV54's method) for the 82 splits + the 133 kept gaps, or the owner's sign sorter, ~$2.5
- ink 54 clean reading - blocker: not-attempted; window look-alike pass done (residual 0.134), true-error audit a non-test, no stretch near ~42 letters (N7-VIV54L); next: owner's sign sorter on tx/lookalike54/*_focus.tsv (275 questions) or a window-instrument audit (lookalike_pass.py audit + viv53L_windows.py audit), ~$1.5
- ink 54 key question "to z" (qae) - blocker: not-attempted; key cell added (key.tsv Zu -> u, N7-VIV54R); two machine shape judges NON-TEST (N7-VIV54R, DEF1-VIV54); clerk anchors on ink 40 (VIV-ANCHOR) give the u-after-q slot to z 2 and 2 2 of 4 positions: undecided (no share >= 2/3); next: the owner's sign sorter with Zu as a pile (tx/lookalike54/viv54H_xmarks.tsv), or the ink 50/51 known plaintext for more qu anchors, ~$1
- ink 54 D2 (depth re-check done 7 Oct 2026, DA1-VIV, hold D1, H 76.2%) - blocker: not-attempted; ink 40 clerk anchors (VIV-ANCHOR) fixed V -> n only (4 ink-54 letters moved, H 1,491 of 1,954, longest H run 26, unchanged); f, m, p and u-after-q stay under 3 positions; next: the ink 50/51 known plaintext (fr.16104 ff.157-159v against ff.162r-163r), then a PREREG'd key-change step with the wrong-key control, ~$15
- label p carries f in ink 40 (VIV-ANCHOR CONFLICT) - blocker: not-attempted; 4 of 6 clerk-anchored f slots hold label p (key n), at f102v L07:46-47 and L34:33-34 ("affaires" both times); the key has no f row; crops cut and a sorter page built (D4-VIV, 8 Oct 2026: tx/sorter_fp/, 4 focus tiles + 2 p-labelled refs + the readers' f sign, preflight PASS); next: the owner sorts tx/sorter_fp/sorter_viv_fp.html, then tools/sign_sorter_apply.py and a PREREG'd key-change step with the wrong-key control, ~$1
- Judge calibration for this hand - blocker: not-attempted; the fr16 judge FAILs the known-good f.103r control at this noise (N5-VIV54, N6-VIV53); next: score a lower-noise control (the clerk decipherment's own text, or f.103r after a lookalike pass) to see whether the judge can gate at all, ~$2
- fr.16104 ink 52 (5 Sept 1572, to the Queen, ff.164r-168v, ~290 lines) - blocker: not-attempted; premise negative in print (VIV52) and on the leaves (VIV52-O, 13 Oct 2026: c178-c183 viewed, no dechiffre or clear copy); f.164r-v transcribed and decoded (VIV52-O: H 2,217 / M 404 / U 106 of 2,727, b2 PASS -1.514 vs p99 -1.775, 200 wrong keys PASS margin 0.262 vs p99 0.026, longest H run 24, D1-like as 53/54/63); next: ff.165r-168v, 8 pages (f.168v 15 lines) x (2 blind Sonnet passes + 1 reconciliation) = 24 units at ~1.4 = ~$34, plus 4 native regions on openapi.bnf.fr, gates re-run with tx/viv52_test.py on the whole piece; then a first verifier (step 4)
- fr.16104 5 Sept 1572 cipher block (ff.157-159v) against its decipherment ff.162r-163r - blocker: not-attempted; known-plaintext check, not a reading; next: crops + two blind passes, aligned as tx/vivk_test.py, ~$15
- Unviewed stretches of the per-piece table - blocker: not-attempted; fr.16104 c1-c169, c192-c324 and fr.16105 c1-c94, c113-c191 not viewed (N5-VIVTAB); a decipherment of 63 filed in another volume (fr.16106 holds one such stray) not checked; next: 1200 px pass every second canvas, contact sheets, ~$3
- fr.16105 f.104r, first page of the decipherment - blocker: illegible; native crop shows word shapes only (N4-VIV3)
- Spanish-side copies (AGS Estado K) and Gachard vol. I - blocker: needs-physical-access; AGS is not digitised in a route this worker could open
- ink 52 print search on the decoded fragments (G3) - blocker: not-attempted; done by V-VIV52 (13 Oct 2026, print-check-52.tsv: generic hits only) except Google Books (HTTP 503 all session); next: rerun `tools/print_check.py ciphers/fr16104-vivonne-spain-1572 --phrases ciphers/fr16104-vivonne-spain-1572/phrases_52.txt --only gbooks` when the host answers, ~$0.3
- ink 52 La Ferriere f.191v lead (V-VIV52, AUDIT 5) - blocker: not-attempted; answered by VIV-191V (13 Oct 2026): f.191v (c208 left) is the clerk decipherment ("dechiffré de la precedente", ink 58, docket 19 Sept 1572) of the 19 Sept 1572 letter to the Queen whose cipher ends f.190r, and carries the Infante / "peau de l'ours" passage La Ferriere quotes; not ink 52 (no ink-52 phrase seen, other date, other leaves), so ink 52 gains no plaintext; next: only a side step, align the 19 Sept cipher (ff.188v-190r, first page on c204 or earlier) with ff.191r-192r as a known-plaintext pair, crops + two blind passes as tx/vivk_test.py, ~$15
- ink 67 rest (f.201v-203r) against ink 68 (ff.205v end-207) - blocker: not-attempted; f.201r only (VIV-67, 14 Oct 2026); the last 401 letters of dec67 (end of f.205v) lie past f.201r's aligned span; next: c206 left/c207-c208 and c211-c212 native regions on openapi.bnf.fr, 2 blind passes per page, the same build (benchmark item extended or a second dev item), ~$12 per two cipher pages
- image-side sign classifier for this hand - blocker: not-attempted; VIV-CLS (14 Oct 2026): a pen-unit tile kNN trained on f.102r + f.103r reads f.201r at 0.313 top-1 err vs passA 0.154 on the same 415 covered positions (gate FAIL), top-3 holds the truth for 0.359 of passA's covered errors (under 0.50), coverage 0.46 of scored positions (joined signs), permuted-label control 0.848 vs chance 0.908 (0.010 outside its band); next: a box-free window classifier (crop each reader token's own x-span, so coverage is not bounded by the segmenter), PREREG'd on the same three leaves with the same gate, ~$3
- vivonne1573-f201r-dev flags - blocker: not-attempted; align-conflict 163 and clerk-split 356 automatic flags, no verifier verdicts (confirm2 had TXV-VIV); f.205r decipherment read at word agreement 0.661; next: a TXV-VIV-style verifier pass on the 163 align-conflict positions, ~$3
- ink 70 f.211r against its decipherment 71 (ff.215r-215v) - blocker: not-attempted; VIV-70 (14 Oct 2026): registered gate FAIL, rank 2 of 201 (real 0.700, shuffled p95 0.661, max 0.701) because the whole-text target (2,614 letters for 519 codes) smeared the band-DP alignment; post-hoc trim to the opening (773 letters, ink 67 ratio) reads 0.769 vs p95 0.522, rank 1 (licenses nothing); passes, rec (err_2reader 0.154) and dec70 on disk; next: PREREG-VIV70B fixing the target trim rule before scoring (ink 67 ratio + 200), then the truth item vivonne1573-f211r-dev and tx/viv70_labels.py, disk only, ~$2; then f.211v ff. for more ink-70 cipher, ~$12 per two pages
- a person as reader of this hand (VIV-HUMAN known-answer test) - blocker: waiting-on the owner's answer on the VIV-HUMAN sorter page (14 Oct 2026); page https://claude.ai/artifact/WAPAiDSVDwYjvDotTgBFhA (23 tiles of f.201r, PREREG-VIVHUMAN.md + Addendum A: W 12, R 11); the parent scores with tx/vivhuman/score.py when saved; pass -> a person reads the disputed positions of ink 63 next, fail -> key-side and alignment work
## Escalation (14 Oct 2026, VIV-HUMAN refresh; from the VIV-KEYV list)
- [x] siblings: ink 38 located; ink 40 vs 41 aligned (N5-VIVK); ink 67 f.201r vs 68 aligned (VIV-67, PASS); ink 70 f.211r vs 71 (VIV-70, registered gate FAIL rank 2 of 201 on a smeared whole-text alignment, post-hoc trimmed 0.769 rank 1: re-register); decipherment 51 found (N5-VIV5S); per-piece table (N5-VIVTAB); ink 54 read (N5-VIV54); ink 53 ff.170r-171v read (N6-VIV53, N6-VIV53B); ink 63 ff.190r-194r read in full (N6-VIV63, N6-VIV63B, N6-VIV63C, N7-VIV63G); ink 52 f.164r-v read (VIV52-O)
- [x] clear-pages: decipherments 41, 44, 51, 68, 71, 76 are on the leaves; inks 54 and 53 interlinear words used as gloss checks (N5-VIV54 PASS, N6-VIV53 FAIL at the floor); f.171v has none (N6-VIV53B); ink 63 has none (order gate b2 instead)
- [x] known-keys: Tomokiyo's 1572-74 key on disk and held-out PASS (N5-VIVK); applied to inks 54, 53 and 63
- [x] print: Gachard I-II, d'Ars (book 1884 and RQH 35 article, L51), Catherine IV-V, Groen IV read; Ribera 2007 snippets (L50); d'Ars re-checked by date and by k-mer/phrase overlap against inks 53, 54, 63 (VIV-BREMOND); Kervyn I-VI grepped (N6-KERV); print_check on ink 54, 53 and 63 phrases (pc63b/, pc63c/); Gachard I-II, d'Ars, Catherine IV and X re-grepped for ink 52 (VIV52, none)
- [retired] key-rebuild: tools/stream_align.py from a flat start did not converge on this material (Arm A, 2 of 30 codes); a published key exists
- [x] image-check: fr.16104 c170-191 and fr.16105 c95-112, c192-248 viewed; native regions of f.173r-v, ff.170r-171v, ff.190r-194r (N5-VIV54, N6-VIV53, N6-VIV63, N6-VIV63B, N6-VIV63C, N7-VIV63G); ink 52 c178-c183 viewed at 1200 px and f.164r-v native regions via openapi.bnf.fr (VIV52-O, 13 Oct 2026): no dechiffre, no gloss; ink 52 misplaced-decipherment residual (V2-VIV52, AUDIT 6) closed 13 Oct 2026: dechiffre heads of inks 56, 60, 62 (VIV-DECH), 83, 89, 91 + 78 close (VIV-DECH2), 78, 97 (VIV-HEADS) and 101 (VIV-101, f.300r, c322, 24 Dec, King) viewed, each the decipherment of its own letter, none ink 52
- [ ] retry: ink 53 f/m/p key cells for the U labels (AUDIT 4; whole-label test negative, D1-F16104K; hand-placed per-position shape judge NON-TEST, control 4-5/12 vs 8/12, D07-VIV53; clerk word anchors on ink 40, VIV-ANCHOR 8 Oct 2026: control 5/7 PASS, V -> n assigned, f/m/p/qu under 3 positions, f on label p a conflict; next instrument: ink 50/51 known plaintext or sign sorter); ink 63 key questions on the key image (context table done, N7-VIV63G); ink 63 label questions (lookalike pass, overlap dedup); ink 53 residual unsettled tiles and kept gaps (window look-alike pass N7-VIV53L; gap re-read R7A-VIV53, 137/270 settled); ink 54 sorter/window audit (lookalike pass done, N7-VIV54L) and the col-u-row-3 relabel (key cell found, N7-VIV54Q; window judge NON-TEST, N7-VIV54R; hand-placed judge NON-TEST 0/18, DEF1-VIV54; next instrument: sign sorter / clerk alignment, hand-placed per-position crops); ink 63 noise: key-constrained lattice with a learnt confusion matrix (VIV-LAT, 14 Oct 2026: dev PASS, confirm2 FAIL, truth-in-lattice 0.124 -- next instrument: a reader that puts the true sign in the lattice); key rows from pooled clerk anchors ink 40 + 67 (VIV-KEY, 14 Oct 2026: e -> m added, gates PASS but non-discriminating; c/o under 2/3, 2 a CONFLICT; VIV-KEYV verifier 14 Oct 2026: e -> m downgraded to M, label e merges three signs; next: split label e by shape, more ink-67 anchors); image-side tile classifier (VIV-CLS, 14 Oct 2026: f.201r top-1 0.313 vs passA 0.154 on covered positions, top-3 0.359 of passA's errors, coverage 0.46: FAIL; next instrument: a box-free window classifier)
Verdict: keep going: 20 internal gaps and one waiting on the owner (VIV-HUMAN sorter page, 14 Oct 2026, https://claude.ai/artifact/WAPAiDSVDwYjvDotTgBFhA); VIV-KEYV (14 Oct 2026, AUDIT 7) key row e -> m downgraded C -> M (label e merges three signs: e-loop+n compound = mm, hooked c, Tomokiyo col f row 1; D1 held on 63/53/54/52; next for e: split the label by shape, ~$3); VIV-70 (14 Oct 2026) ink 70/71 pair registered gate FAIL (rank 2 of 201, whole-text target smeared the alignment; post-hoc trim 0.769 vs p95 0.522 rank 1, licenses nothing), next a PREREG-VIV70B with the trim rule fixed, ~$2; VIV-CLS (14 Oct 2026) image-side tile classifier trained on f.102r + f.103r FAILs on f.201r (0.313 vs passA 0.154 on covered positions, top-3 0.359 of passA's errors, coverage 0.46); VIV-KEY (14 Oct 2026) e -> m added to key.tsv from pooled clerk anchors (ink 63 U 1,103 -> 942, longest H run 40 unchanged; gates PASS but cannot discriminate one row; the crossword prefers e = i: verifier shape look next); VIV-67 (14 Oct 2026) second known-plaintext pair ink 67/68 PASS (0.744 vs p95 0.507), dev item vivonne1573-f201r-dev registered, c/o/e/S label counts reach 3+ on one leaf (no key edit); VIV-LAT (14 Oct 2026) lattice decode confirm2 FAIL at a 0.124 truth-in-lattice ceiling, ink 63 not re-decoded; ink 52 f.164r-v read at D1 (VIV52-O, 13 Oct 2026, b2 + wrong-key PASS; audit 1 N3 D1, V-VIV52; audit 2 N3 D1 upheld, V2-VIV52, misplaced-decipherment residual added; inks 56, 60, 62 dechiffre heads viewed by VIV-DECH and inks 83, 89, 91 (+78 close, a Dec body) by VIV-DECH2 and inks 78, 97 heads by VIV-HEADS, 13 Oct 2026: not ink 52; and ink 101 head by VIV-101 (f.300r, 24 Dec, King): not ink 52; residual closed); f.191v viewed (VIV-191V, 13 Oct 2026: decipherment of the 19 Sept letter, not ink 52); cheapest next: the owner sorts tx/sorter_fp/sorter_viv_fp.html (D4-VIV), ~$0 agent cost; then ink 52 ff.165r-168v via openapi.bnf.fr, ~$34 (24 units), and the ink 50/51 known plaintext for f, m, p, ~$15
## VIV-ESPLIT (14 Oct 2026, 01:46-02:1x UTC by date -u, account-4 worker for LANE VIV-KEYSTONE): split reader labels e and y by shape on the three truth leaves
Brief: .claude/briefs/runs/2026-10-13-acct4-keystone-viv-jobs.md "Wave 4", "VIV-ESPLIT". Measurement only: key.tsv, the ciphertext files, reading_piece63.tsv,
status.json and every committed reading untouched. PREREG-VIVESPLIT.md pushed a766d2881 (01:5x UTC) before any tile was classified; Addendum A 3351f861b
(the registered class rule admits six y classes; sixth control label p; feature cache for speed) before any accuracy was printed; Addendum B 5b9dac01c
written AFTER the step-1 look (per-class breakdown; no key edit; step 2 a measurement only).

Prior work (`tools/prior_work.py fr16104-vivonne-spain-1572 --item-spec 'fr.16105 reader labels e and y ... within-label sign split' --step-type key`, exit 4,
run after the one f.201r fetch and before any tile was classified): owed LEAD 1-own x2 = the VIV-KEY and VIV-KEYV claims (both have done lines; neither split a
label by shape: CLEAR); UNCHECKED 3-tomokiyo / 3-solver / 4-editions are generic and do not bear on a shape split of this hand's own reader labels.

**Data.** Items = every truth row on f.102r (dev2), f.103r (confirm2), f.201r (dev) whose reader label (`ref_sign`) is y or e and whose clerk letter (`plain`)
is set; class = that letter. Tiles: VIV-CLS's glyph_atlas segment atlas (regenerated, 1,655 / 1,835 / 1,139 tiles, identical counts) and its round-2
label-aware box maps (f.201r map built now against its truth skeleton, tx/vivesplit/f201r_map_r2_truthskel.tsv); per token T1 one 1:1 box / T2 union of its
boxes / T3 half of a box shared with a neighbour (instead of the brief's token-count window). Features HOG -> PCA 20 + glyph_atlas zone_topo (29), one LDA
(shrinkage auto), leave-one-leaf-out. tx/vivesplit/esplit.py, items.tsv, gate.json, pred_y.tsv.
**Label e: untestable on the truth leaves at this N.** 15 items (m 5, s 2, i 2, f 1, p 1, ...): no letter reaches the class rule (>= 8 pooled, >= 2 leaves),
so no classifier, no ink-63 split, no key row. VIV-KEYV's three shape groups stay the only evidence; 63 ink-63 e tokens on f.193v/f.193r/f.192v are listed
with next-label hints (17 before n = group A?, 4 before 6 = group B?) in tx/viv63_esplit/owner_questions.tsv for a later sorter ask.
**Label y, step 1 (registered gate): PASS as registered, but the per-class breakdown shows only l and h separate.**
| | n | held-out acc | baseline p0 (fold majority) | binomial p | permuted (200) mean / p95 | per leaf (f102r / f103r / f201r) |
|---|---|---|---|---|---|---|
| y, six classes l 46, r 19, h 13, e 9, n 8, u 8 | 103 (T1 28, T2 1, T3 74) | **0.408** (42) | 0.165 | < 1e-6 | 0.230 / 0.330 | 0.549 / 0.158 / 0.333 |
| G0 positive control (keyed labels m o d tz g p, same counts) | 103 | **0.748** (77) | 0.165 | < 1e-6 | 0.248 / 0.359 | 0.765 / 0.737 / 0.727 |
The registered p0 is weak: predicting l everywhere scores 0.447, above 0.408 (rule 3, the AX-NAMES shape: unbalanced classes). Per class, held-out precision vs
base rate (post-hoc): **l 28/43 = 0.651 vs 0.447 (p 0.006); h 6/13 = 0.462 vs 0.126 (p 0.003)**; u 3/7 vs 0.078 (p 0.013); r 4/21 vs 0.184 (p 0.56); e 1/15
(p 0.75); n 0/4. So label y holds at least an l-like and an h-like shape group that a classifier finds on a leaf it never saw (the control shows the tile
pipeline separates distinct keyed signs at 0.75 at the same N); r, e and n under label y are not separated by this instrument.
**Step 2, ink 63 (measurement, post-hoc; tx/vivesplit/step2.py, tx/viv63_esplit/):** 3 openapi.bnf.fr native regions (f.193v, f.193r, f.192v; crop boxes equal
images/p63/manifest.json's 72/74/72), glyph_atlas segment, width-only box map against viv63_decode's token sequence; 245 label-y tokens (T1 132, T2 11, T3 102),
model refit on all three leaves: top sub-label l 67, e 64, r 50, n 27, u 20, h 17; y_l (P(l) >= 0.6) 51. Gates on the three pages (5,609 letters):
| | score | b2 p99 | b2 | 200 wrong keys: real margin vs p99 |
|---|---|---|---|---|
| unsplit (y = h) | -1.5534 | -1.8125 | PASS | 0.2591 vs 0.0448 PASS |
| split (51 y_l = l) | -1.5289 | -1.7858 | PASS | 0.2569 vs 0.0512 PASS |
| 200 random splits of 51 y positions to l | mean -1.5285, p95 -1.5242 | | | real at rank 119 of 201 (118 random >= real) |
| every y read as l (descriptive) | -1.4307 | | | |
**The classifier's choice of which y tokens are l is no better than a random choice of the same count**: the score gain from the split is the gain of reading
any 51 y tokens as l rather than h. Both gates pass both versions (non-discriminating for one label, as VIV-KEY found for e). The crossword (`tools/decode_key.py
. --ciphertext <scratch> --key <scratch> --try ... --lm fr16`, non-blind, weak): on the 51 y_l tokens l beats h, r, e (-214 vs h -1340, r -569, e -488 bits) but
loses to i; on all 245 y tokens of the three pages every letter tried loses to reading y as a null, and h (the current key value) is the worst (-6,587 bits vs
l -1,210). Reading (descriptive, licenses nothing): Tomokiyo's y -> h fits only a minority shape group; most label-y tokens behave like l or like no letter.
Not done: no key edit, no ciphertext split, no re-decode of committed files; longest H run and judge unchanged by construction (y_l would be M). Requests:
openapi.bnf.fr 4 (HTTP 200: c206 f201r; c199 f193v; c198 f193r; c198 f192v), gallica 0. Subagent calls 0. No image committed (crops under images/p63/esplit
and images/p67, ignored). Cost not visible to this session.

## Remaining gaps (VIV-ESPLIT refresh, 14 Oct 2026; supersedes the VIV-HUMAN list, all its other lines kept)
Read so far: ink 40 checked against its decipherment 41 with Tomokiyo's key (N5-VIVK PASS); ink 54 read with key.tsv, gloss check PASS (N5-VIV54), window look-alike pass + re-decode, b2 + wrong-key PASS (N7-VIV54L); ink 53 Ink 52 f.164r-v read (VIV52-O, 13 Oct 2026): H 2,217 / M 404 / U 106 of 2,727, b2 + 200-wrong-key PASS.
ff.170r-171v read, b2 + wrong-key PASS (N6-VIV53B), window look-alike pass + ': :' join + re-decode, b2 + wrong-key PASS again (N7-VIV53L); ink 63 ff.190r-194r read in full (f.194r L5-10 added by N7-VIV63G): b2 PASS on every part (N6-VIV63, N6-VIV63B,
N6-VIV63C, N7-VIV63G), whole piece -1.548 vs p99 -1.836, wrong-key specificity PASS (real 0.288 vs p99 0.064), H 12,151 / M 2,329 / U 1,282 of 15,762 tokens. VIV-ANCHOR (8 Oct 2026): key.tsv V -> n (grade C, clerk word anchors) re-decodes all three inks: H 12,290 / M 2,369 / U 1,103 of 15,762 (63), 3,744 / 440 / 196 (53), 1,491 / 272 / 191 (54); b2 and 200-wrong-key gates PASS on each under new seeds.
Ink 67 f.201r checked against its decipherment 68 (ff.205r-205v) with Tomokiyo's key (VIV-67, 14 Oct 2026: 0.744 vs shuffled p95 0.507, rank 1 of 201; benchmark item vivonne1573-f201r-dev).
Pieces with no decipherment located: fr.16105 63, fr.16104 52, 53, 54 (and 38, whose twin is deciphered).
- ink 63 N4 (audit 1 done 4 Oct 2026 by VIV63-A1, AUDIT.md AUDIT 3: N3, D1 fragments read, key published; recipient the King; no decipherment in fr.16105 c95-c248) - blocker: not-attempted; d'Ars 1884 book (VIV-BREMOND) and d'Ars's RQH 35 (1884) article pp.386-412 (L51, DESK-LAND) both checked: neither cites 10 Oct 1573; Ribera 2007 seen as Google Books snippets only (L50: note 139 not visible); fr.16105 c1-c94 and the fr.16106 pieces Gachard skips not viewed; next: Ribera 2007 in full through the owner's interlibrary loan (ILL-SWEEP batch), reading note 139 and every 1573 Saint-Gouard citation, ~owner minutes + $0.5 to land
- Flament 1996 (L'ambassade du marquis de Saint-Gouard en Espagne, maîtrise Lille 3, 158 p.) - blocker: needs-physical-access; only copy located Lille, Bib. G. Lefebvre, cote D 1996 3, "Non disponible pour le PEB" (SUDOC 201366568, L52, 4 Oct 2026); no digitised copy
- tools/iiif_lines.py on steep, uneven line slopes - blocker: not-attempted; --follow-slope (and --centres with it) snapped bands onto neighbouring lines on f.194r; next: an option to deskew the region by a fitted angle before a flat cut (what N6-VIV63C did by hand with PIL), with an offline test, ~$2
- ink 63 key questions (y, single o, c, e, 2, r) - blocker: not-attempted; label e ruled by VIV-KEYV (14 Oct 2026, AUDIT 7): key row e -> m now grade M -- label e merges >= 3 signs, (A) e-loop + n compound = mm (ink-67 comm- anchors, 15 ink-63 "-omman-"), (B) hooked c before 6 (plus contexts), (C) Tomokiyo col f row 1 (faict/France contexts); VIV-ESPLIT (14 Oct 2026): a supervised split of e is untestable on the three truth leaves (15 items, no letter >= 8); next for e: split label e into three labels on the existing crops (tools/lookalike_pass.py with the three pile exemplars in tx/vivkeyv_tiles.tsv, or the owner's sign sorter), re-decode with (A)+n -> mm, (C) -> f, (B) -> p as candidates, each through the PREREG'd anchor + wrong-key gates, ~$3; V settled as an n homophone by VIV-ANCHOR (8 Oct 2026, 7 of 8 clerk-anchored ink-40 positions, control 5/7 PASS; key.tsv row V, grade C); context table (N7-VIV63G, tx/viv63g_keyctx.tsv): y->l and e as an "m(m)" sign remain weak proposals; in ink 40 the clerk anchors give 2 (u 2, m 1), o (p 2), c (p 1), e (0): none reaches 3 positions; ink 67 f.201r against its decipherment 68 (VIV-67, tx/viv67_labels_summary.tsv, counts only): c p 8 / e 5 of 18, single o p 5 of 16, 2 e 3 of 5, e m 4 of 5, y r 11 / l 9 (not h), S b 10 of 15, V n 7 of 13 -- c, o, e and S now reach 3+ aligned positions on one leaf, but no per-label gate has been run; next: a PREREG'd per-label anchor test on the ink 67 stream (tx/vivanchor.py's gates on tx/f201r_rec.tsv vs tx/dec67_norm.txt, wrong-key control), disk only, ~$2; then ink 67 f.201v-203r for more occurrences, ~$12
- ink 63 label splits and overlap duplication - blocker: not-attempted; r/z, 2/z (f.193v 25x), c/e and 6/b (f.192r, 19x) left at pass A; readers wrote some s1/s2 overlaps twice (f.192r L06, L34; f.193r L07); f.193r err_2reader 0.297; next: tools/lookalike_pass.py on those pairs + a pre-registered overlap-dedup step in tx/viv63_clean.py, re-decode, ~$4
- ink 53 D2 (depth re-check done 6 Oct 2026, D1-F16104I, AUDIT.md AUDIT 4: hold D1, H 85.2%) - blocker: not-attempted; three instruments on f, m, p now: whole-label key-cell n-gram rank (D1-F16104K, negative), hand-placed shape judge (D07-VIV53, NON-TEST), and clerk word anchors on ink 40 (VIV-ANCHOR, PREREG-VIVANCHOR: control PASS, but f, m, p each under 3 decided positions: m 4 split 3:2/2:1/z:1, p 3 split o:2/c:1; f 4 of 6 on label p, which the key reads n -- a CONFLICT, key unchanged: "affaires" is written p p twice, so readers' label p merges an f-sign); V -> n moved 16 ink-53 letters, longest H run 41 (unchanged, salad), V_strict top-1 20 (unchanged, null p99 24); next: the ink 50/51 known plaintext (fr.16104 ff.157-159v vs ff.162r-163r) for more f, m, p anchors, then split label p by shape at the anchored f positions, ~$15
- ink 53 residual label questions - blocker: not-attempted; the 270 one-reader gaps were window re-read under PREREG-R7VIV53G (decoy control PASS): 121 settled present, 16 removed, 133 still flagged; the 82 UNSETTLED split tiles, the ': :'-as-null alternative and "rauldhoit" (f.171r L15) remain; f.171v gap windows mostly unfindable (65 of 87 kept, the reader called 56 NONE but mostly at L) -- the window x-estimate drifts on that page; next: hand-placed per-tile crops (DEF1-VIV54's method) for the 82 splits + the 133 kept gaps, or the owner's sign sorter, ~$2.5
- ink 54 clean reading - blocker: not-attempted; window look-alike pass done (residual 0.134), true-error audit a non-test, no stretch near ~42 letters (N7-VIV54L); next: owner's sign sorter on tx/lookalike54/*_focus.tsv (275 questions) or a window-instrument audit (lookalike_pass.py audit + viv53L_windows.py audit), ~$1.5
- ink 54 key question "to z" (qae) - blocker: not-attempted; key cell added (key.tsv Zu -> u, N7-VIV54R); two machine shape judges NON-TEST (N7-VIV54R, DEF1-VIV54); clerk anchors on ink 40 (VIV-ANCHOR) give the u-after-q slot to z 2 and 2 2 of 4 positions: undecided (no share >= 2/3); next: the owner's sign sorter with Zu as a pile (tx/lookalike54/viv54H_xmarks.tsv), or the ink 50/51 known plaintext for more qu anchors, ~$1
- ink 54 D2 (depth re-check done 7 Oct 2026, DA1-VIV, hold D1, H 76.2%) - blocker: not-attempted; ink 40 clerk anchors (VIV-ANCHOR) fixed V -> n only (4 ink-54 letters moved, H 1,491 of 1,954, longest H run 26, unchanged); f, m, p and u-after-q stay under 3 positions; next: the ink 50/51 known plaintext (fr.16104 ff.157-159v against ff.162r-163r), then a PREREG'd key-change step with the wrong-key control, ~$15
- label p carries f in ink 40 (VIV-ANCHOR CONFLICT) - blocker: not-attempted; 4 of 6 clerk-anchored f slots hold label p (key n), at f102v L07:46-47 and L34:33-34 ("affaires" both times); the key has no f row; crops cut and a sorter page built (D4-VIV, 8 Oct 2026: tx/sorter_fp/, 4 focus tiles + 2 p-labelled refs + the readers' f sign, preflight PASS); next: the owner sorts tx/sorter_fp/sorter_viv_fp.html, then tools/sign_sorter_apply.py and a PREREG'd key-change step with the wrong-key control, ~$1
- Judge calibration for this hand - blocker: not-attempted; the fr16 judge FAILs the known-good f.103r control at this noise (N5-VIV54, N6-VIV53); next: score a lower-noise control (the clerk decipherment's own text, or f.103r after a lookalike pass) to see whether the judge can gate at all, ~$2
- fr.16104 ink 52 (5 Sept 1572, to the Queen, ff.164r-168v, ~290 lines) - blocker: not-attempted; premise negative in print (VIV52) and on the leaves (VIV52-O, 13 Oct 2026: c178-c183 viewed, no dechiffre or clear copy); f.164r-v transcribed and decoded (VIV52-O: H 2,217 / M 404 / U 106 of 2,727, b2 PASS -1.514 vs p99 -1.775, 200 wrong keys PASS margin 0.262 vs p99 0.026, longest H run 24, D1-like as 53/54/63); next: ff.165r-168v, 8 pages (f.168v 15 lines) x (2 blind Sonnet passes + 1 reconciliation) = 24 units at ~1.4 = ~$34, plus 4 native regions on openapi.bnf.fr, gates re-run with tx/viv52_test.py on the whole piece; then a first verifier (step 4)
- fr.16104 5 Sept 1572 cipher block (ff.157-159v) against its decipherment ff.162r-163r - blocker: not-attempted; known-plaintext check, not a reading; next: crops + two blind passes, aligned as tx/vivk_test.py, ~$15
- Unviewed stretches of the per-piece table - blocker: not-attempted; fr.16104 c1-c169, c192-c324 and fr.16105 c1-c94, c113-c191 not viewed (N5-VIVTAB); a decipherment of 63 filed in another volume (fr.16106 holds one such stray) not checked; next: 1200 px pass every second canvas, contact sheets, ~$3
- fr.16105 f.104r, first page of the decipherment - blocker: illegible; native crop shows word shapes only (N4-VIV3)
- Spanish-side copies (AGS Estado K) and Gachard vol. I - blocker: needs-physical-access; AGS is not digitised in a route this worker could open
- ink 52 print search on the decoded fragments (G3) - blocker: not-attempted; done by V-VIV52 (13 Oct 2026, print-check-52.tsv: generic hits only) except Google Books (HTTP 503 all session); next: rerun `tools/print_check.py ciphers/fr16104-vivonne-spain-1572 --phrases ciphers/fr16104-vivonne-spain-1572/phrases_52.txt --only gbooks` when the host answers, ~$0.3
- ink 52 La Ferriere f.191v lead (V-VIV52, AUDIT 5) - blocker: not-attempted; answered by VIV-191V (13 Oct 2026): f.191v (c208 left) is the clerk decipherment ("dechiffré de la precedente", ink 58, docket 19 Sept 1572) of the 19 Sept 1572 letter to the Queen whose cipher ends f.190r, and carries the Infante / "peau de l'ours" passage La Ferriere quotes; not ink 52 (no ink-52 phrase seen, other date, other leaves), so ink 52 gains no plaintext; next: only a side step, align the 19 Sept cipher (ff.188v-190r, first page on c204 or earlier) with ff.191r-192r as a known-plaintext pair, crops + two blind passes as tx/vivk_test.py, ~$15
- ink 67 rest (f.201v-203r) against ink 68 (ff.205v end-207) - blocker: not-attempted; f.201r only (VIV-67, 14 Oct 2026); the last 401 letters of dec67 (end of f.205v) lie past f.201r's aligned span; next: c206 left/c207-c208 and c211-c212 native regions on openapi.bnf.fr, 2 blind passes per page, the same build (benchmark item extended or a second dev item), ~$12 per two cipher pages
- image-side sign classifier for this hand - blocker: not-attempted; VIV-CLS (14 Oct 2026): a pen-unit tile kNN trained on f.102r + f.103r reads f.201r at 0.313 top-1 err vs passA 0.154 on the same 415 covered positions (gate FAIL), top-3 holds the truth for 0.359 of passA's covered errors (under 0.50), coverage 0.46 of scored positions (joined signs), permuted-label control 0.848 vs chance 0.908 (0.010 outside its band); next: a box-free window classifier (crop each reader token's own x-span, so coverage is not bounded by the segmenter), PREREG'd on the same three leaves with the same gate, ~$3
- vivonne1573-f201r-dev flags - blocker: not-attempted; align-conflict 163 and clerk-split 356 automatic flags, no verifier verdicts (confirm2 had TXV-VIV); f.205r decipherment read at word agreement 0.661; next: a TXV-VIV-style verifier pass on the 163 align-conflict positions, ~$3
- ink 70 f.211r against its decipherment 71 (ff.215r-215v) - blocker: not-attempted; VIV-70 (14 Oct 2026): registered gate FAIL, rank 2 of 201 (real 0.700, shuffled p95 0.661, max 0.701) because the whole-text target (2,614 letters for 519 codes) smeared the band-DP alignment; post-hoc trim to the opening (773 letters, ink 67 ratio) reads 0.769 vs p95 0.522, rank 1 (licenses nothing); passes, rec (err_2reader 0.154) and dec70 on disk; next: PREREG-VIV70B fixing the target trim rule before scoring (ink 67 ratio + 200), then the truth item vivonne1573-f211r-dev and tx/viv70_labels.py, disk only, ~$2; then f.211v ff. for more ink-70 cipher, ~$12 per two pages
- a person as reader of this hand (VIV-HUMAN known-answer test) - blocker: waiting-on the owner's answer on the VIV-HUMAN sorter page (14 Oct 2026); page https://claude.ai/artifact/WAPAiDSVDwYjvDotTgBFhA (23 tiles of f.201r, PREREG-VIVHUMAN.md + Addendum A: W 12, R 11); the parent scores with tx/vivhuman/score.py when saved; pass -> a person reads the disputed positions of ink 63 next, fail -> key-side and alignment work
- ink 63 label y split by shape (VIV-ESPLIT, 14 Oct 2026) - blocker: not-attempted; on the three truth leaves a six-class LDA separates an l-like and an h-like shape group held out (precision l 0.651 vs base 0.447, h 0.462 vs 0.126; blended 0.408 under the always-l 0.447; control 0.748), r/e/n not separated; on ink 63 f.193v/f.193r/f.192v the classifier's 51 y_l picks score no better than 51 random y -> l picks (rank 119 of 201), while every y read as l scores -1.431 vs -1.553 as h; next: a PREREG'd two-class (l vs h) gate on the truth leaves with a known-answer per-class threshold, then, only if it passes, a key-change job testing y = l with h kept for the classifier's h group, under the random-split control above (not b2/wrong-key, which cannot discriminate one label), ~$4
## Escalation (14 Oct 2026, VIV-ESPLIT refresh; from the VIV-HUMAN list)
- [x] siblings: ink 38 located; ink 40 vs 41 aligned (N5-VIVK); ink 67 f.201r vs 68 aligned (VIV-67, PASS); ink 70 f.211r vs 71 (VIV-70, registered gate FAIL rank 2 of 201 on a smeared whole-text alignment, post-hoc trimmed 0.769 rank 1: re-register); decipherment 51 found (N5-VIV5S); per-piece table (N5-VIVTAB); ink 54 read (N5-VIV54); ink 53 ff.170r-171v read (N6-VIV53, N6-VIV53B); ink 63 ff.190r-194r read in full (N6-VIV63, N6-VIV63B, N6-VIV63C, N7-VIV63G); ink 52 f.164r-v read (VIV52-O)
- [x] clear-pages: decipherments 41, 44, 51, 68, 71, 76 are on the leaves; inks 54 and 53 interlinear words used as gloss checks (N5-VIV54 PASS, N6-VIV53 FAIL at the floor); f.171v has none (N6-VIV53B); ink 63 has none (order gate b2 instead)
- [x] known-keys: Tomokiyo's 1572-74 key on disk and held-out PASS (N5-VIVK); applied to inks 54, 53 and 63
- [x] print: Gachard I-II, d'Ars (book 1884 and RQH 35 article, L51), Catherine IV-V, Groen IV read; Ribera 2007 snippets (L50); d'Ars re-checked by date and by k-mer/phrase overlap against inks 53, 54, 63 (VIV-BREMOND); Kervyn I-VI grepped (N6-KERV); print_check on ink 54, 53 and 63 phrases (pc63b/, pc63c/); Gachard I-II, d'Ars, Catherine IV and X re-grepped for ink 52 (VIV52, none)
- [retired] key-rebuild: tools/stream_align.py from a flat start did not converge on this material (Arm A, 2 of 30 codes); a published key exists
- [x] image-check: fr.16104 c170-191 and fr.16105 c95-112, c192-248 viewed; native regions of f.173r-v, ff.170r-171v, ff.190r-194r (N5-VIV54, N6-VIV53, N6-VIV63, N6-VIV63B, N6-VIV63C, N7-VIV63G); ink 52 c178-c183 viewed at 1200 px and f.164r-v native regions via openapi.bnf.fr (VIV52-O, 13 Oct 2026): no dechiffre, no gloss; ink 52 misplaced-decipherment residual (V2-VIV52, AUDIT 6) closed 13 Oct 2026: dechiffre heads of inks 56, 60, 62 (VIV-DECH), 83, 89, 91 + 78 close (VIV-DECH2), 78, 97 (VIV-HEADS) and 101 (VIV-101, f.300r, c322, 24 Dec, King) viewed, each the decipherment of its own letter, none ink 52
- [ ] retry: ink 53 f/m/p key cells for the U labels (AUDIT 4; whole-label test negative, D1-F16104K; hand-placed per-position shape judge NON-TEST, control 4-5/12 vs 8/12, D07-VIV53; clerk word anchors on ink 40, VIV-ANCHOR 8 Oct 2026: control 5/7 PASS, V -> n assigned, f/m/p/qu under 3 positions, f on label p a conflict; next instrument: ink 50/51 known plaintext or sign sorter); ink 63 key questions on the key image (context table done, N7-VIV63G); ink 63 label questions (lookalike pass, overlap dedup); ink 53 residual unsettled tiles and kept gaps (window look-alike pass N7-VIV53L; gap re-read R7A-VIV53, 137/270 settled); ink 54 sorter/window audit (lookalike pass done, N7-VIV54L) and the col-u-row-3 relabel (key cell found, N7-VIV54Q; window judge NON-TEST, N7-VIV54R; hand-placed judge NON-TEST 0/18, DEF1-VIV54; next instrument: sign sorter / clerk alignment, hand-placed per-position crops); ink 63 noise: key-constrained lattice with a learnt confusion matrix (VIV-LAT, 14 Oct 2026: dev PASS, confirm2 FAIL, truth-in-lattice 0.124 -- next instrument: a reader that puts the true sign in the lattice); key rows from pooled clerk anchors ink 40 + 67 (VIV-KEY, 14 Oct 2026: e -> m added, gates PASS but non-discriminating; c/o under 2/3, 2 a CONFLICT; VIV-KEYV verifier 14 Oct 2026: e -> m downgraded to M, label e merges three signs; next: split label e by shape, more ink-67 anchors); image-side tile classifier (VIV-CLS, 14 Oct 2026: f.201r top-1 0.313 vs passA 0.154 on covered positions, top-3 0.359 of passA's errors, coverage 0.46: FAIL; next instrument: a box-free window classifier)
Verdict: keep going: 21 internal gaps and one waiting on the owner (VIV-HUMAN sorter page, 14 Oct 2026, https://claude.ai/artifact/WAPAiDSVDwYjvDotTgBFhA); VIV-KEYV (14 Oct 2026, AUDIT 7) key row e -> m downgraded C -> M (label e merges three signs: e-loop+n compound = mm, hooked c, Tomokiyo col f row 1; D1 held on 63/53/54/52; next for e: split the label by shape, ~$3); VIV-70 (14 Oct 2026) ink 70/71 pair registered gate FAIL (rank 2 of 201, whole-text target smeared the alignment; post-hoc trim 0.769 vs p95 0.522 rank 1, licenses nothing), next a PREREG-VIV70B with the trim rule fixed, ~$2; VIV-CLS (14 Oct 2026) image-side tile classifier trained on f.102r + f.103r FAILs on f.201r (0.313 vs passA 0.154 on covered positions, top-3 0.359 of passA's errors, coverage 0.46); VIV-KEY (14 Oct 2026) e -> m added to key.tsv from pooled clerk anchors (ink 63 U 1,103 -> 942, longest H run 40 unchanged; gates PASS but cannot discriminate one row; the crossword prefers e = i: verifier shape look next); VIV-67 (14 Oct 2026) second known-plaintext pair ink 67/68 PASS (0.744 vs p95 0.507), dev item vivonne1573-f201r-dev registered, c/o/e/S label counts reach 3+ on one leaf (no key edit); VIV-LAT (14 Oct 2026) lattice decode confirm2 FAIL at a 0.124 truth-in-lattice ceiling, ink 63 not re-decoded; ink 52 f.164r-v read at D1 (VIV52-O, 13 Oct 2026, b2 + wrong-key PASS; audit 1 N3 D1, V-VIV52; audit 2 N3 D1 upheld, V2-VIV52, misplaced-decipherment residual added; inks 56, 60, 62 dechiffre heads viewed by VIV-DECH and inks 83, 89, 91 (+78 close, a Dec body) by VIV-DECH2 and inks 78, 97 heads by VIV-HEADS, 13 Oct 2026: not ink 52; and ink 101 head by VIV-101 (f.300r, 24 Dec, King): not ink 52; residual closed); f.191v viewed (VIV-191V, 13 Oct 2026: decipherment of the 19 Sept letter, not ink 52); cheapest next: the owner sorts tx/sorter_fp/sorter_viv_fp.html (D4-VIV), ~$0 agent cost; then ink 52 ff.165r-168v via openapi.bnf.fr, ~$34 (24 units), and the ink 50/51 known plaintext for f, m, p, ~$15; VIV-ESPLIT (14 Oct 2026): label y holds an l-like and an h-like shape group (held out, per class) but the classifier's ink-63 split is no better than random for the decode; every y as l beats y as h (-1.431 vs -1.553, descriptive); label e untestable on the truth leaves (15 items); no key edit; next a two-class l/h gate, ~$4
## VIV-70B (14 Oct 2026, 02:13-02:2x UTC by date -u, account-2 worker for LANE VIV-KEYSTONE, account 4): the ink-70 trim rule registered, f.211r truth item, label table
Brief: .claude/briefs/runs/2026-10-13-acct4-keystone-viv-jobs.md "Account-2 row VIV-70B" (= NOTES "VIV-70"'s "Next"). Disk only: no network request, no vision
call, no subagent. Measurement only: key.tsv, reading_piece63.tsv, status.json and every committed reading untouched.

Prior work (`tools/prior_work.py fr16104-vivonne-spain-1572 --item-spec 'fr.16105 f.211r ink 70 cipher vs ff.215r-215v ink 71 dechiffre, trim-rule re-run'
--step-type align`, exit 4): LEAD x2 = the VIV-KEY and VIV-KEYV target-level claims (both done; they cover the e -> m row, not this alignment) -- recorded CLEAR
with --record; UNCHECKED 3-tomokiyo / 3-solver / 4-editions as VIV-70 recorded them (Tomokiyo's page covers the key only; the plaintext of ink 70 is the clerk's
ink 71 by construction). No N-class (rule 10).

**PREREG-VIV70B.md** pushed in its own commit (877b5cdd3, checked on origin/main) before the re-run. Trim rule from ink 67 alone: ratio = dec67 aligned span /
f.201r codes = ((1901 - 200) - (98 + 200)) / 1,270 = 1,403 / 1,270 (tx/vivk67_result.json); target = first int(519 x 1403/1270) + 200 = 773 letters of dec70.
Disclosed in the PREREG: VIV-70 had already computed this exact figure post hoc (tx/vivk70_diag_trim.json), so this pass of the gate is a registration of the rule,
not a blind test of it; the rule's blind test is its next pair.

**Gate, run once** (`python3 benchmark-tx/build_vivonne_f211r.py --trim-ink67`, new option, default path unchanged; tx/vivk70b_result.json; seed 20261014):
| key | real match share | aligned keyed | 200 value-shuffled keys mean / p95 / max | rank | verdict |
|---|---|---|---|---|---|
| published (key_tomokiyo.tsv), gating | **0.769** | 437 | 0.458 / 0.522 / 0.572 | **1 of 201** | **PASS** (not blind, see above) |
| key.tsv full set (report only, 50 draws) | 0.762 | 446 | 0.463 / 0.513 / 0.545 | 1 of 51 | PASS |
Identical to VIV-70's post-hoc numbers, as it must be (same code, same seed). Window [0, 733] of the 773-letter target.

**Truth item registered:** benchmark-tx/vivonne1573-f211r-dev.truth.tsv (split=dev, BENCHMARK-TX.tsv row, sha256 4c1c5414...; `--trim-ink67 --check` ok): 534
positions, 398 scored (excluded: off-key 43, unaligned 36, letter-off-key 27, key-M-y 17, key-M-S 5, align-uncertain 4, key-M-e 3, key-M-b 1); flags on scored:
align-conflict 58, clerk-split 45, unflagged 306; no verifier flags file. Scores (tools/tx_bench.py, as measured / flagged-excluded): passA 0.138 / 0.006,
passB 0.166 / 0.036 (independent); committed 0.136 / 0.000 (circular: the truth was aligned to it, as confirm2's committed figure). err_2reader 0.154 (VIV-70).
Top confusion in every output, the committed included: truth s <- read d x16-17 (also f.103r's top confusion, x17) -- since the circular committed output carries
it too, it is a label-d-vs-clerk-s question on the key or truth side, not a reader slip (listed in Remaining gaps, not settled here).

**Label table** (`tx/viv70_labels.py`, VIV-70's script now on the trimmed alignment; `--check` ok): tx/viv70_labels.tsv (81 occurrences of 17 labels outside the
published key or M in key.tsv; 69 aligned, 68 at local confidence >= 0.5) and tx/viv70_labels_summary.tsv. Totals per label (aligned top letters): {curl} 24
(e 11, p 2, u 2, o 2); y 20 (l 12, h 3); S 7 (b 4); V 6 (n 2, e 2); o 5 (2 aligned: s 1, e 1); 8 3 (a 2); e 3 (m 2, r 1); c 3 (p 3); 9 2; t, (, 5, {omega}, i, Z,
",", b 1 each. Beside ink 67: c -> p and e -> m recur (3/3, 2/3); y leans l here (12 of 17) where ink 67 split r 11 / l 9; {curl} -> e 11 is not seen on ink 67
(7 occurrences, scattered). Counts only, no key edit, no per-label gate run.

Files: PREREG-VIV70B.md; benchmark-tx/build_vivonne_f211r.py (--trim-ink67); tx/vivk70b_result.json; benchmark-tx/vivonne1573-f211r-dev.truth.tsv + .sha256;
benchmark-tx/outputs/vivonne1573-f211r-dev/{committed,passA,passB}.tsv; BENCHMARK-TX.tsv row; tx/viv70_labels.py (trim) + tx/viv70_labels*.tsv; prior-work.tsv.
Requests: none (openapi.bnf.fr 0, gallica.bnf.fr 0). Subagent calls: 0. Cost not visible to this session.
Next (one line, not done): f.211v ff. against the rest of ink 71 under the same registered trim rule -- the rule's first blind use (~$12 per two cipher pages).

## Remaining gaps (VIV-70B refresh, 14 Oct 2026; supersedes the VIV-ESPLIT list, all its other lines kept)
Read so far: ink 40 checked against its decipherment 41 with Tomokiyo's key (N5-VIVK PASS); ink 54 read with key.tsv, gloss check PASS (N5-VIV54), window look-alike pass + re-decode, b2 + wrong-key PASS (N7-VIV54L); ink 53 Ink 52 f.164r-v read (VIV52-O, 13 Oct 2026): H 2,217 / M 404 / U 106 of 2,727, b2 + 200-wrong-key PASS.
ff.170r-171v read, b2 + wrong-key PASS (N6-VIV53B), window look-alike pass + ': :' join + re-decode, b2 + wrong-key PASS again (N7-VIV53L); ink 63 ff.190r-194r read in full (f.194r L5-10 added by N7-VIV63G): b2 PASS on every part (N6-VIV63, N6-VIV63B,
N6-VIV63C, N7-VIV63G), whole piece -1.548 vs p99 -1.836, wrong-key specificity PASS (real 0.288 vs p99 0.064), H 12,151 / M 2,329 / U 1,282 of 15,762 tokens. VIV-ANCHOR (8 Oct 2026): key.tsv V -> n (grade C, clerk word anchors) re-decodes all three inks: H 12,290 / M 2,369 / U 1,103 of 15,762 (63), 3,744 / 440 / 196 (53), 1,491 / 272 / 191 (54); b2 and 200-wrong-key gates PASS on each under new seeds.
Ink 67 f.201r checked against its decipherment 68 (ff.205r-205v) with Tomokiyo's key (VIV-67, 14 Oct 2026: 0.744 vs shuffled p95 0.507, rank 1 of 201; benchmark item vivonne1573-f201r-dev).
Ink 70 f.211r checked against its decipherment 71 (ff.215r-215v) with Tomokiyo's key under the trim rule of PREREG-VIV70B (VIV-70B, 14 Oct 2026: 0.769 vs shuffled p95 0.522, rank 1 of 201, not blind -- VIV-70 had computed it post hoc; benchmark item vivonne1573-f211r-dev).
Pieces with no decipherment located: fr.16105 63, fr.16104 52, 53, 54 (and 38, whose twin is deciphered).
- ink 63 N4 (audit 1 done 4 Oct 2026 by VIV63-A1, AUDIT.md AUDIT 3: N3, D1 fragments read, key published; recipient the King; no decipherment in fr.16105 c95-c248) - blocker: not-attempted; d'Ars 1884 book (VIV-BREMOND) and d'Ars's RQH 35 (1884) article pp.386-412 (L51, DESK-LAND) both checked: neither cites 10 Oct 1573; Ribera 2007 seen as Google Books snippets only (L50: note 139 not visible); fr.16105 c1-c94 and the fr.16106 pieces Gachard skips not viewed; next: Ribera 2007 in full through the owner's interlibrary loan (ILL-SWEEP batch), reading note 139 and every 1573 Saint-Gouard citation, ~owner minutes + $0.5 to land
- Flament 1996 (L'ambassade du marquis de Saint-Gouard en Espagne, maîtrise Lille 3, 158 p.) - blocker: needs-physical-access; only copy located Lille, Bib. G. Lefebvre, cote D 1996 3, "Non disponible pour le PEB" (SUDOC 201366568, L52, 4 Oct 2026); no digitised copy
- tools/iiif_lines.py on steep, uneven line slopes - blocker: not-attempted; --follow-slope (and --centres with it) snapped bands onto neighbouring lines on f.194r; next: an option to deskew the region by a fitted angle before a flat cut (what N6-VIV63C did by hand with PIL), with an offline test, ~$2
- ink 63 key questions (y, single o, c, e, 2, r) - blocker: not-attempted; label e ruled by VIV-KEYV (14 Oct 2026, AUDIT 7): key row e -> m now grade M -- label e merges >= 3 signs, (A) e-loop + n compound = mm (ink-67 comm- anchors, 15 ink-63 "-omman-"), (B) hooked c before 6 (plus contexts), (C) Tomokiyo col f row 1 (faict/France contexts); VIV-ESPLIT (14 Oct 2026): a supervised split of e is untestable on the three truth leaves (15 items, no letter >= 8); next for e: split label e into three labels on the existing crops (tools/lookalike_pass.py with the three pile exemplars in tx/vivkeyv_tiles.tsv, or the owner's sign sorter), re-decode with (A)+n -> mm, (C) -> f, (B) -> p as candidates, each through the PREREG'd anchor + wrong-key gates, ~$3; V settled as an n homophone by VIV-ANCHOR (8 Oct 2026, 7 of 8 clerk-anchored ink-40 positions, control 5/7 PASS; key.tsv row V, grade C); context table (N7-VIV63G, tx/viv63g_keyctx.tsv): y->l and e as an "m(m)" sign remain weak proposals; in ink 40 the clerk anchors give 2 (u 2, m 1), o (p 2), c (p 1), e (0): none reaches 3 positions; ink 67 f.201r against its decipherment 68 (VIV-67, tx/viv67_labels_summary.tsv, counts only): c p 8 / e 5 of 18, single o p 5 of 16, 2 e 3 of 5, e m 4 of 5, y r 11 / l 9 (not h), S b 10 of 15, V n 7 of 13 -- c, o, e and S now reach 3+ aligned positions on one leaf, but no per-label gate has been run; next: a PREREG'd per-label anchor test on the ink 67 stream (tx/vivanchor.py's gates on tx/f201r_rec.tsv vs tx/dec67_norm.txt, wrong-key control), disk only, ~$2; then ink 67 f.201v-203r for more occurrences, ~$12; ink 70 f.211r against decipherment 71 (VIV-70B, tx/viv70_labels_summary.tsv, counts only, trimmed alignment): {curl} e 11 of 21 aligned, y l 12 / h 3 of 17 (ink 67 had r 11 / l 9), S b 4 of 5, c p 3 of 3, e m 2 of 3, V n 2 / e 2 of 6, single o 2 aligned only; no per-label gate run
- ink 63 label splits and overlap duplication - blocker: not-attempted; r/z, 2/z (f.193v 25x), c/e and 6/b (f.192r, 19x) left at pass A; readers wrote some s1/s2 overlaps twice (f.192r L06, L34; f.193r L07); f.193r err_2reader 0.297; next: tools/lookalike_pass.py on those pairs + a pre-registered overlap-dedup step in tx/viv63_clean.py, re-decode, ~$4
- ink 53 D2 (depth re-check done 6 Oct 2026, D1-F16104I, AUDIT.md AUDIT 4: hold D1, H 85.2%) - blocker: not-attempted; three instruments on f, m, p now: whole-label key-cell n-gram rank (D1-F16104K, negative), hand-placed shape judge (D07-VIV53, NON-TEST), and clerk word anchors on ink 40 (VIV-ANCHOR, PREREG-VIVANCHOR: control PASS, but f, m, p each under 3 decided positions: m 4 split 3:2/2:1/z:1, p 3 split o:2/c:1; f 4 of 6 on label p, which the key reads n -- a CONFLICT, key unchanged: "affaires" is written p p twice, so readers' label p merges an f-sign); V -> n moved 16 ink-53 letters, longest H run 41 (unchanged, salad), V_strict top-1 20 (unchanged, null p99 24); next: the ink 50/51 known plaintext (fr.16104 ff.157-159v vs ff.162r-163r) for more f, m, p anchors, then split label p by shape at the anchored f positions, ~$15
- ink 53 residual label questions - blocker: not-attempted; the 270 one-reader gaps were window re-read under PREREG-R7VIV53G (decoy control PASS): 121 settled present, 16 removed, 133 still flagged; the 82 UNSETTLED split tiles, the ': :'-as-null alternative and "rauldhoit" (f.171r L15) remain; f.171v gap windows mostly unfindable (65 of 87 kept, the reader called 56 NONE but mostly at L) -- the window x-estimate drifts on that page; next: hand-placed per-tile crops (DEF1-VIV54's method) for the 82 splits + the 133 kept gaps, or the owner's sign sorter, ~$2.5
- ink 54 clean reading - blocker: not-attempted; window look-alike pass done (residual 0.134), true-error audit a non-test, no stretch near ~42 letters (N7-VIV54L); next: owner's sign sorter on tx/lookalike54/*_focus.tsv (275 questions) or a window-instrument audit (lookalike_pass.py audit + viv53L_windows.py audit), ~$1.5
- ink 54 key question "to z" (qae) - blocker: not-attempted; key cell added (key.tsv Zu -> u, N7-VIV54R); two machine shape judges NON-TEST (N7-VIV54R, DEF1-VIV54); clerk anchors on ink 40 (VIV-ANCHOR) give the u-after-q slot to z 2 and 2 2 of 4 positions: undecided (no share >= 2/3); next: the owner's sign sorter with Zu as a pile (tx/lookalike54/viv54H_xmarks.tsv), or the ink 50/51 known plaintext for more qu anchors, ~$1
- ink 54 D2 (depth re-check done 7 Oct 2026, DA1-VIV, hold D1, H 76.2%) - blocker: not-attempted; ink 40 clerk anchors (VIV-ANCHOR) fixed V -> n only (4 ink-54 letters moved, H 1,491 of 1,954, longest H run 26, unchanged); f, m, p and u-after-q stay under 3 positions; next: the ink 50/51 known plaintext (fr.16104 ff.157-159v against ff.162r-163r), then a PREREG'd key-change step with the wrong-key control, ~$15
- label p carries f in ink 40 (VIV-ANCHOR CONFLICT) - blocker: not-attempted; 4 of 6 clerk-anchored f slots hold label p (key n), at f102v L07:46-47 and L34:33-34 ("affaires" both times); the key has no f row; crops cut and a sorter page built (D4-VIV, 8 Oct 2026: tx/sorter_fp/, 4 focus tiles + 2 p-labelled refs + the readers' f sign, preflight PASS); next: the owner sorts tx/sorter_fp/sorter_viv_fp.html, then tools/sign_sorter_apply.py and a PREREG'd key-change step with the wrong-key control, ~$1
- Judge calibration for this hand - blocker: not-attempted; the fr16 judge FAILs the known-good f.103r control at this noise (N5-VIV54, N6-VIV53); next: score a lower-noise control (the clerk decipherment's own text, or f.103r after a lookalike pass) to see whether the judge can gate at all, ~$2
- fr.16104 ink 52 (5 Sept 1572, to the Queen, ff.164r-168v, ~290 lines) - blocker: not-attempted; premise negative in print (VIV52) and on the leaves (VIV52-O, 13 Oct 2026: c178-c183 viewed, no dechiffre or clear copy); f.164r-v transcribed and decoded (VIV52-O: H 2,217 / M 404 / U 106 of 2,727, b2 PASS -1.514 vs p99 -1.775, 200 wrong keys PASS margin 0.262 vs p99 0.026, longest H run 24, D1-like as 53/54/63); next: ff.165r-168v, 8 pages (f.168v 15 lines) x (2 blind Sonnet passes + 1 reconciliation) = 24 units at ~1.4 = ~$34, plus 4 native regions on openapi.bnf.fr, gates re-run with tx/viv52_test.py on the whole piece; then a first verifier (step 4)
- fr.16104 5 Sept 1572 cipher block (ff.157-159v) against its decipherment ff.162r-163r - blocker: not-attempted; known-plaintext check, not a reading; next: crops + two blind passes, aligned as tx/vivk_test.py, ~$15
- Unviewed stretches of the per-piece table - blocker: not-attempted; fr.16104 c1-c169, c192-c324 and fr.16105 c1-c94, c113-c191 not viewed (N5-VIVTAB); a decipherment of 63 filed in another volume (fr.16106 holds one such stray) not checked; next: 1200 px pass every second canvas, contact sheets, ~$3
- fr.16105 f.104r, first page of the decipherment - blocker: illegible; native crop shows word shapes only (N4-VIV3)
- Spanish-side copies (AGS Estado K) and Gachard vol. I - blocker: needs-physical-access; AGS is not digitised in a route this worker could open
- ink 52 print search on the decoded fragments (G3) - blocker: not-attempted; done by V-VIV52 (13 Oct 2026, print-check-52.tsv: generic hits only) except Google Books (HTTP 503 all session); next: rerun `tools/print_check.py ciphers/fr16104-vivonne-spain-1572 --phrases ciphers/fr16104-vivonne-spain-1572/phrases_52.txt --only gbooks` when the host answers, ~$0.3
- ink 52 La Ferriere f.191v lead (V-VIV52, AUDIT 5) - blocker: not-attempted; answered by VIV-191V (13 Oct 2026): f.191v (c208 left) is the clerk decipherment ("dechiffré de la precedente", ink 58, docket 19 Sept 1572) of the 19 Sept 1572 letter to the Queen whose cipher ends f.190r, and carries the Infante / "peau de l'ours" passage La Ferriere quotes; not ink 52 (no ink-52 phrase seen, other date, other leaves), so ink 52 gains no plaintext; next: only a side step, align the 19 Sept cipher (ff.188v-190r, first page on c204 or earlier) with ff.191r-192r as a known-plaintext pair, crops + two blind passes as tx/vivk_test.py, ~$15
- ink 67 rest (f.201v-203r) against ink 68 (ff.205v end-207) - blocker: not-attempted; f.201r only (VIV-67, 14 Oct 2026); the last 401 letters of dec67 (end of f.205v) lie past f.201r's aligned span; next: c206 left/c207-c208 and c211-c212 native regions on openapi.bnf.fr, 2 blind passes per page, the same build (benchmark item extended or a second dev item), ~$12 per two cipher pages
- image-side sign classifier for this hand - blocker: not-attempted; VIV-CLS (14 Oct 2026): a pen-unit tile kNN trained on f.102r + f.103r reads f.201r at 0.313 top-1 err vs passA 0.154 on the same 415 covered positions (gate FAIL), top-3 holds the truth for 0.359 of passA's covered errors (under 0.50), coverage 0.46 of scored positions (joined signs), permuted-label control 0.848 vs chance 0.908 (0.010 outside its band); next: a box-free window classifier (crop each reader token's own x-span, so coverage is not bounded by the segmenter), PREREG'd on the same three leaves with the same gate, ~$3
- vivonne1573-f201r-dev flags - blocker: not-attempted; align-conflict 163 and clerk-split 356 automatic flags, no verifier verdicts (confirm2 had TXV-VIV); f.205r decipherment read at word agreement 0.661; next: a TXV-VIV-style verifier pass on the 163 align-conflict positions, ~$3
- vivonne1573-f211r-dev flags - blocker: not-attempted; align-conflict 58 and clerk-split 45 automatic flags of 398 scored, no verifier verdicts; s<-d x16-17 is the top confusion in every output including the committed (circular) one, as on f.103r -- a key-side or truth-side question (label d against clerk s), not a reader error; next: a TXV-VIV-style verifier pass on the 58 align-conflict positions plus the s<-d positions of f.211r, f.201r and f.103r together, ~$3
- ink 70 rest (f.211v ff.) against ink 71 (f.215v end-217) - blocker: not-attempted; f.211r checked (VIV-70 registered FAIL on the whole-text target; VIV-70B, 14 Oct 2026, PREREG-VIV70B trim rule from ink 67 alone: 0.769 vs p95 0.522, rank 1 of 201, not blind since VIV-70 had computed the same figure post hoc; dev item vivonne1573-f211r-dev registered, 398 scored, passA 0.138 / 0.006, passB 0.166 / 0.036); the trim rule's blind test is its next pair; next: f.211v + f.212r native regions on openapi.bnf.fr, 2 blind passes per page, aligned under the same registered trim rule (offset by the letters f.211r used), ~$12 per two cipher pages
- a person as reader of this hand (VIV-HUMAN known-answer test) - blocker: waiting-on the owner's answer on the VIV-HUMAN sorter page (14 Oct 2026); page https://claude.ai/artifact/WAPAiDSVDwYjvDotTgBFhA (23 tiles of f.201r, PREREG-VIVHUMAN.md + Addendum A: W 12, R 11); the parent scores with tx/vivhuman/score.py when saved; pass -> a person reads the disputed positions of ink 63 next, fail -> key-side and alignment work
- ink 63 label y split by shape (VIV-ESPLIT, 14 Oct 2026) - blocker: not-attempted; on the three truth leaves a six-class LDA separates an l-like and an h-like shape group held out (precision l 0.651 vs base 0.447, h 0.462 vs 0.126; blended 0.408 under the always-l 0.447; control 0.748), r/e/n not separated; on ink 63 f.193v/f.193r/f.192v the classifier's 51 y_l picks score no better than 51 random y -> l picks (rank 119 of 201), while every y read as l scores -1.431 vs -1.553 as h; next: a PREREG'd two-class (l vs h) gate on the truth leaves with a known-answer per-class threshold, then, only if it passes, a key-change job testing y = l with h kept for the classifier's h group, under the random-split control above (not b2/wrong-key, which cannot discriminate one label), ~$4
## Escalation (14 Oct 2026, VIV-ESPLIT refresh; from the VIV-HUMAN list)
- [x] siblings: ink 38 located; ink 40 vs 41 aligned (N5-VIVK); ink 67 f.201r vs 68 aligned (VIV-67, PASS); ink 70 f.211r vs 71 (VIV-70, registered gate FAIL rank 2 of 201 on a smeared whole-text alignment, post-hoc trimmed 0.769 rank 1; VIV-70B re-registered the trim rule and re-ran once: PASS 0.769 vs p95 0.522, rank 1, not blind; dev item f211r registered); decipherment 51 found (N5-VIV5S); per-piece table (N5-VIVTAB); ink 54 read (N5-VIV54); ink 53 ff.170r-171v read (N6-VIV53, N6-VIV53B); ink 63 ff.190r-194r read in full (N6-VIV63, N6-VIV63B, N6-VIV63C, N7-VIV63G); ink 52 f.164r-v read (VIV52-O)
- [x] clear-pages: decipherments 41, 44, 51, 68, 71, 76 are on the leaves; inks 54 and 53 interlinear words used as gloss checks (N5-VIV54 PASS, N6-VIV53 FAIL at the floor); f.171v has none (N6-VIV53B); ink 63 has none (order gate b2 instead)
- [x] known-keys: Tomokiyo's 1572-74 key on disk and held-out PASS (N5-VIVK); applied to inks 54, 53 and 63
- [x] print: Gachard I-II, d'Ars (book 1884 and RQH 35 article, L51), Catherine IV-V, Groen IV read; Ribera 2007 snippets (L50); d'Ars re-checked by date and by k-mer/phrase overlap against inks 53, 54, 63 (VIV-BREMOND); Kervyn I-VI grepped (N6-KERV); print_check on ink 54, 53 and 63 phrases (pc63b/, pc63c/); Gachard I-II, d'Ars, Catherine IV and X re-grepped for ink 52 (VIV52, none)
- [retired] key-rebuild: tools/stream_align.py from a flat start did not converge on this material (Arm A, 2 of 30 codes); a published key exists
- [x] image-check: fr.16104 c170-191 and fr.16105 c95-112, c192-248 viewed; native regions of f.173r-v, ff.170r-171v, ff.190r-194r (N5-VIV54, N6-VIV53, N6-VIV63, N6-VIV63B, N6-VIV63C, N7-VIV63G); ink 52 c178-c183 viewed at 1200 px and f.164r-v native regions via openapi.bnf.fr (VIV52-O, 13 Oct 2026): no dechiffre, no gloss; ink 52 misplaced-decipherment residual (V2-VIV52, AUDIT 6) closed 13 Oct 2026: dechiffre heads of inks 56, 60, 62 (VIV-DECH), 83, 89, 91 + 78 close (VIV-DECH2), 78, 97 (VIV-HEADS) and 101 (VIV-101, f.300r, c322, 24 Dec, King) viewed, each the decipherment of its own letter, none ink 52
- [ ] retry: ink 53 f/m/p key cells for the U labels (AUDIT 4; whole-label test negative, D1-F16104K; hand-placed per-position shape judge NON-TEST, control 4-5/12 vs 8/12, D07-VIV53; clerk word anchors on ink 40, VIV-ANCHOR 8 Oct 2026: control 5/7 PASS, V -> n assigned, f/m/p/qu under 3 positions, f on label p a conflict; next instrument: ink 50/51 known plaintext or sign sorter); ink 63 key questions on the key image (context table done, N7-VIV63G); ink 63 label questions (lookalike pass, overlap dedup); ink 53 residual unsettled tiles and kept gaps (window look-alike pass N7-VIV53L; gap re-read R7A-VIV53, 137/270 settled); ink 54 sorter/window audit (lookalike pass done, N7-VIV54L) and the col-u-row-3 relabel (key cell found, N7-VIV54Q; window judge NON-TEST, N7-VIV54R; hand-placed judge NON-TEST 0/18, DEF1-VIV54; next instrument: sign sorter / clerk alignment, hand-placed per-position crops); ink 63 noise: key-constrained lattice with a learnt confusion matrix (VIV-LAT, 14 Oct 2026: dev PASS, confirm2 FAIL, truth-in-lattice 0.124 -- next instrument: a reader that puts the true sign in the lattice); key rows from pooled clerk anchors ink 40 + 67 (VIV-KEY, 14 Oct 2026: e -> m added, gates PASS but non-discriminating; c/o under 2/3, 2 a CONFLICT; VIV-KEYV verifier 14 Oct 2026: e -> m downgraded to M, label e merges three signs; next: split label e by shape, more ink-67 anchors); image-side tile classifier (VIV-CLS, 14 Oct 2026: f.201r top-1 0.313 vs passA 0.154 on covered positions, top-3 0.359 of passA's errors, coverage 0.46: FAIL; next instrument: a box-free window classifier)
Verdict: keep going: 22 internal gaps and one waiting on the owner (VIV-HUMAN sorter page, 14 Oct 2026, https://claude.ai/artifact/WAPAiDSVDwYjvDotTgBFhA); VIV-KEYV (14 Oct 2026, AUDIT 7) key row e -> m downgraded C -> M (label e merges three signs: e-loop+n compound = mm, hooked c, Tomokiyo col f row 1; D1 held on 63/53/54/52; next for e: split the label by shape, ~$3); VIV-70 (14 Oct 2026) ink 70/71 pair registered gate FAIL (rank 2 of 201, whole-text target smeared the alignment; post-hoc trim 0.769 vs p95 0.522 rank 1, licenses nothing), VIV-70B (14 Oct 2026) re-ran it once under a pre-registered ink-67 trim rule: PASS 0.769 vs p95 0.522, rank 1 (not blind), dev item vivonne1573-f211r-dev registered, label table tx/viv70_labels*.tsv (no key edit); next f.211v ff., ~$12; VIV-CLS (14 Oct 2026) image-side tile classifier trained on f.102r + f.103r FAILs on f.201r (0.313 vs passA 0.154 on covered positions, top-3 0.359 of passA's errors, coverage 0.46); VIV-KEY (14 Oct 2026) e -> m added to key.tsv from pooled clerk anchors (ink 63 U 1,103 -> 942, longest H run 40 unchanged; gates PASS but cannot discriminate one row; the crossword prefers e = i: verifier shape look next); VIV-67 (14 Oct 2026) second known-plaintext pair ink 67/68 PASS (0.744 vs p95 0.507), dev item vivonne1573-f201r-dev registered, c/o/e/S label counts reach 3+ on one leaf (no key edit); VIV-LAT (14 Oct 2026) lattice decode confirm2 FAIL at a 0.124 truth-in-lattice ceiling, ink 63 not re-decoded; ink 52 f.164r-v read at D1 (VIV52-O, 13 Oct 2026, b2 + wrong-key PASS; audit 1 N3 D1, V-VIV52; audit 2 N3 D1 upheld, V2-VIV52, misplaced-decipherment residual added; inks 56, 60, 62 dechiffre heads viewed by VIV-DECH and inks 83, 89, 91 (+78 close, a Dec body) by VIV-DECH2 and inks 78, 97 heads by VIV-HEADS, 13 Oct 2026: not ink 52; and ink 101 head by VIV-101 (f.300r, 24 Dec, King): not ink 52; residual closed); f.191v viewed (VIV-191V, 13 Oct 2026: decipherment of the 19 Sept letter, not ink 52); cheapest next: the owner sorts tx/sorter_fp/sorter_viv_fp.html (D4-VIV), ~$0 agent cost; then ink 52 ff.165r-168v via openapi.bnf.fr, ~$34 (24 units), and the ink 50/51 known plaintext for f, m, p, ~$15; VIV-ESPLIT (14 Oct 2026): label y holds an l-like and an h-like shape group (held out, per class) but the classifier's ink-63 split is no better than random for the decode; every y as l beats y as h (-1.431 vs -1.553, descriptive); label e untestable on the truth leaves (15 items); no key edit; next a two-class l/h gate, ~$4
## VIV-F191 (14 Oct 2026, 02:20-02:3x UTC by date -u, account-4 worker for LANE VIV-KEYSTONE): f.191r re-cut and four-pass re-read -- stopped at step 2
Brief: .claude/briefs/runs/2026-10-13-acct4-keystone-viv-jobs.md "Wave 5" VIV-F191. Measurement only: key.tsv, reading_piece63.tsv, status.json untouched.

Prior work (`tools/prior_work.py fr16104-vivonne-spain-1572 --item-spec 'fr.16105 f.191r ink 63 cipher page, re-cut ...' --step-type transcribe`,
exit 4): LEAD x2 = the VIV-KEY / VIV-KEYV target-level claims (both have done lines; key rows, not this page) -> CLEAR; UNCHECKED 3-tomokiyo (key only)
and 3-solver (N6-VIV63 / AUDIT 3 searched) -> CLEAR; LOOK 2-leaf -> CLEAR after the native region below (cipher only, no gloss or clear copy at 1600 px).
UNCHECKED-NET 3-solver clone and 4-editions left as AUDIT 3 records them. No N-class (rule 10).

**PREREG-VIVF191.md** pushed in its own commit (1b3ae6b82, checked on origin/main 02:24 UTC) before any pass.

**Step 1 done.** `tools/iiif_lines.py --deskew-region [DEG]` added (rotate the whole region by one read-free fitted angle -- row-profile sharpness over
-3..+3 deg -- then cut flat bands; manifest entries carry deskew_region {deg, centre, how}; exclusive with --deskew/--follow-slope/--check-boxes);
offline test tools/tests/test_iiif_deskew_region.py: 13/13 PASS (tilted synthetic page b=-0.025: fitted -1.45 vs true -1.43 deg, every rotated band end
within 2.3 px of the crop middle vs 30.5 px for the fixed-y cut; level page 0.00 deg; refusals); test_iiif_lines/slant/host/views still pass.
Crop command (openapi.bnf.fr 1 request, HTTP 200; crops in the scratchpad only, not committed; manifest images/p63/manifest_vivf191.json):
```
$ python3 tools/iiif_lines.py --ark btv1b9009663p --canvas 196 --iiif-host openapi --region 5020,540,2760,4400 --out <dir> --prefix c196_f191r_dr --deskew-region --distance 70 --max-width 1600 --overlap 150 --band-extent 0.1 --mask-neighbours --debug
  deskew-region: rotated -0.60 deg about the region centre (fitted (row-profile sharpness, read-free))
  region 2760x4400, 36 lines, 36 bands x 2 segments; pitch 112; wrote 72 crops
```
Debug overlay checked by eye: 36 red centres, one on each written line, level end to end; L20 s1 spot-checked (line centred, neighbour ink masked).

**Step 2 stopped.** Two blind Sonnet passes (C, D) launched on the 72 crops. Pass C read all 72 crops but its write of the pass file to the scratchpad was
blocked by the session's auto-mode classifier; per the common tail (one classifier denial: flag and stop, no variant of the action) it was told not to
write by another route, and pass D was stopped before it reached its write. No new pass exists, so no reconciliation, decode or statistic on new
passes was computed and PREREG-VIVF191's gates are unspent.
**Ready for the re-run:** tx/viv63_f191/f191.py implements PREREG sections 2-5 (clean, line-mapping check, four-pass vote with the RULES pairs, grades,
err_2reader per pair, longest H run, b2 + 200 wrong keys with C1/C2 controls, V_strict stretch vs 200 letter shuffles, owner_questions.tsv).
Implementation note: the shared tools/reconcile_passes.columns star alignment lists each pass's insertion relative to A as its own column; f191.py
pairs insertions after the same A sign across passes by their order within each pass before voting (otherwise a sign A lacks but C and D share would be
outvoted by its own split). Dry run with A, B copied in as C, D (a wiring check, not a result): err_2reader AB 0.156 (= N6-VIV63), AC/BD 0.000,
line mapping 36/36; before-page numbers on seed 20261014VIVF191: 1,785 tokens H 1,427 / M 234 / U 124, longest all-H run 32 (L11, = AUDIT 3),
b2 -1.454 vs p99 -1.815 PASS (controls C1 -1.695 vs -1.902, C2 -1.657 vs -1.832 pass), wrong keys margin 0.361 vs p99 0.058 PASS, V_strict top-1 17
(L10 "ung tres grande"), top-3 mean 16.0, null median 10 p99 15; no stretch near 42. Dry-run outputs deleted (they are not results).

Requests: openapi.bnf.fr 1 (HTTP 200), gallica.bnf.fr 0. Subagent calls: 2 Sonnet (pass C completed reading, unsaved; pass D stopped). Cost not visible to this session.

## VIV-HUMAN result (parent, account 4, 14 Oct 2026, 02:3x UTC by date -u): the owner's blind placements scored
The owner answered the page (https://claude.ai/artifact/WAPAiDSVDwYjvDotTgBFhA) at 02:28-02:31 UTC; db exported with ArtifactData
(tx/vivhuman/answers_2026-10-14/db/: 21 moves, 3 recuts, 2 checked, 2 newpiles), applied with `tools/sign_sorter_apply.py --labels
tx/sorter_human/labels.tsv --db <dir> --out settled.tsv --page tx/sorter_human/sorter_viv_human.html` (mode blind, 577 tiles, 21 moved,
3 recuts), scored with tx/vivhuman/score.py exactly as PREREG-VIVHUMAN.md fixed before the page was built (score.txt, per_tile.tsv).
- **W (reader-wrong, truth certain), n 12: 5 correct (0.417); 4 wrong; 2 "new sign"; 1 unanswered.** All four wrong placements are the
  same pair: the d-sign the readers label 3 placed in pile z (Q04, Q14, Q15, Q19; pass B wrote z at each, pass A 3). The two "new sign"
  calls are Q12 (truth L/g = r; both readers L or l) and Q23 (truth s/P/z = a; readers S/s). The unanswered W tile (Q25) and the
  unanswered R tile (Q24) are the two the owner recut: the page wrote them to `checked` with pile unsorted and never let him place
  them (his report, now sorter requirement R12 in tools/data/sorter_owner_requirements.tsv).
- **R (reader-right, truth certain), n 11: 10 correct (0.909); 1 unanswered (the recut tile).**
- **Verdict by the registered rule: undecided** (W 0.417 sits between 0.40 and 0.60; R 0.909 is at the 0.90 line only with the lost tile
  counted against it). Not threshold-shopped: with the two cut-lost tiles excluded post hoc, W would read 5/11 = 0.455 and R 10/10, still
  undecided -- reported here as a sensitivity note, not the verdict.
- What it changed: nothing in the key or any reading. What it says: where the machine readers fail on this hand, a person recovers
  about half; the half he misses is one look-alike pair (3 vs z, the d-sign), the same pair pass B and VIV-67's split table name first
  (3/z 15). That is a pile-exemplar question (do the 3 and z piles show the distinction?) before it is a reading question. A second
  owner ask on this hand, if any, targets that pair with its exemplars side by side, and only once R12 is fixed.
- Pile check (parent, 02:4x UTC, from the page's own embedded tiles): the "z" pile the page showed the owner is dominated by
  3-shaped glyphs (8 of 8 examples drawn from the committed f.201r labels are 3-like), while the "3" pile mixes 9-, m-, g- and
  Z-like shapes with 3-shapes. His four "wrong" placements therefore follow the page's own examples: the committed f.201r labels
  carry the 3/z confusion (VIV-67's first split pair, 15 columns), and a blind pile sort inherits it. The scoring stands as registered,
  but these four are a page defect (pile exemplars built from unsettled labels), not evidence about the owner's eye. The VIV-CLS map
  is too thin (46% coverage) to tally truth per label-z tile cleanly (label z: truth a 3, u 2, r 2, none d; label 3: a 2, d 1).

## Remaining gaps (VIV-F191 refresh, 14 Oct 2026; supersedes the VIV-70B list, all its other lines kept)
Read so far: ink 40 checked against its decipherment 41 with Tomokiyo's key (N5-VIVK PASS); ink 54 read with key.tsv, gloss check PASS (N5-VIV54), window look-alike pass + re-decode, b2 + wrong-key PASS (N7-VIV54L); ink 53 Ink 52 f.164r-v read (VIV52-O, 13 Oct 2026): H 2,217 / M 404 / U 106 of 2,727, b2 + 200-wrong-key PASS.
ff.170r-171v read, b2 + wrong-key PASS (N6-VIV53B), window look-alike pass + ': :' join + re-decode, b2 + wrong-key PASS again (N7-VIV53L); ink 63 ff.190r-194r read in full (f.194r L5-10 added by N7-VIV63G): b2 PASS on every part (N6-VIV63, N6-VIV63B,
N6-VIV63C, N7-VIV63G), whole piece -1.548 vs p99 -1.836, wrong-key specificity PASS (real 0.288 vs p99 0.064), H 12,151 / M 2,329 / U 1,282 of 15,762 tokens. VIV-ANCHOR (8 Oct 2026): key.tsv V -> n (grade C, clerk word anchors) re-decodes all three inks: H 12,290 / M 2,369 / U 1,103 of 15,762 (63), 3,744 / 440 / 196 (53), 1,491 / 272 / 191 (54); b2 and 200-wrong-key gates PASS on each under new seeds.
Ink 67 f.201r checked against its decipherment 68 (ff.205r-205v) with Tomokiyo's key (VIV-67, 14 Oct 2026: 0.744 vs shuffled p95 0.507, rank 1 of 201; benchmark item vivonne1573-f201r-dev).
Ink 70 f.211r checked against its decipherment 71 (ff.215r-215v) with Tomokiyo's key under the trim rule of PREREG-VIV70B (VIV-70B, 14 Oct 2026: 0.769 vs shuffled p95 0.522, rank 1 of 201, not blind -- VIV-70 had computed it post hoc; benchmark item vivonne1573-f211r-dev).
Pieces with no decipherment located: fr.16105 63, fr.16104 52, 53, 54 (and 38, whose twin is deciphered).
- ink 63 N4 (audit 1 done 4 Oct 2026 by VIV63-A1, AUDIT.md AUDIT 3: N3, D1 fragments read, key published; recipient the King; no decipherment in fr.16105 c95-c248) - blocker: not-attempted; d'Ars 1884 book (VIV-BREMOND) and d'Ars's RQH 35 (1884) article pp.386-412 (L51, DESK-LAND) both checked: neither cites 10 Oct 1573; Ribera 2007 seen as Google Books snippets only (L50: note 139 not visible); fr.16105 c1-c94 and the fr.16106 pieces Gachard skips not viewed; next: Ribera 2007 in full through the owner's interlibrary loan (ILL-SWEEP batch), reading note 139 and every 1573 Saint-Gouard citation, ~owner minutes + $0.5 to land
- Flament 1996 (L'ambassade du marquis de Saint-Gouard en Espagne, maîtrise Lille 3, 158 p.) - blocker: needs-physical-access; only copy located Lille, Bib. G. Lefebvre, cote D 1996 3, "Non disponible pour le PEB" (SUDOC 201366568, L52, 4 Oct 2026); no digitised copy
- tools/iiif_lines.py on steep, uneven line slopes - blocker: not-attempted; option built (VIV-F191, 14 Oct 2026: --deskew-region, read-free fitted angle, offline test tools/tests/test_iiif_deskew_region.py PASS; f.191r cut at -0.60 deg, 36 bands, overlay clean); next: use it on f.194r lines 5-10 (c199 region 4800,200,2950,2700) with --image on a re-fetched region, 2 blind passes, ~$3
- ink 63 key questions (y, single o, c, e, 2, r) - blocker: not-attempted; label e ruled by VIV-KEYV (14 Oct 2026, AUDIT 7): key row e -> m now grade M -- label e merges >= 3 signs, (A) e-loop + n compound = mm (ink-67 comm- anchors, 15 ink-63 "-omman-"), (B) hooked c before 6 (plus contexts), (C) Tomokiyo col f row 1 (faict/France contexts); VIV-ESPLIT (14 Oct 2026): a supervised split of e is untestable on the three truth leaves (15 items, no letter >= 8); next for e: split label e into three labels on the existing crops (tools/lookalike_pass.py with the three pile exemplars in tx/vivkeyv_tiles.tsv, or the owner's sign sorter), re-decode with (A)+n -> mm, (C) -> f, (B) -> p as candidates, each through the PREREG'd anchor + wrong-key gates, ~$3; V settled as an n homophone by VIV-ANCHOR (8 Oct 2026, 7 of 8 clerk-anchored ink-40 positions, control 5/7 PASS; key.tsv row V, grade C); context table (N7-VIV63G, tx/viv63g_keyctx.tsv): y->l and e as an "m(m)" sign remain weak proposals; in ink 40 the clerk anchors give 2 (u 2, m 1), o (p 2), c (p 1), e (0): none reaches 3 positions; ink 67 f.201r against its decipherment 68 (VIV-67, tx/viv67_labels_summary.tsv, counts only): c p 8 / e 5 of 18, single o p 5 of 16, 2 e 3 of 5, e m 4 of 5, y r 11 / l 9 (not h), S b 10 of 15, V n 7 of 13 -- c, o, e and S now reach 3+ aligned positions on one leaf, but no per-label gate has been run; next: a PREREG'd per-label anchor test on the ink 67 stream (tx/vivanchor.py's gates on tx/f201r_rec.tsv vs tx/dec67_norm.txt, wrong-key control), disk only, ~$2; then ink 67 f.201v-203r for more occurrences, ~$12; ink 70 f.211r against decipherment 71 (VIV-70B, tx/viv70_labels_summary.tsv, counts only, trimmed alignment): {curl} e 11 of 21 aligned, y l 12 / h 3 of 17 (ink 67 had r 11 / l 9), S b 4 of 5, c p 3 of 3, e m 2 of 3, V n 2 / e 2 of 6, single o 2 aligned only; no per-label gate run
- ink 63 label splits and overlap duplication - blocker: not-attempted; r/z, 2/z (f.193v 25x), c/e and 6/b (f.192r, 19x) left at pass A; readers wrote some s1/s2 overlaps twice (f.192r L06, L34; f.193r L07); f.193r err_2reader 0.297; next: tools/lookalike_pass.py on those pairs + a pre-registered overlap-dedup step in tx/viv63_clean.py, re-decode, ~$4
- ink 53 D2 (depth re-check done 6 Oct 2026, D1-F16104I, AUDIT.md AUDIT 4: hold D1, H 85.2%) - blocker: not-attempted; three instruments on f, m, p now: whole-label key-cell n-gram rank (D1-F16104K, negative), hand-placed shape judge (D07-VIV53, NON-TEST), and clerk word anchors on ink 40 (VIV-ANCHOR, PREREG-VIVANCHOR: control PASS, but f, m, p each under 3 decided positions: m 4 split 3:2/2:1/z:1, p 3 split o:2/c:1; f 4 of 6 on label p, which the key reads n -- a CONFLICT, key unchanged: "affaires" is written p p twice, so readers' label p merges an f-sign); V -> n moved 16 ink-53 letters, longest H run 41 (unchanged, salad), V_strict top-1 20 (unchanged, null p99 24); next: the ink 50/51 known plaintext (fr.16104 ff.157-159v vs ff.162r-163r) for more f, m, p anchors, then split label p by shape at the anchored f positions, ~$15
- ink 53 residual label questions - blocker: not-attempted; the 270 one-reader gaps were window re-read under PREREG-R7VIV53G (decoy control PASS): 121 settled present, 16 removed, 133 still flagged; the 82 UNSETTLED split tiles, the ': :'-as-null alternative and "rauldhoit" (f.171r L15) remain; f.171v gap windows mostly unfindable (65 of 87 kept, the reader called 56 NONE but mostly at L) -- the window x-estimate drifts on that page; next: hand-placed per-tile crops (DEF1-VIV54's method) for the 82 splits + the 133 kept gaps, or the owner's sign sorter, ~$2.5
- ink 54 clean reading - blocker: not-attempted; window look-alike pass done (residual 0.134), true-error audit a non-test, no stretch near ~42 letters (N7-VIV54L); next: owner's sign sorter on tx/lookalike54/*_focus.tsv (275 questions) or a window-instrument audit (lookalike_pass.py audit + viv53L_windows.py audit), ~$1.5
- ink 54 key question "to z" (qae) - blocker: not-attempted; key cell added (key.tsv Zu -> u, N7-VIV54R); two machine shape judges NON-TEST (N7-VIV54R, DEF1-VIV54); clerk anchors on ink 40 (VIV-ANCHOR) give the u-after-q slot to z 2 and 2 2 of 4 positions: undecided (no share >= 2/3); next: the owner's sign sorter with Zu as a pile (tx/lookalike54/viv54H_xmarks.tsv), or the ink 50/51 known plaintext for more qu anchors, ~$1
- ink 54 D2 (depth re-check done 7 Oct 2026, DA1-VIV, hold D1, H 76.2%) - blocker: not-attempted; ink 40 clerk anchors (VIV-ANCHOR) fixed V -> n only (4 ink-54 letters moved, H 1,491 of 1,954, longest H run 26, unchanged); f, m, p and u-after-q stay under 3 positions; next: the ink 50/51 known plaintext (fr.16104 ff.157-159v against ff.162r-163r), then a PREREG'd key-change step with the wrong-key control, ~$15
- label p carries f in ink 40 (VIV-ANCHOR CONFLICT) - blocker: not-attempted; 4 of 6 clerk-anchored f slots hold label p (key n), at f102v L07:46-47 and L34:33-34 ("affaires" both times); the key has no f row; crops cut and a sorter page built (D4-VIV, 8 Oct 2026: tx/sorter_fp/, 4 focus tiles + 2 p-labelled refs + the readers' f sign, preflight PASS); next: the owner sorts tx/sorter_fp/sorter_viv_fp.html, then tools/sign_sorter_apply.py and a PREREG'd key-change step with the wrong-key control, ~$1
- Judge calibration for this hand - blocker: not-attempted; the fr16 judge FAILs the known-good f.103r control at this noise (N5-VIV54, N6-VIV53); next: score a lower-noise control (the clerk decipherment's own text, or f.103r after a lookalike pass) to see whether the judge can gate at all, ~$2
- fr.16104 ink 52 (5 Sept 1572, to the Queen, ff.164r-168v, ~290 lines) - blocker: not-attempted; premise negative in print (VIV52) and on the leaves (VIV52-O, 13 Oct 2026: c178-c183 viewed, no dechiffre or clear copy); f.164r-v transcribed and decoded (VIV52-O: H 2,217 / M 404 / U 106 of 2,727, b2 PASS -1.514 vs p99 -1.775, 200 wrong keys PASS margin 0.262 vs p99 0.026, longest H run 24, D1-like as 53/54/63); next: ff.165r-168v, 8 pages (f.168v 15 lines) x (2 blind Sonnet passes + 1 reconciliation) = 24 units at ~1.4 = ~$34, plus 4 native regions on openapi.bnf.fr, gates re-run with tx/viv52_test.py on the whole piece; then a first verifier (step 4)
- fr.16104 5 Sept 1572 cipher block (ff.157-159v) against its decipherment ff.162r-163r - blocker: not-attempted; known-plaintext check, not a reading; next: crops + two blind passes, aligned as tx/vivk_test.py, ~$15
- Unviewed stretches of the per-piece table - blocker: not-attempted; fr.16104 c1-c169, c192-c324 and fr.16105 c1-c94, c113-c191 not viewed (N5-VIVTAB); a decipherment of 63 filed in another volume (fr.16106 holds one such stray) not checked; next: 1200 px pass every second canvas, contact sheets, ~$3
- fr.16105 f.104r, first page of the decipherment - blocker: illegible; native crop shows word shapes only (N4-VIV3)
- Spanish-side copies (AGS Estado K) and Gachard vol. I - blocker: needs-physical-access; AGS is not digitised in a route this worker could open
- ink 52 print search on the decoded fragments (G3) - blocker: not-attempted; done by V-VIV52 (13 Oct 2026, print-check-52.tsv: generic hits only) except Google Books (HTTP 503 all session); next: rerun `tools/print_check.py ciphers/fr16104-vivonne-spain-1572 --phrases ciphers/fr16104-vivonne-spain-1572/phrases_52.txt --only gbooks` when the host answers, ~$0.3
- ink 52 La Ferriere f.191v lead (V-VIV52, AUDIT 5) - blocker: not-attempted; answered by VIV-191V (13 Oct 2026): f.191v (c208 left) is the clerk decipherment ("dechiffré de la precedente", ink 58, docket 19 Sept 1572) of the 19 Sept 1572 letter to the Queen whose cipher ends f.190r, and carries the Infante / "peau de l'ours" passage La Ferriere quotes; not ink 52 (no ink-52 phrase seen, other date, other leaves), so ink 52 gains no plaintext; next: only a side step, align the 19 Sept cipher (ff.188v-190r, first page on c204 or earlier) with ff.191r-192r as a known-plaintext pair, crops + two blind passes as tx/vivk_test.py, ~$15
- ink 67 rest (f.201v-203r) against ink 68 (ff.205v end-207) - blocker: not-attempted; f.201r only (VIV-67, 14 Oct 2026); the last 401 letters of dec67 (end of f.205v) lie past f.201r's aligned span; next: c206 left/c207-c208 and c211-c212 native regions on openapi.bnf.fr, 2 blind passes per page, the same build (benchmark item extended or a second dev item), ~$12 per two cipher pages
- image-side sign classifier for this hand - blocker: not-attempted; VIV-CLS (14 Oct 2026): a pen-unit tile kNN trained on f.102r + f.103r reads f.201r at 0.313 top-1 err vs passA 0.154 on the same 415 covered positions (gate FAIL), top-3 holds the truth for 0.359 of passA's covered errors (under 0.50), coverage 0.46 of scored positions (joined signs), permuted-label control 0.848 vs chance 0.908 (0.010 outside its band); next: a box-free window classifier (crop each reader token's own x-span, so coverage is not bounded by the segmenter), PREREG'd on the same three leaves with the same gate, ~$3
- vivonne1573-f201r-dev flags - blocker: not-attempted; align-conflict 163 and clerk-split 356 automatic flags, no verifier verdicts (confirm2 had TXV-VIV); f.205r decipherment read at word agreement 0.661; next: a TXV-VIV-style verifier pass on the 163 align-conflict positions, ~$3
- vivonne1573-f211r-dev flags - blocker: not-attempted; align-conflict 58 and clerk-split 45 automatic flags of 398 scored, no verifier verdicts; s<-d x16-17 is the top confusion in every output including the committed (circular) one, as on f.103r -- a key-side or truth-side question (label d against clerk s), not a reader error; next: a TXV-VIV-style verifier pass on the 58 align-conflict positions plus the s<-d positions of f.211r, f.201r and f.103r together, ~$3
- ink 70 rest (f.211v ff.) against ink 71 (f.215v end-217) - blocker: not-attempted; f.211r checked (VIV-70 registered FAIL on the whole-text target; VIV-70B, 14 Oct 2026, PREREG-VIV70B trim rule from ink 67 alone: 0.769 vs p95 0.522, rank 1 of 201, not blind since VIV-70 had computed the same figure post hoc; dev item vivonne1573-f211r-dev registered, 398 scored, passA 0.138 / 0.006, passB 0.166 / 0.036); the trim rule's blind test is its next pair; next: f.211v + f.212r native regions on openapi.bnf.fr, 2 blind passes per page, aligned under the same registered trim rule (offset by the letters f.211r used), ~$12 per two cipher pages
- a person as reader of this hand (VIV-HUMAN known-answer test) - blocker: waiting-on the owner's answer on the VIV-HUMAN sorter page (14 Oct 2026); page https://claude.ai/artifact/WAPAiDSVDwYjvDotTgBFhA (23 tiles of f.201r, PREREG-VIVHUMAN.md + Addendum A: W 12, R 11); the parent scores with tx/vivhuman/score.py when saved; pass -> a person reads the disputed positions of ink 63 next, fail -> key-side and alignment work
- ink 63 label y split by shape (VIV-ESPLIT, 14 Oct 2026) - blocker: not-attempted; on the three truth leaves a six-class LDA separates an l-like and an h-like shape group held out (precision l 0.651 vs base 0.447, h 0.462 vs 0.126; blended 0.408 under the always-l 0.447; control 0.748), r/e/n not separated; on ink 63 f.193v/f.193r/f.192v the classifier's 51 y_l picks score no better than 51 random y -> l picks (rank 119 of 201), while every y read as l scores -1.431 vs -1.553 as h; next: a PREREG'd two-class (l vs h) gate on the truth leaves with a known-answer per-class threshold, then, only if it passes, a key-change job testing y = l with h kept for the classifier's h group, under the random-split control above (not b2/wrong-key, which cannot discriminate one label), ~$4
- ink 63 f.191r four-pass re-read (VIV-F191, PREREG-VIVF191.md) - blocker: not-attempted; crops re-cut (--deskew-region -0.60 deg, 36 bands, scratch only; manifest images/p63/manifest_vivf191.json, re-fetch command in NOTES "VIV-F191") and tx/viv63_f191/f191.py written and dry-run on a self-copy (A,B as C,D: err_2reader AC/BD 0.000, before-page numbers reproduce: longest H run 32, b2 PASS -1.454 vs p99 -1.815, wrong keys PASS 0.361 vs p99 0.058, V_strict top-1 17 vs null p99 15); stopped because the auto-mode classifier blocked the fresh blind pass's file write (pass C read all 72 crops, could not save); next: re-run the two blind Sonnet passes in a session whose permission mode lets a subagent write its pass file to the scratchpad (or have the reader return the TSV text in its final message and the worker save it, which needs no subagent file write), then `python3 tx/viv63_f191/f191.py --stats`, ~$4
## Escalation (14 Oct 2026, VIV-F191 refresh; from the VIV-70B list)
- [x] siblings: ink 38 located; ink 40 vs 41 aligned (N5-VIVK); ink 67 f.201r vs 68 aligned (VIV-67, PASS); ink 70 f.211r vs 71 (VIV-70, registered gate FAIL rank 2 of 201 on a smeared whole-text alignment, post-hoc trimmed 0.769 rank 1; VIV-70B re-registered the trim rule and re-ran once: PASS 0.769 vs p95 0.522, rank 1, not blind; dev item f211r registered); decipherment 51 found (N5-VIV5S); per-piece table (N5-VIVTAB); ink 54 read (N5-VIV54); ink 53 ff.170r-171v read (N6-VIV53, N6-VIV53B); ink 63 ff.190r-194r read in full (N6-VIV63, N6-VIV63B, N6-VIV63C, N7-VIV63G); ink 52 f.164r-v read (VIV52-O)
- [x] clear-pages: decipherments 41, 44, 51, 68, 71, 76 are on the leaves; inks 54 and 53 interlinear words used as gloss checks (N5-VIV54 PASS, N6-VIV53 FAIL at the floor); f.171v has none (N6-VIV53B); ink 63 has none (order gate b2 instead)
- [x] known-keys: Tomokiyo's 1572-74 key on disk and held-out PASS (N5-VIVK); applied to inks 54, 53 and 63
- [x] print: Gachard I-II, d'Ars (book 1884 and RQH 35 article, L51), Catherine IV-V, Groen IV read; Ribera 2007 snippets (L50); d'Ars re-checked by date and by k-mer/phrase overlap against inks 53, 54, 63 (VIV-BREMOND); Kervyn I-VI grepped (N6-KERV); print_check on ink 54, 53 and 63 phrases (pc63b/, pc63c/); Gachard I-II, d'Ars, Catherine IV and X re-grepped for ink 52 (VIV52, none)
- [retired] key-rebuild: tools/stream_align.py from a flat start did not converge on this material (Arm A, 2 of 30 codes); a published key exists
- [x] image-check: fr.16104 c170-191 and fr.16105 c95-112, c192-248 viewed; native regions of f.173r-v, ff.170r-171v, ff.190r-194r (N5-VIV54, N6-VIV53, N6-VIV63, N6-VIV63B, N6-VIV63C, N7-VIV63G); ink 52 c178-c183 viewed at 1200 px and f.164r-v native regions via openapi.bnf.fr (VIV52-O, 13 Oct 2026): no dechiffre, no gloss; ink 52 misplaced-decipherment residual (V2-VIV52, AUDIT 6) closed 13 Oct 2026: dechiffre heads of inks 56, 60, 62 (VIV-DECH), 83, 89, 91 + 78 close (VIV-DECH2), 78, 97 (VIV-HEADS) and 101 (VIV-101, f.300r, c322, 24 Dec, King) viewed, each the decipherment of its own letter, none ink 52
- [ ] retry: ink 53 f/m/p key cells for the U labels (AUDIT 4; whole-label test negative, D1-F16104K; hand-placed per-position shape judge NON-TEST, control 4-5/12 vs 8/12, D07-VIV53; clerk word anchors on ink 40, VIV-ANCHOR 8 Oct 2026: control 5/7 PASS, V -> n assigned, f/m/p/qu under 3 positions, f on label p a conflict; next instrument: ink 50/51 known plaintext or sign sorter); ink 63 key questions on the key image (context table done, N7-VIV63G); ink 63 label questions (lookalike pass, overlap dedup); ink 53 residual unsettled tiles and kept gaps (window look-alike pass N7-VIV53L; gap re-read R7A-VIV53, 137/270 settled); ink 54 sorter/window audit (lookalike pass done, N7-VIV54L) and the col-u-row-3 relabel (key cell found, N7-VIV54Q; window judge NON-TEST, N7-VIV54R; hand-placed judge NON-TEST 0/18, DEF1-VIV54; next instrument: sign sorter / clerk alignment, hand-placed per-position crops); ink 63 noise: key-constrained lattice with a learnt confusion matrix (VIV-LAT, 14 Oct 2026: dev PASS, confirm2 FAIL, truth-in-lattice 0.124 -- next instrument: a reader that puts the true sign in the lattice); key rows from pooled clerk anchors ink 40 + 67 (VIV-KEY, 14 Oct 2026: e -> m added, gates PASS but non-discriminating; c/o under 2/3, 2 a CONFLICT; VIV-KEYV verifier 14 Oct 2026: e -> m downgraded to M, label e merges three signs; next: split label e by shape, more ink-67 anchors); image-side tile classifier (VIV-CLS, 14 Oct 2026: f.201r top-1 0.313 vs passA 0.154 on covered positions, top-3 0.359 of passA's errors, coverage 0.46: FAIL; next instrument: a box-free window classifier)
Verdict: keep going: 23 internal gaps; cheapest next: the f.191r four-pass re-read (VIV-F191 stopped before any new pass when the classifier blocked the reader's file write; crops recipe and tx/viv63_f191/f191.py ready), ~$4; earlier: 22 internal gaps and one waiting on the owner (VIV-HUMAN sorter page, 14 Oct 2026, https://claude.ai/artifact/WAPAiDSVDwYjvDotTgBFhA); VIV-KEYV (14 Oct 2026, AUDIT 7) key row e -> m downgraded C -> M (label e merges three signs: e-loop+n compound = mm, hooked c, Tomokiyo col f row 1; D1 held on 63/53/54/52; next for e: split the label by shape, ~$3); VIV-70 (14 Oct 2026) ink 70/71 pair registered gate FAIL (rank 2 of 201, whole-text target smeared the alignment; post-hoc trim 0.769 vs p95 0.522 rank 1, licenses nothing), VIV-70B (14 Oct 2026) re-ran it once under a pre-registered ink-67 trim rule: PASS 0.769 vs p95 0.522, rank 1 (not blind), dev item vivonne1573-f211r-dev registered, label table tx/viv70_labels*.tsv (no key edit); next f.211v ff., ~$12; VIV-CLS (14 Oct 2026) image-side tile classifier trained on f.102r + f.103r FAILs on f.201r (0.313 vs passA 0.154 on covered positions, top-3 0.359 of passA's errors, coverage 0.46); VIV-KEY (14 Oct 2026) e -> m added to key.tsv from pooled clerk anchors (ink 63 U 1,103 -> 942, longest H run 40 unchanged; gates PASS but cannot discriminate one row; the crossword prefers e = i: verifier shape look next); VIV-67 (14 Oct 2026) second known-plaintext pair ink 67/68 PASS (0.744 vs p95 0.507), dev item vivonne1573-f201r-dev registered, c/o/e/S label counts reach 3+ on one leaf (no key edit); VIV-LAT (14 Oct 2026) lattice decode confirm2 FAIL at a 0.124 truth-in-lattice ceiling, ink 63 not re-decoded; ink 52 f.164r-v read at D1 (VIV52-O, 13 Oct 2026, b2 + wrong-key PASS; audit 1 N3 D1, V-VIV52; audit 2 N3 D1 upheld, V2-VIV52, misplaced-decipherment residual added; inks 56, 60, 62 dechiffre heads viewed by VIV-DECH and inks 83, 89, 91 (+78 close, a Dec body) by VIV-DECH2 and inks 78, 97 heads by VIV-HEADS, 13 Oct 2026: not ink 52; and ink 101 head by VIV-101 (f.300r, 24 Dec, King): not ink 52; residual closed); f.191v viewed (VIV-191V, 13 Oct 2026: decipherment of the 19 Sept letter, not ink 52); cheapest next: the owner sorts tx/sorter_fp/sorter_viv_fp.html (D4-VIV), ~$0 agent cost; then ink 52 ff.165r-168v via openapi.bnf.fr, ~$34 (24 units), and the ink 50/51 known plaintext for f, m, p, ~$15; VIV-ESPLIT (14 Oct 2026): label y holds an l-like and an h-like shape group (held out, per class) but the classifier's ink-63 split is no better than random for the decode; every y as l beats y as h (-1.431 vs -1.553, descriptive); label e untestable on the truth leaves (15 items); no key edit; next a two-class l/h gate, ~$4
## VIV-HUMAN2 (14 Oct 2026, 02:41-02:4x UTC by date -u, account-4 worker for LANE VIV-KEYSTONE): the owner's second try -- stopped before building
Brief: .claude/briefs/runs/2026-10-13-acct4-keystone-viv-jobs.md "VIV-HUMAN2". PREREG-VIVHUMAN.md Addendum B pushed b3d056715 (02:42 UTC) before any build. Prior work (`tools/prior_work.py ... --item-spec 'fr.16105 f.201r ink 67 tiles: blind sorter packet attempt 2 for a person (VIV-HUMAN2)' --step-type transcribe`, exit 4): LEAD 1-own x3 (VIV-KEY, VIV-KEYV claims and this job's own: none covers this packet; CLEAR), LOOK 2-leaf (f.201r viewed by VIV-67/VIV-CLS, no gloss; CLEAR), UNCHECKED 3-tomokiyo/3-solver, UNCHECKED-NET 3-solver/4-editions (a page build, not a reading; not run).
Crops re-fetched with the manifest "vivcls" commands (openapi.bnf.fr 1 request, HTTP 200, take/release lines; gallica.bnf.fr 0; untracked). `tx/vivhuman/build_inputs.py` gained `--attempt 2` (questions = Q04 Q14 Q15 Q19 Q12 Q23 Q24 Q25 shuffled seed 20261014; the other 15 attempt-1 questions back in their committed piles; the Addendum B filter on 3 z L l s S h k; output tx/sorter_human2/ with filter.tsv). Attempt 1 rebuilds byte-identically (git status clean on tx/sorter_human after a re-run).
**Result: not built.** filter.tsv: 3 8 -> 0, z 18 -> 1, S 7 -> 0, k 2 -> 0, L 4 -> 1, h 5 -> 3, s 40 -> 22, l 0 -> 0; every removal a flagged (clerk-split, align-conflict) or unscored (off-key, unaligned) row, none a label outside its truth set. The 7 scored unflagged 3-rows (all d) are the four question tiles plus three with no 1:1 tile, so no pile 3 can be shown and the page cannot ask its question. A scratch contact sheet of the 56 3/z/h/k/question tiles with their truth rows: the surviving z (truth a, scored) and the three clerk-split z (truth a) are 3-shaped like Q04/Q14/Q15/Q19 (truth d), so on this hand the key's z (= a) and 3 (= d) signs look alike; the attempt-1 z pile was not only mislabelled d-signs. Possibly the d-sign has a rounder top and the a-sign a flatter one (an eye impression, untested). Nothing scored; no key, reading or status.json change.
Options for the parent (not taken; the registered rule is not loosened by a worker): (a) pile 3 from d-sign tiles on the f.102r/f.103r truth leaves at scored unflagged d rows (other ink, same hand); (b) admit clerk-split f.201r rows whose label is in the truth set (adds 3 tiles labelled 3, one a bad cut); (c) side-by-side 3 vs z exemplar card as the parent's VIV-HUMAN result suggested. Each needs an Addendum C before a rebuild (~$2).
Requests: openapi.bnf.fr 1; subagent calls 0. Cost not visible to this session.

## Remaining gaps (VIV-HUMAN2 refresh, 14 Oct 2026; supersedes the VIV-F191 list, all its other lines kept)
Read so far: ink 40 checked against its decipherment 41 with Tomokiyo's key (N5-VIVK PASS); ink 54 read with key.tsv, gloss check PASS (N5-VIV54), window look-alike pass + re-decode, b2 + wrong-key PASS (N7-VIV54L); ink 53 Ink 52 f.164r-v read (VIV52-O, 13 Oct 2026): H 2,217 / M 404 / U 106 of 2,727, b2 + 200-wrong-key PASS.
ff.170r-171v read, b2 + wrong-key PASS (N6-VIV53B), window look-alike pass + ': :' join + re-decode, b2 + wrong-key PASS again (N7-VIV53L); ink 63 ff.190r-194r read in full (f.194r L5-10 added by N7-VIV63G): b2 PASS on every part (N6-VIV63, N6-VIV63B,
N6-VIV63C, N7-VIV63G), whole piece -1.548 vs p99 -1.836, wrong-key specificity PASS (real 0.288 vs p99 0.064), H 12,151 / M 2,329 / U 1,282 of 15,762 tokens. VIV-ANCHOR (8 Oct 2026): key.tsv V -> n (grade C, clerk word anchors) re-decodes all three inks: H 12,290 / M 2,369 / U 1,103 of 15,762 (63), 3,744 / 440 / 196 (53), 1,491 / 272 / 191 (54); b2 and 200-wrong-key gates PASS on each under new seeds.
Ink 67 f.201r checked against its decipherment 68 (ff.205r-205v) with Tomokiyo's key (VIV-67, 14 Oct 2026: 0.744 vs shuffled p95 0.507, rank 1 of 201; benchmark item vivonne1573-f201r-dev).
Ink 70 f.211r checked against its decipherment 71 (ff.215r-215v) with Tomokiyo's key under the trim rule of PREREG-VIV70B (VIV-70B, 14 Oct 2026: 0.769 vs shuffled p95 0.522, rank 1 of 201, not blind -- VIV-70 had computed it post hoc; benchmark item vivonne1573-f211r-dev).
Pieces with no decipherment located: fr.16105 63, fr.16104 52, 53, 54 (and 38, whose twin is deciphered).
- ink 63 N4 (audit 1 done 4 Oct 2026 by VIV63-A1, AUDIT.md AUDIT 3: N3, D1 fragments read, key published; recipient the King; no decipherment in fr.16105 c95-c248) - blocker: not-attempted; d'Ars 1884 book (VIV-BREMOND) and d'Ars's RQH 35 (1884) article pp.386-412 (L51, DESK-LAND) both checked: neither cites 10 Oct 1573; Ribera 2007 seen as Google Books snippets only (L50: note 139 not visible); fr.16105 c1-c94 and the fr.16106 pieces Gachard skips not viewed; next: Ribera 2007 in full through the owner's interlibrary loan (ILL-SWEEP batch), reading note 139 and every 1573 Saint-Gouard citation, ~owner minutes + $0.5 to land
- Flament 1996 (L'ambassade du marquis de Saint-Gouard en Espagne, maîtrise Lille 3, 158 p.) - blocker: needs-physical-access; only copy located Lille, Bib. G. Lefebvre, cote D 1996 3, "Non disponible pour le PEB" (SUDOC 201366568, L52, 4 Oct 2026); no digitised copy
- tools/iiif_lines.py on steep, uneven line slopes - blocker: not-attempted; option built (VIV-F191, 14 Oct 2026: --deskew-region, read-free fitted angle, offline test tools/tests/test_iiif_deskew_region.py PASS; f.191r cut at -0.60 deg, 36 bands, overlay clean); next: use it on f.194r lines 5-10 (c199 region 4800,200,2950,2700) with --image on a re-fetched region, 2 blind passes, ~$3
- ink 63 key questions (y, single o, c, e, 2, r) - blocker: not-attempted; label e ruled by VIV-KEYV (14 Oct 2026, AUDIT 7): key row e -> m now grade M -- label e merges >= 3 signs, (A) e-loop + n compound = mm (ink-67 comm- anchors, 15 ink-63 "-omman-"), (B) hooked c before 6 (plus contexts), (C) Tomokiyo col f row 1 (faict/France contexts); VIV-ESPLIT (14 Oct 2026): a supervised split of e is untestable on the three truth leaves (15 items, no letter >= 8); next for e: split label e into three labels on the existing crops (tools/lookalike_pass.py with the three pile exemplars in tx/vivkeyv_tiles.tsv, or the owner's sign sorter), re-decode with (A)+n -> mm, (C) -> f, (B) -> p as candidates, each through the PREREG'd anchor + wrong-key gates, ~$3; V settled as an n homophone by VIV-ANCHOR (8 Oct 2026, 7 of 8 clerk-anchored ink-40 positions, control 5/7 PASS; key.tsv row V, grade C); context table (N7-VIV63G, tx/viv63g_keyctx.tsv): y->l and e as an "m(m)" sign remain weak proposals; in ink 40 the clerk anchors give 2 (u 2, m 1), o (p 2), c (p 1), e (0): none reaches 3 positions; ink 67 f.201r against its decipherment 68 (VIV-67, tx/viv67_labels_summary.tsv, counts only): c p 8 / e 5 of 18, single o p 5 of 16, 2 e 3 of 5, e m 4 of 5, y r 11 / l 9 (not h), S b 10 of 15, V n 7 of 13 -- c, o, e and S now reach 3+ aligned positions on one leaf, but no per-label gate has been run; next: a PREREG'd per-label anchor test on the ink 67 stream (tx/vivanchor.py's gates on tx/f201r_rec.tsv vs tx/dec67_norm.txt, wrong-key control), disk only, ~$2; then ink 67 f.201v-203r for more occurrences, ~$12; ink 70 f.211r against decipherment 71 (VIV-70B, tx/viv70_labels_summary.tsv, counts only, trimmed alignment): {curl} e 11 of 21 aligned, y l 12 / h 3 of 17 (ink 67 had r 11 / l 9), S b 4 of 5, c p 3 of 3, e m 2 of 3, V n 2 / e 2 of 6, single o 2 aligned only; no per-label gate run
- ink 63 label splits and overlap duplication - blocker: not-attempted; r/z, 2/z (f.193v 25x), c/e and 6/b (f.192r, 19x) left at pass A; readers wrote some s1/s2 overlaps twice (f.192r L06, L34; f.193r L07); f.193r err_2reader 0.297; next: tools/lookalike_pass.py on those pairs + a pre-registered overlap-dedup step in tx/viv63_clean.py, re-decode, ~$4
- ink 53 D2 (depth re-check done 6 Oct 2026, D1-F16104I, AUDIT.md AUDIT 4: hold D1, H 85.2%) - blocker: not-attempted; three instruments on f, m, p now: whole-label key-cell n-gram rank (D1-F16104K, negative), hand-placed shape judge (D07-VIV53, NON-TEST), and clerk word anchors on ink 40 (VIV-ANCHOR, PREREG-VIVANCHOR: control PASS, but f, m, p each under 3 decided positions: m 4 split 3:2/2:1/z:1, p 3 split o:2/c:1; f 4 of 6 on label p, which the key reads n -- a CONFLICT, key unchanged: "affaires" is written p p twice, so readers' label p merges an f-sign); V -> n moved 16 ink-53 letters, longest H run 41 (unchanged, salad), V_strict top-1 20 (unchanged, null p99 24); next: the ink 50/51 known plaintext (fr.16104 ff.157-159v vs ff.162r-163r) for more f, m, p anchors, then split label p by shape at the anchored f positions, ~$15
- ink 53 residual label questions - blocker: not-attempted; the 270 one-reader gaps were window re-read under PREREG-R7VIV53G (decoy control PASS): 121 settled present, 16 removed, 133 still flagged; the 82 UNSETTLED split tiles, the ': :'-as-null alternative and "rauldhoit" (f.171r L15) remain; f.171v gap windows mostly unfindable (65 of 87 kept, the reader called 56 NONE but mostly at L) -- the window x-estimate drifts on that page; next: hand-placed per-tile crops (DEF1-VIV54's method) for the 82 splits + the 133 kept gaps, or the owner's sign sorter, ~$2.5
- ink 54 clean reading - blocker: not-attempted; window look-alike pass done (residual 0.134), true-error audit a non-test, no stretch near ~42 letters (N7-VIV54L); next: owner's sign sorter on tx/lookalike54/*_focus.tsv (275 questions) or a window-instrument audit (lookalike_pass.py audit + viv53L_windows.py audit), ~$1.5
- ink 54 key question "to z" (qae) - blocker: not-attempted; key cell added (key.tsv Zu -> u, N7-VIV54R); two machine shape judges NON-TEST (N7-VIV54R, DEF1-VIV54); clerk anchors on ink 40 (VIV-ANCHOR) give the u-after-q slot to z 2 and 2 2 of 4 positions: undecided (no share >= 2/3); next: the owner's sign sorter with Zu as a pile (tx/lookalike54/viv54H_xmarks.tsv), or the ink 50/51 known plaintext for more qu anchors, ~$1
- ink 54 D2 (depth re-check done 7 Oct 2026, DA1-VIV, hold D1, H 76.2%) - blocker: not-attempted; ink 40 clerk anchors (VIV-ANCHOR) fixed V -> n only (4 ink-54 letters moved, H 1,491 of 1,954, longest H run 26, unchanged); f, m, p and u-after-q stay under 3 positions; next: the ink 50/51 known plaintext (fr.16104 ff.157-159v against ff.162r-163r), then a PREREG'd key-change step with the wrong-key control, ~$15
- label p carries f in ink 40 (VIV-ANCHOR CONFLICT) - blocker: not-attempted; 4 of 6 clerk-anchored f slots hold label p (key n), at f102v L07:46-47 and L34:33-34 ("affaires" both times); the key has no f row; crops cut and a sorter page built (D4-VIV, 8 Oct 2026: tx/sorter_fp/, 4 focus tiles + 2 p-labelled refs + the readers' f sign, preflight PASS); next: the owner sorts tx/sorter_fp/sorter_viv_fp.html, then tools/sign_sorter_apply.py and a PREREG'd key-change step with the wrong-key control, ~$1
- Judge calibration for this hand - blocker: not-attempted; the fr16 judge FAILs the known-good f.103r control at this noise (N5-VIV54, N6-VIV53); next: score a lower-noise control (the clerk decipherment's own text, or f.103r after a lookalike pass) to see whether the judge can gate at all, ~$2
- fr.16104 ink 52 (5 Sept 1572, to the Queen, ff.164r-168v, ~290 lines) - blocker: not-attempted; premise negative in print (VIV52) and on the leaves (VIV52-O, 13 Oct 2026: c178-c183 viewed, no dechiffre or clear copy); f.164r-v transcribed and decoded (VIV52-O: H 2,217 / M 404 / U 106 of 2,727, b2 PASS -1.514 vs p99 -1.775, 200 wrong keys PASS margin 0.262 vs p99 0.026, longest H run 24, D1-like as 53/54/63); next: ff.165r-168v, 8 pages (f.168v 15 lines) x (2 blind Sonnet passes + 1 reconciliation) = 24 units at ~1.4 = ~$34, plus 4 native regions on openapi.bnf.fr, gates re-run with tx/viv52_test.py on the whole piece; then a first verifier (step 4)
- fr.16104 5 Sept 1572 cipher block (ff.157-159v) against its decipherment ff.162r-163r - blocker: not-attempted; known-plaintext check, not a reading; next: crops + two blind passes, aligned as tx/vivk_test.py, ~$15
- Unviewed stretches of the per-piece table - blocker: not-attempted; fr.16104 c1-c169, c192-c324 and fr.16105 c1-c94, c113-c191 not viewed (N5-VIVTAB); a decipherment of 63 filed in another volume (fr.16106 holds one such stray) not checked; next: 1200 px pass every second canvas, contact sheets, ~$3
- fr.16105 f.104r, first page of the decipherment - blocker: illegible; native crop shows word shapes only (N4-VIV3)
- Spanish-side copies (AGS Estado K) and Gachard vol. I - blocker: needs-physical-access; AGS is not digitised in a route this worker could open
- ink 52 print search on the decoded fragments (G3) - blocker: not-attempted; done by V-VIV52 (13 Oct 2026, print-check-52.tsv: generic hits only) except Google Books (HTTP 503 all session); next: rerun `tools/print_check.py ciphers/fr16104-vivonne-spain-1572 --phrases ciphers/fr16104-vivonne-spain-1572/phrases_52.txt --only gbooks` when the host answers, ~$0.3
- ink 52 La Ferriere f.191v lead (V-VIV52, AUDIT 5) - blocker: not-attempted; answered by VIV-191V (13 Oct 2026): f.191v (c208 left) is the clerk decipherment ("dechiffré de la precedente", ink 58, docket 19 Sept 1572) of the 19 Sept 1572 letter to the Queen whose cipher ends f.190r, and carries the Infante / "peau de l'ours" passage La Ferriere quotes; not ink 52 (no ink-52 phrase seen, other date, other leaves), so ink 52 gains no plaintext; next: only a side step, align the 19 Sept cipher (ff.188v-190r, first page on c204 or earlier) with ff.191r-192r as a known-plaintext pair, crops + two blind passes as tx/vivk_test.py, ~$15
- ink 67 rest (f.201v-203r) against ink 68 (ff.205v end-207) - blocker: not-attempted; f.201r only (VIV-67, 14 Oct 2026); the last 401 letters of dec67 (end of f.205v) lie past f.201r's aligned span; next: c206 left/c207-c208 and c211-c212 native regions on openapi.bnf.fr, 2 blind passes per page, the same build (benchmark item extended or a second dev item), ~$12 per two cipher pages
- image-side sign classifier for this hand - blocker: not-attempted; VIV-CLS (14 Oct 2026): a pen-unit tile kNN trained on f.102r + f.103r reads f.201r at 0.313 top-1 err vs passA 0.154 on the same 415 covered positions (gate FAIL), top-3 holds the truth for 0.359 of passA's covered errors (under 0.50), coverage 0.46 of scored positions (joined signs), permuted-label control 0.848 vs chance 0.908 (0.010 outside its band); next: a box-free window classifier (crop each reader token's own x-span, so coverage is not bounded by the segmenter), PREREG'd on the same three leaves with the same gate, ~$3
- vivonne1573-f201r-dev flags - blocker: not-attempted; align-conflict 163 and clerk-split 356 automatic flags, no verifier verdicts (confirm2 had TXV-VIV); f.205r decipherment read at word agreement 0.661; next: a TXV-VIV-style verifier pass on the 163 align-conflict positions, ~$3
- vivonne1573-f211r-dev flags - blocker: not-attempted; align-conflict 58 and clerk-split 45 automatic flags of 398 scored, no verifier verdicts; s<-d x16-17 is the top confusion in every output including the committed (circular) one, as on f.103r -- a key-side or truth-side question (label d against clerk s), not a reader error; next: a TXV-VIV-style verifier pass on the 58 align-conflict positions plus the s<-d positions of f.211r, f.201r and f.103r together, ~$3
- ink 70 rest (f.211v ff.) against ink 71 (f.215v end-217) - blocker: not-attempted; f.211r checked (VIV-70 registered FAIL on the whole-text target; VIV-70B, 14 Oct 2026, PREREG-VIV70B trim rule from ink 67 alone: 0.769 vs p95 0.522, rank 1 of 201, not blind since VIV-70 had computed the same figure post hoc; dev item vivonne1573-f211r-dev registered, 398 scored, passA 0.138 / 0.006, passB 0.166 / 0.036); the trim rule's blind test is its next pair; next: f.211v + f.212r native regions on openapi.bnf.fr, 2 blind passes per page, aligned under the same registered trim rule (offset by the letters f.211r used), ~$12 per two cipher pages
- a person as reader of this hand (VIV-HUMAN known-answer test) - blocker: not-attempted; attempt 1 scored by the parent (14 Oct 2026: W 5/12, R 10/11, undecided; the four wrong W are the d-sign tiles placed in pile z); attempt 2 (VIV-HUMAN2, PREREG-VIVHUMAN Addendum B) not built: the truth-consistent filter leaves pile 3 with 0 tiles (3: 8 -> 0, z: 18 -> 1) and the surviving z (truth a) is itself 3-shaped; next: the parent chooses an exemplar source for pile 3 (d-sign tiles from the f.102r/f.103r truth leaves at scored unflagged d rows, or the clerk-split f.201r rows whose label is in the truth set) and writes Addendum C before a rebuild with build_inputs.py --attempt 2, ~$2
- ink 63 label y split by shape (VIV-ESPLIT, 14 Oct 2026) - blocker: not-attempted; on the three truth leaves a six-class LDA separates an l-like and an h-like shape group held out (precision l 0.651 vs base 0.447, h 0.462 vs 0.126; blended 0.408 under the always-l 0.447; control 0.748), r/e/n not separated; on ink 63 f.193v/f.193r/f.192v the classifier's 51 y_l picks score no better than 51 random y -> l picks (rank 119 of 201), while every y read as l scores -1.431 vs -1.553 as h; next: a PREREG'd two-class (l vs h) gate on the truth leaves with a known-answer per-class threshold, then, only if it passes, a key-change job testing y = l with h kept for the classifier's h group, under the random-split control above (not b2/wrong-key, which cannot discriminate one label), ~$4
- ink 63 f.191r four-pass re-read (VIV-F191, PREREG-VIVF191.md) - blocker: not-attempted; crops re-cut (--deskew-region -0.60 deg, 36 bands, scratch only; manifest images/p63/manifest_vivf191.json, re-fetch command in NOTES "VIV-F191") and tx/viv63_f191/f191.py written and dry-run on a self-copy (A,B as C,D: err_2reader AC/BD 0.000, before-page numbers reproduce: longest H run 32, b2 PASS -1.454 vs p99 -1.815, wrong keys PASS 0.361 vs p99 0.058, V_strict top-1 17 vs null p99 15); stopped because the auto-mode classifier blocked the fresh blind pass's file write (pass C read all 72 crops, could not save); next: re-run the two blind Sonnet passes in a session whose permission mode lets a subagent write its pass file to the scratchpad (or have the reader return the TSV text in its final message and the worker save it, which needs no subagent file write), then `python3 tx/viv63_f191/f191.py --stats`, ~$4
## Escalation (14 Oct 2026, VIV-HUMAN2 refresh; from the VIV-F191 list)
- [x] siblings: ink 38 located; ink 40 vs 41 aligned (N5-VIVK); ink 67 f.201r vs 68 aligned (VIV-67, PASS); ink 70 f.211r vs 71 (VIV-70, registered gate FAIL rank 2 of 201 on a smeared whole-text alignment, post-hoc trimmed 0.769 rank 1; VIV-70B re-registered the trim rule and re-ran once: PASS 0.769 vs p95 0.522, rank 1, not blind; dev item f211r registered); decipherment 51 found (N5-VIV5S); per-piece table (N5-VIVTAB); ink 54 read (N5-VIV54); ink 53 ff.170r-171v read (N6-VIV53, N6-VIV53B); ink 63 ff.190r-194r read in full (N6-VIV63, N6-VIV63B, N6-VIV63C, N7-VIV63G); ink 52 f.164r-v read (VIV52-O)
- [x] clear-pages: decipherments 41, 44, 51, 68, 71, 76 are on the leaves; inks 54 and 53 interlinear words used as gloss checks (N5-VIV54 PASS, N6-VIV53 FAIL at the floor); f.171v has none (N6-VIV53B); ink 63 has none (order gate b2 instead)
- [x] known-keys: Tomokiyo's 1572-74 key on disk and held-out PASS (N5-VIVK); applied to inks 54, 53 and 63
- [x] print: Gachard I-II, d'Ars (book 1884 and RQH 35 article, L51), Catherine IV-V, Groen IV read; Ribera 2007 snippets (L50); d'Ars re-checked by date and by k-mer/phrase overlap against inks 53, 54, 63 (VIV-BREMOND); Kervyn I-VI grepped (N6-KERV); print_check on ink 54, 53 and 63 phrases (pc63b/, pc63c/); Gachard I-II, d'Ars, Catherine IV and X re-grepped for ink 52 (VIV52, none)
- [retired] key-rebuild: tools/stream_align.py from a flat start did not converge on this material (Arm A, 2 of 30 codes); a published key exists
- [x] image-check: fr.16104 c170-191 and fr.16105 c95-112, c192-248 viewed; native regions of f.173r-v, ff.170r-171v, ff.190r-194r (N5-VIV54, N6-VIV53, N6-VIV63, N6-VIV63B, N6-VIV63C, N7-VIV63G); ink 52 c178-c183 viewed at 1200 px and f.164r-v native regions via openapi.bnf.fr (VIV52-O, 13 Oct 2026): no dechiffre, no gloss; ink 52 misplaced-decipherment residual (V2-VIV52, AUDIT 6) closed 13 Oct 2026: dechiffre heads of inks 56, 60, 62 (VIV-DECH), 83, 89, 91 + 78 close (VIV-DECH2), 78, 97 (VIV-HEADS) and 101 (VIV-101, f.300r, c322, 24 Dec, King) viewed, each the decipherment of its own letter, none ink 52
- [ ] retry: ink 53 f/m/p key cells for the U labels (AUDIT 4; whole-label test negative, D1-F16104K; hand-placed per-position shape judge NON-TEST, control 4-5/12 vs 8/12, D07-VIV53; clerk word anchors on ink 40, VIV-ANCHOR 8 Oct 2026: control 5/7 PASS, V -> n assigned, f/m/p/qu under 3 positions, f on label p a conflict; next instrument: ink 50/51 known plaintext or sign sorter); ink 63 key questions on the key image (context table done, N7-VIV63G); ink 63 label questions (lookalike pass, overlap dedup); ink 53 residual unsettled tiles and kept gaps (window look-alike pass N7-VIV53L; gap re-read R7A-VIV53, 137/270 settled); ink 54 sorter/window audit (lookalike pass done, N7-VIV54L) and the col-u-row-3 relabel (key cell found, N7-VIV54Q; window judge NON-TEST, N7-VIV54R; hand-placed judge NON-TEST 0/18, DEF1-VIV54; next instrument: sign sorter / clerk alignment, hand-placed per-position crops); ink 63 noise: key-constrained lattice with a learnt confusion matrix (VIV-LAT, 14 Oct 2026: dev PASS, confirm2 FAIL, truth-in-lattice 0.124 -- next instrument: a reader that puts the true sign in the lattice); key rows from pooled clerk anchors ink 40 + 67 (VIV-KEY, 14 Oct 2026: e -> m added, gates PASS but non-discriminating; c/o under 2/3, 2 a CONFLICT; VIV-KEYV verifier 14 Oct 2026: e -> m downgraded to M, label e merges three signs; next: split label e by shape, more ink-67 anchors); image-side tile classifier (VIV-CLS, 14 Oct 2026: f.201r top-1 0.313 vs passA 0.154 on covered positions, top-3 0.359 of passA's errors, coverage 0.46: FAIL; next instrument: a box-free window classifier)
Verdict: keep going: 24 internal gaps; cheapest next: an exemplar source for pile 3 so the owner's VIV-HUMAN2 retry can be built (Addendum B leaves pile 3 empty, 8 -> 0; parent decision, then ~$2); earlier: 23 internal gaps; cheapest next: the f.191r four-pass re-read (VIV-F191 stopped before any new pass when the classifier blocked the reader's file write; crops recipe and tx/viv63_f191/f191.py ready), ~$4; earlier: 22 internal gaps and one waiting on the owner (VIV-HUMAN sorter page, 14 Oct 2026, https://claude.ai/artifact/WAPAiDSVDwYjvDotTgBFhA); VIV-KEYV (14 Oct 2026, AUDIT 7) key row e -> m downgraded C -> M (label e merges three signs: e-loop+n compound = mm, hooked c, Tomokiyo col f row 1; D1 held on 63/53/54/52; next for e: split the label by shape, ~$3); VIV-70 (14 Oct 2026) ink 70/71 pair registered gate FAIL (rank 2 of 201, whole-text target smeared the alignment; post-hoc trim 0.769 vs p95 0.522 rank 1, licenses nothing), VIV-70B (14 Oct 2026) re-ran it once under a pre-registered ink-67 trim rule: PASS 0.769 vs p95 0.522, rank 1 (not blind), dev item vivonne1573-f211r-dev registered, label table tx/viv70_labels*.tsv (no key edit); next f.211v ff., ~$12; VIV-CLS (14 Oct 2026) image-side tile classifier trained on f.102r + f.103r FAILs on f.201r (0.313 vs passA 0.154 on covered positions, top-3 0.359 of passA's errors, coverage 0.46); VIV-KEY (14 Oct 2026) e -> m added to key.tsv from pooled clerk anchors (ink 63 U 1,103 -> 942, longest H run 40 unchanged; gates PASS but cannot discriminate one row; the crossword prefers e = i: verifier shape look next); VIV-67 (14 Oct 2026) second known-plaintext pair ink 67/68 PASS (0.744 vs p95 0.507), dev item vivonne1573-f201r-dev registered, c/o/e/S label counts reach 3+ on one leaf (no key edit); VIV-LAT (14 Oct 2026) lattice decode confirm2 FAIL at a 0.124 truth-in-lattice ceiling, ink 63 not re-decoded; ink 52 f.164r-v read at D1 (VIV52-O, 13 Oct 2026, b2 + wrong-key PASS; audit 1 N3 D1, V-VIV52; audit 2 N3 D1 upheld, V2-VIV52, misplaced-decipherment residual added; inks 56, 60, 62 dechiffre heads viewed by VIV-DECH and inks 83, 89, 91 (+78 close, a Dec body) by VIV-DECH2 and inks 78, 97 heads by VIV-HEADS, 13 Oct 2026: not ink 52; and ink 101 head by VIV-101 (f.300r, 24 Dec, King): not ink 52; residual closed); f.191v viewed (VIV-191V, 13 Oct 2026: decipherment of the 19 Sept letter, not ink 52); cheapest next: the owner sorts tx/sorter_fp/sorter_viv_fp.html (D4-VIV), ~$0 agent cost; then ink 52 ff.165r-168v via openapi.bnf.fr, ~$34 (24 units), and the ink 50/51 known plaintext for f, m, p, ~$15; VIV-ESPLIT (14 Oct 2026): label y holds an l-like and an h-like shape group (held out, per class) but the classifier's ink-63 split is no better than random for the decode; every y as l beats y as h (-1.431 vs -1.553, descriptive); label e untestable on the truth leaves (15 items); no key edit; next a two-class l/h gate, ~$4
## Siblings (8 Oct 2026)

SUCCESS-SIBS (account 1, 8 Oct 2026, repository files only, no network, nothing decoded). Siblings of this folder's N3+ document(s) by volume, sender, recipient, key, design and series; 6 listed, 6 unread or not in the repository. Full rows with evidence: `SIBLINGS-2026-10-08.tsv`. p = the compiler's conservative estimate that the step yields a new counted document (N3+, D2+, two audits); not a novelty claim (rule 10). Required by `tools/gaps_check.py` for every N3+ target.

- fr.16105 ff.99-108v letter 4 June 1573 (cipher block ff.100-103; clerk decipherment at same ff. per N4-VIV2) [same-volume; unread] -- crop cipher block with iiif_lines, decode with Tomokiyo key + control; use clerk leaf as C, ~$3; ~$3; p 0.2; evidence: ciphers/fr16104-vivonne-spain-1572/NOTES.md:79,89,132-133
- fr.16104 ff.157-159v letter 5 Sept 1572 ('sans le dechiffrement'; located, same pool) [same-volume; unread] -- transcribe with key.tsv/key_tomokiyo.tsv via viv54 pipeline, decode --check + shuffled-key control, ~$3; ~$3; p 0.15; evidence: ciphers/fr16104-vivonne-spain-1572/NOTES.md:49,89,96 (located, no clerk gloss; ~150-175 cipher lines)
- 26+ cipher letters 'avec le dechiffrement' in fr.16104-16106 (period decipherment on leaf, Gachard II) [same-key; unread] -- pick one letter with adjacent clerk gloss, align as known plaintext to extend key, ~$3 each; plaintext mostly N1-N2 (Gachard abstracts); ~$3; p 0.10; evidence: ciphers/fr16104-vivonne-spain-1572/NOTES.md:8,16-18,89 (floors from Gachard OCR)
- fr.16105 ink piece 38 (4 June 1573 second copy, 'sans') and 8 June 1573 duplicate [same-volume; unread] -- view canvases 95-101 for old ink no. 38, ~$0.5-1; ~$1; p 0.08; evidence: ciphers/fr16104-vivonne-spain-1572/NOTES.md:127,133 (leaves not yet located)
- fr16106-vivonne-longlee-1579 (Vivonne/Longlee cipher family, 1579) [same-design; unread] -- blocked: owner sign sorter on c107 crops; Mousset 1912 prints Longlee dispatches (N1); p 0.02; evidence: KEY-DESIGN.tsv fr16106 key.tsv homophonic fr 1570s; NEXT-STEPS.tsv (needs-person: sign sorter)
- fr16142-noailles-constantinople-1571 (same decade/language alphabet-substitution) [same-design; unread] -- none: different key; blocked on person's read; p 0.01; evidence: KEY-DESIGN.tsv fr16142 key.tsv; NEXT-STEPS.tsv (needs-person)

## D4-VIV (8 Oct 2026, 09:01-09:08 UTC by date -u, account-4 worker for LANE DEFAULT-account-4-20261008-0740): crops of the four f-on-label-p positions for the sign sorter
Brief: .claude/briefs/runs/2026-10-08-account4-default-0740-jobs.md "### D4-VIV". No reading change, no key change, no score.
**Positions** (tx/vivanchor_result.json target/cell_centric/f/positions/p, token index of tx/f102v_rec.tsv as read by tx/vivanchor.py): f102v L07:46, L07:47 and L34:33, L34:34,
the "ff" of "affaires" twice, read "x s p p s tz" / "s p p s tz". f102v_passB.tsv wrote L07:46 as "f"; pass A and the reconciled row have p. Placed by eye on zoomed native strips.
**Native regions (one fetch each, Gallica IIIF, canvas 106 = f.102v):**
`python3 tools/iiif_lines.py --ark btv1b9009663p --canvas 106 --region 1200,1290,2980,220 --centres 110 --out ciphers/fr16104-vivonne-spain-1572/images --prefix c106_viv_fp_L07 --lines-per-crop 1 --top-margin 60 --bottom-margin 60 --debug`
`python3 tools/iiif_lines.py --ark btv1b9009663p --canvas 106 --region 1200,4360,2980,220 --centres 110 --out ciphers/fr16104-vivonne-spain-1572/images --prefix c106_viv_fp_L34 --lines-per-crop 1 --top-margin 60 --bottom-margin 60 --debug`
(two earlier calls with a doubled "ark:/12148/" prefix got HTTP 500 for the malformed URL and stopped; Gallica requests 4 in all.)
**Sorter inputs, tx/sorter_fp/:** signs.tsv (sid, page, x, y, w, h in region pixels), labels.tsv (sid, sign, family), focus.tsv (the four questions), cipher_lines.tsv,
pages/ (symlinks to the two src_..._1200_1290_ and _1200_4360_ region files). Seven tiles: fp_L07_46, fp_L07_47, fp_L34_33, fp_L34_34 (label p, family clerk-f);
ref_L07_01_p and ref_L34_02_p (p-labelled signs from the same lines, family p-as-n); ref_L07_03_f (the sign the readers label f, L07 token 3). Page built:
`python3 tools/sign_sorter.py --signs tx/sorter_fp/signs.tsv --labels tx/sorter_fp/labels.tsv --pages tx/sorter_fp/pages --focus tx/sorter_fp/focus.tsv --cipher-lines tx/sorter_fp/cipher_lines.tsv --title ... --out tx/sorter_fp/sorter_viv_fp.html`
(paths relative to this folder): 2 piles, 7 tiles, preflight PASS (template, answerable, right line, contact sheet tx/sorter_fp/sorter_viv_fp.preflight.png, eyed: every box on its sign).
**Descriptive, not a judgement:** in both words the first sign is a tall stroke with a crossbar and the second a tall p, both descending well below the line; the two p-as-n refs
have a short descender and a bar through the stem; the readers' f (L07:3) is a small looped sign. Whether the tall pair is its own pile is the owner's call. Tomokiyo's key
column f is not on the page (no crop of the key image cell was on disk). Not published as an artifact; the owner opens the HTML from the repository.


## VIV52-R (8 Oct 2026, 14:13 UTC by date -u, account-2 lane orchestrator for acct3-orchestrator): step 0 probe 403, stopped
Brief: .claude/briefs/runs/2026-10-08-acct3-sibs-ledger3.md "## VIV52-R". One reachability request,
`curl -sS -A "Mozilla/5.0" -o /dev/null -w "%{http_code}" https://gallica.bnf.fr/iiif/ark:/12148/btv1b9009609w/f178/info.json`,
answered 403 at 14:13:18 UTC (about 80 min after VIV52's block). Per the brief: no retry, steps 2-4 not run, WORK-QUEUE row VIV52-R
bounced. Gallica requests this job: 1. Next: the ink 52 crops need a container or desk Gallica does not block (e.g. a LOCAL-QUEUE row
for the owner's browser, or a later cloud retry once the block lifts); premise (VIV52 step 1) stays negative.

## TX-CONFIRM-SET-2 (9 Oct 2026, 15:44-15:5x UTC by date -u, account-1 worker for orchestrator (account-4)): ink 40 f.103r as BENCHMARK-TX confirm2 item
Brief: .claude/briefs/runs/2026-10-09-account4-lane-tx-engineer-2.md (S2 guard) with the first campaign brief's "Note for TX-CONFIRM-SET".
A session outside LANE TX-ENGINEER-2. No reads, no subagent calls, no network; disk only. **LANE TX-ENGINEER-2 and its workers do not open this
folder, benchmark-tx/vivonne1573-f103r-confirm2.truth.tsv, its outputs or benchmark-tx/build_vivonne_confirm2.py before their single final score.**
- Why this leaf: a symbol cipher with a published key (Tomokiyo, henryiii_Vivonne1.png) and a period clerk decipherment on separate leaves
  (ff.104r-108v, no gloss on the cipher leaf), crops and a reconciled transcription already on disk (N5-VIVK), on a hand none of the six
  benchmark items use. Considered and not taken: fr20140-danzay-1557 f.16/f.24/f.30 (images not on disk, Gallica 403 all of 9 Oct);
  clair349-este-guise-1556 and decode-1168-modena-costabili-1492 (interlinear decipherment written over the cipher: a reader would see it in
  the line crops); rah-juan-manuel-1521 (DECODE images not committed, word-code layer); the Dinteville fr.3619/fr.3623 DECODE records
  (the lane's own scout, decode-scout-2026-10-09.md).
- Build: `python3 benchmark-tx/build_vivonne_confirm2.py` (recipe in its docstring; `--check` exit 0). 2033 positions (raw tokens of
  tx/f103r_rec.tsv), 1068 scored, 965 excluded (align-uncertain 310, unaligned 226, off-key 147, key-M 169, letter-off-key 113).
  Control: f.103r match share under the published key 0.605 vs 200 value-shuffled keys mean 0.426, p95 0.498, max 0.557 (rank 1/201): it
  passes, but by a narrow margin (Spinelli's was 0.901 vs 0.360).
- Truth quality, stated plainly: the clerk's hand was read at A/B word agreement 0.66-0.71 (N5-VIVK), so the known text is noisy. Two flags were
  set at build time, before any reader score: align-conflict 256 (the committed sign decodes to another letter), clerk-split 438 (the two clerk
  readings differ at that letter); 588 of 1068 flagged. Tightening the neighbour window (0.5 -> 0.7) or requiring both neighbours to match
  left the conflict share at 0.23-0.24, so the conflicts are not mostly alignment drift; the top one (s <- d, 17) matches VIV-ANCHOR's finding
  that readers write d for an s homophone (a reader-inventory error class, not only truth noise). The build kept window 0.5 (the value first
  written); no truth row was edited by hand.
- Baseline at build (N5-VIVK's blind Sonnet passes, value-level): committed 0.221 (236/1068), passA 0.232, passB 0.246 as measured; passA vs
  passB paired fixed 26 / broken 14, p 0.081. Flagged-excluded: committed 0.000 by construction, passA 0.017, passB 0.044. The item has the
  headroom S2 needs (an 8-25% hand); read it with the paired count against today's pipeline and both figures, never the flagged figure alone.
- prior_work.py: no items.tsv row for f.103r (`--derive` proposed 9 rows, none for ink 40; the pending file was not kept). Novelty is not in
  question for a benchmark item (key published, text a period clerk decipherment); no N-class assigned (rule 10).
Requests 0; subagent calls 0. Cost: the orchestrator's get_session reading.

## Access log

- 11 Oct 2026 01:03:43 UTC (account-3 parent, L74 whole-page view of f.102r): one request, curl with a browser User-Agent, https://gallica.bnf.fr/iiif/ark:/12148/btv1b9009663p/f105/4320,380,3941,4850/full/0/native.jpg (canvas 105 = f.102r; the region runs to the canvas's right edge, 8261 px per sources/gallica-manifests/btv1b9009663p.json) -> HTTP 403, server cloudflare, 'Attention Required! | Cloudflare' (cf-ray a489f25f2d627be0-IAD), the same block two requests met at 00:05-00:06 UTC; not retried (good-citizen rule); desk fetch queued as LOCAL-QUEUE L78.

## V2-VIV52 (13 Oct 2026, 10:06-10:2x UTC by date -u, account-4 verifier for LANE DEFAULT-A4-0935): ink 52 second adversarial audit
AUDIT.md "AUDIT 6": N3 upheld, D1, key published (Tomokiyo). f.191v verified from the images on disk (VIV-191V upheld); Gachard II LVII-LVIII prints the f.191r decipherment text verbatim (19 Sept letter), and f.191v reports a visit made after the 7 Sept news, so it cannot be in a letter closed 5 Sept. New residual: misplaced decipherments (Tomokiyo, citing Mousset) -- ink 51 and ink 58 excluded, later dechiffre heads unviewed (gap line added). Searches: IA FTS 14, OpenAlex 5, S2 2, CORE 2, HAL 2, CrossRef 1, Persee 1, Google Books 1 (503); 4 JSTOR-QUEUE rows queued. No reading changed.
