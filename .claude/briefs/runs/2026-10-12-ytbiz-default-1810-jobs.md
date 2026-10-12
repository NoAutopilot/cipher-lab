# LANE DEFAULT-account-2-20261012-1810 jobs (account 2, lane orchestrator session_017m6ER4Th7oGWxvSdb5ZLxz) -- 12 Oct 2026 18:2x UTC

Lane brief: .claude/briefs/default-lane.md. Cap 60, box 18:10 UTC 12 Oct - 04:10 UTC 13 Oct (80% line 02:10). Gate 0a: SESSION-SWEEP-account-2
stale-claimed since 5 Oct 2026; proceeded, as the 11-12 Oct incarnations did. Backlog read 18:1x UTC: VERIFY-BACKLOG.tsv regenerated -- high rows
are Birago only (off limits); every audit2 row is N0 (Manteuffel 0436, 0109) or N1 (eckert-1864), so Outreach gate 2 does not apply.
`next_steps.py --hot-only`: Gallica answers 403 (18:1x UTC) and googleapis 503 (18:1x UTC), which removes baluze167, fr4712, fr3985/3987,
fr5160, fr3993, colbert26, gramont, ceppo, eckert-1864 and the Verbael step. Rows taken: thurloe-printed's image-check rung (IA), the
fr16045 f.244r merge questions (disk only; text known from the Colbert copy, counted in the guardrail fifth: it builds key86 for the
unread 1585 letters), and the Manteuffel census's never-read unglossed leaves pooled to a testable N (MANT-CEN5 census_unglossed.tsv;
wave 3 of 9 Oct found single leaves under ~60 tokens fail on power, so this job pools four).

## Common rules for every job
Exactly the "Common rules for every job" section of `.claude/briefs/runs/2026-10-09-ytbiz-family-1310-jobs.md` (read it in full), with these
substitutions: address every ROOM line "for LANE DEFAULT-A2-1810 (account 2)"; the hosts bullet below replaces the one there. Halfway line:
one ROOM line at half the box or half the cap, whichever first (skip if done before). `get_session` is not available to you: say
"cost not visible to this session" in the done line. Check 1 before any unit: grep the folder's NOTES.md for a later section that already
ran the unit; if it did, one ROOM line and skip that unit.
Hosts this wave: archive.org ("IA", THUR-94 only, <= 15 requests, >= 1.5 s, take/release lines); www.archiv.sachsen.de ("sachsen", MANT-POOLU
only, <= 12 requests, >= 2 s, take/release lines). PISA-MERGE is disk only. No Gallica, no googleapis.

## Wave 1 (18:2x UTC 12 Oct)

### THUR-94 (Opus, cap 3.5, box 55 min): thurloe-printed, the image-check rung (code 94 conflict and the unread Bamfylde/physician leaves)
NOTES.md "## Remaining gaps (THUR-IA, 12 Oct 2026)" items "Code 94 conflict", "Bamfylde l.68904", "Vol 4 physician l.46866", and the Escalation
image-check line. Intake gate (18:20 UTC, pasted): `thurloe-printed: partial (line 2) -- edition/page or full-text-search citation found within
6 lines`, exit 0. IA images only (Birch vols 4-6 djvu text on disk or one fetch each; leaf images through the same route THUR-IA used).
Units at ~0.8 each (Opus rate from THUR-57/THUR-PS/THUR-IA), in this order, stopping before a unit that would cross 80% of the cap:
(1) vol 5 l.35701 (Bamfylde, "94-77" in the OCR): one leaf, strip crops with `tools/iiif_lines.py --image <leaf> --out <dir>` (pasted), one look:
is there a printed gloss line for 94 the OCR dropped; record the cell and its gloss; (2) vol 4 Bamfylde ll.15913 and 18992: one leaf each, same
procedure, every 94/25/51 with its printed gloss; (3) vol 6 l.68904 (p.576, leaf n579, Second Cipher period): strip crops, transcribe the table
or run, align with bamf/tomokiyo/bamp2_table.tsv, list agreements/conflicts; (4) vol 4 physician l.46866, one leaf, if the cap allows. A value
enters the key only with two printed glosses (rule 4; a conflict with Tomokiyo is logged in HYPOTHESES.md with both witnesses, never settled
by majority); any decode script touched re-run with `--check`. Commit crops a later eye check needs. Update Remaining gaps / Escalation,
`tools/gaps_check.py thurloe-printed`. Report what was found and where it was not found; do not classify novelty.

### PISA-MERGE (Opus, cap 3, box 50 min): fr16045-pisany-rome-1585, the f.244r merge questions as one pre-registered re-score
NOTES.md "## PISA-244" leads (lines ~1265-1267), "## PISA-RS244" and the Verdict's cheapest next: (a) L05 p29-p30, one sign carrying two
labels (T35 p29, T57 p30); (b) the three crossed-p double tokens (?[tcross] + T45 at L02 p11-12 and L04 p44-45; T45 + ?[tcross] at L06 p24-25);
(c) the s1/s2 overlap repeats (L06 p27-p30, probably L08 p25-p26). Intake gate (18:20 UTC, pasted): `fr16045-pisany-rome-1585: partial (line 1)
-- edition/page or full-text-search citation found within 6 lines`, exit 0. Disk and CPU only; at most one vision call (tiles on disk) if a
merge cannot be decided from the committed strips' geometry. Units: (1) PREREG-PISA-MERGE.md pushed in its own commit and checked on
origin/main (`git log origin/main -1 -- <PREREG>`) BEFORE any score: each merge as a tx change (delete/merge tokens), scored with the same
re-score instrument and gates PISA-RS244 used (control 5/5, both p99s, the alignment check vs the Colbert copy, the subset null), one gate per
merge group; (2) score (read the scorer headers; add an option rather than a private copy); (3) commit only PASSing groups (readings
regenerated, `--check` exit 0), log FAILs as FAILs. A changed count goes to a verifier as a one-line next step (no AUDIT edits). Update
Remaining gaps / Escalation, `tools/gaps_check.py fr16045-pisany-rome-1585`. Report what was found and where it was not found; do not classify
novelty.

### MANT-POOLU (Opus, cap 8, box 100 min, sachsen take/release): sachsstaatsarchiv-manteuffel-1712, four never-read unglossed 1712 leaves pooled
MANT-CEN5's census (census_unglossed.tsv) names unglossed or partially glossed code-bearing frames that no reading section has touched. Take the
four with the longest runs by the census notes: 694/08 **0146** (Berl. 25 Juin 1712, No. 48, two long runs), **0088** (Berl. 31 May 1712, No 35,
right page: 17.1.35.21.119.7.10.60 ...), **0247** (Berl. 6 Aout 1712, No 63, right page unglossed: 'le projet de 57.28...'), **0489** (Berl. 15
Nov 1712: 44.66.63.50.39.60.35.51.15.26.10.2.35 ...). Intake gate (18:20 UTC, pasted): `sachsstaatsarchiv-manteuffel-1712: partial (line 1) --
edition/page or full-text-search citation found within 6 lines`, exit 0. Pattern: NOTES.md "## MANT-0454" (the one unglossed leaf that PASSed)
and "## MANT-0181" / "## MANT-0491" (why short single leaves fail: power, and the shuffled-target VOID). Steps:
(0) prior work per the common rules: `tools/prior_work.py` once per frame (item spec as MANT-0491's), checks 1-4 by hand, including Acta Borussica
BO I by date from disk (mant0608/abbo_check.py's PRINTED list) -- a frame printed there is dropped from the pool (one line why) and replaced by the
next census frame (0442, then 0435, 0483, 0426);
(0a) pool size: the census estimates are small (0247 est. 6-8, 0489 est. 14-18; 0146 and 0088 from the census notes). Aim at a pooled N of
at least 60 letter-class tokens (MANT-0454 PASSed at 52; MANT-UNGL's pooled 41 FAILed at power 1.00): if the four frames' code lines hold
fewer, add from 0442, 0435, 0483, 0426 in that order, at most six frames; fix the pool in the PREREG before any pass. Short frames (est. < 20
tokens) may share one subagent call per pass (crops only, labelled per frame).
(1) PREREG-MANT-POOLU.md pushed in its own commit and checked on origin/main BEFORE any pass: the pool (frames, runs), gate (b) exactly as
MANT-0454 ran it (fr18 permuted-key, power control at the pool's N, p95), PLUS the shuffled-target rule from MANT-0181 (the same decode of the
shuffled target through the same judge must NOT pass, else the gate is void for this pool), the per-leaf numbers reported but only the pooled
gate decides; any partial gloss (0088's/0489's small words, if present) read blind in both passes and scored as known answers, never settled
first;
(2) fetch (sachsen take, <= 12 requests, >= 2 s; frame URLs in images/loc694-08-09/frames.tsv), crops with `tools/iiif_lines.py --image <frame>
--out <dir>` (pasted) of the code-bearing lines only, committed;
(3) two blind passes per leaf (one subagent call per leaf per pass, crops only; per-pass rate ~0.7, 8 calls) + one reconciliation unit; decode with
key.tsv via the folder's existing decode script (add an option, no private copy), `--check` exit 0; grade per rule 4 (S only if the pooled gate
PASSes and is not void; else M);
(4) gate, then the reading per leaf (what the runs say, M/S as earned). Stop before a unit that would cross 80% of the cap (8 calls + 1 at ~0.7 ~
6.3 plus the Opus floor). Update Remaining gaps / Escalation, `tools/gaps_check.py sachsstaatsarchiv-manteuffel-1712`. A reading goes to a
verifier as a one-line next step (no AUDIT edits, no status.json edits). Report what was found and where it was not found; do not classify novelty.
