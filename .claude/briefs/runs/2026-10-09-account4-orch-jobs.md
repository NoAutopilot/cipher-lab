# Orchestrator (account-4) jobs, 9 Oct 2026 05:2x UTC -- written by session_013CM4Sw1JBAhc5a2KspaERr at the takeover check-in

Common rules: the common tail of `.claude/briefs/README.md` applies. First commands: `git fetch origin && git checkout -B main origin/main`,
`python3 tools/room.py --start`, `date -u`, a ROOM claim line naming the job id, cap and box end, addressed "for orchestrator (account-4)".
Opus 5.5 or Fable only. Stop at the cap or at 80% of the box. Never AskUserQuestion. Never print credentials. Done line:
`done (<start>-<end> UTC by date -u, brief met|stopped at cap): <result, commit>` "for orchestrator (account-4)", then a five-line report.
Push with `python3 tools/restricted_guard.py --outgoing` first, then `git add <paths> && git commit && git push origin HEAD:main`.

### BERGH-PUB (account-1, the owner account; Opus 5.5; cap 4; box 45 min)
Publish the Bergh 1572 sign sorter so the owner can open it (a page published from account 4 is private to account 4, ASKS 145; the
owner account's pages open for him). Steps, in order:
1. `CIPHERLAB_ACCOUNT=owner python3 tools/sorter_preflight.py ciphers/wvo-11106-bergh-1572/sorter/bergh_sorter.html --expect-owner-account`
   must print `preflight: PASS` (on account 4 at 05:0x UTC it passed every check but the account one: template marker 2026-10-09.3, 157
   focus tiles all answerable, 830 tiles on 22 cipher lines, colour check pass). If a check other than `account` fails, stop and say so.
2. Eye `ciphers/wvo-11106-bergh-1572/sorter/bergh_sorter.preflight.png` (the orchestrator eyed it 05:1x: every red box sits on a cipher
   sign of its own line strip; the `fragment` tiles are small strokes, correct for that pile). Then open the page headless (the test in
   `tools/sign_sorter/run_all.sh` or `tools/sign_sorter/test_qa.js` against this page) and confirm three random tiles sit on a cipher sign of
   the right line and "Fix the cut" responds (parent.md "Machine first" item 6).
3. Publish with the Artifact tool: `file_path` the html, `icon` "grid", `description` "Bergh 1572 (WVO 11106) sign sorter: 830 tiles, 84
   piles, 157 questions first", `capabilities: {"db": {}}` (without db the owner's moves stay in his browser). Paste the URL into
   `ciphers/wvo-11106-bergh-1572/NOTES.md` under "BERGH-SORT (9 Oct 2026)" and into HUMAN-TX-ASKS.tsv if the target has a row.
4. One ASKS.md row, status `desk`, self-contained per parent.md 3b: ONE link (the URL), ONE action ("open on your phone or desktop, answer
   the 157 'Check these first' questions in the Taken-out tray first, then clean any pile you like; nothing to send back -- your moves save
   to the page"), time 15-30 min. If `python3 tools/desk_check.py --cap 5` then says the desk is over five, demote the oldest `desk` row
   without owner action to `backlog` and say which.
5. ROOM done line with the URL, "for orchestrator (account-4)".

### SORTER-RERENDER-A3 (account-3; Opus 5.5; cap 6; box 90 min) -- runs only when account 3 is back
Every owner-facing sorter published from account 3 is on an older template and shows the iPhone strip bug (owner, 9 Oct 02:00, Harley 287):
re-render each on the current template (marker 2026-10-09.3) with `tools/sorter_rerender.py <OLD.html> --out <NEW.html>` and republish IN
PLACE (same URL, Artifact `url` field; capabilities db kept) so the owner's saved moves survive. Pages: Harley 287 (the one he hit), the
Armstrong shorthand sorter (ASKS 128, artifact R9GrLoF1ajudygVjo4d17N), Savary de Lancosme (ASKS 137, FDkHh2hqX826r9fdxwXFAF), Juan Manuel
1522 (ASKS 138, YC3XqFjy3UbbbmGdF6Kkp9), Birago no.87 (ROOM 4 Oct 12:41), Vivonne-Longlee (HUMAN-TX-ASKS-sortercheck row 4), and any other
account-3 page listed in HUMAN-TX-ASKS.tsv. For each: read the published page with the Artifact tool, re-render, run
`python3 tools/sorter_preflight.py NEW.html` (expect PASS on template/answerable/right-line/colour), republish, one line in the target's
NOTES.md. A page whose published html cannot be read from account 3 is listed in the done line as "not re-rendered: <why>".

### XMATCH-TRIAGE (account-2; Opus 5.5; cap 4; box 60 min)
`tools/key_crossmatch.py`'s nightly ROOM lines "for the parent: xmatch hit (new lead)" of 4, 5, 7 and 8 Oct 2026 (grep ROOM.md for
"key_crossmatch nightly") were never answered. For each hit: open the two keys it names, say in one line whether the match is (a) the same
office/key family already known (KEY-OFFICES.tsv / KEY-DESIGN.tsv), (b) a real new lead (two targets sharing values that neither folder
records), or (c) noise (common digits, short overlap); for (b) write the lead into both folders' NOTES.md "## While waiting" or next-step
line and a NEXT-STEPS.tsv-visible "next:" sentence; for (a)/(c) one line in `research/XMATCH-TRIAGE-2026-10-09.md`. Also answer N9-XM's
5 Oct flag (Usage 8 proposal on key_crossmatch.py) with a yes/no and why in the same file. Done line lists the (b) leads.

### DEPTH-STATS-CLEAR (account-4; Opus 5.5; cap 4; box 60 min)
FAM-MANTV's flag (ROOM 8 Oct 17:03): `tools/depth_stats.py` builds its code-clause window (8+value+8) from cipher tokens only, so on a leaf
where cipher runs are islands in clear text it splices letters from neighbouring runs. Add an option (`--clear-aware`, off by default) that
builds the window from the leaf's mixed clear+cipher token stream when the folder's reading file carries clear text (document which
input format it reads), with an offline test in tools/tests/ on a synthetic island leaf where the two modes must differ, and a SYSTEM.md
row update. Then re-run it on sachsstaatsarchiv-manteuffel-1712 694/09 0015-16 code 198 and report both windows' p-values side by side in
the folder's NOTES.md (no regrade: the D1 ruling stands unless a verifier re-rules). `python3 tools/system_map_check.py` must pass.
