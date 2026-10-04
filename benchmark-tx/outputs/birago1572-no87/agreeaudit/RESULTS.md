# TX-AGREEAUDIT result on Birago no.87 (4 Oct 2026, 05:18 UTC; pre-registration benchmark-tx/PREREG-agreeaudit.md, commit 7e7395d0)

Vision calls: 2 Sonnet subagent calls (G1: 110 items, 48 line crops; G2: 90 items, 39 crops), no reconciliation call.

| | G1 (f178r, f179r, f178v L01-10) | G2 (f178v L11-23) | pooled |
|---|---|---|---|
| planted caught (firm pick == original) | 3/6 | 4/4 | **7/10 = 0.70 < 0.80 gate: NON-TEST** |
| planted, original picked at any confidence | 5/6 | 4/4 | 9/10 |
| agreed-wrong flagged (truth: clerk sheet) | 0/15 | 2/11 | 2/26 |
| false flags on agreed-right, unplanted | 0/87 | 0/71 | 0/158 |
| paired fixed / broken if flags applied | 0/0 | 2/0 | 2/0 (sign test p 0.25) |

err_true (tools/tx_bench.py, no.87 eval): passC 0.053 (43/803, 0.040-0.071) -> flags applied 0.051 (41/803, 0.038-0.069)
(`passC_audit_applied.tsv`). Not adopted: the control missed its gate, and fixed 2 > broken 0 is p 0.25, short of 0.05.

What it says. The three missed plants were all L-confidence answers (two picked the original at L, one accepted the planted
label at L): the auditor hesitates rather than rubber-stamps, but the pre-registered firm-pick rule does not count a
hesitation. Picks equalled the shown label on 188/200 items; the false-flag rate is zero. The ceiling stated in advance
held the target side down too: only 8 of the 26 agreed-wrong signs have a truth sign among the k=3 candidates (the
other 18 are value confusions outside the look-alike pairs, e.g. e<-T76, t<-T90), and the auditor fixed 2 of those 8.
Next step (one line, not run): a second seeded packet with plants >= 20 so the catch estimate can clear 0.80 with a
usable interval, and k widened to the atlas top-3 (TRANSCRIPTION.md row 4) instead of confusion partners, which is
what limits the agreed-wrong ceiling; an L answer that names a non-shown label could be routed to the sorter focus.
