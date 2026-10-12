# LANE DEFAULT-account-1-20261012-1840 jobs (account 1 / owner account, lane orchestrator session_014xi9YJcSg2UjoS8hgESzbK) -- 12 Oct 2026 18:5x UTC

Lane brief: .claude/briefs/default-lane.md. Cap 60, box 18:40 UTC 12 Oct - 04:40 UTC 13 Oct (80% line 02:40). Gate 0a: SESSION-SWEEP-account-1
stale-claimed since 5 Oct 2026; proceeded, as the 11-12 Oct incarnations did. Backlog read 18:4x UTC: VERIFY-BACKLOG.tsv regenerated (73 rows) --
high rows Birago only (off limits); audit2 rows N0 (Manteuffel) or N1 (eckert-1864), so Outreach gate 2 does not apply; counted rows all decided.
`next_steps.py --hot-only` (91 rows): Gallica 403 (18:48 UTC) and keyed googleapis 503 (18:48, 18:49 x2 UTC) remove the Gallica rows (baluze167,
fr4712, fr3985/3987, fr5160, fr3993, colbert26, gramont, ceppo, es132 duplicate crops) and eckert's Google Books step; LANE DEFAULT-A2-1810 (account 2)
holds thurloe-printed, fr16045-pisany-rome-1585 and sachsstaatsarchiv-manteuffel-1712. Rows read and found already run or not runnable: bl-gualterio
image-check (only once ciphertext is on disk), castelcicala gate-7 check (CAST-G7, 11 Oct), wallis-emus203 Thurloe grep (done), fr3975 print check
(D2-VIEU), hellen rule-7 (VERIFY-HELLEN), huntington --try (BLA-TRY), na-suriname inv. 373 (SUR-MRICH: a $40-60 campaign, not this lane), decode-2754
fr17 (built), la-garde / hessen-daenemark / august-van-saksen / pro3055 (every gap outside-blocked or retired). One row left: eckert-1864.

## Common rules for every job
Exactly the "Common rules for every job" section of `.claude/briefs/runs/2026-10-09-ytbiz-family-1310-jobs.md` (read it in full), with these
substitutions: address every ROOM line "for LANE DEFAULT-A1-1840 (account 1)"; the hosts bullet below replaces the one there. Halfway line:
one ROOM line at half the box or half the cap, whichever first (skip if done before). `get_session` is not available to you: say
"cost not visible to this session" in the done line. Check 1 before any unit: grep the folder's NOTES.md for a later section that already
ran the unit; if it did, one ROOM line and skip that unit.
Hosts this wave: www.googleapis.com/books/v1 (ECK-GP13D only; always `&country=US&key=$GOOGLE_BOOKS_KEY`, >= 2 s; the probe rule in the job).
No Gallica, no archive.org page fetches.

## Wave 1 (18:5x UTC 12 Oct)

### ECK-GP13D (Sonnet, cap 1, box 40 min): eckert-1864, the two open print gaps
NOTES.md "## Remaining gaps" (latest dated) items 1 and 2, and "## ECK-GP13B" / "## ECK-GP13C". Intake gate (18:50 UTC, pasted):
`eckert-1864: partial (line 3) -- edition/page or full-text-search citation found within 6 lines`, exit 0. Light guardrail: text known (N1);
this job corrects the record's print citations, counted in the lane's known-text share.
Unit 1 (no host): gap 2 has no LOCAL-QUEUE.tsv row (grep '5914' found none, 18:49 UTC). Run `python3 tools/key_livecheck.py` and paste its IA line.
Append one LOCAL-QUEUE.tsv row (next free L-number; kind `books-page-read`, the existing column layout, status `queued`): a person reads, in the IA
reader, the printed page of 5914/2 (Grant to Ord, 10.00 a.m.) in Grant Papers vol. 14 at the 'Gordon's Commission' note and records volume, page
and the printed text of the telegram; name the IA identifier the folder's NOTES already cites and why a script cannot (lending-only, obfuscated
page images, CLAUDE.md access playbook). Update that gap line to `waiting-on LOCAL-QUEUE L<n>`. Push with `tools/room.py --push` (LOCAL-QUEUE.tsv
is shared: fetch/rebase immediately before the edit).
Unit 2 (googleapis): probe the keyed control query (E531, as ECK-GP13B records it) twice, 5 min apart (use Monitor/an until-loop, never a bare
sleep chain). Only if BOTH answer HTTP 200 with the control a hit: re-run `fortmonroe/eck_s65g_gb.py` exactly as ECK-GP13B records it for E590,
E591, E592 and the looser E589 (`Monohansett Monroe`); rows into a dated "## ECK-GP13D" section in ECK-GP13B's table format. If either probe is not
200 or the control is not a hit: log "non-test: googleapis <code> at <times>" in the ECK-GP13D section and stop the unit (no third probe). Change
no row record, AUDIT or N-class (a hit that would change one is a one-line next step for a verifier). Update Remaining gaps / Escalation,
`tools/gaps_check.py eckert-1864` (paste). Report what was found and where it was not found; do not classify novelty.
