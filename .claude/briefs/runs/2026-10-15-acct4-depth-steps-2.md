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

## JOB HEID-1621D (account 2; Opus 5.5 worker, Sonnet readers for step 3 only; cap USD 4; box 60 minutes; resources.huygens.knaw.nl <= 15 (one retry after a pause on a 503, never a loop), service.archief.nl <= 4; Price: vision calls: 2 x USD 1.4 + 1 reconciliation = 4.2 -- run step 3 only if steps 1-2 leave at least USD 4.2 under the cap, else name it as the next row)
HEID-1621C's own next line for ciphers/brederode-heidelberg-1621 (status blocked: Resolutien der Staten-Generaal nieuwe reeks 5, 1621-1622,
Roelevink 1983, unread -- Huygens retroboeken answered 503 twice, Google Books NO_PAGES). (1) One Huygens retroboeken retry for the
Staten-Generaal 1621 volume (CLAUDE.md host table: `retroboeken/<book>/<accessor>/index_html?search_term...`; sources/huygens/NOTES.md for the
accessor), searching Brederode / Heidelberg / the receipt dates 20 Aug 1621 and the letter dates 8 and 13 Aug 1621; read the calendar
entries and say whether the resolution prints or summarises the letter's content and whether it mentions cipher. If it answers 503 again:
stop that host, write one LOCAL-QUEUE.tsv row (tools/local_runner_brief.md shape) for the owner's browser naming the volume, the dates and
the question, and leave the status blocked. (2) If the edition is read: write the "## Premise check" verdict, run `python3
tools/intake_gate_check.py brederode-heidelberg-1621` and paste it; if it passes, write `specs/brederode-heidelberg-1621.json` as HEID-1621C
specified (pair+letter units, (n, n+1) constraint, one unit per word, Dutch 1621, second witness scan 375, first cheap test = unit inventory
vs an nl16 word list under a frozen pool, matched control = a synthetic 21-unit word code of the same length and unit count) and run that
first test at cap 3 within this job (control first, both numbers into the spec's `cheap_test_done` and HYPOTHESES.md). (3) Only if cap room
remains: the scan 375 second witness -- `tools/iiif_lines.py --image <scan375 1200 px> --out <dir>` pasted, two blind Sonnet readers on the
numeral lines, one reconciliation, agreement with ciphertext.tsv (scan 379) per unit as the transcription control; no reading, no key.
NOTES.md "## HEID-1621D (<date -u)" ending in the status word and the next row.

## JOB HEID-1621E (account 2; Opus 5.5; cap USD 5; box 75 minutes; service.archief.nl <= 140 (take/release lines, >= 3.1 s apart, one at a time with any other NA worker), www.nationaalarchief.nl <= 10, resources.huygens.knaw.nl <= 15; no reader subagents; Price: vision calls: 0 x USD 0 = 0 (this worker's own eye on 700 px contact sheets, the OBRED-6021 method))
ciphers/brederode-heidelberg-1621 is open (HEID-1621D: Resolutien SG NR 5 p.260 res. 1644b "Gedeeltelijk in code", no decipherment; spec test 1
undecided at N=45 units). One block of 96 numerals cannot be read alone: the next step is a POOL and the KEY (CLAUDE.md selection rule, pools
first). (1) `python3 tools/design_prior.py` for the design (two-digit consecutive-pair groups + trailing letter, Dutch agent to the States
General, 1621) and KEY-OFFICES.tsv / KEY-DESIGN.tsv for any States General or Palatinate-mission key of 1618-1625 already on file; paste.
(2) Pool: the other five sixths of NA 1.01.02 inv. 6021 (HEID-1621 read every sixth scan of 1-697; HEID-1621B read 361-397 at stride 1) --
contact sheets at 700 px by the OBRED-6020/6021 method with the same sheet controls, scans 1-360 and 398-805 at stride 6 offset by 3 from
HEID-1621's grid (so the two sweeps together cover stride 3), PREREG-HEID1621E.md first with the stop rule (80% of cap or box) and what counts
as a hit (a numeral block, a key leaf, an interlinear decipherment, a figure postscript); every hit by scan number with a 1200 px re-look of
the hit only. (3) Key: the NA finding aid for 1.01.02 (www.nationaalarchief.nl item pages, not data.nationaalarchief.nl) for 'sleutel',
'cijfer', 'chiffre' entries 1618-1625 and the Brederode liassen after 6021 (6022 onward: inventory titles only, no scans), and the Huygens
Resolutien SG NR 5 index for 'cijfer'/'sleutel'/'Brederode' entries that mention a decipherment ('gedecifreerd') in 1621-1622; list every
candidate with its inventory number and whether it is digitised. No decode, no key edit, no reading. NOTES.md "## HEID-1621E (<date -u>)":
hits, candidates, requests per host, and the next row (a transcription of any second block found, or the key leaf if one is named).

## JOB HEID-1621F (account 2; Opus 5.5; cap USD 4; box 60 minutes; service.archief.nl <= 140 (take/release lines, >= 3.1 s apart, one at a time with any other NA worker); no reader subagents; Price: vision calls: 0 x USD 0 = 0 (this worker's own eye on 700 px contact sheets, the OBRED-6021 method))
HEID-1621E's next line for ciphers/brederode-heidelberg-1621: the Resolutien SG NR 5 p.295 res. 1879b calendars Brederode's **17 Sept 1621**
letter as "S.G. 6021 (orig.). Gedeeltelijk in code" -- a sibling in the same liasse, not seen by the stride-3 screens. The liasse runs
roughly in date order (13 Aug 1621 sits at scans 375-380), so: PREREG-HEID1621F.md first (stop rule, sheet controls, what counts as a hit),
then a stride-1 screen at 700 px on contact sheets with the OBRED-6020 sheet controls from scan 398 upward, in order, stopping at the first
letter dated 17 Sept 1621 carrying numeral groups (signed letter and any duplicate, as 375/379 were) or at 136 requests, whichever first;
one 1200 px re-look of each hit only, recorded in images/manifest.json with sha1 (no image committed). Report the hit scan numbers, the
date line and signature as read (M unless on the leaf), whether the numeral system is the pair+letter design of 375/379 (by eye, M), and the
last scan screened, so the next row can continue from there. Also record in NOTES.md, as a separate intake candidate and nothing more, scan
58's French text with 2-digit groups and 3/4-digit name codes (HEID-1621E), with its date line if legible. No decode, no key, no reading.
NOTES.md "## HEID-1621F (<date -u>)" ending in the next row (the two-block transcription priced per pass, or the continuation screen).

## JOB HEID-1621G (account 2; Opus 5.5 worker, Sonnet readers; cap USD 11; box 90 minutes; service.archief.nl <= 8 (take/release lines, >= 3.1 s apart; scans already on disk are never refetched); Price: vision calls: 4 x USD 1.4 + 2 reconciliation = 8.4)
HEID-1621F's next line for ciphers/brederode-heidelberg-1621: the pool is now two letters in one key -- scan 379/375 (13 Aug 1621, 96 numerals,
pair+letter units) and scan 423 (17 Sept 1621, about 20 groups on two lines, mostly one-number+letter units that repeat the first number and
letter of the 13 Aug units: 22.x, 40.d, 46.f). Two units, two blind passes each, one reconciliation each (the per-pass pricing of CLAUDE.md
Usage 6: 2 blocks x (2 reads + 1 reconciliation)). (1) Fetch scan 423 and scan 375 at 1200 px if not on disk (manifest.json entries, sha1,
no image committed); `tools/iiif_lines.py --image <scan> --out <dir>` for the numeral lines of each, command pasted before the first reader
call; readers get only the line crops, return text only (numerals, dots, letters, in order), no key shown. (2) PREREG-HEID1621G.md first: the
known-answer control = scan 375 against the committed ciphertext.tsv (scan 379, the duplicate of the same letter): per-unit agreement must be
>= 0.90 or the pass is a non-test; the unit grammar to record (pair or single number, trailing letter, dots); the rule for M vs S (both
readers agree = S for the digits/letters as transcribed, else M; no value is read, so nothing is H/C). (3) Outputs: `ciphertext_6021_423.tsv`
(line, pos, unit, number(s), letter, confidence, why) and `ciphertext_6021_375.tsv`, the per-unit agreement table 375 vs 379, and a merged
`units.tsv` across both letters (unit id, letter, numbers, occurrences per letter) so the next spec can count the shared units. Report in
NOTES.md "## HEID-1621G (<date -u>)": agreement numbers, unit inventory (distinct units across both letters, how many are shared), whether
the 17 Sept single-number form is the 13 Aug pair's first number every time, requests per host, and the next row (the pooled spec +
first cheap test, cap 3). No decode, no key, no reading.

## JOB HEID-1621H (account 2; Opus 5.5; cap USD 5; box 75 minutes; disk only, no network, no reader subagents (the crops are on disk from HEID-1621G); Price: vision calls: 0 x USD 0 = 0)
HEID-1621G's next line for ciphers/brederode-heidelberg-1621: the 375-vs-379 known-answer control FAILed on letters (37/45 = 0.822 vs 0.90)
while the numbers agree 96/96 -- every miss is the naming of the trailing letter sign. (1) `tools/lookalike_pass.py` on the trailing-letter
signs across the reads on disk (heid1621g/ readA/readB for 375 and 423, the 379 reads of HEID-1621), the named pairs being whatever the
misses split on (list them first from the 8 misses); its 2-of-3 residual is agreement, not accuracy (CLAUDE.md Usage 6) -- report per
letter sign the agreement after the pass, and write the still-split signs to a focus.tsv for the owner's sign sorter (never blocking). Re-run
the 375-vs-379 control on the post-pass units: PASS at >= 0.90 licenses the letters at S-as-transcribed; otherwise the letters stay M and
the spec below treats the letter as an unreliable field (say so in the spec). (2) Pooled spec `specs/brederode-heidelberg-1621.json`
updated (HEID-1621D wrote the single-letter version): ciphertext = the 13 Aug units (379, with 375 as witness) + the 17 Sept units (423),
alphabet = the unit inventory (pair or single number + letter), constraints = (n, n+1) pairs, one unit per word, the 17 Sept single-number
form matches the 13 Aug pair's first number in 6/12 (either number 9/12 -- register the hypothesis "single = first number" as a counted test
against the shuffled-pairing null, not as a fact), Dutch 1621, two letters one key; cheap tests in order; `judge` block. (3) Test 1 at cap 3
inside this job, control first: unit inventory of the pooled units vs a frozen nl16 word pool (as t1/inventory.py did at N=45, now at the
pooled N), matched control = a synthetic word code with the same unit count, the same letter/number split and the same two-letter division,
scored by the same script; both numbers into `cheap_test_done` and HYPOTHESES.md. No decode, no key, no reading. NOTES.md "## HEID-1621H
(<date -u>)" ending in the status word and the next row (or "spec moved / did not move" per CLAUDE.md 3a).

## JOB HEID-1621I (account 2; Opus 5.5; cap USD 4; box 60 minutes; service.archief.nl <= 6 (take/release lines, >= 3.1 s apart; only the scans the regen script names); no reader subagents; Price: vision calls: 0 x USD 0 = 0 (lookalike_pass.py on crops; this worker's own eye on its windows only))
ciphers/brederode-heidelberg-1621 after HEID-1621H (spec did not move; the lookalike pass ran WITHOUT crops because HEID-1621G's crops were
never committed -- the brief's error, not the worker's). (1) Regenerate the crops: fetch scans 375, 379 and 423 at 1200 px only if absent
(manifest.json sha1 must match), `tools/iiif_lines.py --image <scan> --out <dir>` pasted, and write `heid1621i/regen_crops.sh` so nobody
refetches; then `tools/lookalike_pass.py` on the 22 split positions of heid1621h/focus.tsv WITH the crops, pairs as listed there (B/S, r/x,
S/g, c/r, c/x, f/s ...); report settled vs still split, re-run the 375-vs-379 control on the post-pass units (PREREG-HEID1621I.md first with
the gate 0.90 and the rule for S-as-transcribed); what stays split goes to the owner's sign sorter via focus.tsv (never blocking). (2) Rule 5:
write NOTES.md "## Remaining gaps" and "## Escalation" (tools/gaps_check.py format; `python3 tools/gaps_check.py brederode-heidelberg-1621`
must pass, paste it) ending in a Verdict; the outside blocker is the period decipherment / key material not digitised: NA 1.01.02 inv. 6056
(Mansfelt 13 Mar 1622 "in cijfer, met de oplossing", Resolutien NR 5 p.447), inv. 6055 (SG minute with code, 1621) and inv. 12578.1 (Haga key
1618-22). (3) REQUEST.md for the target: the exact Nationaal Archief reproduction request (their own order route and contact page, read on
the day and dated; shelfmark, inventory numbers, the folios or the item descriptions as the finding aid gives them, scan quality, and the
question "does 6056's 'oplossing' key cover the 1621 Heidelberg pair+letter system"), rule 9 (no personal data), and one ASKS.md row for the
owner's desk naming the cost if the NA page states one. (4) status head: `partial` only if every unread piece is blocked from outside per rule
5, else `open` with the next step named. No decode, no key, no reading. NOTES.md "## HEID-1621I (<date -u>)".

## JOB HEID-1621J (account 2; Opus 5.5; cap USD 4; box 60 minutes; resources.huygens.knaw.nl <= 20 (>= 2 s apart), service.archief.nl <= 140 (take/release lines, >= 3.1 s apart, one at a time with any other NA worker), www.nationaalarchief.nl <= 6; no reader subagents; Price: vision calls: 0 x USD 0 = 0 (this worker's own eye on 700 px contact sheets, the OBRED-6021 method))
ciphers/brederode-heidelberg-1621 pool step (HEID-1621I's next line). The Resolutien SG NR 5 (1621-1622, Roelevink) calendar Brederode's
letters with the note "Gedeeltelijk in code" where they carry cipher (p.260 res. 1644b for 13 Aug 1621, p.295 res. 1879b for 17 Sept 1621).
(1) Through the Huygens retroboeken full-text search of that volume (sources/huygens/NOTES.md for the accessor; HEID-1621D/E used it), list
EVERY Brederode entry in 1621-1622 whose note says "in code" / "in cijfer" / "gedecifreerd", with its date, the "S.G. 60xx (orig.)" inventory
pointer and the page; write `heid1621j/code_letters.tsv`. (2) For each entry pointing at inv. 6021 or 6022 and not yet located (13 Aug =
375/379, 17 Sept = 423 are done), locate the letter by date order on 700 px contact sheets (the OBRED-6020 sheet controls, PREREG-HEID1621J.md
first with the stop rule and the request budget; a liasse runs in date order, so start from the scan the neighbouring dates predict), one
1200 px re-look per hit, manifest.json entries with sha1, no image committed. (3) Report per entry: located or not, scan numbers, whether the
numeral units are the pair+letter / number+letter system (by eye, M), unit count estimate. No transcription in this job (the next row prices
it per pass: 2 reads + 1 reconciliation per block at USD 1.4). No decode, no key, no reading. NOTES.md "## HEID-1621J (<date -u>)" ending in
the next row and the projected pooled N if every located block is transcribed.

## JOB OUT-CHECK-NA1621 (account 2; Opus 5.5; cap USD 2.5; box 40 minutes; www.nationaalarchief.nl <= 6, no other network; Price: vision calls: 0 x USD 0 = 0)
Gate-7 pre-send fact check (CLAUDE.md Outreach (7)) of `ciphers/brederode-heidelberg-1621/REQUEST.md`, the Nationaal Archief reproduction
request for NA 1.01.02 inv. 6056, 6055 and 12578.1 drafted by HEID-1621I (a different session from this one -- never the drafter). Read the
draft against every file and page it cites: the NA item pages for 6021 (control, must read digitised), 6056, 6055, 12578.1 (physical only),
the NA contact/reproduction route and its public address as the institution's own page shows it today (dated), the Resolutien pages cited
(NR 5 p.260, p.295, p.447), and NOTES.md sections HEID-1621 through HEID-1621I. Try to falsify every factual sentence: inventory numbers,
dates, folio or item descriptions, what was and was not checked, the voice (outreach/README.md rule 1a: "I" for what the person does, "we"
for what the agents did), the AI-disclosure sentence (rule 1), rule 9 (no personal data, no payment details), rule 10 wording (no
"unpublished"/"first"), the [SIGN-OFF] placeholder and blank subject/recipient lines. Write the `checked:` line in the draft's header naming
what you corrected (or "nothing"), add the CONTRIBUTIONS.md row for the draft's slug (date, recipient = the NA reproduction service, class
= access request, link), and update ASKS 170 from backlog to desk with the one-line ask for the owner (send from the project mailbox per
Outreach (8) is NOT licensed by this job: the owner sends or queues it). `python3 tools/send_queue_check.py` on the draft if it has a
SEND-QUEUE row; `python3 tools/desk_check.py`; paste both. No other edits. ROOM done line with what was corrected.

## JOB HEID-1623A (account 2; Opus 5.5 worker, Sonnet readers; cap USD 14; box 100 minutes; service.archief.nl <= 10 (take/release lines, >= 3.1 s apart; scans on disk never refetched); Price: vision calls: 6 x USD 1.4 + 3 reconciliation = 12.6)
ciphers/brederode-heidelberg-1621, new material from HEID-1621J: NA 1.01.02 inv. 6022 I, Brederode, Straatsburg 12 Aug 1623 (Resolutien NR 6
p.260 res. 1721a: "bevat enkele regels in cijfer ... tot dit is opgelost" -- the States General's decipherer Joachimi solved it), located at
scans 165-167 (cipher block on 166, about 50 tokens) and its duplicate 170-172 (block on 171 with an 8-line marginal note in a smaller hand
beside it). Three units, each 2 blind Sonnet readers + 1 reconciliation (CLAUDE.md Usage 6 per-pass pricing): (1) fetch 166 and 171 at 1200 px
if absent (manifest.json sha1), `tools/iiif_lines.py --image <scan> --out <dir>` pasted before the first reader call, readers get line crops
only, text only; (2) PREREG-HEID1623A.md first: the witness control = block 166 vs block 171 per token (gate 0.90, as 375 vs 379); the rule
for S-as-transcribed; and, for the marginal note, the rule for calling it a decipherment (it must align token-for-token or word-for-word with
the cipher block under one mapping -- test with `tools/interlinear_align.py` on (group, span) pairs, the control being a shuffled pairing of
note words to groups, 200 draws) -- a note that is a summary, a docket or a clerk's remark is reported as such, not forced; (3) outputs:
`ciphertext_6022_166.tsv`, `ciphertext_6022_171.tsv` (line, pos, unit, number(s), letter, confidence, why), `note_6022_171.tsv` (the marginal
note's words, two readers, reconciled, grade M), the alignment result with its control, and, ONLY if the alignment passes its control, a
`key_1623_draft.tsv` (value -> meaning, count, grade C, source = the note) that the parent and a verifier look at before it touches any
key.tsv; (4) report: witness agreement, unit grammar of the 1623 block vs the 1621 pair (pair+letter / number+letter / bare number), whether
any 1623 unit coincides with a 1621 unit (same number and letter), the alignment numbers, requests per host. No reading of the 1621 pair, no
key.tsv edit, rule 10 wording. NOTES.md "## HEID-1623A (<date -u>)" ending in the next row (scan 181 + its note, 6 units, or the key test on
the 1621 pair if a draft key exists).

## JOB DESK-MERCY-REFRESH (account 2; Opus 5.5; cap USD 2.5; box 30 minutes; disk only; Price: vision calls: 0 x USD 0 = 0)
`python3 tools/desk_check.py` flags outreach/aymeloglu-issue-mercy.md as STALE (status dated 9 Oct; ciphers/espagnol142-mercy-1648 NOTES.md
and AUDIT.md changed 15 Oct: MERCY-M33, MERCY-IMG, DV-MERCY2 -- 13 positions settled at S, depth_pct 92.2 -> 94.7, D1 held, longest run 53 ->
89 under AD 125.9). Re-read the draft against AUDIT.md "## Depth re-rule 2 (DV-MERCY2, 15 Oct 2026)" and status.json result row for Espagnol
144 f.22; correct every sentence the change touches (counts, percentage, the depth words "fragments read", nothing above rule 10), update
its status line date, add a `checked:` line naming what changed (a separate session from the drafter, as gate 7 requires), and run
desk_check again (paste). Also look at gramont-jstor-waive (flagged stale against ciphers/eckert-1864/NOTES.md c1ba59c): say in one line
whether the Eckert change touches that draft's facts; fix only if it does. No send, no CONTRIBUTIONS change unless a slug is missing.

## JOB HEID-1623CAL (account 2; Opus 5.5; cap USD 2.5; box 40 minutes; disk only, no network, no readers, no images; Price: vision calls: 0 x USD 0 = 0)
ciphers/brederode-heidelberg-1621 after HEID-1623A: `tools/interlinear_align.py` on the 12 Aug 1623 block (64 tokens) against its marginal
clear note read "real 1 vs p95 1", and a known-true positive control also read 1 at that N -- untestable by this tool at N=63 (CLAUDE.md
rule 3, "control first"). Before anyone reads scan 181 + its note (6 priced units) for a pooled alignment at about N=85, calibrate: build
synthetic known-true (group, span) pairs with the 1623 block's own grammar (numeral groups with free-standing letters, Dutch clear spans of
the note's word-length distribution; heid1623a/grammar_1623_vs_1621.tsv), 20 seeds each at N = 64, 85, 120, 200, and run the tool exactly
as HEID-1623A did (shuffle 200); report per N the share of seeds whose positive control passes the p95 gate, and the smallest N at which
it passes in >= 90% of seeds. PREREG-HEID1623CAL.md first (the gate, the seeds, the grammar). Write the result to HYPOTHESES.md (one row,
"untested-by-this-tool below N = ..."), NOTES.md "## HEID-1623CAL (<date -u>)", and the one-line verdict: "read scan 181 for a pooled
alignment: yes (N=85 passes) / no (next instrument or more material)". No reading, no key. If the answer is no, name what else the 1623
clear note licenses (a text-known item at N0 on the leaf: AUDIT-ready as 'period decipherment on the leaf', not a reading of ours).
