# FORM-REDRAFT (account 3, 5 Oct 2026). Model Opus. Cap $3, box 40 min. Model floor Opus 5.5.

Job: bring two web-form drafts up to the current outreach/README.md rules (1, 1a, 1b, 7, 8) so the owner can paste them.
Do NOT send anything, do NOT touch Gmail drafts. No owner name in the repo (rule 9): keep `[SIGN-OFF]` / `[OWNER NAME]`.

1. outreach/mailbox/na-heinsius-quote-form.json (Nationaal Archief, Dutch form):
   - extend the request to the full revised extent in ciphers/borssele-heinsius-1714/REQUEST.md (3 Oct 2026 addition:
     letters 936, 959, 970 in H.A. 1836 and Deel 16 letter 104; about 6-8 leaves), citing Veenendaal pages as REQUEST.md does.
   - rule 1b: one short paragraph on our relevant work ONLY if the folder supports one (e.g. the Veenendaal read and the
     PHYSICAL/scans:[] check); rule-10 wording; nothing padded.
   - rule 7: Dutch text, then a separator line, then the full English version, all in the message field. Check the form's
     message field length limit on the live page (one fetch, good-citizen rule) and record it; if both versions don't fit,
     say so in notes and keep Dutch + a short English summary.
2. outreach/mailbox/agr-mercy-quote-form.json (AGR Brussels, form):
   - French first, separator, then English (rule 7).
   - rule 1b paragraph from ciphers/espagnol142-mercy-1648/AUDIT.md's safe sentence (Espagnol 144 f.22 read in part by our
     own cryptanalysis, numbers as AUDIT.md states them, "cryptanalytic result, not confirmed by a key or a clear copy"),
     and why the 15 April 1648 instruction (SEE t. LXIV f.16) matters to it, as NOTES.md supports. Folder link.
   - keep everything else in the checked text.
3. Both: disclosure sentence stays (first contact; Gmail searched 5 Oct 2026, no prior thread with either). Voice per 1a.
   Set "checked" to "PENDING re-check (FORM-REDRAFT 5 Oct 2026)" and keep the old text in a body_prev field.
   Set SEND-QUEUE.tsv S3/S4 status to `redraft` with a note; run tools/send_queue_check.py and paste output.
4. Commit by explicit path, push (pull --rebase retry), ROOM line via tools/room.py, report 5 lines. A separate session does gate 7.
