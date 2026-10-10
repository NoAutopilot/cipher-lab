# LANE LEDGER-16 worker jobs (account 1, session_01TLWfkiSj8wYTbXc7mEnE5G; written 10 Oct 2026 14:5x UTC by date -u)

Lane brief .claude/briefs/lane-ledger.md (+ lane-common-blast.md). WORK-QUEUE row DEFAULT-account-1-20261010-1440. Blast refill after LANE LEDGER-15
(closing 14:3x, wave 3 done). **Scope: eckert-1864 Fort Monroe ledger mssEC 25 (obj 5952, `ciphers/eckert-1864/fortmonroe/`) -- the 33 filings CLEAR-SWEEP
left NONE or NEAR (fortmonroe/clear_sweep.tsv), never first-audited, plus a FIX job on FV-L15m s.5.** Every ROOM line ends "for LANE LEDGER-16 (account 1)".
seven_day allowed_warning has been on since 9 Oct (not a stop under lane-common-blast; say so in your done line if you see it). New entry IDs, if any: E578-E599
(check the highest used first; R-5855 filed none).

Intake gate: `python3 tools/intake_gate_check.py eckert-1864` -> "eckert-1864: partial (line 3) -- edition/page or full-text-search citation found within
6 lines" (exit 0, 14:4x UTC 10 Oct). Re-run it yourself before deep work and paste the line.

**Common to every worker** -- exactly the "Common to every worker" block of .claude/briefs/runs/2026-10-10-acct1-lane-ledger15-jobs.md (and what it points
back to): the hdl.huntington.org / CONTENTdm token shared with every other session (post `take` in ROOM, re-read ROOM, wait for any earlier un-released take;
`release` with the request count; <= 40 requests per take, < 300 per session; on a dropped connection one retry after 25 s, then stop that take); the same
take/release discipline for be-api.us.archive.org, archive.org and googleapis (one worker per host at a time across the lane); prior-work step
(.claude/briefs/prior-work-step.md, civil-war adapter) pasted before the first priced step; **step 0 is a non-test on mssEC 25** (never N1 from a step-0 hit);
all 411 Fort Monroe page JSONs on disk; rebase before every push to shared files (status.json, AUDIT.md, NOTES.md, WORK-QUEUE.tsv, SECOND-OPINIONS-QUEUE.tsv);
lessons (1)-(4) of that block, with LEDGER-15's correction: Grant Papers vol. 14 IS on IA (`papersofulyssess0014gran`, be-api); vol. 13 is not (Google Books
API, `&country=US&key=$GOOGLE_BOOKS_KEY`, never print the key; ids mnRjmhe3QLoC / ij8fAQAAMAAJ). Lessons added by LEDGER-15: (5) of 12 wave-1 entries, 7 had a
holder clear copy at another pointer (Washington clear books ~7680-7830 and 8500-8660) or print -- CLEAR-SWEEP already ran two-word queries on these 33 and
found none; its NONE is a search result, not a negative (control E557 hit only after rewording): run at least three FRESH queries per entry (different rare
words, names, vessel names, numbers), not CLEAR-SWEEP's (its queries are in NOTES "## CLEAR-SWEEP"); (6) J. E. O'Brien, Telegraphing in Battle (1910),
IA `telegraphinginba00obri`, prints Richard O'Brien's diary Feb-Mar 1865 -- read it for every O'Brien / Wilmington / Army of the James entry; Plum, Military
Telegraph vols 1-2 on IA; (7) **a verifier stops at 80% of its cap even mid-entry and names the unaudited rest** (FV-L15a ran 65% over cap by running full G3
+ press on every entry after the holder pass); (8) header word "Washington" decoded [Volunteer] in "Maj. Eckert , Washington" rows is a known key slip
(`plain-at: washington#1`, NOTES "## FIX-L15") -- put it in s.5, do not count it as an M against the body.

---

# Wave 1

## FV-L16a, FV-L16b, FV-L16c, FV-L16d (Opus 5.5, first verifiers, separate from every reader; cap $8 each, box 120 min each)
Exactly "## FV-L15a, FV-L15b, FV-L15c, FV-L15d" of .claude/briefs/runs/2026-10-10-acct1-lane-ledger15-jobs.md (FV-FM9a/FV-FM10a method: all-pointer CONTENTdm
clear-copy search FIRST, duplicate diff against every mssEC 18/19/25 entry, OR I-III and ORN by date (1865: OR I/46 pts 1-3, I/47 pts 1-2, ORN I/11-12; 1864:
the OR ser. I parts in print/or_volume_map.tsv, fetch a missing part's _djvu.txt once, <= 2 per verifier), Grant Papers 13/14 per lesson (1), Butler Corr. IV-V
where Butler is a party, the press of the day for any press-shaped dispatch, G3 with decoded phrases, rare-name OR grep, eye-check every graded line on crops
with tools/iiif_lines.py --image), step 0 never a reason for N1, depth per rule 4a / tools/depth_check.py / .claude/briefs/runs/2026-10-08-acct3-depth-bar.md.
Diff the print against the derived reading block (E420 lesson). Reading fixes go in AUDIT s.5 for a FIX job, not into the reading. Order inside each set is by
H count (reading.md "Code-word tokens"); sets are grouped by date so one OR / Grant Papers window serves the set:
- FV-L16a (4-6 Jan 1865, Wilmington fleet): E509 (H14) E511 (H14) E514 (H12) E506 (H8) E508 (H8) E521 (H4). AUDIT.md "## AUDIT (FV-L16a)".
- FV-L16b (7 Jan-8 Feb 1865): E518 (H11, CLEAR-SWEEP NEAR) E527 (H12) E526 (H10) E546 (H10) E553 (H9) E554 (H7). AUDIT.md "## AUDIT (FV-L16b)".
- FV-L16c (22 Feb-18 Mar 1865): E564 (H12) E577 (H11) E566 (H10) E574 (H10) E558 (H7, NEAR) E569 (H7). AUDIT.md "## AUDIT (FV-L16c)".
- FV-L16d (Mar-May 1864, Butler / Bermuda Hundred): E441 (H16) E472 (H12) E442 (H9, NEAR) E473 (H7) E469 (H6) E466 (H4). AUDIT.md "## AUDIT (FV-L16d)".
status.json/SO rows for N3+ only, audit_status "one audit"; depth_check; file_shrink_guard. On N3+ D2+ append WORK-QUEUE `AUD2-LEDGER16-<n>` (a..d -> 1..4;
fetch first, take the next free number if taken), **tagged account-1** (owner-account orchestrator rule, ROOM 10:28 10 Oct: accounts 3 and 4 silent), Opus 5.5,
cap 2.5 per entry, box 30 per entry + 30; name it in ROOM for the orchestrator (owner account). Unit ~1.3 per entry (6 entries = ~7.8; the cap is the stop, at
80% = 6.4 stop starting a new entry). The four never hold one host's token at the same time as each other: take it in turn.

## FIX-L16 (Sonnet 5.5; cap $2.5, box 70 min, no network)
Exactly FIX-L15's method (ledger15 jobs file "## FIX-L15", entry-note mechanism, never hand-edit reading*.md; extend `fixl15_apply.py` or write an idempotent
`fixl16_apply.py`): apply (1) AUDIT.md "## AUDIT (FV-L15m)" s.5 (E550 anna police / An Apple is = Annapolis; E543 tarquinty = necessity; E571 pilot = pilots;
E465 feeble ghost = 10 15 AM; and any other item that section lists) and its N1 header notes; (2) NOTES "## FIX-L15" open lead: `plain-at: washington#1` on the
"Maj. Eckert , Washington" rows E166 E215 E250 E562 E542 E548 E550 -- NOT E546 or E569 (under FV-L16b/c audit now; the FIX after them takes those). Check
each fix is not already applied. decode x3 --write/--check exit 0; status.json/SO: check FV-L15m's entries have no stale row (all N1); NOTES "## FIX-L16 (10
Oct 2026, account 1, for LANE LEDGER-16)"; depth_check; gaps_check; file_shrink_guard on every touched file.

Held for wave 2: FV-L16e on the 1864 Oct-Dec / Mar group (E447 H11, E474 H8, E470 H8, E468 H8, E443 H8, E445 H7, E471 H8, E446 H4, E448 H3), sized by
wave 1's per-entry cost; a FIX on wave 1's s.5.

(14:46 UTC 10 Oct by date -u: wave 1 spawned with source_url: FV-L16a session_01Ls4x34TEjAEr8ze954EVWY, FV-L16b session_01XgoX4dz8k6DR79HqcRypaA, FV-L16c session_01M6B2VzGbp7U241d8wD5Ek4, FV-L16d session_011JePD7wMqLcoFvgxZvAUYt, FIX-L16 session_01GvMLdw368na1CbqhUCw1fZ.)
