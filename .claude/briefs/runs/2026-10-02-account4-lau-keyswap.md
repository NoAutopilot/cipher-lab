# LAU-KEYSWAP: fr3625-lauriere-1593 -- re-run the key57 control with the alphabet correction PR 15 names (script only)

Written 2 Oct 2026 00:1x UTC (clock read) by the account-4 parent (session_01SEzoee67SivPooFpTkxMme).
Role field for ROOM.md lines: `LAU-KEYSWAP (account-4)`. Model: Fable 5.1 (Opus 5.5 if Fable fails). Cap: USD 3.
Box: 25 minutes. Disk only: no network, no vision.

## Context (read NOTES.md's two newest sections first)

WEBCHECK-fr3625-lauriere-1593 (1 Oct 2026 23:41 UTC) found the target `found-solved`: dbourdeau/cyphersolver issue 13
and PR 15 (merged 30 Sept 2026) read every run of no.55 with Tomokiyo's key no.57, and the PR thread says key57's
alphabet had "mu under C and the c-form under H the wrong way round" -- the likely cause of NX-LAU3's 4/12 miss.
LAU-U3U4 (23:43 UTC) settled fol.58r (key57/f58s_ciphertext.tsv, 138 numerals 85H/37M/16L) and ran
`key57/control_key57.py --apply-f58` with the uncorrected key57.tsv: real -0.930 vs 20 shuffled keys mean -0.957,
3 of 20 better -- GATE FAIL. Any reading here is N0 (rule 10); this job is a key-table correction to hand on
(README "contribution"), not a solve.

## The job

1. `python3 tools/room.py --start`; last 30 ROOM.md lines; claim line.
2. In `key57/` make `key57_v2.tsv`: a copy of the key57 table with the two letter values swapped exactly as PR 15
   describes (read the PR text quoted in NOTES.md's Web and blog check section; if the quoted text does not name
   both signs unambiguously, stop and say so -- do not guess a different swap). Leave key57.tsv untouched.
3. Re-run exactly LAU-U3U4's U4 command with the v2 key (gloss rows removed as before, 20 seeds), and the same on
   fr.3625 no.55's own ciphertext if `control_key57.py` supports it (its `--help`; the NX-LAU3 12-anchor test is the
   relevant known-answer: report anchors matched out of 12 with v2 vs the 4/12 on record).
4. Report, side by side: v1 real vs shuffle (from LAU-U3U4) and v2 real vs shuffle, judge lines, anchors 12.
   Append one HYPOTHESES.md row per run; a dated NOTES.md section "## LAU-KEYSWAP (2 Oct 2026, account-4)" with
   the numbers and one sentence on what the correction does or does not change. Status word stays `found-solved`.
   No reading file is written (N0 item).
5. Commit by explicit path, rebase on origin/main, `python3 tools/restricted_guard.py --outgoing`, push to main.
   Done line with both pairs of numbers. Stop.

Rule 10 wording only; cite setsunaatto and Bourdeau (cyphersolver issue 13 / PR 15) wherever the correction is
mentioned. The common tail of `.claude/briefs/README.md` applies in full.
