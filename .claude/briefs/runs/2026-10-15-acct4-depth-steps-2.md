# Depth-step jobs, second file (account-4 parent, LANE VIV-KEYSTONE, session_01D7XWmthshMVqxumdDvitPh), 15:27 UTC 15 Oct 2026

Same rules as 2026-10-15-acct4-depth-steps.md (claim, PREREG before measurement, usage self-report on every claim/halfway/done line, commit
by path, five-line report, no key/reading/status edit by a solver; rule 10 wording only). Account 1 is paused (seven_day allowed_warning,
resets 05:00 UTC 17 Oct): nothing here runs on account 1.

## JOB DV-MERCY2 (verifier; Opus 5.5; cap USD 5; box 60 minutes; disk only, no network, no readers, no images; Price: vision calls: 0 x USD 0 = 0; run by the account-4 parent as its own worker)
VERIFIER: ciphers/espagnol142-mercy-1648, item Espagnol 144 f.22 (AUDIT.md "## Depth re-rule (DV-MERCY, 8 Oct 2026)": N4, D1, 92.2%).
Claim under audit: NOTES.md "## MERCY-IMG" (15 Oct 2026) and "## MERCY-M33": with 13 of the 19 M glyphs on r16-r24 settled as transcribed
(two blind readers reproduce the H glyphs at 0.994; each glued cluster has one parse into the 2-34 key) the longest H/C/S stretch is 89
letters (r20:8-r24:13) against the authentication distance 84 (R 3.4 convention) and 135.1 (es17c). You are a separate session from both
solvers and do not protect their conclusions. Decide, per rule 4a and the DV-MERCY section's own method: (i) whether segmentation-by-key-
range of a glued cluster is S or stays M (state the rule you apply and apply it to every such cluster, not only these); (ii) which AD
convention governs this item (R 3.4 vs es17c), consistently with how DV-MERCY and the other Spanish items in status.json were ruled --
name those items; (iii) your own recount of the longest clause with every liberty counted, from the files (tools/decode_key.py --check,
mercym33/runs.py on a scratch copy with the 13 settled positions applied), and, if D2 is met, one true, specific sentence about the content
of that clause written by you. Write the ruling as "## Depth re-rule 2 (DV-MERCY2, <date -u>)" in AUDIT.md with the depth, depth_pct,
depth_sentence and the check used; if D2, the outward words are "partially deciphered (about N%)" and you propagate any wording change into
NOTES.md's status head and the SECOND-OPINIONS-QUEUE.tsv row for this target if one quotes the old depth (rule 10 propagation). If the
settled positions enter the reading at S, say so and let the parent apply key/reading edits with decode_key --check (you edit no reading).
Do not decode further, do not touch other targets. Report: depth before/after, the AD convention chosen and why, the recount, the sentence.

## JOB HEID-1621B (account 2; Opus 5.5 worker, Sonnet readers; cap USD 3; box 45 minutes; service.archief.nl <= 45 (take/release lines, >= 3 s apart); Price: vision calls: 0 x USD 0 = 0 (this worker's own eye on 700 px contact sheets, as OBRED-6021; no reader subagent))
HEID-1621's two next lines, NOTES "## HEID-1621" (ciphers/oldenbarnevelt-brederode-1605): (1) scans 370-377 of NA 1.01.02 inv. 6021 at
700 px for the letter's opening and the sender's name (scan 380 is the address leaf "Duplicaet vanden 13 Augusti 1621" to the States
General); (2) stride-1 361-397 at 700 px on contact sheets with the OBRED-6020 sheet controls for a second numeral letter, a key leaf or a
figure postscript in the same hand. PREREG-HEID1621B.md first (the stop rule, the sheet controls, what counts as a hit). Report: the sender
if read (grade M unless the name is on the leaf), every further numeral text with scan numbers, requests per host; manifest.json entries,
no image committed. If a sender is read, write the "## Premise check" update (edition step now due: name the sender's printed
correspondence, Japikse/Rijks Geschiedkundige Publicatien, and whether 1621 Heidelberg letters are printed) so the parent can run the intake
gate. No decode, no key.
