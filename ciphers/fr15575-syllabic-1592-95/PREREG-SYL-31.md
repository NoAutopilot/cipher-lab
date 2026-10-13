# PREREG-SYL-31 (13 Oct 2026, written 08:2x UTC by date -u, before key_no31.tsv is reconciled and before any count)

Job SYL-31 (account-2 worker for LANE DEFAULT-A2-0710). Question: do fr.15576 f.2's 3-digit tokens fall on key no.31's codes
(BnF fr.3995 f.62r, canvas f126) more often than a matched null predicts? Count level only; no decode, no reading.

**Inputs (fixed now).**
- f.2 side: `f2_fr15576/ciphertext_body.tsv` (D4-15576 reconciled body C01-C21) exactly as committed at origin/main when this
  file is pushed. A token's value = its digits after stripping every non-digit (marks such as + ¨ ² ^), as nomen_range_check.py
  does; a "3-digit token" is one whose stripped value has exactly 3 digits. (SYL-NOM's census: 319 such tokens, 142 distinct.)
- Key side: the set C of codes in `key_no31.tsv` as built by this job's reconciliation (both grades H and M), restricted to
  codes whose stripped value has exactly 3 digits. Let k = |C|. (D4-SYL54's one look saw only the z row as 3-digit,
  za 704 ... zu 708, k = 5, a run of consecutive numbers; the count below uses whatever the reconciled file holds.)

**Statistics.** T = number of f.2 3-digit tokens whose value is in C (primary); D = number of distinct f.2 3-digit values in C
(secondary, reported, not gated).

**Matched null (no.31's own layout).** No.31 assigns codes to a row of five syllables as a run of consecutive numbers. Null
draw: a set of k codes laid out the way C is laid out on the sheet -- if C is one run of consecutive numbers (as expected), a
run of k consecutive numbers with a uniformly random start s in 100 .. 999-k+1; if C is several runs, the same number of runs
with the same lengths, each with an independent random start in the same range (overlapping draws redrawn). 10,000 draws,
seed 31. Secondary null (reported, not gated): k distinct values drawn uniformly from 100-999 with no layout.
The null can differ from the target on T: a different start moves the run onto different f.2 values (not a non-test).

**Gate.** p = (1 + #{null T >= observed T}) / (10,000 + 1). The overlap "clears the null" iff p <= 0.05. If it clears, the next
step named is a pre-registered decode test of f.2's 3-digit block against no.31 (priced in NOTES.md); if it does not clear, the
result is logged as "f.2's 3-digit overlap with no.31's codes is at chance (count level)", which is not evidence against a
no.31-family key with a nomenclator not on this sheet. No threshold, input or null is changed after the count is computed.

Script: `no31_overlap.py` (prints T, D, null mean/p95, p for both nulls; exit 0 always, a census with a gate line).
