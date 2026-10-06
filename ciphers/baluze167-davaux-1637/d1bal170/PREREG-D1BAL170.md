# PREREG D1-BAL170 (account 1 worker, for LANE DEFAULT-account-1-20261006-1240), written 6 Oct 2026 before any pass was run

Target: Baluze 170 f.228r-v (ark btv1b90015040, canvases 239 right page and 240 left page), the bare cipher of Chavigny to d'Avaux,
Amiens 25 Aug 1640 (Tomokiyo "undeciphered"; DECODE R2761 key only). ff.229r-229v (c240 right, c241 left) are not passed in this job
unless the cap allows after f.228 (brief: f.228 first).

Crops (tools/iiif_lines.py, native regions on disk in images/crops/src_ark_12148_btv1b90015040_*):
 f.228r: b170f228r_a_L02, b170f228r_c_L01, b170f228r_b_L01, b170f228r_b_L02 (s1/s2 each)
 f.228v: b170f228v_a_L01, b170f228v_a_L02, b170f228v_b_L01..L07 (s1/s2 each)

Passes: two blind Sonnet subagent calls per page (A, B), same prompt (d1bal170/prompt.txt), crops + d1bal167/exemplar_sheet.png only.
Letter signs are written as shape classes from the exemplar sheet's labels (s:<shape>), not as letters; the shape -> letter step is
done afterwards by this worker from d1bal167/exemplars.tsv.

Split statistic (fixed now): token disagreement = 1 - (agreed aligned tokens / aligned columns), from
`python3 tools/reconcile_passes.py passA passB --keep-plain` per page, cipher tokens only (clear words in braces excluded as the tool
does by default), marks included (72' vs 72 is a disagreement). Both passes are the same model on the same crops, so this is
agreement, not accuracy (TRANSCRIPTION.md); it is reported as such.
Gate (brief): split > 0.10 on a page -> reconcile that page by eye (1 unit), stop; next step is a sign sorter, no decode claimed.
Split <= 0.10 -> reconcile, then a provisional decode with key.tsv; every letter sign whose shape carries more than one letter in
exemplars.tsv (u4, loop, 4u) or is a singleton or unmatched is graded M; nothing is graded above S without a control, and no reading
is claimed beyond "numerals decoded with the published key" (grade H for the numeral code values themselves only).
No known-answer control is run in this job (it is a transcription job; the labeller control remains as PREREG-D2DAVEX states it).
