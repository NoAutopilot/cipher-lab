# PREREG C1161-EXC (15 Oct 2026, account-4 worker for LANE DEFAULT-A4-1441-15), pushed before any window is built or looked at

Question: for each of the 24 labels C1161-LKEY left `unmapped` (lkey/concordance.tsv: + 0 2 6 6r K Sorn blot d dia eloop f iii l ls o psi
rot s spiralG th tri vdash x), which exemplar on George Lasry's key sheet (sources/cyphersolver/2026-10-14-lasry/clair1161/lasry_p073_1.png,
CC BY 4.0, credit rule 8) shows the same sign, judged from image exemplars of OUR tokens, not from label descriptions.

Windows (`exc/exc_windows.py`, seed 1441): up to 3 tokens per label, drawn among tokens whose position lies within 4 of a hand-placed S
(shc/hand.tsv, L2 PASS) in the same line, nearest distance first; x = x_S + (pos - pos_S) * pitch on the S's own piece; window format of
shc/cut_hc.py (+-2 pitches, band +-90 px, red tick on the target). A label with no such token is UNTESTABLE (logged, not matched).
Controls (power): 4 labels whose LKEY passes both agreed with the sheet: qb -> a, 9 -> s, sd -> g, y -> r; one per group, hidden among the
test labels with the same ids format. Groups: 4, test labels assigned in a seeded shuffle.

Passes: two blind Sonnet calls per group (pass A, pass B), each sees ONLY the sheet and its group montage; ids and row order re-drawn per
pass (seeds 14411, 14412); no label names, no values, no key, no descriptions, no prior concordance. Answer per id: sheet column letter +
row (e.g. `s:3`), or `nom:<entry>` / `null:///` / `null:x`, or `none`; confidence high/med/low. Montages in the session scratchpad only.

Gates (exc/exc_score.py):
- POWER per pass per group: the control row answered with its agreed column. A group whose pass fails POWER is a non-test for that pass.
- MAPPED: a label is mapped when, in groups whose two passes both pass POWER, pass A and pass B name the same column letter (rows may differ)
  or the same nom/null entry, and neither says `none`. Column u/v counts as one.
- SPLIT: both answered (not none) but differ -> one reconciliation unit: a third blind Sonnet call (seed 14413) over the split labels only,
  same format; final = the column named by >= 2 of A/B/C, else UNDECIDED.
- NONE: either pass says none and the other does not agree on a column -> NO MATCH (a lead that the shape is outside his sheet).
Outcome use: a MAPPED/final label gets `his_value_blind` in exc/concordance_exc.tsv and agree/disagree vs our key value. No edit to key.tsv
or ciphertext.tsv in this job (no --try registered here); disagreements are data conflicts (rule 4) and leads for a later --try.
