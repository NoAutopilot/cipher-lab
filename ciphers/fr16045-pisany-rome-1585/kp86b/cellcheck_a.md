# Unit (a): key86 cell eye check, T31 T45 T47 T49 T57 (RUN4-PIS1, 4 Oct 2026, disk only)

Inputs: kp86/anchored_map.tsv (RUN3-PISA), per-occurrence contexts from kp86b/cellctx.py (same key86-anchored alignment),
the f.244r crops (L03, L05, L08, L09 viewed), tx86/SIGNSHEET86.png and Tomokiyo's table zoomed by column
(sources/cryptiana/web/henryiii_Vivonne5.png; header centres m ~x230, n ~255, o ~279, s ~370, t ~391, u ~414).

| Label (sheet sign) | key86 | Table placement checked | Page sign carrying the label (crops) | Aligned clear | Finding |
|---|---|---|---|---|---|
| T31 (x with hook) | m | under m, row 2 (x~237): cut is right | the hand's x/gamma form (L03 tok 6, L09 tok 21/27/31); RUN3's rule 4 also folds A's T45 into T31 | o:6 u:1 of 11 (sorte, voudroit, retourner, pouvoir, auroient) | conflict inside Tomokiyo's own page: his printed specimen reading of this passage has o at these places (voudroit, retourner, pouvoir, soupcon); candidate table correction m -> o, or this page form is his circled o-cell drawn differently. Not settled from the table alone. |
| T45 (circled rho) | o | under o, row 3 (x~279): cut is right | L08 tok 2 is the looped f-with-cross form = sheet T19 (u) | u:5 o:3 e:2 | transcription confusion with T19 (u): avec, fust, asseurement. Label-level value u. |
| T47 (k) | m | under m, row 4 (x~237): cut is right | L05 tok 1 is the k with a looped top = sheet T27 (f, row 2) | f:3 | transcription confusion with T27 (f): confidences, fust. Label-level value f. |
| T49 (inverted T) | s | under s, row 4 (x~372): cut is right | L05 tok 43, L08 tok 3 and 20 are the cross/tau form = sheet T21 (y); L06 tok 5, L07 tok 2 read s | y:2-3 s:2 | split: some tokens are T21 (y) misread, some true s. No label-level change (no majority). |
| T57 (circled omega, "la") | la | word row (x~325): cut is right | L05 tok 12, L08 tok 21 are the pi-over-w form = sheet T32 (circled, n) | n:5 c:2-3 | transcription confusion with T32 (n): intelligences, entretenir, ruinez, nulle. Label-level value n; the c cases not checked on the image. |

Result: the table is cut correctly for all five cells; four of the five flags are readers putting a page form on the
wrong sheet cell (T45 for T19, T47 for T27, T49 partly for T21, T57 for T32), not errors in Tomokiyo's table. T31 is the one
real conflict: the table puts the sign under m, but Tomokiyo's own specimen reading and the copy both read o there.
Arm B for the pre-registered test (kp86b/PREREG_kp86b.md) is therefore a label-level remap fitted on f.244r --
T31->o, T45->u, T47->f, T57->n -- which corrects the readers' habitual confusions as well as the one cell; it is not a
corrected publication of the table, and the main arm keeps key86 unchanged.
