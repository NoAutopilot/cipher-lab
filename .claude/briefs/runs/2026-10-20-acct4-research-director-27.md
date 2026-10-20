# Research director, wave 27 (20 Oct 2026, 01:1x UTC by date -u): Sherwood both-unseen groups, blind digit re-read

Common tail: .claude/briefs/README.md applies (ROOM claim/done with the usage phrase, wall-clock box, no AskUserQuestion, never a dollar
figure for yourself, `tools/experiment_log.py --check`, `python3 tools/dup_check.py sherwood-cossit-1781` pasted). Solver job: report
what was found and where it was not found; no novelty class (rule 10). Pre-register before reading: write
ciphers/sherwood-cossit-1781/PREREG-SHERWOOD-REREAD.md (hypothesis, statistic, known-answer set, gate, Decision block) and push it first.

## JOB SHERWOOD-REREAD (account 4; Opus 5.5; cap USD 6; box 50 minutes; hosts: none (all images on disk); Price: vision calls: 6 x USD 0.5 + 1 reconciliation = 3.5)

ciphers/sherwood-cossit-1781 is `partial`, N3/D2, H/C/S 72.7% (157/216). SHERWOOD-MROWS (NOTES.md "## M-row pass", 20 Oct 2026) retired
n-gram column choosers for the M residue: 33 rows of mrows/mrows.tsv have margin 0.00 under both models because neither Entick candidate
occurs in period prose (Hug/Humoral, Crestfallen/Crisp ...). Hypothesis: many of these are misread cypher digits in our transcription
(the 0/6 and 3/5 shapes: 226-30 reads 220-30 = "March", 131-22 reads 151-22 = "From" on one blind read), not encoder slips or rare words.
The 33 rows sit on 22 line crops of pp.345-347 (images/crops/, tools/iiif_lines.py, 18 Oct 2026; manifest images/crops/manifest.json).
1. Crops: paste `ls ciphers/sherwood-cossit-1781/images/crops/` and the 22 crop names you will use (lines listed in mrows/mrows.tsv where
   bigram_margin and trigram_margin are both 0.00). If a crop is too tight, make a taller one the way mrows/crop_slips.py does and paste
   the command; never send a full page image to a reader.
2. Two independent blind passes, one subagent call per page per pass (3 pages x 2 passes = 6 calls): the reader gets only that page's
   line crops and transcribes EVERY cypher group on each line (page-line pairs, '?' for an unreadable digit), never our transcription,
   any decode, any Entick word or the sketch. Write tx2/passA.tsv and tx2/passB.tsv; align with tools/reconcile_passes.py.
3. Known-answer gate (pre-registered): the groups on the same lines that decode as S with bigram margin >= 4 are the known-answer set.
   Reader error = share of known-answer groups where a pass differs from ciphertext.tsv. If either pass exceeds 10%, stop: the reader is
   not trusted at this resolution; log "untested-by-this-tool (blind Opus line reads)" and change nothing.
4. A digit change on one of the 33 groups is accepted only where passA and passB agree with each other and both differ from
   ciphertext.tsv; then one reconciliation call shows the crop with the two digit strings only (no words) and confirms. Control: the
   change rate on the known-answer set; if the 33-group change rate is not clearly above it, say the changes are reader noise.
   Accepted changes go to tx2/changes.tsv (group, old, new, passA, passB, reconciliation) and to ciphertext.tsv with a dated note in
   NOTES.md (a transcription correction from the image, not a repair: rule "never silently repaired").
5. Re-decode with decode_entick.py (the bigram chooser, unchanged): a corrected group whose new cell is a headword and wins its column by
   >= 2 nats is S; otherwise it stays M. Report agreement with the sketch only afterwards, as a check. Regenerate reading.tsv/reading.txt,
   `decode_entick.py --check` passing; paste tools/judge_plaintext.py output (rule 7). New H/C/S share.
6. NOTES.md "## Digit re-read (SHERWOOD-REREAD, 20 Oct 2026)" with the six research-director questions. Do not edit AUDIT.md.
Report: reader error on the known-answer set (both passes), groups changed, rows moved M -> S, new H/C/S share, judge, five lines.
