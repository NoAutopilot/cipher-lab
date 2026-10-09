# TX-RECOVERY-PRACTICE: what document-recovery teams do with a faint scan (TXE-G, LANE TX-ENGINEER idea O5, 9 Oct 2026)

Worker TXE-G (account 4, Opus 5.5), 07:22-07:3x UTC by `date -u`. Brief `.claude/briefs/runs/2026-10-09-account4-txe-g.md`.
The owner asked (lane brief Amendment 1, item 5) what expert document-recovery teams do with a damaged or faint page, so
the lane can test their methods rather than reinvent them. Sources: 20 WebSearch queries (standard mode) on 9 Oct 2026,
logged at the end. Abstracts and documentation pages only: no paywalled full text was read, and every efficacy figure
below is the cited authors' own claim on their own data.

**One premise of the brief does not hold for our material.** The brief describes "RGB JPEG scans from Gallica". On disk,
every Birago 1572 family atlas page source is greyscale (PIL mode `L`, all 18 in `atlas/pages.json`), and the harvest
line crops are RGB files with R = G = B exactly (mean |R-G| = 0.0 on `harvest/f178v/f178v_L01_s1.jpg`; source
`gallica.bnf.fr/iiif/ark:/12148/btv1b9060248g/f182/.../native.jpg`). Whether Gallica holds a colour master for this ark
was not checked, because this brief allows no host. Until a colour fetch exists, every colour method below (channel
separation, decorrelation stretch, ICA/colour decorrelation for bleed-through) is a non-test on Birago no.87. That
includes TXE-D's `channel=R|G|B`, `sep` and `false` settings. Flagged in ROOM.md at 07:25 UTC.

## (a) Methods found

| # | method (family) | what it fixes | evidence (source, searched 9 Oct 2026) | runnable here on our scans (numpy/Pillow/OpenCV/skimage)? | code licence named |
|---|---|---|---|---|---|
| 1 | Global threshold (Otsu) | ink/paper split on even backgrounds | DIBCO comparisons: Otsu F 80.04 on DIBCO 2013 vs Sauvola 82.73 (arXiv 1901.09425) | yes (cv2) | OpenCV Apache-2.0 |
| 2 | Local threshold: Niblack | uneven background | worst of six on DIBCO 2013/H-DIBCO 2014, F 34.12 (arXiv 1901.09425; computeroptics.ru KO43-5) | yes (skimage) | skimage BSD-3 |
| 3 | **Local threshold: Sauvola** (window, k ~0.2-0.5) | faint strokes on uneven paper; the standard document baseline | second only to the proposed method on DIBCO 2013 (F 85.02, arXiv 1901.09425); k = 0.2, R = 128 original values, window must exceed stroke width, typical 15-31 (academia.edu 8088371 survey; MVTec HALCON local_threshold doc); stroke-width-adaptive window variant (kr.cup.edu.in 32116/2654) | yes (`skimage.filters.threshold_sauvola`) | BSD-3 |
| 4 | Wolf-Jolion (Niblack/Sauvola family, contrast-normalised) | low-contrast pages | named as a Niblack refinement; no DIBCO score found (Khurshid et al., DRR 2009, helios2.mi.parisdescartes.fr) | yes (about 15 lines) | n/a |
| 5 | Background-surface estimation + compensation (Gatos 2006; Lu-Su-Tan 2010; median-filter variant) | shading, stains, uneven light; the DIBCO 2009 winner estimates the background by iterative polynomial smoothing and then thresholds from stroke edges | Gatos et al., Pattern Recognition 39 (2006), DOI 10.1016/j.patcog.2005.09.010; DIBCO 2009 top of 43 (staff.fnwi.uva.nl HDIBCO.pdf); Su-Lu-Tan IEEE TIP 2013 (ieeexplore 6373726) | yes. **Already the atlas's own threshold**: `glyph_atlas.binarise` divides by a morphological-closing background (rel 0.78) | n/a |
| 6 | Laplacian-energy graph cut (Howe 2011/2013) | degraded handwriting; won H-DIBCO 2012, 2014, 2016, second in DIBCO 2013 (variants) | scholarworks.smith.edu csc_facpubs/127; Springer s10032-017-0283-9; IAPR ICFHR2014 H-DIBCO report | partly (needs a max-flow solver; PyMaxflow not installed; over 40 lines) | Howe's code: not checked |
| 7 | CNN/GAN binarisation (DIBCO 2017+) | everything above, learnt | arXiv 1708.03276 (FCN), 2010.10103 (two-stage GAN), 2007.07075 | no: needs downloaded weights | n/a |
| 8 | **CLAHE** (clip 2.0, 8x8 tiles) | local contrast on faint writing | handwritten Katakana ResNet-18, 89.75% -> 95.10% with CLAHE, clip 2.0 / 8x8 best (repository.upnjatim.ac.id 56515); in historical Arabic VLM pipelines without an ablation (aclanthology 2026.nakbanlp-1.43); "helps only marginally" for fine-tuned Qwen/Gemma (2026.nakbanlp-1.42) | yes (cv2.createCLAHE) | Apache-2.0 |
| 9 | Unsharp mask / sharpening | soft strokes | tested alongside CLAHE in the NAKBA VLM paper: marginal (2026.nakbanlp-1.42) | yes | n/a |
| 10 | **Stroke-width normalisation**: thin-only (adaptive), or multi-thickness ensembling | thin or uneven pen; recognition degrades strongly with stroke width (Arabic OpenHaRT) | multi-thickness test-time ensembling gave significant gains for HMM and BLSTM recognisers (researchportal.ip-paris.fr "stroke width exploitation"); thickness and intensity normalisation, 2-3% absolute (scholarhub.balamand.edu.lb uob/597); reliability-driven adaptive normalisation 60.8 -> 67.7 (uniform) -> 69.3% (adaptive) (kochi-tech.ac.jp a1070398) | yes (distance transform + dilation) | n/a |
| 11 | Recto-verso registration + bleed-through classification and inpainting (Savino and Tonazzini) | show-through from the verso | J. Cultural Heritage 19 (2016) 511-521, DOI 10.1016/j.culher.2015.11.005; patch-wise local registration (iris.cnr.it 20.500.14243/359135) | no: needs the verso image registered to the recto; neither is in the atlas, and verso fetches are a host job | n/a |
| 12 | Single-side bleed-through separation from colour channels: ICA, colour decorrelation, correlated component analysis (Tonazzini, Bedini, Salerno 2004-2012) | show-through, using the colour difference between recto and verso ink | iris.cnr.it 20.500.14243/152170; data.cnr.it ID217220 ("Restoration of historical RGB manuscripts via correlated component analysis") | **no on our files: greyscale** (needs colour) | n/a |
| 13 | Decorrelation stretch (Gillespie 1986; JPL; DStretch, Harman 2005) | faint pigment on a similar ground: spreads correlated bands | dstretch.com/AlgorithmDescription.html; Årsand 1: about 15 new figures (NASA spinoff page) | **no on our files: greyscale** | DStretch is closed-source (paid plug-in); the algorithm is public |
| 14 | Forensic colour separation: Lab, channel mixer, colour deconvolution (desired/undesired/background colours clicked) | crossing or obliterating inks; faint ink on a coloured ground | J Forensic Sci 2003 (store.astm.org jfs2002425) and 2006 (colour deconvolution); NCJRS 186090, 203520, 234411 | **no on our files: greyscale** | n/a |
| 15 | Multispectral imaging, UV fluorescence (UVL/UVR), IR (iron-gall ink vanishes in IR), RIS + PCA, micro-XRF for galled text | faded, erased or chemically damaged iron-gall ink | Knox and Easton (RIT); UCL Discovery 10196293; incipit.csic.es; Smithsonian archives forum; activehistory.ca 2018 | **no**: physical capture at the holding archive | n/a |
| 16 | Super-resolution: bicubic/LANCZOS; sparse-dictionary SR; GAN/Real-ESRGAN | low-resolution handwriting | sparsity SR improves HWR (isi.edu 11362); GAN 8x character SR (arXiv 1901.06199); Real-ESRGAN in a 2025 dissertation, with spurious-stroke artefacts (drepo.sdl.edu.sa) | interpolation yes (TXE-D's sr2/sr4); learned SR no (needs weights) | Real-ESRGAN BSD-3 (weights a download) |
| 17 | Skew, slant and line-bend normalisation (deskew, deslant, dewarp) | sloping lines, slanted script | CITlab's ICDAR2017 system: contrast enhancement *without binarisation*, then line bends, skew and slant (arXiv 1804.09943) | yes; crop geometry is TXE-B's (sloped bands) | n/a |
| 18 | HTR-pipeline input practice: Kraken (binarisation deprecated: "can often worsen text recognition results especially for ... faint writing"), PyLaia (fixed line height 128 px, grey), Transkribus (projects preprocess outside the platform) | n/a (practice) | kraken.re 5.3.0 advanced docs; doc.teklia.com/pylaia; zenodo 10451396 (TibSchol); aplicat.upv.es 294797 (binarisation keeping grey levels) | n/a | Kraken Apache-2.0; PyLaia MIT |
| 19 | Cipher-specific transcription practice: DECRYPT few-shot symbol recognition and clustering with manual correction of a few lines (TranscriptTool); Megyesi's transcription guidelines; Mary Stuart: 150,000 symbols transcribed, by the authors' account the most intensive step | n/a (practice) | arXiv 2107.10064; ep.liu.se ecp2020_171_008 and _014; diva-portal diva2:1437998 (guidelines, 10 Feb 2020); dspace.ut.ee Decrypt pipeline; Scientific American and National Geographic coverage of Lasry, Biermann and Tomokiyo 2023 (the Cryptologia text was not reachable) | the atlas + sorter already follow this shape (cluster, then a person settles) | n/a |

What the field converges on, as far as the abstracts show:
- On faint writing, binarisation is a known risk for *recognisers*. Kraken deprecates it; the CITlab ICDAR2017 system
  enhanced contrast without binarising; one line of work keeps grey levels for the HTR model.
- The robust classical binarisers (Gatos, Lu-Su-Tan, Howe) all start by estimating the background. Our atlas already
  does this.
- Colour, IR and UV recovery need capture we do not have.
- For thin strokes, the evidence favours adaptive (thin-only) normalisation or ensembling several thicknesses over
  thickening everything.

## (b) The three methods most applicable to our tiles

The proxy for all three (TXE-D's design, run here by `tools/tx_recovery.py proxy`):
- Every one of the 4,209 atlas boxes gets its 48x48 bitmap re-derived from its page under the setting. The boxes are the
  same, so the comparison is paired position by position.
- `glyph_atlas.py classify --topk 3` runs with all of no.87 held out (`--holdout f178r_ --holdout f178v_ --holdout f179r_`).
- The bench recipe is label-blind: dev_tune boxes per line in x order, `_` dropped, k1 as the sign.
- Scoring is `tx_bench.py --item birago1572-no87 --paired plain`, run only after the topk files were committed (becae9a4).
- Gate: fixed > broken, p < 0.01.

1. **Sauvola local binarisation** (DIBCO family; method 3).
   - Mechanism attacked: taxonomy class 3, thin strokes. A hairline gets a threshold from its own neighbourhood rather
     than from a page-wide ratio.
   - Recipe: `skimage.filters.threshold_sauvola`, window = odd(max(15, 0.5 x the page's median sign height)), i.e. 31-35
     px on f178v (median_h 68), k = 0.2. Ink = grey < threshold. Flag `--setting sauvola`.
   - Test: the proxy above. Cost: under a minute of CPU, no model call.
2. **CLAHE** (method 8).
   - Mechanism attacked: class 3, thin and faint strokes, through local contrast; it is also a grey rendering a reader
     could be shown without binarising.
   - Recipe: `cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))` on the grey page, then the atlas threshold (rel 0.78).
     Flag `--setting clahe`.
   - Test: the proxy. Note: the proxy sees CLAHE only through the binary mask it produces, not as a grey image.
   - Cost: under a minute.
3. **Adaptive stroke-width normalisation** (method 10, the thin-only variant).
   - Mechanism attacked: class 3, the d/s descender and p/t loop that vanish in hairline ink.
   - Recipe: after the atlas threshold, a box's stroke width = 2 x the median distance-transform value over its ink. A
     box under the page's median width is dilated once (3x3); the others are untouched. Flag `--setting swn`.
     (TXE-D's `thicken=1` is the uniform variant; the cited evidence favours the adaptive one.)
   - Test: the proxy. Cost: under a minute.

`tools/tx_recovery.py render --image IN --setting S --out OUT.png` gives each one as a reader-facing image (ink black on
white; CLAHE stays grey) for any later read the lane briefs.

## (c) Not applicable here, and why

- **Multispectral, UV-fluorescence, IR, RIS, micro-XRF** (method 15): physical capture at the BnF. Our input is one
  greyscale visible-light scan.
- **Colour methods** (12-14: ICA or colour decorrelation for bleed-through, decorrelation stretch, Lab or colour
  deconvolution, channel mixing): the scans on disk are greyscale. They become testable only if a colour master is
  fetched for btv1b9060248g (a host job for the lane, if Gallica serves one).
- **Recto-verso bleed-through removal** (11): needs the verso leaf registered to the recto. That is a fetch plus a
  registration job; the taxonomy does not name bleed-through as an error class on no.87.
- **Learned binarisation and learned super-resolution** (7, 16 learned): need pretrained weights this container cannot
  download offline (and none is installed). Interpolated super-resolution is TXE-D's `sr2`/`sr4`.
- **Howe graph cut** (6): implementable, but needs a max-flow library (not installed) and more than 40 lines. Its gain
  over Sauvola on DIBCO comes on stains and heavy degradation; the atlas's background normalisation already covers part
  of that ground.

## RESULTS (read-free proxy, dev_tune f178v L01-12, 343 scored; commit becae9a4 before scoring, 07:28 UTC)

All four settings use the same 4,209 boxes re-derived by the tool, with no.87 held out. The `stored` row is the atlas's
own bitmaps, for reference.

| setting | err_true dev_tune | wrong / deleted / inserted | paired vs plain: fixed / broken, p | gate (p < 0.01) |
|---|---|---|---|---|
| stored (atlas bitmaps, reference) | 0.192 (66/343) | 43 / 19 / 4 | 7 / 3, p 0.34 | n/a |
| **plain** (control, re-derived) | 0.204 (70/343) | 49 / 17 / 4 | n/a | n/a |
| sauvola | 0.210 (72/343) | 51 / 18 / 3 | 7 / 10, p 0.63 | FAIL |
| clahe | 0.394 (135/343) | 89 / 38 / 8 | 4 / 65, p < 0.0001 against | FAIL (harmful) |
| swn | 0.204 (70/343) | 47 / 19 / 4 | 3 / 3, p 1.00 | FAIL |

Raw `tx_bench.py` lines are in `benchmark-tx/txeng/recovery/RESULTS.md`.

- **Sauvola and adaptive stroke-width normalisation do not change what the atlas reads** (7/10 and 3/3, inside noise).
  The top confusion (s <- T50 x7) is untouched by both: the d/s pair is a shape-inventory problem (class 1), not an ink
  problem the threshold can fix.
- **CLAHE with the atlas threshold is clearly harmful** (65 broken vs 4 fixed). Equalising each 8x8 tile lifts paper
  texture and bleed into "ink" under a ratio threshold. That is consistent with the literature's warning that contrast
  steps help mostly after train-time adaptation (NAKBA 2026). It says nothing about how a vision reader would see a
  grey CLAHE image, which the proxy cannot measure.
- Limit of the proxy: HOG on a 48x48 binary bitmap sees a rendering only through its binary mask. A pure contrast or
  gamma change reaches it only through the threshold.

**Recommendation for the single read: none of the three.** No method passed the proxy gate, and the gate is the lane's
rule for earning a read. If the lane wants one grey-rendering read despite the proxy's blindness to contrast, the
literature points to a grey (not binarised) rendering: TXE-D's `stretch` or `gamma` fit that better than any setting
here, and Kraken's own advice is not to binarise faint writing. The binarised settings here (sauvola, swn) moved nothing
read-free.

Follow-up, one line: a colour master of btv1b9060248g, if Gallica serves one (a host check the lane can brief), is the only
thing that would make the colour half of this literature testable.

## Search log (WebSearch, standard mode, 9 Oct 2026, 07:22-07:24 UTC by date -u; pages named are the ones cited)

1. "Sauvola Niblack Wolf binarization historical handwritten documents comparison DIBCO": arxiv.org/pdf/1901.09425; computeroptics.ru/KO/PDF/KO43-5/430516.pdf; helios2.mi.parisdescartes.fr/~vincent/articles/DRR_nick_binarization_09.pdf; lme.tf.fau.de/?p=25926
2. "Howe binarization Laplacian energy graph cut DIBCO winner document image": scholarworks.smith.edu/csc_facpubs/127; link.springer.com/doi/10.1007/s10032-017-0283-9; iapr.org/archives/icfhr2014/.../ICFR2014-H-DIBCO.pdf
3. "bleed-through removal RGB scan recto verso historical manuscript method": publications.cnr.it/doc/345617 (DOI 10.1016/j.culher.2015.11.005); iris.cnr.it/handle/20.500.14243/359135; ercim-news.ercim.eu/en111/special/restoration-of-ancient-documents-using-sparse-image-representation
4. "faded iron gall ink enhancement RGB image channel decorrelation stretch principal component palimpsest": discovery-pp.ucl.ac.uk/id/eprint/10196293; repository.rit.edu/theses/7957; siarchives.si.edu/.../help-making-documents-more-legible; cool.culturalheritage.org/byform/mailing-lists/cdl/2004/1310.html
5. "forensic document examination faded ink digital enhancement color channel separation scan": store.astm.org/jfs2002425.html; ojp.gov/ncjrs/virtual-library/abstracts/color-separation-forensic-image-processing; activehistory.ca/2018/09/recovering-contrast-in-faded-documents/
6. "Transkribus preprocessing image enhancement binarization handwritten text recognition input": zenodo.org/records/10451396; aplicat.upv.es/exploraupv/ficha-publicacion/publicacion/294797
7. "Kraken eScriptorium binarization nlbin preprocessing grayscale recognition": kraken.re/5.3.0/_sources/advanced.rst.txt; kraken.re/5.2/api.html
8. "DECRYPT project cipher image transcription symbol recognition few-shot ...": arxiv.org/pdf/2107.10064; ep.liu.se/ecp/171/008/ecp2020_171_008.pdf; dh-abstracts.library.virginia.edu/works/3905
9. "Lasry Biermann Tomokiyo 2023 Mary Stuart cipher letters transcription method Cryptologia": scientificamerican.com/article/scientists-decipher-50-letters-...; on.natgeo.com/3KsKpqI (press only; the paper was not reached)
10. "background estimation normalization degraded document image contrast compensation Lu Su Tan binarization": eejournal.ktu.lt/index.php/elt/article/view/20982; journals.utm.my/jurnalteknologi/article/download/6668/4397/18363; cedar.buffalo.edu/~zshi/Papers/segmentation.pdf
11. "CLAHE contrast enhancement historical document handwriting recognition improvement evaluation": repository.upnjatim.ac.id/56515/5/22081010058-bab5.pdf; aclanthology.org/2026.nakbanlp-1.43.pdf; hal-univ-bourgogne.archives-ouvertes.fr/hal-01858390
12. "super-resolution low resolution handwritten text recognition improves accuracy ...": isi.edu/results/publications/11362; arxiv.org/pdf/1901.06199; drepo.sdl.edu.sa/items/857de394-39ad-4e60-8d72-6723359a0005
13. "stroke width normalization handwriting recognition morphological dilation thin strokes preprocessing": researchportal.ip-paris.fr/en/publications/stroke-width-exploitation-to-improve-automatic-recognition-of-ara/; scholarhub.balamand.edu.lb/handle/uob/597; kochi-tech.ac.jp/library/ron/pdf/2006/03/44/a1070398.pdf
14. "vision language model OCR image preprocessing binarization hurts or helps handwritten ...": arxiv.org/pdf/2608.22366; aclanthology.org/2026.nakbanlp-1.42.pdf; arxiv.org/pdf/2008.02777
15. "pseudo multispectral RGB document image ink separation independent component analysis bleed-through Tonazzini": iris.cnr.it/handle/20.500.14243/152170; data.cnr.it/.../ID217220; faculty.iiit.ac.in/~anoop/papers/Shrikant2013Ink-Bleed.pdf
16. "Gatos Pratikakis Perantonis adaptive degraded document image binarization background surface estimation Wiener": datalearner.com/.../paper-detail/98741 (DOI 10.1016/j.patcog.2005.09.010); comengapp.unsri.ac.id/index.php/comengapp/article/view/21
17. "DStretch decorrelation stretch rock art faint pigment RGB enhancement method Harman": dstretch.com/AlgorithmDescription.html; nasa.gov/technology/tech-transfer-spinoffs/nasa-technique-for-manipulating-satellite-photos-now-reveals-ancient-images
18. "PyLaia preprocessing image height normalization grayscale line images HTR Teklia": doc.teklia.com/pylaia/usage/datasets/; arxiv.org/pdf/2404.18722
19. "Copiale cipher transcription symbol inventory image Knight Megyesi ..." and "Megyesi transcription of historical ciphers guidelines DECODE ...": su.se/.../the-copiale-cipher; diva-portal.org/smash/get/diva2:1437998/FULLTEXT01.pdf; ep.liu.se/ecp/171/014/ecp2020_171_014.pdf; dspace.ut.ee/items/04bdeacd-5298-4e4d-a45a-8049779821de/full
20. "Lu Su Tan document image binarization stroke edge detection DIBCO 2009 winner local contrast": staff.fnwi.uva.nl/s.karaoglu/HDIBCO.pdf; ieeexplore.ieee.org/document/6373726
21. "Sauvola window size k parameter choice stroke width historical document skimage threshold_sauvola": scikit-image.org/docs/stable/auto_examples/segmentation/plot_niblack_sauvola.html; mvtec.com/doc/halcon/2211/en/local_threshold.html; kr.cup.edu.in/handle/32116/2654
22. "ICDAR 2017 competition handwritten text recognition READ dataset historical preprocessing contrast normalization slant": arxiv.org/pdf/1804.09943 (CITlab); zenodo.org/record/835488

No code was copied from any source; every flag is implemented from the method's published description.
