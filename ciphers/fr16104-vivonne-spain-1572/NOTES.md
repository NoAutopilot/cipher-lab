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
