# LANE R7 R7-MEYE -- blind eye-check, espagnol142-mercy-1648

Blind re-transcription of recto lines 6, 14, 16, 17 and verso lines 4, 7, from
`images/f22r_canvas58.jpg` and `images/f22v_canvas59.jpg` only, before opening any
existing transcription file (AUDIT.md section 3(d)). Crops, boxes and `blind_pass.tsv`
were committed and pushed before `compare.py` was written or run.

**Disclosure (blind-rule note):** while dumping `images/manifest.json` with a generic
`json.dumps` for the "entries" block, the full file printed, including the
`iiif_lines` block's pixel boxes for recto bands 6-8 (prior tooling's line
segmentation). This revealed the y-range used for a prior r06 crop before I cut my
own. No glyph content was exposed, only a line boundary. I did not reuse that box;
all six crop boxes here were re-derived from scratch by eye and by an independent
ink-profile / valley-finding pass over the raw canvas images (see `crop_boxes.tsv`),
and each was verified by viewing the resulting crop against my own line count from
the top of the page before transcribing. Flagged in ROOM.md at the time.

## Method

1. Counted lines from the top of each side by eye on a full-page preview, confirmed
   against two overlapping native-resolution crops of the recto and one of the verso.
2. Found line y-boundaries with an ink-density profile (`scipy.signal.find_peaks` on
   smoothed row-darkness, x-restricted to avoid the marginal flourish); the prose
   section's decorative capitals and connecting flourishes make bands merge, so every
   candidate boundary was checked by cropping and viewing the line, not trusted from
   the profile alone (`crop_boxes.tsv` records the boxes actually used).
3. Built `ref_4_9.png` from row 9 (`4 8 19 33 28 21 25 18 32 22 10 14 2 32 8 23 6 3 10
   5 10 4 8`), which has two isolated 4s and two 9s (in 19 and 14), and compared every
   doubtful digit in the six target lines against it at 3-4x zoom.
4. Transcribed all six lines token by token into `blind_pass.tsv` (122 tokens),
   confidence H/M/L, alternates for every M/L token, before running `compare.py`.

## Numbers

`compare.py` output, against `ciphertext.tsv` (the two earlier passes' settled form):

```
overall: 116/122 agree, 4/122 disagree, 2/122 unreadable
```

Every one of the 6 non-agreements is explained, not a fresh error signal:

- **r06 pos.14, r17 pos.5** (2 rows): my blind read is `14` at both; `ciphertext.tsv`
  still carries the old two-pass `19` (the M-graded exception has not been merged into
  it), so these count as "disagree" against `ciphertext.tsv` but as agreement with
  `exceptions.tsv`'s correction (below).
- **v07 pos.15-16** (2 rows): my pass reads an extra token here (`3` then `17`) where
  `ciphertext.tsv` has a single `7`; zoomed to 4x (see ROOM/this file), there is a
  distinct thin `1` stroke separate from the `7`-shaped stroke, so I do not think this
  is my misreading a single glyph as two -- it reads as a real segmentation question
  worth a targeted look, not resolved here. Named as a `COUNT MISMATCH` row in
  `compare.tsv`.
- **v04 pos.19** (1 row): the photograph's right edge cuts the line before the last
  numeral finishes (only a leading stroke survives); `ciphertext.tsv` itself marks this
  position `M`/`gap`, consistent with a genuinely hard spot rather than a fresh
  disagreement.

## The five exceptions.tsv 14-vs-19 positions (the point of this job)

```
r06 pos 14: blind read '14' (conf M), exceptions.tsv says '14' -> AGREE
r14 pos 7:  blind read '19' (conf M), exceptions.tsv says '14' -> DISAGREE
r16 pos 3:  blind read '19' (conf M), exceptions.tsv says '14' -> DISAGREE
r16 pos 6:  blind read '19' (conf M), exceptions.tsv says '14' -> DISAGREE
r17 pos 5:  blind read '14' (conf M), exceptions.tsv says '14' -> AGREE
```

2 of 5 agree with the exceptions.tsv correction, 3 of 5 (r14 pos.7, r16 pos.3, r16
pos.6) read as `19` on this independent pass -- closed loop top with a descending
tail, matching the isolated 9s in `ref_4_9.png` better than the angular
diagonal-plus-vertical 4s there. r16 pos.6 is the strongest 9-reading of the three
(clean closed loop, long tail); r16 pos.3's loop is more open and r14 pos.7's is
close to the boundary between the two shapes. This is a genuine split, not a
rubber-stamp of either the original passes' `19` or the exception's `14`: see
`blind_pass.tsv` for the per-token alternate/reasoning on all five.

Grade: cryptanalytic (S/M per rule 4, no key or known-plaintext source used); this is
an eye-check re-transcription, not a decipherment. Not classifying novelty (rule 10).
