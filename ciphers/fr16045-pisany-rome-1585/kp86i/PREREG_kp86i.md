# PREREG kp86i -- fr16045 f.275v block B lines 12-15 (L17-L20) vs the Colbert p.123 copy extended to the end of the passage (RUN6-PISFIN, 5 Oct 2026)

Written and pushed before kp86i is run. kp86h Test 2 (kp86h/PREREG_kp86h.md) unchanged except the copy span.

Copy span (the one change). kp86h/colbert_f275v.txt ended at "seureté d'icelle". Colbert 16 pt II p.123 (Gallica btv1b100341061 c480,
right page, read once at 1400 px this job, scratch only: `https://gallica.bnf.fr/iiif/ark:/12148/btv1b100341061/f480/pct:50,0,50,100/1400,/0/default.jpg`)
continues: ", a laquelle elle porte toute affection amour et bienveillance, et qu'encore entendant Vostre Majesté que Sa Sainteté en
recevoit plaisir, elle s'y efforceroit tant plus volontiers." and then begins a new sentence "Elle fut ..." running onto p.124.
kp86i/colbert_f275v.txt = kp86h/colbert_f275v.txt + exactly that string (spelling normalised as the existing file: apostrophes,
accents on Majesté/Sainteté). Why it ends at "volontiers.": the RUN6-PIS descriptive decode of L18-L19 reads "s'y efforceroit ...
plus volontiers", and "volontiers." closes the sentence and the last full sentence on p.123; nothing of "Elle fut" is in the decode.
The span is fixed from the copy and that sentence boundary, not from any scored run.

Unchanged: tokens tx86h/local_ciphertext.tsv (+ tx86h/local_passA/B.tsv as blind passes); kp86d/kp86d.py statistic (nw_score),
key-shuffle 1000 and order-shuffle 1000 nulls (p99), seeds, arms A (key86.tsv) and B (key86 + RUN4-PIS1 remap, beside A only);
--inms phrase unchanged (from "ou je suis que je ne la sors" to "je dis au Pape,", control plaintext only). Wrapper kp86i/kp86i.py =
kp86h/kp86h.py with COPY and output names changed only.

Control: positive control at err 0.223 (the measured L17-L20 two-reader error, 1 - 136/175, as the brief names; kp86h ran 0.190, the
full-page figure; 0.223 is the harsher), 5 seeds, 200/200 nulls, pass >= 4/5, N = local decoded-letter count.

Command: `python3 kp86i/kp86i.py --local --err 0.223 --inms "<phrase>"` -> kp86i/kp86i_local_result.json, log kp86i/kp86i_local_run.log.
Gate per arm (as kp86d-h): PASS if the reconciled target > p99 of both nulls AND that arm's control passes; control fails -> NON-TEST;
target fails at err > 0.10 with control passing -> FAIL at that e. One run, no parameter change after it.
Grades: arm A PASS -> L17-L20 tokens regraded C where the decoded letter aligns identically to the copy (kp86h/grades_f275v_h.py with
the kp86i copy, L17-L20 rows only; L01-L16 grades stay kp86h's), T31 tokens M; otherwise L17-L20 stay M and kp86h/grades_f275v.tsv stands.
