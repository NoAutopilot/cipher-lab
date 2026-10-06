# PREREG gl275 -- f.275v L17-L20 later-hand interlinear gloss as a C witness (R8-PIS, 6 Oct 2026)

Written and pushed before any gloss read is opened. Brief: .claude/briefs/runs/2026-10-06-account1-run8-jobs.md "R8-PIS".

Material: the small later-hand letters written above the cipher signs of f.275v block B lines 12-15 (L17-L20; c563 of
btv1b9060906j), seen by D2-PIS275. Cipher tokens: the committed tx86h/ciphertext_f275v.tsv L17-L20 (tx86i's eye-reconciled
variant is reported beside it, not used for grades).

Procedure (fixed now):
1. Crops: tools/iiif_lines.py on the native c563 region with RUN6-PIS's centres, a larger top margin so the gloss row above each
   line is inside the crop, narrower segments; command pasted in NOTES.md before the first reader call.
2. Two blind Sonnet readers (A, B), one call per line, each told only: transcribe the small later-hand letters written ABOVE the
   large cipher signs, left to right, word-level, with for each gloss group the segment and the approximate x-position, and to
   write '?' for an unreadable letter. Readers are not shown the Colbert copy, the key or the decode.
3. Reconcile A vs B by eye from the crops (worker), letter by letter; letters where A and B disagree and the eye cannot settle
   stay '?'. Agreement A vs B reported (letters, after aligning).
4. Alignment: each reconciled gloss group is placed over its cipher sign run by x-position on the crop; its letters are aligned
   to the signs under it (one letter per sign for the alphabet cells; a code-word cell such as T55 'faict' or T63 'qui' takes the
   gloss letters of its value). A gloss letter is a C witness for the sign under it only when (a) A and B agree on it or the eye
   settles it, (b) the group aligns to a contiguous sign run with no insertion, deletion or shift (no repair), and (c) the gloss
   word is a French word or a word of the Colbert p.123 passage. Everything else: M.
5. Conflicts: a C-aligned gloss letter that differs from key86's value for the sign is logged as a conflict (rule 4: both
   witnesses recorded -- key86 = Tomokiyo's published table, gloss = period/later hand on this leaf -- not settled by majority);
   key86.tsv is not changed by this job.
6. Report: C / M counts per line over the L17-L20 sign tokens, the number of gloss letters agreeing with key86, and the
   conflict list. No gate statistic: this is a witness read, not a test; nothing here moves kp86h/grades_f275v.tsv unless every
   condition in 4 holds for a token, and then only that token moves M -> C (gloss).
