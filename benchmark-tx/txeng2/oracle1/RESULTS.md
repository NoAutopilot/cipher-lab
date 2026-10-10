# OL1-BOXES results (PREREG-txeng2-21 section OL1-BOXES; TXE2-OL1BOXES worker, account-4, Opus 5.5; 10 Oct 2026 02:13-02:3x UTC by date -u)

Machine-proposed sign boxes, a left-to-right reading order and blind overlays on the 35 ORACLE-LOCATION-1 manifest lines, plus
the inputs and build of the owner's blind box-verify sorter page (LOCAL-QUEUE L74). **Read-free**: no reader call, no vision call
on any crop or overlay, no truth file, no key, no decode, no pass output, no label from any read. Box counts are compared to
nothing. Openings of eval truth: 0. No read, no truth, no pass opened.

Manifest check before anything: `sha256sum benchmark-tx/txeng2/oracle1/manifest.tsv` =
978322f62c04d59097f521d73690db00d61a44e794af40546db3d9dfb34b45de, equal to manifest.tsv.sha256; the manifest was not re-sampled
or edited.

## Recipe (regenerate: `sh benchmark-tx/txeng2/oracle1/build.sh`)
1. `tools/glyph_atlas.py segment` default mode (the no.87 atlas recipe), one run per hand over that hand's crops. `--median-h` was
   NOT used: no crop is speck-dominated (per-crop median sign height against its hand's: vivonne 44-71 px, birago 39-82 px,
   luzerne 12-18 px; lowest/hand-typical 0.72, 0.63, 0.75 -- none collapses the way c.127 L08_s1 did, 4 px against ~50).
2. `build_ol1_boxes.py`: TXE2-BOXES's spin_join.py overlap rule generalised to n crops (a box kept from s_i when its centre in
   line coordinates lies between the s_(i-1)/s_i and s_i/s_(i+1) overlap midpoints; three-crop no.87 lines s1/s2 then s2/s3;
   crop geometry from each crop folder's manifest.json, luzerne lines are one crop each). Small detached marks (glyph_atlas
   marks.tsv) KEPT as their own boxes (kind=mark). spin_join.py's --min-frac fragment rule NOT applied (PREREG step 2). Its
   --ghost (verso bleed-through) rule made **crop-relative** -- a declared deviation: the Spinelli absolute 0.45 dropped 461 of 468
   luzerne boxes (a small pale hand; box darkest-10%/crop-median ratios 0.49-0.77, median 0.67, against 0.27 vivonne and 0.38
   birago), so a box is dropped when that ratio exceeds max(0.45, 1.25 x the crop's own median sign ratio). Set from those ratio
   numbers alone, before any overlay existed; no image was looked at. Dropped counts are in boxes/counts.tsv (ghost_dropped).
   Reading order = ascending line-coordinate centre x, signs and marks together.
3. Overlays: per line, the line's crops stacked top to bottom on a greyscale page; signs solid Okabe-Ito blue #0072B2, marks
   DASHED orange #B35900 (Okabe-Ito orange #E69F00 darkened: #E69F00 fails 3:1 on the page grey -- cvd_check "contrast 2.25 < 3");
   order numbers in black on a white tag; never red/green, never meaning by hue alone (solid vs dashed). `<line>_plain.jpg` is the
   same stack unmarked, beside it.
4. Sorter: `tools/sign_sorter.py` blind mode, --signs boxes (page = the crop image, via sorter/pages.json), --labels every tile
   in ONE neutral pile `unsorted` (no label, no value, no cluster, no rank, no focus, no --show-values), --tile-quality 70,
   title "Oracle boxes: verify the cuts", lede = L74's instruction. The tool's blind seed note ("first piled by our readers'
   labels") is untrue here and is replaced in the built page and data by "all in one pile, unsorted: no reader, no label and no
   machine guess went into this page, so what you decide is blind." (the only edit to the tool's output; build.sh does it).

## Boxes per hand (compared to nothing)
| hand | lines | boxes | signs | marks | ghost-dropped |
|---|---|---|---|---|---|
| vivonne1573-f102r | 12 | 565 | 516 | 49 | 42 |
| birago1572-no87 | 12 | 367 | 340 | 27 | 52 |
| luzerne108a-p1 | 11 | 480 | 428 | 52 | 3 |
| **total** | 35 | 1412 | 1284 | 128 | 97 |

## Boxes per line
| hand | line | boxes | signs | marks | ghost-dropped |
|---|---|---|---|---|---|
| vivonne1573-f102r | f102r_L03 | 47 | 44 | 3 | 3 |
| vivonne1573-f102r | f102r_L06 | 48 | 43 | 5 | 0 |
| vivonne1573-f102r | f102r_L09 | 43 | 41 | 2 | 4 |
| vivonne1573-f102r | f102r_L11 | 45 | 43 | 2 | 7 |
| vivonne1573-f102r | f102r_L12 | 57 | 54 | 3 | 3 |
| vivonne1573-f102r | f102r_L15 | 45 | 44 | 1 | 4 |
| vivonne1573-f102r | f102r_L17 | 45 | 41 | 4 | 1 |
| vivonne1573-f102r | f102r_L21 | 44 | 40 | 4 | 2 |
| vivonne1573-f102r | f102r_L22 | 48 | 45 | 3 | 8 |
| vivonne1573-f102r | f102r_L23 | 49 | 42 | 7 | 1 |
| vivonne1573-f102r | f102r_L26 | 53 | 43 | 10 | 4 |
| vivonne1573-f102r | f102r_L27 | 41 | 36 | 5 | 5 |
| birago1572-no87 | f178v_L01 | 26 | 25 | 1 | 7 |
| birago1572-no87 | f178v_L02 | 30 | 26 | 4 | 4 |
| birago1572-no87 | f178v_L03 | 30 | 28 | 2 | 0 |
| birago1572-no87 | f178v_L04 | 28 | 27 | 1 | 3 |
| birago1572-no87 | f178v_L05 | 33 | 29 | 4 | 6 |
| birago1572-no87 | f178v_L06 | 29 | 27 | 2 | 4 |
| birago1572-no87 | f178v_L07 | 25 | 25 | 0 | 8 |
| birago1572-no87 | f178v_L08 | 34 | 32 | 2 | 5 |
| birago1572-no87 | f178v_L09 | 29 | 28 | 1 | 7 |
| birago1572-no87 | f178v_L10 | 35 | 33 | 2 | 3 |
| birago1572-no87 | f178v_L11 | 31 | 29 | 2 | 2 |
| birago1572-no87 | f178v_L12 | 37 | 31 | 6 | 3 |
| luzerne108a-p1 | p1_L01 | 35 | 32 | 3 | 0 |
| luzerne108a-p1 | p1_L02 | 46 | 39 | 7 | 1 |
| luzerne108a-p1 | p1_L03 | 43 | 37 | 6 | 0 |
| luzerne108a-p1 | p1_L04 | 44 | 39 | 5 | 0 |
| luzerne108a-p1 | p1_L05 | 47 | 42 | 5 | 0 |
| luzerne108a-p1 | p1_L06 | 48 | 41 | 7 | 0 |
| luzerne108a-p1 | p1_L07 | 33 | 32 | 1 | 2 |
| luzerne108a-p1 | p1_L08 | 45 | 40 | 5 | 0 |
| luzerne108a-p1 | p1_L09 | 48 | 43 | 5 | 0 |
| luzerne108a-p1 | p1_L10 | 48 | 43 | 5 | 0 |
| luzerne108a-p1 | p1_L11 | 43 | 40 | 3 | 0 |

## tools/cvd_check.py (overlay colours)
```
benchmark-tx/txeng2/oracle1/build_ol1_boxes.py: 4 colour literals, 2 chromatic, 0 flags
--marks #0072B2,#B35900,#000000 --bg #DCDCDC:
normal  worst pair #0072B2 vs #000000  dE2000 39.2  margin +19.2
protan  worst pair #B35900 vs #000000  dE2000 38.1  margin +18.1
deutan  worst pair #0072B2 vs #000000  dE2000 38.3  margin +18.3
tritan  worst pair #0072B2 vs #000000  dE2000 41.5  margin +21.5
PASS
--marks #0072B2,#B35900,#000000 --bg #FFFFFF:
normal  worst pair #0072B2 vs #000000  dE2000 39.2  margin +19.2
protan  worst pair #B35900 vs #000000  dE2000 38.1  margin +18.1
deutan  worst pair #0072B2 vs #000000  dE2000 38.3  margin +18.3
tritan  worst pair #0072B2 vs #000000  dE2000 41.5  margin +21.5
PASS
```

## tools/sorter_preflight.py (the built page) -- **FAIL; the page is NOT fit to publish as built**
```
1 piles, 1412 tiles, 0 skipped, 0 clusters (none), 0 ranked, 4752 KB -> benchmark-tx/txeng2/oracle1/sorter/oracle_boxes_sorter.html
PASS template: ok, Fix the cut present, marker 2026-10-09.4
FAIL answerable: 0 focus tiles, 0 named piles of 1, 0 unanswerable -- focus box empty; 0 named pile(s) [] -- a tile has nowhere to go
FAIL right line: 1412 tiles; 0 tile(s) off the cipher lines, 71 of 71 listed lines have tiles; shape: 62 wide (>2.5x median 39 px), 21 strip-height boxes, 136 ink outside 3-60% of 1412 measured; 198 = 14.0% (limit 5%) [list: benchmark-tx/txeng2/oracle1/sorter/cipher_lines.tsv]
PASS contact sheet: 24 tiles beside their line strips -> benchmark-tx/txeng2/oracle1/sorter/oracle_boxes_sorter.preflight.png (seed 20261006; eye it before publishing)
PASS colour: tokens, tints, box colours and person-facing text pass tools/cvd_check.py
preflight: FAIL
```
Two checks fail, for reasons the lane must decide (this worker changed no tool and no PREREG):
- **answerable** fails by construction: the PREREG requires one neutral pile `unsorted` and no focus; the preflight requires a
  non-empty focus box and >= 2 named piles. A blind box-verify page with no labels cannot satisfy both as the tools stand. Routes
  for the lane (not taken here): a declared box-verify mode in sorter_preflight.py with its own must-not-block test, or neutral
  named decision piles on the page -- either is a tool or PREREG change.
- **right line (shape)** 198 of 1412 tiles = 14.0% against a 5% limit: 62 "wide" against a median width pooled over three hands at
  different scales (39 px; per hand, against each hand's own median width, only 15 are over 2.5x: vivonne 11, luzerne 4, birago 0),
  21 strip-height boxes (this worker's own count by hand: birago 11, vivonne 9, luzerne 0), 136 ink outside 3-60% (mostly small dense boxes: the
  kept marks and narrow strokes, PREREG step 2 keeps them). These are the machine proposals' own bad cuts -- what the owner's
  check is for -- but the gate as written does not pass them.
Template PASS (Fix the cut present, marker 2026-10-09.4), contact sheet PASS (not eyed by this worker: read-free), colour PASS.

## Files (sha256)
```
1f2d0ba2451fdb6552b6c5895263a974d89a96bbcc2ec987060258dfc127f350  benchmark-tx/txeng2/oracle1/boxes/birago1572-no87/f178v_L01.tsv
af7f8c4361ea542e9db73584b0d579748c701d44f58cd2aa05c3be69d46b3148  benchmark-tx/txeng2/oracle1/boxes/birago1572-no87/f178v_L01_overlay.jpg
be607c5d4e195af1a09fb83dc12a0cbb2f08311b751227a5ed390535a560ca7c  benchmark-tx/txeng2/oracle1/boxes/birago1572-no87/f178v_L01_plain.jpg
1a04398805f7a918c706f0497519575ce3c2eeac28a61c31ac26f73dbcfeda27  benchmark-tx/txeng2/oracle1/boxes/birago1572-no87/f178v_L02.tsv
fe9cc3bb1d9aa76e848a6c902dc36dc22a7879329ad62346e86fb513d1d9e00e  benchmark-tx/txeng2/oracle1/boxes/birago1572-no87/f178v_L02_overlay.jpg
25f5e1a965ee4dd840df434f7abd39fbfaeb3c7ac408a95ece40b871fd6d362d  benchmark-tx/txeng2/oracle1/boxes/birago1572-no87/f178v_L02_plain.jpg
cd14ec44684e2821d2d0541a2710c630d6bbd2d9b1cdef31012d7bab3528962e  benchmark-tx/txeng2/oracle1/boxes/birago1572-no87/f178v_L03.tsv
d825d68128eabbdcd58fa944a92405675581a4246324686bc6d3ef1d977989e4  benchmark-tx/txeng2/oracle1/boxes/birago1572-no87/f178v_L03_overlay.jpg
6b03523e5051870457e5529104a749036ed265de8e2f63157e1591ba52128b7e  benchmark-tx/txeng2/oracle1/boxes/birago1572-no87/f178v_L03_plain.jpg
2ddf8e6df13756c7d3aca83b340c17f14c96b1df95f3e305795ceaeca5c81405  benchmark-tx/txeng2/oracle1/boxes/birago1572-no87/f178v_L04.tsv
452165e6cf481392fa1dc6ec032351f358db8a5a43b1b6fc1de141884c3d9ae2  benchmark-tx/txeng2/oracle1/boxes/birago1572-no87/f178v_L04_overlay.jpg
871b37a7373b0ad71ddf661f9dc36f2cfb1ecd44d9e6406c330930a39f62f536  benchmark-tx/txeng2/oracle1/boxes/birago1572-no87/f178v_L04_plain.jpg
9251de4bb4d8c0e48cb11087fd377df23837efd90a46aa0279f0bf788f3b5b17  benchmark-tx/txeng2/oracle1/boxes/birago1572-no87/f178v_L05.tsv
48dcc31ad3b806d338d052b98f16c17ef18b996edc17f1a6eaf1bcf056cc1e02  benchmark-tx/txeng2/oracle1/boxes/birago1572-no87/f178v_L05_overlay.jpg
84dac836f286cbafb7a11628357c203cac0a402cdce5024d8a5ce50867754057  benchmark-tx/txeng2/oracle1/boxes/birago1572-no87/f178v_L05_plain.jpg
8dfa3736135e4e2c41533889d1c5378a87f768e969e94680f20638f462eb1daa  benchmark-tx/txeng2/oracle1/boxes/birago1572-no87/f178v_L06.tsv
c034855841476af9191d0c21b1119cec7664dc683ac307fa38576fa2a367352f  benchmark-tx/txeng2/oracle1/boxes/birago1572-no87/f178v_L06_overlay.jpg
4a7b26b72a70cc7a6f2c9a6d2c4294d66607684ceab7bac70504eea4dd74a7c5  benchmark-tx/txeng2/oracle1/boxes/birago1572-no87/f178v_L06_plain.jpg
a82b5e8e2d45e30db625517cf9953132be71119b27f2dda9b674f8adfe2a2f16  benchmark-tx/txeng2/oracle1/boxes/birago1572-no87/f178v_L07.tsv
3ee8a59cfa546e6a80495b883514714024c1b265e27798a30a83621e9bcd95c6  benchmark-tx/txeng2/oracle1/boxes/birago1572-no87/f178v_L07_overlay.jpg
020a90fd0320bc3d2a350d5b224deba00b7677b6943d904bd4c501c29dfd5fc5  benchmark-tx/txeng2/oracle1/boxes/birago1572-no87/f178v_L07_plain.jpg
a227505977ee2b7ef7e25868911d4b2773b2f45ff02e9f981822f6663d4947ee  benchmark-tx/txeng2/oracle1/boxes/birago1572-no87/f178v_L08.tsv
9fbff37451bb39de55fb2feba92f9de0eb619f60fca49237d8314dff13e5ce47  benchmark-tx/txeng2/oracle1/boxes/birago1572-no87/f178v_L08_overlay.jpg
51da3cd31b03c6a1108d54e2cf3435967406dfd920bbd85c314f9964b6522724  benchmark-tx/txeng2/oracle1/boxes/birago1572-no87/f178v_L08_plain.jpg
ceb4c1d899f099e428b282629331beb10284def90dfc10c16bcbacd91d149bd9  benchmark-tx/txeng2/oracle1/boxes/birago1572-no87/f178v_L09.tsv
0d14febd325b7cdc39a75f144fefc725c79279b11b6c09d13204cdf3a16e78e5  benchmark-tx/txeng2/oracle1/boxes/birago1572-no87/f178v_L09_overlay.jpg
fba4ba9d82da8c388e7c3f5516a87694bc3545b882dadbb601cdd6ff3cd60671  benchmark-tx/txeng2/oracle1/boxes/birago1572-no87/f178v_L09_plain.jpg
77bfba6a5bf0a88a94d8daf925f3bcefe0cf35ea33d99e3f447f2674bd4172bc  benchmark-tx/txeng2/oracle1/boxes/birago1572-no87/f178v_L10.tsv
8129d652d713ac5b478b3f16c5717297ca24816bec05ded7840f8c97899648ec  benchmark-tx/txeng2/oracle1/boxes/birago1572-no87/f178v_L10_overlay.jpg
47f4c2107c968278d689af8493515949350add2de3a44a52bead854b71d69326  benchmark-tx/txeng2/oracle1/boxes/birago1572-no87/f178v_L10_plain.jpg
594084186e8a822de524801301797710ac0b2e3aadedce2bb2ff91670df55742  benchmark-tx/txeng2/oracle1/boxes/birago1572-no87/f178v_L11.tsv
bf78caa85f2fc216010c3c2cac85585dcd0e73b6d47511efba727f566ec8bd78  benchmark-tx/txeng2/oracle1/boxes/birago1572-no87/f178v_L11_overlay.jpg
3951cc1bdb6d43f327ed9b5167508076966ba1cf9ba10fa17431a3513286bd20  benchmark-tx/txeng2/oracle1/boxes/birago1572-no87/f178v_L11_plain.jpg
75d90437ca4426318c1ab80fed5dc8b15e2d6bad7e5b8138ecf965d409ddf09c  benchmark-tx/txeng2/oracle1/boxes/birago1572-no87/f178v_L12.tsv
d20fbd5f7b5105178b956cb14396556bc548a49d173f61f80e757ace66277d36  benchmark-tx/txeng2/oracle1/boxes/birago1572-no87/f178v_L12_overlay.jpg
3b4fa7ed5b76e343ea87817875321dfc543d61cc6423599700f14bb8e189e681  benchmark-tx/txeng2/oracle1/boxes/birago1572-no87/f178v_L12_plain.jpg
d0ebedb9f9e73807e9892ffc5dd9685c90390084a121b21ed236dec1fedbe001  benchmark-tx/txeng2/oracle1/boxes/boxes_all.tsv
fa366d7b52d86af5fe23b4624348a4e8d86aca7b67aa0692fb3b9ed0507bee65  benchmark-tx/txeng2/oracle1/boxes/counts.tsv
385264e0253f7fd2e24b740c732faf700f24f367693e62e45c5f6fc58cc35873  benchmark-tx/txeng2/oracle1/boxes/luzerne108a-p1/p1_L01.tsv
c8ca8ff290f8dbfed9fd345f01b8fb7ecef65f5357674937c14e94a5bda9df49  benchmark-tx/txeng2/oracle1/boxes/luzerne108a-p1/p1_L01_overlay.jpg
82833c9d4981518eafe14b36d2c7baa9ecd7e17fdfd2d66b675aa1cffa1a2f52  benchmark-tx/txeng2/oracle1/boxes/luzerne108a-p1/p1_L01_plain.jpg
931738a6261d329481eb9f9700cdcc0297d3487a0825774ffe16e1c9c2d9e7ad  benchmark-tx/txeng2/oracle1/boxes/luzerne108a-p1/p1_L02.tsv
24eaf7bac1d565f1dbf92dabbc87c228045711d385c5b037bb1ed128856b2bd4  benchmark-tx/txeng2/oracle1/boxes/luzerne108a-p1/p1_L02_overlay.jpg
cb2277a1cc3bd465b4a29ead6df012e013bef49fb96829b61ddb3755387de4fd  benchmark-tx/txeng2/oracle1/boxes/luzerne108a-p1/p1_L02_plain.jpg
3054f51d41d7d7349b1f0c26803f66504e7634cb4039eb8d7c2ba66702f3ca2b  benchmark-tx/txeng2/oracle1/boxes/luzerne108a-p1/p1_L03.tsv
cf4cb997af9fd21108fcef6825036b144c532bb19e546b37c261eb2d97983923  benchmark-tx/txeng2/oracle1/boxes/luzerne108a-p1/p1_L03_overlay.jpg
3aa272c6c8e92647974a4d1e3c206ecdb77f36cda6a10eb256e1a5a9e99e34da  benchmark-tx/txeng2/oracle1/boxes/luzerne108a-p1/p1_L03_plain.jpg
301683f1297984fbdf0bf64aa9b974715d980631bf34000f0852c806d9b8362d  benchmark-tx/txeng2/oracle1/boxes/luzerne108a-p1/p1_L04.tsv
f9f9d36b613c45b38221c74517234a27645a14565e999f885bfd1a83fc7e67c5  benchmark-tx/txeng2/oracle1/boxes/luzerne108a-p1/p1_L04_overlay.jpg
941abf9c981310c31bd13cb3f2ca1b74e9eb77134773c9352788124e841bc718  benchmark-tx/txeng2/oracle1/boxes/luzerne108a-p1/p1_L04_plain.jpg
0f1dbf719b6c15679d2b141880587c4d993f65e8683986cb994a9ff48708226b  benchmark-tx/txeng2/oracle1/boxes/luzerne108a-p1/p1_L05.tsv
1c9f3e15e55f738d5bc4a63b5c021f7296bc6072d7d63812ed1179f6206160ef  benchmark-tx/txeng2/oracle1/boxes/luzerne108a-p1/p1_L05_overlay.jpg
7c7d355f37dc4e5096f989c8d356d10f7e1c07b0804c246cad63cc70053011af  benchmark-tx/txeng2/oracle1/boxes/luzerne108a-p1/p1_L05_plain.jpg
3562f6bc7e2ab69e789f542875e5054f6cb79b4c7d123132ad912c22da566af9  benchmark-tx/txeng2/oracle1/boxes/luzerne108a-p1/p1_L06.tsv
4a4cdd1e7a7b082d53bb7211aa2209b877245dc3df9285389519ebd5c20d8154  benchmark-tx/txeng2/oracle1/boxes/luzerne108a-p1/p1_L06_overlay.jpg
38ac58b17daf02d627873aa0e47c3dd8503e15c6fc66de6901e8c5e326a7ea1e  benchmark-tx/txeng2/oracle1/boxes/luzerne108a-p1/p1_L06_plain.jpg
0fc65217805e82bf201c3dc3b5ae70f0683231d0784e6ab2785ad95a23ca2e1c  benchmark-tx/txeng2/oracle1/boxes/luzerne108a-p1/p1_L07.tsv
3ec9f373befbc55b77b18f838e9f06a1a4bdec92e1d1967d90587b1a469b6b72  benchmark-tx/txeng2/oracle1/boxes/luzerne108a-p1/p1_L07_overlay.jpg
6753c6a4a2494196be4f8e6b918348b50a468b52cd7ce25134f2b7a587925b9d  benchmark-tx/txeng2/oracle1/boxes/luzerne108a-p1/p1_L07_plain.jpg
db71dfaf0c8ef3b2d51a1bdf9ca8e398d9d8cbe254c0813982acf81202246e2c  benchmark-tx/txeng2/oracle1/boxes/luzerne108a-p1/p1_L08.tsv
f341e52785f0c4f53be439c69632ec084f00bd7a646b17a4e8727fe1cc2e9d18  benchmark-tx/txeng2/oracle1/boxes/luzerne108a-p1/p1_L08_overlay.jpg
6ec261e0c11649d89a76b550ebd95b3e731effa6c8a95eaa3a76453af64e77b8  benchmark-tx/txeng2/oracle1/boxes/luzerne108a-p1/p1_L08_plain.jpg
708abeab29aa8420a49df8aea46e2978d76773ca1c79be1c2a7ba390d251fa6e  benchmark-tx/txeng2/oracle1/boxes/luzerne108a-p1/p1_L09.tsv
ce8fd7b712859dd639ccc2a1068b17aeaf4fff6de7616d4c9b28dda094357864  benchmark-tx/txeng2/oracle1/boxes/luzerne108a-p1/p1_L09_overlay.jpg
d09fa2974751ed411828a1f4edbd6d6928b60928e8e404fc35b6b90c2ae3b18a  benchmark-tx/txeng2/oracle1/boxes/luzerne108a-p1/p1_L09_plain.jpg
18f8929510dc0249bf2e8364112d3ea1773bb680c9dec8473ae2633e15f40a67  benchmark-tx/txeng2/oracle1/boxes/luzerne108a-p1/p1_L10.tsv
a363f488a4b3b74a9b46fa73a478aa4b42f476885b28cc1236ed43a16d7013c6  benchmark-tx/txeng2/oracle1/boxes/luzerne108a-p1/p1_L10_overlay.jpg
5a7ae6f6c8f801ae188d166450b32362ee8a2687ea7b30be5bec4d908e0b997f  benchmark-tx/txeng2/oracle1/boxes/luzerne108a-p1/p1_L10_plain.jpg
c0769982fd5dc828782eea28dcb23677cb7e5adb9a0e938d557f14a08a3d3b35  benchmark-tx/txeng2/oracle1/boxes/luzerne108a-p1/p1_L11.tsv
77bf2fe673317cd4e731f7990c16edc6d525a0ac8fe15f27e918a75a078ddb02  benchmark-tx/txeng2/oracle1/boxes/luzerne108a-p1/p1_L11_overlay.jpg
50d5be24ee916a7a2973010762f64f3e730e839cbe5213f99d07431e8276dee3  benchmark-tx/txeng2/oracle1/boxes/luzerne108a-p1/p1_L11_plain.jpg
d27704f9b80ecc962faddc818094bfb7fd593205b7cdfac2bfee8f4699395394  benchmark-tx/txeng2/oracle1/boxes/vivonne1573-f102r/f102r_L03.tsv
ace393f4e67046ab1fde709fb081c4131aed4be2c923ff64d5fb5c966137bf58  benchmark-tx/txeng2/oracle1/boxes/vivonne1573-f102r/f102r_L03_overlay.jpg
1db228aed07b15745c8335dda48b4c1c86703fd6c6f483c1eb4d02c78262bf7d  benchmark-tx/txeng2/oracle1/boxes/vivonne1573-f102r/f102r_L03_plain.jpg
896de31e20f633a21339403917b8388adcd37a0e41912e0b45e95789fff270e8  benchmark-tx/txeng2/oracle1/boxes/vivonne1573-f102r/f102r_L06.tsv
58074cfa760a1a4822614d5792a5a2342338ebaeb9c5c12f60c70e4b5e75a902  benchmark-tx/txeng2/oracle1/boxes/vivonne1573-f102r/f102r_L06_overlay.jpg
36dfed82ee2fec2dff138c88cb8dd039420a803ceadf3d38c589e029a2afc536  benchmark-tx/txeng2/oracle1/boxes/vivonne1573-f102r/f102r_L06_plain.jpg
eee81f08461dea9ffc0262b586e1361ff333b3ac376ea8f6f6fcb2f205b634d3  benchmark-tx/txeng2/oracle1/boxes/vivonne1573-f102r/f102r_L09.tsv
e609542940e9b5b6a2888c7e0b429c32fbd58c6c52ae51d7266e2b321972e30c  benchmark-tx/txeng2/oracle1/boxes/vivonne1573-f102r/f102r_L09_overlay.jpg
f9d0186c40a5dfd1683ed6fa479ee6e3d4e8fdf20f0935ce95202813dd5622a1  benchmark-tx/txeng2/oracle1/boxes/vivonne1573-f102r/f102r_L09_plain.jpg
e898e3bd814ab5754e73806f09b94f49a8237c4c3db52d90327c6ea268022f25  benchmark-tx/txeng2/oracle1/boxes/vivonne1573-f102r/f102r_L11.tsv
ae7f2e907f6833a1d89eff919f9c63ea77e5d77c2fdaca567fb4dc61392c62e2  benchmark-tx/txeng2/oracle1/boxes/vivonne1573-f102r/f102r_L11_overlay.jpg
62900cf45a65a317c9a80f993cc9eac291e4ae414477f2fb816a894fc9ed6efc  benchmark-tx/txeng2/oracle1/boxes/vivonne1573-f102r/f102r_L11_plain.jpg
34cb28ad4d71fbf2380fcb52953c3350152b9c38ee351db17821c74d737bdacc  benchmark-tx/txeng2/oracle1/boxes/vivonne1573-f102r/f102r_L12.tsv
39ec6effa095837d47dfe135a23094c34579367e68cd303d35cacee9652148c5  benchmark-tx/txeng2/oracle1/boxes/vivonne1573-f102r/f102r_L12_overlay.jpg
6f42743c4892317679d2dd00570e09c77e8bb3106d372536fa2582426b77745d  benchmark-tx/txeng2/oracle1/boxes/vivonne1573-f102r/f102r_L12_plain.jpg
7d4da8343631edb4fd37970c1fa1cc51be4a9060245849204da8fd8554e9f988  benchmark-tx/txeng2/oracle1/boxes/vivonne1573-f102r/f102r_L15.tsv
05d512eeb4ee60654d81958898d58955ba30e3f05eac30fcde8fd946fa2a4219  benchmark-tx/txeng2/oracle1/boxes/vivonne1573-f102r/f102r_L15_overlay.jpg
04593f13756b9e96639665acefe3d9d6c9757e286f9daf1b702c7afcbb09cd2d  benchmark-tx/txeng2/oracle1/boxes/vivonne1573-f102r/f102r_L15_plain.jpg
41bfba69d0bb8544767125ca5fb945956cb920928cffa69e23786ccd1ac67106  benchmark-tx/txeng2/oracle1/boxes/vivonne1573-f102r/f102r_L17.tsv
74290da54a474b832aec4d6b693840b70a4e7c52c0a843371aaa41d858f9a320  benchmark-tx/txeng2/oracle1/boxes/vivonne1573-f102r/f102r_L17_overlay.jpg
74a9509cbf88aff731bdd67935c6e5d7973d0eca2fe23212167366c15166a506  benchmark-tx/txeng2/oracle1/boxes/vivonne1573-f102r/f102r_L17_plain.jpg
3a1d6d08d7188413fc230501c8657472e1ad02ca647d23652863118ad6d4ea11  benchmark-tx/txeng2/oracle1/boxes/vivonne1573-f102r/f102r_L21.tsv
d0d527b34c6d370ff033ea60cedc476ac77cdb167001a7b19a4ec1dffb3a1f75  benchmark-tx/txeng2/oracle1/boxes/vivonne1573-f102r/f102r_L21_overlay.jpg
e41d1c4be92ce6a11555e9906ffed20d00f3ae65e69d8761499b11110818145c  benchmark-tx/txeng2/oracle1/boxes/vivonne1573-f102r/f102r_L21_plain.jpg
074cfc5ff4e6ad7047bc4e594ef12828336b7331673578517945c8f6111d96d2  benchmark-tx/txeng2/oracle1/boxes/vivonne1573-f102r/f102r_L22.tsv
3b982dac68028424f323eed6ca720843cc05dc33ecade681ced007e94a22c50d  benchmark-tx/txeng2/oracle1/boxes/vivonne1573-f102r/f102r_L22_overlay.jpg
3da65a8b1df059ced74d6d7955661e749fff808fe1bef05ff90ea96ae1f26bce  benchmark-tx/txeng2/oracle1/boxes/vivonne1573-f102r/f102r_L22_plain.jpg
59dcdc95f6c36d8dcd3ad8c1945ff461a2631b83fbfa3fa5466fe1188278ea48  benchmark-tx/txeng2/oracle1/boxes/vivonne1573-f102r/f102r_L23.tsv
4df9f9c0998cb127e091766c8f596923535535c6327e7e49f31f47aa1c964797  benchmark-tx/txeng2/oracle1/boxes/vivonne1573-f102r/f102r_L23_overlay.jpg
310d86fe7b7c9b6895983a455727a34396fe63e54c6f4dba223e4ebdf3a8eafa  benchmark-tx/txeng2/oracle1/boxes/vivonne1573-f102r/f102r_L23_plain.jpg
a5790e09fecd59eaed863a5615cee34a7f2324ba721ceff5000db7cd8b56ba5f  benchmark-tx/txeng2/oracle1/boxes/vivonne1573-f102r/f102r_L26.tsv
336756864bfc0834e6f9642fc96aa03249bda9a9b90334754f1ea6939a7a14b5  benchmark-tx/txeng2/oracle1/boxes/vivonne1573-f102r/f102r_L26_overlay.jpg
89b71067faeae934fd056089cb78159aae1b6a1da01e84b1cdb9bd33527d900b  benchmark-tx/txeng2/oracle1/boxes/vivonne1573-f102r/f102r_L26_plain.jpg
553de9c40e447c959ded83a3a029f939c4b1f9cb2dc1b9b562fc41b58ae9dc54  benchmark-tx/txeng2/oracle1/boxes/vivonne1573-f102r/f102r_L27.tsv
787022db6994c4be746dfa0932db9334264a037370381345ef793300a85241c9  benchmark-tx/txeng2/oracle1/boxes/vivonne1573-f102r/f102r_L27_overlay.jpg
426f10fe1fa8904a31dd68c28dfc2d811e5f97c830c7e90b5b53affffd8bcefa  benchmark-tx/txeng2/oracle1/boxes/vivonne1573-f102r/f102r_L27_plain.jpg
ed5e8a911a9665cf4141f428f6a939421ece50b8e3b6d4c7d563ed57288034a8  benchmark-tx/txeng2/oracle1/build.sh
fec641a56ee25ec9a306a2e9b8b69a956e7b4424fd410dce4cb4eed0afde9c6c  benchmark-tx/txeng2/oracle1/build_ol1_boxes.py
9deeae0ccde1d1fd7fabd639903a30a2bed832cedb829d545e51b0e334286eef  benchmark-tx/txeng2/oracle1/sorter/cipher_lines.tsv
1ec95b6a8f7874b98b11af9eab6c868f621792ddf83e1cb7329bc329c124a6c6  benchmark-tx/txeng2/oracle1/sorter/labels.tsv
b35fda04a5cdf6bd1ebeecdd07c28341fb54ca814fb4d6a5399e71091fd82f61  benchmark-tx/txeng2/oracle1/sorter/oracle_boxes_sorter.html
8ccd62625fa231a4e6e34e272e7229422816effbb3e342bbb198cb1696321f37  benchmark-tx/txeng2/oracle1/sorter/oracle_boxes_sorter.json
7e81235a5611e00c89b31a332ba7b2ff725f5249cfa0ede95ada7f308adca29a  benchmark-tx/txeng2/oracle1/sorter/oracle_boxes_sorter.preflight.png
39aa7aac9cfea1cdd1a131bd6d9f70c99f5c8ab6e00c85117190bacabc4a1840  benchmark-tx/txeng2/oracle1/sorter/pages.json
f1f24d696f59ca449b6df55d90df8c5ae7912cd53a075426422d4aaa3f5c9ce7  benchmark-tx/txeng2/oracle1/sorter/signs.tsv
```

Folder total: 16M (under 30 MB). Commit hash: in the ROOM done line (this file is committed with the outputs).

Openings of eval truth: 0. No read, no truth, no pass opened. Nothing published: the orchestrator publishes, and only after the preflight question above is settled.

## OL1-PAGE (PREREG-txeng2-21 "OL1-PAGE amended", TXE2-OL1PAGE worker, account-4, Opus 5.5; 10 Oct 2026 02:59-03:0x UTC by date -u)

Read-free: no reader call, no vision call on any crop, no truth, no key, no decode, no pass output, no label from any read. Inputs:
the committed boxes/boxes_all.tsv and the crop images only. Step (i) of the original OL1-PAGE (a `--box-verify` mode) was withdrawn
by the amendment before any tool was touched: tools/sorter_preflight.py and its tests are unchanged.

**Re-cut** (`recut_ol1_boxes.py`, rules in its docstring, in the PREREG's order; medians per hand over kind=sign widths: vivonne 51 px,
birago 65 px, luzerne 11 px; every change a row of boxes/boxes_recut.tsv):
| rule | vivonne1573-f102r | birago1572-no87 | luzerne108a-p1 |
|---|---|---|---|
| (1) split over-wide (pieces) | 33 | 0 | 10 |
| (2) strip-height trimmed / dropped | 14 / 0 | 11 / 0 | 0 / 0 |
| (3) ink under 3% dropped | 0 | 0 | 0 |
| (3) ink over 60% padded 2 px | 16 | 11 | 48 |
| marks attached to a sign (--marks) / left alone (`mark box`) | 46 / 3 | 24 / 3 | 42 / 10 |
Page: 1,329 tiles (1,313 `sign box`, 16 `mark box`), 215 focus tiles with a geometric note only, lede = L74's instruction plus "The two
piles are only the machine's cut kind (a sign box, or a small mark with no sign in reach), not a reading."; seed note replaced as in
OL1-BOXES. 4.66 MB (under 16 MB).

**Plain preflight** (`python3 tools/sorter_preflight.py sorter/oracle_boxes_sorter.html --cipher-lines sorter/cipher_lines.tsv --pages-json sorter/pages.json`):
```
PASS template: ok, Fix the cut present, marker 2026-10-09.4
PASS answerable: 215 focus tiles, 2 named piles of 2, 0 unanswerable
FAIL right line: 1329 tiles; 0 tile(s) off the cipher lines, 71 of 71 listed lines have tiles; shape: 44 wide (>2.5x median 41 px), 9 strip-height boxes, 46 ink outside 3-60% of 1329 measured; 92 = 6.9% (limit 5%)
PASS contact sheet: 24 tiles -> sorter/oracle_boxes_sorter.preflight.png (seed 20261006)
PASS colour: tokens, tints, box colours and person-facing text pass tools/cvd_check.py
preflight: FAIL
```
cvd_check (`sorter_preflight.py --cvd` on the page): PASS colour: tokens, tints, box colours and person-facing text pass tools/cvd_check.py.

**STOPPED per the amendment** (shape still over 5% after the rules): no further rule improvised, no gate touched, nothing published.
Residual by class and hand (92 tiles = 6.9%; a tile can carry more than one class):
| hand | tiles | flagged | wide | strip-height | ink > 60% |
|---|---|---|---|---|---|
| vivonne1573-f102r | 541 | 40 (7.4%) | 31: 30 under 2.5x the HAND median (flagged only by the gate's POOLED median, 41 px), 1 widened past it by an attached mark | 6, all mark unions (a sign + its attached mark span the strip) | 4: 1 padded and still over; 3 under 60% by the re-cut's measure, over by the gate's (embedded JPEG) |
| birago1572-no87 | 343 | 21 (6.1%) | 13, all under 2.5x the hand median (pooled-median only) | 3, all mark unions | 11, padded and still over (2 with a mark) |
| luzerne108a-p1 | 445 | 31 (7.0%) | 0 | 0 | 31: 21 padded and still over (5 with a mark), 10 under 60% by the re-cut's measure, over by the gate's |
For the lane's decision (observations, not rules applied): 43 of 44 wide flags come from the gate pooling widths across hands where the
PREREG's rules are per hand; 9 strip-height flags are created by the --marks union, not by any sign box; 34 ink flags are small dense
glyphs a 2 px pad does not bring under 60% (luzerne's median width is 11 px), 13 more differ only between the crop and the embedded
JPEG measure.

sha256 (committed in the same commit as this section):
```
92eb9a7a5424cc64fef3397baf00ee1d78a6304718bcd24042a4df7419f8a591  sorter/oracle_boxes_sorter.html
9bad5ad205a21aea71d3961a4cd7e4758342ec15f8557f0fbfb92bab40ed2f79  sorter/oracle_boxes_sorter.json
e81262cb3055a42f9a5641b2c7e2a104dd3b45be5983ac5c186b71020742e457  sorter/signs.tsv
2d04145ff68529ad404d6ad198167efbd68fcdddaaa407268c7df99f01e6523d  sorter/labels.tsv
525c8eb881897619b10b6d1719e5c0330d0aa251260ce097eedf5517064efa1e  sorter/marks.tsv
fd7f1e6a09274bddd7906cd16b566e9ec7d55fefce9f2e561f69e9bc8272aa35  sorter/focus.tsv
81298643849f1bdcf32f6495830bb6acddfb6dbf9898389b36ab9aab31ce189f  boxes/boxes_recut.tsv
926241e24bc53bec24a0b2a9c5501f425b06680d4b187ed7380f5ed8a63a650e  boxes/boxes_recut_all.tsv
7079f30588f8162c989d50da2036e6b997d00d98f898940d2a71024f0ee0e1c7  recut_ol1_boxes.py
f146df0b3dcaf6da758ee045940d0eaab4be164abb0f9d1763f89a6bb405d57b  build.sh
```
Openings of eval truth: 0. No read, no truth, no pass opened.

## OL1-PAGE per hand (PREREG-txeng2-21 "OL1-PAGE, the next rule", da5f3d10a; TXE2-OL1PAGE worker, account-4, Opus 5.5; 10 Oct 2026 03:05-03:0x UTC by date -u)

Read-free, nothing re-cut: `split_per_hand.py` splits the re-cut inputs above into sorter/<hand>/ (signs, labels, marks, focus,
pages.json, cipher_lines.tsv); on the luzerne inputs only, EVERY box (all 445, sign and mark) is padded 4 px a side, clamped to its crop,
before the tile is cut and measured. Same piles, marks (--marks), focus notes and lede as the combined page (lede says "one hand"; title
"Oracle boxes (<hand>): verify the cuts"). Plain `tools/sorter_preflight.py <page> --cipher-lines sorter/<hand>/cipher_lines.tsv
--pages-json sorter/<hand>/pages.json`, gate untouched. Build: `build.sh` (last block).

**sorter/oracle_boxes_vivonne.html** -- 541 tiles, 99 focus, 2.29 MB -- preflight: PASS
```
PASS template: ok, Fix the cut present, marker 2026-10-09.4
PASS answerable: 99 focus tiles, 2 named piles of 2, 0 unanswerable
PASS right line: 541 tiles; 0 tile(s) off the cipher lines, 24 of 24 listed lines have tiles; shape: 1 wide (>2.5x median 51 px), 6 strip-height boxes, 4 ink outside 3-60% of 541 measured; 11 = 2.0% (limit 5%)
PASS contact sheet: 24 tiles -> sorter/vivonne/oracle_boxes_vivonne.preflight.png (seed 20261006)
PASS colour: tokens, tints, box colours and person-facing text pass tools/cvd_check.py
preflight: PASS
```
**sorter/oracle_boxes_birago.html** -- 343 tiles, 33 focus, 2.14 MB -- preflight: PASS
```
PASS template: ok, Fix the cut present, marker 2026-10-09.4
PASS answerable: 33 focus tiles, 2 named piles of 2, 0 unanswerable
PASS right line: 343 tiles; 0 tile(s) off the cipher lines, 36 of 36 listed lines have tiles; shape: 0 wide (>2.5x median 65 px), 3 strip-height boxes, 11 ink outside 3-60% of 343 measured; 14 = 4.1% (limit 5%)
PASS contact sheet: 24 tiles -> sorter/birago/oracle_boxes_birago.preflight.png (seed 20261006)
PASS colour: tokens, tints, box colours and person-facing text pass tools/cvd_check.py
preflight: PASS
```
**sorter/oracle_boxes_luzerne.html** -- 445 tiles, 83 focus, 0.89 MB -- preflight: PASS
```
PASS template: ok, Fix the cut present, marker 2026-10-09.4
PASS answerable: 83 focus tiles, 2 named piles of 2, 0 unanswerable
PASS right line: 445 tiles; 0 tile(s) off the cipher lines, 11 of 11 listed lines have tiles; shape: 0 wide (>2.5x median 19 px), 0 strip-height boxes, 12 ink outside 3-60% of 445 measured; 12 = 2.7% (limit 5%)
PASS contact sheet: 24 tiles -> sorter/luzerne/oracle_boxes_luzerne.preflight.png (seed 20261006)
PASS colour: tokens, tints, box colours and person-facing text pass tools/cvd_check.py
preflight: PASS
```
Counts match the lane's expectation from per-hand medians (vivonne 11/541, birago 14/343); luzerne 31 -> 12 of 445 after the uniform pad.
The combined page sorter/oracle_boxes_sorter.html (FAIL 6.9%, above) stays withheld. Folder benchmark-tx/txeng2/oracle1/ is 30 MB
(sorter/ 25 MB); the combined page + its JSON (9.6 MB) are the obvious thing to drop if the folder must shrink -- left for the lane.

sha256 (committed with this section):
```
5416ec4d798b90a7d37eedd982cdc81324af2b26d213a7c6b679735dcbf3cfd4  sorter/oracle_boxes_vivonne.html
741f38a735a17e85767e51ce77cf37c1de1d9c0c0fc0209fb61b34e79d5be593  sorter/oracle_boxes_birago.html
444292ea74e7ea43868265a68fcda0bbe8daa6559518c557fa0a41bd16079811  sorter/oracle_boxes_luzerne.html
eae68e3beeb72aa133194f06e6222471635d9ad03047e719ce3bb28004aadeca  sorter/vivonne/oracle_boxes_vivonne.json
ad3e4dddd49f79e39b048b802006ca6a78f6b0e34b1d3486b7f146930deb0baf  sorter/birago/oracle_boxes_birago.json
3b4cbb6ba639969c48fcea8cfef50558335bca2ac6c84e998a15a2f481085884  sorter/luzerne/oracle_boxes_luzerne.json
7a0e82d807f8c4b8cf6b33abd8a496a42a728040078aacf6f9a08303f6d88e9c  split_per_hand.py
60514db02a24178d2642ef8d005a708bce32af3028e7990dc860fae55356c839  build.sh
```
Openings of eval truth: 0. No read, no truth, no pass opened. Nothing published (the orchestrator publishes for L74).

## Combined page removed (lane incarnation 5, 10 Oct 2026 03:0x UTC by date -u)
The withheld combined page (sorter/oracle_boxes_sorter.html, its JSON and preflight PNG; FAIL 6.9% as recorded above) is removed from the
tree in this commit to keep the folder under 30 MB (30 -> 19 MB); it stays in git history (906d366fa and before) with its sha256 above. The
three per-hand pages are the pages of record for LOCAL-QUEUE L74; the orchestrator publishes each.
