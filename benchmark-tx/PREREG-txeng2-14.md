# PREREG TX-ENGINEER-2 round 14 (lane incarnation 3, session_01P46fwsU5VTc1oJiV1sayg5, 9 Oct 2026 22:5x UTC by date -u; pushed BEFORE any read or score; Amendment 9 additions)

Rules as PREREG-txeng2-5's preamble. `tools/tx_register.py --check benchmark-tx/PREREG-txeng2-14.md` output before the spawn: `OK benchmark-tx/PREREG-txeng2-14.md: names register rows and states a difference` (exit 0).

## DV1b Today's pipeline on the dev leaf vivonne1573-f102r-dev: a dev baseline (TXE2-VIV102-BASE; Opus 5.5 worker, Sonnet adjudicator; cap 12; box 90 min; dev, never a look)
Nearest prior: S2-READ + S2-ADJ (the frozen pipeline's steps 1-4 on f.103r: two blind Opus passes under the folder's value-blind
sheet, reconcile, packet-shape Sonnet adjudication), DV1 / TXP-VIV102 (the dev item and its Sonnet-pass baseline), B3b (the same
read protocol priced per packet). What is different: the leaf (f.102r, dev; crops ciphers/fr16104-vivonne-spain-1572/images/
c105_f102r_L??_s{1,2}.jpg, 74 files, zero network) and the purpose -- a dev baseline of today's pipeline on this hand so that the
S2 failure classes (':' deletions, the 3/z pair, invented sign names, segmentation) can be studied with a known answer on a leaf
that is not the spent confirm2; the reader sheet is the S2 readers' sheet (txeng2/s2read/sheet_SIGNS.md) with S2-NOTE's 13
missing committed labels ADDED as tokens (t, Z, i, J, w, H), committed with sha256 and a changelog before any read -- a
baseline-side correction declared here, never an instrument; the brief says "do not resize" and carries the manifest-measured
overlap sentence (tools/overlap_audit.py, O1's method); readers never see truth, decodes, the key, the folder's f102r passes or
committed; one subagent call per <= 8 lines; reconcile_passes.py; ONE Sonnet adjudication in packet shape (<= 16 rows per call,
each crop viewed, viewed recorded per row; priced from the queue's row count, not a fixed 2); passZ_dv1.tsv with sha256; ONE
tx_bench run (--item vivonne1573-f102r-dev --exclude-flagged --paired committed.tsv, passA_dv1/passB_dv1 beside in the same run),
both figures, reported as a dev baseline (flagged-excluded binds, the truth's control margin is 0.003: no as-measured level is
read as a figure). Read-free beside the score: label counts of ':' 'S' 's' '3' 'z' in each pass vs committed, and the per-class
split of the flagged-excluded errors (segmentation / read / notation) by S2-NOTE's classify.py with S2-NOTE's map. The dev pool
grows by passZ_dv1's flagged-excluded count (recorded in a dated Amendment 9 line). Priced: 2 passes x 3 calls + ~13 adjudication
packets (f.103r's queue was 375 rows for 37 lines; f.102r has 20 lines) + 1 reconciliation unit. Openings of eval truth: 0.

Costs this round: 12. Eval looks this round: 0. Openings: 0.

## DV1b re-priced (lane, 9 Oct 2026 22:5x UTC by date -u; on the worker's pricing flag BEFORE any read; the lane's own error)
The lane priced f.102r at 20 lines; the BENCHMARK-TX row is f102r_L01-L37 (74 crops, 37 lines), the same size as f.103r. Re-priced per
unit from the nearest ledger rows (S2-READ 12.70 for 10 Opus calls + overlap check; S2-ADJ 5.40 for 13 packets): 5 calls per pass x 2 =
10 Opus reads, packets from the DISAGREE rows only (the S2-ADJ shape, which is the frozen step 3 as actually executed on f.103r; the
agreed-uncertain rows are kept as agreed), about 13 packets, plus 1 reconciliation unit. **Cap 22, box 120 min**; nothing else in the
section changes. The pipeline on the dev leaf is thereby identical to the S2 pipeline as run (steps 1-4 + the packet-shape repair).
Workers' stop rule unchanged (80% of either figure).
