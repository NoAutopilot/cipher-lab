# WIT-ANCHOR and WIT-GROEN: printed witnesses as read-free anchor checks of dec_norm (lane incarnation 4, 10 Oct 2026)

Run by LANE TX-ENGINEER-2 incarnation 4 (session_01GukpgU1yBAfju3zg6g8ayG) in its own session under PREREG-txeng2-19's dated
addenda (WIT-ANCHOR 01:07, WIT-GROEN 01:2x; both pushed before the runs). Reads: the on-disk IA OCR of the two editions and the
folder's clerk reading ciphers/fr16104-vivonne-spain-1572/tx/dec_norm.txt (9,554 letters after the fold). Reads no truth file, no
output file. Openings of eval truth: 0. Scripts: wit_anchor.py (result.json), wit_groen.py (result_groen.json).

## WIT-ANCHOR: Gachard II (1875) p.428 vs dec_norm (run 01:08-01:21 UTC)
The passage "Quant a la paix que l'on dit ... appaisees par la force" (OCR, p.428) normalised to 498 letters (Gachard's
"...." omission after "Anglois" did not split on the OCR's spacing, so the passage aligned as one segment; the omission costs ratio,
never position). Best window: dec_norm **2697-3195**, SequenceMatcher ratio **0.6707**; selection-fair null (200
letter-shuffled copies, each at its own best window): max 0.3153, p95 0.2791; **margin vs max 0.3554**.
Gate (declared): within 100 letters of the string-search placement 2669 (yes: 28) and margin >= 0.03 (yes): **ANCHORED**.
Reading: Gachard's quotation, an independent transcription of the same clerk decipherment, lands where WIT-VIV's string search put
it; its first ~150 letters fall inside the re-anchored f.102r stretch (dec_norm 550-2850, DV1d) and the rest beyond the f.102r/f.102v
seam -- consistent with dev2's anchor and with the seam where DV1d placed it. The ratio 0.67 (difflib's 2M / (|a| + |b|)) is
bounded by OCR quality, Gachard's omission and period spelling, and is a transcription-agreement figure, not an error rate. Nothing
rebuilt, nothing re-scored.

## WIT-GROEN: Groen van Prinsterer IV pp.90*-91* vs dec_norm's end (running; appended when done)
Run 01:21-01:3x UTC 10 Oct (wit_groen.py; result_groen.json). The passage "L'Empereur fait asseurément ... remédier ses affaires"
(letter 63, "St. Goard au Roi Charles IX: Madrid, 8 juin (MS. P. Sup. G. H. 228, vol. 79a)", printed from a manuscript copy other than
BnF fr.16105) split at the p.90*/p.91* page break into a clean part (370 letters) and an OCR-damaged part (189 letters).

| part | best window in dec_norm | ratio | selection-fair null max / p95 (n) | margin vs max | letters before dec_norm's end (9554) |
|---|---|---|---|---|---|
| p.90* clean | **8937-9307** | **0.7865** | 0.3297 / 0.3135 (200) | **0.4568** | 247 |
| p.91* damaged | 9270-9459 | 0.6508 | 0.381 / 0.3651 (50) | 0.2698 | 95 |

Gate as declared (the clean part's window ends within 150 letters of dec_norm's end AND margin >= 0.03): margin passes (0.457),
the end condition FAILS (247 letters) -> **NOT SUPPORTED by the declared gate**. Reading beside the gate, not
a verdict: the gate was written for the whole passage but tested on its clean HALF; the damaged half follows contiguously
(9270-9459, 37 letters of overlap at the join, margin 0.27 despite the OCR) and the whole passage ends 95
letters before dec_norm's end -- inside 150 -- with the 95 letters after it being the clerk's own close (date and subscription,
which Groen's extract omits). So the clerk-independent copy places the dispatch's closing passage at the end of dec_norm, where
N5-VIVK's end anchor put the f.103r stretch, and agrees with the clerk's text there at ratio 0.79 (bounded by OCR, period spelling
and the two copies' own variants). What this licenses: the END anchor of the f.103r stretch is consistent with an independent
witness (a post-hoc reading; the declared gate itself fails on its own wording, and that is recorded, not reworded). What it does
not: nothing about the 310 align-uncertain positions inside the stretch, nothing about the cipher reads, nothing rebuilt; a verifier
pass on the closing stretch's clerk-doubtful flags against Groen's text is a later PREREG (flags change only through the build's
flag column by a verifier).
