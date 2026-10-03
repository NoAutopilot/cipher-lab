# PREREG VILL-KEYS (3 Oct 2026, committed before any fr.3995 no.39/40/43/58 image is viewed)

Target inventory: bourdeau/ct_f148r.txt + ct_f148v_149r.txt, 753 sign tokens: 445 figures (1-9, o) and 308 other
signs, of which the brief's family is L (lambda) 16, P (pi) 12, Q (theta) 14, D (Delta) 5, V (varpi) 11, W (infinity) 13.

Rule 1 (eligibility, from the heading/upper-table crops only). A table is "family-bearing" iff the crops show
(a) figure codes (one- or two-figure numbers used as cipher values) AND (b) at least 3 of the 6 family signs
lambda, pi, theta, Delta, varpi, infinity used as cipher values.
Rule 2 (coverage). coverage = share of the 753 target tokens whose sign type occurs among the table's cipher values
as seen in the crops (figures count as covered when (a) holds; each non-figure target sign counts only when an
identical-looking sign is seen in the table). Coverage < 0.5 => "not testable", not a negative.
Rule 3 (score, only if coverage >= 0.5). Transcribe the table to keys/*.tsv, decode the target with it, score with
tools/judge_plaintext.py (fr16), and rank the real key against 200 value-shuffled keys (same code set, plaintext
values permuted); report rank and z side by side. Real key pass = rank 1/201 and z >= 3.
If no table is family-bearing, the step is closed "not testable" for these four tables and no score is run.
