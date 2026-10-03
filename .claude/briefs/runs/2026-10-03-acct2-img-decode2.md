# IMG-DECODE2: one DECODE login, image fetch for siena-concistoro-2308 and the Clairambault key records (3 Oct 2026, LANE-IMAGES, account 2)

Model: Opus 5.5. Cap USD 6; box 75 min from your claim. Runs only after IMG-DECODE1's done line (one worker per host at a time).
Units: 2 targets (siena ~USD 3.5, clair keys ~USD 2), one login shared, <=60 requests at >=1.6 s, <=3 vision calls in the whole job
(contact sheets or one page at <=1500 px). Stop before a unit that would cross 80% of cap or box. No transcription, no decoding.
Start: `python3 tools/room.py --start` (detached HEAD: `git push origin HEAD:main; git checkout -B main HEAD`); `date -u`;
`python3 tools/key_livecheck.py` (paste the DECODE line); claim
`python3 tools/room.py "IMG-DECODE2 (account 2 worker, for LANE-IMAGES)" 'claim: siena-concistoro-2308 + clair571/clair577 key records DECODE image fetch (one login); box ends <HH:MM> UTC'`.
Read IMG-DECODE1's NOTES sections (decode-9970-simancas-1527, hellen-frederick-1752) for what the login route did tonight, and the
DECODE host-table row. Route: ONE login, `NODE_PATH=$(npm root -g) node tools/decode_browser_login.js <rec> <scratchpad> --guess-fullsize`
with absolute `--fetch`/`--fetch-page` URLs for the other records (relative filesrv URLs 404). Scrub the account name from saved pages.
1. siena-concistoro-2308: the still-open pieces in NOTES.md (nos. 7 R4796, 9 R4798, 11 R4800, 15 R4803, 19 R4807, 21 R4809, and the
   pairs 6/24, 20/23 -- take their R-numbers from the folder; no.17's R-number is unlisted, find it in RecordsList only if cheap):
   RecordsView fields + full-size images where served. "We have not seen the images ourselves" is the gap this closes.
2. clair571-estrades-1645 / clair577-*: key records 9430 (Clair 577 p.1, Chiffre pour l'Italie), 9431 (Clair 574 p.4-5, Brasset),
   9432 (Clair 580 p.89-95): RecordsView text + images. Write a short pointer in each clair* NOTES.md; images live in
   ciphers/clair571-estrades-1645/keys_decode/ (one place, others point to it).
Images: DECODE images are NOT committed (IMG-DECODE1, 3 Oct 21:35: DECODE record, not public domain, library permission
needed) -- commit images/manifest.json only (URL, record, page, native px, sha1, re-fetch command) and keep files in the scratchpad.
Where full size answers forbidden.png, say so per record. NOTES.md per target: route, requests per host, what was / was not
served. Grades: none. gaps_check on any partial folder touched. Rule 10 wording; "report what was found and where it was not found;
do not classify novelty". Never print credentials, never retry a failed login, never call AskUserQuestion.
End: commit by explicit path, `python3 tools/file_shrink_guard.py <paths>`, `python3 tools/room.py --push <paths>`, confirm on
origin/main, one done line for LANE-IMAGES (account 2).
