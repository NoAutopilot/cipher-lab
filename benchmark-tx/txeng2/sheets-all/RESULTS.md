# TXE2-SHEETS-ALL: every reader sheet and atlas under ciphers/, classified, atlas exemplars crossed where a truth exists

LANE TX-ENGINEER-2 incarnation 2, account 4, Opus; PREREG benchmark-tx/PREREG-txeng2-8.md A2 (binding); brief
.claude/briefs/runs/2026-10-09-account4-txe2-round8.md row TXE2-SHEETS-ALL. 9 Oct 2026, 20:46-20:5x UTC by date -u.
Read-free: no reader, no subagent, no host request, no pass run. Nothing corrected: no sheet, atlas or *.truth.tsv edited
(a correction is a per-folder baseline change for that folder's own lane to pre-register, PREREG-txeng2-0 Amendments 4-6).

Openings of eval truth: 0

Benchmark eval items (Spinelli confirm, Birago no.87, f152r) are A1's (benchmark-tx/txeng2/sheetaudit/RESULTS.md) and were
not re-opened: in the one cross below that touches the Birago family, every exemplar on f178r/f178v/f179r/f152r is dropped
by leaf name before any lookup, and no benchmark-tx/*.truth.tsv or harvest/align87 file was read.

Method. `find ciphers -name 'sign_sheet*' -o -name 'atlas*' -o -path '*/glyphs/*' -o -path '*/sorter/*'` (1,702 paths, 38
folders) plus a grep of every folder's NOTES.md for `*sheet*`/`*atlas*` image or TSV names (added 14 folders' sheets the
find missed). Each sheet classified as **printed-key cut** (cells cut from a period or published key image), **text list**
(words, no tiles), **atlas-built** (tiles cut from the letter's or family's own boxes), **instrument** (a shuffled or
hidden-truth test sheet, a review montage, an unlabelled cluster sheet) or **sorter pool** (tiles for a person's sort, not
an exemplar sheet). A truth counts for a cross only if it is (a) per position and (b) independent of the sheet's own labels
(a gloss, a known plaintext, a key value). An H decode whose sign ids were read with the same atlas reads key[cell] at every
exemplar by construction, so it is listed as "circular", not as a check. Script: `cross_all.py` (A1's cross_spinelli.py
pattern), output `cross.tsv` (131 rows).

## 1. Every sheet, one row each

| folder | sheet | kind | tiles | truth | verdict |
|---|---|---|---|---|---|
| nevers-birago-fr3251-1572 (+ birago-fr3252 f117 copy) | harvest/sign_sheet_blind_1572.png | printed-key cut (Tomokiyo NeversBirago.png) | key cells | -- | clean by construction (A1) |
| nevers-birago-fr3251-1572 | atlas/sheet_truth/sheet_01-04.png (TX-SHEET) | atlas-built | 185 | A1 | A1: 1 MISLABELLED (f152r T36) |
| nevers-birago-fr3251-1572 | **atlas/atlas.jpg + atlas.tsv** (TX-ATLAS-B72; TX-DECODE top-k input, not the readers' sheet) | atlas-built (glyph_atlas.py, 45 cells) | 414 | atlas/secure_tokens.tsv, grade S, not independent (its rule needs the atlas kNN to agree) | 345 on eval leaves not crossed; 69 crossed: 12 OK, **1 MISLABELLED**, 56 no-truth |
| ceppo-nevers-fr3251-1570s (+ ceppo-nevers-fr4702-f36 uses it) | harvest/sign_sheet_blind.png | printed-key cut (nevers_add1.png) | 55 | -- | clean by construction (A1) |
| spinelli-beinecke-c1515 | glyphs/atlas.png v3, atlas_v2.png, atlas_v4.png | atlas-built | 152 / 34 rows / v4 | eval truth (A1) | A1: v3 3, v2 5 MISLABELLED; v4 0 (not re-opened) |
| fr3985-nevers-revol-1593 / fr3986-nevers-revol-1593 | **tools/keys/key60_atlas/contact_sheet*.png** (atlas.tsv 80, atlas264.tsv 52, atlas264ext.tsv 10); readers: fr3985 f176 passes, fr3986 held-out passes | atlas-built (exemplars cut from the interlined leaves c.264 / c.298) | 80 + 10 | contemporary interlined gloss (aligned S) vs key.tsv (no.60 table, H/M) | atlas264+ext 62 crossed: 41 OK, **4 VALUE-CONFLICT**, 17 no key cell; on-file atlas.tsv `agreement`: 67 yes, 7 form, 4 no, 2 partial |
| fr5761-election-1519 | glyphs/atlas.png, atlas_part1/2, sheet_signs_00-04 (readers: key_pass*_atlas.tsv) | atlas-built (35 cells) | 169 | key.tsv H plain per key row, but rows carry no box id | uncrossable by script; NOTES already records K1, K13, K15, K28 impure |
| clair349-este-guise-1556 | images/atlas/S*_sign crops, sign_sheet.jpg (readers: passA/passB_atlas.tsv) | atlas-built (one hand crop per sign) | 80 | gloss + published key exist; crops carry no position id | uncrossable |
| baluze167-davaux-1637 | d1bal167/exemplar_sheet.png, d2davex/exemplar_sheet.png | atlas-built from glossed crops | 66 | gloss = the cell by construction | no value mislabel possible; NOTES l.557 eye check: one shape glossed u and i, two shapes per u and per s (shape hazard, on file) |
| dupuy452-carpi-1520 | glyphs/contact_sheet.jpg (50 cluster codes) | atlas-built cluster sheet | 5,792 boxes | reading_tokens H, read through the same code->key mapping | circular, not a check |
| moray-wood-1568 | no804/refsheet/refsheet_classes.png, refsheet_mi.png | atlas-built (DP-placed boxes, labels from a published transcription) | 134 | none independent | eye check RUN4-MOR: 0 wrong, 0 clipped; not yet in reader use |
| debosnys-1883 | glyphs/atlas.png (68 cells), inventory.png (160 ids, the readers' sheet), sheet_signs/marks | atlas-built | 392 (+163 inventory rows) | none (open) | **unverifiable, atlas-built** |
| fr2933-salviati-1525 | glyphs/atlas.png, atlas_part1/2 (readers: passA/passB_atlas.tsv) | atlas-built (35 cells) | 350 | none (open) | **unverifiable, atlas-built** |
| fr3151-seure-1558 | glyphs/atlas.png (21 cells) | atlas-built | 210 | none | **unverifiable, atlas-built** |
| fr3151-seure-1558 | known_keys/tournon/exemplar_sheet.png (readers: tournon passA/passB/passR) | atlas-built (leaf's own crops) | 31 | slip key gives values per shape, not per position | **unverifiable, atlas-built** |
| fr2980-gramont | atlas/atlas_f29.png + atlas_f30add.png (readers: f.30 passes, PASS-BRIEF-f30.md) | atlas-built (DP of the f.29r transcription onto boxes, eye-fixed) | 124 + f30 additions | none (transcription only) | **unverifiable, atlas-built** |
| fr16142-noailles-constantinople-1571 | run2/nxatl/sheets/atlas_k*.jpg | instrument: unlabelled cluster sheets for the sorter | 1,440 line-half exemplars, 120 clusters | no box ids | out of scope (no cell values) |
| wvo-11106-bergh-1572 | atlas/sheet_signs_00-02.png | instrument: unlabelled cluster sheets (readers read numbered strips) | 875 boxes | purity vs reads on file (0.402 vs null 0.273) | out of scope |
| fr3416-nevers-fils-1589 | verify/l05_atlas (box_labels.tsv) | instrument: classifier labels, gate FAILed (LOO 0.644) | 87 | H tokens | out of scope (not a reader sheet) |
| trew-posthius-1614-18 | glyphs/atlas.tsv/png (G1-G9) | printed-key cut (hand boxes on the period key leaf 1618_left) | 9 | the key leaf itself | clean by construction |
| florence-dieci-responsive | key4/sheet_key4_anon.png | printed-key cut (58-6.pdf) | 162 | -- | clean by construction |
| fr15564-mercoeur-1586 | sheet/tile_1..4.jpg, sheet_full.jpg | printed-key cut (Lasry's key image) | -- | -- | clean by construction |
| baluze103-letellier-marca-1644 | tx/key_sheet_3x.png | printed-key cut (Tomokiyo's drawing) | -- | -- | clean by construction |
| fr4735-monluc-lansac-poland-1573 | keysheet_monluc1_ids.png | printed-key cut | -- | -- | clean by construction |
| fr4735-monluc-lansac-poland-1573 | blind_sheet.png (34 numbered tiles) | instrument (hidden-truth test) | 34 | -- | out of scope |
| espagnol142-mercy-1648 | sheet_unlabelled.png | instrument (key in sheet_key.json) | -- | -- | out of scope |
| fr4715-vieuville-pool | images/f60r_zero_sheet.png | instrument (shuffled Z01-Z30, hidden truth json) | 30 | -- | out of scope |
| sachsstaatsarchiv-manteuffel-1712 | sheet_blind_*.tsv / sheet_key_*.tsv contact sheets | instrument (blind-then-key) | -- | -- | out of scope |
| fr16104-vivonne-spain-1572 | tx/lookalike53L/sheet.png | instrument (line crops; "this hand has no reference-shape sheet") | -- | -- | out of scope |
| fr2933-salviati-1525 | atlas_review/grp_*.png, glyphs/f55v_atlas_pass/cmp*.png | instrument (review montages) | -- | -- | out of scope |
| fr3986-nevers-revol-1593 / florence-dieci-responsive / willem-van-hessen-1567 | atlas_heldout/, atlas_tune/, siblings/atlas/ | instrument (scoring, tuning, 5 illustrative crops) | -- | -- | out of scope |
| dint-f128, bir1591, dint-f98v/f113/f89, fr16104 tx/SIGNS.md | pass_instructions / blind_pass_brief vocabularies | text list | 0 | -- | clean by construction (A1) |
| fr4715-f61-mayenne-1592, august-van-saksen-1561-64, rah-canada-1869, beinecke-mellon29-elia | verify_v5/atlas_blind.tsv, glyphs/atlas.md, glyphs/atlas.md, atlas.tsv | text list (shape words / code counts) | 0 | -- | clean by construction |
| 26 folders: armstrong-madison-1808, baluze103, birago-fr3252, bne20211, ceppo-nevers-fr3251, debosnys, decode-1162, esp318, florence, fr16045, fr16106, fr16142, fr16144, fr3151 (known_keys/sorter), fr3416, fr3621, fr3986, harley-287, matignon, mlh-1976, na-oldenbarnevelt, nevers-birago (two), rah-juan-manuel, rayburn, wvo-11106, wvo-hessen | sorter/ | sorter pool (tiles for a person's sort; no exemplar sheet exported) | -- | -- | out of scope |

## 2. Exemplars whose value is not the cell they illustrate

| folder | sheet | cell | box id | truth value | verdict |
|---|---|---|---|---|---|
| nevers-birago-fr3251-1572 | atlas/atlas.tsv | T64 | f184v_04_009 | T52 (secure_tokens.tsv, S) | MISLABELLED (S-grade truth, not independent of the atlas) |
| fr3985/fr3986 key60 | tools/keys/key60_atlas/atlas264.tsv | v | A07 (c.264, v[n]) | gloss u; key v = li/lo (M) | VALUE-CONFLICT (on file as "partial": v'=u, tick not seen) |
| fr3985/fr3986 key60 | atlas264.tsv | v | A21 (reconn[u]) | gloss u; key li/lo | VALUE-CONFLICT (on file "partial") |
| fr3985/fr3986 key60 | atlas264.tsv | ꝑ (pl) | A31 (p[e]re) | gloss e; key so (M) | VALUE-CONFLICT (on file "no") |
| fr3985/fr3986 key60 | atlas264.tsv | v | A44 (cour[o]nne) | gloss o; key li/lo | VALUE-CONFLICT (on file "no": "v as o, not in key") |

The four key60 rows agree one for one with LANE R5 G's own `agreement` column of 24 Sept 2026 (atlas.tsv), so they were
already on file; whether each is a tile of the wrong cell, a homophone missing from the no.60 table, or a gloss misalignment
(the alignment is grade S) is not settled by this read-free job. A16/A28 (pi-with-i = que) first read as conflicts only
because key.tsv spells that ligature's tag differently; the on-file column decides them OK. The 7 "form" rows (the gloss
value is a key value, but this hand's shape resembles another cell: φ like f, +o like to, 20 like ro) and the 2 "no key
sign" rows (A09, A15) are look-alike or unlisted-sign hazards, not value mislabels, and are not counted.

## 3. Counts

- Sheets classified: 34 rows above (sorter folders grouped as one row of 26).
- Atlas-built sheets crossed against a per-position independent truth: 2 here (Birago 1572 atlas, key no.60 atlas) + 2 by
  A1 (Spinelli, TX-SHEET). Mislabelled or value-conflicting exemplars found here: 5 (1 + 4; the 4 already on file).
- **Folders whose readers use an atlas-built sheet with no truth to check it against: 4** (debosnys-1883 1 sheet,
  fr2933-salviati-1525 1, fr3151-seure-1558 2, fr2980-gramont 1; 1,107 tiles plus debosnys's 163-id inventory). Two more
  have a truth that cannot be crossed at box grain (fr5761-election-1519, 169 tiles; clair349-este-guise-1556, 80 crops):
  6 if counted together.

## Files (as of origin/main 4f3e84a98 at start; each input last touched in commit 91b568a0d)

| file | commit | sha256 |
|---|---|---|
| ciphers/nevers-birago-fr3251-1572/atlas/atlas.tsv | 91b568a0d | 010b40276d3bda10e9df711d3b5cbd21d81ead89a0995a5e9dce32f074860fd8 |
| ciphers/nevers-birago-fr3251-1572/atlas/secure_tokens.tsv | 91b568a0d | b69e997f0f82d2e808c005a5cbf7e1a4aa760edfef5ea4724a697fe89eb47976 |
| tools/keys/key60_atlas/atlas.tsv | 91b568a0d | 378ee54dcda7fc79370c2aa5a85327f4875b0af0025223fb65e3d1e7151119d9 |
| tools/keys/key60_atlas/atlas264.tsv | 91b568a0d | 52f522c0e29ad85ea56e08b6cda8f1d15ffdbd598299be2a7b700d31f7fad761 |
| tools/keys/key60_atlas/atlas264ext.tsv | 91b568a0d | 583e34ed722f8813932c3a6458b54e150185e8edc32db217b99bf517096f47ea |
| ciphers/fr3986-nevers-revol-1593/key.tsv | 91b568a0d | b21d6ed47ab3e614bbd768382d0c05be909a0da06e061dd98d829e5b070706b0 |
| ciphers/debosnys-1883/glyphs/atlas.tsv | 91b568a0d | 43b71a96778bac6b075fd248c76fdfe43ada144fa0924a750462bebe0af7877e |
| ciphers/debosnys-1883/glyphs/inventory.tsv | 91b568a0d | 72778f3a739ec5f1a5596c3370ce1f1942769b26ce648089ee4a9fae7509230a |
| ciphers/fr2933-salviati-1525/glyphs/atlas.tsv | 91b568a0d | 21514859db10612790c854e2682672f5648d2a201c89a06bf04173e6e674a599 |
| ciphers/fr3151-seure-1558/glyphs/atlas.tsv | 91b568a0d | 09a0ff5bf7d58e2f1a95161f71db8f7a396958509c2a43e072f6852126a1a3e1 |
| ciphers/fr3151-seure-1558/known_keys/tournon/exemplars.tsv | 91b568a0d | 0ea3761254a0864cd9e617292ddca2235e16bce8c359bdd145ff358feed5ec0d |
| ciphers/fr5761-election-1519/glyphs/atlas.tsv | 91b568a0d | 52031675f39dd41b8e3006285eba2f111a92236c8d3f448690235ea0dc4ed808 |
| ciphers/fr2980-gramont/atlas/atlas_f29.tsv | 91b568a0d | 6fe37b27a3398f19a05b5459e679b66ecc4b70e72e2ce6a7632df1c8bc121c7c |
| ciphers/fr16142-noailles-constantinople-1571/run2/nxatl/atlas.tsv | 91b568a0d | 214d53b53b0c1711bf31d13b4072de443b433b131dc57cf501d15f09d1bf7c65 |
| ciphers/moray-wood-1568/no804/refsheet/boxes.tsv | 91b568a0d | e98b9ec94d2a6a00ed5767e29714c943e9950c241b57e183eb11c646fc52cb59 |
| ciphers/clair349-este-guise-1556/images/atlas/atlas.tsv | 91b568a0d | 807e2dd28bc47d7bdb44f8dcabc0767bf7fd60be583dde1325c7493058d62e07 |
| ciphers/trew-posthius-1614-18/glyphs/atlas.tsv | 91b568a0d | ca518334e87df9e402c53e71c531c2952fecb49f1b9bcd36adead860cad2b240 |
| benchmark-tx/txeng2/sheets-all/cross_all.py | this job | 56422b828f82a3ecbad54228f23e861f1ab210d7f8f0254c38e2fae4117fb6a2 |
| benchmark-tx/txeng2/sheets-all/cross.tsv | this job | fc2e13140d66d5b786af4a3b742ba1b33476cb58d9147b4940c3cabcfc3bd7c4 |

Suggestion (one line, not done): the four uncheckable folders' own lanes could each pre-register a gloss-or-key cross the
way A1 did, where a glossed sibling leaf exists.
