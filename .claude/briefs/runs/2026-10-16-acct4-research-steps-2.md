# Research steps, account 4, second file (16 Oct 2026, 13:5x UTC by date -u; owner's directive: research, not occupation)

Common tail: .claude/briefs/README.md applies (ROOM claim/done with the usage phrase, wall-clock box, no AskUserQuestion, never a
dollar figure for yourself, `tools/prior_work.py` before the first priced step, PREREG with a `## Decision` block before any scored
run, `tools/experiment_log.py --check` on it). Stop at the brief's end; a follow-up is one line in NOTES.md. A stop criterion that
fires is the result.

## JOB CLIN-F49 (account 4; Opus 5.5 worker, Opus readers; cap USD 8; box 75 minutes; heritage.canadiana.ca <= 4 requests (one page image at native size, 1.5 s apart); Price: vision calls: 3 x USD 1.3 = 3.9 (2 blind column reads + 1 reconciliation, one page); scripts for the key and the control)

Target: ciphers/pro3055-clinton-1779. CLIN-UNREAD (NOTES.md "## CLIN-UNREAD (16 Oct 2026)") found no unread cipher page on disk and
named one off-disk lead with no period decipherment recorded: **B.148 f.49, H-1649 Image 1125** (IIIF id in images/h1649/seq_to_iiif.tsv),
Carleton to Haldimand, 22 July 1782; Tomokiyo (sources/cryptiana/web/haldimand.htm) prints about a dozen groups and says the
deciphered letter at pp.50-51 "does not seem to match". Question: does the 1778 title-page key read this page (B2 decode-run gate
against the page-permuted-key control, exactly as passes/check_p300.py), and is the result text nobody has?
1. `tools/prior_work.py pro3055-clinton-1779 --item-spec 'B.148 f.49 Image 1125' --step-type key --fetch`; paste. Fetch Image 1125 once
   at native size by the route in images/h1649/manifest.json and regen_images.sh (one request, 1.5 s apart if a retry is needed);
   write the manifest entry; keep the folder under 30 MB (a 1600 px copy committed, the full size in the scratchpad).
2. Cut the cipher columns with `tools/iiif_lines.py --image <file> --out ciphers/pro3055-clinton-1779/images/h1649/p49_cols` (paste the
   command; check the debug overlay). Two blind Opus reads of the column crops (one subagent per read, crops only, no key, no reading
   shown) + your reconciliation against the crops -> passes/p49_reconciled.tsv (the p300 format). That is the 3 priced calls.
3. PREREG-CLIN-F49.md first (belief, gate, control, what would change it, Decision block), then copy passes/check_p300.py to
   passes/check_p49.py (names, input, no known-answer section: there is none) and run it: B2 decode runs on the 1778 key as printed
   (variant a gated, b reported) vs the page-permuted-key control. Paste both numbers.
4. If the gate PASSes: decode the page with the key, grade decoded letters S only inside gate-passing runs (M elsewhere), write
   reading_p49.txt with the grade counts, and run `tools/print_check.py` phrases from the decoded runs (archive.org, Google Books with
   `country=US`) plus a read of the pp.50-51 decipherment (Images 1126-1127 are NOT to be fetched in this job: compare against
   Tomokiyo's extract and the Brymner B.148 calendar entry for 22 July 1782 only, both on disk or in the NOTES). Report what was found
   and where it was not found; no novelty word (rule 10); no AUDIT.md edit; "reading ready" ROOM line for a verifier if the gate passed.
   If the gate FAILs or is NON-TEST at its floor: write that with the numbers and STOP (f.93 is not this job).
Write "## CLIN-F49 (16 Oct 2026)" in NOTES.md with the table row for f.49 added to the CLIN-UNREAD table; update the Verdict line.
Report: the gate numbers, the grade counts if decoded, the print check result, requests per host, vision calls used.

## JOB OUT-CHECK-CLAR (account 4; Opus 5.5; cap USD 3; box 40 minutes; network: bodleian.ox.ac.uk contact page <= 2 requests; no images; Price: vision calls: 0 x USD 0 = 0)

Outreach gate 7 (CLAUDE.md Outreach (7)): the pre-send fact check of outreach/bodleian-clarendon94-roe.md (mailbox draft placed
5 Oct 2026 by the orchestrator as a reply in the existing Bodleian thread; status "awaiting check"). You are not the drafter. Read the
draft against every file and source it cites (the target folder's NOTES.md/REQUEST.md, the earlier thread draft
outreach/bodleian-rawl-a24-p4.md, CONTRIBUTIONS.md rows, the Imaging Services page for the cc address), try to falsify each factual
sentence (shelfmarks, folios, dates, counts, what was and was not checked, the recipient line), confirm the voice (outreach/README.md
rule 1a: "I" for what the person does, "we" for what the agents did) and the AI-disclosure sentence (rule 1) and the `[SIGN-OFF]`
placeholder, and write the `checked:` header line naming what you corrected (or "no correction"). Then, if the mailbox JSON exists
(outreach/mailbox/), update its body to the checked text; if a CONTRIBUTIONS.md row for this draft exists, leave it; if none, add one
(date, item, class per AUDIT.md or "no reading claimed", recipient, channel, what is asked, status "checked, not queued"). Do not queue
a SEND-QUEUE row and do not send: the parent queues after reading your checked: line. Report: corrections made, the checked: line, and
whether the draft is ready to queue.
