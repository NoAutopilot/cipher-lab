# MQS-SEGMENTER (LANE MQS next, account 4) -- brief stub

Written 2026-10-09 by the LANE MQS orchestrator (account 4, session_01M1fN8Gk2cnaYWXybwXW1xD) at close step 3a. A stub: the
lane orchestrator that picks this row up reads the research row and the named tools, and sharpens the known answer and
gate into a pre-registration (`tools/tests/PREREG-MQS-SEGMENTER.md`, pushed before any scoring) as its worker's first step.

- **Model, cap, box:** Sonnet, cap USD 2.5, box 90 min.
- Goal (research/MARY-STUART-TALK-2026-10-09.tsv row M18, "Highlight plausible fragments automatically in solver output"): Also covers M24 (word division as a separate last step): later SEGMENTER: one shared era-lexicon segmenter (start from judge_plaintext.cover's greedy segmentation) feeding judge_plaintext.py --fragments K (null = the same list from the shuffled-target decode, ARM-C1 rule) and decode_key --consistency Gap as recorded: No tool lists the fragments; undivided decodes have no segmenter
- **Known answer and gate:** a known-answer control of the same design, length and language as the intended use, with a
  shuffled or permuted null that can differ from the target on the statistic computed (CLAUDE.md rule 3); report both
  numbers; a control that misses its gate ships the option at most `weak` on tools/data/tool_shelf.tsv and is not re-briefed.
- **Files:** only the tool(s) named above, their offline tests in tools/tests/, the PREREG file, tool_shelf rows and the
  SYSTEM.md row (append and rebase). No status, key, reading or AUDIT.md change anywhere; nothing from ciphers/debosnys-1883
  or the private repository; no Birago 1572 family value-bearing page for the owner while ASKS 118 is open.
- **Credit (CLAUDE.md rule 8):** CTTS (Lasry); Lasry, Biermann and Tomokiyo 2023 (Cryptologia 47:2)
- **Common rules:** as in `2026-10-09-acct3-mqs-sheets.md` ("Common rules"), with this job's name MQS-SEGMENTER.
