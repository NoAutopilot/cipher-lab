# PREREG C1161-LKEY (14 Oct 2026, written 07:3x UTC by date -u, before any score)

Instrument: George Lasry's published key sheet for this item (sources/cyphersolver/2026-10-14-lasry/clair1161/lasry_p073_1.png;
"BnF cipher research", 10 Oct 2026; published by D. Bourdeau, cyphersolver dde5b0ea; text CC BY 4.0). No "?" marks on the sheet,
so each of his values is grade H for the key value; the label -> exemplar mapping is graded by its own agreement.

1. Mapping. Two blind Sonnet passes (lkey/matchA.tsv, lkey/matchB.tsv, same prompt lkey/match_prompt.md, neither shown the other,
   key.tsv or any reading) match each of our labels (tx/labels_v2.md) to a sheet exemplar. A label is MAPPED when both passes name
   the same plaintext value (same letter column, or the same nomenclature/null entry); otherwise UNMAPPED.
2. Concordance (lkey/concordance.tsv): per label, our value+grade / his value (mapped) / agree | disagree | new | unmapped.
   Disagreements on our S/C signs are a data conflict (rule 4): both recorded, not settled.
3. key_lasry.tsv (V1, the brief's variant): our value and grade for every S/C sign; for every M sign (and any U shape) that is
   MAPPED, his value, grade H (key) with the mapping noted; unmapped M signs keep our value at M. Single-sign substitution only;
   decoded through decode_lasry.json with tools/decode_key.py (--check exit 0).
   V2 (reported, not the gate): V1 plus his nomenclature applied to digit pairs as units (77 de, 76 le, 62 est, 55 que, 52 qui,
   48 fait, 37 ou, 30 quant, 60 puis, 44 il) and his nulls, only if both passes map the digit/null shapes; overrides S tokens, so
   reported as a data conflict count, never as grade H on our S signs.
4. Statistic: the spec judge's mean log10 4-gram per letter (tools/judge_plaintext.py NgramModel on the spec's fr16 corpora) of the
   whole decode; secondary, greedy word cover.
   Control (rule 3): 200 draws in which the values his key assigns to the CHANGED signs (M signs whose value V1 changes) are
   permuted among those signs (same multiset, same tokens, same positions; the key changes the text, so the control can differ).
   Gate: V1 score > p99 of the 200 permuted draws. Also reported: V1 vs our key.tsv score (baseline).
   If fewer than 3 signs change, the permutation null has too few distinct draws: logged "non-test (too few changed signs)".
5. Faces: per face (c185R, c186L, c186R, c187L, c187R, c188L) the longest run of consecutive letters covered by greedy-segmented
   lexicon words of length >= 3 (model.words), ours vs V1. A face "gains a readable stretch" when V1's longest run is >= 20 letters
   AND exceeds ours by >= 5 letters. Reported for the four faces he left "in part" (all but c186R and the one other he read; which
   one is not stated in his folder, so all five non-c186R faces are reported).
No key.tsv edit; no regrading of our tokens; no novelty claim.
