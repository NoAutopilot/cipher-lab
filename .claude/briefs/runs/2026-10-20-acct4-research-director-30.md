# Research director, wave 30 (20 Oct 2026, 03:0x UTC by date -u): the Vivonne sorter lost the owner's sort -- diagnose, recover, fix

Common tail: .claude/briefs/README.md applies (ROOM claim/done with the usage phrase, wall-clock box, no AskUserQuestion, never a dollar
figure for yourself). Load the artifact-capabilities and artifact-design skills before touching the page. No personal data in the repo.

## JOB SORTER-SAVEFIX (account 4; Opus 5.5; cap USD 8; box 75 minutes; hosts: claude.ai artifact read/publish and its database only; Price: vision calls: 0 x USD 0 = 0)

What happened. The owner sorted https://claude.ai/artifact/6cP2xmEZertkDcPoc9uYRC ("Vivonne 1573: split two signs", ASKS 173) on 20 Oct
2026 about 02:4x-02:54 UTC: he went through each tray, took out every tile that did not fit, and grouped them with look-alikes into
SEVERAL new piles. The database holds only 6 `moves` docs (all 02:54:00-02:54:14), 3 `newpiles` (tray A-b, B-b, B-c), and nothing in
`piles`, `clusters`, `checked`, `added`, `recuts`. On reload (owner's screenshot, 03:0x) the page shows tray A 12 tiles, tray A-b 2, and
a NOT-LETTER pile of 1 tile that is in no newpiles doc -- "that's not how I left them". His work was lost; this job exists so he does not
have to redo it and so it never happens again on any sorter page.
1. Diagnose from the published page, not the repo copy: `Artifact` action read on the URL (the repo file
   ciphers/fr16104-vivonne-spain-1572/tx/ksplit/sorter/sorter_viv_ksplit.html may differ); read every collection with ArtifactData. Find
   the path by which moves can be dropped or never sent: `dbMode` 'connecting'/'local' fallback (track() stores only in localStorage
   'sorter:all' in local mode), failedPaths after one retry, onSnapshot overwriting local state, doc-key collisions in key(), the
   NOT-LETTER pile's origin. Write the cause, with the code lines, in tx/ksplit/sorter/SAVE-INCIDENT-2026-10-20.md.
2. Recovery: if any path can have left his full arrangement in his browser (localStorage 'sorter:all'), add to the page a clearly
   labelled one-click "Recover my sort from this browser" that shows him the recovered piles and, on his confirm, writes them to the
   database (never silently, never over newer database docs without saying so). If no such path exists, say so plainly in the incident
   file.
3. Fix, for this page and the sorter generator (tools/sign_sorter.py and the page template it emits, so every future sorter gets it):
   every write is confirmed by a read-back; a persistent, high-contrast banner shows "N changes NOT saved" (with a retry button) whenever
   any write is pending or failed, and "All changes saved" only after read-back; if storage cannot connect the page says so before he
   starts, not after; local mode keeps working but is labelled. Add an offline test in tools/tests/ for the save state machine
   (connecting -> held -> pumped; failure -> visible). Keep the page blind (no values, no machine guesses; tools/sorter_preflight.py and
   tools/cvd_check.py pass).
4. Republish the page to the SAME URL (read first, then publish with `url`), keeping the existing database docs. Verify with ArtifactData
   (as_level interact) that a test write from the page round-trips, then delete your own test docs.
5. Do NOT change, reconstruct or guess the owner's piles from his description or the screenshot. ROOM done line names what he must do
   (open the page in the same browser and press Recover, or re-sort if recovery is impossible).
Report: cause (one sentence), recovery possible yes/no, fix and test results, five lines.

Amendment (owner, 20 Oct 2026 ~03:0x UTC, relayed to the worker by send_message): he will redo the sort, so step 2 (recovery) is
optional. Add an explicit "Save my sort" button that batch-writes the full arrangement, reads it back and shows "Saved: N tiles in M piles
at HH:MM" or a red error; keep autosave and the unsaved banner. Clear the stale 02:54 partial-sort docs only after the incident file
records them, so he starts from clean trays; ROOM line when the page is ready.
