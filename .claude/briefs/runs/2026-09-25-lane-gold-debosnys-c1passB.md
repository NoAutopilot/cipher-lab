JOB GOLD-4E: Debosnys cryptogram 1 only: blind pass B on the split inventory and reconcile. Sonnet (claude-sonnet-5). Stop and push at $3 or 25 minutes, whichever first. NO subagents. Lane: LANE GOLD orchestrator session_01DKDynpdEwZK5EokxtjCM3P. Written 25 Sept 2026 19:04 UTC.

Why this is small: GOLD-4D tried all four cryptograms (about 1300 signs against a 160-sign atlas) through one subagent and was stopped at 3.3x its cap with nothing pushed. This job is cryptogram 1 (6 lines, about 132 signs), done by you directly, one line at a time, committed after each two lines.
Read first: `.claude/briefs/runs/2026-09-24-lane-r4-common.md`, `.claude/briefs/runs/2026-09-25-lanes-7b-COMMON.md` (binding), the GOLD-4C section of `ciphers/debosnys-1883/NOTES.md`, `glyphs/inventory.tsv` (look at `glyphs/inventory.png` once). Claim in ROOM.
Intake gate (live, 19:04 UTC): debosnys-1883: open (line 1) -- edition/page or full-text-search citation found within 6 lines  (exit 0)
Do:
1. Blind: never open passA.tsv, box_labels.tsv, ciphertext_draft.tsv or ciphertext.txt before step 2. From the c1 line strips/crops, transcribe each sign as an inventory id into `passB_c1.tsv` (line, position, sign id, base id for composites, confidence). Commit and push after lines 2, 4 and 6.
2. Reconcile against GOLD-4C's pass A for c1 with `tools/reconcile_passes.py` (one id convention first). Report agreement at full id and at base level. Settle every disagreement on the image; classify each as inventory confusion / segmentation / reading error.
3. If full-id agreement after settling is at least 80 percent, write cryptogram 1 into `ciphertext.txt` (replace B2's c1 draft section; header line with passes, agreement, date from date -u). Otherwise leave it and write `ciphertext_c1_draft.tsv`.
4. Short "GOLD-4E, cryptogram 1 pass B" section in NOTES.md.
Read your own cost (get_session is not available to you; use elapsed time: stop at 25 minutes). Done line: agreement full/base, disagreement classes, written to ciphertext.txt yes/no, no cost figure. No decoding. Rule 10 wording.
