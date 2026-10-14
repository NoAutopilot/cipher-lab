# PREREG C1161-V2 (14 Oct 2026, written 07:5x UTC by date -u, before any V2 score)

Worker C1161-V2 for LANE DEFAULT-A1-0640-14 (account 1), brief `.claude/briefs/runs/2026-10-14-acct1-default-0640-jobs.md` Wave 4.
Instrument: George Lasry's published key sheet (sources/cyphersolver/2026-10-14-lasry/clair1161/lasry_p073_1.png; "BnF cipher research",
10 Oct 2026; published by D. Bourdeau, cyphersolver dde5b0ea; text CC BY 4.0), its nomenclature block: 77 de, 62 est, 55 que, 52 qui,
48 fait, 76 le, 37 ou, 30 quant, 60 puis, 44 il (### et, /// null, x-blot null not used: no two-pass mapping, C1161-LKEY).

Why a fresh PREREG: PREREG-C1161-LKEY.md made V2 conditional on both blind passes mapping the digit shapes; that condition was not met.
His nomenclature codes are typeset digits on the sheet (no exemplar crops), so no exemplar matching can map them; the mapping used here
is label-name identity (our labels 2 3 4 6 7 8 9 0 are named for digit shapes). That mapping is not two-pass agreement, so every
pair-unit token is graded **M** whatever the score (value from his sheet, mapping unverified). V2 yields 0 H tokens by construction.

1. Derived ciphertext `lkey/ciphertext_v2.tsv` (ciphertext.tsv untouched): within each line, left to right, two adjacent signs whose
   labels form one of his ten codes become one unit sign `n77`, `n76`, ...; greedy, no overlap (4877 -> 48 77; 776 -> 77 6; 377 -> 37 7).
   Pairs not in his list (84 x18, 42 x5, 67, 87, 83, ...) stay as single signs. Present (counted before scoring, structure only):
   77 x77, 76 x16, 44 x10, 37 x9, 48 x4 = 116 units, 232 digit tokens.
2. V2 (the gate): key.tsv for every single sign + his nomenclature value for each unit (`lkey/key_v2.tsv`, decode `lkey/decode_v2.json`,
   `tools/decode_key.py --config ... --check` exit 0).
   Statistic: the spec judge's mean log10 4-gram per letter (fr16 corpora, as lkey_score.py) on the whole decode.
   Rule-3 control: 300 draws, his ten nomenclature values permuted among his ten codes (so a present code takes any of the ten words,
   30,240 distinct assignments for the five present codes); same positions, same single-sign key. The key changes the text, so the
   control can differ. Gate: V2 > p99 of the null. Also reported: V2 vs baseline (key.tsv, pairs read as two letters) and vs V1.
3. V2b (reported, post-hoc selection, M at best even on a PASS): V2 plus the five single-sign values C1161-LKEY's post-hoc diagnostic
   found positive alone (8 c, rc s, tz l, c f, L s), z held at t, / and phi and to at ours. Control: 300 draws, nomenclature permuted as
   in 2 AND the five signs' values permuted among themselves. Gate form as in 2.
4. Known-answer (secondary, descriptive with its own null): on face c186R (his f163r paragraph, quoted in his folder NOTES), the share of
   his excerpt's letters covered by difflib matching blocks of length >= 4 against our decode (folded a-z), baseline vs V2 vs V2b, and the
   p99 of the same statistic under the V2 null draws. "Agrees better" = V2 > baseline and V2 > null p99.
5. Faces: per face longest run of consecutive letters covered by lexicon words of length >= 3 (lkey_score.py longest_run), baseline vs V2;
   a face "gains a licensed stretch" only if the gate in 2 PASSes AND V2's run >= 20 AND >= baseline + 5.
6. Data conflict (rule 4): count S tokens our key reads that a unit overrides (e.g. 7 = i S); recorded both ways, not settled.
No key.tsv edit; no regrading of our existing tokens; no novelty claim.
