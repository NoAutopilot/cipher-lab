# PREREG R14-SUR746 (6 Oct 2026, 15:2x UTC by date -u; committed and pushed BEFORE the blind passes are read or score.py is run)
Material: NA 1.05.03 inv. 373 scan 0746 (IIIF 6faa084a-...58a8.jp2, native 4992x4023), two pages: left 20 gloss+cipher pairs
(lighter plain Dutch line ABOVE its heavy cipher line) plus a catchword pair (cipher "#&..." with a small plain word below), right
5 pairs plus one crop holding "oorlog de Valk" (end of the "Actum aan boord van 's Lands Fregat van oorlog de Valk" plain) and the
cipher group before "den 24 October 1781"; signatures below, not cropped. 27 crops cut by tools/iiif_lines.py (crops/manifest.tsv).
Crops not committed (folder over 30 MB); regenerate from the manifest.
Question: does 0746's cipher use the same sign system as the map key / the 0692-0693, 0702 and 0730 letters?
Method: R13-SUR702's PREREG and score.py unchanged in every rule (passes/inv373_0702_r13/PREREG.md, pushed 2fcd61117), with
R13-SUR730's parser fix ('\&' = one sign '&'), except:
- Reader: ONE blind Sonnet pass per page (left L01-L21, right R01-R06; crop paths only; the same reader-code vocabulary as
  0702/0730; NO values, NO key) -> passA_sonnet_blind.tsv. The worker reconciles the GLOSS only -> gloss_reconciled.tsv; no blind
  cipher token is altered for S1/S2. Where a gloss line spans two cipher lines (right page Actum/Valk) the pair will simply fail
  the word-count rule and be skipped; no hand re-pairing.
- S2 = agreement with the POOLED 0693+0702+0730 sign table (a code agrees if the gloss letter is among its letters_seen in any of
  passes/inv373_0693_r10, inv373_0702_r13, inv373_0730_r13 sign_table.tsv). S2 descriptive.
- Control: gloss letters permuted across all used positions, 1,000 permutations, seed 746 (can vary on S1 and S2).
Gate (unchanged): SAME SYSTEM if S1 (key_period_codes_nieuw.tsv) >= 0.60 AND S1 > control p99. Otherwise 'not shown'.
Per-code table descriptive; conflicts with an H/C value seen >= 2 times -> conflicts.tsv rule-4 data row (no key edit);
[y-fam] m|n vs d counts added to the y row of conflicts.tsv as a further glossed witness.
No key.tsv / key_period_codes_nieuw.tsv edit; candidate values -> candidates_0746.tsv for a verifier.
Also listed (not tested): gloss words naming a map sheet, a legend letter or a fortress work, as crib candidates for 4.VEL 2039.
