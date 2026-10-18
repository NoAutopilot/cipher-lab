# Research director, wave 22 (18 Oct 2026, 14:1x UTC by date -u): Haldimand pool rank 1, B.149 p.286

Common tail: .claude/briefs/README.md applies (ROOM claim/done with the usage phrase, wall-clock box, no AskUserQuestion, never a dollar
figure for yourself, `tools/experiment_log.py --check`). The job ends with the six research-director questions in one line each.
Report what was found and where it was not found; no novelty class (rule 10).

## JOB HALD149 (account 4; Opus 5.5; cap USD 6; box 60 minutes; hosts: heritage.canadiana.ca + image-uab.canadiana.ca (at most 30 requests, 1.5 s apart), archive.org (Brymner 1888 text; Entick 11280377bsb page images only for the cells this page uses), github.com (two shallow clones), de-crypt.org listing cache, web search; Price: vision calls: 5 x USD 0.5 + 1 reconciliation = 3.0)

QUEUE.md "## Haldimand-service cypher pool (18 Oct 2026)" rank 1: Haldimand Papers B.149 p.286 (BL Add MS 21809), Brymner 1888: "Page 286
in cypher from Carleton", 1783-84, Carleton-Haldimand. Keys on disk: the 1778 title-page book key (ciphers/pro3055-clinton-1779/passes/
title1778_reading.txt, tomokiyo_key_pairs.tsv) and the Entick 1781 page/column-line code (ciphers/sherwood-cossit-1781/decode_entick.py,
book/entries_image.tsv; Leighton and Matyas snippets also name a page.column.line+1 Entick form).
1. Check-solved first, short (.claude/briefs/check-solved.md): create ciphers/hald149-carleton-1783/NOTES.md (status word on line 1; line 2
   the Brymner page read, quoted); premise check against pro3055-clinton-1779's files and AUDIT.md (is B.149 already in its scope or
   print checks?), Tomokiyo's haldimand.htm, Bourdeau, Aymeloglu, DECODE cache, a web search for the letter. Paste
   `tools/intake_gate_check.py hald149-carleton-1783`; a nonzero exit stops the job before any decoding.
2. Locate the reel and frame (the series oocihm.lac_mikan_105513; H-1649 ends in B.148 near p.180, so try H-1650 and the reel list),
   fetch p.286 (and the facing page and any decipherment or covering letter beside it), line crops by `tools/iiif_lines.py --image FILE
   --out DIR` (paste the commands), never a full frame to a vision call.
3. Describe the form. Transcribe the cipher (two blind passes if more than 30 groups; tools/reconcile_passes.py). Then apply, by script,
   whichever key the form fits: figure pairs under 30/30 -> the 1778 title page; page-line pairs up to 472 -> Entick (both the plain and
   the +1 displacement forms). Matched control for any key tried: the same script with shuffled keys/offsets (20 seeds), reporting English
   cover or bigram score for both. Grade per token. If neither key fits, say what the form suggests and stop.
4. NOTES.md sections for the check, the pages and the test; the "## Remaining gaps"/"## Escalation" pair if the result is partial
   (tools/gaps_check.py passes).
Report: check-solved verdict, reel/frame, cipher form, key result vs control, five lines.
