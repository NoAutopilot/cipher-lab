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

## H2 (GAPS2-na-schonenberg-1678-1716, 2 Oct 2026): passB's gloss letters are right, their attachment to groups was off in seven lines

- `tools/interlinear_align.py` (align/gloss_align.py, R0 unseeded / R1 C-seeded / R2 C+crib-seeded) re-attaches 88 of 256 glossed
  tokens, all in L02, L08, L09, L10, L12, L13, L14 and two in L01 -- the lines passB's own summary flagged (plus L02, a whole-line
  one-position slip). R2 agreement 0.699, 44 C-bar codes; within-line shuffled-gloss control (n=300, seed 1) max 0.301 / 11, 0 at
  or above either target. R0 alone (no key) reaches 0.570 / 30 against its own control max 0.254 / 7.
- H1's open question answered for three of five crib codes: 24 = o, 51 = t, 65 = l read the crib letter (or nothing) at every body
  occurrence in R1, where they are not seeded, with R0 agreeing -> C. 34 = a keeps a body d at L11 pos14 in every run (3/4) and
  11 = a keeps s at L09 pos15 (R0/R1 tie) -> M, conflicts standing.
- New conflicts, all two-witness and all graded M (rule 4): **50** -- s at six glossed occurrences in every run (R2 6/7 even when
  seeded r) against VX-RD01's pixel-verified r at L06 pos17 (key.tsv 50 = s M; exceptions.tsv keeps L06 pos17 = r); **49** n/r/u
  and **31** x/d tie, broken toward the L06 letter at M; **)0** q 2/2 in R2 (R0 q/u tie) where passB had u 2/3; **6)** n 4/5 in R2
  but R0 ties n/o. **8)** p vs l (L03 pos0 / L19 pos20) unchanged. Witnesses in conflicts.tsv (2 Oct 2026 GAPS2 rows).
- What would settle them: the image pass of gap 2 (one line crop per call, gloss letter over the named groups only); an aligner
  cannot add letters passB did not record (L08 pos18, L10 pos14-15, L13 pos16, L14 pos17 still have none), and the five conflicts
  are each one witness against one or three, which no re-run of the same tool on the same letters can break (rule 3's
  third-attempt clause: the next instrument is the image, not the aligner again).

## H3 (GAPS4-na-schonenberg-1678-1716, 2 Oct 2026): the body is a cover-address instruction, and sense predicts letters for the unsettled codes
Status: untested by the image (sense only, grade I/M; nothing applied to key.tsv). Segmenting reading.txt L01-L14 (body/reading_body.txt)
reads "No abye[n]do nobe[d]ad en estas partes qu[e] [l]a de a[v]er muda(d)o e(s)te gouye(r)[n]o ... las que ybye(r)e del norte y de ytalya
... las qu[e] puedan ocurryr. Para (m)a(s) se(g)u(r)(y)da(d) de la [c]orespondenzya ... p[o]ndra solamente [e][n] sobre (s)cryto en esta
forma: a doña antonya de albanylla". Predicted values, one row each in body/sense_inferences.tsv: 8) = l (L03 pos0, as the L19 crib), 55 = v,
31 = d (L03; the L06 pixel x stands as a second witness), )2 = s at L03 pos15 / L14 pos6 and r elsewhere (homophone or two signs), 49 = r
(L04), 23 = n (L01, L04, L13) and r (L07), 14 = c (L04), 81 = d (L02 pos0), 58 = c (L12), 96 = o (L13 pos1) / e (L13 pos15). What would
settle it: the gap-2 image pass reading the gloss letter over exactly these groups (a confirmation at >= 10 of the 13 is the gate; the
L19 address written out as the "forma" is the sense-side corroboration of H1, not a control for it). Judge: body/judge_body.log -- every
rendering FAILs real_p05 on es17c7 and es while all 80 shuffled controls sit lower; the leaf's own gloss FAILs too (judge cannot decide).

<!-- family_run.py table: one row per run, appended by the tool, never edited by hand -->

| date (UTC) | family | parameters | seeds | CONTROL mean (range) | TARGET best score | judge | gate met | label |
|---|---|---|---|---|---|---|---|---|

## H3 result (GAPS7-na-schonenberg-1678-1716, 2 Oct 2026): image pass on the sense predictions
Two blind passes (not shown the predictions) + reconciliation: 10 of 11 predicted letters at the 12 codes agree with the leaf's own
gloss (L13 pos15 predicted e, read y); predictions shuffled across the same 11 positions, 20 seeds: mean 1.50, max 4, 0 of 20 >= 10.
Codes settled C: 23 n, 14 c, 55 z, 50 s, 34 a, 49 r, 11 a, 31 x, 8) l, [blot] NULL; 96 o/y per position. H1's 8) p/l conflict
resolves to l (L03 pos0 and L09 pos13 both l, with the L19 crib). body/image_pass/compare.log.
