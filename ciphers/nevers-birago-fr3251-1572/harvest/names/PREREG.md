# NEVBIR-NAMES pre-registration (3 Oct 2026, written and pushed before any gap was inventoried)

Gazetteer: `gazetteer.tsv` (239 forms, built from `gazetteer_src.txt`; normaliser lower case, accents off, v->u, j->i, y->i).
Disclosure: before writing it this worker saw only the first five lines of reading_f139v.txt while learning the file format
(no name was read off them; the list's sources are tagged per row).

Units. Letters: fr.3251 no.71 (reading_f139v_tokens.tsv), no.86 (reading_no86_tokens.tsv + reading_no86B_tokens.tsv),
no.90 (reading_no90_tokens.tsv); fr.3252 f.47r and f.117r readings as committed in ciphers/birago-fr3252-1571-72. Each letter's
tokens are one stream in file order (line breaks ignored: a name may cross a line end).

Gap = maximal run of tokens graded U or M, length >= 3. Fixed = tokens graded S or C (single letter value). Word-sign tokens
(value longer than one letter, or [..] bracketed) and null tokens are barriers: no name may span them.

Placement of a form of length L at a gap: a window of L consecutive tokens that overlaps the gap in >= min(3, L) tokens and
contains no barrier. Admissible iff every fixed token inside the window equals the form's letter at that position.
Score = (fixed tokens matched) + 0.5 x (M tokens whose decoded letter equals the form's letter). A gap's statistic =
max score over all admissible (form, placement); fills with fixed-matched < 3 are never reported.

Controls (rule 3; both vary letters at the positions the statistic reads, so both can fail):
 (i) random gazetteer: 200 draws of 239 words from tools/data/it16dip (about 80%) and tools/data/fr16 (about 20%), same
     length distribution as the gazetteer, gazetteer forms excluded, same normaliser -> per gap, the max statistic per draw.
 (ii) flank shuffle: 200 permutations of the fixed letters among the fixed positions of the same letter (positions and
     grades kept) -> per gap, the real gazetteer's statistic per permutation.
A fill counts only if its gap statistic is strictly above the p95 of BOTH controls at that gap. Surviving fills are grade M.
Off-sheet single tokens read as whole-name codes admit any name (no constraint), so they are not scored.
Bonus: a U token class (sign id) given the same letter by surviving fills at >= 2 gaps is listed as a candidate value (M),
never applied to a key.
