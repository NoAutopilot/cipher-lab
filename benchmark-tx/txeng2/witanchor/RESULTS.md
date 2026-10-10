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
