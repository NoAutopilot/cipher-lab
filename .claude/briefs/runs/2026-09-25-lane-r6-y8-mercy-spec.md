LANE R6 Y8 -- espagnol142-mercy-1648: spec and first cheap test (Sonnet, cap $5, box 45 minutes). Common: 2026-09-25-lane-r6-common.md.
Intake gate (live, 25 Sept 16:18 UTC): "espagnol142-mercy-1648: open (line 1) -- edition/page or full-text-search citation found within 6 lines" (exit 0).
CLAUDE.md 3a: breadth before campaign. State (Y6): ciphertext.tsv, 521 code/mark tokens over 38 distinct values plus 174 plain Spanish words,
pass agreement 95.3 percent; no published key of the office found. A 38-value set with plain framing looks like a letter cipher (monoalphabetic
with a few homophones or code words) under Spanish plaintext.
Job: (1) a Spanish c.1600-1650 prose corpus of >= 200k letters that is not a target reading: fetch Cervantes/Quevedo prose once from archive.org
(djvu txt; NOT gutenberg.org, which LANE GOLD's worker holds today), clean, save to tools/data/es17/ with a README row; wire it into
tools/judge_plaintext.py LANG_CORPORA as es only if its selftest passes. (2) specs/espagnol142-mercy-1648.json per specs/README.md (ciphertext as
transcribed with source and date, alphabet, constraints -- the plain framing words are context, cheap tests in order, a judge block). (3) First
cheap test: tools/homophonic_anneal.py on the code stream (codes only, marks as the design says; try marks ignored and marks as separate
symbols) with the es17 corpus; matched control FIRST: a synthetic Spanish text of the same N, same 38-symbol count and the target's own code
frequency profile, encrypted the same way, 3 seeds; report control token accuracy and the target's score vs the control's score. Only if the
control reads >= 80 percent does the target result mean anything. Write both numbers to cheap_test_done. If the target decode reads as Spanish,
paste `tools/judge_plaintext.py specs/espagnol142-mercy-1648.json --file <reading>` and route "for LANE V6"; if not, the negative with its control
is the result. NOTES.md section "## Y8: spec and first test (25 Sept 2026, LANE R6)". Hosts: archive.org only. ROOM done: "for LANE R6: mercy test 1
target <x> vs control <c>%". Report what was found; do not classify novelty.
