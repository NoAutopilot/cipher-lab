# PREREG-SUP-MONLUC-L26: c268 L26-L30 transcription and alignment (20 Oct 2026, 03:2x UTC by date -u; account 2, Opus, job SUP-MONLUC)

Written and pushed before the crop is fetched, any pass is run or any score is computed. Method exactly MONL-L21's
(passes/PREREG-MONL-L21.md), including its stated deviation (each pass ONE call carrying all five lines' crops; pass B reversed with
MONL-L16's extra sentence). Readers: two blind subagent passes on the strongest model (CLAUDE.md Usage 1 measured exception), shown only
the ids-only key sheet and the crops; reconciliation by this worker's eye on the native crops before the clear text facing L26-L30 is opened.

**Crops.** regen_monll26.sh: one openapi.bnf.fr region on f268, 600,4180,3100,800, tools/iiif_lines.py with MONL-L21's options. Line identity
from the debug overlay: the top band must be L25 (its opening signs as passes/c268e_reconciled.tsv L25); if not identifiable, stop and log.

**Scoring (registered, MONL-L21's unchanged).** Pass agreement per line and total (agreement, not accuracy). Reconciled conf H where both
passes agree, M otherwise. align_c268.py as committed (200 shuffled-clear draws, seed 140; f.139 c270 control) on L26-L30 alone (`--lines`)
and on L01-L30. The band is placed as running on from L25 only if L26-L30 alone beats its own shuffled-clear p95 AND 0/200 draws reach the
real share; otherwise "band not placed", L26-L30 stays U/M, nothing in L01-L25 changes. The L01-L30 run is kept only if 0/200 at or above.
No key edit, no relabel of L01-L25 tokens. Re-runs named by NOTES (k14try/run_k14try.py for K34/K62, K14 split, K40=z --try) only if this
band adds tokens to them and cap remains; otherwise logged as next step.
