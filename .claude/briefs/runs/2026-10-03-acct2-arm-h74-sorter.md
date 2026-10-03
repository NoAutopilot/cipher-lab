# ARM-H74: the Armstrong shorthand as a sign-sorter page for the owner (H59 pack rebuilt)
(LANE-ARM-B, account 2 lane orchestrator session_017E8NVaLGF23Wd9DtaiA91T, 3 Oct 2026 19:2x UTC)

Target: ciphers/armstrong-madison-1808, the 35 shorthand passages. Row H74 in CAMPAIGN.md is yours (claimed by the lane; set its
status/result and add a log line when you stop). Model: Opus 5.5. Cap USD 4, box 45 min. This is an offline build: no model reads of
the signs (H54/H55 retired model readers for this script; the person labels are the instrument).

Read first: CAMPAIGN.md rows H54, H55, H58, H59, H60, H61 and the log; NOTES.md steps H58, H59, H61; h59/README and h59/person_pack/;
images/shorthand/index.tsv and INVENTORY_reconciled.tsv; TRANSCRIPTION.md (the transcription standard, owner 3 Oct); LESSONS.md
"Settle the alphabet before reading"; `python3 tools/sign_sorter.py --help` and its test in tools/tests/, plus one existing sorter
build in the repo as the worked example (grep for sign_sorter.py invocations under ciphers/*/ and .claude/briefs/runs/).

1. Tiles: cut every shorthand sign of the corrected line crops (H58 crops, H61's page-2 line mapping) into tiles with a deterministic
   segmentation step (connected components or the segmentation tools/sign_sorter.py expects); record the cut rule and the count per
   line; where a component plainly joins two signs or splits one, leave it for the sorter's bad-cut pile rather than guessing.
2. Starting piles: Tomokiyo's 38-type sheet (B35/H59) as the initial labels where a line already has them, unlabelled otherwise; the
   "Check these first" focus list = the types B35's two readers split on most (line-b/b35 pass files, read only).
3. Build: `python3 tools/sign_sorter.py ... --title "Armstrong 1808 shorthand" --out ciphers/armstrong-madison-1808/h74/sorter.html
   --data-out ciphers/armstrong-madison-1808/h74/data` (exact flags from --help); open the page headless once
   (`node tools/browser_fetch.js file://... --shot`) to confirm it renders; keep the folder under 30 MB.
4. Hand-off, not publish: update ASKS.md row 92 in place (fetch/rebase first; keep its existing facts) with the sorter's path, what the
   owner does (sort piles, merge, mark bad cuts), and that tools/sign_sorter_apply.py turns the result into h59/person_labels.tsv-style
   labels for H60. One ROOM flag line addressed to the account-3 orchestrator: "H74 sorter page ready to publish for the owner: <path>".
   Do not publish an artifact yourself.
5. NOTES.md "## Step H74", CAMPAIGN.md H74 status/result + log line with cost; tools/gaps_check.py armstrong-madison-1808 before the
   done line; tools/file_shrink_guard.py on ASKS.md before the push. Commit by explicit path, fetch/rebase, push.

ROOM: claim line first with your box end time, a halfway cost line, a done line addressed to LANE-ARM-B. Cost from get_session.
Report what was found and where it was not found; do not classify novelty. Never call AskUserQuestion; never print credentials; never
name the owner; never the words solved, cracked, novel, first, new for anything this project did.
