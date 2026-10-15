# PREREG ELEC-2R (15 Oct 2026, written 18:1x UTC by date -u, before any fetch or read)

Brief: ELEC-27 Next (1)-(3). Account 4, LANE DEFAULT-account-4-20261015-1735.

## (1) Blind second reader on the l.29 / l.21 signs
Material: openapi.bnf.fr btv1b90096539 f142 `full/2400,` (f.116r) and f106 `full/2000,` (f.84r), as ELEC-27 fetched (2 requests, >= 3 s apart,
scratch only). Crops (ELEC-27's coordinates, padded so a few neighbouring letters show; f.84r scaled to the f.116r line height):
 S1 f.116r l.29 (ELEC-PAIR "4"; ELEC-27 says Lbar shape)       S2 f.84r l.21/22 (ELEC-356 "Lbar"; pairs.tsv row line 22)
 S3 f.116r l.11 (ELEC-PAIR "4", reference)                      S4 f.116r l.32 (ELEC-PAIR "flag", reference)
 S5 f.84r l.27 (ELEC-27 "flag" under PREREG-ELEC-27, one reader)
Crops get random letter names (order shuffled, seed written in the scratch log); the reader is a fresh subagent that is told only "each crop is
centred on one non-letter sign in a 16th-century French cipher letter" and is not told any label, any printed name, any prior reader's grouping,
or which crops come from which leaf. Task: describe each centred sign's strokes, then partition the five into same-shape groups, with a
confidence per group (high / medium / low).
First reader (ELEC-27) partition: {S1,S2} {S4,S5} {S3}.
Decision rule (fixed now):
 - Relabel elecpair/pairs.tsv f.116r l.29 from "4" to "Lbar" only if the second reader puts S1 with S2 AND not with S3.
 - Relabel elec356/pairs.tsv f.84r l.27 from "4|flag" to "flag" only if the second reader puts S5 with S4 AND not with S3.
 - Any other outcome for a slot: label unchanged, slot logged "readers disagree". A low-confidence grouping counts as agreement only if it is
   the same partition; it is reported as low.
 - Non-test check: if the second reader puts S3 and S4 together (the two references), the references do not discriminate for this reader and
   neither slot is relabelled.
Then re-run elecpair/pair_control.py and elec356/pair_control.py (seed 357, 1000 permutations, ELEC-PAIR rule 4 unchanged) and report flag, 4
and Lbar. Rule 3 check: the control permutes the printed names over the both-sided slots and counts, per sign, permutations in which the sign
still reads one name; relabelling moves slots between signs, so the per-sign counts (pairs, real_consistent, shuffle share) can and do change
with the labels -- the control can differ from the target for this statistic (not orthogonal). A sign reads >= 2 pairs, all one name, and
shuffle < 5% before anything above M; no key.tsv change in this job in any outcome. A sign that pairs two names (Lbar = Trèves | Palatin if
relabelled) is a rule-4 data conflict, recorded with witnesses, never resolved by frequency.

## (2) Kluckhohn print check
archive.org `bub_gb_0gFoAAAAMAAJ` djvu.txt (1 request): read p.814 l.14 (nr. 357, the slot ELEC-PAIR paired as Palatin) and p.813 l.10 (nr. 356,
Trèves). Report the printed words verbatim (OCR, rule 2: conditional on the OCR; a page image only if the OCR is garbled at that line, and
only within the request budget). Outcome is a fact about the print, not a resolution of the conflict.

## (3) Item 37 (only if under 60% of the USD 4 cap after (1)-(2))
fr.3897 item 37, between f.74r and f.81v: locate via canvas labels (gallica_folio-style, <= 2 openapi.bnf.fr requests) and say whether
name signs (set A shapes) appear, M, no pairing.
