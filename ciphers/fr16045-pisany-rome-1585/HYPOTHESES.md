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
