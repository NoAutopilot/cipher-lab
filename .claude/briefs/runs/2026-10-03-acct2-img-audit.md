# IMG-AUDIT: needs-image rows -- catalogue flag, REQUEST.md and ASKS row per target (3 Oct 2026, written by LANE-IMAGES, account 2)

Model: Sonnet 5 (catalogue checks). Cap USD 4; box 60 min from your claim. Units: ~40 targets, script first (grep the folders),
network only where a folder lacks a quoted catalogue flag (<=3 requests per such target). 0 vision calls. Stop before 80% of cap/box.
Start: `python3 tools/room.py --start` (detached HEAD: `git push origin HEAD:main; git checkout -B main HEAD`); `date -u`; claim
`python3 tools/room.py "IMG-AUDIT (account 2 worker, for LANE-IMAGES)" 'claim: audit of NEXT-STEPS needs-image rows (catalogue flag / REQUEST.md / ASKS row); box ends <HH:MM> UTC'`.
Scope: `python3 tools/next_steps.py` then every row with blocker `needs-image`, EXCEPT decode-9970-simancas-1527, hellen-frederick-1752,
sp87-further-1712, clair1161-avis-flandre-1688, fr3151-noailles-1558, gla-claudiamedici-1633 (other LANE-IMAGES workers), any folder with
a ROOM claim younger than 6 h without a done line, and birago/nevers/armstrong/debosnys folders.
Per target, write one row to `IMAGES-AUDIT-2026-10-03.tsv` (repo root; columns: folder, holding, shelfmark, catalogue_record_url,
availability_flag_quoted (verbatim, with date), request_md (y/n + item), asks_row (number or none; ASKS rows often name a shelfmark or a
batch -- e.g. TNA row 57 -- not the folder, so search by shelfmark too), blocker_ok (is the needs-image label right? e.g. moray-wood-1568
already has its full-size images since GAPS3, fr4712 ff.9/11/12 carry no cipher), action_taken).
Actions allowed: (a) where a folder quotes no holding-catalogue availability flag, fetch it once via the CLAUDE.md host-table route
(TNA Discovery API `digitised` field, tools/discovery_items.py; BL searcharchives.bl.uk?format=json; NA item page drupal-settings-json;
archivesetmanuscrits; LABW) and quote it in NOTES.md; if the flag says digitised, say so in the TSV and stop on that target (the lane
orchestrator briefs the fetch); (b) where the image is genuinely not online and REQUEST.md lacks the item, add the REQUEST.md row
quoting the record; (c) where no ASKS row covers it, append one ASKS row (fetch/rebase first) quoting the record -- never a guess, and
batch by holding (one ASKS row per archive, listing shelfmarks), not one per folder. Do not edit NEXT-STEPS.tsv by hand.
Good-citizen rule per host (>=1.5 s, one at a time). Rule 10 wording; "report what was found and where it was not found; do not
classify novelty". Never call AskUserQuestion; never name a person's private address.
End: commit by explicit path, `python3 tools/file_shrink_guard.py <paths>`, `python3 tools/room.py --push <paths>`, confirm on
origin/main, one done line for LANE-IMAGES (account 2): counts (flag present / fetched / digitised-found / REQUEST rows added / ASKS
rows added / mislabelled blockers), requests per host.
