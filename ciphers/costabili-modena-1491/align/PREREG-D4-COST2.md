# PREREG D4-COST2, 7 Oct 2026 (written and pushed before any reader call on the cipher crops and before any score)

Target: R1167 P1 page lines 7-16 (cipher, crops c1b_L01-L10 of `tools/iiif_lines.py --image IMG_R1167_I5857_P1.png --region
480,1380,1880,960 --out c1b --prefix c1b --ink 90 --prominence 30 --debug`, 10 lines) against the clear copy P5 lines 5-11 (crops
k5b_L01-L07 of `--image IMG_R1167_I5861_P5.png --region 380,1130,1950,800 --out k5b --prefix k5b --ink 90 --prominence 30`). D4-COST read
and scored only page lines 1-8 (spans s1, s2 up to the code x on line 6), so the scored stretch here (after "& poi" on line 7) is held out.
Images: one DECODE browser login 14:23 UTC, R1167 P1/P2/P5/P6, sha1 = images_manifest.tsv, scratch only. This worker looked at P1 lines 7-16
and P5 lines 5-11 at line-crop scale to place spans and read the copy (the plaintext source); no cipher sign was transcribed by this worker.

## Clear copy, P5 lines 5-11 as read by this worker (sigla shown as written)
L5 dicto Mons. lo Arciuescouo suo figliolo: Et poi lo oratori Regio liquali se
L6 ritrouorono presenti alo exponere de lambassata: La ambassata sua nō ha contenuto
L7 altro se non uisitatione e excusatione d-l S. Re: sel nō uisita sua m.ta p-sonalmente
L8 pch ancora il stae alquanto debilo p- rispecto d-la infirmita passata, e confortare
L9 sua m.ta ad non stare malo contenta ma a stare cum lo animo lieto e cum
L10 patientia expectare ch il se fari q-sta dieta ch se debbe fare pch a q-lla hora
L11 sua m.ta tractara dele cose sue cum li Baroni de sua m.ta usando formalmente

## Expansion table (fixed here, applied to the clear text before any score; the PX-BRODEC normalisation of CLAUDE.md rule 3)
| siglum as written | expanded | evidence of the copy's own usage |
|---|---|---|
| d with barred l stroke (d-l) | del | the standard siglum; "dele" written out L11 |
| d-la | de la | "de" written out L6, L11; "la" written out L6 |
| nō | non | "non" written out L7, L9 |
| p- (barred p) | per | "per" written out P5 L2 ("per questa") |
| p-sonalmente | personalmente | as p- |
| pch | perche | p- + che |
| ch (with stroke) | che | the standard siglum; "che" not written out on P5 (D4-COST), taken as the ruling's convention |
| q-sta, q-lla | questa, quella | "questo" written q-sto P5 L13; standard |
| m.ta | maesta | the standard siglum |
| uisita, uisitatione, ritrouorono | visita, visitatione, ritrovorono | u/v are one letter in the hand; the alignment string uses v where the word is v |
Abbreviated proper words with no clear role (Mons., Arciuescouo) fall outside the spans. Any further siglum met in a span and not in this
table drops that span before scoring (as D4-COST's registered rule did).

## Spans (sign stream = the pass's groups for c1b_L01..L10 in order; tokens `{CLEAR}` and `{CODE}` are markers, removed from the sign string)
Readers write clear words as `{CLEAR}` and a dotted code group (.30., .f., .13., etc.) as `{CODE}`; x is a sign label (code for "il S. Re").
- u1: from after the leading clear/code run of c1b_L01 ("ha dicto .30. & poi ...") to the first x (exclusive), clear =
  "lo oratori regio liquali se ritrovorono presenti alo exponere de la ambassata la ambassata sua non ha contenuto altro se non visitatione e excusatione del"
- u2: from after that x to the second `{CODE}` after it (exclusive), clear =
  "sel non visita sua maesta personalmente perche ancora il stae alquanto debilo per rispecto de la infirmita passata e confortare"
- u3: from after that `{CODE}` to the first `{CLEAR}` on c1b_L10 ("usando") (exclusive), clear =
  "ad non stare malo contenta ma a stare cum lo animo lieto e cum patientia expectare che il se fari questa dieta che se debbe fare perche a quella hora sua maesta tractara de le cose sue cum li baroni de sua maesta"
Code groups inside a span are removed from the cipher string; the clear text is kept whole (the alignment's gaps absorb what a code stands for).
A pass whose markers do not fall as stated (no x on c1b_L04, fewer than two `{CODE}` after x, no `{CLEAR}` on c1b_L10) loses that span for that pass.

## Statistic, control, gate: D4-COST's, unchanged
`align/d4cost2_score.py` imports `nw` and `stat` from `align/d4cost_score.py` unchanged: NW, +2 C value == letter, -1 differs, 0 non-C sign,
gap -1; real = share of C-valued sign tokens aligned to their own letter; null = the clear span's letters shuffled within the span, 20
seeds; gate per pass: pooled real >= null p95 + 0.20 and >= 4 C-valued tokens per span on average. Key: align/key_n9cos2.tsv C values.

## New values (D4-COST conditions a-d, unchanged, on this held-out stretch alone)
A sign without a C value goes to C only if (a) both passes clear the gate, (b) it aligns to a letter >= 3 times in each pass, (c) the modal
letter is the same in both passes with share >= 0.6 in each, (d) the modal letter occurs for that sign in >= 2 different spans.
TT (s?) and Z (t?) are tested this way. q rule: q goes to C only if q itself meets (a)-(d) for one letter; a q split by shape is not attempted
here (R9-COST: no reader-visible shape split); a q whose modal share is < 0.6 stays M and its letter counts are reported.
If any value passes, it is written to align/key_d4cost2.tsv (key_n9cos2.tsv + the new C rows, occurrences cited), and R1166 P4's
PREREG-R8-COST decode gate (C coverage of agreed positions >= 0.80) is re-scored with the same R8-COST passes and that key:
`python3 align/r8cost_score.py align/r8cost_reads/passA.tsv align/r8cost_reads/passB.tsv --key align/key_d4cost2.tsv`. The number is reported
either way; the gate is not moved.
Readers: two blind Sonnet calls over the 10 line crops (pass A top-down, pass B bottom-up), labels.tsv shapes + the RUN3-COSK2 dash
convention, no value, no clear copy, no key. Reconciliation by this worker (copy in view) licenses M at most.
Units: 2 Sonnet reader calls (~1.5 each) + scoring; Opus floor ~1.5; cap 5.
