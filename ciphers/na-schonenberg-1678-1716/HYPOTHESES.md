# na-schonenberg-1678-1716 -- hypotheses and key conflicts

Append-only. Prose sections above the table; the table is written by `tools/family_run.py` (none run here yet).

## H1 (GAPS-na-schonenberg-1678-1716, 2 Oct 2026): the two "unglossed" closing lines encipher the clear text beside them

- **L18 = "forma"** is not a hypothesis but a layout fact: the word "forma." stands in the small interlinear gloss
  hand letter-for-letter over 61.68.2).88.)8. (images/crop_layout_L14_to_address.jpg), continuing L14's gloss tail
  "en, esta" -> "en esta forma". VX-CS01/VX-RD01 took it for a clear word of the main text. Period gloss, grade C per
  the folder's own convention (a transcription tally of the period gloss is C, not H).
- **L19 = "a doña antonya de albanylla"** (the clear address at the foot, in the large main hand, 23 letters = 23
  groups, cipher spelling -y- because 32 = y is C): a crib, not a displaced gloss. Target 15/16 resolved positions
  agree (only 8) = p vs l); of 6 U positions with a body tie set, 4 contain the crib letter. Controls
  (`crib_align.py --shuffles 2000 --seed 1`): slid-window over L01-L14, n=229, mean 0.104, p95 0.235, max 0.286,
  0 windows at or above the target's 0.938; shuffled crib at L19's own position, n=2000, mean 0.162, p95 0.312,
  max 0.438, 0 permutations at or above. L18 "forma" 4/4: slid-window n=247 mean 0.078 max 0.500, 0 at target;
  all 120 permutations, only the identity reaches 4/4. Both controls can move the statistic (letter agreement
  changes with window and with letter order), so this is a test (rule 3).
- What the crib fixes and at what grade: [n] = ñ (C: the sign is an n with a mark above, no body occurrence,
  no conflict); 61 = f (C, from L18's own gloss, crib-independent); 88 raised M -> C (body m + gloss m).
  24 = o, 34 = a, 51 = t, 11 = a, 65 = l: each agrees with the crib (and 24/34/51/11 with one body gloss) but
  disagrees with one or two other body glosses -> **M under rule 4's conflict clause**, witnesses in conflicts.tsv.
  ?9 (L19 pos9) = n via exceptions.tsv (M: blotted sign; 89 = n fits). 8) at L19 pos20 = l via exceptions.tsv (M)
  against body L03 pos0 "P" (conf M): a real two-witness conflict, unresolved.
- What would settle the M codes: `tools/interlinear_align.py` over L01-L14 (gap 2), which decides whether the
  disagreeing body glosses are alignment slips (then the crib values rise to C) or genuine homophony/second values.

<!-- family_run.py table: one row per run, appended by the tool, never edited by hand -->

| date (UTC) | family | parameters | seeds | CONTROL mean (range) | TARGET best score | judge | gate met | label |
|---|---|---|---|---|---|---|---|---|
