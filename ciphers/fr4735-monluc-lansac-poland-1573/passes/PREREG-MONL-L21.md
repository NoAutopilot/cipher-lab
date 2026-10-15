# PREREG-MONL-L21: c268 L21-L25 transcription and alignment (15 Oct 2026, account 4, for LANE DEFAULT-A4-1035-15)

Written and pushed before any crop is cut, any pass is run or any score is computed. Method exactly MONL-L16's (NOTES.md "MONL-L16"):
ids-only key sheet (images/keysheet_monluc1_ids.png), no value, reading, decode or clear text shown to the readers; two blind Sonnet
passes; reconciliation by this worker's eye on the native line crops **before** the clear text facing L21-L25 is opened; then
score_c268.py / align_c268.py / decode_key.py.

**Deviation (pricing, stated before the run).** MONL-L16 used one call per line per pass (10 calls); this job's brief prices 3 units
(pass A, pass B, reconciliation) at ~1 each. So each pass is ONE Sonnet call carrying all five lines' crops (10 images), with the
same per-line prompt wording repeated per line. Pass B carries MONL-L16's extra sentence ("work carefully sign by sign; read segment
2 before segment 1 if that helps you check the overlap") and lists the lines in reverse order (L25 first).

**Crops.** regen_monll21.sh: one openapi.bnf.fr region on f268 below MONL-L16's (600,3650,3100,800), tools/iiif_lines.py with
MONL-L16's options. Line identity from the debug overlay: the top band must be L20 (its last sign, a C-curl K38 after a flagged cross
K62, MONL-L16 L20:29-30); if it is not identifiable, stop and log, no pass is run. Crops stay untracked (self-ignoring .gitignore).

**Scoring (registered).**
- Pass agreement (sequence match) reported per line and in total, as agreement, not accuracy.
- Reconciled tokens: conf H where both passes agree, M otherwise (eye decision or pass A).
- Alignment: align_c268.py as committed (200 shuffled-clear draws, seed 140; f.139 c270 other-letter control), on L21-L25 alone
  (`--lines`) and on L01-L25. The band is reported as **running on** from L20 only if L21-L25 alone beats its own shuffled-clear p95
  AND 0/200 shuffled draws reach the real share; otherwise it is logged as "band not placed" and the reading of L21-L25 stays
  U/M (no C grade from the alignment), and nothing else in L01-L20 changes.
- L01-L25 committed run is kept only if it stays 0/200 at or above the real share.
- No key edit, no relabel of L01-L20 tokens in this job. Watch for the "adhuc" group K66 K49 ?h_bar K35 K15 (log, no action).
- Optional second step (K04-for-n --try) only if >= 30% of the 4.5 cap is left by estimate after the reconciliation; otherwise skipped
  and left as the next step.
