# PREREG R13-SUR730 (6 Oct 2026, ~14:10 UTC by date -u; committed and pushed BEFORE the blind pass is read or score.py is run)
Material: NA 1.05.03 inv. 373 scan 0730 (IIIF 50305553-...df5e.jp2, native 4783x3963), one page (left; right page blank) of 11
cipher lines, each with a lighter plain Dutch line ABOVE it, signed "Fortresse Nieuw Amsterdam d: 20 Octob: 1781". 11 gloss+cipher
pair crops cut by tools/iiif_lines.py (crops/manifest.tsv). Crops not committed (folder over 30 MB); regenerate from the manifest.
Question: does 0730's cipher use the same sign system as the map key / the 0692-0693 and 0702 letters?
Method: R13-SUR702's PREREG and score.py unchanged in every rule (passes/inv373_0702_r13/PREREG.md, pushed 2fcd61117), except:
- Reader: ONE blind Sonnet pass on the 11 crops (crop paths only; the same reader-code vocabulary as 0702; NO values, NO key)
  -> passA_sonnet_blind.tsv. The worker reconciles the GLOSS only -> gloss_reconciled.tsv; no blind cipher token is altered for S1/S2.
- S2 = agreement with the POOLED 0693+0702 sign table (a code agrees if the gloss letter is among its letters_seen in
  passes/inv373_0693_r10/sign_table.tsv OR passes/inv373_0702_r13/sign_table.tsv), as the brief names. S2 descriptive.
- Control: gloss letters permuted across all used positions, 1,000 permutations, seed 730 (can vary on S1 and S2).
Gate (unchanged): SAME SYSTEM if S1 (key_period_codes_nieuw.tsv) >= 0.60 AND S1 > control p99. Otherwise 'not shown'.
Per-code table descriptive; conflicts with an H/C value seen >= 2 times -> conflicts.tsv rule-4 data row (no key edit).
No key.tsv / key_period_codes_nieuw.tsv edit; candidate values -> candidates_0730.tsv for a verifier.
Also listed (not tested): any gloss word naming a map sheet, a legend letter or a work on the fortress, as a crib for 4.VEL 2039.
