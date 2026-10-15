# Depth-step jobs queued by the account-4 parent (LANE VIV-KEYSTONE, session_01D7XWmthshMVqxumdDvitPh), 15 Oct 2026 13:15 UTC

Why: in the last 24 h about 50 lane jobs ran on next-step rows and no target moved a class. These four each aim at one named
depth step (rule 4a) on a target already at N3/N4. All report to the account-4 parent (ROOM.md "for LANE VIV-KEYSTONE (account 4)");
the account that runs them ledgers them. Each worker: CLAUDE.md first, `python3 tools/room.py --start`, last 30 ROOM.md lines, claim
before any edit, PREREG file pushed before any measurement, usage self-report on every claim/halfway/done line, commit by explicit path,
pull --rebase, push to main, five-line report. None edits key.tsv, a committed reading, AUDIT.md or status.json: each ends with a
"for the verifier" paragraph in NOTES.md and the parent decides what goes to a verifier. Rule 10 wording only.

## JOB THUR-P188 (Opus 5.5 worker, Sonnet readers; cap USD 6; box 75 minutes; disk only, no network; Price: vision calls: 2 x USD 1.4 + 1 reconciliation = 4.2)
ciphers/thurloe-printed P4 (Stamford, Calais, 13 March 1655; N4 D2 97.9%). D3 is withheld only because p.188 lines 50-61 (144 of 424 numerals,
interleaved with 29 non-numeral tokens such as 'am.' x7) do not read (status.json depth_note; AUDIT.md THUR-P4-DEPTH). Verifier V3a's own
suggestion (NOTES.md section 21, 24 Sept 2026, not done): re-check the p.188 line associations against the page image before anything else.
Steps: (1) crop lines 50-61 from images/collectionofstat03thur_leaf0198_p188.jpg with `tools/iiif_lines.py --image ... --out <dir>` (paste the
command), two blind Sonnet readers on the line crops (numerals and the interleaved words, text only), one reconciliation against the crops;
(2) PREREG-THURP188.md before scoring: hypotheses in order -- (a) the djvu/print tokenisation split or joined digit groups (compare against the
reconciled image read), (b) a compositor line transposition (try each adjacent-line swap), (c) the 'am.' tokens are set signs for a key
value (test the siblings' printed forms); statistic = share of the 144 numerals that read under the fixed period key (P4's key, no edit) as
ordinary French/English text, scored by tools/judge_plaintext.py's P4 spec; null = 200 shuffles of the line order and of the group boundaries;
gate = target share above the null p95 AND at or near the siblings' own share (NOTES gives it). (3) Report the block's reading if the gate
passes, graded per token, with the one hypothesis that did it; otherwise log all three as tested with numbers. NOTES.md "## THUR-P188 (<date -u>)",
HYPOTHESES.md one row per hypothesis with the control. Stop before a unit that would cross 80% of cap or box.

## JOB MERCY-M33 (Opus 5.5; cap USD 4; box 60 minutes; disk only, no readers, no images; Price: vision calls: 0 x USD 0 = 0)
ciphers/espagnol142-mercy-1648, Espagnol 144 f.22 (N4 D1 92.2%): D1 because the longest S run is 53 letters against an authentication
distance of 84 (R 3.4 convention) / 135 es17c, with 33 M ordinary letters still open (AUDIT.md "Depth re-rule (DV-MERCY, 8 Oct 2026)").
Steps: PREREG-MERCYM33.md first (the 33 positions listed; the registered accept rule for `tools/decode_key.py ciphers/espagnol142-mercy-1648
--try CODE=VALUE` with `--avalanche`, and its value-class control exactly as MQS-CROSSWORD describes; the run statistic = longest S/C/H run
in letters before and after, every liberty counted). Run --try at every occurrence for each of the 33 under the es17c judge; accept only what
passes the registered rule; then report the longest clean run before/after against both AD figures, and whether any accepted value joins two
runs. No key.tsv edit: write the accepted values and their numbers to NOTES.md "## MERCY-M33 (<date -u>)" and HYPOTHESES.md; if a run crosses
84, say so in the "for the verifier" paragraph (the verifier decides D2, with the R 3.4 vs es17c convention question flagged to the parent).

## JOB LVN-NAMES (Opus 5.5; cap USD 6; box 90 minutes; resources.huygens.knaw.nl <= 10, archive.org <= 10; no images; Price: vision calls: 0 x USD 0 = 0)
ciphers/lodewijk-van-nassau-1573-74, letters 4610/4611/4616 (N4 D2, 58-73%; key ours from the 4613/4615 period sheets): the gap to D3 is
largely the 575 U name/null codes above 120 (status.json depth_unread). Steps: list the codes above 120 by frequency across the three
letters with their decoded contexts (tools/decode_key.py --consistency or the folder's own decode); PREREG-LVNNAMES.md first: a pool of
candidate names and places frozen BEFORE scoring (Groen van Prinsterer Archives IV's index for Oct 1573-Apr 1574, the 4613/4615 period
sheets' own name values, KEY-OFFICES.tsv), a known-answer control = the codes above 120 whose value the period sheets already give (held
out, must be recovered at the registered rate), and the shuffled-pool null. For the ten most frequent unread codes run `tools/name_candidates.py
ciphers/lodewijk-van-nassau-1573-74 --code C --sender --recipient --date` then `decode_key.py --try CODE=VALUE` at every occurrence; report
per code: candidate, --try verdict, occurrences, grade M. No key edit (AX2-172's data-conflict rule: a code with conflicting H support stays M).
NOTES.md "## LVN-NAMES (<date -u>)": what the ten add to the H/C/S share if a verifier accepts them, and the control numbers.

## JOB HEID-1621 (Opus 5.5 worker, Sonnet readers; cap USD 6; box 75 minutes; service.archief.nl <= 12 (take/release lines, >= 3 s apart); Price: vision calls: 2 x USD 1.4 + 1 reconciliation = 4.2)
ciphers/oldenbarnevelt-brederode-1605 NOTES "## OBRED-6021" (15 Oct 2026): NA 1.01.02 inv. 6021 scan 379 is a Dutch letter, Heidelberg,
August 1621, with about 12 lines of two-digit consecutive-pair groups each followed by a letter (22.23 x, 40.41 d ...), sender not read.
This is new material and gets the intake path, not a solve attempt: (1) fetch scans 378, 379, 380 at 1200 px (manifest.json entries, sha1,
no image committed above the folder's 30 MB); (2) check-solved by holder, shelfmark, scan and glyph set per CLAUDE.md's anonymous-pile
paragraph (DECODE, Cryptiana, both solver repositories, the NA notice; `tools/prior_work.py`; edition step deferred until the sender is
read), written as "## Premise check" + verdict in a new NOTES.md section (a new target folder is NOT created by this job: a subsection of
the oldenbarnevelt folder named "## HEID-1621", the parent splits it off if it is unsolved and the sender is Brederode's circle);
(3) line crops with `tools/iiif_lines.py --image <scan379.jpg> --out <dir>` pasted before the first reader call, two blind Sonnet readers
of the numeral lines and the dateline/subscription only (text only), one reconciliation; a transcription TSV of the groups (pair, letter)
graded M; (4) PREREG-HEID1621.md before any count: the cheap structural test only -- are the pairs always (n, n+1), how many distinct
pairs, do the trailing letters form a small alphabet, and does a pair+letter unit count match a syllable or word count for a Dutch line
of that length (control: the same statistics on OBRED's no. 92 groups, which are a different design). No family_run, no key, no reading:
report the design class the numbers suggest, as a lead (M), and the sender if the neighbouring scans name him. Requests per host in the
done line. NOTES.md "## HEID-1621 (<date -u>)".

## JOB MERCY-IMG (added 14:25 UTC 15 Oct 2026; Opus 5.5 worker, Sonnet readers; cap USD 6; box 75 minutes; openapi.bnf.fr <= 6 (take/release lines, >= 3 s apart; a canvas already on disk is never refetched); Price: vision calls: 3 x USD 1.4 + 1 reconciliation = 5.6)
MERCY-M33's own next line: the 33 M ordinary letters of Espagnol 144 f.22 sit mostly on r17-r24 (NOTES "## MERCY-M33", table), and the
statistic could not move the 53-letter run because every accepted position sits beside another M. Image step, not a statistic: crop r16-r24
of f.22 from the native image on disk (images/manifest.json; fetch only if absent) with `tools/iiif_lines.py --image <leaf> --out <dir>`
(paste the command), two blind Sonnet readers on the row crops for the cipher glyphs only (text only, no key shown), one reconciliation
against the crops. PREREG-MERCYIMG.md first: the known-answer control = the H/S positions on the same rows (readers must reproduce the
committed glyph at >= 0.90 or the pass is a non-test), the rule for when a reader agreement re-labels an M glyph (both readers agree on a
glyph that key.tsv maps to one letter, and the glyph differs from the one the transcription carries), and the run statistic re-run with
`mercym33/runs.py` on a scratch copy. Report per M position: transcription glyph, reader A, reader B, settled glyph, key letter, grade (M
unless the control passed and both agree); longest run before/after against 84 (R 3.4) and 135 (es17c). No key.tsv, reading, AUDIT.md or
status.json edit; HYPOTHESES.md one row with the control; NOTES.md "## MERCY-IMG (<date -u>)" ending in a "for the verifier" paragraph.
