# PREREG VILL-7280 (3 Oct 2026, committed before fr.3995 f.80v / f.72v are viewed)

Units: fr.3995 f.80v (canvas f159; no.43, heading "22 Novem 1591" on f.80r) and f.72v (canvas f144; no.39, 1591,
"symbols and figures" per Bourdeau's checked set). First a thumbnail sheet of canvases 143, 144, 158, 159 (recto + verso,
to catch show-through as VILL-STRIPS found on f.74r/f.104r); a table is read only from the side whose ink is not mirrored.
If a letter strip exists: native crops by tools/iiif_lines.py, one blind read -> keys/key_f80v_letters.tsv /
keys/key_f72v_letters.tsv (code -> letter, grades M/I; nothing H).

Rules: identical to fr3995/PREREG-VILL-STRIPS.md, unchanged -- Gate 1 coverage >= 0.5 (figures count only if the strip
uses that figure in a code; a non-figure sign only if certified identical, which this job cannot do without a target image,
so signs do not count); Gate 2 power control first, 20 synthetic French texts at the target's length/coverage and the
strip's measured reader error, power < 16/20 => non-test, no score; Gate 3 rank 1/201 and z >= 3 vs 200 value-shuffled keys,
fr16 4-gram model, same segmentation (two-figure-first when the pair is a key code, 'o' = 0, signs dropped) via
strips_score.py extended to the new key files. No reading committed unless pass with power; grade S at best.
Also recorded per table: whether lambda, pi, theta, Delta, varpi or infinity (the target's family signs) appear.
If no letter strip is visible on either side of a leaf: that leaf is "no table", logged, no score.
