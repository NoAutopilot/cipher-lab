# Retrospective, account-4 lineage, 1 Oct 2026 23:25 UTC to 2 Oct 2026 06:10 UTC

Written 2 Oct 2026 06:1x UTC (clock read) by RETRO-account4-1 (account-4), session_01Xznr5oo8hFLzbWNPHd2w7V,
brief `.claude/briefs/retrospective.md` plus the parent's prompt (four numbered questions). Window: every LEDGER.md
row with `account-4` in its account cell (75 rows, two parents session_01SEzoee67SivPooFpTkxMme and
session_01SnKHiQk7k7VPDGhfcPeiVV), STATUS.md "Parent handoff (account-4 ...)" check-ins 1-7 and parent 2's check-in 1,
ROOM.md lines with `(account-4)` in the role field (69 claim lines), the 16 generic briefs under
`.claude/briefs/runs/2026-10-0[12]-account4-*.md`, and the transcripts of the two hung sessions (list_events, kinds
control_request/user). Read with scripts (scratchpad `ledger.py`, `caps.py`), not by eye. Disk only, 0 outside
requests; the two list_events calls are platform reads of our own sessions. Nothing is applied here.

The last retrospective on file is RETRO-2026-09-27 (retro x); this window alone is 75 rows and USD 458, about six
times the "12 rows or USD 60" trigger -- the trigger was not fired by either account-4 parent (recommendation 1).

## 1. Numbers

**75 rows, USD 457.76 of worker usage.** By outcome: D 30 (USD 160.4), D- 34 (239.3), N 7 (29.9), X 3 (8.6), F 1
(19.6). 71 rows actually ran; 63 of those carry a cap in their claim line, ledger row or the parent's spawn list.

Cost per delivered result by role prefix ("delivered" = the step's own result landed: a target moved, a
control-backed negative, a filed row or a tool; N and X rows count as not delivered):

| prefix | rows | USD | delivered | USD per delivered |
|---|---|---|---|---|
| GAPS | 29 | 213.68 | 28 | 7.63 |
| WEBCHECK | 16 | 70.18 | 15 | 4.68 |
| LIKELY | 8 | 54.78 | 4 | 13.70 |
| OPEN | 3 | 14.99 | 3 | 5.00 |
| SPLIT | 2 | 12.81 | 1 | 12.81 |
| CLOSER | 4 | 11.63 | 4 | 2.91 |
| CHECK | 1 | 9.79 | 1 | 9.79 |
| SHORTLIST | 1 | 9.78 | 1 | 9.78 |
| LAU | 2 | 20.07 | 1 | 20.07 |
| one-offs (BER, BLZ x2, RIK, HEL, SPEC, OLD, D4450, HUN) | 9 | 40.5 | 7 | 5.8 |

**Share that stopped within cap: 23 of 63 (37%); 40 of 63 over cap (63%).** Median cost/cap ratio 1.10, p75 1.50,
max 3.26 (GAPS-fr4715-vieuville-pool, F). Parent 2's wave 1 (05:17-05:34 UTC): 11 workers, caps USD 52, actual
82.35, 9 of 11 over. The caps were written at Sonnet-era per-job figures; the rows give the Fable floor directly:

| job shape | n | min | p25 | median | p75 | max | over cap | median cap written |
|---|---|---|---|---|---|---|---|---|
| disk-only (no host, no vision; CLOSER's platform-only jobs included at 2.70-3.18) | 22 | 2.70 | 4.49 | 5.49 | 6.65 | 9.78 | 13/19 | 4 |
| one host (web/blog check, one archive.org or DECODE fetch, a LOCAL-QUEUE probe) | 33 | 3.71 | 4.63 | 5.07 | 5.59 | 9.79 | 20/32 | 5 |
| vision (two blind passes + reconcile, a known-answer image read) | 16 | 4.23 | 7.18 | 8.20 | 12.05 | 19.58 | 7/12 | 7.5 |

Two clean calibration pairs inside the window: WEBCHECK at cap 3 (8 rows, mean 4.61, 8 of 8 over) against the same
brief at cap 5 after check-in 1 raised it (7 rows, mean 4.76, 2 of 7 over) -- the job's cost did not move when the
cap did, so the cap was simply wrong, not the workers; and the five CLOSER/GAPS4-janssens-shaped minimal jobs at
2.70-3.71 show the Fable session floor (room.py --start, brief read, one small push) is about USD 2.7, not the
USD 1.3 the 26 Sept parent-worker rule in STATUS.md measured on Sonnet. A disk-only Fable step costs about 2x and a
vision step about 1.5-3.5 per subagent call on top (GAPS-fr4715: five Fable vision calls of 24 crops each, 19.58;
GAPS3-na-suriname: five calls, 7.65; GAPS-intercepted-royalist: two calls plus a djvu read, 7.58).

## 2. Over-claims and non-tests caught before the person saw them

- **found-solved** fr3625-lauriere-1593 (WEBCHECK, 23:41 UTC 1 Oct: cyphersolver issue 13 / PR 15, read with key
  no.57) -- caught by the gate step itself; but LAU-U3U4 (15.57, already running) and LAU-KEYSWAP (4.50, spawned
  00:18, after the 23:40 flag) ran anyway; KEYSWAP was a non-test by construction (key57.tsv has no alphabet row).
  USD 4.50 spent on a target already flagged found-solved in ROOM.md.
- **Non-tests logged as non-tests, not negatives** (rule 3 held): HEL-T2 (both controls 0.10 vs gate 0.6, target
  not run); LIKELY-5 fr3151-noailles (positive control fails its own gate 0/5 seeds, second attempt -> "untestable by
  this method"); LIKELY-4 decode-1162 (premise wrong: sibling 1168 holds no key); LIKELY-7 roell (inv.164 is a code
  table of a different decade); LIKELY-8's de16 judge voided on Groen's own prose before its PASS could be used.
- **Judge FAILs read correctly as "cannot decide"**: na-schonenberg (leaf's own gloss FAILs at -1.346 beside the
  candidate's -1.204); nevers-birago (near-miss -1.032 vs -0.905, shuffled-target 0/20) -- both `partial` with NEAR
  rows, neither "closed-negative" (rule 5 held).
- **Gate mis-parse flagged twice, fixed zero times**: `tools/intake_gate_check.py intercepted-royalist-1646` returns
  "offline-only (line 137) -- already terminal, nothing to gate", exit 0. Line 4 reads `- **Status:** partial ...`,
  which VERDICT_RE (`^[\s\-*>#]*\b(open|partial|...)`) cannot match because of the `Status:` label, so the scan runs
  on to line 137, a quotation of Bourdeau's status for the same shelfmark. LIKELY-9 flagged it (04:33), GAPS-
  intercepted-royalist flagged it again (05:31); a terminal verdict from a quoted line would let a deep-work worker
  skip the gate on any target whose NOTES.md quotes another project's status. Proposal 2.
- **A reading error caught one worker later**: GAPS-mornington (02:05) read Martin Vol.2 p.311 as the 21 Jun 1800
  letter; GAPS2-mornington (05:25) found two footnotes read as one, and that D623/24 is printed at No. XV pp.35-43.
- **mccormick-1999**: 18 claimed readings quoted, none taken as a decipherment (rule 10 held).

## 3. Did the top of the queue produce results?

**Likely-solves shortlist (SHORTLIST 9.78, then 8 LIKELY + 3 follow-on GAPS, about USD 100):**

| rank | target | outcome | why |
|---|---|---|---|
| 1 | fr4715-vieuville-pool | folder created, no.44 f.67r 95% clear French, 27 cipher tokens, 14 word-codes at slot class I, 0 values; GAPS-fr4715 F at 3.3x cap | moved a little; the pool's cipher content on that leaf is small, and the follow-on was priced per leaf, not per Fable vision call |
| 2 | ceppo-nevers-fr3251-1570s | **non-job** (3.75) | every folio the row names was already counted; NEAR.md's own "Why it left" table lists f.21v and f.87 as done -- SHORTLIST ranked without reading it |
| 3 | nevers-birago-fr3251-1572 | **moved**: printed key reads its witness leaf rank 1/201, z 4.53 -> 4.84 over three steps, Italian decode, judge near-miss; NEAR row added | the only shortlist row with a key on disk and an unread witness leaf |
| 4 | decode-1162 | **non-test** (3.79) | premise wrong: no key in 1168, no ciphertext on disk, transcription doc login-gated |
| 5 | fr3151-noailles-1558 | **non-test** (5.49) | alignment instrument fails its own positive control; second attempt, retired for this method |
| 6 | fr3986-90 | held, spawned 06:06 | -- |
| 7 | roell-vandedem-1809 | **non-test** (6.74) | inv.164 is digitised but is a one-part code of a different decade |
| 8 | jan-van-nassau 5549 | control-backed negative on the body under three keys; key confirmed on the postscript (0.842 vs 0.340) | a real result, no reading |
| 9 | intercepted-royalist-1646 | **moved** offline-only -> partial; key129 confirmed 32/65 rows against Evelyn; NEAR row added | Aymeloglu's key plus a printed clear text, the pool/known-key shape the selection rule names |
| 10 | fr4687-paleologue-nevers | blocked on LOCAL-QUEUE L33 (CHECK 9.79, 2x cap) | Ferrari 1999 is a 16-page essay in a 1999 catalogue on no cloud route |

Two of ten moved (3, 9), one created (1), one clean negative (8), three non-tests and one non-job (2, 4, 5, 7; USD
19.77 together), one blocked, one held. The three premise failures share one cause: the `head_start` cell asserted
a file or key on disk that nobody checked with `test -f` before spawning (Proposal 5).

**The 12 partials' Verdict steps (29 GAPS rows, USD 213.68):** every one of the 11 targets' gates passes; targets
that moved in substance: pro3055-clinton-1779 (2894 is now text-known at H via H-1649 fo.161; 315 figure pairs
transcribed; the 1761 Army List confirms 14/25 key lines -- GAPS3 fetched the 1761 printing when the step named
1778, half a non-test), na-janssens-java-1811 (leaf 188 keyed 76 -> 88/163, C 77 after regrades; judge flat FAIL),
na-schonenberg-1678-1716 (L19 address crib 15/16, seeded alignment 0.699 vs 0.301, Spanish sense C 115),
na-suriname-map-1781 (the plain plan 4.VEL 2038 and its legend crib found, 40 rows), mornington-1798 (two of three
letters located in print, text known C), rah-morillo-1817 (key_5186 C 90 / M 7 / U 0), matignon-mayenne-1586
(f143r opening aligns 468 vs shuffle max -67; Bourdeau's HEAD key carries no new value -- step closed), moray-
wood-1568 (Aymeloglu transcription on disk, S 119; the DECODE fetch spent its one login on relative URLs, 0 images),
vanbeuningen-dewitt-1657 (new shared tool key_order_test.py). Non-jobs inside the wave: SPLIT-matignon (5.63 N, 0 of
31 hits had an image on disk -- parent's error, same premise shape as Proposal 5), HUN-108B (skipped, correctly).
No reading cleared both its judge and the shuffled-target check, so no verifier was spawned (correct under rule 7).

**Wait-only at the window's end: 25 rows** (`tools/next_steps.py --wait-only`), of which 11 are account-4's own
partials (matignon, moray-wood, mornington, janssens, schonenberg, pollaky, pro3055, rah-morillo, spinelli,
vanbeuningen, wellington). None of the 14 account-4 target folders carries a "## While waiting" section after 29
GAPS workers rewrote their Verdict lines: the gaps-step brief never asks for it (Proposal 4). Per the retrospective
brief this is the first proposal's subject; it is Proposal 4 here only because the parent's four questions come
first in this file.

**NEAR.md review:** rows moved this window: nevers-birago-fr3251-1572 (added, 2 Oct 03:49, refreshed 05:25),
intercepted-royalist-1646 (added 05:31); rows that left: fr3625-lauriere-1593 (found-solved), ceppo-nevers (counted).
Six rows are over the 48-hour window and none is account-4's: antt-msliv0638-brochado-1712 (143 h), koehler-1944
(149 h), malsburg-hessen-1636 (134 h), fr2933-salviati-1525 (116 h), fr4715-montholon-1589 (110 h),
espagnol142-mercy-1648 (107 h) -- for the owner-account and account-3 parents, named here, not actioned.

## 4. The X rows

Three X rows, USD 8.63. BLZ-FR (2.41) was a correct stop at the intake gate (the brief should have carried the gate
output; fixed by WEBCHECK then BLZ-FR2). The other two are **one failure shape**, read from their transcripts:

- WEBCHECK-ormond-arran-1678 (first try, session_01WYFaBZMJFFu1EixG8WbuwQ): 00:14:12 first tool call prints
  `## HEAD (no branch)` and `HEAD detached from refs/heads/main`; 00:14:36 and 00:14:54 two git commands denied
  by the auto-mode classifier as "[Irreversible Local Destruction]"; 00:15:06 the third Bash call -- `tail -12
  ROOM.md` -- is turned into a human permission prompt ("3 consecutive actions were blocked. Please review the
  transcript before continuing"); nobody can answer in a create_session worker; archived 01:04. 0 cost, 50 minutes.
- GAPS3-na-schonenberg-1678-1716 (session_017Z5EZboi3jdB2qdt1PGG3y): 03:34:35 same `HEAD (no branch)`; `git pull`
  fails on divergent branches; two denials at 03:35:10 and 03:35:21; at 03:35:37 `git switch --detach origin/main`
  becomes the prompt; archived 04:24. USD 6.22 (the brief and 30 ROOM lines read, nothing pushed), 50 minutes.

What caused it. Platform: the container checkout comes up detached from main with local main diverged (every
worker's first output this window shows `HEAD (no branch)`; the other 15 of 17 sessions in the same waves survived
it because `tools/room.py --start` did the force-checkout for them), and auto mode's three-strike rule makes the
next call after three denials -- any call -- a human prompt. Brief: the session prompt opens "read the brief first",
so both workers ran `cat brief; git branch; git log` before `tools/room.py --start`, saw the odd git state, and
repaired it by hand with exactly the commands the classifier treats as destructive; nothing in the common tail says
a classifier denial is terminal in an unattended session, or that the repair belongs to room.py and never to the
worker. Detection: both sat until the parent's next scheduled check-in (50 min each); the CLOSER brief, which
already reads every finished session's status, does not look at live ones.

## Proposals (at most five; diffs; none applied here)

### Proposal 1 -- a classifier denial is terminal; the first action is the first sentence of the prompt (X rows: ormond-arran first try, GAPS3-na-schonenberg)

`.claude/briefs/README.md`, common tail, after the "First action: `tools/room.py --start` ..." sentence:

```diff
 > First action: `tools/room.py --start` (fetches, force-checks-out `main` onto `origin/main`, and refuses a
 > ROOM.md under 50 lines rather than a shrunk stub; replaces raw `git fetch`/`git reset` for this step,
 > RETRO-2026-09-24b -- the prose fix alone let the identical stale-clone/detached-HEAD failure recur at least
-> twice more the same day).
+> twice more the same day). The container normally starts with `HEAD (no branch)` and a diverged local main:
+> that is room.py --start's job, never yours -- no `git checkout`, `git switch`, `git reset`, `git pull` or
+> `git branch -f` by hand at any point. If the auto-mode classifier denies a command ("Irreversible Local
+> Destruction" or any other reason), do not re-issue it or a variant: in an unattended session the third
+> consecutive denial turns your next call -- any call, even `tail ROOM.md` -- into a human permission prompt
+> that nobody answers (2 Oct 2026: WEBCHECK-ormond-arran-1678 and GAPS3-na-schonenberg-1678-1716 each sat 50
+> minutes, USD 6.22 lost). After one denial: `python3 tools/room.py "<role>" "flag: classifier denied <what>;
+> stopping" --push` and stop.
```

`.claude/briefs/runs/2026-10-02-account4-gaps-step.md` (and likely-phase2.md, open-step.md, split-check.md,
webcheck.md, whose session prompts share the opening), the prompt template line:

```diff
-The session's prompt names the target, the Verdict step verbatim, the cap and the vision-call count.
+The session's prompt opens with `python3 tools/room.py --start` as its first sentence (before "read the
+brief"), then names the target, the Verdict step verbatim, the cap and the vision-call count.
```

`.claude/briefs/runs/2026-10-02-account4-closer.md`, after the per-id loop:

```diff
 If `archive_session` is refused for an id, leave the retitle and say so.
+Then `list_sessions` (mine, limit 40): any session titled `LIVE account-4 worker ...` whose `get_session` status
+reads REQUIRES_ACTION is a worker stuck at a permission prompt (2 Oct 2026, two cases, 50 minutes each): retitle
+it `HUNG <old title> (REQUIRES_ACTION at <clock time>)`, archive it, and name it in the done line so the parent
+re-spawns it in the same check-in rather than the next.
```

### Proposal 2 -- `tools/intake_gate_check.py` reads a labelled status line and only the head of the file (LIKELY-9 and GAPS-intercepted-royalist, both flagged line 137)

Usage 8a: the rule ("status vocabulary in the first lines of every NOTES.md", rule 5) was mis-read twice in one
window by the gate itself. Diff sketch, with the offline test the tool's docstring requires:

```diff
 VERDICT_RE = re.compile(
-    r'^[\s\-*>#]*\b(open|partial|blocked|found-solved|solved|closed-negative|offline-only)\b',
+    r'^[\s\-*>#]*(?:\**\s*status\s*:?\**\s*)?\b(open|partial|blocked|found-solved|solved|closed-negative|offline-only)\b',
     re.IGNORECASE,
 )
+# Rule 5 puts the status word in the first lines of NOTES.md; a status word matched further down is a
+# quotation (intercepted-royalist-1646 line 137 quotes Bourdeau's `offline-only` for the same shelfmark while
+# line 4 reads `- **Status:** partial`; LIKELY-9 and GAPS-intercepted-royalist, 2 Oct 2026). Scan at most the
+# first STATUS_HEAD_LINES lines for the verdict; past that, report "no status line in the head" and exit 1.
+STATUS_HEAD_LINES = 12
```

Test: `tools/tests/test_intake_gate_check.py` gains a fixture whose line 4 is `- **Status:** partial (...)` and
whose line 40 is `offline-only (Bourdeau)`: the gate must report `partial (line 4)`, never `offline-only`; and a
fixture with no status word in the first 12 lines must exit 1 naming that, not take line 137. Must NOT block: the
existing terminal fixtures (`blocked`, `solved`, `closed-negative`, `offline-only` on line 1).

### Proposal 3 -- Fable caps from the measured floor, per job shape (40 of 63 over cap; parent 2 wave 1: 9 of 11; WEBCHECK cap 3 -> 5)

`.claude/briefs/README.md`, "Sizing a unit-loop brief's box" paragraph, append:

```diff
 ...not only after aggregate elapsed time crosses 80%, which one large unit can jump past in a single step.
+**Fable floor (2 Oct 2026, RETRO-2026-10-02-account4, 71 Fable 5.1 workers):** a Fable session's fixed cost
+(room.py --start, brief and 30 ROOM lines, one small push) is about USD 2.7, twice the Sonnet figure of 26 Sept.
+Measured medians (p75): disk-only step 5.5 (6.7); one-host step (a web/blog check, one archive.org or DECODE
+fetch) 5.1 (5.6); a vision step 8.2 (12.1), about 1.5-3.5 per Fable subagent vision call. A Fable cap is written
+at the p75 of its shape, never below USD 5 for any job that reads a brief, plus 2.5 per planned vision call;
+raising WEBCHECK from 3 to 5 moved its over-cap rate from 8 of 8 to 2 of 7 at the same mean cost (4.6-4.8).
```

`.claude/briefs/runs/2026-10-02-account4-gaps-step.md` header:

```diff
-Role field for ROOM.md lines: `GAPS-<target> (account-4)`. Model: Fable 5.1 (Opus 5.5 if Fable fails). Box: 60 minutes.
+Role field for ROOM.md lines: `GAPS-<target> (account-4)`. Model: Fable 5.1 (Opus 5.5 if Fable fails). Box: 60 minutes.
+Cap: never under USD 5; USD 7 for a one-host step; USD 7 + 2.5 per planned vision call for a crop pass (README
+"Fable floor"); the prompt states the planned call count beside the cap.
```

(The same two lines go into likely-phase2.md and open-step.md. GAPS-fr4715's F at 3.3x of a USD 6 cap for five
vision calls prices at 7 + 12.5 = 19.5 under this rule, i.e. the actual 19.58.)

### Proposal 4 -- a GAPS step leaves a "## While waiting" section and a clean `--wait-only` line (25 wait-only rows, 11 of them account-4's; 0 of 14 folders have the section)

`.claude/briefs/runs/2026-10-02-account4-gaps-step.md`, step 4:

```diff
 4. Update the "## Remaining gaps" section IN PLACE (...), then run
    `python3 tools/gaps_check.py <target>` and paste its output.
+   If the rewritten Verdict line is "blocked on <ASKS/LOCAL-QUEUE row>" or names a person, also write or refresh
+   "## While waiting" with the one action that depends on nobody (WAIT-CHECK, 27 Sept 2026), then run
+   `python3 tools/next_steps.py --wait-only | grep <target>` and paste the (empty) result; a non-empty result is
+   a brief failure, not a done line.
```

### Proposal 5 -- a premise check before a LIKELY/SPLIT session is spawned (LIKELY-2, -4, -7 and SPLIT-matignon: USD 19.77 on rows whose `head_start` named material not on disk)

Usage 8a (a rule broken more than twice): new `tools/premise_check.py <slug> [--key PATH] [--needs-images]
[--row-text TEXT]`, offline test in `tools/tests/`, exit 1 naming the first failure: (a) `ciphers/<slug>/` exists
and `ciphertext.txt` is non-empty when the step decodes; (b) every `keys/...` or `.tsv` path the row's `head_start`
cell names exists (LIKELY-4: "sibling 1168 key" named a file that does not exist); (c) with `--needs-images`,
`images/manifest.json` lists the leaf the step names (SPLIT-matignon: 0 of 31 hits had an image); (d) the slug is
not in NEAR.md's "Why it left" table (LIKELY-2: f.21v and f.87 were already counted there). Must NOT block: a
`new` row with no folder (likely-phase2 step 2 creates it). Brief diff, likely-phase2.md after the first paragraph
and split-check.md's prompt template:

```diff
+Before `create_session`, the parent runs `python3 tools/premise_check.py <slug> --row-text "<head_start cell>"`
+and pastes its output in the prompt; a nonzero exit means no session (the row goes back to SHORTLIST with the
+failure named). SHORTLIST itself runs it on every row it ranks.
```

## Recommendations to the parent (goals, spend, the person's asks -- not applied, not proposals)

1. **Fire the retrospective on its trigger.** This one covers 75 rows and USD 458, six triggers' worth; the lessons
   in Proposals 1 and 3 were visible by check-in 2 (00:11 UTC, 11 rows, USD 62.6, two over-cap patterns already).
2. **Stop spawning on a found-solved target the same check-in the flag lands.** LAU-KEYSWAP (USD 4.50) was spawned
   38 minutes after WEBCHECK's found-solved line; the parent's own check-in 2 notes it. A one-line parent rule, not
   a worker rule.
3. **Price a GAPS follow-on per Fable vision call before re-spawning it** (GAPS-fr4715 F, 3.3x): the held fr4715
   no.37 f.60 is already "priced per pass next time" in check-in 1 -- Proposal 3's formula gives the number.
4. **Caps total per wave against the rate window**: parent 2's wave 1 was briefed at USD 52 and cost 82; wave 2
   (06:06) is briefed at 70, which under Proposal 3's floors reads nearer 100. BUDGETS.md's scaling rule decides,
   not this file.
5. **Six NEAR rows over 48 h belong to other accounts** (section 3); hand the list to the owner-account and
   account-3 parents in ROOM.md rather than acting on them from account-4.
