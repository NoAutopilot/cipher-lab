# LANE A2PUSH2: account-2 lane orchestrator, second incarnation (account-3 orchestrator, 3 Oct 2026 03:3x UTC)

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
below is spent or the window is rejected; then write "LANE A2PUSH2 handoff" in STATUS.md and one done ROOM line.

Backlog, in this order (the first incarnation closed 03:16 UTC 3 Oct with its own backlog spent; read its STATUS.md
"LANE A2PUSH handoff" first). Rows 1-4 have account-3 briefs already written and price-checked: claim them in
WORK-QUEUE.tsv (tools/work_queue.py) and spawn them as written.
0. FIRST (owner's priority, 3 Oct 03:4x): TX-BENCH, TX-ATLAS-B72, TX-DECODE, TX-SORTER (...-tx-*.md; TRANSCRIPTION.md),
   all four at once -- each has a fallback if its neighbour has not landed.
1. NV01-READ (.claude/briefs/runs/2026-10-03-acct3-nv01-read.md), 2. NV02-READ (...-nv02-read.md),
3. F36R-REREAD (...-f36r-reread.md), 4. BIRAGO-NUM4 (...-birago-num4.md).
5. Handoff "Open next steps": colbert26 canvases 50-51 (~4); na-raad-azie leaf 3 (~5); manteuffel key table -> key.tsv
   (~7, low value: Krauske 1893 printed -- check-solved first). Kaliningrad Russian tool (~12) only if 1-5 are spent.
6. Then the first incarnation's sources: tools/next_steps.py runnable rows, gaps_check --all "keep going" partials,
   needs-triage check-solved (Sonnet allowed), breadth specs (cap 3 each).
Every brief you write with an image step carries "vision calls: N x USD r [+ k reconciliation] = X" and passes
`python3 tools/brief_price_check.py <brief>` (exit 0) before you spawn it (RETRO-2026-10-03-acct3 P2).
Ledger each worker once, yourself (CLAUDE.md Improvement loop: the running account ledgers a cross-account job).

Excluded (other owners): armstrong-madison-1808 (owner's own sprint), debosnys-1883 and anything private,
nevers-birago-fr3251-1572 and birago-* (account-3 orchestrator's live campaign, except rows 3-4 above), mercy/espagnol142 (hold), any target with a
live ROOM claim younger than 6 h. Never take an account-4 target with a live claim.

Each worker brief (file `.claude/briefs/runs/2026-10-0X-acct2-<role>.md`, fetch before write, Usage section of
CLAUDE.md applies): one target, one step, cap $3-6 and a box sized per unit (Usage 6), the intake gate
(`tools/intake_gate_check.py <target>` pasted) before any deep work, matched control (rule 3), grades (rule 4),
gaps_check before the done line, rule 10 wording, "report what was found and where it was not found; do not
classify novelty". Any reading that reaches a verifier-worthy state: spawn a separate verifier session (CLAUDE.md
verifier template). A result worth the owner's attention (judge PASS with control, a key opening a letter, a
found-solved): one ROOM `flag` line addressed to the account-3 orchestrator, with an English gist of what it says.
Never call AskUserQuestion; never print credentials; never name the owner; never send email; never force-push.
