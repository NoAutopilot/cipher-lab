# TOOL-BRIEF-PRICE (account-3 orchestrator, 3 Oct 2026): build tools/brief_price_check.py (RETRO-2026-10-03-acct3 P2)

Model Opus 5.5. Cap $3, box 35 min. Disk only, no images. Build exactly the gate specified in RETRO-2026-10-03-acct3.md
"Proposal 2" (docstring scope: what it catches and what it must NOT block, CLAUDE.md 8a), with tools/tests/
test_brief_price_check.py covering: F36-GLOSS's brief (.claude/briefs/runs/2026-10-03-acct3-f36-gloss.md) FAILS; a
gate-fix/print-check brief with no image step passes; a "disk only" brief passes; a brief with a correct "vision calls:
N x USD r = X" line under its cap passes; one over its cap fails; the "Opus rate unmeasured" wording passes. Then apply the
README diff in that proposal (shrink the "Vision calls are a counted unit" prose to name the tool), add the SYSTEM.md row
(tools/system_map_check.py ok), and run the gate over every .claude/briefs/runs/2026-10-0[23]-*.md, pasting the counts.
file_shrink_guard on README/SYSTEM.md. Done line "for the account-3 orchestrator".
