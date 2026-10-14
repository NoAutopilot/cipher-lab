# PREREG-SALV-TRY (14 Oct 2026, written 07:48 UTC by date -u, before any --try run or re-score)

Worker SALV-TRY (Opus), LANE DEFAULT-A1-0640-14 (account 1), brief `.claude/briefs/runs/2026-10-14-acct1-default-0640-jobs.md`
"Wave 4" + row SALV-TRY. Hypothesis: our sign `nt^` (95 tokens, mapped to his u/v cell by both SALV-LKEY passes, value u, grade M)
is George Lasry's "ss" cell (look-alike exemplars; SALV-LKEY's f54r L14 side by side). Key: lkey/key_lasry.tsv (published, credit
George Lasry, D. Bourdeau cyphersolver dde5b0ea, CC BY 4.0), never edited; the hypothesis is held in memory only.

1. `python3 tools/decode_key.py ciphers/fr2933-salviati-1525 --config ciphers/fr2933-salviati-1525/decode_lasry.json --try 'nt^=ss'
   --lm it16 --nulls 200` (its own two nulls: shuffled positions, value class). Verdict as the tool prints it. Grade if accepted: M
   (the tool's K3 letter-control passed only for a single-letter value in a Danzay/Gramont letter cipher; "ss" in a syllabary is
   neither, so M regardless). Logged to crossword_log.tsv.
2. Known answer, f54r L14 only (his excerpt "che l'essere restituita la possessione basti", salviati1525/NOTES.md): the three nt^
   tokens (L14 pos 4, 14, 16) stand at "l'e-SS-ere", "po-SS-e", "e-SS-io" by the alignment SALV-LKEY published before this file.
   Count = keyed L14 tokens whose value matches his excerpt syllable, before (u) and after (ss), on the pre-set alignment:
   pos2 che, pos3 le (l'e), pos4 ss, pos5 e, pos6 re, pos7 re, pos8 s, pos11 ta, pos13 po, pos14 ss, pos15 e, pos16 ss.
   (pos10 ci vs his ti/tu, pos17 et vs his io and pos18 ne|no|nu are counted as they stand, unchanged by this test.) This line is
   the source of the hypothesis, so it is a consistency figure, not evidence; evidence is items 1 and 3.
3. Re-score with lkey/score_lasry.py logic, same 300 permuted keys (seed 1, same class lists; nt^ stays in class "letter"), with
   nt^ = ss in memory: 4-gram mean (all and per leaf) and >=4-letter it16 word hits, target vs permuted p99 and rank. Written to
   lkey/score_try_ntss.json; score.json untouched. Same gate as PREREG-SALV-LKEY item 5: all-letter 4-gram target > permuted p99.
   Also reported: the same re-score with nt^ = u (reproduction check of score.json; must match it exactly or the comparison is void).
4. Reading: gain on (1) accepted AND (3) moves the 4-gram score up => "nt^=ss supported, M"; (1) rejected or (3) moves down =>
   "not supported by this test"; otherwise undecided. No key edit, no re-grading, no further mapping pass, no novelty classification.
