# PREREG-DEF1F3416 -- upper letter M/U words as whole line strips, blind Opus pass C (account 1, 5 Oct 2026, written 21:1x UTC before any read)

Brief: `.claude/briefs/runs/2026-10-05-account1-default-2039-jobs.md` job DEF1-F3416 (LANE DEFAULT-account-1-20261005-2039),
cap $7, box 21:05-22:15 UTC. Instrument (different from the retired 1100-px word windows): the FILS-UPPER line-strip
segments themselves, the material FILS-UPPER's two Opus passes read.

**Crop step (mandatory, pasted).** The strips were cut on 3 Oct 2026 by
`python3 tools/iiif_lines.py --ark btv1b9058240c --canvas 43 --region 3550,420,3550,3260 --out ciphers/fr3416-nevers-fils-1589/images --prefix f43u --debug`.
Re-run today from the on-disk source (pillow+numpy installed in the container for it):
`python3 tools/iiif_lines.py --image ciphers/fr3416-nevers-fils-1589/images/src_ark_12148_btv1b9058240c_f43_3550_420_3550_3260.jpg --out <scratch>/strips --prefix f43u --debug`
-> "26 lines, 26 bands x 2 segments; pitch 116"; f43u_L03_s2 and f43u_L13_s2 byte-identical (`cmp`) to the committed
crops, so the committed crops are used. Every strip 2400 px wide (< 2500), 81-139 px high. B11 = `images/f43b_L03_s1.jpg`
(region 3550,4560,3550,400, same tool, 3 Oct). Margin rows M2-M4 (separate sideways images) are out of this run.

**Strips (12, = 3 calls of 4).** `verify/upper_strips/select_strips.py` ranks each line's two segments by the number of
M/U tokens whose proportional offset falls inside it (s1 = 0-0.676 of the line, s2 = 0.324-1) and takes the best
segment of the 12 best lines: U03 s2, U11 s2, U12 s2, U13 s1, U17 s2, U18 s1, B11 s1, U07 s2, U09 s2, U20 s2, U24 s2,
U25 s1 (`verify/upper_strips/targets.tsv`; 30 of the 52 M/U tokens of U01-U26+B11 fall in them by offset). Twelve,
not all lines: the cap allows 3 reader calls at ~$1.2 + 1 reconciliation unit by me inside 80% of $7.

**Controls (hidden from the reader), fixed now:** `random.Random(20261005)` over plain H tokens of >= 5 letters inside
the chosen segments (>= 0.05 of the line from the segment edges), at most one per strip: B11 "reste", U25 "estat",
U13 "chascun", U18 "desia", U12 "affin", U11 "estoit" (`verify/upper_strips/controls.tsv`). The neighbour rule of
cut_cap.py (no M/U within 2 places) left a pool of 5 here, so it was dropped before sampling (pool 16).

**Reader.** One blind Opus subagent per 4 strips, 3 calls. It sees only the strip images under neutral names
s01-s12 (order random.Random(202610051).shuffle over the 12) and the instruction: "Each image is one line of a
handwritten 16th-century French letter. Transcribe every word of each image, left to right, as written (keep
abbreviations as written, e.g. q' , p'r, l'res). Use [?] for a letter you cannot read and [...] for a word you cannot
read. The line is cut at the image edges, so the first and last words may be partial. Give a confidence H/M/L per
image." No row text, candidates, grades or key.

**Gate.** A control word is right when the reader's word at that place equals the H reading exactly, modulo u/v,
i/j, accents and case (abbreviation marks as written count). **Fewer than 5 of 6 right: non-test, no grade moves; the
line-strip instrument is logged and the step is [retired] (rule 3 third-attempt clause).**

**At >= 5/6, rules per target token** (located by its neighbours in the read):
1. M token `{w}` -> H when the reader's word(s) equal w exactly (same normalisation).
2. U token `{A / B}` -> H when the reader equals one candidate and I see it clearly on the strip myself; -> M when the
   reader equals one candidate and I do not see it clearly; otherwise stays U.
3. U token `[...]` -> M when the reader gives a whole word (no [?]) and my own look at the strip agrees; else stays U.
4. Mismatch, [...]/[?] at the target, or target not locatable: grade unchanged, listed. Every token recorded per word in
   `verify/upper_strips/results.tsv`; counts H/M/U words before and after.
