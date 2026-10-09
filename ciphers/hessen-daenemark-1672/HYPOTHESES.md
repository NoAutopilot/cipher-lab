# hessen-daenemark-1672: hypotheses and data conflicts

## Nomenclator conflicts with HCPortal key 255 (logged GAPS163, 3 Oct 2026, account-4; rule 4)

Key 255 (HStAM 4 d Nr. 1234 ff.13-16, "Clavis ... mit Secretario Lincker 1666") and this letter's own bold-hand glosses
give different values for two codes. These are not settled by majority, and neither value is merged into the other's
row: key_gloss.tsv carries the letter's gloss value, and key.tsv carries only key 255's letter table, no nomenclator.

| code | letter gloss (witness) | key 255 (witness) | reading |
|---|---|---|---|
| 229 | Berlin: p2:17 and p3:5, both blind passes read the gloss both times (C) | Frankreich: key 255 f.13-16, 1666, same sender family (Lyncker to the Kassel chancery) | different list; the letter's 229 stays Berlin (C) in this letter only |
| 303 | allian?e: p3:26, one letter unsettled (M) | Munster: preview read of keys/hcportal_key255_0014.jpg (M) | different list; 303 stays M |

Context: every other gloss-pinned nomenclator code here (437, 447, 601, 602, 605, 625, 634, 641, 651, 653, 681, 690,
768, 774, 775, 834, 5756) lies above key 255's 180-407 range. Key 255 also has Dennemarck at 184 and 212, where the
letter has 601, 602 and 605. So the 1672 letter used a different nomenclator, with the letter table kept, or nearly
kept: see NOTES.md GAPS163, where 2 of 7 letter-glossed groups disagree with the 1666 table. Witness direction and
date: the letter is Lyncker (Hamburg) to Chancellor Vultejus (Kassel), 4/14 May 1672 (M, siblings lookup). Key 255 is
dated 1666 and names the same secretary. Neither witness is an H-grade period decipherment of this letter's codes,
except the gloss itself.

## Nomenclator list identification (GAPS176, 3 Oct 2026, account-4)

| hypothesis | control | target | verdict |
|---|---|---|---|
| a key table on disk carries the 1672 nomenclator (18 gloss-pinned codes) | positive control, 3/4/6/9 planted values in a decoy key: real 3/4/5/8 vs shuffle p99 2/2/2/3, all flagged | 224 key tables: 0 hits in total, 0 candidates (shuffle p99 0 for every key) | no list on disk; DECODE 1650-1690 Marburg/Danish keys = 4687-4692, all opened, none matching; list needs the archive (keys/nomen_list_match.py) |

## Nomenclator bracketing (GAPS193, 3 Oct 2026, account-4; PREREG-GAPS193.md)

| hypothesis | control (K=16, code+mark, noise 0/0.2/0.4) | target | verdict |
|---|---|---|---|
| one-part alphabetical nomenclator (S1, Kendall tau) | power 1.000/0.989/0.807, size 0.051/0.047/0.040 | tau 0.194, p 0.172 | control-backed negative at K=16 |
| topical-block nomenclator (S2, same-topic adjacent pairs) | power 1.000/0.769/0.318, size 0.017/0.026/0.016 | 5 pairs, p 0.014 | non-test at this N (power < 0.8 at noise 0.4); not support |

## Context fill of unread nomenclator groups (D4-HDK, 7 Oct 2026, account-4; PREREG-D4HDK.md)

| hypothesis | control (14 held-out C-grade gloss tokens, 28 referents) | target | verdict |
|---|---|---|---|
| a de17 word-bigram context fill recovers nomenclator values (625, 634, 602) | top-1 0.071, MRR 0.208 vs shuffled-context null p95 0.314; prior-only top-1 0.000 | not scored (gate FAIL); record-only ranks in keys/context_fill_d4hdk.tsv | CONTROL BELOW GATE: instrument non-discriminating at these contexts; key-rebuild [retired] (keys/context_fill_d4hdk.py) |

| BRANDT-TX (9 Oct 2026): the period margin gloss of Dänemark 131 0020 is a letter-level decipherment of its lower block (interlinear_align, 10 clear-word anchor pairs, PREREG-BRANDT-TX) | 200 gloss derangements: CONSISTENT mean 6.13, p95 10, max 12 | CONSISTENT 9, p = 0.149; exploratory agrees 95 vs derangement max 49 (p = 0.005, not a gate) | FAIL (pre-registered); next: pre-register the agrees count + held-out 0049 |
| BRANDT-GATE test 1 (9 Oct 2026, PREREG-BRANDT-GATE.md 13865ab70): token agrees count of interlinear_align on pairs_0020.tsv (registered form of BRANDT-TX's exploratory statistic) | 2000 gloss derangements, seed 20261009: mean 33.53, p95 43, p99 48, max 54 | agrees 95, p = 0.0005 | PASS (real > max, p < 0.01) |
| BRANDT-GATE test 2 (9 Oct 2026, same prereg): key_0020.tsv's 58 single-letter values predict the period one-letter glosses of the held-out 0049 slip + left-page foot | 2000 permutations of key_0020's value->letter assignments: mean 3.76, p99 12, max 20 (sensitivity without the 8 groups HDK-131 had noted: mean 3.37, p99 11) | 34/48 scorable groups (sensitivity 28/42), p = 0.0005 | PASS (real > p99); 16 values grade C, 8 disagreeing values M (dk131_brandt/values_gate.tsv) |
| BRANDT-UP (9 Oct 2026, PREREG-BRANDT-UP.md committed before scoring): values_gate.tsv's 16 C values predict the period gloss letters over two further glossed blocks (0020 right-page head block, margin gloss; 0021 top, interlinear), LCS of C-letter sequence vs gloss letters summed over blocks | 2000 permutations of the C values' letters, seed 20261009: mean 15.58, p99 19, max 20 | LCS 23 of 25 C-value tokens, p = 0.0005 | PASS (real > p99, p < 0.01); 23 tokens C, 29 M (reading_up.tsv, grade_up.py --check) |
| V-BRANDT (9 Oct 2026, verifier, dk131_brandt/v_brandt.py --check): re-run of BRANDT-GATE tests 1-2 and BRANDT-UP at fresh seeds and on blind inputs | test 1 derangements seed 777: mean 33.79, p99 48, max 56; test 2 permutations seed 31337: p99 12; UP permutations seed 31337: p99 16 (glossA20u), 17 (glossB20u) | test 1 95 (same statistic and pairs BRANDT-TX had seen: confirmation, not independent); test 2 blind pass A 33/48, blind pass B 30/49; UP blind glossA 15, glossB 16 | test 2 HOLDS on blind input; UP FAIL on blind gloss (PASS only on the worker's gloss settled with the values in view): UP's 23 C tokens -> M; value 46 -> M (15 C, 9 M) |
