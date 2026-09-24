# Second opinions

Answers from outside models to the board's second-opinion prompt, filed verbatim, one file per answer, named <model>-<date>.md. Leads, not verdicts: the verifier checks every citation (see .claude/briefs/verifier.md).

Labels (24 Sept 2026). Each prompt carries a label `SO-<TARGET>` (PROMPT-chatgpt.md here). The outside model
files its answer as `chatgpt-<date>.md` in this folder on a branch `second-opinion/<label>` and opens a pull
request titled `[<label>] second opinion: ...`, never a commit to main. The orchestrator posts "for LANE V:
<folder> second opinion <label> PR #n" in ROOM.md; the verifier reads it as leads, checks every citation, and
merges or closes the PR after logging unconfirmed citations in AUDIT.md.
