# LEDGER.md accepted-history audit (16 Oct 2026, account-4 parent; owner's follow-up 1 to "Close the Learning Loop")

What `tools/ledger_check.py --all` reports behind the baseline line (4803), classified by reading each class against the
rows, so that nothing unresolved is hidden by the baseline. Numbers from `python3 tools/ledger_check.py --all` on commit be2aeb79c.

| Class | Count | What it is | Integrity effect | Disposition |
|---|---|---|---|---|
| Non-standard outcome codes, Sept 2026 rows (lines 230-1115) | 119 (B 51, A 43, C 14, F-rl 5, S/S- 5, B+ 1) | the 24 Sept scout-quality shorthand (A/B/C), two blocked check-solved verdicts coded B, the 24 Sept Salviati S/S- grades, F-rl "failed, rate limit" | outcome unreadable by code; cost readable; all read and tallied by RETRO-2026-09-24d, 25h and 25k at the time | accepted history: recoding 119 four-week-old rows one by one buys nothing a retrospective has not already read; the codes are listed here so no one has to rediscover them |
| Non-standard outcome codes, Oct 2026 rows (lines 2662-4604) | 83 (Y 44, B 19, C 16, A 4) | Y = LANE FAMILY-A2p and LEDGER-14 account-1 rows (10 Oct); C = FV-* verifier confirmations; B = blocked check-solved | outcome unreadable; `progress_metrics` share-D excludes them (counted in its "skipped outcome" line, 325) | **not accepted**: LEDGER-RECODE (account 2, queued 16 Oct, cap 4) recodes each from its own Lesson cell and moves the baseline only when every row after it passes |
| Duplicate session ids: running/done or placeholder pairs | 29 | a "running" or "cap N" row later followed by the done row with the real cost | the running row carries no numeric cost, so totals are not inflated; `progress_metrics` reads prose costs as none | accepted; `learning_metrics.py` keeps the last costed row per id (dedupe) |
| Duplicate session ids: a lane orchestrator's self-ledger row written twice with two costs (V3, G3, N2, R4, B5, V7, GOLD3; lines 429-920) | 7 | the lane closed, ledgered itself, then re-ledgered with its final cost | **cost double-counted by about USD 179** in any naive total (RETRO-2026-09-26c's own warning) | not hidden: `learning_metrics.py` drops the earlier row (keeps the last costed row per id) and prints how much it removed; progress_metrics's week totals still double-count them (a Sept-only effect, about USD 179 of USD 9,533 in W39) |
| Duplicate session ids: the same role written twice | 2 | double-written rows (3654/3655 shape) | about USD 38 double-counted | same handling as above |
| Shifted cost cell | 1 (line 1408) | a "not spawned" row with "-" in Cost and 0 in Outcome | none (a worker that never ran) | accepted |
| Wrong session id (one id on two unrelated rows: 1258 parent 7n and 2345 LANE-ARM-B) | 1 | a copy-paste id | the two rows' costs are both real; only the id is wrong | flagged to the LEDGER-RECODE worker to annotate, not to guess |

Also found by the 16 Oct ledger audit and NOT concealed: 118 status/log rows that are not outcomes (lines 1290-1384, "running",
"done 06:15"), 158 cost cells that are prose ("not visible from account 3" x77, "cap N" x22), 381 rows without a trailing pipe (all
parse), and the header still declares six columns while rows carry eight. None of these changes a count; the metrics tools skip
what they cannot read and print the skipped totals.

What the baseline does: it stops the gate being permanently red so that a NEW bad row after line 4803 is the only thing it
reports; it does not make the old rows right. `--all` prints every one of them on every run that asks.
