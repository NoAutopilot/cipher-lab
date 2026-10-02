# NEVBIR-LOOKALIKE (account-3 orchestrator, 2 Oct 2026)

Target: ciphers/nevers-birago-fr3251-1572, the two short runs no.73 (f.144r, 90 signs) and no.85 (f.168r + f.168v
head, 121 signs). Model Opus 5.5. Cap $5, box 50 min. Disk + Gallica IIIF only (crops already on disk; refetch
nothing that is already in images/manifest.json).

Why: both runs read under the published 1572 key + T42=m but the 200-shuffle control has no power at their
length and the measured reader error (0.24 on f.144r, 0.13 on f.168). NEVBIR-POOL (2 Oct) pooled them: still not
licensed. The lever is reader error, not more text. The 1570-71 Ceppo-Nevers leaves use an earlier key and cannot
be pooled.

Steps
1. Confusion map (disk only): from every 1572 two-reader pass on disk (harvest/*/pass*.tsv, f139v, f152r, f174r,
   f174vA, no86B, f184r, f178*), tabulate which sign-sheet labels the two readers swap, with counts. Write
   harvest/confusion_1572.tsv (label_a, label_b, n, examples).
2. Look-alike pass: for every f.144r and f.168 tile whose two readers disagreed, or whose label sits in a top-10
   confusion pair, one Opus subagent call per run (line crops only, never the full canvas; Usage 6) re-reads that
   tile against the sign-sheet crops for the candidate labels only. N reads + 1 reconciliation, priced per call.
3. Re-run the control: printed key + T42=m, 200 shuffled keys, seeds 1-3, plus the power control at the NEW
   measured error. Write both numbers to HYPOTHESES.md. Rule 3: report rank, z, power side by side; non-test is
   not a negative.
4. Human-review package (owner's request, 2 Oct 2026: signs that machines cannot settle go to the owner's sign
   sorter for when he has time -- never block on it). Write sorter/ inputs for tools/sign_sorter.py:
   sorter/signs.tsv, sorter/labels.tsv, sorter/pages/ (the public Gallica line crops already on disk), and
   sorter/focus.tsv (sid<TAB>question) listing every tile still split after step 2, with the two candidate labels.
   Build the HTML once into your scratch dir to prove it renders; do NOT publish an artifact (the account-3
   orchestrator publishes it to the owner). Add sorter/README.md with the build command, like
   ciphers/debosnys-1883/sorter/README.md.
5. NOTES.md: update the f.144/f.168 rows, Remaining gaps/Escalation, run tools/gaps_check.py; update PROGRESS.tsv
   rows "Birago 1572 f.144" and "Birago 1572 f.168" notes (firm counts only if the control now licenses S grades).

Gates: stop before step 3 if step 2 has not lowered the measured disagreement on either run (log "no lift",
skip to step 4). Report what was found and where it was not found; do not classify novelty.
Room: claim, halfway, done via tools/room.py; done line names the commit and "for the account-3 orchestrator".
