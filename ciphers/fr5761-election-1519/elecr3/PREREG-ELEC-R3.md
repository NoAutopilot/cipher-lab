# PREREG ELEC-R3 (addendum to elecr2/PREREG-ELEC-R2.md; worker ELEC-R3, LANE DEFAULT-A1-1426-15, account 1, 15 Oct 2026, 14:4x UTC by date -u)

Written and pushed before any fetch and before the reader call. The registered rule, the targets, the decoys, the shuffle (seed 20261015,
labels T1-T6 as in elecr2/reader2_result.tsv) and the reader task are exactly ELEC-R2's. Only the crops change:
- Panel A: f.51r lower part, the same region (canvas105 1500-px frame x 0-1500 y 1250-2050), fetched at native resolution from
  openapi.bnf.fr IIIF v3 as `pct:0,56.84,100,36.38` /max/ (1 request), plus two zooms cut locally from that same fetch: the lower key block
  (1500-px frame x 0-700 y 1270-2000) and the side note (x 620-1500 y 1560-1860), given as A-block and A-note (same panel A for scoring).
- Real target crops re-fetched at native resolution (ELEC-R2's scratch is gone): c336 one region covering oXo and Lfo
  (`650,180,1500,1580`, cut locally into ELEC-R2's two regions) and c335 `860,2780,400,170` (cut into Phi and Hbar halves); 2 requests.
- Decoys and panel B from disk as before (canvas109 f.53r Colonien and palatinus; canvas106 f.51v), 1500-px frame.
- openapi.bnf.fr <= 3 requests in all; crops in the session scratchpad only, never git.
Scoring: ELEC-R2's rule unchanged (PASS iff >= 3/4 real targets to their own panel-A row AND 0/2 decoys to any panel-A row). Reported per
target and decoy: agree/disagree with R1 (ELEC-VERSO) and R2 (ELEC-R2). Note: second name reported as read; "Orval" counted only if the
reader gives an O-initial -rval form unprompted. Grade M whatever the result; no key.tsv edit.
