# PREREG -- R7C-BAL103K sibling calibration of Tomokiyo's 1644 table (written and pushed before the answer is read)

Worker R7C-BAL103K (account 1, LANE LANE-RUN7-account-1), 6 Oct 2026, written 02:3x UTC by `date -u`.

Material: Gallica btv1b9001389d canvas 366 = f.171r (cipher, headed "Du premier septembre 1644 a Paris", foliated 171 by eye on a
600 px view) and canvas 368 = f.172r (period decipherment, headed "Du 1er de Sepbre 1644 a Paris", foliated 172). DECODE R2743 lists
this letter as f.171-173. Disclosure: both canvases were viewed once at 600 px to identify them; the decipherment's first two lines
were legible at that size ("On a advis icy, que ceux qui apres la prise de Lerida ..."). The blind transcription below is done by a
Sonnet subagent that is given the f.171r line crops and the key sheet only, never the decipherment and never told the letter's content.

Units: the first 4 cipher lines of f.171r (line crops by tools/iiif_lines.py), one blind Sonnet pass (brief: one pass; the
reconciliation only if the cap allows).

Decode: each transcribed sign through key_decode.tsv (first value of an a|b cell; U and numeral codes > 23 dropped from the letter
string, kept in the token table).

Statistic A: normalise both strings (lowercase, letters only, j->i, v->u, accents stripped); global edit-distance alignment
(difflib-free exact DP, unit costs) of the decoded letter string D against the decipherment span P covering the same lines (P = the
decipherment from its start up to the point where the alignment's end is best, i.e. a semi-global alignment, free end gaps in P);
A = matched letter positions / len(D).

Control (can vary on the same axis -- key correctness): 200 random permutations of the letter values across the key's cells
(the sign -> letter map shuffled, same transcription, same alignment procedure); report mean, p95, p99. A second, descriptive control:
D aligned against an equal-length span from later in the decipherment (wrong-span null), not gated.

Gate (table calibrated): A >= 0.60 AND A > permutation p99.
- PASS: the table, as this folder names its signs, reads the sibling. Key changes licensed only for a sign seen >= 2 times in the
  sample whose aligned decipherment letter is the same on every occurrence (or >= 3/4 with n >= 4) and differs from key.tsv; each
  change recorded in key.tsv with source "R7C-BAL103K f.171r calibration", then f.50 re-decoded (decode_key --check) and the fr17
  judge re-run.
- A > p99 but < 0.60: partial calibration; no key change; per-sign mismatch table logged for the next job.
- A <= p99: gate FAIL; logged; no key change; stop.
The ambiguous 9 (i|r|s) and 3 (h|x): each occurrence's aligned decipherment letter is tabulated (descriptive, no gate on its own).
