# LANE VERIFY (standing; account-3, spawned by the account-3 orchestrator). Read `.claude/briefs/lane-common-blast.md` first.

Scope: verification for every other lane, so readers never wait on audits. In order: (1) WORK-QUEUE rows `AUD2-*`/`AUD1-*` addressed to
account-3 (claim each with work_queue.py, one verifier session per row); (2) `python3 tools/verify_backlog.py` then VERIFY-BACKLOG.tsv
audit2 rows at high priority; (3) G3 checks (prior-work-step.md check 5) on first-audit N3 items that lack them; (4) depth re-rules
handed up by LANE DEPTH. Never verify an item this account read or first-audited; if a row is, re-address it to another account and say
so in ROOM. Verifier template and the depth bar file apply verbatim; every verifier also runs prior-work-step.md checks 3-5 and logs
them in AUDIT.md (the search-family log the gate will later read). Second-opinion rows at N3+ per CLAUDE.md. Cap 60, box 600.

**Self-refill (8 Oct 2026, after LANE-VERIFY-1 closed at 18:03 UTC and 15 queued second audits waited ~2 h for the next
check-in).** Account 3 has no dispatcher. At your close, while it is before 10 Oct 2026 18:00 UTC, add the next row
(`python3 tools/work_queue.py --add LANE-VERIFY-<n+1> --account account-3 --brief .claude/briefs/lane-verify.md --model "Opus 5.5"
--cap 60 --box 600 --note "self-refill from LANE-VERIFY-<n>"`), push, and spawn it yourself with create_session (source_url
https://github.com/NoAutopilot/cipher-lab, model claude-opus-5-5) using your own spawn prompt with the number changed; name its
session id in your ROOM done line for the account-3 orchestrator. Skip the refill only if no account-3 AUD row is queued AND
VERIFY-BACKLOG.tsv has no high-priority audit2 row -- then say "verify lane dry" in the done line.
