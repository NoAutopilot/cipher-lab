# Research director, wave 28 (20 Oct 2026, 01:5x UTC by date -u): support jobs for accounts 1 and 2, plus Vivonne machine sort

Owner, 20 Oct 2026 ~01:45 UTC: "ok, sure" to queuing the cheapest runnable next steps for accounts 1 and 2 (their dispatchers had spawned 0
since the 16 Oct unblast because nothing was queued for them). Each job is the folder's OWN named next step, read from the regenerated
NEXT-STEPS list (tools/next_steps.py, 20 Oct 01:4x UTC) and its NOTES.md "## Escalation" section.

Common to every job below. Common tail: .claude/briefs/README.md applies (ROOM claim/done with the usage phrase, wall-clock box, no
AskUserQuestion, never a dollar figure for yourself, `tools/experiment_log.py --check`). Before any other work, paste the output of:
`python3 tools/dup_check.py <target>`, `python3 tools/intake_gate_check.py <target>` and `python3 tools/prior_work.py <target>` (warn-first);
if prior_work or the cyphersolver "BnF cipher research" folders (Lasry, published by Bourdeau 10 Oct 2026; LANE BNF-FOCUS flag 14 Oct)
show this item already deciphered, stop, record found-solved in NOTES.md and do nothing else. Then read the folder's NOTES.md "## Remaining
gaps" and "## Escalation" and do exactly the step named, no other. A scored test gets a PREREG (hypothesis, statistic, control, gate,
Decision block) pushed before it runs, and its matched control runs first (rule 3); a control below its gate stops the job. Grade per
token (rule 4); transcription from crops runs on the strongest model, crops cut with `tools/iiif_lines.py` (paste the command), never a
full page to a reader. Solver jobs: report what was found and where it was not found; no novelty class (rule 10). Update NOTES.md
(a dated section with the six research-director questions, then Remaining gaps / Escalation), run `tools/gaps_check.py <target>` before
the done line. Hosts: Gallica/openapi.bnf.fr only as each job names, one request at a time, >= 1.5 s apart; on 403/429 one retry after a
pause, then log and stop (a blocked host is a blocker, not a negative).

## JOB SUP-GIEVRE (account 2; Sonnet 5; cap USD 1.5; box 25 minutes; hosts: gallica.bnf.fr IIIF (3 views); Price: vision calls: 3 x USD 0.2 + 0 reconciliation = 0.6)
ciphers/fr3985-gievre-1593: read views 757-759 for the letter, then re-run the intake gate and set `open` if the letter is absent (the
folder's own next step). Report: letter found or absent per view, status set, three lines.

## JOB SUP-PAGET (account 2; Sonnet 5; cap USD 1.5; box 25 minutes; hosts: the pages the draft cites, one fetch each; Price: vision calls: 0 x USD 0 = 0)
ciphers/sp105-paget-1693: gate-7 pre-send fact check of outreach/soas-paget-ppms4-enquiry.md (CLAUDE.md Outreach gate 7, outreach/README.md
rule 1a voice). You are not the drafter. Read the draft against every file and source it cites, try to falsify each factual sentence
(counts, dates, shelfmarks, names, what was and was not checked, the recipient address on SOAS's own contact page), fix what is wrong,
and write the `checked:` header line naming what you corrected. Do not send anything; the owner sends. Report: corrections, three lines.

## JOB SUP-ELECTION (account 2; Opus 5.5; cap USD 3; box 30 minutes; hosts: openapi.bnf.fr (1 region request); Price: vision calls: 2 x USD 0.5 + 0 reconciliation = 1.0)
ciphers/fr5761-election-1519: step (1) of its next step only: a native-resolution crop of f.116r l.29 (1 request) and a forced-choice
third blind reader on it against the f.84r Lbar and the l.11 4 exemplars; apply the answer as its NOTES rule says. Step (2) (Lisch) is
not in this job. Report: the reader's choice with confidence, grade change if any, three lines.

## JOB SUP-MONLUC (account 2; Opus 5.5; cap USD 5; box 50 minutes; hosts: gallica.bnf.fr IIIF only if a crop is missing on disk; Price: vision calls: 3 x USD 0.5 + 1 reconciliation = 2.0)
ciphers/fr4735-monluc-lansac-poland-1573: (a) the eye look at the 7 split/low-confidence K04 tiles (~$1), then (b) c268 L26-L30 (~$3.5)
as NOTES.md "## Escalation" names it, then the K14 split and K34/K62/K40 `decode_key.py --try` re-runs only if (b) gives them input.
Stop before (b) if (a) spends more than 40% of the cap. Report: tiles settled, lines read, codes moved and their grades, five lines.

## JOB SUP-NEVREVOL (account 2; Opus 5.5; cap USD 8; box 60 minutes; hosts: gallica.bnf.fr IIIF (the six lines of f.66, at most 10 requests); Price: vision calls: 2 x USD 0.75 + 1 reconciliation = 2.25)
ciphers/fr3987-nevers-revol-1593 (Nevers to Revol, 10 Nov 1593, f.66): six-line crop, two blind passes, reconcile against
ciphers/fr3986-nevers-revol-1593's sign_guide/atlas (same copyist family), decode with the sibling key, and a shuffled-key control first (the control must be
able to fail differently: shuffle values, score the same statistic). If the decode beats the control, grade per token and set the folder
`partial`; if not, log the numbers and keep `blocked`/`open` with the blocker named. Report: pass agreement, control vs target, grades.

## JOB SUP-CEPPO (account 2; Opus 5.5; cap USD 4; box 45 minutes; hosts: gallica.bnf.fr IIIF (fr.4715 f.20, at most 8 requests); Price: vision calls: 3 x USD 0.5 + 1 reconciliation = 2.0)
ciphers/ceppo-nevers-fr3251-1570s: the fr.4715 f.20 glosses for the f.21v count-1 pairs that have no glossed side on disk (UNA-CEPPO
9 Oct 2026), aligned with `tools/interlinear_align.py` (grade C from the gloss), then `decode_key.py --check`. Report: pairs gained,
f.21v tokens moved and grades, H/C/S share before/after, five lines.

## JOB SUP-PISANY (account 2; Opus 5.5; cap USD 4; box 45 minutes; hosts: gallica.bnf.fr IIIF only if a crop is missing on disk; Price: vision calls: 4 x USD 0.5 + 1 reconciliation = 2.5)
ciphers/fr16045-pisany-rome-1585: the f.244r overlap double reads NOTES.md "## Escalation" names (L06 p27-p30, L08 p25 ...), two blind
reads per span and one reconciliation, then the re-decode it names. AUDIT.md is the verifier's: if a counted reading changes, say so in
NOTES.md and ROOM.md for a verifier; do not edit AUDIT.md. Report: spans settled, tokens moved, grades, five lines.

## JOB VIV-MSORT (account 4; Opus 5.5; cap USD 3; box 40 minutes; hosts: none (tiles on disk); Price: vision calls: 0 x USD 0 = 0)
ciphers/fr16104-vivonne-spain-1572, RESEARCH.md 6d instrument (2): an unsupervised machine sort-into-shapes of the same 36 ink-40 tiles
the owner's blind sorter shows (tx/ksplit/tiles/, tiles.tsv), image features only (no labels, no truth, no key values), scored against
tx/ksplit/truth.tsv after the sort is frozen. Held until now so the two sorts could be compared; the owner's sort has not landed in three
days (ASKS 173 still open, sorter empty 20 Oct 01:2x), and scoring the machine sort first does not touch the owner's blind page. PREREG
first (statistic: purity / adjusted Rand vs truth; null: the same clustering on label-shuffled tiles and on random features, 20 draws;
gate: beats the null p95). Do not show the machine sort or truth on the sorter page or anywhere the owner sorts. Update RESEARCH.md with
a dated 6e entry and the six questions. Report: purity/ARI vs null, whether label c splits into p vs e/q, five lines.
