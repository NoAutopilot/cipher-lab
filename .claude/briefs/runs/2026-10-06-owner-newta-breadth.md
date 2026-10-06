# LANE NEWT-A-account-1 -- breadth jobs (written by NEWT-A-account-1, account 1 / owner tag, 6 Oct 2026 23:5x UTC)
Template: .claude/briefs/breadth.md (read it in full). Specs written by LANE NEWT-B-account-2 (NB-CRAV ee817892, NB-HYDE a12bf0d9);
intake gate pasted below for each (run 23:4x UTC by the lane orchestrator, both exit 0). Run test 1 of the spec and its matched
control only; never test 2. Write both numbers into the spec's `cheap_test_done` (date, by, test, target, control, verdict, cost --
cost is "read from get_session by the orchestrator"); a short NOTES.md section with what was done; push. Report in five lines.

## Job NA-HYDE (Sonnet 5.5, cap $3, box 45 min)
Spec specs/hyde-add4166-1659.json, folder ciphers/hyde-add4166-1659.
Gate: `hyde-add4166-1659: open (line 1) -- edition/page or full-text-search citation found within 6 lines` (exit 0).
Test 1 (spec): census plus structure test on the printed groups (Birch 1742 Thurloe vol. 7 pp.775-776 via British History Online,
one fetch, ~1 request; Tomokiyo's copy in sources/cryptiana/web/ as a cross-check). Write the printed numerals as
`ciphertext_print.txt` (state it is a print transcription, rule 2; never call it the leaf). Per name line: groups before each cover
name vs letters in the name; statistic = agreement rate (exact group count == letter count, and correlation); matched control =
shuffled pairing of the same number lines to the same names, 1000 draws, same line lengths. Before running, confirm the control can
differ from the target for this statistic (rule 3, orthogonality paragraph) -- shuffling which line goes with which name changes
the count match, so it can. Also report repeats (670 x6, 101 x6, 25 x4) by position relative to name boundaries. No key, no
decipherment attempt, no plaintext guessed. Unit count: one script + one fetch; no subagents.

## Job NA-CRAV (Opus 5.5, cap $6 -- image fetch plus two-pass transcription, breadth.md; box 70 min)
Spec specs/craven-rupert-1648.json, folder ciphers/craven-rupert-1648.
Gate: `craven-rupert-1648: open (line 1) -- edition/page or full-text-search citation found within 6 lines` (exit 0).
Test 1 (spec): obtain the three pages and transcribe. Route: DECODE R8447, ONE browser login for the whole session
(`NODE_PATH=$(npm root -g) node tools/decode_browser_login.js 8447 <scratch dir> --guess-fullsize` -- check its --help for the exact
flag; A2-HDK 2 Oct 2026 got a full-size JPEG this way for record 4692; re-test per record). If full-size is refused, fall back to the
three login-free thumbnails, say so, and do only a rough group count (no transcription at thumbnail resolution). Scrub the account
name from any saved page; never print credentials. Image to images/ with images/manifest.json (keep folder under 30 MB). Then crop
lines with `tools/iiif_lines.py --image <page file> --out <dir> --debug` (MANDATORY, paste the command; give subagents crops only,
never a full page), two blind passes per TRANSCRIPTION.md (pass A yourself or a Sonnet subagent, pass B a Sonnet subagent, one
page per call: 3 pages x 2 passes = 6 calls at ~$0.6 + 1 reconciliation unit; stop before starting a unit that would cross 80% of
cap or box), `tools/reconcile_passes.py`, ciphertext.txt as transcribed. Report: groups per page, N, distinct values, value range,
repeats, inter-pass agreement, and `python3 tools/design_prior.py` on the ciphertext as the control-backed design reading (its own
shuffled-input false-positive rate is the control number for this descriptive test). No key applied (that is test 2).

## Common tail (both jobs)
First action: `python3 tools/room.py --start` (if it fails to push from a detached HEAD: `git push origin HEAD:main; git checkout -B
main HEAD`). Read the last 30 lines of ROOM.md; ROOM claim line naming the job, cap and box end time (with `date -u`), "for LANE
NEWT-A-account-1"; a `done` line when you stop, with target and control numbers side by side. If ROOM.md says 'retrospective
starting' or 'swap starting', push what you hold and stop. At most 2 subagents at once, Sonnet. Good-citizen rule and the CLAUDE.md
host table for every request; report request count per host. Commit by explicit path, `git fetch origin main && git rebase FETCH_HEAD
&& git push origin HEAD:main`; run `python3 tools/file_shrink_guard.py <paths>` before the final push if you edited existing files.
Per rule 10, report what was found and where it was not found; never new, unpublished, first, solved, cracked; do not classify
novelty. Do not start other targets. Never print or commit credentials, never name the owner. Never call AskUserQuestion.
A negative's done line carries target and control numbers side by side, or it is not a negative.
