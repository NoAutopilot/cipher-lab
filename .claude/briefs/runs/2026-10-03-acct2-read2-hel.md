# READ2-HEL: transcribe the R4369 Hellen key and run the known-key test on R1953 (3 Oct 2026, written by LANE-READ2, account 2)

Why: IMG-DECODE1 found that DECODE R4369 (BL Add MS 32276 f.44, 1751, headed "Hellen avec le Roy de [Prusse]") is the English
Deciphering Branch's reconstructed key for Hellen's own correspondence, with French meanings, codes to past 1500. R1953 (4 Jan 1752,
835 tokens, 834 at or below ~1650) has never been tested against Hellen's own key. Target folder: ciphers/hellen-frederick-1752.
Intake gate (pasted by the lane, 23:2x UTC): `hellen-frederick-1752: open (line 1) -- edition/page or full-text-search citation found
within 6 lines`, exit 0.

Model: Opus 5.5. Cap USD 18; box 120 min from your claim, whichever first. Units (Usage 6, per pass = one subagent call on one
page's column crops): R4369 P1-P4, about 4 pages that carry entries x 2 blind passes + 1 reconciliation per page = up to 12 calls at
~USD 1.5 each (~18 with the fixed cost; first look at P1 and P4 at contact size and skip a page that carries no entries, which
cuts the count). The test step is disk-only (~USD 2). Before starting a unit (a pass on one page), stop if it would take you past
80% of the cap or the box; a partial key.tsv with its pages named is a valid stopping point, and the test then runs on what exists
only if the brief's gate below is met.

Start: read `.claude/briefs/README.md` "Common tail" and follow it. `python3 tools/room.py --start` (detached HEAD: `git push
origin HEAD:main; git checkout -B main HEAD`); `date -u`; `python3 tools/key_livecheck.py` (paste the DECODE line); claim with
`python3 tools/room.py "READ2-HEL (account 2 worker, for LANE-READ2)" 'claim: hellen-frederick-1752 R4369 key transcription + R1953 known-key test; box ends <HH:MM> UTC'`.
Read NOTES.md sections "First cheap test: Michell sibling key", "FT4b" and "IMG-DECODE1", `sibling_michell/README.md`,
`sibling_michell/test_sibling.py`, `images/decode/manifest.json`, TRANSCRIPTION.md "Rules for every account", and run
`python3 tools/tool_shelf.py "transcribe a code table (number -> French meaning) from a key sheet image"`.

Steps:
1. Re-fetch R4369 P1-P4 full size per the manifest: ONE login, `NODE_PATH=$(npm root -g) node tools/decode_browser_login.js 4369
   <scratchpad> --guess-fullsize` (absolute URLs for further pages; read the tool header). Check sha1 against the manifest. Images
   go to your scratchpad only, never committed (DECODE images are not public domain); scrub the account name from any saved page.
2. Column crops: `python3 tools/iiif_lines.py --image <page file> --out <scratchpad>/crops --columns ... --debug` (check the debug
   overlay; paste the command and crop count in NOTES.md) BEFORE any subagent call; give subagents only crop paths, never a full page.
3. Two blind Sonnet passes per page (each pass: code -> meaning rows, TSV, `?` for unsure), then `tools/reconcile_passes.py` and your
   own reconciliation against the crops for disagreements only. Write `key_r4369/key.tsv` (code, meaning, grade H -- a period key
   sheet -- or M where the two readers and you could not settle it; source page) and report err_2reader (no benchmark item of this hand:
   say "err_true not measurable").
4. Gate before the test: key.tsv must cover at least 40% of R1953's tokens by code value; if not, stop after step 3 and say so (a
   coverage shortfall is a finding, not a negative).
5. Known-key test, by `sibling_michell/test_sibling.py` (or a `--key` option added to it, not a private copy): decode R1953 with the
   key, score mean fr18 word log-prob of covered tokens; controls side by side: (a) 200 value-shuffled keys (p-value), (b) the same key
   on R1953 with its token ORDER shuffled (200x) -- the statistic is order-sensitive, so this control can differ; (c) positive control
   power at R1953's covered count (FT4's method, using a sample of the key's own meanings as a synthetic plaintext). Write the table to
   HYPOTHESES.md. Also run the same scoring on the other seven letters' ciphertext_R*.txt as secondary rows (no extra cost).
6. If the test beats its controls: a decode via `tools/decode_key.py` with decode.json, `--check` passing, grades per token
   (H/C/S/M/I counts), and `python3 tools/judge_plaintext.py <spec> --file <reading>` output pasted (FAIL may be reported as FAIL).
   No reading is called more than "read with a period key, grade H for <n> tokens". If it does not beat its controls, report both
   numbers as a control-backed result.

NOTES.md: new section "READ2-HEL (3 Oct 2026)" with route, request count per host, vision/subagent calls, err_2reader, the test table.
Status stays `open` unless a reading passes; if you set `partial`, append Remaining gaps/Escalation and paste `tools/gaps_check.py`.
Rule 10 wording only; "report what was found and where it was not found; do not classify novelty". Never print credentials, never
retry a failed login, never call AskUserQuestion. End: commit by explicit path, `python3 tools/file_shrink_guard.py <paths>`,
`python3 tools/room.py --push <paths>`, confirm on origin/main, one done line for LANE-READ2 (account 2) with target and control
numbers side by side, requests per host, calls used, "cost: see the lane ledger".
