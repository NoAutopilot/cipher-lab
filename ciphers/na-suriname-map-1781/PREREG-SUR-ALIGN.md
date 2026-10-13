# PREREG-SUR-ALIGN (13 Oct 2026, 07:4x UTC by date -u; account 2, Opus worker for LANE DEFAULT-A2-0710)

Written and pushed before any score is computed. Script: `align_2046_crib2042.py` (committed with this file); only its
`--dry` mode (crib word list, slot counts, no score) has been run.

## Question
Does the decoded 4.VEL 2046 text block (Nieuw period key, `reading_2046_legend_nieuw_tokens.tsv` as of 5ddcc3c97: 362 slots,
H 233 C 22 M 83 U 24) align with the plain Purmerent legend of 4.VEL 2042 (`crib_2042_legend.tsv`, 11 entries a-l) well
enough that the crib may assign values to U tokens ([d-hook] x10, [o-flag] x3, [s-hook] x3, [3-breve] x2, [delta-grave] x2,
[1-hook], [a-grave], [amp], [delta-dots])?

Model choice: `tools/interlinear_align.py` aligns a cipher line to the clear line written with it (or a whole letter to its own
clear copy); 2042 is a sibling map's own plain legend, not a copy of 2046's text (2046 a = officiers, 2042 a = Battery; GAPS6
found the same-label null for 2039 vs 2042), so its model does not fit. The scan here is a word-anchor search, not a DP.

## Inputs
- Target slots: every token of the 11 lines of 2046. H/C and single-valued M = keyed letter; two-valued M (g|l, k|i) = either
  letter; U = wildcard. Segments are cut at plain tokens (labels, gun counts): 26 segments.
- Crib words: `crib_2042_legend.tsv` lowercased, ij/ÿ -> y (2046 spells y), à -> a, digits and ℔/° dropped, "Provi,"+"ant" joined;
  words of >= 5 letters: 15 (affdakken battery batteryen buite gereedschap keuke magas magasyn officiers plaats proviant provost
  quartier stukke water).

## Statistics
- **S (primary)**: number of distinct crib words that anchor in the 2046 block. Anchor: all L slots in one segment, no keyed slot
  disagreeing, keyed agreements >= max(4, L-2), wildcard slots <= 2.
- **S1 (secondary, the brief's entry-by-entry)**: mean over the 2046 legend entries a-k of the best-offset fraction of keyed slots
  equal to the same-label 2042 entry (GAPS5/6 same-label score). S1 assigns no token on its own.

## Controls (seed 20261013, N = 1000 each) and the rule-3 check
| control | what it permutes | can it differ from the target on S? | on S1? |
|---|---|---|---|
| value-shuffle | the values of the (sign, value) pairs present in 2046, permuted among those pairs (the key's letters permuted within the Nieuw alphabet as used here) | yes: every decoded letter can move | yes |
| label-shuffle | the crib entries permuted across the labels a-l | **no**: S counts words regardless of label, so it is identical by construction (non-test for S; computed and reported only to show this) | yes: changes which crib entry each 2046 entry meets |
| crib-letter shuffle (substitute for label-shuffle on S) | letters permuted within each crib entry, word lengths kept (GAPS5/6's shuffled-crib) | yes: changes every word | not used |

A control whose null takes one value only, equal to the real one, is reported as a non-test. Headroom: if the value-shuffle null
mean is already at or above the real S, the control has no room to show a gain and the result is FAIL (no assignment).

## Gates
- **S PASS**: at most 1% of the value-shuffle null AND at most 1% of the crib-letter-shuffle null at or above the real S.
- **S1 PASS**: at most 5% of the value-shuffle null AND at most 5% of the label-shuffle null at or above the real S1. Reported; a
  PASS of S1 alone changes no token.

## Decision rule for U/M tokens (fixed now)
- S FAIL: nothing changes. Anchors are listed as observations only.
- S PASS: for each U sign class, take its instances that sit in a wildcard slot of a real anchor; the crib letter there is the
  proposal. If all anchored instances of the class give one letter AND they come from >= 2 distinct crib words, each anchored
  instance (only those) gets a per-token row in `exceptions_nieuw_image.tsv`, grade **M** (crib_2042 is a sibling map's plain
  legend, not a period gloss of this text, so C is not licensed). One crib word only: logged in HYPOTHESES.md, no change.
  Disagreeing letters: logged, no change. Instances outside an anchor stay U; no class-wide or key-file change
  (`key_period_codes_nieuw.tsv` untouched).
- Two-valued M slots (g|l, k|i) under an anchor: the implied letter is logged only, no change (a class question, GAPS37).
- Single-valued M and H/C slots cannot be reassigned: an anchor requires them to agree.
- After any change: `tools/decode_key.py ciphers/na-suriname-map-1781 --check` must pass.
