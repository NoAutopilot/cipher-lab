# PREREG-MQS-SCOUT (written before any score is computed; 9 Oct 2026, MQS-SCOUT worker, account 4)

Tool job: no target is read or decoded, no target status/key/reading changes. The "controls" are rank tests on
`QUEUE-scores.json`'s 33 scored rows (plus the test row) and date identities. Expected numbers and gates, fixed now:

| # | Test | Expected / gate | Why the null can differ from the known answer |
|---|---|---|---|
| S1 | fr.2988-shaped row (lang pending=2, material 3, key 0, size 3, competition 3, weight prior 2, unread 3, pile 3) | total 47 (FORMULA), rank 1 of 34, gate: rank <= 4 (top decile = ceil(34/10)) | the same row scored with the OLD formula (no pile, lang 0, weight 0) must NOT reach the top decile (null: the rubric change is what moves it, not the row) |
| S2 | same row, active-edition flag set | rank > 4 (flagged rows rank after every unflagged row) | the unflagged copy ranks <= 4, so the flag is the only difference |
| S3 | must not block: top three named rows before (royalist, Wellington, Charles II) | stay in the top five with S1 inserted; their totals unchanged (pile absent = 0) | |
| S4 | must not block: a short named letter with a key lead (Stepney) | same total, same tier (A >= 38, B 28-37, C < 28) before and after | |
| S5 | held-out shape: fr.20506 volume-level "depeches chiffrees" notice, no item list (lang pending 2, material 1, key 0, size 1, competition 3, weight prior 2, unread 3, pile 0 -- est_signs unknown) | not used to set any weight; rank reported whatever it is (unflagged and flagged) | |
| S6 | drift: scout.js total expression == `scout_rubric.FORMULA` | equal | |
| S7 | drift: QUEUE-scores.json stored `formula` == FORMULA | expected to FAIL today (material x2, no unread/pile): recorded as known drift, reported by --rerank, not weakened | |
| C1 | calendar: 21 May 1584 Julian is a Thursday; 4 May 1531 Julian Thursday, 4 May 1530 Wednesday | exact | a wrong calendar or year gives a different weekday, so the check can fail |
| C2 | Julian 15 Jan 1700 = Gregorian 25 Jan 1700 (10 d); Julian 1 Mar 1700 = Gregorian 12 Mar 1700 (11 d) | exact | |
| A1 | prior_work `--item-spec 'shelfmark=BnF fr.2988;folio=38r'` | active-project LEAD row, exit 4 | fr.3413 f.1r (unrelated BnF item) must give no active-project row |

Weights are a declared prior, not fitted: one fr.2988-shaped row cannot fit them. Ceiling check: the row's rank (1 of 34)
is not a near-ceiling accuracy but the margin over the next row (47 vs 46) is one point -- reported, no gain claimed.
