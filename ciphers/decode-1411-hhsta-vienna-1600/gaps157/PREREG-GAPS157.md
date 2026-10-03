# PREREG-GAPS157: one spelling normalisation, applied identically to corpus, gloss and decode (3 Oct 2026, account-4)

Written and pushed before any normalised score is computed. Rule 3 PX-BRODEC lesson: before a judge compares two
renderings, put both on one convention. CORP-DE16 found the leaf's own 62-letter gloss at -1.423 under de1600, below
199-200/200 genuine held-out windows; this step asks whether spelling convention, not the corpus era, is the gap.

## Normalisation N (function `norm` in gaps157/score157.py, applied after the judge's own `fold`)
1. `fold` as tools/judge_plaintext.py does it (lower case, its accent table, ß->ss, everything outside a-z removed --
   this removes abbreviation marks, superscripts, punctuation, spaces, digits).
2. v -> u, j -> i, y -> i (the decode's 24-letter alphabet already merges i/j and u/v).
3. Any run of the same letter collapses to one (double letters removed: "dann" -> "dan", "sollen" -> "solen").
Nothing else. No letter-value change to the frozen table (residue/frozen_table.tsv); z stays z, s stays s, etc.
The same N is applied to: every corpus file before the model is built (n=4, k=0.01, as the judge), the gloss text
(gaps150/gloss_text.txt), the frozen-table decode of the 176 numbers (residue/numbers.tsv), every shuffled-target
decode (200 draws, seed 157), and the 23 shifted-rule decodes (k=1..23). N is length-changing, so real/null controls
are drawn at each normalised text's own length.

## Scored, side by side, raw (fold only) and normalised, under de1600 (primary) and de17 (secondary)
gloss: score, real_p05, real_p01, null_p99, letter-shuffled (200, seed 1570) mean/p99.
decode: score, real_p05, null_p99, shuffled-target p99 and count >= decode, shifted max and count >= decode.

## Registered verdict (primary corpus de1600, normalised; de17 reported, must agree for the strong word)
A. Normalised gloss > real_p05 AND normalised decode > real_p05, > null_p99, > shuffled-target p99, > shifted max:
   "reading ready" ROOM flag for a separate verifier (no status change by this worker).
B. Normalised gloss > real_p05 but decode fails A: "calibrated judge FAILs the frozen-table decode" -- recorded as a
   control-backed FAIL of the frozen table on these 176 numbers, conditional on the transcription; status unchanged.
C. Normalised gloss <= real_p05: "judge cannot recognise this leaf's text even normalised" -- the judge is retired as a
   gate for this leaf (rule 3 third-attempt clause: de17, de1600, de1600+N); next instrument is a person's read of the
   gloss (ASKS row), not a further machine pass. Decode-vs-controls numbers are reported but license nothing.
