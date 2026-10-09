# PREREG HEIN-SR (9 Oct 2026, written before any new Deel 2 page is fetched)

Job: run `small_runs.py` unchanged (the rule, filters and amendment of PREREG-D2-HEIN.md stand; no new gate) over Deel 2 printed pages
7-600 that `deel2_ocr/` does not hold (the 75 pages A2P4-HAER / D2-HEIN already read are skipped), ascending order, one fetch per page,
>= 2.2 s apart, at most 118 fetches (budget 120 incl. 2 spare); stop at the budget and record the last page.
Positive control (disk, before any target page): p.130 (letter 341) and p.398 (letter 1017) must each fire at least once.
Negative controls (disk): pp.17, 60, 473 and 397 must fire 0 times. If either fails, the target result is reported as a non-test.
The control is a pair of known-cipher pages and known-clear pages for the same statistic (small-number runs) so it can differ from the target.
Hits are reported with page, letter number, sender, date and snippet; eye-read from OCR text only; no reading, no key change.
