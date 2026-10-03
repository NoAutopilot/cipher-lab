# READ2-ROELL: crib-position test of the NA 1.02.20 inv. 164 key table against the Roell-Van Dedem 1809 letter (3 Oct 2026, written by LANE-READ2, account 2)

Why: READ2-RELABEL (NOTES.md "Next step (READ2-RELABEL, 3 Oct 2026)") named it: the candidate key bundle NA 1.02.20 inv. 164 (1747,
78 scans, DIGITALIZED; 11 at 1000 px on disk, native URLs in images/na_1.02.20_164_viewer.json) against the letter's 2,585 groups
(decode_transcription/, R1469/R1470). A hit licenses a full table transcription (~USD 35-40, not this job); a miss with its control
closes inv. 164 for this letter. Target folder: ciphers/roell-vandedem-1809. Intake gate (pasted by the lane, 23:3x UTC):
`roell-vandedem-1809: open (line 1) -- edition/page or full-text-search citation found within 6 lines`, exit 0.

Model: Opus 5.5 (Sonnet subagents for crop reads). Cap USD 10; box 75 min from your claim, whichever first. Units (Usage 6): 4 native
region fetches (Nationaal Archief / service.archief.nl IIIF, one at a time, >=1.5 s, descriptive UA) + about 8 subagent calls, one per
crop, at ~USD 0.8, + your reconciliation (one unit). Stop before a unit that would cross 80% of the cap or the box.

Start: read `.claude/briefs/README.md` "Common tail" and follow it. `python3 tools/room.py --start` (detached HEAD: `git push origin
HEAD:main; git checkout -B main HEAD`); `date -u`; claim with `python3 tools/room.py "READ2-ROELL (account 2 worker, for LANE-READ2)" 'claim: roell-vandedem-1809 inv. 164 crib-position test with control; box ends <HH:MM> UTC'`.
Read NOTES.md "LIKELY-7" and later sections, HYPOTHESES.md, images/manifest.json, and the CLAUDE.md host-table rows for Nationaal Archief.

Steps:
1. Pre-register in `inv164/PREREG.md` (commit before any vision call): the ~20 French function words (de, la, le, et, que, les, des, a,
   en, du, pour, qui, il, est, ne, pas, par, sur, se, au -- adjust only before looking), the statistic (the summed frequency in the
   letter's 2,585 groups of the code numbers the table assigns to those words, or the count of them among the letter's 20 most frequent
   groups), and the control. **Control (rule 3 orthogonality):** shuffling the letter's group order cannot change a frequency, so the
   control is 1,000 random sets of the same size drawn from the table's own read code numbers (same range, same count), scored the same
   way; pass = target above the control's p99 (several words tested at once). Also record, before looking, what share of the letter's
   groups fall inside the table's numeric range (a range mismatch is a finding by itself).
2. Native region crops of the column bases (or wherever the function words sit) of scans 1, 3, 5, 7 (5000x3904): `tools/iiif_lines.py
   --image <native file> --region ... --out <scratchpad or images/inv164> --debug` (paste commands) BEFORE any subagent call; subagents see
   only crop paths. Keep the folder under 30 MB (commit crops, not full natives; manifest with URLs and sha1). One Sonnet read per crop
   (word -> code number), your check of the function-word rows only.
3. Score target vs control; HYPOTHESES.md row with both numbers. If it passes, write the full-table transcription as the named next step
   (~USD 35-40) and stop; if it fails, log "inv. 164 does not key this letter (control-backed)", conditional on the transcription (rule 2).
NOTES.md: new section "READ2-ROELL (3 Oct 2026)" with route, requests per host, calls, the numbers. If the status moves to `partial` append
Remaining gaps/Escalation and paste `tools/gaps_check.py`. Rule 10 wording only; "report what was found and where it was not found; do not
classify novelty". Never call AskUserQuestion. End: commit by explicit path, `python3 tools/file_shrink_guard.py <paths>`,
`python3 tools/room.py --push <paths>`, confirm on origin/main, one done line for LANE-READ2 (account 2) with target vs control numbers,
requests per host, calls used, "cost: see the lane ledger".
