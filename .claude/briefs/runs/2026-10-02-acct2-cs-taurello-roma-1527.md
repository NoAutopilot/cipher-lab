# CS-TAURELLO-ROMA (taurello-roma-1527): check-solved with Premise check, to clear the intake gate (2 Oct 2026, written by LANE-A2PUSH, account 2)

Model: Sonnet 5.5 (claude-sonnet-5-5; the owner allows Sonnet for this role only). Cap USD 4, box 45 min from your claim;
stop before any step that would cross 80% of either. One target, one job: stop when it is met.

Why: NEXT-STEPS.tsv marks taurello-roma-1527 `needs-triage`: `python3 tools/intake_gate_check.py taurello-roma-1527` exits nonzero (an
open/blocked status line without the edition actually read and the pages or full-text search, and/or no Web and blog
check or Premise check section). Nothing deep may be briefed on it until the gate passes or the status honestly reads blocked.

1. `python3 tools/room.py --start` (if it fails to push from a detached HEAD: `git push origin HEAD:main; git checkout -B main HEAD`);
   read the last 30 ROOM.md lines; if a live claim (<6 h, no done line) covers taurello-roma-1527, stop and post one line saying so.
   Otherwise `date -u`, then claim: `python3 tools/room.py "CS-TAURELLO-ROMA (account 2, LANE-A2PUSH)" 'claim: taurello-roma-1527 -- check-solved + premise check; cap USD 4, box ends <HH:MM> UTC'`.
2. Read ciphers/taurello-roma-1527/NOTES.md in full and `.claude/briefs/check-solved.md` in full (the six sources, the required
   "## Web and blog check (<worker>, <date>)" section, the "## Premise check" adversarial pass, the citation line under
   the status word, the HTRC fallback for an unreachable calendar). Paste the gate's current output first.
3. Do the check yourself, sequentially (no Workflow; at most 2 subagents for independent searches): the standard edition
   / calendar for the sender actually opened and searched (page numbers or full-text phrase), the web and blog check,
   DECODE listing (login-free tools/decode_list.py), the two solver repositories grepped for the target (shallow clone,
   grep only; Aymeloglu: cite, never copy code), and the Premise check. Good-citizen rule: one request at a time per host,
   >=1.5 s apart, stop on 403/429/challenge; API keys per CLAUDE.md (Google Books `&country=US`), never printed.
4. Write the verdict: status word alone on line 1 (open / blocked / found-solved / ...), the citation sentence on line 2
   naming what THIS worker read; if you could not open the edition, the honest word is `blocked` with what blocked it.
   `python3 tools/intake_gate_check.py taurello-roma-1527` pasted after; exit 0 for open, or a blocked line that says why.
   A found-solved: one ROOM `flag` line addressed to the account-3 orchestrator with the English gist and the citation.
5. Report what was found and where it was not found; do not classify novelty, never new/first/solved for our work.
6. Commit by explicit path; `python3 tools/file_shrink_guard.py ciphers/taurello-roma-1527/NOTES.md`; `python3 tools/room.py --push <paths>`;
   done line addressed "for LANE-A2PUSH (account 2)": verdict word, edition read, gate exit code, request count per host
   (cost: the orchestrator reads get_session). Do not edit status.json, STATUS.md or NEAR.md. Never call AskUserQuestion.

