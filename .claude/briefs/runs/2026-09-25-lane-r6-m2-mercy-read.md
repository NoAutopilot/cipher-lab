LANE R6 M2 -- espagnol142-mercy-1648: from the annealed key to a graded reading (Fable, cap $15, box 75 minutes; disk only).
Common: 2026-09-25-lane-r6-common.md. Parent 7c's instruction (ROOM 17:30): a Fable read of the best decode against the 1648 Brussels context
and a crib loop, reported only with judge output.
Intake gate (live, 25 Sept 17:46 UTC): "espagnol142-mercy-1648: open (line 1) -- edition/page or full-text-search citation found within 6 lines" (exit 0).
State (Y8, NOTES.md "Y8: spec and first test"): 521 code tokens over 38 values; the homophonic anneal on es17 reaches -1154.3 on 4 seeds against
a matched control best of -1321.7 (5 seeds, spread ~35); judge FAILs language at -1.048 (null_p99 -1.88, real_p05 -0.897). Fragments such as
"elector de Brandenburg", "cartas de creencia", "mil hombres" / "infanteria" appear; 7 letters (f g h k w x z) have no code.
Job: (1) Read candidate_reading_*.txt against ciphertext.tsv's plain Spanish context (the address to the Baron de Mercy, the connectives,
"Barneton a seis Junio de 1648"); propose code->letter corrections one at a time, each justified by >= 2 independent occurrences (a word that
reads in two places), never by one; codes that may be nulls, homophones or words stay open. Keep a log (corrections.tsv: code, old, new, the
occurrences that justify it). (2) Crib loop with a control (rule 3 gain gate): before trusting any gain, run the same correction procedure on
the Y8 matched control's decode (cheap_test_1/) and report how many points the procedure adds there; the target's gain must clearly exceed the
control's. (3) Write key.tsv (code, letter, grade S where the correction log and the control support it, M otherwise), decode.json, and
`tools/decode_key.py ciphers/espagnol142-mercy-1648 --check` exit 0; reading.txt with the plain framing restored in place. (4) Paste
`tools/judge_plaintext.py specs/espagnol142-mercy-1648.json --file reading.txt` (es17 corpus; if it FAILs, report the FAIL). (5) Historical sense
check only as context: does the reading fit Spanish Netherlands affairs in June 1648 (Münster, Brandenburg, troop numbers)? Name what you
checked; do not search for the letter in print (that is the verifier's job). NOTES.md section "## M2: graded reading (25 Sept 2026, LANE R6)".
Grades per token and counts (rule 4: no H or C means "cryptanalytic result"). ROOM done: "for LANE V6: ciphers/espagnol142-mercy-1648 reading
ready, S <n> M <n>, judge <PASS/FAIL score>" if it reads; else "for LANE R6: mercy M2 <what blocked>". Report what was found and where it was
not found; do not classify novelty; no rule-10 words.
