# PREREG-BRANDT-TX (9 Oct 2026, written 01:2x UTC by date -u, before any alignment score is computed)

Target: Friedrich von Brandt to Hedwig Sophie, Copenhagen 27 Feb 1672, HStAM 4 f Staaten D Dänemark 131 image 0020, right page,
lower cipher block (the "troupe deutscher Commedianten" passage) and its period marginal gloss. Job BRANDT-TX, LANE FAMILY-A2d.

Inputs (frozen before scoring): `ciphertext_0020.tsv` (two blind Sonnet passes + reconciliation) and `gloss_0020.txt` (one Sonnet
pass + worker check, normalised: lowercase, abbreviations expanded, umlauts folded by the tool, rule 3 convention clause).

Pairs: the cipher stream and the gloss are cut into segments at the clear German words the writer left among the groups
("undt", "sonderlich", "hat", "haben", "da die", "niemalen", "bis" ...) wherever the same word stands in the gloss; each segment is one
(cipher run, gloss span) pair in `pairs_0020.tsv`, cipher_line = segment id. Segmentation is done by the clear-word anchors only,
before any alignment is run.

Primary run (one configuration; any other configuration is exploratory and reported as such):
`python3 tools/interlinear_align.py align pairs_0020.tsv align_0020.tsv key_0020.tsv --floor 150 --clear-consumes --max-chunk 8
 --shuffle 200 --seed 1672 --min-share 0.6 --shuffle-out shuffle_0020.json`
(groups < 150 take 0-1 gloss letters; groups >= 150 take up to 8; no prior key -- key 255 disagrees with 0049, HDK-131).

Statistic: CONSISTENT (the tool's --shuffle statistic: values whose top chunk is non-empty, occurs >= 2 times on >= 2 different
segments and is >= 0.6 of the value's aligned occurrences). Control: the same run with gloss spans dealt to the wrong segments
(200 derangements, seed 1672). This control can differ from the target on the statistic: a gloss over the wrong segment gives
letters that disagree across segments.

Gate: PASS if real CONSISTENT > the maximum of the 200 draws (empirical p < 0.005) AND real >= 2 x the control mean.
FAIL otherwise. Not-a-test if fewer than 8 pairs can be formed (the derangement control then has too few arrangements).
A PASS licenses only: the period gloss is a decipherment of these groups at letter level, and the per-value table (grade C for
values the gloss gives at >= 2 occurrences with top share >= 0.6; M otherwise) is fit to test on the held-out 0049 slip in a
later job. 0049 is not read in this job; 0050 and 0062-0064 are not decoded.
