# H28 pre-registration (campaign runner armstrong-madison-1808, owner account, session_01NuaRiPghx6VRXA6GuJE8ne)

Written 28 Sept 2026 02:11 UTC, before any reader output existed. The one-knob re-run H24 named: same instrument
class (a blind Sonnet reader given only a period alphabet plate and shorthand crops, no title, author, system or
text, web tools forbidden), same scorer and gate (`h24/score.py`, `h24/PREREGISTRATION.md`: S1 > null p95 AND
S2 >= 3 AND S2 > null p95 over 200 consonant bijections), with the knob changed as H18 suggested: PER-GROUP
magnified crops (2x) in reading order for each of the five ruled lines, the whole line strip beside them, and the
book's own worked example ("In the Word Man": m, a, n joined) on the same call.

Specimen: Macaulay, *Polygraphy, or Short-hand made easy* (1747), archive.org
bim_eighteenth-century_polygraphy-or-short-hand_macaulay-aulay_1747, leaf 22 (the book's page 13), Psalm I "written
in the long Short-hand, wherein all ye Vowels are included in each Word", the five ruled lines on that leaf (verses 1-3
opening). Plate: `images/shorthand/specimens/macaulay1747_alphabet_p3.jpg` (leaf 12, the comparative alphabet with a
sample word per letter, ARM-S1). Reference: KJV Psalm 1 (`h28/ref_psalm1_kjv.txt`, Gutenberg pg10).

Crops: `h28/crops/line{1..5}_strip.jpg` (native), `line{L}_w{NN}.jpg` (2x, gap-segmented at 10 view px after
dropping the printed rule rows; `crops/manifest.json` has the native coordinates), `leaf22_worked_example_man.jpg`.
Segmentation is by ink gaps, so a "word" crop may hold one character or two words; the reader is told this and
returns letters per crop, which the scorer concatenates (S1 is alignment-based, S2 counts exact word skeletons).

Outcome rule (from the H24 row): CONTROL PASS licenses one target read (the five `h24/target_*.jpg` crops, T2 vs
the en18 skeleton null, at most one more call); CONTROL FAIL retires the plate-only reader for this family
("untested-by-this-tool" in HYPOTHESES.md), no target read, no third attempt with the same instrument.
Budget: 2 vision subagent calls at most (of the step's 4), cap 3 USD.
