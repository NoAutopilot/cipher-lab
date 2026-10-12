# LANE DEFAULT-account-2-20261012-0510 jobs (account 2, lane orchestrator session_01CKd3VUundhU5gtJWumnf3R) -- 12 Oct 2026 05:2x UTC

Lane brief: .claude/briefs/default-lane.md. Cap 60, box 05:10-15:10 UTC 12 Oct (80% line 13:10). Gate 0a: SESSION-SWEEP-account-2 row
stale-claimed since 5 Oct 2026; proceeded, as the 11 Oct incarnations did. Backlog read 05:1x UTC: VERIFY-BACKLOG.tsv regenerated (73 rows) --
every audit2 row is N0 (Manteuffel 0436, 0109) or N1 (eckert-1864), so Outreach gate 2 does not apply; the counted rows are decided.
`next_steps.py --hot-only`: Gallica answers 403 to the manifest (05:1x UTC), which still removes baluze167, fr4712, fr3985 f.143r, fr5160,
fr3993, colbert26, gramont, ceppo; HTRC EF still errors (MongoError) on osu.32435013919725 (rah-salazar out). The `parallel` column was
spot-checked on six rows and is stale on all six (harley-287 HAR-GLOSS, blathwayt BLA-TRY, brochado BRO-CT, Jan van Nassau JVN-GLY,
Vivonne-Longlee D4-VIVMOUS done; matignon f.179 taken by account 1, MAT-F179). Google Books API answers 200 again (05:1x UTC; 503/429 on
10-11 Oct), which reopens the two jobs below.

## Common rules for every job
Exactly the "Common rules for every job" section of `.claude/briefs/runs/2026-10-09-ytbiz-family-1310-jobs.md` (read it in full), with these
substitutions: address every ROOM line "for LANE DEFAULT-A2-0510 (account 2)"; the hosts bullet below replaces the one there. Halfway line:
one ROOM line at half the box or half the cap, whichever first (skip if done before). `get_session` is not available to you: say
"cost not visible to this session" in the done line. Check 1 before any unit: grep the folder's NOTES.md for a later section that already
ran the unit; if it did, one ROOM line and skip that unit.
Hosts this wave: www.googleapis.com/books/v1 (always `&country=US&key=$GOOGLE_BOOKS_KEY`, >= 1.5 s, one retry after a pause on 429/503 then
stop); archive.org ("IA", THUR-GB only, >= 1.5 s, <= 30 requests, take/release lines); www.delpher.nl / jsru.kb.nl (THUR-GB only, <= 10,
>= 2 s). No Gallica.

## Wave 1 (05:2x UTC 12 Oct)

### ECK-GP13 (Opus, cap 2, box 40 min): eckert-1864, Grant Papers vol. 13 by Google Books
NOTES.md "## Remaining gaps (ECK-S65G, 11 Oct 2026)" item 1 and its Verdict cheapest next. Intake gate (05:19 UTC, pasted):
`eckert-1864: partial (line 3) -- edition/page or full-text-search citation found within 6 lines`, exit 0.
Units: (1) the positive control the ECK-S65G section names, then `fortmonroe/eck_s65g_gb.py` (the keyed googleapis pass, read its header;
fix only a stale argument, no new script) for E589 E590 E591 E592 against Papers of Ulysses S. Grant vol. 13 (2-20 Feb 1865), ~0.4; (2) for
each hit, record volume id, the snippet and, where the API gives it, the page; say "in print (snippet)" / "not located (searched ...)" per
row in a dated NOTES.md section; (3) only if a hit changes a row's record: correct NOTES.md and the folder's status/AUDIT pointers the way
FIX-AUD2-L17 did (no N-class edits -- a changed class goes to a verifier: write it as a one-line next step). Update Remaining gaps /
Escalation, `tools/gaps_check.py eckert-1864`. ~3 units at ~0.4. Report what was found and where it was not found; do not classify novelty.

### THUR-GB (Opus, cap 2.5, box 70 min): thurloe-printed, the Google Books / Delpher text routes and the p.511 image check
NOTES.md "## Remaining gaps (THUR-NIJ, 11 Oct 2026)" (l.3871 on). Intake gate (05:19 UTC, pasted): `thurloe-printed: partial (line 2) --
edition/page or full-text-search citation found within 6 lines`, exit 0. Units, cheapest first, each logged done or blocked:
(1) Nijhoff Bijdragen X p.291 (the Dutch of the 18 July 1653 letter, Birch I p.340): Google Books API (country=US, key) for "Geheime brieven"
Beverningh / Bijdragen voor vaderlandsche geschiedenis X, with a positive control (a phrase known in an on-disk Bijdragen volume), ~0.3;
(2) the 1725 Verbael (Beverningh): Google Books API, then Delpher/KB once, ~0.4; if a full-view copy of either exists, list the pages that
should carry the 27 June / 18 July / 22 Aug 1653 letters (a page read is a later unit, not this job, unless it is one page under 0.3);
(3) image-check vol 5 p.511 (IA leaf n504, the 2 Nov 1656 letter's first runs) for a 94 and its gloss: one leaf, strip crops with
`tools/iiif_lines.py --image <leaf file> --out <dir>` pasted before the subagent call, one blind look, ~0.5. No key edits unless a printed gloss of
the same table supports one (then rule 7: the folder's p.160 decode script with --check). Update Remaining gaps / Escalation,
`tools/gaps_check.py thurloe-printed`. Report what was found and where it was not found; do not classify novelty.

## Wave 2 (06:1x UTC 12 Oct)
Wave 1 results: ECK-GP13 done 1.46 (control HIT vol. 13; E589 not located; E590 503 twice, E590-E592 unsearched). THUR-GB done 5.17 (2.07x
its 2.5 cap; Nijhoff Bijdragen X pp.291-294 found on Delpher, p.340 code 330 now C; Verbael not located). Gallica 403 at 06:1x UTC;
googleapis 200 at 06:1x UTC.

### ECK-GP13B (Sonnet, cap 1, box 25 min): eckert-1864, the rest of the Grant Papers vol. 13 pass
NOTES.md "## Remaining gaps (ECK-GP13, 12 Oct 2026)" item 1. Intake gate as ECK-GP13 (exit 0). Re-run `fortmonroe/eck_s65g_gb.py` (the same
way ECK-GP13's section records: keyed, `country=US`, >= 2 s) for the control, E590, E591, E592 and one looser E589 query (`Monohansett
Monroe`); 5 queries, one retry after 60 s on a 503 then stop. Add the rows to a dated "## ECK-GP13B" section in ECK-GP13's table format;
change no row record, AUDIT or N-class (a hit that would change one is written as a one-line next step for a verifier). Update Remaining
gaps / Escalation, `tools/gaps_check.py eckert-1864`. Report what was found and where it was not found; do not classify novelty.
