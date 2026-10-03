# READ2-SIENA: classify the 11 Siena Concistoro 2308 DECODE records (open cipher vs key vs clear) (3 Oct 2026, written by LANE-READ2, account 2)

Why: IMG-DECODE2 fetched all 24 full-size images of the 11 DECODE records (R4795-R4812) but looked only at a 250-px contact sheet,
which cannot tell cipher from clear. Bourdeau (dbourdeau/cyphersolver targets/siena1421, MIT/CC BY 4.0) filed nos. 6/24, 20/23, 7, 9,
11, 15, 17, 19, 21 as open; his keys are nos. 25/14/4. Target folder: ciphers/siena-concistoro-2308. Intake gate (pasted by the lane,
23:2x UTC): `siena-concistoro-2308: open (line 1) -- edition/page or full-text-search citation found within 6 lines`, exit 0.

Model: Opus 5.5. Cap USD 12; box 90 min from your claim, whichever first. Units (Usage 6): re-fetch (one login, ~30 requests, disk
only) then classification looks, one vision call per record (11 records; a record's pages at <=1500 px long side, or a 2x2 sheet of
its pages; ~USD 0.8 per call) = ~11 calls; then at most ONE known-key test (disk-only, ~USD 2) if step 3's condition holds. Before
starting a unit, stop if it would take you past 80% of the cap or the box.

Start: read `.claude/briefs/README.md` "Common tail" and follow it. `python3 tools/room.py --start` (detached HEAD: `git push
origin HEAD:main; git checkout -B main HEAD`); `date -u`; `python3 tools/key_livecheck.py` (paste the DECODE line); claim with
`python3 tools/room.py "READ2-SIENA (account 2 worker, for LANE-READ2)" 'claim: siena-concistoro-2308 record-by-record classification (open cipher / key table / clear / glossed) + at most one known-key test; box ends <HH:MM> UTC'`.
Read the folder's NOTES.md in full (especially "QUEUE row 2's first cheap test: Bourdeau nos. 25/14/4 key transfer", "bSIE2", "Premise
check", "Image check"), HYPOTHESES.md, and Bourdeau's targets/siena1421/NOTES.md piece table (shallow clone, grep/read only).

Steps:
1. Re-fetch per `images/manifest.json`: ONE login, `NODE_PATH=$(npm root -g) node tools/decode_browser_login.js 4795 <scratchpad>
   --guess-fullsize` (absolute URLs, `--listen` for further records; read the tool header); check sha1s. Images stay in your scratchpad,
   never committed; account name scrubbed from any saved page.
2. One vision call per record: for each page record what it carries -- cipher running text (sign family: graphic signs / alphabet /
   numerals), a key table, clear text, interlinear or marginal decipherment (glossed), address/docket -- with an estimated sign count of
   the unglossed cipher. Cross-check against Bourdeau's piece table and the folder's transcripts/*.tok (do the tokens on disk match what
   the image shows, at a glance?). Write `records.tsv` (no, record, page, content class, est open signs, glossed y/n, matches Bourdeau y/n,
   note). This is a classification, not a transcription: nothing graded.
3. Known-key test only if a record pairs a key table (on these images or Bourdeau's filed keys 25/14/4) with an open piece the folder has
   NOT already tested against that key (read HYPOTHESES.md first -- do not repeat a logged test). Then as in the folder's earlier key-transfer
   section: decode the piece's on-disk transcript, score against 200 value-shuffled keys AND an order-shuffled-cipher control (order-sensitive
   statistic, so the control can differ), with positive-control power at the piece's covered count; both numbers to HYPOTHESES.md. If no
   such untested pair exists, say so and stop after step 2.
4. Name the next step for each open piece in NOTES.md (e.g. a line-crop reread of no.6/20/23 transcripts against the images to get a
   reader-error figure, ~USD 3-4 per pair) -- as suggestions, not run.

NOTES.md: new section "READ2-SIENA (3 Oct 2026)" with route, requests per host, vision calls, the records table summary, the test (if
any) with both numbers. If you set `partial`, append Remaining gaps/Escalation and paste `tools/gaps_check.py`. Rule 10 wording only;
"report what was found and where it was not found; do not classify novelty". Never print credentials, never retry a failed login, never
call AskUserQuestion. End: commit by explicit path, `python3 tools/file_shrink_guard.py <paths>`, `python3 tools/room.py --push <paths>`,
confirm on origin/main, one done line for LANE-READ2 (account 2), "cost: see the lane ledger".
