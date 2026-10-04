# fr16045-pisany-rome-1585 -- hypotheses and data conflicts (append-only)

Opened 4 Oct 2026 (RUN5-PIS3). Rule 4: a key cell whose witnesses disagree is a data conflict, recorded with its witnesses,
never settled by the more frequent value alone.

## key86 T31: table m vs page o (RUN4-PIS1 finding; logged RUN5-PIS3, 4 Oct 2026)

Sign: SIGNSHEET86 cell T31 ("x with hook", the hand's x/gamma form). Correspondence: Jean de Vivonne, marquis de Pisany,
ambassador in Rome, to Henry III (fr.16045), 1586-87 key. Witness table built by `kp86e/t31_grades.py` ->
kp86e/t31_witness.tsv (same key86-anchored alignment as kp86b/cgrades.py; a T31 token decoded as m, the copy letter it
aligns to).

| value | witness | letter (sender -> recipient, date) | how read | count / strength |
|---|---|---|---|---|
| m | Tomokiyo's table "Vivonne's Cipher (1586-1587)", sources/cryptiana henryiii_Vivonne5.png, row 2 under m (x~237); cut checked correct (kp86b/cellcheck_a.md) | the table covers 1586-87; no letter named for this cell | published modern key table (circled, "with n2") | 1 cell |
| o | Tomokiyo's own printed specimen reading of f.244r (henryiii.htm): voudroit, retourner, pouvoir, soupcon at T31 places | Pisany -> Henry III, Rome 17 Sept 1586 | the same author's decipherment of the page | 4 places |
| o | Colbert 16 pt II pp.49-50 clear copy vs f.244r tokens | Pisany -> Henry III, 17 Sept 1586 (f.244r) | key86 alignment to the period copy (kp86 PASS) | o 6, u 1, gap 4 of 11 |
| mixed | Colbert pp.51-52 vs f.244v + f.245r | same letter, postscript (f.244v-f.245r) | alignment (kp86c PASS) | o 1, t 1, i 1, gap 2 of 5 |
| mixed, mostly s | Colbert pp.121-123 vs f.275r (kp86e per-line passes) | Pisany -> Henry III, Rome 4 Nov 1586 (f.275r) | alignment; see kp86e verdict in NOTES.md | s 6, e 2, f 1, m 1, n 1, o 1, gap 1 of 13 |

Reading of the witnesses: on 17 Sept 1586 f.244r the page form labelled T31 is o (the copy and Tomokiyo's own reading
agree); the table cell says m. The other pages do not repeat that: on f.275r the readers' T31 tokens align mostly with s
(key86 s-cells are T17, T36, T49; the readers' T31 there may be another sign, and kp86d/reconcile_d.py's pair rule folds
T45/T31 into T31). So the label T31 as the readers use it is not one page sign, and the conflict is not settled by any
clear copy across letters.

Standing: key86.tsv unchanged (T31 = m, as published). Grades: every T31 token is M on every page (not C), unless a later
test settles the cell; arm B's remap T31->o stays a fitted label remap reported beside arm A, never in key86.tsv. What would
settle it: an image comparison of the T31-labelled tokens on f.244r (L03 tok 6, L09 tok 21/27/31) against those on f.275r
(t31_witness.tsv rows) and against the table cell, then the period interlinear letters over f.244v L02-L03 / f.245r
L04-L05 where they stand over a T31 token.

### T31 image compare (RUN5-PIS4, 4 Oct 2026, one look by the worker, no subagent)
Crops on disk only (f244r_L03_s1/s2, f244r_L09_s2, f275rL_L04_s2, f275rL_L05_s1) beside the table cells of
henryiii_Vivonne5.png: images/t31_compare.jpg (p1-p4 f.244r, q1-q2 f.275r, t31/t36/t45 table cells).
- f.244r, 4 of 4 T31-labelled tokens looked at (L03 tok 6, 26, 36; L09 tok 31): one shape, an x whose right arm
  closes in a loop (a flattened "p"/rho form). It is not the table's bare x under m (T31); it is closest to the
  table's circled loop sign under o (T45). The copy reads o at these places.
- f.275r, 2 of 2 looked at (L04 the x before T30 near the line end; L05 tok 1): a crossed x with a hooked arm,
  followed at once by a small o. That is the table's s cell "x with o" (T36, circled with r2); the readers cut it
  into T31 + T30. The copy reads s at both places.
- So the page signs are **two shapes**, neither the bare table x: the label T31 as the readers used it merges a
  T45-like loop form (o) on f.244r and a T36 x+o form (s) on f.275r. The table cell (T31 = m) is not contradicted
  by any token looked at; the "conflict" reads as a reader-label merge, not a table error.
Standing unchanged: key86.tsv untouched, every T31 token stays M (rule 4: the shape match is an eye read at
crop resolution, not the clear copy deciding each token). Next: re-label the T31 tokens of f.244r/f.275r by shape
(loop -> T45, x+o -> T36) as a pre-registered relabel of the existing tsv files, then re-run kp86b/kp86e arm A
unchanged and see whether these tokens move to C, disk only, ~$1.

### kp87b witness (PIS1-302, 4 Oct 2026): f.302v alignment against the Colbert copy, cells the PASS contradicts
From kp87b's arm-A alignment (tx87b/ciphertext_f302v.tsv vs kp87b/colbert_p341_342.txt, err_2reader 0.335; per-sign
aligned copy letters by the same band_dp as kp87b/cgrades87b.py). Witness only; key86.tsv unchanged.
- T57 (table la): 0 of 6 C; aligned copy letters n 4, u 2 -- agrees with REMAP_B's T57 -> n (kp86d).
- T47 (table m): 0 of 4 C; aligned f 2, e 1 -- agrees with REMAP_B's T47 -> f.
- T40 (table a): 0 of 12 C; aligned s 5, r 1, o 1 -- new on this page; may be a reader-label merge (cf. T31) rather
  than a table error; not seen on f.301v/f.275r as a conflict. Next: image compare of the f.302v T40 tokens with the
  table's a and s cells, disk only.
- T31 (table m): 9 tokens, aligned m 3, o 3, t 1, r 1: still split. Rule 4: every T31 token stays M (3 that
  cgrades87b scores C are counted M in NOTES).
Arm B (key86 + REMAP_B) scored 0.621 vs arm A 0.590 on the reconciled page (blind A 0.571 vs 0.553, blind B 0.630
vs 0.598): B above A on a fourth page, by 0.017-0.032. Still not a held-out test (PIS1-KEY's job).

## kp86f witness (PIS1-275V, 4 Oct 2026): f.275v lines 1-16
Arm A PASS (0.622 vs p99 0.419 / 0.482, control 5/5 at err 0.181). T31 (table m): 15 tokens, aligned o 5, e 4, m 3, i 1,
gap 2 (kp86f/t31_witness.tsv): still split, a fifth page where the table's m is not the majority. All T31 tokens M.
Arm B (T31->o, T45->u, T47->f, T57->n) above A by 0.009 (reconciled), 0.010 / 0.006 (blind A / B): the same small margin as
on the other pages; not a held-out test (that is PIS1-KEY's). key86.tsv unchanged.

## kp86g witness (PIS1-247, 4 Oct 2026): f.247r (second 17 Sept 1586 letter)
Arm A PASS (0.639 vs p99 0.431 / 0.494, control 5/5 at err 0.268). T31 (table m): 7 tokens, aligned o 2, m 2, a 1, s 1, gap 1
(kp86g/t31_witness.tsv): still split; all T31 tokens M. Arm B above A by 0.025 (reconciled), 0.010 / 0.026 (blind A / B): the
same small margin as on the other pages; not a held-out test (PIS1-KEY's). key86.tsv unchanged.

## PIS1-KEY held-out remap and T31 relabel (PIS1-KEY, finished by PIS1-KEY2, 4 Oct 2026)
Pre-registered pis1key/PREREG_pis1key.md; details NOTES.md "key86 T31 relabel and held-out remap".
| hypothesis | instrument | control | target | verdict |
|---|---|---|---|---|
| T45->u, T47->f, T57->n (fit on f.244r+f.244v/f.245r) | pis1key.py remap, held out f.275r / f.301v | kp86d control 5/5 / 5/5 at e 0.215 / 0.192 | 0.656 / 0.663 vs arm A 0.647 / 0.630; degenerate all-e 0.643 / **0.644** | joint gate FAIL (G3 on f.301v); key86 unchanged; retired for this instrument |
| T31 tokens are page signs T45 (f.244r) / T36 (f.275r) | pis1key.py relabel, arm A | f.244r 5/5; f.275r not re-run (kp86e 5/5) | f.244r 0.677->0.695, f.275r 0.647->0.657, above both p99s | SUPPORTED in aggregate; tokens stay M; key86 T31 = m unchanged |
Witnesses beside it, not key changes: PIS1-302 f.302v (kp87b) T57 -> n 4 of 6, T47 -> f 2 of 4, T40 (table a) -> s 5 of 7 aligned
(section "kp87b witness"); PIS1-275V f.275v (kp86f) T31 aligned o 5, e 4, m 3, i 1 (section "kp86f witness"). T57 -> n is also the
one cell that alone beats arm A on both held-out pages (0.654, 0.658), but the per-cell rule needs the joint gate, which failed.
