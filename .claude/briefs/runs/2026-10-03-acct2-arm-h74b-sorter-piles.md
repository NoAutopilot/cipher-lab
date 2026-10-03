# ARM-H74b: rebuild the Armstrong shorthand sorter with provisional piles (account-3 orchestrator's return of H74)
(LANE-ARM-B, account 2 lane orchestrator session_017E8NVaLGF23Wd9DtaiA91T, 3 Oct 2026 19:4x UTC)

Why: H74 (ciphers/armstrong-madison-1808/h74/, commit 057ef3e3) cut 997 tiles from the 28 corrected shorthand lines and built
sorter.html, but every tile sits in one pile '?'. The account-3 orchestrator (ROOM 19:39 UTC, read it in full) will not publish it:
the two-step page has nothing to compare against and tools/sign_sorter/browser_tests/test_qa.js fails on a single-pile page.
Model: Opus 5.5. Cap USD 4, box 45 min. Offline, no model reads of the signs (H54/H55 retired model readers here).

Read first: ROOM.md 19:32 (H74 done) and 19:39 (the return flag); NOTES.md step H74; h74/cut_tiles.py, lines.tsv, signs.tsv,
labels.tsv, focus.tsv; TRANSCRIPTION.md (pipeline: family atlas -> top-k -> sorter); `python3 tools/glyph_atlas.py --help`
(pip install numpy if the container lacks it) and `python3 tools/sign_sorter.py --help`; one other published sorter's build as the
worked example (grep sign_sorter.py and glyph_atlas.py invocations under ciphers/*/).

1. Provisional piles: cluster the 997 tiles into about 30-45 shape piles with tools/glyph_atlas.py's cluster mode (or
   tools/sign_sorter.py --auto-clusters K) -- deterministic, seed recorded; where a pile's medoid is nearest one of Tomokiyo's 38
   types (h59/person_pack/tomokiyo_38_types.png) by the same distance, name the pile after it, else a neutral name; family = stroke
   class. These are starting labels for the owner to correct, not readings (say so on the page lede).
2. Rebuild h74/sorter.html in place with the piles, keep focus.tsv (page 3 line 13), keep the folder under 30 MB.
3. Run `tools/sign_sorter/browser_tests/test_qa.js` against the page (run_all.sh shows the harness) and paste its output; it must
   pass. Fix the build, not the test.
4. Hand back: one ROOM flag addressed to the account-3 orchestrator: "H74b sorter rebuilt with N piles, test_qa.js passes:
   ciphers/armstrong-madison-1808/h74/sorter.html; Tomokiyo sheet ciphers/armstrong-madison-1808/h59/person_pack/tomokiyo_38_types.png".
   Do not publish yourself. ASKS 92: update its pointer line in place only if the path or steps changed (fetch/rebase first).
5. NOTES.md "## Step H74b" (cluster count, rule, seed, test output), CAMPAIGN.md: H74 result amended "rebuilt H74b <commit>" and a
   log line with cost; tools/file_shrink_guard.py on every edited shared file before the push. Commit by explicit path, fetch/rebase,
   push.

ROOM: claim line first with your box end time, a halfway cost line, a done line addressed to LANE-ARM-B. Cost from get_session.
Report what was found and where it was not found; do not classify novelty. Never call AskUserQuestion; never print credentials; never
name the owner; never the words solved, cracked, novel, first, new for anything this project did.
