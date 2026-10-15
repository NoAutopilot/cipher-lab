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

## JOB HEID-1621C (account 2; Opus 5.5; cap USD 4; box 60 minutes; resources.huygens.knaw.nl <= 20, archive.org <= 10, de-crypt.org listing <= 5, no images; Price: vision calls: 0 x USD 0 = 0)
HEID-1621B read the sender: P. van Brederode, agent at Heidelberg, to the States General, 13 Aug 1621 (NA 1.01.02 inv. 6021 scans 375 signed
+ 379 duplicate, same numeral block, 96 numerals, word-level pair+letter code lead). The anonymous-pile path ends; the normal gate applies.
(1) Check-solved by sender (CLAUDE.md pipeline step 2 and .claude/briefs/check-solved.md): the Resolutien der Staten-Generaal nieuwe reeks,
1621 volume (Roelevink), around the receipt date 20 Aug 1621, through the Huygens retroboeken search (CLAUDE.md host table: Staten-Generaal
retroboeken) -- does the resolution summarise or print the letter's content or its cipher; Brederode's printed correspondence (any edition:
search archive.org and Google Books API with country=US for "Brederode" "Heidelberg" 1621 and the quoted opening "bekomme ick advijs");
DECODE listing, Cryptiana, both solver repositories, the NA notice for 1.01.02 inv. 6021; `tools/prior_work.py` with the shelfmark. Write
the "## Premise check" verdict (open / found-solved / blocked, naming the edition and pages actually read, or the one it could not open) in
a NEW target folder `ciphers/brederode-heidelberg-1621/` (NOTES.md head per rule 5; ciphertext.tsv copied from
ciphers/oldenbarnevelt-brederode-1605/heid1621/ciphertext_6021_379.tsv with its grades; images manifest entries pointing at the NA scans,
no image committed; a one-line pointer section "## Split to ciphers/brederode-heidelberg-1621" in the oldenbarnevelt NOTES.md). (2) Run
`python3 tools/intake_gate_check.py brederode-heidelberg-1621` and paste its output. (3) If the gate passes, write `specs/brederode-
heidelberg-1621.json` (CLAUDE.md 3a: ciphertext as transcribed with source and date, alphabet = the pair+letter units, constraints = pairs
are (n, n+1), one unit per word, Dutch 1621, second witness scan 375 for a transcription control, cheap tests in order -- first: unit
inventory vs a Dutch word-frequency list under a frozen pool, with the matched control a synthetic 21-unit word code of the same length;
a `judge` block on the nl corpus if tools/data has one, else say so). No decode, no key, no reading. NOTES.md "## HEID-1621C (<date -u>)"
ending in the verdict and the next breadth row (cap 3) the parent should queue.
