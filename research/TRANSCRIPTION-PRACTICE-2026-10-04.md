# How expert transcribers work, and what our pipeline lacks (research note, 4 Oct 2026)

Written 4 Oct 2026, about 03:05 UTC, by a research subagent for the owner's question: what do palaeographers,
documentary editors, cipher historians and HTR researchers actually do with difficult manuscripts and cipher
documents, what could we add, and would a 3D model of a page help a vision model? Compared against
TRANSCRIPTION.md (3 Oct 2026), LESSONS.md ("Settle the alphabet before reading", "Look-alike pass"),
`.claude/briefs/transcription.md` and the docstrings of `tools/iiif_lines.py`, `reconcile_passes.py`,
`lookalike_pass.py`, `sign_sorter.py` and `glyph_atlas.py`. Research only: no other repository file was changed.
Every source in the table was opened in this session unless it is marked *(memory)*. Sources that would not open
are listed at the end.

## Summary

1. **Our weakest point is that our readers make the same mistakes.** Editors key a text twice by *different
   people* and then proofread it against the original (MLA CSE; Guide to Documentary Editing). Our two "independent"
   passes are the same model reading the same crop. LESSONS.md "Look-alike pass" found that half the wrong signs on
   no.87 had both readers agreeing on them, so reconciliation never flagged them. One 2025 study of multimodal LLMs
   reading historical records (arXiv 2509.09722) got its best consensus from views of the page that made the
   readers' errors *least correlated*, not from the views each reader read best.
2. **Nothing checks the signs both readers agree on.** Editors proofread the finished transcription against the
   source, and team proofreading is the preferred method. Every one of our later steps (reconcile, look-alike,
   sorter focus) looks only at disagreements or known confusion pairs.
3. **Cipher transcribers write down their doubts as alternatives.** The DECRYPT guidelines (Megyesi 2020) say to
   write an unsure sign as `0/6?`, and TEI has `<unclear cert>` and `<choice>`. Our passes give one label plus
   H/M/L. TX-DECODE found that only 27 of 97 errors on no.87 have the true sign anywhere in the lattice, so the
   key-constrained decode has nothing to pick from in most cases.
4. **Palaeographers learn the hand from the document itself.** They build an alphabet from words they can already
   read and compare each hard letter with its secure occurrences (Northumberland Archives guide). We do this at the
   level of the atlas and clusters. The line-read passes, which are still our best readers (0.040 against the
   atlas's 0.162 on no.87), do not get a sheet of this hand's own variant forms taken from secure positions.
5. **Our fixed-protocol standard is already close to the field's best practice.** We have a known-answer benchmark,
   SER as an edit-distance count with Wilson intervals, clustering with human naming, and a person deciding "same
   sign or not". Published cipher HTR scores worse than our line reads: few-shot detection reaches SER 0.10-0.15 on
   seen ciphers and 0.75 on an unseen one (Magnifico and Megyesi). We should not adopt a trained detector.
6. **3D: no.** A 3D model built from one diffusely lit 2D scan contains no information that is not already in the
   pixels. Real multi-angle methods (RTI, raking light, multispectral) need the physical leaf under several captures.
   The cheap version that does help is several views of the same pixels (scale, padding shift, contrast or
   decorrelation stretch, small warp), each read separately and then voted.

## Practices compared with ours

| # | Practice | Who does it (source opened) | Do we already do it? (our file) | Proposed addition | Expected gain | Cost / effort |
|---|---|---|---|---|---|---|
| 1 | **Double keying by different people, then a computer diff** | MLA CSE guidelines: "inputting the same text twice, by two different people" then software finds the differences (https://www.coverpages.org/mlaGuidelines970812.html). Eleanor Roosevelt Papers: "Each document is transcribed independently by two different editors. Computer comparison ... identifies letters ... that demand special attention" (https://gde.upress.virginia.edu/04-gde.html) | Partly. We run two blind passes and `reconcile_passes.py`. But they are the same model family on the same crop, so their errors are correlated (LESSONS.md "Look-alike pass": half the wrong signs had two readers agreeing) | Make the readers different: different views of the crop and/or different model tiers (see #10), and measure how correlated their errors are | High. This attacks the error class the pipeline cannot see today | Low to medium: a few more cheap passes, plus an option in `reconcile_passes.py` |
| 2 | **Proofread the finished text against the original, by someone other than the transcriber** | MLA CSE: "double-checked and perfected by persons other than the transcriber". Guide to Documentary Editing ch. 6: oral team proofreading, where one person reads the source "word for word (or letter for letter in an old-spelling edition)"; "team proofreading is a more effective insurance against error than visual collation" (https://gde.upress.virginia.edu/06-gde.html) | No. Reconcile, look-alike and the sorter focus all start from disagreements or known confusion pairs. The agreed signs are never re-checked | A verification pass over **agreed** signs: show the crop sign by sign next to the tiles of the reconciled reading. To guard against confirmation bias, plant known errors and report the catch rate (see Top 5 #2) | High if the catch rate on planted errors is real. LESSONS.md shows a re-read that sees its answer tends to confirm it (9 of 11 wrong labels confirmed) | Medium: one pass per leaf plus a planted-error control |
| 3 | **Write uncertainty down as alternatives, not only as a confidence level** | Megyesi, "Transcription of Historical Ciphers and Keys", HistoCrypt 2020: "Uncertain symbols are transcribed with added question mark '?' ... Possible interpretations of a symbol can be transcribed using the delimiter '/'. For example ... '0/6?'"; "all symbols are transcribed somehow, and no symbols are left out" (https://ep.liu.se/ecp/171/014/ecp2020_171_014.pdf). TEI `<unclear reason cert>` ("eccentric_ductus" is a listed reason) (https://tei-c.org/release/doc/tei-p5-doc/en/html/ref-unclear.html); `<choice>` "groups a number of alternative encodings for the same point" (https://tei-c.org/release/doc/tei-p5-doc/en/html/PH.html) | Partly. Passes write H/M/L and a trailing `?` (`reconcile_passes.py` REC-CONF). The atlas gives top-3 (`glyph_atlas.py classify --topk 3`), but line reads, our best reader, give one label. TRANSCRIPTION.md row 5: only 27 of 97 errors have the true sign in the lattice | Pass prompts must write `a/b?` whenever the reader hesitates; `reconcile_passes.py` keeps every alternative into the lattice that `key_decode_lattice.py` reads | Medium to high for the decode. It raises how often the truth is in the lattice, which caps everything TX-DECODE can do | Low: a prompt rule plus a parser change |
| 4 | **Build the hand's alphabet from secure words before the hard passages** | Northumberland Archives guide: treat "the document you are transcribing as the definitive tool to establish letter forms"; find "already-transcribed words to help decode unfamiliar letter forms"; leave hard words and "Come back to it at the end" (https://northumberlandarchives.com/learn/decoding-manuscripts/handy-hints-guide/) | Partly. Atlas clusters are named from known answers first (TRANSCRIPTION.md pipeline step 4), and the sorter has a context view. Line-read passes get a key or atlas sheet, but not a sheet of *this hand's* variant forms from secure positions | An exemplar sheet per hand: for each sign, 4-6 tiles from H/C-graded positions (clerk sheet, gloss, H tokens) in the same family, chosen to show the variation, never from the eval leaf | Medium. Aims at confusions such as d<-T98 and s<-T50 on no.87 | Low to medium: an option in `glyph_atlas.py atlas` |
| 5 | **Read the whole document, use context, come back later** | Northumberland guide (above); Megyesi 2020 says transcription "shall reflect the intention of the encoder" and margin corrections are moved into place | Yes, in our own form. The key-constrained decode (`key_decode_lattice.py`) and the brief's gloss check do this. One open caution: the lam=1 decode *raised* err_true on no.87 | None new. Keep the pre-registered lam rule | -- | -- |
| 6 | **Uniform, explicit conventions and metadata, including method and time spent** | Megyesi 2020: metadata records "the approximate time it took to transcribe the image along with the transcription method so we can compare various methods"; conventions for spacing, catchwords, cleartext `<CLEARTEXT LANG ...>`, decrypted plaintext `<PLAINTEXT ...>`, `<ABBR ...>`. Transkribus: ground truth must use "uniform transcription conventions" (https://blog.transkribus.org/en/how-to-improve-the-cer-of-your-model) | Mostly. TRANSCRIPTION.md target 8 is cost per 100 signs, but only two jobs ledger a sign count. Glosses: the CLAUDE.md rule 3 PX-BRODEC lesson (normalise abbreviations before diffing) | Every pass file carries a header (`# method: model, view, prompt-id, sheet-id; signs; cost`) so that views and models can be compared later | Low directly. It makes every other comparison possible | Very low |
| 7 | **Abbreviation tables for clear glosses** | Cappelli online, Ad fontes (Zurich): "all 14'357 abbreviations included in the Cappelli", searchable "by visual criteria" with wildcards (https://eadh.org/node/810) | No. The ceppo f.36v gloss benchmark is our worst item (err 0.31-0.44 on 16 signs). It is an Italian clerk's hand with abbreviations | Gloss reads are semi-diplomatic: the reader writes the abbreviated form plus an `<ABBR expansion>` (Megyesi's tag), checking Cappelli or a period hand table *(Cappelli use for 16th-c. Italian/French secretary hands: memory, not tested here)* | Medium on gloss items only | Low |
| 8 | **Ground truth: perfect, consistent, and added where the model fails** | Transkribus: training data "should be 100% accurate"; single hand 15-30 pages for CER <5%; "add more pages where the model struggles" (search summary of https://www.transkribus.org/character-error-rate-cer-explained, not opened; the opened page is https://blog.transkribus.org/en/how-to-improve-the-cer-of-your-model) | Partly. BENCHMARK-TX.tsv has one eval item (no.87, 803 signs) and dev items; Dinteville f.128r (0.19-0.35) is the clear "struggles" hand | Every new hand gets a small known-answer item from its first secure span (gloss, clerk copy, H tokens) before line reads are priced. Adoption decisions use a **paired** test on the same signs (discordant counts, McNemar), not two overlapping Wilson intervals | Indirect but large. With one eval item, most proposed changes cannot clear their own CI | Low per item |
| 9 | **Few-shot symbol detection / clustering HTR for ciphers** | Magnifico and Megyesi, "Lost in Transcription of Graphic Signs in Ciphers" (HistoCrypt): SER clustering 0.638/0.350/0.800, few-shot 0.150/0.104/0.754 (Borg/Copiale seen, Ramanacoil unseen). Few-shot needs 10 support examples per sign, hand line cropping (~2 min per line) and a GPU (https://ecp.ep.liu.se/index.php/histocrypt/article/download/403/361). Souibgui et al. 2020 (arXiv 2009.12577, abstract only opened). DECRYPT pipeline 2024 notes "challenges with the accuracy of automated transcription" and "the necessity for significant user involvement" (https://dspace.ut.ee/items/04bdeacd-5298-4e4d-a45a-8049779821de/full) | We already do better on our hands. no.87 reconciled is 0.053, single pass 0.069. Their recommended combination (automatic segmentation + corrected clusters + few-shot) is what `glyph_atlas.py` + sorter already are | Do not adopt a trained detector. Only take their note that clustering breaks on cursive, which matches our RUN1-SEG `--cursive` work | -- | -- |
| 10 | **Ensembles and test-time augmentation with character-level alignment voting** | Improving MLLM historical record extraction with test-time image augmentations (arXiv 2509.09722; Gemini 2.0 Flash): padding shift, resize 30-130%, blur, noise, grid warp, and temperature. Outputs aligned with Needleman-Wunsch and voted per character, giving per-character confidence. CER 9.0% -> 7.2% (10 samples). Padding was best (7.4%). Grid warp was individually worst (12.4%) but gave a strong consensus (8.0%) because it had the "lowest error correlation (0.575)" (https://ar5iv.labs.arxiv.org/html/2509.09722). Classical HTR: ROVER voting over several recognisers (LV-ROVER, https://arxiv.org/pdf/1707.07432, search summary only) | Partly. `reconcile_passes.py` already uses NW alignment, but for at most 3 passes, with the passes as equals and no vote share | `reconcile_passes.py` takes N passes and writes a vote share per sign. A view generator makes the crops differ (see Top 5 #1) | Medium to high: the MLLM study's relative CER cut was about 20% | Low to medium: each view is one more cheap pass |
| 11 | **Image enhancement: decorrelation stretch / alternative colour spaces** | Tonazzini 2010, "Color space transformations for analysis and enhancement of ancient degraded manuscripts": colour spaces from "the decorrelation of the original RGB channels" improve "text readability" (https://iris.cnr.it/handle/20.500.14243/63765). DStretch is the ImageJ implementation (search summary, CAA proceedings link not opened) | No. Only `glyph_atlas.py --cursive`'s ghost floor and the sorter touch pixel values | `iiif_lines.py --enhance dstretch,clahe,sauvola` writes extra crop variants beside the plain ones, to use as voting views (#10) and in the sorter's context view | Low on clean Gallica scans. Medium on faded or stained leaves | Low (numpy only) |
| 12 | **Bleed-through removal using the registered verso** | Savino and Tonazzini 2016, "Digital restoration of ancient color manuscripts from geometrically misaligned recto-verso pairs" (J. Cultural Heritage, doi 10.1016/j.culher.2015.11.005): register recto with the mirrored verso, then find and inpaint bleed-through pixels (https://iris.cnr.it/handle/20.500.14243/312138) | No. `glyph_atlas.py --cursive` uses a single-image ghost threshold. The IIIF manifest already gives us the verso canvas for free | `iiif_lines.py --verso-canvas N`: fetch the verso once, mirror it, register by patch cross-correlation, and write a crop with bleed-through suppressed | Medium on bleed-through leaves (the R9528 DECODE hand) | Medium |
| 13 | **Raking light, RTI, multispectral imaging** | Cultural Heritage Imaging: RTI needs "multiple digital photographs ... from a stationary camera position" with light "from a different known, or knowable, direction" (https://culturalheritageimaging.org/Technologies/RTI/). Archimedes Palimpsest: a "stack" of images at different wavelengths, then algorithms (https://archimedespalimpsest.org/about/imaging/) | Not possible: no physical access | Ask the holding archive (REQUEST.md) only for a named leaf whose reading is blocked by fading, erasure or overwriting | High for that one leaf. Zero otherwise | Owner's time and money |
| 14 | **Work at several magnifications** | Palaeographic habit *(memory)*. The Northumberland guide's "block out all the other letters" is the zoom-in half | Partly. The sorter has tile plus context view. Line reads see one scale (`iiif_lines.py` caps width at 2400 px) | A scale-0.7 and a scale-1.3 view as voting views (#10), plus the sign tile in the verification pass (#2) | Folded into #10 | -- |

## The 3D idea: verdict

**It does not help with our material, and we should not build it.** Reasons:

- **What real multi-angle imaging needs.** RTI and photometric stereo get surface shape from *several photographs
  taken under different light directions* with a fixed camera (Cultural Heritage Imaging, above). Raking light is
  one physical capture at a low angle. Multispectral imaging is a stack of captures at different wavelengths
  (Archimedes Palimpsest, above). All three need the leaf in front of a camera. We have one IIIF image per side,
  shot under even copy-stand lighting, which is designed to remove shading.
- **A synthetic 3D model adds no information.** A depth map or mesh made from one image (monocular depth networks,
  shape-from-shading *(memory: general computer-vision knowledge, no paper opened)*) is a guess drawn from the
  network's priors about how scenes usually look. On a flat-lit scan of ink on paper, the "relief" it produces is
  a function of the grey levels already in the image. Turning that model to another angle and rendering it shows
  the same pixels distorted, plus invented geometry. It cannot reveal an indentation, an erased stroke or a
  pen-pressure difference that the camera did not record. At worst it adds plausible-looking artefacts that a
  vision model may read as strokes.
- **The one case where relief matters**, blind-stylus ruling, scratched-out signs or overwritten corrections, needs
  a physical capture by the archive. That is a REQUEST.md item for a named leaf, not a software step.
- **What does help, cheaply: several views of the same pixels, voted.** This is the honest form of "let the model
  look from different angles". Each view is a different presentation of the same information: padding shift,
  rescale 0.7x/1.3x, a small rotation (+-2 degrees) or mild grid warp, decorrelation stretch or CLAHE, a binarised
  copy. A vision model's mistakes depend on the presentation, so reading each view separately and voting by
  aligned character cancels part of the error. The MLLM study above measured this: CER 9.0% -> 7.2%. Its key
  finding for us is that the most useful views were the ones whose errors were least correlated with the others,
  not the ones read best alone. An "embossed" or hill-shaded rendering of ink density is allowed as one more such
  view, but it is a photometric filter, not 3D. Large rotations hurt reading and should not be used *(memory)*.

## Top 5 additions, ranked (expected gain per unit of cost)

Every test is scored with `python3 tools/tx_bench.py OUT.tsv --bench BENCHMARK-TX.tsv` on the **eval** item
birago1572-no87 (reconciled baseline err_true 0.053, CI 0.040-0.071; single pass A 0.069). Each is also reported as
a **paired** comparison on the same scored signs: count the signs right before and wrong after, and wrong before and
right after. The Wilson intervals of the two runs overlap at this size. Each test also states its cost per 100 signs
(TRANSCRIPTION.md target 8). Nothing is tuned on no.87, so tuning happens on the dev items, per BENCHMARK-TX.tsv's
own rule.

1. **Decorrelated multi-view voting.** Add a `--views pad,s70,s130,dstretch,warp` option to `tools/iiif_lines.py`
   that writes view variants of every crop, as per-view crop sets with manifest entries. Extend
   `tools/reconcile_passes.py` to take N passes (now at most 3) and write `vote_share` per sign plus an
   `err_corr` summary: the share of one pass's errors that another pass repeats, measured on dev items. Run one
   cheap blind Sonnet pass per view and add one pass from a different model tier, then vote.
   *Test:* on no.87, the N-view vote beats the reconciled 0.053 at no more than 2x the current cost per 100 signs,
   with more signs fixed than broken in the paired count. Also, `err_corr` between views is below the A/B pair's
   value (about 0.5 by LESSONS.md).
2. **Adversarial verification of agreed signs, with a planted-error control.** Add a new
   `tools/lookalike_pass.py audit` subcommand. It samples signs that **both** readers agreed on, plus 5% planted
   substitutions taken from known confusion pairs. It shows each crop sign next to *two* candidate tiles in random
   order (the reconciled label and its top confusion partner), never "is this X?". A sign settles only if the
   auditor picks the other tile firmly. This is the editors' proofreading step (MLA CSE; Guide to Documentary
   Editing ch. 6) with a known-answer catch rate attached, because LESSONS.md showed an unblinded re-read confirms
   its own answer. *Test:* catch rate on planted errors is at least 60%, and on no.87 the agreed-wrong signs
   (about half the errors) fall, with err_true below 0.053 in the paired count. If the planted catch rate misses
   its gate, stop: by rule 3 this is a non-test.
3. **Alternatives in every line read, fed to the lattice.** Add a rule to the pass prompts in
   `.claude/briefs/transcription.md` (parent-approved): when hesitating, write `a/b?` (Megyesi 2020), never a single
   guess. Then `reconcile_passes.py --keep-alts` carries every alternative from every pass into a top-k file in the
   format that `key_decode_lattice.py` already reads. *Test:* the share of no.87 errors whose truth is in the lattice
   rises from 27/97 to at least 50% of errors, and lattice decode at the pre-registered lam improves err_true in
   the paired count. A rise in coverage alone with no err_true gain counts as "not adopted".
4. **Per-hand exemplar sheet from secure anchors (the palaeographer's alphabet).** Add an option
   `glyph_atlas.py atlas --from-truth TOKENS.tsv --per 6 --spread --exclude-leaf <eval leaves>`. It takes 4-6
   tiles per sign from H/C-graded positions of the same key family, chosen for the widest shape spread (allographs,
   cramped and line-end forms), and gives the sheet to line-read passes in place of one canonical shape per sign.
   *Test:* single pass A on no.87 with the sheet goes below 0.069 in the paired count, with the d<-T98 and s<-T50
   confusions down in tx_bench's top-confusions list. The Dinteville dev item (mapped 0.19-0.25) is the tuning
   ground. Building the sheet from the no.87 clerk sheet voids the test.
5. **Enhancement and recto-verso views for damaged leaves.** Add `iiif_lines.py --enhance dstretch|clahe|sauvola`
   (Tonazzini 2010) and `--verso-canvas N`, which mirrors and registers the verso by patch cross-correlation and
   suppresses bleed-through (Savino and Tonazzini 2016). The outputs feed #1 as extra views and the sorter's context
   view. *Test:* first add one benchmark item with real fading or bleed-through. The candidate is the R9528/RAH
   cursive hand if a known-answer span exists; otherwise this step stays "not testable". On that item, enhanced-view
   voting beats plain-view voting in the paired count. On no.87 (a clean scan) it must not make err_true worse.

**Smaller rule changes worth adopting with no test of their own:**
- every pass file carries a method header (model, view, prompt-id, sheet-id, sign count, cost), per Megyesi's
  "transcription method ... so we can compare various methods";
- gloss reads use `<ABBR ...>` expansions and are normalised before scoring (extends the PX-BRODEC lesson);
- a new hand gets a small known-answer item before its line reads are priced (Transkribus' "add data where the
  model struggles", applied to the benchmark).

## What we already do at or above the published standard

Some of our practice already matches or goes beyond what we found published:
- the known-answer benchmark with SER as substitution + deletion + insertion over scored, with intervals. This is
  the same metric as Magnifico and Megyesi's SER, and we also report confusions;
- a person deciding "same sign or different" on side-by-side tiles with cluster propagation. DECRYPT's own
  clustering tool uses a cluster-clean-and-label step (~1 h per 10 pages);
- the rule that agreement is not accuracy (LESSONS.md "Look-alike pass").

We found no published inter-annotator agreement figures for cipher transcription in the sources we opened. Megyesi
2020 and the DECRYPT pipeline paper give conventions and tooling, not reader-agreement numbers. A further search is
needed before we say none exist.

## Sources opened (4 Oct 2026) and not reached

Opened:
- ep.liu.se ecp2020_171_014 (Megyesi 2020, full text via pdftotext)
- ecp.ep.liu.se histocrypt 403/361 (Magnifico and Megyesi, full text)
- dspace.ut.ee DECRYPT pipeline record (abstract)
- arxiv 2009.12577 (abstract only)
- TEI PH chapter and ref-unclear
- coverpages MLA CSE guidelines (1997 mirror)
- gde.upress.virginia.edu chapters 4 and 6
- northumberlandarchives.com hints
- blog.transkribus.org CER page
- kraken.re (no figures used)
- jdmdh.episciences.org/11592 (CREMMALab abstract only; not cited for specifics)
- culturalheritageimaging.org RTI
- archimedespalimpsest.org imaging
- iris.cnr.it records for Tonazzini 2010 and Savino and Tonazzini 2016 (abstracts)
- ar5iv 2509.09722
- eadh.org Cappelli online
- cryptool.org Mary Stuart post

Not reached:
- (Read later, 4 Oct 2026: research/MARY-STUART-METHOD-2026-10-04.md.) Lasry, Biermann and Tomokiyo, "Deciphering Mary Stuart's lost letters from 1578-1584", Cryptologia 2023
  (doi 10.1080/01611194.2022.2160677): tandfonline answered 403 to WebFetch and to one curl. Its transcription
  method is therefore **not** described here. The CrypTool post says only that it took simulated annealing "as
  well as a lot of manual work". The usual description of their method, transcribing symbols and correcting the
  transcription as partial decipherment exposes errors, is *(memory)*, not verified.
- Megyesi 2020's long-form guidelines (cited inside the HistoCrypt paper): not opened.
- Tomokiyo's own transcription notes on cryptiana: not opened in this pass.

Requests made: about 25 web fetches/searches, one at a time, plus one curl to tandfonline.com, which returned 403
and was not retried.
