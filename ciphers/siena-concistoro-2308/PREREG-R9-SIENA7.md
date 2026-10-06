# PREREG R9-SIENA7 -- no. 7 anchored homophonic fit (6 Oct 2026, written before any scored run)

Worker R9-SIENA7 (account 4, LANE LANE-RUN9-account-4), brief `.claude/briefs/runs/2026-10-06-account4-run9-jobs.md`.
Script `specs/cheap-tests/siena-concistoro-2308/run_test_no07.py` (committed with this file); output `results_no07.json`.

**Material.** `transcripts/no07.tok`: 20 cipher runs, 363 tokens, K=45 (Bourdeau agent J, CC BY 4.0, adbf9a1). Fixed values
= the seven grade-C glosses of `glosses_no07.tsv`: q=a, 6=n, +=o, 2=e, x=r, c=o, QP=e (88 tokens, 24.2%). The four M glosses
are not fixed.

**Solver.** `tools/homophonic_anneal.py` solve(), unchanged: order-3 add-k character model, unigram weight 1.0, 20 restarts x
60,000 iterations, sign -> one of 24 folded letters, fixed signs never move.

**Corpus (era).** No 15th-century Italian corpus exists in tools/data. Model = tools/data/it16dip (16th-c. Italian diplomatic
letters, 1520s-1560s) minus one held-out file, gri_33125010469852 (Desjardins/Canestrini II, Florentine despatches), which
supplies the control plaintext. Not era-matched to a 1450s Sienese despatch (Milan embassy, per Bourdeau's description): a
real era and orthography gap (e.g. 15th-c. Sienese "et", "ch", doubled consonants), stated, not corrected.

**Matched control (rule 3).** Per seed: 20 windows of the held-out text with no. 7's own run lengths, concatenated (so the run
breaks are matched), N=363, enciphered with a random K=45 homophonic key (tools' make_control allotment); seven of its signs
carrying the letters a, n, o, e, r, o, e at the token counts nearest the target's fixed signs (10, 6, 10, 11, 25, 24, 2) are held
fixed. Same solver, same settings. Seeds 1-5. Reported per seed: letter accuracy overall and on unfixed tokens, both for the
anchored solve and for a blind solve (no fixes) of the same cipher (headroom check: the blind baseline must not already be
near ceiling for the anchors to mean anything).

**Gate.** Control anchored mean letter accuracy (overall) >= 0.60 over seeds 1-5. If below: stop, log "non-test at this N"
for the anchored homophonic family on no. 7, do not run the target. Statistic varies with the manipulation (accuracy depends
on what the solver recovers; the fixed signs alone give 24%).

**If the gate passes.** Target with the seven fixes, seeds 1-3, best score reported with its decode; the decode judged by
`tools/judge_plaintext.py specs/siena-concistoro-2308.json --file <decode>` (spec language `it` = it16, FAIL reported as FAIL),
and the same solver's decode of the order-shuffled target (seeds 1-3, same fixes) judged the same way (ARM-C1: a PASS on a
shuffled decode voids the judge as a gate for this family at this N). Any value it yields enters no key file above M.
