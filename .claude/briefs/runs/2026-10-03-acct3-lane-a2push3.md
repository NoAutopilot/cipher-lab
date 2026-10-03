# LANE A2PUSH3: account-2 lane orchestrator, third incarnation (account-3 orchestrator, 3 Oct 2026; start when account 2 resets, ~13:30 UTC)

Owner's directive, 2 Oct 2026 ~20:20 UTC: account 2 has unused usage before its reset (about this time 3 Oct);
"push as far and hard as we want". You are a LANE ORCHESTRATOR on account 2 (CLAUDE.md "Operating model"), Opus 5.5.
You write job briefs and spawn workers yourself with create_session on account 2 (source_url
https://github.com/NoAutopilot/cipher-lab, model claude-opus-5-5; never below Opus 5.5). You do no solving yourself.

Pace: keep about 6 workers live at once. Before each spawn read get_session on yourself: five_hour
allowed_warning or rejected on either type -> stop spawning, post a ROOM flag, let live workers finish. A seven_day
allowed_warning alone does not stop you (BUDGETS.md amendment 27 Sept). Re-arm yourself with send_later every
15 min (owner, 2 Oct 20:4x: accounts sat idle between hourly firings; most jobs finish in 10-20 min, so a slot
must be refilled within ~15 min of a done line); each wake: read ROOM since your last line, ledger finished workers in LEDGER.md (cost from get_session on
each worker), update the target's PROGRESS.tsv row only if one exists, spawn into free slots. Stop when the backlog
below is spent or the window is rejected; then write "LANE A2PUSH3 handoff" in STATUS.md and one done ROOM line.

Backlog, in this order. Read STATUS.md "LANE A2PUSH2 handoff" (your previous incarnation, interrupted 05:30 UTC by the usage limit)
and ROOM.md since 3 Oct 09:00 UTC first. LANE-A1 (account 1) runs the Birago / fr3416 / Dinteville follow-ups: skip any target
with a live claim under 6 h from any account. Owner, 3 Oct 09:2x UTC: do NOT resume the interrupted A2-* work (colbert26,
harley-287, na-raad-azie, fr2980-gramont, A2-DIN4) -- their NOTES carry "Interrupted" sections; leave them parked.
WORK-QUEUE.tsv rows with status `queued` first. Then, writing each brief from the target's NOTES.md (tools/tool_shelf.py first;
TRANSCRIPTION.md for any transcription step):
1. Nevers vein, new letters: NEVERS-VEIN.tsv NV-04 (fr.3984 f.198, Sillery 1593, key no.40: locate the leaf) and NV-05
   (fr.15575/15576 syllabic numerical pool, keys no.31/54): check-solved + premise check (Cabinet Noir grep) + intake gate, then
   a first test with a known-answer control on a glossed sibling, as NV01/NV02 did (~6-12 each).
2. Dinteville siblings: fr.3623 f.23r (Gallica f55) is a Dinteville cipher slip (DIN-3623, 3 Oct) -- if no live claim, first test
   with the print-built key (f130/print key) and its controls; it is the natural third letter for that key (~6).
3. Transcription benchmark: TX-BENCH could not build colbert26 or Mercy items (no raw passes / no independent answer); add
   benchmark items from targets with a period gloss and two blind passes on disk (fr3621 f.128 vs the 1882 print, fr3416 glossed
   siblings, fr3993 f.71-72 clerk gloss), and score err_true per hand (TRANSCRIPTION.md rows 1 and 8) (~5).
4. fr17 corpus (account 4, 3 Oct): re-judge 1620s-1640s French readings judged with fr16 (grep NOTES for "fr16" with dates
   1620-1650); report PASS/FAIL changes with the real-prose false-negative rate per fold (CLAUDE.md rule 3) (~4).
5. Then tools/next_steps.py runnable rows (not the parked ones), needs-triage check-solved (Sonnet allowed for that role only),
   breadth specs (cap 3).
Ledger each worker once, yourself. One ROOM flag to the account-3 orchestrator for any result worth the owner's attention, with a
one-line English gist marked as interpretation.

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
Usage register: none needed (owner reads bars himself). Never call AskUserQuestion; never print credentials; never name the owner; never send email; never force-push.
