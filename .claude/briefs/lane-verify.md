# LANE VERIFY (standing; account-3, spawned by the account-3 orchestrator). Read `.claude/briefs/lane-common-blast.md` first.

Scope: verification for every other lane, so readers never wait on audits. In order: (1) WORK-QUEUE rows `AUD2-*`/`AUD1-*` addressed to
account-3 (claim each with work_queue.py, one verifier session per row); (2) `python3 tools/verify_backlog.py` then VERIFY-BACKLOG.tsv
audit2 rows at high priority; (3) G3 checks (prior-work-step.md check 5) on first-audit N3 items that lack them; (4) depth re-rules
handed up by LANE DEPTH. Never verify an item this account read or first-audited; if a row is, re-address it to another account and say
so in ROOM. Verifier template and the depth bar file apply verbatim; every verifier also runs prior-work-step.md checks 3-5 and logs
them in AUDIT.md (the search-family log the gate will later read). Second-opinion rows at N3+ per CLAUDE.md. Cap 60, box 600.
