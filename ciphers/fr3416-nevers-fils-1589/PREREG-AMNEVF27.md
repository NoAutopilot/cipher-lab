# PREREG AM-NEVF27 -- period gloss over fr.4715 f.27r L09 at the lone '1' (account 2 for LANE LANE-AM-0914, 7 Oct 2026, written 10:3x UTC by date -u, before any gloss crop is fetched or looked at)

Question (D07-NEVF25 observation): f.27r L09 as read by two blind passes runs `4 65 63 64 45 48 67 76 84 37 45 84 87 43 18 1 32 94 57 67 54 64 84 ...`.
Under key no.25 (keys/key_no25.tsv) frame 1 reads o n n e h o r s c e s t e s + 18 (null), frame 0 after the '1' reads a u m o i n s.
Between the e (43) and the a (32) stand three figures `1 8 1`; no frame-preserving parse gives them zero letters (odd count), and
frame 1 continued reads 13 (null) 29 (no code), frame 0 before reads 74 31 81 (r, no code, no code). Does the period decipherer
read across that spot, i.e. treat a one-figure orphan as nothing?

Material: the interlinear gloss over L09 on Gallica btv1b52509819x canvas f67 (label 27r). One region fetch at native size covering
L09's figure band and the gloss band above it (located from the D07-NEVF25 region 560,1000,3150,1100, band 9), cut with
`tools/iiif_lines.py` into crops under 2500 px; crop paths only to readers.

Reading: 2 blind Sonnet passes (crop paths only; no key, no decode, no figures, not told what the question is), each asked to
transcribe the clear-text letters written between/above the figure lines, left to right, with '_' for a visible gap and '?'
for an illegible letter, plus the figures under the first and last letter of each gloss word. Then my reconciliation (1 unit).

Statistic S (target): in each pass's gloss over L09, the letters between the end of the word read over `...37 45 84 87 43`
("ces te s" / "cestes") and the start of the word read over `32 94 57 67 54 64 84` ("au moins").
Known-answer control K (can fail): LCS of each pass's gloss over the frame-1 span with "onnehorscestes" (14 letters); and LCS
of the gloss over the frame-0 span with "aumoins" (7). Gate: both passes K1 >= 10/14 and K2 >= 5/7. Shuffle control Z (can
vary on the same LCS): the same LCS of the same gloss text against 1000 random permutations of each target string (seed 20261007);
the real LCS must exceed the shuffle p95 for both strings. K or Z below gate in either pass -> NON-TEST, nothing concluded.
Null-junction control N (can vary on S): the gloss over the known null 18 itself is part of the same junction, so S counts the
letters given to `18 1` together; a second junction on the same line read the same way is the word-to-word gaps elsewhere in
L09's gloss -- reported, not gated (no other odd-figure junction is known on L09).

Outcomes (controls passing):
 A. both passes: S = 0 letters (gloss runs "...cestes" straight into "au moins", a gap or word space allowed) -> the period
    decipherer read across three figures `1 8 1` with no letter = a one-figure orphan in key-no.25 practice, grade C as a
    practice witness (a known-plaintext reading of the same figures by a reader of the time), conditional on the digits
    `4 3 1 8 1 3 2` as both D07-NEVF25 passes read them.
 B. both passes: S >= 1 letter that the key cannot give to 18 or 1 alone, or the gloss reads a different word at either side
    -> not a witness; record what the gloss reads.
 C. passes disagree on S -> non-test unless the crop settles it on my reconciliation look (one look, recorded).
Grade rule (carried from PREREG-D07NEVF25, fixed now): f.27r is "Evesque"'s hand, not the f.35r writer's. Outcome A makes the
`4 57 9` parse of f.35r L05 admissible as practice; it does not by itself move tokens 45 or 79 from M (the f.35r image shows even
spacing; a grade move needs same-writer material read at H). So the re-judge of f.35r token 79 under this rule leaves 45/79 M
whatever the outcome; `decode_f35.py --check` is run to show nothing moved. The rest of f.27r is not transcribed here (~$30 job).

Deviation, recorded 10:2x UTC before any pass read: the locating look (one 0.5x strip of region y 600-800, then the debug crop) shows the
decipherer's gloss for L09 written BELOW the figure line, between L09 and L10 (the clear word under `48 67 76` sits there), not above it;
the words above L09 belong to L08's gloss. Crop (pasted): `python3 tools/iiif_lines.py --image <src_..._f67_560_1000_3150_1100.jpg>
--region 0,680,3150,175 --out <scratch>/g --prefix f27g --centres 87 --top-margin 87 --bottom-margin 88 --max-width 1700 --debug` ->
2 segments 1700x175 (overlap 150), each holding the L08 gloss line, L09 figures, the L09 gloss line, and the top of L10's figures.
S, K and Z are computed on the gloss line BELOW L09 (the band between L09 and L10); the gloss above is transcribed and reported only.
