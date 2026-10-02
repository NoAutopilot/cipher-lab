# LANE A2PUSH: account-2 lane orchestrator, backlog push (account-3 orchestrator, 2 Oct 2026)

Owner's directive, 2 Oct 2026 ~20:20 UTC: account 2 has unused usage before its reset (about this time 3 Oct);
"push as far and hard as we want". You are a LANE ORCHESTRATOR on account 2 (CLAUDE.md "Operating model"), Opus 5.5.
You write job briefs and spawn workers yourself with create_session on account 2 (source_url
https://github.com/NoAutopilot/cipher-lab, model claude-opus-5-5; never below Opus 5.5). You do no solving yourself.

Pace: keep about 6 workers live at once. Before each spawn read get_session on yourself: five_hour
allowed_warning or rejected on either type -> stop spawning, post a ROOM flag, let live workers finish. A seven_day
allowed_warning alone does not stop you (BUDGETS.md amendment 27 Sept). Re-arm yourself with send_later every
15 min (owner, 2 Oct 20:4x: account 2 sat idle between hourly firings; most jobs finish in 10-20 min, so a slot
must be refilled within ~15 min of a done line); each wake: read ROOM since your last line, ledger finished workers in LEDGER.md (cost from get_session on
each worker), update the target's PROGRESS.tsv row only if one exists, spawn into free slots. Stop when the backlog
below is spent or the window is rejected; then write "LANE A2PUSH handoff" in STATUS.md and one done ROOM line.

Backlog (pick in order of expected value = P(step moves it) x value / cost, CLAUDE.md Pipeline 3):
1. `python3 tools/next_steps.py` then NEXT-STEPS.tsv rows with blocker `runnable` (and `needs-key`/`needs-edition`
   rows whose next step names a concrete disk/API action), plus `python3 tools/gaps_check.py --all` partials whose
   Verdict is "keep going" with a named cheapest next step and cost.
2. `needs-triage` rows: one check-solved worker (with the Premise check section, .claude/briefs/check-solved.md)
   per target, Sonnet allowed for this role only per the owner, else Opus 5.5.
3. Breadth: specs/*.json whose first cheap test is unrun (CLAUDE.md Pipeline 3a, cap $3 each).

Excluded (other owners): armstrong-madison-1808 (owner's own sprint), debosnys-1883 and anything private,
nevers-birago-fr3251-1572 (account-3 orchestrator's live campaign), mercy/espagnol142 (hold), any target with a
live ROOM claim younger than 6 h. Never take an account-4 target with a live claim.

Each worker brief (file `.claude/briefs/runs/2026-10-0X-acct2-<role>.md`, fetch before write, Usage section of
CLAUDE.md applies): one target, one step, cap $3-6 and a box sized per unit (Usage 6), the intake gate
(`tools/intake_gate_check.py <target>` pasted) before any deep work, matched control (rule 3), grades (rule 4),
gaps_check before the done line, rule 10 wording, "report what was found and where it was not found; do not
classify novelty". Any reading that reaches a verifier-worthy state: spawn a separate verifier session (CLAUDE.md
verifier template). A result worth the owner's attention (judge PASS with control, a key opening a letter, a
found-solved): one ROOM `flag` line addressed to the account-3 orchestrator, with an English gist of what it says.
Never call AskUserQuestion; never print credentials; never name the owner; never send email; never force-push.
