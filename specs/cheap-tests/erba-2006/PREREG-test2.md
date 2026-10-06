# PREREG -- erba-2006 spec test 2 (xs = word space?), R12D-ERBA, 6 Oct 2026 (written before any scored run)

Input: `transcription_bERB.txt` (image-checked reading, 114 tokens; case folded, trailing '-' dropped). Three streams in page
order: main text (lines 1-17, 95 tokens), block right (lines 18-20, 12), block left (lines 21-22, 7). Line ends and (Bild)
breaks are NOT boundaries; a stream end is. The statistic depends only on where `xs` falls, so the 8 open me/ne calls
(grade M) cannot change it. Target xs count (descriptive, read before writing this file): 14/114.

Segmentation: split each stream on `xs`; every segment (including the first and last of a stream, and empty segments between
adjacent xs) is a "word"; its length = number of non-xs tokens.

Statistic S = mean over words of log P_ref(len), P_ref = word-length distribution of the reference corpus in the unit of the
design (floor 1e-4 for any length with zero mass, including 0). Two designs, both run, pre-registered here:
- L (token = letter): P_ref over word length in letters.
- Y (token = syllable): P_ref over word length in syllables (count of vowel nuclei: maximal vowel runs, +1 for each
  adjacent pair of a/e/o inside a run; i/u glides otherwise merge -- a heuristic, stated as such).
Reference corpus: `tools/data/it19` (Italian prose 1800-1830, incl. Foscolo letters). ERA MISMATCH stated: the target is a
2013 Italian private message; no modern Italian corpus is on disk and building one is outside this job's cap. it19's own
README rates its FAIL/PASS reliability as unknown (fold spread); word-length profile is expected to be less era-sensitive
than letter n-grams, but this is a caveat on both numbers.

Null ("randomly segmented" control): permute the positions of the xs tokens within each stream (other tokens keep their
order), 10,000 permutations, seed 12. p = (1 + #{S_perm >= S_obs}) / 10,001, one-sided.
Descriptive comparators (no gate): S for the unsegmented streams (each stream one word), and S when segmenting on each other
base token instead of xs (rank of xs among the 9 tokens).

Matched control (power, rule 3): 200 windows of real it19 prose rendered in the design's units with the real word spaces as
the separator token, cut to the same three stream lengths (95, 12, 7 units incl. separators), same statistic, same 10,000-
permutation null (2,000 per window to stay in cap -- stated). This control can vary on the statistic (its separator
positions are real word boundaries; the permutation destroys them). Also reported: the control windows' separator count
distribution vs the target's 14.

Gates, per design:
- Power gate: control windows reaching p < 0.05 in >= 80% of the 200. Below it -> target result for that design is a
  NON-TEST at this N ("untestable by this statistic at N=114"), whatever the target p.
- Target: PASS (xs-as-space supported under that design) if power gate met and target p < 0.05. FAIL (control-backed
  negative for xs-as-space under that design at this N) if power gate met and p >= 0.05.
A PASS is evidence about segmentation only, not a reading, and licenses nothing beyond spec test 3's design choice.
