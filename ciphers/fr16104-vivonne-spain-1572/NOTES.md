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
