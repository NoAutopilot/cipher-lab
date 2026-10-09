# TXP-DEC (LANE TX-ENGINEER-2 round 0b, scout; Opus 5.5; cap 6 of usage; box 60 min from claim, 80% line at 48 min)

For LANE TX-ENGINEER-2 (account 4, session_01NmaB9fhuaMSMYexV4NaVsR). Written 9 Oct 2026 15:1x UTC by date -u.
PREREG `benchmark-tx/PREREG-txeng2-0.md` section 0b item 1. First: `git fetch origin && git checkout -B main origin/main`;
`export CIPHERLAB_ACCOUNT=account-4`; `python3 tools/room.py --start`; read the last 30 lines of ROOM.md; claim with
`python3 tools/room.py "TXP-DEC worker (account 4, Opus)" "claim ..." --push`. Read CLAUDE.md "Access playbook" item 3 (DECODE)
and the good-citizen rule; `sources/decode/NOTES.md`; `tools/decode_browser_login.js` usage line. Never print credentials
(`test -n "$DECODE_USER"`); one browser login this session; scrub the account name from any saved page before committing.

## Job (scout only: no transcription, no decode, no class, no reading of any cipher)
The lane needs known-answer leaves on hands that today's readers get 8-25% wrong, to build a benchmark pool of >= 60 baseline
errors (PREREG 0b). Gallica answers 403 today, so the only reachable copies are DECODE's. The BnF Nevers-office 1590s cluster
is listed Decrypted on DECODE (sources/decode/records-decrypted-2026-09-24.tsv): fr.3621 records 9444-9448 (ff.31-89; 9450 =
f.128 is already dint-f128-print, do not refetch), fr.3623 records 9452-9458 (ff.23-75), fr.3619 records 9438-9443 (ff.73-113).
Dinteville f.128's key is `ciphers/fr3621-dinteville-1592/f128/print_align/` (key_print.tsv) -- read its sign column so you can
say whether a record's cipher uses the same repertoire; its hand, crops `ciphers/fr3621-dinteville-1592/images/f128_L0?_s?.jpg`.

1. One login: `NODE_PATH=$(npm root -g) node tools/decode_browser_login.js 9445 OUT_DIR --guess-fullsize ...` -- read the
   script's usage first; fetch, in this order and 2 s apart, the RecordsView page and every full-size image of records 9444,
   9445, 9446, 9447, 9448, 9452, 9453, 9454, 9455, 9456, 9457, 9458, 9438, 9439, 9440, 9441, 9442, 9443. Stop at 60 requests
   or at the first 403/challenge (log it, one retry after 20 s, then stop). Full-size images go to your scratchpad; commit to
   `sources/decode/nevers-1590s-2026-10-09/` only a 1600-px-wide JPEG of each page plus `manifest.tsv` (record, page, DECODE
   image URL, native pixel size, sha1 of the native file, which page carries the decipherment) -- keep that folder under 30 MB;
   the native files stay in scratch and the manifest says how to refetch.
2. Per record, from the images (your own eyes, one look per page; no subagent, no transcription): (a) cipher kind -- symbol,
   digit, mixed; (b) does the image carry a period decipherment (interlinear above the cipher, facing clear copy, separate
   sheet) and is it legible at native resolution; (c) estimated cipher signs and lines (count one line, multiply); (d) is the
   hand Dinteville f.128's by eye (same scribe) -- y / n / ?; (e) sign repertoire: name 5-8 signs you see and whether they are
   in key_print's sign column; (f) anything that makes it unusable (bleed-through, damage, cipher inside prose only).
3. Write `benchmark-tx/txeng2/decode-scout-2026-10-09.md`: one table row per record with (a)-(f), then a ranked list of the
   best 3-5 items to build as BENCHMARK-TX items, each with estimated scored signs, whether truth could come from the period
   decipherment + key_print (same cipher) or would need a key rebuilt from that decipherment (interlinear_align, agree >= 2,
   the dint-f128-print recipe), and the per-item build cost (two blind Opus passes at about 1.5 per call, one call per page,
   + adjudication + the build script, roughly 7-9 per item). Also `python3 tools/prior_work.py` for the top 3 shelfmarks (the
   lane needs the "own work / contact first" lines; they are Decrypted on DECODE, so N0 by construction -- say so).
4. Commit by path (the md, the manifest, the 1600-px JPEGs), push, ROOM done line "for LANE TX-ENGINEER-2": records fetched,
   requests per host, the top 3 with estimated signs and today's reader error if a figure exists on file for that hand
   (dint pass B 0.188 mapped is the Dinteville figure), and the cost line as "cost: the orchestrator get_session reading".

Stop rules: 80% of cap or box -> finish the record in hand, write the table with what you have, done line. Never AskUserQuestion.
+ `.claude/briefs/README.md` common tail.
