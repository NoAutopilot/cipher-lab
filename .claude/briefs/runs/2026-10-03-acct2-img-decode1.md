# IMG-DECODE1: one DECODE login, image fetch for three image-blocked targets (3 Oct 2026, written by LANE-IMAGES, account 2)

Model: Opus 5.5. Cap USD 6; box 75 min from your claim. Units: 3 targets, about USD 1.5-2 each (one login shared, ~40 requests
total at >=1.6 s, at most 3 vision calls in the whole job, each on a contact sheet or one page at <=1500 px). Before starting a
unit, stop if it would take you past 80% of the cap or the box. No transcription, no decoding, no key test: the next lane does that.

Start: `python3 tools/room.py --start` (detached HEAD: `git push origin HEAD:main; git checkout -B main HEAD`); `date -u`;
`python3 tools/key_livecheck.py` (paste the DECODE line); claim with
`python3 tools/room.py "IMG-DECODE1 (account 2 worker, for LANE-IMAGES)" 'claim: decode-9970-simancas-1527 + hellen-frederick-1752 + sp87-further-1712 DECODE image fetch (one login); box ends <HH:MM> UTC'`.
Read each folder's NOTES.md "While waiting"/"Remaining gaps"/last section first, and the CLAUDE.md host-table DECODE row.
Route: ONE login for the whole job, `NODE_PATH=$(npm root -g) node tools/decode_browser_login.js <rec> <scratchpad> --guess-fullsize`
with absolute `--fetch`/`--fetch-page` URLs for every further record in the same run (relative filesrv URLs 404 -- moray-wood GAPS2
lesson; read the tool's header for the multi-record flags). Scrub the account name from any saved page before committing.

Units, in order:
1. decode-9970-simancas-1527: R9970 RecordsView + its images (full size). One vision look at most: does each page carry cipher or
   clear Spanish text, and does it read as a minute to "al principe"/"Antonio Fucar" (Bourdeau, 28 Sept) -- an image-type check,
   recorded as such, no transcription. Update "While waiting" and flip the image blocker.
2. hellen-frederick-1752: RecordsView (sender, date, pages) + thumbnails for R4369, R4370, R4373, R4377, R4378, R4379 (NOTES.md
   line ~574 and "Next suggestion"). One contact-sheet look: which sheets carry French meanings (like R4374) vs tallies (like
   R4380). Full size only for meaning-bearing sheets. Table into NOTES.md.
3. sp87-further-1712: key records 8957 and 8763-8765 (NOTES.md ~line 210): are full-size images served, RecordsView fields, and
   whether any key's caption/title names the French plenipotentiaries or Malknecht (from the record text first; one thumbnail look
   only if the record text is silent).
Images: keep each folder under 30 MB -- commit thumbnails and full-size pages downscaled to <=2500 px long side as JPEG, with
images/manifest.json (URL, record, page, native px, sha1 of the native file, how to re-fetch); line crops with
`tools/iiif_lines.py --image <file> --out <dir> --debug` only for pages that carry cipher, debug overlay checked.
NOTES.md per target: route that worked, request count per host, what was fetched, what was NOT served. If a record's full size
answers forbidden.png, say so and file nothing new unless the folder has no REQUEST.md row for that image (then add one).
Grades: none (nothing read). gaps_check on any `partial` folder touched. Rule 10 wording; "report what was found and where it
was not found; do not classify novelty". Never print credentials, never retry a failed login, never call AskUserQuestion.
End: commit by explicit path, `python3 tools/file_shrink_guard.py <paths>`, `python3 tools/room.py --push <paths>`, confirm on
origin/main, one done line for LANE-IMAGES (account 2) with per-target result, requests per host, vision calls used.
