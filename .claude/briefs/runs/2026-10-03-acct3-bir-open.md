# BIR-OPEN (account-3 worker, 3 Oct 2026 12:5x UTC)

Targets: birago-fr3252-1571-72 (f.117r) first, then nevers-birago-fr3251-1572 (f.168). Opus 5.5. Cap USD 6, box 45 min.
Vision calls <= 3 x USD 1.5 + 1 reconciliation unit. Crops: the existing line crops under
ciphers/nevers-birago-fr3251-1572/harvest/tx_decode/eye/verify (or tools/iiif_lines.py, command pasted before the first call).
Claim in ROOM.md first; done line at the end.

Why: BIR-ROUND2 found the two-option lattice instrument exhausted at lam 4 (0 new questions). Its named next instrument is an
open-choice blind re-read of the M positions against the full printed-key sign sheet (not two options), then one lattice pass.
1. Pre-register (commit + push first): the M positions per leaf (f.117r 74, f.168 22), equal ambiguity-matched H decoys; the reader
   sees a masked crop with the target sign boxed and the FULL sign sheet (all key signs + "other"), never the current transcription;
   gate = agreement with the current transcription on H decoys >= 80% (reader calibration), and on M positions report the
   change rate. Then re-run tools/key_decode_lattice.py lam 4 on the base with re-read M values as new candidates; posnull (200) must
   still PASS; judge (fr for f.117r, it for f.168).
2. Changes the reader makes on M positions that the lattice also prefers are applied at S only if decoy calibration passed; others
   stay M. decode_key.py --check; judge lines pasted in NOTES.md.
3. NOTES section in both folders; gaps_check; file_shrink_guard; commit by explicit path; push.
Grades per leaf. Report what was found and where it was not found; do not classify novelty.
