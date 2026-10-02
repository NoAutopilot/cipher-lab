# castelcicala-1816 -- hypothesis families

Append-only. Rows below are written by `tools/family_run.py` (CLAUDE.md rule 3: the matched CONTROL number sits beside the TARGET number in every row; a row with gate met = no reports a control that could not read its own design, and the target was not run). Prose sections may be added above this table by workers.

<!-- family_run.py table: one row per run, appended by the tool, never edited by hand -->

| date (UTC) | family | parameters | seeds | CONTROL mean (range) | TARGET best score | judge | gate met | label |
|---|---|---|---|---|---|---|---|---|
| 2 Oct 2026 23:50 | seeded_code | N=9388 K=1269 restarts=4 corpus=bub_gb_ODloWJYQNSYC.txt.gz+bub_gb_jVdaVPIiH8sC.txt.gz+saggiostoricosul00cuoc.txt.gz+storiadelreamedi00coll.txt.gz+storiaditaliadal01bottuoft.txt.gz pins=ciphers/castelcicala-1816/key.tsv,iters=300000,words=1000 | 1-3 | 0.070 (0.052-0.100) | not run (CONTROL BELOW GATE) | - | no (gate 0.6) | A2-CAS8 matched control, 165 key.tsv values pinned, run=6 bracket=8, it19 LM |
| 2 Oct 2026 23:51 | seeded_code | N=9388 K=1269 restarts=4 corpus=bub_gb_ODloWJYQNSYC.txt.gz+bub_gb_jVdaVPIiH8sC.txt.gz+saggiostoricosul00cuoc.txt.gz+storiadelreamedi00coll.txt.gz+storiaditaliadal01bottuoft.txt.gz pins=ciphers/castelcicala-1816/key.tsv,iters=300000,words=1000,pinshare=0 | 1 | 0.028 (0.028-0.028) | not run (control-only) | - | no | A2-CAS8 blind baseline (headroom check, no pins) |
