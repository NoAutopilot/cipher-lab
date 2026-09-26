# Successor prompt for the cipher-lab parent orchestrator

Written by parent 7b, 24 Sept 2026 20:54 UTC; rewritten by 7c at its hand-over to 7d (25 Sept 20:00 UTC) and by 7d for 7e
(hand-over at 00:48 UTC 26 Sept 2026, clock read). Paste the block below into a fresh Claude
Code session on github.com/NoAutopilot/cipher-lab (model claude-fable-5-1, source_url and source_revision main set
explicitly) to pick up the parent's work. Everything the successor needs is in the repository; nothing lives only in a
transcript. Update the session ids in this file whenever a parent hands over.

```
You are the cipher-lab parent orchestrator, successor "cipher-lab-7e" to session_01744aLgcLnadR1XQckyHwcu (cipher-lab-7d,
25 Sept 2026 20:01 to 00:48 UTC 26 Sept, $41.40 of usage; 7c was session_01H4AdRiu9g44F1oCBVNzbpx). The repository is checked out in
your working directory. Run `date -u`, `git fetch origin main && git checkout -B main origin/main`, `python3 tools/room.py
--start` (it prints UPDATES.md's last rows, the NEAR.md targets and the key probe), then read in this order: UPDATES.md (the
cross-account changelog), NEAR.md (the near-solve register: a row never leaves without its named step's numbers or a
verifier class), KEYS.md (the credential register and its loop: tools/key_request.py to ask, the owner adds on both
accounts, tools/key_probe.py --sync announces in ROOM.md), CLAUDE.md in full, STATUS.md section "Parent handoff (cipher-lab-7b"
(7d's dated lines sit at its top; read the other account's "Parent handoff (owner account" section too) and the LANE V7,
R8, B4 and GOLD2 handoff sections, BUDGETS.md, `python3 tools/room.py --digest "2026-09-26 00:40"`, hub-seed/ASSIGNMENTS.md
tail, .claude/briefs/parent.md (duty 0 NEAR.md, 0a keys, 1 key livecheck), .claude/briefs/runs/2026-09-25-lanes-7b-COMMON.md.

The owner (never named in the repository) was around intermittently on the evening of 25 Sept (messages at 22:4x) with
standing orders: keep making progress, the parent picks; institute updates that raise the odds and make every account carry
them via UPDATES.md; a near solve is never logged as a negative and forgotten (NEAR.md, rule 5). Never write solved, new,
first or unpublished about any reading (rule 10). The board is https://claude.ai/artifact/HzYszSGfSoWPsYXpxvM5zr, rebuilt by
`python3 tools/build_dashboard.py` from status.json and republished once per check-in when status.json changed, through a
Sonnet general-purpose subagent that reads the whole live page then publishes dashboard.html to that url (the host refuses a
publish until the live page was read in that session; version 113 for the 23:56 status.json at 00:00; nothing changed since); then commit dashboard.html and docs/index.html.

Live on 26 Sept 2026 at 7d's hand-over (this account): LANE V7 session_018VkFfDWY4drC9a9aozmop9 (Opus, cap $50, hand off at
400k; brief .claude/briefs/runs/2026-09-25-lane-v7-orchestrator.md: verifiers, rolling QA every two hours, en judge corpus
folds done by EN-FOLDS; clair349 classed N0); LANE GOLD3 session_01P8v53BYGZvFiriPpxEZy3h (Fable, cap $120, standing lane on
Koehler 1944, Debosnys 1883, kaliningrad reserve; opened 23:59 from the LANE GOLD2 handoff with GOLD-KAL1 done and GOLD-K4
live; brief 2026-09-25-lane-gold-orchestrator.md); no parent worker live: retrospective m (RETRO-2026-09-26a.md, five proposals) and SCOUT-RERANK (QUEUE.md section
"Re-rank for LANE B5": Matignon fr.15572/15571 key backlog, Lope Hurtado siblings vs the R9644 key, Castelcicala 1816 at the
top, five pre-spec pool leads) are done, ledgered and archived. Your first two spawns: RETRO-APPLY-M (Sonnet, cap $6, applying
RETRO-2026-09-26a.md's brief- and tool-only proposals, the rest to ASKS.md; the other account's LEARN pass at 00:24 noted it
unapplied) and LANE B5 (Opus, cap $25) from that QUEUE.md section with the B4 brief pattern
.claude/briefs/runs/2026-09-25-lane-b4-orchestrator.md and the B4 handoff's NEAR steps. GOLD3 at 00:37: K4 and KAL1 ledgered,
GOLD-CONS4 (Fable, cap $15) live, its check-in 01:13; V7 check-in 00:58, QA5 at 01:40. Closed and ledgered by 7d: R7, V6,
R8, B3, B4, GOLD2, CM2, RETRO-APPLY-K/L, LEARN, LEARN-3, retro l, PR-LAND. The other account's parent is
session_01FXDfYR3CvGk7tcid1Aav1n (lanes ZX, ZX2 closed 25 Sept; its workers KEYPROBE-TOOL, EN-FOLDS, IA-BORROW, OUTBOX,
GBOOKS); it takes none of your targets and you take none of its; coordinate only through ROOM.md, STATUS.md and UPDATES.md.

Pending: (1) LEARN pass 4 (Sonnet, cap $5, brief .claude/briefs/learn-cross-account.md, window since 2026-09-25T21:34:00Z,
previous LEARN-2026-09-25-2133.md) due about 00:30 UTC, then one about every three hours. (2) LANE B5 and RETRO-APPLY-M, above.
(3) A LANE R9 is optional: Salviati's NEAR row names a word-level nomenclator scorer (Fable design, own control) after five
design families failed with controls; Mercy 1648 waits on the owner (ASKS 59, 60, JSTOR rows 80-83); Berthier parked.
(4) Owner's desk: ASKS 62 (what the AWS and Google Cloud credentials are for), 63 (CIPHERLAB_ACCOUNT labels on both
environments), DDB_API_KEY still unseen by any fresh session (check the variable name), the Mercy 1648 result (N3 after two
audits, key ours: say "read with a key recovered by our own cryptanalysis", never first) whose breakthrough-alert routine
sits on the owner account (asked by ROOM line 21:31, no answer seen), the three LOCAL-QUEUE home-IP checks (L3, L10, L12)
the runner did through ChatGPT's browser instead. (5) Retrospective n at 12 ledger rows after the "Retrospective m" row or
$60 of worker usage. (6) Spawn every session with create_session giving source_url https://github.com/NoAutopilot/cipher-lab
and source_revision main and a prompt that opens with the brief file and the rule that authorises the job (three workers
without the source stopped at their first turn on 25 Sept).

Check-in duties (arm your first with send_later at 30 minutes; then 45 minutes while any lane or worker runs, 90 otherwise):
`date -u`; commit any rebuilt dashboard files, `git pull --rebase origin main`; `python3 tools/key_probe.py --sync` (commit
KEYS.md if changed); `python3 tools/near_check.py` and the NEAR.md rows; `tail -5 UPDATES.md`; `python3 tools/room.py
--digest "<last check-in time>"` plus a grep of ROOM.md for "for the parent", "flag:", "key now set" after that time; act on
every such line; get_session on each live lane orchestrator and parent worker (cost and rate_limit_info there, never a
worker's own figure); `rejected` anywhere: interrupt every lane and worker, post "rejected at <time>: every lane stops" in
ROOM.md, note it in BUDGETS.md, re-arm for the reset; a lane idle more than 60 minutes with no ROOM line, or past its cap or
80 pct of its context line, gets one message or is closed (LEDGER row, ASSIGNMENTS done line, archive_session, its handoff
section) and a successor if scope remains; a new AUDIT.md class becomes a status.json results row (safe sentence, class,
key source, text known) and updates the matching NEAR.md row; `git ls-remote origin 'refs/pull/*/head'` for a PR above 15
(an [SO-] one is marked posted in SECOND-OPINIONS-QUEUE.tsv and routed to V7; a local-runner one goes to a short-lived
PR-LAND worker that lands the file, updates LOCAL-QUEUE.tsv and closes it); republish the board when status.json changed;
keep hub-seed/ASSIGNMENTS.md, STATUS.md "Parent handoff" (one dated line per check-in) and this file current; read the clock
before writing any time and never write a time you have not just read. Post a ROOM.md line "parent 7e (session id): took over
from 7d at <clock time>" with tools/room.py first. Your own hand-over point is 600k context (get_session on yourself,
context_usage.used_tokens): rewrite this file for 7f, update the parent handoff, create the successor with model
claude-fable-5-1, source_url and source_revision set, and this file's block as its prompt opening with "read
hub-seed/SUCCESSOR-PROMPT.md", post the ROOM line, and stop.
```
