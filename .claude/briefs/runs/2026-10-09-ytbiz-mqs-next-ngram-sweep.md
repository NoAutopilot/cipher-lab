# MQS-NGRAM-SWEEP (LANE MQS next, account 4) -- brief stub

Written 2026-10-09 by the LANE MQS orchestrator (account 4, session_01M1fN8Gk2cnaYWXybwXW1xD) at close step 3a. A stub: the
lane orchestrator that picks this row up reads the research row and the named tools, and sharpens the known answer and
gate into a pre-registration (`tools/tests/PREREG-MQS-NGRAM-SWEEP.md`, pushed before any scoring) as its worker's first step.

- **Model, cap, box:** Sonnet, cap USD 2, box 80 min.
- Goal (research/MARY-STUART-TALK-2026-10-09.tsv row M13, "Score S = sum N_g log F_g / sum N_c^2 with 5-grams from an era corpus"): MQS-SOLVER: --norm nc2paper (raw sum divided by sum N_c^2, no floor), every norm run at --uni-weight 0 and 1, docstring corrected; later NGRAM-SWEEP (3/4/5-gram x norm on the matched control) Gap as recorded: --norm nc2 is not the paper's score: it subtracts a floor per n-gram before dividing (which changes rankings between keys with different sum N_c^2) and the solver adds a KL unigram term (uni_weight default 1.0); the docstring's 'the ranking is exactly the paper's' is wrong. Its one real use was a NON-TEST (clair1161 planted control 0/3); C1161-LOLO diagnosed why: "nc2 rewards rare letters at this free share (D2, D3)" (clair1161 tx/PREREG_reanneal_lolo.md point 1)
- **Known answer and gate:** a known-answer control of the same design, length and language as the intended use, with a
  shuffled or permuted null that can differ from the target on the statistic computed (CLAUDE.md rule 3); report both
  numbers; a control that misses its gate ships the option at most `weak` on tools/data/tool_shelf.tsv and is not re-briefed.
- **Files:** only the tool(s) named above, their offline tests in tools/tests/, the PREREG file, tool_shelf rows and the
  SYSTEM.md row (append and rebase). No status, key, reading or AUDIT.md change anywhere; nothing from ciphers/debosnys-1883
  or the private repository; no Birago 1572 family value-bearing page for the owner while ASKS 118 is open.
- **Credit (CLAUDE.md rule 8):** Lasry, Biermann and Tomokiyo 2023 (Cryptologia 47:2) App. A
- **Common rules:** as in `2026-10-09-acct3-mqs-sheets.md` ("Common rules"), with this job's name MQS-NGRAM-SWEEP.
