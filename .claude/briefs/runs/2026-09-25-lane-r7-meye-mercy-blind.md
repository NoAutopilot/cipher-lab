LANE R7 MEYE -- espagnol142-mercy-1648: blind re-transcription of six rows (Sonnet, cap $2.50, box 35 minutes; disk only, no hosts, no subagents).
Common: 2026-09-25-lane-r7-common.md. AUDIT.md section 3 (d): "a blind re-transcription of the five 14/19 glyphs and of r16-r17, v04, v07".
Intake gate (live, 25 Sept 20:00 UTC): "espagnol142-mercy-1648: partial (line 1) -- edition/page or full-text-search citation found within 6 lines" (exit 0).
BLIND RULE (the point of the job): before you commit blind_pass.tsv you must NOT open, cat, grep or diff any of these in ciphers/espagnol142-mercy-1648/:
ciphertext.tsv, ciphertext_draft.tsv, passA.tsv, passB.tsv, agreement.tsv, disagreements.tsv, cipher_codes*.tsv, key.tsv, exceptions.tsv, corrections.tsv,
reading*, candidate_reading*, m2/, rederive/, NOTES.md, AUDIT.md, second-opinions/, and not the existing line crops (images/f22*_L*_s*.jpg), nor ROOM
lines about Mercy. Read only images/f22r_canvas58.jpg, images/f22v_canvas59.jpg and images/manifest.json's "entries" block.
The letter: numerals (two-digit and one-digit codes, some followed by a dot or a mark) mixed with plain Spanish words. Rows are counted per side from the
top: r01 is the first written line of the recto (canvas 58), v01 the first of the verso (canvas 59).
Job:
(1) Cut your own crops of recto lines 6, 14, 16, 17 and verso lines 4, 7 (PIL, at native resolution, under 2500 px wide, two halves per line) into
    ciphers/espagnol142-mercy-1648/meye/ (not images/). Count the lines on the image carefully; record each crop's pixel box.
(2) Transcribe each of the six lines token by token in reading order: every numeral as written (keep a following dot as '.'), every plain word as
    [PLAIN:word], confidence H/M/L per token, and for any L or M numeral the alternative you considered. Pay particular attention to how this hand
    writes 4 and 9: build a small reference sheet of unambiguous 4s and 9s from elsewhere on the page (meye/ref_4_9.png) and compare each
    doubtful digit to it.
(3) Commit and push meye/blind_pass.tsv (columns line, position, sign, confidence, alt, crop) and the crops BEFORE any comparison. Push.
(4) Only then: a script meye/compare.py diffs your pass against ciphertext.tsv and exceptions.tsv (by line and position; align by the plain-word
    anchors if counts differ) and writes meye/compare.tsv; report agreement with ciphertext.tsv (the two earlier blind passes' settled form) and with
    exceptions.tsv's five M-graded 14 readings (r06 14, r14 7, r16 3, r16 6, r17 5), each as agree / disagree / unreadable.
Write a short meye/README.md with the numbers. Do not edit any other file in the folder.
ROOM done: "done: for LANE R7: mercy blind eye-check -- 6 rows <n> tokens, agreement with ciphertext.tsv <x>%, the five exceptions: <k> read 14, <j> read 19, <u> unreadable".
