# TX-SHEET result (4 Oct 2026, 14:3x UTC, account-3 worker) -- FAIL, not adopted

Pre-registered in benchmark-tx/PREREG-txsheet.md (commit 627f0347, pushed before the pass). One blind Sonnet line-read
pass (pass E) of the eval item birago1572-no87, with the per-hand exemplar sheet (atlas/sheet_truth/sheet_01..04.png)
replacing the canonical 51-cell sheet. Crops, brief and call grouping matched pass A; 3 calls, 843 signs read.

| gate | pass A | pass E (sheet) | met? |
|---|---|---|---|
| err_true, 803 scored | 0.069 (55) 0.053-0.088 | 0.077 (62) 0.061-0.098 | no |
| paired vs pass A | -- | fixed 16 / broken 22, sign test p = 0.42 | no |
| d<-T98 | x7 | x2 | yes |
| s<-T50 | x7 | x15 | no |

`python3 tools/tx_bench.py benchmark-tx/outputs/birago1572-no87/passE_sheet.tsv --bench BENCHMARK-TX.tsv --item birago1572-no87`:
err_true 0.077 (62/803) | wrong 51 deleted 9 inserted 2; top confusions s<-T50 x15, e<-T89 x4, m<-T66 x3, e<-T60 x2, n<-T86 x2.

What it says. The hand tiles fixed the T18/T98 split it was aimed at (d<-T98 7 -> 2), but doubled s<-T50. no.87's s-errors
are the curled "Ce" (an off-sheet sign, X_CE, NO87-LABELS). The sheet's T50 row is six tiles of the hand's own T50, which
looks like the Ce more than the printed shape does, so the reader filed every Ce under T50. A secure tile can still
teach a confusion when the eval hand carries a look-alike sign the sheet has no row for. New errors also appeared on
print-only rows (m<-T66 x3) and on the T60/T86 pair, which all three readers named their hardest split. Net: the
sheet trades one confusion for another and does not lower err_true on this item.

Limits: one pass, one seed. The sheet settings were a-priori, untuned (the PREREG says why dint-f128-print could not
be used). The exemplars are S-grade (two blind readers plus the atlas agree), never C/H. The atlas's cluster names
carry some no.87 tune-line information (disclosed in the PREREG).
Possible next step, not run: give X_CE its own row with secure tiles, then re-test. That is a sheet-design change, so
by rule 3's third-attempt clause it is a new instrument only if it changes more than one knob.

Cost: session total USD 6.31 at write-up (worker plus the 3 Sonnet read calls; the per-call split is not visible). That
is about USD 0.74 per 100 signs at job level (853 signs), an upper bound for the read pass alone.
