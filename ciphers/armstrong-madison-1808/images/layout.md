# Frame layout, NARA M34 roll 14 frames 0029-0032 (ARM-TR, 26 Sept 2026)

Reduced-size (1200px-wide) look at each frame with PIL, by this worker directly (not a subagent), per
brief step 1.

- **0029** (3728x3280): a *different, unrelated document* -- a docketing/cover memo dated later in 1808
  ("Paris [ ] 1808"), addressed "Madison" / "Present", referencing "translation of a certain part of another
  letter ... to Gen'l Armstrong ... his letter of the 17th Feb 1808 ... to the Secretary of State" and
  continuing in ordinary cursive prose (not numeric groups). This is NOT part of the 20 Feb 1808 ciphertext
  letter and was not transcribed. Left page of the spread is blank. **Flag for the lane**: this frame appears
  to be misfiled/adjacent-item bleed in the roll sequence, not page 0 of our target; it references a *17 Feb*
  letter, not the 20 Feb letter this target is about, and is in clear prose throughout as far as legible at
  this resolution. Not investigated further (out of this brief's scope).

- **0030** (2096x2624): the actual start of the 20 Feb 1808 numeric-code letter. Single page (the manifest's
  "cleaner copy" framing does not apply to this frame -- it is simply one page, left margin blank). Header
  reads "Paris 20 [F]eb[r]y 1808". Body opens "The 453. 240. 760. 1480. [mark] 35. 681. 1752. 1843(?). 1314. ..."
  -- matches `ciphertext.txt`'s opening groups closely on a direct look (one apparent digit difference already
  visible by eye at group 9: manuscript looks like **1843**, `ciphertext.txt` has **1841** -- exactly a
  units-digit question, priority per this brief; not yet confirmed against the reconciled blind passes, see
  HYPOTHESES.md). 17 manuscript lines detected and cropped (`crops_0030/`, region 250,300,1846,2200 in native
  pixels, distance 100 prominence 15).

- **0031** (3968x2576) and **0032** (3968x2608): **NOT sequential pages -- verified by direct pixel/content
  comparison to be two separate photographic scans of the SAME physical leaf-spread** (identical handwritten
  content down to the exact ink-stroke shapes and flourishes on both the left and right pages; see the
  side-by-side crops in ROOM.md/NOTES.md). **This corrects the job brief's own assumption** ("Where 0030 and
  0031 are the same page in two copies, pass A reads 0031 and pass B reads 0030"): 0030 and 0031 are NOT
  duplicates of each other -- 0031's first line ("54. 1631. 12. 78. 350. 1470. 764. 18. 1801. [mark]...")
  picks up immediately where 0030's last line leaves off (ciphertext.txt row: "...41 1250 17 ** 1210 | 54
  1631 12 78 350 1470 764 18 1801 **..."), i.e. 0030 is page 1 and the two-page spread in 0031/0032 is pages
  2-3, continuing directly. The manifest.json `note` field on 0031 ("a cleaner copy of 30", copied from an
  earlier worker's crib_sources.md paraphrase of a Founders editorial note) is therefore either a mislabel or
  refers to something else in the Founders apparatus, not to this frame's actual relationship to 0030 -- not
  resolved further here (out of scope; flagged for a successor/orchestrator).

  Given 0031 and 0032 genuinely are two independent camera exposures of the identical leaf-spread, this
  worker uses them as the two witnesses the brief calls for, but on the correct pairing: pass A reads 0031's
  crops, pass B reads 0032's crops, for BOTH halves of the spread (left page = manuscript page 2, right page
  = manuscript page 3). Region/line-detection parameters were tuned separately per frame to produce matching
  line counts so `reconcile_passes.py` aligns row-for-row:
  - Left half: `crops_0031L/` (region 50,50,1850,2450, distance 100 prominence 15, 16 lines) and
    `crops_0032L/` (region 50,180,1850,2350, distance 100 prominence 15, 16 lines).
  - Right half: `crops_0031R/` (region 1950,50,2000,2500, distance 100 prominence 15, 15 lines) and
    `crops_0032R/` (region 1950,120,2000,2450, distance 100 prominence 15, 15 lines).

  Page 1 (0030) has no second photographic witness -- both blind passes for that page read the same
  `crops_0030/` images, independently, as a transcription-reliability check rather than a two-scan check.

## Page/pass plan

| Manuscript page | Source frame(s) | Pass A crops | Pass B crops | Lines |
|---|---|---|---|---|
| 1 | 0030 | crops_0030 | crops_0030 (same images, independent blind read) | 17 |
| 2 (left of spread) | 0031 / 0032 | crops_0031L | crops_0032L | 16 |
| 3 (right of spread) | 0031 / 0032 | crops_0031R | crops_0032R | 15 |

0029 excluded (different document, see above). Total manuscript lines covering the target's 369 groups: 48
(17+16+15), consistent with the target's own ~33 printed/wrapped lines in `ciphertext.txt` (wider Bourdeau
line-wrap vs the manuscript's own narrower physical lines).
