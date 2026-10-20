# Research director, wave 32 (20 Oct 2026, 03:4x UTC by date -u): re-render the other live sorters with the fixed save

Common tail: .claude/briefs/README.md applies (ROOM claim/done with the usage phrase, wall-clock box, no AskUserQuestion, never a dollar
figure for yourself). Load the artifact-capabilities and artifact-design skills before touching a page. No personal data in the repo.

## JOB SORTER-RERENDER (account 4; Sonnet 5; cap USD 5; box 60 minutes; hosts: claude.ai artifact read/publish and database only; Price: vision calls: 0 x USD 0 = 0)

SORTER-SAVEFIX (20 Oct 2026, a85ed30ca; ciphers/fr16104-vivonne-spain-1572/tx/ksplit/sorter/SAVE-INCIDENT-2026-10-20.md) found that
sorter template 2026-10-15.1 can silently drop a person's choices (a refused write dropped after one retry; a this-browser-only session
never handed back), and fixed tools/sign_sorter.py's template (read-back confirmed writes, "N changes NOT saved" banner, "Save my sort"
button). The owner's Vivonne sort was lost this way. Every other live sorter page is still on the old template.
1. List the sorter pages linked from OPEN ASKS.md rows (102, 107, 118, 119, 128, 145 and any other open row naming a claude.ai/artifact
   sorter link); for each, `Artifact` read it and note its template version and owner (whether this account can write it).
2. For each page this account can write: BEFORE republishing, read every database collection with ArtifactData and save a copy of the
   docs to the target folder's sorter/ directory as db-snapshot-2026-10-20.json (these may hold a person's earlier choices -- never
   delete or overwrite them). Re-render the page with the fixed template from the same inputs the page was built from (tools/sign_sorter.py
   with the target's existing pile/sign files; tools/sorter_preflight.py and tools/cvd_check.py pass), republish to the SAME URL, and
   verify with ArtifactData that the existing docs still load and a test write round-trips (then delete only your own test doc).
3. For a page this account cannot write, do not copy it elsewhere: list it in the report with its owning account.
4. Append to each affected ASKS row: "re-rendered 20 Oct 2026 with the Save button and confirmed saves (SORTER-RERENDER)" or "still on
   the old template; owned by <account>; do not sort until re-rendered". ROOM done line for the account-4 parent.
Report: pages found, re-rendered, skipped (and why), docs preserved per page, five lines.
