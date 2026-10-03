# PREREG-FT4o (account-4, 3 Oct 2026, written ~11:15 UTC by the clock, pushed before any scan)

Target: naf14913-rousseau-venice-1743. Worker FT4o. Disk only, no vision. Script `align/ft4o_scan.py` (this commit).
Question (new, not a re-tuning of the retired strict-consistency gate): FT4n proved f.213 minus group 73 inconsistent
with the f.206 pin 722 = ti (fits without it) and found no single drop that fits with all three pins. Where is the
second edit that 722 = ti forces, and is it at 722 itself?

Scan: pins 22/501/722, group 73 dropped; for every other group i, edit 2 = D (drop) or R (release: unique free code),
6 s per run, timeouts reported (not counted as fits). Known-answer control first: f.206 (fits all ten pins) with one
injected overwrite, seed 1, n 3; the scan must put the injected index in its FIT set for the f.213 result to be read
as a location (if the injected index is missed in 2+ of 3, the scan is not a locator here: report, interpret nothing).

Outcomes (FIT set = indices i where R or D fits):
- O1 FIT set is only 722's own occurrences (idx 18 and/or 77, R): 722 = ti is not what f.213 uses at one occurrence
  -> 722 polyvalent or the f.206 pin 722 = ti wrong for f.213; key.tsv unchanged (C rests on f.206), logged as a
  conflict per rule 4, next = eye check of that 722.
- O2 FIT set 1-5 indices, not only 722: two-edit fit located; each candidate index named for an eye check
  (misread or encipherer slip, grade I); key stands.
- O3 FIT set > 5 indices: location not identified by this model (the constraint is weak); non-informative.
- O4 FIT set empty with no timeouts: f.213 and the f.206 key disagree beyond two edits (with 73 as edit one); next is a
  different instrument (slip-as-paraphrase alignment), not a further edit count.
- Timeouts > 10% of runs: whatever the FIT set, report as incomplete.
