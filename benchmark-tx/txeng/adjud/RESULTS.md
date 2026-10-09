# TXE-K results: stronger-model adjudicator of A/B splits (M19), Birago no.87 dev_tune (9 Oct 2026, 07:56 UTC by date -u)

PREREG: `PREREG.md` (pushed dd9be65b8 before any read). Raw reads committed before scoring (7b15404ca and earlier):
`reads/{fable,opus}_call0{1,2}.tsv`, joined `reads/{fable,opus}_dev_tune.tsv`.

## Verdict: FAIL, both arms; no eval look taken (0 of 1)
| arm | paired vs L_dev_tune (gate fixed > broken, p < 0.01) | err_true | items right / 36 | worse than Sonnet on an item |
|---|---|---|---|---|
| Sonnet third reader (passC, committed) | baseline | L 0.041 (14/343) | 35 | - |
| Fable (`model: fable`) | fixed 0 / broken 1, p 1.0 | 0.050 (17/343; 15 wrong + 2 inserted) | 32 | 3 (items 18, 27, 35) |
| Opus 5.5 (`model: opus`) | fixed 0 / broken 1, p 1.0 | 0.044 (15/343) | 34 | 1 (item 18) |

Register verdict: **adjudication by a stronger model does not beat the Sonnet third reader on this hand**; Fable is the weaker of
the two adjudicators (32 vs 34 of 36), as it was the weaker line reader in TX-FABLE.

## Why the gate could never be met here (headroom, CLAUDE.md rule 3)
The committed Sonnet adjudication is already right on 35 of the 36 items; only ONE of L's 14 dev errors sits on an item position
(item 34, f178v L11 pos 29: passC chose A's T60, B's T86 was right). Maximum possible fixed = 1, so p < 0.01 was unreachable by
construction -- the prediction in PREREG.md said a pass was unlikely. The gain question on dev_tune is therefore a non-test; what
the run does measure is breakage: both stronger adjudicators broke a position the Sonnet adjudication had right. L's other 13
dev errors are positions where A and B AGREED (wrong-in-every-pass, taxonomy below): adjudication cannot reach them at all.

## Packet defect found by the readers (reported, not corrected after the fact)
The bracket comes from the label-blind box<->position map (`benchmark-tx/txeng/compare/box_pos.tsv`). Both readers flagged it as
one sign off on item 18 (L07 29: "the bracket sits on a plain cross"; both answered T85) and on items 33-35 (L11 14, 29, 31-32;
Fable: "the sign both options describe sits one sign to the right"). Item 34, the only fixable item, is one of them, so the one
chance of a fix was lost to geometry. Post hoc (not gating, not a re-score): treating "other cell" answers as abstain would leave
Fable broken 0 on item 18/35 and Opus broken 0, still fixed 0. Follow-up (one line): a re-run needs the bracket from the line
read's own positions, verified per line against the crop (or the ordinal form the brief asked for), and a unit whose errors are
on split positions -- on this hand the splits are already settled correctly by Sonnet.

## tx_bench (pasted)
```
birago1572-no87 [eval] err_true 0.050 (17/343) 95% 0.031-0.078 | wrong 15 deleted 0 inserted 2 | excluded 11 | lines missing 17
paired passS_adj_fable_dev_tune.tsv vs labels_dev_tune.tsv on birago1572-no87: 343 common scored signs; base wrong 14, output wrong 15; fixed 0, broken 1; sign test p = 1.0000
birago1572-no87 [eval] err_true 0.044 (15/343) 95% 0.027-0.071 | wrong 15 deleted 0 inserted 0 | excluded 11 | lines missing 17
paired passS_adj_opus_dev_tune.tsv vs labels_dev_tune.tsv on birago1572-no87: 343 common scored signs; base wrong 14, output wrong 15; fixed 0, broken 1; sign test p = 1.0000
```
(tx_bench labels the dev lines "[eval]" by its own split column; the unit is dev_tune.) Item scores: `score_items_dev_tune.tsv`
(`tx_adjudicate.py score`: Sonnet wrong only on 34; Fable wrong on 18, 27, 34, 35; Opus on 18, 34).

## Taxonomy (`tools/tx_taxonomy.py`, `taxonomy_dev_tune.md`)
L 14 / Fable 15 / Opus 15 wrong-or-deleted; every L error is repeated by both arms (14/14); 14 positions wrong in every pass,
0 wrong in exactly one. No class moved: the arms add one error each (Fable: L07.29 s <- T85 plus two inserted signs from its
three-sign answer on item 35) and fix none.

## Items, packet, task text, calls
36 items (44 non-agree rows of passC_agreement.tsv L01-10 + passC_L11-23_agreement.tsv L11-12, merged into runs), 8 sheets of 5,
2 calls per arm (18 items each). Answers: Fable 19 opt1 / 9 opt2 / 8 other / 0 ?; Opus 19 / 12 / 5 / 0.
Reader task text (each of 4 calls, N = 1 or 2, arm = fable or opus):
"Read /home/user/cipher-lab/benchmark-tx/txeng/adjud/dev_tune/call_0N.md and do exactly what it says. Open no other file than the
images it names. Write your TSV to /home/user/cipher-lab/benchmark-tx/txeng/adjud/reads/<arm>_call0N.tsv." The call file
(`dev_tune/call_0N.md`) carries the sheets, the sign sheet and the options; no truth, base, passC or key.
Vision calls: 4 (Fable 2, Opus 2), none on eval. Subagent tokens: Fable 127,497 + 140,384 = 267,881 (25 and 33 tool uses,
185 s and 301 s; it re-cropped the sheets to check the brackets); Opus 109,942 + 110,880 = 220,822 (46 s, 53 s).
Tool: `tools/tx_adjudicate.py` (items / packet / resolve / score), test `tools/tests/test_tx_adjudicate.py` (offline, ok).
