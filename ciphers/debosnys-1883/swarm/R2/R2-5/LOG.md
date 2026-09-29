# R2-5 log (29 Sept 2026, UTC from `date -u`; the container clock)

| time | step | control result | real-text result | why it stopped / what it shows |
|---|---|---|---|---|
| 08:14 | read brief, DIGEST-1 R2-5, shared rules, Bennett (PDF text layer), dcore.py, R2-1, base_mark_recount.py, B's fitter | -- | -- | -- |
| 08:18 | B's fitter rebuild: 10 of 17 Gutenberg books fetched (byte sizes match MANIFEST), 7 reset (SSL/connection reset three times); stopped fetching | -- | -- | model5_en.bin from 14 of 21 files; stated in PREREG |
| 08:23 | PREREG.md + r25.py + folger_fig3.txt committed (5cf97fca) before any real score | -- | -- | -- |
| 08:23 | calibration (5 texts x 3 noise x 7 designs x 40 pairs), controls, real scores started | -- | -- | -- |
| 08:25 | first calibration rows: NULL-SPLIT median 34.6 above every language design (15.6-26.5) | -- | not read | the split writes its own pairs; D2 added as a registered diagnostic (addendum dc1e269a) |
| 08:36 | main test, controls read first | folger pass (0.843; 40/40); planted **fail** (0.555; 25/40) | real-T 36.8, real-N 41.7 vs NULL-SPLIT p95 44.2/44.9; gates 0.50-0.52 | kill test met on the control clause; untestable at the real composite share |
| 08:47 | D2 (box-level null) | folger 40/40 pass; planted 26/40 **fail** (power ~65 pct) | real-T 3.51 (3 of 40 null as high); real-N **9.55** (0 of 40; 0 of 80 all nulls, nearest 8.9); unsplit 1.70 | one weak lead (post-calibration diagnostic, 2 orders); larger than planted French (5.0) |
| 08:50 | d2_drivers.py: pair excesses | -- | few-count pairs + WAVE-PCT (H48, box-level) | no clear single driver; drawing habit not excluded |
| 08:54 | B's fit gap | folger 0.224/0.257 pass | real-T 0.059, real-N 0.077 vs NULL-SPLIT 0.086/0.039 | at shuffle level in English |
| 08:55 | stop: brief met; RESULT.md written | -- | -- | no key, nothing read |
