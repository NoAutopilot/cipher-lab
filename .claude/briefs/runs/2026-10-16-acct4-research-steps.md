# Research steps, account 4 (16 Oct 2026, 13:4x UTC by date -u; owner's directive: research, not occupation)

Common tail: .claude/briefs/README.md applies (ROOM claim/done with the usage phrase, wall-clock box, no AskUserQuestion, never a
dollar figure for yourself, `tools/prior_work.py` before the first priced step, PREREG with a `## Decision` block before any scored
run, `tools/experiment_log.py --check` on it). Stop at the brief's end; a follow-up is one line in NOTES.md. Each job stops the
moment its stop criterion fires: an empty result is the result, not a reason to widen the search.

## JOB CLIN-UNREAD (account 4; Opus 5.5; cap USD 3; box 40 minutes; disk only, no network, no readers, no images; Price: vision calls: 0 x USD 0 = 0)

Target: ciphers/pro3055-clinton-1779 (partial). The 1778 title-page key reads B.147 cipher copies with the B2 decode-run gate
PASSing against a page-permuted-key control (CLIN-3004C, CLIN-3502, CLIN-3502B, 15 Oct 2026, NOTES.md ~1991-2126) -- every page so
far had a known answer (a period decipherment later in the same volume, or print). Question: is there any cipher page on disk for
which NO period decipherment and NO printed text is recorded, so that the key would produce a reading nobody has?
1. Read NOTES.md's item table (~lines 300-360), the "Read so far" line (~928), the CLIN-* sections (~1991-2126) and
   images/h1649/manifest.json + images_manifest_full.tsv. Build a table: page (B.147/B.148 p., H-1649 Image), item, cipher
   on disk (y/n), period decipherment located (page/Image, or none), printed text (edition + page, or none), key tested (gate result).
   Scripts read, you judge: grep the NOTES, do not re-read the volume.
2. If every cipher page on disk has a period decipherment or a print: write the table into NOTES.md as section "## CLIN-UNREAD
   (16 Oct 2026)" with the sentence "no unread cipher page on disk; the 1778 key can add depth on known text only", update the
   Verdict line (keep `partial`), and STOP. Do not fetch any new image.
3. If one page has neither: name it, and run the existing scorer pattern (copy passes/check_p300.py to check_p<N>.py with the
   page's reconciled cells if they exist on disk; if the page has no reconciled cells on disk, STOP at step 2's write-up naming it as
   the next row with the per-pass price from CLIN-3502B's ledger row -- do not transcribe in this job). A PREREG before any score.
   Report the gate numbers, grade decoded letters S only inside gate-passing runs, no AUDIT.md edit, no novelty word (rule 10).
Report: the table's row count, the answer to the question in one sentence, what was found and where it was not found.

## JOB HEID-NA-SCREEN (account 4; Opus 5.5; cap USD 4; box 60 minutes; service.archief.nl <= 140 requests, one at a time, >= 3 s apart, take/release lines as HEID-1621B; your own eye on 700 px contact sheets only, no reader subagents; Price: vision calls: 0 x USD 0 = 0)

Target: ciphers/brederode-heidelberg-1621 (open) via ciphers/oldenbarnevelt-brederode-1605 (screen tooling). The 1621 and 1623
Brederode numeral blocks came from NA 1.01.02 inv. 6021/6022 screens (OBRED-6021, HEID-1621B, HEID-1621J); more ciphertext in the
same system is the only thing that moves this target before the key arrives (ASKS 170), and the alignment tool is retired below
N=200 for it (HEID-1623CAL). Two units, in this order, each a stop point:
U1. inv. 6022 scans 186-595 on composite/contact sheets (the method and commands of HEID-1621B / OBRED-6021:
    screen_tools/na_fetch.py + contact_sheets.py, 700 px tiles, planted controls as before -- state the control count), looking for
    numeral-code blocks and any key table or decipherment. Log every hit with scan number, a one-line description and M grade.
U2. Only if U1 ends under 80 percent of the box and cap: inv. 6016 orders 1-259 at stride 3 (the OBRED next row, ~87 requests).
No transcription, no reading. Write "## HEID-NA-SCREEN (16 Oct 2026)" in brederode-heidelberg-1621/NOTES.md (hits, controls,
request count per host, scans seen / total) and one line in oldenbarnevelt-brederode-1605/NOTES.md pointing to it; update the
Remaining gaps "siblings" line. A screen with no hit is a result: write it as "no numeral block on the scans seen (stride, controls)".
Report: hits (scan numbers), controls, requests, what was not covered.
