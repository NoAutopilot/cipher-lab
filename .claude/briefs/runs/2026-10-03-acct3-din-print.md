# DIN-PRINT (account-3 orchestrator, 3 Oct 2026): rebuild the Dinteville key against the 1882 print of f.128

Target ciphers/fr3621-dinteville-1592. VERIFY-DIN (27ad8129, N3): Revue de Champagne et de Brie XII (1882) p.340 prints f.128
(1 July 1592) in full, and it corrects the f.128 gloss reading (Besançon/Vesoul, not "bestiaux"; "doivent partir"). OCR excerpt
in print/revue-champagne-t12-1882-pp340-341.txt. Model Opus 5.5, cap USD 4, box 40 min. Disk only (the f.128 transcription and
gloss are on disk): vision calls: 0 x USD 1.5 = 0.
1. Normalize print and gloss to one convention (CLAUDE.md rule 3, PX-BRODEC: expand abbreviations, one case, one spelling set).
2. Align the f.128 cipher to the PRINT with tools/interlinear_align.py (grade C from the print); key-blind control (shuffled
   print, rotated print) must fail. Report how many rows change vs key_syl.tsv.
3. Re-decode f.130r with the print-built key (no hill-climb repair); rerun the shuffle + frequency-banded controls; grade per
   token (C only where the print supports the value; no S without its own control). Fix the inflated grade columns in the
   solvers' outputs (key_repaired.tsv, repair/tokens.tsv, decode.json job 2) per VERIFY-DIN, or mark them superseded.
4. Settle the date (3 vs 4 July: BnF finding aid and print say 4) from the leaf crop on disk if present; else leave flagged.
NOTES.md, AUDIT.md propagation note (rule 10: a reading revised after AUDIT.md is carried into it and SO-DIN-F130), NEAR row,
gaps_check, file_shrink_guard. Done line "for the account-3 orchestrator" with a one-line English gist (interpretation).
